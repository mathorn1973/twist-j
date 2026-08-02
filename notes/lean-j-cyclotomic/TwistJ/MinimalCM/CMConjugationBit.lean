import Mathlib.Algebra.Field.ZMod
import Mathlib.Algebra.Module.ZMod
import Mathlib.GroupTheory.OrderOfElement
import Mathlib.LinearAlgebra.Basis.VectorSpace
import Mathlib.LinearAlgebra.Dual.Lemmas
import Mathlib.Tactic.NormNum

/-!
# The quadratic-character quarter-turn floor

Status: **NON-CANONICAL NOTE**.

This module proves only the abstract additive-group theorem frozen in
`SELECTION-CONTRACT.md`. It makes no claim about finite groups, unique bits,
CM fields, unit ranks, discriminants, cyclotomic fields, or physical motion.
-/

set_option autoImplicit false

namespace TwistJ.MinimalCM

/--
If every additive quadratic character kills a nonzero involution `c` in an
abelian group, then `c` has a square root of additive order four.

No finiteness or uniqueness-of-character hypothesis is used. The proof passes
to `G / 2G`, separates a nonzero class by the linear dual over `ZMod 2`, and
then applies the prime-power order criterion.
-/
theorem exists_addOrderOf_four_of_all_quadratic_chars_vanish
    {G : Type*} [AddCommGroup G] (c : G)
    (hc_ne : c ≠ 0)
    (hc_two : 2 • c = 0)
    (hχ : ∀ χ : G →+ ZMod 2, χ c = 0) :
    ∃ τ : G, addOrderOf τ = 4 ∧ 2 • τ = c := by
  let D : AddSubgroup G := (nsmulAddMonoidHom 2).range
  let q : G →+ G ⧸ D := QuotientAddGroup.mk' D
  letI : Module (ZMod 2) (G ⧸ D) :=
    QuotientAddGroup.zmodModule fun x ↦ ⟨x, rfl⟩
  have hqc : q c = 0 := by
    rw [← Module.forall_dual_apply_eq_zero_iff (ZMod 2)]
    intro φ
    simpa [q] using hχ (φ.toAddMonoidHom.comp q)
  have hcD : c ∈ D := by
    exact (QuotientAddGroup.eq_zero_iff c).mp (by simpa [q] using hqc)
  obtain ⟨τ, hτ⟩ := hcD
  have hτ_two : 2 • τ = c := hτ
  have hτ_two_ne : 2 • τ ≠ 0 := by simpa [hτ_two] using hc_ne
  have hτ_four : 4 • τ = 0 := by
    calc
      4 • τ = (2 * 2) • τ := by norm_num
      _ = 2 • (2 • τ) := by rw [mul_nsmul]
      _ = 2 • c := by rw [hτ_two]
      _ = 0 := hc_two
  refine ⟨τ, ?_, hτ_two⟩
  simpa using
    (addOrderOf_eq_prime_pow (p := 2) (n := 1) (x := τ)
      (by simpa using hτ_two_ne) (by simpa using hτ_four))

end TwistJ.MinimalCM
