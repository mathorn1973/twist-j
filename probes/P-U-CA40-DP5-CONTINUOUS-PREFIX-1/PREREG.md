# Fixed short continuous-prefix DP5/N384 versus RK4/N512 comparison

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering evidence.
Original work Apache-2.0, A. M. Thorn, 2026-10-12.

```text
probe_id: P-U-CA40-DP5-CONTINUOUS-PREFIX-1
branch: probe/P-U-CA40-DP5-CONTINUOUS-PREFIX-1
public_issue: https://github.com/mathorn1973/twist-j/issues/1470
authority_base: 200ebb118bc62b02c634afa9e68bd91a7de3191b
owner: A. M. Thorn, coordinated numerical engineering session
```

The exposed DP5/N384 predecessor passed its local reset-window screen.
Those data motivate this new unblinded study but do not establish error
accumulation along a trajectory. No scientific candidate is imported or
executed before all new sources are committed, pushed and publicly read
back. No pilot, post-pin repair, retry, adaptation or long run is admitted.

## 1. Model and frozen question

Retain the exact same compensated sine parent, full two-frequency linear
reference, coherent force coefficients and moving-frame residual:

```text
H_S/hbar = 2u sum_i s_i [sin(chi_i+X_i)-sin chi_i],
H_L/hbar = 2u sum_i s_i cos(chi_i) X_i,
R_z = 2u sum_i s_i [sin(chi_i+m_i+X_i)-sin chi_i
                    -cos(chi_i)(m_i+X_i)],
i dot(W_z) = R_z W_z,   U_S,z = U_L,z W_z.
```

input.json has SHA-256
`ca6b286c9e6d45795677b05e09fbe1b38043c8ff8369b57b652c83195a156d53`.
Decimal tokens are exact rational inputs. Keep coherent coefficients
derived from the common model, not the legacy rounded eta table; all
seven modes, five 100-us loops, sixteen 6.25-us constant-amplitude
segments per loop, ideal electronic cycle and absolute physical clock.
Do not retune pulses or change physical parameters.

The question is whether the accumulated DP5/N384 certificate is no larger
than the accumulated RK4/N512 certificate at each of four matched
checkpoints, while taking less measured program end-to-end time. Report
how each accumulated bound grows. The compensated parent is the model
being tested; an omitted uncompensated unary phase is not silently treated
as a common global phase at intermediate times.

## 2. Methods and numerical arithmetic

| Arm | N certificate cells per original segment | Method | Dense curve | Substeps / RHS per cell |
|---|---:|---|---|---|
| A | 512 | RK4 | QUINTIC_ENDPOINT_DIRECTIONAL_FD | 1 / 9 |
| C | 384 | DP5_TWO_HALF_STEPS | QUINTIC_THREE_POINT_HERMITE | 2 / 13 |

DP5 uses two consecutive halfsteps per cell, sharing the derivative of the
actually stored midpoint, and a quintic through start/midpoint/end values
and derivatives. Recompute the first derivative every cell. Its eleven
distinct normalized stage times are
`0,1/10,3/20,2/5,4/9,1/2,3/5,13/20,9/10,17/18,1`.
Baseline retains delta=h/128 acceleration estimates and same-segment
one-sided analytic extension. There is no adaptive controller, embedded
error acceptance, phase fit or renormalization.

The DP5 coefficient table, step and quintic formulas are inherited from
the sealed predecessor without modification. Attribution of the weights:
Hairer and Wanner's [DOPRI5 source, CDOPRI](https://www.unige.ch/~hairer/prog/nonstiff/dopri5.f),
accessed by the predecessor on 2026-10-11. No Fortran solver or its dense
output/adaptive controller is copied or run.

kernel.cpp retains SHA-256
`9ba07011d2405e609eb84be8cb5d7781bb06b7cc50be53fbd5304ac5fa93c3f2`.
input.json, prepare_input.py, validated_model.hpp/.cpp and dp5_tableau.hpp
also remain byte-identical. Adapt only the short harness, its layout,
comparator, bounded runner and supporting proofs/checks. L8/G10, dimensions
6435/19448, K3, sixteen Gauss nodes per cell, outside-guard tail, analytic
continuum allowance, endpoint jumps and norm-ball certifier are unchanged.
Stored curve coefficients are exact dyadics for certification. Do not
weaken the bound or alter its reduction order. Bypass the original long
main; no reachable option enables it.

Use GNU C++ 14.2.0, MPFR 4.2.2, GMP 6.3.0 and common flags
`-O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math -fno-tree-vectorize`.
Build all three executables from the public pin. Record commands and
binary hashes. Require binary64, finite data, gradual underflow,
FTZ/DAZ disabled, inherited directed-arithmetic and runtime fixtures.
Baseline uses its original seven stage nodes and no DP5 workspace;
candidate uses eleven stage nodes.

