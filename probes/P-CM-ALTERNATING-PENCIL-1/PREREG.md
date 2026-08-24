# P-CM-ALTERNATING-PENCIL-1 preregistration

Date: 2026-08-06

Author of record: A. M. Thorn

Status: preregistered protocol only. No claim is earned by this file. No
formal gate may run before this file and the accepted verifier are committed
and pushed together as the immutable pin.

## Authority record

The currency gate records these five fields from `STATUS.md`:

```text
CANON:          Public Canon v37
TAG:            canon-v37
CONTENT_COMMIT: cbc0be8abf63d3f14fd9f8e912a1c8d59f03e626
CANON_SHA256:   f02f2c3129455852ed650fd644377263c492c058456873017b8a0fa9f3dc0148
CANON_BYTES:    177251
```

The governing authority is `mathorn1973/twist-j` on `main`, at L1 state.

## Corrected predecessor boundary

A predecessor note proposed that multiplication by `J` was a similitude of
one fixed alternating form with multiplier `phi^-2`. That statement is false.
For an integral multiplication matrix of determinant one, the identity

```text
Pf(M^T W M) = det(M) Pf(W)
```

would force a scalar multiplier to have square one, and direct comparison of
entries shows that the pullback by `J` is not a scalar multiple of the fixed
form. This probe preregisters the corrected object: the rank two lattice of
alternating trace forms, its unit action, and the repaired similitude boundary
in P8. The false predecessor statement is not restored or used as evidence.

## Field one: equation

### Fixed notation

```text
j            zeta_5, primitive fifth root of unity, j^5 = 1
K, O_K       Q(j), Z[j] with Z-basis 1, j, j^2, j^3
conj         complex conjugation, the Galois element sigma_4
K+, O_K+     Q(sqrt5), Z[phi], phi = -j^2 - j^3, phi^2 = phi + 1
             sigma_2(phi) = 1 - phi, N_{K+/Q}(phi) = -1,
             phi^-1 = phi - 1
Tr           the absolute trace from K to Q
J            1 + j^2, the axiom object; J phi = j, N(J) = 1,
             Tr(J) = 3
             M_J is multiplication by J in the basis above, det M_J = 1
lambda_1     j - j^-1 = j - j^4, coordinates (1, 2, 1, 1)
lambda_2     j^2 - j^-2 = j^2 - j^3, coordinates (0, 0, 1, -1)
L            the purely imaginary lattice, {z in O_K : conj(z) = -z}
Omega_lam    the form Omega_lam(x, y) = Tr(lam x conj(y)) / 5
             on O_K = Z^4
Omega_1      Omega at lam = lambda_1
Omega_2      Omega at lam = lambda_2
Omega_{a,b}  a Omega_1 + b Omega_2
Omega        in P8, a fixed nonzero pencil member; the finite audit uses
             Omega_1
phi action   in P7, multiplication of the form parameter by phi; a
             pullback by the unit phi acts instead through phi^2 as in P6
Pf           the Pfaffian of a 4 by 4 alternating matrix,
             Pf(A) = A[0][1] A[2][3] - A[0][2] A[1][3]
                     + A[0][3] A[1][2]
```

The fixed ordered basis throughout is `1, j, j^2, j^3`. No replacement
symbol is introduced for a basis element, a Weyl generator, or a matrix
coordinate.

### Frozen claims

The intended grade on each item is a ceiling. The claims are frozen in the
following order and wording, with no additional claim implied by the proof
plans or finite checks.

P1 [T intended]  L = lambda_1 . Z[phi], free of rank 1 over Z[phi], with
                 lambda_2 = lambda_1 phi^-1. Equivalently L has Z-basis
                 lambda_1, lambda_2.

P2 [T intended]  For every lam in L the form Omega_lam is alternating:
                 Omega_lam(x, x) = 0 and Omega_lam(y, x) = -Omega_lam(x, y),
                 for all x, y in O_K.

P3 [T intended]  Omega_lam is Z-valued for every lam in L, and Omega_lam is
                 unimodular exactly when lam generates the ideal (lambda_1).
                 In particular det(Omega_1) = 1.

