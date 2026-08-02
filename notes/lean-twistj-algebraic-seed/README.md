# Lean laboratory: integer-native algebraic seed

Status: **NON-CANONICAL MANUAL LABORATORY ONLY**.

This directory is a standalone Lean laboratory for the Public Canon v32
algebraic seed.  It changes no public claim or evidence.  Its purpose is to
separate four things cleanly:

```text
Lean definition of J          term construction
explicit integer carrier      algebra
published TWIST-J adoption     Canon ontology
public architecture U          separate declaration
```

The laboratory defines a four-coordinate integer ring, explicitly fixes its
natural/integer scalar actions and casts, proves its additive-group and
`CommRing` laws, constructs a primitive fifth root `j`, defines
`J = 1 + j^2`, and checks the exact golden and regular-representation
identities listed in `ALGEBRAIC-SEED-CONTRACT.md`.

## Files

- `ALGEBRAIC-SEED-CONTRACT.md` freezes scope, import order, target statements,
  and exclusions.
- `TwistJ/AlgebraicSeed/FifthRootData.lean` contains the general root data and
  the carrier-independent cube law.
- `TwistJ/AlgebraicSeed/IntegralCarrier.lean` constructs the explicit
  rank-four integer ring, proves its ring laws, and proves immediately that
  its named root satisfies the fifth cyclotomic presentation.
- `TwistJ/AlgebraicSeed/JArithmetic.lean` proves the concrete golden bridge,
  the displayed `M_J` action, determinant, and trace.
- `Audit.lean` prints the logical footprint of the selected theorems.

The older `notes/lean-j-cyclotomic/` laboratory is intentionally unchanged.
It has a different selection-theorem contract and is not imported here.  The
counter foundations laboratory is likewise a sibling, not a dependency.

## Manual build

Repository CI does not build this notes project.  From this directory:

```bash
env -u LEAN_PATH lake build
env -u LEAN_PATH lake env lean Audit.lean
```

The pinned environment is:

```text
Lean toolchain   leanprover/lean4:v4.30.0
Lean commit      d024af099ca4bf2c86f649261ebf59565dc8c622
Lake             5.0.0-src+d024af0
Mathlib commit   c5ea00351c28e24afc9f0f84379aa41082b1188f
manifest schema  1.2.0
manifest entries 9, all type git and all at full revisions
manifest bytes   3175
manifest SHA-256 6c7e5e1552fbe44a03eb3218215d8fbc13d655a4b3d0f2ebeed18d24d5645e7e
```

`lake-manifest.json` records every transitive package at a full Git revision.
The ignored `.lake/` directory is generated build state and is not evidence.

The final manual review ran on Ubuntu 24.04.3 LTS under WSL2, x86_64.  The
isolated `lake build` completed successfully with 1584 jobs, and
`lake env lean Audit.lean` exited successfully.  The printed logical footprint
used only Lean/Mathlib foundations `propext`, `Quot.sound`, and, where finite
orders or matrices require it, `Classical.choice`.  It contained no `sorryAx`
and no project axiom.  This metadata is a review note, not a formal run record.

The first clean build may take several minutes because the custom
multiplication associativity proof normalizes four cubic polynomial identities
in twelve integer coordinates.  That cost is intentional: the proof acts as a
falsifier for the multiplication table.  It is not a repository gate or a
reason to weaken the table check.

No `EXPECTED.txt`, `RUN.md`, `RESULT.md`, or saved axiom transcript belongs in
this directory.  A successful manual build is a review aid only; see the
contract for the status firewall and exact public-scope boundary.
