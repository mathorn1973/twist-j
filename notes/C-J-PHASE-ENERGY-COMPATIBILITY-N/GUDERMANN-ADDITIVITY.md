# Gudermann bridge, additive energy and locality

PUBLIC / NON-CANONICAL / L1 / analytical candidate-T ceiling.
Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
Exposed continuation of #1603, 2026-10-18 Europe/Prague.
The owner supplied this interpretation after publication of the preceding
analytical addendum. No blind prediction or new scientific execution is
claimed. PROPOSALS.md and ENERGY.md supply the step and sign conventions.

## 1. The complementary Gudermann angle and the exact golden factor

For integer n>=1, let eta=n log(phi)>0 and set q=exp(-eta), m=csch(eta),
and theta=atan(q).
Then 0<theta<pi/4 and

    m=2q/(1-q^2),
    omega0=atan(m)=2theta=pi/2-gd(eta),
    cos(omega0)=tanh(eta),   sin(omega0)=sech(eta).

The standard Gudermann identity is gd(eta)=atan(sinh(eta)); see
[NIST DLMF 4.23.40](https://dlmf.nist.gov/4.23.E40).
The angle here is its complement. The equality atan(m)=2atan(q) needs no
branch correction because both sides lie in (0,pi/2).

Write I(x)=x/atan(x) for the inertia/frequency ratio. This is the reciprocal
of the centered-phase invariant R used in CLOCKS.md; ENERGY.md section7
calls the inertia ratio R. Here I avoids that local notation collision.
Direct substitution proves

    I(m)/I(q) = 1/(1-q^2).

At n=1, q=phi^-1 and 1-q^2=q, hence

    I(2)=phi I(phi^-1).

This exact factor strengthens the rest-coin bridge. It does not identify
the two complete spatial walks or show that their curvature masses are
related by regrouping identical physical ticks. PROPOSALS.md and CLOCKS.md
give the explicit spatial discrepancy and the restricted blocking proof.

The same factor quantifies that discrepancy near rest. In the comparison
Omega_block(k)=2 omega_q(k/2), which preserves the massless reference
slope, omega_x''(0)=1/x implies

    Omega_block(0)=omega_m(0),
    Omega_block''(0)/omega_m''(0)=m/(2q)=1/(1-q^2).

Thus at n=1 the rest phases agree while the curvatures differ by phi.
This is a relation between declared dispersions, not a physical clock
construction or an identified force-response mass.

The calculation starts with q in Z[phi], since phi is a unit. Its division
is valid in Q(sqrt5), not necessarily inside Z[phi]: already n=3 gives
m=1/2, which is not an algebraic integer. The polynomial identity
(1-q^2)m=2q can be cleared of denominators. For odd n, m=2/L_n, exactly
as in PROPOSALS.md. The phase angle itself is not an element of that
number field; nor does this argument put the normalized half-coin there.

There is nevertheless an exact ring-level statement at the basic lock:
for q=phi^-1,

    (I+iqX)^2=q(I+2iX),       1+q^2=sqrt5 q.

The first identity is over Z[phi,i]. Dividing by the positive
normalizations gives U_q(0)^2=U_2(0), as previously established.

The minus sign in 2q/(1-q^2) describes addition of circular phases. It
is not Einstein velocity addition, whose dimensionless denominator is
1+beta1 beta2. In these variables doubling rapidity eta instead gives
q -> q^2 and m -> m^2/(2 sqrt(1+m^2)). Thus doubling the rest angle and
doubling rapidity are different operations.

## 2. What conservation and tensor composition actually give

For a declared self-adjoint phase lift Omega with U=exp(-i Omega), every
bounded real Borel function f gives a self-adjoint conserved f(Omega).
Unbounded functions require their spectral domains to be specified.
This functional family is contained in the commutant of U; degeneracies
can make the full commutant larger. Conservation alone does not select f.

If U_AB=U_A tensor U_B and real phase lifts Omega_A,Omega_B are chosen,
the commuting operator

    Omega_sum=Omega_A tensor I+I tensor Omega_B

satisfies exp(-i Omega_sum)=U_AB. It need not equal the principal logarithm
i log(U_AB): eigenphases of U_AB retain sums only modulo 2pi. On a chosen
sector where every chosen phase sum lies in (-pi,pi), the principal
equality holds.

There is a precise conditional linearity result. Suppose a universal
continuous real function f on the real phase lift is used for every
subsystem AND their composite, with a fixed zero, and require

    f(x+y)=f(x)+f(y)     for all real x,y.

Then f(0)=0; integer and rational scaling give f(r)=r f(1), and continuity
extends this to f(x)=a x for every real x. A positive energy calibration
adds a>0. Continuity can be replaced by other regularity conditions, but
it cannot simply be omitted. A finite set of spectral values does not
by itself supply this universal Cauchy equation.

If f is required also to depend only on exp(-ix), it is 2pi-periodic.
The linear conclusion then forces a=0. Equivalently, a continuous real
additive energy cannot be a nonzero single-valued global function of the
phase circle under multiplication. A nonzero additive phase energy needs
extra phase-lift information, a restricted no-alias domain, or a different
composition contract. A one-step unitary alone supplies none of these.

For an explicit alias with no eigenvalue on the logarithm's cut, choose
Omega_A=Omega_B=diag(pi/4,-3pi/4). Their unitaries have algebraic entries,
and

    U_AB=diag(-i,i,i,-i),
    Omega_sum=diag(pi/2,-pi/2,-pi/2,-3pi/2).

Omega_sum commutes with U_AB and exponentiates to it, but is not a scalar
spectral function of U_AB: the same eigenvalue -i carries two different
energies. This is already a finite-dimensional obstruction to reconstructing
the additive lift from the total unitary's eigenvalue alone.

## 3. Additive local energies are not excluded

Given ANY bounded self-adjoint conserved H_A,H_B on the separate systems,
define

    H_AB=H_A tensor I+I tensor H_B.

It is additive by construction and commutes with U_A tensor U_B. This
also applies to the local sine candidates of ENERGY.md. With declared
subsystem structure, locality of these separate terms is preserved.
Generally H_AB differs from applying the SAME sine function to Omega_sum.
Thus extensivity alone does not force each H_A to be the logarithm of U_A.
That conclusion additionally requires the universal phase-only composition
law in section2, or a generator/physical-contact principle of comparable
strength. There is no general impossibility of local AND additive energy.

## 4. Locality must name the space and the allowed operations

For the finite-range walk U_m, H_m=r(U_m*-U_m)/(2i) has spatial range one.
Finite Laurent polynomials in U and U* have finite spatial range. Many
such conserved operators exist; finite range and algebraic coefficients
alone do not single out sine. ENERGY.md section3 even supplies alternatives
with the same rest energy, curvature and massless reference slope.

The Cayley expression contains an inverse, (I+U)^-1. A short formula in U
is not a finite-range rule. For this walk its symbol has denominator
r+cos(k), and its spatial range is infinite for m>0: the X coefficient
m cos(k)/(r+cos(k)) has poles at complex cos(k)=-r and cannot be a finite
Laurent polynomial. The inverse exists on the physical spectrum here,
but that does not remove its spatial tails. A tan(Omega) reader also needs
care at its poles; the Dirac bands contain omega=pi/2.

The principal logarithm is an instantaneous operator on the state at a
chosen time. Its generally infinite spatial range, or an infinite series
in U, is not by itself a theorem that it depends on the state's temporal
history. An onsite unitary can even have an onsite logarithm. Conversely,
the centered sine equation uses neighboring time slices on solutions.
Temporal stencil, spatial range, spectral algebraicity and dependence on
past states are distinct properties and must be tested separately.

## 5. Research consequence

The exact golden multiplier and complementary Gudermann identity stand.
They do not require sending m to zero. The finite inertia/frequency
mismatch remains a physical hypothesis at the scope stated in ENERGY.md.

A concrete selection test must now specify the complete composite state,
whether a phase winding/branch record is present, how noninteracting
systems combine, the allowed spatial range, and the energy exchanged by a
contact. Those data can distinguish additive unwrapped phase energy from
an additive sum of local algebraic energies. Neither selection follows
from discreteness, conservation, or algebraic closure alone.
