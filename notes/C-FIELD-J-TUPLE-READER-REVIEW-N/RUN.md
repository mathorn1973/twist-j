# Independent tuple reader and author comparison runs

PUBLIC, NON-CANONICAL. Independent finite audits on one architecture.

Independent pre-exposure freeze: `49fe93dd9854f55a1d5aabb8dca62dadd66ea8d4`.
Author source freeze: `4fde4fa50409d5df16fd4b210880044a87eb7a2f`.
Clean common execution pin: `9e2337869174b4a8edba204ea667109e75fb05be`.
All frozen source blobs were publicly read back before comparison; the merge
retains each original file unchanged. Runs were sequential.

```text
python3 notes/C-FIELD-J-TUPLE-READER-REVIEW-N/break.py
python3 notes/C-FIELD-J-TUPLE-READER-REVIEW-N/break.py --candidate notes/C-FIELD-J-TUPLE-READER-N/verify.py --sha256 8481877b0582c915340e0d3e2d2262a3345c71b4709849196f7a19d7e10ba818 --reader decode
```

Date: 2026-10-01. Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12.
Environment: `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.
Per-process timeout: 600 seconds. Each exit code: 0. Each stderr: 0 bytes,
SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| Independent PREREG.md | 7326 | `20a73b15f36b22b2e3c30c2324eda47916c7791bed0dd6f14371e5fd03339684` |
| Independent DERIVATION.md | 6988 | `90ae6ecc28c34d46260375af517b8a3871b50e83bf20afaeb3dda559cf9e63eb` |
| Independent break.py | 14236 | `107f5f861f6da0f07e6bf19f6eb614630f72082630f7871f4820040efa74c197` |
| Author verify.py, hash checked before import | 11334 | `8481877b0582c915340e0d3e2d2262a3345c71b4709849196f7a19d7e10ba818` |
| EXPECTED.txt, independent mode | 161 | `41af9b36f1e02ded4e8a862290cf9712721dd301e40c60dd2efa3531f22ec4a5` |
| EXPECTED-COMPARISON.txt, author comparison mode | 238 | `68523bdf64fa423cf37694dd75c8a3302538a3830fc312692a37e65a19e4defa` |

Elapsed subprocess seconds: 1.465 (independent), 3.363 (comparison).
Both frozen audits passed. The comparison uses the independently frozen
oracle and fixtures unchanged; it adds direct testing of the author's decode
callable. Source proof supplies the all-object conclusion, not the finite
subclass sample. The predecessor's failed contract remains rejected.
Notes-only CI is not a scientific execution or a two-architecture gate.
