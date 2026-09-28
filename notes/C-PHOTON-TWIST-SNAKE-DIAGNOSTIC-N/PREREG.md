# Telescoping twist-ratio diagnostic with local estimators

**PUBLIC / NON-CANONICAL. Prospective engineering diagnostic.**

- Item: C-PHOTON-TWIST-SNAKE-DIAGNOSTIC-N, issue #1259.
- Author: A. M. Thorn.
- Basis: Public Canon v92; main `213fad32b3cc3070685d226403d5aec93a37c9f5`.
- Scope: L6 finite measure; numerical output has ZERO scientific evidential weight.
- Written identities (PROOF.md): candidate-T, reviewed before execution (REVIEW.md).
- No thermodynamic lower bound, P1, phase or physical-photon decision is authorized.

## Prior knowledge and execution boundary

The predecessor `notes/C-PHOTON-TWIST-ENDPOINT-DIAGNOSTIC-N` (#1249, merged
in #1250) is a completed and consumed attempt, not an abandoned pin. Its
preserved records were read before this design: every one of its 24
chains recorded zero complete replica round trips, at least one adjacent
temperature edge with zero accepted production exchanges, and at L=8 zero
endpoint changes (`ENGINEERING/analysis.json`, SHA-256
`d5b48289d55d028b29c7635355fa487def2ced7ea9f0b4436c58686e1ee23b38`; all
figures NONINFERENTIAL under that preregistration). The reading adopted
here is that its temperature ladder scaled the whole extensive weight, so
adjacent replicas differed by an extensive amount, and that the single
global endpoint flip changes the weight of L^2 seam plaquettes at once.
By Jensen's inequality -log R_k <= L^2 E_{pi_0} log(W(F_q)/W(F_q+k)) for
one seam plaquette q, hence pointwise -log R_1 <= L^2 log(W(1)/W(2)) =
1.925 L^2 and -log R_2 <= L^2 log(W(0)/W(2)) = 2.349 L^2; the zero-curl
value L^2 log(W(0)/W(1)) ~ 0.424 L^2 is the k=1 integrand at one point,
not a bound. No value of R_k is predicted.

The same records show a second fact used in this design. In the fully
twisted k=2 chains the 128-sweep block means of Y alternate between two
plateaus near +1.5 and -2.25 (`ENGINEERING/L4_k2_c2.tsv`, `L4_k2_c3.tsv`,
`L6_k2_c3.tsv`), with no change at all in either L=8 chain over 4096
sweeps. This design hypothesises that the plateaus correspond to the
integer sector w of the slice flux sums defined in PROOF.md section 6;
PROOF.md makes no statement about the plateaus or about the weight of any
sector. This design records that sector, starts
one chain in the alternative sector, and labels a run in which the chains
do not agree on the sector occupancy SECTOR_FROZEN. It does not claim to
sample the sector distribution at any L.

No #1249 output, seed, run, threshold value, budget or identifier is
resumed or extended; the source files here are retargeted under a new
identifier and a new pin, with seed base 202609280000 distinct from
202609270000. The written proof in #1217 concerns the same first-order
identity C_k = i rho_k D_k in written form; it is not executed, promoted
or depended on here.

This design has no mobility observable. The twist count n is driven by a
fixed schedule, so the predecessor's round-trip, endpoint-change and
exchange-acceptance gates have no counterpart and no comparison of
transport between the two items is made or implied. The gates below
detect forward/reverse, direction, start, time and sector inconsistencies
and check exact identities; passing all of them means that no
preregistered inconsistency was detected, not that any ensemble was
equilibrated or sampled at stationarity.

## Departure from the #1249 pre-pin rule

#1249 stated: "No sampler, sampler audit, pilot analysis or scientific
fixture is executed before the complete sources, proof, this file and the
static review are committed, pushed and read back publicly." This item
relaxes that rule in one respect and tightens it in another. Before the
public pin the compiled binary was executed only as `sample --audit`, a
deterministic implementation test whose output is a fixed-form transcript
containing no estimate of any target quantity; `test_analyze.py`, which
fabricates block records from declared pseudo-random parameters in Python
and never calls the sampler, and `run_snake.py` and `run_analysis.py`
with a stub executable and fabricated records, were executed. No
invocation of the production entry point `sample L k chain base`, with
any argument, seed, size or sweep count, took place before the pin,
whatever it would have printed. The sweep counts of the schedule are
prior design choices fixed without any run of this kernel. For
throughput only, the frozen #1249 sampler was compiled and its L=4 and
L=6, k=1, chain 0 jobs were re-executed on the executing system with
output discarded; nothing from those runs is preserved, compared or used
except the wall-clock figure below.

The pre-pin audit is therefore an observed implementation test, not a
prediction. REVIEW.md discloses every pre-pin audit failure and the code
change it caused. The audit's fixture pattern, tolerances, exercise seed
and printed counts may not be changed after the pin.

## Fixed carrier and observable

For L in {4,6,8,10}, use the periodic positively oriented cubical
four-torus, links alpha in F5 and W(f)=2+2cos(2 pi f/5). The seam Sigma
contains the L^2 positive 01 plaquettes at x0=x1=0, ordered by j=x2+L x3;
seam plaquette j lies in slice j. Independently for k=1,2, PROOF.md
defines the partially twisted ensembles nu_n, 0<=n<=L^2, with the source
k on the first n seam plaquettes; nu_0 is the untwisted measure and
nu_{L^2} the fully twisted endpoint pi_k of #1249. The quantities are

    R_k = Z_k/Z_0 = prod_{n<L^2} r_n,   r_n = Q_{n+1}/Q_n,  Q_n = Z(k S_n),
    Y_k = L^-2 sum_(p parallel 01) tan(pi F_p/5),  F = curl + source,
    -i C_k = R_k E_{pi_k} Y_k,   E_{pi_0} Y_0 = 0,   E_{pi_0} Y_0^2 <= 1.

Per step n the naive forward estimator is W(F_q+k)/W(F_q) at the step
plaquette q=q_n under nu_n and the naive reverse estimator is
W(F_q-k)/W(F_q) under nu_{n+1}; the conditional (Rao-Blackwellised)
estimators are the heat-bath normaliser ratios of PROOF.md (8)-(11),
averaged over the four boundary links of q. All four estimators are
bounded by the extreme values of W(f+k)/W(f): [0.1459, 6.854] for k=1
and [0.09549, 10.47] for k=2. The conditional estimators are primary by
prior decision; the naive ones are recorded, together with the exact
integer histogram of the flux of q, for the consistency gate and a
secondary Bennett estimate.

The sector bookkeeping of PROOF.md section 6 is recorded every production
sweep: the numbers of twisted slices with w=0, w=-1, w=+1 and other, the
number of untwisted slices with w!=0, whether all twisted slices share
one of the three values while every untwisted slice has w=0 (a pure
layout, labelled by that value), and the number of changes of the layout
label (pure w=0, pure w=-1, pure w=+1 or mixed) between consecutive
sweeps of a segment.

## Fixed numerical kernel and budget

The standard-library C++17 sampler uses the single-link five-state heat
bath at the target weight (one table) and no other move: no tempering,
replica exchange, global flip, adaptive weight or fractional source. The
twist count changes only between segments, by one plaquette, through the
exact cache update of PROOF.md (2). Every chain follows the same schedule:

| Stage | Sweeps | Recorded |
|---|---|---|
| warmup at the start twist | 512 | no |
| DWELL at the start endpoint | 16384 | 32 blocks |
| each of the L^2-1 intermediate twists, in order | 32 discarded + 2048 | 4 blocks |
| DWELL at the far endpoint | 32 discarded + 16384 | 32 blocks |
| each intermediate twist again, in reverse order | 32 discarded + 2048 | 4 blocks |

Main groups (base 0) have five chains per (L,k): chain 0 all-zero links
at n=0; chain 1 independently uniform links at n=0; chain 2 all-zero
links at n=L^2; chain 3 uniform links at n=L^2; chain 4 at n=L^2 with
all links zero except alpha_0=2 on the 0-link at x0=x1=0 of every slice,
which is the pure w=-1 layout (seam flux k+2 and -2 on the neighbouring
01 plaquette in every slice). Exact control groups (base 2) exist for
L in {4,6} with chains 0 to 3 only: the whole seam carries the source 2k
and the chain adds k to the seam plaquettes one by one, so its endpoints
are Z(2k) and Z(3k)=Z(2k). The seed is
202609280000+1000 L+100 k+10 base+chain. There are 56 declared jobs (40 main, 16 control).
Blocks are 512 consecutive production sweeps; every production sweep is
measured once, after the full heat-bath sweep. Each block row records
the sums and sums of squares of the four estimators, of Y and of the
action density, the two flux histograms and the sector counts. No
adaptive length, seed, threshold or stopping rule is allowed after
observation.

The cached effective flux is compared exactly with the direct curl plus
source, and the cached score with its recomputation within 1e-8 times the
plaquette count, after every block and every twist change; the slice
flux sums are checked for congruence with their sources every sweep;
failure exits nonzero. The controller `run_snake.py` runs the audit
(600-second timeout) and then the 56 jobs with four workers, largest
volume first and a 2400-second timeout per job. Audit failure prevents
all sampling. A failed or timed-out job is preserved and never retried;
other declared jobs complete. The output directory must not already
exist.

Cost basis: the #1249 controller recorded 41.320 s for its longest L=8
job (17 replicas, 4608 sweeps); the frozen #1249 sampler re-executed
here for timing ran at about 2.0e7 link updates per second. The L=10
schedule is about 4.5e5 sweeps of 4e4 links, roughly 1.8e10 updates, so
about 900 s per job; the whole run is expected to need about one hour of
wall time on four workers, within the per-job timeout by a factor of
about 2.5. Expected precision at this budget, as an engineering estimate
and not a prediction of any value: 4 SE of log R_k of order 0.1 L to
0.15 L.

## Implementation checks

The deterministic audit (`sample --audit`) checks, for L in {4,6,8,10}:
neighbour inverses and commutation; plaquette-boundary versus link
incidence; for k in {1,2}, base in {0,2} and twist counts
{0,1,L^2/2,L^2} on a fixed link pattern: effective flux minus curl equals
the source, d^2=0 of the curl, seam rank equals slice index, incidence
versus curl, heat-bath pairwise balance against direct scores, the sector
bookkeeping on the all-zero and alternative layouts, twist steps and
their reversal, the local-ratio identity against independently computed
conditional probabilities and direct fluxes of both ensembles, invariance
of the conditional estimator under changes of its own link, exact
enumeration of all 625 assignments of the four links of the step
plaquette (over the local Gibbs law of 21 plaquettes, all four estimators
must average to the local partition ratio to 1e-12 in both directions),
inversion of the cumulative tables, rejection of flux, score and
twist-count corruptions, and the sector labels of the declared initial
states of chains 0, 2 and 4; then eight validated sweeps at each of the twist
counts 0,1,8,16,0 on L=4 with seed 1 for both bases; and finally the
complete chain code path of the declared jobs (header, warmup, dwell,
pass, dwell, pass back, footer) on L=4 with a tiny schedule of 4 warmup,
512 dwell, 512 visit and 2 equilibration sweeps, seed 7, for chains 0, 4
and 2 at base 0 and chains 0 and 2 at base 2, written into a memory
buffer that is checked for the frozen segment, twist and phase sequence,
39 fields per row and the completion line, and then discarded; only the
row count is printed. The observed pre-pin
transcript, 238 bytes, SHA-256 `1e2f30627085f6d5b46ae16e1e1249c1041e74ca01447dd8dd73bf0e6c90a41d`, compiled
with GCC 13.3.0 (Ubuntu 24.04 package, x86_64) to binary SHA-256 `72ec9f6cdd3107fda4cac98d95171c1d166f030b2777c7b23d6752a7002e8794`, is:

```text
NON-CANONICAL floating-point engineering audit
geometries	4
fixture_states	64
estimator_identities	384
local_enumerations	96
invariance_checks	384
inversion_checks	42
exercise_sweeps	160
schedule_rows	320
mutations_caught	192
result	PASS
```

The analyzer embeds this transcript and admits no run whose audit differs
from it byte for byte. `test_analyze.py` checks the analyzer on
fabricated records: recovery of fabricated ratios and means, passing of
fabricated exact controls, detection of a frozen alternative sector and
of a violated control identity, rejection of a reordered block, of zeroed
estimator sums at a visit, of a tampered byte count, of a wrong audit
transcript, and the INCOMPLETE and FAIL_IMPLEMENTATION routes for a
timed-out and a crashed job. Fabricated numbers are not scientific values.

## Prospective analysis, gates and statuses

Estimates are regrouped by ensemble m=0..L^2. With F_m the pooled mean of
the conditional forward estimator at m, B_m the pooled mean of the
conditional reverse estimator at m (for step m-1), and relative batch
variances rv at the finest scale,

    w_n = rv_B(n+1)/(rv_F(n)+rv_B(n+1)),
    log R_k = sum_m [ w_m (log F_m + rv_F(m)/2) 1_{m<L^2}
                    - (1-w_{m-1}) (log B_m + rv_B(m)/2) 1_{m>0} ].

The rv/2 terms are first-order corrections of the log of a mean. Batch
standard errors use the per-batch influence
u_b = w_m f_b/F_m 1_{m<L^2} - (1-w_{m-1}) g_b/B_m 1_{m>0}, where f_b and g_b
are the batch means of the forward and reverse estimators in the same
batch, at block scales 512, 1024 and 2048 sweeps (coarsening inside one
segment only), SE^2 = sum_m Var_b(u_b)/B_m, and the reported batch SE is
the maximum over scales of this aggregate. Partial sums over a range of
steps use the same influence restricted to that range. Subset gates use
the pooled within-group batch variance at each m, the deviations being
taken from each group's own mean with the groups being the chains (G3,
G9), the pass directions (G4) or the chain halves (G5), so that the
deviation a gate tests never enters its own tolerance. For the mean of Y
at an endpoint the batch means of Y are used in the same way. The
reported SE is the larger of the batch SE and the between-chain SE, the
standard deviation of the single-chain values divided by the square root
of their number; the gates use the batch SE only, so disagreement cannot
enlarge its own tolerance. Intervals are +-4 SE and are empirical
engineering intervals with NO rigorous coverage claim. The equal-weight
and Bennett estimates of log R_k are recorded as secondary values.

