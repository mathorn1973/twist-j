# Static geometry review

Date: 2026-10-13.

Disposition: no blocking mathematical defect found in the geometry and target
operation at the explicit L1 scope. This is a pre-execution review, not a run
record, a completed public gate, or a Canon promotion.

## Review provenance

The reviewing assistant independently read the supplied
`GEOMETRY_PROOF_CS.md`, `TARGET_OPERATION.md`, `signed_a4_audit.py` and
`independent_geometry_audit.py` against Public Canon v101. The same assistant
then authored the publication adaptation `GEOMETRY_PROOF.md`. Consequently
the initial source review is a separate assistant assessment of the supplied
proof, while the final adaptation check is self-review. Neither is blind or
external review, independent experimental reproduction, or evidence of an
additional implementation having been executed.

No supplied scientific code was executed or imported. The JSON audit outputs
were not accepted as formal evidence. No remote simulation service was used.
The checks reported here are algebraic reading, manual finite calculations,
source inspection, and administrative content hashing only.

The reviewed adaptation has SHA-256:

```text
GEOMETRY_PROOF.md
e3c26ff45a1d927394992aac93e295f33f84401ccccd304201eb8f060b6d6e7c
```

The original intake inputs used for this assessment have SHA-256:

```text
GEOMETRY_PROOF_CS.md
82f3ccddf0557271e74f020ade352636869af89e0c99e35d6a0fbfa61c271ab1
TARGET_OPERATION.md
bae49ed776530fd4d2d61c056682b9e0785cf7f25462da4870eeb766fede00c8
signed_a4_audit.py
9092a1dc10fac13c11754e9ce0212d3a990c7748324102afbd042bc6e493ad42
independent_geometry_audit.py
080ac4616bbb390d39edc5f7ed9b98c546ceff4c8caa2fee76d5f2362604e35a
```

## Canon comparison

The authority comparison is public main
`5f54015ed8361e3a64cb10894397020ddfadd104`, Public Canon v101, content
commit `421a4ec1daf07c04d19022c1ee219607e83c09a8`.
The checked Canon SHA-256 is
`b83a99feccac173bd3c9c5851c5874ca27cbd135f71d136d793b45f86c8a87f7`.

At that source, the directly relevant owned material is:

| Existing owner | Public source location | Consequence for this proof |
|---|---|---|
| TRACEKERNEL-F5-HODGE-BRACKET | CANON.md:18609; REGISTRY.tsv:378 | Explicit B, bracket, sl2 and scale isomorphisms are inherited; physical/Hodge forcing is not supplied. |
| TRACEKERNEL-F5-AUTOMORPHISM-BOUNDARY | CANON.md:18663; REGISTRY.tsv:379 | Killing=2B, Aut120 and the SL2/A5 distinction are inherited. |
| CARRY-PENTAD | CANON.md:10999; REGISTRY.tsv:299 | e2, its singular pentad, O(q)=S5, the A4 and tau15 transports are inherited. |
| CARRY-QUADRATIC-SYMMETRY | CANON.md:10950; REGISTRY.tsv:82 | Pure quadratic carry structure supplies no selected cycle or physical reading. |
| J-BINARY-NORM-DESCENT | CANON.md:10971; REGISTRY.tsv:83 | The binary/cyclotomic isometries do not identify all original carriers literally. |
| A4-RAMIFIED-HODGE-TRACEKERNEL | CANON.md:12087; REGISTRY.tsv:425 | A4 residual quotient-to-W5 is already owned, with frozen bracket sign and marked A5 equivariance. |
| NATIVE-LINEAR-HODGE-ORDER5-OBSTRUCTION | REGISTRY.tsv:431 | The full checkpoint linear group has order-five elements; the new eight-element fiber image is a different representation. |

The actual addition is the intrinsic five-element set of orthogonal triples,
its concrete identification with the five A4 coordinate labels, and the
compatible signed full-S5 action on the residual Lie carrier and binary
reduction. Calling this the first A4/trace-kernel bridge would overstate the
delta. No claim of historical novelty is needed.

## Mathematical checks

1. The triple-product sign is correct for det B=-1. Taking its trace gives
   Killing=2B and B=Killing/2=3 Killing. The square class used for the pentad
   must be B-norm: using raw Killing norm would switch the two nonzero norm
   classes because 2 is nonsquare in F5. The adaptation states this explicitly.
   A nonzero volume rescaling multiplies reconstructed B by a square, so it
   preserves the same pentad.
