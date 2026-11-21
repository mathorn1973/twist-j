# P-U-ION-NATIVE-FIRST-STEP-1: effective physical model

NON-CANONICAL. This is a conditional construction of the first native step
on its actual 25 inputs, using a specified data-memory interaction. Public
authority remains Canon v97. It is neither a measured seventeen-ion device
nor a certificate of preparation through the second contact and `n=9`.
Source provenance is in [SOURCES.md](SOURCES.md); the exact construction and
its conservative pulse counts are in [PROOF.md](PROOF.md).

## 1. Fixed physical coordinates and endpoint contract

There are seventeen `40Ca+` internal data factors, one harmonic axial COM
mode, and the explicitly retained external remainder. All seventeen ions,
including memory and the finite counter, use the same Hrmo dictionary [S1]:

| Physical label | Level |
| --- | --- |
| 0 | 4^2 S_(1/2), m_J = -1/2 |
| 1 | 3^2 D_(5/2), m_J = -3/2 |
| 2 | 3^2 D_(5/2), m_J = -1/2 |
| 3 | 3^2 D_(5/2), m_J = -5/2 |
| 4 | 3^2 D_(5/2), m_J = +1/2 |

These labels are not an increasing energy order. The physical ordering is

```text
index:  0   1    2    3     4     5   6  7    8    9    10    11  12 13  14 15 16
factor: S1  S2  R1.p1 p4   p1'   p4'  q  r   R2.p1 p4   p1'   p4'  y  r   M1 M2 N
```

The fixed dictionary of [S0] is retained from initial preparation:
`R2.y=R2.q+4 mod 5`, with decoder `R2.q=y+1 mod 5`; all other data labels
are direct. Memory and counter labels are direct. All five counter levels
can be visited by refocusing pulses, but the counter endpoint claim is
only `N=0 -> N=1`. No unbounded clock or later counter law is supplied.

Let `s=a1+1 mod 5` and `t=a2+1 mod 5`. The supplied input family is the
actual post-first-contact, pre-`U0` family from [S0], for all `(s,t) in F5^2`:

```text
S1=1, S2=t, R1=(0,0,0,0,s,0), R2=(0,0,0,0,0,0),
M1=0, M2=0, N=0.
```

`M1,M2,N` are counted carriers prepared in physical level 0 at initial
preparation, not ancillas inserted or reset at this native-step boundary.
Their readiness at the supplied boundary is an input condition. This
one-step construction does not certify the preceding preparation or contact
in the enlarged apparatus. In particular, an unproved preparation channel
is not replaced by an assertion of fresh common motion.

The required full internal output is

```text
S1=1, S2=t, R1=f(s), R2=(0,0,0,0,3,0), M1=s, M2=1, N=1,
```

where

| s | Native selector | f(s), ordered (p1,p4,p1',p4',q,r) |
| --- | --- | --- |
| 0 | a | (0,0,0,0,0,0) |
| 1 | b | (0,0,0,0,4,0) |
| 2 | c | (2,1,2,1,4,0) |
| 3 | d | (2,1,3,4,3,1) |
| 4 | e | (2,1,3,4,3,1) |

This is the native function on the actual input slice, not the general
controlled native generators on arbitrary receiver contents. The controller
uses one fixed sequence and common endpoint time for all 25 inputs. It
receives no external `s,t` labels. `M1` retains the selector physically;
in particular, the two equal data outputs for `s=3,4` have distinct memory
outputs. No postselection, reset, ignored leakage or failed reading is used.
Known endpoint basis phases are allowed; the declared control-frame
construction and laboratory-frame phase convention are distinguished below.

## 2. Independently fixed parameters and global force

Fix the following finite calibration inputs before target comparison:

```text
eta > 0, delta > 0, 0 < lambda_max < infinity,
d=(d_0,...,d_4) real, non-scalar; S=sum_j d_j, Q=sum_j d_j^2,
B=5 Q-S^2 > 0,
c_0,...,c_16 complex and fixed,
0 < Omega_min <= Omega_(i,j) < infinity, i=0,...,16, j=1,...,4.
```

`d_j` is an angular-frequency light-shift profile at reference beam powers.
Optical frequencies, polarizations, geometry and the ratio of the two LS
beam intensities are fixed. Their common dimensionless intensity scale is
`lambda`. Fixed-frequency Stark shifts are linear in intensity and the
travelling-wave amplitude scales with the geometric mean of the two beam
intensities [S2]. There are no five independently variable `d_j` controls.

