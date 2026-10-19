#!/usr/bin/env python3
"""Create complete, versioned GitHub source snapshots with SHA-256 evidence.

Source repositories are public and explicitly allowlisted. All tracked files
are included, including existing ZIPs, PNGs and source documentation.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import zipfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
SOURCES = (
    "glitchbyte-phantom-labs",
    "rosieriot-overdrive-2026",
)
OWNER = "Hellfire13666"


def run(*args: str, cwd: Path | None = None) -> bytes:
    return subprocess.check_output(args, cwd=cwd, stderr=subprocess.STDOUT)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            h.update(chunk)
    return h.hexdigest()


def json_write(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    date_dir = ROOT / "snapshots" / stamp
    latest = ROOT / "snapshots" / "latest.json"
    previous = json.loads(latest.read_text(encoding="utf-8")) if latest.is_file() else {}
    previous_items = {x["repository"].split("/")[-1]: x for x in previous.get("backups", [])}
    jobs = []

    with tempfile.TemporaryDirectory(prefix="phantom-vault-") as temp:
        for name in SOURCES:
            checkout = Path(temp) / name
            repo_url = f"https://github.com/{OWNER}/{name}.git"
            run("git", "clone", "--depth", "1", "--branch", "main", "--", repo_url, str(checkout))
            commit = run("git", "rev-parse", "HEAD", cwd=checkout).decode("ascii").strip()
            paths = [x.decode("utf-8") for x in run("git", "ls-files", "-z", cwd=checkout).split(b"\0") if x]

            archive_name = f"{name}-{commit[:12]}.zip"
            archive_path = date_dir / archive_name
            manifest_path = date_dir / f"{name}-{commit[:12]}.manifest.json"
            past = previous_items.get(name)
            if past and past.get("source_commit") == commit:
                existing_archive = ROOT / past["archive_path"]
                existing_manifest = ROOT / past["manifest_path"]
                if existing_archive.is_file() and existing_manifest.is_file() and sha256(existing_archive) == past.get("archive_sha256"):
                    jobs.append(past)
                    print(f"Unchanged and verified: {name} at {commit[:12]}")
                    continue

            date_dir.mkdir(parents=True, exist_ok=True)
            file_info = []
            with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as archive:
                for relpath in sorted(paths):
                    src = checkout / relpath
                    if not src.is_file():
                        raise RuntimeError(f"Tracked file missing or not regular: {name}/{relpath}")
                    file_info.append({"path": relpath, "size": src.stat().st_size, "sha256": sha256(src)})
                    archive.write(src, arcname=f"{name}/{relpath}")

            with zipfile.ZipFile(archive_path, "r") as archive:
                corrupt = archive.testzip()
                if corrupt:
                    raise RuntimeError(f"Damaged ZIP entry: {corrupt}")
                stored = archive.namelist()
                if len(stored) != len(paths):
                    raise RuntimeError(f"ZIP file count mismatch for {name}")

            digest = sha256(archive_path)
            entry = {
                "repository": f"{OWNER}/{name}",
                "source_commit": commit,
                "source_url": f"https://github.com/{OWNER}/{name}/tree/{commit}",
                "archive_path": archive_path.relative_to(ROOT).as_posix(),
                "archive_sha256": digest,
                "manifest_path": manifest_path.relative_to(ROOT).as_posix(),
                "file_count": len(file_info),
            }
            json_write(manifest_path, {
                **entry,
                "format": "full tracked-file snapshot",
                "generated_utc": datetime.now(timezone.utc).isoformat(),
                "source_files": file_info,
            })
            jobs.append(entry)
            print(f"Verified {name}: {len(file_info)} files, sha256 {digest[:16]}…")

    # Include all archives (new and previously current), each with an exact checksum.
    all_current = [ROOT / x["archive_path"] for x in jobs]
    sums = ROOT / "snapshots" / "SHA256SUMS.txt"
    sums.parent.mkdir(parents=True, exist_ok=True)
    sums.write_text(
        "".join(f"{sha256(p)}  {p.relative_to(sums.parent).as_posix()}\n" for p in all_current),
        encoding="utf-8",
    )
    latest_value = {
        "schema_version": 1,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "backups": jobs,
        "checksum_file": sums.relative_to(ROOT).as_posix(),
        "notice": "Only committed, public GitHub files are covered; keep a second copy offline.",
    }
    json_write(latest, latest_value)

    for entry in jobs:
        archive = ROOT / entry["archive_path"]
        if sha256(archive) != entry["archive_sha256"]:
            raise RuntimeError(f"Checksum verification failed for {archive}")
    print("PASS: Current Vault archives, per-file manifests, and SHA256SUMS verified.")


if __name__ == "__main__":
    main()
