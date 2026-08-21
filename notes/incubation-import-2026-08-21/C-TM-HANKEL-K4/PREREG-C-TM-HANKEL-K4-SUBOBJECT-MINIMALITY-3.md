# PREREG C-TM-HANKEL-K4-SUBOBJECT-MINIMALITY-3

```text
CANDIDATE:    C-TM-HANKEL-K4-SUBOBJECT-MINIMALITY-3
STATUS:       incubation candidate, NO AUTHORITY, promotes nothing
PUBLIC BASIS: Public Canon v44, main = tag canon-v44 =
              1417b533944e85106901079cc73ae7a0c3c42dc2, STATUS ACTIVE,
              re-read at freeze time
PARENTS:      C-TM-HANKEL-K4-SUBSTRATE-1 (frozen substrate, cell order,
              canonical 109-entry S_4-invariant map, consumed unchanged)
              C-TM-HANKEL-K4-SPECTRAL-FLOW-2 (flow convention, profile
              locus, LCG domain protocol, layer slices, consumed
              unchanged; its G5 killed gram211 by exact collision and
              left gram22 alive on its pool)
OWNER GATE:   conditional GO of 2026-08-11: granularity approved ONLY as
              minimality inside the frozen 109-entry parent map; the
              ambient completeness overstatement is corrected below; the
              scope is the frozen domain D, never the whole abstract
              stratum, until a separate coverage theorem exists.
LAYER:        L1 only. One session per candidate; this document claims
              the id.
```

## Correction carried from the owner audit, before anything else

The earlier proposal wrote "nothing of degree at most 2 exists outside
the pool". That sentence is FALSE for the 109-entry parent map. The
correct accounting: the space of S_4-invariant polynomials of degree at
most 2 on the 65-cell sign space has dimension 1 + 10 + 154 = 165
(constant, linear invariants, homogeneous quadratic invariants, with
154 = 55 + 78 + 15 + 6 by real orthogonal type of every S_4
irreducible). The parent map has 10 + 78 + 15 + 6 = 109 coordinates: its
first ten are the LINEAR orbit sums, not the 55 quadratics of the
trivial isotypic sector. The 55 trivial-sector quadratics, in particular
all products of orbit sums, are OUTSIDE the parent map.

The frozen consequence, stated in the owner's words:

The admissible class is not the full space of degree-at-most-two
invariant polynomial features. In particular, quadratic products in the
trivial isotypic sector are outside the frozen 109-coordinate parent
map. Q2 asserts minimality only among subobjects of that parent map.

The result of this candidate is therefore named PARENT-SUBOBJECT
MINIMALITY and never "quadratic invariant minimality".

## The admissible class, frozen

```text
F_109 = { F(B, S31, S22, S211) }
B    subset of [10]  whole orbit-sum coordinates, taken individually
S31  subset of [12]  copies of [31]; F carries the FULL Gram block over S31
S22  subset of [5]   copies of [22]; full Gram block over S22
S211 subset of [3]   copies of [211]; full Gram block over S211

d(F) = |B| + g(|S31|) + g(|S22|) + g(|S211|),   g(m) = m(m+1)/2

atoms: 10 + 12 + 5 + 3 = 30 labeled atoms; |F_109| = 2^30 exactly
```

Completeness of this class holds BY CONSTRUCTION for the claim as
stated: Q2 quantifies over subobjects of the parent map assembled from
whole orbit-sum coordinates and whole copy-subset Gram blocks, nothing
else. Layer slices of the parent 109-vector are inherited unchanged:
sums10 = [0:10], gram31 = [10:88], gram22 = [88:103],
gram211 = [103:109]. The class derives from the parent module data
(multiplicities 10, 12, 5, 3, 0; isotypic ranks 10, 36, 10, 9, 0),
frozen before the seventeen failures existed. No construction step below
reads the seventeen.

## The domain D, frozen exactly

