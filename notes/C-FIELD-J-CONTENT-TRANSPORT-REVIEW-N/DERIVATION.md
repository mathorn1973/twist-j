# Independent derivation of packet transfer and finite record retention

**PUBLIC, NON-CANONICAL. Prospective independent L1 derivation; unexecuted.**
Inputs, exposure and finite audit bounds are fixed in PREREG.md. Throughout,
T means 2N-1 and M means 1226. This is a selected law with identity field
transport, not the old field chain or native U.

## 1. Complete coordinates, energy and the content reader

Use alternating path slots indexed 0,...,2N-2, with C_i at 2i and Q_j at
2j+1. The state consists of 2N-1 packets (b,y,r), together with receiver
latch l and record p. Each packet has six integer coordinates, giving
6(2N-1)+2=12N-4 stored coordinates. Their stated finite/discrete domains and
literal order are part of equality; no other memory is present.

Substitute the given integral inverse chart a=C^-1 y into H. With
x=(a2,a0,a3,a1), the result is

    H(Ca)=sum_i a_i^2-a0*a2-a0*a3-a1*a3
          =(x0^2+(x0-x1)^2+(x1-x2)^2+(x2-x3)^2+x3^2)/2.

This equality can be verified in its ten quadratic coefficients, and both
chart products are identity. Thus H is positive definite and its zero is
exactly zero. Bounded H bounds every coefficient, hence every field. More
sharply the admitted inverse path-Gram diagonal (6,4,4,6)/5 gives
a0^2,a3^2<=12H/5 and a1^2,a2^2<=8H/5. Therefore every integral H<=5 field
lies in the complete 1225-element coefficient box in the specification.

Let d=(a0+3,a1+2,a2+2,a3+3). Successive Horner bases (5,5,7) map that
box bijectively to integers 0,...,1224; adding one gives 1,...,1225.
Repeated Euclidean divisions by 7,5,5 recover its unique four digits.
Reconstruction followed by H<=5 is therefore a total image recognizer
on every admitted modular record. Zero alone denotes BLANK. A supported
zero field receives code 613, which is nonzero. A nonzero supported code
can never masquerade as blank on the first write into p=0.

The packet reader requires presence before the energy guard. Hence b=0
with arbitrary stored field/reserve reports ABSENT, while b=1,y=0 reports
VALUE. ABSENT describes that reader's observation, not erasure of the
packet's other coordinates. The record reader depends only on p and the
fixed code, with no time/source/N arguments. Derived E5 is computed from
the recovered coefficient/field; it is not extra transmitted data.

For ell=(1,-1,-1,1) and jell=(-1,0,-2,-2), the quadratic gives H=5 in both
cases. The fixed LOW formula s^2/[4(5Q-s^2)] gives 0 and 5/16, respectively,
using (Q,s)=(4,0),(9,-5). Their codes differ by box injectivity. This is a
comparison of two literal classical vectors in a declared context.

## 2. The complete receiver permutation

Fix supported (b,y) and its code c. The local conserved integer is
q=r+2l. If q<2 the only admissible latch is l=0, and G fixes the state.
If q>=2 there are exactly two resource/latch configurations,

    A_q=(r=q,l=0), B_q=(r=q-2,l=1).

For every p the forward rule is

    (A_q,p) -> (B_q,p+c), (B_q,p) -> (A_q,p).

Thus it is a permutation, with inverse (B_q,p)->(A_q,p-c) and
(A_q,p)->(B_q,p). This proves both compositions on every admitted local
state and explains why G is generally not an involution. The q<2 fixed
states cannot collide with these q>=2 orbits. Unsupported (b,y) states
are fixed separately, and support never changes; so all branch images
are disjoint and exhaustive. This includes arbitrary p, huge reserves,
inactive nonzero contents and arbitrary initial latch.

G changes neither b nor y and preserves q. Its energy change is exactly
Delta r+2 Delta l=0; the p register has constant assigned energy. No
unlisted resource is discarded. The accepted event predicate is exactly
supported, l=0, r>=2 on the input. Both funding and code therefore come
from that one received packet. A forward release does not subtract c;
only the inverse of an accepted write does.

## 3. Whole-state inverse, accounts, locality and cuts

A exchanges slots (2j,2j+1); B exchanges (2j+1,2j+2). Each layer's pairs
are disjoint. Each exchange retains the entire two old packets, regardless
of equality, presence, support or occupation. It is an involution. Since
forward chronological order is G,A,B, the inverse order is B,A,G^-1.
Composition of the proved permutations gives both full inverse identities
without any restriction to a clean preparation.

G and swaps separately preserve the multiset of (b,y), sum r+2l, and
sum(b+H(y)+r)+2l+1. Therefore so do both full directions. Positivity of H,
nonnegativity of the other variable terms and finiteness of b,l,p imply
every bounded energy set is finite. A permutation preserving such a set
has every orbit periodic from its initial state; this makes no uniform
period claim for arbitrary dirty states.

