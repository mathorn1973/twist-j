# Full-pulse approximation audit: preregistration

PUBLIC NON-CANONICAL. Conditional L1 mathematics and floating engineering.
Original text Apache-2.0. Date: 2026-10-11.

```text
probe_id: P-U-CA40-TRAJECTORY-VALIDITY-1
branch: probe/P-U-CA40-TRAJECTORY-VALIDITY-1
public_issue: https://github.com/mathorn1973/twist-j/issues/1454
authority_base: 9568bc89867d705e7b9e43951a238c9c44318c0f
owner: A. M. Thorn, coordinated source-preparation session
```

This freezes a new audit of the already completed nominal waveforms in
P-U-CA40-WAVEFORM-SOURCE-1. It does not rerun their construction or optimize
their parameters. No new scientific computation is executed before the
complete source is committed, pushed and publicly byte-read back.

## 1. Equation and question

Keep the seven axial harmonic modes, physical order `(s,x,u,y,w,q,r)`,
active ions A=(4,5), protected ions P=(1,2,3,6,7), and the two original
nominal waveforms. Each has five 100-microsecond loops of 16 equal constant
segments, with ideal instantaneous X5 after each loop. Protected electronic
responses are identically zero. All 25 active labels represent the entire
5^7 electronic carrier with the 3125 protected labels factored out.

Compare the previous rotating-wave force with the declared full linear force:

```text
kappa_mi = Delta_k b_mi sqrt(hbar/(2 M omega_m)), real,
eta_mi = kappa_mi exp(i Delta_k x_i),
g_m(z,c) = sum_(i in A) eta_mi [(z_i+c) mod 5 = 0],
f_R,m = u(t) g_m exp(i(omega_m-mu)t),
f_L,m = f_R,m + u(t) conjugate(g_m) exp(i(omega_m+mu)t).
```

The full linear force is the first displacement derivative of the explicitly
selected sine-potential parent in DERIVATION.md. The previous RWA model does
not uniquely determine this optical parent or its microscopic implementation.
Its zero-displacement diagonal term and endpoint phase must be accounted for;
no unreported physical correction is inferred from a comparison's common
scalar phase. Carrier durations remain zero, and there is no bus reset.

Questions: how large are intermediate motion and Lamb-Dicke arguments; how
different are the two linear channels; and does a Gaussian-state Duhamel
bound control the nonlinear optical remainder for these unchanged pulses?
The source-preservation claim concerns this auxiliary G block, not the full
informative contact whose unknown-source preservation is already excluded.

## 2. Code and accepted methods

The accepted exact standard-library verifier is `verify.py`, with fixture
contract EXACT-DESIGN.md. It audits rational formal-series identities,
chronological displacement/phase composition, Gaussian moments, remainder
majorants and protected-register factorization. It does not certify a
floating waveform or substitute for numerical model comparison. Its stdout
is deterministic ASCII with an explicit final LF; exit zero and empty stderr
are required for a completed exact audit.

`numerical_run.py` reads the adjacent frozen input.json and supplies the
derived plain-text input to `trajectory.cpp`. It independently evaluates
all segment boundary states and the fixed interior fixture panel in source.
The C++ program uses analytic two-frequency segment integrals, chronological
prefix states, explicit AVX-512 FP64 operations and OpenMP. It evaluates both
models over all branches and all segments. No numerical ODE solver, adaptive
pulse search or outcome-dependent grid refinement is used.

For each of the 50 sign/branch cases the independent panel contains all 81
segment boundaries and these eight interior `(segment, fraction)` nodes:
`(0,1/512), (0,511/512), (15,255/512), (16,1/512), (39,257/512),
(40,1/512), (64,255/512), (79,511/512)`. These are 4450 fixture locations,
each checking both linear models, their phases and the raw unary ledger.

Freeze 256 equal subintervals per segment, midpoint evaluation and analytic
derivative envelopes extending to the whole subinterval. There are 4000
branch/segment tasks and 1,024,000 midpoints per model. Full-linear Gaussian
moments, not RWA moments, enter the nonlinear comparison. Report sampled
maxima separately from intersample upper estimates. The mathematical
inequalities apply to exact values; ordinary FP64/libm evaluations and
tolerance checks are not outward-rounded interval certificates.

