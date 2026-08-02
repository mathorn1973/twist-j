import Mathlib.GroupTheory.OrderOfElement
import Mathlib.Tactic.Ring
import TwistJ.AlgebraicSeed.FifthRootData

/-!
# The integer-native fifth-cyclotomic carrier

Status: **NON-CANONICAL NOTE**.

`CyclotomicFiveInt` is the explicit rank-four integer carrier with ordered
coordinates in the basis `1, j, j^2, j^3`.  Multiplication reduces `j^4` by
`1 + j + j^2 + j^3 + j^4 = 0`.  No number-field, analytic, decoder, counter,
or public-update structure is imported.
-/

set_option autoImplicit false

namespace TwistJ.AlgebraicSeed

/-- Four integer coordinates in the ordered basis `1, j, j^2, j^3`. -/
@[ext]
structure CyclotomicFiveInt where
  c0 : ℤ
  c1 : ℤ
  c2 : ℤ
  c3 : ℤ
deriving DecidableEq, Repr

namespace CyclotomicFiveInt

protected def add (x y : CyclotomicFiveInt) : CyclotomicFiveInt :=
  ⟨x.c0 + y.c0, x.c1 + y.c1, x.c2 + y.c2, x.c3 + y.c3⟩

protected def neg (x : CyclotomicFiveInt) : CyclotomicFiveInt :=
  ⟨-x.c0, -x.c1, -x.c2, -x.c3⟩

protected def zero : CyclotomicFiveInt :=
  ⟨0, 0, 0, 0⟩

protected def one : CyclotomicFiveInt :=
  ⟨1, 0, 0, 0⟩

/--
Convolution followed by the reductions `j^4 = -(1+j+j^2+j^3)`,
`j^5 = 1`, and `j^6 = j`.
-/
protected def mul (x y : CyclotomicFiveInt) : CyclotomicFiveInt :=
  ⟨x.c0 * y.c0 - (x.c1 * y.c3 + x.c2 * y.c2 + x.c3 * y.c1) +
      (x.c2 * y.c3 + x.c3 * y.c2),
    x.c0 * y.c1 + x.c1 * y.c0 -
      (x.c1 * y.c3 + x.c2 * y.c2 + x.c3 * y.c1) + x.c3 * y.c3,
    x.c0 * y.c2 + x.c1 * y.c1 + x.c2 * y.c0 -
      (x.c1 * y.c3 + x.c2 * y.c2 + x.c3 * y.c1),
    x.c0 * y.c3 + x.c1 * y.c2 + x.c2 * y.c1 + x.c3 * y.c0 -
      (x.c1 * y.c3 + x.c2 * y.c2 + x.c3 * y.c1)⟩

instance : Add CyclotomicFiveInt := ⟨CyclotomicFiveInt.add⟩
instance : Neg CyclotomicFiveInt := ⟨CyclotomicFiveInt.neg⟩
instance : Zero CyclotomicFiveInt := ⟨CyclotomicFiveInt.zero⟩
instance : One CyclotomicFiveInt := ⟨CyclotomicFiveInt.one⟩
instance : Mul CyclotomicFiveInt := ⟨CyclotomicFiveInt.mul⟩

@[simp] theorem add_c0 (x y : CyclotomicFiveInt) : (x + y).c0 = x.c0 + y.c0 := rfl
@[simp] theorem add_c1 (x y : CyclotomicFiveInt) : (x + y).c1 = x.c1 + y.c1 := rfl
@[simp] theorem add_c2 (x y : CyclotomicFiveInt) : (x + y).c2 = x.c2 + y.c2 := rfl
@[simp] theorem add_c3 (x y : CyclotomicFiveInt) : (x + y).c3 = x.c3 + y.c3 := rfl

@[simp] theorem neg_c0 (x : CyclotomicFiveInt) : (-x).c0 = -x.c0 := rfl
@[simp] theorem neg_c1 (x : CyclotomicFiveInt) : (-x).c1 = -x.c1 := rfl
@[simp] theorem neg_c2 (x : CyclotomicFiveInt) : (-x).c2 = -x.c2 := rfl
@[simp] theorem neg_c3 (x : CyclotomicFiveInt) : (-x).c3 = -x.c3 := rfl

@[simp] theorem zero_c0 : (0 : CyclotomicFiveInt).c0 = 0 := rfl
@[simp] theorem zero_c1 : (0 : CyclotomicFiveInt).c1 = 0 := rfl
@[simp] theorem zero_c2 : (0 : CyclotomicFiveInt).c2 = 0 := rfl
@[simp] theorem zero_c3 : (0 : CyclotomicFiveInt).c3 = 0 := rfl

@[simp] theorem one_c0 : (1 : CyclotomicFiveInt).c0 = 1 := rfl
@[simp] theorem one_c1 : (1 : CyclotomicFiveInt).c1 = 0 := rfl
@[simp] theorem one_c2 : (1 : CyclotomicFiveInt).c2 = 0 := rfl
@[simp] theorem one_c3 : (1 : CyclotomicFiveInt).c3 = 0 := rfl

