# The affine kernel group and its order-three obstruction

**PUBLIC-source, NON-CANONICAL L1 candidate-T proof.** This is a proposed
analytical result for the five registered maps. It is not an accepted public
T promotion, a completed formal run, or a physical realization. The finite
census surfaces and their equivalence conventions are specified separately
in [SURFACES.md](SURFACES.md); this proof does not enlarge those surfaces.

## 1. Public dependencies and conventions

The source is [Public Canon v98](../../canon/CANON.md), with exact claim
identities in [REGISTRY.tsv](../../canon/REGISTRY.tsv):

- `KERNEL-WEDGE-AFFINITY` [T] supplies the five affine maps and their
  determinant-one linear parts, reproduced in the public
  [kernel-connectivity verifier](../../reproduce/kernel-connectivity/verify.py).
- `NATIVE-LINEAR-HODGE-ORDER5-OBSTRUCTION` [T] supplies the complete linear
  group order 200; its [proof](../P-NATIVE-LINEAR-ORDER5-HODGE-CLASS-1/PROOF.md)
  and [verifier](../P-NATIVE-LINEAR-ORDER5-HODGE-CLASS-1/verify.py) are public.
- `KERNEL-WEDGE-COUPLING` [T] supplies the two-way CSUM comparison and its
  SL2(F_5) group. It does not make CSUM a word in the five single-cell maps.

No unpublished original census is a premise of the following derivation.
`KERNEL-CELL-COMPONENTS` remains at its registered C scope; no census row is
silently promoted by citing it here.

Work over V=F_5^6 with x=(p_1,p_4,p'_1,p'_4,q,r). The symbol r is the
sixth coordinate called `t` in the source verifier. Products mean
gh=g composed with h, so the rightmost map acts first. Define
T_v(x)=x+v and [g,h]=ghg^-1h^-1. Every displayed coordinate is modulo five.
The five source maps are

```text
a(x) = (p_4,p_1,p'_4,p'_1,q,r),
b(x) = (-p'_1,-p'_4,-p_1,-p_4,-q,-r),
c(x) = (-p'_1+2,-p'_4+1+r,-p_1+2,-p_4+1-r,1-q,-r),
d(x) = C-x,                         C=(2,1,3,4,1,1),
e(x) = C+e_q-x,                     e_q=(0,0,0,0,1,0).
```

Direct substitution gives g^2=id for all five maps. Set
G=<a,b,c,d,e> and let pi:G->GL(V) take the linear part M_g.
For an affine map g=(M_g,v_g),

```text
(M,v)(N,w)=(MN,Mw+v),
g T_v g^-1=T_(M_g v).
```

These identities fix every composition and commutator sign below.

## 2. Six independent translations inside G

First, e and d have the same linear part, hence

```text
ed=T_(e_q),
[b,d]=T_((M_b-I)C)=T_(3e_q+3e_r),
[b,d]^2(ed)^-1=T_(e_r),              e_r=(0,0,0,0,0,1).
```

The last equality uses 2(3e_q+3e_r)-e_q=e_r in F_5^6.
Put

```text
u=(0,1,0,-1,0,0),
s=(2,1,2,1,1,0).
```

Since M_c e_r=u-e_r, conjugation gives

```text
c T_(e_r) c^-1 T_(e_r)=T_u,
a T_u a^-1=T_(M_a u),               M_a u=(1,0,-1,0,0,0).
```

For h=cb, direct substitution into the source maps gives
h(x)=x-r u+s. Thus M_h=I-u e_r^*, where e_r^* selects the sixth
coordinate, and e_r^*C=1. Since d(x)=C-x, affine multiplication gives

```text
[d,h]=T_((I-M_h)C-2s)=T_(u-2s),
T_(2s)=T_u[d,h]^-1,
T_s=(T_(2s))^3.
```

The final identity uses 3 times 2=1 in F_5. Consequently G also contains

```text
T_(s_0)=T_s T_(e_q)^-1,             s_0=(2,1,2,1,0,0),
a T_(s_0) a^-1=T_(M_a s_0),         M_a s_0=(1,2,1,2,0,0).
```

The first four coordinates split as the direct sum of the two-dimensional
spaces p'=-p and p'=p, because two is invertible in F_5. The vectors
u,M_a u form a basis of the first space. In the second space s_0,M_a s_0
have coordinate columns (2,1) and (1,2), with determinant 3!=0. Adding
e_q,e_r therefore gives six independent vectors of V.

Translation composition is vector addition and powers give scalar
multiples. Hence every T_v, v in V, belongs to G. Since an affine map with
identity linear part is a translation, the kernel of pi is exactly the
full translation group V. Its dimension is six, not merely bounded below
by the translations used in one word.

