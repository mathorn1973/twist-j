# A concrete calcium-ion carrier and source contract

**PUBLIC, NON-CANONICAL. Analytical realization audit; no experiment or
scientific program executed for this note.**
Reservation: [issue #1444][reservation].
Branch: `codex/v101-ca40-contact-audit`.
Source base: `408fc7a34cbd8113b4d5e1dac43793c7ad0270b0`.
Original text: Apache-2.0. Date: 2026-10-10.

## 1. Selected physical ingredient and exact label dictionary

We select the optical ququint of Hrmo, Wilhelm et al. (2023), which
experimentally entangles two five-level Ca-40 ions. Its Fig. 1 gives the
following encoding, transcribed from the published diagram. [H23]

| Label | Ca-40 ion electronic level |
| --- | --- |
| 0 | 4S_(1/2), m_J=-1/2 |
| 1 | 3D_(5/2), m_J=-3/2 |
| 2 | 3D_(5/2), m_J=-1/2 |
| 3 | 3D_(5/2), m_J=-5/2 |
| 4 | 3D_(5/2), m_J=+1/2 |

The reported apparatus has two ions, approximately 3.6 G bias field and
1.1 MHz axial centre-of-mass frequency. Preparation uses Doppler and
resolved-sideband cooling (mean axial occupation about 0.1), then optical
pumping. Resonant 729 nm rotations connect label 0 to the four D levels.
The entangler uses 401.2 nm light and shared motion. [H23]

These are measured physical ingredients, independently motivated by atomic
spectroscopy and quantum control. Their selection does not select the
TWIST-J contact law from nature. The allocation below and the compilation
of the requested arithmetic are new engineering choices.

| Proposed ion | Encoded coordinate | Role during the contact |
| --- | --- | --- |
| 1 | s | independent source |
| 2 | x | receiver control |
| 3 | u | receiver target |
| 4 | y | receiver control |
| 5 | w | receiver target |
| 6 | q | spectator data |
| 7 | r | spectator data |

All labels are elements of F5 represented by integers 0,...,4. The direct
physical encoding is of the **centred** coordinates

```text
x=p1-1, u=p4-3, y=p1p-4, w=p4p-2, h=y-x,
|s,x,u,y,w,q,r> -> |s,x,u-2sh,y,w+2sh,q,r>.          (1)
```

Thus an energy attached to label u is the physical energy of that table
entry, not the energy of label p4. A raw-p encoding would require explicit
centering and uncentering operations and their own time/work accounting.
It is not used in this audit.

The ideal computational subspace is (C^5)^(tensor 7). This is a subspace of
seven ions' atomic Hilbert spaces, not their complete physical carrier.
Leakage levels, collective vibrational modes, electromagnetic fields,
control electronics and dissipative environments remain outside this
notation; none is thereby discarded from a physical account.

## 2. What source preparation means

The source preparation ends at a declared time before the contact begins.
Cooling, pumping, heralding and any discarded photons before that boundary
belong in the preparation account. Applying them to an unknown incoming
source during the contact would be a reset, not preservation.

**Known basis input.** Prepare label 0 by pumping, then use a calibrated
0-to-s pi rotation when s is nonzero. The ideal output is |s><s|. Its
global preparation phase is irrelevant for that basis input. Randomly
choosing s prepares a diagonal mixture, but any retained randomizer record
must remain in the declared environment.

**Known coherent input.** Use phase-controlled rotations. For an explicit
ideal |+>=5^(-1/2) sum_s |s> preparation, define

```text
R^(0,j)(theta,phi)
 = exp[-i theta (cos(phi) sigma_x^(0,j)
                  + sin(phi) sigma_y^(0,j))/2],
sigma_y^(0,j) = -i|0><j| + i|j><0|.
```

Starting at |0>, apply j=4,3,2,1 in that chronological order, with
theta_j=2 asin(1/sqrt(j+1)) and phi=pi/2. The transferred amplitude at
each step is positive 1/sqrt(5); the final label-0 amplitude is the same.
This is an exact pulse-area construction in the ideal addressed rotation
model, not a newly measured preparation fidelity. A physical implementation
must calibrate optical phases and compensate known free evolution.

**Unknown input.** Accept the actual source density matrix, including any
reference correlations, without tomography, measurement-and-repreparation,
or source-dependent receiver initialization. Its readiness specification
must identify the incoming encoding, leakage allowance and phase frame.
An arbitrary unknown source is not supplied by the known-input protocol.

The previous [complete-source proof][source] fixes the ideal implications:

- Each basis source, and each diagonal source mixture, has its marginal
  preserved by (1). This is a useful commuting source family.
- For a fixed receiver basis input with h!=0, the five receiver outputs are
  orthogonal. The source channel is complete dephasing in the s basis;
  |+><+| becomes I_5/5. The occupied-SUM checkpoints satisfy this premise.
- Preservation of every unknown source state, including its reference
  correlations, cannot coexist with an informative retained archive under
  the stated deterministic channel and independent-ready-state assumptions.
  Undoing the complete contact also undoes its record.

Ca-40 supports coherent control of these electronic levels, so the
distinction is operationally relevant to this candidate. Restricting the
source promise to basis states must be explicit. It is not evidence for
preservation of the complete arbitrary quantum source.

## 3. Published timing and readout versus the proposed protocol

In [H23], one closed motional-loop pulse has t_LS=2pi/delta, typically
about 35 microseconds. The d=5 composite gate contains five such pulses
interleaved with cyclic permutations. Measurement uses 397 nm fluorescence
and 729 nm transfer/analysis pulses. Its estimated SPAM-corrected d=5 gate
performance is 93.7(3)%; the authors explicitly caution about non-Markovian
noise. This is neither a contact fidelity nor an all-input channel bound.

For that pulse architecture the bookkeeping identity is

```text
T_G = sum_(k=1)^5 t_LS,k + sum_(k=1)^5 T_X5,k,
T_X5,k = sum_(j=1)^4 t_pi,k,j,                         (2)
```

when the four transition pulses comprising each permutation are sequential
and applied to both selected ions together. Local addressing or routing can
add time. Multiplying 35 microseconds by five accounts only for the force
pulses at that illustrative setting. It does not determine T_G for every
phase angle, much less the duration of the full contact circuit.

For the proposed preparation, calibrated pulse envelopes must satisfy
integral Omega_j(t) dt=theta_j. For a constant resonant drive this gives
t_j=theta_j/|Omega_j|. No numerical Omega_j is assigned here. A complete
preparation duration requires the cooling, pumping, transfers, switching
and stabilization times; a retention interval requires the full compiled
schedule. Those numbers are not filled by a native integer tick.

Ringbauer et al. demonstrate multi-ion qudit control; the published Figs. 2
and 3 identify an eight-ion register, with qutrit entangling tests. Their
author manuscript reports ququint Clifford error 1.0(2) percent, and pulse
error 3.2_(−0.7)^(+0.8) times 10^(-4). Its sequential fluorescence scheme
uses shelving and recooling; the quoted 500-microsecond detection and
2500-microsecond recooling setting is a qutrit readout example. [R22]

These observations do not establish a seven-ion version of the selected
S-plus-four-D LS gate. The 2022 and 2023 experiments and encodings must not
be silently combined into a single measured device specification. Neither
the quoted Clifford error nor the qutrit readout setting is a certified
seven-ququint source-preparation/readout budget.

The proposed seven-ion instrument therefore needs state-resolved readout
calibration for all five labels on every measured ion, an explicit
leakage outcome, and a rule for reporting rejected runs. Receiver measurement
is after the declared contact boundary. Fluorescence measurement of the
source cannot demonstrate preservation of its premeasurement coherences;
separate phase-sensitive validation is necessary on independently prepared
trials.

## 4. Retention and omitted physical resources

For the ideal map (1), q and r have the identity channel, including their
coherences and correlations with a noninteracting reference. In the proposed apparatus they are
other ions sharing fields and motion. Absence from the algebraic gate list
does not imply immunity to off-resonant light shifts, scattering or heating.
Pair selection and spectator protection are explicit additional premises.

A closed trajectory of the ideal driven oscillator restores its motional
state at a gate boundary. It does not imply that seven-ion spectator modes,
leakage populations, scattered radiation, or the controller have returned
to their inputs. Those factors require separate evidence for the actual
pulse sequence, with the approximations of the force model exposed.

The claimed source boundary must be fixed. A certificate restricted to
computational-subspace inputs does not cover leakage inputs or unmodelled
motional and environmental degrees of freedom. A normalized postselected
five-level state also does not certify the probability of remaining in that
subspace. Neither certificate returns every source-associated preparation
device and environment. Shared motion cannot be assigned to the source or
receiver differently at different stages to conceal a change. If motion
or a controller is external, its final state and correlations still count
in the full physical process and work ledger.

Atomic label arithmetic is modulo five; laboratory energy is not. The
selected S/D levels are not a degenerate five-state memory. Lasers, trap
drives, cooling and measurement participate in the physical energy account.
A restored motional mode alone does not prove zero work. No numerical
total preparation energy, gate work, dissipated heat or reset cost is
inferred from the published fidelity and pulse duration.

The completed part of this file is a concrete carrier/preparation boundary.
Actual seven-ion pair access, error thresholds, SI timing, physical-source
retention and the complete work account remain protocol obligations. No
TWIST-J native-law admission or apparatus-owner closure follows.

## 5. Why not the cited barium alternative

Low et al.'s Ba-137 ground-hyperfine proposal uses the five-state zigzag
encoding (F,m_F)=(2,-2),(1,-1),(2,0),(1,1),(2,2). Its final paper reports a
simulated d=5 entangling fidelity of only 2.96 percent due to off-resonant
couplings, and explicitly limits applicability of that gate/encoding.
This is a specific obstruction to adopting that proposal unchanged, not
a no-go theorem for barium. [L20]

## Source locators

- **[H23]** P. Hrmo, B. Wilhelm et al., *Native qudit entanglement in a
  trapped ion quantum processor*, Nature Communications **14**, 2242 (2023),
  [published full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10115791/).
  Published Fig. 1 fixes the level dictionary; Results, Eqs. (1)-(6), fix
  the force, rotations and pulse sequence. The [author PDF][h23pdf] has
  Fig. 1 on PDF p. 2, apparatus on p. 3, preparation/readout on p. 4 and
  fidelity discussion on p. 5. Page numbers here refer to that PDF.
- **[R22]** M. Ringbauer et al., *A universal qudit quantum processor with
  trapped ions*, Nature Physics **18**, 1053-1057 (2022),
  [published figure captions][r22], Figs. 2-4; [full author manuscript][r22author],
  Figs. 2 and 4 and Supplementary Sections I-III. Numerical settings above
  are attributed to the author manuscript rather than silently identified
  with every configuration in the final paper.
- **[L20]** P. J. Low et al., *Practical trapped-ion protocols for universal
  qudit-based quantum computing*, Physical Review Research **2**, 033128
  (2020), [published PDF][l20], pp. 033128-3--4 (encoding), 033128-12--13
  (specific d=5 obstruction and Table VI). Proposed/calculated performance
  is not an experimental two-ququint demonstration.

[reservation]: https://github.com/mathorn1973/twist-j/issues/1444
[source]: ../C-U-CONTACT-FULL-SOURCE-ADMISSION-N/SOURCE-PROOF.md
[H23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10115791/
[h23pdf]: https://arxiv.org/pdf/2206.04104
[r22]: https://www.nature.com/articles/s41567-022-01658-0
[r22author]: https://arxiv.org/html/2109.06903
[l20]: https://journals.aps.org/prresearch/pdf/10.1103/PhysRevResearch.2.033128
