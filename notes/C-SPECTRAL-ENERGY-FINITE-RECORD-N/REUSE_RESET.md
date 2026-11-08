# Exact cartridge reset and the resources for repeated use

**NON-CANONICAL, L1. Conditional analytical extension; independent
mathematical acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1767. The seventeen preceding files at
`485f907531ab329b3aabc08d0a1bf594ae987c80` are unchanged.

An identical-spectrum cartridge permits an exact reset by a complete
SWAP. The old state, its entropy and all reference correlations move into
the spent cartridge. They are not erased. This gives an exact finite-use
channel identity and an explicit stock requirement for every attempt,
including rejected and dormant attempts. It does not supply free
regeneration of that stock.

The endpoint identities below can be used either by an explicitly
switched apparatus or by a finite outer history. Their physical control
contracts differ. Isolation after export can retain the record in the
switched model. A finite reversible outer history has its own later
return and does not establish permanent autonomous storage.

## 1. Typed core, protected output and next information input

Let D be the S-qubit core of THERMAL_RESOURCES.md and THERMAL_CLOCK.md.
Write

    D=T tensor I,           dim I=2^15,                (U1)

where I is the fifteen fixed physical row-zero input sites containing
the admitted logical label, old memory and occupied archive blocks, and
T contains every remaining physical core qubit.
The input on I has its earlier valid-code promise and may be entangled
with any passive reference R. It is not a thermal or expendable purity
resource. Every thermal hardware factor in T is included: hot fuel and
reset donors, cold energy/label copies, cursor, sink, latch, and all
zero-gap mixed auxiliaries.

Let Omega_T be exactly the product of those physical onsite Gibbs states
at the two specified temperatures. It is full rank. It is not a Gibbs
state of the complete interacting core Hamiltonian. A next-use package
consists of fresh hardware Omega_T and a new admitted information input.

The exported block is

    B=A tensor P tensor L,        dim B=2^7,           (U2)

with five raw archive qubits and the pointer in the final physical data
row, together with the separately located completion latch. These output
sites belong to T in the initial physical partition. Transport of an
abstract information factor from row zero does not identify its input
site with its later output site. Its physical bare Hamiltonian is
E_B=d n_L; the other six gaps are zero. Each output slot O_j has the same
seven physical spectra. Its initial contents may be mixed or occupied.
No blank state is required by a SWAP. For the product-stock formulas
below the slots start independently of the input packages; their old
states are retained after export.

The passive reference excludes the destination slots themselves, but
may include purifying references for admitted information. It is not
consistent to designate the same subsystem both as an overwritten
destination and as an unchanged passive reference.

## 2. Exact export and complete-core replacement

For any complete core/output/reference density, a SWAP of B with O
relabels the old core block as the new output. In particular

    Tr_(D)[SWAP_(B,O)(rho_DR tensor zeta_O)SWAP_(B,O)^*]
      =rho_(B,R), with B relabelled O.                 (U3)

The remaining core contains the old output contents, including their
entropy. This identity preserves the joint quantum record/reference
state. It is not a measurement or a cloning map. A distinct outcome
selection rule is not supplied by (U3).

Next let F be a full S-qubit cartridge with identical site spectra. If
its complete input were a fixed state omega_F independent of D,R, then

    SWAP_(D,F)(rho_DR tensor omega_F)SWAP_(D,F)^*
       =omega_D tensor rho_FR.                       (U4)

This is exact for arbitrary rho_DR, including every failure branch.
The output D is independent of the spent cartridge and reference; all
old D:R correlations are now F:R correlations. The trace-distance error
of this replacement channel is zero on the complete raw space.

For a next information input the correct statement is more general.
Let F=T_F tensor I_F, and let chi_(D,I_F,R) be arbitrary while the fresh
hardware is independent Omega_(T_F). The same full SWAP gives

    Omega_(T_D) tensor chi_(F,I_D,R),                  (U5)

with the displayed relabelling of the old D and the new information
input. Thus thermal hardware is exactly reset and independent of all
other retained systems. The next input I_D may remain correlated with
earlier records or R. Calling the entire D a Gibbs state, or calling
that next input independent, would exceed (U5).

The spent F includes all old core degrees of freedom, including the old
output contents inserted by (U3). No register is restored by deleting
its old value. Exact replacement by a full-rank mixed thermal state
also does not contradict the earlier obstruction to producing an
exactly pure nontrivial marginal from finite full-rank closed inputs.

## 3. A reference-uniform N-use channel identity

Put U=exp(-i tau H_D/hbar), where H_D is the previously specified complete
core generator and tau=3T_h/2 is its exact active completion time. Define
the complete one-use output channel

    E(sigma_I)=Tr_(D\B)[U(Omega_T tensor sigma_I)U^*]. (U6)

