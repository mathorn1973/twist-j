# P-LAMBDA-COCYCLE-ANGLES-1 result

Route: positive local formal leg with a passed architecture gate. The pinned
verifier exited zero, wrote empty standard error, and ended with
`RESULT 31/31 ALL PASS`. The required GitHub Linux x86_64 and aarch64 jobs
reproduced the exact stdout bytes from the same verifier hash, and their
aggregate `check` job succeeded. The grades below are the earned grades of
record.

Scope: the exact relation between the two registered falsifier branches of
`LAMBDA-COCYCLE-ANGLES [H]`, at L6 measure and spectral only. This result
changes no Canon, registry, frontier, or status file.

`LAMBDA-COCYCLE-ANGLES [H]` is **not fired** by this probe and its registered
text is unchanged. Nothing here proves or disproves RH, decides whether the
declared class is empty, or excludes any ordinate from the grid.

## Evidence state

```text
pin_commit: d7ad9d9973a7859e030b42e572b7f64a1f926b2d
prereg_sha256: 736b9bd8b6a189c9c9a4a80ac128c7f259c4f87a0d7539f3ae66adcdb761b783
verifier_sha256: 3263191dd30c07f9895f1b2c95f347d3d9a45ecb8dfcf136e1a34997891f62b1
stdout_sha256: 9e46f7f56d7e4b22683e3b595707f5bb880ef707771ac75aaa35a8dcc2584688
stdout_bytes: 2118
stdout_lines: 32
exit_code: 0
stderr_bytes: 0
local_result: 31/31 ALL PASS
local_leg: Ubuntu 24.04, x86_64, CPython 3.11.15
public_lock: issue 284
pull_request: 285
workflow_run: 31110661860
tested_head: a7f65508ac9afff9a67fa5881e3a313c7d833e0e
github_aarch64_job: 92647281077
github_x86_64_job: 92647281487
github_check_job: 92647355707
github_verifier_sha256: 3263191dd30c07f9895f1b2c95f347d3d9a45ecb8dfcf136e1a34997891f62b1
github_stdout_sha256: 9e46f7f56d7e4b22683e3b595707f5bb880ef707771ac75aaa35a8dcc2584688
github_byte_identity: PASS
architecture_gate: PASS
```

No registered falsifier of this probe fired.

## R1 [T]

Write `rho = (1 + 2 i g)/2` for a critical-line zero of ordinate `g`. Then
`1/rho = 2(1 - 2 i g)/(1 + 4 g^2)`, so

```text
w = 1 - 1/rho = ((4 g^2 - 1) + 4 i g)/(4 g^2 + 1) = (A + i B)/D.
```

Expanding, `A^2 + B^2 = 16 g^4 + 8 g^2 + 1 = (4 g^2 + 1)^2 = D^2`, so the
Cayley factor is a unit for every real ordinate. With `U = 1` and `V = 2 g`,

```text
(A, B, D) = (V^2 - U^2, 2 U V, V^2 + U^2),
```

which is exactly the tangent half-angle parametrization of `e^(i alpha)` at
`tan(alpha/2) = U/V = 1/(2 g)`. Hence

```text
1 - 1/rho = e^(i alpha_g),   alpha_g = 2 arctan(1/(2 g)),
```

on the principal branch, which is the registered Cayley angle. This is the
structural fact the whole probe rests on: the Cayley factor of a critical-line
zero is not merely of modulus one, it *is* the Cayley-angle unit.

Squaring and inverting `rho` gives
`1/rho^2 = (4(1 - 4 g^2) - 16 i g)/D^2`, which equals `-w . 4/D`, that is

```text
1/rho^2 = -w/(1/4 + g^2).
```

Finally `1/rho + 1/conj(rho) = 2 Re(1/rho) = 4/D = 1/(1/4 + g^2)`.

Verifier blocks B1-01 through B1-05 and B2-01 through B2-03 check every one of
these as an identity of rational functions in the free variable `g`, compared by
cross multiplication, so they hold for all ordinates at once and not on a
sample.

## R2 [T]

For `v` in the declared class, `lambda_n = ||sum_(k<n) U_J^k v||^2` is a squared
norm, so `lambda_n >= 0` for every `n >= 1`. By Li's criterion the declared
class is empty unless RH holds. RH is therefore a consequence of membership and
not an added assumption, and every later step is applied only inside the class.
The result is consequently not a conditional theorem.

## R3 [T]

In any commutative ring,

```text
X^(n+1) + X^(n-1) - 2 X^n = X^(n-1) (X - 1)^2.
```

Apply it termwise to the Bombieri-Lagarias representation with `X = w_rho`.
Since `w - 1 = -1/rho`, the factor `(w - 1)^2` is `1/rho^2`, so the `rho` term
of the second difference is `-w^(n-1)/rho^2`, which by R1 equals
`w^n/(1/4 + g^2)`. Because `A` is even and `B` is odd in `g`, the conjugate
ordinate carries the conjugate factor, so pairing `rho` with `conj(rho)` gives
a real contribution. The `n = 1` case of Bombieri-Lagarias with the last
identity of R1 gives the total mass. Therefore

```text
t_n = sum_(gamma>0) 2 cos(n alpha_gamma)/(1/4 + gamma^2),
M   = sum_(gamma>0) 2/(1/4 + gamma^2) = 2 lambda_1,
```

and subtracting termwise, with `|z - 1|^2 = 2 - 2 Re z` for `|z| = 1`,

```text
M - t_n = sum_(gamma>0) |w_gamma^n - 1|^2/(1/4 + gamma^2)
        = sum_(gamma>0) 4 sin^2(n alpha_gamma/2)/(1/4 + gamma^2).
```

