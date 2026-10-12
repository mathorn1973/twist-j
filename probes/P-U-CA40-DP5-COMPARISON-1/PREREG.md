# Fixed short three-arm integrator comparison

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering evidence.
Original work Apache-2.0, A. M. Thorn, 2026-10-11.

```text
probe_id: P-U-CA40-DP5-COMPARISON-1
branch: probe/P-U-CA40-DP5-COMPARISON-1
public_issue: https://github.com/mathorn1973/twist-j/issues/1466
authority_base: 9bbb5e64ef852d82133cf94f5c31166b73d328b3
owner: A. M. Thorn, coordinated numerical engineering session
```

The GRID predecessor is exposed design information: the RK4 N256 panel
ran faster, but its frozen twofold bound-growth condition failed in every
matched column. This study is neither blinded nor an independent external
replication. It uses a new identifier and leaves all previous pins and
results unchanged. No pilot, post-pin repair, retry, adaptation, longer
trajectory or pulse retuning is admitted here.

## 1. Equation, data and question

Use the unchanged compensated sine parent, full two-frequency linear
reference and moving frame:

```text
H_S/hbar = 2u sum_i s_i [sin(chi_i+X_i)-sin chi_i],
H_L/hbar = 2u sum_i s_i cos(chi_i) X_i,
R_z = 2u sum_i s_i [sin(chi_i+m_i+X_i)-sin chi_i
                    -cos(chi_i)(m_i+X_i)],
i dot(W_z) = R_z W_z,   U_S,z = U_L,z W_z.
```

The unchanged input.json has SHA-256
`ca6b286c9e6d45795677b05e09fbe1b38043c8ff8369b57b652c83195a156d53`.
Its decimal tokens are exact rational model inputs. Derive coherent force
coefficients as before; the legacy rounded eta table is not substituted.
Keep five 100-us loops, sixteen 6.25-us constant-amplitude segments per loop,
the ideal electronic cycle and the absolute physical clock.

The question is whether arm C improves the measured local cost while
reporting no larger local certificate than arm A. Arm B separates the old
grid change from the new method at the same certificate-cell count. The
experiment does not decide complete-pulse accuracy or physical realization.

## 2. Fixed methods and arithmetic

| Arm | N | integrator | dense_curve | substeps / RHS calls per certificate cell |
|---|---:|---|---|---|
| A | 512 | RK4 | QUINTIC_ENDPOINT_DIRECTIONAL_FD | 1 / 9 |
| B | 256 | RK4 | QUINTIC_ENDPOINT_DIRECTIONAL_FD | 1 / 9 |
| C | 256 | DP5_TWO_HALF_STEPS | QUINTIC_THREE_POINT_HERMITE | 2 / 13 |

N is the number of certificate cells in one original 6.25-us segment.
Arm C performs two consecutive DP5 steps of length h/2 inside a cell of
length h, sharing the actual midpoint RHS between them. Its endpoint and
midpoint values, together with their actual RHS values and the starting
RHS, determine one quintic Hermite curve. No embedded error estimate,
adaptive step controller, normalization or phase fitting is used.

The distinct normalized DP5 evaluation times in a cell are

```text
0, 1/10, 3/20, 2/5, 4/9, 1/2, 3/5, 13/20, 9/10, 17/18, 1.
```

All lie within the same constant-amplitude segment, using its one-sided
endpoint convention. The midpoint derivative must be evaluated on the
stored midpoint state; the final derivative on the stored final state.
The first cell RHS is recomputed at every cell, so the frozen count is
13 per candidate cell. A/B retain the inherited directional acceleration
construction with delta=h/128 and its same-segment extension.

