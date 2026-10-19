<!-- GLITCHBYTE-UPLOAD-DOOR:START -->
<div align="right"><a href="https://github.com/Hellfire13666/glitchbyte-phantom-labs-releases/upload/main" title="Upload release files"><img alt="UPLOAD FILES" src="https://img.shields.io/badge/UPLOAD-FILES-7850E8?style=flat-square&logo=github&logoColor=white"></a></div>
<!-- GLITCHBYTE-UPLOAD-DOOR:END -->

<div align="center">

![Phantom Vault artwork](https://raw.githubusercontent.com/Hellfire13666/glitchbyte-phantom-labs/main/artwork/vaultlab.png)

# 🔐 GLITCHBYTE PHANTOM VAULT
### The verified safety archive of Phantom Labs

**“Build it. Test it. Archive it. Verify it. Protect the original.”**

</div>

## 🚪 Instant Vault doors

| Destination | Open |
| --- | --- |
| 📦 **Latest verified backup index** | [snapshots/latest.json](snapshots/latest.json) |
| 🗃️ **Versioned backup ZIP archives** | [Browse all snapshots](snapshots/) |
| 🔏 **SHA-256 checksums** | [SHA256SUMS.txt](snapshots/SHA256SUMS.txt) |
| 🧭 **Restore and verify instructions** | [Recovery guide](docs/RESTORE_GUIDE.md) |
| 🗂️ **Find any of the 24 tools** | [Tool-by-tool recovery index](docs/TOOL_RECOVERY_INDEX.md) |
| ⚙️ **Back up now / Actions log** | [Run Phantom Vault Versioned Backups](https://github.com/Hellfire13666/glitchbyte-phantom-labs-releases/actions/workflows/vault-backup.yml) |
| 📤 **Direct Vault upload door** | [Upload files](https://github.com/Hellfire13666/glitchbyte-phantom-labs-releases/upload/main) |

**Archive status:** An archive is confirmed only when its ZIP, JSON file manifest, and checksum can be found under `snapshots/` and verified successfully. If those files are absent, a workflow or README alone is **not** a completed backup.

## 📦 Latest verified recovery set (October 19, 2026 UTC)

| Backup | Download / inspect | Complete manifest |
| --- | --- | --- |
| 👻 **Phantom Labs HQ** · 109 files, including 6 published images | [📥 Full archive ZIP](snapshots/2026-10-19/glitchbyte-phantom-labs-148ff3c454bf.zip) | [SHA-256 file manifest](snapshots/2026-10-19/glitchbyte-phantom-labs-148ff3c454bf.manifest.json) |
| ⚡ **RosieRiot Overdrive** · 14 files, including 4 images and its original ZIP | [📥 Full archive ZIP](snapshots/2026-10-19/rosieriot-overdrive-2026-521b7c53599c.zip) | [SHA-256 file manifest](snapshots/2026-10-19/rosieriot-overdrive-2026-521b7c53599c.manifest.json) |

**Checksums passed:** [View the two matching SHA-256 digests](snapshots/SHA256SUMS.txt). [View successful GitHub backup run](https://github.com/Hellfire13666/glitchbyte-phantom-labs-releases/actions/runs/39183929281).

These links identify the first confirmed version. When the source repositories change, use [latest.json](snapshots/latest.json) to find the newest verified backups.

## What is preserved

- **Phantom Labs Headquarters:** all currently committed tool source, test scripts, lab and tool READMEs, images, and existing project files
- **RosieRiot Overdrive:** complete committed repository including original release ZIP, Python installer, demos, banner, icon, and docs

Each version records the exact Git source commit, tracked-file list, per-file SHA-256 hashes, archive checksum, archive ZIP integrity result, and a dated recovery location.

**Public-repository boundary:** The Vault only archives already-public, committed source files. It does not store credentials, unpublished artwork, private reports, or local uncommitted changes. Keep a separate trusted offline backup, too.

## 🧭 GLITCHBYTE LAB DOORS

| Destination | Open lab | Upload files |
| --- | --- | --- |
| 👻 Phantom Labs HQ | [Headquarters](https://github.com/Hellfire13666/glitchbyte-phantom-labs) | [📤 HQ door](https://github.com/Hellfire13666/glitchbyte-phantom-labs/upload/main) |
| 🌱 Cultivation Room | [Building laboratory](https://github.com/Hellfire13666/glitchbyte-phantom-labs/blob/main/docs/CULTIVATION_ROOM.md) | [📤 Cultivation door](https://github.com/Hellfire13666/glitchbyte-phantom-labs/upload/main) |
| ⚡ RosieRiot Overdrive | [Tool repository](https://github.com/Hellfire13666/rosieriot-overdrive-2026) | [📤 Overdrive door](https://github.com/Hellfire13666/rosieriot-overdrive-2026/upload/main) |
| 🔐 Phantom Vault | [Backup repository](https://github.com/Hellfire13666/glitchbyte-phantom-labs-releases) | [📤 Vault door](https://github.com/Hellfire13666/glitchbyte-phantom-labs-releases/upload/main) |

The Cultivation Room is part of Headquarters, not a separate source repository. Every standalone future tool repo must be added explicitly to the snapshot allowlist before its files are protected.

**GlitchByte Phantom Labs • Official versioned source and artwork safety zone**