P4 [T intended]  Pf(Omega_{a,b}) = a^2 - a b - b^2 for all integers a, b,
                 equal to N_{K+/Q}((a - b) + b phi). The Pfaffian is a
                 quadratic form in (a, b), so evaluation at (1,0), (0,1),
                 (1,1) determines it everywhere: the finite check IS the
                 proof, which is why this claim can carry T and not only C.

P5 [T intended]  The unimodular members of the pencil are exactly those with
                 a^2 - a b - b^2 = +1 or -1, the Pell layer, which is the
                 orbit of the units of Z[phi]. The Fibonacci pairs
                 (a, b) = (F_{n+1}, F_n) give Pf = (-1)^n.

P6 [T intended]  For u in O_K^x the pullback of Omega_lam by multiplication
                 by u is Omega at lam u conj(u): the unit group acts on the
                 pencil through the relative norm N_{K/K+}. The kernel of
                 that action is the norm one units, which are exactly the
                 ten roots of unity in K.

P7 [T intended]  In the basis lambda_1, lambda_2 the action of J on the
                 pencil is A_J = [[1, -1], [-1, 2]] with det 1, trace 3,
                 characteristic polynomial t^2 - 3 t + 1 and eigenvalues
                 phi^2 and phi^-2; the action of phi is [[1, 1], [1, 0]]
                 with det -1; A_J is the inverse of the action of phi^2.

P8 [T intended]  No multiplication by a unit is a similitude with a scalar
                 multiplier other than 1: M^T Omega M = mu Omega with M
                 integral of determinant 1 forces mu = +1 or mu = -1 by the
                 Pfaffian law, and the unit maps achieving mu = +1 are
                 exactly the ten roots of unity. Conjugation is not
                 multiplication by a unit and satisfies
                 C^T Omega C = -Omega.

### Written proof plan

These derivations must be completed in the result record. A finite verifier
audits them but does not replace a missing argument, except for the explicitly
finite three-value determination in P4.

#### P1

Write an element of `O_K` in the fixed basis with coordinates `(a,b,c,d)`.
Conjugation has coordinates

```text
conj(a,b,c,d) = (a-b, -b, d-b, c-b).
```

Equating this tuple to `(-a,-b,-c,-d)` gives `b = 2a` and
`c + d = 2a`. Put `r = c-a`; then every solution is

```text
(a,2a,a+r,a-r) = a lambda_1 + r lambda_2.
```

Conversely, every tuple on the right satisfies the two coordinate equations,
so this is an equality of lattices, not only a containment. Direct ring
reduction gives

```text
lambda_1 phi = lambda_1 + lambda_2.
```

Since `phi^-1 = phi-1`, this gives
`lambda_2 = lambda_1 phi^-1`. Finally,
`Z[phi] = Z + Z phi^-1`, so the coordinate description becomes
`L = lambda_1 Z[phi]`, free of rank one over `Z[phi]`.

#### P2

For `lam` in `L`, P1 and the coordinate equation give
`conj(lam) = -lam`. The absolute trace is invariant under conjugation. Apply
that invariance to

```text
w = lam y conj(x).
```

Commutativity and the imaginary condition give

```text
conj(w) = conj(lam) conj(y) x = -lam x conj(y).
```

Thus `Tr(lam y conj(x)) = -Tr(lam x conj(y))`, which proves
antisymmetry after division by five. Setting `y = x` makes the same rational
number equal to its negative, so it is zero and the form is alternating.

#### P3

The trace-dual criterion says that `Omega_lam` is integer-valued on
`O_K` exactly when `lam/5` belongs to the inverse different. For
`K = Q(j)`, the different and inverse different are

```text
D_K = (5 / (1-j)),        D_K^-1 = ((1-j) / 5).
```

The identities

```text
N(lambda_1) = 5 = N(1-j),
lambda_1 = j (1-j) (1+j+j^2)
```

