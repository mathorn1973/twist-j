# A local record of work after reversal of the receiving reaction

NON-CANONICAL / candidate-T / L1.
Candidate: C-FIELD-WORK-RECORD-UNIT-N. Reservation: issue #1315.
Public authority remains Public Canon v95; this note creates no Canon claim.

For every finite N>=2 and every integer w with H(w)=1, the declared
preparation delivers two resource units at boundary N-1 and spends them on
the receiver reaction at step N. A new five-state receiver coordinate records
that accepted reaction. The original receiver cell returns to its ready state
at N+1, while the new coordinate remains readable as HIT at every boundary
N,...,N+7. This is eight consecutive boundaries, or seven elapsed macrosteps;
it is a lower bound on retention, not an asserted first reset at N+8.

The mathematical construction was supplied by the user as a known candidate
proof. This note makes its full carrier, inverse, preparation, invariants and
scope explicit. It does not claim a blind prediction or independent discovery.
The supplied report described earlier local executions, but its original ZIP
was unavailable for this work. Its reported 145800 local cases, 69 trajectories
and 1280 general states are unverified historical claims, not evidence earned
by this candidate. This proof does not depend on those counts or executions.

## 1. Exact dependencies and the inherited carrier

The base is the four-layer law and complete local arithmetic of
[PR #1310 at dd354e3e01ad7f7bb535f33e012c5ef1b46a87d2](https://github.com/mathorn1973/twist-j/blob/dd354e3e01ad7f7bb535f33e012c5ef1b46a87d2/notes/C-FIELD-THREE-CELL-DELAYED-TRANSFER-N/PROOF.md),
available at `../C-FIELD-THREE-CELL-DELAYED-TRANSFER-N/PROOF.md`.
The all-length preparation and first-delivery theorem are
[PR #1312 at 04fa72ca2506398bf47a64fe33aa024625bd4f9b](https://github.com/mathorn1973/twist-j/blob/04fa72ca2506398bf47a64fe33aa024625bd4f9b/notes/C-FIELD-FINITE-CHAIN-FIRST-DELIVERY-N/PROOF.md),
available at `../C-FIELD-FINITE-CHAIN-FIRST-DELIVERY-N/PROOF.md`.
Both remain NON-CANONICAL dependencies. Their exact integer certificates are
inputs to this conditional proof. PR #1314 is a comparison only: its extra
matter-permutation layer is absent from the law here.

Fix N>=2 and target t=N-1. The original carrier X_N consists of

```text
s=(c0,...,c(N-1),q0,...,q(N-2)),
ci=(mi,bi,zi,ri),
mi,bi in (Z^4)^3, zi=(Ei,Mi) in Z^4 x Z^2,
ri>=0, qj>=0, all resources integral.
```

Each cell has 31 stored coordinates. Its three ordered reacting registers
mi are at its actual electric vertex 0; its three spectator registers bi
are at its respective vertices 0,1,2. Cells do not share electric vertices.
The N-1 neutral channel coordinates are not electric edges or charge currents.
The base therefore has 32N-1 coordinates. Equality means literal equality of
all coordinates, including spectators, every raw-field component and old
channel contents.

For reference the exact local energies and actual charges are

```text
K=[[6,2,-1,2],[2,6,2,-1],[-1,2,6,2],[2,-1,2,6]],
C=[[1,-1],[-1,0],[0,1],[0,1]],
D=[[1,1,1,0],[-1,-1,0,-1],[0,0,-1,1]], DC=0,
Q(v)=v^t K v, chi(v)=sum_j v_j,
Hraw(E,M)=E^t E+M^t M+E^t C M,
Hcell(m,b,z,r)=sum_j Q(mj)+sum_j Q(bj)+Hraw(z)+r,
H_N(s)=sum_i Hcell(ci)+sum_j qj,
rho_i=(chi(bi0)+sum_j chi(mij),chi(bi1),chi(bi2)),
defect_i=D Ei-rho_i.
```

These are accounts on the full stored carrier. In particular a field's static
part and the spectators are never discarded. The cited certificate gives

```text
Q(v)>=||v||^2,
4Hraw(E,M)=||2E+CM||^2+M0^2+(M0+M1)^2.
```

## 2. The original total reaction and free field map

Write A_field for the active field matrix, to distinguish it from the contact
layer A. For x=(a,b,c,d), sigma=(u,v), put

```text
P(a,b,c,d)=(a-b,-a,b,b,c,d),
S(u,v)=(u,u,v,u-v,0,0),
A_field=[[1,0,1,0],[0,1,0,1],[-2,1,-1,1],[1,-3,1,-2]],
L=[[1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]],
H(a,b,c,d)=2a^2-2ab+3b^2+c^2+d^2+2ac-ad-bc+3bd.
```

The exact pinned certificates establish an injective L, the unique rational
split z=Py+S sigma, and

```text
Hraw(Py+S(u,v))=H(y)+3u^2-2uv+2v^2,
H(Lx)=5H(x), H(A_field x)=H(x),
L A_field=A_field L, A_field^5=I,
y=(a,b,c,d) in L Z^4 iff a+2b=0 mod5 and c+2d=0 mod5.
```

The split is admitted only if all its coordinates are integers. All division
and image tests are exact; the definition permits no rounding.

Let Z4 denote the zero vector in Z^4, and set

```text
R=((1,-2,1,0),Z4,Z4),
AM=((1,0,0,0),(0,-1,0,0),(0,-1,1,0)),
ZM=(Z4,Z4,Z4).
```

Their matter energies are 18,20,0. R and AM have the same reacting-vector
sum (1,-2,1,0), of total charge zero; individual register charges need not
be equal. All three registers are at the same actual vertex. ZM is neither
reaction endpoint. No permuted triple is silently identified with an endpoint.

For integer x,sigma and arbitrary spectators b, the original complete gate is

```text
G(R,b,PLx+S sigma,r)=(AM,b,Px+S sigma,r+4H(x)-2)
    if r+4H(x)-2>=0;
G(AM,b,Px+S sigma,r)=(R,b,PLx+S sigma,r+2-4H(x))
    if r+2-4H(x)>=0.
```

Every other complete input is fixed. In particular failed matter recognition,
nonintegral split, R-side image failure and insufficient funding cause no
partial update. The disjoint complete accepted pairs are transpositions, so
G^2=I on the full carrier, including rejections. The energy identity is

```text
18+5H(x)+r = 20+H(x)+(r+4H(x)-2).
```

Both spectators and the static field remain on both sides. G preserves the
reacting-vector sum, each actual node charge, DE and each Gauss defect.

The original local free map and inverse are

```text
F(m,b,z,r)=(m,b,T_field z,r),
T_field(E,M)=(E+CM,M-C^t(E+CM)),
T_field^-1(E',M')=((I-CC^t)E'-CM',M'+C^t E').
```

They are integer bijections, preserve Hraw and DE, and obey
T_field P=P A_field and T_field S=S. These identities also explain why a
zero active field remains zero when a retained static field is present.

## 3. One stored pointer and its total reversible writer

The new carrier is

```text
Xhat_N=X_N x C_5, C_5=Z/5Z,
shat=(s,p), p in {0,1,2,3,4}.
```

The pointer is stored at the target only. The target block has 32 coordinates,
the other cell blocks have 31, and the N-1 channels remain present. The total
is 32N, of which one coordinate is restricted to the five-element carrier.
There is no additional stored branch bit, controller, clock or unbounded log.

Define the accepted R-side predicate on the full local input by

```text
e(c)=1 if matter(c)=R and matter(Gc)=AM, otherwise 0.
```

Equivalently, e(c)=1 exactly when c has literal matter R, an integral split
z=Py+S sigma, admitted y=Lx with integer x, and r+4H(x)-2>=0.
It tests the actually accepted reaction, not just R, AM, field energy or the
presence of resource. It is a local function of the current complete input.

At the target replace G by

```text
Ghat_t(c,p)=(Gc,p+e(c) mod5).
```

Every other primitive fixes p. On arbitrary output (c',p') define

```text
Ghat_t^-1(c',p')=(Gc',p'-e(Gc') mod5).
```

**Lemma 1: total local bijection.** Substituting c'=Gc gives Gc'=c and
e(Gc')=e(c), so Ghat_t^-1 Ghat_t(c,p)=(c,p). Conversely, start from
(c',p'), put c=Gc', and apply Ghat_t to (c,p'-e(c)); Gc=c' and the
pointer sum returns p'. Thus both inverse identities hold on the full
carrier, for every p and every rejected or accepted input. No external record
of the accepted branch is needed: the inverse recovers its input using G.

Ghat_t is not an involution. On each accepted pair c_R,c_A with respective
matter R,AM, its orbit is

```text
(c_R,p) -> (c_A,p+1) -> (c_R,p+1) -> ... -> (c_R,p+5)=(c_R,p).
```

The exact local orbit length is ten, since matter alternates and a return at
an even length 2a requires a=0 mod5. Rejected c is fixed, with its old p
retained. In particular the forward AM-to-R branch of Ghat_t does not undo
the earlier pointer increment. The mathematical inverse subtracts instead.

## 4. The four layers, full inverse and base projection

For j=0,...,N-2 retain the original contacts

```text
A_j=swap(rj,qj), B_j=swap(qj,r(j+1)).
```

They exchange entire nonnegative contents even when both sides are occupied.
Let Ghat apply G_i to every i<t and Ghat_t to the target, A apply all A_j,
B apply all B_j, and F apply all F_i. The chronology is exactly

```text
Ghat; A; B; F,
That_N=F B A Ghat,
That_N^-1=Ghat^-1 A B F^-1,
inverse chronology: F^-1; B; A; Ghat^-1.
```

Composition acts from right to left in the formulas. The supports within
each layer are disjoint. Ghat^-1 uses G at the other cells and the target
inverse of Lemma 1. Adjacent inverse factors cancel in either product;
no commutation of a reaction with a contact is assumed. In particular using
the forward Ghat as the inverse reaction layer would be wrong.

The original four-layer law is T_N=F B A G. For pi(s,p)=s, each extended
primitive projects exactly to its original primitive, and therefore

```text
pi That_N=T_N pi,
pi That_N^k=T_N^k pi for every integer k.
```

The inverse identity follows from the same primitive projection. This is a
statement on all complete states, not just the positive witness. It preserves
the entire original evolution, including the future evolution after the
first receiver reaction. The new register cannot affect financing, transport,
field phase or any original coordinate.

For a fixed cut j, replace both A_j and B_j by identities at every step;
keep the old q_j stored and fixed. The same bijection and projection statements
hold with the corresponding original cut law. Deletion is not a temporary
time-dependent switch or an erasure of q_j.

The write is part of the declared target reaction primitive. Thus the number
of macro-layers remains four, independently of N. This algebraic accounting
does not claim an unchanged physical implementation cost for the enlarged
local gate or an implemented microscopic layer controller.

## 5. Fixed local reading and the general retention lemma

Use exactly the reader

```text
O:C_5->{BLANK,HIT},
O(p)=BLANK if p=0, otherwise HIT.
```

Its sole input is the current stored target coordinate. It takes no N, time,
source state, trajectory or historical snapshot. The two labels are a defined
L1 state classification; transmission into a physical reading apparatus is
not constructed here.

**Lemma 2: eight-boundary retention.** Start with p=0 on any complete
state. Suppose the first accepted target R-to-AM transition occurs in
forward step j. Then O(p_k)=HIT for all k=j,...,j+7, and O(p_k)=BLANK
at all earlier complete boundaries k<j.

**Proof.** Before step j there is no pointer increment. In step j it becomes
1. After any increment the target matter is AM. No subsequent contact or
free-field operation changes matter, and only one target G is evaluated per
complete step. A later accepted R-to-AM therefore requires at least one
intervening step with an accepted AM-to-R; rejections can only delay it.
Consecutive increments are separated by at least two macrosteps. If n_k
denotes the number of accepted target R-to-AM transitions up to boundary k,
then p_k=n_k mod5, and for 0<=ell<=7,

```text
1<=n_(j+ell)<=1+floor(ell/2)<=4.
```

All these residues are nonzero. The fifth increment, the first one that could
restore p=0, cannot occur before j+8. This proves the lemma. The count n_k
is a proof device; no unbounded counter is added to the automaton. Only its
residue p is stored.

The lemma does not assert that a fifth event actually occurs at j+8, or that
this earliest possible time is attained by the chain preparation below.
Its guarantee covers eight boundaries spanning seven elapsed steps. Arbitrary
preloaded p is outside the ready-state guarantee: for example p=4 would become
0 at the next accepted event. Applying the mathematical inverse can also undo
a recent write immediately; the stated retention is for the fixed forward law.

## 6. All finite lengths: arrival, work, local reversal and retained record

Fix any integer w with H(w)=1 and prepare the entire state by

```text
c0(0)=(R,0,PLw,0),
ci(0)=(ZM,0,0,0) for 1<=i<=N-2,
ct(0)=(R,0,0,0), qj(0)=0 for every channel, p0=0.
```

Zeros denote every component of the relevant full tuple. All spectators,
all intermediate and target fields, and all cell and channel resources are
zero. The total original energy is 23+18=41. The empty intermediate range
for N=2 is allowed without changing the chronology.

For completeness the length induction uses the following exact contact map.
Write rhat_i for resources just after G and q_j for the incoming channels:

```text
r'_0=q0,
r'_i=rhat_(i-1) for 1<=i<=N-1,
q'_j=q_(j+1) for 0<=j<=N-3,
q'_(N-2)=rhat_(N-1).
```

The q'_j middle range is empty when N=2. F and the pointer write do not
change these coordinates. The map is a permutation of the resources after
the reactions, rather than an assumption that old channels were empty.

In step 1 the source's admitted h=1 reaction produces AM, field Pw and
resource 2. All other reactions reject: ZM is off-endpoint and the ready
target R with zero active field cannot pay 2. Contacts place the resource
in r1. F changes the source field to P A_field w. At every boundary
1<=k<=N-1, induction now gives the complete base state:

```text
source matter AM, source field P A_field^k w, source resource 0;
intermediate matter ZM, target matter R;
all other fields and all spectators zero;
ri=2 exactly when i=k and otherwise zero; all channels zero.
```

For the induction step k<N-1 the resource is in an intermediate cell with
matter ZM, which does not react. The source remains AM with active energy 1
and resource 0, so its reverse would produce -2 and rejects. The target
still lacks funding. Contacts therefore advance the two units to r_(k+1),
and F advances only the source field phase. This also shows that any repeat
of that field phase has no bearing on funding or the proof.

Thus the first positive target resource is at boundary N-1; its target G
was evaluated before those contacts and the target is still R. In step N,
the target's h=0 branch spends exactly two units and gives AM with resource
0. The new predicate e is 1, so the pointer becomes 1. All base resources
and channels are now zero. These are exact first times:

```text
t_delivery=N-1,
t_target_reaction=t_first_HIT=N.
```

At the next target G, in step N+1, the input AM has zero active field and
resource 0. Its reverse produces R and resource 2. It contributes e=0 and
leaves p=1. A does not touch the last cell resource; B moves those two units
into the old empty last channel. Hence the full boundary state at N+1 has

```text
source matter AM, source field P A_field^(N+1) w;
all intermediate matter ZM, target cell ct=(R,0,0,0);
all spectators and other fields zero; all cell resources zero;
q_(N-2)=2 and all other channels zero; p=1.
```

The source reverse still rejects during this step, since that released
resource has not yet returned to it. This also covers N=2. The old target
cell is literally its initial 31-coordinate tuple at N+1. Its new complete
32-coordinate block is distinguishable from readiness by p=1.

Lemma 2 with j=N proves HIT at all boundaries N,...,N+7 for every N and w
in this preparation. No closed formula for the old coordinates beyond N+1
is asserted here; their exact continuation is T_N by projection. Later source
reactions or returning resources cannot invalidate the event-spacing lemma.

## 7. Equal-energy offimage source and all individual cuts

For the offimage control replace only the initial source's active coordinate
Lw by

```text
y_minus=(0,0,1,-2).
```

It has H(y_minus)=5, equal to H(Lw), but c+2d=-3 is nonzero modulo 5,
so y_minus is outside L Z^4. The integer automorphism A_field commutes with
L. It carries L Z^4 onto itself: A_field L=L A_field and its integer
inverse gives the converse inclusion. It consequently preserves the complement
as well. At every future source opportunity A_field^k y_minus still fails
image admission, while its source matter remains R. The source never releases
resource. All resources elsewhere stay zero under the contacts, every passive
intermediate remains fixed, and the target's R branch stays unfunded. Thus
there is no target event and p_k=0 for every k>=0. The source field may
evolve; rejection is not being mistaken for a fixed complete source state.

Now take the positive preparation and any one fixed cut j in 0,...,N-2.
The downstream component consists of cells j+1,...,N-1 and their internal
channels q_(j+1),...,q_(N-2), together with p at the target. Its complete
initial state contains only ZM intermediate matter, ready R target matter,
zero fields, spectators, resources, channels and p. No remaining contact
connects that component to the source side or to stored q_j.

Every primitive fixes this prepared downstream state: ZM rejects, target R
cannot pay its h=0 cost, e=0, contacts exchange zeros and F fixes zero fields.
Induction over primitives proves that the component stays exactly fixed for
all future steps. In particular its target stays (R,0,0,0;p=0) and reads
BLANK for every k>=0. This includes the sole cut when N=2 and the empty
internal-channel range when j=N-2. It does not require a finite-time search.

Both controls use the same declared ready receiver and p=0. For arbitrary
excited initial states, a preloaded target resource can finance an event
without source delivery. The pointer certifies a local accepted reaction in
its own trajectory; it does not independently certify the energy's origin.
BLANK also does not distinguish the offimage source from a disconnected path.

## 8. Complete energy, invariants, locality and recurrence

Assign every pointer value the same chosen energy and zero charge:

```text
E_p(p)=1 for every p in C_5,
Hhat_N(s,p)=H_N(s)+1.
```

Each original primitive preserves H_N; incrementing or decrementing p
preserves E_p. Therefore every new primitive, layer boundary, complete step
and inverse preserves Hhat_N. Each also preserves all original spectators,
every reacting-vector sum, every actual charge and every Gauss-defect entry.
The pointer introduces no electric vertex, flux or charge. These conclusions
hold on the complete carrier even when initial Gauss defects are nonzero,
and after any fixed cut. Every resource remains nonnegative.

For the positive and offimage neutral preparations Hhat_N=42. During the
positive transfer the account is source 21, ready target 18, moving resource
2 and pointer 1. Upon delivery it is 21+(18+2)+1. After the paid reaction
it is 21+20+1; following the local reversal it is 21+18+2+1, with the
resource in the last channel. The pointer's prepared unit neither supplies
nor replaces either of the two units spent by the target reaction.

For any retained static-field and spectator preparation, their exact original
energy is still included. In particular the original charged three-cell
witness of #1310 has original energy 253 and extended energy 254; the
projection and retention lemmas apply unchanged whenever its first event is
at step 3. This is the same existing charged witness, not a new physical
energy identification.

The target writer reads and modifies only the target block. On the contact
graph C0--Q0--C1--...--Q(N-2)--C(N-1), Ghat and F have radius 0 and
A,B are nearest-neighbour matchings. One forward or inverse macrostep has
dependency radius at most two edges, as in #1310. Adding p inside the last
cell does not add a remote dependency. This says nothing about an
implementation along individual electric edges or a measured physical speed.

For fixed finite N and Hhat_N=E, the original coordinates lie on the finite
shell H_N=E-1. The positive forms and the displayed square identity bound
all original integer coordinates, and nonnegative resources are bounded by
E-1. There are exactly five available pointer values per original state.
Consequently each extended shell is finite. The conserved-energy bijection
restricts to a permutation of it; every orbit is periodic from its initial
state, without a transient. This applies to each fixed cut law too. No common
period across lengths is claimed, and the active field's period alone does
not determine the period of the complete machine.

At the fifth accumulated accepted event the pointer returns to BLANK. The
finite cyclic record therefore cannot be permanent on a positive periodic
orbit. A map that sets all five p values to 0 while fixing every other
coordinate is not injective, hence is not an admissible reset of the full
machine. Any separate reset protocol must account for where the discarded
distinction goes. No such reusable reset or disturbance protection is supplied.

## 9. Result and limits of the conditional model

The declared finite automaton connects a prepared source, transport of two
resource units, their local use and a stored locally readable record of that
accepted use. The extension preserves the full original dynamics in projection
and has an explicit total inverse. The new record survives the original
receiver's immediate local reversal and is guaranteed for eight boundaries.
All lengths, admissible H(w)=1 seeds and individual cuts are covered by proof.
Any separately pinned finite audit checks implementation against this proof;
it cannot substitute for the quantified induction or earn a stronger scope.

The five-state degeneracy with assigned energy 1, neutral pointer, accepted
reaction control, ordered path and four-layer schedule are explicit model
choices. Adding a stored coordinate and enlarging a local gate is a resource
and architecture change even though pointer writes have zero energy difference
under this definition. The value 1 is a prepared model account; it does not
derive the physical cost of controlling or realizing five distinct degenerate
states. No claim of a minimal pointer, minimal energy cost or optimal retention
is made.

This is an L1 conditional automaton construction, not a selection of its law
from J, a lift to physical apparatus semantics, native-U compatibility, a
laboratory realization or an identification of the model's units with joules.
It does not implement a measured external readout, infinite storage, robust
memory or a renewable record protocol. The status remains NON-CANONICAL,
candidate-T, L1; public authority remains Public Canon v95.
