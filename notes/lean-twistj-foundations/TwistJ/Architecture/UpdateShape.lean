import Mathlib.Data.ZMod.Basic
import TwistJ.Architecture.CounterCheckpoint
import TwistJ.Foundation.InternalCounter

/-!
# Counter consequences of the declared update shape

Status: **NON-CANONICAL NOTE**.

This module depends on the foundation and the update shape only. It imports no
decoder, dictionary, or algebraic-seed module.
-/

set_option autoImplicit false

namespace TwistJ.Architecture

open TwistJ.Foundation

universe u

namespace CounterCheckpointSystem

/-- Every counter-checkpoint skew product carries the displayed natural counter. -/
def internalCounter (A : CounterCheckpointSystem.{u}) :
    InternalCounter A.autonomousSystem where
  tick := fun ω => ω.counter.index
  tick_step := by
    intro ω
    cases ω
    rfl

/-- The complete-state counter advances by exactly the iteration count. -/
theorem counter_index_evolve (A : CounterCheckpointSystem.{u}) (k : ℕ)
    (ω : Omega A) :
    (A.autonomousSystem.evolve k ω).counter.index =
      ω.counter.index + k := by
  exact (A.internalCounter.tick_evolve k ω)

/-- No complete state in this skew-product architecture has positive period. -/
theorem fullState_nonreturn (A : CounterCheckpointSystem.{u}) (ω : Omega A)
    {k : ℕ} (hk : 0 < k) :
    A.autonomousSystem.evolve k ω ≠ ω :=
  A.internalCounter.no_positive_period ω hk

end CounterCheckpointSystem

/-- The Public Canon v32 checkpoint carrier `F_5^6`. -/
abbrev PublicCheckpoint : Type :=
  Fin 6 → ZMod 5

/-- The v32 state/update shape with the internal five-map formula left parametric. -/
def publicCanonV32System
    (updateCheckpoint : N0 → PublicCheckpoint → PublicCheckpoint) :
    CounterCheckpointSystem where
  Checkpoint := PublicCheckpoint
  updateCheckpoint := updateCheckpoint

/-- Exact v32-shaped specialization of the counter-advance theorem. -/
theorem publicCanonV32_counter_index_evolve
    (updateCheckpoint : N0 → PublicCheckpoint → PublicCheckpoint)
    (k : ℕ) (ω : Omega (publicCanonV32System updateCheckpoint)) :
    ((publicCanonV32System updateCheckpoint).autonomousSystem.evolve k ω).counter.index =
      ω.counter.index + k :=
  (publicCanonV32System updateCheckpoint).counter_index_evolve k ω

/-- Exact v32-shaped specialization of complete-state non-return. -/
theorem publicCanonV32_fullState_nonreturn
    (updateCheckpoint : N0 → PublicCheckpoint → PublicCheckpoint)
    (ω : Omega (publicCanonV32System updateCheckpoint))
    {k : ℕ} (hk : 0 < k) :
    (publicCanonV32System updateCheckpoint).autonomousSystem.evolve k ω ≠ ω :=
  (publicCanonV32System updateCheckpoint).fullState_nonreturn ω hk

end TwistJ.Architecture
