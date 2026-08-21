import TwistJ.Foundation.AutonomousSystem

/-!
# Natural-valued internal counters

Status: **NON-CANONICAL NOTE**.

The counter is a function of the complete state. Its update law is an explicit
hypothesis and is not inferred from determinism or from the word "counter".
-/

set_option autoImplicit false

namespace TwistJ.Foundation

universe u

/-- A natural-valued state component that advances once per autonomous step. -/
structure InternalCounter (S : AutonomousSystem.{u}) where
  tick : S.State → ℕ
  tick_step : ∀ x, tick (S.step x) = tick x + 1

namespace InternalCounter

/-- Iterating the update `k` times advances the internal counter by `k`. -/
theorem tick_evolve {S : AutonomousSystem.{u}} (C : InternalCounter S)
    (k : ℕ) (x : S.State) :
    C.tick (S.evolve k x) = C.tick x + k := by
  induction k generalizing x with
  | zero => rfl
  | succ k ih =>
      calc
        C.tick (S.evolve k.succ x) =
            C.tick (S.evolve k (S.step x)) := rfl
        _ = C.tick (S.step x) + k := ih (S.step x)
        _ = (C.tick x + 1) + k := by rw [C.tick_step]
        _ = C.tick x + (1 + k) := Nat.add_assoc _ _ _
        _ = C.tick x + (k + 1) := by rw [Nat.add_comm 1 k]
        _ = C.tick x + k.succ := rfl

/-- A system with such a counter has no point of positive period. -/
theorem no_positive_period {S : AutonomousSystem.{u}} (C : InternalCounter S)
    (x : S.State) {k : ℕ} (hk : 0 < k) :
    S.evolve k x ≠ x := by
  intro hreturn
  have htick := congrArg C.tick hreturn
  rw [C.tick_evolve] at htick
  have hlt : C.tick x < C.tick x + k :=
    Nat.lt_add_of_pos_right hk
  exact (Nat.ne_of_lt hlt) htick.symm

end InternalCounter

end TwistJ.Foundation
