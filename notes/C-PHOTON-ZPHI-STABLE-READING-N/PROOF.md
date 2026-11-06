# Integer waves over Z[phi]: a stable reading and its quantum boundary

NON-CANONICAL. Conditional candidate-T, pending independent review.
Reservation #1404. No native-U, particle or registered-gate closure.

## 1. Inputs, attribution and exact domains

Let R=Z[phi], phi^2=phi+1, with the marked real root phi=(1+sqrt(5))/2.
Put phi'=1-phi and s=2-phi=phi^-2. Then s'=1+phi=phi^2, ss'=1,
and 0<s<1/2. The canonical identity J Jbar=s supplies this scalar's
algebraic provenance, not a reason for using it as a wave coefficient.

Use precisely the triangular cochain complex of #1403 at commit
30095fff125e664b2495784504a4524d29d37781. Its offsets are
b0=0, b1=(1,1,0), b2=(1,0,1), b3=(0,1,1). Edges are all translates
of b_j-b_i for i<j; faces are the translates of the eight oriented
triangles +(b_i,b_j,b_k) and -(b_i,b_j,b_k), i<j<k. Counting adjoints,
these field spaces, and P=C^T C are selected mathematical inputs.
They are not the original Z5 Gibbs model or the weighted scalar operator.

On a finite periodic quotient let E be the number of labelled edges.
G is the vertex-to-edge difference and C the triangle circulation.
All entries are integers; CG=0 and G^T P=0. The source proof gives

    spec P(k)={0,8,4-|S|,4-|S|,4+|S|,4+|S|},
    S=1+exp(i k.b1)+exp(i k.b2)+exp(i k.b3).

In particular 0<=P<=8I, and 8 is present. Briefly, in the six-dimensional
exterior-square representation P is unitarily equivalent to
8I-(ee*+zz*)^[2], where e=(1,1,1,1), z=(1,z1,z2,z3). The only potentially nonzero
eigenvalues of ee*+zz* are 4+|S| and 4-|S|. Their pair sums establish
the displayed spectrum, including its degeneracies. This source remains
conditional mathematics, not a physical photon premise.

The new complete state is (A,B) in R^E x R^E, two consecutive field slices.
As integer coefficient arrays this is Z^(4E). The same finite-range rule
makes sense on all infinite-lattice configurations; energy sums below are
claimed on finite quotients or finite-support data at each finite time.
Spatial statements are supplied L2 mathematics, coefficient dynamics is
new L1 comparison mathematics. NOTE-D3-ZPHI-READING names an unadopted
comparison to L5 field histories, not a registered cross-layer gate.

The user supplied the Z[phi] route and the two directional fourth-order
coefficients before this work. They are attributed inputs to the research,
not blind discoveries. The separately reported review files were not
retrieved. No result here depends on the general Laurent/no-cone lemma.

## 2. A genuine local integer automorphism

For a supplied current j in R^E set

    A_next=2A-B-s P A-j,                 T_j(A,B)=(A_next,A).       (1)

Write A=u+phi v, B=u_old+phi v_old and j=j_u+phi j_v. Since
s(u+phi v)=(2u-v)+phi(-u+v), equation (1) is exactly

    u_next=2u-u_old-2P u+P v-j_u,
    v_next=2v-v_old+P u-P v-j_v.                                  (2)

There is no division. The full inverse, for the same supplied j, is
B=2A-A_next-sPA-j. It uses the same local integer operations. Thus T_0
is an automorphism of the whole Z^(4E), not of a prepared subset only.
A supplied-current step is an affine bijection; the current is not yet
produced by a matter subsystem.

In order (u,v), set M_s=[[2,-1],[-1,1]] and Q=2I-M_s tensor P.
The two-slice integer matrix is [[Q,-I],[I,0]]. Its determinant is one.
Q is symmetric, so direct multiplication also proves preservation of the
standard integer symplectic form [[0,I],[-I,0]]. No physical unit of action
is selected by this integer bilinear identity.

P connects only edges sharing a triangle. Both directions of (2) have
finite propagation of dependence on this supplied graph. No SI light speed
or identification of the integer iteration label with physical time follows.

## 3. Total stable reading, conservation and the zero-mode exception

