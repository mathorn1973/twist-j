# Strict finite profiles do not see the lambda grid

```text
STATUS:      NON-CANONICAL candidate-T RESULT
ISSUE LOCK:  #363
METHOD:      written proof; no computation is load-bearing
TARGET:      finite-profile and effective-conductor-tail shortcut only
DECISION:    bounded no-go; LAMBDA-COCYCLE-ANGLES remains H
```

## 1. Attack question

Can finitely many exact Li second differences, after passing every required
Toeplitz positivity test, force or falsify a nontrivial upper bound on the
mass above conductor `4*5^A`?

The answer is no. The obstruction is not numerical precision. It is the
interior geometry of the truncated trigonometric moment problem.

## 2. Dense-grid truncated moment lemma

Let

```text
c_(-k) = conjugate(c_k),
c_0    = M > 0,
T_N(c) = (c_(j-k))_(j,k=0)^N.
```

Let `E` be any dense subset of the unit circle. If

```text
T_N(c) is positive definite,
```

then there is a finite positive measure `tau_E`, carried by `E`, such that

```text
c_k = integral_T z^k d tau_E(z),   |k|<=N.
```

It can be chosen with at most `2N+1` atoms. If, in addition, `E` is invariant
under complex conjugation and the profile is real and even, conjugation
symmetrization preserves every displayed moment and uses at most `4N+2`
atoms.

### Proof

Normalize by `M` and use the real moment curve

```text
Phi_N(z)
  = (Re z, Im z, Re z^2, Im z^2, ..., Re z^N, Im z^N)
  in R^(2N).
```

Its convex hull is the mass-one trigonometric moment body. The normalized
profile lies in its interior exactly when `T_N(c)` is positive definite.
Indeed, the dual affine functionals are real trigonometric polynomials of
degree at most `N`; by Fejer-Riesz every nonzero nonnegative one is
`|p(z)|^2`, and its value on the profile is

```text
coeff(p)^* T_N(c) coeff(p) > 0.
```

Write

```text
K = conv(Phi_N(T)),
C = conv(Phi_N(E)).
```

The preceding dual argument gives that the normalized profile `x` belongs to
`int K`: otherwise a supporting hyperplane would give a nonzero real
trigonometric polynomial `q>=0` with `L_x(q)<=0`, whereas Fejer-Riesz and
positive definiteness give `L_x(q)>0`.

Density of `E` gives `closure(C)=K`. For every nonempty convex set, its
relative interior equals the relative interior of its closure. Here `K` is
full-dimensional in `R^(2N)`, so

```text
x in int K = int C subset C.
```

Thus `x` is an exact finite convex combination of points `Phi_N(E)`, not only
a limit of such combinations. Caratheodory's theorem reduces the combination
to at most `2N+1` points. The resulting positive barycentric weights give
`tau_E` and reproduce the moments exactly.

For a real even profile, replace `tau_E` by

```text
(tau_E + conjugation_* tau_E)/2.
```

The grid sets used below are closed under conjugation, so the symmetrized
measure remains on the same allowed set.

## 3. Finite-profile grid-realization theorem

Put

```text
G_A = {z : z^(4*5^A)=1},
G   = union_(A>=0) G_A.
```

Assume `T_N(c)>0`. Then all of the following hold.

### R1. Exact grid fit

There is a finite positive measure carried by `G` that reproduces every
`c_k`, `|k|<=N`.

This is the lemma with the dense subset `E=G`.

### R2. Exact high-conductor fit

For every fixed `A`, there is such a measure carried by `G minus G_A`.

The set `G_A` is finite, while `G` is dense; hence `G minus G_A` is dense and
the lemma applies again.

### R3. Exact bounded-conductor fit

There is `A_0` such that for every `A>=A_0` there is such a measure carried by
`G_A`.

Choose the finite grid measure from R1. Its finite support lies in one common
`G_(A_0)`, and the sets `G_A` are nested.

### R4. The same profile permits every tail mass

For every `A>=A_0` and every `r in [0,M]`, there is a grid-carried measure
with the same moments through degree `N` and

```text
tau(T minus G_A) = r.
```

Let `tau_in` be an R3 measure carried by `G_A` and let `tau_out` be an R2
measure carried by `G minus G_A`. Both have total mass `M` and the same
profile. Then

```text
tau_r
  = (1-r/M) tau_in + (r/M) tau_out
```

has the required moments and tail exactly `r`.

This proves a complete finite-profile no-go: once the Toeplitz block is
strictly positive, the same exact data permit both zero tail and full tail at
every sufficiently large frozen conductor.

## 4. Arbitrarily slow tails at one fixed finite profile

The obstruction is stronger than the one-conductor statement. Let

```text
1 >= r_0 >= r_1 >= ... -> 0
```

