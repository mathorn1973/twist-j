# Receiver Conjugacy, Native Intertwiner, Physical Cut Current, and Infinite-Carrier No-Go

**PUBLIC, NON-CANONICAL. Self-contained analytical proof (`PROOF_CURRENT_RECORD_INTERFACE.md`) for `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N`.**

Owner: A. M. Thorn. License: Apache-2.0.
Authority basis: `mathorn1973/twist-j` main `e6240e2689bb22aab5f02bad90b75d3692bb96d9` (Public Canon v104, content commit `4a50e527d20018839f006ed312454b710e6486b4`).

---

## 1. Label-Complete Receiver Conjugacy and Coherent Old-Memory Transfer

### 1.1 Half-Line Calibration $\mathcal{T}$ and Contact Commutation

Fix the receiver site at $z = 100 \in \mathbb{Z}$. On $\mathcal{H} \otimes \mathcal{V}_{\mathrm{rec}} \otimes \mathcal{H}_{\mathrm{ref}}$ where $\mathcal{V}_{\mathrm{rec}} = \operatorname{span}\{|d_k\rangle : 0 \le k \le 25\}$, define the self-adjoint unitary calibration operator $\mathcal{T} = \mathcal{T}^* = \mathcal{T}^{-1}$ by:
$$\mathcal{T}\bigl(|\psi_{\mathrm{obj}}\rangle \otimes |\mathrm{tok}_j(y)\rangle \otimes |d_k\rangle\bigr) = |\psi_{\mathrm{obj}}\rangle \otimes |\mathrm{tok}_j(y)\rangle \otimes |d_k\rangle \qquad (\forall y \in \mathbb{Z}),$$
$$\mathcal{T}\bigl(|\psi_{\mathrm{obj}}\rangle \otimes |p_{j,b}(y)\rangle \otimes |d_k\rangle\bigr) = \begin{cases} |\psi_{\mathrm{obj}}\rangle \otimes |p_{j,b}(y)\rangle \otimes |d_k\rangle, & y < z, \\ |\psi_{\mathrm{obj}}\rangle \otimes |p_{k,b}(y)\rangle \otimes |d_j\rangle, & y \ge z. \end{cases}$$

**Theorem 1.1 (Receiver Conjugacy, Wave Operators, and Coherent Old-Memory Transfer).**
1. **Exact commutation with contact:** Because the homogeneous contact $C$ acts with the **identical** $4\times 4$ matrix on every label $j \in \{0,\dots,25\}$ at every site $y \in \mathbb{Z}$, swapping the carrier label $j$ with the receiver label $k$ at $y \ge z$ commutes with $C \otimes I_{\mathrm{rec}}$:
   $$[\mathcal{T}, C \otimes I_{\mathrm{rec}}] = 0.$$
   (This is verified exhaustively on all $4 \times 26 \times 26 = 2704$ basis states in Group 3 of `verify.py`, alongside the negative control proving that a single-label contact fails commutation.)
2. **Local receiver bond $D_{\mathrm{rec}}$:** Conjugating the free step $U_0 \otimes I_{\mathrm{rec}}$ by $\mathcal{T}$ leaves the object walk $W$, the token sector, the on-site pulse coin $Q$, and every pulse bond $(y, y+1) \ne (z-1, z)$ unchanged. Only at the single bond $(z-1, z) = (99, 100)$, where $y = z-1 < z$ lies outside the $\mathcal{T}$-support and $y+1 = z$ lies inside, does $\mathcal{T}$ conjugate $D_{\mathrm{edge}} \otimes I_{\mathrm{rec}}$ into the local receiver edge:
   $$D_{\mathrm{rec}}\binom{v_1(z-1, j, k)}{v_2(z, j, k)} = \frac{1}{\sqrt{5}}\begin{pmatrix} I & -2\,\mathrm{SWAP} \\ 2\,\mathrm{SWAP} & I \end{pmatrix}\binom{v_1(z-1, j, k)}{v_2(z, j, k)} = \frac{1}{\sqrt{5}}\binom{v_1(z-1, j, k) - 2v_2(z, k, j)}{2v_1(z-1, k, j) + v_2(z, j, k)}.$$
   Hence $U_{\mathrm{rec}} = \mathcal{T}(U \otimes I_{\mathrm{rec}})\mathcal{T}^* = U_{\mathrm{rec},0}(C \otimes I_{\mathrm{rec}})$ is strictly local on the lattice.
