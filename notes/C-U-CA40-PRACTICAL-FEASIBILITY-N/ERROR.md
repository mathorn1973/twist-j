# Noise, lifetime, and useful performance requirements

PUBLIC NON-CANONICAL engineering analysis; no new simulation or experiment.
Reservation: [#1446](https://github.com/mathorn1973/twist-j/issues/1446).
Branch: `codex/v101-ca40-practical-feasibility`.
Public base: `4699d2b651dda6cb17a71492a47e47e14831e969`.
Original text Apache-2.0. Date: 2026-10-10.
Rounded numerical illustrations below are analytic estimates, not executed
scientific data, measured contact fidelities, or frozen acceptance thresholds.
The coherent engineering criteria are delta_contact <= 0.10 or 0.01,
including leakage and spectator action. Separate 90%/99% no-fault indicators
are design illustrations, not conversions to those criteria or universal laws.

## 1. What is actually observed

The declared contact uses 56 ideal two-ququint G gates, plus local operations,
pair selection, spectator protection and any hiding/unhiding. The earlier
9758-pulse figure was a loose constructive ceiling, not a realistic compiled
pulse count. The tightened constructive bounds are N_R,out<=1496 local pulses
outside G, or <=1000 with phase-frame optimization, before spectator hiding.

| Primary source | Reported quantity | Its scope |
|---|---|---|
| Kreuter et al. [K05] | D5/2 natural lifetime 1.168(9) s | Single-ion lifetime measurement; not a seven-ion coherence time |
| Hrmo et al. [H23] | d=5 G performance estimate 93.7(3)% | Decay-fit estimate on two ions, with non-Markovian qualification |
| Ringbauer author manuscript [R22] | Ququint Clifford error 1.0(2)%; inferred pulse error 3.2(+0.8,-0.7) x 10^-4 | Local randomized benchmarking in that setup |
| Ringbauer author manuscript [R22] | Spin coherence scale about 100 ms with magnetic shielding | Transition/control-dependent capability, not a certificate for this contact |

Hrmo's author-PDF Table A1 reports independently measured noise parameters
and model-derived gate infidelities. These are different kinds of evidence:

| Noise input in that model | Input value | Simulated d=5 contribution |
|---|---:|---:|
| Motional heating | 15 phonons/s | 7 x 10^-4 |
| Motional coherence | 16 ms | 5 x 10^-3 |
| Initial mode occupation | 0.1 phonon | 1.3 x 10^-3 |
| Local operation frequency noise | 2 pi x 19 rad/s | 3.3 x 10^-2 |
| Elastic/inelastic scattering | Model of their beams | 3 x 10^-4 |
| D-state decay | 1 s model lifetime | 9 x 10^-4 |

The author-manuscript model total is 6.2 x 10^-2; slow local-frequency noise dominates
its d=5 result. These component values are not independent event probabilities.
They refer to the published sequence, not our addressed seven-ion sequence
at the required G angles +/-4 pi/5. The lifetime parameter in that model is also not
the more precise lifetime measurement used for the separate estimate below.

The G benchmark already includes its cyclic-echo local pulses and physical
noise during G. Adding their errors again would double count them.
The other experiment's pulse error is not automatically a calibrated value
for Hrmo's device, every local macro, or arbitrary occupied spectator levels.

## 2. Three incompatible meanings of a complete error estimate

**Observed:** measure the complete scheduled channel or declared input/output
task, including leakage, spectators and inherited motion. No such measurement
is supplied. Classical full-tuple truth-table success is weaker than coherent-
channel accuracy on unknown inputs and entangled references; a SUM scalar
alone is weaker still.

**Strict compositional bound:** let delta_j=(1/2)||E_j-U_j||_diamond for
compatible channels on the full retained system. For memoryless CPTP maps,
or a justified enlarged-state description retaining the memory,

```text
delta_contact <= sum_j delta_j
              <= 56 delta_G + N_R,out delta_R
                 + delta_hide + delta_idle + delta_other.
```

Every term must include the actual spectator action, and each physical
interval/noise contribution is counted once. A pair-only estimate with
spectators initialized to a special state does not bound its full extension.
Bath/motional memory cannot be discarded between factors merely to make this
formula applicable. Preparation/readout errors are added for a full experiment.
This telescoping bound is sufficient, usually loose, and is not inferred from
the reported decay-fit numbers. [WF14] explains the average/worst-case gap.

If r is a true average infidelity of a d-dimensional CPTP channel against
its unitary target, then
`(d+1)r/d <= delta <= min(1,sqrt(d(d+1)r))` [WF14, Proposition 9].
For d=25 and r=0.063 the generic upper bound is already trivial. Even a true
d=5 pulse r=0.00032 only gives an upper bound about 0.098. Reported fitted
figures need their own interpretation before this inequality may be applied.

**Independent-event illustration:** only after postulating independent
stochastic failures with per-operation probabilities p_j may one use

```text
P_no-fault = (1-p_G)^56 (1-p_R)^N_R,out
             * P_hide * P_idle * P_other.
```

It is not the general formula for circuit fidelity: faults may cancel,
coherently accumulate, or retain overlap with the target. Temporally correlated
noise violates the premise, as does treating a selected-state fit as p_G.
Use either aggregate G errors or a microscopic breakdown of G, never both.

## 3. Numerical engineering targets, explicitly conditional

The deliberately crude substitution `(0.937)^56` is about 0.026. It diagnoses
why simply chaining the reported primitive is unpromising; it is neither a
prediction nor an upper bound on actual contact fidelity. A real sequence
at different angles, with correlated errors, can depart in either direction.

For a target eta, allocating the entire independent-event budget to 56 G
gates gives `p_G <= 1-eta^(1/56)`. Allocating the whole strict diamond budget
gives `delta_G <= (1-eta)/56`. These are different metrics:

| Engineering target eta | Toy-model G success required | Strict delta_G ceiling if G uses all budget |
|---|---:|---:|
| 90% | 99.812% | 1.79 x 10^-3 |
| 99% | 99.9821% | 1.79 x 10^-4 |

External local pulses, storage, hiding, leakage and SPAM also consume budget,
so real G allocations must be tighter. Counterfactually assigning toy
p_R=0.00032 at the tightened constructive ceiling counts
gives local-only no-fault factors about 0.620 for N_R,out=1496, or 0.726 for
the 1000-pulse phase-frame variant. This transfers a number across devices
and control contexts solely for illustration. Hiding/unhiding needs its own
calibrated budget; that pulse probability is not inherited. With that probability,
the entire 90% local-only budget permits about 329 pulses; 99% permits about
31. These illustrate the value of reducing pulse count and error together.
They do not substitute Clifford infidelity for a measured pulse failure law.

## 4. D-state exposure is state-dependent, including hidden ions

Let P_D,i project onto all D5/2 levels of ion i, including hiding levels,
and N_D=sum_i P_D,i. Under the declared Markov spontaneous-emission model
with common rate Gamma=1/tau_D, the exact expected photon-jump count is

```text
E[N_jump] = Gamma integral_0^T Tr[rho_actual(t) N_D] dt.
```

This is not a no-jump probability. For the normalized state conditioned on
no jump, the exact survival law in the same unraveling is

```text
P_0(T) = exp[-Gamma integral_0^T Tr[rho_no-jump(t) N_D] dt].
```

The conditional and unconditional states generally differ. Replacing either
by the noiseless state is a weak-decay approximation, which we label
`mu_0=Gamma integral Tr[rho_ideal(t) N_D]dt`. To first order the jump
probability is mu_0. `exp(-mu_0)` is a useful hazard approximation, not an
exact identity or a theorem that contact fidelity equals no-jump probability.
Some jumps have nonzero overlap with a particular ideal output; no-jump
evolution can itself distort amplitudes. Basis inputs and quantum-channel
tests therefore do not share a universal lifetime-to-fidelity conversion.

For a maximally mixed ensemble on the seven direct S-plus-four-D codes,
ideal register-unitary control preserves average D population 4/5 per ion,
hence <N_D>=5.6. This also holds for the declared diagonal-force, closed-loop
skeleton between its local controls. It is an ensemble statement, not the
instantaneous D occupation of every input. Exporting entropy or using another
storage subspace changes its premise and must be included explicitly.

For that same maximally mixed ensemble, if two ions are active in that code
while five unknown spectators are
unitarily hidden in five D levels each, the loop-period average becomes
`2*(4/5)+5=6.6`. Hiding arbitrary quantum states is not pumping five ions
to one known dark label; such pumping would destroy their information.
Hiding/unhiding pulses add exposure, phases and errors of their own.
If q and r remain wholly in D throughout storage T, their combined hazard is
exactly 2 Gamma in this model, even for unknown entangled states. They contribute
a factor exp(-2 T/tau_D) to no-emission survival, not a process-fidelity bound.

Using tau_D=1.168 s, illustrative constant-population exposures are:

| Hypothetical elapsed exposure T | mu_0, direct 5.6 | mu_0, hidden 6.6 |
|---|---:|---:|
| 9.8 ms | 0.047 | 0.055 |
| 20 ms | 0.096 | 0.113 |
| 50 ms | 0.240 | 0.283 |

The 9.8 ms row is `280*35 microseconds`, only a reference force-pulse
subtotal. It assumes that loop setting remains usable at the required angles;
it omits carrier, switching and hiding time. It is not a measured contact
duration or a universal lower bound. The other rows are scenarios as well.

In the constant-hazard illustration, `exp(-mu_0)>=eta` gives exposure ceilings
about 22.0 ms/2.10 ms for 90%/99% with 5.6 occupied D levels, and
18.6 ms/1.78 ms with 6.6. These are emission-free budget diagnostics, not
strict channel-fidelity thresholds. They show why a many-millisecond pulse
sequence has little room for a 99% all-register target in this encoding.
Do not add this full exposure cost to an empirical G error that already
contains active-ion decay; use it in a resolved microscopic budget instead.

## 5. Coherence, motion and spectator errors require the actual schedule

A quoted T2 is insufficient for this multilevel circuit. Each coherence has
its own magnetic sensitivity and filter function. Slow common frequency
offsets can accumulate coherently; cyclic echoes may suppress some terms.
Neither `exp(-7T/T2)` nor independent per-pulse errors follows from a T2
measurement. Idle spectator coherences must be tested, not just populations.

For a spin-dependent force and thermal mode m, residual displacements give
the coherence factor between basis histories z,z'

```text
exp[-(1/2) sum_m (2 nbar_m+1)|alpha_m(z)-alpha_m(z')|^2],
```

apart from the intended and unwanted geometric phases. Closing only the COM
mode does not set every difference to zero. A seven-ion chain has many
collective modes; pair isolation must control all relevant residual motion
and unwanted pair/spectator phases. Mode-shaping methods have experimental
precedent on other trapped-ion qubit systems [M18], not a certificate for our
seven-ququint LS implementation.

Heating also acts between pulses. At the reference 15 phonons/s, 20 ms adds
about 0.3 phonon to an uncooled mode, but this alone is not a gate infidelity:
timing relative to the force trajectory matters. Recooling after every G is
not a free step and can disturb an unknown stored register. Emitted photons,
off-resonant scattering, differential D light shifts, phase drift and leakage
must remain in the same history; no fresh product environment may be assumed.

## 6. Practical disposition

The published d=5 performance does not support an evidence-based claim of a
90% or 99% complete 56-G contact on seven arbitrary ququints. The leading
identified limitations are technical control noise and depth, with lifetime,
motion and spectator protection becoming more restrictive as runtime grows.
This is an engineering assessment, not a mathematical impossibility theorem.

A useful next device milestone is a calibrated selected-pair G at both needed
angles while all five spectators hold arbitrary coherent test states, followed
by a compiled SUM with measured phases, leakage and inherited-mode behavior.
The complete contact then needs the actual compiled pulse word, a schedule-aware
noise budget, and full-sequence data in the chosen metric. Population-only
demonstrations must be labelled as a weaker classical-source experiment.

Substantially better control is physically plausible: a different Ca40 optical
qubit experiment achieved Bell-state infidelity 6(3) x 10^-4 in 35 microseconds
using 532 nm light [W21]. That does not transfer its number to a five-level G,
seven-ion pair isolation or this circuit. Optimized hardware/compiler work
must establish its own improvement; no extrapolated fidelity is certified here.

[K05]: https://www.quantumoptics.at/images/publications/papers/pra04_kreuter.pdf
[H23]: https://arxiv.org/pdf/2206.04104
[R22]: https://arxiv.org/html/2109.06903
[WF14]: https://arxiv.org/pdf/1404.6025
[M18]: https://arxiv.org/abs/1808.10462
[W21]: https://arxiv.org/abs/2105.05828
