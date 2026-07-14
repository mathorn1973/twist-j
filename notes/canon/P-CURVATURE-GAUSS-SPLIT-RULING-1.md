# P-CURVATURE-GAUSS-SPLIT-1: Owner Ruling (NON-CANONICAL)

```text
Program:          CURVATURE-GAUSS-SPLIT
Probe:            P-CURVATURE-GAUSS-SPLIT-1
Track:            C
Owner:            master C, public lock issue 22
Date:             2026-07-14
Basis:            Public Canon 2, tag canon-v2
Activation:       5abb22319007fd3172f7123f4b3a71b547fb94af
Content commit:   7cfe2a62a456d0f84b1f60b4945dcdfe896e99db
Canon SHA-256:    abd0e026ccc2be00cdb0d9d13d634e0a71602b1565e6d53ac23a99b506281021
Canon bytes:      54705
Status:           RULING CANDIDATE BEFORE MERGE; PINNED NON-CANONICAL
                  OWNER RULING AFTER REVIEWED MERGE AND PUBLIC BYTE READBACK
Scientific claim: remains O
Action layer:     L2
Public record:    mathorn1973/twist-j issue 22
Computation:      NOT AUTHORIZED
Result:           NONE
```

## 0. Owner decision and purpose

Public Canon 2 separates three facts:

1. the frozen historical operator has exact trace square `-881/8`;
2. the historical proposal `-21/8` is false at that surface; and
3. a canonical spatial-curvature operator has not been selected.

This ruling does not reopen any of those results. It asks a narrower structural
question about the already frozen historical operator: how much of its
commutator is internal to the selected subspace, and how much is created by
leaving that subspace and returning through the projection?

The probe is diagnostic, not canonicalizing. No outcome selects a preferred
carrier, measure, symmetry group, projection, connection, normalization, or
continuum interpretation. `CURVATURE-OPERATOR-CANONICAL` remains `[O]` after
every valid outcome.

No computation is authorized by this ruling candidate. Formal execution may
begin only after the ruling is reviewed, merged, and read back from public
`main`, and after the future preregistration and verifier pass reciprocal byte
review and are committed and pushed as one immutable pin.

## 1. Authority and incorporated public surface

The exact definitions are incorporated from the following public objects at
the authority pin above:

```text
notes/canon/P-CURVATURE-TRACE-RULING-1.md
  SHA-256 cf15037f5cc2690a9633ca68ef13107920ce9ce81116963dc9d8490c088eeccb

probes/P-CURVATURE-TRACE-VALUE-1/PREREG.md
  SHA-256 94ec5263d2b2931bcd3863cb5f78e2326944479aa28aef987495c8601c65f8c9

probes/P-CURVATURE-TRACE-VALUE-1/verify.py
  SHA-256 c9b4d253a609cc489efc4386e5e61d3e92baa16b736b899048f2a3afa5e78c99

probes/P-CURVATURE-TRACE-VALUE-1/RESULT.md
  SHA-256 5d3c406233958bee62076a624012c28bf38c7c770bb79d35f62cf49e699e6baf
```

The new verifier must reconstruct the incorporated definitions itself. It may
not import executable code or cached matrices from the prior probe. The prior
result supplies a public read-back anchor, not an implementation dependency.

## 2. Frozen carrier, maps, and projection

Work over

```text
X = F_5^6,
x = (p1,p4,p1p,p4p,q,r),
F = Q^X,
<f,g> = sum_(x in X) f(x) g(x).
```

All state arithmetic is modulo 5. Freeze the Public Canon 2 checkpoint maps
exactly as in the incorporated probe:

```text
a(p1,p4,p1p,p4p,q,r) = (p4,p1,p4p,p1p,q,r)

b(p1,p4,p1p,p4p,q,r) = (-p1p,-p4p,-p1,-p4,-q,-r)

c: piston -> b4(piston) + (2,1,2,1) + r(0,1,0,-1)
   q       -> 1-q
   r       -> -r

d(x) = (2,1,3,4,1,1) - x
e(x) = (2,1,3,4,2,1) - x.
```

The composition and Koopman conventions remain

```text
(g o h)(x) = g(h(x)),
(T_g f)(x) = f(g^-1 x),
T_g T_h = T_(g o h).
```

Put

```text
A = T_a,
C = T_c,
H = <b,d>,
R_H = (1/20) sum_(h in H) T_h,
Pi_1(f) = (1/|X|) (sum_(x in X) f(x)) 1_X,
P0 = I - Pi_1,
P = P0 R_H = R_H P0,
Q = I_F - P,
V = im(P) = F^H intersect 1_X^perp.
```

