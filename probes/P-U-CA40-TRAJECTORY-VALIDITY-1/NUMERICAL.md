# Numerical approximation audit

PUBLIC NON-CANONICAL. Floating engineering estimates for the frozen conditional
Hamiltonians; no interval certificate or physical experiment. Date: 2026-10-11.

The first and only pinned campaign completed with consistency checks passing.
Both RWA accuracy screens have a numerical lower witness above the declared
1e-3 threshold. The nonlinear optical remainder is NOT_CERTIFIED_BY_THIS_BOUND.
The fixed input, pulse, grid, thresholds and first outcome were not changed.

## Endpoint comparison of the two linear models

All figures compare the full linear harmonic model with its RWA comparator.
The distance convention is trace distance, equivalently half-diamond for the
uniform upper bound. It is not average gate infidelity or a measured error rate.

| Quantity | +4*pi/5 | -4*pi/5 |
|---|---:|---:|
| Direct two-branch witness | 0.0140671379814 | 0.00937853599417 |
| Common-phase optimized upper estimate | 0.0215862939212 | 0.0163546998083 |
| Raw-convention upper estimate | 0.324697962318 | 0.217146131945 |
| Optimized common phase, rad | 0.312149381972 | 0.208223718007 |
| RWA endpoint max abs(alpha) | 4.96389168488e-14 | 4.05284863371e-14 |
| Full-linear endpoint max abs(alpha) | 0.0138576656353 | 0.0113147366109 |
| RWA target phase discrepancy, rad | 7.81597009336e-14 | 4.70734562441e-14 |
| Uncompensated common unary phase, rad | -0.00127065245129 | -0.00103748338203 |
| Numerical unary branch spread, rad | 2.66181521269e-12 | 2.17287299265e-12 |

For both signs the maximal witness is the pair of active labels `(4,3)`
and `(4,4)` (zero-based flattened indices 23 and 24). A coherent superposition
of these branches, optionally correlated with an orthogonal reference, has
trace-distance change `abs(lambda_L-lambda_R)/2`. All 300 unordered pairs
were evaluated in the predeclared search per sign; the maximal witness is retained. This witnesses a violation
of 1e-3 in the stated model comparison; a large upper bound alone would not.

The old RWA target still passes its own numerical closure/phase sanity checks.
The added counterrotating term leaves nonzero final motion and relative
electronic phase. A single global phase does not remove this discrepancy.
This does not prove the same error for the full nonlinear sine parent:
its actual propagator has not been simulated here.

## Whole-pulse motion and nonlinear-remainder diagnostics

Each row below is maximized independently over all 25 branches for that sign.
The maximizing branches need not coincide. Sampled maxima are distinguished
from mathematical intersample envelopes evaluated in floating arithmetic.

| Quantity | +4*pi/5 | -4*pi/5 |
|---|---:|---:|
| Sampled max abs(alpha), full linear | 4.33479172277 | 3.53934262067 |
| Continuous max abs(alpha) upper estimate | 4.33542772257 | 3.53986191234 |
| Sampled max abs(alpha_L-alpha_R) | 0.0195674713568 | 0.0159767734602 |
| Continuous displacement-difference upper estimate | 0.022107420273 | 0.018050633066 |
| Sampled max RMS(k q) | 0.600209872746 | 0.496318971751 |
| Continuous max RMS(k q) upper estimate | 0.644623798997 | 0.532157077983 |
| Sampled adjacent relative RMS / spacing | 0.00262303368332 | 0.00262067522757 |
| Continuous adjacent relative RMS / spacing upper estimate | 0.00263376585744 | 0.00262784130172 |
| Continuous coherent adjacent displacement / spacing upper estimate | 0.000305807217491 | 0.000249690547505 |
| Uncapped exact-Gaussian-RMS midpoint integral | 16.314448541 | 10.2862939549 |
| Uncapped continuous Duhamel upper estimate | 22.7679776433 | 14.0352866627 |
| Uncapped quartic alternative upper estimate | 30.2288480004 | 18.7095439126 |
| Lipschitz allowance before taking min with quartic bound | 6.97250546864 | 4.07952065596 |
| Continuous-envelope minus midpoint gap | 6.45352910231 | 3.74899270781 |

The Duhamel integral is an upper bound obtained by integrating residual
norms and applying triangle inequalities. Values above one reduce to the
trivial channel bound one. Neither 22.77 nor 14.04 is an observed error or
a lower bound. Even the midpoint sums are above one; reducing only the mesh
allowance does not supply a small bound from this same norm-integral method.

The frozen RMS<=0.1 heuristic also fails already at the initial thermal state:
the seven initial RMS(k q) values are
`0.1359918471, 0.1207368374, 0.1150000656, 0.1133966399, 0.1150000656, 0.1207368374, 0.1359918471`.
Thus its failure cannot be attributed solely to the pulse. The pulse further
raises sampled RMS to about 0.600 and 0.496. This dimensionless diagnostic is
not a necessary-and-sufficient gate-accuracy criterion. Its frozen threshold
is reported honestly and is not relaxed after inspection.

