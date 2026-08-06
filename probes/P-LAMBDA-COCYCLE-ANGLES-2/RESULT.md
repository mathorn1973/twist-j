# P-LAMBDA-COCYCLE-ANGLES-2 result

Route: positive local formal leg. The pinned verifier exited zero, wrote empty
standard error, and ended with `RESULT 33/33 ALL PASS`. The required GitHub
Linux x86_64 and aarch64 jobs are pending; until that gate passes the grades
below are intended and not earned.

Scope: the converse direction of the compact lambda-adic cocycle-vector
hypothesis and the resulting characterization, at L6 measure and spectral only.
This result changes no Canon, registry, frontier, or status file.

`LAMBDA-COCYCLE-ANGLES [H]` is **not fired** by this probe and its registered
text is unchanged. Nothing here proves or disproves RH, decides whether the
declared class is nonempty, or excludes any ordinate from the grid.

## Evidence state

```text
pin_commit: ac496a684d715cbfca69b199abfb19dcc8000c20
prereg_sha256: 1e566e8df11645395db00c8eec556a24547c9bf6303dc8594e37bca5de918196
verifier_sha256: 37347d200eba27b2aa94da3e79c3705aa1e8e4d8cc6136c6347d32cd7b6306a9
stdout_sha256: 7c5b661401dc245e9469e9cc7b6e9129f4a773b44226410ff557770d35727eeb
stdout_bytes: 2234
stdout_lines: 34
exit_code: 0
stderr_bytes: 0
local_result: 33/33 ALL PASS
public_lock: issue 287
sibling_pin: d7ad9d9973a7859e030b42e572b7f64a1f926b2d (P-LAMBDA-COCYCLE-ANGLES-1)
architecture_gate: pending
```

No registered falsifier of this probe fired.

## S1 [T intended]

Ring arithmetic in the fixed basis gives `J phi = zeta`, `N(J) = 1` and
`Tr(J) = 3`. A unit of finite order in a number field is a root of unity, and
the roots of unity of `Q(zeta_5)` are exactly the ten elements
`{+/- zeta^j : 0 <= j < 5}`. The verifier checks that `J` is not among that
explicit ten-element list, so the exclusion is complete rather than a bounded
search over powers. Hence `J` has infinite order. Blocks C1-01 through C1-07.

## S2 [T intended]

`J` is a unit, so multiplication by `J` is a continuous additive automorphism of
`O_lambda` with continuous inverse; since `|N(J)|_lambda = 1` it preserves Haar
measure, and `U_J` is unitary. By Pontryagin duality the characters `chi_y`,
indexed by `y in K_lambda/O_lambda`, form an orthonormal basis, and

```text
chi_y(J x) = chi_(J y)(x),
```

so `U_J` permutes that basis by `y -> J y`. Every `y` lies in
`lambda^(-k) O_lambda / O_lambda` for a finite `k`, a finite set preserved by
the bijection, so **every orbit is finite**. `U_J` is a permutation of an
orthonormal basis with finite cycles.

## S3 [T intended]

For `y` of exact level `k`, the orbit size is the least `d` with `J^d y = y`,
that is `ord_(lambda^k)(J)`. Since `zeta = 1 mod lambda`,

```text
J = 1 + zeta^2 = 2 mod lambda,
```

and `2` has order `4` in `F_5^x`, so `ord_lambda(J) = 4`. The group
`(O/lambda^k)^x` has order `4 . 5^(k-1)`, verified by direct count at the
declared levels, so by Lagrange every element order is `4` times a power of `5`.

Because the ramification index is `4`, the ideals `lambda^(4m)` and `(5^m)`
coincide, so `O/lambda^(4m)` is `Z[x]/(Phi_5(x), 5^m)` and the order is computed
there exactly. The verifier computes the order from the divisors of the known
multiple `4 . 5^(4m-1)` rather than assuming the answer, and finds

```text
ord_(lambda^(4m))(J) = 4 . 5^m    for 1 <= m <= 12.
```

**The registered index sequence `n_A = 4 . 5^A` is therefore exactly the orbit
size of `J` at level `4A`.** That is why that sequence appears in the row: it is
not a chosen test sequence but the period of the operator on each level.
Blocks C2-01 through C3-05.

## S4 [T intended]

The valuation ladder, computed exactly through `v_lambda(x) = v_5(N(x))`, is

```text
v_lambda(J^4 - 1)   = 1,
v_lambda(J^20 - 1)  = 6,
v_lambda(J^(4 . 5^m) - 1) = 4m + 2   for m >= 1.
```

