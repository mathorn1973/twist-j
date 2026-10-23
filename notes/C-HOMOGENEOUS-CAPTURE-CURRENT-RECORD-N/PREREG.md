# Prospective Specification: Connected Asymptotic Capture, Current, and Record Audit

**PUBLIC, NON-CANONICAL. Prospective specification (`PREREG.md`) for `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N`.**

Owner: A. M. Thorn. License: Apache-2.0.
Authority basis: `mathorn1973/twist-j` main `e6240e2689bb22aab5f02bad90b75d3692bb96d9` (Public Canon v104, content commit `4a50e527d20018839f006ed312454b710e6486b4`).

This document freezes the scientific scope, carrier, native code allocation, mathematical constants, certificate inequalities, verifier soundness contract, failure thresholds, and execution limits before the formal pinned run of `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py`.

---

## 1. Frozen Carrier, Coordinates, and Dynamical Law

1. **Physical lattice and sector:**
   - Two object constituents at $x_A = R + r \in \mathbb{Z}$, $x_B = R - r \in \mathbb{Z}$ ($x_A \equiv x_B \pmod 2$), with four coin states $d \in \{1,2,3,4\} \equiv \{++, +-, -+, --\}$ and streaming shifts $(\delta R_d, \delta r_d) \in \{(-1,0), (0,-1), (0,+1), (+1,0)\}$.
   - Single carrier at $y \in \mathbb{Z}$, either a standing token $|\mathrm{tok}_j(y)\rangle$ or a two-bank moving pulse $|p_{j,b}(y)\rangle$ ($b \in \{1,2\}$), with label $j \in \{0,\dots,25\}$.
   - Single encoded receiver memory at fixed site $z = 100 \in \mathbb{Z}$ with memory state $|d_k\rangle$, $k \in \{0,\dots,25\}$, plus arbitrary untouched spectator/helper occupancy $\eta$ and external reference state $|\phi_k\rangle$.
2. **Native 38-coordinate site code:**
   - Coordinates $0..3$ ($h_1..h_4$): object configurations `object_codes = [(-1,0,0,-1), (0,-1,-1,0), (1,0,1,0), (0,1,0,1)]`, each of native charge $2\sum_{\alpha=1}^4 h_\alpha^2 = 4$.
   - Coordinates $4..15$ ($h_5..h_{16}$): 26 token codes ($h_5 = \pm 1$ and one $\pm 1$ in $h_6..h_{16}$, charge $4$, $\mathrm{tok}_1 = (1,1,0,\dots,0)$) and $2\times 26$ embedded pulse codes ($h_5 = h_6 = 0$, two $\pm 1$ entries in bank 1 $h_7..h_{11}$ or bank 2 $h_{12}..h_{16}$, charge $4$, $p_1 = (-1,-1,0,0,0)$).
   - Coordinates $24..36$ ($h_{25}..h_{37}$): 26 memory codes (one $(-1)^k$ at index $\lfloor k/2 \rfloor$, charge $2$, $d_1 = (-1,0,\dots,0)$).
   - Coordinates $16..23$ and $37$: nine untouched auxiliary/helper coordinates. Active encoded charge without helpers is $H_N = 4 + 4 + 2 = 10$.
