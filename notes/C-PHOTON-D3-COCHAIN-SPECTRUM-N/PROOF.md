# D3 triangular cochains: exact spectrum and integer-update boundary

NON-CANONICAL. Conditional candidate-T; no independent review yet.
Spatial L2 mathematics and the separately declared L5 comparison seam
NOTE-D3-COCHAIN-TEMPORAL. No registered gate is passed by this note.
All spaces, orientations and selections are frozen in CONTRACT.md, #1402.

## 1. What the new comparison is, and is not

The input is the D3 nearest-neighbour graph with all elementary triangles,
not a state of native U. Six oriented edge types and eight oriented triangle
types per primitive cell follow from the tetrahedral offsets b0,b1,b2,b3 in
the contract. The six differences are one orientation of the twelve vectors
of squared length two. Every elementary triangle uses three distinct offset
indices, with either sign and an arbitrary translation. This gives the
four triples and two signs; reversed circulation is not another field.
The finite periodic complexes retain these cell types even when endpoints
coincide after taking a small quotient.

G maps a vertex potential to its oriented edge difference. C maps edge
potentials to the circulation around a triangle. Both are integer matrices.
Every vertex contribution cancels on a closed triangle, so

    C G = 0,              P G = 0,              G* P = 0,
    P = C* C >= 0.

This proves a redundancy A -> A+G f of the curvature C A. The uniform
counting adjoints and the quadratic field energy remain choices. Neither
incidence alone nor the algebraic axiom specifies an energy, a probability
measure or a time update. Our P is not the registered weighted scalar A_F0.

The use of cochains and gauge-preserving discrete actions has substantial
prior literature; see Stern et al., arXiv:0707.4470 and arXiv:0803.2070.
Those papers are methodological context, not a theorem about this P or an
import that selects it from J. No claim of novelty for discrete Maxwell
integration as a general method is made.

## 2. Complete Bloch spectrum by a four-dimensional exterior calculation

Let z0=1 and z_i=exp(i k.b_i), and write e=(1,1,1,1), z=(z0,z1,z2,z3).
Identify the six edge amplitudes with the ordered basis of Lambda^2 C^4.
Let B:Lambda^2 C^4 -> Lambda^3 C^4 be wedge multiplication by e:

    (B x)_ijk = x_jk - x_ik + x_ij.

For an edge amplitude a_ij use the unitary change x_ij=z_i a_ij.
The positive triangle has circulation

    z_i a_ij + z_j a_jk - z_i a_ik = (B x)_ijk.

The negative triangle has circulation

    -z_j^-1 a_ij - z_k^-1 a_jk + z_k^-1 a_ik.

Consequently its map in x variables is -B U, where

    U = Lambda^2 diag(z0^-1,z1^-1,z2^-1,z3^-1).

The counting adjoint of wedge multiplication L_u is contraction i_u.
The elementary exterior identity i_u L_u + L_u i_u=||u||^2 I gives

    B*B = 4 I - L_e i_e.

Since diag(z_i^-1) is unitary and sends z to e, P is unitarily equivalent to

    P' = 8 I - L_e i_e - L_z i_z.

For a Hermitian operator H on C^4 let H^[2] act on a wedge by
H^[2](u wedge v)=(H u) wedge v+u wedge (H v). For H=e e*+z z*,

    H^[2] = L_e i_e + L_z i_z.

Put S=e*z=1+z1+z2+z3 and R=|S|. The possibly nonzero eigenvalues of H are the
eigenvalues of the two-column Gram matrix [[4,S],[conjugate(S),4]], namely
4+R and 4-R. The other two eigenvalues are zero. Taking all pairwise sums
on Lambda^2 and subtracting from eight proves, for EVERY character,

    spec P(k) = {0, 8, 4-R, 4-R, 4+R, 4+R},
    det(tI-P(k)) = t(t-8)[(t-4)^2-R^2]^2.                 (1)

