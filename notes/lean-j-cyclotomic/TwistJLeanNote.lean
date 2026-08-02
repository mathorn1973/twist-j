import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

namespace TwistJLeanNote

/--
The fifth cyclotomic relation implies the fifth-power relation.
The proof uses only commutative-ring algebra. No division is needed.
-/
theorem fifth_power_eq_one
    {R : Type*} [CommRing R] (ζ : R)
    (hζ : ζ ^ 4 + ζ ^ 3 + ζ ^ 2 + ζ + 1 = 0) :
    ζ ^ 5 = 1 := by
  have h : ζ ^ 5 - 1 = 0 := by
    calc
      ζ ^ 5 - 1 =
          (ζ - 1) * (ζ ^ 4 + ζ ^ 3 + ζ ^ 2 + ζ + 1) := by
            ring
      _ = 0 := by
        rw [hζ]
        ring
  exact sub_eq_zero.mp h

/--
If ζ satisfies Φ₅, then ζ² satisfies the same cyclotomic relation.
This makes the substitution J = 1 + ζ² available directly.
-/
theorem square_satisfies_fifth_cyclotomic
    {R : Type*} [CommRing R] (ζ : R)
    (hζ : ζ ^ 4 + ζ ^ 3 + ζ ^ 2 + ζ + 1 = 0) :
    (ζ ^ 2) ^ 4 + (ζ ^ 2) ^ 3 + (ζ ^ 2) ^ 2 + ζ ^ 2 + 1 = 0 := by
  have h5 : ζ ^ 5 = 1 := fifth_power_eq_one ζ hζ
  have h8 : ζ ^ 8 = ζ ^ 3 := by
    calc
      ζ ^ 8 = ζ ^ 5 * ζ ^ 3 := by ring
      _ = 1 * ζ ^ 3 := by rw [h5]
      _ = ζ ^ 3 := by ring
  have h6 : ζ ^ 6 = ζ := by
    calc
      ζ ^ 6 = ζ ^ 5 * ζ := by ring
      _ = 1 * ζ := by rw [h5]
      _ = ζ := by ring
  calc
    (ζ ^ 2) ^ 4 + (ζ ^ 2) ^ 3 + (ζ ^ 2) ^ 2 + ζ ^ 2 + 1 =
        ζ ^ 8 + ζ ^ 6 + ζ ^ 4 + ζ ^ 2 + 1 := by ring
    _ = ζ ^ 3 + ζ + ζ ^ 4 + ζ ^ 2 + 1 := by rw [h8, h6]
    _ = 0 := by
      linear_combination hζ

/--
For J = 1 + ζ², the fifth cyclotomic relation
forces the quartic relation

  J⁴ - 3J³ + 4J² - 2J + 1 = 0.

This is Φ₅(J - 1) = 0, formalized without numerical approximation.
-/
theorem J_satisfies_quartic
    {R : Type*} [CommRing R] (ζ : R)
    (hζ : ζ ^ 4 + ζ ^ 3 + ζ ^ 2 + ζ + 1 = 0) :
    let J : R := 1 + ζ ^ 2
    J ^ 4 - 3 * J ^ 3 + 4 * J ^ 2 - 2 * J + 1 = 0 := by
  dsimp
  have hζ2 := square_satisfies_fifth_cyclotomic ζ hζ
  calc
    (1 + ζ ^ 2) ^ 4 - 3 * (1 + ζ ^ 2) ^ 3 +
          4 * (1 + ζ ^ 2) ^ 2 - 2 * (1 + ζ ^ 2) + 1 =
        (ζ ^ 2) ^ 4 + (ζ ^ 2) ^ 3 + (ζ ^ 2) ^ 2 + ζ ^ 2 + 1 := by
          ring
    _ = 0 := hζ2

end TwistJLeanNote
