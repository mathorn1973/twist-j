# Packet Normalization, Hardy-Carathéodory Bound, and Standard-Library Soundness Proof

**PUBLIC, NON-CANONICAL. Self-contained analytical proof (`PROOF_PACKET_CERTIFICATE.md`) for `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N`.**

Owner: A. M. Thorn. License: Apache-2.0.
Authority basis: `mathorn1973/twist-j` main `e6240e2689bb22aab5f02bad90b75d3692bb96d9` (Public Canon v104, content commit `4a50e527d20018839f006ed312454b710e6486b4`).

---

## 1. Incoming Scalar Schur Complement and Actual $W(P)$ Spectral Density

### 1.1 Closed-Form Boundary Formula for $F_{0,B}(P, \omega + i0)$

On the incoming token arrangement, the token stands at $y$ so the center momentum $P \in I_P = [-1/1000, 1/1000]$ is conserved. Total quasi-energy $E \in I_E = [8\pi/5 - 1/1000, 8\pi/5 + 1/1000]$ corresponds to object relative quasi-energy $\omega = E - \beta \in I_\omega = [4\pi/5 - 1/1000, 4\pi/5 + 1/1000]$ ($\beta = 4\pi/5$).
The contact vector on the token side is $|a_0\rangle = \delta_{r=0}\frac{i(|2\rangle - |3\rangle)}{\sqrt{2}} = i\delta_{r=0} B_{\mathrm{coin}}$.

**Theorem 1.1 (Incoming Scalar Boundary Value and Möbius Contact Transform).**
For any $P \in I_P$ and $\omega \in I_\omega$:
1. Under the free relative walk $F_0(P) = S_P M_2$, eliminating the stationary coin channels $(|1\rangle, |4\rangle)$ at energy $\omega$ produces the nonsingular Schur denominator
   $$D(P, \omega) = \cos\omega - \cos P < 0,$$
   and reduces the moving-channel resolvent at $r = 0$ to a scalar Toeplitz integral in relative momentum $q \in [-\pi, \pi)$ with symbol $\cos q - x(P, \omega)$, where
   $$d(P, \omega) = \frac{4\sin\omega}{D(P, \omega)}, \qquad x(P, \omega) = \cos\omega - d(P, \omega)\sin\omega \in (-1, 1).$$
2. Because $x(P, \omega) \in (-1, 1)$ and $\frac{\partial x}{\partial\omega} = -\sin\omega\bigl(1 + \frac{8\cos\omega}{D} + \frac{4\sin^2\omega}{D^2}\bigr) < 0$, the outgoing radiation limit $z = r e^{i\omega}$ ($r \uparrow 1^-$) picks the unique root inside the unit disk with positive real part of the Carathéodory function:
   $$F_{0,B}(P, \omega + i0) = X(P, \omega) + i\,d(P, \omega), \qquad X(P, \omega) = \frac{\sin\omega + d(P, \omega)(\cos\omega + x(P, \omega))}{\sqrt{1 - x(P, \omega)^2}} > 0.$$
3. Including the rank-one contact phase $\Gamma = I + (e^{-ig} - 1)\delta_{r=0}$ on $B_{\mathrm{coin}}$ acts on $F_{0,B}$ by the unitary Möbius transformation with $\tau = \tan(g/2) = \tan(\pi/5) > 0$:
   $$F_B(P, \omega + i0) = \frac{F_{0,B}(P, \omega + i0) + i\tau}{1 + i\tau F_{0,B}(P, \omega + i0)}.$$
   Taking the real part yields the exact boundary spectral density of $W(P)$ on $|a_0\rangle$:
   $$\rho_{B,W}(P, \omega) = \frac{1}{2\pi}\operatorname{Re} F_B(P, \omega + i0) = \frac{(1 + \tau^2)X(P, \omega)}{2\pi\bigl[(1 - \tau d(P, \omega))^2 + \tau^2 X(P, \omega)^2\bigr]}.$$
4. Uniformly on $(P, \omega) \in I_P \times I_\omega$, the certified interval audit proves $\rho_{B,W}(P, \omega) > \frac{77}{1000}$, so the integrated incoming port-2 spectral density on fiber $K$ satisfies
   $$a(K, E) = \int_{-p_{\mathrm{in}}}^{p_{\mathrm{in}}} \rho_{B,W}(P, E - \beta)\,\frac{dP}{2\pi} \ge a := \frac{p_{\mathrm{in}}}{\pi}\inf_{I_P \times I_\omega}\rho_{B,W} > \frac{24}{10^6}.$$
