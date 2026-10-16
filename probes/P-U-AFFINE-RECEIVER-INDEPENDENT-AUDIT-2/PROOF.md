# P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-2: Independent Proof and Adversarial Review

- **Status:** NON-CANONICAL / L1 / Independent review of `#1519` (`notes/C-U-AFFINE-TWO-COORD-RECEIVER-N`, PR `#1520`) under assignment `#1521`
- **Owner session:** `Antigravity-20261015-abdf12b3`
- **Author:** A. M. Thorn `<thorn@twistj.com>`
- **Immutable code pin:** `725b519cb49de7ccf8de5086ec6543c625e68f1c`
- **First formal run commit (before primary inspection):** `8df07b09001d4b36b1e7a96dc2e57e5d337dde76`

---

## 1. Complete Trace Maps and Involution Structure

For $x = (a, u, c, v, q, r) \in \mathbb{F}_5^6$, let $z(x) = a + u + c + v + q + r \bmod 5$.
The five generators $g_0, \dots, g_4$ are affine maps $g_k(x) = M_k x + t_k$ on $\mathbb{F}_5^6$:
$$\begin{aligned}
g_0(x) &= (u, a, v, c, q, r), & z(g_0(x)) &= z(x), \\
g_1(x) &= (-c, -v, -a, -u, -q, -r), & z(g_1(x)) &= -z(x) \bmod 5, \\
g_2(x) &= (2-c, 1-v+r, 2-a, 1-u-r, 1-q, -r), & z(g_2(x)) &= 2 - z(x) \bmod 5, \\
g_3(x) &= -x + t_3,\quad t_3 = (2,1,3,4,1,1), & z(g_3(x)) &= 2 - z(x) \bmod 5, \\
g_4(x) &= -x + t_4,\quad t_4 = (2,1,3,4,2,1), & z(g_4(x)) &= 3 - z(x) \bmod 5.
\end{aligned}$$
Direct substitution shows $g_k(g_k(x)) = x$ for every $k \in \{0,1,2,3,4\}$ and every $x \in \mathbb{F}_5^6$ (for $g_2$, $1 - (1 - u - r) + (-r) = u$ and $1 - (1 - v + r) - (-r) = v$). Thus each $g_k$ is an involution and restricts to a bijection from each trace sheet $X_z = \{x \in \mathbb{F}_5^6 : z(x) = z\}$ ($|X_z| = 5^5 = 3125$) onto $X_{z(g_k(x))}$.

Under $T_t(x) = g_{(z(x) + 2t) \bmod 5}(x)$ for control bit $t \in \{0, 1\}$, the induced trace maps $\tau_t: \mathbb{F}_5 \to \mathbb{F}_5$ are:

| $z$ | $0$ | $1$ | $2$ | $3$ | $4$ | Image $\operatorname{im}(\tau_t)$ | Image size in $\mathbb{F}_5^6$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $T_0$ generator | $g_0$ | $g_1$ | $g_2$ | $g_3$ | $g_4$ | | |
| $\tau_0(z)$ | $0$ | $4$ | $0$ | $4$ | $4$ | $\{0, 4\}$ | $2 \times 3125 = 6250$ |
| $T_1$ generator | $g_2$ | $g_3$ | $g_4$ | $g_0$ | $g_1$ | | |
| $\tau_1(z)$ | $2$ | $1$ | $1$ | $3$ | $1$ | $\{1, 2, 3\}$ | $3 \times 3125 = 9375$ |

---

## 2. Section A: Late Construction from $n = 5$, Global Splits, and Continuation

### 2.1 Global affine splits and inverses
With $A = a+c$, $B = u+v$, $C = a-c-2$, $D = u-v-1$, $\Sigma = q+r$, $w = q-r$, and $H = \Sigma + 3(A-B) \pmod 5$:
1. The $3+3$ split $\bar{R}(x) = (u, v, \Sigma)$, $\bar{S}(x) = (a, c, w)$ has exact global inverse
   $$q = 3(\Sigma + w) \bmod 5, \qquad r = 3(\Sigma - w) \bmod 5$$
   because $3 \equiv 2^{-1} \pmod 5$.
