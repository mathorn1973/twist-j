# Infinite-volume assessment of the finite S2 candidate

**Author:** A. M. Thorn.  
**Date:** 21 September 2026.  
**Status:** PUBLIC; NON-CANONICAL; candidate compactness proof and conditional reconstruction plan.

This file is a mathematical assessment of the supplied definitions,
not a change to the frozen bundle, a scientific execution, a Canon promotion, or
a proof of the photon predicates. The statements below distinguish a complete
compactness argument, abstract conditional lemmas, and model-specific work still
needed before claiming their complete application.

## 1. An unconditional next result: cluster states exist

Let `mu_N` be the given periodic measure on the even `N^4` torus, using exactly
the fixed positive plaquette weight and all link configurations. Let
`X = F_5^{E(Z^4)}` be the space of positive-oriented infinite-lattice edge fields.
Extend each torus field periodically to `X`; this defines a probability measure
`nu_N` on `X`. No new measure or boundary prescription is introduced by this
bookkeeping operation.

**Proposition A.** Every sequence of even sizes tending to infinity has a
subsequence along which every bounded local cylinder expectation converges.
Every such limiting state is a probability state for the same finite-range
plaquette specification. It inherits lattice translations, the lattice
reflections and rotations preserved by the periodic action, charge conjugation,
and local gauge invariance.

**Proof.** Enumerate the cylinder events specifying finitely many edge values.
There are countably many. Their probabilities lie in `[0,1]`. Successively
extract convergent subsequences and use the diagonal subsequence. Finite marginal
normalization, positivity and consistency are finite equalities/inequalities and
therefore pass to the limit. The consistent marginals define a probability
measure on the countable product `X`. Every local cylinder function is a finite
linear combination of cylinder indicators, so all such expectations converge
on this same subsequence. Any symmetry identity involving finitely many edges
passes to the limit. A finitely supported gauge transformation and all tested
edges embed without collisions in every sufficiently large torus, so its
invariance identity also passes to the limit.

For the Gibbs conditional equations, fix a finite edge set `Delta`, a local
function `F`, and a local function `H` depending only on edges outside `Delta`.
For all sufficiently large tori the support and the plaquette neighborhood of
`Delta` embed without wrapping or collisions. The finite conditional-resampling
identity is then

`mu_N(F H) = mu_N((gamma_Delta F) H)`,

where `gamma_Delta` resamples the edges in `Delta` with probabilities proportional
to the product of the original weights on the plaquettes meeting `Delta`.
Strict positivity of `W` makes its finite denominator nonzero. Both sides are
expectations of fixed cylinder functions, so the identity passes to the limit.
The cylinder identities imply the conditional equations for the infinite state
by the usual monotone-class extension. This argument does **not** claim that a
periodically lifted finite measure itself satisfies the infinite conditional
equations: conditioning on all its periodic copies would be an invalid shortcut.

**Exact limitation.** Proposition A does not prove convergence through *all*
even sizes, uniqueness of the periodic cluster state, uniqueness of all Gibbs
states, clustering, or ergodicity. A subsequence cannot replace the stipulated
state in S1-S7.md:134-156. Even a uniquely selected subsequence would change that
contract unless equivalence to the full sequence were proved.

For the full prescribed limit, the missing condition can be stated minimally:
all cluster states of the even periodic sequence agree on every gauge-invariant
local cylinder function. Compactness then implies convergence on that algebra.
Uniqueness among all Gibbs states would suffice but is stronger than necessary.

## 2. Reflection positivity: what must be checked locally

Let `A_+` consist of gauge-invariant cylinder functions all of whose supporting
edges lie in the closed half-space `x_0 >= 0`. Spatial links on its boundary are
included; links crossing from `-1` to `0` are excluded. Let `tau` translate a
function one time step into this half-space. Let `Theta_0` be the antilinear
cochain pullback by reflection in `x_0=0`, and let
`Theta_{-1/2}=tau^{-1} Theta_0` be the reflection in `x_0=-1/2`.

For an infinite cluster state `omega`, the sufficient forms are

`s(F,G) = omega((Theta_0 F) G)`,

`l(F,G) = omega((Theta_{-1/2} F) G)`.

