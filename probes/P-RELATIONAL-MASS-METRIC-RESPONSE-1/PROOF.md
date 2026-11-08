# Relational mass and its complete planar metric response

Status: PROSPECTIVE, NON-CANONICAL, NEW_DECLARED L1.
Candidate: P-RELATIONAL-MASS-METRIC-RESPONSE-1.
Public ownership: https://github.com/mathorn1973/twist-j/issues/1684.
This is an analytical proof draft. No scientific program, import or finite
fixture evaluation was used to derive the statements below. Universal
claims rest on the proofs, not on a bounded audit.

## 1. Declared carrier and the new metric dependence

Let j be the chosen complex primitive fifth root, j=exp(2*pi*i/5), and set

    K=Q(j), F=Q(phi), phi=-j^2-j^3, phi^2=phi+1,
    gamma=phi-1=j+j^4, gamma^2=1-gamma=2-phi.

Complex conjugation is c(j)=j^4. For z in K write

    h(z)=z*c(z), Re(z)=(z+c(z))/2.

The chosen real place has phi>1. The automorphism sigma_2(j)=j^2 restricts
to tau(phi)=1-phi on F and commutes with complex conjugation. Counts
n_0,...,n_4 are nonnegative integers and remain fixed in every metric
variation. Define

    N=sum_k n_k, Z=sum_k n_k*j^k, W=sum_k n_k*j^(2k),
    D=N^2-h(Z), Q=N*W-Z^2.                         (1)

The count model and D are the mathematical carrier of the local reference
package C-RELATIONAL-MASS-1. Its comparison with physical null momenta is
not assumed to be a native physical realization here.

In this probe the individual planar covectors are fixed. A positive
definite inverse spatial metric G changes their lengths; the covectors
are NOT renormalized to unit length after changing G. This is a new
declared dependence, not a consequence of the cyclotomic ring alone.

It is convenient to give their components in the F-basis (1,j). They are

    u_0=(1,0), u_1=(0,1), u_2=(-1,gamma),
    u_3=(-gamma,-gamma), u_4=(gamma,-1).             (2)

Indeed j^2=gamma*j-1, j^3=-gamma-gamma*j, and j^4=gamma-j.
The Euclidean reference quadratic form in these components is

    G0=[[1,gamma/2],[gamma/2,1]],
    det(G0)=1-gamma^2/4=(2+phi)/4>0.                (3)

If A maps the components (x,y) to the ordinary real and imaginary
coordinates of x+y*j, then A^T A=G0. Thus u_k^T G0 u_k=1 and the actual
reference directions A*u_k are the fifth-root unit directions.

For any real symmetric positive definite 2-by-2 matrix G, put

    epsilon_k(G)=sqrt(u_k^T G u_k)>0,
    E(G)=sum_k n_k*epsilon_k(G),
    P=sum_k n_k*u_k,
    D_G=E(G)^2-P^T G P.                            (4)

P is fixed under the variation. At G0, E=N, the complex representative
of A*P is Z, and D_G0=D. The empty preparation has E=D_G=0. All matrix
derivatives below use symmetric increments S and the Frobenius pairing
tr(R*S), so the derivative with respect to a single shared off-diagonal
coordinate is twice the corresponding off-diagonal matrix entry.

Equations (2)-(4) describe one marked plane, a fixed count preparation,
and an inverse metric. No spacetime metric, volume factor, local source
distribution, Lorentz closure or physical energy unit is inferred.

## 2. The arithmetic conjugate is the second angular moment

Because the counts are rational integers, sigma_2 fixes every n_k. Hence

    W=sigma_2(Z), h(W)=tau(h(Z)),
    tau(D)=N^2-h(W).                               (5)

The first equality is special to rational/integer weights. For arbitrary
real weights the two angular moments must instead be regarded as separate
data; no Galois action on arbitrary real coefficients is implicit.

For context, expansion of D cancels all same-direction terms and gives

    D=sum_(r<s) n_r*n_s*h(j^r-j^s)
     =(3-phi)*sum_k n_k*n_(k+1)
       +(2+phi)*sum_k n_k*n_(k+2),                  (6)

