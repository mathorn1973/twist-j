# A bounded local record of a transferred event

NON-CANONICAL / L1. Conditional candidate-T analytical construction.
Candidate: C-FIELD-RECEIVER-BOUNDED-RECORD-N. No Canon authority.
Public reservation: https://github.com/mathorn1973/twist-j/issues/1313.

The exact dependency is
`notes/C-FIELD-FINITE-CHAIN-FIRST-DELIVERY-N/PROOF.md` at commit
`04fa72ca2506398bf47a64fe33aa024625bd4f9b`, the candidate in PR #1312.
That proof in turn uses the four-layer construction from PR #1310 at
`dd354e3e01ad7f7bb535f33e012c5ef1b46a87d2`. These dependencies remain
NON-CANONICAL candidates. Public authority remains Public Canon v95 at its
existing scope. This note changes no predecessor source or claim.

The new construction adds one receiver-local permutation to the inherited
law. Its three phases, reader, duration and resource account are selected
analytically before execution. The conclusions below are known analytical
predictions for a subsequent audit, not independently discovered audit
outcomes. This proof reports no scientific execution.

## 1. Exact carrier, energy and charge

Fix a finite integer N>=2. Cell i, for 0<=i<N, stores

```text
ci=(mi,bi,zi,ri),
mi=(mi0,mi1,mi2) in (Z^4)^3,
bi=(bi0,bi1,bi2) in (Z^4)^3,
zi=(Ei,Mi) in Z^4 x Z^2,
ri in Z_{>=0}.
```

The separately stored neutral channels are q0,...,q(N-2) in Z_{>=0}.
The complete ordered state is

```text
s=(c0,...,c(N-1),q0,...,q(N-2)).
```

Equality means literal equality of every stored coordinate, including the
order of the three matter registers. There are 31N+(N-1)=32N-1 coordinates:
30N unrestricted integers and 2N-1 nonnegative resources. No coordinate,
external history, time register or readout state is appended.

For v in Z^4 define Q(v)=v^t K_Q v and chi(v)=sum_j v_j, with

```text
K_Q=[[6,2,-1,2],[2,6,2,-1],[-1,2,6,2],[2,-1,2,6]],
C=[[1,-1],[-1,0],[0,1],[0,1]],
D=[[1,1,1,0],[-1,-1,0,-1],[0,0,-1,1]], DC=0,
Hraw(E,M)=E^t E+M^t M+E^t C M,
Hcell(m,b,z,r)=sum_j Q(mj)+sum_j Q(bj)+Hraw(z)+r,
H_N(s)=sum_i Hcell(ci)+sum_j qj.
```

The notation K_Q distinguishes this quadratic matrix from the new gate K.
The electric edges inside each cell are (0->1,0->1,0->2,2->1), where the
parallel edges are distinct. The three reacting registers are all at that
cell's vertex 0; the spectator registers are at vertices 0,1,2. Thus the
actual local vertex charge and Gauss defect are

```text
rho_i=(chi(bi0)+sum_j chi(mij),chi(bi1),chi(bi2)),
defect_i=D Ei-rho_i.
```

There are 3N actual charge entries and 3N defect entries. Cells have disjoint
electric vertices. The contact graph below connects stored blocks; it is
not an additional electric boundary. Preserving only a sum over different
electric vertices would not suffice. Here the new permutation exchanges
registers at the same vertex and preserves the actual charge there.

For x=(a,b,c,d) and sigma=(u,v), the inherited local definitions are

```text
P(a,b,c,d)=(a-b,-a,b,b,c,d),
S(u,v)=(u,u,v,u-v,0,0),
A_field=[[1,0,1,0],[0,1,0,1],[-2,1,-1,1],[1,-3,1,-2]],
L=[[1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]],
H(a,b,c,d)=2a^2-2ab+3b^2+c^2+d^2+2ac-ad-bc+3bd,
T(E,M)=(E+CM,M-C^t(E+CM)).
```

L is the predecessor's energy-five map, also written L_5. The exact
certificates used from the pinned dependency are

```text
Hraw(Px+S(u,v))=H(x)+3u^2-2uv+2v^2,
DP_E=0, TP=P A_field, TS=S,
H(A_field x)=H(x), A_field^5=I,
L A_field=A_field L, H(Lx)=5H(x),
T^-1(E',M')=((I-CC^t)E'-CM',M'+C^t E').
```

These are exact polynomial and matrix identities for the displayed
definitions. The theorem below is conditional on those inherited local
certificates; it does not upgrade their status. The split z=Py+S sigma is
unique over the rationals. For z=(E0,E1,E2,E3,M0,M1), it is explicitly

