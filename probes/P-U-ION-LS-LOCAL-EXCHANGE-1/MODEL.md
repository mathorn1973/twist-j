# P-U-ION-LS-LOCAL-EXCHANGE-1: frozen effective physical model

NON-CANONICAL. This is a conditional, ideal two-ion reachability model.
It supplies neither a fourteen-ion apparatus nor a physical certificate of
the preparation-to-`n=9` history. Public authority remains Canon v97.
Sources and their limits are identified in [SOURCES.md](SOURCES.md).
The constructive derivation and pulse accounting belong to [PROOF.md](PROOF.md).

## 1. Fixed carriers, dictionary and local targets

The two active factors `S,Q` are `40Ca+` ions with the Hrmo dictionary [S1]:

| Label | Physical level |
| --- | --- |
| 0 | 4^2 S_(1/2), m_J = -1/2 |
| 1 | 3^2 D_(5/2), m_J = -3/2 |
| 2 | 3^2 D_(5/2), m_J = -1/2 |
| 3 | 3^2 D_(5/2), m_J = -5/2 |
| 4 | 3^2 D_(5/2), m_J = +1/2 |

These are physical labels, not increasing energy order. The offset note [S0]
fixes `K` from preparation: only `R2.q` has physical label `q+4 mod 5`.
Its logical decoder is `q=physical_label+1 mod 5`. The other thirteen data
coordinates retain their original labels. No dictionary is changed at a
contact. The whole-history conjugated native law in [S0] is an input to
identifying the local tasks; this probe does not implement that law.

The required families at isolated contact endpoints are

```text
first contact:  S=S1, Q=R1.q, |s,1> -> |1,s>, s in F5;
second contact: S=S2, Q=R2.q, |s,4> -> |4,s>, s in F5.
```

For each contact the control word and its timing are the same for every `s`.
The choice `c=1` or `c=4` identifies a contact in the fixed schedule; it is
not feedback from a source label. Success means the two required physical
level readings, with no leakage, postselection or discarded failed reading.
Known phases on the five basis inputs are allowed and must be declared.
The construction gives a common phase on the required family in its stated
rotating frame. It does not claim a coherent laboratory-frame SWAP on all
twenty-five pair states.

The complete history still has fourteen data factors, motion, controls,
history memory and work sources. Their actual states at the second contact
are not certified here. In particular, the four distinguishable remainders
required by the original fourfold history collision are not erased.

## 2. Independently fixed parameters and allowed LS control

Before comparing with either target, fix finite parameters

```text
eta > 0, delta_* > 0, phi_Q-phi_S = pi,
d=(d_0,...,d_4) real and non-scalar,
B = 5 sum_j d_j^2 - (sum_j d_j)^2 > 0,
0 < lambda_max < infinity.
```

The profile `d` is the same at both ions. Optical frequencies, polarizations,
beam geometry and the ratio of the two beam intensities are fixed. A single
nonnegative scale `lambda` multiplies both intensities, giving
`Delta_(S,j)=Delta_(Q,j)=lambda d_j`. There are no five independent shift
controls. The coefficients are independent atomic/calibration inputs, not
values fitted to a carry table. Fixed-frequency Stark shifts are linear in
intensity, while their travelling-wave amplitude is proportional to the
geometric mean of the two beam intensities [S2].

In the COM interaction frame the admitted force is Hrmo Eq. (1) [S1]:

```text
H_LS(t) = i hbar eta/2
          [exp(i phi_S) D_S + exp(i phi_Q) D_Q]
          exp(-i delta_* t) a^dagger + h.c.,
D=diag(lambda d_j), D_S=D tensor I, D_Q=I tensor D.
```

Each force pulse has constant parameters and lasts exactly
`tau_LS=2 pi/delta_*`. No data rotation occurs inside an unfinished loop.
The same phase origin and effective pulse integral are used at each loop.
The half-period spatial phase is supported by the source configuration [S1].
Equal illumination and equal COM participation are exact class premises.

Set

```text
lambda_* = delta_*/(eta sqrt(2 B)).
```

The admitted parameter class requires `lambda_* <= lambda_max`. This is an
explicit admissibility inequality, not a measured intensity bound supplied
by the paper. Detuning is not retuned during synthesis: this avoids silently
changing the calibrated atomic profile with the optical frequencies.
Non-scalar `d` is sufficient; equal shifts of the four D levels are not used.

## 3. Closed propagator and stationary local phases

