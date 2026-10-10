# Shared-waveform and complete-source preregistration

PUBLIC NON-CANONICAL. Conditional L1 mathematics and floating engineering.
Original text Apache-2.0. Date: 2026-10-10.

```text
probe_id: P-U-CA40-WAVEFORM-SOURCE-1
branch: probe/P-U-CA40-WAVEFORM-SOURCE-1
public_issue: https://github.com/mathorn1973/twist-j/issues/1452
authority_base: 7e2b199086a14b2e2183d684e388a42679652a1d
owner: A. M. Thorn, coordinated source-preparation session
```

This is a source candidate, not a run result. All parameters, methods,
thresholds and fixture selectors below are frozen before public pinning.
The candidate can fail its own cap or solver conditions. No successful pulse,
source-preservation bound or runtime is predicted as already obtained.
The scope is theoretical and numerical only; no physical ion experiment is
available or planned under this probe.

## 1. Equation and question

Physical-ion order is `(s,x,u,y,w,q,r)`, active A=(4,5), protected
P=(1,2,3,6,7), source S=(1,6,7). The electronic carrier is F5^7.
For each electronic label z, the interaction-frame Hamiltonian is

```text
H_z(t)/hbar = sum_m [f_m(t,z) a_m^dagger + conjugate(f_m(t,z)) a_m],
f_m(t,z) = u_k exp(i delta_m t) sum_i eta_mi response_i(z_i,cycle),
U_z = exp(i Phi_z) D(alpha_z),
alpha_m = -i integral f_m(t,z) dt,
Phi_z = sum_m Im integral_(t>v) f_m(t,z) conjugate(f_m(v,z)) dt dv.
```

There is no additional diagonal d_z(t) term in this first model. Chronological
composition retains `Im(beta*conjugate(old_alpha))`; segment-local area and
every inter-loop term remain. Final alpha and Phi are generated from the same
force history. Global phase is recorded and the nominal G all-zero branch
fixes one subtraction per target sign; G and E use it in every context.
I uses zero subtraction. No adaptive unary or mixed phase correction is allowed.

The two targets are `I_P tensor G(sigma*4*pi/5)`, sigma=+1,-1, with G
diagonal phase theta*[z4!=z5]. For a product thermal bus independent of all
electronic/reference systems, nu_m=nbar_m+1/2. For a protected-zero anchor
z0 with the same active labels, define

```text
rG(z) = sum_m nu_m |alpha_m(z)|^2,
etaG(z) = wrap(Phi_corrected(z)-theta*[z4!=z5]),
rP(z) = sum_m nu_m |alpha_m(z)-alpha_m(z0)|^2,
etaP(z) = wrap(Phi(z)-Phi(z0)
          + Im sum_m conjugate(alpha_m(z0))*alpha_m(z)).
B(R,E) = min(1,sqrt(-2*expm1(-R)+4*exp(-R)*sin(E/2)^2)), E<=pi/2;
B(R,E) = 1 otherwise.
```

The scanner uses separate maxima R=max r and E=max|eta| for gate and source.
The exact-coefficient formula is a sufficient half-diamond comparison under
the displayed model. Floating evaluated maxima and bounds remain numerical
estimates, with no interval-certified rounding margin. The P comparator
factorizes as identity on P and a channel on A/bus, so its preservation
contract includes arbitrary P/A/reference correlations, with the bus fixed
independently. It is not restricted to a selected source superposition.

The complete informative C negative control is separately expressed in
abstract order `(x,u,y,w,q,r,s)`; its physical order is the fixed permutation
above. It shifts u by -2(y-x)s and w by +2(y-x)s. A sharp informative receiver
and an unknown coherent source cannot retain both a readable record and the
whole source/reference state. Exposing this overclaim is required, not a
failure of the intended pair-gate source-preservation question.

## 2. Code and accepted methods

The complete source inventory is `verify.py`, `model_builder.py`,
`waveform_scan.cpp`, `numerical_run.py`, `MODEL-INTERFACE.md`, `DERIVATION.md`,
`README.md` and this file. A separate `SOURCE_SHA256SUMS` binds their final
bytes before pinning; the immutable Git commit binds that manifest too.
No self-referential pin hash is inserted into these files. RUN.md records
the resulting full pin and PREREG/verifier hashes after execution.

The exact standard-library verifier does not import or launch any floating
program. It uses integer phase exponents modulo 20, Fraction arithmetic and
exact finite permutations/partial traces. Its compact ASCII JSON stdout ends
in one explicit LF written through stdout.buffer. Reuse of the prior ideal
word verifier is credited to its immutable predecessor pin in the source.
The new rational resonant-drive fixture and source controls have their own
explicit scopes; they do not certify the later floating waveform solver.