Gates for each main group (L,k):

- G1 completeness: all five chains present with exit 0, empty stderr,
  matching byte counts and hashes, the frozen metadata and block
  sequence, moment consistency, histogram and sector counts, naive sums
  equal to the histogram sums, and the conditional block means within
  the exact bounds.
- G2 forward-reverse: |sum_m (log F_m 1_{m<L^2} + log B_m 1_{m>0})| <= 4 SE,
  with the influence v_b = f_b/F_m + g_b/B_m.
- G3 start independence: each chain's log R_k and mean Y_k agree with
  the values from the other chains within 4 sqrt(SE_c^2+SE_-c^2), both
  SEs from the pooled batch variance.
- G4 direction: the up-pass and down-pass values of log R_k, formed from
  the complete contributions c_m of the intermediate ensembles
  m=1..L^2-1 (the dwell contributions are common to both and cancel
  exactly), agree within 4 SE from the within-direction pooled variance.
- G5 time: each chain's first and second half of its twisted dwell agree
  in mean Y_k within 4 SE from the pooled dwell variance.
- G6 consistency: sum_n (naive mean - conditional mean)/conditional mean
  over steps, forward and reverse separately, within 4 SE of the paired
  batch differences.
- G7 coarsening: the largest divided by the smallest aggregate SE across
  the three block scales is at most 1.5, for log R_k and for mean Y_k.
  For a stationary process the coarse-over-fine SE ratio can never exceed
  2, so 2 is not a threshold; 1.5 corresponds to a batch correlation time of a few blocks
  and lies more than four null standard deviations above 1. Correlation
  beyond the coarsest batch of 2048 sweeps, one visit, is invisible to
  this gate. A zero SE at any scale is degenerate and counts as a G7
  failure.
