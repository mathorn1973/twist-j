import TwistJLeanNote
import Mathlib.Algebra.Module.ZMod
import Mathlib.GroupTheory.Abelianization.Defs
import Mathlib.GroupTheory.OrderOfElement
import Mathlib.GroupTheory.Sylow
import Mathlib.LinearAlgebra.Dual.Lemmas
import Mathlib.NumberTheory.Cyclotomic.Discriminant
import Mathlib.NumberTheory.Cyclotomic.Gal
import Mathlib.NumberTheory.DirichletCharacter.Basic
import Mathlib.NumberTheory.NumberField.CMField
import Mathlib.NumberTheory.NumberField.Discriminant.Basic
import Mathlib.NumberTheory.NumberField.Units.DirichletTheorem

/-!
NON-CANONICAL ENVIRONMENT INVENTORY ONLY.

This file checks that selected upstream names elaborate at the pinned Mathlib
commit and prints the axiom footprints of selected existing declarations. It
proves no MinimalCM result, creates no public evidence, and must not be reused
as an A-LEAN audit source.
-/

set_option autoImplicit false

-- Group-theory API floor.
#check Abelianization
#check Abelianization.of
#check Abelianization.lift
#check Abelianization.lift_of_comp
#check nsmulAddMonoidHom
#check QuotientAddGroup.zmodModule
#check Module.forall_dual_apply_eq_zero_iff
#check addOrderOf
#check Sylow
#check Sylow.card_eq_multiplicity

-- CM, units, and discriminant API floor.
#check NumberField.IsCMField
#check NumberField.IsCMField.complexConj
#check NumberField.IsCMField.orderOf_complexConj
#check NumberField.Units.rank
#check NumberField.Units.rank_modTorsion
#check NumberField.discr
#check NumberField.abs_discr_ge_of_isTotallyComplex

-- Cyclotomic witness API floor.
#check IsCyclotomicExtension.Rat.isCMField
#check IsCyclotomicExtension.autEquivPow
#check IsCyclotomicExtension.discr_odd_prime

-- Dirichlet-character primitives only; no field correspondence is claimed.
#check DirichletCharacter
#check DirichletCharacter.conductor
#check DirichletCharacter.IsPrimitive
#check DirichletCharacter.primitiveCharacter
#check DirichletCharacter.primitiveCharacter_isPrimitive
#check DirichletCharacter.Even
#check DirichletCharacter.Odd
#check DirichletCharacter.conductor_inv

-- Selected upstream logical footprints.
#print axioms Abelianization.lift_of_comp
#print axioms NumberField.IsCMField.orderOf_complexConj
#print axioms NumberField.Units.rank_modTorsion
#print axioms NumberField.abs_discr_ge_of_isTotallyComplex
#print axioms IsCyclotomicExtension.autEquivPow
#print axioms IsCyclotomicExtension.discr_odd_prime
#print axioms DirichletCharacter.primitiveCharacter_isPrimitive

-- Existing symbolic note only; no MinimalCM theorem exists at this stage.
#print axioms TwistJLeanNote.fifth_power_eq_one
#print axioms TwistJLeanNote.square_satisfies_fifth_cyclotomic
#print axioms TwistJLeanNote.J_satisfies_quartic
