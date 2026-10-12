# Result: DP5/N384 passes the short continuous-prefix comparison

Status: C

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering evidence.
Original record Apache-2.0, A. M. Thorn, 2026-10-12.

**CONTINUOUS_PREFIX_SPEED_AND_BOUND_SCREEN_PASSED.** With unchanged
pulses, the fixed A,C,C,A panel completed in 541.4358367137611 seconds.
RK4/N512 is arm A; two consecutive DP5 halfsteps per N384 certificate
cell with the inherited three-point Hermite quintic is arm C. Each
case/batch was initialized once and advanced through four adjacent
48.828125 ns blocks, retaining both state and cumulative certificate.
The total active prefix is 195.3125 ns. This replaces the predecessor's
independently reset windows with an actual initial-value trajectory
prefix of the same compensated model.

Both matched comparisons classified all 2880 checkpoint/case/column rows
COMPATIBLE, with zero INCONSISTENT and zero UNRESOLVED. The exact saved-
dyadic condition epsilon_C <= epsilon_A passed for every row in both
comparisons. The separate strict program-time criterion also passed.
No pulse, tolerance, threshold or source changed after the pin.

| Two-observation median | RK4/N512 A | DP5/N384 C | Observed A/C factor |
|---|---:|---:|---:|
| Kernel seconds | 71.88849217817187 | 57.79166380036622 | 1.2439249443743532 |
| Program end-to-end seconds | 136.77622311748564 | 100.37065240740776 | 1.362711308902392 |

These timings cover both angles together. Each median is the arithmetic
mean of two observations; no statistical confidence or general speed
guarantee is claimed. Preparation varied substantially: the two A runs
took 76.0088607967 and 49.1916612796 seconds to prepare. The end-to-end
factor therefore includes preparation variability. Every observation,
including the first A run, is retained in COMPARISON.md. Method, dense
curve, substeps and certificate density change together; the panel does
not isolate the effect of integrator order.

| Active elapsed time ns | A maximum, +4*pi/5 | C maximum, +4*pi/5 | A maximum, -4*pi/5 | C maximum, -4*pi/5 |
|---:|---:|---:|---:|---:|
| 48.828125 | 7.76886781316e-8 | 3.20815769029e-8 | 6.30866529437e-8 | 2.36547388287e-8 |
| 97.65625 | 1.63623597316e-7 | 7.92298882066e-8 | 1.32804315924e-7 | 5.63306947788e-8 |
| 146.484375 | 2.56765051404e-7 | 1.36881558088e-7 | 2.08205643353e-7 | 9.55585319953e-8 |
| 195.3125 | 3.54859488296e-7 | 2.07737693882e-7 | 2.87089347057e-7 | 1.43477444429e-7 |

Each maximum is over the three cases and 120 retained initial columns
for that sign, at the same active elapsed time. Decimal maxima above are
rounded upward from saved binary64 values. They are cumulative
vector-norm error upper bounds, not observed true errors or gate
infidelities. Cases have different absolute onset times, so these
maxima do not describe simultaneous intercase coherences.

| Angle | A columnwise E4/E1 range | C columnwise E4/E1 range |
|---|---:|---:|
| +4*pi/5 | 3.51888070025 to 6.03647693196 | 3.64252172663 to 7.66316600217 |
| -4*pi/5 | 3.50106649963 to 5.98037250180 | 3.49196474496 to 8.12491163591 |

Growth ranges are outward decimal enclosures of exact rational quotients
of the same column's saved bounds; there were no zero denominators.
Bounds need not grow linearly. A smaller initial C bound can have a
larger relative growth factor while remaining below A at every tested
checkpoint. No growth threshold was imposed. Differences of cumulative
bounds are reported as diagnostics, not separately certified block
errors; cumulative checkpoint totals are never added together.

The largest matched C/A cumulative-bound ratio over all checkpoints was
0.829375647215 for the positive angle and 0.785417659126 for the negative
angle (upward decimal displays). The two formerly exposed column-36
targets, occupation (0,0,0,0,0,0,3), cases 0 and 3, pass at every checkpoint
in both comparisons. Their final C/A ratios lie respectively in
[0.238053503493, 0.238053503494] and
[0.219985769277, 0.219985769278]. Full component and growth tables are in
COMPARISON.md.

Each child recorded 90 initializations, 270 byte-exact state/certificate
carry checks, and 360 snapshots. Polynomial-start and cumulative-
component checks passed at all 1440 A or 1080 C certified cells. Saved-
output auditing checked 21,600 component monotonicity comparisons and
2880 directed totals per child. Monotonicity alone is not evidence of
state continuity: the reviewed harness and its actual byte-exact carry
assertions supply that additional check. No phase fitting or state
normalization is present.

The five state/component/basis/layout/metadata payloads agree byte for
byte in each same-arm repetition. A separate remote saved-byte audit
also found every first checkpoint identical to the predecessor's first
window. Large endpoints remain in the private remote evidence; the
downloaded compact archive includes their size/hash receipts, the
comparison records and all component bytes. Local saved-output review
does not independently rerun those endpoint comparisons or the floating
campaign. Source/input/binary custody, runtime fixtures, AVX-512F/DQ/VL,
eighty-worker placement and post-run process closure passed.

The immutable source pin is
`4c3a29e3ce4db210b754cd18e5340b805f8c5df7`.
All fifteen sources plus SOURCE_SHA256SUMS were publicly read back before
execution. The first exact supporting gate passed with exit zero and
empty stderr; EXPECTED.txt and RUN.md preserve its actual output and
receipt. Later exact CI replay audits algebra/geometry/negative fixtures,
not a second execution of the floating numerical experiment.

The earlier inactive prefix is exactly dark in the declared compensated
model. Cases (4,3)/(4,4) first activate at 100 us, and (1,1) at 400 us;
absolute time and linear history are retained. All four blocks stay
inside the first occupied segment and cross no amplitude switch. The
seven modes, L8/G10 truncation and all 120 retained thermal columns are
unchanged. Full-program prepared.final/delta/rotation values were not
used as prefix endpoint observables.

The result supports DP5/N384 for this short continuous workload. It does
not close the full-pulse error account, full thermal state, final gate
coherences, all-input source/reference preservation, physical feasibility
or energy/work account. The compensated model's omitted uncompensated
unary phase is not treated as a common phase at intermediate times.
Exact-darkness and unknown-source no-imprinting boundaries remain intact.

All first outcomes were retained without retry, repair, discarded warmup
or extension. No long run or automatic successor was started. This
identifier is sealed; a further numerical scope requires a new
preregistration and source pin.
