# A local thermal controller with fixed exported records

**NON-CANONICAL, L1. Conditional analytical construction; independent
mathematical acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1769. The source is the immutable revision
`811daddc3b2f085ee5bc6f50261ac95a4c11fe44` named in CONTRACT.md.
No source file is changed. This is a construction on the complete raw
space, not an expanded circuit calculation or a numerical simulation.

The controller transports a finite payload through separate spatial
layers, applies one small gate per layer, freezes each output when its
latch is exported, and returns all three core banks to their original
physical sites. Distinct cursor lanes implement the outward and return
transfers. A counted identity detour makes the first record available
before the first reset has appreciable probability. Every auxiliary
initial factor is thermal; the forty-five admitted information qubits
retain their separately specified joint input and reference.

## 1. Frozen local instructions and fixed interaction scale

Let S,K_D,g_D and d be the frozen core parameters. The complete core
has integer planar site coordinates (x_u,y_u). Every old local term
has at most seven sites in a Manhattan-radius-16 ball. Let Q_D be its
rounded onsite energy, R_D its residual, and C_D=N_X+n_fuel its conserved
occupation count. The full raw source satisfies

    [H_D,Q_D]=[H_D,C_D]=0,       0<=R_D<=d C_D.        (L1)

Use the primary complete-space local product word specified by the
companion compilation proof. Each approximation to
V_D=exp(-i H_D tau/hbar) includes its exact onsite-Q phase gates and
has operator error below 2^-120. No free-Q phase is silently omitted
from this operator comparison. Put

    M=2^121(K_D+1)^4,
    P_0=2M(2K_D+1)+14+4S.                             (L2)

This is the primitive count for two approximated core runs, two
seven-pair exports and two S-pair resets. Each primitive is a complete
raw unitary on at most seven sites, commutes with the appropriate
rounded energy and summed C count, and has the inherited local support.
The exact matched-spectrum export/reset SWAPs are two-site gates.

Each export uses its five archive pairs, pointer pair, and latch pair
in that order, with the latch last. Insert an identity primitive just
before a latch instruction if needed to put that instruction at an odd
stage number. Finally insert an identity primitive after reset two if
needed to make the total stage count P even. Thus

    P_0<=P<=P_0+3,       P even.                      (L3)

The two latch stages t_1<t_2 are odd. Their padding changes neither the
target word nor the two-run error below 2^-119.

As fixed in CONTRACT.md, let E_* be the largest frozen physical onsite
gap, and set before M or the new geometry is chosen

    J_*=E_*+g_D+d,            g_out=J_*/4.              (L4)

The enlarged device never increases these scales. Its execution time
will grow with its cursor length.

## 2. Payload coordinates and the fixed output locations

Let x_min,x_max,y_min,y_max bound the frozen core coordinates, and put
X=x_max-x_min, Y=y_max-y_min. Translate each old coordinate to
(x,y)=(x_u-x_min,y_u-y_min). For every old site u, put the three
same-spectrum core channels at planar positions

    D_u:   (8x,   8y),
    F1_u:  (8x+2, 8y),
    F2_u:  (8x+4, 8y).                                (L5)

For each of the seven physical output sites u in the old final record
block B, also put output channels at

    O1_u:  (8x,   8y+2),
    O2_u:  (8x+2, 8y+2).                              (L6)

There are W=3S+14 payload channels. Distinct channel positions have
Manhattan distance at least two. Their planar bounding box is contained
in [0,P_x] times [0,P_y], where

    P_x=8X+4,             P_y=8Y+2.                   (L7)

For each channel put a physical same-spectrum copy at (x,y,4t),
t=0,...,P. All these copies, including ones later left unused, are
counted. There are W(P+1) data qubits.

The fixed saved output O_i is the seven-site block at layer t_i, not
an abstract register renamed at every step. In the frozen core all
seven record sites share its final y-row: archive/pointer data have
y=2s and the latch is at (4W_old+5,2s). The latch is further right
than each archive/pointer site. Consequently every output channel in
(L6) has y=P_y and its latch is furthest right among its seven channels.
This explicit feature is used below; it is not inferred from their
logical register names.

## 3. Outward layers: one transfer edge and one gate edge

