# Exact scattering of the unchanged contact walk at P=0

Author: A. M. Thorn
Date: 2026-10-30
Candidate: C-W-P0-SCATTERING-N
Owner: ChatGPT-W-P0-scattering-20261030; issue #1840
Status: NON-CANONICAL / L1 / analytical candidate-T.

## 0. Exact source, conventions and scope

Use precisely CONTACT-W-SPECTRAL-READING and
CONTACT-W-BOUND-PAIR-RESPONSE from Public Canon v106, main
 a193e389fb1ddb0bdc89165b015c95a17eb1e425.
The carrier in this note is the existing P=0 relative fibre
ell2(Z_r) tensor C4, coin order (++,+-,-+,--), with

    G=((I+2iX) tensor (I+2iX))/5,
    F(q)=diag(1,exp(iq),exp(-iq),1) G,
    W=Gamma F,    Gamma_r=kappa_r I4,
    kappa_0=gamma=exp(-ig), kappa_r=1 for r!=0,
    g=2pi/5.

The Fourier convention is sum_r exp(-iqr) psi_r; thus the +- channel
streams from r+1 to r and the -+ channel from r-1 to r. P=0 is a fixed
fibre, not a normalizable full center-momentum preparation. The four
coin channels and all lattice sites are retained. There is no new
fermionic projection, particle species, interaction or Born occurrence law.

Existing point-contact quantum walks and their scattering/bound states
are established literature; see Ahlbrecht et al., arXiv:1105.1051, and
Bisio et al., arXiv:1804.08508. Their different coins/statistics/contacts
are not imported as this calculation. The proof below derives the
specific scattering matrix of the already declared W directly.
Issue #1796 concerns a DIFFERENT massless/massive port-direct-sum walk.
The capture apparatus of #1812 has an extra carrier; neither is reused.

The user reported finite-packet floating-point reflections in chat. The
named BUILD-MALY-VESMIR project file and its scripts were not retrieved
by the available file search. Those values are comparison motivation,
not accepted input evidence or independently reproduced packet data.

## 1. Remove the output contact phase without changing asymptotes

The diagonal Gamma commutes with the onsite coin G. Therefore

    W'=Gamma^-1 W Gamma = S_stream Gamma G.              (1)

Conjugation is the identity off r=0, so asymptotic scattering amplitudes
are unchanged. If W' chi=lambda chi, the original state is psi=Gamma chi.
We will also substitute the resulting states directly into W.

The inherited A=(|++>-|-->)/sqrt2 channel is invariant and F acts as the
identity there. For a propagating spectral parameter lambda!=1,gamma,
its component is zero. In the symmetric complement write

    chi_r=(u_r,L_r,R_r,u_r).

The stationary component of the eigenvalue equation gives

    u_r=2i kappa_r (L_r+R_r)/(5lambda+3kappa_r).          (2)

For unit-modulus lambda,kappa the denominator cannot vanish. Eliminating
u in the two moving coin outputs gives

    a_kappa=kappa(lambda-kappa)/(5lambda+3kappa),
    b_kappa=-4kappa(lambda+kappa)/(5lambda+3kappa).        (3)

The equations on the bonds become

    lambda L_(r-1)=a_kappa_r L_r+b_kappa_r R_r,
    lambda R_(r+1)=b_kappa_r L_r+a_kappa_r R_r.

Consequently for v_r=(L_(r-1),R_r)^T,

    v_(r+1)=T_kappa_r(lambda) v_r,

    T_kappa(lambda)=
      [[lambda/a_kappa, -b_kappa/a_kappa],
       [b_kappa/a_kappa,(a_kappa^2-b_kappa^2)/(lambda a_kappa)]]. (4)

Equivalently

    T_kappa(lambda)=T(lambda/kappa),
    T(rho)=1/(rho-1) *
      [[rho(5rho+3), 4(rho+1)],
       [-4(rho+1), (-3rho-5)/rho]].                     (5)

Every displayed step is reversible for lambda!=kappa. For the fixed
gamma in a free gap, lambda=kappa never occurs in the open propagating
bands studied below. Direct multiplication proves

    det T(rho)=1,
    T(rho)^* J T(rho)=J,    J=diag(-1,1), |rho|=1.      (6)

The conserved stationary flux is |R_r|^2-|L_(r-1)|^2.
This is also the actual discrete walk current across the cut. Equality
follows either from the local unitary probability balance before
elimination or from the two displayed moving-channel equations.

## 2. Free modes and a flux-normalized scattering basis