The counting inner product, full carrier, and `H = <b,d>` are fixed. The map
`e` remains an integrity-only generator. It does not enter `H`, `P`, `Q`, or
any curvature operator.

The verifier derives rather than assumes

```text
|X| = 15625,
|H| = 20,
X/H = 1 orbit of size 5, 74 orbits of size 10,
      and 744 orbits of size 20,
dim F^H = 819,
dim V = rank(P) = 818,
P^2 = P = P*,
Q^2 = Q = Q*,
PQ = QP = 0,
P + Q = I.
```

Changing the group to `<b,d,e>`, changing the measure, omitting `P0`, or
replacing the orthogonal projection by a fitted map is a different probe.

## 3. Frozen Gauss split

Form all displayed products first as operators in `End(F)`, and define the
scientific operators by their explicit restrictions to `V`. Define the
already public ambient compression

```text
K_amb = P[A,C]P |_V
      = P(AC-CA)P |_V.
```

The operators induced inside `V` are

```text
A_V = PAP |_V,
C_V = PCP |_V.
```

Define

```text
K_int = [A_V,C_V]
      = (PAPCP - PCPAP) |_V,

K_ext = (PAQCP - PCQAP) |_V.
```

Also define the two leakage maps

```text
L_A = QAP |_V : V -> V^perp,
L_C = QCP |_V : V -> V^perp.
```

They give the exact factorization

```text
K_ext = L_A* L_C - L_C* L_A.
```

In the non-orthonormal basis, audit this factorization through the
basis-independent bilinear identity

```text
<w_i, K_ext w_j>
  = <L_A w_i, L_C w_j> - <L_C w_i, L_A w_j>
```

for every ordered pair of basis vectors. An ordinary Euclidean transpose of
the coordinate matrices is not an admissible adjoint.

Inserting `I = P + Q` between the two ambient factors gives the exact operator
identity

```text
K_amb = K_int + K_ext.                 (G)
```

All three operators are total endomorphisms of `V`. Since `A`, `C`, `P`, and
`Q` are self-adjoint,

```text
K_amb* = -K_amb,
K_int* = -K_int,
K_ext* = -K_ext.
```

The labels `amb`, `int`, and `ext` describe this exact algebraic split only.
In particular, `K_ext = 0` can occur by cancellation even when one or both
leakage maps are nonzero. Therefore the decision word `INTRINSIC` below means
only that the ambient and internal commutators agree at this frozen surface;
it does not by itself mean that `A` and `C` preserve `V`. The verifier must
print exact zero/nonzero diagnostics for `L_A` and `L_C` so this distinction
cannot be hidden. The labels do not assert a differential-geometric Gauss
equation, a second fundamental form, or a physical embedding theorem.

## 4. Canonical integer basis

Enumerate all `H`-orbits as

```text
O_0, O_1, ..., O_818
```

in lexicographic order of their least states, and put `s_i = |O_i|`. Freeze
the ordered integer basis of `V`

```text
w_i = s_0 1_(O_i) - s_i 1_(O_0),      i = 1,...,818.       (B)
```

Every `w_i` is `H`-invariant and has counting sum zero. The basis is complete
because every orbit-constant mean-zero function has one unique expansion in
`(B)`.

Let `G` be its exact Gram matrix,

```text
G_ij = <w_i,w_j>.
```

For a matrix `M` in this non-orthonormal basis, skew-adjointness means

```text
M^T G + G M = 0.
```

The verifier must use this Gram identity. Entrywise antisymmetry of `M` is not
a valid substitute in a non-orthonormal basis.

## 5. Required independent constructions

The accepted verifier must construct the split in two exact ways. The routes
may share only the frozen carrier, affine maps, complete `H` action, orbit
ordering, projector definitions, and basis `(B)`.

### Route A: direct full-carrier propagation

For each basis column `w_i`, represent the function exactly on all 15625
states and apply the operators in their displayed order. In particular,
`K_ext w_i` must be constructed by the actual leakage path

```text
w_i -> C -> Q -> A -> P
w_i -> A -> Q -> C -> P
```

and subtraction. Route A may process one column at a time, but it must not
define `K_ext` as `K_amb - K_int`.

Route A returns exact rational matrices

```text
M_amb_A, M_int_A, M_ext_A.
```

### Route B: complete orbit transitions

Independently count complete transitions between every ordered pair of
`H`-orbits. For each `g` in `{a,c,a o c,c o a}`, define

```text
n^g_ij = #{x in O_j : g(x) in O_i}.
```

The orbit-average coordinate of `P T_g` on `O_i` is exactly `n^g_ij/s_i`,
followed by the frozen mean-zero projection and exact change to basis `(B)`.
From these complete counts construct the exact compressed matrices