- G8a calibration: |mean Y_0| <= 4 SE over the n=0 dwells of chains 0
  and 1 only. For these two chains the initial law and the kernel are
  reversal symmetric, so the mean of Y_0 is exactly zero at every sweep;
  the gate tests the batch SE against an exactly known mean and is not an
  equilibration test. The pooled n=0 mean over all chains is reported
  descriptively.
- G8b bound: mean Y_0^2 - 4 SE <= 1 over all n=0 rows, an exact bound of
  the stationary law only; a violation is classed with the equilibration
  gates.
- G9 sector: at the twisted dwell, each chain's fraction of sweeps in the
  pure w=0 layout and in the pure w=-1 layout agrees with the fraction of
  the other chains within 4 sqrt(SE_c^2+SE_-c^2) from the pooled batch
  variance. Chain 4 starts in the pure w=-1 layout, so agreement requires
  that the alternative sector either relaxes or is reached by the others.
- G10 cross-mode positivity, per L when both modes pass G9: the exact
  inequalities R_1 <= 0.618+0.382 R_2 and R_2 <= 0.618+0.382 R_1 of
  PROOF.md (15) hold at the most favourable corners of the two 4 SE
  intervals formed from the batch SE.

Gates for each exact control group (L in {4,6}, k):

- C1: |sum_n log r_n| <= 4 SE (Z(3k)=Z(2k)).
- C2: for every m with 1 <= m < L/2, the sum of log r_n over the middle
  steps mL <= n < (L-m)L lies within 4 SE of zero (PROOF.md (13)).