## 3. Exact group order, splitting and point stabilizers

Let H=pi(G). The registered linear-group result gives |H|=200. The same
order has a short structural derivation from the displayed maps. Write
A=M_a, J=-I and S=-M_b. The matrices A and S independently swap the two
entries within each piston and the two piston blocks, while fixing q,r.
They commute with J and generate D=<A,S,J> isomorphic to C_2^3.

Let W=span(u,Au). Then

```text
N={I+w e_r^*: w in W} is isomorphic to (F_5)^2,
M_c M_b=I-u e_r^*.
```

The generators A,S,J normalize N: they act on w as, respectively,
w->Aw, w->-w and w->w under conjugation of the shear. Conjugating
I-u e_r^* by A and taking powers generates N. Moreover N intersects D
only in I: every shear fixes the first five coordinate basis vectors,
and comparison on those vectors and e_r forces all three D exponents
to vanish. All five original linear parts lie in ND, so
H=N semidirect D and |H|=25 times 8=200.

For every g=(M,v) in G, the translation T_(-v) is now known to lie in G.
Therefore (M,0)=T_(-v)g also belongs to G. This supplies an actual linear
complement, and proves

```text
G=V semidirect H,
|G|=5^6 times 200=3,125,000=2^3 times 5^8.
```

Translations act transitively on V. The stabilizer of zero is the displayed
linear copy of H, and the stabilizer of every point has order 200. These
conclusions use the affine words above and do not depend on executing a
new state-space or group census.

## 4. The common covector and the word-parity character

For ell=(1,-1,1,-1,0,0), the source linear parts satisfy

```text
ell M_a=ell M_b=ell M_c=ell M_d=ell M_e=-ell.
```

For c this follows from ell M_b=-ell and ell u=0. Consequently the dual
line spanned by ell is invariant, and there is a unique sign epsilon(g)
with ell M_g=epsilon(g)ell for every g in G. Multiplication of linear
parts proves epsilon(gh)=epsilon(g)epsilon(h). Every generator has sign
-1, so epsilon is surjective and equals word-length parity; in particular,
the parity is independent of the chosen word representing an element.

This is a character of the linear action carried by an affine group. It
is not the determinant character: all five determinants are one. It is
also not the identity ell(gx)=epsilon(g)ell(x) for the full affine action.
Indeed ell s=2, so ell(cx)=-ell(x)+2. No physical spatial orientation,
metric or geometric mirror is selected by calling this a sign character.

## 5. No factor three in single-cell words or independent copies

The exact group order has only the prime factors two and five. By
Lagrange's theorem, every subgroup has this property. A section means a
quotient K/L with L normal in a subgroup K of G; its order divides |G|
and likewise has no factor three. Thus G has no element of order three
and cannot have A_5 (order 60) or 2I (order 120) as a subgroup, quotient
or section. This is an obstruction for the whole group of arbitrary
finite single-cell words, not merely the five letters individually.

For any fixed finite number m of independently controlled, labelled
cells, the available local-word group is G^m, of order
2^(3m) times 5^(8m). The same subgroup, quotient and section argument
applies. The group generated by any restricted collection of local words
is a subgroup and inherits the obstruction. Additional cell permutations or intercell
couplings are not elements of this stipulated direct-product control
model merely because several cells are present.

For the fixed surfaces in [SURFACES.md](SURFACES.md), this also constrains
their type-preserving chamber automorphism group H, a subgroup of G.
It makes no claim about all homeomorphisms or type-permuting symmetries of
the surfaces, unrelated mirror systems or other carriers.

## 6. The separate CSUM comparison has an explicit order-three word

On a column of two cell states the public two-way CSUM matrices are

```text
P=[[1,1],[0,1]],       Q=[[1,0],[1,1]].
```

Under the same rightmost-first convention, set

```text
R=P Q^-1=[[0,1],[-1,1]],
R^2=[[-1,1],[-1,0]],
R^3=-I.
```

Since R^2!=I and (R^2)^3=I, the word R^2 has exact order three.
The block action on V times V is faithful, so the same order holds for
the cell-pair transformation. This explicit word agrees with the
registered comparison group SL2(F_5), of order 120.

The comparison adds declared CSUM operations and therefore changes the
available group. It is not a counterexample to the single-cell or
independent-copy obstruction. It supplies no derivation of those coupling
operations from U/J, no apparatus or physical controllability guarantee,
and no lift beyond L1. Formal execution, audit and any public status
decision remain separate obligations of this probe.
