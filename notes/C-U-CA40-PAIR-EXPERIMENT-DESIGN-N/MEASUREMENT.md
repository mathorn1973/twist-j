# Phase-sensitive measurement plan for one selected Ca40 pair

This is an analytical, non-canonical experimental design in reserved issue
[#1448](https://github.com/mathorn1973/twist-j/issues/1448), based on public main
`6aae5de19bd2e04049b4d6893f18291e8465bf1a`. No experiment, simulation, pulse
search, scientific verifier, or data analysis has been executed for this note.
The pulse route is [PULSES.md](PULSES.md); thresholds and statistical decisions
belong to [ACCEPTANCE.md](ACCEPTANCE.md). Setting counts below are design counts,
not observations. The common problem, phase convention, and panel were shared
within the same assistant team; this is not an independent experimental result.

## 1. Target, preparation, and the finite scope

The active ions are `(A,B)=(4,5)`; spectators are `S=(1,2,3,6,7)`.
For both signs separately, the target is

```text
theta = +4 pi/5 or -4 pi/5,
G_theta |j,k> = exp(i theta [j != k]) |j,k>,  j,k in F5.
```

The code is the stated `S_{1/2},m=-1/2` level 0 and four specified `D_{5/2}`
levels 1--4. Use the physical level map in PULSES.md throughout. The unused
`a=D_{5/2},m=+3/2` level is the hiding/readout auxiliary, not a sixth code level.
Before every validation contact, prepare the five spectators in the fixed state

```text
|Phi_S> = tensor_i F|q_i>,  (q_1,q_2,q_3,q_6,q_7)=(0,1,2,3,4),
F|q> = 5^(-1/2) sum_j omega^(q j)|j>,  omega=exp(2 pi i/5).
```

Each spectator has all five amplitudes and all ten off-diagonal coherences:
`rho_jl=omega^(q_i(j-l))/5`. This is one fixed product-state context, not five
independent spectator contexts or a test on arbitrary spectator/reference
states. Spectators remain coherent through every main acceptance contact.
Preparation errors are calibrated separately; preparation is not inferred from
the gate data. No spectator is initialized into a blank logical state to hide
its possible interaction with the selected pair.

For each sign use three frozen arms: gate, time-matched idle, and the explicit
sham sequence in PULSES.md. Match preparation, analysis, total hold time, and
readout. The sham is a diagnostic physical sequence, not an assumed ideal
identity channel. Randomize/interleave a fixed setting schedule and retain
timestamps; never tune phases on the locked validation sample.
The primary target includes the physical endpoint phase-correction pulses in
PULSES.md and their duration/error costs. Absorbing an unwanted physical phase
only into the analysis basis gives a separately labeled corrected-frame
diagnostic, not a pass for the same physical endpoint output.

## 2. Six local analysis bases

Freeze the ordered basis list `B=(infinity,0,1,2,3,4)`. Infinity denotes the
computational basis. For `b=0,...,4` use

```text
|b,k> = 5^(-1/2) sum_j omega^(b j^2 + k j)|j>, k=0,...,4,
W_b = diag_j(omega^(b j^2)) F,
analysis W_b^dagger = F^dagger diag_j(omega^(-b j^2)).
```

The quadratic Gauss sum gives overlap squared `1/5` between distinct bases;
these six bases are informationally complete for one ququint. The prime-power
MUB construction has a primary precedent in
[Wootters and Fields (1989)](https://doi.org/10.1016/0003-4916(89)90322-9).
All local analysis rotations on all seven ions finish before any fluorescence.
They use independently calibrated, phase-tracked local rotations, not an
inverse of the entangling gate under test.

For a subnormalized code-block state `sigma`, with `t=Tr(sigma)`, the ideal
analysis identity is `sigma=sum_(b,k) p_bk |b,k><b,k| - t I`.
Use original trial denominators, including flagged trials. When counting only
events with all seven code labels valid, this reconstructs the corresponding
unnormalized projected marginal, without conditioning on survival. A quantum
interpretation requires a common setting-independent preparation/channel and
the calibrated POVMs; otherwise report the operational scores only.

## 3. Fixed internal-state panel: 266 settings per sign and arm

| Block | Preparation on A,B | Analysis | Settings |
|---|---|---|---:|
| A | Every `(a,b)` in `F5^2` | A,B computational; all spectators in common basis `v in B` | `25*6=150` |
| B | Target `(0+j)/sqrt(2)`, control `k` | Both orientations, `j=1..4`, `k=0..4`, target X or Y; control computational; spectators Fourier | `2*4*5*2=80` |
| C | `\|+5,+5>` | All `v,w in B` on A,B; all spectators in basis `v` | `6*6=36` |

Here `|+5>=F|0>`. The table completely enumerates the panel; there is no
adaptive selection of favorable states or phases. Two signs times three arms
give `1596` internal-state settings. With 6000 validation shots per setting this
is `9,576,000` attempted shots; a separate 200-shot pilot has `319,200` shots.
The pilot is for tuning only and is excluded from validation inference.

### A. Populations, every spectator coherence, and context dependence

Record all seven outcomes jointly on each trial. Computational populations
alone cannot distinguish this diagonal gate from identity. Their role is to
test the expected active output `(a,b)`, leakage flags, and readout consistency.
The six spectator bases reconstruct each spectator's entire code-block marginal
for every active basis input, including all ten complex coherences. Explicitly
compare their phases and magnitudes with the fixed `F|q_i>` target across the
25 active contexts. This exposes, within the panel, active-state-dependent
spectator phases that a single average return probability could hide.

In the Fourier setting, record the simultaneous five-spectator return event
`all spectator labels equal q_i`, as well as each return separately. Store its
joint occurrence with correct/incorrect active labels and leakage flags. Do not
infer seven-body factorization from good one-ion marginals. Settings in A with
input `00` also provide the no-sideband-probe electronic-population baseline
for the separate motion diagnostic.

### B. Signed conditional Ramsey phases

For target pair `(0,j)` define

```text
X_0j=|0><j|+|j><0|,
Y_0j=-i|0><j|+i|j><0|.
```

Measure X in eigenvectors `(0 +/- j)/sqrt(2)` and Y in
`(0 +/- i j)/sqrt(2)`, extending each analysis by identity on the other three
levels. Freeze which physical output labels represent eigenvalues +1 and -1.
Prepare `(0+j)/sqrt(2)` with control `k`. The relative output phase is

```text
phi(theta,j,k)=theta(delta_(0,k)-delta_(j,k)),
z=<X_0j>+i<Y_0j>=exp(i phi),
Q=Re(exp(-i phi) z), R=Im(exp(-i phi) z).
```

Thus the expected phase is `+theta` for `k=0`, `-theta` for `k=j`, and zero
otherwise. Both quadratures distinguish the two signs and reject identity in
the nonzero-phase contexts. Repeating both orientations and all control labels
distinguishes the intended conditional phase from a simple one-ion phase.

The raw X/Y score is +1 or -1 for the specified target eigen-outcome, intended
control label `k`, and seven valid code labels; otherwise it is zero. It is an
unnormalized projected-control coherence, not a postselected Ramsey fringe.
Also retain signed products of that score with each spectator Fourier-return
indicator and with their joint return. Their differences from the corresponding
marginal products diagnose observed active-spectator correlations; they do not
prove absence of all correlations or source/reference disturbance. Idle and
sham comparisons have their own frozen expected phases; do not rotate away
observed gate phase errors by fitting a new phase to the same validation data.
These extra signed-product diagnostics are exploratory raw summaries, not
additional simultaneous acceptance claims in the enumerated interval family.

### C. One entangled output with local analysis only

The target on the pair is
`|psi_theta>=5^(-1) sum_(j,k) exp(i theta[j!=k]) |j,k>`.
For each of the 36 product-MUB settings, record the 25 pair outcomes jointly
with the five spectator outcomes. The overlap with this target is estimated
linearly, without maximum-likelihood reconstruction or an inverse gate.
In the six C rows with `v=0` and arbitrary `w`, the five-spectator joint Fourier
return is also a required acceptance score: lower bound at least `0.85` and
gate-minus-idle lower bound at least `-0.10`, using the existing shots.
For ideal local projectors `Pi_a,Pi_b`, freeze the score

```text
w_ab=Tr[|psi><psi| (6 Pi_a-I) tensor (6 Pi_b-I)]
    =36 |<a,b|psi>|^2 -6 <a|rho_A|a> -6 <b|rho_B|b> +1.
```

Set the score to zero on any flagged trial. Average the sample means equally
over all 36 settings. The local MUB frame identity makes its expectation
`F_psi=<psi|sigma_AB|psi>` for the subnormalized all-code block. Do not divide
by a measured survival probability. All weights are specified by the analytic
formula before validation, not fitted to the resulting data.

The squared Schmidt coefficients of the target are

```text
lambda_0=(17+8 cos(theta))/25,       approximately 0.4211,
lambda_1=...=lambda_4=(2-2 cos(theta))/25, approximately 0.1447.
```

For either sign, `lambda_0` is largest. Since product overlap is at most
`lambda_0` and each marginal probability is at least that product overlap,
`1-12 lambda_0 <= w <= 1+24 lambda_0`; score width is `36 lambda_0`.
A SPAM-bounded lower confidence bound above `lambda_0` witnesses entanglement.
A bound above `lambda_0+3 lambda_1` (approximately `0.8553`) would witness
Schmidt number five, but this stronger claim is not required by this design.
The proposed overlap threshold `0.60` is an output-state criterion, never a
process fidelity, diamond-distance bound, or an arbitrary-input gate guarantee.

[Hofmann's complementary-basis bound](https://arxiv.org/abs/quant-ph/0409083)
uses correct ideal-output overlaps for two complete mutually unbiased input
bases. Here the Fourier-product inputs generally have entangled ideal outputs;
their computational truth table is not the required complementary fidelity.
The present one-input witness therefore makes no Hofmann process-bound claim.

## 4. Joint destructive readout with explicit leakage flags

The design adapts the sequential shelving/readout principle demonstrated by
[Ringbauer et al.](https://ar5iv.labs.arxiv.org/html/2109.06903), whose local
Givens rotations also support these analysis bases. Their reported qutrit
readout performance is not a calibration of this seven-ion ququint protocol.
Fluorescence initially distinguishes S from D, not the two S Zeeman levels.
Calling every initial bright ion code 0 would hide `S,+1/2` leakage.

After all analysis rotations, use this six-round classifier:

1. Swap code 0 with auxiliary `a=D,+3/2` on each ion. Intended code 0 is now
   parked in a; population already in a is transferred to S and is leakage.
2. Initial fluorescence: any bright ion receives flag L, including leaked
   `S,+1/2` population. Intended code population is dark in this round.
3. Sequentially transfer D code levels 1,2,3,4 to `S,-1/2`, with fluorescence
   after each transfer. For an unresolved ion, first brightness assigns the
   corresponding code label. Already classified ions retain their first label.
4. Transfer a to `S,-1/2`; first brightness here assigns code label 0.
5. Never-bright, lost, or ambiguous histories receive L. In particular unused
   `D,+5/2` population is not silently merged with a valid code outcome.

Later brightness on an already classified ion is expected and does not itself
invalidate its earlier first-bright label. Store per-ion photon counts and
timestamps in every round, classifier version, and the seven-label vector from
the same trial. Separate one-ion ensembles cannot replace the joint outcomes.
No hiding failure, L event, or lost ion is removed from the attempted-shot
denominator. L is an observed flag, not an assumption that every physical leak
is detected; missed leakage and false labels need independently bounded bias.

Independently calibrate code inputs, both unused D inputs and the other S input,
analysis-induced code/leak mapping, state-transfer errors, fluorescence
confusion, decay during all six rounds, and spectator-dependent crosstalk.
Scattering by bright ions heats the chain; inter-round recooling and subsequent
transfer errors require a measured schedule and error budget. Such recooling
is after the measured gate/probe, not a permissible pre-probe motion reset.
The readout destroys the tested state; it does not certify subsequent native
continuation. The experimental POVM and preparation bounds must cover every
analysis context, not merely a convenient computational calibration table.
In particular, a classical basis-confusion matrix alone cannot bound coherent
MUB or entanglement-witness bias. Require trusted analysis/POVM bounds including
correlated seven-ion detection and crosstalk; do not infer a five-spectator
joint-return error by assuming independent one-ion readout noise.

## 5. Motion panel without erasing the motion under test

Add 42 settings per sign and arm: seven axial modes `m=1,...,7`, red and blue
resolved sideband, and three probe areas. Prepare active `|00>` and the same
coherent spectator product state. After the gate/idle/sham, apply the sideband
probe directly, with no optical pumping, recooling, projective reset, or
unrecorded waiting operation between the tested sequence and that probe.

For each mode freeze a probe ion `r_m` in `{4,5}` with a resolved, calibrated
nonzero `0<->1` sideband coupling. Ion 4 alone is not automatically adequate:
a middle ion can be at a normal-mode node. Freeze its blue ground-state Rabi
rate `Omega_(m,blue,0)` and durations `t=beta/Omega_(m,blue,0)` for
`beta in {pi/4,pi/2,pi}`. Use these same durations on the red sideband; do not
silently replace them with a thermal-model-dependent effective pi pulse.
If a mode is inaccessible to both active ions or cannot be resolved, the stated
seven-mode contract is incomplete, not passed by omitting that mode.

Analyze the active ions computationally and the spectators in the Fourier
basis. The raw event is `probe-ion outcome=1 and all seven code labels valid`;
any flagged trial scores zero, with flag rates also reported separately.
Compare gate and matched-idle probabilities for every fixed setting, using the
operational tolerance in ACCEPTANCE.md. The A-input-00 baseline identifies
electronic population errors that can otherwise mimic sideband excitation.
No population correction is silently fitted or subtracted from the same data.

Seven modes times two sidebands times three areas times two signs times three
arms gives 252 additional settings. Grand totals are 1848 settings,
11,088,000 validation attempts at 6000 each, and 369,600 separate pilot attempts
at 200 each, excluding calibration trials. Relevant radial couplings require
an expanded preregistered mode list and budget; this axial panel cannot certify
their closure. Preparation, detection, recooling, and calibration time are
additional to the gate duration, so this is a substantial laboratory campaign.

A thermal sideband fit needs a justified motional-state and electronic-state
model. The selected operational probability comparison is not an exact mean
phonon-number bound or a universal phase-space-closure certificate. Even equal
mean energy need not imply zero branch-dependent displacement. For a thermal
mode a displacement difference Delta alpha suppresses branch coherence by
`exp[-(nbar+1/2)|Delta alpha|^2]`; multiple modes multiply these factors.
Ramsey/coherence and motion diagnostics constrain different failure signatures,
without replacing a calibrated multimode closure analysis.

## 6. What an accepted panel establishes

Freeze pulse programs, all settings, phase frames, classifiers, calibrations,
shot counts, and rejection rules before fresh validation. ACCEPTANCE.md assigns
simultaneous intervals and explicit systematic/SPAM bias allowances. Missing
calibration or a setting-dependent measurement model gives INCONCLUSIVE for
the corresponding quantum claim, even when a raw score looks favorable.
The evidence would concern both signed selected-pair operations for these
finite contexts and this hardware schedule. It would not establish spectator
identity on arbitrary states, a full seven-ion channel norm, the complete
56-gate contact, a source-restoration theorem, autonomous timing, or physical
admission of the TWIST-J contact.
