# The summability dichotomy for the fixed-r=2 cell-sector ansatz

```text
STATUS:      NON-CANONICAL ANALYSIS NOTE. No claim status earned.
             Repository-certified inputs are the closed horizons 2..4,
             2..5, 2..6 and the special-block closures in horizon6_prep /
             horizon7_prep. Horizon-7 ordinary and coupled numbers below
             are an explicitly unpinned experiment, not a certificate.
SCOPE:       the DECLARED fixed-level-2 structured cell-sector ansatz of
             ENTROPY-SELECTION-RECON. Nothing here decides r > 2 collars,
             other sectors, or ENTROPY-LAYER-BRIDGE globally, exactly as
             the recon's stop conditions prescribe.
```

## 1. The exact finite-prefix dichotomy

Fix the level-2 family `F_2`. Let `T_H` be the finite, possibly empty set of
feasible prefixes `(F_2, ..., F_H)` in the declared ansatz and put

```text
D_H(F_2, ..., F_H) = sum_{l=2}^{H-1} d_l,
o_H                  = min_{T_H} D_H.
```

Use the extended-real conventions `min(empty) = +infinity` and
`inf(empty) = +infinity`.

Assume the finite problems are prefix-closed, each prefix has only finitely
many one-step extensions, and every `d_l` is nonnegative. These are the exact
finite-state conditions of this fixed-`F_2` cell-sector tree. Then, in the
extended nonnegative reals,

```text
inf over infinite chains (sum_{l>=2} d_l) = sup_H o_H.
```

In particular,

```text
there exists a chain with sum_l d_l < infinity
    if and only if
sup_H o_H < infinity.
```

The forward implication is immediate: each finite restriction of a summable
chain is feasible, so `o_H` is bounded by the corresponding partial sum.
Conversely, let `M = sup_H o_H < infinity`. Prefixes of accumulated cost at
most `M` form a rooted subtree with a vertex at every depth. Nonnegative costs
make it prefix-closed; the fixed root and finite branching make it a finitely
branching tree. Koenig's lemma supplies an infinite ray, and every partial sum
on that ray is at most `M`. Its total cost therefore converges. Combining both
directions gives the displayed equality. Restriction also shows that `o_H` is
nondecreasing, so unboundedness is equivalent to `o_H -> infinity`.

Thus the decision surface is exact:

```text
(A) bounded finite-horizon optima  <=>  a summable chain exists in this tree;
(B) unbounded finite-horizon optima <=> no summable chain exists in this tree.
```

This strengthens branch (A) from "not yet excluded" to existence inside the
declared prefix tree. It does not construct a canonical or measurable
selector and does not leave the fixed-`r=2` cell sector.

### Scale-invariant special-block lower bound

The common scale 48 and `OBJECTIVE_SCALE = 150000` apply to the displayed
horizons, not to all horizons. The exact denominator lcm is 24 for `H=4,5`,
jumps to 48 at `H=6`, to 96 at `H=10`, and to 192 at `H=18`. Asymptotic
statements must therefore use the original rational weights.

Let `b_H,j^ord` be the ordinary minimum for source block `j`, and let
`b_H^sp` be the special minimum, all in unscaled rational units. The
zero-price block dual gives

```text
3125 * o_H >= sum_{j=1}^{624} b_H,j^ord + b_H^sp >= b_H^sp.
```

If `q_H` is a valid integral scale and `B_H = q_H*b_H`, the same inequality is

```text
(q_H*3125) * o_H >= sum_{j=1}^{624} B_H,j^ord + B_H^sp.
```

The 624 ordinary minima happen to be homogeneous in the certified small
horizons. No such homogeneity is assumed asymptotically.

Consequently, special-block divergence is sufficient for branch (B) only in
the invariant sense `b_H^sp -> infinity`, equivalently
`B_H^sp/q_H -> infinity`. Growth of the raw scaled integer `B_H^sp` is not
enough when `q_H` changes. Conversely, bounded special minima do not decide
branch (A): the ordinary blocks or their global coupling may still diverge.

## 2. Exact small-horizon data and the open horizon `2..7`

At the common scale 48 the repository-certified comparisons are

```text
horizon   exact optimum     scaled   ordinary  special   named optimal-witness transitions
2..4      417/1250           50040       80      120     (209/2500, 1/4)
2..5      1459/2500          87540      140      180     (209/2500, 1/2, 0)
2..6      5939/7500         118780      190      220     (313/1875,
                                                          573/1250,
                                                          1249/7500, 0)
```

The special block is also repository-certified at horizon `2..7`:

```text
special minima (scale 48): 120, 180, 220, 260
special marginals:          +60, +40, +40
unscaled minima:            5/2, 15/4, 55/12, 65/12
```

Two consecutive scaled `+40` steps refute an exact geometric-progression fit
to these three marginals, but they prove neither a uniform unscaled floor nor
an asymptotic law.

### Unpinned ordinary/coupled experiment at `2..7`

A completed local experiment reported the following, but no ordinary dual,
MILP proof log, solution file, or coupled witness is committed in this branch:

```text
ordinary local-polytope optimum: 192 (denominator-5 primal, integer dual)
ordinary integral witness:       220 (exact replay and 624-fibre lift)
reported HiGHS MILP result:      220 with floating-point gap 0
special exact optimum:           260 (repository-certified)
joint integral witness:          624*220 + 260 = 137540
```

The reported exactly replayed joint witness gives the attainable upper bound
inside this unpinned experiment

```text
o_7 <= 137540/150000 = 6877/7500.
```

The reported LP dual would give the relaxation lower bound

```text
(624*192 + 260)/150000 = 30017/37500,
```

but that dual is not present here and is not repository-auditable yet. The
floating-point branch-and-bound lower bound is likewise not a replayable exact
certificate excluding integer cost `<= 219`. Therefore this note does not
state `o_7 = 6877/7500`.

The reported experiment outcomes are:

```text
E1  PASS for the named witness: the terminal 6 -> 7 transition costs 0.
E2  reported FAIL in the solver output: the candidate integer optimum has
    marginal 220 - 190 = 30, outside [40, 60].
E3  reported PASS literally: the LP dual is integral.
    The floating-point B&B result indicates that the relaxation is not tight,
    with candidate gap 220 - 192 = 28.
```

An integral dual does not imply an integral primal optimum, and terminal zero
is recorded only for this witness, not for every optimum.

## 3. The transition-local kill shot is falsified

The proposed positive-value obstruction packing confined to the newly added
transition does not exist. Exact isolated-slice replay gives

```text
transition   edges   vertices   components   cycle rank   nonzero holonomy
4 -> 5          24         22            4            6                   0
5 -> 6          32         28            6           10                   0
6 -> 7          40         36            6           10                   0
```

On every isolated slice, root propagation constructs a consistent potential
on every connected component. Each slice therefore admits a zero-cost
labeling. No positive-value obstruction certificate can be supported only on
the new transition. The observed `+40,+40` special increments arise only
after coupling the new slice to earlier levels and the fixed anchor.

The stronger assertion that one edge of an obstructed walk must carry a full
mismatch 5 is also false in general. The valid statement is a capacity
inequality. For an isometric edge transport `T_e`, let

```text
d_e(x)   = rho(x_head(e), T_e x_tail(e)),
n_C(e)   = the multiplicity of edge e in a closed walk C,
delta(C) = min_z rho(z, H_C z),
```

where `H_C` is the holonomy of `C`. The triangle inequality gives

```text
sum_e n_C(e) d_e(x) >= delta(C).
```

For nonnegative allocations `a_C` satisfying the combined capacity constraint

```text
sum_C a_C n_C(e) <= w_e                         for every edge e,
```

one obtains the dual lower bound

```text
sum_e w_e d_e(x) >= sum_C a_C delta(C).
```

Terminal-to-terminal paths obey the same argument after both endpoint anchor
distances are included in the path inequality and both endpoint anchor edges
are charged against their own capacities. The capacities `w_e` are the
original rational weights in an asymptotic statement; multiplying them by
`q_H` produces only a `q_H`-scaled finite-horizon bound.

## 4. Surviving proof program: global duals or logarithmic bands

Two routes remain viable:

1. one global capacity dual on the complete anchored graph; or
2. compatible obstruction packings in bands that reach far enough backward
   to expose the conflict with inherited levels and boundary data.

In both routes the combined load of all certificates, not each certificate
separately, must satisfy every edge capacity.

Let `K(L)` denote the tested backward band width needed to expose an
obstruction involving scale `L`, including inherited boundary data. The
reported census through `L=129` satisfies

```text
K(L) <= ceil(log_2 L) + 1.
```

No census artifact is committed here, so this is finite experimental evidence
only: it proves neither the inequality for all `L`, a positive uniform defect,
nor global capacity compatibility.

To fire branch (B), construct globally capacity-feasible certificates whose
values in original rational units tend to infinity. One sufficient conditional
route would provide, for every sufficiently large endpoint `L` (or a linearly
dense set of endpoints), a uniform unscaled value `c > 0` and a uniform
constant `A` with band width at most `A log L`. The loaded supports, including
all inherited boundary and terminal capacities, must then be selectable
disjointly or fractionally charged within capacity. Only under all of these
conditions does a disjoint selection yield on the order of `H/log H`
contributions and force divergence. If the same anchor edges recur in every
band, disjoint-band counting is unavailable and the global dual is required.

For horizon `2..7`, the immediate exact task is narrower: freeze and replay an
integer infeasibility certificate for ordinary cost `<= 219`, then replay the
joint witness. Until that lower certificate exists, `6877/7500` remains an
attainable value rather than a closed optimum.

## 5. Non-claims

- No asymptotic special marginal or log-band theorem is claimed.
- Bounded special minima do not imply bounded coupled optima.
- The terminal-zero value belongs to one reported witness, not every optimum.
- An integral LP dual does not imply tightness of the integral problem.
- Koenig's lemma produces a summable chain only inside the declared fixed-`F_2`,
  fixed-`r=2` prefix tree; it supplies no canonicity, measurable selector,
  regularity, entropy, or global layer-bridge statement.
- A negative branch would close only this cell-sector ansatz. Wider collars
  and other sectors of ENTROPY-LAYER-BRIDGE remain untouched.
