# REVIEW ADDENDUM C-RH-PYTHAGORAS-HALFANGLE-2-N

```text
STATUS:        NON-CANONICAL POST-PREREGISTRATION REVIEW
AUTHORITY:     none
ISSUE:         #355
OPEN PR:       #356 (pre-consolidation lane)
PUBLIC BASIS:  Public Canon v46, main 6545c1d0
PUBLIC STATUS: no change
RH STATUS:     O (unchanged)
```

This addendum records review corrections without rewriting the frozen
`PREREG.md` or relabelling its G1-G7 gates and existing candidate results.

## 1. Source-scope correction

The frozen preregistration imports Suzuki Theorem 1.7, the diagonal condition
`RH iff Psi(t)>=0`. That is sufficient for the pointwise norm-difference
reading in `RESULT.md`, but it does not establish positivity of every mixed
finite screw-kernel Gram matrix.

The source-side factorization and the abstract Gram-domination lemma require
no RH input. The downstream statement

```text
RH iff the full screw kernel is positive on every finite window
```

additionally imports Suzuki Theorem 1.2. Suzuki Theorem 1.3 is a separate
localized hermitian-form criterion on its stated zero-mean test class; it is
not a direct replacement for the pointwise-kernel statement without a typed
kernel-to-form bridge and matching normalizations. Any future public claim
lock must name the theorem matching its exact kernel or form scope.

## 2. Exact complete-prime-sector no-go

The one-prime-leg breaker can be strengthened without computation. Let

```text
a=(1/4)log 6,   t_1=-a,   t_2=a.
```

For the full finite-prime delayed kernel, every `n>=3` term vanishes on these
two points, while `n=2` contributes

```text
(log 2)/sqrt(2) [[0,d],[d,0]],
d=(1/2)log(3/2)>0.
```

The determinant is exactly

```text
-(log 2)^2 (log(3/2))^2 / 8 < 0.
```

Therefore the entire finite-prime kernel is indefinite, not merely each
independent prime-power leg. Arbitrary mixing among prime powers cannot yield
the required contraction for the frozen feature carriers. Any surviving full
contraction for this source-side factorization must contain a nonzero
finite/archimedean cross block coupling prime channels to pole and/or
Gamma/Hurwitz channels.

This is a no-go, not the construction of that cross-place block. A later
public promotion of the stronger statement requires its own current claim
lock and review.

The theorem overlaps exactly with the prime-kernel half of #358 N5, up to the
sign convention relating `G_P` and `K_P`. The #358 `(3,6)` computation is a
second witness for the same no-go, not an independent theorem. The analytic
`+/-(1/4)log 6` witness is the shorter exact proof. The scalar-capacity `K_A`
half of #358 N5 remains separate.

## 3. Eighth-root convention

For the displayed unitary transform `U`, `det U=i`. A scalar determinant-one
correction satisfies

```text
lambda^2=-i,
lambda=+/-sqrt(-i)=+/-zeta_8^(-1).
```

The central sign remains free. This transform-specific conjugate eighth root
must not be conflated with a separate convention that writes
`zeta_8=sqrt(i)`. The phase changes neither norms nor kernel signature and is
not an RH mechanism.

## 4. Window coherence remains untyped

The finite-window factorization is exact at each fixed cutoff, but increasing
the window admits additional neutral Krein pairs. The feature spaces
`X_(+,a)` and `X_(-,a)` are therefore not automatically nested Hilbert spaces.
A coherence claim still requires frozen maps `J_(a,b)^+`, `J_(a,b)^-`, or a
specified neutral quotient, together with exact preservation laws. No such
global family is claimed here.

## 5. Relationship readback

The delayed and half-angle formulations are Fourier/Plancherel dual
descriptions of one mechanism, not two independent mechanisms. The abstract
contraction lemma in this lane and the diagonal-model lemma discussed in #358
belong to the same lemma family at different scopes and are not double-counted.

The feature carrier `X_(+,a)` and the functional candidate `q_A,a` in #357
are inequivalent-looking candidates for the same positive-capacity role. They
must enter one outcome-blind G0 classification before either is selected.
After a typed test-function-to-kernel map and Plancherel normalizations are
fixed, their prime sine/cosine pieces may be directly comparable to the
`V^-`/`V^+` channels. No such equality is claimed here before that bridge is
written.

Nothing in this addendum proves RH, proves #357 G3, constructs a cross-place
contraction, or changes any public status.
