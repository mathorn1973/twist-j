# Sector-restricted twist ladders with a class sum rule

**PUBLIC / NON-CANONICAL. Prospective engineering diagnostic.**

- Item: C-PHOTON-TWIST-SNAKE-SECTOR-N, issue #1265.
- Author: A. M. Thorn.
- Basis: Public Canon v92; main `fe64af20c9aae768de8a25576e3316ba0b5bd352`.
- Scope: L6 finite measure; numerical output has ZERO scientific evidential weight.
- Written identities (PROOF.md): candidate-T, reviewed before execution (REVIEW.md).
- No thermodynamic lower bound, P1, phase or physical-photon decision is authorized.

## Prior knowledge and execution boundary

The predecessor `notes/C-PHOTON-TWIST-SNAKE-DIAGNOSTIC-N` (#1259, merged in
#1260) is a completed and consumed attempt whose preserved records
(`ENGINEERING/analysis.json`, SHA-256
`144456b0897bf0d40a0982d89620b412d7e863a16cc18f904956f5f64ae61c43`, and its
block records) were read before this design. All figures below are
NONINFERENTIAL under that preregistration; none is a prediction here.

- Its disposition was FAIL_CONSISTENCY because one exact control group
  (L=6, k=2) fired C1 at 4.1 batch standard errors; in that group one chain
  sat at the 3k endpoint with mean Y = -3.0 and w = -1 on 91 percent of
  its slices, while the other three chains agreed with each other. The
  frozen rule could not separate a violated identity from an endpoint
  that one chain never reached.
- Its pure-layout sector gate G9 was uninformative at L=8 and L=10, where
  no chain attained a pure layout, while the fraction of twisted slices
  with w = -1 separated the chains clearly: chain 4 (started in the
  alternative layout) recorded 0.83, 0.91, 0.87 and 0.81 at L=4, 6, 8, 10
  for k=2 against 0.02 to 0.10 for every other chain at L>=6 (at L=4
  chain 3 recorded 0.27 with mean Y_2 = +0.52, its two dwell halves at
  -0.47 and +1.50). For k=2 at L>=6 the single-link heat bath did not move
  any chain between the two sectors in 16384 dwell sweeps; chain 4
  recorded mean Y = -2.26 and the others +1.50 to +1.51.
- Recomputing the consumed control groups at L=6 per chain with the
  consumed analyzer's own subset routine: for k=2 the chain sums of
  log r_n are +0.05, +0.17, +0.34 and +0.86 (chains 0-3; pooled +0.35,
  batch SE 0.09), the last being the chain with mean Y = -3.0 at the 3k
  endpoint; for k=1 they are -2.35, -2.34, +2.34 and +2.37, the two chains
  started at the 2k endpoint recording mean Y = +2.26 at the 3k endpoint
  and the two started there recording -1.51, so that C1 passed only by
  the cancellation of two groups of chains that never agreed on the
  endpoint (control sources 2k = 2 and 3k = 3 for k=1 carry the sector
  structure that the main ladders meet at k=2, not at k=1). Under the
  rule below both L=6 control groups would have been CONTROL_SECTOR_FROZEN
  and the L=4 groups read.
- At twist count 1 the single twisted slice had w = -1 in 0.033 to 0.044
  (L=4), 0.047 to 0.060 (L=6), 0.065 to 0.082 (L=8) and 0.100 to 0.112
  (L=10) of the sweeps for k=1, and in 0.197 to 0.249 of the sweeps for
  k=2 at every L, for the chains that had never visited the alternative
  sector. The two chains that reached twist 1 after a down pass from the
  alternative sector (chain 4 at L=8 and L=10, k=2) recorded 0.735 and
  0.686 there and mean Y = -3.76 at twist 0 instead of the exact value
  zero: a state trapped at the twisted endpoint stayed trapped through
  the down pass. The step-0 estimators of the relaxed chains lay at
  F_0 = 0.785-0.796 and Bw_1 = 1.24-1.28 (k=1), F_0 = 0.443-0.457 and
  Bw_1 = 2.17-2.26 (k=2), so log r_0 is about -0.23 (k=1) and -0.79 (k=2)
  at every L.
- For k=1 every ladder was consistent at every L (log R_1 about -0.48,
  mean Y_1 about +0.755) and chain 4 relaxed to the other chains.

This design adopts three consequences. (i) The sector is tracked by the
exact integer W_n of PROOF.md (1), the sum of w_j over the twisted slices,
and the link fields are split into two classes by the sign of 2W_n + n;
the partition ratio is estimated separately inside each class by
restricted ladders whose single-link kernel cannot leave the class, and
the classes are recombined by the exact sum rule PROOF.md (9)-(10) with
the class weights measured at twist count 1, where the consumed records
show both classes occupied. (ii) The unconstrained ladder is kept as an
exact cross-check and receives a sector gate built on the class indicator
and the w = -1 slice fraction rather than on pure layouts. (iii) The exact
control groups are read only after their endpoint chains agree in sector
observables. The design does not claim that the restricted kernel is
irreducible on a class (PROOF.md section 2); it probes that assumption
with chains started in the cold class layout at the twisted endpoint.

No #1259 output, seed, run, threshold value, budget or identifier is
resumed or extended. The seed base 202609300000 is distinct from the
consumed 202609280000 and from the #1249 base 202609270000; no job of this
design reproduces a consumed trajectory. The unconstrained round-trip
schedule, block format, estimators, control identities and gates G1-G8 of
#1259 are retargeted under a new identifier and a new pin.

This design has no mobility observable. The twist count is driven by a
fixed schedule; passing every gate means that no preregistered
inconsistency was detected, not that any ensemble was equilibrated or
sampled at stationarity.

## Pre-pin rule

Before the public pin the compiled binary was executed only as
`sample --audit`, a deterministic implementation test whose output is a
fixed-form transcript containing no estimate of any target quantity;
`test_analyze.py`, which fabricates block records from declared
pseudo-random parameters in Python and never calls the sampler, was
executed; and a separate throughput harness that includes `sample.cpp`,
performs 80 heat-bath sweeps of the unrestricted and of the two restricted
kernels at L=10 from a hot start and prints only milliseconds per sweep,
was compiled and executed once, its output discarded except the figures
in the cost basis below. No invocation of the production entry point
`sample L k chain kind`, with any argument, took place before the pin. The
sweep counts of the schedule are prior design choices; the two changes
made after the first synthetic tests (four step-zero chains and 32768-sweep
dwells for the step-zero and restricted endpoint dwells, and the use of two
block scales for restricted ladders) were made because the fabricated null
of the coarsening gate G7 fired at the 3 percent level with 64 blocks and
because a two-chain single-visit ladder has no within-chain degrees of
freedom at the coarsest scale; they were fixed before any sampler output
existed. The audit's fixture patterns, tolerances, exercise seeds and
printed counts may not be changed after the pin. REVIEW.md discloses every
pre-pin audit failure and the code change it caused.

## Fixed carrier and observables

For L in {4,6,8,10}, the periodic positively oriented cubical four-torus,
links alpha in F5, W(f) = 2+2cos(2 pi f/5), the seam Sigma of the L^2
positive 01 plaquettes at x0=x1=0 ordered by j = x2 + L x3, and for k in
{1,2} the partially twisted ensembles nu_n of #1259 with

    R_k = Z_k/Z_0 = prod_{n<L^2} r_n,  r_n = Q_{n+1}/Q_n,
    Y_k = L^-2 sum_(p parallel 01) tan(pi F_p/5),  F = curl + source,
    -i C_k = R_k E_{pi_k} Y_k,  E_{pi_0} Y_0 = 0,  E_{pi_0} Y_0^2 <= 1.

Per slice j the integer w_j = (s_j - c_j)/5 of PROOF.md (1) with the
source-inclusive flux representatives; W_n = sum_{j<n} w_j; the classes
C_0(n) = {2 W_n >= -n} and C_-(n) = {2 W_n < -n}. The restricted step
estimators of PROOF.md (6) are, for a chain restricted to class c,

    F  = rho_n 1[C_c(n+1)]         at twist n,
    PF = 1[C_c(n+1)]               at twist n,
    PB = 1[C_c(n)]                 at twist n+1,
    Bw = rho_n^-1 1[C_c(n)]        at twist n+1,

with rho_n = W(F_q + k)/W(F_q) at the step plaquette q = q_n, and
r_n^{(c)} = F/PB = PF/Bw exactly. Their conditional (Rao-Blackwellised)
forms PROOF.md (8), averaged over the four boundary links of q, are
primary; the naive forms are recorded with the exact integer flux
histograms of q over the indicator-1 sweeps, so that every naive sum is an
integer-weighted sum of a histogram. PB has no conditional form. For the
unconstrained chains the indicators are identically one and F, Bw are the
estimators of #1259. Bounds: F, Bw in [0, 6.854] (k=1) and [0, 10.47]
(k=2), with the lower bound 0.1459 respectively 0.09549 for unconstrained
chains; PF, PB in [0,1].

Every production sweep records, in addition: the class indicator
1[2 W_n + n < 0], W_n and the block extremes of W_n, the numbers of
twisted slices with w = 0, -1, +1, other, the numbers of untwisted slices
with w = -1, +1, other, the pure-layout label and its changes (descriptive
only), and whether the up step that opened the segment reset the new
slice (`forced`).

## Fixed numerical kernel, groups and budget

The standard-library C++17 sampler uses the single-link five-state heat
bath at the target weight and no other move; on a restricted chain the
candidates of a 0- or 1-link of a twisted slice that would leave the class
receive weight zero and the remaining probabilities are renormalised
(PROOF.md section 2). The twist count changes only between segments, by
one plaquette, through the exact cache update; on a restricted chain an up
step whose field leaves the class resets the 0- and 1-links of the newly
twisted slice to the class layout (all zero for class 0; alpha_0 = 2 on
the 0-link at x0 = x1 = 0 and zero elsewhere for class minus), which is
followed by 512 discarded sweeps instead of 32. Per-slice flux sums and
W_n are maintained incrementally and compared with direct recomputation
every sweep; a restricted chain that records a sweep outside its class
exits nonzero. Every chain counts its heat-bath sweeps and prints the
total, which the analyzer requires to equal warmup + production +
32 x (twist steps without a reset) + 512 x (resets).

Per (L,k) the declared job groups are (kind codes in the CLI
`sample L k chain kind`):

| Group | kind | chains | start | schedule |
|---|---|---|---|---|
| U | 0 | 0 cold0, 1 hot0, 2 coldT, 3 hotT, 4 coldAltT | 0,0,L^2,L^2,L^2 | warmup 512; dwell 16384; L^2-1 visits of 32 discarded + 2048; dwell 32 + 16384; visits back |
| P | 3 | 0 cold0, 1 hot0, 2 cold0, 3 hot0 | 0 | warmup 512; dwell 32768 at 0; one step, 32 discarded; dwell 32768 at 1 |
| C0 | 4 | 0 cold1C0, 1 hot1C0 | 1 | warmup 512; visits 2048 at n = 1..L^2-1 (32 discarded after a step, 512 after a reset); dwell 32768 at L^2 |
| C0 | 4 | 2 coldTC0 (all zero) | L^2 | warmup 512; dwell 32768 at L^2 |
| CM | 5 | 0 coldAlt1CM, 1 hot1CM | 1 | as C0 chains 0, 1 |
| CM | 5 | 2 coldAltTCM (alternative layout on every slice) | L^2 | warmup 512; dwell 32768 at L^2 |
| control | 2 | 0..3 as U, L in {4,6} only, whole-seam source 2k | as U | as U |

Cold starts have all links zero; hot starts independently uniform links;
the class-minus cold starts carry alpha_0 = 2 on the 0-link at x0 = x1 = 0
of slice 0 (chains 0) or of every slice (chain 2); a hot restricted start
whose drawn field lies outside the class has slice 0 reset to the class
layout. Chain 4 of U is the consumed alternative layout. There are 136
declared jobs (40 U, 32 P, 24 C0, 24 CM, 16 control); seed
202609300000 + 1000 L + 100 k + 10 kind + chain. Blocks are 512
consecutive production sweeps, every production sweep measured once after
the full heat-bath sweep; 49 fields per block row. No adaptive length,
seed, threshold or stopping rule is allowed after observation.

The cached effective flux, slice sums, W_n and score are compared with
direct recomputation after every block and every twist change and W_n
every sweep; failure exits nonzero. The controller `run_snake.py` runs the
audit (600-second timeout) and then the 136 jobs with four workers,
largest L first and within an L the U, C0, CM, P and control groups in
that order, with a 2400-second timeout per job. Audit failure prevents
all sampling. A failed or timed-out job is preserved and never retried;
other declared jobs complete. The output directory must not already exist.

Cost basis: the #1259 controller recorded 650-666 s for its L=10 jobs
(4.45e5 sweeps, 1.49 ms per sweep of 4e4 links); the throughput harness
measured 1.66 ms per unrestricted sweep and 3.2 ms per restricted sweep
at L=10 with half of the slices twisted. Expected job times at L=10: U
about 740 s, restricted up-only about 800 s (2.6e5 sweeps at a rising
restricted fraction), restricted top dwell about 120 s, P about 110 s;
the whole run about 2.4e4 CPU-s, roughly 100 to 120 minutes of wall time
on four workers. The worst case for a restricted up-only job (every step
reset, 5.4 ms per fully twisted class-minus sweep) is about 1100 s, a
factor 2.2 below the per-job timeout. Expected precision at this budget,
an engineering estimate and not a prediction of any value: the consumed
unconstrained ladders gave 4 SE of log R_1 of 0.013 L with 20480 sweeps
per intermediate twist; a two-chain single-visit ladder has 4096, so the
class-sum 4 SE of log R_1 is expected of order 0.03 L, and that of log R_2,
whose per-chain spread in the consumed run was about ten times larger,
of order 0.3 L, so the 1.0 half-width criterion may fail for k=2 at L=8
and L=10 and the volume label there is then UNRESOLVED by the frozen
rule. The class-sum mean Y_k carries the term (Y_- - Y_0)^2 Var(P_-), so
for k=2 its 4 SE half-width can exceed 0.05 whenever the class weight P_-
is neither close to 0 nor close to 1, with the same consequence.

## Implementation checks

The deterministic audit (`sample --audit`) checks, for L in {4,6,8,10}:
neighbour inverses and commutation; plaquette-boundary versus link
incidence; that every 0- and 1-link has exactly two 01 plaquettes, both
in its own slice; for k in {1,2}, base in {0,2} and twist counts
{0,1,L^2/2,L^2} on a fixed link pattern: effective flux minus curl equals
the source, d^2 = 0, seam rank equals slice index, incidence versus curl,
the slice change of a link against direct recomputation for all five
candidates, heat-bath pairwise balance, the sector bookkeeping of the
all-zero and alternative layouts including W_n, twist steps and their
reversal including the slice sums, the local-ratio identity against
independently computed conditional probabilities and direct fluxes,
invariance of the conditional estimators under changes of their own
link, exact enumeration of all 625 assignments of the four links of the
step plaquette (all estimators average to the local partition ratio to
1e-12 in both directions), rejection of flux, score, twist, slice-sum
and W_n corruptions; for both classes, k in {1,2} and twist counts
n in {1,2,3,4,L^2/2,L^2/2+1}, layout states with W_n at and away from the
class boundary and three layouts of slice n: the up step leaves the class
exactly when the layout arithmetic says so, the reset restores the class,
changes no other slice and leaves the sum of the other twisted slices
unchanged; exact restricted local enumeration in both directions with the
four estimators, both pairings and the class indicators compared with
direct recomputation, with the number of enumerations whose indicator
takes both values on the fixed pattern printed (`mixed_enumerations`);
the restricted single-link law against direct class recomputation of all
five candidates, including the inversion of its cumulative table at
midpoints, boundaries and one ulp below one; the declared initial states
of every kind and chain (class and W_n); eight validated sweeps at the
twist counts 0,1,8,16,0 on L=4 with seed 1 for both bases, and eight
validated restricted sweeps at twist counts 1,2,5,8,16 for both classes
with the number of zero-weight candidates counted (`forbidden_candidates`,
required positive); and the complete chain code path of every kind (round
trip, step zero, up-only, top dwell) on L=4 with a tiny schedule (4
warmup, 512 dwell, 512 long dwell, 512 visit, 2 equilibration, 4
post-reset sweeps, seed 7) written into a memory buffer that is checked
for the frozen segment, twist, phase and class sequence, the forced
flags, the printed sweep total against the schedule formula, 49 fields
per row and the completion line, and then discarded; the class-reset
check also runs on the fixed link pattern at twist n+1 and requires every
link outside the 0- and 1-links of slice n unchanged; the restricted
sweep exercise feeds every sweep to a scratch recorder and requires the
indicator-1 histograms to follow the two indicators exactly. The observed pre-pin
transcript, 384 bytes, SHA-256 `c1286c6e30e6876c1e1c4bba0a20efdcf9e94eb4d0e2958739cb094300c8533e`, compiled with GCC
13.3.0 (Ubuntu 24.04 package, x86_64) to binary SHA-256 `21c5cb2ebe983c325131cf26f928da226d063297f8136f7c83e8348fa6318805`, is:

```text
NON-CANONICAL floating-point engineering audit
geometries	4
fixture_states	864
estimator_identities	384
local_enumerations	96
restricted_enumerations	1312
mixed_enumerations	10
forcing_checks	1440
restricted_law_checks	6976
invariance_checks	384
inversion_checks	42
exercise_sweeps	160
restricted_sweeps	160
forbidden_candidates	961
schedule_rows	464
mutations_caught	320
result	PASS
```

The analyzer embeds this transcript and admits no run whose audit differs
from it byte for byte. `test_analyze.py` checks statically that the
sampler's header literal, metadata keys, seed base and field count agree
with the analyzer, and checks the analyzer on fabricated records:
recovery of fabricated step ratios, class weights, restricted ladder sums,
endpoint means and the class sum with the unconstrained cross-check
passing; a frozen unconstrained chain (U route SECTOR_FROZEN, class sum
unaffected); a violated control identity; a control endpoint chain in
another sector (CONTROL_SECTOR_FROZEN, with and without another qualified
control of the same mode); rejection of a reordered block, of zeroed
estimator sums at a visit, of a class-0 block reaching class minus, of a
forced flag on an unconstrained chain, of a tampered byte count and of a
wrong audit transcript; INCOMPLETE for a missing or timed-out class-sum
job and for a timed-out control; the U route alone INCOMPLETE for a
missing U job; FAIL_IMPLEMENTATION for a crashed job; and one fabricated
deviation per gate (U G2-G7, G9', calibration, G10, G11 on log R and on
pi_1(-), restricted G2, G3, G5, G6 for PF and Bw, G7, the plateau chain
in Y and in W, P chain and half disagreements, a zero-indicator step, C3,
a degenerate variance, a negligible contrast). Fabricated numbers are not
scientific values.

## Prospective analysis, gates and statuses

*Step estimator, every ladder.* With pooled means F_m, PF_m of the
conditional forward estimators at twist m and PB_m, Bw_m of the reverse
estimators at m (for step m-1), and relative batch variances rv at the
finest scale,

    log r_n = 1/2 [ (log F_n + rv/2) + (log PF_n + rv/2)
                  - (log PB_{n+1} + rv/2) - (log Bw_{n+1} + rv/2) ],

the equal-weight geometric mean of the two exact pairings, with no
data-driven weights. Batch standard errors use the per-batch influence
u_b = 1/2 (f_b/F_m + pf_b/PF_m) [step m exists] - 1/2 (pb_b/PB_m +
bw_b/Bw_m) [step m-1 exists] at block scales 512, 1024 and 2048 sweeps
(coarsening inside one segment only), SE^2 = sum_m Var_b(u_b)/B_m, and the
maximum over scales. Subset gates use the pooled within-group batch
variance (groups: chains, pass directions, chain halves), so the tested
deviation never enters its own tolerance; for a restricted ladder (two
chains, one visit per twist) the within-chain pooled variance of the
ladder sum uses the scales 512 and 1024 only, since at 2048 sweeps each
visit is one batch per chain, while its aggregate SE, deficit, G6 and G7
keep all three scales (one degree of freedom per intermediate twist at
the coarsest scale; under an independent-block null the G7 ratio of the
ladder sum exceeds 1.5 with probability about 3 percent at L=4, 0.1
percent at L=6 and below 0.01 percent at L=8 and L=10, and with a block
autocorrelation of 0.5 in more than half of the cases at every L). The
reported SE of every quantity is the larger of its batch SE and its
between-chain SE; the gates use batch SEs only. Intervals are +-4 SE,
empirical engineering intervals with NO rigorous coverage claim. A
pooled mean of zero of any restricted estimator at any twist makes that
ladder INCONCLUSIVE_EQUILIBRATION (named failure); a zero mean in one
chain alone withholds that chain's ladder value and G3 (named failure,
INCONCLUSIVE_EQUILIBRATION); neither is a custody failure.