With `A=exp(i phi_S)D_S+exp(i phi_Q)D_Q`, the exact effective propagator is

```text
U_LS(t) = exp(alpha(t) A a^dagger - conjugate(alpha(t)) A^dagger a)
          exp(-i K(t) A A^dagger),
alpha(t) = eta [1-exp(-i delta_* t)]/(2 i delta_*),
K(t) = eta^2 [delta_* t-sin(delta_* t)]/(4 delta_*^2).
```

At `tau_LS`, displacement vanishes and `K=pi eta^2/(2 delta_*^2)`.
The data operation is `exp(-i K A A^dagger)` and the motion operation is
`I_motion` in this frame. This is an operator identity, not a claim based
only on equal mean energies or a fresh ground-state preparation.

Additionally admit any finite, stationary, diagonal one-ion terms during
every identical LS pulse. These are residual terms in the declared control
frame: bare H0 energies already included in the laboratory-frame factor
below are not counted again. Their integrated phase profiles `L_S,L_Q` are
fixed across all twenty members of an echo and can differ between ports.
They commute with the force. Both their conjugated sums are scalar because
each physical label occurs four times at each position of the affine echo.
This covers retained residual detuning or static Stark phases during these loops.
It does not cancel changing pulse integrals, arbitrary time-dependent drift,
or errors during a carrier rotation. Bare carrier transition frequencies
must still satisfy the common-resonance condition in the next section.

For `p(j)=a j+b mod 5`, `a in F5*`, `b in F5`, conjugate a completed loop
by the same monomial permutation on both ions. All twenty resulting loop
endpoints are diagonal and commute. Their product is, up to a scalar,

```text
Q(theta)=exp(-i theta E), E=sum_j |jj><jj|,
theta=2 K cos(phi_S-phi_Q) lambda_*^2 B = -pi/2.
```

Without the additional residual diagonal terms, the raw twenty-loop gate
is `G=(-i) Q(-pi/2)`: its equal-label entries are 1 and its unequal-label
entries are -i. PROOF.md and both verifiers retain this raw global phase.

The permutations are compiled into the finite carrier pulses below;
they are not extra instantaneous operations. Monomial phases do not change
the conjugation of a diagonal profile. The affine echo is a derivation of
this probe, not an operation claimed to have been tested in [S1].

## 4. Finite elementary 729 nm carrier rotations

The elementary controls are common resonant star rotations only [S1]:

```text
R^(0,j)(vartheta,phi) = r^(0,j)(vartheta,phi) tensor r^(0,j)(vartheta,phi),
r^(0,j) = exp[-i vartheta sigma^(0,j)(phi)/2],
sigma^(0,j)(phi) = exp(-i phi)|0><j| + exp(i phi)|j><0|,
j=1,2,3,4.
```

Use calibrated `0 < Omega_min <= Omega_j < infinity`, constant during a
rectangular pulse, with duration `abs(vartheta)/Omega_j`. Negative angles
are implemented by shifting the optical phase by `pi`. The construction
uses phases in integer multiples of `pi/2` and finitely many pulse areas.
Each transition has its own resonant optical frequency and calibration;
their Rabi frequencies are not assumed equal. The four changes of `m_J`
are respectively `-1,0,-2,+1`.

In this exact effective model, bare port spectra have the same transition
frequencies up to additive scalar offsets. Optical phases and frequencies
are tracked in a common, fixed resonant rotating frame. LS fields are off
during carrier pulses. The carrier Hamiltonian is the resolved resonant
carrier RWA at leading Lamb-Dicke order, with no motional operator or
uncompensated spectator term. Its finite-time propagator is exactly the
rotation above in this model; it is not an impulsive-limit assumption.

No direct D-D transition or arbitrary `U(5)` is admitted for free. For
`j,k != 0`, define `T_j=R^(0,j)(pi,0)`. The explicit three-pulse identity

```text
R^(j,k)(vartheta,phi)
  = T_j R^(0,k)(vartheta,phi-pi/2) T_j^dagger
```

implements the needed common two-level rotation in time
`2 pi/Omega_j + abs(vartheta)/Omega_k`. Products act rightmost first.
Collective permutations, their inverses and phase corrections are likewise
compiled from these star pulses; see the exact word and count in PROOF.md.

## 5. Finite time and incident optical energy

For one contact, the declared construction uses `240` closed LS loops and
at most `2923` common elementary star pulses. The sum of absolute star pulse
areas is at most `2918 pi`. Hence the active illumination time obeys