show that `(lambda_1) = (1-j)`. By P1, every element of `L` is a
multiple of `lambda_1` by an element of `Z[phi]`, hence belongs to this
ideal and gives an integer-valued form.

The pairing is perfect over `Z` exactly when `lam/5` generates the inverse
different, equivalently when `(lam) = (lambda_1)`. Its Gram determinant is
then a unit in `Z`. Since an alternating four by four determinant is the
square of its Pfaffian, `det(Omega_1) = 1`. If `lam` is not a generator,
there are two cases. For `lam = 0`, the determinant is zero. For nonzero
`lam = lambda_1 eta` with nonunit `eta` in `Z[phi]`,

```text
det(Omega_lam) = N_{K/Q}(eta) = N_{K+/Q}(eta)^2,
```

so the absolute determinant is greater than one. The frozen finite witness
for that final check is `lam = 2 lambda_1`.

#### P4

Every entry of `Omega_{a,b}` is linear in `(a,b)`. The four by four
Pfaffian is quadratic in the matrix entries, hence there are integers
`q_20`, `q_11`, and `q_02` such that

```text
Pf(Omega_{a,b}) = q_20 a^2 + q_11 a b + q_02 b^2.
```

The three exact evaluations are frozen as

```text
Pf(Omega_{1,0}) = 1,
Pf(Omega_{0,1}) = -1,
Pf(Omega_{1,1}) = -1.
```

They give `q_20 = 1`, `q_02 = -1`, and `q_11 = -1`, proving the formula
for every integer pair. Under the two real embeddings of `K+`, direct
multiplication gives

```text
N_{K+/Q}((a-b)+b phi)
  = ((a-b)+b phi)((a-b)+b(1-phi))
  = a^2 - a b - b^2.
```

The verifier checks the three determining evaluations before checking the
larger frozen box.

#### P5

By P1, write

```text
lambda_{a,b} = a lambda_1 + b lambda_2
             = lambda_1 ((a-b)+b phi).
```

P3 says that its form is unimodular exactly when the coefficient in
`Z[phi]` is a unit. P4 identifies the norm of that coefficient with the
Pfaffian. The unit group is

```text
Z[phi]^x = <-1> x <phi>,       N(phi) = -1.
```

For completeness, let `epsilon` be a unit and choose its sign and an integer
`n` so that the principal real value of
`delta = +/- epsilon phi^-n` lies in `1 <= delta < phi`. If its norm is one,
its integer trace is `delta + delta^-1`, which lies in `[2,3)`, so the trace
is two and `delta = 1`. If its norm is minus one, its integer trace is
`delta - delta^-1`, which lies in `[0,1)`, so the trace is zero and
`delta = 1`, contradicting the norm. Thus every unit is `+/- phi^n`, which
proves the displayed unit-group description.

Therefore the parameter orbit
`{lambda_1 epsilon : epsilon in Z[phi]^x}` is exactly the locus on which the
displayed binary quadratic form is `+1` or `-1`. For `n >= 1`, induction from
`phi^2 = phi+1` gives

```text
phi^n = F_n phi + F_{n-1}.
```

The pair `(a,b) = (F_{n+1},F_n)` has coefficient
`F_{n-1}+F_n phi = phi^n`, and its Pfaffian is `N(phi)^n = (-1)^n`.

#### P6

For a unit `u`, commutativity gives the exact pullback identity

```text
Omega_lam(u x,u y)
  = Tr(lam u x conj(u y)) / 5
  = Tr(lam u conj(u) x conj(y)) / 5
  = Omega_{lam u conj(u)}(x,y).
```

The factor `u conj(u)` is the relative norm. It is a unit in `O_K+`, so P1
shows that multiplying `lam` by it stays in `L`. The kernel is therefore the
relative norm one subgroup.

The unit ranks of `K` and `K+` are both one. On real-subfield units the
relative norm sends `v` to `v^2`, so its image has rank one. The relative
norm kernel therefore has rank zero and is finite. Every finite-order field
unit is a root of unity, and the roots of unity in `Q(j)` are exactly

```text
{+j^k, -j^k : 0 <= k < 5}.
```

