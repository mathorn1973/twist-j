# PREREG C-READ-REDUNDANCY-1

```text
candidate     C-READ-REDUNDANCY-1
lane          incubation (project claude/), targets the public line on
              promotion via PROMO and the public probe protocol
claimed by    incubation session 2026-07-29, workstream A of
              claude/PLAN-DECODER-SECTOR-POST-V27_2026-07-29.md
basis         Public Canon v27, mathorn1973/twist-j main, STATE ACTIVE,
              tag canon-v27, CONTENT_COMMIT
              116b62edf505914d96fcd65318d97f3675c53f85, CANON_SHA256
              c7c4c7e6d5a3116e356b060eaf696963285b0f2f465d5f2e1dcda5c094a309f6,
              canon/SHA256SUMS 5 of 5 OK, verified by clone this session
question      route precondition 5 of
              notes/canon/ADOPT-COIN-MINIMAL-READ-2026-07-29.md section 5:
              does absence of feedback alone bound admissible read
              redundancy? Quoted target: "whether a multiplicity-2w cover
              delivers redundant terminal reads that the architecture
              cannot reconcile and whether the smallest integer-admissible
              value, w = 1, is forced."
authority     none. Candidate labels only. No outcome of this candidate
              closes, moves, or anchors MINIMAL-READ-DERIVATION [O] or
              COIN-MINIMAL-READ [H]; their decision texts govern.
formal runs   zero before this freeze. Only py_compile and other
              non-executing static checks are permitted between the freeze
              and the first run.
```

## Field 1. Equation and statement

Coefficient rings. R = Z_S, the localization of Z at a set of primes S.
Instances tested: S in { {} (that is Z), {2}, {5}, {2,5}, {2,3,5} } and Q.
The registered-place instances are S = {2} (the prime 2 read place) and
S = {2,5} (both registered places); citation: Z2-PLACES-SPLIT [T],
TWO-PLACE-PHYSICS [D]. The identification of admissible accumulator
constants with Z_S is an auxiliary clause (field 4, A3).

Funnel. A finite DAG: input ports s_1..s_m, internal nodes computing
addition, multiplication, and constants from R, one terminal output port,
no edge from any output back to the autonomous state (citation: CORE.md,
decoder outputs never feed the state update), acyclic. Composition
closure: every total funnel computes a polynomial P in R[x_1..x_m], and
every such P is realized by a funnel; so total classes are polynomial
classes and the graph shape adds no constraint beyond totality. This
equivalence is checked at K1.

Cover datum. m equal copies of one velocity value v, the same velocity
under m band descriptions. Per COIN-SELECTION-CONDITIONAL [T]: the
admissible pair has generic and rung multiplicities m in {2, 1} for
w = 1 (beta_1) and m in {6, 5} for w = 3 (beta_3).

Read semantics (the DIAG condition). The accumulator output on the
diagonal (all ports carrying v) equals v itself, identically in v.
Citation with one inference step: DRIFT-IS-THE-READ [T] defines the read
as returning the drift value in the registered normalization with
coherent range [-beta_1, beta_1]; a rescaled output c v with c = 6 leaves
the velocity ball at generic v since (6 beta_1)^2 = 36/5 > 1 exactly, so
factor absorption is not available at m = 6 (recorded as K12; note the
honest asymmetry: (2 beta_1)^2 = 4/5 < 1, so at m = 2 the exclusion of a
rescale rests on the read semantics, not on the range).

Clauses (the two poles and their negations):

```text
ANON    output invariant under every permutation of the input ports
        (anonymous copies: no port identity available to privilege one)
TOTAL   the accumulator is a total polynomial map over R (no domain
        restriction, no partiality)
TYPED   negation of ANON: ports carry distinct translation-invariant
        types (the offset unit-interval index of the band cover), and
        wiring may depend on the type
PART    negation of TOTAL: the map may be restricted to the diagonal,
        where the common value is well defined
```

CARRY(m, class, R): an admissible accumulator exists in the class over R
whose output equals v identically on the diagonal.

Statements under test:

```text
S1  TYPED pole: CARRY(6, TYPED, Z) holds by an explicit projection
    funnel (wire from the type-0 port to the output, zero arithmetic).
    Consequence if it holds: no-feedback, acyclicity, integrality and
    totality together bound nothing; the route as sketched is dead
    (plan outcome W6).
S2  ANON + TOTAL pole: CARRY(m, ANON+TOTAL, Z_S) holds iff every prime
    factor of m lies in S. Necessity: in the monomial-symmetric basis
    the diagonal identity forces, on its weight-1 stratum, the single
    equation m c_(1) = 1 in R, since (1) is the only weight-1 partition
    and every basis element contributes diagonal degree equal to its
    weight; hence 1/m in R. Sufficiency: P = (x_1 + .. + x_m)/m.
    This is the candidate redundancy theorem (plan outcome OBS) and, over
    Q where every m carries, the tolerance statement (plan outcome WALL:
    the graph never obstructs; the ring does).
S3  Selection corollary: for any S with 3 not in S (both registered-place
    instances), CARRY(6) fails and CARRY(2) holds whenever 2 in S; rungs:
    CARRY(1) holds over Z, CARRY(5) holds iff 5 in S. Under ANON + TOTAL
    with registered-place constants, w = 1 is forced among the admissible
    pair {beta_1, beta_3}: the sixfold read requires the prime 3, which
    the architecture does not carry; the twofold read requires only the
    prime 2, which the read place carries.
S4  PART pole: the diagonal common-value map carries every m; dropping
    TOTAL voids every bound.
S5  Blindness table for the S2 selector over S = {2,5}, on hypothetical
    generic-multiplicity pairs: {2,6} forces the 2-cover; {2,10} is
    nonunique (both carry); {6,10} forces the 10-cover. The argument can
    fail and can pick the larger cover; it is not smaller-is-better
    rhetoric.
```