Define a rectangular raster F with integer vertices

    -4<=x<=P_x+4,          -4<=y<=P_y+4,
    F_num=(P_x+9)(P_y+9).                              (L8)

Its base path begins at A_F=(-4,-4), scans the first row left to
right, moves one unit upward, scans the next right to left, and
continues. Since P_y+9 is odd, it ends at
B_F=(P_x+4,P_y+4). It has F_num-1 edges and visits every vertex once.
Stage t places this path at height z=4t-2, in the base direction for
odd t and reverse direction for even t. Consecutive stages are joined
by four vertical edges at their common outer corner. These corners
are outside every data position.

On the incoming edge to an active channel position (x,y), apply the
same-spectrum vertical SWAP between (x,y,4t-4) and (x,y,4t). This
instruction has two data sites and two cursor endpoints. The channel
is inactive after its output has been frozen; its incoming edge then
has identity instead of a transfer.

The stage's program gate acts on its destination-layer operands. Put
that gate on the outgoing cursor edge immediately after the last of
its operands has been transferred. Every other operand has arrived
already. The minimum channel spacing in (L5)-(L6) ensures that this
outgoing edge does not also transfer a different channel. Guard rows
ensure that such an outgoing edge exists. Thus a seven-data-site gate
uses exactly its seven sites and two cursor endpoints, not an extra
old-row site. Combining its last transfer and gate would have required
ten sites and is not done.

For a padding identity with no nominated operands, use the first raster
edge. Zero-term or zero-phase identities may instead keep their named
old operand location. Neither convention changes any state or count.

Transfers of other channels commute with the gate. Hence one completed
stage is exactly the product of its active-channel SWAPs followed by
the specified gate, independent of all destination-row contents. This
operator identity holds on the entire tensor product, including dirty
or correlated future copies. It does not assume empty transport space.

At an odd latch stage, the raster visits y=P_y in the left-to-right
direction: its row offset P_y+4 is even. All seven O_i operands have
therefore arrived before its latch is transferred, and the matching
core latch, at y=P_y-2, arrived earlier. Put the last latch SWAP on
the next outgoing edge. At that edge the full saved block at layer
t_i contains the exported record. Freeze all its channels immediately:
no subsequent forward transfer, program gate or return transfer acts
on that physical block.

Before this gate the fixed latch is either its original cold copy or
the transported initial output latch. On their ground-state comparison
both are zero. The pointer or archive may have arrived sooner; the
zero latch still excludes an incomplete physical record. This is why
the odd-stage ordering and latch-last export are necessary.

## 4. A separate return lane to the original three banks

After the final stage, all three core-bank states are in layer P.
The even P makes the final outward cursor position
(-4,-4,4P-2). Define a smaller raster with

    -2<=x<=P_x+2,          -2<=y<=P_y+2,
    R_num=(P_x+5)(P_y+5).                              (L9)

Its base raster starts at (-2,-2) and ends at (P_x+2,P_y+2), because
P_y+5 is odd. Add a four-edge horizontal lead from
A_R=(-6,-2) to its start, and a four-edge lead from its end to
B_R=(P_x+6,P_y+2). Its total length is R_num+7.

Join the final outward vertex to (A_R,4P-1) by the following five
edges: two steps left to (-6,-4,4P-2), one step upward in z, then
two steps in positive y. Traverse the return raster at z=4P-1 from
A_R to B_R. Descend four edges at B_R to the next return plane and
traverse the raster in reverse. Continue down through t=P,...,1,
alternating directions. The last return plane is z=3 and, since P
is even, the final position is (A_R,3).

At each core-bank channel position in return plane t, its incoming
edge SWAPs the two corresponding data copies at z=4t and z=4t-4.
There are no output-channel return SWAPs. A whole return sweep moves
all three active core-bank states one layer down. Repeating it puts
D,F1,F2 at their original physical layer-0 sites. In each such vertical
column, the future-copy contents are restored to their original order.
The fixed O1/O2 blocks are excluded from this permutation. Displaced
unused output-copy values remain in their counted sites; no claim that
those separate permutations are reset is needed.