Every member of this ten-element group has relative norm one, so the kernel
is exactly this group.

#### P7

First reduce the relative norm of `J`:

```text
J conj(J) = 2-phi = (phi-1)^2 = phi^-2.
```

Using `lambda_2 = lambda_1 phi^-1` gives

```text
lambda_1 phi^-2 = lambda_1 - lambda_2,
lambda_2 phi^-2 = -lambda_1 + 2 lambda_2.
```

Reading these coordinate columns in the ordered basis
`lambda_1, lambda_2` yields

```text
A_J = [[1,-1],[-1,2]].
```

Its determinant is one, its trace is three, and direct expansion of
`det(t I_2-A_J)` gives `t^2-3t+1`. The two real embeddings send
`phi^-2` to `phi^-2` and `phi^2`, so these are its eigenvalues.

Multiplication of `L` by `phi` has columns determined by

```text
lambda_1 phi = lambda_1 + lambda_2,
lambda_2 phi = lambda_1,
```

and therefore has matrix `[[1,1],[1,0]]` with determinant `-1`. Squaring
this matrix gives multiplication by `phi^2`; direct matrix multiplication
shows that `A_J` is its inverse. Here the stated matrix for `phi` is
multiplication on the coefficient lattice. The pullback by the unit `phi`
uses its relative norm `phi^2`, consistently with P6.

#### P8

For every four by four alternating matrix `W` and every four by four matrix
`M`, use the standard identity

```text
Pf(M^T W M) = det(M) Pf(W).
```

Take the fixed nonzero form in P8 to be `Omega_1`. If `det(M) = 1` and
`M^T Omega_1 M = mu Omega_1`, then

```text
Pf(Omega_1) = Pf(mu Omega_1) = mu^2 Pf(Omega_1).
```

Thus `mu^2 = 1` over `Q`, so `mu` is `+1` or `-1`. A multiplication matrix
of a unit of `K` has determinant equal to its absolute norm, which is one.
The parameter map `lam -> Omega_lam` is injective: if its value is zero,
setting the second argument to one and using the nondegenerate trace pairing
forces `lam = 0`. By P6, a scalar pullback multiplier for a unit map therefore
equals `u conj(u)`.
Relative norms from this CM extension are positive in both real embeddings,
so `-1` cannot occur for a unit multiplication map. The multiplier is
therefore one, and P6 identifies its unit maps with the ten roots of unity.

For `J`, P7 gives the pullback coefficient
`lambda_1 phi^-2 = lambda_1-lambda_2`; comparison with `lambda_1` gives
the frozen entry obstruction to the withdrawn scalar multiplier. Finally,
direct substitution and trace invariance give

```text
Omega_lam(conj(x),conj(y)) = -Omega_lam(x,y),
```

which is the matrix identity `C^T Omega C = -Omega`. This last map is
distinct from multiplication by a unit.

## Field two: code

The accepted verifier is
`probes/P-CM-ALTERNATING-PENCIL-1/verify.py`. It is the exact-arithmetic
audit for P1 through P8. It must use only the Python standard library,
integers, and `Fraction`. It must run from the repository root, finish in
under one hundred twenty seconds, print one fixed-order line for every check
followed by one summary line, print nothing to stderr, and exit nonzero if any
check fails.

The verifier blocks and their fixed order are:

```text
B1  ring arithmetic self-test: j^5 = 1, the minimal polynomial,
    phi^2 = phi + 1, J phi = j, N(J) = 1, Tr(J) = 3,
    and det M_J = 1
B2  P1: coordinate-box solution of conj(z) = -z and
    lambda_2 = lambda_1 phi^-1
B3  P2: antisymmetry and alternation on all ordered basis pairs and the
    declared nonbasis vectors
B4  P3: integrality over the declared coefficient box,
    det(Omega_1) = 1, and the declared nongenerator determinant
B5  P4: the Pfaffian formula over the declared coefficient box and the
    printed three-value determination
B6  P5: equality of the unimodular and Pell lists in the declared box and
    the declared Fibonacci staircase
B7  P6: the pullback identity for the declared units, the ten fixed roots
    of unity, and the nonfixing declared units
B8  P7: both action matrices, determinants, trace, characteristic
    polynomial, eigenvalue polynomial identities, and inverse relation
B9  P8: the Pfaffian law on the declared integral matrices, the entry
    obstruction for J, and the conjugation identity
```

