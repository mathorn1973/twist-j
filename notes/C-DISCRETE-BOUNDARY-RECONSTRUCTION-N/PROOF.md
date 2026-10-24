# Conditional reconstruction and exact Gauss fibres

Status: NON-CANONICAL / NO AUTHORITY. Proof status: candidate-T.
Action layer: L1. Scope and equality are exactly those of [PREREG.md](PREREG.md).
The proof was written from its frozen commit
`e092feb641e859d7d959e72f3ab39ec88d4fc53c`, without reading either candidate
implementation or executing scientific code. Finite audit results, when
obtained, are separate candidate-C evidence and do not prove the size
quantifiers below.

All coordinates are in the field F = F5 unless stated otherwise. Edge
coordinates are independent directed labels. Equality is literal equality,
with no gauge quotient. The geometric boundaries here are selected subsets
of finite L1 carriers, not an identification with the protocol's L3 layer.

## 1. Exact restriction, fixed-boundary operations and dynamics

Let X be a nonempty subset of F^V, let B be a subset of V, and let
R:X -> F^B be coordinate restriction. There is a map D:R(X) -> X satisfying
D R = id_X if and only if R is injective.

Indeed, a left inverse gives Rx = Ry => x = D Rx = D Ry = y. Conversely,
injectivity assigns each b in R(X) exactly one preimage D(b). This also
proves R D = id_R(X), uniqueness of D, and |X| <= 5^|B|. The bound alone
does not imply that this particular coordinate restriction is injective.

For a nonempty affine class X = {x : Hx = b}, fix x0 in X. Then
X = x0 + ker H. Two members have the same restriction exactly when their
difference belongs to ker H intersect ker R. Consequently

```text
R is injective on X  iff  ker H intersect ker R = {0}.
```

Here the second R denotes the same coordinate map on the full ambient
vector space. Equivalently, the stacked matrix (H,R) has full column rank.
If K is this common kernel, every nonempty fibre of (H,R) is a translate
of K by any one of that fibre's members and has exactly 5^dim(K) members.

Suppose now that R is injective and P:X -> X satisfies R P = R. For every
x, injectivity applied to R(Px) = R(x) gives Px = x. Thus P = id_X. This
conclusion concerns precisely maps preserving both X and its entire frozen
boundary reading; it does not prohibit operations that change that reading.

For any specified U:X -> X, define U_B = R U D on R(X). The inverse
identities above give

```text
R U = U_B R,       D U_B = U D.
```

If U is bijective, R U^(-1) D is the inverse of U_B. Conversely, if U_B is
bijective then U = D U_B R is bijective. These are conjugacy statements;
they do not imply locality of a boundary update.

## 2. Mixed-cube reconstruction for every N >= 2

Use V_N = {0,...,N-1}^3 and the union
B_N = {i = 0 or j = 0 or k = 0}. Each point in an intersection is one
point, carrying one value. Define forward differences only where their
arguments lie in V_N. The frozen eight-vertex equation is
Delta_0 Delta_1 Delta_2 f = 0 on every unit cube.

For i,j,k > 0, sum this equation over all lower vertices
0 <= a < i, 0 <= b < j, 0 <= c < k. Telescoping in the three coordinates
leaves exactly

```text
f(i,j,k)-f(i,j,0)-f(i,0,k)-f(0,j,k)
          +f(i,0,0)+f(0,j,0)+f(0,0,k)-f(0,0,0) = 0.
```

Hence every admissible f obeys the reconstruction formula

```text
D(b)(i,j,k) = b(i,j,0)+b(i,0,k)+b(0,j,k)
             -b(i,0,0)-b(0,j,0)-b(0,0,k)+b(0,0,0).       (1)
```

If any coordinate is zero, (1) reduces to the given value at that boundary
point by cancellation. Thus it defines a field extending every arbitrary
assignment b on the union B_N. Every summand in (1) is independent of at
least one coordinate, so its third mixed difference vanishes. The field
therefore satisfies every unit-cube constraint. Existence and uniqueness
are proved for every N >= 2, including all face intersections.

The maps D and R are linear inverses. Counting the complement of B_N gives

