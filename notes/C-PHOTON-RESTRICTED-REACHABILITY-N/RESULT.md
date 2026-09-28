# Restricted reachability and ladder localization result

**PUBLIC / NON-CANONICAL.** Written proof: **candidate-T**. Finite integer
audit: **PASS, candidate-C on one architecture**. Retrospective localization:
**DESCRIPTIVE_ONLY, ZERO scientific evidential weight**.

Source pin: `33cd67b43bdcb1a6508f87ab54b26caaaa84a688`.
The single execution and public preregistration readback are recorded in RUN.md.
No source file changed after the pin. Both declared computations completed
with exit 0 and empty stderr. No falsifier of the written construction was
found in the analytical review or the admitted finite audit.

## Mathematical conclusion and boundary

PROOF.md supplies a constructive argument that both restricted single-link
move graphs C_0(n) and C_minus(n) are connected for every even L>=4,
k in {1,2} and n=1,...,L^2 in the parent's declared F_5 model. The construction
includes the full link-field fibers, gauge directions and torus cycles.
At n=0, C_0 is the whole link space and C_minus is empty.

Fixed-total bounded heights are connected by transfers on a slice's connected
dual graph. Modular wrapping then moves winding monotonically to a class-safe
extreme. At that extreme the complete cycle-space adjustment has at most a
one-unit winding excursion, so fibers can be joined without leaving the class.
All plaquette weights are strictly positive. The ideal restricted heatbath
therefore has an irreducible, aperiodic sweep kernel with its unique finite
conditional measure and eventual convergence.

This is a candidate theorem about the ideal mathematical kernel. It supplies
no mixing rate, finite-run equilibration certificate, floating-point
implementation certificate, reliable sampling interval, thermodynamic bound,
physical dynamics, P1 closure or phase conclusion. Subject to acceptance of
the proof, a disconnected restricted ideal move graph cannot explain the
parent discrepancy; the speed of traversal and implementation remain open.
The n=0 full-space connectivity likewise gives no timescale for leaving the
reported long-lived configurations.

## Exact finite audit

The deterministic integer audit passed all 125 local height/update triples,
all 3,900 height states on the four declared small connected graphs, and the
actual periodic square grids below. Each grid used k=1,2, both class extrema,
all four nonzero cycle coefficients and n=1,L^2.

| L | Fundamental cycles | Noncontractible cycles | Completed cycle paths | Intermediate link checks |
|---:|---:|---:|---:|---:|
| 4 | 17 | 8 | 544 | 2624 |
| 6 | 37 | 12 | 1184 | 7360 |
| 8 | 65 | 16 | 2080 | 15424 |
| 10 | 101 | 20 | 3232 | 27584 |

Totals: 7,040 completed cycle paths and 52,992 intermediate checks. This audits
the declared finite domains and construction; it does not exhaust the full
four-dimensional configuration space or establish the all-L statement by
computation. The exact transcript is ENGINEERING/audit_stdout.txt.

## Complete preserved-record comparison

The frozen transformation accepted all sixteen up-only class-minus records
from parent commit `fc16df1b06d971ca7ef4e2f35eab92d8b9637bdb` and its
analysis.json: 864 ensembles, 848 chain steps, eight chain pairs. Every
per-chain reconstruction is MATCH; the largest absolute difference from the
parent value is 7.11e-15, within the preregistered arithmetic tolerance.
No admitted estimator mean was zero. Exact rational operations apply to the
rounded decimal records; logarithms and displayed values are engineering
floating-point quantities, without inferential coverage.

The next tables include every admitted pair. All differences are chain 0
minus chain 1. Values below are rounded to six decimals; complete values,
all steps, both pairings, exact rational corrections and cumulative sums
remain in ENGINEERING/localization/.

| L | k | log l_minus, chain 0 | log l_minus, chain 1 | Difference | Recorded resets 0 / 1 |
|---:|---:|---:|---:|---:|---:|
| 4 | 1 | -4.249822 | -3.954322 | -0.295500 | 5 / 5 |
| 4 | 2 | -2.052712 | -2.029905 | -0.022806 | 2 / 3 |
| 6 | 1 | -8.270310 | -8.375283 | +0.104974 | 8 / 8 |
| 6 | 2 | -2.559934 | -0.473121 | -2.086814 | 5 / 5 |
| 8 | 1 | -16.478297 | -13.605028 | -2.873269 | 16 / 14 |
| 8 | 2 | -5.066001 | -4.020728 | -1.045272 | 7 / 7 |
| 10 | 1 | -18.041148 | -20.685650 | +2.644502 | 15 / 19 |
| 10 | 2 | -8.072864 | -8.092582 | +0.019717 | 5 / 2 |

The preregistered ensemble decomposition partitions each difference into
initial m=1, intermediate 2<=m<L^2, and endpoint m=L^2 contributions.
These are additive algebraic terms, not independent estimates.

