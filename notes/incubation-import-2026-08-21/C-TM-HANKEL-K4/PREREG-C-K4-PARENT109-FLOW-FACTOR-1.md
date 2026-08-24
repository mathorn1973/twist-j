# PREREG C-K4-PARENT109-FLOW-FACTOR-1

```text
CANDIDATE:    C-K4-PARENT109-FLOW-FACTOR-1
STATUS:       incubation candidate, NO AUTHORITY, promotes nothing
REVISION:     revision 1, the frozen text. Revision 0, sha256
              d3ff23ce26c5568f27076ca3ede2f381a72dfd4cd4b23abb71deb7c3fb66281b,
              is superseded and archived. NOTHING was computed against
              revision 0: no verifier existed, no gate ran, no threshold
              moved. Revision 1 carries the owner's five formulation
              corrections of 2026-08-11, every one of which tightens the
              claim or the disclosure. The id is retained because neither
              E' nor the search space changed; had either moved, this id
              would have died unused and a successor would carry it.
PUBLIC BASIS: Public Canon v44, main = tag canon-v44 =
              1417b533944e85106901079cc73ae7a0c3c42dc2, STATE ACTIVE,
              re-read at freeze time
PARENTS:      C-TM-HANKEL-K4-SUBSTRATE-1 (substrate, cell order, the
              canonical 109-entry map F_109), C-TM-HANKEL-K4-SPECTRAL-
              FLOW-2 (flow convention, profile locus),
              C-TM-HANKEL-K4-SUBOBJECT-MINIMALITY-3 (FIRED; machinery
              reused, claims not)
RECON IN:     RECON-PAIR-FIRST-K4 and RECON-FIBER-MECHANISM-K4, both
              NON-CANONICAL and disclosed below
LAYER:        L1 only. One session per candidate; this document claims it.
```

## The claim

The stratum S is the abstract k = 4 substrate: 65 free cells, 2^65 sign
tables. Define the domain of the claim as a SUBSET of S, not as a
coordinate:

```text
S_pm := { x in S : profile(x) in { (7,0,9), (9,0,7) } }
```

On S_pm the flow is the sign of the profile in the frozen parent
convention, +1 on (7,0,9) and -1 on (9,0,7). T-A is then, with no second
antecedent of any kind:

```text
T-A   for all x, y in S_pm:  F_109(x) = F_109(y)  =>  flow(x) = flow(y)
```

Equivalently: no opposite-flow pair of S_pm lies in one fiber of F_109;
flow factors through F_109 on S_pm. The profile appears only in the
definition of S_pm and as the target label. It is not a quotient
coordinate and no gate may treat it as one. This wording is deliberate:
an earlier draft carried the profile as a second antecedent, which would
have made the implication vacuously true, since flow is a function of the
profile by definition. That degenerate reading is now syntactically
impossible.

## The asymmetry, and its exact reach

```text
FIRED     one opposite-flow pair in one F_109 fiber, found anywhere,
          falsifies T-A over S_pm outright. A witness is a witness.
UNFIRED   no positive claim of any kind. The recorded outcome is
          "T-A unfired at the declared search scope", the hypothesis
          keeps its [H] grade, nothing is promoted.
```

The bound 2^65, about 3.7 . 10^19, rules out ENUMERATION of S_pm, and
therefore rules out confirming T-A by this or any computational probe of
this shape. It does NOT say T-A is unconfirmable in principle: a
structural proof would confirm it, and finding one is a legitimate future
route. UNFIRED must never be read, quoted, or summarized as a proof or as
evidence for T-A. The domain is an instrument, never a claim; that is the
direct correction of the fired third cut.

## Field 1. EQUATION (gates, in the owner's frozen order)