```text
y=((2E0-3E1+E2+E3)/5,(-E0-E1+2E2+2E3)/5,M0,M1),
sigma=((2E0+2E1+E2+E3)/5,(E0+E1+3E2-2E3)/5).
```

An integral split is required wherever the gate below uses one. Integral
y=(a,b,c,d) lies in L Z^4 exactly when a+2b and c+2d are divisible by 5;
then its unique preimage is x=(A_field^2 L)y/5. There is no rounding,
projection, partial field discard or implicit admission of a rational state.

## 2. Inherited gates and the new receiver-local gate

The inherited literal matter triples are

```text
R=((1,-2,1,0),(0,0,0,0),(0,0,0,0)),
AM=((1,0,0,0),(0,-1,0,0),(0,-1,1,0)),
ZM=((0,0,0,0),(0,0,0,0),(0,0,0,0)).
```

Their respective matter energies are 18,20,0. Both R and AM have register
sum (1,-2,1,0), whose chi is zero. For integer x,sigma and arbitrary
spectators b, the complete reaction gate G exchanges the funded pairs

```text
(R,b,PLx+S sigma,r) -> (AM,b,Px+S sigma,r+4H(x)-2),
    when r+4H(x)-2>=0;
(AM,b,Px+S sigma,r) -> (R,b,PLx+S sigma,r+2-4H(x)),
    when r+2-4H(x)>=0.
```

Every other full input is fixed. This includes off-endpoint matter,
nonintegral splits, failed R-side image admission and insufficient funding.
The unique split, injective L and distinct literal endpoints make the
exchanged pairs disjoint. Thus G^2=I globally. Its energy identity is

```text
18+5H(x)+r = 20+H(x)+(r+4H(x)-2).
```

The spectators, reacting-register vector sum and DE are preserved.
In particular the charge and Gauss defect are preserved. The free gate is
F(m,b,z,r)=(m,b,Tz,r), with the displayed inverse of T.

Write a=(1,0,0,0), b_*=(0,-1,0,0), c=(0,-1,1,0), and define

```text
M0=(a,b_*,c)=AM,
M1=(b_*,c,a),
M2=(c,a,b_*).
```

The name b_* here denotes one literal matter vector, not the spectator
triple b. These three matter triples are distinct, because a,b_*,c are
distinct. None is R or ZM. Define a total local gate K by

```text
K(M0,b,z,r)=(M1,b,z,r),
K(M1,b,z,r)=(M2,b,z,r),
K(M2,b,z,r)=(M0,b,z,r),
K(m,b,z,r)=(m,b,z,r) for every other matter triple m.
```

The same permutation is used for every possible spectator, raw-field and
resource input. It is not conditional on time, channel contents or a
recent reaction. It obeys K^3=I and K^-1=K^2 on the whole local carrier.

Each cycle state has matter energy Q(a)+Q(b_*)+Q(c)=6+6+8=20 and
register vector sum (1,-2,1,0). Hence K preserves the complete local
energy, each actual vertex charge and every Gauss defect. It also preserves
nonnegativity of resources by leaving them untouched.

K is applied only at the designated receiver, cell N-1. The source and
intermediate cells have no K operation. Being the receiver is a declared
boundary role in the architecture, not a label inferred from an observed
run. The local formula for K is independent of N. This is not a claim of
a translation-homogeneous cell law.

## 3. Five-layer law and fixed local reader

For 0<=j<=N-2 define A_j=swap(rj,qj) and
B_j=swap(qj,r(j+1)). These swap entire stored contents, including occupied
receiving resources and old channels. The layers mathcal G, mathcal A,
mathcal B and mathcal F apply all their inherited cell or contact gates.
Within each layer the supports are disjoint. Let mathcal K mean K on the
receiver and identity on every other coordinate. The new chronology is

```text
mathcal G; mathcal K; mathcal A; mathcal B; mathcal F,
V_N=mathcal F mathcal B mathcal A mathcal K mathcal G.
```

Composition in the second line acts from right to left. The complete
inverse is

```text
V_N^-1=mathcal G mathcal K^-1 mathcal A mathcal B mathcal F^-1,
chronologically: mathcal F^-1; mathcal B; mathcal A; mathcal K^-1; mathcal G.
```

Adjacent inverse factors cancel. This uses no commutation between G and K,
nor between reactions and contacts. K is an inserted fifth layer; the
predecessor's four-layer law is not being silently reinterpreted.

If rhat_i is the resource just after mathcal G, mathcal K leaves it
unchanged. The exact complete contact equations therefore remain

