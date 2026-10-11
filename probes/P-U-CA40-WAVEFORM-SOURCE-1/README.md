# One waveform, both pair angles, and the complete protected source

PUBLIC NON-CANONICAL. Conditional L1 theory and numerical engineering witness.
Original text Apache-2.0. Date: 2026-10-10.
Probe: `P-U-CA40-WAVEFORM-SOURCE-1`.
Reservation: [issue #1452](https://github.com/mathorn1973/twist-j/issues/1452).
Branch: `probe/P-U-CA40-WAVEFORM-SOURCE-1`.
Authority base: `7e2b199086a14b2e2183d684e388a42679652a1d`.

This candidate derives its displacement and phase coefficients from the same
declared pulse history. It extends the earlier synthetic-coefficient scan with
a seven-mode harmonic construction, independent direct integration and a
uniform comparison for the complete protected quantum state and its reference.
It contains no run result yet. The proposed pulse may fail the frozen drive
cap, solver conditions or numerical targets; those outcomes must be retained.

The work is theoretical and numerical only. A physical ion experiment is not
available or planned in this probe. No apparatus calibration or hardware
feasibility PASS is claimed.

## Carrier and the two source questions

Waveform physical-ion order is `(s,x,u,y,w,q,r)`. Ions 4,5 form the active
pair; protected ions 1,2,3,6,7 include source ions 1,6,7, namely `(s,q,r)`.
The pair primitive has target `I_P tensor G(theta)`, with

```text
G(theta)|a,b> = exp(i theta*[a!=b]) |a,b>,
theta = +4*pi/5 or -4*pi/5.
```

Preservation of P is a quantum-channel question for arbitrary electronic
inputs, including P/A correlations and entanglement with an untouched
reference. The initial motional bus is independently prepared in the frozen
product thermal state; unspecified initial spin/bus correlations are outside
this contract. Checking source populations alone would be insufficient.

The full informative contact C is a different operation. Its exact negative
control uses abstract coordinate order `(x,u,y,w,q,r,s)`, related to the
physical-ion order by the fixed permutation shown above. It verifies

```text
C:(x,u,y,w,q,r,s) -> (x,u-2*(y-x)*s,y,w+2*(y-x)*s,q,r,s) over F5.
```

At a fixed basis receiver with y!=x, C preserves every classical s label but
dephases a coherent source. A Bell source/reference input loses its joint
off-diagonal entries too. Its joint inverse restores the input while erasing
the receiver record; keeping an informative archive prevents universal source
restoration. A pair gate that leaves the source untouched does not evade this
already established boundary for the complete informative contact.

## Shared pulse model

`DERIVATION.md` fixes the Hamiltonian, chronological Weyl sign, source bound
and assumptions. `MODEL-INTERFACE.md` fixes the builder schema and numerical
construction. Physical quantities here are assumptions, not measured inputs.

The model uses seven identical ions of mass 40 times the declared atomic mass
unit in a harmonic axial trap with omega_z=2*pi*1 MHz. Coulomb equilibrium and
its Hessian supply seven axial modes. The beatnote is omega_z+2*pi*20 kHz;
Delta_k=2*pi/(397 nm), with its complex spatial phases retained. Radial modes
and finite carrier pulses are omitted. The initial occupation is nbar=0.05 in
each mode. Heating, decay, scattering and counterrotating terms are absent.

Five 100-microsecond LS loops each contain 16 equal real-amplitude segments.
Ideal instantaneous shelving, adjoint return and X5 pulses give a total model
block duration of 500 microseconds. A 14-by-16 real closure system supplies a
two-dimensional nullspace; its projected interaction matrix chooses the
largest-absolute-eigenvalue direction. This minimizes squared envelope norm
at fixed phase in that subspace, not peak power or physical gate duration.

Both targets use that direction with different scales. The available phase
orientation determines which target uses magnitude 4*pi/5 and which 6*pi/5;
the force-scale ratio is sqrt(3/2). Negating the waveform does not reverse its
quadratic geometric phase. The theoretical drive cap is 2*pi*5 MHz, including
the amplitude-stress context. A cap failure is INCOMPLETE, with no fallback.

For each branch and mode, the same force history supplies alpha and Phi:

```text
U_z = exp(i Phi_z) D(alpha_z),
alpha <- alpha + beta,
Phi <- Phi + chi + Im(beta * conjugate(old_alpha)).
```

The phase update uses the old displacement. All 80 segments share one absolute
clock. The builder may factor a repeated loop algebraically, but retains its
inter-loop Weyl terms; it never resets motion between loops. A single nominal
G all-zero branch fixes the common-phase subtraction for G and E, across every
context. I subtracts zero. No result-dependent phase correction is fitted.

The generated tables contain 203 complex displacement coefficients and 364
nonconstant phase coefficients, plus the separate common phase. Their
constant/unary/pair representation is a consequence of this additive force
model; the tables are not independent synthetic inputs.

## Frozen panel and acceptance

There are 24 jobs: two target signs, four contexts and three arms.

| Dimension | Frozen choices |
|---|---|
| Context | nominal; delta+2*pi*100 Hz; force amplitude times 1.005; protected D-response differential 0.002 |
| Arm G | Correct active-only X5, protected levels hidden during LS |
| Arm E | Deliberately incorrect global X5; protected nonzero labels can visit physical S |
| Arm I | Zero drive and no X5, same 500-microsecond model interval |

Each job scans all 78,125 electronic labels. Uniform gate and protected-source
comparisons use the actual corrected phase and final displacement, including
the Weyl phase relative to the protected-zero anchor at the same active labels.
The exact formulas bound half-diamond distance under their stated fixed-bus
assumptions. Their floating-point evaluations here are numerical estimates;
no interval enclosure or rigorous rounding-error margin is supplied.

For both nominal G jobs require `gate_bound <= 1e-6` and
`source_bound <= 1e-8`. For each nominal I sign require both bounds `<= 1e-10`.
For each nominal E sign require the maximum source/Bell-reference trace
distance in its fixed 300-fixture panel to exceed `1e-6`. This negative
control must expose the wrong protected echo. All stress-arm values are diagnostic
results, not additional mandatory gate/source PASS thresholds.

An independent path integrates all 80 absolute-time segments on 69 fixed
branches per job: 25 protected-zero active anchors; 32 full indices
`(12345+1871*k) mod 78125`, k=0,...,31; and 12 source variants at active
labels (1,3), varying physical ion 1,6 or7 to label1,...,4. Index digits are
little-endian base5. Absolute comparison tolerances are 1e-9 for alpha and
1e-8 radians for phase. The 300 Bell fixtures are three source ions times
four nonzero labels times 25 active pairs, each compared with its source-zero
anchor; they test source/reference coherence, not only source population.
For every job, every direct Bell trace distance must also lie below the
scanner's uniform source estimate plus the frozen numerical slack 1e-7.

The full scan compares its AVX-512 and scalar paths over all branches at
absolute tolerance 1e-9. Independent fixtures and the exact verifier have
different scopes: neither makes a floating bound an exact physical certificate.
The declared numerical criteria are engineering targets for this model.

## Exact audit and numerical execution

`verify.py` is a separate standard-library exact verifier. It credits reuse of
the earlier ideal-word audit, adds rational Gaussian/Weyl identities, and
derives coefficients of a resonant rational segment fixture using exact
indicator polynomials. Its two orientations give 365 phase-anchor and 203
complex-displacement checks each. Its source audit covers all 78,125 C columns
and all 25 source matrix units at each of 15,625 basis receiver preparations.
The expected negative source result is part of PASS, not a hidden promise of
full-source preservation. It does not execute or certify the floating solver.

`model_builder.py` constructs the frozen default model once.
`numerical_run.py` coordinates the independent 80-segment fixtures, Bell tests,
input serialization, source custody and six scanner invocations: one warmup
and five measured invocations on AVX-512/80. Each invocation has a full
scalar/SIMD validation scan and a separate timed scan of 24*78,125=1,875,000
branches. Report all five measured observations; do not select the fastest run.
Topology, actual CPU placement and finite JSON outputs must be validated.
The target has 80 allowed logical CPUs, 40 physical cores, two SMT threads per
core, two packages of 20 cores and two NUMA nodes. Repeated diagnostics must
agree with the warmup at both absolute and relative tolerance 1e-12; witness
indices must agree exactly. Missing support or inconsistent placement stops
the campaign, without silently changing the declared execution configuration.

Kernel timing excludes input preparation, the scalar/SIMD validation pass
and team arrival, but includes the final timed OpenMP barrier. Subprocess wall
timing ends after observing child exit and includes the wait's possible
polling overhead; parsing and custody checks have a separate invocation
duration. End-to-end timing additionally includes model construction, direct
validation and all six validated scanner invocations. Compilation and transfer
are reported separately. Each scanner child has a 55-second watchdog.

Frozen scanner build recipe:

```text
g++ -O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math \
  -fno-tree-vectorize waveform_scan.cpp -o <external-output>/waveform_scan
```

Direct component interfaces, for use only after the complete public pin:

```text
python3 model_builder.py --output <new-external-model.json>
waveform_scan --input <frozen-derived-coefficients.txt>
python3 numerical_run.py --binary <absolute-external-waveform_scan> --output <new-external-directory>
python3 probes/P-U-CA40-WAVEFORM-SOURCE-1/verify.py
```

The scientific campaign is run through the pinned numerical coordinator,
which supplies generated inputs to the scanner; these component interfaces
do not authorize a second builder run or a retuned result. A new output
directory is required. Exact and numerical execution receipts remain distinct.

## Custody, failures and boundary

Before any scientific execution, commit and push all sources, this README,
PREREG, MODEL-INTERFACE, DERIVATION and the source-hash manifest. Read the
immutable commit back from the public repository and verify every byte/hash.
Compile outside the public checkout; retain actual flags, compiler and binary
hash. Source inspection, AST parsing and compilation may precede the pin;
solver construction, validation and timed scanning may not.

Preserve every INCOMPLETE, validation failure, timeout, stderr record and
measured sample. No threshold changes, silent repeats, alternative pulse shape
or fallback solver are permitted after inspection. The exact formal probe
uses EXPECTED.txt/RUN.md/RESULT.md and unchanged two-architecture CI replay;
the floating campaign has a separately labelled engineering closure.

Publish reviewed neutral summaries, not raw machine logs, private paths or
compiled binaries. The bus energy diagnostic is only displacement energy in
the modeled harmonic modes; it is not total control work, optical power or a
wall-plug energy account. An exact algebra PASS, a numerical nominal PASS and
a hardware realization are distinct claims. This probe can earn only the
first two, within their declared scopes.
