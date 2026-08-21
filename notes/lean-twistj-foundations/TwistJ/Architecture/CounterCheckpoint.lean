import TwistJ.Architecture.N0
import TwistJ.Foundation.AutonomousSystem

/-!
# Counter-checkpoint skew products

Status: **NON-CANONICAL NOTE**.

The checkpoint is a projection of the complete state. Its update may depend on
the current counter and checkpoint, but the counter always advances by one.
-/

set_option autoImplicit false

namespace TwistJ.Architecture

open TwistJ.Foundation

universe u

/-- The data needed for a counter-driven checkpoint update. -/
structure CounterCheckpointSystem where
  Checkpoint : Type u
  updateCheckpoint : N0 → Checkpoint → Checkpoint

/-- Complete state: forward counter together with a finite or infinite checkpoint. -/
structure Omega (A : CounterCheckpointSystem.{u}) where
  counter : N0
  checkpoint : A.Checkpoint

namespace CounterCheckpointSystem

/-- The autonomous skew-product update. -/
def U (A : CounterCheckpointSystem.{u}) : Omega A → Omega A
  | ⟨n, ψ⟩ => ⟨n.succ, A.updateCheckpoint n ψ⟩

/-- Regard the skew product as an autonomous one-step system. -/
def autonomousSystem (A : CounterCheckpointSystem.{u}) : AutonomousSystem.{u} where
  State := Omega A
  step := A.U

@[simp]
theorem U_counter (A : CounterCheckpointSystem.{u}) (ω : Omega A) :
    (A.U ω).counter = ω.counter.succ := by
  cases ω
  rfl

@[simp]
theorem U_checkpoint (A : CounterCheckpointSystem.{u}) (n : N0)
    (ψ : A.Checkpoint) :
    (A.U ⟨n, ψ⟩).checkpoint = A.updateCheckpoint n ψ :=
  rfl

end CounterCheckpointSystem

end TwistJ.Architecture
