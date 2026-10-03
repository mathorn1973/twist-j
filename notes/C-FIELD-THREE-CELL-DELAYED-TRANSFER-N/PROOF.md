# Three-cell transfer with a stored intermediate step

PUBLIC / NON-CANONICAL / L1. Candidate proof, not Canon authority.
Candidate: C-FIELD-THREE-CELL-DELAYED-TRANSFER-N.

This proof concerns exactly the carrier and four-layer law in PREREG.md,
publicly frozen at 9e04d722d95f2ad4725ce859164ab8aa8ca5ccdc. It proves a
three-cell work witness with a middle resource at complete-step boundary1,
arrival at boundary2 and receiver reaction at step3. It also proves a
fixed-depth finite-chain wiring template and its support bound; it does not
claim an all-length work theorem. All conclusions are conditional on the
declared architecture, preparations and equality of complete coordinates.

The local field and reaction inputs of #1304, #1306 and #1308 remain
NON-CANONICAL candidate dependencies. The definitions and exact certificates
needed here are restated, so the proof requires no predecessor executable.
Public Canon v95 supplies the earlier matter chart, generic funded-involution
principle and actual Gauss framework at their accepted scopes. This is a
new selected macrostep, not a derivation or continuation of native U.

## 1. Full stored carrier and complete energy

Cell i stores ci=(mi,bi,zi,ri). Here mi=(mi0,mi1,mi2) consists of three
ordered Z4 matter registers at its vertex0, bi=(bi0,bi1,bi2) consists of
three Z4 spectator registers at its vertices0,1,2, zi=(Ei,Mi) is a raw
field in Z4 x Z2, and ri is a nonnegative integer. Cells have no shared
matter, field or electric-graph vertices. Two separately stored neutral
integers q0,q1>=0 connect cells0--1 and1--2. Thus

```text
s=(c0,c1,c2,q0,q1)
```

has 95 coordinates: 90 unrestricted integers and five nonnegative resource
integers. Equality means literal equality of this entire ordered tuple.
No charge, static field, matter phase, endpoint or old channel value is
discarded. The channel coordinates are neutral energy resources, not
electric edges or an implicit charge current.

Each cell uses ordered electric edges (0->1,0->1,0->2,2->1), with the
first two distinct parallel edges, and faces e0-e1 and -e0+e2+e3. For
the +tail/-head convention the matrices and energies are

```text
C=[[1,-1],[-1,0],[0,1],[0,1]],
D=[[1,1,1,0],[-1,-1,0,-1],[0,0,-1,1]], DC=0,
K=[[6,2,-1,2],[2,6,2,-1],[-1,2,6,2],[2,-1,2,6]],
Q(v)=v^t K v, chi(v)=sum_j v_j,
Hraw(E,M)=E^t E+M^t M+E^t C M,
Hcell(m,b,z,r)=sum_j Q(mj)+sum_j Q(bj)+Hraw(z)+r,
Hjoint(s)=Hcell(c0)+Hcell(c1)+Hcell(c2)+q0+q1.
```

K has eigenvalues 9,1,7,7: the constant and alternating vectors have
eigenvalues9 and1, and their orthogonal complement has eigenvalue7. Hence
Q(v)>=||v||^2. Since C^t C=[[2,-1],[-1,3]], completing squares gives

```text
4Hraw(E,M)=||2E+CM||^2+M0^2+(M0+M1)^2.
```

This is positive definite: its vanishing forces M0=M1=0 and then E=0.
Consequently Hjoint is a nonnegative integer accounting for every stored
matter, spectator, active field, static field, cell and channel resource.
No external energy credit enters its definition.

For each cell the actual node charges and Gauss defect are

```text
rho_i=(chi(bi0)+sum_j chi(mij),chi(bi1),chi(bi2)),
defect_i=D Ei-rho_i.
```

