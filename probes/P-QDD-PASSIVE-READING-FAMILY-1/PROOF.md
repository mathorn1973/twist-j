# Exact passive readings of the existing QDD source

This is an independent proof of the mathematical assertions proposed for
`P-QDD-PASSIVE-READING-FAMILY-1`. The selected reading family is a declared
input. The proof establishes its algebraic properties and total snapshot
maps; it does not select that family.

## 1. Source and comparison space

Keep the existing source definition

```text
K_QDD = {kappa_x = (U^n(0,x))_(n>=0) : x in F_5^6},
```

with equality of complete pointed forward sequences and distinguished head
at n=0. Write that head as `x=(p1,p4,p1p,p4p,q,r)`. The only source factor
used below is the existing balanced piston

```text
ell(0,1,2,3,4) = (0,1,2,-2,-1),
beta_QDD(kappa_x) = (ell(p1),ell(p4),ell(p1p),ell(p4p))^T.
```

Neither q,r nor any later checkpoint is a weight input. The auxiliary
space `V=Q^4` permits a universal algebraic proof of the same formulas.
It is not a replacement or enlargement of the decoder domain K_QDD.
The decoder maps remain the composites with beta_QDD defined in section 4.

Fix `G=I_4-uu^T/5`, `u=(1,1,1,1)^T`, and
`chi=(1,-1,-1,1)^T`. For a rational matrix A its G-adjoint is
`A^sharp=G^-1 A^T G`. A source effect P and its quadratic coefficient
matrix GP are distinct objects. The source weight is `v^T G P v`.

## 2. Three projectors and their complete chosen Boolean algebra

Define

```text
P_t = uu^T/4,
P_l = chi chi^T/4,
P_r = I_4-P_t-P_l,
A = {t,l,r},   t<l<r,
P_S = sum_(a in S) P_a,   S subset A.
```

The vectors u and chi are orthogonal, and each has Euclidean squared
length 4. The vectors `a=(1,0,0,-1)^T` and `b=(0,1,-1,0)^T` are orthogonal
to both and to each other, with squared length 2. They form a rational
basis of the remaining two-dimensional subspace. Thus

```text
P_r = aa^T/2 + bb^T/2.
```

The three matrices are rational symmetric projectors, have pairwise zero
products, and have ranks 1,1,2. Their sum is I_4. The matrix G acts as
1/5 on Qu and as the identity on its Euclidean orthogonal complement.
It therefore commutes with all three projectors, making them G-self-adjoint.

Orthogonality gives, for all S,T subset A,

```text
P_S P_T = P_(S intersection T),
I_4-P_S = P_(A minus S).
```

The eight subset sums are distinct. If S and T differ at atom a, choose
a nonzero vector in ran(P_a); the two sums act on that vector respectively
as identity and zero. Consequently the subset map is an isomorphism from
the eight-element Boolean algebra of subsets of A to the generated
projector algebra.

A projector-valued partition in this algebra is a family of nonzero
pairwise orthogonal members summing to I. Injectivity of the subset map
makes it exactly a partition of the three atoms into nonempty blocks.
There is one one-block partition, three two-block partitions, and one
three-block partition. Fix their IDs and literal block order as

```text
PI-ALL    ((t,l,r))
PI-TRACE  ((t),(l,r))
PI-LEG    ((t,r),(l))
PI-PAIR   ((t,l),(r))
PI-ATOMS  ((t),(l),(r)).
```

This proves completeness in the declared three-atom algebra. It does not
assert completeness among all possible rational projectors or source readings.
Different IDs remain different readings even when their numerical weights
happen to coincide at a particular source.

## 3. Exact weights and the zero branch

For v in Q^4 put `Q=v^T v`, `s=u^T v`, and `ell=chi^T v`. Directly from
the orthogonal decomposition above,

```text
m_t(v) = v^T G P_t v = s^2/20,
m_l(v) = v^T G P_l v = ell^2/4,
m_r(v) = v^T G P_r v
       = ((v1-v4)^2+(v2-v3)^2)/2
       = (4Q-s^2-ell^2)/4.
```

These are nonnegative rationals. Their sum is
`m(v)=v^T G v=Q-s^2/5`. Since `s^2<=4Q`, one has `m(v)>=Q/5`, so m(v)>0
exactly when v!=0. For a displayed block B set `w_B(v)=sum_(a in B)m_a(v)`.
The blocks partition A, so their weights sum to m(v).

