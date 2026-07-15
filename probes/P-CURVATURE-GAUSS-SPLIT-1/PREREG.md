# P-CURVATURE-GAUSS-SPLIT-1 preregistration

Status: PRE-PIN DRAFT

This document freezes the complete decision surface for the exact Gauss split
of the already public historical curvature operator. It contains no gate
output and earns no scientific status. Formal execution is forbidden until
this document and the accepted verifier pass reciprocal byte review, are
committed and pushed as one immutable preregistration pin, and that remote pin
is read back.

## Public identity and action layer

```text
program:          CURVATURE-GAUSS-SPLIT
probe:            P-CURVATURE-GAUSS-SPLIT-1
public lock:      issue 22
owner:            master C
branch:           probe/P-CURVATURE-GAUSS-SPLIT-1
path:             probes/P-CURVATURE-GAUSS-SPLIT-1/
initial base:     57de0af8a50e14e52f0fa81e0158f6a370cab5a5
action layer:     L2
scientific state: O
```

Pinned owner ruling, the definitional source of every term below:

```text
ruling merge SHA:  57de0af8a50e14e52f0fa81e0158f6a370cab5a5
ruling file:       notes/canon/P-CURVATURE-GAUSS-SPLIT-RULING-1.md
ruling SHA-256:    94ae6278c5ec27262d7eeb443e1a8461a84c2f59df6f315fb5fda24f63bcb02e
ruling size:       17392 bytes, 541 lines, 0 CR bytes
```

The ruling is based on Public Canon 2, tag `canon-v2`, activation commit
`5abb22319007fd3172f7123f4b3a71b547fb94af`, content commit
`7cfe2a62a456d0f84b1f60b4945dcdfe896e99db`, and Canon SHA-256
`abd0e026ccc2be00cdb0d9d13d634e0a71602b1565e6d53ac23a99b506281021`.

The incorporated historical curvature result is pinned by its public files:

```text
trace ruling SHA-256:   cf15037f5cc2690a9633ca68ef13107920ce9ce81116963dc9d8490c088eeccb
trace PREREG SHA-256:   94ec5263d2b2931bcd3863cb5f78e2326944479aa28aef987495c8601c65f8c9
trace verifier SHA-256: c9b4d253a609cc489efc4386e5e61d3e92baa16b736b899048f2a3afa5e78c99
trace RESULT SHA-256:   5d3c406233958bee62076a624012c28bf38c7c770bb79d35f62cf49e699e6baf
```

No canonical-operator selection, spectrum, continuum lift, boundary lift,
physical decoder, fitted normalization, or curvature-sign interpretation is
included.

## Frozen carrier and operators

Work over

```text
X = F_5^6,
x = (p1,p4,p1p,p4p,q,r),
F = Q^X,
<f,g> = sum_(x in X) f(x) g(x).
```

All state arithmetic is modulo 5. The exact public affine involutions are

```text
a(p1,p4,p1p,p4p,q,r) = (p4,p1,p4p,p1p,q,r)

b(p1,p4,p1p,p4p,q,r) = (-p1p,-p4p,-p1,-p4,-q,-r)

c: piston -> b4(piston) + (2,1,2,1) + r(0,1,0,-1)
   q       -> 1-q
   r       -> -r

d(x) = (2,1,3,4,1,1) - x
e(x) = (2,1,3,4,2,1) - x.
```

Freeze

```text
(g o h)(x) = g(h(x)),
(T_g f)(x) = f(g^-1 x),
T_g T_h = T_(g o h),

A = T_a,
C = T_c,
H = <b,d>,
R_H = (1/20) sum_(h in H) T_h,
Pi_1(f) = (1/|X|) (sum_(x in X) f(x)) 1_X,
P0 = I_F - Pi_1,
P = P0 R_H = R_H P0,
Q = I_F - P,
V = im(P) = F^H intersect 1_X^perp.
```

The verifier derives and audits

```text
|X| = 15625,
|H| = 20,
X/H = 1 orbit of size 5, 74 of size 10, 744 of size 20,
dim F^H = 819,
dim V = 818,
P^2=P=P*, Q^2=Q=Q*, P+Q=I_F, PQ=QP=0.
```

The map `e` is integrity-only. It does not enter the group or any operator.

Every route input and intermediate to which the verifier applies `P` or `Q`
has counting mean zero, and that fact is audited before projection. On this
audited subspace `P=R_H` and `Q=I_F-R_H`; this is an implementation
simplification only. The global frozen definitions remain `P=P0 R_H` and
`Q=I_F-P`.

