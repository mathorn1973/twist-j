# A static local controller returning both outputs to the original ports

**NON-CANONICAL, L1. Conditional analytical candidate-T. Independent
acceptance pending.** Author: A. M. Thorn. Apache-2.0.

This note compiles two specified finite gate words into one positive,
time-independent Hamiltonian on the entire finite raw space. It returns
the payload to its original physical sites after each word. The two
return events have different flags and different time windows. This is
an added Hamiltonian model; it is not a derivation from the native
six-pentit rule or an identification of the native occupation energy
with a spectral logarithm of the source unitary. No expanded circuit,
scientific program, or numerical simulation was executed.

## 1. Input word, site types and fixed scales

Let the payload consist of S finite sites in a specified planar layout.
It contains the original occupation registers, all helper registers,
the full ladder rail, and all hot and cold reset donors. In particular,
a single occupation coordinate is one four-state site with charges

    q_h=diag(0,2,2,8),                                (S1)

corresponding to occupations 0,+1,-1,2. Its two encoding bits are not
transported separately. A ladder is one 26469-state site with charges
0,...,26468. A helper is a zero-gap qubit. Each reset donor, hot or
cold, is a qubit with gap

    G=17643 epsilon,       epsilon>0.                 (S2)

Thus both members of a reset pair have the same spectrum. A common
hot inverse temperature satisfying beta_h G=log 2 gives excitation
probability 1/3 for these donors and the launch fuel alike.

The two specified complete raw unitary words have P_1 and P_2 gates:
the first cools the original helpers and prepares the source; the
second implements the three specified forward source steps. Each
gate has at most seven payload sites, commutes with their summed
bare onsite energy, and has a fixed bounded geometric support.
The primitive counts and the readiness contract are supplied by the
companion program and thermal proofs. The construction below works
for positive P_i; the chosen application has even P_i.

More precisely, use integer payload coordinates in
[0,X_0] times [0,Y_0], with distinct sites at distinct coordinates.
Every gate support lies in a Manhattan-radius-128 ball. The four
source occupations to be excited by launch, and the home ladder, also
lie in one such fixed local cluster. These are premises on the
already routed word. A growing list of donors cannot be coupled to
one distant target without the counted local routing that establishes
this premise.

Fix g>0 before choosing word length, copy count or padding. Put

    J=max{26468 epsilon,g}.                           (S3)

Every displayed summand in the final Hamiltonian has norm at most J.
Its support has at most nine sites and Manhattan radius at most 1024.
The number of summands incident on any physical site is at most 64.
These are bounds on the stated decomposition, including onsite terms;
they do not bound the norm of the extensive total Hamiltonian by J.

## 2. Whole-site copies and one raster per gate

Scale every payload coordinate by four. The original payload remains
at z=0. Put an identical-spectrum copy of every payload site at

    z=4t,  t=1,...,P_1,
    z=-4t, t=1,...,P_2.                               (S4)

There are exactly S(1+P_1+P_2) payload sites. This counts every
occupation four-level site, entire ladder and donor separately.
The spectra of different payload columns may differ; only copies
within one column are SWAPped.

Use the integer raster rectangle

    -2<=x<=4X_0+2,  -2<=y<=4Y_0+2,
    F=(4X_0+5)(4Y_0+5).                              (S5)

Its base path starts at (-2,-2), scans the first row to the right,
moves one step up, scans the next row to the left, and continues.
It visits every vertex exactly once. Its odd number of rows makes
its endpoint (4X_0+2,4Y_0+2).

For excursion i use this raster at z=4t-2 for i=1 and at z=-4t+2
for i=2. Odd stages traverse the base direction; even stages traverse
the reverse. Consecutive rasters are joined by four vertical edges
at their common outer corner. The corner lies outside all payload
columns. These links have three new intermediate vertices each.

