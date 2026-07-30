# PREREG P-READ-REDUNDANCY-1

Public preregistration. Frozen before any formal gate execution. Claimed in
issue #216.

```text
probe            P-READ-REDUNDANCY-1
branch           probe/P-READ-REDUNDANCY-1
path             probes/P-READ-REDUNDANCY-1/
owner            mathorn1973
informs          MINIMAL-READ-DERIVATION [O], program DECODER_CORE
closes           nothing
basis            Public Canon v27, STATE ACTIVE, AUTHORITY mathorn1973/twist-j main
                 tag              canon-v27
                 CONTENT_COMMIT   116b62edf505914d96fcd65318d97f3675c53f85
                 CANON_SHA256     c7c4c7e6d5a3116e356b060eaf696963285b0f2f465d5f2e1dcda5c094a309f6
                 CANON_BYTES      150959
                 canon/SHA256SUMS 5 of 5 OK
provenance       incubation candidate C-READ-REDUNDANCY-1, landed as
                 NON-CANONICAL notes in pull request 211. That bundle carries
                 no authority and its runs predate any public pin, so this
                 probe re-preregisters and re-runs rather than importing.
```

## Field 1. Equation and statement

**Coefficient rings.** `R = Z_S`, the localization of `Z` at a set of primes
`S`. Instances tested: `S` in `{ {} (that is Z), {2}, {5}, {2,5}, {2,3,5} }`
and `Q`. The registered-place instances are `S = {2}` (the prime 2 read place)
and `S = {2,5}` (both registered places); citation `Z2-PLACES-SPLIT [T]`,
`TWO-PLACE-PHYSICS [D]`. The identification of admissible accumulator constants
with `Z_S` is an auxiliary clause, field 4 item A3.

**Funnel.** A finite DAG: input ports `s_1..s_m`, internal nodes computing
addition, multiplication and constants from `R`, one terminal output port, no
edge from any output back to the autonomous state (citation: `canon/CORE.md`,
decoder outputs never feed the state update), acyclic. Composition closure:
every total funnel computes a polynomial `P` in `R[x_1..x_m]`, and every such
`P` is realized by a funnel, so total classes are polynomial classes and the
graph shape adds no constraint beyond totality.

**Cover datum.** `m` equal copies of one velocity value `v`, the same velocity
under `m` band descriptions. Per `COIN-SELECTION-CONDITIONAL [T]` the
admissible pair has generic and rung multiplicities `m in {2, 1}` for `w = 1`
(`beta_1`) and `m in {6, 5}` for `w = 3` (`beta_3`).

**Read semantics, the DIAG condition.** The accumulator output on the diagonal,
all ports carrying `v`, equals `v` itself, identically in `v`. Citation with
one inference step: `DRIFT-IS-THE-READ [T]` defines the read as returning the
drift value in the registered normalization with coherent range
`[-beta_1, beta_1]`; a rescaled output `c v` with `c = 6` leaves the velocity
ball at generic `v` since `(6 beta_1)^2 = 36/5 > 1` exactly, so factor
absorption is not available at `m = 6`. The honest asymmetry is recorded:
`(2 beta_1)^2 = 4/5 < 1`, so at `m = 2` the exclusion of a rescale rests on the
read semantics, not on the range.

**Clauses, the two poles and their negations.**

```text
ANON    output invariant under every permutation of the input ports
        (anonymous copies: no port identity available to privilege one)
TOTAL   the accumulator is a total polynomial map over R (no domain
        restriction, no partiality)
TYPED   negation of ANON: ports carry distinct translation-invariant types
        (the offset unit-interval index of the band cover), and wiring may
        depend on the type
PART    negation of TOTAL: the map may be restricted to the diagonal, where
        the common value is well defined
```

`CARRY(m, class, R)`: an admissible accumulator exists in the class over `R`
whose output equals `v` identically on the diagonal.

**The three frozen statements.** The probe carries exactly these and nothing
else.