Form products in `End(F)` and restrict every scientific operator to `V`:

```text
K_amb = P[A,C]P |_V,
K_int = [PAP,PCP] |_V,
K_ext = (PAQCP-PCQAP) |_V,
K_amb = K_int + K_ext.
```

Define the leakage maps

```text
L_A = QAP |_V : V -> V^perp,
L_C = QCP |_V : V -> V^perp,
K_ext = L_A*L_C - L_C*L_A.
```

All three `K` operators must be total and skew-adjoint on `V`.

## Canonical basis and exact coordinates

Order the 819 `H`-orbits `O_0,...,O_818` by their least states and put
`s_i=|O_i|`. Freeze the ordered integer basis

```text
w_i = s_0 1_(O_i) - s_i 1_(O_0), i=1,...,818.
```

Let `G_ij=<w_i,w_j>`. Every matrix adjoint is checked against the exact Gram
matrix:

```text
M^T G + G M = 0.
```

No Euclidean-transpose shortcut or floating orthonormalization is allowed.

## Route A: direct leakage propagation

For every basis column, represent the function exactly on the full carrier.
Apply the displayed operators in order and construct independent exact
rational matrices

```text
M_amb_A, M_int_A, M_ext_A.
```

The exterior column is computed directly by

```text
w_i -> C -> Q -> A -> P
w_i -> A -> Q -> C -> P
```

and subtraction. Route A must not define `M_ext_A` as a residual.

It also constructs `L_A w_i` and `L_C w_i` directly and checks for every
ordered basis pair

```text
<w_i,K_ext w_j>
  = <L_A w_i,L_C w_j> - <L_C w_i,L_A w_j>.
```

## Route B: complete orbit transitions

For every `g` in `{a,c,a o c,c o a}`, count every transition

```text
n^g_ij = #{x in O_j : g(x) in O_i}.
```

The orbit-average coordinate of `P T_g` on `O_i` is `n^g_ij/s_i`. After the
exact mean-zero projection and change to the frozen basis, construct

```text
B_a  = matrix(PAP |_V),
B_c  = matrix(PCP |_V),
D_ac = matrix(PACP |_V),
D_ca = matrix(PCAP |_V).
```

Then form

```text
M_amb_B = D_ac-D_ca,
M_int_B = B_a B_c-B_c B_a,
M_ext_B = (D_ac-B_a B_c)-(D_ca-B_c B_a).
```

Route B does not read Route A columns or observables. Before any decision,
require entrywise equality of the two routes for all three matrices and the
entrywise identity `M_amb=M_int+M_ext`.

## Frozen observables

For each `K` compute exactly over `Q`

```text
Tr_V(K^2), rank_V(K), nullity_V(K)=818-rank_V(K).
```

Also compute

```text
cross = 2 Tr_V(K_int K_ext),
Tr(MN) = sum_(i,j) M_ij N_ji.
```

The exact control identity is

```text
Tr(K_amb^2)
  = Tr(K_int^2) + cross + Tr(K_ext^2)
  = -881/8.
```

Only the last ambient value is prior public knowledge. No split trace, cross,
rank, nullity, or decision outcome is predicted.

## Exact rank and kernel certificates

All rational matrix rows are cleared to primitive integer rows without
changing rank. Packed elimination over `F_2` and `F_3` supplies only auxiliary
one-sided lower bounds on rational rank; it is never the final rank method.

For every matrix the verifier performs deterministic exact rational Gaussian
elimination, implemented fraction-free on primitive integer rows and followed
by exact `fractions.Fraction` back substitution. Columns are taken in basis
order and the first available row in row order. Each fraction-free row update
is an invertible rational row operation, followed only by division by a common
integer row content. The resulting echelon system returns the exact rational
rank and exactly `nullity` kernel vectors. The verifier checks that the two
modular lower bounds do not exceed the rational rank, that the kernel vectors
are linearly independent through their distinct free coordinates, that all
are annihilated by the original matrix, that they span the full kernel under
the same echelon system, and that `rank+nullity=818`.

For every skew-adjoint matrix, require

```text
rank is even,
Tr(K^2) <= 0,
K=0 iff rank(K)=0 iff Tr(K^2)=0.
```

Zero tests use exact matrix equality. The cross term may have either sign;
the trace summands are not percentages or normalized curvature shares.