5. Moreover, the relative group speed $v_{\mathrm{rel}} = \frac{\sqrt{1-x^2}}{-\partial_\omega x} > 0$ and the center-to-relative speed ratio $\frac{|\partial_P x|}{\sqrt{1-x^2}} < 1$ hold strictly across $I_P \times I_\omega$, ensuring that both object constituents move strictly away from the standing token at $y = 0$ in the asymptotic incoming regime.

---

## 2. Contact-Selected Flat-Energy Packet and Unit Normalization

**Proposition 2.1 (Packet Construction, Unit Norm, and Zero Incoming Bound Weight).**
Let $\Pi_{\mathrm{sc}}^W(P) = I - \Pi_b(P)$ on $P \in I_P = [-1/1000, 1/1000]$.
1. For each $P \in I_P$, the spectral measure of $U_{0,\mathrm{tok}}(P) = e^{-i\beta}W(P)$ on $\Pi_{\mathrm{sc}}^W(P)|a_0\rangle$ restricted to $E \in I_E$ is absolutely continuous with density $\rho_{B,W}(P, E-\beta) > 77/1000 > 0$.
2. By the Borel functional calculus for the normal operator $W_{\mathrm{sc}}(P) = W(P)\Pi_{\mathrm{sc}}^W(P)$, define on each fiber $K \in [-\pi, \pi)$ the incoming token state localized at $y = 0$ with label $1$:
   $$\Psi_{\mathrm{in}}(K, P, E) = \mathbf{1}_{I_P}(P)\,\frac{\mathbf{1}_{I_E}(E)}{\sqrt{|I_E|}}\,\frac{\Pi_{\mathrm{sc}}^W(P)|a_0\rangle}{\sqrt{a(K, E)}} \otimes |\mathrm{tok}_1(y=0)\rangle.$$
3. Integrating over $P \in I_P$, $E \in I_E$, and $K \in [-\pi, \pi)$ with $\frac{dK}{2\pi}$ gives exact unit norm:
   $$\|\Psi_{\mathrm{in}}\|^2 = \int_{-\pi}^{\pi}\frac{dK}{2\pi}\int_{I_E}\frac{dE}{|I_E|}\,\frac{1}{a(K,E)}\int_{I_P}\rho_{B,W}(P, E-\beta)\,\frac{dP}{2\pi} = \int_{-\pi}^{\pi}\frac{dK}{2\pi}\int_{I_E}\frac{dE}{|I_E|} = 1.$$
4. Because $\Psi_{\mathrm{in}}(K, P, E) \in \operatorname{Ran}(\Pi_{\mathrm{sc}}^W(P) \otimes I_{\mathrm{tok}}) = \ker(\Pi_b(P) \otimes I_{\mathrm{tok}})$ for every $P \in I_P$ and vanishes outside $I_P$, its incoming relative-bound component is identically zero:
   $$(\Pi_b \otimes I_{\mathrm{car}})\Psi_{\mathrm{in}} = 0.$$
   For the auxiliary $K$-windowed reference packet $\Psi_{\mathrm{in}}^{\mathrm{win}} = \sqrt{\frac{\pi}{\delta_K}}\mathbf{1}_{I_K}(K)\Psi_{\mathrm{in}}$, the factor $\pi/\delta_K = 2\pi/|I_K|$ cancels $\int_{I_K}\frac{dK}{2\pi} = \frac{\delta_K}{\pi}$, giving $\|\Psi_{\mathrm{in}}^{\mathrm{win}}\|^2 = 1$.

---

## 3. Homogeneous Output Coarea Density $b_{\mathrm{hom}}$

On the outgoing pulse arrangement in fiber $K \in I_K = [k_0 - \delta_K, k_0 + \delta_K]$ with $k_0 = -\arccos\bigl(\frac{9-5\sqrt{5}}{16}\bigr)$ and $\delta_K = 1/1000$, restrict the object center momentum to $P \in I_P^{\mathrm{out}} = [-p_b, p_b]$ with $p_b = 1/100 < 1/12$, and project onto the bound object branch $\Pi_b(P)$ and the right-moving pulse branch $P_{\mathrm{pulse},1,+}(k)$ at pulse momentum $k = K - P \in [k_0 - p_b - \delta_K, k_0 + p_b + \delta_K] \subset (-\pi, 0)$.

