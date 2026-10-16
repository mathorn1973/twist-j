# One bounded full-pulse DP5/N384 campaign

PUBLIC NON-CANONICAL. Conditional L1 mathematical and numerical evidence.
Original work Apache-2.0, A. M. Thorn, 2026-10-12.

```text
probe_id: P-U-CA40-DP5-FULL-CLOSURE-1
branch: probe/P-U-CA40-DP5-FULL-CLOSURE-1
public_issue: https://github.com/mathorn1973/twist-j/issues/1472
authority_base: 5f54015ed8361e3a64cb10894397020ddfadd104
owner: A. M. Thorn, coordinated numerical session
```

The exposed short continuous-prefix outcome motivates this new unblinded
attempt. It established only 195.3125 ns within one occupied segment, not
full-pulse error closure. The earlier sealed ERROR-CLOSURE and BALL-CLOSURE
attempts remain incomplete and are not resumed. Freeze this complete new
source set publicly before importing or executing its scientific code.
Static source review and compilation are allowed before the source pin.

## 1. Model and equation

Keep the exact same decimal-rational input and compensated sine parent,
full two-frequency linear reference, coherent force coefficients and
moving-frame residual:

```text
H_S/hbar = 2u sum_i s_i [sin(chi_i+X_i)-sin chi_i],
H_L/hbar = 2u sum_i s_i cos(chi_i) X_i,
R_z = 2u sum_i s_i [sin(chi_i+m_i+X_i)-sin chi_i
                    -cos(chi_i)(m_i+X_i)],
i dot(W_z) = R_z W_z,   U_S,z = U_L,z W_z.
```

input.json retains SHA-256
`ca6b286c9e6d45795677b05e09fbe1b38043c8ff8369b57b652c83195a156d53`.
No pulse retuning, rounded-eta substitution or model-parameter adaptation
is allowed. Five 100-us electronic loops each contain sixteen 6.25-us
constant-amplitude segments. Preserve the absolute clock, ideal electronic
cycle and all seven harmonic modes through the common endpoint T=500 us.
The compensated parent is the declared model; an omitted uncompensated
unary phase is not silently treated as common global phase.

## 2. Code, arithmetic and inherited certificate

Run only DP5_TWO_HALF_STEPS at N=384 certificate cells per original
occupied segment. Each cell has two consecutive halfsteps and the
inherited three-point Hermite quintic, using 13 RHS evaluations and
sixteen Gauss certificate nodes. Recompute each cell's first derivative;
there is no adaptive controller or FSAL carry across cells or switches.
The DP5 weights and step/quintic formulas are unchanged from the sealed
continuous-prefix probe. Their coefficient attribution is Hairer and
Wanner's [DOPRI5 source](https://www.unige.ch/~hairer/prog/nonstiff/dopri5.f),
already consulted by the predecessor; no Fortran adaptive solver is run.

kernel.cpp, input.json, prepare_input.py, validated_model.hpp/.cpp,
dp5_tableau.hpp and higher_order.hpp remain byte-identical to that predecessor. The original
kernel main is bypassed: the new full.cpp harness performs the fixed DP5
trajectory and retains the inherited full-time restoration and interval
Gram account. Its full-word layout helpers are local to full.cpp;
DP5 step and quintic formulas stay fixed.

Dynamic cutoff L=8 and guard G=10 have dimensions 6435 and 19448.
Use the existing finite-guard cancellation, infinite creation tail,
degree-15/rho-6 analytic continuum allowance, norm-ball arithmetic and
polynomial-to-stored-endpoint jumps. Arithmetic is already in the guard;
sampled time/projection/arithmetic diagnostics must not be added again.
Stored polynomial coefficients are exact dyadics for the certificate.
The unitary defect bound adds contributions without a Gronwall factor.

GNU C++14.2, MPFR4.2.2 and GMP6.3 are the selected environment. Compile
with -O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math
-fno-tree-vectorize and the inherited explicit AVX-512 target functions.
Require binary64, nearest rounding, finite values, gradual underflow,
FTZ/DAZ disabled and all inherited runtime arithmetic/displacement
fixtures. Invalid intervals, NaN, overflow or failed fixtures are fatal.
Record compiler commands, versions and executable/source/input hashes.

## 3. Carrier, continuous execution and checkpoints

All seven modes start in independent thermal states with nbar=1/20.
Retain every total-occupation K<=3 column: 120 columns, exact weights
(20/21)^7(1/21)^N without renormalization. The omitted mass is exactly
680046581/794280046581. The initial bus is independent of electronic
registers and their external reference under the inherited model.

Cases 0,1,2 have labels (4,3),(4,4),(1,1) at +4*pi/5; cases 3,4,5 repeat
them at -4*pi/5. Run all six with eight SIMD columns per batch, fifteen
batches per case and 90 tasks. Fixed task order is cases [1,2,4,5,0,3]
with ascending batches. This schedule changes no physical chronology.
Cases 0/3 have 32 occupied segments and 12288 cells each; the other four
have 16 occupied segments and 6144 cells each. Across all batches there
are 737280 certified eight-column cells, 9584640 RHS evaluations and
11796480 Gauss-node evaluations. There is no cutoff/grid ladder.

Initialize each task's state and Certificate once at t=0. Traverse all
80 original segments in order. An inactive segment has R=0 and carries
both objects unchanged even after an earlier active segment. At finite
amplitude jumps, the state remains continuous and the next segment uses
fresh right-side Hamiltonian data. Each cell's poly[0] equals the actual
incoming state exactly; charge its final endpoint jump once. There is
no state reset, normalization, branch-phase fit or thermal reweighting.

