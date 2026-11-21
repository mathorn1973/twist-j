# A sharp-energy source for the exact accepted channel

**Status: NON-CANONICAL, L1, conditional candidate-T. Independent acceptance
pending.** This is a separate admitted interface from the coherent product
interface in [FUEL.md](FUEL.md). The reservation is
[issue #1753](https://github.com/mathorn1973/twist-j/issues/1753).

The source of the sharper energy account and accepted-channel theorem is
[PR #1752, PROOF.md at e19b071](https://github.com/mathorn1973/twist-j/blob/e19b07183c3e4841e18c8913de7c4c83429b94f3/notes/C-FINITE-HAMILTONIAN-READOUT-N/PROOF.md).
Its ideal capture word is the candidate in
[PR #1746 at 01acc42](https://github.com/mathorn1973/twist-j/blob/01acc42b78f75095587765e9a5b91ee70dc28f37/notes/C-FORWARD-ONLY-CAPTURE-FILTER-N/PROOF.md),
with the named gate compilation from
[PR #1748 at ecb3460](https://github.com/mathorn1973/twist-j/blob/ecb3460977cd2ee8a120797ffa53ba88cbe14171/notes/C-FORWARD-AUTONOMOUS-CLOCK-N/CLOCK.md).
These pins remain conditional inputs. This note supplies a local conserving
implementation and a sharp basis-fuel charging step. It does not claim the
original time interval survives an arbitrary circuit compilation.

## 1. The different interface and its finite target

Let D=327680, let D+1=327681 be the number of pentits including the source
loader, and let B_work=2D+3=655363 count the binary predicate targets.
Use the short native transport T=2. The ideal word through the completed
flag has length

\[
L_* =5+T+3D+B_{\rm work}=1638410.
\]

Write its gates as G_0,...,G_(L_*-1). The inner history clock has labels
j=0,...,M_*, where M_*=2L_*=3276820. Put G_j=I for L_*<=j<M_* and define

\[
V_0=I,\qquad V_j=G_{j-1}\cdots G_0,\qquad V=V_{L_*}.
\]

Thus V_j=V throughout the inner identity tail. This is not the cyclic
clock of #1748, and it includes no later native-release steps.

Use exactly the finite spatial box of #1752, with source s=99,
R_box=327784 and N_box=2R_box+1=655569. Its total finite gates and source
prefixes are the ones declared there. The inherited infinite-space band
observable uses that source's fixed zero extension, not an asserted equality
of finite and infinite spectra.

On the finite data space define

\[
A_{\rm aux}=\sum_{\text{pentits }a}(I-|0\rangle\langle0|)_a
             +\sum_{\text{bits }b}|1\rangle\langle1|_b,
\qquad A=I_{\rm pulse}+A_{\rm aux}.
\]

Let C=sum_j j|j><j| on the inner clock, N=C+A on S=H_clock tensor H_data,
and

\[
R_{\rm aux}=1+(D+1)+B_{\rm work}=983045,
\qquad Q_*=M_*+R_{\rm aux}=4259865.
\]

Then 0<=N<=Q_*I. This energy reading is independent of positions, coins,
logical messages, receiver values and references, except for the declared
pulse-presence contribution. It is the selected account of #1752; it is
not the spatial-square account of the coherent-source construction.

The prescribed initial source has clock zero and A=0. The unknown logical
source label and old receiver may be entangled with any passive reference.
The ready condition fixes none of those unknown messages.

## 2. A total algebraic endpoint unitary

Define an inner-clock mirror, including its data action, by

\[
U_{\rm mir}=\sum_{j=0}^{M_*}|M_*-j\rangle\langle j|
                    \otimes V_{M_*-j}V_j^*.
\tag{S1}
\]

Let Z=sum_j |j><j| tensor V_j and let R|j>=|M_*-j>. Then
U_mir=Z(R tensor I)Z*. Consequently it is a unitary involution on all
inner-clock and data states, not only the prepared source. In particular,

\[
U_{\rm mir}(|0\rangle\otimes|\psi\rangle)
 =|M_*\rangle\otimes V|\psi\rangle.
\tag{S2}
\]

The symmetric-tensor proof in #1752 gives the same mirror at its transfer
time with a common phase. Equation (S1) fixes that irrelevant common phase
to one. Every entry is algebraic because every finite named gate is
algebraic. This endpoint definition requires no numerical matrix logarithm.
The adjoints in (S1) specify its all-state extension; the local simulator
is not claimed to execute only original forward-query primitives.

Use a logical battery with levels 0,...,Q_*. If P_q are the projections
of N, define

\[
J_{Q_*}|\psi\rangle=\sum_{q=0}^{Q_*}P_q|\psi\rangle
                                     \otimes|Q_*-q\rangle_B.
\tag{S3}
\]

This is an isometry onto the entire total-energy-Q_* sector of N+B_num.
Let \(\Pi_Q=J_{Q_*}J_{Q_*}^*\) be its range projection. Define the total unitary


\[
T_{\rm sharp}=J_{Q_*}U_{\rm mir}J_{Q_*}^*+(I-\Pi_Q).
\tag{S4}
\]

It acts by a unitary on that whole sector and by identity on every other
sector. Therefore [T_sharp,N+B_num]=0 on the entire finite space, including
all battery boundaries. Here the sector projection is an explicit macro
definition, not a claim of microscopic locality or a physical measurement.
The conserving compiler below supplies its actual local gates.

The initialized input is already \(J_{Q_*}(|0\rangle\psi_0)\), because \(N(|0\rangle\psi_0)=0\)
and the charged battery is |Q_*>. Hence its exact endpoint is

\[
T_{\rm sharp}(|0\rangle|\psi_0\rangle|Q_*\rangle_B)
 =J_{Q_*}(|M_*\rangle V|\psi_0\rangle).
\tag{S5}
\]

These equations hold with arbitrary reference systems. The output generally
contains battery correlations with auxiliary histories; it is not the ideal
full state tensor a fixed battery.

## 3. Physical coding and charging from a basis fuel

Let n_* be the registerwise binary information width of this S:

\[
n_*=\lceil\log_2(M_*+1)\rceil+\lceil\log_2 12\rceil
 +3\lceil\log_2N_{\rm box}\rceil+2\lceil\log_2 26\rceil
 +3(D+1)+B_{\rm work}.
\]

Encode every information bit by 0 -> 10 and 1 -> 01. For a basis state x
with N-value q(x), append the Q_*-qubit thermometer theta_Q*(q(x)).
The S code uses 2n_*+Q_* physical qubits and has excitation number n_*+q(x).
Encode battery level n by theta_Q*(n) on Q_* further qubits. All physical
qubits have the same positive onsite gap epsilon. Valid information codes
are chosen registerwise, so the physical output, auxiliary and inner-clock
information factors remain separately identified.

Supply Q_* additional fuel qubits in |1>^Q*, with battery qubits initially
|0>^Q*. Define P_ch to exchange precisely the two battery-and-fuel words

\[
|0\rangle_B^{\otimes Q_*}|1\rangle_F^{\otimes Q_*}
\quad\longleftrightarrow\quad
|1\rangle_B^{\otimes Q_*}|0\rangle_F^{\otimes Q_*},
\tag{S6}
\]

and fix all other raw words. Both words have weight Q_*; they are distinct
because Q_*>0. This is a specified total excitation-conserving unitary.
It charges the battery exactly to its level Q_* and leaves the fuel in
its ground state. It consumes energy epsilon Q_* with no initial variance
or coherence across total bare-energy sectors. The input is a supplied
energized basis state, not free preparation from an all-ground apparatus.

Embed T_sharp on the valid S-and-battery code and extend it by identity
off that code, tensor identity on every fuel qubit. Call this raw-space
unitary W_sharp. The code is invariant under the physical number operator,
and its number there is n_*+q+n; consequently W_sharp preserves physical
number on all raw inputs. The two-macro word is

\[
\mathcal C_{\rm sharp}=W_{\rm sharp}(I_S\otimes P_{\rm ch}).
\tag{S7}
\]

The core width, work count and one-line width are

\[
P_*=2n_*+3Q_*,\qquad A_*=P_*,\qquad S_*=3P_*.
\tag{S8}
\]

The P_* work pairs start in |10> each and return exactly after each macro.
For the standard source the entire line, including unknown logical inputs,
has the one sharp excitation number

\[
E_*^{\rm num}=n_*+P_*+Q_*.
\tag{S9}
\]

Thus its bare energy is epsilon E_*^num and its bare-energy variance is
zero. Energy-basis charging creates no contradiction with FUEL.md: that
file's obstruction concerns a pure battery superposition across different
energies, which is not requested here.

## 4. Exact local conservation and a physical endpoint

Apply the sectorwise QR, equal-weight paths, dual-rail AND computation and
routing proved in sections 4-6 of [COMPILATION.md](COMPILATION.md), now with
core width P_* and exactly two macros. The result is a fully specified finite
algebraic circuit, with

\[
R_*\le256P_*^3 4^{P_*},\qquad S_*=3P_*.
\tag{S10}
\]

Every gate acts on at most four consecutive physical qubits and conserves
their total excitation number as a full-space operator identity. It
implements (S7) on every raw core input, including its identity extensions,
and returns all clean work. No coefficient table or scientific simulation
has been executed to obtain this analytic bound.

The fresh-row and domain-wall construction in
[HAMILTONIAN.md](HAMILTONIAN.md) therefore supplies a positive autonomous
local Hamiltonian for this circuit too. For the unpadded outer clock put
k=R_*(S_*+3)-1. There are (R_*+1)S_* data qubits and k physical
clock qubits; the latter have zero bare splitting. Every extra data row is
initially empty, so (S9) remains the exact total bare charge.

Its endpoint is (S7) in the final physical row, with the earlier rows empty,
up to a common phase. Since the entire initialized family has sharp H_0,
the bare factor is a common phase for every epsilon/g>0. The special
phase-matching choice epsilon=4g is permitted but is unnecessary for this
sharp family. All microscopic propagation terms commute with the same
physical onsite H_0, including on illegal clock and data strings.

The physical battery bank includes its Q_* columns in every row. Its raw
capacity is epsilon(R_*+1)Q_*, while its single-active-row code uses levels
only through epsilon Q_*. These extra empty copies count as hardware.
At the endpoint its physical energy is the thermometer excitation energy,
not merely an encoded name. Work, information, fuel and interaction energy
are also included. The initial physical moments for the unpadded law are

\[
\langle H_{\rm tot}\rangle=\epsilon E_*^{\rm num}+g,
\qquad
\operatorname{Var}(H_{\rm tot})=
                         \frac{g^2k}{(k+1)^2}.
\tag{S11}
\]

The input is stationary for H_0 but nonstationary for the complete generator
because of the localized outer clock. No preparation of that working clock
from a stationary state of H_tot is claimed.

## 5. Exact accepted physical channel, including references

Separate the ideal data as H_phys tensor H_aux in the sense of #1752:
H_phys contains object and carrier coordinates, coins/arrangement, the
incoming logical label, receiver and passive reference. H_aux contains all
loader, filter and predicate registers, including the final flag f. Write
F=|1><1|_f and

\[
\sigma_{\rm acc}=\operatorname{Tr}_{\rm aux}
                 [F V\rho_0V^*F].
\tag{S12}
\]

On this accepted sector pulse presence is one, so A=1+A_aux is independent
of H_phys. Expand a pure accepted ideal vector in an orthonormal auxiliary
energy basis as sum_alpha |phi_alpha>_phys |alpha>_aux, where alpha has
A_aux-value a_alpha. Equation (S5), with physical coding, attaches to each
summand the factors

\[
|\operatorname{dr}(M_*)\rangle_{\rm inner\ clock},\qquad
|\theta_{Q_*}(M_*+1+a_\alpha)\rangle_{\rm tally},\qquad
|\theta_{Q_*}(R_{\rm aux}-1-a_\alpha)\rangle_B.
\tag{S13}
\]

They depend only on alpha, and are normalized. The fuel is zero and the
work is in its returned basis state. Tracing the auxiliary information
basis removes distinct alpha terms. The attached tally, battery and clock
vectors therefore change no surviving physical matrix element.

Let E_phys denote the fixed dual-rail registerwise isometry on the physical
output information factors, tensor identity on the reference. Read the
true rail of the final-row encoded flag as F_enc. Let D_keep be the partial
trace over inner clock, auxiliary histories, tally, battery, fuel, work,
outer clock and empty rows, retaining the final-row physical information
registers and the reference. For the complete endpoint state rho_end,

\[
\boxed{\quad
\mathcal D_{\rm keep}[F_{\rm enc}\rho_{\rm end}F_{\rm enc}]
       =E_{\rm phys}\sigma_{\rm acc}E_{\rm phys}^*.
\quad}
\tag{S14}
\]

Purification or linearity proves this equality for all admitted logical
input operators, including off-diagonal matrix units and arbitrary
reference correlations. It is an exact accepted-channel identity, without
a small-acceptance error factor or a coherent-battery approximation.
Partial traces in (S12)-(S14) compare channels; no physical history is
reset, destroyed or omitted from the closed evolution.

Conditionally on the pinned #1746 source and filter proof, the endpoint has

\[
p_{\rm acc}>1/20000,\qquad
r_{\rm unwanted}<\frac{50000}{99\,2^{29}}<1/10^6.
\tag{S15}
\]

The accepted incoming-message/old-memory channel is the exact SWAP, including
its reference correlations. For incoming label 1 the receiver is exactly
the encoded d_1. The final flag is a specified physical qubit observable;
identifying the retained information registers with H_phys is a stated
mathematical decoding. No physical decoding operation, local measurement of
the band projector, or equality of encoded positions with native particle
positions is supplied for free by (S14). The weights remain L1 norm data.

## 6. Timing and scope

The exact endpoint of the newly compiled law does not inherit #1752's
physical time interval. Generic conservative gate synthesis can change the
flag and physical register locations during intermediate primitive gates.
A read of that flag alone before completion has no asserted source-channel
identity. Circuit checkpoints are not deterministic physical times.

[PADDED.md](PADDED.md) supplies a separate outer identity tail with no
further data motion and a completion-qualified physical herald. Its proof
uses (S14) as its endpoint interface and counts its own extra clock sites,
strength, duration and read interval. Neither its interval nor its later
conditioned-read continuation is silently imported from the inner clock.

The changed energy account is essential. On acceptance it assigns the same
physical energy to all retained object and message values; the auxiliary
history pays the variable charge. The battery may remain correlated with
that history. Tests on the whole history/battery state can distinguish this
output from the coherent product interface in the companion construction.
Thus (S14) neither violates that interface's no-go theorem nor establishes
its stronger whole-state product approximation.

This construction supplies a finite local sharp-energy implementation of
the selected accepted channel. Its degenerate energy reading, supplied
charged fuel, ready dual-rail work, localized clock, exact local couplings
and continuous-time law are explicit added premises. Independent acceptance,
native-law derivation, practical scale, repeatable reset and a mechanism for
individual outcomes remain outside its scope.
