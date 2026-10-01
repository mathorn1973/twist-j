# First delivery and first work on every finite open chain

NON-CANONICAL / L1. Local conditional candidate-T analytical note.
Candidate: C-FIELD-FINITE-CHAIN-FIRST-DELIVERY-N. No Canon authority.

This is a separate extension of the finite-chain template in PR #1310,
not a restatement of that PR's earned three-cell work scope. Its exact
dependency is
`notes/C-FIELD-THREE-CELL-DELAYED-TRANSFER-N/PROOF.md` at commit
`dd354e3e01ad7f7bb535f33e012c5ef1b46a87d2`. That dependency and its local
field/reaction inputs remain NON-CANONICAL candidates. Public authority
remains Public Canon v95 at its existing scope.

The user supplied the contact equations, induction, proposed first times,
constant-energy account and downstream cut argument before this work. They
are known candidate proof input, not independently predicted outcomes. This
note makes their quantifiers, complete states and boundary cases explicit.
It reports analytical reasoning only; it claims no new scientific execution
or independent computational reproduction. It does not reopen or alter the
predecessor's frozen scope, verifier or records.

## 1. Carrier and inherited local law

Fix an integer N>=2. Cell i, for 0<=i<N, stores

```text
ci=(mi,bi,zi,ri),
mi=(mi0,mi1,mi2) in (Z^4)^3,
bi=(bi0,bi1,bi2) in (Z^4)^3,
zi=(Ei,Mi) in Z^4 x Z^2,
ri in Z_{>=0}.
```

There are also N-1 separately stored neutral channel resources
q0,...,q(N-2) in Z_{>=0}. The complete ordered state is

```text
s=(c0,...,c(N-1),q0,...,q(N-2)).
```

Each cell has 31 coordinates. The whole state therefore has
31N+(N-1)=32N-1 coordinates: 30N unrestricted integers and 2N-1
nonnegative resources. Equality always means literal equality of these
coordinates. Cells have disjoint matter, field and electric-graph vertices;
the channel graph is a graph of stored blocks, not an electric boundary.

For completeness the local definitions needed below are restated from the
pinned predecessor. For v in Z^4 let Q(v)=v^t K v and chi(v)=sum_j v_j,
where

```text
K=[[6,2,-1,2],[2,6,2,-1],[-1,2,6,2],[2,-1,2,6]],
C=[[1,-1],[-1,0],[0,1],[0,1]],
D=[[1,1,1,0],[-1,-1,0,-1],[0,0,-1,1]], DC=0,
Hraw(E,M)=E^t E+M^t M+E^t C M,
Hcell(m,b,z,r)=sum_j Q(mj)+sum_j Q(bj)+Hraw(z)+r,
H_N(s)=sum_i Hcell(ci)+sum_j qj.
```

The electric edges in each cell are (0->1,0->1,0->2,2->1), with
the two parallel edges distinct. Each cell's three reacting registers are
at its vertex 0; its spectator registers are at vertices 0,1,2. Thus

```text
rho_i=(chi(bi0)+sum_j chi(mij),chi(bi1),chi(bi2)),
defect_i=D Ei-rho_i.
```

There are 3N actual charge entries and 3N defect entries. They are functions
of the stored state, not quantities obtained by discarding a field component.

Write A_field for the active field matrix, to distinguish it from the
contact layer mathcal A below. For x=(a,b,c,d) and sigma=(u,v), define

```text
P(a,b,c,d)=(a-b,-a,b,b,c,d),
S(u,v)=(u,u,v,u-v,0,0),
A_field=[[1,0,1,0],[0,1,0,1],[-2,1,-1,1],[1,-3,1,-2]],
L=[[1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]],
H(a,b,c,d)=2a^2-2ab+3b^2+c^2+d^2+2ac-ad-bc+3bd,
T(E,M)=(E+CM,M-C^t(E+CM)).
```

The exact certificates in Sections 1-3 of the pinned predecessor establish

```text
Hraw(Px+S(u,v))=H(x)+3u^2-2uv+2v^2,
DP_E=0, TP=P A_field, TS=S,
H(A_field x)=H(x), A_field^5=I,
L A_field=A_field L, H(Lx)=5H(x),
T^-1(E',M')=((I-CC^t)E'-CM',M'+C^t E').
```

In particular T is an integer automorphism preserving Hraw and DE.
P and S give a unique rational split z=Py+S sigma. For raw
z=(E0,E1,E2,E3,M0,M1), this split is

```text
y=((2E0-3E1+E2+E3)/5,(-E0-E1+2E2+2E3)/5,M0,M1),
sigma=((2E0+2E1+E2+E3)/5,(E0+E1+3E2-2E3)/5).
```

