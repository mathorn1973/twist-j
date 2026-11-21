# Proof: paid quadratic recording of an oriented integer loop

PUBLIC / NON-CANONICAL / L1. Authored candidate-T, not independent review.
Probe P-FUNDED-AREA-PHASE-RECORD-1, reservation #1584.
A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
All hypotheses, primitives and scope are fixed in PREREG.md.

## 0. What is constructed, and what is not

This constructs one deliberately selected integer comparison automaton.
It answers an existence question conditional on its explicit carrier,
quadratic cost, two shear primitives, reference preparation, direction and
program bits, finite controller and algebraic Weyl representation.
It does not select these data from J, the registered native U, or Nature.

The registered INTEGER-ENERGY-FUNDED-INVOLUTION [T] gives the general funding
mechanism. The finite Weyl relation in FORCE-WEYL-HOLONOMY [T] supplies the
algebraic phase convention. The present result connects them on actual
finite histories of a newly specified model. The preceding noncanonical
P-J-RAMIFIED-AREA-WEYL-1 is motivation and a boundary, not a promoted premise.
In particular this proof does not preserve a positive cost under its J/phi
scaling, nor identify its paired module with this state space.

## 1. Whole-carrier invertibility, including funding failure

Write z=(q,p,u,v) in Z^4. The underlying maps Q_h and P_h have inverses
Q_-h and P_-h. This follows by substitution; P_h fixes q, so its inverse
subtracts the same h*q from both references.

On s=(z,b,sigma,eta,c), with b>=0, the requested letter F_a,epsilon tries
T_a^(epsilon*sigma), where T_0=Q_1 and T_1=P_1. Set
Delta=H(T_a^(epsilon*sigma)z)-H(z).
An accepted step changes z to the candidate and b to b-Delta while retaining
sigma. A rejected step fixes z,b and flips sigma. Eta and c are spectators.

Claim: F_a,-epsilon is the complete inverse.
If the first step is accepted, the opposite sign tries the inverse lattice
map. Its cost is -Delta, and its proposed bank is (b-Delta)+Delta=b>=0.
It is accepted and restores every coordinate. If the first step rejects,
the opposite requested sign at the flipped direction tries
(-epsilon)*(-sigma)=epsilon*sigma, the same unaffordable candidate. It
rejects again and restores sigma. No two inputs are merged. The same
argument with epsilon reversed proves both inverse compositions.

E=H+b is preserved in either case and b stays nonnegative. Each accepted
P step changes both references by the same integer and Q changes neither;
therefore d=u-v is invariant on the whole raw carrier, including rejection.

The expanded cost formulas, for h in {+1,-1}, are

    Delta_Q = 2h q+1,
    Delta_P = 2h p+1+2h q(u+v)+2q^2.

The alternate calculation in verify.py uses these polynomials rather than
subtracting two values of H. Its agreement is a same-author implementation
check, not an independent proof or blind second author.

For comparison with the inherited funding theorem, adjoin the direction to
the bare bijection to obtain the involution
(z,sigma)->(T_a^sigma z,-sigma), fund it using H, then compose with a direction
flip. This gives the positive requested F above, including its reflected
rejection; the negative F is its inverse. Simply fixing an unaffordable
input of an arbitrary noninvolutive translation would not suffice.

## 2. One autonomous finite controller

The program bit eta is part of the complete state and remains unchanged.
At phase c the word is (Q+,P_eta,Q-,P_-eta). Apply its funded letter and
replace c by c+1 modulo four. To invert, replace c by c-1 and apply the
inverse of the letter at that previous phase. This proves that U_* is a
total autonomous permutation on

    Z^4 x N_0 x {+1,-1}^2 x C4.

Eta is neither secretly changed during execution nor an argument to the
reference reader. The two opposite witnesses have different initial eta:
there is no claim that equal complete initial states give different results.
The two finite bits and the four-phase clock have zero assigned cost in this
selected model. No infinite zero-cost history tape has been added.

## 3. Actual path, occupied reference update and quadratic readout

Every step is axis aligned in (q,p), and on every actual step, accepted or
rejected,

    Delta u = Delta v = q_i Delta p.

This identity follows directly from P_h; on Q or rejected steps both sides
are zero. Thus on any finite actual history let

    A=sum_i q_i Delta p_i.

