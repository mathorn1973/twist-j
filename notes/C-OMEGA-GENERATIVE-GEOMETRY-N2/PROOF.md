# Prefix-consistent geometry and exact field continuation

PUBLIC NON-CANONICAL. Author: A. M. Thorn <thorn@twistj.com>.
Owner: #1247. Prospective pin: a6be00cb11f9b521841250418a3daf4b69e8dbf3.
Status: candidate-T conditional mathematical results; selected construction
choices are candidate-D. No Canon authority or physical-spacetime closure.

## 1. Inherited inputs and the new claim

The registered [relational-growth proof](../../probes/P-RELATIONAL-GROWTH-SATURATION-1/PROOF.md)
constructs a chosen torsion-free Z^2 cover of the fired translations, whose
word balls have radius rho(x,y)=max(|x|,|y|,|x-y|). Their tagged accumulation
has a cubic count. It explicitly does not supply a physical third dimension
or identify this cover with the silent-spatial channel of TIME-CUT-READING.
The [occurrence-address proof](../../probes/P-SNAP-OCCURRENCE-IDENTITY-1/PROOF.md)
constructs a serial rank and an atomic-emission lower bound. We inherit those
scopes without promotion.

The [selected event-Cauchy model](../C-HODGE-EVENT-CAUCHY-N/PROOF.md) supplies
one injective embedding e_h:Z x Z^3 -> E_+ for every fixed h>=3, with actual
windowed integer representatives and its own positive-energy scalar law.
This is a NON-CANONICAL selected target, not a native-U theorem.

The new result supplies actual coordinates for the tagged carrier, a fixed
metric and immutable prefix exhaustions, then a dependency-closed ordering
which emits exact field values rather than recomputing a finite-boundary
approximation. A separate negative theorem proves that this construction's
prefix properties still do not force its target geometry.

## 2. Hexagonal balls are diagonal projections of positive cube shells

Fix r>=0 and let H_r={ (x,y) in Z^2:rho(x,y)<=r }. Set

    M=max(0,x,y), ell=min(0,x,y), c=r-M,
    Phi(r,x,y)=(x+c,y+c,c).                            (1)

The elementary identity M-ell=rho(x,y) implies that all three coordinates
are nonnegative: their minimum is r-M+ell>=0. Their maximum is r, since
max(x+c,y+c,c)=M+c=r. Thus (1) lands in the positive cube shell

    Q_r^+={ (a,b,c) in {0,...,r}^3:max(a,b,c)=r }.

Conversely, take a point of Q_r^+ and put x=a-c, y=b-c. Then
max(0,x,y)=r-c and min(0,x,y)=min(a,b,c)-c, so rho(x,y)<=r.
Substitution in (1) recovers (a,b,c). This proves the inverse

    (a,b,c) -> (max(a,b,c),a-c,b-c).                    (2)

Consequently Phi is a bijection on every layer and from the disjoint tagged
union of H_r onto N_0^3. Completed layers 0..R give exactly {0,...,R}^3.
The projection (a,b,c)->(a-c,b-c) forgets displacement in direction (1,1,1);
the tag r=max(a,b,c) fixes the otherwise missing position on that line.
This is a coordinate construction, not merely a count identity. It is not
an isometry of the original two-dimensional word metric. The third layer
coordinate and the optional infinite cover are real additional inputs.

To obtain all signs, give each nonzero coordinate its independent sign and
allow only + at zero. Taking absolute values recovers a unique positive
representative, so there are no duplicate signed points. The completed
signed layers are C_R={z in Z^3:||z||_infty<=R}. Hence

    |C_R|=(2R+1)^3,
    |C_r minus C_(r-1)|=24r^2+2       (r>=1),          (3)

and the origin is the single radius-zero point. Signing is a declared
completion, not a theorem that native state symmetries force three signs.

## 3. An actual native prefix drives a connected append-only spatial archive

Let H_N=(x_0,...,x_N) be a legal prefix of the unchanged native update.
The implementation verifies each supplied successor before appending its
record; it neither changes U nor consumes a future checkpoint.

