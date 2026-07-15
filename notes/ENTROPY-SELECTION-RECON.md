# Entropy selection recon

Status: **NON-CANONICAL LOCAL ANALYSIS**

This note starts the successor analysis to the finite entropy bridge and
mirror work. It is not a preregistration, verifier record, or evidence bundle.
No target below is frozen and no claim status is earned.

## Public inputs

The analysis uses only public finite facts under Public Canon v6. The mirror
result is public probe evidence merged by PR #37 and folded at its finite
scope as `ENTROPY-MIRROR-LAW [C]` in Public Canon v5:

- the recurrent core has 6250 states and two living halves of 3125 states;
- each branch restricts bijectively between living halves;
- living trajectories over a fixed driver word number 3125;
- `|O/lambda^5| = 3125` and multiplication by `J` has orbit spectrum
  `{1: 1, 4: 1, 20: 156}`;
- every living half has 625 canonical pentagons of five states;
- the finite-cylinder selector route is already falsified;
- the coherent-gauge block cocycle is affine and periodic on the tested
  dyadic levels;
- the merged mirror probe establishes at its frozen finite scope that one-tick
  cell maps are reflections and the two own-half maps have a unique singlet
  fixed state.

### Binding definition boundary

The bridge source is not waiting for new definitions of `Y_5` or `nu_*`.
The pinned owner ruling in `P-ENTROPY-BRIDGE-1` at
`9fc7a6c3a3d1d4024f4bd9f8fdb844733a80fbc8` already fixes:

- `Y_5 = O_{K,lambda}` for `K = Q(zeta_5)` and `lambda = 1-zeta_5`, with
  verb `y -> J y`; the kernel coordinates `q,r` must come from higher
  lambda-adic digits and carry rather than free factors;
- the two-sided Thue--Morse base `K_TM`, its shift `S_K`, measure `m_TM`, and
  reading `theta(kappa)=kappa_0`;
- the source, finite cut, and almost-everywhere equivariance equation; and
- the Cesaro sequence `nu_N`, the candidate limit `nu_*`, and the required
  component and recurrent-state weights.

Existence of `nu_*` and the asserted closed form are mathematical gates, not
owner choices that may be supplied by a definition. The exact public kernel
constants, selector, and census are also already present in the public probes;
the local target reconstruction imports the merged public mirror verifier
without invoking its formal entry point.

Three contract choices remain before any public result may claim canonicity or
regularity:

1. the equivalence relation for transfer families (in particular, the
   2500-element arithmetic unit action is not silently identified with the
   full permutation centralizer);
2. the regularity class and quantifier, including whether the equation is
   everywhere or `m_TM`-almost everywhere; and
3. unambiguous notation for the living fiber. This recon uses `L_kappa`;
   the public shorthand `L_n` is unsuitable here because `L_n` already denotes
   the Lucas numbers elsewhere in the Canon.

These choices do not block the current local existence and falsification
work. They must be frozen before a later public probe whose decision surface
uses uniqueness, canonicity, or regularity.

A minimal proposed working contract, still non-canonical and subject to owner
review, is:

```text
Q_5       = O/lambda^5,
H_eps     = Im(F_eps | recurrent core),
L_kappa   = H_(kappa_-1),
F_(kappa_0): L_kappa -> L_(S_K kappa).
```

Represent a transfer by a Borel family on an `S_K`-invariant conull subset of
`K_TM`, with equivariance there for every `y in Q_5`. Identify two
representatives only when they agree `m_TM`-almost everywhere for every finite
`y`. For the canonicity test, the proposed primary equivalence is constant
precomposition by a unit of `(O/lambda^5)^x`, of order 2500. A quotient by the
much larger full permutation centralizer is retained only as a sensitivity
comparison: it preserves the `J` cycle type but forgets the arithmetic
structure. No kappa-dependent relabeling or post-hoc target-cell gauge is
admitted. The pushforward to `nu_*` remains a theorem gate under this proposal.

This is not yet a public issue lock. The current recon has neither a compatible
inverse system nor a global obstruction, so a scientific preregistration would
still be premature.

The sought equation is

```text
Psi_(S kappa)(J y) = F_(theta(kappa))(Psi_kappa(y)),
```

with `Psi_kappa` a bijection from `O/lambda^5` to the living fiber appropriate
to `kappa`. A fiberwise bijection turns the question into conjugacy of two
finite permutation cocycles over the Thue--Morse base.

