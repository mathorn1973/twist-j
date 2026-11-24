# Physical model and endpoint convention

**NON-CANONICAL, candidate-T conditional ideal-model construction; L1.**
This model retains the physical class of #1369 at
`abbe72037e14d436091294adf006d51bbfca750a`. The new work changes its
forward compilation on the same input sector. It adds no ion, physical
edge, independently adjustable profile component or entangling primitive.
Public Canon v97 and the physical HOLD remain unchanged. Source
provenance and limitations are in [SOURCES.md](SOURCES.md).

## 1. Physical factors, preparation and complete target

There are seventeen `40Ca+` five-level internal factors, one included
harmonic axial COM mode and an explicitly retained uncoupled remainder.
Every ion uses the same inherited Hrmo dictionary:

| Label | Physical level |
| --- | --- |
| 0 | 4^2 S_(1/2), m_J=-1/2 |
| 1 | 3^2 D_(5/2), m_J=-3/2 |
| 2 | 3^2 D_(5/2), m_J=-1/2 |
| 3 | 3^2 D_(5/2), m_J=-5/2 |
| 4 | 3^2 D_(5/2), m_J=+1/2 |

These labels are not an increasing energy order. The fixed factor order is

```text
0:S1, 1:S2,
2:R1.p1, 3:R1.p4, 4:R1.p1p, 5:R1.p4p, 6:R1.q, 7:R1.r,
8:R2.p1, 9:R2.p4, 10:R2.p1p, 11:R2.p4p, 12:R2.y, 13:R2.r,
14:M1, 15:M2, 16:N.
```

The preparation-time dictionary is `R2.y=R2.q+4 mod5`; all other labels
are direct. The supplied post-contact family and required endpoints are

```text
I(s,t): S1=1, S2=t, R1=(0,0,0,0,s,0), R2=(0,0,0,0,0,0),
        M1=0, M2=0, N=0,                       s,t in F5;
O(s,t): S1=1, S2=t, R1=f(s), R2=(0,0,0,0,3,0),
        M1=s, M2=1, N=1.
f(0)=(0,0,0,0,0,0);
f(1)=(0,0,0,0,4,0);
f(2)=(2,1,2,1,4,0);
f(3)=f(4)=(2,1,3,4,3,1).
```

M1, M2 and N are physically counted from preparation, not inserted or
reset at the supplied boundary. Their readiness there is an input
condition that this probe does not prepare. N is a five-level physical
factor, not an unbounded clock. All its levels can be visited by
refocusing, but its endpoint claim is only `0 -> 1`.

The model admits one fixed input-independent sequence and endpoint time.
The raw control-frame coherent contract is
`W|I(s,t)>=Gamma_new|O(s,t)>` with a common scalar. Removing this scalar
gives normalized amplitude +1. Laboratory phases are tracked separately
below. Both M1 values 3 and 4 remain distinct.

## 2. Fixed optical parameters and global force

Independently fix finite parameters

```text
eta>0, delta>0, 0<lambda_max<infinity;
d=(d_0,...,d_4) real and nonscalar;
c_0,...,c_16 complex and fixed;
0<Omega_min<=Omega_(i,j)<infinity, i=0,...,16, j=1,...,4.
```

The d_j are the angular-frequency light-shift profile at fixed reference
beam powers. Optical frequencies, polarizations, geometry and the ratio
of the two LS beam intensities are fixed. Only their common intensity
scale lambda is scheduled. No five independent level-shift controls are
admitted. The c_i include spatial travelling-wave phase, illumination
and COM participation; the reference eta is outside them. They must
come from one jointly calibrated geometry, not seventeen independently
fitted logical-control knobs.

With `D_i=diag(d)` on ion i, the adopted effective force is

```text
A_e=lambda_e sum_i c_i D_i,
H_LS(t)=i hbar eta A_e exp(-i delta t) a^dagger/2+h.c.,
[a,a^dagger]=I.
```

This is the same explicitly adopted many-ion one-COM model as #1369.
Its physical ingredients are sourced, but their joint ideal realization
on seventeen ions is not supplied by a two-ion experiment.

Let `S=sum_j d_j`, `Q=sum_j d_j^2`, `B=5Q-S^2>0`. On the six edges
`e={14,k}`, k=2,...,7, require simultaneously

```text
g_e=Re(c_14 conjugate(c_k)) != 0,
lambda_e=delta/[eta sqrt(50 B abs(g_e))] <= lambda_max.
```

These six scheduled intensities are determined from the independently
specified model parameters. They are independent of s,t. Every loop
illuminates all seventeen ions, at fixed detuning, for `tau=2pi/delta`.
No new pair-selective LS illumination is introduced.