For one fixed h, enumerate the signed shells in increasing radius. At the
opening of shell r, with a already completed native transitions, compute

    i_a=(z_6(x_a)+2 theta_a) mod5,       b_r=i_a mod2.

Freeze b_r for that entire shell. Order its points by the number k of
coordinates satisfying |z_i|=r, increasing k, then lexicographically for
b_r=0 or reverse lexicographically for b_r=1. Output exactly one point on
each completed transition. This rule is defined at every finite prefix.

For r>=1, every point of the shell has k>=1 boundary coordinates. Move one
boundary coordinate one integer toward zero. If k=1, the neighbor lies in
C_(r-1); if k>1, it lies in the same shell with k-1 boundary coordinates.
In either case it was emitted earlier, regardless of the lexicographic bit.
Thus every noninitial point has an earlier nearest neighbor, and EVERY
spatial prefix is connected. Each coordinate appears exactly once.

The record contains its fixed integer address z, actual coordinates e_h(0,z)
and references to all already present nearest neighbors (at most six).
Interpret each reference as an undirected edge. An edge is emitted exactly
once, when its second endpoint appears. This representation never appends a
new reference into an old vertex record. At any prefix the accumulated edge
set is exactly the nearest-neighbor induced graph on the present vertices.
No false nonedge is asserted just because one endpoint is not yet present.

All old point records and all old edge records are preserved literally.
If H_N is a prefix of H_(N+1), every earlier shell bit is the same, so pure
redecoding also has exactly the same old record list. This proves more than
nested vertex sets: coordinates, metric evaluation and old adjacency agree
on overlaps. A fixed h is essential; changing resolution is another family.

After exactly N_R=(2R+1)^3 appends, the points are precisely C_R. Every
integer point occurs at finite index. The limiting label graph is Z^3.
The source selector changes an ordering convention, not a completed cube.

## 4. A positive fixed metric with proved cubic metric-ball growth

Work in the inherited E_+ frame t,s1,s2,s3, where

    g(t,t)=-ct,  g(si,sj)=delta_ij ai,
    ct=(2+sqrt5)/8,
    (a1,a2,a3)=(2sqrt5/5,6sqrt5/5,3sqrt5/2).

All ai>ct>0. Write tau(v)=-g(t,v)/ct and P_s(v)=v-tau(v)t.
The predecessor's ideal event at (0,z) is y(z)=h^-1 sum_i z_i si. Its
rounding error satisfies

    ||e_h(0,z)-y(z)||_* <= R0/h^4,
    R0=10-9sqrt5/5<6,
    ||v||_*=max(|tau(v)|,sqrt(g(P_s v,P_s v)/ct)).