This is the actual thermal channel, including its dormant, rejected and
defective components. It is not only its accepted branch. Its output is
the complete seven-qubit block and its action is extended by identity
on any passive reference.

Supply N fresh S-qubit cartridges F_1,...,F_N, in addition to the first
core D. The thermal hardware in all N+1 packages is independent
Omega_T. Their information inputs I_0,...,I_N can have an arbitrary joint
state rho_(I_0,...,I_N,R). Supply N independent occupied output slots.
For j=1,...,N execute the three complete endpoint operations

    U on D;
    SWAP_(B_D,O_j);
    SWAP_(D,F_j).                                     (U7)

The last step is unconditional. It is performed after a rejected or
dormant attempt as well as after an accepted one. The final cartridge
prepares the core for use N+1, so its fifteen next-input qubits are
explicitly included even if that next use is not performed.

After the complete word, trace the spent cartridges but keep the core,
all output slots and R. Equations (U3)-(U5), applied successively, give
the exact identity

    rho_(D,O_1,...,O_N,R)
      =Omega_(T_D) tensor
        (E^tensor N tensor id_(I_N,R))
                          (rho_(I_0,...,I_N,R)),       (U8)

with the information and output factors ordered as indicated. Each copy
of E acts on one input I_(j-1). No independence between those information
inputs is used. The old output states and all used hardware remain in
the traced physical cartridges. Equation (U8) therefore does not assert
a factorization of the outputs from the waste.

In particular the hardware factor is exactly fresh even after
conditioning on any event on the output tape with positive probability.
The next information input may change conditionally through its original
correlations; this is not a failure of reset. Conditioning does not
retroactively make the consumed cartridges or rejected attempts free.

The statement adds no approximation to the one-use channel. Its thermal
error and accepted-state bounds remain those of that channel. If complete
one-use channels have a reference-uniform error epsilon relative to a
specified comparison, telescoping gives at most N epsilon for their
complete retained N-use output. Normalizing a selected multi-use event
then requires its own success denominator. An N-fold conditional fidelity
claim does not follow merely by adding normalized one-use errors.

If every admitted conditional next input has one-use acceptance at least
p_min, the fixed N-use protocol has expected accepted count at least
N p_min and probability of no acceptance at most (1-p_min)^N. This uses
the chain rule and the same uniform bound on each conditional input,
not independence of the information or an uncounted repeat-until-success
controller.

## 4. Stock, entropy and correlations consumed by a reset

For N uses followed by the final exact reset, the core, cartridge and
output stock contains

    N_stock=(N+1)S+7N qubits.                          (U9)

There are N+1 admitted fifteen-qubit information inputs, one in every
core-sized package. These factors are already counted in (U9). A passive
external reference is not part of the apparatus dimension. To stop
after use N without a final reset requires only N-1 replacement
cartridges; it does not leave the core ready for another use.

Every component of Omega_T is replicated N+1 times. If its physical bare
mean, variance and entropy are e_Omega, v_Omega and S_Omega, the initial
thermal hardware stock contributes

    (N+1)e_Omega,    (N+1)v_Omega,    (N+1)S_Omega.     (U10)

The information factors have zero bare energy, but their actual joint
entropy and reference correlations are additional information resources.
The output stock contributes its actual energy, variance and entropy.
For independent Gibbs slots at beta_c these are, with
gamma=(1+exp(beta_c d))^(-1),

    <E_outputs>=N d gamma,
    Var(E_outputs)=N d^2 gamma(1-gamma),
    S_outputs=N[6 log(2)+h_2(gamma)].                 (U11)

For other occupied slot states use their actual moments, including any
declared covariances. Initial slot purity is not needed for (U3) or (U8).
Cold Gibbs preparation of a latch is a thermal resource, not a free
perfectly zero latch.

For the simple full replacement (U4), the exact entropy and mutual
information transfers are

    Delta S_F=S(rho_D)-S(omega_F),
    I(F:R)_after=I(D:R)_before.                       (U12)

The old core can have the same marginal entropy as its replacement and
still carry substantial reference information. For example an initially
maximally entangled D:R pair transfers that entanglement to F:R under
(U4). A zero marginal-entropy change does not mean that the cartridge
is unchanged or available for free reuse.

For (U5) apply the same relabelling to the complete joint input instead
of pretending that the next information input was independent. Used
cartridges must retain their correlations with the tape, future inputs
and R. Replacing them by an uncorrelated thermal description would be
an additional irreversible operation requiring its own environment.

## 5. An exact Gibbs cost identity with the correct subsystem

Restrict this identity to the thermal hardware T of a fresh cartridge.
Write its full-rank reference state as

    Omega_T=tensor_i exp(-beta_i E_i)/Z_i,

including zero-gap factors I/2. Let sigma_T be the actual spent-hardware
marginal after the SWAP, and define the deposited energy at site i by

    Q_i=Tr[E_i(sigma_T-Omega_T)].

