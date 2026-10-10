# Calcium-ion contact: concrete carrier and realization audit

**PUBLIC / NON-CANONICAL / analytical audit, not a device certificate.**
Author: A. M. Thorn <thorn@twistj.com>. Date: 2026-10-10.
Reservation: [#1444](https://github.com/mathorn1973/twist-j/issues/1444).
Basis: `408fc7a34cbd8113b4d5e1dac43793c7ad0270b0`, Public Canon v101.
Original text: Apache-2.0. No new scientific program or experiment was run.

## Result

Select seven distinguishable **40Ca+ optical ququints**, each using one
S1/2 ground level and four D5/2 metastable levels. This is an external
quantum-physics comparison supported by published local-control and
two-ion entangling experiments. It is not a physical dictionary derived
from J or an assertion that TWIST-J has access to that apparatus.

Encode the centered coordinates `(x,u,y,w,q,r,s)` directly as the five
physical level labels. The requested complete contact is

```text
h=y-x,
C:(x,u,y,w,q,r,s) -> (x,u-2hs,y,w+2hs,q,r,s), over F5.
```

The previous [contact/source note][previous] compiled C using a conditional
number-product interaction. Here an explicit analytic construction instead
uses the published **light-shift equality-phase gate family**. With ideal
pair access and local controls it needs at most **56 ququint entangling
gates**, plus the specified local operations. In the five-loop ideal
experimental template this is 280 closed light-shift loops. These are
conditional resource counts, not a demonstrated seven-ion implementation.

The audit reaches three different decisions:

| Question | Result |
|---|---|
| Are there independently evidenced five-level physical systems with relevant preparation and control? | Yes: the selected calcium platform has published local-control and two-ion precedents. |
| Is there a full-space contact construction in the stated effective control model? | Yes, analytically; it needs addressed pair access, calibrated phases, mode closure and protected spectators. |
| Has this seven-ion contact, its complete preparation/history, error budget, controller and numerical energy/work account been realized? | **NOT PROVIDED.** The literature ingredients do not certify this apparatus. |

The strongest requested source contract also has a decisive boundary:
**an informative write can retain each classical source label, but cannot
universally retain an arbitrary unknown source quantum state and its
reference correlations.** For a coherent equal source superposition and a
fixed receiver basis state with h nonzero, C produces a maximally mixed
source marginal. The complete ideal joint state remains recoverable by
the inverse; applying that inverse removes the new record.

## What the physical audit adds

- [CARRIER.md](CARRIER.md) fixes the actual levels, preparation, available
  optical controls, readout and the limits of the published experiments.
- [COMPILATION.md](COMPILATION.md) derives SUM from the actual gate family,
  then C; it states phases, counts, finite durations and control assumptions.
- [PROTOCOL.md](PROTOCOL.md) fixes the proposed operational order, inherited
  state obligations, native-counter distinction and discriminating tests.
- [ENERGY.md](ENERGY.md) accounts for internal states, motion, fields,
  control, baths, detection and renewal without omitting coupling energy.
- [VALIDATION.md](VALIDATION.md) records review, source custody and repository
  checks separately from physical evidence.

The chosen S-D levels are not an equally spaced modular energy ladder.
For example, at centered `(x,y,u,w,s)=(0,1,0,0,1)`, the targets change from
`(u,w)=(0,0)` to `(3,2)`: two optical excitations, with the source label
unchanged. Their energy must come from another participant. More generally,
all-state bare-energy conservation would require both target spectra to
be flat. An exact clean autonomous realization under the stated additive
endpoint assumptions is therefore excluded; approximate driven control
has a different resource contract.

The full energy balance can be written now. A numerical number of joules
for the proposed complete contact cannot be obtained from gate count,
fidelity, wavelength or one published pulse duration. It requires the
actual seven-ion pulse schedule, state populations, fields, mode histories,
optical powers, coupling energies, controller changes and preparation/readout
cycle. Incident light, net work on ions and electricity drawn by the
apparatus are separate measured quantities.

## Scope and next physical decision

The near-term meaningful milestone is a calibrated **driven contact
experiment** with an explicitly chosen classical-source or quantum-channel
contract. It must supply the pair-addressing and spectator certificate,
complete finite pulse schedule, inherited motional state and error/energy
records listed in PROTOCOL. This note has no measurements from such a device.

An autonomous implementation of unchanged native U is a separate problem.
The seven ions do not contain its unbounded counter or all information
discarded by its globally noninjective update. Scheduling native operations
on an external computer does not close that physical bridge. Preparing a
known checkpoint directly tests a contact, not the actual preceding native
history. Finite pulses also cannot be inserted into a continuously running
native trajectory solely because the completed algebraic C commutes with
some completed native maps.

This lane follows the occupied-SUM contact of #1439 and #1443. It does not
resume the consumptive trace-port contact of #1353-#1371. In particular,
the older fixed-profile/common-control restrictions and their exclusions,
the seventeen-ion retained-memory constructions, and the different
all-D-plus-ground-auxiliary sideband dictionary retain their own scopes.
The standard source-information and conservation boundaries are attributed
in the companion files. No priority for those general principles is claimed.

No Canon, Registry, Frontier, physical-owner disposition, gate, sealed
probe, workflow or release changes. The note selects and audits a candidate;
it does not promote it to a physically admitted native contact.

[previous]: ../C-U-CONTACT-FULL-SOURCE-ADMISSION-N/README.md
