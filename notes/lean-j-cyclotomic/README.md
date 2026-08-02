# Lean laboratory: cyclotomic quartic and minimal CM selection

Status: **NON-CANONICAL NOTE**.

This directory is an exploratory manual laboratory under `notes/`. It does not
modify the Canon, registry, frontier, evidence ledger, or any claim status or
scope. It is not a formal probe, a minimal public reproduction, or registry
evidence, and it must not be cited as earned public evidence.

It contains four deliberately separate surfaces:

1. `SELECTION-CONTRACT.md` specifies a proposed minimal-abelian-CM theorem,
   its selection assumptions, regressions, dependency graph, and the firewall
   between arithmetic claims and physical interpretation. It is a frozen
   design contract only.
2. `TwistJLeanNote.lean` is the pre-existing symbolic quartic experiment
   described below. It is not a premise of the selection theorem.
3. `TwistJ/MinimalCM/CMConjugationBit.lean` proves the first abstract group
   floor: a nonzero involution killed by every additive character to `ZMod 2`
   has a square root of additive order four. It is a manual theorem in this
   non-canonical laboratory, not public evidence.
4. `MATHLIB-MAP.md`, `lake-manifest.json`, and `Audit.lean` form a pinned
   environment and axiom inventory. They check dependency resolution,
   upstream names, and the printed logical footprint of the new theorem.

The dependency environment was pinned before any new `MinimalCM` source.
Later theorem commits must preserve that separation and may not reinterpret
the environment inventory as evidence.

## First minimal-CM group floor

For an additive commutative group `G`, the new module proves exactly:

```text
c ≠ 0,  2 • c = 0,  (∀ χ : G →+ ZMod 2, χ c = 0)
  ⇒ ∃ τ, addOrderOf τ = 4 ∧ 2 • τ = c.
```

Finiteness and uniqueness of the quadratic bit are deliberately absent from
this lemma. The finite unique-bit/Sylow classification, CM interpretation,
unit rank, discriminant bounds, `ℚ(ζ₅)` witness and minimality, conductor
gate, and any conclusion about `J` remain unproved here.

The abstract element `τ` is not the semilinear operator `ν`, a spinor lift, or
an operator from `P-CENTRAL-LIFT-PHASE-1` or `P-CM-2I-QCARRIER-1`. Those public
objects have separate carriers, hypotheses, and evidence.

## Existing symbolic experiment

In an arbitrary commutative ring, assume that `ζ` satisfies the fifth
cyclotomic relation

```text
ζ^4 + ζ^3 + ζ^2 + ζ + 1 = 0.
```

The Lean source derives:

1. `ζ^5 = 1`;
2. `ζ^2` satisfies the same fifth cyclotomic relation; and
3. for `J = 1 + ζ^2`,

   ```text
   J^4 - 3 J^3 + 4 J^2 - 2 J + 1 = 0.
   ```

The proof is symbolic. It uses no floating-point calculation, finite search,
division, or physical interpretation. It does not assert that the displayed
quartic is minimal in every commutative ring; it proves only the stated
annihilating relation.

## Deliberate boundary

This laboratory has no repository workflow and no automatic gate. Repository
CI does not build this Lean project. A successful manual build is an optional
review aid only and creates no scientific or procedural status. Admitting a
selected Lean theorem as public audit evidence requires a separate policy
change with explicit scope, provenance, dependency, and failure rules; it does
not turn this notes tree into a primary canonical pipeline.

## Optional local build

```bash
cd notes/lean-j-cyclotomic
lake update
lake env lean --version
lake build TwistJLeanNote
lake build TwistJ
lake env lean Audit.lean
```

The lock names Lean `4.30.0`, Mathlib commit
`c5ea00351c28e24afc9f0f84379aa41082b1188f`, and full commit SHAs for every
transitive Lake package. `.lake/` remains ignored; `lake-manifest.json` is
committed. See `MATHLIB-MAP.md` for the exact inventory, known API gaps, and
the evidence firewall.
