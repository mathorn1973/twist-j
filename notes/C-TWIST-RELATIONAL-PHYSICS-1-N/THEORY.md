# TWIST-J as a finite relational physical candidate

**C-TWIST-RELATIONAL-PHYSICS-1-N. NON-CANONICAL.**
Author: A. M. Thorn. License: Apache-2.0.

This document specifies one effective physical theory of a finite quantum
source, contact interaction, occupied memory and clock readout. It uses public
TWIST-J v106 as its mathematical input and adds explicit physical postulates.
It is a complete definition of this selected sector's states, preparation
family, energy constraint, observations and single-read probabilities. It is
not a completed fundamental theory of particles or gravity.

## 1. The physical choice

The primary object in this candidate is a stationary joint quantum state.
Operational time is a reading of a named subsystem correlated with the rest.
The native integer `n` in `N_0 x F_5^6` remains part of the separate arithmetic
model. It is not identified with a universal physical time, the new clock
outcome, a program-cursor position, or proper time.

This is an explicit physical choice. It does not simultaneously adopt the
native counter as an observable cosmic evolution parameter. The native rule
and the public integer/residue bridges remain meaningful at their proved
scopes; a derivation of this complete apparatus from that rule is not among
the premises already established.

The general stationary-clock mechanism is Page and Wootters' relational-time
idea, with finite history-state formulations developed in the literature
[R1, R2]. The mathematical contribution proposed here is the exact composition
with the particular complete TWIST-J apparatus [S1-S3], including its source,
three contact/record steps, unknown old memory, physical pointer and finite
completion window. Its physical meaning is fixed by the following postulates.

## 2. Carrier and matter degrees of freedom

Use the exact eleven-register data space

\[
\mathcal D=(\mathbb C^{15})^{\otimes3}\otimes\mathbb C^4
\otimes\mathbb C^3\otimes(\mathbb C^{26})^{\otimes2}
\otimes\mathbb C^3\otimes(\mathbb C^2)^{\otimes3}.
\]

Its dimension is `657072000`. The registers are `R,r,c,o,a,l,m,q,b,s,d`.
The first three encode the center coordinate, relative coordinate and carrier
coordinate in the admitted period-15 realization. `o` stores four object
channels; `a` distinguishes a stationary token and two pulse banks; `l,m`
are the carrier and receiver labels. `q,b` are preparation helpers, `s` is
the retained coherent source setting, and the final two-state `d` is the
write pointer. This last register name is unrelated to the dimension below.

Add the inherited program cursor `P` and the new reference clock `C`, both
of dimension `d_clock=561`. The complete modeled carrier is

\[
\mathcal H=\mathbb C^{561}_C\otimes\mathbb C^{561}_P\otimes\mathcal D.
\]

An arbitrary passive reference may be tensored with this space. It carries
zero Hamiltonian in this account. Unknown old-memory/reference correlations
are preserved; they are not replaced by classical inputs or clean workspace.

**Postulate P1.** These registers and their observables describe the chosen
physical system. Density operators on the stated carrier are the kinematic
states. The selected physical sector is the fixed-energy shell defined below.
The identification is a physical hypothesis; it is not inferred from the
finite dimension of the native arithmetic alphabet.

The coordinate registers simulate an interacting one-dimensional sector.
Their locality as device registers is different from locality in the encoded
particle positions. The matter content is a specified quantum object pair,
carrier and memory. No register is identified with an observed electron,
photon, gravitational field or three-dimensional space.

## 3. One exact Hamiltonian for source, interaction and record

Take the 140 complete gates `G_1,...,G_140` of [S2-S3], including every
controlled scalar phase. Their finite interaction step is exactly

\[
U_{\rm fin}=P_\beta\Gamma S_R S_r E_{\rm rec}Q_pM_2C_{\rm contact},
\qquad \beta=\frac{4\pi}{5},\quad\theta_{\rm contact}=\frac{2\pi}{5}.
\]

Here `C_contact` names the source-contact gate, distinct from reference
clock `C`. The object mixing is
`M2=((I+2iX) tensor (I+2iX))/5`; the source-contact rotation has entries
`3/5,-4/5,4/5,3/5`; the receiver edge retains the complete carrier-memory
label swap. Full raw-space matrices, reflections, inverse operations and
source settings are fixed by [S2-S3], rather than chosen after an outcome.