| L | k | Initial | Intermediate | Endpoint | Total |
|---:|---:|---:|---:|---:|---:|
| 4 | 1 | -0.097101 | -0.196232 | -0.002167 | -0.295500 |
| 4 | 2 | -0.038271 | +0.012896 | +0.002569 | -0.022806 |
| 6 | 1 | -0.268745 | +0.374486 | -0.000767 | +0.104974 |
| 6 | 2 | -0.063639 | -2.025965 | +0.002790 | -2.086814 |
| 8 | 1 | -0.045543 | -2.826834 | -0.000891 | -2.873269 |
| 8 | 2 | +0.091442 | -1.133151 | -0.003563 | -1.045272 |
| 10 | 1 | -0.172083 | +2.815734 | +0.000851 | +2.644502 |
| 10 | 2 | +0.014086 | +0.001801 | +0.003830 | +0.019717 |

For the three parent groups with class-minus G3/G7 failures, the intermediate
terms are -2.025965 (L=6,k=2), -2.826834 (L=8,k=1), and +2.815734 (L=10,k=1).
Their endpoint terms are +0.002790, -0.000891, and +0.000851 respectively.
Thus the preserved chain-pair discrepancy resides chiefly in intermediate
ensemble terms in this fixed decomposition. This does not reproduce the
parent's full G3 own-versus-others comparison, which can include endpoint
chain 2; that chain is outside the admitted localization.

## Exhaustive reset partitions

Each cell gives the sum of differences followed by the number of terms in
parentheses. Column flags refer to chain 0 and chain 1. Every category is
retained, including empty ones. The first partition uses the reset flags of
the reached destination n+1 for each step n -> n+1.

| L | k | 00 | 01 | 10 | 11 |
|---:|---:|---:|---:|---:|---:|
| 4 | 1 | -0.027349 (10) | +0.000000 (0) | +0.000000 (0) | -0.268151 (5) |
| 4 | 2 | +0.171632 (11) | -0.167475 (2) | +0.013910 (1) | -0.040873 (1) |
| 6 | 1 | -0.328382 (24) | +0.826117 (3) | -0.167009 (3) | -0.225752 (5) |
| 6 | 2 | -1.543124 (27) | -0.154989 (3) | -0.340183 (3) | -0.048518 (2) |
| 8 | 1 | -1.008611 (43) | +0.059840 (4) | -1.221300 (6) | -0.703198 (10) |
| 8 | 2 | -1.067879 (51) | -0.092802 (5) | +0.146452 (5) | -0.031043 (2) |
| 10 | 1 | +1.297703 (72) | +1.270559 (12) | +0.154247 (8) | -0.078007 (7) |
| 10 | 2 | +0.244081 (94) | +0.000000 (0) | -0.231085 (3) | +0.006721 (2) |

The second partition uses each ensemble's own reached flags. It partitions
the same total with different algebraic terms.

| L | k | 00 | 01 | 10 | 11 |
|---:|---:|---:|---:|---:|---:|
| 4 | 1 | -0.151890 (11) | +0.000000 (0) | +0.000000 (0) | -0.143610 (5) |
| 4 | 2 | -0.126617 (12) | -0.022625 (2) | +0.099034 (1) | +0.027402 (1) |
| 6 | 1 | -0.714239 (25) | +0.082156 (3) | +0.672994 (3) | +0.064062 (5) |
| 6 | 2 | -1.718725 (28) | -0.242453 (3) | -0.122285 (3) | -0.003351 (2) |
| 8 | 1 | -2.847012 (44) | +0.254089 (4) | -0.388556 (6) | +0.108210 (10) |
| 8 | 2 | -0.826783 (52) | +0.044935 (5) | -0.186412 (5) | -0.077012 (2) |
| 10 | 1 | +2.537296 (73) | +0.034345 (12) | +0.047608 (8) | +0.025253 (7) |
| 10 | 2 | +0.082028 (95) | +0.000000 (0) | -0.000635 (3) | -0.061676 (2) |

The decompositions associate terms with recorded flags; they do not identify
a causal reset effect. A step combines estimators at two ensembles, and
memory may persist after the reset. The differing partition values make that
boundary concrete. Initial forcing is outside these twist-advance reset
flags, so an initial zero flag or null reset distance does not mean no
initialization forcing occurred.

## Disposition

The source schema preserves block statistics, not complete link
configurations. The recorded long-lived n=0 configurations cannot be
reconstructed or assigned a constructive escape trajectory from these data.
No new simulation, post-hoc gate, selected statistical test or retuning was
performed. The parent outcome remains INCONCLUSIVE_EQUILIBRATION, and its
recorded gates have not been reclassified.

The candidate proof addresses qualitative reachability. Quantitative mixing,
implementation certification and a prospectively qualified measurement remain
separate tasks; any new computation requires its own declared identifier and
public pin. This notes-only result promotes nothing into Canon v92.
