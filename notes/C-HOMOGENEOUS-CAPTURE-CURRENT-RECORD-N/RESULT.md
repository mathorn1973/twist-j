# Result Summary: `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N`

**Status:** `NON-CANONICAL` (Research-Note & First-Principles Reproduction Result Summary)  
**Claim ID:** `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N`  
**Base Commit (`main`):** `e6240e2689bb22aab5f02bad90b75d3692bb96d9`  
**Active Prospective Source Pin Commit (Pin 3):** `4c7287debe0f28930acb9a9da20a9ba79d41d7d2`  
**Execution Record:** `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/RUN.md`

---

## 1. Executive Outcome

The preregistered first-principles standard-library verification suite `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py` (pinned prospectively at commit `4c7287debe0f28930acb9a9da20a9ba79d41d7d2` with SHA-256 `589d0a34042ea88ea9f5246e84585d716d194deafb4a8d58613e5dbbd4eea470`; see `RUN.md` §1 for the complete `Pin 1 -> Run 1`, `Pin 2 -> Run 2`, `Pin 3 -> Run 3` chronology) executed with **exit code `0`**, **`0` bytes on `stderr`**, and **141 passed checks across all 6 frozen check groups**, producing `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/EXPECTED.txt` (`708` bytes, SHA-256 `1c0d4c4459a4ae52a74adf6d1206ff4eb91a9042f200708c5a8d06aeb831a43b`).

Every mathematical premise required for the connected asymptotic capture-current-record theorem on the one-pair, one-carrier (standing token or moving pulse), one-receiver sector is proved in `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_*.md` and certified from first principles in standard-library Python without external libraries, floating-point arithmetic, or imported interval endpoints.

---

## 2. Summary of Certified Quantitative Results by Group

### Group 1 — `BRANCH_GAP` (24 / 24 checks passed)
- **Exact $\mathbb{Q}(\sqrt{5})$ identities:** $c_0 = \cos(\pi/5) = (1+\sqrt{5})/4$, $s_0 = \sin(\pi/5) = \sqrt{(5-\sqrt{5})/8}$, $\cos(2\pi/5) = (\sqrt{5}-1)/4$, $k_0 = -\arccos((9-5\sqrt{5})/16)$ solving $\varepsilon(k_0) = g = 2\pi/5$, and $64\cos^2 k_0 - 72\cos k_0 - 11 = 0$.
- **Infinite-operator Woodbury & Hermitian positivity at $P = 0$:** On $\mathcal{H}_\perp = \ell^2(\mathbb{Z}_r)\otimes\operatorname{span}(S_{\mathrm{coin}}, T_{\mathrm{coin}}, B)$, $\delta_f = (4c_0 - 2s_0)/\sqrt{5} > 68/75 > 9/10$ ($\|R_0\| < 10/9$), $R_0^* = zI - z^2 R_0$, $K^* = zK$ ($z = e^{-ig}$), and $\widetilde{K} = e^{-ig/2}K$ satisfies $\widetilde{K}_{BB} > 2/3 > 1/2$, $(\widetilde{K}_{ST})_{11} > 24/25 > 1/2$, $\det(\widetilde{K}_{ST}) > 4/5$, $\operatorname{tr}(\widetilde{K}_{ST}) < 829/415 < 2$, and $\det(\widetilde{K}_{ST} - I_2/2) > 17/332 > 0$, yielding $\|K^{-1}\| < 2$ and $\operatorname{dist}(z, \operatorname{spec}(W(0))\setminus\{z\}) > \delta_0 = 27/110$.
- **Uniform branch gap & Riesz projector derivative bound on $|P| \le 1/12$:** On the circle $|w - z| = 1/8$, the distance is $53/440$ ($M_0 = 440/53$) and the Neumann product on $|P| \le 1/12$ is $110/159 < 1$, certifying the rank-one bound branch $\Pi_b(P)$ with:
  $$\operatorname{dist}\bigl(\lambda(P),\, \operatorname{spec}(W(P)) \setminus \{\lambda(P)\}\bigr) \ge \frac{13}{165}, \qquad \|\Pi_b'(P)\|_{\mathrm{op}} \le L := \frac{165}{13}, \qquad |\langle b_0, \chi_b(P)\rangle|^2 \ge \frac{8424}{11449} > \frac{1}{2}.$$

