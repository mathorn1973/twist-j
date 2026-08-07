# P-LAMBDA-COCYCLE-ANGLES-1 preregistration

Date: 2026-08-06

Author of record: A. M. Thorn

Status: preregistered protocol only. No claim is earned by this file. No
formal gate may run before this file and the accepted verifier are committed
and pushed together as the immutable pin.

Public claim lock: issue 284.

## Authority record

The currency gate records these five fields, read back from public `main` at
claim time:

```text
CANON:          Public Canon v38
TAG:            canon-v38
CONTENT_COMMIT: 64639e922c774990884963a708d7efb86b9dc1a7
CANON_SHA256:   f4bb9d7700f08c9609068e3e3eac4b60259c8f1ae3eab49eaa92832bc591c703
CANON_BYTES:    182096
```

The governing authority is `mathorn1973/twist-j` on `main`, at L6 measure and
spectral layer.

## Target row and corrected scope

The target is the live frontier row

```text
LAMBDA-COCYCLE-ANGLES [H]
program: ENRICHMENT
queue:   ROOT
state:   READY
layer:   L6 measure / spectral
```

whose registered falsifier has two branches: one exact Cayley-angle exclusion,
or a proof that the Li second differences do not approach `2 lambda_1` along
`n = 4 . 5^A`.

A predecessor non-canonical design draft offered two scopes, `TAIL` and
`FINITE`, and preferred `TAIL`. Both are rejected here, and the reason is part
of the registered result rather than a procedural remark. This probe registers
the scope `REDUCTION`: it proves the exact relation between the two falsifier
branches instead of attempting either.

This probe does not fire `LAMBDA-COCYCLE-ANGLES [H]` and does not edit its
registered text.

## Frozen decision boundary

The hypothesis under analysis is the compact lambda-adic cocycle-vector
residue: there exists `v in L^2(O_lambda,Haar)` with

```text
|| sum_(k=0)^(n-1) U_J^k v ||^2 = lambda_n
```

for every integer `n >= 1`. Call this the declared class. Nothing below asserts
that the declared class is nonempty or empty.

## Field one: equation

### Fixed notation

```text
lambda_n     the standard Li coefficients, from
             log xi(1/(1-z)) = -log 2 + sum_(n>=1) (lambda_n / n) z^n;
             if an implementation starts from Keiper coefficients kappa_n the
             conversion is fixed as lambda_n = n kappa_n
lambda_0     0
t_n          lambda_(n+1) + lambda_(n-1) - 2 lambda_n
n_A          4 * 5^A
M            2 lambda_1
rho          a nontrivial zero of zeta; on the critical line rho = 1/2 + i g
g            the ordinate of a critical-line zero, carried as a FREE variable
w            the Cayley factor 1 - 1/rho
alpha_g      2 arctan(1/(2 g)), the Cayley angle of the ordinate g
A, B, D      4 g^2 - 1, 4 g, 4 g^2 + 1
U, V         1, 2 g, the tangent half-angle pair with U/V = 1/(2 g)
D_n(theta)   |1 + z + ... + z^(n-1)|^2 at z = e^(i theta), with D_0 = 0
grid         2 pi (1/4) Z[1/5], that is alpha/(2 pi) = m/(4 * 5^a)
```

The ordinate `g` is never instantiated from a numerical zeta table. It is a
free variable of the polynomial ring, so every identity below is a statement
about all ordinates simultaneously.

### Cited external theorems

Two published results are used and are not reproved here.

```text
BL   Bombieri and Lagarias: lambda_n = sum_rho [1 - (1 - 1/rho)^n], summed
     symmetrically over the nontrivial zeros; in particular
     lambda_1 = sum_rho 1/rho.

LI   Li's criterion: RH holds if and only if lambda_n >= 0 for every n >= 1.
```

Both are unconditional. No step below assumes RH as a hypothesis; RH enters
only as a consequence of membership in the declared class, through LI.

### Frozen claims

The intended grade on each item is a ceiling.

