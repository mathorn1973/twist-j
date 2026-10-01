# Qualification and prospective four-configuration test

NON-CANONICAL / OPEN engineering test specification, issue #1317.
All numbers below are preselected requirements. None is a measurement.
This document does not start a physical gate or claim laboratory readiness.

## 1. What has to be frozen before confirmation

The mathematical target remains #1316 at
312d0a90b24d5f9e743096f0ee2a477cda719a10, with the exact encoding and complete
auxiliary account in DESIGN.md. First publish circuit/BOM and fixture
drawings, controller HDL/firmware and readout implementation, component inventory,
calibration method, uncertainty/covariance budgets, actual sampling settings,
raw-data schema and reduction code. The run-assignment key, acquisition order,
serial-to-role mapping and identifying calibration files follow the sealed
commitment and later disclosure procedure in section 5a; publish their
commitments before confirmation, not their revealing contents. Their complete
bytes must already be fixed and retained for the subsequent full audit.
These implementation files do
not exist in this package. Their absence is a construction/confirmation STOP,
not a reason to substitute a software trajectory for a device observation.

Qualification uses separate development data and fixed acceptance limits
below. Its outcome cannot count as a blind discovery or confirmation. Freeze
the successful implementation and qualification records under a new public
commit and separately owned physical gate before any confirming trial.
If qualification fails, preserve that outcome and revise/re-pin before new
confirmation; never relax a threshold while keeping the old confirmation pin.

## 2. Named metrology and power boundaries

