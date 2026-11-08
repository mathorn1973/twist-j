# First pinned Linux replay

NON-CANONICAL / L1 / exposure-disclosed prospective composition check.

pin_commit: 4e448bb3b13c4e8f0338524e7c69ade1c01caf0f
verifier_sha256: fbee888930ac613c517c2ec0b4312c5b7b9860d1e1f21be21e9d12ba03cf0884
command: python3 probes/P-RELATIVE-CONTACT-INDEPENDENT-RELOAD-1/verify.py
platform: Ubuntu 24.04.1 LTS
architecture: x86_64
python: 3.12.3
exit_code: 0
stdout_sha256: 40a71401c28406605aea666a40fec5f773505d3a5b56b82897cdc09ad4c1952c
stdout_bytes: 2807
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-11-03T06:51:44.824167+00:00
completed_utc: 2026-11-03T06:51:48.368675+00:00

All eight scientific source files were fetched through GitHub at the exact
pin and compared byte for byte before the first execution. A fresh Linux
worktree fetched that public pin and independently checked the same eight
SHA-256 values before running. Both worktrees were clean; no scientific
source was changed after the pin.

The command ran with assertions enabled, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0, LC_ALL=C, LANG=C and TZ=UTC. Other inherited PYTHON* and
TWISTJ_* variables were removed. The timeout was 600 seconds. The observed
wall duration was approximately 3.54 seconds; this is operational timing,
not a scientific duration or a performance threshold.

## Pinned source custody

| File | SHA-256 | Bytes |
|---|---|---:|
| CONTRACT.md | `874aa49ce91dcc234ad50b4f218e1078544c72925f3da9e43d012b188f9a86ba` | 13555 |
| PREREG.md | `c91d56f439294489011ddba235248d508a02c480a6db9d8382fdbb95198a3cee` | 9684 |
| PROOF.md | `b9bdfce2b21eec6f11bb3c0f8a09469919fc7122356876bf30b4edcf59b30ef2` | 13049 |
| PROVENANCE.md | `9015092e6a0b77304c9ed176cf799908008fe8c272675c79ac357868a09b3b30` | 2357 |
| SOURCE-MAP.md | `4eec327b22fcfefd9c4c6827bfc0938d591287be26e9c39e2ca4f7bb66493357` | 2634 |
| SOURCES.tsv | `958e743330be3d48de779ffc59a2cb09a2a1295d4789a0efaea9e46c80dad154` | 3411 |
| WORD535.txt | `ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b` | 4877 |
| verify.py | `fbee888930ac613c517c2ec0b4312c5b7b9860d1e1f21be21e9d12ba03cf0884` | 23140 |

This record describes the first local x86_64 execution only. The required
GitHub x86_64 and aarch64 jobs replay the same verifier against these exact
EXPECTED.txt bytes. Their actual outcomes and head are on the pull request;
this local record does not claim their results in advance. No independent
mathematical verdict is represented by the arithmetic crosscheck.
