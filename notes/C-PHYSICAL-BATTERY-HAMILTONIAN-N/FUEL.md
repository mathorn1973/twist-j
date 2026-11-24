# Finite fuel sources for two physical battery interfaces

**Status: NON-CANONICAL, L1, candidate-T.** These are exact finite
constructions and conditional resource obstructions, not an executed
scientific verifier or independent acceptance. The reservation is
[issue #1753](https://github.com/mathorn1973/twist-j/issues/1753).

There are two different source contracts. Sections 1-6 construct the
nominated pure coherent battery \(b_L\) used for the stronger complete-state
interface. Section 7 gives a sharp-energy battery prepared from charged
basis fuel for the changed ledger and exact accepted reduced channel of
[PR #1752 at e19b071][sharp-proof]. The latter needs no cross-energy
coherence with respect to the additive bare energy \(H_0\).

In both cases the battery starts empty and charging is an explicit
energy-conserving unitary. The finite fuel is consumed. Charged fuel,
low-entropy encodings, clock readiness, and any coherence required by the
chosen interface are supplied resources, not consequences of the original
transport law. Neither option prepares its complete ready apparatus from
empty stationary resources.

[COMPILATION.md](COMPILATION.md) gives the full-space local implementation,
including its work registers and gate bound.
[HAMILTONIAN.md](HAMILTONIAN.md) embeds that circuit in a single positive
autonomous Hamiltonian. Here the battery Hamiltonian is an actual positive
on-site operator on its physical qubits.

## 1. Physical banks and the supplied source

Use the parameters of COMPILATION.md:

\[
Q=5^{2r}\ge\max\{1,q_{\max}\},\qquad
\ell=2r+22,\qquad L=5^\ell=Q5^{22},\qquad
B_{\max}=L+2Q-1.
\]

Every physical battery, fuel, data, and work qubit has the same positive
on-site Hamiltonian \(\epsilon |1\rangle\langle1|\). For a bank of width w
write

\[
|\theta_w(k)\rangle=|1^k0^{w-k}\rangle,\qquad 0\le k\le w.
\]

On one circuit line, the battery B has \(B_{\max}\) physical qubits,
initially all zero, and

\[
H_B=\epsilon\sum_{i\in B}|1\rangle\langle1|_i.
\]

Its full physical space includes all bit strings. The thermometer code
selects one vector for each energy \(0,\epsilon,\ldots,\epsilon B_{\max}\).
There is no projection onto that code in the preparation.

These bank widths describe one circuit line. The autonomous layout has
\(R_g+1\) data rows. Its fixed physical battery subsystem contains the
battery columns in every row, with on-site Hamiltonian summed over all
those copies. Initially the extra rows are empty, and at the final endpoint
only the last row contains the output code. Thus the full raw battery
capacity is \(\epsilon(R_g+1)B_{\max}\); the one-row code capacity is
\(\epsilon B_{\max}\). Equations below about the autonomous battery
include the empty other-row factors in its endpoint vectors. The same
convention applies to the fuel-bank copies.

The charge donor O has Q qubits in \(|1\rangle^{\otimes Q}\). Its sharp
energy is \(\epsilon Q\). The coherence donor C is a product of \(\ell\)
specified blocks. Block j has \(4\cdot5^j\) physical qubits and initial state

\[
|d_j(a)\rangle=|\theta_{4\cdot5^j}(a5^j)\rangle,\qquad
|\eta_j\rangle=\frac1{\sqrt5}\sum_{a=0}^4|d_j(a)\rangle,
\qquad 0\le j<\ell.
\]

Each block is a coherent state across five different physical energies
\(\epsilon a5^j\). It is not a product of independent physical qubits in
\(|+\rangle\). The product is between blocks; correlations within each
block are part of the supplied resource.

The donor width is exactly

\[
\sum_{j=0}^{\ell-1}4\cdot5^j=L-1.
\]

For the unique base-five expansion \(n=\sum_j a_j5^j\), put
\(|d(n)\rangle=\bigotimes_j|d_j(a_j)\rangle\). These are orthogonal
physical basis vectors, each with exactly n excitations. Consequently

\[
|\eta\rangle_C=\bigotimes_j|\eta_j\rangle
 =\frac1{\sqrt L}\sum_{n=0}^{L-1}|d(n)\rangle,\qquad
|f\rangle_{OC}=|1\rangle^{\otimes Q}|\eta\rangle_C.                 \tag{F1}
\]

This supplies one vector at each of L consecutive total fuel energies.
The battery-and-fuel banks alone have

\[
B_{\max}+Q+(L-1)=2L+3Q-2
\]

physical qubits. This is not the full apparatus width. Data encoding,
charged work pairs, routing, history storage, and the autonomous clock
are counted separately in the companion construction.

The positive real coefficients in (F1) specify a phase relation to the
hardwired interactions and the initial clock boundary. This alignment is
part of the supplied state. Under a common free time shift t, the
coefficient of \(d_j(a)\) acquires
\(\exp(-i\epsilon a5^j t/\hbar)\). Independent unspecified digit phases
would not in general prepare the nominated flat battery state.

## 2. A total energy-conserving charging permutation

For \(0\le n<L\) define

\[
\begin{split}
|a_n\rangle&=|\theta_{B_{\max}}(0)\rangle_B
 |1\rangle_O^{\otimes Q}|d(n)\rangle_C,\\
|b_n\rangle&=|\theta_{B_{\max}}(Q+n)\rangle_B
 |0\rangle_O^{\otimes Q}|0\rangle_C^{\otimes(L-1)}.
\end{split}
\]

Each pair has the same total physical energy \(\epsilon(Q+n)\).
The \(a_n\) are mutually distinct, the \(b_n\) are mutually distinct,
and the two sets are disjoint: every \(a_n\) has empty battery, while
every \(b_n\) has nonzero battery charge because \(Q\ge1\).

Define on the full battery-and-fuel Hilbert space

\[
P_{BF}=I+\sum_{n=0}^{L-1}
 \left(|b_n\rangle\langle a_n|+|a_n\rangle\langle b_n|
       -|a_n\rangle\langle a_n|-|b_n\rangle\langle b_n|\right).       \tag{F2}
\]

It swaps every pair and fixes every other physical basis vector.
Thus it is a unitary involution and

\[
[P_{BF},H_B+H_O+H_C]=0.                                           \tag{F3}
\]

In particular,

\[
P_{BF}\bigl(|\theta_{B_{\max}}(0)\rangle_B|f\rangle_{OC}\bigr)
 =|b_L\rangle_B|0\rangle_{OC},\qquad
|b_L\rangle=\frac1{\sqrt L}
 \sum_{n=0}^{L-1}|\theta_{B_{\max}}(Q+n)\rangle.                    \tag{F4}
\]

There is no conditioning or discarded outcome. Tensoring (F2) with the
identity proves (F4) also in the presence of any spectator and reference.
The fuel ends exactly in its ground state, so this is a consumed source,
not an unchanged catalyst.

The L swaps in (F2) are a specification of one macro. They are not local
elementary operations. COMPILATION.md decomposes this same macro into
finite constant-support conserving gates and spatial routing, including
the invalid raw encodings, with all work returned at macro boundaries.
Its gate count already includes the preparation macro.

## 3. Energy, variance, capacity, and coherence

In one donor block the uniform digit a has mean 2 and variance 2. The
product between blocks therefore gives

\[
\begin{split}
\langle H_{C_j}\rangle&=2\epsilon5^j,&
\operatorname{Var}(H_{C_j})&=2\epsilon^2 25^j,\\
\langle H_C\rangle&=\epsilon\frac{L-1}{2},&
\operatorname{Var}(H_C)&=\epsilon^2\frac{L^2-1}{12}.
\end{split}                                                       \tag{F5}
\]

The total initial fuel has

\[
\boxed{\quad
\langle H_F\rangle=\epsilon\left(Q+\frac{L-1}{2}\right),\qquad
\operatorname{Var}(H_F)=\epsilon^2\frac{L^2-1}{12}.
\quad}                                                           \tag{F6}
\]

Its maximum available energy is \(\epsilon(Q+L-1)\).
The one-row battery code capacity is \(\epsilon(L+2Q-1)\), leaving
the finite margin
required by the subsequent lift. In (F4) the battery acquires exactly the
mean and variance in (F6), and the fuel loses all its mean energy and
variance. Equation (F3) preserves the complete total-energy distribution,
not merely its first two moments.

For a state \(\rho\), let \(\Delta_H(\rho)\) remove off-diagonal blocks
between distinct eigenspaces of H, and define
\(A_H(\rho)=S(\Delta_H(\rho))-S(\rho)\), with natural logarithms.
For the pure total fuel state in (F1),

\[
\Delta_{H_F}(|f\rangle\langle f|)
 =\frac1L\sum_{n=0}^{L-1}|1^Q,d(n)\rangle\langle1^Q,d(n)|,
\qquad A_{H_F}(|f\rangle\langle f|)=\log L=\ell\log5.               \tag{F7}
\]

This is dephasing with respect to the total physical fuel Hamiltonian.
Its value follows from the unique base-five energy expansion, not an
assumption that asymmetries add for arbitrary product sources with
degenerate energy sums.

For \(0\le k<L\), the part of the coherent donor density matrix carrying
energy difference \(\epsilon k\) is

\[
\rho_C^{(k)}=\frac1L\sum_{n=0}^{L-1-k}|d(n+k)\rangle\langle d(n)|,
\qquad
\|\rho_C^{(k)}\|_1=\frac{L-k}{L}.                                  \tag{F8}
\]

Negative k gives the adjoint; all modes with \(|k|\ge L\) vanish.
The trace norm follows because the summands map orthogonal inputs to
orthogonal outputs. This exhibits exactly which finite coherence modes
are supplied and transferred. Averaging the unknown common phase over
one period \(2\pi\hbar/\epsilon\) removes all nonzero modes and gives
the dephased state in (F7); that averaged resource cannot prepare (F4).

## 4. Why energy-diagonal resources cannot replace the donor

The target in this section is the nominated pure battery state \(b_L\)
and its full coherent interface. This obstruction does not rule out an
incoherent battery used for weaker reduced-output semantics, a different
energy assignment, or other detector constructions.

Let the physical bare Hamiltonian split as \(H_0=H_B+H_R\), with R
containing all other apparatus degrees of freedom. Suppose a closed
unitary evolution U obeys \([U,H_0]=0\), and the initial joint state is
stationary, \([\rho_0,H_0]=0\). The final state is also stationary.
Partial trace gives

\[
e^{-itH_B/\hbar}\rho_B e^{itH_B/\hbar}
 =\operatorname{Tr}_R\!
 \left(e^{-itH_0/\hbar}\rho\,e^{itH_0/\hbar}\right)=\rho_B.
\]

Thus \([\rho_B,H_B]=0\). This argument admits arbitrary stationary
correlations and energy degeneracies.

For every stationary battery state \(\sigma_B\), including states outside
the thermometer code,

\[
\langle b_L|\sigma_B|b_L\rangle
 =\frac1L\sum_{n=0}^{L-1}
 \langle\theta_{B_{\max}}(Q+n)|\sigma_B|
        \theta_{B_{\max}}(Q+n)\rangle\le\frac1L.                    \tag{F9}
\]

Different terms have different physical energies, and the sum of these
diagonal entries is at most one. With trace distance
\(D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1\), the projector
\(|b_L\rangle\langle b_L|\) then yields

\[
D\bigl(\sigma_B,|b_L\rangle\langle b_L|\bigr)\ge1-\frac1L.          \tag{F10}
\]

The bound is attained by the uniform incoherent mixture of these L
thermometer vectors. Extra energy-basis charge, arbitrarily many
degenerate helpers, or a clock with zero bare energy do not evade it.

In the companion law \([H_{\rm tot},H_0]=0\). Therefore an all-energy-basis
initial apparatus cannot be converted into the donor (F1), or directly
into (F4), by that law. Adding an unaccounted Fourier preparation of a
nondegenerate fuel block would only hide the same missing coherence
resource. A native phase relation in an energy-degenerate coin has no
nonzero mode with respect to that degenerate energy. This does not say
that every native input is stationary under a spectral-energy reading.
As [NATIVE.md](NATIVE.md) explains, such coherence and the new qubit
excitation energy cannot simply be identified. An admitted coupling,
energy dictionary, and quantitative transfer construction would be
needed to obtain (F1) from a particular native input.

## 5. Scoped lower bounds and the non-return statement

These lower bounds also concern exact preparation of this pure \(b_L\),
not every output semantics of a finite detector.

The following bounds concern exact preparation by an energy-conserving
closed unitary. Assume the initial battery is its ground state, the
supplied fuel is pure, and every other initial subsystem has sharp total
energy independent of that fuel. The latter allows unknown data
entangled with a reference inside a fixed-charge subspace. If the final
battery is the pure state \(b_L\), it factors from the remaining state.
Since H_0 is additive, variance in these initial and final product
splittings gives

\[
\operatorname{Var}_{\rm initial}(H_F)
 =\operatorname{Var}_{b_L}(H_B)
  +\operatorname{Var}_{\rm final}(H_R)
 \ge\epsilon^2\frac{L^2-1}{12}.                                   \tag{F11}
\]

The sharp initial energies contribute no variance. This source saturates
(F11) because its residual fuel is in a sharp ground state. The equation
is not a universal bound for correlated initial sources or a system with
other unaccounted energy variance.

If no other subsystem supplies net mean energy and the residual source
Hamiltonian is nonnegative, mean-energy conservation similarly requires

\[
\langle H_F\rangle_{\rm initial}
 \ge\epsilon\left(Q+\frac{L-1}{2}\right).                           \tag{F12}
\]

This is a statement about source consumption under the stated boundary
conditions, not a lower bound on all imaginable rearrangements of
precharged apparatus.

There is also a simple pure-state asymmetry bound. For a pure initial
global state with all nonfuel inputs of sharp energy, the entropy of
the total-energy distribution is the entropy of the fuel-energy
distribution. Exact conservation preserves it. At the pure-battery
endpoint, total energy is the sum of an independent uniform variable X
on L levels and a remaining energy variable Y. Therefore

\[
H(X+Y)\ge H(X+Y\mid Y)=H(X)=\log L.
\]

For pure states that energy-distribution entropy equals \(A_H\).
Hence the initial pure fuel must have \(A_{H_F}\ge\log L\). The donor
(F1) attains this bound. This derivation does not assume that the final
rest has sharp energy.

For comparison, if N independent physical qubits of gap \(\epsilon\)
were the only initial sources of energy variance, each would contribute
at most \(\epsilon^2/4\). Equation (F11) would require

\[
N\ge\frac{L^2-1}{3}.                                               \tag{F13}
\]

The present source uses L-1 coherent-donor qubits because they are
correlated within the specified blocks. Calling the \(\ell\) blocks
"\(\ell\) elementary physical qubits" would give an incorrect resource
account.

Finally suppose an initially pure finite fuel were returned in exactly
the same pure state, the battery started sharp and ended in \(b_L\),
and all other initial resources were sharp. Purity forces the returned
fuel and the pure battery to factor from each other and the rest.
Conservation of variance would require

\[
\operatorname{Var}(H_F)
 =\operatorname{Var}(H_F)
  +\operatorname{Var}_{b_L}(H_B)
  +\operatorname{Var}_{\rm final}(H_{\rm other}),
\]

which is impossible for \(L>1\). This rules out that exact pure returned
catalyst under these conditions. It is not a blanket theorem about
mixed correlated catalysts, approximate return, or consumed coherent
fuel. If every other marginal is returned unchanged, even a positive
increase of battery mean energy is separately excluded by conservation
of the mean.

## 6. Integration in one autonomous physical Hamiltonian

The companion construction uses

\[
H_{\rm tot}=H_0+H_{\rm prop},\qquad
H_0=\epsilon\sum_{\text{physical charged qubits }i}
 |1\rangle\langle1|_i,\qquad
[H_0,H_{\rm prop}]=0,\qquad \epsilon=4g>0.                          \tag{F14}
\]

Both terms are positive. The physical history-clock qubits have zero
bare energy in H_0, but their initial boundary state is nonstationary
under H_prop. For a compiled word with K propagation edges the declared
readiness values are

\[
\langle H_{\rm prop}\rangle=g,\qquad
\operatorname{Var}(H_{\rm prop})=
 \frac{g^2K}{(K+1)^2}.
\]

A bare-energy-degenerate clock therefore is not a zero-resource clock.
Its propagation energy and initial boundary condition are explicit.
Because H_prop commutes with H_0, that clock resource cannot replace the
nonzero H_0 coherence modes of the donor.

At the exact transfer time

\[
\tau=\frac{\pi\hbar(K+1)}{2g},\qquad
\frac{\epsilon\tau}{\hbar}=2\pi(K+1),
\]

all eigenvalues of \(H_0/\epsilon\) are integers, so

\[
e^{-iH_0\tau/\hbar}=I.
\]

Consequently the autonomous endpoint implements the nominated compiled
word up to its common propagation phase. There is no unmentioned
relative bare-energy phase on the flat battery state.

Let C_0 be the fixed number of initial excitations outside the fuel,
including dual-rail information and clean work, with the battery empty.
In COMPILATION.md the standard initial source has q=0 and
\(C_0=n_S+A\). All later fresh data rows start empty. Even for an unknown
logical input entangled with a reference, this charge is fixed. The
complete initial physical energy and variance are

\[
\begin{split}
\langle H_{\rm tot}\rangle
 &=\epsilon\left(C_0+Q+\frac{L-1}{2}\right)+g,\\
\operatorname{Var}(H_{\rm tot})
 &=\epsilon^2\frac{L^2-1}{12}
   +\frac{g^2K}{(K+1)^2}.                                         \tag{F15}
\end{split}
\]

The covariance vanishes: on the initial history boundary, the
clock-diagonal part of H_prop is \(gI\), while its off-diagonal part
changes the clock; H_0 preserves the clock. Thus
\(\langle H_0H_{\rm prop}\rangle=g\langle H_0\rangle\).
The on-site H_0 terms have norm \(\epsilon=4g\); a bound of g on
propagation terms must not be presented as a bound on every term of
H_tot.

A circuit consisting only of P_BF has the exact pure charged-battery
endpoint (F4) under this autonomous construction. For the full word
\(V^{L_{\rm prog}+h}P_{BF}\), preparation is included as a logical
prefix. Intermediate continuous-time states generally superpose
prefixes. There is no asserted deterministic intermediate physical time
at which the pure battery can be extracted before the rest of the word
runs. At the final full-word endpoint, later operations may have changed
or entangled the battery.

The construction accounts for charging from a specified coherent fuel
and a specified clock boundary. It does not derive the supplied coherent
blocks, their phase alignment, cooling, reset, or the local interactions
from the original transport law. Deriving those blocks from stationary
resources while retaining (F14) is excluded by (F9)-(F10); a stronger
native completion must identify its actual nonstationary source rather
than move this assumption into another unnamed preparation stage.


## 7. A sharp-energy alternative with no bare-energy coherence donor

The alternative [PROOF.md in PR #1752][sharp-proof] selects a different
account. It omits coordinate-square and coin energies, and counts the
inner clock, pulse presence, auxiliary nonzero pentits, and predicate
bits. On the accepted pulse sector, the data part of that account is
identity on the physical object, carrier variables, receiver, logical
labels, and reference. Only auxiliary histories and clock remain
energy-dependent. This is a supplied energy assignment, not the canonical
spectral energy.

For its pinned short word define distinct parameters

\[
L_\star=1638410,\quad M_\star=3276820,\quad
R_{\rm aux}=983045,\quad Q_\star=M_\star+R_{\rm aux}=4259865.
\]

The battery levels are \(0,\ldots,Q_\star\), with prepared value
\(|Q_\star\rangle\). The initialized target has account zero and therefore
the ready target-plus-battery lies in one total-energy sector. Its
sector embedding is

\[
J_{Q_\star}\psi=\sum_{q=0}^{Q_\star}P_q\psi\otimes|Q_\star-q\rangle.
\]

On that sector the target evolution is exact. The full output generally
correlates the battery with auxiliary and clock energies. For the named
accepted physical output, tracing the retained auxiliaries, clock, and
battery leaves precisely the ideal accepted physical channel, including
arbitrary logical/reference correlations. The equality is an
observational comparison; those histories are not physically deleted.

[SHARP.md](SHARP.md) supplies the local endpoint construction with this
contract. In particular it does not replace \(b_L\) by \(|Q_\star\rangle\)
while keeping the old spatial-square ledger and demanding the old
complete product output. Both the ledger and the comparison channel have
changed. Sections 4-5 therefore do not obstruct this alternative.

### Exact charging from a supplied basis fuel

Use \(Q_\star\) identical-gap battery qubits B and \(Q_\star\) identical-gap
fuel qubits F. Define the two raw basis words

\[
|u\rangle=|0\rangle_B^{\otimes Q_\star}|1\rangle_F^{\otimes Q_\star},
\qquad
|v\rangle=|1\rangle_B^{\otimes Q_\star}|0\rangle_F^{\otimes Q_\star}.
\]

They have equal total physical excitation number \(Q_\star\).
The specified charging macro is the single-pair transposition

\[
P_{\rm ch}=I+|v\rangle\langle u|+|u\rangle\langle v|
             -|u\rangle\langle u|-|v\rangle\langle v|.             \tag{F16}
\]

It swaps u and v and fixes every other raw basis word. Thus it is a total
unitary on the complete banks, obeys
\([P_{\rm ch},H_B+H_F]=0\), and prepares exactly the thermometer code
for \(|Q_\star\rangle\) with the fuel ground-state depleted.
It extends by the identity to all other inputs and references.
The same conserving local compiler includes this macro; naming it
does not make its controls or physical implementation free.

Here the initial fuel resource is

\[
\boxed{\quad
\langle H_F\rangle=\epsilon Q_\star,\qquad
\operatorname{Var}(H_F)=0,\qquad A_{H_F}=0.
\quad}                                                           \tag{F17}
\]

All its nonzero energy-difference modes vanish. The battery gains exactly
\(\epsilon Q_\star\) and remains energy-sharp at this charging endpoint.
No donor phase alignment between different bare energies is required.
Subsequent target evolution can redistribute this sharp total energy and
correlate the battery with the target. That does not contradict its exact
accepted reduced-channel contract.

For the notation of SHARP.md, the core width is
\(P_\star=2n_\star+3Q_\star\): \(2n_\star\) information qubits, a \(Q_\star\)-qubit
system tally, a \(Q_\star\)-qubit battery and a \(Q_\star\)-qubit fuel.
The compiler uses \(P_\star\) clean dual-rail work pairs. Their one
excitation per pair and the \(n_\star\) information excitations are counted.
The complete initial line is an eigenstate of physical bare energy with

\[
H_0=\epsilon(n_\star+P_\star+Q_\star)
\]

on the entire admitted input family, also with an arbitrary reference.
This is an eigenvalue on that family, not an operator identity on all
raw states. Its \(H_0\) variance is zero. Every additional data row starts
empty but remains counted hardware. If the physical layout has
\(R_\star+1\) rows, its battery and fuel banks each have
\((R_\star+1)Q_\star\) qubits and raw capacity
\(\epsilon(R_\star+1)Q_\star\); only the specified one-row code is occupied
at an endpoint.

### What the sharp source does not eliminate

It eliminates the broad donor's \(H_0\)-energy variance and \(\log L\)
asymmetry requirement for this changed interface. It does not create
charged basis fuel from nothing. In any closed conserving preparation,

\[
\Delta\langle H_B\rangle=-\Delta\langle H_{\rm rest}\rangle.
\]

If all other final energy marginals are required to be unchanged, an
initially empty battery cannot acquire \(\epsilon Q_\star>0\).
The present fuel supplies exactly that loss. More strongly, an initial
state supported in the ground space of the nonnegative \(H_0\) stays
there under any unitary commuting with \(H_0\). The separately conserved
propagation energy cannot pay a missing bare-energy charge.

The sharp fuel and fixed-charge work do not make the initialized complete
apparatus stationary under the actual generator. For the physical clock
boundary and K propagation transitions of HAMILTONIAN.md, the corresponding
ready state has

\[
\langle H_{\rm tot}\rangle
 =\epsilon(n_\star+P_\star+Q_\star)+g,\qquad
\operatorname{Var}(H_{\rm tot})=\frac{g^2K}{(K+1)^2}>0.             \tag{F18}
\]

The broad fuel-variance term in (F15) is absent; clock readiness remains.
Here the bare part is sharp, so its free evolution is a common phase on
the reached sector. The common choice \(\epsilon=4g\) is still admissible,
but no relative bare-energy phase needs cancellation within this prepared
sector. The localized clock is a basis state for its bare-degenerate
subsystem, while it is nonstationary for the interacting Hamiltonian.

For a mixed data/reference density operator \(\rho_D\), nonstationarity
also follows directly, rather than from its positive variance alone.
For \(\rho=|0\rangle\langle0|_{\rm clock}\otimes\rho_D\), the clock block

\[
[H_{\rm tot},\rho]_{1,0}=-a_0G_0\rho_D\ne0
\]

is nonzero because \(a_0>0\), \(G_0\) is unitary and \(\rho_D\ne0\).
The same proof applies to the padded outer clock; see PADDED.md section 7.

This last distinction has a general obstruction. If a complete initial
state is stationary for \(H_{\rm tot}\), a preparation unitary commuting
with \(H_{\rm tot}\), in particular evolution under that fixed Hamiltonian,
preserves stationarity:

\[
[\rho,H_{\rm tot}]=0,\quad[U,H_{\rm tot}]=0
\ \Longrightarrow\ [U\rho U^*,H_{\rm tot}]=0.                     \tag{F19}
\]

It cannot prepare the nonstationary clock-boundary state in (F18) from
such an input. A larger source, changing an interaction, or another
preparation intervention would require its own account. No such source is
silently supplied here. The charged basis fuel, clean dual-rail work,
empty storage rows, and localized clock boundary are explicit initial
conditions of the added law. Cooling, resetting, and deriving those
conditions from the unchanged native model remain open.

[sharp-proof]: https://github.com/mathorn1973/twist-j/blob/e19b07183c3e4841e18c8913de7c4c83429b94f3/notes/C-FINITE-HAMILTONIAN-READOUT-N/PROOF.md
