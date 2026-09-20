# Exact conditional writer from carrier and blue-sideband pulses

**PUBLIC; candidate-T, L1; NON-CANONICAL.** This is a theorem about an
explicit ideal driven-ion Hamiltonian and a specified input subspace. It is
not an assertion of exact laboratory performance, a Hamiltonian derived from
native `U`, or physical closure of `QDD-INSTRUMENT-APPARATUS`.

## 1. Registers, phase convention, and physical assumptions

Use source `S`, port `P`, and archive `A`. Each has five logical levels
`|0>,...,|4>` and a distinct auxiliary level `|g>`. The logical levels are
encoded in five `D_(5/2)` Zeeman states of a calcium-40 ion; `g` is in
`S_(1/2)`. One possible assignment is

\[
|k\rangle=|D_{5/2},m=-5/2+k\rangle\quad(0\leq k\leq4),
\qquad |g\rangle=|S_{1/2},m=-1/2\rangle.
\]

This assignment is a proposed engineering dictionary. Its five optical
transitions have changes of magnetic quantum number `-2,-1,0,1,2` and are
allowed quadrupole transitions. It is not a claim that the exact apparatus
specified here has been calibrated or built.

Source hardware levels `0,1,2,3` represent native labels `h=1,2,3,4`.
Hardware level `0` is LOW. Hardware levels `1,2,3` span HIGH. Hardware level
`4` is outside the source code and is not identified with native `h=0`.
The mathematical extension below assigns response `2` to this extra level;
it does not reproduce the older global convention `f(0)=0`.

Let `b` be the annihilation operator of one common motional mode, with
number states `|n>_b`. This operator is not a native generator named `b`.
The input motion is `|0>_b`; every auxiliary `g` is initially empty. The
archive is arbitrary and is untouched by the writer. Thus the intended
joint logical code has dimension `4*5*5=100`.

We define our own explicitly Hermitian phase convention. On ion `I`, a
carrier pulse addressing logical level `k` has interaction-picture
Hamiltonian

\[
H^c_{I,k}(t)=\frac{\hbar\Omega^c_{I,k}(t)}2
\left(e^{i\phi}|k\rangle\langle g|
+e^{-i\phi}|g\rangle\langle k|\right).
\tag{1}
\]

The first blue sideband has Hamiltonian

\[
H^b_{I,k}(t)=\frac{\hbar\Omega^b_{I,k}(t)}2
\left(e^{i\phi}b^\dagger|k\rangle\langle g|
+e^{-i\phi}b|g\rangle\langle k|\right).
\tag{2}
\]

Here `Omega^b` is the calibrated sideband Rabi frequency including the
Lamb-Dicke factor, not the carrier Rabi frequency. Write `R_(I,k)(theta,phi)`
and `B_(I,k)(theta,phi)` for the resulting propagators with respective
pulse areas `theta=integral Omega(t) dt`. The carrier optical frequency is
`omega_(kg)`; the blue-sideband frequency is `omega_(kg)+nu`, where `nu`
is the angular frequency of the selected mode. The laser phase absorbs the
fixed phase introduced in the Lamb-Dicke expansion.

Equations (1)-(2) are effective Hamiltonians after the optical rotating-wave
approximation, resolved-sideband selection and the Lamb-Dicke
approximation. They also presume individually addressed ions, zero residual
detuning and compensation of deterministic optical and spectator-level
phases. Their physical origin is the laser coupling of internal ion levels
to the normal modes of the Coulomb-coupled trapped ions. They do not posit
an elementary `N_i N_j` interaction.

Residual light shifts, other modes, heating, spontaneous decay, imperfect
pulse areas and cross-talk are experimental errors outside this exact
ideal statement. In particular, phase compensation must be calibrated for
all logical states; reproducing output populations alone is insufficient.

