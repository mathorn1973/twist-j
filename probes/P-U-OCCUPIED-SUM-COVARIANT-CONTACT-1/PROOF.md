# Occupied native SUM and the complete declared continuation class

**NON-CANONICAL. Proposed conditional L1 proof; analytical result exposed.**
A. M. Thorn; original text Apache-2.0.

This document supplies a symbolic proof, not an execution record, public
reservation, accepted physical contact, or Canon promotion. The counts
`5^6` and `5^5`, the representative contact, and the continuation formulas
were derived before preparation of the proposed exact audit. Their later
audit must not be described as a blind discovery.

The result classifies one explicitly declared family of additional
interactions. It also constructs two consecutive readable updates on the
actual occupied receiver, with one unreset native counter. It does not
derive that interaction family, its source register, preparation, scheduling,
or reading from native dynamics or from J.

## 1. Complete carrier, equality, and native law

All checkpoint and source arithmetic is in F5. Equality of checkpoints and
of maps is literal coordinate equality, without quotienting or relabeling.
Write

    v=(p1,p4,p1p,p4p,q,r),  z(v)=p1+p4+p1p+p4p+q+r,
    H_j={v:z(v)=j}.

The five native generators, in selector order, are

    a(v)=(p4,p1,p4p,p1p,q,r),
    b(v)=(-p1p,-p4p,-p1,-p4,-q,-r),
    c(v)=(2-p1p,1-p4p+r,2-p1,1-p4-r,1-q,-r),
    d(v)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
    e(v)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).

Each is an affine involution. Set `theta_n=popcount(n) mod 2` and

    G_n(v)=g_(z(v)+2 theta_n mod 5)(v),
    (g_0,g_1,g_2,g_3,g_4)=(a,b,c,d,e),
    U(n,v)=(n+1,G_n(v)).

The added source is one register `s in F5`. The complete new carrier is

    Omega_ext=N0 x F5^6 x F5, with state (n,v,s).

During free motion its declared law is `U x identity_s`. This product law
and the source register are explicit additional architectural premises.
There is no omitted working register, saved input, phase register, history,
or second clock. The source can initially have any of its five values; it
is not assumed blank. The original q,r and all four pistons are retained
as actual coordinates throughout.

The native formulas and stable-sheet table below are already public in
[P-QDD-UNINTERRUPTED-RECORD-1/PROOF.md](../P-QDD-UNINTERRUPTED-RECORD-1/PROOF.md)
and Public Canon v101, `U-STABLE-PAIRED-PORT-TRANSPORT`. That theorem uses
the distinct fibre displacement `T_delta:(q,r)->(q-delta,r+delta)`.
Its off-stable calculation also defines `V_delta`, adding delta to p4
and subtracting delta from p4p. Here `C_s^f=V_(-f(x,y)s)` below is an
additional controlled use of that piston displacement. Neither the name
V_delta nor its appearance in a native commutation defect admits it as
an available interaction. The present proof derives every identity it
uses directly from the displayed generators.

## 2. The actual first write and its entire native continuation

Define the receiver functions

    S=p1+p4+p1p+p4p,  L=p1+p4p,
    x=p1-1, y=p1p-4,
    M=2*((p1-1)*(p4-3)+(p1p-4)*(p4p-2)),
    R=(1-S^2)*L+S^2*M.

The original two-symbol preparation and the complete three-symbol
preparation are

    E_SUM(s1,t)=(t,0,-t,0,-s1,s1),
    E(t,s1,s2)=(0,E_SUM(s1,t),s2),
    (t,s1,s2) in F5^3 independently.

At launch S=z=0 and R=t. The first actual clock bits are 0,1,1.
Substitution into the literal generators gives the whole checkpoints

    n=1: a E_SUM=(0,t,0,-t,-s1,s1),                z=0,
    n=2: c a E_SUM=(2,1+t+s1,2,1-t-s1,1+s1,-s1), z=2,
    n=3: e c a E_SUM=(0,-t-s1,1,t+s1+3,1-s1,1+s1), z=1.

Thus the actual selected letters are a,c,e; they are not externally
chosen controls. The same direct composition on the whole H0 is

    e c a(A,B,C,D,q,r)=(D,C-r,B+1,A+r+3,q+1,r+1).       (1)

