# The exact global fixed-reader quotient

**NON-CANONICAL. Proposed status: candidate-T. Action layer: L1.**

This is an analytical derivation in the candidate
`C-U-SELECTOR-READING-STRUCTURE-N`. The reported count of thirteen components
was exposed before this work. This proof makes no blind-count claim and
does not execute or dispose of the separately owned
`P-U-J-HODGE-SEPARABLE-COUNTER-READ-1` probe. Its additional content is an explicit
piecewise-affine invariant and a constructive completeness proof.

The native formulas are those in [Public Canon](../../canon/CANON.md),
`DEF-ARCHITECTURE` and the displayed five affine generators. The
313-component theorem used below is `U-NATIVE-INVARIANT-AND-NOWRITE`, with
its exact coordinate proof in
[MEMORY-PROOF, sections 1-2](../../probes/P-U-NATIVE-MEMORY-EVENT-1/MEMORY-PROOF.md).
All computations in this proof are identities over `F5`.

## 1. The graph and the proposed invariant

Let `X=F5^6`, with the native coordinate order
`x=(p1,p4,p1p,p4p,q,r)`. Put

```text
A=p1+p1p,       B=p4+p4p,
C=p1-p1p-2,     D=p4-p4p-1,
S=A+B,         T=C+D,
z=S+q+r.
```

The tuple `(A,B,C,D,z,r)` is an affine coordinate system. In particular,

```text
p1=3(A+C+2),    p1p=3(A-C-2),
p4=3(B+D+1),    p4p=3(B-D-1),
q=z-A-B-r.
```

Define the oriented two-coordinate reading `kappa:X->F5^2` by

```text
                 (S-1, -T-2r)   if z=0,
kappa(x) =       (S,    T)       if z=1 or z=2,
                 (S,   -T)       if z=3 or z=4.
```

Write `Q(x)=[kappa(x)]` for its simultaneous-sign class in
`F5^2/{+1,-1}`. This is a piecewise-affine reading, with pieces selected
by the native phase. It is not claimed to be the sign quotient of a single
global affine map on `X`.

For `t in {0,1}`, let `f_t(x)=g_(z(x)+2t)(x)`. Let `G` be the directed
graph with the two edges `x->f_t(x)` from each checkpoint. A weak component
means a connected component after forgetting edge orientation. This is
the equality graph relevant to a reading satisfying `F(f_t(x))=F(x)` for
both controls at every checkpoint.

**Claim.** The weak components of `G` are exactly the fibres of `Q`.

## 2. Invariance is an identity in ten cases

Substitution of the five native generator formulas gives the following
coordinate actions. Only the listed phase/control pairs select each row.

| Generator | `(A',B',C',D',r')` | `z'` |
| --- | --- | --- |
| `a` | `(B,A,D-1,C+1,r)` | `z` |
| `b` | `(-A,-B,C,D,-r)` | `-z` |
| `c` | `(-A-1,2-B,C,D+2r,-r)` | `2-z` |
| `d` | `(-A,-B,-C,-D,1-r)` | `2-z` |
| `e` | `(-A,-B,-C,-D,1-r)` | `3-z` |

Therefore the complete phase/control table is

| `z` | `t` | Selected generator | `z'` | `kappa(f_t(x))` |
| --- | --- | --- | --- | --- |
| `0` | `0` | `a` | `0` | `kappa(x)` |
| `0` | `1` | `c` | `2` | `-kappa(x)` |
| `1` | `0` | `b` | `4` | `-kappa(x)` |
| `1` | `1` | `d` | `1` | `-kappa(x)` |
| `2` | `0` | `c` | `0` | `-kappa(x)` |
| `2` | `1` | `e` | `1` | `-kappa(x)` |
| `3` | `0` | `d` | `4` | `-kappa(x)` |
| `3` | `1` | `a` | `3` | `kappa(x)` |
| `4` | `0` | `e` | `4` | `-kappa(x)` |
| `4` | `1` | `b` | `1` | `-kappa(x)` |

