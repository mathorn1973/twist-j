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

## 5. Band-diagonal displacement and the cosine factor

The owner's further identity is exact after specifying the band-diagonal
projection. Put N(k)=H(k)/E(k), so N^2=I, Pi_s=(I+sN)/2 and
U Pi_s=exp(-is omega)Pi_s. Thus Omega=omega N is the principal phase
generator. For D(A)=sum_s Pi_s A Pi_s, differentiating the eigenvalue
equation and N^2=I gives

    D(V_step)=omega' N,
    D(-i[x,H])=D(H')=E' N=cos(k) D(V_step),
    D(-i[x,Omega])=omega' N.

These are band-diagonal identities, not equality of the full operators.
In particular H'(pi/2)=mX is nonzero and purely interband, although its
band-diagonal part vanishes. The band expectations have opposite signs
for pi/2<|k|<pi; at k=+/-pi the group velocity itself is zero.
For m=2,k=pi/2 the two actual band velocities are +/-1/sqrt5, whereas
both band expectations of H' vanish.

This projection also has a precise time-average meaning. For m>0,
|1-exp(2i omega)|=2E/r>=2m/r. Hence for bounded fiberwise A,

    D_N(A)=(1/N) sum_(t=0)^(N-1) U^(-t) A U^t,
    ||D_N(A)-D(A)|| <= r/(mN) ||A-D(A)||.

The bound follows by summing the two interband geometric series. For
A=V_step, D_N(A)=(U^(-N)xU^N-x)/N. Thus it is the actual mean displacement
per step. Instantaneous interband oscillations remain; no decoherence or
finite-period disappearance is inferred. The uniform bound does not
extend to the degenerate massless case by setting m=0.

There is a conditional uniqueness statement. Let G(k) be a smooth
self-adjoint reader commuting with U, so G=sum_s g_s(k)Pi_s. Matching
D(-i[x,G]) to D(V_step) for every k on a connected domain gives
g_s'=s omega', hence precisely

    G=Omega+C_+ Pi_+ + C_- Pi_-.

Band constants are not selected by velocity. Requiring exp(-iG)=U further
restricts them to 2pi integers; the principal spectral branch then sets
them to zero. Conservation, differentiability, the all-k requirement and
the original position are premises of this result. It is not an unrestricted
physical selection theorem or equality of full instantaneous commutators.

## 6. Joint conservation: local rank and positive-band rigidity

Allow masses m_A,m_B>0 and r_i=sqrt(1+m_i^2). For locally lifted signed
phases theta_i=s_i omega_i define S=theta_A+theta_B and
T=r_A sin(theta_A)+r_B sin(theta_B). In phase coordinates,

    det d(S,T)/d(theta_A,theta_B)
      =r_B cos(theta_B)-r_A cos(theta_A)=cos(k_B)-cos(k_A).

Therefore a nonzero first-order phase-exchange vector exists exactly
when the cosines agree. In momentum coordinates, with v_i=theta_i',

    det d(S,T)/d(k_A,k_B)=v_A v_B [cos(k_B)-cos(k_A)].

The equal-cosine criterion as a regular k-coordinate statement needs
v_A v_B!=0. Turning points also make that Jacobian singular. Moreover,
singularity is only a first-order condition: it does not prove a curve
of jointly conserved states or a nonzero transition amplitude. At fixed
S, the second derivative of T with respect to theta_A is -T. A stationary
point with T>0 is therefore a strict maximum, not a freely moving channel.

For EQUAL masses and TWO POSITIVE bands let a=atan(m). Then
omega_A,omega_B lie in [a,pi-a], so S lies in
[2a,2pi-2a], strictly inside (0,2pi). Modular conservation of S fixes its
real lift uniquely on this sector. With delta=(omega_A-omega_B)/2,

    T=2r sin(S/2) cos(delta),       |delta|<=pi/2-a<pi/2.

Since sin(S/2)>0 and cos(delta) is strictly decreasing in |delta| on this
interval, fixed S,T determine |delta| and thus the unordered frequency
pair {omega_A,omega_B}. This is an exact two-positive-band rigidity result.
It does not eliminate dynamics: labeled subsystem energies may exchange,
and momentum signs and scattering phases remain possible. The individual
momentum freedom at fixed frequency is k -> -k modulo 2pi. In contrast,
k -> pi-k changes omega -> pi-omega and is not an unrestricted symmetry
of both conserved totals.

## 7. The complete signed-phase exception

For fixed S modulo 2pi, eliminate theta_B=S-theta_A modulo 2pi:

    T=(r_A-r_B cos S) sin(theta_A)+r_B sin S cos(theta_A),
    R^2=r_A^2+r_B^2-2r_A r_B cos S.

If R>0, the circle equation has zero, one or two solutions according as
|T|>R, |T|=R or |T|<R. Keep only the solutions lying in each declared
signed band, including its momentum domain. This classification is a
kinematic constraint, not a construction of a coupling realizing it.

R=0 occurs exactly for equal masses and S=0 modulo 2pi. Then the equation
requires T=0 and permits the whole admissible opposite-band family
(theta,-theta). Thus the preceding positive-band theorem cannot be
extended to the complete two-spin carrier as a general freezing theorem.
On a finite ring, quantized momenta leave discrete alternatives rather
than a continuous family. There is still no general uniqueness of the
frequency pair on that full carrier.

## 8. A fixed weak interaction need not conserve the old free phase

The time-independent recurrence U_g=exp(-igV)U0 exists for every bounded
self-adjoint V. The extra requirement [V,U0]=0 is not a consequence of
using the same step at each tick. Requiring both [V,U0]=0 and [V,H0]=0
defines a narrower class than autonomous energy-preserving interactions.

A finite exact example, with a common r>0, is

    Omega_A=diag(pi/6,pi/2),   Omega_B=diag(pi/2,5pi/6),
    U_i=exp(-i Omega_i),       H_i=r sin(Omega_i),
    V=|00><11|+|11><00|.

In the ordered product basis,

    H0=diag(3r/2,r,2r,3r/2),
    U0=diag(exp(-2pi i/3),-1,-1,exp(-4pi i/3)).

Thus [V,H0]=0 but [V,U0]!=0. Every U_g preserves H0, while an arbitrarily
small nonzero generic g mixes |00> and |11>, exchanging subsystem energies
by r/2 and changing their free phase sum. The free unitary entries are
algebraic. Choosing m=1/sqrt3 and r=2/sqrt3 realizes these phase levels
at Dirac momenta 0,pi/2,pi. This mode-selective coupling is not thereby a
spatially local or native contact. It refutes the claimed general
impossibility of an autonomous weak perturbation, not a separately posed
local-contact obstruction.

Finite-time transition and asymptotic scattering are distinct. If the
relevant wave operators exist and intertwine interacting and free steps,
the scattering operator can commute with U0 although V does not. This
standard distinction and modulo-2pi quasienergy conservation are stated
in Bisio, Mosco and Perinotti, *Scattering and perturbation theory for
discrete-time dynamics*, equations (3)–(5) and (12),
[arXiv:1912.09768v2](https://arxiv.org/abs/1912.09768v2), published as
Phys. Rev. Lett. 126, 250503 (2021). No asymptotic scattering theorem is
asserted for the finite ring merely from its one-step contact amplitude.
