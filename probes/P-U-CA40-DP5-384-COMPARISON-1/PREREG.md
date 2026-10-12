# Fixed short DP5/N384 versus RK4/N512 comparison

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering evidence.
Original work Apache-2.0, A. M. Thorn, 2026-10-12.

```text
probe_id: P-U-CA40-DP5-384-COMPARISON-1
branch: probe/P-U-CA40-DP5-384-COMPARISON-1
public_issue: https://github.com/mathorn1973/twist-j/issues/1468
authority_base: 99094c18e668213a44532b7fb6053ca434293e9d
owner: A. M. Thorn, coordinated numerical engineering session
```

The sealed DP5/N256 predecessor is exposed design information. It passed
consistency and repeatability, improved the observed end-to-end timing,
and failed the strict C/A bound condition at two of 2880 columns in each
comparison. This is a new, unblinded short study, not an independent
external replication or a repair of that outcome. No scientific candidate
is imported or executed before all new sources are publicly pinned and
read back. No pilot, post-pin repair, retry, adaptation or longer trajectory
is admitted.

## 1. Fixed model and question

Use the unchanged compensated sine parent, full two-frequency linear
reference, coherent coefficients and moving-frame residual:

```text
H_S/hbar = 2u sum_i s_i [sin(chi_i+X_i)-sin chi_i],
H_L/hbar = 2u sum_i s_i cos(chi_i) X_i,
R_z = 2u sum_i s_i [sin(chi_i+m_i+X_i)-sin chi_i
                    -cos(chi_i)(m_i+X_i)],
i dot(W_z) = R_z W_z,   U_S,z = U_L,z W_z.
```

input.json retains SHA-256
`ca6b286c9e6d45795677b05e09fbe1b38043c8ff8369b57b652c83195a156d53`.
Its decimal tokens are exact rational inputs. Derive coherent force
coefficients as before rather than substituting the legacy rounded eta
table. Keep five 100-us loops, sixteen 6.25-us constant-amplitude segments
per loop, the ideal electronic cycle and the absolute physical clock.

The question is whether DP5/N384 has no larger certificate in any matched
local column while taking less measured program end-to-end time than
RK4/N512. Neither the pulses nor physical parameters are optimized.

## 2. Fixed methods and arithmetic

| Arm | N | integrator | dense_curve | Substeps / RHS per cell |
|---|---:|---|---|---|
| A | 512 | RK4 | QUINTIC_ENDPOINT_DIRECTIONAL_FD | 1 / 9 |
| C | 384 | DP5_TWO_HALF_STEPS | QUINTIC_THREE_POINT_HERMITE | 2 / 13 |

N counts certificate cells per original 6.25-us segment. C performs two
consecutive DP5 halfsteps inside each cell, sharing the actual midpoint
derivative. Values and actual derivatives at cell start, midpoint and end
determine its single quintic Hermite curve. Recompute the initial RHS for
every cell: the frozen count is 13. Do not substitute an internal same-time
stage for the derivative of the stored midpoint or endpoint. There is no
embedded-error controller, normalization, phase fit or adaptive step.

The eleven distinct normalized DP5 stage times remain

```text
0, 1/10, 3/20, 2/5, 4/9, 1/2, 3/5, 13/20, 9/10, 17/18, 1.
```

