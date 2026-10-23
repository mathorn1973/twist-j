# C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N

**PUBLIC, NON-CANONICAL. L1 candidate evidence package: connected asymptotic capture, complete physical current, and coherent receiver record.**

Owner: A. M. Thorn. License: Apache-2.0.
Authority basis: `mathorn1973/twist-j` main `e6240e2689bb22aab5f02bad90b75d3692bb96d9` (Public Canon v104, content commit `4a50e527d20018839f006ed312454b710e6486b4`).

This package provides a self-contained, publicly auditable proof and standard-library verification surface for the connected asymptotic capture-current-record mechanism on the homogeneous one-object-pair, one-carrier (standing token **or** moving pulse), one-encoded-receiver sector. Every decisive analytical premise and quantitative certificate inequality is proved or verified from first principles within this package without requiring private repository access or external third-party libraries.

---

## 1. Connected Asymptotic Theorem Statement

### 1.1 Common Carrier, Coordinates, Native Allocation, and Clock Convention

1. **Physical coordinates and active sector:** Let $x_A = R + r \in \mathbb{Z}$ and $x_B = R - r \in \mathbb{Z}$ ($x_A \equiv x_B \pmod 2$) be the physical lattice coordinates of the two object constituents, $y \in \mathbb{Z}$ be the physical coordinate of the single carrier (either a standing token at site $y$ or a moving pulse at site $y$), and $z = 100 \in \mathbb{Z}$ be the fixed physical coordinate of the receiver memory. Let $d \in \{1,2,3,4\} \equiv \{++, +-, -+, --\}$ denote the four two-body coin directions with streaming displacements $(\delta R_d, \delta r_d) \in \{(-1,0), (0,-1), (0,+1), (+1,0)\}$, i.e., $(\delta x_A, \delta x_B) \in \{(-1,-1), (-1,+1), (+1,-1), (+1,+1)\}$.
2. **All 26 carrier and receiver labels:** The carrier and receiver each carry a complete 26-label alphabet $j, k \in \{0, 1, \dots, 25\}$:
   - **Token codes** $\{\mathrm{tok}_j\}_{j=0}^{25} \subset \{-1,0,1\}^{12}$ on local coordinates $(h_5, \dots, h_{16})$: each code has $h_5 \in \{-1, +1\}$ and exactly one nonzero entry $\pm 1$ in $\{h_6, \dots, h_{16}\}$, with $\mathrm{tok}_1 = (1, 1, 0, \dots, 0)$. Every token code has native charge $2\sum_{\alpha=5}^{16} h_\alpha^2 = 4$ and at most one nonzero entry inside either pulse bank $\{h_7,\dots,h_{11}\}$ or $\{h_{12},\dots,h_{16}\}$.
   - **Pulse codes** $\{p_j\}_{j=0}^{25} \subset \{-1,0,1\}^5$: all $\binom{5}{2}\cdot 4 = 40$ two-occupied signed vectors in $\{-1,0,1\}^5$ supply 26 distinct codes (with $p_1 = (-1,-1,0,0,0)$), embedded into bank $b=1$ ($h_7,\dots,h_{11}$) or bank $b=2$ ($h_{12},\dots,h_{16}$) with $h_5 = h_6 = 0$. Every pulse code has native charge $4$. The token and embedded pulse sectors are strictly disjoint, and both the on-site pulse coin and vacuum pulse edge act as the identity on every token.
   - **Receiver memory codes** $\{d_k\}_{k=0}^{25} \subset \{-1,0,1\}^{13}$ on local coordinates $(h_{25}, \dots, h_{37})$: each code has a single nonzero entry $(-1)^k$ at index $\lfloor k/2 \rfloor$, with $d_1 = (-1, 0, \dots, 0)$ and native charge $2$.
   - **Spectator/helper coordinates:** The remaining nine local coordinates $\{h_{17},\dots,h_{24}, h_{38}\}$ (0-indexed $\{16,\dots,23,37\}$) are untouched spectators. On the active sector without helper occupancy, total native charge is $H_N = 4_{\mathrm{obj}} + 4_{\mathrm{car}} + 2_{\mathrm{rec}} = 10$.
