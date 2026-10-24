# Energy from the same step: exact construction and selection boundary

PUBLIC / NON-CANONICAL / L1 / analytical candidate-T ceiling.
Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
This exposed follow-up selects the finite-step energy-reading route as the
main next question in #1603. The unitary comparison and Hilbert carrier are
explicit premises, not a realization by the original native U. No new
scientific program or formal computation was run.

## 1. A finite-range conserved operator, not only a scalar shell

On ell2(Z,C^2) let the conditional shift have Fourier symbol
S(k)=diag(exp(ik),exp(-ik)) and let

    U_m(k)=S(k)(I+i m X)/r,       r=sqrt(1+m^2), m>0.

With standard Pauli matrices, multiplication gives

    U_m(k)=[cos k I+i K_m(k)]/r,
    K_m(k)=sin k Z + m cos k X - m sin k Y.

Equivalently, for the actual unitary operator,

    K_m=r(U_m-U_m*)/(2i).

This is self-adjoint, range one, and commutes with U_m. To fix the sign
of the energy reading, use the Fourier convention in PROPOSALS.md and
psi_t=U_m^t psi_0. The wave exp(i(kx-omega t)) belongs to the eigenvalue
exp(-i omega), where K_m has NEGATIVE eigenvalue. Define the candidate

    H_m=-K_m=r(U_m*-U_m)/(2i).

Then H_m has positive eigenvalue r sin omega on this band and the physical
group-drift sign is +omega'. The opposite temporal-phase convention would
use K_m instead. Neither sign convention is a separate physical selection.
Let P have scalar
symbol sin k on both spin components. The Pauli anticommutation identities
give the exact operator equality

    H_m^2-P^2=K_m^2-P^2=m^2 I.

Both K_m and P commute with U_m. Therefore for every square-summable
initial state and every integer t, with psi_t=U_m^t psi_0,

    <psi_t,H_m psi_t>=<psi_0,H_m psi_0>,
    <psi_t,P psi_t>=<psi_0,P psi_0>.

All operators here are bounded, so no domain qualification is hidden.
This is conservation in the declared linear unitary model. It is not yet
the funded integer bank energy or a physical energy measurement.

The connection to the SAME time evolution is also exact:

    i r(psi_(t+1)-psi_(t-1))/2=H_m psi_t.

Thus H_m is the normalized centered time-difference operator on solutions.
Together with P it yields the corresponding second-order discrete mass
shell. On the exp(-i omega) band with 0<omega<pi its eigenvalue is

    Ehat=r sin omega=sqrt(m^2+sin^2 k),
    phat=sin k,              omega'=phat/Ehat.

This constructs the algebraic energy candidate from the same step, rather
than only attaching a name to the scalar radical. The choice to interpret
this centered difference as physical energy is still an extra reading law.

H_m has both signs. A positive-band restriction needs its declared state
sector; the globally positive operator |H_m| is not thereby shown to have
finite range. Nor is a globally conserved quadratic expectation an actual
local energy-transfer apparatus. A contact and its complete account are
still required to connect this candidate to the existing integer machines.

## 2. Sine, logarithm and Cayley must not be conflated

With the time convention above, the centered sine reading is
H_m=r sin(H_log) on the branch U_m=exp(-i H_log), H_log=i log U_m. Its band values are
not omega. For m>0 the principal logarithm is well-defined because the
bands stay away from -1, but this does not give a finite-range logarithm.

The geometric Cayley transform with the sign in the proposal is instead

    H_C=-i(U_m-I)(U_m+I)^-1,
    U_m=(I+iH_C)(I-iH_C)^-1.

Its eigenvalues are +/- tan(omega/2), not r sin omega or tan omega;
on the exp(-i omega) band the value is NEGATIVE tan(omega/2).
For this walk,

    H_C(k)=K_m(k)/(r+cos k).

The positive-energy-sign Cayley reading for the adopted time convention
is -H_C=H_m/(r+cos k). This inverse generally has infinite spatial range.
The expression in the
proposal (U-U*)/(2i cos omega0) equals K_m since cos omega0=1/r; it is a
normalized SINE transform, not the Cayley transform. Their shared commutation
with U does not make them the same energy observable.

## 3. Conservation still leaves a concrete family

For every real a>=0 define

    H_(m,a)=H_m(I+a P^4).

It is self-adjoint, finite range, commutes with U_m, and has positive-band
eigenvalue

    E_a(k)=sqrt(m^2+sin^2 k)(1+a sin^4 k).

