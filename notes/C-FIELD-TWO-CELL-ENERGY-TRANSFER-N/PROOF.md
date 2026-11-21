# Two disjoint L5 cells with a stored neutral exchange channel

PUBLIC / NON-CANONICAL. Action layer: L1. Authority: none.
Candidate C-FIELD-TWO-CELL-ENERGY-TRANSFER-N, issue #1307.
This proof uses the frozen PREREG at
9a6f128172c9efa37f77ca05e1861a9d6f241845, SHA-256
b3ad38c5af85519c8cdc9e8dbbd1a5549c6d6c28046caf85b9f3e2be48c39fc4.
Universal algebraic statements are distinguished from the later finite audit.

## 1. Provenance, inherited facts and the new construction

The public authority basis is Canon v95, content
5a1dd8ba6c339640940b5a013d3c412025a1f8fc, at public main
b8ba1a07ad776cdd8d878fe0a407e07312c0e263. Its Canon SHA-256 is
b4ebf2ffc7393b703d65ce62cf3e0ee382e7309a563d99ec866ee3fa82f9ba7f.
The inherited canonical inputs are INTEGER-F-JG-INVARIANTS for the chosen
matter chart, quadratic family and additive charge; INTEGER-ENERGY-FUNDED-
INVOLUTION for funding and reverse-order composition; FIELD-GAUSS-CONTACT-
MEMORY for actual pointwise defect bookkeeping; and FIELD-EISENSTEIN-
RESONANCE for the selected R18/A20 matter energies. The generic lift and
these endpoint energies are not new results here.

The one-cell source is unmerged draft PR #1306 at
869998eb8c1c68f7a884fafbf683bf20db0eb7f1, whose proof SHA-256 is
58cc146e07a32dd36119cb9caf52e9c58c1137d7216fb0f48ba264e8da272861.
Its field source is unmerged PR #1304 at
dcfde46760bdfd4551686be1e99b5433fa6e9adf. These are reviewed
NON-CANONICAL candidate inputs, not Canon authority. The needed definitions
and algebraic certificates are restated below. No predecessor executable,
private archive or runtime network source is required.

The new object is a specified composition of two disjoint copies of that
cell and two contacts with one neutral channel. Its witnesses demonstrate
energy leaving one complete cell and paying a reaction in the other, with
an exact full-state inverse and a matched disabled-channel control. The
channel, its energy weight, the ordered roles and the schedule are declared
construction choices. They are not selected by the inherited field theorem.

This proof was written from the frozen preregistration, the public
predecessor proof and repository rules, without reading either new
implementation or executing or importing scientific code. The witness
accounts and period-five table were already exposed symbolic targets;
this is not a claim of blind prediction. Implementation independence is a
separate property of the executable audit.

## 2. Literal 63-coordinate carrier and complete energy

A cell state is (m,b,z,r). Its ordered reacting triple m consists of three
Z4 vectors, all at vertex0. Its spectator triple b consists of three Z4
vectors at vertices0,1,2 respectively. The raw field is
z=(E0,E1,E2,E3,M0,M1) in Z6, and r is a neutral integer in Z>=0 at vertex0.
The source and target use disjoint copies, with vertex labels (s,j),(t,j).
The complete joint state is (ss,st,q), where q is one stored neutral integer
in Z>=0. Thus there are 60 unconstrained integer coordinates and three
nonnegative resource coordinates. Equality is literal on all 63 coordinates.
There is no quotient by field phase, charge, energy, endpoint or routing.

Each cell has ordered electric edges (0->1,0->1,0->2,2->1), the first two
being distinct parallel edges, and faces e0-e1 and -e0+e2+e3. With +tail/-head,

