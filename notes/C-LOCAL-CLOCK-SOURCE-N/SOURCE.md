# A local excitation source for an initially empty clock

**NON-CANONICAL, L1, conditional candidate-T. Independent acceptance pending.**
This is an analytical construction under
[claim #1755](https://github.com/mathorn1973/twist-j/issues/1755).
No scientific execution is reported.

The source is one supplied excited qubit. The device cursor initially has
no excitation and is stationary under its isolated law. A fixed local
exchange coupling launches the cursor; no separate scheduling clock
switches that coupling on. The initial source and device are stationary
for a specified separated Hamiltonian, but their product is not stationary
for the interacting Hamiltonian that actually runs.

The improvement over the preceding domain-wall construction is a conserved
physical excitation entering an empty device from an explicit source.
It is not the first localization of an initial commutator: the earlier
domain-wall boundary also had a nonzero commutator only at its first edge.
Nor is this a construction of nonstationarity from a state stationary
under the complete running law.

## 1. Source, empty device, and counted data readiness

The finite local data circuit is the sharp-energy interface described in
the companion [HAMILTONIAN.md](HAMILTONIAN.md). Write

\[
E_{\rm old}=n_*+A_*+Q_*
\]

for its initial data excitation number before the added completion latch.
The latch is a dual-rail pair in its specified one-excitation basis state.
Thus the entire data register D, including information, work, basis fuel,
empty battery and latch, starts in the fixed excitation sector

\[
N_D\rho_D=(E_{\rm old}+1)\rho_D.                                  \tag{S1}
\]

The density operator \(\rho_D\) may contain arbitrary admitted logical and
passive-reference correlations. A reference has no Hamiltonian here.
Every data instruction \(G_j\) is unitary and commutes with \(N_D\).

Use physical cursor qubits \(c_0,c_1,\ldots,c_M\), with
\(n_j=|1\rangle\langle1|_{c_j}\) and
\(N_C=\sum_{j=0}^M n_j\). The source is \(c_0\); the device cursor is
\(c_1,\ldots,c_M\). Denote the one-excitation basis by

\[
|j\rangle_C=|0\cdots 010\cdots0\rangle,\qquad 0\le j\le M.
\]

The initial cursor is \(|0\rangle_C\): source occupied, every device
cursor qubit empty. This notation means one excitation at site zero,
not the all-vacuum bit string. The latter is denoted
\(|{\rm vac}\rangle_C\).

To distinguish the loading runway from the compiler work count \(A_*\),
write \(N_{\rm act}\) for the number of old active cursor instructions and

\[
A_{\rm run}=N_{\rm act}+1,\qquad
L_{\rm done}=2A_{\rm run},\qquad M=4A_{\rm run}.                     \tag{S2}
\]

There are \(A_{\rm run}\) identity loading edges, then the
\(N_{\rm act}\) active instructions and one completion-latch instruction,
followed by the identity tail. In particular \(G_0=I\), and the physical
source-device bond has no data control. The implementation and geometry
of these instructions are specified in HAMILTONIAN.md.
[PREPARATION.md](PREPARATION.md) gives the finite loading interval.

## 2. One positive Hamiltonian on the full raw space

Let

\[
s_j^+=|1\rangle\langle0|_{c_j},\qquad
s_j^-=|0\rangle\langle1|_{c_j},\qquad
X_j=s_{j+1}^+s_j^-\otimes G_j.
\]

For a fixed \(g>0\), put

\[
a_j=\frac{g}{M+1}\sqrt{(j+1)(M-j)},\quad 0\le j<M,\qquad
a_{-1}=a_M=0,
\]
\[
v_j=g-a_{j-1}-a_j\ge0,\qquad 0\le j\le M.                         \tag{S3}
\]

The bound \(a_j\le g/2\) proves the last inequality. Define

\[
\begin{split}
H_0&=\epsilon(N_D+N_C),\qquad \epsilon>0,\\
h_j&=a_j\bigl((n_j+n_{j+1})\otimes I-X_j-X_j^*\bigr),\\
H_{\rm prop}&=\sum_{j=0}^{M-1}h_j+\sum_{j=0}^M v_j n_j\otimes I\\
 &=gN_C\otimes I-\sum_{j=0}^{M-1}a_j(X_j+X_j^*),\\
H&=H_0+H_{\rm prop}.
\end{split}                                                       \tag{S4}
\]

These operators are defined on every cursor bit string. In the
two-site cursor sectors 00 and 11, \(h_j\) is respectively zero and
\(2a_jI\). In the 10/01 sector it has diagonal blocks \(a_jI\) and
unitary off-diagonal blocks \(-a_jG_j\), \(-a_jG_j^*\), so its
eigenvalues are zero and \(2a_j\). Therefore

\[
h_j\ge0,\qquad \|h_j\|\le2a_j\le g,\qquad
H_{\rm prop}\ge0,\qquad H\ge0.                                    \tag{S5}
\]

No illegal cursor sector is discarded to prove positivity.
Each exchange preserves \(N_C\), and each data gate preserves \(N_D\).
Consequently

\[
[H,N_C]=[H,N_D]=[H,H_0]=0.                                        \tag{S6}
\]

The source excitation is physically conserved; every propagation edge
only moves it. The full initial bare energy, with the latch included, is

\[
E_0=\epsilon(E_{\rm old}+2).                                      \tag{S7}
\]

The empty device cursor qubits still count as physical hardware.

## 3. Separated stationarity and the actual local launch

Because \(G_0=I\), the off-diagonal source-device coupling is simply

\[
V_{01}=-a_0(s_1^+s_0^-+s_0^+s_1^-)\otimes I_D.                    \tag{S8}
\]

Consider the comparison Hamiltonian

\[
H_{\rm sep}=H-V_{01}
 =H_{\rm source}\otimes I+I_{c_0}\otimes H_{\rm device},
\qquad H_{\rm source}=(\epsilon+g)n_0.                            \tag{S9}
\]

Here \(H_{\rm device}\) includes the data, all device cursor sites, and
all cursor exchanges except the source-device bond. It is positive.
One way to see this is the positive partition in the next section:
\(H_{\rm device}=H_{\rm rest}+a_0n_1\).

The occupied source is an eigenstate of \(H_{\rm source}\). On the device
cursor vacuum every cursor propagation term vanishes, so the isolated
device acts on the initialized data as the scalar
\(\epsilon(E_{\rm old}+1)\). Thus

\[
\rho_0=|0\rangle_C\langle0|\otimes\rho_D,\qquad
[H_{\rm sep},\rho_0]=0.                                          \tag{S10}
\]

This is a comparison of operators and states. It is not a protocol that
switches from \(H_{\rm sep}\) to H at a chosen time. The actual law is the
fixed H in (S4), including \(V_{01}\), throughout the declared experiment.

All terms of \([H,\rho_0]\) except this one local bond vanish. Explicitly,

\[
[H,\rho_0]
 =-a_0\bigl(|1\rangle_C\langle0|
           -|0\rangle_C\langle1|\bigr)\otimes\rho_D,
\qquad
\|[H,\rho_0]\|_1=2a_0>0.                                        \tag{S11}
\]

The formula holds for mixed logical/reference inputs, since
\(\|\rho_D\|_1=1\). It proves nonstationarity directly; positive energy
variance by itself would not prove that for a mixed state.

The failure of stationarity is generated by a coupling supported on two
neighboring physical sites. The energy eigenstates and complete
energy-coherence distribution of H still depend on the whole apparatus.
It would be stronger, and incorrect without another argument, to identify
all global energy asymmetry with a tensor factor consisting of that bond.

No relative phase of an isolated \(|1\rangle\) source qubit needs to be
specified. Nevertheless the localized source/contact input (S10) is a
nonstationary initial condition for H. Its preparation under a larger
physical law is not derived by writing (S9).

## 4. A positive local energy account for launch

The physical source bare-energy term is \(\epsilon n_0\). To include the
local propagation contribution in a positive account, define

\[
H_{\rm launch}=(\epsilon+v_0)n_0\otimes I+h_0,\qquad
H_{\rm rest}=H-H_{\rm launch}.                                   \tag{S12}
\]

Both operators are positive. The rest consists exactly of
\(\epsilon N_D\), the bare cursor terms at sites \(1,\ldots,M\),
the potentials \(v_jn_j\) for \(j\ge1\), and edges \(h_j\) for \(j\ge1\).
The launch term is supported on the source and its first device neighbor.
It is a local positive part of the energy, not solely an energy operator
on the source tensor factor.

On the initialized state,

\[
\langle H_{\rm launch}\rangle_0
 =\epsilon+v_0+a_0=\epsilon+g,\qquad
\langle H_{\rm rest}\rangle_0=\epsilon(E_{\rm old}+1).
\]

In particular

\[
\boxed{\quad
\langle H\rangle_0=\epsilon(E_{\rm old}+2)+g,\qquad
\operatorname{Var}_{\rho_0}(H)=
 a_0^2=\frac{g^2M}{(M+1)^2}.
\quad}                                                           \tag{S13}
\]

Indeed H has initial diagonal scalar \(E_0+g\) and its only
off-diagonal action is \(-a_0|1\rangle_C\otimes I_D\).
This also proves the variance formula for a mixed \(\rho_D\).

Thus the bare clock excitation costs \(\epsilon\), and the complete
initial launch region carries \(\epsilon+g\). Counting only
\(\epsilon\) while omitting g would lose part of the physical energy.
The initial data energy includes the original basis fuel, every
information/work excitation, and the additional latch excitation.
No second broad coherent fuel is used here.

The individual means of \(H_{\rm launch}\) and \(H_{\rm rest}\) need not
be conserved. Their sum is the conserved mean of H. This local partition
therefore describes energy leaving the launch region without introducing
a negative counterterm.

## 5. Exact source survival and complete transfer

Let \(\mathcal V_0=I\) and
\(\mathcal V_j=G_{j-1}\cdots G_0\).
On the one-cursor sector the history change of basis
\(|j\rangle\psi\mapsto|j\rangle\mathcal V_j\psi\) turns the propagation
matrix into \(gI-[2g/(M+1)]J_x\). The symmetric-spin expansion then gives

\[
|\Omega(t)\rangle=e^{-it(E_0+g)/\hbar}
 \sum_{j=0}^M
 \sqrt{\binom Mj}\,(i\sin\theta)^j(\cos\theta)^{M-j}
 |j\rangle_C\,\mathcal V_j|\psi_D\rangle,
\qquad
\theta=\frac{gt}{\hbar(M+1)}.                                     \tag{S14}
\]

Density operators and arbitrary reference inputs follow by linearity.
Since every history has the same \(H_0\) value \(E_0\), its bare-energy
phase is common for every positive ratio \(\epsilon/g\).

The exact source occupation is

\[
p_0(t)=\operatorname{Tr}(n_0\rho(t))=\cos^{2M}\theta,               \tag{S15}
\]

and the probability weight at its first neighbor is

\[
p_1(t)=M\sin^2\theta\,\cos^{2M-2}\theta.
\]

For the prepared evolution the expectation of \(X_0\) is purely imaginary.
Therefore the positive local launch energy has the explicit mean

\[
\langle H_{\rm launch}\rangle_t
 =(\epsilon+g)p_0(t)+a_0p_1(t).                                  \tag{S16}
\]

At

\[
t_*=\frac{\pi\hbar(M+1)}{2g},
\]

the cursor is exactly at M, the completed data occupies its nominated
output, and \(p_0(t_*)=p_1(t_*)=0\) because \(M\ge2\).
The launch-region energy is then exactly zero. Its initial energy has
moved into the rest under the same autonomous law.

The source does not create a perfect isolated ready-clock state at an
earlier deterministic boundary. The loading runway instead provides the
finite approximate preparation interval proved in PREPARATION.md.
During that interval the device has nearly all the cursor weight while
the computation has not yet begun on the good runway portion. The full
state, including the small source and early-processing components,
continues unitarily.

As a negative control, replace the occupied source by the cursor vacuum
while keeping the same data preparation and the same H. Every \(X_j\),
\(h_j\), and \(v_jn_j\) annihilates that vacuum. Hence

\[
e^{-itH/\hbar}
 (|{\rm vac}\rangle\langle{\rm vac}|_C\otimes\rho_D)
e^{itH/\hbar}
 =|{\rm vac}\rangle\langle{\rm vac}|_C\otimes\rho_D.                \tag{S17}
\]

There is no launch or computation. The data's charged basis fuel does not
silently replace the missing cursor excitation because \(N_C\) and
\(N_D\) are separately conserved in this law.

## 6. Full-energy coherence, not a new bare-energy donor

The initial state is sharp for \(H_0\), so its cross-\(H_0\)-energy modes
vanish. Its coherence relative to H is different. Write
\(\gamma=g/(M+1)\). On the reached sector the distinct energy values and
their initial weights are

\[
E_r=E_0+g-\gamma(M-2r),\qquad
p_r=2^{-M}\binom Mr,\qquad 0\le r\le M.                            \tag{S18}
\]

They give mean and variance (S13). For energy dephasing \(\Delta_H\), the
relative-entropy asymmetry is exactly

\[
A_H(\rho_0):=D\bigl(\rho_0\,\|\,\Delta_H(\rho_0)\bigr)
 =-\sum_{r=0}^M p_r\log p_r>0.                                   \tag{S19}
\]

To verify this also for mixed reference inputs, use the history basis
and then the spin energy basis. The state is a pure clock vector tensor
\(\rho_D\); dephasing replaces that clock vector by the diagonal weights
\(p_r\) and leaves \(\rho_D\) unchanged. Relative entropy thus reduces
to the displayed finite Shannon entropy. This formulation does not
subtract two possibly infinite reference entropies.

The stationary state \(\Delta_H(\rho_0)\) has exactly the same energy
distribution, mean, and variance as \(\rho_0\), but cannot act as the
same localized initial launch. For example its source occupation is

\[
\sum_{r=0}^M p_r^2=4^{-M}\binom{2M}{M}<1,
\]

whereas the supplied source occupation is initially one. This provides
a direct check against treating nonzero variance alone as the presence
of a usable clock resource.

Equation (S19) is not a claim that the global asymmetry was produced from
nothing when the experiment began. It belongs to the specified initial
source/contact state relative to the fixed full Hamiltonian. Rescaling g
changes the variance and duration; it does not eliminate that distinction.

## 7. The remaining preparation boundary and exact no-go statements

For any fixed Hamiltonian H,

\[
[\rho,H]=0,\quad[U,H]=0
 \quad\Longrightarrow\quad[U\rho U^*,H]=0.                        \tag{S20}
\]

Thus a stationary complete source-plus-device input cannot be converted
into (S10) by evolution under H or by another H-conserving preparation
unitary. The separated stationarity in (S10) does not evade (S20):
\(H_{\rm sep}\) and H are different operators. No physical switching
protocol between them has been supplied or used.

The exact excitation conservation also forbids obtaining the one-cursor
initial state from a zero-cursor state under this same law. A separately
supplied excited source is therefore an actual premise. Any proposal to
prepare it from another source must count that source and its coupling.
This does not imply that an arbitrarily extended physical source must
contain a pre-existing abstract clock; it identifies the nonstationary
boundary condition that a complete extension would have to supply.

There is also an exact finite-dimensional obstruction to a permanent
launch plateau. If the initially occupied source had zero occupation on
an open later time interval, then for every pure component of the initial
state the vector

\[
n_0 e^{-itH/\hbar}|\psi\rangle
\]

would vanish throughout that interval. Its components are analytic
functions of t for finite H. They would consequently vanish for all t,
including \(t=0\), contradicting the initial source occupation. Positivity
gives the same conclusion for a mixed initial state.

Therefore an exactly empty source for a finite open interval, followed by
a separate exact start, or a permanently emptied source under this closed
finite law cannot be inferred from the single transfer endpoint.
Approximate loading and retention intervals are compatible with this
obstruction and are separately quantified. No finite self-stopping
controller, reusable reset, or occurrence rule follows.

The construction specifies local source coupling, conserved physical
energy, initially empty cursor storage, charged data readiness and a
nonstationary source/contact input. It does not derive those qubits,
interactions, source acquisition, cooling, or preparation of that localized
source/contact state from the original native TWIST-J update. Those distinctions
are retained in [NATIVE.md](NATIVE.md).
