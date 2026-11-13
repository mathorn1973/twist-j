# Reciprocal bound-charge and field dynamics over Z[phi]

NON-CANONICAL. Conditional candidate-T, pending independent review.
Reservation #1406. This is a closed comparison model, not a derivation of
an electron, proton, neutron, photon quantum, or the native update U.

## 1. Complete carrier and the new premises

Let R=Z[phi], phi^2=phi+1, s=2-phi. The marked real embedding has
0<s<2/5, s^2=3s-1 and s(1+phi)=1. Every ring operation is an integer
operation on the coefficient pair of 1,phi. The canonical equality
s=J Jbar supplies algebraic provenance, not dynamical selection.

Keep precisely the D3 triangular cochain geometry of #1403, head
30095fff125e664b2495784504a4524d29d37781. On a finite primitive periodic
quotient, G maps vertex values to oriented edge differences and C maps
edge values to the eight translated triangle circulations per cell.
P=C^T C, CG=0, and 0<=P<=8I in the counting inner products. The last
bound follows from the source's exterior representation
P(k)~8I-(ee*+zz*)^[2], whose spectrum is
0,8,4-|sum z_i|,4-|sum z_i|,4+|sum z_i|,4+|sum z_i|.
No mode is discarded. The empty-material limit below is precisely the
Z[phi] wave of #1405, head 393354eaa6ff8afc84d624c06995c3c087f679cd,
proof blob 989c28c5c3c07a0810c50c15011869c482fbcb01.
Both source notes remain NON-CANONICAL.

Choose a subset of distinct labelled oriented edges. Each supports one
material displacement x_m and its increment v_m. Let L:R^M->R^Ne be the
coordinate injection onto those edges, so L^T L=I and ||L||<=1 in the
marked real embedding. M=0 and L=I are allowed. Define Gamma=sL.
The placement of these bound degrees, their inertia normalization, the
restoring coefficient s, the coupling Gamma, and the action below are
NEW premises. They are not a discovered particle carrier or a consequence
of the axiom. A fixed support is not a freely recoiling particle centre.

The complete state is (A,E,x,v) in R^Ne x R^Ne x R^M x R^M, equivalently
Z^(4Ne+4M). No current, energy account, bath, switch, or program is supplied
at subsequent steps. All arrays have literal equality. Supplied spatial
geometry is L2 mathematics; the coefficient update is L1 comparison
mathematics. NOTE-MATTER-FIELD-RECIPROCAL-READING is an unadopted comparison
to L5 histories, not a registered or passed layer gate.

## 2. One autonomous local rule and its full inverse

Prime denotes one full step. In the written order, define

    x' = x+v,
    E' = E-s P A-Gamma v,
    A' = A+E',
    v' = v-s x'+Gamma^T E'.                                  (1)

The material current is j=Gamma v. The last term in (1) is the response
of the material to the actual updated field, not an assigned current law.
The inverse, on EVERY complete state, is

    v = v'+s x'-Gamma^T E',
    x = x'-v,
    A = A'-E',
    E = E'+s P A+Gamma v.                                    (2)

There is no division, rounding, state restriction, or growing denominator.
Since s(u+phi w)=(2u-w)+phi(-u+w), all displayed operations are integer
coefficient operations. Each elementary shear has determinant one, so the
complete integer automorphism does too. Dependence propagates only between
edges sharing a triangle and their attached material coordinates. One full
step has a finite dependency neighbourhood; this does not identify a
physical distance, time, or limiting signal speed.

For a second description set D=E+Gamma x. Equation (1) is exactly

    x'=x+v,        D'=D-s P A,
    E'=D'-Gamma x', A'=A+E', v'=v-s x'+Gamma^T E'.             (3)

In canonical pairs (A,D),(x,v), (3) composes the exact shears of the two
quadratic generators

    H1=|v|^2/2+s|CA|^2/2,
    H2=|D-Gamma x|^2/2+s|x|^2/2.

This proves symplecticity algebraically. Taking the coefficient of 1 in
the ring symplectic identity gives the ordinary nondegenerate integer
coefficient pairing, because that coefficient in ab is a0*b0+a1*b1.
It supplies no unit of physical action. The exact conserved discrete
energy is stated below; it is not silently equated with H1+H2.

Marked evaluation D_+(u,w)=u+phi w intertwines the ENTIRE joint map with
(1) over the reals. All couplings are matrices over R, so the induced
finite-dimensional marked response is continuous. There is no conjugate-
to-marked mixing. This does not select the marked physical interpretation.

## 3. A single gauge-invariant action and endogenous charge

To display the stagger explicitly, introduce notation X_n for material
positions in the action and write

    E_(n+1)=A_(n+1)-A_n-G psi_n.

With time endpoints fixed, take the one action

    S_action=sum_n [ |E_(n+1)|^2/2-s|CA_n|^2/2
                     +|X_(n+1)-X_n|^2/2-s|X_n|^2/2
                     +<Gamma X_n,E_(n+1)> ].                (4)