```text
R1 [T intended]  On the critical line the Cayley factor is exactly a unit and
                 exactly the half-angle unit:
                   1 - 1/rho = (A + i B)/D,   A^2 + B^2 = D^2,
                   (A, B, D) = (V^2 - U^2, 2 U V, V^2 + U^2),
                 so w = e^(i alpha_g) with alpha_g = 2 arctan(1/(2 g));
                 and 1/rho^2 = -w/(1/4 + g^2), and
                 1/rho + 1/conj(rho) = 1/(1/4 + g^2).

R2 [T intended]  Membership in the declared class forces lambda_n >= 0 for
                 every n >= 1, because lambda_n is a squared norm. By LI, the
                 declared class is empty unless RH holds. RH is therefore a
                 consequence inside the class and not an added assumption.

R3 [T intended]  For every n >= 1 the second difference obeys the single
                 algebraic identity
                   X^(n+1) + X^(n-1) - 2 X^n = X^(n-1) (X - 1)^2,
                 and applying it to BL with X = w and (w - 1)^2 = 1/rho^2 and
                 R1 gives, inside the declared class,
                   t_n = sum_(gamma>0) 2 cos(n alpha_gamma)/(1/4 + gamma^2),
                   M   = sum_(gamma>0) 2/(1/4 + gamma^2) = 2 lambda_1,
                 hence
                   M - t_n = sum_(gamma>0) |w_gamma^n - 1|^2/(1/4 + gamma^2)
                           = sum_(gamma>0) 4 sin^2(n alpha_gamma/2)
                                           /(1/4 + gamma^2).

R4 [T intended]  Every summand of R3 is nonnegative and bounded by
                 4/(1/4 + gamma^2), so 0 <= M - t_n <= 2 M holds for every n
                 whenever the declared class is nonempty. Consequently no
                 exact value, and no interval enclosure, of any finite set of
                 Li coefficients can contradict membership in the declared
                 class. The finite scope has no falsifying power at any range
                 or precision.

R5 [T intended]  alpha/(2 pi) lies in the grid exactly when n_A annihilates it
                 for all large A: for alpha/(2 pi) = m/(4 * 5^a) with m
                 coprime to 5, the product n_A alpha/(2 pi) is an integer
                 precisely when A >= a; and for alpha/(2 pi) = p/q in lowest
                 terms with q dividing no 4 * 5^A, the distance from
                 n_A alpha/(2 pi) to Z is at least 1/q for every A.

R6 [T intended]  t_(n_A) -> M holds if and only if n_A alpha_gamma -> 0 modulo
                 2 pi for every ordinate. If the tail branch fires with a
                 rational delta > 0 on an infinite set S, then choosing a
                 finite window with tail mass below delta/2 leaves head mass at
                 least delta/2 on K ordinates, so some ordinate in that window
                 has |w_gamma^(n) - 1|^2 >= delta/(8 K) for infinitely many
                 n in S, because 1/4 + gamma^2 >= 1/4. The angle branch
                 therefore fires at one located ordinate.

R7 [T intended]  The Li second difference and the Fejer second difference are
                 driven by the same identity of R3: for |z| = 1,
                   D_(n+1) + D_(n-1) - 2 D_n = 2 cos(n theta),
                 and D_1 = 1. The spectral and arithmetic sides therefore agree
                 termwise, which is what identifies the forced spectral measure
                 with the Cayley-angle measure.
```

The registered consequence of R4 and R6 is that the two falsifier branches of
`LAMBDA-COCYCLE-ANGLES [H]` are not independent attack surfaces. The
second-difference branch is fired only by firing the angle branch.

### Written proof plan

These derivations must be completed in the result record. The verifier audits
them exactly but does not replace a missing argument.

#### R1

Write `rho = (1 + 2 i g)/2`. Then `1/rho = 2(1 - 2 i g)/(1 + 4 g^2)` and

```text
w = 1 - 1/rho = ((4 g^2 - 1) + 4 i g)/(4 g^2 + 1) = (A + i B)/D.
```