```
G0  RECONSTRUCTION. Rebuild from the parents, unchanged: the 65-cell
    substrate and cell order; K linear in the signs; the extremal
    skeleton endpoint NEG 8 ZERO 0 POS 8; S_pm and the flow convention;
    F_109 with its four layer slices; multiplicities (10, 12, 5, 3, 0);
    parent_coordinates 109. Print the claim and the asymmetry above
    verbatim. No known-failure input in any construction step.
G1  T-A, MAIN GATE. Search for an opposite-flow pair inside one F_109
    fiber over the frozen search space, in three arms:
    A1 single-swap (weight 2) fiber neighbours of the first 400 tables
       of E' in ascending bits order;
    A2 disjoint-double-swap (weight 4) fiber neighbours of 40 tables of
       E' taken by a fixed stride;
    A3 the mechanism family: the orbit Orb_S4(m) = { g . m : g in S_4 }
       of the recon mask m = {21, 41, 37, 61}, as a SET of distinct
       images. The verifier computes the stabilizer, removes duplicates
       and PRINTS the actual orbit size; no orbit size is assumed and
       triviality of the stabilizer is not a hidden premise. Every mask
       of the orbit is applied to every table of E' on which it acts as
       two orbit-preserving swaps.
    Gate: no opposite-flow pair shares an F_109 value in any arm. Every
    candidate collision is rechecked by an independent path, explicit
    coordinate-by-coordinate comparison of the two 109-vectors plus
    recomputed endpoint inertia by two exact paths, before the gate may
    fire. Also printed, gating nothing: same-flow fiber pairs per arm.

    EXHAUSTIVE, bounded once and for all: in A1 and A2 exhaustive means
    exhaustive within the frozen local move class around the frozen
    bases, NOT exhaustive over S_pm. In A3 it means the full computed
    mask orbit against every eligible table of E', again not over S_pm.
G2  T-B, COMPRESSION ARM. F_14 = the eight orbit sums with indices 0 to
    7 together with the full gram211 block, dim 8 + 6 = 14, decides flow
    on E'. Gate: no two tables of E' share the F_14 projection and
    differ in flow. E' does not grow, whatever the outcome. PASS means
    at most survival on E', grade candidate-C on E', and says nothing
    about S_pm. FIRED means an exact counterexample on E'. T-B does not
    steer T-A and its outcome cannot alter G1.
G3  REGRESSION AND READBACK SET, last. The seventeen real failures and
    the G6 pair are evaluated here. They are NOT a held-out set in the
    strong sense and are not called one: the recon has seen them, and
    the G6 pair is what motivated arm A3. They can expose an
    implementation error or a contradiction with an earlier record;
    they add no independent evidence. Reported: F_14 on the reals and
    on E' union reals, F_109 fibers across that union. A hit is a break
    of the EXTENSION of a gated statement, explicitly distinct from the
    gates, which stand or fall on E' alone.
G4  DIAGNOSTICS, gating nothing: d_min over the third cut's admissible
    class on E', searched to cost 8 and reported as "at least 9" if not
    reached; mixed-bucket counts per layer; orbit relation of any fiber
    pair found; eligible and preserved counts of the mechanism family.
```

## Field 2. CODE

`verify_k4_parent109_flow_factor_1.py`, assembled from the pinned parent
machinery plus the gates above; hash recorded after this freeze. Python
standard library only; exact integer and Fraction arithmetic; no float
anywhere; deterministic stdout; environment LC_ALL=C LANG=C
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC. Two platforms,
byte-identical stdout, x86_64 and aarch64. Declared budget 3600 seconds,
a disclosed deviation from the 120 second public style forced by the
exact-inertia volume of E' and by the slower aarch64 leg; a later public
probe re-engineers or re-scopes it.

## Field 3. CARRIER AND DATA, the frozen domain E'

Abstract only. The seventeen reals and the G6 pair enter at G3 and
nowhere else. One stream throughout: 64-bit LCG, x_0 = 1, multiplier
6364136223846793005, increment 1442695040888963407, steps numbered from
1. Steps 1 to 4000 are discarded. Table i, for i = 0, 1, 2, ..., consumes
steps 4001 + 2i and 4002 + 2i, and is
bits = (x_lo mod 2^33) + ((x_hi mod 2^32) << 33).

