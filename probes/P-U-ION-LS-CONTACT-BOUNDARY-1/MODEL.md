# P-U-ION-LS-CONTACT-BOUNDARY-1: frozen physical model boundary

NON-CANONICAL. This document defines `C_closed_Ca5`, an idealized,
favourable control class derived from a specified effective ion Hamiltonian.
It is a candidate model for the isolated second contact. Its mathematical
boundary is not a certificate of a complete physical apparatus, of the
fourteen-ion history, or of the physical input contract discussed in #1359.
Public authority remains Canon v97. Source provenance is in [SOURCES.md](SOURCES.md);
the analytical argument is in [PROOF.md](PROOF.md).

## 1. One fixed coordinate-to-level dictionary

Every data coordinate is encoded in a separate five-level `40Ca+` ion using
the same map `iota(x)=|ell_x>`, fixed from initial preparation onwards:

| Coordinate value x | Physical level ell_x |
| --- | --- |
| 0 | 4^2 S_(1/2), m_J = -1/2 |
| 1 | 3^2 D_(5/2), m_J = -3/2 |
| 2 | 3^2 D_(5/2), m_J = -1/2 |
| 3 | 3^2 D_(5/2), m_J = -5/2 |
| 4 | 3^2 D_(5/2), m_J = +1/2 |

These labels were read directly from Hrmo et al., Fig. 1 [S1]. In particular,
the label order is not increasing energy order. No old `(h,e)` encoding or
exception for `h=0` is used.

The proposed complete data register has the ordered coordinates

```text
S1, S2,
R1.p1, R1.p4, R1.p1p, R1.p4p, R1.q, R1.r,
R2.p1, R2.p4, R2.p1p, R2.p4p, R2.q, R2.r.
```

This is fourteen data ions before adding control, motion, history memory,
work sources or buffer ions. It is an architecture declaration, not an
experimental claim. Each coordinate retains its physical factor and its
dictionary throughout the proposed horizon. There is no relabeling of the
ports after contact and no decoder that consults the original input labels.

The inherited logical input is [S0]: `s_i=a_i+1 mod 5`, both receiver states
`rho=(0,0,0,0,1,0)`, and all 25 pairs `a1,a2 in F5`. At boundary `n=6`, the
second receiver is `(2,1,3,4,0,4)` and its unused source is still `a2+1`.
Thus the active physical factors at the second contact are `S=S2` and
`Q=R2.q`, with the actual family `(s,q)=(a2+1,0)`. In particular `s=0`
comes from `a2=4`; it is not an invented test preparation.

The complete preparation-to-`n=9` problem retains both receivers and sources
at every boundary. It does not reset a receiver, source, clock, motion or
other resource at `n=6`. This probe uses that problem to identify the
required local input. It does not physically implement its intermediate
native steps, assign SI times to all ten boundaries, or certify the
resulting inherited resource states.

## 2. Precisely isolated endpoint target

With `P=(p1,p4,p1p,p4p)`, `kappa=sum(P)=0` and `r=4`, the existing contact is

```text
C4(s,q) = (q+4, s+1) mod 5,
C4(s,0) = (4, s+1) mod 5.
```

Its coherent permutation representative is
`T_C4=(X^4 tensor X) SWAP`, where `X|j>=|j+1 mod 5>`.
Success in this probe means the required pair of fixed level labels is
obtained at a completed, isolated contact endpoint. For every original
history h=(a1,a2), with s=a2+1 mod 5, define

```text
p_h = Pr[(S,Q)=(4,s+1) | actual full inherited input for history h],
epsilon_write_worst = max_h (1-p_h).
```

Every wrong output or departure from the two five-level code spaces counts
as failure. There is no postselection, conditional renormalization, ignored
readout event or input-dependent choice of successful branch. The model
uses ideal level projectors and the ordinary quantum probability rule as
external physical premises, not as consequences of J.

The larger history contract also permits a combined contact/native step
without an isolated contact boundary. Such a combined endpoint is outside
this target. Excluding the isolated `C4` task does not exclude that route.

## 3. Effective Hamiltonian and conditions adopted here

Hrmo et al. [S1, Eq. (1)] supply the two-ion light-shift Hamiltonian in the
COM interaction frame,

```text
H_LS(t) = i hbar eta/2 sum_(N,j)
          Delta_(N,j) |j_N><j_N| exp(-i delta t) exp(i phi_N) a^dagger
          + h.c.
```

