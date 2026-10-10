# First pinned execution

**PUBLIC, NON-CANONICAL. Neutral execution custody.**

```text
pin_commit: f32f24e6e9ee85d1a9f8839ce314d3d0eb1fbe6c
verifier_sha256: 0e3d5e97e80f07957fce7d15b540780f2b721127d3b700e7ad9f8d81886f3e2f
command: python3 probes/P-U-OCCUPIED-SUM-COVARIANT-CONTACT-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 2983e2d3dd647ace8f10beea79c4fe2df3315f4f14b0bc6813acca6f9ea31e65
stdout_bytes: 840
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

First execution started at 2026-10-10T10:09:19.150615+00:00 and completed at
2026-10-10T10:09:20.692244+00:00. Both timestamps are UTC.
The exact pin was fetched from the public branch into a clean detached
checkout before execution. All six immutable public files were first read
back from their full-commit raw URLs and compared byte for byte.
No earlier execution of either newly written scientific program occurred.

The local command ran on Linux with `LC_ALL=C`, `LANG=C`, `TZ=UTC`,
`PYTHONHASHSEED=0` and `PYTHONDONTWRITEBYTECODE=1`. The fixed whole-command
limit was 600 seconds; the frozen wrapper allows each child 240 seconds.
The worktree remained clean, and all six file hashes remained unchanged.
Exact stdout and stderr were retained by the local custody runner;
EXPECTED.txt is a byte copy of that stdout, not a reconstructed report.

## Immutable input custody

| File | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 12278 | `cffe55f1f8a89b37bf65b0796ac2aaa18380096c0f7a7e7dc20650878df0144c` |
| PROOF.md | 16345 | `1172f643c544ecb40fd7880b1b26e98cf036a0b52d9e8747d7ca3c441ac0966a` |
| REVIEW.md | 13966 | `3dae33b1118d11ab5e98121f006a4371ecb065a2fbad80a295a1d178c69d4ece` |
| independent.py | 10486 | `6ad152ea9b871580e5b76034245585623162d0bb182bf089eb7a37577da4b228` |
| primary.py | 12911 | `439cd7c2a8a774204a07d8af3271d8ffb106398e5751559671b60211ae95195e` |
| verify.py | 3996 | `0e3d5e97e80f07957fce7d15b540780f2b721127d3b700e7ad9f8d81886f3e2f` |

The wrapper itself checks the first five input hashes before running the
two programs. Their complete 21-field canonical reports agreed byte for
byte; the wrapper emitted the one-line report retained as EXPECTED.txt.

This is the first local x86_64 run, not a two-architecture certificate.
Required GitHub x86_64 and aarch64 jobs must replay these same pinned
inputs and compare against this exact EXPECTED.txt. Their successful
aggregate is the separate public acceptance gate.
