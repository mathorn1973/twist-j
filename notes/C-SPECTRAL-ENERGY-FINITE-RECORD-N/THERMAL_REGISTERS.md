# Thermal preparation of the zero-energy registers

**NON-CANONICAL, L1. Conditional analytical candidate; independent
mathematical acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1767. This additional note changes none of the twelve
preceding candidate files.

This note supplies an explicit finite thermal reset circuit and a local
layout for its autonomous prefix. Every reset uses two physical Gibbs
qubits and a complete three-qubit unitary. No pure scratch, work ladder,
refreshed bath or externally timed reset is required by that prefix. Its
timing still requires the separately specified thermal launch and complete
history Hamiltonian. A scheduled list of reset gates alone is not that
autonomous construction.

The contract here prepares the zero-energy basis-ready registers. The
logical input, old memory and occupied archive remain arbitrary and can
be correlated with a reference. The charged source is created by the
launch, not by these resets. The cold-vacuum battery alternative retains
the narrower record/reference and commuting-effect contract; it does not
restore the earlier full source/battery product-state approximation.

## 1. Parameters and the two-temperature input

Use the three-track finite circuit of LOCALITY.md. One row has n cells
and W=3n data qubits. Its E qubits have gap d>0; its X qubits have physical
gaps d(1+j_i)+r_i, with 0<=r_i<=d. Its Z qubits have gap zero. Thus every
charged data qubit has gap at least d. These are complete physical qubits,
including padding and invalid computational configurations.

Let I be the nominated Z sites requiring a specified basis value, let
M=|I|, and write that value as ready_i. The other basis value is bad_i.
For the displayed finite model,

    M=n-15,                                             (T1)

when every Z site except the three five-qubit blocks for the logical
label, old memory and occupied archive is initialized. This includes the
new pointer, information-register blanks and the entire compiler scratch
and routing workspace. Those fifteen untouched bits retain their stated
valid-code input promise; they are not described as Gibbs inputs. An
additional preserved register changes M and must be counted explicitly.

For each i in I and each reset round t=1,...,r, introduce a distinct hot
qubit H_(i,t) and cold qubit C_(i,t). Both have physical gap d. Initially
their states are independent Gibbs states with excited probabilities

    p=1/(1+exp(beta_h d)),
    gamma=1/(1+exp(beta_c d)).                            (T2)

Use 0<gamma<1/2 and 1/3<=p<1/2. The same beta_h and beta_c can serve the
thermal launch. For example, if its actual hot-fuel gap is G+r_*>=d,
choosing beta_h(G+r_*)=log(2) gives launch excitation probability 1/3
and the bound p>=1/3. The actual fuel residual r_* is included in that
temperature specification.

Initially each zero-gap Z hardware qubit is exactly I/2 at either
temperature. Low temperature does not make it ready. The charged data
copies, cold reset donors, controller qubits and other nominated cold
sites are in their Gibbs states at beta_c. The hot fuel and the hot reset
donors have the common beta_h. There are no supplied pure hardware
factors in this thermal input. The admitted logical/memory/archive input
and its reference remain separate information resources.

## 2. A complete energy-conserving reset primitive

For target T with zero energy and the prescribed ready/bad basis, define
U_res by exchanging just the following two computational states:

    |1,0,bad>_(H,C,T)  <->  |0,1,ready>_(H,C,T),          (T3)

with identity on the other six basis states. This is a Hermitian unitary
on the full eight-dimensional physical space. Both exchanged states have
energy d, so

    [U_res,d(n_H+n_C)]=0.                               (T4)

The prescription covers ready=0 and ready=1. It requires no auxiliary
control bit and no initially empty target. In particular it is not an
unfunded complement of an energy-bearing qubit.

Let R be an arbitrary reference initially independent of the fresh donor
pair, while rho_TR may be arbitrary. Put

    a=p(1-gamma),   b=(1-p)gamma,
    lambda=1-a-b.                                      (T5)

Tracing the donor pair after (T3) gives exactly

    (Phi tensor id_R)(rho_TR)
      =lambda rho_TR
       +a |ready><ready| tensor rho_R
       +b |bad><bad| tensor rho_R.                     (T6)

To prove (T6), decompose the diagonal donor input into its four basis
sectors. Sector 10 implements replacement of T by ready and stores the
old target in the two-dimensional donor subspace spanned by 10 and 01.
Sector 01 implements replacement by bad. Sectors 00 and 11 act identically
on T. This argument includes off-diagonal target/reference terms. It is
not merely a population computation.