The word performs source preparation, coherent setting, exactly three
original admitted record steps and the final memory-to-pointer unitary.
The last gate flips the initially zero pointer precisely on receiver label
`d_0`. Before that gate the pointer remains zero. Pad the word by identities
to `K=560`, put `A_m=G_m...G_1`, `A_0=I`, and define

\[
\mathcal W=\sum_{m=0}^{560}|m\rangle\langle m|_P\otimes A_m,
\]

\[
H_A=\mathcal W\left[\left(E_{\rm ctl}I-
\frac{2E_{\rm ctl}}{561}S_x\right)\otimes I_{\mathcal D}\right]
\mathcal W^\dagger,\qquad E_{\rm ctl}>0.
\]

`S_x` is the spin-280 matrix with neighboring entries
`sqrt((m+1)(560-m))/2`. This specifies a self-adjoint positive Hamiltonian
on the full apparatus carrier. Its spectral projectors `P_s` have energies

\[
E_s=\frac{E_{\rm ctl}(2s+1)}{561},\qquad s=0,\ldots,560.
\]

**Postulate P2.** `H_A` is the apparatus energy operator of this candidate.
The new reference clock has

\[
H_C=\frac{2E_{\rm ctl}}{561}\sum_{q=0}^{560}q|q\rangle\langle q|,
\qquad H_{\rm total}=H_C\otimes I+I\otimes H_A.
\]

`E_ctl` is an independent calibration scale. It is neither the contact phase
nor a previously chosen spectral energy `E0 f(U_rec)`. Occupation charge,
logarithmic energy, sine energy and this Hamiltonian are separate operators.
No conservation statement about one is transferred to another by notation.

## 4. Preparation and the stationary constraint

Define the isometry

\[
V\psi=\sum_{s=0}^{560}|560-s\rangle_C\otimes P_s\psi.
\]

For an admitted ready apparatus input
`rho_0=|0><0|_P tensor rho_data,reference`, prepare

\[
R=(V\otimes I_{\rm ref})\rho_0(V^\dagger\otimes I_{\rm ref}).
\]

**Postulate P3.** This exact family of correlated states is physically
admissible. It includes the prescribed source seed, helpers, setting, zero
pointer and the reference-clock correlations. The old memory remains unknown.
Recognition of a fresh write requires its support in
`span(d_1,...,d_25)`. This preparation postulate is not a thermal or native-U
preparation theorem.

Orthogonality of the full apparatus projectors proves `V*V=I`. Each paired
clock/apparatus energy is the same:

\[
\frac{2E_{\rm ctl}(560-s)}{561}
+\frac{E_{\rm ctl}(2s+1)}{561}
=E_*:=\frac{1121E_{\rm ctl}}{561}.
\]

Thus the complete state is stationary, with exactly that positive total
energy. The zero constraint is
`(H_total-E_* I)R=0`; it does not say that physical energy is zero.
Let `Q_*=VV*`, the full projector onto this shell. The shell supports the
physical states of the selected constrained model; the supplied ready
preparations form a specified subset.

A finite preparation unitary exists by extension of an isometry. This
existence does not provide a local device, a thermal source or an energy-
conserving preparation from an uncorrelated ready clock and apparatus.
The correlations and any work/reference resources needed to create them
remain explicit physical inputs.

## 5. What time means

Define the orthonormal clock basis

\[
|t_j\rangle=\frac1{\sqrt{561}}
\sum_{q=0}^{560}e^{-2\pi i qj/561}|q\rangle,
\qquad j=0,\ldots,560.
\]

**Postulate P4.** This is the selected reference-clock reading. Its time
calibration is

\[
\tau_j=\frac{\pi\hbar j}{E_{\rm ctl}}.
\]

The exact conditional identity is

\[
\langle t_j|R|t_j\rangle
=\frac1{561}e^{-iH_A\tau_j/\hbar}\rho_0e^{+iH_A\tau_j/\hbar}.
\]

Every clock outcome has probability `1/561`, independently of source setting,
old memory and passive references. The evolving apparatus density is the
conditional slice of one stationary joint state. No external variable has
to advance for the joint probabilities to be defined.

