# P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-1: Preregistration

- **Status:** PREREGISTERED (independent result-exposed adversarial audit of `#1519` / `#1520`, assigned in `#1521`)
- **Owner session:** `Antigravity-20261015-abdf12b3` (distinct from primary author session `ChatGPT-20261015-affine-receiver`)
- **Author:** A. M. Thorn `<thorn@twistj.com>`
- **Branch:** `probe/P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-1`
- **Path:** `probes/P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-1/`
- **Action layer:** `L1` (exact finite-field state and orbit algebra on unchanged native `U`; no Canon promotion, merge, release, or physical apparatus/occurrence claim)
- **Public authority basis:** `mathorn1973/twist-j` `main` at `8b91a935c426036e00ecb300019fd94734addeec`, `Public Canon v101`, tag `canon-v101` (`1be57c8104b5cfef68a3268131f43200a0e133ac`), `CONTENT_COMMIT` `421a4ec1daf07c04d19022c1ee219607e83c09a8`, `CANON_SHA256` `b83a99feccac173bd3c9c5851c5874ca27cbd135f71d136d793b45f86c8a87f7`, `CANON_BYTES` `992352`.

## 1. Exposure and independence statement

This audit is a result-exposed independent review, not a blind prediction. Before committing, pushing, and reading back this preregistration and executing the first formal run:

- Read only:
  - Issue `#1521` (`[INDEPENDENT AUDIT] P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-1`),
  - Issue `#1519` summary and comments,
  - `5caff8280c195c12c8c41bf462daae8e6d4bd64b:notes/C-U-AFFINE-TWO-COORD-RECEIVER-N/PREREG.md`,
  - `probes/P-U-NATIVE-MEMORY-EVENT-1/MEMORY-PROOF.md` and `probes/P-U-NATIVE-MEMORY-EVENT-1/CLOCK-PROOF.md`,
  - `STATUS.md`, `POLICY.md`, `AGENTS.md`, `canon/CORE.md`, `canon/FRONTIER.md`, and relevant rows of `canon/REGISTRY.tsv`, `canon/EVIDENCE.tsv`, and `canon/GATES.tsv`,
  - Titles/states of neighboring issues `#992`, `#993`, `#994`, `#1429`, `#1430`.
- Did **NOT** read or inspect the primary `notes/C-U-AFFINE-TWO-COORD-RECEIVER-N/verify.py`, `EXPECTED.txt`, `RUN.md`, `RESULT.md`, `PROOF.md`, or the PR `#1520` diff/files. (The closing comment on `#1519` mentions the primary stdout byte count and SHA-256; no primary code or output lines were viewed.)
- `probes/P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-1/break.py` and `probes/P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-1/verify.py` were authored from scratch from the mathematical specification alone and checked only with `python3 -m py_compile` before the pin commit.

## 2. Equations Under Audit

Let $x = (a, u, c, v, q, r) \in \mathbb{F}_5^6$, $z(x) = a + u + c + v + q + r \bmod 5$, $\theta_n = \operatorname{popcount}(n) \bmod 2$, and
$$U(n, x) = \left(n + 1,\; T_{\theta_n}(x)\right), \qquad T_t(x) = g_{(z(x) + 2t) \bmod 5}(x),$$
where the five generators on $\mathbb{F}_5^6$ are:
$$\begin{aligned}
g_0(x) &= (u, a, v, c, q, r), \\
g_1(x) &= (-c, -v, -a, -u, -q, -r), \\
g_2(x) &= (2-c, 1-v+r, 2-a, 1-u-r, 1-q, -r), \\
g_3(x) &= (2-a, 1-u, 3-c, 4-v, 1-q, 1-r) = -x + t_3, \quad t_3 = (2,1,3,4,1,1), \\
g_4(x) &= (2-a, 1-u, 3-c, 4-v, 2-q, 1-r) = -x + t_4, \quad t_4 = (2,1,3,4,2,1).
\end{aligned}$$

### Target A (Late construction from $n = 5$)
Define
$$A = a+c,\quad B = u+v,\quad C = a-c-2,\quad D = u-v-1,\quad \Sigma = q+r,\quad w = q-r,\quad H = \Sigma + 3(A-B) \pmod 5.$$
- Split 1: $\bar{R}(x) = (u, v, \Sigma) \in \mathbb{F}_5^3$, $\bar{S}(x) = (a, c, w) \in \mathbb{F}_5^3$, with inverse $q = 3(\Sigma + w), r = 3(\Sigma - w)$.
- Split 2: $\tilde{R}(x) = (D, H) \in \mathbb{F}_5^2$, $\tilde{S}(x) = (a, c, B, w) \in \mathbb{F}_5^4$, with proposed inverse
  $$u = 3(B + D + 1),\quad v = 3(B - D - 1),\quad \Sigma = H - 3(A - B),\quad q = 3(\Sigma + w),\quad r = 3(\Sigma - w).$$
