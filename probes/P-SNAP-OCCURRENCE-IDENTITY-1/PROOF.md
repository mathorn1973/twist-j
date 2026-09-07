# P-SNAP-OCCURRENCE-IDENTITY-1: occurrence, address and log equality

**NON-CANONICAL; proof-first, result-exposed L1 mathematics.**
Public lock: [#893](https://github.com/mathorn1973/twist-j/issues/893).
The constructions and counterexamples precede execution. No historical
novelty, physical Snap identity, persistent apparatus write or new Canon
status is claimed. Each equality below belongs to its specified carrier.

## 1. Exact classification of autonomous counter-address quotients

Let E be an equivalence relation on N_0 satisfying successor preservation:

    n E m  implies  (n+1) E (m+1).                         (1)

Then E is equality, or there are unique mu>=0 and p>=1 such that

    n E m iff n=m or (n,m>=mu and p divides n-m).           (2)

Proof. Put q_n=[n]_E. Equation (1) makes T(q_n)=q_(n+1) well-defined.
If no class repeats, E is equality. Otherwise choose the least j>=1 for
which q_j=q_i with i<j. The j classes q_0,...,q_(j-1) are distinct, so i
is unique. Set mu=i, p=j-i. Iterating T gives q_(j+t)=q_(i+t) for t>=0.
Every index n>=j therefore reduces by p until it lies in [mu,j-1]. These
representatives and the earlier transient representatives are all distinct.
This proves (2), including the absence of further identifications. The
first repeated endpoint recovers j and i, proving uniqueness. Conversely,
each relation (2) is an equivalence satisfying (1). It has mu+p classes.

Add the reflection/cancellation condition

    (n+1) E (m+1)  implies  n E m.                         (3)

For mu>0, the inequivalent indices mu-1 and mu+p-1 have equivalent
successors mu and mu+p, contradicting (3). For mu=0, modular arithmetic
gives (3); equality also satisfies it. Thus the cancellative possibilities
are exactly equality and reduction modulo p, including total equality for
p=1. Condition (3) says T is injective on the reachable quotient. It does
not by itself say T is surjective: successor on the equality quotient N_0
has no preimage of zero. On a finite quotient injectivity does give a
permutation, and the pointed orbit has mu=0.

For a deterministic address read h:N_0->A, its equality kernel satisfies
(1) if and only if an autonomous map T on h(N_0) obeys h(n+1)=T(h(n)).
The forward implication defines T(h(n))=h(n+1), with (1) ensuring that
the value is independent of representative. The reverse implication is
immediate. An arbitrary deterministic h need not qualify: h(0)=h(1)=0,
h(n)=1 for n>=2 has equal addresses at 0,1 but different successor values.
Repeated native checkpoint or decoder values therefore cannot be assumed
to define an autonomous quotient without this additional closure property.

Within this contract, a repeated address forces finite eventual periodicity;
an infinite reachable address set forces equality. At most M reachable
addresses imply mu+p<=M. Fresh addresses for N occurrences need at least
N distinct values. Nevertheless constant addresses, periodic phase tags
n mod p, and fresh tags n all satisfy (1) and (3). Homogeneity and address
cancellation alone do not select freshness.

For a finite prefix {0,...,N}, test (1) only where both successors remain
in that prefix. The same first-repeat proof shows that the possibilities
are equality and the restrictions of (2) with mu+p<=N. Their number is
1+sum_(j=1)^N j=1+N(N+1)/2. Adding (3) leaves equality and p=1,...,N,
hence N+1 possibilities. At N=0 there is just the equality relation.
These finite counts are derived here, rather than extrapolated from audits.

For sparse accepted events t_0<t_1<..., this classification can instead
use accepted rank r in N_0. Advancing that rank and advancing native tick
n are different operations; no successor on a sparse subset is presumed.
An empty or finite accepted stream does not supply an infinite rank orbit.

As background, index/period classification is standard monogenic algebra;
see [Harju, Semigroups, printed p. 10](https://users.utu.fi/harju/semigroups/semigroups96.pdf).
The zero-origin proof above is complete and uses no external computation.

## 2. Histories: append congruence does not force an exact log

Let Sigma* be the finite words over an alphabet Sigma, with empty word eps.
A right congruence satisfies u E v => uw E vw for every suffix w. It is
exactly the kernel of a pointed deterministic history reader. Indeed take
states [u], root [eps], and append transition delta([u],a)=[ua]. The right
congruence makes each transition well-defined, and every state is reachable.
Conversely, equal states in a deterministic reader remain equal after every
common suffix. Requiring compatibility with common prefixes as well gives
a two-sided monoid congruence; the quotient multiplication [u][v]=[uv]
is then well-defined. These are different requirements.

Examples of monoid congruences include exact words, total identification,
length modulo p, Parikh counts (one count per letter), and the set of letters
that occurred. Concatenation respectively preserves the word, adds lengths,
adds count vectors, or unions sets. Parikh counts identify ab with ba;
set accumulation identifies aa with a. For p>=1, length modulo p satisfies
ua E va => u E v, by cancelling one from the residues. Parikh equality
has the same cancellation by subtracting the unit count of a. Thus even
cancellation of an appended known symbol need not recover the history.

A precise recoverable-word contract does force exact equality:

    [eps]_E={eps},
    ua E vb  implies  a=b and u E v   (a,b in Sigma).       (4)

Starting with equivalent words, repeatedly recover their final symbols and
predecessors using (4). If their lengths differed, this would eventually
identify eps with a nonempty word. Otherwise every recovered letter agrees,
so the words are equal. Exact word equality satisfies (4), proving both
directions. This expresses an empty marker and recovery of the last payload
and preceding log; it is a log contract, not a consequence of native U.
Merely preserving equal-length prefix classes is weaker: length equality
does so while forgetting every payload.

For output alphabet {0,1,*}, let * mean SILENT. The map sending 0 to 0,
1 to 1, and * to eps extends by concatenation to a monoid morphism into
{0,1}*. Its kernel is therefore a consistent history congruence. It identifies
0*0 with 00, losing tick timing, but 00 remains different from 0: accepted
multiplicity survives. A formal append-only accepted log distinguishes
repeated equal payloads by position because word equality was chosen.
Timestamped words, bags, sets and phase summaries choose other identities.
None of these definitions alone demonstrates a physically retained record.

## 3. Derived native finite-window identity obstruction

Without any native or autonomy hypothesis, an identity alphabet A of finite
size can injectively tag at most |A| occurrences. This is the pigeonhole
bound alone; it does not imply recurrence or bounded gaps of any label.

Use the unchanged origin-zero native trajectory U^n(0,x_0)=(n,x_n),
x_0 in F5^6, and decorated letters d_n=(x_n,theta_n), where
theta_n=popcount(n) mod 2. Fix one finite L>=1 and one fixed function

    f: legal length-L decorated windows -> I union {*},
    id_n=f(d_(n-L+1),...,d_n),             n>=L+2,          (5)

where I is any set of identity labels with literal equality, and * is a
separate SILENT symbol. No absolute counter, growing history, changed
context, independent persistent memory or input is supplied to f.

The exact dependencies are
[P-U-FINITE-READER-INDEPENDENCE-1/PROOF.md](../P-U-FINITE-READER-INDEPENDENCE-1/PROOF.md),
sections 1-4, and the full-trajectory proofs explicitly cited in its section
2. They establish 3,125 synchronized charts, each a length-two morphic
image of a primitive length-two substitution on 100 clock letters, with
every letter occurring in every depth-77 substituted letter. They apply
to the actual unbounded-counter trajectory, not a periodic surrogate.

For completeness, their consequences needed here follow directly. A native
factor of length L fits in two adjacent aligned superblocks of length
B=2^(j+1), with L<=B<=2L. Its ordered ancestor pair has at most 100^2
choices and its offset has B choices. Thus the legal L-window count on
one chart is at most 20,000 L. If a legal window W occurs, choose j with
W in the finite prefix psi(sigma^j(c_0)). Primitivity puts this prefix
inside psi(sigma^(j+77)(c)) for every letter c. Every aligned block of
length 2^(j+78) therefore contains W, and every interval of 2^(j+79)
letters within the synchronized tail contains a whole such block. Thus
occurrences of W have bounded gaps between their admitted right endpoints.

It follows that (5) emits at most 20,000 L distinct non-SILENT identities
on one trajectory, and every emitted identity recurs infinitely often
with bounded gaps: fix any window yielding that identity and use its
recurrence. This holds even if I itself is infinite. Across all charts
the union has at most 62,500,000 L identities. Acceptance is either empty
or infinite. Hence a nonempty reader of the class (5) cannot issue a fresh
literal identity at every accepted occurrence. These are consequences of
the inherited arbitrary-length coding and recurrence proofs, not finite
prefix extrapolations or assumptions about an autonomous address quotient.
This does not rule out distinct physical events: repeated labels may
describe different occurrences whose identities
are supplied by external history positions or another relational carrier.
The excluded task is fresh reader-derived literal IDs, not repeated events.

If the same fixed reader also receives a state in a fixed finite apparatus
set A, its input pairs have at most |A|20,000 L possibilities per chart.
Its distinct output IDs obey that bound regardless of the apparatus-state
update. This pigeonhole argument does not establish recurrence of each ID
for arbitrary added dynamics. Infinitely many accepted occurrences still
cannot all have distinct IDs in this enlarged finite-input class.

The full counter permits the mathematical tag (n,id_n), which is fresh
within one trajectory whenever emitted; accepted-rank tagging is another
fresh construction with an additional accumulated-rank input. Both enlarge
the read domain beyond (5). Counter values alone need not distinguish
different preparations at the same tick. No identity across contexts or
merged source histories is inferred. A trace indexed externally by n is
also not automatically a separately written apparatus log.

## 4. Atomic emission capacity and an exact serial construction

Suppose an append-only log starts with L_0 atomic entries and each tick
appends a word of at most c entries, where c>=0 is fixed. After N ticks,

    L_N=L_0+sum_(k=0)^(N-1) b_k <= L_0+cN,   0<=b_k<=c.  (6)

This bound is sharp: append exactly c entries per tick; fresh tokens can
be (k,j), 1<=j<=c. From an empty log, writing V distinct atomic entries
requires at least ceil(V/c) ticks when c>=1; when c=0 no positive target
can be reached. The bound concerns atomic entries, not the cardinality
of a relational set encoded in one structured entry or integer count.

Here is a sharp one-entry-per-tick realization of the previous cubic tagged
carrier. Choose the explicitly additional integer lift from
[P-RELATIONAL-GROWTH-SATURATION-1/PROOF.md](../P-RELATIONAL-GROWTH-SATURATION-1/PROOF.md),
section 4. Its derived translation lattice is Z^2 with steps
+/-e1,+/-e2,+/-(e1+e2). A step changes x,y,x-y by at most one; diagonal
then axial steps for matching signs, and axial steps for opposite signs,
attain the lower bound rho(x,y)=max(|x|,|y|,|x-y|).

Let B_r={z:rho(z)<=r}. For -r<=x<=r, its row has

    l_r(x)=max(-r,x-r),    u_r(x)=min(r,x+r),
    ell_r(x)=u_r(x)-l_r(x)+1=2r+1-|x|.

Summing rows gives H_r=3r(r+1)+1=(r+1)^3-r^3. Order B_r lexicographically
by x and then y, and define its zero-based rank

    k_r(x,y)=sum_(u=-r)^(x-1) ell_r(u) + y-l_r(x).         (7)

The row intervals are consecutive, disjoint and of lengths ell_r(x), so
(7) bijects B_r with {0,...,H_r-1}, including B_0={(0,0)}. Consequently

    (r,x,y) -> n=r^3+k_r(x,y)                              (8)

maps the disjoint union of all tagged B_r bijectively onto N_0: its intervals
[r^3,(r+1)^3) partition N_0. Given n, integer comparisons find the unique
r with r^3<=n<(r+1)^3; consecutive row sums determine x uniquely, and
(7) then recovers y. Thus the inverse is a completely specified integer
algorithm. At tick n output this one tagged point. After N=(R+1)^3 ticks,
the log contains exactly all (r,z) with 0<=r<=R and z in B_r, each once.
It attains (6) with c=1. At arbitrary N the entry count is exactly N.
For c>=1, emit up to c consecutive slots per tick, stopping at the finite
target V=(R+1)^3. This reaches it in exactly ceil(V/c) ticks, with a partial
last batch when needed, attaining the general atomic-capacity lower bound.

This is a chosen serialization, not a geometric law of tick frequency:
radius advances on a cube-root schedule, and completing layer r requires
H_r ticks. Lexicographic order is an enumeration convention, not a claim
that consecutive outputs are neighboring native states or one native move
apart. Reading (8) from U's explicit counter is mathematically possible;
its computation, physical storage and geometry are not thereby realized.
The integer lift, layer tags and schedule are all additional choices.
Forgetting tags leaves only the largest ball, whose count is quadratic.
The literal modulo-five quotient instead saturates at 25 points.

## 5. Disposition

Successor homogeneity and cancellation underdetermine occurrence identity.
The native fixed-window class cannot produce forever-fresh literal tags;
counter and recoverable-word constructions can, within their declared
enlarged domains. One atomic write per tick is compatible with a serialized
cubic tagged carrier, but its count is cubic in the chosen radius and
linear in elapsed ticks. None of these statements selects a physical Snap,
event equality, persistent record or spatial radius. That bridge remains
STOP-DEFINITION. Canon, Registry and physical owners remain unchanged;
finite audits check the written proofs and establish no unstated limit.