```text
A.  Absence of feedback alone does not bound finite read redundancy.
    CARRY(6, TYPED, Z) holds by an explicit projection funnel, a wire from
    the type-0 port to the output with zero arithmetic nodes; and
    CARRY(m, ANON+TOTAL, Q) holds for every m. Acyclicity, no-feedback,
    integrality and totality together obstruct nothing.

B.  CARRY(m, ANON+TOTAL, Z_S) holds if and only if every prime factor of m
    lies in S.
    Necessity: in the monomial symmetric basis the diagonal identity forces,
    on its weight-1 stratum, the single equation m c_(1) = 1 in R, since (1)
    is the only weight-1 partition and every basis element contributes
    diagonal degree equal to its weight; hence 1/m in R.
    Sufficiency: P = (x_1 + .. + x_m)/m.

C.  The result only informs MINIMAL-READ-DERIVATION. It does not close it,
    and it does not derive beta_1 as the physically canonical coin.
```

**Corollary recorded inside B, not as a separate claim.** For any `S` with
`3 not in S`, in particular both registered-place instances, `CARRY(6)` fails
while `CARRY(2)` holds whenever `2 in S`; on rungs `CARRY(1)` holds over `Z`
and `CARRY(5)` holds iff `5 in S`.

**Anti-rhetoric fence, part of the frozen statement.** The `B` selector is a
prime-support selector, not a smaller-is-better principle. On hypothetical
generic-multiplicity pairs over `S = {2,5}` it gives: `{2,6}` forces the
2-cover; `{2,10}` is nonunique, both carry; `{6,10}` forces the **larger**
cover. The argument can fail and can pick the larger cover.

## Field 2. Code

```text
verifier   probes/P-READ-REDUNDANCY-1/verify.py
rules      Python standard library only; Fraction and integer arithmetic only;
           no float anywhere in any assertion or any printed field; runs from
           the repository root in well under 120 s with
           LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
           deterministic output, no wall-clock, no hostname, no nickname
```

The verifier merges the constructive legs and the independent brute-force legs
of the incubation candidate into one file. Its groups are:

```text
A1  composition closure sample: a three-node funnel equals its polynomial
A2  typed projection witness carries m = 6, every port order, Q and Q(sqrt5)
A3  the sixfold cover: 6 sheets, translation-invariant offsets, distinct types
A4  PART pole: the diagonal common-value map carries every m in 1..8
A5  WALL: over Q every m in 1..12 carries
B1  orbit counts, closed formula against explicit enumeration
B2  weight-1 stratum is exactly {(1)} with orbit count m, and every monomial
    symmetric basis element has diagonal degree equal to its weight
B3  ring table: 1/m in Z_S iff primes(m) subset S, with hand-checked cells
B4  sufficiency witnesses P = e_1/m over the minimal ring
B5  necessity by exhaustion at m = 2: every integer symmetric combination in
    the monomial basis, weight <= 4, coefficients in [-2,2], semantic diagonal
    test at v in 1..5; expect zero hits
B6  necessity by exhaustion at m = 6, dyadic power-sum family
    (a p_1 + b p_1^2 + c p_2)/2^k, a,b,c in [-32,32], k in 0..6; expect zero
B7  necessity by exhaustion at m = 6, dyadic elementary family
    (a e_1 + b e_2 + c e_3)/2^k, same boxes; expect zero
B8  independent cross-check of one ring cell by a route that does not use the
    prime-support rule: 6a = 10^k has no solution for k <= 12
C1  registered places: m = 1 free over Z, m = 2 needs the prime 2, m = 6 is
    obstructed because it needs the prime 3, m = 5 needs the prime 5
C2  blindness table: {2,6} forces 2; {2,10} nonunique; {6,10} forces 10
C3  range asymmetry: (6 beta_1)^2 = 36/5 > 1 and (2 beta_1)^2 = 4/5 < 1
```

`B5`, `B6`, `B7` and `B8` are independent code paths: they evaluate candidate
accumulators semantically on the diagonal and never reuse the coefficient
argument that `B2` establishes.

## Field 3. Carrier and data

No external data, no file, no network. Enumerated objects: integer partitions
of weight at most `D = 4` with at most `m` parts, for `m in {1, 2, 5, 6}`; the
brute-force coefficient boxes of field 4; and the explicit witness funnels
written in the code. The band-offset structure is recomputed from scratch: for
noninteger rational `x` and `w = 3` the cover sheets are the six integers `n`
with `|x - n| < 3`, and the offset multiset `{x - n}` is checked to be
translation invariant.

## Field 4. Systematics, auxiliary clauses, frozen bounds

