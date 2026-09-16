# Binary records and quadratic selection: exact boundary

Proof-first, result-exposed mathematical target. Public lock: [#885](https://github.com/mathorn1973/twist-j/issues/885).
Scope: L1 finite combinatorics, integer source readings and symbolic reversible
maps. These proofs do not construct a physical instrument or an L5 event law.

## 1. The admissible class

For each finite set X and fixed integer k>=1 consider the ordered tuples X^k.
The only structure on X is equality. A relation support is a subset of X^k;
simultaneous relabeling acts on every coordinate by the same bijection of X.
For weighted counting, every tuple has a nonnegative integer atomic weight
v_X(t), and the valuation of a subset is the sum of its atomic weights.
Require stability under every injection f:X->Y:

```text
v_Y(f(t_1),...,f(t_k)) = v_X(t_1,...,t_k).
```

This is an explicit hypothesis about local weights, not a derived law of a
physical apparatus. It implies relabeling covariance and excludes hidden
dependence of an atom's weight on the number of unused labels. Without it,
the weights below can depend on |X| and the polynomial conclusion is absent.
The support-only version uses weights in {0,1}.

The equality partition pi(t) partitions {1,...,k} by i~j iff t_i=t_j.
Write b(pi) for its number of blocks and (d)_r=d(d-1)...(d-r+1), with
(d)_0=1 and (d)_r=0 when 0<=d<r. Ordered argument positions remain distinct.

## 2. Complete equality-pattern classification

**Theorem 1.** For any d=|X|, simultaneous S_d orbits on X^k are exactly
the equality partitions with at most d blocks. The orbit of a partition with
r blocks has (d)_r tuples. Every invariant support is a union of these orbits.

**Proof.** A bijection preserves all equality and inequality comparisons.
Conversely, if two tuples have the same partition, sending the r distinct
labels of the first tuple to the corresponding r labels of the second is a
bijection between two r-element subsets. Extend it arbitrarily to a bijection
of the finite ambient sets of equal size. Thus the tuples lie in one orbit.
Order the blocks by their least positions; choosing distinct labels for those
blocks is an ordered injection from r positions into X, with (d)_r choices.
Invariance makes membership constant on every orbit. This also covers d=0:
for k>=1 there are no tuples and the unique support is empty. QED.

**Theorem 2.** Injection-stable atomic valuations in section 1 are in exact
bijection with assignments c_pi in N_0 to all partitions of {1,...,k}. Their
full-carrier counts are

```text
W_k(d) = sum_pi c_pi (d)_(b(pi)).
```

**Proof.** Realize pi first on a set of b(pi) elements. Theorem 1 makes its
weight independent of the chosen labels there. Every other tuple with pi is
an injective image of such a minimal representative, so has that same weight
c_pi. Conversely, assigning a coefficient by equality partition respects all
injections and defines an additive subset valuation. Summing the orbit sizes
proves the formula. QED.

For any nonzero valuation its polynomial degree is exactly the largest
b(pi) with c_pi>0: the corresponding leading coefficients are positive, so
cannot cancel. Full Cartesian counting has every c_pi=1 and gives d^k.
This yields the identity d^k=sum_pi (d)_(b(pi)) by partitioning tuples,
without assuming a power law.

At k=3 there are five partitions: one with one block, three with two blocks,
and one with three blocks. Thus

```text
W_3(d)=c_1 d+(c_12+c_13+c_23)d(d-1)+c_123 d(d-1)(d-2).
```

For supports defined respectively by all entries equal, first two entries
equal, and no constraints, the counts are d, d^2 and d^3. They all use triples.
This is a complete census for equality-only relations, not for relations
carrying native TWIST-J algebra, orientation, a metric or a group action.

## 3. Binary specialization and the extra condition for a square

At k=2 there are two orbits, the diagonal and its complement. Theorem 2 gives

```text
v(x,y)=a if x=y, and b if x!=y, with a,b in N_0,
W_2(d)=a d+b d(d-1).
```

The four injection-stable supports are empty, diagonal, off-diagonal and full,
with counts 0, d, d(d-1), d^2 (some coincide at d=0 or 1).

**Theorem 3.** W_2(d)=c d^2 for every d>=0 iff a=b=c. For a prescribed unit
diagonal a=1, the square therefore requires b=1 as an additional condition.

**Proof.** At d=1 the claimed equality gives a=c. At d=2 it gives
2a+2b=4c, hence b=c. Substitution proves sufficiency for every d. QED.

Positivity, additivity over disjoint subsets of edges, simultaneous label
covariance and injection stability allow every a,b>=0. Even strict positive
atomic weights do not force a=b: a=1,b=2 gives W=d(2d-1).

For two *unmarked* carriers S,T, the product action Sym(S) x Sym(T) is
transitive on S x T whenever both sets are nonempty. Therefore a relation
invariant under that action is either empty or complete. An invariant atomic
weight is constant at fixed carrier sizes. Stability under separate injections
makes that constant size-independent; unit normalization yields |S||T|.
This is a sufficient route to complete incidence.

It cannot silently replace the symmetry of a record correspondence. If a
bijection f:S->T is part of the data, its automorphisms obey tau f=f sigma;
the graph of f and its complement remain two orbits. Relabeling both carriers
independently while also transporting f to tau f sigma^-1 preserves a faithful
graph and does not force a=b. Demanding the larger product action while keeping
f fixed instead discards the matching as a structure. The two symmetry
requirements concern different objects.

## 4. A reversible, covariant, faithful symbolic writer

For every nonempty finite symbol set S, let B={blank} disjoint-union S be the
record-cell carrier. Source and record symbols share a declared matching.
For s in S let tau_s be the transposition of blank and s on B, fixing every
other symbol. Define

```text
T(s,r)=(s,tau_s(r)).
```

**Theorem 4.** T is a total involutive bijection on S x B. It preserves the
source, maps (s,blank) to (s,s), and is covariant under every relabeling sigma
of S extended to fix blank. Its active source-to-record graph has |S| edges.
It extends to any finite collection of record cells by acting on one chosen
cell and fixing all others; consecutive writes to fresh cells preserve every
older record and the complete sequence is invertible.

**Proof.** tau_s^2=id, so T^2=id. Also sigma tau_s sigma^-1=tau_(sigma(s)),
which gives the covariance square on every (s,r). The blank input produces
exactly the graph {(s,s):s in S}. A map acting on one coordinate fixes all
others and remains an involution; the inverse of a finite sequence is the
reversed sequence of those involutions. QED.

Fresh blank cells and their addresses are declared resources; this theorem
derives neither reset nor an infinite memory supply. It copies finite classical
symbols, not arbitrary unknown quantum states. The cardinality |S| counts
possible matched source-record pairs across inputs; each invocation makes one
symbolic write. Neither cardinality is an occurrence probability.

For d=2 the active graph has 2 edges while full Cartesian incidence on its two
active carriers has 4. Hence binary representation, source retention,
reversibility, covariance and preservation of older records do not force the
full Cartesian count. The active graph is the a=1,b=0 case of section 3.
Whether this symbolic mechanism belongs to a physical apparatus class is a
separate question; it is enough to refute the unrestricted mathematical
implication from these structural properties alone.

## 5. Distinct readings on the chosen v80 integer channels

This comparison conditions on v80's already adopted integer source
z=(z_0,z_1,z_2,z_3) and its channel forms. It does not derive that channel
selection from U or from a target-independent physical apparatus.

For every integer p>=1 define

```text
s=sum_i z_i,
A_p=|s|^p,
B_p=5 sum_(i<j) |z_i-z_j|^p,
D_p=A_p+B_p,
r_p(z)=(A_p/D_p,B_p/D_p) when D_p>0,
r_p(0)=ZERO_SUPPORT (no normalized ratio).
```

**Theorem 5.** Every member has nonnegative integer branch weights, total zero
iff z=0, LOW zero iff s=0, HIGH zero iff all coordinates are equal, and a
normalized rational pair off zero. It is invariant under source-coordinate
permutations and global sign reversal. Its weights are homogeneous of degree
p under integer scaling, and its normalized pair is invariant under nonzero
integer scaling. The readings for different positive integers p are distinct.

**Proof.** Each term is a nonnegative integer. B_p=0 iff all six differences
vanish, hence z=(t,t,t,t); A_p=0 then implies 4t=0 and t=0. The branch-zero
statements, invariances and homogeneity follow directly from the absolute
values and the complete unordered difference set. At z=(1,1,0,0), there are
four unit differences, so

```text
A_p=2^p, B_p=20, r_p,LOW=2^p/(2^p+20).
```

This is strictly increasing in p: for 0<u<v, u/(u+20)<v/(v+20) by multiplying
the positive denominators. Thus all p give different readings. In particular,
p=1 gives 1/11 and p=2 gives 1/6. QED.

At p=2 these are exactly v80's A=s^2 and B=5(4 sum z_i^2-s^2). At p=1 they
count the reduced units once; at p=2 they count complete ordered fibre pairs.
For general p they count ordered p-tuples in each residual fibre. The power
family is fixed as a class before physical comparison. No member is asserted
to satisfy complete rational-frame additivity, the full QDD record contract,
the same density-state output or the same physical effect as another member.
The theorem establishes nonselection under the *listed* source/weight laws.

The writer in section 4 can record any selected finite symbol, whether it
labels a unit or a tuple; reversibility of that final recording step does not
choose the prior symbol inventory. No onset, sampling or event law follows.

## 6. Signed biadditivity obstruction

**Theorem 6.** If B:G x H -> R_(>=0) is additive in each argument and G,H are
abelian groups, then B=0.

**Proof.** Additivity gives B(0,h)=2B(0,h), so B(0,h)=0. Then
0=B(g+(-g),h)=B(g,h)+B(-g,h). Both terms are nonnegative and must vanish.
Only additivity in the first group argument was needed. QED.

Thus unsigned nonzero pair counting on a positive monoid cannot also be a
nonnegative bilinear law on its whole signed group completion. A signed
bilinear form may be nonzero by taking negative values off the diagonal; a
positive quadratic diagonal B(g,g) does not contradict this theorem.
Residual reduction followed by squaring is also not separately additive in
raw signed arrivals. For (+1,-1), raw unsigned pair count is 4 and reduced
residual count is 0. Cancellation/composition must be specified independently.

## 7. Scientific disposition at the frozen scope

The claims "binary arity forces a square" and "reversible faithful covariant
record writing forces full Cartesian incidence" are refuted by the exact
examples above. At the explicitly classified binary weight scope, quadratic
selection is exactly the additional equality a=b. A sufficient unmarked-set
symmetry route is identified, together with why it is stronger than symmetry
of a matched record. The equality-pattern census answers the arity question
for a complete elementary class and the native-channel family shows that the
ambiguity survives the listed scalar reading constraints.

These are mathematical nonselection results. Born's empirical rule, the v80
simplex pair theorem and all physical QDD obligations retain their scopes.
A physical argument may still justify the missing premises in an independently
specified apparatus class. It must also supply its occurrence/statistical law.
