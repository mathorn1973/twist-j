# Entropy-selection local solver package

Status: **NON-CANONICAL LOCAL ANALYSIS**

This package is a local construction and falsification surface for the open
entropy selection problem. It does not modify the Canon, run a formal probe,
or create evidence authority.

Modules:

- `lambda5.py`: exact `O/lambda^5` ring, `J` action, orbits, and distinct
  arithmetic/full permutation centralizers;
- `living.py`: exact `(component,half,cell,xi)` reconstruction of the merged
  public living kernel;
- `morse.py`: actual finite Thue--Morse language, Rauzy context graphs, and
  exact substitution-tower refinement;
- `block_solver.py`: cell-section, affine `F_5`, and unrestricted `S_5`
  coboundary solvers on finite desubstituted contexts;
- `tower.py`: an explicit lexicographic bijective Rokhlin-tower baseline, roof
  defects, and cross-level refinement diagnostics;
- `test_lambda5.py`, `test_solver.py`: focused exact gates;
- `run_solver.py`: complete human-readable local report.

Run from the repository root:

```text
python -m unittest discover -s notes/entropy_selection -p "test_*.py" -v
python -m notes.entropy_selection.run_solver
```

An `EMPTY` result belongs only to the finite-context cell-sector ansatz named
by the report. A shrinking tower-roof error is not a measurable construction
without a Cauchy-compatible sequence of refinements.