## First diagnostic: repeated dyadic supertiles

`notes/ENTROPY-SELECTION-RECON.py` compares, for `L = 2^n`, the monodromy
cycle type of `J^L` on `O/lambda^5` with the living-kernel monodromy obtained
by repeating the length-`L` Thue--Morse prefix.

For every tested `n = 2..10`, the source type is

```text
{1: 5, 5: 624}.
```

The target types are

```text
n = 2,3,4,6,7,8,10:  {5: 625}
n = 5,9:              {1: 3125}
```

Therefore no tested repeated-supertile model admits a fiber conjugacy to
`J^L`. This is not a no-go for the desired measurable family: the Thue--Morse
subshift is aperiodic, so these periodic repetitions are diagnostics rather
than points of the actual base system.

Two features are nevertheless informative:

1. On the non-identity levels, all 312 size-20 component-halves split into two
   five-cycles. This exactly accounts for the source's 624 nontrivial
   five-cycles. The residual mismatch is concentrated in the five-state
   singlet sector: five source fixed points versus one target five-cycle.
2. At levels `n = 1 mod 4` in the tested range, the target block map is the
   identity on the whole living fiber while `J^(2^n)` is not. A stationary
   block dictionary cannot absorb this. Any viable transfer must depend on
   the unbounded 2-adic phase/carry of `kappa`.

This agrees with the earlier finite-cylinder no-go but is a different
observation: it identifies where a naive lambda-digit/living-state dictionary
breaks at dyadic renormalization scales.

## Structural reduction to attempt

Use the canonical decomposition

```text
living state = (recurrent component, pentagon cell, q in F_5).
```

On the target, one tick acts by a component-preserving cell permutation and
an affine reflection `q -> -q + b`. Longer dyadic blocks act by translations
in the tested coherent gauge. On the source, represent `O/lambda^5`
explicitly by five lambda digits and separate the carry induced by `J`.

The transfer family should then be solved in layers:

1. component label;
2. pentagon-cell label;
3. within-cell `F_5` coordinate;
4. singlet correction;
5. compatibility under refinement of the 2-adic phase.

The objective is a cohomological transfer equation over the 2-adic factor,
not a lookup table on a bounded Thue--Morse window.

## Explicit source and target models

The local package `notes/entropy_selection/` now implements both finite
carriers without changing a public file.

For the source, substitution in `Phi_5(zeta)=0` gives

```text
lambda^4 = -5 + 10 lambda - 10 lambda^2 + 5 lambda^3,
(lambda^5) = (5 lambda),
O/lambda^5 = Z/25 + (Z/5)^3.
```

The code enumerates all 3125 canonical five-digit classes, performs exact
ring arithmetic and carries, and reconstructs multiplication by
`J = 1 + zeta^2`. Its full orbit spectrum is exactly
`{1: 1, 4: 1, 20: 156}`. Two different symmetry objects are retained:

```text
ring-unit multiplication subgroup:  (O/lambda^5)^x, order 2500;
full permutation centralizer:         C_4 x (C_20 wr S_156).
```

The second is vastly larger. Neither is silently declared a gauge group, and
literal uniqueness of a transfer is impossible before an equivalence relation
is specified.

For the target, the merged mirror definitions are reconstructed, without
running their formal entry point, as exact addresses

```text
(component, half, cell, xi),  xi in F_5.
```

The reconstruction has 313 components, 1250 pentagons, and all 6250 recurrent
states. Direct comparison with the public kernel passes eight local gates,
including every one of the `2 x 6250` one-tick transitions. One tick is stored
as a cell map and a genuine affine rule on `xi`; no spectrum-only replacement
is used.

## Source-sector construction

At a level-`r` substitution boundary, `r >= 2`, each oriented 20-cycle of `J`
splits by orbit position modulo four. This gives

```text
156 x 4 = 624 five-point sectors,
4 points of the unique 4-cycle + zero = 5 singleton sectors.
```

These counts match, respectively, the 624 nonsinglet target pentagons in a
living half and the five points of its singlet pentagon. On each five-sector,

```text
J^(2^r): q -> q + delta_r,
delta_r = 2^(r-2) mod 5 = 1,2,4,3,... .
```

