# Pair isolation and complete spectator protection

**PUBLIC / NON-CANONICAL / analytical feasibility audit; no execution.**
Author: A. M. Thorn. Original text Apache-2.0.
Reservation: [#1446][claim]. Public base: `4699d2b651dda6cb17a71492a47e47e14831e969`, Canon v101.

The earlier [Ca40 audit][prior] supplied a conditional compiler, not calibrated
seven-ion pair access. This note identifies a concrete shelving candidate and
its missing measurements. It does not conclude that present hardware cannot
perform the task. No scientific program, simulation or experiment was run.

## 1. The five physical edges

Keep the physical allocation `s:1, x:2, u:3, y:4, w:5, q:6, r:7` and the
direct centered encoding of the previous audit. Its unoptimized compiler needs:

| Logical control,target | Physical ions | SUM occurrences | G occurrences |
|---|---|---:|---:|
| x,y | 2,4 | 2 | 8 |
| u,w | 3,5 | 2 | 8 |
| s,w | 1,5 | 4 | 16 |
| y,w | 4,5 | 4 | 16 |
| s,y | 1,4 | 2 | 8 |

Every G must protect all five nonparticipating ions, including temporarily
inactive data among s,x,u,y,w. Protection must act as identity on an arbitrary
five-dimensional spectator and its reference, after declared local frame
corrections. Measuring only populations or the active pair is insufficient.

## 2. What the primary experiments establish

[Hrmo et al.][hrmo], published Results, Eq. (1)-(3), demonstrate two Ca40 ions
with broad approximately 45-micrometre-waist LS beams at 401.2 nm. Their
five-loop ququint gate uses a single-mode effective model and neglects
differences among the small D-state shifts. The reported approximately
35 microseconds is one LS pulse. Neither the beam geometry nor that number
certifies a selected pair in a seven-ion chain.

The [Poloczek et al. DPG contribution][dpg], dated 5 March 2026, describes
development of an individually addressed Raman system for this LS qudit gate,
using counterpropagating beams. It is a primary conference abstract describing
work in progress; it supplies no measured seven-ion fidelity, crosstalk matrix
or gate-time budget. The literature search found no such certification for
these five edges. This is a statement about the evidence located here.

Addressed Ca40 control itself is established. [Pogorelov et al.][pogorelov],
published Sec. IV D/Fig. 13, measure 729 nm AOD addressing in ten ions:
mean resonant Rabi-frequency ratio 0.2%, nearest-neighbour mean 0.5%, maximum
1%; off-resonant measurements give maximum 2.6e-4. These are addressing
ratios in that optical-qubit setup, not gate infidelities or 401 nm force
ratios transferable to this ququint apparatus.

An earlier seven-Ca-ion experiment demonstrates coherent spectroscopic
decoupling for global MS **qubit** gates. [Nigg et al.][nigg], author manuscript
Appendix A2, PDF pp. 7-9, describes up to nine operations per complete
decoupling, and likewise recoupling, at about 10 microseconds per pulse.
Its resonant neighbour/target Rabi ratio is about 5% in the chain centre;
composite operations suppress the leading addressing effect to its square.
This establishes a useful technique, not five-state LS spectator protection.

## 3. A complete five-state shelving candidate

The fixed code uses S_(1/2),m=-1/2 as |0> and D_(5/2) states
`m=-3/2,-1/2,-5/2,+1/2` as |1>,...,|4>. Choose the unused
`|a>=|D_(5/2),m=+3/2>`. A phase-calibrated resonant 729 nm pi pulse can
transfer |0> to |a>, leaving the four code D states untouched in the ideal
resolved-transition model. The change in m is +2; the other unused D state
at +5/2 would require the forbidden direct change +3 from this S state.
The S(-1/2)-D(+3/2) transition is explicitly used in [Hilder et al.][hilder],
published Appendix A2; its use there is a qubit preparation operation.

Write the shelving isometry as

```text
V|0> = exp(i phi)|a>,       V|j> = |j>, j=1,2,3,4.
V sum_j alpha_j|j> = exp(i phi)alpha_0|a> + sum_(j=1)^4 alpha_j|j>.
```

V is the restriction of a six-level unitary; its calibrated inverse restores
all amplitudes and coherences, including correlations with other registers.
No spectator measurement, source reset or blank logical register is involved.
The extra D level and its control are nevertheless physical resources.

This solves the dimension problem. It does **not** solve the force or phase
problem. On the hidden five-D subspace the effective LS operator must be
scalar, or its nonscalar part must be bounded or refocused. Hrmo's neglect
of differences among four code D shifts does not establish equality for all
five hidden states including |a>. These states also have different Zeeman
energies. Known, reproducible one-ion phases can be tracked and corrected;
unknown drift, state-dependent scattering or phases conditioned on another
ion cannot be removed by merely naming a local phase frame.

There is a separate 729 nm trap: a globally applied R_(0,j) echo excites
the spectator amplitude already in D_j back into S. Shelving |0> alone
does not make the occupied original D levels dark to the active-pair X5
cycles. Every echo and external local macro must therefore address only its
intended ions, with off-resonant effects on all occupied levels included.
Accidental driving of |a> must also be excluded. Replacing this requirement
by common 729 nm pulses would invalidate the proposed protection.

For a deliberately unoptimized schedule, hide each of the five spectators
before each of the 56 G gates and unhide it afterwards. This adds at most
`56*5*2=560` ideal one-ion shelving pi operations. Consecutive compatible
gates may share a hiding interval. Composite transfer pulses, calibration
corrections and phase compensation increase the physical pulse count; 560
is not a bound after arbitrary error-suppression overhead is added.
Their durations and all hidden-state storage intervals belong in the time
and decay account. Hiding populations in D does not extend its lifetime.

## 4. Residual force and all-mode closure

In the declared Lamb-Dicke, rotating-wave, harmonic force model, during
an LS segment write

```text
H_I(t)/hbar = sum_m [F_m(t) a_m^dagger + F_m(t)^dagger a_m],
F_m(t) = sum_i sum_j f_(imj)(t) |j_i><j_i|.
```

The coefficients include spatial illumination, mode participation, light
shifts and optical phases. There are seven axial modes; any coupled radial
modes must be included too. For a fixed electronic branch ell, the final
displacement is `alpha_m(ell)=-i integral_0^T F_m(t;ell) dt`, with the
oscillatory mode phases already included in F_m. Piecewise ideal permutations
may be incorporated by tracking the label history. Finite overlapping
carrier/LS drives require the more general joint dynamics instead.

Closing one COM loop does not imply closure of the other modes. A strong
clean-bus condition is `alpha_m(ell)=0` for every included mode and every
allowed branch. A common nonzero displacement might preserve the data but
changes the bus resource; it must not be called apparatus restoration.

Even closed loops can leave unwanted geometric phases. After removing the
desired pair gate and calibrated one-ion phases, the residual phase must
be independent of every spectator branch. For a pair label A and spectator
label j, separability requires, modulo 2pi,

```text
Phi(A,j)-Phi(A',j)-Phi(A,j')+Phi(A',j') = 0.
```

Analogous conditions cover spectator-spectator correlations. A nonzero mixed
difference is a conditional phase error, not a correctable one-ion Z phase.

If all hidden-state force coefficients for an ion are equal, that ion's
force is proportional to identity on its logical subspace. It can still
drive the bus and shift the active-pair phase, which must be calibrated,
but it cannot imprint its hidden logical label through that force term.
The measured differences between coefficients, rather than their merely
small average, determine the missing spectator error.

For independent thermal modes with occupations nbar_m, residual displacements
multiply a branch coherence by a factor of modulus

```text
exp[-sum_m (nbar_m+1/2)|alpha_m(ell)-alpha_m(ell')|^2].
```

This is a diagnostic within the stated harmonic model, not an experimental
error certificate; leakage, scattering, mode heating and nonthermal or
correlated bus states require their own analysis. Measuring unchanged mean
phonon number alone cannot certify these coherence conditions.

## 5. Route choice and a finite acceptance gate

| Route | Evidence and practical disposition |
|---|---|
| Addressed 401 nm force plus addressed 729 nm pulses | Closest route to the original compiler; calibrate the five edges and all coupled modes. The 2026 LS addressing abstract supplies development evidence, not the required error numbers. |
| Broad LS illumination plus full five-D shelving | Concrete candidate above; retains a static chain. Requires five-D differential-force and phase tests, selective echoes, and transfer-error accounting. Do not assume perfect darkness. |
| Shuttle only the active pair to a gate zone | Spatial isolation has a strong Ca-qubit precedent; changes the trap, routing, phase and motion resources. No published unknown-ququint transfer certificate was located here. |
| Global force with refocusing | [#1369][refocusing] is an existing conditional 500-loop isolation construction with a larger carrier, not an experimentally validated replacement preserving the 280-loop budget. |

For a concrete transport comparison, [Hilder et al.][hilder] demonstrate a
six-Ca-qubit register with pairwise gate-zone access. Published Sec. III and
Appendix C give 120-microsecond entangling gates at 99.6(2)% subspace-cycle
performance, 20.9 microseconds per neighbouring-segment move, a 50.6-microsecond
settling wait, roughly 100-microsecond separation and 60-microsecond rotation.
The encoding is a ground-state Zeeman qubit, with transverse gate modes;
these numbers cannot be substituted for optical-ququint routing or gate error.

The recommended next hardware test is **one G on one required edge with all
five spectators occupied**, including coherent five-state inputs. First
certify the hide/idle/unhide channel; then add the active gate and check
spectator reference coherence, mixed phases and residual motion. Repeat on
all five edges and at both required phase angles before using the full C.
Direct local illumination is preferred when available; shelving is a
specific fallback candidate whose additional obligations are explicit.

For an operational 90% or 99% guarantee, choose a composable channel metric.
With `delta=0.5*||E-U||_diamond`, delta bounds every output-event probability
change, also with a reference. In a justified composition model, sufficient
conditions are `sum delta_k <= 0.10` or `<=0.01`, respectively. If all that
budget were assigned to isolation alone, a uniform allocation over 56 uses
would require `delta_iso <=0.10/56` or `0.01/56`; all other errors consume
part of the same budget. For 560 additional transfers the analogous ceilings
are `0.10/560` and `0.01/560`. These are requirements, not measured fidelities.

Without compatible measured bounds, the disposition is **not yet certified
at either target**, rather than physically impossible. A population truth
table, a two-ion Bell-state fidelity, or a 729 nm Rabi-frequency crosstalk
ratio does not supply the missing complete seven-ququint channel bound.

[claim]: https://github.com/mathorn1973/twist-j/issues/1446
[prior]: https://github.com/mathorn1973/twist-j/tree/4699d2b651dda6cb17a71492a47e47e14831e969/notes/C-U-CA40-CONTACT-REALIZATION-AUDIT-N
[hrmo]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10115791/
[dpg]: https://www.dpg-verhandlungen.de/year/2026/conference/mainz/part/q/session/67/contribution/9
[pogorelov]: https://journals.aps.org/prxquantum/pdf/10.1103/PRXQuantum.2.020343
[nigg]: https://arxiv.org/pdf/1403.5426
[hilder]: https://journals.aps.org/prx/pdf/10.1103/PhysRevX.12.011032
[refocusing]: https://github.com/mathorn1973/twist-j/pull/1369
