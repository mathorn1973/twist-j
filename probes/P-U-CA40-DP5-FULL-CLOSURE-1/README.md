# Full-pulse DP5/N384 numerical error account

PUBLIC NON-CANONICAL. Conditional L1 numerical evidence.
Original work Apache-2.0, A. M. Thorn, 2026-10-12.
Reservation: https://github.com/mathorn1973/twist-j/issues/1472.
Authority base: `5f54015ed8361e3a64cb10894397020ddfadd104`.

The sealed continuous-prefix comparison supported the unchanged DP5/N384
method on 195.3125 ns inside the first occupied segment. This new probe
attempts one complete 500-us program, preserving the same pulses,
compensated sine parent, coherent model coefficients, seven modes,
L8/G10 and all 120 unnormalized K3 thermal columns for both angles.
The user-authorized numerical campaign has a fixed 24-hour ceiling.

The numerical method is two DP5 halfsteps per certificate cell, with the
inherited three-point quintic Hermite curve and full-space defect account.
Every original segment boundary preserves the numerical state and its
cumulative certificate. Inactive intervals are identity in the moving
frame, even after earlier occupation. Final pair observables restore
branch-dependent linear frames at the common physical time 500 us.

The workload uses Linux, explicit AVX-512 and 80 bound workers. There is
one configuration and one numerical launch, with no automatic refinement,
retry, reset, phase fit or renormalization. State and certificate snapshots
are retained at the initial point and all 80 original segment endpoints.
These snapshots do not archive every intermediate quintic or certify a
complete all-input channel.

The precision target is total radius at most exactly 1/1000 for each of
the six selected final pair observables, including thermal and arithmetic
contributions. A separate test reports whether nonlinear discrepancy
from the full-linear reference is resolved. Wide but valid intervals,
timeout and invalid/incomplete execution are distinguished.

After all sources are publicly pinned and read back byte for byte, the
exact supporting gate is:

```sh
python3 probes/P-U-CA40-DP5-FULL-CLOSURE-1/verify.py
```

The numerical runner takes an executable built from that pin and a new
output directory:

```sh
python3 full_run.py --binary /absolute/path/full --output /absolute/path/new-directory
```

PREREG.md freezes the scope, budget and decisions. DERIVATION.md records
the cumulative and final-pair bounds; EXACT-DESIGN.md identifies the
limited role of exact fixtures. The exact gate does not execute or
independently reproduce the floating campaign. Actual first outcomes
will be preserved in RESULT.md/NUMERICAL.md when the campaign ends.

Physical source preservation still requires the ideal dark-source premise;
the unknown-source no-imprinting boundary remains. This is neither an ion
experiment nor an apparatus, energy/work or all-input source-channel
certificate. No Canon, registry, predecessor or workflow is changed.