Compare every C++ scalar/SIMD summary, plus an independent Python panel.
Use one warmup and three measured invocations, preserving all timings.
Each invocation contains scalar validation separately from the timed SIMD
scan. Freeze 80 OpenMP workers with 80 unique allowed logical CPUs, explicit
places, dynamic teams disabled; record the actual CPU/place map. Compiler:
GNU C++ with `-O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math
-fno-tree-vectorize`, plus explicit AVX-512 targeting in source or compiler
flags. Record the exact command and binary hash. These switches do not imply
portable floating bit identity or a hardware performance guarantee.

The fixed topology is 40 physical cores, two SMT threads per core, two
20-core packages and two NUMA nodes with 20 complete cores each. The runner
requires all 80 logical CPUs and binds one worker to each explicit place.

The endpoint channel comparison permits exactly one common scalar phase
per complete sign/program. Freeze the finite stationary/crossing candidate
enumeration in source; never fit individual branch phases. Retain raw phase
differences. Also compare all 300 unordered two-branch coherent inputs per
sign by their full complex reduced-channel factors. These give actual
trace-distance witnesses in the two stated linear models, distinct from
conservative upper bounds.

A separate all-time RWA diagnostic uses one analytic midpoint state per
original segment and a derivative envelope covering that entire segment.
With delta_z=Phi_L-Phi_R+Im(conj(alpha_R)*alpha_L), its exact derivative is
Im[(dot(alpha_L)-dot(alpha_R))*conj(alpha_L+alpha_R)], summed over modes.
Use the fixed same-time branch00 anchor gamma(t)=delta_00(t) for each sign.
DERIVATION.md specifies the resulting phase/displacement envelope. This
coarser 4000-state calculation is distinct from the 256-cell LD/motion grid
and the optimized endpoint comparison. Report it even if its bound is
trivial. It compares compensated frames, equivalently physical models with
the same known unary phase added to both; it does not silently remove that
phase from only one intermediate physical evolution. Only at the endpoint
is the inherited unary phase common to every branch. No all-time accuracy
claim follows solely from a passing endpoint screen.

The Gaussian remainder uses the nonnegative decomposition in DERIVATION.md,
with the source's fixed small-variance series for sinh(v)-v. Publish the
uncapped midpoint sum, continuous envelope, quartic alternative and
Lipschitz allowance separately. The series and FP roundoff are not a
rigorous upper rounding rule.

## 3. Carrier and data

`input.json` is a lossless selection of config, modes and pulses from the
completed predecessor model, SHA-256
`fb9fe824c7f925ad1690f7f7f4a150deafdd57c4e683007586da4bddddc87e15`
(1,240,110 bytes). Its producing source pin is
`1e078f6281b8f9ce813b6f08200d9caedf1bac14`; its public result is in
merge `9568bc89867d705e7b9e43951a238c9c44318c0f`. Extraction reads old
results only, performs no solver or rounding, and introduces no measured
apparatus data. The small selected input is public and sufficient for replay.

Mass is 40 atomic mass units, axial frequency 1 MHz, beatnote offset 20 kHz,
wavevector 2*pi/(397 nm), thermal occupation 0.05 in each of seven modes.
The exact decimal constants and pulse amplitudes are in input.json. The
initial product thermal bus is independent of electronic/reference states.
Electronic states and external reference correlations are otherwise arbitrary.

The full potential remains a conditional, prescribed classical-control
Hamiltonian. The microscopic light-shift calibration, finite controller,
radial confinement, heating, scattering, decay and finite carrier pulses
are outside this test. No finite Fock truncation is used. Gaussian moments
include unbounded thermal tails; a small RMS is not a uniform support bound.

## 4. Systematics

- Both numerical implementations share physical assumptions and frozen data;
  independent chronology and algebra checks cannot eliminate model error.
