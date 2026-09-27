# Rank-four seam: canonicity and inherited-form obstruction

Status: candidate-T, PUBLIC NON-CANONICAL, L1 only.
Author: A. M. Thorn <thorn@twistj.com>. Owner: #1223.
Preregistration and audit pin: 57ad7319ff06d3523eb84706a348727912264626.
All classes, equalities and forms are those of PREREG.md. No Canon promotion.

## 1. The two targets must not be identified

Write F=Q(sqrt5), W=(Lambda^2 A4) tensor F, and retain the marked C, L, K
and beta. The accepted predictive chart is E=E_+, of F-dimension four,
with g=beta|E of real signature (3,1), and A=L|E.
The NEW comparison target is Z=Lambda^2 E, of dimension six, with
B=Lambda^2 A. A four-dimensional subspace of Z is not E.

The inherited exact anchor reconstructs C, K, beta, L, E, A and g from the
marked A4 construction. It is replayed at its frozen hash. The arguments
below are written proofs; the exact matrix audit checks their premises.

Let r=phi^20>1. The source decomposition is

    W = P_+ direct-sum P_- direct-sum H_+ direct-sum H_-,
    dimensions: 2, 2, 1, 1.

Here P=P_+ direct-sum P_-=ker(L^10-I) is the periodic space,
P_+/-=P intersect ker(K-/+sqrt5 I), and
H_+/-=ker(L-phi^(+/-2) I). Use P_+/- here for these TWO-dimensional
periodic spaces, not the full three-dimensional Hodge eigenspaces.
Put T=H_+ direct-sum H_-. Then E=T direct-sum P_+ and E^(perp_beta)=P_-.
On this decomposition L^10 acts by (I4,r,r^-1).

The target decomposition is

    Z = Z0 direct-sum Z_+ direct-sum Z_-,
    Z0 = Lambda^2 T direct-sum Lambda^2 P_+,
    Z_+/- = H_+/- wedge P_+,
    dimensions: 2, 2, 2.

B^10 acts by (I2,r I2,r^-1 I2). All three eigenvalues are distinct in F.

## 2. Complete blocked class, kernels and images

An intertwiner between these diagonal primary decompositions can have only
three nonzero blocks:

    S0: P -> Z0,       v_+: H_+ -> Z_+,       v_-: H_- -> Z_-.

Conversely every such triple is an intertwiner. Thus the full solution
space has F-dimension 8+2+2=12. Rank four is equivalent to S0 being
surjective and v_+,v_- both nonzero. In particular, the rank-four class
is nonempty, and all its kernels and images have precisely the form

    ker S = N,         N any two-plane in P,
    im S = Z0 direct-sum (H_+ wedge ell_+) direct-sum (H_- wedge ell_-),
                       ell_+,ell_- any lines in P_+.

Every pair (N,ell_+,ell_-) occurs: choose an isomorphism P/N -> Z0 and
nonzero maps from each one-dimensional H factor to its selected line.
This is a classification of the whole class, not selected examples.

## 3. The retained five-cycle is a symmetry of the input

Let Q=Lambda^2 C on W, R=Q|E, and D=Lambda^2 R on Z.
C preserves the A4 Gram and has determinant one. Therefore Q preserves
beta and the Hodge operator K. Q commutes with L because C commutes with
I+C^2. It consequently preserves E, so R and D are well-typed. They
preserve g and the target forms defined below. Q has order five.

The actions on the primary blocks can also be obtained without a matrix
census. Diagonalize C over Q(zeta5); its eigenvalues are j^a, a=1,2,3,4.
On the exterior pair (a,b), Q has eigenvalue j^(a+b), while L has
(1+j^(2a))(1+j^(2b)). On the two pairs with a+b=5 the Q eigenvalue is one;
these are T. On the other four pairs the identity 1+j+...+j^4=0 gives
L=-Q. It follows, using the inherited compact factor of A, that

    Q|T = I,
    char(Q|P_+) = x^2+phi x+1,
    char(Q|P_-) = x^2-(phi-1)x+1.

