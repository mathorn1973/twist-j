# Five fixed field-cell shear comparison

Status: PASS / NON-CANONICAL L1 candidate.

The first formal run at immutable pin
`423c6f7488b35399ff40fcc30be01df526aba795` completed with exit zero,
empty stderr and the exact 874-byte, eight-line stdout in EXPECTED.txt.
Its SHA-256 is
`9a722d992c12eea57c9de5220c68b02877c688f92da5fd1a5801f15cf27107d3`.
No scientific falsifier fired. No frozen source or threshold was changed.

## Exact disposition

| Fixed Gram type | Characteristic polynomial | Least matrix order | Energy |
|---|---|---:|---|
| (2) | X^2+1 | 4 | positive definite |
| (3) | X^2+X+1 | 3 | positive definite |
| [[2,1],[1,2]] | X^4+X^2+1 | 6 | positive definite |
| [[2,1],[1,3]] | X^4+X^3+X^2+X+1 | 5 | positive definite |
| [[3,1],[1,3]] | (X^2+1)(X+1)^2 | infinite | positive semidefinite, one-dimensional nullspace |

Each active determinant is one. Explicit boundary incidences, complete
coordinate conventions, inverse and energy identities, and the relation
to the full raw carrier are in PROOF.md. The verifier audits five exact
representatives and all 248 signed edge/face markings, including metric
transport and the exact canonical A_f/B_f identification.

The infinite-order conclusion rests on the analytical certificate
`v=(1,1,-2,-2)`, `u=(0,0,1,1)`, `(A+I)v=0`, `(A+I)u=v!=0`.
For every k>=0, `A^k u=(-1)^k(u-kv)`, which excludes every positive
identity power. The coefficient checks audit that certificate; neither a
finite search nor a repeated characteristic root alone proves infinity.
Likewise, universal energy and state claims rest on the written proof,
not finite sampling of states.

## Inheritance, novelty and limitations

The general shear-energy theorem, triangle resonance, canonical positive
order-five cell and shared-triangle zero-energy witness are inherited from
v102. LINEAGE.md records the inspected source scope. The candidate addition
is the narrowly bounded common-coordinate comparison, including explicit
digon/double-digon representatives, minimal orders and the shared-triangle
infinite-order certificate. Repository novelty is a bounded audit finding,
not a claim that this linear algebra is new to mathematics.

Reversing a physical edge changes its C row and D column together and leaves
the Gram matrix unchanged. The opposite offdiagonal sign is a whole-face
orientation change. The order-five minus marking is exactly the existing
canonical field, not a replacement law. Digons use distinct parallel edges
in finite CW cells; they are not asserted to be simple simplicial faces.

The result concerns precisely five supplied types and their orientation
equivalents. It does not classify all two-face complexes or select p=5.
It supplies no U-to-field lift, physical energy selection, source transport,
contact or apparatus, and changes no Canon, registry, frontier or open owner.
Raw rational decomposition is not an integral direct-sum claim, and matrix
order is not the least period of every individual state or of a coupled chain.

## Review and reproducibility boundary

This author package is ready for the required repository checks and separate
review. The pull request must have passing x86_64 and aarch64 jobs with
byte-identical output and the aggregate check before its computation gate is
claimed satisfied. Actual job identities/results are linked on #1554 and
the pull request, rather than inferred from this first local run.

The distinct RC lane remains a separate independent derivation and audit.
Same-session proof and static-check helpers do not supply that independence.
Reviewers must respect PREREG.md's exposure barrier before their own freeze.
Until separately accepted and promoted at its exact scope, this package
remains NON-CANONICAL; a queue review or successful CI alone assigns no
public theorem status. No merge or release is performed by this submission.
