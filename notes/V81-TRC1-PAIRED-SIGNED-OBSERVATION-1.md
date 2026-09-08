# TRC1: one observation equation for the paired first signed response

**NON-CANONICAL / CONDITIONAL PHYSICAL READOUT / NO QUALIFIED DATA OR NEW RUN**

```text
basis_main: 67a7c03b7a4f37fb9d1d3e0f1150c0b87fc70960
authority: ACTIVE Public Canon v81
definition lane: DECODER-PORT-OBSERVABLE-CALIBRATION-1, issue #830
scientific owner: QDD-INSTRUMENT-APPARATUS [O]
new physical measurement / formal probe / owner closure: NONE
```

This note selects one measurement: the signed outgoing directional velocity
coefficient for two fixed cold preparations at the same port and first cut.
It specializes the [existing port observation proposal](DECODER-PORT-OBSERVABLE-CALIBRATION-1.md),
not its alternative force/velocity identification route. The equation below
has an exact target. The [bounded source audit](V81-TRC1-SIGNED-RESPONSE-SOURCE-QUALIFICATION-1.md)
finds no qualified record among the inspected sources. Thus it is a concrete
conditional observation equation, not a completed physical identification.

## 1. The two initial states and the model target

The [sealed source implementation](../probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/transport.py)
defines, in the following order,

```text
sites = ((0,0,0),(1,1,0),(1,0,1),(0,1,1),(2,0,0)),
S(z) = (z0,z1,z2,z3,0) - (z0+z1+z2+z3)/5,
prepare(z) = Pair(0,S(z)).

z^(0) = (1,0,0,0),  S(z^(0)) = ( 4,-1,-1,-1,-1)/5,
z^(1) = (0,1,0,0),  S(z^(1)) = (-1, 4,-1,-1,-1)/5.
```

Both heads have the same model norm and scalar QDD weights; they have
different spatial fields. With one cold origin port
`Gamma=g delta_origin`, the same `g>0` and no earlier interaction,
[TRC1 proof section 4](../probes/P-TRC1-END-TO-END-IDENTIFIABILITY-1/PROOF.md)
gives the first-step row

```text
k = (1421,-349,-349,-349)/1620,
b(z) = -k z/(2+g),                 D(z) = g b(z)^2.

b(z^(0)) = -1421/[1620(2+g)],
b(z^(1)) =   349/[1620(2+g)],
b(z^(1))/b(z^(0)) = -349/1421,
D(z^(1))/D(z^(0)) = 121801/2019241.
```

These ratios are analytic consequences of the fixed model. The subscripts
below label the two preparations, not adjacent recurrence steps. The selected
test consumes the signed ratio; it needs neither a threshold `q` nor a
random law selecting heads. Separate preparation certificates do not assert
statistical independence of repeated experiments.

## 2. Exactly what the physical preparation certificate must identify

Choose a fixed physical initial-state coordinate map with five marked source
basis fields `Phi_r`. For a positive common displacement conversion `A0` and
independently known nonzero relative source factors `alpha_j`, its two initial
coordinate fields must be

```text
U_previous^(j) = 0,
U_current^(0) = A0 alpha_0 (4 Phi_0-Phi_1-Phi_2-Phi_3-Phi_4)/5,
U_current^(1) = A0 alpha_1 (-Phi_0+4 Phi_1-Phi_2-Phi_3-Phi_4)/5.
```

The desired equal-amplitude pair has `alpha_0=alpha_1`. Each `Phi_r` must
have its physical location, sign, shape and units supplied independently of
the two target responses. The preparation also identifies the previous/current
state meaning and the cold incoming condition `a=0`. A zero sensor baseline
alone establishes neither. Actual uncertainty in these certificates must
be propagated through the response; it is not erased by equal nominal settings.

The certificate must justify the same source-to-first-port transition, including
the stencil underlying `k`, under one apparatus context. A point actuator at
site 0 and then site 1 is not the displayed balanced pair. Likewise, assigning
these coefficients to arbitrary speaker channels does not identify their
physical fields with `S`. A postprocessed linear combination of archived
responses would require its own independently established source map,
linearity, phase and transfer calibration; it is not evidence that the two
stated initial fields were physically prepared.

No inspected archive presently supplies this certificate. Numerical `A0`,
physical basis fields, duration `tau` per transition and their uncertainties
are therefore not invented here. The ratio removes a common amplitude and
response scale; it does not remove the obligation to identify the states.

## 3. The selected signed observation equation