with indices modulo five. Each unordered pair appears once. Its tau
conjugate interchanges 3-phi and 2+phi. Both coefficients are positive
at the chosen place, so D=0 exactly when at most one direction is
occupied. This agrees with the metric argument below and does not
identify an arithmetic field norm with a physical mass.

## 3. Energy response and mass-square response are different matrices

Differentiating a positive square root gives

    d epsilon_k[G;S]=(u_k^T S u_k)/(2*epsilon_k).

Define

    T_G=sum_k (n_k/epsilon_k)*u_k*u_k^T,
    R_G=E*T_G-P*P^T.                               (7)

Then direct differentiation of (4) yields

    dE[G;S]=(1/2)*tr(T_G*S),
    dD[G;S]=tr(R_G*S).                             (8)

Thus T_G/2 is the derivative of the declared total energy, whereas R_G
is the derivative of its mass-square form. Substituting one for the
other would change the variational problem. A matter Hamiltonian or
common action has to state which function is coupled and how; (8)
does not by itself declare a gravitational stress tensor.

The contractions are exact:

    tr(G*T_G)=E,
    tr(G*R_G)=E^2-P^T G P=D_G.                     (9)

They also follow from E(lambda*G)=sqrt(lambda)*E(G) and
D_(lambda*G)=lambda*D_G for lambda>0. These are homogeneity identities
under metric scaling, not time-reparametrization or conservation laws.

## 4. Positive covariance form and complete rank classification

For occupied directions write

    w_k=n_k*epsilon_k>0, v_k=u_k/epsilon_k.

Then E=sum w_k, P=sum w_k*v_k and T_G=sum w_k*v_k*v_k^T.
Expanding both sides proves the weighted covariance identity

    R_G=sum_(r<s) w_r*w_s*(v_r-v_s)*(v_r-v_s)^T.    (10)

In particular R_G is positive semidefinite. For any real column x,

    x^T R_G x=sum_(r<s) w_r*w_s*(x^T(v_r-v_s))^2.

Consequently its kernel consists exactly of those x for which x^T v_k
is the same for every occupied direction. Its rank is the affine
dimension of the occupied normalized covectors.

The vectors v_k are distinct and lie on the strictly convex ellipse
v^T G v=1. A line meets this ellipse in at most two points. Therefore

    number of occupied directions  0 or 1     2       at least 3
    rank R_G                         0        1           2.      (11)

This includes the empty case directly from (7). By (9), positive
definiteness of G implies D_G=0 exactly when R_G=0, hence exactly when
at most one direction is occupied. D_G>0 for every other preparation.

For positive-semidefinite S, equation (8) gives dD[G;S]>=0. Integrating
along G+t*S, 0<=t<=1, proves monotonicity in the positive-semidefinite
order. Strictness for a given rank-one strain x*x^T is characterized by
the kernel above. In particular a two-direction preparation has positive
mass square but a nonzero blind rank-one strain direction. With at least
three occupied directions every nonzero positive-semidefinite strain
has strictly positive first mass-square response.

The rank of T_G is different: it is the linear dimension of the occupied
u_k. No two distinct fifth-root directions are parallel, since fifth
roots contain no antipodal pair. Thus T_G has rank zero for no support,
rank one for single support, and rank two for every support of size at
least two. Confusing T_G and R_G would already fail on two directions.

## 5. Concavity and all flat second-variation directions

Expanding (4) by unordered pairs gives

    D_G=2*sum_(r<s) n_r*n_s*
        (epsilon_r*epsilon_s-u_r^T G u_s).          (12)

Along G(t)=G+t*S, in any open interval where G(t)>0, set at t=0

    beta_k=(u_k^T S u_k)/(u_k^T G u_k).

For f(t)=sqrt((a+t*b)*(c+t*d)), direct differentiation gives

    f''(0)=-(sqrt(a*c)/4)*(b/a-d/c)^2.

The remaining term in each pair of (12) is linear in G. Therefore

    d^2 D[G;S,S]=-(1/2)*sum_(r<s) n_r*n_s*
        epsilon_r*epsilon_s*(beta_r-beta_s)^2<=0.   (13)

This proves concavity of D_G on the positive-definite cone. The full
bilinear Hessian follows by polarization; its quadratic kernel suffices
to classify equality.

