# 🔐 Phantom Vault | Verified Recovery Guide

> **Backup status is only confirmed when `snapshots/latest.json`, the referenced ZIP files, and SHA-256 hashes exist and pass validation.** A workflow definition alone is not an archive.

## What the Vault protects

The versioned backup job snapshots **every tracked file**, including source code, README pages, tool examples, test files, existing release ZIPs, and PNG artwork, from these public repositories:

1. [GlitchByte Phantom Labs Headquarters](https://github.com/Hellfire13666/glitchbyte-phantom-labs)
2. [RosieRiot Overdrive](https://github.com/Hellfire13666/rosieriot-overdrive-2026)

Snapshots include only files committed to GitHub. Uncommitted changes, local-only scripts, credentials, private reports, and unpublished chat artwork **are not backed up**. Never store credentials, personal data, or private reconnaissance results in this public Vault.

## Find an archive

1. Open [Latest backup index](../snapshots/latest.json) and read each `source_commit`, `archive_path`, and `sha256`.
2. Open [snapshots folder](../snapshots/) and choose the corresponding date/version.
3. Download the ZIP and its associated `.manifest.json`, plus `SHA256SUMS.txt` from the same dated folder.
4. Keep a **second offline copy** of the downloads on trusted storage. GitHub alone is not an independent backup.

## Verify SHA-256 checksums (Ubuntu/Linux)

Download `snapshots/SHA256SUMS.txt` and the ZIP files in their **original dated subfolders**. From the folder containing `SHA256SUMS.txt`, run:

```bash
cd "$HOME/Downloads/snapshots"
sha256sum -c SHA256SUMS.txt
```

Each listed archive should report `OK`. A missing file produces a warning; a mismatched checksum means **do not restore** until you obtain a verified copy.

Optionally verify archive integrity:

```bash
unzip -t 2026-10-18/glitchbyte-phantom-labs-REPLACE_WITH_SHA_PREFIX.zip
unzip -t 2026-10-18/rosieriot-overdrive-2026-REPLACE_WITH_SHA_PREFIX.zip
```

## Recover safely

Never unpack untrusted archives on top of production tools without reviewing their contents first.

```bash
mkdir -p "$HOME/PhantomLabsRecovered"
unzip -n 2026-10-18/glitchbyte-phantom-labs-REPLACE_WITH_SHA_PREFIX.zip -d "$HOME/PhantomLabsRecovered"
unzip -n 2026-10-18/rosieriot-overdrive-2026-REPLACE_WITH_SHA_PREFIX.zip -d "$HOME/PhantomLabsRecovered"
find "$HOME/PhantomLabsRecovered" -maxdepth 2 -type f | head -40
```

Each archive preserves the repository directory name and original relative paths. These recovered files are **source snapshots**, not proof the software was tested or installed. Run the relevant offline verification commands from each project's README.

## Update or re-run the backup

Open [Phantom Vault backup workflow](../.github/workflows/vault-backup.yml). From the repository's **Actions** tab, choose **Phantom Vault Versioned Backups** then **Run workflow**. The backup also checks daily for changes in the two public source repositories and only adds a new version if source commits differ from the latest completed snapshot.

If the workflow cannot push (for example, repository Actions policy restricts write tokens), check the workflow's error log and update the repository's Actions permissions. Do not claim a completed archive until a snapshot ZIP and checksum file can be verified.

## Understanding the manifest

- `source_commit` is the exact Git commit preserved.
- `source_files` lists every included tracked file with its own SHA-256 and byte size.
- `archive_sha256` is a checksum for the entire final ZIP.
- `snapshots/latest.json` points to the most recent verified version and should contain no secrets.

**Build it. Test it. Archive it. Verify it. Protect the original.**
