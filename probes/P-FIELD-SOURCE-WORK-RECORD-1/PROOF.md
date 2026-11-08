# Exact autonomous source-to-work-to-record construction

PUBLIC / NON-CANONICAL / L1 / conditional candidate-T. DECLARED-EXTENDED.
Author: A. M. Thorn. Apache-2.0. Exposed analytical derivation before execution.

## 1. Inherited complete carrier and accounts

Use precisely DEF-FIELD-WORK-RECORD-CHAIN, Shared proof 1--8, in Public
Canon v103 at dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d. We restate the
data needed here. Cell i is c_i=(m_i,b_i,z_i,r_i), with three ordered
reacting vectors m_ij and three spectator vectors b_ij in Z^4, raw field
z_i=(E_i,M_i) in Z^4 x Z^2 and resource r_i in N_0: 31 coordinates.
There are N>=2 cells, N-1 neutral resources q_j in N_0 and one receiver
pointer p in C5. The receiver is t=N-1. The full carrier has 32N stored
coordinates; literal equality retains all of them.

The fixed matrices and energy forms are

```text
C = [[1,-1],[-1,0],[0,1],[0,1]],
D = [[1,1,1,0],[-1,-1,0,-1],[0,0,-1,1]], D C=0,
Kmat = [[6,2,-1,2],[2,6,2,-1],[-1,2,6,2],[2,-1,2,6]],
Q(w)=w^t Kmat w, chi(w)=sum(w),
Hraw(E,M)=E^t E+M^t M+E^t C M,
Hcell(c)=sum_j Q(m_j)+sum_j Q(b_j)+Hraw(z)+r,
Htot=sum_i Hcell(c_i)+sum_j q_j+1.
```

The pointer's energy 1 is the inherited chosen constant, not a measured
memory cost. All these forms and the graph remain declared architecture.
The actual charge is

```text
rho_i=(chi(b_i0)+sum_j chi(m_ij), chi(b_i1), chi(b_i2));
div_i=D E_i; defect_i=div_i-rho_i.
```

The active/static maps, whose symbol S is NOT the signed block swap, are

```text
P(a,b,c,d)=(a-b,-a,b,b,c,d),
S(u,v)=(u,u,v,u-v,0,0),
H(a,b,c,d)=2a^2-2ab+3b^2+c^2+d^2+2ac-ad-bc+3bd,
Hraw(P y+S(u,v))=H(y)+3u^2-2uv+2v^2.
```

The rational split of an arbitrary raw field is unique:

```text
a=(2E0-3E1+E2+E3)/5,
b=(-E0-E1+2E2+2E3)/5,
c=M0, d=M1,
u=(2E0+2E1+E2+E3)/5,
v=(E0+E1+3E2-2E3)/5.
```

It is integral exactly when g=2E0-3E1+E2+E3 is divisible by 5.
Off this sublattice the new operation below is the identity. In particular
we do not round, erase the static field or discard a raw-field coset.
The identity D P_E=0 will preserve every divergence, including nonzero
Gauss defects and charged spectator preparations.

The inherited free map is

```text
Fraw(E,M)=(E+C M, M-C^t(E+C M)),
Fraw^-1(E',M')=((I-C C^t)E'-C M', M'+C^t E'),
A_f=[[1,0,1,0],[0,1,0,1],[-2,1,-1,1],[1,-3,1,-2]],
Fraw P=P A_f, Fraw S=S, A_f^5=I, H(A_f y)=H(y).
```

It preserves Hraw and divergence on every raw integer field, not only
integrally split ones. The shell maps are

```text
L=[[1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]],
Vinv=[[1,2,1,2],[2,-1,2,-1],[0,-5,1,-3],[-5,5,-3,4]],
Vinv L=L Vinv=5I, H(Lx)=5H(x),
y=(a,b,c,d) in L Z^4 iff a+2b=c+2d=0 mod5.
```

With Z4 the zero vector, literal ordered matter endpoints are

