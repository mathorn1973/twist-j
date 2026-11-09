# One funded law from a local sign to a remote finite record

NON-CANONICAL / L1. Supplied architecture and reader: candidate-D. The
conditional analytical construction below: candidate-T, author-side proposal
pending independent review and prospective verification. No scientific program
was executed to obtain this note. It changes no Canon status.

The inherited primitive and four-cell writer are restated from
[P-J-FUNDED-PAIR-NETWORK-1](https://github.com/mathorn1973/twist-j/issues/1969).
The primitive's separate ownership remains
[issue 1968](https://github.com/mathorn1973/twist-j/issues/1968).
The source manifest accompanying this note identifies the inspected inputs.

## 1. Precisely what is constructed

For every integer distance parameter d >= 1 and hold parameter h >= 1, one
finite raw-cell array, one fixed five-layer update F, and one fixed reader
confined to a declared remote region have the following property.

The two preparations differ ONLY at a source raw cell, whose value is 2a
for an unknown a in {-1,+1}. Every payer, rail and receiver cell is prepared
identically for both signs. The reader is initially BLANK. Its first nonblank
full-boundary reading is at tau = d+2, and it returns a at every full boundary

    tau, tau+1, ..., tau+h-1.

It returns BLANK at every earlier full boundary and at tau+h. During the
hold it also returns a at the intervening boundaries of all five layers.
The same F continues throughout: there is no output feedback, reader-controlled
switch, external driver word, advancing program tape, reset or gate removal.

The receiver is an initially occupied, counted, contiguous delay-memory
REGION. A two-pulse word moves inside it while its decoded value stays fixed.
This is not a stationary one-cell latch, a permanent archive, or a proof of
physical detector implementation. Sections 2-7 first establish the data
apparatus and its finite first window.
Sections 8-10 then expose a later false passage of that ungated reader and
complete the apparatus with a counted B-only clock rail. The final reader
is correct or BLANK at every time: it reads a for h ticks in each period
P=2L+4 and is BLANK otherwise, including later occupied-state continuation.
This is recurrence of the same input, not independent renewal.

## 2. Exact primitive and accounts

Let O=Z[j], with 1+j+j^2+j^3+j^4=0. Put

    rho = j^2, J = 1+rho, Jinv = -j-j^2,
    phi = -j^2-j^3, g = J conjugate(J) = 2-phi,
    W = J rho.

Here J Jinv=1, g^(-1)=1+phi, g is positive at both real embeddings, and g!=1.
Write h(z)=z conjugate(z). For a raw array z set

    S(z) = sum_i z_i,
    H(z) = sum_i h(z_i),
    E(z) = Tr_(Q(j)/Q)(H(z))/2.

In particular E(z)=2A+B if H(z)=A+B phi. For a single cell represented by
integer coefficients c0,...,c3,

    q(c) = [5 sum_i c_i^2 - (sum_i c_i)^2]/2,
    E(z) = sum_i q(z_i).

The quadratic form is integral, positive definite, and obeys
q(c)>=sum_i c_i^2/2. Thus fixed finite arrays have finite bounded-E sets.

The four-cell gate B takes ordered cells (x,y,p,r). It is identity unless
both x-y and p-r belong to 2O. On that admitted domain define

    c=(x+y)/2, d=(p+r)/2, u=(x-y)/2, v=(p-r)/2.

Keep c,d fixed. Apply precisely one of:

1. If u!=0 and h(v)=g h(u), use (u,v)->(Ju,Jinv v).
2. If v!=0 and h(u)=g h(v), use (u,v)->(Jinv u,Jv).
3. Otherwise use identity.

Reassemble (c+u,c-u,d+v,d-v). The two nonzero branches are disjoint: their
intersection would imply (g^2-1)h(u)=0 and therefore u=0. Each branch maps
into the opposite branch. Both parity-admitted pair differences remain even.
The complement is fixed, so B^2=I on the entire O^4 carrier.

The gate preserves each of its two marked pair sums, and hence S. On an
accepted branch it exchanges h(u),h(v). Since the four-cell account equals
2h(c)+2h(d)+2h(u)+2h(v), it preserves full H and E. No separate positive
or negative-energy reservoir is omitted.

## 3. Geometry, law and common preparation

Use four source cells x=(x0,x1,x2,x3), and m fixed rail sites
P_i=(p_i^+,p_i^-), i modulo m, where

    L=2d+h+3, m=2L.

All named gates below are the SAME B from section 2.

- B0 acts on source cells in order (0,1,2,3).
- B1 acts on source cells in order (1,2,3,0).
- I acts on (x2,x3,p_0^+,p_0^-).
- K0 applies B simultaneously to rail-site pairs (0,1),(2,3),... .
- K1 applies B simultaneously to rail-site pairs (1,2),(3,4),...,(m-1,0).

One full tick, with the rightmost factor acting first, is

    F = K1 K0 I B1 B0.

Thus every tick first operates the four-cell writer, then its interface to
the launch site, then the two conveyor layers. The graph, constituent pairs
within each layer, layer order and source location are supplied parts of
one fixed law. The source is a local inhomogeneity; no spatially homogeneous
or native-U derivation is asserted. All layers have finite support radius
on this supplied graph, independent of d and h.

The two initial arrays are

    x=A_a=(2a,0,W,-W), a in {-1,+1};
    P_0=(J,-J);
    P_i=(1,-1) for every i!=0.

The rail preparation is COMMON, including the initially high launch pair.
There is no selection of a rail preparation after learning a. Receiver pairs
are occupied low pairs, not literal zero cells.

For the rail code define low=(1,-1), high=(J,-J). A B contact swaps the two
occupations: low/high becomes high/low, high/low becomes low/high, and equal
occupations stay fixed. On this canonical code the local phases do not change.
K1 K0 moves any occupation at an even site two sites forward per full tick;
one at an odd site moves two sites backward. The construction launches only
on the even forward lane.

## 4. Three-tick sign encoder

Define the following source states:

    A_a=(2a,0,W,-W),
    C_+=(1+J,1-J,rho,-rho),
    C_-=(-1-J,J-1,rho,-rho),
    B_+=(2,-W,W,0),
    Z_-=(-1-J,J-1,W,-W),
    D_a=(2a,0,rho,-rho).

The inherited four-cell writer T4=B1 B0 satisfies

    A_+ -> B_+ -> C_+ -> A_+,
    A_- -> C_- -> A_-.

For completeness, B0 exchanges A_a and C_a by its balance condition. B1
rejects A_a by parity. On C_+ its two half-differences are -rho and -J,
so it takes the forward branch and gives B_+; on B_+ it takes the inverse
branch and gives C_+, while B0 rejects B_+ by parity. On C_- the B1
half-differences are 0 and 1, so it rejects by balance.

The additional states needed for the connection also have exact simple
behavior. T4 fixes Z_-: B0 sees two relative accounts g and g, and B1
rejects because its first difference is rho-W=-rho^2, which is not in 2O.
T4 fixes either D_a: B0 sees two relative accounts 1 and 1, and B1 rejects
the difference -rho by parity. Both rho and rho^2 are units modulo 2.

Before tick 1 the launch site is high. Before ticks 2 and 3 it is low,
because the conveyor has removed the preceding launch value and no pulse
has yet circled the rail. The table records the source immediately after
T4, the subsequent I action, and the launch value entering the conveyor.

| Tick | Input sign | After T4 | Interface I | Source after I | Launch |
|---|---|---|---|---|---|
| 1 | + | B_+ | parity refusal | B_+ | high |
| 1 | - | C_- | forward | Z_- | low |
| 2 | + | C_+ | equal low accounts | C_+ | low |
| 2 | - | Z_- | inverse | C_- | high |
| 3 | + | A_+ | inverse | D_+ | high |
| 3 | - | A_- | inverse | D_- | high |

The nontrivial interface identities are simply

    (rho,J) -> (W,1),
    (W,1) -> (rho,J)

for the relative values of payer and launch pair. At the positive first
tick the payer pair is (W,0), whose difference is odd, so I refuses.
At the negative first tick the payer is (rho,-rho), which accepts the
common high launch pair. This is the exact local-sign-to-account interface:
the source-dependent parity created by re-pairing decides when the common
launch stock leaves.

Consequently the positive input emits highs at ticks {1,3}; the negative
input emits highs at ticks {2,3}. The second pulse is common and supplies
a marker. The original source sign remains in D_a; it is not erased or
silently substituted by a different input convention.

After tick 3, D_a is fixed by T4 and by I whenever the incoming launch
pair is low. All other rail pairs stay in the canonical binary code.
The first possible full-boundary return to launch is tick L for the
positive leading pulse. Thus the launch is low at the START of every tick
2 through L, apart from any locally generated high during I. This proves
the claimed encoder continuation through the first read window without
assuming that the source or interface is disconnected afterward.

## 5. Closed-form transport before return

At full tick 1 the positive rail has its sole high at site 2; the negative
rail has no high. At full tick 2 the positive rail has its sole high at
site 4; the negative rail has its sole high at site 2.

For 3<=n<L, all indices in the following formula lie in the unwrapped
range and the exact high sets are

    positive: {2n-4, 2n},
    negative: {2n-4, 2n-2}.

Every other rail site is low. The trailing high is the common tick-3
marker. The bit is the distance from that marker to the leading high:
four sites for +, two for -. This is a phase-to-temporal-word conversion,
followed by exact account transport. It is not phase transport by the
fixed-pair conveyor itself.

During the subsequent K0 layer each of these even high positions increases
by one, leaving its separation unchanged. K1 then increases both by a
further one. The source-only layers B0,B1 and interface I do not touch the
remote receiver. This observation will give a reader that remains correct
also at the intermediate layer boundaries.

## 6. Fixed remote reader and the common hold interval

Let r=2d. The receiver consists of ALL rail sites in the contiguous region

    R={r,r+1,...,r+2h+3}.

Its largest index is 2d+2h+3, strictly below m. It neither wraps nor
contains the launch site. Along the data ring its closest site is at least
2d bonds from launch in either direction: the reverse distance to its far
end is 2L-(2d+2h+3)=2d+3. Thus d controls actual graph remoteness, not
merely a longer trip to a receiver close by the reverse ring arc.
The region contains 2h+4 rail pairs, all initially low and already counted
in the full apparatus.

Define a total reader on arbitrary raw states. First require every site in
R to be exactly low or high as defined in section 3. If this fails, return
BLANK. Require exactly two highs in R; otherwise return BLANK. If those
highs have ordered positions s<t, return

    VALUE(+1) if r<=s<=r+2h-1 and t-s=4;
    VALUE(-1) if r<=s<=r+2h-1 and t-s=2;
    BLANK otherwise.

The tagged BLANK is not the numeric value zero. The reader accesses only
this fixed remote region and never reads a tick counter, source, payer,
launch site, or any external clock. Its spatial anchor mask is part of
the declared reader, not a feedback condition in F.

Put tau=d+2. Before tau the common trailing marker has not entered R:
its position 2n-4 is less than r. At most one leading pulse can be in R,
so the reader is BLANK. This also covers ticks 0,1,2 directly from the
preparations and the one-pulse cases above.

At n=tau+j with 0<=j<=h-1, the trailing marker is at s=r+2j. The positive
leading high is at s+4 and the negative one at s+2. Both lie in R, all
remaining sites in R are low, and the allowed anchor condition holds.
Thus both inputs are read correctly for exactly the h declared consecutive
full boundaries.

At the intervening K0 boundary the anchor is r+2j+1. It remains within
[r,r+2h-1], and the positive leading high is at most r+2h+3. The same reader
therefore remains correct there. B0,B1,I leave R unchanged. Each K1 boundary
except the final expiry boundary is the next admitted full boundary.
This proves correctness at every declared layer boundary between the arrival
boundary tau and the expiry boundary tau+h, with expiry excluded. It does
not assert behavior during an unspecified physical interpolation of a layer.

At n=tau+h the anchor has moved to r+2h, outside the permitted anchor mask.
The positive leading pulse has also exited R. The positive reader is BLANK
because at most one high remains; the negative reader is BLANK because the
anchor is no longer permitted, although both highs can still be inside R.
There is no sign-dependent extension of the read window.

Crucially,

    tau+h = d+h+2 < L=2d+h+3.

Every step in this proof therefore precedes the first rail return. There is
no unproved boundary switch or source-interface assumption inside the read
interval. The raw word resides entirely in the counted receiver region
during the whole admitted hold interval while its decoded value is stable.

## 7. Whole apparatus inverse and budget

Each layer is a full-carrier bijection. B0,B1 and I are involutions, as are
the disjoint parallel layers K0,K1. Consequently

    F^(-1) = B0 B1 I K0 K1.

This inverse is defined on the entire integer raw carrier, not only the
binary preparations. Every layer preserves S,H,E. Initially

    S=2a,
    H=(4+2g)+(2m-2+2g)=2m+2+4g,
    E=14+(4m+2)=4m+16.

For the DATA apparatus, m=2L and L=2d+h+3 give

    raw cell count = 4L+4 = 8d+4h+16,
    H=4L+2+4g = 8d+4h+22-4phi,
    E=8L+16 = 16d+8h+40.

These are data-only budgets. Section 10 includes the clock required by the
final all-time truthful reader.

The source costs 14 initially and 12 after the third tick. The common
initial high launch pair supplies two excess units; the payer supplies
the other two. The final pre-return rail has exactly two highs, costing
4m+4. Therefore 12+(4m+4)=4m+16, with full H conservation already proved
independently at every gate. There is no unexplained energetic payment
for the transmitted sign distinction.

Distance, hold capacity, occupied background, source and initial marker
stock are all explicit. These formulas are construction budgets, not
minimum-resource theorems or identifications with measured physical energy.

## 8. Complete data recurrence and the ungated reader's false passage

The returning data word must not be ignored. To analyze it exactly, define

    Z_a=(a(1+J),a(1-J),W,-W).

As for Z_- above, T4 fixes Z_+: B0 sees equal relative accounts g, while
B1 sees first difference -rho(1+J), which is odd. Thus both Z_a are fixed
by T4. In even-lane coordinates q=i/2 modulo L, every rail step shifts a
high by one. The source and launch interface have the following relevant
rules, where b is the incoming launch occupation and b' its outgoing value:

| Source before tick | b | Source after T4 and I | b' |
|---|---:|---|---:|
| A_+ | 0 or 1 | B_+ | b |
| B_+ | 0 | C_+ | 0 |
| B_+ | 1 | Z_+ | 0 |
| A_- | 0 | C_- | 0 |
| A_- | 1 | Z_- | 0 |
| C_a | 0 | D_a | 1 |
| C_a | 1 | A_a | 1 |
| D_a | 0 | D_a | 0 |
| D_a | 1 | A_a | 0 |
| Z_a | 0 | C_a | 1 |
| Z_a | 1 | Z_a | 1 |

This finite transition table follows directly from the balance identities,
T4 identities and parity refusals proved above. Combining it with the
one-site shift gives the following complete return certificates. Between
listed events the source is D_a, the launch input is low, and the two highs
translate by one; the first three events have the behavior already proved.

| Full tick | Positive source | Positive rail high q values |
|---:|---|---|
| 0 | A_+ | {0} |
| 1 | B_+ | {1} |
| 2 | C_+ | {2} |
| 3 | D_+ | {3,1} |
| L+1 | A_+ | {L-1} |
| L+2 | B_+ | {0} |
| L+3 | Z_+ | empty |
| L+4 | C_+ | {1} |
| L+5 | D_+ | {2,1} |
| 2L+3 | D_+ | {0,L-1} |
| 2L+4 | A_+ | {0} |

| Full tick | Negative source | Negative rail high q values |
|---:|---|---|
| 0 | A_- | {0} |
| 1 | Z_- | empty |
| 2 | C_- | {1} |
| 3 | D_- | {2,1} |
| L+1 | D_- | {0,L-1} |
| L+2 | A_- | {0} |

Because L>=6, the stated events do not alias. The full raw data array,
including the source, launch and every low pair, is restored at 2L+4 for
positive input and L+2 for negative input. Hence

    F_data^P z_a = z_a, P=2L+4,

for both preparations. A minimal-period assertion is unnecessary here.
Bijectivity and the explicit return make this an all-time analytical
continuation, not a simulation ending before return.

The table also exposes a real failure of the ungated data reader. The
positive source emits its second pair of highs at L+4 and L+5, so their
separation is now TWO raw rail sites rather than four. At full ticks

    L+d+4, ..., L+d+h+3

that word crosses the same receiver with the permitted anchors. The
section-6 reader consequently returns VALUE(-1) for the original positive
input. This is an explicit counterexample to extending the first-window
reader to an all-time decoder. It is retained as a negative result.

This is also an exact alias obstruction to ANY fixed instantaneous reader
of the data rail alone, even one allowed to inspect the whole data rail.
At positive tick L+5 the source is D_+ and the complete rail high set is
{2,1}; at negative tick 3 the source is D_- and the entire rail is identical.
Their subsequent rails remain identical after the same number of shifts
until feedback, while their source signs differ. In particular the negative
first read window and the positive later window separated by L+2 ticks have
identical complete data-rail states. Any such reader that correctly reads
-1 in the former must give the false -1 in the latter. A different fixed
rail-only formula cannot cure this alias. Additional retained state or a
phase reference is required for the stronger all-time contract; section 9
supplies the latter explicitly and charges for it.

## 9. Counted local phase qualification by the same gate

Complete the apparatus by adding a disjoint clock rail with 2P fixed pair
sites, P=2L+4. Initialize clock site 0 to high=(J,-J), every other clock
site to low=(1,-1), identically for both source signs. Apply its even and
odd conveyor layers in parallel with the DATA K0 and K1, respectively.
There is still one fixed five-layer law and still only the primitive B:

    F_full = K1_joint K0_joint I B1 B0.

The clock does not control, reset or switch any data gate. It is a finite,
explicitly funded local phase reference used by the reader. At full tick n
its sole high is at clock site 2n modulo 2P; at the intervening K0 boundary
it is at 2n+1. The complete clock array returns after P full ticks.

The receiver has a second local component on the clock rail:

    R_clock={2tau,2tau+1,...,2(tau+h)-1}, tau=d+2.

This is a corridor of 2h clock sites. Supply a layout with this short arc
and the data receiver arc co-located in the receiver region. They need no
interaction edge. The reader accesses only these two local arcs, not the
whole clock ring, the source, or a global time label. The two cycles and
their layout are declared apparatus geometry, not a derived spacetime.

Define ENABLE to mean that every pair in R_clock is canonical low/high
and exactly one of them is high. The final total reader is

    R_full = R_data when ENABLE, otherwise BLANK.

At full boundaries on the declared preparations,

    ENABLE iff n modulo P belongs to {tau,...,tau+h-1}.

During the K0 layer between n and n+1 the same condition holds, because the
clock corridor includes both 2n and 2n+1 for every admitted n. During B0,B1,I
neither receiver component changes. Thus the phase qualification has no
intermediate-layer holes within the hold interval and switches off at the
same final K1 boundary as the prescribed expiry.

The data array has period dividing P on each input, and the clock array
has period P. Therefore every enabled window is an exact recurrence of the
proved first data window, including its intermediate layer boundaries.
At all other boundaries the final reader is BLANK regardless of the data
word. In particular the wrong positive second passage from section 8 occurs
a half-period L+2 after the admitted passage and is suppressed.

The final all-time contract at full ticks is exactly

    R_full(F_full^n z_a) = VALUE(a)
        when n mod P is in {d+2,...,d+h+1},
    R_full(F_full^n z_a) = BLANK otherwise.

Within each admitted hold the same correct value is returned at every
intervening layer boundary. This supplies a truthful finite retained record
with explicit continued erasure and recurrence. It does not create a fresh
independent input whenever the record recurs.

The phase mechanism is materially part of the apparatus. Removing it really
breaks the stronger contract, as the exhibited false passage proves. It
cannot be omitted from the resource account or relabeled as a free external
observation time.

## 10. Full inverse and complete resource account

The joint K0,K1 layers remain involutions because their blocks are disjoint
within each rail and the rails are disjoint. Thus

    F_full^(-1) = B0 B1 I K0_joint K1_joint

on the whole raw integer carrier. All five layers preserve S,H,E. The clock
costs 4P raw cells and has H_clock=4P-2+2g and E_clock=8P+2. Adding the data
apparatus of section 7 gives

    total raw cells = (4L+4)+4P = 12L+20,
    H_total = (4L+2+4g)+(4P-2+2g)
            = 12L+16+6g = 12L+28-6phi,
    E_total = (8L+16)+(8P+2) = 24L+50,
    S_total = 2a,
    L = 2d+h+3, P = 2L+4.

Every stock and clock cell is prepared before the unknown sign is processed.
All non-source coordinates are identical in the two preparations, and full
H/E are identical. There is no uncharged timer, reset, output-controlled
switch or post-start replenishment. The source sum differs, as it must for
these particular raw inputs, and is preserved exactly.

For example d=4,h=8 gives L=19, P=42, 248 raw cells, E=506 and
H=256-6phi. The first read window is full ticks 6 through 13, inclusive,
with the same eight-tick readable window recurring every 42 ticks. These
numbers are direct substitutions in the analytical formulas, not a reported
scientific run or a resource optimum.

## 11. Scope and prospective verification still owed

The positive result is one continuing native-B apparatus for an unknown
local sign, paid temporal-word encoding, exact transport, remote finite
retention and truthful occupied-state continuation. The fixed-site
no-export theorem is respected: source B1 changes the original constituent
pairs, and the conveyor sees the new account word emitted by that exact
interface. The conveyor alone still does not export an arbitrary local phase.

The receiver is regional delay memory with a paid local phase reference.
A stationary point latch, a literal blank pair excited by the fixed-pair
conveyor, permanent archival storage, an unlimited stream of independent
bits, universal computation, native-U realization and physical energy,
proper time, gravity or Born occurrence are not established here. Supplied
geometry, five-layer order, initial stock, semantic reader and its local
phase corridor remain declared choices.

A new prospective verification must freeze the full law, raw preparations,
reader, d/h range, layer-boundary contract, data recurrence, charged clock,
exact arithmetic implementations and negative controls BEFORE scientific
execution. It should compare raw states against both encoder and recurrence
tables, exercise F and F^(-1), check full H/E/S, inspect every layer through
at least a complete common period, and compare the reader to the exact
all-time formula. The ungated positive second-passage misreading is a required
negative control, not an outcome to hide by stopping early. This note supplies
the analytical candidate; it is not a completed computational gate or a
substitute for independent review.