The degenerate cases are included. At R=4 the multiplicities are 0^3,8^3;
at R=0 they are 0^1,4^4,8^1. There is no globally separated lower two-band
bundle at the R=0 crossing.

Equality in R<=4 requires all z_i equal, and z0=1 then makes every z_i=1.
This is one reciprocal-lattice point on the D3 character torus, not two
photons or a polarization count. Off that point e and z are independent.
The kernel of P' is their wedge e wedge z. In the original edge coordinates,

    G(k)_ij = z_j/z_i - 1,
    (diag(z_i) G(k))_ij = z_j-z_i = (e wedge z)_ij.

Thus ker C(k)=im G(k) is exactly one-dimensional at every nonzero character.
It is an actual gradient null direction, not a removed nonzero eigenmode.
At the zero character G=0 and ker C has dimension three: the harmonic
constant potentials must be retained separately.

For 0<R<4 set W=span(e,z)^perp. It has dimension two. If u_+,u_- are
normalized H eigenvectors with eigenvalues 4+R,4-R, respectively, then

    span(e wedge z):     eigenvalue 0;
    u_+ wedge W:         eigenvalue 4-R, dimension 2;
    u_- wedge W:         eigenvalue 4+R, dimension 2;
    Lambda^2 W:          eigenvalue 8, dimension 1.

This is the full six-component decomposition. There are FIVE non-gauge
configuration modes at a nonzero character, not only two. Exactly two of
those become soft near k=0. The other three remain gapped. They are not
identified here with an electron, proton, neutron or any physical mass.

## 3. Isotropic transverse tangent, derived rather than stipulated

Write v_ij=b_j-b_i. Direct integer outer products give

    sum_(i<j) v_ij v_ij^T = 4 I_3.                       (2)

Let L(k)=16-R^2=2 sum_(i<j)(1-cos(k.v_ij)). If r=|k|,

    0 <= 4r^2-L(k) <= (2/3) r^4.                        (3)

Indeed 0<=t^2-2(1-cos t)<=t^4/12 for every real t. Summing and using
(k.v)^2<=2r^2 with (2) bounds the sum of fourth powers by 8r^4.
With lambda_-=4-R one has lambda_-(8-lambda_-)=L. Also
lambda_-=L/(4+R)<=r^2, so

    -r^4/12 <= lambda_-(k)-r^2/2 <= r^4/8.             (4)

This is an all-real lifted-k bound; it proves the local coefficient 1/2
and bounded-set convergence after rescaling, without a numerical fit.
It is not a state-limit or physical-continuum theorem.

The zero-character kernel is the image of the ordinary three-vector map

    F(a)_ij = v_ij.a,        ||F(a)||^2 = 4 |a|^2.

For k=epsilon n with a fixed unit direction n, G(k)=i epsilon F(n)+O(epsilon^2).
The spectral separation from the three eigenvalues tending to eight implies
that limits of normalized low-eigenvalue vectors lie in im F. They are
orthogonal to G(k); dividing that orthogonality by epsilon and using (2)
gives n.a=0. Conversely in the exterior decomposition above, u_+ tends to
e/2 and W tends to the orthogonal complement of e and (b_i.n)_i. Thus the
entire limiting low subspace is exactly F(n^perp), of dimension two.

The two transverse long-wave modes have therefore been derived from this
specified incidence/metric problem. They were not put in as two scalar copies.
This conclusion is conditional on the new cochain inputs in Section 1, and
is not the original Z5 Gibbs-phase or physical-photon conclusion.

## 4. Gauss law from a declared action, not an informal polarization deletion

On a finite periodic complex introduce edge A_n and vertex phi_n, with

    E_(n+1)=A_(n+1)-A_n-G phi_n,
    B_n=C A_n.

For a declared positive rational sigma choose the discrete action

    S = sum_n [ ||E_(n+1)||^2/2 - sigma ||B_n||^2/2
                - <j_n,A_n> + <rho_(n+1),phi_n> ].       (5)

