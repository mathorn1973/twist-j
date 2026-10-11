# Exact supporting audit for P-U-CA40-CLOSURE-PERF-1

PUBLIC NON-CANONICAL conditional L1 engineering witness.
Reservation: https://github.com/mathorn1973/twist-j/issues/1462.
Authority base: `264d792eb433c9a032f6282b3c7800ee1837f73b`.
Mutable preparation until the coordinator seals the complete source pin.
No Canon promotion, new physical theorem, or hardware admission is proposed.
No execution or import of this verifier is authorized before the public source pin.

## 1. Frozen comparison scope

The proposed campaign compares the sealed BALL implementation with the new
memory-traffic optimization, using the same pulses and model input. The source
baseline is P-U-CA40-BALL-CLOSURE-1, pin
`ab33a3f42af66b9bfa52915871b10ce3d914c124`. Its kernel SHA-256 is
`e84a7071fcbd10461bbce54e30638ecd68845fe0cc0a901e827be0d2bd9cfee8`.
The reviewed optimization before the common prefix harness has SHA-256
`9ba07011d2405e609eb84be8cb5d7781bb06b7cc50be53fbd5304ac5fa93c3f2`.
The coordinator must pin the final instrumented sources and disclose their
diffs before execution; those final hashes must not be inferred from these
pre-harness identities.

The frozen workload is L=8, guard G=10, 512 subdivisions per occupied segment,
80 threads, six cases spanning both signs, and all 120 retained thermal
columns. Only the first four occupied cells of each trajectory are evolved.
This is not four complete pulses and is not a full-trajectory comparison.
There are 90 eight-column tasks. The six-child order is B,F,F,B,B,F, where B
is baseline and F is optimized. Each child has a 300-second ceiling; the
campaign has a 1,800-second ceiling. The runner's preregistration defines
precise timer boundaries, cleanup, and preservation of incomplete attempts.
No long calculation is authorized by this short engineering experiment.

The implemented changes remove redundant zeroing and copies, use guarded
ownership exchange, and evaluate the polynomial in P_L before one zero
extension. They do not implement table caches, tiled scheduling, in-place
triangular multiplication, smaller quadrature rules, or coefficient dropping.
The predecessor's timing and stack snapshot informed this design: the study
is result-exposed, same-session engineering, not a blinded replication.

## 2. What the exact verifier establishes

`verify.py` is a small independent standard-library rational fixture audit.
It does not read, import, compile, or execute either C++ implementation. Its
one deterministic ASCII JSON line uses an explicit LF byte. It uses no RNG,
network, file inputs, floating-point tolerances, clocks, or external packages.
The main guard makes source import free of test execution, although imports
are also prohibited before this source pin. Assertions use explicit exceptions
and remain active if Python optimization flags are supplied.

The mathematical statements are elementary implementation-support identities,
not new theorems about the ion model. Their application to the C++ code still
requires static review and the separate frozen runtime comparison.

### 2.1 Overwrite and complement clearing

Let the graded basis be ordered by total excitation. For creation, every
target row of P_G is assigned, so previous destination contents are irrelevant.
For annihilation applied to a vector supported in P_L, all rows within P_L
are assigned and every remaining row must be zero. The optimized operation
therefore clears exactly the complement before reusing a destination buffer.
This statement requires disjoint input/output storage. It does not permit an
arbitrary in-place ascending triangular multiplication.

The fixtures enumerate 1, 2, and 3 modes; G=1,2,3; every support L=0,...,G;
every mode; and both triangular directions. Rational complex matrices have
the correct support graph but deliberately generic nonzero coefficients.
They are not claimed to be normalized-Fock displacement coefficients.
Two SIMD-like lanes and separated real/imaginary blocks exercise both zero
ranges. The reference assigns every row from an independent input. The
optimized model begins with nonzero stale destination contents and clears
only the annihilation complement. Every L<G annihilation fixture also runs
the mutant that omits this clearing and requires that mutant to disagree.

### 2.2 Ownership exchange and repeated buffer reuse

For a fixed sequence A_1,...,A_n, copying the initial x into scratch and
copying the final product out equals applying A_1 directly to x, using
ping-pong scratch buffers for subsequent actions, and exchanging ownership
of the final buffer with the output. This assumes x, output, and the two
constructed scratch members have distinct storage. The source must remain
unchanged; destination buffers may contain arbitrary earlier results.

Rational lower/upper matrix words test dimensions 2,3,5, lengths 2,3,14,
and three successive calls with the same recycled scratch objects. Each
result is checked against a separate copy-based matrix product. Object
identities verify that the scratch/output buffers remain distinct. Five
forbidden source/output/scratch alias relationships must raise. A concrete
three-dimensional lower-triangular in-place mutant produces a different
answer and is required to fail.

