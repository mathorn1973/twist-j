# Intrinsic bracket pentad, signed A4 transport, and a missing native operation

This is a prospective L1 proof for the named public probe. It makes no Canon
promotion by itself. No execution or passing formal gate is asserted here.
The source authority is Public Canon v101 at public main
`5f54015ed8361e3a64cb10894397020ddfadd104`.

## 1. Inherited premises and the new scope

The following are inherited results, not new claims of this probe:

- `TRACEKERNEL-F5-HODGE-BRACKET`: the displayed residual form and
  metric-volume bracket, its `sl_2(F_5)` identification and volume-scale
  isomorphisms. Application of that branch as a forced Hodge home retains
  the separate `DEF-EXACT-HODGE-HOME-CLOSURE` premise.
- `TRACEKERNEL-F5-AUTOMORPHISM-BOUNDARY`: Killing form `K=2B`,
  `Aut(beta)=SO(B,F_5)=PGL_2(F_5)`, order 120, and the distinct 60-element
  adjoint image of `SL_2(F_5)`.
- `CARRY-PENTAD`, `CARRY-QUADRATIC-SYMMETRY` and
  `J-BINARY-NORM-DESCENT`: the binary form `e_2`, its five nonzero singular
  vectors, its `S_5` isometry group, the integral A4/binary/cyclotomic maps,
  and the explicitly registered `tau_15` isometry.
- `A4-RAMIFIED-HODGE-TRACEKERNEL`: the ramified A4 quotient-to-`W_5`
  isometry, the descended bracket with its frozen minus sign, and marked
  A5 equivariance.
- `FIRED-COMMUTATOR-NOGO`, `COLOR-TORSOR-HOLONOMY`, and
  `NATIVE-LINEAR-HODGE-ORDER5-OBSTRUCTION`: the already delimited fired
  spatial action and the distinct full-checkpoint linear group. The
  fiber-homogeneous image below is a different, explicitly smaller image;
  it does not remove the known order-five elements of the full-checkpoint
  group.

The additions proved below are the intrinsic five-triple object inside the
explicit three-dimensional bracket, its compatible signed full-S5 transport
through a common A4 lattice and binary reduction, and the explicit missing
transposition and its generation properties. This is not the first A4 to
trace-kernel isometry. No historical novelty in finite group theory is claimed.

All following finite-field calculations are exact. They use neither a physical
spatial commutator nor a physical reading of these carriers.

## 2. The explicit bracket and its intrinsic norm class

Let `V=F_5^3` with column vectors, and put

```text
B    = [[2,4,0],[4,2,4],[0,4,2]],
B^-1 = [[2,3,4],[3,1,3],[4,3,2]],
beta(x,y) = B^-1 (x cross y),
B(x,y) = x^T B y,             q(x)=B(x,x).
```

Here `det B=4=-1`. The vector triple-product identity gives

```text
[x,[y,z]] = B(x,y)z - B(x,z)y.                         (G1)
```

For example it follows by substituting the displayed inverse and expanding
the three coordinates; both sides are trilinear, so equality on the 27 triples
of basis vectors is also a complete exact certificate. Summing (G1) cyclically
proves Jacobi. Taking the trace of its operator form gives

```text
ad_x ad_y = B(x,y)I - y(Bx)^T,
K_beta(x,y) = tr(ad_x ad_y) = 2B(x,y),
B = (1/2) K_beta = 3K_beta.                            (G2)
```

Thus B, with its normalization, is reconstructible from the bracket. The
square-type condition below is imposed on `q=B(x,x)`, not on `K_beta(x,x)`:
the factor 2 is a nonsquare in F5 and would interchange the two nonzero norm
classes. This normalization is essential.

Also

```text
ad_x^2 = q(x)I - x(Bx)^T,       ad_x^3 = q(x)ad_x.
```

For nonzero x its characteristic polynomial is `t(t^2-q(x))`: its trace
and determinant are zero and (G2) gives `tr(ad_x^2)=2q(x)`, which fixes the
remaining coefficient in characteristic five. Consequently
`q(x)` is a nonzero square exactly when `ad_x` has three distinct eigenvalues
in F5. This is an alternative intrinsic characterization of the same lines.

