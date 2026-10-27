# Preparing the thermal contrast from one temperature

**NON-CANONICAL, L1, conditional analytical candidate-T.**
Independent mathematical acceptance is pending.
Public reservation: [#1765](https://github.com/mathorn1973/twist-j/issues/1765).

The hot and cold Gibbs resources supplied in [#1764][prior] can be
prepared from finite hardware initially at one common temperature, plus
one explicitly inverted fuel qubit. A single positive, static local
Hamiltonian includes fuel release, clock loading, paid thermal-state
exchanges and the subsequent capture endpoint. Every donor, thermal
defect, work record and unfinished history remains in the apparatus.

This moves the preparation boundary. The temperature contrast is now an
output of a specified operation. Fuel inversion, a common-temperature
Gibbs product, manufactured spectra and its contact with the fixed
interaction remain supplied. No preparation from a stationary total
input, native-law derivation or material realization is claimed.

## 1. The actual thermal preparation

Put beta_0 epsilon=ln 2. Keep the physical target gaps of #1764 fixed.
Use its parameters R_o, K_o, D=2^84 and
b_o=84+ceil(log_2(D+K_o+3)). Add these matching-dimension donors:

| Target | Fixed target spectrum | Donor spectrum, initially at beta_0 | Prepared target |
| --- | --- | --- | --- |
| Hot source | D excited states at (R_o+3)epsilon | D excited states at epsilon | beta_h=beta_0/(R_o+3) |
| Cold sink | D excited states at epsilon | D excited states at b_o epsilon | beta_c=b_o beta_0 |
| Distinguished old work ladder | levels 0 through 2R_o, spacing epsilon | same levels, spacing b_o epsilon | beta_c |
| Each of K_o+1 old clock sites | two levels, gap epsilon | two levels, gap b_o epsilon | beta_c |

All targets initially have their own Gibbs state at beta_0. Each funded
SWAP puts the donor's population distribution on the target and retains
the old target distribution in the donor. This prepares the entire joint
Gibbs product required by #1764 on the good buffered component, including
the logical/reference interface. Separate matching marginals would not
suffice for the subsequent channel.

Let a pair have spectra g epsilon n and G epsilon n with the same level
multiplicities. Write mu_g and mu_G for their initial mean level numbers.
The exact mean work paid to that pair is

\[
 W_{pair}=\epsilon(g-G)(\mu_G-\mu_g)\ge0.
\]

Thus both cooling and heating in this fixed-gap protocol have a stated
cost. [ENVIRONMENT.md](ENVIRONMENT.md) gives the explicit sum for every
pair, the entropy retained in donors and work records, and the distinction
between this protocol's cost and a minimum resource cost.

## 2. Starting the work store and clocks

The new work ladder has physical levels 0 through 4Q and initially has
its Gibbs distribution at beta_0. Here Q is a finite upper bound on the
one-row payload energy in units epsilon, enlarged to at least 128.
The new clock and counter gap is ell epsilon. They also start at beta_0;
ell is chosen from the finite number of actual sites that must be empty.
No further pure timer or initially charged work peak is supplied.

One fuel qubit has gap E_f=(2Q+2ell)epsilon and input excited population
1-delta_f, delta_f=2^-96. For each b=0,...,Q the local resonant reaction is

\[
 |1_f,b_B,0_{m_0},0_{t_0}\rangle
 \longleftrightarrow
 |0_f,(b+2Q)_B,1_{m_0},1_{t_0}\rangle.
\]

Its released energy is exactly 2Q epsilon for the work shift plus
2ell epsilon for the two created clock excitations. The shifted range
supports every energy-conserving gate prefix without truncation at the work
ladder boundary. The probability outside the joint fuel/work/clock/counter
reference component is less than 3 times 2^-96. All such states remain
under the same Hamiltonian.

The inverted qubit is the newly supplied nonthermal resource. It needs
no phase coherence between its bare-energy eigenstates. Its exact excess
free energy relative to beta_0, and a strictly positive full-H initial
commutator, are exhibited in ENVIRONMENT.md. Calling this qubit thermal
or claiming to have prepared its inversion would be incorrect.

## 3. One local Hamiltonian and the complete endpoint

[HAMILTONIAN.md](HAMILTONIAN.md) constructs the finite gate word without
encoding the large thermal sites into an unprepared clean binary code.
A physical multilevel counter, dirty routing partners, energy-conserving
finite work lifts and retained rows give a local implementation. The
parameter order fixes the gate structure before choosing ell, Q and the
work dimension, avoiding a circular clock-error budget.

The full raw-space law is

\[
 H=H_0+H_{prop}\ge0,\qquad [H_0,H_{prop}]=0.
\]

The time-independent propagation terms have both forward and adjoint
matrix elements. A guarded loader supplies one legal active history,
with a finite interval during which the prepared thermal targets stay
on a fixed row. The later program implements

\[
 T=\exp(-i\tau_{old}H_{1764}/\hbar)
\]

on the entire old raw apparatus, including its old thermal defects.
This exact mathematical unitary is defined analytically; its potentially
very large gate list has not been enumerated or simulated.

The new law replaces the old interaction dynamics. It preserves the
specified endpoint interface, not the old trajectory, clock time or
interaction-energy partition. The old H_1764 is not added a second time
to the new physical Hamiltonian.

On the initialized-counter subspace, the completed funded T leaves the
new work head unchanged, even with the correlations left by preparation.
[PREPARATION.md](PREPARATION.md) gives the full joint proof, the finite
preparation/output windows and the complete acceptance predicate. The
conditional inherited capture bounds remain p>1/75000 and unwanted
accepted fraction<1/10^6, with an explicit additional small error.
Those numbers still describe L1 squared norms and reduced states, not
frequencies of realized physical events.

## 4. Energy and the remaining initial condition

The initial mean and variance use every physical row, donor, counter,
work copy, cursor, fuel state and interaction term. They include thermal
defects without dropping their potentially large energies. Bare energy,
interaction energy and total generator energy are distinguished.

For a general initially thermal subsystem S and all remaining resource
factors A, an energy-conserving unitary from a product input obeys

\[
 \beta_0 W+\Delta S_A
 =D(\rho'_S\Vert\tau_S)+I(S:A)'\ge0,
\]

where W is the decrease of the resource's bare mean energy. The entropy
term prevents a battery or controller from acting as an uncounted entropy
sink. Specializing A to fuel alone is justified only on an acquisition
interface for which the logical input is an unchanged spectator.

A complete common-temperature Gibbs input of H_0 would be stationary
for this H. So would any state commuting with H. The construction runs
because its fuel inversion and product/contact boundary supply full-H
nonstationarity. [NATIVE.md](NATIVE.md) separates this addition from the
unchanged native U_rec and identifies the remaining fuel preparation,
material coupling, readout and reset obligations.

The status, immutable inputs, proof-byte manifest and actual checks are
recorded in [VALIDATION.md](VALIDATION.md). No new scientific executable,
verifier or simulation was run. The parallel #1762 capacity result is
not substituted into this different resource class.

[prior]: https://github.com/mathorn1973/twist-j/tree/6670ac274888927be3429a463966da41ca8d2e8b/notes/C-THERMAL-WORK-CLOCK-BOOTSTRAP-N