**Theorem 3.1 (Output Root Existence, Coarea Formula, and Uniform Lower Bound $b_{\mathrm{hom}}$).**
1. On $P \in [-p_b, p_b]$ and $K \in I_K$, the total quasi-energy of the bound-pair-plus-right-moving-pulse branch is
   $$f_{K,E}(P) := \Omega_b(P) + \beta + \varepsilon(K - P) - E.$$
   Since $\Omega_b(0) = g = 2\pi/5$, $\beta = 4\pi/5$, $E_* = 8\pi/5$, and $\varepsilon(k_0) = g = 2\pi/5$ (as $\cos\varepsilon(k_0) = \frac{1-4\cos k_0}{5} = \frac{\sqrt{5}-1}{4} = \cos(2\pi/5)$), we have $f_{k_0, E_*}(0) = 0$.
2. By the inherited branch regularity (§4 of `PROOF_CAPTURE_SCATTERING.md`), $|\Omega_b(P) - g - P\Omega_b'(0)| \le L P^2$ with $\Omega_b'(0) = 0$ (by $P \mapsto -P$ symmetry at $P=0$), so $|\Omega_b(P) - g| \le L P^2$ and $|\Omega_b'(P)| \le 2L|P| \le 2Lp_b$ on $|P| \le p_b$.
3. On $k \in [k_0 - p_b - \delta_K, k_0 + p_b + \delta_K]$, the pulse group velocity $v(k) = \varepsilon'(k) = -\frac{4\sin k}{5\sin\varepsilon(k)}$ satisfies $0 < v_{\min} \le v(k) \le v_{\max} < 1$ with
   $$\text{monotonicity margin:} \quad -\frac{\partial f_{K,E}}{\partial P}(P) = v(K-P) - \Omega_b'(P) \ge v_{\min} - 2Lp_b > 0.$$
   Hence $P \mapsto f_{K,E}(P)$ is strictly decreasing on $[-p_b, p_b]$.
4. At the endpoints $P = \mp p_b$, for every $K \in [k_0 - \delta_K, k_0 + \delta_K]$ and every $E \in [E_* - h, E_* + h]$:
   $$f_{K,E}(-p_b) \ge v_{\min}(p_b - \delta_K) - Lp_b^2 - h > 0, \qquad f_{K,E}(+p_b) \le -\bigl[v_{\min}(p_b - \delta_K) - Lp_b^2 - h\bigr] < 0.$$
   By the intermediate value theorem, for every $(K, E) \in I_K \times I_E$ there exists a unique root $P_*(K, E) \in (-p_b, p_b)$ solving $f_{K,E}(P_*) = 0$.
5. At $P = P_*(K, E)$, the bound-branch overlap with $|b_0\rangle$ satisfies $|\langle\chi_b(P), b_0\rangle|^2 = \langle b_0, \Pi_b(P)b_0\rangle \ge 1 - \|\Pi_b(P) - \Pi_b(0)\| \ge 1 - Lp_b > 0$, the right-moving pulse eigenvector $u_+(k)$ has bank-1 weight $|u_{1,+}(k)|^2 = \frac{1 - v(k)}{2} \ge \frac{1 - v_{\max}}{2} > 0$, and the coarea Jacobian is $|\partial_P f_{K,E}(P_*)| \le v_{\max} + 2Lp_b$. Therefore the outgoing port-1 spectral density on $(K, E) \in I_K \times I_E$ is bounded below by
   $$\rho_{1,\mathrm{bd},+}(K, E) = \frac{|\langle\chi_b(P_*), b_0\rangle|^2\,|u_{1,+}(K-P_*)|^2}{2\pi\,|\partial_P f_{K,E}(P_*)|} \ge b_{\mathrm{hom}} := \frac{(1 - Lp_b)\frac{1 - v_{\max}}{2}}{2\pi(v_{\max} + 2Lp_b)} > \frac{1}{100}.$$

---

## 4. Full-Function Hardy-Carathéodory Denominator Bound and Probability Certificate

We bound the Lippmann-Schwinger denominator $|4 + F_1(K, E+i0)F_2(K, E+i0)|^2$ on $I_E$ using the **complete** Carathéodory functions $F_1(K, z)$ and $F_2(K, z)$ without dropping any spectral channels and without extrapolating radial limits from interior circles.