For example, from `z=0`, the selected `c` has
`S'=1-S`, `T'=T+2r`, and `z'=2`, so its reading is
`(1-S,T+2r)=-(S-1,-T-2r)`. From `z=2`, the selected `c` has
`r'=-r`, and its reading on `z'=0` is
`(1-S-1,-T-2r+2r)=(-S,-T)`. The other rows follow immediately
from the same table.

Hence `Q` is invariant on every edge and on every weak component. No
properties of the Thue-Morse word are needed for this identity.

## 3. Reduction to the synchronized sheets

Let `X14={x:z(x) in {1,4}}`. Every checkpoint is connected to `X14`:

```text
z=0:  c then e,   giving 0 -> 2 -> 1;
z=2:  e,          giving 2 -> 1;
z=3:  d,          giving 3 -> 4.
```

On `X14` put

```text
V(x)=(A,B,chi(z)C,chi(z)D),
chi(1)=1, chi(4)=-1.
```

The prior theorem identifies its controlled strongly connected components
as the classes `[V]` under simultaneous sign. Its proof is elementary:
in coordinates `(z,V,r)` the two available operations are

```text
B0(z,V,r)=(5-z,-V,-r),
C0(z,V,r)=(z,-V,1-r).
```

Their composition sends `(z,V,r)` to `(5-z,V,r+1)`. Its first ten
powers realize every `(z,r)` at fixed `V`, and one further operation
realizes `-V`. Consequently a representative of `[V]` may be taken at
either phase with any `r`.

On these sheets the new reading is simply

```text
kappa(x)=(V1+V2, V3+V4).
```

It remains to determine which of these 313 terminal components the
transient sheets identify in the full weak graph.

## 4. The two transient excursions generate the missing translations

Write `V=(alpha,beta,gamma,delta)`. We exhibit two families of
identifications between terminal components. They are relations between
sign classes, not claims that the displayed affine maps individually
descend to maps on the sign quotient.

First take a terminal representative at `z=4`. The undirected path

```text
terminal z=4 --d (backwards)--> z=3 --a--> z=3 --d--> terminal z=4
```

is legal in the weak graph. Using the coordinate table, its effect on `V`
is

```text
H(V)=(beta,alpha,delta-1,gamma+1).
```

Thus `[V]` and `[H(V)]` lie in the same full weak component for every
`V`.

Next take a terminal representative at `z=1` with `r=s`. The path

```text
z=1 --e (backwards)--> z=2 --c--> z=0 --a--> z=0 --c--> z=2 --e--> z=1
```

has effect

```text
G_k(V)=(beta+3,alpha-3,delta+k,gamma-k),
k=2s-1.
```

For a direct check, the intermediate checkpoint on `z=0` after `c e`
has coordinates

```text
A=alpha-1, B=beta+2, C=-gamma,
D=-delta+2-2s, r=s-1.
```

Applying `e c a` gives the displayed `G_(2s-1)`. Since `s` ranges over
all five values within the original terminal component, all `k in F5`
are available.

Composition on oriented representatives gives

```text
G_k(H(V)) = V + (3,-3,k+1,-k-1).
```

For `k=-1`, this is translation by `(3,-3,0,0)`, which generates
the complete line `(a,-a,0,0)` because `3` is invertible in `F5`.
Combining the `k=0` translation with the inverse `k=-1` translation gives
`(0,0,1,-1)`, which generates the other line. Thus weak connectivity
contains translation by every element of

```text
N={(a,-a,b,-b):a,b in F5}
 = kernel(V -> (V1+V2,V3+V4)).
```

Suppose two terminal representatives have the same `Q`. After replacing
one by its negative, their oriented sums agree. Their difference belongs
to `N`, so the translations above connect their terminal components. If
their sums vanish, the same argument applies without a sign adjustment.
Section 3 connects every nonterminal checkpoint to a terminal one.
Together with invariance from section 2, this proves the claim: the full
weak components are exactly the `Q` fibres.

## 5. Fibre sizes and the thirteen-class count

