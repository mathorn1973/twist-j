# Retained outputs and counted reuse: scope and resource account

**NON-CANONICAL, L1. Conditional analytical candidate-T; independent
mathematical acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1767.

This continuation starts from PR #1768 at
`485f907531ab329b3aabc08d0a1bf594ae987c80`. The seventeen preceding files
remain unchanged. The separate mathematical PASS review applies only to
the older seven-file revision `d13851796d5e7a316e1f628407e1bedef04f9bad`.
The local, thermal and present reuse constructions need their own review.

There are two constructive contracts. A specified driven apparatus exports
each record into an isolated memory and replaces the working state from a
counted cartridge. Its record can persist under the stated isolated-memory
law. A different finite autonomous Hamiltonian implements the complete
export/reset sequence and a prescribed holding interval, with entirely
thermal auxiliary input. Its outer clock eventually reverses the sequence.
The two laws must not be combined into a claim of permanent autonomous
storage with all resources restored.

[REUSE_RESET.md](REUSE_RESET.md) proves the export/reset maps and the
driven account. [RETAINED_CYCLE.md](RETAINED_CYCLE.md) gives the finite
autonomous implementation. [RETENTION_LIMITS.md](RETENTION_LIMITS.md)
states the closed-system and information-capacity obstructions.
[REUSE_VALIDATION.md](REUSE_VALIDATION.md) specifies the review contract.

## 1. What returns, what is retained, and what is consumed

Write D for the complete S-qubit device of THERMAL_CLOCK.md, including
all data rows, donors, source and battery, old cursors, fuel, sink and
completion latch. Its 15 admitted information qubits are logical input,
old receiver and old archive. The other S-15 factors have the declared
product Gibbs state. They are not supplied pure.

These fifteen information sites are in the initial row. The physical
archive and pointer read after the run are in the final row; the logical
values have been transported there. The input and output tensor factors
are therefore not identified by their logical names.

The output block Y consists of five archive qubits, the acceptance pointer
P, and the completion latch L. Its physical bare energy is d n_L; the
other six qubits have zero bare energy. A new slot O_i has precisely this
seven-qubit spectrum. The full SWAP_(Y,O_i) transfers the record and every
correlation with the passive reference. It does not copy an unknown state.
The slot's previous contents enter D and remain in the later waste.

One complete use has the endpoint word

    V_i = SWAP_(D,B_i) SWAP_(Y,O_i) U_D(tau),
    tau=3 T_h/2,                                     (U1)

where B_i is a fresh S-qubit cartridge with the same site spectra as D.
It contains the next admitted information input and a fresh Gibbs hardware
bank. The first rightmost factor is the exact old midpoint endpoint.
The second exports the record on every branch. The last restores the
entire working hardware to its supplied Gibbs state while moving the
spent state, including all old correlations, into B_i.

The reset acts on rejected and dormant runs as well as accepted runs.
There is no outcome-conditioned omission from the resource count. The
hardware factors return independently of the retained record; the next
information input may have its specified correlations with other inputs
or the passive reference. Calling that correlated next input independent
would change the contract.

Thus the old clocks are restored by replacement. This is not a proof that
the old Hamiltonian's unperturbed return at 3 T_h survives extraction.
An export generally changes the old invariant history. Neither applying
the old inverse after export nor waiting for its former return time is
a valid substitute for the displayed reset.

## 2. Finite inventory for N uses and a final ready core

Fix N>=1 before constructing the apparatus. Count an initial core D,
N reset cartridges B_1,...,B_N, and N output slots O_1,...,O_N. The Nth
cartridge supplies the state left in the core after the Nth reset. The
construction therefore includes N+1 admitted 15-qubit information inputs,
including the prospective next input. Their states and correlations are
declared information resources, not thermal auxiliaries.

For the autonomous version add K_o physical outer cursor qubits, an outer
hot launch fuel, a cold launch sink and a cold completion latch. Node zero
of the history is a fuel configuration, not another cursor qubit. The
exact physical inventory is

    S_total=(N+1)S+7N+K_o+3,
    dim H_total=2^S_total.                            (U2)

Let s=r+J, and retain the inner definitions

    S=3n(s+1)+2Ar+K+3,
    C_c=2n(s+1)+Ar+K+2,
    N_hot=Ar+1.