Take 0<q<pi and define theta by

    cos(theta)=(cos(q)-4)/5,
    2atan(2)<theta<pi,    lambda=exp(i theta).            (7)

Let

    s=sin(q)>0,   zeta=exp(iq),
    b0=4cot(theta/2),
    a0=b0(1-5cos(theta))/4.

Then a0,b0>0, a0^2-b0^2=s^2, and

    T(lambda)=[[cos(q)+i a0, -i b0],
               [i b0, cos(q)-i a0]].                  (8)

Define H=a0+s and the real mode matrix

    V=[[b0,H],[H,b0]],    D=diag(zeta^-1,zeta).

One checks

    T(lambda) V=V D,
    V^* J V=2sH diag(1,-1).                            (9)

Thus the columns have equal and opposite flux. The common normalization
sqrt(2sH) cancels from every scattering coefficient. For W^n, eigenvalue
exp(i theta) and spatial factor exp(iqr), the group speed is -dtheta/dq.
The first column, spatial factor exp(-iqr), travels right; the second
travels left. This names incoming and outgoing modes without guessing a
sign from a packet simulation.

The other flat eigenvalue 1 in the symmetric sector is excluded by the
open-band energy, not discarded from the model. Eliminating u and solving
the two eigenvalues zeta,zeta^-1 of the transfer covers the full stationary
propagating solution space at this lambda. There is no third open channel.

## 3. Complete S matrix, including phases [candidate-T]

Let delta=theta+g and put

    C=5cos(delta)+4,
    b1=4cot(delta/2),
    a1=b1(1-5cos(delta))/4,
    Y=a0 b1-b0 a1,
    Z=a0 a1-b0 b1,
    Dsc=s C+i Z.                                       (10)

The fixed g and open theta interval avoid delta=0 mod2pi. Using (8)-(9)
for the single defect in (5),

    M=V^-1 T(lambda/gamma) V
     =[[C-i Z/s, i Y/s],[-i Y/s,C+i Z/s]].             (11)

Let c_left and c_right be the free mode coefficients in
v_r=V D^r c_left for r<=0 and V D^r c_right for r>=1.
The one defective bond imposes

    c_right=K c_left,    K=D^-1 M.                      (12)

For left incidence c_left=(1,r_L), c_right=(t_L,0).
For right incidence c_left=(0,t_R), c_right=(r_R,1).
Solving (12), with det K=1, gives the exact matrix from incoming
(left,right) to outgoing (left,right):

    S(lambda)=1/Dsc *
      [[iY, zeta s],
       [zeta s, i zeta^2 Y]].                          (13)

In particular t_L=t_R, while r_R=zeta^2 r_L in this explicitly fixed
bond-coordinate convention. The latter phase is not a difference of
reflection probabilities. One may rephase modes, but (13) freezes the
convention instead of silently doing so.

Since C^2+a1^2-b1^2=1 and a0^2-b0^2=s^2,

    |Dsc|^2=s^2 C^2+Z^2=s^2+Y^2>0.                    (14)

This proves that (13) is defined on the whole open band and S^*S=I.
In the free limit g=0, Y=0, Z=s^2, Dsc=s zeta, so S swaps incoming left
and right into transmitted right and left with amplitude one.

The exact reflected/transmitted flux fractions are

    R=Y^2/(s^2+Y^2),    T=s^2/(s^2+Y^2),    R+T=1.     (15)

These are quadratic scattering weights within the nominated Hilbert
model. No physical sampling, finite detector or event occurrence theorem
follows from flux unitarity alone.

For implementation without trigonometric phases define

    c=cos(theta), d=cos(theta+g),
    Knum=80(1+d)(d-c)^2,
    Lnum=(1-c)(1-d)(-5c-3).

Then (15) simplifies exactly to

    R=Knum/(Knum+Lnum),    T=Lnum/(Knum+Lnum).           (16)

To prove the simplification, use
b0^2=16(1+c)/(1-c), b1^2=16(1+d)/(1-d),
Y=(5/4)b0 b1(d-c), and
s^2=1-(5c+4)^2=-5(c+1)(5c+3).
All cancellations are on the specified open interval, so no division
by a zero endpoint is hidden.

For lambda=exp(-i theta) at the SAME gamma, complex conjugation relates
scattering to the above system with g replaced by -g, using the constant
internal matrix Z tensor Z to restore G after conjugation. This matrix
changes no channel flux. Reflection and
transmission probabilities therefore use d=cos(theta-g), not the same
cos(theta+g). A preparation's eigenphase branch matters.