```text
T_active <= 480 pi/delta_* + 2918 pi/Omega_min.
```

These are conservative constructive bounds, not optimality claims or the
duration of the experimentally measured Hrmo gate. With a separately
calibrated finite maximum switching/settling interval `t_switch`, allow one
interval at each primitive boundary, including the two ends: at most `3164`
intervals. Then `T_total <= T_active + 3164 t_switch`. This overhead is an
additional apparatus input; it is not inferred from ideal rotations.

Define optical power at one fixed, declared reference plane. Let `P_1,P_2`
be the two LS powers at reference scale `lambda=1`, and `P_(729,j)` the
calibrated power used for carrier Rabi rate `Omega_j`. With fields off
outside their pulse intervals, incident pulse energy is

```text
E_incident = (480 pi/delta_*) lambda_* (P_1+P_2)
             + sum_r abs(vartheta_r) P_(729,j_r)/Omega_(j_r)
          <= (480 pi/delta_*) lambda_* (P_1+P_2)
             + 2918 pi max_j [P_(729,j)/Omega_j].
```

Nonzero illumination during switching adds its measured integral explicitly.
This is beam energy crossing the reference plane, not absorbed work, wall
power, a finite quantum battery construction, or total apparatus energy.
The control fields remain classical in the exact model. With identical
disconnected port spectra up to additive constants, each required exchange
has zero change of their combined bare endpoint energy. This does not make
the pulses free or remove preparation and native-evolution energy costs.

## 6. Inherited remainder, motion domain and frame convention

Each actual-history local input is `|s,c><s,c| tensor sigma_h`, where
`sigma_h` is the actual inherited joint remainder, including motion and
history memory. It need not be common between histories or internally
uncorrelated. No cooling, reset, replacement battery or common fresh
ancilla is inserted. The exact effective algebra factors each complete
word from this remainder; laboratory free motion may contribute a known
input-independent `W_rem` instead of interaction-frame identity.

Here the quantum remainder comprises the COM mode and uncoupled
spectator/history/reference factors with their declared free evolution.
The lasers and controller are prescribed classical inputs in this local
model; the factorization does not prove a return channel for finite quantum
work or control sources. Their complete inherited states and output
account remain part of the unprovided full apparatus contract.

For prospective physical error statements, freeze the input motion domain
to support on COM Fock levels `0,...,10`, with arbitrary correlations inside
the remainder. This is a chosen validation domain, not evidence that the
actual `n=6` preparation meets it. The algebraic identity does not require
this cutoff, and the driven oscillator is not truncated at level 10.
During a loop the maximum displacement obeys

```text
b_max = eta lambda_* max_(j,k)|d_j-d_k|/delta_*
      = max_(j,k)|d_j-d_k|/sqrt(2 B).
```

Lamb-Dicke validity must cover the excursion as well as the input, e.g.
`eta (sqrt(10)+sqrt(11)+2 b_max) << 1`; carrier Lamb-Dicke parameters require
their corresponding condition. This qualitative regime condition is not
an assigned numerical error bound. Off-resonant spectator modes are absent
from the exact single-COM model, not proved closed in a real apparatus.

If `E_j` are the static common bare energies, a rotating-frame output
`exp(i chi_c)|c,s>` gives laboratory phase
`exp[i chi_c-i(E_c+E_s)T_total/hbar]`, apart from scalar port offsets.
These known per-input phases do not affect the required basis readings.
They are not silently identified with one common laboratory phase. More
general retained known diagonal frame phases must be declared the same way.

## 7. Exact premises and unearned physical conclusions

The exact class adopts harmonic COM motion, adiabatic electronic elimination,
the LS Lamb-Dicke/RWA Hamiltonian, equal illumination, fixed phase and shift
profiles, calibrated finite carrier controls, and the common rotating-frame
description. Scattering, metastable decay, heating, anharmonicity, imperfect
closure, differential carrier response, off-resonant excitation and control
noise are excluded from that algebra, not assigned zero in experiment.

A device claim requires independently measured parameter bounds, validation
of the inherited motion domain and a uniform error bound for the whole word.
No such numerical error is assigned here. The source's short-gate fidelity
cannot be reused as the error of 240 LS loops and thousands of rotations.
This probe does not establish addressability and archive protection in a
fourteen-ion chain, the conjugated native evolution, a finite complete work
source, the full two-contact history, or a derivation of quantum mechanics
or this architecture from J. The earlier isolated same-dictionary C4
obstruction remains valid in its own fixed scope.
