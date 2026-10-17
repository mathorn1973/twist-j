# Independent derivation before author-result exposure

PUBLIC / NON-CANONICAL / L1 analytical review. A. M. Thorn. Apache-2.0.
Public claim #1560; public session `Codex-v103-RD-20261016`.
This text is frozen before reading the Antigravity proof or result.

All native arithmetic below is in F5; integer and rational formulas are
explicitly labelled. The starting definitions and support theorems are
inherited from v102, as bound by SOURCES.tsv. This is an independent
derivation of their interface consequences, not a new proof of every
inherited native/field theorem. No numerical program is used.

## 1. Reduce the gate to two independent equations

For x=(a,b,c,d,q,r), let A=a+c, B=b+d, C=a-c-2, D=b-d-1.
The inverse affine chart gives

    h1=b+2a=A+3B+C+3D,
    h2=d+2c=A+3B-C-3D.

Consequently

    h1+h2=2A+B,       h1-h2=2C+D,
    h=0 iff A+3B=0 and C+3D=0.                    (1)

Since 2 is invertible, these are equivalences, not only necessary tests.
Direct substitution into the literal generators gives

    g1: h -> (-h2,-h1),
    g2: h -> (-h2+r,-h1-r),
    g3,g4: h -> (-h1,-h2).                       (2)

Thus h=0 and its complement are both preserved by every selected branch
on X14. No closed h-only law for g0 is assumed: it gives
(a+2b,c+2d), which depends on additional piston coordinates.

**Literal specification defect.** Author CONTRACT Q2(1) states
`h_1 = B+2A`. Under its own definitions this is false; the true identity
is the SUM in (1). For E(0,0) at n=0 the raw checkpoint is
(4,3,2,2,0,1), h=(1,1), but B+2A=2. This refutes that literal
clause. The intended necessary condition h=0 => B+2A=0 remains
valid and will be used explicitly; the frozen clause is not silently
rewritten or treated as a reason to discard the entire obstruction.

## 2. Original two-message family: no shell gate point

Let k=lambda+3mu. At origin zero the actual selected prefix is
g2,g2,g4. Substitution in the generators and (1) gives the complete
parametric table for all 25 pairs:

| n | z,A,B,C,D | q,r | h |
|---|---|---|---|
| 0 | 2,1,0,lambda,mu | 0,1 | (1+k,1-k) |
| 1 | 0,3,2,lambda,mu+2 | 1,4 | (k,3-k) |
| 2 | 2,1,0,lambda,mu | 0,1 | (1+k,1-k) |
| 3 | 1,-1,0,-lambda,-mu | 2,0 | (-1-k,-1+k) |

The sums of h's coordinates are 2,3,2,3, respectively, so none is zero.
For n>=3, let s=A in {1,-1}. The complete inherited tail for this pair
is parameterized by

    z,s in {1,-1}, q in F5,
    B=0, C=s*z*lambda, D=s*z*mu, r=z-s-q.

The two selected actions either negate z,s together or negate s,C,D
together. They preserve zC/A=lambda and zD/A=mu, so induction gives

    h=s(1+z*k,1-z*k),       h1+h2=2s != 0.      (3)

The inherited recurrence theorem supplies the complete 20-point tail
for each pair. The 25 disjoint tails, 25 blank points and 25 first-message
points have total 550. Equations above hold on their full parameter sets,
not merely a finite orbit sample. There is no gate point in this entire
support. An alternative integer representative of the same piston residue
cannot change this conclusion.

At each fixed common time, h retains exactly k and loses the other
independent message combination: there are five pairs per k. In contrast,
the full piston vector retains all 25 pairs at every fixed time. The
prefix has two independent preparation directions; on the tail lambda
and mu are recovered from zC/A,zD/A using the common time's z. Equivalently
one common word of bijective generators acts on the 25 prepared points,
whose q,r are common. This does not imply global bijectivity of T_t.
The stationary canonical mixed reader uses full-state context to return
mu on the tail. Cross-time interpretation must keep that context; the
fixed-time argument is not a stationary piston-only reader theorem.

## 3. Alternative family: one transient gate point

Put t=r0=3(1+mu-lambda). The literal g2,g2,g4 prefix gives

| n | z,A,B,C,D | q,r | h |
|---|---|---|---|
| 0 | 2,mu,0,3,0 | 2-mu-t,t | (mu+3,mu-3) |
| 1 | 0,4-mu,2,3,2t | mu+t-1,-t | (-mu+3+t,-mu-3-t) |
| 2 | 2,mu,0,3,0 | 2-mu-t,t | (mu+3,mu-3) |
| 3 | 1,-mu,0,2,0 | mu+t,1-t | (-mu+2,-mu-2) |

