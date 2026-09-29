# Intrinsic ramified addresses and a conditional transport obstruction

**Prospective proof for P-RAMIFIED-TREE-COUNTER-LOCALITY-1. Candidate-T,
L1; NON-CANONICAL until a separate reviewed Canon fold.**

Author: A. M. Thorn <thorn@twistj.com>.

This is a proof-first result. The formulas and their intended conclusion
were exposed before preregistration; no blind discovery is claimed. The
proof is universal in the stated depths and carriers. A bounded exact audit
can check its algebra and witnesses, but cannot replace these arguments.

## 1. Sources, notation and proposed claims

The source authority is Public Canon v94, whose content commit is
`42e87e7c36b8b8adb6cb7375db55bebb53fb403e`, active on public `main` at
`af8dc5956e26917b265fd0070f500c841c326512`. The algebraic definitions and
registered premises are in `canon/CANON.md` and `canon/REGISTRY.tsv`:

- `J-STEP [T]`, multiplication by `J` on the integral cyclotomic lattice;
- `C20-TEICHMULLER-SPLIT [T]`, with its proof in
  `probes/P-C20-TEICHMULLER-SPLIT-2/PREREG.md`, for the ramified quotients,
  their cardinalities and the ideal equality `(5)=(1-j)^4`;
- the native architecture in `canon/CORE.md`, used only to delimit what the
  new arithmetic construction does and does not identify with native `U`;
- `U-COUNTER-REACHABLE-AMPLITUDE-CLASS [T]`, proved in
  `probes/P-U-COUNTER-AMPLITUDE-CLASS-1/PROOF.md`, used only in the final
  scope discussion, not as a premise of the tree or transport proofs.

The earlier proof-only note in PR #1295,
`notes/C-J-LOCAL-RAMIFIED-MEMORY-N/PROOF.md`, exposed a different latency
obstruction in a chosen balanced coefficient code. It is not a theorem
premise here. No finite-expansion assertion about literal ramified digits
is used.

Set

```text
O = Z[j],  j^4+j^3+j^2+j+1 = 0,
J = 1+j^2,
beta = 1-j,
P = beta O,
v_P(0) = infinity.
```

The proposed claim units are:

1. **RAMIFIED-COSET-TREE**: the intrinsic five-branching rooted coset tree,
   its graph metric, and the distinct normalized boundary ultrametric.
2. **RAMIFIED-COUNTER-ORBIT**: the exact integer intersection,
   cycle lengths, visited fractions, and rank-one closure of the natural
   integer counter inside the rank-four local additive module.
3. **RAMIFIED-AFFINE-ADDRESS-TRANSITIVITY**: translation by one and
   multiplication by `J` preserve levels, yet together generate every
   integral translation and act transitively at every finite level.
4. **RAMIFIED-TREE-TRANSPORT-RADIUS**: under the explicit independent-cell,
   literal-address and finite-radius contract below, transport by either
   `+1` or `J` requires at least `ceil(2k/R)` steps at depth `k`.
5. **RAMIFIED-TREE-TRANSPORT-CAPACITY**: if total cell states have a fixed
   finite alphabet as well, exact simultaneous transport obeys the
   cut-transcript bound `Q^(b_R tau)>=q^(5^(K-1))` at depth `K`, with
   `b_R=(5^R-1)/4`.

All five are statements of exact L1 mathematics. They do not identify the
tree with physical space, its vertices with native subsystems, a graph
metric with a physical metric, or an abstract operation with a fired native
instruction.

## 2. Integral identities and the intrinsic ideal

Directly in `O`,

```text
J^(-1) = -j-j^2,
j = (J-1)^3,
beta^4 = 5 J^2.
```

Indeed, `J(-j-j^2)=-j-j^2-j^3-j^4=1`, and
`(J-1)^3=j^6=j`. Reducing `(1-j)^4` with the cyclotomic relation gives
`5(-j+j^2-j^3)`, while `J^2=-j+j^2-j^3`. In particular `J` is a unit,
`Z[J]=O`, and `(5)=P^4`. The last equality is an ideal equality;
`beta^4=5` is not an element identity.