This is a finite cyclic time reading. The density returns after
`561 pi hbar/E_ctl`; the apparatus unitary at that period is `-I`.
The state contains no cycle number. These clocks do not supply unbounded
elapsed time, permanent records or a proper-time functional on spacetime
paths. They are a named internal subsystem, not a proof of local relativistic
clock behavior.

## 6. Complete observations and outcome law

Let `Pi_0,Pi_1` be the apparatus pointer projectors. Local product effects
`F_jy=|t_j><t_j| tensor Pi_y` give a useful calculation of joint statistics.
They generally do not commute with `H_total`.

For the constrained physical reading use the global effects

\[
E_{jy}=Q_*F_{jy}Q_*,\qquad E_{\rm out}=I-Q_*.
\]

They form a complete POVM on the full carrier, commute with `H_total`, and
give exactly the same ideal probabilities as `F_jy` on `R`. The additional
outcome is kept under preparation errors. Compression is generally nonlocal
and the effects are generally not projectors.

**Postulate P5.** One outcome `a=(j,y)` or `out` occurs with probability
`Tr(E_a R)`. The adopted single-read state-update law is
the square-root instrument

\[
R\longmapsto\frac{\sqrt{E_a}R\sqrt{E_a}}{\operatorname{Tr}(E_aR)}
\]

for a positive denominator. This is an explicit effective measurement law,
not a derivation of Born probabilities or outcome occurrence from `J`.
The update is well defined and preserves the energy shell on ideal input.
Its physical implementation, spatial support and external display are not
supplied by the compact apparatus theorem.

The conditional slice in Section 5 is **not** asserted to be the actual
free apparatus state after this instrument. Every state in the energy shell
has an apparatus marginal diagonal between distinct apparatus energies.
A shell-preserving read cannot at the same time release the generally
energy-coherent conditional slice as an uncorrelated apparatus state.
Relational conditional statistics and actual measurement disturbance have
different roles in this theory.

## 7. A sharp prediction on the same carrier

Use the two fixed source settings of `ACTIVE-ISOSPECTRAL-RECORD`. Their
prepared source states have the same initial configuration populations and
the same complete spectral distributions of `U_rec`. After the prescribed
three steps their fresh-record probability difference is exactly

\[
\Delta=\frac{65536(48533-10985\sqrt5)}
{5^9(39521+154\sqrt5)}>\frac1{50}.
\]

This value is inherited from [S1]. It is not an experimental measurement.
The compact apparatus has the same full Hamiltonian spectral law for both
ready settings. The new stationary whole has the same total energy `E_*`
for both. A different record is therefore a test of the specified coherent
preparation and readout, not a hidden difference in total energy.

Conditional on clock value `j`, program-cursor completion has weight

\[
B_j=\sum_{m=140}^{560}\binom{560}{m}
\sin^{2m}\!\frac{\pi j}{561}
\cos^{2(560-m)}\!\frac{\pi j}{561}.
\]

Every completed prefix gives the same endpoint. Every earlier prefix has
pointer zero. Consequently the exact pointer difference is `B_j Delta`.

Select the event **clock `187,...,374` and pointer one**. It is defined
before any observation. Its setting difference per prepared trial is

\[
\boxed{\delta_{\rm joint}=\frac{\Delta}{561}
\sum_{j=187}^{374}B_j>\frac{47}{14025}.}
\]

There are 188 accepted clock values, with total clock probability `188/561`.
All other clock values, pointer zero and `out` remain in the outcome space.
The inequality therefore includes the cost of the clock window. It is not a
success-conditioned contrast with rejected events silently removed.

The bound follows from `sin^2(pi j/561)>=3/4` on that window and
`1-B_j<(3/16)^140<2^(-280)`. `PROOF.md` supplies the complete derivation
for mixed inputs and arbitrary allowed reference correlations.

## 8. Empirical meaning and a fixed robustness requirement

**Postulate P6.** Application to an actual apparatus requires independently
specified physical encodings, preparation and measurement implementations,
and a calibration of `E_ctl` and the clock. Dimensionless probabilities are
predicted before SI units are assigned. No measured mass or time scale is
reused as an alleged independent prediction.

