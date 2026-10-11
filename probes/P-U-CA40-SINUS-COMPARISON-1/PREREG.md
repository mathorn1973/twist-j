# Direct fixed-pulse nonlinear comparison: preregistration

PUBLIC NON-CANONICAL. Conditional L1 mathematics and floating engineering.
Original work Apache-2.0, A. M. Thorn, 2026-10-11.

```text
probe_id: P-U-CA40-SINUS-COMPARISON-1
branch: probe/P-U-CA40-SINUS-COMPARISON-1
public_issue: https://github.com/mathorn1973/twist-j/issues/1456
authority_base: cdc0c2d2e1eb3710fdc01ae784a86bc199947d94
owner: A. M. Thorn, coordinated source-preparation session
```

The complete source, data, numerical defaults, exact verifier and manifest
are committed, pushed and publicly byte-read back before first scientific
execution or import. Static inspection, syntax parsing and compilation are
allowed before that pin. No pulse, threshold or source changes after it.

## 1. Equation and question

Keep the compensated sine parent H_S/hbar=2u sum_i s_i[sin(chi_i+X_i)-sin chi_i]
and its full two-frequency linearization H_L/hbar=2u sum_i s_i cos(chi_i) X_i.
Their exact definitions, absolute phases and physical constants are inherited
from P-U-CA40-TRAJECTORY-VALIDITY-1, not fitted to new outputs. Seven harmonic
axial modes and both original envelopes are retained. In the known full-linear
frame W_z=U_L,z^dagger U_S,z, propagate

```text
i dW_z/dt = 2u sum_i s_i {sin(chi_i+m_i+X_i)
                         -sin chi_i-cos chi_i (m_i+X_i)} W_z,
m_i=2 sum_m kappa_mi Re(alpha_L,m exp(-i omega_m t)).
```

There are five identical 100-us loops, sixteen constant segments each, ideal
instantaneous active X5 at each loop end, and no bus reset. Only identically
zero-response intervals may be skipped; the absolute optical/motional clock
and linear prefix displacement are never reset.

Test active input labels (4,3), (4,4), (1,1), in this order, for the +4*pi/5
envelope and then the -4*pi/5 envelope. The first pair exposed the prior RWA
error; (1,1) exposed the large intermediate displacement. This openly selected
panel is not a random sample or a worst-case guarantee over all 25 labels.
The immediate question is the direct nonlinear change in these three
pairwise reduced electronic coherences per sign, with independently reported
thermal omission, dynamic truncation and time-step sensitivity.

## 2. Code and numerical method

verify.py is the accepted standard-library exact verifier, scoped by
EXACT-DESIGN.md. It audits algebra and bookkeeping; no floating waveform
or propagator is thereby certified. Deterministic ASCII stdout, explicit LF,
exit zero and empty stderr are required for a completed exact gate. Its
first invocation has a 600-second limit.

kernel.cpp propagates all deterministic thermal columns using classical RK4
with a fixed number of equal steps per original constant-amplitude segment.
The sine is projected from the actual unbounded oscillator displacement
operator using exact normal ordering. It is not obtained by taking the sine
of a truncated position matrix. Total-phonon cutoff L gives dimension
C(L+7,7). Normal-ordered ladder polynomials terminate exactly in this space;
their floating evaluation adds roundoff but no selected Taylor-order model.

Freeze the initial total occupation cutoff K=3, giving 120 columns. Their
weights (20/21)^7 (1/21)^N are retained without renormalization. The exact
omitted mass is 1-sum_(N=0..3) C(N+6,6)(20/21)^7(1/21)^N. All seven initial
mode occupations are enumerated. This mass is distinct from dynamical
population beyond L and is never inferred from a convergence comparison.

The four configurations run once in this fixed order:

| Total dynamic cutoff L | Dimension | RK4 steps per 6.25-us segment |
| --- | ---: | ---: |
| 4 | 330 | 128 |
| 6 | 1716 | 128 |
| 6 | 1716 | 256 |
| 6 | 1716 | 512 |

No alternative cutoff, outcome-dependent step refinement, waveform search,
new thermal cutoff or replacement campaign is allowed. The whole floating
campaign has a 1800-second budget for launching and running kernel children,
measured from the start of setup. Each child is limited by the remaining
budget. Final validation, endpoint comparisons and archival may extend the
reported total wall time. Preserve every completed output,
partial progress and timeout. The budget is a workload limit, not a promise
that this initial campaign reaches the desired accuracy.

The kernel uses explicit AVX-512 FP64 across batches of eight thermal
columns and 80 OpenMP workers over 90 case/batch tasks. All 80 logical CPUs
must be available, representing two packages and NUMA nodes, 40 physical
cores and two complete SMT siblings per core. Record actual thread/CPU/place
maps and use explicit binding with dynamic teams disabled. No assertion
that every task has equal runtime or that 80 threads outperform 40 follows.
That performance comparison belongs to the completed earlier benchmark.

Compile with GNU C++ using -O3 -std=c++20 -fopenmp -ffp-contract=off
-fno-fast-math -fno-tree-vectorize and the explicit AVX-512 target attributes
in source. Save command, compiler version and executable SHA-256. Numerical
replay uses Python standard library plus NumPy only for recorded endpoint
array comparisons; record its version. No dependency installation is needed.

## 3. Carrier, data and observables

