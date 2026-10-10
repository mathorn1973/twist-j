# Gaussian branch-kernel and exact pulse-fixture preregistration

PUBLIC NON-CANONICAL; conditional L1 calculation and engineering appendix.
Date: 2026-10-10. Original text Apache-2.0.

Complete source candidate for public immutable pin. No scientific execution precedes that pin and readback.
The custody fields below are not measured data.

```text
probe_id: P-U-CA40-PAIR-KERNEL-1
branch: probe/P-U-CA40-PAIR-KERNEL-1
public_issue: https://github.com/mathorn1973/twist-j/issues/1450
authority_base: 94ccde4408de312d515b57ede6102d2081604ec9
authority_and_collision_readback: reservation #1450; remote heads, current relevant open issues, probes and registry checked; main policy run 38064991158 success at authority_base
```

The pin commit and this file's final hash are recorded externally in RUN.md
after pinning; do not insert a self-referential hash into this file. The full
Git commit binds every source. The source custody list is:

| Public file | Purpose | SHA-256 custody |
|---|---|---|
| verify.py | Renamed exact verifier preparation source | Bound by immutable pin and RUN.md |
| contact_bench.cpp | Scalar/AVX2/AVX-512 engineering kernel | a8d39443fcdba1d79baf54044c97f38718a093673b92c04d1a99f17d74128309 |
| run_benchmark.py | Benchmark runner | 16aa85a9f98ede6dd7f9526a51cb37f5336e30b1a205ce69909508f8217f5d4e |
| README.md | Model, interfaces and scope | d40f8714cb5170d243401a03843423440b8f2ac5a285d82b8318572ad907791e |
| Build recipe | Inline below and in README.md; no separate file | Bound by immutable pin |

The equations, synthetic workload and ideal checks are already designed;
this is not a blind prediction. Authors have shared the mathematical task
and reporting contract. Static cross-review is disclosed. No first-run
outputs, successful timing claims or fabricated EXPECTED.txt are preregistered.

## 1. Equation and question

For each synthetic context c and full label z in F5^7, with active physical
ions 4,5 and spectator ions 1,2,3,6,7, freeze

```text
theta_c = sigma_c*4*pi/5,  sigma_c in {-1,+1},
alpha_(c,m)(z) = a_(c,m) + sum_(i=1)^7 A_(c,m,i)(z_i), m=0,...,6,
epsilon_c(z) = sum_i u_(c,i)(z_i)
             + sum_(i<j) v_(c,i,j)(z_i,z_j),
Phi_c(z) = theta_c*[z_4!=z_5] + epsilon_c(z),
r_c(z) = sum_(m=0)^6 ((m+1)/2)*
          (Re(alpha_(c,m)(z))^2+Im(alpha_(c,m)(z))^2).
```

A(0)=u(0)=v(0,b)=v(a,0)=0. Seven common complex displacements a_m are
retained; only the common scalar phase is zero. There are 203 complex
displacement coefficients (seven common and 196 nonconstant A entries),
28 unary terms and 21*16=336 pair terms: 364 nonconstant phase terms.
This is an additive-displacement/pair-phase branch kernel, not an integration
of a laser waveform or a claim that arbitrary tables have one physical source.

The reported model-only `synthetic_bound` is
min(1,sqrt(2-2*exp(-R)*cos(E))), using separate uniform maxima
R=max_(c,z) r_c(z) and E=max_(c,z)|epsilon_c(z)|. The fixed coefficient
ranges give E<=49/2048<pi/2 and r<=7/262144, so using the separate maxima is
a conservative bound on the per-branch Gaussian comparison, not its exact
maximum. The implementation evaluates the equivalent stable expm1/sine form.
This interpretation assumes fixed independent product-thermal motion with
nbar_m=m/2 and the declared Gaussian model. It is not a hardware bound.

The exact question is finite ideal pulse-word and phase-fixture conformance
under roots-of-unity arithmetic. The floating question is whether the frozen
scalar and SIMD implementations agree on the stated validation contexts,
and how fast the complete frozen synthetic workload runs under explicit
placement. These two outcomes have separate evidential scope.

## 2. Code and accepted methods