3. **Synchronized phase-zero macrostep:**
   - Two microticks per macrostep; $U = U_0 C$ and $U_{\mathrm{rec}} = \mathcal{T}(U \otimes I_{\mathrm{rec}})\mathcal{T}^*$, where $\mathcal{T} = \mathcal{T}_1 \oplus \mathcal{T}_2$ swaps the token/pulse label on $\{y \ge z\}$ / $\{x \ge z\}$ with the receiver memory label at $z = 100$.
   - Contact $C$: rotation $\begin{pmatrix} 3/5 & -4/5 \\ 4/5 & 3/5 \end{pmatrix}$ on $\operatorname{span}\{|a_0\rangle|\mathrm{tok}_j(y)\rangle, |b_0\rangle|p_{j,1}(y)\rangle\}$ at $R = y, r = 0$ for every $j \in \{0,\dots,25\}$, where $|a_0\rangle = \delta_{r=0}\frac{i(|+-\rangle - |-+\rangle)}{\sqrt{2}}$ and $|b_0\rangle = \delta_{r=0}\frac{|++\rangle - |--\rangle}{\sqrt{2}}$.
   - Free step $U_0 = e^{-i\beta}(W \otimes V_{\mathrm{car}})$ with $\beta = 4\pi/5$, $g = 2\pi/5$, $W = \Gamma S M_2$, $\Gamma = I + (e^{-ig}-1)\delta_{r=0}$, on-site pulse coin $Q = \frac{1}{\sqrt{5}}\begin{pmatrix} 1 & -2 \\ 2 & 1 \end{pmatrix}$, and bond hop $D_{\mathrm{edge}}$ replaced at bond $(z-1,z) = (99,100)$ under $\mathcal{T}$-conjugation by $D_{\mathrm{rec}} = \frac{1}{\sqrt{5}}\begin{pmatrix} I & -2\,\mathrm{SWAP} \\ 2\,\mathrm{SWAP} & I \end{pmatrix}$.

---

## 2. Frozen Constants and Parameters

All parameters are fixed prospectively without free tuning:

| Symbol | Exact Value | Role |
|---|---|---|
| $\mu, g, \beta$ | $2, \frac{2\pi}{5}, \frac{4\pi}{5}$ | Object coin parameter, contact phase, free phase |
| $E_*, h, \ell$ | $\frac{8\pi}{5}, \frac{1}{1000}, \frac{1}{500}$ | Total energy center, half-width, and interval length $|I_E| = 2h$ |
| $p_{\mathrm{in}}, p_b, \delta_K$ | $\frac{1}{1000}, \frac{1}{100}, \frac{1}{1000}$ | Incoming $P$ half-width, outgoing $P$ half-width, auxiliary $K$ half-width |
| $p_*, \delta_0, \text{gap}, L$ | $\frac{1}{12}, \frac{27}{110}, \frac{13}{165}, \frac{165}{13}$ | Branch radius, $P=0$ gap, uniform branch gap on $|P|\le 1/12$, projector derivative bound |
| $k_0$ | $-\arccos\bigl(\frac{9-5\sqrt{5}}{16}\bigr)$ | Right-moving pulse momentum solving $\varepsilon(k_0) = g = 2\pi/5$ |
| $\alpha, f_{\mathrm{bad}}, f_{\mathrm{good}}$ | $\frac{9}{10}, \frac{40}{49}, \frac{9}{49}$ | Hardy-Carathéodory exponent, Chebyshev bad-measure and good-measure fractions |
| $y_0, j_0, z, \ell_{\mathrm{cut}}$ | $0, 1, 100, 99$ | Initial token site, initial token label, receiver site, physical half-space cut |

---

## 3. First-Principles Standard-Library Soundness Contract

To avoid any dependence on external C libraries (`python-flint`/`Arb`) or imported floating-point/dyadic endpoints, `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py` is restricted to the Python 3 standard library (`fractions.Fraction`, `int`, `math.isqrt`, `itertools`) with **zero floating-point operations** and implements self-certifying rational interval arithmetic (`RI(lo, hi)` with `lo, hi` in `fractions.Fraction`):

