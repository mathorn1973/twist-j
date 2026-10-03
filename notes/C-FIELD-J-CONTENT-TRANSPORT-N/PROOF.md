# A selected conservative classical packet and local record law

**NON-CANONICAL, L1, prospective candidate-T.** The complete contract is
PREREG.md. Independent review and scientific execution are pending. The
accepted Stage-A inputs remain candidate-level; the earlier failed Python
contract remains rejected at its original pin. This construction selects a
new law and does not claim a projection to native U or to the v96 chain.

## 1. Content chart, positivity and fixed finite code

For y in Z^4 use

```text
H(y)=2y0^2-2y0*y1+3y1^2+y2^2+y3^2
     +2y0*y2-y0*y3-y1*y2+3y1*y3,
a=C^-1 y=(2y0-2y1+y2-y3,y0,y0-y1-y3,y0-2y1-y3),
C a=(a1,a2-a3,a0-a1-a3,a1-2a2+a3).
```

Substituting either chart in the other returns the four coordinates. Thus
this is an integral bijection. Substitution into H gives

```text
H(Ca)=sum a_i^2-a0*a2-a0*a3-a1*a3,
2H(Ca)=a2^2+(a2-a0)^2+(a0-a3)^2+(a3-a1)^2+a1^2.
```

The last sum vanishes only at zero, proving positivity. The Gram inverse
diagonal in the original coefficient order is (6,4,4,6)/5; it follows either
by direct multiplication of the A4 path Cartan inverse or from the accepted
Stage-A proof. Metric Cauchy-Schwarz gives a0^2,a3^2<=12H/5 and
a1^2,a2^2<=8H/5. Hence H<=5 lies in
B=[-3,3]x[-2,2]x[-2,2]x[-3,3], independently of enumeration.

Shift by (3,2,2,3). The resulting digits have radices (7,5,5,7), and

```text
c(y)=1+(((a0+3)*5+(a1+2))*5+(a2+2))*7+(a3+3)
```

is one plus their position index. Repeated Euclidean division by 7,5,5,7
uniquely recovers the shifted digits from any index 0,...,1224. Therefore
c is a bijection B -> {1,...,1225}; its restriction to K5 is injective and
never zero modulo M=1226. Every nonzero p in this residue ring first gives
one point of B. The record decoder accepts it exactly when H(Ca)<=5.
It returns BLANK at p=0 and INVALID at every other non-image code. The
finite census of 291 K5 elements is exposed from Stage A; it is not used
to prove this inverse or choose the containing box.

For a supported field the scalar is alpha=sum a_i j^i, with
1+j+j^2+j^3+j^4=0. The accepted identities give

```text
e0=H(y)=sum a_i^2-a0*a2-a0*a3-a1*a3,
e1=H((I+A_f^2)y)=sum a_i^2-a0*a1-a1*a2-a2*a3.
```

These energies and a mod5 are available as derived mathematical data from
the recovered a,y. They are not measurements performed by the selected
transport law. In particular I+A_f^2 is not its free step: this law has no
free evolution of packet y. Its transport action on content is identity.

## 2. Complete carrier and receiver branch bijection

Fix N>=2. Each of N cell and N-1 channel slots stores P=(b,y,r), with
b in {0,1}, y in Z^4 and r>=0. Inactive b=0 does not erase y or r.
The receiver cell Ct, t=N-1, additionally stores l in {0,1} and p in Z/MZ.
All coordinates and ordered slots participate in state equality. This is
12N-4 integer coordinates; there is no history, branch bit or clock.

A packet is supported exactly when b=1 and H(y)<=5. Receiver G fixes every
unsupported packet and l,p. On a supported packet it fixes b,y and acts by

```text
(r,0,p), r>=2 -> (r-2,1,p+c(y));
(r,0,p), r<2  -> (r,0,p);
(r,1,p)       -> (r+2,0,p),
```

with record arithmetic modulo M. The first branch is the accepted write;
the last is the release. These names describe actual branches, not extra
stored controls. All other packets and registers are untouched.

Because support and c(y) are unchanged, the inverse image of every supported
output is determined by its latch and reserve:

```text
(r,1,p)       <- (r+2,0,p-c(y));
(r,0,p), r>=2 <- (r-2,1,p);
(r,0,p), r<2  <- (r,0,p).
```

Unsupported outputs have themselves as preimage. Output latch one comes
only from a funded write, output latch zero with r>=2 only from release,
and supported latch zero with r<2 only from rejection. These disjoint
classes cover the local carrier. Substitution verifies both compositions,
including arbitrary p, and every restored reserve is nonnegative.

The forward release does not subtract c; G is consequently not an involution.
The mathematical inverse of a write does subtract c. Recovering the input
requires only the current receiver packet and registers, not a past log.
For fixed received content, p->p+c is a permutation, so an old record is
not overwritten by a noninjective assignment. Its semantic meaning may
nevertheless change; invertibility is not unbounded archival capacity.