*Class sum (primary route), per (L,k).* log r_0 from the P group
(1/2[(log F_0 + rv/2) - (log Bw_0 + rv/2)] with F_0 at its twist-0 dwell
and Bw_0 at its twist-1 dwell); pi_1(-) the class-minus fraction at the P
twist-1 dwell; l_c = sum_{n=1}^{L^2-1} log r_n^{(c)} from the C0 and CM
ladders (chains 0 and 1; chain 2 contributes to the endpoint dwell only);
E^{(c)} Y from the three-chain endpoint dwells; then PROOF.md (9)-(10).
Errors by the delta method with log r_0, pi_1(-), l_0, l_- and the two
endpoint means treated as independent (log r_0 and pi_1(-) share the P
twist-1 sweeps; their covariance is declared neglected): Var(log R) = Var(log r_0) +
P_0^2 Var(l_0) + P_-^2 Var(l_-) + ((e^{l_-} - e^{l_0})/D)^2 Var(pi_1(-)),
Var(P_-) = (P_0 P_-)^2 (Var(l_0) + Var(l_-)) + (e^{l_0+l_-}/D^2)^2
Var(pi_1(-)), Var(E Y) = P_0^2 Var(Y_0) + P_-^2 Var(Y_-) + (Y_- - Y_0)^2
Var(P_-), each with the batch and with the report SEs.

