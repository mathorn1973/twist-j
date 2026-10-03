# Exact autonomous factors of a current checkpoint

**NON-CANONICAL / candidate-T / L1 only.**
Author: A. M. Thorn <thorn@twistj.com>. Owner #1290.
All source links below refer to the v94 base pinned in PREREG.md.

## 1. Inherited native coordinates and domains

Put X=F5^6, x=(p1,p4,p1p,p4p,q,r), z=sum x_i, and

    theta_n=s_2(n) mod2,
    F_t(x)=g_(z(x)+2t mod5)(x),
    U(n,x)=(n+1,F_(theta_n)(x)),
    E_n(x0)=pr_X U^n(0,x0).

The unchanged generators are

    a(x)=(p4,p1,p4p,p1p,q,r),
    b(x)=(-p1p,-p4p,-p1,-p4,-q,-r),
    c(x)=(-p1p+2,-p4p+1+r,-p1+2,-p4+1-r,1-q,-r),
    d(x)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
    e(x)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).

All checkpoint arithmetic is in F5. KERNEL-Z6-SYNCHRONIZATION [T] gives,
for every n>=3,

    E_n(X)=X_n={x:z(x)=4+2theta_(n-1)}.

In particular the entire indicated sheet, not merely some sampled states,
is reached when the head varies. Set X14={x:z(x) in {1,4}}.

U-NATIVE-INVARIANT-AND-NOWRITE [T], proved in
[MEMORY-PROOF, sections 1-2](../../probes/P-U-NATIVE-MEMORY-EVENT-1/MEMORY-PROOF.md),
supplies the following present-checkpoint chart:

    A=p1+p1p, B=p4+p4p,
    C=p1-p1p-2, D=p4-p4p-1,
    chi(1)=1, chi(4)=-1,
    V(x)=(A,B,chi(z) C,chi(z) D).

The map x -> (z,V(x),r) is a bijection
X14 -> {1,4} x F5^4 x F5. For v=(u1,u2,u3,u4), its inverse is

    C=chi(z) u3, D=chi(z) u4,
    p1=3(u1+2+C), p1p=3(u1-2-C),
    p4=3(u2+1+D), p4p=3(u2-1-D),
    q=z-u1-u2-r.

The factor 3 is the inverse of 2 in F5. In these coordinates the two
selected operations on X14 are the involutions

    beta(z,v,r)=(5-z,-v,-r),
    delta(z,v,r)=(z,-v,1-r).                         (1)

Here beta is b. Delta is d on z=1 and e on z=4; it is a single piecewise
map, not a newly added native generator. Both send V to -V. The coordinate
identities, the ten-point orbit of delta beta at fixed V, and the 313
invariant sign classes are inherited facts. The new question permits a
changing autonomous target value, rather than demanding an invariant.

## 2. The actual-drive condition gives exactly both edge equations

Fix any set Y, any self-map L:Y->Y and one function f:X14->Y. The primary
condition is

    f(F_(theta_n)(x))=L(f(x))
    for every n>=3 and every x in X_n.              (2)

The actual adjacent drive pairs occur as follows:

| n | (theta_(n-1),theta_n) | X_n | Selected map |
| --- | --- | --- | --- |
| 3 | (1,0) | z=1 | b |
| 4 | (0,1) | z=4 | b |
| 6 | (0,0) | z=4 | e |
| 8 | (1,1) | z=1 | d |

These four bit pairs follow directly from the binary expansions of
2,3,4,5,6,7,8. Full-sheet reachability therefore makes (2) imply

    f beta = L f = f delta on X14.                 (3)

Conversely every synchronized native step is one of beta,delta, so (3)
implies (2). This equivalence uses all heads and the named actual times.
It does not claim that one native trajectory realizes every freely chosen
control word. Compositions below are deductions from simultaneous function
identities (3), not a change to the native drive.

## 3. Complete covariant factor and realized target systems

**Theorem A.** For the class (2), the exact classification is

    f=h V,  h:F5^4->Y,
    h(-v)=L(h(v)) for every v.                     (4)

For each admitted f the h is unique. No injectivity assumption on L is
needed. On the realized image I=f(X14), L is automatically an involutive
bijection.

Proof. Applying beta twice in (3) gives L^2 f=f. Also
L(I)=f(beta(X14))=I because beta is onto. Thus L|I is its own inverse.
Put K=delta beta. Formula (1) gives

    K(z,v,r)=(5-z,v,r+1),  f K=L^2 f=f.

For k=0,...,9 its iterates exhaust both z values and every r at fixed v:
the pairs (k mod2,k mod5) are all distinct. Hence f is constant on each
V-fibre, and V is onto, proving unique factorization f=h V. Equation (3)
then gives h(-v)=Lh(v). Conversely (4) and V beta=V delta=-V immediately
give (3). QED.

