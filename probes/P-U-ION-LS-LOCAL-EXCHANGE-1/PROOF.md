# Finite common-control words for the actual local exchanges

**NON-CANONICAL analytical candidate; conditional on [MODEL.md](MODEL.md).**
Reservation: #1364. This proof supplies two predetermined local pulse words,
not a full preparation-to-boundary-nine apparatus. No numerical integration,
pulse search or scientific program execution establishes the construction
below. Its mathematics was known during preparation and is disclosed before
the prospective formal audit.

## 1. Target, primitive convention and fixed profile

The active physical label spaces are S=Q=C^5, with basis labels 0,...,4.
For c=1 and c=4 separately, the required local family is

    |s,c> -> |c,s>,                s=0,...,4.             (1)

The fixed unequal dictionary of the global encoding audit gives c=1 at the
first actual contact and c=4 at the second. The two words constructed here
depend on c, which is fixed by the contact stage, but never on s or an
original history label. The other data coordinates are spectators in this
local model; their physical isolation remains a declared premise.

Write single-ion selective rotations as

    R_ab(theta,phi) = exp[-i theta sigma_ab(phi)/2],
    sigma_ab(phi) = exp(-i phi)|a><b| + exp(i phi)|b><a|.

The physical carrier primitives are ONLY common star rotations

    R_0j(theta,phi) tensor R_0j(theta,phi),    j=1,...,4.

On levels outside {0,j}, each R_0j is identity. An inverse requires no
negative-duration pulse:

    R_ab(theta,phi)^dagger = R_ab(theta,phi+pi),           (2)

with positive theta and phase understood modulo 2 pi. All carrier actions
below refer to the complete compensated/frame-specified primitives in
MODEL.md. Additional unaccounted level-dependent drift is not silently
discarded from a claim about coherent phases.

Use one fixed real nonconstant light-shift profile

    D0 = diag(d0_0,...,d0_4),             D=u D0,
    S1 = sum_j d_j,                      S2 = sum_j d_j^2,
    V_D = 5 S2-S1^2 = sum_(j<k) (d_j-d_k)^2 > 0.         (3)

Here d_j=u*d0_j are the entries of D. In MODEL.md notation, u=lambda_*,
d0_j=MODEL.d_j, delta=delta_* and V_D=u^2 B. This distinguishes the fixed
reference profile from its single chosen intensity scaling.

The one positive scalar u is common to both ports and to every LS pulse.
No individual d_j is tuned independently and no new profile is selected
for a permutation, axis, contact input or intermediate state. The spatial
phase separation is pi, as specified in the physical model.

## 2. One completed force loop

Let F=D_S-D_Q, with D_S=D tensor I and D_Q=I tensor D. After fixing a common
oscillator phase, the selected effective Hamiltonian is

    H(t) = i hbar eta/2 F
           [a^dagger exp(-i delta t)-a exp(i delta t)],
    delta>0,             [a,a^dagger]=I.

For L(t)=-iH(t)/hbar, direct expansion gives

    [L(t1),L(t2)] = -i eta^2 F^2 sin(delta(t1-t2))/2.

This commutator commutes with every L(t). The Magnus terms therefore stop
after the second:

    Omega1(t) = beta(t) F a^dagger-beta(t)^* F a,
    beta(t) = eta[1-exp(-i delta t)]/(2 i delta),
    Omega2(t) = -i K(t) F^2,
    K(t) = eta^2[delta t-sin(delta t)]/(4 delta^2).

Resolving the finite diagonal F into scalar force blocks identifies exact
oscillator displacement operators and justifies these identities without
a numerical Fock cutoff. At the common completed-loop time

    tau = 2 pi/delta,             K = pi eta^2/(2 delta^2),

the displacement vanishes and the full ideal block is

    L_D = exp[-i K(D_S-D_Q)^2] tensor I_motion.           (4)

This closure is an operator identity within the adopted harmonic effective
model. It is not restricted to a freshly prepared motional vacuum. Other
modes, model errors and the physical validity range of this effective
equation remain the limitations stated in MODEL.md.

## 3. Twenty finite conjugations produce the equality phase

Let Aff(1,5) consist of the twenty permutations

    pi_(a,b)(j)=a j+b mod5,       a=1,2,3,4; b=0,...,4.

Use this lexicographic a-then-b order. Let M_pi be any single-ion monomial
unitary with underlying permutation pi. Apply M_pi to both ions, then one
completed L_D, then the true adjoint M_pi^dagger to both ions. In operator
order this block is

    (M_pi^dagger tensor M_pi^dagger) L_D (M_pi tensor M_pi).

The diagonal profile seen in the block is D_pi with entries d_(pi(j)).
Phases in M_pi cancel under conjugation of diagonal D. Every such completed
block is diagonal on the data, so all twenty blocks commute EXACTLY.

For a fixed label j, pi(j) takes every value four times. For distinct j,k,
the ordered pair (pi(j),pi(k)) takes every distinct ordered pair exactly
once: solve a=(v-u)/(k-j) and b=u-a j for any u!=v. Consequently

    sum_pi (D_pi)_S^2 + sum_pi (D_pi)_Q^2 = 8 S2 I,
    sum_pi D_pi tensor D_pi
       = (S1^2-S2) I + V_D E,
    E = sum_j |j,j><j,j|.

