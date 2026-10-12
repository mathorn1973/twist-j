# Short DP5/N384 comparison at the same four local windows

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering evidence.
Apache-2.0, A. M. Thorn, 2026-10-12.
Reservation: https://github.com/mathorn1973/twist-j/issues/1468.
Authority base: `99094c18e668213a44532b7fb6053ca434293e9d`.

P-U-CA40-DP5-384-COMPARISON-1 tests whether DP5 at N384 reduces the cost of
the same local calculation without increasing any matched certificate
bound relative to inherited RK4 at N512. The pulses, exact model, seven
modes, L8/G10, 120 retained thermal columns and 80 AVX-512 workers stay
fixed. This is a short local panel with no automatic complete trajectory.

The exposed DP5/N256 predecessor completed its fixed panel with consistent
endpoints and reproducible bytes. Its observed A/C program end-to-end ratio
was 1.7359961608417056, but the strict bound condition failed for two of
2880 columns in each matched comparison. Both were window 0, labels (4,3),
thermal column 36, occupation (0,0,0,0,0,0,3), once per angle. Their C/A
ratios were 1.001164071473513 and 1.0012107880240055. Those known results
motivate this new identifier and are not a blinded prediction. The earlier
pin and negative first outcome remain unchanged.

| Arm | N certificate cells per original segment | Endpoint method and dense curve | Cells / integration substeps / RHS / Gauss nodes per window |
|---|---:|---|---|
| A | 512 | inherited RK4; endpoint Hermite with directional finite-difference accelerations | 4 / 4 / 36 / 64 |
| C | 384 | two DP5 halfsteps per cell; three-point Hermite quintic | 3 / 6 / 39 / 48 |

N counts certificate cells, not integrator substeps. C has 768 DP5
substeps per original segment. A/C changes both the endpoint method/dense
curve and certificate-cell density; any measured speed difference cannot
be assigned solely to formal integration order. The exact same DP5 weights,
step implementation and quintic construction are inherited from the sealed
predecessor. Their attribution is Hairer and Wanner's
[DOPRI5 coefficient table](https://www.unige.ch/~hairer/prog/nonstiff/dopri5.f),
subroutine CDOPRI. The original C++ implementation does not run the Fortran
solver or its adaptive controller. Formal order supplies no numerical
certificate by itself.

Each of four windows per case lasts exactly 48.828125 ns. Every window
independently starts from a unit basis vector in the moving full-linear
frame, retaining the complete analytic displacement/phase history and
absolute clock. Its physical input is U_L(t0)|n>, not the nonlinear state
reached during an earlier complete evolution. These reset-window bounds
cannot be added or extrapolated into a complete-pulse certificate.

The frozen order is A,C,C,A: two fresh observations per arm. Each child has
at most 300 seconds and each of two matched comparisons at most 90 seconds,
inside a 1200-second campaign budget including validation and comparison.
There is no pilot, retry, adaptive window, discarded warmup, pulse retuning
or longer follow-up. Failed engineering screens continue the fixed panel;
integrity failures stop after preserving evidence.

The separate decisions are:

- Both repetitions of each arm must reproduce endpoint, component, basis,
  immutable metadata and layout bytes exactly.
- Both comparisons must classify all 2880 directed endpoint differences
  COMPATIBLE with the sums of the respective local certificate bounds.
- C must satisfy e_C <= e_A in every matched column of both comparisons,
  decided by exact Fractions of the stored binary64 values.
- C's two-observation program end-to-end median must be strictly smaller
  than A's; exact sums of the two times decide this without a speed factor.

The two earlier failing states are explicitly reported under the same
conditions, with no exemption, extra tolerance or replacement of the full
2880-column gate. Joint success additionally requires intact custody,
repeatability and compatibility. UNRESOLVED prevents PASS. Two-observation
medians are descriptive averages, not confidence intervals or general
performance guarantees.

After the complete public pin and byte readback, the exact supporting gate is:

```sh
python3 probes/P-U-CA40-DP5-384-COMPARISON-1/verify.py
```

The separate numerical driver uses executables built from that public pin:

```sh
python3 integrator_run.py --baseline /absolute/path/baseline \
  --candidate /absolute/path/candidate --comparator /absolute/path/compare \
  --output /absolute/path/new-directory
```

All fifteen scientific sources and their manifest are pinned before any
scientific execution or candidate import. Raw states and machine records
remain private; public results retain neutral summaries and hashes. This
study closes no complete-trajectory error, final coherence, all-input
channel, physical realization, energy/work account or complete-source
preservation claim. The exact-darkness and unknown-source no-imprinting
boundaries remain unchanged.
