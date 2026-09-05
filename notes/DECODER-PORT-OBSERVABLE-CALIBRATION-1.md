# Decoder port observable and calibration 1

**NON-CANONICAL / PROPOSED MECHANICAL PORT / STOP-DEFINITION / NO PHYSICAL DATA**

This is the next specification for the unresolved signed-port observable in
[reservoir profile RRP1](DECODER-RESERVOIR-PHYSICAL-PROFILE-1.md).
It selects force and velocity as one proposed physical interpretation, defines
the calibration needed to identify the port response, and exposes where that
identification can become circular. It supplies neither a realized apparatus
nor a physical test result. The accompanying
[template](DECODER-PORT-OBSERVABLE-CALIBRATION-1.template.json) is deliberately
incomplete and is not executable.

```text
definition lane: DECODER-PORT-OBSERVABLE-CALIBRATION-1, issue #830
basis_main: 60f7649747fd5dba4279ae8f840da3b0f3ae9729
authority: ACTIVE Public Canon v76
canon_content: 07910adb8418742bf52a0d204577b84b38009b18
canon_sha256: c151a19997dba95d78836c46f38463ab2735ae1c98674f87888d519d7a500112
canon_bytes: 420539
new scientific probe / execution / physical measurement: NONE
physical dictionary adoption / scientific status move: NONE
```

The scientific owner is the registry row `QDD-INSTRUMENT-APPARATUS [O]`.
Issue #539 is its shared definition surface, not the registry claim itself.
Neither is discharged by this note. The RRP1 reset mismatch and unimplemented
wrapper remain. Source, context, complete family, occurrence and the named
L1-to-L5 bridge are still required separately.

## 1. The inherited port and a selected dimensional interpretation

The fixed input is the [general coupling contract](../probes/P-DECODER-RESERVOIR-COUPLING-1/CONTRACT.md),
source pin `550420d188a45c4929e300ca6aabcde812f4d65a`.
For one port with dimensionless rational coefficient `g>0`,

```text
p=(w-u)/2=a-b,
f=g(2a-p)=g(a+b),
p f=g(a^2-b^2).
```

The global wave budget is `Delta E=sum_x p_x f_x`; it is `p f` only when
this is the sole active port. A local wave-energy density also has transport
terms. The [quadratic partition result](../probes/P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1/RESULT.md)
does not identify these amplitudes with physical observations.

Select three positive, fixed conversion quantities, all physically unresolved:

| Symbol | Proposed meaning | SI dimension |
|---|---|---|
| `A0` | Wave-coordinate displacement scale | m |
| `tau` | Duration assigned to one coupled transition | s |
| `E_star` | Conversion of dimensionless wave/port energy | J |

`E_star` is a constant scale, not the state energy `E(u,v)`. `A0` is a field
amplitude scale, not the spatial lattice spacing. Define

```text
V0=A0/tau, F0=E_star/A0,
Z0=F0/V0=E_star*tau/A0^2,
Z=Z0*g,
V=V0*p, F=F0*f, v_plus=V0*a, v_minus=V0*b.
```

Here `V` proposes a signed mechanical velocity and `F` the force exerted
by the port on the wave subsystem; both use one marked positive direction.
`v_minus` is an outgoing amplitude in this convention, not an independently
chosen outward coordinate orientation. `Z` has units N s/m, and the word
conductance in the rational model is not an electrical SI identification.
The selected map gives

```text
V=v_plus-v_minus,
F=Z(v_plus+v_minus),
tau*F*V=E_star*g(a^2-b^2).
```

In the cold specialization `a=0`, force opposes motion: `F=-Z V`.
These are dimensional identities under a chosen map. They are not a proof
that a mechanical object realizes the discrete wave dynamics. The effective
mass scale `M0=E_star*tau^2/A0^2` is likewise only a conversion quantity;
it is not identified with the electron mass by definition.

No numerical `A0`, `tau`, `E_star` or `Z` is supplied. A laboratory calibration
can characterize an apparatus context. It does not derive additional
universal dimensionless parameters or complete the Canon's single-electron-mass
SI bridge. `METRO-TICK` is dimensionless and does not by itself provide `tau`
in seconds. A named physical dictionary and admissibility ruling must distinguish
apparatus settings from new theory inputs before adoption.

## 2. What must actually be observed

Choose one reference plane, coordinate orientation and declared observation
band. Preserve the full raw traces, instrument settings, clock readings and
invalid/saturated samples. Derived records must point back to those bytes.
No target-dependent filtering or phase choice is allowed.