1. **Outward rational rounding (`trim`):** Given `SCALE = 10**36`, any interval `[lo, hi]` is rounded outward to `lo' = floor(lo * SCALE) / SCALE` and `hi' = ceil(hi * SCALE) / SCALE`, followed by the explicit assertion `lo' <= lo and hi <= hi'`.
2. **Algebraic square root (`sqrt`):** For `[lo, hi]` with `lo >= 0`, integer square roots `isqrt` on `SCALE^2`-scaled numerators produce candidate bounds `lo_f, hi_f >= 0`, which are certified from first principles by asserting `lo_f * lo_f <= lo` and `hi <= hi_f * hi_f` (sound by strict monotonicity of $t \mapsto t^2$ on $[0, \infty)$).
3. **Constant $\pi$ (`atan_unit_fraction`, `PI`):** For integer $q \ge 2$, the alternating Taylor series $\arctan(1/q) = \sum_{m=0}^\infty (-1)^m \frac{q^{-(2m+1)}}{2m+1}$ has strictly decreasing positive terms. Summing $2N$ terms ends on a subtracted term, so by Leibniz's alternating series theorem the partial sum $S_{2N}$ is a strict lower bound and $S_{2N} + \frac{q^{-(4N+1)}}{4N+1}$ is a strict upper bound. $\pi$ is enclosed via Machin's identity $\pi = 16\arctan(1/5) - 4\arctan(1/239)$.
4. **Trigonometric enclosures (`cos_sin_point`, `cos_sin`):**
   - At any exact rational midpoint $t_0 \in \mathbb{Q}$, $\cos(t_0)$ and $\sin(t_0)$ are enclosed by their Taylor polynomials of degree $2N-2$ and $2N-1$ at $0$ with Lagrange remainders bounded by $\frac{|t_0|^{2N}}{(2N)!}$ and $\frac{|t_0|^{2N+1}}{(2N+1)!}$ (since $|\cos^{(k)}(\xi)| \le 1$ and $|\sin^{(k)}(\xi)| \le 1$ for all $\xi \in \mathbb{R}$).
   - On an interval $[t_0 - r, t_0 + r]$, the verifier asserts $0 \le r \le 2$ and applies the exact addition identities $\cos(t_0+\delta) = \cos(t_0)\cos(\delta) - \sin(t_0)\sin(\delta)$ and $\sin(t_0+\delta) = \sin(t_0)\cos(\delta) + \cos(t_0)\sin(\delta)$ with the Leibniz enclosures $\cos(\delta) \in [1 - r^2/2, 1]$ and $\sin(\delta) \in [-r, r]$.
5. **Inverse cosine (`acos_iv`):** For `[lo, hi] subset (-1, 1)`, rational candidates $0 \le \theta_{\mathrm{lo}} \le \theta_{\mathrm{hi}} \le \pi_{\mathrm{lo}}$ are certified from first principles by asserting $\cos_{\mathrm{hi}}(\theta_{\mathrm{hi}}) \le \mathrm{lo}$ and $\mathrm{hi} \le \cos_{\mathrm{lo}}(\theta_{\mathrm{lo}})$ (sound by strict decrease of $\cos$ on $[0, \pi]$).
6. **Rational power $u^{20/9}$ (`power_20_9`):** For `[lo, hi]` with `lo > 0`, rational candidates $0 < m_{\mathrm{lo}} \le m_{\mathrm{hi}}$ are certified from first principles by the exact integer-power assertions $m_{\mathrm{lo}}^9 \le \mathrm{lo}^{20}$ and $\mathrm{hi}^{20} \le m_{\mathrm{hi}}^9$ (sound by strict increase of $t \mapsto t^9$ on $(0, \infty)$).
7. **Pulse bandwidth $2\arctan 2$:** Certified by asserting $\tan(\theta/2) = \sin(\theta/2)/\cos(\theta/2) \ni 2$ on $\theta/2 \in (0, \pi/2)$.

---

## 4. Six Frozen Audit Groups and Failure Thresholds

The verifier `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py` must execute all six audit groups below and halt immediately (`AssertionError` / nonzero exit) if any check or negative control fails:

