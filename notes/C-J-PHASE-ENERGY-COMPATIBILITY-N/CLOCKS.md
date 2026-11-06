# Exact clock readings and their compatibility boundaries

PUBLIC / NON-CANONICAL / L1 / analytical candidate-T ceiling.
Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
Basis: Public Canon v103 at dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d.
All continuous carriers below are declared mathematical comparisons, not
admitted spacetime or measure lifts. No scientific execution is used.

## 1. The positive arithmetic clock already exists

J-UNIT-STRIP-NORMAL-FORM [T] gives, for nonzero alpha in O=Z[zeta_5],

    A=|sigma_1(alpha)|^2, B=|sigma_2(alpha)|^2,
    k(alpha)=-floor(log_(phi^4)(A/B)),
    A(J alpha)/B(J alpha)=phi^-4 A/B.

Therefore k(J alpha)=k(alpha)+1 exactly, including strip endpoints with
the registered half-open convention. No numerical logarithm is required:
the exact comparison algorithm in Q(sqrt5) finds the normalized strip.
This is existing mathematics, not a new discovery or a new physical clock.

J-TWO-TRACE-RESIDUE-INVERSE [T] recognizes and inverts D25 on the declared
nonzero norm<=941 carrier, returning alpha, its strip representative and k.
The traces are unbounded integers. U-NORMALIZED-SCALAR-READBACK [T] then
recovers the native counter on n>=3 from the explicitly CHOSEN
representation D25(J^n G(Lambda_n(x))), for a known normalized injection
G:F5^5->B_941 and the canonical reachable-sheet chart Lambda_n. It retains
G, the target J-action and availability
of exact observation as premises. The existence of this inverse is not
a mechanism that physically acquires its inputs or writes a receiver.

For any theta in R, the same clock supports

    chi_theta(alpha)=exp(i theta k(alpha)),
    chi_theta(J alpha)=exp(i theta) chi_theta(alpha).

Thus an exact orbit counter alone does not select theta. Even an
orbit-dependent theta(beta), with beta the invariant strip representative,
obeys that law on each orbit. Choosing a Compton frequency requires an
independently admitted energy and phase relation, not another counter.

On the declared noncompact V=K tensor_Q R, sigma_1(x)!=0, a smooth
alternative is s(x)=-log|sigma_1(x)|/log phi, with s(Jx)=s(x)+1. Its
logarithmic tick adds n after n steps, not phi^n. These functions depend on
the representative in V and do not descend to V/O.

## 2. A different answer on the Haar torus

The Fourier argument already in J-LI-TORAL-HAAR-NOGO [T] applies to
T_J on V/O with normalized Haar measure. The exact eigenvalue moduli of
M_J are phi,phi,phi^-1,phi^-1 (J-TORAL-ENTROPY [T]), so no eigenvalue
is a root of unity. For characters e_a indexed by a in Z^4,

    U e_a=e_(M_J^T a),       U f=f o T_J.

Every nonzero dual orbit is infinite: a repetition would give
((M_J^T)^r-I)a=0, whose coefficient matrix is invertible. If an L2
function f=sum_a c_a e_a satisfies U f=lambda f, |lambda|=1, the absolute
values |c_a| are constant on each such orbit. Square summability forces
all its coefficients to zero. Only c_0 remains, and (1-lambda)c_0=0.

Consequently lambda!=1 implies f=0; lambda=1 permits only constants almost
everywhere. In particular there is no nontrivial measurable unit-modulus
scalar phase with a constant nonzero angular advance on this Haar carrier.
The noncompact/arithmetic clock above is not a counterexample: quotienting
by O loses the representative on which it depends.

This does not exclude selected periodic orbits with a different measure,
an extra clock register, noncompact carriers, or general cocycles whose
products depend on history. No universal clock impossibility is claimed.

The proposed Lucas return requires a separate proof. L_n is a number-field
trace, not an established common return period. #Fix(T_J^r) counts points
whose least period DIVIDES r; it does not make L_r their period. T_J has
infinite order since |sigma_2(J^r)|=phi^r>1 for r>0. The field trace of a
representative is not automatically a function of its torus class either.

## 3. Blocking a fixed Dirac walk does not produce the new family

Use U_m and omega_m from PROPOSALS.md. First, the centered, unwrapped
phase-curvature quantity

    R(m)=omega_m(0) omega_m''(0)=atan(m)/m