The joint electric boundary is diag(D,D,D), with nine actual nodes.
Joint Gauss means that all nine defect entries vanish. The argument below
preserves every entry even when the initial defect is nonzero. The
cell/channel path used for the contact schedule is a separate graph of
stored blocks; it does not replace this electric boundary.

## 2. Exact local field certificates

For active x=(a,b,c,d) and static s=(u,v), define

```text
P(a,b,c,d)=(a-b,-a,b,b,c,d), S(u,v)=(u,u,v,u-v,0,0),
A=[[1,0,1,0],[0,1,0,1],[-2,1,-1,1],[1,-3,1,-2]],
B=[[4,-2,2,-1],[-2,6,-1,3],[2,-1,2,0],[-1,3,0,2]],
H(x)=x^t B x/2
    =2a^2-2ab+3b^2+c^2+d^2+2ac-ad-bc+3bd,
L=[[1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]],
N=[[1,2,1,2],[2,-1,2,-1],[0,-5,1,-3],[-5,5,-3,4]].
```

Solving z=Py+Ss over Q gives the unique coordinates

```text
a=(2E0-3E1+E2+E3)/5, b=(-E0-E1+2E2+2E3)/5, c=M0, d=M1,
u=(2E0+2E1+E2+E3)/5, v=(E0+E1+3E2-2E3)/5.
```

Substitution verifies both inverse identities. If
g=2E0-3E1+E2+E3, the four electric numerators are respectively
g,2g,g,3g modulo5. Thus the split is integral exactly when g=0 mod5.
The residue map is onto Z/5 because its E2 coefficient is one, so the
integral split sublattice has index5. This is an admission test before
division, not permission to round a rational projection. PZ4 is saturated
in its rational span because (-E1,E2,M0,M1) is an integer left inverse;
SZ2 is saturated because its elements have E0=E1=u,E2=v,E3=u-v,M=0.
Their full-rank direct sum still has index5 in the raw lattice.

The active electric vector is C(a,b), while C^t S_E=0. Therefore

```text
DP_E=0, DS_E(u,v)=(2u+v,-3u+v,u-2v),
Hraw(Py+Ss)=H(y)+3u^2-2uv+2v^2.
```

The last identity follows by substitution or by orthogonality of the
active electric and static electric parts. H is positive definite by
injectivity of P and positivity of Hraw. Its displayed polynomial is
integral on Z4, so H(x)>=1 for nonzero integer x.

The free field map and its inverse are

```text
T(E,M)=(E+CM,M-C^t(E+CM)),
T^-1(E',M')=((I-CC^t)E'-CM',M'+C^t E').
```

They are inverse integer shears. Expansion gives Hraw(Tz)=Hraw(z), and
DC=0 gives D(Tz)_E=DE. Direct substitution gives TP=PA, TS=S and
A^t B A=B. An exact finite-order certificate is

```text
Jcyc=[[0,1,0,0],[0,0,1,-1],[1,-1,0,-1],[0,1,-2,1]], det Jcyc=-1,
Z=[[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]], A Jcyc=Jcyc Z.
```

Z is multiplication by t on Z[t]/(1+t+t^2+t^3+t^4), so A^5=I.
Since P and S together span the raw space over Q, T^5=I on every raw
integer field, including those with nonintegral split coordinates.

Multiplication of the displayed matrices gives

```text
L=(I-A)(I-A^2), AL=LA, N=A^2 L, NL=LN=5I.
```

For another algebraic verification, (1-t)^2(1-t^2)^2=5t^3 in the same
cyclotomic quotient. As A is a B-isometry, the B-adjoint of L is
A^-3 L=A^2 L=N. Hence L^t B L=5B and H(Lx)=5H(x). The adjoint here
belongs to B; it is not the ordinary coordinate transpose alone.

The following integral certificate fixes the exact image:

```text
V=[[1,1,1,1],[2,1,2,1],[0,-1,1,0],[-5,-2,-3,-1]], det V=1,
L V=[[5,3,0,0],[0,1,0,0],[0,0,5,3],[0,0,0,1]].
```

