# Fixed short time-grid comparison

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering evidence.
Original work Apache-2.0, A. M. Thorn, 2026-10-11.

```text
probe_id: P-U-CA40-GRID-COMPARISON-1
branch: probe/P-U-CA40-GRID-COMPARISON-1
public_issue: https://github.com/mathorn1973/twist-j/issues/1464
authority_base: 37529581a5e0e111668f5f6501d633dbcbb3d2bc
owner: A. M. Thorn, coordinated numerical engineering session
```

The preceding PERF result is exposed design information: strict prefix
bit equality passed, but the frozen twofold speed target was missed.
The present study is neither blinded nor an independent external replication.
It changes the subdivision count in a new local comparison, not the pulses
or the sealed predecessor's result. No pilot, post-pin repair, retry, longer
trajectory or adaptive window selection is permitted under this identifier.

## 1. Equation and question

Use the unchanged compensated sine parent, full two-frequency linear
reference and moving frame:

```text
H_S/hbar = 2u sum_i s_i [sin(chi_i+X_i)-sin chi_i],
H_L/hbar = 2u sum_i s_i cos(chi_i) X_i,
R_z = 2u sum_i s_i [sin(chi_i+m_i+X_i)-sin chi_i
                    -cos(chi_i)(m_i+X_i)],
i dot(W_z) = R_z W_z,   U_S,z = U_L,z W_z.
```

Input.json is unchanged, SHA-256
`ca6b286c9e6d45795677b05e09fbe1b38043c8ff8369b57b652c83195a156d53`.
Its decimal tokens are exact rational model inputs. Derive coherent force
coefficients as before; do not substitute the legacy rounded eta table.
Keep five 100-us loops, sixteen 6.25-us constant-amplitude segments per loop,
the ideal electronic cycle and the absolute physical clock.

The question is the local cost/bound tradeoff between N=256 and N=512 on
four fixed windows for both angles. No full-trajectory error closure,
final nonlinear-coherence decision or hardware claim is attempted.

## 2. Code and arithmetic contract

The optimized kernel is copied unchanged from PERF, SHA-256
`9ba07011d2405e609eb84be8cb5d7781bb06b7cc50be53fbd5304ac5fa93c3f2`.
Retain L=8, guard G=10, dimensions 6435/19448, the quintic dense curve,
sixteen Gauss nodes, analytic continuum and outside-guard tail allowances,
endpoint jumps, norm-ball arithmetic and conservative U_G. No coefficient
cache, different reduction order, weaker allowance or state normalization
is admitted. The common harness bypasses the original long main and
accepts only the frozen N values 256 and 512.

Use the same GNU C++14.2, MPFR4.2.2, GMP6.3.0 and OpenMP toolchain and flags:
`-O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math -fno-tree-vectorize`.
Centers use binary64 nearest rounding; bounds use the prescribed directed
arithmetic. Require finite values, gradual underflow, no FTZ/DAZ and all
inherited runtime fixtures. Preserve exact build commands and source,
input, executable and artifact hashes.

The supporting standard-library verifier tests only its specified exact
identities and negative fixtures. Its first gate has a 600-second ceiling,
exit zero, empty stderr and actual deterministic ASCII/LF stdout. It does
not execute the C++ kernel or certify a trajectory. No EXPECTED transcript
is manufactured before that first actual run.

## 3. Carrier and four independent windows

Retain all seven modes and all 120 thermal basis columns with total
occupation at most three, in the original order. No column is dropped or
renormalized. The original unnormalized weights and omitted-tail contract
remain available, but this study computes no full thermal pair coherence.

Cases 0,1,2 have labels (4,3),(4,4),(1,1) for +4*pi/5; cases 3,4,5 repeat
those labels for -4*pi/5. Let S be the number of occupied amplitude segments:
S=32 in cases 0 and 3, and S=16 in the other four cases. The zero-based
occupied-segment ordinals are

```text
j = [0, floor((S-1)/3), floor(2*(S-1)/3), S-1].
S=32: j=[0,10,20,31];  S=16: j=[0,5,10,15].
q_256=[0,128,128,254]; q_512=[0,256,256,508].
```

Window w starts at cell j[w]*N+q_N[w] in the original ordered occupied-cell
sequence. Evolve two consecutive cells for N256, four for N512. Their
physical start/end times are identical, and each duration is exactly
6.25 us / 128 = 48.828125 ns. No window crosses an amplitude-segment boundary;
the last one ends exactly at that boundary. Preserve the original endpoint
one-sided segment convention and full analytic displacement/phase prefixes.

Every window starts independently with W-frame vector |n> and zero local
error accumulators. Its physical initial state is U_L,z(t0)|n>. This is a
deliberately prepared local test state, not the actual nonlinear state at
t0 and not an unshifted physical thermal state. Do not chain windows, reuse
their evolved outputs as another window's seed, reset the analytic clock,
or carry an earlier window's error into the next window.

This yields four windows times 90 case/batch tasks, 360 tasks at each N,
with eight thermal lanes and all 2880 case/window/column endpoints. It
samples the local generator at early/interior/late analytic histories,
but does not cover accumulated nonlinear state spreading or correlations.
No sum or extrapolation of these window bounds is a global certificate.

