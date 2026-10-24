# Preparing the clock source from a finite thermal environment

**NON-CANONICAL, L1, conditional analytical candidate-T.**
Independent mathematical acceptance is pending. Public claim:
[#1757](https://github.com/mathorn1973/twist-j/issues/1757).

The previously supplied occupied source can be replaced by a specified
finite mixed environment. One static local Hamiltonian first charges the
actual source, creates its loading cursor, holds the old apparatus ready
during an approximate preparation window, and then executes the complete
capture word. The environment has an active weight of 4/15. All inactive
branches are retained and the final unconditioned throughput includes that
factor.

The remaining initial resource is explicit: stationary bare Gibbs marginals
and empty apparatus cells form a nonstationary input for the coupled total
Hamiltonian. This is acquisition of the source from a concrete environment,
not preparation of every initial resource from global equilibrium.

## 1. Environment and local reaction

Use two qubits with bare Hamiltonians H_h=3 epsilon n_h and H_c=epsilon n_c.
Their initial density operators are

\[
 \tau_h=\frac23|0\rangle\langle0|+\frac13|1\rangle\langle1|,\qquad
 \tau_c=\frac45|0\rangle\langle0|+\frac15|1\rangle\langle1|.
\]

These are Gibbs states at beta_h=log(2)/(3 epsilon) and
beta_c=log(4)/epsilon. They are independent of the previous data/reference
input. The old source s=c_0, the rest of the main clock, and the new loader
are empty. Data fuel, work and the completion latch remain supplied as in
the fixed input [#1756 at 901c400f][prior].

The conversion operator is

\[
 B=\sigma_h^-\sigma_c^+\sigma_s^+\sigma_{t_0}^+.
\]

It connects h1 c0 s0 t0=0 with h0 c1 s1 t0=1 and conserves the bare
energy: 3 epsilon equals epsilon+epsilon+epsilon. No new occupied timer is
supplied. The same reaction creates both the actual source excitation and
the loader excitation.

The initial environment weights in order 00,01,10,11 are (8,2,4,1)/15.
Only the 10 sector launches. Its weight is

\[
 q=\frac4{15}.
\]

The other sectors stay inactive and are never omitted from the density
operator. Thermal weights here are specified L1 state data, not a derived
law of individual observed occurrences.

## 2. Preparation and handoff under one law

Let a be the input candidate's runway parameter, L=2a its main completion
index, and 2L its old main-path length. Add L loader sites in a U-shaped
path and extend the old main identity tail to main index 3L. The full
active history has K=4L transitions.

After conversion, the loader moves while the original source remains
occupied. Its last hop is controlled by the source occupation. The first
main-clock hop is controlled by the loader endpoint. These two local
guards permit the handoff and prevent the loader from retreating while
the main cursor is away. There is no external switch between preparation
and computation.

[HAMILTONIAN.md](HAMILTONIAN.md) gives all raw-space positive edge terms,
local history-indicator potentials and the onsite energy. The full law is

\[
 H=H_0+H_{\rm prop}\geq0,\qquad [H_0,H_{\rm prop}]=0,
\]
\[
 a_j=\frac{g}{K+1}\sqrt{(j+1)(K-j)}.
\]

It is not g times the number of cursor excitations minus hopping: there
are two cursor/source excitations after conversion but only one history
position. The explicit positive-block construction is essential.

Each term acts on at most seven qubits within Manhattan radius four.
The maximum term valence is six. The complete Hilbert space, off-path
strings and reverse Hermitian edges are included.

With theta=gt/[hbar(K+1)], the active history weights are binomial with
parameter p=sin^2(theta). For the first interval 1/16<=p<=1/8, good
histories have an occupied source, an interior loader, a disabled main
handoff and exactly unchanged old data/clock/latch input. Their bad weight
is bounded by

\[
 \delta\leq(15/16)^{4L}+(625/768)^L\leq2(5/6)^L.
\]

The active full-state trace distance to the explicit source-ready product
is at most sqrt(delta)<10^-30. The unconditioned state is within
q sqrt(delta) of the corresponding retained mixture, with active weight q
and the three original failures. The local mathematical ready predicate
n_s(1-n_t_last) has weight at least q(1-delta). It is not asserted to be a
built physical heralding instrument.

This prepares the actual old source on the good component, not merely a
renamed occupied environment site. It does not prepare that source with
unit unconditioned weight or halt the entire apparatus. See
[PREPARATION.md](PREPARATION.md).

## 3. Inclusive energy and remaining nonstationarity

Let E_old count the original sharp data/work/fuel excitations and put
D=E_old+1, including the initialized completion latch. Initially the full
mean energy is

\[
 \boxed{\langle H\rangle=\epsilon(D+6/5)+\frac4{15}g.}
\]

The environment's bare contribution is 6 epsilon/5. Its local positive
input/contact partition has mean 6 epsilon/5+4g/15. At the exact endpoint
that partition has mean 2 epsilon/3; the remainder receives
8 epsilon/15+4g/15. This counts both the two created bare excitations and
the propagation energy. It is a specified partition of positive Hamiltonian
terms with a shared boundary, not a minimum manufacturing-work claim.

All initial marginals are stationary for their bare energies, and
[H_0,rho_in]=0. Nevertheless

\[
 \boxed{\|[H,\rho_{\rm in}]\|_1=2qa_0=\frac8{15}a_0>0.}
\]

Only the conversion term fails initially to commute. The supplied product
state and fixed contact therefore already contain full-H nonstationarity.
[ENVIRONMENT.md](ENVIRONMENT.md) derives the full mean, variance, energy
distribution, depletion, entropy and correlation account. No cold vacuum,
ready data fuel or joint initial-state acquisition is treated as free or
derived merely because its mean energy has been recorded.

## 4. Whole-input output and scope

At tau=pi hbar(K+1)/(2g), the active branch executes the entire target word
exactly, up to a common phase. The old latch and final flag reject every
inactive branch and unfinished prefix. Throughout the derived output
window the reduced accepted operator is exactly

\[
 \sigma_{\rm acc}(t)=q\,w(t)\,\sigma_{\rm ideal}.
\]

Consequently the inherited whole-input lower bound becomes greater than
1/75000; it is not the former 1/20000. The normalized unwanted fraction
remains below 1/10^6 and the accepted occupied-memory/reference SWAP is
unchanged, conditional on the fixed inherited premises.

The unchanged native U_rec does not contain these thermal qubits or their
reaction. [NATIVE.md](NATIVE.md) identifies every new assumption, the
difference from a Gibbs state of full H, and the remaining preparation
boundary. The environment is finite and depleted, not a replenished heat
bath or a repeatable autonomous engine. Coupling calibration, material
implementation, physical readout and occurrence, useful reset and
preparation of the supplied environment/cold apparatus remain open.

[VALIDATION.md](VALIDATION.md) records fixed inputs and proof custody.
This is an analytical construction; no new scientific executable or
simulation was run.

[prior]: https://github.com/mathorn1973/twist-j/tree/901c400f85c427752e2e4367afb6cd00e59ac8c8/notes/C-LOCAL-CLOCK-SOURCE-N