- C3: |mean Y at source 2k + mean Y at source 3k| <= 4 sqrt(SE^2+SE^2).

Closed status set and strict precedence, implemented in analyze.py:
per (L,k): FAIL_IMPLEMENTATION > INCOMPLETE > FAIL_CONSISTENCY >
INCONCLUSIVE_EQUILIBRATION > SECTOR_FROZEN > UNRESOLVED >
RESOLVED_SIGNED_CONTRAST. A job with exit 124 (timeout) or 127 (launch
failure) makes its group INCOMPLETE and nothing else; the other groups
are analyzed. Any other nonzero exit, nonempty stderr, byte or hash
mismatch, malformed record, histogram or sector inconsistency, audit or
environment mismatch labels every group FAIL_IMPLEMENTATION. Any control
gate failure labels every main group FAIL_CONSISTENCY, as do G6 and
G10 failures; G2, G3, G4, G5, G7, G8a or G8b failure gives
INCONCLUSIVE_EQUILIBRATION; G9 failure alone gives SECTOR_FROZEN. A mode
that passes every gate carries the per-mode outcome GATES_PASSED, which
is not a volume label. In every non-passing case every estimate stays
visible under NONINFERENTIAL_ESTIMATE and the intervals are withheld.
Per L the label is the worst of the two modes; RESOLVED_SIGNED_CONTRAST
requires both modes to pass every gate, both 4 SE half-widths of
log R_k at most 1.0, both 4 SE half-widths of mean Y_k at most 0.05,
and at least one mean-Y_k interval excluding zero; otherwise
UNRESOLVED. An exact control group that is INCOMPLETE leaves its L
without the control guard: the volume of that L and the overall label
are capped at INCOMPLETE. The overall label is the worst volume label;
the result of the item is the per-L list, and an INCOMPLETE or
SECTOR_FROZEN label at one L says nothing about the others.