```text
C=[[1,-1],[-1,0],[0,1],[0,1]],
D=[[1,1,1,0],[-1,-1,0,-1],[0,0,-1,1]], DC=0,
K=[[6,2,-1,2],[2,6,2,-1],[-1,2,6,2],[2,-1,2,6]],
chi(v)=sum_j v_j, Q(v)=v^t K v,
Hraw(E,M)=E^t E+M^t M+E^t C M,
Hcell(m,b,z,r)=sum_j Q(mj)+sum_j Q(bj)+Hraw(z)+r,
Hjoint(ss,st,q)=Hcell(ss)+Hcell(st)+q.
```

The canonical four-phase matter chart is not identified with the four
active field coordinates introduced below. K has eigenvalues 9,1,7,7:
its constant and alternating vectors have eigenvalues9 and1, and their
orthogonal complement has eigenvalue7. Hence Q(v)>=||v||^2. Since
C^t C=[[2,-1],[-1,3]], direct completion of squares gives

```text
4Hraw(E,M)=||2E+CM||^2+M0^2+(M0+M1)^2.
```

This is positive definite: vanishing makes M0=M1=0 and then E=0.
Hjoint is consequently a nonnegative integer and counts all matter,
spectator, static and active field, cell-resource and channel energies.
There is no external energy account.

For each cell define its actual node charges and field defect by

```text
rho=(chi(b0)+sum_j chi(mj),chi(b1),chi(b2)), defect=DE-rho.
```

The joint electric boundary is diag(D,D). The channel q is an added neutral
energy coordinate, not an electric edge or an unstored charge. Joint Gauss
means that both three-component defects vanish. We will preserve each actual
rho and each defect separately, including initially nonzero defects.

## 3. Local field certificates and exact admission

For active x=(a,b,c,d) and static s=(u,v), set

```text
P(a,b,c,d)=(a-b,-a,b,b,c,d), S(u,v)=(u,u,v,u-v,0,0),
A=[[1,0,1,0],[0,1,0,1],[-2,1,-1,1],[1,-3,1,-2]],
B=[[4,-2,2,-1],[-2,6,-1,3],[2,-1,2,0],[-1,3,0,2]],
H(x)=x^t B x/2
    =2a^2-2ab+3b^2+c^2+d^2+2ac-ad-bc+3bd,
L=[[1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]],
N=[[1,2,1,2],[2,-1,2,-1],[0,-5,1,-3],[-5,5,-3,4]].
```

The unique rational solution of z=Py+Ss is

```text
a=(2E0-3E1+E2+E3)/5, b=(-E0-E1+2E2+2E3)/5, c=M0, d=M1,
u=(2E0+2E1+E2+E3)/5, v=(E0+E1+3E2-2E3)/5.
```

Substitution proves both inverse identities. If g=2E0-3E1+E2+E3, the
four electric numerators are respectively g,2g,g,3g modulo5. Therefore the
split is integral exactly when g=0 mod5. The residue map is onto Z/5, since
its E2 coefficient is one, so the integral split sublattice has index5.
Admission must precede division; this does not project nonsplit states onto
an integer subspace. Separately, PZ4 is saturated because
(-E1,E2,M0,M1) is an integer left inverse on its rational span. SZ2 is
saturated because its coordinates are E0=E1=u,E2=v,E3=u-v,M=0.

Direct substitution gives

```text
DP_E=0, C^t S_E=0,
DS_E(u,v)=(2u+v,-3u+v,u-2v),
Hraw(Py+Ss)=H(y)+3u^2-2uv+2v^2.
```

The cross terms vanish since the active electric columns lie in im C and
the static electric columns are orthogonal to it. H is positive definite
by injectivity of P and positivity of Hraw. On integer x, H(x) is integral;
in particular H(x)>=1 for x!=0.

The free field map and its inverse are

```text
T(E,M)=(E+CM,M-C^t(E+CM)),
T^-1(E',M')=((I-CC^t)E'-CM',M'+C^t E').
```

They are inverse integer shears. Expanding Hraw after the two shears gives
Hraw(Tz)=Hraw(z). Also DT_Ez=DE by DC=0, and substitution gives TP=PA,
TS=S and A^t B A=B. An exact order certificate is

