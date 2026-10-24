# Connected Asymptotic Capture, Current, and Record: Standard-Library Verification

**PUBLIC, NON-CANONICAL. Conditional L1 candidate reproduction.**

Owner: A. M. Thorn. License: Apache-2.0.
Authority basis: `mathorn1973/twist-j` main `e6240e2689bb22aab5f02bad90b75d3692bb96d9` (Public Canon v104, content commit `4a50e527d20018839f006ed312454b710e6486b4`).

This directory provides the self-contained, dependency-free Python 3 standard-library reproduction accompanying `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/`:
- Prospective specification: `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PREREG.md`
- Analytical proofs and soundness theorem:
  - `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_CAPTURE_SCATTERING.md`
  - `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_PACKET_CERTIFICATE.md` (§5 proves soundness of the rational interval arithmetic in `verify.py`)
  - `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_CURRENT_RECORD_INTERFACE.md`

---

## 1. Execution and Custody

From the repository root on any system with Python 3.10 or later:

```text
python3 reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py
```

The verifier uses **only** the Python standard library (`fractions.Fraction`, `int`, `math.isqrt`, `itertools`). It performs **zero floating-point operations**, imports no third-party or predecessor scripts, reads no files, makes no network calls, uses no randomness, and writes deterministic ASCII summaries to stdout.

The registered execution contract (`tools/check_reproduce.py`) enforces:
- Environment: `LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`
- Timeout: 120 seconds (actual runtime $< 2$ seconds)
- Exit code: `0`
- Standard error: `0` bytes
- Standard output: byte-for-byte identical to `EXPECTED.txt` on both `x86_64` (`ubuntu-latest`) and `aarch64` (`ubuntu-24.04-arm`).

---

## 2. Six Frozen Audit Groups