| Record | Required independently owned content |
|---|---|
| Force trace | Sensor transfer, polarity, offset, dynamic range, loading, bandwidth and uncertainty; force on the wave side, not its reaction without a sign change. |
| Motion trace | Displacement or velocity measurand, transfer, polarity, timing and uncertainty; a differentiation/filter rule if velocity is derived. |
| Directional port traces | A physical separation of incoming/outgoing amplitudes, its reference impedance and calibration; the names a/b alone supply no such measurement. |
| Source/ready record | Actual preparation, cold incoming condition or warm pulse, reference plane and initial wave state, with an independent certificate. |
| Time/cut record | Common trigger, delay corrections, sample-to-coefficient map, interval endpoints and assignment to RRP1/U labels. |
| Work/energy record | Independently calibrated force-motion work and, where claimed, reservoir or wave-energy measurement with response delay and loss accounting. |

Force/motion observations and independently separated directional amplitudes
are different observation routes, not automatically four independent sensors.
Any reuse of sensors or calibration standards must be recorded with its joint
uncertainty. Mechanical loading, reflected pulses and the energy exchanged by
a measuring device belong to the declared apparatus boundary.

A zero electronics baseline only calibrates an offset. It proves neither
`(u,v)=(0,0)` nor cold `a=0`. A warm incident pulse is a diagnostic outside
RRP1's cold operational domain. It is not a new runtime input to U. The mapping
from the physical preparation and context to an admitted pointed source
remains an independent decoder obligation.

## 3. Three separate calibration stages

**Stage S: sensors and readout.** Before using the tested port law, establish
the two channels' offsets, relative gain, relative polarity, response and time
alignment using independent references. A possible laboratory procedure applies
a separately certified common signed signal in both polarities through the
declared measurement paths, checks zero and several amplitudes, and characterizes
the acquisition transfer on the chosen band. It is only a proposed procedure:
actual instruments, reference certificates and bounds are absent. A route that
cannot deliver the same reference to both paths needs its own traceable transfer.
Channel swapping alone does not establish an absolute reference or justify
equating two unknown path responses.

For a predeclared coefficient extraction with certified scalar response,

```text
y_a=o_a+k_a*a+eta_a,
y_b=o_b+k_b*b+eta_b,
rho=(y_b-o_b)/(y_a-o_a), kappa=k_b/k_a.
```

In the noiseless special case, `rho=kappa*r`, where `r=b/a`. A single scalar
gain is not silently used for dispersive signals. If the actual transfer is
frequency-dependent, the frozen extraction must incorporate the independently
calibrated transfer operator and its error, or the scalar route stays STOP.

**Stage I: constitutive identification.** With Stage S frozen, use designated
identification preparations to determine a context's admissible parameter set.
The source/cut/ready certificates and conversion map must already be explicit.
The declared model response cannot calibrate the channels that will test it.

**Stage V: independent validation.** Freeze the identified parameter set and
readout before acquiring or opening the designated validation records. Use
different preparation records and predeclared amplitudes or source vectors.
Their calibration references may be shared only with the dependence recorded;
the identification and validation data themselves must be disjoint. No refit,
sign flip, branch choice, window shift or threshold change follows validation.
Without an identified apparatus and a preregistration this remains a proposed
design, not an experiment ready to run.

## 4. What is and is not identifiable

For a diagnostic zero wave pair and a single nonzero incoming coefficient
`a=A`, the inherited equations give

```text
w=4g*A/(2+g), b=(2-g)*A/(2+g),
r=b/A=(2-g)/(2+g),
g=2(1-r)/(1+r), -1<r<1.
```

Thus an independently calibrated signed ratio identifies `g` conditionally on
that preparation and response model. It does not validate the model by itself.
Unknown positive `kappa` leaves a continuum of `g` values; known polarity only
distinguishes `g<2` from `g>2` away from zero. Unknown relative polarity reverses
`r`, and

```text
r(4/g)=-r(g).
```

It therefore restores exactly the reciprocal ambiguity. A common nonzero gain
and common polarity applied to both ideal channels cancel in the ratio; an
unknown relative gain or polarity does not. At `r=0`, `g=2` is regular.

There is an additional circularity test. If one constructs rather than measures
the directional amplitudes using the same unknown `Z=Z0*g`,

```text
v_plus=(F/Z+V)/2, v_minus=(F/Z-V)/2,
r=(F-Z*V)/(F+Z*V),
```

