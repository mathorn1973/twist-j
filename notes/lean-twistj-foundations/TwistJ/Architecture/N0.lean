import Mathlib.Data.Nat.Notation

/-!
# The named forward-counter carrier `N0`

Status: **NON-CANONICAL NOTE**.

`N0` is a named copy of the natural numbers. It represents the forward
odometer orbit by its index; it is not the whole 2-adic space.
-/

set_option autoImplicit false

namespace TwistJ.Architecture

/-- The forward odometer orbit, represented only by its natural index. -/
structure N0 where
  index : ℕ
deriving DecidableEq

namespace N0

/-- The initial forward-orbit index. -/
def zero : N0 :=
  ⟨0⟩

/-- Advance once along the named forward orbit. -/
def succ (n : N0) : N0 :=
  ⟨n.index + 1⟩

@[simp]
theorem zero_index : zero.index = 0 :=
  rfl

@[simp]
theorem succ_index (n : N0) : n.succ.index = n.index + 1 :=
  rfl

end N0

end TwistJ.Architecture