Replacing beta by `c beta`, `c in F5^*`, replaces Killing by `c^2 K_beta`
and the reconstructed B by `c^2 B`. It therefore leaves orthogonality and the
square-type projective lines unchanged. The pentad below is insensitive to
that nonzero volume rescaling; no volume orientation is selected by it.

## 3. Exactly five orthogonal triples

A line means a one-dimensional subspace `<x>` with `x!=0`. Define

```text
S = {<x> : q(x) in {1,4}},
P = {unordered triples of distinct pairwise B-orthogonal lines in S}.
```

The condition on S is independent of the nonzero representative. Square type
is a finite-field condition and is not positivity.

**Theorem G3.** S has 15 lines, P has five elements, and every line of S
belongs to exactly one element of P.

**Proof.** The matrix

```text
R = [[3,2,2],[0,0,4],[2,2,2]]
```

satisfies `R^T B R=I` and `det R=2`. In its coordinates the norm is
`a^2+b^2+c^2`. Every square-type line has exactly two unit representatives.
The unit vectors are exactly the six permutations of `(+-1,0,0)` and the
24 vectors obtained by putting `+-2` in one position and `+-1` in each of
the other two. There are therefore 30 unit vectors and 15 lines.

The five triples, in these orthonormal coordinates, are

```text
F0 = {<(1,0,0)>, <(0,1,0)>, <(0,0,1)>},
F_s = {<(2,s2,s3)>, <(1,2s2,s3)>, <(1,s2,2s3)>},
       s=(1,s2,s3),  s2,s3 in {1,-1}.
```

Every vector in F_s has norm `4+1+1=1` and each distinct pair has dot product
`2+2+1=0`. These five triples are disjoint and exhaust the 15 lines. There
are no further orthogonal pairs: a coordinate-axis line is orthogonal only
to the other two axis lines among S. For `(2,1,1)`, an axis line is not
orthogonal; among vectors of unit norm with the doubled coordinate in the
first position there is no orthogonal line, and with it in the second or
third position the unique orthogonal lines are respectively `<(1,2,1)>`
and `<(1,1,2)>`. Signed coordinate permutations give the same assertion for
every non-axis line. Hence every line has precisely its two stated neighbors.
This proves both the count and uniqueness. QED.

In the original difference basis, with the first nonzero coordinate normalized
to one, the complete table is

| Orthonormal label | First line | Second line | Third line |
|---|---|---|---|
| F0 | (1,0,1) | (1,0,4) | (1,2,1) |
| F++ | (0,1,2) | (1,1,2) | (1,2,2) |
| F+- | (0,1,4) | (1,1,4) | (1,2,0) |
| F-+ | (0,1,3) | (1,4,0) | (1,4,4) |
| F-- | (1,1,3) | (1,3,0) | (1,3,3) |

There are `(5^3-1)/(5-1)=31` projective lines. A nonzero zero-norm vector
in orthonormal coordinates has one zero entry and two entries whose squares
are 1 and 4: three choices of zero position, two orders of those squares,
and four sign choices give 24 vectors and six lines. Three nonzero squares
cannot sum to zero in F5. The remaining ten lines therefore have nonsquare
norm. The construction of P uses only B from
(G2); R and these labels are proof coordinates, not additional structure.

## 4. The faithful full automorphism action

Every bracket automorphism preserves Killing and hence B. It permutes P,
giving a homomorphism `Aut(beta) -> Sym(P)`.

**Theorem G4.** This action is faithful and is all of `Sym(P)`.

**Proof.** An element fixing every member of P fixes F0 and so is a signed
permutation matrix in the orthonormal coordinates. Its action on the other
four triples is the action on the four projective directions
`<(1,+-1,+-1)>`: directly, a signed coordinate permutation sends F_s to
the triple indexed by the image direction of s. Those four directions form
a projective frame. Any three are independent and, in that basis, the fourth
has all three coefficients nonzero. A projective linear map fixing all four
is therefore the identity. Our matrix is scalar, and orthogonality restricts
it to `+-I`. The inherited determinant-one condition excludes -I. The kernel
is trivial. Finally the inherited order is 120, equal to `|Sym(P)|=5!`.
Thus

```text
Aut(beta) ~= Sym(P) ~= S5.                              (G4)
```

QED. This is a specific natural five-element carrier for the already known
120-element group, not a new proof that its order is 120.

For example

```text
C0 = [[4,0,4],[0,4,3],[0,0,1]]
```