1. **Group 1 (`BRANCH_GAP` — 24 checks):**
   - Exact $\mathbb{Q}(\sqrt{5})$ identities: $c_0^2 + s_0^2 = 1$, $\cos(2\pi/5) = (\sqrt{5}-1)/4$, $\cos k_0 = (9-5\sqrt{5})/16$, $64\cos^2 k_0 - 72\cos k_0 - 11 = 0$.
   - Rational brackets for $\sqrt{5}, c_0, s_0, s$, free resolvent distance $\delta_f > 68/75 > 9/10$, $1 < |z-1| < 6/5$, Hermitian block bounds $\widetilde{K}_{BB} > 2/3 > 1/2$, $(\widetilde{K}_{ST})_{11} > 24/25 > 1/2$, $\det(\widetilde{K}_{ST}) > 4/5$, $\operatorname{tr}(\widetilde{K}_{ST}) < 829/415 < 2$, $\det(\widetilde{K}_{ST} - I_2/2) > 17/332 > 0$, $\|K^{-1}\| < 2$, $\delta_0 = 27/110$, Riesz circle distance $53/440$, Neumann product $110/159 < 1$ on $|P|\le 1/12$, uniform gap $13/165$, $L = 165/13$, anchor overlap $|\langle\chi_0,\chi(P)\rangle|^2 \ge 8424/11449 > 1/2$, and negative control.
2. **Group 2 (`PACKET_CERTIFICATE` — 44 checks):**
   - Incoming rectangle $P \in [-1/1000, 1/1000]$, $\omega \in [4\pi/5 - 1/1000, 4\pi/5 + 1/1000]$: $D < 0$, $x \in (-1,1)$, $\mathrm{num} > 0$, $dx/d\omega < 0$, relative speed $> 0$, $|dx/dP|/\sqrt{1-x^2} < 1$, contact denominator $> 0$, $\rho_{B,W} > 77/1000$, $a > 24/10^6$.
   - Central $P=0$ cross-check with PR29 radical formula ($0 \in F_{\mathrm{center}} - F_{\mathrm{old}}$), golden-ratio shell $0 \in x_{\mathrm{center}} - (4 - 5(1+\sqrt{5})/4)$, PR29 decimal interval $(0.077904561913345292, 0.077904561913345293)$, and wrong-root negative control ($\operatorname{Re} F_{\mathrm{wrong}} < 0$).
   - Homogeneous output rectangle $k \in [k_0 - 11/1000, k_0 + 11/1000]$: $p_b < 1/12$, $k \in (-\pi,0)$, $\varepsilon \in (0, 2\arctan 2)$, $v \in (0,1)$, monotonicity margin $v_{\min} - 2Lp_b > 0$, root-straddling margin $v_{\min}(p_b-\delta_K) - Lp_b^2 - h > 0$, contact weight $1 - Lp_b > 0$, port-1 weight $(1-v_{\max})/2 > 0$, and $b_{\mathrm{hom}} > 1/100$.
   - Fixed-source comparison density $b_{\mathrm{fixed}} > 49/10^7$.
   - Full-function Hardy-Carathéodory bound $M > 0$ and probability bounds $B_{\mathrm{hom}} > 8/10^{25}$, $P_{\mathrm{fixed}} > 4/10^{28}$, $p(Q_{\mathrm{full}}) \ge p(Q_{\mathrm{win}}) \ge (\delta_K/\pi)B_{\mathrm{hom}} > 2/10^{28}$ evaluated on the analytically derived transition kernel $\mathcal{P}(K,E) = 64\pi^2\rho_{1,\mathrm{in}}(E)\rho_{2,b,+}(K,E)/|4+F_1(E)F_2(K,E)|^2$, plus safe-window and normalization checks.
3. **Group 3 (`NATIVE_COMPLETION` — 27 checks):**
   - Enumeration of all 26 pulse, 26 token, and 26 memory codes, charges $(4,4,2)$ and $H_N = 10$, sector disjointness, on-site pulse coin and vacuum edge fixing every token, $C^T C = I_4$, $[C\otimes I_{\mathrm{rec}}, \mathrm{swap}] = 0$ on all $2704$ states, receiver edge $D_{\mathrm{rec}}^\dagger D_{\mathrm{rec}} = D_{\mathrm{rec}} D_{\mathrm{rec}}^\dagger = 5I$ on all $1352$ states, coherent transfer $|p_1\rangle|d_j\rangle \mapsto |p_j\rangle|d_1\rangle$, and 3 negative controls.
