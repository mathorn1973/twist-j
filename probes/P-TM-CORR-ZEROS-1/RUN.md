# P-TM-CORR-ZEROS-1 first formal run

Date: 2026-08-30

```text
RUN STATE:            FIRST FORMAL RUN / X86_64 ONLY
PUBLIC PIN:           f594c8ddd39e63432ac58026dd402b756f4893ad
PIN BASE:             7f4c102e27e7b2ebdf5ca9215db5c5ab846ebbe2
PREREG SHA-256:       fc92c07cb17670872cde748d52ddf8b3b11b8e0f35ea0f20a84ffd45b8740d9b
VERIFIER SHA-256:     a4f95475eb4b859c83b0e38256d3b9d5bc92772d6e06a57ad620ef50220a7861
ARCHITECTURE:         x86_64
PYTHON:               3.12.13
EXIT CODE:            0
STDOUT BYTES:         901
STDOUT SHA-256:       355eb61bb6fac32e3346fd4e0e76bbf6034eb9d15b372f27d1cbef91050845be
STDERR BYTES:         0
DECISION:             PROOF-SURVIVES / 7 OF 7 PASS
AARCH64 REPLAY:       PENDING
SCIENTIFIC STATUS:    UNCHANGED
PRIORITY CLAIM:       NONE
```

The public branch and both pin files were read back byte for byte before the
first execution. Issue #694 records the full pin commit, hashes, byte counts,
and successful public readback.

The frozen command environment was:

```text
PATH=/usr/local/bin:/usr/bin:/bin
LC_ALL=C.UTF-8
LANG=C.UTF-8
PYTHONHASHSEED=0
PYTHONIOENCODING=utf-8
python3 probes/P-TM-CORR-ZEROS-1/verify.py
```

The first direct formal run exited 0 and produced exactly the bytes committed
as `EXPECTED.txt`. A same-architecture capture replay, used only to separate
the process streams, again exited 0, produced the same 901-byte stdout with
SHA-256
`355eb61bb6fac32e3346fd4e0e76bbf6034eb9d15b372f27d1cbef91050845be`,
and produced zero stderr bytes.

This record is neutral. It does not create a Canon or Registry row, does not
satisfy the required aarch64 replay, and does not by itself move any
scientific status. The next gate is byte-identical GitHub x86_64 and aarch64
replay of the pinned verifier. No `RESULT.md` exists at this stage.
