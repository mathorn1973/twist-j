# Physical batteries, funded preparation and one local Hamiltonian

**NON-CANONICAL. L1. Conditional candidate-T; independent acceptance pending.**
Public claim: [#1753](https://github.com/mathorn1973/twist-j/issues/1753).

An explicit finite qubit apparatus can implement the complete capture word
with a battery whose energy is a positive onsite part of the very same
Hamiltonian. The battery starts empty. Its charging is included and paid by
a specified finite fuel source. Two output contracts require different fuel:

| Contract | Energy account and required output | Supplied fuel |
| --- | --- | --- |
| Coherent interface from #1748 | Spatial-square ledger; retain the predecessor's complete funded joint output and its comparison with an ideal product | Charged basis bank plus correlated coherent donor blocks |
| Sharp interface from #1752 | Clock/auxiliary/pulse ledger; exact accepted object/carrier/memory/reference reduced channel | Charged basis bank; no initial coherence across bare-energy sectors |

These are different physical energy choices and output promises. A no-go for
preparing the pure coherent battery of the first row does not exclude the
second row. Both use a localized clock that is nonstationary for the full
Hamiltonian. Neither starts from a stationary ground state of the complete
running apparatus.

This is an added Hamiltonian model, not a derived native TWIST-J implementation
or an experimental device. Unlike the encoded ledger in #1751, the battery
energy here is an actual partial sum of physical onsite terms, and every
elementary interaction conserves their full sum. Initial resources, exact
couplings, clock readiness and geometry remain supplied data. The finite
resource bounds are enormous.

## 1. Common Hamiltonian and complete endpoint

Give every physical data, battery, fuel and work qubit the same positive gap:

\[
 H_0=\epsilon\sum_{i\in\mathrm{data\ sites}}|1\rangle\langle1|_i.
\]

The physical history-clock qubits have zero bare splitting; their energy is
included through the propagation interactions. Define

\[
 \boxed{H_{\rm tot}=H_0+H_{\rm prop}},\qquad
 H_0\ge0,\quad H_{\rm prop}\ge0,\quad[H_0,H_{\rm prop}]=0.
\]

[COMPILATION.md](COMPILATION.md) supplies exact excitation-preserving gates
on at most four neighboring qubits, including charging and all dirty-state
extensions. [HAMILTONIAN.md](HAMILTONIAN.md) routes them through fresh rows
and a domain-wall clock on a two-dimensional lattice. Its propagation terms
act on at most eight qubits within Manhattan radius four, with bounded
interaction valence. No target-sized Hilbert space is hidden inside one site.

For K clock transitions, the weights are

\[
 a_k=\frac{g}{K+1}\sqrt{(k+1)(K-k)}.
\]

The positive diagonal correction makes the legal history Hamiltonian
\(gI-[2g/(K+1)]J_x\). At

\[
 \tau=\frac{\pi\hbar(K+1)}{2g},\qquad \epsilon=4g,
\]

it executes the entire compiled word with common phase -i. The bare factor
\(\exp(-iH_0\tau/\hbar)\) is exactly identity because the excitation spectrum
is integer. This equality holds for the complete prepared state, including
rejected histories, the occupied old memory and arbitrary reference inputs.
No clock outcome is postselected.

A fixed battery bank consists of the battery-designated columns in every
data row. Its actual energy is

\[
 H_B=\epsilon\sum_{i\in\mathrm{battery\ bank}}|1\rangle\langle1|_i,
 \qquad H_{\rm rest}=H_0-H_B\ge0.
\]

At all physical times,

\[
 \Delta\langle H_B\rangle+\Delta\langle H_{\rm rest}\rangle=0,
 \qquad \Delta\langle H_{\rm prop}\rangle=0.
\]

There is no negative counterterm canceling the storage energy. At restored
code checkpoints H_B equals the intended ladder energy. During routing,
H_B still denotes those same physical cells, even if the abstract register
is temporarily represented elsewhere. The final endpoint has the exact
specified register interpretation.

## 2. Coherent interface: an explicit consumed source

Let q_max bound the preceding finite system/clock ledger. Choose

\[
 Q=5^{2r}\ge\max(1,q_{\max}),\qquad
 \ell=2r+22,\qquad L=5^\ell=Q5^{22}.
\]

The battery code uses \(B_{\max}=L+2Q-1\) qubits in one circuit row.
A sharp charge bank of Q excited qubits supplies the offset energy
\(\epsilon Q\). A second bank has L-1 identical-gap qubits, arranged in
blocks of widths \(4\cdot5^j\), with the prescribed initial states

\[
 |\eta_j\rangle=\frac1{\sqrt5}\sum_{a=0}^{4}
 |1^{a5^j}0^{(4-a)5^j}\rangle,
 \qquad j=0,\ldots,\ell-1.
\]

The product is between these blocks. Inside a block the qubits are
correlated; it is not a bank of independently prepared single-qubit
superpositions. Their relative phases to the fixed interactions and initial
clock boundary are part of the source specification.

[FUEL.md](FUEL.md) defines disjoint equal-energy transpositions that send

\[
 |0\rangle_B\,|1\rangle^{\otimes Q}\bigotimes_j|\eta_j\rangle
 \longmapsto
 |b_L\rangle_B\,|0\rangle_F,
 \qquad
 |b_L\rangle=\frac1{\sqrt L}\sum_{n=0}^{L-1}|Q+n\rangle.
\]

Each arrow is extended to a total unitary and compiled into the same
energy-preserving local gate alphabet. The source has exactly

\[
 \boxed{\langle H_F\rangle=\epsilon\left(Q+\frac{L-1}{2}\right)},
 \qquad
 \boxed{\operatorname{Var}(H_F)=\epsilon^2\frac{L^2-1}{12}}.
\]

At the charging endpoint the battery acquires this energy distribution and
the source is ground-state depleted. Its coherence relative to total fuel
energy has entropy \(\log L\), and its nonzero energy-difference modes are
precisely \(\epsilon k\), \(0<|k|<L\), with norms \((L-|k|)/L\).
Averaging an unknown common phase removes these modes. Their preparation
cannot be replaced by declaring an unspecified Fourier operation free.

## 3. Pure coherent preparation cannot use only stationary resources

If a complete initial state commutes with H_0 and evolution conserves H_0,
its reduced battery remains stationary for H_B. For the nominated pure
state b_L, every stationary battery state obeys the sharp bound

\[
 D(\rho_B,|b_L\rangle\langle b_L|)\ge1-\frac1L.
\]

This remains true with degeneracies, occupied helpers and arbitrarily much
incoherent charge. In this model the bare-degenerate physical clock cannot
supply the missing H_0 modes. It has a separate nonstationary resource with
respect to H_prop, which schedules the experiment but does not create bare
energy coherence.

For the stated pure-source/product boundary conditions, an exact pure b_L
also requires fuel variance at least \(\epsilon^2(L^2-1)/12\) and energy
asymmetry at least \(\log L\). FUEL.md gives the assumptions and proof,
including why a finite pure source returned exactly unchanged cannot serve
as the sole coherence donor. These are restrictions on this pure coherent
interface. They do not prohibit every detector with an incoherent battery
or a different reduced-output requirement.

The source blocks are therefore the exact added initial resource. Their
acquisition from another physical source remains open. Moving them into a
new box and calling that box a preparation device would not eliminate the
obligation.

## 4. Cost of the coherent interface, including readiness and time

Let n_S be the registerwise binary information width of the finite target.
Its physical code uses n_S dual-rail pairs and Q tally qubits. With the
battery and both fuel banks, the core width and compiler work are

\[
 P=2n_S+Q+B_{\max}+Q+L-1,\qquad A=P,\qquad S=3P.
\]

Every clean work pair starts with one excitation, so the initialized
information/work energy is \(\epsilon(n_S+A)\), not zero. For
\(\nu=1+L_{\rm prog}+h\) macros, default h=0, the explicit gate bound is

\[
 R_g\le128\nu P^3 4^P,\qquad
 K=R_g(S+3)-1.
\]

The complete layout has \((R_g+1)S\) qubits with gap epsilon and K clock qubits.
All additional rows are initially empty but count as hardware and ready
storage. In particular the full battery bank has
\((R_g+1)B_{\max}\) qubits and raw capacity
\(\epsilon(R_g+1)B_{\max}\); the one-active-row code uses only the ladder
capacity \(\epsilon B_{\max}\).

For the specified source with initial q=0, the complete initial energy is

\[
 \langle H_{\rm tot}\rangle
 =\epsilon\left(n_S+A+Q+\frac{L-1}{2}\right)+g,
\]

and its variance is

\[
 \sigma^2=\epsilon^2\frac{L^2-1}{12}
                 +\frac{g^2K}{(K+1)^2}.
\]

Both are conserved. Thus the broad coherent source also contributes to
physical timing sensitivity: modulo a common phase, the complete endpoint
vector changes by at most \(|\delta t|\sigma/\hbar\). The former clock-only
variance bound from #1751 cannot be reused for this energy-coherent output.
Exact coupling precision, fabrication, source cooling and reset costs are
not quantified by the gate count.

## 5. Sharp interface: basis fuel and a newly derived read window

[SHARP.md](SHARP.md) takes the changed ledger and accepted physical channel
of [#1752 at e19b071](https://github.com/mathorn1973/twist-j/blob/e19b07183c3e4841e18c8913de7c4c83429b94f3/notes/C-FINITE-HAMILTONIAN-READOUT-N/PROOF.md).
It counts inner clock, nonzero auxiliary records and pulse presence; object
positions, coins and unknown messages are degenerate. The inner padded
clock has M_*=3276820 transitions and the auxiliary bound is R_aux=983045,
so Q_*=M_*+R_aux=4259865. These are the predecessor's selected account,
not a derivation of kinetic energy from the original transfer law.

The new physical battery uses Q_* identical-gap qubits as a thermometer,
with Q_*+1 valid levels. It begins empty. A separate Q_*-qubit fuel bank
begins fully excited. A conserving transposition charges the battery:

\[
 |0^{Q_*}\rangle_B|1^{Q_*}\rangle_F
 \longmapsto |1^{Q_*}\rangle_B|0^{Q_*}\rangle_F.
\]

This permutation and a fully specified, energy-conserving endpoint unitary
are compiled by the same sectorwise local compiler. The initial fuel has
energy epsilon Q_* and zero bare-energy variance. A preparation-only
instance ends with an exactly charged pure basis battery. In the combined
experiment the endpoint battery is correlated with the retained clock and
auxiliary records. It is not an unchanged pure product battery. On accepted
histories, its label and the system tally depend only on those traced
auxiliary indices. The accepted physical/reference channel is therefore
exactly the ideal channel, with no coherent-battery approximation.

With n_* information digits, core width P_*=2n_*+3Q_*, A_*=P_* clean work
pairs and line width S_*=3P_*, the two-macro compiler gives

\[
 R_*\le256P_*^3 4^{P_*}.
\]

The one-active-row battery capacity is epsilon Q_*. The complete battery
bank across the R_*+1 rows has capacity epsilon(R_*+1)Q_*; the empty
copies are included in the hardware count. All the initial information
and work excitations are charged readiness resources too.

[PADDED.md](PADDED.md) appends a physical clock-only tail after the last
row transfer. Put k=R_*(S_*+3)-1 and K_*=2k. Completion is read by the
conjunction of the final flag and the physical clock bit c_k. This matters:
arbitrary local compiler prefixes need not leave the decoded flag zero.
The tail applies identity to the entire completed data, including memory,
battery and work. For this new local Hamiltonian, set

\[
 \theta(t)=\frac{gt}{\hbar(K_*+1)},\qquad
 w(t)=\sum_{j=k}^{2k}\binom{2k}{j}
      \sin^{2j}\theta(t)\cos^{2(2k-j)}\theta(t).
\]

After tracing the clock and retained helpers, and applying the fixed mathematical decoding of the final-row information registers, the accepted physical state obeys the exact linear-map identity

\[
 \boxed{\sigma_{\rm acc}^{\rm local}(t)=w(t)\sigma_{\rm acc}^{\rm ideal}}.
\]

For pi/3<=theta(t)<=2pi/3, its incomplete weight is at most (3/4)^k,
less than 10^-30. The inherited explicit acceptance margin still gives
p>1/20000, unwanted bound-band fraction below 1/10^6, and exact occupied
memory/reference SWAP, conditional on the source/filter premises. These
are newly derived times for the compiled physical apparatus; they are not
the numerical gate-level times of #1752.

At t_*=pi hbar(K_*+1)/(2g), completion is exact. After a mathematical
accepted endpoint read with incoming label 1, the same Hamiltonian bounds
wrong-memory weight by (3/4)^k for delays up to
pi hbar(K_*+1)/(6g). This continuation uses a stated projection as a
mathematical contract; no physical occurrence or readout mechanism is added.
The tail keeps the original native law off, and eventually recurs.

The whole initial input is sharp for H_0 but nonstationary for H_tot:

\[
 \langle H_{\rm tot}\rangle=\epsilon(n_*+A_*+Q_*)+g,
 \qquad
 \operatorname{Var}(H_{\rm tot})=
       \frac{g^2K_*}{(K_*+1)^2}>0.
\]

Consequently no initial coherence between different H_0 energies is needed
for this interface. The initialized clock still supplies nonstationarity
relative to the actual generator. The bare-energy phase is common at all
times, so this route does not require epsilon=4g. Making a stationary
complete input into these working clock resources by a unitary commuting
with H_tot remains impossible. Charged fuel acquisition, basis readiness,
clock preparation and a useful reset are exposed initial obligations.


## 6. Meaning for the original law

[NATIVE.md](NATIVE.md) audits the pinned Canon and predecessor scopes.
The original occupation model supplies the target U_rec and charge current;
its active total charge is 10I and added helpers are spectators. Merely
appending a battery to that law leaves it unchanged. Its supplied spectral
packets can have spectral-energy coherence, but an energy-compatible transfer
from them into these donor blocks has not been proved.

The Canon already constructs a supplied coherent spectral-energy source and
a positive generator H_0+K. Its source preparation and full locality were
explicitly outside that result. Here finite onsite storage and locally
conserving interactions are constructed for the new hardware encoding.
The energy dictionary, the respective fuel states, ready states, qubit interactions and
continuous-time law are additional model data. Native physical positions
are still encoded values, not identified with the new hardware lattice.

For the coherent interface, the h=0 endpoint conditionally inherits the complete funded output of #1748
and the source/selectivity conclusions of #1746. An h>0 suffix keeps only
its stated memory-endpoint guarantee, not an unproved continued binding
bound. A preparation-only instance has an exact pure charged-battery endpoint;
the combined experiment includes preparation coherently and does not assert
a unique intermediate physical time at which the pure battery waits for use.

No original-law derivation, material realization, independent mathematical
acceptance, useful reset, permanent record or law of individual outcomes is
claimed. [VALIDATION.md](VALIDATION.md) records custody, checks and falsifiers.