### Group 2 — `PACKET_CERTIFICATE` (44 / 44 checks passed)
- **Incoming Schur density and contact-selected packet normalization:** On $I_P \times I_\omega = [-1/1000, 1/1000] \times [4\pi/5 - 1/1000, 4\pi/5 + 1/1000]$, $D(P,\omega) = \cos\omega - \cos P < 0$, $x(P,\omega) \in (-1,1)$, $\partial_\omega x < 0$, $\rho_{B,W}(P,\omega) > 77/1000$, and under the Fourier measure $\frac{dP}{2\pi}$, $\rho_{1,\mathrm{in}}(E) = \int_{-p_{\mathrm{in}}}^{p_{\mathrm{in}}}\rho_{B,W}(P,E-\beta)\frac{dP}{2\pi} \ge a > 24/10^6$. The packet $\psi_{\mathrm{in}} = \mathbf{1}_{I_E}(H_1)[\ell_E\rho_{1,\mathrm{in}}(H_1)]^{-1/2}P_{\mathrm{in}}a_0$ ($a_0 = \delta_{u=0,r=0}iB$, $P_{\mathrm{in}}$ on $\mathscr{H}_{\mathrm{ac}}(W(P))$) and localized preparation $\Psi_{\mathrm{loc}}$ have exact unit norm and zero free incoming bound weight $(\Pi_b\otimes I_{\mathrm{tok}})\Psi_{\mathrm{loc}} = 0$.
- **Homogeneous output coarea density:** On $I_K \times I_E$ with $P \in [-p_b, p_b] = [-1/100, 1/100]$, $f_{K,E}(P) = \Omega(P) + \beta + \varepsilon(K-P) - E$ has strict monotonicity margin $v_{\min} - 2Lp_b > 0$ and endpoint straddling margin $v_{\min}(p_b - \delta_K) - Lp_b^2 - h > 0$, certifying a unique root $P_*(K,E) \in (-p_b, p_b)$ and outgoing bound-branch density $\rho_{2,b,+}(K,E) \ge b_{\mathrm{hom}} > 1/100$.
- **Full-function Hardy-Carathéodory bound & probability certificate (`SCALE = 10**36`):** Applying Cauchy-Schwarz and Markov's inequality at $\alpha = 9/10$ to the complete Carathéodory functions $F_1(E), F_2(K,E)$ on the analytically derived transition kernel $\mathcal{P}(K,E) = 64\pi^2\rho_{1,\mathrm{in}}(E)\rho_{2,b,+}(K,E)/|4+F_1(E)F_2(K,E)|^2$ certifies:
  $$B_{\mathrm{hom}} = 64\pi^2\,a\,b_{\mathrm{hom}}\,\frac{9/49}{(4 + M)^2} \ge 903{,}570{,}708 \times 10^{-33} > 8 \times 10^{-25},$$
  $$p(Q_{\mathrm{full}}) \ge p(Q_{\mathrm{win}}) \ge \frac{\delta_K}{\pi}\,B_{\mathrm{hom}} \ge 287{,}615{,}489 \times 10^{-36} > 2 \times 10^{-28}.$$

