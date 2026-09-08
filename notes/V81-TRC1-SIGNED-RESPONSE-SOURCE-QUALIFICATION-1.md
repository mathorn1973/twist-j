# TRC1 paired signed response: bounded source qualification

**NON-CANONICAL / COMPLETED DOCUMENTATION AUDIT / SOURCE NOT QUALIFIED FOR THIS TEST**

```text
review date: 2026-09-08
basis_main: 67a7c03b7a4f37fb9d1d3e0f1150c0b87fc70960
authority: ACTIVE Public Canon v81
scientific owner: QDD-INSTRUMENT-APPARATUS [O]
scope: two named wave-response archives and one coherent-optical source lead
outcome-container access / new measurement / scientific execution: NONE
physical dictionary adoption / owner closure / Canon promotion: NONE
```

**Disposition:** no source inspected below qualifies for the paired first
signed TRC1 response test. The disposition is
`SOURCE_NOT_QUALIFIED_FOR_THIS_TEST` for these documented sources, not a
claim that no suitable archive exists anywhere, and not a physical falsifier.
The documents do provide useful signed-wave measurement information; they do
not supply the independently established preparation and dynamical mapping
needed to compare their measurements with the fixed rational prediction.

The companion [paired observation note](V81-TRC1-PAIRED-SIGNED-OBSERVATION-1.md)
owns the proposed observation equation. This note decides whether the named
public sources currently provide its inputs. It is not a new apparatus
proposal, a raw-data manifest, or permission to execute a measurement gate.

## 1. The precise target