The read V itself is admitted with target P=F5^4 and s(v)=-v. Thus two
source states are identified by every admitted read if and only if their
V values agree. This is the stated maximal covariant factor. Any other
surjective factor with the same unique-factorization property is isomorphic
to (P,s): factoring the two universal maps through each other makes their
composites identity by uniqueness and surjectivity. No physical selection
of this input class follows from that elementary universal property.

**Corollary A1 (sharp image classification).** If the induced target on I
has a fixed points and b two-cycles, then exactly the following pairs occur:

    a,b are nonnegative integers,
    a>=1,  a+b<=313.                               (5)

Indeed P has the singleton {0} and 312 two-point s-orbits. The singleton
must map to a fixed point; every other source orbit maps into one target
orbit. Surjectivity onto I gives (5). Conversely, choose a fixed target
point as h(0); use a-1 source pairs, collapsed separately, for the remaining
fixed points, and b source pairs for the distinct two-cycles. There are
enough source pairs exactly when a+b<=313. Send all unused pairs to h(0).
This is a surjective h satisfying (4). QED.

For a prescribed Y,L, the same statement applies to any proposed finite
invariant image having these orbit counts; unused target points are
unconstrained. The largest image has 625 points, attained by V. A global
reader into a pure two-cycle cannot exist because h(0) must be fixed.
The special case L=id gives exactly f=g({V,-V}), the inherited 313-class
maximal invariant. Invariance and covariance must not be conflated.

## 4. A reader total on every native checkpoint is stationary

Now change the domain explicitly. Let f:X->Y be fixed and require
f(F_(theta_n)(x))=L f(x) for all n>=0 and all x in X, not just E_n(X).
Since theta_0=0 and theta_1=1, this is equivalent to

    f F_0=L f=f F_1 on all X.                      (6)

The inherited U-COUNTER-SEPARABLE-QUOTIENT [T], proved in
[counter-amplitude PROOF, section 2](../../probes/P-U-COUNTER-AMPLITUDE-CLASS-1/PROOF.md),
classifies the weak components of this two-control graph. In the notation
of section 1 put S=A+B, T=C+D and

    kappa(x)=(S-1,-T-2r) if z=0,
             (S,T)       if z=1 or2,
             (S,-T)      if z=3 or4;
    Q(x)=[kappa(x)] in F5^2/{+1,-1}.               (7)

Exactly thirteen Q-fibres are the weak components, and Q F_t=Q.
These statements, including connectivity, are inherited premises.

**Theorem B.** Even for arbitrary self-maps L, all reads (6) are exactly

    f=g Q,
    g:F5^2/{+1,-1}->Fix(L).                        (8)

Proof. Every x has a two-edge return using the following control word:

| Starting phase | Chronological controls | Generators | Phases |
| --- | --- | --- | --- |
| 0 | 00 | aa | 0,0,0 |
| 1 | 11 | dd | 1,1,1 |
| 2 | 01 | cc | 2,0,2 |
| 3 | 11 | aa | 3,3,3 |
| 4 | 00 | ee | 4,4,4 |

The generators in each row are involutions. Equation (6) applied along
the indicated return gives L^2 f(x)=f(x). Thus L is an involution on f(X),
which is closed under L; this justifies using its inverse on that image
without an assumption about the rest of Y.

Every Q-component contains a point fixed by F_0=a. To see this, for u,v in
F5 choose

    x(u,v)=(u,u,v,v,-2(u+v),0).

It has z=0 and is fixed by a. At this point (7) is

    kappa=(2(u+v)-1, 3-2(u-v)).                     (9)

The linear coefficient matrix in (u,v) has determinant 8=3 in F5, so
these representatives cover every oriented kappa, hence every Q-class.
Its f value is fixed by L. Along any weak graph edge the same fixed value
propagates in either direction, because L is invertible on f(X). The whole
Q-component therefore has that value. This proves (8) and uniqueness of g.
Conversely Q F_t=Q and Lg=g prove (6). QED.

This class is stronger than the origin-zero reachable-tail class. Nor is
it the whole-Omega separable class R(n,x)=L^n g(Q(x)), which explicitly
receives n. There is no domain identification between these statements.
All thirteen stationary values can be retained by taking f=Q and L=id.

## 5. Sharp exclusion of the marked J targets

**Corollary C.** Let the target be a vector space and L a linear operator
with ker(L^2-I)={0}. Every read in Theorem A is zero. This follows directly
from L^2 f=f and does not assume f linear.

The scalar multiplication M_J on K=Q(j) meets this condition: J^2!=1,
and multiplication by the nonzero field element J^2-1 is injective.
The same conclusion applies on its integral lattice or after real or
complex scalar extension.

