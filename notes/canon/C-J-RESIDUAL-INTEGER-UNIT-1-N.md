# C-J-RESIDUAL-INTEGER-UNIT-1-N

Status: **FROZEN CANDIDATE DEFINITION / NON-CANONICAL / NO VERIFIER / NO
FORMAL RUN / NO PUBLIC STATUS / CANON UNCHANGED.**

Date: **2026-09-04.**

This note freezes one candidate meaning of an integer unit for the next
coincidence probe. It corrects one tempting but non-invariant phrase:
`a path that survived cancellation`. The coefficient magnitude is canonical;
the identity of a surviving historical path generally is not.

Nothing here defines a physical record, event, occurrence, frequency,
probability, observer, or apparatus. The one proposed physical line is stated
separately in section 8 and remains `candidate-H / STOP`.

## 0. Authority and scope

```text
authority:       mathorn1973/twist-j main
base main:       06ef23bc0ae7130214c15a5b9c0b4478d6fcbbfc
Canon:           Public Canon v75
state:           ACTIVE
tag:             canon-v75
tag target:      c4f00e1d9c89f503d913224dc3c09dc760dcec9d
content commit:  e32e85ed7297d4320df5b345e4488d78323d550c
Canon SHA-256:   44130160a3ce29bfcdc757e255d2d1c25a010b22911edfe66cf6b132be081fbe
Canon bytes:     399513
formal runs:     NONE
public status:   NONE
```

The two immediate algebraic inputs are the public but unregistered probe
results merged by PRs #805 and #807. The first separates the raw `J` step from
the integral mixer `A` and normalized isometry `U_5`. The second exposes the
full-cell controlled copy, its diagonal quadratic Gram contraction, and the
compression obstruction. Neither input gives the diagonal entries a counting
or physical meaning.

The divergent note `C-J-PLENUM-BORN-CHAIN-1-N` is a design predecessor. This
note narrows one definition needed by that design and does not promote or
silently import its candidate claims.

## 1. Candidate definition: reduced residual unit

For `n>=0`, let

```text
[n]={1,...,n},       [0]=empty set.
```

For an integral five-cell coefficient vector

```text
d=(d_0,...,d_4) in Z^5,
```

put

```text
d_k^+=max(d_k,0),       d_k^-=max(-d_k,0).
```

The two signed residual fibres in cell `k` are

```text
U_k^+(d)={(k,+,m):m in [d_k^+]},
U_k^-(d)={(k,-,m):m in [d_k^-]}.
```

Exactly one of them is nonempty. Define

```text
U_k(d)=U_k^+(d) disjoint-union U_k^-(d),
U(d)=disjoint-union_k U_k(d).
```

One element of `U_k(d)` is a **reduced residual integer unit**. It carries
only:

1. its cell label `k`;
2. the sign of the reduced coefficient;
3. a fresh ordinal label `m` at the selected cut.

The reconstruction and cardinality identities are immediate:

```text
d_k=|U_k^+(d)|-|U_k^-(d)|,
|U_k(d)|=|d_k|,
|U(d)|=sum_k |d_k|.
```

The ordinal representative makes the finite set literal rather than only
specified up to bijection. It is regenerated from the reduced coefficient at
each cut. It does not assert persistence of token `m` between cuts.

This is a candidate definition, not a theorem that Nature realizes such
objects.

## 2. Why a historical surviving path is not canonical

Suppose a coefficient in one cell is presented by finite labelled positive
and negative word sets `W^+` and `W^-`:

```text
d_k=|W^+|-|W^-|.
```

Cancellation requires a matching between opposite signs. If

```text
W^+={a,b},       W^-={c},
```

either `a` or `b` may be paired with `c`. The reduced coefficient is `+1` in
both cases, but the alleged surviving historical path differs. No ordering,
matching, priority rule, or microscopic ancestry has been supplied by integer
addition.

What is invariant under every presentation and cancellation matching is only

```text
sign(d_k),       |d_k|.
```

Therefore this note does not call elements of `U_k(d)` surviving paths. They
are fresh normal-form tokens representing the residual signed multiplicity.
Any theory that needs path identity, ancestry, or token persistence must add a
separate rule and expose its dependence on the chosen word presentation.

Equivalently, signed finite populations form the Grothendieck completion of
finite sets under disjoint union. The integer is the invariant class. The
ordinal fibre above is a chosen normal-form representative of that class, not
a selected subset of the original words.

## 3. Covariance and state-locality

A permutation `pi` of the five cells transports the normal form by