The repository inputs are the [sealed TRC1 proof](https://github.com/mathorn1973/twist-j/blob/67a7c03b7a4f37fb9d1d3e0f1150c0b87fc70960/probes/P-TRC1-END-TO-END-IDENTIFIABILITY-1/PROOF.md),
sections 1, 4 and 6, and the [port observable calibration note](https://github.com/mathorn1973/twist-j/blob/67a7c03b7a4f37fb9d1d3e0f1150c0b87fc70960/notes/DECODER-PORT-OBSERVABLE-CALIBRATION-1.md).
They distinguish a conditional mathematical reading from an established
physical preparation or sensor dictionary.

For the marked sites
`((0,0,0),(1,1,0),(1,0,1),(0,1,1),(2,0,0))`, the two preparations are

```text
z0=e0, S(e0)=( 4,-1,-1,-1,-1)/5,
z1=e1, S(e1)=(-1, 4,-1,-1,-1)/5,
P_i=(0,S(e_i)).
```

With the same single cold origin port, `Gamma=g delta_origin`, `g>0`, the
first outgoing amplitudes and deposits satisfy

```text
b0 = -1421/[1620(2+g)],
b1 =   349/[1620(2+g)],
b1/b0 = -349/1421,
D1/D0 = 121801/2019241,     Di=g bi^2.
```

Here the subscripts distinguish preparations, not successive time steps.
Both responses refer to the same first transition. Two unrelated source
locations or two arbitrary basis vectors of a measured transfer matrix do not
become this pair by relabeling. A qualifying source must independently map
the physical initial states, relative amplitudes, marked port, cold condition,
discrete transition and observation cut to this target before comparison.

## 2. What was actually inspected

Primary literature and public catalogue/README surfaces were inspected.
Searches followed signed mechanical velocity, measured acoustic impulse
response and phase-resolved optical transfer measurements; they did not
select sources by numerical agreement with the target. No numerical response
arrays, raw traces, data-container previews or archive tails were opened.

| Candidate and exact surface | Inspected scope and custody limit |
|---|---|
| Open Guided Waves #4: [project catalogue](https://openguidedwaves.de/downloads/), [author article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8987639/), [Zenodo 5105861](https://zenodo.org/records/5105861) | Published method and indexed version 1.0 catalogue: Intact, FirstImpact and SecondImpact ZIPs remain unopened. Standalone Readme.txt was not retrievable. |
| dEchorate: [author article](https://link.springer.com/article/10.1186/s13636-021-00229-0), [author repository README](https://github.com/Chutlhu/dEchorate), [Zenodo 6576203](https://zenodo.org/records/6576203) | Sections 2.1-2.5 and version 2.0 HDF5 catalogue, listing RIR, silence and database files. No HDF5, pickle, CSV row or audio content was accessed. |
| Valzania-Gigan coherent optical transfer: [author preprint v1](https://arxiv.org/pdf/2210.04033v1), [author repository](https://github.com/comediaLKB/online_learning_TM) | Preprint sections II-IV and repository README. The repository describes simulation/reconstruction code. This establishes a primary experimental-method lead, not a verified signed archive inventory. The [Figshare 22012736 locator](https://doi.org/10.6084/m9.figshare.22012736) and [public metadata endpoint](https://api.figshare.com/v2/articles/22012736) were not retrievable; no claim about its container contents is made. |

The dEchorate README advertises a later refactoring and a temporary data
location; neither is silently substituted for the named archive. The source
qualification is versioned by the inspected documents and catalogue record.

## 3. Candidate findings

### Open Guided Waves #4: transverse velocity with a different preparation

The article documents one piezoelectric disk exciting a CFRP plate with an
omega stringer, using chirp or five-cycle Hann-windowed tone bursts. One laser
head records transverse velocity over a `483 x 483` grid; this is not a
three-component velocity measurement. Excitation is repeated and averaged at
each point. Generator settings and a factor-20 amplifier are specified, as is
an acquisition band-pass with cutoffs `0.5 fc` and `1.5 fc`. The three archive
scenarios change the specimen's damage state.
[Method, sections 1 and 2.3](https://pmc.ncbi.nlm.nih.gov/articles/PMC8987639/).

**Qualification inference:** the single-actuator protocol does not document
either five-site initial field above. Repeated velocity scans do not
certify `P=(0,S(e_i))`, a cold origin reservoir, the same `g`, or the first
discrete cut. Instrument filtering also cannot be treated as a common scalar
gain without a band/phase justification. This archive is
`SOURCE_NOT_QUALIFIED_FOR_THIS_TEST`; changing damage states is not an
admissible way to manufacture the required pair.

### dEchorate: useful polarity and timing, but no TRC1 source pair

The article documents six loudspeakers with sequential excitations, an
emission loop-back channel, and synchronous `48 kHz`, `32 bit/sample`
microphone acquisition. Microphone polarity was checked using a book clap;
gain was corrected using room tone. RIRs are estimated by swept-sine
deconvolution. For echo annotation, the authors display normalized
absolute echograms and equalize each RIR with its own isolated direct path.
[Method, sections 2.1-2.3](https://link.springer.com/article/10.1186/s13636-021-00229-0).

**Qualification inference:** those annotation products cannot preserve the
required signed relative amplitude. Original signed responses would be the
relevant surface, but the inspected documentation does not identify their
source preparations with the five-site `S` pair, microphone pressure with the
selected outgoing port coefficient, or room propagation with the first TRC1
transition. Same receiver electronics do not establish equal emitted source
amplitudes or a common directional-port gain. The inspected archive is
`SOURCE_NOT_QUALIFIED_FOR_THIS_TEST`; geometric calibration alone cannot fill
these gaps.

### Coherent optical transfer: phase is measurable, preparation is still unmatched

The author preprint describes phase-shifting digital holography recovering
complex output fields after a ZnO scattering layer. Input fields use a
phase-only SLM and a separate reference arm. The transmission experiment is
monochromatic at `808 nm`; the reflection experiment uses time-gated pulses.
Hadamard inputs are used for transfer-matrix estimation, and sample movement
introduces dynamics. [Experimental method and inputs, sections III-IV](https://arxiv.org/pdf/2210.04033v1).

**Qualification inference:** this supports the feasibility of phase-resolved
readout in a real apparatus, but no inspected source identifies those optical
inputs with `P_i=(0,S(e_i))`, the ZnO transfer with the TRC1 stencil, or an
optical gate with the first recurrence cut. A measured arbitrary complex
matrix cannot supply that identification by fitting two outputs. This lead
is `SOURCE_NOT_QUALIFIED_FOR_THIS_TEST` under its inspected method; its
unretrieved archive metadata is an additional, separate limitation.

## 4. Consequences for the observation equation

The observation contract requires four distinctions:

1. **Preparation and relative amplitude.** The coefficient vectors must be
   physically certified in the selected initial-state coordinates. Generator
   voltage, a source label or an SLM basis label alone is insufficient. Any
   independently measured relative scale `alpha1/alpha0` remains in the
   observation equation; it cannot be chosen to enforce the target ratio.
2. **Signed extraction and transfer.** Freeze offsets, receiver path,
   polarity, bandwidth, reference plane and a common linear extraction before
   comparison. For complex readout, one external phase convention must serve
   both preparations, retaining the orthogonal component as a diagnostic.
   Magnitudes, separately normalized traces and separate phase rotations do
   not preserve the signed target. Distinct gain/phase transfers remain
   explicit until their equality is independently established.
3. **Direction, context and cut.** A scalar velocity or pressure trace is not
   automatically the outgoing `b`. A continuous-frequency transfer or an
   acoustic arrival time is not automatically the first discrete transition.
   Common `g` and cold incoming state must be supported separately from the
   target outcomes. Reconstruction using the target `g` would be circular.
4. **Denominator and energy.** If calibrated uncertainty admits a zero first
   reference response, the ratio is unresolved. Neither clipping nor choosing
   a different peak repairs that. Squaring the measured signed ratio is a
   derived diagnostic; an independent energy comparison requires independent
   calibrated deposit measurements and retained relative source scales.

Virtual superposition of measured Green functions is a different proposal
unless an independent source/dynamics certificate proves it realizes these
initial fields with the same observation operator. Merely assigning the
coefficients of `S` to arbitrary loudspeaker or optical channels would encode
a chosen input array, not establish the requested TWIST-J physical reading.

## 5. Completed disposition and next action

The bounded audit is finished. None of these sources is admitted for target
outcome analysis, and no raw-data execution follows from this note. The exact
missing evidence is a target-independent same-apparatus preparation/transition
certificate for the two marked `S` fields, linked to calibrated signed
directional readout at the common first cut. No inspected source supplies
that conjunction.

Keep the companion observation equation as a reviewable conditional contract.
A subsequent concrete public source can reopen qualification only by supplying
that missing certificate and its measurement provenance. The present result
does not justify constructing a new apparatus, opening a generic click
archive, fitting an arbitrary transfer matrix, or declaring the physical
owner closed.