It proves det L=25 and shows that y=(a,b,c,d) lies in LZ4 exactly when
a-3b and c-3d are divisible by5, equivalently

```text
a+2b=0 mod5, c+2d=0 mod5.
```

On this admitted image x=Ny/5 is integral and Lx=y; it is the unique
preimage because NL=5I. These congruences are also equivalent to every
coordinate of Ny being divisible by5. Necessity follows from NL=5I;
sufficiency follows from L(Ny/5)=y. Among the 625 literal residue
representatives in {0,1,2,3,4}^4, there are exactly25 admitted vectors,
one choice of a for each b and one of c for each d. This residue count
is not an energy-shell count. In particular H(0,0,1,-2)=5 but its
c+2d=-3 fails image admission.

## 3. Total funded gate and all local invariants

The canonical matter chart and the active field chart are distinct.
The chosen ordered matter endpoints are

```text
R=((1,-2,1,0),(0,0,0,0),(0,0,0,0)),
AM=((1,0,0,0),(0,-1,0,0),(0,-1,1,0)),
ZM=((0,0,0,0),(0,0,0,0),(0,0,0,0)).
```

The sums of the R and AM registers both equal (1,-2,1,0). Their
additive Q energies are18 and20. Their total chi is zero, although
the individual register charges change from (0,0,0) to (1,-1,0).
All three registers occupy the same actual node. ZM is neither endpoint.
Other matter phases and permutations are not equated to either endpoint.

For integer x,s and any spectator triple b, the non-resource endpoints
(R,b,PLx+Ss) and (AM,b,Px+Ss) form a pair. Unique split coordinates,
injective L and the disjoint matter labels make these pairs disjoint.
Define G by the two funded branches

```text
(R,b,PLx+Ss,r)  -> (AM,b,Px+Ss,r+4H(x)-2), if r+4H(x)-2>=0;
(AM,b,Px+Ss,r) -> (R,b,PLx+Ss,r+2-4H(x)), if r+2-4H(x)>=0.
```

On every other input G fixes the entire input. The tests are literal
matter recognition, integral raw split, R-side image admission and then
funding. There is no clipping, partial update or clearing on rejection.

The reverse branch restores the original nonnegative r and every other
coordinate. Thus each accepted pair is a transposition of two full states.
Every rejected state is a singleton: it cannot also be the result of an
accepted branch, since such a result has its admitted funded reverse.
Consequently G^2=I on the full declared carrier.

Writing h=H(x), its exact accepted-branch energy identity is

```text
18+5h+r+sum_j Q(bj)+Hstatic(s)
 =20+h+(r+4h-2)+sum_j Q(bj)+Hstatic(s).
```

The opposite branch reverses this identity. It counts all spectators and
the entire static field; neither disappears into an active-field quotient.
At h=0 the R branch requires two previously stored units, while the AM
branch releases two. At h=1 the R branch deposits two and its reverse
requires two. The zero-active-field funded activation is an explicit part
of the law, not an extra operation introduced for the receiver witness.

G preserves each spectator and the complete reacting-vector sum. It
retains static s and changes only a divergence-free active field part.
It therefore preserves each actual rho, each DE and each component of
DE-rho. F(m,b,z,r)=(m,b,Tz,r) has the same energy and defect invariants
and an exact integer inverse. G need not preserve the three individual
reacting-register charges separately, nor is that required.

For completeness F and G commute locally. On split fields F acts by
x->Ax with s fixed; commutation with L and N and H(Ax)=H(x) preserve
image and funding decisions. On nonsplit fields use
g=2(DE)_0+(DE)_2 modulo5: F preserves this residue and hence nonsplit
rejection. Off-endpoint matter is also unchanged by F. This establishes
commutation on both accepted and rejected branches. It does not make the
new reaction layers commute with resource contacts.