input.json is byte-identical to the predecessor's public 10093-byte input
at source pin 604bad993830222ab8c34cee6f31a7a36043e350. It contains both
envelopes, seven mode vectors/frequencies, geometry and explicit constants.
linear_model.py copies the predecessor's model and exact-frequency integral
helpers. There is no new equilibrium or pulse-construction solver.

Physical order is (s,x,u,y,w,q,r), active A=(4,5), protected P=(1,2,3,6,7).
All protected responses are exactly zero, independent of their coherent
electronic state and an arbitrary external reference. The bus is initially
the declared independent product thermal state with nbar=1/20 in every mode.
The full electronic carrier is 5^7, but dynamics are sampled only at the
three named active labels. Protected states factor out exactly in the model.

For each pair a,b restore the different linear frames before taking overlaps:
Gamma_S,ret=sum_ret w_n <W_b n| U_L,b^dagger U_L,a |W_a n>.
Compare with the full analytic thermal Gamma_L, not a renormalized thermal
approximation. The omitted thermal contribution to Gamma_S has modulus at
most p_tail. Thus a thermal-only interval for D_pair is

```text
[max(0,(|Gamma_S,ret-Gamma_L|-p_tail)/2),
 min(1,(|Gamma_S,ret-Gamma_L|+p_tail)/2)].
```

This is not a total-error interval: it omits dynamic, integration and
floating errors. The restore operation uses projected true displacement
matrix elements and its Weyl/linear phase; comparing raw W overlaps would
describe a different observable. No independent branch phase fitting is
allowed. Retain complex coherences, raw phases, return/norm/shell diagnostics
and endpoints for all cases, not just maxima.

Compare L4/128 with L6/128 by embedding the smaller graded basis in the
larger. Compare L6/128 with L6/256 and L6/256 with L6/512. For each branch
report sqrt(sum_ret w_n ||psi_new,n-psi_old,n||^2) without phase fitting.
These are differences of approximations, not rigorous error bounds.

## 4. Systematics and frozen decision rules

The exact algebraic gate and floating diagnostics have separate outcomes.
Numerical invariants and thresholds do not promote the floating dynamics
to exact arithmetic. Preserve failed thresholds as results.

Integrity requires the complete source manifest, valid finite input and
output, declared dimensions/chronology, all 80 CPU places, valid endpoint
byte counts, scalar/SIMD and independent small displacement fixtures, and
independent Python full-linear endpoint agreement (alpha <=1e-9 absolute,
phase <=1e-8 absolute). Numerical fixture tolerance is 1e-11 on the absolute
or source-declared scaled discrepancy. A failed integrity check stops further
configurations while preserving the first evidence; no silent retry.

The nonlinear comparison target remains D_pair<=1e-3. For an engineering
convergence screen, require the largest cutoff-vector difference and largest
fine-step-vector difference <=1e-4, and norm drift <=1e-6. Also report the
coarse/fine time differences rather than extrapolating their ratio into an
unproved bound. A larger difference means UNRESOLVED at this resource budget.
Thermal-only intervals crossing the target are UNRESOLVED even before
dynamic/time error. A thermal-only lower endpoint above target is a candidate
numerical discrepancy, qualified by those other diagnostics.

Dynamic residual diagnostics use the triangle formula in DERIVATION.md at
every RK4 stage of each occupied step, on the actual approximate stage
vectors. Per retained thermal column accumulate
`I_n += h*(rho_1+2*rho_2+2*rho_3+rho_4)/6`, then report
`sqrt(sum_n p_n I_n^2)` without normalizing the weights. This distinguishes
norm outside the truncated space from population in its last shell.
Retain the minimum raw projected-displacement squared norm deficit; a
deficit below `-1e-10*(1+norm_squared)` fails numerical integrity. Smaller
negative values are clamped only for the diagnostic square root.
Cancellation, approximate stage vectors and finite sampling prevent
treating this FP residual quadrature as a rigorous all-time upper bound.
No two-cutoff agreement, norm conservation, small shell population or
step-doubling ratio alone proves a total error bound.

Consequently this campaign has no positive rigorous infinite-bus channel
certificate. A numerical result may motivate a larger convergence or
validated-residual successor; that requires a new preregistration and pin.
The initial thermal truncation has an exact mass account even if the
dynamic/time screens remain inconclusive.

## 5. Layer and disposition

Action layer L1: conditional operator algebra, finite numerical comparison
and exact bookkeeping. No new L1-to-L6 gate, native-U coupling, occurrence
law or apparatus-class completeness is claimed. No experiment is performed.
Classical prescribed control, harmonic confinement, axial-only motion,
ideal instantaneous carriers and ideal shelving remain selected premises.
Heating, scattering, finite pulse controls, radial motion, trap anharmonicity
and complete source/controller work accounting remain outside this probe.

The auxiliary protected-register identity does not establish preservation
of an unknown full source while a full informative contact retains a readable
record. The existing obstruction to that stronger claim is unchanged.

A completed exact first run is copied byte for byte to EXPECTED.txt and
recorded in RUN.md. RESULT.md and NUMERICAL.md retain negative, incomplete
and inconclusive numerical outcomes at conservative status C. An exact gate
that never completes is disposed as ABANDONED under POLICY.md, consuming
the identifier without invented EXPECTED.txt or RUN.md. No Canon, registry,
workflow, policy, earlier probe, promotion or threshold change belongs here.