Every member has E_a(0)=m and E_a''(0)=1/m; its massless positive-band
right-hand slope at k=0 is one. The choices nevertheless differ away from rest.
For algebraic m,a, all Laurent coefficients are algebraic as well.
Thus conservation, finite range, rest energy, local curvature and massless
speed do not select H_m. Choosing the exact shell with the already fixed
P, or choosing exactly the centered time difference, can select it within
this comparison, but then that condition itself needs justification.

This is not a claim that EVERY physical admissibility class is nonunique.
It identifies alternatives under the listed tests only. A subsequent
native contact/reading contract must state which of them it admits and why.

## 4. Corrected transcendence lemma

The owner proposed a useful general obstruction. Algebraicity of U(0)
alone is insufficient. A sufficient local hypothesis is algebraicity of
the three matrices U(0),U'(0),U''(0), together with a simple eigenvalue at
zero and a twice differentiable eigenphase. In particular it holds for a
finite-dimensional finite-range unitary Laurent matrix

    U(k)=sum_(j=-R)^R A_j exp(ijk)

whose EVERY coefficient A_j is algebraic. Finite range alone does not
imply a dispersion of the special form cos omega=P(cos k).

Assume a local eigenvalue lambda(k)=exp(i omega(k)), simple at zero,
with omega0!=0 and omega''(0)!=0. Write q(lambda,k)=det(lambda I-U(k)).
The eigenvalue lambda0 is algebraic, and q_lambda(lambda0,0)!=0.
Implicit differentiation gives

    lambda'=-q_k/q_lambda,
    lambda''=-(q_kk+2q_(lambda k)lambda'
                  +q_(lambda lambda)(lambda')^2)/q_lambda

at zero. All terms are algebraic under the local hypotheses. Consequently

    omega''(0)=-i[lambda''/lambda-(lambda'/lambda)^2]_(k=0)

is algebraic. Hermite-Lindemann says that exp(alpha) is transcendental for
nonzero algebraic alpha. Applied contrapositively to exp(i omega0)=lambda0,
it proves that omega0 is transcendental. Hence

    omega0 omega''(0) is transcendental, in particular it is not1.

The imported theorem is explicitly available with proof in J.-H. Evertse,
*Transcendence results*, Section4.2, Theorem4.9 and Corollary4.10(i),
[Leiden lecture notes](https://pub.math.leidenuniv.nl/~evertsejh/dio14-4.pdf).
No external source code or dataset is imported. The local derivative
argument above is the application; the transcendence theorem is not
claimed as a new TWIST-J result.

For rest require omega'(0)=0 as well. With the fixed literal readings
E=A omega, p=B k and the common speed calibration c=A/B,

    M_curv=B^2/(A omega''(0)),
    M_curv c^2=E0  iff  omega0 omega''(0)=1.

Thus the equality is impossible under these hypotheses. Arbitrary common
positive A,B cancel; their algebraicity is unnecessary. If a separately
fixed reference slope v defines c=Av/B, the target is v^2 instead of1 and
is excluded whenever v^2 is algebraic. The energy origin must remain the
declared one. A freely chosen additive energy offset is outside the claim.
Every nonzero real phase lift of the same algebraic eigenvalue is covered.
Zero phase, zero curvature, band degeneracy, nonalgebraic derivative data,
different readings and additional limits are not covered by this lemma.

For the special two-band relation cos omega=P(cos k), with polynomial
P in Qbar[x], P'(1)!=0 and sin omega0!=0, differentiation gives
omega''(0)=P'(1)/sin omega0 and recovers the proposed special case.
The Dirac family for algebraic m>0 (including m=2), and both algebraically
specified scale families satisfy the strengthened assumptions at rest.

## 5. Why the weaker lemma is actually false

Let C_alpha=exp(i alpha X), theta=asin(1/pi)/2, and

    V(k)=S(k) C_theta S(k) C_(pi/2-theta).

This is a unitary Laurent matrix of range two, with algebraic V(0)=iX.
Direct multiplication yields

    cos omega(k)=(cos(2k)-1)/(2pi)=-sin^2(k)/pi,
    omega0=pi/2,       omega''(0)=2/pi,
    omega0 omega''(0)=1.

Its eigenvalues are simple since cos omega stays in [-1/pi,0]. It even
has the requested form P(cos k)=(cos^2 k-1)/pi, but P does not have
algebraic coefficients.
This refutes the original claim based on algebraic rest entries alone.
It is a mathematical counterexample, not a proposed physical model or a
new calibrated massless branch. The clock scales can be set to1.

## 6. What is now concrete, and what remains open

The finite-step route has a specific operator H_m (with K_m=-H_m), exact state evolution,
mass shell, conserved quadratic quantity and centered difference equation.
Its competitors and the distinction from Cayley/logarithm are explicit.
The next necessary input is an admitted complete contact and reading
family that selects this energy, relates it to actual source/receiver
changes, and supplies inertia using the same time/space convention.

The transcendence lemma does not force the particular Lucas sequence,
an n->infinity mechanism, or a unique alternative algebraic energy.
It rules out the frozen conjunction of assumptions. The Lucas family is
one useful conditional limit; a common native refinement is still absent.
Nor does algebraic normalization alone supply a frequency, a spatial
intertwiner, physical energy conservation or a return period L_n.

## 7. Preserve the finite mismatch as a physical hypothesis

The owner's further proposal is to retain, rather than remove, the exact
finite-step difference. This is an admissible research direction. Agreement
with a continuous relativistic dispersion is one possible target, not a
logical prerequisite for studying the given discrete law.

For the original literal phase reading and common c=A/B, define

    R(m)=M_curv c^2/E_phase(0)=m/atan(m)>1,
    Delta(m)=M_curv c^2-E_phase(0)=A[m-atan(m)].

These are exact mathematical consequences already established in PROOF.md.
For all m>0,

    m-atan(m)=integral_0^m s^2/(1+s^2) ds >0.

The power series m^3/3-m^5/5+... is valid for |m|<1 (and converges at1);
it must not be used as a convergent expansion at m=2. R extends to1 at
m=0 and increases continuously for m>0. A separately selected discrete
parameter set may sample it; the function itself is not quantized.

**Hypothesis, not admitted physical law:** if an independently calibrated
physical clock measures E_phase=A omega, and a declared source/contact
causes an inertial response equal to this curvature mass, then their ratio
is R(m), not1. The difference can be a persistent relation between two
readings. This proposal is not rejected merely because R differs from1.
Neither mass identification is already established by the free dispersion.

What does not follow is an entropy production, heat loss or payment on each
tick. For the complete linear walk on the infinite lattice (or a periodic
lattice),

    D_m*=r U_m*,   D_m* D_m=r^2 I,
    D_m^t=r^t U_m^t,          ||U_m^t psi||=||psi||.

The raw norm factor is state-independent and can be removed once per step
without losing the normalized state. Replacing D_m by s D_m, s>0, leaves
the same normalized U_m but changes that raw growth factor. Thus growth
of the unnormalized norm alone cannot specify a physical energy debit.
Its logarithmic growth log r=log(1+m^2)/2 is also a different function
from m-atan(m): near zero their leading orders are m^2/2 and m^3/3.
For a density operator, U rho U* has the same spectrum and von Neumann
entropy as rho. No energy reservoir, dissipation or irreversible erasure
has been specified here. A reduced subsystem can behave differently only
after its coupling and discarded degrees of freedom are declared.

The topological/Haar entropy of the DIFFERENT toral map M_J is exactly
2 log phi, with log phi the positive expansion exponent on each of its
two expanding real directions. This dynamical entropy is compatible with
invertibility. It is not already thermodynamic entropy production per
Dirac tick or energy dissipated by a clock. No common carrier or conversion
law equating these quantities has been proved.

The geometric rest-coin picture is exact: (1,m) has angle atan(m), tangent
coordinate m and radius sqrt(1+m^2). That picture does not force a physical
trajectory along the tangent or assign work to its length. A discrete
unitary is itself an exact finite rotation. Similarly,

    atan(m)+atan(1/m)=pi/2,
    U_m(0) U_(1/m)(0)=iX

hold for EVERY m>0, not just2. The m=2 and1/2 pair has the existing
golden-rapidity specializations, but the reciprocal identity alone does
not select that pair or a universal quantum of time cost.

Finally m=0 is the massless shift, not the vacuum: nonzero states and
finite packets still propagate. In an independently supplied Lorentzian
geometry null curves have zero proper time and no rest frame; a rest
clock of the photon is not defined. This does not equate a massless state
with absence of matter/information, and no such geometry is derived here.

The useful next test keeps R(m) finite and asks for the actual contact
response, phase-clock reading and complete energy balance. If a per-tick
cost is claimed in addition, it must identify which record/reservoir changes
after N free ticks and derive its N-dependence. The present free unitary
model supplies no such debit; Delta(m) is a fixed difference of readings,
not an accumulated loss. A positive result for the persistent mismatch
would still be meaningful without an entropy-cost interpretation.
