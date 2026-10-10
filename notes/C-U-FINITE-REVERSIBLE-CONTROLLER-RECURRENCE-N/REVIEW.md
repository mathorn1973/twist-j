# Independent symbolic review: finite reversible controller recurrence

**NON-CANONICAL. Conditional mathematical review at L1. No execution.**

This review was derived from the exposed common statement before reading
the companion PROOF.md or the scope author's draft. The proposed result,
the finite-group route and the intended Thue-Morse application were already
known. This is a separate derivation within one coordinated assistant team,
not blind prediction, external peer review or independent physical evidence.
No scientific program, enumeration or verifier was executed for this review.

The conclusion is affirmative under the exact hypotheses below. A crucial
distinction is recurrence of an auxiliary finite-window skew product versus
recurrence of the public autonomous state with its increasing integer clock.

## 1. Exact statement accepted by this review

Let X be a nonempty compact metric space and S:X->X a minimal homeomorphism.
Let B be a nonempty finite discrete set containing the complete varying
finite state admitted by the controller model. Assume a continuous map

    pi:X -> Sym(B),
    T(x,b)=(Sx,pi(x)(b)).

Here Sym(B) has the discrete topology. A feedback rule may depend on b:
the requirement is that its WHOLE b-to-next-b map is a permutation for
every x. Choosing individual invertible instructions according to the
current b does not by itself satisfy this requirement.

Then every point of X x B belongs to a minimal subsystem and is uniformly
recurrent. The space is a finite disjoint union of clopen minimal components.
Neither unique ergodicity nor a probability measure is required.

For a subshift X over a finite alphabet, continuity of pi is equivalent to
dependence on one fixed finite coordinate window. Compactness and finiteness
give a common window: take a finite cylinder cover on which pi is constant
and enlarge all cylinder supports to one interval.

## 2. Proof through a finite group extension

Put G=Sym(B) and fix b0 in B. Consider

    F(x,g)=(Sx,pi(x) g),
    p(x,g)=(x,g(b0)).

Composition is written with the right factor acting first. F is a
homeomorphism; its inverse is

    F^-1(x,g)=(S^-1 x,pi(S^-1 x)^-1 g).

The map p is continuous and onto, and p F=T p.

Choose a nonempty compact minimal F-invariant subset M of X x G.
Such a set exists by compactness, taking a minimal nonempty closed invariant
set. Its projection on X is a nonempty compact S-invariant set, hence all
of X by minimality of S.

For h in G define the right translation R_h(x,g)=(x,g h). It commutes
with F, so every R_h(M) is again a minimal compact invariant set. Given
any (x,g), choose (x,g0) in M using the surjectivity of its base projection.
Then (x,g)=R_(g0^-1 g)(x,g0). Consequently

    X x G = union_(h in G) R_h(M).

These are finitely many minimal sets. Two of them are either disjoint or
equal: a nonempty intersection is a closed invariant subset of each.
Thus their distinct members form a finite closed partition and are clopen.

Their images p(R_h(M)) are compact minimal T-invariant sets and cover X x B.
The same disjoint-or-equal argument gives a finite clopen minimal partition
downstairs. In particular, every point lies in a minimal subsystem.

For completeness, a point z in a compact minimal homeomorphism subsystem Y
has syndetic forward returns to each open neighborhood U of z in Y.
The sets T^-k(U), k in Z, cover Y; a finite subcover uses a bounded interval
of integers. Apply that subcover to sufficiently advanced iterates of z:
every sufficiently long forward interval then contains a visit to U.
Enlarging the interval bound covers the finite initial portion as well.
This proves uniform recurrence, not merely recurrence almost everywhere.

## 3. Precise readout and contact consequences

Let r:X x B->Y be one fixed continuous readout, with Y Hausdorff. If

    r(T^n z)=c for all n>=N,

then r(T^k z)=c for every k>=0. Indeed each T^k z is recurrent, so it is
the limit of arbitrarily late iterates of itself; continuity and the
eventually constant tail force its readout to be c. For a metric output
the same argument shows that convergence of r(T^n z) forces the whole
forward readout sequence to be constant at its limit.

Thus a fixed finite-valued readout cannot change nontrivially and then
remain at the new value forever inside this class. This does not prohibit
pre-existing invariant memory, an initially constant nonblank record,
arbitrarily long finite retention, or recurrent writing and undoing.

A contact indicator e:X x B->{0,1} must itself be continuous. If it is one
at some forward time, its later occurrences are syndetic and infinite.
It cannot occur exactly once or finitely many positive times. An indicator
of a transition is covered when e(z,Tz) is a continuous Boolean function
of the current point; finite-window, finite-state transition rules have
this property.

The Boolean continuity requirement matters. Hitting a single closed point
in an infinite minimal system can happen once; a discontinuous indicator
of that event is outside the statement. Likewise, distinct event labels
containing an absolute invocation number are not this fixed finite-state
contact indicator. The theorem does not claim that all repeated contacts
have the same externally assigned event identity.