On the incoming raster edge to a payload coordinate, apply the full
SWAP between that column's previous and destination layer. Place
the stage's program gate on the outgoing raster edge immediately
after its last operand has arrived. The other operands have already
arrived. Different payload coordinates are at least four lattice
steps apart, so this gate edge does not also transfer another site.
The outer guard provides an outgoing edge even for the last payload
coordinate. An identity stage can use the first raster edge.

All remaining transfers commute with the stage gate. Consequently a
completed outward stage equals all its whole-column SWAPs followed
by the declared gate on the destination layer. This is an operator
identity on the complete tensor product, including arbitrary mixed
or correlated future copies. It requires no empty-space promise.

## 3. Local launch lead and two colors on the same return path

Choose nonnegative multiples of four x_*,y_* near the launch cluster,
with x_*<=4X_0 and y_*<=4Y_0. The first cursor sites are

    c_+=(x_*,y_*,1),       c_-=(x_*,y_*,-1).           (S6)

They are local to the original source and home ladder. In particular,
launch is not an interaction from a distant raster corner.

For the positive excursion, a lead from c_+ travels in negative x
to (-2,y_*,1), then in negative y to (-2,-2,1), then up one step
to the first raster corner. Reflect it in z=0 for the negative
excursion. Each lead has

    ell=x_*+y_*+5                                    (S7)

edges. Its plane z=+1 or -1 contains no payload site or raster.
Combining the lead, rasters and interstage links gives

    r_i=P_i F+3(P_i-1)+ell                           (S8)

distinct physical cursor vertices for excursion i. This count includes
its first site c_+ or c_- and its last raster vertex.

Each such vertex is a qutrit with orthonormal states
|0>,|F>,|R>. Traverse the outward path in color F, applying the
instructions just specified. At its last vertex apply an onsite
F-to-R transition. Retrace the same spatial path in color R. On this
return, repeat just the matched whole-column SWAP instructions in
reverse order; replace all program-gate instructions by identities.
The lead also carries identity in both directions.

Thus an excursion from its initial F state to its final R state has

    (r_i-1)+1+(r_i-1)=2r_i-1                         (S9)

history edges. Its 2r_i legal occupied-clock states are distinct,
even though pairs share one physical qutrit. No color conversion is
included anywhere except its single terminal turn.

The reverse SWAP chain restores every future-copy state to its exact
initial position and puts the transformed payload at z=0. One way
to prove the assertion is to move each stage's remaining transfers
before its gate as in Section 2, then conjugate the destination-layer
gate by the cumulative whole-payload permutation. It becomes that
gate on the original payload. The final inverse permutation cancels
all transport. Hence the complete excursion is exactly

    word_i on original payload tensor I_on_future_copies.  (S10)

The identity includes correlations with an arbitrary reference or
between future copies. Tracing out displaced junk is not part of
this proof. The two excursions use disjoint copy layers, while
sharing only the original payload.

## 4. Explicit padding, two flags and exact clock count

Let k>=0 be the precision parameter used by the companion bounds and
choose an integer

    B>=max{r_1+1,r_2+1,8192,32(k+3),4Y_0+4}.
    L_1=B-r_1-1,   L_2=B-r_2-1,   K=12B.             (S11)

Use two separate qubit flags A and B_f, both with gap epsilon. The
subscript distinguishes the final flag B_f from the integer B.
Initially both flags are zero on the comparison subspace. No third
run flag is used.

The full path is the following exact edge list.

1. Node 0 is the fuel-ready state with no cursor. Launch reaches
   color F at c_+ at node 1. The first excursion ends in color R
   at c_+ at node 2r_1.

2. From there take L_1 steps in positive x, two steps in positive
   y, then L_1 steps in negative x, ending at
   c_A=(x_*,y_*+2,1). Its length is 2L_1+2. The last edge raises
   A from zero to one. Its endpoint is exactly node 2B.
   For L_1=0 the path is simply the two positive-y steps.

3. From c_A take B-1 steps in positive y, two steps in negative z,
   then B-1 steps in negative y, ending at
   c_E=(x_*,y_*+2,-1). This identity buffer has exactly 2B edges;
   c_E is node 4B. Its vertical segment is outside the payload
   rectangle because of the last lower bound in (S11).

