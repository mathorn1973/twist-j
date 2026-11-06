# A local source for an initially inactive clock

**NON-CANONICAL. L1. Conditional analytical candidate-T.**
Independent mathematical acceptance is pending. Public claim:
[#1755](https://github.com/mathorn1973/twist-j/issues/1755).

A finite local source can load a running clock and execute the funded capture
experiment under one fixed positive Hamiltonian. The construction changes
its clock carrier: one supplied source excitation enters an otherwise empty
cursor line. The isolated empty device is stationary. An explicit idle
runway gives a high-weight interval in which the clock has been loaded but
the data experiment has not started. The same Hamiltonian later executes
that experiment and supplies a finite accepted-record interval.

The supplied excitation and its contact are not stationary for the FULL
Hamiltonian. Their complete initial energy cost is epsilon+g, including
the local propagation contribution, rather than only the bare epsilon.
This is a concrete local source/interface and an inclusive energy account,
not preparation of a moving closed world from a stationary closed world.

## 1. Fixed target and changed clock

The target is the sharp-energy local circuit in
[SHARP.md of #1754 at 89f69e4](https://github.com/mathorn1973/twist-j/blob/89f69e40f6ccfd950bf2e6c446ec38bc51f7f71b/notes/C-PHYSICAL-BATTERY-HAMILTONIAN-N/SHARP.md).
It includes charging the initially empty DATA battery from Q_*=4259865
excited fuel qubits, the complete capture/filter word, retained rejected
histories and the exact accepted physical/reference channel. Its inherited
source and spectral conclusions remain conditional. It is not altered here.

Let R_* be its actual local line-gate count and S_* its line width. Reuse
its fresh data rows and N=R_*(S_*+3)-1 gate-labelled cursor transitions.
Set A=N+1. Add A idle transitions before that word and one local completion
latch transition after it. Completion is at L=2A; a further L idle
transitions give M=4A in total.

The physical clock now consists of M+1 qubits. Site zero is the source,
initially occupied, and all other cursor sites are empty. The added latch
is a dual-rail pair in |10>, costing one more epsilon of ready-state energy.
It is swapped to |01> only at completion, and reversed on a reverse
crossing. This replaces the old domain-wall completion bit correctly.

## 2. One local Hamiltonian including the source

Write n_j=|1><1| on cursor site j and

\[
 T_j=\sigma^+_{j+1}\sigma^-_j\otimes G_j,
 \qquad a_j=\frac{g}{M+1}\sqrt{(j+1)(M-j)}.
\]

The first A labels are identity, including the data-free source bond.
The complete Hamiltonian is

\[
 H=H_0+H_{\rm prop},\qquad
 H_0=\epsilon(N_{\rm data}+N_{\rm latch}+N_{\rm cursor}),
\]
\[
 H_{\rm prop}=gN_{\rm cursor}-\sum_{j=0}^{M-1}a_j(T_j+T_j^*).
\]

Here the three N symbols denote excitation-number operators for the data, latch and cursor registers. [HAMILTONIAN.md](HAMILTONIAN.md) proves full-space positivity by writing it
as positive edge terms a_j(n_j+n_(j+1)-T_j-T_j*) and nonnegative onsite
corrections. Both H_0 and H_prop are positive and commute. Cursor number
and data/latch excitation number are separately conserved. The bare clock
charge therefore comes from the supplied source, not from the data battery
or an omitted driver.

All qubits have local dimension two. Each propagation term involves at
most seven qubits within Manhattan radius four. Term valence is at most
four, including onsite terms. The first source bond is just an ordinary
two-qubit exchange. All couplings are fixed; there is no externally switched
preparation-to-computation boundary in the asserted evolution.

The all-empty cursor is exactly inactive under this law. With the source
occupied, the only initially noncommuting coupling is the first local bond.
For any admitted mixed data/reference input rho_D,

\[
 \|[H,\rho_{\rm initial}]\|_1=2a_0,
 \qquad \operatorname{Var}(H)=a_0^2=\frac{g^2M}{(M+1)^2}.
\]

The first identity, not variance alone, establishes nonstationarity.

## 3. What actually gets prepared

With theta=gt/[hbar(M+1)], the source population is exactly

\[
 p_{\rm source}(t)=\cos^{2M}\theta.
\]

During the first interval in which

\[
 \frac1{16}\leq\sin^2\theta\leq\frac18,
\]

the clock lies in the idle runway, with the source empty and the complete
data input unchanged, except for a bad weight bounded by

\[
 \delta_{\rm prep}\leq
 \left(\frac{15}{16}\right)^{4A}
 +\left(\frac{625}{768}\right)^A
 \leq2\left(\frac56\right)^A.
\]

[PREPARATION.md](PREPARATION.md) gives an explicit normalized runway
wavepacket whose product with the untouched data has full-state trace
distance at most sqrt(delta_prep). This includes arbitrary passive reference
correlations. No actual projection onto the runway is required for that
approximation statement. The finite construction has A>=1024, so the
full-state error is below 10^-30 by the displayed exact bounds.

This is preparation of a moving cursor packet, not an exact intermediate
preparation of the previous domain-wall clock state or a sharp cursor at
site one. The latter is not reached in this chain. No exact newly loaded
plateau or permanent one-way halt is possible under this finite fixed law;
the appropriate statements are the finite approximate window and exact
final endpoint.

## 4. Energy and the remaining source assumption

The source/input-interface operator

\[
 H_{\rm launch}=(\epsilon+v_0)n_0+h_0,\qquad
 v_0=g-a_0,
\]

is positive and supported only on the source and the adjacent cursor cell.
The remainder H-H_launch is positive too. Initially its cursor/interface
energy is epsilon+g; at the final endpoint H_launch annihilates the state.
[SOURCE.md](SOURCE.md) gives the exact transfer and explains why this is a
partition of Hamiltonian terms with a shared boundary, not two uncoupled
subsystems at intermediate times.

If E_old=n_*+A_*+Q_* is the prior circuit's sharp initial data excitation
count, the complete new initial mean energy is

\[
 \boxed{\langle H\rangle=\epsilon(E_{\rm old}+2)+g.}
\]

The extra two excitations are the source and the completion latch. Empty
rows, the full cursor and both battery/fuel banks count as hardware. Their
ready-state purity, the initially charged data fuel, the localized source
excitation and the exact couplings are supplied initial/model data.

No superposition of the source qubit's two bare-energy levels is needed.
Its isolated |1> state is stationary. Nevertheless its localization next
to the permanently present contact fixes a nonstationary boundary for H.
The global energy distribution is explicitly binomial. Its dependence on
the full clock spectrum is not erased by the locality of the term causing the initial
commutator. A completely H-stationary input cannot be transformed into this
ready state by evolution or a unitary conserving H.

## 5. Execution, readout and native scope

At tau=pi hbar(M+1)/(2g), the cursor is at its far endpoint, the source is
empty, the completion latch is true, and the entire target word has been
executed exactly, up to a common phase. No clock outcome is selected.
A physical read uses the fixed latch rail AND the final acceptance flag.
The new identity tail gives the exact reduced-channel relation
sigma_acc(t)=w(t) sigma_ideal. The inherited margins p>1/20000 and unwanted
fraction<1/10^6 hold conditionally for pi/3<=theta<=2pi/3. A separately
specified endpoint-postselection continuation bounds wrong receiver weight
by (3/4)^L for delays up to tau/3. These are the new longer clock's times.
There is no occurrence law or implemented readout instrument in this claim.

[NATIVE.md](NATIVE.md) distinguishes this added qubit/source law from the
unchanged original update and from its occupation/spectral readings. The
old domain-wall ready state already had only one initially noncommuting local term. The
new result is the conserved, energy-priced injection into an inactive
vacuum plus a quantified loading interval; localization by itself is not
new, nor is it a removal of every initial-condition requirement.

[VALIDATION.md](VALIDATION.md) records fixed inputs, proof-file custody,
actual checks, remaining assumptions and decisive falsifiers. This is an
analytical candidate, not a material device or a native derivation.