```text
B_a  = matrix(PAP |_V),
B_c  = matrix(PCP |_V),
D_ac = matrix(PACP |_V),
D_ca = matrix(PCAP |_V).
```

Then form

```text
M_amb_B = D_ac - D_ca,
M_int_B = B_a B_c - B_c B_a,
M_ext_B = (D_ac - B_a B_c) - (D_ca - B_c B_a).
```

Route B must not read Route A columns, matrices, traces, ranks, or zero tests.
Complete orbit transition totals and exact mean-zero projection are integrity
gates.

Before any observable or decision is printed, require exact entrywise
agreement

```text
M_amb_A = M_amb_B,
M_int_A = M_int_B,
M_ext_A = M_ext_B,
M_amb_A = M_int_A + M_ext_A.
```

The direct `Q` path in Route A makes the last comparison a real check rather
than a definition of the exterior term.

## 6. Frozen observables

For each of `K_amb`, `K_int`, and `K_ext`, compute exactly over `Q`

```text
trace square: Tr_V(K^2),
rank:         rank_Q(K),
nullity:      818 - rank_Q(K).
```

Also compute

```text
cross = 2 Tr_V(K_int K_ext).
```

For ordinary coordinate matrices in any basis, freeze

```text
Tr(MN) = sum_(i,j) M_ij N_ji.
```

The scalar control identity is

```text
Tr_V(K_amb^2)
  = Tr_V(K_int^2) + cross + Tr_V(K_ext^2)
  = -881/8.                                      (T)
```

The final value in `(T)` is an incorporated Public Canon 2 theorem and a
read-back anchor. It is not a target value for any split component. No value
for `Tr(K_int^2)`, `Tr(K_ext^2)`, `cross`, any rank, or any nullity is known or
frozen by this ruling.

Ranks must be obtained by deterministic exact rational elimination, with
columns and pivot candidates considered in basis order. The verifier must
also construct an exact kernel basis for each matrix and check

```text
the certificate contains exactly nullity many linearly independent vectors,
M u = 0 for every reported kernel vector,
the vectors span the full kernel under the same exact reduction,
rank + nullity = 818.
```

Because the three operators are skew-adjoint on a positive definite rational
space, the verifier also checks

```text
rank(K) is even,
Tr(K^2) <= 0,
K is the zero matrix iff rank(K) = 0 iff Tr(K^2) = 0.
```

Scientific zero tests use exact matrix equality. They do not use a decimal,
tolerance, rank heuristic, or trace alone.

The two trace-square terms are nonpositive, but `cross` may have either sign.
The three summands are an exact algebraic decomposition, not nonnegative
percentages or separately normalized curvature shares.

The verifier must additionally test `L_A` and `L_C` directly on every basis
column. It prints whether each leakage map is zero. These diagnostics are not
new decision branches and do not alter the frozen zero test for `K_ext`; they
distinguish invariant compression from cancellation of leakage contributions.

## 7. Integrity gates

The future preregistration must preserve at least the following ordered
integrity tally. It may split a gate into smaller printed checks, but may not
weaken or merge away a requirement.

1. `I1`: authority read-back, incorporated file pins, and exact public tag;
2. `I2`: all 15625 states and exact total affine maps `a,b,c,d,e`;
3. `I3`: five involutions, composition convention, and Koopman product law;
4. `I4`: exact group `H`, closure, action, orbit census, and orbit ordering;
5. `I5`: exact `P0`, `R_H`, `P`, `Q`, projector identities, and dimensions;
6. `I6`: canonical basis completeness and exact positive Gram matrix;
7. `I7`: total typing of all three operators as endomorphisms of `V`, and of
   `L_A,L_C : V -> V^perp`;
8. `I8`: Route A complete direct propagation, including the explicit `Q`
   leakage path;
9. `I9`: Route B complete orbit-transition construction;
10. `I10`: exact entrywise agreement of both routes for all three matrices;
11. `I11`: exact operator identity `(G)`, the leakage factorization, and Gram
    skew-adjointness of all three matrices;
12. `I12`: exact trace-square and cross identity `(T)` with the public
    `-881/8` anchor;
13. `I13`: deterministic exact ranks, kernel certificates, nullities, parity,
    and zero equivalences;
14. `I14`: standard-library-only exact arithmetic, no float, sampling,
    randomness, external input, cache, or network;
15. `I15`: deterministic stdout, empty stderr, complete tally, and
    audit-before-decision precedence.

Any failure is `STOP`. A route mismatch may not be repaired by choosing one
route, averaging values, changing basis, or redefining the exterior term.

## 8. Scientific decision routing

The complete integrity tally is evaluated before the decision. With a valid
public anchor, `K_amb` is nonzero, so the following cases are exhaustive and
disjoint:

```text
DECISION INTRINSIC
  every integrity gate passes and K_ext is the zero matrix.
  This means K_amb = K_int; the separate leakage diagnostics decide whether
  the equality comes from invariant action or cancellation.

DECISION MIXED
  every integrity gate passes, K_int is nonzero, and K_ext is nonzero.

DECISION PROJECTION-INDUCED
  every integrity gate passes, K_int is the zero matrix, and K_ext is
  nonzero.

DECISION STOP
  any authority, typing, exactness, completeness, identity, rank/nullity,
  determinism, execution, or public-anchor gate fails.
```

The first three decisions are valid first-class scientific outcomes and exit
zero. `STOP` is invalid execution and exits nonzero. It may print the process
marker `DECISION STOP`, but it prints no valid scientific outcome. An
exception or incomplete run is `STOP`, never a negative result.
The simultaneous case `K_int = K_ext = 0` is also `STOP`, because it would
contradict the required nonzero public ambient anchor.

## 9. Prior knowledge and forbidden targets

Known before this ruling:

```text
dim V = 818,
Tr_V(K_amb^2) = -881/8,
the historical proposal -21/8 is false,
the separate ten-mode checksum is -22 and is not a spectrum of K_amb.
```

No split trace, cross term, rank, nullity, or decision outcome has been
computed or predicted here. The verifier and preregistration must not contain
a hidden expected split value, a preferred sign pattern, a golden block, or a
target rank.

The following substitutions are forbidden:

- quotienting by a new symmetry or automorphism;
- using `<b,d,e>` instead of the frozen `H`;
- replacing the counting inner product or orthogonal projectors;
- dropping constants by an unproved coordinate deletion;
- defining `K_ext` only as a residual;
- using an orthonormalization with floating point or algebraic square roots;
- rescaling any operator after seeing output;
- reading a negative trace square as negative physical curvature;
- promoting `K_amb`, `K_int`, or `K_ext` to the canonical curvature operator.

## 10. Required formal output and evidence

The future stdout freezes only labels and ordering, not unknown values. It must
contain:

```text
authority and source-pin read-back
carrier, group, orbit, and dimension certificates
AUDIT PASS m/m
Tr(K_amb^2), Tr(K_int^2), Tr(K_ext^2), and cross as reduced fractions
rank and nullity of K_amb, K_int, and K_ext
exact zero/nonzero diagnostics for L_A and L_C
exact reconstruction of identity (T)
one of DECISION INTRINSIC, MIXED, PROJECTION-INDUCED
RESULT VALID
```

The formal local run must be from a clean descendant of the immutable pin,
use neutral public environment fields, exit zero, write empty stderr, and
save byte-exact stdout as `EXPECTED.txt`. `RUN.md` must contain the pin,
command, hashes, sizes, platform, architecture, Python version, and result,
without a machine nickname or private path.

The formal local architecture is `aarch64`. The pull-request workflow must
reproduce the pinned verifier and `EXPECTED.txt` byte for byte on GitHub
`x86_64`. Only that two-architecture agreement makes a finite computation
eligible for a later `[T]` fold.

## 11. Scope boundary and later routing

This probe can establish only the exact decomposition of the frozen
historical compression. A valid result may later support a separately named
claim such as `CURVATURE-HISTORICAL-GAUSS-SPLIT`, at exactly this carrier,
measure, group, and operator scope.

It cannot close `CURVATURE-OPERATOR-CANONICAL`. That obligation requires a
separate classification probe over publicly admissible carriers, measures,
projection groups, and commutator types, with `UNIQUE`, `NONUNIQUE`, `EMPTY`,
and `STOP` routing fixed before execution.

No normative Canon, registry, dependency, evidence, ledger, frontier, or
status file changes on this ruling branch or on the later probe branch. Any
earned status is applied only in a separate reviewed Canon fold.

## 12. Freeze protocol

Required order:

1. reciprocal byte review of this ruling candidate;
2. ruling PR, required check, merge commit, and public byte read-back;
3. drafting of `PREREG.md` and exact `verify.py` without execution;
4. reciprocal byte review of both files;
5. immutable preregistration commit and remote byte read-back;
6. first formal aarch64 execution;
7. `EXPECTED.txt`, `RUN.md`, and `RESULT.md` on the same probe branch;
8. policy/self-check, probe PR, and byte-identical GitHub x86_64 execution;
9. merge without squash or rebase;
10. later normative fold, if warranted.

After step 5, any change to the carrier, map, convention, projector, basis,
operator, route, observable, zero predicate, identity, threshold, or decision
logic invalidates the run surface and requires a new probe ID. Thresholds do
not move and failed branches are archived rather than deleted.