is `-I-11^T` in orthonormal coordinates. It has determinant one, square I,
and exchanges exactly F0 and F++ in the table. Thus three-dimensional volume
orientation is not parity of the permutation of P: SO(B) includes odd
permutations of the five triples. The inherited 60-element adjoint image of
SL2 is the A5 subgroup; in PGL2 it is characterized by square determinant
of a two-dimensional representative.

## 5. The binary carrier constructed from the pentad

Without labeling P, define

```text
E = {a in F2^P : sum_F a_F=0},
q2(a) = |supp(a)|/2 mod 2.
```

This is a four-dimensional binary vector space. Its polarization is

```text
b2(a,b) = q2(a+b)+q2(a)+q2(b) = sum_F a_F b_F.            (G5)
```

Indeed `|A triangle B|=|A|+|B|-2|A intersect B|` gives the formula directly.
The orthogonal complement of E in the full dot-product space F2^P is the
line of constant vectors. Its nonzero vector has odd weight five, hence is
not in E. Thus b2 is nondegenerate on E.

The nonzero vectors have weight two or four. The ten of weight two have
q2=1; the five of weight four have q2=0. Write the latter as

```text
v_F = 1+e_F,              F in P.
```

Their sum is zero and this is their only linear relation: if coefficients
`c_F` give `sum c_F v_F=0`, the F-coordinate says `c_F=sum_G c_G` for every
F, so all coefficients are equal. Any four form a basis. For F!=G,
`b2(v_F,v_G)=1`, while `q2(v_F)=0`. Therefore in any basis of four such
vectors,

```text
q2(x1 v_1+...+x4 v_4) = sum_(i<j) x_i x_j = e2(x).       (G6)
```

This is an explicit transported presentation of the inherited CARRY-PENTAD
form, not literal equality of originally differently typed carriers.

Every permutation of P acts linearly on E and preserves q2. Conversely an
isometry permutes the five nonzero singular vectors, which span E, so its
action on those vectors determines it. Thus

```text
Aut(beta) ~= Sym(P) ~= O(E,q2).                          (G7)
```

The five-point object and E do not require labels. Four-bit coordinates
require a choice of four v_F as a basis; no original native bit assignment
or physical reading is thereby selected.

## 6. A common integral lattice and one signed action

Let

```text
L=A4={x in Z^5 : sum_(i=0)^4 x_i=0}.
```

For a permutation sigma of the five coordinates use the single integral
action `rho_tilde(sigma)=sgn(sigma) P_sigma`, where the active permutation
convention is `P_sigma e_i=e_(sigma(i))`.

### 6.1 Reduction at five

Reduction maps L onto `H={x in F5^5:sum x_i=0}` with kernel 5L. On H the
coordinate dot product has radical `<1>`: its full-space annihilator is that
line and `1` belongs to H because five is zero. Hence

```text
V5 = H/<1>
```

has a nondegenerate induced metric. The map

```text
T0[x]=(x1-x0,x2-x0,x3-x0,x4-x0)
```

is invariant under adding a constant vector. Its image is
`W={y in F5^4:sum y_i=0}`, its kernel on H is `<1>`, and it is onto: use
the representative `(0,y1,y2,y3,y4)`. For x,z in H, expansion using their
zero sums gives `T0[x] dot T0[z]=x dot z`. It is therefore an isometry.

In the public difference basis

```text
u1=(1,-1,0,0), u2=(0,1,-1,0), u3=(0,0,1,-1),
```

its coordinate version is

```text
T[x]=(x1-x0, x1+x2-2x0, x1+x2+x3-3x0).                 (G8)
```

The Gram of this basis is exactly B. The inverse representative for a
three-coordinate vector `(a,b,c)` is

```text
(0,a,-a+b,-b+c,-c).                                    (G9)
```

For each i let P_i be the three projective classes of vectors in H which
have coordinate i zero and two +1 and two -1 elsewhere, transported by T.
Six vectors give three lines after identifying opposites. Each has norm four;
distinct nonopposite vectors in the same family are orthogonal. All 15 lines
are distinct even in the quotient: if two such vectors represent the same
projective quotient line, `y=a x+c1`, then equality of their four-valued
norms forces `a=+-1`. If c!=0, the unique zero coordinate of y forces
`c=+-1`; one of the two entries of x of the opposite sign would then give
at least two zeros in y. Thus c=0 and their zero coordinates agree. By G3
these are exactly the five intrinsic triples.