The dimensionless `c_i` include the spatial travelling-wave phase, relative
illumination and relative COM participation at ion `i`; the reference
Lamb-Dicke factor `eta` is outside `c_i`. The common profile assumption
allows different scalar couplings but not arbitrary ion-dependent spectral
profiles. The `c_i` are constrained by one geometry and calibrated jointly;
they are not seventeen independent synthesis knobs. Neither `d` nor `c_i`
is fitted to the native output table.

In the COM interaction frame admit the global force

```text
D_i = diag(d_0,...,d_4) on ion i, identity on all other internal factors,
A_e = lambda_e sum_(i=0)^16 c_i D_i,
H_LS(t) = i hbar eta/2 A_e exp(-i delta t) a^dagger + h.c.
```

This is the linear many-ion extension of the state-dependent force in [S1],
consistent with the multimode form in [S4]. Selecting one COM mode and exact
factorized profiles is an explicit adopted effective model. It is not a
statement that the two-ion experiment already supplies this seventeen-ion
Hamiltonian, mode isolation or calibrated geometry.

Only the six unordered active edges

```text
e={14,k}, k=2,3,4,5,6,7
```

are needed. The `q1:M1` selector copy uses edge `{6,14}` with reversed
control orientation. For each edge define

```text
g_e = Re(c_14 conjugate(c_k)) != 0,
lambda_e = delta / [eta sqrt(50 B abs(g_e))] <= lambda_max.
```

These six inequalities and six nonzero couplings must hold simultaneously
for one independently admissible geometry. No numerical instance with an
uncertainty budget is claimed here. `lambda_e` is an input-independent
scheduled intensity, not selection of a pair by an optical beam. Every LS
pulse illuminates all seventeen ions. Detuning remains fixed during the
whole construction; each completed pulse lasts `tau_LS=2 pi/delta`.

## 3. Closed loops and exact selection by refocusing

For a constant pulse with no intervening carrier operation, Magnus expansion
terminates and gives

```text
U_LS(t) = exp[alpha(t) A_e a^dagger-conjugate(alpha(t)) A_e^dagger a]
          exp[-i K(t) A_e A_e^dagger],
alpha(t) = eta [1-exp(-i delta t)]/(2 i delta),
K(t) = eta^2 [delta t-sin(delta t)]/(4 delta^2).
```

At `tau_LS`, displacement is zero and `K=pi eta^2/(2 delta^2)`.
The exact endpoint is `exp(-i K A_e A_e^dagger) tensor I_motion`.
Its internal phase includes all ion pairs; a pair gate is not a primitive.

Also retain arbitrary finite integrated diagonal local phase profiles
`L_(i,e)(j)` during the LS pulses. Their propagator is
`exp[-i sum_i L_(i,e)]`. They are fixed across the 500 identical pulses of
one refocusing block, may differ between ions, and may differ with the
scheduled intensity `lambda_e`. They are residual phases in the stated
control frame; bare energies tracked by the laboratory-frame factor are
not counted again. Time-varying integrals and carrier errors are excluded
from this exact stationary-phase claim.

For the active pair choose the same projective direction `v` in `F5^3`.
Assign different, nonparallel directions to every other ion. The 31
projective directions suffice for these 17 ions. For each of the 500 pairs
`(a,u) in F5* x F5^3`, conjugate one completed global loop by the individually
compiled monomial permutations

```text
p_i(x)=a x+v_i dot u mod 5.
```

All conjugated endpoints are diagonal and commute. Each label occurs 100
times at each ion. Distinct directions give every ordered label pair 20
times; on the active pair equal labels contribute `100 Q`, while unequal
labels contribute `25(S^2-Q)`. Consequently the 500-loop product is

```text
G_e = gamma_e exp[-i sign(g_e) pi E_e/2] tensor I_other_internal,
E_e = sum_j |jj><jj| on the active pair,
```

with no residual operator on other ions or motion. Here `gamma_e` is a
known scalar; equivalently

```text
C_e = 100 Q sum_i abs(c_i)^2
      +40 S^2 sum_(i<j) Re(c_i conjugate(c_j)) -10 B g_e,
gamma_e = exp[-i K lambda_e^2 C_e -i 100 sum_i Tr L_(i,e)].
```

The equal-versus-unequal coefficient before intensity substitution is
`50 K lambda_e^2 B g_e`. Every stationary local profile sums to
`100 Tr L_(i,e)` and is scalar. Thus arbitrary prior internal correlations
with the spectator ions are covered. Monomial pulse phases cancel in each
conjugation. The actual permutations, inverses and any needed repeated
blocks are finite pulses counted below, not instantaneous extra controls.
This refocusing proof is new work, not an experimental claim of [S1].

