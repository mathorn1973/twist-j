# Independent exposed proof review

Status: NON-CANONICAL / NO AUTHORITY. Action layer: L1.
Disposition: ACCEPTED at the frozen conditional mathematical scope.
The review was performed by a separate assistant context within this session.
A. M. Thorn <thorn@twistj.com> is the repository attribution and commit
identity, not a claim that the user personally performed the review.
Review session: discrete-boundary-proof-review-20261008.
Reservation: https://github.com/mathorn1973/twist-j/issues/1421.

This is a separate mathematical review of the written proof. It is not
formal peer review, blind proof discovery, independent computational
confirmation, or a public status promotion. The proof's status remains
candidate-T. No exact counterexample or material proof gap was found in
the reviewed statements.

## 1. Exact reviewed object and method

```text
proof commit   0e56f9605129d414348a3cf1a0629c1c607bc43f
parent / prereg commit
               e092feb641e859d7d959e72f3ab39ec88d4fc53c
PROOF.md SHA-256
               a3684d789d4876b812c76d6ef2f53ff34924f77135f5cd4b017782f44c2ec029
```

The review checkout was created at exactly the proof commit. Its parent
and the proof-file hash were checked. The complete PREREG.md and PROOF.md
were read. The repository operating rules are unchanged from the checked
public basis 7d7f588c42422c2cf37b04d76ebc13ca55eb96dc.

No candidate implementation, scientific transcript, or EXPECTED.txt was
read. No scientific code was executed. The reasoning below is an exposed
review of the proof and frozen definitions; it makes no claim about whether
the separate finite audits implement them correctly. The review also uses
the reviewer's preceding read-only audit of the public native, Maxwell,
and selected-field source boundaries.

## 2. Restriction, operations, and transferred dynamics

The inverse criterion in section 1 is correct on the specified image R(X).
If R is injective, each image point has one preimage, so D is uniquely
defined and satisfies both D R = id_X and R D = id_R(X). The cardinality
bound is a consequence; the proof correctly does not use that bound as a
sufficient condition for the particular restriction to be injective.

For a nonempty affine class, subtracting one member identifies the class
with ker H. Differences within one boundary fibre are therefore exactly
ker H intersect ker R, with the latter R acting on the ambient space.
The stacked-rank criterion and the size of every nonempty affine fibre
follow without assuming that arbitrary target data are feasible.

The fixed-boundary-operation conclusion requires both P(X) subset X and
R P = R. Under those hypotheses injectivity forces P = id_X, even when P
was not assumed bijective. This does not forbid a map that changes the
boundary data or leaves the admitted class.

For U:X -> X the map U_B = R U D is defined on R(X), and both displayed
intertwining equations follow from the two inverse identities. Bijectivity
transfers in both directions. The proof expressly avoids an inference
that the induced boundary law must be local.

## 3. Mixed-difference class for every N

The signs of the frozen eight-corner equation agree with the third mixed
forward difference. Summing over the rectangular block from the origin
to (i,j,k) leaves precisely the eight corner terms in section 2. This
proves necessity of the proposed reconstruction formula at every point
with all three coordinates positive.

The converse is also proved. On any selected coordinate face, cancellation
reduces the formula to the assigned value at that point. This remains true
on pairwise face intersections and at the origin, since B_N is a union
with each point carrying one value. Each summand in the extension is
independent of at least one coordinate, so its third mixed difference is
zero on every unit cube. Thus arbitrary data on the union extend, and the
telescoping identity makes that extension unique.

The dimension and rank follow from this linear bijection, not from a
finite-size pattern or merely counting equations. Rank-nullity gives
rank H_N = (N-1)^3, which also proves independence of all actual cube rows.
The images of all boundary coordinate unit vectors form a complete basis.
The argument covers N=2 without requiring an unstated large-box condition.

Multiplication by 2 preserves this linear class, multiplication by 3 is
its inverse over F5, and the extension commutes with the multipliers by
linearity. The third coordinate is an index in the selected box, not a
substitute for the separately specified update time.

## 4. Graph lemma and the complete Gauss-box classification

The graph argument handles independent parallel and opposite directed
labels. Leaf elimination proves that the retained spanning-tree columns
are independent over any field. The augmentation has a one-dimensional
image, so the zero-total-charge target space has dimension v-1, including
the case v=1. No assumption about the characteristic not dividing v is
needed.

For each non-tree label, its unit vector minus the signed tree path has
zero divergence. Its own non-tree coordinate is one and every other
non-tree coordinate is zero. This proves independence. Subtracting the
corresponding combination from an arbitrary cycle leaves a tree-supported
cycle, which vanishes by leaf elimination. The construction therefore
spans the entire kernel, rather than just a collection of elementary
plaquette cycles. It leaves no unclassified winding or cycle sector.

In the box reader, setting observed coordinates to zero leaves exactly
the induced graph on the interior vertices. Its columns have no outer
endpoints, so the full divergence equations add no further outer-vertex
condition on those remaining coordinates. This justifies the identification
of K_N with the entire interior incidence kernel.