At n=0,2,3 the two components cannot both vanish. At n=1 their
sum forces mu=0 and then either component forces t=2, hence lambda=2.
The unique gate checkpoint there is

    x=(2,1,2,1,1,3).                            (4)

On the tail, C in {2,3}, z in {1,4}, B=D=0 and A=2Cz*mu.
Both selected actions preserve these relations. Formula (1) becomes

    h=C(2z*mu+1,2z*mu-1).                       (5)

C is nonzero and the two parenthesized quantities differ by 2, so the
tail contains no gate point. This conclusion includes mu=0.
For each mu the inherited complete tail uses C,z as above and r in F5,
with q=z-A-r. It has 20 points; all five mu give 100, supplemented by
the two 25-point prefix sheets. Thus (4) is the sole gate point in the
full 150-point support. The canonical proof's common times 3,4,7,8 and
the nonzero r slope establish actual coverage; no new search is used.

At a fixed time n=0,2 or n>=3, the piston block and h depend only on mu
and distinguish its five values. At n=1 the two h coordinates recover
mu from their sum and t from their difference, hence also lambda.
The full checkpoint retains both labels at every common time. In
particular the initial raw controls satisfy

    q0=3lambda+mu+4,    r0=2lambda+3mu+3.

Their linear determinant is 2, a unit in F5. At every common time all
pairs share the trace/selected word, and its q,r restrictions are
invertible affine maps. Thus (q_n,r_n) still distinguishes all 25 pairs.
This is quite different from the original common raw port.

The balanced lift of W applied to (4) is y=(1,2,1,2). Direct integer
multiplication gives L(2,0,-3,2)=y; direct substitution in H gives
H(2,0,-3,2)=5, so H(y)=25. This particular balanced representative
does not supply a unit H(w)=1 first-work source. No claim is made here
about minimum energy among other representatives of that residue; that
is a separate arithmetic question. Gate admission alone is insufficient.

## 4. Registered one-shot family and absence

For x_lambda(0)=(lambda,0,-lambda,0,0,0), the native prefix is
g0,g2,g4 and gives

| n | x_lambda(n) | h |
|---|---|---|
| 0 | (lambda,0,-lambda,0,0,0) | (2lambda,-2lambda) |
| 1 | (0,lambda,0,-lambda,0,0) | (lambda,-lambda) |
| 2 | (2,1+lambda,2,1-lambda,1,0) | (lambda,-lambda) |
| 3 | (0,-lambda,1,3+lambda,1,1) | (-lambda,lambda) |

Thus the gate holds exactly for occupied lambda=0 at every prefix time.
On the canonical complete ready graph, let B in {2,3}, z in {1,4},
r,D in F5, and set

    u=3(B+D+1), v=3(B-D-1), q=z-3B-r,
    a=1+B+2Bz, c=-1+B-2Bz, b=u, d=v.

Then A=2B, C=4Bz and the declared payload is lambda=3-BzD.
Substitution gives

    h=(3D+4Bz,-3D-4Bz)=(3Bz*lambda,-3Bz*lambda). (6)

The selected tail actions negate B and either negate z or negate D,
preserving BzD and the graph. Equation (6) proves by induction that
the gate is equivalent to lambda=0 for every later actual time. On the
entire 100-state ready graph it selects exactly 20 states: each of
2*2*5 choices B,z,r has one D solving lambda=0. This is a graph count,
not an assertion that an actual orbit visits all 100 states.

At each fixed common time h distinguishes the five occupied lambdas.
Across all ready contexts it identifies only a sign-dependent value
of lambda because 3Bz is 1 or -1; h alone is not the stationary
canonical payload reader. The complete piston block on this graph
contains B,C,D and determines z from C=4Bz, so the lost context may
be recovered there, but this uses a different access class from the
literal receiver (b,d,q,r).

For the distinct absence x_empty(0)=(0,0,1,0,0,0), the prefix is

| n | x_empty(n) | h |
|---|---|---|
| 0 | (0,0,1,0,0,0) | (0,2) |
| 1 | (4,0,0,0,0,0) | (3,0) |
| 2 | (0,0,1,0,0,0) | (0,2) |
| 3 | (2,1,2,4,1,1) | (0,3) |

It starts in X14 with A=1,B=0,C=2,D=4. On its tail, including n=0,
write A=s in {1,-1}, C=2sz, D=4sz. Then

    h=s(1-z,1+z),       h1+h2=2s != 0.          (7)

So absence never enters the gate. Its protected sign fibre is the
original family's tail fibre (lambda,mu)=(2,4). Those raw checkpoints
carry BLANK under the registered absence reader but PRESENT(4) under
the original mixed reader. The readings have different frozen contexts;
one cannot identify their semantics merely from a shared checkpoint.

