# A tighter constructive pulse and time budget

**PUBLIC / NON-CANONICAL / analytical feasibility estimate; no execution.**
Author: A. M. Thorn. Original text Apache-2.0. Date: 2026-10-10.
Reservation: [#1446][claim]. Base: `4699d2b651dda6cb17a71492a47e47e14831e969`.
No scientific program, numerical pulse search, simulation or experiment was
performed. The counts below are constructive upper bounds, not measured or
optimal pulse counts. They refine the prior loose 9758-pulse upper bound.

## 1. Fixed circuit and addressed-rotation convention

Keep exactly the [previous centered contact compiler][compiler]: fourteen
SUM gates, each built from four normalized Hrmo-family G gates, with gains
plus/minus one. Hence there are 56 G gates, 112 reflections J_c (c=1,...,4),
28 quadratic A phases, seven cubic Q phases and 32 Fourier/inverse Fourier
macros. The five physical pair edges and all seven data ions are unchanged.
This assumes the same ideal matching-phase family and pair/spectator contract;
it does not establish that those controls exist at a measured precision.

Write the addressed star rotation as

```text
R_0j(beta,phi)=exp[-i beta(cos(phi)X_0j+sin(phi)Y_0j)/2],
R_0j(pi,phi)|0>=-i exp(i phi)|j>,
R_0j(pi,phi)|j>=-i exp(-i phi)|0>.
```

All other levels are fixed. Off-resonant spectator phases must be compensated.
Here one pulse means one such ideal resonant rotation, not an experimental
composite pulse that may itself need several driven intervals.

## 2. Exact four-pulse reflections and eight-pulse diagonal macros

For c nonzero, the reflection J_c:j->c-j has cycle form `(0 c)(a b)` and
one fixed point. The following chronological four pi pulses implement J_c
with coefficient one on every column:

```text
R_0a(pi,0), R_0b(pi,pi), R_0a(pi,0), R_0c(pi,-pi/2).
```

The first three exchange a,b exactly and multiply |0> by -1; the last
exchanges 0,c and cancels that sign. This covers every J_c actually used;
the unused c=0 reflection need not have the same pulse count.

For a determinant-one diagonal D=diag(exp(i d_0),...,exp(i d_4)), take
for each j=1,...,4 the chronological pair

```text
R_0j(pi,0), R_0j(pi,d_j+pi).
```

Its phases are exp(-i d_j) on 0 and exp(i d_j) on j. Their product is D,
because d_0=-sum_(j=1)^4 d_j modulo 2pi. Thus each A or Q needs at most
eight pi pulses, without treating a physical phase gate as automatically free.
All matrices A,Q in the contact have determinant one.

## 3. Fourier macro: at most 24 star pulses

A constructive star-graph elimination improves the generic 42-pulse bound.
For an arbitrary SU(5) matrix, use row 0 as the active pivot. In column 0,
zero rows 1,2,3,4 with four equatorial star Givens rotations. Store this
completed pivot by a star pi swap of rows 0 and 1. In column 1, zero rows
2,3,4 using three rotations and store its pivot by swapping rows 0 and 2.
In column 2, zero rows 3,4 with two rotations and store by swapping 0 and 3.
In column 3, zero row 4 with one rotation. Previously stored columns stay
zero in every active row, so none of these eliminations damages them.

Unitarity leaves a monomial matrix: its column positions are rows
`1,2,3,0,4`. Restore their order with three star pi swaps. The phases of
these swaps are included in the remaining diagonal, which is in SU(5).
Elimination therefore uses ten Givens rotations, six pi swaps, and at most
eight pulses for the diagonal. Reverse and adjoint the word to synthesize
the target. Every Givens angle can be chosen between 0 and pi: for active
entries v_0,v_j, its magnitude is `2 atan2(|v_j|,|v_0|)` and its phase
aligns the two terms for cancellation. Vanishing entries allow fewer pulses.

This gives at most 24 star pulses for each Fourier macro, including its
diagonal. Use an SU(5) representative of F and its actual inverse; the
paired scalar phases cancel as in the previous compiler. No empty level
or computational ancilla is used in this elimination.

## 4. Operation counts versus elapsed-time slots

Without cancellations or virtual phase updates, the counts are

| Component | One-ion resonant pulses, at most |
|---|---:|
| 112 reflections, four pi pulses each | 448 |
| 35 A/Q diagonal macros, eight pi pulses each | 280 |
| 32 Fourier macros, at most 24 pulses each | 768 |
| Local subtotal outside G | 1496 |
| 56 G, five X5 echoes on each of two ions, four pi pulses/X5 | 2240 |
| Complete centered contact | 3736 |

There are also 280 closed LS loop segments. Each echo applies the same
transition on its two selected ions. If those two rotations can be driven
simultaneously with their required phases and calibrated equal duration,
the 2240 one-ion echo pulses occupy 1120 temporal slots. Keep the other
1496 pulses serial: this yields at most 2616 carrier slots. If the hardware
cannot supply those simultaneous pair rotations, use 3736 slots instead.
Neither count assumes parallel operations on unrelated pairs.

The pair-hiding proposal is a separate conditional overhead. Hiding and
unhiding five spectators once around each G adds at most `56*5*2=560`
one-ion pi pulses under its one-transfer contract. Add their actual time,
phase compensation, address changes and leakage error; hiding is not proved
by this arithmetic. Composite transfers would increase the count.

## 5. Optional tracked phases, with a physical endpoint correction

Calibrated local diagonal frames can reduce the resonant pulse budget.
For D=diag(exp(i d_j)),

```text
D R_0j(beta,phi) D^dagger = R_0j(beta,phi+d_j-d_0).
```

Every G is diagonal and commutes with these frames. Push the A/Q and
Fourier residual diagonals through the subsequent primitives by changing
the addressed laser phases, while keeping a frame for each active ion.
At the end physically correct the residual diagonal with at most eight
pulses on each of the five active ions. This preserves the specified
quantum output rather than merely relabeling a population measurement.

The resulting upper bound is `448+32*16+40=1000` external pulses, hence
3240 one-ion pulses or 2120 slots with simultaneous pair echoes. The saved
496 slots are conditional on phase tracking, coherent calibration and a
pair implementation compatible with independently adjusted echo phases.
If the two ions require different echo phases that a common beam cannot
provide, the 2120-slot schedule does not follow; retain the serial count.
Frame updates and controller latency are resources, not zero-duration physics.
No global program phase is discarded relative to a coherently controlled
alternative program branch.

## 6. Published scales and explicitly assumed SI scenarios

[Hrmo 2023][hrmo] reports a representative approximately 35-microsecond LS
loop, with theta tunable by power or detuning/time. It does not establish
that all 280 loops at our two required angles and five pair geometries run
at that time. [Ringbauer 2022][ringbauer], Supplementary I, reports addressing
reconfiguration below 10 microseconds, rather than a zero-cost switch.
Neither inspected main/author-supplement text supplies the complete four-
transition carrier timing table needed for this proposed seven-ion contact.

[Nigg 2014][nigg], Appendix A2, reports roughly 10 microseconds per pulse
in its qubit decoupling/recoupling sequence. Those operations include pi/2
and AC-Stark pulses; this is not a measured uniform ququint pi time.
A newer [Ca-40 experiment][zhang], published online in December 2025,
explicitly reports global 729-nm pi pulses at 100 kHz, or 5 microseconds.
It uses two qubits on S(+1/2)-D(+3/2), not our four addressed ququint
transitions, and reports sequence-length limitations from laser noise.
Thus it supplies a demonstrated speed scale, not a transferable contact
fidelity or proof that all of our pulses can run at 5 microseconds.

Let t_pi be an assumed upper duration for every selected star pi pulse,
and bound every Givens duration by t_pi at its calibrated amplitude. With
simultaneous pair echoes, no virtual-frame savings and actual loop bound t_LS,

```text
T_contact <= 280 t_LS + 2616 t_pi + T_pair + T_overhead.
```

T_pair is zero only if the selected-pair primitive is already provided;
for the unoptimized hiding proposal use at most 560 t_pi plus its overhead.
This also assumes that the auxiliary shelving transition has pi duration
at most t_pi; otherwise replace that term by 560 t_shelf,max. Its coupling
strength is not fixed by the four computational transitions.
T_overhead includes switching, waiting, calibrated compensation and routing.
The following are evaluations of the assumed bounds, not measured runtimes:

| Assumed t_pi; every loop 35 us | Pair echoes, no hiding | Plus 560 serial hiding pulses | Fully serial, no hiding |
|---|---:|---:|---:|
| 5 us, fast illustrative transfer of a qubit speed scale | 22.88 ms | 25.68 ms | 28.48 ms |
| 10 us, central illustrative scenario | 35.96 ms | 41.56 ms | 47.16 ms |
| 20 us, slower-transition sensitivity scenario | 62.12 ms | 73.32 ms | 84.52 ms |

Every entry excludes T_overhead. The optional frame scheme at 10 us gives
31.00 ms before hiding/overhead, or 36.60 ms with the 560-pulse allowance.
One additional microsecond of dead time per carrier slot already adds
2.616 ms in the non-frame schedule. Reconfiguration time cannot be added
once globally or once per pulse without the actual beam/address schedule.
Using the older twenty-affine unequal-profile construction changes the LS
and permutation counts; the five-loop time table must not be reused for it.

## 7. Practical reading of this estimate

The analytically compiled contact has a plausible **tens-of-milliseconds
control budget under the displayed assumptions**, with a credible danger
of appreciably longer times once pair isolation, compensated pulses and
seven-ion mode closure are implemented. This is substantially more useful
than treating 9758 as an actual pulse count, but is still a design estimate.
Pulse duration alone does not establish useful total fidelity. Thousands of
addressed operations, slow correlated detuning, unequal transition strengths,
spectator phases, leakage and long-lived motional correlations remain the
important experimental constraints. Multiply neither published gate
fidelities nor randomized-benchmarking averages into a claimed failure bound.

Preparation/cooling, state readout/reset, and any separately compiled native
U continuation are outside T_contact. A complete trial duration adds each
of these measured stages. This estimate implements a driven endpoint gate;
it does not fit a finite pulse sequence into an unmodified autonomous native
tick or prove source preservation throughout intermediate physical time.

[claim]: https://github.com/mathorn1973/twist-j/issues/1446
[compiler]: ../C-U-CA40-CONTACT-REALIZATION-AUDIT-N/COMPILATION.md
[hrmo]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10115791/
[ringbauer]: https://ar5iv.labs.arxiv.org/html/2109.06903
[nigg]: https://arxiv.org/pdf/1403.5426
[zhang]: https://www.nature.com/articles/s41467-025-66828-z
