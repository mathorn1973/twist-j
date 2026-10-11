# Short DP5 comparison at four fixed local windows

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering evidence.
Apache-2.0, A. M. Thorn, 2026-10-11.
Reservation: https://github.com/mathorn1973/twist-j/issues/1466.
Authority base: `9bbb5e64ef852d82133cf94f5c31166b73d328b3`.

P-U-CA40-DP5-COMPARISON-1 tests whether a different integrator and dense
curve can reduce the measured cost of the same local calculation without
increasing its reported error bound. The pulses, exact model, seven modes,
L8/G10 spaces, all 120 retained thermal columns and 80 AVX-512 workers stay
fixed. There is no complete trajectory or automatic longer successor run.

The exposed GRID predecessor found faster RK4 propagation at N256, but
every tested local bound exceeded twice its matched N512 bound. Its observed
kernel speedup was 1.9681268374684553. Those results motivate this new
identifier; the predecessor remains sealed and unchanged.

The fixed panel has three arms:

| Arm | N certificate cells per original segment | Endpoint method | Dense quintic | Cells / integration substeps / RHS calls per window |
|---|---:|---|---|---|
| A | 512 | inherited RK4 | endpoint values, derivatives and directional finite-difference accelerations | 4 / 4 / 36 |
| B | 256 | inherited RK4 | same construction as A | 2 / 2 / 18 |
| C | 256 | two consecutive DP5 half-steps per cell | values and derivatives at start, midpoint and end | 2 / 4 / 26 |

N counts certificate cells. Arm C has 512 DP5 integration substeps per
original segment. A/B measures the grid change with the old method; B/C
compares methods at the same certificate grid; A/C is the practical
cost/bound comparison. Its two effects must not be attributed solely to
formal integration order.

The DP5 weights follow the Dormand-Prince coefficient table in Hairer and
Wanner's [DOPRI5 source](https://www.unige.ch/~hairer/prog/nonstiff/dopri5.f),
subroutine CDOPRI. This study supplies original C++ code and a separately
derived three-point quintic Hermite reconstruction. It does not copy or run
the Fortran solver, its adaptive controller or its supplied dense output.
Formal method order alone establishes no useful error bound for this panel.

Four windows per case cover fixed early, interior and late occupied
segments. Each lasts exactly 48.828125 ns. Every window independently starts
from a unit thermal basis vector in the moving full-linear frame, while
retaining the complete analytic displacement/phase history and absolute
clock. Its physical initial state is U_L(t0)|n>, rather than the nonlinear
state reached by an earlier complete evolution. These local bounds cannot
be summed or extrapolated into a complete-pulse certificate.

PREREG.md freezes six fresh children in order A,B,C,C,B,A: two observations
per arm. Each child has at most 300 seconds; each of six directed pair
comparisons has at most 90 seconds, inside the same 1800-second campaign
budget. No pilot, retry, retuning, discarded warmup or adaptive window is
permitted. Failed engineering screens continue the fixed plan; integrity
failures stop after preserving their records.

The decisions are separate:

- Both observations of each arm must reproduce all endpoint and local-account
  binary64 words exactly. B and C are different arms even though both use N256.
- Each of six matched comparisons checks the directed endpoint difference
  against the sum of the two local certificate bounds, yielding COMPATIBLE,
  INCONSISTENT or UNRESOLVED.
- C must satisfy e_C <= e_A for every one of the 2880 matched columns in each
  of its two A/C comparisons. This compares upper bounds, not actual errors.
- The two-observation program end-to-end median of C must be strictly less
  than A's. There is no imposed speed factor or twofold error allowance.

A joint engineering success requires both final conditions and intact
repeatability/consistency evidence. An unresolved consistency test prevents
a PASS. Every negative outcome remains visible. With two observations, the
reported median is their arithmetic mean; this supplies no confidence
interval, statistical significance or full-campaign forecast.

The exact supporting gate is:

```sh
python3 probes/P-U-CA40-DP5-COMPARISON-1/verify.py
```

It audits only its stated exact fixtures. The separate numerical driver
uses prebuilt absolute paths and a new output directory:

```sh
python3 integrator_run.py --baseline /absolute/path/baseline \
  --candidate /absolute/path/candidate --comparator /absolute/path/compare \
  --output /absolute/path/new-directory
```

All fifteen sources plus their manifest must be publicly pinned and read
back before scientific execution or candidate imports. Static review and
compilation produce no numerical result. Raw states and machine-specific
records remain private; public outcomes use neutral summaries and hashes.

This study closes no full-trajectory radius, final coherence, all-input
channel, physical contact admission, energy/work account or complete-source
preservation claim. Exact-darkness and unknown-source no-imprinting
boundaries remain unchanged.
