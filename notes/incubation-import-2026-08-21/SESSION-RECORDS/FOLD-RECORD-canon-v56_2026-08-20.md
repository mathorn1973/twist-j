# FOLD RECORD. Public Canon v56, four-probe consolidation. LANDED

Status: `LANDED / TAGGED / ALL GATES PASS`. Public line only. This document is
a record, not an authority. `STATUS.md` on `mathorn1973/twist-j main` is the
only statement of what the Canon is.

Supersedes `claude/FOLD-RECORD-canon-v56-PREPARED_2026-08-20.md`, which
described the same fold before it was pushed. The prepared record's every
declared value was confirmed on landing, unchanged.

## Release form, read back from public main on 2026-08-20

```text
STATE:          ACTIVE
CANON:          Public Canon v56
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v56
CONTENT_COMMIT: b36c93ed8ce24a9cbd771168094db04f5a5ac06c
CANON_SHA256:   b284ed6e78341aa6e3a74652d6f1f8f4079c270461f28bf32f2d95a6bd8b6645
CANON_BYTES:    288492
```

Verified against the live head: tag `canon-v56` is an ancestor of main, the
content commit is an ancestor of main, `canon/SHA256SUMS` is 5 of 5 OK, and
`canon/CANON.md` measures 288492 bytes with the declared digest. The content
commit is exactly the one this session built and delivered as a bundle.

## What landed, seven rows

```text
J-LI-PENTAGON-DILATION-DEFICIENCY  T  16. p = 5 and the wall
PENTAGON-ONLY-DILATIONS            F  16. p = 5 and the wall
J-LI-CYCLIC-CARRIER-DIMENSION      T  16. p = 5 and the wall
KERNEL-SUBSET-LANDSCAPE            T  3. The kernel and the census
J-TORAL-ENTROPY                    T  2. Time, space, and the decoder
TM-ENTROPY-ZERO                    T  3. The kernel and the census
BINARY-READ-RELATIVE-ENTROPY       T  2. Time, space, and the decoder
```

Ledger delta confirmed by the machine on the live head:
`LEDGER PASS claims=287 items=332 dependencies=493 evidence=287 history=805
gates=10 programs=7`. Claims 280 + 7, T 165 + 6 = 171, F 15 + 1 = 16, live H/O
27 unchanged, `FRONTIER.md` byte-identical to v55.

## What v56 anchored, and what it left open

v56 anchored `2 log phi` in the dynamical direction: `J-TORAL-ENTROPY [T]`
gives `h_top = h_Haar = 2 log phi` for the toral automorphism induced by the
step matrix, with the exact fixed-point law and the witness
`#Fix(T^15) = 1860496`. It anchored nothing in the arithmetic direction: at
v56 the strings `Mahler`, `regulator` and `class number` applied to
`Q(zeta_5)` still occur zero times each in `canon/CANON.md`. That gap is what
`P-TWOLOGPHI-INVARIANTS-1` was built to close.

`ENTROPY-LAYER-BRIDGE [O]` keeps its exact scope in both directions and is
neither closed nor weakened.