```text
D     tables i = 0..3999, that is stream steps 4001..12000, two-profile
      kept; then single-cell flips over every member plus the substrate
      witness 0x02e639472cd318ed2; then double-cell flips over the first
      40 members in ascending bits order. Identical to the third cut's
      frozen domain.
B2    tables i = 4000..7999, that is stream steps 12001..20000, no
      further discard, two-profile kept; then single-cell flips over
      every member of B2; then double-cell flips over the first 40
      members of B2 in ascending bits order.
T3    triple-cell flips, all C(65,3) = 43680 of them, over the first 3
      members of D in ascending bits order, two-profile kept.
E'    the union of D, B2 and T3, deduplicated by bits, enumerated in
      ascending bits order. No other table is admitted at any point, for
      any reason, whatever the gates return.
```

The verifier itself asserts that the two table-index intervals
[0, 3999] and [4000, 7999], equivalently the step intervals
[4001, 12000] and [12001, 20000], are disjoint, and prints the number of
bit values common to the two blocks' two-profile sets as a finding.

## Field 4. SYSTEMATICS

```
S1  polarization t(1) = -1 fixed, as in the whole lane.
S2  scope: G1 and G2 quantify over E' only; the falsification direction
    of T-A carries to S_pm because a witness is a witness, the
    confirmation direction does not carry and is never asserted.
S3  independence: every candidate fiber collision is confirmed by a
    second exact path before firing; endpoint inertias come from the
    parents' multi-path machinery.
S4  disclosed recon, motivating this freeze and nothing else: the blind
    radius-4 fiber search found zero collisions in 289807 moves around
    40 bases, and the one mechanism mask preserved F_109 on 179 of 6943
    eligible tables with zero profile flips. Those numbers are the
    reason a freeze is warranted rather than premature. After this pin
    they move no threshold and no scope, and no later number may.
S5  F_109 is S_4-equivariant, so a live mask stays live on S_4 images;
    any statement that some mask family is rare is probe-dependent and
    is printed as an observation, never as structure.
S6  the mask of A3 came from an abstract equal-F_109 table pair found in
    recon, not from the seventeen and not from the G6 pair; arms A1 and
    A2 are independent of it. G3 is a regression set, not evidence.
```

## Field 5. FAILURE THRESHOLD

Prereg freeze absolute at the SHA-256 of this revision. Verifier
construction and debugging before the accepted run is ordinary work,
disclosed by superseded hashes; the accepted run is declared once by
pinning verifier and stdout. After that pin: a FAIL line fires the gated
claim; a defect in the verifier rather than in a claim, a gate name
exceeding its test, or a check beyond this specification is an integrity
STOP, and the candidate is dead under this id with a successor taking a
new name. E', the arms, the budget and the thresholds never move.

## Field 6. ACTION LAYER AND NON-CLAIMS

Layer L1 throughout. Frozen verbatim at the owner's instruction:

No claim is made that F_109 separates tables, S_4 orbits, isotypic
components, or arbitrary invariant-polynomial classes. The sole question
is whether flow is constant on every fiber of the frozen map F_109 over
the frozen two-profile locus S_pm of the stratum S.

Further not claimed: any confirmation of T-A by any amount of search; any
statement about S_pm from E'; the cubic [22] frontier (T-C, held
NON-CANONICAL and not posed); minimality of F_14 or of anything else;
sufficiency of any layer; any coverage theorem; the completeness of the
seventeen at their bound; anything about zeta zeros, RH, Weil positivity,
explicit formulae, the infinite operator, J, p = 5, decoder, measure,
physical readings, or L2-L6 lifts. No registry row, no status movement,
no public movement from this candidate alone.