Blocks B3-01, B3-02 and B4-01 through B4-05 audit these identities exactly.

## R4 [T]

Every summand of R3 lies between `0` and `4/(1/4 + gamma^2)` because
`|w^n| = 1`. Summing against `sum 2/(1/4 + gamma^2) = M` gives

```text
0 <= M - t_n <= 2 M    for every n >= 1.
```

These bounds follow from membership alone and constrain no individual index.
Any finite family of exact Li values or interval enclosures that is consistent
with RH is therefore consistent with membership in the declared class.

**A finite Li profile has no falsifying power against this row, at any range
and at any precision.** This retires the finite scope, not because it is
expensive or imprecise, but because it is provably empty of consequence. Blocks
B5-01, B5-02 and B8-02 record the sign, the bound, and this conclusion.

## R5 [T]

For `alpha/(2 pi) = m/(4 . 5^a)` with `m` coprime to `5`,

```text
n_A alpha/(2 pi) = m . 5^(A-a),
```

an integer exactly when `A >= a`. Coprimality is needed: a numerator carrying a
factor `5` is the same angle at a smaller level, not a counterexample, and the
verifier enforces coprimality of every declared numerator rather than assuming
it. For `alpha/(2 pi) = p/q` in lowest terms, the reduced denominator of
`n_A p/q` is `q/gcd(q, 4 . 5^A)`, which exceeds one exactly when `q` divides no
`4 . 5^A`; a nonzero fraction with denominator dividing `q` lies at distance at
least `1/q` from `Z`. Blocks B7-01 and B7-02 check both statements in exact
integer and `Fraction` arithmetic, including that each declared off-grid
denominator really divides no `4 . 5^A`.

So the registered grid `2 pi (1/4) Z[1/5]` is exactly the set of angles the
index sequence `n_A = 4 . 5^A` annihilates, which is why the grid appears in
the row at all.

## R6 [T]

If every Cayley angle is annihilated in the limit, each summand of R3 tends to
zero and the convergent majorant `sum 4/(1/4 + gamma^2) = 2 M` gives
`t_(n_A) -> M`.

Conversely suppose the tail branch fires: `M - t_(n_A) >= delta > 0` for every
`A` in an infinite set `S`. Choose a finite ordinate window whose tail mass is
below `delta/2`; the head, carried by `K` ordinates, then holds at least
`delta/2`, so some head ordinate satisfies

```text
|w^(n_A) - 1|^2/(1/4 + gamma^2) >= delta/(2 K),
```

and since `1/4 + gamma^2 >= 1/4`,

```text
|w^(n_A) - 1|^2 >= delta/(8 K).
```

The window is finite and `S` is infinite, so one fixed ordinate serves
infinitely many `A`. By the Jordan inequality
`|e^(i x) - 1| = 2 |sin(x/2)| >= 2 |x|/pi` for `|x| <= pi`, that bound is
equivalent to a positive lower bound on the distance from
`n_A alpha_gamma/(2 pi)` to `Z`, which is an exact angle exclusion at that
located ordinate. Blocks B7-03, B7-04, B7-05 and B8-04 audit the pigeonhole,
the head and tail split, and the descent.

**The two registered falsifier branches are therefore one branch.** The
second-difference falsifier of `LAMBDA-COCYCLE-ANGLES [H]` cannot be fired
without firing its angle falsifier at a specific ordinate.

## R7 [T]

For `|z| = 1`, the Fejer quantity `D_n = |1 + z + ... + z^(n-1)|^2` equals
`|z^n - 1|^2/|z - 1|^2`. Its numerator obeys the same identity as R3, and on
the unit circle `(z - 1)^2/|z - 1|^2 = -z`, so

```text
D_(n+1) + D_(n-1) - 2 D_n = 2 cos(n theta),   D_1 = 1.
```

A positive measure `mu` with `lambda_n = integral D_n d mu` therefore has
`t_n = 2 integral cos(n theta) d mu` and `M = 2 mu(T)`, matching R3 termwise
and identifying the forced spectral measure with the Cayley-angle measure
carried by the atoms `alpha_gamma` of mass `1/(1/4 + gamma^2)`.

The Li second difference and the Fejer second difference are the same algebraic
identity read on two sides. Blocks B6-01 through B6-04 check this on a free
rational point of the unit circle.

## Consequence for the frontier

Within the declared compact-boundary class, the surviving attack surface on
`LAMBDA-COCYCLE-ANGLES [H]` is exactly one: an exact arithmetic exclusion of a
single Cayley angle `2 arctan(1/(2 gamma))` from `2 pi (1/4) Z[1/5]`.
Equivalently, by R1, an exact proof that some nontrivial zero is **not** of the
form

```text
rho = 1/(1 - zeta),   zeta^(4 . 5^a) = 1,
```

that is, that some zero is not the explicit algebraic number
`1/2 + (i/2) cot(pi m/(4 . 5^a))` lying in `Q(zeta_(4 . 5^a))`. Since the grid
is dense in the circle, no numerical enclosure of an ordinate can decide this;
the exclusion needs an arithmetic or transcendence input.

This is a sharpening of the row and not a weakening: both registered falsifier
branches remain valid, and the row remains falsifiable. What is established is
that they coincide, so effort spent on second-difference computation is effort
spent on the angle problem in a strictly harder disguise.

No Canon, registry, frontier, evidence, or status file is edited by this probe.
A separate sealed fold would be required to record the sharpening in
`canon/`.
