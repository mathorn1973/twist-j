# Mathlib environment map

Status: **NON-CANONICAL ENVIRONMENT INVENTORY ONLY**.

This file records the exact manual-development environment and maps selected
upstream API names needed by the frozen selection contract. It proves no
`MinimalCM` theorem, creates no public evidence, and is not an `A-LEAN-*`
package.

## Immutable inputs

```text
lean_toolchain:       leanprover/lean4:v4.30.0
lean_commit:          d024af099ca4bf2c86f649261ebf59565dc8c622
lake_version:         5.0.0-src+d024af0
mathlib_remote:       https://github.com/leanprover-community/mathlib4.git
mathlib_commit:       c5ea00351c28e24afc9f0f84379aa41082b1188f
manifest_format:      1.2.0
manifest_sha256:      f39024c57bf76c4d3a7a5691164cb267c679dc51ed2d3d08cdd8655f8fa8f5e7
manifest_bytes:       3170
manual_platform:      Ubuntu 24.04.3 LTS
manual_architecture:  x86_64
```

The full Mathlib commit appears both in `lakefile.lean` and as the `mathlib`
package `rev` and `inputRev` in `lake-manifest.json`. The manifest is generated
by Lake for this project; it is not copied from upstream Mathlib.

## Locked package graph

Every `rev` below is a full 40-hex commit recorded in `lake-manifest.json` and
verified against the corresponding local checkout.

| Package | Commit |
|---|---|
| mathlib | `c5ea00351c28e24afc9f0f84379aa41082b1188f` |
| plausible | `a456461b368b71d2accd95234832cd9c174b5437` |
| LeanSearchClient | `c5d5b8fe6e5158def25cd28eb94e4141ad97c843` |
| importGraph | `515cf9d0c00ece5e661f6de4326a53dedc1e8ea1` |
| proofwidgets | `a84b3e2475d5c5ab979567b1ad8aea21b764bcf8` |
| aesop | `558915ae105bfd8074e22d597613d1961822adc2` |
| Qq | `a6e6c34c4ef182f83b219a3a5a385f51f44bdc4c` |
| batteries | `32dc18cde3684679f3c003de608743b57498c56f` |
| Cli | `6b907cf12b2e445ccb7c24bc208ef04a1f39e84c` |

## API inventory

`Audit.lean` checks that these names elaborate at the pinned commit. Presence
of an API name is not a proof of any project theorem.

| Contract block | Direct import | Upstream anchors | Environment finding |
|---|---|---|---|
| Abelianization | `Mathlib.GroupTheory.Abelianization.Defs` | `Abelianization`, `.of`, `.lift`, `.lift_of_comp` | Universal-property API is present; the Hom-to-`C₂` equivalence remains a project lemma. |
| Square-root floor | `Mathlib.Algebra.Module.ZMod`, `Mathlib.LinearAlgebra.Dual.Lemmas`, `Mathlib.GroupTheory.OrderOfElement` | `nsmulAddMonoidHom`, `QuotientAddGroup.zmodModule`, `Module.forall_dual_apply_eq_zero_iff`, `addOrderOf` | The quotient-dual route is available; the quarter-turn theorem is not claimed here. |
| Finite bit classification | `Mathlib.GroupTheory.Sylow` | `Sylow`, `Sylow.card_eq_multiplicity` | Sylow primitives are present; the unique-bit classification remains a project theorem. |
| CM conjugation | `Mathlib.NumberTheory.NumberField.CMField` | `NumberField.IsCMField`, `.complexConj`, `.orderOf_complexConj` | Complex conjugation is available in `Gal(K/K⁺)`; transport to `Gal(K/ℚ)` must be constructed and audited. |
| Units | `Mathlib.NumberTheory.NumberField.Units.DirichletTheorem` | `NumberField.Units.rank`, `.rank_modTorsion` | Dirichlet-unit primitives are present; the CM degree-to-rank formula still needs assembly. |
| Minkowski | `Mathlib.NumberTheory.NumberField.Discriminant.Basic` | `NumberField.discr`, `.abs_discr_ge_of_isTotallyComplex` | The required totally-complex lower-bound theorem is present. |
| Cyclotomic witness | `Mathlib.NumberTheory.Cyclotomic.Gal`, `Mathlib.NumberTheory.Cyclotomic.Discriminant`, `Mathlib.NumberTheory.NumberField.CMField` | `IsCyclotomicExtension.autEquivPow`, `.discr_odd_prime`, `.Rat.isCMField` | The cyclotomic primitives are present; `discr_odd_prime` computes a power-basis discriminant, not automatically `NumberField.discr`. |
| Dirichlet primitives | `Mathlib.NumberTheory.DirichletCharacter.Basic` | `.conductor`, `.IsPrimitive`, `.primitiveCharacter`, `.Even`, `.Odd`, `.conductor_inv` | Conductor and parity primitives are present. |

## Open hard gaps

The pinned source contains no located direct declaration closing either block
below. These remain explicit mathematical dependencies, not library facts.

1. **G1:** an arbitrary cyclic quartic abelian field over `ℚ` corresponds to a
   primitive Dirichlet character of exact order four whose induced Galois
   character is faithful.
2. **G2:** the conductor-discriminant formula
   `absDisc(K) = f(ψ)^2 * f(ψ^2)` for that field.

No local axiom, hidden instance, unnamed assumption, or cyclotomic special-case
proxy may be used to fill either gap. G3 and G4 also remain project theorems.

## Manual environment verification

On the neutral platform recorded above:

- the first `lake update` completed with exit 0 and downloaded/decompressed
  all 8459 Mathlib cache objects;
- a second invocation left `lake-manifest.json` byte-identical at the recorded
  SHA-256 and byte count;
- `lake env lean --version` reported Lean 4.30.0 at commit `d024af0...`;
- `lake build TwistJLeanNote` completed with exit 0; and
- `lake env lean Audit.lean` completed with exit 0.

No stdout from these manual checks is retained in the repository. These facts
describe environment validation only and are not a reproduction or an
evidence record.

## Manual checks

From this directory in a Linux-compatible environment:

```bash
lake update
lake env lean --version
lake build TwistJLeanNote
lake env lean Audit.lean
```

The successful environment inventory means only that the pinned dependency
graph resolves, the existing symbolic note builds, and the listed upstream
names elaborate. Do not save its stdout as `EXPECTED.txt`, `RUN.md`,
`RESULT.md`, or `AXIOMS.txt`. A future public Lean audit must be a new,
separately claimed and pinned `A-LEAN-*` package after the exact theorem scope
has already been released at `T` or `T-LOCK` through primary evidence.
