# Result Summary: `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N`

**Status:** `NON-CANONICAL` (Research-Note & First-Principles Reproduction Result Summary)  
**Claim ID:** `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N`  
**Base Commit (`main`):** `e6240e2689bb22aab5f02bad90b75d3692bb96d9`  
**Prospective Source Pin Commit:** `fd710dbc6ca5023dba89c26de7421a6bbd9c01b5`  
**Execution Record:** `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/RUN.md`

---

## 1. Executive Outcome

The preregistered first-principles standard-library verification suite `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py` (pinned prospectively at commit `fd710dbc6ca5023dba89c26de7421a6bbd9c01b5` with SHA-256 `4a5bb106f680527a77093c5596463e18a1becf6ff7cf8e58364c86e96141370c`) executed with **exit code `0`**, **`0` bytes on `stderr`**, and **141 passed checks across all 6 frozen check groups**, producing `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/EXPECTED.txt` (`708` bytes, SHA-256 `1c0d4c4459a4ae52a74adf6d1206ff4eb91a9042f200708c5a8d06aeb831a43b`).

Every mathematical premise required for the connected asymptotic capture-current-record theorem on the one-pair, one token OR pulse, coded receiver sector is proved in `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_*.md` and certified from first principles in standard-library Python without external libraries, floating-point arithmetic, or imported interval endpoints.

---

## 2. Summary of Certified Quantitative Results by Group

### Group 1 — `BRANCH_GAP` (24 / 24 checks passed)
- **Secular determinant & rank-one bound branch $\Pi_b(P)$:** Certified on the frozen strip $I_P = [-1/12, 1/12]$ via the exact degree-$2$ polynomial $D(z,P) = z^2 \det(I - K(z,P)) = a_0(P) + a_1(P)z + a_2(P)z^2$.
- **Exact $P=0$ endpoints:** $\theta_b(0) = \arccos(-11/16)$, $\cos\theta_b(0) = -11/16$, $\sin\theta_b(0) = 3\sqrt{15}/16$, $z_0 = (-11 + 3i\sqrt{15})/16$ with $|z_0|^2 = 1$, and $\|u_b(0)\|_{\ell^2}^2 = 30/11$.
- **Uniform branch gap & Riesz projector derivative bound:** On $|P| \le 1/12$, the finite-matrix perturbation bound on $G(e^{i\theta},P)^{-1}$ and Riesz contour estimate on $|z - z_b(P)| = 13/330$ certify:
  $$\operatorname{dist}\bigl(z_b(P),\, \sigma(U_{\mathrm{fib}}(P)) \setminus \{z_b(P)\}\bigr) \ge \frac{13}{165}, \qquad \|\Pi_b'(P)\|_{\mathrm{op}} \le \frac{165}{13}.$$

### Group 2 — `PACKET_CERTIFICATE` (44 / 44 checks passed)
- **Scattering normalization:** Relative trace-class perturbation rank $\le 8$ per $(P,K)$ fiber; Birman–Krein determinant invariance; center+relative to physical $(x_A, x_B) = (R+r, R-r)$ Jacobian $= 2$ compensated by half-density $dP\,dk/(2\pi)^2 = d(2P)\,dk/(8\pi^2)$ to yield the exact $(8\pi^2)^{-2} = (64\pi^2)^{-1}$ cross-term denominator.
- **Incoming packet normalization & zero bound overlap:** Exact Fourier normalization $\|\psi_{\mathrm{in}}\|^2 = 1$, strictly disjoint support from the incoming bound branch ($\Pi_{\mathrm{bound}}(U)\psi_{\mathrm{in}} = 0$), and full-function Hardy–Carathéodory denominator bound $M$ on $|z| < e^{1/10}$ replacing the retracted polynomial-part shortcut.
- **First-principles outward-rounded rational interval certificate (`SCALE = 10**36`):**
  $$\mathcal{B}_{\mathrm{hom}} = \frac{|c_{\mathrm{win}}|^2}{64\pi^2 N_{\mathrm{in}}} \ge 903{,}570{,}708 \times 10^{-33} > 8 \times 10^{-25},$$
  $$p(Q_{\mathrm{full}}) \ge p(Q_{\mathrm{win}}) \ge \mathcal{B}_{\mathrm{hom}}\bigl(\Delta E_{\mathrm{safe}} - 2\varepsilon_{\mathrm{tail}}(z_0)\bigr) \ge 287{,}615{,}489 \times 10^{-36} > 2 \times 10^{-28}.$$

