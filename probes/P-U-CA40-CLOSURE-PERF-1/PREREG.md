# Short closure-kernel regression and performance test

PUBLIC NON-CANONICAL. Conditional L1 engineering evidence.
Original work Apache-2.0, A. M. Thorn, 2026-10-11.

```text
probe_id: P-U-CA40-CLOSURE-PERF-1
branch: probe/P-U-CA40-CLOSURE-PERF-1
public_issue: https://github.com/mathorn1973/twist-j/issues/1462
authority_base: 264d792eb433c9a032f6282b3c7800ee1837f73b
owner: A. M. Thorn, coordinated performance session
```

The sealed predecessor P-U-CA40-BALL-CLOSURE-1 used source pin
`ab33a3f42af66b9bfa52915871b10ce3d914c124` and result head
`6b1ec24c69ee1a66166bc0bbcce5401f67da06f8`, preserved in PR #1461.
It completed its exact supporting gate but no numerical configuration before
a documented manual resource stop. This new probe is a short engineering
comparison, not a resumption or amendment of that attempt. The preceding
timing and stack observations are exposed design information. This is not
a blinded prediction, independent external replication, or hardware test.

The complete thirteen-file source inventory plus manifest must be committed,
pushed and publicly read back before any scientific execution or candidate
import. Compilation, AST parsing and static inspection may precede that pin.
No unrecorded pilot, retry, post-pin repair or longer campaign is permitted.

## 1. Equation and question

Retain the predecessor's compensated sine parent, full two-frequency linear
comparison and moving frame, without changing a pulse or model parameter:

```text
H_S/hbar = 2u sum_i s_i [sin(chi_i+X_i)-sin chi_i],
H_L/hbar = 2u sum_i s_i cos(chi_i) X_i,
R_z = 2u sum_i s_i [sin(chi_i+m_i+X_i)-sin chi_i
                    -cos(chi_i)(m_i+X_i)],
i dot(W_z) = R_z W_z, U_S,z = U_L,z W_z.
```

The original input.json bytes have SHA-256
`ca6b286c9e6d45795677b05e09fbe1b38043c8ff8369b57b652c83195a156d53`.
Decimal tokens remain exact rational model inputs. The coherent derived
force coefficients, absolute time and full-linear prefixes remain unchanged;
no legacy rounded eta table is substituted as a new force definition.

The question is whether the low-copy implementation has identical tested
prefix endpoint/component bits and an observed median propagation-window
speedup of at least exactly 2 relative to the sealed implementation.
This is not the predecessor's full error-closure or nonlinear-discrepancy gate.

## 2. Code and arithmetic contract

The baseline_kernel.cpp bytes are the sealed BALL kernel, SHA-256
`e84a7071fcbd10461bbce54e30638ecd68845fe0cc0a901e827be0d2bd9cfee8`.
The optimized implementation before the common harness is kernel.cpp,
SHA-256 `9ba07011d2405e609eb84be8cb5d7781bb06b7cc50be53fbd5304ac5fa93c3f2`.
The final source manifest, not an inferred executable identity, freezes the
complete files actually compiled and executed.

One shared benchmark.cpp includes the selected kernel and renames its full
campaign entry point. Its own reachable dynamics loop is fixed to four
occupied cells per task. Compile-time variants select baseline or optimized;
the only constructor adapter accommodates the supported-space Ball workspace.
CLI options cannot enlarge the prefix. Neither the original full campaign
entry point nor a second cutoff configuration is launched.

The changes remove creation pre-zeroing, clear only the annihilation guard
complement, remove unused half copies, replace displacement copies with
guarded ownership exchange, and evaluate dual Horner in P_L before exact
zero extension. The old conservative U_G remains. Every coefficient-center
pair, outward error allowance and order of occupied-entry arithmetic remains
subject to the trace-equivalence premises in OPTIMIZATION.md. No table cache,
FMA, in-place triangular action or altered reduction order is admitted.

Use the same GNU C++14.2/MPFR4.2.2/GMP6.3.0 toolchain and flags for both:
`-O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math -fno-tree-vectorize`.
Keep binary64 nearest-rounded centers, prescribed embedded directed bounds,
gradual underflow, no FTZ/DAZ, finite values and the inherited runtime fixtures.
Record compiler, dependencies, exact commands, source and binary hashes.

The accepted verify.py is a separate standard-library Fraction audit of
support/layout, guarded ownership and exact Horner/embedding identities.
EXACT-DESIGN.md lists its finite positive and negative fixtures. Its first
gate has a 600-second ceiling, exit zero, empty stderr and exact ASCII/LF
stdout. It does not execute or certify C++, IEEE equivalence, timing, or a
trajectory. No expected transcript is created before its first actual run.

## 3. Carrier and frozen short workload

Retain seven axial modes and the existing pulse/input bytes: five 100-us
loops, sixteen 6.25-us amplitude segments per loop, the ideal electronic
cycle, the absolute clock and no bus reset. Branch labels are (4,3), (4,4),
(1,1) for +4*pi/5, followed by the same labels for -4*pi/5.