## 3. Completed loops, stationary phases and spectator identity

The exact force propagator in the adopted harmonic frame is

```text
U_LS(t)=exp[alpha(t) A_e a^dagger-conjugate(alpha(t)) A_e^dagger a]
         exp[-i K(t) A_e A_e^dagger],
alpha(t)=eta[1-exp(-i delta t)]/(2i delta),
K(t)=eta^2[delta t-sin(delta t)]/(4 delta^2).
```

A_e is diagonal and normal. The Magnus expansion terminates at its
second term; at tau the displacement vanishes and
`K(tau)=pi eta^2/(2 delta^2)`. The oscillator is not truncated.

As in #1369, retain fixed integrated diagonal residual local profiles
`L_(i,e)(j)` during each LS loop. Their propagator is
`exp[-i sum_i L_(i,e)]`. They are fixed across each 500-loop block and
at each selected intensity. Already tracked bare free phases are not
counted twice. Time-dependent profile drift is excluded from this exact
stationary-profile claim.

PROOF.md specifies the unchanged projective directions, 500 affine
frames, chronological order, monomial compiler and true adjoints. Its
full seventeen-ion identity is

```text
G_e=gamma_e exp[-i sign(g_e) pi E_e/2] tensor I_motion,
E_e=sum_x |xx><xx| on e, identity on other ions,
C_e=100Q sum_i abs(c_i)^2
    +40S^2 sum_(i<j) Re(c_i conjugate(c_j))-10B g_e,
gamma_e=exp[-i K lambda_e^2 C_e-i100 sum_i Tr L_(i,e)].
```

All spectator dependence becomes scalar as a complete operator identity,
not only on basis spectators or after averaging outcomes. Each G still
contains exactly 500 completed loops and 61200 addressed star pi pulses.
No frame fusion or reordered refocusing is part of this probe.

## 4. Individually addressed carriers and finite switching

The allowed carrier is

```text
R_(i;0,j)(theta,phi)
 =exp[-i theta (exp(-i phi)|0><j|+exp(i phi)|j><0|)_i/2],
duration=abs(theta)/Omega_(i,j),                    j=1,2,3,4.
```

These are resolved resonant 729 nm star transitions with changes in
m_J equal to -1,0,-2,+1. Each transition has its own fixed calibrated
nonzero Rabi rate. Negative angles use phase shifted by pi and positive
duration. LS fields are off during carriers, and the serial schedule
needs no simultaneous-pulse capability.

Ideal individual addressing, carrier RWA at leading Lamb-Dicke order,
phase tracking and compensated off-resonant spectator terms are model
assumptions. Their physical principles are documented in the inherited
source set, but their error-free action across this word is not measured.
The paired axis rotations in the exchange are two individual star
pulses. No common two-ion carrier primitive, D-to-D primitive, arbitrary
U(5), abstract controlled rotation or sideband gate is supplied for free.

If switching intervals are included, their actual duration and dynamics
must be specified, with a common bound t_switch for the displayed bound.
They cannot contain unaccounted differential phases or uncontrolled
forces. No intensity change or carrier interrupts an unfinished LS loop.

## 5. Forward word, common phase, time and incident energy

PROGRAM.json freezes four embedded exchanges, the two complement writes,
two singleton controls and seven top-level pair masks, then the original
four-pulse memory phase correction and three fixed preparations. Its
expanded forward count is exactly 64 G blocks, distributed as

```text
edge {14,k}, k=2,3,4,5,6,7: n_G(e)=4,4,16,16,20,4.
Gamma_new=product_e gamma_e^n_G(e).
```

The original normalized target is retained, but the common scalar and
the actual endpoint time are recalculated for this word. PROOF.md gives
the analytical forward bounds

```text
N_LS=32000,
N_carrier<=3917023,
sum_carriers abs(theta)<=3916995 pi,
T_active<=64000 pi/delta+3916995 pi/Omega_min,
T_total<=T_active+3949024 t_switch.
```

The carrier count is an upper bound from the unshortened compiler,
not a measured or precomputed exact new count. No runtime depends on
the logical input. The exact schedule's actual T, rather than its upper
bound, determines the laboratory phases.

At a fixed declared beam reference plane use finite reference LS powers
P_1,P_2 and carrier powers P_(i,j) calibrated for Omega_(i,j). Then

```text
P_LS,e=lambda_e(P_1+P_2),
E_incident=(2pi/delta)*500*sum_e n_G(e) P_LS,e
            +sum_carriers abs(theta_r) P_(i_r,j_r)/Omega_(i_r,j_r)
 <=(64000pi/delta)lambda_max(P_1+P_2)
      +3916995pi max_(i,j)[P_(i,j)/Omega_(i,j)].
```

