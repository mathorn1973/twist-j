# Thermal readiness for the sharp-fiber record: complete account

**NON-CANONICAL, L1. New conditional analytical candidate-T; independent
mathematical acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1767.

This continuation replaces the supplied pure clock, source seed and
auxiliary register bank of the local sharp-fiber construction by a finite
product of two-temperature Gibbs resources. Every physical site is a
qubit. The arbitrary logical input, occupied old memory and occupied
archive retain their reference correlations and are excluded from
cooling. The result is an approximate preparation and conditional record
theorem under one specified positive static Hamiltonian. It does not
assert equilibrium for that interacting Hamiltonian.

The input package is PR #1768 at
`7550a73d02fbb6a85d73b77e027671a42970ffbc`. All twelve earlier files are
unchanged. Independent mathematical PASS applies only to the older
seven-file revision `d13851796d5e7a316e1f628407e1bedef04f9bad`, as stated
in LOCAL_VALIDATION.md. Neither that review nor the same-session checks
accept this new extension.

[SHARP_THERMAL.md](SHARP_THERMAL.md) proves the restricted output contract,
[THERMAL_REGISTERS.md](THERMAL_REGISTERS.md) proves the thermal reset,
and [THERMAL_CLOCK.md](THERMAL_CLOCK.md) supplies the complete static
assembly. [THERMAL_VALIDATION.md](THERMAL_VALIDATION.md) gives its review
contract and integrity evidence.

## 1. The contract and its energy source

Let a,b be the minimum and maximum actual occupied rounded charges of
the finite source, v=b-a, and choose a common eigenvector x_* at charge b
with residual r_*, 0<=r_*<=d. Take N=max{1,v} gap-d battery qubits. The
extra qubit when v=0 is harmless counted padding. On the exact vacuum
input, the complete compensated word has exactly the ideal
archive/pointer/reference output and the specified commuting band
statistics. It requires no coherent battery and no charged buffer bank.
It generally leaves the source correlated with the battery rather than
preparing a standalone coherent spatial state.

The source seed is created by the actual launch. Set the label offset
mu=d and put G=(b+4)d. A fuel qubit h has rounded gap G and prescribed
physical gap G+r_*. Its resonant conversion is

    |h,c,X_*,C_1>=|1,0,0,0> <-> |0,1,1,1>.

Here the sink c has gap d, the chosen label site has gap (b+1)d+r_*,
and the first cursor has gap 2d. Both sides have physical energy G+r_*.
The label is subsequently transported through the preparation and
program rows. The fuel and sink remain in the apparatus.

The thermal fuel excitation has weight 1/3. Its ground branch, with
empty cold cursor sites, never starts the programmed history. No outer
pure timer is supplied. The construction therefore pays an explicit
factor 1/3 in throughput. Increasing this factor by changing fuel
degeneracy or using many launch sources would be another counted design.

## 2. A complete finite parameter list

Retain the finite source dimension s and information register count

    f=1638451=16+3*327681+655392.

The three arbitrary 26-state factors occupy 15 physical qubits; the
remaining factors include the final pointer. Sort the source eigenlabels
in descending rounded charge, with x_* first in the maximum-charge group,
and insert missing intermediate heights. Let ell<=s+v count this chain.
Its reflected local compiler has the same conserving support and count
proof as LOCALITY.md. Put

    B_size=ell+N+f,       n=16 B_size,       A=n-15.

There are n cells on each of the energy, label and zero-energy tracks.
A counts every zero-energy ready target in the active row, including
all padded scratch, flag and pointer bits. No arbitrary logical or
occupied-memory bit is reset. Choose each auxiliary basis encoding so
that its prescribed ready label is all zero; the finite target matrices
use that same encoding. This changes no physical zero-energy spectrum.

Choose the number of reset layers first:

    u=ceil(log_2 A)+104,       r=2u.

Because (2/3)^2=4/9<1/2, this ensures

    xi=A(2/3)^r<2^-104.                                (R1)

Let J be the actual routed primitive count for the compensated source
word and occupied-archive writer, including any required parity padding.
The conservative bound of LOCALITY.md still allows
J<=20000000 B_size^4 4^B_size. The preparation adds r data-row
transitions, so write T=r+J. The thermal clock construction chooses a
finite L_c at least its complete launch/preparation/program/latch path
length and at least 512, then sets K=2L_c. Index zero is the virtual
fuel state; indices 1,...,K are K physical cursor qubits.

The exact number of physical qubits is

    S=3n(T+1)+2Ar+K+3,       dim H_raw=2^S.             (R2)

The additional three sites are the launch fuel, its sink and the
completion latch. The 2Ar sites are all fresh hot/cold reset pairs.
All data copies, energy and label padding, cursor lead-ins and tails
are included. The geometry uses bounded-support interactions and fixed
site dimension; the precise support and geometric bounds are in
THERMAL_CLOCK.md. The finite circuit bound is extremely large and is
not an efficiency or manufacturability claim.

## 3. Actual initial states, without a pure auxiliary bank

