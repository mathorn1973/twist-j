# Fixed-budget acceptance for one protected pair

PUBLIC NON-CANONICAL proposed experimental design; no acquisition or scientific
program was run. Reservation: [#1448][issue]. Branch:
`codex/v101-ca40-pair-experiment-design`. Public base:
`6aae5de19bd2e04049b4d6893f18291e8465bf1a`. Date: 2026-10-10.
Original text Apache-2.0. These are chosen prototype engineering thresholds,
not measured apparatus specifications or an executed preregistration.

## 1. Fixed scope and the two data stages

The selected ions are 4 and 5, at both normalized G angles +/-4 pi/5.
Ions (1,2,3,6,7) start in the full five-level product state
`F|0> tensor F|1> tensor F|2> tensor F|3> tensor F|4>`.
All amplitudes remain part of the test. The gate, matched-idle and force-off
sham arms use the same declared preparation, protection and readout interfaces.
Their complete pulse words and distinct ideal outputs must be frozen.
Each sign/arm has one protected-block waveform and correction file, independent
of active input labels, spectator analysis basis and measurement row. Only
preparation and post-boundary analysis vary. Input-conditioned gate phases or
corrections are forbidden: they would test different maps across the panel.

The panel has 266 quantum settings per sign and arm: 150 basis-input/spectator
MUB settings, 80 star-Ramsey settings and 36 active-pair product-MUB settings.
There are another 42 motion settings per sign and arm: seven axial modes,
red/blue sideband, and three fixed probe areas. Thus the default total is
`(266+42)*2*3=1848` settings. Any coupled radial modes must be added before
freezing: M resolved modes give `6*(266+6M)` settings, not the default total.

| Stage | Attempts per setting | Total at M=7 | Permitted use |
|---|---:|---:|---|
| Pilot | 200 | 369,600 | Tune, assess feasibility, or stop before validation |
| Fresh validation | 6000 | 11,088,000 | The single frozen acceptance decision |

The quantum-only part of the pilot is 319,200 attempts; its motion part is
50,400. Pilot observations cannot contribute to validation estimates.
Calibration has a separate preregistered setting list and shot cap; it is
not hidden in either total. No validation starts until that cap, the calibrated
measurement model and its uncertainty contract are supplied. No apparatus
calibration or hardware access is supplied by this note.

At a hypothetical uniform 10 ms per attempt the full panel takes 30.8 hours;
at 20 ms it takes 61.6 hours, before calibration or overhead. The full pilot
takes 61.6 minutes at 10 ms; its quantum-only part takes 53.2 minutes.
The actual budget is `sum_setting N_setting*t_trial(setting)+T_cal+T_overhead`.
Destructive motional probes need not have the same duration as quantum rows.

Freeze pulse/compiler and classifier hashes, detector mappings, all score
definitions, analysis phases, systematic bounds, setting list, shot allocation,
randomization procedure and timing contract before fresh validation. A blinded
analyst receives coded arm labels; the arm key opens only after raw-data and
analysis-version hashes are recorded. Tuning personnel do not alter the locked
analysis from validation outcomes. A known target is not a blind prediction.

Interleave sign/arm/setting blocks in a predeclared randomized order and retain
timestamps. Choose the analysis basis independently of the gate output,
preferably after the protected block. Fixed balanced allocation alone does not
prove this independence. Record the required common-state/stability assumption.

Exactly 6000 attempted records per setting are used. Lost ions, ambiguous
classification and erasures are retained, not replaced by extra successful
shots. A safety stop preserves the partial record and yields INCONCLUSIVE,
unless a fully completed predeclared N=6000 comparison (both arms where
required), or a calibrated duration breach, already establishes FAIL.
An outcome-dependent partial-sample interval is not used; no anytime-valid
statistical rule is specified here. No extra shots are added
to turn an inconclusive result into a pass. A revised apparatus gets a new
frozen validation identifier and retains the earlier outcome.

## 2. Scores and simultaneous uncertainty

Every attempt retains seven reported labels and all flags. A probability
indicator lies in [0,1]. Ramsey scores are +1 or -1 for the designated target
outcome only when the control label is correct and all seven codes are valid;
otherwise they are zero. They lie in [-1,1]. No renormalization by survival,
correct-control counts or detected population is allowed.

Use fixed weighted bounded-observable intervals, not clipped reconstructed
states or a fitted fringe with unpropagated fit uncertainty. Let

```text
T_hat = sum_l weight_l Y_l,
T_*   = sum_l weight_l E[Y_l | past before this observation],
V     = sum_l weight_l^2 (high_l-low_l)^2,
h     = sqrt((V/2) log(2 K/alpha_stat)).
```

Each Y_l is bounded by [low_l,high_l]. All weights and ranges are fixed
independently of validation outcomes.
Use `K=100000` and `alpha_stat=0.025`; enumerate at most that many reported
primitive/contrast intervals before acquisition. The seven five-label
marginal histograms alone use 35*1848=64,680 intervals. The other fixed rows
are 1848 flag rates, 900 A pair returns, 666 spectator returns, 222 spectator
gate-idle contrasts, 480 B signed components, 480 aligned Q/R components,
six C overlap/return scores, 84 motion contrasts and 18 drift contrasts:
69,384 primitive intervals in total for the seven-mode baseline. Linear
reconstruction and circular
phase bounds propagate these intervals and earn no extra sampling confidence.
The unused K allowance is conservative, not permission to add primary tests;
the full joint outcome table is retained but is not given 5^7 simultaneous
cell intervals. Extra exploratory claims do not silently enter this family.

The bound is
`Pr(|T_hat-T_*|>h) <= alpha_stat/K`.
Conditional Hoeffding's lemma bounds each centered exponential moment by
`exp(lambda^2 weight_l^2 range_l^2/8)`. Iteration, Chernoff optimization and
a union bound give the displayed rule, also for adapted records. This is
standard bounded-variable/martingale mathematics [H63, A67], not a new result.
It does not assume shot independence or erase slow drift. Its estimand is the
campaign's average conditional score, not a guaranteed stationary future gate.

The reserved joint calibration/model failure budget is `alpha_cal=0.025`.
For each physical estimand a predeclared calibration supplies a valid bound
`|T_physical-T_*|<=b_sys`, jointly except with probability alpha_cal.
Use `[T_hat-h-b_sys,T_hat+h+b_sys]`, or the corresponding asymmetric
calibration bounds. Do not subtract a point SPAM correction and forget its
uncertainty. State-preparation imperfections in the actual tested state are
not automatically removable errors. Readout/control uncertainty must be
propagated through the actual score coefficients, including negative weights.
Classical basis confusion calibration alone is insufficient for the coherent
MUB, Ramsey and joint-return claims. The trusted analysis/POVM bounds must
cover seven-ion readout correlations, coherent analysis errors and cross-talk;
independent detector errors are not assumed merely to reduce calibration cost.
Unknown or unsupported measurement-model error makes the physical decision
INCONCLUSIVE, however good a raw score looks. At the declared scope the joint
sampling-plus-calibration coverage is at least 95% by a union bound.

At N=6000 the sampling-only halfwidths are approximately 0.0364 for one
probability, 0.0515 for a direct gate-minus-idle probability contrast, and
0.0728 for a Ramsey quadrature. These are illustrations of the exact formula,
not rounded decision boundaries. For a contrast use its fixed signed weights
on both arms; subtracting two separate generic intervals is valid but looser.

## 3. Required prototype decisions

L and U below are simultaneous bounds including the stated systematic
uncertainty. A lower-bound requirement T>=t passes only if L>=t and fails
if U<t. An upper-bound requirement T<=t passes only if U<=t and fails if
L>t. Everything between is INCONCLUSIVE. Two-sided requirements use both
ends. All indicated settings and both signs must pass; averaging bad settings
into good ones is forbidden. An unknown prerequisite is also INCONCLUSIVE.

| Required quantity | Prototype PASS threshold | Scope |
|---|---|---|
| Correct active basis-pair output | L>=0.90 | Every A input and arm; any invalid record scores zero |
| Joint return of all five spectator states | L>=0.85 | Fourier-return rows in A, B and C(v=0,w in all six bases); all five inverse analyses precede any fluorescence |
| Spectator return change | L(G-idle)>=-0.10 | Each matched return context; absolute criterion also applies |
| Any invalid/leakage/loss outcome | U<=0.05 | Every setting; inferred physical leakage includes missed-event uncertainty |
| Phase-aligned active Ramsey Q | L>=0.75 | Every B control, star transition, orientation, sign and arm |
| Orthogonal active Ramsey R | [L,U] subset [-0.20,0.20] | Same B cells, with target phase fixed before data |
| Target entangled-output overlap | L>=0.60 | Each G sign, under the measurement/preparation contract below |
| Active product-state return in idle/sham C | L>=0.90 | Direct matching product-Fourier projection, not the entangled target |
| Motional response change | [L(G-idle),U(G-idle)] subset [-0.10,0.10] | Every red/blue mode/probe-area setting |
| Protected-block duration | Every trace's upper endpoint <=1.0 ms | Both signs, including calibrated timestamp uncertainty |

These thresholds are intentionally a component-development decision. They
do not imply 90% or 99% fidelity for a 56-G contact. Matched idle and sham are
not zero-error standards: their absolute tests are retained, and sham changes
are reported separately instead of being used to normalize away gate errors.

The five-spectator joint return measures a known coherent product state under
the calibrated inverse/readout model. It is stronger than testing five dark
populations. It still is not identity-channel certification on every unknown
spectator state or on arbitrary external references. The full MUB marginals,
including small coherences, are reported with their propagated intervals;
there is no unjustified 0.1-radian phase demand on a magnitude-0.2 coherence.

## 4. Phase and entangled-state witnesses

For the B preparation (|0>+|j>)/sqrt(2) of the target with basis control k,
write z=X+iY in the fixed analysis convention of the measurement protocol.
Let phi_ideal be its exactly specified relative phase: the G phase for the
gate arm, and the frozen ideal idle/sham phase for each control. Set

```text
Q = Re(exp(-i phi_ideal) z),
R = Im(exp(-i phi_ideal) z).
```

Apply the weighted bound directly to the two quadrature settings. The
sin/cos squared coefficients sum to one, so its sampling halfwidth is that
of one [-1,1] quadrature. No local phase is estimated from validation data
and subsequently removed. A calibrated physical endpoint phase correction
belongs in the frozen pulse word and has uncertainty of its own. Analysis-only
phase changes are a separate corrected-frame diagnostic, not primary PASS.

For k!=0, the residual mixed phase is the circular difference
`chi_kj=arg(exp(-i phi_kj)z_kj)-arg(exp(-i phi_0j)z_0j)`.
It cancels a target-local phase common to the control values. Propagate the
confidence rectangles, not only phase point estimates. The Q/R requirements
imply |arg residual|<=atan(0.20/0.75), hence |chi_kj|<0.522 radians.
The explicit mixed-phase limit is 0.55 radians. This is a redundant derived
check with the same uncertainty family, not an independent precision gain.
If a rectangle contains zero, its phase is unresolved. Spectator conditional
coherences and active-spectator signed products remain additional diagnostics,
not a complete classification of mixed many-ion phases.

For C, the target is `|psi_theta>=G(theta)|+_5,+_5>`.
The complete six-by-six product-MUB score uses

```text
w_ab = <psi_theta|(6 Pi_a-I) tensor (6 Pi_b-I)|psi_theta>.
F_hat = (1/36) sum_settings mean_shots(w_ab).
```

Flagged outcomes score zero with their original denominator. In the trusted
setting-independent preparation and measurement model this is an unnormalized
target overlap; the measurement document specifies the surviving code block.
With `lambda_max=(17+8 cos(theta))/25`, score bounds are
`1-12 lambda_max <= w <= 1+24 lambda_max`, including zero, so the score
range is 36 lambda_max, approximately 15.16. Pooling 36N bounded scores gives
a sampling halfwidth approximately 0.092 at the declared N and K, before
measurement-systematic uncertainty. This explains the moderate 0.60 target.

At either angle lambda_max is about 0.4211. A valid overlap lower bound above
it witnesses entanglement of the stated pair output; 0.60 does not certify
Schmidt rank five, whose overlap threshold is about 0.8553. It is an output-
state overlap, never a gate process fidelity. Idle/sham use their own known
product-output return score; comparing them with the G target would be wrong.

Martingale concentration alone does not turn 36 measurements of differently
prepared states into one density matrix. The witness requires analysis-choice
independence and an independently justified common prepared state or common
averaged-state model across the randomized settings. If a setting-dependent
preparation, analysis-correlated drift or unbounded POVM error remains, report
the raw campaign scores and mark the quantum witness INCONCLUSIVE. More shots
cannot repair this failure. No maximum-likelihood projection is used to make
an unphysical linear estimate appear to pass.

## 5. Motion, timing and drift boundaries

Each motion score is the raw outcome-1 indicator after the specified probe on
the independently frozen ion r_m in {4,5}, with nonzero resolved mode coupling.
Flags score zero. The areas are pi/4, pi/2 and pi in
the frozen blue-calibrated convention, using those same durations on red.
There is no pumping, recooling or reset between G and its probe. A00 zero-probe
rows diagnose internal-state confounding; their disagreement is retained.
The +/-0.10 criterion compares observed responses, not an inferred thermal
mean phonon number, a tail cutoff or a theorem that every mode closed.
Unresolved coupled modes make the stated complete motion screen INCONCLUSIVE.

Measure the protected interval from the start of hiding to the completion of
unhiding, all physical phase corrections and settling. The duration bound
includes pulse shaping, address changes and controller latency in that block.
The endpoint has physical phase corrections. A version corrected only by
changing the later measurement frame is a separately labelled diagnostic,
not a full PASS under this protected-endpoint contract.
Use recorded trigger traces plus a calibrated upper timing uncertainty, not
nominal pulse sums or an average that hides overruns. At the earlier reference
35 us/loop and 10 us/pi, 0.475 ms with pair echoes or 0.675 ms serial is only
a subtotal before compensation/overhead. The 1.0-ms limit is an explicit speed
target. Its failure can coexist with good coherence, but overall PASS requires
both. A trace fails only when its calibrated lower time bound exceeds 1.0 ms;
an interval straddling 1.0 ms is INCONCLUSIVE. Fifty-six such blocks alone
would permit up to 56 ms; this says nothing
about full-contact lifetime fidelity or its external operations.

Report predeclared first-half/second-half contrasts for the A00 pair return,
A00 joint spectator return and the lowest-frequency axial mode's blue
pi/2 response in every sign/arm (18 contrasts). Use the Fourier-analysis A00
row v=0 for both return anchors. The two fixed halves are the first 3000 and
last 3000 attempts in each chosen setting. The direct contrast weights are
+1/3000 for the latter and -1/3000 for the former; its binary sampling
halfwidth is approximately 0.0728, before systematic uncertainty.
Use the same simultaneous machinery and a +/-0.15 operational stability band.
An interval outside the band is a drift FAIL; one straddling it is INCONCLUSIVE.
These limited anchors cannot prove stationarity. All records and timestamps
remain in the campaign-average analysis; failing blocks are not removed.

Overall PASS means every required criterion, model prerequisite and drift
anchor passes for this finite diagnostic panel. FAIL identifies each
statistically established breach, including a duration breach. Otherwise the
outcome is INCONCLUSIVE. Publish raw scores, simultaneous intervals, systematic
budgets and all three dispositions. A passing panel authorizes no claim of a
complete seven-ion diamond bound, universal spectator identity, physical source
preservation for unknown quantum states, or a validated full 56-G contact.

[issue]: https://github.com/mathorn1973/twist-j/issues/1448
[H63]: https://doi.org/10.1080/01621459.1963.10500830
[A67]: https://www.jstage.jst.go.jp/article/tmj1949/19/3/19_3_357/_article/-char/en
