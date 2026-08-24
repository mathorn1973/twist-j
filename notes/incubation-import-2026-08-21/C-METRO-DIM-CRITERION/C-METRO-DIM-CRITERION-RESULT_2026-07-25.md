# C-METRO-DIM-CRITERION-1 RESULT (rev1 and rev2)

CANDIDATE. NO AUTHORITY. Incubation lane, 2026-07-25. Target line: public
Public Canon v22.

STATUS: **candidate-F twice, with the scientific core standing.** Both fires were
gate-design errors, and each produced a new exact fact. One architecture only
(x86_64, Python 3.11.15); the aarch64 leg is owed.

## 0. Headline

The attack: close the named residual class **higher dimensional supports** of
`METRO-ADMISSIBILITY [O]` by lifting the public v21 theorem
`METRO-FINITE-STATE-RATIONALITY [T]` to dimension `d` and supplying the existence
criterion the public row explicitly lacks, plus the reduction calculus the
obligation demands.

```
What stands
  the criterion (A') (B) (C) (D), exact and decidable in integers and rationals
  R1 state relabeling      invariant   42092 cases, 0 violations
  R3 delta-stable lumping  invariant    4702 cases, 0 violations  (killed rev1)
  R5 dimension embedding   invariant    7927 cases, 0 violations
  R4 base change           FORBIDDEN, exact witness
  R6 factorwise            FORBIDDEN, exact witness
  gcd-guarded base change  invariant   12968 cases, 0 violations
  value by two routes agree            7429 cases, 0 disagreements
  clause (A) vs an independent polynomial peripheral test
                                      66605 automata, 0 disagreements
  BOX-A verdicts computed on         879874 automata across five (q,d) boxes

What fired
  rev1  F-MDC-INVAR     R3 changes the verdict in 182 cases
  rev2  F-MDC2-SUBSUME  (A') disagrees with (A) at one output vector, 8 cases

Neither fire is a defect in the mathematics. Both are defects in a gate I wrote.
```

## 1. The criterion (public derivation, dimension d)

```
q >= 2, d >= 1, A = {0,...,q-1}^d, Q = |A| = q^d.
A (q,d)-DFAO is (S, delta, w), S finite nonempty, delta: S x A -> S, w in Q^S,
accessible. B[s][t] = #{D in A : delta(s,D) = t}; every row of B sums to Q;
P = B/Q is nonnegative rational row-stochastic.
(P^m w)(s) = Q^(-m) sum over the Q^m words of length m of w(delta(s, word)).

||P^m||_inf = 1 for every m, so every peripheral eigenvalue of P is semisimple
(a nontrivial Jordan chain there would make the norm grow at least linearly).
This is the public row's boundedness step with Q in place of q. A non-terminal
irreducible class is strictly substochastic on at least one row, hence has
spectral radius below 1. So the peripheral spectrum of P is exactly the union,
over terminal classes R of period p_R, of the p_R-th roots of unity.

For a terminal class R of period p, the cyclic layers are the p classes of
"equal breadth-first level modulo p" inside R; pi_R^(j) is the stationary row
vector of mass 1 of P^p restricted to layer j, and a_R^(j) = pi_R^(j) . w|layer j.

(A') EXISTENCE, per output vector. P^m w converges entrywise iff for every
     terminal class R the p_R layer values a_R^(0),...,a_R^(p_R - 1) are equal.
     When every p_R = 1 the condition is vacuous, giving convergence for every w.
(B)  CONSTANCY. The limit is L . 1 iff the numbers L_R = pi_R . w|R agree across
     terminal classes, where pi_R is the stationary vector of P|R.
(C)  VALUE. Then L = L_R, rational, exactly computable over Q.
(D)  AGREEMENT. Then E w = L . 1 for the rational Q-primary Bezout projector E
     of the public row with q replaced by Q = q^d.
```