For support zero or one, D_G is identically zero. For support two,
equality in (13) is equivalent to equality of the two occupied beta_k.
For support at least three, equality forces all occupied beta_k=c for
one real c. Hence

    u_k^T(S-c*G)u_k=0

on at least three distinct projective lines. A nonzero homogeneous binary
quadratic polynomial has at most two distinct real projective zero
directions. It follows that S=c*G. Conversely S=c*G gives beta_k=c
for every k and equality in (13). Thus, with at least three occupied
directions, overall scaling is exactly the Hessian kernel. Strict
concavity away from scaling concerns D_G, not an unstated action.

## 6. Exact determinant identities at the reference metric

At G0 define the F-valued component matrices

    T=sum_k n_k*u_k*u_k^T,
    R=N*T-P*P^T.                                   (14)

Their matrices in orthonormal physical coordinates are
T_o=A*T*A^T and R_o=A*R*A^T. For a unit complex direction z=x+i*y,

    x^2+y^2=1, (x^2-y^2)+2*i*x*y=z^2.

Summing this identity over the count preparation gives

    tr(T_o)=N,
    (T_o)11-(T_o)22+2*i*(T_o)12=W.                 (15)

The same calculation for (A*P)*(A*P)^T gives trace h(Z) and complex
anisotropy Z^2. Consequently

    tr(R_o)=D,
    (R_o)11-(R_o)22+2*i*(R_o)12=Q=N*W-Z^2.        (16)

For every real symmetric 2-by-2 matrix B, with trace b and complex
anisotropy q=B11-B22+2*i*B12, expansion shows

    4*det(B)=b^2-q*c(q).

Using (5), (15), (16), and det(A)^2=det(G0), one obtains the exact
component-basis identities

    4*det(G0)*det(T)=N^2-h(W)=tau(D),
    4*det(G0)*det(R)=D^2-h(Q).                     (17)

Thus the other arithmetic place of the mass-square form is exactly four
times the determinant of the reference moment matrix T_o in an
orthonormal frame. Since the actual energy derivative is T_o/2, the
equivalent derivative statement is tau(D)=16*det(T_o/2). In the declared
F-basis the factor det(G0) is essential. Omitting it changes the result.

The first identity concerns T and the second R. At support two, T is
positive definite while R has rank one: tau(D)>0 but D^2=h(Q). At
support at least three, both are positive definite and D^2>h(Q). At
support at most one, D=Q=0 and det(T)=det(R)=0. These are exact
consequences of (11), not numerical eigenvalue tests.

No assertion extends the particular tau(D) identity to arbitrary G
without also specifying how the arithmetic automorphism acts on the
metric. Here (17) is explicitly a reference-metric identity.

## 7. Complete data and the fixed-spatial-sum ambiguity

Every cyclotomic integer Z has a unique integral expansion

    Z=z_0+z_1*j+z_2*j^2+z_3*j^3.

For a count vector with this Z, comparison after eliminating
j^4=-1-j-j^2-j^3 gives z_i=n_i-n_4, i=0,...,3. Therefore the full
integral fibre is

    n=(z_0+r,z_1+r,z_2+r,z_3+r,r),                 (18)

where r is an integer chosen so every entry is nonnegative. If N is
also supplied, it fixes r uniquely:

    r=(N-z_0-z_1-z_2-z_3)/5.                       (19)

Conversely, whenever this value is integral and every displayed count
is nonnegative, (18) is an admitted count vector with exactly those
N and Z. Equations (18)-(19) are therefore both reconstruction and
an exact admission criterion. In particular the complete pair (N,Z)
determines T, R and the full metric-dependent E(G), D_G of (4).

The word complete is algebraic: Z is an exact cyclotomic element, not
an approximate measured complex number. No physical finite-precision
decoder or robustness bound is supplied by (18)-(19).

Since sum_k j^k=sum_k j^(2k)=0, adding r whole pentagons leaves Z
and W unchanged and raises N by 5*r. The orthonormal moment of one
whole pentagon has trace five and zero anisotropy, so

    sum_k u_k*u_k^T=(5/2)*G0^(-1).

