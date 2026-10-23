# Receiver Conjugacy, Native Intertwiner, Physical Cut Current, and Infinite-Carrier No-Go

**PUBLIC, NON-CANONICAL. Self-contained analytical proof (`PROOF_CURRENT_RECORD_INTERFACE.md`) for `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N`.**

Owner: A. M. Thorn. License: Apache-2.0.
Authority basis: `mathorn1973/twist-j` main `e6240e2689bb22aab5f02bad90b75d3692bb96d9` (Public Canon v104, content commit `4a50e527d20018839f006ed312454b710e6486b4`).

---

## 1. Label-Complete Receiver Conjugacy and Coherent Old-Memory Transfer

### 1.1 Half-Line Calibration $\mathcal{T} = \mathcal{T}_1 \oplus \mathcal{T}_2$ and Contact Commutation

Fix the receiver site at $z = 100 \in \mathbb{Z}$. On $\mathscr{H}_{\mathrm{rec}} = (\mathscr{H}_{\mathrm{ch},1} \oplus \mathscr{H}_{\mathrm{ch},2}) \otimes \mathcal{V}_{\mathrm{mem},z} \otimes \mathcal{H}_{\mathrm{aux},\mathrm{ref}}$ where $\mathcal{V}_{\mathrm{mem},z} = \operatorname{span}\{|d_k\rangle : 0 \le k \le 25\}$, define the self-adjoint unitary calibration operator $\mathcal{T} := \mathcal{T}_1 \oplus \mathcal{T}_2$ ($\mathcal{T}^* = \mathcal{T} = \mathcal{T}^{-1}$) by
$$\mathcal{T}_1 := \bigl(\mathbf{1}_{y < z} \otimes I_{\mathrm{tok},\mathrm{mem}} + \mathbf{1}_{y \ge z} \otimes \mathsf{J}_{T,\mathrm{mem}}\bigr) \otimes I_{\mathrm{aux},\mathrm{ref}},$$
$$\mathcal{T}_2 := \bigl(\mathbf{1}_{x < z} \otimes I_{\mathrm{pulse},\mathrm{mem}} + \mathbf{1}_{x \ge z} \otimes \mathsf{J}_{p,\mathrm{mem}}\bigr) \otimes I_{\mathrm{aux},\mathrm{ref}},$$
where $\mathsf{J}_{T,\mathrm{mem}}\bigl(|t_j\rangle \otimes |d_k\rangle\bigr) = |t_k\rangle \otimes |d_j\rangle$ swaps the token label $j$ with the receiver memory label $k$ on $\{y \ge z\}$, and $\mathsf{J}_{p,\mathrm{mem}}\bigl(|p_j\rangle \otimes |d_k\rangle\bigr) = |p_k\rangle \otimes |d_j\rangle$ swaps the pulse label $j$ with the receiver memory label $k$ on $\{x \ge z\}$.

**Theorem 1.1 (Receiver Conjugacy, Wave Operators $\Omega_{\mathrm{rec},\pm}$, and Coherent Old-Memory Transfer).**
1. **Exact commutation with contact at all sites:** At every contact site $s \in \mathbb{Z}$, the homogeneous contact operator $C \otimes I_{\mathrm{rec}}$ acts at $R = y = x = s, r = 0$ with the **identical** $2\times 2$ core matrix $C_{\mathrm{core}} = \begin{pmatrix} 3/5 & -4/5 \\ 4/5 & 3/5 \end{pmatrix}$ on $(\alpha_{s,j}, \beta_{s,j})$ for every label $j \in \{0,\dots,25\}$. For $s < z$, $\mathcal{T} = \mathcal{T}_1 \oplus \mathcal{T}_2$ acts as the identity on both token and pulse channels at $s$; for $s \ge z$, both $\mathcal{T}_1$ and $\mathcal{T}_2$ apply the same label transposition $j \leftrightarrow k$ to $\alpha_{s,j}\otimes|d_k\rangle$ and $\beta_{s,j}\otimes|d_k\rangle$. Therefore $\mathcal{T}$ commutes identically with $C \otimes I_{\mathrm{rec}}$ across the entire lattice:
   $$[\mathcal{T}, C \otimes I_{\mathrm{rec}}] = 0 \qquad (\text{at all contact sites } s \in \mathbb{Z}).$$
   (This is verified exhaustively on all $4 \times 26 \times 26 = 2704$ basis states in Group 3 of `verify.py`, alongside the negative control proving that a single-label contact fails commutation.)
2. **Local receiver bond $D_{\mathrm{rec}}$:** Conjugating the uncoupled evolution $U'_0 := U_0 \otimes I_{\mathrm{rec}}$ by $\mathcal{T}$ leaves the object walk $W$, the token sector ($\mathcal{T}_1(U_{0,1}\otimes I_{\mathrm{rec}})\mathcal{T}_1^* = U_{0,1}\otimes I_{\mathrm{rec}}$ since tokens do not hop across sites), the on-site pulse coin $Q$, and every pulse bond $(x, x+1) \ne (z-1, z)$ unchanged. Only at the single bond $(z-1, z) = (99, 100)$, where $x = z-1 < z$ lies outside the $\mathcal{T}_2$-swap support and $x+1 = z$ lies inside, does $\mathcal{T}_2$ conjugate $E \otimes I_{\mathrm{rec}}$ into the local receiver edge:
   $$D_{\mathrm{rec}}\binom{v_1(z-1, j, k)}{v_2(z, j, k)} = \frac{1}{\sqrt{5}}\begin{pmatrix} I & -2\,\mathrm{SWAP} \\ 2\,\mathrm{SWAP} & I \end{pmatrix}\binom{v_1(z-1, j, k)}{v_2(z, j, k)} = \frac{1}{\sqrt{5}}\binom{v_1(z-1, j, k) - 2v_2(z, k, j)}{2v_1(z-1, k, j) + v_2(z, j, k)}.$$
   Hence $U_{\mathrm{rec}} := \mathcal{T}(U \otimes I_{\mathrm{rec}})\mathcal{T}^* = \mathcal{T}(U_0 \otimes I_{\mathrm{rec}})\mathcal{T}^*(C \otimes I_{\mathrm{rec}})$ is strictly local on the lattice.
