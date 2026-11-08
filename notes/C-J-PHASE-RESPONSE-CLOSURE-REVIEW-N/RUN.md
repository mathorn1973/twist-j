# Exact execution record

PUBLIC / NON-CANONICAL / L1. A. M. Thorn; Apache-2.0.

Immutable scientific pin: `8ac342acc63a187fb480b678f3fa4030ef02afd2`.
Public byte readback completed at 2026-10-20T08:46:45.626205+00:00, before the first run.
Receipt: https://github.com/mathorn1973/twist-j/issues/1609#issuecomment-6287129508.
The checkout was clean and at that exact pin. All five payload hashes in
FROZEN.sha256 were verified immediately before execution.

| Frozen file | Bytes | SHA-256 |
|---|---:|---|
| FROZEN.sha256 | 386 | `25d7e3e57ec0f2f25d0f33f89d1a24f6a32aa0af3ce0ff4bfc6a5054d3eaa657` |
| OBLIGATIONS.md | 2583 | `1750fc6e582264b3600f936919ad7e4913e379b1c553888d3f79a185a3adead3` |
| PREREG.md | 10521 | `49847fc752cbb573592acdd743c23384366498e693ae834287dc5c013681c2e2` |
| PROOF.md | 16550 | `2e76e4511c6168228db098d37859728ef07977f6ff3c0a60311274d715902a32` |
| SOURCES.tsv | 5597 | `163f7ea66272b308229fd0ad859563c00bd84a36cbbb05806aeb019c1fa8fb90` |
| verify.py | 19310 | `11fcf33586a4d60806d80c64f378b97278aa517d06d3e3a495910f8d44b0d134` |

The exact scientific command, from the repository root, was:

```text
python3 notes/C-J-PHASE-RESPONSE-CLOSURE-REVIEW-N/verify.py
```

The shell's python3 resolved to Python 3.13.13. The capture wrapper used
the preregistered 600-second outer limit. It did not import or modify the
scientific program. No smoke run or earlier scientific execution occurred.

| Recorded field | Actual value |
|---|---|
| Platform | macOS 27.0.1 |
| Architecture | arm64 (aarch64) |
| Python | Python 3.13.13 |
| UTC start | 2026-10-20T08:47:45.983545+00:00 |
| UTC finish | 2026-10-20T08:48:00.376681+00:00 |
| Elapsed seconds | 14.393 |
| Outer limit seconds | 600 |
| Completion | COMPLETED |
| Exit code | 0 |
| stdout bytes | 2141 |
| stdout SHA-256 | `bbb97741dcb682fc412e09fc3f398426c384e0c4e24806f0663d0aea3421dd66` |
| stderr bytes | 0 |
| stderr SHA-256 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

EXPECTED.txt is the exact first completed stdout, copied byte-for-byte.
The emitted status is PASS_DEFINED_SUCCESSOR, including the preserved
STOP_UNDEFINED for the old relation. No named scientific falsifier fired.

This is one-architecture execution evidence. It does not by itself satisfy
the two-architecture computation gate. Notes-only repository CI validates
repository integrity but does not run this scientific checker. The universal
claims rest on the submitted exact derivations and await independent review;
the finite executed results remain candidate-C at the evidence above.