The first fifth-power step adds `5`, not the ramification index `4`. That is the
boundary case of the standard lifting estimate: here `e/(p-1) = 4/4 = 1` and the
starting valuation is exactly `1`, so the estimate `v(x^p - 1) = v(x - 1) + e`
does not yet apply. From `v = 6 > 1` onward it does, and every later step adds
`4`. The ladder is strictly increasing and never reaches infinity, so no power
`J^(4 . 5^m)` equals `1`, consistent with S1. Blocks C4-01 through C4-04.

## S5 [T intended]

A permutation of an orthonormal basis with all cycles finite has pure point
spectrum: the space is the orthogonal direct sum of the finite-dimensional
cycle spans, and on a cycle of length `d` the operator is the cyclic shift,
whose eigenvalues are exactly the `d`-th roots of unity, each once. With S3 the
cycle lengths are exactly `{4 . 5^a : a >= 0}`, so the eigenvalue angle set is

```text
union over a of {2 pi j/(4 . 5^a)} = 2 pi (1/4) Z[1/5],
```

the registered grid, with every grid angle attained. The verifier builds the
orbit-generated angle set and, independently, the set of reduced fractions whose
denominator is `2^e . 5^f` with `e <= 2`, and checks the two sets are equal;
it also checks that each declared off-grid denominator divides no `4 . 5^a` and
never appears. Blocks C5-01 through C5-04.

**This identifies the grid.** The registered grid is not an assumption about
zeta; it is the point spectrum of `U_J`, forced by the multiplicative order of
`J` in the residue rings.

## S6 [T intended]

Assume RH and assume every Cayley angle lies in the grid. Let `mu` carry mass
`(1/2)/(1/4 + gamma^2)` at each of `+/- alpha_gamma`; its total mass is
`sum_(gamma>0) 1/(1/4 + gamma^2) = lambda_1`, finite. By assumption each atom
sits at a grid angle, hence by S5 at an eigenvalue angle of `U_J`. Choosing one
unit eigenvector per distinct atom angle, which are orthogonal because the
angles differ, and setting

```text
v = sum sqrt(mass_i) . eigenvector_i,
```

gives `||v||^2 = sum mass_i = lambda_1 < infinity`, so `v` lies in
`L^2(O_lambda,Haar)`, and its spectral measure is `mu`. If two ordinates share
an angle their masses are added before the choice, so the atoms stay distinct.

By the spectral theorem `||sum_(k<n) U_J^k v||^2 = integral D_n d mu =: f(n)`.
Since `D_0 = 0` and `D_1 = 1`, we get `f(0) = 0 = lambda_0` and
`f(1) = mu(T) = lambda_1`. By `P-LAMBDA-COCYCLE-ANGLES-1` R3 and R7, at pin
`d7ad9d99`, the second differences agree for every `n >= 1`. A sequence is
determined by two consecutive values together with all its second differences,
so `f(n) = lambda_n` for every `n >= 0`. That is exactly the cocycle condition,
so `v` is a cocycle vector. Blocks C6-01, C6-02, C7-01 through C7-03.

## S7 [T intended]

Combining the directions:

```text
a cocycle vector exists
  <=>  RH holds and every Cayley angle 2 arctan(1/(2 gamma))
       lies in 2 pi (1/4) Z[1/5].
```

Necessity is `P-LAMBDA-COCYCLE-ANGLES-1` R2 and R3 together with S5: the
hypothesis forces `lambda_n >= 0` hence RH, its spectral measure is the
Cayley-angle measure, and by S5 the spectral measure of any vector is supported
on the grid. Sufficiency is S6. Blocks C8-01 through C8-04.

## Consequence for the frontier

`LAMBDA-COCYCLE-ANGLES [H]` was registered as a one-way implication: a cocycle
vector *forces* the grid condition. It is now an **equivalence**, and therefore
reducible to a single arithmetic statement about the zeros of zeta. Using
`P-LAMBDA-COCYCLE-ANGLES-1` R1, the row says exactly:

```text
every nontrivial zero of zeta has the form
  rho = 1/(1 - xi),   xi^(4 . 5^a) = 1,
equivalently
  gamma = (1/2) cot(pi m/(4 . 5^a)),
an explicit algebraic number of Q(zeta_(4 . 5^a)).
```

The hypothesis is therefore true if and only if every zeta ordinate is one of
these explicit cyclotomic algebraic numbers, together with RH. No operator,
measure-theoretic, or computational route remains: the third registered
falsifier branch, an all-vector contradiction inside the declared class, is
closed by S5 and S6, because the class is nonempty exactly when the arithmetic
condition holds. The only surviving attack is an exact arithmetic or
transcendence exclusion of one ordinate from that explicit countable set, and
that set is dense in the reals, so no numerical enclosure can decide it.

Taken with `P-LAMBDA-COCYCLE-ANGLES-1`, all three registered falsifier branches
of the row are now known to be the same branch.

No Canon, registry, frontier, evidence, or status file is edited by this probe.
Recording the equivalence in `canon/` requires a separate sealed fold.