3. **Conjugated wave operators and scattering operator:** With reference free evolution $U_{\mathrm{rec},0} = \mathcal{T}(U_0 \otimes I_{\mathrm{rec}})\mathcal{T}^*$, the receiver wave operators and scattering operator are
   $$\Omega_{\mathrm{rec},\pm} = \mathcal{T}(\Omega_\pm \otimes I_{\mathrm{rec}})\mathcal{T}^*, \qquad S_{\mathrm{rec}} = \Omega_{\mathrm{rec},+}^*\Omega_{\mathrm{rec},-} = \mathcal{T}(S \otimes I_{\mathrm{rec}})\mathcal{T}^*.$$
4. **Coherent old-memory transfer:** For any initial state prepared on $y = 0 < z = 100$ with token label $1$ and an arbitrary receiver/reference state $\Phi_{\mathrm{mem},\mathrm{ref}} = \sum_{j=0}^{25}|d_j\rangle\otimes|\phi_j\rangle$, $\mathcal{T}$ acts as the identity on the incoming state ($\mathcal{T}^*(\Psi_{\mathrm{in}}\otimes\Phi_{\mathrm{mem},\mathrm{ref}}) = \Psi_{\mathrm{in}}\otimes\Phi_{\mathrm{mem},\mathrm{ref}}$). On any outgoing right-moving pulse wavepacket $\psi_{\mathrm{out},1}$ carrying label $1$, since $\|(I - \mathbf{1}_{y \ge z})U_0^n\psi_{\mathrm{out},1}\| =: \delta_n \to 0$ as $n \to +\infty$, $\mathcal{T}$ maps the $y \ge z$ support according to
   $$|p_1\rangle \otimes \sum_{j=0}^{25}|d_j\rangle\otimes|\phi_j\rangle \;\longmapsto\; \sum_{j=0}^{25}|p_j\rangle \otimes |d_1\rangle \otimes |\phi_j\rangle.$$
   Thus the receiver deterministically records $|d_1\rangle$ (wrong-memory probability $\le \delta_n^2 \to 0$) while coherently transferring the entire initial memory superposition and its entanglement with $\mathcal{H}_{\mathrm{ref}}$ into the outgoing pulse label.

---

## 2. Safe-Window Spectral Energy Theorem vs. Native Charge $H_N$

**Proposition 2.1 (Safe-Window Binding Guarantee and Distinction from $H_N$).**
1. Because $U_{\mathrm{rec}}$ is unitarily equivalent to $U \otimes I_{\mathrm{rec}}$, its spectral measure on any Borel set $J \subset \mathbb{T}$ is $\mathcal{T}(\mathrm{E}_U(J) \otimes I_{\mathrm{rec}})\mathcal{T}^*$.
2. On the incoming preparation $\Psi_{\mathrm{prep}} = \Omega_{\mathrm{rec},-}(\Psi_{\mathrm{in}}\otimes\Phi_{\mathrm{mem},\mathrm{ref}})$, the spectral support of $U_{\mathrm{rec}}$ lies strictly inside $I_E = [8\pi/5 - 1/1000, 8\pi/5 + 1/1000] \subset J_0 = [3\pi/2, 17\pi/10] \subset J_{\mathrm{safe}} = (5\pi/4, 7\pi/4)$.
3. By Proposition 5.2 of `PROOF_CAPTURE_SCATTERING.md`, the unbound two-pulse continuum has quasi-energy in $[-4\arctan 2, 4\arctan 2] \pmod{2\pi}$, which is disjoint from $J_{\mathrm{safe}}$. Consequently, inside $\mathcal{H}_{I_E}(U_{\mathrm{rec}})$, every outgoing pulse-arrangement state automatically lies in the bound-object sector $\operatorname{Ran}\Pi_b$.
4. **Distinction from native charge $H_N$:** The modular quasi-energy $E \in [-\pi, \pi)$ is the spectral angle of the two-microtick macrostep unitary $U_{\mathrm{rec}}$ ($U_{\mathrm{rec}} = \int e^{-iE}\,d\mathrm{E}(E)$), whereas the native charge $H_N = 2\sum_\alpha h_\alpha^2$ is an exact integer-valued local occupation observable ($H_N = 10$ on the active sector). Native charge conservation does not define a local current for spectral quasi-energy $E$, and the safe-window theorem applies to the one-pair, one-carrier sector, not to arbitrary multi-carrier or asynchronous sectors.