At the displayed prepared output, S=4 and M=t+s1, so R=t+s1.
These first-write identities were also exposed in the open
P-U-NATIVE-FIXED-READ-1 candidate. They are derived here from the native
law; that open candidate is not used as normative authority or counted
as a new result of this proposal.

The trace maps of a,b,c,d,e are respectively

    z, -z, 2-z, 2-z, 3-z.

They give the complete stable selector table

| z | theta | selected letter | next z |
|---|---|---|---|
| 1 | 0 | b | 4 |
| 1 | 1 | d | 1 |
| 4 | 0 | e | 4 |
| 4 | 1 | b | 1 |

Consequently the prepared path stays in H1 union H4 forever. More
generally the path from any initial H0 has the common traces

    z_0=0, z_1=0, z_2=2,
    z_n=4+2 theta_(n-1) for every n>=3.                 (2)

Center the complete piston block as

    (x,u,y,w)=(p1-1,p4-3,p1p-4,p4p-2).

On these coordinates the three possible tail letters act as

    b:(x,u,y,w)->(-y,-w,-x,-u),
    d,e:(x,u,y,w)->(-x,-u,-y,-w).                       (3)

Hence each preserves M=2(xu+yw) and sends S to -S. The same fixed
receiver-only function R therefore equals t+s1 at every native
checkpoint n>=3. At n=3 the first centered pair is (x,y)=(4,2).
Its orbit under (3) consists of

    (4,2), (3,1), (1,3), (2,4).                        (4)

This statement includes occupied receiver values t and retained dirty
q,r. None is replaced by a fresh ready state.

## 3. Exactly the declared contact family

For an arbitrary function f:F5^2->F5 and source s define

    C_s^f(v)=(p1,p4-f(x,y)s,p1p,p4p+f(x,y)s,q,r).       (5)

The class freezes all of the following requirements: an additive F5
source action, fixed x,y,q,r and source register, a balanced displacement
in the specified second and fourth piston slots, dependence of f on
exactly the two arguments x,y, and commutation with each tail letter
b,d,e. In particular it is NOT the class of all source-additive
interactions with those fixed coordinates. No dependence of f on
u,w,q,r, the source, or time is admitted.

This restriction matters. In the broader class, the balanced shift
with coefficient `f_hat=(y-x)*(u+w)^2` is additive and covariant too:
its own displacement fixes u+w, negation reverses its sign, and b
fixes its coefficient. It depends on receiver coordinates excluded
from (5). Neither (11) nor (15) is a completeness claim for that
broader class or for all possible contact architectures.

For every f, without any preparation restriction,

    C_s^f C_t^f=C_(s+t)^f,  C_0^f=identity,
    (C_s^f)^(-1)=C_(-s)^f,
    S(C_s^f v)=S(v),  z(C_s^f v)=z(v),
    M(C_s^f v)=M(v)+2*(y-x)*f(x,y)*s.                  (6)

The group and inverse identities hold because x,y and the source are
not altered. The M identity follows by expanding
`2*(x*(u-fs)+y*(w+fs))`; it has no unaccounted quadratic displacement
term. It describes the contact on the whole carrier, including every
unprepared or occupied auxiliary coordinate.

From (3), comparison of the shifted second slots gives

    d C_s^f=C_s^f d and e C_s^f=C_s^f e
        iff f(-x,-y)=-f(x,y),
    b C_s^f=C_s^f b
        iff f(-y,-x)=f(x,y).                           (7)

Necessity follows by choosing s=1, and sufficiency holds in every
coordinate. Together these conditions are equivalent to

    f(-x,-y)=-f(x,y),  f(y,x)=-f(x,y).                 (8)

Define c=x+y and h=y-x, so that
`x=3*(c-h), y=3*(c+h)`. Denote the same function in this invertible
chart by F(c,h). Conditions (8) become exactly

    F(-c,h)=F(c,h),  F(c,-h)=-F(c,h).                  (9)

In particular F(c,0)=0. On the remaining points the six free values
are

    F(c0,h0),  c0 in {0,1,2}, h0 in {1,2}.             (10)

