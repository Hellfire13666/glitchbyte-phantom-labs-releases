#!/usr/bin/env python3
"""Archive explicitly approved public GitHub release installers into Phantom Vault.

No local report discovery, private repository access, or unsafe auto-upload.
"""
from __future__ import annotations
import hashlib
import io
import json
import re
import urllib.request
import zipfile
from pathlib import Path

REGISTRY = Path('docs/INSTALLER_VAULT_REGISTRY.json')
VAULT = Path('installers')
MAX_DOWNLOAD_BYTES = 90 * 1024 * 1024


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def atom(value: object) -> str:
    if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{0,119}', value) or value in {'.', '..'}:
        raise ValueError('Invalid safe path component')
    return value


def validate(item: object) -> dict:
    if not isinstance(item, dict):
        raise ValueError('Registry entry must be a JSON object')
    expected = {'slug', 'version', 'repo', 'tag', 'archive', 'checksum', 'archive_sha256', 'checksum_sha256'}
    if set(item) != expected:
        raise ValueError('Registry entry keys do not match schema')
    v = {key: item[key] for key in expected}
    for key in ('slug', 'version', 'tag', 'archive', 'checksum'):
        atom(v[key])
    if not isinstance(v['repo'], str) or not re.fullmatch(r'Hellfire13666/[A-Za-z0-9][A-Za-z0-9._-]{0,99}', v['repo']):
        raise ValueError('Only explicitly registered owner GitHub release repos permitted')
    if not v['archive'].endswith('.zip') or not v['checksum'].endswith('.sha256'):
        raise ValueError('Release ZIP and .sha256 assets required')
    if v['archive'] == v['checksum']:
        raise ValueError('Asset names must be distinct')
    for key in ('archive_sha256', 'checksum_sha256'):
        if not isinstance(v[key], str) or not re.fullmatch(r'[0-9a-f]{64}', v[key]):
            raise ValueError('Pinned SHA-256 missing/invalid')
    return v


def verify_data(entry: dict, archive: bytes, checksum: bytes) -> None:
    if digest(archive) != entry['archive_sha256'] or digest(checksum) != entry['checksum_sha256']:
        raise ValueError('Release asset SHA-256 mismatch')
    expected_line = f"{entry['archive_sha256']}  {entry['archive']}"
    lines = checksum.decode('utf-8').strip().splitlines()
    if lines != [expected_line]:
        raise ValueError('Release checksum file does not match registered archive')
    with zipfile.ZipFile(io.BytesIO(archive)) as z:
        if not z.infolist() or z.testzip() is not None:
            raise ValueError('Empty or corrupt ZIP')


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={'User-Agent': 'GlitchByte-Phantom-Vault-Installer-Backup/1.0'})
    with urllib.request.urlopen(req, timeout=75) as response:
        if not response.geturl().startswith('https://'):
            raise ValueError('Release download redirected off HTTPS')
        data = response.read(MAX_DOWNLOAD_BYTES + 1)
    if len(data) > MAX_DOWNLOAD_BYTES:
        raise ValueError('Release asset exceeds 90 MiB guard')
    return data


def mirror(entry: dict, vault: Path, downloader=fetch) -> str:
    folder = vault / entry['slug'] / entry['version']
    archive_path = folder / entry['archive']
    checksum_path = folder / entry['checksum']
    if folder.exists():
        if not archive_path.is_file() or not checksum_path.is_file() or folder.is_symlink() or archive_path.is_symlink() or checksum_path.is_symlink():
            raise ValueError(f'Incomplete or unsafe existing archive: {folder}')
        verify_data(entry, archive_path.read_bytes(), checksum_path.read_bytes())
        return 'PRESERVED'
    base = f"https://github.com/{entry['repo']}/releases/download/{entry['tag']}"
    archive = downloader(f"{base}/{entry['archive']}")
    checksum = downloader(f"{base}/{entry['checksum']}")
    verify_data(entry, archive, checksum)
    folder.mkdir(parents=True, exist_ok=False)
    with archive_path.open('xb') as file:
        file.write(archive)
    with checksum_path.open('xb') as file:
        file.write(checksum)
    return 'ARCHIVED'


def run(registry: Path = REGISTRY, vault: Path = VAULT, downloader=fetch) -> list[dict]:
    payload = json.loads(registry.read_text(encoding='utf-8'))
    if payload.get('schema_version') != 1 or not isinstance(payload.get('approved_public_releases'), list) or set(payload) != {'schema_version', 'approved_public_releases'}:
        raise ValueError('Invalid installer vault registry format')
    entries = [validate(x) for x in payload['approved_public_releases']]
    names = [(x['slug'], x['version']) for x in entries]
    if len(names) != len(set(names)):
        raise ValueError('Duplicate slug/version in registry')
    results = []
    for entry in entries:
        status = mirror(entry, vault, downloader)
        results.append({**entry, 'status': status})
        print(f"[PASS] {entry['slug']} {entry['version']}: {status}")
    vault.mkdir(exist_ok=True)
    index = {'schema_version': 1, 'archives': [{k: v for k, v in x.items() if k != 'status'} for x in results]}
    (vault / 'index.json').write_text(json.dumps(index, sort_keys=True, indent=2) + '\n', encoding='utf-8')
    lines = [f"{x['archive_sha256']}  {x['slug']}/{x['version']}/{x['archive']}" for x in results]
    lines += [f"{x['checksum_sha256']}  {x['slug']}/{x['version']}/{x['checksum']}" for x in results]
    (vault / 'SHA256SUMS.txt').write_text('\n'.join(sorted(lines)) + '\n', encoding='utf-8')
    return results


if __name__ == '__main__':
    run()