The cursor lanes are disjoint. Outward planes have z=4t-2; return
planes have z=4t-1. Outward vertical connectors use corners with
y=-4 or P_y+4, outside the return raster and its leads. Return vertical
connectors use x=-6 or P_x+6, outside the outward raster. Their
intermediate vertices therefore do not collide with the other lane,
data planes or saved outputs. The five-edge top link uses unused
coordinates. These facts also exclude a hidden alternate cursor path.

## 5. Exact path count, buffer and tail

Before adding a long buffer or final tail, the path consists of a launch
edge, the outward block, the five-edge top link, the return block and
one completion edge. Its length is

    B_0=P(F_num-1)+4(P-1)+5
            +P(R_num+7)+4(P-1)+2
        =P(F_num+R_num+14)-1.                         (L10)

Set B=max{512,B_0} and ell_lead=B-B_0. The first physical cursor is
at (-4,-4,2-ell_lead); an ell_lead-edge vertical lead joins it to the
first outward plane. This lead is outside all payload positions. Put
the outer fuel and sink next to its first site, at
(-5,-4,2-ell_lead) and (-5,-5,2-ell_lead), respectively.

The first completed export ends on an outgoing raster edge at layer
t_1. Its endpoint is u=(x_L+1,P_y,4t_1-2), where x_L is O1's latch
x-coordinate. The next raster edge ends at
v=(x_L+2,P_y,4t_1-2). Replace that next edge by this explicit detour:
descend one unit to z=4t_1-3, travel 2B-1 steps in negative y, one
step in positive x, travel 2B-1 steps back in positive y, then ascend
one unit to v. The replacement has 4B+1 edges, adding exactly 4B.
Its first 4B edges are identities; its last edge performs the original
edge instruction, which can be the O2-latch transfer.

This narrow rectangular detour is simple. Its two vertical-in-y legs
have x=x_L+1 and x=x_L+2, strictly inside the outer connector columns.
The plane z=4t_1-3 has no outward or return raster. Its only other
cursor vertices are exterior connectors, whose x or y coordinates
are disjoint from the detour. It also has no data sites. The detour
therefore adds no collision or long-range edge. Moving the original
instruction to its last edge still leaves its transfer support within
a radius-3 ball. No saved output is touched during the detour.

After the last return, complete from (-6,-2,3) to (-7,-2,3), with
the physical outer latch F at (-7,-3,3). Append a straight leftward
identity tail. Define

    L_c=5B,             K_out=10B.                    (L11)

The completion is at node L_c, and the appended tail has L_c edges.
There are exactly K_out physical cursor qubits: node zero is the
fuel configuration, not a further cursor. The base first-export index
e_1 is unchanged by the detour and satisfies e_1<=B<K_out/8.
Every first-reset edge is shifted by 4B, so its earliest index s_1
satisfies s_1>=4B>=3K_out/8. Completion includes both resets and the
return of all three core banks to their original physical sites.

## 6. Positive thermal launch and complete Hamiltonian

The outer launch exchanges

    |1,0,0>_(h,c,C_1) <-> |0,1,1>.                   (L12)

Fuel h has gap 3d, sink c gap d, and all pre-completion cursors gap
2d. At completion the cursor gap changes to d and F, of gap d, rises
from zero to one. Thus both special edges conserve rounded and physical
bare energy. Use the inherited beta_h, giving

    p_o=1/(1+exp(3beta_h d))>=1/3.                    (L13)

All other new positive-gap factors start at the one beta_c selected
after the complete inventory. Every zero-gap new factor is I/2.
There is no initial pure cursor or zero-energy readiness bus.

Let Q_payload sum the rounded onsite energies of all data copies.
Let C_all sum the old C_D over all three banks in all P+1 layers,
and let R_payload sum their old residuals. Output copies have no
residual. Define

    Q=Q_payload+3d n_h+d n_c+d n_F
       +2d sum_(j=1)^(L_c-1)n_(C_j)
       +d sum_(j=L_c)^(K_out)n_(C_j).                  (L14)

Write X_0=s_h^-s_c^+s_(C_1)^+, P_in=X_0^*X_0,
P_out=X_0X_0^*, D_0=P_in+P_out. Every ordinary edge has

    X_j=s_(C_(j+1))^+s_(C_j)^-G_j,
    D_j=n_(C_j)+n_(C_(j+1)),                          (L15)