Thus every nonzero v has well-defined normalized block data w_B(v)/m(v).
Individual zero-weight blocks stay zero and do not require separate division.
For v=0 all raw weights are zero and no normalization is performed.

For PI-TRACE the total and ordered block weights are precisely
`m(v)`, `s^2/20`, and `m(v)-s^2/20`. These agree with the existing
algebraic QDD total and ordered LOW/HIGH weight slots on the same balanced
input v. This is an equality of the identified weight slots, not an equality
between different record schemas or a replacement of the existing binding.

## 4. Typed records and total maps on K_QDD

A passive record has exactly five fields, with literal equality of all
IDs, tags, tuple lengths and rational entries:

```text
partition_id,
support_state,
total_weight,
block_weights,
normalized_weight_state.
```

For each fixed displayed sigma, let `Record_sigma` be the domain of
**coherent records bearing partition_id=sigma**:

- A zero record has support_state ZERO_SUPPORT, total_weight 0, the ordered
  zero tuple of length equal to the number of sigma blocks, and
  normalized_weight_state ZERO_DENOMINATOR.
- A supported record has support_state SUPPORTED, rational total_weight m>0,
  an ordered tuple of nonnegative rationals w with sum m and the displayed
  sigma block length, and normalized_weight_state NORMALIZED(w/m).

This explicitly delimits the domain used for record coarsening below.
An arbitrary collection of five independently type-correct but inconsistent
fields is not asserted to lie in Record_sigma.

Define the auxiliary mathematical map `r_sigma:Q^4 -> Record_sigma` by
the formulas in section 3 and these two branches. Define the adopted-source
map only as

```text
R_sigma = r_sigma o beta_QDD : K_QDD -> Record_sigma.
```

The existing beta is total; r_sigma is total by the positivity and explicit
zero rule. Therefore R_sigma is total on K_QDD. Source equality is respected
because equal pointed sequences have the same distinguished head. In fact,
the map factors through beta, so equal balanced vectors give equal records
for the same sigma regardless of the q,r head coordinates.

The head x determines kappa_x; different heads cannot denote the same
pointed sequence because the distinguished head is part of its equality.
The 5^6=15625 native heads therefore give a complete finite parameterization
of this source. The balanced digit map is a bijection from F_5 to
{-2,-1,0,1,2}. Its first-four-coordinate image has 625 vectors, each with
25 choices of the unused q,r coordinates. This justifies the finite audit
inventory without using any later U step or adding an onset parameter.

## 5. Coarsening and compositional equality

Write `sigma <= pi` when every sigma block is contained in a pi block.
For this relation define a typed map

```text
C_(sigma,pi) : Record_sigma -> Record_pi.
```

It replaces the partition ID by pi, retains support and total weight, and
for each displayed pi block B sums precisely the entries of sigma blocks
contained in B. On a supported record it performs the same sums on the
normalized tuple; on a zero record it retains ZERO_DENOMINATOR.

Since the fine blocks form a disjoint partition of each coarse block,
raw sums remain nonnegative and retain total m. Normalized sums are their
raw counterparts divided by the same m. Thus C is well-defined on the
stated coherent-record domain and its output lies in Record_pi.

For every v in Q^4, the block identity

```text
sum_(C in sigma; C subset B) sum_(a in C) m_a(v)
  = sum_(a in B) m_a(v)
```

proves equality of the raw entries in
`C_(sigma,pi) r_sigma(v)=r_pi(v)`. The ID, support and total fields agree
by construction; the normalized fields agree by division by the same
positive total, or by the common zero tag. Composing with beta gives

```text
C_(sigma,pi) R_sigma = R_pi.
```

If `sigma <= pi <= tau`, each sigma block belongs to exactly one pi block
and exactly one tau block. Summing via the intermediate pi groups or
directly into tau gives the same entries by associativity of finite
addition. The unchanged fields and zero rules agree as above. Therefore,
on the complete coherent domain Record_sigma,

```text
C_(pi,tau) o C_(sigma,pi) = C_(sigma,tau).
```

These are exact one-snapshot record identities. No history, source update,
individual event, sampling law or physical measure is part of either side.

## 6. Scope of the evidence

Sections 1-5 are a universal proof from the stated definitions, including
the Q^4 mathematical extension and the maps on the unchanged K_QDD source.
Finite verifier checks audit arithmetic, literal field ordering, source
factorization and record maps. They do not substitute enumeration for a
proof on all rational vectors. Adoption of the five reading IDs is a
separate owner choice; this proof supplies their mathematical properties.