| Group | Domain and Principal Verified Claims | Checks |
|---|---|---:|
| `GROUP 1: BRANCH_GAP` | Exact $\mathbb{Q}(\sqrt{5})$ identities for $c_0, s_0, \cos(2\pi/5), \cos k_0 = (9-5\sqrt{5})/16$; rational radical brackets and interval enclosures for $\delta_f > 68/75 > 9/10$, Hermitian block $\widetilde{K} > I_3/2$, $\delta_0 = 27/110$, Riesz circle distance $53/440$, Neumann bound $110/159 < 1$ on $|P|\le 1/12$, uniform branch gap $\ge 13/165$, $\|\Pi_b'(P)\| \le L = 165/13$, anchor overlap $\ge 8424/11449 > 1/2$, and negative control. | 24 |
| `GROUP 2: PACKET_CERTIFICATE` | First-principles outward-rounded rational interval arithmetic (`RI`, `CRI` with `SCALE = 10^36`) enclosing $\pi$ (Machin/Leibniz), $\cos,\sin$ (Lagrange/Leibniz), $\arccos$ (certified via $\cos$), and $(\cdot)^{20/9}$ (certified via integer 9th/20th power inequalities) applied to the analytically derived transition kernel $\mathcal{P}(K,E) = 64\pi^2\rho_{1,\mathrm{in}}(E)\rho_{2,b,+}(K,E)/|4+F_1(E)F_2(K,E)|^2$: incoming rectangle $I_P \times I_\omega$ ($\rho_{B,W} > 77/1000$, $a > 24/10^6$), central $P=0$ PR29 radical formula cross-check and wrong-root negative control, homogeneous output coarea rectangle $k \in [k_0-11/1000, k_0+11/1000]$ (strict monotonicity, endpoint straddling, $b_{\mathrm{hom}} > 1/100$), fixed-source comparison $b_{\mathrm{fixed}} > 49/10^7$, full-function Hardy-Carathéodory threshold $M$, and probability bounds $B_{\mathrm{hom}} > 8/10^{25}$, $P_{\mathrm{fixed}} > 4/10^{28}$, $p(Q_{\mathrm{full}}) \ge p(Q_{\mathrm{win}}) > 2/10^{28}$, plus safe-window $(5\pi/4, 7\pi/4)$ inclusion. | 44 |
| `GROUP 3: NATIVE_COMPLETION` | Enumeration of all 26 pulse ($q=4$, $p_1=(1,1,0,0,0)$), 26 token ($q=4$, $t_1=(1,1,0,\dots,0)$), and 26 memory ($q=2$, $d_1=(-1,0,\dots,0)$) codes in $\mathbb{Z}^{38}$, $H_N = 10$ across all 2,704 coded states, disjointness, token invariance under on-site pulse coin and vacuum edge, rational contact orthogonality $C^T C = I_4$, commutation $[\mathcal{T}, C\otimes I_{\mathrm{rec}}] = 0$ on all 2,704 states, receiver bond unitarity $D_{\mathrm{rec}}^\dagger D_{\mathrm{rec}} = I$ (integer numerator $(\sqrt{5}D_{\mathrm{rec}})^\dagger(\sqrt{5}D_{\mathrm{rec}}) = 5I$) on all 1,352 states, coherent transfer $|p_1\rangle|d_j\rangle \mapsto |p_j\rangle|d_1\rangle$, and 3 negative controls. | 28 |
| `GROUP 4: CURRENT_INTERFACE` | Native-to-source coin and step intertwiner $M_{\mathrm{nat}} = D_2^* M_{\mathrm{src}} D_2 = Q \otimes Q$, $M_{\mathrm{nat}} D_2^* = D_2^* M_{\mathrm{src}}$, $(S M_{\mathrm{nat}} \Gamma)(\Gamma^{-1} D_2^*) = (\Gamma^{-1} D_2^*)(\Gamma S M_{\mathrm{src}})$, contact-port gauge images $D_2^*(iB) = (e_2-e_3)/\sqrt{2}$, $D_2^* A = (e_1+e_4)/\sqrt{2}$, and reversed-coin negative control, native object embedding $\mathsf{Emb}$, receiver-bond current $D_{\mathrm{rec}}^* Q_{\mathrm{bond}} D_{\mathrm{rec}} - Q_{\mathrm{bond}} = j_{E,99}$ and $j_{E,99}^2 = \frac{64}{5}I$, complete one-step bilinear current identity $U_{\mathrm{rec}}^* N_{R,99} U_{\mathrm{rec}} - N_{R,99} = N_{L,99} - U_{\mathrm{rec}}^* N_{L,99} U_{\mathrm{rec}} = C^* D_c^*(j_{S,99}+j_{E,99})D_c C$ across all 81 stencil pairs at cut $\ell=99, z=100$, coherent history interference witnesses $\langle v_0, v_2\rangle = 12/25$, $\langle v_0, N_{99}^T v_2\rangle = 48/25$, $\mathfrak{j}_{99}^{(0)} = 1642/625$ vs. incoherent $58/25$, and negative control. | 14 |
| `GROUP 5: OPEN_CHANNEL_AND_CARRIER` | Open-channel transfer $s(z)=(4-F)/(4+F)$, return amplitudes $\nu_0=\nu_2=0, \nu_1=4/5, \nu_3=(48-28e^{ig})/125$, causal history reconstruction $L_m H_m = (\rho_m, p_m)$ for $m=1..4$, dark-state current counterexample $\langle\psi_\pm, \mathcal{J}_n\psi_\pm\rangle = -13/10 \pm 2\sqrt{2}/5$ with identical (nonzero) pulse output histories at all times $m\ge 0$ (and zero initial contact projection at $m=0$), extreme-coordinate linear independence $\langle 0,m,3|T^m\alpha'\rangle = -ie^{-im\beta}5^{1-m}$ ($m=1..6$), canonical open gap $\arccos(7/25)-2\pi/5 > 3/100 > 0$, and infinite $\pm 2$ current eigenspaces ($j=1..8$). | 16 |
| `GROUP 6: FINITE_STRIP` | All 16 Laurent polynomial identity groups over $\mathbb{Z}[i]$ for the finite-strip stationary-channel elimination and compact eigenvector classification of $W(P)$ plus 2 negative controls. | 18 |

---

## 3. Scope Boundaries

This verifier certifies the exact algebraic identities and rational interval inequalities of the asymptotic capture, current, and coherent-record theorem on the infinite lattice. It does not derive finite-time state preparation from vacuum, a finite-time joint detector effect $F_T$, quantitative finite-window record retention on $[T, T+L]$, a local spectral-energy current, or a physical Born-rule occurrence postulate.