Fix an oriented output `(u,v)`, a phase `z`, and a value of `r`. In the
coordinates `(A,B,C,D,z,r)`, the equations `kappa(x)=(u,v)` specify
exactly one value of `A+B` and one value of `C+D`. They leave `A` and
`C` free, hence have exactly `5^2=25` solutions. Summing over five
values of `r` and five phases yields

```text
|kappa^(-1)(u,v)| = 25 * 5 * 5 = 625.
```

This proves surjectivity and constant oriented fibre size. The zero vector
is its own sign class; each of the remaining 24 vectors has a distinct
negative. Therefore

```text
number of weak components = 1+(25-1)/2 = 13;
component sizes           = one 625 and twelve 1250;
total checkpoints         = 625+12*1250 = 15625.
```

Each oriented fibre meets every phase in exactly 125 points. Every `Q`
fibre therefore contains all five phase values. These conclusions follow
from the formula and connectivity proof, without graph enumeration.

## 6. A sign-free separating record

For `kappa(x)=(u,v)`, the symmetric matrix

```text
M(x)=kappa(x) kappa(x)^T = [[u^2,uv],[uv,v^2]]
```

is unchanged by simultaneous sign and by every native selected step. It
has rank one when `kappa(x)` is nonzero and rank zero otherwise.

It separates sign classes. If `u` is nonzero and
`(u^2,uv,v^2)=(u'^2,u'v',v'^2)`, then `u'=epsilon u` for
`epsilon in {1,-1}`. The middle equality implies `v'=epsilon v`.
If `u=0`, then `u'=0`; the equality of `v^2` gives the same conclusion,
including the zero case. Thus `M(x)=M(y)` holds exactly when
`Q(x)=Q(y)`.

The image is the thirteen matrices `w w^T`, not the complete set of
symmetric matrices with determinant zero. The identity `M11*M22=M12^2`
alone does not specify this image over `F5`; for example the rank-one
matrix `diag(2,0)` is not `w w^T` because 2 is not a square in `F5`.

## 7. Six projective directions, with two classes on each

The 24 nonzero vectors of `F5^2` divide into six projective lines, each
with four nonzero vectors. On each line, quotienting by simultaneous sign
leaves two classes. Thus the twelve nonzero `Q` values admit the exact
description

```text
six projective directions, two sign classes in each direction.
```

Equivalently, along a line generated by `w`, the matrices in section 6
are `w w^T` and `4 w w^T`; choosing another generator may exchange the
two labels. There is no selected label ordering on a projective line.

This is finite-field geometry of the explicit reader quotient. The six
directions are not identified with the six-dimensional Hodge carrier,
the six Sylow axes of `A5`, or a physical degree of freedom by this count.
Such identifications need separately defined maps and compatibility laws.

## 8. Universal property and the exact scope of the invariant

For any target set `Y`, a total checkpoint reading `F:X->Y` obeys

```text
F(f_0(x))=F(x)=F(f_1(x)) for every x in X
```

if and only if there is a unique function
`Fbar:F5^2/{+1,-1}->Y` such that `F=Fbar o Q`. Equality propagates
along an edge in either direction, so necessity follows from the weak
component classification. Sufficiency follows from section 2, and
uniqueness from surjectivity.

For the actual autonomous state `omega=(n,x)`, the lifted reading
`Qhat(n,x)=Q(x)` satisfies `Qhat(U(omega))=Qhat(omega)` because the
actual control bit is one of the two already covered. Thus there are
thirteen nonempty invariant subsets of the autonomous state space under
this particular total fixed-checkpoint reading.

This does not assert that a native trajectory visits its entire weak
component. The excursions in section 4 explicitly use reversed edges.
Once synchronized, a trajectory remains in one of the finer 313 terminal
components. The thirteen-component graph is also not a classification of
all counter-dependent or orbit-dependent invariants. Calling its classes
physical superselection sectors would require an additional physical
reading and is not a conclusion here.

Finally, the universal property gives at most thirteen distinct values
for every such `F`. A chosen map into a six-dimensional vector space may
have values spanning that space, but cannot be onto an infinite rational
or number-field carrier. Neither the component count nor its six finite
projective directions supplies the amplitudes or the dynamics of a
Hodge reading.