Time endpoints are fixed in variations. The source fields are prescribed
comparison inputs, not a derived matter evolution. Variation in phi_n and
A_n yields, respectively,

    G* E_(n+1)=rho_(n+1),
    E_(n+1)=E_n-sigma P A_n-j_n.                        (6)

The transformations A_n -> A_n+G chi_n and
phi_n -> phi_n+chi_(n+1)-chi_n leave the field action unchanged. The source
terms change, apart from endpoint terms, by

    sum_n <rho_n-rho_(n+1)-G*j_n,chi_n>.

Thus the required source compatibility is exactly

    rho_(n+1)-rho_n = -G*j_n.                           (7)

Independently, applying G* to (6) proves (7), because G*P=0.
This makes charge/Gauss preservation part of the evolution at every step.
On a closed periodic complex total rho is zero since G 1=0; isolated total
net charge is not admitted without changing the domain or boundary account.

In temporal gauge phi_n=0, E_n=A_n-A_(n-1), equation (6) is exactly

    A_(n+1)=2 A_n-A_(n-1)-sigma P A_n-j_n.              (8)

Given j_n, the complete two-slice inverse is
A_(n-1)=2 A_n-A_(n+1)-sigma P A_n-j_n. No postprocessing erasure is used.
The matrix P only links edges belonging to a common elementary triangle.
Hence (8) has a finite dependency cone in this declared edge-adjacency
graph. Neither its radius nor n is identified with an SI distance/time.

## 5. Exact work balance and the stability boundary

For two successive slices define the comparison energy

    H(a,b)=||a-b||^2/2 + (sigma/2)<a,P b>.

Writing d=a-b and m=(a+b)/2 gives

    H(a,b)=(sigma/2)<m,P m>
           +(1/2)<d,(I-sigma P/4)d>.                  (9)

Equation (1) implies 0<=P<=8 I on every finite periodic complex. Therefore
for 0<sigma<1/2 the expression is nonnegative, and vanishes exactly when
a=b and C a=0. Static gauge and harmonic potentials are legitimate zero
energy configurations. The physical interpretation of this invariant and
its normalization is NOT supplied by choosing (5).

For the forced recurrence a_next=2a-b-sigma P a-j, direct expansion yields

    H(a_next,a)-H(a,b) = -<j,a_next-b>/2.               (10)

For j=0 this is exact conservation. With j prescribed it is an exact work
account, not conservation of a closed matter-field system: the matter
source of that work has not been constructed.

At a stiffness eigenvalue lambda the free temporal polynomial is

    t^2+(sigma lambda-2)t+1.

For 0<sigma<1/2 and lambda>0 its roots are distinct reciprocal conjugates
on the unit circle. The zero-stiffness sector is parabolic and potentials
can drift linearly there; no boundedness assertion for the entire potential
is made. The low-frequency relation is

    4 sin^2(omega/2)=sigma lambda_-(k),
    omega^2=(sigma/2)|k|^2+O(|k|^4) near zero.

Thus the speed coefficient is determined within the comparison, not
assumed to be the one in the old scalar dictionary. Requiring that old
unit tangent coefficient while retaining these same spatial/time units
would require sigma=2, outside the stable interval. This is another reason
not to identify the two constructions silently.

## 6. The naive integer step fails, and a fixed-lattice relabeling cannot cure it

For sigma=1, (8) with zero source is an integer matrix of determinant one
on the full two-slice integer field lattice. Nevertheless the eigenvalue
lambda=8, present at every character, has temporal polynomial

    t^2+6t+1,
    t=-3 +/- 2 sqrt(2).

One root has modulus greater than one. This is exponential growth in a
non-gauge sector, not a zero-mode drift. The finite audit retains a nonzero
integer eigenvector and the scalar sequence

    0,1,-6,35,-204,1189,-6930,40391,-235416,1372105.

Reversibility alone does not make the proposed wave step stable.
The expected negative result is not repaired by the positive rational
comparison sigma=1/4, which fails to preserve arbitrary raw integer fields.

