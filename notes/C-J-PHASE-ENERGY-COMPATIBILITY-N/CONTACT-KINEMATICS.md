# Exact displacement and a local resonant contact test

PUBLIC / NON-CANONICAL / L1 / analytical candidate-T ceiling.
Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
Exposed continuation of #1603, 2026-10-18 Europe/Prague.
This note answers the owner's subsequent group-velocity/contact proposal.
All calculations below are analytical. No scientific program was run.
The Hilbert-space walk and contact are declared comparison models, not
admitted realizations of native U or of a physical interaction.

## 1. The scalar velocity identity is exact; its canonical meaning is local

Use ENERGY.md's U_m(k)=S(k)C, C=(I+imX)/r, r=sqrt(1+m^2), m>0,
and H=r(U*-U)/(2i). On the positive H band, Uu=exp(-i omega)u and

    cos(omega)=cos(k)/r,       0<omega<pi,
    E(k)=sqrt(m^2+sin^2(k)),   p(k)=sin(k),
    omega'(k)=p/E,            d sqrt(m^2+p^2)/dp=p/E.

The scalar equality holds over the full band. At k=+/-pi/2 the quotient
(dE/dk)/(dp/dk) is 0/0, but the derivative of the function E(p) has a
continuous extension, one-sided at p=+/-1 in the physical p interval.
The map is not globally invertible: k and pi-k modulo 2pi give the same
(p,E), with phase angles omega and pi-omega. Branch information is lost.

For Fourier convention psi_hat(k)=sum_x exp(-ikx)psi_x, position is
x=i partial_k. On its natural differentiable domain, the EXACT displacement
operator for one step is

    V_step=U* x U-x=i U* partial_k U=-C* Z C
          =[(m^2-1)Z+2mY]/(1+m^2).

It extends to a bounded operator with V_step^2=I. For the positive-band
projector Pi+=(I+H/E)/2, differentiation of Uu=exp(-i omega)u gives

    Pi+ V_step Pi+=(p/E) Pi+.

Thus group drift is exactly the band expectation of actual displacement.
For a packet in that band, its mean displacement is the spectral average
of p/E; replacing it by the central-mode value needs a narrow packet.
Superpositions of both bands need not have that single-band drift.

The same original position obeys [x,P]=i cos(k), for P=sin(k)I.
Consequently P is not the canonical momentum conjugate to unchanged x.
On smooth functions supported within one branch away from cos(k)=0,

    X_p=(sec(k)x+x sec(k))/2,       [X_p,P]=i.

This is a symmetric local expression, not a proved global self-adjoint
position operator. It is singular at branch boundaries. CLOCKS.md section4
also shows that preserving the full phase-space form changes both the
position and time coordinates. The scalar slope identity therefore does
not make H the generator of the original step or P the generator of the
original spatial translations. With those original coordinates, dE/dk
equals cos(k) omega'(k), as the owner correctly calculated.

## 2. Two additional algebraic qualifications

Finite Laurent polynomials in U,U* with scalar constant coefficients are
conserved and have finite spatial range. They are not ALL such operators.
P=sin(k)I is an explicit counterexample: it commutes with U and has range
one. The trace of any scalar Laurent polynomial f(U(k)) is even in k,
since the eigenvalue pair of U depends only on cos(k). But tr(P)=2sin(k)
is odd and nonzero, so P cannot equal such an f(U).

For U=exp(-i Omega), the positive Cayley sign is
i(U-I)(U+I)^-1=tan(Omega/2); i(I-U)(I+U)^-1 has the opposite sign.
Its infinite spatial range for this walk is proved in
GUDERMANN-ADDITIVITY.md. Also H's MATRIX coefficients require i:
for algebraic m they are in Q(m,i)[z,z^-1]. At m=2 they are already in
Q(i)[z,z^-1]. Its arbitrary real-k entries are not numbers in Q(sqrt5).
The mass-shell identity is an operator identity H^2-P^2=m^2 I; it remains
exact without confusing coefficient fields with all evaluated entries.