## 3. Full energy, content accounts, contacts, cuts and recurrence

Give a packet energy b+H(y)+r, latch energy 2l and each of the M record
states energy one. Thus

```text
E(s)=sum_all_slots [b+H(y)+r]+2l+1.
```

Every field, including inactive and channel fields, is counted. This is
positive on the complete carrier. A write moves two energy units from its
own packet reserve to the latch; a release moves them back into the present
supported packet. Neither changes b,y, and the modular record has constant
energy. Rejection is identity. Therefore every local branch and its inverse
preserve E, the multiset of all (b,y), and sum r+2l. A dirty release can
fund a different packet than an earlier write; the full account allows
this and makes no provenance claim.

Let A_j swap whole packets C_j,Q_j and B_j swap Q_j,C_(j+1). Old data are
retained even if both slots are occupied. Each map is an involution and
preserves every stated account. Each set of contacts is a disjoint matching.
The forward law is T_N=B A G (chronology G;A;B), and the inverse is
G^-1 A B (chronology B;A;G^-1). Adjacent inverse factors cancel in both
compositions without any commutation assertion about G and contacts.

For a fixed cut j omit A_j and B_j in both directions. The remaining
operations have the same proofs, and Q_j is now fixed with all its old
packet content. The cut parameter is fixed for the law, not chosen by a
state-dependent decoder. Local G uses the receiver block only, while each
contact spans one edge of the declared stored-block path. Hence depth is
three and dependence radius at most two path edges in either direction.
This includes occupied and rejected states. There is no unclaimed physical
speed or electric-edge interpretation of these blocks.

At fixed N,E each reserve is bounded by E-1. The positive quadratic and
the coefficient bounds in section 1 bound every coefficient, hence every
y. Presence, latch and record have finite ranges, and there are finitely
many slots. Thus each energy shell is finite. The complete bijection with
or without a fixed cut restricts to a permutation of that shell. Every
orbit is periodic from its initial state. This supplies no uniform period
over arbitrary dirty states, energies or N.

## 4. Clean transfer and its entire future history

Prepare exactly one packet P=(1,y,2) in C0, for any y in K5; every other
slot is E=(0,0,0), and l=p=0. The receiver preparation is common to all
sources. Energy is H(y)+4. The content/presence multiset has one marked
present packet even when y=0, so its position remains distinguishable from
every empty slot. G changes neither its position nor y; unsupported empty
packets always reject. The marked packet is therefore the only possible
participant in receiver G.

Direct application of A then B gives the single slot cycle

```text
C0 -> C1 -> ... -> Ct -> Q(N-2) -> ... -> Q0 -> C0,
```

of length T=2N-1. In particular the packet first occupies Ct at boundary
N-1. The G of step N-1 has already occurred before that arrival. At step N
the receiver sees the packet with reserve two and latch zero, so it writes
c=c(y), consumes precisely two units and becomes latch one. Contacts then
move the packet into Q(N-2). At boundary N the retained local record still
decodes y, despite the now-empty receiver packet slot. First arrival and
first funded write are therefore exactly N-1 and N for every N>=2.

After each such receiver visit the marked packet returns exactly T steps
later. During its absence the receiver holds empty packets and G is identity.
No other reserve is ever created. At the next visit its reserve is zero
and the latch is one, so release restores reserve two and latch zero,
retaining p. The following visit writes again. Induction on visits proves

```text
write steps W_m=N+2mT,
release steps R_m=N+(2m+1)T,              m>=0.
```

This includes every intermediate rejection and every later resource return;
no first-pass pattern is silently assumed forever. At a macro-boundary n,
the number of completed receiver reactions is

```text
e(n)=0 if n<N, otherwise 1+floor((n-N)/T).
```

It follows that l(n)=e(n) mod2, the marked packet reserve is 2(1-l(n)),
and every other reserve is zero. The number of writes is
w(n)=0 for n<N and 1+floor((n-N)/(2T)) otherwise. Thus
p(n)=w(n)c mod M. The packet position is the n-th point of the slot cycle.
These formulas define the complete state at every boundary. At the actual
G substep of step n they already give the new latch/reserve/record, while
the packet remains at its boundary n-1 position; A and B then perform the
two stated matching moves. This also determines every substep state.

The packet-snapshot reader at arrival uses only the receiver packet and
returns its literal y and chart a. The record reader at boundary N uses
only p=c, so the position-code inverse returns exactly the same y. Both
maps are injective on K5. N and launch time are proof parameters, not
hidden inputs to either reader. The physical opportunity to choose or
observe a read time is not supplied by this mathematical theorem.

## 5. Record lifetime, dirty pointers and precise renewal

At W_m the latch rises to one and stays one through boundary R_m-1;
that is exactly T boundaries. The record register is unchanged at release
and at every contact, so the first p=c persists through boundaries
N,...,N+2T-1, exactly 2T boundaries spanning 2T-1 elapsed steps. At the next
write p becomes 2c. Since c is nonzero modulo M, 2c differs from c; the
first exact record value's lifetime ends there. This is a p-only guarantee,
not a requirement that latch one persist for the entire read interval.

