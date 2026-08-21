# PREREG C-K4-W2-OPPOSITE-FIBER-1

```text
CANDIDATE:    C-K4-W2-OPPOSITE-FIBER-1
STATUS:       incubation candidate, NO AUTHORITY, promotes nothing
PUBLIC BASIS: Public Canon v44, main = tag canon-v44 =
              1417b533944e85106901079cc73ae7a0c3c42dc2, STATE ACTIVE, the
              sole authority after the cutover
PARENTS:      C-K4-FIBER-EQUATION-SOLVER-1, SEALED, both legs
              byte-identical, stdout f695aa7a...; its exact fiber
              equations and its 252-pattern class are consumed unchanged.
              Earlier k4 parents supply the substrate and F_109.
DIRECTION:    fiber-first. The attack runs from the fiber space toward a
              spectral cut, never from the known two-profile tables
              outward. That reversal is the methodological point of this
              id and is enforced by Field 3.
LAYER:        L1 only. One session per candidate; this document claims it.
```

## What the sealed parent established, and what remains

```text
for every m in M_2, |M_2| = 252:  there is v in {0,1}^65 with
                                  F_109(v) = F_109(v xor m)
```

Fiber pairs of weight 2 exist for every pattern, constructed rather than
found. The thin-fiber reading is dead. All the rarity therefore sits in
one intersection, which is the only object this candidate attacks:

```text
V_m  intersect  S_pm  intersect  (S_pm xor m)
```

where V_m is the 0/1 solution set of the exact linear fiber equations.

## The frozen question

```text
does there exist m in M_2 and v in {0,1}^65 with
    F_109(v) = F_109(v xor m)
    P(v) = (7,0,9)  and  P(v xor m) = (9,0,7),  or the reverse orientation
```

This is a global existence question over the whole stratum for the
complete weight-2 mask class. It is not a domain test, and no wording of
this document may reduce it to one.

## The three frozen outcomes, and nothing between them

```text
OPPOSITE-W2-FOUND      explicit (m, v). Both profiles confirmed exactly by
                       two independent paths, F_109 equality confirmed by
                       direct coordinate comparison. One witness
                       FALSIFIES T-A over all of S_pm, immediately.
OPPOSITE-W2-EMPTY      all 252 masks completely decided, every
                       intersection empty. Theorem-grade candidacy for
                       "T-A holds for every fiber mask of weight 2", and
                       explicitly NOT a proof of T-A without a weight
                       bound.
INCOMPLETE             at least one mask left undecided at the frozen node
                       budget. Nothing is interpreted, in either
                       direction, about any mask or about T-A.
```

## Field 1. EQUATION (gates)

```
G0  RECONSTRUCTION. Rebuild the substrate, F_109, the profile map and the
    exact fiber equations from the sealed parent; reprint the equation
    proof; assert the 252-pattern class and the 109 coordinates.
G1  SPECTRAL PATHS. Two independent exact profile computations are
    established and cross-checked on a frozen sample before any search:
    the fraction-free symmetric elimination of the parent machinery and
    the Berkowitz characteristic-polynomial sign count. Gate: the two
    paths agree on every table of the frozen sample. Numerical
    eigenvalues appear nowhere, at no stage, for any purpose.
G2  FIBER-FIRST SEARCH. For each of the 252 patterns, in ascending frozen
    order, search V_m for a member whose two endpoints carry opposite
    profiles:
      elimination and propagation on the exact fiber equations fix or
      constrain bits, exactly as in the sealed parent;
      deterministic backtracking over the remaining free bits only, in
      the frozen static order of the parent (decreasing coefficient mass,
      ties by ascending index), branching 0 before 1;
      at each leaf both endpoint profiles are computed exactly by the two
      independent paths of G1 and required to agree;
      NO spectral pruning is applied at internal nodes. This candidate
      claims no safe exact spectral bound and does not pretend to one; a
      later id may add one after proving it never discards a reachable
      target inertia.
    Node budget B = 3000000 per pattern, counted as branch nodes.
    Per-pattern outcome: FOUND with witness, EMPTY with the tree
    exhausted inside B, or UNDECIDED at exactly B nodes.
G3  DECISION. Aggregate to exactly one of the three frozen outcomes
    above. Any UNDECIDED pattern forces INCOMPLETE regardless of how many
    others are EMPTY, and the count of each per-pattern outcome is
    printed.
G4  REGRESSION, last. The seventeen reals, the G6 pair, the known
    equal-F_109 mask and the sealed E' counts are checked for consistency
    with the machinery. They are search inputs NOWHERE: no start point of
    G2 comes from them, which is exactly the reversal this id exists to
    perform. They add no independent evidence.
```

