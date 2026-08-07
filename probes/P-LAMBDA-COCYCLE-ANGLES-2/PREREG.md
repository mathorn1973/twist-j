# P-LAMBDA-COCYCLE-ANGLES-2 preregistration

Date: 2026-08-06

Author of record: A. M. Thorn

Status: preregistered protocol only. No claim is earned by this file. No
formal gate may run before this file and the accepted verifier are committed
and pushed together as the immutable pin.

Public claim lock: issue 287.

## Authority record

```text
CANON:          Public Canon v38
TAG:            canon-v38
CONTENT_COMMIT: 64639e922c774990884963a708d7efb86b9dc1a7
CANON_SHA256:   f4bb9d7700f08c9609068e3e3eac4b60259c8f1ae3eab49eaa92832bc591c703
CANON_BYTES:    182096
```

The governing authority is `mathorn1973/twist-j` on `main`, at L6 measure and
spectral layer.

## Target row and scope

The target is the live frontier row `LAMBDA-COCYCLE-ANGLES [H]`, program
`ENRICHMENT`, queue `ROOT`, state `READY`, layer L6.

`P-LAMBDA-COCYCLE-ANGLES-1` (issue 284, pin
`d7ad9d9973a7859e030b42e572b7f64a1f926b2d`) proved the necessity direction:
the hypothesis forces the Cayley-angle grid condition, and its two registered
falsifier branches coincide. This probe registers the scope `CONVERSE`: the
sufficiency direction and the resulting characterization.

This probe branches from `main`, shares no directory with its sibling, does not
fire `LAMBDA-COCYCLE-ANGLES [H]`, and does not edit its registered text.

## Field one: equation

### Fixed notation

```text
zeta          zeta_5, primitive fifth root of unity
O, K          Z[zeta], Q(zeta), with ordered basis 1, zeta, zeta^2, zeta^3
phi           -zeta^2 - zeta^3, phi^2 = phi + 1
J             1 + zeta^2, the axiom object; J phi = zeta, N(J) = 1, Tr(J) = 3
lambda        1 - zeta, the prime of O above 5; N(lambda) = 5, e = 4, f = 1
O_lambda      the lambda-adic completion, a compact additive group
K_lambda      its fraction field
U_J           the Koopman operator f -> f(J .) on L^2(O_lambda,Haar)
chi_y         the character x -> psi(y x), for y in K_lambda/O_lambda
level(y)      the least k with lambda^k y = 0 in K_lambda/O_lambda
lambda_n      the standard Li coefficients, lambda_0 = 0
gamma         the ordinate of a critical-line zero rho = 1/2 + i gamma
alpha_gamma   2 arctan(1/(2 gamma)), the Cayley angle
grid          2 pi (1/4) Z[1/5], that is alpha/(2 pi) = m/(4 . 5^a)
n_A           4 . 5^A
D_n(theta)    |1 + z + ... + z^(n-1)|^2 at z = e^(i theta), D_0 = 0
```

### Cited external theorems

```text
PONT  Pontryagin duality for the compact group O_lambda: its dual is the
      discrete torsion group K_lambda/O_lambda, and {chi_y} is an orthonormal
      basis of L^2(O_lambda,Haar).

ROU   The roots of unity of Q(zeta_5) are exactly the ten elements
      {+/- zeta^j : 0 <= j < 5}.

SPEC  The spectral theorem for a unitary operator: a vector v has a unique
      positive spectral measure mu_v on the circle with
      <U^n v, v> = integral e^(i n theta) d mu_v, and mu_v(T) = ||v||^2.

BL    Bombieri and Lagarias: lambda_n = sum_rho [1 - (1 - 1/rho)^n], summed
      symmetrically; lambda_1 = sum_rho 1/rho.

LI    Li's criterion: RH holds iff lambda_n >= 0 for every n >= 1.
```

`P-LAMBDA-COCYCLE-ANGLES-1` R1 and R3 are also cited, at its pinned hashes.

### Frozen claims

