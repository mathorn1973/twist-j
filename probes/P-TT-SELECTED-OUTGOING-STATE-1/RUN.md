# First completed run: selected outgoing TT state

PUBLIC; NON-CANONICAL. P-TT-SELECTED-OUTGOING-STATE-1.

All six frozen files were pushed and publicly read back byte for byte before
the first scientific execution. The invocation used a clean worktree at the
exact public pin. Before the pin only analytic derivation, independent
written review and static syntax inspection were performed.

## Run fields

```text
pin_commit: 6257dfaae9132ef2a2a49ec06300775287d595db
verifier_sha256: 8cc1b45f70c71037cdade0046e4ae3d485cd5053293cf907ef14a66d66ff2002
command: python probes/P-TT-SELECTED-OUTGOING-STATE-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_bytes: 1125
stdout_lines: 11
stdout_sha256: dc1e909f2934f7fe3095875d21b374fa79afde6aa6c104d263aa86b6e43c0fc4
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Public lock: [#1097](https://github.com/mathorn1973/twist-j/issues/1097).
Base main: `1d3e70433f850d03aa210374d8cda16dd97a0c10`.
Pin tree: `4dc4f9ce74382de72815f1cd4bfe3559e56fb1e7`.
Date: 2026-09-20. Working directory: repository root.
Environment: `LC_ALL=C`, `LANG=C`, `TZ=UTC`,
`PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`.
Exact stdout is committed unchanged as EXPECTED.txt. All ten gates passed;
no earlier scientific attempt failed or required a new pin.

## Frozen input custody

| Path | Bytes | SHA-256 |
| --- | ---: | --- |
| `probes/P-TT-SELECTED-OUTGOING-STATE-1/PREREG.md` | 9754 | `b71f52f8a417ffe0d2b68436206f4c3168e18d44a405f93b3b0faee31a0fe27d` |
| `probes/P-TT-SELECTED-OUTGOING-STATE-1/MODEL.md` | 11439 | `9f404c424840490c557b2967d239668eeb49afb6b044cc813014a9ecb4b85ecd` |
| `probes/P-TT-SELECTED-OUTGOING-STATE-1/PROOF.md` | 22553 | `7ac6ba0b326052b6f11689c2e6873917b25f5f3ed3ff43b1df98e3a3d2871494` |
| `probes/P-TT-SELECTED-OUTGOING-STATE-1/REVIEW.md` | 13081 | `4530a24e8c1d161333da806db3b6a11868060db4ad1d3b7b1f2df4fa4a513c9f` |
| `probes/P-TT-SELECTED-OUTGOING-STATE-1/verify.py` | 24583 | `8cc1b45f70c71037cdade0046e4ae3d485cd5053293cf907ef14a66d66ff2002` |
| `notes/canon/SELECTED-TT-STATE-FOLD-PROPOSAL.md` | 6695 | `030677e77df2cc4bc4d4b685091295bcad76ed51ab6116d2245f37e6ba1d448a` |

The verifier uses only the Python standard library and exact rational,
cyclotomic and formal radical certificates. It reads no runtime file or
external dataset. Its explicit finite horizon is m=0,...,10; the written
proof owns the all-counter assertions, including nonvanishing and strict
intensity-denominator positivity. The run is not an empirical measurement.

This record describes one local architecture. Subsequent public x86_64 and
aarch64 replay and public acceptance belong to ACCEPTANCE.md and the linked
pull-request record. Canon v90 and the full registered physical normalization
owner remain unchanged.