Later p=w c may be blank, an invalid code or another valid code. There is
no general interpretation as a last-event record. For arbitrary initial
p0 in the same clean packet/latch preparation, the complete derivation is
unchanged except p(n)=p0+w(n)c. Taking p0=-c makes the first accepted write
blank. Thus event occurrence, nonblank record and source provenance are
different statements; a clean initial record is an explicit premise of
the first-trial readback.

After T steps the packet has returned to C0 but the latch is one and its
reserve zero. After 2T steps it is in C0 with reserve two and latch zero;
all other packets are E and p=c. Thus the operative state excluding p has
returned exactly, while the first record is still retained. Repetition gives
the operative initial state at 2kT with p=k c mod M. A complete return must
first return the presence-marked packet position, requiring a multiple of T.
An odd multiple has the wrong latch/reserve, so it must be a multiple of 2T.
The first positive k with k c=0 mod M is M/gcd(M,c). Hence the exact least
full-state period of this clean family is

```text
2T * M/gcd(M,c).
```

This is finite recurrence. The model has one finite record, not fresh
independent archive cells at each cycle. Operative renewal at 2T is not
blank renewal; no externally supplied erase, new-source loading, archival
transfer or resource replacement is included. Those would be additional
operations with their own accounts. The inverse law can undo prior writes.

## 6. Controls and causal content/funding dependence

Absence with all packets E,l=p=0 is fixed by every primitive. A present
zero field has coefficient tuple zero and c=613, so it is a supported,
nonblank first record. These two preparations remain distinct.

For a lone supported packet with reserve zero or one and initial l=0, every
receiver encounter fails funding. Therefore the latch and record remain
zero forever while the literal packet continues around the cycle. A lone
unsupported field H>5, or any lone inactive packet b=0, fails support at
every encounter, again leaving l=p=0. Stored inactive content and reserves
are not discarded: they still circulate and contribute to energy.

For each fixed cut the prepared right component starts with empty packets,
l=p=0. Its surviving contacts swap empties and G rejects. No remaining
contact joins it to the source or the isolated Q_j. Induction over individual
operations proves the receiver fixed for all time. The all-state cut law
retains any old packet in Q_j, but nonempty right preparations can evolve or
write independently; they do not satisfy the clean no-event conclusion.

In the same-energy mismatch control the supported source packet has r=0
and a separate inactive packet has r=2 in Q(N-2). Whole-packet swaps never
combine their coordinates. Assuming l=0, one packet always fails funding
and the other always fails presence. Thus no G branch changes either, and
l=p=0 stays true inductively for all time. The energy is still H(y)+4.
The detector cannot borrow the reserve of an adjacent or remote packet.

Conversely replacing a funded supported source's content y by y' changes
the arrived content and the first record to c(y'). Replacing it by an
unsupported field suppresses the event. The accepted ell/j ell fields
have coefficient tuples (1,-1,-1,1) and (-1,0,-2,-2), H=5 in both cases,
and total trial energy nine. Position-code evaluation gives c=747 and
c=422 respectively. Their different record values decode their different
literal fields; the accepted fixed-B0 ratios remain 0 and 5/16. No quantum
state-discrimination or physical probability claim is involved.

This dependence is local and actual: support, consumed reserve and record
translation all belong to the same received packet. A spectator record
printing a preprogrammed target orbit would not obey these intervention
and mismatch statements. Although transport is a selected swap law, the
funded recorder is not an independent neutral-work process multiplied by
an unrelated content wire.

A funded supported packet initially in Ct writes in step one even if C0
is absent. A latch-one supported receiver releases two units without a
write. Dirty packet histories may trigger these branches before a nominated
source arrives, so clean timing, renewal and readback do not extend to
arbitrary occupied preparations. The all-state inverse and conservation
theorems do extend to them. A valid p value alone certifies no source.

## 7. Interface and surviving boundaries

The construction hands onward the complete local packet (b,y,r), latch l,
finite record p, exact forward/inverse branches, packet and record readers,
and the supported clean-trial domain. It transfers every literal K5 source
distinction with its own two-unit reserve and creates a funded local
first record with the finite lifetime just proved. All resources, returning
content, old channel data and dirty-state branches are explicit.

The added coordinate system, presence rule, fixed support cutoff, modular
code, energy weights and matching schedule are definitions. No coherent
encoding, environmental reference system, Gram-preserving all-superposition
map, QDD post-state instrument, Born or occurrence law, physical locality,
SI energy or native-U realization has been proved. In particular a later
coherent instrument cannot be inferred from this integer-data census.
All existing Canon and physical-owner statuses remain unchanged. Finite
audits test this written construction; independent review and actual run
records must earn any candidate acceptance.
