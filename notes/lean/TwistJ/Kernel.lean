import Mathlib

/-!
# TWIST-J kernel, layer 0: the axiom J = 1 + zeta_5^2

Every identity below is proved in an arbitrary commutative ring `R` from the
single hypothesis that `j` satisfies the fifth cyclotomic relation. Nothing
else is assumed: no field, no embedding, no real numbers. Each proof is one
`linear_combination` whose coefficient is the exact quotient by Phi_5.

The last section instantiates the hypothesis in Mathlib's own
`CyclotomicField 5 ℚ`, so the abstract statements are not vacuous.
-/

set_option autoImplicit false

namespace TwistJ.Kernel

variable {R : Type*} [CommRing R] (j : R)

/-- The fifth cyclotomic relation, the only hypothesis of this file. -/
def Phi5 : Prop := j ^ 4 + j ^ 3 + j ^ 2 + j + 1 = 0

/-- The axiom. -/
def J : R := 1 + j ^ 2

/-- The golden ratio as a projection of `j`. -/
def phi : R := -j ^ 2 - j ^ 3

variable {j}

theorem pow_five (h : Phi5 j) : j ^ 5 = 1 := by
  unfold Phi5 at h; linear_combination (j - 1) * h

/-- `J · φ = j`: rotation is golden ratio times dynamics. -/
theorem J_mul_phi (h : Phi5 j) : J j * phi j = j := by
  unfold Phi5 at h; unfold J phi; linear_combination (-j) * h

/-- `(J - 1)^3 = j`. -/
theorem J_sub_one_cube (h : Phi5 j) : (J j - 1) ^ 3 = j := by
  unfold Phi5 at h; unfold J; linear_combination (j ^ 2 - j) * h

/-- `φ² = φ + 1`. -/
theorem phi_sq (h : Phi5 j) : phi j ^ 2 = phi j + 1 := by
  unfold Phi5 at h; unfold phi; linear_combination (j ^ 2 + j - 1) * h

/-- `φ · (1 - φ) = -1`, so `ψ = 1 - φ` and `φψ = -1`. -/
theorem phi_mul_psi (h : Phi5 j) : phi j * (1 - phi j) = -1 := by
  unfold Phi5 at h; unfold phi; linear_combination (-j ^ 2 - j + 1) * h

/-- `J` is a unit with explicit inverse `-j - j²`. -/
theorem J_mul_inv (h : Phi5 j) : J j * (-j - j ^ 2) = 1 := by
  unfold Phi5 at h; unfold J; linear_combination (-1 : R) * h

/-- `J⁵ φ⁵ = 1`, that is `J⁵ = φ⁻⁵`. -/
theorem J_pow_five_mul_phi_pow_five (h : Phi5 j) : J j ^ 5 * phi j ^ 5 = 1 := by
  rw [← mul_pow, J_mul_phi h, pow_five h]

/-- Norm of `J` as the product of its four Galois images `1 + j^(2t)`. -/
theorem norm_J (h : Phi5 j) :
    (1 + j ^ 2) * (1 + j ^ 4) * (1 + j ^ 6) * (1 + j ^ 8) = 1 := by
  unfold Phi5 at h
  linear_combination
    (j ^ 16 - j ^ 15 + j ^ 14 - j ^ 13 + j ^ 12 + j ^ 10 - j ^ 9 + j ^ 8 - j ^ 7
      + 2 * j ^ 6 - j ^ 5 + j ^ 4 - j ^ 3 + j ^ 2) * h

/-- Trace of `J` as the sum of its four Galois images. -/
theorem trace_J (h : Phi5 j) :
    (1 + j ^ 2) + (1 + j ^ 4) + (1 + j ^ 6) + (1 + j ^ 8) = 3 := by
  unfold Phi5 at h; linear_combination (j ^ 4 - j ^ 3 + j ^ 2 - j + 1) * h

/-- The integer step of the Canon is multiplication by `J` in the basis
`1, j, j², j³`:
`(a,b,c,d) ↦ (a - c + d, b - c, a, b - c + d)`. -/
theorem step_eq_mul_J (h : Phi5 j) (a b c d : R) :
    J j * (a + b * j + c * j ^ 2 + d * j ^ 3) =
      (a - c + d) + (b - c) * j + a * j ^ 2 + (b - c + d) * j ^ 3 := by
  unfold Phi5 at h; unfold J; linear_combination (c + d * j - d) * h