4. **Group 4 (`CURRENT_INTERFACE` — 12 checks):**
   - Native-to-source coin intertwiner $D_2^* M_{\mathrm{nat}} D_2 = M_{\mathrm{src}}$, orthogonality/unitarity, 4 distinct native object kets of charge $4$, receiver-bond current $D_{\mathrm{rec}}^* Q_{\mathrm{bond}} D_{\mathrm{rec}} - Q_{\mathrm{bond}} = j_{E,99}$ and $j_{E,99}^2 = \frac{64}{5}I$ on all $1352$ states, exact bilinear current identity $U_{\mathrm{rec}}^* N_{R,99} U_{\mathrm{rec}} - N_{R,99} = N_{L,99} - U_{\mathrm{rec}}^* N_{L,99} U_{\mathrm{rec}} = C^* D^* (j_{S,99} + j_{E,99}) D C$ across all $9\times 9 = 81$ local stencil pairs around $\ell = 99, z = 100$, coherent history interference witnesses $\langle v_0, v_2\rangle = 12/25$, $\langle v_0, N_{99}^T v_2\rangle = 48/25$, $\mathfrak{j}_{99}^{(0)} = 1642/625$ vs. incoherent $58/25$, and negative control.
5. **Group 5 (`OPEN_CHANNEL_AND_CARRIER` — 16 checks):**
   - Open-channel transfer $s(z) = (4-F)/(4+F)$, return amplitudes $\nu_0 = \nu_2 = 0, \nu_1 = 4/5, \nu_3 = (48-28e^{ig})/125$, causal history reconstruction $L_m H_m = (\rho_m, p_m)$ for $m = 1..4$, dark-state current obstruction $\langle \psi_\pm, \mathcal{J}_n \psi_\pm\rangle = -13/10 \pm 2\sqrt{2}/5$ with identical (nonzero) pulse output histories at all times $m \ge 0$, extreme-coordinate linear independence $\langle 0,m,3|T^m\alpha'\rangle = -ie^{-im\beta}5^{1-m}$ ($m=1..6$), canonical whole-operator gap $\arccos(7/25) - 2\pi/5 > 3/100 > 0$, and infinite $\pm 2$ physical-current eigenspace families ($j=1..8$).
6. **Group 6 (`FINITE_STRIP` — 18 checks):**
   - All 16 Laurent polynomial identity groups over $\mathbb{Z}[i]$ for the finite-strip elimination and compact-support theorem plus 2 negative controls.

---

## 5. Resource Limits, Custody Protocol, and Prior-Outcome Disclosure

- **Execution environment:** Python $\ge 3.10$ (tested on Python 3.12 in CI), standard library only, `LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`, timeout 120 seconds, exit status 0, 0 bytes on stderr, deterministic ASCII stdout.
- **Two-architecture requirement:** Both `x86_64` (`ubuntu-latest`) and `aarch64` (`ubuntu-24.04-arm`) jobs in `.github/workflows/policy.yml` must execute `tools/check_reproduce.py` on the exact PR head and match `EXPECTED.txt` byte-for-byte, with the aggregate `check` job succeeding.
- **Custody protocol:** This `PREREG.md`, the companion proof files, and `verify.py` must be committed, pushed to the public branch, and read back by their immutable Git commit SHA before the formal execution that populates `EXPECTED.txt`, `RUN.md`, and `RESULT.md`.
- **Honest disclosure of prior source results:** The mathematical formulas and numerical thresholds audited here derive from the frozen homogeneous capture source (`0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8`, prospective source pin `df4d70c951c4d0829a22882e4382acdc5ea12d1d`) and frozen public notes `PR #1721` (`d221e10747e009cb1315295a258f1d48e8b75bce`), `PR #1723` (`b4696efa4fcb56cef8883fb593d2ab571bdcd047`), and `PR #1726` (`bebdd534cf1ec57596b83be7faf2b724f00b8f24`). Accordingly, the threshold values ($>8/10^{25}$, $>4/10^{28}$, $>2/10^{28}$) were known from the source analytical/Arb package prior to authoring this standard-library verifier; the purpose of `verify.py` is to provide a self-contained, dependency-free, two-architecture public certificate of those exact inequalities from first principles.