The Dormand-Prince weights are attributed to Hairer and Wanner's
[DOPRI5 coefficient table](https://www.unige.ch/~hairer/prog/nonstiff/dopri5.f),
subroutine CDOPRI, accessed 2026-10-11. The original C++ implementation and
three-point Hermite proof are supplied here. The Fortran solver, its
adaptive controller and Shampine dense-output implementation are not copied.
DERIVATION.md and EXACT-DESIGN.md state the exact identities audited by the
supporting verifier; method order is not used as an error certificate.

kernel.cpp remains byte-identical to the sealed optimized kernel, SHA-256
`9ba07011d2405e609eb84be8cb5d7781bb06b7cc50be53fbd5304ac5fa93c3f2`.
input.json and prepare_input.py remain unchanged. higher_order.hpp and
dp5_tableau.hpp implement only the new candidate step/curve. Model preparation
uses a compile-time method selector: baseline retains the seven-node layout
and original preparation sequence; candidate uses eleven nodes, with no
unused old finite-difference nodes. Baseline children allocate no additional
DP5 workspace and perform no DP5 preparation. Both use the same physical
equation, exact input, coefficient precision and analytic time prefixes.

Retain L=8, G=10, dimensions 6435/19448, K=3, the degree-five curve,
sixteen Gauss nodes, full outside-guard tail and analytic continuum
allowances, endpoint jumps and norm-ball arithmetic. Every stored curve
coefficient is treated as an exact dyadic. The certifier and its arithmetic
allowances are unchanged. No weaker bound, new cache or different
certifier reduction order is admitted. The harness bypasses the original
long main and reaches only the prescribed local cells.

Use GNU C++ 14.2.0, MPFR 4.2.2, GMP 6.3.0 and OpenMP with common flags
`-O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math -fno-tree-vectorize`
and the pinned compile-time method selector. Retain exact build commands
and hashes for baseline, candidate and comparator binaries. Centers use
nearest binary64 rounding and bounds use prescribed directed arithmetic.
Finite values, gradual underflow, disabled FTZ/DAZ and all inherited runtime
fixtures are required. Static compilation is not a scientific run.

The standard-library exact gate has a 600-second ceiling, exit zero, empty
stderr and deterministic ASCII/LF stdout. It does not execute C++ or prove
any observed accuracy or speed. EXPECTED.txt is created only from its actual
first output after the complete public pin and readback.

## 3. Carrier and four independent windows

Keep all seven modes and all 120 basis columns with total occupation at most
three, in the inherited basis order. No column is discarded or renormalized.
Unnormalized thermal weights remain recorded, but no full thermal pair
coherence or thermal-weighted global error summary is claimed.

Cases 0,1,2 have labels (4,3),(4,4),(1,1) for +4*pi/5; cases 3,4,5 repeat
them for -4*pi/5. There are S=32 occupied amplitude segments in cases 0 and
3, and S=16 in the other cases. Freeze the occupied-segment ordinals and
within-segment cell starts:

```text
j = [0, floor((S-1)/3), floor(2*(S-1)/3), S-1].
S=32: j=[0,10,20,31];  S=16: j=[0,5,10,15].
q_256=[0,128,128,254]; q_512=[0,256,256,508].
```

Window w starts at prepared occupied-cell index j[w]*N+q_N[w]. Arm A
evolves four cells; B and C evolve two. Every window lasts exactly
6.25 us / 128 = 48.828125 ns, with identical absolute physical endpoints
in all arms. No window crosses an amplitude switch; the last ends at one.
A/B/C perform respectively 4/2/4 integration substeps and 36/18/26 RHS
calls per window. This count distinction is explicit in metadata and reports.

Every window starts independently from W-frame vector |n> with zero local
certificate accumulators. Its physical initial state is U_L,z(t0)|n>, not
the actual nonlinear state reached at t0 or an unshifted laboratory thermal
state. Preserve all original analytic displacement/phase history. Do not
reset the physical clock, chain windows or carry one window's errors or
evolved vector into another. These states do not cover accumulated nonlinear
spreading and correlations; the window bounds cannot certify the full pulse.

Each child has 360 tasks: four windows, six cases and fifteen eight-lane
thermal batches. It records all 2880 case/window/column endpoints. Canonical
binary order is WINDOW,CASE,COLUMN,BASIS,RE/IM for states and
WINDOW,CASE,COLUMN,FIELD for the twelve local components.

Require Linux, AVX-512F/DQ/VL and all 80 logical CPUs on two packages with
40 physical cores and both SMT siblings. Use singleton OpenMP places, 80
workers, disabled dynamic teams/nested parallelism and the same affinity
policy for all arms. Check worker/CPU/place coverage and observed migrations.

## 4. First-outcome protocol and resources

Run exactly six fresh children A,B,C,C,B,A, giving two observations per arm.
No warmup is discarded. Each child has at most 300 seconds or the remaining
campaign budget, whichever is smaller. The campaign has 1800 seconds from
runner start, including preparation, propagation, serialization, validation,
custody and comparisons. No process launches after its deadline. Cleanup
and final evidence preservation may extend the reported wall time.

After child 3 compare ordinal pairs (1,2), (1,3), (2,3), in that order.
After child 6 compare (6,5), (6,4), (5,4), in that order. Each comparator
has at most 90 seconds within the same campaign budget. Both arms in each
comparison must match the frozen method metadata, common physical windows,
input, basis and binary layout. Preserve all launches, exits, errors,
timeouts, cleanup results and raw stdout/stderr, including failed attempts.
Missing results are not zeros. No output directory may be reused.

Within each arm, repeat comparisons are (3,4) for C, (2,5) for B and (1,6)
for A. Compare actual bytes of endpoints, components, basis, immutable
metadata and layout. Keys must identify the arm, not only N: B/C are distinct
methods and their endpoints need not be bit-identical. Signed zero counts
in strict binary64 repeatability. Include all twelve component fields:

```text
guard, tail, continuum, jumps, total,
sampled_time_node_L2, sampled_projection_node_L2,
sampled_arithmetic_node_L2, maximum_node_bound, maximum_norm_error,
endpoint_norm_squared_lo, endpoint_norm_squared_hi.
```

Same-arm mismatch is a fatal REPEATABILITY_FAILED outcome after saving its
record. Runtime/model/custody failures likewise stop. Sampled arithmetic is
already inside guard; sampled time/projection terms have no standalone
continuous-time certificate and are never added again to the total.

## 5. Fixed decisions and failure thresholds

For each matched column, arms X and Y approximate the same exact local
solution. The conditional defect proof implies

```text
||y_X-y_Y|| <= e_X+e_Y.
```

The comparator encloses the exact dyadic endpoint-difference norm in
[D_lo,D_hi] and computes S_up=up(e_X+e_Y). With no tolerance or phase fit:

```text
D_hi <= S_up: COMPATIBLE;
D_lo >  S_up: INCONSISTENT;
otherwise:   UNRESOLVED.
```

INCONSISTENT is a fatal numerical-integrity failure, not a physical
falsification. Preserve it and stop. UNRESOLVED allows the fixed remaining
work but prevents a compatibility PASS. All 2880 columns in all six
comparisons must be COMPATIBLE for that gate to pass. Large bounds can make
this easy; compatibility alone establishes no useful accuracy.

Freeze two independent engineering conditions:

1. **Bound non-increase:** e_C <= e_A for every matched column in both A/C
   comparisons (1,3) and (6,4). Compare the recorded binary64 bounds as exact
   Fractions, without a multiplicative allowance. If e_A=0, only e_C=0
   passes. Report any positive-over-zero ratio without Infinity/NaN JSON.
2. **End-to-end improvement:** the two-observation program end-to-end median
   of C is strictly less than A's. Decide this by comparing the exact
   Fraction sums of their two stored binary64 timings; division by two
   cancels. Equality fails. No fixed speed factor is imposed.

Failure of either engineering condition continues the remaining fixed
children and comparisons unless an integrity failure occurs. Completion
does not imply a passed screen. A joint engineering PASS additionally
requires completed repeatability and all-comparison compatibility gates.
The old twofold bound-growth allowance is not inherited.

Report all six timings, both observations per arm, descriptive medians and
ratios. With two observations the median is their arithmetic mean. It gives
no confidence interval or statistical significance. Keep every preparation
anomaly. Kernel time includes workspaces, OpenMP startup/barriers, numerical
work and progress logging. Program end-to-end also includes model preparation,
fixtures and serialization; child wall additionally includes process
overhead. Runner custody/comparison time is separate. The primary speed
decision uses program end-to-end, while other timings remain descriptive.

Report the 24 case/window groups and each sign's 1440 local columns, with
paired bound ratios and component diagnostics. A/B describes the old grid
effect; B/C describes the method change at N256; A/C is the primary combined
tradeoff. Ratios of upper bounds are not measured true-error or infidelity
ratios. No empirical convergence order follows from this finite panel.

## 6. Action layer, pin and disposition

Action layer L1 only. Before scientific execution or candidate imports,
publicly pin and read back these fifteen files plus SOURCE_SHA256SUMS:

```text
README.md PREREG.md DERIVATION.md EXACT-DESIGN.md verify.py
input.json prepare_input.py validated_model.hpp validated_model.cpp
kernel.cpp higher_order.hpp dp5_tableau.hpp benchmark.cpp compare.cpp
integrator_run.py
```

The driver uses --baseline, --candidate and --comparator absolute executable
paths and --output pointing to a new directory. Bind all three binaries,
the exact serialized input and source manifest before/after every attempted
child and comparator, including failures. Baseline/candidate method choices
are frozen in the compiled programs and the immutable output metadata.

Preserve the first exact stdout in EXPECTED.txt and its neutral receipt in
RUN.md. If that gate never completes, follow the abandoned-pin policy.
Otherwise preserve every numerical first outcome at conservative status C,
including incomplete, unresolved and negative screens. No result authorizes
a long campaign. The identifier cannot be repaired, resumed or tuned after
its first outcome; any successor needs its own preregistration and pin.

Public summaries exclude raw binaries, private paths, machine identifiers
and credentials. Private evidence retains states, receipts and comparison
records. This study closes no full-trajectory radius, final coherence,
all-input channel, physical apparatus, energy/work or source theorem. The
exact-darkness and unknown-source no-imprinting boundaries remain unchanged.
