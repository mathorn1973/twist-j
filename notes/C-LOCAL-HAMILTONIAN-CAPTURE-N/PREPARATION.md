# Preparing the encoded reservoir and clocks from a basis configuration

**NON-CANONICAL. L1. Conditional candidate-T analytical construction.**
[Claim #1749](https://github.com/mathorn1973/twist-j/issues/1749).
No new scientific executable or numerical experiment is used here.

The construction is a finite local Hamiltonian simulator of a specified
complete target map. This file makes its preparation prefix explicit. The
large flat reservoir state is produced by that prefix and is not supplied
as an initial coherent resource. The generator energy of the simulator and
the target's encoded additive ledger remain different observables.

## 1. Initial state and the two clocks

Use the binary target encoding fixed by the compilation construction.
The target basis-source configuration, including its standing token,
coordinate/coin basis state, zero auxiliaries and cyclic clock value zero,
is assigned a specified computational basis code. Fixed basis-loading gates,
if needed under a different code convention, belong in the compiled prefix.
The incoming label and occupied old memory may be arbitrarily entangled
with a reference; their logical input is not initialized or overwritten.

There are two distinct clocks:

- The simulated target clock is a finite register with the original cyclic
  values c=0,...,M-1. Its initial code is the binary all-zero string for c=0.
- The physical history clock of the local Hamiltonian has the domain-wall
  basis states used in the propagation proof. Its initial t=0 state is the
  all-zero domain-wall string. It is not a supplied clock wave packet or
  a coherent superposition of completed computation histories.

All fresh data rows, routing/work qubits and history-clock bits start in
specified basis states. Only the admitted logical input is unknown. The
initial encoded reservoir is the single level |0>, not the flat state.
This is a complete basis-ready apparatus condition, with an arbitrary
logical/reference vector retained as a tensor factor.

A basis configuration need not be an energy eigenstate of the interacting
propagation Hamiltonian. The initial interaction-energy spread is specified
in Section 4; it must not be described as absent merely because the
configuration has no computational-basis superposition.

## 2. An explicit full unitary preparing the flat reservoir

Let Q>=1 and L>=Q be the fixed integers of the target reservoir construction,
with the nominated choice L=Q 5^22. Set

    B = L+2Q-1,
    H_res = span{|n>: n=0,...,B},
    b_L = (1/sqrt L) sum_(n=Q)^(Q+L-1) |n>.

The integer B is a largest level label. The register dimension is B+1.
Define S_(0,Q) to exchange |0> and |Q> and act as identity on every other
level. For j=1,...,L-1 set

    a_j = Q+j-1,       b_j = Q+j,
    c_j = 1/sqrt(L-j+1),
    s_j = sqrt((L-j)/(L-j+1)).

Define R_j by

    R_j |a_j> = c_j |a_j> + s_j |b_j>,
    R_j |b_j> = -s_j |a_j> + c_j |b_j>,
    R_j |n>   = |n>  for n outside {a_j,b_j}.

Since c_j^2+s_j^2=1, each R_j is a total unitary, including on reservoir
inputs other than the designated basis level. The specified preparation is

    P_B = R_(L-1) ... R_2 R_1 S_(0,Q).                       (P1)

It is the identity on every other target factor, including the logical
input, old memory, reference and target clock. Its inverse is the reverse
word with every R_j replaced by its adjoint. No outcome is discarded and
there is no state-dependent normalization instruction.

After S_(0,Q) and the first j rotations, induction gives

    R_j ... R_1 |Q>
      = (1/sqrt L) sum_(i=0)^(j-1) |Q+i>
        + sqrt((L-j)/L) |Q+j>,       0<=j<=L-1.              (P2)

For j=0 the sum is empty and the remaining coefficient is one. At step j,
the incoming residual coefficient is sqrt((L-j+1)/L). Multiplication by
c_j leaves exactly 1/sqrt L at a_j, and multiplication by s_j passes
sqrt((L-j)/L) to b_j. This proves the induction. For j=L-1 the final
residual is also 1/sqrt L, so

    P_B |0> = b_L.                                          (P3)

The L factors in (P1) are explicit finite two-level unitaries. Their entries
are specified exact real algebraic numbers. Their physical realization may
therefore require exact selected couplings; no robustness or finite-control
precision theorem is inferred from their algebraic specification.

## 3. Local implementation and counted preparation time

The level labels in (P1) specify a logical register, not a single physical
site of dimension B+1. Encode it in ceil(log_2(B+1)) binary qubits. Each
factor on that register is extended as identity on unused battery codes. The resulting
P_B is a completely specified unitary on that binary register. This describes
the preparation on valid composite target codes. For the full simulator,
use COMPILATION.md's common extension: the joint macro is identity whenever
any target register code is invalid. It is not asserted to act as a
battery-only tensor product on invalid composite codes.

The finite compiler in the companion construction expands this explicit
macro into one- and two-qubit gates, routes them through the fresh data rows,
and includes their physical history transitions in its total K. The
large-level SWAP and rotations are not free or instantaneous physical gates.
Its gate expansion, qubit storage, spatial routing and endpoint time are
covered by that construction's bounds. An algorithm specifies the exact
algebraic coefficients, but coefficient bit complexity, physical calibration
precision and fabrication cost are not quantified by those gate counts.

Choose a target release count h with 0<=h<=H, default h=0. The target macro
word begins with P_B, followed by the L_prog+h funded
cyclic-clock ticks of the requested finite experiment. Thus its number of
macros is

    nu = 1+L_prog+h.

The L rotations/SWAP factors make the first macro explicit. Counting that
macro once in nu does not count its physical implementation as one gate:
the compiler's gate bound depends on the full encoded dimension and covers
its expansion. In particular, K includes reservoir preparation before the
first funded target tick. There is no additional uncounted coherent source
preparation at the read boundary.

The Hamiltonian propagation theorem applies to the full compiled word,
including this prefix. At its exact transfer time it produces the complete
word output, including every target rejection, compiled work value and old
logical/reference correlation. Neither the intermediate preparation levels
nor the rejected target histories are postselected away.

The default h=0 word ends at the capture/readout endpoint. The inherited
outside-bound-band threshold belongs to that endpoint. Choosing h>0 gives
a separate compiled target word with h further release steps; its finite
memory-buffer conclusion does not supply a continued binding bound. The
Hamiltonian theorem concerns its exact endpoint, not an interval of physical
time throughout which the simulated gate boundaries are occupied in order.
A family of endpoint constructions is not an actual continuous-time storage
window of one device.

## 4. Physical generator energy and the basis-ready boundary condition

A simple local Hamiltonian specifying the initial ready subspace is

    H_init = Delta sum_(i in ready) (I-|0><0|)_i,     Delta>0.  (P4)

The sum contains the apparatus qubits required to be zero: encoded reservoir,
zero code of the target clock, physical domain-wall clock, fresh data rows
and work/routing registers. Unknown input registers are excluded. Where a
nonzero fixed code is used, replace |0> by that specified local basis value
or load it as an explicitly counted prefix gate.

Every term in (P4) is positive and on-site. Its ground subspace is exactly

    H_input tensor |ready_basis>,

Here H_input=(C^2)^(tensor 10) is the entire raw pair of label-code blocks.
Its admitted logical input occupies the 676-dimensional valid 26-by-26
subspace; that restriction is an input promise, not enforced by H_init.
The gap is Delta to a defect in any constrained qubit. This identifies a local
basis-preparation target without preparing, measuring or dephasing the
unknown logical/reference input. It does not supply a cooling rate, an
exact finite-time reset from arbitrary dirty states, or an implementation
of H_init from the original TWIST-J dynamics.

For the companion positive propagation Hamiltonian H_prop with K compiled
transitions and scale g>0, the ready vector has, for every admitted unknown
logical/reference input,

    <H_prop>_ready = g,
    Var(H_prop)_ready = g^2 K/(K+1)^2.                       (P5)

These follow from the scalar diagonal g and first clock-edge coefficient
g sqrt(K)/(K+1) on the legal history subspace. All other clock-edge terms
annihilate the ready vector. Hence the mean and variance are independent of
the unknown input, while the vector is nonstationary for K>=1.

The exact completion time under that fixed Hamiltonian is

    t_* = pi hbar (K+1)/(2g),                               (P6)

and each individual local term has norm at most g under the specified
normalization. The closed propagation conserves its physical generator
energy, including interactions, throughout preparation and computation.
Equations (P5)-(P6) are not an assertion that the entire many-site operator
norm is at most g.

Preparing a ground state of H_init and then switching to H_prop is one
external way to establish the ready boundary condition. Under an ideal
sudden switch from zero initial H_init energy, its mean energy change is g.
That switch is an additional preparation action; it is not generated by the
subsequent time-independent H_prop. The present autonomous theorem begins
with the explicitly specified nonstationary ready state for H_prop. A closed
model that also generates the switch or cools an arbitrary initial apparatus
must include its source, entropy and retained records separately.

## 5. Why the old additive energy cannot also be silently imposed

Let the target reservoir's former additive reading be

    E_add = epsilon N_res + E_rest,       epsilon>0,
    N_res |n> = n |n>,

where E_rest acts on all other factors. Suppose a proposed preparation
starts from a density operator rho_0 commuting with E_add and evolves with
[H,E_add]=0. Then rho(t) still commutes with E_add. Partial trace over rest
gives

    [rho_res(t),N_res]=0.                                   (P7)

For example, exponentiate the commutator: invariance under the joint
energy-translation unitary and cyclicity of the partial trace imply
invariance under exp(-i epsilon N_res s) for every s. The nondegenerate
reservoir levels therefore make rho_res diagonal in n.

For every normalized diagonal reservoir state sigma,

    <b_L|sigma|b_L>
       = (1/L) sum_(n=Q)^(Q+L-1) sigma_nn <= 1/L.

Measuring the projector |b_L><b_L| gives the trace-distance lower bound

    D(sigma,|b_L><b_L|) >= 1-1/L,                            (P8)

where D is one half of the trace norm. This is sharp: the uniform diagonal
mixture on the L target levels attains it. Thus neither exact preparation
nor a small approximation to b_L is possible from completely stationary
E_add resources while preserving that same additive reading. The result
covers an arbitrarily large incoherent fuel register and an energy-basis
clock as part of rest. It does not exclude a supplied coherent fuel, a
noncovariant interaction law, or a changed physical energy definition.

The circuit prefix P_B is deliberately not constrained to commute with this
old E_add. Its Hamiltonian simulation conserves H_prop instead. The old
reservoir is consequently an **encoded logical reservoir** in this simulator.
Its level number and the target conservation equation remain meaningful
checkpoint observables of the simulated law; epsilon N_res is not proved
to be the physical on-site Hamiltonian of these simulator qubits.

In particular, a large virtual capacity epsilon B cannot be called a large
physical battery capacity funded by the modest mean g in (P5). That would
equate two distinct observables. A physical reservoir interpretation requires
an additional identification of subsystem energies and interactions. This
construction supplies no such identification and does not identify either
energy with the canonical spectral energy.

A related elementary boundary is that if the battery mean increases and
all other subsystem marginals return unchanged, exact additive conservation
is impossible. Returning a coherent fuel exactly while silently assigning
zero cost to the new battery would not repair (P7)-(P8). Supplying the flat
state on an isomorphic fuel and swapping it into the battery merely moves
the required initial coherence to that fuel.

Finally, if the entire initial state were stationary for the actual fixed
Hamiltonian H_prop itself, it could not generate a new clock or preparation
record at all: exp(-iH_prop t/hbar) rho_0 exp(iH_prop t/hbar)=rho_0. The
nonzero variance in (P5) exposes the actual nonstationary resource of this
basis-ready local simulator.

## 6. What this preparation establishes

The flat logical reservoir is generated exactly from one basis level by an
explicit finite unitary. Both clocks start in specified local basis codes,
with no hidden coherent clock packet. The physical local compiler includes
the entire preparation prefix, so its completion time and spatial count
cover that work. The fixed positive propagation Hamiltonian has an explicit
initial energy and energy spread, conserves its full generator energy and
reproduces the complete target output at the stated finite endpoint.

These are properties of an added finite local quantum simulator. They do
not derive its hardware, coupling constants, ready-state preparation or
physical energy identification from the original occupation law or native
checkpoint law. They also do not give a reset, autonomous cooling or a
single realized occurrence. A stronger claim identifying the target's
additive ledger with an actual physical battery remains unsupported and,
under the stationary covariant preparation assumptions of Section 5, is
explicitly obstructed.