The implementation checks this on all source points at every executed scale;
it is not inferred from the aggregate orbit spectrum.

## Reduced exact-context solver

The base is the actual Thue--Morse language. A width-`w` Rauzy vertex is an
allowed desubstituted factor `(previous,current,future,...)`; an edge is an
allowed factor of length `w+1`. No supertile is closed periodically. Graph
cycles impose only consistency of a function constant on those cylinders.
The finite language now has a bounded substitution-closure certificate: for a
factor of length `n`, choose the least `k` with `2^k >= n-1`; every factor lies
in `sigma^k(ab)` for one of the four explicitly witnessed legal pairs `ab`.
Exact rational cylinder frequencies come from the two substitution phases and
pass left/right marginal, complement, and reversal gates through length 20.

For each source sector, the solver first propagates a target cell section.
It then solves, over `F_5`,

```text
xi_v = A_v q + d_v,
A_v = alpha_e A_u,
d_v = alpha_e d_u + b_e - A_v delta_r
```

on every graph edge. All root slopes `A != 0` and root offsets are enumerated.
To ensure this is not an artifact of the affine restriction, the solver also
enumerates all 120 bijections of a five-point source group to every one of the
625 target cell sections. It tests both a source five-cycle and five labeled
fixed points. Thus the fixed points may occupy a nonsinglet cell and a
five-cycle may occupy the singlet; that assignment is not hardcoded. The
mirror-aligned singlet route is retained as a separate diagnostic.

Executed grid: levels `r = 2..6`, context widths `w = 2..8`. Within that exact
factor census, every one of the 35 decisions returned the same layered result:

```text
cell sections:                  624 / 624
target block multipliers:       {1}
affine nonsinglet sections:       0 / 624
unrestricted S5 five-cycle cells: 0 / 625
unrestricted S5 fixed-point cells: 0 / 625
consistent singlet root values:   0 / 5
reduced exact-context transfer: EMPTY
```

Thus the component/cell matching survives completely, while the obstruction
is in the within-pentagon coboundary. Exhausting `S_5` shows that the result is
not created by the affine sub-ansatz or by forcing the five special points
into the mirror singlet. `EMPTY` closes only the finite-context cell-sector
ansatz at the named levels and widths. It is not a global no-go for a
measurable transfer with growing context.

## Explicit Rokhlin-tower baseline

There is also a concrete family of 3125-point bijections, not merely a solver.
At each tower base, ordered source five-sectors are matched to ordered target
pentagons and the five singletons to the singlet points. Inside a level-`r`
tower it is filled by

```text
B_(u,j) = F_(prefix j) X_u J^(-j).
```

Consequently the skew equation and fiber bijectivity are checked exactly at
every interior floor. Only actual allowed Thue--Morse roof transitions are
tested. The lexicographic baseline produced:

```text
r   height   roof carrier-defect fractions   roof-error upper bound
2      4     {1/625, 1}                      <= 1/4
3      8     {1}                             <= 1/8
4     16     {624/625, 1}                    <= 1/16
5     32     {63/125, 624/625}               <= 39/1250
6     64     {1/625, 1}                      <= 1/64
```

The upper bound uses the fact that roofs occupy one floor in `2^r` and takes
the worst conditional carrier defect; it invents no uniform context weights.
This decreasing bound is deliberately not treated as evidence: any finite
cocycle admits tower fills that are exact off the roofs.

The exact refinement map between levels is also implemented. On the tested
transitions the lexicographic matching has conditional disagreement fractions
as large as `1` (and at least `624/625` throughout `r = 2..6`). These adjacent
mismatches remain macroscopic, but a finite list of unweighted conditional
comparisons is neither a proof nor a disproof of Cauchy convergence for an
optimized sequence of boundary maps.

## Growing-context weighted optimizer

The next layer uses anchored two-sided collars rather than adding future bits
only. A collar `[-L,+R]` records a genuine cylinder around the desubstituted
current letter. For a parent sequence `x`, its two substitution children obey

```text
z_(2i)   = x_i,
z_(2i+1) = 1 - x_i.
```

Refinement therefore retains one joint extension atom

```text
parent + common extension -> (child_0, child_1)
```

with exact weight `mu(extension)` and branch weights `mu(extension)/2`. The
two phases are not separately invariant; their half-mixture is. The incidence
implementation checks parent marginals, mixed child marginals, overlap,
complement symmetry, and direct reconstruction of both child words.

