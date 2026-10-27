# Finite battery completion with a positive clock account

**NON-CANONICAL. L1. Conditional candidate-T analytical construction.**
No scientific executable or numerical simulation is used in this proof.
The energy below is a specified account for the extended model. It is not
identified with the canonical spectral energy or with a derived physical
Hamiltonian.

## 1. The system whose energy is counted

Let S be the complete finite Hilbert space of the chosen apparatus: finite
object and carrier boxes, receiver, every preparation and filter register,
every rejected-history register, reversible work bits, program, and cyclic
clock. A passive reference R is arbitrary and is never discarded in the
comparisons below. The finite box is chosen before execution and contains
the entire target support for the stated finite horizon.

Let the clock have labels c=0,...,M-1 and let

    E_C = epsilon sum_c c |c><c|,       epsilon>0.

For the data choose in advance a nonnegative integer diagonal account N_D.
One concrete choice on fixed finite coordinate representatives is

    N_D = (R-s)^2 + r^2 + (x-s)^2 + I_pulse
          + sum_j (I-|0><0|)_pentit_j + sum_k |1><1|_bit_k.

The source site s, coordinate representatives, finite boxes and counted registers
together with the pulse indicator are fixed properties of the model, not selected by
the accepted outcome. This account acts as identity on the logical label
and receiver-message factors and on any omitted coin factor. Uncounted
program states can be assigned one fixed common energy; a constant energy
origin does not affect any transition or proof.

The full system account is

    E_S = epsilon N,       N = c + N_D,
    N = sum_(q=0)^Q q P_q,       0<=N<=Q I,       Q>=1.

Zero projectors are permitted. Q is an upper bound, not necessarily the
largest attained value. Choosing a square integer Q above the maximum is
allowed and makes the flat preparation in Section 4 rational when the
specified L is used. There is no zero-energy clock: the pre-wrap advance
from c=0 to c=k raises its account by k epsilon.

For the common spatial representatives [-R_box,R_box] used in the clock
construction, set R_box=|s|+T+D+H+3. Here D is the number of filter pentits,
D+1 includes the source-loader pentit, and B_work is the number of binary
work/flag registers. An explicit integer upper bound is

    q_max = (M-1) + 2(R_box+|s|)^2 + R_box^2
            + 1 + (D+1) + B_work.

Use Q=q_max, or the least square integer Q>=q_max if rational flat amplitudes
are desired. The bound counts every state of the complete finite boxes,
not only successful histories. The initial full basis source has R=x=s,
r=0, standing-token arrangement, clock c=0 and every auxiliary register zero.
It has N=0 for every initial logical-label/old-memory/reference vector.
These are selected confinement, register and clock energies. They make an
explicit positive account possible. They do not prove that the original
TWIST-J law supplies these energies, or that a unit of clock phase is a
specified number of seconds. A different independently chosen commensurate
finite account can replace N without changing the construction.

## 2. A finite battery and the complete sector map

Fix an integer L>=Q and set

    B = L+2Q-1,
    H_B = span{|n>: n=0,...,B},
    E_B = epsilon sum_(n=0)^B n |n><n|.

The complete system-plus-battery account is E_0=E_S+E_B. Its integer total
energy label is t=q+n. Its t-sector is

    S_t = direct_sum_(q: 0<=t-q<=B) P_q S tensor |t-q>.

For every Q<=t<=B this is a full copy of S. Define the unitary identification

    J_t psi = sum_q P_q psi tensor |t-q>.

Let V be any unitary on S, including a full programmed tick or one complete
forward target gate. Define its battery lift on every sector by

    Gamma(V)|_(S_t) = J_t V J_t^*       if Q<=t<=B,
                     I_(S_t)           otherwise.                 (E1)

Each block is unitary. The sectors are orthogonal and exhaustive, including
all edge sectors. Thus Gamma(V) is a full unitary with

    Gamma(V)^* = Gamma(V^*),
    Gamma(V_2) Gamma(V_1) = Gamma(V_2 V_1),
    Gamma(V)^* E_0 Gamma(V) = E_0.                               (E2)

The second identity is global, not merely an identity on the prepared
state. On full sectors it is multiplication of V_2 and V_1; on every other
sector both sides are identity. Nothing is projected out at the battery
boundary, and no rejection is assigned zero weight.

