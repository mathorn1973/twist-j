# P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-2: Independent Mathematical Proof

- **Status:** PUBLIC / NON-CANONICAL / L1 / Independent proof and audit under [#1534](https://github.com/mathorn1973/twist-j/issues/1534) (successor to abandoned pin `P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-1`)
- **Owner:** `Antigravity-20261015-nonlinear-receiver-independent-audit-1`
- **Author:** A. M. Thorn `<thorn@twistj.com>`
- **License:** Apache-2.0

---

## 1. Native Update $U$, Affine Coordinate Bijection $\Psi_{\mathrm{aff}}$, and Generator Actions

Let $x = (a, b, c, d, q, r) \in \mathbb{F}_5^6$ with trace $z(x) = a + b + c + d + q + r \bmod 5$.
For $n \in \mathbb{N}_0$, let $\theta_n = \operatorname{popcount}(n) \bmod 2 \in \{0, 1\}$. The unchanged autonomous update on $\Omega = \mathbb{N}_0 \times \mathbb{F}_5^6$ is
$$U(n, x) = \bigl(n + 1,\; T_{\theta_n}(x)\bigr), \qquad T_\theta(x) = g_{(z(x) + 2\theta) \bmod 5}(x),$$
where the five generators $g_0, g_1, g_2, g_3, g_4 : \mathbb{F}_5^6 \to \mathbb{F}_5^6$ are:
$$\begin{aligned}
g_0(a, b, c, d, q, r) &= (b,\; a,\; d,\; c,\; q,\; r), \\
g_1(a, b, c, d, q, r) &= (-c,\; -d,\; -a,\; -b,\; -q,\; -r), \\
g_2(a, b, c, d, q, r) &= (2-c,\; 1-d+r,\; 2-a,\; 1-b-r,\; 1-q,\; -r), \\
g_3(a, b, c, d, q, r) &= (2-a,\; 1-b,\; 3-c,\; 4-d,\; 1-q,\; 1-r), \\
g_4(a, b, c, d, q, r) &= (2-a,\; 1-b,\; 3-c,\; 4-d,\; 2-q,\; 1-r).
\end{aligned}$$
Each $g_k$ is an affine involution on $\mathbb{F}_5^6$: $g_k(g_k(x)) = x$ for all $x \in \mathbb{F}_5^6$.

### Proposition 1.1 (Intermediate Affine Coordinate Bijection $\Psi_{\mathrm{aff}}$)
Define $\Psi_{\mathrm{aff}} : \mathbb{F}_5^6 \to \mathbb{F}_5^6$ by $\Psi_{\mathrm{aff}}(a, b, c, d, q, r) = (z, A, B, C, D, q)$, where
$$z = a + b + c + d + q + r, \quad A = a + c, \quad B = b + d, \quad C = a - c - 2, \quad D = b - d - 1, \quad q = q \pmod 5.$$
Then $\Psi_{\mathrm{aff}}$ is an affine bijection on $\mathbb{F}_5^6$ with two-sided inverse $\Psi_{\mathrm{aff}}^{-1}(z, A, B, C, D, q) = (a, b, c, d, q, r)$ given by
$$a = 3(A + C + 2), \quad b = 3(B + D + 1), \quad c = 3(A - C - 2), \quad d = 3(B - D - 1), \quad q = q, \quad r = z - A - B - q \pmod 5.$$

*Proof.* In $\mathbb{F}_5$, $2 \cdot 3 = 6 \equiv 1 \pmod 5$. For any $x = (a,b,c,d,q,r) \in \mathbb{F}_5^6$, $A + C + 2 = 2a$, $A - C - 2 = 2c$, $B + D + 1 = 2b$, $B - D - 1 = 2d$, and $z - A - B - q = (a+b+c+d+q+r) - (a+c) - (b+d) - q = r$, so $\Psi_{\mathrm{aff}}^{-1}(\Psi_{\mathrm{aff}}(x)) = x$. Conversely, for any $(z, A, B, C, D, q) \in \mathbb{F}_5^6$, setting $(a,b,c,d,q,r) = \Psi_{\mathrm{aff}}^{-1}(z,A,B,C,D,q)$ gives $a + c = 3(2A) = A$, $b + d = 3(2B) = B$, $a - c - 2 = 3(2C + 4) - 2 = C + 10 \equiv C$, $b - d - 1 = 3(2D + 2) - 1 = D + 5 \equiv D$, and $a + b + c + d + q + r = A + B + q + (z - A - B - q) = z \pmod 5$. Thus $\Psi_{\mathrm{aff}}(\Psi_{\mathrm{aff}}^{-1}(z, A, B, C, D, q)) = (z, A, B, C, D, q)$. $\square$

### Proposition 1.2 (Action of $g_0, \dots, g_4$ in Affine Coordinates)
In terms of $(z, A, B, C, D, q)$ and $r = z - A - B - q \bmod 5$, the five generators act by:
$$\begin{aligned}
g_0 &: (z', A', B', C', D', q', r') = (z,\; B,\; A,\; D-1,\; C+1,\; q,\; r), \\
g_1 &: (z', A', B', C', D', q', r') = (-z,\; -A,\; -B,\; C,\; D,\; -q,\; -r), \\
g_2 &: (z', A', B', C', D', q', r') = (2-z,\; 4-A,\; 2-B,\; C,\; D+2r,\; 1-q,\; -r), \\
g_3 &: (z', A', B', C', D', q', r') = (2-z,\; -A,\; -B,\; -C,\; -D,\; 1-q,\; 1-r), \\
g_4 &: (z', A', B', C', D', q', r') = (3-z,\; -A,\; -B,\; -C,\; -D,\; 2-q,\; 1-r).
\end{aligned}$$

*Proof.* Direct substitution into the definitions of $(z, A, B, C, D, q, r)$:
- For $g_0$: $A' = b+d = B$, $B' = a+c = A$, $C' = b-d-2 = (b-d-1)-1 = D-1$, $D' = a-c-1 = (a-c-2)+1 = C+1$.
- For $g_1$: $A' = -c-a = -A$, $B' = -d-b = -B$, $C' = -c-(-a)-2 = a-c-2 = C$, $D' = -d-(-b)-1 = b-d-1 = D$.
- For $g_2$: $z' = 7 - z \equiv 2 - z$, $A' = (2-c)+(2-a) = 4 - A$, $B' = (1-d+r)+(1-b-r) = 2 - B$, $C' = (2-c)-(2-a)-2 = a-c-2 = C$, $D' = (1-d+r)-(1-b-r)-1 = b-d-1+2r = D+2r$, $q' = 1-q$, $r' = -r$.
- For $g_3$ and $g_4$: $A' = 5 - (a+c) \equiv -A$, $B' = 5 - (b+d) \equiv -B$, $C' = (2-a)-(3-c)-2 = -(a-c-2)-5 \equiv -C$, $D' = (1-b)-(4-d)-1 = -(b-d-1)-5 \equiv -D$, with $(z', q', r') = (12-z, 1-q, 1-r) \equiv (2-z, 1-q, 1-r)$ for $g_3$ and $(13-z, 2-q, 1-r) \equiv (3-z, 2-q, 1-r)$ for $g_4$. $\square$

---

## 2. Claim 1: Complete Nonlinear Chart $\Phi$, Global Inverse, and Fibre Structure

Let $\tau(z, A) = z A^3 + 1 - A^4 \bmod 5$, and for $j \in \mathbb{F}_5$ let $e_j(z) = 1 - (z - j)^4 \bmod 5$ be the Lagrange idempotent ($e_j(z) = 1$ if $z = j$ and $0$ if $z \ne j$). The nonlinear chart $\Phi : \mathbb{F}_5^6 \to \mathbb{F}_5^6$ is defined sheet-by-sheet as:
$$\Phi(x) = \begin{cases}
(z,\; C,\; A,\; B,\; D,\; q) & \text{if } z = 0, \\
(z,\; q,\; A,\; B,\; C,\; D) & \text{if } z = 2, \\
(z,\; \tau(z, A) D,\; A,\; B,\; C,\; q) & \text{if } z \in \{1, 4\}, \\
(z,\; D,\; A,\; B,\; C,\; q) & \text{if } z = 3,
\end{cases}$$
and globally by the polynomial tuple $\Phi(x) = (y_0, y_1, y_2, y_3, y_4, y_5)$ where:
$$\begin{aligned}
y_0 &= z, \\
y_1 &= T(x) := e_0(z) C + e_2(z) q + \bigl(e_1(z) + e_4(z)\bigr) \tau(z, A) D + e_3(z) D, \\
y_2 &= A, \\
y_3 &= B, \\
y_4 &= e_0(z) D + \bigl(1 - e_0(z)\bigr) C, \\
y_5 &= e_2(z) D + \bigl(1 - e_2(z)\bigr) q \pmod 5.
\end{aligned}$$
The receiver is $R(x) = (y_0, y_1) = (z, T(x)) \in \mathbb{F}_5^2$, and the fixed semantic reader $G : \mathbb{F}_5^2 \to \mathcal{O}$ is
$$G(z, t) = \begin{cases}
\mathrm{BLANK} & \text{if } z \in \{2, 3\}, \\
\mathrm{PRESENT}(t) & \text{if } z \in \{0, 1, 4\},
\end{cases}$$
with $\mathrm{PRESENT}(0) \ne \mathrm{BLANK}$.

### Theorem 2.1 (Two-Sided Bijection, Global Inverse, $A = 0$ Locus, and $625$-State Fibres)
1. **Invertibility of $\tau(z, A)$ on $z \in \{1, 4\}$ including $A = 0$:**
   Define $\sigma(z, A) := z A + 1 - A^4 \bmod 5$. For every $z \in \{1, 4\}$ and every $A \in \mathbb{F}_5$:
   - If $A = 0$, then $\tau(z, 0) = 1$ and $\sigma(z, 0) = 1$, so $\tau(z, 0)\sigma(z, 0) = 1 \pmod 5$.
   - If $A \in \mathbb{F}_5^\times = \{1, 2, 3, 4\}$, Fermat's Little Theorem gives $A^4 \equiv 1 \pmod 5$, while $z \in \{\pm 1\}$ gives $z^2 \equiv 1 \pmod 5$. Hence $\tau(z, A) \equiv z A^3 \equiv z A^{-1} \in \mathbb{F}_5^\times$, $\sigma(z, A) \equiv z A \in \mathbb{F}_5^\times$, and
     $$\tau(z, A) \sigma(z, A) \equiv (z A^3)(z A) = z^2 A^4 \equiv 1 \cdot 1 = 1 \pmod 5, \qquad \tau(z, A)^3 \equiv \sigma(z, A) \pmod 5.$$
2. **Complete two-sided inverse $\Phi^{-1}$:**
   Given any $y = (y_0, y_1, y_2, y_3, y_4, y_5) \in \mathbb{F}_5^6$, set $z = y_0$, $A = y_2$, $B = y_3$, and recover $(C, D, q)$ sheet-by-sheet:
   $$(C, D, q) = \begin{cases}
   (y_1,\; y_4,\; y_5) & \text{if } y_0 = 0, \\
   (y_4,\; y_5,\; y_1) & \text{if } y_0 = 2, \\
   (y_4,\; \sigma(y_0, y_2) y_1,\; y_5) & \text{if } y_0 \in \{1, 4\}, \\
   (y_4,\; y_1,\; y_5) & \text{if } y_0 = 3,
   \end{cases}$$
   or equivalently by the global polynomial formulas:
   $$\begin{aligned}
   C &= e_0(y_0) y_1 + \bigl(1 - e_0(y_0)\bigr) y_4 \pmod 5, \\
   D &= e_0(y_0) y_4 + e_2(y_0) y_5 + \bigl(e_1(y_0) + e_4(y_0)\bigr)(y_0 y_2 + 1 - y_2^4) y_1 + e_3(y_0) y_1 \pmod 5, \\
   q &= e_2(y_0) y_1 + \bigl(1 - e_2(y_0)\bigr) y_5 \pmod 5,
   \end{aligned}$$
   and define $\Phi^{-1}(y) := \Psi_{\mathrm{aff}}^{-1}(z, A, B, C, D, q)$. Then $\Phi^{-1}(\Phi(x)) = x$ for all $15,625$ states $x \in \mathbb{F}_5^6$ and $\Phi(\Phi^{-1}(y)) = y$ for all $15,625$ tuples $y \in \mathbb{F}_5^6$.
3. **Uniform $625$-state receiver fibres:**
   Because $\Phi = (R, S)$ is a bijection $\mathbb{F}_5^6 \to \mathbb{F}_5^2 \times \mathbb{F}_5^4$, every receiver value $r_0 \in \mathbb{F}_5^2$ ($25$ values in total) has preimage $R^{-1}(r_0) = \Phi^{-1}(\{r_0\} \times \mathbb{F}_5^4)$ of cardinality $|R^{-1}(r_0)| = 5^4 = 625$. $\square$

---

## 3. Claim 2: Actual $n = 0$ Prefix, Common Initial Receiver, and Reset

For each ordered message pair $(\lambda, \mu) \in \mathbb{F}_5^2$, the prepared state at $n = 0$ is
$$E(\lambda, \mu) = \bigl(3(\lambda+3),\; 3(\mu+1),\; 3(-\lambda-1),\; 3(-\mu-1),\; 0,\; 1\bigr) \pmod 5.$$

### Theorem 3.1 (Prepared Initial Chart and Three-Step Prefix)
For all $25$ pairs $(\lambda, \mu) \in \mathbb{F}_5^2$, let $x_0 = E(\lambda, \mu)$ and $x_{n+1} = T_{\theta_n}(x_n)$ for $n \ge 0$:
1. **Initial chart at $n = 0$:**
   $$A_0 = 3(\lambda+3-\lambda-1) = 3(2) \equiv 1, \quad B_0 = 3(\mu+1-\mu-1) = 0, \quad q_0 = 0, \quad r_0 = 1,$$
   $$C_0 = 3(2\lambda+4) - 2 = 6\lambda + 10 \equiv \lambda, \quad D_0 = 3(2\mu+2) - 1 = 6\mu + 5 \equiv \mu, \quad z_0 = A_0 + B_0 + q_0 + r_0 = 2 \pmod 5.$$
   Since $z_0 = 2$, $\Phi(E(\lambda, \mu)) = (z_0, q_0, A_0, B_0, C_0, D_0) = (2, 0, 1, 0, \lambda, \mu)$. Thus $R(x_0) = (2, 0)$ is identical across all $25$ pairs, $G(R(x_0)) = \mathrm{BLANK}$, and $(\lambda, \mu)$ are the $5$th and $6$th coordinates of $\Phi(x_0)$ (independent coordinates of the complement $S(x_0) = (1, 0, \lambda, \mu)$).
2. **Step $n = 0 \to 1$ ($\theta_0 = 0$):**
   The selector is $j_0 = (z_0 + 2\theta_0) \bmod 5 = 2$, applying $g_2$. By Proposition 1.2:
   $$(z_1, A_1, B_1, C_1, D_1, q_1, r_1) = (2-2,\; 4-1,\; 2-0,\; \lambda,\; \mu+2,\; 1-0,\; -1) \equiv (0,\; 3,\; 2,\; \lambda,\; \mu+2,\; 1,\; 4) \pmod 5.$$
   On the $z_1 = 0$ sheet, $\Phi(x_1) = (0, \lambda, 3, 2, \mu+2, 1)$, so $R(x_1) = (0, \lambda)$ and $G(R(x_1)) = \mathrm{PRESENT}(\lambda)$.
3. **Step $n = 1 \to 2$ ($\theta_1 = 1$):**
   Since $z_1 = 0$ and $\theta_1 = 1$, the selector is $j_1 = (0 + 2) \bmod 5 = 2$, applying $g_2$ a second time. Because $g_2$ is an involution on $\mathbb{F}_5^6$,
   $$x_2(\lambda, \mu) = g_2(g_2(x_0(\lambda, \mu))) = x_0(\lambda, \mu), \qquad z_2 = 2, \qquad R(x_2) = (2, 0), \qquad G(R(x_2)) = \mathrm{BLANK},$$
   while in $\Omega = \mathbb{N}_0 \times \mathbb{F}_5^6$, $(2, x_2) \ne (0, x_0)$.
4. **Step $n = 2 \to 3$ ($\theta_2 = 1$):**
   Since $z_2 = 2$ and $\theta_2 = 1$, the selector is $j_2 = (2 + 2) \bmod 5 = 4$, applying $g_4$ to $x_2 = x_0$. By Proposition 1.2:
   $$(z_3, A_3, B_3, C_3, D_3, q_3, r_3) = (3-2,\; -1,\; 0,\; -\lambda,\; -\mu,\; 2-0,\; 1-1) \equiv (1,\; 4,\; 0,\; -\lambda,\; -\mu,\; 2,\; 0) \pmod 5.$$
   Here $z_3 = 1$ and $A_3 = 4 \equiv -1 \pmod 5$, so $\tau(1, 4) = 1 \cdot 4^3 + 1 - 4^4 \equiv 4 \equiv -1 \pmod 5$ and $\tau(1, 4) D_3 = (-1)(-\mu) = \mu \pmod 5$. Thus $\Phi(x_3) = (1, \mu, 4, 0, -\lambda, 2)$, $R(x_3) = (1, \mu)$, and $G(R(x_3)) = \mathrm{PRESENT}(\mu)$.
   Hence the selector prefix is $(j_0, j_1, j_2) = (2, 2, 4)$, the trace prefix is $(z_0, z_1, z_2, z_3) = (2, 0, 2, 1)$, and the receiver trace is $((2,0), (0,\lambda), (2,0), (1,\mu))$. $\square$

---

## 4. Claim 3: Synchronized $5,000$-State Invariant Carrier and Permanent Retention

Define the synchronized nonzero-$A$ carrier
$$\mathcal{S}_{5000} := \bigl\{ x \in \mathbb{F}_5^6 : z(x) \in \{1, 4\},\; A(x) \ne 0 \bigr\},$$
and on $\mathcal{S}_{5000}$ define the two rational invariants
$$I_C(x) := \frac{z(x) C(x)}{A(x)} \equiv z(x) A(x)^3 C(x) \pmod 5, \qquad I_D(x) := \frac{z(x) D(x)}{A(x)} \equiv z(x) A(x)^3 D(x) \pmod 5.$$

### Theorem 4.1 (Closure of $\mathcal{S}_{5000}$, Invariance of $(I_C, I_D)$, and All-Time Retention from $n = 3$)
1. **Cardinality:** Because $\Psi_{\mathrm{aff}}$ is a bijection and $(z, A, B, C, D, q) \in \{1, 4\} \times \{1, 2, 3, 4\} \times \mathbb{F}_5^4$ has $2 \times 4 \times 5^4 = 5000$ tuples, $|\mathcal{S}_{5000}| = 5000$.
2. **Closure and Invariance under both selector parities:**
   Let $x \in \mathcal{S}_{5000}$ and $\theta \in \{0, 1\}$, and set $x' = T_\theta(x) = g_{(z + 2\theta) \bmod 5}(x)$.
   - If $(z, \theta) \in \{(1, 0), (4, 1)\}$, then $(z + 2\theta) \bmod 5 = 1$, so $x' = g_1(x)$. By Proposition 1.2,
     $$z' = -z \in \{4, 1\}, \quad A' = -A \ne 0, \quad B' = -B, \quad C' = C, \quad D' = D.$$
     Thus $x' \in \mathcal{S}_{5000}$ and
     $$I_C(x') = \frac{(-z) C}{-A} = \frac{z C}{A} = I_C(x), \qquad I_D(x') = \frac{(-z) D}{-A} = \frac{z D}{A} = I_D(x).$$
   - If $(z, \theta) = (1, 1)$, then $(z + 2\theta) \bmod 5 = 3$ ($x' = g_3(x)$) and $z' = 2 - 1 = 1 = z$. If $(z, \theta) = (4, 0)$, then $(z + 2\theta) \bmod 5 = 4$ ($x' = g_4(x)$) and $z' = 3 - 4 \equiv 4 = z \pmod 5$. In both cases, Proposition 1.2 gives
     $$z' = z \in \{1, 4\}, \quad A' = -A \ne 0, \quad B' = -B, \quad C' = -C, \quad D' = -D.$$
     Thus $x' \in \mathcal{S}_{5000}$ and
     $$I_C(x') = \frac{z (-C)}{-A} = \frac{z C}{A} = I_C(x), \qquad I_D(x') = \frac{z (-D)}{-A} = \frac{z D}{A} = I_D(x).$$
3. **Readout on $\mathcal{S}_{5000}$ and Induction for $n \ge 3$:**
   For every $x \in \mathcal{S}_{5000}$, $A \ne 0 \implies A^4 \equiv 1 \pmod 5$, so $\tau(z, A) = z A^3 + 1 - A^4 \equiv z A^3 \equiv z / A \pmod 5$, and hence $T(x) = \tau(z, A) D = I_D(x)$ and $G(R(x)) = G(z, I_D(x)) = \mathrm{PRESENT}(I_D(x))$.
   By Theorem 3.1(4), at $n = 3$ every prepared trajectory satisfies $x_3(\lambda, \mu) \in \mathcal{S}_{5000}$ with $z_3 = 1$, $A_3 = 4 \equiv -1$, $C_3 = -\lambda$, $D_3 = -\mu$, so
   $$I_C(x_3(\lambda, \mu)) = \frac{1 \cdot (-\lambda)}{-1} = \lambda, \qquad I_D(x_3(\lambda, \mu)) = \frac{1 \cdot (-\mu)}{-1} = \mu.$$
   By induction on $n \ge 3$, since $x_{n+1} = T_{\theta_n}(x_n)$ and $\mathcal{S}_{5000}$ is closed under $T_0$ and $T_1$ with $(I_C, I_D)$ invariant, every $n \ge 3$ satisfies $x_n(\lambda, \mu) \in \mathcal{S}_{5000}$, $(I_C(x_n), I_D(x_n)) = (\lambda, \mu)$, $R(x_n) = (z_n, \mu)$ with $z_n \in \{1, 4\}$, and $G(R(x_n)) = \mathrm{PRESENT}(\mu)$. $\square$

---

## 5. Claim 4: Prepared $500$-State Tail Partition and Closure

For each $(\lambda, \mu) \in \mathbb{F}_5^2$, define
$$\mathcal{T}_{\lambda, \mu} := \left\{ \Psi_{\mathrm{aff}}^{-1}\!\left(z,\; A,\; 0,\; \frac{\lambda A}{z},\; \frac{\mu A}{z},\; q\right) : z \in \{1, 4\},\; A \in \{1, 4\},\; q \in \mathbb{F}_5 \right\}.$$

### Theorem 5.1 (Disjoint $25 \times 20$ Partition and Closure of $\mathcal{T}_{500}$)
1. For each fixed $(\lambda, \mu) \in \mathbb{F}_5^2$, $(z, A, q)$ ranges freely over $\{1, 4\} \times \{1, 4\} \times \mathbb{F}_5$ ($2 \times 2 \times 5 = 20$ tuples) while $(B, C, D) = (0, \lambda A / z, \mu A / z)$ is uniquely fixed. Since $\Psi_{\mathrm{aff}}^{-1}$ is a bijection, $|\mathcal{T}_{\lambda, \mu}| = 20$.
2. Every $x \in \mathcal{T}_{\lambda, \mu}$ lies in $\mathcal{S}_{5000}$ and satisfies $(I_C(x), I_D(x)) = (z C / A, z D / A) = (\lambda, \mu)$. Because $(I_C, I_D)$ is single-valued on $\mathcal{S}_{5000}$, the $25$ sets $\mathcal{T}_{\lambda, \mu}$ are pairwise disjoint, and their union
   $$\mathcal{T}_{500} := \bigsqcup_{(\lambda, \mu) \in \mathbb{F}_5^2} \mathcal{T}_{\lambda, \mu} = \bigl\{ x \in \mathbb{F}_5^6 : z(x) \in \{1, 4\},\; A(x) \in \{1, 4\},\; B(x) = 0 \bigr\}$$
   has cardinality $25 \times 20 = 500$.
3. For any $x \in \mathcal{T}_{\lambda, \mu}$ and $\theta \in \{0, 1\}$, Theorem 4.1 gives $z(T_\theta(x)) \in \{1, 4\}$, $A(T_\theta(x)) = -A(x) \in \{1, 4\}$, $B(T_\theta(x)) = -B(x) = 0$, and $(I_C(T_\theta(x)), I_D(T_\theta(x))) = (\lambda, \mu)$, so $T_\theta(x) \in \mathcal{T}_{\lambda, \mu}$. Since each $T_\theta$ is bijective on $\mathcal{T}_{\lambda, \mu}$, $T_\theta(\mathcal{T}_{\lambda, \mu}) = \mathcal{T}_{\lambda, \mu}$ and $T_\theta(\mathcal{T}_{500}) = \mathcal{T}_{500}$.
4. At $n = 3$, $x_3(\lambda, \mu) = \Psi_{\mathrm{aff}}^{-1}(1, 4, 0, -\lambda, -\mu, 2) \in \mathcal{T}_{\lambda, \mu}$, so $x_n(\lambda, \mu) \in \mathcal{T}_{\lambda, \mu}$ for all $n \ge 3$. $\square$

---

## 6. Claim 5: Autonomous $(z, q, r)$ Quotient and Access Boundary

### Theorem 6.1 (Autonomous $(z, q, r)$ Quotient, $22$-State Reachable Set, and Message-Independent Raw Port)
1. **Closed $(z, q, r)$ quotient:**
   By Proposition 1.2, for every $k \in \{0, 1, 2, 3, 4\}$, the image triple $(z', q', r')$ under $g_k$ is a function $\bar{g}_k(z, q, r)$ of $(z, q, r)$ alone:
   $$\bar{g}_0(z, q, r) = (z, q, r), \quad \bar{g}_1(z, q, r) = (-z, -q, -r), \quad \bar{g}_2(z, q, r) = (2-z, 1-q, -r),$$
   $$\bar{g}_3(z, q, r) = (2-z, 1-q, 1-r), \quad \bar{g}_4(z, q, r) = (3-z, 2-q, 1-r) \pmod 5.$$
   Since the selector $j_n = (z + 2\theta_n) \bmod 5$ depends only on $z$ and $\theta_n$, the projection $\pi_{z,q,r}(x) = (z(x), q, r)$ intertwines $T_\theta$ with $\bar{T}_\theta(z, q, r) := \bar{g}_{(z + 2\theta)\bmod 5}(z, q, r)$:
   $$\pi_{z,q,r}(T_\theta(x)) = \bar{T}_\theta(\pi_{z,q,r}(x)) \quad \forall x \in \mathbb{F}_5^6,\; \forall \theta \in \{0, 1\}.$$
   Starting from $(2, 0, 1)$, the reachable set under $\{\bar{T}_0, \bar{T}_1\}$ consists of the $2$ prefix triples $\{(2, 0, 1), (0, 1, 4)\}$ together with the $20$ tail triples $\{(z, q, z - A - q \bmod 5) : z \in \{1, 4\},\; A \in \{1, 4\},\; q \in \mathbb{F}_5\}$, giving $22$ reachable $(z, q, r)$ states in total (all $22$ of which are visited along the actual trajectory $0 \le n \le 1024$).
2. **Message-independent raw $(q, r)$ history:**
   Every prepared state $E(\lambda, \mu)$ has $\pi_{z,q,r}(E(\lambda, \mu)) = (2, 0, 1)$. By induction on $n \ge 0$,
   $$(z_n(\lambda, \mu),\; q_n(\lambda, \mu),\; r_n(\lambda, \mu)) = \bar{T}_{\theta_{n-1}} \circ \dots \circ \bar{T}_{\theta_0}(2, 0, 1)$$
   is strictly independent of $(\lambda, \mu)$ for all $n \ge 0$. In particular, the raw $(q_n, r_n)$ port trajectory carries zero information about $(\lambda, \mu)$.
3. **Mixed nonlinear coordinate and full-state retention:**
   The receiver $R(x) = (z, T(x))$ reads $(\lambda, \mu)$ only because $T(x)$ is a mixed nonlinear polynomial coupling the source coordinates $(a, b, c, d)$ (through $A = a+c$, $C = a-c-2$, $D = b-d-1$, and $z = a+b+c+d+q+r$) with $q$. At every $n \ge 0$, because $(q_n, r_n)$ is independent of $(\lambda, \mu)$ and $T_{\theta_{n-1}} \circ \dots \circ T_{\theta_0}$ is a bijection on $\mathbb{F}_5^6$, the raw source block $(a_n, b_n, c_n, d_n)$ takes $25$ distinct values across $(\lambda, \mu) \in \mathbb{F}_5^2$ (for $n \ge 3$, $(\lambda, \mu) = (I_C(x_n), I_D(x_n))$). Both messages remain in the full state for all time; there is no source depletion, no fresh second arrival after $n = 0$, and no counter reset in $\Omega = \mathbb{N}_0 \times \mathbb{F}_5^6$. $\square$

---

## 7. Claim 6: Nonaffinity Witness and Reconciliation with the Affine Obstruction

### Theorem 7.1 (Nonaffinity Witness and Compatibility with the Arbitrary-Rank Affine Obstruction)
1. **Explicit nonaffinity witness $E(0, 0)$ vs $E(0, 1)$ under $g_4$:**
   At $n = 2$ (and $n = 0$),
   $$E(0, 0) = (4, 3, 2, 2, 0, 1), \qquad E(0, 1) = (4, 1, 2, 4, 0, 1).$$
   Both states have $z = 2$ and $q = 0$, so before $g_4$:
   $$R(E(0, 0)) = (2, 0) = R(E(0, 1)).$$
   Applying $g_4(x) = -x + t_4$ with $t_4 = (2, 1, 3, 4, 2, 1)$ gives:
   $$g_4(E(0, 0)) = (3, 3, 1, 2, 2, 0), \qquad g_4(E(0, 1)) = (3, 0, 1, 0, 2, 0),$$
   for which $z = 1, A = 4, \tau(1, 4) = 4$ and $D(g_4(E(0, 0))) = 0$, $D(g_4(E(0, 1))) = 4$, yielding:
   $$R(g_4(E(0, 0))) = (1, 0) \ne (1, 1) = R(g_4(E(0, 1))).$$
2. **Why every affine receiver is obstructed and how $R$ escapes:**
   For *any* affine receiver $R_{\mathrm{aff}}(x) = L x + h$ ($L \in \mathbb{F}_5^{k \times 6}, h \in \mathbb{F}_5^k$, arbitrary $k \ge 0$), the fact that $g_3(x) = -x + t_3$ and $g_4(x) = -x + t_4$ have linear part $-I_6$ forces
   $$R_{\mathrm{aff}}(g_j(x)) = L(-x + t_j) + h = -R_{\mathrm{aff}}(x) + 2h + L t_j \qquad (j \in \{3, 4\}).$$
   In particular, $R_{\mathrm{aff}}(x) = R_{\mathrm{aff}}(x') \implies R_{\mathrm{aff}}(g_4(x)) = R_{\mathrm{aff}}(g_4(x'))$. Since every origin-zero trajectory $x_0 \in \mathbb{F}_5^6$ has $z(x_2) \in \{1, 2\}$ and applies either $g_3$ (when $z(x_2) = 1$, where $x_2$ and $x_3$ share the same recurrent $X_{14}$ sign fibre $V(x_3) = -V(x_2)$ with $V(x) = (A, B, zC, zD)$) or $g_4$ (when $z(x_2) = 2$), any family with a common affine receiver state $R_{\mathrm{aff}}(x_2) = r_{\mathrm{ready}}$ has at most $2$ receiver states at $n = 3$ (at most $1$ on $z(x_2) = 2$) and at most $1$ permanently retained nonblank second message.
   That theorem holds without modification for all affine maps $R_{\mathrm{aff}}$. The present receiver $R(x) = (z, T(x))$ escapes the affine obstruction strictly because $T(x) = e_0(z)C + e_2(z)q + (e_1(z)+e_4(z))\tau(z,A)D + e_3(z)D$ is **nonlinear** (total degree $5$), using the sheet idempotents $e_j(z)$ to switch from reading $q$ on $z = 2$ to reading $\tau(z, A) D$ on $z \in \{1, 4\}$, so $R(-x + t_4)$ is not determined by $R(x)$ alone. $\square$

---

## 8. Claim 7: Two-Coordinate Minimality and Non-Autonomous Receiver Evolution

### Theorem 8.1 (Minimal $\mathbb{F}_5$ Coordinate Count and Non-Autonomy Witness)
1. **Minimality of $k = 2$ coordinates in $\mathbb{F}_5$:**
   The semantic output set required by the contract is
   $$\mathcal{O} = \{\mathrm{BLANK},\; \mathrm{PRESENT}(0),\; \mathrm{PRESENT}(1),\; \mathrm{PRESENT}(2),\; \mathrm{PRESENT}(3),\; \mathrm{PRESENT}(4)\},$$
   which has cardinality $|\mathcal{O}| = 6$. For any total fixed reader $G : \mathbb{F}_5^k \to \mathcal{O}$ whose image on the prepared trajectories contains all $6$ semantic values,
   $$6 = |\mathcal{O}| \le |\operatorname{im}(G)| \le |\mathbb{F}_5^k| = 5^k.$$
   Since $5^0 = 1 < 6$ and $5^1 = 5 < 6 \le 25 = 5^2$, the minimum number of $\mathbb{F}_5$ coordinates is $k = 2$.
   *Scope boundary:* This lower bound concerns only the number of $\mathbb{F}_5$ coordinates of a total fixed reader realizing $6$ semantic values; it asserts nothing about binary bit count, physical spatial dimension, or minimal polynomial degree.
2. **Non-autonomy of the receiver on $\mathbb{F}_5^2$:**
   Consider $E(0, 0) = (4, 3, 2, 2, 0, 1)$ and $E(1, 0) = (2, 3, 4, 2, 0, 1)$. At $n = 0$, both states have the same receiver value:
   $$R(E(0, 0)) = (2, 0) = R(E(1, 0)).$$
   At $n = 1$ (under $g_2$),
   $$x_1(0, 0) = g_2(E(0, 0)) = (0, 0, 3, 2, 1, 4), \qquad x_1(1, 0) = g_2(E(1, 0)) = (3, 0, 0, 2, 1, 4),$$
   which have distinct receiver values:
   $$R(x_1(0, 0)) = (0, 0) \ne (0, 1) = R(x_1(1, 0)).$$
   Hence $R(x_{n+1})$ is not a function of $(n, R(x_n))$ (or $R(x_n)$): the receiver does not evolve autonomously on $\mathbb{F}_5^2$. $\square$