then inserting this ratio into the warm response relation reduces to
`F=2*Z0*V` wherever the ratios exist. The unknown `g` cancels. This procedure
does not identify it. A separately fixed reference impedance can define measured
power-wave coordinates, but its equality with the model port impedance must
itself be independently supported; redefining the reference for each trial
`g` is forbidden.

An alternative route uses independently calibrated force and velocity under
a physically established cold condition. For `V!=0`, `Z=-F/V`, and
`g=Z/Z0` only if `Z0` is independently owned. This does not require reconstructing
unknown-impedance directional waves. Its cold preparation, sensor transfer,
units and sampled-law validity are still obligations. Multiple nonzero motions
and an independent validation set are needed to test a constant passive response;
defining `Z=-F/V` for each record would make the test vacuous. The cold `a=0`
certificate cannot itself be inferred from the fitted identity `Z=-F/V`.

The proposed template admits either independently calibrated directional
readout or the cold force/velocity route as an explicit future selection.
It does not choose between them after target data are known.

## 5. Predictions that survive calibration

The identification stage must state which records identify which quantities.
For a signed-pulse route, warm zero, paired positive/negative and distinct
amplitude preparations can test offset, odd response and linearity on a
predeclared domain. The model predicts constant `r` and, on a zero initial pair,
`E_new=8*g^2*A^2/(2+g)^2`. These equations are proposed tests of the combined
preparation/readout/response contract, not assertions about measured data.

A separately prepared cold source `z=(1,0,0,0)` belongs to RRP1's balanced-head
domain. With `H=2I-L`, the fixed five-site source gives
`h=(H S z)_origin=1421/1620`. Its first origin response is

```text
w=2h/(2+g), b=-h/(2+g), deposit=g*h^2/(2+g)^2.
```

The coefficient `h` is a model input, not an instrument calibration standard.
Independent preparation must justify the physical `S z` and its scale.
The normalized quantity `eta=deposit/h^2=g/(2+g)^2` is invariant under
`g -> 4/g`, with maximum `1/8` at `g=2`; this is not a fraction of the initial
wave energy. It cannot choose the branch used to explain the same data.
Use this cold record as validation only if it was excluded from identification;
when the cold force/velocity route is used for identification, reserve different
physical preparation records and amplitudes for validation.

For each held-out record, retain measured values and the full joint admissible
calibration/parameter set. Compare the signed port residuals, the force/velocity
law and the energy/work residuals at the frozen scope. A finite collection of
agreements characterizes at most that tested context and range. It is not
complete apparatus-family classification or a Born occurrence law.

For example the cold signed residuals are `(2+g)*b+h` and `(2+g)*w-2h`.
An energy residual `D-g*b^2` is an independent check only when `D` has a
separate measurement provenance; setting `D=g*b^2` in the readout makes it
an identity. The threshold `q` also needs its own pointer calibration before
any counting comparison. Neither `q` nor the retained record set may select
the conductance branch giving desired QDD weights or frequencies.

## 6. Discrete work is not automatically measured work

The algebraic identity `tau*F*V=E_star*p*f` is exact under Section 1's map.
The actual mechanical work over a physical window I is instead

```text
W_meas=integral_I F_phys(t)*V_phys(t) dt.
```

The physical claim needs a separately justified sampling/work bridge comparing
that integral with `E_star*g*(a^2-b^2)` at the same boundary and time window.
For interval means, `integral F*V = tau*(mean(F)*mean(V)+cov_I(F,V))`;
discarding the covariance is not a calibration. Timing, unresolved bandwidth,
interpolation and quadrature errors need explicit bounds. The centered `p`
uses two wave slices and is not automatically an interval-mean physical velocity.

The inherited `E(u,v)` is a positive discrete two-slice energy. Its positivity
does not make it the instantaneous mechanical energy of a spring lattice, and
the recurrence is not automatically the exact sampled flow of such a lattice.
A realization must supply the state map, dynamics and energy correspondence,
not just Newtonian units. Outgoing signed-tape energy is also not automatically
measured heat: thermalization, delay, leakage, capacity and the calorimeter
boundary require their own response and energy accounting.

Two direct checks exhibit the distinction. With `m=(u+v)/2`, `d=v-u`,
`E=||d||^2/2+<m,Lm>/2-<d,Ld>/8`; the last term cannot be dropped when
identifying an ordinary midpoint mechanical energy. In a free spectral mode
with eigenvalue `lambda`, the recurrence has `cos(theta)=1-lambda/2`.
An ordinary oscillator with squared frequency `lambda` at unit sampling
instead has `cos(theta)=cos(sqrt(lambda))`, generally different. These
comparisons delimit that naive interpretation, not every possible realization.

