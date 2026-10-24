# P-TM-CORR-ZEROS-1 formal run and architecture replay

Date: 2026-08-30

The flat fields below are the machine-readable local record required by
`tools/check_verifier.py`.

```text
pin_commit: f594c8ddd39e63432ac58026dd402b756f4893ad
verifier_sha256: a4f95475eb4b859c83b0e38256d3b9d5bc92772d6e06a57ad620ef50220a7861
command: python3 probes/P-TM-CORR-ZEROS-1/verify.py
platform: Linux
architecture: x86_64
python: 3.12.13
exit_code: 0
stdout_sha256: 355eb61bb6fac32e3346fd4e0e76bbf6034eb9d15b372f27d1cbef91050845be
stdout_bytes: 901
stdout_lines: 16
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

```text
RUN STATE:            FORMAL RUN / TWO-ARCHITECTURE REPLAY COMPLETE
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
AARCH64 REPLAY:       BYTE-IDENTICAL PASS
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

## Repository two-architecture replay

Pull request #696 triggered policy workflow run `33316650855` on evidence
head `9e49b77f8e90f3e35afbe329b6328bf4ff74a13e`. The changed-probe step ran
the pinned verifier independently on both required architectures:

| Architecture | Job | Conclusion | Verifier SHA-256 | Stdout SHA-256 |
| --- | --- | --- | --- | --- |
| x86_64 | `99271221495` | `VERIFY PASS` | `a4f95475eb4b859c83b0e38256d3b9d5bc92772d6e06a57ad620ef50220a7861` | `355eb61bb6fac32e3346fd4e0e76bbf6034eb9d15b372f27d1cbef91050845be` |
| aarch64 | `99271221574` | `VERIFY PASS` | `a4f95475eb4b859c83b0e38256d3b9d5bc92772d6e06a57ad620ef50220a7861` | `355eb61bb6fac32e3346fd4e0e76bbf6034eb9d15b372f27d1cbef91050845be` |

Aggregate job `99271304174` concluded success and emitted
`TWO-ARCHITECTURE CHECK PASS`. The workflow also passed policy, 142 tool
tests, Canon v71, ledger, gate contract, and the unchanged reproduction
checks on both runners.

This record is neutral with respect to the public theory. It completes the
probe's architecture audit but creates no Canon or Registry row and moves no
scientific status. The theorem grade rests on the written proof; the two
architecture jobs reproduce the frozen proof-audit carrier and exact stdout.