The fixture models ownership and center-vector equality. The actual Ball
exchange must also move its radius and center-norm bound with that vector;
this is a source-review/runtime obligation, not inferred from list swapping.
The tail shell norms must be consumed before subsequent creation mutates the
annihilation result. Removing its temporary copy does not remove this ordering
requirement. The separate collective reference fixture still needs its half
buffer and is outside this optimization.

### 2.3 Dual Horner and conservative underflow allowance

Let E map P_L into P_G by zero extension and let every polynomial coefficient
c_j be supported in P_L. Since E is linear,

    E(theta p + c_j) = theta E(p) + E(c_j).

The derivative update must use the OLD value:

    d <- theta d + p_old;   p <- theta p_old + c_j.

Consequently the exact polynomial and its derivative can be evaluated in
P_L and embedded once. E preserves the Euclidean norm. A physical derivative
scale 1/h commutes with E as another scalar multiplication. The C++ sequence
must retain the same operations on occupied entries, exact zeros elsewhere,
the paired radius/norm state, and the old conservative U_G allowance.

Fixtures compare small-space and embedded-space dual Horner for dimensions
1,2,4, three guard sizes per dimension, degrees 0 through 5, and five rational
arguments including endpoints and values outside [0,1]. A monomial expansion
independently checks values and derivatives. A new-value derivative mutant
must fail. Exact rational squared allowances verify

    U_D^2 = 2 D [k eta / (1-k u)]^2 <= U_G^2,  D<=G,
    u=2^-53, eta=2^-1074, k in {1,2,12}.

Here D,G denote vector dimensions in that formula, not excitation cutoffs.
This proves dimension monotonicity of the stated allowance. It does not
emulate binary64 rounding, verify an AVX instruction stream, prove gradual
underflow on the target processor, or reproduce the interval norm reduction.

## 3. Expected fixture inventory, derived before execution

The following counts are derived from the source loops; they are not observed
results and are not an EXPECTED.txt file:

| Family | Count |
| --- | ---: |
| Triangular layout cases | 108 |
| Stale-complement negative controls | 36 |
| Ownership/reuse cases | 27 |
| Alias rejections | 5 |
| In-place corruption negative control | 1 |
| Horner/embedding cases | 270 |
| Underflow dimension cases | 27 |
| New-value derivative negative control | 1 |

Runtime is intended to be short; no runtime or successful output is claimed
before execution. The exact verifier does not enumerate the physical 7-ion
state space, propagate thermal states, or establish any error-closure result.

## 4. Separate runtime evidence and outcomes

Only the pinned C++ comparison can establish prefix endpoint byte equality,
agreement of partial certificate bounds, or observed performance. The runner
must preserve the first outcome of every attempted child, including timeout,
nonzero exit, partial output, raw stdout/stderr, and custody failures. It must
compare both implementations and repeated runs under the frozen comparison
rule, check the required 80-thread placement, retain source/input/binary
hashes, and report timing boundaries without changing them after inspection.

An exact-fixture PASS means these rational fixtures passed. A runtime
equivalence PASS applies only to the four-cell panel and the reported fields.
A required performance PASS additionally needs median baseline kernel seconds
at least twice median optimized kernel seconds, after all six invocations
pass strict endpoint/component bit comparisons. This is a frozen engineering
target, not a theorem or guaranteed acceleration. The propagation timer also
includes OpenMP startup, Work/BWork allocation, barriers and progress logging.
An observed mismatch is a failed equivalence test, not a physical falsifier.
A timeout or incomplete panel establishes no complete equivalence or timing
result. Any speed ratio is an observed engineering statistic under the frozen
protocol; no achieved minimum speedup is established by this exact audit. Full-scale
extrapolations, if reported, must be explicitly conditional and separate.

Passing this study does not close the six full-trajectory error radii, show
nonlinear discrepancy for both signs, certify hardware feasibility, admit a
physical source interaction, or authorize a long successor campaign. Neither
zero noise nor physical source-state preservation follows from this test.
The original unnormalized thermal and source/reference accounting remains
unchanged and unclosed at full-trajectory scope.

## 5. Freeze and publication boundary

Before first execution the coordinator completes the current authority
checks, six preregistration fields, final source hashes and public
readback. Compiler/static syntax checks may precede that pin; running this
verifier, importing candidate modules, or launching a prefix calculation may
not. No expected stdout is manufactured from the count table above.

The public outcome is one non-canonical engineering probe with neutral
sanitized receipts. Raw endpoint binaries, machine-specific diagnostics,
private paths, and other campaign evidence remain in the reviewed private
archive with public hashes as appropriate. A supporting exact gate and its
CI replay do not substitute for running the compiled numerical comparison.
