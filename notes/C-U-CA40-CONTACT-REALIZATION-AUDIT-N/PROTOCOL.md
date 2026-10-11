# Preparation-to-readout protocol and the timing boundary

**PUBLIC / NON-CANONICAL / proposed audit protocol; no execution.**
Author: A. M. Thorn. Reservation: [#1444][claim]. Basis: Public Canon v101
at `408fc7a34cbd8113b4d5e1dac43793c7ad0270b0`.

## 1. Fixed carrier, source family and boundary

Use the CARRIER dictionary and its numbered seven-ion allocation; write
logical coordinates in the order `(x,u,y,w,q,r,s)`. Five ions participate
in the logical contact; q,r remain
part of the physical apparatus and require spectator protection. This
is a seven-ion proposal, not the two-ion device in the primary experiment.

At the ideal contact boundary, the required channel is `rho -> C rho C†`,
where C is the phase-free basis permutation in README. The interaction
picture, endpoint drift and any global program phase must be declared.
Physical equality includes a transformation back to the same specified
laboratory frame; changing frames cannot remove work or an unknown
source-dependent phase.

There are two distinct input contracts:

1. **Classical source:** an unknown member of the orthogonal family |s>,
   possibly a statistical mixture with classical side information. The
   protocol can retain the value s at its endpoint while transferring it.
2. **Coherent source:** arbitrary source density operators, possibly
   correlated with an external reference. The target is the complete joint
   C channel. Local source preservation is not required because the prior
   source theorem excludes that stronger informative-write contract.

Source preparation is independent of the receiver. A device that receives
an already unknown source may not pump it to |0> and call that preparation
of the same input. A classical preparation command or retained random seed
is an additional information-bearing system. A known coherent preparation
uses a phase reference; its availability and later state belong to the
apparatus. Source populations alone do not define its complete state.

The centered dictionary is an explicit choice: physical |u> represents
`p4-3`, and physical |w> represents `p4p-2`. A raw-coordinate dictionary
instead requires the chart conjugation K^-1 C K and the corresponding
physical energy relabeling. One must not calculate the pulses in the
centered dictionary and the energy in the raw one.

## 2. Ordered physical stages

| Stage | Proposed action | State/resource obligation |
|---|---|---|
| Calibration | Determine level frequencies, phases, addressed couplings, mode frequencies and light-shift profiles before data trials. | Retain calibration uncertainty, drift and dependence on seven-ion geometry. Do not fit only the desired SUM output. |
| Initial preparation | Cool motion, optically pump and prepare the declared source and receiver states using carrier rotations. | Account for emitted photons, remaining mode occupation, leakage, preparation command and phase reference. This is paid initial preparation. |
| Ready boundary | Establish the full seven-ion state and its permitted correlations with motion and apparatus. | A native occupied checkpoint must come from its actual preceding history; a directly prepared identical reduced checkpoint is only a stand-alone contact test. |
| Contact | Execute the complete compiled pulse sequence in its specified rotating frame. | All five active registers, q,r spectators, motion, controls and fields remain in the account. No readout/reset between compute and uncompute. |
| End of contact | Close the required motional excursions and restore temporary logical data. | Check leakage, residual displacements, spin-motion correlations, unwanted spectator phases and endpoint frame. Equal mean phonon occupation alone does not certify decorrelation. |
| Reading | On designated trials, rotate into the chosen measurement basis and perform fluorescence detection. | Include photons, detector electronics, record storage and measurement disturbance. These trials need not leave a reusable register. |
| Continuation | If demanded, run the separately specified native continuation with all inherited states retained. | An externally simulated counter/generator sequence must be labeled as such; it is not autonomous native U. |
| Renewal | Reset only the declared apparatus systems or perform a declared joint inverse. | List destroyed records, retained side information, emitted energy and entropy, and the new ready-state accuracy. |

This order supplies a reviewable experimental design. It does not imply
that a seven-ion device with these controls has been calibrated or run.
The two-ion cooling and entangling protocols are source precedents, not
measurements of this sequence. In particular a new motional vacuum cannot
be inserted before each gate or second contact without a physical reset.

## 3. Physical time is not the native counter

For a serial implementation with primitive pulse intervals I_l, define

```text
t_contact = sum_l duration(I_l) + t_switch + t_wait + t_transport,
t_cycle   = t_prepare + t_contact + t_read + t_reset + t_other.
```

Overlapped pulses require the actual union of scheduled intervals instead
of a serial sum. Carrier durations depend on transition-resolved Rabi
frequencies and rotation angles; closed-loop durations depend on the
chosen detunings and envelope. Phase updates still need a defined clock
and oscillator reference. COMPILATION gives conditional operation counts
and symbolic duration bounds, not a calibrated t_contact.

For an isolated driven emulator, the controller can reserve this entire
interval for C, compensate the physical free drift, and start the next
emulated native operation afterward. That is a legitimate proposed driven
experiment. Its clock, pause instruction, drift compensation and finite
native schedule are resources. It makes no claim that an unforced ion chain
follows U or that the native counter advances once per optical pulse.

For a continuously running native realization one would instead have to
establish, on the full included state and declared interval, the required
propagator under the **combined** native and contact Hamiltonians. Completed
map covariance alone is insufficient: intermediate Fourier transforms,
additions and cubic phases alter the very data used by the native selector.
The previous [chronology lane][chronology] already distinguishes completed
contacts from their interrupted factors. No commutation of our pulse
Hamiltonians with a physical native generator has been shown here.

The occupied-SUM theorem triggers C at one specified counter N>=4 and
then applies native continuation. To claim that experiment, one needs a
physical representation of that counter, its acquisition/trigger rule,
the accumulated first record and the inherited environment at N. Resetting
the counter, preparing a new receiver or stopping its physical evolution
changes the contract unless explicitly included in the driven emulator.
The [finite-controller result][controller] also prevents replacing the
literal unbounded counter by an exact finite reversible clock without
revisiting the complete-state recurrence requirements.

## 4. Discriminating tests and what they establish

The following predictions are analytic consequences of C, not recorded
outcomes, a frozen experimental preregistration or new computational data.
Before actual trials, freeze the device model, channel/error metric,
preparations, readout correction, sample plan and pass/failure thresholds.

| Preparation/test | Ideal prediction | Distinction tested |
|---|---|---|
| h=0, arbitrary s and targets | Identity contact. | Input-dependent coupling versus an unconditional target kick. |
| x=0, y=1, u=w=0, s=1 | u'=3, w'=2; other labels fixed. | Full contact outside the occupied SUM orbit; two optical target excitations. |
| Fixed h nonzero, all five basis s | Five distinct target pairs; each s unchanged at endpoint. | Classical source transfer, including s=0 as a value rather than absence. |
| Same receiver, source \|+> | Source marginal I/5; joint state remains pure in the ideal model. | Population retention versus loss of local source coherence. |
| Phase-sensitive source and joint measurements | The source X expectation changes from 1 to 0 in the preceding test; joint coherence is present. | Dephasing in the reduced source versus irreversible destruction of the joint information. |
| Apply the complete joint inverse | Original source and receiver restored, new record removed. | Reversibility under the same admitted resources. |
| q,r in superpositions or correlated test states | Their complete operator algebra is unchanged by ideal C. | Spectator protection beyond matching basis populations. |

Here `|+>=sum_s|s>/sqrt(5)` and `X|s>=|s+1>`. Estimating its real and
imaginary parts requires phase-sensitive measurement, not only population
histograms. Comparing independent preparations measures an ensemble; it
does not observe the before/after quantum state nondestructively in one run.
An external entangled-reference test would require an additional physical
reference and its own controls; it is not hidden inside the seven-ion count.

Checking a computational truth table cannot certify relative phases or
the complete quantum channel. Likewise published randomized-benchmarking
averages cannot simply be multiplied across this contact and treated as a
worst-case guarantee. With compatible per-primitive channel bounds in a
submultiplicative channel norm, a telescoping argument bounds the complete
error by the sum of those bounds, including spectator and motion errors.
Such compatible calibrated bounds are not provided for this device.

To certify a second contact, repeat the analysis using the **inherited**
occupied register and environment, not fresh product preparations. The
existing ideal LS loop's mode-independence, when its stated conditions hold,
is useful but does not calibrate other modes, noise or prior correlations.
Cooling, optical pumping and fluorescence may disturb both the archive and
source, so their placement must be explicit in that full history.

## 5. Admission decision

The carrier choice, physical level dictionary, conditional gate synthesis,
finite scheduling requirements and energy/work balances are supplied.
The following device-specific evidence remains absent:

- Seven-ion pair isolation/addressing and full spectator protection.
- Calibrated light-shift profiles, all relevant modes, complete pulse
  waveforms and laboratory-frame compensation for this C.
- Source/receiver preparation, leakage and inherited-history error bounds.
- A controller/clock and native-dynamics bridge for a claim beyond a driven
  stand-alone contact experiment.
- Measured energy flows and work over the declared preparation/contact/
  readout/renewal cycle, including coupling energy and control backaction.

Thus **candidate selected; driven compilation conditional; physical
certificate NOT PROVIDED**. This conclusion records the precise engineering
and physical boundary. It is not an impossibility theorem for approximate
ion control, nor completion of the canonical apparatus owners or gates.

[claim]: https://github.com/mathorn1973/twist-j/issues/1444
[chronology]: https://github.com/mathorn1973/twist-j/pull/1428
[controller]: ../C-U-FINITE-REVERSIBLE-CONTROLLER-RECURRENCE-N/README.md