### Group 3 — `NATIVE_COMPLETION` (27 / 27 checks passed)
- **Typed native embedding:** All $26$ alphabet labels (`16` interior + `6` boundary + `4` receiver-edge), $2{,}704$ contact configurations, and $1{,}352$ receiver-edge configurations verified.
- **Exact conjugacy & commutation:** $\mathcal{I} = \mathsf{Emb}\,\Gamma^{-1} D_2^*$ is a partial isometry satisfying $\mathcal{I}^*\mathcal{I} = I_{\mathcal{H}_{\mathrm{rec}}}$, $U_{\mathrm{nat}}\mathcal{I} = \mathcal{I} U_{\mathrm{rec}}$, and $[\mathcal{T}, C \otimes I_{\mathrm{rec}}] = 0$.
- **Coherent old-memory transfer:** On every pulse-present contact input $(s_1, m) \in \{t_1, t_2\} \times \{0, u, d\}$, $\mathcal{T}$ writes $m_{\mathrm{rec}}' = d$ when $s_1 = t_1$ and $m_{\mathrm{rec}}' = u$ when $s_1 = t_2$, while transferring the incoming receiver memory $m$ coherently into the outgoing carrier label $b_m \in \{b_0, b_u, b_d\}$ so that $\operatorname{Tr}_{\mathrm{env}}(\mathcal{T}(|\psi\rangle\langle\psi| \otimes \rho_{\mathrm{old}})\mathcal{T}^*) = |\psi_{\mathrm{code}}\rangle\langle\psi_{\mathrm{code}}|$.
- **Two-pulse alias obstruction:** Repeated arrivals $(t_2 \text{ after } t_1)$ collide in outgoing state with $(t_1 \text{ after } t_2)$ on the $3$-state memory register, confirming the one-pulse sector domain boundary.

### Group 4 — `CURRENT_INTERFACE` (12 / 12 checks passed)
- **Exact conserved native charge and cut current:** On the native space, $U_{\{ \mathrm{nat} \}}^* Q_{\mathrm{nat}} U_{\mathrm{nat}} = Q_{\mathrm{nat}}$ and $\mathcal{I}^* Q_{\mathrm{nat},R}(\ell)\mathcal{I} = Q_R(\ell) \otimes I_{\mathrm{rec}}$.
- **Full-step decomposition at $\ell = 99$:** $J_\ell = U^* Q_R(\ell) U - Q_R(\ell) = Q_L(\ell) - U^* Q_L(\ell) U = C^* D_c^*(j_{S,\ell} + j_{E,\ell}) D_c C$, with $j_{E,99}$ equal to the exact rank-$2$ swap skew-hermitian form across bond $(99,100)$ and coherent contact-plus-bridge expectation $j_{\mathrm{coh}} = 1642/625$.

### Group 5 — `OPEN_CHANNEL_AND_CARRIER` (16 / 16 checks passed)
- **Open-channel $L_m$ reconstruction:** At $C = (3/5, 4/5)$, $\sum_{m=0}^2 L_m^* L_m = I_4$, $L_1^* L_1 = (16/25)|e_0\rangle\langle e_0|$ ($\nu_1 = 4/5 > 0$), and $4\times 4$ Choi rank $= 3$.
- **Dark-state current counterexample & infinite-carrier no-go without P24:** Certified $\langle \psi_+ | J_{\mathrm{op}} | \psi_+ \rangle - \langle \psi_- | J_{\mathrm{op}} | \psi_- \rangle = 4\sqrt{2}/5 \ne 0$ despite identical channel populations, and verified the exact finite-candidate exclusion table without P24.

### Group 6 — `FINITE_STRIP` (18 / 18 checks passed)
- **Algebraic elimination & no-uniform-shutoff:** All $16$ exact Laurent polynomial identity groups $R_k A_k + S_k B_k = \Delta_{\mathrm{strip}}$ over $\mathbb{Q}[u, u^{-1}, w, w^{-1}]$ (with $\Delta_{\mathrm{strip}}(1,1) = -8192 \ne 0$), plus the $2$ negative controls (`NEG_CTRL_1_WRONG_SIGN_R1` and `NEG_CTRL_2_PERTURBED_M12`), and the exact identity $p_{\mathrm{act}}(0) + p_{\mathrm{act}}(\pi) = 2\sin^2\theta \cdot \tau^2 = 32/25 > 0$.

---

## 3. Scope Fences and Non-Canonical Status

This result package is explicitly **`NON-CANONICAL`**:
1. It does not promote any claim to `DERIVED` in `canon/` or modify `STATUS.md`.
2. It establishes the connected **asymptotic** wave-operator capture, complete full-step current interface, and coherent record transfer lower bound $p(Q_{\mathrm{full}}) \ge p(Q_{\mathrm{win}}) > 2/10^{28}$ from the prepared incoming packet $\Psi_{\mathrm{in}}$, while leaving **finite-time preparation** (`T-20261023-v105-finite-preparation-52cb1a`), **joint detector / false-positive bounds** (`T-20261023-v105-joint-detector-332ed7`), and **finite-horizon record retention** (`T-20261023-v105-record-retention-55d493`) explicitly outside its claimed scope (`NOT DERIVED`).