with the local gate, transfer or identity assigned above. On completion
j=L_c-1 use G_j=s_F^+, retaining the same D_j. Put V_0=P_in,
V_j=n_(C_j) for j>=1, and

    a_j=g_out sqrt((j+1)(K_out-j))/(K_out+1),
    a_(-1)=a_(K_out)=0,      v_j=g_out-a_(j-1)-a_j>=0,
    H_hist=sum_j a_j(D_j-X_j-X_j^*)+sum_j v_j V_j,
    H_local=Q+H_hist.                                  (L16)

The ordinary 10/01 cursor blocks are positive unitary blocks; their
11 sectors have diagonal 2a_j. The launch has its positive exchanged
two-state block. Completion uses the contraction s_F^+, so its
[[I,-s_F^-],[-s_F^+,I]] block is positive. Every v_j is nonnegative.
Consequently H_hist and H_local are positive on the complete raw
space, including all multiple-cursor and invalid-data sectors.

Every instruction preserves Q and C_all. This includes each small
product-formula gate, every matched copy transfer, export and reset.
The exact physical bare reading and counterterm account are

    E_phys=Q+R_payload,       H_int=H_hist-R_payload,
    0<=R_payload<=d C_all,
    -d C_all<=U_t^*E_phys U_t-E_phys<=d C_all.          (L17)

The residual counterterms are onsite and include each copied old fuel.
The last inequality is a full-raw operator bound and hence an
unconditioned energy bound. It is not a statement about selected
successful records or an original-walk trajectory intertwiner.

## 7. Uniform support, radius, degree and strength

A transfer edge has two data sites and two cursor sites. Its data
separation is four in z; its support fits in radius 3. A program
edge has at most seven data sites and two cursor endpoints. Under
(L5), an old radius-16 ball scales to radius 128 in the plane.
The destination plane is two units from its cursor plane, and the
outgoing cursor endpoint adds at most one planar step. Radius 132
suffices; radius 256 is the fixed conservative contract. Matched
export/reset pairs have only the small offsets in (L5)-(L6).
Launch, completion and their diagonals have radius at most 2.

No two instructions have been fused to exceed nine sites. Each data
site participates in at most two outward transfers, two return
transfers, one program gate, one onsite physical-energy term and one
onsite residual counterterm. Saved outputs participate in fewer.
Each ordinary cursor site has two adjacent edge terms, its vertex
potential and its onsite term; the first cursor additionally occurs
in the launch-source potential. Launch fuel/sink/latch have only their
listed nearby terms. Thus incidence 64 is conservative, with room
well below the cap. The long buffer and raster subdivisions add sites,
not extra terms incident on an old site.

Each history edge has norm at most 2a_j<=g_out and each vertex term
at most g_out. Physical onsite gaps are at most E_*: future copies
keep their spectra, and 3d<=E_*. Residual counterterms have norm at
most d. Thus every listed term has norm at most J_* fixed in (L4).
All sites are qubits at distinct integer triples; the construction
has uniform finite geometry and degree, not a whole-device cell.

## 8. Thermal inventory and exact raw dimensions

Write the old core partition as S=C_c+H_h+Z, with C_c cold positive-gap
sites, H_h hot sites and Z zero-gap sites. At layer zero the three
core packages retain their actual independent thermal hardware and
the arbitrary joint input on their 45 information sites. Only layer
zero has these three old hot banks. All positive-gap core copies in
layers 1,...,P are cold, including copies of old fuel and hot-donor
sites. Their spectra are unchanged. The exact inventory is

    S_new=(3S+14)(P+1)+K_out+3,
    dim H_raw=2^S_new,
    H_new=3H_h+1,
    C_new=3C_c+3P(C_c+H_h)+2(P+1)+K_out+2,
    Z_new=(P+1)(3Z+12).                               (L18)

H_new+C_new+Z_new=S_new. The 45 information factors are a subset
of Z_new, not additional sites. The remaining zero-gap factors are
thermal I/2. All output-copy latches and all cursor, buffer, lead,
tail, return, launch and completion sites are included.

After P,B,K_out are fixed, choose

    beta_c d>=[120+ceil(log_2 C_new)]ln 2.              (L19)

