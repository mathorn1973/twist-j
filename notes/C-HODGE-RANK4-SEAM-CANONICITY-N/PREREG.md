# C-HODGE-RANK4-SEAM-CANONICITY-N: preregistration

Status: PUBLIC NON-CANONICAL incubation, no Canon authority.
Owner: A. M. Thorn / rank4-seam-canonicity-20260927; issue #1223.
Action layer: L1 exact algebra. Date: 2026-09-27.
Basis: Public Canon v92, main 09ace5f4664392e007a353e822350c9e4d094783.
Predecessor: C-HEXAGON-HODGE-PHOTON-SEAM-N, merged #1221; not reopened.

## 1. Fixed inputs and complete classes

Use the marked A4 basis e0-e4,...,e3-e4 and its five-cycle C.
Let F=Q(sqrt5), W=(Lambda^2 A4) tensor F, L=Lambda^2(I+C^2),
beta the wedge pairing and K the integral Hodge operator K^2=5I.
The real embedding has sqrt5>0. Put P_+=(I+K/sqrt5)/2,
E=im(P_+)+im((I-P_+)LP_+), A=L|E, and g=beta|E.
The target is Z=Lambda^2 E, with B=Lambda^2 A. Z is NOT native U,
F5^6, a physical field, or the selected photon carrier T_D3.

Inherited T rows: J-HODGE-PREDICTIVE-CLOSURE,
J-HODGE-HERM2-LOXODROME, J-HODGE-RATIONAL-CLOSURE,
J-C5-HODGE-CONIC-ATLAS and J-HODGE-SEMILINEAR-MEMORY.
The frozen inherited matrix source is
probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py,
SHA-256 02f33f1de4174ee4d4aeb45202d838897e68c3bd205df23f9b208cc669f489d9.
Its exact anchor replay is reproduction, not independent confirmation.
The predecessor supplies a written comparison to audit, not a Canon premise.

The complete blocked class is

    H = {S in Hom_F(W,Z): S L^10 = B^10 S},
    R4 = {S in H: rank_F(S)=4}.

No restriction on entries, basis coefficients or source vectors is imposed.
Literal equality of maps is entry equality. Literal kernel/image equality is
subspace equality, independently of the map. The additional equivalence is
ONLY the finite cyclic action described below (and, for maps only, optionally
nonzero scalar multiplication). These equalities are not interchangeable.

## 2. Symmetry and canonicity test

Set Q=Lambda^2 C, R=Q|E and D=Lambda^2 R on Z.
First prove that R is well-defined and Q preserves beta and K and commutes
with L. The cyclic action on H is S -> D S Q^-1.
It fixes the specified input data; it is a subgroup of the marked A5 axis
normalizer, not the assumption that every A5 element preserves one chart.

Decide separately:
(a) dim H and the complete maximum-rank block form;
(b) existence and dimensions of equivariant maps S Q=D S;
(c) existence of D-invariant images of members of R4;
(d) classification of Q-invariant kernels of members of R4;
(e) uniqueness of literal images and uniqueness modulo the finite C5 action.

Canonical literal selection means a selector from the fixed data invariant
under its automorphisms, not merely choosing coordinates or returning a
symmetry orbit. Absence of a fixed image obstructs such a literal selector;
it does not exclude a covariant family or equivalence under a different,
separately declared gauge group. A subgroup obstruction suffices for every
larger same-target naturality requirement containing that subgroup.

## 3. Natural target forms, without an inserted metric

On Z freeze h=Lambda^2 g and gamma(z,z')=(z wedge z')/vol_E, with vol_E the
ordered basis volume from the inherited E chart. A volume rescaling changes
gamma by a nonzero scalar and not any signature conclusion. Classify the
restriction to every image of R4 of h and gamma and of their real pencil
lambda h+mu gamma, (lambda,mu)!=(0,0).

Record all nondegenerate signatures and all degeneracies. Test the proposal
that an inherited restriction is Lorentz (3,1) or (1,3), rather than putting
that signature into the definition. A metric transported from a source
quotient through a chosen S is a DIFFERENT construction and must be named.
No identification of the Euclidean-source Hodge involution with the Lorentz
Hodge star on Z is allowed.

## 4. Surviving direct quotient control

Let P=ker(L^10-I), T=ker(L^2-3L+I), P_-=P intersect ker(K+sqrt5 I).
Test the orthogonal projection Pi onto E along E^(perp_beta): Pi^2=Pi,
rank Pi=4, [Pi,L]=[Pi,Q]=0, ker Pi=P_-, and its induced source-quotient
metric has the already accepted (3,1) signature. Determine its relation to
Galois conjugation. Conjugation transports E_+ to E_-, so it is not silently
an endomorphism of the same target. Relative uniqueness of an orthogonal
projection onto a chosen E is not physical selection of that chart.

## 5. Prospective exact audit

Commit this file and verify.py and publicly read back both before executing.
The standard-library audit uses Fraction-based Q(sqrt5) arithmetic only;
it replays the hash-pinned anchor, constructs both exterior powers, solves
the full linear intertwining systems, checks the primary blocks and the
natural forms, and tests explicit distinct rank-four images plus the direct
quotient. Universal classifications rest on a separate written proof.

There is no blind independent agent. Any second formulation in this session
is proof-aware cross-checking, not independent confirmation. Notes are not
replayed by the ordinary changed-public-probe CI selector; green CI alone
will not be described as two-architecture execution of this note.

## 6. Decisions and falsifiers

Accept UNIQUE, NONUNIQUE or EMPTY for each separately typed class. Exact
mathematical counterexamples decide a proposed clause negatively. Audit
implementation or integrity failure is STOP, not a physical falsifier.
No threshold changes, resumed sealed probe, or post-result equivalence
change is allowed. New work beyond these targets needs another candidate.

Only this new notes directory may be added. No Canon, Registry, Frontier,
public gate, existing note, workflow or tool changes. PHOTON-CONE-CONVERGENCE,
PHOTON-MASSLESS-PHASE and TRACEKERNEL-CURVATURE-FORCING remain unchanged.
No physical dimension/time, native-state identification, continuum,
propagator, polarization, measurement, apparatus, probability or SI result.
