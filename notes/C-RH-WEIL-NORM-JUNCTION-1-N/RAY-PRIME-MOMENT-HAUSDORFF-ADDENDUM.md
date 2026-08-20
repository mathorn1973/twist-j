# RAY-PRIME-MOMENT-HAUSDORFF addendum, 2026-08-20

```text
STATUS:      NON-CANONICAL INCUBATION ADDENDUM under issue #374
AUTHORITY:   none
TARGET LINE: PUBLIC context, notes-only analytic continuation
BASIS:       Public Canon v56 ACTIVE on current public main
TAG:         canon-v56
CONTENT:     b36c93ed8ce24a9cbd771168094db04f5a5ac06c
CANON SHA:   b284ed6e78341aa6e3a74652d6f1f8f4079c270461f28bf32f2d95a6bd8b6645
CANON BYTES: 288492
COMPUTATION: none
LABELS:      candidate grade only; no public status movement
```

This addendum continues the Ray-Stieltjes master formulation without using the
Li sequence as an input. Its only new purpose is to put the complete
Hausdorff condition onto one ordinary-convergence Euler ray, where every
needed derivative is an absolutely convergent von Mangoldt moment plus the
completed archimedean term.

Nothing here proves any one of the resulting inequalities from the Euler side.
That remains the source wall.

## 0. Falsifiers first

```text
FD1 kills B1 if A_(n+1)(c) differs from
    (-1)^n/n! (d/d(c^2))^n [M(c)/(2c)].

FD2 kills B2 if the finite-difference transform H_(n,r)(c) differs from
    the displayed squared-pole sum, including any sign, factorial, power of c,
    or unordered-pair multiplicity.

FD3 kills B3 if the stated formula for M^(k)(c) has a wrong sign in the
    von Mangoldt term, a wrong factor in the polygamma term, or fails absolute
    convergence for c>1/2.

FD4 kills the complete Euler-Hausdorff criterion if all displayed prime-side
    inequalities can hold while one nontrivial zero is off the critical line,
    or RH can hold while one inequality is negative.

FD5 kills the claim that c=1 is B6-clean if any asserted prime series at
    sigma=3/2 requires analytic continuation, regularization, or zero data.
```

A finite list of positive inequalities is not a success condition. A failed
transport, changed note, or source-pin error is integrity STOP rather than a
mathematical falsifier.

## 1. Frozen objects

Retain the conventions of the Ray-Stieltjes addendum:

```text
X(z) = xi(1/2+z),
M(c) = X'(c)/X(c) = (xi'/xi)(1/2+c),
S(x) = M(sqrt(x))/(2sqrt(x))
     = sum_P m_alpha/(x-alpha^2),
```

where `P` is the multiset of unordered pairs `{alpha,-alpha}` and
`alpha=rho-1/2`.

For fixed `c>1/2`, define

```text
A_k(c) = sum_P m_alpha/(c^2-alpha^2)^k,       k>=1,
b_n(c) = c^(2n) A_(n+1)(c),                  n>=0.
```

The previous addendum gives

```text
RH iff {b_n(c)}_(n>=0) is a Hausdorff moment sequence
```

for any one fixed `c>1/2`.

## 2. B1, one-point differential generator

Let

```text
D_c := d/d(c^2) = (1/(2c)) d/dc.
```

Since `S(c^2)=A_1(c)=M(c)/(2c)`, termwise differentiation of the absolutely
convergent paired resolvent gives

```text
A_(n+1)(c)
 = (-1)^n/n! D_c^n [M(c)/(2c)].
```

Equivalently define recursively

```text
P_0(c)     = M(c)/(2c),
P_(n+1)(c) = -(1/(2(n+1)c)) dP_n(c)/dc.
```

Then

```text
P_n(c)=A_(n+1)(c),
b_n(c)=c^(2n)P_n(c).
```

This is a finite differential recursion. No zero table is needed to evaluate
its Euler-side form.

## 3. B2, complete finite-difference family

Use the forward difference

```text
Delta b_n = b_(n+1)-b_n
```

and define

```text
H_(n,r)(c)
 := (-1)^r Delta^r b_n(c)
  = sum_(j=0)^r (-1)^j binom(r,j) b_(n+j)(c).
```

Direct substitution of the paired resolvent yields the exact closed form

```text
H_(n,r)(c)
 = sum_P m_alpha c^(2n)(-alpha^2)^r
     /(c^2-alpha^2)^(n+r+1).
```

Under RH, `alpha=i gamma`, so every summand is

```text
m_gamma c^(2n) gamma^(2r)/(c^2+gamma^2)^(n+r+1) >= 0.
```