Clause (D) is the public row verbatim with `Q` for `q`, so the lift costs no new
mathematics. Clauses (A') to (C) are the part the public row explicitly does not
supply: it gives "no convergence existence criterion", and this is one.

## 2. Reduction calculus

```
ALLOWED and verified invariant
R1 state relabeling      bijection of S carried through delta and w
R3 delta-stable lumping  partition refining the level sets of w, stable under
                         delta; the quotient has the same verdict triple
R5 dimension embedding   d -> d+1 adjoining a coordinate delta ignores;
                         B -> qB, Q -> qQ, so P and every clause are fixed

FORBIDDEN, each with an exact witness
R4 base change by k      sends P to P^k; flips the verdict when a terminal
                         period divides k. Allowed only when gcd(k, p_R) = 1
                         for every terminal period.
R6 factorwise            per-coordinate decomposition; a periodic peripheral
                         mode of one coordinate is annihilated jointly by the
                         contraction of another.
```

Declaring R4 and R6 forbidden is the substance, not a convenience. If either were
allowed, the obligation's own negative branch would fire, because two
reduction-equivalent protocols would receive different classifications.

### 2.1 The R6 witness, reproduced exactly

`q = 2`, `d = 2`, `|S| = 2`, commuting coordinate actions: coordinate 1 swaps on
both digits, coordinate 2 is the identity on digit 0 and the swap on digit 1.

```
commuting on all digit pairs and all states     : True
coordinate-1 transfer operator = swap, square = identity
factorwise gap ||T1^(m+1) - T1^m||_max = 1 at every m, so no factorwise limit
coordinate-2 operator idempotent and absorbing: T2^2 = T2, T1 T2 = T2 T1 = T2
joint anchored value exactly 1/2 on every state, every m1 >= 0, m2 >= 1
```

Factorwise diverges; the joint decision converges to `1/2`. R6 is forbidden.

### 2.2 The R4 witness, reproduced exactly

`q = 2`, `d = 1`, `|S| = 2`, both digits swapping. `B = [[0,2],[2,0]]`, one
terminal class of period 2. With `w = (0,1)`, clause (A') says NOT convergent.
After base change `k = 2` the automaton has terminal classes `[0]`, `[1]`, both
of period 1, and (A') says convergent. `gcd(2, 2) = 2`, so the declared gcd
condition correctly forbids exactly this base change; with the guard in place,
12968 cases show no violation.

## 3. rev1 fired: F-MDC-INVAR on R3, and why

rev1 declared clause (A) universally in `w`: "converges for every `w` iff every
terminal period is 1". It declared R3 allowed. Both are correct statements. The
gate that compared them was not.

```
R3 violations: 182 of 4702
  convergence flag changed : 182
  constancy flag changed   : 0
  value L changed          : 0
smallest witness  q=2, d=1, |S|=2, delta=(1,1,0,0), w=(0,0), partition=(0,0)
  original  terminal class [0,1] of period 2; (A) says NOT convergent
  lumped    one state, period 1;             (A) says convergent, L = 0
```

Clause (A) is universal in `w`; R3's admissibility is `w`-relative, because the
partition must refine the level sets of `w`. When `w` is constant on a periodic
terminal class, lumping that class to a point destroys the period, so the
universal verdict flips although the `w`-specific averages converge in both
presentations, trivially, since `w` is constant there. Zero constancy or value
violations is the tell: the mathematics was never wrong, only the comparison.

rev1 predicted this failure in its own section 6 before computing. It is archived
as candidate-F at the R3 clause; its threshold was not moved.

## 4. rev2 repaired R3 and then fired on its own subsumption gate

rev2 replaced (A) by the per-`w` clause (A'). **The gate that killed rev1 now
passes clean: N2 R3-invariance, 4702 cases, 0 violations.** R1, R5, value by two
routes, both witnesses, and the gcd guard all pass. N7 found 37 automata with a
periodic terminal class whose convergence genuinely depends on `w`, which is the
phenomenon rev1 could not express at all.

`F-MDC2-SUBSUME` fired: 8 of 879874 automata where (A') at the all-distinct
output vector `w = (0,1,...,|S|-1)` disagrees with (A).

The gate asserted that a single output vector detects periodicity. It does not.
Smallest witness, verified three ways:

```
q = 2, d = 1, |S| = 3, delta = (1,1,0,2,1,1)
B = [[0,2,0],[1,0,1],[0,2,0]], row sums 2, terminal class {0,1,2} of period 2
cyclic layers {0,2} and {1}

w = (0,1,2):  layer averages 1 and 1  -> (A') convergent
              direct iteration: P^m w = (1,1,1) for every m >= 1, exactly
w = (0,0,1):  layer averages 1/2 and 0 -> (A') NOT convergent
              direct iteration oscillates forever between
              (0, 1/2, 0) and (1/2, 0, 1/2)
```

So (A) and (A') are both correct and they say different things: (A) is universal,
(A') is per vector. Asserting they agree at one chosen vector was the error.

**New exact fact worth registering.** The all-distinct output vector is NOT a
separating vector for the periodicity obstruction: there exist accessible
(q,d)-DFAOs with a period-2 terminal class whose all-distinct-`w` layer averages
coincide, so that vector converges immediately while another vector oscillates
forever. Eight witnesses in the enumerated boxes, the smallest at `|S| = 3`,
`q = 2`, `d = 1`. Any future criterion test must use a separating family, not one
"generic-looking" vector.

Correct subsumption, one direction only, and it did verify:

```
every terminal period 1  =>  (A') holds for every tested w
    966 automata, 0 violations
```

rev2 is archived as candidate-F at the N1 clause. rev2's threshold does not
authorize a repair for `F-MDC2-SUBSUME`, so **no rev3 was run in this session.**
Its specification is handed over in the bundle instead.

## 5. Pins

```
rev1 prereg    032369c416c750fea65e14e6b74f6a304a4af0c1d2b797c8e02d130ccb86e552
rev1 verifier  a497e6517984fac7551cbf8732ea8a65350bf23d2dee56d00f87ad9ffc454181
rev1 outcome   F-MDC-INVAR FIRED (R3, 182 cases). candidate-F, archived.

rev2 prereg    8fbb1aab5459048f6abfd7dc2839a2ba0abcdb6c387cb2ecb90cb04b79e301dc
rev2 verifier  93145674cae85dd6d6cab9a89a1a40688cf327978126095915c246d1116a0fd4
rev2 outcome   F-MDC2-SUBSUME FIRED (N1, 8 cases). candidate-F, archived.
               N2, N3, N4, N5, N6, N7 all clean.

platform       x86_64, Python 3.11.15, LC_ALL=C LANG=C TZ=UTC,
               PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0
runtime        rev1 21.8 s, rev2 24.9 s
```

## 6. Disclosures

1. **Timing recon before the rev1 freeze**: box sizes were printed and the
   criterion was timed on the full `(2,2,|S|=3)` box, 531441 automata in 5.2 s.
   No verdict, value, invariance, witness or cross-check result was computed
   before the freeze.
2. **rev2 declared coverage cap on N1**: the all-distinct-`w` comparison ran on
   all of BOX-A; the every-tested-`w` check ran only on the sub-box
   `(2,1,|S|<=3)` and `(2,2,|S|<=2)`, because it is vacuous by construction
   wherever all periods are 1. Printed in the run output, not silent.
3. **A convergence-only code path** (`conv2_only`) was added after the rev2
   freeze to bring N1 inside the runtime budget. It computes clause (A') and
   skips the (B)/(C) solves; it changes no reported value. Disclosed rather than
   passed over.
4. **My first R3 diagnostic script carried a stale `Q`** and reported "no
   separating output vector exists", which is false. Caught by hand computation
   and then by focused re-execution. The verifier was never affected. Recorded so
   the wrong statement does not propagate.

## 7. What this does and does not license

It does not close `METRO-ADMISSIBILITY`, and it does not narrow it yet either,
because both revisions are candidate-F. What it establishes is that the lift is
real, the reduction calculus is the hard part, and the two forbidden reductions
are forbidden for exact, witnessed reasons.

**The live count does not move.** It would not move even on a clean pass:
narrowing is not closing, and the residual would still contain non finite state
streams, unbounded memory adaptive protocols, stochastic protocols without an
exact finite reduction, irrational carriers with cross layer normalization, and
physical units.
