# Q2 admissible class, enumeration proposal for owner review, 2026-08-11

NON-CANONICAL, pre-prereg. Nothing is pinned. This document exists to
answer one question before the third-cut pin: is the proposed class
complete with respect to the intended minimality claim? It states the
class, the completeness argument in three layers, what is provable, what
is frozen by construction, and what is explicitly NOT claimed. Owner
conditions carried: Q1 and Q2 separate; class finite or exactly
parametrized and provably complete; enumeration derived from stratum
structure, dimension, and allowed operations, never from the seventeen
failures.

## The structural pool, inherited and predating the seventeen

The parent lane froze, from the S_4 module structure of the 65-cell
substrate alone, the canonical invariant map with 109 entries:

```text
sums10   10 orbit sums, one per S_4 cell orbit          (trivial [4], m=10)
gram31   78 Gram pairings of the 12 standard copies     ([31], m=12)
gram22   15 Gram pairings of the 5 copies               ([22], m=5)
gram211   6 Gram pairings of the 3 copies               ([211], m=3)
          [1111] absent, m=0: no pure sign channel exists
```

Multiplicities 10, 12, 5, 3, 0 and isotypic ranks 10, 36, 10, 9, 0 are
already gated exactly (spectral-flow cut, G3). The map predates the
seventeen failures and was constructed without them; the seventeen enter
this lane only as held-out evaluation and break points. Condition 3 is
met at the root: everything below derives from this map and from
dimension arithmetic, nothing from the failure list.

## Layer 1, ambient completeness: a provable theorem, gated

CLAIM (to be proved in the prereg and verified two ways): every
S_4-invariant polynomial of degree at most 2 on the sign space of the 65
cells is a linear combination of 1, the 10 orbit sums L_i, the 55
products L_i L_j with i <= j, and the 99 same-sector Gram entries.

PROOF SHAPE. The cells form a permutation S_4-module V. All irreducible
representations of S_4 are of real orthogonal type, so
dim Inv(Sym^2 V) = sum over sectors of m(m+1)/2 = 55 + 78 + 15 + 6 + 0
= 154. Independently, invariant quadratics on a permutation module are
spanned by orbit sums over unordered cell pairs, so the same dimension
equals the exact Burnside count of S_4 orbits on unordered pairs of
cells, diagonal included. The verifier computes both integers exactly
and gates their equality with 154; the degree-1 statement is the
already-gated multiplicity 10. If the two counts differ, the ambient
completeness claim is false and the candidate fires honestly.

Consequence: NOTHING of degree at most 2 exists outside the linear span
of this pool. The class below therefore misses no degree-2 invariant, it
only fixes a granularity on how the pool may be cut into sub-objects.

## Layer 2, the granularity, frozen by definition

Two remarks force the granularity choice, and both go into the prereg.

REMARK A, linear combinations are the wrong class. On any finite domain,
if the full 109-entry map decides orientation at all, then a GENERIC
single real linear combination of the 109 entries also decides it
(injectivity of a generic projection on a finite set of value vectors).
Minimality against arbitrary linear combinations is therefore false at
dimension 1 for trivial reasons, and the claim would be empty. The class
must consist of combinatorial sub-objects, not spans.

REMARK B, entry-level subsets are out of computational reach. The
monotone reduction still leaves on the order of C(109,14), about 10^17,
maximal subsets. This stronger minimality is named, bounded, and left
explicitly UNCLAIMED. It does not silently become part of the claim.

THE ADMISSIBLE CLASS. An admissible invariant is a pair-free assembly

```text
F = (B, A31, A22, A211)
B    a subset of the 10 orbit sums, taken as whole named coordinates
A31  a subset of the 12 standard copies, contributing its FULL internal
     Gram block, all pairings within A31
A22  a subset of the 5 [22] copies, full internal Gram block
A211 a subset of the 3 [211] copies, full internal Gram block

dim F = |B| + g(|A31|) + g(|A22|) + g(|A211|),   g(m) = m(m+1)/2
```

