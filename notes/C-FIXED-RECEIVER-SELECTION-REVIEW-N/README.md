# Independent review of the fixed receiver, root clock and stock census

**NON-CANONICAL / L1.** Target:
[PR #1930](https://github.com/mathorn1973/twist-j/pull/1930),
`notes/C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N`, exact head
`3d8d364cb981bb5d53bbede432fb5a4ac4181709`. Review lock:
[issue #1935](https://github.com/mathorn1973/twist-j/issues/1935).

**State: checker pinned, not yet executed.** This commit pins three files:

- the code-independent checker review.py;
- the pre-run MATHEMATICAL-REVIEW.md;
- PREREG-AMENDMENT-1.md.

They are read back from GitHub before the single run. Nothing has been
executed under this review.

PREREG.md was frozen in commit acf69adba32e838a7891bb8b3c1e4386abaf690f,
before the checker existed. It fixes:

- the exposure record;
- the source boundary of the checker;
- the frozen checks R1 to R10, with their expected values;
- the execution and failure rules.

PREREG-AMENDMENT-1.md corrects one false equality in R7. It was found by
the code-free reviewers before the pin and before any execution.

The earlier informal check by the same reviewer is disclosed and published
unchanged in INFORMAL/. It is not backdated as a preregistered test.

## Files

| File | Content |
| --- | --- |
| PREREG.md | Scope S1 to S7, exposure, source boundary, frozen checks R1 to R10, exploratory outputs, execution and failure rules. |
| PREREG-AMENDMENT-1.md | The R7 "For T" correction: Q(T-1)=20 and Q((T-1)/2)=5. |
| MATHEMATICAL-REVIEW.md | Code-free review of the seven scopes: verdicts, corrections E1 to E35 and non-binding expectations for X1 and X2. |
| review.py | The code-independent checker. It was written from the definitions alone and only parsed for syntax before the pin. |
| TARGET-SHA256SUMS | SHA-256 of the 19 target files at the head. |
| INFORMAL/PROVENANCE.md | Executed bytes, hashes, transcribed stdout and seven known weaknesses of the earlier unregistered check. |
| INFORMAL/check_receiver_indep.py | The informal checker, byte for byte as executed. |
| INFORMAL/stock_scan.py | The informal stock scan, byte for byte as executed. |
| SHA256SUMS | Hashes of the files above. |

A later, separate commit adds the run record (RUN.md), the stdout
(EXPECTED.txt) and the result (RESULT.md).

The review changes no target file, registry row, Canon text or release.
Accepting it, and any merge or promotion of the target, are decisions for
the Canon owner.