The formal entrypoint `verify.py` is the final renamed `verify_exact.py`
preparation source. It uses only the Python standard library and exact
integer exponents modulo 20 for phase roots. It performs both-sign full-code
checks and its frozen negative fixtures. It produces one deterministic JSON
line and returns zero only when its assertions pass; no timing is in that
scientific stdout. It never imports or launches the floating implementation.

`contact_bench.cpp` supplies a scalar implementation and four/eight-lane
FP64 implementations for AVX2/AVX-512. Use no fast-math and no FMA/floating
contraction. The frozen build recipe is

```text
g++ -O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math \
  -fno-tree-vectorize contact_bench.cpp -o /absolute/external/path/contact_bench
```

Per-function target attributes select the SIMD instruction sets. Actual
compiler version and binary hash are recorded after compilation.
Unsupported ISA is rejected, not emulated under the requested backend name.
Maxima/checksums use the fixed source ordering; no outcome-dependent tuning.

Every invocation validates before its timed workload; `--validate` performs
only validation and exits. Validation compares the selected backend against compiled scalar
over all 78,125 labels of each of contexts 0,1,510,511. The absolute numerical
tolerance is 1e-12 for each reported validation comparison. This is a shared-
source reference comparison, not a fully independent implementation. At labels
0,1,15624,39062,54321,78124 in each validation context, separately decoded
digits and reverse-order long-double contractions supply point checks at the
same 1e-12 threshold. Target/residual reconstruction is checked there too.
The frozen Gaussian tests require a closed displacement square's Weyl phase,
Hermitian/diagonal kernel behavior, a fixed Weyl-sign value, displacement
inverse and a nonzero common-displacement witness, at tolerance 1e-14.

`run_benchmark.py` accepts --binary, --output, --rounds and --repeats, together
with its frozen source-custody options. Freeze rounds=5, repeats=4 and the
binary's candidates=512. The runner requires one complete finite JSON object,
exit zero and empty stderr, valid numerical results and the exact requested
thread/CPU map. NaN and Infinity are rejected. Every completed or timed-out
child has its output and outcome retained before a failure stops the run.
The runner also requires the reported 512 candidates, four repeats and exactly
160,000,000 processed branches, with finite nonnegative max_abs_error<=1e-12.
Checksum, phase_max and r_max must agree numerically exactly across all 24
invocations against the first warmup. A mismatch is preserved and stops the
campaign; it does not authorize choosing a new tolerance after seeing results.

Repository replay uses `python3 probes/P-U-CA40-PAIR-KERNEL-1/verify.py`, with the
ordinary 600-second verifier limit. The benchmark child limit is 55 seconds.
Compilation and static review are allowed before pinning. Neither exact
science execution, the binary validation nor timed candidate evaluation is
allowed before the complete candidate is public and read back byte for byte.

## 3. Carrier, synthetic data and fixed inventory

The full code carrier is F5^7, with 78,125 labels; temporary shelving in the
ideal-word verifier is represented explicitly in its frozen discrete model.
For the exact nominal check use both signs: 156,250 sign/label cases. Freeze
six negative fixture families: wrong angle, wrong unhide, missing cycle,
global spectator echo, active-spectator phase, spectator-spectator phase.
The exact source defines each fixture and the observable that must expose it.
An endpoint permutation alone is insufficient to detect phase imprint.

The engineering generator has 512 deterministic contexts, 256 per sign.
Its 32-bit integer hash is a function of frozen indices, with no runtime randomness.
Coefficient scales are 2^-16 for A, 2^-12 for u and 2^-14 for v; label-zero
entries vanish and common displacements have scale 2^-16. Hash values map
to integers (h modulo 17)-8, hence [-8,8]. The source fixes index ordering;
even context indices use positive sign, odd negative. Contexts divisible by
64 are replaced with zero-error coefficients, yielding eight positive-sign
ideal fixtures. These definitions cannot change after pinning. The target
phase is analytically removed in the scanner; alternating signs do not mean
that two physical force waveforms were independently integrated.
The residual phase stays inside [-49/2048,49/2048]. No measured calibration or external
hardware dataset is loaded. The synthetic mode weights are (m+1)/2.