In a full sector the matrix formula is

    Gamma(V)(P_q psi tensor |n>)
      = sum_(q') P_(q') V P_q psi tensor |n+q-q'>.                (E3)

Equation (E3) is the matrix of one coherent unitary. It does not instruct
an energy measurement or a sequence of sharp spectral projections. The
projectors only specify that matrix. The inverse in (E2) proves retained
information; it is not an instruction to run a backward object step.

## 3. Exact positive energy, including clock advance

Prepare the battery in

    b_L = (1/sqrt L) sum_(n=Q)^(Q+L-1) |n>.                     (E4)

For every system input, every supported initial total label satisfies

    Q <= q+n <= L+2Q-1 = B.

Therefore all amplitudes start in full sectors. Every lifted operation
preserves t, so all later amplitudes remain in those full sectors, for any
word length and any retained history. One does not need a fresh battery or
an additional Q-wide margin for each gate.

The battery dimension, capacity and initial mean are exactly

    dim H_B = L+2Q,
    E_B,max = epsilon (L+2Q-1),
    <E_B>_initial = epsilon [Q+(L-1)/2] = E_B,max/2.             (E5)

For every input, including arbitrary reference entanglement, conservation
gives the actual account

    Delta<E_B> = -Delta<E_S>.                                  (E6)

If the target tick advances a sharp clock c to c+1 mod M and E_S commutes
with the clock projectors, its lift has the same sharp clock transition:
the spectral blocks in (E3) cannot create an absent clock matrix element.
Consequently, before the first wrap, after k ticks from c=0,

    Delta<E_B> = -k epsilon - Delta<E_D>.                       (E7)

The battery actually supplies or receives this account. It is not assumed
to return exactly to b_L, and it may be correlated with the data and the
retained histories. On the eventual clock wrap its clock contribution is
returned according to the same law. That cyclic bookkeeping does not reset
or erase any data and does not supply an indefinitely advancing clock.

For a bounded data account, a useful energy-readout consequence of the
uniform error below is

    |Delta<E_S>_actual - Delta<E_S>_target| <= epsilon Q eta.    (E8)

Here the initial states agree, and the output expectation comparison follows
from trace distance at most eta and spectral diameter epsilon Q. Energy
conservation (E6) itself has no approximation error.

## 4. Uniform complete-state error with no gate-count multiplier

Embed H_B by zero extension in l2(Z). Let T|n>=|n+1> and define the unitary

    A = sum_q P_q tensor T^q.

On every prepared input in (E4), and on all its later full-sector outputs,

    Gamma(V) = A^* (V tensor I) A.                              (E9)

For the flat vector in (E4), and 0<=q<=Q<=L, direct overlap counting gives

    <b_L,T^q b_L> = 1-q/L,
    ||(T^q-I)b_L||^2 = 2q/L <= 2Q/L.                         (E10)

Orthogonality of the P_q implies, for every unit vector psi in S tensor R,

    ||(A-I)(psi tensor b_L)|| <= sqrt(2Q/L).

The same bound holds with A^*, with V psi in place of psi, and with arbitrary
reference dimension. Applying the triangle inequality to (E9) gives

    || Gamma(V)(psi tensor b_L) - (V psi) tensor b_L ||
         <= 2 sqrt(2Q/L) =: eta.                              (E11)

The two compared vectors include the complete battery, clock, work bits and
all accepted and rejected histories. A final flag or a partial trace cannot
increase the associated trace-distance bound.

For an arbitrary gate word V_k...V_1, identity (E2) gives

    Gamma(V_k)...Gamma(V_1) = Gamma(V_k...V_1).

Apply (E11) once to the product. The bound is eta for every complete prefix,
not k eta. This is a property of this one common coherent battery and this
exact representation; it is not a generic claim that independent gate errors
fail to accumulate. It also does not compare the actual correlated battery
after a prefix with a newly prepared battery at that prefix.

For the stated finite apparatus choose

    L = Q 5^22.

Then

    eta^2 = 8/5^22,
    eta < 3/5^11 < 1/6000000,                                (E12)

since 8<9 and 3*6000000<5^11=48828125. No decimal estimate is used. If Q is
chosen square, the coefficient 1/sqrt L=1/(sqrt Q 5^11) in (E4) is rational.
This algebraic convenience supplies no native preparation circuit. The
battery still has the explicitly large dimension Q 5^22+2Q.