```text
r'_0=q_0,
r'_i=rhat_(i-1)                       for 1<=i<=N-1,
q'_j=q_(j+1)                         for 0<=j<=N-3,
q'_(N-2)=rhat_(N-1).
```

These hold for every full input. The q_j on the right are the old channel
contents. For N=2 the middle channel range is empty, giving
(rhat0,rhat1,q0) -> (q0,rhat0,rhat1).

The single local reader is the total function

```text
Read(m,b,z,r)=1 if m is one of M0,M1,M2; otherwise Read(m,b,z,r)=0.
```

It has domain the complete local cell carrier and codomain {0,1}; equality
in its definition is literal ordered-register equality. Its only selection
of location is the designated receiver. It takes neither N, the step
number, a channel, an external history nor a stored previous readout as
an argument. No adaptive decoder selection is allowed.

The three distinguishable matter arrangements are an explicitly chosen
autonomous phase mechanism. They supply a three-state clock inside the
already stored coordinates. The construction does not claim to have no
timing mechanism: it avoids an external timestamp by encoding the phase
in the receiver's actual matter. The reader intentionally ignores which
of these three phases is present.

## 4. Uniform preparation and complete-state theorem

Fix any w in Z^4 with H(w)=1. Prepare exactly the predecessor's cells and
channels:

```text
c0(0)=(R,0,PLw,0),
ci(0)=(ZM,0,0,0)                     for 1<=i<=N-2,
c(N-1)(0)=(R,0,0,0),
qj(0)=0                             for 0<=j<=N-2.
```

Every zero denotes the complete appropriate tuple. In particular, all
spectators, all non-source raw fields and all resources start at zero.
The prepared receiver is identical for every N and every w. This is a
family over admitted high source fields PLw, not arbitrary source
preparations. Put s(k)=V_N^k s(0), where k counts complete macrosteps.

**Theorem.** For every finite N>=2 and every integer H(w)=1, the complete
states through boundary N+3 are given below. In all columns after k=0,
source matter is AM and its six raw-field coordinates are exactly
P A_field^k w. At k=0 they are R and PLw. At every displayed boundary,
intermediate matter is ZM, every spectator is zero, and every raw field
outside the source is zero. The remaining coordinates are:

| Boundary k | Target matter | Cell resources ri | Channels qj |
| --- | --- | --- | --- |
| 0 | R | all zero | all zero |
| 1<=k<=N-1 | R | 2 if i=k, otherwise 0 | all zero |
| N | M1 | all zero | all zero |
| N+1 | M2 | all zero | all zero |
| N+2 | M0=AM | all zero | all zero |
| N+3 | R | all zero | 2 if j=N-2, otherwise 0 |

Empty intermediate ranges have their ordinary empty meaning. Thus the
first boundary with a positive target resource is N-1 and the first step
with a target G-reaction is N, exactly as in the predecessor. Under the
new law, the first boundary with Read=1 is N, and

```text
Read(c(N-1)(k))=0                    for 0<=k<N,
Read(c(N-1)(k))=1                    for N<=k<=N+2,
Read(c(N-1)(N+3))=0.
```

The first record has exactly three consecutive complete-boundary states.
Its onset is N, its first loss is N+3, and its elapsed boundary-time
retention is three macrosteps. This is a first-episode statement; it makes
no claim that the reader can never become one again after N+3.

**Proof: release and first delivery.** In step 1, source G changes
(R,0,PLw,0) to (AM,0,Pw,2), since H(w)=1. Each intermediate G fixes
ZM. The target's G has zero active field and no resource, so its forward
branch would leave -2 and fixes the full input. K fixes that target R.
The contact equations put exactly two units in r1. The free layer changes
the source field to P A_field w and fixes all other fields. This proves
the first boundary, including N=2 where cell 1 is already the target.

Suppose the table holds at boundary 1<=k<N-1. The only resource is
r_k=2, at an intermediate ZM cell. No intermediate G changes any
coordinate. The source is AM with active energy H(A_field^k w)=1 and
r0=0; its proposed reverse resource is 0+2-4=-2, so it rejects. The
target remains unfunded R with zero field and is fixed by both G and K.
The contacts move the two units from r_k to r_(k+1), leaving every
channel zero. F advances only the source field to P A_field^(k+1)w.
This proves the complete state by induction through N-1. Repetition of
the source's period-five field phase has no effect on its failed funding
condition. For N=2 this induction interval is empty.

