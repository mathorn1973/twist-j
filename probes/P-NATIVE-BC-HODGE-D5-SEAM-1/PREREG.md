# PREREG: P-NATIVE-BC-HODGE-D5-SEAM-1

FORMAL PUBLIC PROBE. Action layer L1. Issue #1061.
Base: Public Canon v89 main 5422e122f3b29b1810011a92be3c9d1c90006049.

## Frozen carriers

Native tangent carrier X=F_5^6 uses coordinate order
(p1,p4,p1p,p4p,q,r) and the exact linear parts of the declared affine
checkpoint generators. Matrix multiplication uses column-vector composition.
Let B_n=Lin(b), C_n=Lin(c), A_n=Lin(a), D_n=E_n=-I and P_n=B_n C_n.

Hodge carrier is W=(Lambda^2 A4) tensor F_5. Let C_4 be the marked coordinate
five-cycle, A_h=Lambda^2 C_4, and let s:k->-k on the five labels. Since s is
the even permutation (1 4)(2 3), S_h=Lambda^2 s lies in the marked A5 action
and satisfies S_h A_h S_h=A_h^-1. The two target reflection pairs are frozen
as (S_h,S_h A_h) and (S_h,S_h A_h^-1). Kbar is the accepted integral Hodge
operator reduced mod five and beta is the wedge pairing.

## Complete decision class

G1 Verify the exact native and Hodge D5 presentations and exact order five of
their products.

G2 Compare the Jordan rank sequences of P_n-I and A_h-I. For each orientation
eps in {+1,-1}, solve the complete linear systems
    X B_n = S_h X,
    X C_n = (S_h A_h^eps) X.
The verifier computes the full intertwiner vector space over F_5 and enumerates
one representative of every nonzero projective coefficient class. Every
invertible projective intertwiner is therefore exhausted exactly. SEAM means
at least one orientation has an invertible intertwiner; DIFFER means neither.

G3 For every invertible intertwiner in every successful orientation pull
Kbar back as N_X=X^-1 Kbar X. Classify the complete set of projective lines
<N_X>. Every member must have rank three, square zero and im=ker.
CANONICAL-K means exactly one projective line occurs. More than one is a
NONCANONICAL result, not STOP.

G4 Pull beta back as Q_X=X^T beta X, classify its projective lines, and solve
independently the complete native D5-invariant symmetric-form vector space.
A unique transported beta line is CANONICAL-BETA; multiplicity is recorded
exactly.

G5 If the K line is unique, test whether A_n,D_n,E_n normalize it. If the beta
line is unique, test whether those remaining linear generators preserve it up
to nonzero scalar. This decides only extension from the D5 sector to the five
LINEAR PARTS. Affine translations and the state-dependent selector are not
included.

G6 FIRED-COMMUTATOR-NOGO remains an explicit boundary. A positive linear seam
does not make the fired affine commutators nonabelian. A negative extension
does not falsify native U.

## Code and systematics

verify.py is Python standard-library only and uses exact arithmetic in F_5.
The native matrices are reconstructed directly from the public coordinate
formulas. The Hodge matrices, Kbar, beta and marked D5 normalizer are generated
inside the verifier. No target intertwiner, K line, metric line or expected
count is supplied as data.

The two marked cycle orientations are both frozen before execution. Projective
enumeration removes only multiplication of an intertwiner by a common nonzero
scalar. All scalar-equivalence tests use exact F_5 projective normalization.
No floating point, randomness, external package, network data or tolerance is
admitted.

## Outcomes and failure threshold

Scientific outcomes SEAM/DIFFER, CANONICAL/NONCANONICAL and
FULL-LINEAR-SEAM/D5-ONLY are all accepted exact decisions. Any failed
assertion about carrier construction, relation checks, exhaustion integrity,
rank-three square-zero transport or invertibility is an implementation or
scientific fired condition as printed. Runtime/integrity failure is STOP.

## Explicit nonclaims

No affine conjugacy, selector equivalence, native-Hodge identity outside the
frozen linear class, physical spatial dimension or time, observer, decoder,
occurrence law, measure, SI quantity, TRACEKERNEL-CURVATURE-FORCING closure or
L2-L6 lift follows from this probe. The author explicitly authorized the
connected GitHub commit identity.
