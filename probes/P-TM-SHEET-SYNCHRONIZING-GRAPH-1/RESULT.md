# P-TM-SHEET-SYNCHRONIZING-GRAPH-1 result

Status: SCIENTIFIC RESULT; LOCAL LEG PASS; PULL-REQUEST LEG PENDING;
PUBLIC CANON UNCHANGED

The immutable preregistration pin
`4d526476d33885224424a2bc68549ea48e877b0e` was executed exactly once on
native Linux/aarch64 after public remote readback. The verifier exited
zero, wrote no stderr, and produced the exact 1157-byte output recorded in
`EXPECTED.txt` with SHA-256
`7d267d7a74bdd745b68443bd63514834700580525391b42436ff988f9031bafc`.
All sixteen frozen gates passed: runtime, carrier, generators, sheet table,
transformation automaton, minimal reset, reset theorem, Thue-Morse pairs,
mu^4 language, nonsync table, w* facts, leaf transformations,
quadratic-class cut, invariant graph, and sign law. No counterexample was
emitted; the falsifier did not fire.

## Recorded decision

```text
run integrity:       PASS
counterexample:      NONE
result:              PASS
scope:               the eight frozen clauses of PREREG.md, layer L1
status discipline:   candidate result; the registry row and Canon fold are
                     a separate sealed step after the pull-request replay
                     supplies the second architecture leg
```