Gates of the P group: chain agreement, each chain against the others (4
sqrt(SE^2+SE^2), within-chain pooled variance), in the class-minus
fraction, mean Y and Bw at twist 1 and in F and mean Y at twist 0; time
halves of every chain's dwells in the class-minus fraction and mean Y (4
SE, within chain-half pooled); coarsening ratios at most 1.5 for
pi_1(-), mean Y at twist 1 and log r_0; calibration |mean Y_0| <= 4 SE
(exactly zero for the reversal-symmetric initial laws and kernel) and the
bound mean Y_0^2 - 4 SE <= 1. Any failure: INCONCLUSIVE_EQUILIBRATION.

Gates of each restricted group (C0, CM): G1 completeness and the class
membership of every block (block extremes of W_n inside the class);
G2 pairing deficit sum_n [(log F - log PB) - (log PF - log Bw)] within
4 SE of zero (unit-weight influence); G3 the two ladder chains' l_c
against each other and the three endpoint chains' mean Y, mean W and
all-slice w = -1 count each against the other two (4 SE, within-chain
pooled; a zero pooled variance with a nonzero difference is a
disagreement); G5 halves of every endpoint dwell in mean Y; G6 naive
against conditional for F, PF and Bw separately (paired block
differences, 4 SE); G7 coarsening at most 1.5 for l_c and for mean Y;
zero-mean steps as above. G6: FAIL_CONSISTENCY; the others:
INCONCLUSIVE_EQUILIBRATION.