**Theorem 4.1 (Universal Hardy-Carathéodory Bound and Certified Capture Probability).**
1. For each fiber $K \in [-\pi, \pi)$ and port $\alpha \in \{1, 2\}$, $F_\alpha(K, z) = \langle\phi_\alpha, (I + zU_0(K))(I - zU_0(K))^{-1}\phi_\alpha\rangle$ is analytic on $|z| < 1$ with $\operatorname{Re} F_\alpha(K, z) > 0$ and $F_\alpha(K, 0) = \|\phi_\alpha\|^2 = 1$.
2. By the Riesz-Herglotz representation and Zygmund's $H^\alpha$ inequality for functions with positive real part normalized by $F(0) = 1$: for any $\alpha \in (0, 1)$ and $0 < r < 1$, writing $F_\alpha(K, re^{iE}) = |F_\alpha|e^{i\vartheta}$ with $|\vartheta| < \pi/2$,
   $$\operatorname{Re}\bigl(F_\alpha(K, re^{iE})^\alpha\bigr) = |F_\alpha(K, re^{iE})|^\alpha \cos(\alpha\vartheta) \ge |F_\alpha(K, re^{iE})|^\alpha \cos\Bigl(\frac{\pi\alpha}{2}\Bigr).$$
   Since $z \mapsto F_\alpha(K, z)^\alpha$ is analytic on $|z| < 1$ with value $1$ at $z = 0$, the mean-value property gives
   $$\int_{-\pi}^{\pi} |F_\alpha(K, re^{iE})|^\alpha\,\frac{dE}{2\pi} \le \sec\Bigl(\frac{\pi\alpha}{2}\Bigr)\operatorname{Re}\bigl(F_\alpha(K, 0)^\alpha\bigr) = \sec\Bigl(\frac{\pi\alpha}{2}\Bigr).$$
   By Fatou's lemma as $r \uparrow 1^-$, the non-tangential boundary values $F_\alpha(K, E+i0)$ satisfy
   $$\int_{-\pi}^{\pi} |F_\alpha(K, E+i0)|^\alpha\,dE \le C_\alpha := 2\pi\sec\Bigl(\frac{\pi\alpha}{2}\Bigr).$$
3. Fix $\alpha = 9/10 \in (0, 1)$ and energy interval $I_E$ of length $\ell = 2h = 1/500$. Choose the threshold
   $$M := \left[\frac{C_\alpha}{(40/49)\ell}\right]^{2/\alpha} = \left[\frac{2\pi\sec(9\pi/20)}{(40/49)\ell}\right]^{20/9}.$$
   By Markov/Chebyshev's inequality, for each $\alpha_{\mathrm{port}} \in \{1, 2\}$, the bad set $E_{\mathrm{bad},\alpha_{\mathrm{port}}}(K) := \{E \in I_E : |F_{\alpha_{\mathrm{port}}}(K, E+i0)| > M^{1/2}\}$ has Lebesgue measure
   $$\bigl|E_{\mathrm{bad},\alpha_{\mathrm{port}}}(K)\bigr| \le \frac{1}{M^{\alpha/2}}\int_{I_E}|F_{\alpha_{\mathrm{port}}}(K, E+i0)|^\alpha\,dE \le \frac{C_\alpha}{M^{\alpha/2}} = \frac{40}{49}\ell \cdot \frac{1}{2}?$$
   Wait: let us state the exact product Chebyshev bound! By Cauchy-Schwarz on $|F_1 F_2|^{\alpha/2} = |F_1|^{\alpha/2}|F_2|^{\alpha/2}$:
   $$\int_{I_E} |F_1(K, E+i0)F_2(K, E+i0)|^{\alpha/2}\,dE \le \left(\int_{-\pi}^{\pi}|F_1|^\alpha\,dE\right)^{1/2}\left(\int_{-\pi}^{\pi}|F_2|^\alpha\,dE\right)^{1/2} \le C_\alpha.$$
   Therefore, the product bad set $E_{\mathrm{bad}}(K) := \{E \in I_E : |F_1(K, E+i0)F_2(K, E+i0)| > M\}$ satisfies
   $$\bigl|E_{\mathrm{bad}}(K)\bigr| \le \frac{1}{M^{\alpha/2}}\int_{I_E}|F_1(K, E+i0)F_2(K, E+i0)|^{\alpha/2}\,dE \le \frac{C_\alpha}{M^{\alpha/2}} = \frac{40}{49}\ell!$$
   Consequently, the complementary good set $E_{\mathrm{good}}(K) := I_E \setminus E_{\mathrm{bad}}(K)$, on which $|F_1(K, E+i0)F_2(K, E+i0)| \le M$ and hence $|4 + F_1 F_2| \le 4 + M$, has Lebesgue measure at least
   $$\bigl|E_{\mathrm{good}}(K)\bigr| = \ell - \bigl|E_{\mathrm{bad}}(K)\bigr| \ge \Bigl(1 - \frac{40}{49}\Bigr)\ell = \frac{9}{49}\ell.$$
