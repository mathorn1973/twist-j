# Independent exact audit run

PUBLIC, NON-CANONICAL. One x86_64 run of an independently written proof/audit.
No author Stage-C implementation exposure preceded this source freeze or run.

Candidate specification: `0ca0605bee475ed3ab86f9a7c1129ea00a09d86d`.
Independent source pin: `79d4d3ece7e473921e96634facdf8653e210a9b3`.
All three source blobs were publicly read back before execution. The run used
an exact clean checkout with its own Git metadata under Linux.

```text
python3 notes/C-FIELD-J-LOCAL-INSTRUMENT-REVIEW-N/break.py
```

Date (UTC): 2026-10-01. Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12.
Environment: `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.
External timeout: 600 seconds. Elapsed: 18.102 seconds. Exit: 0.
Stderr: 0 bytes, SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 8504 | `6fe31e9b201b94c73c776bf56fe7818ee936e7b782599cd982dda2eaead0abaf` |
| PROOF.md | 13176 | `1c6678934307fe53d2cdb5ba193777fc9cf00c9e79b2cbb682214b68576f3ae3` |
| break.py | 28097 | `da26e40b9bbfd2534d0bc3e530d88fa505d9143d0d0c9542bb0e4493aeea69fd` |
| EXPECTED.txt, exact stdout | 816 | `49bc7306bedebd523a7cfa7f886e4ab854c631cb7e7a31045f7bd4f4339b13b7` |

PASS: 28128 local reaction cases, 432 dirty whole states, 111744 clean
steps, 2448 raw control steps; 677448 pointer coefficients, 356766
translations and 882720 pointer-operator partition cases; 3006152 append
basis cases; 1111 history branches, 17776 source-unit cases and 2048 coherent
cross-unit pairs. The independent finite-span dimensions for E/E, E/O and
E/plus are 56,112,116. EXPECTED.txt preserves the exact deterministic output.

This audits the independent proof at its frozen conditional L1 scope.
Finite execution does not establish universal claims by extrapolation.
It is not an author replay, a scientific second-architecture run or a
physical occurrence test. Notes-only CI does not execute this program.
The source remains frozen; final comparison is recorded separately in REVIEW.md.