The first argument extends evenly to +/-c0, and the second extends
oddly to +/-h0. This construction covers all twenty h!=0 points and
the five h=0 points without conflicting assignments. The six signed
orbits have sizes 2,2,4,4,4,4. Conversely every function satisfying
(9) is uniquely determined by (10). There are therefore exactly

    5^6=15625                                           (11)

distinct full contact laws in the declared class. Distinct functions
give distinct maps by setting s=1; this count is not a count modulo
agreement on a smaller prepared family.

Since (5) preserves z, its selected native letter is unchanged. On the
stable union, (7) therefore gives

    G_n C_s^f=C_s^f G_n                                (12)

for every native time n. Induction gives this equality for every
finite stable continuation, with equality of whole checkpoints and
of all selected-letter and trace paths. No periodicity or finite
search horizon for theta is assumed.

## 4. The occupied-SUM comparison and the exact remaining freedom

On (4), the chart values are exactly c=+/-1,h=+/-2. The contact changes
M by s for every independent source s precisely when

    2*h*F(c,h)=1                                      (13)

there. Evenness in c and oddness in h make the left side constant on
this orbit. At (x,y)=(4,2), (c,h)=(1,3), so (13) is exactly

    F(1,3)=1, equivalently F(1,2)=4.                  (14)

This fixes one of the six values (10), leaving exactly

    5^5=3125                                           (15)

full laws. A convenient representative is

    f_*(x,y)=2*(y-x).                                 (16)

It satisfies (8) everywhere and (14). Equations (11) and (15) are
complete classifications only inside (5) and its frozen covariance
requirements. The unit-gain comparison (13) is an extra target
normalization, not an independent physical selection principle.

There is precisely one normalized affine member of this class.
For `f=alpha*x+beta*y+gamma`, (8) forces gamma=0 and beta=-alpha.
At (4,2), condition (14) reads 2*alpha=1, giving
`(alpha,beta)=(3,2)`, exactly (16). Restricting to affine dependence
is a further mathematical class choice, not a physical derivation.

Every law counted by (15) gives the identical complete contact map
on every checkpoint in (4), for all other coordinates and all s.
They consequently give identical whole prepared trajectories below.
Their nonuniqueness concerns off-orbit extensions of the complete
law; it does not produce competing outcomes of this experiment.

There is a sharp limitation even inside the declared class. At h=0
every admitted F is zero, so M cannot change at all. Thus no class
member gives M'=M+s on the entire carrier or even the entire stable
union. For example

    v=(1,0,4,0,1,0) in H1, s=1

has x=y=0 and M=0, and every admitted contact fixes v. Also no
nonzero constant f satisfies (8). A fixed nonzero source-controlled
translation without the declared receiver dependence cannot be
covariant in this class.

## 5. One autonomous law with one continuing counter

Choose one N>=4, independent of t,s1,s2, and one law satisfying (14).
Define the total forward map

    W_N(n,v,s) =
        (n+1, G_n(C_s^f v), s), if n=N,
        (n+1, G_n(v), s),       otherwise.             (17)

This is one autonomous map on Omega_ext: n is a state coordinate,
and the trigger is evaluated on that same unbounded native counter.
Every update executes exactly one actual native step with theta_n.
The counter is never reset. There is no runtime external insertion
of s2 and no omitted phase or completion bit. The special step
contains the declared contact followed by a native step; it is not
asserted to be a single operation of the original U.

Let v_n^0 be the checkpoint of `U^n(0,E_SUM(s1,t))`, and let
`(n,v_n,s2)=W_N^n E(t,s1,s2)`. Then the exact complete-state formula is

    v_n=v_n^0,           0<=n<=N,
    v_n=C_(s2)^f v_n^0,  n>=N+1.                      (18)

The first case is immediate from (17). At the contact step (12)
gives `G_N C_s^f v_N^0=C_s^f v_(N+1)^0`. Repeated application of
(12) proves the second case for every later n. Throughout, the
source coordinate is still exactly its initial s2.
Also `(q_n,r_n,s2)` equals the corresponding unconstrained native
trajectory's `(q_n^0,r_n^0,s2)` at every boundary. The original q,r
are not constant in time; their actual free evolution is preserved.

