# P-QDD-SHORT-GAUSS-CLOCK-1 proof

## Register and positive-time primitives

Let \(e_x\), \(x\in\mathbb F_5\), be the orthonormal point basis and \(g e_x=e_{x+1}\). Define \(N=\mathbf1\mathbf1^{\mathsf T}=\sum_{a=0}^4g^a\), \(P_0=N/5\), and \(\Gamma=g+g^{-1}-g^2-g^{-2}\). With \(A=g+g^{-1}\), we have \(\Gamma=2A+I-N\), \(A^2=N+I-A\), \(AN=2N\), and \(N^2=5N\). Hence \(\Gamma^2=5I-N\) and \(\Gamma P_0=0\). These identities agree with the marked-register Gauss algebra in [Public Canon v116](https://github.com/mathorn1973/twist-j/blob/93c36089db57032a6cbca482ff62c95884567d0f/canon/CANON.md#L4073-L4106).

Use evolution \(\exp(-iHt/\hbar)\), positive \(\omega\), and a common phase frame. Set \(s=(0,1,-1,-1,-1)^{\mathsf T}\), \(r_{ab}=e_a-e_b\) for \(a\ne b\), and \(E_a=e_ae_a^\dagger\).

| Primitive | \(H/\hbar\) | Duration | Full propagator |
| --- | --- | --- | --- |
| Gauss quarter | \(\omega\Gamma\) | \(\pi/(2\sqrt5\,\omega)\) | \(U=P_0-i\Gamma/\sqrt5\) |
| Contact | \(\omega ss^{\mathsf T}\) | \(\pi/(4\omega)\) | \(C=I-ss^{\mathsf T}/2\) |
| Transposition | \(\omega r_{ab}r_{ab}^{\mathsf T}\) | \(\pi/(2\omega)\) | \(T_{ab}=I-r_{ab}r_{ab}^{\mathsf T}\) |
| Point sign | \(\omega E_a\) | \(\pi/\omega\) | \(Z_a=I-2E_a\) |

The uniform direction has Gauss eigenvalue zero and the centered space has eigenvalues in \(\{\sqrt5,-\sqrt5\}\). This gives the displayed \(U\) with \(U^2=2P_0-I\) and \(U^4=I\) on the entire register. Three positive quarters give \(U^3=U^\dagger\). Each rank-one Hamiltonian accumulates phase \(-1\) on its defining vector and \(+1\) on the perpendicular space. The transposition Hamiltonian includes both diagonal terms and maps \(e_a\) to \(+e_b\) and \(e_b\) to \(+e_a\).

## Signed word and routing

Put \(S=T_{14}\) and \(r=e_1-e_4\). Directly, \(v=\Gamma r=(0,1,2,-2,-1)^{\mathsf T}\), \(Ur=-iv/\sqrt5\), and \(USU^\dagger=I-vv^{\mathsf T}/5\). Since \(s^{\mathsf T}v=2\), the contact sends \(v\) to \(w=v-s=(0,0,3,-1,0)^{\mathsf T}\). Thus \(CUSU^\dagger C=I-ww^{\mathsf T}/5\). It acts by the block \(\frac15\begin{pmatrix}-4&3\\3&4\end{pmatrix}\) on the ordered pair \((2,3)\) and fixes the other three points. Left multiplication by \(Z_2\) flips the first row, giving \(R=\frac15\begin{pmatrix}4&-3\\3&4\end{pmatrix}\). Placing the sign on the input instead gives \(R^\dagger\).

For each \(k=1,2,3,4\), choose \(Q_k\) with \(Q_k(0)=2\) and \(Q_k(k)=3\). Its full action and transposition decomposition are given below. Operators act from right to left.

| \(k\) | \(Q_k(0),\ldots,Q_k(4)\) | \(Q_k\) | Transpositions including \(S\) and both routes | Total gates |
| --- | --- | --- | --- | --- |
| 1 | \(2,3,0,1,4\) | \(T_{02}T_{13}\) | 5 | 12 |
| 2 | \(2,1,3,0,4\) | \(T_{03}T_{02}\) | 5 | 12 |
| 3 | \(2,1,0,3,4\) | \(T_{02}\) | 3 | 10 |
| 4 | \(2,1,0,4,3\) | \(T_{02}T_{34}\) | 5 | 12 |

The word in operator order is \(R_k=Q_k^{-1}Z_2 C U S U^3 C Q_k\). Its schedule is routing, \(C\), three positive Gauss quarters, \(S\), one positive Gauss quarter, \(C\), \(Z_2\), then inverse routing. It maps \(e_0\) to \((4e_0+3e_k)/5\), \(e_k\) to \((-3e_0+4e_k)/5\), and every other basis vector to itself. This proves the full gate identity for complex inputs, including extension by the identity on a passive reference, and gives the action of its channel on every matrix unit.

Each word has four Gauss quarters, two contacts and one point sign. Its active time in the sequential model is \((4+2/\sqrt5)\pi/\omega\) for \(k=1,2,4\) and \((3+2/\sqrt5)\pi/\omega\) for \(k=3\), including both routes. The count treats the three consecutive quarters as three gates even if the drive is held continuously. These are realized durations with instantaneous switching and upper bounds on the minimum active time in that model.

For comparison, an explicit longer construction uses \(L=T_{23} C T_{13}\), \(P_k:x\mapsto 1+x/k\) and the relabeling \(\mu:x\mapsto 2x\), all modulo five. Since \(\mu\Gamma\mu^{-1}=-\Gamma\), one may implement \(U^\dagger=\mu U\mu^{-1}\). With \(L^{\mathsf T}v=3e_1-e_2\), the word \(P_k^{-1} Z_1 L^{\mathsf T} U S U^\dagger L P_k\) realizes the same rotation. For \(k=1\), \(P_1\) is a five-cycle and \(\mu\) has a four-cycle. Direct transposition routing there and back costs \(8+6\) swaps, the two copies of \(L\) use four more, and \(S\) adds one. Including two Gauss quarters, two contacts and the sign gives 24 operations and \((11+1/\sqrt5)\pi/\omega\). Every permutation on five labels takes at most four transpositions, so this realizes the worst cost of this longer schedule. The shorter construction reduces the largest gate count from 24 to 12. Neither count proves global minimality.

## Joint clock and data evolution

Fix one setting before evolution. Let \(G_0,\ldots,G_{11}\) be its gates in time order, padded at the end by identities to 12 links. Idle uses 12 identities. For clock positions \(|0\rangle,\ldots,|12\rangle\), set
\[
H_{\rm path}=\hbar\lambda\sum_{q=0}^{11}\sqrt{(q+1)(12-q)}
\bigl(|q+1\rangle\langle q|\otimes G_q+
      |q\rangle\langle q+1|\otimes G_q^\dagger\bigr),\qquad \lambda>0.
\]
This time-independent Hamiltonian assumes a frame with flat clock energies and no additional drift terms. Each link acts jointly on clock and data. The backward hop applies the adjoint of the forward hop.

Define \(V_0=I\), \(V_{q+1}=G_qV_q\), and \(D=\sum_{q=0}^{12}|q\rangle\langle q|\otimes V_q\). Conjugating by \(D^\dagger H_{\rm path}D\) gives the scalar weighted clock adjacency tensored with \(I\), because \(V_{q+1}^\dagger G_q V_q=I\). In the symmetric subspace of 12 qubits, identify \(|q\rangle\) with the normalized equal sum of bit strings of weight \(q\). The restriction of \(\sum_{j=1}^{12}X_j\) has the same adjacency. For the increase \(q\to q+1\), each weight-\((q+1)\) string receives \(q+1\) contributions from weight \(q\). The matrix element is \((q+1)\sqrt{\binom{12}{q+1}/\binom{12}{q}}=\sqrt{(q+1)(12-q)}\), and the decrease is its adjoint.

The initial scalar clock is the all-zero bit string. Each zero evolves to \(\cos(\lambda t)|0\rangle-i\sin(\lambda t)|1\rangle\). Undoing the conjugation gives the full joint evolution for any data input \(\psi\),
\[
e^{-itH_{\rm path}/\hbar}(|0\rangle\otimes\psi)=
\sum_{q=0}^{12}\sqrt{\binom{12}{q}}\,
 \cos^{12-q}(\lambda t)\bigl(-i\sin(\lambda t)\bigr)^q
 |q\rangle\otimes V_q\psi .
\]
At \(T=\pi/(2\lambda)\) all nonterminal amplitudes vanish, and the state is \(|12\rangle\otimes V_{12}\psi\) with phase \((-i)^{12}=+1\). Here \(V_{12}=R_k\) for the active setting and \(V_{12}=I\) for idle. This identity also applies with a passive reference. Under continued evolution the endpoint probability is \(\sin^{24}(\lambda t)\), so the transfer is transient.

The largest value of \((q+1)(12-q)\) is \(42\), attained on links \(q=5,6\). Each \(G_q\) is unitary, so the strongest link has forward coupling norm \(\hbar\lambda\sqrt{42}\). If \(g_{\rm head}>0\) bounds the link frequency, then \(\lambda\le g_{\rm head}/\sqrt{42}\). The earliest exact transfer attainable in this specified path family under that bound is \(\pi\sqrt{42}/(2g_{\rm head})\), achieved at equality. At fixed \(\lambda\) the transfer time is \(\pi/(2\lambda)\). The sequential pulse times apply to a separate model.

## Phase-sensitive Gauss calibration

One Gauss quarter on \(e_0\) predicts point probabilities \((1,6,6,6,6)/25\), with \(x=(Ue_0)_1=1/5-i/\sqrt5\) and \(y=(Ue_0)_2=1/5+i/\sqrt5\). The probabilities for projection onto \((e_1-e_2)/\sqrt2\) and \((e_1+e_2)/\sqrt2\) are \(2/5\) and \(2/25\), respectively. Replacing \(U\) by \(U^\dagger\) conjugates the state, so every real Hermitian effect gives the same probability. Also \(U^\dagger r=-Ur\), which makes \(U^\dagger S U=U S U^\dagger\). The compiled real reflection therefore has the same action for either orientation of the Gauss quarter.

Fix the analyzer orientation with an independent signed phase reference for levels 1 and 2 in the marked frame used to specify \(U\), with the time and sign convention of the primitive table. For the projector onto \((e_1+i e_2)/\sqrt2\) the probability is
\[
\frac{|x-iy|^2}{2}
=\frac{|x|^2+|y|^2}{2}+\operatorname{Im}(\bar x y)
=\frac{6+2\sqrt5}{25}.
\]
For \(U^\dagger\), the same fixed projector gives \((6-2\sqrt5)/25\). Simultaneous conjugation of pulse and analyzer preserves the probability. With the analyzer calibrated independently, this single setting distinguishes the two specified pulses on \(e_0\). Full characterization of an unknown five-level channel requires further data.

## Scope and relation to localization

The model assumes coherent access to all named gates on the same marked register. The public four-state pointer/bath COLLIDE matrix has the contact reflection on its four configurations. Identifying those configurations with point labels \(1,2,3,4\) on the Gauss register and supplying an untouched level \(0\) are additional assumptions. The Hamiltonians require the signed couplings, phase conventions, level addressing and spectator action specified above. The ideal model permits extension by the identity on unused data levels. Physical leakage and drift require independent characterization. [Public COLLIDE rule](https://github.com/mathorn1973/twist-j/blob/93c36089db57032a6cbca482ff62c95884567d0f/reproduce/C-FIELD-J-INTERNAL-CONTROL-N/verify.py#L215-L237)

The four rotations and idle are ideal intervention settings of the type considered in the separate conditional localization proposal. For a convention using \((4I+3iX)/5\) on \((0,k)\), \(F=\operatorname{diag}(1,i,i,i,i)\) gives \(F R_k F^\dagger=\frac15\begin{pmatrix}4&3i\\3i&4\end{pmatrix}\) on that pair for every \(k\), and preserves idle. This is a common basis conversion. Using it as an operation in a fixed preparation and measurement frame would require the corresponding phase controls. The word and clock proofs are independent of the localization proposal. An actual localization experiment additionally requires establishing the physical cut, the site of the intervention and the constraints on the shared preparation and receiver, as well as verifying the received channels. [Conditional localization proposal](https://github.com/mathorn1973/twist-j/pull/2061)

Promoting the Gauss matrix to a physical Hamiltonian and placing all controls on a particular site are assumptions. The engineered clock additionally requires initialization, supplied joint link operators, and synchronized endpoint readout. Its path is nearest-neighbor in clock position, with data action carried by the link gates. Hardware implementation, native coupling strengths, timing windows, and physical measurements remain outside this construction.
