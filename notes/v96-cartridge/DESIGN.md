# Stage A cartridge and disconnected sensing candidate

NON-CANONICAL / STATIC DESIGN + SOFTWARE / A1 INCOMPLETE / A2 NOT MEASURED.

This note makes the sensing topology and its arithmetic concrete. It does not
release a production drawing, authorize construction, purchase or energization,
or claim that the assembled cartridge can meet the loss limit. The selected D1 prototype now has a full point-to-point netlist, driver,
service heads and dimensioned enclosure. Independent pole-state metrology
and as-built engineering review remain necessary before A1 is complete.
The mathematical and physical limits remain those of #1318 at
`4756a3df650b91fb1d30806b0fb2aaac00e50cc2`.

## Selected electrical topology

The storage element is the original MAL210118223E3. Both sense conductors
disconnect with independent normally-open relays. An idle cartridge has no
charger, load, bleed resistor, common-ground sense conductor, conductive
temperature lead or permanent voltage-divider path attached. Electrical paths
through insulation, housing, open contacts and parasitic capacitances remain
real paths and require measurement. The full removable housing, both storage
terminals and capacitor move together in a future dock; this Stage A fixture
does not implement the five-dock mechanism.

```text
CAP+ -- K_PLUS.NO -- R1 -- R2 -- R3 -- R4 -- R5 -- R6 -- R7 -- R8 -- R9 -- SENSE
CAP- -- K_MINUS.NO ------------------------------------------------------- RETURN
SENSE -- R10 -- RETURN
SENSE -- U1.IN+       U1.OUT -- U1.IN-       U1.OUT -- R11(100ohm) -- DMM.HI
RETURN -- U1.V-       RETURN -- DMM.LO
METERED_ISOLATED_5V -- R12(100ohm) -- U1.V+; C1(100nF) from U1.V+ to RETURN
```

R1..R9 are 10 Mohm each; R10 is 1 Mohm. The nominal divider ratio is 91:1.
The full resistor chain, buffer, cables, relays, instrument range and settling
history are calibrated together; nominal ratio is not a measurement conversion.
Both relays close only for the declared quiet/read sequence. Both open before
idle or movement. Loss of coil supply opens both poles. Physical pole-state
feedback must be independent of the command bit; two commanded OFF values
are insufficient evidence that the terminals disconnected.