Direct expansion gives `A^2 + B^2 = 16 g^4 + 8 g^2 + 1 = D^2`, so `|w| = 1`
for every real ordinate. With `U = 1` and `V = 2 g` the triple `(A, B, D)` is
literally `(V^2 - U^2, 2 U V, V^2 + U^2)`, which is the tangent half-angle
parametrization of `e^(i alpha)` at `tan(alpha/2) = U/V = 1/(2 g)`. Hence
`w = e^(i alpha_g)` with `alpha_g = 2 arctan(1/(2 g))`, taking the principal
branch of `arctan`, which is the branch that places `alpha_g` in
`(-pi, pi)` and agrees with the registered Cayley angle. Squaring `rho` and
inverting gives `1/rho^2 = (4(1 - 4 g^2) - 16 i g)/D^2`, which is exactly
`-w . 4/D = -w/(1/4 + g^2)`. Finally `1/rho + 1/conj(rho) = 2 Re(1/rho)
= 4/D = 1/(1/4 + g^2)`.

#### R2

For `v` in the declared class, `lambda_n` is the squared norm of a vector, so
`lambda_n >= 0` for every `n >= 1`. LI converts this into RH. No further
appeal to RH is made anywhere in this probe: every later step is applied only
inside the declared class, where RH already holds, so the result is not a
conditional theorem.

#### R3

The identity `X^(n+1) + X^(n-1) - 2 X^n = X^(n-1)(X - 1)^2` holds in any
commutative ring, by factoring `X^(n-1)` and expanding `X^2 - 2 X + 1`. Apply
BL termwise with `X = w_rho`. Since `w - 1 = -1/rho`, the factor `(w - 1)^2`
is `1/rho^2`, so the `rho` term of `t_n` is `-w^(n-1)/rho^2`. By R1 this
equals `w^n/(1/4 + g^2)`. Pairing `rho` with `conj(rho)`, whose Cayley factor
is `conj(w)` because `A` is even and `B` is odd in `g`, gives the real form
`2 cos(n alpha_gamma)/(1/4 + gamma^2)`. The `n = 1` case of BL together with
the last identity of R1 gives `M = 2 lambda_1 = sum 2/(1/4 + gamma^2)`.
Subtracting termwise and using `|z - 1|^2 = 2 - 2 Re z` for `|z| = 1` gives
the stated nonnegative form, and `2 - 2 cos x = 4 sin^2(x/2)` gives the sine
form.

#### R4

Each summand is `|w^n - 1|^2/(1/4 + gamma^2)` with `|w^n| = 1`, so it lies
between `0` and `4/(1/4 + gamma^2)`. Summing and using
`sum 2/(1/4 + gamma^2) = M` gives `0 <= M - t_n <= 2 M`. Since these bounds
are implied by membership alone and constrain no individual index, any finite
family of exact Li values or enclosures that is consistent with RH is
consistent with the declared class. A finite profile therefore cannot fire the
row.

#### R5

For `alpha/(2 pi) = m/(4 * 5^a)` with `m` coprime to `5` we have
`n_A alpha/(2 pi) = m 5^(A-a)`, an integer exactly when `A >= a`. The
coprimality is required: a numerator carrying a factor `5` reduces the level
and is annihilated earlier, which is a smaller `a` for the same angle rather
than a counterexample. The verifier enforces the coprimality of every declared
numerator instead of assuming it. For
`alpha/(2 pi) = p/q` in lowest terms, the reduced denominator of
`n_A p/q` is `q/gcd(q, 4 * 5^A)`, which exceeds one exactly when `q` does not
divide `4 * 5^A`. A nonzero fraction with denominator dividing `q` is at
distance at least `1/q` from `Z`.

#### R6