The one-shot occupied q,r histories are common to all five payloads.
The absence history is different, for example at n=2 it has (0,0)
while occupied inputs have (1,0). At n=3 both have quotient (z,q,r)
=(1,1,1), so their later q,r histories agree. This does not erase a
receiver record made from a difference before n=3.

## 5. Typed comparison diagram and equality

These stages are a comparison diagram, not an already composed physical
or mathematical transmitter. In particular the native checkpoint forks
to piston residues and to the separate retained q,r controls.

| Stage/map | Exact domain and output | Equality and limitation |
|---|---|---|
| Native U | (n,x) in N0 x F5^6 | Literal counter and ordered checkpoint. x2=x0 does not reset n. |
| Piston projection then W | F5^6 -> F5^4, x -> (b,a,d,c) | Forget q,r; W is a bijection only on the four-piston carrier. Equal residues are not equal whole checkpoints. |
| Gate h | F5^6 -> F5^2 | h(x)=0 iff W(pistons(x)) belongs to the shell image-residue set; ker(h) is its inverse image in F5^6, not that subset of F5^4 itself. The gate is a predicate, not a message decoder. |
| Balanced section ell^4 | F5^4 -> {-2,-1,0,1,2}^4 subset Z^4 | Injective chosen representative, not an additive field embedding. General lifts are ell^4(rho)+5Z^4, equal only modulo 5. |
| Integer shell | y in Z^4 with y0+2y1=y2+2y3=0 mod 5 | Equivalent to y in LZ^4, with unique preimage Vinv*y/5. Every lift of a passing residue is in the shell, and no lift of a failing residue is. |
| Raw field split | (y,sigma) in Z^4 x Z^2 -> Py+S_st sigma in Z^6 | Injective, with image the separate index-five split lattice; equality fixes both y and sigma. It is not the index-25 shell condition. |
| Integer chain input | X_N or Xhat_N | Literal equality includes all reacting/spectator tuples, raw fields, nonnegative resources, channels and pointer. A four-vector does not specify the 31-coordinate source cell or full chain preparation. |
| Retained contact controls | x -> (q,r) in F5^2 -> eta in Q^4 -> S eta in Q^D | This is a different fork from x, not a provided map from the integer chain. Equality of S eta is equivalent to equality of q,r. |
| Funded rational receiver | wave/tapes/pointer/store/ledger/direction, controlled by retained q,r | Literal occupied-state equality; H_B fixes q,r during an invocation and uses the complete wave and store guard. Ignoring controls gives a controlled family, not a closed autonomous total state. |
| Semantic reading | Each family's own fixed raw reader followed by its declared total decoder | Semantic equality is coarser than raw equality. BLANK is distinct from PRESENT(0); two different reader contracts cannot be silently identified. |

The raw split and shell equivalences, field energy relation H(Lw)=5H(w),
and full chain chronology are inherited theorems. No map is supplied by
them from a full integer chain to the rational occupied contact carrier.
Even a shell-admitted y leaves matter, static field, resources, channels,
pointer and chronology unspecified. The funded G guard also depends on
the literal reacting endpoint and available nonnegative resource.

The reset/absence obligations are different for the three families:

| Family/access | Initial/reset semantics | Stored zero and absence |
|---|---|---|
| Original global mixed chart | One common R0=R2=(2,0), exact x2=x0; outputs BLANK, PRESENT(lambda), BLANK, then PRESENT(mu) | PRESENT(0) is occupied; no extra absence preparation is supplied. |
| Original quadratic witness | Raw blanks (0,mu) vary; only decoded BLANK is common | Same six-label semantics; not common raw blank across preparations. |
| Alternative affine witness | Raw blanks (mu,0) vary; x2=x0 and common semantic BLANK | PRESENT(0) remains occupied; no extra absence preparation is supplied. |
| Registered one-shot receiver | Initially common entire receiver; BLANK at n=0,1,2 and PRESENT(lambda) for all n>=3; no common checkpoint reset is asserted | Explicit sixth preparation stays BLANK forever; occupied zero becomes PRESENT(0). |

In particular zero-gate passage is not a readiness test: occupied zero
already passes during the three BLANK prefix times. The original family
has semantic readback although it never passes the shell gate.

## 6. Scoped contact-source blindness

Let Q(x)=(z,q,r). The five selected quotient restrictions are

    (z,q,r), (-z,-q,-r), (2-z,1-q,-r),
    (2-z,1-q,1-r), (3-z,2-q,1-r).

Selection uses only z and the common native bit. Every original E starts
at Q=(2,0,1). Induction therefore gives identical Q histories and
identical selected words for every original message pair at every common
time. This recovers the inherited q,r blindness without assuming global
invertibility of the state-selected update.

The supplied rational source has no additional message access:

    eta(q,r)=(ell(q)/2,(ell(r)+1)/2,0,0), a=S eta.