Then u_final=u_initial+A and v_final=v_initial+A. This is an induction over
actual transitions, not a preparation or a phase-based definition of the
reader. It works also on already occupied references and on reflected
trajectories after funding failures.

Writing D=u^2-v^2, its actual energy difference obeys

    D_final-D_initial=2(u_initial-v_initial)A.

For the once-only common reference (1,-1), D_initial=0 and the invariant
reference separation is two. Consequently

    A_read=(E_+-E_-)/4=A,       E_+=u^2, E_-=v^2,
    E_++E_-=2+2A^2.

The reader receives only two ORDERED current quadratic values. It does not
receive eta, q,p, a transcript, loop count, phase exponent or an external
answer. The coefficient four is the elementary polarization factor for this
selected reference separation, not a Planck normalization.

If the references are unprepared, d may vanish or their initial D may be
unknown. This readout claim is not total on all those states. General
occupied-reference continuation remains reversible; to recover the
increment from energies one additionally needs the appropriate initial D
and nonzero d. Aggregate area is recorded, not every previous state: paths
with equal A can have the same references, and reversed area can cancel.

The shoelace sum is computed only from the base path:

    A2=sum_i(q_i p_(i+1)-p_i q_(i+1)).

Because Delta q Delta p=0 at each step,

    q_final p_final-q_initial p_initial
      =sum_i(p_i Delta q_i+q_i Delta p_i),
    A2=sum_i(q_i Delta p_i-p_i Delta q_i).

Subtracting gives

    2A=A2+q_final p_final-q_initial p_initial.

For an integer-closed base path, A=A2/2 is its signed rectilinear polygon
area, with repeated edges and signed winding counted. For open paths it is
a marked line integral, not a translation-invariant closed area. Reversing
a whole actual path negates this integral and restores the two references.

## 4. Literal Weyl path calculation and its limits

Fix an abstract five-dimensional module with X|k>=|k+1> and Z|k>=j^k|k>.
This is an additional algebraic representation. It is not an observed phase
of U_* and does not supply a physical Hilbert norm or Born instrument.

For a given realized history, assign X^Delta q to a q step, Z^Delta p to
a p step, and I to a rejected step. Evaluate the ordered product literally
on all five basis vectors, applying each new letter on the left. For a path
starting with base coordinate q0, let Q=q_final-q0 and P=p_final-p0.
Induction gives

    W_path |k> = j^(kP + A - q0 P) |k+Q>.

A horizontal step only changes the current basis label. A vertical step
adds Delta p times its current label k+q_i-q0 to the phase, proving the
formula. In particular, from q0=p0=0 this is

    W_path |k> = j^(k p_final+A) |k+q_final>.

For an integer-closed base path, Q=P=0, hence W_path=j^A I. With the prepared
reference, this is exactly

    W_path = j^((E_+-E_-)/4) I.

The polygon sum, literal five-basis product and ordered quadratic reader
are computed separately in the audit. Their equality follows from the
chosen primitive algebra. It is not independent physical confirmation and
not a derivation of that algebra.

Important distinctions:

* A scalar j^A on one isolated ray is not itself an interferometric
  observation. A physical phase comparison/reference apparatus is absent.
* U_* has state-dependent funding and direction reflection. The nominal
  four-letter word is valid only when every requested move succeeds with
  the prescribed direction. The proof assigns the word to ACTUAL moves,
  including identity at rejection, and claims no global unmodified Weyl
  representation of the whole funded automaton.
* Closure modulo five alone is not integer closure. The probe's closed-loop
  claims use q_final=q_initial and p_final=p_initial as integers.
* The area integer is not asserted to be the Hamiltonian principal action
  or a stationary-action functional. No physical energy-time law follows.

## 5. Same complete coarse cost history, opposite recorded area

At B=4 the once-prepared eta=+1 history in (q,p,u,v,b) is

    (0,0,1,-1,4),
    (1,0,1,-1,3),
    (1,1,2,0,0),
    (0,1,2,0,1),
    (0,0,2,0,2).

For eta=-1 it is

    (0,0,1,-1,4),
    (1,0,1,-1,3),
    (1,-1,0,-2,0),
    (0,-1,0,-2,1),
    (0,0,0,-2,2).