The definition of quantum relative entropy gives the exact identity

    sum_i beta_i Q_i
      =S(sigma_T)-S(Omega_T)+D(sigma_T||Omega_T).        (U13)

Indeed -log Omega_T=sum_i beta_i E_i+sum_i log Z_i,
and S(Omega_T)=sum_i beta_i Tr(E_i Omega_T)+sum_i log Z_i.
Substitution proves (U13), with all internal correlations of sigma_T
retained in its relative entropy. The next-input fifteen qubits are
separate nonthermal information resources and are not included in this
Gibbs formula. Correlations between T and those information factors or
the protected tape are also retained; (U13) does not declare them zero.

For comparison, let a system A and a finite reservoir B initially have
the product state rho_A tensor tau_B, where tau_B is Gibbs at inverse
temperature beta for H_B. For a complete unitary on AB, put
Q=Tr[H_B(rho_B'-tau_B)]. Entropy conservation and the same logarithm
identity give

    beta Q=S(rho_A)-S(rho_A')
           +I(A:B)'+D(rho_B'||tau_B).                 (U14)

If A initially has a passive reference R and the reservoir is independent
of AR, the equally exact conditional-entropy form is

    beta Q=S(A|R)_in-S(A|R)_out
           +I(B:AR)'+D(rho_B'||tau_B).                (U15)

Here the unitary acts only on AB and R is unchanged. To obtain (U15),
use S(ARB)_in=S(AR)_in+S(tau_B) and express the final total entropy by
S(AR)_out+S(B)_out-I(B:AR)'. Neither formula assumes a new pure blank.
The standard finite-reservoir context is
[Reeb and Wolf, New Journal of Physics 16 (2014) 103011](https://doi.org/10.1088/1367-2630/16/10/103011),
also available as [arXiv:1306.4352v3](https://arxiv.org/abs/1306.4352v3).
The equalities used here have been derived above.

These are reservoir-energy identities, not universal work formulas.
Adding a work store or a controller changes the entropy and correlation
account unless its endpoint properties are explicitly imposed. Restoring
a mixed Gibbs hardware state is not erasing S pure classical bits, and
there is no justified universal k_B T log(2) cost per physical qubit in
this protocol. Regenerating the spent two-temperature stock requires a
new specified operation and reservoirs. It is not performed by (U7).

## 6. Exact local SWAP pulses and the switching account

Equal-spectrum corresponding sites permit export and replacement on
every raw state. Let E be the summed physical onsite energy of the paired
systems, and let S_k be their corresponding one-qubit SWAPs. They commute
with E and with one another. With m such pairs define the positive pulse

    H_swap=lambda sum_(k=1)^m (I-S_k),
    lambda delta/hbar=pi/2.                           (U16)

During an idle interval with this pulse,

    exp[-i delta(E+H_swap)/hbar]
      =exp(-i delta E/hbar) product_k S_k.             (U17)

Each pair interaction has two sites. There are seven pairs for export
and S pairs for full-core replacement. The equality needs no one-label
promise, clean scratch or generic compiler. A local geometric placement
requires corresponding sites to be adjacent, for example in matching
parallel layers. Bringing successive cartridges and output slots into
that placement requires declared routing or transport; it is not an
implicit free operation in (U16).

The free physical-energy factor in (U17) is explicit. Fresh hardware
Omega_T commutes with its onsite energy, and I has zero energy, so the
reset state itself remains exactly the intended package. The spent state
may undergo its known free evolution. On an isolated output,

    E_O=d n_L,    Pi_O=n_L n_P,    [E_O,Pi_O]=0.        (U18)

The entire output is retained up to this known free evolution. On the
accepted subspace E_O=d I, so the accepted archive/reference density is
unchanged for arbitrarily long time under exact isolation. This is a
storage statement of the isolated-output model, not of a fixed coupled
writer which later reverses its export.

An additive-energy SWAP need not commute with the active core interaction.
For a direct switched realization, set

    E_D=H_(0,D)+R_D,
    V_D=H_(prop,D)-R_D,
    H_D=E_D+V_D.                                      (U19)

Idle cartridges and outputs have only their physical onsite Hamiltonians.
Turn on V_D for the intended core run, turn it off at tau, then perform
export and replacement with (U16). All old hardware, input values and
destination contents are retained as above. Turn on the same V_D on the
fresh package for the next attempt. The idle, run and SWAP Hamiltonians
are each positive. An interpolation E_D+u V_D with 0<=u<=1 is positive
as a convex combination, but a finite-duration ramp changes the exact
gate and must be modeled rather than silently identified with a quench.

For ideal quenches and the actual run states rho_0,rho_tau, mean control
work delivered to the modeled systems is

    W_on=Tr(V_D rho_0),
    W_off=-Tr(V_D rho_tau),
    W_run=W_on+W_off
         =Tr[E_D(rho_tau-rho_0)].                     (U20)

The last equality uses conservation of the complete H_D during the run.
The previous residual bound therefore gives

    |W_run|<=d<C>_(rho_0).                            (U21)

This is an unconditioned mean for all branches, not a small-work claim
after selecting a rare accepted outcome. Nor does a small net value make
the separate switches small. A conservative operator estimate is

    ||V_D||<=max{(2K+1)g,d(N_X,sites+1)},              (U22)

using 0<=H_prop<=(2K+1)g I and
0<=R_D<=d(N_X,sites+1)I. The coefficient bounds of the complete old clock
may sharpen this loose estimate.

For a pulse in (U16), its mean interaction energy is conserved throughout
the pulse because [H_swap,E]=0. The switch-on and switch-off mean works
cancel exactly. Its positive interaction norm is at most 2 lambda m;
borrowed switching energy and control of the duration are still physical
resources. Equations (U20)-(U22) quantify mean work and interaction scales;
they do not specify a microscopic finite quantum controller, its work
fluctuations, or the manufacture of exact coupling waveforms.

Under this explicitly switched contract the protected outputs may remain
isolated while the core runs, is replaced, or is allowed to evolve for
any further time. Export changes the old core's state, so applying the
old exact-return theorem to that altered state without proof is invalid.
The protection identity does not require such a return. It guarantees
that any later core evolution cannot erase the isolated output.

## 7. The finite outer-history alternative and its limits

The three operations in (U7) also have the exact rounded-energy interface
needed by a finite outer history. The old U commutes with H_(0,D) and
C_D. Export exchanges equal-spectrum archive/pointer/latch sites.
Replacement exchanges identical full core spectra and the corresponding
C counts. Thus the complete word preserves the summed rounded energy
and summed core occupation count on all raw states.

An outer history can execute this word with its own counted thermal
launch, cursor, completion latch, interaction energy and error. Its
completed word has exactly (U8), before adding those outer readiness and
timing errors. In the direct macro construction a label U or full-core
SWAP is a large-support gate; the earlier seven-site local Hamiltonian
bound is not automatically inherited. A local bounded-support compiler
on arbitrary raw thermal sectors would need its own proof and resource
count.

This replaces continuous old-core dynamics by the selected endpoint U.
It does not make the original H_D keep running through its literal
3T_h return. The new outer Hamiltonian has its own time scale and return.
If its inverse history later undoes export and replacement, the tape
can be restored to its original contents. A longer finite outer window
and indefinitely protected storage under external isolation are distinct
claims.

Likewise the full outer resource count exceeds (U9). In the stated
all-qubit macro option, K_out physical cursors plus a launch fuel, sink
and completion latch add K_out+3 sites. All of their Gibbs states,
nonstationarity, interaction terms and energy moments belong to that
option's inclusive account. They cannot be supplied by the old core's
clock-readiness theorem without a separate construction.

## 8. Exact-reset lower bounds and failure conditions

A universal replacement channel C->omega_C cannot erase arbitrary
information while returning the complete remainder to one fixed
uncorrelated state. Two orthogonal inputs would then have identical
global outputs, contradicting preservation of trace distance by a
unitary. Leaving input-dependent correlations in a nominally restored
machine does not return that machine as an independent fresh resource.

There is also a finite-dimensional lower bound. Let dim C=D, let omega_C
have rank r_omega, and implement its exact replacement channel by a
unitary with an environment of dimension M initially of rank r_env.
Diagonalizing that initial environment supplies at most M r_env Kraus
operators. The replacement channel's Choi operator has rank D r_omega,
so

    M r_env>=D r_omega.                               (U23)

For a full-rank target r_omega=D and r_env<=M, this implies M>=D.
A same-sized mixed cartridge meets that dimension requirement by (U4).
Apply the statement to the reset thermal hardware, or to a complete core
with a specified full-rank next-input state. It is not a lower bound on
the work of every restricted-input or approximate-reset protocol.

The concrete N-use protocol consumes its declared cartridges even when
the corresponding core record is rejected. A finite stock is not an
infinite reset cycle. Output memory capacity, fresh information inputs,
spent quantum correlations, temperature contrast and control must all
be retained in any extension to more uses.

Decisive falsifiers include a failure of the complete SWAP identities,
using a referenced next input as if it were thermal or independent,
dropping old output contents, resetting only successful branches while
charging a fixed number of attempts, applying (U13) to nonthermal input
qubits, ignoring an active interaction during a claimed conserving SWAP,
or transferring the local/permanent-storage claim between the two
different control contracts. No scientific executable, simulation or
expanded circuit was run. Same-session review is not independent
mathematical acceptance.
