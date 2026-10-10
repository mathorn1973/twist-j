# Energy, work, and resource boundary for the Ca-40 contact

PUBLIC NON-CANONICAL analytical hardware comparison; no physical admission.
Reservation: [#1444](https://github.com/mathorn1973/twist-j/issues/1444).
Branch: `codex/v101-ca40-contact-audit`.
Public main base: `408fc7a34cbd8113b4d5e1dac43793c7ad0270b0`.
Date: 2026-10-10. License: Apache-2.0.
No scientific program, pulse simulation, or experiment was performed for this note.
The component balance is symbolically closed; a numerical full energy account
is **NOT PROVIDED**. The contact is an assumed target operation, not an observed
seven-ion implementation or a native TWIST-J Hamiltonian.

## 1. Freeze the physical label chart before assigning energy

Seven ququints encode `(x,u,y,w,q,r,s)` directly into physical levels 0 through 4.
Here `x,y,u,w` are the declared centered-chart fields, not raw `p` labels.
The representative contact, with all arithmetic in F5, is

```text
a=2(y-x)s,
C(x,u,y,w,q,r,s)=(x,u-a,y,w+a,q,r,s).
```

This note uses the selected Ca-40+ encoding from Hrmo et al., Fig. 1:

| Label | Physical level | Magnetic quantum number |
|---|---|---|
| 0 | S(1/2) | -1/2 |
| 1 | D(5/2) | -3/2 |
| 2 | D(5/2) | -1/2 |
| 3 | D(5/2) | -5/2 |
| 4 | D(5/2) | +1/2 |

[Primary experiment][hrmo]. This mapping is part of the hardware contract.
If raw `p` labels are instead encoded, the chart K must be inserted explicitly:
the centered operation is K C_raw K^-1 and the energy indices change with K.
One must not reuse this note's witness with the raw labels left unshifted.

For an ion j, use its measured lab-frame energy epsilon_j,l(B). In the linear
Zeeman approximation, with additional calibrated shifts delta_j,l retained,

```text
epsilon_j,0(B)=E_j,S-(g_S/2) mu_B B + delta_j,0,
epsilon_j,l(B)=E_j,D+g_D m_l mu_B B + delta_j,l,  l=1,...,4.
H_Q(B)=sum_j sum_l epsilon_j,l(B) |l><l|_j.
```

The delta terms can include electric-quadrupole, Stark, and higher-order shifts.
This is not an assertion of exact LS-coupling g factors or uniform spacing.
Even at zero B, the S-D optical gap remains. At finite B the D labels are
also split, in the non-monotone label order fixed above.

## 2. Exact endpoint change and a concrete energy witness

For a basis input with target labels u,w and a=2(y-x)s, the additive bare
register energy change is exactly

```text
Delta E_Q = epsilon_uion,[u-a]_5 + epsilon_wion,[w+a]_5
            - epsilon_uion,u - epsilon_wion,w.
```

The endpoint contributions of x,y,q,r,s cancel. For an arbitrary register
density matrix, average this expression with its basis populations: C is a
permutation of the energy basis, so coherences do not affect this endpoint mean.
This does not remove their role in faithful coherent gate implementation.

Take centered x=0, y=1, u=w=0, s=1, with arbitrary fixed q,r. Then a=2 and
the two target labels become (3,2). Both targets undergo S-to-D excitation;
the source label 1 and every spectator label are unchanged. Thus

```text
Delta E_Q = (epsilon_uion,3-epsilon_uion,0)
          + (epsilon_wion,2-epsilon_wion,0).
```

For identical spectra and common B this is
`2(E_D-E_S)+(g_S-3 g_D) mu_B B+delta_3+delta_2-2 delta_0`.
The optical contribution has scale `2 h_P c/(729 nm)`; this is an endpoint
energy scale, not measured gate work, input optical pulse energy, or electrical
consumption. The witness is on the full declared carrier; it is not asserted
to be an occupied-SUM preparation. No numerical contact energy was measured.

There is also an all-state obstruction independent of this witness. For any
nonzero a, energy conservation for all independent u,w would require
`epsilon_uion,[u-a]-epsilon_uion,u` to be a constant independent of u.
Summing it over the five-cycle gives zero, so the constant is zero. A nonzero
F5 step visits all five labels, forcing all five target energies to be equal.
The same argument applies to the other target. Therefore C cannot commute
with this additive bare Hamiltonian on the full carrier unless both target
ququints are degenerate. Optical S-D encoding fails that condition.
Restricted input sets or individual inputs require their own assessment.
Conservation of u+w modulo 5 is not conservation of real-valued energy.

## 3. Minimal complete ledger and its boundary

Choose one physical boundary and count each energy term once. A sufficient
schematic partition is `H_tot=H_Q+H_M+H_F+H_K+H_B+H_R+V_cross`:

| Component | Required account | Missing contact-specific input |
|---|---|---|
| Q: seven internal ions | Actual levels, shifts, populations, leakage | Calibrated spectra, prepared state, measured output |
| M: ion motion | All relevant modes, micromotion, kinetic/trap/Coulomb energy | Seven-ion mode structure, initial/final occupation and residual displacement |
| F: fields and supplies | Laser modes, RF source, DC electrodes, magnetic-field source | Incident/outgoing fields, pulse envelopes, source energy changes |
| K: control | Clock, switching electronics, phase reference, feedback | Controller state/energy changes, backaction, reset cycle |
| B: environment | Cooling reservoirs, scattered/emitted photons, heating channels | Energy fluxes, bath states and temperatures where applicable |
| R: readout and memory | Fluorescence, detection, stored outcomes, erasure | Detection/reset protocol and retained side information |
| V_cross | Ion-field, spin-motion, system-bath and other cross-boundary couplings | Endpoint interaction energies and switching contributions |

Trap potentials and field energy cannot both include the same interaction
without an explicit allocation convention. An effective pseudopotential is
not a ledger for the RF power supply. A static B may have constant field
energy while its real coil supply dissipates power. Leaving those supplies
outside the boundary requires explicit incoming energy fluxes.
For a complete autonomous, isolated, time-independent H_tot,

```text
Delta <H_tot> = sum_A Delta <H_A> + Delta <V_cross> = 0.
```

This says neither Delta E_Q=0 nor zero resource consumption. A boundary with
external electrical/optical inputs is open and must include those inputs.
Initial and final times must be specified: one contact pulse sequence, or a
full prepare-contact-read-reset cycle, are different accounting questions.

## 4. Driven work, heat, phases, and reference frames

For unitary evolution under `H(t)=H_S(t)+H_B+V(t)` with fixed H_B,

```text
W_ext = integral dt Tr[rho(t)(dot H_S(t)+dot V(t))],
Delta E_S = W_ext - Delta E_B - Delta <V>.
```

This is the explicit inclusive balance in Esposito et al., Eqs. (10)-(12).
Under their thermal-reservoir convention, heat into S plus its assigned
interaction is Q=-Delta E_B. Omitting Delta<V> or dot V needs justification,
not a change of notation. [Primary derivation][esposito]

The identity `d<E_S>=Tr(rho_S dH_S)+Tr(H_S d rho_S)` alone does not identify
all of its second term as heat. With a fixed bare H_Q and coherent drive V_d,
`dot E_Q=(i/hbar)Tr(rho[V_d,H_Q])` already includes coherent energy transfer.
A master-equation heat account must identify the dissipative channels and
their reservoir assumptions separately. A laser is not automatically a bath.

The interaction-frame LS Hamiltonian and its geometric phase are useful gate
descriptions; neither gives a lab-frame energy account by itself. Carrier
energies and the reference-frame transformation must be restored before
evaluating physical energy. Pulse phase, accumulated dynamical/geometric
phase, and energy or work are different quantities. Unknown label-dependent
phases can preserve endpoint populations while failing the coherent C target.

Keep `W_ext`, incident optical energy `integral P_opt,in dt`, net field energy
loss, and electrical energy `integral P_elec dt` distinct. Transmitted and
reflected light is not energy deposited in the ions. Laser/RF inefficiency,
cryogenics, stabilisation, idle power and duty cycle affect electrical cost.
Gate count, pulse area and fidelity alone determine none of these conversions.

## 5. Exact clean-apparatus obstruction

Assume a fixed independent initial apparatus tau_A and exact channel C on
every state rho of the finite register Q. Include all energy-supplying degrees
of freedom in A, assume finite initial/final mean energies, and assume the
same additive endpoint Hamiltonian H_Q+H_A with zero interaction-energy change.
Exact unitary output on Q forces the final apparatus state tau'_A to be
independent of rho: purify tau_A, apply pure-state preservation, and use
linearity on superpositions. This is the usual no-imprinting argument.
Energy conservation then implies

```text
Tr[rho(C^dagger H_Q C-H_Q)] = -Delta E_A = K, for every rho.
```

Thus `C^dagger H_Q C-H_Q=K I`. Its finite-dimensional trace is zero, so K=0
and `[C,H_Q]=0`, contradicted by section 2. The apparatus need not return to
its initial state for this argument: input-independent finite-energy change
already suffices. It is an exact all-state obstruction under named boundary
assumptions, not a numerical error bound or a prohibition of approximate gates.
External classical drive, nonzero endpoint interaction change, restricted
inputs, or an approximate channel changes those assumptions and needs its own
ledger. Finite control backaction cannot be replaced by a free perfect clock.
[Conservation-law precedent][ozawa]; [explicit control-resource framework][woods].

## 6. Source coherence, preparation, readout, and reset

The ideal contact commutes with the diagonal source Hamiltonian, so its source
energy and energy populations are preserved. Complete source state preservation
does not follow: a basis receiver with a nontrivial contact orbit can perfectly
record s and completely dephase the reduced source. The joint ideal state can
retain the coherence in correlations. The earlier [source proof][source-proof]
excludes restoring every unknown source while keeping an informative archive.
Adding energetic resources does not evade that information-theoretic result.

With fixed H_s, a reduced source entropy increase changes
`F_T(rho_s)=Tr(rho_s H_s)-k_B T S(rho_s)` even when its energy is unchanged.
For pure uniform source becoming I/5, Delta F_T=-k_B T ln 5. This is a local
free-energy comparison at a declared T, not proof of heat k_B T ln 5 dissipated
during the contact; joint correlations and the reset contract matter.
Preparing coherent S-D superpositions also requires a phase reference.

Source/receiver preparation, cooling, optical pumping, fluorescence readout,
and classical outcome storage must be included when claiming a repeatable
cycle. An initial projective energy measurement can itself destroy input
coherence. Endpoint mean energy can instead be assessed on separately prepared
ensembles; it does not certify the coherent channel. There is no universal
state-independent work-POVM prescription that, for arbitrary driven processes, both reproduces
two-energy-measurement statistics on diagonal states and the unmeasured mean
energy change on every input state. Particular processes, including an
energy-basis permutation such as ideal C, can satisfy both.
[Primary work-statistics limitation][work]

For jointly unitary evolution of memory M and bath B, initially independent
with B thermal at positive temperature T and fixed bath Hamiltonian H_B,
Reeb-Wolf give (entropy in natural-log units and beta=1/(k_B T))
`beta Q_B=S(M)-S(M')+I(M':B')+D(rho'_B||tau_B)`.
Only the specified erasure of a uniform unknown five-valued memory without
used side information yields the familiar bound Q_B >= k_B T ln 5. Correlated
side information, uncomputation, retained archives and nondegenerate memory
energies require their own account. There is no automatic 7 k_B T ln 5 cost
per reversible contact, and resetting a known state is not restoring an
unknown one. [Primary reset theorem and its assumptions][reeb]

## 7. What publications supply, and what remains unprovided

Hrmo et al. report a two-ion implementation with approximately B=3.6 G,
axial COM frequency 1.1 MHz, radial frequencies 3.5/3.2 MHz, 729 nm control,
401.2 nm light-shift beams and approximately 35 microseconds per LS pulse.
Their ideal motional loop closes after 2 pi/delta. These are component facts,
not a measured seven-ion C implementation or its complete energy bill. [hrmo]

They permit identifying transition and phonon energy scales and an existing
gate mechanism. A numerical account here still lacks the compiled pulse
schedule, calibrated seven-ion Hamiltonian, actual input ensemble, residual
motion/leakage, all field fluxes, control backaction, bath exchanges and
prepare/read/reset cycle. No total joules/contact, wall-plug efficiency,
exact-native gate, zero-work result, or physical TWIST-J admission is supplied.

[hrmo]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10115791/
[esposito]: https://arxiv.org/pdf/0908.1125
[ozawa]: https://arxiv.org/abs/quant-ph/0112179
[woods]: https://arxiv.org/abs/1912.05562
[work]: https://arxiv.org/abs/1606.08368
[reeb]: https://arxiv.org/html/1306.4352v3
[source-proof]: https://github.com/mathorn1973/twist-j/blob/408fc7a34cbd8113b4d5e1dac43793c7ad0270b0/notes/C-U-CONTACT-FULL-SOURCE-ADMISSION-N/SOURCE-PROOF.md
