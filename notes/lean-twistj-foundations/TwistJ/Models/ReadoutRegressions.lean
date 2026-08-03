import TwistJ.Observation.OrbitReadout

/-!
# Partial and heterogeneous readout regressions

Status: **NON-CANONICAL NOTE**.

These examples freeze the distinction between undefined and defined output,
show that two undefined reads agree, and show that observational equivalence
for one family may be strictly coarser than equality of named forward orbits.
-/

set_option autoImplicit false

namespace TwistJ.Models

open TwistJ.Foundation
open TwistJ.Observation

/-- A simple autonomous system used only to type the regression orbits. -/
def successorSystem : AutonomousSystem where
  State := ℕ
  step := Nat.succ

/-- The named forward orbit beginning at `n`. -/
def successorOrbit (n : ℕ) : ForwardOrbit successorSystem :=
  ⟨n⟩

/-- Expose the concrete natural initial state of a demonstration orbit. -/
def successorInitial (κ : ForwardOrbit successorSystem) : ℕ :=
  κ.initial

@[simp]
theorem successorInitial_successorOrbit (n : ℕ) :
    successorInitial (successorOrbit n) = n :=
  rfl

theorem successorOrbit_one_ne_two :
    successorOrbit 1 ≠ successorOrbit 2 := by
  intro horbit
  have hinitial : (1 : ℕ) = 2 := congrArg successorInitial horbit
  exact (by decide : (1 : ℕ) ≠ 2) hinitial

/-- A partial readout defined only on the orbit named by initial state zero. -/
def zeroInitialReadout : OrbitPartialReadout successorSystem where
  Output := ℕ
  read := fun κ =>
    if successorInitial κ = 0 then some (successorInitial κ) else none

@[simp]
theorem zeroInitialReadout_zero :
    zeroInitialReadout.read (successorOrbit 0) = (some 0 : Option ℕ) := by
  simp [zeroInitialReadout]

@[simp]
theorem zeroInitialReadout_nonzero {n : ℕ} (hn : n ≠ 0) :
    zeroInitialReadout.read (successorOrbit n) = none := by
  simp [zeroInitialReadout, hn]

/-- `none` is not silently identified with a defined value. -/
theorem undefined_ne_defined :
    zeroInitialReadout.read (successorOrbit 1) ≠
      zeroInitialReadout.read (successorOrbit 0) := by
  simp

/-- Two distinct inputs can both lie outside one partial readout's domain. -/
theorem two_inputs_both_undefined :
    zeroInitialReadout.read (successorOrbit 1) =
      zeroInitialReadout.read (successorOrbit 2) := by
  simp

/-- The two output types of the demonstration family are genuinely different. -/
inductive DemoLeg where
  | initial
  | zeroFlag
deriving DecidableEq

def DemoOutput : DemoLeg → Type
  | .initial => ℕ
  | .zeroFlag => Bool

/-- A heterogeneous family with one total and one partial leg. -/
def demoFamily : OrbitReadoutFamily successorSystem where
  Index := DemoLeg
  Output := DemoOutput
  read := fun i κ =>
    match i with
    | .initial => some (successorInitial κ)
    | .zeroFlag =>
        if successorInitial κ = 0 then some true else none

@[simp]
theorem demoFamily_initial (n : ℕ) :
    demoFamily.read .initial (successorOrbit n) = (some n : Option ℕ) :=
  rfl

@[simp]
theorem demoFamily_zeroFlag_zero :
    demoFamily.read .zeroFlag (successorOrbit 0) =
      (some true : Option Bool) := by
  rfl

@[simp]
theorem demoFamily_zeroFlag_nonzero {n : ℕ} (hn : n ≠ 0) :
    demoFamily.read .zeroFlag (successorOrbit n) = none := by
  simp [demoFamily, hn]

/-- Equal undefined results at one leg do not imply family equivalence. -/
theorem same_undefined_leg_but_not_equivalent :
    demoFamily.read .zeroFlag (successorOrbit 1) =
        demoFamily.read .zeroFlag (successorOrbit 2) ∧
      ¬ demoFamily.ObservationallyEquivalent
        (successorOrbit 1) (successorOrbit 2) := by
  constructor
  · simp
  · apply demoFamily.not_observationallyEquivalent_of_read_ne .initial
    intro hread
    have hinitial : (1 : ℕ) = 2 := Option.some.inj hread
    exact (by decide : (1 : ℕ) ≠ 2) hinitial

/-- A defined/undefined difference in one leg refutes family equivalence. -/
theorem definedness_difference_breaks_equivalence :
    ¬ demoFamily.ObservationallyEquivalent
      (successorOrbit 0) (successorOrbit 1) := by
  apply demoFamily.not_observationallyEquivalent_of_read_ne .zeroFlag
  simp

/-- A heterogeneous family may leave every leg undefined. -/
def everywhereUndefinedFamily : OrbitReadoutFamily successorSystem where
  Index := DemoLeg
  Output := DemoOutput
  read := fun _ _ => none

/-- Equality of all partial readings need not reconstruct the orbit input. -/
theorem equivalent_but_distinct_orbits :
    everywhereUndefinedFamily.ObservationallyEquivalent
        (successorOrbit 1) (successorOrbit 2) ∧
      successorOrbit 1 ≠ successorOrbit 2 := by
  constructor
  · intro i
    cases i <;> rfl
  · exact successorOrbit_one_ne_two

/-- Even everywhere-defined constant readings need not separate inputs. -/
def everywhereConstantFamily : OrbitReadoutFamily successorSystem where
  Index := DemoLeg
  Output := DemoOutput
  read := fun i _ =>
    match i with
    | .initial => (some 7 : Option ℕ)
    | .zeroFlag => (some false : Option Bool)

theorem constant_defined_readings_equate_distinct_orbits :
    everywhereConstantFamily.ObservationallyEquivalent
        (successorOrbit 1) (successorOrbit 2) ∧
      successorOrbit 1 ≠ successorOrbit 2 := by
  constructor
  · intro i
    cases i <;> rfl
  · exact successorOrbit_one_ne_two

/-- No nonemptiness assumption is hidden in `ReadoutFamily`. -/
def emptyFamily : OrbitReadoutFamily successorSystem where
  Index := Empty
  Output := Empty.elim
  read := fun i => Empty.elim i

/-- An empty family gives vacuous observational equivalence. -/
theorem emptyFamily_equates_all (κ μ : ForwardOrbit successorSystem) :
    emptyFamily.ObservationallyEquivalent κ μ := by
  intro i
  exact Empty.elim i

end TwistJ.Models