## 3. One trajectory, four checkpoints

Cases 0,1,2 have labels (4,3),(4,4),(1,1) at +4*pi/5; cases 3,4,5 repeat
them at -4*pi/5. Keep all 120 thermal basis columns of total occupation
at most three with their inherited ordering and unrenormalized weights.

For each case start at the first occupied segment, q=0, occupied ordinal
zero. Cases 0,1,3,4 first activate at original segment 16 (100 us), cases
2,5 at segment 64 (400 us). All preceding active indicators are zero:
both H_S and H_L, their residual and the linear history vanish there.
Thus a single initial W-frame |n> is the actual declared model's initial
state continued through that inactive prefix, not a reset mid-trajectory.
Retain the absolute time throughout.

Advance four adjacent blocks from that point. With dt=6.25 us, checkpoint
k=1,2,3,4 is at t_onset+k*dt/128. The block duration is exactly
48.828125 ns and the total active duration 195.3125 ns. All blocks remain
inside the first occupied original segment; none crosses an amplitude
switch. The two arms have identical physical times for the same case.
Different cases do not share one absolute endpoint; no simultaneous
intercase coherence, full thermal state or final gate value is computed.
In particular inherited prepared.final/delta/rotation describe the full
500-us program and must not be used as prefix endpoint data.

| Checkpoint k | A cumulative cells / substeps | C cumulative cells / substeps |
|---:|---:|---:|
| 1 | 4 / 4 | 3 / 6 |
| 2 | 8 / 8 | 6 / 12 |
| 3 | 12 / 12 | 9 / 18 |
| 4 | 16 / 16 | 12 / 24 |

Per block A uses 36 RHS calls and 64 Gauss nodes; C uses 39 RHS calls and
48 Gauss nodes. Initialize y and Certificate once per (case,batch), outside
the checkpoint loop. Carry both unchanged into each following block;
checkpoint output only copies them. Each polynomial's initial coefficient
must equal the actual incoming dyadic y. Charge the final polynomial-to-
stored-endpoint jump once per cell, including at checkpoint boundaries.
The unitary defect proof gives an additive cumulative bound with no
amplification factor. Never sum already cumulative checkpoint bounds.

There are 90 trajectories (6 cases, 15 eight-lane batches), 360 snapshots,
90 initializations and 270 checked checkpoint transitions per child.
Before advancing a later block, compare y and Certificate byte-exactly to
their previous saved snapshots. Check cumulative components for monotone
nondecrease. Detect state replacement, certificate reset, phase fitting
or normalization as integrity failures. Exact supporting fixtures test
state/certificate resets, snapshot aliasing, an incorrect polynomial start
and double counting. Source review and custody separately exclude phase
fitting and normalization. The fixtures do not certify the floating
program on their own.

Use fixed heavy-first task order cases [1,2,4,5,0,3], each with ascending
batches; output remains canonical checkpoint/case/column order. This is a
predeclared scheduling permutation only. Every child does 1440 A or 1080 C
certified cells, as much numerical cell work as the previous four-window
panel. No speed is guaranteed from that count.

Keep four checkpoint endpoints for every case and column: 2880 rows,
296524800 endpoint bytes and 276480 twelve-field component bytes. Layout
is versioned CONTINUOUS_PREFIX_CHECKPOINTS_V1, scope
SHORT_CONTINUOUS_PREFIX_ONLY. Endpoint order is
CHECKPOINT,CASE,COLUMN,BASIS,RE/IM; component order is
CHECKPOINT,CASE,COLUMN,FIELD. No column is discarded.

Require Linux, AVX-512F/DQ/VL, logical CPUs 0..79, two packages,
40 physical cores and both SMT siblings; 80 workers, singleton OpenMP
places, disabled dynamic/nested teams, full worker/CPU/place coverage and
no observed worker migration.

## 4. First outcomes and fixed short limits

Run A,C,C,A, two fresh observations per arm. At most 300 seconds per child
and 1200 seconds for the full panel including model preparation,
propagation, serialization, validation, custody and comparisons. Launch
only inside the remaining deadline; use the smaller remaining budget.
At most 90 seconds per comparator inside that same panel budget. Bounded
cleanup and final evidence preservation may extend the final wall receipt.
No pilot, retry, discarded warmup, adaptation or automatic extension.