Thus the sum of the twenty squared force profiles is

    sum_pi [(D_pi)_S-(D_pi)_Q]^2 = 2 V_D (I-E).          (5)

The exact twenty-loop echo is therefore

    G = exp[-i 2 K V_D (I-E)].                           (6)

Choose the one scalar intensity so that 2 K V_D=pi/2. Equivalently, with
V_0=5 sum_j d0_j^2-(sum_j d0_j)^2,

    u^2 = pi/(4 K V_0) = delta^2/(2 eta^2 V_0).         (7)

This is finite and positive for finite delta>0, eta!=0 and V_0>0. It is a
parameter choice in the ideal model, conditional on its admitted scalar
control range; no apparatus calibration or measured error follows from it.
The resulting raw echo is exactly

    G|j,k> = |j,k>             if j=k,
    G|j,k> = -i |j,k>          if j!=k,
    G = gamma Q,    gamma=-i,  Q=exp(+i pi E/2).          (8)

Equation (5) retains every difference among the four D-manifold shifts.
It needs neither their equality nor arbitrary per-level light-shift control.
This is a finite product identity, not a continuous twirl or a Trotter
approximation.

## 4. Compile all conjugations into the admitted star pulses

Set T_j=R_0j(pi,0). It maps |0> to -i|j>, |j> to -i|0>, and fixes every
other level. Its underlying label permutation is the transposition (0,j),
while its adjoint is implemented by R_0j(pi,pi), as required by (2).

The deterministic compiler writes each permutation into disjoint cycles,
starting each cycle at its smallest member and ordering cycles by their
smallest members. A displayed cycle follows the forward permutation.
Its chronological star lists are:

    [0,a1,...,aL]  ->  a1,...,aL;
    [a1,...,aL]    ->  a1,...,aL,a1   when 0 is absent and L>=2;
    singleton     ->  empty list.

Each listed j means a common T_j pulse. Following a label through these
lists proves the stated cycle permutation: in the second rule 0 returns
to itself, each a_k goes to a_(k+1), and a_L goes to a1. The accumulated
phases need not be corrected because only monomial conjugation of D is
required. Apply the adjoint word in reverse chronological order, using
phase pi on its star pulses, after the LS loop. Replacing that adjoint by
the same pi pulses without inversion is not assumed valid.

Every permutation of five labels requires at most six such star pulses.
If 0 is fixed, a nontrivial cycle among the other four labels of length l
costs l+1; at most two such cycles occur, giving at most 4+2=6. If 0 lies
in a cycle of length l>=2, that cycle costs l-1 and the remaining cycles
give a total at most 4+floor((5-l)/2)<=5. The bound applies in particular
to all twenty affine permutations.

Rotations on two nonzero levels are also finite star words. For distinct
c,j in {1,...,4}, direct conjugation of the two matrix units gives

    R_cj(theta,phi)
       = T_c R_0j(theta,phi-pi/2) T_c^dagger.             (9)

For j=0 one instead uses

    R_c0(theta,phi)=R_0c(theta,-phi).                    (10)

These are one-ion identities applied in common to both ions. Equation (9)
uses three actual star pulses, not a newly assumed direct c-to-j transition.

## 5. Three equality phases exchange one embedded pair

Fix c and j!=c. On their two-level subspace define

    J = |c><c|+|j><j|,
    Z = |c><c|-|j><j|,
    X = |c><j|+|j><c|,
    Y = -i|c><j|+i|j><c|,
    E_out = sum_(k notin {c,j}) |k,k><k,k|.

All of X,Y,Z vanish outside that subspace. Use

    Vx=R_cj(pi/2,pi/2),       Vy=R_cj(pi/2,0).

Conjugation sends Z to X under Vx and to -Y under Vy. The sign in the
second case disappears in the two-ion product. Hence the three conjugated
equality projectors are

    E_z = (J tensor J+Z tensor Z)/2 + E_out = E,
    E_x = (J tensor J+X tensor X)/2 + E_out,
    E_y = (J tensor J+Y tensor Y)/2 + E_out.               (11)

They commute exactly: within the two-qubit block XX, YY and ZZ commute;
on the outside-equal block they coincide; and on the other blocks they
vanish. Their canonical product Q_y Q_x Q_z is

    B_cj = exp[+i pi(E_z+E_x+E_y)/2].                    (12)

Within the two-level tensor square, XX+YY+ZZ=2P_pair-J tensor J, where
P_pair is SWAP on that square. Thus E_z+E_x+E_y=J tensor J+P_pair there.
Its eigenvalues are 2 on the symmetric sector and 0 on the antisymmetric
sector. Equation (12) therefore has the following complete action:

| Input sector | Action of B_cj |
| --- | --- |
| Both labels in {c,j} | minus the two-level SWAP |
| Exactly one label in {c,j} | identity |
| Equal labels k,k outside {c,j} | phase -i |
| Unequal labels both outside {c,j} | identity |

