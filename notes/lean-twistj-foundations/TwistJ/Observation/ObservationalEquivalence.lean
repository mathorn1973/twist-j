import TwistJ.Observation.ReadoutFamily

/-!
# Observational equivalence for one fixed readout family

Status: **NON-CANONICAL NOTE**.

The relation below is exactly the kernel relation of one supplied family. It
is not a completeness theorem, maximal invariant, orbit quotient, decoder
identity, or factor-canonicity result.
-/

set_option autoImplicit false

namespace TwistJ.Observation

universe u v w

namespace ReadoutFamily

/-- Two inputs agree at every leg of this fixed heterogeneous family. -/
def ObservationallyEquivalent {Input : Type u}
    (R : ReadoutFamily.{u, v, w} Input) (x y : Input) : Prop :=
  ∀ i, R.read i x = R.read i y

theorem observationallyEquivalent_iff {Input : Type u}
    (R : ReadoutFamily.{u, v, w} Input) (x y : Input) :
    R.ObservationallyEquivalent x y ↔
      ∀ i, R.read i x = R.read i y :=
  Iff.rfl

theorem observationallyEquivalent_refl {Input : Type u}
    (R : ReadoutFamily.{u, v, w} Input) (x : Input) :
    R.ObservationallyEquivalent x x := by
  intro i
  rfl

theorem observationallyEquivalent_of_eq {Input : Type u}
    (R : ReadoutFamily.{u, v, w} Input) {x y : Input} (hxy : x = y) :
    R.ObservationallyEquivalent x y := by
  subst y
  exact R.observationallyEquivalent_refl x

theorem observationallyEquivalent_symm {Input : Type u}
    (R : ReadoutFamily.{u, v, w} Input) {x y : Input}
    (hxy : R.ObservationallyEquivalent x y) :
    R.ObservationallyEquivalent y x := by
  intro i
  exact (hxy i).symm

theorem observationallyEquivalent_trans {Input : Type u}
    (R : ReadoutFamily.{u, v, w} Input) {x y z : Input}
    (hxy : R.ObservationallyEquivalent x y)
    (hyz : R.ObservationallyEquivalent y z) :
    R.ObservationallyEquivalent x z := by
  intro i
  exact (hxy i).trans (hyz i)

/-- Package the kernel relation as a setoid without constructing a quotient. -/
def observationalSetoid {Input : Type u}
    (R : ReadoutFamily.{u, v, w} Input) : Setoid Input where
  r := R.ObservationallyEquivalent
  iseqv := {
    refl := R.observationallyEquivalent_refl
    symm := R.observationallyEquivalent_symm
    trans := R.observationallyEquivalent_trans
  }

/-- One unequal leg is enough to refute equivalence for the fixed family. -/
theorem not_observationallyEquivalent_of_read_ne {Input : Type u}
    (R : ReadoutFamily.{u, v, w} Input) {x y : Input}
    (i : R.Index) (hne : R.read i x ≠ R.read i y) :
    ¬ R.ObservationallyEquivalent x y := by
  intro hxy
  exact hne (hxy i)

end ReadoutFamily

namespace PartialReadout

/-- The unit-indexed family compares exactly the original partial reading. -/
theorem toFamily_observationallyEquivalent_iff {Input : Type u}
    (R : PartialReadout.{u, w} Input) (x y : Input) :
    R.toFamily.ObservationallyEquivalent x y ↔ R.read x = R.read y := by
  constructor
  · intro hxy
    exact hxy ()
  · intro hread i
    cases i
    exact hread

end PartialReadout

end TwistJ.Observation
