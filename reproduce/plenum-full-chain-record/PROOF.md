<!-- SPDX-License-Identifier: Apache-2.0 -->
# Transfer to a permanent fine-value record in a prepared contact field

NON-CANONICAL public intake proof. The finite certificate and its analytical
consequence are separate claims. No input preparation is registered as a
standalone D claim.

The new contribution is remote transfer into a stationary cell of the same
colour. A persistent local distinction in the pointer position was already
available after writer escape in the earlier scattering construction, at its
stated scope. The present complete retained-writer chain adds a remote
fine-value record and an all-future guarantee for the specified phase family.

## Explicit field and clock

Let O=Z[j], Phi_5(j)=0, rho=j^2, J=1+j^2 and phi=-j^2-j^3.
Conjugation sends j to j^4; h(z)=z conjugate(z) and
Q(z)=(5 sum z_i^2-(sum z_i)^2)/2 in the basis 1,j,j^2,j^3.
Use only the registered two-slot C_rho: on x-y in 2O, put d=(x-y)/2
and send (x,y) to (x+(rho-1)d,y-(rho-1)d); otherwise fix it.
This is not the reciprocal four-slot B. Let lambda=1-j,
delta=j^4 and beta_i=0 for even i, beta_i=delta for odd i, on the entire
integer line. At letter a in {0,1}, simultaneously apply C_rho to all
adjacent pairs (i,i+1) with i congruent to a modulo 2.

The clock is p(n)=1 when v_2(n) is even and 0 otherwise, n>=1.
A field initialized at boundary n0 is subsequently updated with
p(n0+1),p(n0+2),... . This supplied clock-driven contact field is not
identified with the full native U.

A listed value replaces beta, rather than being added to it. All unlisted
sites equal beta. Since delta is nonzero modulo 2, every background pair
refuses; each finite-time deviation has finite support. For such a field
define only the finite excess accounts

    S=sum_i(z_i-beta_i),
    H=sum_i(h(z_i)-h(beta_i)).

Their conservation follows from the two-slot sum and full-H identities
and finite propagation. The unrenormalized background H is infinite;
half-trace(H) is not the total energy of a finite apparatus.

## Proposed PLENUM-ALIGNED-ESCAPE-CRITERION [T]

Let r,N be nonnegative integers with N divisible by 2^r. Consider this
explicit contact field at boundary N.
Suppose it is a union of a stationary finite component F and at most one
outgoing finite component on each side, all interpreted relative to beta.

Assume:
1. F is fixed under both individual matchings; its support is in [A,B].
2. For each outgoing component, normalized states are represented relative
   to the even floor of their leftmost support site. The initial state is
   in a finite set of nonempty normalized states, with an exact transition
   row for every state under each word tau^r(0) and tau^r(1). Every output
   is in that same set, where tau(0)=11 and tau(1)=10.
3. Every transition records its complete normalized output, an even anchor
   displacement and the min/max defect coordinates over every intermediate
   tick, including start and end.
4. Every left displacement is strictly negative and every right displacement
   strictly positive. At the initial left anchor l, every left row has
   l+max<=A-2; at the initial right anchor u, every right row has u+min>=B+2.

Then the complete future contact field remains the disjoint union of F
and the separately evolving outgoing components for any sequence of these
two blocks. In particular the stationary component is retained forever
under the native-clock suffix after N.

### Proof

From the valuation definition,

    p(2n-1)=1, p(2n)=1-p(n).

Thus consecutive letters at indices 2n-1,2n are tau(p(n)).
Iteration proves that every aligned length-2^r block is tau^r(b) for
some b in {0,1}; the claim includes the actual suffix at N.

Even translation preserves beta and both marked matchings. Hence each
normalized transition table gives the corresponding raw transition at
every even anchor. After a left transition its new anchor is smaller,
so every future upper support bound is at least as safe as the initial
one. The analogous lower bound improves on the right. F is unchanged
at each individual tick. At every tick a contact pair can meet at most
one of the component supports; the stated gaps prevent a contact joining
different components. All other background contacts refuse.

