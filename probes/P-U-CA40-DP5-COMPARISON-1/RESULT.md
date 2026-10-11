# Result: faster DP5 panel; strict local-bound condition narrowly missed

Status: C

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering evidence.
Original record Apache-2.0, A. M. Thorn, 2026-10-11.

The frozen A,B,C,C,B,A panel completed in 633.9374961871654 seconds.
A is inherited RK4/N512, B is inherited RK4/N256, and C uses two DP5
halfsteps per N256 certificate cell with a three-point Hermite quintic.
All three within-arm repetitions were byte-identical. All six matched
comparisons classified all 2880 columns COMPATIBLE, with no INCONSISTENT
or UNRESOLVED case. Source/input/executable custody, runtime fixtures and
eighty-worker placement passed. The exact supporting gate also passed;
RUN.md and EXPECTED.txt retain its first actual output.

The two-observation program end-to-end median decreased from
116.45330219529569 seconds for A to
67.08154362440109 seconds for C, an observed factor of
1.7359961608417056. The propagation-window median decreased from
69.5893381414935 to 37.616538549773395 seconds,
an observed factor of 1.8499665525953268.
The speed screen passed, but the strict bound screen failed:
**LOCAL_BOUND_NONINCREASE_CONDITION_MISSED**. The joint engineering screen
therefore failed. No acceptance threshold was changed after the source pin.

The condition epsilon_C <= epsilon_A failed for exactly two of 2880 columns
in each A/C comparison. Both failures occur in window zero, labels (4,3),
thermal column 36, occupation (0,0,0,0,0,0,3), once per angle. The positive
angle bound increases from 4.777055050900987e-8 to 4.782615884413142e-8;
the negative angle increases from 3.879535150480492e-8 to
3.884232445179402e-8. These are increases of approximately 0.1164% and
0.1211%. They remain failed preregistered cases despite their small size.

| Angle | Maximum local bound A | Maximum local bound C | Paired C/A bound ratio range |
|---|---:|---:|---:|
| +4*pi/5 | 2.599540871089461e-07 | 2.2155191582107428e-07 | 0.7465265043592806 to 1.001164071473513 |
| -4*pi/5 | 1.975169639385187e-07 | 1.6808552213677247e-07 | 0.7470746296290185 to 1.0012107880240055 |

Maxima are taken independently over each angle's 1440 local columns;
ratios compare matching columns. These are certificate upper bounds on
local vector-norm error, not measured true errors or gate infidelities.
At the same N256 certificate grid, C's bound is smaller than B's for every
column. C uses more integration work per cell than B; its kernel median is
37.616538549773395 seconds versus 35.304124534130096.
The second B preparation took 56.07066703028977 seconds versus
23.60707475990057 on its first observation; both are retained. This variation
affects B's end-to-end median. Two observations per arm provide descriptive
averages, not confidence intervals or a universal speed guarantee.

COMPARISON.md records all six individual timings, the 24 window/case
groups, component diagnostics, matched pairs and evidence hashes. Timings
cover a joint panel containing both angles, not separately timed angle
campaigns. A/C changes both the integrator/dense curve and certificate-cell
density; its speedup cannot be attributed solely to integration order.
A and C have the same four actual integration substeps per local window.

The immutable source pin is
`09dde450cfcb9386262afbd0b790250bd3c1bb4a`.
All fifteen sources plus their manifest were publicly read back before
execution. Original pulses/input bytes, seven modes, L8/G10 and all 120
retained thermal columns stayed fixed. Each 48.828125 ns window independently
starts from a moving-frame basis state with full analytic linear history;
it is not the nonlinear state reached partway through a full pulse.

This is a useful local speed/bound tradeoff, with a narrowly negative strict
screen. It does not adopt C for a complete calculation, close either angle's
full numerical error account, compute final coherences or prove complete-source
preservation. No complete trajectory or longer successor run was started.
The exact-darkness and unknown-source no-imprinting boundaries remain unchanged.

Every first outcome is retained without retry, repair or discarded warmup.
This identifier is sealed. Any refinement requires a new preregistration,
source pin and short comparison; this result authorizes no further run.
