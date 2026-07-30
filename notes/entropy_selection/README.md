# Entropy-selection local solver package

Status: **NON-CANONICAL LOCAL ANALYSIS**

This package is a local construction and falsification surface for the open
entropy selection problem. It does not modify the Canon, run a formal probe,
or create evidence authority.

## Current control documents

- `RECON-V28-STATUS.md`: current Public Canon v28 basis, exact finite state,
  corrections binding successor work, and the live work list. It supersedes
  the stale authority sentence and final task-list reading of
  `../ENTROPY-SELECTION-RECON.md`.
- `PREREG-C-ENTROPY-MACKEY-OBSTRUCTION-4-N.md`: frozen non-canonical
  preregistration for the next attack. It states `r >= 2`, treats the target as
  312 separate regular `D_5` torsors plus `D_5/C_2`, and makes uniform
  pushforward conditional on the proved Haar quotient lemma and fiberwise
  bijectivity. No `mackey4` code existed or ran at the freeze commit.
- `ENTROPY-DICHOTOMY.md`: exact fixed-`F_2`, fixed-`r=2` prefix-tree
  dichotomy, finite optima through `2..7`, and the falsified transition-local
  kill shot.
- `HORIZON7_EXACT.md`: exact horizon `2..7` closure record.

Modules:

- `lambda5.py`: exact `O/lambda^5` ring, `J` action, orbits, and distinct
  arithmetic/full permutation centralizers;
- `living.py`: exact `(component,half,cell,xi)` reconstruction of the merged
  public living kernel;
- `morse.py`: actual finite Thue--Morse language, Rauzy context graphs, and
  exact substitution-tower refinement;
- `measure.py`: finite substitution-closure certificates and exact rational
  cylinder frequencies;
- `collars.py`: two-sided anchored collars and joint weighted two-child
  refinement incidence;
- `block_solver.py`: cell-section, affine `F_5`, and unrestricted `S_5`
  coboundary solvers on finite desubstituted contexts;
- `tower.py`: an explicit lexicographic bijective Rokhlin-tower baseline, roof
  defects, and cross-level refinement diagnostics;
- `growing.py`: structured boundary maps, exact adjacent-level distances,
  maximum-weight tree families, anchored finite-horizon coordinate
  optimization, and an all-levels-free sensitivity mode;
- `bounds.py`: replayable fixed-anchor lower-bound certificates from exact
  first-layer minima, a fractional packing of every positive-defect simple
  cycle at horizon `2..4`, and edge-disjoint fundamental holonomy cycles at
  horizon `2..5`;
- `path_bounds.py`: a standalone blockwise anchor-to-anchor path certificate
  for horizon `2..4`, with ten explicit paths, exact per-block edge loads, and
  a matching catalog dual within the blockwise relaxation for all 622 simple
  terminal paths plus 20 simple cycles;
- `coupled_exact.py`: the zero-assignment-price lift of that block dual,
  a coupled structured witness attaining every block minimum, and a replayed
  conflict-core branch-and-bound on the five special-block coordinates;
- `horizon5_ordinary.py`: the full-domain ordinary-block point bundle, its
  equivariant `3125 -> 5` retraction, and the conditioned standard-library
  min-sum elimination proving the scaled minimum `70`;
- `coupled_horizon5.py`: the matching special-block retraction and five exact
  coordinate DPs, the structured `{70:624, 90:1}` witness, and the zero-price
  coupled closure at `1459/2500` for horizon `2..5`;
- `horizon6_prep.py`: the scale-48 correction, graph/retraction preparation,
  and independent exact special-block closure at scaled cost `220`;
- `horizon6_ordinary.py`: the full 220-variable ordinary point bundle,
  equivariant retraction, exact integer local-polytope dual of value `190`,
  matching assignment, and all-624 structured reassembly; its two small JSON
  files are the pinned dual and assignment certificates;
- `coupled_horizon6.py`: the structured `{190:624, 220:1}` witness and the
  zero-price coupled closure at `5939/7500` for horizon `2..6`;
- `horizon7_prep.py`: exact horizon-7 graph and special-block preparation at
  scaled cost `260`;
- `horizon7_ordinary.py`: the 320-variable ordinary bundle, exact data-only
  branch-and-bound and Hall-infeasibility replay, and the matching cost-`220`
  structured witness across all 624 ordinary fibres;
- `coupled_horizon7.py`: the full `{220:624,260:1}` coupled witness and exact
  closure at `6877/7500`;
- `basins.py`: context-dependent, separated free-map initializations for one
  frozen boundary problem and each fixed lift phase;
- `test_*.py`: focused exact gates;
- `run_solver.py`: complete human-readable local report;
- `run_growing.py`: bounded growing-context and finite-horizon report;
- `run_landscape.py`: certified small-horizon bounds and initialization grid.

Run from the repository root with CPython 3.10 or newer and without `-O`:

```text
python -m unittest discover -s notes/entropy_selection -p "test_*.py" -v
python -m notes.entropy_selection.run_solver
python -m notes.entropy_selection.run_growing
python -m notes.entropy_selection.run_landscape
python -m notes.entropy_selection.path_bounds
python -m notes.entropy_selection.coupled_exact
python -m notes.entropy_selection.coupled_horizon5
python -m notes.entropy_selection.horizon6_prep
python -m notes.entropy_selection.horizon6_ordinary
python -m notes.entropy_selection.coupled_horizon6
python -m notes.entropy_selection.horizon7_prep
python -m notes.entropy_selection.horizon7_ordinary
python -m notes.entropy_selection.coupled_horizon7
```

An `EMPTY` result belongs only to the finite-context cell-sector ansatz named
by the report. A shrinking tower-roof error is not a measurable construction
without a Cauchy-compatible sequence of refinements.
