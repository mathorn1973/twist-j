# C-READ-REDUNDANCY-1 RESULT

```text
candidate     C-READ-REDUNDANCY-1, incubation lane, no authority
date          2026-07-29
prereg        claude/PREREG-C-READ-REDUNDANCY-1.md
              sha256 334cb3bf9ef6feaccaa7e48c809e0f2f880c6686c025eee96474fb31c743d0d2
              frozen and written to the project before any execution
basis         Public Canon v27, tag canon-v27, CONTENT_COMMIT 116b62ed,
              SHA256SUMS 5 of 5 OK, verified by clone this session
verifier      verify_read_redundancy_1.py
              sha256 3febde99b4f0c328452bf435406b689a24343c576959f58368b96107b6e5fdcf
              stdout sha256 05d567dc19a3705e7de6fcae4a91cc85964c1b2207d7c2da4fead959d901f3ef
              exit 0, 13/13 PASS
breaker       break_read_redundancy_1.py
              sha256 ac22ddb164d3d835d0f7bac32ea9e33f62f9b2bbc0ec49ce0aec49f347229482
              stdout sha256 4e4aa7b5b1f7ac0fac1f8df754ec68774d4ac55176103cbd655e35dd54b3f2da
              exit 0, NO FALSIFIER FIRED
environment   Linux x86_64, Python 3, LC_ALL=C LANG=C
              PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC,
              stdlib only, int and Fraction only, no float anywhere
platform      ONE platform. Every label below is a candidate label; the
              two-architecture leg belongs to the later public probe.
falsifiers    none of F1 to F5 fired
```

## Headline

The question was route precondition 5: does absence of feedback alone
bound admissible read redundancy? The answer is exact and split:

```text
NO   absence of feedback alone bounds NOTHING. Witnessed twice: the
     typed projection funnel carries the sixfold cover over Z with zero
     arithmetic nodes (S1), and over Q every multiplicity carries (S2
     sufficiency). Acyclicity and no-feedback never obstruct; the graph
     is innocent. Plan outcomes W6 and WALL both realized.
YES  absence of reconciliation, formalized as anonymity of the cover
     sheets plus totality of the accumulator, bounds redundancy exactly:
     over Z_S an anonymous total accumulator carries multiplicity m iff
     every prime factor of m lies in S (S2). Plan outcome OBS realized.
```

The two answers coexist because they concern different clause sets. The
route as sketched (no-feedback implies budget) is dead. The repaired
route (anonymity plus totality plus the registered constant primes
implies budget) is alive and selects. One sentence: acyclicity is free,
anonymity is priced, and the price is a prime. The sixfold read costs
the prime 3, which the architecture does not carry; the twofold read
costs the prime 2, which the read place carries; the rung read of the
beta_1 coin costs nothing at all.

## Statements and labels

```text
S1  candidate-T (exhibition)
    The typed funnel (wire from the type-0 port to the output) carries
    m = 6 over Z: total, acyclic, feedback-free, integer, translation
    invariant (offset types are shift invariant, K6b), zero arithmetic.
    Verified on Q and Q(sqrt5) values under 8 port orders (K6a, B3).
    Consequence: no-feedback + acyclicity + integrality + totality
    together do not bound redundancy. The route as sketched is dead.

S2  candidate-T (symbolic proof, structure machine-checked)
    Anonymous total accumulators over R = Z_S are exactly the symmetric
    polynomials in R[x_1..x_m]. CARRY(m) holds iff 1/m in R iff every
    prime of m lies in S.
    Proof of necessity, four lines: the monomial symmetric functions
    m_lam are an R-basis; on the diagonal m_lam = M_lam v^(|lam|), so
    diagonal v-degree equals weight (K3); the only weight-1 partition is
    (1) with M = m (K3); the diagonal identity P(v..v) = v therefore
    forces m c_(1) = 1 in R, that is 1/m in R. Sufficiency: e_1/m (K5).
    Degree-independent: higher-weight terms cannot reach v^1.
    Independent legs: 390625 integer symmetric candidates at m = 2 give
    zero diagonal identities (B1); 2 x 1922375 dyadic candidates at
    m = 6 in two families give zero (B2, B2b).

S3  candidate-T, conditional on A1, A2, A3 (named in the prereg)
    For any S with 3 not in S, in particular the read place {2} and the
    registered pair {2,5}: m = 6 is obstructed, m = 2 carries when
    2 in S, m = 1 is free over Z, m = 5 carries iff 5 in S (K10).
    Under anonymity + totality + registered-place constants, w = 1 is
    forced among the admissible pair {beta_1, beta_3}.

S4  candidate-T (trivial)
    Dropping totality voids every bound: the diagonal common-value map
    carries every m (K8). It relies on equality of the copies and never
    verifies it; verification would be the reconciliation channel.

S5  candidate-C (computed table)
    Blindness of the selector over S = {2,5}: pair {2,6} forces the
    2-cover; pair {2,10} is NONUNIQUE; pair {6,10} forces the 10-cover
    (K9). The argument can fail and can pick the larger cover. It is a
    prime-support selector, not smaller-is-better rhetoric.
```

