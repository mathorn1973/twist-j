import Mathlib.Data.Option.Basic

/-!
# Typed partial readouts

Status: **NON-CANONICAL NOTE**.

A partial readout is an ordinary explicit structure. `Option` keeps an
undefined read distinct from every defined output value. This definition does
not assert totality, uniqueness, completeness, or a physical interpretation.
-/

set_option autoImplicit false

namespace TwistJ.Observation

universe u v

/-- A typed partial observation of values in `Input`. -/
structure PartialReadout (Input : Type u) where
  Output : Type v
  read : Input → Option Output

namespace PartialReadout

/-- The readout returns a defined value at this input. -/
def IsDefinedAt {Input : Type u} (R : PartialReadout.{u, v} Input)
    (x : Input) : Prop :=
  ∃ output, R.read x = some output

/-- The readout is undefined at this input. -/
def IsUndefinedAt {Input : Type u} (R : PartialReadout.{u, v} Input)
    (x : Input) : Prop :=
  R.read x = none

theorem isDefinedAt_iff {Input : Type u} (R : PartialReadout.{u, v} Input)
    (x : Input) :
    R.IsDefinedAt x ↔ ∃ output, R.read x = some output :=
  Iff.rfl

theorem isUndefinedAt_iff {Input : Type u} (R : PartialReadout.{u, v} Input)
    (x : Input) :
    R.IsUndefinedAt x ↔ R.read x = none :=
  Iff.rfl

/-- Undefined and defined output are mutually exclusive. -/
theorem not_isDefinedAt_of_isUndefinedAt {Input : Type u}
    (R : PartialReadout.{u, v} Input) {x : Input}
    (hundefined : R.IsUndefinedAt x) :
    ¬ R.IsDefinedAt x := by
  rintro ⟨output, houtput⟩
  rw [hundefined] at houtput
  simp at houtput

end PartialReadout

end TwistJ.Observation
