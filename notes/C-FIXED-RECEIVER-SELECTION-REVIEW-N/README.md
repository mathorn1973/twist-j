# Independent review of the fixed receiver, root clock and stock census

**NON-CANONICAL / L1.** Target:
[PR #1930](https://github.com/mathorn1973/twist-j/pull/1930),
`notes/C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N`, exact head
`3d8d364cb981bb5d53bbede432fb5a4ac4181709`. Review lock:
[issue #1935](https://github.com/mathorn1973/twist-j/issues/1935).

**State: specification frozen. No checker exists yet, and nothing has been
executed under this review.**

PREREG.md fixes four things before any new execution:

- the exposure record;
- the source boundary for a code-independent checker;
- frozen checks R1 to R10, with their expected values;
- the execution and failure rules.

The earlier informal check by the same reviewer is disclosed and published
unchanged in INFORMAL/. It is not backdated as a preregistered test.

## Files

| File | Content |
| --- | --- |
| PREREG.md | Scope S1 to S7, exposure, source boundary, frozen checks R1 to R10, exploratory outputs, execution and failure rules. |
| TARGET-SHA256SUMS | SHA-256 of the 19 target files at the head. |
| INFORMAL/PROVENANCE.md | Executed bytes, hashes, transcribed stdout and seven known weaknesses of the earlier unregistered check. |
| INFORMAL/check_receiver_indep.py | The informal checker, byte for byte as executed. |
| INFORMAL/stock_scan.py | The informal stock scan, byte for byte as executed. |
| SHA256SUMS | Hashes of the files above. |

The code-independent review.py, the pre-run MATHEMATICAL-REVIEW.md, the run
record and the result are added in later, separately pinned commits.

The review changes no target file, registry row, Canon text or release.
Accepting it, and any merge or promotion of the target, are decisions for
the Canon owner.