---

## 3. Native Occupancy Intertwiner $\mathcal{I}_{\eta,\xi}$ and Right-Half Charge Pullback

### 3.1 Native-to-Source Object Intertwiner $\mathcal{I}_0 = \mathsf{Emb}\,\Gamma^{-1} D_2^*$

In the native integer-occupation lattice, each site carries 38 integer coordinates $(h_1,\dots,h_{38})$.
- On the object subbank $(h_1, h_2, h_3, h_4)$ at $(x_A, x_B)$, the four coin basis states $|1\rangle, |2\rangle, |3\rangle, |4\rangle$ map via the unitary occupancy embedding $\mathsf{Emb}$ to the four distinct orthonormal native occupation kets $|\mathfrak{o}_d(x_A, x_B)\rangle$ given by `object_codes = [(-1,0,0,-1), (0,-1,-1,0), (1,0,1,0), (0,1,0,1)]`, each having native charge $2\sum_{\alpha=1}^4 h_\alpha^2 = 4$.
- The diagonal coin gauge $D_2 = \operatorname{diag}(1, i, i, -1)$ intertwines the real orthogonal native object coin $M_{\mathrm{nat}}$ and the source coin $M_2$:
  $$D_2^* M_{\mathrm{nat}} D_2 = M_2.$$
- In the native gate order, the object step is $F_{\mathrm{nat}} = S_{\mathrm{nat}} M_{\mathrm{nat}} \Gamma_{\mathrm{nat}}$, whereas the source object step is $W = \Gamma S M_2$. Defining the unitary intertwiner
  $$\mathcal{I}_0 := \mathsf{Emb}\,\Gamma^{-1} D_2^*,$$
  we have $F_{\mathrm{nat}}\mathcal{I}_0 = (\mathsf{Emb}\,S D_2 M_2 D_2^* \Gamma\mathsf{Emb}^*)(\mathsf{Emb}\,\Gamma^{-1}D_2^*) = \mathsf{Emb}\,\Gamma^{-1}D_2^*(\Gamma S M_2) = \mathcal{I}_0 W$.

### 3.2 Full Sector and Occupied-Helper Extension $\mathcal{I}_{\eta,\xi}$

Tensoring $\mathcal{I}_0$ with the native code embedding of the 26 token codes ($q=4$), $2\times 26$ pulse codes ($q=4$), and 26 memory codes ($q=2$ at $z=100$), and fixing any static helper occupancy configuration $\eta$ on the nine spectator coordinates $\{16,\dots,23,37\}$ across the lattice together with any external reference state $\xi \in \mathcal{H}_{\mathrm{ref}}$, defines the isometric embedding $\mathcal{I}_{\eta,\xi}$ satisfying:
$$U_{\mathrm{nat}}\mathcal{I}_{\eta,\xi} = \mathcal{I}_{\eta,\xi} U_{\mathrm{rec}}, \qquad \mathcal{I}_{\eta,\xi}^*\mathcal{I}_{\eta,\xi} = I.$$
For any physical cut $\ell \in \mathbb{Z}$ (separating $\mathbb{Z}_{\le \ell}$ from $\mathbb{Z}_{> \ell}$, with $\Theta_\ell(m) := \mathbf{1}_{m > \ell}$), pulling back the full right-half native charge $H_{N,R,\ell}^{\mathrm{full}}$ through $\mathcal{I}_{\eta,\xi}$ yields
$$\mathcal{I}_{\eta,\xi}^* H_{N,R,\ell}^{\mathrm{full}}\mathcal{I}_{\eta,\xi} = N_{R,\ell} + H_{N,R,\ell}^{\mathrm{help}}(\eta)\cdot I,$$
where the active half-space charge operator on $\mathcal{H}_{\mathrm{tok}} \oplus \mathcal{H}_{\mathrm{pulse}}$ is diagonal in the position basis:
$$N_{R,\ell} = 2\Theta_\ell(x_A) + 2\Theta_\ell(x_B) + 4\Theta_\ell(y) + 2\Theta_\ell(z).$$
Notice that $\Gamma^{-1}D_2^*$ is strictly diagonal at each site $(x_A, x_B)$, so it commutes identically with $\Theta_\ell(x_A)$ and $\Theta_\ell(x_B)$, and the static helper charge $H_{N,R,\ell}^{\mathrm{help}}(\eta)$ is conserved by $U_{\mathrm{rec}}$ and cancels identically from the one-step difference!