Choose the two inverse temperatures by

    beta_h(G+r_*)=ln 2,
    B_c=ceil(log_2 C_c)+104,
    beta_c d=B_c ln 2,
    C_c=2n(T+1)+Ar+K+2.                                (R3)

C_c counts every positive-gap cold factor: all E/X data sites in every
row, every reset cold sink, all cursor sites, the launch sink and the
completion latch. There are Ar+1 hot factors: the reset donors and
the launch fuel. No dimension in (R2) depends on beta_c, so choosing
the cold temperature after constructing the finite geometry is not
a circular size prescription.

Every nonlogical factor is an independent Gibbs state for its stated
physical onsite spectrum. Hot reset donors and their cold sinks have
gap d. Their excitation probabilities are

    p=1/(1+exp(beta_h d))>=1/3,
    gamma=1/(1+exp(beta_c d))<z,       z=2^-B_c.

The fuel has excitation probability exactly 1/3. E bits have gap d;
X_i bits have gap d(1+j_i)+r_i; cursors before completion have gap 2d
and those at/after completion have gap d; the completion latch has
gap d. All those cold gaps are at least d. Zero-energy Z factors have
the genuine Gibbs state I/2. Only the original 15 information-input
qubits are replaced by their arbitrary admitted joint input/reference
state. Their information is not an expendable preparation resource.

Let q_c be the exact product of the cold ground-state probabilities,

    q_c=product_(cold sites i) [1+exp(-beta_c e_i)]^-1,
    eta_c=1-q_c<=sum_i exp(-beta_c e_i)<C_c z<=2^-104.   (R4)

The actual input decomposes as q_c times the all-cold-zero comparison
state plus its complete complementary thermal component. This is an
analysis of the mixed state, not a preparation postselection. The hot
fuel, hot reset donors, all dirty Z rows and arbitrary information input
retain their actual states in the comparison. Every thermal defect
evolves under the same raw Hamiltonian and may affect the output.

No pure auxiliary qubit, pure work store or inverted cursor input is
assumed. The input still supplies two different temperatures, specified
spectra and a product-state boundary condition relative to an already
specified interacting law. Their laboratory preparation is not derived
from a single equilibrium state or from the native TWIST-J update.

## 4. Cooling and the completion instrument

Each reset gate swaps only

    |H,C,Z>=|1,0,1> <-> |0,1,0>,

and fixes all other states. It conserves the actual bare energy because
H,C have equal gap d and Z has zero gap. With a fresh donor pair, the
reduced target/reference channel is a mixture of identity and two exact
replacement channels. THERMAL_REGISTERS.md gives its complete formula.
On the all-cold-zero comparison state, one hot excitation resets Z to
zero; later reset pairs keep it there. After r layers the joint error
for all A targets is at most xi in (R1), including the reference.

Every used pair is retained beside its row. Future Z rows may remain
maximally mixed: vertical same-spectrum exchanges transport the active
factors and permute the previous row contents. They do not reset that
junk. After the panel, the main word acts on the active prepared row
and leaves the donor records idle. Their correlations therefore do not
invalidate the reduced-state preparation bound.

A zero-energy pointer alone would falsely report one on half of the
dormant Gibbs-input branches. The new physical instrument instead reads

    Pi_read=n_L n_P,

where L is the additional gapped completion latch and P is the final
source-acceptance pointer. The latch is raised unconditionally only on
the completed history edge. That edge lowers the cursor gap from 2d
to d, paying the latch excitation d. Its partial-isometry coupling has
a positive entire-space completion. Rejected source histories also
raise L but have P=0 after correct preparation. Dormant histories have
L=0. No clock projector or discarded thermal sector is hidden in this
two-qubit read instrument.

## 5. Output bounds and reversal

Let p_0 be ideal source acceptance and Sigma_0 its accepted
archive/reference output. On exact cold readiness, completed histories
give the accepted map (1/3)w(t) Sigma, where Sigma is the actually cooled
completed-word output. The spin-chain tail obeys

    w(t)>=1-(3/4)^L_c>1-2^-128

throughout [T_h,2T_h], for g=pi hbar(K+1)/(3T_h). Tracing the history
removes cross-history terms. Every incomplete history has L=0, so the
clean conditional record pays no extra tail-normalization error.

Using the accepted-plus-rejected instrument and (R1),(R4),

    p_read,actual(t)>=(1/3)w(t)(p_0-xi)-eta_c,
    D(rho_actual,acc(t),rho_ideal,acc)
       <=xi/p_0+eta_c/[(1/3)w(t)(p_0-xi)].             (R5)

The comparison retains the admitted logical/occupied-memory/archive
reference scope. It includes false positives from the complete cold
defect component. There is no renewal of the battery or reset donors
between gates.

The source margins in FINITE_MODEL.md, namely
p_0>1/20000+1/1000000 and ideal unwanted weight
u_0<19/(20*1000000), imply

    p_read,actual(t)>1/60000,
    D(rho_actual,acc(t),rho_ideal,acc)<60000*2^-103,
    u_actual,acc(t)<1/1000000.                         (R6)