- The sine parent is a specified comparison model, not a uniquely justified
  Hamiltonian of a real apparatus. Account for its scalar/unary term explicitly.
- Seven-mode harmonic motion is retained in both comparisons. Adjacent
  displacement divided by equilibrium spacing is a geometric diagnostic,
  not a rigorous bound on the singular Coulomb remainder or radial stability.
- A large Duhamel upper bound is inconclusive about the actual nonlinear
  error. A positive lower witness for the RWA comparison has a different
  logical meaning. Report uncapped error integrals when caps become trivial.
- No threshold, grid, waveform, input, model or reference panel changes after
  the pin. No favorable subset or fastest invocation replaces the full result.
- Runtime varies with frequency, NUMA, load and compiler. Keep compilation,
  process duration, validation and SIMD kernel timings separate.
- None of these calculations is a total energy/work account, a physical
  contact demonstration, a full 56-G circuit simulation or a Canon fold.

## 5. Frozen thresholds and disposition

| Check | Requirement and interpretation |
|---|---|
| Exact audit | All exact identities and controls, exit 0, empty stderr, deterministic stdout |
| Input/execution | Frozen hashes, finite outputs, successful required processes, 80 unique worker placements |
| Independent analytic integration | Maximum absolute alpha discrepancy <=1e-9 and phase discrepancy <=1e-8 radians |
| Inherited input/target consistency | eta reconstruction discrepancy <=1e-12; nominal RWA endpoint alpha <=1e-9 and target phase pattern discrepancy <=1e-8; unary endpoint branch spread <=1e-8 radians |
| Scalar/SIMD | Each diagnostic finite and absolute discrepancy <=1e-9 (relative tolerance 1e-12 where source specifies large aggregates) |
| Repeat consistency | Diagnostic values agree at absolute/relative 1e-12; exact case order and witness indices |
| RWA approximation screen | Common-phase channel upper estimate <=1e-3 for each sign |
| RWA failure witness | A fixed-panel trace-distance witness >1e-3 establishes threshold violation in the declared linear comparison |
| Optical linearization screen | Full-duration Duhamel upper estimate <=1e-2 for each sign |
| Lamb-Dicke heuristic | Maximum RMS argument <=0.1; diagnostic only, never sufficient for a channel guarantee |

The numerical outcome is a SCREEN result, not a rigorously interval-certified
bound. If an upper screen misses and no lower witness fires, its disposition
is NOT_CERTIFIED_BY_THIS_BOUND, not proof that the physical gate fails.
Numerical inconsistency makes dependent interpretations INCOMPLETE. Preserve
every exit, timeout, stderr and partial result. A completed exact audit and
an inconclusive or failed engineering screen can coexist.

Freeze a 180-second watchdog for each scanner invocation, 600 seconds for the
exact audit and 1800 seconds for the complete numerical coordinator. No
outcome-dependent rerun or replacement candidate is allowed. If the exact
formal gate never completes, preserve the immutable pin and close ABANDONED
under POLICY.md with no invented EXPECTED.txt/RUN.md; the identifier is spent.

## 6. Action layer and custody

Action layer L1. Canon v101 and all physical-admission obligations remain
unchanged. This work is theoretical and numerical only.

Complete and review every scientific source and declaration, freeze
SOURCE_SHA256SUMS, commit and push, publicly read back all bytes, then fetch
the exact pin into a clean Linux checkout. Only static inspection, AST parsing
and compilation are allowed before that boundary. Hash sources, input and
binary before use and recheck sources after execution. Keep raw records,
private paths, machine names, binaries and generated bulk outputs outside
the public repository.

After execution copy exact stdout into EXPECTED.txt; write neutral RUN.md
with pin, command, versions, exits, hashes and byte counts. RESULT.md separates
algebraic and floating dispositions. Publish a reviewed numerical summary.
Required unchanged x86_64/aarch64 CI replays the exact verifier; it does not
claim floating bit identity. Finish by reviewed merge commit and green main
checks. No amend, rebase, squash, force push, workflow change or Canon edit.