They lie in the same constant-amplitude segment with its one-sided endpoint
convention. A retains the inherited acceleration estimate with delta=h/128
and the same-segment extension. DP5 weights and the original step/quintic
implementation are inherited unchanged from P-U-CA40-DP5-COMPARISON-1.
The weights are attributed to Hairer and Wanner's
[DOPRI5 source](https://www.unige.ch/~hairer/prog/nonstiff/dopri5.f), CDOPRI,
accessed in the predecessor on 2026-10-11. No Fortran solver, adaptive
controller or supplied dense-output implementation is copied or executed.
DERIVATION.md and EXACT-DESIGN.md state the exact supporting identities.

kernel.cpp retains SHA-256
`9ba07011d2405e609eb84be8cb5d7781bb06b7cc50be53fbd5304ac5fa93c3f2`.
input.json, prepare_input.py, coefficient table, model formulas and the
inherited certifier remain unchanged. Adapt only the two-arm interface,
fixed N384 windows, metadata, supporting checks and bounded driver.
Compile-time selection retains baseline's seven-node layout and original
preparation sequence; candidate uses eleven nodes and no old finite-
difference nodes. Baseline allocates no extra DP5 workspace.

Keep L=8, G=10, dimensions 6435/19448, K=3, degree-five curves, sixteen
Gauss nodes per cell, outside-guard tail, analytic continuum allowance,
endpoint jumps and norm-ball arithmetic. Stored curve coefficients are
exact dyadics for certification. Do not weaken the bound or change
certifier reduction order. The harness bypasses the original long main
and executes only the frozen local cells.

Use GNU C++ 14.2.0, MPFR 4.2.2, GMP 6.3.0 and OpenMP with common flags
`-O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math -fno-tree-vectorize`
and the frozen method selector. Build all three executables from the
publicly pinned checkout and retain commands and binary hashes. No private
source export is needed. Centers use nearest binary64; bounds use the
prescribed directed arithmetic. Finite values, gradual underflow, disabled
FTZ/DAZ and all inherited runtime fixtures are required.

The standard-library exact gate has a 600-second ceiling, exit zero, empty
stderr and deterministic ASCII/LF stdout. It does not execute the numerical
kernel or establish measured accuracy/performance. EXPECTED.txt is created
only from its actual first output after the complete pin/readback.

## 3. Carrier, windows and focused prior failures

Keep all seven modes and all 120 basis columns with total occupation at
most three in the inherited ordering. Do not discard or renormalize any
column. Thermal weights remain recorded, but no full thermal coherence or
thermal-weighted global error summary is claimed.

Cases 0,1,2 are (4,3),(4,4),(1,1) for +4*pi/5. Cases 3,4,5 repeat them for
-4*pi/5. Cases 0 and 3 have S=32 occupied amplitude segments; the others
have S=16. Freeze the occupied-segment ordinals and cell starts:

```text
j = [0, floor((S-1)/3), floor(2*(S-1)/3), S-1].
S=32: j=[0,10,20,31];  S=16: j=[0,5,10,15].
q_512 = [0,256,256,508], cells_A=4.
q_384 = [0,192,192,381], cells_C=3.
q_N = [0,128,128,254] * N / 256, with exact multiplication before division.
```

Window w starts at prepared occupied-cell index j[w]*N+q_N[w]. Require
exact grid alignment. Every window has duration 6.25 us / 128 =
48.828125 ns, with identical absolute physical endpoints in both arms.
None crosses an amplitude switch; the last ends at one. Per window, A
uses four RK4 steps, 36 RHS calls and 64 certificate Gauss nodes; C uses
six DP5 halfsteps, 39 RHS calls and 48 certificate Gauss nodes. This count
distinction must appear in method metadata and interpretation.

Every window independently starts from W-frame |n> with zero local error
accumulators. Its physical input is U_L,z(t0)|n>, not the nonlinear state
previously reached at t0 or an unshifted laboratory thermal state. Preserve
the full original analytic displacement/phase history and absolute clock.
Do not chain windows or their errors. This panel does not cover accumulated
nonlinear spreading/correlations and cannot certify the complete pulse.

Each child has 360 tasks (four windows, six cases, fifteen eight-lane
batches) and 2880 local column endpoints. Binary order is
WINDOW,CASE,COLUMN,BASIS,RE/IM for states and WINDOW,CASE,COLUMN,FIELD for
components. Each complete endpoint artifact is 296524800 bytes; each
twelve-field component artifact is 276480 bytes.

The two prior failing states are explicitly frozen as window 0, cases 0
and 3, column 36, occupation (0,0,0,0,0,0,3). Check both occupation and
column identity. Retain their full A/C endpoint vectors and report local
totals, paired ratios, component diagnostics and compatibility decisions
in both observations.
They receive no exemption or extra tolerance. Passing only these two does
not pass the all-2880-column screen; prior values are context, not a
replacement for fresh A observations.

Require Linux, AVX-512F/DQ/VL, affinity to logical CPUs 0..79, two packages,
40 physical cores and both SMT siblings. Use 80 workers with singleton
OpenMP places, disabled dynamic/nested teams and common affinity policy.
Check complete worker/CPU/place coverage and observed migrations.

## 4. First-outcome protocol and resource limits

Run exactly four fresh children A,C,C,A, two observations per arm. Each
child has at most 300 seconds or the remaining campaign budget, whichever
is smaller. The runner has 1200 seconds total including preparation,
propagation, serialization, validation, custody and comparison. No launch
may occur after its deadline. Bounded cleanup and final evidence
preservation may extend the final wall receipt. No pilot, retry, discarded
warmup, retuning, adaptation or automatic longer follow-up is allowed.

After child 2 compare pair (1,2); after child 4 compare pair (4,3). A is
always left and C right. Each comparator has at most 90 seconds within the
same total budget. Require matching physical windows, input, basis, method
metadata and binary layout. Retain all attempted launches, exits, errors,
timeouts, cleanup, stdout/stderr and incomplete artifacts. Missing output
is not zero. Do not reuse output directories.

Repeat checks compare C runs (2,3) and A runs (1,4). Compare actual bytes
of endpoint/component bodies, basis, immutable metadata and layout, with
signed zero included. All twelve component fields are retained:

```text
guard, tail, continuum, jumps, total,
sampled_time_node_L2, sampled_projection_node_L2,
sampled_arithmetic_node_L2, maximum_node_bound, maximum_norm_error,
endpoint_norm_squared_lo, endpoint_norm_squared_hi.
```

Same-arm mismatch is fatal REPEATABILITY_FAILED after its record is saved.
Runtime, model and custody failures likewise stop. Sampled arithmetic is
already in guard. Sampled time/projection diagnostics have no independent
continuum allowance and must not be added again to the total.

## 5. Frozen decisions

Both arms approximate the same exact local solution, so the conditional
defect proof implies ||y_A-y_C|| <= e_A+e_C. Enclose the exact dyadic
endpoint-difference norm by [D_lo,D_hi] and set R=up(e_A+e_C):

```text
D_hi <= R: COMPATIBLE;
D_lo >  R: INCONSISTENT;
otherwise: UNRESOLVED.
```

There is no tolerance, normalization or phase fit. INCONSISTENT is fatal
numerical-integrity failure, not physical falsification; preserve and stop.
UNRESOLVED permits the remaining fixed work but prevents compatibility
PASS. Both comparisons must classify every one of their 2880 columns
COMPATIBLE. Large bounds can make this easy; consistency is not accuracy.

Freeze separate engineering screens:

1. **Bound non-increase:** e_C <= e_A on every matched column in both
   pairs (1,2) and (4,3), using exact Fractions of the saved binary64
   bounds. If e_A=0 only e_C=0 passes. Report positive-over-zero separately
   without nonfinite JSON. There is no multiplicative or additive allowance.
2. **End-to-end improvement:** C's two-observation program end-to-end
   median is strictly smaller than A's. Compare exact Fraction sums of
   the two stored timings; division by two cancels. Equality fails and
   there is no required speed factor.

An engineering failure continues the remaining fixed panel unless an
integrity failure occurs. Completion alone is not a passed screen. Joint
PASS requires both screens, intact custody, byte repeatability and full
compatibility; UNRESOLVED or recorded failure cannot yield joint PASS.

Report all four timings and both observations per arm. Their median is a
descriptive arithmetic mean, not a confidence interval or significance
test. Preserve preparation anomalies. Kernel time includes workspaces,
OpenMP startup/barriers, numerical work and progress logging. Program
end-to-end also includes preparation, fixtures and serialization; child
wall adds process overhead. Runner custody/comparison time is separate.

Report all 24 window/case groups, each angle's 1440 local columns, paired
bound ratios/components, and the two focused earlier failures. Upper-bound
ratios are not true-error or infidelity ratios. A/C changes integrator,
dense curve, substep count and certificate grid together; this two-arm
panel does not isolate those effects or establish empirical convergence
order. Do not reinterpret the old N256 timing as a fresh matched arm.

## 6. Pin, action layer and disposition

Action layer L1 only. Before scientific execution or candidate imports,
publicly pin and read back these fifteen sources plus SOURCE_SHA256SUMS:

```text
README.md PREREG.md DERIVATION.md EXACT-DESIGN.md verify.py
input.json prepare_input.py validated_model.hpp validated_model.cpp
kernel.cpp higher_order.hpp dp5_tableau.hpp benchmark.cpp compare.cpp
integrator_run.py
```

The driver uses absolute --baseline, --candidate and --comparator paths
and a new --output directory. Bind all three binary hashes, serialized
input and source manifest before/after every attempted child/comparator,
including failures. Keep arm identity in immutable output metadata.

Retain actual first exact stdout in EXPECTED.txt and its neutral receipt
in RUN.md. If it never completes, follow abandoned-pin policy. Otherwise
preserve every numerical first outcome at conservative status C, including
negative, unresolved and incomplete results. No result authorizes a long
campaign. After the first outcome, this identifier cannot be repaired,
resumed or tuned; a successor requires its own preregistration and pin.

Public summaries exclude raw binaries, private paths, machine identifiers
and credentials. Private records retain states and receipts. This study
closes no complete-trajectory bound, final coherence, all-input channel,
physical apparatus, energy/work or complete-source theorem. Exact-darkness
and unknown-source no-imprinting boundaries remain unchanged.
