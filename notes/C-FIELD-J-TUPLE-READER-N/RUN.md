# Tuple-reader author audit

PUBLIC, NON-CANONICAL. One x86_64 finite audit, not independent review.

Specification pin: `cba479dcc05fbcadec70007a5a8642547372c1f2`.
Complete source pin: `4fde4fa50409d5df16fd4b210880044a87eb7a2f`.
All three public source blobs matched before execution. Exact clean checkout.

```text
python3 notes/C-FIELD-J-TUPLE-READER-N/verify.py
```

Date: 2026-10-01. Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12.
Environment: `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.
Timeout: 600 seconds. Elapsed subprocess: 1.461 seconds. Exit: 0.
Stderr: 0 bytes, SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 10345 | `bfa94e9b5d471f65fe3243e2abde2837a40247f0518c09677e6d0fbf31752fb4` |
| PROOF.md | 8321 | `befa36a9cbf04a9f1bda0e3bbb6c7d9c4b58d81466576d649c1e89283f34944d` |
| verify.py | 11334 | `8481877b0582c915340e0d3e2d2262a3345c71b4709849196f7a19d7e10ba818` |
| EXPECTED.txt, exact stdout | 520 | `ceabad71746b75eb2c5af737d6f97f3697e155d8e67fdb8b0c807c39bee6597f` |

All preregistered finite checks passed, including 472500 bounded-key reader
calls, 168750 outside-key calls, 147 malformed fixtures, original regression
counterexamples, hostile/lying views and unchanged metadata. The proof, not
this finite subclass sample, supplies the universal carrier argument.

This successor result does not change the predecessor's REJECT disposition.
No second-architecture execution is claimed. Notes-only CI does not execute
this candidate verifier automatically. Independent acceptance is recorded
separately in RESULT.md only after the fresh review completes.