```text
R=((1,-2,1,0),Z4,Z4), Qsum(R)=18,
AM=((1,0,0,0),(0,-1,0,0),(0,-1,1,0)), Qsum(AM)=20,
ZM=(Z4,Z4,Z4).
```

The original total local involution G exchanges funded pairs

```text
(R,b,PLx+S sigma,r) <-> (AM,b,Px+S sigma,r+4H(x)-2).
```

On R the split must be integral, y must be in L Z^4, x=Vinv y/5 and
r+4H(x)-2>=0. On AM the split must be integral and r+2-4H(y)>=0.
Every other whole input is fixed, including all ZM inputs. The spectator,
static field, reacting-vector sum, charge, divergence and defect are fixed.
The two endpoint energy equality proves full Hcell conservation.

At the receiver replace G by

```text
e(c)=1 iff the actual G(c) accepts R -> AM, otherwise 0,
Ghat_t(c,p)=(G(c),p+e(c) mod5),
Ghat_t^-1(c',p')=(G(c'),p'-e(G(c')) mod5).
```

All other operations fix p. This writer has a recovered-input inverse;
it is not an involution. The fixed reader O(p) is BLANK for p=0 and HIT
otherwise. It reads no clock, N, source coordinates or history.

Original contact layers A and B exchange r_j with q_j, then q_j with
r_(j+1), respectively. Both are complete swaps, including occupied slots.
The original macrostep is That=F B A Ghat, with rightmost operation first.
A fixed cut j omits BOTH swaps incident with q_j, retains its content,
and changes neither the local reactions nor the source operation below.

## 2. The single added source-local operation

To distinguish the signed block swap from static S and contact B, call it

```text
Bstar(a,b,c,d)=(-c,-d,-a,-b), Bstar^2=I,
f(a,b)=(a-b)^2+b^2,
Delta(y)=H(Bstar y)-H(y)=f(c,d)-f(a,b).
```

Expanding H gives the displayed difference; equivalently its cross terms
are unchanged while the diagonal block weights exchange. Hence
Delta(Bstar y)=-Delta(y).

Define Ksrc on an arbitrary complete cell:

1. If its raw split is not integral, retain the whole cell.
2. Otherwise calculate Delta(y). If r-Delta(y)<0, retain the whole cell.
3. Otherwise replace (P y+S sigma,r) by
   (P Bstar y+S sigma,r-Delta(y)), retaining m,b and sigma.

The accepted image is integrally split. Applying Ksrc again is funded,
since (r-Delta(y))-Delta(Bstar y)=r>=0, and recovers the exact input.
Thus accepted states occur in transpositions or fixed points. A refused
state cannot be an accepted image, by the same identity. Nonsplit states
remain nonsplit fixed points. This proves Ksrc^2=I on the entire cell
carrier, including arbitrary occupied resources and all refusal branches.

All unchanged matter and spectator terms remain in the energy account.
The static field is retained, and H(Bstar y)+(r-Delta(y))=H(y)+r.
Thus Ksrc preserves Hcell, resource nonnegativity, spectators and all
reacting-vector sums. Its field difference P(Bstar y-y) is divergence
free. Charge, divergence and Gauss defect are separately preserved on
ALL cells, without assuming Gauss's law initially.

This realizes the local conservative operation proposed in #1608, with
Delta Q(m)=0 because matter is retained. The generic funding mechanism
and Bstar are inherited ideas; their existence is not a selection theorem.

## 3. One autonomous law on the unchanged carrier

Apply Ksrc at cell 0 before every original macrostep:

```text
Tnew = F B A Ghat Ksrc_0,
Tnew^-1 = Ksrc_0 Ghat^-1 A B F^-1.
```

Each adjacent inverse cancels, so both inverse identities hold on the full
carrier. Every original account from section 1 is preserved by every
factor. The same applies with any fixed cut. The added factor has radius
zero, so the two-way dependence radius remains at most two stored-block
edges; depth increases from four to five. All cells, occupied channels
and pointer are retained; no stored counter, new clock, selector bit,
one-off prefix or direct energy reader is added.