```text
Jcyc=[[0,1,0,0],[0,0,1,-1],[1,-1,0,-1],[0,1,-2,1]], det Jcyc=-1,
Z=[[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]], A Jcyc=Jcyc Z.
```

Z is multiplication by t in Z[t]/(1+t+t^2+t^3+t^4), so A^5=I. The
rational split spans the raw six-dimensional space; hence T^5=I on every
raw integer field, including nonsplit fields.

Matrix multiplication gives L=(I-A)(I-A^2), AL=LA, N=A^2 L and
LN=NL=5I. These identities may also be seen from
(1-t)^2(1-t^2)^2=5t^3 modulo 1+t+t^2+t^3+t^4. Since A is a B-isometry,
the B-adjoint of L is A^-3 L=A^2 L=N. Consequently L^t B L=5B and
H(Lx)=5H(x). For completeness an integer image certificate is

```text
V=[[1,1,1,1],[2,1,2,1],[0,-1,1,0],[-5,-2,-3,-1]], det V=1,
L V=[[5,3,0,0],[0,1,0,0],[0,0,5,3],[0,0,0,1]].
```

It proves det L=25 and that y=(a,b,c,d) lies in LZ4 exactly when
a-3b and c-3d are divisible by5, equivalently a+2b=c+2d=0 mod5.
Only on this image is x=Ny/5 the unique integer preimage. Indeed NL=5I
gives the necessary formula and L(Ny/5)=y gives sufficiency on admission.
The image index25 is distinct from the raw split index5. Its 25 classes
among the 625 active residue representatives do not describe an energy
shell. For example H(0,0,1,-2)=5 but c+2d=-3 is not divisible by5.

## 4. Total local gate, complete inverse and local invariants

Fix the literal ordered matter endpoints

```text
R=((1,-2,1,0),(0,0,0,0),(0,0,0,0)),
AM=((1,0,0,0),(0,-1,0,0),(0,-1,1,0)).
```

Their full vector sums both equal (1,-2,1,0), their additive Q energies
are18 and20, and their total chi is zero. The three individual register
charges change from (0,0,0) to (1,-1,0); they are not separately conserved.
All three reacting registers occupy the same vertex, so their sum preserves
the actual charge at that vertex. Other phases and permutations are not
identified with these endpoints.

For every integer x,s and every spectator triple b, pair
(R,b,PLx+Ss) with (AM,b,Px+Ss). Unique splitting, injective L and disjoint
matter endpoints make these disjoint two-element pairs, including x=0.
Their non-resource energies differ by2-4H(x) from the R side. Funding this
pair defines G by

```text
(R,b,PLx+Ss,r)  -> (AM,b,Px+Ss,r+4H(x)-2), if r+4H(x)-2>=0;
(AM,b,Px+Ss,r) -> (R,b,PLx+Ss,r+2-4H(x)), if r+2-4H(x)>=0.
```

G fixes the entire input upon any endpoint, raw-split, R-side image or
funding failure. There is no partial write. The inverse of every accepted
branch is the other branch: the second resource update recovers r>=0 and
the field maps recover x,s exactly. Every rejected state repeats its same
rejection. Thus G^2=I on the full declared cell carrier.

Writing h=H(x), the complete energy identity on an accepted R branch is

```text
18+5h+r+sum Q(bj)+Hstatic(s)
 =20+h+(r+4h-2)+sum Q(bj)+Hstatic(s).
```

The opposite branch reverses this identity. Static fields, spectators and
their energies remain stored. The resource guard ensures nonnegativity.
For h=0, R needs r>=2; for h=1, R deposits2 and its reverse needs2.
This law includes reservoir-funded activation at zero active field.

G preserves the full reacting vector sum and each spectator. Its field
change retains static s and has zero divergence in its active part.
Therefore it preserves actual rho, actual DE and each component of DE-rho,
including states that do not initially satisfy Gauss. F(m,b,z,r)=(m,b,Tz,r)
has the same energy and defect invariants and inverse F^-1 using T^-1.