Integral split admission is literal; no rounding is allowed. If the split
is integral and y=(a,b,c,d), then y lies in L Z^4 exactly when
a+2b and c+2d are divisible by5. Its unique preimage is
x=(A_field^2 L)y/5. These are inherited exact algebraic certificates,
not new computational observations in this note.

The literal matter endpoints are

```text
R=((1,-2,1,0),(0,0,0,0),(0,0,0,0)),
AM=((1,0,0,0),(0,-1,0,0),(0,-1,1,0)),
ZM=((0,0,0,0),(0,0,0,0),(0,0,0,0)).
```

Their matter energies are respectively 18,20,0. The R and AM register
sums both equal (1,-2,1,0), of chi zero, and ZM is neither endpoint.
For integer x,sigma and arbitrary spectators b, the total local gate G is

```text
(R,b,PLx+S sigma,r) -> (AM,b,Px+S sigma,r+4H(x)-2),
    when r+4H(x)-2>=0;
(AM,b,Px+S sigma,r) -> (R,b,PLx+S sigma,r+2-4H(x)),
    when r+2-4H(x)>=0.
```

All other full inputs are fixed. This includes off-endpoint matter,
nonintegral splits, failed R-side image admission and insufficient funding.
No partial update, resource clipping or clearing occurs. The endpoint
pairs are disjoint by the unique split, injectivity of L and literal matter
labels. Each funded pair is exchanged, so G^2=I on the complete carrier.
Its exact resource/matter/active-field energy identity is

```text
18+5H(x)+r = 20+H(x)+(r+4H(x)-2).
```

Spectators and static fields are retained on both sides. G also preserves
the reacting-register vector sum and DE. The local free operation is
F(m,b,z,r)=(m,b,Tz,r), with the displayed inverse of T.

## 2. The same four layers and their exact contact map

For 0<=j<=N-2 let

```text
A_j=swap(rj,qj), B_j=swap(qj,r(j+1)).
```

These exchange entire contents, including an occupied old channel or
receiving resource. Define layers mathcal G, mathcal A, mathcal B and
mathcal F by applying all G_i, all A_j, all B_j and all F_i, respectively.
Within each layer the supports are disjoint. The chronological schedule is

```text
mathcal G; mathcal A; mathcal B; mathcal F.
U_N=mathcal F mathcal B mathcal A mathcal G.
```

Composition in the second line acts from right to left. Its inverse is

```text
U_N^-1=mathcal G mathcal A mathcal B mathcal F^-1,
chronologically: mathcal F^-1; mathcal B; mathcal A; mathcal G.
```

Adjacent inverse factors cancel; no gate/contact commutation is assumed.
Every resource remains nonnegative and every old coordinate is retained by
the complete bijection.

Let rhat_i denote the resources immediately after mathcal G, and let q_j
denote the old channels, unchanged by that layer. Immediately after
mathcal A, the resources are q_i for i<N-1 and rhat_(N-1) for i=N-1;
the channels are rhat_j. Applying mathcal B gives exactly

```text
r'_0=q_0,
r'_i=rhat_(i-1)                       for 1<=i<=N-1,
q'_j=q_(j+1)                         for 0<=j<=N-3,
q'_(N-2)=rhat_(N-1).
```

mathcal F changes none of these values. When N=2, the range 0<=j<=N-3
is empty. These equations hold for every full input, including occupied
channels. They are a resource permutation after the reaction layer; the
reaction layer itself exchanges resources with matter/field energy.

## 3. The all-length first-delivery theorem

Fix any w in Z^4 satisfying H(w)=1. The assertion is uniform in this w;
it does not require choosing only the predecessor's displayed example.
Prepare

```text
c0(0)=(R,0,PLw,0),
ci(0)=(ZM,0,0,0)                     for 1<=i<=N-2,
c(N-1)(0)=(R,0,0,0),
qj(0)=0                             for 0<=j<=N-2.
```

Every zero denotes the full appropriate tuple: all spectator registers,
all six raw-field coordinates, or the stated resource. Put s(k)=U_N^k s(0)
for nonnegative integer k. Times below count complete macrosteps from this
initial state. Define first delivery as the least k>=0 with
r_(N-1)(k)>0, and first target reaction as the first step in which its
local G changes the target matter.

**Theorem.** For every N>=2 and every such w, the complete states through
k=N are precisely the following:

| Coordinates | k=0 | 1<=k<=N-1 | k=N |
| --- | --- | --- | --- |
| Source matter m0 | R | AM | AM |
| Source field z0 | PLw | P A_field^k w | P A_field^N w |
| Intermediate matter mi, 1<=i<=N-2 | ZM | ZM | ZM |
| Target matter m(N-1) | R | R | AM |
| All fields zi, 1<=i<=N-1 | 0 | 0 | 0 |
| All spectators bi | 0 | 0 | 0 |
| Resources ri, 0<=i<=N-1 | 0 | 2 if i=k, otherwise 0 | 0 |
| All channels qj | 0 | 0 | 0 |