The proof yields existence of a finite return-gap bound for each particular
point and neighborhood. It derives no numerical recurrence bound, retention
time, first-return index, practical latency or common effective bound from
the cardinality of B alone. No such general quantitative bound is earned
by this compactness argument; a separately specified example may have a
directly proved period.

## 4. Thue-Morse minimality without a simulation premise

For mu(0)=01, mu(1)=10, let theta be the one-sided fixed point beginning
with zero and let X_TM be its two-sided language subshift. Every finite
factor w of theta lies inside a sufficiently long prefix mu^k(0).
Each of mu^(k+1)(0) and mu^(k+1)(1) contains mu^k(0), since mu(0) and
mu(1) both contain zero. The aligned substitution blocks therefore give
bounded gaps for w in theta. This bounded-gap property passes to all
points of the language subshift. Every allowed cylinder is visited by
every orbit, so the two-sided shift is minimal.

There is a two-sided point kappa whose nonnegative coordinates equal theta:
use arbitrarily late occurrences of increasing prefixes of theta and a
compactness limit. This is an auxiliary extension of the drive; it does
not add an accessible physical past or replace the native integer counter.

## 5. Correct native stable carrier and its trivialization

For the original raw checkpoint

    v=(p1,p4,p1p,p4p,q,r) in F5^6,
    z(v)=p1+p4+p1p+p4p+q+r,
    H_j={v:z(v)=j},

the actual H0-origin native path satisfies

    z(v_n)=4+2 theta_(n-1) for every n>=3.

The stable hull is therefore the graph bundle

    E={(x,v):x in X_TM, v in H_(h(x))},
    h(x)=4+2 x_(-1).

Do NOT replace this graph by X_TM x (H1 union H4) and assert that the
fixed-bit native update is a permutation there. For bit zero, both input
sheets map to H4; for bit one, both map to H1. The graph condition is
essential. On its four allowed edges the native generator is

| x_(-1) | x_0 | input sheet | generator | output sheet |
|---|---|---|---|---|
| 0 | 0 | H4 | e | H4 |
| 0 | 1 | H4 | b | H1 |
| 1 | 0 | H1 | b | H4 |
| 1 | 1 | H1 | d | H1 |

Each displayed restriction is a bijection between the indicated sheets,
because b,d,e are affine involutions with those exact trace images.

A concrete common fiber is A=F5^5. For j in {1,4}, define

    phi_j(a1,a2,a3,a4,a5)
      =(a1,a2,a3,a4,a5,j-a1-a2-a3-a4-a5).

This is a bijection A->H_j. Let g_x be the generator in the table and set

    nu_x=phi_(h(Sx))^-1 o g_x o phi_(h(x)).

Then nu_x is a permutation of A depending only on x_(-1),x_0. This gives
an explicit finite permutation cocycle for the stable native checkpoint.
It is consistent with the existing public
TM-CHECKPOINT-HULL-STABLE-IMAGE theorem; it does not strengthen that theorem
into a physical identification of the auxiliary hull with U.

Extra finite source and controller registers can be included by using
B=A x C, where C contains ALL their admitted finite coordinates. The
controlled combined step must be a permutation of this whole B for every
admitted driver context, must retain the graph/fiber interpretation, and
must obey one unchanged local rule on the whole tail under discussion.
Checking an inverse only on an initialized subfamily is insufficient.

## 6. Actual one-sided interfaces and warmup

The public autonomous state remains (n,v,...) with n increasing in N0.
It is not recurrent in that literal state space. The theorem concerns the
projection to a finite-window drive state and complete finite fiber, and
only controls and observations that factor through that projection.
It does not permit observing the discarded absolute n when applying the
recurrence conclusion.

Suppose the declared interface uses x[-a..b]. For the actual one-sided
clock sequence a left window is available without invented data only once
n>=a. To apply the theorem directly to an H0-origin path, choose an actual
start n0 at which the stable graph condition, the entire declared window,
and the fixed total permutation controller law all apply. With the stated
one-sided past convention a necessary simple choice is n0>=max(3,a),
plus any separately declared interface initialization requirements.
Any lookahead b>0 remains an explicit information-access premise.

An artificial origin marker, padded negative indices, a different startup
rule or an incompletely filled history buffer is not automatically a point
of the minimal two-sided driver model. If such a startup occurs, the
conclusion begins only after a valid stationary interface has been reached.
A proposed contact at N>=4 is not covered merely by that inequality when
its declared window or controller interface is unavailable there.

To exclude a permanent second write, both its prior distinct readout and
its claimed permanent tail must lie inside the same admitted regime. An
eventual ready-domain reader cannot be silently treated as a continuous
total reader during a preceding phase where its meaning was not defined.

## 7. A reversible cyclic example passes any chosen finite retention test

After the proof above was written, the coordinator supplied the following
constructive boundary for separate checking. No companion draft or code
was consulted. The check below is symbolic, not a new machine execution.

Fix N>=4 and a finite observation horizon H>=N+1. Take an integer
P>H-3 and a complete controller k in Z/PZ, initialized to zero at the
stable starting boundary n=3. Retain the passive source s2. Put

    a=N-3 in Z/PZ,
    epsilon(k)=1 if k=a, and 0 otherwise.

