# P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-1 — Preregistration

## 1. Metadata and Authority Pin

- **Probe ID:** `P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-1`
- **Title:** Maurer–Cartan Gauge Curvature Factorization, Stencil-Width Growth, Exact Degree-3 and Degree-4 Off-Shell Commutator Closure, and Forced Scalar-Lapse Completion
- **Class:** `NON-CANONICAL`, `L1` (`NEW_DECLARED`)
- **Ownership Issue:** [`#1669`](https://github.com/mathorn1973/twist-j/issues/1669)
- **Predecessors:**
  - `P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1` (`#1650`, issue `#1649`)
  - `P-INTEGER-LOCAL-NOETHER-OBSTRUCTION-1` (`#1662`, issue `#1661`)
  - `P-INTEGER-LOCAL-AUXILIARY-NOETHER-1` (`#1664`, issue `#1663`)
  - `P-INTEGER-SCALAR-LAPSE-RIGIDITY-1` (`#1666`, issue `#1665`)
  - `P-INTEGER-FIXED-DURATION-BOUNDARY-1` (`#1668`)
- **Frozen Pre-Run Files:** `PREREG.md`, `PROOF.md`, `SOURCE.md`, `verify.py`, `breaker.py`, `FROZEN.sha256`

### Canonical Authority Inputs

| Path | Bytes | SHA-256 |
|---|---:|---|
| `canon/CANON.md` | `1052518` | `d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b` |
| `canon/CORE.md` | `30714` | `9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728` |
| `canon/FRONTIER.md` | `27382` | `8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0` |
| `canon/REGISTRY.tsv` | `532811` | `5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d` |
| `canon/CHANGELOG.md` | `207770` | `79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078` |

---

## 2. Scientific Question and Problem Statement

In `P-INTEGER-SCALAR-LAPSE-RIGIDITY-1` (`#1666`), the all-order scalar-lapse completion
$$M(s) = M_0 \exp(s K), \qquad F_s(q, Q) = \frac{1}{2}\bigl(q^\mathsf{T} A(s) q + Q^\mathsf{T} A(s) Q\bigr) - q^\mathsf{T} E(s) Q$$
of the six-component autonomous K1 metric-source carrier was established for $a = 0$, together with the all-order off-shell Ward identity for the raw gauge generator $(V_t(s) q)_n = \frac{t_n}{2}(p_n^- + p_n^+)$ and its degree-2 skew-adjusted modification
$$\tilde V_t^{\le 2}(s) q = V_t(s) q + A_t^{(1)}(s) \nabla_q S(q, s), \qquad [A_t^{(1)}(s)]_{n,n+1} = s_{n+1}\frac{t_n + t_{n+1}}{8} I_6.$$
Two fundamental questions remained open after `#1666` and `#1668`:

1. **Higher-Order Off-Shell Gauge Commutator Closure (`#1666` Section 6):**
   In `#1666`, the degree-2 skew adjustment $A_t^{(1)}(s)$ closed the off-shell commutator at degree 2 (`ADJUSTED2 = 0`), but left an explicit nonzero **degree-3 off-shell commutator witness** at slice $n = 1$:
   $$[\tilde\delta_t^{\le 2}, \tilde\delta_s^{\le 2}]^{(3)} x_1 = -\frac{1}{8} C u = \left(-\frac{395}{5184}, 0, \frac{395}{5184}, -\frac{1}{144}, \frac{1}{144}, -\frac{1}{5184}\right)^\mathsf{T}.$$
   What is the exact algebraic mechanism generating this degree-3 residual, why can no nearest-neighbor ($|m - n| \le 1$) skew operator cancel it, and how do higher-order multi-bond skew kernels $A_t^{(2)}(s), A_t^{(3)}(s)$ close the off-shell commutator through degree 3 and degree 4?

2. **Nonzero Source Forcing $a \in \{-1, 0, 1\}$ and Free-Lapse De-Freezing (`#1650`, `#1664`, `#1666`):**
   In `#1650`, the autonomous metric-source equations carry the constant source drive $f_* = (0, 0, 0, 0, 0, a/4)^\mathsf{T}$ with $a \in \{-1, 0, 1\}$ and equilibrium energy shift $E_* = \frac{4342005}{8683757}(a/4)^2$. In `#1666` (which restricted to $a = 0$), free-lapse variation $\partial S / \partial s_b = 0$ imposed $H_{\mathrm{bond}} = 0$, collapsing the positive-definite sector $\mathbf{1}_5^\perp \oplus \mathbb{Q}$ to a single static point. How does restoring $a \in \{-1, 0, 1\}$ extend the all-order scalar-lapse action and its commuting gauge algebra, and what does the free-lapse constraint $\partial S^{(a)} / \partial s_b = 0$ select when $a = \pm 1$?

---

## 3. Frozen Mathematical Definitions

### 3.1 Carrier Matrices and Scalar-Lapse Series

Let $L \in \mathbb{Q}^{5 \times 5}$ be the canonical K1 five-site circulant Laplacian with entries $L_{ii} = \frac{188}{324}$, $L_{ij} = -\frac{29}{324}$ for $|i - j| \equiv 1, 4 \pmod 5$, and $L_{ij} = -\frac{65}{324}$ for $|i - j| \equiv 2, 3 \pmod 5$. With $\ell = (1, -1, 0, 0, 0)^\mathsf{T}$ and $\gamma = \frac{1}{324}$, define on $\mathbb{Q}^6 = \mathbb{Q}^5 \oplus \mathbb{Q}$:
$$V = \begin{pmatrix} L & -\gamma \ell \\ -\gamma \ell^\mathsf{T} & 1 \end{pmatrix}, \qquad C = I_6 - \frac{1}{2} V, \qquad D = I_6 - C^2 = V\left(I_6 - \frac{1}{4} V\right),$$
$$K = \begin{pmatrix} 0 & I_6 \\ -D & 0 \end{pmatrix}, \qquad M_0 = \begin{pmatrix} C & I_6 \\ -D & C \end{pmatrix}, \qquad M(s) = M_0 \exp(s K) = \begin{pmatrix} U(s) & B(s) \\ -D B(s) & U(s) \end{pmatrix}.$$
The bond generating matrices $E(s) = B(s)^{-1} = \sum_{k \ge 0} s^k E_k$ and $A(s) = E(s) U(s) = \sum_{k \ge 0} s^k A_k$ have low-order Taylor coefficients:
$$E_0 = I_6, \quad E_1 = -C, \quad E_2 = \frac{1}{2}(I_6 + C^2), \quad E_3 = -\frac{1}{6}(2 C + C^3),$$
$$A_0 = C, \quad A_1 = -I_6, \quad A_2 = \frac{1}{2} C, \quad A_3 = -\frac{1}{6}(I_6 + 2 C^2).$$

### 3.2 Interior Hessian, Raw Gauge Operator, and Maurer–Cartan Curvature

On a finite horizon $T \ge 3$ with fixed endpoints $q_0, q_T \in \mathbb{Q}^6$, bond lapses $s = (s_1, \dots, s_T) \in \mathbb{Q}^T$, and Dirichlet gauge parameters $t = (t_0, t_1, \dots, t_T)$ with $t_0 = t_T = 0$, the homogeneous scalar-lapse action is
$$S(q, s) = \frac{1}{4}\bigl(q_0^\mathsf{T} V q_0 + q_T^\mathsf{T} V q_T\bigr) + \sum_{b=1}^T F_{s_b}(q_{b-1}, q_b).$$
Its interior Euler–Lagrange gradient $g(q, s) = \nabla_q S(q, s) = H(s) q$ on interior slices $n \in \{1, \dots, T-1\}$ has tridiagonal block operator $H(s) = \sum_{k \ge 0} H_k(s)$:
$$[H_k(s)]_{n,n} = (s_n^k + s_{n+1}^k) A_k, \qquad [H_k(s)]_{n,n-1} = -s_n^k E_k, \qquad [H_k(s)]_{n,n+1} = -s_{n+1}^k E_k.$$
The raw gauge generator $V_t(s) q = L_t(s) q$ with $L_t(s) = \sum_{k \ge 0} L_t^{(k)}(s)$ acts on interior slice $n \in \{1, \dots, T-1\}$ by
$$(L_t^{(k)}(s) q)_n = \frac{t_n}{2}\Bigl((s_n^k - s_{n+1}^k) A_k q_n - s_n^k E_k q_{n-1} + s_{n+1}^k E_k q_{n+1}\Bigr).$$
With directional parameter derivative $\partial_t := \sum_{b=1}^T (t_b - t_{b-1}) \frac{\partial}{\partial s_b}$, the Ward identity $\langle \nabla_q S, V_t(s) q \rangle + \partial_t S = 0$ holds to all orders and implies the exact matrix Ward identity
$$\partial_t H(s) = -H(s) L_t(s) - L_t(s)^\mathsf{T} H(s).$$
For any skew-symmetric interior operator series $A_t(s) = \sum_{m \ge 1} A_t^{(m)}(s)$ ($A_t^{(m)}(s)^\mathsf{T} = -A_t^{(m)}(s)$, homogeneous of degree $m$ in $s$ and linear in $t$), define the adjusted generator
$$\tilde\delta_t = \partial_t + \tilde V_t(s) \cdot \nabla_q, \qquad \tilde V_t(s) q = \tilde L_t(s) q := L_t(s) q + A_t(s) \nabla_q S(q, s) = \bigl(L_t(s) + A_t(s) H(s)\bigr) q.$$
Then $\tilde\delta_t S(q, s) = 0$ to all orders, $\tilde\delta_t(\nabla_q S) = -\tilde L_t(s)^\mathsf{T} \nabla_q S$, and the off-shell commutator factors to all orders through $\nabla_q S(q, s)$:
$$\boxed{[\tilde\delta_t, \tilde\delta_r] q = \mathcal{F}_{t,r}(s) \nabla_q S(q, s),}$$
where the skew-symmetric Maurer–Cartan curvature operator $\mathcal{F}_{t,r}(s) = \sum_{k \ge 0} \mathcal{F}_{t,r}^{(k)}(s)$ is given by
$$\boxed{\mathcal{F}_{t,r}(s) = \Omega_{t,r}(s) + \partial_t A_r(s) - \partial_r A_t(s) + \bigl(L_r(s) A_t(s) + A_t(s) L_r(s)^\mathsf{T}\bigr) - \bigl(L_t(s) A_r(s) + A_r(s) L_t(s)^\mathsf{T}\bigr) + A_r(s) H(s) A_t(s) - A_t(s) H(s) A_r(s),}$$
with raw curvature $[\Omega_{t,r}(s)]_{n,n+1} = -\frac{1}{4}(r_n t_{n+1} - t_n r_{n+1}) E(s_{n+1})$ and $[\Omega_{t,r}(s)]_{n,n-1} = -[\Omega_{t,r}(s)]_{n-1,n}^\mathsf{T}$.

### 3.3 Explicit Skew Kernels $A_t^{(1)}(s)$, $A_t^{(2)}(s)$, and $A_t^{(3)}(s)$

For $1 \le n < m \le T - 1$ (with $[A_t^{(d)}(s)]_{m,n} = -[A_t^{(d)}(s)]_{n,m}^\mathsf{T}$ and $[A_t^{(d)}(s)]_{n,n} = 0$):

1. **Degree-1 in $s$ (total generator degree 2, stencil width $|m - n| = 1$):**
   $$[A_t^{(1)}(s)]_{n,n+1} = \frac{t_n + t_{n+1}}{8} s_{n+1} I_6.$$

2. **Degree-2 in $s$ (total generator degree 3, stencil width $|m - n| \le 2$):**
   $$[A_t^{(2)}(s)]_{n,n+1} = -\frac{t_n + t_{n+1}}{16} s_{n+1}^2 C,$$
   $$[A_t^{(2)}(s)]_{n,n+2} = -\frac{s_{n+1}^2 t_{n+2} + 4 s_{n+1} s_{n+2} t_{n+1} + s_{n+2}^2 t_n}{32} I_6.$$

3. **Degree-3 in $s$ (total generator degree 4, stencil width $|m - n| \le 3$):**
   - For $m = n + 1$:
     $$[A_t^{(3)}(s)]_{n,n+1} = \frac{t_n + t_{n+1}}{48} s_{n+1}^3 C^2 + \bigl(W_{\mathrm{L}}^{(n)}(t, s) + W_{\mathrm{R}}^{(n)}(t, s)\bigr) I_6,$$
     where the bulk left wing (for $n \ge 2$) and left Dirichlet boundary wing (for $n = 1$) are
     $$W_{\mathrm{L}}^{(n)}(t, s) = \begin{cases}
     \dfrac{s_n\bigl(s_n^2(t_{n-1} - t_{n+1}) + 3 s_n s_{n+1}(t_{n-1} - 3 t_{n+1}) + 6 s_{n+1}^2 t_{n-1}\bigr)}{384}, & n \ge 2, \\[8pt]
     -\dfrac{s_1^2(s_1 + 3 s_2) t_2}{96} = W_{\mathrm{L}}^{\mathrm{bulk}}(0, t_1, t_2; s_1, s_2) - \dfrac{s_1^2(s_1 + s_2) t_2}{128}, & n = 1,
     \end{cases}$$
     and the right wing is the exact time-reversal $W_{\mathrm{R}}^{(n)}(t, s) = W_{\mathrm{L}}^{(T-1-n)}(t^{\mathrm{rev}}, s^{\mathrm{rev}})$:
     $$W_{\mathrm{R}}^{(n)}(t, s) = \begin{cases}
     \dfrac{s_{n+2}\bigl(s_{n+2}^2(t_{n+2} - t_n) + 3 s_{n+2} s_{n+1}(t_{n+2} - 3 t_n) + 6 s_{n+1}^2 t_{n+2}\bigr)}{384}, & n \le T - 3, \\[8pt]
     -\dfrac{s_T^2(s_T + 3 s_{T-1}) t_{T-2}}{96}, & n = T - 2.
     \end{cases}$$
   - For $m = n + 2$:
     $$[A_t^{(3)}(s)]_{n,n+2} = \frac{4 s_{n+1}^3 t_{n+2} + 3 s_{n+1}^2 s_{n+2}(5 t_{n+1} + 3 t_{n+2}) + 3 s_{n+1} s_{n+2}^2(3 t_n + 5 t_{n+1}) + 4 s_{n+2}^3 t_n}{384} C.$$
   - For $m = n + 3$:
     $$\begin{aligned}
     [A_t^{(3)}(s)]_{n,n+3} = \frac{1}{768}\Bigl(&4 s_{n+2}^3(t_{n+1} + t_{n+2}) + 12 s_{n+2}^2\bigl(s_{n+1}(t_{n+2} + t_{n+3}) + s_{n+3}(t_n + t_{n+1})\bigr) \\
     &+ 24 s_{n+1} s_{n+2} s_{n+3}(t_{n+1} + t_{n+2}) + 3 s_{n+1} s_{n+3}\bigl(s_{n+1}(3 t_{n+2} + t_{n+3}) + s_{n+3}(t_n + 3 t_{n+1})\bigr)\Bigr) I_6.
     \end{aligned}$$

### 3.4 Forced Affine Scalar-Lapse Action for $a \in \{-1, 0, 1\}$

For $a \in \{-1, 0, 1\}$ and forcing vector $f_* = (0, 0, 0, 0, 0, a/4)^\mathsf{T}$, let $x_* \in \mathbf{1}_5^\perp \oplus \mathbb{Q}$ be the unique static equilibrium solving $V x_* = f_*$:
$$\boxed{x_* = \frac{a}{17367514}\bigl(20493, -20493, 2916, 0, -2916, 4342005\bigr)^\mathsf{T}, \qquad E_* := \frac{1}{2} f_*^\mathsf{T} x_* = \frac{4342005}{8683757}\left(\frac{a}{4}\right)^2.}$$
With $\tilde q_n := q_n - x_*$, define the forced scalar-lapse action:
$$\boxed{S^{(a)}(q, s) := \frac{1}{4}\bigl(\tilde q_0^\mathsf{T} V \tilde q_0 + \tilde q_T^\mathsf{T} V \tilde q_T\bigr) + \sum_{b=1}^T \Bigl(F_{s_b}(\tilde q_{b-1}, \tilde q_b) + (1 + s_b) E_*\Bigr) - \frac{a}{8}(\chi_0 + \chi_T) + \frac{1}{2} E_*.}$$
At $s = 0$, completing the square gives $F_0(\tilde q_{b-1}, \tilde q_b) + E_* = F_0(q_{b-1}, q_b) + \frac{a}{8}(\chi_{b-1} + \chi_b)$, so $S^{(a)}(q, 0)$ reduces identically to the forced autonomous action of `#1650` (with interior Euler–Lagrange residual $(\Delta_c^2 + V) q_n - f_*$).
The affine gauge generator $\tilde\delta_t^{(a)} q = \tilde L_t(s)(q - x_*)$, $\tilde\delta_t^{(a)} s_b = t_b - t_{b-1}$ satisfies $\tilde\delta_t^{(a)} S^{(a)}(q, s) = 0$ to all orders and $[\tilde\delta_t^{(a),\le 4}, \tilde\delta_r^{(a),\le 4}]_{\le 4} = 0$ identically off-shell.
On stationary trajectories $\tilde z(\tau) = M_0 \exp(\tau K) \tilde z_0$, the free-lapse variation is
$$\frac{\partial S^{(a)}}{\partial s_b} = -H_{\mathrm{bond}}(\tilde z_0) + E_* = 0 \iff \boxed{\frac{1}{2}\|\tilde p_0\|^2 + \frac{1}{2}(q_0 - x_*)^\mathsf{T} D (q_0 - x_*) = E_* = \frac{4342005}{8683757}\left(\frac{a}{4}\right)^2.}$$
Because $D x_* = (V - \frac{1}{4} V^2) x_* = f_* - \frac{1}{4} V f_*$, the cold-start bond energy at $(q_0, \tilde p_0) = (0, 0)$ is
$$E_{\mathrm{cold}} := \frac{1}{2} x_*^\mathsf{T} D x_* = E_* - \frac{1}{8}\|f_*\|^2 = \frac{26052283}{69470056}\left(\frac{a}{4}\right)^2,$$
and the canonical vacuum cold-start trajectory $q_{-1} = q_0 = 0$ of `#1650`, which has $q_0 = 0$ and $\tilde p_0 = \frac{1}{2} f_* = (0, 0, 0, 0, 0, a/8)^\mathsf{T}$, satisfies $H_{\mathrm{bond}}(-x_*, \frac{1}{2} f_*) = E_{\mathrm{cold}} + \frac{1}{8}\|f_*\|^2 = E_*$ identically, lying on the free-lapse stationary constraint surface for all $a \in \{-1, 0, 1\}$.

---

## 4. Acceptance Gates and Certificate Specification

Both `verify.py` and `breaker.py` must verify all five canonical authority files, execute all positive checks and all eight negative controls `NC01`–`NC08`, and emit the exact ASCII certificate:

```text
CERTIFICATE=P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-1
AUTHORITY_FILES=5
SERIES_ORDER=4
MAURER_CARTAN_CASES=12
DEGREE2_BRACKET_CASES=12
DEGREE3_BRACKET_CASES=12
DEGREE4_BRACKET_CASES=12
BIANCHI_COCYCLE_ENTRIES=20
FORCED_WARD_CASES=18
COLD_START_SLICES=18
EQUILIBRIUM_ENERGY_RATIO=4342005/8683757
COLD_START_METRIC_DIFF=1/648,-1/648,0,0,0
PAYLOAD_SHA256=<64-hex-digest>
NEGATIVE_CONTROLS=8
CERTIFICATE_RESULT=PASS
```

`verify.py` additionally runs `breaker.py` in a subprocess, compares raw stdout bytes, and appends:

```text
BREAKER_RAW_BYTES=IDENTICAL
RESULT=PASS
```
