import TwistJ.Observation.PartialReadout

/-!
# Heterogeneous families of partial readouts

Status: **NON-CANONICAL NOTE**.

Each index chooses its own output type. Outputs are compared only at the same
index, so no coercion between heterogeneous legs is installed.
-/

set_option autoImplicit false

namespace TwistJ.Observation

universe u v w

/-- A family of typed partial observations with index-dependent output types. -/
structure ReadoutFamily (Input : Type u) where
  Index : Type v
  Output : Index → Type w
  read : (i : Index) → Input → Option (Output i)

namespace ReadoutFamily

/-- Select one leg of a heterogeneous family as an ordinary partial readout. -/
def leg {Input : Type u} (R : ReadoutFamily.{u, v, w} Input)
    (i : R.Index) : PartialReadout.{u, w} Input where
  Output := R.Output i
  read := R.read i

@[simp]
theorem leg_read {Input : Type u} (R : ReadoutFamily.{u, v, w} Input)
    (i : R.Index) (x : Input) :
    (R.leg i).read x = R.read i x :=
  rfl

end ReadoutFamily

namespace PartialReadout

/-- Regard one partial readout as a one-leg family, without a coercion. -/
def toFamily {Input : Type u} (R : PartialReadout.{u, w} Input) :
    ReadoutFamily.{u, 0, w} Input where
  Index := Unit
  Output := fun _ => R.Output
  read := fun _ => R.read

@[simp]
theorem toFamily_read {Input : Type u} (R : PartialReadout.{u, w} Input)
    (i : (R.toFamily).Index) (x : Input) :
    R.toFamily.read i x = R.read x :=
  rfl

end PartialReadout

end TwistJ.Observation