Formal variation can be performed after real extension; all resulting
identities have coefficients in R. Under A_n->A_n+G chi_n and
psi_n->psi_n+chi_(n+1)-chi_n every field term is unchanged, and X is
unchanged. Variation gives

    G^T(E_(n+1)+Gamma X_n)=0,
    E_(n+1)-E_n=-sPA_n-Gamma(X_n-X_(n-1)),
    X_(n+1)-2X_n+X_(n-1)=-sX_n+Gamma^T E_(n+1).              (5)

In temporal gauge, identify the state in (1) at n by
x_n=X_(n-1), v_n=X_n-X_(n-1), E_n=A_n-A_(n-1).
Thus the staggering is explicit and (5) is exactly (1), with the initial
Gauss condition. No physical time assignment follows from this notation.

Define the material charge and full Gauss defect by

    rho_n=-G^T Gamma x_n,
    Q_n=G^T(E_n+Gamma x_n)=G^T E_n-rho_n.                    (6)

The actual displacement generates the current, with

    j_n=Gamma(x_(n+1)-x_n)=Gamma v_n,
    rho_(n+1)-rho_n=-G^T j_n,       Q_(n+1)=Q_n.             (7)

The second equality uses G^T P=0 and holds even for nonzero initial Q.
Zero Gauss defect is therefore an invariant prepared sector, not a
projection after each step. On a closed quotient total rho is zero.
An occupied edge represents a bound charge dipole; isolated nonzero total
charge, free particle transport, and quantized charge are not supplied.

## 4. Common energy, reciprocal force, and local transfer

Use ordinary products in R, not products between real embeddings. Freeze
three doubled contributions on the complete state:

    F=|E|^2+s<A,P(A-E)>,
    M=|v|^2+s<x+v,x>,
    I=-<E,Gamma v>,             Ecal=F+M+I.                 (8)

F is exactly the predecessor field invariant at the two slices A,A-E.
M is the analogous material oscillator expression at x+v,x. I is a real
interaction term, not an extra account coordinate.