2. The $2+4$ affine split $\tilde{R}(x) = (D, H)$, $\tilde{S}(x) = (a, c, B, w)$ has exact global inverse
   $$A = a+c,\quad u = 3(B + D + 1),\quad v = 3(B - D - 1),\quad \Sigma = H - 3(A - B),\quad q = 3(\Sigma + w),\quad r = 3(\Sigma - w) \pmod 5,$$
   since $B + D + 1 = 2u$ and $B - D - 1 = 2v$. Both are verified both algebraically and across all $62,500$ two-way inverse checks on $\mathbb{F}_5^6$.

### 2.2 Four-step prefix from $n = 5$
For $(\lambda, \mu) \in \mathbb{F}_5^2$, the prepared state at $n = 5$ is
$$x_5(\lambda, \mu) = (\lambda,\; 0,\; 2-\lambda,\; 0,\; -1-\mu,\; \mu-1) \pmod 5.$$
Since $\theta_5 = 0, \theta_6 = 0, \theta_7 = 1, \theta_8 = 1$:
- **$n = 5$:** $A_5 = 2, B_5 = 0, C_5 = 2\lambda + 1, D_5 = 4, \Sigma_5 = 3, w_5 = 3\mu, z(x_5) = 0$.
  $\bar{R}(x_5) = (0, 0, 3)$ and $\tilde{R}(x_5) = (4, 4)$ are common across all $25$ pairs. Since $H_5 = 4 \in \{1, 4\}$ and $B_5 = 0 \notin \{2, 3\}$, both $G(\tilde{R}(x_5))$ and $\bar{G}(\bar{R}(x_5))$ return $\mathrm{BLANK}$.
- **$n = 5 \to 6$ ($\theta_5 = 0, z_5 = 0 \implies g_0$):**
  $$x_6(\lambda, \mu) = (0,\; \lambda,\; 0,\; 2-\lambda,\; -1-\mu,\; \mu-1) \pmod 5.$$
  Here $A_6 = 0, B_6 = 2, D_6 = 2\lambda + 2, \Sigma_6 = 3, z_6 = 0, H_6 = 3 + 3(0 - 2) \equiv 2 \pmod 5$.
  Thus $G(D_6, H_6) = \mathrm{PRESENT}(4 - 2(2\lambda + 2)) = \mathrm{PRESENT}(\lambda)$, and $\bar{G}(\lambda, 2-\lambda, 3)$ takes the branch $(B_6, \Sigma_6) = (2, 3)$ to return $\mathrm{PRESENT}(u_6) = \mathrm{PRESENT}(\lambda)$.
- **$n = 6 \to 7$ ($\theta_6 = 0, z_6 = 0 \implies g_0$):**
  Because $g_0$ is an involution, $x_7(\lambda, \mu) = g_0(x_6(\lambda, \mu)) = x_5(\lambda, \mu)$ (while $(7, x_7) \ne (5, x_5)$ in $\mathbb{N}_0 \times \mathbb{F}_5^6$). Both $\bar{R}(x_7) = (0, 0, 3)$ and $\tilde{R}(x_7) = (4, 4)$ are completely restored, and both readers return $\mathrm{BLANK}$.
- **$n = 7 \to 8$ ($\theta_7 = 1, z_7 = 0 \implies g_2$):**
  $$x_8(\lambda, \mu) = (\lambda,\; \mu,\; 2-\lambda,\; 2-\mu,\; 2+\mu,\; 1-\mu) \pmod 5.$$
  Here $A_8 = 2, B_8 = 2, C_8 = 2\lambda + 1, D_8 = 2\mu + 2, \Sigma_8 = 3, w_8 = 1 + 2\mu, z_8 = 2, H_8 = 3$.
  Both $G(D_8, 3) = \mathrm{PRESENT}(4 - 2(2\mu + 2))$ and $\bar{G}(\mu, 2-\mu, 3)$ (via $B_8 = 2, \Sigma_8 = 3$) return $\mathrm{PRESENT}(\mu)$. The second source is not emptied ($w_8 = 1 + 2\mu, r_8 = 1 - \mu$).
- **$n = 8 \to 9$ ($\theta_8 = 1, z_8 = 2 \implies g_4$):**
  $$x_9(\lambda, \mu) = (2-\lambda,\; 1-\mu,\; 1+\lambda,\; 2+\mu,\; -\mu,\; \mu) \pmod 5.$$
  Here $A_9 = B_9 = 3 \in \{2, 3\}$, $z_9 = 1 \in \{1, 4\}$, $C_9 = 4 - 2\lambda$, $D_9 = 3 - 2\mu$, $\Sigma_9 = H_9 = 0$, $w_9 = 3\mu$, and
  $$A_9 z_9 C_9 = 3 \cdot 1 \cdot (4 - 2\lambda) \equiv 2 - \lambda \pmod 5, \qquad B_9 z_9 D_9 = 3 \cdot 1 \cdot (3 - 2\mu) \equiv 4 - \mu \pmod 5.$$

