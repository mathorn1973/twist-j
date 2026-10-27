# What the environment prepares and what the native law does not supply

**NON-CANONICAL, L1. Conditional analytical candidate-T, claim #1757.**
Independent mathematical acceptance is pending.

## 1. Fixed inherited target

Authority remains Public Canon v105 at main
892a0b11089d34e241e1eb76d2c03247022d18e6. The fixed direct input is
[#1756 at 901c400f85c427752e2e4367afb6cd00e59ac8c8][previous].
Its physical source is the qubit s=c_0 at the entrance of a main clock.
Its sharp data/fuel/battery circuit and completion latch come from #1754;
the accepted source/filter channel remains conditional on #1746/#1752.

This note keeps that logical word and its data interface. It replaces the
clock coefficients, adds an environment and a loading path, guards the
handoff, and extends the output tail. The resulting full Hamiltonian is a
new law. Preparation of the old source state is not a claim that the entire
old autonomous Hamiltonian has survived unchanged.

## 2. The concrete environment and genuine acquisition step

The environment is two finite qubits h and c, initially in the product of
Gibbs states for the bare Hamiltonians 3 epsilon n_h and epsilon n_c.
Their excitation probabilities are 1/3 and 1/5. The specified source, main
clock and loading path are initially empty. There is no preoccupied new
loader cell that merely renames the previous supplied source excitation.

The local reaction converts h1 c0 s0 t0=0 into h0 c1 s1 t0=1.
Thus two bare quanta leave the environment and populate the actual source
and the loader. A stationary bare-energy mixture supplies the energy;
no superposition between different bare-energy eigenspaces is inserted.
The hot/cold population ratio for the participating environment levels is
p_10/p_01=2. The virtual gap is 2 epsilon, so its population-inversion
parameter is beta_virtual=-log(2)/(2 epsilon).

The four initial environment weights are (8,2,4,1)/15 in order 00,01,10,11.
Only the 10 sector enters the active history path. The other three sectors
remain present and inactive. This is a complete mixed-state construction,
not selection of the favorable environment at zero cost.

During the specified preparation window, the active state is close to
spent environment |01>, the original ready source |1>, the untouched old
apparatus data and a moving interior-loader packet. The original first
clock edge is disabled on every such good history. Source charging is a
real intermediate interface. The full apparatus is not then frozen, and
the loader remains part of the state.

Unconditionally the comparison state is a mixture with active weight
q=4/15. The local ready predicate n_s(1-n_t_last) has weight at least
q(1-delta), not near one. It is a mathematical observable; no detector or
postselection instrument is added silently. The old capture threshold must
also be multiplied by this environment weight. PREPARATION.md proves the
new whole-input bound greater than 1/75000.

## 3. Bare stationarity and full-generator nonstationarity

The initial density operator commutes with H_0. Each environment marginal
is a stationary Gibbs state for its own bare Hamiltonian, and the empty
source and loader are stationary for their isolated onsite energies.

The product is nevertheless not stationary for H=H_0+H_prop. The reverse
reaction configuration is initially empty, while the forward configuration
has weight 4/15. The only initially noncommuting Hamiltonian term is the
local conversion edge. Its contribution gives exactly

\[
 \|[H,\rho_{\rm in}]\|_1=\frac8{15}a_0>0.
\]

This is the remaining initial nonstationarity. The full-energy asymmetry
is not a preexisting phase between the hot qubit's two levels. It is a
property of the prepared joint state relative to the coupled Hamiltonian.
The active state's full-energy spectral distribution depends on the entire
engineered path. ENVIRONMENT.md gives that distribution and distinguishes
asymmetry from energy variance.

No coupling is switched on in the claimed dynamics. H is fixed from the
initial instant. Comparing with a decoupled or hopping-removed Hamiltonian
is not a physical assembly protocol. Producing the stated uncorrelated
input while this contact is present remains a preparation requirement.
A claim that an actual switch has zero cost cannot be inferred from a
zero initial mean hopping term.

## 4. Which thermal claim is and is not proved

Thermal-machine descriptions using virtual transitions and autonomous
clocks powered by thermal disequilibrium are prior art; see
[Brunner et al.][virtual] and [Erker et al.][clocks].
The present note supplies its own finite Hamiltonian, geometry, loading
bounds and accounts. It imports no bath limit, dissipation theorem or
material device from those references.

The two environment qubits are finite, become depleted and correlated, and
are not continuously replenished reservoirs. Their initial temperatures
are labels for the specified Gibbs marginals, not claims that they remain
at those temperatures while operating. The environment is not a Gibbs state
of the full coupled Hamiltonian. The clean vacuum source/loader, clean work,
charged data fuel and initialized latch are further supplied resources.

Different temperatures make the specified virtual transition inverted.
The proof does not show that a temperature difference is necessary for
every finite transient excitation transfer: even equal-temperature donors
can transfer energy into an initially pure ground-state receiver. Such a
receiver is already an additional thermodynamic resource. Nothing here is
a cyclic heat engine, an efficiency claim or work from a single equilibrium
bath with every other subsystem restored.

For any finite fixed H, a full Gibbs state exp(-beta H)/Z commutes with H
and remains constant. More generally [rho,H]=0 implies constant closed
evolution; a unitary commuting with H preserves this stationarity.
Consequently that preparation class cannot produce this working input.
Adding an environment is useful only if its complete initial state and
contact supply the required departure from full stationarity.

## 5. Original-law boundary

The canonical occupation-space U_rec specifies a transfer/contact law on
its declared carrier. The [Canon][canon] distinguishes its occupation
charge from a spectral energy. The active one-pair, carrier and memory
sector has occupation charge 10I; this is not the onsite energy used here.
The selected spectral-energy source in the Canon also has its own specified
coherent input and generator. It is not an implementation of these new
thermal qubits or their local reaction.

Under the unchanged spectator extension
U_rec tensor I_environment,source,loader, every marginal of those added
registers is constant. That law neither charges this empty source nor
creates the loader. This observation is specific to the unchanged extension;
it is not an impossibility theorem for every future native coupling.

The additions here are physical model assumptions: qubit carriers, bare gaps,
Gibbs marginals at specified parameters, clean vacuum cells, a four-site
resonant conversion, local guarded propagation, engineered coefficients,
and continuous-time Hamiltonian evolution. Original particle coordinates
remain encoded data, not positions on this added qubit lattice. A native
implementation would require explicit compatible dynamics, position and
energy identifications.

What remains unprepared includes the initial environment itself, its
uncorrelated contact with the cold ready apparatus, empty-register purity,
charged data fuel, latch/work preparation, and precision of the couplings.
The complete energy expectation includes the environment and the contact;
it is not the minimum work required to manufacture all these initial states.
Cooling, material realization, physical readout, repeatable replenishment,
useful reset and an occurrence law remain separate obligations.

[previous]: https://github.com/mathorn1973/twist-j/tree/901c400f85c427752e2e4367afb6cd00e59ac8c8/notes/C-LOCAL-CLOCK-SOURCE-N
[canon]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md
[virtual]: https://arxiv.org/abs/1106.2138v2
[clocks]: https://arxiv.org/abs/1609.06704v3