The complete cold excitation probability is then below 2^-120. No
dimension or instruction count depends on beta_c. There is no bath
refresh between stages. For a sharper channel comparison one may
leave all three original cores and all future core-copy states actual,
and compare only the outer sink/cursors/F and every output-copy latch
with zero. Its defect weight obeys

    eta_ctrl<=[K_out+2+2(P+1)]exp(-beta_c d)<2^-120.   (L20)

Comparing all output-copy latches covers both the transported original
latches and the fixed destination latches before their arrival. The
exact permutation proof requires no cold readiness of other future
copies. Their actual thermal populations, energy and entropy remain
counted even when they add no channel error. Old source/reset errors
remain separate from eta_ctrl.

If S_info is the entropy of the joint 45-qubit information input, the
complete initial apparatus entropy is

    S_initial=S_info+(Z_new-45)ln 2
                  +sum_(positive-gap sites u)h_2(p_u). (L21)

For a partition including the passive reference, use its actual joint
information/reference entropy. No purification of a thermal factor is
assumed to be free.

## 9. Invariant history, early availability and final return

On the controller ground-state comparison, the outer fuel-ground
component has no cursor and never runs; its fixed output latches
remain zero. On its excited component, every initial data/reference
vector has the exact finite history specified above. The transfer
permutation identities identify its endpoint with the compiled
two-use word, with D,F1,F2 back at their original layer-zero sites,
and O1/O2 at their fixed export layers. All displaced values remain
in counted copies. The source-side hardware reset and joint-channel
claims therefore use these fixed tensor factors.

The ordinary unitary edges and special launch/completion give on that
history

    H_hist=g_out I-[2g_out/(K_out+1)]J_x,
    p_j(t)=binom(K_out,j)sin(theta)^(2j)
                         cos(theta)^(2(K_out-j)),
    theta=g_out t/[hbar(K_out+1)].                    (L22)

The actual input and comparison commute with Q: unknown information
has zero energy and all other initial factors are diagonal onsite
Gibbs states or compared ground states. Since [Q,H_hist]=0, the free
Q evolution cancels from their density evolution. The diagonal fuel
mixture has no coherence between active and dormant branches.

Let

    T_hold=pi hbar(K_out+1)/(3g_out).                  (L23)

At t_1=T_hold/2, sin(theta)^2=1/4. The inequalities in Section 5 and
Hoeffding's bound yield

    Pr{j<e_1}<=exp(-K_out/32),
    Pr{j>=s_1}<=exp(-K_out/32).                        (L24)

Thus with conditional active-history probability at least
1-2exp(-K_out/32)>1-2^-128, the first physical output is exported
and no first-reset gate has yet occurred. Here K_out>=5120 and e>2
suffice for the displayed exact power-of-two estimate.

There is also an explicit interval, not only the single time t_1.
On the outward half define

    I_early=[(3T_hold/pi)arcsin sqrt(15/64),
             (3T_hold/pi)arcsin sqrt(17/64)].          (L24a)

It contains T_hold/2. Throughout this positive-width interval the
binomial parameter lies between 15/64 and 17/64, at least 7/64 from
each of the conservative thresholds 1/8 and 3/8. Thus the total
plateau deficit is at most

    2exp(-49K_out/2048)<2^-128.                       (L24b)

For the last inequality K_out>=5120 and e^3>16 suffice. The latter
follows already from the first five terms of the positive series for
exp(3). This interval and its error are fixed by the constructed path.

On every subsequent forward-history node, O1 is untouched. For its
fixed record-only projector Q1=n_(O1,L)n_(O1,P), tracing the cursor
gives the exact comparison substate

    Sigma_1(t)=p_o Pr{j>=e_1} Sigma_1,compiled.         (L25)

The joint record/reference state is preserved; the reference must be
passive. Future information inputs later acted on are treated by the
joint two-use theorem instead. The binomial tail in (L25) is monotone
on the outward half of the clock and remains at least its value at
t_1 while the first reset and second run proceed. It stays above the
same bound through 2T_hold because sin(theta)^2>=1/4 on that whole
interval. This is a physical-time availability estimate, not only a
literal untouched-prefix statement.

Throughout the final window [T_hold,2T_hold],

    Pr{j>=L_c}>=1-(3/4)^(K_out/2)>1-2^-128.           (L26)