```text
S1 [T intended]  J is a unit of O with N(J) = 1 and Tr(J) = 3; J phi = zeta;
                 J is none of the ten roots of unity of ROU, hence J has
                 infinite order.

S2 [T intended]  Multiplication by J is a Haar-preserving automorphism of
                 O_lambda.  By PONT, U_J permutes the orthonormal character
                 basis by chi_y -> chi_(J y).  Every y has finite level, and
                 multiplication by J preserves level, so every orbit is
                 finite: U_J is a permutation of an orthonormal basis with
                 finite cycles.

S3 [T intended]  The orbit of y of exact level k has size ord_(lambda^k)(J).
                 J = 2 mod lambda and ord_lambda(J) = 4.  Since lambda^4 and
                 (5) generate the same ideal,
                   ord_(lambda^(4m))(J) = 4 . 5^m,
                 and every orbit size is 4 times a power of 5.  Hence the
                 registered index sequence n_A = 4 . 5^A is exactly the orbit
                 size at level 4A.

S4 [T intended]  The valuation ladder is
                   v_lambda(J^4 - 1) = 1,
                   v_lambda(J^20 - 1) = 6,
                   v_lambda(J^(4 . 5^m) - 1) = 4m + 2 for m >= 1.
                 The first step jumps by 5 rather than by e = 4 because
                 s = 1 = e/(p-1) is the boundary case of the standard
                 p-adic lifting estimate.  The ladder is strictly increasing,
                 so no power J^(4 . 5^m) equals 1, consistent with S1.

S5 [T intended]  A finite-cycle permutation of an orthonormal basis has pure
                 point spectrum; a cycle of length d contributes exactly the
                 d-th roots of unity as eigenvalues.  With S3, the set of
                 eigenvalue angles of U_J is exactly the registered grid
                 2 pi (1/4) Z[1/5], and every grid angle is attained.

S6 [T intended]  Converse construction.  Assume RH and assume every Cayley
                 angle lies in the grid.  Let mu be the atomic measure with
                 mass (1/2)/(1/4 + gamma^2) at each of +/- alpha_gamma.  Its
                 total mass is lambda_1 < infinity.  By S5 each atom sits at
                 an eigenvalue angle; choosing one unit eigenvector per atom
                 and setting v = sum sqrt(mass) . eigenvector gives
                 v in L^2 with mu_v = mu.  Then
                   ||sum_(k<n) U_J^k v||^2 = integral D_n d mu,
                 which agrees with lambda_n at n = 0 and n = 1 and has the
                 same second differences by P-LAMBDA-COCYCLE-ANGLES-1 R3;
                 two initial values and all second differences determine a
                 sequence, so the two agree for every n.

S7 [T intended]  Characterization.  A cocycle vector exists if and only if RH
                 holds and every Cayley angle lies in 2 pi (1/4) Z[1/5].
                 Necessity is P-LAMBDA-COCYCLE-ANGLES-1 R2 and R3 together
                 with S5; sufficiency is S6.
```

### Written proof plan

These derivations must be completed in the result record.

#### S1

Direct ring arithmetic in the fixed basis gives `J phi = zeta`, `N(J) = 1` and
`Tr(J) = 3`. A unit of finite order in a number field is a root of unity; by
ROU the roots of unity of `K` are the ten listed elements, and `J` is not among
them, so `J` has infinite order. The verifier checks membership against the
explicit ten-element list rather than testing finitely many powers, so the
argument is complete rather than a bounded search.

#### S2

`J` is a unit, so multiplication by `J` is a continuous additive automorphism
of `O_lambda` with continuous inverse, and it carries Haar measure to Haar
measure by uniqueness of Haar measure up to scale together with
`|det| = |N(J)|_lambda = 1`. Hence `U_J` is unitary. By PONT the characters
`chi_y` form an orthonormal basis and `chi_y(J x) = chi_(J y)(x)`, so `U_J`
permutes that basis. Each `y` lies in `lambda^(-k) O_lambda / O_lambda` for
some finite `k`, a finite set preserved by the bijection `y -> J y`, so every
orbit is finite.

#### S3

For `y` of exact level `k`, `J^d y = y` holds iff `(J^d - 1) y = 0` iff
`J^d = 1` in `(O/lambda^k)`, so the orbit size is `ord_(lambda^k)(J)`. Since
`zeta = 1 mod lambda`, `J = 1 + zeta^2 = 2 mod lambda`, and `2` has order `4`
in `F_5^x`, so `ord_lambda(J) = 4`. The group `(O/lambda^k)^x` has order
`4 . 5^(k-1)`, so every element order is `4` times a power of `5` by Lagrange.
Because `e = 4`, the ideals `lambda^(4m)` and `(5^m)` coincide, so
`O/lambda^(4m)` is `Z[x]/(Phi_5(x), 5^m)` and the order is computed there
exactly. The verifier computes the order from the divisors of the known
multiple `4 . 5^(4m-1)` rather than assuming the answer.

#### S4