A fixed point of G need not be a fixed point of F or of a complete
network step. Gate rejection and rest under the full law remain distinct.

## 4. Four layers and the complete inverse

Lift Gi and Fi to cell i, fixing all other cells and channels. Define

```text
A0=swap(r0,q0), A1=swap(r1,q1),
B0=swap(q0,r1), B1=swap(q1,r2).
```

Each contact exchanges entire nonnegative contents, including any old
channel value and any old receiving resource. It is an involution. For
the affected cell resource r and channel q its energy increments are
(q-r,r-q), with r and q evaluated immediately before that contact.
The full energy is therefore unchanged at every contact. Fields, matter,
spectators, all charges and all defects are untouched by contacts.

The chronological macrostep is exactly

```text
G0 G1 G2 in parallel;
A0 A1 in parallel;
B0 B1 in parallel;
F0 F1 F2 in parallel.
```

Within each layer the supports are disjoint. Let G=G0G1G2,
A=A0A1, B=B0B1 and F=F0F1F2, using these capital A and B for
contact layers only in this section and later schedule formulas. The
four-dimensional matrices A and B in Section2 retain their earlier
meaning in field formulas. Then

```text
U=F B A G,
U^-1=G A B F^-1.
```

The inverse is applied chronologically as F^-1; B; A; G. Since G,A,B
are involutions, adjacent inverse factors cancel in either product:

```text
(G A B F^-1)(F B A G)=I,
(F B A G)(G A B F^-1)=I.
```

No commutation across contact layers or between contacts and gates is
assumed. The inverse restores every original field, matter, spectator,
cell resource and channel value. A reverse local reaction is invoked only
after the inverse contacts have restored its appropriate resource.

All ten primitives in any serialization respecting the four layers are
bijections of the carrier. Each separately preserves total Hjoint,
spectators, each cell's reacting-vector sum, all nine actual node charges
and all nine Gauss-defect entries. Thus every intermediate primitive and
layer boundary, U and U^-1 have those invariants and nonnegative resources.
Reversing the serialization within any one layer gives the same result
because its supports are disjoint.

To see exact content retention without using reaction assumptions, let
the resources immediately after G be

```text
(r0,r1,r2,q0,q1)=(a,b,c,p,q).
```

The contact layers give

```text
(a,b,c,p,q) --A--> (p,q,c,a,b) --B--> (p,a,b,q,c).
```

This is a permutation of all five old resources. The inverse contact
order B then A restores their original locations. This content statement
applies to the contacts, not to G, which exchanges matter/field energy
with resources.

## 5. Access frames, fixed depth and cuts

Gi decides from its own matter, raw field and resource and changes only
those coordinates; its spectators are fixed. Fi reads and changes only
its own six raw field coordinates. Each Aj or Bj reads and exchanges
exactly its two named resource coordinates. No contact reads remote
matter, a remote field or a nonincident resource. Cell-local access still
means access inside the specified finite electric cell; it is not a claim
of a one-electric-edge implementation of G or F.

On the stored-block path C0--Q0--C1--Q1--C2, local G and F have radius0.
A and B are two nearest-neighbour matchings, each of radius1. One forward
step therefore has dependency radius at most2 contact-graph edges. Its
inverse has the same bound, because it reverses those same two matchings
between local layers. Iteration gives a radius bound2k after k steps.
Equivalently, agreement of two inputs on the radius2 neighbourhood of an
output block ensures agreement of that block after one step. This is a
structural dependence bound; it neither asserts propagation of every
perturbation at that bound nor assigns a measured physical speed.

For any finite open chain with N>=2 cells, use the same template:
all Gi; all swaps(ri,qi) for i=0..N-2; all swaps(qi,r(i+1)) for
i=0..N-2; all Fi. Every individual layer again has disjoint supports.
The number of sequential layers is four regardless of N. The same inverse,
primitive conservation and radius2 proof apply on its complete finite
carrier. They require no sweep from the first cell to the last. This
template statement does not claim successful work delivery at every
distance, an optimal latency or an infinite-chain construction. The
executed preparations and work witness here are only for N=3.

