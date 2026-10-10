# One selected calcium pair with five coherent spectators

**PUBLIC / NON-CANONICAL. Proposed experiment, not an executed result.**
Author: A. M. Thorn <thorn@twistj.com>. Date: 2026-10-10.
Reservation: [#1448](https://github.com/mathorn1973/twist-j/issues/1448).
Base: `6aae5de19bd2e04049b4d6893f18291e8465bf1a`, Public Canon v101.
Original text Apache-2.0. No scientific program or experiment was run.

## Decision to test

Test **physical ions 4 and 5**, the adjacent y,w pair used by the existing
contact compiler. Keep ions **1,2,3,6,7** coherently occupied throughout
the protected block. Test both target gates separately:

```text
theta = +4 pi/5 or -4 pi/5,
G_theta |j,k> = |j,k>                 if j=k,
G_theta |j,k> = exp(i theta)|j,k>     if j!=k.
```

The specific candidate is a static seven-ion chain with the existing broad
401-nm force geometry, **individually addressed 729-nm carrier pulses**,
and coherent five-D-level spectator shelving. This deliberately tests the
protection mechanism identified as incomplete in the [previous audit][prior].
It is an apparatus proposal; the cited two-ion experiment does not already
provide this seven-ion primitive.

The proposed outcome is one of PASS, FAIL or INCONCLUSIVE for the frozen
finite validation panel below. A pass means that this pair meets the stated
prototype criteria on these preparations and controls. It does not establish
identity on every unknown spectator input/reference, full-channel diamond
accuracy, a 56-G contact, or preservation of an informative quantum source.

## One trial, in laboratory order

1. Load and stabilize seven 40Ca+ ions; measure the actual mode spectrum,
   cool the relevant modes and optically pump into the declared |0> level.
   Finish all cooling and pumping before the coherent test state is prepared.
2. Prepare each spectator in a full five-level Fourier state
   `|Fq>=sum_j exp(2 pi i q j/5)|j>/sqrt(5)`, with
   `q=(0,1,2,3,4)` on ions `(1,2,3,6,7)`. Prepare the active pair in the
   basis, Ramsey or coherent-pair state specified by the measurement row.
3. Hide each spectator's |0> amplitude in the unused D5/2(+3/2) level with
   one phase-calibrated addressed pi pulse. Its other four D amplitudes stay
   occupied. This is a reversible coherent transfer, not pumping into a
   single dark state.
4. Apply five calibrated closed force segments. After each segment apply
   the four-pulse X5 cycle **only on ions 4 and 5**. This is 40 one-ion echo
   pulses, or 20 slots if the two ions can be driven simultaneously with
   the correct phases. Neither global echoes nor COM-only closure suffice.
5. Apply the actual inverse of each hiding pulse and the frozen local phase
   corrections. Count all physical correction and settling time within the
   protected block. There are ten elementary hiding/return pulses in total.
6. Apply the declared local analysis rotations to every ion before the first
   fluorescence exposure. Then destructively measure the seven-ion output,
   retaining leakage/invalid outcomes. Dedicated motion rows instead apply
   their sideband probe before fluorescence, with no intervening recooling.

[PULSES.md](PULSES.md) gives the rotation convention, exact preparation
angles, echo phases, both-sign force-calibration requirements and complete
timeline. The actual waveform samples, mode frequencies, Rabi rates and
laser powers must come from the apparatus and be frozen before validation.
The note supplies no invented calibrated waveform. Failure to obtain a
feasible closed-mode pulse for either sign is a failed prerequisite.

## Controls and measurements

Randomly interleave three arms separately for each sign, with matched block
duration: G (force plus echoes), E (same echoes, force blanked), and I
(hide, wait and unhide). Preparation and terminal analysis are shared.
Any arm-specific local phase correction is calibrated and frozen before
validation; no phase is refitted to make held-out data pass.
For each sign and arm, one protected pulse block and correction file is used
for every input and analysis row. Neither the gate nor its correction may
depend on the prepared active labels. Physical endpoint corrections are the
primary contract; analysis-only phase compensation earns at most a separately
labelled corrected-frame diagnostic.

| Measurement family, per sign and arm | Settings | Main question |
|---|---:|---|
| All 25 pair basis inputs, six spectator analysis bases | 150 | Population retention, all ten spectator coherences, dependence on active labels |
| Ramsey on levels 0,j for j=1,...,4, five partner labels, both orientations, two quadratures | 80 | Correct conditional phase and sign, not merely unchanged populations |
| Both active ions in F0, six-by-six local analysis bases | 36 | Entangled pair output without using an inverse entangling gate as the analyzer |
| Seven axial modes, red/blue sidebands, three fixed probe areas | 42 | Changes in a finite motional diagnostic panel |

The electronic panel therefore has 266 settings per sign and arm. The
42 motion rows are additional for the seven-axial-mode baseline. If other
modes are measurably coupled, include them before freezing the experiment
and update the resource count; they cannot be silently ignored.

For an active Ramsey input `(|0>+|j>)/sqrt(2)` with partner label k, the
ideal relative phase is `theta*(delta_(k,0)-delta_(k,j))`. Its nonzero rows
distinguish the right sign from the opposite sign and from no gate.
The raw two quadratures are compared to this fixed prediction without
normalizing away population loss. The simultaneous spectator outcomes
also test return to their known joint coherent input.
That return is required in the Fourier-analysis rows of the fully coherent
pair experiment too, so protection is tested while the pair becomes entangled.

The fluorescence sequence must distinguish code labels from leakage,
including the other S level and the auxiliary D level. In particular,
ordinary initial bright/dark detection would conflate code |0> with
another S state. [MEASUREMENT.md](MEASUREMENT.md) specifies a preliminary
0-to-auxiliary swap and first-bright classification to avoid that idealized
ambiguity, plus its required measurement calibration. Failed or invalid
outcomes remain in every denominator.

## Proposed prototype acceptance

These are **chosen engineering thresholds**, not values measured in a
published seven-ququint experiment. [ACCEPTANCE.md](ACCEPTANCE.md) defines
the exact rows, simultaneous confidence intervals, systematic allowances,
control comparisons and decision rules. Both signs must pass.

| Observable or resource | Proposed requirement |
|---|---|
| Active pair retains each prepared basis label | Lower bound at least 0.90 |
| Five spectators jointly return to their prepared coherent state | Lower bound at least 0.85; degradation against matched idle at most 0.10 |
| Any leakage/invalid flag | Upper bound at most 0.05 on the declared rows |
| Active Ramsey quadrature along expected phase | Lower bound Q at least 0.75 |
| Active Ramsey quadrature perpendicular to expected phase | Absolute upper bound on R at most 0.20 |
| Pair overlap with the specified entangled target | Lower bound at least 0.60, after measurement uncertainty |
| Each declared sideband diagnostic | Gate-minus-idle probability difference bounded in absolute value by 0.10 |
| Complete protected block | At most 1.0 ms including timing uncertainty, physical corrections and settling |

The overlap threshold concerns one prepared **output state**, not gate
process fidelity. Its ideal target has largest Schmidt weight about 0.4211;
a defensible overlap above that value witnesses entanglement. The 0.60
criterion does not demonstrate Schmidt rank five. All such statements need
the calibrated measurement and leakage model, not a normalized best-fit
density matrix that discarded bad shots.

The speed target is equally explicit: meeting 1 ms for one protected G does
not establish a whole-contact error budget. At the earlier illustrative
35-us force segments and 10-us pi pulses, its elementary block would take
0.475 ms with simultaneous echoes or 0.675 ms with serial echoes, before
additional waveform/compensation overhead. Those are conditional examples,
not a claim that seven-mode closure is achievable at those durations.

## Execution size and remaining prerequisites

The seven-mode baseline has 1848 settings including both signs and all
three arms. A tuning-only pilot of 200 shots per setting is distinct from
the proposed fresh validation run of 6000 shots per setting: **11,088,000
validation shots**. At a hypothetical 10 ms per full trial that is 30.8 h;
at 20 ms it is 61.6 h, before calibration and downtime. Actual readout and
cooling times determine the real cost. This is a multi-session measurement
campaign; the protected gate duration is a small part of a complete trial.
The pilot including motion totals 369,600 shots; it cannot earn a validation
pass or be pooled with the later validation data.

Calibration may tune waveforms and choose fixed compensations. Validation
must use new data, frozen pulse files, fixed analysis, randomized balanced
blocks and the declared stopping rule. Statistical intervals and measurement
uncertainty must fit inside each threshold for PASS. A threshold crossing in
the opposite direction is FAIL; an overlapping interval, missing calibration
or invalid inference model is INCONCLUSIVE, not a success rounded upward.

The final laboratory preregistration must identify the apparatus, calibrated
controls, sideband probes, detector model, randomization, data schema,
analysis implementation and exact hashes. This analytical design has not
executed or formally preregistered those missing device-specific inputs.
No change to Canon or the existing physical-admission gates follows.

[VALIDATION.md](VALIDATION.md) records analytical review and repository checks.

[prior]: ../C-U-CA40-PRACTICAL-FEASIBILITY-N/README.md