- Initial family at $n = 5$ for $(\lambda, \mu) \in \mathbb{F}_5^2$:
  $$x_5(\lambda, \mu) = (\lambda,\; 0,\; 2-\lambda,\; 0,\; -1-\mu,\; \mu-1) \pmod 5,$$
  with common $\bar{R}(x_5) = (0, 0, 3)$ and $\tilde{R}(x_5) = (4, 4)$.
- Readers:
  $$G(D, H) = \begin{cases} \mathrm{PRESENT}(4 - 3D) & H = 0, \\ \mathrm{PRESENT}(4 - 2D) & H \in \{2, 3\}, \\ \mathrm{BLANK} & H \in \{1, 4\}, \end{cases}$$
  and for $\bar{R} = (u, v, \Sigma)$ with $Z = 2B + \Sigma \bmod 5$:
  $$\bar{G}(u, v, \Sigma) = \begin{cases} \mathrm{PRESENT}(u) & B = 2,\; \Sigma = 3, \\ \mathrm{PRESENT}(4 - B Z D) & B \in \{2, 3\},\; Z \in \{1, 4\},\; (B, \Sigma) \ne (2, 3), \\ \mathrm{BLANK} & \text{otherwise}. \end{cases}$$
- Audit targets:
  1. Actual transitions at $n = 5, 6, 7, 8$ select $g_0, g_0, g_2, g_4$, yielding $x_7(\lambda, \mu) = x_5(\lambda, \mu)$ (full receiver and checkpoint restoration at $n=7$, with $(7, x_7) \ne (5, x_5)$) and outputs $\mathrm{BLANK}, \mathrm{PRESENT}(\lambda), \mathrm{BLANK}, \mathrm{PRESENT}(\mu)$ at $n = 5, 6, 7, 8$.
  2. For $n \ge 9$, trajectories remain in the 500-state continuation carrier
     $$\mathcal{C}_{500} = \{x \in \mathbb{F}_5^6 : A = B \in \{2, 3\},\; z(x) \in \{1, 4\}\},$$
     on which both $T_0$ and $T_1$ preserve $A z C = 2 - \lambda$ and $B z D = 4 - \mu$, both readers $G \circ \tilde{R}$ and $\bar{G} \circ \bar{R}$ output $\mathrm{PRESENT}(\mu)$, and $2 - A(2A + H)C \equiv \lambda \pmod 5$.
  3. The second source is not emptied ($w_8 = 1 + 2\mu, w_9 = 3\mu \bmod 5$ retains all 5 values), $H$ depends on the source sum $A = a+c$, at least two $\mathbb{F}_5$ coordinates are necessary for 6 distinct labels ($5^1 < 6 \le 5^2$), and the bare memory pair $(u, v)$ has identical recurrent support on the $\mu$-classes $\{0, 3\}, \{1, 2\}, \{4\}$.

### Target B (Preparation boundary and $0011$ launch windows)
- Complete trace maps $\tau_t(z) = z(T_t(x))$:
  $$\tau_0 = (0 \mapsto 0,\; 1 \mapsto 4,\; 2 \mapsto 0,\; 3 \mapsto 4,\; 4 \mapsto 4), \qquad \tau_1 = (0 \mapsto 2,\; 1 \mapsto 1,\; 2 \mapsto 1,\; 3 \mapsto 3,\; 4 \mapsto 1).$$
- Control window characterization:
  $$(\theta_n, \theta_{n+1}, \theta_{n+2}, \theta_{n+3}) = (0, 0, 1, 1) \iff n = 2m + 1 \text{ and } (\theta_m, \theta_{m+1}, \theta_{m+2}) = (1, 0, 1).$$
- Infinite family $n_k = 3 \cdot 2^k + 5$ ($k \ge 4$) satisfies this characterization.
- Because $n - 1 = 2m$ has $\theta_{n-1} = \theta_m = 1$ and $0 \notin \operatorname{im}(\tau_1) = \{1, 2, 3\}$, no state $(n, x_n)$ with $z(x_n) = 0$ at any $0011$ launch index $n$ has an immediate predecessor under $U$.

### Target C (Origin-zero all-affine obstruction)
For any preparation map $E: \mathbb{F}_5^2 \to \mathbb{F}_5^6$, any fixed affine receiver $R(x) = L x + h$ ($L \in \mathbb{F}_5^{k \times 6}, h \in \mathbb{F}_5^k$, arbitrary $k \ge 0$), and any fixed total reader $G: \mathbb{F}_5^k \to \mathcal{O}$:
1. For every $x_0 \in \mathbb{F}_5^6$, origin-zero evolution gives $z(x_1) \in \{0, 4\}$ and $z(x_2) \in \{1, 2\}$ ($z(x_2) = 2$ for $z(x_0) \in \{0, 2\}$; $z(x_2) = 1$ for $z(x_0) \in \{1, 3, 4\}$). At $n = 2$ ($\theta_2 = 1$), the selected generator is $g_3$ if $z(x_2) = 1$ and $g_4$ if $z(x_2) = 2$, so $x_3 = -x_2 + t_3$ or $x_3 = -x_2 + t_4$.
2. If $R(x_2(\lambda, \mu)) = r_{\mathrm{ready}}$ is common, then
   $$R(x_3(\lambda, \mu)) \in \{-r_{\mathrm{ready}} + 2h + L t_3,\; -r_{\mathrm{ready}} + 2h + L t_4\},$$
   so $|\{R(x_3(\lambda, \mu))\}| \le 2$, excluding 5 distinct second messages at $n = 3$.