### 2.3 All-time invariance on the 500-state continuation carrier ($n \ge 9$)
Define
$$\mathcal{C}_{500} = \{x \in \mathbb{F}_5^6 : A = B \in \{2, 3\},\; z(x) \in \{1, 4\}\}.$$
Because $(z, A, B, C, D, r)$ is a bijection on $X_{14}$, $|\mathcal{C}_{500}| = 2 \times 2 \times 5 \times 5 \times 5 = 500$ (20 states for each of the 25 pairs $(\lambda, \mu)$).
On $X_{14}$, any control bit $t \in \{0, 1\}$ selects either:
- $g_1$: $(A', B', C', D', z') = (-A, -B, C, D, -z)$, or
- $g_3, g_4$: $(A', B', C', D', z') = (-A, -B, -C, -D, z)$.
In both cases, $A = B \in \{2, 3\} \implies A' = B' = -A \in \{2, 3\}$, $z' \in \{1, 4\}$, and
$$A' z' C' = A z C = 2 - \lambda \pmod 5, \qquad B' z' D' = B z D = 4 - \mu \pmod 5.$$
Moreover, on $\mathcal{C}_{500}$, $A = B$ implies $H = \Sigma = z - 2B \in \{0, 2, 3\}$ and $Z = 2B + \Sigma = 2A + H = z \in \{1, 4\}$:
- When $(B, z) \in \{(2, 4), (3, 1)\}$, $H = 0$ and $B z \equiv 3 \pmod 5$, so $4 - B Z D = 4 - 3D = \mu$.
- When $(B, z) \in \{(2, 1), (3, 4)\}$, $H \in \{2, 3\}$ and $B z \equiv 2 \pmod 5$, so $4 - B Z D = 4 - 2D = \mu$.
Thus for every $n \ge 8$, both $G(\tilde{R}(x_n))$ and $\bar{G}(\bar{R}(x_n))$ return $\mathrm{PRESENT}(\mu)$, and for every $n \ge 9$, $2 - A_n(2A_n + H_n)C_n = 2 - A_n z_n C_n = \lambda$.

### 2.4 Two-coordinate lower bound and bare $(u, v)$ support
1. Because $|\mathbb{F}_5^1| = 5 < 6$, no fixed total reader on fewer than two $\mathbb{F}_5$ coordinates can produce the six distinct outputs $\mathrm{BLANK}, \mathrm{PRESENT}(0), \dots, \mathrm{PRESENT}(4)$. Thus $k \ge 2$ is sharp in the affine-split class. However, $H = \Sigma + 3(A - B)$ depends on the source sum $A = a+c$, so $\tilde{R} = (D, H)$ changes the allowed coordinate-access class relative to $\bar{R} = (u, v, \Sigma)$.
2. Along the recurrent $X_{14}$ sign fibre $\{V(x_9), -V(x_9)\}$, the bare memory pair $(u, v)$ is determined by $B \in \{2, 3\}$ and $D \in \{\pm(3 - 2\mu)\}$. Since $3 - 2(3 - \mu) \equiv -(3 - 2\mu) \pmod 5$, the recurrent $(u, v)$ support depends only on $\{3 - 2\mu, 2 + 2\mu\}$ and merges into the exact equivalence classes $\{0, 3\}$ (4 points), $\{1, 2\}$ (4 points), and $\{4\}$ (2 points).

---

## 3. Section B: $0011$ Launch Windows and Missing Predecessors

1. **Characterization of $0011$ starts:**
   Since $\theta_{2m} = \theta_m$ and $\theta_{2m+1} = 1 - \theta_m$, an even index $n = 2m$ always has $\theta_n \ne \theta_{n+1}$ and cannot start $0011$. For odd $n = 2m + 1$:
   $$(\theta_{2m+1}, \theta_{2m+2}, \theta_{2m+3}, \theta_{2m+4}) = (1 - \theta_m,\; \theta_{m+1},\; 1 - \theta_{m+1},\; \theta_{m+2}) = (0, 0, 1, 1) \iff (\theta_m, \theta_{m+1}, \theta_{m+2}) = (1, 0, 1).$$
2. **Infinite family $n_k = 3 \cdot 2^k + 5$ ($k \ge 4$):**
   Writing $n_k = 2m_k + 1$ gives $m_k = 3 \cdot 2^{k-1} + 2$. Because $k - 1 \ge 3$, the binary support of $3 \cdot 2^{k-1}$ lies at bit positions $\ge 3$ and does not overlap $\{2, 3, 4\}$. Hence $\operatorname{popcount}(m_k) = 3$, $\operatorname{popcount}(m_k + 1) = 4$, and $\operatorname{popcount}(m_k + 2) = 3$, so $(\theta_{m_k}, \theta_{m_k+1}, \theta_{m_k+2}) = (1, 0, 1)$ for every $k \ge 4$.
3. **No predecessor on $X_0$:**
   At every $0011$ start $n = 2m + 1$, the preceding index is $n - 1 = 2m$, which has $\theta_{n-1} = \theta_m = 1$. Thus any predecessor $(n-1, x_{n-1})$ under $U$ would satisfy $x_n = T_1(x_{n-1})$ and $z(x_n) \in \operatorname{im}(\tau_1) = \{1, 2, 3\}$. Since $0 \notin \{1, 2, 3\}$, no state $(n, x_n)$ with $z(x_n) = 0$ (including all 25 late-start states $x_5(\lambda, \mu)$) has an immediate predecessor under $U$.

---

## 4. Section C: Complete Origin-Zero All-Affine Obstruction

Let $E: \mathbb{F}_5^2 \to \mathbb{F}_5^6$ be any preparation map, $R(x) = L x + h$ ($L \in \mathbb{F}_5^{k \times 6}, h \in \mathbb{F}_5^k$, arbitrary $k \ge 0$) any fixed affine receiver, and $G: \mathbb{F}_5^k \to \mathcal{O}$ any fixed total reader.

### Theorem C1 (At most two receiver states at $n = 3$)
From $\theta_0 = 0, \theta_1 = 1, \theta_2 = 1$ and the trace table in Section 1, every initial state $x_0 \in \mathbb{F}_5^6$ satisfies:
$$\begin{aligned}
z(x_0) \in \{0, 2\} &\implies z(x_1) = 0 \implies z(x_2) = 2 \implies x_3 = g_4(x_2) = -x_2 + t_4, \\
z(x_0) \in \{1, 3, 4\} &\implies z(x_1) = 4 \implies z(x_2) = 1 \implies x_3 = g_3(x_2) = -x_2 + t_3.
\end{aligned}$$
If $R(x_2(\lambda, \mu)) = r_{\mathrm{ready}}$ for all prepared pairs, then for every preparation:
$$R(x_3(\lambda, \mu)) = L(-x_2(\lambda, \mu) + t) + h = -r_{\mathrm{ready}} + 2h + L t \in \left\{\, -r_{\mathrm{ready}} + 2h + L t_3,\;\; -r_{\mathrm{ready}} + 2h + L t_4 \,\right\}.$$
Hence $|\{R(x_3(\lambda, \mu))\}| \le 2$ and $|\{G(R(x_3(\lambda, \mu)))\}| \le 2 < 5$, ruling out the 25-pair $n = 3$ retention contract for every affine receiver $R$ and every reader $G$.

*Sharpness:* The bound $2$ is attained by $R(x) = q$ on $x_0^{(1)} = (1,0,0,0,0,0)$ and $x_0^{(2)} = (2,0,0,0,0,0)$, which satisfy $R(x_2^{(1)}) = R(x_2^{(2)}) = 0$ and $\{R(x_3^{(1)}), R(x_3^{(2)})\} = \{1, 2\}$.

### Theorem C2 (At most one permanently retained nonblank second message)
Suppose $R(x_2) = r_{\mathrm{ready}}$, $G(r_{\mathrm{ready}}) = \mathrm{BLANK}$, and for each prepared trajectory there is a finite onset $N(x_0) \ge 3$ such that $G(R(x_n)) = \mathrm{PRESENT}(\mu(x_0))$ for all $n \ge N(x_0)$. Apply `U-NATIVE-INVARIANT-AND-NOWRITE` to the fixed full-checkpoint reader $f = G \circ R: \mathbb{F}_5^6 \to \mathcal{O}$:
1. If $z(x_2) = 1$ ($z(x_0) \in \{1, 3, 4\}$), then $x_2 \in X_1 \subset X_{14}$ and $x_3 = g_3(x_2) \in X_1$ satisfy $V(x_3) = -V(x_2)$ (verified both algebraically from `MEMORY-PROOF.md` Section 1 and across all $9,375$ states with $z(x_2) = 1$). Thus $x_2$ lies in the $X_{14}$ recurrent sign fibre $\{V(x_3), -V(x_3)\}$ of $x_3$. By `U-NATIVE-INVARIANT-AND-NOWRITE`, $(x_n)_{n \ge 3}$ visits every point of that fibre—including $x_2$—infinitely often, forcing $\mathrm{PRESENT}(\mu(x_0)) = f(x_2) = G(r_{\mathrm{ready}}) = \mathrm{BLANK}$, a contradiction.
2. Therefore every admitted preparation must satisfy $z(x_2) = 2$ ($z(x_0) \in \{0, 2\}$) and $x_3 = g_4(x_2) = -x_2 + t_4$, so all admitted preparations share the single receiver state
   $$R(x_3) = -r_{\mathrm{ready}} + 2h + L t_4 =: r_3^{(4)}.$$
   Since $x_3 \in X_1 \subset X_{14}$ recurs infinitely often in $(x_n)_{n \ge 3}$ by `U-NATIVE-INVARIANT-AND-NOWRITE`, $\mathrm{PRESENT}(\mu(x_0)) = f(x_3) = G(r_3^{(4)})$ for every admitted preparation. Thus at most **one** nonblank second message $\mu$ can ever be permanently retained.

*Sharpness:* The bound $1$ is attained by $R(x) = z(x)$ on $x_0 \in X_2$, where $R(x_0) = R(x_2) = 2$, $R(x_1) = 0$, and $R(x_n) \in \{1, 4\}$ for all $n \ge 3$.

---

## 5. Post-Pin Comparison with Primary `notes/C-U-AFFINE-TWO-COORD-RECEIVER-N`

After committing, pushing, and reading back the independent pin (`725b519cb49de7ccf8de5086ec6543c625e68f1c`) and first run (`8df07b09001d4b36b1e7a96dc2e57e5d337dde76`), the primary files at `fec2816939ba610a914f7e7e59eb10729999d72e` were inspected:

| Audit item | Primary (`notes/.../EXPECTED.txt`) | Independent (`break.py` / `EXPECTED.txt`) | Verdict |
| :--- | :--- | :--- | :--- |
| Full state space $\mathbb{F}_5^6$ | `15625` | `15625` | Exact match |
| Generator direct vs matrix comparisons | `78125` (+ `78125` involution checks) | `78125` (+ `78125` involution checks) | Exact match |
| Global coordinate inverse checks | `62500` | `62500` | Exact match |
| Selected trace checks & image sizes | `31250`, `[6250, 9375]` | `31250`, $T_1^{-1}(X_0) = \emptyset$, $|X_0 \cup X_4| = 6250$ | Exact match |
| Late $n=5$ preparations & prefix edges | `25` pairs, `100` prefix edges | `25` pairs, $n=5 \to 6 \to 7 \to 8 \to 9$ verified | Exact match |
| Continuation carrier & transitions | `500` states, `1000` edges | `500` states, `1000` edges | Exact match |
| Trajectory checkpoint checks ($5 \le n \le 1024$) | `25500` | `25500` | Exact match |
| Bare $(u, v)$ support partition | `[[0,3],[1,2],[4]]` | `{0,3}\|{1,2}\|{4}` | Exact match |
| $0011$ launch criterion ($0 \le n < 4096$) & $k=4,\dots,31$ | `4096` indices (`341` starts), `28` $n_k$ checks | `4096` indices (`341` starts), `28` $n_k$ checks | Exact match |
| Origin-zero $x_2$ sheets & $x_2 + x_3$ shifts | `X1, X2`; `{t_d, t_e}` | `{1, 2}`; `{t_3, t_4}` (plus `sign_class_v(x2) == sign_class_v(x3)` on $z_2 = 1$ and sharpness witnesses) | Confirmed & strengthened |

No mathematical error, hidden assumption, or scope inflation was found in the primary `PROOF.md`, `RESULT.md`, or `verify.py`.