The donor output in this reduction is mathematically traced, but remains
physically present. In particular (T6) is not a claim that the changed
donors factor from the target or its original reference.

## 3. Finite repetition and reference-uniform error

Every repetition uses its own independent pair from (T2). The previously
used pairs are left untouched. Define the replacement channel R_tau and

    tau_*=(a |ready><ready|+b |bad><bad|)/(a+b).

Since a+b>0 and a replacement channel is idempotent, (T6) implies

    Phi^r=lambda^r id+(1-lambda^r)R_(tau_*).             (T7)

For the stated p,gamma, direct comparison gives

    0<=lambda<=2/3,
    b/(a+b)<=2 gamma/(1+gamma)<=2 gamma.                 (T8)

Indeed a+b=p+gamma-2p gamma is increasing in p for gamma<1/2, while
b/(a+b) is decreasing in p; substituting p=1/3 proves both bounds.
Thus, in trace-distance convention D=||.||_1/2, for arbitrary rho_TR,

    D((Phi^r tensor id_R)(rho_TR),
      |ready><ready| tensor rho_R)
       <=lambda^r+(1-lambda^r)b/(a+b)
       <=(2/3)^r+2 gamma.                              (T9)

The same inequality is uniform over reference dimension. Applying these
channels to M different targets, a telescoping comparison with the ideal
replacement channels gives

    D(rho_prepared, |ready_I><ready_I| tensor rho_R)
       <=M[(2/3)^r+2 gamma].                            (T10)

Here R contains the unreset input and its admitted reference. The changed
fresh donor banks are not included in the target comparison. All of them
remain in the full physical model. The reference-uniform channel bound
means that arbitrary old target/reference correlations are transferred
out of the targets without requiring an initially factorized target.

For the actual Gibbs zero-gap target, its initial bad probability is
x_0=1/2. More generally its population follows the exact recurrence

    x_(t+1)=lambda x_t+b,
    x_r=x_*+(x_0-x_*)lambda^r,
    x_*=b/(a+b).                                      (T11)

The linear error in (T9)-(T10) follows from the complete channel identity,
not from replacing a generic gentle-measurement square root by its square.

## 4. The all-cold-ground comparison used by the assembly

A particularly simple global budget compares the actual input with the
component on which every nominated positive-gap cold qubit is in its
ground state. Include every E/X data copy, every cold reset donor, every
cursor and loader, and all additional cold launch/safety sites. Do not
include the zero-gap Z sites in this comparison: their exact Gibbs state
is still I/2. Hot reset donors retain their actual Gibbs distribution.

Let C_c be the full number of those cold qubits and E_k>=d their actual
physical gaps. Their exact joint ground probability is

    q_c=product_(k=1)^C_c (1+exp(-beta_c E_k))^(-1),
    eta_c=1-q_c<=C_c exp(-beta_c d).                    (T12)

The actual input is exactly q_c rho_cold0+(1-q_c)rho_bad. Both components
evolve under the same complete Hamiltonian. This is a retained convex
decomposition, not a preparation by postselection. Initial independence
of these cold Gibbs factors from the admitted information is the resource
assumption used in (T12).

On rho_cold0 all reset cold donors are zero. Therefore b=0 and

    Phi^r=(1-p)^r id+[1-(1-p)^r]R_ready,
    xi<=M(1-p)^r<=M(2/3)^r.                            (T13)

The error eta_c already covers the actual nonzero cold-donor population;
the assembly need not add another 2M gamma to (T13). Formula (T10)
remains an independent direct bound when that global comparison is not
used.

There is a noncircular finite parameter choice. Fix an integer s>=1 and
M>=1, put u=ceil(log_2 M), and choose

    r=2(s+u+1).                                       (T14)

Because (2/3)^2=4/9<1/2, this gives xi<2^(-s-1). Fix the resulting finite
reset panel and main-clock geometry, count its actual C_c, and only then
choose beta_c so that

    beta_c d >= [s+1+ceil(log_2 C_c)] log(2).           (T15)

Then eta_c<=2^(-s-1), hence xi+eta_c<2^(-s). Enlarging the cold gap or
changing the gate count is not needed to satisfy (T15). The temperature
is selected after the physical site count. For M=0 omit the reset panel
and use xi=0.

The full read instrument must reject the dormant unlaunched component.
A zero-gap pointer alone cannot do this: before any successful launch it
is maximally mixed, and on a dormant branch it remains so. The autonomous
assembly must use its specified completed-tail/launch-sensitive read
predicate. Neither a zero initial dormant pointer nor a pure omitted
completion latch follows from (T13).

## 5. A local reset panel with arbitrary future-row contents

