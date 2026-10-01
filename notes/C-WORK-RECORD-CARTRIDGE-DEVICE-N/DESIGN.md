# One apparatus with full state and a measured energy path

NON-CANONICAL / OPEN design; C-WORK-RECORD-CARTRIDGE-DEVICE-N, issue #1317.
No hardware, physical result or cross-layer acceptance is asserted.

## 1. Fixed mathematical target

Use exactly the carrier, matrices, predicates, four layers and inverse in
[the pinned #1316 proof](https://github.com/mathorn1973/twist-j/blob/312d0a90b24d5f9e743096f0ee2a477cda719a10/notes/C-FIELD-WORK-RECORD-UNIT-N/PROOF.md).
Chronological order is Ghat; A; B; F. There is no timer in its reader, extra
logical memory, inhibited reverse reaction or changed contact rule.

The proposed apparatus domain is the entire invariant shell

```text
S42 = {(s,p): s in X_3, H_3(s)=41, p in {0,1,2,3,4}}.
```

It includes arbitrary allowed spectators, static/raw fields and occupied
channels, not only the four experiment preparations. All four layers and
their inverses preserve the shell, also with either fixed single cut. This
restriction therefore needs no clipping or saturation during evolution.
It is not a proposed implementation of every unbounded integer input.

There are 72 matter/spectator entries, 18 raw-field entries, five nonnegative
resource entries and one C5 pointer. Store the first 95 as signed 16-bit
registers in a dedicated FPGA state block, with fixed ordering

```text
c0=(m0[3][4], b0[3][4], E0[4], M0[2], r0),
c1=(m1[3][4], b1[3][4], E1[4], M1[2], r1),
c2=(m2[3][4], b2[3][4], E2[4], M2[2], r2), q0, q1.
```

The wheel, not a redundant historical event counter, is authoritative for p.
The FPGA may sample its position to execute the exact inverse. Use 64-bit
signed intermediate arithmetic and exact divisibility tests; compare literal
ordered matter triples. Inconsistent input, arithmetic overflow, undecodable
wheel position or physical transfer fault goes to an apparatus ERROR state,
never to a silently altered mathematical transition.

For a concrete controller select a Digilent Arty A7-100T FPGA board. Its HDL
and bitstream have not yet been written. The 95 state registers require
1520 bits; this is not a total hardware or thermodynamic memory budget.
Workspace, duplicate transfer registers, controller phase, sensors, host and
event logs are additional apparatus. Board resources are documented by
[Digilent](https://digilent.com/shop/arty-a7-100t-artix-7-fpga-development-board/).

The following safe bounds follow without enumeration from the inherited
positive forms and are sufficient for this encoding:

| Coordinates | Count | Allowed bounding interval |
| --- | ---: | --- |
| matter and spectator components | 72 | -6..6 |
| raw E0 | 3 | -15..15 |
| raw E1 | 3 | -9..9 |
| raw E2 and E3 | 6 | -11..11 |
| raw M0 | 3 | -12..12 |
| raw M1 | 3 | -18..18 |
| r and q | 5 | 0..41 |
| p | 1 | 0..4 |

Here E0 in the table denotes a component within a cell, not the cell index.
The box alone is not the domain: positivity, integrality and total H_3=41
must also pass. For the bounds put u=2E+CM, a=M0, b=M0+M1. Then
||u||^2+a^2+b^2<=164 and
2E0=u0-2a+b, 2E1=u1+a, 2E2=u2+a-b, 2E3=u3+a-b.
Cauchy-Schwarz and Q(v)>=||v||^2 give the displayed integer intervals.

## 2. Eleven physical banks and the encoding relation

For each cell form three nonnegative integer accounts:

```text
B_i = sum_j Q(m_ij) + sum_j Q(b_ij),
Z_i = Hraw(E_i,M_i), and r_i.
```

Together with q0,q1 these are eleven accounts, whose sum is 41.
Every account has a real capacitor bank. The six B/Z banks are fixed in their
cells. The five r/q banks are insulated removable cartridges. Combining the
spectator energy with B does not omit their 36 separately stored coordinates.

Choose nominal epsilon=0.500 J per account unit and a 5.000 V baseline.
Each bank uses one Vishay MAL210118223E3 capacitor, nominal 22000 uF, 63 V,
50 x 80 mm, in a protected individually identified housing. The manufacturer
specifies +/-20% capacitance, a maximum 2.77 mA leakage after five minutes at
rated voltage and 19 milliohm maximum ESR at 100 Hz. These are component
limits, not the experiment's accuracy or measured DC leakage.
[Vishay document 28371, 21-Jul-2022, pp.4-5](https://www.vishay.com/docs/28371/101102phrst.pdf).

For sizing ONLY, a constant nominal capacitance gives

```text
E_inc(V) = C (V^2 - Vref^2)/2,
V(n) = sqrt(25 + n/0.022) volts.
```

n=2 is about 10.77 V; n=41 about 43.46 V. At the low end of nominal
capacitance tolerance n=41 requires about 48.53 V. A 50 V operational ceiling
is below the 63 V component rating. A bank unable to hold 20.500 J above its
measured baseline below 50 V is rejected. These are engineering calculations,
not science runs or a measured calibration.

For evidence replace nominal CV^2/2 by each cartridge's calibrated stored
energy function U_a(V,T,settling protocol), referenced to its own Vref.
Calibrate differential capacitance/charge and terminal work, hysteresis,
dielectric absorption, ESR and relaxation; do not fit U to a desired reaction
outcome. If a single-valued function under the frozen settling protocol cannot
meet TEST_PLAN's uncertainty, this encoding fails. Calibration travels with
the physical serial identity when cartridges exchange docks.

Dec(x) is a set-valued physical decoding/acceptance relation, not an equality
of voltages or an automatically invariant operating domain. Dec(x) contains
physical states whose exact digital registers and decoded
wheel equal x, whose eleven measured energies satisfy the bank tolerances,
whose cartridge identities are correctly docked, and whose auxiliary phase
is READY with converters disconnected and mechanics stationary. A fixed
representative preparation Prepare(x) charges each bank to n*epsilon within
the tighter initial tolerance. No history, run class or time is needed to
decode a bank. Use Enc_oper(x) only for the subset of Dec(x) with a qualified
local loss/reserve certificate for the next required operation and horizon.
These certificates have not been supplied; no universal robustness over
Dec(x) is claimed.

This distinction matters even without losses. A target R,h=0,r=2 can have
B=8.780 J and r=0.780 J, both inside the broad bands with 20 mJ uncertainty.
Its total 9.560 J cannot produce B>=9.780 J at the AM endpoint without
borrowing energy. Hence F_device(Dec(x)) subset Dec(That(x)) is false in
general. Narrow preparation and correlated reachable-energy bounds, not
independent per-bank tolerances alone, are needed for a realization claim.
For positive post-counts summing S, define d=epsilon*S-sum(E_inc). A
prequalified upper loss L over the next G must leave, conservatively,
(d+L)*n'_max/S + control_error + measurement_uncertainty within the bank
budget; include bounds on excess energy, zero-account drift and any later
operations separately. This is a necessary budget check, not a convergence
or full-horizon certificate. Missing reserve or an unqualified transition
is ERROR, never an excuse to add energy.

Every n is separated from neighbouring n by 0.500 J. Allowed boundary error
including uncertainty is 0.240 J, below half that spacing. The remaining
0.020 J between adjacent acceptance intervals is a rejection gap. A register
claiming n when its energy fails the interval is a failed physical state,
not evidence that the integer register overrules the voltmeter.

The cartridge-to-dock identity permutation is part of the auxiliary physical
state and measurement record. Dec admits every qualified identity permutation
with the proper calibration at each dock; it does not pretend equal-count
cartridges are microscopically identical. This is an explicit physical
equivalence class, not a hidden model coordinate or history-dependent reader.

The baseline is real stored energy: nominally 0.275 J per bank, 3.025 J total.
It is excluded from the model account but included in the apparatus balance.
Converters must not intentionally withdraw it. No replenishment is allowed
between boundary 0 and boundary 10. Here replenishment means an external input;
local baseline restoration by the G servo is allowed only by debiting another
bank in the same cell and recording that use of its available energy.
Baseline droop from leakage is measured and
counts against error/loss limits, including for a model-zero bank. All banks
must additionally remain within 4.7..50 V; the broad energy interval alone is
not a sufficient operating-voltage limit. Passive zero-bank droop is allowed
only under this bound and the much tighter idle-loss requirement.

The chosen model pointer offset adds another formal 0.500 J to make the
scaled account 42*epsilon. It is NOT an extra measured capacitor, measured
preparation cost, or a battery financing the reaction. Its absolute energy
reference is conventional. All five physical wheel positions must separately
meet the degeneracy tolerance, while drive/readout costs remain auxiliary.
Only calibrated energy differences have physical evidential meaning.

## 3. Contact fixture: move the stored energy itself

Five fixed docks lie at 150 mm spacing on one bench:

```mermaid
flowchart LR
    m0["Cell 0: B_0, Z_0"] <-->|"local G"| r0["r_0 cartridge"]
    r0 <-->|"contact A_0"| q0["q_0 cartridge"]
    q0 <-->|"contact B_0"| r1["r_1 cartridge"]
    m1["Cell 1: B_1, Z_1"] <-->|"local G"| r1
    r1 <-->|"contact A_1"| q1["q_1 cartridge"]
    q1 <-->|"contact B_1"| r2["r_2 cartridge"]
    r2 <-->|"local G: measured work"| m2["Cell 2: B_2, Z_2"]
    m2 -->|"accepted R to AM only"| p["C5 wheel: local reader"]
```

Here contact B0 is a layer label, distinct from the cell0 matter bank B_0.
Each r/q dock contains exactly one cartridge at every completed layer. Four
local paired pick-and-place fixtures exchange the complete adjacent
cartridges: two disjoint pairs in A, then two disjoint pairs in B. A proposed
fixture picks both housings, lifts them clear of the sockets, rotates a paired
arm 180 degrees about a vertical axis, and redocks them at the same height.
Fixtures for the other layer are interlocked and parked clear. Their detailed
mechanical drawings and collision checks remain construction deliverables.

Before motion, disconnect both cartridge terminals from all power ports;
break-before-make and insulated housings prevent charge sharing. The energy
carrier really traverses the contact distance. Relabelling stationary banks
or exchanging FPGA addresses alone is forbidden. Sensors read cartridge IDs,
dock occupancy and voltages before/after each swap. A and B must exchange
occupied pairs as well as occupied/empty pairs. Unequal calibrated
capacitances are harmless only because the *whole* energy carrier moves.

Actuator motors use an independently metered 24 V supply. Kinetic/potential
energy, friction and braking belong to the fixture account. Motion does not
authorize an electrical charging connection. Any measurable electrical
injection caused by switching, probes or motion is nevertheless included in
the energy ledger. No identification of model contact speed with c is made.

Cut j disables BOTH A_j and B_j mechanically and electrically. Keep its q_j
cartridge and content in place; do not remove or discharge it. The command
schedule still has the same slots. Physical locks and connectivity inspection
must establish the cut, not just a software flag hiding an observation.

## 4. Local work ports and exact gate sequencing

Each cell has one custom LT8708-based bidirectional buck-boost stage with an
interlocked two-port selector connecting only two of its own B,Z,r banks.
There is no common energy bus between cells. The power-stage input and output
are independently metered. Use donor-current setpoints0.10..0.50 A,
with recipient current separately limited to 0.50 A and allowed below 0.10 A,
8 V gate/control power derived from the currently selected donor behind its
input work meter, and optically isolated commands. Use a custom LT8365 SEPIC
for this 8 V supply; its 2.8..60 V input range covers the selected donor range.
Its BIAS pin and output-storage charging have no external supply connection.
The auxiliary branch must be inside the measured donor boundary, including
startup energy. This topology is a design, not a qualified efficiency claim.
[LT8365 datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/LT8365.pdf).
Auxiliary supply,
secondary-side sensors, gate-drive coupling, local converter capacitors and
inductor energy are all separately accounted for. No battery or charging
supply connects to B_i or r_i during a trial.

[LT8708 Rev.D](https://www.analog.com/media/en/technical-documentation/data-sheets/lt8708.pdf)
supports bidirectional buck-boost operation across equal or unequal voltages;
its low-input operation needs EXTVCC above 6.4 V, and its output range starts
at 1.3 V. The design's4.7..50 V bank range and donor-fed 8 V rail address these
range constraints. The advertised efficiency of up to 99% is not a guaranteed
minimum for the proposed short pulses. Existing high-power evaluation-board
efficiency plots do not qualify this custom converter. Component values,
layout, stability and pulse losses remain qualification tasks.

Evaluate the exact local G predicate on the full input first. A rejection
leaves all registers, banks and p unchanged except measured passive drift.
For an accepted R-side input write h=H(x) after the exact high-branch split.
The ideal bank operations in units of epsilon are:

| Branch | First transfer | Second transfer |
| --- | --- | --- |
| R -> AM, h=0 | r -> B: 2 | none |
| R -> AM, h>=1 | Z -> B: 2 | Z -> r: 4h-2 |
| AM -> R, h=0 | B -> r: 2 | none |
| AM -> R, h>=1 | r -> Z: 4h-2 | B -> Z: 2 |

For every accepted pair in S42, 18+5h<=41, hence h<=4. The largest resource
transfer is 14 units=7 J, and total field change at most 16 units=8 J. No
unbounded reservoir or undeclared energy buffer is needed. Transient energy
in actual converter parts is not zero and belongs to the apparatus ledger.
Before changing donors, disconnect both banks, stop switching and verify
inductor current is negligible. Measure remaining8 V/output-filter energy,
return it to the same donor through a metered route or dissipate it in a
metered discharge. Start each new donor connection from the qualified
near-zero auxiliary-storage state. Do not carry a hidden charged converter
buffer from a different donor into the receiving event.

These are the ideal transfers. The physical control must distribute losses,
not repeatedly demand exact withdrawals from a bank already below its nominal
energy. Freeze the following local feedback target: for the three exact
post-gate counts n'_j, every zero account returns to its reference; positive
accounts share one measured energy-per-unit lambda. Thus their target
energies are lambda*n'_j, with lambda determined by the remaining local
energy after loss, not by an external charger. Small equalization transfers
remain inside the same cell's G slot and are included in its work ledger.

The table specifies mathematical changes, not mandatory exact withdrawals
before feedback. Physical control starts from actual input energies using
deterministic pair equalization throughout: restore a below-reference bank
from the bank with the largest positive E_inc, stopping when the recipient
reaches reference; drain a positive remainder in a zero-count bank into the
lowest-ratio positive-count bank, stopping when the donor reaches reference;
otherwise transfer from the largest to the smallest measured E_inc/n'_j,
stopping when their ratios agree within the prequalified control resolution.
Ratios are used ONLY for n'_j>0. Ties use B,Z,r order. Repeat at most 32
times. At each comparison compute lambda_now=sum(E_inc)/sum(n'_j), not a
predicted final value before unknown losses. Commit only when every account
is within 0.005 J of lambda_now*n'_j and its absolute Dec interval. Deadline1.7 s
and the 4.7 V floor override every transfer. Failure to converge is ERROR.
The control-resolution bound
requires its own calibration and is not inferred from a 20 mJ absolute energy
uncertainty. Arithmetic counts and event predicates remain exact throughout.

This feedback uses only local measured energy and exact post-counts, never
the run label or desired observed outcome. It may not top up from a third
rail. It is a proposed physical error-allocation procedure within Dec, not a
new exact mathematical gate or a proof of analog convergence. Its dynamics
and extra dissipation need qualification. Small errors can still accumulate;
failure before step 10 is a failure, never permission to reset a bank or clock.

Commit the new digital matter/field/resource block only after the physical
transfers meet the frozen completion checks. At the receiver, an accepted
R -> AM completion advances p by one modulo5; mere energy arrival, a command
or a failed attempted transfer does not. Partial failures produce apparatus
ERROR and end the trial. This is fault handling outside qualified Enc_oper
domain, not a new branch of the mathematical law.

For the prepared positive case, Z_0 initially holds 2.500 J above baseline,
B_0 and B_2 each 9.000 J, and all resources are model-zero. At step1 the
source field supplies 2.000 J: approximately1.000 J to B_0 and1.000 J to r_0,
with all discrepancies recorded. The same charged cartridge reaches r_1
then r_2. At step3 it performs electrical work charging B_2 towards 10.000 J.
This charging is the declared receiver work, measured as integral V I dt and
as independently calibrated stored-energy increase. It is not inferred from
an LED, software resource decrement or a separately powered output motor.
At step4 B_2 supplies the reverse transfer, the old receiver registers return
to their preparation and the wheel remains readable. No export load is
attached during these ten steps: it would change the specified energy path.

F updates all six raw-field integers by the exact inherited matrix. It leaves
the corresponding physical Z bank connected to no work port because Hraw is
unchanged. Treat F as one boundary operation; its algebraic shear factors need
not individually preserve Hraw. The encoded E/M integers are *codes*, not a
claim that the bench has generated those literal Maxwell fields or charges.

## 5. Pointer, clock and inverse

Use one horizontal five-detent wheel with positions 72p degrees and a passive
three-track code mask. Three independent optical channels decode p=0..4;
unused codes and transition regions are ERROR. BLANK is position0 only;
HIT is any other valid position. The reader accepts only position within
5 degrees of a calibrated detent centre, leaving wide rejection zones.
No run number, step number, expected answer or stored history enters O_lab.
The local drive/readout uses its own metered 5 V rail, independent of B_2.
Its energy does not count as transmitted receiver work.

Detents must have matched static energies within 0.005 J after uncertainty.
Measure forward/backward quasi-static torque-angle work and bound friction,
magnetic/spring asymmetry and readout disturbance; similarity of appearance
or equal heights alone does not certify degeneracy. A commanded 72-degree
rotation that fails position qualification fails the trial. No assumption of
zero write/reset/reading cost is made.

Choose a fixed 10.000 s macrostep for the first design:

| Layer | Operation slot | Quiet settling | Fixed measurement window |
| --- | --- | --- | --- |
| G |0..1.7 s |1.7..1.9 s |1.9..2.0 s |
| A |2.0..4.2 s |4.2..4.4 s |4.4..4.5 s |
| B |4.5..6.7 s |6.7..6.9 s |6.9..7.0 s |
| F |7.0..7.1 s |7.1..9.9 s |9.9..10.0 s |

The energy-map qualification uses these same settling histories and windows;
if dielectric relaxation prevents one valid decoding map, reject the parts.
All cells receive the same layer schedule. An operation that
misses its slot is a timing failure; do not slow the clock after inspecting
the result. This is a mechanical throughput requirement to qualify, not a
datasheet prediction. Boundary k is the state latched at 10k s. Confirm the
same decoded state and analog drift limits throughout the final read window.

The reverse mode is F^-1; B; A; Ghat^-1. Assign the same operation/settling/read
durations to the corresponding reversed layers: F^-1 in0..3 s, B in3..5.5 s,
A in5.5..8 s, Ghat^-1 in8..10 s; within each slot use its forward operation
length, quiet remainder, and final100 ms measurement window. Ghat^-1 recovers c=G(c') and
subtracts e(c) from p, then performs the corresponding physical bank transfers.
It does not simply invoke the forward extended gate twice. No event-history
log is used. Both forward-then-reverse and reverse-then-forward must recover
all 96 decoded coordinates and qualified analog intervals.

Losses, emitted heat, dissipated motor work and recording electronics are
not reversed by this procedure. It tests implementation of the mathematical
inverse under the stated physical tolerance, not reversal of every microscopic
degree of freedom. Logical reversibility does not by itself establish
thermodynamic reversibility; see [Bennett's review](https://research.ibm.com/publications/the-thermodynamics-of-computation-a-review).

## 6. Complete accounting and the scope of a future success

Record separately: eleven bank energies including baselines; local converter
input/output and stored transients; 8 V control/gate rails; 24 V fixture rail;
5 V FPGA/pointer/sensor rails; host and acquisition power; charging and reset
supplies; mechanical positions/velocities; external heat and any electrical
work crossing each boundary. Resetting logs or preparing p=0 is preparation
with its own resources, not a reversible free operation.

For a closed measurement interval use the signed first-law ledger

```text
Delta U_banks + Delta U_aux + Q_out + W_out = W_external,in.
```

Electrical contributions are measured at ports. Fixture/control dissipation
may be bounded from metered input and changes of stored energy; report that
as an inferred heat budget, not independent calorimetry. Any unmeasured port
or insufficiently bounded stored energy prevents closure. Include correlated
uncertainties and publish the full ledger, even when auxiliary energy greatly
exceeds the 1 J receiver event. No efficiency or minimal-cost claim is made.

The smaller causal claim needs a stronger, local balance: net source-created
resource energy, cartridge energy along the path and net receiver work must
agree after their measured losses; all possible auxiliary contribution to the
receiver work must be below the specified bound. Isolation barriers alone do
not prove this. The two cuts and equal-energy offimage case test the causal
contrast with the same apparatus and ready receiver.

A successful four-configuration campaign would establish this finite
operating witness and complete decoded trajectory at its tested inputs.
It would not establish operation on every S42 state. The design specifies
that larger domain so it can be audited for full-state coverage; full-domain
certification additionally needs verified arithmetic/control and qualified
analog bounds for every admitted transition class. Neither certificate is
supplied here. It would also not establish natural selection of L5, J,
the contact geometry, clock rate or five-state carrier.
