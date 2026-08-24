# P-FINITE-PRIME-SUPPORT-DILATIONS-1 preregistration

Status: `PREREGISTERED / RESULT-EXPOSED / PROOF-FIRST`

One unconditional Hilbert-space theorem and the route kill it forces. The
universal result is carried by the written proof below. The verifier is a
finite exact audit with an independent piecewise-integration path for the
public Gram formula, exact residual checks, exact finite projections, and
scope-negative controls. It is not a discovery engine. The complete result is
exposed before execution: the theorem holds and the frozen route is dead.

## Public identity, authority, predecessor, and action layer

```text
probe:           P-FINITE-PRIME-SUPPORT-DILATIONS-1
public claim:    issue #463
probe owner:     A. M. Thorn / delegated session
                 finite-prime-support-dilations-2026-08-20
branch:          probe/P-FINITE-PRIME-SUPPORT-DILATIONS-1
basis:           Public Canon v56 ACTIVE
claim main:      4ed6cb72ab1110b68ed0574115e9dacbaf65e954
tag:             canon-v56 at 6e521f077b57ea343e5b456adb666b50e6a17eb4
content commit:  b36c93ed8ce24a9cbd771168094db04f5a5ac06c
Canon SHA-256:   b284ed6e78341aa6e3a74652d6f1f8f4079c270461f28bf32f2d95a6bd8b6645
Canon bytes:     288492
action layer:    L2 function-space geometry only
predecessor:     issue #445, P-PENTAGON-ONLY-DILATIONS-1;
                 J-LI-PENTAGON-DILATION-DEFICIENCY [T] and
                 PENTAGON-ONLY-DILATIONS [F]
formal status:   no formal execution before the remote pin of this file and
                 verify.py
```

The tag and content commit are ancestors of the claim-time main. The five
normative v56 hashes are unchanged. The collision search found no issue,
branch, probe path, Registry row, or candidate with this probe id or with
`FINITE-PRIME-SUPPORT-DILATIONS`.

## Falsifier first

The theorem fires negative if any exact instance in the frozen class exhibits
one of the following:

```text
F1  a finite prime set P, a prime q outside P, and s in S_P with gcd(q,s)>1;
F2  <g_q-(1/q)g_1,g_s> != 0 for an admitted s;
F3  ||g_q-(1/q)g_1||^2 != (1/12)(1-1/q^2);
F4  an admitted closed-span vector closer to g_q than (1/q)g_1;
F5  a finitely generated multiplicative semigroup containing a prime divisor
    outside the union of the prime supports of its generators.
```

For the F row, any F1 through F5 witness returns the finite-prime-support route
to life. A pin mismatch, stdout mismatch, architecture mismatch, changed
execution order, or changed accepted verifier without an exact mathematical
negation is integrity STOP, not a scientific falsifier. Infinite prime support
is outside scope and is not a repair of this frozen result.

## Frozen objects

Let

```text
H = L^2(0,1),
g_n(x) = frac(n x) - 1/2,      n >= 1.
```

The predecessor public theorem supplies

```text
<g_m,g_n> = gcd(m,n)^2/(12mn).
```

For a finite set `P` of rational primes define the full smooth-index family

```text
S_P = {s >= 1 : every prime divisor of s belongs to P}.
```

The empty product gives `1 in S_P`. An admitted family is any
`S subset S_P` with `1 in S`. Its carrier is the closed Hilbert subspace

```text
V_S = closure(span{g_s : s in S}).
```

A finitely generated multiplicative dilation semigroup means

```text
S(A) = {a_1^e_1 ... a_k^e_k : e_i >= 0},
```

for a finite tuple of positive integer generators `A=(a_1,...,a_k)`. It
contains `1`, and all prime divisors of all its elements lie in the finite
union of the prime supports of the generators.

## The six fields

```text
EQUATION     for every finite prime set P, every prime q not in P, and every
             S subset S_P containing 1:

             dist(g_q,V_S)^2 = (1/12)(1-1/q^2),

             with unique best approximant (1/q)g_1. Consequently every
             finitely generated multiplicative dilation semigroup misses at
             least one prime direction by an exact positive rational.

CODE         probes/P-FINITE-PRIME-SUPPORT-DILATIONS-1/verify.py;
             Python standard library only; Fraction arithmetic; no float;
             deterministic; run from repository root under
             LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
             TZ=UTC.

CARRIER      no external carrier and no data file. The only mathematical
             dependency is the public predecessor Gram theorem, which the
             verifier independently audits on frozen instances by exact
             piecewise polynomial integration.

SYSTEMATICS  exact breakpoint integration uses midpoint floor values and
             skips degenerate intervals; finite Gram projections use Gaussian
             elimination over Q; semigroup controls enumerate bounded exponent
             boxes only. The universal theorem is carried by the written
             proof, not by those finite audits.

THRESHOLD    any gate FAIL kills the formal run. No numerical tolerance exists.
             Every asserted equality is exact in Z or Q. Negative controls
             must be nonzero exactly.

LAYER        L2 only. RH remains O. No live row moves. No physical, decoder,
             Born, L5, L6, or cross-layer conclusion is admitted.
```

## Written proof

### 1. Public Gram input

For completeness, the predecessor proof is recalled but not claimed as new.
The Fourier expansion

```text
g_n(x) = -sum_(k>=1) sin(2 pi k n x)/(pi k)
```

and Parseval give

```text
<g_m,g_n> = gcd(m,n)^2/(12mn).
```

The accepted verifier does not assume this formula on its integration gate. It
reconstructs selected values by exact piecewise polynomial integration.

### 2. Finite-prime-support orthogonal residual

