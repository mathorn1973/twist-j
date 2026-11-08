# A local autonomous clock for the conserving finite circuit

**NON-CANONICAL, L1. Conditional analytical candidate; independent
mathematical acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1767.

This note converts the finite conserving circuit into a positive static
Hamiltonian with bounded geometric support and qubit sites. It preserves
the specified completed record channel and gives a new finite window.
It does not preserve the continuous trajectory of the previous global
Hamiltonian or turn its source preparation into an equilibrium process.

The geometry and raw cursor completion adapt [#1761 HAMILTONIAN.md,
Sections 3-5, at
`32c17259c4baf40bb6d08b521adc642956b57e94`](https://github.com/mathorn1973/twist-j/blob/32c17259c4baf40bb6d08b521adc642956b57e94/notes/C-THERMAL-REGISTER-PREPARATION-N/HAMILTONIAN.md).
The changes here are three typed tracks, weighted label energies, four-site
controlled funded hops, and a physical pointer written only at the final
edge. All new row copies and cursor sites are counted explicitly.

## 1. The conserving circuit interface

The companion circuit construction fixes a finite sequence of complete
raw qubit unitaries. The target word is the battery preparation `C` of
[PREPARATION.md](PREPARATION.md), followed by
`Gamma_B(U_f(P_x tensor I_F))`, then the controlled archive exchange and
finally the flag-to-pointer CNOT. Thus the abstract source and battery
wavepacket are prepared within the complete word before its output is
compared with [FINITE_MODEL.md](FINITE_MODEL.md). All circuit scratch is
restored before the final pointer write. The independently stated
whole-word battery error is retained.
Its elementary instructions conserve the rounded data energy and label
occupation defined below. This is a gate-by-gate contract, not an inference
from the completed word alone.

Use three interleaved tracks with `n` cells in one row:

    E_i at column 3i-2,   X_i at column 3i-1,   Z_i at column 3i,
    1 <= i <= n,         W=3n.                              (L1)

Every site is a physical qubit. The `E` track carries gap-`d` energy bits.
The `X` track is the one-hot spectral-label register. The `Z` track contains
the zero-energy finite information registers, logical labels, occupied
archive, readiness/work bits, control buses and new pointer.

Simultaneously diagonalize the finite `q_f,r_f`. Order the original label
states by their integer rounded charge, and insert filler labels only
for missing integers between successive original heights. Filler
residuals are zero; no occupied source label at height zero or `m` is
assumed. Place this active label chain starting at cell 6. Prefix padding
has the first active height and suffix padding the last active height,
both with residual zero. Thus the complete physical label track obeys

    0 <= j_i <= m,     j_(i+1)-j_i in {0,1},
    0 <= r_i <= d.                                         (L2)

The original labels retain their exact residual eigenvalues; this is not
an approximation of those onsite potentials. The compiler and input
contract identify the original labels, fillers and padding. A filler or
padding label is an admitted auxiliary state, not an additional original
spatial state.

Reserve `Z_1,...,Z_5` for the occupied archive and start the active
battery segment at `E_6`. Source and battery preparation route zero-energy
data and control buses only within the connected suffix `Z_6,...,Z_(n-1)`.
The archive is therefore untouched even during routing until its actual
writer. The writer may use `Z_1,...,Z_(n-1)`. The new pointer `Z_n` is
excluded throughout until the last CNOT. Padding the tracks this way
changes neither the site counts nor any local support bound.

For a nonnegative uniform label gap `mu`, define the one-row rounded
energy and residual by

    D_row = sum_i [d n_(E_i) + (mu+d j_i) n_(X_i)],
    R_row = sum_i r_i n_(X_i).                              (L3)

The actual selected bare label spectrum is `mu+d j_i+r_i`. The uniform
`mu` shift is separately counted; on the one-label input it adds one
constant offset to the original energy comparison. It may not be omitted
from the hardware energy or readiness accounting.

The circuit uses local copies of controls into zero-energy buses, not
energy-violating swaps between differently weighted label sites. A
neighboring upward label hop is funded by an energy bit and exchanges

    |1,0,1>_(X_i,X_(i+1),E) <-> |0,1,0>                 (L4)

when `j_(i+1)=j_i+1`. Equal-charge label hops require no energy change.
A zero-energy flag controlling (L4) gives four data qubits. Energy-track
swaps, zero-energy gates and bus operations use at most three. Each full
raw primitive preserves label number and (L3), including either value of
its controls. Invalid work or control values remain part of its unitary
extension.

The geometric compiler arranges each primitive in the following local
forms: a controlled funded hop within two neighboring cells; a copy
between an `E` or `X` site and a nearby `Z` bus; or a gate on at most
three consecutive `Z`-track positions. Same-type energy and zero-energy
routing is already included in the word. Consequently an ordinary
primitive uses at most three data qubits spanning six columns; a funded
controlled hop uses four data qubits within a smaller span. The physical
interaction never treats the whole apparatus as one cell.

Let `J` be the actual number of primitives after all routing, control
computation/uncomputation and archive exchange. Require the final
primitive to be the CNOT from the final acceptance flag to the new
pointer. Place those two logical factors in the penultimate and final
`Z` slots, at columns `W-3,W`, respectively. The pointer is excluded
from every earlier primitive and from routing. Earlier routes restore
the acceptance flag to its specified slot. Insert an identity primitive
before the final one if necessary so that `J` is odd. These choices
fix the endpoint layout before the autonomous evolution.

## 2. Row transport, clock path and exact counts

Use `J+1` data rows at heights `y=2t`, `0<=t<=J`. Every row repeats the
same column types, dimensions, `j_i` and `r_i`. To implement primitive
`t`, transfer row `t` to row `t+1` by separate vertical site SWAPs, in
alternating left-to-right and right-to-left order. A vertical SWAP joins
two copies with identical full onsite spectra and therefore preserves
both the rounded energy and residual sum.

For a primitive other than the last pointer write, apply the primitive
to the destination operands immediately after its last operand arrives.
It commutes with the remaining transfers, whose columns are outside its
support. Thus the entire stage equals the complete-row SWAP followed
by that primitive. Induction proves an exact operator identity:
the original row-zero factors, acted on by the programmed word, occupy
the final row, while the original other rows are permuted backwards.
The argument permits arbitrary contents and correlations in those other
rows. It does not infer that their unused registers are empty.

For the last primitive, first finish every vertical transfer and then
apply the flag-to-pointer CNOT on the final outward guard edge. Because
`J` is odd, this last sweep runs left to right. The flag and pointer at
`W-3,W` have both arrived. Delaying this one gate to the outward guard
makes its write occur at the exact completion index below, with no
post-write data transfer or routing.

Put the cursor rails at heights `2t+1`, `0<=t<J`, with sites at columns
`0,...,W+1`. Each rail has `W+1` horizontal edges. Join successive rails
by two vertical edges at their common outer column, with one cursor
site between the rails. Columns `0,W+1` lie outside the data rows.
An initial source at `(-1,1)` contributes one identity edge into the
first rail. The resulting primitive block has exactly

    b(J)=1+J(W+1)+2(J-1)=J(W+3)-1                       (L5)

edges. Column-transfer instructions occupy the first `W` edges of each
rail; its final edge is the outward guard.

Choose integers

    L_c >= max{b(J),512},    p=L_c-b(J),    K=2L_c.        (L6)

Extend the initial source line leftwards from `(-1,1)` to `(-p-1,1)`.
This inserts exactly `p` identity edges before the primitive block.
The final pointer flip now occurs at global history index `L_c`. From the
last outward guard append a straight rightward identity tail of `L_c`
edges, reaching history `K`. There is no subsequent data operation.
The lead-in lies left of the strip and the tail right of it. The rails,
outer connectors and padding are disjoint except at their consecutive
path vertices.

The exact site count and complete raw dimension are

    N_data=3n(J+1),       N_cursor=K+1,
    N_sites=3n(J+1)+K+1,
    dim H_raw=2^[3n(J+1)+K+1].                            (L7)

A containing integer rectangle has width at most `W+K+3` and height
`2J+1`. These counts include every row copy, bus, label padding site,
energy bit, pointer copy, and all zero- and multiple-cursor states.

## 3. Geometric support and degree

A vertical transfer uses two data sites. If it is combined with a
four-site primitive, the last-arriving destination site is already one
of the four operands; its old source adds only one further data site.
Hence every scheduled data instruction uses at most five sites. Its
propagation term also uses two neighboring cursor sites, giving at most
seven physical qubits.

For a controlled funded hop the operands occupy two neighboring cells,
so adding the source above the last operand and the two rail endpoints
fits in a Manhattan-radius-four ball. For an ordinary primitive the
widest case is three `Z` sites in consecutive cells, spanning six
columns. The destination data row and its old source row lie one unit
above and below the intervening rail. Center a ball at the middle
column on that rail: all data operands are at distance at most four.
The adjacent rail edge may extend one column past the last operand and
is still at distance at most four. Reversing the sweep reflects this
argument. The last guard CNOT, identity padding and vertical cursor
connectors use smaller supports.

A data site participates in at most its incoming and outgoing row
transfers and the one primitive belonging to that row. A cursor site
belongs to at most two edge terms. Potentials and bare terms are onsite.
Counting all other sites in these supports gives the conservative bound
of 64 interacting neighbors per physical site. Neither this degree bound
nor the seven-site support bound hides a growing local Hilbert dimension:
every site is two dimensional.

## 4. One positive law on all raw states

Let `H_D` be the sum of (L3)'s rounded `D_row` over every row. Let `G_j`
be the scheduled complete data instruction on path edge `j`; identities
fill the lead-in, guards not otherwise used, and tail. Every `G_j`
commutes with `H_D` and with total label occupation `N_X`.

For a cursor gap `kappa>=0` and `g>0`, define

    N_C=sum_(j=0)^K n_j,
    a_j=(g/(K+1))sqrt((j+1)(K-j)),  0<=j<K,
    a_(-1)=a_K=0,      v_j=g-a_(j-1)-a_j>=0,
    H_0=H_D+kappa N_C,                                    (L8)

    h_j=a_j[(n_j+n_(j+1))I
         -s_(j+1)^+ s_j^- G_j-s_j^+ s_(j+1)^- G_j^*],
    H_prop=sum_(j=0)^(K-1) h_j+sum_(j=0)^K v_j n_j,
    H=H_0+H_prop.                                          (L9)

The inequality `v_j>=0` follows from `a_j<=g/2`. On cursor blocks `00`,
`11` and `span{10,01}`, an edge term is respectively zero, `2a_j I`,
and `a_j [[I,-G_j^*],[-G_j,I]]`, up to the basis ordering. The last
matrix is positive because `G_j` is unitary. Therefore on the entire
raw space,

    H>=0,       [H_0,H_prop]=0,       [H,N_C]=[H,N_X]=0.    (L10)

In particular an incorrectly occupied clock follows the same positive
Hamiltonian; it is not projected into a legal clock code. Several
cursor excitations can trigger other data histories, which remain in
the full evolution. No correctness claim for their program order is
needed to prove positivity or (L10).

The onsite data capacity and an inclusive operator bound are

    C_D=(J+1)[n d+sum_i(mu+d j_i)]
         <=(J+1)n[mu+(m+1)d],
    0<=H<=[C_D+kappa(K+1)+(K+1)g]I.                       (L11)

Here `2 sum_j a_j+sum_j v_j=(K+1)g`. All row copies contribute to `C_D`.
Every edge has norm at most `g`; the only additional terms are the
counted onsite potentials and bare energies.

## 5. Original-energy comparison and the local correction

Put

    R=sum_(rows t,i) r_i n_(X_i,t),
    E_phys=H_0+R,       H_int=H_prop-R,
    H=E_phys+H_int.                                       (L12)

This is the actual decomposition when the bare label spectrum is
`mu+d j_i+r_i`. The compensating `-R` is onsite. It is not a hidden
global operator, and it cannot be dropped while retaining the same law.
The complete `H` is positive although `H_int` need not be.

Since `0<=R<=d N_X` and `N_X` is conserved, for every real `t`, with
`Z_t=exp(-itH/hbar)`,

    Z_t^* H_0 Z_t=H_0,
    -d N_X <= Z_t^* E_phys Z_t-E_phys <= d N_X.             (L13)

This is a full-raw operator inequality. It holds for every preparation,
including correlated rows and defective clocks. On a declared initial
state with total `N_X=1`, the original bare-energy drift is at most `d`
at every time and between any two times. On a general input the mean
drift is bounded by `d <N_X>`, using its actual conserved expectation.
Initial label defects cannot be ignored because they are unlikely.

On the correctly encoded original source and completed-output states,
the weighted original labels reproduce the compressed original energy
from FINITE_MODEL.md, together with the explicit battery, row, label-gap
and clock contributions. Filler labels and other raw configurations
are additional hardware states. Intermediate compiler states are
governed by the definite extension (L12), not asserted to be an unchanged
original spatial trajectory. The drift estimate is unconditioned;
selection of an accepted subensemble may reweight its initial energy.

## 6. Required readiness and the record-only window

For the exact history comparison, the initial cursor is one excitation
at the start of the lead-in and vacuum at every other cursor site.
The input/data resource contract must also supply the following:

- the encoded active input and all circuit scratch readiness in row zero;
- total one label excitation in row zero and label vacuum in every other
  row, when the unit-drift form of (L13) is used;
- zero in the physical new-pointer column of every data row;
- the specified finite battery and any preparation/source/control
  resources, with all other row contents and their energies retained.

These are additional state conditions on all the counted copies. The
algebraic row-transport identity alone does not prepare them. The
companion resource analysis must either construct them within its stated
scope or retain them as supplied resources with a quantified error.
In particular this note does not call the one-excitation cursor a Gibbs
state prepared by its own yet-unstarted circuit.

Let `F_0=I` and `F_j=G_(j-1)...G_0`. On the one-cursor sector the history
isometry maps `|j> tensor |psi>` to `|j> tensor F_j|psi>`, giving

    H_prop ~= gI-2g J_x/(K+1),
    p_j(t)=binom(K,j) sin^(2j)(theta) cos^[2(K-j)](theta),
    theta=gt/[hbar(K+1)].                                 (L14)

This is exact for arbitrary admitted data/reference states, including
coherence between rounded energies. Because of (L10), the free factor
is `exp(-itH_0/hbar)`. It acts on energy, label and cursor factors but
not on zero-energy logical/archive/pointer factors. Its action therefore
disappears after tracing those charged factors when comparing the
record. No assumption of a stationary source or battery is made here.

Every prefix before index `L_c` leaves the actual final-row pointer zero:
its original copy was zero, all incoming copies were zero, and no
earlier gate targets it. The index-`L_c` guard writes it after the whole
final row arrives. Every later prefix is identical on all data. If
`Sigma` is the subnormalized accepted archive/reference output of the
complete compiled word, then the physical final-pointer read gives
exactly

    sigma_rec,acc(t)=w(t) Sigma,
    w(t)=Pr[X>=L_c],     X~Bin(2L_c,sin^2 theta).          (L15)

No clock projector appears in this instrument. The old archive contents
are retained by the compiled exchange. The binomial notation denotes
coherent squared norms, not an occurrence process. All rejected source
branches remain in the complete state and the complementary pointer
output.

For `theta in [pi/3,2pi/3]`, Markov's inequality applied to `3^(-X)` gives

    1-w(t)<=3^(L_c)(1-2 sin^2(theta)/3)^(2L_c)
           <=(3/4)^(L_c) < 2^-128.                       (L16)

The last inequality follows from `L_c>=512` and `(3/4)^4<1/2`.
The normalized accepted record is exactly `Sigma/Tr Sigma` whenever
`w>0`; the incomplete-tail factor does not change its conditional state.
Before conditioning, the complete reduced record differs from its
completed-word value by at most `1-w` in trace distance.

For any prescribed finite duration `T_h>0`, select before evolution

    g=pi hbar(K+1)/(3T_h).                                (L17)

Then (L15)-(L16) hold at every time in `[T_h,2T_h]`. The exact endpoint
is `tau=3T_h/2`. This is a new window of the compiled Hamiltonian, not
the old 65-state clock's unchanged trajectory.

The inherited battery and preparation errors must be applied to the
completed-word comparison before asserting numerical success bounds.
For example, if its ideal accepted weight is at least `p_*` and its
accepted-plus-reject comparison error is `epsilon<p_*`, then

    p_rec >= w(t)(p_*-epsilon),
    D(rho_rec,acc,rho_ideal,acc)<=epsilon/p_* .             (L18)

An additional reference-uniform error `zeta` in the complete declared
new readiness changes the probability by at most `zeta` and adds at
most `zeta/[w(t) Tr Sigma]` to the conditional comparison, when this
denominator exceeds `zeta`. Defective pointer or clock states may
produce false acceptance and are included in this bound. These
estimates are not a derivation of the required input accuracy.

## 7. Complete energy moments and coupling cost

For data independent of an exactly ready one-cursor input, let
`mu_D=<H_D>` and `nu_D=Var(H_D)` include all initial rows and covariances.
The exact full-generator moments are

    <H>=mu_D+kappa+g,
    Var(H)=nu_D+g^2 K/(K+1)^2.                            (L19)

The diagonal propagation term is `g N_C`; every hopping expectation is
zero in the ready clock. Only a hop on the first edge and its return
contributes to the initial squared hopping term, and its data unitaries
cancel. This proves (L19) without discarding mixed or coherent data energy.
The physical bare mean instead contains `<R>`; its difference from the
full-generator mean includes the actual `-R` interaction correction.

For the explicit product input of PREPARATION.md, let `M` denote its
number of coherent preparation qubits, not the clock length `L_c`.
The same `N=M+2m` energy qubits contain `m` supplied excited bits, `M`
specified-phase plus states and `m` ground bits. Let the sharp source
label have rounded charge `j_*` and residual `r_*`. If all other energy
and label copies are vacuum and the cursor is exactly ready, then

    mu_D=d(m+M/2+j_*)+mu,      nu_D=d^2 M/4,
    <H>=d(m+M/2+j_*)+mu+kappa+g,
    Var(H)=d^2 M/4+g^2 K/(K+1)^2.                         (L19a)

The actual initial bare energy includes `r_*` in place of the propagation
contribution `g`. The coherent input state on those `M` qubits is
transported by the explicit row SWAPs through `C` and the subsequent
battery use; no second coherent bank is supplied. All added row and
clock vacuum states remain physical preparation requirements, even when
their initial energy is zero. The unknown logical and occupied-archive
inputs are on the declared degenerate information track.

For independent data and a product of diagonal cursor bits with occupation
probabilities `p_j`, the inclusive formulas are

    <H>=mu_D+(kappa+g)sum_j p_j,
    Var(H)=nu_D+(kappa+g)^2 sum_j p_j(1-p_j)
       +sum_(j=0)^(K-1) a_j^2
          [p_j(1-p_(j+1))+(1-p_j)p_(j+1)].                (L20)

These retain every vacuum and multiple-cursor configuration. For
correlated readiness use the actual full expectations of `H,H^2` rather
than (L20). The finite operator capacity (L11) is available for such
estimates. Neither small defect weight nor degenerate information energy
removes a resource from the dimension, entropy or preparation account.

There are `n(J+1)` label sites. A trace-distance readiness bound `zeta`
alone permits the conservative estimate
`<N_X>_actual<=1+zeta n(J+1)` relative to an ideal one-label input.
The size factor matters in (L13); an enormous row bank cannot be dropped
from its mean-energy defect budget. Direct population estimates may be
sharper and should be used when the resource preparation supplies them.

At fixed local coupling scale `g`, the window duration and acquisition
latency grow with `K+1`. Holding `T_h` fixed while increasing the compiled
word instead requires the larger `g` in (L17); each propagation edge can
then have norm up to `g`. This construction does not execute an
arbitrarily long local computation at unchanged interaction strength
and unchanged time. The onsite gaps, exact funded rotations, row
architecture, timing calibration and coupling precision are specified
resources, not experimentally established hardware.

## 8. Reversal and the scope of completion

On the entire one-cursor history, at `2tau=3T_h`,

    exp(-i 2tau H_prop/hbar)
       ~= exp[-i pi(K+1)] exp(i 2pi J_x)=-I.              (L21)

The subsequent free `H_0` action is the identity on every zero-energy
information factor. Consequently the archive/pointer/reference marginal
returns to its initial value, although charged-source free phases need
not return. The new pointer is again zero. The Hamiltonian therefore
has a finite record window, not an absorbing halt or permanent archive.

The pointer instrument is a specified local read of a physical qubit.
It supplies neither a material readout coupling nor a law selecting an
individual observed outcome. The theorem describes unmeasured evolution;
an inserted measurement or a detached archive changes its continuation
contract and requires a separate proof.

The result supplies a full-raw positive local autonomous realization
conditional on the declared complete conserving circuit and readiness
contract. It counts all row copies, keeps the residual-energy correction
onsite, and separates the exact rounded account from the bounded drift
of the prescribed physical reading. It does not by itself produce its
initial pure clock, source coherence, empty copies, or scratch states.
No new scientific executable, expanded circuit or numerical simulation
was run, and no Canon status is changed.