Orientation is defined on the locus where the table's K inertia is
(7,0,9) or (9,0,7); the skeleton endpoint is the parent's constant
(8,0,8), so the flow label is +1 on (7,0,9) and -1 on (9,0,7), in the
frozen convention of the spectral-flow parent (upward crossing +1).

D is abstract-only and is generated deterministically:

```text
BASE   x = 1; 64-bit LCG x -> (6364136223846793005 x
       + 1442695040888963407) mod 2^64; discard 4000 steps; then 4000
       tables, each from two further steps, bits = (x1 mod 2^33)
       + ((x2 mod 2^32) << 33), exactly the parent protocol; keep the
       two-profile tables. Enumeration order: ascending bits value.
EXP1   single-cell flips: seeds = sorted(BASE) + [0x02e639472cd318ed2]
       (the substrate parent's abstract witness); for EVERY seed in
       order, flip cells j = 0..64 ascending; keep two-profile tables
       not already present.
EXP2   double-cell flips: over the FIRST M = 40 members, in ascending
       bits order, of the two-profile set after EXP1; pairs (i, j),
       0 <= i < j < 65, lexicographic; keep two-profile tables not
       already present. M = 40 is frozen and does not move.
D      the union, deduplicated by bits. The seventeen real tables are
       NOT in D and are used in no construction step; they enter only
       in the held-out break stage G6.
```

## The two claims, frozen in the owner's strict form

```text
Q1  SUFFICIENCY.  gram22 decides orientation on D.
    Falsifier: exist x, y in D with flow(x) != flow(y) and
    gram22(x) = gram22(y). d(gram22) = g(5) = 15.

Q2  PARENT-SUBOBJECT MINIMALITY (lower bound).  No F in F_109 with
    d(F) <= 14 decides orientation on D.
    Falsifier: one such F, printed with its shape, together with an
    INDEPENDENT direct recheck of its deciding property against the
    raw opposite-flow pairs of D.

On Q1 PASS and Q2 PASS jointly: d_min = 15 in the declared class on the
declared domain. Dimension 15 objects other than gram22 do not touch
minimality; uniqueness at 15 is Q3 and is NOT posed.
```

Scope is D. Not the abstract stratum. A full-stratum statement would
require a separate coverage theorem, that the agreement-pattern
antichain of opposite-flow pairs realized by D equals that of the full
stratum; no such theorem is claimed, gated, or implied here.

## Field 1. EQUATION (gates; each check name states exactly its test)

```
G1  DOMAIN. Rebuild BASE, EXP1, EXP2 exactly as frozen; print |BASE|,
    |after EXP1|, |D|, and the two flow counts; gate: both flows
    present in D; gate: none of the seventeen real tables is used in
    construction (the code path takes no real input; any coincidental
    bit-equality of a D member with a real table is printed as a
    finding and fires nothing).
G2  STRUCTURE. Multiplicities (10, 12, 5, 3, 0) and parent_coordinates
    = 109 and atoms = 30 recomputed and gated; the ambient accounting
    gated by two independent exact computations: sum of m(m+1)/2 over
    sectors = 154 and the Burnside count of S_4 orbits on unordered
    cell pairs = 154, with the frozen statement printed that the 55
    trivial-sector quadratics lie OUTSIDE the parent map and outside
    the admissible class.
G3  Q1. Bucket D by the 15-entry gram22 vector; gate: no bucket
    contains both flows; on failure print the witness pair exactly.
G4  Q2. Exact certificate that no F in F_109 with d(F) <= 14 decides
    orientation on D. Machinery: reduce opposite-flow pairs of D to
    the antichain of maximal agreement patterns (per pair: the set of
    agreeing orbit-sum atoms, and per sector the maximal copy subsets
    whose full Gram blocks agree); a configuration F fails iff it is
    contained in some pattern; the gate certifies every maximal
    admissible configuration under the cap, INCLUDING plateau maxima
    of cost below 14 with no admissible extension under 15, as
    contained in a pattern; print the pattern antichain size and the
    maximal-configuration count. Any candidate decider found by the
    search is rechecked directly against the raw pairs before the
    gate may fire.
G5  DIAGNOSTICS, findings only, fire nothing: the true minimum
    deciding cost d_min on D by extending the exact search to cap 15;
    all minimal deciding configurations at d_min up to a printed
    count; whether the gram22 block is among them and whether it is
    the only one (that is Q3 material, reported, not claimed); the
    per-layer separation table for sums10, gram31, gram22, gram211,
    full109 on D, continuing the parent's G4/G5 series.
G6  HELD-OUT BREAK, after all gates: the seventeen reals evaluated
    against D and against each other; any equal-gram22 opposite-flow
    hit within D union reals is printed as a fired break of the
    EXTENSION of Q1 to D union reals, labeled exactly that, distinct
    from Q1 on D; absence is printed as survived.
```