Fix a finite prime set `P`, a prime `q not in P`, and an admitted family
`S subset S_P` with `1 in S`. Every `s in S` is coprime to `q`. Define

```text
r_q = g_q - (1/q)g_1.
```

For every `s in S`, the exact Gram formula gives

```text
<r_q,g_s>
 = gcd(q,s)^2/(12qs) - (1/q) gcd(1,s)^2/(12s)
 = 1/(12qs) - 1/(12qs)
 = 0.
```

Thus `r_q` is orthonal to the algebraic span of the declared generators and,
by continuity, to its closure `V_S`.

### 3. Exact norm and projection

The residual norm is

```text
||r_q||^2
 = <g_q,g_q> - (2/q)<g_q,g_1> + (1/q^2)<g_1,g_1>
 = 1/12 - (2/q)(1/(12q)) + (1/q^2)(1/12)
 = (1/12)(1-1/q^2).
```

Since `q>=2`, this rational is strictly positive. Since `1 in S`, the vector
`(1/q)g_1` belongs to `V_S`. The decomposition

```text
g_q = (1/q)g_1 + r_q,      (1/q)g_1 in V_S,      r_q orthogonal V_S
```

is therefore the Hilbert projection decomposition. Orthogonal projection onto
a closed subspace is unique, so `(1/q)g_1` is the unique best approximant and
the displayed residual norm is the exact squared distance.

The result is independent of how large `S` is inside `S_P`. It applies to the
full infinite smooth family, to any finite or infinite subfamily containing
`1`, and to every multiplicative semigroup within it.

### 4. Finitely generated semigroup corollary

Let `A=(a_1,...,a_k)` be finitely many positive integer generators. Let `P_A`
be the union of their prime divisors. This set is finite. Every element of
`S(A)` has prime support contained in `P_A`. Euclid supplies a prime
`q not in P_A`; no quantitative prime bound is needed. Applying the theorem
with `P=P_A` and `S=S(A)` yields

```text
dist(g_q,V_(S(A))^2 = (1/12)(1-1/q^2) > 0.
```

Adding finitely many new generators only replaces `P_A` by another finite set,
so another prime direction remains unreachable.

### 5. Route consequence

The predecessor row already freezes the Nyman-Beurling / Baez-Duarte
criterion as motivation and kills the five-power-only route. The new theorem
shows that the obstruction is not pentagonal. Any dilation family whose
indices use only finitely many rational primes misses every outside prime
direction by the exact residual above. Therefore the realization route
restricted to finite prime support is falsified. The unrestricted criterion,
families with infinite prime support, and non-dilation carriers remain open.

## Accepted exact audit

The verifier freezes seven gates:

```text
FP1  exact piecewise integration reproduces selected Gram entries;
FP2  residual orthogonality and norm identities on a broad exact grid;
FP3  full finite-prime-support family controls for several P and outside q;
FP4  exact Gaussian projections on selected finite spans;
FP5  finitely generated semigroup support and residual controls;
FP6  negative controls fire when q lies inside the support;
FP7  the predecessor five-tower theorem is recovered as the P={5} slice.
```

The formal stdout is fixed by the pinned verifier. `EXPECTED.txt` will be the
byte-for-byte output of the one first formal execution after remote readback.

## Proposed fold edits, later and separately sealed

Registry row 1, proposed `[T]`, Canon section 16:

```text
J-LI-FINITE-PRIME-SUPPORT-DILATION-DEFICIENCY	T	in L^2(0,1), with g_n(x)=frac(nx)-1/2 and the public Gram gcd(m,n)^2/(12mn), for every finite rational-prime set P, every prime q outside P, and every S contained in the P-smooth positive integers with 1 in S, the residual g_q-(1/q)g_1 is orthogonal to the closed span of {g_s:s in S}, so the squared distance is exactly (1/12)(1-1/q^2)>0 and the unique best approximant is (1/q)g_1; every finitely generated multiplicative dilation semigroup is a corollary because its prime support is finite; L2 exact function-space mathematics only, with no RH, zero, physical, or layer-lift conclusion	16. p = 5 and the wall	probes/P-FINITE-PRIME-SUPPORT-DILATIONS-1	fires if an admitted q and s are not coprime, the residual is not orthogonal, its norm differs from (1/12)(1-1/q^2), a closer admitted approximant exists, or a finitely generated semigroup acquires a prime outside its generators' combined support; an integrity mismatch without exact mathematical negation is STOP
```

Registry row 2, proposed `[F]`, Canon section 16:

```text
FINITE-PRIME-SUPPORT-DILATIONS	F	the Nyman-Beurling / Baez-Duarte realization route restricted to dilation indices supported on finitely many rational primes is falsified: for every finite support P, any outside prime q remains at the exact positive squared distance (1/12)(1-1/q^2) from every declared family containing g_1; in particular no finitely generated multiplicative dilation semigroup is complete in this clock-function carrier; unrestricted infinite-prime-support dilation families and non-dilation carriers remain outside scope	16. p = 5 and the wall	probes/P-FINITE-PRIME-SUPPORT-DILATIONS-1	fired by J-LI-FINITE-PRIME-SUPPORT-DILATION-DEFICIENCY; the route returns only if that exact theorem is refuted, while changing to infinite prime support is outside the fired class
```

Frontier: no change. Proposed later ledger delta: claims `+2`, T `+1`, F `+1`.
The predecessor rows remain valid and are not removed. The new F strictly
contains the old pentagon-only route as one special case.

## Non-claims

No proof of RH and no evidence for RH. No assertion about zero locations. No
claim that a particular infinite-prime-support family is complete. No claim
that all TWIST-J carriers are dilation carriers. No physical interpretation.
No new J-native source. No use of numerical approximation. No Canon edit by
this probe.