Empty intermediate ranges have their ordinary empty meaning. Therefore

```text
t_delivery(N)=N-1,
t_reaction(N)=N.
```

Both are first times for this preparation and schedule, not an optimization
over alternative laws or preparations. The total initial energy is 41 for
every N. All actual charges and all Gauss defects are zero throughout.

**Proof: initial step.** The source has admitted field PLw, h=H(w)=1
and r0=0. Its gate gives (AM,0,Pw,2). Each intermediate ZM gate fixes
the complete input. The target has R, h=0 and no resource, so its proposed
output resource would be -2 and it rejects. Thus rhat0=2, all other
rhat_i=0 and all q_j=0. The exact contact map places the two units in r1
and leaves every other resource and channel zero. The free layer sends
Pw to P A_field w and fixes every zero field. This proves the table at
k=1, including N=2 where cell 1 is already the target. The target's reaction
was evaluated before that step's contacts and hence it is still R.

**Proof: moving through an intermediate cell.** Suppose the table holds
at some boundary k with 1<=k<N-1. The only nonzero resource is r_k=2.
Cell k is intermediate because k<=N-2; its matter is ZM and its gate fixes
the full input regardless of this resource. All other intermediate gates
also fix their full inputs. The source is AM, r0=0 and its active field
coordinate is x=A_field^k w, with H(x)=1. Its reverse branch would leave
0+2-4=-2, so the entire source is fixed by G. The target is R with zero
field and zero resource, and again rejects its unfunded h=0 branch.
Consequently rhat_i=r_i for all i. The contact map moves the two units
from r_k to r_(k+1), while every other resource and channel stays zero.
The free layer gives z0=P A_field^(k+1)w and retains all other zero fields.
This is the complete table at k+1.

Induction proves the table through k=N-1. It requires no distinctness of
the source field phases: even when A_field^k repeats, its energy is one
and its reverse remains underfunded. For N=2 the induction interval is
empty, and the initial-step argument already proves the needed boundary.

**Proof: first target reaction.** At boundary N-1 the only resource is
r_(N-1)=2 and the target is still R with zero field. In step N its G uses
x=0 and maps (R,0,0,2) to (AM,0,0,0). The source still has active energy
one and no resource, so its reverse rejects. All intermediate gates fix
ZM. Every resource and channel is now zero, so contacts exchange zeros;
the free layer sends the source to P A_field^N w and fixes all other
fields. This proves the final column. At all earlier boundaries the
target resource was zero until N-1, and every earlier target G rejected.
The two times are therefore exact first times, completing the proof.

For the smallest case N=2 the contact formula reads

```text
(rhat0,rhat1,q0) -> (q0,rhat0,rhat1).
```

Boundary 1 has source AM/field P A_field w, target R/r1=2 and q0=0.
Boundary 2 has source AM/field P A_field^2 w, target AM/r1=0 and q0=0.
This is the two-cell restriction of the new four-layer schedule in #1310.
In #1308 the target gate followed the contacts; that older complete step
is a different law and its timing is not imported here.

## 4. Complete energy account and the limit of first work

The initial source energy is 18+H(Lw)=18+5=23, the initial target energy
is 18, and every intermediate cell and channel has energy zero. Thus

```text
H_N(s(0))=23+18=41.
```

At boundaries 1<=k<=N-2, the source has energy 20+1=21, the target 18,
and the intermediate cell k holds two resource units. The account is
21+18+2=41. This boundary interval is empty when N=2.
At boundary N-1 the account is source 21 and target 18+2=20, with all
intermediate and channel energies zero. At boundary N the account is
source 21 and target 20, now entirely matter energy at the target. Thus
arrival and use have equal target total energy but different literal
target states. There is no extra initial energy proportional to distance.
There are extra stored coordinates proportional to distance.

All spectator registers remain zero. The R and AM matter sums have chi zero,
all intermediate matter is zero, and every nonzero field is in P Z^4.
Since DP_E=0, all actual charges and defects are zero in the entire table.
This includes the source's evolving six raw-field coordinates, not only a
scalar resource or energy projection.

The theorem does not assert permanent activation. Indeed its own final
state determines the next target gate: in step N+1 the target is AM with
x=0 and r=0, so the reverse branch releases two units and returns it to R.
The A layer does not touch r_(N-1), and B_(N-2) swaps those units into
the formerly empty q_(N-2). At boundary N+1 the target is again
(R,0,0,0); all cell resources are zero, q_(N-2)=2, and all other channels
are zero. The source remains AM with field P A_field^(N+1)w. Hence even
this immediate continuation rules out interpreting the first reaction as
an irreversible event or a persistent stored record.

