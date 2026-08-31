# Complex-source current suppression and all-turn path tails

Status: NON-CANONICAL / RESULT-EXPOSED / CONDITIONAL MODEL / NO FORMAL RUN.

Identity: `P-PHOTON-GEOMETRIC-CURRENT-REDUCTION-1`.
Notes claim: [issue #727](https://github.com/mathorn1973/twist-j/issues/727).
Date: 2026-08-31.

Public reference: main `1c5f7832a9dec807d1f9830be3cdbdd092ff4f99`,
Public Canon v72 unchanged. This note proves stronger integrated current
bounds and exponential tails for a family of directed paths with arbitrary
turn counts. It neither adopts the conditional model as TWIST-J nor proves
infrared screening. Its identities are original analytic proofs, not a new
formal census or an enlargement of any existing probe's scope.

## 1. Selected model and named conditional measure boundary

Use the finite free rectangular cubical boxes K in Z^4 of the
[unsigned-current suppression note](PHOTON-UNSIGNED-CURRENT-SUPPRESSION.md).
Let E,P denote positively oriented edges and plaquettes, d the cellular
coboundary, and partial its transpose. All boundary edges are summed.
The selected primal factor and its normalized version are

```text
W(theta)=2+2cos(theta),
Q(theta)=W(theta)/2=1+cos(theta),
A_e in (2pi/5)Z modulo2pi.
```

Normalized five-point Haar averages give

```text
Z_K=E_(A in Z5^E) product_p Q((dA)_p)
   =sum_(n in{-1,0,1}^P, partial n=0 mod5) 2^(-|supp n|).
nu_K(n)=Z_K^-1 2^(-|supp n|) on this constrained carrier,
j=partial n/5.
```

This follows by expanding Q=1+(exp(i theta)+exp(-i theta))/2 and using
edge-character orthogonality. In particular Z_K>=1. Since at most six
plaquettes meet an edge, j_e belongs to{-1,0,1}; also partial j=0.

All probability statements below are inside the notes-only conditional
boundary `NOTE-GATE-L4-L6-PHOTON-UNSIGNED-CURRENT-IDENTITY`: from this
specified L4 incidence/action to its explicitly normalized L6 finite
current law. This is not a registered or Canon-adopted gate and not
GATE-L4-L6-PHOTON-MASSLESS-PHASE. The complete action and its physical
occurrence law remain unselected. The complex polynomial source used
below is an auxiliary identity, not adoption of a physical source coupling.

## 2. Arbitrary marked sectors and an exact complex-source inequality

Let T be any finite edge set. For u in{-1,0,1}^T define N_T(u) as the
positive sum of2^(-|supp n|) with

```text
(partial n)_e=5u_e for e in T,
(partial n)_e=0 modulo5 for e outside T.
```

Thus N_T(u)>=0, N_T(0)>=1, and sum_u N_T(u)=Z_K. Every unmarked current
sector remains summed. No plaquette-independence assumption is made on T.

Write integral_mix for normalized U(1) Haar integration over A_e on T
and normalized Z5 averaging on its complement. For a real edge cochain f
supported on T, the finite Fourier expansion gives exactly

```text
integral_mix exp(-i5<u,A_T>) product_p Q((dA)_p-i(df)_p)
  =exp(5<u,f>) N_T(u).                                  (SOURCE)
```

Indeed each expanded term acquires exp(<n,df>)=exp(<partial n,f>).
The mixed character projection fixes partial n=5u on T, and f vanishes
outside T. No contour deformation or convergence interchange is involved.

For real theta,y one has the exact modulus identity

```text
|1+cos(theta-i y)|=cosh(y)+cos(theta).
```

Squaring the left side gives(cosh(y)+cos(theta))^2, and the right side is
nonnegative. Taking absolute values in(SOURCE), whose right side is
nonnegative, removes the unit-modulus insertion. Put c_p=cosh((df)_p)>=1.
Then

```text
exp(5<u,f>)N_T(u)
  <=integral_mix product_p [c_p+cos((dA)_p)].
```

Expand this last product and integrate with no insertion. It is exactly
the zero-selected-current sector, with the same modulo5 constraints outside
T. A ternary field n in this sector now has coefficient

```text
2^(-|supp n|) product_(p:n_p=0) c_p
  <=2^(-|supp n|) product_p c_p.
```

Every coefficient is nonnegative. Summing proves the main inequality

```text
N_T(u)/N_T(0)
  <=exp[-5<u,f>+sum_p log cosh((df)_p)]                 (CS)
```

for every real f supported on T. This is an integrated positive
zero-sector comparison, not a pointwise conditional-current estimate.
Continuous zeros of Q are retained; no logarithm of Q is taken.

## 3. Independent stars: a small exact constant and unsigned odds

Suppose T is plaquette-independent and every u_e is+1 or-1. Put L=|T|
and f=h u, with h>0. Each plaquette meets at most one selected edge, so
its source is0,+h,or-h, and there are at most6L nonzero incidences.
Equation(CS) yields

```text
N_T(u)<=b(h)^L N_T(0),
b(h)=exp(-5h)cosh(h)^6.
```

The minimum occurs at tanh(h)=5/6, namely h=(log11)/2. Therefore

```text
b=6^6/11^(11/2),
P_nu_K(j_T=u)<=b^L P_nu_K(j_T=0).
```

This is an exact analytic constant. In particular b<1/11: the inequality
6^4=1296<1331=11^3 implies6^12<11^9 and hence b^2<1/121.

Summing the2^L nonzero sign assignments gives

```text
P_nu_K(j_e!=0 for every e in T)
  <=(2b)^L P_nu_K(j_T=0).
```

For nonempty T, the all-zero and all-nonzero events are disjoint. Thus
the unconditional unsigned odds bound is

```text
P_nu_K(j_e!=0 for every e in T)
  <=(2b)^L/[1+(2b)^L].                                  (STAR-ODDS)
```

For one edge this is less than2/13, a genuine improvement over the
earlier uniform6/25 Ward bound. All outside current sectors remain summed;
arbitrary conditioning on those currents is not asserted.

There is no contradiction with the earlier sharp1/2 fifth-harmonic bound
at a fixed complementary angle environment, or with the exact pointwise
unsigned star census. Those are different pointwise comparisons. Here a
complex source is inserted before integration and a positive expansion
compares the complete zero-selected sector after integration. No old
pointwise constant or frozen census threshold is changed.

## 4. A universal arbitrary-marker bound

The elementary even inequality log cosh(y)<=y^2/2 follows by integrating
tanh(y)<=y for y>=0. Also, on finite free boxes,

```text
sum_(p in P)|(df)_p|^2<=16 sum_(e in E)|f_e|^2.
```

For completeness extend f by zero to all edges of Z^4. Restricting the
full-lattice curl back to K can only decrease its squared norm. Commuting
coordinate differences and their adjoints give the discrete identity

```text
||d_1 f||_2^2+||partial_1 f||_2^2
  =sum_(i=1)^4 sum_(a=1)^4 ||nabla_i f_a||_2^2.
```

Here partial_1 is divergence on one-cochains and nabla_i is the forward
coordinate difference. Each difference has norm at most2, so the right
side is at most16||f||_2^2. This proves the stated bound without imposing
periodic or fixed-angle boundary conditions on the original measure.

For arbitrary T, L=|T|, all u_e=+1 or-1, take f=(5/16)u in(CS). Then

```text
N_T(u)<=exp(-25L/32) N_T(0).
```

Summing signs and using disjointness as above gives, for nonempty T,

```text
q=2exp(-25/32)<1,
P_nu_K(j_e!=0 for every e in T)<=q^L/(1+q^L).            (ALL-MARKERS)
```

The strict sign needs no decimal: exp(25/32)>
1+25/32+(25/32)^2/2=4273/2048>2. This uniform event bound alone is not a
connected-component or covariance-tail estimate: the number of possible
paths or connected sets must still be controlled.

## 5. A geometry-weighted bound without star independence

For a finite set T of distinct edges define its plaquette-conflict graph:
vertices are edges of T, and a pair is adjacent exactly when the lattice
edges belong to a common elementary plaquette. Let m(T) count unordered
adjacent pairs in the full lattice. Distinct edges share at most one
plaquette: an adjacent perpendicular pair fixes its plane and square,
while an opposite parallel pair fixes its two spanning directions and
square. Thus no pair is counted twice by summing over plaquettes.

Fix the same h=(log11)/2 and put

```text
c_h=cosh(h)=6/sqrt(11),
r=tanh(h)=5/6,
R=1+r^2=61/36.
```

The symbol R here is a scalar factor, not the spectral screening ratio
or a spatial radius. For k marked edges on one plaquette, k belongs to
{0,1,2,3,4}, and their signed source sum has modulus at most kh. The
following complete list proves

```text
cosh(h sum_(a=1)^k sigma_a)
  <=cosh(kh)<=c_h^k R^binomial(k,2), sigma_a in{+1,-1}:

k=0: cosh(0)=1;
k=1: cosh(h)=c_h;
k=2: cosh(2h)/c_h^2=1+r^2=R;
k=3: cosh(3h)/c_h^3=1+3r^2<=(1+r^2)^3;
k=4: cosh(4h)/c_h^4=1+6r^2+r^4<=(1+r^2)^6.
```

The last inequality follows directly from the nonnegative binomial
coefficients: its r^4 coefficient on the right is15 rather than1,
and all higher coefficients are nonnegative. For k=3 the omitted terms
are likewise nonnegative.

Use f=h u for arbitrary marked signs u_e=+1 or-1. If k_p is the number
of marked edges of p, then sum_(p in K)k_p<=6L, because boundary edges
have no more than six incident plaquettes. Also
sum_(p in K)binomial(k_p,2)<=m(T), with equality when all relevant
plaquettes are in K. Since c_h,R>=1, (CS) gives

```text
N_T(u)<=b^L R^m(T) N_T(0),
P_nu_K(j_T=u)<=b^L R^m(T).                              (WEIGHTED)
```

No plaquette independence, favorable relative signs, or omitted outside
current sector is required. If this upper bound exceeds one it is simply
uninformative; it is not a statement that a probability exceeds one.

## 6. All-turn paths with few excess contacts

Let gamma=(v0,...,vL) be a vertex-simple nearest-neighbor directed path:
all vertices are distinct and each of its L edges is followed in its
occupied current direction. Let t(gamma) count turns, namely consecutive
perpendicular steps, and put

```text
m(gamma)=m(E(gamma)),
c(gamma)=m(gamma)-t(gamma).
```

An immediate reversal is excluded by vertex simplicity. Straight
consecutive steps do not share a plaquette, while every turn contributes
one distinct conflict pair. Therefore c(gamma)>=0 and counts exactly
the conflicts between nonconsecutive path edges. In particular the
condition below does not restrict how often the path turns:

```text
c(gamma)<=L/24.                                         (EXCESS)
```

Fix a directed first edge e0. At length L and turn count t, the number
of nonbacktracking path descriptions is at most binomial(L-1,t)6^t:
choose the turning positions and one of six perpendicular directions
at each turn. Straight steps have one continuation. This count may
include intersecting paths and paths outside K, which only enlarges it.

For every path satisfying(EXCESS), (WEIGHTED) bounds its probability by
b^L R^(t+L/24). Summing over every possible turn count, without a cutoff,
gives

```text
P_nu_K(exists such a length-L path starting with e0)
  <=(b R^(1/24))^L sum_(t=0)^(L-1)binomial(L-1,t)(6R)^t
  =(b R^(1/24))^L(1+6R)^(L-1)
  <=kappa_path^L,

kappa0=b(1+6R)=67*6^5/11^(11/2),
kappa_path=kappa0 R^(1/24)<1.                            (PATH)
```

These kappa symbols denote path-decay constants, not the score
normalization tan(pi/5). The contraction is certified by exact integers:

```text
kappa0^2=271432664064/285311670611<20/21,
21*271432664064=5700085945344
  <5706233412220=20*285311670611.
```

Furthermore, the binomial expansion with positive terms gives

```text
(21/20)^12>1+12/20+66/400=353/200>61/36=R.
```

Consequently

```text
kappa_path^48=kappa0^48 R^2
  <(20/21)^24 R^2
  <(3050/3177)^2<1.
```

This proves strict contraction without a numerical fit, asymptotic
estimate, or formal enumeration. With c(gamma)=0 the stronger constant
kappa0 itself applies.

## 7. Root factors, distance tails, and local limits

At a specified root vertex there are at most eight first directed edges,
so the right side of(PATH) becomes8 kappa_path^L. For a specified
unoriented first edge with both directions allowed, the factor is2.
For every integer a>=1, summing the separate length events gives

```text
P(exists a path satisfying(EXCESS) from e0 of length L>=a)
  <=kappa_path^a/(1-kappa_path),

P(exists such a path from a specified root vertex of length L>=a)
  <=8 kappa_path^a/(1-kappa_path).                       (TAIL)
```

These bounds can always be capped by1. Reaching l1-distance at least a
along a path satisfying(EXCESS) requires length at least a, hence has
the same upper bound. No assumption is made that every prefix of a
qualifying path itself qualifies; the proof uses a union over all lengths.

For fixed L and root there are finitely many candidate paths, and the
events are cylinders. The finite-volume bounds therefore pass to every
local subsequential limit of the selected current laws and to convex
averages, including the paired averaged construction of the
[defect-screening criterion](PHOTON-DEFECT-SCREENING-CRITERION.md).
Apply the countable union bound after that limit to obtain(TAIL).
Neither Gibbs-state identification nor uniqueness is needed. Almost
surely, each fixed root has a finite maximum length among paths obeying
(EXCESS); the countable union over lattice roots retains this statement.
It does not forbid infinite paths outside that geometric family.

## 8. Sign-sensitive contacts and the remaining shortest-path limitation

Use the selected law nu_K on ternary faces n with partial n=0 modulo5,
j=partial n/5, and the established source estimate

```text
P_nu_K(j_T=v)
 <=exp[-5<v,f>+sum_p log cosh((df)_p)]
```

for real f supported on the marked edges T and nonzero prescribed signs
v. All unmarked current sectors are summed. Keep

```text
h=(log11)/2,   cosh(h)=6/sqrt(11),
b=6^6/11^(11/2),   R=61/36.
```

### 8.1 Classification and the exact local factors

Let gamma be a vertex-simple directed open path of L edges, with t turns.
Two nonconsecutive path edges sharing a plaquette cannot be perpendicular:
such edges would share a vertex, contradicting vertex simplicity. They
are therefore opposite parallel sides. A plaquette containing three path
edges contains one consecutive three-edge U-turn block: the two internal
vertices force those adjacent edges to be consecutive in the path.
A plaquette cannot contain four path edges, since that would form a
cycle inside the vertex-simple open path.

Classify the nonconsecutive contact pairs as follows:

```text
z_cancel: opposite parallel sides traveled in the SAME physical direction;
u_U:      the opposite pair inside a three-consecutive-edge U-turn block;
r_remote: opposite sides traveled in OPPOSITE physical directions,
          on a plaquette containing only those two path edges.
```

These classes are disjoint and exhaustive. Every U-turn plaquette contains
two turns and one nonconsecutive pair. Thus

```text
m(gamma)=t+z_cancel+u_U+r_remote.
```

The charge-five local constraint explains the canceling class. At a
defective interior edge, six ternary oriented face contributions sum to
5 or-5. Exactly five contributions have the current's sign and one is
zero. At degree5 all five have that sign; degree below5 cannot support
a defect. Therefore each defective edge meets at most one zero face.
Same-direction opposite parallel currents demand opposite signs for the
shared n-face, forcing that face to zero. Since each such plaquette has
exactly two path edges, the canceling contact pairs form a matching on
path edges. This matching property is not needed to discard their
favorable factor in the upper bound below.

Set f=h v along the path and zero elsewhere. On a two-edge canceling
plaquette, the two incidences in df cancel exactly. On a two-edge
reinforcing plaquette they add. On a U-turn plaquette all three oriented
incidences add, because the path follows three sides of one oriented
square. Relative to one factor cosh(h) per marked incidence, the exact
factors are

```text
canceling pair:     S_cancel=1/cosh(h)^2=11/36;
reinforcing pair:   cosh(2h)/cosh(h)^2=R;
three-edge U-turn:  cosh(3h)/cosh(h)^3=37/12.
```

Allocate R to each turn. A U-turn uses two such turn factors, leaving

```text
H_U=(37/12)/R^2=3996/3721>1.
```

H_U is a path factor, not the score's branch observable H.

In a rectangular box, any plaquette containing two marked path edges is
itself in K: all its vertices lie within the same coordinate intervals.
Thus every favorable canceling factor above belongs to the actual action;
omitted exterior plaquettes cannot supply an artificial factor below one.
Summing marked incidences over plaquettes gives at most6L, including the
free-box boundary. The same integrated source proof therefore yields

```text
P_nu_K(gamma occupied in its prescribed direction)
 <=b^L R^t R^r_remote S_cancel^z_cancel H_U^u_U.          (SIGNED-CONTACT)
```

No favorable relation between different outside currents is assumed.
Dropping S_cancel^z_cancel is legitimate since0<S_cancel<1. The factor
H_U is much smaller than the R penalty previously assigned to every
nonconsecutive pair.

### 8.2 Summing arbitrary turns and U-turns

Fix a first directed edge. Weighted nonbacktracking descriptions can be
counted one step at a time. A straight continuation has weight1.
If the preceding transition was a turn from direction a to perpendicular
direction b, precisely one of the six possible new turns, to direction
-a, completes a U-turn. It has weight R H_U; the other five have weight R.
If the preceding transition was straight, no allowed next step can
complete a U-turn, and the six turn choices have total weight6R.
The first transition obeys the same upper bound because H_U>1.

Hence each step contributes at most

```text
A_path=1+R(5+H_U)=24797/2196,
```

and the sum of R^t H_U^u_U over vertex-simple paths of length L is at most
A_path^(L-1). Counting also descriptions with repeated vertices only
enlarges this positive sum; on every valid path, each U-turn is exactly
the local three-step pattern just counted. No independence of current
edges is used.

Put

```text
kappa_H=b A_path.
```

For paths with r_remote<=L/64, (SIGNED-CONTACT), the preceding weighted
count, and S_cancel<=1 imply

```text
P(exists such a length-L path starting with a fixed directed edge)
 <=(b R^(1/64))^L A_path^(L-1)
 <=kappa_signed^L,
kappa_signed=kappa_H R^(1/64)<1.                        (REMOTE-TAIL)
```

The numbers of U-turn and canceling contacts are unrestricted. The
contraction can be checked using only the earlier exact integer bound
kappa0^2<20/21, where kappa0=(67/6)b:

```text
b^2<(20/21)(6/67)^2=720/94269<49/6400,
720*6400=4608000<4619181=49*94269,
so b<7/80.
```

Consequently

```text
kappa_H<(7/80)(24797/2196)=173579/175680<99/100,
100*173579=17357900<17392320=99*175680.
```

Finally, the positive binomial expansion gives

```text
(100/99)^64>1+64/99+2016/99^2=18153/9801>61/36=R,
36*18153=653508>597861=61*9801.
```

It follows that kappa_signed^64=kappa_H^64 R<(99/100)^64 R<1.
These are written exact inequalities, not a census or an additional
formal computation.

The root and tail statements of section7 apply with kappa_signed and
the new condition r_remote<=L/64: a root vertex contributes the factor8,
an unoriented first edge the factor2, and summing all lengths L>=a gives
kappa_signed^a/(1-kappa_signed) for a fixed first directed edge. A path
reaching l1-distance a has length at least a. Fixed-length events are
cylinders, so the same uniform bounds pass to the stated local limits
and convex averages. Neither an arbitrary-current conditional bound
nor a full component-tail estimate is asserted.

### 8.3 Shortest paths need not have few remote reinforcing contacts

There is an explicit admissible example, not just an abstract graph.
Let B be the oriented1-by-4a rectangle of plaquettes in the12-plane,
with a a positive integer. For each transverse direction
v in{+e3,-e3,+e4,-e4}, take the three-chain prism C_v from B to B+v,
oriented so its boundary is -B plus the translated cap and perimeter
side faces. Define

```text
n_B=B+sum_v(B+partial C_v).
```

Each cup B+partial C_v has one translated cap and the side strip along
partial B. Internal side faces cancel in the prism chain. Its remaining
coefficients are+1 or-1. The central B, the four caps, and the four
transverse side strips are mutually face-disjoint. Therefore n_B is
ternary and

```text
partial n_B=5 partial B,
|supp n_B|=5(4a)+4(8a+2)=52a+8,
nu_K(n_B)=2^(-52a-8)/Z_K>0
```

in a box containing this construction. All other current edges vanish;
j is the counterclockwise boundary cycle of the rectangle.

On this current take the root(a,0,0,0) and target(3a,1,0,0).
The unique directed path follows the lower side rightward to(4a,0),
the short end upward, and the upper side leftward to(3a,1). It has
length4a+1 and endpoint l1-distance2a+1. Both boundary arcs between
these endpoints have length4a+1, so it is also an undirected shortest
path in the occupied-current graph.

The a plaquettes nearest the right end each contain an opposite parallel
path pair traveling in opposite directions. One is the three-edge
U-turn at the end; the other a-1 are remote reinforcing contacts.
There are no canceling pairs. Thus r_remote/L=(a-1)/(4a+1) tends to1/4,
well above1/64. The intermediate connecting edges have zero current,
so a common plaquette is not an occupied-graph shortcut.

This disproves a deterministic small-remote-contact bound for arbitrary
shortest directed or undirected occupied paths, even with charge five.
It does NOT disprove extraction of some other useful path from a large
component: this rectangle also contains long straight paths with no
contacts. Its positive finite-volume weight is not a lower tail bound
or a typicality statement. A global extraction theorem or an independent
probabilistic estimate for the remaining high-remote-contact family is
still missing, as is the required connected-covariance screening estimate.

## 9. What the new path estimate includes, and what it leaves open

The estimate admits arbitrary turn counts. In particular the monotone
staircase alternating+e1,+e2 has c=0: its nonconsecutive parallel edges
are not opposite sides of a unit plaquette, and nonconsecutive perpendicular
edges do not share a vertex. The staircase running through a diagonal
chain of equally oriented elementary12-plaquette current loops is therefore
included. Such a chain is no longer an obstruction to this stronger path
family. It would be incorrect to carry forward an obstruction based only
on having many turns or only length-four vertex-simple circuits.

There is still no proved extraction theorem saying that every large
connected current component contains a long directed path obeying either
(EXCESS) or the remote-contact condition of section8. Paths escaping both
bounds, and general connected components, remain uncontrolled here.
Conservation alone is not supplied as a replacement for that missing
geometric or probabilistic argument. The universal marker bound in
section4 likewise does not automatically pay the entropy of all connected
supports.

Neither a marker bound nor this restricted path tail establishes the
needed connected-covariance or weighted second-moment estimate. The
separate positive auxiliary-current representation of the full score
defect, if used, retains rather than removes its long-distance obligation.
The actual screening inequality for both current channels remains open.

The sharper integrated bounds do not refute any sharp pointwise star
constant. They exploit information that those local conditional bounds
did not use. No massless phase, continuum propagator, polarization,
physical photon, apparatus reading, or Canon adoption follows here.
Both photon successor roots remain open. This notes-only result changes
no Canon, registry, registered gate, or accepted probe scope.