The reset gates admit a direct geometric prefix; a general matrix
compiler is unnecessary. Label the W original data columns by c=1,...,W.
For reset layers t=0,...,r, place their same-spectrum copies at

    T_(c,t)=(4c,2t).                                  (T16)

For each target column c in I and t>=1 place its hot donor at
(4c-1,2t) and cold donor at (4c+1,2t). The pairs are distinct at every
layer. Their gaps are all d. The first active row is t=0, and the last
reset row t=r becomes the first active row of the main compiler.

At layer t, transfer the active row from t-1 to t by separate vertical
SWAPs of corresponding data sites. Such copies have exactly the same
physical and rounded spectra. Immediately after transferring a reset
target, apply (T3) to its destination and its adjacent pair. The other
columns receive only their vertical SWAP. Use alternating sweep
directions on successive layers.

The gates for distinct columns have disjoint targets and donor pairs.
Each reset therefore commutes with all remaining transfers of other
columns. One completed layer is exactly a complete-row SWAP followed by
the product of its M reset gates. Induction shows that the original row-0
factors undergo the reset word and reach row r, while the original future
row contents are permuted backwards. This operator identity holds for
arbitrary future-row contents and correlations. It does not assume that
any future Z row is clean. The logical, memory and archive factors are
transported but never reset.

Put a unit-step cursor rail at height 2t-1, with outer columns 0 and
4(W+1)=4W+4. The right guard is beyond the last possible donor at 4W+1;
putting a vertical connector at 4W+1 would incorrectly collide with that
donor. Adjacent rails are joined at the alternating outer column by two
vertical edges and one intervening cursor site. Data rows and donor
stations do not intersect those outer connectors.

A transfer followed by its local reset acts on at most four data qubits:
the old target, new target, hot donor and cold donor. Its two cursor
endpoints fit with them in a Manhattan-radius-2 ball around
(4c,2t-1). Thus a reset propagation term uses at most six sites.
Unreset transfer terms are smaller. This support count concerns the
combined instruction, not a claim that its data unitary has three sites.

Each rail has 4W+4 horizontal edges. A block of k>=1 such sweeps, with
one initial source edge and two connector edges between successive rails,
has

    b_panel(k)=k(4W+6)-1                               (T17)

edges before additional padding or handoff edges. Identity instructions
fill rail positions not carrying a transfer. The clock labels order the
gates; no external gate schedule is part of the dynamics.

Continue the main compiler from row r, using the same horizontal scaling
by four and the same outer guard columns. Insert unit identity edges when
subdividing its former horizontal cursor edges. Scaling x coordinates by
four takes the previous Manhattan-radius-4 bound to at most radius 16;
the main term still has at most seven sites. These are uniform bounds,
independent of M,r and the main word length. All sites remain qubits and
each site participates in a bounded number of local terms. The detailed
launch, guarded handoff, potentials and history-window padding belong to
the complete autonomous construction.

For its final left-to-right sweep, that assembly pads the main word by an
identity if necessary so that r+J is odd. This is the parity of the new
combined construction, not an unchanged parity assumption imported from
the preceding main-only clock.

If the main compiler has J row-transfer stages, the combined reset and
main data bank has

    N_data=W(r+J+1),
    N_reset,hot=N_reset,cold=Mr.                       (T18)

The panel adds rW data copies and 2Mr donor qubits to the preceding main
data bank. In the complete thermal assembly let K denote its number of
physical cursor qubits, with its initial no-cursor vertex counted only
as a virtual history node. Its other added qubits are the hot launch
fuel, cold launch sink and cold completion latch. The exact total site
and cold-qubit inventories are then

    N_sites=3n(r+J+1)+2Mr+K+3,
    C_c=2n(r+J+1)+Mr+K+2.                             (T19)

The full raw Hilbert dimension is 2^(N_sites). Every controller and
additional charged cold launch/safety site is included exactly once.
Row-zero source and battery sites are already part of the first term and
must not be counted again. Zero-gap Z copies contribute dimensions and
entropy, although not to the cold-ground event. Extra helper sites would
change these counts; none is implicit in (T19).

## 6. All donor energy, entropy and old-value records

For each reset collision let x be the target bad probability immediately
before it and put

    nu=a x-b(1-x)=x-x'.                                (T20)

The exact mean-energy changes are

    Delta E_H=-d nu,  Delta E_C=d nu,  Delta E_T=0.      (T21)