---

## 4. Exact Physical-Cut Current Identity at Cut $\ell = 99$

Fix the physical cut at $\ell = z - 1 = 99$ (between $m = 99$ and $m = 100$, so $z = 100 > \ell$ has $2\Theta_{99}(z) = 2$). On the active sector, $N_{R,\ell} + N_{L,\ell} = 10 I$.

**Theorem 4.1 (One-Step Physical Current Across Cut $\ell$).**
Write $U_{\mathrm{rec}} = e^{-i\beta}\Gamma S_{\mathrm{obj}} D_{\mathrm{edge},\mathrm{rec}} D_c C$, where $C$ is the homogeneous contact (I3), $D_c$ applies the on-site object coin $M_2$ on both arrangements and the on-site pulse coin $Q$ on the pulse arrangement, $D_{\mathrm{edge},\mathrm{rec}}$ applies the pulse bond hop (with $\mathrm{SWAP}$ at bond $(99, 100)$), and $S_{\mathrm{obj}}$ shifts $(x_A, x_B)$ by $(v_{A,d}, v_{B,d}) \in \{(-1,-1), (-1,+1), (+1,-1), (+1,+1)\}$. Then at the same synchronized macrostep phase:
$$J_\ell := U_{\mathrm{rec}}^* N_{R,\ell} U_{\mathrm{rec}} - N_{R,\ell} = N_{L,\ell} - U_{\mathrm{rec}}^* N_{L,\ell} U_{\mathrm{rec}} = C^* D_c^* (j_{S,\ell} + j_{E,\ell}) D_c C,$$
where:
1. **Object streaming current $j_{S,\ell}$:**
   $$j_{S,\ell} = 2\sum_{d=1}^{4}\bigl[\Delta_\ell(x_A, v_{A,d}) + \Delta_\ell(x_B, v_{B,d})\bigr]|d\rangle\langle d|, \qquad \Delta_\ell(q, +1) = \mathbf{1}_{q=\ell}, \quad \Delta_\ell(q, -1) = -\mathbf{1}_{q=\ell+1}.$$
2. **Pulse/receiver bond current $j_{E,\ell}$:** Acting on pulse bank $1$ at $y = \ell$ and pulse bank $2$ at $y = \ell + 1$ (and zero elsewhere and on tokens),
   $$j_{E,\ell} = 4\begin{pmatrix} s^2 I & sc\,\mathsf{S}_\ell \\ sc\,\mathsf{S}_\ell & -s^2 I \end{pmatrix} = \frac{4}{5}\begin{pmatrix} 4I & 2\,\mathsf{S}_\ell \\ 2\,\mathsf{S}_\ell & -4I \end{pmatrix}, \qquad \mathsf{S}_\ell = \begin{cases} \mathrm{SWAP}, & \ell = z - 1 = 99, \\ I, & \ell \ne z - 1, \end{cases}$$
   which satisfies $(j_{E,\ell})^2 = \frac{64}{5}P_{\mathrm{bond},\ell}$ (nonzero eigenvalues $\pm 8/\sqrt{5}$), so $\|J_\ell\| \le 4 + \frac{8}{\sqrt{5}}$.