The bound applies uniformly to the full cyclic autonomous unitary U and
all its powers by taking V=U^k. The intended finite experiment uses only the
pre-wrap interval specified in the main construction. Repetition on a fixed
finite S does not imply repeated fresh experiments with growing archives;
adding those archives changes S and its energy bound Q.

## 5. Sharper initialized-source statement and unchanged acceptance weight

The common source just specified has an advantage over arbitrary-input
comparison: its complete initial vector psi_0 is an N-eigenvector of value
q_0=0, even when its logical input and occupied old memory are arbitrarily
entangled with a reference. More generally assume N psi_0=q_0 psi_0. Then
(E9) gives the exact complete output

    Gamma(V)(psi_0 tensor b_L)
      = sum_q P_q V psi_0 tensor T^(q_0-q) b_L.                 (E13)

For any bounded system observable O commuting with N, orthogonality of the
energy blocks and unit norm of every shifted battery state give

    <Gamma(V)(psi_0 tensor b_L), O Gamma(V)(psi_0 tensor b_L)>
         = <V psi_0, O V psi_0>.                              (E14)

The same assertion holds with a passive reference included. In particular
the final flag projector F commutes with the selected diagonal N, so its
weight p is exactly the ideal weight, not merely close to it.

There is also a stronger conditional vector comparison. Write phi=V psi_0
and assume p=||F phi||^2>0. Since F commutes with each P_q, the actual flagged
vector is sum_q P_q F phi tensor T^(q_0-q)b_L and has the same squared norm p.
The energy components remain orthogonal even after F. Equation (E10), also
valid for negative shifts of the same magnitude, therefore gives

    || F Gamma(V)(psi_0 tensor b_L) - (F phi) tensor b_L ||^2
       = sum_q ||P_q F phi||^2
                       ||(T^(q_0-q)-I)b_L||^2
       <= (2Q/L) p.                                         (E15)

Dividing by the common sqrt(p), the normalized conditional joint states
have vector distance at most

    delta = sqrt(2Q/L) = sqrt(2)/5^11 < 1/30000000.            (E16)

The last strict inequality follows from sqrt(2)<3/2 and
3*30000000 < 2*48828125. There is no inverse acceptance-weight factor in
(E16). This exception to generic postselection error amplification uses the
specific energy-eigenstate preparation, diagonal flag, one common battery,
and exact representation (E2). It is not asserted for arbitrary preparation
errors, arbitrary target implementations or flags failing to commute with N.

Consequently, if the pinned ideal source-and-filter construction of PR #1746
is correct at its stated scope, the present basis-source implementation has
exactly its ideal acceptance weight and hence

    p_basis > 1/20000.                                       (E17)

Let B_b be the nominated wider bound-band projector of that source. It need
not commute with the selected coordinate energy, so its expectation is not
claimed exact. Nevertheless, the conditional trace distance is at most
delta, and the ideal conditional outside-band weight satisfies

    r_ideal < 50000/(99*2^29) < 19/(20*10^6).

For completeness, the latter rational comparison is equivalent to

    1000000000000 < 1009854185472.

Taking the outside-band observable of norm at most one in the conditional
state gives

    r_actual <= r_ideal + delta
              < 19/(20*10^6) + 1/(30*10^6)
              = 59/(60*10^6) < 1/10^6.                      (E18)

Thus these two displayed thresholds survive this particular finite energy
completion. Equations (E17)-(E18) inherit the ideal source/selection proof as
a candidate premise. They are L1 squared-norm statements, not an occurrence
law and not independent acceptance of that premise.

The occupied-memory transfer also has an exact initialized statement.
The selected N is identity on every source label and receiver-message
factor. Suppose the target accepted vector factorizes, as in the pinned
source proof, as

    F V(psi_rest tensor Xi_(L,D,R))
      = phi_rest tensor (SWAP_(L,D) tensor I_R) Xi_(L,D,R).

Each P_q acts on rest only, so (E13) gives exactly

    [sum_q P_q phi_rest tensor T^(-q)b_L]
      tensor (SWAP_(L,D) tensor I_R) Xi_(L,D,R).                (E19)