Thus the reset consumes the hot/cold population contrast and transfers
energy to its cold donor. It does not draw energy from a hidden work
ladder. For r repetitions the net transfer telescopes to d(x_0-x_r).
For the product zero-gap Gibbs targets, x_0=1/2 and the completed panel
has hot-to-cold transfer Md(1/2-x_r). This is the net completed-prefix
transfer, not the total energy initially supplied in its bank and not
an unconditional transfer at an arbitrary clock time.

The full initial donor bank has the exact moments and entropy

    <H_donors>_0=Mr d(p+gamma),
    Var(H_donors)_0=Mr d^2[p(1-p)+gamma(1-gamma)],
    S_donors(0)=Mr[h_2(p)+h_2(gamma)],                 (T22)

where h_2(x)=-x log x-(1-x)log(1-x). These are moments of the donor
bare Hamiltonian, not of the complete interacting generator. Unused
energy, population fluctuations and all correlated donor outputs remain
physical. Repetition does not reuse a refreshed pair.

Every additional full data row in (T18) is also retained. If its physical
gaps are e_c>=0 and it starts at beta_c, its mean energy and variance are

    mu_row=sum_c e_c/(1+exp(beta_c e_c)),
    v_row=sum_c e_c^2 exp(beta_c e_c)
                         /(1+exp(beta_c e_c))^2.       (T23)

Its entropy is sum_c h_2(1/(1+exp(beta_c e_c))). In particular every
zero-gap Z copy contributes log(2) even though its energy and variance
are zero. The r added data rows contribute r times these quantities.
The main rows, launch fuel, sink, clocks, interactions and reference
belong to the separate inclusive assembly account; they are not made
free by (T22)-(T23).

For initially independent reset targets T and their complete donor bank D,
unitarity gives

    Delta S_D=S_T(0)-S_T(final)+I(T:D)_final.           (T24)

On the stated product Gibbs target, S_T(0)=M log(2) and
S_T(final)=M h_2(x_r). The old target information and the new correlations
are retained in D. A comparison tracing D is not a physical entropy
deletion. No claim is made that (T21) is the minimum possible heat cost
or that the finite bank can be reused without restoration.

## 7. Original-energy and autonomous-interface boundaries

The reset gates touch only zero-energy data and equal-gap donors. They
preserve the complete rounded bare energy and label number on every raw
state. Vertical transfers preserve the complete physical onsite spectra.
They also preserve the label residual used in the original-energy
comparison. No X seed is pumped by this reset panel.

For the direct single-label launch, a consistent optional convention
assigns its fuel the same residual r_* as the created label. With

    C=N_X+n_fuel,     N_X counts X sites in every row,
    R_total=R_X+r_* n_fuel,                            (T25)

the launch and this panel preserve C, and 0<=R_total<=d C. The main
compiler preserves C as well. If the complete Hamiltonian preserves
the rounded H_0 and C, the all-raw-space inequality remains

    -d C<=U(t)^*E_phys U(t)-E_phys<=d C,
    |Delta <E_phys>|<=d<C>,
    E_phys=H_0+R_total.                               (T26)

This is the bounded residual statement, not exact conservation of the
unrounded original energy. The inclusive interaction then contains the
explicit counterterm -R_total when H=H_0+H_prop is written as physical
bare energy plus interaction. The actual fuel gap and its Gibbs state
must include r_* under this convention. This note does not mix it with
a different fuel spectrum or omit residual energy on bad thermal rows.

The thermal input is not a Gibbs state of the complete interacting
Hamiltonian. Its unequal temperatures and locally manufactured spectra
are supplied resources. A common Gibbs state of a conserved additive
H_0 would be stationary, as would a Gibbs state of the full H. A finite
full-rank closed state also cannot acquire an exactly pure nontrivial
marginal by a unitary. The finite errors in (T9), (T12) and (T13) respect
both boundaries.

The prefix becomes autonomous only after its instructions are inserted
into the specified positive history Hamiltonian, with the thermal
launch, guarded handoff and complete raw-space potentials. Its controller
vacuum is then supplied approximately by the counted cold Gibbs factors;
the launch creates the running excitation. This is what avoids using a
ready timer to prepare the same timer. No permanent record, bath reset,
manufacturing mechanism or selection of a realized outcome follows from
the reset circuit itself.

Decisive falsifiers include a failure of (T6) on an admitted reference,
an uncounted cold or hot donor, reusing a donor as if it were fresh, a
geometric collision or unsupported local gate in the panel, a neglected
future-row entropy contribution, a read predicate accepting the dormant
mixed pointer without its stated error, or omission of a residual term
from the original-energy comparison. No scientific executable, numerical
simulation or expanded gate list was run for this note.
