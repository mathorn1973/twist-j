# Physical apparatus profile: an ion implementation of the code and port writer

**PUBLIC; engineering proposal supporting a candidate-T, L1 probe;
NON-CANONICAL. Hardware experiment: NOT_RUN.**

This profile specifies an apparatus to build and test. It does not report a
device built by this project, laboratory access, acquired data, or an earned
L1-to-L5 bridge. The equations and pulse compiler elsewhere in this probe
describe an ideal controlled interaction. Their exact verification is not a
measurement of the apparatus described here. `QDD-INSTRUMENT-APPARATUS [O]`
retains the physical obligations.

## 1. Target and carrier choice

The target is the coherent four-label code with its entire five-state native
port, followed by transfer to a separate five-state archive. The working
dimensions are therefore source 4, port 5, and archive 5: 20 states before the
archive is included, and 100 joint internal states afterwards. These are the
declared code/chart domains, not all of the native checkpoint space.

Choose three active trapped calcium-40 ions. One stores the four source
labels, one the port, and one the archive. Each has an auxiliary ground state;
the shared axial centre-of-mass motional mode supplies the temporary coupling
carrier. Its ground-state preparation is a physical input, not an automatic
consequence of the internal-register preparation.

For this proposal, fix five storage states in the metastable
`3D5/2` manifold with magnetic quantum numbers

```text
logical index        0       1       2       3       4
magnetic quantum m  -5/2    -3/2    -1/2    +1/2    +3/2
auxiliary ground state: 4S1/2, m = -1/2
```

The source uses four declared storage states and treats the remaining state
as outside its code. The local label assignment must agree with the frozen
compiler; a later experimentally convenient reassignment requires an explicit
conjugation of preparation, pulses, and analysis. It cannot silently change
the tested map. Unused magnetic sublevels are leakage states unless the
profile expressly assigns them another function.