For cut-j, replace both Aj and Bj by identity, leaving qj stored and
fixed. All other factors and their ordering remain unchanged. This is a
separate fixed law, not a changing reader flag. Deleting these contact
factors preserves the same inverse construction, locality bound and all
primitive invariants. The paired preparation controls in Section7 compare
these fixed laws on literally identical initial complete states.

This schedule is an explicit new choice even at N=2. In #1308 the
receiver reaction followed the contacts; here every reaction precedes
them. The inherited pieces are the local gates and resource swaps, not
the earlier complete two-cell step or its witness period.

## 6. Full-boundary work witnesses

Let w=(0,0,1,0). The exact local data give

```text
H(w)=1, Lw=(-1,-2,1,2), PLw=(1,1,-2,-2,1,2),
Pw=(0,0,0,0,1,0),
PAw=(1,-1,0,0,-1,1),
PA^2w=(-1,0,1,1,0,-2),
PA^3w=(1,0,-1,-1,-1,1).
```

Here powers of A mean the active field matrix of Section2. Initially
take cells (R,0,PLw,0), (ZM,0,0,0), (R,0,0,0) and q0=q1=0.
This state has total energy41 and zero actual charges and defects.
The middle cell has zero energy, but all 31 of its coordinates and its
contacts remain part of the architecture.

At step1 G0 changes the source to AM with field Pw and resource2,
preserving its energy23. G1 fixes ZM and G2 rejects the unfunded h=0
reaction. In the A layer, A0 stores those two units in q0 while reducing
the source energy to21, and A1 exchanges zeros. Only then, in the B
layer, B0 moves them into r1 and B1 exchanges zeros. Finally F0 takes
the source field to PAw; the other zero fields stay zero.

At step2 the source AM reverse requires two units and rejects at r0=0.
The passive middle gate still fixes ZM, and the target R gate still
rejects at r2=0. A1 stores the middle's two units in q1, and B1 gives
them to r2. The target remains R at this complete-step boundary: its
reaction has already been evaluated. At step3 its G2 sees the received
two units and changes R to AM, consuming them. Every remaining resource
and channel is then zero.

The complete boundary states are fixed by the following table, the
displayed source fields and the unchanged zero spectators and other
fields:

| k | Matter0,1,2 | r0,r1,r2,q0,q1 | H0,H1,H2,q0,q1 |
| ---: | --- | --- | --- |
| 0 | R,ZM,R | 0,0,0,0,0 | 23,0,18,0,0 |
| 1 | AM,ZM,R | 0,2,0,0,0 | 21,2,18,0,0 |
| 2 | AM,ZM,R | 0,0,2,0,0 | 21,0,20,0,0 |
| 3 | AM,ZM,AM | 0,0,0,0,0 | 21,0,20,0,0 |

At k=0 the source field is PLw and at k=1,2,3 it is respectively
PAw, PA^2w, PA^3w. Its h=1 reverse remains underfunded throughout
these latter steps. There is no direct source/target contact. Boundary1
stores the two units in the middle; boundary2 stores them at the target;
step3 uses them for a matter change. Arrival and use have the same
target total energy20 but different literal target states. At the final
displayed boundary the source has lost two units and the receiver has
gained two, with zero net energy in the middle and channels.

For the charged witness add static fields S(1,0),S(1,0),S(0,1) to
the three raw fields, and use respective spectator triples
(2e0,-3e0,e0), (2e0,-3e0,e0), (e0,e0,-2e0), where e0=(1,0,0,0).
The actual charge vectors are (2,-3,1),(2,-3,1),(1,1,-2), matching
their retained divergences. Their fixed spectator energies are84,84,36
and their static energies are3,3,2. The same gate and resource trace
therefore gives the exact complete energy vectors

