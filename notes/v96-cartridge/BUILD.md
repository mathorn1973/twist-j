# C96-A1-D1 prototype construction candidate

NON-CANONICAL / ENGINEERING REVIEW PENDING / NO PHYSICAL PASS.

The point-to-point candidate is specified in `BOM.tsv` and `NETLIST.tsv`.
This is a design, not a construction record, purchase order or permission to
energize hardware. There is no released PCB or qualified enclosure. D1 must
receive electrical, mechanical and protection review before the first build.
Any later change needs a new as-built/calibration pin.

## Wiring and disconnect

A netlist row joins its listed terminals, except the explicitly marked series
service chains and no-connect lists. Use manufacturer TOP VIEW pin numbers.
Check every pin/net and no-connect with a recorded continuity worksheet.

Pickering Type1 contacts are 1/7; diode coil is +3/-5. Locate pin1 by the body
mark; populated pins are 1,3,5,7, approximately5.08mm between populated leads.
The current specification is [Series104 issue4.1, May2025](https://www.pickeringrelay.com/pdfs/104-high-voltage-sil-reed-relays.pdf).
The pin drawing was also visually checked in a manufacturer-authored
[older drawing hosted by Rapid](https://static.rapidonline.com/pdf/565695_v1.pdf).
Use the current document for ratings, not the older drawing's different values.

Build the divider point-to-point on a120x80x3mm PTFE plate; two rows of five
supports at20mm pitch, joints8mm above the plate. Keep unrelated conductors
at least10mm from high-impedance joints. These are chosen layout controls,
not certified insulation distances. No flux-coated board or unguarded solder
mask lies under SENSE. Qualify cleaning/drying and record blank-fixture leakage.

Place U1 on an18x18mm SOIC breakout island with pin1 raised from ordinary
perfboard. Surround SENSE/R10 high end with FOLLOWER guard, including U1 pins2/7.
Keep input/feedback wires<=10mm and C1 within5mm of supply pins. U1 pin5 is
isolated. R11=100ohm follows the feedback junction; R12=100ohm precedes100nF
bypass. No SENSE clamp diode or input capacitor adds an unaccounted path.
The nine10Mohm series resistors limit normal50V input current below0.6uA;
this does not establish transient immunity or single-fault protection.
Required qualification includes unpowered input, rail startup, overload
recovery, input faults and output-cable stability.

Use a separate100x80mm control perfboard, at least30mm from SENSE. C2 bypasses
coil rail near U2 COM; C3/C4 bypass U3/U4. Twist coil pairs away from the divider.
Fit every pulldown and ground unused logic inputs. The one-shot has390kohm
from rail to pin15 and ten parallel100nF between pins14/15. Positive Q is13,
inverted Q is4. Its nominal pulse is about273ms; actual limits require
measurement. [TI CD74HCT221 SCHS166F](https://www.ti.com/lit/ds/symlink/cd74hc221.pdf)
and [CD74HCT08 SCHS403A](https://www.ti.com/lit/ds/symlink/cd74hct08.pdf)
define pins and functions.

The DAQ REQUEST is optically isolated, never connected directly to HCT inputs.
U6 SN74LVC1G17DBVR runs from the DAQ-side 3.3 V (+/-5%) rail and drives U5
VO617A-4 LED through R20=120 ohm. DAQ-side ground has no coil/sense ground bond.
U5 collector pin4 is supplied only by COIL_5V2; emitter pin3 has R15=10 kohm
to C_GND and feeds U7. U7 is another SN74LVC1G17DBVR, powered by COIL_5V2,
which restores fast Schmitt edges before U3/U4. U6/U7 pins are NC1,A2,GND3,Y4,
VCC5; each has100nF local bypass. R21/R22 pull down the receiver output and
DAQ input respectively. The DAQ3.3V supply must provide40mA; a GPIO does not
source LED current directly. No direct electrical path can power the coil
rail from a high DAQ request. Loss of the coil supply removes the source for
both opto transistor output and receiver; the normal no-weld coil release
still needs physical verification. Test both power-up orders, lost supplies,
open input and stuck input; no oscilloscope ground may bridge the isolation.
At3V supply the buffer's guaranteed2.3V output with24mA load leaves at least
about5.36mA through120ohm at1.65V LED drop and1% high resistance; optical response,
aging and20/23/26C behavior are nevertheless qualification inputs. The opto's
typical transition delays are not timing ceilings. The Schmitt receiver avoids
passing a slow opto edge into ordinary HCT inputs.
[TI SN74LVC1G17 SCES351Y](https://www.ti.com/lit/ds/symlink/sn74lvc1g17.pdf)
and [Vishay VO617A document83430 Rev2.8](https://www.vishay.com/docs/83430/vo617a.pdf)
are the interface references. The optocoupler's component isolation rating is
not an assembled safety qualification.

U2 sinks each coil separately. Coil-rail loss, LOW REQUEST or LOW one-shot Q
removes coil drive. A sustained HIGH request cannot indefinitely extend one
pulse. Opening either arm/lid switch resets the one-shot. These parts do not
detect welded contacts or shorted drivers. Arming with REQUEST high can
trigger: verify REQUEST LOW before power/arming and before fitting the sense
head. This is not a safety-rated or single-fault-tolerant disconnect.

The frozen numerical adapter currently requires exactly200ms observed probe
intervals, with independent trigger and measurement-complete timestamps plus
uncertainty wholly within the final100ms read interval. Only1NPLC is allowed.
Physical pickup/bounce/release must fit that contract; command bits are not
the interval observations. A practical tolerance or shorter on-duration needs
an explicit frozen interval contract and a new reviewed adapter revision,
never a silent reinterpretation of the present equality check. D1 has not
demonstrated physical compatibility. The hardware backstop must cut off in
205..400ms across20/23/26C and supply tolerances; X7R bias/temperature effects
are measured. Backstop use invalidates the hold. Repeated requests still need
independent observation. No failure may lengthen the scientific read windows.

## Supplies and service heads

Prospective PS1 E36312A settings: channel2=5.20V,50mA limit,OVP5.4V;
channel3=5.00V,10mA limit,OVP5.2V; channel1 OFF. No tracking, series/parallel
connection or deliberate common negative. Verify limits, channel/chassis
leakage and shutdown as part of the assembled energy boundary. R12 alone
limits a5.2V rail short to about52.6mA with1% low resistance; it is not an
independent overvoltage limiter. [E36300 reference](https://www.keysight.com/us/en/assets/7018-05629/data-sheets/5992-2124.pdf).
No supplied code enables the outputs.

The Darlington coil drop requires measured pickup/release at all conditions.
The5.2V rail gives nominal headroom; neither a typical driver drop nor the
relay's25C pickup figure certifies the assembly.
[ULN2003A SLRS027T](https://www.ti.com/lit/ds/symlink/uln2003a.pdf).

Three heads fit the single keyed port, mutually exclusively:

* SENSE contains only the dual-pole measurement connection.
* DISCHARGE contains ten1kohm,0.6W MRS25 resistors in series across its two
  plugs, with no bypass or switch. At50V and1% low total resistance, dissipation
  is below0.253W. Mount resistors10mm apart in air inside a100x60x40mm vented
  polycarbonate service box, on insulating supports.
* CHARGE contains a separate ten-resistor10kohm series positive path and a
  direct floating negative lead. PS_CHARGE E36105B is preset<=49.0V,5mA limit,
  OVP49.5V. Verify these limits and their uncertainties before laboratory use;
  preparation setpoints come from the empirical map. Its
  [60V model rating](https://www.keysight.com/us/en/assets/7018-05830/data-sheets/5992-2437.pdf)
  does not change the experiment's50V limit.

Both service heads have covered insulated capacitor-side test lugs for
DMM_SERVICE. All service leads leave with the head before a hold. Discharge
acceptance requires independent |V|<1V observation and a recheck after the
preregistered recovery wait. A countdown is insufficient: ideal22mF/10kohm
would take about861s from50V to1V, but absorption and capacitance uncertainty
defeat that as an access criterion. The physical lab must approve the access
and recovery-wait procedure for the actual specimen.

## Dimensioned stationary prototype

Coordinates: internal lower-front-left origin; x right, y rear, z up. All
dimensions mm. Internal100x100x150;3mm clear polycarbonate walls; outside
nominal106x106x156. This is a stationary cartridge, not the five-dock mechanism.
Material batch/flame rating and safe tool access remain engineering review.

| Item | D1 choice |
| --- | --- |
| Base/lid |106x106x3, two pieces|
| Front/back |106x150x3, two pieces|
| Sides |100x150x3, two pieces;10x10 bonded corner strips|
| Bank |axis x50,y50; lower face z20; nominal diameter50,height80|
| Vent keep-out |above bank to z125, radius30; no wire/clamp across vent|
| Cradle |PEEK70x70x8, centre x50,y50; radius25.5 recess,depth3|
| Retainer |split PEEK collar ID51,OD64,height10 at z40..50; four M3 nylon screws on cradle standoffs; no can compression|
| Bank jacks |front y0; centres x35/z130 and x65/z130; red left|
| Jack holes |diameter0.472inch=11.9888 per Pomona drawing; trial-fit|
| Asymmetric key |PEEK tongue6x8x12 centred x20/z130; only left recess|
| Head carrier |PEEK90x40x30; plug axes30apart; captive4933 plugs; key recess6.4x8.4x12.5|
| Head retention |captive M3 nylon screws at x10/z112 and x90/z112 into insulated bosses|
| Vent slots |rear wall40x4 centred x50/z130 and x50/z140, offset insulating baffle; not sealed|
| Lid fastening |four M3 nylon corner screws; head carrier blocks lid removal|
| Sense box |internal260x160x70;3mm polycarbonate; separated divider/control plates|

Pomona72930 has M4x0.7 terminal nut, maximum terminal-nut torque30Ncm.
Component ratings do not qualify the full cartridge or converter currents.
These dimensions were visually checked in its
[drawing](https://www.pomonaelectronics.com/files/datasheets/panel-mount-iec61010-4mm-0-16-in-jack-for-sheathed-plugs.pdf).
The [4933 plugs](https://www.pomonaelectronics.com/sites/default/files/d4933_100.pdf)
accept18AWG. Trial-check their full mating/shroud coverage together; shared
nominal4mm size alone is insufficient. Use18AWG stranded copper/PTFE wire
rated>=300V. Cartridge leads are<=120mm with strain relief, no exposed joints.

Verify C_BANK terminal thread, permitted lug stack and torque against the
actual delivered variant and archived [Vishay28371 drawing](https://www.vishay.com/docs/28371/101102phrst.pdf)
before choosing screw length; a screw must not bottom in the capacitor.
The20mm vent keep-out is a proposal, not a verified manufacturer clearance.
`candidate-layout.svg` visualizes the selected envelope.

S_ARM uses a captive PEEK slider; S_LID is actuated by the sense-box lid.
Use manufacturer C/NO markings; insulate NC. Adjust and record roller stops
from the switch operating-position/overtravel drawing on the fitted assembly.
The [SS-01GL2](https://www.fa.omron.co.jp/product/item/SS-01GL2/)
is the gold-alloy microload version, not the SS-5 general-load substitute.

## Precisely remaining external inputs

Temperature topology: enclosed Luxtron m924, all-dielectric STF surface probe,
2m lead, calibration covering20/23/26C. Retain it against the can with a PTFE
strip under the loose collar, outside the vent. Manufacturer literature gives
[model and compatible probe family](https://www.advancedenergy.com/getmedia/8aecd484-a0b2-445b-8126-ae709e5b945d/en-fot-m924oem-data-sheet.pdf)
but no fully configured SKU/connector drawing for this length/calibration.
Vendor configuration sheet, lab interface and calibration are required;
no imaginary ordering suffix is supplied. Optical heating/contact bias enter
the uncertainty budget; catalogue accuracy is not a calibration certificate.

Independent acquisition must observe actual two-pole conduction/opening and
aperture edges with expanded timing uncertainty<=1ms, quantify all additional
probe paths/signed energy exchange, and bind original samples/calibrations
to immutable custody. GPIO requests, coil current and synthetic pole flags
do not prove contact state. The lab has not supplied that independent
observation chain, its wiring and uncertainty evidence. This is a genuine
remaining measurement-interface design gap. Along with mechanical/protection
review, it prevents an A1-complete claim; no physical A2/PASS is claimed.

The unmet A1 item is a measurement **topology**, not merely a missing PASS
certificate: a voltage/continuity witness connected across an open relay
creates a parallel electrical path, while a coil/Hall signal cannot exclude
welded contacts. Such a witness would need explicit circuitry plus validated
loading, injection and <=1ms timing. It is not present in NETLIST.tsv. This
candidate can be reviewed and prototyped as a sensing circuit after hardware
review, but it does not yet meet the requested complete buildable-and-measurable
A1 boundary. A2 then additionally requires real calibrated hold observations.