Require Linux and AVX-512F/DQ/VL, two packages, 40 physical cores and all 80
logical CPUs with both SMT siblings. Fix singleton OpenMP places, 80
workers, disabled dynamic teams and nested parallelism, and validate
thread/CPU/place coverage and observed migrations.

## 4. First-outcome protocol and resource limits

Run exactly six fresh children in order 512,256,256,512,512,256. No warmup
is discarded. Each child has at most 300 seconds or the remaining total
budget, whichever is smaller. The total is 1800 seconds from runner start,
including topology, preparation, serialization, custody and comparison.
No child or comparator launches after its deadline. Cleanup and final
preservation may extend the reported wall time.

After children 2,4,6 compare the fine/coarse ordinal pairs (1,2),(4,3),(5,6).
Each comparator has at most 90 seconds inside the same remaining total
budget. Preserve launch, exit, timeout, error, cleanup and custody receipts
and raw stdout/stderr. Never overwrite an output directory or discard a
failed first attempt. A missing artifact is not an implicit zero result.

At each N, all three repetitions must reproduce endpoint and local-account
binary64 words byte for byte, including signed zero, with canonical
window/case/thermal-column/basis ordering. Compare actual bytes, not only
hashes or parsed decimals. Include all twelve inherited local-account fields:

```text
guard, tail, continuum, jumps, total,
sampled_time_node_L2, sampled_projection_node_L2,
sampled_arithmetic_node_L2, maximum_node_bound, maximum_norm_error,
endpoint_norm_squared_lo, endpoint_norm_squared_hi.
```

Same-N mismatch stops with REPEATABILITY_FAILED after saving the comparison.
Invalid runtime/model/custody data also stops. No numeric tolerance or
endpoint phase fit is substituted. Sampled arithmetic is already in guard;
sampled time/projection components have no separate continuum certificate.

## 5. Directed consistency and independent engineering screen

For each matched case/window/thermal column let y_256,y_512 be the stored
dyadic endpoints and e_256,e_512 their reported validated local total bounds.
They approximate the same exact local solution with the same initial vector.
Hence the conditional defect proof implies

```text
||y_256-y_512|| <= e_256+e_512.
```

The comparator encloses the actual endpoint-difference norm by directed
arithmetic, D in [D_lo,D_hi], and uses the upward sum
S_up=up(e_256+e_512). Classify each column without tolerance:

```text
D_hi <= S_up: COMPATIBLE;
D_lo >  S_up: INCONSISTENT;
otherwise:   UNRESOLVED.
```

A directed inconsistency is a failure of this numerical integrity contract,
not physical evidence against the ion model. Save it and stop. UNRESOLVED
permits the remaining prescribed work but prevents a compatibility PASS.
All 2880 columns in every one of the three matched comparisons must be
COMPATIBLE for the complete local consistency gate to pass. Large bounds
can make consistency easy; this gate alone says nothing about useful accuracy.

Independently freeze a bound-growth engineering screen:
e_256 <= 2*e_512 for every matched column. Compare the recorded binary64
numbers as exact Fractions. If e_512=0, only e_256=0 passes; report a failed
positive-over-zero case without an Infinity/NaN JSON value. Report maxima
and detailed ratios by angle, case and window, together with components.
This is growth of upper bounds, not a measured growth of true error.
Failure of this screen is a negative engineering outcome and does not stop
the fixed remaining runs. It is not a physical or mathematical falsifier.

Report all six timings and per-N medians, with observed median time ratios.
No additional minimum speedup is selected in this study. The propagation
window includes workspace/thread startup, barriers, numerical work and
progress logging; model preparation/fixtures, serialization and comparison
are separate. Three repetitions give no confidence interval or universal
speed guarantee. Keep preparation anomalies and all first observations.

## 6. Action layer and disposition

Action layer L1 only. Completion means the six children and three comparisons
finished with intact required records; it does not mean the bound-growth or
compatibility screens passed. Report their individual outcomes explicitly.
Incomplete, unresolved and negative outcomes remain first outcomes. No
screen result authorizes a full trajectory or a longer follow-up campaign.

Before first execution, freeze and publicly read back these thirteen files
plus SOURCE_SHA256SUMS: README.md, PREREG.md, DERIVATION.md, EXACT-DESIGN.md,
verify.py, input.json, prepare_input.py, validated_model.hpp,
validated_model.cpp, kernel.cpp, benchmark.cpp, compare.cpp and grid_run.py.
Verify source, serialized input and executable custody before and after all
attempted processes, including failures. Static review/compilation may
precede the pin; scientific execution and candidate imports may not.

Retain actual exact stdout in EXPECTED.txt and RUN.md after a completed first
gate; apply the abandoned-pin policy if that gate never completes. Preserve
the numerical first outcome at conservative status C. Public summaries have
no raw binaries, private paths, credentials or machine identifiers. Private
evidence retains artifacts and receipts. This identifier cannot be resumed,
tuned, or repaired after its first outcome.

The study closes no full-trajectory radius, final nonlinear coherence,
physical apparatus, energy/work account, all-input channel or source theorem.
The exact-darkness and unknown-source no-imprinting boundaries are unchanged.