For (1), expansion gives separately

    F'-F=-<Gamma v,E'+E>,
    M'-M=<E',Gamma(v'+v)>,
    I'-I=-<E',Gamma v'>+<E,Gamma v>.                        (9)

Every term cancels in their sum. Thus Ecal'=Ecal exactly in R, so BOTH
integer coefficients are conserved. The marked comparison energy is
H=D_+(Ecal)/2. No external work source balances a discrepancy.

The reciprocity in (1) is necessary within a precise class. Keep its first
three equations and (8) fixed, but replace the last equation by
v'=v-sx'+K E', for any matrix K over R. Then

    Ecal'-Ecal=<E',(K^T-Gamma)(v'+v)>.                     (10)

For fixed E' the vector v'+v can be arbitrary: take A=v=0, E=E', and
x=s^-1(K E'-(v'+v)). The inverse s^-1 is in R. Hence conservation on
EVERY state is equivalent to K=Gamma^T. This does not classify different
energy functionals, nonlinear laws, or arbitrary physical interactions.

There is also a literal local balance. Assign E_e^2 to each edge, assign
s(CA)_f C(A-E)_f to each face, and assign
v_m^2+s(x_m+v_m)x_m-s E_(edge m)v_m to each material site. For each
incident face/edge and each material site put

    J_fe=s C_fe(CA)_f(E'_e+E_e),
    W_m=s v_m(E'_(edge m)+E_(edge m)).                      (11)

The local changes are

    Delta(edge e)=-sum_f J_fe-sum_(m on e) W_m,
    Delta(face f)=sum_e J_fe,
    Delta(material m including its interaction)=W_m.       (12)

Thus both spatial transfer and matter work cancel locally, before summing
the system. The local time-mixed densities need not be pointwise positive.
This is an exact lattice conservation identity, not an SI Poynting law.

## 5. Positivity and stability in the marked reading

All terms in this section are evaluated in the marked real embedding.
Let a_mid=A-E/2 and x_mid=x+v/2. Then

    Ecal=s|C a_mid|^2+s|x_mid|^2
          +<E,(I-sP/4)E>+(1-s/4)|v|^2-<E,Gamma v>.       (13)

By ||L||<=1, P<=8I and 2|<E,Lv>|<=|E|^2+|v|^2,

    Ecal>=s|C a_mid|^2+s|x_mid|^2
           +(1-5s/2)|E|^2+(1-3s/4)|v|^2 >=0.             (14)

Both last coefficients are strictly positive because 0<s<2/5. Equality
holds exactly when E=v=x=0 and CA=0. It follows that E, CA, x and v stay
bounded along every free joint orbit on a fixed finite quotient. For CA
use CA=C a_mid+CE/2 and ||CE||<=sqrt(8)||E||; x=x_mid-v/2.
A pure gauge or harmonic potential coordinate is not bounded by this claim.

This is stability of the marked fields and bound material motion, not of
all integer coefficient arrays. The marked image remains dense; a coupled
conjugate-growth example is given in Section 6. No
positive coercive full-integer-state energy, thermal counting measure,
quantum state, or physical energy normalization is asserted.

## 6. Exact material response and mixed normal modes

For the homogeneous comparison L=I, diagonalize P at any stiffness
lambda in [0,8]. Let z be a time multiplier and q=2-z-z^-1. For a
nonzero frequency the four equations yield

    (s lambda-q)A+s(z-1)x=0,
    (s-q)x-s(z-1)A/z=0.

Consequently the full characteristic polynomial is

    z^2[(s lambda-q)(s-q)-s^2 q]
      =z^4+[(lambda+4)s-5](z^3+z)
            +[8-lambda+(lambda-8)s]z^2+1.                 (15)

The polynomial identity includes z=1 by expansion, so no root is lost by
the intermediate divisions. Writing a=s lambda, the two q roots solve

    q^2-(a+s+s^2)q+a s=0.                                (16)

For lambda>0 their product and sum are positive and their discriminant is
(a-s)^2+2s^2(a+s)+s^4>0. Moreover f(4) is minimized at lambda=8, where
f(4)=12(1-2s)>0, and their sum is at most 12s-1<8. Hence both roots lie
strictly between zero and four, giving distinct unit-circle temporal
pairs. At lambda=0 the q roots are 0 and s+s^2=4s-1; the z=1 root has
algebraic multiplicity two, with the usual potential drift possibility.
All original spatial modes remain; two spatially degenerate transverse
low branches remain degenerate after the same coupling. For the conjugate
embedding s'=1+phi, the two q roots at lambda=8 have sum 12s'-1>8
and are real and positive. At least one exceeds four, producing an
expanding temporal root. Thus even the homogeneous coupled integer map
has unbounded coefficient orbits; marked stability does not bound them.

The displacement equation gives, away from q=s,

    x=s E/(s-q),
    D=E+s x=epsilon(q)E,     epsilon(q)=1+s^2/(s-q),
    q epsilon(q)=s lambda.                               (17)

At q=s the undivided determinant is -s^3, not zero. It is not an omitted
eigenmode. This material response and the mixed-mode splitting follow
from the same dynamics; they were not entered as a refractive-index fit.
For long waves, using lambda_low=|k|^2/2+O(|k|^4),

    q_low=[s/(1+s)]lambda_low+O(lambda_low^2),
    c_material^2=s/[2(1+s)]=(3-phi)/10,
    c_empty^2=s/2,      c_empty^2/c_material^2=1+s=3-phi.   (18)

These are dimensionless consequences of the selected homogeneous bound
medium, not experimental constants or a vacuum modification. Empty
material supports recover the original free field exactly.
Longitudinal modes with Gauss imposed carry the bound-charge response,
not an additional freely propagating photon polarization. No branch is
named as an electron, proton, neutron, or its mass.

## 7. A source that pays, and the retained quantum boundary

With just one material site on edge e, prepare A=E=x=0, v=1. Then
Ecal=1 and one actual step gives

    x'=1, j=s e, E'=A'=-s e,
    v'=1-s-s^2=2-4s,
    rho'=-s G^T e,       Ecal'=1.                         (19)

The force contribution is Gamma^T E'=-s^2. Both a dipole and field have
appeared at the expense of the evolving material subsystem and the
interaction, with no prescribed current at the next step. At step two,
away from edge e, A''=s^2(Pe), so field transport beyond the source is
explicit wherever the corresponding incidence coefficient is nonzero.

Remove only the backreaction term while keeping everything else. On the
same first preparation the doubled energy change is 1-2s>0. A one-way
emitter is therefore not a conservative instance of this exact law.

The entire map is R-linear. Multiplication of every state coordinate by
s^m commutes with it, preserves Gauss and primitive integer gcd, and changes
H by s^(2m). The initial source of (19) is primitive and has H=1/2. Thus
this already CLOSED matter-field system still has primitive states of
arbitrarily small positive H. Coupling alone did not derive a photon
energy quantum, discrete particle number, or a Born/event rule.

## 8. Scientific scope and prior context

The new result removes the externally supplied current in this comparison
and replaces it by autonomous, energy-paying bound-charge motion with
reciprocal feedback. Selection of the material carrier, occupied supports,
restoring law, coefficient role, field action, and marked reading remains
open as physics. Nothing here derives native U, freely moving charged
particles, spin/statistics, proton/neutron structure, rest masses, particle
creation, Planck's constant, SI calibration, or any canonical physical O.

Electromagnetic coupling to polarization oscillators and gauge-preserving
variational discretization are established methods. The present proof is
self-contained and claims only this exact integer-ring implementation and
its stated boundaries, not novelty of those general physical ideas.
Primary context (not redistributed or used as a black-box theorem):
- J. J. Hopfield, Phys. Rev. 112, 1555 (1958), DOI 10.1103/PhysRev.112.1555.
- J. Squire, H. Qin, W. M. Tang, arXiv:1401.6723.
- A. Stern et al., arXiv:0803.2070.
Original text and code: Apache-2.0.