**Proof.** Both $C$ and $D_c$ act strictly at single physical sites ($C$ at $x_A = x_B = y$ where both token+object and pulse+object have total site charge $2+2+4=8$), so $C^* N_{R,\ell} C = N_{R,\ell}$ and $D_c^* N_{R,\ell} D_c = N_{R,\ell}$. Similarly $\Gamma$ and $e^{-i\beta}$ are diagonal in position and commute with $N_{R,\ell}$. Only $S_{\mathrm{obj}}$ and $D_{\mathrm{edge},\mathrm{rec}}$ move charge across cut $\ell$, and they act on disjoint tensor factors and commute. On bond $(99, 100)$, $D_{\mathrm{rec}}$ swaps the pulse label $j$ (charge $4$) and receiver memory label $k$ (charge $2$ at $z=100$), which preserves the charge of the receiver at $z=100$ ($2$) and changes $N_{R,99}$ solely by $4(\|w_2(100)\|^2 - \|v_2(100)\|^2) = \langle v, j_{E,99} v\rangle$. $\square$

---

## 5. Exact Interface Equality of the Capture, Current, and Record Projectors

On the free outgoing reference space $\mathcal{H} \otimes \mathcal{V}_{\mathrm{rec}} \otimes \mathcal{H}_{\mathrm{ref}}$, let:
- $\Pi_b^{\mathrm{out}}(K, [-p_b, p_b]) = \mathbf{1}_{[-p_b, p_b]}(P)\Pi_b(P)$ be the bound-pair projector on outgoing center-momentum window $[-p_b, p_b]$ ($p_b = 1/100$),
- $P_{\mathrm{pulse},1,+}(K) = P_{\mathrm{pulse},+}(K-P) \otimes |p_1\rangle\langle p_1|$ be the right-moving pulse projector at $k = K - P$ with outgoing pulse label $1$ before $\mathcal{T}$ (which after $\mathcal{T}$ on $y \ge z$ becomes $\sum_{j=0}^{25}|p_j\rangle\langle p_j| \otimes |d_1\rangle\langle d_1|$),
- $R_1 = I_{\mathcal{H}} \otimes |d_1\rangle\langle d_1| \otimes I_{\mathrm{ref}}$ be the receiver record projector onto $|d_1\rangle$.

**Proposition 5.1 (Exact Equality of Interface Projectors and Physical Lifts).**
1. The three component outgoing projectors on the calibrated reference space satisfy the exact operator identity:
   $$A:E_{\mathrm{joint}} = B:Q_{\mathrm{win}} = \mathbf{1}_{I_K}(K)\,C:Q_{\mathrm{joint}} \le C:Q_{\mathrm{joint}} = Q_{\mathrm{full}},$$
   where
   $$Q_{\mathrm{full}} = \int_{[-\pi,\pi)}^{\oplus} \Pi_b^{\mathrm{out}}(K, [-p_b, p_b])\,P_{\mathrm{pulse},+}(K-P)\,\frac{dK}{2\pi} \otimes I_{\mathrm{label}} \otimes |d_1\rangle\langle d_1| \otimes I_{\mathrm{ref}}, \qquad Q_{\mathrm{win}} = \mathbf{1}_{I_K}(K)\,Q_{\mathrm{full}}.$$
2. Lifting via the physical receiver wave operator $\Omega_{\mathrm{rec},+}$ gives the interacting scattering event projectors
   $$E_{\mathrm{scat}}^{\mathrm{win}} = \Omega_{\mathrm{rec},+} Q_{\mathrm{win}} \Omega_{\mathrm{rec},+}^* \le E_{\mathrm{scat}}^{\mathrm{full}} = \Omega_{\mathrm{rec},+} Q_{\mathrm{full}} \Omega_{\mathrm{rec},+}^*,$$
   and on $\Psi_{\mathrm{prep}} = \Omega_{\mathrm{rec},-}(\Psi_{\mathrm{in}} \otimes \Phi_{\mathrm{mem},\mathrm{ref}})$:
   $$p(Q_{\mathrm{full}}) = \langle\Psi_{\mathrm{prep}}, E_{\mathrm{scat}}^{\mathrm{full}}\Psi_{\mathrm{prep}}\rangle = \|Q_{\mathrm{full}} S_{\mathrm{rec}}(\Psi_{\mathrm{in}}\otimes\Phi_{\mathrm{mem},\mathrm{ref}})\|^2 \ge p(Q_{\mathrm{win}}) = \|Q_{\mathrm{win}} S_{\mathrm{rec}}(\Psi_{\mathrm{in}}\otimes\Phi_{\mathrm{mem},\mathrm{ref}})\|^2 > \frac{2}{10^{28}}.$$

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
is completely dark to the contact at all times. Setting $\chi_0 = W\alpha_n$ and $d_0 = W^* d$, the normalized initial states $\psi_\pm = \bigl(\frac{\chi_0 \pm d_0}{\sqrt{2}}, 0\bigr)$ have **identical zero pulse output histories at all times**, yet at cut $\ell = n$ ($z = n+1$) their first physical currents differ by $\frac{4\sqrt{2}}{5}$:
$$\langle\psi_\pm, J_n\psi_\pm\rangle = -\frac{13}{10} \pm \frac{2\sqrt{2}}{5}.$$
Thus $J_n$ cannot be written as a function of the pulse history alone on the full domain without retaining $t_0$ in $L_m$ (or restricting initial preparations in advance to the reducing subspace $\mathscr{S} = (\bigoplus_n \mathcal{K}_n) \oplus \mathcal{H}_P$, where $I_{\mathscr{S}}^* J_\ell I_{\mathscr{S}} = U_{\mathscr{S}}^* N_{\mathscr{S},\ell} U_{\mathscr{S}} - N_{\mathscr{S},\ell}$).