The two small cases are treated correctly:

- N=2 has no interior vertices or unobserved edges. Its kernel is zero;
  applying e-v+1 to an empty graph would be wrong, and the proof does not
  do that.
- N=3 has one interior vertex and no interior edges. The connected-graph
  formula now applies, giving rank and kernel dimension zero.

For every larger interior grid, the stated parent rule stays in the
interior, strictly decreases the coordinate sum, and reaches (1,1,1).
It defines a spanning tree. Its fundamental cycles, extended by zero,
give the complete basis required for the affine-fibre count.

The feasibility condition is also complete. After fixing the observed
coordinates, eta = rho - d qbar must vanish outside the interior. On a
nonempty connected interior its sum must vanish and that condition is
sufficient by the incidence image theorem. For the empty interior the
condition is eta=0 on all vertices. In particular the singleton interior
condition forces its one remaining eta entry to be zero. Empty fibres are
not assigned the positive cardinality formula.

The four signed edges of the N=4 witness follow the frozen nonperiodic
square. Every endpoint is interior, all four edge labels are distinct,
and successive incidence contributions cancel. It therefore differs from
zero while fixing every individually observed edge and the full charge
vector.

## 5. The 24-label torus and the distinct dimensions five and ten

The proof retains all 24 directed labels of the public Maxwell torus.
Opposite wrapping labels are distinct coordinates. Its chosen seven tree
edges connect all eight vertices, and the general cycle-basis argument
therefore applies without replacing the object by a twelve-edge cube.
The whole-torus rank and kernel dimension are correctly identified as
already present in the public source.

The marked slice has four vertices and eight internal labels. Its
connected incidence has rank three. The four two-edge wrapping cycles in
(7) have disjoint supports. The four-edge square has unequal coefficients
on the marked opposite pair on which any combination of those four cycles
has equal coefficients. This proves independence of the fifth vector.
The resulting five vectors form the complete region-supported kernel.

Fixing only the eight crossing labels on the whole carrier leaves both
internal slice graphs. Their vertex sets and divergence equations are
disjoint, so the full fixed-cut kernel is the direct sum of two copies of
the five-dimensional kernel. This gives dimension ten, not five. The
proof correctly distinguishes fixing the entire complementary field from
fixing only the cut.

For arbitrary charge and crossing data, subtracting the fixed crossing
field leaves two independent charge problems. Zero residual charge sum
on each slice is necessary and sufficient. Thus the feasibility condition
and the cardinality of every nonempty full fibre are both justified.

The torus witness uses the positive wrapping labels at the last two
corners. Its support, signs, and orientation agree with the frozen cycle;
it is not the signed nonperiodic witness with labels silently reused.

## 6. Aggregate readings and temporal qualification

The incidence convention in both candidate edge carriers is -tail/+head,
and equation (9) has the corresponding signs. An aggregate crossing flux
is a linear combination of individual crossing coordinates. The box
reader additionally retains edges within the outer vertex boundary.
Both witnesses vanish on the complete specified reader, so their
invisibility is stronger than agreement of one total flux.

Translation by either witness preserves the zero-charge class and its
reader, giving a nonidentity mathematical operation. No native or
physical admission of this translation is assumed.

The temporal statement is qualified correctly. Multiplication by 2
preserves the zero-charge and zero-observation kernels; on a general
affine fibre it instead changes the target data to (2rho,2q). For a
nonzero witness, the scalar sequence 1,2,4,3 has least period four in F5.
A nonzero edge coordinate rules out an earlier return, and no phase
loses support or becomes the zero field. Periodicity therefore proves
all-time boundary invisibility for this chosen comparison law. A static
Gauss witness alone would not establish that statement for an unrelated
time law, and the proof makes no such claim.

## 7. Scope and remaining limits

The positive vertex-field class, the negative edge-field class, their
different readers, and the public torus comparison remain explicitly
distinct. No conclusion about unrestricted fields is inferred from the
mixed-difference class. No curl, energy, preparation, or topology-sector
restriction is inserted into the frozen Gauss-only class to repair its
noninjectivity.

The dependence on five is accurately delimited. Telescoping, the inverse
criterion, and the graph arguments do not select this prime. The finite
state counts and the particular multipliers and four-phase orbit use F5.

The native and physical limitations agree with the public-source audit:
the growing boxes, constraints, readers, and multiplication update are
chosen comparison structures. No scalable native carrier, native region
selection, complete native reader, or actual-U intertwining is provided.
The proof does not identify a selected finite subset with an adopted L3
boundary, derive physical dimension or entropy, or close any public
physical owner. Prior locality and field-spectrum lanes are not re-earned.

The acceptance here covers the written universal arguments at their
frozen scope. It does not certify either implementation, finite audit
coverage, execution custody, byte agreement, a second architecture, or
physical realization. Those are separate records and obligations.