Write `J^4 = 1 + w` with `v_lambda(w) = 1`. Here `e/(p-1) = 4/4 = 1`, so `s = 1`
is exactly the boundary of the standard estimate `v(x^p - 1) = v(x - 1) + e`,
which is why the first fifth-power step is anomalous and adds `5`. From
`v_lambda(J^20 - 1) = 6 > 1` the estimate applies at every later step and adds
`e = 4`, giving `4m + 2` for `m >= 1`. Each value is checked exactly through
`v_lambda(x) = v_5(N(x))`, valid because `N(lambda) = 5`.

#### S5

Let `U` permute an orthonormal basis with all cycles finite. On the span of one
cycle of length `d`, `U` is the cyclic shift, whose eigenvalues are exactly the
`d`-th roots of unity, each once. The whole space is the orthogonal direct sum
of these finite-dimensional invariant pieces, so `U` has pure point spectrum
and its eigenvalue set is the union of the `d`-th roots of unity over the cycle
lengths `d`. By S3 those lengths are exactly `{4 . 5^a}`, and the union of the
corresponding root-of-unity angle sets is exactly `2 pi (1/4) Z[1/5]`. Every
grid angle therefore occurs, with at least one eigenvector.

#### S6

The measure `mu` is positive with total mass
`sum_(gamma>0) 1/(1/4 + gamma^2) = lambda_1`, finite. Its atoms are at grid
angles by assumption, hence at eigenvalue angles by S5. Distinct angles have
orthogonal eigenvectors; choosing one unit eigenvector `e_i` per distinct atom
angle `theta_i` of mass `m_i` and setting `v = sum sqrt(m_i) e_i` gives
`||v||^2 = sum m_i = lambda_1 < infinity`, so `v` lies in `L^2`, and by SPEC its
spectral measure is `mu`. If two ordinates share an angle their masses are added
before the choice, so the atoms remain distinct.

By SPEC, `||sum_(k<n) U_J^k v||^2 = integral D_n d mu =: f(n)`. Then
`f(0) = 0 = lambda_0` and `f(1) = mu(T) = lambda_1`, because `D_0 = 0` and
`D_1 = 1`. By P-LAMBDA-COCYCLE-ANGLES-1 R3 and R7 the second differences agree:
`f(n+1) + f(n-1) - 2 f(n) = t_n` for every `n >= 1`. A sequence is determined by
two consecutive values together with all its second differences, by induction on
`n`, so `f(n) = lambda_n` for every `n >= 0`. That is exactly the cocycle
condition.

#### S7