One complete scan evaluates 512*78,125=40,000,000 context/label pairs.
Four repeats evaluate 160,000,000, excluding setup and validation. Four
configurations are fixed: (AVX2,40), (AVX-512,40), (AVX2,80), (AVX-512,80).
Each has one warmup followed by five measured samples, with round-r order
the base order cyclically rotated by r modulo four. Report all samples.

The target topology is a Linux affinity set with 80 logical CPUs, 40 physical
cores, two threads per core, two packages of 20 cores and two NUMA nodes.
Use one allowed thread per physical core for 40, and both for 80. Explicit
OpenMP places, fixed binding, disabled dynamic teams and no nested/secondary
runtime oversubscription are frozen. A detected mismatch stops the campaign;
the operator does not quietly replace the declared comparison with another.

## 4. Systematics and limits

- Floating arithmetic is a labelled engineering witness. No numerical bound
  is promoted to exact arithmetic merely because this dyadic fixture is easy.
- Scalar/SIMD paths share the model and source; they can share a systematic
  error. The exact verifier audits its stated fixtures, not every C++ branch.
- CPU/OS ISA support, compiler, FMA contraction, vector implementation,
  affinity, NUMA placement, page faults, frequency/power state, thermal drift
  and background load can change timings. Record actual supported metadata.
- Thread binding is checked from actual worker CPU reports. Warmups and the
  five rotated rounds are retained; no best-run selection or silent retry.
- The kernel's A/u/v tables are synthetic residuals, not jointly fitted
  light-shift profiles, multimode waveforms or measured error channels.
- Carrier leakage, scattering, heating histories, nonthermal correlated
  motion, detector errors and all 1848 experimental settings are outside this
  first implementation. No laboratory confidence interval is manufactured.
- The fixed product-thermal characteristic-function interpretation of r is
  conditional. It is not a physical reset law for a sequence of 56 gates.

## 5. Frozen failure thresholds and disposition

| Layer | PASS condition | Failure/incomplete disposition |
|---|---|---|
| Exact finite audit | Every exact assertion and required negative fixture passes; deterministic stdout, exit 0, empty stderr | Preserve exact failure; do not revise its target after inspection |
| Numerical backend validation | Every frozen comparison finite and absolute discrepancy <=1e-12 | Numerical validation FAIL; no performance claim from that invalid campaign |
| Workload identity | Correct 512 contexts, both signs, all 78,125 labels, four repeats, valid maxima/checksums | Invalid workload FAIL |
| Placement and execution | Exact requested workers/CPUs, valid topology/ISA, valid JSON, no timeout or process error | Preserve failure/unsupported outcome and stop |
| Timing | Five valid samples per configuration, with frozen warmups/order | Report medians and spread; no universal speed threshold or presumed AVX-512/SMT win |
| Physical feasibility | Not assessed by this fixture | No hardware PASS is available |

The engineering threshold is implementation agreement, not a gate fidelity
threshold. A slower backend is a measured performance result, not a scientific
falsifier. Timeout is reported as failure to complete under the declared
budget, not mathematical impossibility. Missing physical calibration cannot
be turned into a gate certificate by increasing benchmark speed.

If a formal verifier pin does not complete, follow the repository's abandoned-
pin rules and preserve the reason; never reuse the identifier. If it completes
and a falsifier fires, retain that outcome rather than relabel it abandoned.
Do not change sources, datasets, thresholds or comparison schedule after pin.

## 6. Action layer, custody and publication

Action layer: L1, conditional finite-state/code-model audit only. The Gaussian
kernel is a separate floating engineering comparison, not an L1-to-physical
admission bridge. No Canon, experimental occurrence law, full-source quantum
preservation or complete seven-ion hardware result is earned by this run.

After the exact run, write EXPECTED.txt and neutral RUN.md fields including
pin_commit, verifier_sha256, exact command, platform, architecture, Python,
exit code, stdout hash/bytes/lines and stderr hash/bytes. RESULT.md states the
earned outcome and limits. Required x86_64 and aarch64 workflow replay remains
unchanged; the floating executable is not added to that exact-output gate.

Benchmark source/binary/runner hashes and raw child outcomes are retained in
a fresh external output directory. Do not commit compiled objects, binaries,
private metadata, .log or .jsonl files. Public engineering summaries use neutral
platform/core/ISA descriptors, with no machine nicknames or private paths.
Any numerical appendices are clearly labelled and reviewed before publication.

