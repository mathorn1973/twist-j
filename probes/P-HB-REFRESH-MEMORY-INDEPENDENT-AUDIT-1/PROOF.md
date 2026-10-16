# Independent Mathematical Proof: Two-Contact Wave-Summary Memory Ranks and Refresh Laws on the 705-Site $D_3$ Carrier

**PUBLIC / NON-CANONICAL / L1 — `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` ([#1528](https://github.com/mathorn1973/twist-j/issues/1528))**

- **Author:** A. M. Thorn `<thorn@twistj.com>`, Apache-2.0
- **Owner Session:** `Antigravity-20261017-v103-hb-refresh-memory-audit`
- **Primary Subject Audited:** `notes/C-HB-REFRESH-MEMORY-BOUNDARY-N` ([#1525](https://github.com/mathorn1973/twist-j/issues/1525))
- **Action Layer:** `L1` (conditional exact finite rational linear-algebraic and dynamical audit on the fixed $705$-site carrier $D$)

---

## 1. Carrier, Operators, and Linear-Algebraic Preliminaries

### 1.1 Finite Dirichlet Carrier $D$ and Stencil Operators $L_D, H$

Let $\Lambda = \{x = (x_1, x_2, x_3) \in \mathbb{Z}^3 : x_1 + x_2 + x_3 \equiv 0 \pmod 2\}$ be the even-sum $D_3$ lattice. The five-site source support is
$$Y = (y_0, y_1, y_2, y_3, y_4) = \bigl((0,0,0),\; (1,1,0),\; (1,0,1),\; (0,1,1),\; (2,0,0)\bigr) \subset \Lambda,$$
where $Y_p = (y_0, y_1, y_2, y_3)$ are the four port sites and $y_4 = (2,0,0)$ is the fifth source site.

The isotropic five-shell stencil $B \subset \Lambda \setminus \{0\}$ consists of all displacements $d \in \Lambda$ with $\|d\|^2 = d_1^2 + d_2^2 + d_3^2 \in \{2, 4, 8, 10, 16\}$ and shell weights
$$w(d) = \frac{\tilde{w}(\|d\|^2)}{324}, \qquad \bigl(\tilde{w}(2), \tilde{w}(4), \tilde{w}(8), \tilde{w}(10), \tilde{w}(16)\bigr) = (6, 1, 15, 1, 1).$$
The shell multiplicities in $\Lambda$ are $(12, 6, 12, 24, 6)$, giving $|B| = 60$, $|B_0| = 61$ for $B_0 = \{0\} \cup B$, and total stencil weight
$$\sum_{d \in B} w(d) = \frac{12 \cdot 6 + 6 \cdot 1 + 12 \cdot 15 + 24 \cdot 1 + 6 \cdot 1}{324} = \frac{288}{324} = \frac{8}{9}.$$

The principal two-step finite domain is
$$D = Y + B_0 + B_0 = \{y + d_1 + d_2 : y \in Y,\; d_1, d_2 \in B_0\} \subset \Lambda,$$
ordered lexicographically on $\mathbb{Z}^3$, with $|D| = 705$.

On $\mathbb{Q}^D$, the full-diagonal Dirichlet Laplacian $L_D$ and wave propagation operator $H = 2I - L_D$ act on $u \in \mathbb{Q}^D$ at $x \in D$ by
$$(L_D u)_x = \frac{8}{9} u_x - \sum_{\substack{d \in B \\ x + d \in D}} w(d)\, u_{x+d}, \qquad (H u)_x = \frac{10}{9} u_x + \sum_{\substack{d \in B \\ x + d \in D}} w(d)\, u_{x+d}.$$
Since $B = -B$ and $w(-d) = w(d)$, both $L_D$ and $H$ are symmetric ($L_D^T = L_D$, $H^T = H$).

### 1.2 Port Insertion, Projectors, and Native Two-Column Source Matrix

Let $\delta_x \in \mathbb{Q}^D$ denote the standard unit vector at $x \in D$. Define:
- Port insertion $P = [\delta_{y_0}\ \delta_{y_1}\ \delta_{y_2}\ \delta_{y_3}] \in \mathbb{Q}^{D \times 4}$, satisfying $P^T P = I_4$.
- Port projector $Q_p = P P^T$, port-complement projector $J_0 = I - Q_p$, and port damping operator
  $$K = (I + Q_p)^{-1} = I - \frac{1}{2} Q_p.$$
- Fifth-site unit vector $e_4 = \delta_{y_4} \in \mathbb{Q}^D$. Because $y_4 = (2,0,0) \notin Y_p$, we have
  $$P^T e_4 = 0, \qquad Q_p e_4 = 0, \qquad J_0 e_4 = e_4, \qquad K e_4 = e_4.$$
- Five-site zero-sum source columns $s_i = \delta_{y_i} - \frac{1}{5}\sum_{j=0}^4 \delta_{y_j} \in \mathbb{Q}^D$ for $i \in \{0, 1, 2, 3\}$, with $S = [s_0\ s_1\ s_2\ s_3] \in \mathbb{Q}^{D \times 4}$ and two active native-source columns
  $$A = [s_0\ s_1] \in \mathbb{Q}^{D \times 2}.$$
- Using the balanced lift $\ell(0, 1, 2, 3, 4) = (0, 1, 2, -2, -1)$, each native receiver pair $(q, r) \in \mathbb{F}_5^2$ defines
  $$\eta_2(q, r) = \begin{pmatrix} \ell(q)/2 \\ (\ell(r) + 1)/2 \end{pmatrix} \in \mathbb{Q}^2, \qquad \eta(q, r) = \begin{pmatrix} \eta_2(q, r) \\ 0 \\ 0 \end{pmatrix} \in \mathbb{Q}^4,$$
  and the injected wave source vector is $a(q, r) = S \eta(q, r) = A \eta_2(q, r) \in \mathbb{Q}^D$.
- The source Gram matrix $G = A^T A \in \mathbb{Q}^{2 \times 2}$, port-overlap matrix $M = A^T P \in \mathbb{Q}^{2 \times 4}$, and fifth-site port-stencil row $h^T = e_4^T H P \in \mathbb{Q}^{1 \times 4}$ are:
  $$G = \frac{1}{5}\begin{pmatrix} 4 & -1 \\ -1 & 4 \end{pmatrix}, \qquad M = \frac{1}{5}\begin{pmatrix} 4 & -1 & -1 & -1 \\ -1 & 4 & -1 & -1 \end{pmatrix}, \qquad h^T = \frac{1}{324}(1,\; 6,\; 6,\; 0) = \left(\frac{1}{324},\; \frac{1}{54},\; \frac{1}{54},\; 0\right),$$
  since $\|y_4 - y_0\|^2 = \|(2,0,0)\|^2 = 4$ ($\tilde{w}(4) = 1$), $\|y_4 - y_1\|^2 = \|(1,-1,0)\|^2 = 2$ ($\tilde{w}(2) = 6$), $\|y_4 - y_2\|^2 = \|(1,0,-1)\|^2 = 2$ ($\tilde{w}(2) = 6$), and $\|y_4 - y_3\|^2 = \|(2,-1,-1)\|^2 = 6 \notin \{2,4,8,10,16\}$ ($\tilde{w}(6) = 0$).

### 1.3 Key Projector Identities on $A$, $J_0$, and $K$

**Lemma 1 (Port-Complement Collapse of $A$).** Let $\mathbf{1}_2 = (1, 1)^T \in \mathbb{Q}^2$. Then:
$$J_0 A = -\frac{1}{5} e_4 \mathbf{1}_2^T, \qquad A^T J_0 = -\frac{1}{5} \mathbf{1}_2 e_4^T,$$
$$K - \frac{1}{2} I = \frac{1}{2} J_0, \qquad K J_0 = J_0, \qquad K P = \frac{1}{2} P.$$

*Proof.* For each $i \in \{0, 1\}$, $s_i = \delta_{y_i} - \frac{1}{5}\sum_{j=0}^3 \delta_{y_j} - \frac{1}{5} e_4$. Since $J_0 = I - Q_p$ annihilates $\delta_{y_0}, \delta_{y_1}, \delta_{y_2}, \delta_{y_3}$ and fixes $e_4 = \delta_{y_4}$, we have $J_0 s_i = -\frac{1}{5} e_4$, giving $J_0 A = -\frac{1}{5} e_4 \mathbf{1}_2^T$ and, by symmetry of $J_0$, $A^T J_0 = -\frac{1}{5} \mathbf{1}_2 e_4^T$. Next, from $K = I - \frac{1}{2} Q_p$ and $J_0 = I - Q_p$:
$$K - \frac{1}{2} I = \frac{1}{2}(I - Q_p) = \frac{1}{2} J_0, \qquad K J_0 = \left(I - \frac{1}{2} Q_p\right)(I - Q_p) = I - Q_p = J_0,$$
and $K P = (I - \frac{1}{2} P P^T) P = P - \frac{1}{2} P = \frac{1}{2} P$. $\blacksquare$

---

## 2. Target 1: Exact Refresh Identities Across $F$ and $F^2$

### 2.1 Wave/Tape Map $F$ and Linear Wave Functionals $(\rho, \gamma, \delta)$

The full linear wave/tape carrier is
$$X = (u, v, a_0, a_1, b_0, b_1) \in \mathbb{Q}^D \times \mathbb{Q}^D \times (\mathbb{Q}^4)^4 \cong \mathbb{Q}^{1426}.$$
One step of the coupled wave/tape evolution $F : \mathbb{Q}^{1426} \to \mathbb{Q}^{1426}$ is
$$F(u, v, a_0, a_1, b_0, b_1) = (v, w, a_1, b_1, b_{\mathrm{out}}, b_0),$$
where
$$w = K(H v - J_0 u + 4 P a_0), \qquad b_{\mathrm{out}} = a_0 - \frac{1}{2} P^T(w - u).$$
Define the three wave-only linear functionals on $(u, v) \in \mathbb{Q}^D \times \mathbb{Q}^D$:
$$\rho(u, v) = A^T\left(v - \frac{1}{2} H u\right) \in \mathbb{Q}^2,$$
$$\gamma(u, v) = \frac{1}{5}\left(e_4^T u - \frac{1}{2} e_4^T H v\right) \in \mathbb{Q},$$
$$\delta(u, v) = \frac{1}{5}\left(e_4^T v - \frac{1}{2} e_4^T H K H v + \frac{1}{2} e_4^T H J_0 u\right) \in \mathbb{Q}.$$

### 2.2 Algebraic Proof of the Three Refresh Identities

**Theorem 1 (Exact Refresh Identities on $\mathbb{Q}^{1426}$).** For every full state $X = (u, v, a_0, a_1, b_0, b_1) \in \mathbb{Q}^{1426}$,
$$\begin{aligned}
\rho(FX) &= \gamma(X)\mathbf{1}_2 + 2 M a_0, \\
\gamma(FX) &= \delta(X) - \frac{1}{5} h^T a_0, \\
\rho(F^2 X) &= \left(\delta(X) - \frac{1}{5} h^T a_0\right)\mathbf{1}_2 + 2 M a_1.
\end{aligned}$$

*Proof.*
1. **Identity for $\rho(FX)$:** Since $FX$ has wave pair $(u', v') = (v, w)$,
   $$\rho(FX) = A^T\left(w - \frac{1}{2} H v\right) = A^T\left(K H v - K J_0 u + 4 K P a_0 - \frac{1}{2} H v\right) = A^T\left(K - \frac{1}{2}I\right) H v - A^T K J_0 u + 4 A^T K P a_0.$$
   Applying Lemma 1 ($K - \frac{1}{2}I = \frac{1}{2}J_0$, $K J_0 = J_0$, $A^T J_0 = -\frac{1}{5}\mathbf{1}_2 e_4^T$, and $K P = \frac{1}{2}P$):
   $$\rho(FX) = -\frac{1}{10} \mathbf{1}_2 e_4^T H v + \frac{1}{5} \mathbf{1}_2 e_4^T u + 2 A^T P a_0 = \frac{1}{5}\left(e_4^T u - \frac{1}{2} e_4^T H v\right)\mathbf{1}_2 + 2 M a_0 = \gamma(X)\mathbf{1}_2 + 2 M a_0.$$

2. **Identity for $\gamma(FX)$:** Using $w = K H v - K J_0 u + 4 K P a_0 = K H v - J_0 u + 2 P a_0$,
   $$\begin{aligned}
   \gamma(FX) &= \frac{1}{5}\left(e_4^T v - \frac{1}{2} e_4^T H w\right) \\
   &= \frac{1}{5}\left(e_4^T v - \frac{1}{2} e_4^T H K H v + \frac{1}{2} e_4^T H J_0 u - e_4^T H P a_0\right) \\
   &= \delta(X) - \frac{1}{5} h^T a_0.
   \end{aligned}$$

3. **Identity for $\rho(F^2 X)$:** Applying the first identity to $Y = FX$, whose first incoming tape slot is $a_0(FX) = a_1(X)$, and substituting the second identity gives
   $$\rho(F^2 X) = \gamma(FX)\mathbf{1}_2 + 2 M a_0(FX) = \left(\delta(X) - \frac{1}{5} h^T a_0\right)\mathbf{1}_2 + 2 M a_1. \qquad \blacksquare$$

Because $\rho(FX) \in \mathbb{Q}^2$, $\gamma(FX) \in \mathbb{Q}$, and $\rho(F^2 X) \in \mathbb{Q}^2$ form $5$ linear functionals on $\mathbb{Q}^{1426}$, Theorem 1 is equivalent to $5 \times 1426 = 7130$ exact coefficient equalities on the standard basis of $\mathbb{Q}^{1426}$.

---

## 3. Target 2: Necessary and Sufficient Kernel Criteria and Exact Rank Minors

### 3.1 Expansion of Pre-Guard Contact Work

For any wave pair $(u, v) \in \mathbb{Q}^D \times \mathbb{Q}^D$, the quadratic Dirichlet wave energy is
$$E_D(u, v) = \frac{1}{2}\|v - u\|^2 + \frac{1}{2} u^T L_D v.$$
For any source vector $a = A \eta_2(q, r)$ and sign $\sigma \in \{-1, +1\}$, expanding $\Delta(u, v; q, r, \sigma) = E_D(u, v + \sigma a) - E_D(u, v)$ using $L_D^T = L_D$, $\sigma^2 = 1$, and $I - \frac{1}{2}L_D = \frac{1}{2}H$ yields
$$\begin{aligned}
\Delta(u, v; q, r, \sigma) &= \frac{1}{2}\left(\|v - u + \sigma a\|^2 - \|v - u\|^2\right) + \frac{1}{2}\sigma u^T L_D a \\
&= \frac{1}{2}\|a\|^2 + \sigma a^T\left(v - \left(I - \frac{1}{2}L_D\right)u\right) \\
&= \frac{1}{2}\eta_2(q, r)^T G \eta_2(q, r) + \sigma \eta_2(q, r)^T \rho(u, v).
\end{aligned}$$
In particular, among the $25$ native labels $(q, r) \in \mathbb{F}_5^2$, the pairs $(2, 4)$ and $(0, 1)$ give the standard basis of $\mathbb{Q}^2$:
$$\eta_2(2, 4) = \begin{pmatrix} \ell(2)/2 \\ (\ell(4)+1)/2 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad \eta_2(0, 1) = \begin{pmatrix} \ell(0)/2 \\ (\ell(1)+1)/2 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}.$$

### 3.2 Kernel Characterization for Fixed Linear Wave Summaries

Let $L : \mathbb{Q}^D \times \mathbb{Q}^D \to \mathbb{Q}^r$ be a fixed linear wave summary (with arbitrary, possibly nonlinear, readout decoders acting on $(L(u, v), a_0, a_1, b_0, b_1, q, r, \sigma, b, B)$).

**Theorem 2 (Kernel Characterization for Horizons $\{0, 2\}$ and $\{0, 1, 2\}$).**
1. Exact pre-guard contact work $\Delta(F^n X; q, r, \sigma)$ (and likewise the Boolean guard decision $\mathbf{1}\{0 \le b - \Delta(F^n X; q, r, \sigma) \le B\}$ across all admissible rational stores $0 \le b \le B$) at horizon $n \in \{0, 2\}$ is determined by $L(u, v)$ together with known tape and spectator inputs if and only if
   $$\ker L \subseteq \ker(\rho, \delta),$$
   which requires $\operatorname{rank}(L) \ge \operatorname{rank}(\rho, \delta) = 3$.
2. The same determination at horizon $n \in \{0, 1, 2\}$ holds if and only if
   $$\ker L \subseteq \ker(\rho, \gamma, \delta),$$
   which requires $\operatorname{rank}(L) \ge \operatorname{rank}(\rho, \gamma, \delta) = 4$.

*Proof.*
- **Sufficiency:** If $\ker L \subseteq \ker(\rho, \delta)$ (respectively $\ker(\rho, \gamma, \delta)$), then $(\rho, \delta)$ (respectively $(\rho, \gamma, \delta)$) factors linearly through $L(u, v)$. By Theorem 1, for any $X = (u, v, a_0, a_1, b_0, b_1)$,
  $$\rho(X) = \rho(u, v), \qquad \rho(FX) = \gamma(u, v)\mathbf{1}_2 + 2 M a_0, \qquad \rho(F^2 X) = \left(\delta(u, v) - \frac{1}{5}h^T a_0\right)\mathbf{1}_2 + 2 M a_1.$$
  Hence $\rho(F^n X)$ and $\Delta(F^n X; q, r, \sigma) = \frac{1}{2}\eta_2(q, r)^T G \eta_2(q, r) + \sigma \eta_2(q, r)^T \rho(F^n X)$ (and thus $0 \le b - \Delta \le B$) are uniquely determined at $n \in \{0, 2\}$ from $(\rho, \delta)$ and at $n \in \{0, 1, 2\}$ from $(\rho, \gamma, \delta)$.
- **Necessity (for exact pre-guard work and for Boolean guard decisions):** Suppose $(u, v) - (u', v') = (\tilde{u}, \tilde{v}) \in \ker L$, so $L(u, v) = L(u', v')$. Fix zero tapes $a_0 = a_1 = b_0 = b_1 = 0$.
  - If $(\tilde{u}, \tilde{v}) \notin \ker \rho$, then $\rho_i(u, v) \ne \rho_i(u', v')$ for some $i \in \{0, 1\}$. Choosing the corresponding basis label $(q, r) \in \{(2, 4), (0, 1)\}$ (where $\eta_2(q, r) = e_i$), we have $\Delta(X; q, r, +1) - \Delta(X'; q, r, +1) = \rho_i(u, v) - \rho_i(u', v') \ne 0$ at $n = 0$.
  - If $(\tilde{u}, \tilde{v}) \notin \ker \gamma$, then by Theorem 1 at $a_0 = 0$, $\rho_0(FX) - \rho_0(FX') = \gamma(u, v) - \gamma(u', v') \ne 0$, so $\Delta(FX; (2, 4), +1) \ne \Delta(FX'; (2, 4), +1)$ at $n = 1$.
  - If $(\tilde{u}, \tilde{v}) \notin \ker \delta$, then by Theorem 1 at $a_0 = a_1 = 0$, $\rho_0(F^2 X) - \rho_0(F^2 X') = \delta(u, v) - \delta(u', v') \ne 0$, so $\Delta(F^2 X; (2, 4), +1) \ne \Delta(F^2 X'; (2, 4), +1)$ at $n = 2$.
  This immediately proves necessity for exact pre-guard work queries. Moreover, whenever $\rho_i(F^n X) \ne \rho_i(F^n X')$ for $(q, r) \in \{(2, 4), (0, 1)\}$, we have $\frac{1}{2}\eta_2^T G \eta_2 = \frac{2}{5} > 0$, so $\Delta(F^n X; q, r, +1) + \Delta(F^n X; q, r, -1) = \frac{4}{5} > 0$. Choosing $\sigma \in \{-1, +1\}$ so that the larger of $\Delta_+ = \Delta(F^n X; q, r, \sigma)$ and $\Delta_- = \Delta(F^n X'; q, r, \sigma)$ is strictly positive ($\max(\Delta_+, \Delta_-) \ge \frac{2}{5} > 0$) and relabeling if needed so that $\Delta_1 < \Delta_2$ with $\Delta_2 > 0$:
  - If $\Delta_1 \ge 0$, set $b = B = \Delta_1 \ge 0$ ($0 \le b \le B$). Then $b - \Delta_1 = 0 \in [0, B]$ (accepted), whereas $b - \Delta_2 = \Delta_1 - \Delta_2 < 0$ (lower refusal).
  - If $\Delta_1 < 0 < \Delta_2$, set $b = B = \Delta_2 > 0$ ($0 \le b \le B$). Then $b - \Delta_2 = 0 \in [0, B]$ (accepted), whereas $b - \Delta_1 = B - \Delta_1 > B$ (upper refusal).
  Hence even Boolean guard-only decoders fail whenever $\ker L$ is not contained in $\ker(\rho, \delta)$ for $n \in \{0, 2\}$ or $\ker(\rho, \gamma, \delta)$ for $n \in \{0, 1, 2\}$. $\blacksquare$

### 3.3 Exact $3 \times 3$ and $4 \times 4$ Rank Certificates

Let $z_{\mathrm{near}} = (6, 0, 0) = y_4 + (4, 0, 0) \in D$ and $z_{\mathrm{far}} = (10, 0, 0) = y_4 + (4, 0, 0) + (4, 0, 0) \in D$.

**Proposition 1 (Exact Rank Minors).**
1. On the three pure-velocity columns $C_3 = \bigl((0, s_0),\; (0, s_1),\; (0, \delta_{(10,0,0)})\bigr)$, the $3 \times 3$ matrix of $(\rho_0, \rho_1, \delta)$ is block lower-triangular:
   $$M_3 = \begin{pmatrix} 4/5 & -1/5 & 0 \\ -1/5 & 4/5 & 0 \\ \kappa_0 & \kappa_1 & -\frac{1}{10 \cdot 324^2} \end{pmatrix}, \qquad \det(M_3) = \frac{3}{5}\left(-\frac{1}{10 \cdot 324^2}\right) = -\frac{3}{5248800} = -\frac{1}{1749600} \ne 0.$$
   Since $(\rho, \delta)$ has $3$ rows, $\operatorname{rank}(\rho, \delta) = 3$.
2. Inserting $(0, \delta_{(6,0,0)})$ as the third column before $(0, \delta_{(10,0,0)})$, the $4 \times 4$ matrix of $(\rho_0, \rho_1, \gamma, \delta)$ on $C_4 = \bigl((0, s_0),\; (0, s_1),\; (0, \delta_{(6,0,0)}),\; (0, \delta_{(10,0,0)})\bigr)$ is block lower-triangular:
   $$M_4 = \begin{pmatrix} 4/5 & -1/5 & 0 & 0 \\ -1/5 & 4/5 & 0 & 0 \\ \gamma(0, s_0) & \gamma(0, s_1) & -\frac{1}{10 \cdot 324} & 0 \\ \kappa_0 & \kappa_1 & \delta(0, \delta_{(6,0,0)}) & -\frac{1}{10 \cdot 324^2} \end{pmatrix},$$
   with determinant
   $$\det(M_4) = \frac{3}{5}\left(-\frac{1}{10 \cdot 324}\right)\left(-\frac{1}{10 \cdot 324^2}\right) = \frac{3}{1698693120000} = \frac{1}{566231040000} \ne 0.$$
   Since $(\rho, \gamma, \delta)$ has $4$ rows, $\operatorname{rank}(\rho, \gamma, \delta) = 4$.

*Proof.* Because $z_{\mathrm{near}} = (6, 0, 0) \notin Y$ and $z_{\mathrm{far}} = (10, 0, 0) \notin Y$, $\rho(0, \delta_{(6,0,0)}) = A^T \delta_{(6,0,0)} = (0, 0)^T$ and $\rho(0, \delta_{(10,0,0)}) = A^T \delta_{(10,0,0)} = (0, 0)^T$, while $\rho(0, [s_0\ s_1]) = A^T A = G$ has $\det(G) = \frac{16 - 1}{25} = \frac{3}{5}$.

Next, $y_4 = (2, 0, 0)$, so $z_{\mathrm{near}} - y_4 = (4, 0, 0) \in B$ has squared norm $16$ and stencil weight $w(4, 0, 0) = \frac{1}{324}$, whereas $z_{\mathrm{far}} - y_4 = (8, 0, 0) \notin B_0$ has squared norm $64 > 16$, giving $H_{y_4, z_{\mathrm{near}}} = \frac{1}{324}$ and $H_{y_4, z_{\mathrm{far}}} = 0$. Therefore:
$$\gamma(0, \delta_{(6,0,0)}) = -\frac{1}{10} e_4^T H \delta_{(6,0,0)} = -\frac{1}{10 \cdot 324} = -\frac{1}{3240}, \qquad \gamma(0, \delta_{(10,0,0)}) = -\frac{1}{10} e_4^T H \delta_{(10,0,0)} = 0.$$

Finally, for $\delta(0, \delta_{(10,0,0)}) = -\frac{1}{10} e_4^T H K H \delta_{(10,0,0)}$, any two-step stencil path $y_4 \xrightarrow{+d_1} x \xrightarrow{+d_2} z_{\mathrm{far}}$ satisfies $d_1 + d_2 = (8, 0, 0)$ with $d_1, d_2 \in B_0$. Since every $d \in B_0$ has $\|d\|^2 \le 16$, its first coordinate satisfies $|d_x| \le 4$, with $d_x = 4$ if and only if $d = (4, 0, 0)$. Hence $d_1 = d_2 = (4, 0, 0)$ is the unique two-step path, with intermediate site $x = (6, 0, 0) \in D \setminus Y_p$ where $K_{x,x} = 1$. Thus
$$e_4^T H K H \delta_{(10,0,0)} = H_{(2,0,0),(6,0,0)} K_{(6,0,0),(6,0,0)} H_{(6,0,0),(10,0,0)} = \frac{1}{324} \cdot 1 \cdot \frac{1}{324} = \frac{1}{324^2},$$
and $\delta(0, \delta_{(10,0,0)}) = -\frac{1}{10 \cdot 324^2} = -\frac{1}{1049760}$. Taking the product of the diagonal blocks yields $\det(M_3)$ and $\det(M_4)$. $\blacksquare$

---

## 4. Target 3: Equal-Energy, Equal-Tape Opposite-Velocity Counterexample

**Proposition 2 (Counterexample to $(\rho, \gamma)$ Two-Step Closure).** Define the opposite-velocity full states
$$X_\pm = \bigl(u = 0,\; v = \pm \delta_{(10,0,0)},\; a_0 = 0,\; a_1 = 0,\; b_0 = 0,\; b_1 = 0\bigr) \in \mathbb{Q}^{1426}.$$
Then:
1. At $n = 0$: $\rho(X_\pm) = (0, 0)^T$, $\gamma(X_\pm) = 0$, $E_{\mathrm{full}}(X_\pm) = \frac{1}{2}$, and $\delta(X_\pm) = \mp \frac{1}{1049760}$.
2. At $n = 1$ ($F X_\pm$) and $n = 2$ ($F^2 X_\pm$): all four tape slots $(a_0, a_1, b_0, b_1)$ remain identically zero and $E_{\mathrm{full}}(F^n X_\pm) = \frac{1}{2}$ for $n \in \{0, 1, 2\}$, while
   $$\rho(F X_\pm) = \begin{pmatrix} 0 \\ 0 \end{pmatrix}, \qquad \rho(F^2 X_\pm) = \mp \frac{1}{1049760}\begin{pmatrix} 1 \\ 1 \end{pmatrix}.$$
3. Under a second contact at $n = 2$ with source $a = A(1, 0)^T = s_0$ (native label $(q, r) = (2, 4)$), sign $\sigma = +1$, capacity $B = 1$, and store $b = \frac{1}{2}$, both states are accepted ($0 \le b - \Delta \le B$) with distinct exact work and post-contact stores:
   $$\Delta(F^2 X_+) = \frac{2}{5} - \frac{1}{1049760} = \frac{419903}{1049760}, \qquad \Delta(F^2 X_-) = \frac{2}{5} + \frac{1}{1049760} = \frac{419905}{1049760},$$
   $$b - \Delta(F^2 X_+) = \frac{104977}{1049760} \ne \frac{104975}{1049760} = b - \Delta(F^2 X_-).$$

*Proof.* Part 1 follows from Proposition 1 and $E_D(0, \pm \delta_{(10,0,0)}) = \frac{1}{2}\|\pm \delta_{(10,0,0)}\|^2 = \frac{1}{2}$. For Part 2, every $d \in B_0$ satisfies $|d_x| \le 4$. Thus $\operatorname{supp}(v_0) = \{(10, 0, 0)\}$ has $x = 10$; after one step, $\operatorname{supp}(w_0) = \operatorname{supp}(H v_0)$ has $x \ge 6$; after two steps, $\operatorname{supp}(w_1) = \operatorname{supp}(K(H w_0 - J_0 v_0))$ has $x \ge 2$. Since all four ports $y_0, y_1, y_2, y_3 \in Y_p$ have $x \in \{0, 1\}$, the vectors $u_0, w_0, w_1$ vanish on $Y_p$, so $P^T(w_0 - u_0) = 0$ and $P^T(w_1 - u_1) = 0$. Hence all four tape slots remain zero through $n = 0, 1, 2$, and $E_{\mathrm{full}}$ is conserved at $\frac{1}{2}$. Theorem 1 gives $\rho(F X_\pm) = 0$ and $\rho(F^2 X_\pm) = \delta(X_\pm)\mathbf{1}_2 = \mp \frac{1}{1049760}\mathbf{1}_2$. Part 3 follows immediately from $\Delta = \frac{1}{2}G_{00} + (1, 0)\rho(F^2 X_\pm) = \frac{2}{5} \mp \frac{1}{1049760}$ and $0 < \frac{419903}{1049760} < \frac{419905}{1049760} < \frac{1}{2} < 1$. $\blacksquare$

---

## 5. Target 4: Finite Two-Contact Predictor $\xi = (\rho, \delta)$ and Exact Update Row $\kappa^T$

### 5.1 Contact Update of $\xi = (\rho, \delta)$ and Exact Computation of $\kappa^T$

**Theorem 3 (Two-Contact Reduced Predictor $\xi = (\rho, \delta)$).** Let $\xi(u, v) = (\rho(u, v), \delta(u, v)) \in \mathbb{Q}^2 \times \mathbb{Q}$.
1. Under a first contact with native label $(q_1, r_1) \in \mathbb{F}_5^2$, $\eta^{(1)} = \eta_2(q_1, r_1)$, sign $\sigma_1 \in \{-1, +1\}$, store $b$, and capacity $B$:
   - The pre-guard work is $\Delta_1 = \frac{1}{2}(\eta^{(1)})^T G \eta^{(1)} + \sigma_1 (\eta^{(1)})^T \rho(u, v)$.
   - Setting $\tilde{\sigma}_1 = \sigma_1$ if $0 \le b - \Delta_1 \le B$ and $\tilde{\sigma}_1 = 0$ otherwise, the post-contact wave $(u^+, v^+) = (u, v + \tilde{\sigma}_1 A \eta^{(1)})$ has summary
     $$\rho(u^+, v^+) = \rho(u, v) + \tilde{\sigma}_1 G \eta^{(1)}, \qquad \delta(u^+, v^+) = \delta(u, v) + \tilde{\sigma}_1 \kappa^T \eta^{(1)},$$
     where
     $$\kappa^T = \frac{1}{5} e_4^T\left(A - \frac{1}{2} H K H A\right) = \left(-\frac{145483}{10497600},\; -\frac{173653}{10497600}\right) \in \mathbb{Q}^{1 \times 2}.$$
2. After two free/tape-coupled steps $F^2(u^+, v^+, a_0, a_1, b_0, b_1)$, the wave functional $\rho_2 = \rho(F^2 X^+)$ is given solely in terms of $(\delta(u, v), a_0, a_1)$ and the first contact by
   $$\rho_2 = \left(\delta(u, v) + \tilde{\sigma}_1 \kappa^T \eta^{(1)} - \frac{1}{5} h^T a_0\right)\mathbf{1}_2 + 2 M a_1,$$
   and for any second contact $(q_2, r_2) \in \mathbb{F}_5^2$, $\eta^{(2)} = \eta_2(q_2, r_2)$, sign $\sigma_2 \in \{-1, +1\}$, the exact second pre-guard work $\Delta_2 = \frac{1}{2}(\eta^{(2)})^T G \eta^{(2)} + \sigma_2 (\eta^{(2)})^T \rho_2$, second guard decision $0 \le b_1 - \Delta_2 \le B$, updated work $W$, updated store $b$, updated signs, and post-second-contact $\rho_2^+ = \rho_2 + \tilde{\sigma}_2 G \eta^{(2)}$ agree identically with the full $1426$-coordinate wave/tape evolution.

*Proof.* By linearity of $\rho(u, v) = A^T(v - \frac{1}{2}H u)$ and $\delta(u, v) = \frac{1}{5}(e_4^T v - \frac{1}{2}e_4^T H K H v + \frac{1}{2}e_4^T H J_0 u)$ in $v$, shifting $v \mapsto v + \tilde{\sigma}_1 A \eta^{(1)}$ at fixed $u$ shifts $\rho$ by $\tilde{\sigma}_1 A^T A \eta^{(1)} = \tilde{\sigma}_1 G \eta^{(1)}$ and shifts $\delta$ by
$$\delta(0, \tilde{\sigma}_1 A \eta^{(1)}) = \tilde{\sigma}_1 \cdot \frac{1}{5} e_4^T\left(A - \frac{1}{2} H K H A\right)\eta^{(1)} = \tilde{\sigma}_1 \kappa^T \eta^{(1)}.$$
Evaluating $\kappa_j = \frac{1}{5}e_4^T(s_j - \frac{1}{2} H K H s_j)$ for $j \in \{0, 1\}$ directly from the integer stencil (and matching the first two columns of the blank-wave two-step work matrix $\Omega_{i,j} = \delta(0, s_j) = -\mu_j / 10497600$ established in `probes/P-FUNDED-TWO-USE-INDEPENDENT-AUDIT-2/PROOF.md`) gives
$$\kappa_0 = -\frac{145483}{10497600}, \qquad \kappa_1 = -\frac{173653}{10497600}.$$
Applying Theorem 1 to $X^+ = (u^+, v^+, a_0, a_1, b_0, b_1)$ yields $\rho_2 = (\delta(u^+, v^+) - \frac{1}{5}h^T a_0)\mathbf{1}_2 + 2 M a_1$, from which the second contact work $\Delta_2$ and guard decision follow by Section 3.1. $\blacksquare$