The floating builder runs once with its complete default dictionary. It uses
damped Newton equilibrium, maximum-pivot Jacobi diagonalization, normalized
closure rows, pivoted twice-reorthogonalized Gram-Schmidt and a projected
2-by-2 interaction eigenproblem. No third-party numerical package, alternative
solver, root-polynomial fallback, different detuning or new segment count is
substituted after a failure. `MODEL_BUILT_NOT_VALIDATED` is construction only.

`numerical_run.py` independently integrates every one of the 80 absolute-time
segments on the frozen validation branches. It does not call the builder's
factored loop coefficient routine as its independent reference. It also
evaluates the fixed Bell controls, serializes coefficients for the scanner,
and preserves all process outcomes and raw outputs externally.

`waveform_scan.cpp` scans every branch with explicit AVX-512 FP64 and compares
all branch summaries against its scalar path before each separate timed scan.
Freeze GNU C++ flags `-O3 -std=c++20 -fopenmp -ffp-contract=off
-fno-fast-math -fno-tree-vectorize`; build outside the public checkout.
Record compiler version, full command and binary hash. No promise of portable
bit identity is inferred from disabling contraction or automatic vectorization.

## 3. Carrier, inputs and fixed inventory

All numerical constants are the exact source defaults. They are theoretical
choices: mass 40*1.66053906660e-27 kg, hbar=1.054571817e-34 J s,
e=1.602176634e-19 C, epsilon0=8.8541878128e-12 F/m,
omega_z=2*pi*1 MHz, mu=omega_z+2*pi*20 kHz, Delta_k=2*pi/(397 nm),
nbar_m=0.05. The complex optical phase exp(i Delta_k*x_i) is retained.
There are seven axial modes, 16 equal segments per 100-microsecond loop and
five loops, with ideal zero-duration carrier operations: 500 microseconds.
No external calibration or private scientific dataset is loaded.

The real-amplitude closure matrix is 14-by-16. Its declared rank is 14 and
nullity 2. Choose the largest-absolute projected pair eigenvalue direction,
fix its sign and scale it separately for both target angles. A global real
force sign flip is not an angle-sign switch. The frozen theoretical peak cap
is 2*pi*5 MHz for nominal and stress amplitudes; no higher cap is substituted.

The 24 jobs are ordered sign (+,-), context (nominal, delta+2*pi*100 Hz,
amplitude*1.005, protected-D differential 0.002), arm (G,E,I). G uses active-only
X5; E uses the deliberately wrong global X5 while shelved logical 0 remains
auxiliary; I has zero force and no X5. Differential profiles are defined in
MODEL-INTERFACE and source, including auxiliary response -2*0.002.
Stress contexts retain the nominal waveform and nominal global correction.

Every job scans all 78,125 labels in little-endian base-5 order. The independent
direct-integration panel contains 69 specified branch entries per job:

- All 25 active label pairs with protected labels 0.
- 32 full indices `(12345+1871*k) mod 78125`, k=0,...,31.
- 12 variants: physical source ion 1, 6 or 7 at level 1,...,4, all other protected
  labels 0 and active labels (1,3).

The 300 Bell fixtures per job are physical source ion 1, 6 or 7, level 1,...,4,
and all 25 active pairs. Each uses the coherent source/reference pair between
source levels 0 and the selected level, with all other protected labels 0.
Its trace distance uses the full complex reduced-channel factor, including
the relative Weyl phase. This is a fixed witness panel, not a search over
favorable source states or a replacement for the uniform all-branch bound.
Every direct Bell trace distance, in every job, must be no larger than the
scanner's source_bound plus 1e-7. This is a frozen numerical consistency check,
not a rounding-error proof or an additional physical margin.

One warmup and five measured invocations use AVX-512/80, with actual unique
CPU/place maps checked. Each timed scan covers 24*78125=1,875,000 branches,
preceded by a separate full scalar/SIMD validation scan. The five observed
times are retained without optional stopping or fastest-run selection.
The strict topology is 80 allowed logical CPUs, 40 physical cores, two SMT
threads per core, two packages of 20 cores and two NUMA nodes. The runner
binds explicit OpenMP places and disables dynamic/nested oversubscription.
The eight named case diagnostics must match the warmup with absolute and
relative tolerances 1e-12; witness indices and case ordering must match exactly.

Kernel timing excludes preparation, scalar validation and team arrival,
and includes the final timed OpenMP barrier. Subprocess wall duration ends
after child exit is observed, includes any wait polling overhead, and excludes
subsequent parsing/repeat/hash checks. Invocation-with-custody timing includes
those checks. End-to-end timing includes model construction, direct validation
and all six validated scans, with compilation and transfer accounted separately.

## 4. Systematics and independence

- Assumed harmonic axial motion omits radial instability, counterrotating
  forces, nonlinear motion, finite carrier durations, leakage, heating,
  spontaneous decay, scattering and optical power calibration.
- A theoretical 5 MHz drive cap does not establish the validity of the
  rotating-wave or Lamb-Dicke approximations at that drive.