```text
|B_N| = N^3 - (N-1)^3 = 3N^2 - 3N + 1,
dim X_N = 3N^2 - 3N + 1,
rank H_N = N^3 - dim X_N = (N-1)^3,
ker H_N intersect ker R = {0},
|X_N| = 5^(3N^2 - 3N + 1).
```

There are exactly (N-1)^3 constraint rows, so these rows are independent.
The fields D(delta_b), one for each boundary unit vector, form a complete
basis of X_N. Checking a linear identity on this entire basis proves that
identity on X_N; it is not a sample of selected configurations.

The selected map U_2(f) = 2f preserves the constraints. Its inverse is
U_3(f) = 3f because 2*3 = 1 in F5. Equation (1) is linear, so

```text
R U_2 = (2 id) R,       D (2 id) = U_2 D,
U_3 U_2 = U_2 U_3 = id_X_N.
```

The third coordinate has not been designated a time coordinate. This is a
restriction on a spatially indexed comparison class, with a separately
chosen update.

## 3. Incidence lemma and a complete cycle basis

Let a connected finite graph have v >= 1 vertices and e directed edge
labels, with incidence -1 at a tail and +1 at a head. Parallel or opposite
labels are not identified. Choose a spanning tree T in its underlying
graph, retaining one directed label for each tree edge.

The sum of all incidence rows is zero, giving rank d <= v-1. The v-1 tree
columns are independent: in a linear dependence, a leaf row forces its
unique tree coefficient to be zero, and deleting leaves proves that every
coefficient is zero. Therefore

```text
rank d = v-1,       dim ker d = e-v+1,
im d = {rho : sum_vertex rho = 0}.                         (2)
```

The image equality follows because the right side has dimension v-1.

For each edge label a outside T, let p_a be the signed tree path from its
tail to its head. A path coefficient is +1 when traversed with its retained
label and -1 when traversed against it. With epsilon_a the edge unit vector,
put c_a = epsilon_a - p_a. Then d c_a = 0. The coordinates of these vectors
on non-tree labels form the identity matrix, proving independence. For any
z in ker d, subtract sum_(a outside T) z_a c_a. The remainder is a cycle
supported on T and must vanish by the same leaf argument. Thus the c_a
are a complete basis, with no unclassified cycle or topology sector.

This proof uses no special property of five beyond the field operations.
The empty graph is treated separately below; formula (2) is not applied
with v = 0.

## 4. Complete Gauss-box fibres

For the nonperiodic edge carrier of PREREG section 4, the full graph has
N^3 vertices and 3N^2(N-1) edges. The literal reader Q_N returns each edge
with at least one endpoint in the outer vertex boundary O_N. Its unobserved
edges are exactly the induced graph on I_N = {1,...,N-2}^3.

Fix a nonempty fibre F(rho,q) and one member E0. Subtraction gives

```text
F(rho,q) = E0 + K_N,
K_N = {c : dc = 0 and Q_N c = 0}.                          (3)
```

The condition Q_N c = 0 sets every observed coordinate to zero. Extension
by zero identifies K_N with the incidence kernel of the induced interior
graph: its remaining columns have both endpoints in I_N, so no additional
equations occur at outer vertices.

For N = 2 there are no interior vertices and no unobserved edges. Thus
K_2 = {0}, its dimension is zero, and every nonempty fibre is a singleton.
This case is not obtained by substituting m = 0 into e-v+1.

For N >= 3 put m = N-2 >= 1. The interior grid is connected, has m^3
vertices and 3m^2(m-1) edges. Equation (2) gives

```text
rank d_interior = m^3-1,
k_N = dim K_N = 3m^2(m-1)-m^3+1 = 2m^3-3m^2+1,
|F(rho,q)| = 5^k_N.                                       (4)
```

In particular N = 3 has one interior vertex, no interior edges, rank zero
and k_3 = 0. A complete explicit basis in every other size is furnished
by section 3 as follows. Root the interior tree at (1,1,1). For every
other vertex v, take the edge from v-e_a to v, where a is the least axis
with v_a > 1. Coordinate sum decreases along parents, so these edges form
a spanning tree. Take its fundamental cycles for every remaining interior
edge and extend each by zero to the full graph. These vectors form the
complete basis of K_N in (3). For N = 2 and N = 3 the basis is empty.

For completeness, nonemptiness can also be decided without choosing E0.
Extend q by zero on unobserved edges and call this full vector qbar. Put
eta = rho - d qbar. If N = 2, nonemptiness is exactly eta = 0. If N >= 3,
it is exactly