3. **Synchronized phase-zero chart and macrostep:** One complete macrostep occupies two autonomous microticks between synchronized phase-zero slices. On the uncoupled carrier-memory space $\mathcal{H} \otimes \mathcal{V}_{\mathrm{rec}}$, where $\mathcal{H} = \mathcal{H}_{\mathrm{obj}} \otimes \mathcal{H}_{\mathrm{car}}$ with $\mathcal{H}_{\mathrm{car}} = \mathcal{H}_{\mathrm{tok}} \oplus \mathcal{H}_{\mathrm{pulse}}$, the dynamics is
   $$U = U_0 C, \qquad U_{\mathrm{rec}} = \mathcal{T}(U \otimes I_{\mathrm{rec}})\mathcal{T}^*,$$
   where:
   - $C$ is the local homogeneous contact unitary acting at $R = y, r = 0$ on each label $j \in \{0,\dots,25\}$ as the orthogonal rotation $\begin{pmatrix} 3/5 & -4/5 \\ 4/5 & 3/5 \end{pmatrix}$ on $\operatorname{span}\{|a_0\rangle \otimes |\mathrm{tok}_j(y)\rangle, |b_0\rangle \otimes |p_{j,1}(y)\rangle\}$ with $|a_0\rangle = \delta_{r=0}\frac{i(|+-\rangle - |-+\rangle)}{\sqrt{2}}$ and $|b_0\rangle = \delta_{r=0}\frac{|++\rangle - |--\rangle}{\sqrt{2}}$, and as the identity on the orthogonal complement;
   - $U_0 = e^{-i\beta}(W \otimes V_{\mathrm{car}})$ with $\beta = 4\pi/5$, $g = 2\pi/5$, object walk $W = \Gamma S M_2$ ($\Gamma = I + (e^{-ig}-1)\delta_{r=0}$), and free carrier step $V_{\mathrm{car}} = I_{\mathrm{tok}} \oplus V_{\mathrm{pulse}}$ where $V_{\mathrm{pulse}}$ applies the on-site pulse coin $Q = \frac{1}{\sqrt{5}}\begin{pmatrix} 1 & -2 \\ 2 & 1 \end{pmatrix}$ followed by the bond hop $D_{\mathrm{edge}}$;
   - $\mathcal{T}$ is the unitary half-line calibration swapping the pulse label $j$ and receiver memory label $k$ on pulse sites $y \ge z = 100$ while acting as the identity on all tokens and on pulse sites $y < z$. Because $[\mathcal{T}, C \otimes I_{\mathrm{rec}}] = 0$, the conjugated step $U_{\mathrm{rec}}$ replaces only the bond $(z-1, z) = (99, 100)$ by the local receiver edge $D_{\mathrm{rec}} = \frac{1}{\sqrt{5}}\begin{pmatrix} I & -2\,\mathrm{SWAP} \\ 2\,\mathrm{SWAP} & I \end{pmatrix}$.

### 1.2 Fixed Incoming Preparation