- Thermal initial motion is fixed and independent. Initial spin/bus
  correlations or an intermediate bus reset change the contract.
- Source population, one chosen coherence or the Bell panel alone cannot
  establish complete-source preservation. The uniform formula has the
  stated model assumptions and floating numerical limitations.
- The independent integration shares the frozen physical model and inputs
  but uses the full chronology, not the builder's coefficient contraction.
  Shared model mistakes remain possible. The exact audit is not a hardware
  or floating-integration oracle.
- All authors know the mathematical target; static cross-review is exposed,
  not blind. No scientific numerical outputs were inspected during design.
- CPU frequency, thermal state, NUMA placement, compiler and system load can
  change runtime. The five samples are a short engineering comparison, not
  a confidence interval for all systems. Keep kernel and process timings separate.
- Motional energy is a modeled endpoint displacement diagnostic. It does
  not count lasers, fields, electronics, baths, preparation, readout or reset;
  no total work or wall-plug energy is inferred.

## 5. Failure thresholds and disposition

| Gate | Frozen requirement |
|---|---|
| Exact audit | Every positive identity and declared negative-control exposure passes; exit 0, empty stderr, deterministic exact stdout |
| Equilibrium/modes | gradient infinity norm <=5e-13; positive axial eigenvalues; eigen residual <=1e-10; orthogonality error <=1e-12 |
| Closure construction | rank 14 at tolerance 1e-10, every normalized pivot >=1e-8, normalized null residual <=1e-11 |
| Interaction/cap | nonzero projected pair phase above source relative threshold 1e-10; absolute optical pair cosine >=1e-8; every applied peak <=2*pi*5 MHz |
| Independent direct validation | all 69 branches/job finite; absolute alpha discrepancy <=1e-9 and phase discrepancy <=1e-8 radians |
| Floating analytic fixtures | resonant force, closed circle, thermal damping and Weyl-sign discrepancies <=1e-12 |
| Scalar/SIMD | all scanned branch-summary discrepancies finite and <=1e-9 |
| Bell/source consistency | all 300 direct witnesses/job have trace distance <= source_bound+1e-7 |
| Nominal G, each sign | numerical gate_bound <=1e-6 and source_bound <=1e-8 |
| Nominal I, each sign | numerical gate_bound <=1e-10 and source_bound <=1e-10 |
| Nominal E, each sign | maximum fixed-panel source/Bell trace distance >1e-6 |
| All stress arms | retain all diagnostics; no additional mandatory gate/source target |
| Execution integrity | frozen hashes, valid input/output, actual 80 unique workers/places, finite values and successful required processes |

Use the source's fixed solver iteration caps and the coordinator's 55-second
watchdog per scanner child. A construction failure is INCOMPLETE, not evidence that no pulse
exists. A numerical target failure is a failure of this frozen candidate,
not a proof of mathematical or hardware impossibility. Stress diagnostics
may be large without silently becoming new acceptance thresholds.

Retain every nonzero exit, timeout, stderr and failed fixture, plus any partial
construction record. No retuning, threshold movement, outcome-dependent
repeat or replacement candidate is allowed at this pin. A failed engineering
campaign does not erase an independently completed exact audit. If the
formal exact gate never completes, follow POLICY's abandoned-pin record
without fabricated EXPECTED.txt/RUN.md and do not reuse the identifier.

## 6. Action layer, rollout and custody

Action layer L1 only. No native physical admission, Canon promotion, actual
ion operation or apparatus source-preservation claim follows from this work.

Before first scientific execution: complete every source and declaration,
commit the source manifest, push the immutable candidate and publicly read
back all pinned files byte for byte. Confirm source hashes on the selected
execution system. Record the full pin and readback. Static review, AST parsing
and compilation are permitted earlier; numerical construction, exact formal
execution, validation and performance measurement are not.

Use a clean pinned checkout and a new external result directory. Record source,
derived-model/input and binary hashes before use; check immutable files after
execution. Run the exact verifier separately and preserve its raw stdout/stderr.
The numerical coordinator runs the frozen default construction and campaign
once; unavailable construction or validation stops dependent steps.

Afterward EXPECTED.txt is the exact stdout byte copy. RUN.md records the pin,
PREREG and verifier hashes, exact command, neutral platform/architecture/Python,
exit code, stdout hash/bytes/lines and stderr hash/bytes. RESULT.md separates
the exact and engineering dispositions. Required unchanged x86_64/aarch64 CI
replays the exact verifier with the ordinary 600-second limit; it does not
pretend that floating outputs or timing are byte-identical science.

Keep raw machine records, private paths, `.jsonl`/`.log`, binaries and compiled
objects outside the public repository. Publish reviewed neutral numerical
summaries and a complete sanitized timing projection. Do not amend, rebase,
squash or force-push the pin. A reviewed PR changes only this probe directory
and must pass both architecture jobs and the aggregate `check` plus manual
security review. No workflow or policy exception is introduced.