Rationale, structural only: orbit sums are individually canonical, each
is the sum over one cell orbit; within a nontrivial sector the
structurally meaningful sub-object is a copy subset carrying its whole
internal Gram, because a lone off-diagonal entry names two copies anyway
and the block is what the parent construction makes canonical. Products
L_i L_j are excluded from the pool because the parent's canonical map
excludes them (they are functions of B whenever their factors are
present, and the frozen object of this program is the 109-entry map, not
its degree-2 closure); Layer 1 is still proved for the full degree-2
space so the exclusion is visible, not hidden.

The class is exactly parametrized: 2^10 x 2^12 x 2^5 x 2^3 = 2^30
configurations, finite. The claim quantifies over all of them with
dim F <= 14. Deciding is upward-closed and failing is downward-closed,
so the machine enumerates the antichain of maximal admissible
configurations under the cap (dimension 14, plus the plateau cases below
14 whose every extension jumps the cap; both enumerated exactly). The
labeled maximal family has size on the order of 10^5 to 10^6 and is
printed as a count by shape.

## Layer 3, degree scope

Degree at most 2 only. Higher-degree invariants are outside the class
and the claim says nothing about them. This is a scope line in Field 6,
not a hidden assumption.

## The two claims, separated, with their falsifiers

Domain D, frozen for both: the cut-2 abstract domain regenerated exactly
(same LCG constants, same table indices, same expansion rule), enlarged
deterministically: single-cell flips over the WHOLE two-profile pool
instead of the first 200, plus double-cell flips over the first M pool
members in ascending order, M fixed numerically at the pin; plus the
seventeen reals as held-out evaluation points. Only tables with the two
frozen endpoint profiles are kept; both profiles must be present.

```text
Q1  SUFFICIENCY of gram22 on D: bucket D by the 15-entry gram22 vector;
    PASS iff no bucket contains opposite flows.
    Falsifier: one pair, equal gram22, opposite flow, printed as exact
    witnesses. Grade on PASS: candidate-C on D, nothing universal.
Q2  MINIMALITY over the admissible class on D: no admissible F with
    dim F <= 14 decides orientation on D.
    Certificate structure: F decides iff F hits, for every opposite-flow
    pair, a coordinate or block on which the pair differs. The verifier
    reduces pairs to the exact antichain of maximal agreement patterns,
    then certifies every maximal admissible configuration as failing by
    exhibiting a covering pattern, in exact integer arithmetic.
    Falsifier: one admissible F, dim F <= 14, with a certified hit of
    every pattern, printed with its shape and hits.
Q3  UNIQUENESS at dimension 15 is NOT posed here.
```

Q1 gates before Q2. A fired Q1 kills the [H] first and Q2 is still
evaluated and reported. The seventeen reals additionally run as a break
set against whatever survives, after the gates, disclosed as such.

## Findings reported but gating nothing

The exact minimum admissible deciding dimension on D and one witness
configuration attaining it; whether that witness is the gram22 block
itself; the count of maximal admissible configurations by shape; the
sizes of the reduced pattern antichain. These are data for the owner's
next decision, not claims.

## The completeness question, answered directly

Complete with respect to WHAT: the claim as stated in Q2, quantifying
over every sub-object of the canonical 109-entry map assembled from
whole orbit-sum coordinates and whole copy-subset Gram blocks, below
dimension 15, on the frozen domain D. Relative to that claim the class
is complete BY CONSTRUCTION, and Layer 1 proves nothing of degree at
most 2 lives outside the ambient pool the sub-objects are cut from.
What the claim does NOT cover, stated in the prereg so a negative result
cannot be over-read: arbitrary linear combinations (empty claim, Remark
A), entry-level subsets (out of reach, Remark B, about 10^17), degree
3 and higher, and anything off the frozen domain D. If the owner wants
minimality against a different granularity, that is a different Q2 and
needs its own freeze; this document is the place to say so, before the
pin.