The complete counts for the autonomous input are

    C_total=(N+1)C_c+N+K_o+2,
    H_total=(N+1)(Ar+1)+1,
    Z_total=(N+1)n(s+1)+6N.                           (U3)

Here C_total is the number of positive-gap cold factors, H_total is a
count of hot factors, not the Hamiltonian, and Z_total counts zero-gap
factors including 15(N+1) information qubits. The identity
C_total+H_total+Z_total=S_total checks the partition. Every retained output
slot, spent cartridge and outer controller site is included.

For the thermal specialization each output slot starts with its six
zero-gap qubits in I/2 and its latch at the same cold temperature as the
device. No pure blank output tape is assumed. Record interpretation uses
the slot's completion/acceptance bits, and not the preexisting contents
of its six zero-gap qubits. REUSE_RESET.md also allows occupied slots;
those supplied states have their own entropy and correlation account.

Choose the one cold temperature after fixing the enlarged finite
inventory. All positive cold gaps are at least d, so it suffices to take

    beta_c d=[ceil(log_2 C_total)+104] log 2.           (U4)

The probability of any cold excitation in the complete inventory is then
less than 2^-104. The earlier inner reset depth still gives xi<2^-104;
lowering its cold temperature only improves its bounds. The hardware size
and specified endpoint matrices do not depend on this temperature, so
(U4) is not a circular prescription.

The outer fuel has gap 3d and is at the inherited hot temperature. Its
excitation probability is

    p_o=1/[1+exp(3 beta_h d)]>=1/3,                    (U5)

because beta_h(G+r_*)=log 2 and G+r_*>=4d. Thus no third temperature is
introduced. There is one outer activation event for the complete N-use
sequence, not N independently supplied outer clocks.

If S_info is the entropy of the admitted joint information-input marginal,
the input entropy of the complete autonomous apparatus is exactly

    S_initial=S_info+[Z_total-15(N+1)] log 2
              +sum_(all hot/cold factors a) h_2(p_a). (U6)

For a partition including the passive reference, replace S_info by the
actual joint information/reference entropy. The thermal factors remain
independent of that joint input. A purification of them is not a free
extra reference in the output contract.

## 3. Retention under the two complete laws

In the driven construction the old interaction is turned off at tau,
the export and reset contacts are applied, and used output slots are
thereafter isolated with Hamiltonian d n_(O_i,L). The accepted sector
n_(O_i,L)n_(O_i,P)=1 has only a scalar free phase, so its quantum record
and reference state persist. The reset of D does not affect those slots.
This assertion requires continued isolation and the specified switching
schedule. It is not a theorem about the old permanently coupled device.

The switching schedule and work exchange are explicit physical inputs.
REUSE_RESET.md gives the positive SWAP pulse Hamiltonians, their durations,
transient interaction energies and net work. Those formulas do not
constitute a microscopic autonomous implementation of an ideal classical
timing source. Replenishing that source cannot be inferred to be free.

The autonomous construction instead uses a positive static outer history
Hamiltonian for the complete word (U1). During its completed tail all
N outputs have been exported and the original core, including its clocks,
has been reset. The slots are not modified by subsequent tail edges.
For a predetermined [T_o,2T_o], the outer completed-tail deficit is below
2^-128. The fixed slot-only read predicate is

    Q_i=n_(O_i,L)n_(O_i,P).                            (U7)

Cold-zero output latches exclude false reads before their exports,
including the dormant outer branch. A separate outer completion latch
can certify that the whole N-use/reset word has finished. Individual
slot reads do not require a hidden outer-clock projector.

With the inherited source margin and the thermal budget, the conservative
per-slot bounds throughout that window are

    p_read,i>1/200000,
    D(rho_i,acc,rho_i,ideal,acc)<200000*2^-103,
    u_i,acc<1/1000000.                                (U8)

The reference here is genuinely passive during the subsequent operations.
The complete tape theorem uses the joint sequential channel, so it also
handles correlated information inputs without pretending that future
operated-on inputs stay passive. The common outer launch means that
unconditioned slots need not be independent even for independent inputs.
No product success law or unlimited number of successful trials follows.