Illumination during idle or switching intervals adds its explicit
integral. This is incident optical energy, not absorbed work, electrical
consumption or a finite quantum battery trajectory. The prescribed
classical controller and lasers are not claimed to return to their
initial quantum states.

## 6. Bare energy and laboratory phases

Retain identical independently calibrated bare level spectra, up to
irrelevant per-ion scalar offsets, with E_0=0 and finite E_1,...,E_4.
They are physical inputs, not quantities fitted to the native table.
For illustration the inherited weak-field first-order Zeeman model is

```text
E_j=hbar omega_SD+mu_B B_field(g_D m_j+g_S/2),
(m_1,m_2,m_3,m_4)=(-3/2,-1/2,-5/2,+1/2).
```

The endpoint energy proof only uses the calibrated energies. Interactions
are off at endpoints. If F_s is the bare energy of f(s), then

```text
F_s=(0,E_4,2E_2+2E_1+E_4,
     E_2+2E_1+2E_3+E_4,E_2+2E_1+2E_3+E_4),
E_input(s,t)=E_1+E_t+E_s,
E_output(s,t)=E_1+E_t+E_s+F_s+E_3+2E_1,
Delta E(s)=F_s+E_3+2E_1.
```

The source label energy moves from q to M1 and cancels in the difference;
it is not erased. The endpoint energies agree with #1369, although the
intermediate path, time and incident drive energy change. This table
does not construct a finite work source for every intermediate pulse.

Every pulse is defined in a single phase-tracked resonant control frame.
For actual common duration T_new the laboratory output includes
`exp(-i H0 T_new/hbar)`, hence on O(s,t) the phase
`exp[-i E_output(s,t) T_new/hbar]` in addition to Gamma_new. A clock
origin before the supplied boundary also needs its known initial-frame
factor. The coherent comparison to #1369 is between the same normalized
control-frame maps, or between laboratory outputs with these profiles
explicitly retained or compensated. Different durations must not be
treated as the same laboratory phase.

## 7. Remainder inheritance and physical validation domain

The included COM mode may be in its actual inherited state and may be
correlated with the internal inputs, other retained records or a
reference. Each exact loop closes as an operator, and ideal carriers
act trivially on motion. No cooling, reset or new motion source occurs
in this step. A declared free laboratory remainder evolution is
input independent; a finite quantum control/work reservoir is not
silently included in the proven identity remainder.

The inherited prospective physical validation domain is input COM Fock
support 0,...,10, without truncating intermediate motion. It is a
readiness condition, not an established preparation result. With the
fixed global force, an excursion bound is

```text
b_max <=(eta max_e lambda_e/delta)
          sum_i abs(c_i) max_j abs(d_j).
```

This includes the common force component. A compatible Lamb-Dicke
condition must cover that excursion, for example
`eta_i(sqrt(10)+sqrt(11)+2b_max)<<1` for the actual geometric LS
Lamb-Dicke parameter at each ion. Carriers require their own conditions.
These qualitative inequalities supply no numerical error estimate.
Other axial and radial modes are omitted, not demonstrated to close.

## 8. Controls, inverse scope and unresolved device obligations

The omitted-LS negative control retains the entire carrier chronology
and replaces every LS pulse by an equal-duration LS-off wait, including
the absence of its LS-induced residual shifts. In the compensated
control frame the wait is identity; free laboratory evolution is still
tracked. PROOF.md shows algebraically why it reaches zero of the 25
complete target labels.

The formal inverse audit is the algebraic relation `W^dagger W=I`.
It establishes neither a same-duration physically executable inverse
nor new inverse resource counts. A force with negative duration is not
admitted. Only the specified forward word is physically synthesized
and counted at the conditional ideal level.

The ideal approximations are harmonic one-COM motion, effective optical
elimination, LS and carrier RWA/Lamb-Dicke Hamiltonians, fixed common
profile and stable calibrated geometry, exact addressing and declared
phase compensation. Decay, scattering, heating, off-resonant excitation,
mode crowding, anharmonicity, drift, cross-talk and imperfect closure are
excluded from the proof, not set to zero in an actual apparatus.

A physical conclusion still needs joint calibration of the six edge
inequalities, actual input preparation and inherited motion domain,
and a complete error account for this long program and all driven modes.
No source fidelity for a shorter experiment is assigned to this word.
Neither finiteness nor shortening settles the quantum controller/work
account, occupied-memory reuse, archive protection, the later n=9 history
or derivation of this architecture from J. The physical HOLD remains.