Necessity: a cocycle vector forces `lambda_n >= 0` and hence RH by LI
(P-LAMBDA-COCYCLE-ANGLES-1 R2); its spectral measure is the Cayley-angle
measure (that probe's R3), and by S5 the spectral measure of any vector is
supported on the grid, so every Cayley angle lies in the grid. Sufficiency is
S6. The two directions give the stated equivalence.

## Field two: code

The accepted verifier is `probes/P-LAMBDA-COCYCLE-ANGLES-2/verify.py`. It is
the exact-arithmetic audit of S1 through S7. It uses only the Python standard
library, integers, and `Fraction`. It runs from the repository root, finishes in
under one hundred twenty seconds, prints one fixed-order line per check followed
by one summary line, prints nothing to standard error, and exits nonzero if any
check fails.

Blocks and fixed order:

```text
C1  S1: ring arithmetic, N(J), Tr(J), J phi = zeta, and the ten-root-of-unity
    exclusion that proves infinite order
C2  S3: the residue map to F_5 as a ring homomorphism, J = 2 mod lambda, and
    ord_lambda(J) = 4
C3  S3: lambda^4 = (5) as ideals, the measured order ladder
    ord_(lambda^(4m))(J) = 4 . 5^m, the direct unit count, and the Lagrange
    divisibility
C4  S4: the valuation ladder, including the boundary jump at the first step
    and strict increase
C5  S5: the orbit-generated angle set compared with an independently built
    (1/4) Z[1/5] set, the off-grid exclusion, and the index action
C6  S6: the two-initial-values induction and the Fejer normalization
    D_0 = 0, D_1 = 1
C7  S6: atom-mass positivity, the paired-mass identity, and the norm equals
    total mass bookkeeping
C8  the registered conclusions S5, S6 and S7
```

Compilation and static inspection are permitted before the pin. No block,
partial block, exploratory call through the accepted verifier, or formal gate
may be executed before the pin is pushed and read back. The program was drafted
and statically checked outside the repository; the pinned file's first execution
is the formal gate.

## Field three: carrier or data

There is no external dataset, manifest, or generated numerical table. The
carrier is `Z[zeta_5]` in the fixed basis and its finite quotients
`Z[x]/(Phi_5(x), 5^m)`, together with declared exact rational instances. No
zeta ordinate is instantiated anywhere: the ordinate appears only as a free
rational parameter in the mass bookkeeping.

Frozen finite ranges and ordered lists:

```text
order levels m            1 .. 12, increasing
valuation levels m        0 .. 4, increasing
unit-count levels m       1, 2
grid levels a             0 .. 5, increasing
off-grid denominators     3, 7, 8, 9, 11, 12, 16, 60, in this order;
                          each divides no 4 . 5^a, checked rather than assumed
induction length          24
declared induction        n^2/3, n, (-1)^n n/7, n(n-1)/2, in this order,
  sequences               each normalized to start at 0
circle points             (3/5,4/5), (5/13,12/13), (-7/25,24/25), (8/17,15/17)
ordinate ladder           g = k/2 for k = 1..12, a structural ladder
coefficient ladder        c_k = 1/k for k = 1..14
```

The order ladder, the valuation ladder, and the unit counts are recomputed from
the ring by the verifier; none is supplied as input.

## Field four: systematics

All assertions use exact integer or `Fraction` arithmetic. No float literal
appears in the accepted verifier and no floating-point value is formed. Ranges
and lists are traversed only through the explicit ordered declarations above.
The verifier must not rely on dictionary or set iteration order for output.
Output must not depend on locale, timezone, timestamps, filesystem paths,
hostnames, platform strings, architecture strings, memory addresses, seeds, or
random state. Every output label and line order is fixed in the accepted source.
There is no tolerance, heuristic branch, retry, cache, or widened range.

The verifier must independently reject:

```text
a wrong value of N(J), Tr(J), or J phi;
J coinciding with a root of unity;
a residue map that is not a ring homomorphism;
a wrong residue of J modulo lambda;
an order ord_(lambda^(4m))(J) different from 4 . 5^m;
an orbit size that is not 4 times a power of 5;
a wrong unit-group count;
a valuation ladder that differs at any declared level, or fails to increase;
an orbit-generated angle set that differs from the independently built grid;
an off-grid denominator that in fact divides some 4 . 5^a;
an induction that does not rebuild a declared sequence exactly;
a Fejer normalization other than D_0 = 0 and D_1 = 1;
a nonpositive atom mass or a norm that is not the total mass.
```

Frozen local command:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 probes/P-LAMBDA-COCYCLE-ANGLES-2/verify.py
```

## Field five: failure threshold

### Probe package failure

Any failed exact gate, hash, identity, stdout, stderr, or deterministic-order
check fails the probe package. There is no retry with a moved threshold, an
enlarged range, a different precision rule, or a replacement source after the
pin.

### Scientific decision

```text
EARNS S1..S7
  every declared check passes exactly, the written derivations are complete,
  and the two required architecture jobs reproduce the committed stdout byte
  for byte.

DOES NOT EARN
  any declared check fails; a derivation step is missing; or a claim is stated
  beyond the audited identity.

STOP
  a cited theorem is used outside its published statement, or a step assumes
  RH outside the declared class, or the sibling probe's cited results are used
  at hashes other than its pin.
```

`LAMBDA-COCYCLE-ANGLES [H]` is not fired by this probe and remains
byte-for-byte unchanged by it. This probe proves nothing about RH, decides
nothing about whether the declared class is nonempty, and excludes no ordinate
from the grid. It establishes only that the grid condition is sufficient as
well as necessary, so that the row is equivalent to an arithmetic statement
about the zeros of zeta.

Every fired falsifier and every null result is retained. No threshold moves
after the pin.

## Field six: action layer

The action layer is L6 measure and spectral. Every definition, proof, range,
verifier check, and possible conclusion remains at L6. The probe makes no L1
state, L2 manifold, L3 boundary, L4 support, L5 stream, decoder,
physical-observable, SI, or empirical claim. Any lift requires its own named
gate.

## Required disclosure

The `P-LAMBDA-COCYCLE-ANGLES-1` disclosure carries over: a prior non-canonical
reconnaissance session opened rounded Keiper-Li values before pin, and those
values, their file, and every exploratory output are excluded from evidence.
This probe opens no numerical dataset at all.

The orbit sizes and valuations named in S3 and S4 were derived from the group
structure and confirmed by exact integer computation in `Z[zeta_5]` while the
scope was being written. They are frozen in public issue 287 before this pin,
and the accepted verifier recomputes them from the ring rather than accepting
them as input, so the audit does not depend on the pre-pin computation.

## Pin and hash record

The pin consists of this file and the accepted `verify.py`, committed and pushed
together before any formal execution. The pin record must publish the full
commit hash and the SHA-256 of each file. The SHA-256 of this file is recorded
outside this file at pin time to avoid a self-referential hash.