4. Take two steps in negative y to color F at c_-. Execute the
   second excursion. This ends in color R at c_- after a total
   of 2+(2r_2-1)=2r_2+1 edges from c_E.

5. From c_- take L_2 steps in positive x, one step in negative y,
   then L_2 steps in negative x, ending at
   c_B=(x_*,y_*-1,-1). This adds 2L_2+1 edges. Raise B_f on its
   last edge. The endpoint is exactly node 6B.

6. Append 6B identity edges in negative y from c_B, at fixed x_*
   and z=-1. The last node is K=12B.

Put A at (x_*-1,y_*+2,1), adjacent to c_A, and B_f at
(x_*,y_*-1,0), adjacent to c_B. These are unused positions:
the latter has y-coordinate not divisible by four, and the former
is outside both its lead and padding track. Fuel is another unused
local site near c_+. No additional logical history state is assigned
to a flag or fuel site.

All newly introduced cursor vertices outside the two colored paths
are qubits. They are distinct. Indeed the positive lead runs toward
negative x and then down at x=-2, while the positive padding runs
toward positive x and back at y_*+2. The positive buffer continues
above that row. The negative lead is its mirror; second ingress lies
between y_* and y_*+2; final padding lies at y_* and y_*-1; final
tail lies below y_*-1. The buffer's only crossing of z=0 is beyond
all payload coordinates. Raster planes, payload planes and the
lead planes are distinct; raster connectors use exterior corners.
Orthogonal colors account for the deliberate outward/return reuse.

The exact cursor counts are

    N_3=r_1+r_2,
    N_2=(2L_1+2)+2B+1+(2L_2+1)+6B
       =K-2(r_1+r_2),
    N_cursor=N_2+N_3=K-r_1-r_2,
    sum_cursor (dim-1)=N_2+2N_3=K.                  (S12)

The single intermediate site in the second ingress contributes the
isolated +1; its final site c_- was already counted as a qutrit.
There is no physical site for virtual node 0. The two flags and one
fuel qubit are additional to (S12), as are all payload copies (S4).

## 5. Bare energy and energy-conserving launch

Give both colors of every first-excursion qutrit energy 3epsilon,
and both colors of every second-excursion qutrit energy 2epsilon.
Each other occupied cursor state has energy 3epsilon before the
A-raising edge, 2epsilon from that endpoint until the B_f-raising
edge, and epsilon from the latter endpoint onward. Vacuum has
energy zero. At either flag edge a cursor gap drops by epsilon
and the corresponding flag gains exactly epsilon.

The launch fuel has gap G from (S2). Its launch partial isometry
maps the following local basis vectors:

    |fuel 1, four seed occupations 0, home ladder 0, cursor 0>
      -> |fuel 0, four specified charge-2 occupations,
          home ladder 17632, cursor F at c_+>.       (S13)

The four signs and the known scalar phase in this map are the
specified seed under the occupation intertwiner; memory is not
tested or changed. The energy identity is

    17643=8+17632+3.                                 (S14)

This is a seven-site operation: fuel, four occupation sites, home
ladder and first cursor. Let X_0 be this partial isometry, extended
by identity on all other factors, and put

    P_in=X_0^*X_0,  P_out=X_0 X_0^*,
    D_0=P_in+P_out,  V_0=P_in.                       (S15)

Its two supports are orthogonal. Fuel remains zero throughout the
subsequent word. The returned cursor is R rather than F at c_+.
Consequently the good return cannot trigger the inverse launch or
start a second autonomous run. An initially ground-state fuel and
empty cursors is a dormant comparison branch; all history terms
annihilate it.

Let H_0 denote the sum of all bare onsite Hamiltonians: all payload
copies, donors, ladders, cursor states, two flags and fuel. Every
program gate commutes with its local part of H_0 by hypothesis.
Every transport SWAP exchanges identical spectra. All ordinary
cursor hops and turns conserve H_0; the two flag edges conserve H_0
by the gap drop; launch conserves H_0 by (S14).

