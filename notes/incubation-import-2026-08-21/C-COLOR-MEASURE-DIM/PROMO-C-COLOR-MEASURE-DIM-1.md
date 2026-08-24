# PROMO-C-COLOR-MEASURE-DIM-1

Promotion proposal for candidate C-COLOR-MEASURE-DIM-1. A public canon fold can
consume this without reading anything else. This proposal is not canon. It
becomes canon only after the public pipeline validates it: verifier reproduced on
two architectures byte-identical, public checks green, owner opens the fold PR.

Target line: Public Canon v5 (mathorn1973/twist-j main).
Proposed by: in-project incubation lane, session 2026-07-15.
Commit identity for any resulting fold: A. M. Thorn <thorn@twistj.com> (public POLICY).

## Candidate id and proposed status

C-COLOR-MEASURE-DIM-1. Two tiers are proposed; they are independent.

Tier 1 (public inputs only, promotable now): one new computed row [C].
Tier 2 (gated on a public dependency): one further computed row [C].

Neither tier closes COLOR-MEASURE-SELECTION [O]. Both sharpen it.

## Exact statement

Model the color measure as a probability weight vector w over the 24 carrier
orbits (w_i >= 0, sum w_i = 1). Impose two named structural constraints:
  O (observable measurability): w constant on the fibers of the 24 -> 16
     observable-type map;
  S (symmetry): w invariant under the color automorphism symmetry acting on the
     carrier orbits.
Exact result (exact arithmetic over Q, no floats in any assertion):
  under O alone, the admissible family has dimension 15;
  under S alone (the symmetry acting trivially on the orbits), dimension 23;
  under O and S together, dimension 15;
  the admissible set is the relative interior of a 15-simplex, the uniform
  weight 1/24 is a strict interior point, and the weight vectors carry exactly
  16 observable equivalence classes.
The observable difference system has rank 8 = 24 - 16, and the dimension is
independent of which orbits pair (any surjection 24 -> 16 gives rank 8).

## Falsifier

Sub-hypothesis H-DIM "the observable and the symmetry select a unique color
measure" predicts admissible dimension 0. Computed dimension is 15 >= 1, with two
exhibited inequivalent survivors, so H-DIM is FALSE. Concrete falsifier for the
promoted [C] rows: any exact recomputation, under the same named constraints,
that yields an admissible dimension other than 15 (Tier 1: observable alone) or
other than 15 with the symmetry included (Tier 2).

## Verifier and pins

```
PREREG.md        sha256 6fca2545264531fe23337b09bdb7552dcafb6f33c6dadd55a109736c45ac79d0  (5125 bytes)
verify.py        sha256 5f3954f883a0e2653038e7420659d8e764394801319795f71676f76de402daac  (8211 bytes)
stdout           sha256 b0924ff000bbf157c39e450137d6afa39374cd96c87eeb986e1e1b29d4208693
break_check.py   independent second reading (not the frozen verifier); agrees d = 15
env              LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform         x86_64 CPython 3.11.15 (single platform; public validation must add a second arch)
```
verify.py is Python standard library only, exact Fraction arithmetic, well under
120 seconds. For public folding it should be placed at probes/color-measure-dim/
and re-run on a neutral second platform (for example Ubuntu 24.04 aarch64) for
byte-identical stdout.

## Dependency edges

Tier 1 depends only on public objects: the 24 carrier orbits and the 16
observable types named in the COLOR-MEASURE-SELECTION scope, and the public color
sector rows. Not gated.
Tier 2 additionally depends on the fact that the color automorphism symmetry acts
trivially on the 24 carrier orbits (fixes all 24). This fact is presently sealed
internal census data, not public. Tier 2 is GATED on that action being typed in
the public line first; until then Tier 2 stays a candidate and is not folded.

## Exact edits the fold would make

Registry (canon/REGISTRY.tsv), Tier 1, new row (evidence is a path):
```
COLOR-MEASURE-OBS-RESIDUAL   C   under 16-type observable measurability alone, the admissible color-measure family over the 24 carrier orbits has dimension 15; the observable does not select the measure; rank of the difference system is 24-16=8, shape-independent   12. The color door   reproduce/color-measure-dim   any exact recomputation under observable measurability yielding admissible dimension not equal to 15
```

Registry (canon/REGISTRY.tsv), Tier 2, new row, GATED:
```
COLOR-MEASURE-RESIDUAL-DIM   C   adding invariance under the color automorphism symmetry (trivial on the 24 orbits) leaves the admissible dimension 15 (23 under symmetry alone); a unique measure is not selected by symmetry and the observable together   12. The color door   reproduce/color-measure-dim   any exact recomputation with the symmetry included yielding admissible dimension not equal to 15, or a public typing of the symmetry action that is not trivial on the 24 orbits
```

Frontier (canon/FRONTIER.md), sharpen COLOR-MEASURE-SELECTION [O], do NOT close:
add to its scope note "the residual under the 16-type observable alone is a
computed 15-dimensional simplex (COLOR-MEASURE-OBS-RESIDUAL); symmetry and the
observable together do not select a unique vector; the remaining named routes
stay open." Keep the status O and the existing negative-closure clause.

Canon (canon/CANON.md), section 12 "The color door": one sentence recording that
the measure residual left by the observable is an exact 15-dimensional simplex,
using neutral descriptors only, no internal names. No axiom change, no prior LOCK
retracted.

Changelog (canon/CHANGELOG.md): integer version bump, new hashes for every
normative file touched, statement that only the two [C] rows above are added and
COLOR-MEASURE-SELECTION stays [O].

## What this does not claim

It does not close COLOR-MEASURE-SELECTION. It evaluates two named constraints,
not the three registered routes. It claims no selection of a unique measure, no
QCD content, no measure lift to the full SL_3(F_5) carrier. It is a quantified
lower bound on the residual freedom plus a fired uniqueness sub-falsifier.