Conversely, the Hausdorff moment theorem and the pole argument in the previous
addendum give

```text
RH iff H_(n,r)(c) >= 0 for every n,r>=0
```

for any one fixed `c>1/2`.

This is an infinite criterion. No bounded rectangle in `(n,r)` is claimed to
be complete.

## 4. B3, ordinary-convergence Euler source

Put

```text
sigma = c+1/2 > 1.
```

The completed logarithmic derivative has the honest Euler-side expression

```text
M(c)
 = 1/sigma + 1/(sigma-1) - (1/2)log pi
   + (1/2)psi(sigma/2)
   - sum_(m>=2) Lambda(m)m^(-sigma).
```

For every integer `k>=0`, differentiation is termwise absolutely convergent
and gives

```text
M^(k)(c)
 = (-1)^k k![sigma^(-k-1)+(sigma-1)^(-k-1)]
   - delta_(k,0)(1/2)log pi
   + 2^(-k-1) psi^(k)(sigma/2)
   + (-1)^(k+1) sum_(m>=2) Lambda(m)(log m)^k m^(-sigma).
```

The sign in the last line follows from differentiating
`-m^(-sigma)` exactly `k` times. Every logarithmic moment converges absolutely
for `sigma>1`.

Combining this display with the finite recursion in B1 makes every
`H_(n,r)(c)` a finite exact combination of completed archimedean terms and
ordinary von Mangoldt logarithmic moments. No Li power series, zero list,
Perron regularization, or boundary continuation is used.

## 5. B4, the canonical clean point c=1

Choose

```text
c=1,     sigma=3/2.
```

Write

```text
M_j := M^(j)(1).
```

Then `b_n(1)=A_(n+1)(1)` and the first rungs are

```text
b_0 = M_0/2,
b_1 = (M_0-M_1)/4,
b_2 = (3M_0-3M_1+M_2)/16,
b_3 = (15M_0-15M_1+6M_2-M_3)/96.
```

The first Hausdorff cells are therefore

```text
H_(0,0) = M_0/2,
H_(1,0) = (M_0-M_1)/4,
H_(0,1) = (M_0+M_1)/4,
H_(2,0) = (3M_0-3M_1+M_2)/16,
H_(1,1) = (M_0-M_1-M_2)/16,
H_(0,2) = (3M_0+5M_1+M_2)/16.
```

Each `M_j` is supplied at `sigma=3/2` by the absolutely convergent formula in
B3. These low cells are diagnostics only. Their positivity, even if proved,
does not close RH.

## 6. B5, exact prime-moment criterion

The preceding identities give the candidate equivalence

```text
RH
iff for every n,r>=0 the finite differential expression H_(n,r)(1),
    generated from M(c) at c=1 by B1 and B2, is nonnegative
iff the corresponding completed archimedean plus absolutely convergent
    von Mangoldt logarithmic-moment expression at sigma=3/2 is nonnegative
    for every n,r>=0.
```

**Status: [candidate-T, NON-CANONICAL].**

This is not an RH proof. It is the first version of the Ray-Stieltjes line in
which the full criterion is written entirely on a single ordinary-convergence
Euler ray.

## 7. Relation to the lambda attempt

The Li endpoint is `c=1/2`, where `sigma=1` and the ordinary von Mangoldt
series is no longer absolutely convergent. At that endpoint the `A_k` tower is
a finite transform of the Li coefficients, but the Li generating series has
the radius caveat already recorded in this lock.

The present continuation deliberately uses `c=1` instead. It consumes no
lambda coefficient and no lambda-adic grid hypothesis. Lambda data may audit
or compare endpoint rungs, but it is not a premise of B1 through B5 and cannot
supply the missing all-cell Euler positivity by finite testing.

## 8. Next falsification target

The next mathematical attack is sharply scoped:

```text
EHP1  derive an integral or sum-of-squares representation for the complete
      family H_(n,r)(1) from the Euler side; or

EHP2  find the first exact pair (n,r) whose source expression cannot be
      nonnegative unconditionally, and identify the missing global coupling;
      or

EHP3  prove a source-side recursion or total-positivity theorem propagating a
      finite set of named boundary inequalities to all n,r.
```

A finite numerical scan is not EHP1, EHP2, or EHP3. Any successful statement
must control the complete infinite family or prove an exact obstruction at a
frozen scope.

## 9. Firewall

No RH evidence or status movement. No Canon, Registry, Frontier, evidence, or
gate edit. No J-native carrier, lambda-adic realization, physical reading,
Born rule, decoder, SI statement, or L1-L6 lift. The parent owner remains issue
#374. Promotion, if any, requires a later fresh public procedure on the then
current authority.