3. Under the stronger eventual-retention contract ($R(x_2) = r_{\mathrm{ready}}$, $G(r_{\mathrm{ready}}) = \mathrm{BLANK}$, and $G(R(x_n)) = \mathrm{PRESENT}(\mu)$ for all $n \ge N(\lambda, \mu)$):
   - Every preparation with $z(x_2) = 1$ has $x_2 \in X_1 \subset X_{14}$ and $x_3 = g_3(x_2)$ in the same $X_{14}$ recurrent sign fibre $\{V(x_3), -V(x_3)\}$. By `U-NATIVE-INVARIANT-AND-NOWRITE`, $(x_n)_{n \ge 3}$ visits $x_2$ infinitely often, forcing any eventually constant value of $G \circ R$ to equal $G(R(x_2)) = \mathrm{BLANK}$.
   - All remaining preparations have $z(x_2) = 2$, hence share the single receiver state $R(x_3) = -r_{\mathrm{ready}} + 2h + L t_4 =: r_3^{(4)}$ at $n = 3$, and since $x_3 \in X_1 \subset X_{14}$ recurs infinitely often in $(x_n)_{n \ge 3}$ by `U-NATIVE-INVARIANT-AND-NOWRITE`, any eventually constant value of $G \circ R$ must equal $G(r_3^{(4)})$. Thus at most **one** nonblank second message label can ever be permanently retained.

## 3. Code Pin

- `probes/P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-1/break.py`:
  - SHA-256: `3f54909fbc1ac70f2176c3b0a277b2611b932f1a6bea9d3b9092f84e1d578e7c`
  - Bytes: `17871`
- `probes/P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-1/verify.py`:
  - SHA-256: `b7feb582c56ffd0299b1f4bfb7d54193baebcf067a8553c217da8858b1b71267`
  - Bytes: `580`

## 4. Carrier and Finite Audit Domain

- Full state space $\mathbb{F}_5^6$ ($15,625$ states):
  - $78,125$ direct-vs-matrix generator comparisons and $78,125$ involution checks;
  - $31,250$ controlled trace-map checks and $T_1^{-1}(X_0) = \emptyset$ verification;
  - $62,500$ two-way global chart-inverse checks for $(\bar{R}, \bar{S})$ and $(\tilde{R}, \tilde{S})$;
  - $15,625$ origin-zero three-step prefix checks ($x_0 \mapsto x_1 \mapsto x_2 \mapsto x_3$), verifying $z(x_2) \in \{1, 2\}$, $x_2 + x_3 \in \{t_3, t_4\}$, and $V(x_3) = -V(x_2)$ for all $9,375$ states with $z(x_2) = 1$, plus constructive sharpness witnesses for the bounds $\le 2$ and $\le 1$.
- Late construction domain:
  - All $25$ preparations $x_5(\lambda, \mu)$, four prefix steps $n = 5 \to 6 \to 7 \to 8 \to 9$, full $500$-state continuation carrier $\mathcal{C}_{500}$ and all $1,000$ controlled transitions, $25 \times 1,020 = 25,500$ trajectory states ($5 \le n \le 1024$), and bare $(u, v)$ recurrent-support equivalence classes $\{0, 3\}, \{1, 2\}, \{4\}$.
- Launch window regression domain:
  - All $0 \le n < 4096$ and the explicit infinite family $n_k = 3 \cdot 2^k + 5$ for $k = 4, \dots, 31$.

## 5. Systematics

- All calculations use Python standard-library exact integer arithmetic modulo $5$; no floating-point numbers, random sampling, or external packages are used.
- Infinite-time claims (universal retention from $n \ge 9$, infinitely many $0011$ launch indices $n_k$, and the all-affine origin-zero obstructions) rest on self-contained algebraic proofs and the public theorem `U-NATIVE-INVARIANT-AND-NOWRITE`, never on finite simulation length alone.

## 6. Failure Threshold

- **Zero tolerance:** Any single mismatch in any of the $15,625$-state generator/inverse/prefix checks, any violation on the $500$-state carrier or $1,000$ transitions, any discrepancy along the $25,500$ trajectory states, any $0011$ window mismatch or predecessor witness on $X_0$, or any loophole in the all-affine proof immediately fires and invalidates the affected target claim. No threshold or code may be modified after the pin.