## 4. Individually addressed finite carrier primitives

The new control support, relative to the earlier common-rotation model, is
individual 729 nm addressing of every ion [S3]. The ideal primitive is

```text
r_i^(0,j)(theta,phi)=exp[-i theta sigma_i^(0,j)(phi)/2],
sigma^(0,j)(phi)=exp(-i phi)|0><j|+exp(i phi)|j><0|,
duration=abs(theta)/Omega_(i,j), j=1,2,3,4.
```

The four changes of `m_J` are `-1,0,-2,+1`. Each transition has its own
resonant frequency and calibrated nonzero rate. A negative angle is a
positive-duration pulse with phase shifted by `pi`. All simultaneous
control is conservatively scheduled as sequential individual pulses.
The construction uses a finite set of pulse areas and phases specified in
PROOF.md, not an arbitrary one-ion unitary admitted without a pulse word.

These are resolved resonant carrier-RWA Hamiltonians at leading Lamb-Dicke
order. LS fields are off during carriers. Exact individual addressing,
phase tracking, and absence of uncompensated off-resonant spectator terms
are class assumptions. The real addressing and phase-control principle is
documented by [S3]; its reported MS gate is not imported. The alternate
sideband controlled gate and different encoding in [S5] are not imported.

Rotations between two D levels are compiled via the star. For nonzero
`j,k`, with `T_i,j=r_i^(0,j)(pi,0)`,

```text
r_i^(j,k)(theta,phi)
  = T_i,j r_i^(0,k)(theta,phi-pi/2) T_i,j^dagger.
```

Products act rightmost first. All carrier pulses have finite duration and
power. Their crosstalk, spectator Stark shifts and errors are not canceled
merely by the diagonal LS refocusing proof. Such effects require an
explicit compensated primitive or a separate device-error bound.

## 5. Complete one-step word, time and optical resources

The fixed word first copies the actual `q1=s` selector into prepared `M1`,
then uses that physical memory to condition the needed receiver changes.
It comprises 26 derived controlled transpositions on the six edges, with
local updates of `R2.y`, `M2` and `N`. These are derived operations; none is
added to the admitted primitive set. The memory is retained at the output.
PROOF.md specifies the word independently of the 25 input values.

The conservative bounds for the complete native step are

```text
312 refocusing blocks,
156000 completed global LS loops,
at most 19095499 individual elementary star carrier pulses,
sum of absolute carrier pulse areas <= 19095386 pi.
```

Therefore

```text
T_active <= 312000 pi/delta + 19095386 pi/Omega_min.
T_total <= T_active + 19251500 t_switch.
```

The second line assumes an independently bounded switching/settling time
`t_switch` at every primitive boundary, including both ends. The schedule
and resulting endpoint time are common to all inputs. These deliberately
large bounds establish conditional finiteness, not practical performance.

At a fixed declared beam reference plane, let `P_1,P_2` be the LS powers
at `lambda=1`, `n_e` the number of loops at intensity `lambda_e`, and
`P_(i,j)` the carrier power calibrated for `Omega_(i,j)`. Then

```text
sum_e n_e = 156000,
E_incident = (2 pi/delta)(P_1+P_2) sum_e n_e lambda_e
             +sum_carriers abs(theta_r) P_(i_r,j_r)/Omega_(i_r,j_r)
 <= (312000 pi/delta) lambda_max (P_1+P_2)
    +19095386 pi max_(i,j)[P_(i,j)/Omega_(i,j)].
```

Any illumination during switching adds its explicit integral. This is
incident beam energy, not absorbed work, electrical consumption or a
finite quantum battery construction. Classical lasers and controller are
prescribed inputs of the model. They are not claimed to return to their
initial quantum state. No numerical physical error is inferred from the
number of pulses or from a source's fidelity for a much shorter gate.

## 6. Independently defined bare energy account

Assume identical fixed bare spectra up to irrelevant per-ion scalar
offsets, and take the energy of label 0 as zero. Independently calibrate
`E_1,...,E_4` from the physical levels, not from `f(s)`. For example, the
first-order weak-field Zeeman approximation gives

```text
E_j = hbar omega_SD + mu_B B_field (g_D m_j + g_S/2), j=1,...,4,
(m_1,m_2,m_3,m_4)=(-3/2,-1/2,-5/2,+1/2).
```

