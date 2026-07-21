# P-CURVATURE-OPERATOR-CANONICAL-1: affine group reduction and EMPTY routing (NON-CANONICAL)

Status: `DRAFT / ALGEBRAIC-LEMMA-ONLY / STOP-DEFINITION`

This note answers two open items of
`notes/canon/P-CURVATURE-OPERATOR-CANONICAL-1-DEFINITION-CANDIDATE.md`:
the worst-case affine solver bound of section 8, and the parent `EMPTY`
reachability obstruction of section 10. It is not a public definition,
probe, verifier, run, Canon change, or status proposal. It changes no Canon
object and authorizes no promotion. The scheduler stays `STOP`.

## Authority pin

```text
Canon:              Public Canon v14
state:              ACTIVE
tag:                canon-v14
activation commit:  f278855cada75691142c02ebad1a75ecc2730db3
content commit:     ab4ea07d15ab1cfa0c403d3c2a74164011ffa0e7
Canon SHA-256:      f9f06af42a9b0b63f806603ddc671ebe6a9e5014b50d230da04a28722ed1a6a2
Canon bytes:        87061
owner row:          CURVATURE-OPERATOR-CANONICAL [O]
gate:               GATE-L1-L2-CURVATURE-CANONICAL
child candidate:    CURV-PRIMITIVE-REYNOLDS-CHILD-1
scheduler:          DECODER_CORE / ROOT / STOP / FORMAL
```

## 1. The affine architecture group is trivial

The child note asks for a prior exact reduction of the affine solver, whose
declared worst case is `120 * 5^42` assignments. The reduction exists and
collapses to two lemmas and one small linear system.

```text
Lemma 1 (selector slope).  The proposal-local covariance
    pi_bar(z_6(x) + 2 eps) = z_6(h(x)) + 2 eps
  read at eps = 0 and eps = 1 on one x forces
    pi_bar(z + 2) = pi_bar(z) + 2   for all z in F_5,
  so pi_bar commutes with the transitive action z -> z + 2; pi_bar is a
  cyclic shift. Exactly 5 of the 120 label permutations survive.

Lemma 2 (the central pair).  The linear parts of the fourth and fifth
  public generators (the two mirror maps) are -I, hence central; the linear
  parts of the first three are not. An invertible conjugation
    M A_i = A_(pi(i)) M
  must send the {-I} label pair to itself, and no nonzero shift does.
  Survivor: pi = identity.

System (pi = identity).  The remaining conditions
    M A_g = A_g M                 (first three generators),
    M s_g + t = A_g t + s_g       (all five),
    1^T M = 1^T,   z_6(t) = 0
  are a linear system in 42 unknowns over F_5. Exact RREF has rank 42: the
  unique solution is M = I, t = 0, invertible.
```

Result:

```text
Aut_arch_aff = { identity }.
```

Integrity anchors, computed on the full 15625-state space in the same run:
the five generators are involutions and `(bc)^5 = id`; the orbits of the
`{b, d}` action number 819, so `dim V_S = 818`, reproducing the public
historical regression row exactly. Two architectures byte identical
(x86_64 and aarch64):

```text
verifier stdout sha256 78992a5983d1ad9e2cd4d41d3f6791bc0bd134fb7f4f325fdbf47e6b628afa71
```

This is incubation-lane candidate evidence, not authority; the public
two-platform gate remains the promotion requirement.

## 2. Consequences for the child classification

```text
1  The affine solver feasibility question is closed. A public checker can
   carry the full 120-permutation discipline (an exact RREF no-solution
   certificate for 119 label permutations, the rank-42 solved system for
   pi = identity) at negligible cost; the 120 * 5^42 fallback is never
   reached.
2  The certified affine-equivalence graph has no nontrivial edges. Child
   classes therefore equal typed exact-equality classes; the affine
   quotient merges nothing.
3  CHILD_UNIQUE is consequently unreachable by symmetry alone: distinct
   nonzero operators on distinct typed carriers can never be identified by
   this group. If the parent expected uniqueness to come from the affine
   quotient, that route is closed at candidate grade. Canonicity, if
   wanted, must come from a named principle, not from Aut_arch_aff.
```

## 3. Proposal for the parent EMPTY route (no result-dependent filtering)

The child cannot reach `CHILD_EMPTY` because zero operators are correctly
retained and the empty subset gives a positive-dimensional carrier. The
minimal revision that makes all four parent routes reachable does not touch
admissibility and reads no operator value; it types the parent routing on
the completed classification:

```text
EMPTY      iff every surviving class is a zero class
UNIQUE     iff exactly one nonzero class survives
NONUNIQUE  iff at least two nonzero classes survive
STOP       as frozen
```

Zero rows stay in the family, the inventory, and the certificate; nothing
is deleted; no admissibility predicate reads `K`. The audit-ruling concern
(deleting zeros could manufacture uniqueness) is respected: two nonzero
classes fire `NONUNIQUE` regardless of how many zero classes accompany
them. `EMPTY` then carries its honest meaning, every canonical curvature
candidate vanishes, which is the falsifier route of the
space-is-a-commutator reading.

The alternative kept by the note's own closing line, retaining this child
purely as a necessarily nonempty enrichment classification with a separate
parent surface, remains available; the routing retype above is strictly
cheaper and adds no contract debt.

## 4. What stays open

No admissibility surface, canonical selector, or `K`-dependent principle is
proposed here. The parent gate, the completeness/resource plan of the
public checker, and the choice between the routing retype and a separate
parent surface remain owner decisions. `CURVATURE-OPERATOR-CANONICAL`
stays `[O]`, the scheduler stays `STOP`, and no Canon frontier count
changes.
