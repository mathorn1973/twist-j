# Author exact audit run

PUBLIC, NON-CANONICAL. One x86_64 author audit of the frozen conditional law.

Specification pin: `0ca0605bee475ed3ab86f9a7c1129ea00a09d86d`.
Complete author source: `61a98eb1732ddf3effff0b386953e2fa7844f15e`.
All source blobs were publicly read back before execution. The run used an
exact clean checkout with its own Git metadata under Linux.

```text
python3 notes/C-FIELD-J-LOCAL-INSTRUMENT-N/verify.py
```

Date (UTC): 2026-10-01. Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12.
Environment: `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.
External timeout: 600 seconds. Elapsed: 7.132 seconds. Exit: 0.
Stderr: 0 bytes, SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 36265 | `66f6df4102a5c88295926ea1c1afb8cbac56848d3ab19be7b84fea9e26ac8c2c` |
| PROOF.md | 42028 | `e9fb15931ce121a5face104c627663a48ead164c409d64b17945fffa3dc82baa` |
| verify.py | 38296 | `76f92f9b8fe0501f58d25bb16f3d066e3a0e5a39e01e80a1939657c88bd6bbcc` |
| EXPECTED.txt, exact stdout | 590 | `5ba56f3fa9036a0d5cc1fe13dba06250362850c3fbe38c6779c78fe106b694b1` |

PASS: 27936 clean B steps, 560 cut steps, 768 negative-control steps;
356766 pointer translations, 9808 phase coordinates, 677448 coefficients,
882720 pointer-operator partition cases and 320 instrument matrix-unit
comparisons; 3006152 archive basis cases; 1111 history branches, 17776
source-unit comparisons and 1024 coherent cross-unit comparisons. Exact
complex controls, untouched-reference, adaptive, capacity and family-equality
checks passed as summarized in EXPECTED.txt. No frozen source was changed.

The universal results rest on PROOF.md and separate independent review,
not finite trajectory extrapolation. This is not a two-architecture
scientific run; ordinary notes-only CI does not execute this verifier.
No physical occurrence, native sampling, preparation mechanism or empirical
closure is tested by this selected L1 audit.
