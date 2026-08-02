import Mathlib.Data.ZMod.Basic
import TwistJ.Architecture.UpdateShape

/-!
# Counter regressions

Status: **NON-CANONICAL NOTE**.

These examples prevent the no-return theorem from being overread. A finite
modular counter can return, a checkpoint can recur while the complete state
does not, and a deterministic system need not admit the required natural
counter law.
-/

set_option autoImplicit false

namespace TwistJ.Models

open TwistJ.Foundation
open TwistJ.Architecture

/-- A modular counter carrier, finite when `m` is positive. -/
def modularCounterSystem (m : ℕ) : AutonomousSystem where
  State := ZMod m
  step := fun x => x + 1

/-- Iteration of the modular update is addition by the iteration count. -/
theorem modularCounter_evolve (m k : ℕ) (x : ZMod m) :
    (modularCounterSystem m).evolve k x = x + (k : ZMod m) := by
  induction k with
  | zero => simp
  | succ k ih =>
      rw [AutonomousSystem.evolve_succ, ih]
      simp [modularCounterSystem, Nat.cast_succ, add_assoc]

/-- The modular counter returns after `m` updates. -/
theorem modularCounter_period (m : ℕ) (x : ZMod m) :
    (modularCounterSystem m).evolve m x = x := by
  calc
    (modularCounterSystem m).evolve m x = x + (m : ZMod m) :=
      modularCounter_evolve m m x
    _ = x := by rw [ZMod.natCast_self, add_zero]

/-- The modulus-five instance is explicitly periodic. -/
theorem modularFive_period_five (x : ZMod 5) :
    (modularCounterSystem 5).evolve 5 x = x :=
  modularCounter_period 5 x

/-- Therefore the modular counter cannot satisfy the natural-valued tick law. -/
theorem modularFive_no_internalCounter :
    IsEmpty (InternalCounter (modularCounterSystem 5)) := by
  refine ⟨fun C => ?_⟩
  exact (C.no_positive_period (0 : ZMod 5) (k := 5) (by decide))
    (modularFive_period_five 0)

/-- A one-state deterministic system. -/
def stationarySystem : AutonomousSystem where
  State := Unit
  step := id

/-- Determinism alone does not supply an internal natural counter. -/
theorem stationary_no_internalCounter :
    IsEmpty (InternalCounter stationarySystem) := by
  refine ⟨fun C => ?_⟩
  exact (C.no_positive_period () (k := 1) (by decide)) (by rfl)

/-- Equal checkpoints do not imply equal complete states. -/
theorem same_checkpoint_different_full_state
    {A : CounterCheckpointSystem} {n m : N0} (hnm : n ≠ m)
    (ψ : A.Checkpoint) :
    ((⟨n, ψ⟩ : Omega A) ≠ ⟨m, ψ⟩) ∧
      (⟨n, ψ⟩ : Omega A).checkpoint = (⟨m, ψ⟩ : Omega A).checkpoint := by
  constructor
  · intro hstate
    apply hnm
    exact congrArg Omega.counter hstate
  · rfl

/-- A checkpoint may recur at every step while the complete state never returns. -/
def constantCheckpointSystem : CounterCheckpointSystem where
  Checkpoint := Unit
  updateCheckpoint := fun _ _ => ()

theorem constantCheckpoint_recurs (ω : Omega constantCheckpointSystem) :
    (constantCheckpointSystem.U ω).checkpoint = ω.checkpoint := by
  cases ω
  rfl

theorem constantCheckpoint_fullState_nonreturn
    (ω : Omega constantCheckpointSystem) {k : ℕ} (hk : 0 < k) :
    constantCheckpointSystem.autonomousSystem.evolve k ω ≠ ω :=
  constantCheckpointSystem.fullState_nonreturn ω hk

end TwistJ.Models