The forward direction is R3 plus termwise nonnegativity: if every angle is
annihilated in the limit then every summand tends to zero and dominated
convergence against the convergent majorant `sum 4/(1/4 + gamma^2) = 2 M`
gives `t_(n_A) -> M`. For the converse, suppose `M - t_(n_A) >= delta` for
every `A` in an infinite set `S`. Choose a finite window with tail mass below
`delta/2`; the head, carried by `K` ordinates, then holds at least `delta/2`,
so some head ordinate has
`|w^(n_A) - 1|^2/(1/4 + gamma^2) >= delta/(2 K)`, and since
`1/4 + gamma^2 >= 1/4` this gives `|w^(n_A) - 1|^2 >= delta/(8 K)`. The window
is finite and `S` is infinite, so one fixed ordinate serves infinitely many
`A`. By the elementary Jordan inequality `|e^(i x) - 1| = 2 |sin(x/2)|
>= 2 |x|/pi` for `|x| <= pi`, that lower bound is equivalent to a positive
lower bound on the distance from `n_A alpha_gamma/(2 pi)` to `Z`, which is an
exact angle exclusion at that ordinate.

#### R7

For `|z| = 1` write `D_n = |z^n - 1|^2/|z - 1|^2`, which is the closed form of
the geometric sum. The numerator obeys the R3 identity, and on the unit circle
`(z - 1)^2/|z - 1|^2 = -z`, so the second difference collapses to
`2 Re(z^n)`. At `n = 1` the quotient is `1`. Hence a positive measure `mu`
with `lambda_n = integral D_n d mu` has `t_n = 2 integral cos(n theta) d mu`
and `M = 2 mu(T)`, matching R3 termwise and identifying `mu` with the
Cayley-angle measure.

## Field two: code

The accepted verifier is
`probes/P-LAMBDA-COCYCLE-ANGLES-1/verify.py`. It is the exact-arithmetic audit
of R1 through R7. It uses only the Python standard library, integers, and
`Fraction`. It runs from the repository root, finishes in under one hundred
twenty seconds, prints one fixed-order line for every check followed by one
summary line, prints nothing to standard error, and exits nonzero if any check
fails.

Its load-bearing objects are integer polynomials in the free ordinate variable
`g` and complex rational functions over them, compared by cross multiplication.
A passing identity check is therefore a statement about every ordinate at once.
No floating-point value is formed anywhere, and no external dataset is read.

The verifier blocks and their fixed order are:

```text
B1  R1: the Cayley factor is a unit, is the half-angle triple, is conjugated
    by the conjugate ordinate, and carries the paired mass identity
B2  R1: the reciprocal-square collapse and its powered form
B3  R3: the second-difference identity for a free base and for the Cayley
    factor
B4  R3: unit powers, the paired real contribution to t_n, the contribution to
    M, the residual identity, and its sine form
B5  R4: the exact sign and bound of the residual on the declared ordinate
    ladder
B6  R7: the free unit-circle point, D_1 = 1, the Fejer second difference, and
    its shared mechanism with B3
B7  R5 and R6: annihilation of grid angles by n_A, the rational separation of
    off-grid angles, the pigeonhole, the head and tail split, and the descent
    to the |w^n - 1|^2 bound
B8  the registered conclusions of R4, R6, and the grid characterization
```

Compilation and static inspection are permitted before the pin. No block,
partial block, exploratory call through the accepted verifier, or formal gate
may be executed before the pin is pushed and read back. The program was drafted
and statically checked outside the repository; the pinned file's first
execution is the formal gate.

## Field three: carrier or data

There is no external dataset, no manifest, and no generated numerical table.
The carrier is the polynomial ring `Z[g]` in one free ordinate variable,
together with the exact rational instances declared below. The proof is
self-contained apart from the two cited theorems BL and LI, whose used
statements are reproduced above at the necessary scope.

The frozen finite ranges and ordered lists are:

