# Exact finite-centre measurement contract

**PUBLIC / NON-CANONICAL.** Candidate `C-PHOTON-U1-FINITE-CENTER-N`,
owner issue #1715. Original work by A. M. Thorn, Apache-2.0.

This file specifies a source observable and its exact computational
implementation. It is not a phase result, an infinite-volume certificate,
or a replacement for the separately owned Z5 probe #1116. Any execution
is restricted to the complete prospectively pinned PREREG.md of this item.
The deterministic qualification and bounded engineering exercise below
must not be represented as a production phase measurement.

## 1. Fixed finite measure and real source

Let K be the periodic positive-coordinate cubical lattice with lengths
`(L_0,...,L_(D-1))`, each at least two, with `2<=D<=4`. All links are
summed, without gauge fixing or a selected flux sector. The normalized
partition function is

```
Z_7[a] = 7^(-|E|) sum_(A in Z7^E) product_p w((dA)_p + a_p),
w(theta) = 2 + 2 cos(theta).
```

The integer argument `(dA)_p` in the displayed shorthand represents
`2*pi*(dA)_p/7`; `a_p` is a real angle. The implemented untwisted weight
is `w(2*pi*k/7)`, not a Wilson exponential or a Villain approximation.

The finite-centre theorem gives `Z_7[a]=Z_U1[a]` for all real plaquette
sources. This statement concerns the selected finite action and source
carrier. No physical measure-selection or L4-to-L6 bridge follows.

For orientation `(mu,nu)`, put `A_mu_nu=L_mu*L_nu`. Let B be the stack
of `(mu,nu)` plaquettes based at `x_mu=x_nu=0`, with all transverse
coordinates unrestricted. Let U be `1/A_mu_nu` on every plaquette of
this orientation and zero on other orientations. Integer closure implies

```
<n,B> = W_mu_nu in Z,
sum_(p parallel mu,nu) n_p = A_mu_nu * W_mu_nu,
<n,B> = <n,U>.
```

The equality is for every integer-closed two-chain, including nontrivial
torus cycles. Consequently the complete source functions agree:

```
Z_7[alpha B] = Z_7[alpha U] = Z_U1[alpha B],
Z[alpha B]/Z[0] = E_n exp(i alpha W_mu_nu),
h_(mu,nu) = -d^2/dalpha^2 log Z[alpha B] at alpha=0
           = Var_n(W_mu_nu).
```

This exact stack/uniform equality at all orders uses integer closure.
It must not be transferred to Z5, where charge-five currents are admitted.

## 2. Bounded cubic-field reader on untwisted Z7 states

Let x be the root in `(1,3/2)` of

```
x^3+x^2-2x-1=0,
x=2 cos(2*pi/7),
r=(2-x)/(2+x)=tan(pi/7)^2.
```

The four distinct weights are

```
w(0)=4,
w(+/-1)=2+x,
w(+/-2)=x^2,
w(+/-3)=3-x-x^2.
```

Define the odd seven-value reader G by

```
G(0)=0,
G(1)=1,
G(2)=(2+x)/x,
G(3)=(1+x)/(x-1),
G(7-k)=-G(k).
```

Then `X(k)=tan(pi*k/7)=sqrt(r)*G(k)`, with the odd residue convention.
For `s=-log w`, `s'=X` and `s''=(1+X^2)/2`. Charge conjugation makes the
equilibrium first source derivative zero. Thus one exact per-configuration
reader for an arbitrary rational real-source direction `a` is

```
H_a(A) = sum_p a_p^2 * (1+r*G(f_p)^2)/2
         -r*(sum_p a_p*G(f_p))^2,
E_7 H_a = -d^2/dalpha^2 log Z_7[alpha a] at zero.
```

For the uniform source this specializes to

```
H_(mu,nu)(A)
  = [V/2 + (r/2) sum_x G(f_(mu,nu)(x))^2
     -r*(sum_x G(f_(mu,nu)(x)))^2] / (L_mu*L_nu)^2,

E_7 H_(mu,nu) = h_(mu,nu) = Var_n(W_mu_nu).
```

On an isotropic four-torus `V=L^4`, the prefactor is `1/V`. In other
dimensions or rectangular boxes retain the displayed plane-area square;
replacing it with `1/V` is generally wrong. The default reader averages
all `C(D,2)` orientations with equal preassigned coefficients.

Every value is in the real cubic field Q(x). No square-root extension is
needed because the score occurs quadratically. Unlike the continuous U1
score estimator near angle pi, this finite-centre estimator has no poles
on its sampled alphabet. It is bounded at every finite volume, although
its worst-case magnitude and variance need not be uniform in volume.

Individual H values may be negative. They must never be clipped to zero,
and the square of a finite sample mean must not replace the displayed
per-configuration squared total score. The equality with `Var(W)` is an
expectation identity, not equality of the two random variables.

## 3. Exact heat bath and what it proves

`z7_exact.py` implements Q(x) by rational triples modulo the minimal
polynomial. The selected embedding is ordered by certified rational root
intervals. Nonzero quadratic polynomials cannot vanish at x, so every
nonzero sign comparison terminates after sufficiently many refinements.

A four-dimensional link meets six plaquettes. For current link value k,
signed incident fluxes f_p and incidence signs s_p, define staples

