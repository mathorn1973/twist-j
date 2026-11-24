# Exact phase-to-account conversion and parity-protected retention

NON-CANONICAL / L1 / analytical candidate, pending external review.
Reservation: https://github.com/mathorn1973/twist-j/issues/1891.
All claims below concern the specified contact model. They are not empirical
claims or newly assigned registry statuses.

## 1. Inputs, authority and exposure

Use RELATIVE-CONTACT-INTEGRAL-LAW [T] from Public Canon v109.
The contact, marked slots, graph, identity refusal and quadratic account
are declared premises. Put

    O = Z[j], Phi_5(j) = 0, p = j^2, a = 1-j,
    Q(z) = Tr_(Q(j)/Q)(z conjugate(z))/2.

For a coefficient vector z=(z0,z1,z2,z3),

    Q(z) = [5 sum zi^2 - (sum zi)^2]/2.

On x-y in 2O the contact is

    C(x,y) = (s+p d, s-p d),
    s=(x+y)/2, d=(x-y)/2.

On the complete refused complement it is identity. It is a bijection,
C^5=I, preserving pair sum, Hermitian account, Q and both residues modulo a.

A supplied non-canonical finite ring report and its implementation were
read before this work. Its result and the local analytical derivation are
exposed inputs. PROVENANCE.md records this without making that attachment a
runtime dependency. The ring rule and every tested input are defined here
and in PREREG.md. No blind discovery or independent review is claimed.

## 2. Exact integral realization of the phase ring

Let L be even and sites run modulo L. Set

    x_i = (-1)^i a p^(k_i),  k_i in Z/5.

At layer t apply C on disjoint edges with left endpoint i=t modulo 2.
The signs alternate also across the closing edge, because L is even.

Phi_5 is irreducible over F2: a degree-four reducible polynomial with no
linear factors would have to be divisible by the only irreducible quadratic
X^2+X+1, but at a root w of that quadratic Phi_5(w)=w+1 is nonzero.
Consequently O/2O is F16. The classes of a and p are nonzero, and p has
order five. Thus neighboring residues agree precisely when k_i=k_(i+1).
In that case the input is (u,-u), up to ordering, and C sends it to
(pu,-pu). Otherwise it is fixed. This is exactly the attached phase rule.

Every site has Q(x_i)=Q(a)=5 at every undisturbed snapshot, in every
preparation in this phase family. Both complex embeddings separately keep
their site norm. Every marked residue modulo a is zero. The two supplied source bits also
have the same total sum and account: the changed adjacent source pair sums
to zero before and after its common phase shift.

