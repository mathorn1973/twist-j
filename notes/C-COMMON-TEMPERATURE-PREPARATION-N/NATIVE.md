# Native-law boundary and the remaining inverted fuel

**NON-CANONICAL, L1, conditional analytical candidate-T.**
Independent mathematical acceptance is pending.

## 1. What this preparation actually changes

The fixed input is [#1764][prior] at
6670ac274888927be3429a463966da41ca8d2e8b. Its supplied hot and cold
Gibbs factors are replaced by a preparation from one common inverse
temperature beta_0, with beta_0 epsilon=ln 2. The target onsite gaps do
not change during that preparation.

Each required thermal target is paired with a physical donor of the same
dimension and degeneracies but a different fixed energy scale. A funded
state exchange prepares the target distribution and moves its old state
to the donor. All those donors initially have the same temperature beta_0.
No variable gap, external switch, discarded donor, or infinite bath is
hidden in the exchange.

The hot donor has a smaller gap than its target. The cold donors have
larger gaps than their targets. Their populations become respectively hot
and cold Gibbs populations when placed on the fixed target spectra. This
is an operation on the target states, not merely a change of temperature
notation: target input and output populations differ. The joint target
product, including the preceding physical work ladder and every preceding
clock site, is proved in [PREPARATION.md](PREPARATION.md).

The mean bare-energy increase of each target/donor pair is nonnegative.
Its actual value, the retained entropy and correlations, and the complete
Hamiltonian energy account are in [ENVIRONMENT.md](ENVIRONMENT.md).
The entire finite environment is depleted or correlated; it is not an
implicitly replenished reservoir.

## 2. What has to be added

The new initial resources are explicitly separated:

- All new nonlogical hardware other than one fuel qubit is in a Gibbs
  state at the common finite temperature beta_0. The corresponding
  spectra, degeneracies, dimensions and initial product structure are
  specified. Equal temperature does not mean equal gaps or equal entropy.
- The fuel qubit has gap (2Q+2ell)epsilon and excited population
  1-delta_f, with delta_f=2^-96. This is supplied inversion. It is not
  a positive-temperature Gibbs state, and its preparation is not proved.
- New clock sites and counter sites have gap ell epsilon and are initially
  Gibbs at beta_0. Their near-ground populations follow from their large
  physical gaps at that temperature; an additional low temperature is
  not supplied. Those gaps and all copies remain in the resource account.
- The new work ladder is initially Gibbs at beta_0, not initially charged
  at its central level. A resonant fuel reaction shifts its admitted
  low-energy distribution upwards by 2Q and creates both clock entries.
- The old admitted logical input and its arbitrary reference remain an
  input interface. Their purity or correlations are not a thermal fuel.

Thus the temperature contrast and the specific cold states of #1764 are
produced within the new law. The inverted fuel, the common-temperature
Gibbs product, the manufactured spectra and the product/contact boundary
are not produced from an earlier stationary state in this model.

The large local Hilbert spaces and arbitrary exact gate matrix elements
are declared additions. Mathematical locality here means finite support
and bounded geometric range of each term. It does not establish a
bounded small onsite dimension, achievable atomic couplings, a realistic
manufacturing cost, or robustness to laboratory errors.

## 3. One complete law, with a changed trajectory

[HAMILTONIAN.md](HAMILTONIAN.md) defines a single positive, static local
Hamiltonian H=H_0+H_prop, with [H_0,H_prop]=0 on every raw state.
The fuel reaction, loader, paid preparation, retained rows, computation
and output tail belong to this same law. No externally timed change of
Hamiltonian is used.

The subsequent target unitary is the exact finite endpoint

\[
 T=\exp(-i\tau_{old}H_{1764}/\hbar)
\]

on the entire pinned old raw apparatus, including its thermal defects.
Its matrix is compiled into the new finite word. The old interaction
Hamiltonian is therefore an input defining T; it is not an additional
physical summand of the new Hamiltonian. Counting both would be incorrect.
The old onsite spectra remain part of the new H_0.

On the correctly initialized counter subspace, T commutes with the old
bare energy and the completed funded operation leaves the new work head
unchanged even when that head is correlated with the old apparatus and
donors. This establishes the old endpoint channel after the new
preparation. It does not preserve the old continuous trajectory, clock
times, post-read retention interval, or physical interaction-energy
partition.

The gate list has a forward program order. Every Hermitian propagation
term also contains its adjoint and allows reverse propagation. This is
not a strictly one-directional Hamiltonian. The earlier forward-only
controlled-filter statement concerns the object-level circuit, not the
absence of reverse matrix elements in a closed physical generator.

## 4. The nonstationarity that remains

The actual initial state commutes with the additive bare H_0 under the
fixed-charge logical promise. No supplied coherence between distinct bare
energies of the new work ladder or fuel qubit is needed. Diagonal inversion
and the fixed resonant interaction nevertheless give unequal populations
to the two configurations joined by the launch term. The resulting
nonzero full-H commutator is proved in ENVIRONMENT.md.

Absence of bare-energy phase coherence is not stationarity for the full
interacting Hamiltonian. The initial state has the required full-H
nonstationarity because the fuel inversion and product/contact condition
are supplied. Preparing them in a material device is a remaining task.

For every closed time-independent H,

\[
 [H,\rho_0]=0\implies e^{-itH/\hbar}\rho_0e^{itH/\hbar}=\rho_0.
\]

In this construction a complete common-temperature Gibbs state of H_0
is stationary too, since [H,H_0]=0. This last comparison concerns the
complete thermal input, including all factors to which it is applied.
An arbitrary pure logical input cannot silently be included in that
hypothesis or spent as an uncounted resource.

The relative-entropy identity in ENVIRONMENT.md includes all nonthermal
factors in its general resource subsystem. Only where the logical
interface is proved to be an unchanged spectator is its specialization
to fuel alone justified. A mean-work inequality without the resource's
entropy change would generally omit part of the cost.

## 5. Exact Gibbs preparation versus exact purity

The donor populations give exactly the requested full-rank Gibbs factors
on the good buffered component. The actual autonomous finite-time input
and output additionally retain all fuel, work-tail, counter and clock
defects, with explicit trace-distance bounds. No actual defect is removed
from the Hamiltonian or assigned zero energy.

Every new thermal factor and the inverted fuel state are full rank.
This preparation does not create exactly pure blank registers from a
finite full-rank resource. The inherited approximate ready-register
preparation remains approximate. A pure admitted logical input is kept
separate from that full-rank statement and is not erased to improve it.

The finite preparation window and final output window eventually close
under the same reversible law. Useful reset with retained output,
replenishment of the inversion, a physical detector, and a law for
individual events remain outside this candidate.

## 6. What unchanged U_rec supplies

Public Canon v105 supplies the native transfer and receiver model within
its stated scope. Its conserved charges and selected spectral energy do
not automatically equal the positive onsite energies assigned to this
added apparatus.

Under the literal spectator extension U_rec tensor I_aux, the auxiliary
marginal is unchanged, including for correlated inputs. That extension
cannot create the new thermal contrast, exchange a donor and target,
charge the new work head, or populate the new clocks. A coupling which
does so is an additional law to be specified and checked.

The present thermal spectra, high-gap counter, inverted fuel, resonant
reaction, funded controlled gates and continuous Hamiltonian are such
additions. No encoding or intertwining theorem deriving them from the
unchanged native law or from J alone is supplied. This comparison does
not exclude every possible future native realization.

The parallel [#1762][parallel] concerns capacity in its own fixed thermal
resource class. Its two-pair weight 7/15 is not imported here; adding a
high-energy inverted fuel and scaled-gap donors changes the class.
This construction claims neither that optimum nor a better optimum.
Its joint-input and retrigger cautions remain applicable.

[prior]: https://github.com/mathorn1973/twist-j/tree/6670ac274888927be3429a463966da41ca8d2e8b/notes/C-THERMAL-WORK-CLOCK-BOOTSTRAP-N
[parallel]: https://github.com/mathorn1973/twist-j/pull/1762