These two quadratics are distinct and have negative real discriminants.
They are irreducible both over F and over R. Neither has eigenvalue one.
On Z0 the action D is identity (both factors are determinant lines),
and on each Z_+/- it is the same irreducible action R|P_+.

This C5 is already a subgroup of the marked A5 axis normalizer. No
assumption that all of A5 preserves a fixed chart is needed.

## 4. No equivariant map and no invariant rank-four image

An equivariant blocked map would satisfy S Q=D S in addition to the
blocked intertwining equation. On the first block this says

    S0 (Q|P-I)=0.

Q|P-I is invertible, so S0=0. On the two other blocks it says

    (R|P_+-I) v_+/-=0.

Again the coefficient is invertible, so both vectors vanish. Consequently

    {S: S L^10=B^10 S and S Q=D S} = {0}.

This excludes every nonzero equivariant map, not just rank four.

There is a stronger image statement, independent of map equality. If an
image from section 2 were D-invariant, its one-dimensional intersections
with Z_+ and Z_- would each be D-invariant. An irreducible real rotation
plane has no invariant real line. Hence

    {im S: rank S=4, S L^10=B^10 S, D(im S)=im S} = empty.

Thus no literal image selector natural under this C5 exists. Adding other
same-target symmetries containing C5 cannot produce such a selector.
This is NOT an exclusion of covariant families or every possible gauge
quotient. In particular, returning an orbit is different from returning a
fixed subspace. A basis chosen for displaying the matrices is not an extra
preferred physical frame that removes this naturality requirement.

## 5. Kernels are less obstructed, but do not select an image

P is the sum of two inequivalent simple F[C5] modules of dimension two.
By semisimplicity and multiplicity one its invariant two-planes are exactly
P_+ and P_-. Each is a possible rank-four kernel. Requiring the kernel to
be beta-negative definite selects P_- relative to the chosen Hodge sign.
Even after this kernel is fixed, both target lines ell_+,ell_- remain free,
and section 4 still excludes an invariant image.

There are infinitely many image classes even under the preregistered finite
C5-orbit equivalence. Fix a basis p1,p2 of P_+ and choose

    ell_+ = F p1,       ell_-(t)=F(p1+t p2),       t in F.

Distinct t give distinct images. A nonidentity power of the order-five
rotation cannot fix the real line F p1. Thus no such power identifies two
members of this family, and equality under the finite action requires t=t'.
Map rescaling does not change the image and cannot remove this freedom.

This is the full-class NONUNIQUE result for that finite equivalence. It is
not a classification under an unspecified larger gauge group.

## 6. Every inherited-form restriction is split or degenerate

Choose h_+,h_- spanning H_+,H_- and a basis p1,p2 of P_+. In the ordered
basis (h_+,h_-,p1,p2), g has block matrix

    [[0,a],[a,0]] direct-sum Gp,
    a != 0,          Gp positive definite,          delta=det Gp>0.

The two null diagonal entries follow from invariance under the distinct
nonunit eigenvalues; nondegeneracy forces a!=0. Let v!=0 be this basis's
volume in units of the frozen vol_E. On Z use the ordered blocks

    Z0: (h_+ wedge h_-, p1 wedge p2),
    Z_+: (h_+ wedge p1, h_+ wedge p2),
    Z_-: (h_- wedge p1, h_- wedge p2).

Define h=Lambda^2 g, the determinant-pairing form on two-vectors, and
 gamma(z,z')=(z wedge z')/vol_E. They have exact block data

    h|Z0 = diag(-a^2,delta),        h(Z_+,Z_-)=a Gp,
    gamma|Z0 = [[0,v],[v,0]],       gamma(Z_+,Z_-)=-v epsilon,
    epsilon=[[0,1],[-1,0]].

