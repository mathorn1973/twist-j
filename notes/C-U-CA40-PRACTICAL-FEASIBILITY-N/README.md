# Seven-calcium-ion contact: practical feasibility

**PUBLIC / NON-CANONICAL. Analytical engineering audit, not a device result.**
Author: A. M. Thorn <thorn@twistj.com>. Date: 2026-10-10.
Reservation: [#1446](https://github.com/mathorn1973/twist-j/issues/1446).
Base: `4699d2b651dda6cb17a71492a47e47e14831e969`, Public Canon v101.
Original text Apache-2.0. No new scientific program or experiment was run.

## Practical decision

**The proposed 56-G contact is not ready to be claimed as a reliable complete
seven-ion implementation. A selected-pair prototype is physically plausible;
the complete coherent contact remains an unvalidated engineering proposal.**
Published results support individual ingredients, but do not supply their
required combination, spectator isolation, runtime or complete error.
This is an evidence-based engineering assessment, not an impossibility proof.

The most consequential isolation finding is that shelving each spectator's
ground component into an auxiliary D level does **not** protect it from
global 729-nm echo pulses: its four occupied computational D levels remain
coupled to S. All echo pulses must be selectively addressed, as must the
external local gates. Small residual D-dependent optical forces, coherent
cross-talk and motion must then be included explicitly.

The reviewed literature does not justify treating this pair primitive as
already available. Hrmo's two-ion demonstration uses broad force beams
[H23]. A March 2026 conference abstract explicitly describes individual
Raman addressing for this qudit LS mechanism as under development [P26].
That abstract supplies neither a measured seven-ion gate nor its error;
it is not a proof that no other laboratory could implement one.

## Fixed task and apparatus

The unchanged contact acts over F5:

```text
C:(x,u,y,w,q,r,s) -> (x,u-2s(y-x),y,w+2s(y-x),q,r,s).
physical ions: s=1, x=2, u=3, y=4, w=5, q=6, r=7.
```

Each five-level code uses S1/2(-1/2) and D5/2 levels with magnetic quantum
numbers -3/2, -1/2, -5/2, +1/2. The candidate hiding level is D5/2(+3/2).
Its coherent transfer preserves all five amplitudes and reference
correlations in the ideal limit; it is not optical pumping or reset.
The [previous audit][previous] specifies preparation, controller, readout,
the driven nature of the contact, and the complete symbolic energy account.

| Active physical pair | Number of G gates | Inactive ions requiring protection at each G |
|---|---:|---|
| (2,4), x-y | 8 | The other five |
| (3,5), u-w | 8 | The other five |
| (1,5), s-w | 16 | The other five |
| (4,5), y-w | 16 | The other five |
| (1,4), s-y | 8 | The other five |

All five axial-pair geometries require calibrated phases and closure of
every coupled motional mode, not merely the two-ion COM condition. There
are seven axial modes, plus any radial modes coupled by imperfect geometry.
Spectator phase tests must distinguish removable local phases from
unwanted conditional phases or residual entanglement with motion.

For the coherent task define the engineering error
`delta_C=(1/2)||E_C-U_C||_diamond`, including all seven encoded ions,
leakage and arbitrary input references. Motion and controller memory must
be retained in composition or their reduction independently justified.
Illustrative goals are delta_C<=0.10 or <=0.01; these are selected design
criteria, not an earned result or a conversion of reported average fidelity.
Classical full-tuple correctness is a weaker, separately reportable task.

## Time budget and error assessment

[TIMING.md](TIMING.md) improves the earlier loose 9758-pulse ceiling:

| Constructive schedule | External one-ion pulses | Including G echo pulses | Carrier time slots with simultaneous pair echoes |
|---|---:|---:|---:|
| Direct physical phases | <=1496 | <=3736 | <=2616 |
| Calibrated phase frames and physical final correction | <=1000 | <=3240 | <=2120 |

These bounds are before spectator hiding. Both schedules still use
56 G gates, or 280 LS loops in the ideal five-loop template. The elementary
hide/unhide construction adds at most 560 transfers; compensated pulses
can cost more. Simultaneous echoes require independent compatible phases
on both active ions, not simply a global beam illuminating the chain.

At **assumed** bounds of 35 microseconds per LS loop and 10 microseconds
per carrier or hiding pi pulse, the direct schedule's budget evaluates to
**41.56 ms with simultaneous pair echoes**, or **52.76 ms with serial
echoes**, including that 560-transfer allowance. Both omit switching,
settling, compensation, routing and other overhead. They are evaluations
of conditional upper bounds, not measured durations or rigorous lower
bounds. The phase-frame variant gives 36.60 ms under the same simultaneous
echo assumptions. The complete trial additionally includes preparation,
cooling, readout and reset; the actual schedule must supply their times.

The published d=5 G decay-fit performance is 93.7(3)% on two ions [H23],
with correlated-noise qualifications. It cannot be multiplied into a
certified whole-contact fidelity. The deliberately crude independent-event
substitution `0.937^56` is about 0.026: a warning about depth, **not** a
prediction or bound on actual contact fidelity.

Even allocating an entire independent-event success budget to G alone
would require 99.812% per G for 90% circuit no-fault probability, or
99.9821% for 99%. The corresponding sufficient half-diamond allocations
are instead delta_G<=0.10/56 or <=0.01/56. These are different metrics;
external pulses, hiding, storage and leakage leave less budget for G.
[ERROR.md](ERROR.md) gives the compositional bound and explains why the
reported benchmarks cannot fill its terms.

Lifetime also matters across the whole register. For the stated maximally
mixed ensemble, average D population is 5.6 ions in the direct code or
6.6 during loops with five hidden spectators. With measured lifetime
1.168(9) s, a hypothetical 50-ms constant exposure has first-order jump
parameter about 0.240 or 0.283. These are exposure diagnostics, not total
contact error probabilities. Exact no-jump survival uses the conditioned
state; even no-jump evolution may distort amplitudes. Decay already inside
a measured G must not be counted again as an additional independent error.

## Concrete decision sequence

1. Calibrate one selected pair at both required G angles, +/-4 pi/5,
   while all five spectators hold coherent states. Measure population
   leakage, phases, cross-talk, spectator coherences and residual motion.
   A test with spectators all in a convenient basis state is insufficient.
2. Establish the same capability on all five listed pairs, including both
   individually addressed echo control and the actual seven-ion mode spectrum.
   Test inherited motional states instead of assuming a reset between gates.
3. Compile and test a four-G SUM with its complete local operations and
   protection schedule. Fix an actual pulse word, calibrated durations and
   a noise model checked against sequence-length and phase-sensitive data.
4. Attempt the complete contact only with a justified full error budget;
   report the declared classical or coherent metric, preparation/readout
   cost and the complete energy/work cycle. Short benchmark sequences
   alone cannot certify the 56-G result.

The present proposal therefore supports **a component-development experiment**,
not a claim of a demonstrated high-reliability contact. Better addressed
control and a substantially shallower compilation or better primitives
could change that decision; those improvements need their own evidence.

The earlier source boundary remains: ideal C retains classical source
labels, but an informative write cannot universally leave an arbitrary
unknown quantum source and all its reference correlations unchanged.
Error reduction does not remove that distinction. The joint ideal state
is reversible; undoing C also removes the new record.

[ISOLATION.md](ISOLATION.md), [TIMING.md](TIMING.md), and
[ERROR.md](ERROR.md) contain the derivations and primary sources.
[VALIDATION.md](VALIDATION.md) records analytical cross-review and repository
checks. Canon, physical-owner dispositions and sealed probes are unchanged.
No experimental access, full-channel fidelity or numerical total energy
consumption is claimed.

[previous]: ../C-U-CA40-CONTACT-REALIZATION-AUDIT-N/README.md
[H23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10115791/
[P26]: https://www.dpg-verhandlungen.de/year/2026/conference/mainz/part/q/session/67/contribution/9