**Proof: writing and holding the event.** At boundary N-1, target R has
zero field and r_(N-1)=2. In step N, G maps it to (M0,0,0,0), spending
two units, and K maps this full cell to (M1,0,0,0). Every resource and
channel is then zero. Contacts exchange zeros. The source still rejects
its reverse branch, and F only advances its field. This gives boundary N.
The matter change in G is a reaction at layer G; the complete boundary
matter is M1 after the subsequently applied K. These must not be conflated.

In step N+1, target matter M1 is neither literal G endpoint, so G fixes
the full cell. K maps M1 to M2. Contacts again exchange zeros. In step
N+2, G similarly fixes M2 and K maps M2 to M0. All resources, channels,
spectators and non-source fields remain zero. Source reverse funding
continues to fail, giving precisely the two following table rows.

**Proof: first loss.** In step N+3, the target is M0=AM with active
field zero and resource zero. Its reverse G is funded and gives
(R,0,0,2). K fixes R. The A layer does not touch the final cell resource;
B_(N-2) moves those two units into the previously empty q_(N-2).
Thus the receiver's complete boundary cell is exactly (R,0,0,0), every
cell resource is zero, and only the last channel holds two units. The
source has no resource during G in this step and remains AM; its field
advances as in the table. Earlier Read values follow from the distinct
literal matter states. This proves the exact first loss and the theorem.

In particular, the N=2 sequence has first delivery at 1, first target
G-reaction and record at 2, positive boundary reads at 2,3,4, and first
loss at 5 with q0=2. This is the two-cell restriction of the new
five-layer law, not the older target-after-contact order from PR #1308.

## 5. Complete resource account and local reset limitation

Initially, source energy is 18+H(Lw)=18+5=23 and target energy is 18.
Everything else has zero energy. Therefore H_N(s(0))=41, independently
of N and of the admitted w. At boundaries 1 through N-2 the account is
source 21, target 18 and two units at the unique occupied intermediate
resource. This interval is empty when N=2. At N-1 it is source 21 and
target 18+2. At N,N+1,N+2 it is source 21 and target matter energy 20.
At N+3 it is source 21, target 18 and last channel 2. Every sum is 41.

All prepared matter triples have zero total chi, and K preserves the full
reacting-register vector sum. Every nonzero field in the table is in
P Z^4, with DP_E=0. Hence every actual charge entry and every Gauss
defect entry is exactly zero throughout this complete trajectory. This
includes the six raw source field coordinates and all spectator registers;
the argument is not a projection onto a scalar energy or marker.

The architecture still has 32N-1 stored coordinates. It uses one extra
local gate per macrostep, depth five rather than four, a predetermined
receiver role, and the explicitly chosen three-cycle on ordered matter.
No additional initial energy is required. This accounting does not mean
the new control law has no cost or is forced by the preceding dynamics.
Increasing N still increases the number of stored coordinates.

There is also an exact restriction on what a cell-only reader could
achieve without changing the law. In the predecessor four-layer law, the
target's complete cell at boundary N+1 is its initial (R,0,0,0). Therefore
any fixed function of that complete cell which reads zero initially must
read zero at N+1. Merely changing the reader cannot provide an uninterrupted
longer record in that prepared family. Moving the released resource along
channels changes no coordinate in that local input. An external channel,
past history or time-dependent interpretation would enlarge the contract.

The same restriction applies to the present construction at N+3: its
complete receiver cell is again exactly its initial cell, although the
global state differs because q_(N-2)=2 and the source has changed. No
fixed function of this cell alone can distinguish those two local inputs.
The added cycle delays this exact local reset; it does not eliminate it.

## 6. Every single cut prevents the record for all time

Fix any j in {0,...,N-2}. Define V_N^(cut j) by replacing both A_j and
B_j with identities, leaving every other factor, including K, unchanged.
The stored q_j is retained and fixed. This is a separate fixed cut law,
compared on the identical preparation; it is not a switch introduced after
observing an event or deletion of a channel coordinate.

The downstream component comprises cells j+1,...,N-1 and channels
q_(j+1),...,q_(N-2). Its prepared state is zero in all raw fields,
spectators and resources, with intermediate ZM and target R. There is
no remaining primitive connection to cells 0,...,j or to stored q_j.
Each intermediate G fixes ZM. Target G rejects its unfunded zero-field
R branch. K fixes target R. Every remaining contact exchanges two
zeros, and every F fixes its zero field. Thus every primitive fixes this
entire prepared component. Induction over primitives and macrosteps gives

```text
c(N-1)^(cut j)(k)=(R,0,0,0)           for every k>=0,
Read(c(N-1)^(cut j)(k))=0             for every k>=0,
q_j^(cut j)(k)=0                     for every k>=0.
```

