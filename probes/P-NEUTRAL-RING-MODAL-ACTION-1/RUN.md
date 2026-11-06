# First pinned Linux run

NON-CANONICAL / L1 / exact arithmetic audit.

pin_commit: 6c0520e77d5bdb98a3e3834977b27c442ec63651
verifier_sha256: 20c8a2ee4d3506842e968e67f8ee4ea3c4abe18691f2c4b1856c8013381968fd
command: python3 probes/P-NEUTRAL-RING-MODAL-ACTION-1/verify.py
platform: Ubuntu 22.04.5 LTS, Linux WSL2
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 929ae0e43a5c286c5eaf600869b434161ecfd38ef81a3a46649f8c7d2f151e52
stdout_bytes: 311
stdout_lines: 7
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

All seven immutable sources were publicly read back byte for byte before
the first execution. A clean Linux clone fetched the exact pin, verified
all seven hashes, and remained clean after the run. This was the first
scientific execution of this probe; no failed attempt or retry occurred.
The accepted sources and thresholds remained unchanged.

Assertions were enabled. The environment set LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC, and removed
PYTHONOPTIMIZE, PYTHONIOENCODING, PYTHONUNBUFFERED and TWISTJ_EVIDENCE_DIR.
The unchanged execution limit was 600 seconds. The measured wall duration
was approximately 0.823 seconds, operational metadata rather than physical time.

## Pinned source custody

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| ACTION.md | 9152 | `cb75033acbcd5d792579fa174fff3bee147371674a1de931a629fba4740161ad` |
| ENERGY.md | 10576 | `33878ad81ebbf2580e14692d1684550051c1edcd1c6d951d322656830142852c` |
| PREREG.md | 8170 | `739d42f53f4856f4ad45de6da7a5d558833d0142d87d311a067fad8c2a59216e` |
| PROVENANCE.md | 2292 | `9221c98bda340dac8f9711f5872cbb672599ede64ed200f7f6fcc8ff8b54eee6` |
| README.md | 2167 | `6115b2cdc2e14190ffcb359cd8919f222155e6532d3bc0dbdd0eed934fa236f7` |
| SOURCES.tsv | 1973 | `922cd9d7dd5dbb79e30ca687ec59f7e71699d2bb72c21a2c22bef625020f409b` |
| verify.py | 19285 | `20c8a2ee4d3506842e968e67f8ee4ea3c4abe18691f2c4b1856c8013381968fd` |

This records the actual author Linux x86_64 run. Required GitHub x86_64
and aarch64 results are reported only after the relevant jobs complete.
Same-session static review does not constitute independent acceptance.