For one port, a future work residual is
`R_work=W_meas-E_star*g*(a^2-b^2)`; for several ports sum the right-hand side
and use the matching global boundary. Under cold conditions the outgoing-energy
increment has the opposite sign to work done on the wave. A calorimeter test
must preserve that convention and cannot add tape energy to heat as two stores.

## 7. Error bounds, records and decision routing

Exact model arithmetic does not make a physical measurement exact. Use a
predeclared joint uncertainty set for offsets, gains, polarity, delays, source,
scales and observed coefficients. A denominator interval containing zero forbids
the ratio estimate. A nonempty allowed ratio set is intersected with `(-1,1)`
only as a reported model-consistency test, never by deleting inconvenient data.

If the entire certified ratio interval `[l,u]` lies in `(-1,1)`, monotonicity gives

```text
g in [2(1-u)/(1+u), 2(1-l)/(1+l)].
```

An interval crossing zero includes `g=2`; that is not singular. An interval
touching `r=-1` has no finite upper bound, and one touching `r=1` may approach
zero conductance. Model-incompatible parts and unavailable bounds must be
reported, not clipped into a finite best estimate. Unknown polarity gives the
union of both admissible branches. Correlated calibration uncertainty is not
replaced silently by independent error bars or a probability distribution.

A finite measurement interval does not determine an exact rational `g`.
RRP1's rational mathematical context must be distinguished from a physical
parameter set. A chosen rational nominal value needs a frozen selection rule
and model-error allowance; rounding a fitted real estimate is not a derivation
of rationality or a status promotion.

Before a physical test, freeze source and data manifests, hashes of existing
inputs and licenses, the future acquisition/custody protocol, sensor and
conversion certificates, extraction code and version,
context/reference-plane equality, preparation domain, split of identification
and validation, joint uncertainty construction, failure thresholds and invalid
record disposition. Hash each new raw record at acquisition and retain its
custody/readback receipt; its bytes cannot be pinned before it exists.
Record every attempted acquisition in order. A failed or
invalid acquisition is retained with its reason and is not silently replaced.
No numerical tolerance, uncertainty budget or dataset is supplied here.

The template distinguishes missing-definition STOP, acquisition-invalid records
and a completed model decision. Only a later independently reviewed complete
physical preregistration may produce a scoped physical agreement or rejection.
It must define the exact predicates separating agreement, unresolved overlap
and incompatibility before data inspection. Failure of this proposed realization
does not establish impossibility of physical apparatuses or falsify Born's law.

The present decision is **STOP-DEFINITION / NO DATA / NO PHYSICAL PASS**.
QDD effects, post-state instruments, reset, ordered occurrence, family
completeness and L1-to-L5 realization remain open. `COINCIDENCE-RECORD-FREQUENCY`
is candidate-H / UNTESTED / STOP outside the registry. The photon identification
chain, #756 F3 and the restriction on production #742 are untouched. No normalized
energy share or laboratory calibration supplies an L6 probability measure.

## 8. External terminology and scope

The mechanical port is our proposed interpretation of the displayed equations.
Two primary sources support the external terminology, with deliberately limited
use:

- K. Kurokawa, [Power Waves and the Scattering Matrix](https://cseweb.ucsd.edu/classes/fa12/cse291-c/papers/ScatteringMatrix.pdf),
  IEEE Transactions on Microwave Theory and Techniques 13(2), 194-202 (1965),
  equations (1), (10) and sections VIII-IX: power-wave normalization and the
  distinction from general traveling-wave amplitudes. Our real mechanical
  force/velocity application is an explicit analogy, not a theorem imported
  about TWIST-J. No complex-impedance or electromagnetic interpretation follows.
- N. Vlajic and A. Chijioke,
  [Traceable Dynamic Calibration of Force Transducers by Primary Means](https://pmc.ncbi.nlm.nih.gov/articles/PMC5990289/),
  Metrologia 53, S136-S148 (2016), sections 2.1, 3.4.3 and 3.6: physical
  reference traceability and characterization of dynamic amplitude and phase
  through the measurement chain. This is methodological support, not a
  calibration certificate for the proposed apparatus.

Neither source supplies a TWIST-J state map, physical decoder, source
preparation, occurrence law or evidence that this profile is realized.
No third-party dataset or code is imported, and no quoted passage is reused.