Let actual joint preparations differ from their ideal states by trace
distances at most `epsilon_+` and `epsilon_-`. Let the implemented joint-event
effect differ in operator norm by at most `eta`. The contrast can change by
at most `epsilon_++epsilon_-+2eta`. The fixed sufficient budget

\[
\epsilon_+,\epsilon_-,\eta\le\frac1{10000}
\]

therefore gives the robust prediction

\[
\delta_{\rm actual}>\frac{47}{14025}-\frac1{2500}>\frac1{400}.
\]

These full-state and effect bounds are demanding mathematical sufficient
conditions. They are not achieved hardware precision or a claim that full
tomography of this large model is practical. They cover the new clock and
correlated preparation, which the inherited apparatus tolerances do not.

A physical test prepares both fixed settings, counts every outcome, and
compares their frequencies for this one predeclared event. Under independently
established error bounds, a statistically reliable discrepancy falsifies the
selected physical model or its claimed applicability. Before collecting data,
the hardware protocol must additionally fix trial counts, dependence between
trials, error characterization and a statistical rejection rule. No such
experimental execution is claimed here.

Realizing the channel on a programmable quantum device would establish an
implementation of this model. A fundamental claim about nature additionally
needs a predeclared mapping to an independently observed physical system and
predictions not used to select that mapping.

## 9. What is established and what is still a hypothesis

| Item | Status in this candidate |
| --- | --- |
| Complete source/contact/occupied-memory apparatus | Inherited conditional mathematical theorem [S1-S3] |
| Finite stationary extension on one declared carrier | New analytical construction; exact checks supplied |
| Complete joint-event formula and strict lower bound | New conditional mathematical consequence |
| Choice of carrier, preparation, clock, energy and readout | Explicit physical postulates P1-P6 |
| Actual material preparation and readout | Not demonstrated |
| Born law and outcome occurrence | Adopted effective physical law |
| Native-U realization of the whole apparatus | Not derived |
| Electron/photon identification | Not made |
| Proper time, full Lorentz symmetry and gravity | Not supplied |
| Thermodynamic arrow and permanent archive | Not derived; finite recurrence remains |

The fixed `mu=2` walk cannot simply be named an ordinary relativistic
electron under the common frequency/wavevector energy-momentum reading.
`PHYSICS_BOUNDARY.md` gives the analytic mismatch
`m_in/m_rest=2/atan(2)`. A continuum limit requires a stated scaling;
an exact sine-shell identity is a different energy-momentum dictionary.
Neither choice is smuggled into this apparatus Hamiltonian.

The direction of the computational history is selected by the ready boundary,
gate order and clock convention. Entropy is not used to manufacture a time
orientation. The finite stationary model includes the return that undoes
the unmeasured record. Durable archives require additional resources and a
separate protocol.

The resulting object is an explicit physical hypothesis for a bounded sector.
Its value is that states, time readings, interactions, records and predictions
can now be checked together under one declared interpretation.

## References and pinned inputs

- **S1:** [Public Canon v106 at the fixed main commit](https://github.com/mathorn1973/twist-j/blob/a193e389fb1ddb0bdc89165b015c95a17eb1e425/canon/CANON.md), sections `ACTIVE-ISOSPECTRAL-RECORD` and `COMPACT-ACTIVE-RECORD-APPARATUS`.
- **S2:** [Complete compact apparatus](https://github.com/mathorn1973/twist-j/blob/a193e389fb1ddb0bdc89165b015c95a17eb1e425/notes/C-COMPACT-ENERGY-RECORD-N/COMPACT_MODEL.md).
- **S3:** [Complete source circuit](https://github.com/mathorn1973/twist-j/blob/a193e389fb1ddb0bdc89165b015c95a17eb1e425/notes/C-ORIGINAL-PORT-SOURCE-PREPARATION-N/SOURCE_CIRCUIT.md).
- **R1:** D. N. Page and W. K. Wootters, [Evolution without evolution: Dynamics described by stationary observables](https://doi.org/10.1103/PhysRevD.27.2885), Physical Review D 27, 2885 (1983).
- **R2:** A. Boette and R. Rossignoli, [History states of systems and operators](https://arxiv.org/abs/1806.00956v2), Physical Review A 98, 032108 (2018).