@[simp] theorem mul_c0 (x y : CyclotomicFiveInt) :
    (x * y).c0 = x.c0 * y.c0 - (x.c1 * y.c3 + x.c2 * y.c2 + x.c3 * y.c1) +
      (x.c2 * y.c3 + x.c3 * y.c2) := rfl
@[simp] theorem mul_c1 (x y : CyclotomicFiveInt) :
    (x * y).c1 = x.c0 * y.c1 + x.c1 * y.c0 -
      (x.c1 * y.c3 + x.c2 * y.c2 + x.c3 * y.c1) + x.c3 * y.c3 := rfl
@[simp] theorem mul_c2 (x y : CyclotomicFiveInt) :
    (x * y).c2 = x.c0 * y.c2 + x.c1 * y.c1 + x.c2 * y.c0 -
      (x.c1 * y.c3 + x.c2 * y.c2 + x.c3 * y.c1) := rfl
@[simp] theorem mul_c3 (x y : CyclotomicFiveInt) :
    (x * y).c3 = x.c0 * y.c3 + x.c1 * y.c2 + x.c2 * y.c1 + x.c3 * y.c0 -
      (x.c1 * y.c3 + x.c2 * y.c2 + x.c3 * y.c1) := rfl

instance instAddCommGroup : AddCommGroup CyclotomicFiveInt := by
  refine
    { sub := fun a b => a + -b
      nsmul := @nsmulRec CyclotomicFiveInt ⟨CyclotomicFiveInt.zero⟩
        ⟨CyclotomicFiveInt.add⟩
      zsmul := @zsmulRec CyclotomicFiveInt ⟨CyclotomicFiveInt.zero⟩
        ⟨CyclotomicFiveInt.add⟩ ⟨CyclotomicFiveInt.neg⟩
        (@nsmulRec CyclotomicFiveInt ⟨CyclotomicFiveInt.zero⟩
          ⟨CyclotomicFiveInt.add⟩)
      add_assoc := ?_
      zero_add := ?_
      add_zero := ?_
      neg_add_cancel := ?_
      add_comm := ?_ } <;>
    intros <;>
    ext <;>
    simp <;>
    ring

/--
The natural and integer casts are explicit coordinate embeddings.  Keeping
them in the structure prevents later scalar-action diamonds from being hidden
behind defaults.
-/
instance instAddGroupWithOne : AddGroupWithOne CyclotomicFiveInt :=
  { CyclotomicFiveInt.instAddCommGroup with
    natCast := fun n => ⟨n, 0, 0, 0⟩
    intCast := fun z => ⟨z, 0, 0, 0⟩ }

instance instCommRing : CommRing CyclotomicFiveInt := by
  refine
    { CyclotomicFiveInt.instAddGroupWithOne with
      npow := @npowRec CyclotomicFiveInt ⟨CyclotomicFiveInt.one⟩
        ⟨CyclotomicFiveInt.mul⟩
      add_comm := ?_
      left_distrib := ?_
      right_distrib := ?_
      zero_mul := ?_
      mul_zero := ?_
      mul_assoc := ?_
      one_mul := ?_
      mul_one := ?_
      mul_comm := ?_ } <;>
    intros <;>
    ext <;>
    simp <;>
    ring

@[simp]
theorem natCast_coordinates (n : ℕ) :
    (n : CyclotomicFiveInt) = ⟨(n : ℤ), 0, 0, 0⟩ :=
  rfl

@[simp]
theorem intCast_coordinates (z : ℤ) :
    (z : CyclotomicFiveInt) = ⟨z, 0, 0, 0⟩ :=
  rfl

/-- The named fifth root, in integer coordinates. -/
def j : CyclotomicFiveInt :=
  ⟨0, 1, 0, 0⟩

theorem j_pow_two_coordinates : j ^ 2 = ⟨0, 0, 1, 0⟩ := by
  decide

theorem j_pow_three_coordinates : j ^ 3 = ⟨0, 0, 0, 1⟩ := by
  decide

theorem j_pow_four_coordinates : j ^ 4 = ⟨-1, -1, -1, -1⟩ := by
  decide

theorem cyclotomic_relation :
    1 + j + j ^ 2 + j ^ 3 + j ^ 4 = 0 := by
  decide

theorem j_pow_five : j ^ 5 = 1 := by
  decide

theorem j_ne_one : j ≠ 1 := by
  decide

theorem j_isPrimitiveRoot : IsPrimitiveRoot j 5 := by
  refine ⟨j_pow_five, ?_⟩
  intro n hn
  letI : Fact (Nat.Prime 5) := ⟨Nat.prime_five⟩
  have horder : orderOf j = 5 := orderOf_eq_prime j_pow_five j_ne_one
  rw [← horder]
  exact orderOf_dvd_of_pow_eq_one hn

/-- The explicit integer carrier instantiates the general root data. -/
def fifthRootData : FifthRootData CyclotomicFiveInt where
  ζ := j
  primitive := j_isPrimitiveRoot

end CyclotomicFiveInt

end TwistJ.AlgebraicSeed
