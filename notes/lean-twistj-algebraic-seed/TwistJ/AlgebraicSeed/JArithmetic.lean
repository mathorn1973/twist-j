import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.FinCases
import TwistJ.AlgebraicSeed.IntegralCarrier

/-!
# Exact arithmetic of `J` on the integer carrier

Status: **NON-CANONICAL NOTE**.

The matrix below is multiplication by `J` on the rank-four integer carrier.
It is not the Public Canon v32 autonomous update `U`, is not a time input, and
does not imply the declared counter-checkpoint architecture.
-/

set_option autoImplicit false
open scoped Matrix

namespace TwistJ.AlgebraicSeed.CyclotomicFiveInt

/-- The defined seed in the explicit integer carrier. -/
def J : CyclotomicFiveInt :=
  fifthRootData.J

/-- The exact golden element `-(j^2+j^3)` in the integer carrier. -/
def phi : CyclotomicFiveInt :=
  -(j ^ 2 + j ^ 3)

theorem J_coordinates : J = ⟨1, 0, 1, 0⟩ := by
  decide

theorem phi_coordinates : phi = ⟨0, 0, -1, -1⟩ := by
  decide

theorem cube_law : (J - 1) ^ 3 = j :=
  fifthRootData.J_sub_one_cube

theorem phi_quadratic : phi ^ 2 = phi + 1 := by
  decide

theorem golden_bridge : J * phi = j := by
  decide

theorem fifth_power_bridge : J ^ 5 * phi ^ 5 = 1 := by
  decide

/-- Exact normal form behind the non-periodicity regression at exponent five. -/
theorem J_pow_five_coordinates : J ^ 5 = ⟨-8, 0, -5, -5⟩ := by
  decide

/-- Regression: the seed itself is not a fifth root of unity. -/
theorem J_pow_five_ne_one : J ^ 5 ≠ 1 := by
  rw [J_pow_five_coordinates]
  decide

/-- The displayed integer action of multiplication by `J`. -/
def step (x : CyclotomicFiveInt) : CyclotomicFiveInt :=
  ⟨x.c0 - x.c2 + x.c3, x.c1 - x.c2, x.c0, x.c1 - x.c2 + x.c3⟩

theorem J_mul_eq_step (x : CyclotomicFiveInt) :
    J * x = step x := by
  rw [J_coordinates]
  ext
  all_goals simp [step] <;> ring

/-- Coordinates in the ordered basis `1, j, j^2, j^3`. -/
def coordinates (x : CyclotomicFiveInt) : Fin 4 → ℤ :=
  ![x.c0, x.c1, x.c2, x.c3]

/-- The public `M_J` matrix, with images of basis vectors as columns. -/
def M_J : Matrix (Fin 4) (Fin 4) ℤ :=
  !![1, 0, -1, 1;
     0, 1, -1, 0;
     1, 0,  0, 0;
     0, 1, -1, 1]

theorem M_J_mulVec_coordinates (x : CyclotomicFiveInt) :
    M_J *ᵥ coordinates x = coordinates (J * x) := by
  funext i
  fin_cases i
  all_goals
    simp [M_J, coordinates, J_mul_eq_step, step, Matrix.mulVec, dotProduct,
      Fin.sum_univ_succ] <;>
    ring

/-- Basis elements used to define the regular multiplication matrix. -/
def basisElement : Fin 4 → CyclotomicFiveInt :=
  ![1, j, j ^ 2, j ^ 3]

/-- Matrix of left multiplication in the ordered integer basis. -/
def mulMatrix (x : CyclotomicFiveInt) : Matrix (Fin 4) (Fin 4) ℤ :=
  fun row col => coordinates (x * basisElement col) row

theorem mulMatrix_J : mulMatrix J = M_J := by
  decide

/-- The determinant of the regular multiplication matrix. -/
def regularNorm (x : CyclotomicFiveInt) : ℤ :=
  (mulMatrix x).det

/-- The trace of the regular multiplication matrix. -/
def regularTrace (x : CyclotomicFiveInt) : ℤ :=
  Matrix.trace (mulMatrix x)

theorem det_M_J : M_J.det = 1 := by
  decide

theorem trace_M_J : Matrix.trace M_J = 3 := by
  decide

/-- Regression: the integral multiplication matrix is not period five. -/
theorem M_J_pow_five_ne_one : M_J ^ 5 ≠ 1 := by
  decide

theorem regularNorm_J : regularNorm J = 1 := by
  rw [regularNorm, mulMatrix_J, det_M_J]

theorem regularTrace_J : regularTrace J = 3 := by
  rw [regularTrace, mulMatrix_J, trace_M_J]

end TwistJ.AlgebraicSeed.CyclotomicFiveInt