The quotient by `P` sets `j=1`, and the cyclotomic relation then sets
`5=0`. Hence

```text
O/P = F_5,       P intersect Z = 5 Z.
```

Thus `P` is prime. It is the unique prime of `O` above five: any prime
containing `(5)=P^4` contains `P`, and `P` is already maximal. Consequently
every Galois automorphism of `Q(j)` preserves `P` and every power `P^k`.
Replacing a generator `beta` by an associate does not change these ideals.
This is the precise intrinsic meaning used here. It is relative to the
ramified prime five already determined by the cyclotomic arithmetic, and
does not assert uniqueness of every conceivable geometry on `O`.

Multiplication by `beta^r` identifies the additive quotient `O/P` with
`P^r/P^(r+1)`. Therefore each successive quotient has five elements and

```text
[O:P^k] = 5^k       for every k >= 0.
```

For nonzero `x` in `O`, let `v_P(x)` be the largest `r` such that
`x in P^r`. This largest value is finite: divisibility by `beta^r` forces
`5^r` to divide the nonzero integer absolute norm of `x`. The valuation
has the usual multiplicative and minimum properties, either from the
prime-ideal valuation or the localization at `P`.

## 3. The rooted coset tree and its two metrics

Let `T` have vertices the subsets `a+P^k` of `O`, for `a in O` and
`k>=0`. Its root is `O`. Join two vertices when one is an immediate strict
subset of the other **within this family of cosets**. Equivalently, the
children of `a+P^k` are its cosets modulo `P^(k+1)`.

This equivalence follows because a contained coset at a depth more than
one greater has an intermediate coset. Each vertex at positive depth has
exactly one parent, and every vertex has five children by
`|P^k/P^(k+1)|=5`. Repeated parent maps reach `O`; there are no cycles.
Thus `T` is a rooted tree, with `5^k` vertices at depth `k`.

No external spatial coordinate is required in this definition. The symbol
`k` names the depth recovered from containment and the root. Restricting
to this ideal chain matters: unrestricted maximal proper subideals would
also involve other rational primes and would define a different graph.

For vertices `v=a+P^k` and `w=b+P^l`, their last common ancestor has depth

```text
h = min(k,l,v_P(a-b)).
```

To prove this, an ancestor at depth `r<=min(k,l)` is common exactly when
`a-b in P^r`. Therefore the graph distance, assigning length one to each
tree edge, is

```text
d_T(v,w) = k+l-2 min(k,l,v_P(a-b)).                     (1)
```

The truncated valuation in (1) is independent of the chosen coset
representatives. At equal depth this becomes

```text
d_T(a+P^k,b+P^k) = 2(k-min(k,v_P(a-b))).               (2)
```

The boundary is the inverse limit `O_hat_P = lim O/P^k`. If its valuation
is normalized by `v_P(beta)=1`, one may equip it with the ultrametric

```text
d_P(x,y) = 5^(-v_P(x-y)),    d_P(x,x)=0.              (3)
```

Formula (3) is a metric on boundary points, whereas (1) is the path metric
on finite-depth vertices. They are not the same metric. In particular,
for every integer `n` and every `k>=1`,

```text
d_T(n+P^k,n+1+P^k) = 2k,       d_P(n,n+1)=1.         (4)
```

Both follow from `v_P(1)=0`. The graph displacement `2k` occurs at every
integer increment, not just at increments with a long positional carry.
The depth of a carry in a chosen numeral code is a third notion and is
not computed by (4).

## 4. Natural counter orbit and its closure

For a nonzero integer `n=5^t u` with `5` not dividing `u`, the residue of
`u` in `O/P=F_5` is nonzero. Thus `v_P(u)=0` and, from `(5)=P^4`,

```text
v_P(n)=4 v_5(n),
P^k intersect Z = 5^(ceil(k/4)) Z.                   (5)
```

