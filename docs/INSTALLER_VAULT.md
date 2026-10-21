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

## ✅ HEXBAZAAR Live Command Deck v0.1.0 archived and verified (October 21, 2026)

[Official public GitHub Release](https://github.com/Hellfire13666/hexbazaar-live-command-deck-2026/releases/tag/v0.1.0) · [Independent archived HEXBAZAAR Deck ZIP + checksum](../installers/hexbazaar-live-command-deck/v0.1.0/) · [Successful archive workflow](https://github.com/Hellfire13666/glitchbyte-phantom-labs-releases/actions/runs/39674856072).

Both immutable versioned installer files are physically present: `HEXBZ-LIVE-COMMAND-DECK-v0.1.0.zip` (**5,822,079 bytes**, SHA-256 `6439e4cd2b6d275b189a18dfc41a262ddcc62dcd1aa4ffb01b67a25ac9906f78`) and `HEXBZ-LIVE-COMMAND-DECK-v0.1.0.sha256` (SHA-256 `34c328639a1388ab3b93a41469812ea4e1dc78b57517eb5cc453ca5f4af63a8f`). Their pinned digests appear in [Vault SHA256SUMS](../installers/SHA256SUMS.txt) and [index.json](../installers/index.json). Archiver logs confirm offline installer safety tests, release mirroring, digest verification and publication passed. Deck does not bundle the separately installed HEXBAZAAR research engine. Prior Master Hub v0.2.0/v0.3.0 and PHANTOM SPINE v0.2.0 copies remain separate.

## ✅ Master Hub v0.3.0 archived and verified (October 21, 2026)

The actual [GlitchByte Master Hub v0.3.0 public GitHub Release](https://github.com/Hellfire13666/glitchbyte-phantom-labs/releases/tag/master-hub-v0.3.0) is independently preserved in the [separate v0.3.0 Installer Vault folder](../installers/glitchbyte-phantom-labs-master-hub/v0.3.0/). Its ZIP (**4,419,234 bytes**, SHA-256 `49a97d14dd352f2708537bf64981f874a21fa02b86c3550066ff49d32e262580`) and checksum file (SHA-256 `0619cc406cc3de1beefb4e4f6d6a7207839970f48df33f06e7b7a7d0b3aa31ec`) appear in the [Vault SHA256SUMS](../installers/SHA256SUMS.txt) and [machine-readable catalog](../installers/index.json).

[Installer Vault workflow #39665211599](https://github.com/Hellfire13666/glitchbyte-phantom-labs-releases/actions/runs/39665211599) completed successfully after allowlisted download, offline archive tests, SHA-256 ZIP/checksum validation, integrity checks, and commit of immutable versioned assets. This version includes the owner's exact approved Rosie-and-spine image, permanent PHANTOM SPINE v0.2.0 switch, and real copyable research commands. **Master Hub v0.2.0 and PHANTOM SPINE v0.2.0 remain separate, intact backups.**

## ✅ Master Hub v0.2.0 archived and verified

Official release: [Master Hub v0.2.0](https://github.com/Hellfire13666/glitchbyte-phantom-labs/releases/tag/master-hub-v0.2.0).

Pinned archive SHA-256: `e5b1ef241ab8e3058fae593ecb1ea4fe26d95cdfb9eca1a0e84c656a1025fac7`.

The official ZIP and checksum are **archived under [installers/glitchbyte-phantom-labs-master-hub/v0.2.0](../installers/glitchbyte-phantom-labs-master-hub/v0.2.0/)**. The [GitHub archiving workflow](https://github.com/Hellfire13666/glitchbyte-phantom-labs-releases/actions/runs/39611133094) passed the offline tests, download/hash verification, ZIP validation, and publish steps. The two actual files (ZIP 981,915 bytes and checksum 112 bytes) appear in the Vault's [installer hash manifest](../installers/SHA256SUMS.txt).

The **earlier PHANTOM SPINE Visual Portal** is a different, locally distributed historical candidate and was not archived by this release. The fully published **PHANTOM SPINE Live Signal v0.2.0**, including its exact approved Rosie artwork, has its own independently verified archived ZIP below.

## ✅ PHANTOM SPINE Live Signal v0.2.0 archived and verified

Official public GitHub release: [PHANTOM SPINE v0.2.0](https://github.com/Hellfire13666/phantom-spine-live-signal-2026/releases/tag/v0.2.0). This includes the owner-approved Rosie-and-spine public artwork, real DNS public-source intelligence interface, separately installed HEXBAZAAR adapter, and RIFTSEAL SHA-256 evidence bridge.

The exact ZIP and `.sha256` assets are saved separately in [the PHANTOM SPINE v0.2.0 Installer Vault folder](../installers/phantom-spine-live-signal/v0.2.0/). **ZIP size:** 3,758,458 bytes; **ZIP SHA-256:** `946262cad583f4a22d82091a805da089b6ef68c16815316772f45fb51e87a4f7`; **checksum-file SHA-256:** `055eee08c6ec473ab14cd79f88a25c53b7f7a0b2da768a6b7c2653bb9be06e9d`. The [successful approved installer archiving run](https://github.com/Hellfire13666/glitchbyte-phantom-labs-releases/actions/runs/39650838678) verified both files' hashes and ZIP contents before publication; [SHA256SUMS.txt](../installers/SHA256SUMS.txt) and [index.json](../installers/index.json) list the backup.

The separately approved **old PHANTOM SPINE Visual Portal candidate** is not this v0.2.0 official release. Public publication and Vault mirroring were completed only for the exact version/asset pair listed here. Older backups are retained.

### Safe restore

In the Vault repository, find a specific version in `installers/index.json`; download that ZIP and accompanying checksum file and verify their hashes. Extract to a **new** directory, never over the user's working tool folder without review. The original installation and pinned desktop shortcuts stay unchanged.