Observation (not a claim): the rescale escape is asymmetric in exactly
the right direction. A factor-6 output leaves the velocity ball, since
(6 beta_1)^2 = 36/5 > 1, so at m = 6 not even a units convention can
absorb the redundancy; a factor-2 output stays inside, (2 beta_1)^2 =
4/5 < 1, so at m = 2 the exclusion of rescaling rests on the read
semantics of DRIFT-IS-THE-READ, not on well-formedness (K12).

## The flipping clause, located

```text
The sixfold carry flips exactly on the triple {ANON, TOTAL, 3 not in S}.
Relax any single element and the carry returns:
  drop ANON  (typed ports)        -> S1 projection witness
  drop TOTAL (partial map)        -> S4 diagonal common-value map
  put 3 in S (enlarge constants)  -> K5 witness e_1/6 over Z[1/30]
```

This triple is the constructive content of "no channel to reconcile
them". The two undefined items the public O row already lists, the
cover-to-output map and the accumulator/equality rule, are exactly the
decisions ANON and TOTAL. They are no longer mush; they are two named
bits, and each bit's price is now known.

## Break round

```text
B1   390625 semantic candidates, m = 2, integer symmetric, weight <= 4,
     coefficients [-2,2]: zero pass the five-point diagonal test.
B2   1922375 dyadic power-sum candidates, m = 6: zero.
B2b  1922375 dyadic elementary candidates, m = 6: zero.
B3   the S1 witness survived 50 exact values (large numerators, Q(sqrt5)
     pairs) under 8 fixed port orders.
B4   repair attempts, informational: stripping powers of 2 from 6v
     leaves 3v; stripping powers of 2 and 5 leaves the factor 3. The
     foreign prime survives every registered-place normalization.
B5   independent scan (6a = 10^k has no solution, k <= 12) agrees with
     the prime-support rule: 1/6 is not in Z[1/10].
```

## What this does and does not do

```text
DOES      kill the route as sketched (no-feedback alone) by exhibition;
          supply the candidate redundancy theorem for route
          precondition 5 in conditional form; locate the flipping
          clause; keep both plan outcomes W6 and OBS, which the prereg
          declared compatible.
DOES NOT  close, move, or anchor MINIMAL-READ-DERIVATION [O] or
          COIN-MINIMAL-READ [H]. The O row's own decision text governs:
          failure of one favored route is STOP, and closure in either
          direction requires the complete registered decoder class.
          No lift; GATE-L5-L1-MINIMAL-READ untouched. No L6, Born,
          measurement, SI, decoherence, or unique-physics content.
RESIDUAL  A2: a third public reading of "no reconciliation" may exist;
          the owner of the O row decides. A1: the arithmetic-circuit
          model is auxiliary. Single platform: candidate grade only.
```

## Verifier stdout (verbatim)

```text
C-READ-REDUNDANCY-1 verifier
basis: Public Canon v27, tag canon-v27, content commit 116b62ed
arithmetic: int and Fraction only; no float in this file

K1 composition-closure sample (funnel = polynomial), 10 points PASS
K2 orbit counts formula = enumeration, m in {1,2,5,6}, weight <= 4 PASS
K3 weight-1 stratum = {(1)}, orbit m; diagonal degree = weight PASS
K4 ring table: 1/m in Z_S iff primes(m) subset S; hand cells agree PASS
K5 sufficiency: P = e_1/m carries m over Z_S with primes(m) in S PASS
K6a W6 typed projection returns v, all port orders, Q and Q(sqrt5) PASS
K6b sixfold cover: 6 sheets, offsets shift invariant, types distinct PASS
K7 W2 dyadic: (x1+x2)/2 carries m = 2 over Z[1/2] PASS
K8 PART: diagonal common-value map carries every m in 1..8 PASS
K9 blindness: {2,6} forces 2; {2,10} nonunique; {6,10} forces 10 PASS
K10 pair: m=1 free; m=2 needs prime 2; m=6 obstructed (needs 3); m=5 needs prime 5 PASS
K11 WALL: over Q every m in 1..12 carries PASS
K12 range: (6 beta_1)^2 = 36/5 > 1 exactly; (2 beta_1)^2 = 4/5 < 1 PASS

SUMMARY 13/13 PASS
```

## Breaker stdout (verbatim)

```text
C-READ-REDUNDANCY-1 breaker
independent code path; semantic evaluation, no reuse of the
verifier's coefficient argument

B1 (F1) m=2 symmetric integer accumulators, 390625 candidates no counterexample  zero satisfy the diagonal
B2 (F4) m=6 dyadic power-sum family, 1922375 candidates no counterexample  zero satisfy the diagonal
B2b (F4) m=6 dyadic elementary family, 1922375 candidates no counterexample  zero satisfy the diagonal
B3 (F2) W6 typed witness, 50 values x 8 port orders no counterexample  output = v every time
B4 repair 1 (strip powers of 2 from 6v): fails, residue 3v
B4 repair 2 (strip powers of 2 and 5 from 6v): fails, factor 3 survives
B5 (F3) 1/6 in Z[1/10]: independent scan vs prime-support rule no counterexample  both say NO

NO FALSIFIER FIRED
```
