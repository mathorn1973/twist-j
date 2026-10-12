# Short N256 versus N512 comparison at four local windows

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering evidence.
Apache-2.0, A. M. Thorn, 2026-10-11.
Reservation: https://github.com/mathorn1973/twist-j/issues/1464.
Authority base: `37529581a5e0e111668f5f6501d633dbcbb3d2bc`.

P-U-CA40-GRID-COMPARISON-1 asks how halving the time-grid subdivisions
changes runtime, local endpoints and validated local error bounds for the
same pulses and both angles. It uses the sealed low-copy kernel from
P-U-CA40-CLOSURE-PERF-1, with L8/G10, all seven modes, all 120 retained
thermal basis columns and 80 bound AVX-512 workers. It runs no complete
trajectory and permits no automatic long successor calculation.

The predecessor preserved every tested endpoint and partial-account bit,
but its observed propagation-window speedup was 1.4377742506583304,
below its frozen twofold target. This exposed result motivates a distinct
time-grid comparison; no previous outcome or source is amended.

Four fixed windows sample early, interior and late occupied segments.
Each window lasts exactly 48.828125 ns: two N256 cells or four N512 cells.
The absolute clock and complete analytic full-linear displacement history
are retained. Each window independently starts from a basis vector in the
moving full-linear frame. In the physical frame this is the corresponding
displaced state U_L(t0)|n>, not the actual nonlinear state reached midway
through the original pulse sequence. The four windows are never chained.

This design samples the local generator at different analytic displacements
and phases. It does not test the potentially broader or correlated nonlinear
state that a complete earlier evolution would produce. Its local bounds
cannot be summed or extrapolated into a full-trajectory certificate.

PREREG.md fixes the windows, six-run order 512,256,256,512,512,256 and
300-second child / 1800-second total campaign limits. A separate directed
endpoint comparison has at most 90 seconds after each matched pair, inside
the same total budget. All first outcomes, including incomplete and negative
ones, are preserved. No pilot, retry, adaptation or pulse retuning is allowed.

Three distinct questions remain separate:

- Repeated runs at the same N must reproduce all endpoint and local-account
  binary64 words exactly, including signed zero.
- For each matched window and thermal column, a directed enclosure of the
  endpoint difference is checked against the sum of the two validated local
  error bounds. The outcomes are COMPATIBLE, INCONSISTENT or UNRESOLVED.
- The coarse reported bound must be at most twice the fine reported bound
  to pass a separate engineering screen. This tests growth of upper bounds,
  not growth of the unknown actual numerical error.

Same-N bit mismatch, invalid runtime/custody data or a directed inconsistency
stops the campaign after preserving its record. An unresolved comparison
may finish the remaining fixed runs but cannot yield a compatibility PASS.
A failed bound-growth screen also completes the fixed plan if no fatal
condition occurs; it is a recorded negative engineering outcome. Completion
does not mean that every screen passed.

The performance report uses all three timings at each N. There is no new
speed threshold selected after inspection. The propagation window includes
thread startup, workspace allocation, barriers, numerical work and progress
logging, while model preparation, fixtures and serialization are reported
separately. All six timings and their medians remain visible.

The independent supporting gate is:

```sh
python3 probes/P-U-CA40-GRID-COMPARISON-1/verify.py
```

It establishes only its stated exact fixtures. The separate frozen driver
accepts prebuilt absolute paths and a new output directory:

```sh
python3 grid_run.py --binary /absolute/path/benchmark \
  --comparator /absolute/path/compare --output /absolute/path/new-directory
```

All scientific execution and candidate imports follow a complete public
source pin and byte readback. Static inspection and compilation establish
no numerical result. The manifest and build receipts identify the actual
sources, common toolchain, flags, binaries and serialized model input.

No result here certifies a full error radius, a final nonlinear coherence,
an all-input channel, physical ion hardware or complete-source preservation.
Exact-darkness and no-imprinting premises remain unchanged. Raw binary
states and machine-specific records stay in the private evidence archive;
public outcomes contain neutral summaries and receipt hashes.
