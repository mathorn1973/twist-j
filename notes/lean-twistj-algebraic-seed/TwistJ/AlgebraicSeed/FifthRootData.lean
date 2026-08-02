import Mathlib.RingTheory.RootsOfUnity.PrimitiveRoots
import Mathlib.Tactic.Ring

/-!
# A primitive fifth root and the defined TWIST-J seed

Status: **NON-CANONICAL NOTE**.

This module contains only the carrier-independent definition boundary.  Lean's
`def J` constructs a term; it does not encode the Public Canon's ontological
decision to adopt that term as the generator of reality.
-/

set_option autoImplicit false

namespace TwistJ.AlgebraicSeed

/-- A named primitive fifth root in a commutative ring. -/
structure FifthRootData (K : Type*) [CommRing K] where
  ζ : K
  primitive : IsPrimitiveRoot ζ 5

namespace FifthRootData

variable {K : Type*} [CommRing K]

/-- The TWIST-J algebraic seed is a definition, not a Lean axiom. -/
def J (A : FifthRootData K) : K :=
  1 + A.ζ ^ 2

@[simp]
theorem J_sub_one (A : FifthRootData K) :
    A.J - 1 = A.ζ ^ 2 := by
  simp [J]

/-- The cube law uses only the fifth-power relation. -/
theorem J_sub_one_cube (A : FifthRootData K) :
    (A.J - 1) ^ 3 = A.ζ := by
  rw [J_sub_one]
  calc
    (A.ζ ^ 2) ^ 3 = A.ζ ^ 5 * A.ζ := by ring
    _ = A.ζ := by rw [A.primitive.pow_eq_one, one_mul]

end FifthRootData

end TwistJ.AlgebraicSeed