F and G commute. On split fields, F changes active x to Ax and leaves s
fixed. The identities AL=LA, AN=NA and H(Ax)=H(x) preserve image and
funding decisions and commute with the accepted field updates. Nonsplit
fields remain nonsplit: for all raw fields
g=2(DE)_0+(DE)_2 mod5, and F preserves DE. Off-endpoint matter remains
off-endpoint. This covers fixed and switching branches on the full carrier.

Fixation here is a statement about G alone. A rejected gate input can move
under F, and a contact can change its resource before a later reaction.
No assertion G(s)=s implies U(s)=s is used.

## 5. The two contacts and the complete joint step

Lift Gs,Gt,Fs,Ft to the two cells, acting as identity on the other cell and
on q. Let Xs exchange rs and q, and Xt exchange rt and q, fixing every
other coordinate. Each contact is an involution on arbitrary nonnegative
resources. Their combined action, before considering reaction, is

```text
(rs,q,rt) --Xs--> (q,rs,rt) --Xt--> (q,rt,rs).
```

This is a permutation of whole stored resources. It is not restricted to
two-unit packets, initially empty channels or initially empty receivers.
There is no clearing, direction tag, capacity threshold or lost old value.
For example (2,1,3) goes to (1,2,3) and then (1,3,2); the six energy units
and each original coordinate value remain in the joint state.

With values evaluated immediately before the indicated contact, Xs changes
(Hsource,q) by (q-rs,rs-q), and Xt changes (Htarget,q) by (q-rt,rt-q).
The other cell is fixed at that stage. Thus each contact preserves Hjoint.
Neither touches fields or matter, so each preserves both actual charge
vectors and both defects, all spectators and reacting vector sums.

Apply the specified six forward stages in this exact order:

```text
Gs ; Xs ; Xt ; Gt ; Fs ; Ft,
U=Ft Fs Gt Xt Xs Gs.
```

Each factor is a bijection on the full carrier. Hence the complete inverse
applies Ft^-1 ; Fs^-1 ; Gt ; Xt ; Xs ; Gs. In product notation it is
Gs Xs Xt Gt Fs^-1 Ft^-1. Cancelling adjacent inverse factors proves both
U^-1 U=I and U U^-1=I, without a commutation assumption about the contacts
and reactions. It restores every original coordinate, including any initially
occupied channel and any original target resource.

Every stage separately preserves the full state space, total energy, each
cell's actual rho and defect, spectators and reacting vector sum. These
are therefore invariants of U and its inverse. In particular the joint
Gauss subset is invariant, without imposing zero charges or zero defects
on the larger carrier. No charge is transported through the neutral channel.

The access frames are explicit. G reads its own ordered matter, field and
resource and changes only those coordinates; F reads and changes only its
own field. Xs reads and exchanges exactly (rs,q), and Xt exactly (rt,q).
Neither contact reads the other cell. Their writes to q are serial.
The inverse has the corresponding same finite supports. No field register
is shared between cells; no compatibility of overlapping field updates is
assumed. Fixed source/target roles and stage order belong to the law, not
to a hidden dynamic label or a reader intervention. This gives a complete
map at macrostep boundaries, without constructing an autonomous microstep
clock, a translation-invariant network or a finite-speed propagation law.

The matched disabled-channel control replaces both contacts by identity:
U0=Ft Fs Gt Gs. It is a separately specified bijection with the same energy,
charge and defect invariants. Its preparation is literally the same full
joint initial state; no reader toggles a hidden coordinate during either run.

## 6. Transferred work in the neutral and charged witnesses

Put w=(0,0,1,0). The local formulas give

```text
H(w)=1, Lw=(-1,-2,1,2), PLw=(1,1,-2,-2,1,2),
Pw=(0,0,0,0,1,0), PAw=(1,-1,0,0,-1,1).
```

Start with source (R,0,PLw,0), target (R,0,0,0), q=0. Both actual charge
vectors and defects are zero. The complete staged account is

