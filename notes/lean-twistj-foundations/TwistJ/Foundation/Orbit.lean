import TwistJ.Foundation.AutonomousSystem

/-!
# Forward orbits

Status: **NON-CANONICAL NOTE**.

An orbit is named by its initial complete state. Its points are derived by
iterating the one-step update. A future readout layer can therefore accept a
`ForwardOrbit S` without pretending that it reads a single state.
-/

set_option autoImplicit false

namespace TwistJ.Foundation

universe u

/-- A named forward orbit of an autonomous system. -/
structure ForwardOrbit (S : AutonomousSystem.{u}) where
  initial : S.State

namespace ForwardOrbit

/-- The state at metatheoretic iteration index `k`. -/
def stateAt {S : AutonomousSystem.{u}} (κ : ForwardOrbit S) (k : ℕ) : S.State :=
  S.evolve k κ.initial

@[simp]
theorem stateAt_zero {S : AutonomousSystem.{u}} (κ : ForwardOrbit S) :
    κ.stateAt 0 = κ.initial :=
  rfl

theorem stateAt_succ {S : AutonomousSystem.{u}} (κ : ForwardOrbit S) (k : ℕ) :
    κ.stateAt k.succ = S.step (κ.stateAt k) := by
  simp [stateAt]

end ForwardOrbit

end TwistJ.Foundation