```text
(110,87,56,0,0)
 -> (108,89,56,0,0)
 -> (108,87,58,0,0)
 -> (108,87,58,0,0).
```

All total253. Middle baseline87 is explicitly84+3, with zero matter
energy. Every source field above receives S(1,0), the middle field
remains S(1,0), and the target field remains S(0,1); all spectators
remain unchanged. This specifies the full charged states, not just their
energy labels, and retains all nine nonzero/zero charge entries exactly.

The inverse of the three steps exists on these witnesses because the
inverse exists on every full state. No irreversible consumption, channel
clearing or additional reader write is used to cause receiver work.

## 7. Matched controls and preparation cost

For either neutral or charged witness, cut0 isolates the ready middle
and target component from the source. That component consists of ZM
middle with its fixed static field, R target with its fixed static
field, and zero r1,r2,q1. Its local G operations fix both inputs, its
remaining contacts exchange zeros, and its F operations fix the static
fields. This component is invariant by induction for all time, whatever
the isolated source does. The target consequently remains exactly its
initial full state, and cut q0 remains stored and fixed.

With cut1 the target is isolated directly. Its R endpoint, zero active
field and resource0 fail the h=0 budget test; F fixes its static field.
Its complete state is invariant for all time. These two arguments prove
both all-time cut claims without searching longer trajectories. They do
not claim that an arbitrary target under an arbitrary preparation cannot
react. The finite audit checks only the specified boundaries k=0..3.

The equal-energy offimage control uses source R and active
y=(0,0,1,-2), with all resources and channels empty, passive middle and
ready zero-field target. Although H(y)=5, y is not in LZ4. As A is
an integer automorphism commuting with L, both LZ4 and its complement
are invariant under A: applying A^-1=A^4 proves the converse direction
as well as forward inclusion. Thus the source G always rejects its
image test. All resources remain zero, so the target never receives
funding. Nevertheless the first complete step changes the source field:

```text
Py=(0,0,0,0,1,-2), PAy=(3,-1,-2,-2,-3,5).
```

This separates field energy from arithmetic admission and G rejection
from a full-step fixed point. Its displayed finite control stops at k=3;
the all-time statement follows from image invariance.

Replacing the neutral middle ZM by R adds18 units to the preparation,
raising total energy to59. At boundary1 the middle is R with r1=2.
At the next G layer it spends those units on its own h=0 reaction,
becoming AM with r1=0. Consequently at boundary2 the target remains
R with r2=0; the cell energies are21,20,18. This is a paid intermediate
reaction, not a zero-cost passive conductor. The control is only k=0..2;
it asserts no permanent absorption or future reaction history.

## 8. Occupied contents and distinct orderings

Set all three matter triples to ZM and all fields and spectators to
zero. Every local gate and field step then fixes its non-resource
coordinates. With resource vector (r0,r1,r2,q0,q1)=(0,1,2,3,4),
the chosen contacts give

```text
(0,1,2,3,4) --A then B--> (3,0,1,4,2).
```

All ten units and every old resource survive. Applying B then A to
this result restores the original vector. Either cut law also remains
invertible on this occupied fixture; its cut channel keeps its original
value, and the other contacts are still exact swaps.

In contrast, copying r0=2 into initially empty q0 while retaining r0
creates two energy units. The destructive send formula (r,q)->(0,r)
loses old q and maps (2,0) and (2,1) to the same output. The destructive
receive formula (q,r)->(0,q) loses old r and likewise maps (2,0) and
(2,1) to the same output. At the occupied input each loses one unit
and is noninjective. The argument applies to both A contacts and both
B contacts. These are erroneous formulas explicitly excluded from U.