Implement the raw version in this chronological order:

    G;
    (Vx^dagger on both), G, (Vx on both);
    (Vy^dagger on both), G, (Vy on both).

It equals gamma^3 B_cj=i B_cj. Every G includes its twenty independently
closed LS loops. No rotation is inserted inside an unfinished force loop.

## 6. Four pair blocks and a three-pulse correction

For c=1 and c=4 separately, perform the raw pair blocks for j=0,...,4 with
j!=c, in increasing j order. There are four blocks and twelve raw echoes,
so their common echo phase is gamma^12=(-i)^12=1. On the target family,
their product therefore acts as

    |s,c> -> -|c,s>       if s!=c,
    |c,c> ->  |c,c>.                                    (13)

For s!=c, only the block with j=s finds both labels in its pair; it exchanges
them. Every other block sees exactly one label in its pair, before or after
that exchange, and is identity. For s=c, all four blocks contribute minus
one to |c,c>, giving plus one. This proves (13) for every s without an
input-dependent schedule.

Finally define D_c with diagonal entry +1 at c and -1 at the other four
labels. It has determinant +1 and, for either c=1 or c=4, is exactly

    D_c = product_(j in {1,...,4}, j!=c) R_0j(2 pi,0).    (14)

Each of the three factors negates levels 0 and j. Level 0 consequently
receives three signs, each other non-c level one, and c none. The common
correction D_c tensor D_c cancels the minus sign in the first line of (13)
and leaves its second line unchanged. The complete word W_c satisfies

    W_c |s,c> = |c,s>             for every s in F5.      (15)

In the declared ideal primitives the phase in (15) is exactly +1, including
the raw echo phases. Additional uniform scalar phases of a physical model
would affect only a common global phase; any unaccounted level-dependent
phase requires a separate correction or error bound.

Equation (15) is a statement in the declared control frame. MODEL.md also
states the known laboratory-frame phases on these outputs. Those phases
preserve the required basis-label transfer but are not silently identified
with a single common laboratory phase. The stronger coherent comparison
must use that declared phase profile or explicitly compensate it.

The equation also holds by linearity for a coherent source and for a source
entangled with another counted resource, on the whole subspace
C^5 tensor span{|c>}. No coherent-input hypothesis is needed to establish
the weaker original five-label exchange requirement.

This word is NOT a full coherent five-level SWAP. Its action outside the
required family can be read from the same sector table:

    W_c |c,s> = |s,c>                  for s!=c,
    W_c |s,t> = |s,t>                  for s!=t, s,t!=c,
    W_c |s,s> = -i |s,s>               for s!=c.

For example, two distinct labels neither equal to c are left in their
original order. No complete-SWAP synthesis is asserted or required here.

## 7. Finite conservative resource bounds and inherited motion

Each echo has twenty completed LS loops. Four triple blocks use exactly
240 such loops. A permutation and its inverse use at most twelve star pi
pulses per loop, giving at most 2880 star pulses for the twelve echoes.

There are four pair-axis rotations and inverses per pair block. For the
one pair with j=0 these are four direct star pulses of angle pi/2. For
each of the other three pairs, equation (9) implements each of its four
rotations by three star pulses with total angle 5 pi/2. All axis changes
therefore cost forty star pulses with total positive carrier angle 32 pi.
The final correction costs three pulses of angle 2 pi. Altogether:

    completed LS loops:                240,
    common star carrier pulses:        at most 2923,
    total positive carrier angle:      at most 2918 pi.  (16)

These are conservative finite bounds, not optimal counts. If every admitted
star transition has a fixed positive Rabi rate at least Omega_min, the
ideal pulse-duration sum is bounded by

    240 (2 pi/delta) + 2918 pi/Omega_min.

Additional switching, calibration or waiting intervals require their own
stated dynamics and durations; (16) does not silently provide them.

Every LS loop returns the ideal motion operator to identity. Carrier and
monomial pulses have the motion-independent action stipulated in MODEL.md.
Consequently the complete ideal data action factors from the included
motion. It applies to arbitrary inherited motional states and correlations
within the model's admitted domain, without resetting motion between loops
or before the second contact. A separately admitted remainder-only evolution
can be appended without requiring that remainder to be common or fresh.

This factorization does not establish the real-device validity of the
single-mode approximation on arbitrary excitations, closure of other modes,
finite controller or work-source resources, or protection of spectator data.
Those remain separate physical input and error-accounting obligations.

## 8. Meaning of success or failure of this candidate

The analytical result is a finite synthesis of two local ordered-exchange
families in the specified ideal model, using fixed-profile LS loops and
explicit shared star rotations. It is not an implementation of the full
fourteen-register history or its conjugated native selector and generators.
It supplies no independently calibrated numerical error, inherited battery
budget, physical archive-retention interval or derivation of quantum theory
from J. Existing Canon status and the broader physical HOLD are unchanged.

A prospective exact verifier can audit the finite word, phases, compilation
and target action. A failed candidate word or failed audit would refute that
candidate at its stated cause. It would NOT establish an impossibility for
the whole compatible control class. Conversely, exact ideal pulse algebra
does not by itself certify a constructed or error-bounded physical device.