Let $\Pi_b(P) = |\chi_b(P)\rangle\langle\chi_b(P)|$ be the original rank-one Riesz bound branch of $W(P)$ continued analytically from $\chi_b(0) = |b_0\rangle$ with eigenvalue $e^{-i\Omega_b(0)} = e^{-ig}$ on $|P| \le p_* = 1/12$, and let $\Pi_{\mathrm{sc}}^W(P) = I - \Pi_b(P)$ on $I_P = [-p_{\mathrm{in}}, p_{\mathrm{in}}]$ with $p_{\mathrm{in}} = 1/1000$.
For total energy window $I_E = [E_* - h, E_* + h] = [8\pi/5 - 1/1000, 8\pi/5 + 1/1000]$ ($|I_E| = \ell = 1/500$, corresponding to object relative-energy window $I_\omega = [4\pi/5 - 1/1000, 4\pi/5 + 1/1000]$ where $E = \omega + \beta$), define the normalized contact-selected flat-energy incoming state with standing token label $1$ localized at $y = 0$ (uniform across all total momentum fibers $K \in [-\pi, \pi)$):
$$\Psi_{\mathrm{in}}(K, P, E) = \mathbf{1}_{I_P}(P)\,\frac{\mathbf{1}_{I_E}(E)}{\sqrt{|I_E|}}\,\frac{\Pi_{\mathrm{sc}}^W(P)(b_0)}{\sqrt{a(P,E)}} \otimes |\mathrm{tok}_1\rangle, \qquad a(P,E) = \int_{I_P} \rho_{B,W}(P', E-\beta)\,dP',$$
and its physical interacting preparation
$$\Psi_{\mathrm{prep}} = \Omega_{\mathrm{rec},-} (\Psi_{\mathrm{in}} \otimes \Phi_{\mathrm{mem},\mathrm{ref}}),$$
where $\Phi_{\mathrm{mem},\mathrm{ref}} = \sum_{j=0}^{25} |d_j\rangle \otimes |\phi_j\rangle$ ($\sum_{j=0}^{25} \|\phi_j\|^2 = 1$) is an arbitrary normalized initial receiver-memory/helper/reference state.

### 1.3 Main Connected Theorem

**Theorem (Connected Asymptotic Capture, Complete Current, and Coherent Record).**
Under the exact law and preparation of §§1.1–1.2:

1. **Fiber Wave Operators and Inherited Infinite-Operator Branch Gap:**
   On each total-momentum fiber $K = P + k \in [-\pi, \pi)$, $U(K) - U_0(K)$ has finite rank ($2$ per carrier label), so the fiber wave operators $\Omega_\pm(K) = \operatorname{s-lim}_{n\to\mp\infty} U(K)^{-n} U_0(K)^n P_{\mathrm{ac}}(U_0(K))$ and their direct integrals $\Omega_\pm$ and $\Omega_{\mathrm{rec},\pm} = \mathcal{T}(\Omega_\pm \otimes I_{\mathrm{rec}})\mathcal{T}^*$ exist, are isometric on the absolutely continuous scattering subspaces, and intertwine $U$ with $U_0$ and $U_{\mathrm{rec}}$ with $U_{\mathrm{rec},0} = \mathcal{T}(U_0 \otimes I_{\mathrm{rec}})\mathcal{T}^*$. On $|P| \le 1/12$, the infinite-lattice operator $W(P)$ has a simple isolated bound branch $\Pi_b(P)$ separated from the rest of $\operatorname{spec}(W(P))$ by at least $13/165$ with $\|\Pi_b'(P)\| \le L = 165/13$. By the finite-strip elimination theorem, the only compactly supported eigenvectors of $W(P)$ are the bound-pair family at $P = 2\theta$, so $W(P)$ has no extra point spectrum on $I_P$, and $\Psi_{\mathrm{in}}$ is unit-normalized with zero incoming bound weight: $(\Pi_b \otimes I_{\mathrm{car}})\Omega_- \Psi_{\mathrm{in}} = 0$.
2. **Exact Interface Equality and Quantitative Probability Certificate:**
   Let $I_K = [k_0 - \delta_K, k_0 + \delta_K]$ with $k_0 = -\arccos\bigl(\frac{9 - 5\sqrt{5}}{16}\bigr)$ and $\delta_K = 1/1000$, and let $I_P^{\mathrm{out}} = [-p_b, p_b]$ with $p_b = 1/100$. On the free outgoing reference space, define the full-momentum and $K$-windowed joint capture-and-record projectors:
   $$Q_{\mathrm{full}} = \int_{[-\pi,\pi)}^{\oplus} \Pi_b^{\mathrm{out}}(K, [-p_b, p_b])\,P_{\mathrm{pulse},1,+}(K)\,\frac{dK}{2\pi} \otimes |d_1\rangle\langle d_1| \otimes I_{\mathrm{ref}}, \qquad Q_{\mathrm{win}} = \mathbf{1}_{I_K}(K)\,Q_{\mathrm{full}}.$$
   These agree identically with the three component-interface projectors:
   $$A:E_{\mathrm{joint}} = B:Q_{\mathrm{win}} = \mathbf{1}_{I_K}\,C:Q_{\mathrm{joint}} \le C:Q_{\mathrm{joint}} = Q_{\mathrm{full}},$$
   with physical wave-operator lifts $E_{\mathrm{scat}}^{\mathrm{win}} = \Omega_{\mathrm{rec},+} Q_{\mathrm{win}} \Omega_{\mathrm{rec},+}^* \le E_{\mathrm{scat}}^{\mathrm{full}} = \Omega_{\mathrm{rec},+} Q_{\mathrm{full}} \Omega_{\mathrm{rec},+}^*$. Using the full Carathéodory functions $F_1, F_2$ without dropping spectral channels or extrapolating radial limits, the asymptotic joint capture-and-record probability satisfies the conservative certified lower bound
   $$p(Q_{\mathrm{full}}) = \|Q_{\mathrm{full}}\,\Omega_{\mathrm{rec},+}^* \Psi_{\mathrm{prep}}\|^2 \ge p(Q_{\mathrm{win}}) = \|Q_{\mathrm{win}}\,\Omega_{\mathrm{rec},+}^* \Psi_{\mathrm{prep}}\|^2 \ge \frac{\delta_K}{\pi}\,B_{\mathrm{hom}} > \frac{2}{10^{28}},$$
   where $B_{\mathrm{hom}} = 64\pi^2 a b_{\mathrm{hom}} \frac{9/49}{(4+M)^2} > \frac{8}{10^{25}}$, $a > \frac{24}{10^6}$, $b_{\mathrm{hom}} > \frac{1}{100}$, and $M = \bigl[\frac{2\pi\sec(9\pi/20)}{(40/49)\ell}\bigr]^{20/9}$.
3. **Coherent Old-Memory Transfer and Safe-Window Binding Guarantee:**
   For every outgoing right-moving pulse wavepacket supported on $y \ge z = 100$ with carrier label $1$, $\mathcal{T}$ maps
   $$|p_1\rangle \otimes \sum_{j=0}^{25} |d_j\rangle \otimes |\phi_j\rangle \;\longmapsto\; \sum_{j=0}^{25} |p_j\rangle \otimes |d_1\rangle \otimes |\phi_j\rangle,$$
   writing $|d_1\rangle$ into the receiver memory while coherently transferring the arbitrary old memory state (including all entanglement with the reference system) into the outgoing pulse label. Moreover, because $I_E \subset [3\pi/2, 17\pi/10] \subset J_{\mathrm{safe}} = (5\pi/4, 7\pi/4)$ and $2\arctan 2 < 3\pi/4$, the two-pulse continuum cannot alias into $J_{\mathrm{safe}} \pmod{2\pi}$; hence on $\mathcal{H}_{I_E}(U_{\mathrm{rec}})$, any outgoing pulse-channel wavepacket automatically lies in the bound-object sector $\operatorname{Ran}\Pi_b$ and writes $|d_1\rangle$ at $z = 100$.
4. **Native Occupancy Intertwiner, Physical Cut Charge, and Full Current:**
   The native-to-source intertwiner $\mathcal{I} = \mathsf{Emb}\,\Gamma^{-1} D_2^*$ and its occupied-helper extension $\mathcal{I}_{\eta,\xi}$ satisfy $U_{\mathrm{nat}}\mathcal{I}_{\eta,\xi} = \mathcal{I}_{\eta,\xi} U_{\mathrm{rec}}$, pull back the full right-half native charge across any physical cut $\ell \in \mathbb{Z}$ (in particular $\ell = z - 1 = 99$) as $\mathcal{I}_{\eta,\xi}^* H_{N,R,\ell}^{\mathrm{full}}\mathcal{I}_{\eta,\xi} = N_{R,\ell} + H_{N,R,\ell}^{\mathrm{help}}(\eta)\cdot I$ with active weights $(2,2,4,2)$ on $(x_A, x_B, y, z)$, and yield the exact one-step physical current at the same macrostep phase:
   $$J_\ell = U_{\mathrm{rec}}^* N_{R,\ell} U_{\mathrm{rec}} - N_{R,\ell} = N_{L,\ell} - U_{\mathrm{rec}}^* N_{L,\ell} U_{\mathrm{rec}} = C^* D_c^* (j_{S,\ell} + j_{E,\ell}) D_c C.$$

---

## 2. Package Architecture and Navigation

| File | Role |
|---|---|
| [PREREG.md](PREREG.md) | Prospective specification freezing scientific scope, carrier, code, failure thresholds, exact rational interval soundness contract, and resource limits prior to execution. |
| [PROOF_CAPTURE_SCATTERING.md](PROOF_CAPTURE_SCATTERING.md) | Self-contained analytical proofs: homogeneous carrier, 26-label code, $K=P+k$ fiber wave operators, $2\times 2$ Lippmann-Schwinger inversion and $64\pi^2$ normalization, inherited infinite-operator branch gap ($\ge 13/165$, $\|\Pi'\|\le 165/13$), finite-strip elimination theorem, two-pulse alias obstruction, and no-uniform-shutoff identity. |
| [PROOF_PACKET_CERTIFICATE.md](PROOF_PACKET_CERTIFICATE.md) | Self-contained analytical proofs: incoming scalar Schur complement $F_{0,B}=X+id$, Möbius contact transform, contact-selected packet normalization and zero incoming bound weight, output coarea density $b_{\mathrm{hom}}$, full-function Hardy-Carathéodory bound $M$, probability bound $p(Q_{\mathrm{full}})\ge p(Q_{\mathrm{win}})>2/10^{28}$, and soundness proof of the standard-library rational interval verifier. |
| [PROOF_CURRENT_RECORD_INTERFACE.md](PROOF_CURRENT_RECORD_INTERFACE.md) | Self-contained analytical proofs: receiver conjugacy $[\mathcal{T},C\otimes I_{\mathrm{rec}}]=0$, coherent old-memory transfer, safe-window $(5\pi/4,7\pi/4)$ binding theorem vs. native charge $H_N$, native intertwiner $\mathcal{I}_{\eta,\xi}$, physical cut $\ell=99$ charge and full current $J_\ell$, exact interface equality $A:E_{\mathrm{joint}}=B:Q_{\mathrm{win}}=\mathbf{1}_{I_K}C:Q_{\mathrm{joint}}$, causal history reconstruction $L_m$, dark-state current counterexample, and infinite-carrier no-go theorems. |
| [CLAIMS_AND_DISPOSITIONS.md](CLAIMS_AND_DISPOSITIONS.md) | Complete claim/dependency/status/falsifier and scope tables, including explicit dispositions for PR1721, PR1723, PR1726, and the primary homogeneous source, plus P24 vs. PR1726 separation. |
| [CLAIMS.tsv](CLAIMS.tsv) | Machine-readable TSV ledger of all claims, dependencies, verification routes, falsifiers, and scope boundaries. |
| [SOURCES.md](SOURCES.md) | Immutable source provenance, SHA-256 manifest, custody and extraction record, manifest file-count reconciliation (59 vs. 62), and license/security review. |
| [RESULT.md](RESULT.md) | Pinned verification result and audit summary (recorded after prospective pin readback and execution). |
| [`../../reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/`](../../reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/) | Standard-library Python 3 verifier (`verify.py`), deterministic expected output (`EXPECTED.txt`), reproduction guide (`README.md`), and pinned execution record (`RUN.md`). |

---

## 3. Explicit Scope Boundaries (What Is Not Claimed)

1. **Asymptotic scattering vs. finite-time preparation and detection:** The quantitative bound $p(Q_{\mathrm{full}}) \ge p(Q_{\mathrm{win}}) > 2/10^{28}$ is an asymptotic scattering statement ($\lim_{n\to\infty}$) for the exact contact-selected flat-energy incoming state $\Psi_{\mathrm{prep}}$. Finite-resource state preparation, a finite-time joint detector effect $F_T$, and false-positive bounds at finite read time $T$ are separate successor tasks and are **not derived** here.
2. **Asymptotic record vs. finite-window retention:** The coherent transfer $|p_1\rangle\sum_j |d_j\rangle|\phi_j\rangle \mapsto \sum_j |p_j\rangle|d_1\rangle|\phi_j\rangle$ holds asymptotically on the outgoing pulse channel ($\delta_n \to 0$ as $n \to \infty$); no finite-time recrossing modulus or uniform retention bound on $[T, T+L]$ is claimed here.
3. **Bare $|d_1\rangle$ is not a herald:** If the receiver is initialized in $|d_1\rangle$, the uncaught component retains $|d_1\rangle$; the binding event requires the joint projector (or safe-window energy plus outgoing right-moving pulse beyond $z=100$).
4. **Native charge $H_N$ vs. spectral quasi-energy $E$:** Native charge $H_N = 10$ (with exact local half-space current $J_\ell$) and modular quasi-energy $E \in [-\pi, \pi)$ (used in the safe-window alias theorem) are distinct quantities; no local spectral-energy current, many-body/multi-carrier scattering theorem, Lorentz/Hodge identification, or Born-rule occurrence axiom is claimed.