Treat packet plus the two receiver auxiliaries as one block at Ct. G and
G^-1 act on that block only; each matching crosses one neighboring edge.
Following dependence backwards through three layers proves radius at most
two path edges for each full direction. This is a property of the declared
block topology and depth, not a dimensional physical velocity.

A cut omits both pairs involving Q_j. All remaining swaps are still
involutions; all foregoing proofs apply. Q_j is fixed in its entirety.
Removing those two incident edges separates left cells C0,...,Cj from
right cells C(j+1),...,Ct. The clean right component is entirely empty,
so swaps and unsupported receiver G fix it at each layer. This induction
proves receiver E and l=p=0 forever, including j=0, j=N-2 and N=2.
Dirty right components can react and have no source-provenance guarantee.

## 4. All-N transport and event timing

Away from G, compute BA on a slot label. For i<t, C_i first goes to Q_i
then C_(i+1). Ct is fixed by A then goes to Q_(t-1). For j>=1, Q_j goes
to C_j then Q_(j-1). Q0 goes to C0 and stays there under B. These cases
partition every slot even when N=2, and give the single length-T cycle

    C0,C1,...,Ct,Q_(t-1),...,Q0.

G never changes packet presence/content or position. The clean preparation
has exactly one presence-marked packet; all other packets remain E under
the swaps and G. Consequently its position at boundary n is the nth
cycle position, independently of y and resource/latch state. Its first
receiver boundary is t=N-1, and G sees it in steps N+hT, h>=0.

Before the first visit, packet reserve is two and latch zero. At a visit
with that pair, the write yields reserve zero and latch one; at the next
visit the release restores reserve two and latch zero. At every intervening
step the receiver packet is E, hence unsupported, and neither auxiliary
changes. Induction on h establishes the pair alternation and

    W_m=N+2mT, R_m=N+(2m+1)T.

For macro-boundary n the number of completed writes is

    w(n)=0 for n<N; otherwise 1+floor((n-N)/(2T)).

For any initial p0, p(n)=p0+w(n)c mod M. This formula follows by induction
on actual reaction times, not by fitting a finite trajectory. Content is
literally y at first receiver arrival. At boundary N the packet has entered
Q_(t-1), but the receiver-local record is c and decodes that same y.

Latch one lasts at boundaries W_m,...,R_m-1, exactly T boundaries. The
first record remains c at N,...,N+2T-1, exactly 2T boundaries and 2T-1
elapsed steps. At the next write it becomes 2c, different from c since
0<c<M. Later repeated sums can be BLANK, INVALID or a different VALUE.
Their label alone carries neither source provenance nor latest-event truth.
For example p0=-c gives BLANK after the first accepted write.

## 5. Operative return and exact complete period

At boundary 2kT the marked packet is back at C0, it has undergone exactly
2k receiver visits, reserve is two and latch zero. Every other packet is
E, and p=p0+kc. Thus the first operative return at 2T retains p=c for
p0=0; it is not full blank reset. The earliest complete return must be a
multiple hT because the sole b=1 packet distinguishes every cycle position.
At hT the number of previous receiver visits is exactly h, so odd h leaves
latch one/reserve zero. Thus h=2k, and complete equality further requires
kc=0 modulo M. Its least positive solution is M/gcd(M,c). The exact clean
period is therefore 2T M/gcd(M,c), including stored zero. This proves both
the claimed return and absence of any earlier one.

## 6. Interventions and boundaries

All-empty preparation is fixed. Supported r=0 or 1 with latch zero never
passes funding: swaps preserve that reserve, so the packet circulates while
G stays fixed forever. Unsupported b=1 packets and all b=0 packets are
fixed by G regardless of stored energy. These statements induct over each
actual layer and do not discard inactive energy.

In the mismatch preparation, the supported packet has r=0 forever and the
other packet has b=0,r=2 forever. Swaps never merge packets. Neither can
trigger a write, latch stays zero and no release creates funding. Their
energy equals the clean funded trial but their event behavior differs.
Replacing the content of a funded preparation changes the arriving literal
content and first code; an unsupported replacement removes all reactions.

A funded supported packet preloaded at Ct instead writes in step one.
A supported packet at Ct with l=1 releases two units and retains p. These
follow directly from the actual local branches and require no packet ever
to have originated at C0. Dirty occupied channels retain whole-state
bijectivity/accounts, but have no clean-trial arrival or provenance theorem.

The proof establishes only a selected classical construction. Its support,
weight, latch, code, record degeneracy and scheduling are explicit choices.
It supplies no coherent Gram-preserving transfer, QDD instrument/Born event
law, native-U/J selection, physical realization, infinite fresh archive or
physical-parent closure. Finite audits and static author comparison remain
pending at the independent freeze.
