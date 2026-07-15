# Entropy selection recon

Status: **NON-CANONICAL LOCAL ANALYSIS**

This note starts the successor analysis to the finite entropy bridge and
mirror work. It is not a preregistration, verifier record, or evidence bundle.
No target below is frozen and no claim status is earned.

## Public inputs

The analysis uses only public finite facts. The mirror result is public probe
evidence merged by PR #37; it has not yet been folded into the Canon registry:

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
For this local recon the finite language is obtained by a stabilized
substitution census with additional look-ahead. A future public verifier must
replace that development check by a bounded substitution-closure certificate
or an equivalent automaton proof.

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

Executed grid: levels `r = 2..6`, context widths `w = 2..8`. Within that
stabilized factor census, every one of the 35 decisions returned the same
layered result:

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

## Next exact local tests

1. Emit short closed-walk obstruction certificates for the empty affine and
   singlet equations, so the finite-context no-go is auditable without solver
   internals.
2. Replace the lexicographic boundary matching by an optimizer on the exact
   tower refinement graph. Context collars must grow; a fixed pair context
   cannot represent an arbitrary measurable transfer.
3. Compute exact invariant frequencies of the allowed cylinders and minimize
   the genuine cross-level distance, not an unweighted context average.
4. Search for a chain whose refinement disagreements are summable. A surviving
   chain is only a measurable-transfer candidate; a positive uniform lower
   bound closes only the declared cell-sector ansatz.
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
```

The package uses the Python standard library and writes no evidence artifact.
Its output begins with `NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS`.