The source derives this effective description using adiabatic elimination,
the Lamb-Dicke approximation and a rotating-wave approximation. It treats
one near-resonant COM mode. Its resonant rotations and light-shift fields
use 729 nm and approximately 401 nm light, respectively. The reported
system contains two ions, not fourteen. [S1]

For this probe, additionally freeze the following conditions. These are
restrictions of the candidate, not assertions about every ion apparatus:

1. During each LS pulse, `Delta_(S,j)=Delta_(Q,j)=Delta_j` are finite, real
   and constant. The COM Lamb-Dicke parameter `eta` is the same at both
   ports. Define `D=diag(Delta_0,...,Delta_4)`, `D_S=D tensor I` and
   `D_Q=I tensor D`. This equality of light-shift profiles is an explicit
   model input; the source's general notation allows ion dependence.
2. The detuning `delta` is finite and positive and the pulse lasts exactly
   `tau=2 pi/delta`. Spatial phases `phi_S,phi_Q` are arbitrary, constant
   and need not coincide. No other data operation is interleaved inside
   an unfinished LS excursion.
3. The harmonic mode and classical control description are ideal. Leakage,
   scattering, finite-level decay, heating, anharmonicity, unclosed
   spectator modes and calibration error are absent in the exact class.
   They are not assigned zero error in a real apparatus.
4. Bare energies, including any retained diagonal drift, satisfy
   `E_(S,j)(t)=E_j(t)+c_S(t)` and `E_(Q,j)(t)=E_j(t)+c_Q(t)`. Hence a port
   difference is only an additive scalar. Any rotating-frame correction
   must preserve this common action. An uncompensated state-dependent
   differential drift is outside the class; it cannot be silently omitted.
5. Between completed LS pulses, allow common finite rotations `R tensor R`
   with the same level-pair, angle and phase on the two ports. Eq. (5) of
   [S1] supplies this form. For the negative argument we may enlarge it
   to every `R in U(5)`; that favourable superset is not a claim of
   implementing arbitrary R within a measured time or energy budget.

The complete word has finitely many completed pulses and common rotations,
with an input-independent order and control schedule. There is no
individually addressed operation, port-conditioned feedback, transported
asymmetric reference, measurement feed-forward, or direct data coupling to
another register in this class. These exclusions specify the class being
tested; they are not prohibitions on future designs.

## 4. Closed motion is derived, not inferred from endpoint energy

Write

```text
A = exp(i phi_S) D_S + exp(i phi_Q) D_Q,
alpha(t) = eta (1-exp(-i delta t))/(2 i delta),
K(t) = eta^2 (delta t-sin(delta t))/(4 delta^2).
```

Because A is normal and all its data projectors commute, the Magnus
expansion terminates after its second term. The effective propagator is

```text
U_LS(t) = exp(alpha A a^dagger - conjugate(alpha) A^dagger a)
          exp(-i K A A^dagger).
```

At the prescribed endpoint `alpha(tau)=0`. In this interaction frame,

```text
U_LS(tau) = exp(-i K(tau) A A^dagger) tensor I_motion,
A A^dagger = D_S^2 + D_Q^2
            + 2 cos(phi_S-phi_Q) D_S D_Q.
```

The last expression is invariant under exchanging S and Q. Consequently
the closed data propagator commutes with `P_swap`, independently of the
spatial phase difference. Common diagonal drift and every admitted common
rotation have the same endpoint symmetry. This conclusion retains all
five `Delta_j`; neglecting differences among the D-level shifts is not
needed for it.

The source's generalized echo construction and diagonal `G(theta)`
([S1], Eqs. (2)-(3), (5)-(6)) are a motivating special case. Its additional
large S-versus-D light-shift approximation simplifies the phase pattern;
the present obstruction is derived from the Hamiltonian above rather than
assuming that a desired two-port gate is available.

There is deliberately no claim that `[H_LS(t),P_swap]=0` at intermediate
times. For example, at `phi_Q=phi_S+pi`, the force is proportional to
`D_S-D_Q`, which changes sign under port exchange. A closed propagator may
have the stated symmetry although its instantaneous generator does not.
Using a joint port-swap/motional-parity symmetry before closure would
require additional assumptions on the inherited motion; this proof does
not use that route.

## 5. Inherited remainder and exact domain

Let the counted remainder contain motion, the other twelve data ions,
the finite-horizon clock, history distinctions, control and work systems.
At every completed control-block endpoint the admitted mathematical
action factors as

```text
V_block = V_SQ tensor W_remainder,
[V_SQ,P_swap]=0.
```

