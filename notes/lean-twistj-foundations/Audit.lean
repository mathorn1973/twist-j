import TwistJ.Foundation.Orbit
import TwistJ.Models.CounterRegressions
import TwistJ.Models.ReadoutRegressions

/-!
NON-CANONICAL MANUAL AXIOM AUDIT.

This file prints the logical footprint of the first two foundation and
observation cuts. It is not an `A-LEAN-*` package, public evidence, or a
claim-status mechanism.
-/

set_option autoImplicit false

#print axioms TwistJ.Foundation.InternalCounter.tick_evolve
#print axioms TwistJ.Foundation.InternalCounter.no_positive_period
#print axioms TwistJ.Architecture.CounterCheckpointSystem.counter_index_evolve
#print axioms TwistJ.Architecture.CounterCheckpointSystem.fullState_nonreturn
#print axioms TwistJ.Architecture.publicCanonV32_counter_index_evolve
#print axioms TwistJ.Architecture.publicCanonV32_fullState_nonreturn
#print axioms TwistJ.Models.modularFive_period_five
#print axioms TwistJ.Models.same_checkpoint_different_full_state
#print axioms TwistJ.Models.constantCheckpoint_fullState_nonreturn
#print axioms TwistJ.Foundation.ForwardOrbit.stateAt_succ
#print axioms TwistJ.Observation.PartialReadout.not_isDefinedAt_of_isUndefinedAt
#print axioms TwistJ.Observation.ReadoutFamily.leg_read
#print axioms TwistJ.Observation.PartialReadout.toFamily_read
#print axioms TwistJ.Observation.ReadoutFamily.observationallyEquivalent_refl
#print axioms TwistJ.Observation.ReadoutFamily.observationallyEquivalent_of_eq
#print axioms TwistJ.Observation.ReadoutFamily.observationallyEquivalent_symm
#print axioms TwistJ.Observation.ReadoutFamily.observationallyEquivalent_trans
#print axioms TwistJ.Observation.ReadoutFamily.observationalSetoid
#print axioms TwistJ.Observation.ReadoutFamily.not_observationallyEquivalent_of_read_ne
#print axioms TwistJ.Observation.PartialReadout.toFamily_observationallyEquivalent_iff
#print axioms TwistJ.Models.undefined_ne_defined
#print axioms TwistJ.Models.two_inputs_both_undefined
#print axioms TwistJ.Models.same_undefined_leg_but_not_equivalent
#print axioms TwistJ.Models.definedness_difference_breaks_equivalence
#print axioms TwistJ.Models.equivalent_but_distinct_orbits
#print axioms TwistJ.Models.constant_defined_readings_equate_distinct_orbits
#print axioms TwistJ.Models.emptyFamily_equates_all