| Stage | Source matter/resource | Target matter/resource | q | Hsource,Htarget,q |
| --- | --- | --- | ---: | --- |
| Initial | R/0 | R/0 | 0 | 23,18,0 |
| Gs | AM/2 | R/0 | 0 | 23,18,0 |
| Xs | AM/0 | R/0 | 2 | 21,18,2 |
| Xt | AM/0 | R/2 | 0 | 21,20,0 |
| Gt | AM/0 | AM/0 | 0 | 21,20,0 |
| Fs then Ft | AM/0 | AM/0 | 0 | 21,20,0 |

Gs takes source field PLw to Pw. The contacts and Gt leave that field
unchanged, and Fs then gives PAw. The target field remains zero throughout.
The target's zero-active-field R branch requires two resource units, which
it lacks initially and receives through q before its reaction. Gt consumes
those units while raising target matter energy from18 to20. Source energy
has fallen from23 to21; the channel starts and ends empty. All intermediate
energy is accounted for, with constant joint total41.

Under U0, Gs still produces source resource2, but the target never receives
it. Gt therefore fixes the entire target, and Ft fixes its zero field. The
complete output is source (AM,0,PAw,2), target (R,0,0,0), q=0, with the
same total41. This matched control isolates what the contacts enable at
the specified step boundary. It is not just a comparison of energy labels.

The global inverse of the successful witness first undoes the free field
motion, then Gt reverses target activation and restores target resource2.
Xt moves those units into q, Xs returns them to the source, and Gs can then
restore its high field and R endpoint. Attempting Gs reversal while the
source still has resource0 would reject; the full inverse restores the
needed budget before invoking it.

For a nonzero-charge witness, add source static S(1,0), source spectators
(2e0,-3e0,e0), target static S(0,1) and target spectators(e0,e0,-2e0),
where e0=(1,0,0,0). Their static energies are3 and2; their spectator
energies are84 and36. The actual source and target charges are respectively
(2,-3,1) and (1,1,-2), matching their divergences. The target has zero
active field but a retained nonzero static field.

The successive energy triples are (110,56,0), (110,56,0), (108,56,2),
(108,58,0), (108,58,0), with no change at the two free-field stages.
Thus 110+56=108+58=166, and source loss and target gain are again two.
The final source raw field is (2,0,0,1,-1,1); the target raw field remains
(0,0,1,-1,0,0). Both actual charge vectors, all spectator coordinates and
the complete static energies remain present. Under U0 that target's whole
state is fixed, just as in the neutral control.

The source with R and active y=(0,0,1,-2), empty resource and channel,
has the same field energy5 as the successful source. However y is offimage,
so Gs fixes it. The contacts exchange only zeros and the ready neutral
target cannot react. The complete U nevertheless moves the source field:
P y=(0,0,0,0,1,-2) becomes P A y=(3,-1,-2,-2,-3,5). This is an explicit
separation of energetic availability from exact arithmetic admission, and
of reaction-gate rejection from rest under the complete step.

## 7. Exact recurrence of these preparations and general recurrence

Let W=Gt Xt Xs Gs and F=Ft Fs, so U=FW. Each free-field factor commutes
with its local G by Section4 and with the other cell's gate by disjoint
support. It commutes with both contacts because it neither reads nor changes
resources. Hence FW=WF and U^k=F^k W^k. Also F^5=I on the full carrier.

For either witness preparation, suppress the free field motion temporarily.
W first makes both endpoints AM with all resources zero. On the next step
the source reverse gate rejects at resource0 while the zero-active-field
target AM gate releases two. The next two contact passes move those two
units first to q and then to the source. The following source gate has its
required two-unit inverse budget and returns to R and high field. In full,

| k | Source endpoint | Target endpoint | rs,rt,q |
| ---: | --- | --- | --- |
| 0 | R | R | 0,0,0 |
| 1 | AM | AM | 0,0,0 |
| 2 | AM | R | 0,2,0 |
| 3 | AM | R | 0,0,2 |
| 4 | AM | R | 2,0,0 |
| 5 | R | R | 0,0,0 |