Adjacent relative RMS stays below about 0.00264 of the corresponding
equilibrium spacing in these estimates. That supports only a small-relative-
motion diagnostic. It is not a rigorous Coulomb-anharmonicity bound; the
harmonic axial trap and omission of radial instability remain assumptions.

## Continuous RWA phase coverage

The separately preregistered whole-segment midpoint/derivative envelope gives
the trivial uniform channel upper estimate 1 for both signs. The circular
phase envelope reaches pi; the corresponding displacement-exponent maxima
are 0.821214144857 and 0.547476096571.
This coarse envelope does not establish a large actual intermediate error.
Its first maximizing case/segment indices are `(0,1)` and `(25,1)`.
It is a compensated-frame comparison, or one with the same known unary
evolution included in both models. No unconditional all-time validity
certificate was earned. The optimized endpoint bound is a different quantity.

## Source scope and numerical validation

All three declared Hamiltonians have zero protected electronic response.
Their endpoint factorization is `I_P tensor U_(A,bus)` after ideal adjoint
unhide; all 3125 protected labels are therefore covered by the 25 active
branches. The complete protected/source-reference marginal is preserved
under this assumption, including arbitrary electronic correlations. Real
spectator darkness, finite control pulses and the full informative-contact
source obstruction were not retested or removed by this calculation.

The numerical campaign covers two signs, 25 branches, 80 segments and 256
midpoints per segment: 1,024,000 midpoints per model per invocation.
Independent Python integration checks all 81 segment boundaries plus eight
fixed interior nodes for every branch/sign, totaling 4450 locations.
Maximum alpha discrepancy: `2.2204460492503131e-15`; phase/unary discrepancy:
`1.2289058659575858e-12` rad. Maximum C++ scalar/SIMD discrepancy:
`8.8817841970012523e-16`. All are below their preregistered tolerances.
All four diagnostic trees were identical after removing only the three timing
fields. Every scalar and SIMD invocation verified 80 unique CPUs/places.

## Complete timing projection

Platform: Debian GNU/Linux 13, x86_64, Python 3.13.5; GNU C++ 14.2.0.
Topology: 40 physical cores, 80 logical CPUs, two packages and two NUMA nodes.
Compile from the probe directory with an external output path:

```sh
g++ -O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math -fno-tree-vectorize trajectory.cpp -o /tmp/trajectory
```

The AVX-512 target is explicit in the C++ function attribute. The kernel
combines SIMD trajectory arithmetic with scalar special-function evaluation;
it is not a claim that every instruction uses 512-bit vectors. Scalar checking
uses the same 80-thread topology and runs before the timed SIMD pass.

| Invocation | C++ preparation (s) | Scalar scan (s) | SIMD scan (s) | Process wall (s) |
|---|---:|---:|---:|---:|
| warmup | 0.125262797 | 0.045594696 | 0.012718270 | 0.216910498 |
| measured_1 | 0.124845376 | 0.044108801 | 0.011873735 | 0.217721434 |
| measured_2 | 0.125122162 | 0.044801068 | 0.012066556 | 0.215774335 |
| measured_3 | 0.124131771 | 0.044773567 | 0.012028687 | 0.214318980 |

Measured SIMD median: **0.012028687 s**.
Whole numerical campaign: **2.887861272 s**, including
1.848810667 s for input/independent-fixture preparation,
all four validated invocations, parsing, repeat and custody checks. Process
duration includes child-wait overhead. SIMD timing excludes preparation,
scalar checking, final channel comparisons and output serialization; its
OpenMP end barrier is included. No fastest-run substitution was used.
Compilation was separate: 4.221145933 s. The separate exact
audit took 1.567317182 s. Transfer and source preparation are excluded.
These are computational times; the ideal pulse schedule remains 500 us.

## Custody

Source pin: `604bad993830222ab8c34cee6f31a7a36043e350`.
All nine public files were read back byte for byte before the first execution. The first
exact and numerical processes exited zero with empty stderr. Sources and
the binary were hashed before use and remained unchanged. The complete
39-file raw evidence archive was retained privately and independently checked
byte for byte; private paths and machine identifiers are excluded here.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| Raw evidence archive | 1117255 | `ce59cf7ca2797d5cde8dc68423359c87a92c9482bdcd2350276fa96b7d436574` |
| numerical/input.txt | 2442175 | `4bbb0431b26a4b0e10a212c252bdad15febd152cdd54250e4f8e8767ef255c6c` |
| numerical/independent-fixtures.json | 3574638 | `dba1fe747817007a63398f403103f37a2607952da51f3a3186720c68c41526fc` |
| numerical/result.json | 86261 | `3ff307c1f84864958950c05e3d02b6d829093df725275077e37a6f03d3d81d4a` |
| Compiled executable | recorded outside public checkout | `b098bc4ef7ab5d2c4074fd850ce4bb681c9507f3f6c336a2430685226ab71d9d` |

The public frozen input/source suffices to reproduce the calculation.
Required exact CI has a separate byte-identity contract; floating results
remain ordinary numerical estimates, with no experimental or Canon status.