## Field 2. CODE

`verify_k4_w2_opposite_fiber_1.py`, assembled from the sealed parent
machinery plus the search; hash recorded after this freeze. Python
standard library only; exact integers and Fractions; no float anywhere;
no numerical eigenvalue routine anywhere; deterministic stdout;
environment LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
TZ=UTC. Two platforms, byte-identical stdout. The node budget B is the
only bound with scientific standing; wall time is operational only.

## Field 3. CARRIER AND DATA

No external data, no network, no randomness. The search space of G2 is
V_m for the 252 weight-2 patterns, entered through the fiber equations
alone. Explicitly forbidden as a search input, by construction and not
merely by intent: the seventeen real failures, the G6 pair, the sealed E'
and any table set derived from them. The G1 sample and the G4 regression
objects are the only places any previously seen table appears, and
neither can influence a search start.

## Field 4. SYSTEMATICS

```
S1  polarization t(1) = -1 fixed.
S2  scope: the question is global over S_pm for the weight-2 mask class;
    FOUND carries to S_pm because a witness is a witness; EMPTY carries
    only to that mask class and never to T-A without a weight bound.
S3  independence: both endpoint profiles at every leaf come from two
    exact paths that must agree; a disagreement is an integrity STOP, not
    a scientific result.
S4  no spectral pruning is claimed or used; the budget absorbs the cost.
S5  the intersection V_m and S_pm is the target; the parent's finding
    that V_m is large is the reason this search can exist at all, and it
    moves no threshold here.
```

## Field 5. FAILURE THRESHOLD

Prereg freeze absolute at the SHA-256 of this file. Verifier construction
and debugging before the accepted run is ordinary work, disclosed by
superseded hashes; the accepted run is declared once by pinning verifier
and stdout. After the pin: a disagreement between the two spectral paths,
a defect in the verifier rather than in a claim, a gate name exceeding
its test, a check beyond this specification, or any change to B, to the
orders, to the pattern class or to the forbidden inputs is an integrity
STOP. INCOMPLETE and OPPOSITE-W2-FOUND and OPPOSITE-W2-EMPTY are all
ordinary reportable outcomes; a firing of T-A is first-class progress and
is pinned, never hidden.

## Field 6. ACTION LAYER AND NON-CLAIMS

Layer L1 throughout. Carried verbatim from the sealed predecessors:

No claim is made that F_109 separates tables, S_4 orbits, isotypic
components, or arbitrary invariant-polynomial classes. The sole question
is whether flow is constant on every fiber of the frozen map F_109 over
the frozen two-profile locus S_pm of the stratum S.

Additionally not claimed: any statement about masks of weight above 2;
any proof of T-A from an empty weight-2 sweep; any safe spectral pruning;
any structural no-go theorem, which is the named successor route and is
NOT opened here; the cubic [22] frontier, still asleep; any further
compression object or enlarged flip domain, both closed by owner
decision; anything about zeta zeros, RH, Weil positivity, explicit
formulae, the infinite operator, J, p = 5, decoder, measure, physical
readings, or L2-L6 lifts. No registry row, no status movement, no public
movement from this candidate alone.