2. The displayed orthonormal R has the stated determinant and metric. The
   unit-vector census is exhaustive. For a representative (2,1,1), the only
   other square-type orthogonal lines are (1,2,1) and (1,1,2); signed coordinate
   permutations cover the other non-axis lines. The five triples are therefore
   all triples, not merely one chosen partition of fifteen lines.
3. The faithful-action argument is valid: a kernel element is a signed
   permutation matrix, fixes a projective frame of four directions, and is
   scalar; determinant one removes -I. The inherited group order then makes
   the action onto S5. It is unnecessary to infer a new group merely from a
   coincidence of orders.
4. On even subsets of five labels, the half-weight form has the dot-product
   polarization, which is nondegenerate. Its five nonzero zeros have one sole
   linear relation and pair to one. This proves the e2 coordinate expression
   and exhausts the isometry group through the singular-vector action.
5. T0 has exactly the constant-vector kernel and is a metric isometry onto
   the four-coordinate sum-zero space. The cumulative difference map and its
   inverse representative agree. The adaptation supplies an explicit proof
   that the fifteen coordinate-frame lines remain distinct after the radical
   quotient. The integer half-norm descends exactly to binary half-weight.
6. The ordinary residual permutation determinant is its sign. The signed
   three-dimensional action has determinant one and preserves the bracket;
   its sign disappears modulo two. This proves a shared integral action and
   compatible reductions, rather than a 125-to-16 state identification.
7. A4 labels (0,1,2,3,4) correspond to orthonormal-table labels
   (F0,F--,F-+,F+-,F++). Hence signed(01) T exchanges F0 and F--. The earlier
   C0 exchanges F0 and F++; these are different transpositions. Both matrices
   are valid and the adaptation keeps their labels distinct.
8. A and Phi give a transitive Klein action on the four labels outside P0.
   Conjugating T by it gives every star transposition, proving order 120 for
   the augmented class. Phi T has type (0 3 1)(2 4), proving the distinct
   order-twelve dihedral result for the Phi-only class without a computation.
9. The five generator fiber formulas give exactly the stated C2^3 homogeneous
   image and C2^2 bracket subgroup. Shared base and selector histories justify
   applying the same bound to actual U on one starting fiber. Translations,
   new contacts, nonlinear encodings and different observation classes are
   outside this conclusion.
10. The supplied T-specific checkpoint-only obstruction was manually checked:
    the forced image of zero is (1,3,0,1), and applying a gives (3,1,1,0).
    Its interpretation depends on the precise active-action and extension
    contract in NATIVE_PROOF.md. The geometry adaptation does not claim a
    universal centralizer or apparatus obstruction from this one witness.

## Static verifier assessment

Both inspected scripts use exact integer modular arithmetic and the Python
standard library. Their imports are collections/itertools/json; inspection
found no network, subprocess, source-loading, eval/exec or filesystem-writing
operation. This is a static assessment, not a claim that the scripts passed.

`signed_a4_audit.py` constructs the signed S5 action from explicit quotient
maps, checks the homomorphism on all permutation pairs, the frame census,
binary transport, native comparison groups and target T. Its basis-pair
bracket checks exhaust the bilinear identity. Its group-generation loops
are finite exact closure computations.

`independent_geometry_audit.py` constructs the same automorphism set by GL2
conjugation and by orthonormal columns; it also enumerates all triples,
all binary states and the quotient maps. Its 27 basis checks exhaust the
trilinear identity. Its binary completeness conclusion uses the written
singular-vector spanning argument; it is not a separate enumeration of every
binary matrix. That is sufficient at the declared scope.

Neither script proves the physical Hodge premise, native implementation of
T, selected occurrence, or an arbitrary-layer bridge. The accepted wrapper,
its unchanged helper bytes, execution command, all six preregistration fields,
output contract and public pin must be frozen by the coordinator before
formal execution. Any infrastructure or byte-integrity defect is STOP;
an exact mathematical negation is the scientific failure criterion.

## Scope and review disposition

The signed residual S5 action is not a claim that the rank-four integral
Hodge operator K commutes with every odd signed permutation: those still
reverse orientation. The inherited marked A5 result and the frozen minus
sign remain separate and unchanged.

The pentad does not select a five-cycle, direction, exponent, J, native bit
identification, physical selector or implementation. A counter-dependent
trajectory symmetry and an original native word are different typed objects.
The explicit target T supplies a useful future contact specification only
after its independently admitted carrier and operation class are fixed.

Within these boundaries the geometry proof is suitable for inclusion in the
frozen formal revalidation package. This assessment does not replace the
separate native-proof review, formal run, two-architecture gate or reviewed
Canon-fold decision.