A boundary bijection is stored without expanding `3125!` possibilities:

```text
625 source five-blocks -> 625 target pentagons,
one internal S_5 permutation on every matched block.
```

The 625th source block consists of the five `J^(2^r)` fixed points, so the
optimizer does not force it into the target singlet. This structured ansatz is
closed under every exact block `advance` and `retreat` operation.

For adjacent levels, the exact invariant distance is

```text
D_r = sum_e mu(e)/2 * (
          d(X_(r+1,parent), X_(r,child_0))
        + d(advance_r(X_(r+1,parent)), X_(r,child_1))) .
```

No additional `1/2^r` appears: the boundary Hamming distance is preserved on
all floors of a common child tower. For one variable with all neighbors fixed,
the code enumerates the internal `S_5` choices and solves the remaining sparse
maximum-weight block/cell matching exactly. A forward/backward sweep therefore
never increases the rational objective. The full finite-horizon problem is
still discrete and nonconvex. In the primary runs level 2 is a fixed boundary,
so convergence gives only a coordinate optimum conditional on that declared
seed, not a local optimum of the unrestricted horizon and not a global
certificate. A separate all-levels-free mode diagnoses this boundary choice.

The exact weighted readback of the old lexicographic pair-collar baseline is

```text
D_2 = 209/1250
D_3 = 1/2
D_4 = 937/1875
D_5 = 521/1250
D_6 = 209/1250
```

The first growing schedule alternates the added side:

```text
r=2 [-1,+0], r=3 [-1,+1], r=4 [-2,+1], ... , r=8 [-4,+3].
```

For horizon `r=2..5`, four deterministic initializations were swept while
holding level 2 fixed. Their conditional coordinate-optimum objectives were

```text
lexicographic / child 0: 1313/1500
lexicographic / child 1: 5/6
tree seed     / child 0: 3751/5000
tree seed     / child 1: 10631/15000   (best of these four)
```

The best anchored run decomposes as

```text
D_2 = 157/1875
D_3 = 5629/15000
D_4 = 1873/7500
```

An extended anchored `r=2..8` tree/child-1 run reached `23131/15000`, with

```text
(D_2,...,D_7) =
(157/1875, 6253/15000, 437/1500,
 3751/15000, 3751/15000, 1/4).
```

Allowing level 2 to move from the same tree/child-1 seeds lowers the `2..5`
objective to `10627/15000` and the `2..8` objective to `7709/5000`. These are
all-levels-free coordinate optima, included only as a sensitivity diagnostic;
they do not turn the anchored runs into unrestricted optima.

Thus growing context and exact weighting are operational, and local sweeps do
improve their declared finite objectives. They do not yet expose a summable
Cauchy tail: the last three distances in this run remain approximately `1/4`.
Some individual child-branch terms vanish, but none of the reported total
adjacent distances does. The outer cell matching also stayed in a narrow
basis: the largest positive matching component was only 2 (and only 1 in the
best and extended runs). The default collar schedule happened to give a unique
child pair per parent, so its executed runs did not exercise the separately
tested ambiguous-incidence path. This is a result about four related seeds and
their coordinate sweeps, not a lower bound for all structured families and not
a global entropy no-go.

## Small-horizon lower bounds and separated initializations

The fixed-`r=2` tree-boundary problem now has replayable global lower bounds
inside the declared structured `625`-block/`S_5` finite-horizon ansatz. The
certificate has two disjoint parts:

1. the exact minimum `209/2500` of the first anchored refinement distance;
2. holonomy-cycle inequalities on all later edges, after dropping the
   all-different coupling between source blocks. Horizon `2..4` uses a
   fractional packing of every positive-defect simple cycle; horizon `2..5`
   retains the smaller edge-disjoint fundamental-cycle certificate.

For one cycle, exact block transport and the triangle inequality give

```text
sum_e w_e d_e >= min_e(w_e) d(x,H_C(x)).
```

The holonomy defect is minimized over all `625 * 120` cell/`S_5` labels for
one ordinary source block and again for the special block. Ordinary source
blocks have identical position action, so the full relaxed contribution is
the exact sum of `624` ordinary coordinates and one special coordinate. The
checker reconstructs every edge, transport, witness, weight, minimum, and
packing-capacity condition.

