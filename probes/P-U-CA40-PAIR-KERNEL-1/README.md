# Seven-ion Gaussian branch-screen prototype

PUBLIC NON-CANONICAL source candidate. This is the first implemented
branch-evaluation kernel and a proposed benchmark, not a hardware result.
Date: 2026-10-10. Original text Apache-2.0.

Probe: P-U-CA40-PAIR-KERNEL-1. Reservation:
[issue #1450](https://github.com/mathorn1973/twist-j/issues/1450).
Branch: `probe/P-U-CA40-PAIR-KERNEL-1`.
Authority base: `94ccde4408de312d515b57ede6102d2081604ec9`.
The source candidate must be publicly pinned and read back before execution.
No runtime or validation result is claimed here.

The kernel evaluates the algebraic form used by a conditional seven-ion
spin-dependent-force model: seven additive complex motional displacements and
a residual phase with unary and pair terms. It screens every one of the
78,125 five-level basis labels for each synthetic coefficient context.
The initial workload is 512 contexts, 256 for each target sign.

The contexts are deterministic dyadic test coefficients. They are not measured
calibrations or solved pulse waveforms. Their displacement and phase tables
are not claimed to originate from one realizable optical waveform. This
prototype does not optimize all-mode-closed pulses, simulate the complete
experimental measurement panel, or establish error for a real calcium gate.

## Mathematical workload

Let z=(z_1,...,z_7) be in {0,1,2,3,4}^7. Physical ions 4 and 5 are active;
1,2,3,6,7 are spectators. For each frozen context c,

```text
theta_c = +4*pi/5 or -4*pi/5,
alpha_(c,m)(z) = a_(c,m) + sum_i A_(c,m,i)(z_i),  m=0,...,6,
epsilon_c(z) = sum_i u_(c,i)(z_i)
             + sum_(i<j) v_(c,i,j)(z_i,z_j),
Phi_c(z) = theta_c*[z_4 != z_5] + epsilon_c(z),
r_c(z) = sum_(m=0)^6 ((m+1)/2)*|alpha_(c,m)(z)|^2.
```

Label-zero coefficients vanish: A(0)=u(0)=v(0,b)=v(a,0)=0. There are
seven common and 196 nonconstant complex displacement entries, 28 unary
phases and 336 pair phases per context: 203 complex displacement coefficients
and 364 phase entries. Only the common scalar phase is fixed to zero.
The generator keeps |epsilon| <= 49/2048 < pi/2, so this workload does not
exercise a wrapped-phase branch-cut implementation.

The displacement coefficients have scale 2^-16, unary phases 2^-12 and pair
phases 2^-14; common displacements also use 2^-16. Each signed integer lies
in [-8,8]. Values and ordering are defined by the frozen source's deterministic
32-bit index hash, not a runtime random seed. Context sign alternates, even
indices positive; each index divisible by 64 is replaced with zero error
coefficients. These eight zero fixtures consequently have positive sign.
The mode weights are
synthetic; in a product-thermal interpretation they correspond to nbar_m=m/2.
The scanner reports its residual-phase and r maxima and fixed ordered
checksums. It evaluates the residual directly instead of repeatedly adding
and subtracting the same non-dyadic target angle. Thus both target sign labels
are carried, but no positive/negative force waveform is independently integrated.

For a separately justified harmonic Gaussian model with fixed independent
thermal initial motion, the characteristic-function factor is exp(-r).
The executable reports separate uniform maxima R=max_(c,z) r_c(z) and
E=max_(c,z) |epsilon_c(z)|, then the conservative model comparison
`synthetic_bound=min(1,sqrt(2-2*exp(-R)*cos(E)))` after assumed frozen physical
corrections. This bounds the corresponding maximum of the per-branch expression
because R>=r>=0 and 0<=|epsilon|<=E<pi/2. It need not equal that per-branch
maximum. The first optimized scan evaluates r and epsilon, not a measured
channel or a waveform-derived certificate. Even a valid model bound would
not include omitted leakage, scattering, off-resonant carrier errors or
uncharacterized initial motion.

## Two deliberately distinct checks

The formal exact verifier audits the ideal discrete pulse-word fixtures using
integer roots-of-unity exponents modulo 20. It covers both target signs and
all 156,250 sign/label cases, together with declared negative fixtures.
In the public probe its entrypoint is `verify.py`; the preparation source
may initially be named `verify_exact.py`. It uses only the Python standard
library, prints one deterministic JSON line, and never invokes C++.

The floating engineering executable supplies scalar, four-lane AVX2 and
eight-lane AVX-512 FP64 implementations. Its validation compares the optimized
path with the compiled scalar path over all labels of contexts 0,1,510,511,
using absolute tolerance 1e-12. Six fixed branches in each validation context
also use separately decoded digits and reversed-order long-double contractions.
Small displacement/Weyl fixtures use tolerance 1e-14. Scalar/SIMD comparison tests implementation
agreement; it is not independent experimental replication. The exact pulse
verifier does not certify every floating kernel operation or a physical model.

There is no blanket claim that removing FMA and fast-math makes all platforms
bit-identical. Those build restrictions make differences easier to audit.
The engineering output reports actual discrepancies, maxima and checksums.
Nonfinite values, a validation failure, failed process or invalid thread
placement stop the benchmark and preserve the failure record.

## Build and post-pin interfaces

Before the public pin, source review and compilation are allowed; do not run
the scientific verifier, validation switch or timed workload. Compile FP64
without fast-math and without floating contraction/FMA. Keep binaries and
compiler products outside the public repository. Record the actual compiler,
flags and binary hash. The frozen GNU C++ build recipe is

```text
g++ -O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math \
  -fno-tree-vectorize contact_bench.cpp -o /absolute/external/path/contact_bench
```

The source selects AVX instructions in explicit per-function target paths;
the recipe disables automatic vectorization of the scalar reference.

After the complete source pin and public readback, the executable interface is

```text
contact_bench --backend avx2 --threads 40 --repeats 4 --candidates 512
contact_bench --backend avx512 --threads 80 --repeats 4 --candidates 512
```

Every invocation validates before timing. Appending `--validate` runs only
the validation and exits without the timed workload or worker-placement report;
that standalone output is not a benchmark-runner record.

The runner interface is

```text
python3 run_benchmark.py --binary /absolute/path/contact_bench \
  --output /absolute/path/new-result-directory --rounds 5 --repeats 4
```

Supply the runner's source-custody option for every source file named in the
frozen manifest. An output directory must be fresh. The final command and
all actual supported options are bound by PREREG.md and the pinned runner;
these interface examples are not a report of execution.

The declared comparison has four configurations: AVX2/40, AVX-512/40,
AVX2/80 and AVX-512/80. It assumes the runner verifies a Linux affinity set
with 80 logical CPUs, 40 physical cores, two hardware threads per core,
two packages of 20 cores and two NUMA nodes. An incompatible detected topology
is reported instead of silently relabeling 40 arbitrary CPUs as physical
cores. The 40-thread placement chooses one allowed thread from each core;
the 80-thread placement uses both. Explicit OpenMP places, fixed binding,
disabled dynamic teams and single-threaded secondary runtimes are recorded.

Run one warmup per configuration, then five timed rounds with the base
configuration order rotated by the round index. Each measured invocation
uses four complete workload repeats. The workload is 40,000,000 context/label
evaluations per repeat, or 160,000,000 per invocation, excluding validation
and setup. The SIMD implementation additionally visits three padded entries
per context, copies of the all-zero label; these do not change the maxima
or counted scientific workload. Report warmups separately. Five rounds are not a confidence
interval for all future machines or thermal conditions.

The runner records source, binary and runner hashes, actual thread placement,
timing samples and process outcomes. Child timeout is 55 seconds by default.
Missing ISA support, an invalid topology, timeout, nonzero exit, stderr,
nonfinite or malformed JSON, a numerical validation failure, or a numerical
checksum/phase-max/r-max difference from the first warmup is retained
and stops that campaign. No automatically weakened fallback earns a pass.
No speedup or sub-second runtime is promised before measurement.

## Public custody and result scope

Use one newly reserved public probe. Freeze this README, PREREG, exact
verifier, C++ source and runner together before the first scientific run.
The exact verifier supplies the normal EXPECTED.txt/RUN.md/RESULT.md record
and two-architecture replay. The C++ measurements are a labelled engineering
appendix with compiler and binary custody, not byte-identical scientific
stdout for that replay. A correct arithmetic verifier cannot retroactively
turn an unpinned floating run into the formal experiment.

The repository validator accepts the exact entrypoint command
`python3 probes/P-U-CA40-PAIR-KERNEL-1/verify.py`, with exit zero, empty stderr and
byte-identical stdout, under its 600-second limit. A preregistration-only
branch is not yet a mergeable closed probe; complete the run records after
execution rather than fabricate them before the pin.

Local benchmark metadata, samples.jsonl and process-failure records remain
outside the public checkout. The repository forbids unapproved .jsonl/.log
files and compiled binaries. Publish only reviewed, compact engineering
summaries and neutral platform/ISA descriptors; exclude machine nicknames,
hostnames, private paths and credentials. Keep all failure outcomes in the
decision record instead of replacing them with the fastest successful run.

An exact-fixture PASS means those finite ideal-word checks passed. A numerical
validation PASS means the specified implementations agreed on their declared
test inputs. Benchmark timings characterize the frozen synthetic branch
kernel on the reported neutral execution environment. None is a hardware
certificate, a full experimental-panel pass, a seven-ion diamond-distance
measurement, a completed 56-G contact or a physical-admission result.

