# Exact original-operator audit of the complete capture resolvents

**PUBLIC ANALYTICAL PROPOSAL. NON-CANONICAL / L1.**

Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.
Reservation: [#1816](https://github.com/mathorn1973/twist-j/issues/1816).
Source custody and immutable dependency commits: `SOURCES.md`.
The separate finite-approximation construction is `FINITE_PROTOCOL.md`.

This is a second derivation within the same continuing authoring session.
It is not external independent acceptance. No scientific module, CAS,
numerical evaluation or verifier has been run in preparing this draft.
The exact checks below are inputs to the separately authored verifier
`probes/P-BOUND-PAIR-RESOLVENT-AUDIT-1/verify.py`, in the same prospective
public pin as this proof. Its first disposition belongs in that probe's
RESULT.md; this analytical text makes no pre-execution run claim.

The defining inputs are the original product coin, streaming and contact
operators in PROOF_CAPTURE_SCATTERING.md, sections 1--3, and the normalized
packet in PROOF_PACKET_CERTIFICATE.md, section 2, under
notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/. The later scalar model is the
object of this audit, not the definition used to derive the formulas.
The unitary spectral and stationary scattering theorems remain explicit
analytical premises. Section 15 checks the primary stationary theorem's
fiberwise application and convention conversion. Finite polynomial
identities do not themselves prove a wave-operator theorem.

## 1. Original operator and an exact Bell change of basis

Use the original coin order (++, +-, -+, --). Put

    M = (1/5) [[1, 2i, 2i, -4],
               [2i, 1, -4, 2i],
               [2i, -4, 1, 2i],
               [-4, 2i, 2i, 1]],
    F(P,kappa) = diag(w,z,z^(-1),w^(-1)) M,
    w = exp(iP), z = exp(i kappa).

The interacting relative operator at fixed P is W(P)=Gamma F(P), with
Gamma=I+(gamma-1)jj*, gamma=exp(-ig), and j the injection of all four coin
states at relative site zero. The ordering is Gamma F, not F Gamma.

Let O=H/sqrt(2) have columns A,S,T,B, where

    H = [[ 1, 1, 0, 0],
         [ 0, 0, 1, 1],
         [ 0, 0, 1,-1],
         [-1, 1, 0, 0]].

Then H^T H=2I. This permits a check over Gaussian rational Laurent
polynomials without adjoining sqrt(2). Define

    d=-3/5, c=4/5, ell=1+d=2/5, b=1-d=8/5,
    v=(w+w^(-1))/2, s=(w-w^(-1))/(2i),
    h=(z+z^(-1))/2, j_k=(z-z^(-1))/(2i).

Thus v^2+s^2=h^2+j_k^2=1 and c^2+d^2=1. Direct multiplication of the
original matrices gives

    F_Bell =
    [[v,       i d s,      -c s,       0],
     [i s,     d v,         i c v,     0],
     [0,       i c h,       d h,       i j_k],
     [0,      -c j_k,       i d j_k,   h]].

This is an analytical change of basis from H^T F H/2. The finite
verifier starts from the original product symbol and transforms its
computed adjugate; it does not use this displayed Bell matrix as its
raw definition or separately test its entries against this table.

## 2. Determinant from the original stationary/moving blocks

For a spectral parameter lambda with |lambda|>1 set L=lambda I-F_Bell and

    D0=lambda^2-ell v lambda+d,
    D1=d lambda^2-ell v lambda+1.

The stationary A,S block of L is

    A2 = [[lambda-v, -i d s],
          [-i s,     lambda-d v]],

with determinant D0. Its coupling column to T is r=(c s,-i c v)^T, and

    A2^(-1) r = (c/D0) (lambda s, i(1-v lambda))^T.

Eliminating A,S therefore gives the moving T,B Schur matrix

    [[lambda-eta h, -i j_k],
     [-i eta j_k,   lambda-h]],
    eta=D1/D0=d+c^2(1-v lambda)/D0.

Its determinant is lambda^2-(1+eta)lambda h+eta. Hence, directly from
the original 4 by 4 operator,

    det L = a-Bcos h,
    a=lambda^2 D0+D1
      =lambda^4-ell v lambda^3+2d lambda^2-ell v lambda+1,
    Bcos=lambda(D0+D1)
         =ell lambda(lambda^2-2v lambda+1).

The stationary block of F is a compression of a unitary symbol and
therefore a contraction. Hence A2, which is lambda I minus that block,
is invertible for |lambda|>1. All identities also hold polynomially,
without requiring an inverse at exceptional algebraic values.

## 3. Full adjugate: explicit Laurent coefficients

The following table is obtained by cofactors of L. It supplies an
independent finite target for a raw determinant/adjugate implementation.
Write

    adj L = N0+h Nc+j_k Ns.

All entries connecting B to A,S,T are odd in kappa. The even 3 by 3
blocks, in order A,S,T, are

    N0_even =
    [[lambda^3-d v lambda^2+d lambda-v,
      i s(d lambda^2+1),
      -c lambda^2 s],
     [i s(lambda^2+d),
      (lambda-v)(lambda^2+d),
      i c lambda(v lambda-1)],
     [c s,
      -i c(lambda-v),
      lambda D0]],

    Nc_even =
    [[-ell lambda(lambda-v),
      -i ell lambda s,
      c lambda s],
     [-i ell lambda s,
      -ell lambda(lambda-v),
      -i c(v lambda-1)],
     [-c lambda s,
      i c lambda(lambda-v),
      -D0]].

The remaining even entries are

    (N0)_BB=lambda D0,  (Nc)_BB=-D1,

and the even cross entries involving B vanish. The odd coefficient is

    Ns =
    [[0,0,0, -i c lambda s],
     [0,0,0,  c(1-v lambda)],
     [0,0,0,  i D0],
     [-i c lambda s, -c lambda(lambda-v), i D1, 0]].

For example, the AA cofactor is

    (lambda-d v)(lambda^2-ell lambda h+d)
      +c^2 v(lambda h-1)
    =lambda^3-d v lambda^2+d lambda-v
      -ell lambda(lambda-v)h.

The BB cofactor is lambda D0-D1 h. These checks determine both source
ports directly; the i in the original incoming vector iB cancels from
its diagonal resolvent expectation.

In the original basis every minor uses the row with z and the row with
z^(-1) at most once, so no harmonic beyond 0,+1,-1 is possible.
Conjugating the raw adjugate by H^T and H and dividing by two gives the
table above. In particular, sampling the adjugate at z=1 and z=-1
recovers N0 and Nc exactly, rather than as an interpolation assumption.

## 4. Exact integration of the infinite free contact Green matrix

Define

    Sigma^2=a^2-Bcos^2,  Sigma/lambda^4 -> 1 at infinity.

The zeros of a+Bcos and a-Bcos are eigenvalues of the original unitary
symbols at kappa=pi and kappa=0. Thus there are no zeros outside the
unit circle, and the exterior sheet is unambiguous. Bcos is nonzero
there as well: its remaining roots solve lambda^2-2v lambda+1=0.

The two roots in z of the denominator are

    z_-= (a-Sigma)/Bcos,  z_+=(a+Sigma)/Bcos.

At infinity z_- is small; it stays inside the unit circle throughout
|lambda|>1, since a crossing would be a nonunit-modulus eigenvalue of a
unitary Fourier symbol. Contour integration gives exactly

    I0 = integral dkappa/[2pi(a-Bcos cos kappa)] = 1/Sigma,
    I1 = integral cos(kappa) dkappa/[2pi(a-Bcos cos kappa)]
       = (a/Sigma-1)/Bcos.

The second identity also follows from a I0-Bcos I1=1.
The sine integral vanishes. Consequently the complete contact matrix is

    G0(P,lambda)=j*(lambda-F(P))^(-1)j=N0 I0+Nc I1.

This is an exact compression of the infinite operator. No relative
spatial truncation or restriction to one relative band has occurred.

In particular,

    G0_BB=lambda D0 I0-D1 I1.

## 5. Reduction to one algebraic root and the complete even inverse

Put

    u=(lambda+lambda^(-1))/2,
    t=v-5u,
    R^2=t^2-16,  R/t -> 1 at infinity,
    q=(t-R)/4.

Then

    2q^2-tq+2=0,
    R=t-4q,
    q=4/(t+R),
    Sigma=-(2/5)lambda(lambda^2-1)R.

The last sign is fixed at infinity, not chosen on a real-energy grid.
Useful exact intermediate identities are

    a^2-Bcos^2=(lambda^2-1)(lambda^2 D0^2-D1^2),
    D0=-(2/5)(4+lambda t),
    D1=-(2/5)lambda(4lambda+t),
    (lambda+q)(a-Sigma)=Bcos(1+lambda q),
    (lambda D0-D1 q)(lambda Bcos-a+Sigma)=Bcos Sigma.

The last two follow after reduction by 2q^2-tq+2 and may be checked
as Laurent-polynomial identities. They imply, respectively,

    I0-lambda I1=-q(lambda I0-I1),
    D0(lambda I0-I1)=1/(lambda-(D1/D0)q).

From the integrated adjugate in section 3, or by multiplying it on both
sides by the following matrix, one obtains

    G0_even^(-1)=Ke(lambda,q),
    Ke(lambda,q)=
    [[lambda-v, -i d s,       c s],
     [-i s,      lambda-d v, -i c v],
     [0,        -i c q,       lambda-d q]].

For the independent verifier, define

    M_even=Bcos N0_even+(a-Sigma)Nc_even.

Then the complete inverse assertion is the pair of finite identities

    Ke M_even = Bcos Sigma I3,
    M_even Ke = Bcos Sigma I3,

after substituting Sigma and reducing in the quadratic q relation.
This comparison begins with the full original 4 by 4 adjugate and is
not an identity checked solely inside the proposed scalar formula.

The entire even contact block is retained. The odd B block is separate
because the corresponding integrated cross entries are odd in kappa.

## 6. Contact phase update and the complete scalar fA

The correct ordered resolvent factorization is

    lambda-Gamma F
      =Gamma[(lambda-F)+lambda(gamma^(-1)-1)jj*].

Woodbury and compression at the contact therefore give

    G_W=gamma^(-1)
         [G0^(-1)+lambda(gamma^(-1)-1)I4]^(-1).

There is no scalar contact approximation in this expression. Set
x=lambda/gamma. In the even block the bracket is Ke with every
diagonal lambda replaced by x, leaving the exterior q(P,lambda)
unchanged:

    Kgamma=
    [[x-v, -i d s, c s],
     [-i s, x-d v, -i c v],
     [0, -i c q, x-d q]].

Its AA cofactor and determinant are

    N=x^2-d(v+q)x+v q,
    D=x^3-(ell v+d q)x^2+(d+ell vq)x-q.

For example, direct expansion of the determinant gives

    D=(x-v)N+d(1-v^2)x-(1-v^2)q.

The Caratheodory function is 2lambda times the Green expectation minus
one, so the original A source gives

    fA(P,lambda)=2x N/D-1.

This derivation confirms the prefactor x rather than lambda and that q
depends on lambda rather than x.

Writing

    C=x^2-ell v x+d,
    Bpoly=-d x^2+ell v x-1,

one has D=x C+q Bpoly. Eliminating q from this original equation gives
the degree-at-most-six candidate polynomial

    4x^2 C^2
    +(2v x-5gamma x^2-5gamma^(-1)) C Bpoly
    +4 Bpoly^2 =0.

This is only a candidate polynomial. The original D, the physical
q sheet and numerator cancellations remain authoritative.

## 7. The odd scalar from the original BB cofactor

Starting from G0_BB in section 4, without the later scalar model,

    f0B=2lambda G0_BB-1
       =2(lambda^2 D0^2-D1^2)/[(D0+D1)Sigma]
          +(D1-D0)/(D0+D1).

Use

    D0+D1=ell(lambda^2-2v lambda+1),
    D1-D0=-b(lambda^2-1),
    lambda^2 D0^2-D1^2=Sigma^2/(lambda^2-1).

Then

    f0B=[R+2(lambda-lambda^(-1))]
          /[v-(lambda+lambda^(-1))/2].

The contact update in this one-dimensional odd contact block is

    fB=[(1+gamma)f0B+(1-gamma)]
         /[(1-gamma)f0B+(1+gamma)].

For gamma=exp(-ig), (1-gamma)/(1+gamma)=i tan(g/2), agreeing with
the original odd-sector Mobius formula and its sign. Direct
cross-multiplication, using only R^2=t^2-16, yields

    fB(P,lambda)
      =[R+2(x-x^(-1))]/[t+2(x+x^(-1))],
    x=lambda/gamma.

On lambda=exp(-i omega) this is precisely

    fB=[R-4i sin(omega-g)]/[t+4cos(omega-g)].

The original denominator v-cos(omega) is removable where both numerator
and denominator vanish. The equality is an exterior analytic identity,
not a new branch convention at such a boundary point.

## 8. Physical sheet and boundary classification

For lambda=r exp(-i omega), r>1,

    Im t=(5/2)(r-r^(-1)) sin(omega).

The exterior lambda domain maps away from the real interval [-4,4]:
if Im t=0 there, lambda is real, and t is strictly outside that
interval. Thus R is the usual analytic root on the complement of
[-4,4] with R/t -> 1. Its boundary is

    R=sgn(t) sqrt(t^2-16)                  for |t|>4,
    R=i sgn(sin omega) sqrt(16-t^2)        for |t|<4.

The second sign must change with sin(omega). It cannot be fixed to a
positive imaginary square root on a shifted energy branch crossing pi.

At a nonexceptional unit-circle point,

    (a/Bcos)^2-1
      =-sin(omega)^2 (t^2-16)/(cos(omega)-v)^2.

The Fourier denominator has a real relative momentum root precisely
when |a/Bcos|<=1. Hence |t|>4 is the continuous region and |t|<4 is a
free gap. Removable denominators and the endpoint flat-band cases are
handled by continuation from the original determinant, not by division
at a zero.

The effective q is not the integrated Fourier variable z and is not
the spatial decay root z_- from section 4. On the physical boundary,
q is real with |q|<1 in the continuum and has modulus one in a gap.

The exterior small branch is independently characterized by

    q=-4/(5lambda)-8v/(25lambda^2)+O(lambda^(-3)).

The other quadratic root is large and does not represent the contact
Green matrix. Polynomial equality modulo the q relation alone does not
select between these two roots.

## 9. Real gap denominator and pole residue

On a strict gap with fixed sign of sin(omega), let

    delta=omega-g,
    eta=sgn(sin omega) arccos(t/4),
    chi=(eta-delta)/2,
    H=(cos delta-v)sin chi-4 sin delta cos chi,
    G=4(cos delta+v)cos chi+sin delta sin chi.

Then q=exp(-i eta), x=exp(-i delta). Factoring the polynomials in
section 6 gives the exact identities

    D=(4i/5)exp[-i(eta+3delta)/2] H,
    2xN-D=(4/5)exp[-i(eta+3delta)/2] G,
    fA=-i G/H.

They follow by collecting exp(i chi) and exp(-i chi) terms. For
example, D divided by the phase factor is

    2i ell(cos delta-v)sin chi-2i b sin delta cos chi.

At a simple, visible object eigenphase omega_b(P), the spectral
representation has singular part

    fA(P,lambda)=r_b(P)(lambda+lambda_b)/(lambda-lambda_b)
                  +regular,
    lambda_b=exp(-i omega_b),  r_b>0.

Equivalently,

    r_b=Res_(lambda_b)fA/(2lambda_b)
       =N/(gamma partial_lambda D)
       =-G/(2 partial_omega H).

The derivatives of D include the lambda dependence of q on its physical
sheet. A zero of D with canceled numerator is not a visible pole.
At P=0 or pi such cancellations can occur.

The real residue sign is also fixed by exterior continuation:
lambda=exp[-i(omega+i epsilon)], epsilon>0, gives

    fA ~ 2i r_b/[omega-omega_b+i epsilon].

Thus its real boundary contains the positive measure
2pi r_b delta(omega-omega_b), and its imaginary part is the corresponding
principal value. This independently fixes the sign needed below.

## 10. Complete pulse convolution, coarea and PV subtraction

Derive the pulse symbol from the original E(k)Q product:

    V(k)=(1/5)[[1-4 exp(ik), -2(1+exp(ik))],
               [2(1+exp(-ik)), 1-4 exp(-ik)]].

It has determinant one and cos(epsilon)=(1-4cos k)/5. For the eigenvalue
exp(-i sigma epsilon), sigma=+1 or -1, its first-bank overlap is

    h_sigma(k)=(1-sigma epsilon'(k))/2.

For example,
P_+=(exp(i epsilon)I-V)/(2i sin epsilon), whose 11 entry is
1/2+2sin k/(5sin epsilon)=(1-epsilon')/2. The negative-band overlap is
the complement. Both branches are retained.

The full incoming and outgoing arrangement functions are therefore

    F1(zeta)=integral fB(P,zeta exp(i beta)) dP/(2pi),
    F2(K,zeta)=integral sum_sigma h_sigma(k)
      fA(K-k,zeta exp[i(beta+sigma epsilon(k))]) dk/(2pi).

The substitution P=K-k is orientation-reversing, but reversing the
integration limits leaves the positive full-circle measure dk/(2pi).
No scalar source restriction belongs in these functions.

For fixed K,E define

    omega_sigma(k)=E-beta-sigma epsilon(k),
    H_sigma(k)=H(K-k,omega_sigma(k)),
    B_sigma(k)=h_sigma(k)G(K-k,omega_sigma(k)).

At a simple root k_j belonging to an object band omega_b, put

    Fband(k)=omega_b(K-k)+beta+sigma epsilon(k),
    c_j=B_sigma(k_j)/(2 H_sigma'(k_j)).

Implicit differentiation of H(P,omega_b(P))=0 gives

    H_sigma'=-H_omega Fband',
    c_j=h_sigma r_b/Fband'.

Consequently the pointwise imaginary singularity is
-2i c_j/(k-k_j). Adding +i c_j cot((k-k_j)/2) removes it. The
cotangent has zero full-circle principal-value integral.

The real boundary contribution after the dk/(2pi) integration is

    h_sigma r_b/|Fband'|=|c_j|.

Thus the complete F2 must include every such real weight, plus both
continuum integrals, and the integral of the fully regularized imaginary
part. The selected output density with respect to dE is

    rho_(2,b,+)=|c_selected|/(2pi).

This factor of 2pi is distinct from the real contribution |c_selected|
to F2. A joint velocity zero Fband'=0 is not covered by this simple-root
formula and must be excluded or treated separately.

At k=+-pi the two pulse branches meet. A full two-branch sum or an
appropriate one-sided chart is needed; dropping a branch is invalid.
A zero-weight exceptional root family may be retained by continuity,
but does not supply a positive spectral weight at that parameter.

## 11. Positive even continuum identity

On the open continuum q is real. Set

    A_poly=x^2+(1-d)v x-d,
    C=x^2-ell v x+d.

For |x|=1, direct polynomial rearrangement gives

    2xN-D=x A_poly+q x^2 conjugate(A_poly),
    D=x C-q x^2 conjugate(C),
    Re(A_poly conjugate(C))=(1-d^2)(1-v^2).

The cross terms in the numerator multiplied by conjugate(D) are purely
imaginary. Hence

    Re fA=(16/25)(1-v^2)(1-q^2)/|D|^2
         =(8/25)(1-v^2)qR/|D|^2,

using qR=2(1-q^2). This confirms the sign and normalization of the
entire even continuum contribution, not only a selected output channel.

## 12. Original rank-two capture normalization

Keep the capture rotation distinct from the internal phase Gamma:

    Kc=Ccore-I=(1/5)[[-2,-4],[4,-2]],
    m=diag((F1-1)/2,(F2-1)/2).

The original ordered law is U=U0(I+J Kc J*). Direct 2 by 2 algebra gives

    det(I-m Kc)=(4+F1 F2)/5,
    [Kc(I-m Kc)^(-1)]_21=4/(4+F1 F2).

With the source convention dmu=rho dE, the Caratheodory real boundary
is Re F=2pi rho. The inherited stationary scattering theorem then
gives the selected transition kernel

    4pi^2 |T21|^2 rho_in rho_(2,b,+)
      =64pi^2 rho_in rho_(2,b,+)/|4+F1 F2|^2.

There is no replacement of F1 by rho_in, or of F2 by its one selected
bound channel. The incoming normalized spectral direction has overlap
sqrt(rho_in) with the full port direction; the outgoing selected
direction supplies sqrt(rho_(2,b,+)).

The original source has energy density 1/(2h) on I_E and a token
localized at y=0. Its total-momentum measure is therefore dK/(2pi) on
the whole circle. The probability of the unchanged windowed event is

    P0=integral_(I_K) dK/(2pi) integral_(I_E) dE/(2h)
       64pi^2 rho_in(E) rho_(2,b,+)(K,E)
       /|4+F1(E)F2(K,E)|^2.

The energy measure has total mass one, whereas the selected K interval
has mass delta_K/pi. Conditioning the input on I_K would remove this
factor and define a different preparation. There is no factor of 26:
the initial token label is fixed, and the complete old-memory output
sum has unit norm. There is no extra factor of two from the common-parity
coordinates: R,r are the original lattice coordinates and their Fourier
measures are already normalized. Macrostep duration does not rescale a
dimensionless event probability.

The exact complete-denominator identity is

    |4+F1 F2|^2-16 Re(F1)Re(F2)
      =|4-F1 conjugate(F2)|^2.

It is a valid lower bound on that same full denominator; it is not a
selected-channel substitution.

## 13. Additional independent low-order checks

The original operator gives moments without any Green elimination.
The A source stays at relative zero in its first step, so

    <A0,W A0>=gamma v,
    <A0,W^2 A0>=gamma^2(v^2-d s^2)
                      =gamma^2(ell v^2-d).

The B source has zero one-step return. Its two-step free return is
(1-d)/2=4/5 and only the returning step receives the contact phase.
Therefore

    fA=1+2gamma v/lambda
         +2gamma^2(ell v^2-d)/lambda^2+O(lambda^(-3)),
    fB=1+(8gamma/5)/lambda^2+O(lambda^(-3)).

These identities check the contact phase factors and the two source
ports. They do not by themselves distinguish Gamma F from F Gamma:
the two operators are conjugate by Gamma, which acts as a common scalar
on the contact subspace, so their contact-compressed Green matrices
agree. The ordered factorization in section 6 was nevertheless derived
from the actual defining law. The exterior branch in section 8 must
reproduce these direct return moments.

At v=1, the original A0 is an exact eigenvector of W with eigenvalue
gamma; at v=-1 it has eigenvalue -gamma. Thus, independently,

    fA(0,lambda)=(lambda+gamma)/(lambda-gamma),
    fA(pi,lambda)=(lambda-gamma)/(lambda+gamma).

The polynomial formulas satisfy D=(x-1)N at v=1 and D=(x+1)N at v=-1.
This confirms the cancellations of A-invisible even factors at the
compact endpoints.

## 14. Audit disposition and scope of a finite verifier

No exact discrepancy was found in this second analytical derivation
between the original defining operators and the proposed fA, fB,
exterior sheet, H/G residue, periodic PV subtraction or original
64pi^2 and window normalization.

The implemented finite checks include:

1. Construct the original product coin and Fourier symbol; verify
   unitarity, the determinant, both raw adjugate identities and its
   complete relative Laurent support.
2. Form the integrated adjugate numerator from those original
   coefficients and check both complete Ke inverse identities.
3. Check the odd free scalar and its Mobius reduction, with the same
   algebraic root, rather than beginning with a pre-simplified odd formula.
4. Check the contact determinant/cofactor, compact endpoints and direct
   low-order return moments.
5. Check the real H/G factorization, positive continuum identity,
   original pulse determinant/trace/unitarity, complete rank-two
   transition and its on-shell unitarity.

The displayed manual Bell-adjugate table and the pulse projector weights
are derived analytically above; they are not additional entry-by-entry
gates in the executable. The complete integrated even inverse is
nevertheless compared with the adjugate computed from the raw symbol.

The finite algebra cannot replace the analytic selection of the exterior
root, the unitary spectral theorem, stationary scattering, normalization
of the actual prepared packet, or the distributional boundary/coarea
argument. Those are explicitly supplied above or inherited at their
stated scope. A successful exact audit would add a different finite
operator-to-scalar check, not a new value of P0, an independent external
review, a finite-time experiment or a native preparation theorem.

## 15. Primary stationary-convention import without a reciprocity assumption

This section was checked against R. Tiedra de Aldecoa, *Stationary
scattering theory for unitary operators with an application to quantum
walks*, arXiv:1912.04960v2 (2 July 2020), available at
https://arxiv.org/pdf/1912.04960. The retrieved PDF itself identifies v2.
The relevant items are Example 3.8, Lemma 4.1, equations (4.2)--(4.3),
and Theorem 4.3, equation (4.6). The operator definition immediately
following (4.2) was also inspected in the rendered PDF.

This supplies the convention conversion omitted by a bare statement
that adjoint scattering preserves transition probabilities. Such a
statement is not valid for an arbitrary fixed input and a restricted
output subspace.

### 15.1 Apply the paper fiberwise and distinguish the two resolvents

Fix total momentum K and one carrier label. The identification operator
in the paper is the identity on the common Hilbert space; it is NOT our
two-port injection J. Write

    C=I+mathcal_B,  mathcal_B=J Kc J*,  U=U0 C,
    V=U0-U=-U0 mathcal_B,
    Rp(z)=(I-z U*)^(-1),  R(z)=(z-U)^(-1),
    R0(z)=(z-U0)^(-1).

The paper uses

    Tp_+(z)=U0* V - V* Rp(z) V,
    Tp_-(z)=Tp_+(1/conjugate(z))*.

In the second formula the final star is the operator adjoint.
Our perturbation is finite rank on each K fiber, so the trace-class
case in Example 3.8 applies there. This is a fiberwise application,
not a claim that the undecomposed homogeneous perturbation is globally
trace class.

Unitarity and U=U0 C imply

    U0*=C U*,  V*=mathcal_B U*,
    Rp(z)=-R(z)U,  U* Rp(z)=-R(z).

Substitution into the paper's actual Tp_+ gives

    Tp_+(z)
      =-mathcal_B-mathcal_B R(z)U0 mathcal_B
      =-mathcal_B[I-R0(z)U0 mathcal_B]^(-1).

The last equality is the resolvent identity. Pushing the finite-rank
injections through the inverse therefore gives exactly

    Tp_+(z)=-J T(z)J*,
    T(z)=Kc[I-m(z)Kc]^(-1),
    m(z)=J* R0(z)U0 J.

For |z|>1 this is the exterior quantity used in the capture proof,
with m_j=(F_j-1)/2. Equivalently, compressing the paper's free
resolvent gives J* Rp0(z)J=-m(z). No unrecorded sign is absorbed into
this definition.

### 15.2 Use equation (4.6) and adjoint the whole on-shell operator

The paper defines Wp_+=lim_(n->+infinity) U^n U0^(-n) and Wp_- with
the negative limit. Our Omega_+=Wp_- and Omega_-=Wp_+, so

    Sp=Wp_+* Wp_-,  S_ours=Omega_+* Omega_-=Sp*.

Let Z(E) be the finite-port spectral map whose columns are

    z_j(E)=(F0 a_j)(E),

using the direct integral with measure dE. Thus
||z_j(E)||^2=rho_(j,total)(E). Changing the paper's spectral label
exp(i theta) to exp(-i E), theta=-E modulo 2pi, preserves the positive
Lebesgue measure and adds no normalization factor.

Equation (4.6) takes Tp_- at the interior boundary. Its adjoint relation
is precisely

    Tp_-((1-epsilon)exp(-iE))
      =Tp_+((1-epsilon)^(-1)exp(-iE))*.

Using Tp_+=-J T J* in that formula gives, at almost every on-shell
point, with T_ext the EXTERIOR boundary,

    Sp(E)=I+2pi Z(E) T_ext(E)* Z(E)*.

Taking the adjoint of this entire fiber operator now yields

    S_ours(E)=I+2pi Z(E) T_ext(E) Z(E)*.

This is the required direct exterior formula. It has not replaced one
selected transition norm by a purported reciprocal transition norm.
In particular, its arrangement-changing block is

    (S_ours)_21=2pi T21 |z_2><z_1|.

Correspondingly (Sp)_12=2pi conjugate(T21)|z_1><z_2|. These are adjoint
rank-one operators with the correct source and target spaces, rather
than scalar entries assigned to whole multichannel arrangements.

### 15.3 Restrict the prepared input and selected output only now

Let Pin(E) be the original incident relative-ac and momentum selection
inside arrangement 1, and let Qout(K,E) be the original selected
bound/positive-pulse/window projection inside arrangement 2. Put

    rho_in=||Pin z_1||^2,
    xi_in=Pin z_1/sqrt(rho_in),
    rho_out=||Qout z_2||^2.

These are exactly the source normalization and selected outgoing
density used in the packet theorem. Since Qout xi_in=0, the identity
part of S contributes nothing to this transition. The full operator
formula gives

    Qout S_ours xi_in
      =2pi T21 sqrt(rho_in) Qout z_2,

and hence

    ||Qout S_ours xi_in||^2
      =4pi^2 |T21|^2 rho_in rho_out
      =64pi^2 rho_in rho_out/|4+F1 F2|^2.

This remains valid when Qout is much narrower than the whole second
arrangement: its only effect is the explicit projected norm
||Qout z_2||^2. The complete F1,F2 in T remain unchanged.

No reciprocity assumption was needed, including no general assertion
that ||Q S psi|| equals ||Q S* psi||. Alternatively, the adjoint
restricted blocks have equal operator norm, and here the prescribed
input xi_in is exactly the aligned vector that attains the rank-one
block norm. An arbitrary input in the same arrangement need not do so.

### 15.4 An additional finite on-shell unitarity check

The complete two-port matrix is explicitly

    T=[[-2F2,-4],[4,-2F1]]/(4+F1 F2).

Set A=diag(Re F1,Re F2)=I+m+m*. Since Ccore=I+Kc is unitary and
Kc is invertible, Kc^(-1)+(Kc*)^(-1)=-I. Consequently

    T^(-1)+(T*)^(-1)=-A,
    T+T*+T* A T=0.

The latter identity is valid without division after clearing the
denominators and can be checked with independent conjugate variables.
It proves unitarity of I+sqrt(A)T sqrt(A) on the two normalized port
directions whenever A is positive. This agrees with the preceding
2pi factor because sqrt(A)=sqrt(2pi rho_total). At F1=F2=1 it reduces
exactly to I+T=Ccore. It is an algebraic consistency check, not a
replacement for the primary stationary theorem.

### 15.5 Disposition of this import audit

The primary operator calculation closes an exposition gap in the
convention conversion. It confirms the exterior m, the selected
transition kernel and its 64pi^2 normalization. It does not reveal a
numerical discrepancy in the predecessor. Any informal transcription
of Tp_+ must retain the minus sign in -V* Rp V with V=U0-U; changing
that sign would invalidate the reduction.