Retain versioned state/certificate snapshots at t=0 and each original
segment endpoint. Expected totals are 90 initializations, 7290 snapshots,
7200 segment carry checks, 1920 active task-segments and 5280 inactive
identity task-segments. Atomic completed checkpoint records distinguish
complete payloads from interrupted writes. Check snapshot identity against
the in-memory state and certificate before the next segment; retain
cellwise cumulative monotonicity and polynomial-start assertions. Emit
progress within active segments as well as at their boundaries. Progress
alone is not a saved-state checkpoint or a final error certificate.

All branches' final W states are transported through inactive suffixes
to T=500 us. Only then restore their branch-dependent exact linear
frames, displacements and Weyl phases for common-time pair observables.
Intermediate snapshots are branch/column data, not final coherences.
The snapshot archive omits intermediate quintic/node arrays; independent
re-audit of each intermediate cell would require deterministic replay.

Require Linux, AVX-512F/DQ/VL, two CPU packages, 40 physical cores,
80 logical CPUs with both SMT siblings, singleton OMP_PLACES on CPUs
0..79, disabled dynamic/nested teams and eighty workers with complete
CPU/place coverage and no observed migration. Set other threaded
libraries to one worker. Before launch require at least 16 GiB free
output storage and 64 GiB MemAvailable. These are resource gates, not
guarantees of peak memory or execution time. No concurrent campaign is
deliberately started.

## 4. Budget, failures and preserved first outcome

One fixed configuration, one numerical launch. The numerical runner has
86400 seconds from entry, including preparation, propagation, output
validation and custody checks. Reserve the final 300 seconds inside that
budget for postprocessing; the child receives the positive remaining
time minus that reserve. No automatic extension, restart, resume, retry,
pilot or discarded warmup is allowed. The separate first exact supporting
gate has a 600-second limit and occurs before the numerical runner.

On timeout or fatal integrity/arithmetic/carry/custody failure, terminate
only the owned process group. Bounded cleanup may take up to 30 additional
seconds; writing a minimal failure receipt afterward performs no further
scientific work. Preserve every attempted launch, error, interruption and
all complete/partial output. Invalid/missing results are NOT_CERTIFIED.
An explicit user/coordinator resource stop is permitted only as a recorded
incomplete outcome, never a precision success or permission to rerun.
A large intermediate upper bound alone is not a physical falsification
and is not an automatic proof of final-goal impossibility.

Source/input/executable custody is checked before and after the attempt,
including failure. Source files and the public source manifest remain
immutable after pinning. No data-dependent numerical change is allowed.

## 5. Observables, precision and discrepancy decisions

For all three unordered branch pairs per sign, retain the complex
unnormalized sine coherence interval and full-thermal linear reference.
Use the inherited restored-frame Gram bound in DERIVATION.md, including
the actual norms of approximate endpoint columns. Each pair reports
numerical, thermal, arithmetic and total radii and a final trace-distance
interval clipped to [0,1]. Thermal omission contributes p_tail/2.
The total radius includes the center-evaluation halfwidth; expand the
already interval-valued center only by numerical plus thermal error so
that arithmetic is not counted twice.

The precision goal is PASS only if all six total radii are <= exactly
1/1000. Otherwise valid completed bounds have precision UNRESOLVED.
Separately classify every pair's discrepancy against exactly 1/1000:
lower > threshold means resolved above, upper <= threshold means bounded
at or below, and overlap means UNRESOLVED. A resolved above-threshold
pair for each sign establishes the selected nonlinear discrepancy for
both angle envelopes. Report the other pairs too. Wide valid intervals
can resolve discrepancy while missing the separate precision target.

All threshold comparisons use exact Fractions of saved binary64 values.
There is no comparison tolerance or interval-midpoint decision. Missing
or invalid output/custody yields NOT_CERTIFIED rather than a precision
or discrepancy conclusion. Reaching a budget limit never changes the
threshold, and upper bounds are not observed true state errors.

## 6. Exact support, action layer and disposition

Action layer L1 only. Before any scientific execution, publicly commit,
push and read back the complete source set and SOURCE_SHA256SUMS:

```text
README.md PREREG.md DERIVATION.md EXACT-DESIGN.md verify.py
input.json prepare_input.py validated_model.hpp validated_model.cpp
kernel.cpp higher_order.hpp dp5_tableau.hpp full.cpp full_run.py
```

The exact standard-library gate audits algebra, piecewise geometry,
continuity/negative fixtures and final-pair accounting. It does not run
the floating solver or certify numerical performance. Require exit zero,
empty stderr and deterministic ASCII/LF stdout; preserve its actual first
output as EXPECTED.txt with RUN.md. No predicted output is substituted.
If no exact first gate completes, follow abandoned-pin policy.

After the numerical attempt, preserve its positive, negative, unresolved
or incomplete first outcome in RESULT.md/NUMERICAL.md at conservative
status C. Do not change the Canon, registry, workflows or sealed prior
probes. Exact CI replay is not independent numerical replication.

Five protected electronic registers and their external-reference marginal
remain unchanged only under the ideal exact-zero-response premise. The
unknown-complete-source plus informative-record obstruction is unchanged.
This attempt has no physical ion experiment, imperfect spectator control,
heating/scattering, radial motion, complete work-reservoir account or
all-input source/reference channel conclusion.