All pairings between Z0 and the other blocks vanish. Each Z_+ and Z_-
is totally isotropic for both forms. The lower cross block is the transpose
of the upper, so both six-dimensional forms are symmetric.

Let M be any rank-four image. Write its additional lines as h_+ wedge x
and h_- wedge y, with nonzero x,y in P_+. For any real lambda,mu not both
zero, the restriction of lambda h+mu gamma to M has the block matrix

    [[-lambda a^2, mu v], [mu v, lambda delta]]
                  direct-sum
    [[0,c],[c,0]],
    c = lambda a (x^T Gp y) - mu v det(x,y).

The determinant of the first block is

    -lambda^2 a^2 delta - mu^2 v^2 < 0.

It therefore has signature (1,1). The second block has signature (1,1)
when c!=0, and is the zero two-form when c=0. For EVERY image and EVERY
nonzero member of the frozen natural pencil, the only possibilities are

    (2 positive, 2 negative),
    (1 positive, 1 negative, 2 zero).

Neither (3,1) nor (1,3) occurs. This is a universal real-parameter proof,
not numerical diagonalization or an extrapolated finite scan.

### Exact inequivalent witnesses

Take S0 to identify P_+ with Z0 and kill P_-, and take x=p1. Let
Gp=[[b,c0],[c0,d]], with b>0. For the first map choose y=p1; for the
second choose y=-c0 p1+b p2. Both maps have rank four and the same kernel
P_-. Their restrictions have

    first image:  rank(h)=4, rank(gamma)=2,
    second image: rank(h)=2, rank(gamma)=4.

Indeed x^T Gp y vanishes only for the second choice, while det(x,y)
vanishes only for the first. These images are inequivalent even under ANY
target h-isometry, since the rank of the restricted form is invariant.
The exact matrix audit constructs both witnesses on the original carriers.

## 7. What survives: the direct predictive quotient

The inherited E has a different and legitimate relationship to W. Since
g=beta|E is nondegenerate, there is a unique beta-orthogonal projection onto
E. If i:E->W is its inclusion, its matrix is

    Pi = i (i^T beta i)^-1 i^T beta.

It has Pi^2=Pi, image E and kernel E^(perp_beta)=P_-. E and P_- are
L- and Q-invariant, so Pi commutes with L and Q. No ten-step blocking is
needed for this projection. The metric on W/P_- induced through its unique
orthogonal representative in E is the accepted (3,1) form g.

This is NOT descent of beta on arbitrary representatives: P_- is
nondegenerate, not a radical. Choosing the orthogonal representative is the
explicit metric construction. It is also NOT restriction of h or gamma
from Z. For a chosen S with this kernel, one may transport g to im S;
that produces an S-dependent Lorentz metric, not one of the inherited
restrictions excluded in section 6. It supplies no canonical target image.

Galois conjugation fixes K and T and exchanges P_+ and P_-. It transports
E_+=T+P_+ to E_-=T+P_- and exchanges their projections. In particular,

    Pi_+ Pi_- = Pi_T,
    Pi_+ + Pi_- = I + Pi_T.

The intersection has dimension two and the sum dimension six. Conjugation
is transport between charts with different targets, not an endomorphism of
one fixed E. A physical choice of chart or proof of equivalent physical
readouts is not supplied by these identities.

## 8. Disposition

The unconstrained blocked rank-four class is nonempty and nonunique.
Its C5-equivariant-map and C5-invariant-image subclasses are empty.
Its natural-pencil Lorentz-restriction subclass is empty. These are narrow
mathematical negatives, not a falsification of the native architecture,
the accepted predictive E, the photon program or physical four-dimensionality.

The direct projection onto the already marked E is unique relative to E
and beta and retains the inherited Lorentz metric. That is the surviving
object to distinguish from an arbitrary four-plane in Lambda^2 E.
Its physical interpretation, native-U bridge, relation to the independently
selected photon characteristic and continuum limit remain unproved here.