The prescribed contact at the distinguished source is a new selected law.
It is not translation invariant over interchangeable source/receiver roles.
Its fixed position and placement before Ghat are explicit architecture
choices shared by every preparation and control.

Positive-definite Q and Hraw, nonnegative r,q and finite p make each fixed
finite-energy shell finite. Since Tnew is a bijection preserving the shell,
every complete finite-energy state is periodic. This does not imply a
permanent event record, a physical clock or dissipation.

## 4. Zero-resource, same-residue source preparations

For every N>=2 prepare zero spectators, static fields, channels and all
cell resources. Source matter and intermediate matter are ZM; the receiver
is (R,0,0,0) and p=0. Change only the source active field between

```text
v=(2,-1,0,0),          H(v)=15,
v_late=A_f v=(2,-1,-5,5), H(v_late)=15.
```

Call the complete preparations s_early and s_late. Their common total is
15+18+1=34. Their actual charges and Gauss defects are zero. They also
have the same full raw-field residue modulo 5 since v_late-v=(0,0,-5,5).
No source-dependent answer is stored in the receiver or a bank.

The exact free orbit and proposed contact costs are

| phase a | A_f^a v | Delta |
|---|---|---:|
| 0 | (2,-1,0,0) | -10 |
| 1 | (2,-1,-5,5) | 115 |
| 2 | (-3,4,5,-10) | 260 |
| 3 | (2,-6,-5,10) | 225 |
| 4 | (-3,4,5,-5) | 60 |

Matrix multiplication gives A_f^5 v=v; direct f evaluation gives all
five costs. On v at r=0 the new operation accepts and produces
y0=(0,0,-2,1), H(y0)=5 and r=10. On the other four phases it refuses
at r=0. In the first four steps from s_late, the source remains ZM,
every resource stays zero, intermediate G rejects, receiver G is
unfunded, and F only advances the source phase. Therefore

```text
Tnew^4(s_late)=s_early
```

as literal equality of the COMPLETE state. Autonomy then gives
Tnew^(n+4)(s_late)=Tnew^n(s_early) for every n>=0 (indeed for all integer
n by bijectivity). This is a phase/latency discriminator. No larger
eventual output energy or permanent distinction is inferred.

For completeness, the subsequent free orbit of y0 has costs
10,55,75,40,0. At r=0 the first four refuse, and the fifth Bstar is an
actual fixed point, (2,-1,-2,1). Thus a source with zero returned resource
retains energy 5 on this orbit; it cannot release a second pulse before
the original pulse reaches the receiver.

## 5. First arrival, actual work, and bounded current record

In step 1 from s_early, Ksrc converts ten units of source field energy
into its original r0. Source G rejects because its matter is ZM. The
receiver G occurs before arrival and rejects at r=0. The original contact
permutation puts ten in r1. Intermediate ZM cells cannot react.

For 1<=k<=N-1 the first ten-unit pulse occupies r_k at boundary k;
all other resources and channels are zero. Before reaching the receiver
there is no return resource at the source, and the y0 cost observation
above rules out another emission. The field evolves as P A_f^k y0.
For k<N-1 the receiver remains exactly ready and p=0. This induction
includes N=2, where the first recipient is already the receiver.

At boundary N-1 the receiver has r=10. In step N its actual R-to-AM
reaction costs two resource units, raises its matter energy from 18 to20
and increments p to1. The remaining eight units go to q_(N-2) in the
contact layer. This is the first write; source energy has already fallen
from15 to5 and no external reserve was present.

Accounts through that step are

```text
initial:            15 + 18 + 0 + 1 = 34,
first transit:       5 + 18 +10 + 1 = 34,
after receiver work: 5 + 20 + 8 + 1 = 34.
```

The four-step full-state identity implies first arrival N+3 and first
write N+4 from s_late. Its first emission is step5. The ten-unit emission
and two-unit receiver reaction are exact chosen accounting quantities,
not an SI energy calibration or an identified particle rest energy.