4. Integrating the transition kernel (§3 of `PROOF_CAPTURE_SCATTERING.md`) over $E \in E_{\mathrm{good}}(K) \subset I_E$ for any $K \in I_K$:
   $$\int_{I_E}\frac{dE}{\ell}\,\frac{64\pi^2\,\rho_2(K,E)\,\rho_{1,\mathrm{bd},+}(K,E)}{|4 + F_1(K,E+i0)F_2(K,E+i0)|^2} \ge B_{\mathrm{hom}} := 64\pi^2\,a\,b_{\mathrm{hom}}\,\frac{9/49}{(4 + M)^2} > \frac{8}{10^{25}}.$$
5. For the localized-token preparation $\Psi_{\mathrm{in}}$ (which has uniform weight $\frac{dK}{2\pi}$ across all $K \in [-\pi, \pi)$, so $\int_{I_K}\frac{dK}{2\pi} = \frac{2\delta_K}{2\pi} = \frac{\delta_K}{\pi}$), the asymptotic capture-and-record probabilities on $Q_{\mathrm{full}}$ and $Q_{\mathrm{win}} = \mathbf{1}_{I_K}Q_{\mathrm{full}}$ satisfy
   $$p(Q_{\mathrm{full}}) \ge p(Q_{\mathrm{win}}) \ge \frac{\delta_K}{\pi}\,B_{\mathrm{hom}} > \frac{2}{10^{28}}.$$

---

## 5. Soundness Proof of the Standard-Library Verifier (`verify.py`)

**Theorem 5.1 (Soundness of `RI` and `CRI` Enclosures in `verify.py`).**
Every interval `I = RI(lo, hi)` computed in `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py` is a closed rational interval $[a, b]$ with exact endpoints $a, b \in \mathbb{Q}$ (`fractions.Fraction`) satisfying $a \le b$. Whenever input intervals enclose exact real numbers $x \in I_x, y \in I_y$, the output interval encloses the exact real value of the operation:

1. **Outward rounding (`trim`):** For $S = 10^{36}$, `n_lo = (lo.numerator * S) // lo.denominator` equals $\lfloor \mathrm{lo}\cdot S\rfloor$, and `n_hi = -((-hi.numerator * S) // hi.denominator)` equals $\lceil \mathrm{hi}\cdot S\rceil$. Thus $\frac{n_{\mathrm{lo}}}{S} \le \mathrm{lo} \le \mathrm{hi} \le \frac{n_{\mathrm{hi}}}{S}$, which is also verified at runtime by `assert res.lo <= self.lo and self.hi <= res.hi`.
2. **Field operations and squares (`+`, `-`, `*`, `/`, `sqr`, `abs_iv`):** Standard interval endpoints on $[a,b]$ and $[c,d]$ are computed in exact `Fraction` arithmetic before calling `trim()`. Division asserts $0 \notin [c, d]$ (`not (o.lo <= 0 <= o.hi)`).
3. **Square root (`sqrt`):** Asserts `self.lo >= 0`, constructs non-negative rational endpoints `lo_f, hi_f`, and executes `assert lo_f >= 0 and lo_f * lo_f <= self.lo and self.hi <= hi_f * hi_f`. Since $t \mapsto t^2$ is strictly increasing on $[0, \infty)$, $lo_f^2 \le x \le hi_f^2 \implies lo_f \le \sqrt{x} \le hi_f$.
4. **Arctangent and $\pi$ (`atan_unit_fraction`, `PI`):** For integer $q \ge 2$ and $x = 1/q \in (0, 1/2]$, $\arctan(x) = \sum_{m=0}^\infty (-1)^m c_m$ where $c_m = \frac{x^{2m+1}}{2m+1} > 0$ decreases strictly with $m$. Summing $2N$ terms ends on $-c_{2N-1}$, so by Leibniz's alternating series theorem:
   $$S_{2N} < \arctan(1/q) < S_{2N} + c_{2N} = S_{2N} + \frac{x^{4N+1}}{4N+1}.$$
   Applying Machin's identity $\frac{\pi}{4} = 4\arctan(1/5) - \arctan(1/239)$ in `RI` yields a certified enclosure `PI` of $\pi$.