The buffer is LMP7721MA/NOPB, using its unusual SOIC pinout:
IN+ 1, V- 3, OUT 4, V+ 6, IN- 8. Connect 2/7 to the output-driven guard around
the input node; 5 has no connection. Power at regulated 5 V. The nominal
input is approximately 0.052..0.549 V for 4.7..50 V at the cartridge.
Single-supply operation does not authorize an unmetered auxiliary connection.
The selected bypass is 100 nF; output isolation and supply limitation are
each 100 ohm. Exact wiring is in NETLIST.tsv and physical layout in BUILD.md.
Cable stability, supply faults and input protection still require review
and measurement of the assembled candidate. Do not substitute a
conventional single-op-amp pinout.
[TI datasheet SNOSAW6E, revision E, December 2014](https://www.ti.com/lit/ds/symlink/lmp7721.pdf).

The relay selection is 104-1-A-5/1D. Its 5 V coil includes a diode, requiring
correct polarity. The source lists 10^12 ohm minimum insulation at 25 C;
2.5 pF switch-to-coil and 0.1 pF open-contact capacitances are typical values,
not certified maxima. Those values do not certify this assembled fixture at
20/23/26 C. Numeric pin orientation was visually checked: contacts 1/7, diode coil
positive 3 and negative 5, referenced to the body pin-1 mark. BUILD.md records
the drawing cross-check. No polarity or top/bottom-view substitution is allowed.
[Pickering Series 104, issue 4.1, May 2025](https://www.pickeringrelay.com/pdfs/104-high-voltage-sil-reed-relays.pdf).

`BOM.tsv` gives exact ordering codes for the selected core. The resistor codes
and 5% tolerance follow [Vishay document 28907, 03-Jun-2025](https://www.vishay.com/docs/28907/vr25vr37vr68.pdf).
The 91 Mohm divider calculation below uses the worst initial 5% low resistance;
temperature, ageing, humidity, surface paths and voltage coefficient require
the assembled calibration/loss bound. Part numbering is independently listed
in [Vishay's product table](https://www.vishay.com/en/product/28907/tab/quality/).

## Concrete D1 prototype and remaining review

`BUILD.md`, `NETLIST.tsv`, `BOM.tsv` and `candidate-layout.svg` specify the
stationary cartridge, keyed shrouded port, three mutually exclusive heads,
point-to-point divider/buffer, ULN2003AN coil driver, CD74HCT221E hardware pulse
backstop, HCT08 logic and two isolated supply channels. The charge/discharge
heads each contain a separate passive 10 kohm chain; neither can remain
connected with the sense head. No energization, purchase or fabrication ran.

The 100 x 100 x 150 mm internal enclosure, 50 x 80 mm bank, 20 mm proposed
vent zone and all selected mounting clearances are design choices pending
engineering review, not manufacturer-approved installation or safety ratings.
Capacitor terminal/lug/screw length must be checked against the delivered part.
[Vishay 28371, 21-Jul-2022](https://www.vishay.com/docs/28371/101102phrst.pdf)
provides the selected capacitor reference. Its catalogue 2.77 mA maximum
leakage at rated conditions is not a working-voltage prediction or a
microampere-scale assembled qualification.

A1 still has a specific external measurement-interface gap: actual two-pole
state and aperture edges need an independent calibrated observation chain,
including wiring and bounded loading/injection. Commands and coil current do
not detect a welded contact. The selected all-dielectric temperature probe
needs a vendor configuration drawing and calibration. As-built fit, venting,
protection, stability and safe service access also require engineering review.
No missing observation is replaced by an invented feedback signal.

## Fixed duty cycle and 20 mJ allocation

Retain the original 10 s clock and read windows ending at G=2, A=4.5, B=7,
F=10 s. The frozen adapter contract requires an observed 200 ms sense interval,
with its final 100 ms serving as the read window. Commands must account for
pickup, bounce and release; physical timing compatibility is not demonstrated.
A revised physical tolerance would require an explicit reviewed contract,
not silent relaxation of the current exact-duration test. Qualification includes the
initial preparation read, conservatively 41 windows/8.2 s on-time at 100 s
and 81 windows/16.2 s at 200 s. The inverse half uses the original reversed
layer windows (ends at 3, 5.5, 8, 10 s), not the forward grid. If the selected
front end fails to settle within 100 ms, this candidate fails; it may not
silently lengthen the read window or alter the experiment clock.

At 50 V and minimum initial divider resistance 86.45 Mohm, the exact
conditional load is 41/172900 J for 100 s and 81/172900 J for 200 s,
approximately 0.237 and 0.468 mJ. `stage_a.py` reproduces this arithmetic.
The capacitor and other components are not qualified by that calculation.

| Allocated contribution | Maximum over the complete 200 s |
| --- | ---: |
| Capacitor loss/relaxation under the frozen history | 14.0 mJ |
| Open-switch, surface and housing paths | 0.5 mJ |
| Connected divider and sense loading | 0.5 mJ |
| Switching/input capacitance transients | 1.0 mJ |
| Possible positive probe/supply injection | 1.0 mJ |
| Propagated uncertainty and unresolved effects | 3.0 mJ |
| Total | 20.0 mJ |

These are proposed allocations, not earned upper bounds. The same total
20 mJ applies at 100 s. At 48.5 V the 14 mJ capacitor allocation over 200 s
corresponds to about 1.44 microampere only as an equivalent-current illustration;
acceptance remains integrated energy with uncertainty. Do not substitute a
current estimate for the energy test.

For each attachment, bound capacitive energy through measured worst-case
capacitance and voltages, including coil/supply coupling in either direction.
The often-used C*V^2/2 describes a simple capacitor transition only; use a
conservative complete switching model or measured signed work for the actual
network. No typical relay capacitance may be promoted to the 1 mJ bound.
Meter or conservatively bound both possible injection and loss. A positive
probe injection is added to the loss upper bound; it cannot cancel dissipation.

## Calibration and acquisition

`keysight_acquire.py` implements actual 34465A SCPI command construction,
identity/firmware hash checks, external triggering, fixed range/NPLC readback,
original response retention, overload and sample-count rejection. The injected
transport is the laboratory's approved VISA/USBTMC/LAN implementation. It has
no default network address and no charging or relay output commands. The
tests inject a permanently SYNTHETIC transport; no device connection occurred.
Commands were checked against the
[Keysight Truevolt operating/service programming guide](https://www.keysight.com/us/en/assets/9018-03876/service-manuals/9018-03876.pdf).

Actual aperture timing, external trigger capture and simultaneous SI V/I
remain independent instrument/DAQ inputs. A fetch timestamp is not the
measurement timestamp. Only NPLC=1 is accepted; NPLC=10 cannot fit the 100 ms read window. Freeze
and verify line frequency and the aperture/trigger policy with the calibrated
clock. Independent measurement-complete timestamps as well as trigger
timestamps and their uncertainty must fit wholly within the final 100 ms. A 100 ms
settled window cannot be certified by a single slow sample. This DMM adapter
alone does not replace the NI simultaneous waveform acquisition or prove
the <=1 ms expanded timing uncertainty.

Keep full identity, specimen/dock, temperature, history, raw response, probe
on-intervals, actual external trigger and measurement-complete timestamps, calibration and protocol
hashes in custody. Failed fetches must retain the original transport response
and initiation record in the independent immutable store; the adapter never
re-arms or replaces a failed attempt automatically. The C96-06 interface is
`../v96-custody/CONTRACT.md`. Conversion to target packets is a later frozen
instrument-reducer responsibility; source IDs never enter target packets.

`calibrated_energy` accepts only a specimen/dock/temperature/history/protocol
specific empirical energy-map table. Its knot uncertainties and interpolation
error must be independently established; it refuses extrapolation, missing
history, non-single-valued maps and nominal-CV2 substitutes. A calibration
builder is not supplied: actual controlled charge/discharge VI measurements,
reference calibration, absorption/hysteresis tests and uncertainty evaluation
are still required. Shared map errors enter the differenced variance through
covariance, not independent RSS by default.

`evaluate_hold` checks the unchanged 100/200 s, preparation/Dec uncertainty
and voltage bounds including voltage_U_V, duty-cycle summary, two-pole isolation, absence of charger,
and loss plus difference uncertainty plus nonnegative injection upper bound.
Its summary inputs must be derived from retained real samples and audited
intervals; the helper does not independently verify continuous behavior from
asserted summary numbers. A numerical SATISFIED result therefore still says
PENDING_AUTHENTICATED_FULL_STAGE_A, and synthetic data say NOT_CONFIRMATORY.