For each matched pair its joint input therefore equals the input in the
isolated evolution of the sole component it meets, or the fixed background
input if it meets none. Locality identifies the joint evolution with the
union of separate evolutions throughout the block; no linear superposition
is assumed. Transition closure gives
the same hypotheses at the next aligned boundary. Induction proves the
claim for arbitrarily many blocks and all intermediate tick boundaries.

This theorem is an implication from exact certificate hypotheses.
It neither generates a certificate nor proves that a proposed numerical
table is correct.

## Frozen input family

Define X_sigma(k)=-sigma J(1+rho^k) and
Y_sigma(k)=-sigma J(1-rho^k), with sigma=1 for positive and sigma=j for
negative packets. Set

    q=j^3,
    m_minus=(-8,-2,-4,-6),
    m_plus =(-6,-4,-2,-8),

in the basis 1,j,j^2,j^3. Both primary inputs have q at -23,
X_j(0) at 49 and m_minus at 562. WRITE has X_1(0) at 1;
FAR has the same X_1(0) at -131073. ABSENT omits that positive packet
and is a secondary control, not an equal-account primary input.

Direct cyclotomic arithmetic gives

    m_plus-m_minus=2Jlambda,
    h(m_minus)=h(m_plus)=72-44phi,
    Q(m_minus)=Q(m_plus)=100.

WRITE and FAR both have S=-7-j-3j^2-4j^3 and H=86-52phi,
with half-trace 120. This equality is only of the displayed S, H and
half-trace accounts. It does not include the reduced colour word: WRITE
places the positive writer to the right of q, FAR to its left, so the
ordered colour invariant differs already in the inputs. ABSENT instead has
S=-6-2j-2j^2-5j^3 and H=79-48phi.

The primary encoded distinction is writer position, not an arbitrary
unknown sign. The receiver is prepared at 562 and is certified to remain
stationary at 560 from the proved cut onward; the cut is not asserted to
be its first settling time.

The receiver value pair and initial site were selected by exposed
reconnaissance. A 51-site scan from prepared q/reader slices at boundary
65536 found 15 sites with different terminal values and both packets
classified as departing right by boundary 196608. Only its first two hits,
562 and 566, were replayed from the full initial field in that scan script.
This selection history is
not a preregistered success probability or an all-site result. The later
frozen finite certificate and phase-extension proof concern the selected
input only. See PROVENANCE.md for the evidence boundaries.

## Proposed PLENUM-FULL-CHAIN-FINITE-CERTIFICATE [C]

For the three stated inputs initialized at n0=1, 196607 applications of
the exact raw rule give the following complete endpoint at boundary 196608.
No other deviations from beta are present.

| Input | Left writer | q | Receiver | Right reader |
|---|---|---:|---|---|
| WRITE | Y_1(4) at -1706; X_1(4) at -1705 | -21 | m_plus at 560 | Y_1(1) at 1282; X_1(1) at 1283 |
| FAR | Y_1(4) at -132822; X_1(4) at -132821 | -23 | m_minus at 560 | X_j(1) at 1873; Y_j(1) at 1874 |
| ABSENT | none | -23 | m_minus at 560 | X_j(1) at 1873; Y_j(1) at 1874 |

The stationary q/receiver component is fixed under each matching.
The exact outgoing closure tables under tau^13(0),tau^13(1) have:

| Component | States | Rows | Initial even anchor | Shift set | Global nearest bound |
|---|---:|---:|---:|---|---|
| WRITE left | 3 | 6 | -1706 | -122,-120,-58,-56 | max<=-1684 |
| WRITE right | 5 | 10 | 1282 | 40,50,52 | min>=1273 |
| FAR left | 3 | 6 | -132822 | -122,-120,-58,-56 | max<=-132800 |
| FAR right | 3 | 6 | 1872 | 56,58,120 | min>=1853 |
| ABSENT right | 3 | 6 | 1872 | 56,58,120 | min>=1853 |

All row extrema include every intermediate tick, not just endpoints.
certificate.json contains the complete normalized start/end fields,
shifts and extrema for all 34 rows, and the exact reference-phase raw
endpoints and accounts. It is an extracted evidence fixture, not a verifier.
Its public computational acceptance remains pending.

### Finite scope and falsifier