Use one fixed outgoing measurement path, reference plane, marked orientation
and observation band for both preparations. Let `y_j` be its raw signed trace,
`o_j` its independently calibrated baseline, and `H_j` its calibrated transfer
from outgoing velocity to trace units on that band. `H_j^{-1}` means the
specified band-limited reconstruction, with its uncertainty and any regularization
frozen by calibration. It is not inversion of the TRC1 response under test.
Physical separation of incoming/outgoing waves, including any reference
impedance used, is part of this independent calibration.

Let `ell_I` be the same fixed linear coefficient extraction at the certified
first cut `I`, with output in m/s. The observation equation is

```text
beta_hat_j = ell_I[H_j^(-1)(y_j-o_j)]
           = V0 alpha_j b(z^(j);g) + epsilon_j,
V0 = A0/tau > 0,                    j in {0,1}.

C_hat = 1421 beta_hat_1/alpha_1 + 349 beta_hat_0/alpha_0
      = 1421 epsilon_1/alpha_1 + 349 epsilon_0/alpha_0.
```

This fixes a directly evaluable linear contrast once the trace, calibration,
preparation and cut records exist. Its exact ideal value is zero. For equal
source factors the ideal ratio is `beta_1/beta_0=-349/1421`; it has opposite
signs in the two preparations. The contrast avoids division by the noisy
reference response, but still requires a certified nonzero response to give
a test of the ratio. Two zero signals passing the contrast are not confirmation.

`ell_I` is required to measure the model's first outgoing coefficient under
the preparation/transition certificate. Neither a digitizer sample, a largest
peak, an arrival time nor an arbitrary window average automatically has that
meaning. The same fixed physical cut includes trigger and delay corrections.
Any actual waveform shape and filtering used to justify this coefficient
must be documented before inspecting the pair's target response.

If the instrument returns a complex coefficient, apply one externally fixed
phase `phi` to both and use `Re(exp(-i phi) c_j)` as the signed coefficient.
Preserve `Im(exp(-i phi) c_j)` and its uncertainty as a compatibility diagnostic.
Rotating each response separately, taking magnitudes, or normalizing each
trace by its own peak would change this observable.

The outgoing trace is not reconstructed as `(F/Z-V)/2` using an unknown
`Z=Z0 g` being selected to explain these same data. The separation and
reference convention must be independently owned. A scalar displacement,
pressure or transverse-velocity trace without this identification does not
yet measure `b`.

## 4. What cancels and what remains observable

The common `g` cancels from the target. So do the common nonzero `V0` and
equal source amplitude. A common receiver gain or common polarity also
cancels, although the physical port orientation must still be defined. If
uncorrected relative gains `lambda_j` remain, the actual ideal trace ratio is

```text
-(349/1421) (lambda_1 alpha_1)/(lambda_0 alpha_0).
```

An unknown relative gain, polarity, source scale or transfer dispersion
therefore cannot be removed by quoting the rational target. Context changes
`g_0 != g_1` similarly leave a factor `(2+g_0)/(2+g_1)`. Equal context and
relative calibration must be established from separate records, not fitted
by requiring `C_hat=0`.

`epsilon=(epsilon_0,epsilon_1)` retains joint sensor, baseline, reconstruction,
timing, preparation, cold-leakage and transition-map uncertainties. Shared
references create dependence and must remain shared in the uncertainty set.
Before a future outcome comparison, freeze that calibration set and its
coverage rule. Check whether its image under the displayed contrast contains
zero; compatibility is not proof of the model. If the corresponding reference
amplitude set contains zero, report the ratio as unresolved. No numerical
tolerance, probability law or confidence level can be justified without the
actual calibration evidence, so this note is not a formal preregistration.

The energy ratio is a secondary model consequence. An experimental check
would require separately calibrated deposits and the same relative preparation
scale. Defining measured deposits as `g beta_hat_j^2` and then squaring the
signed ratio supplies no independent energy evidence.

## 5. Completed delivery and physical boundary

The signed coefficient extraction, paired source fields and null contrast are
now explicit. The accompanying bounded audit inspected Open Guided Waves #4,
dEchorate v2 and one coherent-optical measurement lead. None documents the
required pair of initial fields and common first TRC1 transition together with
the selected calibrated outgoing readout. Its disposition is
`SOURCE_NOT_QUALIFIED_FOR_THIS_TEST` for that inspected scope.

A physical test becomes concrete only with that missing linked evidence.
Agreement would test this preparation/readout/response link in its declared
range. It would not establish a Born occurrence law, physical preservation of
the old reservoir, completeness of the apparatus family, or uniqueness of J.
The merged two-exposure implementation is sufficient background for this
work and receives no additional capacity or exposure here. Original O/H
closures, new formal runs and new physical test results remain zero.
