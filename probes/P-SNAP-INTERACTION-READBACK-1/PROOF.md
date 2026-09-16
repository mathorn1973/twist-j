# P-SNAP-INTERACTION-READBACK-1: loading, retention and passive queries

**NON-CANONICAL; proof-first, result-exposed L1 mathematics.**
Public lock: [#895](https://github.com/mathorn1973/twist-j/issues/895).
The examples and proofs precede formal execution. No historical novelty,
physical Snap, selected detector, realized write or new Canon status is
claimed. A payload, an occupied cell, a completed input batch and a threshold
mark are different types throughout.

## 1. An existing exact zero-batch versus readback witness

The conditional model in
[P-QDD-STABILIZER-APPARATUS-1/RECORD-CONTRACT.md](../P-QDD-STABILIZER-APPARATUS-1/RECORD-CONTRACT.md),
sections 1-3, already fixes these facts: READY has no batches and zero
accounts; READ leaves the complete state unchanged; a valid DEPOSIT supplies
all signed channel vectors and their exact total energy, retains them in
one new batch, and emits all newly crossed threshold ordinals. A zero input
is valid and its zero batch remains explicitly recorded.

Fix one context and positive threshold, and start in READY. Compare its
unchanged readback state with the state after depositing zero input energy
and a zero vector in every channel. In both states the stored energy,
per-channel mark counts, remainders and lifetime mark counts are zero. Their
complete histories differ: one contains no batch; the other contains one
zero batch with its input ordinal and signed zero vectors. The number of
new threshold marks is zero in both cases. The distinguishing target here
is the number of completed input batches, zero versus one, not mark count.

The frozen port observation pi retains the source/receiver amplitudes before
and after the coupling and their energies. For this comparison, a READ is
represented by the identity on idle zero ports; a zero DEPOSIT uses the
declared swap on the same pair (0,0). Both observations are the identical
typed tuple (0,0;0,0), with all its energies zero. Pi forgets operation label,
presence, call/pulse ordinal, new-slot address and archive shape/length.
The batch delta is still respectively zero and one, so it cannot be a
function of this amplitude-and-energy transition either. This is the named
compression being tested, not equality of the complete apparatus states.

Consequently the projection retaining only that common context and scalar
energy/count/remainder account cannot recover this target. More generally,
for pi:X->Y and d:X->D, a map e on pi(X) with d=e pi exists if and only if
d is constant on every pi-fibre: necessity follows by applying e; sufficiency
defines e(pi(x))=d(x), independently of representative. This elementary
criterion is already used in the apparatus ownership contract and earlier
native observation probes. It is a scope check here, not a new physical law.

The witness is established by the different retained states, not by giving
an emitter the words READ and DEPOSIT as a substitute for material evidence.
The existing model nevertheless chooses those operations and batch semantics.
It does not prove that Nature counts a zero input batch as one Snap.

## 2. Complete classification of a perfect two-port loader

Let source and record each be Q^m with the same rational positive definite
Gram matrix G, m>=1. Write their orthogonal sum in source/record order.
An orthogonal rational linear W is a perfect cold loader when

    W(s,0)=(0,s) for every s in Q^m.                        (1)

Then the complete class is

    W = [[0,B],[I,0]],             B^T G B=G.               (2)

Proof. Write W=[[A,B],[C,D]]. Equation (1) gives A=0 and C=I.
The source/record off-diagonal block of
W^T diag(G,G) W=diag(G,G) is G D, so D=0 since G is nonsingular.
The remaining record block gives B^T G B=G. Conversely these equations
verify the full orthogonality identity and (1). Thus every perfect loader
obeys

    W(0,r)=(B r,0).                                       (3)

A nonzero occupied record is exported into the source port on reuse with
zero source input; it is not passively retained. This is a statement about
one fixed linear coupling applied again. A passive query, a changed coupling,
or another fresh record port is a different operation or resource.

In particular B=I gives the ordinary swap. Its existence, and earlier
fresh-cell and cold-port constructions, are acknowledged prior inputs:
[P-BINARY-RECORD-QUADRATIC-SELECTION-1/PROOF.md](../P-BINARY-RECORD-QUADRATIC-SELECTION-1/PROOF.md),
section 4, and
[P-DECODER-RESERVOIR-COUPLING-1/PROOF.md](../P-DECODER-RESERVOIR-COUPLING-1/PROOF.md),
sections 2-3. The classification (2) states the whole frozen two-port class;
it does not select any of its members physically.

## 3. Protected records exclude incoming orthogonal transfer

Let V=S orthogonal-sum R be finite-dimensional over Q with a positive
definite Gram form. If an orthogonal W satisfies W(R) subset R, then
W(R)=R: its restriction is injective and the dimensions agree. For s in S
and r in R, write r=W(r_0), r_0 in R. Orthogonality gives

    <W(s),r>=<W(s),W(r_0)>=<s,r_0>=0.

Thus W(S) subset S. An invariant entire record subspace cannot receive
incoming source amplitude through this same fixed coupling.

Even the apparently weaker passive condition P_R W(0,r)=r for every r
forces W(0,r)=(0,r): the squared norm of its source component must be zero
because the unchanged record already accounts for the entire input norm.
Positive definiteness makes that component zero. Hence this passive
condition also excludes incoming transfer. Fixing R pointwise suffices
without a finite-dimensional assumption, by the same inner-product argument.

Two exact controls delimit the premises. The invertible rational shear
W(s,r)=(s,r+s) fixes every (0,r) and transfers source amplitude into R,
but it is not positive-Gram orthogonal and does not clear the source.
Finite dimension also matters for mere invariance. On the space of finitely
supported rational sequences indexed by Z, give the basis e_j its usual
orthonormal form and put W e_j=e_(j+1). This is an orthogonal bijection.
For R=span{e_j:j>=0}, W(R) is a proper subset of R, while W e_(-1)=e_0
enters R. This does not contradict the finite-dimensional argument.

There is a separate set-theoretic no-arrival lemma. If F:X->X is injective,
F(y)=y and F(x)=y, then F(x)=F(y), so x=y. Repeating this argument shows
that an exact complete fixed point cannot first be reached after any finite
number of iterations from another state. A persistent projected record is
not necessarily a complete fixed point; an increasing counter, moving head
or continuing source prevents that substitution.

## 4. Exact fresh-space criterion while retaining old records

Let V=S orthogonal-sum O orthogonal-sum F, with finite-dimensional rational
positive Gram forms. O is the protected old-record subspace; F is fresh
record capacity. Require W to be orthogonal, fix O pointwise, and perfectly
transfer arbitrary s from the source into F:

    W(s,o,0)=(0,o,J s).                                   (4)

Such a W exists exactly when a rational isometric embedding J:S->F exists.
Necessity follows by restricting W to source inputs: preservation of inner
products gives J^*J=I_S, with * denoting the Gram adjoint. This also proves
injectivity of J. Conversely, given such J, put P=JJ^* and define

    W(s,o,f)=(J^*f, o, J s+(I_F-P)f).                     (5)

Since P^2=P=P^*, F decomposes orthogonally as J(S) plus its orthogonal
complement. Formula (5) swaps S with its isometric copy J(S), and fixes O
and that complement. It is therefore rational, orthogonal and involutive,
and directly satisfies (4). Equivalently these properties follow by
substitution using J^*J=I and J^*(I-P)=0.

Consequently dim F>=dim S=m is necessary. Choosing F as a Gram-isometric
copy of S attains equality and gives the swap, but dimension alone is not
sufficient over Q. For one-dimensional forms G_S=(1), G_F=(2), an embedding
would require a rational a/b in lowest terms with 2a^2=b^2. Then b is even,
and substitution makes a even too, a contradiction. With two fresh
coordinates and G_F=diag(2,2), J(s)=(s/2,s/2) is instead isometric because
2(s/2)^2+2(s/2)^2=s^2. These are exact Gram, not approximate dimension,
conditions. If S is the zero space, loading is vacuous and needs no fresh
dimension.

Mere invariance of O protects it from incoming orthogonal transfer, but may
rotate its old values. Pointwise fixing, as in (4), provides exact retention.
These bounds concern arbitrary vectors in the frozen source space and this
linear loading requirement, not a universal physical memory cost per event.

## 5. A fixed finite-bank flow with explicit occupancy

The following positive protocol changes the carrier explicitly. A cell is

    C={BLANK} disjoint-union {occupied(v):v in Q^m}.

In particular BLANK differs from occupied(0). Define occupancy h(BLANK)=0,
h(occupied(v))=1, and energy E(BLANK)=0,
E(occupied(v))=v^T G v. Both tags can have zero energy. This is a typed
symbolic carrier, not one rational vector space with a single zero.

Fix N>=1. A complete bank state is (j,S,R), with head j in Z/N and two
length-N cell arrays S,R. Its one FLOW map swaps S_j and R_j and then
increments the head modulo N. Every other coordinate is unchanged. There
is no READ/WRITE command flag inside this map. Its inverse decrements the
head and swaps that pair. Thus FLOW is a bijection on the entire declared
state set, including warm and occupied input cells.

Total occupancy and total energy across both arrays are conserved, since
one pair of cells is permuted. After N steps every pair has been swapped
once and the head has returned, so

    FLOW^N(j,S,R)=(j,R,S),       FLOW^(2N)=identity.        (6)

This is an all-state identity; an individual state may have a shorter
period. Head cycling does not make record retention indefinite.

The emitter is a function of the complete executed transition. At its old
head j, it returns the singleton [(j,v)] exactly when the record cell changes
from BLANK to occupied(v); otherwise it returns the empty word. This rule
uses an actual pre/post occupancy change and signed payload, not an external
label saying that a call was fresh. A mathematical log appends the emitted
word. The log is a derived history, not another component hidden in (6).
If it is to be physically retained, it needs its own storage contract.

Now start at head zero with every record cell BLANK. Source cells may be
BLANK or carry any occupied payload, including zero. During the first N
steps, each address is visited exactly once. At its visit, the record cell
is still BLANK, so an occupied source transfers its payload to that record,
leaves its source cell BLANK and emits (j,v). A BLANK source emits nothing.
Previously visited record cells are unchanged during the rest of this lap,
because the head has not revisited them. Induction proves the whole claim
for every first-lap prefix, with no condition on whether payloads coincide.

For N>=2, equal occupied arrivals at two different addresses therefore emit
different occurrence tuples (i,v),(j,v), i!=j. This includes v=0. Their
payload equality does not erase their cell or head identities. Freshness
within this prefix follows from the initially blank bank and unused
addresses, not from an independently selected native occurrence law.

A passive query is a stipulated map returning a projection of the state
without changing it or invoking FLOW. Repeated such queries preserve the
same cells and append no transition emission. Equivalently, the identity
transition has no BLANK-to-occupied change. This supplies a precise
mathematical readback operation, but does not prove that a physical observer
can implement it noninvasively. Observing and evolving remain different
typed maps; a physical read interaction needs its own full input and action.

The finite resource boundary is exact. After the first lap, all initially
occupied source cells have moved to R and their S cells are BLANK. During
the second lap, each is swapped back: its old record is emptied, with no
new emission under the frozen rule. After 2N steps the entire bank state
equals its initial state. A third lap therefore reissues the same addresses
and payloads. Permanent prefix retention and forever-fresh IDs do not hold
for this fixed bank. Period tagging would add a counter not present in (6).

Any prescribed finite number of first-lap input positions can be supplied
by choosing a sufficiently large fresh bank. This is 'for every prefix,
there exists a capacity', not 'one finite capacity works for every prefix'.
Never-reused addresses, an unbounded head/bank, or replacement blank inputs
would be additional resources. The initial source array is itself a declared
input supply. The protocol is not asserted to be native U or a realized
apparatus.

## 6. Why amplitudes and energy alone do not supply occupancy

Erase cell tags by mapping both BLANK and occupied(0) to the zero vector,
and occupied(v) to v. Consider two first-lap states differing only in whether
the active source cell is BLANK or occupied(0), with its record BLANK. Their
amplitude-only pre/post transitions, heads and total energies are identical.
The typed emitter returns no record in the first case and (j,0) in the
second. Hence this emitter does not descend through amplitude erasure.
The extra distinction is exactly the presence/occupancy information; it is
not recovered by attaching an operation name after erasing that information.

For the amplitude swap (s,r)->(r,s), the record-energy change is

    Delta E_R=s^T G s-r^T G r.                             (7)

On a cold record r=0 it is strictly positive exactly when s!=0, by positive
definiteness. It therefore detects nonzero cold loading, but cannot separate
idle zero from a zero-valued arrival. On a warm record it need not even
detect a change of signed value: with m=1, G=(1), s=1 and r=-1, the record
changes from -1 to 1 while Delta E_R=0. Equation (7) is not a universal
event counter. A profile that deliberately accepts only positive deposits
chooses another granularity; the zero-arrival requirement does not apply
to it unless it explicitly adopts that requirement.

The occupancy carrier avoids this mathematical ambiguity by admitting the
missing input distinction. It does not explain its physical realization or
assign energy, preparation cost or a universal event law to that tag.
Earlier symbolic blank-cell and reservoir models likewise declare their
fresh inputs and storage. No operation flag is needed inside the fixed bank
FLOW, but its occupancy, head, prepared sources and fresh capacity are not
free consequences of equal amplitudes or of the native counter.

## 7. Disposition

One protected finite record subspace cannot both remain passively invariant
and receive new orthogonal source amplitude under the same fixed coupling.
Perfect loading instead requires an isometric fresh-space embedding, and
the finite bank realizes a controlled prefix of retained records without
a FLOW opcode. Zero-valued arrivals need a distinction lost by amplitude
and scalar-energy erasure if they are to count differently from idle slots.
The exact finite-capacity failures are retained, not hidden by a reset.

All claims concern the displayed L1 carrier and transition classes. Existing
native observation, fresh-record and reservoir results remain dependencies,
not physical certificates. Which interactions are Snaps, which queries are
passive, how occupancy is realized and how records persist remain
STOP-DEFINITION under the existing apparatus owner. No Born marginal,
physical dimension or canonical status is changed. Finite audits check these
proofs and supply no extrapolation beyond their stated domains.