Compilation and static inspection are permitted before the pin. No block,
partial block, exploratory call through the verifier, or formal gate may be
executed before the pin.

## Field three: carrier or data

The carrier is `O_K = Z^4` in the ordered basis `1, j, j^2, j^3`. All data
are generated by exact ring arithmetic. There is no external dataset.

The frozen finite ranges and ordered test lists are:

```text
B2 coordinate box:
  -4 <= a,b,c,d <= 4, in lexicographic tuple order

B3 nonbasis vectors, in this order:
  (1,-1,2,0), (2,3,-1,4), (-3,0,1,2), (1,1,1,1)
  Check every ordered pair drawn from the four basis vectors followed by
  these four vectors.

B4 through B6 coefficient box:
  -20 <= a,b <= 20, in lexicographic pair order
  Declared nongenerator: 2 lambda_1.

B6 Fibonacci indices:
  1 <= n <= 20, in increasing order

B7 action-generator list, in this order:
  -1, j, j^-1, phi, phi^-1, J, J^-1

B7 fixed-form list, in this order:
  +j^0, -j^0, +j^1, -j^1, +j^2, -j^2, +j^3, -j^3,
  +j^4, -j^4, phi, phi^-1, J, J^-1

B9 integral matrix list, in this order:
  I_4, M_{-1}, M_j, M_{j^-1}, M_phi, M_{phi^-1}, M_J,
  M_{J^-1}, C, S_1, S_2, D_1, 2 I_4

  S_1 = [[1,1,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
  S_2 = [[1,0,0,0],[0,1,0,0],[0,0,1,1],[0,0,0,1]]
  D_1 = [[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
```

The verifier derives ring multiplication matrices and the conjugation matrix
from the fixed basis rather than accepting precomputed Gram or action
matrices as input.

## Field four: systematics

All assertions use exact integer arithmetic or `Fraction`. No assertion uses
floating point. Ring elements, vectors, matrices, units, and coefficient
pairs are traversed only through the explicit ordered ranges and lists above.
The verifier must not rely on dictionary or set iteration order. Output must
not depend on locale, timezone, timestamps, filesystem paths, hostnames,
platform strings, architecture strings, memory addresses, seeds, or random
state. Every output label and line order is fixed in the accepted source.
There is no tolerance, heuristic branch, retry, cache, or widened range.

The formal local command is frozen as:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 probes/P-CM-ALTERNATING-PENCIL-1/verify.py
```

## Field five: failure threshold

Any single failed check is a failure of the claim to which the check belongs.
The verifier must print `FAIL` for that check, print the fixed summary, and
exit nonzero. There is no tolerance and no retry with a widened range. A
fired falsifier or null result remains part of the record; no threshold or
test list may move after the preregistration pin.

The claim set is falsified if `verify.py` exhibits, within the declared
ranges, a lam in L with Omega_lam not Z-valued, or a pair (a, b) with
Pf(Omega_{a,b}) not equal to a^2 - a b - b^2, or a unit whose pullback leaves
the pencil, or a unimodular member off the Pell layer, or a unit outside the
ten roots of unity fixing Omega_1, or a scalar mu outside {1, -1} with
M^T Omega M = mu Omega for integral M of determinant 1.

## Field six: action layer

The action layer is L1 state. Every definition, proof, finite range, verifier
check, and possible conclusion in this probe remains at L1. A lift to any
other layer requires its own named gate and is outside this preregistration.

## Pin and hash record

The pin consists of this file and the accepted `verify.py`, committed and
pushed together before any formal execution. The pin record must publish the
full commit hash and the SHA-256 of each file. The SHA-256 of this file is
recorded outside this file at pin time to avoid a self-referential hash.