The same ideal-intersection formula includes zero. The image of the
natural inclusion `Z -> O/P^k` therefore has exactly
`L_k=5^(ceil(k/4))` elements. Under addition by one, the orbit beginning
at zero consists of this image, and its nonnegative orbit already visits
all of it. Its fraction of the level is

```text
L_k / 5^k = 5^(ceil(k/4)-k) = 5^(-floor(3k/4)).      (6)
```

More generally every orbit of addition by one on the entire additive
group `O/P^k` is a coset of the subgroup generated by one. Every such
orbit has length `L_k`, and the number of orbits is
`5^(k-ceil(k/4))`. These are exact formulas for all `k`, including the
single root at `k=0`.

The `P`-adic and `5`-adic topologies on `O` agree because `P^4=(5)`.
Since `(1,j,j^2,j^3)` is an integral basis, its completion is a free
rank-four `Z_5`-module. In these coordinates the closure of the natural
integer copy is exactly `Z_5*1`, a free rank-one submodule. Indeed,
integer sequences are dense in `Z_5` in the first coordinate and have
zero other coordinates; conversely coordinate convergence preserves those
three zeros. The same closure is obtained from the nonnegative counter.

This rank statement is additive local arithmetic, not a claim about
physical dimension, topological dimension, or the dimension of every
possible reader image. Formulas (5)-(6) concern exactly the natural
inclusion of the integer counter. They do not quantify over arbitrary
functions of the full native state `(n,psi)`.

## 5. Level-preserving actions and affine transitivity

For `c in O`, translation `T_c:a+P^k -> a+c+P^k` is a rooted tree
automorphism, with inverse `T_(-c)`. Multiplication by a unit `u` gives
another rooted tree automorphism

```text
M_u:a+P^k -> ua+P^k,
```

because `uP^k=P^k`. Both types preserve depth, inclusion and graph
distance. They also act isometrically on the boundary metric (3).
In particular neither `A=T_1` nor `M=M_J` is a radial step between depths.

The displacement caused by `M` has the exact formula

```text
d_T(a+P^k,Ja+P^k) = 2(k-min(k,v_P(a))),              (7)
```

because `(J-1)a=j^2 a` and `j^2` is a unit. At every unit residue class
at depth `k>=1`, the displacement is `2k`, even though `M` is an
isometry of the tree.

Depth preservation does not prevent transitivity within a depth. For
every nonnegative integer `r`,

```text
M^r A M^(-r) = T_(J^r).                              (8)
```

Powers, inverses and compositions of these translations give
`T_(sum c_r J^r)` for all finite integer coefficient lists `(c_r)`.
Since `Z[J]=O`, proved in section 2, the group generated by `A` and `M`
contains `T_a` for every `a in O`. Thus it acts transitively on `O`, and
its induced action is transitive on `O/P^k` at every finite depth.

There is no conflict with section 4: one generator `A` alone has the
smaller counter orbits there, while the jointly generated group includes
many additional address operations. Nor does (8) make these operations
fired instructions of native `U`. No control schedule, coupling to a
native checkpoint, or physical implementation has been derived.

## 6. Exact local-dependence lemma

Let `G` be the full tree `T`, or its truncation at a depth `K`. A
configuration assigns a cell state to each vertex. Designate a payload
alphabet `D` with at least two symbols; other coordinates may carry
workspace, controllers or fixed tags. Their alphabet need not be finite
for this lemma.

A deterministic step has radius at most `R` if its output at every
vertex `w` depends only on the prior configuration restricted to
`B_R(w)`. The rule may depend on `w`, on a prescribed time and on local
tags. Different steps may use different rules. The same rules and
schedule must be used on the pair of inputs compared below; any
state-dependent control must itself be represented locally rather than
selected by an external global inspection of the input.

**Lemma.** After `tau` such steps, the output at `w` depends only on the
initial configuration in `B_(R tau)(w)`.