Define d_h as the Euclidean norm distance between P_s e_h(0,z) and
P_s e_h(0,z'). Its exact square is

    d_h(z,z')^2=g(q,q)+ct*tau(q)^2,
    q=e_h(0,z)-e_h(0,z').                              (4)

This is not the Lorentz interval alone and not the shortest-path metric of
a partial graph. Formula (4) is fixed on the complete carrier, so restricting
or enlarging an archive cannot change any previously specified distance.
The program stores integer coordinates and exact rational-coefficient pairs;
no square-root approximation is needed to compare squared distances.

The ideal spatial distance is

    d_0(z,z')^2=h^-2 sum_i ai(z_i-z'_i)^2.

The triangle inequality of the positive spatial norm gives

    |d_h-d_0| <= 2 sqrt(ct) R0/h^4.                    (5)

If z!=z', d_0>=sqrt(min ai)/h>sqrt(ct)/h. Thus

    |d_h-d_0|/d_0 < 2R0/h^3 < 12/27=4/9.

For all z,z' and h>=3 we obtain

    (5/9)d_0 <= d_h <= (13/9)d_0.                      (6)

The lower bound proves injectivity of the positive spatial projection, so
(4) defines a genuine metric, with its triangle inequality inherited from
the positive norm.

Let a_min=min ai and a_sum=sum ai. For every center z0 and metric radius s,

    C_floor(9hs/(13 sqrt(a_sum))) + z0
       subset B_dh(z0,s)
       subset C_floor(9hs/(5 sqrt(a_min))) + z0.        (7)

Using (3), this yields fixed positive two-sided constants times s^3 for
large s. The large-scale metric volume-growth exponent is therefore three.
This is a metric theorem, not an inference from an untyped cardinality or
a statement of Hausdorff dimension of a discrete set. It is still a theorem
about the chosen Hodge reading, not a forced physical spatial dimension.

## 5. A finite spacetime region containing every needed predecessor

Use a separate output mode on

    K_R={ (m,z):m>=0, m+||z||_infty<=R }.

This region is a computational dependency domain, not a Lorentz light cone.
For each new radius R, enumerate m=0,...,R in increasing order and use the
signed spatial shell ||z||_infty=R-m at that m. Within each spatial shell
use the preceding boundary-count/lexicographic rule. One native selector bit
is frozen when the new R shell opens.

The exact point count is

    |K_R|=sum_(r=0)^R (2r+1)^3
         =(R+1)^2(2(R+1)^2-1).                       (8)

The identity follows by subtraction: with n=R+1, the successive difference
of 2n^4-n^2 is (2n-1)^3, and both sides start at one. Every (m,z) with m>=0
has finite shell radius m+||z||_infty, so the union is N_0 x Z^3.

For m>=2 the scalar recurrence uses (m-1,z), (m-2,z) and (m-1,z+/-ei).
For a neighbor predecessor,

    (m-1)+||z+/-ei||_infty <= m+||z||_infty.

Equality is allowed, but that predecessor has smaller m and was emitted
earlier in the same shell. The two on-site predecessors have strictly
smaller radius. Thus all eight distinct predecessor addresses are already
present. At m=0,1 the supplied initial data give the value directly.

This ordering removes the need to invent boundary data. It is not a
redefinition of the inherited scalar operator or its underlying event map.

## 6. Exact field agreement on every finite patch

Freeze total exact initial-data functions f0,f1 with finite spatial support,
and a separately supplied total computable source j_m(z) in F=Q(sqrt5).
Zero forcing is the default. Deterministic function values are part of the
input contract; stateful/random callbacks are not admitted source functions.
At a new (m,z), m>=2, compute

    f_m(z)=(2-2A) f_(m-1)(z)
       +sum_i alpha_i[f_(m-1)(z+ei)+f_(m-1)(z-ei)]
       -f_(m-2)(z)+h^-2 j_(m-1)(z),
    alpha=((5+2sqrt5)/16,(5+2sqrt5)/48,(5+2sqrt5)/60),
    A=sum alpha<1.                                    (9)

The inherited recurrence has a unique pointwise all-grid solution by
induction in m. Each point requires only finitely many predecessors and
source evaluations. The same induction over the present shell order proves
that the emitted value equals that all-grid solution exactly: initial
values agree, and all predecessors of a noninitial point already agree.

Consequently the stored field on K_R is the restriction of one global
solution, not a finite-box approximation. Enlarging R never changes an old
field value, including zeros. The fixed actual-event coordinates are also
unchanged, so metric and field restrictions commute with enlargement.
For any finite target cylinder 0<=m<=M, ||z||_infty<=Z, K_(M+Z) contains it.
Its values require no later records or unknown future source samples.

This does not create a new energy theorem. When the source is finitely
supported on each finite time prefix, the global energy, source-work and
stability theorems remain those of the inherited scalar model. A finite
aperture need not conserve its energy without a boundary-flux term. For
unbounded source profiles the pointwise recurrence still exists, but no
finite global-energy assertion is made here.

The inherited microscopic spacelike impulse response is not repaired by
changing the order in which exact field values are evaluated. Neither a
causal dependency order nor (8) proves physical Lorentz-cone support.

## 7. Sharp materialized-record costs, and two different clocks

For an initially empty archive with at most c>=1 newly materialized vertex
records per native transition, a region with V distinct points requires at
least ceil(V/c) transitions. This is the registered atomic-emission bound,
not a bound on what a short formula may describe.

Batch c successive records of either serial construction per native tick,
freezing each newly opened shell's bit from the currently available native
checkpoint. The ordering proofs hold for every bit sequence, including
several openings at one tick. A partial final batch attains the lower bound.
Thus the exact costs for the two separate modes are

    spatial:    ceil((2R+1)^3/c),
    spacetime:  ceil((R+1)^2(2(R+1)^2-1)/c).           (10)

The reference implementation provides the c=1 serial stream. Batching is
the stated mathematical wrapper; the bound counts a vertex with bounded
many links as one record. Counting each link separately changes the budget
by a bounded factor, not the cubic or quartic exponent. Storing every pairwise
distance as a separate atom is a different, larger representation. Here the
immutable coordinates and fixed metric formula determine those distances.

The spatial completion radius is of order N^(1/3), and the spacetime patch
radius is of order N^(1/4), at fixed c. Requiring cubic volume per N ticks
while allowing only c atomic appends per tick would contradict the count;
we do not make that assertion. A growing-integer record, compressed formula
or symbolic infinite set is outside the same atomic interpretation.

Most importantly, N is the generation/serialization counter of the native
prefix, whereas m is a coordinate of the represented event. Spatial mode
emits points on m=0 at many different N; field mode computes many m values
in dependency order. This is not the clock-aligned point bridge m=N of the
predecessor. No equality with METRO-TICK, physical emission time, SI time,
physical storage capacity or material creation of space follows.

## 8. Prefix consistency still does not select a physical geometry

Consider the broader proposed class which requires only: computability from
a legal native prefix; no future source input; immutable record overlaps;
a fixed append budget; and cubic spatial growth. These requirements are
insufficient to choose a metric.

Let A_N be any fixed computable sequence of nested finite metric records,
with its old distances preserved and at most c new vertex atoms at each
step. The decoder D(H_N)=A_N computes N from the supplied prefix length and
emits the next difference. It is causal in the specified source sense,
preserves every overlap and respects the append budget. It ignores source
values because no axiom of this class requires a metric-sensitive use of
them. Thus every such preassigned geometry family is admissible.

For explicit inequivalent controls, enumerate the same cubes C_R with either

    q0(z-z')=dx^2+dy^2+dz^2,
    q1(z-z')=dx^2+2dy^2+3dz^2.

Both define positive metrics on Z^3, have cubic metric-ball growth and obey
the same prefix/budget rules. In the first infinite metric space each point
has six points at distance one; in the second it has exactly two. They are
not isometric, even after forgetting labels. These controls refute selection
by the broad prefix axioms. They are not claimed to satisfy the additional
fixed-Hodge-metric hypothesis, which of course narrows the target class by
an independent choice.

Our actual chosen Hodge generator does consume native selector bits. They
change partial record order, as the finite audit explicitly checks on five
initial trace phases. Yet every completed cube, its metric, the union of
events and, for the same initial/source functions, the whole field solution
are independent of those bits. Using some native data is therefore not by
itself evidence that native dynamics determine the geometry.

This negative result does not ban a future metric-sensitive native law.
It states exactly which proposed conditions fail to provide one. In
particular it settles the question of whether unbounded prefix access alone
repairs the target-blindness of the previous point-bridge construction: it
does not.

## 9. Final scope

The constructive task is complete at its frozen mathematical scope:

- tagged hexagonal data have an explicit cube-shell coordinate map;
- a native prefix drives a total append-only connected geometry exhaustion;
- a fixed positive Hodge-spatial metric has cubic large-scale ball growth;
- dependency-closed event patches carry exact, immutable scalar solutions;
- materialized spatial/spacetime record budgets are sharp;
- the attempted promotion from these properties to a selected native
  spacetime is obstructed by an explicit nonselection theorem.

The optional infinite cover, layer tag, signed completion, Hodge chart,
window/metric/scale, spatial stencil, initial field and source are declared
choices. No hidden selection, native persistent memory, Galois physical
identification, physical photon, global D3 action/measure, SI scale or
curvature result is supplied. Candidate bridge names are those in PREREG.md;
no public gate or Canon status changes.