/-- The complex conjugate of `J` in the ring: `j ↦ j⁴` sends `j²` to `j⁸ = j³`. -/
def Jbar (j : R) : R := 1 + j ^ 3

/-- The modulus chord: `J · J̄ = 2 - φ`. -/
theorem J_mul_Jbar (h : Phi5 j) : J j * Jbar j = 2 - phi j := by
  unfold Phi5 at h; unfold J Jbar phi; linear_combination (j - 1) * h

/-- `2 - φ = φ⁻²`, written without division: `(2 - φ) φ² = 1`. -/
theorem two_sub_phi_mul_phi_sq (h : Phi5 j) : (2 - phi j) * phi j ^ 2 = 1 := by
  unfold Phi5 at h; unfold phi
  linear_combination (j ^ 5 + 2 * j ^ 4 + j - 1) * h

/-- `1 - J = -j²`. -/
theorem one_sub_J : 1 - J j = -j ^ 2 := by unfold J; ring

/-- `(1 - J)⁵ = -1`, hence `(1 - J)¹⁰ = 1`: a tenth root of unity in the ring. -/
theorem one_sub_J_pow_five (h : Phi5 j) : (1 - J j) ^ 5 = -1 := by
  rw [one_sub_J]; unfold Phi5 at h
  linear_combination (-j ^ 6 + j ^ 5 - j + 1) * h

theorem one_sub_J_pow_ten (h : Phi5 j) : (1 - J j) ^ 10 = 1 := by
  rw [show (10 : ℕ) = 5 * 2 from rfl, pow_mul, one_sub_J_pow_five h]; norm_num

/-- The characteristic polynomial of the step, `x⁴ - 3x³ + 4x² - 2x + 1 = Φ₅(x - 1)`,
annihilates `J`. -/
theorem J_charpoly (h : Phi5 j) :
    J j ^ 4 - 3 * J j ^ 3 + 4 * J j ^ 2 - 2 * J j + 1 = 0 := by
  unfold Phi5 at h; unfold J; linear_combination (j ^ 4 - j ^ 3 + j ^ 2 - j + 1) * h

end TwistJ.Kernel

/-! ## The hypothesis is inhabited: Mathlib's fifth cyclotomic field. -/

namespace TwistJ.Kernel

/-- At this Mathlib pin the generic instance is not found by instance search
(transparency of the two `Algebra ℚ` paths); the term itself typechecks, so it
is registered here under its exact type. -/
instance cyc5 : IsCyclotomicExtension {5} ℚ (CyclotomicField 5 ℚ) :=
  CyclotomicField.isCyclotomicExtension 5 ℚ

/-- Any primitive fifth root of unity in a domain satisfies `Phi5`. -/
theorem phi5_of_isPrimitiveRoot {K : Type*} [CommRing K] [IsDomain K] {z : K}
    (hz : IsPrimitiveRoot z 5) : Phi5 z := by
  have := hz.geom_sum_eq_zero (by norm_num : 1 < 5)
  simp [Finset.sum_range_succ] at this
  unfold Phi5; linear_combination this

/-- The witness: Mathlib's chosen generator of `ℚ(ζ₅)`. -/
theorem phi5_cyclotomicField :
    Phi5 (IsCyclotomicExtension.zeta 5 ℚ (CyclotomicField 5 ℚ)) :=
  phi5_of_isPrimitiveRoot (IsCyclotomicExtension.zeta_spec 5 ℚ (CyclotomicField 5 ℚ))

/-- Concrete instance: `J · φ = j` in `ℚ(ζ₅)`. -/
example : J (IsCyclotomicExtension.zeta 5 ℚ (CyclotomicField 5 ℚ)) *
    phi (IsCyclotomicExtension.zeta 5 ℚ (CyclotomicField 5 ℚ)) =
    IsCyclotomicExtension.zeta 5 ℚ (CyclotomicField 5 ℚ) :=
  J_mul_phi phi5_cyclotomicField

end TwistJ.Kernel