```text
N_MAX                     20; every powered identity runs 1 <= n <= N_MAX
Fejer range               1 <= n <= 12
ordinate ladder           g = k/2 for k = 1..12, in increasing order;
                          a structural ladder, not a zeta table
grid numerators           1, 2, 3, 7, 11, 13, 24, 101, in this order;
                          each coprime to 5, checked by the verifier rather
                          than assumed
grid levels a             0, 1, 2, 3, in this order
grid indices A            0, 1, 2, 3, 4, 5, in this order
off-grid denominators     3, 7, 8, 9, 11, 16, 12, 60, in this order;
                          each divides no 4 * 5^A, checked by the verifier
                          rather than assumed
off-grid index range      0 <= A <= 11
deltas                    1/10, 1/100, 1/1000, in this order
fanouts K                 1, 2, 5, 10, 50, in this order
```

The ordinate ladder carries no scientific weight: it exists only to exhibit the
polynomial identities as concrete rationals and to bound the residual. Every
claim of record rests on the polynomial identities, which are free of `g`.

## Field four: systematics

All assertions use exact integer or `Fraction` arithmetic. No assertion uses
floating point, and no float literal appears in the accepted verifier. Ranges
and lists are traversed only through the explicit ordered declarations above.
The verifier must not rely on dictionary or set iteration order. Output must
not depend on locale, timezone, timestamps, filesystem paths, hostnames,
platform strings, architecture strings, memory addresses, seeds, or random
state. Every output label and line order is fixed in the accepted source. There
is no tolerance, heuristic branch, retry, cache, or widened range.

The verifier must independently reject:

```text
a Cayley factor that is not a unit;
a half-angle triple that does not reproduce the Cayley factor;
a reciprocal-square collapse with the wrong sign or mass;
a second-difference identity that fails at any declared n;
a residual that is negative, unbounded, or not the squared modulus;
a Fejer second difference that is not twice the cosine;
a grid angle that is not annihilated at the declared threshold;
an off-grid denominator that in fact divides some 4 * 5^A;
a separation weaker than 1/q for an off-grid angle;
a pigeonhole, split, or descent bound that does not hold exactly.
```

The formal local command is frozen as:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 probes/P-LAMBDA-COCYCLE-ANGLES-1/verify.py
```

## Field five: failure threshold

### Probe package failure

Any failed exact gate, hash, normalization, identity, stdout, stderr, or
deterministic-order check fails the probe package. There is no retry with a
moved threshold, an enlarged range, a different precision rule, or a
replacement source after the pin.

### Scientific decision

```text
EARNS R1..R7
  every declared check passes exactly, the written derivations are complete,
  and the two required architecture jobs reproduce the committed stdout byte
  for byte.

DOES NOT EARN
  any declared check fails; or a derivation step is missing; or a claim is
  stated beyond the audited identity.

STOP
  a cited theorem is used outside its published statement, or a step silently
  assumes RH outside the declared class.
```

`LAMBDA-COCYCLE-ANGLES [H]` is not fired by this probe and remains
byte-for-byte unchanged by it. This probe earns no `T` for the emptiness or
nonemptiness of the declared class, proves nothing about RH, and excludes no
ordinate from the grid. It establishes only the relation between the two
registered falsifier branches, and the consequent absence of falsifying power
in any finite Li profile.

Every fired falsifier and every null result is retained. No threshold moves
after the pin.

## Field six: action layer

The action layer is L6 measure and spectral. The probe concerns the spectral
measure forced by a compact lambda-adic Koopman cocycle and the Li
second-difference sequence derived from it. It makes no L1 state, L2 manifold,
L3 boundary, L4 support, L5 stream, decoder, physical-observable, SI, or
empirical claim. Every lift requires a separate named gate.

## Required disclosure

A prior non-canonical reconnaissance session opened rounded Keiper-Li values
before pin. Those values, their file, and every exploratory output are excluded
from evidence. The formal scope, threshold, index rule, accepted verifier, and
source-generation protocol were frozen independently in public issue 284 before
any formal data access. The present scope opens no numerical dataset at all:
every load-bearing step is an identity in the ordinate as a free variable.

## Pin and hash record

The pin consists of this file and the accepted `verify.py`, committed and
pushed together before any formal execution. The pin record must publish the
full commit hash and the SHA-256 of each file. The SHA-256 of this file is
recorded outside this file at pin time to avoid a self-referential hash.