Hence, whenever both fibre members have nonnegative counts,

    T(n+r*1)=T(n)+(5*r/2)*G0^(-1).                 (20)

Thus Z alone fixes the anisotropic part of the first energy response,
but not its isotropic part or total energy. Adding a whole pentagon
adds energy; it is not an energy-conserving process of an isolated
system. Likewise Z=0 forces all five counts equal to one common
nonnegative integer. Those are the only rest preparations P=0 within
this marked five-ray, unit-reference-energy carrier.

## 8. Scalar mass does not determine directional response

Cyclically rotating the marked count preparation by r sends

    Z -> j^r*Z, W -> j^(2r)*W, Q -> j^(2r)*Q,
    N -> N, D -> D.                                (21)

It preserves the scalar mass square in both arithmetic places but in
general rotates the energy and mass-response anisotropies. For any two
distinct occupied unit directions u,v, each with count one,

    Q=2*(u^2+v^2)-(u+v)^2=(u-v)^2!=0.

A nontrivial cyclic rotation multiplies Q by j^(2r)!=1. Thus these
preparations have the same N,D but different R in a fixed marked
reference frame. By the nondegeneracy of the Frobenius pairing, some
fixed symmetric strain distinguishes their first responses.

This is a statement about incomplete scalar input at a fixed marking.
If the preparation and metric are rotated together, (4) transforms
covariantly and the corresponding scalar predictions agree. Different
coordinate descriptions of that joint rotation are not being declared
physically inequivalent. The missing anisotropy is supplied by (N,Z)
in the exact count class, not by selecting a preferred orientation
after examining a desired output.

## 9. Exact strain parametrization over the number fields

Use the following no-conjugate convention for a real quadratic strain:

    H_(alpha,beta)(z)=alpha*h(z)+Re(beta*z^2),
    alpha in F, beta in K.                         (22)

Here H denotes both the form and its symmetric matrix in the F-basis
(1,j). Polarization gives its exact entries:

    H=[[alpha+Re(beta), alpha*gamma/2+Re(beta*j)],
       [alpha*gamma/2+Re(beta*j), alpha+Re(beta*j^2)]].       (23)

All these entries lie in F. For a fixed occupied direction define

    a_k=u_k^T H u_k=alpha+Re(beta*j^(2k)).           (24)

At G0+epsilon*H the squared lengths are exactly 1+epsilon*a_k.
The first variations follow either from (8) or from summing (24):

    delta E=(alpha*N+Re(beta*W))/2,
    delta D=alpha*D+Re(beta*Q).                     (25)

For comparison, in an orthonormal frame beta=b+i*c makes the strain
matrix [[alpha+b,-c],[-c,alpha-b]]. This verifies the sign and the
factor two in the off-diagonal contribution of (25). A convention
using Re(conj(beta)*z^2) would require conjugating beta everywhere;
the present proof uses (22) consistently.

The form (22) represents the three real components of a symmetric
planar strain. Restricting alpha to F and beta to K supplies the
exact field-valued class used for rational/cyclotomic formal audits.

## 10. Formal coefficients and the unavoidable fourth-order term

For sufficiently small real epsilon, G0+epsilon*H remains positive
definite, and equivalently one may work as a formal power series in
epsilon over F. The binomial identity gives

    sqrt(1+epsilon*a)
      =1+(a/2)*epsilon-(a^2/8)*epsilon^2
         +(a^3/16)*epsilon^3-(5*a^4/128)*epsilon^4
         +O(epsilon^5).                            (26)

No finite nonzero square root must be evaluated to obtain these
coefficients. Let [epsilon^r] denote a coefficient, not an r-th
derivative. Then

    [epsilon]E=(sum_k n_k*a_k)/2,
    [epsilon^2]E=-(sum_k n_k*a_k^2)/8,
    [epsilon^3]E=(sum_k n_k*a_k^3)/16,
    [epsilon^4]E=-(5/128)*sum_k n_k*a_k^4.           (27)

All a_k are real at the chosen embedding. Nonnegative counts imply
that the fourth coefficient is strictly negative exactly when some
occupied direction has a_k!=0. It vanishes exactly when all occupied
length squares are constant along this strain, in which case the
entire E(G0+epsilon*H) is constant. Cancellation of the first response
does not remove the fourth-order obstruction.

