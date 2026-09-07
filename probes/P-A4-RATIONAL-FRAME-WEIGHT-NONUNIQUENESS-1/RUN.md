# P-A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS-1 run record

Status: completed local formal run.
Date: 2026-09-07.
Public lock: #875.

## Immutable public pin

Pin commit containing PREREG.md, PROOF.md and verify.py before first execution:

```text
c09e7c199046af7cd077cd009e1c8a210cd9fa57
```

GitHub readback blob SHAs at that commit:

```text
PREREG.md  14a33f24252fc02a38a63585f15da7a08b6d5cd8
PROOF.md   442915bccdb696d6c272086433204b2b4abc6fec
verify.py  e7326179c6fd4a2f712705d0d11f194db6ecfbdb
```

The local verifier file was reconstructed from the GitHub readback and checked
with `git hash-object` before execution. Its Git blob SHA matched
`e7326179c6fd4a2f712705d0d11f194db6ecfbdb` exactly.

Verifier SHA-256:

```text
a1a93f0fb981fdb30a42a532c1b190e9e06d74d9dd9ccc529ff0995aaf7af7b2
```

## Command and environment

Command from a clean temporary root containing only the pinned probe path:

```text
python3 probes/P-A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS-1/verify.py
```

Environment:

```text
platform: Debian GNU/Linux 13
architecture: x86_64
Python: 3.13.5
LC_ALL=C
LANG=C
TZ=UTC
PYTHONHASHSEED=0
PYTHONDONTWRITEBYTECODE=1
```

## Result

```text
exit code: 0
stderr bytes: 0
stdout bytes: 318
elapsed witness: 2.63 s
stdout SHA-256: 7592228e4db30ae0a2f07c1ea877c61a15de2aa2cffb17d4dc8cfca4a2e88d69
empty stderr SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
exact assertions: 85517
```

The committed EXPECTED.txt is the exact 318-byte stdout above. No line-ending
normalization is part of the scientific comparison.

## Gate state

This local x86_64 run is one formal reproduction lane. It does not alone
satisfy the two-architecture computation gate. The pull-request workflow must
run the same pinned verifier on clean GitHub x86_64 and aarch64 jobs and both
must match the committed EXPECTED.txt byte for byte with empty stderr.

The theorem claim rests on PROOF.md. The verifier is an audit of the proof's
frozen consequences and controls.