## 6. Complete raw-space positive terms

For an ordinary edge j from color alpha at site u to color gamma
at a different site v, write

    X_j=|0><alpha|_u tensor |gamma><0|_v tensor G_j,
    D_j=n_alpha(u)+n_gamma(v).                       (S16)

Here G_j is its complete unitary instruction, including identity
or a whole-site SWAP. For a flag edge multiply G_j=I by
|1><0| on that flag. This is a contraction rather than a unitary;
the same D_j is retained. For the terminal turn at one qutrit put

    X_j=|R><F|,       D_j=n_F+n_R.                  (S17)

For each nonzero history node j, V_j is the single occupied-color
projector at its named physical site. At a qutrit the F and R
nodes use distinct projectors, not their sum. Use (S15) at launch.

On the source/destination single-occupancy block of (S16),
D_j-X_j-X_j^* has matrix

    [ I  -G_j^* ]
    [ -G_j  I   ].                                  (S18)

It is positive with norm at most two for every contraction G_j.
On the double chosen-color occupancy it is 2I. On zero occupancy
it is zero. If either qutrit contains its other color, the hopping
vanishes and the remaining diagonal is 0,I or 2I. Thus positivity
holds also in opposite-color, multiple-cursor and unready sectors.
No restriction to the intended computation was used.

The turn (S17) has eigenvalues 0 and 2 on span{F,R}, and is zero
on vacuum. The launch block (S15) is the corresponding positive
two-state block, tensored with spectators. In all cases

    0<=D_j-X_j-X_j^*<=2I.                            (S19)

Choose

    a_j=g sqrt((j+1)(K-j))/(K+1),  0<=j<K,
    a_-1=a_K=0,   v_j=g-a_(j-1)-a_j>=0.             (S20)

Each a_j<=g/2. Define the full static law

    H_hist=sum_(j=0)^(K-1) a_j(D_j-X_j-X_j^*)
            +sum_(j=0)^K v_j V_j,
    H=H_0+H_hist.                                   (S21)

Equations (S19)-(S20) prove H>=0 on the entire raw tensor product.
Every summand in H_hist has norm at most g and commutes with H_0.
Consequently [H_0,H_hist]=0 exactly. H_0 is the counted occupation,
reservoir and controller energy; no claim that it equals the
original spectral energy Q=E_0 f(U_rec) is made.

An ordinary program edge contains at most seven payload sites and
two cursor sites. A transfer has two payload sites and two cursors.
A turn has one site, a flag edge three, and launch and V_0 seven.
After coordinate dilation, the radius-128 premise gives radius
at most 4*128+5<1024 for a gate edge. Transfers span four vertical
units, and all new nonlaunch cursor edges are nearest-neighbor.
The launch cluster has the same fixed radius bound. Every raw
onsite norm is at most 26468epsilon, including gap-G donors.

For incidence, a payload copy participates in at most two outward
transfers, their two return counterparts, one destination-layer
program gate, and its onsite term. A launch seed or home ladder
also appears in the launch block and V_0. A qutrit has at most
four intersite colored-edge terms, two vertex potentials, one
onsite term and, at its turn or initial site, the specified local
turn or launch term. A qubit cursor has at most two edge terms,
one potential and one onsite term. Each flag has its edge and
onsite terms. These explicit counts are all below 64; other
colors do not create additional terms. Thus (S3)'s uniform
support, radius, incidence and individual-strength bounds hold.

## 7. Exact path law and the two different availability windows

On the range of P_in with all other cursors empty and both flags
zero, apply each edge instruction to define the history isometries.
In particular the four seed occupations and the home ladder have
the input values specified in (S13).
Every edge is an isometry between its two legal history sectors;
the flag partial isometries have unit norm there. Distinct history
nodes are orthogonal because of their cursor color or, at node 0,
their fuel state. The launch projector and all color-specific
diagonals restrict exactly to their named path positions. Hence
the history restriction is unitarily equivalent to

    g I - (2g/(K+1)) J_x                             (S22)