The eigenvalue-addition statement on a product vector requires subsystem
energy eigenvectors. For general product or entangled states the tensor
sum still gives additive EXPECTATIONS via the two reduced density matrices.

## 3. A coupling criterion, not a claim about every nonzero interaction

Let U0=U_A tensor U_B and H0=H_A tensor I+I tensor H_B with [H0,U0]=0.
For a bounded self-adjoint coupling V define the period-one kicked step

    U_g=exp(-igV) U0.

Then conservation of this particular free energy is equivalent to

    U_g* H0 U_g=H0  iff  exp(igV) H0 exp(-igV)=H0.

It holds for all g in a neighborhood of zero iff [V,H0]=0. Nonzero
couplings can satisfy this condition; for example V=H_A tensor H_B for
bounded subsystem energies. Thus weakness or periodicity alone never
proves that sine energy is lost. A given coupling must be checked.

For free modes a,b, the first-order transition amplitude over N steps
contains V_ba times sum_(t=0)^(N-1) exp(i t(omega_b-omega_a)). Linear-in-N
resonant accumulation requires omega_b-omega_a=0 modulo 2pi and V_ba!=0.
Finite-time off-resonant amplitudes are not identically zero. This
perturbative statement does not identify a physical energy reservoir,
nor the free H0 with a conserved energy of the interacting machine.

On a finite carrier, conservation for EVERY Hermitian resonant V satisfying
[V,U0]=0 would require H0 to be scalar on each U0 eigenspace: within each
such block V can be any Hermitian matrix, whose full commutant consists
only of scalars. The converse also holds. This broad condition selects a
scalar function of U0, not a unique unwrapped phase. The additive phase
lift can itself fail through 2pi aliasing, as in GUDERMANN-ADDITIVITY.md.
If only particular local contacts are admitted, their actual allowed
matrix elements, rather than this unrestricted block algebra, decide
which additional quantities survive.

## 4. An explicit onsite contact fails the sine-energy test

Take TWO DISTINGUISHABLE copies of the same Dirac walk on a periodic ring
of L sites, with L divisible by4, and the complete two-spin carrier. Let

    V=sum_x |x,x><x,x| tensor I_spin.

This is the projector onto coincident positions: a translation-invariant
onsite contact, with no spatial tail. Let a=atan(m), and use positive-band
normalized momentum modes. Consider the two orthogonal product states

| State | Momenta (k_A,k_B) | Phases (omega_A,omega_B) | H0 energy |
|---|---|---|---|
| in | (0,pi) | (a,pi-a) | 2m |
| out | (pi/2,pi/2) | (pi/2,pi/2) | 2r |

Both total momenta are pi and both total phase angles are pi. Thus both
are eigenvectors of U0 with eigenvalue -1, even though 2r>2m.
At k=0 the spin is |-x>, at k=pi it is |+x>. At k=pi/2 the positive-band
spin w satisfies (Z-mY)w=-r w; its Bloch x component is zero. Therefore

    |<w|-x>|=|<w|+x>|=1/sqrt2,
    |<out|V|in>|=1/(2L),
    |<out|[V,H0]|in>|=(r-m)/L >0.

The factor 1/L follows directly by summing normalized plane waves over
the coincident sites; their total momenta agree. This is a nonzero
resonant matrix element of a strictly local contact, not an unspecified
selection rule or numerical observation.

Since V^2=V, exp(-igV)=I+(exp(-ig)-1)V. Hence [U_g,H0]!=0 for EVERY
g not in 2pi Z, including arbitrarily small nonzero g. In fact the exact
one-step probability for this particular in-to-out transition is

    |<out|U_g|in>|^2=sin^2(g/2)/L^2.

The operator conservation defect and transition amplitude begin at first
order in g. An initial H0 eigenstate has no first-order change of the
H0 expectation; transition probabilities begin at second order. No
linear-in-g energy loss is inferred.

This contact is a concrete conditional discriminator: the free sine
sum is not its conserved interacting energy. It does not prove that
every local contact fails or that phase is the unique physical energy.
The model does not assume an identical-fermion sector or a closed
positive-band sector under contact. Native admissibility, the complete
source/receiver account and a force-response interpretation remain open.