## Integrity tally

The verifier evaluates exactly fifteen ordered gates before routing:

1. `I01`: pinned ruling/public authority constants;
2. `I02`: full carrier and exact total affine maps;
3. `I03`: involutions, composition, and Koopman convention;
4. `I04`: exact group, closure, orbit partition, census, and ordering;
5. `I05`: projector identities and dimensions;
6. `I06`: integer basis completeness and exact positive-definite Gram form;
7. `I07`: total typing of the three endomorphisms and two leakage maps;
8. `I08`: complete direct Route A with explicit `Q` propagation;
9. `I09`: complete transition Route B;
10. `I10`: entrywise route agreement for all three matrices;
11. `I11`: operator identity, leakage bilinear identity, and Gram skewness;
12. `I12`: exact trace/cross identity and public `-881/8` anchor;
13. `I13`: exact rank, kernel, nullity, parity, and zero certificates;
14. `I14`: standard-library-only integer/Fraction exactness;
15. `I15`: deterministic stdout, empty stderr, and audit-before-decision.

Any failed gate is `STOP`. A route mismatch cannot be repaired by choosing a
route, averaging, changing a projector, or redefining `K_ext`.

## Frozen decision routing

```text
DECISION INTRINSIC
  all gates pass and K_ext=0.
  This means K_amb=K_int. Separate leakage diagnostics report whether
  L_A=L_C=0 or nonzero leakage contributions cancel.

DECISION MIXED
  all gates pass, K_int!=0, and K_ext!=0.

DECISION PROJECTION-INDUCED
  all gates pass, K_int=0, and K_ext!=0.

DECISION STOP
  any integrity or execution gate fails, including the simultaneous
  K_int=K_ext=0 contradiction with the public ambient anchor.
```

The first three outcomes exit zero and print `RESULT VALID`. `STOP` exits
nonzero, may print the process marker `DECISION STOP`, and prints no valid
scientific outcome.

## Prior knowledge and exclusions

Known before pin:

```text
dim V=818,
Tr(K_amb^2)=-881/8,
the historical -21/8 proposal is false,
the unrelated ten-mode checksum is -22.
```

Forbidden after pin: changing the carrier, group, measure, projection,
commutator type, basis, rank method, zero predicate, route, threshold, or
decision logic; quotienting by a new symmetry; fitting a scale; inserting a
target split value; computing a spectrum; or promoting any historical
operator to the canonical curvature operator.

## Formal execution and evidence

The accepted code is `verify.py` in this directory. Before the immutable pin,
only byte hashing, AST inspection, and syntax compilation without import or
execution are allowed.

The verifier is deliberately free of filesystem and network input. `I01`
checks the exact embedded tag, activation/content commits, Canon hash, ruling
pin, and incorporated public curvature-probe pins against the reviewed
declaration in its own immutable bytes. Git ancestry, source-file hashes, and
remote authority are checked externally during reciprocal byte review, pin
read-back, and the repository workflow.

On a valid run, stdout order is frozen as follows: probe and ruling headers;
the complete `AUDIT` vector and `AUDIT PASS`; `AUTHORITY` and `SOURCES`
read-back lines; carrier, group, projector, route, agreement, leakage, and
skew certificates; the four exact trace terms; an explicit reconstructed
`TRACE_IDENTITY`; three exact rank/nullity records with auxiliary modular
lower bounds; the frozen scientific `DECISION`; and `RESULT VALID`. A failed
audit stops immediately after the audit lines with `DECISION STOP` and
`RESULT INVALID`, before any scientific observable is printed.

After reciprocal byte review, commit and push exactly `PREREG.md` and
`verify.py`. Read back the remote commit and both hashes. Only then may the
formal aarch64 runner execute

```text
python3 probes/P-CURVATURE-GAUSS-SPLIT-1/verify.py
```

in a neutral deterministic environment. Exact stdout becomes `EXPECTED.txt`;
`RUN.md` records the immutable pin, command, neutral platform, architecture,
Python version, exit code, stderr, hashes, and byte counts. `RESULT.md` states
the frozen outcome without scope inflation.

The probe PR changes only the five files in this directory. GitHub x86_64
must reproduce the pinned verifier and `EXPECTED.txt` byte for byte. Only the
two-architecture agreement makes the finite result eligible for a later
normative fold. `CURVATURE-OPERATOR-CANONICAL` remains `[O]` in every branch.