This includes j=0, j=N-2 and the sole cut for N=2. The assertion concerns
the identical prepared receiver and passive downstream states, not
arbitrarily excited downstream inputs. Its all-time force comes from an
invariant complete component, not a finite no-record trajectory search.

## 7. Global invariants, locality and finite recurrence

For arbitrary full states, every G and F preserves energy, actual charges
and Gauss defects. Section 2 proves the same for K. Every contact swaps
two nonnegative resources with equal energy weight one and touches no
field or matter. Each layer and V_N therefore preserve H_N and every
charge/defect entry, not merely their sum over cells. Every inverse layer
has the same invariants, and no coordinate or old channel content is
discarded. These statements survive any stated cut, whose inverse simply
reverses the retained factors and replaces K by K^-1.

On the stored-block path

```text
C0--Q0--C1--Q1--...--Q(N-2)--C(N-1),
```

G, K and F act inside cell blocks and have radius zero. A and B are two
nearest-neighbour matchings. A complete forward or inverse step therefore
has dependency radius at most two contact-graph edges, and k steps at most
2k. The depth is five, independent of N; a cut cannot enlarge the bound.
The boundary role is preselected and entails no global lookup during a
step. This is a locality statement for the declared blocks, not a
single-electric-edge implementation theorem or physical speed claim.

The energy shells at fixed finite N remain finite. The inherited
quadratic form obeys Q(v)>=||v||^2, and directly from the displayed C,

```text
4Hraw(E,M)=||2E+CM||^2+M0^2+(M0+M1)^2.
```

For a fixed total energy, positivity bounds every matter and spectator
coordinate, the two magnetic coordinates, then the four electric
coordinates, and all nonnegative resources. Finitely many integer
coordinates with those bounds give a finite shell. The energy-preserving
bijection V_N restricts to a permutation of that shell, so every full
orbit is periodic from its initial state, without a transient tail. The
same is true for every fixed cut law. The field period five and local
cycle period three do not by themselves give the full orbit period.

In particular, any prepared Read=0 state must recur on its uncut orbit.
A permanent positive record along that whole orbit is impossible for this
fixed state-only reader. Adding finitely many registers with finite
energy shells would not remove the same general recurrence obstruction.
Here the sharper first-loss result N+3 follows from the explicit local
transition, independently of any global recurrence bound.

## 8. Exact scope

The theorem is a conditional L1 construction for all finite N>=2 and all
integer w with H(w)=1 under the specified preparation and new five-layer
law. It retains the exact first delivery N-1 and first receiver G-reaction
N, and supplies one fixed cell-only reader whose first positive interval
has length three, with every individual cut preventing any positive read
forever. All stored coordinates, initial energy 41, local phases and the
first reset are accounted for.

The result is a bounded readable event distinction in actual stored matter.
It is not a permanent latch, fault-tolerant memory, independently justified
physical reading, optimized retention, minimal implementation, arbitrary
source-preparation theorem, or repeated-event protocol. The three-step
choice is not claimed to be unique or optimal. No infinite-network limit,
charge transport, native-U coupling, selection by J, or identification of
propagation speed with physical light speed is established. The reader
and the added phase gate are declared choices, and no Canon promotion is
performed by this construction or by a subsequent finite executable audit.

## Appendix: a containing box for the finite H=1 seed audit

The following exact decomposition and bounds are recalled from
`notes/C-FIELD-FINITE-CHAIN-FIRST-DELIVERY-N/SCOPE.md` at the pinned
dependency commit. They delimit a finite audit, not the theorem's
quantifier over all admitted w. For w=(a,b,c,d),

```text
4H(w)=||C(2a+c,2b+d)||^2+c^2+(c+d)^2.
```

If H(w)=1, every squared term is nonnegative, so |c|<=2 and |c+d|<=2,
hence |d|<=4. Writing x=2a+c and y=2b+d, the displayed C gives
||C(x,y)||^2=(x-y)^2+x^2+2y^2. Thus |2a+c|<=2 and |2b+d|<=2.
The triangle inequality then gives |a|<=2 and |b|<=3. Consequently every
integer H(w)=1 seed belongs to

```text
[-2,2] x [-3,3] x [-2,2] x [-4,4].
```

Filtering this whole box by exact H=1 is therefore exhaustive in w. The
predecessor's reported count of 20 seeds is exposed prior audit knowledge;
neither this containment argument nor the all-N theorem assumes that count.
No new enumeration is asserted by this appendix.