For the already marked exterior operator L_J=Lambda^2 M_J, the inherited
U-J-HODGE-FINITE-READER-BOUNDARY [T] gives complementary invariant sectors
with annihilating polynomials

    p(t)=t^2-3t+1,
    q(t)=t^4-t^3+t^2-t+1.

Their values at +/-1 are

    p(1)=-1, p(-1)=5, q(1)=1, q(-1)=5.

Consequently their product is coprime to t^2-1, and L_J^2-I is invertible.
This uses the spectrum already proved in
[finite-reader PROOF, sections 1-2](../../probes/P-U-J-HODGE-CHECKPOINT-NOGO-1/PROOF.md).
Thus even its nonzero period-ten sector cannot be read in Theorem A's
class. The old finite-image theorem only excluded the hyperbolic sector
for general fixed finite configurations; it did not assert that a native
current-checkpoint read realizes the remaining sector. The new result
uses the actual source edges, on a narrower input class.

If a fixed f:X->Y into either of these invertible linear targets obeys the
law on all origin-zero reachable times including 0, its restriction to
the tail is zero. Then L^3 f(x0)=f(E_3(x0))=0 and invertibility gives
f(x0)=0 for every head. This is a corollary for those targets, not a
classification of all target self-maps on that intermediate domain.

Counter-dependent reads, finite-history reads, finite auxiliary memory,
changed source carriers and selected sampling times are not excluded by
this argument. In particular it does not strengthen the general
finite-reader theorem to a no-go for every period-ten realization.

## 6. Complete symmetric metric class on the maximal factor

Freeze P=F5^4, s(v)=-v. We now ADD the metric condition that d be invariant
under every automorphism of this bare finite dynamical system. These are
permutations commuting with s, not asserted symmetries of all original
marked native or cyclotomic data.

There is one fixed point 0 and 312 disjoint two-cycles. Every automorphism
fixes 0, can arbitrarily permute the two-cycles and can independently
exchange either pair's endpoints. Conversely all these permutations commute
with s. Thus Aut(P,s) is C2 wreath Sym(312).

**Theorem D.** Its invariant real-valued metrics are exactly the following
three-parameter family, with d(v,v)=0:

    d(v,-v)=a             for v!=0,
    d(v,w)=b              for nonzero v,w with w!=v,-v,
    d(0,v)=d(v,0)=c       for v!=0,

where

    a,b,c>0,   a<=2b,   a<=2c,   b<=2c.             (10)

Proof. There are precisely three automorphism orbits of unordered distinct
pairs: partners, different nonzero pairs, and a pair containing zero.
Invariance therefore forces the displayed form. Positivity is necessary.
The distinct-point triangles have side multisets (a,b,b), (a,c,c),
(b,c,c), or (b,b,b); all types occur. Their only nontrivial inequalities
are exactly (10). Conversely those inequalities check every such triangle;
triangles with repeated vertices are automatic. QED.

Even after the additional normalization a=1, both

    (a,b,c)=(1,2,2) and (1,3,3)                    (11)

are admitted. Their nonzero distance sets are {1,2} and {1,3}, so they are
not isometric, even if labels and the dynamics are forgotten. Their minimum
positive distance is one, so an overall rescaling cannot identify them.

The metric class is a deliberately strong symmetry requirement on the
derived factor. Its nonselection cannot be repaired merely by asking for
the same symmetry or by fixing the length of a step pair. Additional
metric-sensitive structure would be a new declared input. The result does
not demand global decoder uniqueness, classify all native geometric reads,
or establish any physical dimensional or curvature obstruction.

## 7. What this restriction resolves and what it leaves open

The counter-dependent class in U-COUNTER-REACHABLE-AMPLITUDE-CLASS [T]
allows every stipulated bijection L through L^n G(ell_n(x)). The fixed
current-checkpoint class instead has the complete factor (P,-id); totality
on all Omega reduces it further to the stationary thirteen-class quotient.
This demonstrates an exact cost of removing the counter from that input
contract. It does not prove that physics must use a counter-free reader.

The original checkpoint trajectories remain aperiodic. A general fixed
observation of them can also be aperiodic because it need not admit any
deterministic autonomous update from its own present output. Theorems A/B
classify the added autonomous-output condition, not every observation.

Neither a sign cycle nor a stationary quotient is identified with physical
time. No material memory, locality, spatial continuum, event law, apparatus
or independent initial field is supplied. The metric counterexamples leave
the finite abstract factor fixed; they do not enlarge the native source or
evade the previously stated configuration-capacity limits.

All new conclusions are candidate-T at L1. No public scientific claim or
live H/O owner changes status in this note.