```text
eta vanishes outside I_N and sum_(v in I_N) eta(v) = 0.
```

Necessity follows from the support of the unseen columns; sufficiency
follows from their image in (2). When these conditions fail the fibre is
empty, and when they hold (3)-(4) classify all of it.

### The frozen box witness

Writing epsilon_(v,a) for a full edge unit vector, the N = 4 witness is

```text
c = epsilon_((1,1,1),0) + epsilon_((2,1,1),1)
    -epsilon_((1,2,1),0) - epsilon_((1,1,1),1).             (5)
```

Its four distinct edges follow the prescribed square, with a minus sign
exactly on backward traversals of forward-labelled edges. Incidence
cancels successively around the square, so dc = 0. Every endpoint has
coordinates in {1,2}, giving Q_4 c = 0. All four coefficients are nonzero,
so its support has size four and c differs from the complete zero field.
Both belong to the same zero-charge, zero-observation fibre.

## 5. The exact public torus and its two different restricted classes

The source is the pinned
[Maxwell reproduction](https://github.com/mathorn1973/twist-j/blob/7d7f588c42422c2cf37b04d76ebc13ca55eb96dc/reproduce/maxwell/README.md),
with the original carrier in
[verify.py](https://github.com/mathorn1973/twist-j/blob/7d7f588c42422c2cf37b04d76ebc13ca55eb96dc/reproduce/maxwell/verify.py).
The registered MAXWELL-GAUSS-CHAIN and Gauss part of MAXWELL-OBSTRUCTION-P
already establish their stated torus incidence and solvability results.
The whole-torus dimension below is a source re-audit, not a new result
earned for either registered claim. The marked-region and fixed-cut
comparisons use the complete restatement frozen in PREREG section 5.

There are eight vertices T = {0,1}^3 and 24 independent directed labels
(v,a), one for each vertex and a in {0,1,2}, with head v+e_a modulo two.
In particular (v,a) and (v+e_a,a) are distinct, opposite wrapping labels.
Replacing this carrier by the twelve edges of a simple cube changes the
problem.

The graph is connected. By (2), rank d_T = 7 and dim ker d_T = 24-7 = 17.
A complete basis is the section 3 construction with root (0,0,0) and the
seven tree edges (v-e_a,a), where for each nonroot v the axis a is the
least one with v_a = 1. Coordinate sum decreases along the parents. The
17 remaining directed labels therefore index 17 independent spanning
cycles. Gauss on the whole torus is solvable exactly when total charge
vanishes, and each such fibre is a translate of this 17-dimensional kernel.

### The marked region

Write R_reg = {v : v_0 = 0} for the marked R of PREREG. It has four
vertices and eight internal labels, those with axes 1 or 2. The eight
axis-0 labels form cut(R_reg); the remaining eight labels are internal to
the complementary slice. Each slice is connected. Hence its internal
incidence rank is three and

```text
dim Z_R = 8-3 = 5.                                        (6)
```

Here is a complete basis without suppressing any opposite wrapping label.
For s in {0,1}, write

```text
A_s=(s,0,0), B_s=(s,1,0), C_s=(s,0,1), D_s=(s,1,1).
```

On that slice define the following five full edge vectors, zero on all
unlisted coordinates:

```text
p1_s = epsilon_(A_s,1) + epsilon_(B_s,1),
p2_s = epsilon_(C_s,1) + epsilon_(D_s,1),
p3_s = epsilon_(A_s,2) + epsilon_(C_s,2),
p4_s = epsilon_(B_s,2) + epsilon_(D_s,2),
w_s  = epsilon_(A_s,1) + epsilon_(B_s,2)
       + epsilon_(D_s,1) + epsilon_(C_s,2).                (7)
```

Each p is a two-edge wrapping cycle; w_s is the four-edge square
A_s -> B_s -> D_s -> C_s -> A_s. All have zero divergence. The four p
vectors have disjoint supports. Their coefficients on each opposite pair
are equal, whereas w_s has coefficients one and zero on the pair
(A_s,1),(B_s,1). Subtracting those two coordinates in any linear relation
first forces the coefficient of w_s to vanish, and the other four
coefficients then vanish by their disjoint supports. By (6), the five
vectors with s = 0 form the complete basis of Z_R. Adding any vector in
Z_R fixes the whole complement and every individual crossing edge.

The prescribed torus witness is exactly w_0. Its four labels are distinct,
all coefficients are +1, its divergence is zero and all its cut values
are zero. Its complete support is internal to R_reg. The wrapping labels
at D_0 and C_0 are essential to this specification.

### The full fixed-cut kernel

Let Q_cut read each of the eight crossing labels individually on the
whole 24-coordinate carrier. Imposing Q_cut c = 0 leaves two disjoint
internal slice graphs. Their divergence equations do not mix. Therefore

```text
ker(d_T,Q_cut) = Z_R direct-sum Z_complement,
dim ker(d_T,Q_cut) = 5+5 = 10.                             (8)
```

The ten vectors in (7), for both values of s, form its complete basis.
Equivalently the full stacked reader (d_T,Q_cut) has rank 24-10 = 14.
This class is larger than Z_R because it does not require the complete
complement to remain fixed.

Every nonempty full fibre {E : d_T E = rho, Q_cut E = q} is a translate of
(8) and has exactly 5^10 members. More explicitly, extend q by zero on
both slices and set eta = rho-d_T qbar. The fibre is nonempty exactly when
the sum of eta on each slice is zero, by (2) applied separately to the
two slices. This also describes all empty fibres of this reader.

## 6. Aggregate flux, literal readers and the chosen four-phase histories

For any vertex subset S in either edge carrier, summing incidence gives
the exact integrated law

```text
sum_(v in S) (dE)(v)
  = sum_e (1_S(head(e))-1_S(tail(e))) E(e).                (9)
```

Internal edges cancel, and only crossing edges contribute on the right.
Thus a total flux is a linear combination of individual crossing values.
It is not the complete coordinate reader. The box reader is stronger
still: it also includes every edge lying in the outer vertex boundary.
The witnesses (5) and w_0 fix all the respective observed coordinates,
so their invisibility survives any aggregation of those observations.
Equation (9) alone supplies no reconstruction of an interior circulation.

For example, on either zero-charge class the mathematical translation
P_c(E)=E+c, with its respective witness c, preserves the class and its
entire reader but is not the identity. This is an explicit failure of
injectivity in that Gauss-only class, consistent with section 1. No
physical or native admission of this operation is asserted.

The separately chosen U_2(E)=2E preserves each zero-charge class and each
zero-observation kernel; U_3(E)=3E is its inverse. In a general affine
box or torus fibre it maps F(rho,q) bijectively to F(2rho,2q), rather than
preserving an arbitrary nonzero data pair. This follows directly from
linearity of incidence and of the complete reader.

For either nonzero witness, its whole orbit is

```text
c, 2c, 4c, 3c, c, ... .
```

The scalar 2 has multiplicative order four in F5, and a nonzero coordinate
of c prevents any earlier return. Thus the least period is exactly four.
Every member has the same four-edge support, zero divergence and zero
complete boundary reading. The zero field is fixed and remains distinct
from every member at every tick. This proves all-time invisibility for
this specified comparison update, not for original U or Maxwell dynamics.

## 7. Dependence on five and the unprovided native bridge

The inverse criterion and fixed-boundary argument are set-theoretic. The
mixed-difference telescoping and extension use only addition and
subtraction. Their linear dimension statements, the graph ranks and the
cycle bases hold over any field. The counts 5^k use the size of F5; the
chosen inverse multiplier 3 and the four-phase orbit of multiplier 2 use
arithmetic in this particular field. No argument selects five physically.

All size-dependent statements concern the separately declared growing
boxes. The exact Maxwell comparison uses its frozen 24-label torus.
Neither carrier has been derived from the original autonomous system
Omega = N_0 times F5^6. Its full counter, coordinate equality and original
update U remain unchanged. A native scalable carrier, independently
selected region, complete native reader and intertwining with actual U
are NOT_PROVIDED. Their absence is not an impossibility theorem for every
native reading.

The positive and negative reconstruction conclusions concern literal
classical finite configurations at L1. They adopt no physical entropy,
quantum-state recovery, area coefficient, SI scale, local physical
operation or spacetime dimension. No cross-layer conclusion or public
status promotion follows from this note.