The balanced scalar section is injective; S is injective because
(S v)(yi)-(S v)(y4)=v_i for i=0,...,3. Thus

    a(q,r)=a(q',r') iff (q,r)=(q',r').           (8)

For the original family this source history is identical, not merely
equal in energy or in some projected statistic. Let Y be the entire
rational receiver: both wave vectors, all four tape slots, pointer,
store, work ledger and direction; include any schedule state and chosen
fixed budget in the common initial condition. At each wave/tape step
the same deterministic map acts on equal Y. At each H_B invocation equal
Y and equal a give equal Delta, equal acceptance/refusal, equal ledger
updates and equal new Y. Induction proves equality of all receiver
histories, hence of every fixed receiver readout. This also covers an
adaptive common controller driven only by the identical receiver history;
it does not cover a controller with an extra message-dependent input.
The schedule must select the same native times and operations across
preparations. A message-dependent waiting or source-retuning rule is an
additional input and is outside this theorem.

This is a conditional deterministic noninterference theorem for the
specified port and family. It does not assert that any schedule, clock,
source access, or contact has been compiled into native U.

For the alternative family, (8) and the determinant calculation in
section 3 show that the supplied input retains both messages at each
fixed time; the original blindness premise fails there. Pair-sensitive
input does not prove funded receiver separation: H_B may refuse and the
chosen reading may discard information. For the five occupied one-shot
inputs Q is common, starting at (0,0,0), so the same noninterference
argument applies to their supplied q,r contact. Their literal native
receiver nevertheless reads lambda because it includes the memory
pistons b,d. Absence requires the separate qualification in section 4.

## 7. W as relabeling and W as a state operation

Over Z write y=(a,b,c,d) and W y=(b,a,d,c). Expanding the fixed form

    H(y)=2a^2-2ab+3b^2+c^2+d^2+2ac-ad-bc+3bd

gives exactly

    H(Wy)-H(y)=a^2-b^2+ac-bd.                  (9)

For e0 this is 1: H(e0)=2 and H(We0)=3. Thus W is not an isometry
of the fixed H marking. In a simultaneous coordinate change y=W y',
the form becomes W^T B_f W and operators become W^-1 A_f W and
W^-1 L W. That re-expression preserves the same underlying mathematics;
it does not justify acting by W while keeping the old form and shell
operator fixed. A convenient comparison map is not an admitted actuation.

## 8. Assumptions, remaining obligation, and negative conclusions

| Assumption | What it supplies | What remains outside it |
|---|---|---|
| Native generators/selector and origin counter | Literal prefix and selected X14 tail | No new access to another port or reading implementation |
| Canonical support/recurrence theorems | Complete original/alternative support and registered ready graph | No inference from finite sampling; ready graph count is not visitation |
| Chosen W and canonical field marking | Exact residue comparison and shell predicate | No energy isometry or native compilation |
| Balanced section or arbitrary coset lift | An integer representative when chosen | No least-energy selection law, complete source preparation or time intertwining |
| Integer chain law and its full preparation | Conditional resource transport and local record | No arbitrary source-content transport or rational-carrier identification |
| Fixed eta/S and retained q,r | A typed rational contact source | No extra piston-message access |
| Equal complete receiver and common schedule | The exact scoped noninterference induction | No universal no-contact or no-transmission theorem |
| Family-specific fixed readers | Their declared semantic histories | No universal identification of BLANK, absence, readiness or raw equality |

For the unchanged original family and fixed W, shell admission is false
on every admitted checkpoint. For the unchanged q,r-fed contact, the
complete receiver cannot distinguish its messages under the stated
common-input assumptions. Neither a different representative of the same
residue nor a different receiver decoder repairs these two exact
obstructions.

The least unresolved positive-interface obligation is therefore to
specify, in a separate scope, a permitted message-sensitive source-access
map on a complete declared family, together with its complete receiver
preparation, funding, timing and equality contract. It must explicitly
state which current family/access restriction changes; the frozen
original route itself is obstructed, not awaiting a better decoder.
Any intended integer-chain leg additionally needs a shell-admitted
complete preparation and a separately stated typed relation to the
rational carrier. There is no justified claim that one numerical
coincidence closes those obligations.

A possible later analytical question is whether a separately frozen
alternative-family, contact-time, funding and receiver-reading contract
can distinguish all intended messages from its already pair-sensitive
q,r input. This note neither chooses such a contract nor runs that
experiment, and does not equate it with native source loading or the
first-work construction.

Independent pre-comparison conclusions: the literal h1 clause is
REFUTED; the corrected original gate obstruction and scoped source
blindness are proved at their stated scopes; the three exact family
classifications and W distinction are above. Author-result agreement
and its final disposition remain UNASSESSED until the public proof pin
has been read back.