Define D_+(u,v)=u+phi v and D_-(u,v)=u+phi'v, componentwise.
Both are ring homomorphisms. On every complete state, not just a low band,

    D_+ T_j = T_(s,j_+) D_+,
    D_- T_j = T_(s',j_-) D_-.                                    (3)

Here the right sides are the real recurrence (1) at the indicated real
coefficient. On integer coefficient arrays D_+ is injective. It does not
delete half the exact information. Its image is dense rather than discrete.
After real-linear extension, the pair (D_+,D_-) is an invertible change of
coordinates and splits the two conjugate evolutions.

For a nonzero stiffness lambda in (0,8], the plus transfer has polynomial

    t^2-(2-s lambda)t+1.

Since 0<s lambda<4, both roots are distinct and on the unit circle. At
lambda=0 there is a parabolic sector A_n=A_0+nV, not bounded potentials.
Its electric difference is constant and its curvature is zero. No theorem
of bounded full integer orbits or bounded all-potential orbits is asserted.

An exact invariant with values in R is the doubled energy

    Ecal(A,B)=<A-B,A-B>+s<A,P B>.                                 (4)

The product here is ordinary multiplication in the real number ring, not
conjugation between its two real embeddings. Expansion of (1) gives

    Ecal(A_next,A)-Ecal(A,B)=-<j,A_next-B>.                        (5)

Both integer coefficients of Ecal are therefore invariant when j=0.
The proposed real energy is H_+=D_+(Ecal)/2. For d=A_+-B_+ and
m=(A_++B_+)/2,

    2H_+=s||Cm||^2+<d,(I-sP/4)d>
         >=s||Cm||^2+(1-2s)||d||^2 >=0.                          (6)

Equality holds exactly for A_+=B_+ in ker C. This controls the electric
field d and both slice curvatures: CA_+=Cm+Cd/2 and ||Cd||<=sqrt(8)||d||.
Consequently these fields stay bounded in norm on a free finite quotient.
Static gauge and harmonic potentials are retained, not counted as particles.

Let rho_n=G^T(A_n-A_(n-1)). Equation (1) implies exactly in R

    rho_(n+1)-rho_n=-G^T j_n.                                    (7)

It preserves source-free Gauss on every state satisfying it initially.
On a closed quotient total rho is zero. Equations (5) and (7) are field
work and charge accounting with a supplied current. They are not closed
matter-field conservation or an electron source law. Selecting H_+ as
physical energy is itself an unproved reading decision.

## 4. The growing conjugate is real mathematics, not a hidden bounded state

At lambda=8 the minus transfer is t^2+kappa t+1, kappa=6+8phi.
Its expanding multiplier has absolute value

    g=(kappa+sqrt(kappa^2-4))/2,
    18<g<19.                                                     (8)

For the lower bound compare kappa with 18+1/18, using sqrt(5)>11/5;
for the upper bound use sqrt(5)<9/4, so kappa<19<19+1/19.
The function x+1/x is increasing for x>1, proving (8) without a decimal.

An integer lambda-eight eigenvector exists already at zero Bloch momentum:
repeat the edge-type vector (1,-1,0,1,0,0) in every cell, in edge order
01,02,03,12,13,23. It is the boundary row of triangle 012 and P v=8v.
With A_0=0,A_1=v both real embeddings have this nonzero initial datum.
The plus solution oscillates; the minus solution contains the growing root.
Since

    v_coeff=(A_+-A_-)/sqrt(5),
    u_coeff=(phi A_--phi' A_+)/sqrt(5),

the integer coefficient vectors are unbounded, growing at rate g in this
example. No positive-definite real quadratic form on the full coefficient
state can be invariant: its bounded ellipsoids would contradict this orbit.
This does not contradict (6), whose pullback is not positive definite on
the full real coefficient space and is not coercive on its integer lattice.

For a stiffness lambda the conjugate-pair mode polynomial is

    t^4+(3lambda-4)t^3+(lambda^2-6lambda+6)t^2
        +(3lambda-4)t+1.                                        (9)

It is the product of the two conjugate quadratics. For integral lambda
it is the characteristic polynomial of an integer four-dimensional mode
block. For lambda=8 it is
t^4+20t^3+22t^2+20t+1. The expanding and stable conjugates belong to the
same exact integer map. Treating only the bounded embedding as a bounded
integer system would be incorrect.

Every s^m, m>=1, is another unit in R with 0<s^m<1/2. Replacing s by s^m
again gives an integer automorphism with stable plus reading. Stability
and membership in R therefore do not select m=1. The algebraic identity
s=J Jbar alone does not select its dynamical role or an experimental scale.

## 5. Which integer local couplings respect this reading continuously?

For one component take an arbitrary integer matrix
B=[[a,b],[c,d]] acting on the two coefficients. The induced map on the
image Z+phi Z is always a set map because D_+ is injective. The substantive
condition is continuity at zero in the ordinary metric of this image.

Precisely, the following are equivalent:

    (i) the induced additive map is continuous at zero;
    (ii) it extends to a real-linear map on R;
    (iii) b=c and d=a+c;
    (iv) B=[[a,c],[c,a+c]], multiplication by a+c phi in R.         (10)

To prove density, s^m is a sequence of positive image elements tending to
zero; nearest integer multiples of s^m approximate every real number.
A continuous additive map on a dense subgroup is uniformly continuous,
so extends uniquely, by limits of subgroup sequences, to a continuous
additive map on R. Rational approximation then makes the extension x->rx.
The images of 1 and phi give r=a+c phi and
b+d phi=phi(a+c phi)=c+(a+c)phi, which proves (iii). Conversely (iv)
clearly induces continuous multiplication. This proof uses the subspace
topology on the dense image, not an unspoken quotient of integer states.

For finitely many inputs and outputs the same argument on each input
component shows that every integer coefficient block must be multiplication
by an element of R. Thus finite-range integer linear couplings compatible
with a continuous plus reading are exactly matrices over R. Ring-polynomial
local maps are a further sufficient continuous class, not a claim of energy
conservation or a classification of arbitrary nonlinear maps.

The conjugation control B_conj=[[1,1],[0,-1]] fails (10). It sends the
sequence s^m, which tends to zero in the plus image, to (s')^m, which grows
without bound. More generally a nonconforming block has a nonzero minus-to-
plus coefficient in the real two-embedding coordinates, and this same
sequence proves its discontinuity. A future matter coupling cannot silently
mix integer coefficients and still claim a robust version of this reading.
Continuity remains an explicit physical-motivated requirement, not a derived
law of Nature or a complete apparatus admission.

## 6. No smallest excitation energy, even among primitive integer states

Take any allowed source-free state X with H_+(X)>0. Scaling every field
coefficient by the unit s^m commutes with T_0 and with G,C,P. Therefore

    X_m=s^m X,             H_+(X_m)=s^(2m) H_+(X)>0,
    H_+(X_m) -> 0.                                             (11)

Spatial spectral support and all temporal frequencies are unchanged.
Gauss constraints, where satisfied, remain satisfied. The states are
nonzero and pairwise distinct.

This is not removed by requiring primitive integer coordinates. Multiplication
by s on each coefficient pair is M_s, an integer unimodular matrix, and
its inverse is integer too. Applying this block matrix to the complete state
preserves the ideal generated by its integer coordinates, hence their gcd.
If X is primitive as a Z-vector, every X_m is primitive as well.

For a literal finite-mode example the primitive 2x2x2 torus has stiffness
2. Since P is rational, its nonzero eigenspace has a nonzero primitive
integer vector v. Prepare (A_1,A_0)=(v,0). It satisfies Gauss because
G^T P=0 and Pv=2v. It has H_+=||v||^2/2>0 at one fixed spatial stiffness
and frequency. Equation (11) supplies primitive states of arbitrarily
small positive energy at that same frequency, on that same finite torus.
This is an amplitude-scaling result, not the infinite-volume infrared limit.

Hence integer coordinate discreteness and a primitive-state rule do NOT
quantize this field's proposed energy. Declaring unit multiples equivalent
also fails to preserve this energy as an observable: (11) changes it.
For any beta>0 a formal counting sum
sum_X exp(-beta H_+(X)) on a state set containing this sequence diverges,
since its terms tend to one. No counting-based thermal measure is supplied.
These are limitations of the declared classical wave reading, not a denial
of photons or a no-go for a different state/interaction/measurement law.

## 7. Exact fourth-order directional consequence

Let r^2=k_x^2+k_y^2+k_z^2, A4=sum_i k_i^4 and
B4=sum_(i<j) k_i^2 k_j^2. Summing the six integer edge moments gives

    M2=4r^2,                   M4=4A4+12B4.

With L=16-|S|^2, the identity lambda_-(8-lambda_-)=L and the cosine
series yield L=4r^2-M4/12+O(r^6) and therefore

    lambda_-=r^2/2-A4/96-B4/16+O(r^6).                           (12)

These are local Taylor statements with a remainder near zero, not global
quartic approximations. Along a unit axis the quartic coefficient is -1/96;
along a unit body diagonal it is -7/288. The directional difference is
-1/72. Isotropy of the quadratic tangent is not exact lattice isotropy.

The plus wave relation is 4sin^2(omega/2)=s lambda_-. It gives

    omega^2=(s/2)r^2+s(-A4/96-B4/16)+(s^2/48)r^4+O(r^6).        (13)

The time correction is isotropic and cannot remove the directional gap.
Its axis and body-diagonal quartic coefficients are, respectively,

    (8-5phi)/96,             (16-11phi)/288.

Their difference is -s/72, or -1/36 after division by the common quadratic
coefficient c^2=s/2. Equivalently the leading difference of phase speeds,
normalized by c, is -r^2/72. This is an explicit dimensionless consequence
of the comparison, not an SI prediction before scale/time admission.

Both low spatial branches have exactly the same lambda_-, and (1) is the
same scalar polynomial on their two-dimensional eigenspace. There is no
frequency splitting between them wherever that band is separated. This
exact degeneracy is not a global polarization frame at the |S|=0 crossing,
not a proof of physical photon polarization transport, and not a special
claim that only D3 can have two transverse long-wave modes.

## 8. Disposition and the next physical obligation

The construction genuinely replaces a growing-denominator evaluation by a
local, invertible integer-coordinate rule with a total stable field reading.
It does so by allowing unbounded conjugate coordinates, not by disproving
a bounded-orbit theorem. Its source graph, energy, coefficient role and
marked physical interpretation are still selected inputs. It is not U.

The continuous-reading criterion gives a concrete restriction for possible
matter couplings, but (5) still consumes an externally supplied current.
The primitive unit sequence is a direct test that this state space alone
does not contain a smallest one-frequency quantum. A physical successor
must explain the allowed preparation/interaction or excitation law, retain
charge and work balance, and make a further observable prediction without
using the desired photon quantum as its construction input. No electron,
proton, neutron, Planck constant, SI calibration or canonical O closes here.