Reported per (L,k): log R_k and log10 R_k with their intervals, the
value -log R_k/L^2 for that L only, a CONTRAST_NEGLIGIBLE flag when the
upper end of the R_k interval is below 1e-3, mean Y_k with its interval,
the product box exp(log R interval) x Y interval, per-step tables, the
sector occupancy of every chain in every phase, and, when chain 2 stays
at least 95 percent in the pure w=0 layout and chain 4 at least 95
percent in the pure w=-1 layout in every segment of their down passes
and in both of their dwells (at the untwisted dwell: the sum over sweeps
of untwisted slices with w!=0 at most 5 percent of the sweep count), the
difference of their down-and-dwell log ratios as a descriptive
sector-conditional value. Per L the residue-law intervals p_a of PROOF.md
(14) are reported when both modes are complete. The squared range D from
the two product boxes (nearest and farthest points, also on the log10
scale) is quoted only when both modes pass and both log R_k half-widths
are at most 1.0. Values at different L are reported separately; no
comparison, trend, ratio, fit, extrapolation, tension, area-law,
collapse or noncollapse language across L is permitted; the four sizes
are not a scaling study. RESULT.md may describe the run only by the fixed
labels and by which gates fired; the words mixed, equilibrated,
transport, mobility improvement and "guides the proof" are not available
to it. No thermodynamic lower bound, phase decision, P1 statement or
Canon promotion may be inferred.

## Custody and publication

Freeze sample.cpp, analyze.py, run_snake.py, run_analysis.py,
test_analyze.py, PROOF.md, PREREG.md and REVIEW.md. Record their public
commit and SHA-256 in issue #1259 and read the pin back before the first
post-pin compilation. Compile outside the repository with
`g++ -std=c++17 -O3 -ffp-contract=off -Wall -Wextra -pedantic sample.cpp -o <binary>`;
do not use fast-math. The contraction flag forbids fused multiply-add so
that the floating-point trajectory does not depend on the architecture's
default contraction; it changes nothing on the executing system. The controller command is
`python3 run_snake.py <binary> <new-output-directory>`. Then run
`python3 run_analysis.py <output-directory>`, which runs analyze.py as a
subprocess, preserves its stdout as analysis.json and its stderr,
records the analyzer's exit code, byte counts and hashes in
analysis_execution.json, and writes SHA256SUMS_FINAL over every file.

RUN.md records: the pin commit and issue; the SHA-256 of every frozen
file; compiler version and command; binary SHA-256; neutral platform and
architecture; start and end UTC times; controller exit code; analyzer
exit code; audit transcript bytes and hash and its byte identity with
the pre-pin transcript; workers, timeouts and the longest job; that no
job was retried and no launch repeated; that the frozen files are
byte-identical after execution. The complete controller and analysis
outputs are preserved under `ENGINEERING/`. Machine nicknames and
private paths do not belong in the record. The branch name is a harness
artefact and not part of the scientific record; the pin is the commit.

All results remain under this notes-only path. The C++ engine is not a
standard-library exact probe verifier, and the run is not a formal
two-architecture scientific computation gate. Existing notes, Canon,
Registry, Frontier, formal probes, workflows and releases remain
untouched.
