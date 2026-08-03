import TwistJ.Architecture.UpdateShape
import TwistJ.Foundation.Orbit
import TwistJ.Observation.ObservationalEquivalence

/-!
# Orbit-valued observation inputs

Status: **NON-CANONICAL NOTE**.

These aliases make the intended input type explicit: a readout receives a
named forward orbit, not an individual state. `ForwardOrbit` is still the
pointed representation from the foundation cut; no quotient or identification
with the Canon orbit set `K` is asserted here.
-/

set_option autoImplicit false

namespace TwistJ.Observation

open TwistJ.Architecture
open TwistJ.Foundation

universe u v w

/-- A partial readout whose input is a named forward orbit. -/
abbrev OrbitPartialReadout (S : AutonomousSystem.{u}) :=
  PartialReadout (ForwardOrbit S)

/-- A heterogeneous readout family whose input is a named forward orbit. -/
abbrev OrbitReadoutFamily (S : AutonomousSystem.{u}) :=
  ReadoutFamily (ForwardOrbit S)

/-- The named forward-orbit input for the Public Canon v32 update shape. -/
abbrev PublicCanonV32ForwardOrbit
    (updateCheckpoint : N0 → PublicCheckpoint → PublicCheckpoint) :=
  ForwardOrbit (publicCanonV32System updateCheckpoint).autonomousSystem

/-- A partial readout on the exact v32-shaped orbit input carrier. -/
abbrev PublicCanonV32PartialReadout
    (updateCheckpoint : N0 → PublicCheckpoint → PublicCheckpoint) :=
  PartialReadout (PublicCanonV32ForwardOrbit updateCheckpoint)

/-- A heterogeneous readout family on the v32-shaped orbit input carrier. -/
abbrev PublicCanonV32ReadoutFamily
    (updateCheckpoint : N0 → PublicCheckpoint → PublicCheckpoint) :=
  ReadoutFamily (PublicCanonV32ForwardOrbit updateCheckpoint)

end TwistJ.Observation
