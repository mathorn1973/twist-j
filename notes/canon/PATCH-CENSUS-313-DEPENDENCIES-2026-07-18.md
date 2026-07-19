# Proposed Canon companion-ledger patch: census bounds for four theorem rows

Date: 2026-07-18.

**NON-CANONICAL PROPOSAL.** This file proposes a later, separately reviewed
fold into `canon/DEPENDENCIES.tsv`. It does not itself change the public ledger.
No claim status, scope, evidence location, evidence hash, history row, or gate
changes are proposed.

## Problem

Four status-T rows quantify over the recurrent carrier certified by the
status-C census, but no dependency row records that scope boundary:

- `COLOR-RETURN-D5`;
- `COLOR-TORSOR-HOLONOMY`;
- `COLOR-KIN-NORMALIZER`;
- `ELECTRON-SIGN-LAWS`.

The omission hides where the word "all" is only as exhaustive as the declared
finite census protocol.

## Proposed TSV rows

Append these rows to `canon/DEPENDENCIES.tsv` in the later fold:

```tsv
COLOR-RETURN-D5	CENSUS-313	BOUNDED_BY	the recurrent-return theorem is exhaustive only over the recurrent carrier certified by CENSUS-313; exact D5 facts on each enumerated attractor do not upgrade census exhaustiveness
COLOR-TORSOR-HOLONOMY	CENSUS-313	BOUNDED_BY	the 312 size-20 torsors plus the singlet are the recurrent carrier certified by CENSUS-313; protocol independence and an all-orbit statement remain outside scope
COLOR-KIN-NORMALIZER	CENSUS-313	BOUNDED_BY	the normalizer theorem permutes all supports in the 313-attractor carrier certified by CENSUS-313; exhaustiveness beyond that C-status carrier is not asserted
ELECTRON-SIGN-LAWS	CENSUS-313	BOUNDED_BY	the exhaustive aligned-protocol sign laws quantify over the recurrent seeds and 313 supports supplied by CENSUS-313; census exhaustiveness remains a C-level bound
```

## Why `BOUNDED_BY`, not `REQUIRES`

`CENSUS-313` has status C. The four consumers have status T.
`tools/check_ledger.py` deliberately rejects a theorem that `REQUIRES` a
lower-status claim. A `REQUIRES` edge would therefore either fail the ledger
firewall or silently ask for an unjustified status promotion.

`BOUNDED_BY` states the actual situation: the algebraic/group-theoretic
statements are theorem-grade on the declared finite carrier, while the claim
that this carrier is the complete recurrent census remains C-level and
one-architecture.

## Fold checklist

1. Append only the four rows above to `canon/DEPENDENCIES.tsv`.
2. Run `python tools/check_ledger.py` and require `LEDGER PASS`.
3. Run `python tools/architecture_map_report.py --strict`; the four census
   rows must print `BOUNDED_BY` and the census-debt section must clear.
4. Update the graph-debt paragraph in
   `notes/ARCHITECTURE_MAP_2026-07-18.md` from "record the edges" to
   "recorded as C-level carrier bounds".
5. Do not change the four T statuses or the C status of `CENSUS-313` in this
   fold. A later status change requires its own evidence and history event.

## Scientific consequence

This patch does not strengthen any theorem. It makes the scope firewall
visible. It also clarifies the highest-leverage evidence task: a
second-architecture replay of the census bundle would strengthen the carrier
on which all four rows are bounded without pretending that a ledger edge is a
new proof.