This C proposal asserts only the stated finite evaluations: the three
histories, stationary checks, and 34 complete transition rows at length
8192, with state limit 16 and span limit 1024. It does not infer permanence
from a finite horizon. Any wrong endpoint, omitted defect, account discrepancy,
wrong row, failed closure or incorrect intermediate extremum falsifies the
corresponding finite assertion. An integrity mismatch stops acceptance;
it is not by itself a scientific negation.

## Proposed PLENUM-PREPARED-PERMANENT-RECORD [C, with analytical extension]

Assume the exact finite certificate just stated is accepted for the given
raw rule and inputs. For every integer h>=0 initialize at
n0=2^18 h+1. Then for every n>=2^18 h+196608,

    z_WRITE(560,n)=m_plus,
    z_FAR(560,n)=m_minus.

The complete original writers are retained in both preparations.

The proposed C status retains the computational dependency. The all-phase-
family and all-future quantifiers below are proved analytically from the
finite certificate; they are not inferred from a long run. No theorem-status
promotion of that computed premise is proposed.

### Proof

For 2<=k<=196608<2^18, writing k=2^v w with w odd gives
2^18 h+k=2^v(2^{18-v}h+w) and hence
v_2(2^18 h+k)=v_2(k). Every letter in the initial 196607-tick
history agrees with h=0. Determinism transfers its complete finite
history and endpoint to every h, not just its final reading.

The cut is divisible by 8192. In WRITE take A=-21,B=560; in FAR
A=-23,B=560. The table's left/right bounds are strictly beyond the
required one-background-site gaps. All displacements are even and
strictly outward, and the stationary component is fixed under both
letters. PLENUM-ALIGNED-ESCAPE-CRITERION therefore applies to the
complete field, including the retained left writers, at every start in
the declared phase progression.
It gives the displayed fixed-cell values for all future boundaries.

The infinite phase progression is proved by the valuation identity.
The four h values directly replayed in the historical source are
implementation checks only; this public verifier replays the three h=0 histories.
The result does not classify every phase or assign a physical success
probability.

## Reading and physical boundary

The passive map R(m_minus)=0, R(m_plus)=1 distinguishes these two terminal
values. It is not a later active reading interaction. Both values have
the same full Hermitian account, Q, colour modulo 2 and residue modulo
lambda. A reader that depends only on those invariants of the receiver
cell cannot distinguish them. The complete fields are distinguishable:
q is at -21 or -23, and the outgoing reader has positive sign in WRITE
and negative sign in FAR. The outgoing packet excess sums are respectively
-Jlambda and +Jlambda. Thus the receiver increase by 2Jlambda is balanced
by the packet decrease by 2Jlambda; the sign already carries a distinction.

Separate finite reconnaissance at 64 start phases and 8000 ticks reports
reverse switching m_plus to m_minus by a positive incident packet with a
negative outgoing packet. For the same selected receiver pair the supplied
quick review reports no receiver change for positive packets incident on
m_minus or negative packets incident on m_plus in that tested class.
The archived program's tally is narrower: it counts completed clean
sign-changing switches and does not certify absence of every transient
change. These observations suggest a
later exchange readout with the outgoing sign as output, but do not prove
an all-phase law or a copy operation. They have not been composed as a
later read in the complete retained-writer chain.

The identity
C_rho^4(X_j(0),m_minus)=(X_1(0),m_plus)
is four repetitions of one edge, equivalently one inverse contact.
It is not the actual clock-driven path. Receiver-window changes are not
counts of receiver contacts: the reported 1544 changes include movement
and other changes inside the window. A separate direct check rejected a
single-contact explanation. Decomposing the actual multi-contact switch
remains open and is needed before comparing its mechanism with B.

No claim here proves formation from plenum, least writing cost, an active
native reader, reset/reuse, unlimited independent inputs, full-U realization,
Born occurrence, physical energy or unit calibration. Q=100 is the account
of this particular supplied receiver, not a proved minimum.

## Negative results retained

Reversible whole-field settling obstructions do not exclude a stationary
local field with escaping components. Finite scar erasure and failed
signed-lambda preparations concern other declared inputs and remain
negative at those scopes. A full winding on a finite ring is not proof
of arrest on the integer line.