The two label conventions are explicitly

| A4 coordinate i | P_i in the orthonormal-label table |
|---|---|
| 0 | F0 |
| 1 | F-- |
| 2 | F-+ |
| 3 | F+- |
| 4 | F++ |

The ordinary coordinate action rho5 on V5 has determinant `sgn(sigma)`.
Indeed the sum quotient of F5^5/H and the line `<1>` both have trivial
action, so determinant multiplicativity leaves the full permutation
determinant on the three-dimensional quotient. The signed action

```text
rho_Lie(sigma)=sgn(sigma) rho5(sigma)                    (G10)
```

therefore has determinant `(sgn sigma)^3 sgn sigma=1` and preserves B.
For any B-isometry M,
`beta(Mx,My)=det(M) M beta(x,y)`, by the cross-product transformation law.
Thus (G10) preserves beta. Its scalar sign does not change projective lines,
so it sends P_i to P_(sigma(i)). Its five-point action is faithful; the 120
signed matrices give all of Aut(beta) by G4.

### 6.2 Reduction at two

Reduction L to F2^5 has image the even-weight subspace. Any even residue
vector can be lifted to an integral zero-sum vector by adjusting one
coordinate by an even integer. The kernel is 2L. Identifying coordinate i
with P_i, this is exactly E.

The half-norm

```text
q_A(x mod 2L) = (sum_i x_i^2)/2 mod 2
```

is integral because `sum x_i=0` implies an even squared norm. Replacing
x by x+2y with y in L changes the half-norm by `2x dot y+2y dot y`, an even
integer. It is well defined. Since an odd square is one modulo four and an
even square is zero,

```text
q_A(x mod 2L)=|supp(x mod 2)|/2 mod 2=q2(x mod 2).        (G11)
```

The integral sign disappears modulo two. Thus the same rho_tilde reduces to
the full Lie automorphism action (G10) on the residual quotient at five and
to ordinary permutation action on (E,q2) at two. This is a compatible diagram
of explicit maps and actions. It is not a bijection of the 125 vectors of
V with the 16 binary vectors of E.

### 6.3 Relation to the inherited Hodge result

The quotient isometry at five and the binary A4 transport already have the
owners named in Section 1. The additional content is the intrinsic pentad
identification and the simultaneous signed full-S5 action on the two
reductions. It does not replace the inherited orientation scalar `-1` in
the ramified Hodge bracket transport.

Nor does it assert that the integral Hodge operator K commutes with all
signed S5 matrices. On the rank-four lattice, an odd signed permutation
still has determinant -1 and reverses orientation. The inherited marked A5
equivariance is not silently promoted to full-S5 commutation with that K.

## 7. The known Phi and the missing transposition

In the difference basis put

```text
A   = [[4,1,0],[0,1,0],[0,1,4]],
Phi = [[0,4,1],[0,4,0],[1,4,0]].
```

Under the A4 labels P_0,...,P_4 they act as

```text
A   <-> (1 2)(3 4),       Phi <-> (1 3)(2 4).            (G12)
```

They fix P_0 and their Klein four group is transitive on the other four
labels. In the orthonormal-label table, Phi fixes F0 and acts as
`(F++ F-+)(F+- F--)`, agreeing with the inherited public involution.

Now interchange coordinates 0 and 1 in (G9), subtract the new zeroth
coordinate, and use (G8). The unsigned matrix is

```text
R01 = [[4,0,0],[2,1,0],[1,0,1]].
```

The permutation is odd, so its signed Lie action is

```text
T = -R01 = [[1,0,0],[3,4,0],[4,0,4]].                   (G13)
```

It satisfies `T^2=I`, `T^T B T=B`, `det T=1` and bracket preservation.
It exchanges P_0 and P_1 and fixes the other three labels. Equivalently it
exchanges F0 and F-- in the orthonormal-label table. It is distinct from
the earlier C0, which exchanges F0 and F++.

For each i=1,...,4 choose k in `<A,Phi>` with k(1)=i. Then
`k T k^-1` acts as the star transposition `(0 i)`. These four transpositions
generate S5, and the action in G4 is faithful. Consequently

