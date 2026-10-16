# Signed two-cut observability and the calibration procedure

**NON-CANONICAL / conditional L1 proof and prospective physical protocol.**
2026-10-13. Original work Apache-2.0, A. M. Thorn.

This is lane O under reservation #1484. Its immutable contract is
`4302c31f07823b2a843e3702ca14620c1917b853`,
[CONTRACT.md](https://github.com/mathorn1973/twist-j/blob/4302c31f07823b2a843e3702ca14620c1917b853/notes/C-CLASSICAL-SIGNED-PORT-CONTRACT-N/CONTRACT.md),
SHA-256 `0a9c248e03385c1a7b5212821f8d6c83b2c76cd4dea626d4e3b984ef6eeb217e`.
All formulas and procedures below preserve that contract. No scientific script,
import, verifier, simulation, data acquisition or experiment was performed to
prepare this document. No passing public or physical gate is reported.

## 1. Exact types and the two-cut causal domain

All mathematical fields are rational. The source is z in Q^4; the operational
domain is max_i |z_i|<=1, with literal signed equality and zero included. Use
the frozen D3 stencil, its full diagonal 8/9, the five sites Y and ordered
ports R=(y0,y1,y2,y3), with

```text
y0=(0,0,0), y1=(1,1,0), y2=(1,0,1), y3=(0,1,1), y4=(2,0,0),
B={d in D3: |d|^2 in {2,4,8,10,16}},
weights=(6,1,15,1,1),       c_d=weight(|d|^2)/324,
B_zero=B union {0},        D=Y+B_zero+B_zero.
```

Let P insert four port coordinates into Q^D, let L_D be the principal
Dirichlet operator, and put H=2I-L_D and J4=11^T on Q^4. The source map is

```text
s=1^T z,
S z=sum_(i=0)^3(z_i-s/5)delta_yi-(s/5)delta_y4,
Q=P^T S=I-J4/5,              G_source=I-J4/5.
```

The same matrix Q also gives the source Gram because
`||S z||^2=sum_i z_i^2-s^2/5=z^T G_source z`. It does not identify the
five-site source with a native finite-field checkpoint or a physical source.

With four conductances equal to two, write

```text
C=2PP^T,       D_g=I+PP^T,       D_g^-1=I-(1/2)PP^T.
```

The last identity follows because P^T P=I. For incoming zero at both cuts,
the complete wave and output sequence is

```text
(u0,v0)=(0,S z),
w0=D_g^-1 H S z,                 b0=-(1/2)P^T w0,
(u1,v1)=(S z,w0),
w1=D_g^-1[H w0-(I-PP^T)S z],     b1=-(1/2)P^T(w1-S z).    (O1)
```

Thus the final wave pair is (w0,w1), not a freshly prepared wave. The suffixes
0 and 1 on b denote the first and second cut.

Multiplication by H enlarges support by at most B_zero. D_g^-1 changes values
only at R and does not enlarge support. Consequently w0 is supported in
Y+B_zero, and w1 in Y+B_zero+B_zero=D. The same support induction applies to
the infinite zero-extended model: no outside value has been discarded through
these two cuts. The principal operator retains the full boundary diagonal,
so the finite energy is the full zero-extension energy. These assertions are
only the prepared two-cut equality, not all-time infinite-lattice equality for
an arbitrary wave supported up to the boundary of D.

## 2. First-cut response and explicit reconstruction

Set M=P^T H S. Then (O1) and P^T D_g^-1=(1/2)P^T give

```text
b0=R0 z,                    R0=-M/4.                    (O2)
```

Here the complete matrix, derived from the frozen stencil, is

```text
M=(1/1620) [[1421,-349,-349,-349],
           [-354,1416,-354,-354],
           [-354,-354,1416,-354],
           [-348,-348,-348,1422]].                       (O3)
```

An independent direct derivation uses only one-hop distances. All six distances
between distinct ports have square two. Therefore

```text
J=P^T H P=(59I+J4)/54.
```

The entries from y4 to the four ports are `(1,6,6,0)/324`: the last distance
has square six and is absent from B. The five-source row sums are therefore
`(379,384,384,378)/324`. Subtracting one fifth of these sums from every
column of J gives (O3).

For v=(349,354,354,348)^T, this is the rank-one form

```text
M=(1770I-v1^T)/1620,            1^T v=1405.
```

Since 1770-1405=365!=0, direct rank-one multiplication yields

```text
M^-1=(54/59)(I+v1^T/365),
det M=1770^3*365/1620^4 != 0,
z=-4 M^-1 b0=-(216/59)(I+v1^T/365)b0.                    (O4)
```

Indeed `(I-v1^T/1770)(I+v1^T/365)=I`, using 1^T v=1405.
This is a symbolic inverse on all Q^4, not a finite source census. First-cut
signed equality is therefore equivalent to equality of the complete source z.
In particular the same assertion holds on the frozen operational domain,
Z_I and Z_V. Four scalar first-cut coordinates are necessary for a linear
injective map from Q^4; this does not prove that four ports are minimal when
multiple cuts or nonlinear observations are allowed.

## 3. Second-cut response, including port loading

The second response must include the first cut's attenuation at every port.
Define K=P^T H^2 S, with the finite H above. Since P^T(I-PP^T)=0,
(O1) gives

```text
b1=R1 z,
R1=Q/2-K/4+J M/8.                                      (O5)
```

In detail, `P^T H D_g^-1 H S=K-(1/2)J M`; the term JM/8 is thus the
effect of all four loaded ports. Replacing it by an origin-only damping term
would describe a different contact. No wave or tape reset occurs in (O5).

For completeness, the exact expanded coefficients are

```text
K=(1/87480) [[85969,-20721,-20721,-20721],
            [-21338,85352,-21338,-21338],
            [-21338,-21338,85352,-21338],
            [-20636,-20636,-20636,86054]],

R1=(1/699840) [[192202,-48768,-48768,-48768],
              [-47829,193141,-47829,-47829],
              [-47829,-47829,193141,-47829],
              [-48879,-48879,-48879,192091]].             (O6)
```

Here is a finite symbolic certificate for K without relying on an execution.
Let h(0)=360/324, h(d)=weight(|d|^2)/324 for d in B, and h=0 otherwise.
The numerator of the convolution h*h, with denominator 324^2=104976, at
the displacements needed here is

| Displacement | Square length | Contributions involving h(0) | Both nonzero stencil entries | Total numerator |
|---|---:|---:|---:|---:|
| (0,0,0) | 0 | 129600 | 3168 | 132768 |
| (1,1,0) | 2 | 4320 | 420 | 4740 |
| (2,0,0) | 4 | 720 | 318 | 1038 |
| (2,1,1) | 6 | 0 | 528 | 528 |

The shell sizes in order (2,4,8,10,16) are (12,6,12,24,6), so the first
nonzero sum is `12*6^2+6+12*15^2+24+6=3168`. For the other three rows,
let N_st(d) count a in the s-shell with d-a in the t-shell. Directly splitting
the signed coordinate permutations of (1,1,0), (2,0,0), (2,2,0), (3,1,0)
and (4,0,0) gives these ordered-pair count matrices in that shell order:

```text
N(1,1,0) = [[4,2,1,0,0],
            [2,0,0,2,0],
            [1,0,0,2,0],
            [0,2,2,4,2],
            [0,0,0,2,0]],

N(2,0,0) = [[4,0,0,4,0],
            [0,0,4,0,1],
            [0,4,0,0,0],
            [4,0,0,4,0],
            [0,1,0,0,0]],

N(2,1,1) = [[2,1,2,2,0],
            [1,0,0,0,0],
            [2,0,0,2,0],
            [2,0,2,0,0],
            [0,0,0,0,0]].
```

Taking `sum_(s,t) N_st weight(s)weight(t)` gives respectively 420, 318 and
528. The distances from each port to the five source sites are exactly the
zero, two, four and six types in the table. Thus P^T H^2 P has diagonal
132768 and off-diagonal 4740 over 104976, and the y4 column is
`(1038,4740,4740,528)^T/104976`. Subtracting one fifth of its complete
five-source row sum yields the displayed K.

Finally

```text
JM=[104430I+(365*1-59v)1^T]/87480.
```

Substitution in (O5), with Q=I-J4/5, gives R1 in (O6). The causal buffer
ensures that the convolution calculation is also the finite Dirichlet
calculation on these prepared inputs.

The complete signed observation is the injective linear map

```text
Y2=(b0,b1)=(R0 z,R1 z),
b1=-4 R1 M^-1 b0.                                      (O7)
```

The last equality is a second-cut consistency condition; it is not a new
calibration reference or an instruction to synthesize b1 from b0 instead
of measuring it.

## 4. Energy targets and sign-loss controls

The frozen per-cut identity gives, for the actual prepared wave,

```text
E0=(z^T G_source z)/2,
E1=E0-2||R0 z||^2,
E2=E0-2||R0 z||^2-2||R1 z||^2.                          (O8)
```

The corresponding per-port deposit is d_tj=2(R_t z)_j^2. E1 and E2 are
energies of the residual wave pairs, not totals with the same deposits
counted again. Positivity follows from the inherited positive pair energy
on the finite zero extension. The full occupied-tape inverse and invariant
are the separate lane R obligation; equations (O8) use only the cold
prepared prefix and do not supply a reset.

On Z_I, E0=0 for z=0 and E0=2/5 for every signed unit vector. On Z_V,
E0=3/5 for equal signs and E0=1 for opposite signs. Together with R0 and R1,
these give exact rational predictions for every frozen preparation and both
cuts, without choosing a new threshold or probability.

Two controls locate the information lost by squaring.

1. For every nonzero z, Y2(-z)=-Y2(z), and Y2(z)!=0 by (O4). All eight
   squared coordinates are nevertheless identical. The pairs +e_i,-e_i
   already occur in Z_I, and z=e0+e1 with -z occurs in Z_V. Literal source
   equality explicitly does not quotient this sign away.
2. The loss at the first cut is not only global sign. Put

   ```text
   z_plus = [27/43070](1063,1073,708,696),
   z_minus = [27/118](1,-1,0,0).
   ```

   Both are in Z_op: their largest absolute components are respectively
   28971/43070<1 and 27/118<1. From (O4) they equal
   `(1/4)M^-1(1,1,0,0)` and `(1/4)M^-1(1,-1,0,0)`. Their first signed
   outputs are respectively `(-1,-1,0,0)/16` and `(-1,1,0,0)/16`, so
   all four first-cut deposits are `(1/128,1/128,0,0)`. Their sources are
   not global-sign equivalents. This is a structural first-cut control
   inside Z_op, not an extra physical validation preparation. It does not
   assert equality of their second-cut deposits or full post-states.

If only the origin channel is observed, the two rows of the present four-port
model are

```text
b0,origin=(-1421 z0+349(z1+z2+z3))/6480,
b1,origin=(192202 z0-48768(z1+z2+z3))/699840.
```

Their two-variable determinant has numerator
`1421*48768-349*192202=2220830!=0`. The two-cut origin-only kernel is
therefore exactly `{z:z0=0, z1+z2+z3=0}`, of dimension two. For example
z=(0,1,-1,0) in Z_V is dark at that observed port at both cuts, while the
full four-port record is nonzero. Waiting beyond the declared two cuts is
not part of this contract. This assertion does not assume that the finite D
boundary preserves the infinite model at later times.

## 5. Exact prediction enumeration for the fixed S/I/V split

Stage S contains independent calibration references; it is not an additional
model-fitting source family. Stage I uses exactly

```text
0,+e0,-e0,+e1,-e1,+e2,-e2,+e3,-e3
```

in that acquisition order. Its model output is zero at zero, and the signed
column `+-R_t e_i` for each nonzero source and cut t.

Stage V uses the six ordered pairs `(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)`;
for each, its sign order is `(-1,-1),(-1,+1),(+1,-1),(+1,+1)`. These are
exactly the 24 frozen sources. Its model prediction is

```text
z_(i,j,sigma,rho)=sigma e_i+rho e_j,
y_model,t=sigma R_t e_i+rho R_t e_j,        t=0,1.         (O9)
```

The baseline acquisition protocol has one complete two-cut record for each
of the nine I preparations and each of the 24 V preparations. There is no
independent-trial, noise-distribution or frequency claim. Repetitions, a
random acquisition order or additional source preparations would need their
own prior acquisition specification; they cannot be introduced after V is
opened to replace inconvenient records.

Every preparation is a new whole-apparatus trial with its own independently
specified preparation/renewal boundary account. There is no refresh or reset
between its two cuts. The need to initialize the next trial is not satisfied
by pointer wrapping or returning one receiver coordinate.

## 6. Physical qualification: required fields, all currently unissued

The physical observable route in this protocol is an independently calibrated
signed outgoing amplitude at each marked port. Its proposed dimensional value
is v_minus=V0 b, with V0=A0_length/tau_step. The extraction must measure that
amplitude; it must not infer it by solving (O1) from the intended source.
Force/motion and energy measurements have distinct roles below. Their proposed
mechanical interpretation remains conditional on the frozen dictionary.

Before any physical V record is opened, one instance packet must resolve the
following fields. A filename or certificate ID without its retrievable payload
and stated range is insufficient. This document issues none of them.

| Required field | Concrete payload and qualification predicate |
|---|---|
| INSTANCE | Physical device, port/mode order, carrier, permitted controls, exact signal/reference planes, external connections and observation band; the same instance is used for I and V. |
| SOURCE | Independently specified preparation of each nominal S z, evidence locating the five sites/modes, marked signs and scale, bounds on preparation error and unwanted inputs, and preparation-to-state equality or error relation. The intended z and a fit to its output are not a source certificate. |
| READY | Actual previous/current wave preparation, two initially cold incoming slots, all outgoing slots and pointer, with initial-state error bounds. Zero sensor offset is not a certificate of zero incoming wave or empty memory. |
| SENSORS | Four independently calibrated signed outgoing channels, offsets, relative and absolute gains/polarities, transfer operators, temporal-mode extraction, bandwidth, saturation, cross-talk, loading and uncertainty over the specified range. |
| UNITS | Independent references and positive bounded conversion sets for A0_length, tau_step and E_star. The same E_star cannot be fitted by imposing the tested energy balance. |
| CLOCK_BINS | Trigger, two ordered cuts, fixed interval endpoints, channel delays and common time convention, with a sample/bin-to-coupled-transition bridge and its error. No native TM clock is identified. |
| CONTACT | Complete actual interaction, source/receiver boundary, passive/active control and physical relation to the frozen four-port g=2 target. Constitutive departures are retained as implementation discrepancy, not a reason to refit g from V. |
| STATE_ENERGY | Independently calibrated wave and tape energy observations at the matching boundaries, their relation to E_star E_D and E_star sum_j 2b_j^2 if those readings are asserted, and their loading/delay uncertainty. Model-predicted energies alone cannot fill this field. |
| BOUNDARY | Every external and internal energy transfer involving wave, both tapes, source, controls, sensors, archives, loss and reset; each store/flux has one sign and appears once. Any unmeasured contribution has an independent bound. |
| RENEWAL | An actual whole-apparatus preparation/reset procedure for the next trial, including retained old records, finite capacity and reset/preparation work outside the two-cut window. No blank register is silently supplied. |
| UNCERTAINTY | One sound joint uncertainty set for shared references, source, sensor, time, scale, loading, extraction and all energy terms, with range/validity evidence; deterministic bounds are not replaced by independent one-sigma bars. |
| CUSTODY | Raw trace, preparation and calibration receipts; acquisition-order manifest; hash/byte-count rules; all invalid/saturated/missing records; separate S, I and V membership and exposure records. |
| I_FREEZE | Completed I records, independently calibrated sensor packet, final physical settings and fixed preprocessing/uncertainty definitions, all frozen before V; no outcome-derived sign, phase, delay, gain or conductance change. |

An unresolved field gives NOT_READY before V. The proof of (O4), the chosen
g=2, and the frozen numerical tolerances do not qualify a physical instance.
Existing external archives must meet the same field requirements; their mere
availability does not do so.

## 7. Stage S: independent sensors, preparation, time and energy

S is a characterization and reference stage, not a fit of the tested response.
Its ordered procedure is as follows.

1. Mark and record the four reference planes, the common positive direction,
   source/mode order, observation band, signal range and actual instance
   boundary. Supply independent source and ready-state evidence, including
   both cold slots. Declare which physical state corresponds to each wave
   slice; an instantaneous displacement is not automatically a two-slice
   energy reading.
2. Characterize each acquisition path against independently certified signed
   references in both polarities, at zero and over its stated nonzero range.
   Retain raw response, reference provenance, loading, cross-talk, drift and
   saturation bounds. Channel swapping may diagnose a relative mismatch; it
   does not supply an absolute amplitude or sign reference. Any instrument
   deconvolution must have a separately calibrated transfer and error bound.
3. Fix the two-cut trigger and extraction functions. For example write the
   processed physical coefficient as a fixed functional

   ```text
   vminus_tj = L_tj(raw_signed_trace_j; calibration),
   bcal_tj   = vminus_tj/V0.
   ```

   L_tj must name the reference plane, interval, delay correction, weighting
   kernel, filtering and transfer correction in the calibration packet. A
   unit-area weighted integral is admissible only when an independent
   temporal-mode certificate makes it the stated coefficient with a bounded
   error. Do not choose a window or phase from the source response. A single
   gain may replace a frequency-dependent transfer only at a certified range.
4. Calibrate A0_length, tau_step and E_star through independent references,
   recording correlations and strictly positive lower bounds. Fix
   `V0=A0_length/tau_step`, `F0=E_star/A0_length`,
   `Z0=E_star*tau_step/A0_length^2` and nominal `Z_j=2Z0` under the
   chosen dictionary. Do not obtain an unknown reference impedance by trying
   different g values in the same directional-wave formula. Do not infer the
   cold condition from a fitted force law.
5. Independently characterize force/motion or other work channels, wave and
   tape energy observations, all external energy inputs and all losses. For a
   force/motion route use the measured integral `sum_j integral F_j V_j dt`
   on the same boundary, not the product of two interval means. The latter
   omits covariance. Specify quadrature, bandwidth, loading and delay errors.
   The identity `tau_step sum F_j V_j=E_star sum 2(a_j^2-b_j^2)` is a
   dictionary identity and is not an independent work measurement.
6. Form and freeze the joint uncertainty set Xi_S, its soundness evidence,
   calibration validity range and expiry rule. Shared scales, source standards,
   timing references and sensor paths remain shared variables in this set.
   Freeze the whole trial preparation/renewal procedure and its separate energy
   account. Close S only after every S-owned qualification field in Section 6
   has a payload capable of supporting the proposed test. I_FREEZE is supplied
   after Stage I; the complete qualification bundle is required before V.

In particular, defining incoming/outgoing waves with the same unknown model
impedance and then recovering that impedance from their ratio is not an
identification. Defining tape heat as `2b^2` and then checking that same
quantity against `2b^2` is not a physical energy test. These routes remain
NOT_READY unless independent measurement content is added.

## 8. Stage I: nine preparations and an unconstrained apparatus diagnostic

After S, prepare and acquire the nine sources in Section 5. For each, retain
the entire two-cut trace and complete post-state/energy record. No wave or
tape is changed between its cuts. The interpretation of z, the matrix target
and g=2 remain fixed.

An explicit apparatus diagnostic, computed from the calibrated signed
observations at each cut, is

```text
c_t = ycal_t(0),
A_t e_i = [ycal_t(+e_i)-ycal_t(-e_i)]/2,
d_ti = [ycal_t(+e_i)+ycal_t(-e_i)]/2-c_t.                 (O10)
```

The exact model gives c_t=0, d_ti=0 and A_t=R_t. Do not constrain a measured
fit to these answers: c_t, d_ti and every entry of A_t must be allowed to
differ. They diagnose offset, oddness, and the local signed linear map on
this training set. They are not a proof of linearity on every Z_op source.

Stage I can characterize the selected instance and document its fixed final
settings. It cannot recalibrate S by declaring its observed map to equal R_t,
replace g=2 by a fitted conductance, fit an arbitrary post-source transform,
or define an energy reference from energy conservation. If prior apparatus
adjustment has occurred, its exposure and physical settings must be recorded;
only one final unchanged instance enters V. No V record may influence it.

Close I by freezing the raw/certificate manifest, exact target matrices, all
preprocessing, Xi, actual instance/settings, source preparation and uncertainty
methods. No successful training fit is a qualification substitute or a
physical PASS. If a required certificate is missing, the next disposition is
NOT_READY rather than acquisition of V in search of a fitting convention.

## 9. Stage V: fixed held-out prediction and sound residuals

The validation packet contains exactly the 24 preparations in Section 5, with
both cuts and all four signed outputs. The mathematical target at each entry
is (O9). It is never the measured A_t from (O10). Nominal preparation errors
belong to the actual implementation/error account; do not rescale nominal z
from its output or subtract a fitted preparation correction to force agreement.

For each preparation z, define eight response residuals

```text
r_y,tj(z) = bcal_tj(z)-(R_t z)_j,        t=0,1; j=0,1,2,3. (O11)
```

Use the same independently defined physical boundary over the complete two-cut
window for its full energy residual:

```text
N_E = Delta E_wave + Delta E_tapes + Delta E_control
      +Delta E_sensors +Delta E_records/reset
      -W_external-Q_external,
r_E(z)=N_E/E_star.                                      (O12)
```

Preparation/reset outside that window has a separate retained ledger. Any
preparation/control action continuing inside it belongs in (O12). Internal
wave-to-tape work is not also an external flux. An outgoing energy packet
retained in a tape is not counted once as tape energy and again as exported
heat. If a readout copy consumes physical power, its own cost is accounted,
not another copy of the same mathematical `2b^2` deposit.

The model energy targets E0,E1,E2 in (O8) are retained alongside the measured
ledger, with their physical mapping/error certificate. They are not substituted
for unmeasured wave/tape energies in (O12). In the absence of that independently
qualified mapping and boundary account, a physical energy-reading conclusion
is unavailable even if every signed response agrees. If only a complete-state
mathematical energy is computed, label it mathematical, not calorimetry.

Let Xi be the frozen sound joint set of all calibration, measurement, source,
time, loading, scale and boundary uncertainties for this validation packet.
The required intervals are enclosures of the joint ranges

```text
I_y,tj(z) contains {r_y,tj(z;xi):xi in Xi},
I_E(z)   contains {r_E(z;xi):xi in Xi}.                  (O13)
```

Compute these by a documented validated interval/range procedure using the
original shared variables. Ordinary floating-point endpoints without an
outward/error certificate are not sound enclosures. A parameter interval
containing zero forbids division by it; qualification requires positive
V0 and E_star bounds. No Gaussian assumption, independent error-bar addition,
or probability law is supplied here. A probabilistic calibration certificate
would need its own explicit coverage interpretation; it cannot silently become
a deterministic sound bound under this protocol.

For example, reconstruction of ideal z has the exact perturbation relation

```text
delta z=-(216/59)(I+v1^T/365)delta b0,
|delta z_i| <= (216/59)[|delta b0_i|+(v_i/365)sum_j|delta b0_j|],
||delta z||_infinity <= (384696/21535)||delta b0||_infinity <18||delta b0||_infinity.
```

This is a mathematical sensitivity bound. Using the reconstructed z as the
independent SOURCE certificate would use the tested law to certify itself.
Correlated interval propagation can give sharper bounds than the displayed
absolute-value estimate; it must retain those correlations explicitly.

There are 192 required signed residual intervals and 24 full-window energy
intervals. Set eps_y=eps_E=1/10000, exactly as in the frozen contract.

- PASS requires qualification and every required interval contained in its
  closed band [-1/10000,+1/10000].
- FAIL requires at least one sound required interval disjoint from that band.
- Otherwise the decision is UNRESOLVED. An interval touching the band is not
  disjoint; a zero-width interval on its boundary is contained.
- Missing qualification is NOT_READY before V. A missing/invalid acquisition
  is retained with its reason and supplies no valid interval. It cannot help
  obtain PASS; without a separate valid decisive FAIL the packet is UNRESOLVED.
  Loss of the underlying calibration/qualification is recorded explicitly and
  cannot be hidden as a physical model failure.

No invalid or failed attempt is replaced or deleted. A later repeated or revised
test has a new prospective acquisition record. No threshold, orientation,
source assignment, phase, timing window, normalization or interpretation is
changed after V is inspected.

A physical PASS covers exactly these 24 preparations and two cuts. It does
not assert a uniform physical bound on all Z_op, complete apparatus-class
coverage, an autonomous clock, source-to-native-U identification, quantum
effects, individual event selection, Born occurrence or an L6 measure.

## 10. Concrete packet and record schema

The following is a required-field schema, not a runnable file or supplied data.
Hashes name actual bytes when they exist; no hash of future data is invented.
An absent payload is represented by null plus its NOT_READY reason, never by
a fabricated zero or empty certificate.

```text
INSTANCE_PACKET
  schema: CLASSICAL_SIGNED_PORT_O_V1
  contract_pin: 4302c31f07823b2a843e3702ca14620c1917b853
  contract_sha256: 0a9c248e03385c1a7b5212821f8d6c83b2c76cd4dea626d4e3b984ef6eeb217e
  physical_instance_id; final_settings_id; source_adapter_id; context_id
  observable_route: INDEPENDENT_SIGNED_OUTGOING_AMPLITUDE
  port_order: [y0,y1,y2,y3]; common_orientation; reference_planes[4]
  preparation_order_I[9]; preparation_order_V[24]; one_record_per_preparation
  preparation_renewal_id; full_boundary_id; clock_bins_id; mode_band_range
  S_certificate_payloads{INSTANCE,SOURCE,READY,SENSORS,UNITS,CLOCK_BINS,
                        CONTACT,STATE_ENERGY,BOUNDARY,RENEWAL,UNCERTAINTY,CUSTODY}
  Xi_definition; range_algorithm_id; preprocessing_id; I_freeze_receipt
  eps_y: "1/10000"; eps_E: "1/10000"
  missing_fields[]; qualification_status: QUALIFIED | NOT_READY

TRIAL_RECORD
  trial_id; acquisition_index; stage: I | V
  preparation_id; nominal_z[4] as exact rational strings
  instance/settings/context/source_adapter/S_certificate/I_freeze references
  actual_preparation_receipt; source_error_bounds; cold_slot_receipts[2]
  initial_wave/tape/pointer_receipts; previous_trial_renewal_boundary_receipt
  start_trigger; clock_reference; declared_intervals[2]; stop_receipt
  cuts[2]:
    cut_index: 0 | 1
    raw_signed_trace_refs[4]: {path_or_uri,bytes,sha256,units,sample_clock}
    sensor_loading/transfer/calibration_refs; fixed_extraction_id
    physical_vminus_intervals[4]; converted_b_intervals[4]
    exact_model_b[4] from (O9), without measured-map refitting
    response_residual_intervals[4]; shared_Xi_reference
  energy_window:
    matching_start/end_boundary_receipts
    independently_measured_Delta_E_wave/tapes/control/sensors/records_reset
    independently_measured_W_external/Q_external
    raw_energy/work_trace_refs; independent_bounds_for_unmeasured_terms
    units/signs/provenance_for_each_term; internal_transfer_double_count_check
    model_E0/E1/E2 as exact rational strings and separate physical_mapping_ref
    full_residual_interval_in_E_star_units; shared_Xi_reference
  full_post_state_retention_ref; archive_and_capacity_status
  status: COMPLETE_VALID | INVALID_ACQUISITION | MISSING_REQUIRED_RECORD
  invalid_or_missing_reason; all_attempt_receipts

DECISION_RECORD
  scope: FIXED_24_PREPARATIONS_TWO_CUTS
  qualified_instance_and_all_input_receipt_refs
  residual_interval_refs: 192 signed + 24 full-window energy
  containment/disjointness_for_each_required_interval
  decision: PASS | FAIL | UNRESOLVED | NOT_READY
  fired_entries[]; missing_or_invalid_entries[]; retained_dispositions
  no_refit/no_replacement/exposure_receipt
```

Intervals must name endpoint representation, units, arithmetic/error evidence
and the same joint-set provenance. Raw records retain saturation, invalid
samples, timing gaps and failed attempts. A single predeclared reduction may
coarsen them but must preserve the original bytes and reasons. Source/pointer
addresses and tape records are not erased by reporting only the residuals.

## 11. Source credit and limits of the present contribution

The mathematical authority is Public Canon v101 at
`5f54015ed8361e3a64cb10894397020ddfadd104`. The exact finite port coupling,
energy, source and positive partition are inherited from
`DECODER-RETARDED-LOCAL-ENERGY-TRANSPORT`,
`DECODER-RESERVOIR-RECORD-ACCOUNTING` and
`DECODER-RESERVOIR-QUADRATIC-PARTITION` at their registered conditional scopes.
This note does not re-earn or promote those statuses.

The first-cut M and inverse were already proposed in
[C-DECODER-PORT-OBSERVABILITY-N/PROOF.md](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/notes/C-DECODER-PORT-OBSERVABILITY-N/PROOF.md).
That source discloses its single-platform local checking and absence of a
public pre-run pin. The independent one-hop derivation here is proof-only;
none of its local stdout is a new public gate receipt.

The S/I/V separation, impedance ambiguity, signed observables and measured-work
boundary are credited to
[DECODER-PORT-OBSERVABLE-CALIBRATION-1.md](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/notes/DECODER-PORT-OBSERVABLE-CALIBRATION-1.md).
The finite zero-extension/realization distinctions are credited to
[DECODER-PASSIVE-REALIZATION-BRIDGE-1.md](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/notes/DECODER-PASSIVE-REALIZATION-BRIDGE-1.md).
Neither proposal supplies the missing physical certificates here.

The contribution is the explicit fixed four-port two-cut response, its
proof-only stencil certificate, signed-domain identifiability and controls,
and the concrete data/decision procedure on the frozen 9/24 preparation split.
It does not identify the classical source with native x, the classical cut
with native n, an admitted contact with the missing T, or the classical
energy with the seven-mode DP5 model. The separate P/R/B lanes retain their
types and obligations. Physical source/contact admission, event/renewal,
sampling, SI ownership and higher-layer gates remain open.

Any later computational or physical execution needs its own accepted code,
complete preregistration and public pin/readback. This analytical packet
does not authorize one and supplies no experiment or calibration data.
