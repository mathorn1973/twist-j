# P-TM-SHEET-SYNCHRONIZING-GRAPH-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS;
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

The first clean GitHub Linux/x86_64 pull-request replay used the identical
pinned verifier at tested merge commit
`7ef57b77eaa0ca14cc32551de2fe49227f7ea81b`. Workflow run `32171197983`,
job `95822501472`, exited zero with empty stderr and reproduced
`EXPECTED.txt` byte for byte; the parallel GitHub Linux/aarch64 job
replayed identically. The two-architecture computation gate is PASS.

## Recorded decision

```text
run integrity:       PASS
counterexample:      NONE
result:              PASS
architecture gate:   PASS (local aarch64, GitHub x86_64, GitHub aarch64)
scope:               the eight frozen clauses of PREREG.md, layer L1
status discipline:   the probe result stands at its evidential grade; the
                     registry row TM-SHEET-SYNCHRONIZING-GRAPH and the
                     Canon fold are a separate sealed integer-versioned
                     step and are not made by this probe
```