is unchanged by omega(k)->b omega(a k) if the massless reference slope
changes from1 to |ba| and R is divided by that slope squared. Indeed both
numerator and denominator acquire b^2 a^2. Its derivative is negative for
m>0 because atan(m)>m/(1+m^2). Arbitrary additive energy offsets are NOT
included in this statement, nor is folding a phase back into a principal
interval after multiplication. The original fixed phase reading supplies
the energy zero.

A stronger operator statement avoids aliasing. For m,mu>0, integer r>=2,
a!=0 and a constant unitary C, there is no identity on an open k interval

    U_mu(k)=exp(i chi) C U_m(a k)^r C*.

Let t_m=(1+m^2)^(-1/2). Determinants force exp(i chi)=+1 or -1. Half
traces would give

    t_mu cos k= +/- T_r(t_m cos(a k)),

where T_r is the Chebyshev polynomial. For r=2 the right side contains the
nonzero constant t_m^2-1 as well as t_m^2 cos(2ak). For r>=3 its two top
harmonics have coefficients

    cos(rak):       t_m^r,
    cos((r-2)ak):   r t_m^(r-2)(t_m^2-1).

Both are nonzero. These coefficients follow by substituting into the
leading two terms 2^(r-1)x^r-r2^(r-3)x^(r-2) of T_r. Distinct real
exponential frequencies are linearly independent on any open interval;
the trace cannot reduce to a single cosine. For r=1 the only possibilities
have mu=m and a=+/-1. The excluded massless case permits a=+/-1/r.
This theorem covers only the displayed two-component identical-step
blocking class. Extra registers, alternating steps, nonlinear momentum
maps or a separately admitted refinement are outside it.

The exact rest identity from PROPOSALS.md is therefore valuable but local.
For 0<q<1 and m=2q/(1-q^2), the explicit discrepancy is

    tr(U_q(k)^2)/2 - tr(U_m(2k))/2
       = -2q^2 sin^2(k)/(1+q^2).

It vanishes in rest and is generally nonzero in motion. Assigning two
half-duration ticks preserves that rest frequency only after this duration
is supplied; it does not repair the spatial dispersion.

## 4. A local phase-space lift of the nonlinear shell

There is a positive local mathematical construction, with a precise price.
Fix m>0, r=sqrt(1+m^2), and the chart |k|<pi/2, |omega|<pi/2. Introduce

    p=sin k,       E=r sin omega,
    F2(x,t;p,E)=x asin p - t asin(E/r).

Treat (x,t;k,-omega) as extended canonical coordinates, with one-form
theta_old=k dx-omega dt. Differentiating F2 gives

    X=x/sqrt(1-p^2)=x/cos k,
    T=t/sqrt(r^2-E^2)=t/(r cos omega).

For B=F2-pX+ET, direct differentiation proves

    theta_old-(p dX-E dT)=dB.

Hence this is a local symplectomorphism of the declared extended phase
space. It preserves the symplectic two-form and carries the action with
an endpoint term; it does NOT assert kx-omega t=pX-ET.

On the positive Dirac shell cos omega=cos k/r, this reduces to

    E^2-p^2=m^2,   X=x/cos k,   T=t/cos k.

For free motion at fixed k, dX/dT=dx/dt=p/E. Thus the shell and free drift
are compatible with a canonical lift. However different momenta assign
different X,T to the same original event. It is not a common point map
of spacetime independent of the wave component. A momentum-independent
linear point map transforms covectors linearly; it cannot implement
sin k on an open interval. More generally a point map has a linear
cotangent action at each fixed base point, whereas the displayed map does
not. No quantum implementation or contact law is derived by this chart.

The chart has |p|<1. In p=m sinh eta,E=m cosh eta coordinates its range is
|eta|<asinh(1/m). At m=2 this is exactly |eta|<log phi: the proposed first
rapidity rung is the singular boundary cos k=0, where the original walk
is regular but this coordinate map diverges. Merely switching real sine
branches cannot allow |p|>1. A complete boost orbit needs a different or
enlarged reading domain and its own global compatibility rule.

## Consequence for the current search

The remaining problem is not existence of any mathematical clock. Exact
arithmetic clocks already exist. It is their joint physical admission with
the same phase, spatial reading, contact and energy law. ENERGY.md develops
the finite-step energy route while retaining these boundaries. General
nonlinear Lorentz/spacetime readings of discrete walks have prior art,
e.g. Bibeau-Delisle et al., EPL109,50003(2015), arXiv:1310.6760; no general
novelty claim is made here, and no theorem from that model is imported as
a TWIST-J physical admission.