Sigma remains +1 and c advances 0,1,2,3,0 in both. Eta differs as an explicit
initial program bit. Both have H=(2,3,6,5,4), bank=(4,3,0,1,2), source costs
q^2+p^2=(0,1,2,1,0) and summed reference costs=(2,2,4,4,4). Thus the entire
coarse history used in PREREG is identical, including all total work
increments (1,3,-1,-1). Any deterministic function of only this coarse
record must return the same value. It cannot return j and j^-1 separately.
This is a precise observation-kernel obstruction, not a claim about a
reader additionally supplied eta or the complete state.

The ordered endpoint reference costs are (4,0) and (0,4). Their difference
reader returns +1 and -1, exactly the two geometric areas and phases. Total
reference work is positive and equal to two in both; the signed readout is
a contrast between two nonnegative energies, not negative total energy.

With both initial references instead zero, the two funded squares finish
at (u,v)=(1,1) and (-1,-1). Squared costs are (1,1) in both, while phases
remain opposite. The chosen antipodal reference is therefore an essential
resource for this readout, not merely decoration.

## 6. Sharp stock requirement and the five-lap witness

Suppose k laps have succeeded from the common preparation. The references
are (1+eta*k,-1+eta*k); their cost is 2+2k^2. During lap k+1 the H values
are, in order after each of its four moves,

    2k^2+3,
    2(k+1)^2+4,
    2(k+1)^2+3,
    2(k+1)^2+2.

The largest H in the first K complete ideal laps is 2K^2+4. Total E is B+2.
Each candidate is funded exactly while its H<=E. Therefore all first 4K
moves succeed iff B>=2K^2+2. This is both necessary and sufficient, not a
post-run fitted buffer. If an earlier move rejects, all-success is already
false and the altered actual path must be evaluated instead.

After K successful laps the bank is B-2K^2, the base and controller return,
and the recorded area is eta*K. For K=5,B=52,eta=+1, the complete endpoint is

    (q,p,u,v,b,sigma,eta,c)=(0,0,6,4,2,+1,+1,0).

The Weyl product is identity, but the ordered reference costs are (36,16),
the area read is five and the paid work is fifty. Initial and final total
E are both 54. Fivefold phase closure therefore does not erase the actual
integer record or restore the stock. Source return alone is not reset.

For B=3 the second candidate is unaffordable. Direction reflection changes
later attempted signs; the nominal loop is not the actual history. The
verifier checks the actual path/read/phase relation in this case too.

## 7. Finite energy implies finite capacity and recurrence here

On the shell E=N, all four integer coordinates have absolute value at most
floor(sqrt(N)), and b is uniquely N-H. Including sigma,eta,c gives at most
16(2 floor(sqrt(N))+1)^4 states. U_* preserves this finite set bijectively,
so every complete state is periodic, with no transient part.

On the prepared class, the reference cost alone is 2+2A^2. Since total E=B+2,
2A^2<=B. Thus |A|<=floor(sqrt(B/2)) along any actual trajectory, even after
failures. This is a bound for this coercive integer model, not a universal
information-versus-energy theorem. The paired references are not an
unbounded zero-cost archive, and the finite controller cannot hide one.

Inverting the complete finite trajectory, including its controller and
rejected branches, restores the initial state and refunds the cost changes.
Forward evolution can also return by finite recurrence. Neither is a
contract for arbitrarily long retained fresh records while reusing the same
finite bank. No preparation/reset operation was derived from native U.

## 8. Verification and scientific meaning

All identities above are direct all-carrier proofs. The frozen audit checks
every raw state with E<=12, all words of length through eight on a sufficiently
funded common ready, the sharp finite budget grid, zero-reference and
underfunded controls, and actual full-state recurrence at B=4.
It never treats a bounded sample as the proof of an unbounded theorem.

The contact/shear, positive cost, marked reference and phase character are
openly selected. Neither the choice of those primitives, an action unit,
the physical tick, nor an SI normalization is forced. Uniform rescaling of
the chosen energetic unit together with the stock changes no funded
trajectory or phase character on the correspondingly scaled stock class.
The integer area read is not a new dimensionful constant.

The substantive advance is a complete mathematical example in which an
ordered pair of paid quadratic reference values retains the oriented area
of actual source cycles, compatible with a separately calculated fifth-root
Weyl path phase. Its substantive boundary is equally precise: scalar cost
history alone loses orientation, phase loses multiples of five, and finite
stock bounds the paid record. Physical admission, an actual phase detector,
a native contact and an energy-time action law are still not supplied.