For horizon `2..4`, the later-edge graph has exactly 20 simple cycles: four
length-four cycles with zero defect and sixteen length-twelve cycles with
ordinary/special minimum mismatches `(0,5)`. Assigning exact weight `1/192`
to each of the sixteen positive cycles saturates every edge at its objective
weight. This replayable fractional packing improves the cycle contribution
from `1/15000` to `1/7500`; no linear-programming solver is trusted by the
checker.

The resulting exact comparisons are

```text
horizon  certified lower bound  feasible incumbent  gap
2..4     157/1875               626/1875            469/1875
2..5     313/2500               10631/15000          8753/15000
```

For `2..4`, all sixteen allocated cycles contribute only through the special
block while their ordinary minimum is zero. For `2..5`, the selected
fundamental cycle contributes `26/625`: every ordinary block has five
mismatches while the special minimum is zero. Both bounds are global for the
named fixed-boundary finite problem, but neither meets the incumbent. The
larger horizon still uses only the deterministic fundamental basis, not all
simple cycles or a fractional packing.

The initialization experiment was also tightened. Every run keeps exactly the
same frozen `r=2` tree family and changes only the free maps. Four deterministic
context/level patterns rotate all 625 block assignments in 125 cycles of
length 5. At every free context the patterns are pairwise at Hamming distance
1 from one another and from the common lift for each fixed lift phase, and no
single global block permutation explains a whole seeded family.

With both lift phases, the `2..5` grid contains eight runs. All stop within
three sweeps and produce eight distinct final free-map signatures, eight
internal diagnostic signatures, and eight exact objectives. The diagnostic
hashes encode exact distance and roof-defect tuples; they are neither physical
observables nor a quotient by the full cocycle centralizer.

```text
context0/phase0  1477/1500      context0/phase1  7199/7500
context1/phase0  70123/75000    context1/phase1  574/625
context2/phase0  1954/1875      context2/phase1  1799/1875
context3/phase0  1877/1875      context3/phase1  3443/3750
```

The best distant terminal point is `3443/3750`, still above the reference
incumbent `10631/15000`. All eight `2..5` profiles retain positive adjacent
distances. The tail beyond level 5 remains tested only in the reference `2..8`
run, so this grid carries no asymptotic or Cauchy conclusion and is not a basin
classification. Large sparse cell-assignment components now have an exact
polynomial min-cost matching fallback; the small bitmask solver is retained as
an independently checked path.

## Next exact local tests

1. Emit short closed-walk obstruction certificates for the empty affine and
   singlet equations, so the finite-context no-go is auditable without solver
   internals.
2. Add tie-neutral moves and additional deterministic seeds, then reproduce
   whether the same small-horizon fixed points recur.
3. Extend the successful all-simple-cycle fractional packing from horizon
   `2..4` to anchor-to-anchor path duals and coupled block duals. The current
   bounds do not certify either incumbent.
4. Use branch-and-bound or an exact dual certificate on `2..4` before extending
   both collar radii and the horizon. Then search for a chain whose
   refinement disagreements are summable. A surviving chain is only a
   measurable-transfer candidate; a positive uniform lower bound closes only
   the declared cell-sector ansatz.
5. If a compatible chain survives, count its orbits separately under the
   2500-element arithmetic subgroup and the full permutation centralizer.
   Existence does not establish canonicity.
6. Only after existence and canonicity, prove the regularity class and derive
   the pushforward of Haar measure. Do not infer the measure clause from the
   cardinality match alone.

## Stop conditions for the recon

- A failed truncated compatibility equation closes only the named transfer
  ansatz, not `ENTROPY-LAYER-BRIDGE` globally.
- Two inequivalent compatible inverse systems are a candidate negative result
  for canonicity.
- Dependence on an unregistered gauge, private data, or a post-hoc cell
  orientation stops the construction.
- A measure mismatch is retained even if an equivariant bijection exists.
- No public issue or preregistration should be created until the local work
  yields a stable decision surface with an honest scope ceiling.

## Reproduction

From the repository root:

```text
python -m unittest discover -s notes/entropy_selection -p "test_*.py" -v
python -m notes.entropy_selection.run_solver
python -m notes.entropy_selection.run_growing
python -m notes.entropy_selection.run_landscape
```

The package uses the Python standard library and writes no evidence artifact.
Its output begins with `NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS`.