The battery can correlate with object and history, but does not erase or
dephase the old logical information or its reference correlations in this
factorized accepted channel. On incoming label 1 the receiver is exactly d1.
For a selected front initially at x=100+H, the diagonal lift preserves the
native transition support, and the H subsequent released ticks cannot reach
the sole rewriting edge (99,100). Hence the same finite-buffer argument
protects this exact receiver value for all those ticks. This is protection
of the record, not an all-time binding or reuse theorem.
## 6. Which support and holding statements remain exact

For the concrete diagonal account in Section 1, E_S and all P_q are diagonal
in the target configuration basis. Equation (E3) then multiplies each allowed
data transition by a battery shift without introducing a new transition
between data configurations. A zero matrix element remains zero. Thus the
clock advance, finite propagation speed, absence of carrier motion during
an object-only filter gate, and any other configuration-support restriction
of a target gate remain exact on the full sectors visited by the preparation.
The amplitudes and data-battery correlations need not be the ideal ones.

There is also an exact spectator statement for the scalar, additive energy
construction used here. Suppose S=S_A tensor S_H,

    N=N_A tensor I + I tensor N_H,
    V=V_A tensor I_H,

with integer spectra. On the infinite comparison battery,

    A=A_A A_H,       [A_A,A_H]=0,       [V,A_H]=0.

The A_H factors cancel in A^* V A. Hence the lift of this operation acts as
identity on the entire H factor, including its arbitrary coherences and
reference correlations, throughout the initialized full-sector domain. This
statement is stronger than fixing a coordinate population. It relies on
additivity of the account and the actual tensor spectator condition. A
controlled position test need not satisfy that condition: its intentional
correlations are part of the target instrument.

In particular, an object-only filtering segment can hold the complete
carrier/receiver factor exactly in this selected additive model. A lifted
native transport step is generally not identical as a data channel to its
unfunded target step, because its energy transitions correlate the battery.
Its complete-state difference is bounded by (E11), while its basis support
and speed bound remain those of the target. No claim of exact unchanged
native dynamics during those transport steps follows from exact funding.

## 7. A nonzero account is not a local physical implementation certificate

The finite construction proves all-state unitarity, exact conservation of a
specified positive additive energy, one finite coherent preparation,
reference-uniform approximation of the complete target, and exact funding
of the nondegenerate clock ladder. These are substantive properties of one
declared discrete extension.

Several boundaries remain explicit:

- The new primitive is Gamma(V), with its energy-dependent coherent battery
  shifts. Even when V contains only forward controlled object calls, (E1)
  is not a compiler of those battery couplings into the original gate alphabet.
- The battery is one finite but large coherent register. Its preparation and
  its routing to the controlled sites remain supplied operations. A finite
  dimension alone gives neither a local bounded-strength interaction nor a
  realistic source preparation time.
- The positive account E_0 is conserved by the discrete unitary. Conservation
  alone does not identify E_0 with the generator of continuous physical time.
  A Hamiltonian, its interactions, their spatial range and strength, and a
  calibration of the clock tick are separate physical data.
- A formal logarithm of the full unitary can interpolate its sampled values,
  but does not prove local interactions, exact holding between sample times,
  or forward-only microscopic Hamiltonian propagation. No such inference
  is made here.
- Finite-box agreement of the original finite-range walk over a support cone
  does not identify a separately defined box energy with the infinite-space
  canonical spectral energy. The selected diagonal account above makes no
  such identification.
- The finite buffer and output comparisons remain finite-horizon statements.
  Actual occurrence, asymptotic frequency, useful reset and an unlimited
  archive are not consequences of this battery construction.

## 8. Relation to existing energy sources

The public canonical [SELECTED-SPECTRAL-ENERGY-SOURCE theorem](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L26773)
already supplies full total-energy fibers, exact additive conservation and
uniform approximation for any specified bounded system energy. Its battery
has finite energy capacity but infinite Hilbert dimension. Its chosen
continuous generator does not include an intrinsic stopping clock.

The construction here uses the same general energy-translation idea with a
finite commensurate spectrum and a finite flat battery. Its additional
features at this scope are the complete finite edge-sector definition, the
exact representation identity for the entire scheduled word, and inclusion
of a positively counted finite clock. It does not claim invention of
coherent energy references. See also Johan Aberg, [Catalytic Coherence,
Phys. Rev. Lett. 113, 150402 (2014), arXiv:1304.1060v3](https://arxiv.org/abs/1304.1060v3).
The finite proof above is self-contained and does not import a claim of
unlimited useful catalytic reuse or independent fresh outputs.