There is a direct experimental precedent for the ingredients. Meth et al.
demonstrate three five-level ion registers, storage in the `D5/2` manifold,
and conditional operations through an auxiliary `S1/2` state and the axial
centre-of-mass mode. Appendix A gives the carrier/blue-sideband construction;
Appendix G explains encoding, Stark-shift compensation, and addressing
limitations. In particular, the simple spectral separation used for neighbouring
three-level registers does not extend to five-level registers. Their experiment
uses extra buffer ions. This supports the carrier and interaction family,
not successful operation of the present writer.
[Meth et al., version 2, Appendices A and G](https://arxiv.org/html/2310.12110v2)

Our build specification therefore allows extra buffer ions between active
registers. Their number and state must be declared before the hardware test;
they alter the mode spectrum and cannot be omitted from calibration. Three
active ions does not mean an unconditional three-ion hardware bill.

## 2. Interaction and the origin of control

The actual resources are the trapping fields, Coulomb-coupled ion motion, a
phase-stable 729 nm manipulation laser, and individually addressed carrier
and motional-sideband pulses. The coherent interaction is the laser-driven
electric quadrupole transition together with the selected normal mode. The
Hamiltonians and phase conventions in this probe specify the ideal model.
Their use requires resolved transitions, sufficiently small motional
excursions, controlled spectator modes, and calibrated pulse areas.

The register is not assumed to have a flat physical energy spectrum. The
Zeeman energies and optical reference determine free phases. A comparison
with the ideal writer is made in one declared interaction picture, with
independently measured free evolution and Stark shifts. A phase register
updates subsequent pulse phases; it is not permission to fit unexplained
HIGH phases after observing the target result.

Schindler et al. document the relevant laboratory control chain: a computer
loads a pulse sequence into an FPGA; direct digital synthesizers drive
acousto-optical devices controlling the laser fields. Their apparatus also
provides optical pumping, motional cooling, and fluorescence detection through
a photomultiplier or camera. The documented calcium wavelengths are 729 nm
for coherent manipulation, 397 nm for fluorescence, 866 nm for repumping the
detection cycle, and 854 nm for depletion of `D5/2` during appropriate reset
or cooling operations. Those reset beams are not harmless to stored data.
[Schindler et al., Sections 1.2, 2.2–2.4](https://arxiv.org/pdf/1308.3096)

For this proposed apparatus, the laboratory oscillator supplies the timing
reference; the laser and electronics supply energy, phase coherence, and the
pulse program. These resources are external physical systems. The native
counter labels the comparison schedule but does not derive this oscillator,
choose a laser frequency, or supply its electrical power. Neither the ion
Hamiltonian nor the stored control program is derived from `J`.

This separate engineering profile declares

```text
comparison_kind: external_controlled_intervention
checkpoint_modified: true
canonical_decoder_profile_submitted: false
```

It does not claim `feeds_U=false`. The writer actively changes the port. A later restoration
of the free checkpoint does not turn the intervention into passive reading.
The hardware does not spontaneously execute native `U`; any chart evolution
implemented by pulses must be listed as an additional controlled stage.

## 3. Build requirements and records to freeze

No procurement or laboratory contact is part of this record. Before a hardware
run, a laboratory must supply a concrete device and complete the following
requirements on that same device:

| Subsystem | Required information before data acquisition |
|---|---|
| Trap and ion string | Active/buffer ion order; trap settings; measured mode frequencies and mode participation; ion addressing map |
| State identification | Resolved transition frequencies, polarizations, selected storage and auxiliary levels, leakage channels |
| Manipulation | Carrier and sideband Rabi calibrations for each used transition; pulse envelopes, durations, areas, phases and detunings |
| Phase reference | Clock/reference identifier, synchronization procedure, free-phase convention, measured drift, spectator Stark corrections |
| Preparation | Pumping sequence, motional cooling sequence, ground-state occupation estimate, preparation checks and their disturbance |
| Readout | Collection geometry, detector settings, count windows, dark/bright distributions, leakage discrimination and fixed decision rule |
| Reset | Which register each beam can affect, energy-removal path, recooling procedure, retained-source disturbance test |
| Data custody | Sequence/compiler version and hashes, immutable calibration bundle, raw shot records, analysis version and outcome labels |

The numerical tolerances, sample counts, confidence procedure, readout
thresholds, and acceptance decision must be registered before the proposed
hardware experiment. They are not supplied by the exact-arithmetic verifier.
Missing device parameters mean `NOT_RUN`, not a passed feasibility gate.

Each attempted shot must retain its preparation setting, declared native
counter and reference-port context, controller timestamps, calibration-bundle
identifier, pulse-program hash, raw photon counts or camera samples, initial
readiness flags, leakage/ion-loss flags, final classification, and archive
write acknowledgement. Failed preparation checks and detector failures remain
in the attempt ledger. Report both unconditional performance and any explicitly
conditioned performance, including the conditioning probability.

## 4. First experiment and sequence boundary

The first hardware target is the writer alone. Its proposed compilation uses
**28 pulses: 14 blue-sideband pulses and 14 carrier pulses**. These counts are
properties of this probe's construction, not published experimental performance.
They exclude preparation, calibration, analysis, fluorescence, reset, and any
additional compensation pulses required by a real device.

An unoptimized complete coherent transfer construction requires
**266 blue-sideband and 58 carrier pulses**, with further waiting and sign
handling where the protocol demands them. A pulse count is not a duration.
Use the calibrated duration of every transition, addressing delay, and
compensation interval to construct the physical schedule. Coherence and
motional-heating budgets may make the full sequence impractical even when the
writer succeeds. Feasibility is currently unknown.

| Stage | Physical action | Required observation or boundary |
|---|---|---|
| Prepare | Load and cool the string, optically pump, transfer to declared storage states, prepare the selected source and port input | Retain failures; establish the motional and auxiliary-state assumptions |
| Write | Apply the frozen 28-pulse sequence with calibrated phases | Compare the complete source-port output, not only its populations |
| Diagnose | On separate shots, perform analysis rotations and final state detection | Reconstruct the writer's action and leakage without treating tomography as part of the retained-source protocol |
| Extend | Only after the writer gate passes, add declared waiting and archive transfer | Check the full native-chart comparison and return of auxiliary motion |
| Emit and append | Read the archive register, classify the physical detector record, append it to durable storage | Distinguish LOW, HIGH, invalid/leakage and failed acquisition |
| Persist and reset | Retain the external record; restore the declared port/archive readiness | Test retained-source disturbance separately from fresh-source preparation |

Preparing a known mathematical input is not capturing an independently
occurring source. The first experiment tests controlled inputs: basis states,
HIGH superpositions, and LOW/HIGH superpositions. A later source-acquisition
claim needs its own preparation and sampling contract.

## 5. Readout, archive and retention

After coherent transfer, the archive ion is the quantum pointer. Its expected
storage labels are the two declared record values. To read it, a selective
carrier transfer can bring a chosen archive label to the `S1/2` manifold,
followed by 397 nm fluorescence with the detection repumper. Source and port
are kept in `D5/2` storage levels.

In the ideal level model those retained states do not participate in the
resonant `S1/2`–`P1/2` fluorescence cycle. That observation is not a measured
absence of back-action. Scattered light, unintended addressing, spontaneous
decay, phase noise, and motional heating must be tested on the retained source.
Global 854 nm light must not be used while claiming preservation of the
stored source.

A single dark result cannot distinguish a valid dark archive label from every
other storage or leakage state. The apparatus must qualify archive-label
discrimination, for example by separate label-selective detection windows on
the archive, or explicitly classify unresolved shots as invalid. Analysis
must not convert an unverified dark event into HIGH by definition. Resolving
the archive's two valid labels does not require resolving the three source
states inside HIGH.

The photodetection record is transferred to ordinary electronic storage.
This creates a macroscopic archive with a different physical carrier from
the temporary ion pointer. Store the raw detection record as well as its
classification. Its persistence requires an independently tested storage
procedure and retention interval; it does not follow from the unitary pulse
identity. The metastable ion pointer likewise has a finite retention budget.

Reset after a realized, recorded outcome can dissipate energy and entropy to
the environment. It must not be represented as a reversible erasure of the
only copy of the outcome. If the same coherent source is retained for another
reading, archive reset and motional recooling need an additional source
disturbance qualification. Resetting all three ions prepares a new trial and
does not establish repeatability on the previous source.

## 6. What must actually be tested

Population truth tables alone cannot establish the proposed writer. On the
source subspace, all three HIGH pairs must be tested in both relative-phase
quadratures. There must also be tests of coherence between LOW and HIGH
before irreversible archive detection, with joint source-pointer analysis:
tracing over the pointer would intentionally hide that coherence.

The contractual writer domain includes all five port inputs. Characterization
must therefore cover the source-port operation on the complete 20-dimensional
code/chart domain, including coherent port inputs and source-port correlations.
The later archive transfer extends the claimed domain to 100 dimensions;
testing only a blank archive cannot establish a claim made for arbitrary
archive inputs. Informationally complete preparation and analysis, or a
separately justified certification method for the stated channel class, must
be fixed before the experimental data are used to infer channel fidelity.

Use matched-duration free-evolution controls and independently calibrated
analysis rotations. Include tests of residual auxiliary-level population,
residual motional entanglement, mode heating, spectator-state phases, and
addressing errors. Compare phases using the frozen reference convention.
The experiment must account for ion loss, failed cooling/preparation checks,
leakage, missed or ambiguous photon counts, and incomplete electronic writes.

After archive detection, the operational preservation target is the conditional
source state and its HIGH coherences, together with the declared native point
or chart comparison. The original uncorrelated source-pointer state is not
restored by recording an outcome. Repeated readings of one retained source
are not independent preparations and must not be counted as independent
draws from the QDD weight.

The count law of actual outcomes remains an empirical claim for a declared
preparation ensemble. Standard quantum measurement theory can supply a
conditional laboratory model; importing it does not derive the occurrence law
from native `U`, or discharge the Canon's physical registration obligation.

## 7. Why this carrier, and what remains open

This ion choice preserves a distinct five-state port and five-state archive
while using a demonstrated multilevel interaction family. It is not a proof
that ions are the cheapest possible apparatus. A superconducting cavity with
a transmon provides another serious carrier for a narrower target: encode
LOW in an odd Fock state and the three HIGH states in distinct even Fock
states, then use a Ramsey parity interaction. Repeated nondestructive parity
measurements have been demonstrated. That compressed realization does not by
itself implement the present full five-state native-port comparison.
[Sun et al., parity-measurement experiment](https://arxiv.org/pdf/1311.2534)

The present profile owns a concrete proposed carrier, a physical interaction
family, an external source of control, and a testable first experiment. It
does not own successful hardware execution, universal apparatus-family
completeness, a native origin for the control fields, a derived physical time
scale, or a new occurrence law. The next material evidence must be a named
laboratory device, its frozen calibrations and schedule, and the resulting
unfiltered experimental records. Until then the hardware status is
**NOT_RUN**, and the physical bridge remains open.