The required finite check is positivity of **both** forms on all gauge-invariant
positive-half cylinder functions, with these geometric support and oriented-edge
conventions. Reflection positivity is a closed inequality in finitely many local
expectations, so established finite inequalities pass to every cluster state.
Pointwise positivity of `W`, by itself, must not be substituted for this check.

There is a concrete route for this weight. For a site cut, condition on the two
boundary spatial-link layers of an even periodic torus; the two half integrals
are conjugate and boundary spatial-plaquette weights are positive. For a link
cut, gauge-fix the temporal links crossing the two cuts, then expand every
crossing plaquette with `W(f)=2+j^f+j^{-f}`. The coefficients `2,1,1` are
nonnegative, so each seam contribution factors into a character and its
reflected conjugate. On even tori of temporal size at least four, the two cut
layers can be fixed separately; no temporal holonomy may be silently removed.

**Remaining model-specific proof obligation.** The supplied TRANSFER.md gives
the positive single-slice matrix, but does not spell out this two-cut argument
for arbitrary gauge-invariant cylinder functions. Before promoting a full
infinite reconstruction claim, write and check the gauge-fixing change of
variables, its counting factor, the treatment of both cuts, and the oriented
reflection action on temporal plaquettes. This assessment identifies the route;
it does not certify that omitted finite-cylinder argument as already reviewed.

## 3. Conditional lemma: both reflected forms give the OS transfer

**Proposition B.** Suppose `omega` is a translation-invariant probability state
and the two forms in section 2 are positive. Then the quotient/completion for
`s` has a positive self-adjoint contraction `T[F]=[tau F]`. Its constant vector
`Omega=[1]` has norm one and `T Omega=Omega`.

**Proof.** Translation and reflection imply
`s(tau F,G)=s(F,tau G)`. Write `b_n=||[tau^n F]||_s`. Cauchy-Schwarz gives

`b_n^2 = s(F,tau^{2n}F) <= b_0 b_{2n}`.

Also `b_n <= ||F||_infinity`, since `omega` is a probability state. If `b_0=0`,
the displayed inequality gives `b_1=0`. Otherwise its iteration gives

`b_1 <= b_0^(1-2^(-k)) ||F||_infinity^(2^(-k))`.

Taking `k` to infinity proves `b_1<=b_0`. Thus time translation preserves the
null space and extends to a contraction. The symmetry identity makes its bounded
extension self-adjoint. Finally translation invariance gives

`s(F,TG)=omega((Theta_{-1/2} F)G)=l(F,G)`,

so link reflection positivity gives `T>=0`. The constant-vector claims follow
directly from normalization and translation invariance.

Let `Pi=1_(0,1](T)` and `H_+=Pi H_OS`. On this space spectral calculus defines
the possibly unbounded nonnegative self-adjoint operator `H=-log T`. It does
not require a lower bound on the nonzero spectrum of `T`. No finite energy is
assigned to `ker T`. The vacuum/reference vector stays in `H_+`.

Spatial translations induce commuting unitaries on the OS quotient. They
commute with `T`, `Pi`, and the spectral projections of `H`. This statement
uses exact lattice symmetry; it supplies neither continuous rotations nor a
causal velocity.

## 4. Bounded electric fields need no limit of the polar unitary

The finite unitary in TRANSFER.md:204-211 changes with the entire volume. Its
finite existence and finite norm identities do not imply convergence or
locality of that unitary. A direct limit of that unitary is unnecessary for the
following route.

Let `g_l=G(f_{0i}(-1,x))` denote the positively oriented temporal plaquette
crossing the cut at `-1/2`. With the convention that the Hilbert inner product is
antilinear in its first entry, define on `A_+` the sesquilinear seam form

`e_l(F,G) = i omega((Theta_{-1/2} F) g_l G)`.

The sign is deliberate: if the negative and positive boundary fields are `a`
and `a'`, this plaquette has `f=a'-a-d lambda`; the matrix in the first-to-second
inner-product order uses `D(a,a')`, so oddness of `WG` converts `+i WG(a'-a)`
to the finite kernel `-iD(a,a')`. The sign must be verified again in the complete
gauge-seam proof, not inferred from an unsigned norm inequality.

The sufficient finite inequalities are

`-(1/kappa) l(F,F) <= e_l(F,F) <= (1/kappa) l(F,F)`.