After reset the source tested by the unwanted-band effect is in spent
cartridge B_i, not in the active core. For the slot-only predicate, the
single export-before-reset history node contributes an additional bound
below 80000*(3/4)^Lambda; RETAINED_CYCLE.md includes it in the joint
comparison budget. Conditioning also on the outer completion latch
removes that location ambiguity. No material band detector is supplied.

At 3T_o the clean outer history reverses the exports and resets as well
as the source operations. The comparison input is restored. Actual read
probability in a specified slot is bounded by the outer cold-defect
weight, including all output latches as well as the outer controller.
This exact reversal includes the waste cartridges and makes clear
why they cannot be removed from the law or the initial resource account.

The autonomous macro gates act on complete device blocks. Their support
grows with S, unlike the earlier seven-site thermal construction. This
note does not claim a bounded-degree geometric compilation of the new
autonomous export/reset controller. It proves a finite full-space law
and endpoint contract. The local SWAP contacts of the driven protocol
do not by themselves close that separate autonomous locality obligation.

## 4. Energy and true replenishment

For the autonomous implementation sum the rounded energy over every core,
cartridge, output and outer-controller site. The interaction retains the
negative residual correction from every core and cartridge. The conserved
occupation budget is

    C_all=sum_(D,B_1,...,B_N) (N_X+n_fuel).

The outer fuel and sink have exact integer-multiple gaps and add no
residual. On the entire raw space,

    -d C_all <= U_t^* E_phys,total U_t-E_phys,total
             <= d C_all,                              (U9)

and the actual initial expectation obeys

    <C_all><(N+1)/3+2^-104.                            (U10)

This is an unconditional bound, not an energy bound for selected records.
The linear dependence counts all supplied cartridges. It is not removed
by calling the active core reusable. RETAINED_CYCLE.md gives the complete
initial Hamiltonian moments and capacities, not just the onsite mean.

The reset SWAP consumes a ready distribution and relocates the old state.
For the Gibbs hardware part F, let tau_F be its fresh product state,
sigma_F its spent state, and Q_a the energy gained by replacement-bank
site a. The exact identity is

    sum_a beta_a Q_a
       = S(sigma_F)-S(tau_F)+D(sigma_F || tau_F).       (U11)

It includes correlations within the spent hardware through the relative
entropy. The 15 information qubits are excluded from this Gibbs formula;
their old states and reference correlations are transferred, not erased.
There is no general rule charging one fixed heat amount per physical
qubit regardless of its initial state, spectrum or correlations.

Restoring a spent cartridge to its original ready state while preserving
the tape requires a further source and a destination for its information,
entropy and changed energy. Relabeling the cartridge as a bath does not
restore it. The elementary finite-reservoir entropy balance is derived in
REUSE_RESET.md; its standard single-temperature form is discussed by
[Reeb and Wolf, New Journal of Physics 16 (2014) 103011](https://arxiv.org/abs/1306.4352).

The construction supplies a finite stock for N attempts and a final reset.
It does not supply a replenished cyclic reservoir, an unlimited tape or an
unchanged control source. Reversing the entire closed preparation restores
those resources only by undoing the retained outputs as well.

## 5. Exact boundaries

Finite-dimensional evolution under a fixed Hamiltonian makes every fixed
record expectation a finite sum of exponentials. Exact permanent change
after a write would make that analytic function constant on an interval,
hence constant also before the write. Recurrence additionally excludes
uniformly accurate permanent retention separated from the initial record.
RETENTION_LIMITS.md supplies the hypotheses and quantitative statements;
neither result rules out the finite window above or driven isolation.

Returning just a clock marginal is a weaker condition than returning the
joint device and all its resources. Likewise, preserving a sharp classical
label by copy/uncompute is a different contract from preserving an
arbitrary quantum input while extracting an additional informative record.
The latter cannot retain the exact identity channel on the unknown input
and also provide an input-dependent complementary record.

The new results are analytical constructions and obstructions in declared
finite models. Their physical premises include specified spectra,
temperatures, couplings, input states and, for permanent driven retention,
the isolation and switching mechanism. Native derivation, material
robustness, an individual-event law and cost-free indefinite reuse remain
outside the result. No scientific executable or expanded circuit was run.