For support at least three, the quadratic form H can vanish on every
occupied direction only if H=0. Consequently every nonzero strain has
a strictly negative fourth coefficient for such a preparation. For
smaller support nonzero strains invisible on the occupied directions
are allowed and are covered by the preceding exact criterion.

The same obstruction holds at any positive-definite base G_star, whether
or not a proposed metric map passes through G0. Writing
b_k=u_k^T H u_k and epsilon_k_star=sqrt(u_k^T G_star u_k), the same
binomial identity gives

    [epsilon^4]E(G_star+epsilon*H)
       =-(5/128)*sum_k n_k*b_k^4/epsilon_k_star^7.  (27a)

Every denominator is positive, so this coefficient is strictly negative
exactly when some occupied b_k is nonzero. Formula (27a) is an analytical
identity; the exact F-valued formal coefficient class is (27) at G0.

Squaring E and subtracting the linear metric term P^T(G0+epsilon*H)P
also gives

    [epsilon]D=alpha*D+Re(beta*Q),
    [epsilon^2]D=((sum n_k*a_k)^2-N*sum n_k*a_k^2)/4
       =-(1/4)*sum_(r<s) n_r*n_s*(a_r-a_s)^2.       (28)

Thus the second derivative is twice the second coefficient in (28),
consistent with (13). All formal products and coefficients at G0 in
(24)-(28) belong to F and can be checked exactly without floating point.

## 11. What this permits and forbids in a gravity continuation

The new choice (4) gives one definite energy dependence on a planar
inverse metric. It supplies an exact variational response, not a
complete interacting gravity model. In particular:

1. Coupling E(G) in a common Hamiltonian or action produces the energy
   derivative T_G/2. Coupling D_G instead produces R_G. Those choices
   are different, and the determinant identity alone does not select
   either as a gravitational source or fix a local source projector.
2. Suppose the old scalar gravitational Hamiltonian H_g is nonnegative
   on its real carrier, and an independently varied lapse multiplies
   exactly H_g+E(G), with no additional signed term. Its lapse equation
   is H_g+E(G)=0. Every nonempty admitted count preparation has E(G)>0,
   so no such sourced stationary state exists. The new relational mass
   does not remove that conditional free-lapse obstruction. A clock
   momentum, an indefinite contribution, another interaction or the
   fixed-total-lapse variational problem is an additional declaration.
3. If G depends affinely on the old metric coordinates and some direction
   in those coordinates induces a strain H with u_k^T H u_k!=0 on at
   least one occupied direction, (27a) proves that E(G) is not a
   quadratic polynomial in those same coordinates. Adding it to an
   old quadratic Hamiltonian therefore does not preserve that old
   quadratic Hamiltonian or its derived fixed linear phase equations.
   The nonzero fourth coefficient cannot be cancelled by a quadratic
   term. A proposed cancellation or a new coordinate construction
   would need its own explicit definition and proof. This is not a
   no-go for nonlinear canonical descriptions or for all gravity.

In particular one cannot insert this source and simply inherit the
previous M0*exp(s*K) scalar flow, its exact Ward identities, or its
closed constraint algebra. Their persistence would be a new theorem
about a newly declared joint action. The present proof supplies no
such action or dynamics.

## 12. Scope of the result

The proved chain is exact count preparation -> chosen metric-dependent
energy -> energy and mass-square responses -> rank, concavity and
arithmetic determinant identities. The arithmetic conjugate controls
the determinant of the reference moment matrix T_o; scalar mass alone
remains insufficient for its marked directional information.

The result stays within one declared planar inverse-metric family,
fixed covectors and nonnegative integer counts. No native realization,
physical energy unit, Lorentz closure, spacetime dynamics, stable
localized particle, physical source projector, common action, gravity
field equation, continuum limit or unnamed cross-layer lift follows.
The two Galois places remain arithmetic embeddings, not two physical
frames or species. Equality of inertial and gravitational mass is not
assumed or proved by differentiating the chosen function.

The full universal assertions are established above. Finite exact
counts and formal coefficients may audit their implementation, but
cannot replace the stated proofs or extend these boundaries.