## 5. Every individual cut fixes the downstream complete state

Fix any j in {0,...,N-2}. Define U_N^(cut j) by replacing both A_j and
B_j with identities. All other operations and their order are unchanged.
The stored q_j remains present and fixed. This is a separate fixed law,
compared to U_N on the identical preparation s(0), not a switch changed
during the run and not deletion of a resource coordinate.

Consider the downstream component consisting of cells j+1,...,N-1
and channels q_(j+1),...,q_(N-2). Its initial state has only ZM
intermediate matter, target matter R, zero raw fields, zero spectators,
zero cell resources and zero internal channels. No remaining primitive
connects it to cells 0,...,j or to stored q_j.

Every primitive on this component fixes that initial full state. Each
intermediate G fixes its ZM input. The target G has R, x=0 and r=0
and rejects. The F operations fix zero fields. Every remaining contact
exchanges two zeros. It follows, by induction over primitives and then
over complete steps, that the entire component is exactly fixed for all
k>=0, independently of all upstream dynamics. In particular

```text
c(N-1)^(cut j)(k)=(R,0,0,0)           for all k>=0,
q_j^(cut j)(k)=q_j(0)=0              for all k>=0.
```

This proves all N-1 individual cuts with one argument. For j=N-2 the
component is only the target; for j=0 it contains every cell after the
source; for N=2 these are the same sole cut. Empty internal-channel or
intermediate-cell ranges cause no exception. The claim concerns this
prepared downstream component, not arbitrary excited target preparations.
No bounded trajectory search is needed to conclude that target delivery
and reaction never occur under these cut laws.

## 6. Invariants, fixed depth and recurrence

These structural statements are inherited from the predecessor's template
and apply to every full state, not only the preparation in Section 3.
Each G_i is an involution preserving complete Hcell, the spectators,
the reacting-register vector sum, each actual charge and DE. Each F_i
is an integer bijection with the same energy, charge and defect invariants.
Every contact is an involution exchanging two nonnegative resources with
equal energy weight 1. It preserves their sum and touches no field, matter
or charge. Consequently every primitive, layer boundary, U_N and U_N^-1
preserves H_N and every charge/defect entry. The same is true after a
cut replaces two contact factors with identities; the inverse simply
reverses the remaining factors. No old channel contents are discarded.

The sequential depth is four for every N. On the stored-block path

```text
C0--Q0--C1--Q1--...--Q(N-2)--C(N-1),
```

G and F act within a cell block and have radius 0; A and B are two
nearest-neighbour matchings of radius 1. One complete forward or inverse
step has dependency radius at most2 contact-graph edges; k steps have
radius at most2k. Removing contacts cannot enlarge that bound. This is
a dependence bound for the declared blocks. It does not assert a
single-electric-edge implementation of G or F, or a measured physical
speed. The theorem's travel time grows with N despite fixed depth per step.

For every fixed finite N, the conserved energy shells are finite. The
matrix K obeys Q(v)>=||v||^2, and

```text
4Hraw(E,M)=||2E+CM||^2+M0^2+(M0+M1)^2.
```

On a shell H_N=E_star, positivity bounds every matter and spectator
coordinate. The square identity bounds M0 and M0+M1, hence M1, and
then bounds E through 2E+CM. Every nonnegative resource is at most
E_star. With finitely many integer coordinates, only finitely many
complete states are possible. The energy-preserving bijection U_N
restricts to a permutation of that finite shell, so every orbit is periodic
from its initial state, without a transient tail. The same argument holds
for each fixed cut law. No common period bound across N, and no period
of this preparation, is asserted or inferred from A_field^5=I.

## 7. Exact scope of the extension

The new analytical claim is first boundary delivery at N-1 and first
target reaction in step N for all finite N>=2 and all integer H(w)=1
under the specified preparation, with the complete-state and all-cut
statements above. The proof is conditional on the inherited local law and
its exact certificates. A bounded executable audit, if separately prepared
and run, can check formulas and implementation but cannot replace this
induction over unbounded N. No such new execution is claimed here.

The cells, ordered path, neutral channels, energy weights, literal matter
endpoints and four-layer update order remain declared architectural choices.
The common local template defines a family of different finite state-space
dimensions, not one unchanged finite architecture accommodating all N.
The result transports energy without transporting charge. It supplies no
permanent record, infinite-network dynamics, derivation of the transfer law
from J, native-U compatibility or identification of its propagation rate
with physical light speed. Those boundaries and the NON-CANONICAL L1
status remain in force.
