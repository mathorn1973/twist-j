# Five-source predictive separation, calibration-to-prediction transport, and the classical-clone boundary

**NON-CANONICAL / conditional candidate-T and candidate-D / L1 analytical proof.**
Original work Apache-2.0, A. M. Thorn, 2026-10-14.
Reservation: [#1500](https://github.com/mathorn1973/twist-j/issues/1500), dispatched under [#1497](https://github.com/mathorn1973/twist-j/issues/1497).
Contract and preregistration pin: `274a88757863f55a838068e92241af1ee23f2de4` ([CONTRACT.md](CONTRACT.md), [PREREG.md](PREREG.md), [SOURCES.json](SOURCES.json)).

All derivations in this document are exact symbolic L1 proofs over $\mathbb{F}_5$ and $\mathbb{Q}$, written after public push and exact-byte readback of `274a88757863f55a838068e92241af1ee23f2de4`. No scientific verifier, numerical solver, or laboratory measurement was executed (`AUTHORED_PROOF`, `SELF_REVIEWED`, `NOT_INDEPENDENTLY_REVIEWED`).

---

## 1. Resolution of the preparation mismatch and rank-two source certificate (Obligation A)

### 1.1 Exact linear and affine span of the native-induced source set $Z_5$

Recall from `CONTRACT.md` Section 1.3 that for every native preparation $p \in \mathbb{F}_5^4$ with initial state $(0; (p, 0, 1))$ and residue sum $h(p) = \sum_{i=0}^3 p_i \pmod 5$, the first native tick $0 \to 1$ ($\theta_0 = 0$) produces the five receiver pairs

$$
C_1(0) = (0,4),\quad C_1(1) = (1,4),\quad C_1(2) = (1,0),\quad C_1(3) = (2,0),\quad C_1(4) = (0,1).
$$

Under the balanced lift $\ell(0,1,2,3,4) = (0,1,2,-2,-1)$ and map $\eta(q,r) = (\ell(q)/2, (\ell(r)+1)/2, 0, 0)$, the induced classical source set in $h$-order is

$$
Z_5 = \bigl\{z^{(0)}, z^{(1)}, z^{(2)}, z^{(3)}, z^{(4)}\bigr\}
= \left\{
(0,0,0,0),\;
\left(\tfrac{1}{2},0,0,0\right),\;
\left(\tfrac{1}{2},\tfrac{1}{2},0,0\right),\;
\left(1,\tfrac{1}{2},0,0\right),\;
(0,1,0,0)
\right\} \subset Z_{\mathrm{op}} \subset \mathbb{Q}^4. \tag{A1}
$$

**Theorem A1 (Rank-two native source span and full-receiver containment).**
Let $\Pi_2 := \mathbb{Q}e_0 \oplus \mathbb{Q}e_1 = \{(z_0, z_1, 0, 0) : z_0, z_1 \in \mathbb{Q}\} \subset \mathbb{Q}^4$. Then:

1. $\operatorname{span}_{\mathbb{Q}}(Z_5) = \operatorname{aff}_{\mathbb{Q}}(Z_5) = \Pi_2$, and $\dim_{\mathbb{Q}}\operatorname{span}_{\mathbb{Q}}(Z_5) = 2$.
2. The five vectors of $Z_5$ satisfy the exact $\mathbb{Q}$-linear basis relations
   $$
   e_0 = 2 z^{(1)}, \qquad e_1 = z^{(4)}, \qquad
   z^{(0)} = 0, \qquad
   z^{(2)} = z^{(1)} + \tfrac{1}{2}z^{(4)}, \qquad
   z^{(3)} = 2z^{(1)} + \tfrac{1}{2}z^{(4)} = z^{(1)} + z^{(2)}. \tag{A2}
   $$
3. Every pair of nonzero vectors $\{z^{(a)}, z^{(b)}\} \subset Z_5 \setminus \{z^{(0)}\}$ ($1 \le a < b \le 4$, all $\binom{4}{2} = 6$ pairs) is linearly independent over $\mathbb{Q}$ and spans $\Pi_2$.
4. Even over the entire $25$-state receiver carrier $\mathbb{F}_5^2$, the image of $\eta$ is
   $$
   \eta(\mathbb{F}_5^2) = \left\{-1, -\tfrac{1}{2}, 0, \tfrac{1}{2}, 1\right\} \times \left\{-\tfrac{1}{2}, 0, \tfrac{1}{2}, 1, \tfrac{3}{2}\right\} \times \{0\} \times \{0\} \subset \Pi_2,
   $$
   so no change of native initial checkpoint $x_0 \in \mathbb{F}_5^6$, waiting tick $n$, or generator word can produce a nonzero $e_2$ or $e_3$ source component through the fixed map $\eta$.

**Proof.**
By definition of $\eta$, the third and fourth coordinates of $\eta(q,r)$ vanish for every $(q,r) \in \mathbb{F}_5^2$, establishing $\eta(\mathbb{F}_5^2) \subset \Pi_2$ and hence $\operatorname{span}_{\mathbb{Q}}(Z_5) \subseteq \Pi_2$. Conversely, $z^{(1)} = \frac{1}{2}e_0 \in Z_5$ and $z^{(4)} = e_1 \in Z_5$ give $e_0 = 2z^{(1)} \in \operatorname{span}_{\mathbb{Q}}(Z_5)$ and $e_1 = z^{(4)} \in \operatorname{span}_{\mathbb{Q}}(Z_5)$, so $\Pi_2 \subseteq \operatorname{span}_{\mathbb{Q}}(Z_5)$ and $\dim_{\mathbb{Q}}\operatorname{span}_{\mathbb{Q}}(Z_5) = 2$. Since $z^{(0)} = 0 \in Z_5$, the affine hull $\operatorname{aff}_{\mathbb{Q}}(Z_5) = z^{(0)} + \operatorname{span}_{\mathbb{Q}}(Z_5 - z^{(0)})$ equals $\operatorname{span}_{\mathbb{Q}}(Z_5) = \Pi_2$. Relations (A2) follow by direct coordinate evaluation. In $\Pi_2 \cong \mathbb{Q}^2$, the four nonzero vectors $z^{(1)}, z^{(2)}, z^{(3)}, z^{(4)}$ have pairwise distinct projective slopes $[1:0], [1:1], [2:1], [0:1]$ in $\mathbb{P}^1(\mathbb{Q})$ (the six $2 \times 2$ determinants $\det[z^{(a)} \mid z^{(b)}]_{01}$ for $(a,b) \in \{(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)\}$ are $\frac{1}{4}, \frac{1}{4}, \frac{1}{2}, -\frac{1}{4}, \frac{1}{2}, 1$, all nonzero), so every pair of distinct nonzero vectors in $Z_5$ is a basis of $\Pi_2$. $\square$

---

### 1.2 Exact comparison with the 9/24 calibration/validation sets $Z_I$ and $Z_V$

Recall from `CONTRACT.md` Section 1.3:

$$
Z_I = \{0\} \cup \{\pm e_i : 0 \le i < 4\} \quad (|Z_I| = 9), \qquad
Z_V = \{\sigma e_i + \rho e_j : 0 \le i < j < 4,\; \sigma, \rho \in \{-1, +1\}\} \quad (|Z_V| = 24).
$$

**Proposition A2 (Exact set and subspace intersections).**

1. **Literal intersections with $Z_5$:**
   $$
   Z_5 \cap Z_I = \{0, e_1\} = \{z^{(0)}, z^{(4)}\} \quad (2\text{ of }9), \qquad
   Z_5 \cap Z_V = \emptyset \quad (0\text{ of }24). \tag{A3}
   $$
2. **Subspace intersections with $\Pi_2 = \operatorname{span}_{\mathbb{Q}}(Z_5)$:**
   $$
   \Pi_2 \cap Z_I = \{0, +e_0, -e_0, +e_1, -e_1\} \quad (5\text{ of }9), \qquad
   Z_I \setminus \Pi_2 = \{+e_2, -e_2, +e_3, -e_3\} \quad (4\text{ of }9), \tag{A4}
   $$
   $$
   \Pi_2 \cap Z_V = \{-e_0-e_1, -e_0+e_1, +e_0-e_1, +e_0+e_1\} \quad (4\text{ of }24), \qquad
   |Z_V \setminus \Pi_2| = 20\text{ of }24. \tag{A5}
   $$
   The $20$ out-of-plane validation sources in $Z_V \setminus \Pi_2$ decompose into $16$ mixed plane-complement sources $\sigma e_i + \rho e_k$ ($i \in \{0,1\}, k \in \{2,3\}, \sigma,\rho \in \{\pm 1\}$) and $4$ pure-complement sources $\sigma e_2 + \rho e_3$ ($\sigma,\rho \in \{\pm 1\}$).

**Proof.**
Every nonzero element of $Z_I$ has Euclidean norm $1$ and one nonzero coordinate in $\{\pm 1\}$; among $z^{(1)}, z^{(2)}, z^{(3)}, z^{(4)}$, only $z^{(4)} = (0,1,0,0) = +e_1$ has this form, while $z^{(0)} = 0 \in Z_I$. Every element of $Z_V$ has two coordinates in $\{\pm 1\}$ and squared norm $2$, whereas the squared norms of $z^{(0)},\dots,z^{(4)}$ are $0, \frac{1}{4}, \frac{1}{2}, \frac{5}{4}, 1$, none of which equals $2$; hence $Z_5 \cap Z_V = \emptyset$. A vector in $Z_I$ or $Z_V$ belongs to $\Pi_2$ if and only if its $e_2$ and $e_3$ coordinates vanish, which selects $\{0, \pm e_0, \pm e_1\}$ from $Z_I$ and $\{\sigma e_0 + \rho e_1 : \sigma,\rho \in \{\pm 1\}\}$ from $Z_V$. $\square$

---

### 1.3 Two-extra-direction spanning criterion and parameter decomposition

**Theorem A3 (Necessary and sufficient quotient condition to span $\mathbb{Q}^4$).**
Let $\pi_{23} : \mathbb{Q}^4 \to \mathbb{Q}^4 / \Pi_2 \cong \mathbb{Q}^2$ be the quotient map $\pi_{23}(z_0, z_1, z_2, z_3) = (z_2, z_3)$. For any additional source set $U_{\mathrm{ext}} \subset \mathbb{Q}^4$:

1. $\operatorname{span}_{\mathbb{Q}}(Z_5 \cup U_{\mathrm{ext}}) = \mathbb{Q}^4$ if and only if $\operatorname{span}_{\mathbb{Q}}(\pi_{23}(U_{\mathrm{ext}})) = \mathbb{Q}^2$.
2. Consequently, $|U_{\mathrm{ext}}| \ge 2$ is necessary, and a two-element set $U_{\mathrm{ext}} = \{u^{(2)}, u^{(3)}\} \subset \mathbb{Q}^4$ satisfies $\operatorname{span}_{\mathbb{Q}}(Z_5 \cup U_{\mathrm{ext}}) = \mathbb{Q}^4$ if and only if $[u^{(2)}], [u^{(3)}]$ are linearly independent in $\mathbb{Q}^4 / \Pi_2$, equivalently
   $$
   \det \begin{pmatrix} u^{(2)}_2 & u^{(3)}_2 \\ u^{(2)}_3 & u^{(3)}_3 \end{pmatrix} = u^{(2)}_2 u^{(3)}_3 - u^{(2)}_3 u^{(3)}_2 \ne 0 \tag{A6}
   $$
   (in particular for $u^{(2)} = e_2, u^{(3)} = e_3$, where the determinant is $1$).

**Proof.**
Since $\operatorname{span}_{\mathbb{Q}}(Z_5) = \Pi_2 = \ker(\pi_{23})$ by Theorem A1, $\operatorname{span}_{\mathbb{Q}}(Z_5 \cup U_{\mathrm{ext}}) = \Pi_2 + \operatorname{span}_{\mathbb{Q}}(U_{\mathrm{ext}}) = \pi_{23}^{-1}(\operatorname{span}_{\mathbb{Q}}(\pi_{23}(U_{\mathrm{ext}})))$. Because $\pi_{23}$ is surjective onto $\mathbb{Q}^2$, the preimage equals $\mathbb{Q}^4$ if and only if $\operatorname{span}_{\mathbb{Q}}(\pi_{23}(U_{\mathrm{ext}})) = \mathbb{Q}^2$, which requires at least $\dim_{\mathbb{Q}}(\mathbb{Q}^2) = 2$ generators and, for two vectors $u^{(2)}, u^{(3)}$, is equivalent to nonvanishing of the $2 \times 2$ determinant (A6). $\square$

**Theorem A4 (Exact identifiable/unconstrained parameter split on $\Pi_2$).**
Along the direct sum $\mathbb{Q}^4 = \Pi_2 \oplus \Pi_\perp$ with $\Pi_\perp = \mathbb{Q}e_2 \oplus \mathbb{Q}e_3$, write any linear/quadratic model $m = (A_0, A_1, G_0) \in \mathcal{A}_{\mathrm{lin}}$ in block form

$$
A_t = \bigl[ A_t^{(01)} \;\big|\; A_t^{(23)} \bigr] \quad (A_t^{(01)}, A_t^{(23)} \in \mathbb{Q}^{4 \times 2},\; t=0,1), \qquad
G_0 = \begin{pmatrix} G_{00} & G_{01} \\ G_{01}^T & G_{11} \end{pmatrix} \quad (G_{00}, G_{11} \in \mathbb{Q}^{2 \times 2}_{\mathrm{sym}},\; G_{01} \in \mathbb{Q}^{2 \times 2}). \tag{A7}
$$

Then restriction of the observable map $\mathcal{O}_m$ to $Z_5$ (or to all of $\Pi_2$) induces the exact direct-sum decomposition

$$
\mathcal{A}_{\mathrm{lin}} \cong \mathcal{I}_{\mathrm{lin}}(\Pi_2) \oplus \mathcal{K}_{\mathrm{lin}}(\Pi_2), \qquad
\dim_{\mathbb{Q}}\mathcal{A}_{\mathrm{lin}} = 42 = 19 + 23, \tag{A8}
$$

where:

1. **Identifiable subspace $\mathcal{I}_{\mathrm{lin}}(\Pi_2)$ ($\dim_{\mathbb{Q}} = 8 + 8 + 3 = 19$):** Consists of $(A_0^{(01)}, A_1^{(01)}, G_{00})$, uniquely reconstructed from the four points $\{z^{(1)}, z^{(2)}, z^{(4)}\} \subset Z_5$ by
   $$
   A_t e_0 = 2 b_{t,m}(z^{(1)}), \qquad A_t e_1 = b_{t,m}(z^{(4)}) \qquad (t = 0, 1), \tag{A9}
   $$
   $$
   g_{00} = 8 E_{0,m}(z^{(1)}), \qquad
   g_{11} = 2 E_{0,m}(z^{(4)}), \qquad
   g_{01} = 4 E_{0,m}(z^{(2)}) - 4 E_{0,m}(z^{(1)}) - E_{0,m}(z^{(4)}). \tag{A10}
   $$
2. **Unconstrained kernel subspace $\mathcal{K}_{\mathrm{lin}}(\Pi_2)$ ($\dim_{\mathbb{Q}} = 8 + 8 + 7 = 23$):** Consists of all tuples $(\Delta A_0, \Delta A_1, \Delta G_0)$ with $\Delta A_t^{(01)} = 0$ ($8$ free parameters each for $t=0,1$) and $\Delta G_{00} = 0$ ($4$ free parameters in $G_{01}$ plus $3$ free parameters in $G_{11}$). Adding any element of $\mathcal{K}_{\mathrm{lin}}(\Pi_2)$ to $m$ leaves $\mathcal{O}_m(z)$ invariant for every $z \in \Pi_2$ (and hence on all $5$ points of $Z_5$).

**Proof.**
For $z = (z_0, z_1, 0, 0)^T \in \Pi_2$, $A_t z = z_0 (A_t e_0) + z_1 (A_t e_1)$ and $E_{0,m}(z) = \frac{1}{2}(g_{00} z_0^2 + 2g_{01} z_0 z_1 + g_{11} z_1^2)$. Thus $\mathcal{O}_m|_{\Pi_2}$ depends only on $(A_0^{(01)}, A_1^{(01)}, G_{00})$ and vanishes if and only if those blocks vanish, giving the kernel $\mathcal{K}_{\mathrm{lin}}(\Pi_2)$ of dimension $8 + 8 + (4 + 3) = 23$. Evaluating at $z^{(1)} = (\frac{1}{2}, 0, 0, 0)$ gives $b_{t,m}(z^{(1)}) = \frac{1}{2}A_t e_0$ and $E_{0,m}(z^{(1)}) = \frac{1}{8}g_{00}$; evaluating at $z^{(4)} = (0, 1, 0, 0)$ gives $b_{t,m}(z^{(4)}) = A_t e_1$ and $E_{0,m}(z^{(4)}) = \frac{1}{2}g_{11}$; and evaluating at $z^{(2)} = (\frac{1}{2}, \frac{1}{2}, 0, 0)$ gives
$$
E_{0,m}(z^{(2)}) = \tfrac{1}{8}g_{00} + \tfrac{1}{4}g_{01} + \tfrac{1}{8}g_{11} = E_{0,m}(z^{(1)}) + \tfrac{1}{4}g_{01} + \tfrac{1}{4}E_{0,m}(z^{(4)}),
$$
which solves directly for (A9)–(A10). $\square$

---

## 2. Target-independent model family and exact-clone indistinguishability bound (Obligation B)

### 2.1 Exact-clone indistinguishability theorem

**Theorem B1 (Ideal classical clone indistinguishability bound).**
Let $D_{\mathrm{NC}}$ be the conditional native-contact composite machine and $D_{\mathrm{cl}}$ the ordinary rational classical wave/port comparator defined in `CONTRACT.md` Section 2.2.

1. **On the native preparation domain $\mathcal{P}_{\mathrm{nat}} = \mathbb{F}_5^4$:** For every $p \in \mathbb{F}_5^4$, the classical port and energy record $\Pi_{\mathrm{port}}$ of $D_{\mathrm{NC}}$ equals that of $D_{\mathrm{cl}}$ identically:
   $$
   \forall p \in \mathbb{F}_5^4 : \quad \Pi_{\mathrm{port}}^{D_{\mathrm{NC}}}(p) = \Pi_{\mathrm{port}}^{D_{\mathrm{cl}}}(p)
   = \Bigl(\bigl(R_0 z^{(h(p))},\, R_1 z^{(h(p))}\bigr),\, \bigl(E_0(z^{(h(p))}), E_1(z^{(h(p))}), E_2(z^{(h(p))})\bigr),\, E_0(z^{(h(p))})\Bigr). \tag{B1}
   $$
2. **On any extended source domain $\mathcal{Z} \subseteq \mathbb{Q}^4$ (including full $\mathbb{Q}^4$ span):** Suppose an extended device pair $(D_{\mathrm{NC}}^{\mathrm{ext}}, D_{\mathrm{cl}}^{\mathrm{ext}})$ admits an enlarged preparation set $\mathcal{Z} \supseteq Z_5$ (for example by adjoining two quotient-independent directions $u^{(2)}, u^{(3)}$ satisfying (A6), or all of $Z_I \cup Z_V$) and both devices implement the same source map $z \mapsto S(z)$, cold ready state $X_{\mathrm{blank}}$, two-cut transition $F$, and observable map $\Pi_{\mathrm{port}}$ on $\mathcal{Z}$. Then
   $$
   \forall z \in \mathcal{Z} : \quad \Pi_{\mathrm{port}}^{D_{\mathrm{NC}}^{\mathrm{ext}}}(z) = \Pi_{\mathrm{port}}^{D_{\mathrm{cl}}^{\mathrm{ext}}}(z). \tag{B2}
   $$
   In particular, **no number of additional source directions in $\mathbb{Q}^4$ separates $D_{\mathrm{NC}}$ from $D_{\mathrm{cl}}$ under $\Pi_{\mathrm{port}}$**.

**Proof.**
In $D_{\mathrm{NC}}$, for any $p \in \mathbb{F}_5^4$, stage 1 advances $(0, x_0(p)) \mapsto (1, x_1(p))$ while leaving $X_{\mathrm{blank}}$ and $w=0$ untouched; stage 2 applies $C_*$, which reads only $C_1(p) = C_1(h(p))$ and writes $X_0(z^{(h(p))}) = ((0, S z^{(h(p))}), (0,0), (0,0), 0)$ and $w = E_D(0, S z^{(h(p))})$; stages 3 and 4 apply $U \times F$ twice on the decoupled product $\Omega \times X$ with $w$ constant. Because $\Pi_{\mathrm{port}}$ depends only on $(X_2, w)$, the post-disconnection native steps $x_1 \mapsto x_2 \mapsto x_3$ drop out of $\Pi_{\mathrm{port}}$:
$$
\Pi_{\mathrm{port}}^{D_{\mathrm{NC}}}(p) = \Pi_{\mathrm{port}}\bigl(F^2(X_0(z^{(h(p))})),\, E_D(0, S z^{(h(p))})\bigr) = \Pi_{\mathrm{port}}^{D_{\mathrm{cl}}}(p).
$$
Likewise, for any $z \in \mathcal{Z}$ where both $D_{\mathrm{NC}}^{\mathrm{ext}}$ and $D_{\mathrm{cl}}^{\mathrm{ext}}$ prepare $(X_0(z), E_D(0, S(z)))$ and apply $F^2$ followed by $\Pi_{\mathrm{port}}$, functional composition gives $\Pi_{\mathrm{port}}(F^2(X_0(z)), E_D(0, S(z)))$ identically in both devices. $\square$

---

### 2.2 Necessary and sufficient mechanism-separating interventions

Theorem B1 shows that mechanism attribution ($D_{\mathrm{NC}}$ versus an $h$-only classical clone $D_{\mathrm{cl}}$) is impossible if the observer accesses only $\Pi_{\mathrm{port}}$ at fixed contact time $n=1$ and infinite work capacity. The following theorem classifies three concrete interventions that genuinely break the factorization through $h \mapsto z^{(h)}$.

**Theorem B2 (Exact mechanism-separation witnesses across $D_{\mathrm{NC}}$ and $D_{\mathrm{cl}}$).**

1. **Intervention M1 (Intra-fibre native-endpoint retention and piston-sum guard on $\mathcal{F}_h$):**
   For each $h \in \mathbb{F}_5$, the fibre $\mathcal{F}_h = \{p \in \mathbb{F}_5^4 : \sum_{i=0}^3 p_i \equiv h \pmod 5\}$ has $|\mathcal{F}_h| = 125$. In $D_{\mathrm{NC}}$, the retained native endpoint $x_3(p) = g_{j_2(h)} g_{j_1(h)} g_{j_0(h)}(p, 0, 1)$ takes $125$ distinct values on $\mathcal{F}_h$ (invertible via $x_0 = g_{j_0(h)} g_{j_1(h)} g_{j_2(h)} x_3$), whereas an $h$-only classical clone $D_{\mathrm{cl}}$ has constant internal state across $\mathcal{F}_h$. Explicitly, for the two $h=0$ preparations $p^{(0,a)} = (0,0,0,0)$ and $p^{(0,b)} = (1,4,0,0) \in \mathcal{F}_0$:
   $$
   \Pi_{\mathrm{port}}^{D_{\mathrm{NC}}}(p^{(0,a)}) = \Pi_{\mathrm{port}}^{D_{\mathrm{NC}}}(p^{(0,b)}) = \bigl((0,0), (0,0,0), 0\bigr),
   $$
   while the retained native endpoints in $D_{\mathrm{NC}}$ are distinct:
   $$
   x_3(p^{(0,a)}) = (2, 1, 3, 4, 1, 0) \ne (1, 2, 3, 4, 1, 0) = x_3(p^{(0,b)}). \tag{B3}
   $$
2. **Intervention M2 (Contact-boundary shift from $n=1$ to $n=2$):**
   Suppose the contact operation $C_*$ is triggered after two native ticks ($n=2$) instead of one ($n=1$), while a static classical lookup clone $D_{\mathrm{cl}}^{\mathrm{static}}$ has no internal $U$-evolution and outputs its stored source $z^{(h)}$ whenever triggered. In $D_{\mathrm{NC}}$, the second-tick receivers $C_2(h)$ for $h=0,1,2,3,4$ are $(0,1), (0,1), (4,0), (3,0), (1,4)$, which under $\eta(q,r) = (\ell(q)/2, (\ell(r)+1)/2, 0, 0)$ induce the source vectors
   $$
   z_{n=2}^{(0)} = z_{n=2}^{(1)} = (0, 1, 0, 0) = e_1, \quad
   z_{n=2}^{(2)} = \left(-\tfrac{1}{2}, \tfrac{1}{2}, 0, 0\right), \quad
   z_{n=2}^{(3)} = \left(-1, \tfrac{1}{2}, 0, 0\right), \quad
   z_{n=2}^{(4)} = \left(\tfrac{1}{2}, 0, 0, 0\right). \tag{B4}
   $$
   Consequently, at $n=2$, $D_{\mathrm{NC}}$ merges classes $h=0$ and $h=1$ (consistent with `U-NATIVE-RAW-RESIDUE-READOUT` `[T]`), drives a nonzero wave at $h=0$ with
   $$
   12960\, b_{0,D_{\mathrm{NC}}}^{(n=2)}(h=0) = (698, -2832, 708, 696) \ne (0,0,0,0) = 12960\, b_{0,D_{\mathrm{cl}}^{\mathrm{static}}}(h=0), \tag{B5}
   $$
   and reverses the sign of the $e_0$ source coordinate for $h=2,3$, producing $4$-chip and $5$-chip initial energies
   $$
   E_{0,D_{\mathrm{NC}}}^{(n=2)}(h=2) = \tfrac{1}{4} \ne \tfrac{3}{20}, \qquad
   E_{0,D_{\mathrm{NC}}}^{(n=2)}(h=3) = \tfrac{3}{5} \ne \tfrac{2}{5}. \tag{B6}
   $$
3. **Intervention M3 (Finite-store energy threshold $B \in \mathbb{Q}_{\ge 0}$):**
   If the unbounded signed work register $w$ is replaced by a nonnegative energy store $B \in \mathbb{Q}_{\ge 0}$ that executes the translation $v \mapsto v + S\eta(q,r)$ only when $B \ge \Delta E_D = E_D(u, v + S\eta(q,r)) - E_D(u,v)$ and otherwise leaves $(u,v)$ unchanged (as in the `#1495`/`#1496` bounded-store involution $H_B$), then preparing an initial store $B = 1/5$ admits $h \in \{0, 1, 2\}$ ($E_0 \in \{0, \frac{1}{10}, \frac{3}{20}\} \le \frac{1}{5}$) while blocking $h \in \{3, 4\}$ ($E_0 = \frac{2}{5} > \frac{1}{5}$, yielding $b_0 = b_1 = 0$), and even with $B = 2/5$ a second un-renewed trial on $h \in \{3,4\}$ (after resetting the wave to zero without replenishing $B = 0$) produces $b_0 = b_1 = 0$, separating a finite-store transducer from an externally powered classical port.

**Proof.**
For (1), `contact/PROOF.md` Section 1 establishes that for $h=0$, $x_3(p) = (2-p_0, 1-p_1, 3-p_2, 4-p_3, 1, 0) \pmod 5$; substituting $p^{(0,a)} = (0,0,0,0)$ and $p^{(0,b)} = (1,4,0,0)$ yields $(2,1,3,4,1,0)$ and $(1,2,3,4,1,0)$.
For (2), applying $\eta(q,r) = (\ell(q)/2, (\ell(r)+1)/2, 0, 0)$ with $\ell(0,1,2,3,4) = (0,1,2,-2,-1)$ to $C_2(0) = C_2(1) = (0,1)$ gives $(0/2, (1+1)/2, 0, 0) = (0,1,0,0) = z^{(4)}$, whose first-cut response is the $h=4$ row of the integer table $12960\,b_0 = (698, -2832, 708, 696)$; applying $\eta$ to $C_2(2) = (4,0)$ gives $(\ell(4)/2, (\ell(0)+1)/2, 0, 0) = (-1/2, 1/2, 0, 0)$ with energy $\frac{1}{2}(\frac{1}{4} + \frac{1}{4} - 0) = \frac{1}{4}$; applying $\eta$ to $C_2(3) = (3,0)$ gives $(\ell(3)/2, (\ell(0)+1)/2, 0, 0) = (-1, 1/2, 0, 0)$ with energy $\frac{1}{2}(1 + \frac{1}{4} - \frac{1}{5}(-\frac{1}{2})^2) = \frac{1}{2}(\frac{5}{4} - \frac{1}{20}) = \frac{3}{5}$; and applying $\eta$ to $C_2(4) = (1,4)$ gives $(1/2, 0, 0, 0) = z^{(1)}$.
For (3), the five cold preparation energies on $Z_5$ are $E_0(z^{(h)}) = (0, \frac{1}{10}, \frac{3}{20}, \frac{2}{5}, \frac{2}{5})$ for $h=0,1,2,3,4$; comparing with $B = \frac{1}{5} = \frac{4}{20}$ separates $\{0, \frac{2}{20}, \frac{3}{20}\} \le \frac{4}{20} < \frac{8}{20}$. $\square$

---

## 3. Calibration-to-prediction criterion $I(m_1)=I(m_2) \Rightarrow V(m_1;s)=V(m_2;s)$ (Obligation C)

### 3.1 Regime C1: Within-plane $Z_5$ calibration and held-out $Z_5 / \Pi_2$ prediction in $\mathcal{A}_{\mathrm{lin}}$ and $\mathcal{A}_{\mathrm{aff}}$

**Theorem C1 (Exact $Z_5$ calibration-to-prediction decision in $\mathcal{A}_{\mathrm{lin}}$).**
Let $\mathcal{A}_{\mathrm{lin}}$ be the $42$-parameter linear/quadratic model class of `CONTRACT.md` Section 2.1.

1. **Two nonzero $Z_5$ calibrations determine linear responses $(b_0, b_1)$ on all of $\Pi_2$, but NOT quadratic energy $E_0$ on $Z_5$:**
   - For any $2$-element subset $I_2 = \{z^{(a)}, z^{(b)}\} \subset Z_5 \setminus \{z^{(0)}\}$ ($1 \le a < b \le 4$), equality of calibrated signed responses $b_{t,m_1}|_{I_2} = b_{t,m_2}|_{I_2}$ implies $b_{t,m_1}(s) = b_{t,m_2}(s)$ for every $s \in \Pi_2$ (including the other $3$ points of $Z_5$, all $5$ points of $Z_I \cap \Pi_2$, and all $4$ points of $Z_V \cap \Pi_2$).
   - However, for the full observable $\mathcal{O}_m = (b_{0,m}, b_{1,m}, (E_{0,m}, E_{1,m}, E_{2,m}))$, calibration on the $3$-point axis subset $I_{\mathrm{axis}} = \{z^{(0)}, z^{(1)}, z^{(4)}\} \subset Z_5$ (and even on all $5$ points of $Z_I \cap \Pi_2 = \{0, \pm e_0, \pm e_1\}$) **fails** to determine $V(m; s)$ at $s \in \{z^{(2)}, z^{(3)}\}$:
     $$
     \mathrm{Det}\bigl(\mathcal{A}_{\mathrm{lin}},\, \{z^{(0)}, z^{(1)}, z^{(4)}\},\, \{z^{(2)}, z^{(3)}\}\bigr) = \text{FALSE (UNDERDETERMINED)}. \tag{C1}
     $$
   - **Explicit positive-definite witness pair $(m_*, m_{\mathrm{off}}) \in \mathcal{A}_{\mathrm{lin}}$:** Let $m_* = (R_0, R_1, G_{\mathrm{source}})$ and $m_{\mathrm{off}} = (R_0, R_1, G_0^{(\mathrm{off})})$ where
     $$
     G_0^{(\mathrm{off})} = G_{\mathrm{source}} + \frac{2}{5}(e_0 e_1^T + e_1 e_0^T)
     = \begin{pmatrix}
     4/5 & +1/5 & -1/5 & -1/5 \\
     +1/5 & 4/5 & -1/5 & -1/5 \\
     -1/5 & -1/5 & 4/5 & -1/5 \\
     -1/5 & -1/5 & -1/5 & 4/5
     \end{pmatrix}. \tag{C2}
     $$
     Here $G_0^{(\mathrm{off})}$ is symmetric and positive definite (with eigenvalues $1, \frac{3}{5}, \frac{4+\sqrt{5}}{5}, \frac{4-\sqrt{5}}{5} > 0$). On $I_{\mathrm{axis}} = \{z^{(0)}, z^{(1)}, z^{(4)}\}$ (and on all of $Z_I \cap \Pi_2$), $\mathcal{O}_{m_{\mathrm{off}}}(z) = \mathcal{O}_{m_*}(z)$ identically ($E_0 = 0, \frac{1}{10}, \frac{2}{5}$). Yet on the held-out superposition inputs $z^{(2)} = (\frac{1}{2}, \frac{1}{2}, 0, 0)$ and $z^{(3)} = (1, \frac{1}{2}, 0, 0)$, their energies diverge:
     $$
     E_{0,m_*}(z^{(2)}) = \frac{3}{20} \ne \frac{1}{4} = E_{0,m_{\mathrm{off}}}(z^{(2)}), \qquad
     E_{0,m_*}(z^{(3)}) = \frac{2}{5} \ne \frac{3}{5} = E_{0,m_{\mathrm{off}}}(z^{(3)}). \tag{C3}
     $$
2. **Three nonzero $Z_5$ calibrations uniquely determine all observables $\mathcal{O}_m$ on all of $\Pi_2$ (including the held-out fifth point of $Z_5$):**
   For any $3$-element subset $I_3 \subset Z_5 \setminus \{z^{(0)}\}$ (all $\binom{4}{3} = 4$ choices),
   $$
   \mathrm{Det}\bigl(\mathcal{A}_{\mathrm{lin}},\, I_3,\, \Pi_2\bigr) = \text{TRUE (DETERMINED)}. \tag{C4}
   $$
   In particular, for the calibration set $I_3 = \{z^{(1)}, z^{(2)}, z^{(4)}\}$ (or $\{z^{(0)}, z^{(1)}, z^{(2)}, z^{(4)}\}$) and the held-out fifth native encoding $s = z^{(3)} = (1, \frac{1}{2}, 0, 0)$, every model $m \in \mathcal{A}_{\mathrm{lin}}$ obeys the exact parameter-free cross-prediction identities:
   $$
   b_{t,m}(z^{(3)}) = 2 b_{t,m}(z^{(1)}) + \tfrac{1}{2} b_{t,m}(z^{(4)}) = b_{t,m}(z^{(1)}) + b_{t,m}(z^{(2)}) \qquad (t = 0, 1), \tag{C5}
   $$
   $$
   E_{0,m}(z^{(3)}) = 2 E_{0,m}(z^{(1)}) + 2 E_{0,m}(z^{(2)}) - \tfrac{1}{4} E_{0,m}(z^{(4)}), \tag{C6}
   $$
   $$
   E_{1,m}(z^{(3)}) = E_{0,m}(z^{(3)}) - 2\|b_{0,m}(z^{(3)})\|^2, \qquad
   E_{2,m}(z^{(3)}) = E_{1,m}(z^{(3)}) - 2\|b_{1,m}(z^{(3)})\|^2. \tag{C7}
   $$
   Similarly, for any $s = (z_0, z_1, 0, 0) \in \Pi_2$ (including all $5$ points of $Z_I \cap \Pi_2$ and all $4$ points of $Z_V \cap \Pi_2$):
   $$
   b_{t,m}(s) = 2z_0\, b_{t,m}(z^{(1)}) + z_1\, b_{t,m}(z^{(4)}), \tag{C8}
   $$
   $$
   E_{0,m}(s) = 4z_0(z_0 - z_1) E_{0,m}(z^{(1)}) + 4z_0 z_1 E_{0,m}(z^{(2)}) + z_1(z_1 - z_0) E_{0,m}(z^{(4)}). \tag{C9}
   $$

**Proof.**
Part (1): By Theorem A1(3), any two nonzero vectors in $Z_5$ form a basis of $\Pi_2$, so a linear map $A_t|_{\Pi_2}$ is uniquely determined by its values on $I_2$. For $I_{\mathrm{axis}} = \{z^{(0)}, z^{(1)}, z^{(4)}\}$, all three vectors lie on the coordinate axes $z_0 z_1 = 0$, so $z^T (e_0 e_1^T + e_1 e_0^T) z = 2z_0 z_1 = 0$ on $I_{\mathrm{axis}}$, proving $I_{\mathrm{axis}}(m_*) = I_{\mathrm{axis}}(m_{\mathrm{off}})$, while on $z^{(2)} = (\frac{1}{2},\frac{1}{2},0,0)$ and $z^{(3)} = (1,\frac{1}{2},0,0)$ the perturbation $\frac{1}{2}z^T[\frac{2}{5}(e_0 e_1^T + e_1 e_0^T)]z = \frac{2}{5}z_0 z_1$ equals $\frac{1}{10}$ and $\frac{1}{5}$ respectively, giving (C3). To verify positive definiteness of $G_0^{(\mathrm{off})}$, note that $(1,-1,0,0)^T$ and $(0,0,1,-1)^T$ are eigenvectors with eigenvalues $\frac{3}{5}$ and $1$, while on the $2$-dimensional symmetric complement $\operatorname{span}\{e_0+e_1, e_2+e_3\}$ the action matrix is $\begin{pmatrix} 1 & -2/5 \\ -2/5 & 3/5 \end{pmatrix}$ with trace $\frac{8}{5} > 0$ and determinant $\frac{3}{5} - \frac{4}{25} = \frac{11}{25} > 0$.
Part (2): Any three vectors in $Z_5 \setminus \{z^{(0)}\}$ have pairwise distinct projective slopes in $\mathbb{P}^1(\mathbb{Q})$ by Theorem A1, so the $3 \times 3$ matrix of quadratic monomials $(z_0^2, 2z_0 z_1, z_1^2)$ is invertible and uniquely fixes $(g_{00}, g_{01}, g_{11})$. Substituting (A10) into $E_{0,m}(s) = \frac{1}{2}(g_{00} z_0^2 + 2g_{01} z_0 z_1 + g_{11} z_1^2)$ yields
$$
E_{0,m}(s) = 4 z_0^2 E_{0,m}(z^{(1)}) + z_0 z_1 \bigl(4 E_{0,m}(z^{(2)}) - 4 E_{0,m}(z^{(1)}) - E_{0,m}(z^{(4)})\bigr) + z_1^2 E_{0,m}(z^{(4)}),
$$
which simplifies to (C9), and setting $(z_0, z_1) = (1, \frac{1}{2})$ gives (C6) (equivalently the quadratic parallelogram identity $E_0(z^{(2)}+z^{(1)}) + E_0(z^{(2)}-z^{(1)}) = 2E_0(z^{(2)}) + 2E_0(z^{(1)})$ with $z^{(2)}-z^{(1)} = \frac{1}{2}z^{(4)}$). $\square$

---

**Theorem C2 (Affine response determination and the $6$-parameter quadratic-affine null polynomial on $Z_5$).**
In the affine model class $\mathcal{A}_{\mathrm{aff}}$ (`CONTRACT.md` Section 2.1):

1. **Affine signed responses $b_{t,m}(z) = c_t + A_t z$:** Calibration on any $3$ affinely independent points of $Z_5$ (such as $I_{\mathrm{aff},3} = \{z^{(0)}, z^{(1)}, z^{(4)}\}$) uniquely determines $b_{t,m}(s)$ for all $s \in \Pi_2$, via
   $$
   b_{t,m}(s) = (1 - 2z_0 - z_1)\, b_{t,m}(z^{(0)}) + 2z_0\, b_{t,m}(z^{(1)}) + z_1\, b_{t,m}(z^{(4)}). \tag{C10}
   $$
2. **Unconstrained affine-quadratic energy $E_{0,m}(z) = e_0 + \ell_0^T z + \frac{1}{2}z^T G_0 z$:** If the linear drift $\ell_0$ and offset $e_0$ of the initial energy are not constrained to zero by preparation readiness, then even calibrating **all five points of $Z_5$** fails to determine $E_{0,m}(s)$ on $\Pi_2 \setminus Z_5$ (including on $Z_I \cap \Pi_2$ and $Z_V \cap \Pi_2$):
   $$
   \mathrm{Det}_{E_0}\bigl(\mathcal{A}_{\mathrm{aff}},\, Z_5,\, (\Pi_2 \cap Z_I) \cup (\Pi_2 \cap Z_V)\bigr) = \text{FALSE (UNDERDETERMINED)}. \tag{C11}
   $$
   Specifically, the space of degree-$\le 2$ polynomials on $\Pi_2$ that vanish on all $5$ points of $Z_5$ is $1$-dimensional and spanned by
   $$
   \Phi_{Z_5}(z_0, z_1) = z_0^2 - 2z_0 z_1 - 2z_1^2 - \frac{1}{2}z_0 + 2z_1 = z_0\left(z_0 - \frac{1}{2}\right) - 2z_1(z_0 + z_1 - 1). \tag{C12}
   $$
   Consequently, the model $m_{\mathrm{aff}} \in \mathcal{A}_{\mathrm{aff}}$ with $b_{t,m_{\mathrm{aff}}} = b_{t,m_*}$ and $E_{0,m_{\mathrm{aff}}}(z) = E_{0,m_*}(z) + \Phi_{Z_5}(z_0, z_1)$ agrees with $m_*$ on all $5$ points of $Z_5$ ($\Phi_{Z_5}|_{Z_5} = 0$), while diverging on $+e_0, -e_0, -e_1 \in Z_I \cap \Pi_2$ and on all $4$ points of $Z_V \cap \Pi_2$:
   $$
   \Phi_{Z_5}(+e_0) = \frac{1}{2},\quad
   \Phi_{Z_5}(-e_0) = \frac{3}{2},\quad
   \Phi_{Z_5}(-e_1) = -4,\quad
   \Phi_{Z_5}(e_0+e_1) = -\frac{3}{2},\quad
   \Phi_{Z_5}(e_0-e_1) = -\frac{3}{2}. \tag{C13}
   $$

**Proof.**
Part (1) follows because $z^{(1)} - z^{(0)} = \frac{1}{2}e_0$ and $z^{(4)} - z^{(0)} = e_1$ span $\Pi_2$, so every $s = (z_0, z_1, 0, 0) \in \Pi_2$ has the unique barycentric decomposition $s = (1 - 2z_0 - z_1)z^{(0)} + 2z_0 z^{(1)} + z_1 z^{(4)}$.
For Part (2), the vector space of polynomials of degree $\le 2$ in $(z_0, z_1)$ has dimension $\binom{2+2}{2} = 6$ with basis $\{1, z_0, z_1, z_0^2, z_0 z_1, z_1^2\}$. Evaluation at the $5$ points of $Z_5$ is a linear map $\mathbb{Q}^6 \to \mathbb{Q}^5$ of rank $5$ (since $\{z^{(0)}, z^{(1)}, z^{(2)}, z^{(3)}, z^{(4)}\}$ impose $5$ independent conditions), so its kernel has dimension $6 - 5 = 1$. Direct substitution into (C12) verifies $\Phi_{Z_5}(0,0) = 0$, $\Phi_{Z_5}(\frac{1}{2},0) = 0$, $\Phi_{Z_5}(\frac{1}{2},\frac{1}{2}) = 0 - 2(\frac{1}{2})(0) = 0$, $\Phi_{Z_5}(1,\frac{1}{2}) = \frac{1}{2} - 2(\frac{1}{2})(\frac{1}{2}) = 0$, and $\Phi_{Z_5}(0,1) = 0 - 2(1)(0) = 0$, as well as the nonzero values (C13). $\square$

---

### 3.2 Regime C2: Out-of-plane $Z_I \setminus \Pi_2$ and $Z_V \setminus \Pi_2$ under $Z_5$ calibration

**Theorem C3 (Complete out-of-plane underdetermination under $Z_5$ calibration).**
In $\mathcal{A}_{\mathrm{lin}}$, calibrating on all $5$ points of $Z_5$ (and even on the entire plane $\Pi_2$) leaves the prediction $V(m; s)$ undetermined at **every** out-of-plane preparation $s \in \mathbb{Q}^4 \setminus \Pi_2$, including all $4$ points of $Z_I \setminus \Pi_2$ and all $20$ points of $Z_V \setminus \Pi_2$:

$$
\forall s \in \mathbb{Q}^4 \setminus \Pi_2 : \quad \mathrm{Det}\bigl(\mathcal{A}_{\mathrm{lin}},\, Z_5,\, \{s\}\bigr) = \text{FALSE (UNDERDETERMINED)}. \tag{C14}
$$

Specifically, let $J_{01} = \operatorname{diag}(1, 1, -1, -1)$ be reflection across $\Pi_2$, and define the isometric positive-definite conjugate model

$$
m_\sharp = \bigl(R_0 J_{01},\, R_1 J_{01},\, J_{01}^T G_{\mathrm{source}} J_{01}\bigr) \in \mathcal{A}_{\mathrm{lin}}. \tag{C15}
$$

Then:

1. **Identical calibration on $\Pi_2$ and $Z_5$:** For every $z \in \Pi_2$ (hence on all $5$ points of $Z_5$, all $5$ points of $Z_I \cap \Pi_2$, and all $4$ points of $Z_V \cap \Pi_2$), $J_{01} z = z$, so $\mathcal{O}_{m_\sharp}(z) = \mathcal{O}_{m_*}(z)$ byte for byte.
2. **Simultaneous divergence on every out-of-plane source $s \in \mathbb{Q}^4 \setminus \Pi_2$:** For every $s = s_{01} + s_{23}$ with $s_{01} \in \Pi_2$ and $s_{23} = (0, 0, s_2, s_3) \ne 0$, $J_{01} s - s = -2 s_{23} \ne 0$. Because $\det R_0 = -\frac{1}{4^4}\det M = -\frac{1770^3 \cdot 365}{4^4 \cdot 1620^4} \ne 0$, we have
   $$
   b_{0,m_\sharp}(s) - b_{0,m_*}(s) = -2 R_0 s_{23} \ne 0 \qquad (\forall s \in \mathbb{Q}^4 \setminus \Pi_2). \tag{C16}
   $$
3. **Explicit rational divergence witness on $s = e_0 + e_2 \in Z_V \setminus \Pi_2$:**
   $$
   \begin{aligned}
   12960\, b_{0,m_*}(e_0 + e_2) &= (-2144,\, 1416,\, -2124,\, 1392) \ne (-3540,\, 0,\, 3540,\, 0) = 12960\, b_{0,m_\sharp}(e_0 + e_2), \\
   1399680\, b_{1,m_*}(e_0 + e_2) &= (286868,\, -191316,\, 290624,\, -195516) \ne (481940,\, 0,\, -481940,\, 0) = 1399680\, b_{1,m_\sharp}(e_0 + e_2), \\
   E_{0,m_*}(e_0 + e_2) &= \frac{3}{5} \ne 1 = E_{0,m_\sharp}(e_0 + e_2).
   \end{aligned} \tag{C17}
   $$

**Proof.**
Since $J_{01}$ fixes $e_0, e_1$ and negates $e_2, e_3$, $J_{01} z = z$ for all $z \in \Pi_2$, giving $R_t J_{01} z = R_t z$ and $z^T J_{01}^T G_{\mathrm{source}} J_{01} z = z^T G_{\mathrm{source}} z$. For any $s \notin \Pi_2$, $s_{23} = \frac{1}{2}(s - J_{01} s) \ne 0$; injectivity of $R_0 = -\frac{1}{4}M$ on $\mathbb{Q}^4$ (`classical/OBSERVABILITY_CALIBRATION.md` equation (O4)) implies $R_0(J_{01}s - s) = -2R_0 s_{23} \ne 0$. For $s = e_0 + e_2$, $J_{01}(e_0 + e_2) = e_0 - e_2$; adding and subtracting columns $0$ and $2$ of $12960\,R_0 = -2(1620\,M)$ and $1399680\,R_1 = 2(699840\,R_1)$ from `classical/OBSERVABILITY_CALIBRATION.md` equations (O3) and (O6) yields (C17), while $(e_0 \pm e_2)^T (I_4 - \frac{1}{5}\mathbf{1}\mathbf{1}^T)(e_0 \pm e_2)/2$ equals $(2 - \frac{4}{5})/2 = \frac{3}{5}$ for $+$ and $(2 - 0)/2 = 1$ for $-$. $\square$

---

### 3.3 Regime C3: Nonlinear source-dependent class $\mathcal{A}_{\mathrm{nl}}$

**Theorem C4 (Nonlinear underdetermination on $Z_5$ and on $Z_I \to Z_V$).**
In the unrestricted deterministic source-dependent class $\mathcal{A}_{\mathrm{nl}}$:

1. **Within $Z_5$:** Even after calibrating four of the five points of $Z_5$, namely $I_4 = \{z^{(0)}, z^{(1)}, z^{(2)}, z^{(4)}\}$, prediction on the fifth point $z^{(3)} = (1, \frac{1}{2}, 0, 0)$ is undetermined. Explicitly, the cubic polynomial
   $$
   \Psi_{z^{(3)}}(z) = 2 z_0 (2z_0 - 1) z_1 \tag{C18}
   $$
   satisfies $\Psi_{z^{(3)}}(z^{(0)}) = \Psi_{z^{(3)}}(z^{(1)}) = \Psi_{z^{(3)}}(z^{(2)}) = \Psi_{z^{(3)}}(z^{(4)}) = 0$ and $\Psi_{z^{(3)}}(z^{(3)}) = 1$. Thus the model $m_{\mathrm{nl}} \in \mathcal{A}_{\mathrm{nl}}$ with $b_{t,m_{\mathrm{nl}}}(z) = R_t z + \Psi_{z^{(3)}}(z)\, e_0$ and $E_{0,m_{\mathrm{nl}}}(z) = E_{0,m_*}(z) + \Psi_{z^{(3)}}(z)^2$ satisfies $I_4(m_{\mathrm{nl}}) = I_4(m_*)$ while $b_{0,m_{\mathrm{nl}}}(z^{(3)}) = b_{0,m_*}(z^{(3)}) + e_0 \ne b_{0,m_*}(z^{(3)})$.
2. **On the classical 9-to-24 protocol ($Z_I \to Z_V$):** Every point $z \in Z_I = \{0, \pm e_0, \pm e_1, \pm e_2, \pm e_3\}$ has at most one nonzero coordinate, so $z_i z_j = 0$ on all $9$ points of $Z_I$ for every $0 \le i < j < 4$. Thus the degree-$2$ polynomial model $m_{\mathrm{cross}} \in \mathcal{A}_{\mathrm{nl}}$ with $b_{t,m_{\mathrm{cross}}}(z) = R_t z + z_0 z_1 e_0$ satisfies $I_{Z_I}(m_{\mathrm{cross}}) = I_{Z_I}(m_*)$ on all $9$ identification sources while diverging on $z^{(2)}, z^{(3)} \in Z_5$ and on all $4$ sources $\sigma e_0 + \rho e_1 \in Z_V \cap \Pi_2$ by $\sigma\rho e_0 \ne 0$.

**Proof.**
Direct substitution of $z^{(0)}=(0,0,0,0)$ ($z_0=0$), $z^{(1)}=(\frac{1}{2},0,0,0)$ ($z_1=0$), $z^{(2)}=(\frac{1}{2},\frac{1}{2},0,0)$ ($2z_0-1=0$), $z^{(4)}=(0,1,0,0)$ ($z_0=0$), and $z^{(3)}=(1,\frac{1}{2},0,0)$ ($2 \cdot 1 \cdot 1 \cdot \frac{1}{2} = 1$) proves (1); vanishing of $z_i z_j$ on the coordinate axes $Z_I$ and nonvanishing $\sigma\rho = \pm 1$ on $Z_V$ proves (2). $\square$

---

### 3.4 Regime C4: Conditional full-span augmentation on $\mathbb{Q}^4$

**Theorem C5 (Sharp preparation bounds for full $\mathbb{Q}^4$ linear response versus symmetric quadratic energy in $\mathcal{A}_{\mathrm{lin}}$).**
Let $U_{\mathrm{ext}} \subset \mathbb{Q}^4$ be a set of additional source preparations adjoined to $Z_5$. Within $\mathcal{A}_{\mathrm{lin}}$:

1. **Linear response $(b_0, b_1)$ on all of $\mathbb{Q}^4$:**
   $$
   \mathrm{Det}_{(b_0, b_1)}\bigl(\mathcal{A}_{\mathrm{lin}},\, Z_5 \cup U_{\mathrm{ext}},\, \mathbb{Q}^4\bigr) = \text{TRUE}
   \iff \operatorname{span}_{\mathbb{Q}}\bigl(\pi_{23}(U_{\mathrm{ext}})\bigr) = \mathbb{Q}^2. \tag{C19}
   $$
   Hence **$\min |U_{\mathrm{ext}}| = 2$** additional preparations (for example $U_{\mathrm{lin},2} = \{e_2, e_3\}$) are both necessary and sufficient to uniquely determine $(b_{0,m}(s), b_{1,m}(s))$ for all $s \in \mathbb{Q}^4$ (including all $24$ points of $Z_V$).
2. **Unconstrained symmetric quadratic energy $E_{0,m}(z) = \frac{1}{2}z^T G_0 z$ on all of $\mathbb{Q}^4$:**
   Adjoining only $U_{\mathrm{lin},2} = \{e_2, e_3\}$ (or even adjoining all $9$ points of $Z_I$) is **not** sufficient to determine $E_{0,m}(s)$ on $Z_V$:
   $$
   \mathrm{Det}_{E_0}\bigl(\mathcal{A}_{\mathrm{lin}},\, Z_5 \cup Z_I,\, Z_V\bigr) = \text{FALSE (UNDERDETERMINED)}. \tag{C20}
   $$
   - **Explicit witness pair $(m_*, m_{\mathrm{energy\text{-}flip}}) \in \mathcal{A}_{\mathrm{lin}}$:** Let $m_{\mathrm{energy\text{-}flip}} = (R_0, R_1, J_{01}^T G_{\mathrm{source}} J_{01})$, which has the **exact same linear response matrices** $(R_0, R_1)$ as $m_*$ on all of $\mathbb{Q}^4$ and the **exact same energy** $E_0(z)$ as $m_*$ on all $5$ points of $Z_5$ and all $9$ points of $Z_I$ (since $z^T J_{01}^T G_{\mathrm{source}} J_{01} z = z^T G_{\mathrm{source}} z$ whenever $z \in \Pi_2$ or $z \in \Pi_\perp$), yet differs from $m_*$ on all $16$ mixed validation sources $\sigma e_i + \rho e_k \in Z_V$ ($i \in \{0,1\}, k \in \{2,3\}$) by
     $$
     E_{0,m_{\mathrm{energy\text{-}flip}}}(\sigma e_i + \rho e_k) - E_{0,m_*}(\sigma e_i + \rho e_k) = \frac{2}{5}\sigma\rho = \pm \frac{2}{5} \ne 0. \tag{C21}
     $$
   - **Exact $7$-preparation necessity and sufficiency for $G_0 \in \mathbb{Q}^{4 \times 4}_{\mathrm{sym}}$:** Because $\dim_{\mathbb{Q}} \mathcal{K}_{\mathrm{quad}}(\Pi_2) = 7$ (Theorem A4), uniquely identifying an arbitrary symmetric matrix $G_0 \in \mathbb{Q}^{4 \times 4}_{\mathrm{sym}}$ from energy measurements $E_{0,m}(u)$ beyond $Z_5$ requires **$\min |U_{\mathrm{ext}}| = 7$** additional preparations whose projections in $\operatorname{Sym}^2(\mathbb{Q}^4) / \operatorname{Sym}^2(\Pi_2^*)$ span the $7$-dimensional complement. An explicit $7$-element sufficient set inside $Z_I \cup Z_V$ is
     $$
     U_{\mathrm{quad},7} = \bigl\{e_2,\; e_3,\; e_0+e_2,\; e_0+e_3,\; e_1+e_2,\; e_1+e_3,\; e_2+e_3\bigr\}, \tag{C22}
     $$
     from which the $7$ remaining entries of $G_0$ are recovered by
     $$
     g_{kk} = 2 E_{0,m}(e_k) \quad (k \in \{2,3\}), \qquad
     g_{23} = E_{0,m}(e_2 + e_3) - E_{0,m}(e_2) - E_{0,m}(e_3), \tag{C23}
     $$
     $$
     g_{0k} = E_{0,m}(e_0 + e_k) - 4 E_{0,m}(z^{(1)}) - E_{0,m}(e_k), \qquad
     g_{1k} = E_{0,m}(e_1 + e_k) - E_{0,m}(z^{(4)}) - E_{0,m}(e_k) \quad (k \in \{2,3\}). \tag{C24}
     $$
   - Conversely, if the model class is further restricted to the $32$-parameter coupler-compatible subclass $\mathcal{A}_{\mathrm{lin}}^{\mathrm{source}} \subset \mathcal{A}_{\mathrm{lin}}$ in which $G_0$ is fixed to $G_{\mathrm{source}} = I_4 - \frac{1}{5}\mathbf{1}\mathbf{1}^T$ (or reconstructed from $A_0 = -\frac{1}{4}P^T H S$ under the frozen stencil $H$), then the $2$-element set $U_{\mathrm{lin},2} = \{e_2, e_3\}$ suffices for the entire observable tuple $\mathcal{O}_m$.

**Proof.**
Part (1) is immediate from Theorem A3 and linearity of $b_{t,m}(z) = A_t z$.
For Part (2), every $z \in Z_5 \cup Z_I$ lies either in $\Pi_2 = \mathbb{Q}e_0 \oplus \mathbb{Q}e_1$ (where $J_{01} z = z$) or in $\Pi_\perp = \mathbb{Q}e_2 \oplus \mathbb{Q}e_3$ (where $J_{01} z = -z$). Since any quadratic form is even ($E_0(-z) = E_0(z)$), $z^T J_{01}^T G_{\mathrm{source}} J_{01} z = (\pm z)^T G_{\mathrm{source}} (\pm z) = z^T G_{\mathrm{source}} z$ for every $z \in Z_5 \cup Z_I$, proving (C20)–(C21). Because each scalar energy observation $E_{0,m}(u) = \frac{1}{2}u^T G_0 u$ supplies one linear functional on $\mathbb{Q}^{4 \times 4}_{\mathrm{sym}}$ and $\dim_{\mathbb{Q}} \mathcal{K}_{\mathrm{quad}}(\Pi_2) = 7$, at least $7$ additional preparations are necessary. For $U_{\mathrm{quad},7}$ in (C22), equations (C23)–(C24) triangularly invert the $7$ entries $(g_{22}, g_{33}, g_{23}, g_{02}, g_{03}, g_{12}, g_{13})$ using $g_{00} = 8E_{0,m}(z^{(1)})$ and $g_{11} = 2E_{0,m}(z^{(4)})$ from (A10), proving sufficiency. $\square$

---

### 3.5 Summary table of calibration-to-prediction outcomes

| Model class | Calibration set $I_{\mathrm{set}}$ | Held-out target $V_{\mathrm{set}}$ | Observable | Verdict | Proof / Witness |
|---|---|---|---|---|---|
| $\mathcal{A}_{\mathrm{lin}}$ | Any $2$ of $\{z^{(1)},z^{(2)},z^{(3)},z^{(4)}\}$ | All of $\Pi_2$ (incl. $Z_5$, $\Pi_2 \cap Z_I$, $\Pi_2 \cap Z_V$) | Signed $(b_0, b_1)$ | **DETERMINED** | Theorem C1(1), (C8) |
| $\mathcal{A}_{\mathrm{lin}}$ | $I_{\mathrm{axis}} = \{z^{(0)},z^{(1)},z^{(4)}\}$ (or $\Pi_2 \cap Z_I$) | $\{z^{(2)}, z^{(3)}\}$ (or $\Pi_2 \cap Z_V$) | Full $\mathcal{O}_m$ (energy $E_0$) | **UNDERDETERMINED** | Theorem C1(1), witness $(m_*, m_{\mathrm{off}})$ in (C2)–(C3) |
| $\mathcal{A}_{\mathrm{lin}}$ | Any $3$ of $\{z^{(1)},z^{(2)},z^{(3)},z^{(4)}\}$ (e.g. $\{z^{(1)},z^{(2)},z^{(4)}\}$) | Held-out $z^{(3)}$ and all of $\Pi_2$ | Full $\mathcal{O}_m$ ($(b_0,b_1,E_0,E_1,E_2)$) | **DETERMINED** | Theorem C1(2), (C5)–(C9) |
| $\mathcal{A}_{\mathrm{aff}}$ | $\{z^{(0)}, z^{(1)}, z^{(4)}\}$ | All of $\Pi_2$ | Signed $(b_0, b_1)$ | **DETERMINED** | Theorem C2(1), (C10) |
| $\mathcal{A}_{\mathrm{aff}}$ | All $5$ points of $Z_5$ | $\Pi_2 \setminus Z_5$ (incl. $\Pi_2 \cap Z_I$, $\Pi_2 \cap Z_V$) | Unconstrained affine-quadratic $E_0$ | **UNDERDETERMINED** | Theorem C2(2), null polynomial $\Phi_{Z_5}$ in (C12)–(C13) |
| $\mathcal{A}_{\mathrm{lin}}$ | All $5$ points of $Z_5$ (or all of $\Pi_2$) | Any $s \in \mathbb{Q}^4 \setminus \Pi_2$ (all $4$ of $Z_I \setminus \Pi_2$, all $20$ of $Z_V \setminus \Pi_2$) | Signed $(b_0,b_1)$ and full $\mathcal{O}_m$ | **UNDERDETERMINED** | Theorem C3, witness $(m_*, m_\sharp)$ in (C15)–(C17) |
| $\mathcal{A}_{\mathrm{nl}}$ | $I_4 = \{z^{(0)},z^{(1)},z^{(2)},z^{(4)}\}$ or $Z_I$ | Held-out $z^{(3)}$ or $Z_V$ | Signed $(b_0,b_1)$ and $E_0$ | **UNDERDETERMINED** | Theorem C4, cubic $\Psi_{z^{(3)}}$ in (C18) and $z_0 z_1$ |
| $\mathcal{A}_{\mathrm{lin}}$ | $Z_5 \cup U_{\mathrm{ext}}$ with $\operatorname{span}\pi_{23}(U_{\mathrm{ext}})=\mathbb{Q}^2$ ($\min |U_{\mathrm{ext}}|=2$) | All of $\mathbb{Q}^4$ (incl. all $24$ of $Z_V$) | Signed $(b_0, b_1)$ | **DETERMINED** | Theorem C5(1), (C19) |
| $\mathcal{A}_{\mathrm{lin}}$ | $Z_5 \cup Z_I$ (includes $U_{\mathrm{lin},2} = \{e_2,e_3\}$) | $16$ mixed points $\sigma e_i + \rho e_k \in Z_V$ | Full $\mathcal{O}_m$ (arbitrary $G_0 \in \mathbb{Q}^{4\times 4}_{\mathrm{sym}}$) | **UNDERDETERMINED** | Theorem C5(2), witness $(m_*, m_{\mathrm{energy\text{-}flip}})$ in (C21) |
| $\mathcal{A}_{\mathrm{lin}}$ | $Z_5 \cup U_{\mathrm{quad},7}$ ($\min |U_{\mathrm{ext}}|=7$) | All of $\mathbb{Q}^4$ (incl. all $24$ of $Z_V$) | Full $\mathcal{O}_m$ ($(b_0,b_1,E_0,E_1,E_2)$) | **DETERMINED** | Theorem C5(2), (C22)–(C24) |
| $\mathcal{M}_{\mathrm{dyn}}$ | Any $I_{\mathrm{set}} \subseteq \mathbb{Q}^4$ (incl. all $\mathbb{Q}^4$) | Mechanism $D_{\mathrm{NC}}$ vs classical clone $D_{\mathrm{cl}}$ | Classical port/energy $\Pi_{\mathrm{port}}$ | **INDISTINGUISHABLE** | Theorem B1, (B1)–(B2) |

---

## 4. Prospective finite test specification and exact qualification debts (Obligation D)

### 4.1 Protocol D1: Prospective $Z_5$-scoped calibration and held-out redundancy test

Without assuming unconstructed out-of-plane sources, the existing native-contact family $Z_5$ supports an exact, non-circular within-plane S/I/V test on $\Pi_2$ under $\mathcal{A}_{\mathrm{lin}}$:

1. **Stage S (Independent pre-calibration qualification, all currently unissued $\implies$ `NOT_READY`):**
   Before opening any Stage $I_5$ or Stage $V_5$ record, the instance packet must supply independent certificates for the twelve qualification fields of `classical/OBSERVABILITY_CALIBRATION.md` Section 6 (`INSTANCE`, `SOURCE`, `READY`, `SENSORS`, `UNITS`, `CLOCK_BINS`, `CONTACT`, `STATE_ENERGY`, `BOUNDARY`, `RENEWAL`, `UNCERTAINTY`, `CUSTODY`) with positive bounded conversion scales $(A_{0,\mathrm{length}}, \tau_{\mathrm{step}}, E_*)$ and derived $V_0 = A_{0,\mathrm{length}}/\tau_{\mathrm{step}}$, $F_0 = E_*/A_{0,\mathrm{length}}$, $Z_0 = E_*\tau_{\mathrm{step}}/A_{0,\mathrm{length}}^2$, $Z_j = 2Z_0$.
2. **Stage $I_5$ (4 native residue-class preparations $h \in \{0, 1, 2, 4\}$):**
   Acquire one complete two-cut record for canonical representatives $p^{(0)}=(0,0,0,0)$, $p^{(1)}=(1,0,0,0)$, $p^{(2)}=(2,0,0,0)$, $p^{(4)}=(4,0,0,0) \in \mathbb{F}_5^4$ prepared at $(0; (p^{(h)}, 0, 1))$ with cold classical state $X_{\mathrm{blank}}$.
   - **Continuing-wave acquisition:** Both $b_{\mathrm{cal},0}(z^{(h)})$ and $b_{\mathrm{cal},1}(z^{(h)})$ must be extracted from the physical outgoing channels during cut $t=0$ and cut $t=1$ of the continuing state; $b_1$ is never computed from $b_0$ via $-4R_1 M^{-1}b_0$.
   - **In-stage diagnostic checks on $I_5$:**
     - Cold zero baseline at $h=0$ ($z^{(0)} = 0$): $b_{\mathrm{cal},0}(z^{(0)}), b_{\mathrm{cal},1}(z^{(0)}), E_{\mathrm{cal},0}(z^{(0)})$ against $0$.
     - Subspace linear basis at $h=1, 4$: $A_{\mathrm{cal},t} e_0 = 2b_{\mathrm{cal},t}(z^{(1)})$, $A_{\mathrm{cal},t} e_1 = b_{\mathrm{cal},t}(z^{(4)})$ against $(R_t e_0, R_t e_1)$.
     - Linear superposition diagnostic at $h=2$ ($z^{(2)} = (\frac{1}{2}, \frac{1}{2}, 0, 0)$): $b_{\mathrm{cal},t}(z^{(2)}) - (b_{\mathrm{cal},t}(z^{(1)}) + \frac{1}{2}b_{\mathrm{cal},t}(z^{(4)}))$ against $0$, while $E_{\mathrm{cal},0}(z^{(2)})$ fixes the off-diagonal Gram entry $g_{01}$ via (A10).
   - Freeze `I_FREEZE` (all sensor calibrations, preprocessing functionals $L_{tj}$, and joint uncertainty set $\Xi$) before acquiring or opening Stage $V_5$.
3. **Stage $V_5$ (Held-out native class $h=3$, $z^{(3)} = (1, \frac{1}{2}, 0, 0)$, plus intra-fibre invariance check):**
   Acquire the complete two-cut record for $p^{(3)} = (3,0,0,0) \in \mathcal{F}_3$ (and optional predeclared second-representative fibre controls $\tilde{p}^{(h)} \in \mathcal{F}_h$, e.g. $(0,3,0,0) \in \mathcal{F}_3$).
   - **Exact model target at $h=3$:**
     $$
     12960\, b_{0,\mathrm{target}}(z^{(3)}) = (-2493, -708, 1062, 1044), \quad
     1399680\, b_{1,\mathrm{target}}(z^{(3)}) = (335636, 97483, -143487, -146637), \quad
     E_{0,\mathrm{target}}(z^{(3)}) = \frac{2}{5}, \tag{D1}
     $$
     together with the parameter-free cross-prediction residuals from (C5)–(C6):
     $$
     r_{\mathrm{cross},t}(z^{(3)}) = b_{\mathrm{cal},t}(z^{(3)}) - \bigl(b_{\mathrm{cal},t}(z^{(1)}) + b_{\mathrm{cal},t}(z^{(2)})\bigr), \qquad
     r_{\mathrm{cross},E_0}(z^{(3)}) = E_{\mathrm{cal},0}(z^{(3)}) - \bigl(2E_{\mathrm{cal},0}(z^{(1)}) + 2E_{\mathrm{cal},0}(z^{(2)}) - \tfrac{1}{4}E_{\mathrm{cal},0}(z^{(4)})\bigr). \tag{D2}
     $$
4. **Full energy boundary and interval acceptance rule:**
   For each trial $z^{(h)}$, the full-window energy residual in $E_*$ units is
   $$
   r_E(z^{(h)}) = \frac{1}{E_*}\bigl(\Delta E_{\mathrm{wave}} + \Delta E_{\mathrm{tapes}} + \Delta E_{\mathrm{control}} + \Delta E_{\mathrm{sensors}} + \Delta E_{\mathrm{records/reset}} - W_{\mathrm{external}} - Q_{\mathrm{external}}\bigr). \tag{D3}
   $$
   Retained outgoing tape deposits $E_* (2\|b_0\|^2 + 2\|b_1\|^2)$ belong to $\Delta E_{\mathrm{tapes}}$ and are not subtracted again in $W_{\mathrm{external}}$ or $Q_{\mathrm{external}}$. Unmeasured controller, native-substrate, sensor, or reset terms are not set to zero.
   Using the frozen engineering allowance $\varepsilon_y = \varepsilon_E = 1/10000$ (`CONTRACT.md` Section 4; distinct from the unrelated DP5 $1/1000$ numerical account):
   - `NOT_READY` if any Stage S or `I_FREEZE` qualification field is absent.
   - `PASS_Z5_SCOPE` if qualified and all required sound residual enclosures $I_{y,tj}(z^{(h)})$ and $I_E(z^{(h)})$ lie in $[-1/10000, +1/10000]$.
   - `FAIL` if at least one sound required interval is disjoint from $[-1/10000, +1/10000]$.
   - `UNRESOLVED` otherwise.

### 4.2 Protocol D2: Conditional full-span and mechanism-separation extensions

1. **Full 9/24 $Z_I/Z_V$ span extension:** Requires an independently qualified source adapter or extended contact supplying at least $2$ quotient-independent vectors $u^{(2)}, u^{(3)}$ satisfying (A6) (for signed responses) and $7$ vectors spanning $\mathcal{K}_{\mathrm{quad}}(\Pi_2)^*$ such as $U_{\mathrm{quad},7}$ in (C22) (for unconstrained symmetric quadratic energy). Negative-amplitude vectors such as $-e_0, -e_1$ are not operationally admitted by $Z_5$ at $n=1$ merely because they lie in $\Pi_2$; they require either an explicit sign-inverting preparation certificate or the $n=2$ contact shift of Theorem B2(2) (which produces $(-\frac{1}{2}, \frac{1}{2}, 0, 0)$ and $(-1, \frac{1}{2}, 0, 0)$).
2. **Mechanism-attribution extension ($D_{\mathrm{NC}}$ vs $D_{\mathrm{cl}}$):** Even after passing `PASS_Z5_SCOPE` or the full 9/24 $Z_I/Z_V$ test on $\Pi_{\mathrm{port}}$, mechanism attribution remains `INDISTINGUISHABLE_ON_PORT` by Theorem B1 unless supplemented by at least one of the three separating interventions of Theorem B2:
   - **Test M1:** Read out the retained native checkpoint $x_3(p)$ on distinct inputs $p \ne p'$ within the same fibre $\mathcal{F}_h$ (e.g. $p^{(0,a)}=(0,0,0,0)$ vs $p^{(0,b)}=(1,4,0,0)$ in (B3)) and verify the guarded prepared-image inverse.
   - **Test M2:** Shift the contact trigger from $n=1$ to $n=2$ and test the predicted merger $z_{n=2}^{(0)} = z_{n=2}^{(1)} = e_1$ (B5) and negative-$e_0$ energies (B6).
   - **Test M3:** Operate under a finite un-renewed energy reservoir $B$ (from `#1495`/`#1496` or Agent 1's $H_B$ interface) or multi-use continuation (from Agent 2's interface) and test the predicted threshold saturation at $h \in \{3,4\}$.
