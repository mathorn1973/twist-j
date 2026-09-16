# Physical registrations: a reusable detector and an exported history

NON-CANONICAL. Primary-source qualification and physical interpretation audit.
No new experimental result, formal verifier run, physical certificate or Canon
promotion. Published conclusions are known; this is retrospective source work.
No raw measurement payload was acquired, opened or reanalyzed in this lane.

Audit: [#897](https://github.com/mathorn1973/twist-j/issues/897), following
[#896](https://github.com/mathorn1973/twist-j/pull/896), based on public main
`a9a990343d9d2f63d67b70fddc4a644858d9bed8`, ACTIVE Public Canon v80.
The [source manifest](C-SNAP-PHYSICAL-REGISTRATION-N.sources.json) distinguishes
published evidence from unissued same-run certificates. Existing owners
[#539](https://github.com/mathorn1973/twist-j/issues/539),
[#830](https://github.com/mathorn1973/twist-j/issues/830),
[#832](https://github.com/mathorn1973/twist-j/issues/832) and
[#834](https://github.com/mathorn1973/twist-j/issues/834) retain their scopes.
The resource constraint remains public sources only, without a new laboratory
acquisition or hardware purchase.

## 1. The physical answer that the evidence supports

Two registrations need not use two newly manufactured detectors. A reusable
sensor can export a signal, recover its operational readiness, and respond
again while downstream apparatus retains earlier information. Equality of a
local ready-state description therefore does not establish equality of the
complete sensor, source, clock, memory and environment configuration.

This is an interpretation of the external evidence in section 2, not a native
TWIST-J realization theorem. Operational recovery also does not demonstrate
exact microscopic recurrence. Conversely, different file offsets alone prove
neither two incoming photons nor two independent physical trials.

The question must distinguish four stages:

```text
source opportunity / incoming physical field
    -> detector response
    -> electrical registration accepted by the acquisition system
    -> retained, subsequently readable record.
```

An external clock can distinguish opportunities with no registered detector
response. A detected signal can fail to reach storage. A stored row can be
reread without becoming a second registration of the original input. These
possibilities must have separate types and independently specified coverage.
They cannot be collapsed into one count called "the number of events".

## 2. Concrete primary evidence, with its actual limits

**Registration chain (S1).** Shalm et al. describe SNSPD detection followed by
amplification and time tagging; their analysis assumes the outcome is fixed at
time-tag registration. Synchronization defines local trials separately from
detector signals. Background registrations are included in the apparatus
account. This documents an external mechanism and its adopted endpoint, not a
proof of universal measurement terminality.
[Paper, p. 250402-4 and start of p. 250402-5](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.115.250402).

**Different components (S2).** The supplement distinguishes Alice's MoSi and
Bob's WSi SNSPDs, their signal path through amplification and a comparator,
and the time tagger. The approximately 55 ns recovery discussion concerns a
different component, the photon-sampling random-number generator's SPAD.
That number is not a calibration of either measurement SNSPD.
[Supplement, sections II and III](https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.115.250402/LHFSupplementary.pdf).

**Detector reuse under intervention (S3).** Kerman et al. vary optical
pulse-pair separation with a delay line. NbN detector signals toggle a flip-flop;
an oscilloscope selects pulse widths matching that separation. Given two
accepted triggers, two ideal toggles restore the bit while the exported waveform
distinguishes the intervening responses: this is stronger evidence than two
file addresses.
Their circuit model has bias-current recovery time constant `L_k / 50 ohm`.
Recovery concerns responsiveness, not exact microscopic recurrence.
The pulse pairs used roughly 70 or 220 incident photons per pulse, a
Poisson-model conversion to single-photon efficiency and a small timing offset.
They are not individually heralded photons. Their parameters do not calibrate
the different NIST devices. No curve was digitized or refitted here.
[Paper, pp. 111116-1 to 111116-3, Fig. 3 and notes 21–23](https://qnn-rle.mit.edu/documents/kerman-published-version-2006.pdf).

**Storage boundary (S4).** The NIST format describes channel/time/transfer
words, an external 10 MHz clock reference and transfers from buffer to disk.
It also flags an incorrect timing correction in the run3 acquisition used by
the existing bounded adapter. Neither a transfer counter nor a final file
certifies complete loss-free acquisition, physical memory capacity, or
readback interleaved with acquisition.
[Provider documentation, pp. 1–2](https://www.nist.gov/document/bell-test-data-file-folder-descriptions).

These sources support different legs in different experiments. Combining
their descriptions does not produce one jointly calibrated apparatus. The
existing [NIST contract](NIST-MEASUREMENT-CONTRACT-1.md) accordingly retains
unresolved same-run clock, coverage, response, instrument and source gates.

## 3. What "fresh" means physically in this candidate

The earlier [isometric loader result](../probes/P-SNAP-INTERACTION-READBACK-1/PROOF.md)
concerns an exact linear map that preserves an arbitrary old record and moves
an arbitrary new vector into a protected sector. Its fresh isometric sector
is necessary within that class. It does not require a newly built detector
for each registration, nor a new physical particle for every stored bit.

For a reusable detector and external memory, distinguish:

| Resource | Physical role to establish | What is not established by a row label |
|---|---|---|
| Prepared source or incoming mode | Supplies the new interaction opportunity | That a source photon actually arrived |
| Bias, cooling and readout circuit | Supports response and recovery | A cold, isolated two-port energy transfer |
| Timing/reference system | Distinguishes admitted intervals | Native U time or exact global ordering |
| Buffer and storage | Carries distinguishable retained record states | Unlimited capacity or zero loss |
| Later readout apparatus | Recovers the retained observable | No microscopic disturbance anywhere |

The interpretation is distributed: the sensor may be reusable while history
is retained elsewhere. A local reset need not erase an exported record.
An archive that preserves the past does not reveal whether its upstream sensor
stored an append-only history or reused a small transient state. The
[open-data bridge](DECODER-OPEN-DATA-BRIDGE-1.md), section 6, already requires
sequential evidence before identifying a post-state or reset law.

At a chosen finite experimental horizon, "fresh capacity" means sufficient
distinguishable record states under the declared encoding, retention time,
readout accuracy and allowed compression. It is not a claim that material is
created at each event. Exact ordered arbitrary histories, a count of identical
responses and a lossy summary are different retention contracts. Their storage
requirements must not be interchanged. No universal energy-per-event or
Landauer bound is asserted by this audit.

The active signal chain also changes the energy boundary. Bias circuitry and
amplification are additional physical resources. Our inference is that the
electrical registration signal cannot simply be identified with the incoming
optical energy in the isolated cold-reservoir equation. A proposed energy
comparison must account for the supply, internal energy, output and losses.
This does not refute conservation, the mathematical reservoir theorem, or the
possibility of a larger physical realization.

## 4. A presence flag needs a physical carrier

In #896, `BLANK` and `occupied(0)` are different mathematical cell states with
the same assigned payload amplitude and payload energy. That distinction was
explicitly supplied; it was not derived from the amplitude.

The same boundary matters physically. If two preparation descriptions supply
exactly the same state to all accessible ports and the same apparatus context,
the description labels cannot by themselves change the apparatus response law.
This does not require identical realized outcomes on repeated preparations.
A proposed difference needs a physical carrier: for example, an independently
recorded trigger, a herald, a clocked slot, or another distinguishable degree
of freedom. The carrier's coupling and calibration remain obligations.

In particular, a trigger can record **an attempted preparation with no detected
signal**. It does not prove a zero-energy object arrived. Nor does a measured
zero of one amplitude observable establish the complete physical state or
absence of all excitations. This audit does not identify the mathematical
payload zero with optical vacuum, or its occupancy tag with a free physical bit.

Consequently, batch identity, preparation identity, accepted electrical
registration and photon attribution must remain distinct. A detector click
requires an attribution/response model before it can be counted as a photon
from the intended source. A missing click requires live-coverage evidence even
to mean no registration; it still need not mean no incoming photon.

## 5. A testable operational Snap proposal

The proposed physical boundary is **creation of a retained registration by a
specified coupling**, with an explicit relation to its preparation and timing
context. It is a profile for testing, not an ontology already derived from U.

Keep three separate operational comparisons:

1. `ReadyCompatible`: operational response within independently calibrated
   tolerance, including the relevant recovery/memory variables. Proximity
   within a tolerance need not be transitive and is not an equality relation.
2. `RegistrationEq`: same admitted acquisition transition, with provenance and
   a physical timing/coverage contract. Identical pulse shapes need not imply
   equal registrations; different row indices do not alone establish different
   physical transitions.
3. `RecordEq`: same retained item and its lineage under a specified readback map.

These are proposed roles, not a completed replacement for #539's schema. Before
admission, separately freeze exact readiness equality or an explicit partition,
and bind registration and retained-history identities to the existing
`EventRecordEq` and history-equality obligations, including their decision rules.

For two equal-valued responses separated by a recovery interval, the desired
test is that two distinct admitted registrations create distinguishable retained
items while the earlier item remains readable. Rereading that earlier item
preserves its registration identity. A read operation may itself create a new
physical response and a new read-audit record; its event type differs from a
fresh registration of the original optical input.

This answers the local-state puzzle conditionally: equal local readiness can
coexist with distinct input couplings and different retained histories. It does
not settle whether two exactly identical **complete substrate states** are two
different physical events. The native full state already includes its advancing
counter; checkpoint recurrence is not full-state recurrence. Physical
interpretation of that counter still requires the named decoder bridge.

The proposed Snap is also narrower than "every physical event leaves a
permanent record". Records can fail, decay, be erased or remain inaccessible.
Persistence is a measured or stipulated property over a declared horizon, not
absolute irreversibility or a solution to the quantum measurement problem.

## 6. Qualification matrix for a public-data test

The next numerical target should be one **same-apparatus sequential response
and retention test**, using an existing public acquisition. The table freezes
what evidence would be relevant; it does not admit new data or run a gate.
S3 already supplies published recovery evidence for its stated setup. It does
not supply the complete joined test below, and the inspected NIST material
does not complete it either. This is not an exhaustive claim about all public
archives.

| Leg | Required independently supported input | Decisive comparison | Present disposition |
|---|---|---|---|
| Preparation | Pulse-pair or herald/trigger schedule, physical source model and timing bounds | Separate opportunity, actual input and registration | S3: controlled optical-pulse evidence; no individually heralded inputs admitted |
| Recovery | Same device, bias, temperature, load, response calibration and latency model | Second-response law versus separation at frozen settings | S3: published result; no new replay or NIST transfer |
| Acquisition | Same-run wiring, discriminator, tagger build/configuration and live intervals | Accepted electrical transitions versus emitted records, with multiplicity | NIST description available; complete same-run certificate absent |
| Capacity/loss | Buffer extent, overflow/drop accounting, stopping/export rules | Claimed accepted transitions all accounted for inside the declared extent | Not established by the inspected archive |
| Retention | Named memory boundary and old-item readback before/after later writes | Earlier decoded item unchanged under `RecordEq` over the specified horizon | No such interleaved physical readback evidence admitted |
| Source attribution | Background, efficiency, recovery, multipulse and coverage model | Source-specific outcome prediction rather than raw row count | No TWIST-J physical prediction admitted |

For a future numerical attack, fix the source version and input selection from
documentation, then freeze the observation adapter, parameters, calibration
partition, uncertainty bounds, exclusions and failure threshold before opening
the accepted measurement payload. If published calibration and test data are
already exposed or shared, do not call them independent or blind. Any model
conversion used in the source must be retained as an assumption, not promoted
into an observed fact. Numerical predictions require the separate public
preregistration and accepted verifier required by POLICY.md.

A proposed **memoryless, instantaneously ready detector** can be challenged by
a calibrated dependence of the second response on pulse separation, after
accounting for source changes and timing electronics. A proposed **lossless
retained-record profile** can be challenged by a documented accepted transition
missing from its claimed record extent, or by a failed promised readback. Those
are falsifiers of named physical profiles. Missing calibration instead leaves
the corresponding comparison undefined.

Counts alone cannot localize storage. Final archive equality therefore cannot
choose between competing internal-memory and exported-memory realizations.
The purpose of sequential controls and a declared physical boundary is to make
that distinction testable, rather than selecting a preferred story afterwards.

## 7. Disposition for TWIST-J

The physical progress is a concrete external mechanism and published recovery
evidence: reusable sensing plus exported information is a viable candidate
architecture. The inference "every new registration requires a fresh complete
detector" is not warranted by the earlier loader theorem. Neither is the
identification of a software presence tag with physically distinguishable
zero input. These are corrections to candidate interpretations, not new
registered falsifications or a new empirical result of this project.

The [passive optical design](DECODER-PASSIVE-REALIZATION-BRIDGE-1.md) remains a
different, unbuilt finite-mode proposal. The
[reservoir physical profile](DECODER-RESERVOIR-PHYSICAL-PROFILE-1.md) still
requires physical source preparation, fresh ports, calibration and record
realization. Native U has not supplied those resources through a certified
physical map. No Born law, event probability, new spatial dimension, unique
Snap, or universal measurement cut follows from the external detector papers.

Status: **external mechanism documented; same-run joined test not admitted;
native physical bridge STOP-DEFINITION; Public Canon v80 unchanged.**