### Group 3 — `NATIVE_COMPLETION` (27 / 27 checks passed)
- **26-label native code in $\mathbb{Z}^{38}$:** All $26$ token codes ($q=4$), $2\times 26$ pulse codes ($q=4$), and $26$ memory codes ($q=2$) with active charge $H_N = 4 + 4 + 2 = 10$, disjoint sectors, token invariance under on-site pulse coin $Q$ and vacuum edge $E$, and $C^T C = I_4$ verified across all $2{,}704$ contact states and $1{,}352$ receiver-edge states.
- **Receiver calibration $\mathcal{T} = \mathcal{T}_1 \oplus \mathcal{T}_2$ and coherent old-memory transfer:** $[\mathcal{T}, C \otimes I_{\mathrm{rec}}] = 0$ at all contact sites $s \in \mathbb{Z}$, $D_{\mathrm{rec}}^\dagger D_{\mathrm{rec}} = D_{\mathrm{rec}} D_{\mathrm{rec}}^\dagger = 5I$, and $\mathcal{T}_+$ maps outgoing right-moving ($\varepsilon'(k)>0$) pulse states according to $|p_1\rangle\sum_{j=0}^{25}|d_j\rangle|\phi_j\rangle \mapsto \sum_{j=0}^{25}|p_j\rangle|d_1\rangle|\phi_j\rangle$.

### Group 4 — `CURRENT_INTERFACE` (12 / 12 checks passed)
- **Native intertwiner and right-half charge pullback:** $\mathcal{I}_0 = \mathsf{Emb}\,\Gamma^{-1}D_2^*$ ($D_2^* M_{\mathrm{nat}} D_2 = M_2$) and $\mathcal{I}_{\eta,\xi}$ satisfy $U_{\mathrm{nat}}\mathcal{I}_{\eta,\xi} = \mathcal{I}_{\eta,\xi}U_{\mathrm{rec}}$ and pull back the right-half native charge to $N_{R,\ell} = 2\Theta_\ell(x_A) + 2\Theta_\ell(x_B) + 4\Theta_\ell(\text{carrier}) + 2\Theta_\ell(z)$ plus conserved static helper charge.
- **Full one-step physical current at cut $\ell = 99$ ($z = 100$):** Verified across all $9\times 9 = 81$ local stencil pairs that $J_{99} = U_{\mathrm{rec}}^* N_{R,99} U_{\mathrm{rec}} - N_{R,99} = N_{L,99} - U_{\mathrm{rec}}^* N_{L,99} U_{\mathrm{rec}} = C^* D_c^*(j_{S,99} + j_{E,99}) D_c C$ with $j_{E,99}^2 = \frac{64}{5}I$, and certified the coherent history interference witness $\mathfrak{j}_{99}^{(0)} = 1642/625$ vs. incoherent $58/25$.

### Group 5 — `OPEN_CHANNEL_AND_CARRIER` (16 / 16 checks passed)
- **Open-channel transfer, causal reconstruction $L_m$, and dark-state current obstruction:** Certified $s(z) = (4-F)/(4+F)$, return amplitudes $\nu_0 = \nu_2 = 0, \nu_1 = 4/5, \nu_3 = (48-28e^{ig})/125$, exact causal reconstruction $L_m H_m = (\rho_m, p_m)$ for $m = 1..4$, and the dark-state pair $\psi_\pm = ((\chi_0 \pm d_0)/\sqrt{2}, 0)$ having zero initial contact projection ($m=0$), **identical (nonzero) pulse output histories $\{p_m\}_{m\ge 0}$ at all times $m \ge 0$**, and distinct initial physical currents $\langle\psi_\pm, J_n\psi_\pm\rangle = -13/10 \pm 2\sqrt{2}/5$ (difference $4\sqrt{2}/5$).
- **Three infinite-carrier no-go theorems (without P24):** Certified extreme-coordinate linear independence $\langle 0,m,3|T^m\alpha'\rangle = -ie^{-im\beta}5^{1-m}$ ($m=1..6$), Canon's open spectral gap width $\arccos(7/25) - 2\pi/5 > 3/100 > 0$ (which together with extreme-coordinate independence proves nonrationality of $F(z)$ and $s(z)$ without P24), and the infinite orthonormal $\pm 2$ current eigenspace families $e_j^\pm$ ($j=1..8$).

### Group 6 — `FINITE_STRIP` (18 / 18 checks passed)
- **Stationary-channel elimination and compact eigenvector classification:** Certified all $16$ Laurent polynomial identity groups over $\mathbb{Z}[i]$ proving that for $P \notin \mathcal{E}_{\mu,z}$ ($|\mathcal{E}_{\mu,z}| \le 10$, measure zero), $W(P)$ has no nonzero compactly supported eigenvector and hence $\bigcap_{n\in\mathbb{Z}} W^{-n}\operatorname{Ran} P_B = \{0\}$, together with $2$ negative controls.

---

## 3. Scope Fences and Non-Canonical Status

This result package is explicitly **`NON-CANONICAL`**:
1. It does not promote any claim to `DERIVED` in `canon/` or modify `STATUS.md`.
2. It establishes the connected **asymptotic** wave-operator capture, complete full-step physical cut current interface, and coherent record transfer lower bound $p(Q_{\mathrm{full}}) \ge p(Q_{\mathrm{win}}) > 2/10^{28}$ from the prepared incoming state $\Psi_{\mathrm{prep}} = \Omega_{\mathrm{rec},-}(\Psi_{\mathrm{loc}}\otimes\Phi_{\mathrm{mem},\mathrm{ref}})$, while leaving **finite-resource incoming state preparation**, **local finite-time joint detector effects and false-positive bounds**, and **quantitative finite-horizon record retention** explicitly outside its claimed scope (`NOT DERIVED`).