*U route (cross-check), per (L,k), read only when all five chains are
present.* G1-G8 of #1259 with the step estimator above, and G9': at the
twisted dwell each chain's class-minus fraction and its w = -1
twisted-slice count per sweep agree with the other chains' (4 SE,
within-chain pooled). Sub-labels: FAIL_CONSISTENCY (G6),
INCONCLUSIVE_EQUILIBRATION (G2, G3, G4, G5, G7, G8a, G8b, degenerate SE),
SECTOR_FROZEN (G9' alone), GATES_PASSED. G6 of the U route also labels the
(L,k) FAIL_CONSISTENCY (shared implementation); its other failures do not
touch the class-sum label.

G11 exact cross-check, read only when the U route is GATES_PASSED and the
class-sum route has fired none of its own gates: the U ladder's log R_k,
its step-0 value and the class-minus fraction of its chains 0 and 1 at
their twist-1 up visits agree with the class-sum log R_k, the P log r_0
and the P pi_1(-) within 4 sqrt(SE^2+SE^2) (batch SEs, the class-sum SE
by the delta method). Any disagreement: FAIL_CONSISTENCY for the (L,k),
because both routes are exact and both passed their own equilibration
gates.

G10 cross-mode positivity, per L when both class-sum routes pass: the
exact inequalities R_1 <= 0.618 + 0.382 R_2 and R_2 <= 0.618 + 0.382 R_1
hold at the most favourable corners of the two 4 SE intervals formed from
the delta-method batch SEs. Violation: FAIL_CONSISTENCY for both modes.

*Exact control groups (L in {4,6}, k).* Sector qualification first: at
both endpoint dwells the four chains agree leave-one-out (4 SE,
within-chain pooled) in the all-slice w = -1 count, the all-slice w = +1
count and mean Y; otherwise CONTROL_SECTOR_FROZEN and C1-C3 are not read.
A qualified group is read with C1 (|sum_n log r_n| <= 4 SE), C2 (middle
blocks mL <= n < (L-m)L for 1 <= m < L/2 within 4 SE of zero) and C3
(|mean Y at 2k + mean Y at 3k| <= 4 sqrt(SE^2+SE^2)); G6 of a control
ladder is FAIL_CONSISTENCY as well. The control sources 2k and 3k are
unrelated to the sector structure of mode k itself, so the four control
groups are read as one implementation check: any qualified control group
that fails labels every main group FAIL_CONSISTENCY; if no control group
is qualified, every main group that would pass is capped at
INCONCLUSIVE_EQUILIBRATION. A control group that is INCOMPLETE caps its
own L and the overall label at INCOMPLETE. The per-chain sums of log r_n
of every control group are reported.

*Closed status set and precedence*, implemented in analyze.py: per (L,k)
FAIL_IMPLEMENTATION > INCOMPLETE > FAIL_CONSISTENCY >
INCONCLUSIVE_EQUILIBRATION > UNRESOLVED > RESOLVED_SIGNED_CONTRAST. A
job with exit 124 or 127 makes its (L,k) INCOMPLETE if it belongs to the
P, C0 or CM group and makes only the U route INCOMPLETE otherwise; any
other nonzero exit, nonempty stderr, byte or hash mismatch, malformed
record, histogram, class or sector inconsistency, audit or environment
mismatch labels every group FAIL_IMPLEMENTATION. A mode that passes every
gate of the class-sum route carries the per-mode outcome GATES_PASSED,
which is not a volume label; in every non-passing case every estimate
stays visible under NONINFERENTIAL_ESTIMATE and the intervals are
withheld. Per L the label is the worst of the two modes;
RESOLVED_SIGNED_CONTRAST requires both modes to pass every gate, both 4 SE
half-widths of the class-sum log R_k at most 1.0, both 4 SE half-widths
of the class-sum mean Y_k at most 0.05, and at least one mean-Y_k
interval excluding zero; otherwise UNRESOLVED. The overall label is the
worst volume label; the result of the item is the per-L list.

Reported per (L,k): the class-sum log R_k and log10 R_k with their
intervals, -log R_k/L^2 for that L only, a CONTRAST_NEGLIGIBLE flag when
the upper end of the R_k interval is below 1e-3, the class weight P_- with
its SE, the class-conditional means E^{(c)} Y and the class-sum mean Y_k
with its interval, the product box, log r_0 and pi_1(-), the ladder sums
l_c with per-step tables, the U-route values and its G11 comparison, the
forced-step counts by chain and by parity of n, and the sector records of
every chain in every phase. Per L the residue-law intervals of #1259
PROOF.md (14) and the squared range D from the two product boxes are
reported as in #1259 when both modes pass and both log R_k half-widths
are at most 1.0. Values at different L are reported separately; no
comparison, trend, ratio, fit, extrapolation, tension, area-law, collapse
or noncollapse language across L is permitted; the four sizes are not a
scaling study. RESULT.md may describe the run only by the fixed labels
and by which gates fired; the words mixed, equilibrated, transport,
mobility improvement, ergodic and "guides the proof" are not available
to it; the class weights P_- are finite-volume records and carry no
thermodynamic reading. No thermodynamic lower bound, phase decision, P1
statement or Canon promotion may be inferred.

## Custody and publication

Freeze sample.cpp, analyze.py, run_snake.py, run_analysis.py,
test_analyze.py, PROOF.md, PREREG.md and REVIEW.md. Record their public
commit and SHA-256 in issue #1265 and read the pin back before the first
post-pin compilation. Compile outside the repository with
`g++ -std=c++17 -O3 -ffp-contract=off -Wall -Wextra -pedantic sample.cpp -o <binary>`;
do not use fast-math. The controller command is
`python3 run_snake.py <binary> <new-output-directory>`. Then run
`python3 run_analysis.py <output-directory>`, which runs analyze.py as a
subprocess, preserves its stdout as analysis.json and its stderr, records
the analyzer's exit code, byte counts and hashes in
analysis_execution.json, and writes SHA256SUMS_FINAL over every file.

RUN.md records: the pin commit and issue; the SHA-256 of every frozen
file; compiler version and command; binary SHA-256; neutral platform and
architecture; start and end UTC times; controller exit code; analyzer
exit code; audit transcript bytes and hash and its byte identity with the
pre-pin transcript; workers, timeouts and the longest job; that no job
was retried and no launch repeated; that the frozen files are
byte-identical after execution. The complete controller and analysis
outputs are preserved under `ENGINEERING/`. Machine nicknames and private
paths do not belong in the record. The branch name is a harness artefact
and not part of the scientific record; the pin is the commit.

All results remain under this notes-only path. The C++ engine is not a
standard-library exact probe verifier, and the run is not a formal
two-architecture scientific computation gate. Existing notes, Canon,
Registry, Frontier, formal probes, workflows and releases remain
untouched.