```
a_p = k - s_p*f_p mod7.
mass(v) = product_(p incident e) w(v-a_p), v=0,...,6.
```

The complete table has at most `binomial(12,6)=924` staple-count vectors
and seven masses per vector. Reversal symmetry of w makes this form
identical to direct replacement of the link in the original action.
All masses and their normalizers lie in Q(x).

Categorical sampling uses successive 32-bit blocks specifying a nested
half-open dyadic interval for a uniform U. A category is accepted only
when the entire dyadic interval lies between its exact cumulative
probabilities. No floating-point probability, acceptance threshold, or
fixed-precision fallback is used. With independent ideal fair bits this
terminates almost surely and has exactly the target categorical law.
The concrete `random.Random(seed)` stream is a reproducible deterministic
engineering input; it is not a proof of ideal independent randomness.

All seven plaquette weights are strictly positive. For example the root
can be isolated inside `(6/5,5/4)`, which gives `w(k)>=3/16` and `w(k)<=4`.
Hence every one-link transition has positive probability, including
self-transitions. A sequence of single-link assignments connects any
two configurations. The finite-volume chain is irreducible and
aperiodic, and each link heat bath preserves the exact Gibbs measure.
A deterministic full sweep preserves it as a composition; the full
sweep is not claimed reversible.

These facts establish the finite stationary distribution and eventual
convergence, not a practical mixing time. The elementary lower bound
`P(v | rest)>=(3/64)^6/7` in four dimensions yields only a prohibitively
small whole-lattice minorization. Passing finite diagnostics does not
turn that bound into useful equilibrium certification.

The implementation retains the full link state, caches plaquette fluxes,
and checks them against a direct curl. It also checks the mod-seven
Bianchi identity and integer divisibility of principal-lift plane sums.
Those plane sums are primal diagnostics; they are not the dual winding W.
Flat holonomy changes leave every plaquette unchanged and do not certify
motion between magnetic-flux sectors.

## 4. Exact end-to-end controls before any phase sampling

Use complete two-dimensional periodic controls with areas A=4 and A=6,
represented by `2x2` and `3x2` tori. A plaquette configuration is admitted
exactly when its residue sum is zero mod7. Enumerating its first A-1
residues determines the last, so there are `7^(A-1)` fields. Every such
field has the same number of link lifts. Therefore normalized sums over
these fields equal normalized Haar link expectations exactly.

The integer-closed surface configurations in two dimensions are only
`n identically 0,+1,-1`. With the unscaled weight w, the exact targets are

```
Z(0) = 2^A+2,
Z(alpha B) = 2^A+2 cos(alpha),
h = 2/(2^A+2).
```

At `alpha=2*pi/7`, the shifted partition is `2^A+x`. The qualification
must check the full partition, the source shift, and the expectation of
both H_stack and H_uniform. The two readers need not agree pointwise.
These controls catch missing winding sectors: a boundary-only dual
representation would instead retain only n=0 and return zero h.

Additional exact checks include the field polynomial and inverses,
positive weights, odd score values, all local staple masses against
direct plaquette replacement, categorical boundary handling with scripted
bit streams, incidence orientations, cache updates and intentional state
corruption. These are deterministic implementation tests. A finite test
does not replace the written all-volume source theorem.

The bounded four-dimensional seeded exercise, if included in the pinned
PREREG.md, is limited to the declared sizes, seeds, starts and sweep
counts. It checks that actual transitions, state readback and the exact
reader operate together. Its H values are engineering output only.
No thermalization or phase terminal is earned by that exercise.

## 5. Prospective finite-size phase experiment

The mathematical primary observable is fixed by section 2: the equal
average of the six uniform-source Hessians on isotropic four-tori, with
all six components retained separately. The comparison model is exactly
the selected U1 action by the finite-centre theorem; no large-N or Wilson
comparison is needed. All topological sectors must remain admitted.

Before production, a separate public execution pin must fix:

1. the complete size list, independently chosen cold/hot/flux-biased
   starts, fresh seed family, warmup budget, recorded count and spacing;
2. source, arithmetic and reader hashes, complete state-custody format,
   an independently authored state reader, and a bounded resource test;
3. chain-preserving uncertainty analysis, autocorrelation handling,
   start/time/orientation comparisons and explicit failure terminals;
4. the precise finite-size inference and its assumptions, including
   whether it examines a positive intercept, a vanishing response or
   merely reports unresolved size dependence;
5. an explicit distinction between empirical mixing diagnostics and a
   proved bound on sampling error relative to equilibrium.

Frozen hard terminals must include `STOP_INTEGRITY`, `STOP_MIXING`, and
`UNRESOLVED`. A finite-size orientation terminal cannot be called an
infinite-volume Coulomb or confinement theorem. In particular a
positive h at each finite L may still vanish as L grows.

Seven discrete twists alone determine only the distribution of W modulo
seven. They do not determine `Var(W)` when the winding range exceeds
that alphabet. The uniform Hessian reader avoids that aliasing issue by
computing the derivative at zero directly. If a later experiment uses
twist ratios instead, its finite-difference or winding-tail error needs
its own bound.

This item supplies no production size law, equilibrium error bound or
phase decision. It supplies an exact observable, an exact transition
kernel, complete finite controls, and a separately auditable route to
the next experiment without confusing code operation with physics.