```text
(k,sign,m) -> (pi(k),sign,m).
```

Thus cell relabelling preserves every fibre cardinality and only permutes the
fibres.

For a general integral linear update `T`, the output carrier is defined by

```text
U(Td)
```

after matrix multiplication and signed reduction. There is in general no
canonical map from individual tokens of `U(d)` to individual tokens of
`U(Td)`. Matrix addition can create opposite contributions in one output cell,
and the same cancellation ambiguity reappears.

The unit ontology frozen here is therefore **state-local**. It gives an exact
finite carrier at a cut. It does not give trajectories of units, a branching
tree, a world count, or a microscopic dynamics.

## 4. The integral mixer and the normalized isometry must not be conflated

On the augmentation lattice, the current convention is

```text
A=1+g^2-g^3-g^4,
U_5=A/sqrt(5).
```

The integral map `A` sends integer states to integer states and satisfies

```text
q(Ad)=5q(d),       q(d)=sum_k d_k^2.
```

It can therefore act on the literal residual fibres above. The normalized map
`U_5` preserves `q` algebraically, but generally sends an integer vector to a
non-integral vector. Without an independently frozen unit quantum on the
scaled tower, `U_5d` does not itself define a finite set with `|d_k|` elements.

Accordingly:

```text
A    is the available integral count update;
U_5  is the normalized direction/profile update.
```

Saying that literal pair counts multiply by five is an `A` statement. Saying
that the quadratic norm is preserved is a `U_5` statement. Interchanging the
two names would change the model.

## 5. Single units do not carry a state-independent extensive law

Let

```text
L(d)=|U(d)|=sum_k |d_k|.
```

For the supported vertex

```text
d_0=(4,-1,-1,-1,-1),
Ad_0=(5,0,5,-5,-5),
```

one has

```text
L(d_0)=8,       L(Ad_0)=20,       ratio=5/2.
```

For the supported vector `5h`, with

```text
h=(-1,1,0,0,0),
Ah=(-2,1,-1,2,0),
```

one has

```text
L(5h)=10,       L(A(5h))=30,       ratio=3.
```

Thus no state-independent multiplier governs the number of single residual
units under `A`. By contrast, the quadratic total has multiplier five on both
witnesses and on every augmentation state.

These two witnesses are enough for the present exclusion. The stronger
all-exponent power-sum characterization proposed in
`C-J-PLENUM-BORN-CHAIN-1-N` remains NON-CANONICAL and is not claimed here.

## 6. What the Cayley copy does and does not count

On the full orthogonal cell register, the controlled addition proved in the
probe merged by PR #807 gives

```text
K d=sum_k d_k e_k tensor e_k.
```

As one signed coefficient vector on the diagonal joint basis, `Kd` has
`|d_k|` reduced joint coefficient units in diagonal cell `(k,k)`. Linear
copying does **not** by itself turn one coefficient `d_k` into `|d_k|^2`
joint coefficient units.

The exact algebraic contraction is nevertheless

```text
Gram_record(Kd)=diag(d_0^2,...,d_4^2).
```

The square appears because the contraction is bilinear. Calling that square a
population requires a new combinatorial object.

To display the missing object, make two tagged copies of the state-local
normal form:

```text
U_k^S(d)={S} x U_k(d),
U_k^R(d)={R} x U_k(d).
```

The **complete within-cell coincidence set** is

```text
C_k^x(d)=U_k^S(d) x U_k^R(d).
```

Its cardinality is the elementary product theorem

```text
|C_k^x(d)|=|d_k| |d_k|=d_k^2.
```

Hence

```text
sum_k |C_k^x(d)|=q(d),
(|C_0^x|,...,|C_4^x|)=diag(Gram_record(Kd)).
```

This equality is the exact algebraic-combinatorial seam. It is not yet the
physical bridge.

## 7. The Cartesian product is the entire missing choice

Two fibres with `|d_k|` elements do not force the complete product to be the
realized relation. A coincidence relation could be any subset

```text
C_k subseteq U_k^S(d) x U_k^R(d).
```

For example, the ordinal diagonal relation

```text
C_k^diag={((S,u_m),(R,u_m)):m in [|d_k|]}
```

has only `|d_k|` pairs. The empty relation has zero. Partial matchings and
arbitrary bipartite graphs give intermediate values. The two marginal fibre
sizes alone therefore do not imply the exponent two.

The exponent is a theorem **after** complete Cartesian incidence is chosen:

```text
complete within-cell incidence  =>  d_k^2 pairs.
```

It is not a theorem that complete incidence is physically realized. That is
exactly the one non-algebraic line which the next probe must isolate.

Under the complete relation, the algebraic extensive law becomes a literal
finite-cardinality law for integral states:

```text
|C^x(Ad)|=5|C^x(d)|,
C^x(d)=disjoint-union_k C_k^x(d).
```

The single-unit total `L(d)` has no corresponding state-independent law. This
explains why single units cannot be substituted for pairs in the proposed
frequency reading.

For the two exposed states,

```text
d_0=(4,-1,-1,-1,-1):       pair counts (16,1,1,1,1), total 20,
Ad_0=(5,0,5,-5,-5):         pair counts (25,0,25,25,25), total 100.
```

The exact zero is combinatorially dark only because the corresponding two
fibres, and hence their product, are empty.

## 8. The sole proposed physical line

The next probe must place every mathematical statement outside the following
box and this one line inside it:

```text
COINCIDENCE-RECORD-FREQUENCY [candidate-H / future L5-L6 / STOP]

At a frozen calibrated read cut for a supported nonzero integral preparation,
the physically realized record population is exactly

    C^x(d)=disjoint-union_k U_k^S(d) x U_k^R(d),

with every within-cell ordered pair realized once and no other record. The
ensemble is this simultaneous finite plenum itself, not repetition in time and
not a set of modal branches. Observed cell frequency is finite self-location
in this record population:

    f_k(d)=|C_k^x(d)|/|C^x(d)|=d_k^2/q(d).
```

This single row does three inseparable physical jobs: it selects complete
incidence, declares its pairs realized records, and identifies finite
self-location frequency with their cardinality ratio. Splitting those jobs
into hidden prose would only hide hypotheses; it would not reduce them.

The row gives no stochastic law for one run. Every pair is realized. The
question `which result do I see?` is a self-location question inside the
finite realized relation.

Model-level falsifiers are:

1. a frozen apparatus whose realized record counts are not the diagonal of
   the joint Gram contraction;
2. a missing or multiply counted within-cell Cartesian pair;
3. an off-cell record or a record with no system-record coincidence;
4. a nonzero realized record in a cell with `d_k=0`.

Operational use of these falsifiers still requires the typed apparatus,
background, gain, resolution, preparation, and read-cut ownership currently
missing from `QDD-INSTRUMENT-APPARATUS [O]`.

## 9. Raw `J` versus `A/U_5` is an owner fork, not part of the definition

The complete-pair carrier makes the scaling difference visible but does not
choose the physical step.

```text
A:    |C^x(Ad)|=5|C^x(d)| for every integral augmentation state.
U_5:  q(U_5d)=q(d), but literal integer fibres need an extra scale law.
J:    q(Jd)/q(d) is state-dependent.
```

For the raw `J` orbit of `d_0`, the first totals are

```text
20, 30, 70, 180.
```

Thus a raw-`J` physical reading contains creation and loss of total record
capacity with no universal gain. It needs a scale or yield channel. Restricting
the count evolution to `A`, while using `U_5` for normalized profiles, avoids
that particular defect but makes the separation of the positive polar factor
`B` a physical choice.

This note makes neither choice. The owner fork comes after the coincidence
probe, where the precise cost of each branch can be read against the same
frozen record definition.

## 10. Firewalls

- This note is NON-CANONICAL and creates no `[T]`, `[D]`, `[C]`, `[H]`, `[O]`,
  or `[F]` row.
- The candidate unit is a normal-form finite token, not a particle, path,
  world, detector click, or persistent object.
- The sign remains part of coefficient reconstruction but drops out of fibre
  cardinality. No physical interpretation of sign is supplied.
- The controlled copy supplies a diagonal joint coefficient, not two
  independently populated physical registers.
- The Gram contraction supplies `d_k^2` algebraically, not a count.
- Two equal marginal counts do not force complete bipartite incidence.
- Darkness and exponent two become counting theorems only inside the chosen
  complete incidence relation.
- The identification of that relation with realized records and frequencies
  is the sole candidate-H line and remains STOP.
- No collapse, stochastic seed, temporal repetition, modal branch measure,
  continuous hidden trajectory, or single-run randomness is introduced.
- `QDD-INSTRUMENT-APPARATUS [O]`, the typed L5 event stream, and the L5-to-L6
  Born reading gate remain open.
- Public Canon, Registry, Frontier, gates, dictionaries, and `STATUS.md` are
  unchanged.