The remainder may evolve, consume resources, and retain information. It is
not required to return to a ready state. Its incoming state may depend on
the actual preceding history and may contain arbitrary internal
correlations. In the LS block, motion may correlate with active data during
the excursion; the displayed factorization holds at its completed endpoint.
An exact encoded input `|s,0><s,0|` is a pure active marginal, so any full
state with that marginal necessarily factors from the remainder initially.
No common fresh remainder at the second contact is assumed.

The oscillator identity is exact throughout the harmonic effective model,
not merely on the oscillator vacuum. Applying this ideal model to physical
inherited motion additionally requires an allowed input-energy/excitation
domain on which all intermediate excursions satisfy its approximations.
No measured domain, all-mode error bound or quantitative finite battery is
supplied here. Allowing an arbitrary counted remainder and generous common
control is favourable to realization and sufficient for this negative
class boundary; it is not a constructive resource account.

The proof gives `p_h<=1/2` for every h with a2=4, hence
`epsilon_write_worst>=1/2`, for every
member of `C_closed_Ca5`. It is independent of pulse count, common control
choice and inherited remainder state within that class. It neither proves
that the bound is attained by this class nor excludes asymmetric controls.

## 6. Conditional approximate extension

Distinguish physical detuning `delta` from an approximation tolerance
`delta_out in [0,1]`. Suppose an independently justified physical output
`rho_phys` for the witness input, with its actual inherited remainder,
obeys

```text
(1/2) ||rho_phys-rho_ideal||_1 <= delta_out
```

for some output of the exact frozen class. Both states are compared on a
common output space including a failure/leakage outcome; the same fixed
success projector is used. Then

```text
p_h(physical) <= min(1, 1/2+delta_out),  for h with a2=4,
epsilon_write_worst(physical) >= max(0, 1/2-delta_out).
```

This is a conditional continuity statement, not an assigned apparatus
error. No numerical `delta_out` is earned by the exact verifier. A uniform
extension over histories requires the bound on each corresponding actual
input/remainder, not a bound measured only on newly cooled motion.
For nonzero residual displacement, a small unrestricted operator-norm
distance on the entire oscillator cannot be inferred from small amplitude;
an explicit restricted domain or energy-constrained state/channel bound is
needed. Multimode closure and residual local phases must be checked rather
than imported from the single-mode period [S3].

## 7. Independent endpoint energies

For fixed bare port spectra the required isolated endpoint energy change is

```text
w_s = E_S(4)+E_Q(s+1 mod 5)-E_S(s)-E_Q(0).
```

Under the identical-spectrum condition, subtract the common zero level to
write `E(0)=0`. The symbolic table is

| s | w_s |
| --- | --- |
| 0 | E(4)+E(1) |
| 1 | E(4)+E(2)-E(1) |
| 2 | E(4)+E(3)-E(2) |
| 3 | 2E(4)-E(3) |
| 4 | 0 |

The zero for `s=4` also holds for different port spectra because `(4,0)`
is a fixed point. For the stated S/D dictionary, an independently supplied
first-order Zeeman approximation would take

```text
E(j) = E_SD + mu_B B (g_D m_j + g_S/2), j=1,...,4,
(m_1,m_2,m_3,m_4)=(-3/2,-1/2,-5/2,+1/2).
```

Here `E_SD`, B and both g factors are physical inputs, not fitted from
contact or carry outputs. No numerical spectroscopy is supplied or tested
by this probe. At leading optical order the table is proportional to
`(2,1,1,1,0)`, not to four identical energy increments.

These are changes of the two encoded bare-state energies at disconnected
endpoints. They are neither laser/electronics consumption nor an account
of switching, intermediate work availability or inherited battery charge.
Other coordinates cancel only if their actual endpoint contributions agree.

## 8. Meaning of the boundary

The tested class admits physical ingredients independently described by
ion experiments but takes their ideal effective equations as premises.
Its negative result rules out the isolated directional endpoint with
worst-case write error below one half in precisely this class. It does not
show that all controls available in the experimental platform belong to
the class, prove physical completeness of the class, or rule out a
different code, addressed control, asymmetric resource or combined step.

In particular, no Hamiltonian for fourteen simultaneously controlled ions,
all-mode closure, finite source renewal, physical archive protection or
complete evolution from preparation to boundary nine is certified.
Spectroscopic hiding and buffer results from other encodings [S4] do not
automatically apply here. No H/O owner, Canon claim or #1359 HOLD is closed
by adopting this model. The theory of the selected physical carrier and
its quantum probability rule remain imported physics, not derived from J.