## 4. Exact transparent point and endpoint limits [candidate-T]

The matrix identity

    T(rho^-1)=T(rho)^-1                               (17)

is immediate from (5). If lambda^2=gamma, the defect transfer is the
inverse free transfer. Hence K=D^-2, so

    R=0,    t=zeta^2.                                 (18)

For gamma=exp(-2pi i/5), the unique such lambda in the exp(i theta)
open propagating band is

    lambda_*=exp(4pi i/5)=j^2,
    theta_*=4pi/5,
    cos(q_*)=4-5phi/2.                                (19)

The other square root is outside that band. The right side lies strictly
between -1 and1. Also (16) vanishes only when d=c or d=-1. The fixed
interval theta+g lies strictly between pi and3pi/2, so d=-1 is absent;
d=c gives exactly (19). Thus this is the unique transparent point of
that band, not merely one searched numerical minimum.
On the opposite eigenphase band d=cos(theta-g) is greater than c
throughout, with d!=-1; it has no transparent point.

The limits are

    q -> 0:   R -> 1,
    q -> pi:  R ->
       20(1-cos g)^3/[20(1-cos g)^3+1+cos g].           (20)

The second limit is the same on the two eigenphase branches. These are
one-sided limits. At q=0 the group velocity vanishes. At q=pi the two
propagating eigenvalues meet at -1 and the basis (9) is singular. We do
not substitute an arbitrary basis at that degeneracy and call it a unique
scattering experiment. The interior formula and its controlled limits
are the claims.

## 5. Existing compact pair is dark to these incident modes [candidate-T]

Let chi_c=delta_(r=0) A, the inherited compact relative state. For every r
the A channel is invariant under W and W acts there by multiplication
by kappa_r. Therefore the rank-one projector Pi_c commutes with W:

    Pi_c W=W Pi_c=gamma Pi_c.

For every integer time n and every initial psi,

    ||Pi_c W^n psi||^2=||Pi_c psi||^2.                 (21)

The propagating modes in sections2-3 have zero A component. Hence they
cannot be converted by this exact P=0 walk into chi_c. An initially
present compact component remains; it is not dynamically manufactured
from zero. This does not refute the existing eigenbranch or its curvature,
and says nothing about the extra-carrier capture apparatus or a different
P fibre. Existence of a bound state is not a capture mechanism.

## 6. Reading interfaces retained explicitly

These are bounded analytical comparisons, not Canon status changes.

(a) Equal norms in the arithmetic two-body note make the elastic partner
a swap: (x+y)x'-(x'+y')y=N(x)-N(y)=0. This admission is always integral.
The present equal-coin W therefore cannot by itself test the unequal-norm
prime denominator obstruction. Unequal norm labels need not mean a new
fundamental species; any proposed comparison must freeze that choice.

(b) The mu=2 sine reading has Ehat=sqrt(4+sin(k)^2), phat=sin(k), and
its rapidity covers the CLOSED interval [-log(phi),log(phi)]. The endpoints
are attained. Differentiating cos(omega)=cos(k)/sqrt5 gives
|v_group|=|sin(k)|/Ehat<=1/sqrt5. This is a group/ballistic speed bound,
not the strict support cone of the finite-range update, which can move
one site per tick. Here the relative Fourier coordinate is q=2k at P=0;
user-reported q must not silently be interpreted as single-particle k.
The equality of the sine-band edge and the first positive-inverse golden
rung selects |mu|=2 within the nominated mass family. It does not derive
particle identity, coin choice or a native clock from J.

(c) Prime points such as phat^2=1/11 or4/19 use a normalization, not the
literal additive O_+ map. For example u_11=-1+3phi has N=-11, and
u_19=-1+4phi has N=-19. Set

    Ehat=(|u|+|u'|)/sqrt(p),
    phat=(|u|-|u'|)/sqrt(p).

This yields mass square4 and the quoted phat^2. It uses absolute values
and a prime-dependent square root. It need not remain in Q(sqrt5), and
it is not an additive map intertwining the arithmetic sum and W contact.
The rest-only literal signed-Galois norm-four intersection from #1839
therefore remains unchanged. A set of normalized spectral addresses is
not yet a common arithmetic dynamics.

(d) This calculation supplies an exact stationary scattering law of the
existing one-species W. It does not close a many-particle universe, source
preparation, event measure, readout apparatus, native U, a second-species
coupling, or any physical-layer gate. It adds no new model in place of W.