After a receiver increment its matter is AM. Another R-to-AM increment
requires an intervening AM-to-R step; Ksrc never touches this receiver
because N>=2. Hence successive increments are at least two macrosteps
apart. Starting with p=0, after the first event j at most four increments
occur through j+7, so the pointer is nonzero on all eight boundaries
j,...,j+7. This inherited retention argument holds for the new law too.

Consequently the SAME current-pointer reader gives

```text
O(Tnew^k s_early)=HIT,
O(Tnew^k s_late)=BLANK,       N<=k<=N+3.
```

There are four common distinguishing boundaries, not eight. Later the
delayed state also writes. Neither first arrival nor first write is
observable from a universal ready-state test asserted here: these times
are conditional statements about the fixed preparations. No optimal
latency or robustness to arbitrary perturbations is claimed.

For an arbitrary initial p, every accepted receiver event still adds one
modulo5 and has the same inverse. The HIT/BLANK guarantee above requires
the frozen ready p=0; occupied-pointer continuation does not promise
non-destructive archival or distinguishability for every old pointer.

## 6. Controls with no hidden reservoir

If the source field is zero and the same zero-resource preparation is
retained, Ksrc fixes it, source ZM rejects, all swaps exchange zeros and
receiver R is always unfunded. The receiver stays BLANK for all time.
Its total energy is19, transparently different from the two H15 signals.

Disabling only Ksrc leaves source matter ZM and active energy15 under F.
There is no release to r. Both original source preparations therefore
leave the original receiver BLANK for all time. This equal-total-energy
control retains every initial resource and field and changes only the
declared new operation.

For any one fixed cut j the downstream component is initially ready,
with zero fields/resources/channels, ZM intermediate matter and receiverR.
Every remaining primitive fixes it. Ksrc belongs upstream and no surviving
swap crosses the cut. The stored q_j is retained. Thus every such cut
keeps the receiver BLANK for all time, for either source. This is a
primitive-level induction and not an extrapolation from finite runs.

These controls establish source/contact/path dependence within the chosen
preparation family. A HIT in an arbitrary occupied apparatus is only a
local accepted-event record; it is not a universal certificate of source
identity, provenance or initial energy.

## 7. Exact selection and native-admission boundary

First, no word in the ORIGINAL complete-chain primitives can implement
Ksrc on all complete states. On a marked source whose matter is ZM,
every original G and inverse rejects. Resource swaps never alter matter
or field. F and its inverse preserve H(y). Thus every finite word,
even one selected from the complete current state, preserves that marked
source's active H. Ksrc maps v with r0 to y0 with r10 and changes H
from15 to5 while retaining ZM. This one witness excludes compilation in
that original alphabet. It is compatible with #1592/#1608's broader
restricted field-word obstruction, not a global impossibility theorem
about all native extensions or encodings.

Second, Ksrc does not descend to a deterministic map on the raw
modulo-5 checkpoint, even when the unchanged matter, spectators, r and
pointer are retained exactly. The two source inputs have identical
projected states, but Ksrc(v,0) has active residue (0,0,3,1) and r10,
whereas Ksrc(A_f v,0) has residue (2,4,0,0) and r0. Even reducing the
resources modulo5 leaves the field residues unequal. P has an integer
left inverse on its image, so the raw projected fields are unequal too.
Therefore no function of that common coarse input can reproduce both
projected outputs. A finer carrier, ancestry or additional reading could
be investigated separately; none is supplied by this witness.

Third, conservation does not select Ksrc. The identity operation has all
the same carrier, inverse, charge, Gauss and energy properties and gives
BLANK forever on the two sources. Both are mathematically admissible
under those properties but predict different present records. Selecting
the new law by demanding the desired record would be circular.

The new positive result closes the whole-carrier composition and work
record for a stated extra law. It removes the additional bank, whole-cell
exchange, direct H reader and separate timing controller used by earlier
comparison constructions. It does not derive the new source contact from
J or original U, nor select its physical occurrence. Clock/action scales,
the Dirac energy pair, inertial response and the physical dictionary are
not determined. #1498/#1398 and #1589 remain the relevant owners; no
registered physical gate or v104 release closes through this probe alone.
