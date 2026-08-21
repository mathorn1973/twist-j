import TwistJ.Foundation.Orbit
import TwistJ.Models.CounterRegressions

/-!
NON-CANONICAL MANUAL AXIOM AUDIT.

This file prints the logical footprint of the first foundation theorems. It is
not an `A-LEAN-*` package, public evidence, or a claim-status mechanism.
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
