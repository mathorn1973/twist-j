import TwistJ.Foundation.Orbit
import TwistJ.Observation.PartialReadout

/-!
# Explicit state and orbit reading inputs

Status: **NON-CANONICAL NOTE**.

`StateReading` is a negative-control type for a partial read of one
state. The public decoder is not modeled by that type: its declared input is
a forward orbit. This module supplies one named state-to-orbit sampler,
`atOrbitIndex`, and installs no implicit conversion.

These are typing strata, not the Canon action layers L1--L6. The sampling
index is metatheoretic and is not an input to the autonomous update.
-/

set_option autoImplicit false

namespace TwistJ.Observation

open TwistJ.Foundation

universe u v

/-- A typed partial readout whose input is one state of `S`.

This is a generic negative-control object, not the public orbit decoder.
-/
abbrev StateReading (S : AutonomousSystem.{u}) :=
  PartialReadout.{u, v} S.State

/-- A typed partial readout whose input is a named forward orbit. -/
abbrev OrbitReading (S : AutonomousSystem.{u}) :=
  PartialReadout.{u, v} (ForwardOrbit S)

namespace StateReading

/-- Explicitly sample a state readout at one metatheoretic orbit index. -/
def atOrbitIndex {S : AutonomousSystem.{u}}
    (R : StateReading.{u, v} S) (k : ℕ) : OrbitReading.{u, v} S where
  Output := R.Output
  read := fun κ => R.read (κ.stateAt k)

@[simp]
theorem atOrbitIndex_read {S : AutonomousSystem.{u}}
    (R : StateReading.{u, v} S) (k : ℕ) (κ : ForwardOrbit S) :
    (R.atOrbitIndex k).read κ = R.read (κ.stateAt k) :=
  rfl

end StateReading

end TwistJ.Observation