The experimentally demonstrated construction used as the physical precedent
is the auxiliary-ground-state, blue-sideband controlled rotation of Meth
et al., Appendix A, Figure 4. Its general form has two control sideband
pulses and three target sideband pulses. Appendix G.2 discusses cancellation
between successive operations sharing the same control. The present
composition and all phase identities below are derived here using (1)-(2),
not imported as a measured result. See
[Meth et al., *Simulating 2D lattice gauge theories on a qudit quantum
computer*, arXiv:2310.12110v2](https://arxiv.org/html/2310.12110v2).

## 2. Exact pulse actions

For a carrier pulse with area `theta`, put `c=cos(theta/2)` and
`s=sin(theta/2)`. Then

\[
R_k(\theta,\phi)|g\rangle
=c|g\rangle-i e^{i\phi}s|k\rangle,
\qquad
R_k(\theta,\phi)|k\rangle
=c|k\rangle-i e^{-i\phi}s|g\rangle.
\tag{3}
\]

Other logical levels are fixed. Carrier pulses do not change the motion.
The blue pulse acts on each two-dimensional subspace
`span{|g,n>,|k,n+1>}` by the same formula with angle
`theta*sqrt(n+1)`:

\[
B_k(\theta,\phi)|g,n\rangle
=c_n|g,n\rangle-i e^{i\phi}s_n|k,n+1\rangle,
\]
\[
B_k(\theta,\phi)|k,n+1\rangle
=c_n|k,n+1\rangle-i e^{-i\phi}s_n|g,n\rangle,
\tag{4}
\]

where `c_n=cos(theta*sqrt(n+1)/2)` and
`s_n=sin(theta*sqrt(n+1)/2)`. The state `|k,0>` is dark, as are all
other logical levels on that ion. We have not replaced the oscillator by
a two-state system or discarded the `sqrt(2)` coupling. Section 6 proves
that no addressed pulse encounters its `n=1` ground-state partner.

Operators in a product act from right to left. Every unspecified phase
below is zero. A negative area `-pi` means a positive-duration `pi` pulse
whose phase is increased by `pi`; it never means negative elapsed time.

## 3. Three-pulse signed exchange and the exact five-cycle

For distinct logical levels `u,v` define the carrier sequence

\[
Q_{u,v}=R_v(\pi,0)R_u(\pi,0)R_v(-\pi,0).
\tag{5}
\]

Substitution into (3), with no suppressed phase, gives

\[
Q_{u,v}|u\rangle=-|v\rangle,\qquad
Q_{u,v}|v\rangle=|u\rangle,\qquad
Q_{u,v}|g\rangle=|g\rangle.
\tag{6}
\]

All other logical levels are fixed. The corresponding blue-sideband
sequence is

\[
M_{u,v}=B_v(\pi,0)B_u(\pi,0)B_v(-\pi,0).
\tag{7}
\]

For logical inputs and motion zero it is the identity. For motion one,

\[
M_{u,v}|u,1\rangle=-|v,1\rangle,\qquad
M_{u,v}|v,1\rangle=|u,1\rangle;
\tag{8}
\]

the other logical inputs with motion one are fixed, and auxiliary `g` is
empty again at the end. For example, the state `|v,1>` follows
`|v,1> -> i|g,0> -> |u,1> -> |u,1>`, whereas `|u,1>` follows
`|u,1> -> |u,1> -> -i|g,0> -> -|v,1>`.

Let `X|j>=|j+1 mod 5>` and write `M_j=M_(j,j+1)`. Apply the four
`M_j` in chronological order `j=0,1,2,3`. On motion one their product is

\[
M_3M_2M_1M_0=X^{-1}\otimes I_b.
\tag{9}
\]

Indeed, input `0` traverses all four exchanges and reaches `4` with phase
`(-1)^4=1`. Each input `j=1,2,3,4` is fixed until the `(j-1,j)` exchange,
then maps to `j-1` with phase `+1`, after which no subsequent exchange
addresses it. Every one of the five output phases is exactly `+1`.
On motion zero the product is the identity.

Individual `M_j` are signed exchanges, not phase-free transpositions.
Equation (9) explains why their signs cancel in the required cycle; no
unmentioned correction to a controlled global phase is permitted.

## 4. Conditional inverse shift with fourteen blue pulses

Choose source control level `c=0` and define

\[
V=B_{S,0}(\pi,0)R_{S,0}(\pi,0),
\qquad
G=V^\dagger M_3M_2M_1M_0V,
\tag{10}
\]

where every `M_j` acts on port `P` and the common mode. Equation (3)
followed by (4) gives

\[
V|0\rangle_S|0\rangle_b=-|0\rangle_S|1\rangle_b,
\qquad
V|s\rangle_S|0\rangle_b=|s\rangle_S|0\rangle_b
\quad(s\ne0).
\tag{11}
\]

The port is arbitrary. All source logical levels are again in `D` after
`V`. By (9), the middle twelve blue pulses apply `X^{-1}` precisely on
the control branch. The inverse `V^dagger` contributes the second minus
sign on that branch and restores the common motional vacuum. Thus, on all
25 source-port logical basis inputs,

\[
G\bigl(|s\rangle_S|p\rangle_P|0\rangle_b\bigr)
=|s\rangle_S|p-\mathbf1_{s=0}\rangle_P|0\rangle_b.
\tag{12}
\]

There is no branch-dependent residual phase, no final auxiliary population,
and no residual correlation with motion. Linear extension proves the same
identity on arbitrary coherent inputs and on inputs entangled with the
untouched archive or an external reference.

The pulse count is two source carrier pulses, two source blue pulses and
twelve target blue pulses: `2 carrier + 14 blue`. This is a construction,
not a minimum-pulse theorem. It can also be obtained from four separate
five-blue-pulse controlled rotations by cancelling the adjacent `V V^dagger`
exactly; the mode need not be uncomputed between the four rotations.

The argument is unchanged for any selected control level `c` in
`{0,1,2,3,4}`: replace the two source pulse labels `0` in `V` by `c`.
It is also unchanged when the control and target are any two distinct
individually addressed ions. Thus the same construction supplies `G_c`
on the full logical space of each such pair, with the same pulse counts.
Its inverse reverses the pulse order and negates every pulse area, and
supplies the controlled shift `X` with the same counts and a common final
motional vacuum. These extensions justify using the primitive to compile
port-archive operations as well as the writer.

## 5. Local offset and complete writer

Use (5) for the four port level pairs, in chronological order,

\[
(0,3),\quad(3,1),\quad(1,4),\quad(4,2).
\tag{13}
\]

Their product is

\[
L=Q_{4,2}Q_{1,4}Q_{3,1}Q_{0,3}=X^2.
\tag{14}
\]

The proof is the same signed-cycle calculation as in (9), now in ordered
labels `(0,3,1,4,2)`: `0` traverses four negative exchanges to `2`; the
remaining inputs map `3->0`, `1->3`, `4->1`, `2->4` with positive phase.
This uses exactly twelve carrier pulses, returns the port auxiliary empty,
and never affects motion.

The writer is `W=G(I_S tensor L)`, which equals `(I_S tensor L)G` on
the logical subspace. Define

\[
\widetilde f(s)=2-\mathbf1_{s=0}\pmod5.
\]

Combining (12) and (14) gives the full identity

\[
W|s,p,a,0\rangle_{S,P,A,b}
=|s,p+\widetilde f(s),a,0\rangle_{S,P,A,b}
\quad(0\leq s,p,a\leq4).
\tag{15}
\]

On source code levels `0,1,2,3`, the responses are `1,2,2,2`.
The equality includes every initial port value, not only a blank port.
All 10,000 matrix units of the 100-dimensional intended joint code are
consequently determined by the same linear isometry (all pairs of its
basis vectors, not merely its 100 diagonal inputs).
Hardware source level `4` receives response `2` by the declared extension.

The exact chronological pulse list, with phase zero and ion labels retained,
is:

| Pulse | Ion | Kind | Logical level `k` | Area |
|---:|:---:|:---:|---:|:---:|
| 1 | P | R | 3 | -pi |
| 2 | P | R | 0 | pi |
| 3 | P | R | 3 | pi |
| 4 | P | R | 1 | -pi |
| 5 | P | R | 3 | pi |
| 6 | P | R | 1 | pi |
| 7 | P | R | 4 | -pi |
| 8 | P | R | 1 | pi |
| 9 | P | R | 4 | pi |
| 10 | P | R | 2 | -pi |
| 11 | P | R | 4 | pi |
| 12 | P | R | 2 | pi |
| 13 | S | R | 0 | pi |
| 14 | S | B | 0 | pi |
| 15 | P | B | 1 | -pi |
| 16 | P | B | 0 | pi |
| 17 | P | B | 1 | pi |
| 18 | P | B | 2 | -pi |
| 19 | P | B | 1 | pi |
| 20 | P | B | 2 | pi |
| 21 | P | B | 3 | -pi |
| 22 | P | B | 2 | pi |
| 23 | P | B | 3 | pi |
| 24 | P | B | 4 | -pi |
| 25 | P | B | 3 | pi |
| 26 | P | B | 4 | pi |
| 27 | S | B | 0 | -pi |
| 28 | S | R | 0 | -pi |

Thus the writer uses `14 carrier + 14 blue` ideal pulses. The count excludes
any extra compensation, addressing-settling and calibration operations.
For square resonant pulses its duration is
`sum_l pi/|Omega_l|`, with the correct carrier or sideband Rabi frequency
for each row; for shaped pulses each signed area is fixed instead. No
zero-time intervention, calibrated numerical duration, or new experimental
fidelity is asserted.

## 6. Why higher oscillator couplings are never truncated away

Initially all three ions are in logical `D` states and the mode is in
vacuum. Pulses 1-12 are carrier pulses; they can temporarily populate
`|g,0>` on the port but keep motion zero, and finish with no port auxiliary
population. Pulse 13 can populate only source `|g,0>` on the LOW branch.
Pulse 14 couples this state only to source `|0,1>` and finishes with the
source in a logical `D` state. On every other source input, pulse 14 is
dark and motion remains zero.

During each of pulses 15-26, the addressed port can occupy a logical
`|k,1>` or its partner `|g,0>`, or a dark logical state. A blue pulse moves
amplitude only between these two partners; after each triple the port is
back in logical `D` and the initial motion of that triple is restored.
The source remains in a `D` state throughout these target pulses. In the
non-LOW branch the target stays in logical `D` with motion zero and all
the blue pulses are dark. Hence no addressed blue pulse ever finds
`|g,1>` or a logical `|k,2>`.

Pulse 27 reverses pulse 14 on the LOW branch, transferring source
`|0,1>` to `|g,0>`. Pulse 28 restores the source logical state. This
argument holds throughout each continuous pulse, not merely at its
endpoints, and holds for superpositions by invariant-subspace linearity.
It proves exact confinement to the used oscillator sectors under (1)-(2).
It is not a claim about off-resonant terms omitted in deriving (1)-(2).

## 7. An eight-carrier-pulse local negation

For use in the encoded waiting and signed exchange, a local operation
`NEG|p>=|-p mod5>` requires no motional excitation. Its chronological
construction is

1. `R_1(2pi,0)`;
2. `R_2(2pi,0)`;
3. the three carrier pulses of `Q_(1,4)` in (5);
4. the three carrier pulses of `Q_(2,3)` in (5).

The first two operations multiply logical levels `1,2` by `-1`, all
others by `+1`, and give auxiliary `g` net phase `+1`. Equation (6)
then gives `1->4`, `4->1`, `2->3`, `3->2`, `0->0`, all with phase `+1`;
the auxiliary is fixed. This is exactly `NEG` on the full five-level
logical space, using eight carrier pulses. The first two have area `2pi`
and must not be assigned the duration of a `pi` pulse.

## 8. Physical scope

This proof supplies a completely phased pulse construction under an
explicitly declared effective Hamiltonian. It does not supply the trap,
laser, cooling, calibration, controller or archive persistence. The drives
are external energy and phase resources; the proof does not assert a closed
energy-conserving unitary with a common unchanged quantum controller.
The moving native dictionary and its experimental use must be stated
separately: implementing a time-dependent encoded model does not derive
its clock, selector, or physical source from native `U`.

The experimentally documented need to track relative phases beyond the
addressed two-level subspaces is also discussed in
[Ringbauer et al., *A universal qudit quantum processor with trapped ions*,
arXiv:2109.06903](https://arxiv.org/abs/2109.06903).
No quantum measurement postulate or first-outcome law is derived by the
unitary writer identity (15).
