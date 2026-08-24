# FOLD RECORD. Public Canon v57, the arithmetic anchor and obligation B

Status: `LANDED / TAGGED / ALL GATES PASS`. Public line only. This document is
a record, not an authority. `STATUS.md` on `mathorn1973/twist-j main` is the
only statement of what the Canon is.

Session: canon-v57-fold-2026-08-20. Basis verified by fresh fetch before any
file was touched: Public Canon v56 ACTIVE at main `d525da0`, tag `canon-v56`
an ancestor of main, `canon/SHA256SUMS` 5 of 5 OK, ledger 287 claims.

## What landed, five rows

```text
J-MAHLER-MEASURE             T  1. The axiom and the two projections   L1
REGULATOR-TWO-LOG-PHI        T  4. The two places                      L1
CYCLOTOMIC-CLASS-NUMBER-ONE  T  4. The two places                      L1
J-TORAL-PERIODIC-POINTS      C  2. Time, space, and the decoder        L2
METRO-FORBIDDEN-WITNESSES    C  15. Couplings, instruments, metrology  L5
```

Both sources are public probes merged earlier the same day, each with a
byte-identical two-architecture replay: `P-TWOLOGPHI-INVARIANTS-1` (issue
#460, PR #461) and `P-METRO-FORBIDDEN-WITNESSES-1` (issue #464, PR #465).

## The chain, in order

```text
probe merges    PR #461 (P-TWOLOGPHI-INVARIANTS-1) and PR #465
                (P-METRO-FORBIDDEN-WITNESSES-1), both merged without squash
                earlier the same day, both probe branches retained
fold branch     release/canon-v57, exactly two frozen commits
  content       8e8b04abe4d3359942449533854ef1d142be70df
                15 files: the five hashed canon files, the five companion
                ledgers, STATUS_COUNTS.tsv, the status-separation trio, and
                the architecture-map test
  release form  4a57f88465c1ed36ad83a7a6165580bd294d95c6
                exactly STATUS.md, README.md, CITATION.cff
fold PR         #467, widened canon sweep green:
                architecture-aarch64 PASS 13m56s,
                architecture-x86_64 PASS 15m58s, aggregate check PASS
merge           4ef54f0c34f80897af0121a2d93b710e70a8377c, no squash, no rebase
readback        fresh clone of main: STATUS fields as declared, SHA256SUMS
                5 of 5 OK, both frozen commits ancestors of HEAD,
                CANON PASS v57 claims=292, LEDGER PASS
tag             canon-v57 on the merge commit, tag object 9a8af9c2,
                publication job success in 45s
release         Public Canon v57, Latest. Draft created with the tag job's own
                activation-manifest.json and the tagged canon/SHA256SUMS, both
                assets downloaded and their digests compared before publishing:
                manifest 267862af..., SHA256SUMS b5b09f72... The release-event
                job then revalidated them, success in 53s. The manifest
                declares content_commit 8e8b04ab, activation_commit 4ef54f0c,
                state ACTIVE. No locally generated manifest was substituted.
```

## Release form, read back from public main

```text
STATE:          ACTIVE
CANON:          Public Canon v57
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v57
CONTENT_COMMIT: 8e8b04abe4d3359942449533854ef1d142be70df
CANON_SHA256:   c96a2ef52c78d68ef8f04b582e4a17328e6a863b49664f29b1bd324171d802a8
CANON_BYTES:    295013
```

## Evidence pins

```text
probe bundles (bundle-manifest-sha256-v1, two-architecture)
  P-TWOLOGPHI-INVARIANTS-1
    78267f36a457c99965cb1f0caa3115b487a9d294a5d709664a4a99a47a8f2d5d
  P-METRO-FORBIDDEN-WITNESSES-1
    790cb07fd16082b29f25855dae763db5f1f7c2962175bc9988b545fed53782a2
history events  CANON57-DECLARE-J-MAHLER-MEASURE,
                CANON57-DECLARE-REGULATOR-TWO-LOG-PHI,
                CANON57-DECLARE-CYCLOTOMIC-CLASS-NUMBER-ONE,
                CANON57-DECLARE-J-TORAL-PERIODIC-POINTS,
                CANON57-DECLARE-METRO-FORBIDDEN-WITNESSES,
                CANON57-SCOPE-METRO-REDUCTION-CALCULUS
```

## What the fold closes

Public Canon v56 anchored `2 log phi` in the dynamical direction, as the
topological and Haar entropy of the toral automorphism induced by the step
matrix. It anchored nothing in the arithmetic direction: at v56 the strings
`Mahler`, `regulator` and `class number` occur in `canon/CANON.md` zero times
each, measured rather than assumed. Three of the five rows close that gap.
`M(J) = phi^2` exactly. `Reg(Q(zeta_5)) = 2 log phi`. Class number one for
both fields, proved by the Minkowski bound rather than imported.

The same constant is therefore the logarithm of a Mahler measure, a regulator
and a toral entropy. The fold states plainly what that is and is not: a fact
about the number `phi`, and not a bridge between layers.
`ENTROPY-LAYER-BRIDGE [O]` keeps its exact scope and each new arithmetic row
carries a `BOUNDED_BY` edge to it, so the fence is a ledger fact and not only
prose.

The fifth row discharges obligation B of `METRO-REDUCTION-CALCULUS [O]` for
the five entries section 15 names, under one ratified reading per phrase. The
parent does not close: status `O`, `STOP` and falsifier all unchanged, only
the obligation B clause replaced, and obligations D and E untouched.

## Ledger delta, signed term by term

```text
claims:    287 + 5 = 292
T:         171 + 3 = 174
C:         30 + 2 = 32
D 43, H 3, O 24, F 16, live H/O 27, all unchanged
normative items: 332 + 3 theorem + 2 computation = 337
dependencies:    493 + 9 = 502
evidence rows:   287 + 5 = 292
history rows:    805 + 5 declarations + 1 scope change = 811
two-architecture evidence: 205 + 5 = 210
reproductions 23, gates 10, programs 7 over 27 rows, unchanged
```

Confirmed by the machine, not summed by hand:
`LEDGER PASS claims=292 items=337 dependencies=502 evidence=292 history=811
gates=10 programs=7`.

## Authoring decisions this fold made, all declared

The probes froze the row texts, the sections and the delta. The following are
this fold's own choices and are open to review.

```text
1  METRO-FORBIDDEN-WITNESSES takes layer L5 in NORMATIVE.tsv. Its
   preregistration phrases the action layer as "L1 formal, on L5 stream
   objects". The ledger layer field records the layer of the objects a row
   quantifies over, which here are L5 streams, and this matches the parent
   METRO-REDUCTION-CALCULUS [O] and the sibling METRO-REDUCTION-ARROWS [C],
   both L5. This is a classification, not a lift, and it is what keeps the two
   new dependency edges inside one layer with no gate invented for them.
2  Nine dependency edges, seven declared by the twologphi preregistration and
   two by the metro promotion's dependency section: the arrows row as the
   control it consumes, and the parent it serves, BOUNDED_BY.
3  Four canon passages: section 1 after the golden bridge, section 2 after the
   toral entropy passage, section 4 after the ramification census whose
   disc(K_5) = 5^3 the Minkowski bound consumes, and section 15 between the
   arrows paragraph and the parent paragraph.
4  The obligation B clause is replaced in REGISTRY.tsv only; FRONTIER.md is a
   generated view and inherits it.
```

## The one deviation from a frozen row, and why

```text
row        METRO-FORBIDDEN-WITNESSES
frozen     "which excludes every output transport tau at once rather than one
            family of them"
folded     "which excludes at once every output transport tau that preserves
            the distinctions of the stream, the class a reduction arrow types
            and in which every registered admitted arrow carries tau_R =
            identity, rather than one family of them, and for the
            box-reordering entry excludes every tau outright"
```

The probe's own `RESULT.md` established the reason and asked a fold to act on
it. With the transformed object free and `tau` unrestricted, a constant
transport satisfies the bare admissibility equation while collapsing the
stream to a point, so the unrestricted phrase is exact for the box-reordering
witness and needs a reading for three of the others. A reduction arrow is
typed with an output transport carrying `w` to `w'` and every registered
admitted arrow carries `tau_R` = identity, so the class that matters is the
distinction-preserving transports. Folding the looser phrase would have put a
claim in the registry stronger than the evidence carries. The pinned probe
files were not touched.

The other four rows are folded byte for byte from their frozen text.

## Gates and audits

On Ubuntu 24.04.4 LTS x86_64 with CPython 3.11.15, and again on macOS arm64
with CPython 3.13.13:

```text
check_canon           CANON PASS v57 claims=292
check_ledger          LEDGER PASS
check_policy          POLICY PASS
check_status_labels   STATUS LABELS PASS
check_preregistration PREREGISTRATION DRAFTS PASS drafts=6
check_reproduce       REPRODUCE PASS, all reproductions re-executed
check_activation      ACTIVATION PASS mode=active full=True
unit tests            99/99 OK
status-separation     RESULT 51/51 ALL PASS, byte identical on both
clean replay          fresh clone of the branch, every gate re-run
```

Two audits are worth naming rather than burying.

```text
1  The v56 entropy-anchor check pinned an exact dependency-edge set that this
   fold legitimately extends by J-TORAL-PERIODIC-POINTS -> J-TORAL-ENTROPY. It
   failed on the first run of the folded tree, was inspected, and was updated
   to the new exact set. It was not loosened into an inequality; a check that
   pins an exact set is doing its job when it fires.
2  A breaker pass over the diff confirmed, by a path independent of the fold
   script: four of five registry rows byte-equal to their frozen text, the
   fifth differing only in field 3 and only by the declared tightening, the
   only removed registry line being the parent row it replaces, every removed
   CANON.md line being a version bump or the one declared clause, and all five
   claim ids present as exact tokens in CANON.md.
```

Disclosure. On the second-architecture machine the reproduction `color-ladder`
fails under that machine's default CPython 3.9, because it calls
`int.bit_count`, which exists from 3.10. It passes and matches its
`EXPECTED.txt` under 3.13 there. This is a pre-existing interpreter floor in
an unrelated reproduction, not a v57 regression, and it is recorded here
rather than left to be rediscovered.

## Falsifier for this record

Wrong if any listed commit, hash, byte count, count or gate line fails
readback from public `main`, or if a rerun of the status-separation verifier
from that tree produces stdout differing from its `EXPECTED.txt`.
