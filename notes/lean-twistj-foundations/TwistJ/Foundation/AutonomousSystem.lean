import Mathlib.Logic.Function.Iterate

/-!
# Autonomous one-step systems

Status: **NON-CANONICAL NOTE**.

The primitive dynamics is the one-step endomap `step : State → State`.
`evolve k` is metatheoretic iteration of that map; `k` is not an input to the
system.
-/

set_option autoImplicit false

namespace TwistJ.Foundation

universe u

/-- A state carrier together with one autonomous update. -/
structure AutonomousSystem where
  State : Type u
  step : State → State

namespace AutonomousSystem

/-- Apply the autonomous one-step update exactly `k` times. -/
def evolve (S : AutonomousSystem) (k : ℕ) : S.State → S.State :=
  S.step^[k]

@[simp]
theorem evolve_zero (S : AutonomousSystem) (x : S.State) :
    S.evolve 0 x = x :=
  rfl

@[simp]
theorem evolve_succ (S : AutonomousSystem) (k : ℕ) (x : S.State) :
    S.evolve k.succ x = S.step (S.evolve k x) := by
  simpa [evolve] using Function.iterate_succ_apply' S.step k x

end AutonomousSystem

end TwistJ.Foundation