be any prescribed rate. There is one positive measure `tau`, carried by `G`,
with the same moments `c_k`, `|k|<=N`, and

```text
R_A(tau) >= M r_A   for every A.
```

For each `A`, choose by R2 a profile-matching probability-scaled measure
`tau_A` of total mass `M`, carried by `G minus G_A`. Put

```text
w_A = r_A-r_(A+1).
```

The weights sum to `r_0`. Choose any further profile-matching grid measure
`tau_*` and define

```text
tau
  = (1-r_0) tau_* + sum_(A>=0) w_A tau_A.
```

This is a finite positive measure of total mass `M`, carried by the countable
set `G`, and every component has the same frozen moments. At level `B`, each
`tau_A` with `A>=B` is carried outside `G_B`, because `G_B` is contained in
`G_A`. Therefore

```text
R_B(tau)
  >= M sum_(A>=B) w_A
   = M r_B.
```

Continuity from above still gives `R_A(tau)->0`; the convergence can simply
be slower than any rate proposed from the finite profile.

## 5. Exact finite witness

The theorem is proof-level, but one small exact example shows the geometry.
Let `N=12` and compare:

```text
tau_in  = uniform probability on mu_100,
tau_out = uniform probability on zeta_500 mu_100.
```

Here `mu_100=G_2`, while the second set is a disjoint coset contained in
`G_3 minus G_2`. For every `0<|k|<=12`, both `k`-th moments vanish, and their
zeroth moments equal one. Thus they have exactly the same profile

```text
c_0=1,
c_k=0,  0<|k|<=12,
```

but their level-two tails are respectively zero and one. Their convex mixture
with outside weight `37/101` has the same profile and tail exactly `37/101`.
No floating point or zero table enters this example; it is illustrative and
is not public probe evidence.

## 6. Li application

Assume RH. The public Cayley measure is

```text
sigma
  = sum_(gamma>0)
      (delta_(exp(i alpha_gamma))+delta_(exp(-i alpha_gamma)))
      /(1/4+gamma^2),

alpha_gamma = 2 arctan(1/(2 gamma)),
```

The positive ordinates are counted with multiplicity. Its Fourier coefficients
are the Li second differences `t_n`. The measure is
finite, positive, and has infinitely many distinct atoms. Hence every finite
Toeplitz block is strictly positive: for a nonzero polynomial `p` of degree at
most `N`,

```text
coeff(p)^* T_N(t) coeff(p)
  = integral_T |p(z)|^2 d sigma(z) > 0,
```

because such a polynomial cannot vanish at infinitely many distinct points.

The theorem therefore implies:

```text
under RH, every finite Li second-difference profile has an exact
positive grid-carried representing measure.
```

The real even profile can be represented by a conjugation-symmetric grid
measure `sigma_N`. Put `mu_N=sigma_N/2`. The public carrier `U_J` has every
grid angle as an eigenvalue, so one can choose finitely many orthogonal
eigenvectors with squared coefficients equal to the masses of `mu_N`. Their
sum is a vector `v_N in L^2(O_lambda)` whose spectral measure is `mu_N`.

The Fejer norm sequence

```text
f_N(n)
  = ||sum_(k=0)^(n-1) U_J^k v_N||^2
```

has

```text
f_N(0)=0,
f_N(1)=lambda_1,
f_N(n+1)+f_N(n-1)-2f_N(n)=t_n.
```

Matching `t_n` through `n=N` therefore gives

```text
f_N(n)=lambda_n,   0<=n<=N+1.
```

This is a different vector for each cutoff. It is not one all-index cocycle
vector and supplies no converse to the public hypothesis.

The strictness hypothesis is essential. An indefinite finite block remains a
valid finite falsifier of RH and of the cocycle class. A singular boundary
profile may impose support restrictions that a chosen dense subset fails to
meet. The theorem neither repairs nor dismisses those cases.

## 7. Decision

[NON-CANONICAL candidate-T]

The finite-profile effective-tail shortcut is structurally dead at exactly
the strict-positive scope that the Li profiles occupy under RH. Within the
truncated positive-moment model, no fixed finite Li profile can force a
nontrivial universal bound on `R_A`, even after restricting candidate measures
to the public grid, absent additional zeta-specific structure. The same
profile permits every tail in `[0,M]` at large enough conductor and permits
arbitrarily slow decay in one grid-carried realization.

This does not fire `LAMBDA-COCYCLE-ANGLES [H]`. It removes one attack route.
The surviving route is genuinely global: prove or disprove the full 5-adic
uniform continuity, an effective all-moment conductor-tail estimate, or exact
arithmetic membership of one Cayley angle.

No computation, finite census, increased precision, or fixed Toeplitz tower
inside this truncated moment model can replace that global input.