For a single admitted edge its account transfer, defined from the actual
endpoint change Q(x_i')-Q(x_i), is therefore zero. Refused edges also
transfer zero. This excludes account transport by this phase family,
not every energy reading and not general contact states. The construction
below explicitly leaves this family when it reads a matched phase.

## 3. Causality and the scope of the ring delay

A layer uses only disjoint nearest-neighbor contacts. Two preparations
identical outside the source sites {-1,0} cannot differ outside the graph
distance-t neighborhood of that source after t layers. A common flaw does
not evade this argument. The earliest possible contrast at D=8 is t=8
for the specified L>=20 rings.

For the clean ring the zero-bit solution is k_i(t)=t modulo five.
For the one-bit source, the right front at snapshot t>=1 has
k_t(t)=t-1 while the next site has k_(t+1)(t)=t.
The edge (t,t+1) is active and unequal, so it holds; the next leading site
is again one phase behind at the next snapshot. The initial layer gives
this induction base at site 1. Before wrap from the other front, first
arrival is t=D. For the clean D=8 family it gives the two inherited
read labels (0,15).

For possible future all-L work, define wall differences
delta_i=k_(i+1)-k_i and
b_i(t)=1 if i=t modulo two and delta_i=0, otherwise zero.
Exactly, in F5,

    k_i' = k_i+b_(i-1)+b_i,
    delta_i' = delta_i+b_(i+1)-b_(i-1).

The attached t_phase=4L-57 is a finite result and a five-size forecast.
No all-L proof is supplied here. Varying L while D stays fixed measures
latency versus circumference. It does not establish four laps or speed 1/4.

## 4. A reference supplied by the same contact

Add two isolated marked slots A,B prepared at

    (A,B)=(3a,-3a).

Contact this pair once per ring layer. At snapshot T it is

    (A_T,B_T)=(3u,-3u), u=a p^T.

The pair costs Q(A)+Q(B)=90 initially. The entire prepared carrier is
O^(L+2), with account 5L+90. A two-state parity label can describe which
ring matching comes next. The update on field plus this label is a
bijection: apply the specified ring matching and the disjoint reference
contact, then flip the label. The inverse first recovers the old label,
then applies inverse contacts.

This is a declared finite scheduling rule, not a derivation of its controller
from original U. The reference replaces access to the numerical T modulo
five at the comparison port. It does not supply the sampling trigger.

## 5. One contact converts the phase into an account pointer

At a preselected snapshot T, couple the even receiver D once to A.
Use D=8 for the supplied defect experiment and the declared even D family
for the clean propagation audit.
Write x_D=a p^k, A=3u. Their residues modulo two coincide iff k=T modulo
five. On mismatch the entire pair is unchanged.

On match the exact transition is

    (u,3u) -> ((2-p)u,(2+p)u).

The input accounts are (5,45), and the output accounts are (25,25).
The unused reference arm remains -3u with account 45.
Thus the three local accounts are

    match:    (5,45,45) -> (25,25,45),
    mismatch: (5,45,45) -> (5,45,45).

Total 95 is preserved. The complete ring-plus-reference account remains
5L+90. The signal site receives 20, and the reference supplies 20.

Here is an embedding-independent proof of the transfer. Set
s=j+j^(-1), so s^2+s=1 and p+p^(-1)=-1-s. Then

    |a|^2 |1-p|^2 = (2-s)(3+s) = 5.

Therefore

    |(2-p)u|^2-|u|^2 = 2 |a|^2 |1-p|^2 = 10.

The other leg loses 10 by conservation. The equality holds as an element
of the real subfield, hence in both complex embeddings. Taking Q sums
the two contributions, giving 20. Also Q((2-p)u)=Q((2+p)u)=25.
No chosen complex embedding is needed to distinguish the pointer states.

Within the restricted family A=c u for odd integers c, matched gain is

    Delta Q_signal = 5(c^2-1)/2.

This follows by putting s_pair=(1+c)u/2 and d_pair=(1-c)u/2 in C,
or by the norm identity above. The choices c=+1 and c=-1 give zero
account transfer; |c|=3 is the smallest odd integer magnitude giving
nonzero transfer. This is not a minimum over arbitrary O-valued apparatuses.

## 6. The match latches the reference through its own parity gate

After the one signal contact, do not couple the reference to the ring again.
Continue applying the same reference-pair contact C(A,B).

On match the reference pair is ((2+p)u,-3u). Its difference is (5+p)u,
whose reduction modulo two is (1+p)u=J u, nonzero in F16.
Its contact is therefore refused. Both arms remain fixed under every
future reference-pair update.

On mismatch the pair remains (3u,-3u), is admitted, and keeps rotating.
Its positive-arm account stays 45. Hence the present-state pointer

    P=Q(A) in {25,45}

persists for any number of subsequent reference updates. Match is 25;
mismatch is 45. No separate freezing operation is needed after the bridge
has been removed. The single bridge use and its removal remain part of the
supplied interaction schedule. Additional external contacts are not covered.

There is no collision of complete states. The read contact M is a bijection
with M^-1=M^4; subsequent ring/reference contacts are also bijections.
The two read branches have disjoint P values. Reset requires the inverse
coupling with the actual disturbed signal, or an explicitly supplied reset
resource. Reversibility is not free renewal, dissipation or irreversible heat.

## 7. Relation to the supplied detector and timing

The attached detector assigns R_old=0 on match and 15 on mismatch.
For separately prepared snapshots, our physical-model pointer obeys

    P = 25+(4/3) R_old.

This is an exact relabeling of two values, not a fit or a new frequency law.
Two source preparations have different P exactly when their inherited
detector labels differ. Unequal phases can still both mismatch the reference;
the original detector delay and possible polarity inversion remain.

T labels the sampled snapshot. The pointer is available after one additional
contact M. During this read layer, pause both the ring matching and the
reference-pair contact; retain the current ring parity label. If one primitive
contact layer is counted as one step, read completion is T+1. This does not silently remove the one-step measurement
latency.

A matched read changes the ring site's account from 5 to 25, so it leaves the
five-phase family. Later ring evolution must use the full contact model;
the original unmeasured ring forecast cannot be reused. Each sampled T
requires a fresh prepared experiment or an explicit controlled reversal.

## 8. What has advanced toward physics

The construction supplies a source-sensitive, locally changed, retained
present-state account pointer. It uses the same contact that transports the
phase signal, and its reference phase is carried by an actual pair of slots.
A match stops that pair without an extra latch instruction.

The following are still declared or open:

- The contact and geometry must be physically realized and identified.
- Preparing the ring, source, flaw, coherent reference phase and account 90
  is a resource, not derived from the axiom alone.
- The one-shot bridge and chosen snapshot are supplied. Fully autonomous
  source triggering and repeated input selection are not proved.
- Q is an explicit mathematical reading. A physical transducer that measures
  it, its energy calibration and the physical tick/edge units remain open.
- The signal controls reference energy release; it has not transported that
  energy around the ring. No passive photon absorption is claimed.
- The persistent pointer is a phase-match record, not generally a source-bit
  record, a Born outcome, a probability law or regenerated archive.
- Same-session review is not independent scientific acceptance.

A physical identification must predict the branch, back-action, reference
depletion and retention together. Relabeling a phase sequence as an electron
or substituting QED coefficients would not establish that interface.

## 9. Adversarial controls: sign, scaling and zero-transfer memory

The principal retained account pointer uses an even receiver with positive
source sign and the positive c=3 reference arm. This sign restriction matters.

For a matched incoming sigma*u, sigma in {+1,-1}, and clock(c*u,-c*u)
with odd integer c, the post-read clock difference reduces modulo two to

    [(c-sigma)/2] (1+p) u.

It is nonzero exactly when c=-sigma modulo 4. Thus this is the general
latch condition. For sigma=-1,c=3 the reference remains admitted.
One further internal contact changes its accounts from (25,45) to (60,10).
This is an expected adversarial control, not a failure of the positive-source
theorem. An odd receiver requires a correspondingly prepared reference sign;
it cannot be substituted silently.

There is also a smaller phase/admission latch with no account transfer.
Prepare the clock (-a,+a), account 10, and match the incoming u to its negative
arm -u. The read contact gives

    (u,-u) -> (p*u,-p*u).

The unused arm is +u. The clock difference is -(1+p)u, nonzero modulo two,
so that pair stops. On mismatch it continues rotating. All three local
accounts remain 5. The persistent admission class, rather than Q of one arm,
distinguishes these outcomes.

This control does not make preparation free: the clock still starts with
account 10 and a chosen phase. It does show that phase/admission recording
does not require nonzero account transfer during this interaction.
The c=3 construction was selected to give a calorimetric account contrast;
it is neither a global minimum-memory theorem nor a universal cost of a bit.

Multiplying every prepared scalar by the same odd integer b preserves
all gate choices, phases and the read/latch calendar, while Q scales by b^2.
The principal gap becomes 20*b^2. Multiplying all prepared scalars by p^g
also preserves admission and Q, proving independence of common phase origin.
Relative reference phase is still a preparation resource.

Finally, with the inherited clean reference r=T, bit zero is the matched
branch that stops the clock; bit one at its clean front keeps it running.
The detector records phase matching. "Signal arrival stops the clock" is
not a universal description of these bit labels.

## 10. Frozen finite whole-apparatus integration

The source ring is prepared at k_i=0 except for k_2=h. Bit one additionally
sets k_(L-1)=k_0=1; bit zero leaves these two phases zero. Each preparation
includes the same reference (3a,-3a), initially shared relative phase, and
ring parity zero. A normal layer performs the current disjoint ring matching
and the disjoint reference contact, then flips parity.

The declared clean family has L=64, h=0 and D=4,8,12,16,20,24.
The first pointer contrast is predicted at sampled snapshot T=D,
completion D+1, with pointer accounts (25,45) in source-bit order.
The reference pair has actually undergone every preceding contact.

The exposed defect regression family has L=20,22,24,26,28,
h=1,2,3,4 and D=8. For L modulo 10 equal to0,2,4,6,8 respectively,
the inherited first-read expectation is T=4L-57 plus 2,0,1,3,0.
Pointer order is (45,25) for remainder2 and (25,45) otherwise.
This checks a transported finite expectation, not a new all-L proof.

At each potential snapshot the audit uses an independent complete state
copy to apply the actual read contact and compute Q of its resulting arm.
It never inserts a precomputed phase-match answer into the receiver.
The earliest unequal pointer pair is selected for the integration audit.
The time horizon remains16L+80, and absence is a failure of the declared
finite expectation. No undisclosed measurement is made on the continued
unmeasured ring.

For each bit at that first contrast, actually keep the disturbed full
O-valued state, including both reference arms and parity. continue 20 normal
layers without another bridge. Check total sum, Hermitian account, Q and
the fixed pointer at every snapshot. Then reverse those 20 layers, recovering
the old parity before inverse contacts, and apply M^4. The entire sampled
ring, both reference arms and parity must be recovered exactly.

This is 52 complete invasive-read continuations and reversals, one per bit
in each of 26 paired experiments. It is a bounded implementation audit of
the construction and its supplied calendar, not autonomous experimental
selection, physical occurrence or a test against measured data.