This illustrative spectral law is an approximation with independent atomic
and field parameters; the exact symbolic account only uses calibrated
energies. Endpoint interactions are off. The supplied input's internal
energy is `E_s+E_1+E_t`, including both source ions and the three prepared
level-0 additional ions. Write `F_s` for the energy of `f(s)`:

```text
F_s = (0, E_4, 2 E_2+2 E_1+E_4,
       E_2+2 E_1+2 E_3+E_4, E_2+2 E_1+2 E_3+E_4).
```

At the output `M1` carries `E_s`, while `M2` and the counter each carry
`E_1`; `R2.y` carries `E_3`. Thus `Delta E_U0(s)=F_s+E_3+2 E_1`:

| s | Change of total internal bare endpoint energy |
| --- | --- |
| 0 | E_3+2 E_1 |
| 1 | E_4+E_3+2 E_1 |
| 2 | 2 E_2+4 E_1+E_4+E_3 |
| 3 | E_2+4 E_1+3 E_3+E_4 |
| 4 | E_2+4 E_1+3 E_3+E_4 |

The input `E_s` cancels against the retained memory contribution, not an
erasure. `S1,S2` cancel because they retain their actual values. The
leading optical-gap counts are `(3,4,8,9,9)`, with Zeeman corrections.
All intermediate internal energies are bounded by the finite seventeen-ion
spectrum; the drive supplies or receives their changes. This bound and
the endpoint table do not demonstrate availability of a finite autonomous
work source at every intermediate pulse or account for initial cooling.

## 7. Inherited motion, physical domain and laboratory phases

The exact effective loop identities hold on the untruncated oscillator.
The input remainder `sigma_(s,t)` may be the actual inherited joint state,
may differ across histories, and may contain correlations among motion,
previous records and other explicitly uncoupled reference factors. There
is no in-step cooling, reset or replacement source. Motion returns to the
identity channel in the COM interaction frame after every full loop.
Free laboratory evolution can supply a known input-independent remainder
unitary instead. This factorization does not include an unconstructed
finite quantum controller or work reservoir.

For any future physical comparison, choose input COM support on Fock
levels `0,...,10` as a validation domain. This is a chosen readiness
condition, not evidence that preparation and the first contact attain it.
No oscillator truncation is imposed during pulses. A uniform excursion
bound for the global force is

```text
b_max <= (eta max_e lambda_e/delta)
         sum_i abs(c_i) max_j abs(d_j).
```

It includes the common, state-independent force component; replacing it by
the earlier two-ion difference bound is invalid. Lamb-Dicke conditions must
cover this excursion, for example
`eta_i (sqrt(10)+sqrt(11)+2 b_max) << 1`, where `eta_i` is the actual
geometric LS Lamb-Dicke parameter at ion `i`, before illumination weights.
Carrier Lamb-Dicke parameters require their corresponding conditions.
These qualitative inequalities supply no
numerical error. Other axial/radial modes are omitted, not shown closed.

All finite pulses are defined in one phase-tracked resonant control frame.
With a common final duration `T`, the physical output also contains the
known free factor `exp(-i H0 T/hbar)`. On each required basis output this
is its actual bare-energy phase, in addition to known scalar pulse phases.
If the clock origin precedes the supplied input, the corresponding known
initial-frame factor is included as well. These phases preserve the frozen
basis readings; they are not silently replaced by one common laboratory
phase. A stronger coherent equality must retain or compensate that profile.

## 8. Exact ideal result and remaining physical obligations

The admitted approximations are harmonic one-COM motion, adiabatic
elimination of optical excited levels, LS and carrier RWA/Lamb-Dicke
Hamiltonians, fixed common force profile, stable calibrated spatial
couplings, resolved individually addressed carriers and the declared
phase tracking. Metastable decay, scattering, heating, mode crowding,
off-resonant excitation, anharmonicity, crosstalk, phase drift and imperfect
closure are excluded from the exact algebra, not set to zero in a device.

A real-device conclusion requires joint calibration satisfying all six
edge inequalities, a demonstrated input preparation and motion domain,
and an error bound for this entire long word including all driven modes,
carrier errors and decay. None is supplied numerically here. A device may
fail those requirements even though the conditional ideal construction is
finite. The claim is restricted to this first native step and its actual
input family, with retained prepared memory. It neither implements the
general native law nor certifies two-contact continuity, long-time archive
protection, the complete preparation/output resource account or derivation
of this apparatus from J. Closed predecessor probes remain unchanged.
