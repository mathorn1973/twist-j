# Result: full-measure estimator defined, pilot does not mix

**PUBLIC / NON-CANONICAL. Engineering disposition: INCONCLUSIVE_MOBILITY.**

The complete frozen pilot ran. The implementation audit and all 24 chains
completed with zero exits and empty stderr. All three volumes nevertheless
failed the prospectively fixed mobility requirements. This is not a
negative result for the sector-polarization lower bound or P1.

## What the records show

Every one of the 24 chains recorded zero complete replica round trips.
Every chain had at least one adjacent temperature edge with zero accepted
production exchanges. The required minima were eight round trips and
0.05 acceptance on every edge.

| L | Mode k | Target endpoint changes across the four chains | Complete replica round trips | Disposition |
|---|---|---|---|---|
| 4 | 1 | 116, 110, 119, 116 | 0, 0, 0, 0 | INCONCLUSIVE_MOBILITY |
| 4 | 2 | 12, 2, 54, 44 | 0, 0, 0, 0 | INCONCLUSIVE_MOBILITY |
| 6 | 1 | 5, 8, 5, 5 | 0, 0, 0, 0 | INCONCLUSIVE_MOBILITY |
| 6 | 2 | 0, 0, 0, 0 | 0, 0, 0, 0 | INCONCLUSIVE_MOBILITY |
| 8 | 1 | 0, 0, 0, 0 | 0, 0, 0, 0 | INCONCLUSIVE_MOBILITY |
| 8 | 2 | 0, 0, 0, 0 | 0, 0, 0, 0 | INCONCLUSIVE_MOBILITY |

The chain order is cold0, hot0, cold1, hot1. At L=8, for both modes,
the endpoint-zero occupancy was exactly (4096,4096,0,0). L=6,k=2 showed
the same pattern. Pooling these four trapped chains gives exactly 1/2
endpoint-zero occupancy solely because their initial endpoints were
balanced. It is not evidence of the correct equilibrium normalization.

The preserved analyzer retains the signed raw estimates under its
`NONINFERENTIAL_ESTIMATE` label. It withholds every sum-of-squares range:
all `D_empirical_engineering_interval` fields are null. Neither their
positive point values nor their finite-size differences support a lower
bound. The full unmodified output is in `ENGINEERING/analysis.json`.

## Mathematical result and remaining problem

At the finite-volume candidate-T scope of PROOF.md, the positive endpoint
measure has

\[
E I_0\ge\tfrac12,\qquad E T^2\le1,\qquad
\frac{ET}{EI_0}=-iC_{L,k}.
\]

These stationary-measure identities survive the failed sampling attempt.
They do not bound the time needed to sample that measure. The run shows
that this fixed temperature ladder and whole-seam endpoint proposal did
not pass their required transport checks within the frozen budget.
It does not prove that every such sampler fails or that the model has a
particular phase.

The declared execution is complete and consumed. Its source, seeds,
budget and thresholds are not extended, tuned or resumed. A successor
would need a new prospective pin and a demonstrated improvement in
transport before its contrast estimates could guide the proof attempt.

The positive thermodynamic sector bound, P1 and PHOTON-MASSLESS-PHASE
remain open. Public Canon v92 is unchanged. The numerical output has
ZERO scientific evidential weight; the written finite identities remain
candidate-T pending any separate promotion process.