At every stable step use exactly the same law

    (x,v,s2,k) -> (Sx, G_x(C_s2^epsilon(k)(v)), s2, k+1).

Here C is the unit representative contact from the merged occupied-SUM
proof, and G_x is the actual native branch from the stable four-edge table.
The comparison coordinate n is used only in this analysis of the resulting
orbit; the law itself reads the cyclic k and local driver context. The
constant a and the controller preparation are declared resources.

This is a permutation between the complete context fibers. From the output
recover k_old=k_new-1; undo the actual native branch first; then undo the
contact with source -s2 exactly when epsilon(k_old)=1. Source s2 is unchanged.
The contact preserves z, so this inverse uses the correct stable sheet and
the table's unique native restriction. All controller values are admitted;
the inverse is not restricted to an initialized one-step image.

Since 0<=N-3<P, contacts along this initialization occur at exactly

    n=N+jP, j>=0.

The unit contact commutes with b,d,e, retains its defining centered pair,
and adds s2 to M on the whole occupied SUM orbit. Native continuation
preserves M there. Thus for every boundary n>=3 the same scalar reader is

    R_n=t+s1+c_n*s2 in F5,
    c_n=#{j>=0:N+jP<n}.

There is no contact before N and the first actual composed step changes
the boundary N+1. Moreover N+P>H, so c_n=0 for 3<=n<=N and c_n=1 for
N+1<=n<=H. The finite experiment therefore displays exactly the two desired
record intervals. Later the contacts recur every P steps. For s2!=0 the
readout changes again; after five contacts its accumulated value returns.
For s2=0 a constant record is the expected degenerate case.

This supplies a family of finite reversible examples with arbitrarily long
but finite apparent post-write retention. It neither establishes a minimum
P nor introduces a universal recurrence-time estimate. It proves why an
arbitrarily large fixed finite replay horizon cannot establish permanent
post-write settling in the full class. The one initialization is an explicit
model premise; no controller reset is performed later in the trajectory.

## 8. Countermodels to overstatements and preserved earlier work

1. A finite latch 0->1, 1->1 over any minimal driver writes once and stays
   written. Its restriction from the initialized singleton {0} to {1} has
   an inverse, but the whole map on {0,1} is not a permutation. Thus a
   restricted prepared-image inverse does not earn the hypothesis above.
2. A flip at the externally singled-out absolute time n=N and identity at
   other times uses permutations on a finite register but is not one
   continuous local cocycle over a minimal Thue-Morse driver. The actual
   conditional W_N contact in P-U-OCCUPIED-SUM-COVARIANT-CONTACT-1 uses this
   absolute-counter resource and is outside this controller class.
3. Fresh external arrivals, resets, unbounded memory, a driver changed by
   feedback, nonminimal forcing and a discontinuous whole-tail predicate
   change the stated class. None is ruled out by this theorem.
4. Existing native transient writing is preserved. In particular public
   issue #992, C-U-NATIVE-CONTACT-TRANSIENT-N, singles out entry into X14
   from an unsynchronized checkpoint. Its one-time entry edge occurs in
   the transient noninjective full native dynamics; it is absent throughout
   the stable graph. A permanent post-entry record can already be constant
   at the beginning of the recurrent regime. There is no contradiction.
   The canonical U-NATIVE-SOURCE-RECEIVER-RECORD likewise changes BLANK to
   PRESENT through the actual a,c,e prefix before its n>=3 stable tail.

The last point forbids any wording such as "unchanged native U cannot
write once" or "finite native memory cannot retain a permanent record."
The reviewed result excludes a nontrivial eventual settling or a one-time
continuous contact INSIDE the frozen finite reversible local-controller
regime. It is a conditional mathematical boundary, not a universal physical
apparatus, event, measurement or sampling impossibility.

## 9. Sources inspected and review disposition

The sources read before this review were the exposed common statement,
the merged occupied-contact PREREG/PROOF, the native formulas and stable
sheet table, the following canonical blocks, and the public #992 issue:

- [TM-CHECKPOINT-HULL-STABLE-IMAGE, fixed integration tree](https://github.com/mathorn1973/twist-j/blob/c17fe88ddd3b95ab8ff76ac7923a37f582c97571/canon/CANON.md#L11392).
- [Native one-shot transfer and continuation boundary](https://github.com/mathorn1973/twist-j/blob/c17fe88ddd3b95ab8ff76ac7923a37f582c97571/canon/CANON.md#L7201).
- [Transient contact scope, issue #992](https://github.com/mathorn1973/twist-j/issues/992).
- [Occupied-contact proof with absolute trigger](https://github.com/mathorn1973/twist-j/blob/c17fe88ddd3b95ab8ff76ac7923a37f582c97571/probes/P-U-OCCUPIED-SUM-COVARIANT-CONTACT-1/PROOF.md).

No companion draft or program was read in deriving this proof. The
finite-group argument proves the common statement at the stated scope;
the carrier, origin and interface caveats above are required conditions
for its native application. This review changes no public status, Canon
claim, scientific threshold, source file or previous run record.