## Field 2. CODE

`verify_tm_hankel_k4_subobject_minimality_3.py`, assembled from the two
parents' pinned machinery (cell order, kflat, exact inertia paths,
invariant 109-vector, LCG protocol) plus the new domain expansion,
bucketing, pattern reduction, and exact search. Python standard library
only; exact integer and Fraction arithmetic; no float anywhere;
deterministic stdout; environment LC_ALL=C LANG=C
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC. Two platforms,
byte-identical stdout: x86_64 and aarch64. Declared budget for this
incubation candidate: 900 seconds, a disclosed deviation from the 120
second public style, forced by the EXP2 volume; a later public probe
re-engineers or re-scopes the domain.

## Field 3. CARRIER AND DATA

No external data, no network, no randomness beyond the frozen LCG
constants above. The seventeen reals appear only in G6.

## Field 4. SYSTEMATICS

```
S1  polarization t(1) = -1 fixed, as in the whole lane.
S2  scope: every quantifier in Q1, Q2, G3, G4 ranges over D and only D;
    the word stratum never carries a claim.
S3  independence: any Q2 falsifier is double-checked by an independent
    direct path before firing; endpoint inertias come from the
    parents' multi-path machinery; a break attempt with independent
    code follows the accepted run.
S4  the flow convention is the parent's; the opposite convention swaps
    the profiles and negates every flow coherently.
S5  granularity: whole coordinates and whole copy-blocks only; this is
    the frozen definition of the class, per the owner gate.
```

## Field 5. FAILURE THRESHOLD (corrected incubation discipline)

Prereg freeze absolute at the SHA-256 of this file; no field moves
after it. Verifier construction and debugging before the accepted run
is ordinary work, disclosed by superseded hashes. The accepted run is
declared exactly once by pinning verifier and stdout hashes. After that
pin: any FAIL line in the accepted stdout fires the candidate on the
gated claim; a defect demonstrated to be in the verifier rather than in
a gated claim, a gate name exceeding its test, or a check beyond this
specification is an integrity STOP; the candidate is then dead under
this id and a successor takes a new name. A fired Q1 or Q2 is a
first-class outcome, archived, never hidden; thresholds, M, and the
domain rule never move.

## Field 6. ACTION LAYER AND NON-CLAIMS

Layer L1 throughout. Not claimed: anything about the full 2^65
substrate or any domain other than D; any coverage theorem; entry-level
subset minimality (out of reach, order C(109,14) maximal subsets);
minimality against linear combinations (empty claim, a generic
projection decides any finite pool); anything of degree 3 or higher;
uniqueness at dimension 15 (Q3, not posed); sufficiency of any layer
beyond D; the owner [H] that orientation lives in the [22] sector stays
[H] regardless of outcome; nothing about zeta zeros, RH, Weil
positivity, explicit formulae, the infinite operator, J, p = 5,
decoder, measure, physical readings, or L2-L6 lifts. No registry row,
no status movement, no public movement of any kind from this candidate
alone.
