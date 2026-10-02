# C-FIELD-J-CONTENT-TRANSPORT-N

**PUBLIC, NON-CANONICAL. Prospective L1 candidate; no execution or earned
status.** Owner: A. M. Thorn / algebra_builder, sequentially after Stage A.
Reservation: [issue #1327](https://github.com/mathorn1973/twist-j/issues/1327).
Original work under Apache-2.0. Prepared 1 October 2026.

## 1. Basis, exposure and architecture decision

Accepted Stage-A handoff: `3f53cff429c67fbdfa95941b3024279d9fd59638`.
Admitted mathematical source: C-FIELD-J-ENERGY-READOUT-N/PROOF.md at
`49dfad177c6ab698b5751de3e56629508982b05f`, with the accepted mathematics
and preserved rejected Python contract recorded at the handoff. Independent
review is pinned at `155dd04446564df7fddbb78996a3ad82231b595d`. Its independent
derivation was frozen at `c404c1c53a9af3ce1b2523de8a56a270e082e7c9`.
The separate inclusive reader at `4fde4fa50409d5df16fd4b210880044a87eb7a2f`
was accepted by review `55c68b6215f2c4e6fac92d29163850eff4179bdb`.
These are candidate-level dependencies, not Canon additions.

The normative basis remains public main/canon-v96
`44423153eee6259c7277eec5f5adbed9679f9146`, content
`d63de7e7345cf5fa5ab344654aafb7238d6d8bca`, CANON.md 873495 bytes, SHA-256
`eb2a7bc1c7e38e130544b9fef4c0f05443df01484bdb55a52fc10b427fcee0a2`.
The coordinator owns current authority, collision, issue and public-pin
checks. STATUS/POLICY/AGENTS/CORE/FRONTIER and the relevant Stage-A/chain
evidence have been read. The public construction lead in
[issue comment 5941266927](https://github.com/mathorn1973/twist-j/issues/1327#issuecomment-5941266927)
is an exposed design suggestion, not evidence of success. The builder and
one disclosed coauthor-side reasoning subagent derived timing on paper.
That check is not the fresh independent review. No Stage-B computation has
run. Stage-A counts, ratios and prior failed-input counterexamples are exposed.

This is a **separately selected classical integer law**. It is neither
unchanged native U nor an asserted extension projecting to U or to the old
field chain. Every packet, latch, modular record, weight, schedule, support
guard and code below is an added architectural choice. The field content
has identity transport action: there is no free A_f or J_f evolution in
this law. No old-chain dimension, energy or latency is inherited.

## 2. Complete stored carrier and energy

Fix any finite integer N>=2 and t=N-1. Stored blocks form the path
C0--Q0--C1--...--Q(N-2)--Ct. Each cell C_i and channel Q_j holds one packet

```text
P=(b,y,r), b in {0,1}, y=(y0,y1,y2,y3) in Z^4, r in Z_{>=0}.
```

All such packets are admitted, including b=0 with nonzero stored field or
reserve. The distinguished empty packet is E=(0,(0,0,0,0),0). Presence b=1
distinguishes stored zero from E. The receiver block alone also holds
l in {0,1} and p in Z/MZ with canonical representatives 0,...,M-1,
M=1226. Thus the complete state is

```text
s=((P_C0,...,P_Ct),(P_Q0,...,P_Q(N-2)),l,p).
```

Equality includes every ordered slot and packet coordinate, old channel
contents, l and p. There are 6(2N-1)+2=12N-4 stored integer coordinates,
with the stated restrictions. No clock, history, source label, provenance
bit, branch log or unlisted reservoir is stored. N and an optional fixed
cut index are parameters of the selected law, not reader inputs.

Use the accepted active-field quadratic

```text
H(y)=2y0^2-2y0*y1+3y1^2+y2^2+y3^2
     +2y0*y2-y0*y3-y1*y2+3y1*y3,
E_packet(b,y,r)=b+H(y)+r,
E_total(s)=sum_all_slots E_packet(P)+2l+1.
```

The last constant is the selected energy of the entire finite record
register: E_record(p)=1 for every p, including blank. Latch energy is 2l.
The presence bit, all fields even in inactive packets, all reserves and
all channels are counted. The full energy is positive and finite-energy
shells are finite by positivity of H and finite b,l,p ranges. These are
selected dimensionless energies; no measured cost or SI identification.

## 3. Exact content code and receiver-local access

For y define its integral coefficient chart

```text
a=C^-1 y=(2y0-2y1+y2-y3, y0, y0-y1-y3, y0-2y1-y3),
C a=(a1,a2-a3,a0-a1-a3,a1-2a2+a3).
```

Supported packets have b=1 and H(y)<=5; zero is supported. Stage A proves
the coefficients lie in B=[-3,3]x[-2,2]x[-2,2]x[-3,3]. Let

```text
code(y)=1+(((a0+3)*5+(a1+2))*5+(a2+2))*7+(a3+3).
```

This is an injective position code on the whole containing box, with values
1,...,1225, so no supported value is blank. It is not a target trajectory
table. Record decoding on every p in 0,...,1225 is: p=0 -> BLANK;
otherwise expand p-1 in radices 7,5,5,7 from right to left to recover a;
subtract shifts (3,2,2,3), compute y=C a and reject with INVALID if H(y)>5;
otherwise return VALUE(a,y). No arbitrary modular value is assumed valid.

The fixed packet-snapshot reader uses only the present receiver packet:
b=0 -> ABSENT; b=1,H>5 -> UNSUPPORTED; otherwise VALUE(a,y), with its
current reserve available as a separate local stored coordinate. The fixed
record reader uses only current p and returns the preceding BLANK/INVALID/
VALUE result. It need not be gated by the latch; its retention interval is
distinct from latch excitation. Neither reader receives N, a clock, launch
time, source, trajectory or initial p. For a decoded VALUE, Stage-A data
E5=(e0,e1,a mod5) are derived with e0=H(y), e1=H((I+A_f^2)y); zero has
its exact zero reading. The new code does not replace the norm-941/mod-25
interface. The fixed B0 LOW comparison is made only at its stated source
domain; not every K5 vector is a native balanced piston.

## 4. Complete dynamics, inverse and rejected branches

Only receiver reaction G changes packet contents. At its input write
P_Ct=(b,y,r). If unsupported, G retains every coordinate for either latch.
If supported, set c=code(y) and use exactly

```text
l=0,r>=2: (r,l,p) -> (r-2,1,p+c mod M), accepted write;
l=0,r<2:  entire input fixed, insufficient same-packet funding;
l=1:      (r,l,p) -> (r+2,0,p), accepted release.
```

b and y are always retained. The release may fund a different supported
packet in a dirty state: no source-provenance property is assumed. An
accepted event means precisely this actual forward funded l=0 branch.
It uses both the content support/code and the reserve of that same packet.
The two consumed units become latch energy, not erased spent resources.

The inverse on the receiver OUTPUT is explicitly

```text
unsupported: entire input fixed;
supported,l=1:      (r,1,p) -> (r+2,0,p-code(y) mod M);
supported,l=0,r>=2: (r,0,p) -> (r-2,1,p);
supported,l=0,r<2:  entire input fixed.
```

Support does not change. These image branches are disjoint and cover every
admitted local state. G is not an involution; the inverse of a write undoes
its record translation, while the forward release leaves the record alone.

A_j swaps the **entire** packets in C_j and Q_j. B_j swaps the entire
packets in Q_j and C_(j+1). Both may be occupied; nothing is copied,
overwritten or cleared. A and B apply their respective disjoint matchings.
Forward chronology is G;A;B, T_N=B A G. Inverse chronology is B;A;G^-1.
G has stored-block radius zero, each matching radius one. Forward and inverse
macrosteps have depth three and dependence radius at most two path edges.
This is mathematical locality on these selected blocks, not physical speed.

A fixed cut j omits both A_j and B_j at every macrostep and in the inverse.
It retains Q_j, whose old complete packet is then fixed. The optional cut
is chosen before the trial and never inferred from a reader; no dynamic
cut control is included. Prove all-state inverse, conservation and locality
for no cut and each j, including all occupied slots and rejected branches.

Claimed invariants are full E_total; the multiset of all (b,y) packet
contents; and sum_all_slots r+2l. Actual electric charge, Gauss law and
coherent amplitude are not defined on this new carrier. Finite-shell
bijectivity implies periodicity from every admitted initial state, without
assuming a uniform period for arbitrary states or cuts.

## 5. Quantified clean trial and all-time record semantics

For every supported y in K5 prepare P_C0=(1,y,2), all other packets E,
l=0,p=0. The energy is H(y)+4. Let T=2N-1. Whole-packet contact transport
follows the single cycle

```text
C0 -> C1 -> ... -> Ct -> Q(N-2) -> ... -> Q0 -> C0.
```

Prove, for all N>=2 and every K5 source, first receiver packet arrival at
boundary N-1; first accepted write at G in step N, visible at boundary N;
and literal local snapshot equality y_received=y_source at arrival. The
record decoder recovers exactly the same y at boundary N even though the
packet has moved into the last channel by then. The receiver preparation
is identical across sources and no reader is given the time parameter.

For every m>=0 the write steps are W_m=N+2mT and release steps
R_m=N+(2m+1)T. Derive this all-time schedule by induction; no finite run
establishes it. If c=code(y), at macro-boundary n let

```text
w(n)=0 if n<N, otherwise 1+floor((n-N)/(2T)),
p(n)=w(n)*c mod M.
```

Latch excitation lasts exactly from W_m through R_m-1, T boundaries. The
first record value remains exactly c at boundaries N,...,N+2T-1, a total
of 2T boundaries spanning 2T-1 elapsed macrosteps. The next write changes it
because c is nonzero modulo M. Subsequent p values may be BLANK, INVALID
or another valid code; do not interpret them generally as the last source.

The packets and latch, excluding record p, return to their exact initial
preparation at boundary 2T, while p=c remains. At boundary 2kT they have
the same operative preparation and p=k*c mod M. Complete initial-state
return occurs at 2T*M/gcd(M,c); prove this exact clean-family period,
using the presence-marked packet to distinguish positions. This is finite
capacity and eventual record recurrence, not unlimited archive space.
No external erase, fresh source replacement or fresh record supply is part
of the autonomous law. Operative renewal with a retained record differs
from blank/full renewal; only the latter eventually returns by the stated
finite recurrence. Applying the mathematical inverse can undo a write.

For the same clean packet/latch preparation but arbitrary p0, derive
p(n)=p0+w(n)c mod M. In particular p0=-c makes the first write BLANK.
The complete dynamics is valid for arbitrary initial latch/record states,
but the first-trial decoding guarantee requires p0=0 and l=0. A valid
record value alone does not certify source provenance or a latest event.

## 6. Controls, causal coupling and transport equality

The transported source class is literal y in K5, with identity action.
The snapshot and first retained record maps are injective on all 291
supported sources; no phase/sign quotient or time-dependent code is used.
Changing y changes the arriving packet and its encoded record. Specifically
test y=C ell and C(j ell), with coefficients (1,-1,-1,1) and (-1,0,-2,-2).
They have equal H=5 and E_total=9, but different records and fixed-B0 LOW
ratios 0 and 5/16. This is classical content transfer, not perfect
single-shot discrimination of nonorthogonal quantum states.

Freeze these controls and their precise conclusions:

* All packets E, l=p=0: absence remains absence and record BLANK forever.
* Supported stored zero (1,0,2): follows the positive theorem and receives
  a nonzero valid code; it differs from absence.
* Source (1,y,r) with y in K5 and r=0 or 1, all else empty/ready: no write
  or release forever, while its literal content still circulates.
* Source (1,y,2) with H(y)>5, all else empty/ready: no reaction forever;
  receiver snapshot reports UNSUPPORTED on arrival.
* Source (0,y,r), all else empty/ready: no reaction forever, although every
  stored field/reserve remains in the total state and energy.
* Any one fixed cut, clean positive trial: receiver packet remains E and
  l=p=0 at every substep forever. Cut Q_j retains its complete old contents
  in arbitrary states; dirty downstream states are not covered by this
  no-event theorem.
* Same energy mismatch: (1,y,0) in C0 and inactive packet (0,0,2) in the
  last channel, all else empty/ready. Content and funding circulate in
  different whole packets, so neither can produce a write forever.
* Content exchange at preparation replaces y by another supported y while
  retaining that packet's r=2: the first recorded code is of the replacement.
  Unsupported replacement suppresses the event. There is no unseen original
  source label for the receiver to recover.
* A supported packet with r=2 preloaded in Ct, all other packets E,l=p=0,
  writes in step one despite absent source. Preloaded latch one with a
  supported receiver packet releases two units without writing. These are
  admitted local events, not source-certified trials.

Packet transport is a chosen swap law, but the detector is not an unrelated
work chain times a phase wire. Its support guard, consumed reserve and
record translation all use the same received packet. Prove the intervention
statements and mismatch control, rather than assuming target dependence.
Arbitrary occupied channels have the total bijection/account theorem, not
the clean first-arrival/provenance theorem. Their old data are never lost.

## 7. Accepted code, precise finite audits and falsifiers

verify.py will be standalone Python 3.10+ with standard-library exact
integer/Fraction arithmetic and no imports from prior candidates, files,
network, randomness or floating point. Its state functions implement only
the admitted mathematical carrier, represented by exact builtin tuples and
genuine ints (bool excluded). Malformed Python objects are outside this API;
there is no new total-all-Python-object theorem. The record decoder is total
on every admitted p. Code/body definitions are frozen before execution.

Finite audits, supplementary to universal proofs:

1. Scan the proved 1225 coefficient box; require the exposed 291 K5 states,
   shell counts (1,20,30,60,60,120), code injectivity and round trips. Exhaust
   all 1226 record values and require exactly one BLANK, 291 VALUE and
   934 INVALID values. Check stored zero and the fixed equal-energy pair.
2. Audit local G and G^-1 in both compositions, energy, content and actual
   write semantics for b=0,1; every K5 y plus unsupported fields C(3,0,0,0)
   and C(10^6,0,0,0); r=0,...,4; l=0,1; and p in (0,1,613,1225,M-c mod M)
   where c is the supported position code or 1 for unsupported content.
   This is 293*2*5*2*5=29300 cases, with duplicate p choices retained.
3. All-state-law finite fixtures: for N=2,...,6, no cut and each fixed cut,
   and fixture index k=0,...,31, populate every cell/channel with the
   deterministic packet list and index rule fixed in verify.py. Set l=k mod2,
   p=(37k) mod M. Check both full-step inverse compositions and every layer's
   invariants, retaining occupied cut-channel contents. Include coincident
   equal packets, inactive stored fields/reserves and unsupported packets.
   The exact list and rule are part of the immutable code; no random search.
4. For N=2,...,6 and every K5 y run exactly 4T macrosteps from each clean
   trial. At every G/A/B boundary check the exact packet position, content,
   reserve/latch conservation, record formula, energy and local readers;
   test forward and inverse round trips on the visited complete states.
   This covers two writes/releases and two operative returns. The all-time
   and all-N assertions depend on induction, not this horizon.
5. For every K5 source and N=2,...,4, run every individual cut for 2T steps,
   requiring the prepared receiver to stay unchanged after every layer.
   Run the absence, reserve-0/1, inactive, unsupported and same-energy
   mismatch controls for N=2,...,6 through 2T steps, using sources zero,
   ell and j ell plus the two stated unsupported witnesses where applicable.
   Test dirty receiver/latch controls and arbitrary p0 in {0,1,613,1225,M-c}
   for those three supported sources through 2T steps. Separate the facts
   proved for all dirty states from these finite examples.
6. For every K5 code, audit its modular record orbit over M successive
   additions, requiring the first return to equal M/gcd(M,c). This is a
   finite arithmetic audit of the proved recurrence, not a long chain run.

Any incorrect admitted inverse, energy/content/resource invariant, code or
image test, claimed locality dependency, all-time formula, clean decoder,
first time, record lifetime, renewal, cut or control result fires its exact
claim. Zero tolerance. Preserve witnesses and scope; do not move thresholds
or edit a fired scientific pin. Authority/custody/runtime faults are reported
separately, not converted into mathematical results.

## 8. Freeze, independent review, execution and handoff ceiling

Root freezes this complete specification publicly before the fresh reviewer
starts its derivation/code. The reviewer receives only PREREG.md and the
admitted immutable mathematical inputs, not author PROOF.md, verify.py,
outputs or diff. It freezes its independent implementation and reasoning
before comparison. Coauthor-side timing advice is disclosed and is not that
review. No known-count or design-result blindness is asserted.

Freeze PREREG.md, PROOF.md and verify.py together at a complete public pin,
record hashes and read back the bytes before any scientific execution.
Before root signals that pin, only static source review/AST parsing is
allowed. No git mutation is delegated to this builder. Prospective command:

    python3 notes/C-FIELD-J-CONTENT-TRANSPORT-N/verify.py

Use the current repository 600-second envelope and LC_ALL=C,LANG=C,TZ=UTC,
PYTHONHASHSEED=0,PYTHONDONTWRITEBYTECODE=1. Only after execution add exact
EXPECTED.txt, neutral RUN.md and scoped RESULT.md with actual hashes,
counts, exit/stderr and independent-review provenance. A notes CI pass does
not execute this verifier or establish a second-architecture gate.

The intended downstream interface is the complete packet/latch/record
carrier, its local forward/inverse laws, supported snapshot and finite
first-record guarantee, with all extra resources exposed. Candidate-T is
possible only for the scoped proved construction after review; finite
audits remain finite evidence. No coherent source representation, Gram-
preserving all-superposition transfer, QDD post-state instrument, Born or
occurrence law, physical energy/locality, native-U selection, SI scale,
infinite fresh archive, Canon promotion or physical-parent closure follows.
