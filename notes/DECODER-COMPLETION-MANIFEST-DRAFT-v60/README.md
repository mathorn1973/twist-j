# notes/DECODER-COMPLETION-MANIFEST-DRAFT-v60

NON-CANONICAL. Audit-only diagnostic instrument, no authority, no Canon
change, no `canon/` file touched. Produced 2026-08-22 against Public Canon
v60 (tag `canon-v60`, content commit
`18b21bdaf2c2236c9444b120900277ccfb63e050`, `canon/CANON.md` SHA-256
`9387b75f2036ac6aff5737255956b93fb9b906511b8184ae4c1c999e8ed46db0`).

`DEF-DECODER-COMPLETION-CONTRACT` (`canon/CANON.md` 489-645, factor-canonicity
overlay to 1090) defines the manifest *shape* a decoder-completion candidate
must publish. No instance existed. This directory holds the first independent
draft instance, built as a diagnostic: every slot the Canon actually supplies
carries a cited public identifier; every slot it does not carries the literal
`UNRESOLVED` mapped to the live frontier row that owns it. The resulting
"unresolved slot -> owning obligation" table is the payload.

Per `canon/CANON.md` 634-645: syntactic conformance, a resolved identifier, or
a submitted candidate is not evidence and cannot change a public status. This
draft asserts no existence, totality, uniqueness, canonicity, or completeness.

## Contents

```text
MANIFEST-DRAFT-v60.md      the contract instance, resolution ledger, and the
                           unresolved-slot -> owning-row table (rev 2)
ARCHITECT-VIEW-v60.md      non-normative architecture assessment of v60:
                           system decomposition, the stage x leg interface
                           matrix, the forced-decoder trichotomy stated in
                           implementation terms, sufficiency audit (rev 2)
README.md                  this manifest
```

## Findings worth naming

- The resolvable surface is one-legged: the quadratic leg can cite a complete
  typed referent set; the linear and binary legs have registered maps but no
  registered record fields; the `D_geom` and `D_clock` stages have no
  registered maps at all.
- Two holes are **ownerless** — they map to no live frontier row: record and
  stage ownership for the linear/binary readouts, and the physical photon
  propagator, whose only registered route is `[F]` with no `[O]` successor.
  Both are recorded as `obligation_manifest[]` rows with
  `owning_item_id: UNRESOLVED` so they stay machine-visible.
- Everything probability-bearing, dimensionful, or detector-facing is
  `UNRESOLVED` with a named owner. `coarse_graining_id` is the single
  unresolved top-level scalar; its owner, `METRO-REDUCTION-CALCULUS [O]`, is
  also the deepest formal dependency of the live set.

## Method and revision

Both documents were produced by a multi-agent analysis pass over this
repository at the pinned commit, then corrected under adversarial review: the
manifest against the contract's own schema and validation rules (enums,
one-owner rule, no bare nulls, gate ids, honesty of every RESOLVED
identifier), the assessment against `canon/REGISTRY.tsv`, `canon/GATES.tsv`,
`canon/FRONTIER.md`, and `canon/CHANGELOG.md`. Both carry their revision notes
at the end. Working files cited as `C:/j/twist-j-manifest/...` are the
author's local area and are not part of this repository.