The physical completion latch F is raised only after both resets and
all return transfers. Its completed substate is p_o times this tail
weight times the compiled endpoint joint state. Consequently the
joint target involving O1,O2, original-site D hardware, I2 and R
has exactly the intended fixed-factor meaning. Approximation and
thermal normalization bounds are supplied by TWO_USE_CHANNEL.md.
F is not replaced by a hidden clock measurement.

At 3T_hold the comparison history returns exactly. The inverse
instruction/permutation word restores the original data and output
copies before the inverse launch. Thus fixed output read probabilities
are at most eta_ctrl at that time. Saved outputs are untouched by
subsequent forward instructions, not by every edge of the reversible
Hamiltonian for all time. The buffer and tail supply finite retention;
they do not implement autonomous permanent stopping.

## 10. Inclusive energy moments and finite capacity

Let mu_Q,hot and mu_R,hot be the old package's initial rounded and
residual means at its declared two temperatures; let mu_Q,cold and
mu_R,cold use beta_c on every positive-gap old-core site. Put
gamma=(1+exp(beta_c d))^-1, gamma_2=(1+exp(2beta_c d))^-1. Then

    <Q>=3mu_Q,hot+3P mu_Q,cold+2(P+1)d gamma+3d p_o
             +2d(L_c-1)gamma_2+d(L_c+3)gamma,
    <R_payload>=3mu_R,hot+3P mu_R,cold.                (L27)

The initial occupation budget satisfies <C_all><1+2^-120: the three
original old fuel excitations contribute one, and every other counted
C occupation is cold. This uses the complete inventory in (L19).

The diagonal history identity and total interacting moments are

    A_hist=g_out sum_(j=1)^(K_out)n_(C_j)+g_out P_in
                      +a_0(P_out-n_(C_1)),
    M_0=Q+A_hist,
    <H_local>=<M_0>,
    Var(H_local)=Var(M_0)+sum_j a_j^2
                                  <X_j^*X_j+X_jX_j^*>. (L28)

Hopping means and distinct-edge cross terms vanish on the initial
diagonal cursor/fuel factors. For v=(h,c,z) in {0,1}^3, define

    m(v)=3dh+dc+(2d+g_out)z
              +g_out 1_(v=100)+a_0[1_(v=011)-z],
    w(v)=p_o^h(1-p_o)^(1-h) gamma^c(1-gamma)^(1-c)
                                  gamma_2^z(1-gamma_2)^(1-z).

For all other sites let e'_u be the Q coefficient plus g_out on
remaining cursor sites, and just the Q coefficient elsewhere. With
their actual physical-Gibbs probabilities p_u,

    <M_0>=sum_v w(v)m(v)+sum_u e'_u p_u,
    Var(M_0)=sum_v w(v)m(v)^2-[sum_v w(v)m(v)]^2
                           +sum_u (e'_u)^2p_u(1-p_u). (L29)

The information correlations have zero energy and do not modify these
expressions. The launch hopping weight is
p_o(1-gamma)(1-gamma_2)+(1-p_o)gamma gamma_2. Ordinary edges have
weight z_j(1-z_(j+1))+(1-z_j)z_(j+1); completion additionally has
latch factors (1-gamma),gamma. These formulas include interactions,
all future copies and all control resources without a large enumeration.
Put pi_in=p_o(1-gamma)(1-gamma_2) and
pi_out=(1-p_o)gamma gamma_2. Then
pi_out/pi_in=exp[-3d(beta_c-beta_h)]<1, giving the strict
nonstationarity witness
||[H_local,rho_in]||_1>=2a_0[pi_in-pi_out]>0.

If Q_D,max and R_D,max are the old raw maxima, the new capacities obey

    Q_max=3(P+1)Q_D,max+2(P+1)d+(3L_c+4)d,
    E_phys,max=Q_max+3(P+1)R_D,max,
    0<=H_local<=[Q_max+(2K_out+1)g_out]I.              (L30)

No term strength increases with these extensive capacities. Enlarging
the circuit increases its length, volume, resource count and runtime
through (L23). The device remains a finite, specified analytical model
with exact spectra and couplings. Precision tolerance, native derivation,
material outcome selection and replenishment of the spent stock are
separate physical questions.