5. **Cosine and Sine (`cos_sin_point`, `cos_sin`):**
   - At $t \in \mathbb{Q}$, Taylor's theorem at $0$ gives $\cos(t) = \sum_{m=0}^{N-1}(-1)^m \frac{t^{2m}}{(2m)!} + R_{2N}(t)$ with $|R_{2N}(t)| \le \frac{|t|^{2N}}{(2N)!}$ and $\sin(t) = \sum_{m=0}^{N-1}(-1)^m \frac{t^{2m+1}}{(2m+1)!} + R_{2N+1}(t)$ with $|R_{2N+1}(t)| \le \frac{|t|^{2N+1}}{(2N+1)!}$ for all $t \in \mathbb{R}$.
   - For an interval $I = [t_0 - r, t_0 + r]$ with midpoint $t_0 \in \mathbb{Q}$ and radius $r \in \mathbb{Q}$, `cos_sin` asserts $0 \le r \le 2$. For all $\delta \in [-r, r]$ ($r \le 2$), the alternating series for $\cos(\delta)$ and $\sin(\delta)/\delta$ have strictly decreasing terms ($r^2/12 < 1$ and $r^2/6 < 1$), so $1 - r^2/2 \le 1 - \delta^2/2 \le \cos(\delta) \le 1$ and $|\sin(\delta)| \le |\delta| \le r$. Evaluating the addition formulas $\cos(t_0+\delta) = \cos(t_0)\cos(\delta) - \sin(t_0)\sin(\delta)$ and $\sin(t_0+\delta) = \sin(t_0)\cos(\delta) + \cos(t_0)\sin(\delta)$ in `RI` encloses $\cos(I)$ and $\sin(I)$.
6. **Arccosine (`acos_iv`):** Asserts $-1 < \mathrm{iv.lo} \le \mathrm{iv.hi} < 1$, computes rational candidates $\theta_{\mathrm{lo}}, \theta_{\mathrm{hi}}$, and executes `assert F(0) <= th_lo <= th_hi <= PI.lo` and `assert c_at_hi.hi <= iv.lo and iv.hi <= c_at_lo.lo` where `c_at_lo, c_at_hi` are certified enclosures of $\cos(\theta_{\mathrm{lo}}), \cos(\theta_{\mathrm{hi}})$. Thus $\cos(\theta_{\mathrm{hi}}) \le \mathrm{iv.lo} \le x \le \mathrm{iv.hi} \le \cos(\theta_{\mathrm{lo}})$. Since $\cos$ is strictly decreasing on $[0, \pi]$, $\theta_{\mathrm{lo}} \le \arccos(x) \le \theta_{\mathrm{hi}}$.
7. **Rational power $u^{20/9}$ (`power_20_9`):** Asserts $\mathrm{iv.lo} > 0$, computes rational candidates $m_{\mathrm{lo}}, m_{\mathrm{hi}} > 0$, and executes the exact rational integer-power assertion `assert m_lo > 0 and m_lo ** 9 <= u_lo_20 and u_hi_20 <= m_hi ** 9` where `u_lo_20 = iv.lo ** 20` and `u_hi_20 = iv.hi ** 20`. Since $t \mapsto t^9$ is strictly increasing on $(0, \infty)$, $m_{\mathrm{lo}}^9 \le u^{20} \le m_{\mathrm{hi}}^9 \implies m_{\mathrm{lo}} \le u^{20/9} \le m_{\mathrm{hi}}$.
8. **Principal complex square root (`CRI.sqrt_principal`):** Asserts $\mathrm{self.im} > 0$, computes $r = \sqrt{\mathrm{re}^2 + \mathrm{im}^2}$, $u = \sqrt{(r+\mathrm{re})/2} > 0$, $v = \sqrt{(r-\mathrm{re})/2} > 0$, and asserts $0 \in (u+iv)^2 - (\mathrm{re}+i\,\mathrm{im})$. Since $u > 0, v > 0$, $u + iv$ encloses the unique principal square root in the first quadrant.