Use a calibrated Keysight 34465A for DC reference calibration and settled
bank voltages. Its100 V range one-year specification is
+/-(0.0040% reading +0.0006% range) under the specified conditions;
at 32 V this is1.88 mV before other effects. Warm-up, temperature, integration
and calibration conditions must be observed. This specification is not the
uncertainty of a stored-energy map.
[Keysight datasheet 5991-1983](https://www.keysight.com/content/dam/keysight/en/doc/ungate/data-sheets/5991-1983.pdf).

Provide three synchronized NI USB-6366 units, one per local converter, each
with simultaneous V/I channels for donor, recipient and8 V auxiliary rail,
plus one local instrumentation rail pair. A fourth synchronized unit records
24 V motion,5 V FPGA/pointer and acquisition/host input power through suitable
isolated transducers. Slow bank-temperature and settled-voltage scanning is
separate. USB-6366 has eight simultaneous 16-bit inputs, up to 2 MS/s/channel;
its inputs are not isolated. External dividers, isolated amplifiers and
their power/coupling must be calibrated as part of each complete signal path.
[NI specifications](https://www.ni.com/en/shop/hardware/voltage/model-usb-6366).

Use calibrated four-terminal50 milliohm shunts, with 0.1% Vishay WSK2512 as the
selected resistor family. Freeze exact ordering codes, measured resistances
and TCR before construction release. The family specifies up to35 ppm/K TCR
in this resistance range; its nominal tolerance is not a calibration.
[Vishay WSK2512](https://www.vishay.com/docs/30108/wsk2512.pdf).
At donor0.10..0.50 A, the shunt drop is5..25 mV and maximum dissipation12.5 mW.
Qualify BOTH donor and recipient currents down to 0.005 A and bound integrated
offset/error below that level during tails. Donor setpoints are not a lower
bound on actual current: recipient limiting, voltage ratios and equalization
can all reduce it. Unresolved low-current energy remains in the error budget.

Primary port work is externally timestamped signed integral V(t)I(t)dt.
Use simultaneous samples, initially 100 ksample/s/channel during all G slots,
calibrated analog filtering and 1 Msample/s qualification captures to bound
unresolved ripple/correlation. The actual frozen rate/filter must satisfy
the integration error budget, otherwise STOP. Merely multiplying separately
averaged V and I is insufficient for a switching waveform. Outside G, isolate
power paths and bound leakage/switching energy, with transient captures during
dock switching. Log raw signed quantities, including reverse currents.

Bank probes must disconnect during motion and idle except declared short
settled-read windows; record their on-time. Use high-input-impedance calibrated
buffers and include their loading, input capacitance and supply coupling.
Do not continuously attach an INA228 VBUS input: its minimum0.8 Mohm input
impedance alone can drain about 0.294 J at 48.5 V over 100 s. Its unsigned energy
accumulator is not a signed bidirectional-work measurement either.
[TI INA228, tables6.5 and register definitions](https://www.ti.com/lit/ds/symlink/ina228.pdf).
The complete probe/duty-cycle design must pass the idle-loss limit; naming a
precision ADC does not establish that it is non-disturbing.

The converter's8 V supply is derived from its selected donor behind the
donor-port meter (DESIGN.md); count it inside donor depletion and losses,
without double-counting its downstream work as another external input.
Document the actual wiring, BIAS connection and switch sequence. It may not
be replaced by a bench8 V supply during confirmation. Charge stored from a
previous donor is discharged/returned and measured before changing donors.
Any unresolved initial converter storage, separate sensor/control injection
or other local storage depletion is conservatively an upper bound on
non-path contribution to receiving work. Subtract that bound from claimed
source-funded work. A galvanically isolated command path alone is not an
energy-origin certificate. If the bound exceeds10 mJ in the first receiving
G, this design fails. An independently powered receiver is insufficient.

Stored-energy change from calibrated U_a is an independent cross-check of
terminal work, not a way to manufacture agreement by adjusting capacitance.
Publish capacitor leakage/relaxation and converter loss determined by balance
as such; neither is direct calorimetry. For the complete apparatus also bound
motor kinetic/potential energy, supply capacitors and readout/controller
storage. Every supply must be metered; unresolved stored energy or heat balance
is an unresolved apparatus account and blocks an energy-closure claim.

## 3. Numerical tolerances and why these numbers were chosen

The0.500 J spacing fixes the upper admissible bank error: it must be below
0.250 J. Choose0.240 J, leaving a 20 mJ rejection gap between neighbouring
energy intervals. A stricter independent work threshold tests whether the
nominal 1 J receiving reaction is actually powered by the path.

| Quantity | Required bound, including uncertainty |
| --- | --- |
| Exact decoded state | all 96 coordinates match the fixed expected state; zero incorrect/invalid words |
| Bank at every layer and boundary | abs(E_inc -0.500*n)+U_E <=0.240 J |
| Bank-map expanded uncertainty | U_E <=0.020 J |
| Initial bank preparation | abs(E_inc -0.500*n)+U_E <=0.020 J |
| Initial positive/offimage source equality | abs(E_source,+ - E_source,-)+U_difference <=0.010 J |
| Actual voltage | 4.7..50 V for every bank; no commanded baseline consumption |
| First receiving net work | W_B - U_W >=0.950 J and W_B + U_W <=1.050 J |
| Source-attributable first work | W_B - U_W - E_other,upper >=0.950 J |
| Non-path energy possibly entering that work | E_other,upper <=0.010 J |
| Work expanded uncertainty | U_W <=0.010 J for a 1 J pulse; <=1% of larger pulse |
| Negative control target work | integral abs(VI)dt plus uncertainty <=0.020 J over the whole 100 s, and <=0.010 J per G slot |
| Cartridge swap disturbance | abs(Delta E_cartridge)+U_delta <=0.005 J per swap |
| Idle loss, including measurement load | <=0.020 J per bank over each of 100 s and 200 s at each qualified level |
| Wheel energy degeneracy | largest static position-energy difference plus uncertainty <=0.005 J |
| Wheel readout | detent angle within5 degrees, correct code, no invalid samples in settled window |
| Timebase and layer timestamps | expanded uncertainty <=1 ms; fixed10 s macrostep |
| Local control equalization | relative energy resolution <=0.001 J; final residual <=0.005 J, with its own calibrated uncertainty included |

W_B is NET SIGNED electrical work into B_2 over the ENTIRE target G_2
operation in macrostep 3, including its settling/read interval,
including every equalization/back-transfer. Record net r_2 depletion over
the same interval; do not count gross r_2-to-B_2 pulses as incoming work if
the servo has first borrowed B_2 energy to recharge r_2. Every B/Z/r path is
metered and signed, and any local baseline restoration is included.
E_other,upper includes possible contributions over the entire causal interval
from source G_0 in macrostep 1 through every moving-cartridge contact/probe to
the end of target G_2 in macrostep 3, plus depletion of other receiver storage
or baselines. It is not just an auxiliary reading during the receiving gate.
An earlier unaccounted injection into the
cartridge must not be relabelled source-origin energy after transport. Report
resource-cartridge depletion, B_2 gain and all losses separately. The95%
threshold is a chosen minimum useful-transfer fraction, not a measured
efficiency or a consequence of the integer theorem. Passing only the broad
0.240 J encoding test cannot satisfy it.

Require each independent port/bank balance residual to be bounded by its
propagated expanded uncertainty, and that uncertainty <=0.020 J for the
first1 J receiving event. No residual may be explained by an unmeasured
energy source. For the entire apparatus publish the measured input energies,
changes of stored energy and bounded heat with uncertainties; a merely
assigned difference called heat is not an independent balance test.

For work on a 1 J pulse allocate the following *standard* uncertainty ceilings:

| Contribution | Budget |
| --- | ---: |
| voltage calibration |0.5 mJ |
| current/shunt/gain calibration |1.0 mJ |
| offsets and drift |1.0 mJ |
| timing |0.1 mJ |
| integration and unresolved ripple |1.5 mJ |
| qualification repeatability |1.5 mJ |

Their uncorrelated root-sum-square is about 2.6 mJ; an illustrative factor 2
gives 5.2 mJ, leaving margin below the10 mJ requirement. These are allocations
to be demonstrated, not uncertainty values already earned. Retain covariance
from common references and differenced readings. Use a justified coverage
factor and effective degrees of freedom, not automatic k=2 on a tiny dataset.
See [NIST TN 1297 propagation](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty)
and [expanded uncertainty](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-6-expanded-uncertainty).

## 4. Qualification before the four-configuration campaign

Start with two ordered hardware gates, before assembling the complete chain.
These are engineering qualification stages, not newly registered scientific
gates or performed measurements:

**Stage A: one complete cartridge with disconnected sensing.** Qualify one
actual capacitor housing, dock, switches, probes and the intended measurement
duty cycle. Establish its energy map, uncertainty, absorption and relaxation,
then require total idle loss plus its propagated uncertainty <=20 mJ at both
100 s and 200 s, with the actual read windows. Include leakage through the
disconnected switch, probe loading, input capacitance, switching transients
and any possible measurement-supply injection. A measurement-free capacitor
test does not qualify the assembled sensing path. No charging is permitted
during the hold; do not let injection mask a loss.

For 200 s, 20 mJ/200 s=0.100 mW average total loss. Near 48.5 V this corresponds
to an equivalent mean current of about 2.1 microampere, including measurement.
These are requirement conversions, not component predictions. The actual
acceptance quantity remains integrated energy with uncertainty; changing
voltage or pulsed probe loading cannot be replaced by a constant-current
assumption. The stricter 200 s test is required now, not postponed until the
inverse campaign. Passing one cartridge permits this design to proceed; it
does not qualify the remaining population or every dock.

**Stage B: one isolated source cell under cut0.** Only after Stage A passes,
assemble its B_0,Z_0,r_0 banks and complete local converter/control/sensing
path. Each of these three banks must individually meet the same Stage A
criteria; the first successful specimen does not qualify the other two.
Use the source-cell restriction of the already declared cut0 law:
both contacts of q0 disabled, fixed G;A;B;F clock, and the admitted prepared
source. Run the entire 100 s repeated-reaction sequence without external
charging, then the required 200 s forward/inverse qualification sequences.
Keep the designated logical holdout out of end-to-end tuning. Meter all
source bank and auxiliary changes, verify the local coordinates, deadlines
and reserve certificates at every layer, and retain any failed attempt.
Loss allocation, donor-fed control startup and cumulative depletion must
pass together. A single successful transfer does not qualify this stage.
Failure stops this implementation before construction of the full chain;
it does not change the mathematical law or relax its physical test thresholds.

After these stages, complete qualification of all banks, cells and fixtures:

1. Characterize every capacitor at all n=0..41 levels, at 20,23,26 degrees C,
   approached from charging and discharging, under the fixed settling/read
   sequence. Determine U, ESR, absorption,100 s and 200 s idle loss and calibration drift.
   Operate confirmation only at 23+/-1 degrees C. Every cartridge/dock pairing
   and its probe loading must qualify. Invalid single-valued energy mapping
   or too much idle loss rejects the encoding.
2. Validate all local accepted energy classes h=0..4, both directions,
   rejection/no-work states, nonzero static/spectator accounts, pulse endpoints,
   low recipient currents, gate-supply injection and switching transients.
   Qualify the equalization policy including its 32-transfer/1.7 s deadline.
   Voltage range and advertised peak efficiency alone are insufficient.
3. Test the *entire 100 s stress sequence*, particularly cut0, where the
   isolated source can alternate forward/backward reaction every step. Ten
   nominal 2 J source reactions already process 20 J: at 1% loss that is0.200 J
   before leakage and sensing. Loss allocation matters; a nominal 99% peak
   rating does not automatically satisfy every per-bank interval. No continual
   compensation charging is allowed.
4. Qualify both occupied/empty and occupied/occupied physical swaps, all five
   pointer states, code rejection regions, no-write-on-rejection, forward
   AM->R retaining p and true inverse subtracting it. Bound torque-angle work,
   static detent differences and reading disturbance. Check both physical cuts.
5. Verify all 96-coordinate arithmetic and complete inverse controls against
   the pinned model before attaching an empirical claim. Verify pulse-energy
   scope separately: a correct FPGA alone does not validate physical work.
   Broad Dec bands are not an invariant physical input class. Publish the
   narrower preparation and reachable reserve/loss certificates for each
   operation/horizon; without these, do not claim F_device implements the
   law for every state inside independently allowed tolerance bands.
   Freeze a corpus covering all accepted h, all p, both directions and every
   contact-occupancy class; publish its exact inputs before using it as evidence.
   Exclude the designated holdout from end-to-end tuning in this corpus;
   shared logic verification and energy-level calibration remain disclosed.

The selected capacitor's catalogue leakage ceiling is 2.77 mA at rated voltage.
At such a current even30 V for100 s would lose8.31 J, far beyond20 mJ.
That calculation is a stress illustration, not a prediction of leakage at 30 V.
Actual qualification must be far better than the catalogue ceiling; the
datasheet does not promise it. Failure here rejects these selected parts for
this protocol. The same applies to converter pulse efficiency, auxiliary
injection, feedback convergence and fixture timing. Do not order a complete
apparatus on the assumption these requirements are already established.

No qualification measurements, circuit simulations, new scientific runs or
hardware construction were performed for this note. The missing implementation
and qualification may force a different physical design and a new public pin.

## 5. Four configurations, fixed preparation and expected order

All cases prepare the same target R with zero field/resource and p=0; middle
cell ZM, all spectators/channels zero. Use identical charging/readout procedures
and blinded run labels. Compare measured initial source energy, not just H.

| Case | Source field and connection | Required target observation |
| --- | --- | --- |
| positive | PLw, H(w)=1; both channels intact | arrival boundary 2; work and first HIT 3; old full block reset4; HIT 3..10 |
| equal-energy offimage | P(0,0,1,-2), energy5, both channels intact | no accepted target event, BLANK 0..10, negative-work limit |
| cut0 | admitted PLw; both contacts of q0 physically disabled | same null target requirements |
| cut1 | admitted PLw; both contacts of q1 physically disabled | same null target requirements |

Use 100 fresh trials per case, total 400. For positive and both cuts, use the
twenty already published integer H(w)=1 seeds, five repetitions each; no new
seed search is proposed. Offimage repeats its single fixed vector 100 times.
Reserve w=(0,0,0,1) as a logical-orientation holdout never used to tune
end-to-end operation; its energy-level calibration may be shared and that
limitation is explicit. Freeze all full inputs and a balanced shuffled run
order before confirmation, with revealing assignments sealed under section 5a.
Blind the outcome evaluator, not the controller's legitimate local state
input. Include every initiated run and every failure;
no optional stopping or replacement of an unsuccessful trial.

The count100 is an engineering repeatability target, not a claim of certain
operation. Under independent identically distributed trials, zero failures
gives a one-sided95% binomial upper bound about 2.95% for one case. This
illustrates why100 runs cannot establish 99% reliability. Shared drift can
invalidate that sampling interpretation; report block/temperature dependence
and make no natural-law or Canon probability claim from these trials.
[NIST exact binomial bounds](https://itl.nist.gov/div898/software/dataplot/refman2/auxillar/exacbino.htm).

Record complete state at boundary 0 and each of the four layer boundaries of
steps1..10, including cartridge identities/positions, all eleven energies,
all 96 decoded coordinates, raw pointer optical codes/angle, physical cut
locks, measured port/supply work, temperatures and timestamps. Store ADC data
independently of the controller. Do not reconstruct alleged measurements by
running the model. The expected full coordinate table is a prediction generated
from the frozen model before data, not an observation.

At boundary 4 require the original 31 receiver coordinates to match their
initial values exactly and its physical bank energies to meet the same Dec
intervals. This is a decoded return within physical tolerances, not an exact
return of every electron, temperature or energy loss. Pointer HIT must hold
on eight boundaries3..10, spanning 70 s for this selected clock. No first
BLANK-at 11 prediction or eternal-record claim is added.

## 5a. Blind target assessment before full-data disclosure

The two target predicates below apply to the 400 FORWARD confirmation trials
of section 5. The separate inverse blocks of section 6 retain their own frozen
expected tables; do not apply forward arrival/HIT timing to inverse-first
runs. Keep any identifying inverse records sealed until all 400 forward
target assessments are locked, then audit them against those separate tables.
This procedure makes no claim of blind forward-predicate validation for the
inverse blocks.

The complete record exposes the configuration through source coordinates,
cut locks and cartridge routes. Random filenames alone do not blind it.
Separate custody/acquisition from target assessment, with no access to
configuration-revealing records or operator discussion by the target evaluator
until ALL target assessments are locked. This procedure hides assignment;
it cannot prevent a guess based on a legitimate target outcome.

Before confirmation, freeze the projection program, common packet schema,
SI conversion and uncertainty rules, local predicates and assessor output
schema. A custodian retains the run-assignment key, shuffled acquisition
order, raw serial-to-role/calibration mappings and other identifying inputs
in an immutable bundle. Publish its SHA-256 commitment with an independently
witnessed timestamp before confirmation. Bind an independently generated
secret 256-bit random nonce and unambiguous byte lengths into that commitment;
a plain hash of a small public set of possible assignments can be guessed.
After acquisition and before assessment, similarly seal and timestamp the
complete raw corpus and trial roster, including failures and missing records.
Retain original bytes; derived packets never replace raw evidence.

Give the evaluator one uniformly structured packet per opaque random ID,
in an independently shuffled presentation order. Its allowlist is:

- the original 31 target coordinates and p, raw target optical codes/angles;
- target B_2,Z_2,r_2 bank energies, signed local V/I series, net work and
  uncertainties, already converted by the frozen calibration procedure;
- fixed relative step/layer times, target temperatures, necessary local
  validity flags and honest missing-data markers.

Exclude source/middle/channel states, cut locks, routes, source seed,
configuration label, original cartridge serials, absolute timestamps,
acquisition order, operator notes and filenames/log links that expose them.
Use fixed target-role names, not persistent cartridge aliases whose changes
reveal a swap. Strip identifying calibration references and coefficients;
the custodian applies the frozen SI conversion and later discloses its full
inputs for verification. Packet schema, metadata and error vocabulary must
not encode configuration. Keep real target values, length/gaps and defects;
do not fabricate samples or suppress a failed trial to make packets look alike.
Source/route fingerprints may still be inferable from genuine target behaviour;
do not promise statistical indistinguishability of the outcomes.

For EVERY FORWARD-TRIAL ID, the evaluator seals the measured target trace, timing/quality
findings, and TWO separate outcomes, each SATISFIED / FAILED / INDETERMINATE:

1. Positive-target predicate: declared arrival/work/write/reset order,
   all required target coordinate/readout bounds, HIT on boundaries3..10,
   and net first receiving work within the frozen 0.950..1.050 J bounds with
   uncertainty over the whole receiving operation, including back-transfers.
2. Null-target predicate: the prepared target stays unchanged in decoded
   coordinates, p remains 0 through boundary 10, and the frozen per-G and
   whole-horizon absolute target-work limits hold.

Do not choose which predicate is expected from a guessed configuration.
Neither target outcome alone certifies source attribution, initial source
energy equality or the complete 96-coordinate balance. Those require data
deliberately unavailable at this stage.

Seal one complete assessor output covering the entire trial roster, with a
hash and independently witnessed timestamp, BEFORE the custodian releases
any assignment key or full record. Freeze all assessments together, not
trial-by-trial with early unblinding that could inform later decisions.
Then disclose the nonce, keys, committed bundles and full calibration/raw
records. Verify the commitments and recompute the target projection; any
mismatch is a custody failure, not permission to replace a packet silently.

Only now assign the already locked positive/null outcomes to the actual
configuration and perform a separate complete-state and energy-origin audit,
including E_other,upper over the full source-to-target interval. A target
predicate may pass while this full audit fails. The final campaign decision
requires the applicable locked predicate for each forward trial, the separate
inverse-block criteria, and all existing full audit criteria. Never rewrite
a target verdict, threshold or exclusion after
disclosure; any later correction is a separately visible amendment retaining
the original. Accidental early access to revealing records is a declared
blinding breach and cannot count as a valid blind confirmation. Guessing from
the allowed target trace alone is not such a breach.

This is a prospective custody protocol. No sealed data, assessments or
laboratory result are claimed here, and no existing public formal-gate
requirement is waived by it. Its complete implementation and custody route
must be reviewed in the separately owned physical gate before confirmation.

## 6. Inverse and decision rules

In a separate predeclared block use the same four cases and twenty prepared
seeds where applicable. For each distinct prepared input do one 10-step
forward/10-step-inverse run and one 10-step-inverse/10-step-forward run, freshly
prepared. Freeze separate inverse-mode expected tables; the forward
HIT 3..10 timing formula is not asserted for inverse-first runs.
Check all 96 coordinates and physical intervals at every layer and
at return; extend idle, drift and uncertainty qualification to 200 s for these
blocks using the SAME20 mJ idle ceiling, not a doubled allowance. This is a
harder additional requirement. Reject any use of recorded forward history to
drive the inverse. Externally dissipated heat is not required to run backward.

Any incorrect word, invalid wheel code, extra HIT, missed HIT, wrong order,
timing overrun, energy/provenance failure, ADC saturation, missing record,
unbounded auxiliary port or uncertainty over budget is a failed/indeterminate
trial, not success. A campaign passes only with zero failed or indeterminate
trials and all balances inside the stated bounds. Keep exclusions and their
reasons visible; never replace a failed trial with an unreported rerun.

Even success is limited to the tested physical preparation class and clock.
It supplies no all-time empirical null, whole-S42 hardware certificate,
permanent memory, robust repeated reset, or evidence that nature selects the
engineered law. The candidate-T/L1 mathematical result does not depend on
whether this particular implementation passes.
