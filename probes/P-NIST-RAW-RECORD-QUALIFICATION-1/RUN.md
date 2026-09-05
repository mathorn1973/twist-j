# NIST archived record qualification: formal run

```text
pin_commit: dc8abb7e8e5ccaad4ff561776b747801a4d4a373
pin_tree: 7da231e8401c056e7cd0d50951f8c3510cbb824e
base_commit: af2240d0a2c4807fc6a01c0c5c3132a22ace6015
public_lock: https://github.com/mathorn1973/twist-j/issues/836
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/836#issuecomment-5551111031
command: python3 probes/P-NIST-RAW-RECORD-QUALIFICATION-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.3
start_utc: 2026-09-05T10:15:48.657159+00:00
finish_utc: 2026-09-05T10:15:57.179273+00:00
formal_execution_count: 1
child_invocations: 1
capture_complete: true
exit_code: 0
stdout_sha256: ac5edf54c34e40613fc22a55c2423169ac3f8c719ff9472d5c2532b75b135439
stdout_bytes: 32414
stdout_lines: 1324
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
stdout_encoding: ASCII / UTF-8 subset
stdout_line_endings: LF-only; final LF present
verifier_sha256: 0e63ea7ee01bff85558af311c8d819440f7155e34a8582b003929701ee1d4bf7
verifier_bytes: 24560
prereg_sha256: 482a4afd1a9010987c2afca5cb39805b29990b79b7a7b1f3234dc31893328f9c
prereg_bytes: 11503
source_manifest_sha256: 653e5dd17b041ecf38244bcd8312fa724863eb681f940795e38974182f7bbe8a
public_readback: PASS before first semantic payload opening and formal execution
all_pinned_sources_pre_post_match: yes
worktree_clean_before_and_after: yes
result: A QUALIFIED; B ONEHOT; both conditional record claims CONFIRMED
architecture_gate: PENDING public aarch64 and x86_64 replay
```

## Immutable source inventory

| File | SHA-256 | Bytes | Git blob |
|---|---|---:|---|
| `probes/P-NIST-RAW-RECORD-QUALIFICATION-1/PREREG.md` | `482a4afd1a9010987c2afca5cb39805b29990b79b7a7b1f3234dc31893328f9c` | 11503 | `cabedcc1ec0cc73119559e490c48e6729177c6d6` |
| `probes/P-NIST-RAW-RECORD-QUALIFICATION-1/verify.py` | `0e63ea7ee01bff85558af311c8d819440f7155e34a8582b003929701ee1d4bf7` | 24560 | `c9fad32da886b7ce19ece76dfb036dc2e19b9d3d` |
| `probes/P-NIST-RAW-RECORD-QUALIFICATION-1/SOURCE.json` | `653e5dd17b041ecf38244bcd8312fa724863eb681f940795e38974182f7bbe8a` | 4058 | `bcc91d20b63ecf362819a7c78cb380abc3a0167a` |
| `probes/P-NIST-RAW-RECORD-QUALIFICATION-1/README.md` | `c0e6faf1b992369cb10db37347639cefa29157e1e6bbc0608812182a9e0d1b7a` | 1365 | `6ab3f70e09d9be3fd8bd7c058690418017072ea6` |
| `notes/NIST-RAW-CUSTODY-1.md` | `b6d19a283ede826cb41910e80db567f71f95e2cc3258fce2f03e0d1525471ec2` | 5906 | `c13ce4a811c39f5d641f0a229787f785f36e5e37` |

## Execution and custody

The exact public pin was checked out in a fresh, clean Linux clone. The first
formal child ran once from the repository root, with PATH=/usr/bin:/bin,
LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1 and
PYTHONNOUSERSITE=1. A lossless subprocess capture saved exact stdout/stderr and
exit status; the external timeout was 600 seconds. The child completed in
approximately 8.52 seconds. EXPECTED.txt is the unedited 32,414-byte capture.

TWISTJ_NIST_CACHE_DIR pointed to the separate opaque custody directory. Each
complete cached archive was counted and rehashed against SOURCE.json before
ZIP access. The inherited NIST notice accompanies those copies. No local
directory name or cache path affects scientific stdout. Cold public replay
downloads the same pinned bytes and must reproduce the output without this
cache. The repository contains no raw archive or extracted experimental file.

Before the formal pin, only catalogue/documentation, acquisition source code,
opaque transfer counts and cryptographic hashes were known. Neither experimental
nor calibration archive metadata or contents were opened. The public readback
comment predates the first semantic opening; pre- and post-run hashes match.

Both frozen predicates passed on their declared scopes. The two sync members
were read completely with CRC verification; only the nominated prefix of each
run3 member was decoded. The run3 tails remain uninspected by this probe.
All future replays use the same frozen scope. Two-architecture reproduction
and post-result independent review will be recorded after completion; neither
can promote this conditional data audit to physical apparatus certification.
