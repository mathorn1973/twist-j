# P-A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS-1 run record

pin_commit: c09e7c199046af7cd077cd009e1c8a210cd9fa57
verifier_sha256: a1a93f0fb981fdb30a42a532c1b190e9e06d74d9dd9ccc529ff0995aaf7af7b2
command: python3 probes/P-A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: 7592228e4db30ae0a2f07c1ea877c61a15de2aa2cffb17d4dc8cfca4a2e88d69
stdout_bytes: 318
stdout_lines: 6
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

Status: completed local formal run.
Date: 2026-09-07.
Public lock: #875.

## Immutable public pin

The pin commit above contains PREREG.md, PROOF.md and verify.py before first
execution. GitHub readback blob SHAs at that commit were:

```text
PREREG.md  14a33f24252fc02a38a63585f15da7a08b6d5cd8
PROOF.md   442915bccdb696d6c272086433204b2b4abc6fec
verify.py  e7326179c6fd4a2f712705d0d11f194db6ecfbdb
```

The local verifier file was reconstructed from GitHub readback and checked
with `git hash-object` before execution. Its Git blob SHA matched the public
readback exactly.

## Environment controls

```text
LC_ALL=C
LANG=C
TZ=UTC
PYTHONHASHSEED=0
PYTHONDONTWRITEBYTECODE=1
```

Local elapsed witness: 2.63 s. Exact assertions: 85517.

The committed EXPECTED.txt is the exact 318-byte stdout. No line-ending
normalization is part of the scientific comparison.

## Gate state

This local x86_64 run is one formal reproduction lane. It does not alone
satisfy the two-architecture computation gate. The pull-request workflow must
run the same pinned verifier on clean GitHub x86_64 and aarch64 jobs and both
must match the committed EXPECTED.txt byte for byte with empty stderr.

The theorem claim rests on PROOF.md. The verifier is an audit of the proof's
frozen consequences and controls.