3. **Asymptotic receiver gauges $\mathcal{T}_\pm$, wave operators $\Omega_{\mathrm{rec},\pm}$, and scattering operator $\mathcal{S}_{\mathrm{rec}}$ (`homogeneous_source.md` (46)–(49)):** Keep the unchanged free reference unitary $U'_0 := U_0 \otimes I_{\mathrm{rec}}$ on $\mathscr{H}_{\mathrm{rec}}$. On the fiberwise channel reference space $\mathscr{H}_{\mathrm{ch},0} \otimes \mathcal{V}_{\mathrm{mem},z} \otimes \mathcal{H}_{\mathrm{aux},\mathrm{ref}}$ (with orthogonal projection $P_{\mathrm{ch},0} \otimes I_{\mathrm{rec}}$), the asymptotic gauge limits
   $$\mathcal{T}_\pm := \operatorname*{s-lim}_{n\to\pm\infty} (U'_0)^{-n}\mathcal{T}(U'_0)^n \bigl(P_{\mathrm{ch},0} \otimes I_{\mathrm{rec}}\bigr)$$
   exist, commute with $U'_0$, preserve $\mathscr{H}_{\mathrm{ch},0} \otimes \mathcal{V}_{\mathrm{mem},z} \otimes \mathcal{H}_{\mathrm{aux},\mathrm{ref}}$ fiberwise, and act as unitary involutions thereon:
   - On the token arrangement $\mathscr{H}_{\mathrm{ch},0,1} \otimes \mathcal{V}_{\mathrm{mem},z} \otimes \mathcal{H}_{\mathrm{aux},\mathrm{ref}}$, since $U_{0,1}$ fixes the token site $y$, $\mathcal{T}_\pm = \mathcal{T}_1$. Because $\mathcal{T}_1$ acts only on $(y, \text{token-label}, \text{mem})$ and commutes with $W(P)$, it preserves $\mathscr{H}_{\mathrm{ac}}(W(P))$ on every fiber. In particular, for any state prepared at $y_0 = 0 < z = 100$, $\mathcal{T}_- = \mathcal{T}_1 = I$.
   - On the pulse arrangement $\mathscr{H}_{\mathrm{ch},0,2} \otimes \mathcal{V}_{\mathrm{mem},z} \otimes \mathcal{H}_{\mathrm{aux},\mathrm{ref}}$, the two spectral branches $e^{-i(\beta + \sigma\varepsilon(k))}$ ($\sigma \in \{+, -\}$) of $\widetilde{V}(k) = \sum_{\sigma\in\{+,-\}} e^{-i(\beta+\sigma\varepsilon(k))} P_\sigma(k)$ have physical group velocity $v_\sigma(k) = \sigma\varepsilon'(k)$. Define the two-band positive- and negative-velocity spectral projectors (`homogeneous_source.md` (46))
     $$\Pi_{v>0}(k) := \sum_{\sigma\in\{+,-\}} P_\sigma(k)\,\mathbf{1}_{\sigma\varepsilon'(k) > 0}, \qquad \Pi_{v<0}(k) := \sum_{\sigma\in\{+,-\}} P_\sigma(k)\,\mathbf{1}_{\sigma\varepsilon'(k) < 0}$$
     ($\Pi_{v>0}(k) + \Pi_{v<0}(k) = I_{\mathbb{C}^2}$ for $k \notin \{0, \pi\}$, i.e., Lebesgue-a.e. $k$). Because wavepackets in $\operatorname{Ran}\Pi_{v>0}$ propagate into $\{x \ge z\}$ as $n \to +\infty$ and into $\{x < z\}$ as $n \to -\infty$ (and vice versa for $\operatorname{Ran}\Pi_{v<0}$), the full pulse-sector asymptotic receiver calibrations are (`homogeneous_source.md` (47)–(48))
     $$\mathcal{T}_+ = \bigl(\Pi_{v<0} \otimes I_{\mathrm{pulse},\mathrm{mem}} + \Pi_{v>0} \otimes \mathsf{J}_{p,\mathrm{mem}}\bigr) \otimes I_{\mathrm{aux},\mathrm{ref}},$$
     $$\mathcal{T}_- = \bigl(\Pi_{v>0} \otimes I_{\mathrm{pulse},\mathrm{mem}} + \Pi_{v<0} \otimes \mathsf{J}_{p,\mathrm{mem}}\bigr) \otimes I_{\mathrm{aux},\mathrm{ref}}.$$
     On each fiber $K$, $\Pi_{v\gtrless 0}(K - P)$ commutes with $U_{0,2}(K) = \int^\oplus e^{-i\beta}W(P) \otimes V(K - P)\,\frac{dP}{2\pi}$, so $\mathcal{T}_\pm$ preserve $\mathscr{H}_{\mathrm{ac}}(U_0(K)) \otimes \mathcal{V}_{\mathrm{rec}}$ and hence $\mathscr{H}_{\mathrm{ch},0} \otimes \mathcal{V}_{\mathrm{rec}}$.
   Consequently, the receiver wave operators and scattering operator with respect to the unchanged free reference $U'_0 = U_0 \otimes I_{\mathrm{rec}}$ exist on $\mathscr{H}_{\mathrm{ch},0} \otimes \mathcal{V}_{\mathrm{rec}}$ and satisfy
   $$\Omega_{\mathrm{rec},\pm} := \operatorname*{s-lim}_{n\to\pm\infty} U_{\mathrm{rec}}^{-n} (U'_0)^n \bigl(P_{\mathrm{ch},0} \otimes I_{\mathrm{rec}}\bigr) = \mathcal{T}(\Omega_\pm \otimes I_{\mathrm{rec}})\mathcal{T}_\pm^*,$$
   $$\mathcal{S}_{\mathrm{rec}} := \Omega_{\mathrm{rec},+}^*\Omega_{\mathrm{rec},-} = \mathcal{T}_+(\mathcal{S} \otimes I_{\mathrm{rec}})\mathcal{T}_-^*.$$
4. **Coherent old-memory transfer and physical-time error decomposition:** For any initial state $\Psi_{\mathrm{in}} \otimes \Phi_{\mathrm{mem},\mathrm{ref}}$ with token at $y_0 = 0 < z = 100$, token label $t_1$, and arbitrary normalized receiver/reference superposition $\Phi_{\mathrm{mem},\mathrm{ref}} = \sum_{j=0}^{25}|d_j\rangle\otimes|\phi_j\rangle$ ($\sum_{j=0}^{25}\|\phi_j\|^2 = 1$), $\mathcal{T}_-^*(\Psi_{\mathrm{in}}\otimes\Phi_{\mathrm{mem},\mathrm{ref}}) = \Psi_{\mathrm{in}}\otimes\Phi_{\mathrm{mem},\mathrm{ref}}$. On any outgoing positive-band right-moving ($\sigma = +, \varepsilon'(k) > 0$) pulse component $\psi_{\mathrm{out},+} \otimes |p_1\rangle$ of $\mathcal{S}\Psi_{\mathrm{in}}$, $\Pi_{v>0}$ acts as the identity and $\mathcal{T}_+$ applies $\mathsf{J}_{p,\mathrm{mem}}$:
   $$\mathcal{T}_+\left(\psi_{\mathrm{out},+} \otimes |p_1\rangle \otimes \sum_{j=0}^{25}|d_j\rangle\otimes|\phi_j\rangle\right) = \Psi_{\mathrm{free},+} := \psi_{\mathrm{out},+} \otimes \left(\sum_{j=0}^{25}|p_j\rangle \otimes |d_1\rangle \otimes |\phi_j\rangle\right).$$
   For such a normalized outgoing branch state $\Psi_{\mathrm{free},+} \in \operatorname{Ran}Q_{\mathrm{full}}$ ($\|\psi_{\mathrm{out},+}\| = 1$), let
   $$\delta_n := \bigl\|(I - \mathbf{1}_{x \ge z})U_0^n(\psi_{\mathrm{out},+}\otimes|p_1\rangle)\bigr\| \xrightarrow[n\to+\infty]{} 0$$
   be the left-of-receiver spatial tail of the free outgoing pulse packet (so the calibrated free surrogate $\mathcal{T}(U'_0)^n\mathcal{T}_+^*\Psi_{\mathrm{free},+}$ has wrong-memory probability $\|(I - \mathbf{1}_{z=|d_1\rangle})\mathcal{T}(U'_0)^n\mathcal{T}_+^*\Psi_{\mathrm{free},+}\|^2 = \delta_n^2 \to 0$), and let
   $$\widetilde{\eta}_n := \bigl\|U_{\mathrm{rec}}^n\Omega_{\mathrm{rec},+}\Psi_{\mathrm{free},+} - \mathcal{T}(U'_0)^n\mathcal{T}_+^*\Psi_{\mathrm{free},+}\bigr\| = \bigl\|(U^n\Omega_+ - U_0^n)(\psi_{\mathrm{out},+}\otimes|p_1\rangle)\bigr\| \xrightarrow[n\to+\infty]{} 0, \qquad \eta_n := \bigl\|U_{\mathrm{rec}}^n\Omega_{\mathrm{rec},+}\Psi_{\mathrm{free},+} - (U'_0)^n\Psi_{\mathrm{free},+}\bigr\| \xrightarrow[n\to+\infty]{} 0$$
   be the wave-operator approximation errors relative to the calibrated free surrogate and the asymptotic free reference $(U'_0)^n\Psi_{\mathrm{free},+}$. By the triangle inequality (and because $(U'_0)^n\Psi_{\mathrm{free},+}$ already lies in $|d_1\rangle$), the physical interacting branch state $\Psi_{\mathrm{phys},+}(n) := U_{\mathrm{rec}}^n\Omega_{\mathrm{rec},+}\Psi_{\mathrm{free},+}$ satisfies
   $$\bigl\|(I - \mathbf{1}_{z=|d_1\rangle})\Psi_{\mathrm{phys},+}(n)\bigr\| \le \min(\eta_n,\; \delta_n + \widetilde{\eta}_n) \xrightarrow[n\to+\infty]{} 0,$$
   so the physical wrong-memory probability on that branch is bounded by $\min\bigl(\eta_n^2, (\delta_n + \widetilde{\eta}_n)^2\bigr) \to 0$ as $n \to +\infty$, while coherently transferring the entire initial memory superposition and its entanglement with $\mathcal{H}_{\mathrm{aux},\mathrm{ref}}$ into the outgoing pulse label.

---

## 2. One-Carrier Safe-Window Spectral Energy Theorem vs. Native Charge $H_N$

**Proposition 2.1 (Safe-Window Intertwining on the One-Carrier Sector and Distinction from $H_N$).**
1. On the one-carrier reference space $\mathscr{H}_1 \oplus \mathscr{H}_2$, with $\alpha = 3\pi/10$, $\beta = 4\pi/5$, and $a = 2\arctan 2 = \arccos(-3/5) < 3\pi/4$, the additive reference energy generator $H_0 = H_{0,1} \oplus H_{0,2}$ ($U_0 = e^{-iH_0}$, $H_{0,1} = (H_W + \beta I)\otimes I_{\mathrm{tok}}$, $H_{0,2} = H_W\otimes I_{\mathrm{pulse}} + I_{\mathrm{obj}}\otimes H_E$) has spectrum $\sigma(H_0) \subset [\pi/2 - a, 5\pi/2 + a]$ (Proposition 5.3 of `PROOF_CAPTURE_SCATTERING.md`).
2. Because no point in $J_{\mathrm{safe}} = (5\pi/4, 7\pi/4) \supset J_0 = [3\pi/2, 17\pi/10] \supset I_E = [8\pi/5 - 1/1000, 8\pi/5 + 1/1000]$ has a $2\pi$-alias in $[\pi/2 - a, 5\pi/2 + a]$, modular quasi-energy $e^{-iE}$ uniquely determines the additive reference energy $E \in \sigma(H_0)$ on $J_{\mathrm{safe}}$, and $\mathcal{S}_{\mathrm{rec}}$ commutes with the lifted additive reference energy $H_0 \otimes I_{\mathrm{rec}}$ on $\operatorname{Ran}(\mathbf{1}_{J_{\mathrm{safe}}}(H_0)P_{\mathrm{ch},0} \otimes I_{\mathrm{rec}})$.
3. **Explicit bound-branch conditioning vs. two-pulse alias obstruction:** By Proposition 5.4 of `PROOF_CAPTURE_SCATTERING.md`, on the two-pulse sector $\sigma(H^{(2)})$ contains an interval $J_*$ of length $> 4\pi$, so every two-pulse energy has a $2\pi$-alias in $\sigma(H^{(2)})$. Furthermore, even on the one-carrier sector, neither outgoing pulse energy nor receiver memory $|d_1\rangle$ alone is claimed to herald object binding without the explicit bound-branch projector $\Pi_b(P)$ included in $Q_{\mathrm{full}}$ and $Q_{\mathrm{win}}$ (§5 below).
4. **Distinction from native charge $H_N$:** The modular quasi-energy $E \in [-\pi, \pi)$ is the spectral angle of the two-microtick macrostep unitary $U_{\mathrm{rec}}$, whereas the native charge $H_N = 2\sum_\alpha h_\alpha^2$ is an exact integer-valued local occupation observable ($H_N = 10$ on the active sector). Native charge conservation does not define a local current for spectral quasi-energy $E$.

---

## 3. Native Occupancy Intertwiner $\mathcal{I}_{\eta,\xi}$ and Right-Half Charge Pullback

### 3.1 Native-to-Source Object Intertwiner $\mathcal{I}_0 = \mathsf{Emb}\,\Gamma^{-1} D_2^*$

In the native integer-occupation lattice, each site carries 38 integer coordinates $(h_1,\dots,h_{38})$.
- On the object subbank $(h_1, h_2, h_3, h_4)$ at $(x_A, x_B)$, the four coin basis states $|1\rangle, |2\rangle, |3\rangle, |4\rangle$ map via the unitary occupancy embedding $\mathsf{Emb}$ to the four distinct orthonormal native occupation kets $|\mathfrak{o}_d(x_A, x_B)\rangle$ given by `object_codes = [(-1,0,0,-1), (0,-1,-1,0), (1,0,1,0), (0,1,0,1)]`, each having native charge $2\sum_{\alpha=1}^4 h_\alpha^2 = 4$.
- With $D_{\mathrm{coin}} = \operatorname{diag}(1, i)$ and the two-constituent diagonal coin gauge $D_2 = D_{\mathrm{coin}} \otimes D_{\mathrm{coin}} = \operatorname{diag}(1, i, i, -1)$, the real orthogonal native object coin $M_{\mathrm{nat}} = Q \otimes Q$ (where $Q = \frac{1}{\sqrt{5}}\begin{pmatrix} 1 & -2 \\ 2 & 1 \end{pmatrix} = D_{\mathrm{coin}}^* \frac{I_2 + 2i\sigma_x}{\sqrt{5}} D_{\mathrm{coin}}$) and the source coin $M_2$ satisfy (`PROOF_NATIVE.md` (N23)–(N25)):
  $$M_{\mathrm{nat}} = D_2^* M_2 D_2 = \frac{1}{5}\begin{pmatrix} 1 & -2 & -2 & 4 \\ 2 & 1 & -4 & -2 \\ 2 & -4 & 1 & -2 \\ 4 & 2 & 2 & 1 \end{pmatrix}, \qquad M_{\mathrm{nat}} D_2^* = D_2^* M_2, \qquad D_2 M_{\mathrm{nat}} D_2^* = M_2.$$
- In the native gate order, the object step is $F_{\mathrm{nat}} = S_{\mathrm{nat}} M_{\mathrm{nat}} \Gamma_{\mathrm{nat}}$ ($\mathsf{Emb}^* F_{\mathrm{nat}} \mathsf{Emb} = S M_{\mathrm{nat}} \Gamma$), whereas the source object step is $W = \Gamma S M_2$. Defining the unitary intertwiner
  $$\mathcal{I}_0 := \mathsf{Emb}\,\Gamma^{-1} D_2^*,$$
  and using $M_{\mathrm{nat}} D_2^* = D_2^* M_2$ together with $[S, D_2^*] = 0$, we obtain the exact step intertwining identity:
  $$F_{\mathrm{nat}}\mathcal{I}_0 = \mathsf{Emb}\,(S M_{\mathrm{nat}} \Gamma)(\Gamma^{-1} D_2^*) = \mathsf{Emb}\,S M_{\mathrm{nat}} D_2^* = \mathsf{Emb}\,S D_2^* M_2 = \mathsf{Emb}\,\Gamma^{-1} D_2^* (\Gamma S M_2) = \mathcal{I}_0 W.$$
  At the contact site $r = 0$ ($\Gamma = e^{-ig}I$ on $r = 0$), $D_2^*$ maps the source contact coin vectors $iB = \frac{i(|2\rangle - |3\rangle)}{\sqrt{2}}$ and $A = \frac{|1\rangle - |4\rangle}{\sqrt{2}}$ to the real native contact vectors $D_2^*(iB) = \frac{|2\rangle - |3\rangle}{\sqrt{2}}$ and $D_2^* A = \frac{|1\rangle + |4\rangle}{\sqrt{2}}$ (matching `a = (1, -1, 0, 0)` and `b = (0, 0, 1, 1)` in `verify.py` Group 3).

### 3.2 Full Sector and Occupied-Helper Extension $\mathcal{I}_{\eta,\xi}$

Tensoring $\mathcal{I}_0$ with the native code embedding of the 26 token codes ($q=4$), $2\times 26$ pulse codes ($q=4$), and 26 memory codes ($q=2$ at $z=100$), and fixing any static helper occupancy configuration $\eta$ on the nine spectator coordinates $\{16,\dots,23,37\}$ across the lattice together with any external reference state $\xi \in \mathcal{H}_{\mathrm{aux},\mathrm{ref}}$, defines the isometric embedding $\mathcal{I}_{\eta,\xi}$ satisfying:
$$U_{\mathrm{nat}}\mathcal{I}_{\eta,\xi} = \mathcal{I}_{\eta,\xi} U_{\mathrm{rec}}, \qquad \mathcal{I}_{\eta,\xi}^*\mathcal{I}_{\eta,\xi} = I.$$
For any physical cut $\ell \in \mathbb{Z}$ (separating $\mathbb{Z}_{\le \ell}$ from $\mathbb{Z}_{> \ell}$, with $\Theta_\ell(m) := \mathbf{1}_{m > \ell}$), pulling back the full right-half native charge $H_{N,R,\ell}^{\mathrm{full}}$ through $\mathcal{I}_{\eta,\xi}$ yields
$$\mathcal{I}_{\eta,\xi}^* H_{N,R,\ell}^{\mathrm{full}}\mathcal{I}_{\eta,\xi} = N_{R,\ell} + H_{N,R,\ell}^{\mathrm{help}}(\eta)\cdot I,$$
where the active half-space charge operator on $\mathscr{H}_{\mathrm{rec}}$ is diagonal in the position basis (with carrier position $y$ on tokens and $x$ on pulses):
$$N_{R,\ell} = 2\Theta_\ell(x_A) + 2\Theta_\ell(x_B) + 4\Theta_\ell(\text{carrier}) + 2\Theta_\ell(z).$$
Notice that $\Gamma^{-1}D_2^*$ is strictly diagonal at each site $(x_A, x_B)$, so it commutes identically with $\Theta_\ell(x_A)$ and $\Theta_\ell(x_B)$, and the static helper charge $H_{N,R,\ell}^{\mathrm{help}}(\eta)$ is conserved by $U_{\mathrm{rec}}$ and cancels identically from the one-step difference.

---

## 4. Exact Physical-Cut Current Identity at Cut $\ell = 99$

Fix the physical cut at $\ell = z - 1 = 99$ (between $m = 99$ and $m = 100$, so $z = 100 > \ell$ has $2\Theta_{99}(z) = 2$). On the active sector, $N_{R,\ell} + N_{L,\ell} = 10 I$.

**Theorem 4.1 (One-Step Physical Current Across Cut $\ell$).**
Write $U_{\mathrm{rec}} = e^{-i\beta}\Gamma S_{\mathrm{obj}} D_{\mathrm{edge},\mathrm{rec}} D_c C$, where $C$ is the homogeneous contact, $D_c$ applies the on-site object coin $M_2$ on both arrangements and the on-site pulse coin $Q$ on the pulse arrangement, $D_{\mathrm{edge},\mathrm{rec}}$ applies the pulse bond hop (with $\mathrm{SWAP}$ at bond $(99, 100)$), and $S_{\mathrm{obj}}$ shifts $(x_A, x_B)$ by $(v_{A,d}, v_{B,d}) \in \{(-1,-1), (-1,+1), (+1,-1), (+1,+1)\}$. Then at the same synchronized macrostep phase:
$$J_\ell := U_{\mathrm{rec}}^* N_{R,\ell} U_{\mathrm{rec}} - N_{R,\ell} = N_{L,\ell} - U_{\mathrm{rec}}^* N_{L,\ell} U_{\mathrm{rec}} = C^* D_c^* (j_{S,\ell} + j_{E,\ell}) D_c C,$$
where:
1. **Object streaming current $j_{S,\ell}$:**
   $$j_{S,\ell} = 2\sum_{d=1}^{4}\bigl[\Delta_\ell(x_A, v_{A,d}) + \Delta_\ell(x_B, v_{B,d})\bigr]|d\rangle\langle d|, \qquad \Delta_\ell(q, +1) = \mathbf{1}_{q=\ell}, \quad \Delta_\ell(q, -1) = -\mathbf{1}_{q=\ell+1}.$$
2. **Pulse/receiver bond current $j_{E,\ell}$:** Acting on pulse bank $1$ at $x = \ell$ and pulse bank $2$ at $x = \ell + 1$ (and zero elsewhere and on tokens),
   $$j_{E,\ell} = 4\begin{pmatrix} s^2 I & sc\,\mathsf{S}_\ell \\ sc\,\mathsf{S}_\ell & -s^2 I \end{pmatrix} = \frac{4}{5}\begin{pmatrix} 4I & 2\,\mathsf{S}_\ell \\ 2\,\mathsf{S}_\ell & -4I \end{pmatrix}, \qquad \mathsf{S}_\ell = \begin{cases} \mathrm{SWAP}, & \ell = z - 1 = 99, \\ I, & \ell \ne z - 1, \end{cases}$$
   which satisfies $(j_{E,\ell})^2 = \frac{64}{5}P_{\mathrm{bond},\ell}$ (nonzero eigenvalues $\pm 8/\sqrt{5}$), so $\|J_\ell\| \le 4 + \frac{8}{\sqrt{5}}$.

**Proof.** Both $C$ and $D_c$ act strictly at single physical sites ($C$ at $x_A = x_B = s$ where both token+object and pulse+object have total site charge $2+2+4=8$), so $C^* N_{R,\ell} C = N_{R,\ell}$ and $D_c^* N_{R,\ell} D_c = N_{R,\ell}$. Similarly $\Gamma$ and $e^{-i\beta}$ are diagonal in position and commute with $N_{R,\ell}$. Only $S_{\mathrm{obj}}$ and $D_{\mathrm{edge},\mathrm{rec}}$ move charge across cut $\ell$, and they act on disjoint tensor factors and commute. On bond $(99, 100)$, $D_{\mathrm{rec}}$ swaps the pulse label $j$ (charge $4$) and receiver memory label $k$ (charge $2$ at $z=100$), which preserves the charge of the receiver at $z=100$ ($2$) and changes $N_{R,99}$ solely by $4(\|w_2(100)\|^2 - \|v_2(100)\|^2) = \langle v, j_{E,99} v\rangle$. $\square$

---

## 5. Exact Typed Interface Equality of the Capture, Current, and Record Projectors

On the outgoing pulse-channel reference space $\mathscr{H}_{\mathrm{ch},2} \otimes \mathcal{V}_{\mathrm{mem},z} \otimes \mathcal{H}_{\mathrm{aux},\mathrm{ref}}$ in momentum coordinates $(P, k)$ ($K = P + k$), define the typed unwindowed and $K$-windowed joint event projectors (`homogeneous_source.md` (59)–(60), `INTERFACE_COMPARISON.md` §1.2):
$$Q_{\mathrm{full}} := \mathbf{1}_{|P|\le 1/100}\,\mathbf{1}_{I_E}\bigl(\Omega(P) + \beta + \varepsilon(k)\bigr)\,\Pi_b(P) \otimes P_+(k)\,\mathbf{1}_{\varepsilon'(k)>0} \otimes I_{\mathrm{carrier\text{-}label},z} \otimes |d_1\rangle\langle d_1| \otimes I_{\mathrm{aux},\mathrm{ref}},$$
$$Q_{\mathrm{win}} := \mathbf{1}_{I_K}(K)\,Q_{\mathrm{full}} \qquad (I_K = [k_0 - \delta_K, k_0 + \delta_K]),$$
where $I_{\mathrm{carrier\text{-}label},z} = \sum_{j=0}^{25}|p_j\rangle\langle p_j|$ is the identity on all 26 outgoing pulse labels (so outgoing pulses carrying any transferred old-memory label $p_j$, $j \in \{0,\dots,25\}$, are accepted), while the receiver memory at $z = 100$ is projected onto $|d_1\rangle\langle d_1|$.

On the uncoupled channel space $\mathscr{H}_{\mathrm{ch},2}$ prior to $\mathcal{T}_+$, define the corresponding channel projectors selecting outgoing pulse label $|p_1\rangle\langle p_1|$:
$$Q_{\mathrm{ch},\mathrm{full}} := \mathbf{1}_{|P|\le 1/100}\,\mathbf{1}_{I_E}\bigl(\Omega(P) + \beta + \varepsilon(k)\bigr)\,\Pi_b(P) \otimes P_+(k)\,\mathbf{1}_{\varepsilon'(k)>0} \otimes |p_1\rangle\langle p_1|, \qquad Q_{\mathrm{ch},\mathrm{win}} := \mathbf{1}_{I_K}(K)\,Q_{\mathrm{ch},\mathrm{full}}.$$

**Proposition 5.1 (Exact Equality of Interface Projectors, $\mathcal{T}_+$ Pullback, and Physical Lifts).**
1. The three component outgoing projectors on $\mathscr{H}_{\mathrm{ch},2} \otimes \mathcal{V}_{\mathrm{mem},z} \otimes \mathcal{H}_{\mathrm{aux},\mathrm{ref}}$ satisfy the exact operator identity:
   $$A:E_{\mathrm{joint}} = B:Q_{\mathrm{win}} = \mathbf{1}_{I_K}(K)\,C:Q_{\mathrm{joint}} \le C:Q_{\mathrm{joint}} = Q_{\mathrm{full}}.$$
2. Because $\mathcal{T}_+$ acts on $\operatorname{Ran}\mathbf{1}_{\varepsilon'(k)>0}$ by swapping the pulse label $p_j$ and receiver memory label $d_k$ ($\mathsf{J}_{p,\mathrm{mem}}^*(I_{\mathrm{carrier\text{-}label},z}\otimes |d_1\rangle\langle d_1|)\mathsf{J}_{p,\mathrm{mem}} = |p_1\rangle\langle p_1| \otimes I_{\mathrm{mem},z}$), we have the exact operator identities
   $$\mathcal{T}_+^*\,Q_{\mathrm{full}}\,\mathcal{T}_+ = Q_{\mathrm{ch},\mathrm{full}} \otimes I_{\mathrm{mem},z} \otimes I_{\mathrm{aux},\mathrm{ref}}, \qquad \mathcal{T}_+^*\,Q_{\mathrm{win}}\,\mathcal{T}_+ = Q_{\mathrm{ch},\mathrm{win}} \otimes I_{\mathrm{mem},z} \otimes I_{\mathrm{aux},\mathrm{ref}}.$$
3. Lifting via the physical receiver wave operator $\Omega_{\mathrm{rec},+}$ gives the interacting scattering event projectors
   $$E_{\mathrm{scat}}^{\mathrm{win}} = \Omega_{\mathrm{rec},+} Q_{\mathrm{win}} \Omega_{\mathrm{rec},+}^* \le E_{\mathrm{scat}}^{\mathrm{full}} = \Omega_{\mathrm{rec},+} Q_{\mathrm{full}} \Omega_{\mathrm{rec},+}^*,$$
   and for any normalized initial receiver/reference state $\Phi_{\mathrm{mem},\mathrm{ref}} = \sum_{j=0}^{25}|d_j\rangle\otimes|\phi_j\rangle$ ($\|\Phi_{\mathrm{mem},\mathrm{ref}}\| = 1$) with localized incoming preparation $\Psi_{\mathrm{prep}} = \Omega_{\mathrm{rec},-}(\Psi_{\mathrm{loc}} \otimes \Phi_{\mathrm{mem},\mathrm{ref}})$:
   $$p(Q_{\mathrm{full}}) = \langle\Psi_{\mathrm{prep}}, E_{\mathrm{scat}}^{\mathrm{full}}\Psi_{\mathrm{prep}}\rangle = \bigl\|Q_{\mathrm{full}}\,\mathcal{S}_{\mathrm{rec}}(\Psi_{\mathrm{loc}}\otimes\Phi_{\mathrm{mem},\mathrm{ref}})\bigr\|^2 = \bigl\|Q_{\mathrm{ch},\mathrm{full}}\,\mathcal{S}\Psi_{\mathrm{loc}}\bigr\|^2$$
   $$\ge p(Q_{\mathrm{win}}) = \bigl\|Q_{\mathrm{win}}\,\mathcal{S}_{\mathrm{rec}}(\Psi_{\mathrm{loc}}\otimes\Phi_{\mathrm{mem},\mathrm{ref}})\bigr\|^2 = \bigl\|Q_{\mathrm{ch},\mathrm{win}}\,\mathcal{S}\Psi_{\mathrm{loc}}\bigr\|^2 \ge \frac{\delta_K}{\pi}\,B_{\mathrm{hom}} > \frac{2}{10^{28}}.$$

---

## 6. Causal History Reconstruction $L_m$, Dark-State Counterexample, and Infinite-Carrier No-Go

### 6.1 Exact Causal History Reconstruction $L_m$

Write $U_{\mathrm{rec}} = \begin{pmatrix} A & B \\ G & D \end{pmatrix}$ on $\mathcal{H}_T \oplus \mathcal{H}_P$, where $A = U_T(I - hP_T)$, $B = -\kappa U_T K^*$, $G = \kappa U_P K$, $D = U_P(I - hP_P)$ ($h = 2/5, \kappa = 4/5$).
For any initial state $(t_0, p_0) \in \mathcal{H}_T \oplus \mathcal{H}_P$ (including arbitrary dark object components in $t_0$) and any finite horizon $m \ge 0$, the exact state $(\rho_m, p_m) = U_{\mathrm{rec}}^m(t_0, p_0)$ is reconstructed from the history $H_m = (t_0, p_0, \dots, p_m)$ by the bounded linear map
$$L_m H_m = \begin{pmatrix} E_m & F_{m,0} & \cdots & F_{m,m-1} & 0 \\ 0 & 0 & \cdots & 0 & I \end{pmatrix}H_m = (\rho_m, p_m), \qquad E_m = A^m, \quad F_{m,j} = A^{m-1-j}B,$$
and the half-space charge pairing $\mathcal{Q}_\ell^{(m)}(H_m, \widetilde{H}_m) = \langle\rho_m, N_\ell^T\widetilde{\rho}_m\rangle + \langle p_m, N_\ell^P\widetilde{p}_m\rangle$ satisfies exact step-by-step continuity $\mathcal{Q}_\ell^{(m+1)}(H_{m+1}, \widetilde{H}_{m+1}) - \mathcal{Q}_\ell^{(m)}(H_m, \widetilde{H}_m) = \mathfrak{j}_\ell^{(m)}(H_m, \widetilde{H}_m)$.

### 6.2 Dark-State Obstruction to Pulse-History-Only Current

At standing token site $n$, the inversion $\mathcal{R}_n|R, r, d\rangle = |2n-R, -r, 5-d\rangle$ commutes with $W$ and satisfies $\mathcal{R}_n\alpha_n = -\alpha_n$, so the contact-generated cyclic subspace $\mathcal{K}_n = \overline{\operatorname{span}}\{W^k\alpha_n : k \in \mathbb{Z}\}$ is $\mathcal{R}_n$-odd.
The normalized $\mathcal{R}_n$-even state
$$d = \frac{1}{2}\bigl(|n-1,-1,1\rangle + |n+1,1,4\rangle - |n-1,1,1\rangle - |n+1,-1,4\rangle\bigr) \in \mathcal{K}_n^\perp$$
is completely dark to the contact at all times ($\langle\alpha_n, W^m d\rangle = 0$ for all $m \in \mathbb{Z}$). Setting $\chi_0 = W\alpha_n$ and $d_0 = W^* d$, both $\chi_0$ and $d_0$ have zero initial contact projection at $m = 0$ ($\langle\alpha_n, \chi_0\rangle = \langle\alpha_n, W\alpha_n\rangle = 0$ and $\langle\alpha_n, d_0\rangle = 0$), while at $m = 1$, $\langle\alpha_n, W\chi_0\rangle = \frac{4}{5}e^{-ig} \ne 0$ and $\langle\alpha_n, W^m d_0\rangle = 0$ for all $m \ge 0$. Because $C - I$ annihilates $(d_0, 0)$ and every $U_{\mathrm{rec}}^m(d_0, 0) = (U_T^m d_0, 0)$, the normalized initial states $\psi_\pm = \bigl(\frac{\chi_0 \pm d_0}{\sqrt{2}}, 0\bigr)$ produce **identical (nonzero) pulse output histories $\{p_m\}_{m \ge 0}$ at all times $m \ge 0$**, yet at cut $\ell = n$ ($z = n+1$) their initial physical currents differ by $\frac{4\sqrt{2}}{5}$:
$$\langle\psi_\pm, J_n\psi_\pm\rangle = -\frac{13}{10} \pm \frac{2\sqrt{2}}{5}.$$
Thus $J_n$ cannot be written as a function of the pulse history alone on the full domain without retaining $t_0$ in $L_m$ (or restricting initial preparations in advance to the reducing subspace $\mathscr{S} = (\bigoplus_n \mathcal{K}_n) \oplus \mathcal{H}_P$, where $I_{\mathscr{S}}^* J_\ell I_{\mathscr{S}} = U_{\mathscr{S}}^* N_{\mathscr{S},\ell} U_{\mathscr{S}} - N_{\mathscr{S},\ell}$).

### 6.3 Three Infinite-Carrier No-Go Theorems (Without P24)

**Theorem 6.1 (No Finite Invariant Carrier, No Finite Linear Memory, No Finite Current Factor).**
1. **No finite invariant contact carrier:** For $\alpha' = |R=0, r=0\rangle \otimes i(|2\rangle - |3\rangle)$ and $T = e^{-i\beta}W$, the extreme coordinate $(R=0, r=m, d=3)$ of $T^m\alpha'$ is
   $$\langle 0, m, 3 | T^m\alpha'\rangle = -i\,e^{-im\beta}\,5^{1-m} \ne 0 \qquad (\forall m \ge 1),$$
   while $\langle 0, m, 3 | T^k\alpha'\rangle = 0$ for all $0 \le k < m$. Thus $\{T^m\alpha'\}_{m \ge 0}$ is linearly independent, and no finite-dimensional $T$-invariant subspace contains $\alpha'$.
2. **No finite-dimensional linear contact memory (proved without P24):** By Public Canon v104 (`CONTACT-W-SPECTRAL-READING [T]`), the full operator $W$ has two open spectral gaps of width at least $\arccos(7/25) - 2\pi/5 > 3/100 > 0$, so the spectral probability measure $\mu_\alpha$ of $T$ on $\alpha = \alpha'/\sqrt{2}$ has a nonempty open gap on $\mathbb{T}$. If the Carathéodory function $F(z) = \int \frac{1+ze^{-iE}}{1-ze^{-iE}}\,d\mu_\alpha(E)$ (or the scalar contact transfer function $s(z) = \frac{4-F(z)}{4+F(z)}$) were rational, Schwarz reflection $F(z) + \overline{F(1/\bar{z})} \equiv 0$ across the open gap arc would force $\mu_\alpha$ to be supported on finitely many points (the poles of $F$ on $\mathbb{T}$), contradicting the infinite linear independence of $\{T^m\alpha'\}_{m \ge 0}$. Therefore no finite-dimensional time-independent linear state-space realization (unitary or dissipative) can reproduce the exact contact response for all input histories and all times. This proof uses only Theorem 6.1(1) and the canonical spectral gap, with zero dependence on the qualitative a.e. positive-density statement (P24).
3. **No finite-dimensional full-state current factor:** For any cut $\ell$ and every integer $j \ge 1$, the orthonormal token states $e_j^+ = |x_A = \ell, x_B = \ell - 2j, d = 3\rangle$ and $e_j^- = |x_A = \ell + 1, x_B = \ell + 1 + 2j, d = 2\rangle$ satisfy $(j_{S,\ell} + j_{E,\ell})e_j^\pm = \pm 2 e_j^\pm$, so $(D_c C)^* e_j^\pm$ are infinitely many orthonormal eigenvectors of $J_\ell$ with eigenvalues $+2$ and $-2$. Hence $J_\ell$ cannot factor as $L^* H L$ through any finite-dimensional linear map $L$ on all finite-support encoded states.