### 6.3 Three Infinite-Carrier No-Go Theorems (Without P24)

**Theorem 6.1 (No Finite Invariant Carrier, No Finite Linear Memory, No Finite Current Factor).**
1. **No finite invariant contact carrier:** For $\alpha' = |R=0, r=0\rangle \otimes i(|2\rangle - |3\rangle)$ and $T = e^{-i\beta}W$, the extreme coordinate $(R=0, r=m, d=3)$ of $T^m\alpha'$ is
   $$\langle 0, m, 3 | T^m\alpha'\rangle = -i\,e^{-im\beta}\,5^{1-m} \ne 0 \qquad (\forall m \ge 1),$$
   while $\langle 0, m, 3 | T^k\alpha'\rangle = 0$ for all $0 \le k < m$. Thus $\{T^m\alpha'\}_{m \ge 0}$ is linearly independent, and no finite-dimensional $T$-invariant subspace contains $\alpha'$.
2. **No finite-dimensional linear contact memory (proved without P24):** By Public Canon v104 (`CONTACT-W-SPECTRAL-READING [T]`), the full operator $W$ has two open spectral gaps of width at least $\arccos(7/25) - 2\pi/5 > 3/100 > 0$, so the spectral probability measure $\mu_\alpha$ of $T$ on $\alpha = \alpha'/\sqrt{2}$ has a nonempty open gap on $\mathbb{T}$. If the Carathéodory function $F(z) = \int \frac{1+ze^{-iE}}{1-ze^{-iE}}\,d\mu_\alpha(E)$ (or the scalar contact transfer function $s(z) = \frac{4-F(z)}{4+F(z)}$) were rational, Schwarz reflection $F(z) + \overline{F(1/\bar{z})} \equiv 0$ across the open gap arc would force $\mu_\alpha$ to be supported on finitely many points (the poles of $F$ on $\mathbb{T}$), contradicting the infinite linear independence of $\{T^m\alpha'\}_{m \ge 0}$. Therefore no finite-dimensional time-independent linear state-space realization (unitary or dissipative) can reproduce the exact contact response for all input histories and all times. This proof uses only Theorem 6.1(1) and the canonical spectral gap, with zero dependence on the qualitative a.e. positive-density statement (P24).
3. **No finite-dimensional full-state current factor:** For any cut $\ell$ and every integer $j \ge 1$, the orthonormal token states $e_j^+ = |x_A = \ell, x_B = \ell - 2j, d = 3\rangle$ and $e_j^- = |x_A = \ell + 1, x_B = \ell + 1 + 2j, d = 2\rangle$ satisfy $(j_{S,\ell} + j_{E,\ell})e_j^\pm = \pm 2 e_j^\pm$, so $(D_c C)^* e_j^\pm$ are infinitely many orthonormal eigenvectors of $J_\ell$ with eigenvalues $+2$ and $-2$. Hence $J_\ell$ cannot factor as $L^* H L$ through any finite-dimensional linear map $L$ on all finite-support encoded states.