The deliverable is the flipping clause: the sixfold carry flips exactly
on {ANON, TOTAL, 3 not in S}; each single relaxation (TYPED, PART, or
3 in S) restores it. S1 with S2 together answer the question as posed:
absence of feedback ALONE bounds nothing; absence of reconciliation,
formalized as ANON + TOTAL, bounds admissible multiplicities to those
whose prime support the constant ring carries.

## Field 2. Code

verify_read_redundancy_1.py (constructive witnesses, coefficient-system
checks, ring tables, blindness table) and break_read_redundancy_1.py
(independent brute-force legs and witness attacks). Python 3 standard
library only. Fraction and integer arithmetic throughout; Q(sqrt5)
values as exact pairs (a, b) meaning a + b sqrt5 where used; no float
anywhere. Each script runs from a clean directory in under 120 s with
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
Verifier exit 0 iff all checks pass. Breaker exit 0 iff no falsifier
fires; a found counterexample prints its witness and exits 1.

## Field 3. Carrier and data

No external data. Enumerated objects: integer partitions of weight at
most D = 4 with at most m parts, for m in {1, 2, 5, 6}; the brute-force
coefficient boxes of field 4; the explicit witness funnels written in
the code. The band-offset structure is recomputed from scratch: for
noninteger rational x and w = 3, the cover sheets are the six integers n
with |x - n| < 3 and the offset multiset {x - n} is checked to be
translation invariant.

## Field 4. Systematics, auxiliary clauses, frozen bounds

```text
A1  accumulator = arithmetic circuit over {+, x, constants from R};
    division appears only as multiplication by a constant of R.
    Auxiliary (not citable to a public row); the program's exact integer
    style motivates it, nothing seals it.
A2  ANON and TOTAL as the formalization of "no channel to reconcile",
    TYPED and PART as the negations. A third public reading may exist;
    residual risk, explicitly left to the owner of
    MINIMAL-READ-DERIVATION [O].
A3  constants ring identified with Z_S at the registered places.
    Auxiliary; motivated by Z2-PLACES-SPLIT [T] and TWO-PLACE-PHYSICS [D].
A4  frozen brute-force boxes:
    B1  m = 2, ANON class in the monomial-symmetric basis, weight <= 4
        (eight basis elements), integer coefficients in [-2, 2],
        semantic diagonal test at v in {1, 2, 3, 4, 5}; expect zero hits.
    B2  m = 6, dyadic family (a p_1 + b p_1^2 + c p_2)/2^k with
        p_1 = x_1 + .. + x_6, p_2 = x_1^2 + .. + x_6^2, integer a, b, c
        in [-32, 32], k in [0, 6], semantic diagonal test at
        v in {1, 2, 3}; expect zero hits.
    Beyond these boxes the enumerative legs assert nothing; the all-m,
    all-degree claims rest on the written symbolic proof of S2, whose
    stratum structure the verifier machine-checks at D <= 4 and whose
    weight-1 equation is degree-independent.
A5  single platform this session; every label below is a candidate
    label. Two-architecture byte identity belongs to the later public
    probe, not to this candidate.
```

## Field 5. Failure threshold and outcome map

Falsifiers. The candidate is falsified, candidate-F, archived not
deleted, thresholds never moved, if any one fires:

```text
F1  B1 finds a symmetric integer accumulator with the diagonal identity
    at m = 2 (kills S2 necessity)
F2  the S1 typed witness fails its identity or clause checks (kills S1)
F3  a coefficient-system conclusion and a brute-force conclusion
    disagree on any shared point (code defect; archive both)
F4  B2 finds a dyadic ANON TOTAL accumulator at m = 6 (kills S3)
F5  the orbit-count or basis cross-check fails at any tested (m, D)
```

Outcome labels per plan section 3: W6 and OBS are expected to hold
TOGETHER, because they concern different clause sets (S1 kills the route
as sketched; S2 and S3 ground the repaired route). WALL is S2 over Q.
NULL is any statement neither proved nor falsified inside the frozen
boxes. Every outcome, including a fired falsifier, is archived in the
RESULT doc with the stdout hashes.

## Field 6. Action layer

L5 read structure over the L1 coin carrier. No lift is performed.
GATE-L5-L1-MINIMAL-READ is owned by MINIMAL-READ-DERIVATION [O] and is
not touched. No L6, measurement, Born, SI, decoherence, environment, or
unique-physics content anywhere in this candidate.