For the last bound apply the same joint comparison to A_bad and the
record. The source effect commutes with q_f; extend it by identity on
invalid source encodings. Commutation with r_f is not assumed. Initial
states commute with H_0, and the conserving evolution retains that
symmetry, so the free H_0 motion does not alter these statistics.
No material implementation of the generally nonlocal source effect is
supplied by its mathematical definition.

At 3T_h the entire clean active history reverses. The dormant component
has remained unchanged. In the all-cold-zero comparison state the latch
returns to zero, including unsuccessful reset histories; hence the
actual read probability at that time is at most eta_c. This is still
a finite record window, not permanent storage or a reusable successful
reset cycle.

## 6. Inclusive energy, entropy and defects

Let H_0 sum the rounded onsite energies, including every donor, row,
cursor, latch, launch fuel and sink. The actual static law and the
prescribed physical bare reading are

    H=H_0+H_prop,
    R_total=sum_(all X sites i) r_i n_i+r_* n_h,
    E_phys=H_0+R_total,
    H_int=H_prop-R_total.                              (R7)

The fuel residual is transferred to the source by the launch itself.
The counterterm, including its fuel contribution, remains an explicit
local part of the interaction. The complete H is positive and conserved.
The conserved occupation budget is

    C=N_X+n_h,       0<=R_total<=d C,

not N_X alone during source creation. Thus every raw state obeys

    -d C<=U_t^* E_phys U_t-E_phys<=d C.                 (R8)

For the actual thermal input,

    <C>=1/3+(T+1)sum_(i=1)^n [1+exp(beta_c e_Xi)]^-1
       <1/3+n(T+1)z<=1/3+2^-104.                     (R9)

The resulting mean-energy bound includes all multiple-label defects.
It is unconditioned and cannot be transferred to a selected successful
ensemble. There is no time accumulation. All other energetic costs
remain in H_0 and H_prop, rather than being erased by (R8).

If e_i^(0) and e_i are the rounded and physical onsite gaps and p_i
the actual supplied excitation probabilities, the initial onsite means
and variance are explicitly

    <H_0>=sum_i e_i^(0) p_i,
    Var(H_0)=sum_i (e_i^(0))^2 p_i(1-p_i),
    <E_phys>=sum_i e_i p_i.                            (R10)

The sums run over every hot and cold site in (R2); zero-energy input
registers contribute no energy. The launch contribution to <H_0> is
G/3, and its contribution to <E_phys> is (G+r_*)/3.
Every reset pair contributes d(p+gamma); all Ar pairs count, including
ones that do no useful reset. Every cursor and future row contributes
its actual thermal population. THERMAL_CLOCK.md gives exact complete-H
mean and variance, including the propagation and launch interaction,
and a finite raw operator-capacity bound. Onsite means alone are not
claimed to be the complete initial energy.

All zero-energy thermal factors contribute ln 2 entropy each. With
S_input the entropy of the admitted 15-qubit input marginal, the actual
apparatus input entropy is

    S_initial=S_input+[n(T+1)-15]ln 2
       +sum_(hot/cold sites i) h_2(p_i).               (R11)

For a logical reference, use its actual joint input entropy when
including it in the partition. No external purification of thermal
factors is assumed free or retained in the output theorem.

Each reset's net forward weight nu changes donor energies by
Delta E_H=-d nu and Delta E_C=d nu; target energy is zero. Every changed
donor and old value remains in the closed system. The full unitary
preserves entropy. For an initially independent target and resource
partition, the exact balance is

    Delta S_resources=S_target(0)-S_target(t)+I(target:resources)_t.

This includes correlations, not only separate marginal entropies.
Cooling does not restore the consumed temperature contrast. Resetting
the apparatus and its reservoirs for another successful use is a
different preparation problem.

## 7. Remaining physical assumptions and falsifiers

The supplied local Gibbs factors commute with the additive rounded
energy H_0 but are not equilibrium for the full H. The launch has a
strict forward/backward population imbalance. THERMAL_CLOCK.md gives
an explicit nonzero full-H commutator witness. No switching operation
is inserted into the evolution, and no initially occupied external
clock drives the reset panel. The product-state boundary condition,
two temperatures, spectra, geometry and exact couplings remain physical
inputs of this existence result.

A common Gibbs state of conserved H_0 is stationary, and a Gibbs state
of full H is stationary. Gibbs(E_phys) is a different statement because
of the interaction correction. These distinctions and the finite
full-rank obstruction to exact unconditional pure readiness are proved
in SHARP_THERMAL.md. The logical information input is not silently
treated as a full-rank thermal resource or used as a purity supply.

At fixed local interaction scale, acquisition time grows with K+1.
Fixing T_h instead requires the stated larger g. All exact gate angles,
very cold temperatures and large finite dimensions are specifications,
not demonstrated hardware tolerances. Original spatial confinement,
native derivation, material detection, lasting storage, renewal and
individual occurrence remain outside the result.

A failure of the raw launch invariant, the reset channel, the thermal
count or error bound, the completed read instrument, or the sharp-fiber
trace identity invalidates its corresponding claim. No scientific
executable, expanded matrix, simulation or experiment was performed.
The new material is handed to independent review; Canon is unchanged.
