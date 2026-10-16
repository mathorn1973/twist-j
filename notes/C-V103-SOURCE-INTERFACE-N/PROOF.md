# Analytical Proofs: C-V103-SOURCE-INTERFACE-N

**NON-CANONICAL / L1 / analytical candidate.**  
A. M. Thorn, 2026-10-16. Original work Apache-2.0.  
Candidate `C-V103-SOURCE-INTERFACE-N`, program [#1548](https://github.com/mathorn1973/twist-j/issues/1548) (Lane D), child issue [#1551](https://github.com/mathorn1973/twist-j/issues/1551).  
Specification pin: `9cb2b7d89eb1fc955fb67e886e46a379cb1aba43`.

All notation and premises are fixed by `CONTRACT.md` and `PREREG.md` from Public Canon v102 at `a632c6a162dc87e60104d7a478e7650a6d5c4a1b` (content commit `b04e22dd3ed8e4240cff347364f24670d4183a4d`). No scientific script or numerical search is used.

---

## 1. Complete Map, Domain, and Equality Table (Question Q1)

### Theorem D1 (Six-stage interface typing and family readiness/absence classification)

Let $x = (p_1, p_4, p_1', p_4', q, r) = (a, b, c, d, q, r) \in \mathbb{F}_5^6$ be a native checkpoint with trace $z = a+b+c+d+q+r \in \mathbb{F}_5$ and canonical affine coordinates
$$A = a+c, \qquad B = b+d, \qquad C = a-c-2, \qquad D = b-d-1,$$
with inverse on $\mathbb{F}_5^6$:
$$a = 3(A+C+2), \quad c = 3(A-C-2), \quad b = 3(B+D+1), \quad d = 3(B-D-1), \quad r = z-A-B-q.$$
The six stages of the source-to-field and contact interface have the following exact domains, codomains, defining maps, and equivalence relations (with piston projection $\pi_P(a,b,c,d,q,r) = (a,b,c,d) \in \mathbb{F}_5^4$, piston gate map $h_P(a,b,c,d) = (b+2a, d+2c) \in \mathbb{F}_5^2$, checkpoint gate map $h = h_P \circ \pi_P$, piston kernel $K := \ker(h_P) = \{(a,3a,c,3c) : (a,c)\in\mathbb{F}_5^2\} \subset \mathbb{F}_5^4$, and active shell residue subgroup $G_L := L\mathbb{Z}^4 \bmod 5 = \{(y_0,y_1,y_2,y_3)\in\mathbb{F}_5^4 : y_0+2y_1 = y_2+2y_3 = 0\} = \{(3y_1,y_1,3y_3,y_3) : (y_1,y_3)\in\mathbb{F}_5^2\} \subset \mathbb{F}_5^4$):

| Stage | Object / Map | Domain $\to$ Codomain | Defining Formula | Equality / Kernel / Image Criterion |
| :--- | :--- | :--- | :--- | :--- |
| **1. Raw checkpoint** | $x = (a,b,c,d,q,r) \leftrightarrow (z,A,B,C,D,q)$ | $\mathbb{F}_5^6 \to \mathbb{F}_5^6$ | $T_\theta(x) = g_{z+2\theta}(x)$, $\theta_n = \operatorname{popcount}(n)\bmod 2$ | Pointwise equality in $\mathbb{F}_5^6$ ($15625$ states); $\pi_{z,q,r}(x)=(z,q,r)$ is an autonomous $\mathbb{F}_5^3$ quotient. |
| **2. $W$-piston & gate residue** | $\pi_P(x)=(a,b,c,d)$; $W(a,b,c,d) = (b,a,d,c)$; $h(x) = h_P(\pi_P(x)) = (b+2a, d+2c)$ | $\mathbb{F}_5^6 \xrightarrow{\pi_P} \mathbb{F}_5^4 \xrightarrow{W} \mathbb{F}_5^4$; $h: \mathbb{F}_5^6 \to \mathbb{F}_5^2$ | $h_1 = 3(B+2A+D+2C)$, $h_2 = 3(B+2A-D-2C)$ | $K = \ker(h_P) \subset \mathbb{F}_5^4$ ($25$ piston residues), $W(K) = G_L$ ($K \ne G_L$), $\mathcal{G}_0 = \ker(h) = \pi_P^{-1}(K) \subset \mathbb{F}_5^6$ ($625$ checkpoints): $h(x)=(0,0) \iff \pi_P(x)\in K \iff W(\pi_P(x))\in G_L \iff B+2A = D+2C = 0$. |
| **3. Balanced integer lift** | $\ell: \mathbb{F}_5 \to \{-2,-1,0,1,2\}$; $\ell_4 \circ W(\pi_P(x))$ | $\mathbb{F}_5^4 \to \{-2,-1,0,1,2\}^4 \subset \mathbb{Z}^4$ | $\ell(0,1,2,3,4) = (0,1,2,-2,-1)$ componentwise | Bijection onto $[-2,2]^4 \cap \mathbb{Z}^4$ ($625$ points); general coset is $\bar{y} + 5\mathbb{Z}^4$. Not an $A_f$-equivariant or $H$-minimizing map. |
| **4. Raw field split & shell $L\mathbb{Z}^4$** | $z_{\mathrm{raw}} = P y + S_{\mathrm{st}}\sigma$; $L = (I-A_f)(I-A_f^2)$ | $\mathbb{Z}^4 \times \mathbb{Z}^2 \to \mathbb{Z}^6$; $L: \mathbb{Z}^4 \to L\mathbb{Z}^4$ | $P(y_0,y_1,y_2,y_3) = (y_0-y_1,-y_0,y_1,y_1,y_2,y_3)$; $V_{\mathrm{inv}} = 5L^{-1}$ | Split lattice has index $5$ in $\mathbb{Z}^6$ ($2E_0-3E_1+E_2+E_3 \equiv 0 \pmod 5$); $y \in L\mathbb{Z}^4 \iff (y\bmod 5)\in G_L \iff h_P(W(y\bmod 5))=(0,0)$ (index $25$ in $\mathbb{Z}^4$). |
| **5. Supplied funded contact $H_B$** | $\eta(q,r) \in \mathbb{Q}^4$; $a(q,r) = S\eta(q,r) \in \mathbb{Q}^D$ | $\mathbb{F}_5^2 \to \mathbb{Q}^4 \to \mathbb{Q}^D$ ($|D|=705$) | $\eta(q,r) = \bigl(\frac{\ell(q)}{2}, \frac{\ell(r)+1}{2}, 0, 0\bigr)$; $\Delta_\sigma = \sigma\langle v-\frac{1}{2}H_D u, a\rangle + \frac{1}{2}\|a\|^2$ | Injects $(q,r) \in \mathbb{F}_5^2$ into $25$ rational vectors supported on $Y=\{y_0,\dots,y_4\}\subset D$; depends only on $(q,r)$, independent of $(a,b,c,d)$. |
| **6. Visible receiver readout** | Family-specific $(R, G)$ or $\operatorname{read}(R_{\mathrm{reg}})$ | $\mathbb{F}_5^6 \to \{\mathrm{BLANK}\} \cup \{\mathrm{PRESENT}(k): k\in\mathbb{F}_5\}$ | See Table D1.2 below | Semantic output equality in the $6$-label set; `BLANK` $\ne$ `PRESENT(0)`. |

#### Proof of Stage 1–6 typing and equivalences

1. **Affine chart, $h(x)$ formula, and distinction between $K = \ker(h_P)$ and $G_L = L\mathbb{Z}^4 \bmod 5$ (Stages 1–2):**
   In $\mathbb{F}_5$, $2 \cdot 3 = 6 \equiv 1 \pmod 5$. Substituting $a = 3(A+C+2)$, $b = 3(B+D+1)$, $c = 3(A-C-2)$, $d = 3(B-D-1)$ into $h_1 = b + 2a$ and $h_2 = d + 2c$ yields
   $$\begin{aligned}
   h_1(x) &= 3(B+D+1) + 6(A+C+2) \equiv A + 3B + C + 3D + 5 \equiv 3\bigl((B+2A) + (D+2C)\bigr) \pmod 5, \\
   h_2(x) &= 3(B-D-1) + 6(A-C-2) \equiv A + 3B - C - 3D - 5 \equiv 3\bigl((B+2A) - (D+2C)\bigr) \pmod 5.
   \end{aligned}$$
   Adding and subtracting gives the invertible change of variables in $\mathbb{F}_5^2$:
   $$s_h(x) := h_1(x) + h_2(x) = B + 2A \pmod 5, \qquad d_h(x) := h_1(x) - h_2(x) = D + 2C \pmod 5.$$
   *Refutation of literal parenthetical clause `h_1 = B+2A` in `CONTRACT.md` line 107 (`R6`):* The literal equation $h_1(x) = B+2A$ does **not** hold on $\mathbb{F}_5^6$ (for example, at $E(0,0) = (4,3,2,2,0,1)$, $h_1(E(0,0)) = 3+2(4) \equiv 1 \pmod 5$, whereas $B+2A = 0+2(1) = 2 \pmod 5$). Instead, $B+2A = h_1(x)+h_2(x) = s_h(x)$ is the **gate sum**, and $D+2C = h_1(x)-h_2(x) = d_h(x)$ is the **gate difference**. Since $3$ is a unit in $\mathbb{F}_5$, $h(x) = (0,0) \iff s_h(x) = 0 \text{ and } d_h(x) = 0 \iff B \equiv 3A \text{ and } D \equiv 3C \pmod 5$. For each of the $25$ pairs $(A, C) \in \mathbb{F}_5^2$, $(B, D) = (3A, 3C)$ is uniquely determined, so the piston kernel $K = \ker(h_P) = \{(a,3a,c,3c) : (a,c)\in\mathbb{F}_5^2\} \subset \mathbb{F}_5^4$ has cardinality $25$ and $\mathcal{G}_0 = \ker(h) = \pi_P^{-1}(K) \subset \mathbb{F}_5^6$ has cardinality $25 \times 25 = 625$. In the fixed marking, $K \ne G_L$ (for instance, $(1,3,0,0) \in K \setminus G_L$ has $1+2(3)\equiv 2\ne 0$, while $(0,0,3,1) = L u_\star \bmod 5 \in G_L \setminus K$ has $h_P(0,0,3,1) = (0,2)\ne(0,0)$); the comparison map $W(a,b,c,d)=(b,a,d,c)$ maps $K$ bijectively onto $G_L = W(K)$.

2. **Balanced lift and integer field shell (Stages 3–4):**
   The map $\ell: \mathbb{F}_5 \to \{-2,-1,0,1,2\}$ is the unique section of $\mathbb{Z} \to \mathbb{F}_5$ into $[-2,2]\cap\mathbb{Z}$. By `FIELD-CONSERVATIVE-CHAIN-LAW` Shared proof 2, $z_{\mathrm{raw}} = (E,M) \in \mathbb{Z}^6$ splits integrally as $P y + S_{\mathrm{st}}\sigma$ with $(y,\sigma) \in \mathbb{Z}^4 \times \mathbb{Z}^2$ if and only if $2E_0 - 3E_1 + E_2 + E_3 \equiv 0 \pmod 5$, and $y \in L\mathbb{Z}^4$ if and only if $y_0 + 2y_1 \equiv 0 \pmod 5$ and $y_2 + 2y_3 \equiv 0 \pmod 5$, with unique preimage $w = \frac{1}{5}V_{\mathrm{inv}} y \in \mathbb{Z}^4$ and $H(y) = H(Lw) = 5H(w)$. The local gate $G$ on $(R, b_{\mathrm{spec}}, P y + S_{\mathrm{st}}\sigma, r_{\mathrm{res}})$ requires literal matter $R$, an integral split, $y \in L\mathbb{Z}^4$, and $r_{\mathrm{res}} + 4H(w) - 2 \ge 0$; at $r_{\mathrm{res}} = 0$ in `FIELD-CHAIN-FIRST-WORK`, the source reaction produces $2$ neutral resource units (`r_0' = 4H(w)-2 = 2`) when $H(w) = 1$ ($H(y) = 5$).

3. **Supplied funded contact (Stage 5):**
   By `FUNDED-CONTACT-INVOLUTION`, $\eta(q,r) = (\ell(q)/2, (\ell(r)+1)/2, 0, 0) \in \mathbb{Q}^4$ has distinct first two coordinates as $(q,r)$ ranges over $\mathbb{F}_5^2$. Because $\ker(S) = \{0\}$ on $\mathbb{Q}^4$ (for $z = (z_0,z_1,0,0)$ and $s = z_0+z_1$, $(Sz)(y_4) = -s/5$ and $(Sz)(y_i) = z_i - s/5$ recover $z_i = (Sz)(y_i) - (Sz)(y_4)$), the map $(q,r) \mapsto a(q,r) = S\eta(q,r)$ is injective from $\mathbb{F}_5^2$ into $\mathbb{Q}^D$, and depends exclusively on the reference pair $(q,r)$.

4. **Comparison of the three native preparation families (Stage 6):**
   The three inherited v102 families differ in their preparation domain, initial $(q_0, r_0)$ encoding, raw vs semantic blank condition, and absence convention as proved in Table D1.2:

| Property | Original 550-point family $E(\lambda,\mu)$ | Alternative 150-point family $E_{\mathrm{alt}}(\lambda,\mu)$ | One-shot family $x_\lambda(0)$ and $x_{\mathrm{empty}}(0)$ |
| :--- | :--- | :--- | :--- |
| **Canonical claim** | `U-ORIGIN-NONLINEAR-TWO-MESSAGE-READOUT`, `U-FIXED-FAMILY-READOUT-COMPLEXITY` | `U-ALTERNATIVE-AFFINE-SEMANTIC-READOUT` | `U-NATIVE-SOURCE-RECEIVER-RECORD` |
| **Parameter space** | $(\lambda, \mu) \in \mathbb{F}_5^2$ ($25$ occupied pairs) | $(\lambda, \mu) \in \mathbb{F}_5^2$ ($25$ occupied pairs) | $\lambda \in \mathbb{F}_5$ ($5$ occupied) $\cup \{x_{\mathrm{empty}}\}$ ($1$ absence) |
| **Initial checkpoint $x(0)$** | $\bigl(3(\lambda+3), 3(\mu+1), 3(-\lambda-1), 3(-\mu-1), 0, 1\bigr)$ | $\bigl(3\mu, 3, 3\mu, 2, 4+3\lambda+\mu, 3+2\lambda+3\mu\bigr)$ | $x_\lambda(0)=(\lambda,0,-\lambda,0,0,0)$; $x_{\mathrm{empty}}(0)=(0,0,1,0,0,0)$ |
| **Initial $(z_0,A_0,B_0,C_0,D_0)$** | $(2,\, 1,\, 0,\, \lambda,\, \mu)$ | $(2,\, \mu,\, 0,\, 3,\, 0)$ | $x_\lambda$: $(0, 0, 0, 2\lambda-2, 4)$; $x_{\mathrm{empty}}$: $(1, 1, 0, 2, 4)$ |
| **Initial $(q_0, r_0)$** | $(0, 1)$ (constant across all $25$ pairs) | $(4+3\lambda+\mu,\, 3+2\lambda+3\mu)$ (bijection of $\mathbb{F}_5^2$) | $(0, 0)$ (constant across all $5$ $\lambda$ and $x_{\mathrm{empty}}$) |
| **Checkpoint reset $x_2 = x_0$** | Yes: $x_2 = x_0$ for all $25$ pairs | Yes: $x_2 = x_0$ for all $25$ pairs | No: $x_\lambda(2) = (2,1+\lambda,2,1-\lambda,1,0) \ne x_\lambda(0)$ |
| **Required support size** | $550$ points ($25$ at $n=0,2$; $25$ at $n=1$; $500$ tail) | $150$ points ($25$ at $n=0,2$; $25$ at $n=1$; $100$ tail) | Ready carrier $Q$ has $100$ receiver states ($20$ per $\lambda \in \mathbb{F}_5$) |
| **Blank condition at $n=0,2$** | Chart $\Phi$: common raw $R_0=R_2=(2,0)$; quadratic $(P,Q)$: message-dependent raw $(0,\mu)$, common semantic `BLANK` | Affine $(X,H) = (A+D, C+z)$: message-dependent raw $(\mu, 0)$, common semantic `BLANK` | Complementary receiver $R_{\mathrm{reg}}=(b,d,q,r)$: common raw $(0,0,0,0)$ at $n=0$; semantic `BLANK` for $0 \le n < 3$ |
| **`PRESENT(0)` vs absence** | $\lambda=0$ or $\mu=0$ gives `PRESENT(0)`; no separate $26$th absence state declared | $\lambda=0$ or $\mu=0$ gives `PRESENT(0)`; no separate $26$th absence state declared | $\lambda=0$ gives `PRESENT(0)` for $n\ge 3$; sixth state $x_{\mathrm{empty}}(0)$ gives `BLANK` for all $n \ge 0$ |

This completes the proof of Theorem D1. $\square$

---

## 2. Algebraic Gate Overlap and Retained Message Distinctions (Question Q2)

### Lemma D2.1 (Action of native generators on the gate residue $h$ and $(s_h, d_h)$)

For every checkpoint $x = (a,b,c,d,q,r) \in \mathbb{F}_5^6$ with $h(x) = (h_1(x), h_2(x)) = (b+2a, d+2c)$ and $(s_h(x), d_h(x)) = (h_1(x)+h_2(x), h_1(x)-h_2(x)) = (B+2A, D+2C)$:
$$\begin{aligned}
h(g_0 x) &= (a+2b,\, c+2d) = (2h_1(x) + 2a,\, 2h_2(x) + 2c), \\
h(g_1 x) &= (-h_2(x),\, -h_1(x)), & (s_h, d_h)(g_1 x) &= (-s_h(x),\, d_h(x)), \\
h(g_2 x) &= (-h_2(x) + r,\, -h_1(x) - r), & (s_h, d_h)(g_2 x) &= (-s_h(x),\, d_h(x) + 2r), \\
h(g_3 x) &= (-h_1(x),\, -h_2(x)), & (s_h, d_h)(g_3 x) &= (-s_h(x),\, -d_h(x)), \\
h(g_4 x) &= (-h_1(x),\, -h_2(x)), & (s_h, d_h)(g_4 x) &= (-s_h(x),\, -d_h(x)).
\end{aligned}$$
In particular, on the absorbing trace sheet $X_{14} = \{x \in \mathbb{F}_5^6 : z(x) \in \{1,4\}\}$, where the selected generator is always $g_1, g_3$, or $g_4$:
1. $s_h(T_\theta(x)) = -s_h(x)$ and $d_h(T_\theta(x)) = \pm d_h(x)$ for both $\theta \in \{0,1\}$;
2. the zero gate $\mathcal{G}_0 = \{x \in \mathbb{F}_5^6 : h(x) = (0,0)\}$ is invariant under every selected step on $X_{14}$, and more generally $x \in \mathcal{G}_0 \iff T_\theta(x) \in \mathcal{G}_0$ for every $x \in X_{14}$.

#### Proof of Lemma D2.1

Direct substitution from the definitions of $g_0, \dots, g_4$ in `CONTRACT.md` Section 1.1:
- For $g_0(a,b,c,d,q,r) = (b,a,d,c,q,r)$: $h_1(g_0 x) = a + 2b = a + 2(h_1 - 2a) = 2h_1 - 3a \equiv 2h_1 + 2a \pmod 5$, and $h_2(g_0 x) = c + 2d \equiv 2h_2 + 2c \pmod 5$.
- For $g_1(a,b,c,d,q,r) = (-c,-d,-a,-b,-q,-r)$: $h_1(g_1 x) = -d - 2c = -h_2(x)$ and $h_2(g_1 x) = -b - 2a = -h_1(x)$.
- For $g_2(a,b,c,d,q,r) = (2-c, 1-d+r, 2-a, 1-b-r, 1-q, -r)$:
  $$h_1(g_2 x) = (1-d+r) + 2(2-c) = 5 - (d+2c) + r \equiv -h_2(x) + r \pmod 5,$$
  $$h_2(g_2 x) = (1-b-r) + 2(2-a) = 5 - (b+2a) - r \equiv -h_1(x) - r \pmod 5.$$
- For $g_3$ and $g_4$, the first four coordinates are $(2-a, 1-b, 3-c, 4-d)$, so
  $$h_1(g_3 x) = h_1(g_4 x) = (1-b) + 2(2-a) = 5 - (b+2a) \equiv -h_1(x) \pmod 5,$$
  $$h_2(g_3 x) = h_2(g_4 x) = (4-d) + 2(3-c) = 10 - (d+2c) \equiv -h_2(x) \pmod 5.$$
Adding and subtracting $h_1, h_2$ yields the formulas for $(s_h, d_h)$. On $X_{14}$, $z \in \{1,4\}$ and $2\theta \in \{0,2\}$, so $z + 2\theta \bmod 5 \in \{1, 3, 4\}$, selecting only $g_1, g_3, g_4$. Since $(-h_2, -h_1)$ and $(-h_1, -h_2)$ are bijections of $\mathbb{F}_5^2$ fixing $(0,0)$, $h(x) = (0,0) \iff h(T_\theta(x)) = (0,0)$ on $X_{14}$. $\square$

---

### Theorem D2 (Exact gate classification of $E(\lambda,\mu)$, $E_{\mathrm{alt}}(\lambda,\mu)$, and $x_\lambda(0)$ / $x_{\mathrm{empty}}(0)$)

1. **Original 550-point family $E(\lambda,\mu)$ (zero gate overlap $0 / 550$):**
   For every $(\lambda, \mu) \in \mathbb{F}_5^2$, let $x_n(\lambda,\mu)$ be the trajectory from $x_0(\lambda,\mu) = E(\lambda,\mu)$:
   $$\begin{aligned}
   n = 0, 2:\quad (z,A,B,C,D,q,r) &= (2, 1, 0, \lambda, \mu, 0, 1), & s_h &= 2, & d_h &= 2\lambda+\mu, & h &= (1+\lambda+3\mu,\, 1-\lambda-3\mu), \\
   n = 1:\quad (z,A,B,C,D,q,r) &= (0, 3, 2, \lambda, \mu+2, 1, 4), & s_h &= 3, & d_h &= 2+2\lambda+\mu, & h &= (\lambda+3\mu,\, 3-\lambda-3\mu), \\
   n = 3:\quad (z,A,B,C,D,q,r) &= (1, 4, 0, -\lambda, -\mu, 2, 0), & s_h &= 3, & d_h &= 3\lambda+4\mu, & h &= (4+4\lambda+2\mu,\, 4+\lambda+3\mu).
   \end{aligned}$$
   On the entire 500-point synchronized tail ($z, A \in \{1,4\}$, $B=0$, $C = Az\lambda$, $D = Az\mu$, $q \in \mathbb{F}_5$, $r = z-A-q$), and for every $n \ge 3$ by induction on $X_{14}$:
   $$A_n = (-1)^{n-2} \in \{1,4\}, \quad B_n = 0, \quad s_h(x) = B + 2A = 2A \in \{2, 3\} \ne 0 \pmod 5,$$
   $$d_h(x) = Az(2\lambda+\mu), \qquad h(x) = \bigl(A(1 + z(\lambda+3\mu)),\, A(1 - z(\lambda+3\mu))\bigr).$$
   Consequently:
   - while the literal parenthetical equation `h_1 = B+2A` in `CONTRACT.md` line 107 is **refuted** (`R6`, witness $E(0,0)$ has $h_1=1 \ne 2 = B+2A$), the gate sum $s_h(x) = h_1(x)+h_2(x) = B + 2A \in \{2,3\} \ne 0$ is nonvanishing on all $550$ points of the required support $S$ and at every time $n \ge 0$, so $S \cap \mathcal{G}_0 = \emptyset$ ($0 / 550$ points);
   - at every fixed $n \ge 0$ (and at every fixed carrier context $(A,z)$ on $X_{14}$), $h(x_n(\lambda,\mu))$ depends on $(\lambda,\mu)$ only through $2\lambda + \mu \pmod 5$ (equivalently $\lambda + 3\mu \pmod 5$), partitioning the $25$ message pairs into $5$ fibres of size $5$.

2. **Alternative 150-point family $E_{\mathrm{alt}}(\lambda,\mu)$ (zero gate overlap $1 / 150$ overall, $0 / 100$ on the synchronized tail):**
   For every $(\lambda, \mu) \in \mathbb{F}_5^2$, let $x_n^{\mathrm{alt}}(\lambda,\mu)$ be the trajectory from $E_{\mathrm{alt}}(\lambda,\mu)$ with $r_0 = 3 + 2\lambda + 3\mu$ and $q_0 = 4 + 3\lambda + \mu$. Its exact raw checkpoints and affine tuples $(z,A,B,C,D,q,r)$ at $n = 0, 1, 2, 3$ are (`R2` corrected from `e3d35709a86b42c21c1bf57e2be2b3a3cf707598`; see `ERRATA.md` R2):
   $$\begin{aligned}
   n = 0, 2:\quad x_0^{\mathrm{alt}} = x_2^{\mathrm{alt}} &= \bigl(3\mu,\, 3,\, 3\mu,\, 2,\, 4+3\lambda+\mu,\, 3+2\lambda+3\mu\bigr), \\
   (z,A,B,C,D,q,r) &= \bigl(2,\, \mu,\, 0,\, 3,\, 0,\, 4+3\lambda+\mu,\, 3+2\lambda+3\mu\bigr), & s_h &= 2\mu, & d_h &= 1, & h &= (3+\mu,\, 2+\mu), \\
   n = 1:\quad x_1^{\mathrm{alt}} &= \bigl(2-3\mu,\, 2+2\lambda+3\mu,\, 2-3\mu,\, 3\lambda+2\mu,\, 2+2\lambda+4\mu,\, 2+3\lambda+2\mu\bigr), \\
   (z,A,B,C,D,q,r) &= \bigl(0,\, 4-\mu,\, 2,\, 3,\, 1+4\lambda+\mu,\, 2+2\lambda+4\mu,\, 2+3\lambda+2\mu\bigr), & s_h &= 3\mu, & d_h &= 2-\lambda+\mu, & h &= (1+2\lambda+2\mu,\, 4+3\lambda+\mu), \\
   n = 3:\quad x_3^{\mathrm{alt}} &= \bigl(2-3\mu,\, 3,\, 3-3\mu,\, 2,\, 3+2\lambda+4\mu,\, 3+3\lambda+2\mu\bigr), \\
   (z,A,B,C,D,q,r) &= \bigl(1,\, 4\mu,\, 0,\, 2,\, 0,\, 3+2\lambda+4\mu,\, 3+3\lambda+2\mu\bigr), & s_h &= 3\mu, & d_h &= 4, & h &= (2+4\mu,\, 3+4\mu).
   \end{aligned}$$
   On the entire 100-point synchronized tail ($B = D = 0$, $C \in \{2,3\}$, $z \in \{1,4\}$, $A = 2Cz\mu$, $r \in \mathbb{F}_5$, $q = z-A-r$), and for every $n \ge 3$:
   $$s_h(x) = B + 2A = 4Cz\mu \equiv -Cz\mu \pmod 5, \qquad d_h(x) = D + 2C = 2C \in \{4, 1\} \ne 0 \pmod 5,$$
   $$h(x) = \bigl(C(2z\mu + 1),\, C(2z\mu - 1)\bigr).$$
   Consequently:
   - at $n=0,2$ ($25$ blank points) and on the entire $100$-point synchronized tail ($n \ge 3$), $d_h(x) \in \{1,4\} \ne 0$, so **zero** blank points and **zero** tail points lie in $\mathcal{G}_0$ (even when $\mu = 0$, where $s_h = B+2A = 0$ vanishes, $d_h = 2C \ne 0$ keeps $h \in \{(3,2),(2,3)\} \ne (0,0)$);
   - at $n=1$ ($25$ first-message points), $(\lambda,\mu) \mapsto h(x_1^{\mathrm{alt}}(\lambda,\mu)) = (1+2\lambda+2\mu, 4+3\lambda+\mu)$ is an affine bijection $\mathbb{F}_5^2 \to \mathbb{F}_5^2$ ($\det\begin{pmatrix}2&2\\3&1\end{pmatrix} = -4 \equiv 1 \pmod 5$), attaining $h = (0,0)$ at **exactly one pair**, $(\lambda,\mu) = (2,0)$, where $x_1^{\mathrm{alt}}(2,0) = (2,1,2,1,1,3)$ ($z_1 = 0 \notin X_{14}$, $r_1 = 3 \ne 0$), which immediately exits $\mathcal{G}_0$ at $n=2$ since $h(x_2^{\mathrm{alt}}(2,0)) = (3,2) \ne (0,0)$.

3. **Registered one-shot source family $x_\lambda(0)$ and absence $x_{\mathrm{empty}}(0)$ (zero gate overlap iff $\lambda = 0$):**
   - For each occupied payload $\lambda \in \mathbb{F}_5$, from $x_\lambda(0) = (\lambda, 0, -\lambda, 0, 0, 0)$:
     $$\begin{aligned}
     n = 0:\quad x_\lambda(0) &= (\lambda, 0, -\lambda, 0, 0, 0), & z &= 0, & s_h &= 0, & d_h &= 4\lambda, & h &= (2\lambda, 3\lambda) = (2\lambda, -2\lambda), \\
     n = 1:\quad x_\lambda(1) &= (0, \lambda, 0, -\lambda, 0, 0), & z &= 0, & s_h &= 0, & d_h &= 2\lambda, & h &= (\lambda, 4\lambda) = (\lambda, -\lambda), \\
     n = 2:\quad x_\lambda(2) &= (2, 1+\lambda, 2, 1-\lambda, 1, 0), & z &= 2, & s_h &= 0, & d_h &= 2\lambda, & h &= (\lambda, 4\lambda) = (\lambda, -\lambda), \\
     n = 3:\quad x_\lambda(3) &= (0, -\lambda, 1, 3+\lambda, 1, 1), & z &= 1, & s_h &= 0, & d_h &= 3\lambda, & h &= (4\lambda, \lambda) = (-\lambda, \lambda).
     \end{aligned}$$
     Note (`R5`): at $n = 0$, $h(x_\lambda(0)) = (2\lambda, 3\lambda)$, whereas for all $n \ge 1$, $h(x_\lambda(n)) = (\pm\lambda, \mp\lambda)$. On the entire 100-state ready carrier graph ($B \in \{2,3\}$, $z \in \{1,4\}$, $A = 2B$, $C = 4Bz$, $D = -Bz(3-\lambda)$ for decoded payload $\lambda = 3 - BzD \in \mathbb{F}_5$, $r \in \mathbb{F}_5$, $q = z - 3B - r$):
     $$s_h(x) = B + 2A = 5B \equiv 0 \pmod 5, \qquad d_h(x) = D + 2C = -Bz(3-\lambda) - 2Bz \equiv Bz\lambda \pmod 5,$$
     $$h(x) = \bigl(-2Bz\lambda,\, 2Bz\lambda\bigr) \in \mathbb{F}_5^2.$$
     Since $2$ (at $n=0$) and $2Bz \in \{\pm 1\}$ (for $n \ge 1$ and on $Q$) are units in $\mathbb{F}_5$, $h(x) = (0,0) \iff \lambda = 0$ at $n = 0$, for every $n \ge 1$, and on all $100$ states of the ready carrier graph ($20/100$ states, all belonging to the single payload $\lambda = 0$). At $n = 3$ for $\lambda = 0$, $x_0(3) = (0,0,1,3,1,1)$ has $W(\pi_P(x_0(3))) = W(0,0,1,3) = (0,0,3,1) = \bar{y}_3 \in G_L$.
   - For the explicit absence preparation $x_{\mathrm{empty}}(0) = (0,0,1,0,0,0)$, $z_0 = 1 \in X_{14}$, $A_0 = 1$, $B_0 = 0$, and $h(x_{\mathrm{empty}}(0)) = (0,2)$. By Lemma D2.1 on $X_{14}$, for every $n \ge 0$,
     $$s_h\bigl(x_{\mathrm{empty}}(n)\bigr) = 2(-1)^n \in \{2,3\} \ne 0 \pmod 5, \qquad h\bigl(x_{\mathrm{empty}}(n)\bigr) \in \{(0,2),(0,3),(2,0),(3,0)\} \subset \mathbb{F}_5^2 \setminus \{(0,0)\}.$$
     Thus $x_{\mathrm{empty}}(n)$ never enters $\mathcal{G}_0$.

#### Proof of Theorem D2

- **Clause 1 ($E(\lambda,\mu)$):** The prefix coordinates at $n=0,1,2,3$ and the 500-point tail parameterization $z,A \in \{1,4\}$, $B=0$, $C = \lambda A/z = Az\lambda$, $D = \mu A/z = Az\mu$ are established in `U-ORIGIN-NONLINEAR-TWO-MESSAGE-READOUT`. Substituting these into $s_h = B+2A$, $d_h = D+2C$, and $h = (3(s_h+d_h), 3(s_h-d_h))$ gives the displayed expressions at $n=0,1,2,3$ and on the tail. Because $A \in \{1,3,4\}$ across all $550$ points while $B = 0$ at $n=0,2$ and $n \ge 3$ (with $A=1,4 \implies s_h = 2A \in \{2,3\}$) and $(A,B) = (3,2)$ at $n=1$ ($s_h = 2 + 6 \equiv 3$), $s_h(x) \in \{2,3\} \ne 0$ everywhere.
- **Clause 2 ($E_{\mathrm{alt}}(\lambda,\mu)$):** At $n=0$, $E_{\mathrm{alt}}(\lambda,\mu) = (3\mu, 3, 3\mu, 2, q_0, r_0)$ with $r_0 = 3(1+\mu-\lambda) = 3+2\lambda+3\mu$ and $q_0 = 2-\mu-r_0 = 4+3\lambda+\mu$ has $h(x_0) = (3+6\mu, 2+6\mu) \equiv (3+\mu, 2+\mu)$. Since $z_0 = 2$ and $\theta_0 = 0$, $x_1^{\mathrm{alt}} = g_2(x_0^{\mathrm{alt}}) = (2-3\mu, 2+2\lambda+3\mu, 2-3\mu, 3\lambda+2\mu, 2+2\lambda+4\mu, 2+3\lambda+2\mu)$, with $A_1 = (2-3\mu)+(2-3\mu) \equiv 4-\mu$, $B_1 = (2+2\lambda+3\mu)+(3\lambda+2\mu) \equiv 2$, $C_1 = 0-2 \equiv 3$, $D_1 = (2+2\lambda+3\mu)-(3\lambda+2\mu)-1 \equiv 1+4\lambda+\mu$, and $z_1 = A_1+B_1+q_1+r_1 = (4-\mu)+2+(2+2\lambda+4\mu)+(2+3\lambda+2\mu) \equiv 0 \pmod 5$. Applying Lemma D2.1 gives
  $$h_1(x_1^{\mathrm{alt}}) = -h_2(x_0^{\mathrm{alt}}) + r_0 = -(2+\mu) + (3+2\lambda+3\mu) \equiv 1 + 2\lambda + 2\mu \pmod 5,$$
  $$h_2(x_1^{\mathrm{alt}}) = -h_1(x_0^{\mathrm{alt}}) - r_0 = -(3+\mu) - (3+2\lambda+3\mu) \equiv 4 + 3\lambda + \mu \pmod 5.$$
  The linear system $2\lambda + 2\mu \equiv 4$, $3\lambda + \mu \equiv 1 \pmod 5$ has unique solution $\mu = 0, \lambda = 2$ since $\det\begin{pmatrix}2&2\\3&1\end{pmatrix} \equiv 1 \pmod 5$. At $n=2$, $z_1 = 0$ and $\theta_1 = 1$ select $g_2$, and since $g_2$ is an involution, $x_2^{\mathrm{alt}} = g_2(x_1^{\mathrm{alt}}) = x_0^{\mathrm{alt}}$. At $n=3$, $z_2 = 2$ and $\theta_2 = 1$ select $g_4$, giving $x_3^{\mathrm{alt}} = g_4(x_0^{\mathrm{alt}}) = (2-3\mu, 3, 3-3\mu, 2, 2-q_0, 1-r_0) = (2-3\mu, 3, 3-3\mu, 2, 3+2\lambda+4\mu, 3+3\lambda+2\mu)$ with $(z_3,A_3,B_3,C_3,D_3) = (1, 4\mu, 0, 2, 0)$ and $h(x_3^{\mathrm{alt}}) = (-h_1(x_2^{\mathrm{alt}}), -h_2(x_2^{\mathrm{alt}})) = (2+4\mu, 3+4\mu)$. On the 100-point tail (`U-ALTERNATIVE-AFFINE-SEMANTIC-READOUT`), $B = D = 0$, $C \in \{2,3\}$, $z \in \{1,4\}$, $A = 2Cz\mu$, so $d_h = D+2C = 2C \in \{4,1\} \ne 0$ and $h_1 = 3(2A+2C) = A+C = C(2z\mu+1)$, $h_2 = A-C = C(2z\mu-1)$.
- **Clause 3 ($x_\lambda(0)$ and $x_{\mathrm{empty}}(0)$):** Direct evaluation on the canonical table of `U-NATIVE-SOURCE-RECEIVER-RECORD` gives $h(x_\lambda(0)) = (2\lambda, 3\lambda)$ at $n=0$ and $h(x_\lambda(n)) = (\pm\lambda, \mp\lambda)$ for $n=1,2,3$. On the 100-state ready carrier graph ($B \in \{2,3\}$, $z \in \{1,4\}$, $p_1 = 1+B+2Bz$, $p_1' = -1+B-2Bz$), $A = p_1+p_1' = 2B$ and $C = p_1-p_1'-2 = 4Bz \equiv -Bz \pmod 5$. Since $B^2 = 4 \equiv -1$ and $z^2 = 1$, the payload relation $\lambda = 3 - BzD$ is equivalent to $D = -Bz(3-\lambda)$. Thus $s_h = B+2A = 5B \equiv 0$ and $d_h = D+2C = -Bz(3-\lambda) - 2Bz = -Bz(5-\lambda) \equiv Bz\lambda \pmod 5$, yielding $h_1 = 3d_h = -2Bz\lambda$ and $h_2 = -3d_h = 2Bz\lambda$. Since $2Bz \in \{\pm 1\}$, $h = (0,0) \iff \lambda = 0$. Finally, $x_{\mathrm{empty}}(0) = (0,0,1,0,0,0)$ has $z_0 = 1 \in X_{14}$ and $h(x_{\mathrm{empty}}(0)) = (0,2)$, and by Lemma D2.1 on $X_{14}$, $g_1, g_3, g_4$ map $(0,2)$ inside $\{(0,2),(0,3),(2,0),(3,0)\} \not\ni (0,0)$ for all $n \ge 0$. $\square$

---

## 3. Scoped Source-Blindness Composition and $W$ Relabeling vs Fixed-Marking Action (Question Q3)

### Theorem D3.1 (Scoped source-blindness composition through $(q,r)$ and $H_B$)

Let $\mathcal{R} = \mathbb{Q}^D \times \mathbb{Q}^D \times (\mathbb{Q}^4)^2 \times (\mathbb{Q}^4)^2 \times (\mathbb{Z}/2\mathbb{Z}) \times ([0,B]\cap\mathbb{Q}) \times \mathbb{Q} \times \{+1,-1\}$ be the complete occupied rational receiver carrier of `SIGNED-PORT-OCCUPIED-REVERSIBILITY` and `FUNDED-CONTACT-INVOLUTION` on the 705-site Dirichlet domain $D = Y + B_\star + B_\star \subset D_3$, with wave/tape bijection $F_{\mathrm{wave}}: \mathcal{R} \to \mathcal{R}$ (fixing $(e, w_{\mathrm{led}}, \sigma)$) and funded contact involution $H_B^{(q,r)}: \mathcal{R} \to \mathcal{R}$ driven by $a(q,r) = S\eta(q,r)$.

1. **Invariance on the original 550-point family $E(\lambda,\mu)$:**
   For every $(\lambda,\mu) \in \mathbb{F}_5^2$ and every integer $n \ge 0$, the native trajectory $x_n(\lambda,\mu)$ starting at $E(\lambda,\mu)$ has $(\lambda,\mu)$-independent trace and reference coordinates:
   $$\bigl(z_n(\lambda,\mu),\, q_n(\lambda,\mu),\, r_n(\lambda,\mu)\bigr) = \bigl(z_n(0,0),\, q_n(0,0),\, r_n(0,0)\bigr),$$
   and hence $(\lambda,\mu)$-independent contact vector $a(q_n(\lambda,\mu), r_n(\lambda,\mu)) = a(q_n(0,0), r_n(0,0)) \in \mathbb{Q}^D$.
   Consequently, for any common initial receiver state $Y_0 \in \mathcal{R}$ (independent of $(\lambda,\mu)$) and any source-independent schedule $\mathcal{S} = (M_1, \dots, M_m)$ where each step $M_t$ is $F_{\mathrm{wave}}$, $F_{\mathrm{wave}}^{-1}$, or $H_B^{(q_{n_t}, r_{n_t})}$ at a schedule-specified checkpoint index $n_t \ge 0$, the resulting complete receiver trajectory satisfies
   $$Y_t(\lambda,\mu) = Y_t(0,0) \qquad \text{for all } (\lambda,\mu) \in \mathbb{F}_5^2 \text{ and all } 0 \le t \le m.$$
   Every function of $(Y_0, Y_1, \dots, Y_m)$ (including wave amplitudes $(u,v)$, outgoing tape records, store $e$, ledger $w_{\mathrm{led}}$, and direction $\sigma$) is therefore constant across all $25$ message pairs $(\lambda,\mu) \in \mathbb{F}_5^2$.

2. **Exact scope comparison with $x_\lambda(0)$ and $E_{\mathrm{alt}}(\lambda,\mu)$:**
   - Across the five occupied payloads $\lambda \in \mathbb{F}_5$ of $x_\lambda(0) = (\lambda,0,-\lambda,0,0,0)$, $(z_0, q_0, r_0) = (0,0,0)$ is also independent of $\lambda$, so $(z_n, q_n, r_n)$ and the composed receiver trajectory $Y_t(\lambda)$ under any common $Y_0 \in \mathcal{R}$ and source-independent schedule $\mathcal{S}$ are identical for all $\lambda \in \mathbb{F}_5$. (By contrast, the sixth absence codeword $x_{\mathrm{empty}}(0) = (0,0,1,0,0,0)$ starts at $(z_0, q_0, r_0) = (1,0,0)$, sharing $(q_0,r_0)=(0,0)$ with $x_\lambda(0)$ at $n=0$ but diverging in trace $z_0$ and hence in $(q_2, r_2) = (0,0) \ne (1,0)$; thus common $(q_0,r_0)$ alone without common $z_0$ is not sufficient for identical $(q_n,r_n)$ or $Y_t$.)
   - On $E_{\mathrm{alt}}(\lambda,\mu)$, the initial map $(\lambda,\mu) \mapsto (q_0, r_0) = (4+3\lambda+\mu, 3+2\lambda+3\mu)$ has determinant $9 - 2 = 7 \equiv 2 \ne 0 \pmod 5$ and is a bijection $\mathbb{F}_5^2 \to \mathbb{F}_5^2$. Since $z_0 = 2$ is common and each generator acts on $(q,r)$ by an affine bijection determined by $z_n$, the map $(\lambda,\mu) \mapsto (q_n, r_n)$ and the contact source $(\lambda,\mu) \mapsto a(q_n, r_n)$ are bijections of $\mathbb{F}_5^2$ onto the $25$-element source set $\{S\eta(q,r) : (q,r) \in \mathbb{F}_5^2\}$ at every $n \ge 0$. This occurs because $E_{\mathrm{alt}}$ prepares $(\lambda,\mu)$ directly inside the initial reference registers $(q_0, r_0)$.

#### Proof of Theorem D3.1

1. At $n=0$, $E(\lambda,\mu) = (3(\lambda+3), 3(\mu+1), 3(-\lambda-1), 3(-\mu-1), 0, 1)$ has $z_0 = 3(2) + 3(0) + 0 + 1 \equiv 2 \pmod 5$ and $(q_0, r_0) = (0,1)$, independent of $(\lambda,\mu)$. By `CONTRACT.md` Section 1.1, the quotient $\pi_{z,q,r}(x) = (z,q,r)$ satisfies $\pi_{z,q,r}(g_j x) = \bar{g}_j(\pi_{z,q,r}(x))$ where $\bar{g}_j(z,q,r)$ depends only on $(z,q,r)$. If $(z_n, q_n, r_n)$ is independent of $(\lambda,\mu)$, then $j_n = z_n + 2\theta_n \bmod 5$ and $(z_{n+1}, q_{n+1}, r_{n+1}) = \bar{g}_{j_n}(z_n, q_n, r_n)$ are independent of $(\lambda,\mu)$. Induction on $n \ge 0$ proves $(z_n, q_n, r_n)$ is independent of $(\lambda,\mu)$ for all $n \ge 0$.
   In `FUNDED-CONTACT-INVOLUTION`, $H_B^{(q,r)}$ is a deterministic total map on $\mathcal{R}$ parameterized solely by $a(q,r) = S\eta(q,r)$, and $F_{\mathrm{wave}}, F_{\mathrm{wave}}^{-1}$ are deterministic total maps on $\mathcal{R}$ with no dependence on $x_n$. Induction on the schedule index $t \in \{0, \dots, m\}$ from common $Y_0(\lambda,\mu) = Y_0$ proves $Y_t(\lambda,\mu) = Y_t(0,0)$ for all $t$ and all $(\lambda,\mu) \in \mathbb{F}_5^2$.
2. For $x_\lambda(0)$, $(z_0, q_0, r_0) = (0,0,0)$ is constant over $\lambda \in \mathbb{F}_5$, so the identical induction applies over $\lambda \in \mathbb{F}_5$. For $x_{\mathrm{empty}}(0)$, $(z_0, q_0, r_0) = (1,0,0)$ gives $(z_1, q_1, r_1) = \bar{g}_1(1,0,0) = (4,0,0)$ and $(z_2, q_2, r_2) = \bar{g}_1(4,0,0) = (1,0,0)$, whereas $x_\lambda(2)$ has $(z_2, q_2, r_2) = (2,1,0)$ (at $n=2$, from a common blank receiver with $\sigma=+1$ and $e=B=1$, $\eta(1,0) = (1/2, 1/2, 0, 0)$ has cost $\frac{1}{2}\|S\eta(1,0)\|^2 = 3/20$ and $\eta(0,0) = (0, 1/2, 0, 0)$ has cost $1/10$, so both contacts accept and write distinct waves `R7`).
   For $E_{\mathrm{alt}}(\lambda,\mu)$, $z_0 = 2$ is independent of $(\lambda,\mu)$, so $z_n$ and the selected sequence of generators $g_{j_n}$ are common to all $25$ pairs. Since each $\bar{g}_j$ restricts at fixed $z$ to an affine bijection of $(q,r) \in \mathbb{F}_5^2$, composition with the initial bijection $(\lambda,\mu) \mapsto (q_0, r_0)$ is a bijection $\mathbb{F}_5^2 \to \mathbb{F}_5^2$ at every $n \ge 0$, and injectivity of $(q,r) \mapsto S\eta(q,r)$ (Theorem D1) makes $(\lambda,\mu) \mapsto a(q_n, r_n)$ bijective onto the $25$ contact vectors at every $n \ge 0$. $\square$

---

### Theorem D3.2 (Coordinate relabeling by $W$ vs fixed-marking action of $W$ on $H(y)$)

On $\mathbb{Z}^4$, let $W(y_0, y_1, y_2, y_3)^T = (y_1, y_0, y_3, y_2)^T$ ($W^T = W^{-1} = W$) and let $B_f, A_f, L, H(y) = \frac{1}{2}y^T B_f y$ be the canonical field-cell objects of `FIELD-CONSERVATIVE-CHAIN-LAW` Shared proof 2.

1. **Passive coordinate relabeling (`R3` corrected for $\widetilde{A}_f = W A_f W$):**
   Setting $\tilde{y} = W y$ while transforming the metric, step, and shell matrices to
   $$\widetilde{B}_f = W^T B_f W = \begin{pmatrix} 6 & -2 & 3 & -1 \\ -2 & 4 & -1 & 2 \\ 3 & -1 & 2 & 0 \\ -1 & 2 & 0 & 2 \end{pmatrix}, \quad
   \widetilde{A}_f = W A_f W = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ -3 & 1 & -2 & 1 \\ 1 & -2 & 1 & -1 \end{pmatrix}, \quad
   \widetilde{L} = W L W = \begin{pmatrix} 4 & -3 & 1 & -2 \\ -3 & 1 & -2 & -1 \\ -5 & 5 & -1 & 2 \\ 5 & 0 & 2 & 1 \end{pmatrix}$$
   preserves $\widetilde{H}(\tilde{y}) := \frac{1}{2}\tilde{y}^T \widetilde{B}_f \tilde{y} = H(y)$ by simultaneously changing the quadratic form and the active-field embedding $P \mapsto P W$. (In `e3d35709a86b42c21c1bf57e2be2b3a3cf707598`, the top-right $2 \times 2$ block of $\widetilde{A}_f = W A_f W$ was erroneously printed as $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ instead of $\begin{pmatrix}0&1\\1&0\end{pmatrix} I_2 \begin{pmatrix}0&1\\1&0\end{pmatrix} = I_2 = \begin{pmatrix}1&0\\0&1\end{pmatrix}$; on $e_2 = (0,0,1,0)^T$, $W A_f W e_2 = (1,0,-2,1)^T$, not $(0,1,-2,1)^T$; see `ERRATA.md` R3.)

2. **Active state map in the fixed canonical marking $H(y) = \frac{1}{2}y^T B_f y$:**
   With $B_f, A_f, L, H$ held fixed, $W$ is **not** an $H$-isometry, does not commute with $A_f$ or $L$, and does not preserve $L\mathbb{Z}^4$. For every $y = (y_0, y_1, y_2, y_3)^T \in \mathbb{Z}^4$, the exact energy difference is
   $$H(W y) - H(y) = \frac{1}{2} y^T (W^T B_f W - B_f) y = y_0^2 - y_1^2 + y_0 y_2 - y_1 y_3,$$
   where
   $$W^T B_f W - B_f = \begin{pmatrix} 2 & 0 & 1 & 0 \\ 0 & -2 & 0 & -1 \\ 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \end{pmatrix} \ne 0.$$
   In particular:
   - on $e_0 = (1,0,0,0)^T$, $W e_0 = e_1 = (0,1,0,0)^T$, with
     $$H(e_0) = 2, \qquad H(W e_0) = 3, \qquad H(W e_0) - H(e_0) = 1 \ne 0;$$
   - on the unit seed $u_\star = (0,-1,-1,2)^T$, $W u_\star = (-1,0,2,-1)^T$, with
     $$H(u_\star) = 1, \qquad H(W u_\star) = 2, \qquad H(W u_\star) - H(u_\star) = 1 \ne 0;$$
   - on $y_- = (0,0,1,-2)^T$, $W y_- = (0,0,-2,1)^T = L u_\star$, where $y_- \notin L\mathbb{Z}^4$ ($y_2+2y_3 = -3 \not\equiv 0 \pmod 5$) whereas $W y_- \in L\mathbb{Z}^4$ ($-2+2(1)=0$), both having $H(y_-) = H(W y_-) = 5$.

#### Proof of Theorem D3.2

Expanding $H(y) = 2y_0^2 - 2y_0 y_1 + 3y_1^2 + y_2^2 + y_3^2 + 2y_0 y_2 - y_0 y_3 - y_1 y_2 + 3y_1 y_3$ at $W y = (y_1, y_0, y_3, y_2)^T$ gives
$$H(W y) = 2y_1^2 - 2y_1 y_0 + 3y_0^2 + y_3^2 + y_2^2 + 2y_1 y_3 - y_1 y_2 - y_0 y_3 + 3y_0 y_2.$$
Subtracting $H(y)$ cancels $-2y_0 y_1 + y_2^2 + y_3^2 - y_0 y_3 - y_1 y_2$ and leaves $(3-2)y_0^2 + (2-3)y_1^2 + (3-2)y_0 y_2 + (2-3)y_1 y_3 = y_0^2 - y_1^2 + y_0 y_2 - y_1 y_3$. Evaluating at $e_0 = (1,0,0,0)^T$, $u_\star = (0,-1,-1,2)^T$, and $y_- = (0,0,1,-2)^T$ yields the stated values. $\square$

---

## 4. Complete Assumption Table and Smallest Unresolved Interface Obligation (Question Q4)

### Table D4.1: Complete Assumption and Boundary Comparison (`R4`, `R5`, `R7` qualifiers restored)

| Interface Requirement | Original 550-point $E(\lambda,\mu)$ | Alternative 150-point $E_{\mathrm{alt}}(\lambda,\mu)$ | One-shot $x_\lambda(0)$ & $x_{\mathrm{empty}}(0)$ | Integer Field Chain (`FIRST-WORK`) | Rational Contact $H_B$ (`FUNDED-CONTACT`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Native origin-zero preparation** | $25$ pairs, $(z_0,q_0,r_0)=(2,0,1)$ fixed | $25$ pairs, $z_0=2$, $(q_0,r_0)$ bijective with $(\lambda,\mu)$ | $5$ occupied $\lambda$ ($z_0=0, q_0=r_0=0$) + $1$ absence ($z_0=1, q_0=r_0=0$) | Not a native $U$ trajectory; takes $y=Lw \in L\mathbb{Z}^4$ | Not a native $U$ trajectory; takes $(q,r)\in\mathbb{F}_5^2$ |
| **Common initial raw receiver** | Yes for $(q,r)=(0,1)$ and $\Phi$-port $(2,0)$; No for quadratic $(0,\mu)$ | No: raw blank is $(\mu,0)$ and $(q_0,r_0)$ depends on $(\lambda,\mu)$ | Yes: $R_{\mathrm{reg}}(0)=(0,0,0,0)$ is common across all $\lambda$ and $x_{\mathrm{empty}}$ | Yes: receiver cell $(R,0,0,0)$ and $p=0$ | Assumed as hypothesis $Y_0 \in \mathcal{R}$ |
| **Zero-gate admission $h(x)=(0,0)$** | **$0/550$ points** ($s_h = B+2A \in \{2,3\} \ne 0$ for all $n \ge 0$) | **$1/150$ points** (only $(\lambda,\mu)=(2,0)$ at $n=1$); **$0/100$ tail points** ($d_h = 2C \in \{1,4\} \ne 0$) | **Iff $\lambda = 0$** ($h=(2\lambda,3\lambda)$ at $n=0$ and $h = (\pm\lambda, \mp\lambda)$ for $n\ge 1$; $20/100$ ready states); $x_{\mathrm{empty}}$ has $0$ hits | Required for source acceptance ($y \in L\mathbb{Z}^4 \iff (y\bmod 5)\in G_L \iff h_P(W(y\bmod 5))=(0,0)$) | Not gated by $h(x)$; accepts iff $0 \le e - \Delta_\sigma \le B$ |
| **Retained message in $h(x)$ on $X_{14}$ at fixed common time / carrier context** | $5$ classes ($2\lambda+\mu \bmod 5$) at fixed common $n \ge 3$ (or fixed $(A,z)$); not stationary across $z\in\{1,4\}$, all outside $\mathcal{G}_0$ | $5$ classes ($\mu \bmod 5$) at fixed common $n \ge 3$ (or fixed $(C,z)$); not stationary across $z\in\{1,4\}$, all outside $\mathcal{G}_0$ | $5$ classes ($\lambda \bmod 5$) at fixed common $n \ge 3$ (or fixed $(B,z)$); not stationary across $(B,z)\in\{2,3\}\times\{1,4\}$, only $\lambda=0$ in $\mathcal{G}_0$ | Only $1$ residue ($\bar{y}_3=(0,0,3,1)\in G_L$) reached by $W(\pi_P(x_0(3)))$ | None ($H_B$ reads $(q,r)$, not $h$) |
| **Retained message in $(q_n, r_n)$** | **$1$ class** (blind to both $\lambda$ and $\mu$ for all $n \ge 0$) | **$25$ classes** at each fixed $n\ge 0$ (bijective with $(\lambda,\mu)$ because preloaded in $(q_0,r_0)$) | **$1$ class** across $\lambda \in \mathbb{F}_5$ (blind to $\lambda$ for all $n \ge 0$; diverges from $x_{\mathrm{empty}}$ at $n=2$ since $z_0$ differs) | Not applicable (no $(q,r)$ register) | $H_B$ trajectory depends on $x_n$ solely through $(q_n,r_n)$ |
| **Downstream receiver message distinction** | Native readers recover $(\lambda,\mu)$; $H_B$ via $(q,r)$ recovers **nothing** ($1$ class) under common $Y_0$ and common schedule $\mathcal{S}$ | Native reader recovers $(\lambda,\mu)$; $H_B$ sees $(q_n,r_n)$ only because initial receiver was not common | Native reader $R_{\mathrm{reg}}$ recovers $\lambda$ and `BLANK` on $x_{\mathrm{empty}}$; $H_B$ via $(q,r)$ is blind across $\lambda\in\mathbb{F}_5$ | Neutral work channel & pointer $p \in C_5$ record $1$ bit (`HIT` vs `BLANK`), blind across unit seeds $H(w)=1$ | $Y_t$ is identical when $(z_0,q_0,r_0)$ (hence all $(q_n,r_n)$), complete $Y_0\in\mathcal{R}$, and schedule $\mathcal{S}$ are common |

### Theorem D4.2 (Synchronized zero-gate sheet, $625$-point three-step preimage, and smallest unresolved interface obligation)

Within the frozen v102 definitions, the piston projection $\pi_P(a,b,c,d,q,r) = (a,b,c,d)$, the piston kernel $K = \ker(h_P) \subset \mathbb{F}_5^4$, and the $W$-piston comparison map $W(p_1,p_4,p_1',p_4') = (p_4,p_1,p_4',p_1')$ with $W(K) = G_L = L\mathbb{Z}^4 \bmod 5$:
1. On the synchronized zero-gate sheet $\mathcal{G}_0 \cap X_{14} = \{x \in \mathbb{F}_5^6 : z(x) \in \{1,4\},\, h(x) = (0,0)\}$, the defining equations $B + 2A = 0$ and $D + 2C = 0$ are equivalent to
   $$B = 3A \pmod 5, \qquad D = 3C \pmod 5,$$
   comprising $2 \times 25 \times 5 = 250$ checkpoints ($125$ on $X_1$ with $z=1$ and $125$ on $X_4$ with $z=4$). On $\mathcal{G}_0 \cap X_{14}$, the protected vector $V(x) = (A, B, zC, zD)$ has the two-parameter form
   $$V(x) = (A,\, 3A,\, zC,\, 3zC) \in K \subset \mathbb{F}_5^4, \qquad (A, zC) \in \mathbb{F}_5^2$$
   ($25$ protected vectors, $13$ sign fibres $\{V, -V\}$), while the $W$-piston residue is
   $$W(\pi_P(x)) = \bigl(3(3A+3C+1),\, 3(A+C+2),\, 3(3A-3C-1),\, 3(A-C-2)\bigr) \in G_L, \qquad (A, C) \in \mathbb{F}_5^2$$
   (mapping $(A,C) \in \mathbb{F}_5^2$ bijectively onto the $25$ shell residues of $G_L = W(K)$). Across $z \in \{1,4\}$, $W(\pi_P(x))$ depends on $(A,C)$ rather than on $V(x) = (A,3A,zC,3zC)$ alone whenever $C \ne 0$ (`R4`: for example, $x = (4,2,1,3,0,1)$ with $z=1, A=0, C=1$ and $x' = (3,4,2,1,0,4)$ with $z=4, A=0, C=4$ share $V(x) = V(x') = (0,0,1,3)$ but have $W(\pi_P(x)) = (2,4,3,1) \ne (4,3,1,2) = W(\pi_P(x'))$).
2. None of the three inherited v102 families realizes two or more distinct messages inside $\mathcal{G}_0 \cap X_{14}$: $E(\lambda,\mu)$ has $B=0, A \in \{1,4\}$ ($0$ points in $\mathcal{G}_0 \cap X_{14}$); $E_{\mathrm{alt}}(\lambda,\mu)$ has $B=D=0, C \in \{2,3\}$ ($0$ points in $\mathcal{G}_0 \cap X_{14}$); and $x_\lambda(3)$ has $(A,B,C,D) = (1, 3, 2, 1-2\lambda)$, which satisfies $B = 3A$ for all $\lambda$ but satisfies $D = 3C \equiv 1 \iff \lambda = 0$, admitting only the single message $\lambda = 0$ (where $V(x_0(3)) = (1,3,2,1) \in K$ and $W(\pi_P(x_0(3))) = (0,0,3,1) = \bar{y}_3 \in G_L$).
3. **Exact three-step preimage cardinality (`R1`, corrected from $250$ to $625$):**
   Under the driver prefix $\theta_0\theta_1\theta_2 = 011$, the trace quotient maps $f_0 = (0,4,0,4,4)$ and $f_1 = (2,1,1,3,1)$ send every initial trace $z_0 \in \mathbb{F}_5$ to $z_3 = f_1(f_1(f_0(z_0))) = 1$ via $(0 \mapsto 0 \mapsto 2 \mapsto 1)$, $(1 \mapsto 4 \mapsto 1 \mapsto 1)$, $(2 \mapsto 0 \mapsto 2 \mapsto 1)$, $(3 \mapsto 4 \mapsto 1 \mapsto 1)$, and $(4 \mapsto 4 \mapsto 1 \mapsto 1)$. On each initial trace sheet $X_{z_0} = \{x \in \mathbb{F}_5^6 : z(x) = z_0\}$ ($|X_{z_0}| = 3125$), $T_1 \circ T_1 \circ T_0|_{X_{z_0}}$ is a fixed composition of three affine bijections onto $X_1$. Therefore:
   - $T_1 \circ T_1 \circ T_0: \mathbb{F}_5^6 \to X_1$ is globally **$5$-to-$1$ onto $X_1$**, and no checkpoint with $z_3 = 4$ is reachable at $n=3$;
   - of the $250$-point target $\mathcal{G}_0 \cap X_{14}$, only the **$125$-point sheet $\mathcal{G}_0 \cap X_1$** ($z_3 = 1, B_3 = 3A_3, D_3 = 3C_3$) is reachable at $n=3$ (where $V(x_3) = (A_3, 3A_3, C_3, 3C_3)$ and $W(\pi_P(x_3)) \in G_L$ are both parametrized bijectively by $(A_3, C_3) \in \mathbb{F}_5^2$);
   - the three-step preimage at $n=0$ has exact cardinality
     $$|\mathcal{P}_{\mathrm{gate}}| = \bigl|(T_1 \circ T_1 \circ T_0)^{-1}(\mathcal{G}_0 \cap X_{14})\bigr| = \bigl|(T_1 \circ T_1 \circ T_0)^{-1}(\mathcal{G}_0 \cap X_1)\bigr| = 5 \times 125 = 625$$
     ($125$ checkpoints on each of the five initial trace sheets $X_0, \dots, X_4$).
4. **Smallest unresolved interface obligation:**
   For the unchanged original family $E(\lambda,\mu)$, both the shell gate ($0/550$ points in $\mathcal{G}_0$) and the $(q,r)$-fed rational contact $H_B$ (identical $(q_n,r_n)$ across all $25$ pairs) are strictly obstructed. Closing a positive source-to-contact interface in a separately scoped future lane requires specifying an explicit source-access, receiver-preparation, funding, timing, and readout contract that states which current restriction changes. On the native shell-gate side, the minimal unresolved mathematical question is:
   > *Within the $625$-point three-step preimage $\mathcal{P}_{\mathrm{gate}} = (T_1 \circ T_1 \circ T_0)^{-1}(\mathcal{G}_0 \cap X_1) \subset \mathbb{F}_5^6$ (or on a single fixed initial trace sheet $X_{z_0}$ of size $125$ inside $\mathcal{P}_{\mathrm{gate}}$), for a single explicitly chosen initial receiver projection $R_{\mathrm{init}}$ (fixing either $R_{\mathrm{reg}}(x(0)) = (b_0, d_0, q_0, r_0)$ or $(z_0, q_0, r_0)$ rather than treating them as interchangeable), what is the exact number of distinct protected sign fibres $\{V(x_3), -V(x_3)\}$ in the $125$-point reachable sheet $\mathcal{G}_0 \cap X_1$ attainable at $n=3$, and can such a family be coupled to a declared contact/readout law without preloading the message into the initial receiver?*

#### Separately Scoped Next-Experiment Description (Not Executed Here)

If authorized as a separate future L1 probe or note, compute and prove by exact symbolic inversion of $T_1 \circ T_1 \circ T_0$ on each of the five initial trace sheets $X_{z_0}$ ($z_0 \in \mathbb{F}_5$) the complete **$625$-point preimage** (`R1`, corrected from $250$)
$$\mathcal{P}_{\mathrm{gate}} := (T_1 \circ T_1 \circ T_0)^{-1}(\mathcal{G}_0 \cap X_{14}) = (T_1 \circ T_1 \circ T_0)^{-1}(\mathcal{G}_0 \cap X_1) \subset \mathbb{F}_5^6 \qquad (|\mathcal{P}_{\mathrm{gate}}| = 5 \times 125 = 625),$$
and separately classify its fibres over (i) fixed $R_{\mathrm{reg}}(x(0)) = (b_0, d_0, q_0, r_0) \in \mathbb{F}_5^4$ and (ii) fixed $(z_0, q_0, r_0) \in \mathbb{F}_5^3$, determining the exact image in $\mathcal{G}_0 \cap X_1$ and in the $13$ protected sign fibres $\{V(x_3), -V(x_3)\}$. Even where multiple sign fibres are reached in $\mathcal{G}_0 \cap X_1$, that preimage classification establishes only native gate admission and does not by itself supply distinct contact inputs, funding, or receiver outputs without a separately declared contact and readout contract. $\square$

---

## 5. Errata and Review Reconciliation Ledger (`R1`–`R7`)

In response to the independent review `C-V103-SOURCE-INTERFACE-REVIEW-N` (`Codex-v103-RD-20261016`, issue [#1560](https://github.com/mathorn1973/twist-j/issues/1560), PR [#1563](https://github.com/mathorn1973/twist-j/pull/1563), commit `2a43c0312af7189b84c099c9482b908ac8e9323b`), the following seven items from the frozen specification `9cb2b7d89eb1fc955fb67e886e46a379cb1aba43` and initial result commit `e3d35709a86b42c21c1bf57e2be2b3a3cf707598` are explicitly recorded and reconciled (full proofs in `ERRATA.md`):

1. **`R1` (`e3d35709` lines 238, 242–244):** Replaced the false cardinality $250$ for $\mathcal{P}_{\mathrm{gate}} = (T_1 \circ T_1 \circ T_0)^{-1}(\mathcal{G}_0 \cap X_{14})$ by the exact cardinality **$625 = 5 \times 125$**, distinguishing the $250$-point two-sheet target $\mathcal{G}_0 \cap X_{14}$, its $125$-point reachable sheet $\mathcal{G}_0 \cap X_1$ at $n=3$ ($z_3 = 1$, since $f_1(f_1(f_0(z_0))) = 1$ for all $z_0 \in \mathbb{F}_5$), and its $625$-point three-step preimage ($125$ points on each initial trace sheet $X_{z_0}$).
2. **`R2` (`e3d35709` lines 119–120):** Replaced the flawed affine tuples of $E_{\mathrm{alt}}(\lambda,\mu)$ at $n=1$ (was $(0, 4\mu, 4, 3, 2+2\lambda+3\mu, 2+2\lambda+4\mu, 2+3\lambda+2\mu)$) and $n=3$ (was $(1, 4\mu, 0, 2, 0, 3+2\lambda, 3+3\lambda+\mu)$) by the exact trajectories $(0, 4-\mu, 2, 3, 1+4\lambda+\mu, 2+2\lambda+4\mu, 2+3\lambda+2\mu)$ at $n=1$ and $(1, 4\mu, 0, 2, 0, 3+2\lambda+4\mu, 3+3\lambda+2\mu)$ at $n=3$.
3. **`R3` (`e3d35709` line 190):** Corrected the top-right $2 \times 2$ block of $\widetilde{A}_f = W A_f W$ from $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ to $\begin{pmatrix}1&0\\0&1\end{pmatrix}$.
4. **`R4` (`e3d35709` lines 25, 222, 234):** Separated the piston projection $\pi_P(x) = (a,b,c,d)$, the piston kernel $K = \ker(h_P) = \{(a,3a,c,3c)\}$, the shell residue subgroup $G_L = L\mathbb{Z}^4 \bmod 5 = \{(3y_1,y_1,3y_3,y_3)\} = W(K)$ ($K \ne G_L$), the integer field shell condition $y \in L\mathbb{Z}^4 \iff h_P(W(y \bmod 5)) = (0,0)$, and the distinction on $\mathcal{G}_0 \cap X_{14}$ between $V(x) = (A,3A,zC,3zC)$ and $W(\pi_P(x)) \in G_L$.
5. **`R5` (`e3d35709` line 222):** Separated $h(x_\lambda(0)) = (2\lambda, 3\lambda)$ at $n=0$ from $h(x_\lambda(n)) = (\pm\lambda, \mp\lambda)$ for $n \ge 1$.
6. **`R6` (`CONTRACT.md` line 107):** Explicitly recorded that the literal parenthetical clause `h_1 = B+2A` in `CONTRACT.md` line 107 is **refuted** on $\mathbb{F}_5^6$ ($h_1(E(0,0)) = 1 \ne 2 = B+2A$), while the gate sum $s_h = h_1 + h_2 = B+2A \in \{2,3\} \ne 0$ retains the `#1548` gate-sum obstruction.
7. **`R7` (`e3d35709` lines 223, 225):** Restored the fixed-common-time / fixed-carrier-context qualifier on the $5$ message classes of $h(x)$ on $X_{14}$ and the full hypothesis $(z_0, q_0, r_0)$, $Y_0 \in \mathcal{R}$, and common schedule $\mathcal{S}$ for rational receiver trajectory equality in Table D4.1.