They have a very short candidate seam proof: replace that crossing factor by
`W + i kappa WG` or `W - i kappa WG`. Their unnormalized Fourier coefficients
are respectively `(10,10,0,0,0)` and `(10,0,0,0,10)`. Both are nonnegative.
Thus the same two-cut character argument, if completed for these two modified
seam weights, proves `l +/- kappa e_l >= 0`. These are algebraic reflected-form
inequalities, not probability measures with complex weights.

**Conditional consequence.** Once these finite-cylinder inequalities are
proved, they pass to the cluster state. The bounded-form lemma then gives a
unique bounded self-adjoint operator `E_l^link` on the quotient/completion for
`l`, with norm at most `1/kappa`. The map

`J[F]_link = T^(1/2)[F]_site`

is an isometry, because `l(F,G)=s(F,TG)`. Its completed range is exactly `H_+`.
Therefore `E_l = J E_l^link J^*` is a bounded self-adjoint operator on the same
positive-support space as `H`, with norm at most `1/kappa`. Its finite-matrix
formula is precisely the sandwiched electric insertion of the supplied S2.

This argument avoids claiming convergence of inverse square roots,
Hamiltonians, or polar unitaries across different finite Hilbert spaces.
It would establish operator matrix elements on the locally generated OS space.
It does not, without further argument, preserve the sharp finite norm, the
exact three-point spectrum, the cubic identity, or joint commutativity.
Compression/weak convergence alone does not preserve those claims.

For magnetic fields, multiplication by a bounded real slice-zero score is
bounded already on the site OS space. Indeed, for `c=||b||_infinity`, the
boundary function `sqrt(c^2-b^2)` is reflection invariant, and positivity of its
OS norm gives `||bF||_s <= c||F||_s`. Compression `Pi b Pi` retains the bound
`2+sqrt(5)`. Products of compressed operators still must not be substituted for
uncompressed coincident insertions.

## 5. Joint measure: existence is weaker than the photon target

Under the completed hypotheses of sections 2-4, let `O_I` be the six resulting
bounded Hermitian insertions on `H_+`, and set
`v_I=(O_I-<Omega,O_I Omega>)Omega`. The commuting spectral resolution of `H`
and the three lattice-translation unitaries gives a projection-valued measure
`P(dE,dk)` on `[0,infinity) x T^3`. Then

`Sigma_IJ(B)=<v_I,P(B)v_J>`

is a finite positive matrix-valued measure, and

`<v_I,exp(-tau H) U(x) v_J>
 = integral exp(-tau E) exp(i k.x) dSigma_IJ(E,k)`.

This is a direct spectral construction in one cluster-state Hilbert space; it
does not interchange the periodic volume limit with a ground-state-first
limit. If the full prescribed periodic state were subsequently proved unique,
the same construction would apply to that state without choosing a favorable
subsequence. The exact centered temporal/spatial covariance identities, signs,
half-step factors, and contact terms should be recorded when identifying this
measure with all entries of the S1 raw covariance.

No momentum density is implied. The joint measure may be singular in momentum,
and it may give the observed fields zero weight. The existence of this measure
does not prove the dimension-two scaling limit, an atom at `E=|q|`, a nonzero
residue, the rank-two projector, the selected D3 tangent normalization, locality,
or any error modulus. Those remain precisely the later S1-S7 obligations.

## 6. Smallest defensible next deliverable

1. Record Proposition A, with its explicit subsequence boundary, as an additional
   candidate mathematical result.
2. Write the finite two-cut reflection and modified-seam proof once, including
   the sign calculation. Propositions B and the bounded-form construction then
   supply a concrete subsequential reconstruction theorem.
3. Retain **OPEN** for convergence of the entire even periodic sequence. The
   exact missing hypothesis is uniqueness of its cluster-state local marginals,
   not an estimate on the finite electric norm.
4. Keep the massless pole and every actual-residue predicate open. A Canon scope
   proposal could concern the finite theorem or the compactness theorem, subject
   to repository review and promotion rules; it cannot close the photon gate.

External historical context only: Osterwalder and Seiler's
[Gauge field theories on a lattice](https://doi.org/10.1016/0003-4916(78)90039-8)
connects lattice reflection positivity with positive self-adjoint transfer
matrices. No phase, uniqueness, or continuum theorem is imported from that
paper here; the statements above concern this explicit finite-group weight.

Original new text: Apache-2.0. The external paper is bibliographic context only.