Compare pair (1,2) after child 2 and pair (4,3) after child 4, always A
left/C right. Require matching input, basis, absolute physical checkpoints
and method-aware layouts. Compare actual bytes of same-arm endpoint,
component, basis, immutable metadata and layout files, including signed
zero: C runs (2,3), A runs (1,4). Mismatch is fatal REPEATABILITY_FAILED.
Retain every attempted launch, error, timeout, cleanup and partial
artifact. Missing output is not zero and output directories must be new.

The twelve fields are guard, tail, continuum, jumps, total,
sampled_time_node_L2, sampled_projection_node_L2,
sampled_arithmetic_node_L2, maximum_node_bound, maximum_norm_error,
endpoint_norm_squared_lo, endpoint_norm_squared_hi. Arithmetic is already
included in guard. Node time/projection diagnostics lack independent
continuum allowances and must not be added again to total.

## 5. Frozen decisions and growth report

For the same case, initial thermal column and checkpoint, both arms
approximate the same exact prefix state. The certificate entails
||y_A-y_C|| <= e_A+e_C. Directed arithmetic encloses the exact dyadic
endpoint-difference norm as [D_lo,D_hi]; R=up(e_A+e_C).

```text
D_hi <= R: COMPATIBLE;
D_lo > R: INCONSISTENT;
otherwise: UNRESOLVED.
```

No tolerance or phase alignment. INCONSISTENT stops as numerical-integrity
failure, not physical falsification. UNRESOLVED allows the rest of the
fixed work but prevents joint PASS. Both pairs must have all 2880 rows
COMPATIBLE. Large bounds can make compatibility easy; it is not accuracy.

Separate engineering criteria, decided on exact Fractions of saved
binary64 values:

1. e_C <= e_A at every checkpoint/case/column in both pairs. If e_A=0,
   only e_C=0 passes. No multiplicative or additive allowance.
2. Sum of the two C program end-to-end times is strictly less than the
   corresponding sum for A. Equality fails; no minimum speed factor.

An engineering failure does not discard later fixed observations.
Integrity, model, continuity or custody failures stop after recording.
Joint PASS requires both criteria, complete compatible comparisons,
repeatability, uninterrupted cumulative state/error accounts and custody.

Report cumulative bounds and their components at all 24 checkpoint/case
groups, each angle and both observations. Report exact-dyadic E_k/E_1
ratios, increase from the preceding checkpoint and E_4/E_1 with zero
denominators separately identified. These are growth of computed upper
bounds, not ratios of actual errors; subtraction of cumulative bounds is
not an independently certified interval error. No assumed linear growth
law, growth-factor acceptance threshold or full-pulse extrapolation.

Also report the inherited focused column 36, occupation (0,0,0,0,0,0,3),
cases 0 and 3, at all checkpoints. No special exemption. Comparing the
first checkpoint with predecessor window zero is an additional saved-data
continuity audit, not replacement of fresh A/C observations or acceptance.

Report all four preparation/kernel/program/child timings. Medians of two
observations are descriptive means, with no statistical confidence claim.
Kernel time includes setup, OpenMP, logging and snapshots. Program time
also includes model preparation, fixtures and serialization; child wall
adds process overhead. Driver custody/comparison cost is separate.
A/C jointly changes endpoint method, dense curve, substep count and
certificate density; the result does not isolate integration order.

## 6. Pin, supporting gate and disposition

Action layer L1 only. Publicly pin/read back all fifteen sources plus
SOURCE_SHA256SUMS before scientific execution or candidate imports:

```text
README.md PREREG.md DERIVATION.md EXACT-DESIGN.md verify.py
input.json prepare_input.py validated_model.hpp validated_model.cpp
kernel.cpp higher_order.hpp dp5_tableau.hpp benchmark.cpp compare.cpp
integrator_run.py
```

The standard-library exact supporting gate has a 600-second limit,
exit zero, empty stderr and deterministic ASCII/LF stdout. It checks
algebra/geometry/negative fixtures, not numerical performance or actual
floating trajectory error. Create EXPECTED.txt from its first actual
output only, with neutral receipt RUN.md. If it never completes, follow
abandoned-pin policy. No predicted stdout is used as observed evidence.

The driver binds all three public-checkout binary hashes, serialized
input and source manifest before/after each attempted child/comparator,
including failures. Private records preserve raw states and receipts;
public reports omit private paths, hostnames, raw logs and credentials.
Preserve the first outcome at conservative status C, including negative,
unresolved or incomplete numerical results. The identifier is then sealed;
no repair, resumed run, retuning or automatic successor is permitted.

This short prefix does not close the complete-pulse error account, final
coherences, all-input channel, source/reference preservation, apparatus
realization or energy/work account. Exact-darkness and unknown-source
no-imprinting boundaries remain unchanged. No long run is authorized.