Combining (6), (13), (18), and S^2=1 along the tail proves

    R(v_0)=t,
    R(v_n)=t+s1,       3<=n<=N,
    R(v_n)=t+s1+s2,    n>=N+1.                        (19)

This is the same receiver function at all displayed times. It is
not claimed to report a valid intermediate value at n=1 or n=2.
N>=4 provides at least one actually elapsed native step of the
first stable record before the second contact. For N=4 the first
record is readable at checkpoints 3 and 4 and the second at every
checkpoint from 5. Equation (19) is not inferred from finite tests:
the proof covers every fixed integer N>=4 and the unbounded tail.

The numerical source value zero is a valid input and gives the
identity contact. No separate absence symbol, arrival detector,
two simultaneous archives, or independently implemented readiness
detector is claimed. The first sum is the current record during its
declared interval; the later record is the accumulated sum.

## 6. Exact inverses and their domain

The joint contact `(v,s)->(C_s^f v,s)` is a permutation on all F5^7
with the full inverse stated in (6). This does not make W_N a
permutation on Omega_ext. In particular the native selector map
on a union of different initial trace sheets can be noninjective,
and the forward N0 counter has no predecessor at zero.

An explicit collision is already present at n=0, before any
trigger N>=4: the distinct checkpoints `(0,0,0,0,0,0)` and
`(2,1,2,1,1,0)` both map to the zero checkpoint, the first through
a and the second through c. With the same arbitrary source s2,
their complete W_N outputs are equal. Thus global injectivity
really fails; it is not merely left unproved.

There is nevertheless a complete inverse on the time slices that
actually arise from H0 x F5. At n=0 these are H0 x F5. Equations
(1)-(2) and the stable table show that at time n they are exactly
`H_(z_n) x F5`, because every step selects one known affine
involution on its entire input sheet. The contact preserves that
sheet and is itself a bijection. This also proves that every
prepared 125-state time slice is injective.

For a supplied positive output time m, set k=m-1 and obtain z_k
from (2). Let `i=(z_k+2 theta_k) mod 5`. The predecessor of
`(m,v',s)` on its actual time slice is exactly

    (k, C_(-s)^f(g_i(v')), s), if k=N,
    (k, g_i(v'), s),          otherwise.              (20)

Each g_i is its own inverse; this reverses the actual order in
(17). It restores all six coordinates and s, including occupied
q,r and receiver coordinates. Iteration recovers the exact prepared
input. Decrementing time in this mathematical inverse is not a
forward reset or an additional operation in (17).

## 7. Admission boundary and planned exact audit

The independent premises consumed are the extra F5 source with its
identity free evolution, the chosen piston-pair contact shape,
its source/receiver coupling and covariance requirement, the fixed
counter trigger and order of substeps, the preparation, and the
chosen receiver function and its interpretation. No conservation
law, energy supply, duration in physical time, physical acquisition
of n, physical contact or physical record is supplied.

Native b,d,e preserve M, while every unit-gain contact changes M
by nonzero s on the prepared tail. Thus selected native tail
steps alone cannot realize the added contact there. This is an
application of the existing native write boundary, not an escape
from it. The canonical paired-fibre translation transports a
different deviation and does not supply the missing interaction.

The accompanying primary.py is a self-contained, standard-library,
integer audit of the exposed proof. It is intended to enumerate
all 15625 contact functions via the six signed orbits, check all
25 points of every function and the 3125 unit-gain survivors,
and hash both complete sets as concatenated lexicographically
sorted 25-byte tables, with point order `(x,y)` lexicographic over
`0,...,4` and table values `0,...,4`, without delimiters. It will
check the representative's full-state inverse, three generator
commutations and M law on all 78125 checkpoint/source pairs, and
check complete prepared histories at triggers 4,5,6,9,16,31,64
through 64 subsequent native steps, including the actual free
source coordinates q,r and unchanged added source s2 at every
boundary. Its off-support and global-collision witnesses reject
the stronger whole-carrier unit-gain and injectivity claims. These finite
checks do not replace the all-time proof or admit the architecture.
No execution or passing result is asserted by this document.
