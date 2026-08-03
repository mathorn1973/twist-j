import TwistJ.Observation.LayerTyping

/-!
# Explicitly declared space readings

Status: **NON-CANONICAL NOTE**.

A `SpaceReading` is an ordinary record for an orbit-indexed partial read that
a dictionary has chosen to call spatial. Supplying a value is declaration
data, not a proof that its output is physical space. No instance, coercion,
reverse constructor, or concrete Public Canon reading is installed here.
-/

set_option autoImplicit false

namespace TwistJ.Dictionary

open TwistJ.Foundation
open TwistJ.Observation

universe u v

/-- A nominal dictionary declaration of an orbit-indexed spatial reading. -/
structure SpaceReading (S : AutonomousSystem.{u}) where
  Output : Type v
  read : ForwardOrbit S → Option Output

namespace SpaceReading

/-- Forget the declared spatial role through an explicit named function. -/
def toOrbitReading {S : AutonomousSystem.{u}}
    (R : SpaceReading.{u, v} S) : OrbitReading.{u, v} S where
  Output := R.Output
  read := R.read

@[simp]
theorem toOrbitReading_read {S : AutonomousSystem.{u}}
    (R : SpaceReading.{u, v} S) (κ : ForwardOrbit S) :
    R.toOrbitReading.read κ = R.read κ :=
  rfl

end SpaceReading

end TwistJ.Dictionary