**Proof.** At zero steps this is the input at `w`. If the assertion holds
at `tau`, the next output at `w` depends on prior outputs at vertices
`z in B_R(w)`. Each of those depends on initial vertices within distance
`R tau` of `z`, all of which lie in `B_(R(tau+1))(w)` by the triangle
inequality. This proves the induction. Equivalently, an initial
difference supported at a single vertex `v` can affect only
`B_(R tau)(v)` after `tau` steps. Reversibility is not assumed. QED.

## 7. Literal-address transport lower bound

Fix `k>=1` and, for a truncated tree, `K>=k`. Let `sigma` be the
permutation of level `k` induced by either `A` or `M`. Freeze this
implementation contract:

1. Every assignment `x` of payload symbols to the level-`k` vertices is
   allowed. In particular assignments differing at just one such vertex
   are allowed.
2. The input payload at `v` is stored at that literal vertex. Auxiliary
   initialization, including all other vertex data, is the same for the
   two assignments in the one-vertex comparison. There are no
   input-dependent distant copies already initialized elsewhere.
3. A common sequence of `tau` radius-`R` steps must produce the transported
   payload at the literal destination, so that for every allowed `x` and
   every level-`k` vertex `v`, the designated output coordinate at
   `sigma(v)` equals `x(v)`.

**Theorem.** If `R>0`, every implementation satisfying this contract obeys

```text
tau >= ceil(2k/R).                                  (9)
```

For `R=0`, no such nontrivial transport is possible in any finite number
of steps.

**Proof.** For `sigma=A`, choose any level-`k` source `v`; equation (4),
with the same proof for arbitrary `a in O`, gives `d_T(v,A(v))=2k`.
For `sigma=M`, choose `v=1+P^k`, or any unit source; equation (7) gives
the same distance. Choose two payload assignments differing only at `v`
and give them identical auxiliaries. The required final payloads differ
at `sigma(v)`. The lemma says that they cannot differ there if
`R tau<d_T(v,sigma(v))=2k`. This proves (9) and the radius-zero case.
QED.

Consequently no fixed finite radius and no fixed finite step count can
implement either literal transport uniformly through all depths. For a
single local step the necessary condition is `R>=2k`.

The lower bound is `Omega(k)` for fixed positive radius, not an `O(k)`
implementation result. This proof gives no matching upper bound for
simultaneously routing all payloads. Congestion, finite cell capacity,
workspace, scheduling and reversibility can impose additional costs.

## 8. Finite-alphabet cut-capacity obstruction

Here impose the additional requirement that every cell's **total** state
alphabet has at most `Q` symbols, where `2<=q<=Q<infinity` and the
independent payload alphabet has `q` symbols. Controller states,
workspace, stored histories, tags and all other mutable coordinates are
included in this bound. Fix integers `K>=1`, `R>=1`, and put `G=T_K`, the
depth-`K` truncation of the tree. A common sequence of `tau` radius-`R`
steps must perform exact simultaneous literal-address transport at level
`K` for every payload assignment, as in section 7.

Choose a first-level coset `s=c+P` and let `S` be its descendant subtree
inside `G`, including `s`. There are `L=5^(K-1)` level-`K` leaves in
`S`. For translation by one, choose any `c`. The image of each such leaf
belongs to the distinct first-level subtree `c+1+P`, hence is outside
`S`. For multiplication by `J`, choose `c!=0` in `F_5`; since
`J mod P=2`, the image belongs to `2c+P`, again outside `S`.

Hold fixed all initial states outside these `L` source payloads and vary
their `q^L` possible assignments independently. In particular the entire
outside initialization and all auxiliaries are common to these inputs.
Define the inside boundary band

```text
B = {v in S : d_G(v,G\S)<=R}.
```

The unique edge joining `S` to its complement joins `s` to the root.
Consequently an inside vertex of global depth `d` has distance `d` to
the complement. Thus `B` consists precisely of the inside vertices at
depths `1,...,min(R,K)`, and

