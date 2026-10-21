# 🌹 GlitchByte Phantom Installer Vault

**Purpose:** preserve separately versioned, SHA-256-verified copies of released installation packages in Phantom Backup HQ. This is independent of the existing **source-code snapshot vault**.

## Rules for every future official tool

1. **Build and test locally.** Do not upload secrets, generated research reports, private databases, private source code, or unreleased artwork.
2. **Publish the reviewed tool release** in its dedicated owner-approved GitHub repository, with a versioned ZIP and SHA-256 file. Do not claim a release is public before both actually exist.
3. **Register its exact public release** in [INSTALLER_VAULT_REGISTRY.json](INSTALLER_VAULT_REGISTRY.json), specifying unique `slug`, `version`, `repo`, `tag`, both asset filenames and **both expected SHA-256 hashes**. Registry edits must be reviewed before merge; no unknown repositories are synced.
4. The [approved installer archiver workflow](../.github/workflows/archive-installers.yml) runs on registry changes, manually, and daily. It downloads *only* registered official release assets over HTTPS, verifies their hashes and the checksum file, tests ZIP integrity, and writes them under `installers/slug/version/`. It refuses to overwrite an existing version.
5. Check the workflow run, the actual files in [installers](../installers/), and their [SHA-256 list](../installers/SHA256SUMS.txt) before marking an archive as present. The workflow creates [index.json](../installers/index.json). A registry entry **alone is not a backup**.
6. Publish a **one-square copy/paste beginner installer** and local desktop shortcut instructions in the tool's README; connect the tool to the Master Hub by a checked card/recipe link, and keep its source repository separate.
7. Keep a second **offline** copy outside GitHub. GitHub in two repositories is useful redundancy, but not an independent off-device backup.

## ✅ Master Hub v0.2.0 archived and verified

Official release: [Master Hub v0.2.0](https://github.com/Hellfire13666/glitchbyte-phantom-labs/releases/tag/master-hub-v0.2.0).

Pinned archive SHA-256: `e5b1ef241ab8e3058fae593ecb1ea4fe26d95cdfb9eca1a0e84c656a1025fac7`.

The official ZIP and checksum are **archived under [installers/glitchbyte-phantom-labs-master-hub/v0.2.0](../installers/glitchbyte-phantom-labs-master-hub/v0.2.0/)**. The [GitHub archiving workflow](https://github.com/Hellfire13666/glitchbyte-phantom-labs-releases/actions/runs/39611133094) passed the offline tests, download/hash verification, ZIP validation, and publish steps. The two actual files (ZIP 981,915 bytes and checksum 112 bytes) appear in the Vault's [installer hash manifest](../installers/SHA256SUMS.txt).

The PHANTOM SPINE Visual Portal is currently a separate local candidate, not a publicly approved release. Do not add it here before its individual publication/privacy/rights checks.

### Safe restore

In the Vault repository, find a specific version in `installers/index.json`; download that ZIP and accompanying checksum file and verify their hashes. Extract to a **new** directory, never over the user's working tool folder without review. The original installation and pinned desktop shortcuts stay unchanged.