This also gives the endpoint/resource table for U, because F changes none
of these coordinates. Put xk=A^k w. The source field under U is PLxk+Ss
at k=0,5 and Pxk+Ss at k=1,2,3,4. Target static field and all spectators
are fixed. Thus k=5 recovers the complete initial state by A^5=I, while
k=1..4 cannot equal it since the source matter endpoint is AM rather than
R. Each of these two preparations has exact period5. The receiver's
activation therefore later reverses. This proof asserts neither U^5=I
nor U^10=I for all states, and performs no search for other periods.

More generally fix an initial total energy E*. Energy conservation keeps
the orbit on that energy shell. Q(v)>=||v||^2 bounds every matter and
spectator coordinate. For each field, the nonnegative-square identity of
Section2 bounds M0 and M0+M1, hence M1, and bounds every component of
2E+CM, hence every component of E. The three nonnegative resources are
at most E*. There are therefore only finitely many integer states on this
shell. Since U is a bijection preserving the shell, its restriction is a
permutation. Every orbit is periodic from its initial state, with no
transient tail. This proves recurrence without a numerical period bound
and without identifying the periods of other preparations.

## 8. Information-retention attacks and scope of the finite audit

The exact contacts retain old contents. In contrast, copying source
resource2 into q while retaining it in the source, at the neutral Gs
output, creates two energy units. The purported send operation
(rs,q)->(0,rs) loses old q and maps inputs (2,0) and (2,1) to the same
output (0,2). Likewise (q,rt)->(0,q) loses old rt and maps (2,0) and
(2,1) to the same output. Each loses one unit on its occupied input and
is noninjective. These are erroneous endpoint formulas, not alternative
laws silently substituted into the construction.

Ordering matters even when conservation survives. If Gt is moved before
both contacts on the same neutral preparation, it sees resource0 and fixes
R; the subsequent contacts leave the target at R with resource2 at this
step boundary. The frozen schedule instead gives AM with resource0.
An energy-only comparison would miss this failure of the work witness.

The universal proof above does not depend on finite enumeration. The
preregistered executable audit checks the displayed algebraic certificates,
the 625 literal active residue representatives with exactly25 image
members, and the 6534 indexed joint fixtures formed from eleven local
templates, six resource pairs, three channel values and three backgrounds.
Those backgrounds include nonzero actual charge and deliberately nonzero
defects. It audits all six substeps, declared access frames, exact contact
accounts, local gate decisions, both complete inverse identities and U0.
Its remaining controls are the explicit witness stages, the fixed six
recurrence states k=0..5 and the specified erroneous endpoint formulas.
These are bounded audits of the proof, not shell classification, parameter
selection, a trajectory census or evidence for every reaction architecture.

## 9. Construction boundary

The result is one explicitly chosen neutral energy exchange between two
disjoint finite cells. The channel's stored content does work elsewhere:
the first cell actually loses two units while the second uses them to
react, and the joint state retains an exact inverse. At the stated scope
this is stronger than an account confined to one isolated cell.

The cell multigraph, matter chart and metric, phase and ordered endpoints,
L5 pairing, neutral resource, channel of weight one, labelled source and
target, serial schedule, preparation and control are all declared choices.
The construction does not derive the channel from native canonical U or
identify its integer energy with measured physical energy. There is no
charge current: all six actual node charges remain fixed. Charge transport
would require a separate continuity and electric-flux construction.

The exact period-five witnesses and finite-shell theorem exclude treating
this result as a terminal activation or permanent record. The law proves
neither network propagation nor overlap compatibility, autonomous clocking,
a detector, finite-speed transport, irreversible emission or a physical
L1--L6 bridge. QDD-INSTRUMENT-APPARATUS, QDD-TERMINAL-EVENT-SEMANTICS
and PHOTON-MASSLESS-PHASE retain their obligations. Any promotion, network
extension or record-persistence claim requires separate work and disposition.