Changing contact-layer order changes the law even though energy and
invertibility survive. Starting from general (a,b,c,p,q), B then A
gives (b,c,q,a,p), whereas A then B gives (p,a,b,q,c). On the occupied
fixture the former is (1,2,4,0,3), distinct from (3,0,1,4,2).
For the neutral work preparation the alternative G;B;A;F schedule
has q0=2 at boundary1, q1=2 at boundary2 and target R/r2=2 at
boundary3. Its target has not reacted at that last boundary. This
comparison uses exactly k=0..3, not a period search.

The serial sweep G;A0;B0;A1;B1;F is another different law. It sends
the source resource through r1 and both channels before boundary1,
leaving target R/r2=2 there. At step2 the target reacts. It has no
complete-step boundary storing these units in the middle. Its contact
depth would be 2(N-1) if continued down an N-cell chain. This is why
the chosen two parallel matchings, and not merely an ordered list of
swaps, are part of the frozen law. The sweep comparison stops at k=2.

## 9. Finite audit and recurrence boundary

The universal inverse, conservation, support and cut results above are
proof statements on their declared carriers. They are not inferred by
exhausting the unbounded state space. The frozen finite audit has64
core ordered template triples and21 indexed exceptional substitutions,
for85 indexed triples without deduplication. Six resource triples,
four channel pairs and three backgrounds give85*6*4*3=6120 indexed
full states. The actual-background construction b_j=(DE)_j e0 retains
Gauss even for a nonsplit raw-field template; the additional spectator
errors in the third background deliberately create the declared
pointwise defects. All reacting templates have total chi0.

The executable obligations also cover the exact field certificates,
625 residue representatives, all primitive and layer frames and energy
accounts, local admission/funding, both inverse identities, within-layer
serialization independence, the stated witness boundaries, cuts,
occupied contents, preparation control and distinct order controls.
These are bounded audits with exposed mathematical targets. A completed
run and cross-architecture agreement must be recorded separately; this
proof text does not claim that execution has already occurred.

For every fixed finite N and initial total energy E*, conservation keeps
the full orbit on its energy shell. Q(v)>=||v||^2 bounds all matter and
spectator coordinates. The square identity in Section1 bounds M0 and
M0+M1, hence M1, and every component of 2E+CM, hence every component
of E. Every nonnegative cell and channel resource is at most E*.
Only finitely many integer full states lie on this shell. Since U is
a bijection preserving the shell, its restriction is a permutation;
every orbit is periodic from its initial state, with no transient tail.

This proves recurrence without a common period bound and without
searching the period of either new preparation. It asserts neither
U^5=I nor U^10=I for the new law. The isolated one-cell identity and
the earlier two-cell witness periods cannot be transferred to this
different network schedule. Receiver work at step3 is consequently
not a proof of terminal activation, permanent memory or irreversible
emission.

## 10. Conditional construction and remaining boundary

The new positive result is a literal full-state path for transferred
work across two separate stored contacts and a passive middle cell:
the source loses two units, the middle holds them between complete
steps, the target receives them later and subsequently uses them.
Both channel cuts remove that target reaction on the same preparation.
The total inverse retains original channel contents and every local
charge and Gauss-defect coordinate.

The incidence, matter chart, ordered reaction endpoints, L pairing,
neutral resources, channel energy weight, directed path labels, fixed
four-layer schedule, preparation and reader are declared architectural
choices. Zero middle energy does not mean absence of its stored
coordinates or of this architecture. The integer energy is not identified
with measured physical energy. No charge is transported, and charge
motion would require its own continuity and electric-flux construction.

The result does not select a global physical interaction from J, prove
native-U compatibility, provide an autonomous microclock, establish
infinite-network dynamics or prove long-term recording. The finite-chain
template establishes fixed depth and a support bound, not a general
all-length paid-work theorem. QDD-INSTRUMENT-APPARATUS,
QDD-TERMINAL-EVENT-SEMANTICS and PHOTON-MASSLESS-PHASE retain their
existing obligations. Any later extension or promotion is separate work;
the delayed work witness, all controls and recurrence boundary belong
together in this NON-CANONICAL candidate.