All 120 thermal columns with total occupation K<=3 remain, with original
unnormalized weights and omitted-tail contract. No thermal column is dropped
for speed and no weight or approximate state is renormalized.

Freeze L=8, G=10, 512 substeps per occupied segment, eight SIMD lanes, 90
case/batch tasks and 80 bound workers. Evolve exactly the first four occupied
cells from each original prepared sequence; do not reset the clock to zero
at that first cell. Preparing the original full node model does not evolve
the full trajectory. The four cells are not four pulses or four loops.

Require Linux, AVX-512F/DQ/VL, two CPU packages, 40 physical cores and all 80
logical CPUs with both SMT siblings. The runner fixes singleton OpenMP
places, disables dynamic teams and nested parallelism, and verifies distinct
thread/CPU/place mappings against the declared affinity. There is no thread
count or architecture search inside this study.

Run six fresh children in order B,F,F,B,B,F, with no discarded warmup and no
extra trials. Every child receives at most 300 seconds or the remaining
campaign time, whichever is smaller. The total ceiling is 1,800 seconds from
runner start, including topology, input serialization, custody and comparison
work. No child starts after that deadline. Cleanup and preservation of the
final failed/partial record may extend the final reported wall time.

## 4. Systematics, output and strict regression gate

Each child must complete all 90 four-cell tasks and pass inherited runtime
fixtures, input/source/binary custody, finite-output and placement checks.
The runner preserves raw stdout/stderr, exact binary endpoint/component
files, basis/layout information, lifecycle and first-outcome receipts.
It compares every completed child against the first baseline without
selecting a favorable repetition. Missing fields or artifacts are failures
of a complete comparison, not implicit zero differences.

Compare little-endian IEEE binary64 words byte for byte, including signed
zero. Endpoint ordering is case, thermal column, basis row, real/imaginary.
Component ordering is case, thermal column and these twelve fields:

```text
guard, tail, continuum, jumps, total,
sampled_time_node_L2, sampled_projection_node_L2,
sampled_arithmetic_node_L2, maximum_node_bound, maximum_norm_error,
endpoint_norm_squared_lo, endpoint_norm_squared_hi
```

All six endpoint files and all six component files must agree. Hashes and
byte counts identify them; direct raw-byte comparison establishes equality.
Parsed decimal equality, normalization, epsilon tolerances, omitted zeros
or exclusion of one component cannot replace this rule. A mismatch is
REGRESSION_FAILED. Timeout, interruption, invalid output, failed custody or
an incomplete set prevents an equivalence PASS. Preserve every outcome and
stop without retry or source modification.

The per-column accounts are partial accounts only. Sampled time/projection
diagnostics are not standalone continuous-time certificates, and sampled
arithmetic is already included in guard; it must not be added a second time.
No final restored-frame pair coherences or full-trajectory radii are computed.

## 5. Performance decision and limitations

After the complete strict regression gate passes, let T_B be the median of
the three baseline kernel_seconds and T_F the median of the three optimized
kernel_seconds. The performance target passes iff T_B >= 2*T_F. Compare the
recorded binary64 seconds as exact rationals for this decision, without a
post-hoc tolerance. Equivalence can pass while this speed target fails.

The propagation timer begins before the OpenMP region and includes worker
startup, Work/BWork allocation, barriers, dynamics, certification and progress
logging. It stops after the parallel region. Model preparation and runtime
fixtures are reported separately; final norms, endpoint/component writes,
hashes and runner comparison are outside that timer. Report all six raw
timings and preparation/end-to-end summaries with those boundaries.

The fixed order reduces neither thermal drift nor scheduling variation to
a proved statistical model. Three repetitions give an observed median, not
a confidence interval or universal speed guarantee. Do not infer full-run
speed or success from the short prefix or extrapolate its partial error as a
final radius. Do not lengthen the panel or budget if the target is missed.
Even a complete engineering PASS authorizes no automatic long campaign.

## 6. Action layer, custody and disposition

Action layer L1 only. This same-session, result-exposed regression witness
changes no Canon, policy, scientific admission or physical source theorem.
It establishes neither hardware feasibility nor a completed numerical
error closure. Exact spectator/source-reference identity remains conditional
on the previous model premises; the unknown-source no-imprinting boundary
is not altered by faster software.

Freeze these thirteen files in SOURCE_SHA256SUMS: README.md, PREREG.md,
EXACT-DESIGN.md, OPTIMIZATION.md, input.json, prepare_input.py,
validated_model.hpp, validated_model.cpp, baseline_kernel.cpp, kernel.cpp,
benchmark.cpp, benchmark_run.py and verify.py. The manifest itself is also
part of the public source pin. Verify source, input and executable custody
before and after attempted children, including failed and timed-out attempts.
Never overwrite an existing output directory.

After a completed exact first gate, retain actual stdout as EXPECTED.txt and
record RUN.md. Report positive, negative and incomplete engineering outcomes
in RESULT.md and a neutral performance summary, at conservative status C.
If the exact gate never completes, apply the abandoned-pin policy; never
invent stdout or resume a spent identifier. Public artifacts contain no raw
binary endpoints, private machine paths, credentials or personal identifiers.
Private raw evidence remains archived with receipt hashes and explicit scope.