```text
A1  accumulator = arithmetic circuit over {+, x, constants from R}; division
    appears only as multiplication by a constant of R. Auxiliary, not citable
    to a public row: the program's exact integer style motivates it, nothing
    seals it.
A2  ANON and TOTAL as the formalization of "no channel to reconcile", TYPED
    and PART as the negations. A third public reading may exist; residual
    risk, explicitly left to the owner of MINIMAL-READ-DERIVATION [O].
A3  constants ring identified with Z_S at the registered places. Auxiliary;
    motivated by Z2-PLACES-SPLIT [T] and TWO-PLACE-PHYSICS [D].
A4  frozen brute-force boxes, stated before execution and never widened after
    it:
    B5  m = 2, ANON class in the monomial symmetric basis, weight <= 4 (eight
        basis elements), integer coefficients in [-2,2], semantic diagonal
        test at v in {1,2,3,4,5}; expected zero hits, 390625 candidates.
    B6  m = 6, dyadic power-sum family, integer a,b,c in [-32,32], k in [0,6],
        semantic diagonal test at v in {1,2,3}; expected zero hits, 1922375
        candidates.
    B7  m = 6, dyadic elementary family, same boxes; expected zero hits,
        1922375 candidates.
    Beyond these boxes the enumerative legs assert nothing. The all-m,
    all-degree content of B rests on the written symbolic proof, whose stratum
    structure the verifier machine-checks at D <= 4 and whose weight-1
    equation is degree independent.
A5  no float. Any float in the code path is itself a failure of the gate.
A6  the exhaustion legs are corroboration of the symbolic proof of B, never a
    substitute for it. A public status that rests only on the finite boxes is
    at most C.
```

## Field 5. Failure threshold and outcome map

Binary, exact, no tolerance. Thresholds are frozen here and are not moved after
the pin. The probe fails if any of the following fires.

```text
F1  B5 finds a symmetric integer accumulator satisfying the diagonal identity
    at m = 2 (kills the necessity direction of B)
F2  the typed projection witness of A fails its identity or clause checks
    (kills A)
F3  a coefficient-system conclusion and a brute-force conclusion disagree on
    any shared point (code defect; both are archived)
F4  B6 or B7 finds a dyadic ANON TOTAL accumulator at m = 6 (kills the
    corollary inside B)
F5  the orbit-count or basis cross-check fails at any tested (m, D)
F6  the ring table disagrees with the independent cross-check of B8
F7  any float appears in an assertion or an emitted field
F8  the local formal leg and the required GitHub leg differ in any byte
```

A fired falsifier is merged, not hidden, and is recorded in `RESULT.md` with
the exact witness. If `F1` or `F4` fires, statement `B` is dead and the
promotion proposal that carried it dies with it.

Proposed registry falsifier text, if a public row is later folded:

```text
fires if a symmetric total polynomial accumulator over Z_S returns the common
value identically at a multiplicity m with a prime factor outside S, if the
typed projection or diagonal common-value witnesses fail on their stated
domains, if a weight-1 partition other than (1) exists, if a monomial
symmetric function has diagonal degree differing from its weight, or if the
aarch64 and x86_64 transcripts differ
```

## Field 6. Action layer

```text
declared layer   L5 read structure over the L1 coin carrier. No lift is
                 performed.
not touched      GATE-L5-L1-MINIMAL-READ is owned by MINIMAL-READ-DERIVATION
                 [O] and is not touched by this probe.
not claimed      no L6, measurement, Born, SI, decoherence, environment or
                 unique-physics content anywhere. No closure of
                 MINIMAL-READ-DERIVATION [O] in either direction, no change to
                 COIN-MINIMAL-READ [H], and no derivation of beta_1 as the
                 physically canonical coin.
scheduler        the O row's own decision text governs: failure of one favored
                 route is STOP unless it classifies the complete registered
                 decoder class. This probe classifies one clause pair, not the
                 class, so the row stays O and STOP whatever the outcome.
```

## Two-architecture protocol

For a computation-only promotion to `T` the local formal leg must be `aarch64`
and the required GitHub leg `x86_64`; byte-identical stdout across the two
satisfies the gate. Same-architecture agreement is a reproduction, not the
gate, and leaves a computation-only result at most `C`. Statement `B` has a
short symbolic proof independent of any run, so an independent proof reading
may earn `T` with the verifier serving as audit.
