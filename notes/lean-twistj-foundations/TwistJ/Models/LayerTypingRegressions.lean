import TwistJ.Dictionary.SpaceReading
import TwistJ.Models.ReadoutRegressions

/-!
# State, orbit, and declared-space typing regressions

Status: **NON-CANONICAL NOTE**.

These examples freeze the named state-to-orbit sampling seam, show that two
indices of one orbit can expose different states, and prevent a declared
`SpaceReading` from silently acquiring a defined spatial output, separation,
or physical content.
-/

set_option autoImplicit false

namespace TwistJ.Models

open TwistJ.Dictionary
open TwistJ.Foundation
open TwistJ.Observation

/-- Read one state of the successor system without changing its payload. -/
def successorStateReadout : StateReading successorSystem where
  Output := ℕ
  read := fun n => some n

/-- The orbit readout is obtained only through the named sampling function. -/
def sampledInitialOrbitReadout : OrbitPartialReadout successorSystem :=
  successorStateReadout.atOrbitIndex 0

@[simp]
theorem sampledInitialOrbitReadout_read (n : ℕ) :
    sampledInitialOrbitReadout.read (successorOrbit n) = some n := by
  rfl

@[simp]
theorem successorStateReadout_at_zero (n : ℕ) :
    (successorStateReadout.atOrbitIndex 0).read (successorOrbit n) = some n := by
  rfl

@[simp]
theorem successorStateReadout_at_one (n : ℕ) :
    (successorStateReadout.atOrbitIndex 1).read (successorOrbit n) =
      some (n + 1) := by
  simp [successorStateReadout, successorOrbit, StateReading.atOrbitIndex,
    ForwardOrbit.stateAt, AutonomousSystem.evolve, successorSystem]

/-- One orbit can yield different state samples at different indices. -/
theorem same_orbit_different_state_samples :
    (successorStateReadout.atOrbitIndex 0).read (successorOrbit 0) ≠
      (successorStateReadout.atOrbitIndex 1).read (successorOrbit 0) := by
  rw [successorStateReadout_at_zero, successorStateReadout_at_one]
  intro hread
  have hzeroOne : (0 : ℕ) = 1 := Option.some.inj hread
  exact Nat.zero_ne_one hzeroOne

/-- A nominal spatial declaration may have no possible defined output. -/
def emptyOutputSpaceReading : SpaceReading successorSystem where
  Output := Empty
  read := fun _ => none

@[simp]
theorem emptyOutputSpaceReading_undefined
    (κ : ForwardOrbit successorSystem) :
    emptyOutputSpaceReading.read κ = none :=
  rfl

/-- A declared spatial reading can also be defined but nonseparating. -/
def constantBoolSpaceReading : SpaceReading successorSystem where
  Output := Bool
  read := fun _ => some true

/-- Declaring the reading spatial does not make it reconstruct orbit inputs. -/
theorem constantSpaceReading_equates_distinct_orbits :
    (constantBoolSpaceReading.toOrbitReading.toFamily).ObservationallyEquivalent
        (successorOrbit 1) (successorOrbit 2) ∧
      successorOrbit 1 ≠ successorOrbit 2 := by
  constructor
  · intro i
    cases i
    rfl
  · exact successorOrbit_one_ne_two

/-- A partial spatial declaration used to freeze the explicit projection. -/
def zeroFlagSpaceReading : SpaceReading successorSystem where
  Output := Bool
  read := fun κ =>
    if successorInitial κ = 0 then some true else none

@[simp]
theorem zeroFlagSpaceReading_zero :
    zeroFlagSpaceReading.read (successorOrbit 0) = some true := by
  rfl

@[simp]
theorem zeroFlagSpaceReading_nonzero {n : ℕ} (hn : n ≠ 0) :
    zeroFlagSpaceReading.read (successorOrbit n) = none := by
  simp [zeroFlagSpaceReading, hn]

/-- Explicit forgetting preserves both defined and undefined outcomes. -/
theorem spaceProjection_preserves_option_boundary :
    zeroFlagSpaceReading.toOrbitReading.read (successorOrbit 0) =
        some true ∧
      zeroFlagSpaceReading.toOrbitReading.read (successorOrbit 1) =
        none := by
  constructor
  · change zeroFlagSpaceReading.read (successorOrbit 0) = some true
    exact zeroFlagSpaceReading_zero
  · change zeroFlagSpaceReading.read (successorOrbit 1) = none
    exact zeroFlagSpaceReading_nonzero (by decide)

end TwistJ.Models