```text
b=|B| = sum_(d=1)^(min(R,K)) 5^(d-1)
      = (5^(min(R,K))-1)/4.                          (10)
```

**Theorem.** Under these additional finite-alphabet and simultaneous
transport premises,

```text
Q^(b_R tau) >= q^L,       L=5^(K-1),                (11)
tau >= ceil(L log(q)/(b_R log(Q))),
b_R=(5^R-1)/4.                                     (12)
```

**Proof.** Associate to an input assignment its boundary transcript: the
complete states of the `b` cells of `B` at times `0,...,tau-1`. There are
at most `Q^(b tau)` such transcripts.

Two executions with the same transcript and the common outside initial
state have identical states outside `S` at every time through `tau`.
This is an induction. If their outside states agree at time `t`, a
radius-`R` update at any outside vertex can inspect inside `S` only at
vertices in `B`. Those states agree by the transcript at time `t`; all
outside inputs to the update also agree by induction. Hence all outside
states agree at time `t+1`.

If two distinct source assignments had the same transcript, their
outside final states would therefore agree. Exact simultaneous
transport, however, puts their differing source symbol at its literal
image outside `S`. The outside final states must differ there, a
contradiction. The transcript map is injective on the `q^L` source
assignments. Thus `Q^(b tau)>=q^L`; since `b<=b_R`, this proves (11),
and taking logarithms gives (12). QED.

On the infinite tree take `G=T` and the full descendant subtree `S`.
The identical proof has `b=b_R`; all other initial cells are held fixed.
Formula (11) therefore applies uniformly to the
infinite tree and every finite truncation containing depth `K`.

For fixed `q,Q,R`, this is an exponential lower bound in depth:
`tau=Omega(5^K)`. It is stronger than the distance bound under its
additional premises. It does not contradict section 7, which allows
unbounded cell alphabets and does not use simultaneous payload capacity.
Neither bound claims an upper bound or optimal schedule.

The finite-state bound is load-bearing. An unbounded register near the
cut, a source-dependent outside initialization, a nonlocal output reader,
an external input-dependent schedule, or transport of only one known
payload changes the counting problem and is outside (11). Likewise, if
`Q` grows with `K`, inequality (11) still applies with that value of `Q`,
but the fixed-alphabet exponential conclusion need not follow.

## 9. Boundary of the native conclusion

The native counter update is the atomic relation `n -> n+1`. Under the
natural address reading `n -> n+P^k`, it has the graph displacement (4).
Calling these vertices simultaneous independent cells and requiring that
one native tick implement their transported payload is an additional
representation contract. **Under that contract**, uniformly bounded
local implementation is excluded by (9).

This result does not prove that every possible physical reading of
native `U` is nonlocal or impossible. It does not exclude another graph,
another encoding, a restricted carrier without independent payload
values, unbounded auxiliary information, or variable numbers of native
iterations between designated completion events. For example an equation
of the form `D(U^(r(omega))(omega))=V(D(omega))`, on an explicitly
specified event section with `r(omega)>=1`, uses a different time
contract and needs its own proof. Merely considering that contract does
not by itself modify native `U`.

The existing reachable-amplitude theorem is also relevant to scope:
for a stipulated bijective target `L`, all exact full-counter readers on
the origin-zero reachable domain have the form
`R(n,x)=L^n G(ell_n(x))`, with the target and the amplitude assignment
unselected. Thus the orbit form is a classification, not itself a defect
that can be prohibited to derive a universal no-go. Nor does conserved
`ell_n(x)` mean that the raw checkpoint `x` is constant; the conserved
chart depends on `n`.

What is established is a definite arithmetic geometry, an exact
restriction of its natural counter orbit, a positive affine
transitivity statement, a conditional finite-radius transport lower
bound, and a stronger simultaneous-transport capacity obstruction under
a fixed finite cell alphabet. A native spatial carrier, a selection rule
for physical readings, and an actual local interaction law remain to be
derived separately.
