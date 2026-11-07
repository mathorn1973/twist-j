# Native piston Gram descent: analytical proof

NON-CANONICAL / L1. Written before execution. Finite classification values
are deliberately absent here and will be reported by the frozen verifier.

## 1. The complete factor criterion

For a set S, map T:S->S and reader R:S->Y, a map F on im(R) with
R T=F R exists iff R(x)=R(y) implies R(Tx)=R(Ty). Necessity follows by
substitution. For sufficiency define F(Rx)=R(Tx); the implication makes it
well-defined. No linearity, invertibility or probability is used.

For the current reader (n,R(x)), equality includes n. Both native bits
occur, at n=0 and n=1. Since the full domain is N0 x F5^6 and R is
independent of n, all-n native descent is equivalent to the same criterion
for T0 and T1. This equivalence does not replace the native clock by an
arbitrary binary clock.

## 2. A native obstruction with nonzero oriented determinant

The two input pistons in PREREG are negatives, with balanced matrices
diag(1,-1) and diag(-1,1). Both Grams are I and both determinants are -1.
Their q,r are 0,4 and their piston sum is zero, so the actual origin
selector is four for both. The next matrices under e are

```
((1,1),(-2,0)) and ((-2,1),(-2,-2)).
```

Their Grams are respectively `((2,-2),(-2,4))` and `((5,2),(2,8))`,
and their determinants are 2 and 6. Both successor receiver pairs are
(2,2). Thus neither raw reader descends, even after the signed determinant
is retained. This does not rely on the zero or rank-one input locus.

## 3. Complete refinement and extra labels

Let P0 be the equality partition of one fixed reader. Define P_(k+1) by
requiring equality at P_k and equality of the T0 and T1 successors at P_k.
Equivalently, P_k identifies exactly those states whose initial-reader
outputs agree after every binary control word of length at most k.
The equivalence follows by induction, adjoining the first letter of a word.

Every strict refinement raises the number of classes. On finite S the
sequence therefore stabilizes. At stability P* is a congruence for both
maps. Any other congruence refining P0 refines every P_k by induction, and
hence refines P*. This proves coarseness and completeness without relying
on a guessed stopping depth or singleton conclusion.

Now consider any counter-independent completion (R,tag). Its equality
partition must refine P*. Within an original fibre B it therefore needs
at least m(B) different tag values, where m(B) counts the P* classes in B.
A fixed alphabet needs at least max_B m(B) values. Conversely number the
P* blocks within each B by their increasing least state index. This tag
has exactly the claimed bound and the pair (R,tag) identifies precisely P*.
The factor criterion supplies both transition maps. The verifier explicitly
constructs them and checks their equality on every checkpoint.

This is a sharp cardinality for the declared present-state reading class.
It is not a storage or thermodynamic theorem about an initialized device.
The completion can be noninjective if P* is not discrete, and the native
map need not be reversible. Neither an arbitrary n-dependent partition nor
a smaller prepared state domain belongs to this minimality statement.

## 4. The stable native centre and exact cone factor

The piston parts of d and e are p->c-p, c=(2,1,3,4). Since 2 is
invertible in F5 their unique fixed piston is p*=c/2=(1,3,4,2).
The piston part of b fixes this same p*. Subtract p* in the field before
taking the balanced lift. Oddness of ell and its compatibility with
coordinate permutations give, exactly over the integers,

```
b: W -> -sigma_x W,
d,e: W -> -W.
```

The native trace transforms as z->-z for b, z->2-z for d and z->3-z for e.
On z=1 or 4 the actual selector gives precisely the four rows of PREREG's
table. Thus these sheets are invariant under both T0 and T1. The centered
Gram and determinant obey the stated rules; the determinant changes sign
under b because det(-sigma_x)=-1, not +1.

For any real integer 2x2 W, write its row Gram as (A,B;B,C) and its
determinant as D. Expanding products gives AC-B^2=D^2. Consequently

```
(A+C)^2-(A-C)^2-(2B)^2-(2D)^2=0.
```

Under b the first and third coordinates of this quadruple are unchanged,
while its second and fourth change sign. Under d/e all four are unchanged.
The matrix Lambda=diag(1,-1,1,-1) preserves diag(1,-1,-1,-1), has
determinant one and fixes the first coordinate. It is a spatial half-turn,
not a boost. The exact map (n,x)->(n,z,Q) therefore intertwines the actual
native U on S14 with the explicitly displayed map on its realizable image.
It is not asserted to be onto the full integer null cone.

Multiplying Q1,Q3 by chi(z), where chi(1)=1 and chi(4)=-1, cancels that
half-turn because b also interchanges the two sheets. The resulting
Q_flat is constant under both controls. This expressly limits the physical
interpretation: the constructed motion is removed by its supplied sheet
frame and gives no propagation or Lorentz boost.

The existing native invariant V also contains this result. Its coordinates
are `(p1+p1p,p4+p4p,chi(z)(p1-p1p-2),chi(z)(p4-p4p-1))` over F5.
Let Vmat have these two rows, eta=(1-chi(z))/2 and S=sigma_x. The centered
residual matrix satisfies

```
S^eta W_res = 3 ((1,1),(1,-1)) Vmat   over F5.
```

Take ell only after this field operation. The public evolution V->-V
then makes the corresponding quadratic Q_flat invariant. Thus the cone
reading is an explicit specialization of U-NATIVE-INVARIANT-AND-NOWRITE,
not a claim that this probe first found stable native invariant geometry.

## 5. Origin entrance

At counter zero the trace maps under the actual bits 0,1,1 are:

```
z0=0 or 2:  z1=0, z2=2, z3=1;
z0=1,3,4:   z1=4, z2=1, z3=1.
```

All initial checkpoints therefore enter S14 by counter three. This is an
inherited control; it does not extend the centered closed formula backwards
through the transient on the other three trace sheets.

## 6. Scope of the bridge

The raw full-domain obstruction, minimal refinement and centered stable
factor have different explicitly declared readers or domains. None is a
repair of another under an unchanged name. The common determinant identity
does not identify the cyclotomic, Hodge or physical carriers. The four cone
coordinates are quadratic readouts, and Q0 is an invariant sum of squares,
not the native counter. No physical photon, mass, time, apparatus or Born
occurrence is inferred from a null equation.