```text
<A,Phi,T> = Aut(beta),                 order 120.        (G14)
```

Keeping only Phi gives a different answer. The product Phi T has type
`(0 3 1)(2 4)` and hence order six. Two involutions whose product has order
six generate a dihedral group of order twelve: every word reduces to either
`(Phi T)^j` or `T(Phi T)^j`; the latter coset is distinct since the only
transposition among the powers of Phi T is `(2 4)`, whereas T is `(0 1)`.
Thus

```text
|<Phi,T>|=12,                                         (G15)
```

not 120. The all-five-generator comparison and the fired orientation-corrected
comparison must not be interchanged.

## 8. Exact native scope of the comparison

For clarity, the native carrier is a checkpoint
`(p1,p4,p1p,p4p,q,r)` over F5, with `p` its four piston coordinates,
`s=sum p_i`, and `z=s+q+r`. Decompose uniquely

```text
p=4s 1+w,               sum w_i=0.
```

Use the same difference basis for w. With `t=(2,3,1)^T` and
`h(r)=(3,r,3+r)^T`, substitution of the five declared generators gives

| Generator | New base (s,q,r) | New w |
|---|---|---|
| a | (s,q,r) | A w |
| b | (-s,-q,-r) | -Phi w |
| c | (1-s,1-q,-r) | -Phi w+h(r) |
| d | (-s,1-q,1-r) | -w+t |
| e | (-s,2-q,1-r) | -w+t |

Their homogeneous parts generate exactly

```text
G_tan = {+-I,+-A,+-Phi,+-A Phi} ~= C2^3.                (G16)
```

Indeed A and Phi are commuting independent involutions of determinant one,
and -I is an independent central involution. The generator a supplies A,
the word bd supplies the homogeneous part Phi, and d supplies -I. Every
finite word has homogeneous part in this group. The base evolution and the
selector `z+2 theta_n` depend only on the base, so the same bound applies
to the actual U composition on one fixed starting fiber, where all states
share the selector history.

For these B-isometries bracket preservation is equivalent to determinant
one. Hence the bracket-preserving subgroup is exactly

```text
{I,A,Phi,A Phi} ~= C2^2.                               (G17)
```

All projective actions fix P_0. In particular T is outside the native
homogeneous image, and no word in this class realizes a three-cycle or
five-cycle on P. This does not exclude affine order-five translations.
It does not classify arbitrary nonlinear observations, other encodings,
memory extensions or new contacts. No generator availability, physical
coupling or implementation is supplied by (G13).

The distinct counter-dependent extension question allows base-preserving
symmetries of whole trajectories, including lifted T, by the first-entry
chart developed in [NATIVE_PROOF.md](NATIVE_PROOF.md). Such a relabeling
symmetry is not a word in the five original operations. As a concrete
checkpoint-only obstruction in that extension class, at `z=0,r=0` the
prescribed active T forces the zero piston to `(1,3,0,1)`, whereas a fixes
zero and sends that proposed image to `(3,1,1,0)`. These unequal values
prevent commutation for a counter-independent base-preserving extension
of that prescribed active action. This witness is not a no-go for every
possible symmetry of the machine.

## 9. Prospective exact audit and final boundaries

The accepted `verify.py` is to audit the exact identities and finite carriers
above after the public preregistration pin. Intended coverage includes:

- the 31 projective lines, their norm classes, all five triples and unique
  orthogonal neighbors;
- the 120 automorphisms via signed A4 permutations, and independent
  conjugation/orthonormal-column constructions;
- the faithful five-point actions, the binary carrier, its polarization,
  all five singular vectors and the transported e2 form;
- the residual quotient map, radical invariance, A4 frame labels and the
  signed action composition law;
- A, Phi, T, the native homogeneous group, and the distinct generation
  conclusions 120 and 12.

No attached exploratory transcript is a completed gate of this probe. A
future exact passing audit supports this written proof; it does not replace
the universal arguments or confer a physical interpretation.

The intrinsic object P does not select one of its 24 five-cycles, an
orientation, a generator, J, an exponent, a physical gate, a native bit
assignment, an occurrence law or a reading family. A contact specification
may use the explicit target T only by separately declaring its carrier,
preparation, continuation, admissible operations and induced difference
action. The literal native-word route on these fibers is already excluded
by G16-G17. The physical and higher-layer forcing obligations remain open.