in spin K/2, with no missing boundary diagonal. Tensoring by an
arbitrary external reference changes none of these identities.

Starting at node 0, the exact node probabilities are

    Pr_t(j)=binom(K,j) p(t)^j (1-p(t))^(K-j),
    p(t)=sin^2(g t/[hbar(K+1)]).                     (S23)

This is also valid with arbitrary future-copy states: each path
map is an isometry on the full admissible input family, preserving
inner products and its reference extension. Future copies can be
displaced or correlated during transit; (S10) restores them at
each completed excursion.
The Schrödinger evolution has the additional free factor
exp(-iH_0 t/hbar). It cancels on initial density operators commuting
with H_0, including their reference extension when that full
commutator vanishes. For a more general initial state it remains
explicit; (S22) alone is an interaction-picture assertion.

At nodes 2B<=j<4B the entire payload is at the original physical
sites with word 1 completed; A=1 and B_f=0. At nodes j>=6B both
words are complete at those same original sites; A=B_f=1. On
the intervening excursion some payload values occupy copy layers.
Thus A alone is not a permanent assertion of present source
readiness.

For the early outward interval defined by

    11/48<=p(t)<=13/48,
    0<=g t/[hbar(K+1)]<=pi/2,                       (S24)

each tail j<2B or j>=4B is at most

    delta=exp(-3B/32).                               (S25)

Indeed the corresponding fractional thresholds are 1/6 and 1/3,
each at distance at least 1/16 from the allowed mean. For a
Bernoulli sum, the centered log moment-generating function has
second derivative at most K/4, so it is at most K s^2/8.
Exponential Markov and optimization give exp(-2K a^2) at distance
a. With a=1/16 and K=12B this is (S25). Conditional on A=1 in
the good launch branch, the late-clock fraction is therefore at
most delta/(1-delta). The exact conditional thermal and reference
error bounds are stated in [THERMAL_CHANNEL](THERMAL_CHANNEL.md).

Put

    T_h=pi hbar(K+1)/(3g).                           (S26)

On the final interval T_h<=t<=2T_h, p(t)>=3/4. Therefore

    Pr_t(j<6B)<=(3/4)^(6B).                         (S27)

For example apply exponential Markov to 3^(-j):
E[3^(-j)]=(1-2p/3)^K<=2^(-K), and use the threshold
3^(-K/2). This yields 3^(K/2)2^(-K)=(3/4)^(K/2).
Only the one common launch probability enters either window;
there is no second thermally independent launch factor.

At t=3T_h, p(t)=0 and the good history returns to node 0 up to
a common phase. Both flags and all newly changed outputs then
return as well, subject to the explicitly retained free H_0 factor
for nonstationary initial data. A measurement at the early window
changes the evolution: no claim about the subsequent unmeasured
final window is conditional on having made that measurement.

## 8. Thermal cursor cost and scope of completion

Every nonvacuum cursor level has gap at least epsilon. A product
cold Gibbs state of all physical cursor sites therefore obeys

    Pr(any cursor nonvacuum)<=K exp(-beta_c epsilon), (S28)

because its total number of nonvacuum levels is exactly K by
(S12). The two flags add at most 2 exp(-beta_c epsilon).
The two qutrit colors are both counted; replacing their sites by
a single two-state vacancy estimate would be incorrect. Future
payload copies need no purity promise for (S10), although their
full Gibbs states, spectra, mean energy and capacities must be
counted in the complete resource ledger.

This closes a local static-control construction conditional on
the exact funded word, the specified site spectra and calibrated
couplings, and the thermal comparison proved separately. It does
not make either window permanent, provide a free measurement or
external archive, regenerate consumed thermal resources, or
derive those couplings from the native discrete rule. The two
physical outputs here are the original occupation ports at their
original locations, with their separate, explicitly timed flags.