There is a stronger algebraic consequence of the same frozen spectrum.
On the L=2 primitive torus P has eigenvalue two. For ANY rational
0<sigma<1/2, that sector of (8) has the irreducible rational polynomial

    t^2-(2-2sigma)t+1,           1<2-2sigma<2.          (11)

Its nonreal roots cannot be algebraic integers: their monic irreducible
polynomial has a noninteger rational coefficient. Any linear map preserving
a full-rank discrete lattice has an integer matrix in a lattice basis, so
all its eigenvalues are algebraic integers. Consequently no change of
basis, nor ANY fixed full-rank discrete lattice in this finite real state
space, can make the stable rational comparison a lattice-preserving map.
This is a proof using the already frozen rational spectrum, not an extra
numerical run. It excludes neither prepared proper subspaces nor a different
microscopic automaton, extra state, nonlinear rule or different temporal law.

For sigma=a/b, a,b positive integers, the source-free rational recurrence
can be evaluated in integers using N_n=b^n A_n:

    N_(n+1)=(2b I-a P)N_n-b^2 N_(n-1).                 (12)

For integer initial A0,A1 the initial N1=b A1 must be retained. Reading A_n
requires the scale b^n. Inverting (12) requires division by b^2 and the
appropriate divisibility conditions. On unrestricted numerator pairs its
state-matrix determinant is b^(2E), where E is the number of edge variables,
not one when b>1. Thus it is a forward integer evaluation, not a bijective
native integer completion. Those scale/domain resources cannot be omitted.

## 7. Finite certificate and explicit negative controls

On the complete L=2 quotient, G has rank seven and C rank thirty-eight.
The 48-dimensional P has the exact spectral multiplicities

    eigenvalue        0     2     4     6     8
    multiplicity     10     8    12     8    10.

These also follow from (1): among the eight characters R=4 occurs once,
R=2 four times, and R=0 three times. The ten zero modes are seven gradients
and three harmonic constants. This finite count is not the count of
physical particles or of continuum polarizations.

Omitting all negative triangle types leaves C=B D_+, of rank three per
character, rather than five generically; its L=2 rank is twenty-four.
Two additional zero directions at nonzero momentum then survive. Reversing
one edge sign in a face breaks CG=0. Omitting the Gauss variation in (5)
allows A_n=n G f with zero curvature but nonzero G*(A_n-A_(n-1)); that is
not a source-free state satisfying the full comparison equations.

The audit constructs the real-space integer matrices independently of the
closed Bloch formula, checks all 64 fourth-root Bloch triples with Gaussian
integer arithmetic, and checks 16 free and 16 forced complete steps. These
finite checks support the formulas; the exterior proof supplies the
all-character scope. Both routes were written by the same coordinator and
are not blind independent confirmation.

## 8. Scientific disposition

The constructive return is exactly two degenerate transverse low branches,
a full accounting of the other branches, a local comparison evolution and
an exact charge/work equation. The negative return is the instability of
the naive integer step and the fixed-lattice obstruction for its stable
rational version. Neither is a no-go for TWIST-J as a whole.

A physical photon requires additional results not present here: selection
of the relevant microscopic source/action, a stable native update and
reading, the actual massless phase where applicable, quantum excitation
and energy-frequency normalization, and compatible matter interaction.
The original selected Z5 model, P1/P2/S7, the original scalar characteristic,
and all live photon owners keep their prior scopes and statuses.

Next use must connect a real native state/update to this or another
independently admitted transverse field, or demonstrate why that class is
inadmissible. Calling a stable rational simulation an integer derivation,
or calling one of the three gapped branches an electron, would not do so.

Primary methodological context (no redistributed source files):
- Stern, Tong, Desbrun, Marsden, https://arxiv.org/abs/0707.4470.
- Stern, Tong, Desbrun, Marsden, https://arxiv.org/abs/0803.2070.
- Tong, QFT, section 6, https://www.damtp.cam.ac.uk/user/tong/qft/qfthtml/S6.html.
