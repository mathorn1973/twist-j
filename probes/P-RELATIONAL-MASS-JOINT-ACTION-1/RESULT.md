# A common action with reciprocal metric and relational-energy dynamics

Status: PASS
Scope: NON-CANONICAL, NEW_DECLARED L1, homogeneous planar common action
Theorem status: conditional candidate-T; no Canon promotion
Fired audit falsifiers: none
Ownership: https://github.com/mathorn1973/twist-j/issues/1686
Preregistration pin: f19fa98dc1634ce1e17b9dec402c51920d2bea8d

## The action and its exact balances

The predecessor supplied the metric variation of relational energy. The
present construction supplies a new common action by declaring a full SPD
inverse metric G, symmetric canonical momentum Pi and occupied matter
pairs (x_k,n_k p_k), with continuously varied nonzero covectors p_k:

    S=integral [tr(Pi Gdot)+sum n_k p_k^T xdot_k-K-E]dt,
    K=tr(G Pi G Pi)/2, E=sum n_k sqrt(p_k^T G p_k).

Multiplicity n_k is a fixed positive integer on an occupied slot. Empty
slots are omitted from the physical carrier. The explicit kinetic
normalization is one. This replaces the earlier scalar carrier; it does
not identify its old amplitudes with metric entries or inherit its M0.

With epsilon_k=sqrt(p_k^T G p_k) and T=sum(n_k/epsilon_k)p_k p_k^T,
variation gives

    Gdot=G Pi G, Pidot=-Pi G Pi-T/2,
    xdot_k=G p_k/epsilon_k, pdot_k=0.

The source is the energy derivative T/2, not the distinct derivative of
mass square. The weighted canonical form gives the individual velocity
without an extra factor n_k. The same variation yields reciprocal exchange

    Edot=tr(T G Pi G)/2=-Kdot.

H=K+E and P=sum n_k p_k are conserved. Simultaneous invertible linear
coordinate changes preserve the action and give the full matrix charge

    J=2G Pi+sum n_k x_k p_k^T, Jdot=0.

This is a finite homogeneous common action, not a first joint action claim
for all TWIST-J. Existing Canon FRW and TT statements retain their own scope.

## Global existence and a sharp long-time limitation

The positive metric kinetic geometry gives K>=0 and the matrix bound

    exp(-c|t-s|)G(s) <= G(t) <= exp(c|t-s|)G(s), c=sqrt(2H).

Together with the momentum and velocity bounds in PROOF.md, this proves
unique global flow for every admitted initial phase point. G stays SPD
for every finite time. This is a universal proof, not extrapolation from
the finite audit.

For nonempty matter, C=tr(G Pi) satisfies Cdot=-E/2<0 and is bounded.
Consequently E is integrable on the full time line. The independent bound
|Edot|<=sqrt(H/2)E supplies the regularity needed to conclude

    E(t)->0, K(t)->H, D_G(t)=E(t)^2-P^T G(t)P->0

at both temporal infinities. If occupied momenta span the plane, G tends
to zero at infinite time. G is the inverse metric; this does not describe
physical spatial collapse. No nonempty equilibrium or periodic full orbit
exists. The construction supplies no binding mechanism or stable-particle
claim, and does not exclude other common actions with additional terms.

The fixed-time problem is well-defined. A free lapse multiplying H alone
would impose the incompatible nonempty constraint H=0. An expressly added
clock pair (t,p_t) with constraint p_t+H=0 admits p_t=-H; it is a separate
canonical extension, not a physical or native clock derivation.

## Exact flow versus a separately declared algebraic step

The exact time-one map of the complete Hamiltonian flow is globally defined,
invertible, canonical symplectic and preserves H,P,J. Integer indexing does
not imply native integer states, an explicit finite formula or cyclotomic
closure at finite time.

The symmetric divided-difference DG relation in PREREG.md is instead an
independent algebraic comparison. Its local branch near h=0 exists uniquely
and is second order. Exact polarization proves H_+=H_-, but its actual
continuous-charge defect is

    DeltaJ=(h/2)(d Nbar d Nbar-M e M e),
    M=(G_++G_-)/2, Nbar=(Pi_++Pi_-)/2,
    d=DeltaG, e=DeltaPi.

At initial Pi=0 the cubic coefficient is -G T G T/8, nonzero for nonempty
matter. Thus even the unique branch near zero does not equal the exact
common-action flow. This conclusion does not depend on the continuation
branch of a finite witness.

The exact witness with all five multiplicities one has h=1100/1921,
G_-=(36/25)G0, Pi_-=0, G_+=G0, Pi_+=-G0^-1 and the prescribed position
increment (1220/1921)G0 u_k. Direct evaluation gives:

| Quantity | Initial | Final |
|---|---:|---:|
| Matter energy E | 6 | 5 |
| Metric kinetic energy K | 0 | 1 |
| Total energy H | 6 | 6 |
| Total momentum P | 0 | 0 |
| Relational mass square D_G | 36 | 25 |
| Dilation C | 0 | -2 |
| Full charge J | 0 | -(792/1921)I |

The Jacobian determinant of the induced isotropic step is 528275/341526, different
from one. The full output relation is regular there; restriction of the
canonical symplectic form proves this branch is nonsymplectic. Therefore
this energy-preserving step is not a canonical variational integrator for
the declared form. No all-h solver uniqueness, finite-field closure or
identification with the h=0 branch is inferred. These disproved alternatives
are intended boundary results; all audit gates passed.

## Exact computational evidence and remaining scope

Two isolated authors used distinct field representations and solvers:
rational pairs with triangular coefficient recursion and binomial roots;
normalized integer triples with four Picard passes and root recurrences.
They computed identical raw certificates without shared scientific code.

| Audit per implementation | Count |
|---|---:|
| Authority files | 5 |
| Binary five-direction preparations | 32 |
| Initial metric momenta | 7 |
| Main trajectory cases | 224 |
| Formal order | 4 |
| FLOW coefficient rows | 1120 |
| DG coefficient rows | 1120 |
| Covariance cases, each for both methods | 6 |
| Finite exchange and nonsymplectic witness | 1 |
| Negative controls detected | 8 |

The computed 2550-record payload has SHA-256
330fb22412f54c6dae1a434d74adf1f68d3e1cfea8b31bbcf59d6e2c0c01caee.
The primary stdout is 431 bytes in 17 lines, SHA-256
a59dd2310ae9f3bface7a738c561a7290d9fe4af2e4d39a5f048b771f1ca2642.
The first run exited zero with empty stderr in 33.012 seconds. Required
architecture replays are pending at this historical record and will be
receipted on the exact-head PR. The immutable pin and independent review
are documented in RUN.md, REVIEW.md and the public issue receipt.

No source localization, local spacetime propagation, scattering, binding,
stable particle, physical energy scale, Lorentz-complete carrier, native
clock, native implementation, unique physical metric, equality of inertial
and gravitational mass, or cross-layer realization is established.
Canon, registry, policy and workflows remain unchanged. The next substantive
obligation is an independently declared mechanism for persistent source energy
and a justified action-compatible realization; energy preservation alone
cannot supply either.
