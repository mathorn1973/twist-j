# Five-source predictive separation, calibration-to-prediction transport, and the classical-clone boundary

**NON-CANONICAL / conditional candidate-T and candidate-D / L1 analytical proof.**
Original work Apache-2.0, A. M. Thorn, 2026-10-14.
Reservation: [#1500](https://github.com/mathorn1973/twist-j/issues/1500), dispatched under [#1497](https://github.com/mathorn1973/twist-j/issues/1497).
Contract and preregistration pin: `274a88757863f55a838068e92241af1ee23f2de4` ([README.md](README.md), [CONTRACT.md](CONTRACT.md), [PREREG.md](PREREG.md), [SOURCES.json](SOURCES.json)).
Revision context: R1 analytical amendment of `58d7d6d962d847a19473dc8b233e2f844b2d378d` addressing [A4 review findings](https://github.com/mathorn1973/twist-j/pull/1503#pullrequestreview-5524640334) per [REVISION_ASSIGNMENT_A3](https://github.com/mathorn1973/twist-j/issues/1500#issuecomment-6178752881) (outcome-exposed after [administrative intake](https://github.com/mathorn1973/twist-j/issues/1497#issuecomment-6178339036) and [A4 review summary](https://github.com/mathorn1973/twist-j/issues/1497#issuecomment-6178492183)).

All derivations in this document are exact symbolic L1 proofs over $\mathbb{F}_5$ and $\mathbb{Q}$. No scientific verifier, numerical solver, or laboratory measurement was executed (`AUTHORED_PROOF`, `SELF_REVIEWED`, `NOT_INDEPENDENTLY_REVIEWED`).

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

Throughout Sections 2–4, the five marked sites $Y = \{y_0, y_1, y_2, y_3, y_4\} \subset D_3 = \{x \in \mathbb{Z}^3 : x_1 + x_2 + x_3 \equiv 0 \pmod 2\}$ and the ordered four-port readout tuple $R = (y_0, y_1, y_2, y_3)$ are frozen to the exact inherited coordinates of `notes/C-CLASSICAL-SIGNED-PORT-CONTRACT-N/CONTRACT.md` (`4302c31f07823b2a843e3702ca14620c1917b853`):

$$
y_0 = (0,0,0), \quad y_1 = (1,1,0), \quad y_2 = (1,0,1), \quad y_3 = (0,1,1), \quad y_4 = (1,-1,0) \in D_3. \tag{B0}
$$

All response matrices $M, Q, K, J, R_0, R_1$ and integer port tables $12960\,b_0, 1399680\,b_1$ in this package are expressed with respect to this exact ordered tuple $R = ((0,0,0), (1,1,0), (1,0,1), (0,1,1))$.

**Theorem B1 (Ideal classical clone indistinguishability bound).**
Let $D_{\mathrm{NC}}$ be the conditional native-contact composite machine and $D_{\mathrm{cl}}$ the ordinary rational classical wave/port comparator defined in `CONTRACT.md` Section 2.2 on the ordered port tuple (B0).

1. **On the native preparation domain $\mathcal{P}_{\mathrm{nat}} = \mathbb{F}_5^4$:** For every $p \in \mathbb{F}_5^4$, the classical port and energy record $\Pi_{\mathrm{port}}$ of $D_{\mathrm{NC}}$ equals that of $D_{\mathrm{cl}}$ identically:
   $$
   \forall p \in \mathbb{F}_5^4 : \quad \Pi_{\mathrm{port}}^{D_{\mathrm{NC}}}(p) = \Pi_{\mathrm{port}}^{D_{\mathrm{cl}}}(p)
   = \Bigl(\bigl(R_0 z^{(h(p))},\, R_1 z^{(h(p))}\bigr),\, \bigl(E_0(z^{(h(p))}), E_1(z^{(h(p))}), E_2(z^{(h(p))})\bigr),\, E_0(z^{(h(p))})\Bigr). \tag{B1}
   $$
2. **On any extended source domain $\mathcal{Z} \subseteq \mathbb{Q}^4$ (including full $\mathbb{Q}^4$ span):** Suppose an extended device pair $(D_{\mathrm{NC}}^{\mathrm{ext}}, D_{\mathrm{cl}}^{\mathrm{ext}})$ admits an enlarged preparation set $\mathcal{Z} \supseteq Z_5$ (for example by adjoining two quotient-independent directions $u^{(2)}, u^{(3)}$ satisfying (A6), or all of $Z_I \cup Z_V$) and both devices implement the same source map $z \mapsto S(z)$, cold ready state $X_{\mathrm{blank}}$, two-cut transition $F$, and observable map $\Pi_{\mathrm{port}}$ on $\mathcal{Z}$. Then
   $$
   \forall z \in \mathcal{Z} : \quad \Pi_{\mathrm{port}}^{D_{\mathrm{NC}}^{\mathrm{ext}}}(z) = \Pi_{\mathrm{port}}^{D_{\mathrm{cl}}^{\mathrm{ext}}}(z). \tag{B2}
   $$
   In particular, **no number of additional source directions in $\mathbb{Q}^4$ separates $D_{\mathrm{NC}}$ from $D_{\mathrm{cl}}$ under $\Pi_{\mathrm{port}}$**. Matched timing, retained-memory scope, and funding resources are required before any mechanism discrimination claim can be formulated.

**Proof.**
In $D_{\mathrm{NC}}$, for any $p \in \mathbb{F}_5^4$, stage 1 advances $(0, x_0(p)) \mapsto (1, x_1(p))$ while leaving $X_{\mathrm{blank}}$ and $w=0$ untouched; stage 2 applies $C_*$, which reads only $C_1(p) = C_1(h(p))$ and writes $X_0(z^{(h(p))}) = ((0, S z^{(h(p))}), (0,0), (0,0), 0)$ and $w = E_D(0, S z^{(h(p))})$; stages 3 and 4 apply $U \times F$ twice on the decoupled product $\Omega \times X$ with $w$ constant. Because $\Pi_{\mathrm{port}}$ depends only on $(X_2, w)$, the post-disconnection native steps $x_1 \mapsto x_2 \mapsto x_3$ drop out of $\Pi_{\mathrm{port}}$:
$$
\Pi_{\mathrm{port}}^{D_{\mathrm{NC}}}(p) = \Pi_{\mathrm{port}}\bigl(F^2(X_0(z^{(h(p))})),\, E_D(0, S z^{(h(p))})\bigr) = \Pi_{\mathrm{port}}^{D_{\mathrm{cl}}}(p).
$$
Likewise, for any $z \in \mathcal{Z}$ where both $D_{\mathrm{NC}}^{\mathrm{ext}}$ and $D_{\mathrm{cl}}^{\mathrm{ext}}$ prepare $(X_0(z), E_D(0, S(z)))$ and apply $F^2$ followed by $\Pi_{\mathrm{port}}$, functional composition gives $\Pi_{\mathrm{port}}(F^2(X_0(z)), E_D(0, S(z)))$ identically in both devices. $\square$

---

### 2.2 Conditional mechanism-separation witnesses against restricted comparators

Theorem B1 shows that mechanism attribution ($D_{\mathrm{NC}}$ versus a classical comparator $D_{\mathrm{cl}}$ with matched source preparation, readiness, transition $F$, and observable $\Pi_{\mathrm{port}}$) is impossible on $\Pi_{\mathrm{port}}$ alone. Rather than a necessary-and-sufficient classification of all possible mechanisms, the following theorem establishes three conditional separation witnesses against **explicitly restricted comparator classes**, while recording what each intervention does and does not exclude.

**Theorem B2 (Conditional witnesses against restricted comparator classes).**

1. **Witness M1 (Within-fibre native retention $x_3(p)$ on $\mathcal{F}_h$ versus an $h$-only comparator):**
   For each $h \in \mathbb{F}_5$, the fibre $\mathcal{F}_h = \{p \in \mathbb{F}_5^4 : \sum_{i=0}^3 p_i \equiv h \pmod 5\}$ has $|\mathcal{F}_h| = 125$. In $D_{\mathrm{NC}}$, the retained native endpoint $x_3(p) = g_{j_2(h)} g_{j_1(h)} g_{j_0(h)}(p, 0, 1)$ takes $125$ distinct values on $\mathcal{F}_h$ (invertible via $x_0 = g_{j_0(h)} g_{j_1(h)} g_{j_2(h)} x_3$), whereas an explicitly $h$-only classical comparator $D_{\mathrm{cl}}^{(h\text{-only})}$ whose state depends only on $h(p)$ is constant across $\mathcal{F}_h$. Explicitly, for the two $h=0$ preparations $p^{(0,a)} = (0,0,0,0)$ and $p^{(0,b)} = (1,4,0,0) \in \mathcal{F}_0$:
   $$
   \Pi_{\mathrm{port}}^{D_{\mathrm{NC}}}(p^{(0,a)}) = \Pi_{\mathrm{port}}^{D_{\mathrm{NC}}}(p^{(0,b)}) = \bigl((0,0), (0,0,0), 0\bigr),
   $$
   while the retained native endpoints in $D_{\mathrm{NC}}$ are distinct:
   $$
   x_3(p^{(0,a)}) = (2, 1, 3, 4, 1, 0) \ne (1, 2, 3, 4, 1, 0) = x_3(p^{(0,b)}). \tag{B3}
   $$
   *Scope and non-exclusion:* M1 breaks $h$-factorization by reading the retained native register $x_3(p)$, separating $D_{\mathrm{NC}}$ from any $h$-only comparator $D_{\mathrm{cl}}^{(h\text{-only})}$. It does **not** exclude a classical comparator that retains the full preparation $p \in \mathbb{F}_5^4$ and computes the bijection $x_3(p)$.
2. **Witness M2 (Time-shifted single contact at $n=2$ reading current $C_2(p)$ versus a static lookup comparator):**
   Suppose the single contact operation $C_*$ is triggered after two native ticks ($n=2$, reading the current receiver $C_2(p)$) instead of one ($n=1$), and compared against a static lookup comparator $D_{\mathrm{cl}}^{\mathrm{static}}$ whose front-end outputs the fixed $n=1$ source table $z^{(h(p))}$ regardless of the trigger tick. In $D_{\mathrm{NC}}$, the second-tick receivers $C_2(h)$ for $h=0,1,2,3,4$ are $(0,1), (0,1), (4,0), (3,0), (1,4)$, which under $\eta(q,r) = (\ell(q)/2, (\ell(r)+1)/2, 0, 0)$ induce the four distinct source vectors
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
   *Scope, $h$-factorization, and non-equivalence to A2:* At the fixed intervention time $n=2$, the receiver $C_2(p) = C_2(h(p))$ and source $z_{n=2}^{(h(p))}$ **still factor through $h(p)$** and do **not** distinguish inputs within any fibre $\mathcal{F}_h$. M2 separates $D_{\mathrm{NC}}$ from a static lookup comparator $D_{\mathrm{cl}}^{\mathrm{static}}$, but does **not** exclude a classical comparator implementing the same time-indexed lookup table $(n, h) \mapsto z_{n}^{(h)}$. Moreover, M2 (reading current $C_2$ at $n=2$) is a different intervention from Agent 2's (`#1499`) second contact at $n=3$, which reads the retained delayed label $d = C_{1,B}$ captured at $n=1$ (for $h_B = 0$, M2 injects $\eta(C_2(0)) = e_1$ whereas A2's delayed second contact injects $\eta(C_1(0)) = 0$).
3. **Witness M3 (Cold one-shot bounded funding under the historical $H_B$ law versus a differently funded comparator):**
   Recall from `notes/C-NATIVE-CLASSICAL-FUNDED-CONTACT-N/CONTRACT.md` (`b7636a334b09fcc68422bcd6cc6e15334d416c59`, `#1495`/`#1496`) that the bounded-store contact involution $H_B$ acts on the composite state $((n,x), ((u,v), A, B_{\mathrm{tape}}, k), w, b, \sigma)$ with fixed capacity $B \in \mathbb{Q}_{\ge 0}$, variable energy stock $b \in [0, B] \cap \mathbb{Q}$, signed work ledger $w \in \mathbb{Q}$, sign/direction bit $\sigma \in \{-1, +1\}$, and source impulse $a = S(\eta(q,r))$ by computing the signed energy increment
   $$
   \Delta_\sigma = E_D(u, v + \sigma a) - E_D(u, v) = \tfrac{1}{2}\|a\|^2 + \sigma\, a^T\bigl(v - \tfrac{1}{2}H_D u\bigr) \tag{B7}
   $$
   and applying the two-sided capacity guard
   $$
   \text{accept} \iff 0 \le b - \Delta_\sigma \le B, \tag{B8}
   $$
   with state transition
   $$
   (v, w, b, \sigma) \mapsto
   \begin{cases}
   (v + \sigma a,\, w + \Delta_\sigma,\, b - \Delta_\sigma,\, -\sigma), & \text{if } 0 \le b - \Delta_\sigma \le B\text{ (accepted)}, \\
   (v, w, b, \sigma), & \text{if } b - \Delta_\sigma < 0\text{ or } b - \Delta_\sigma > B\text{ (refused)}.
   \end{cases} \tag{B9}
   $$
   Both bounds in (B8) are essential on the full state space: the lower bound $0 \le b - \Delta_\sigma$ forbids overdraft when $\Delta_\sigma > b$, while the upper bound $b - \Delta_\sigma \le B$ forbids over-capacity recharge when an occupied wave $(u,v) \ne (0,0)$ yields negative work $\Delta_\sigma < b - B \le 0$.
   At a **cold one-shot trial** with blank wave/tapes $X_{\mathrm{blank}} = ((0,0),(0,0),(0,0),0)$, $w = 0$, initial stock $b = B = \frac{1}{5}$, and direction $\sigma = +1$, we have $\Delta_{+1}(h) = E_D(0, +S z^{(h)}) = E_0(z^{(h)}) \in \bigl(0, \frac{1}{10}, \frac{3}{20}, \frac{2}{5}, \frac{2}{5}\bigr)$ for $h = 0, 1, 2, 3, 4$. Since $0 \le \frac{1}{5} - \Delta_{+1}(h) \le \frac{1}{5}$ holds if and only if $\Delta_{+1}(h) \le \frac{1}{5}$, the guard (B8) accepts exactly $h \in \{0, 1, 2\}$ and refuses $h \in \{3, 4\}$:
   $$
   \begin{aligned}
   h \in \{0, 1, 2\} \ (\text{accepted}) &: \quad (v, w, b, \sigma) \mapsto \bigl(+S z^{(h)},\, E_0(z^{(h)}),\, \tfrac{1}{5} - E_0(z^{(h)}),\, -1\bigr), \\
   h \in \{3, 4\} \ (\text{refused}) &: \quad (v, w, b, \sigma) \mapsto \bigl(0,\, 0,\, \tfrac{1}{5},\, +1\bigr), \quad b_0 = b_1 = 0,\; E_0 = E_1 = E_2 = 0.
   \end{aligned} \tag{B10}
   $$
   *Acceptance versus zero-output projection:* Acceptance cannot be inferred from a zero port/energy/work record $\Pi_{\mathrm{port}} = ((0,0), (0,0,0), 0)$ alone: at cold $b = B = \frac{1}{5}, \sigma = +1$, both the **accepted** zero-source preparation $h = 0$ ($z^{(0)} = 0, \Delta_{+1} = 0$) and the **refused** preparation $h = 3$ ($z^{(3)} = (1,\frac{1}{2},0,0), \Delta_{+1} = \frac{2}{5} > \frac{1}{5}$) project to $\Pi_{\mathrm{port}} = ((0,0), (0,0,0), 0)$. They are separated by the retained contact state $(b, \sigma)$, which is $(\frac{1}{5}, -1)$ for accepted $h = 0$ and $(\frac{1}{5}, +1)$ for refused $h \in \{3, 4\}$ (while accepted $h \in \{1, 2\}$ already produce nonzero $(b_0, b_1)$ and $w = E_0(z^{(h)}) > 0$). Any observable used to certify acceptance in M3 must therefore explicitly include the post-contact direction $\sigma$ (or an explicit acceptance bit / store tuple $(b, \sigma)$) alongside $\Pi_{\mathrm{port}}$.
   *Scope, $h$-factorization, and unrenewed multi-trial status:* At fixed cold store/direction preparation $(b, B, \sigma) = (\frac{1}{5}, \frac{1}{5}, +1)$, M3 still factors through $h(p)$ and does not distinguish preparations within a fibre $\mathcal{F}_h$. M3 separates a device with $(b, B, \sigma) = (\frac{1}{5}, \frac{1}{5}, +1)$ from an unbounded or $b = B \ge \frac{2}{5}$ comparator on $h \in \{3, 4\}$, but does **not** exclude a classical comparator equipped with the same $(b, B, \sigma)$ state and guard (B8)–(B9). Multi-trial operation after "resetting the wave" is `UNSUPPLIED` because the unchanged contract specifies no admitted reset operation on $(u, v, A, B_{\mathrm{tape}}, k, w, b, \sigma)$.

**Proof.**
For (1), `notes/C-NATIVE-CLASSICAL-TWO-CUT-CONTACT-N/PROOF.md` Section 1 establishes that for $h=0$, $x_3(p) = (2-p_0, 1-p_1, 3-p_2, 4-p_3, 1, 0) \pmod 5$; substituting $p^{(0,a)} = (0,0,0,0)$ and $p^{(0,b)} = (1,4,0,0)$ yields $(2,1,3,4,1,0)$ and $(1,2,3,4,1,0)$.
For (2), applying $\eta(q,r) = (\ell(q)/2, (\ell(r)+1)/2, 0, 0)$ with $\ell(0,1,2,3,4) = (0,1,2,-2,-1)$ to $C_2(0) = C_2(1) = (0,1)$ gives $(0/2, (1+1)/2, 0, 0) = (0,1,0,0) = e_1 = z^{(4)}$, whose first-cut response is the $h=4$ row of the integer table $12960\,b_0 = (698, -2832, 708, 696)$; applying $\eta$ to $C_2(2) = (4,0)$ gives $(\ell(4)/2, (\ell(0)+1)/2, 0, 0) = (-1/2, 1/2, 0, 0)$ with energy $\frac{1}{2}(\frac{1}{4} + \frac{1}{4} - 0) = \frac{1}{4}$; applying $\eta$ to $C_2(3) = (3,0)$ gives $(\ell(3)/2, (\ell(0)+1)/2, 0, 0) = (-1, 1/2, 0, 0)$ with energy $\frac{1}{2}(1 + \frac{1}{4} - \frac{1}{5}(-\frac{1}{2})^2) = \frac{1}{2}(\frac{5}{4} - \frac{1}{20}) = \frac{3}{5}$; and applying $\eta$ to $C_2(4) = (1,4)$ gives $(1/2, 0, 0, 0) = z^{(1)}$.
For (3), the exact $H_B$ transition (B7)–(B9) is inherited from `notes/C-NATIVE-CLASSICAL-FUNDED-CONTACT-N/CONTRACT.md` Section 1.2 (`b7636a334b09fcc68422bcd6cc6e15334d416c59`). At $u = v = 0$ and $\sigma = +1$, $\Delta_{+1}(h) = E_D(0, S z^{(h)}) = E_0(z^{(h)}) = (0, \frac{1}{10}, \frac{3}{20}, \frac{2}{5}, \frac{2}{5})$ for $h=0,1,2,3,4$. With $b = B = \frac{1}{5} = \frac{4}{20}$, $b - \Delta_{+1}(h) = (\frac{4}{20}, \frac{2}{20}, \frac{1}{20}, -\frac{4}{20}, -\frac{4}{20})$ lies in $[0, \frac{1}{5}]$ if and only if $h \in \{0, 1, 2\}$, yielding (B10). At $h=0$, $S z^{(0)} = 0$ and $\Delta_{+1}(0) = 0$, so acceptance leaves $v=0, w=0, b=\frac{1}{5}$ and flips $\sigma = +1 \mapsto -1$, whereas at $h \in \{3,4\}$, refusal leaves $v=0, w=0, b=\frac{1}{5}, \sigma=+1$. $\square$

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
2. **Simultaneous divergence on every out-of-plane source $s \in \mathbb{Q}^4 \setminus \Pi_2$:** For every $s = s_{01} + s_{23}$ with $s_{01} \in \Pi_2$ and $s_{23} = (0, 0, s_2, s_3) \ne 0$, $J_{01} s - s = -2 s_{23} \ne 0$. Because $M$ is $4 \times 4$ and $R_0 = -\frac{1}{4}M$,
   $$
   \det R_0 = \det\left(-\tfrac{1}{4}M\right) = (-1)^4 \frac{1}{4^4}\det M = +\frac{1}{4^4}\det M = +\frac{1770^3 \cdot 365}{4^4 \cdot 1620^4} > 0 \ne 0,
   $$
   so $R_0$ is injective on $\mathbb{Q}^4$ and
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
Since $J_{01}$ fixes $e_0, e_1$ and negates $e_2, e_3$, $J_{01} z = z$ for all $z \in \Pi_2$, giving $R_t J_{01} z = R_t z$ and $z^T J_{01}^T G_{\mathrm{source}} J_{01} z = z^T G_{\mathrm{source}} z$. For any $s \notin \Pi_2$, $s_{23} = \frac{1}{2}(s - J_{01} s) \ne 0$; injectivity of $R_0 = -\frac{1}{4}M$ on $\mathbb{Q}^4$ (`notes/C-CLASSICAL-SIGNED-PORT-CONTRACT-N/PROOF.md`, where $\det(-\frac{1}{4}M) = +\frac{1}{4^4}\det M > 0$) implies $R_0(J_{01}s - s) = -2R_0 s_{23} \ne 0$. For $s = e_0 + e_2$, $J_{01}(e_0 + e_2) = e_0 - e_2$; adding and subtracting columns $0$ and $2$ of $12960\,R_0 = -2(1620\,M)$ and $1399680\,R_1 = 2(699840\,R_1)$ yields (C17), while $(e_0 \pm e_2)^T (I_4 - \frac{1}{5}\mathbf{1}\mathbf{1}^T)(e_0 \pm e_2)/2$ equals $(2 - \frac{4}{5})/2 = \frac{3}{5}$ for $+$ and $(2 - 0)/2 = 1$ for $-$. $\square$

---

### 3.3 Regime C3: Nonlinear source-dependent class $\mathcal{A}_{\mathrm{nl}}$

**Theorem C4 (Nonlinear underdetermination on every proper subset $I \subsetneq Z_5$ and on $Z_I \to Z_V$).**
In the unrestricted deterministic source-dependent class $\mathcal{A}_{\mathrm{nl}}$ (`CONTRACT.md` Section 2.1):

1. **General construction for every proper subset $I \subsetneq Z_5$ (all $31$ proper subsets of $Z_5$) and every held-out point $s \in Z_5 \setminus I$:**
   For any finite calibration subset $I \subset \mathbb{Q}^4$ and any held-out point $s \in \mathbb{Q}^4 \setminus I$ (in particular, for every proper subset $I \subsetneq Z_5$ and every $s \in Z_5 \setminus I$), define the rational polynomial Lagrange-distance indicator on $\mathbb{Q}^4$:
   $$
   L_{I,s}(z) := \prod_{a \in I} \frac{\|z - a\|^2}{\|s - a\|^2} \qquad (z \in \mathbb{Q}^4), \tag{C18a}
   $$
   with the standard convention that the empty product for $I = \emptyset$ is $L_{\emptyset,s}(z) \equiv 1$, where $\|w\|^2 = \sum_{i=0}^3 w_i^2$.
   - *Well-definedness and indicator property:* Because $s \notin I$ and the $5$ points of $Z_5$ are pairwise distinct in $\mathbb{Q}^4$, $s - a \ne 0$ for every $a \in I$. Since the Euclidean quadratic form $\|w\|^2 = \sum_{i=0}^3 w_i^2$ on $\mathbb{Q}^4$ is anisotropic ($\|w\|^2 = 0 \iff w = 0$), every denominator factor satisfies $\|s - a\|^2 \in \mathbb{Q}_{>0}$, so $\prod_{a \in I} \|s - a\|^2 > 0$ is strictly positive and $L_{I,s}(z) \in \mathbb{Q}[z_0, z_1, z_2, z_3]$ is a well-defined polynomial of degree $2|I|$ over $\mathbb{Q}$. For every $a_0 \in I$, the factor $\|z - a_0\|^2 / \|s - a_0\|^2$ vanishes at $z = a_0$, whence $L_{I,s}(a_0) = 0$ on all of $I$; at $z = s$, every factor equals $\|s - a\|^2 / \|s - a\|^2 = 1$ (and for $I = \emptyset$ the empty product is $1$), whence $L_{I,s}(s) = 1$.
   - *Complete admitted model pair $(m_*, m_{\mathrm{nl}}^{(I,s)}) \in \mathcal{A}_{\mathrm{nl}}$:* Define the complete model $m_{\mathrm{nl}}^{(I,s)} \in \mathcal{A}_{\mathrm{nl}}$ by
     $$
     \begin{aligned}
     b_{0,m_{\mathrm{nl}}^{(I,s)}}(z) &= R_0 z + L_{I,s}(z)\, e_0, \qquad
     b_{1,m_{\mathrm{nl}}^{(I,s)}}(z) = R_1 z + L_{I,s}(z)\, e_1, \\
     E_{0,m_{\mathrm{nl}}^{(I,s)}}(z) &= E_{0,m_*}(z) + L_{I,s}(z)^2, \qquad
     w_{m_{\mathrm{nl}}^{(I,s)}}(z) = E_{0,m_{\mathrm{nl}}^{(I,s)}}(z), \\
     E_{1,m_{\mathrm{nl}}^{(I,s)}}(z) &= E_{0,m_{\mathrm{nl}}^{(I,s)}}(z) - 2\bigl\|b_{0,m_{\mathrm{nl}}^{(I,s)}}(z)\bigr\|^2, \\
     E_{2,m_{\mathrm{nl}}^{(I,s)}}(z) &= E_{1,m_{\mathrm{nl}}^{(I,s)}}(z) - 2\bigl\|b_{1,m_{\mathrm{nl}}^{(I,s)}}(z)\bigr\|^2.
     \end{aligned} \tag{C18b}
     $$
     Then $b_{0,m_{\mathrm{nl}}^{(I,s)}}, b_{1,m_{\mathrm{nl}}^{(I,s)}} : \mathbb{Q}^4 \to \mathbb{Q}^4$ and $E_{0,m_{\mathrm{nl}}^{(I,s)}} : \mathbb{Q}^4 \to \mathbb{Q}$ are total rational polynomial functions and $w, E_1, E_2$ satisfy the exact two-cut ledger conservation relations of `CONTRACT.md` lines 106–111, so $m_{\mathrm{nl}}^{(I,s)} \in \mathcal{A}_{\mathrm{nl}}$. On every $a \in I$, $L_{I,s}(a) = 0$ yields $\mathcal{O}_{m_{\mathrm{nl}}^{(I,s)}}(a) = \mathcal{O}_{m_*}(a)$ and $w_{m_{\mathrm{nl}}^{(I,s)}}(a) = w_{m_*}(a)$ byte for byte, so $I(m_{\mathrm{nl}}^{(I,s)}) = I(m_*)$. At $z = s \in Z_5 \setminus I$, $L_{I,s}(s) = 1$ yields
     $$
     b_{0,m_{\mathrm{nl}}^{(I,s)}}(s) = R_0 s + e_0 \ne R_0 s = b_{0,m_*}(s), \qquad
     b_{1,m_{\mathrm{nl}}^{(I,s)}}(s) = R_1 s + e_1 \ne R_1 s = b_{1,m_*}(s), \qquad
     E_{0,m_{\mathrm{nl}}^{(I,s)}}(s) = E_{0,m_*}(s) + 1 \ne E_{0,m_*}(s),
     $$
     proving $\mathrm{Det}(\mathcal{A}_{\mathrm{nl}}, I, \{s\}) = \text{FALSE}$ for every proper subset $I \subsetneq Z_5$ and every $s \in Z_5 \setminus I$.
   - *Low-degree cubic witness for $I_4 = \{z^{(0)}, z^{(1)}, z^{(2)}, z^{(4)}\} \to z^{(3)}$:* In the special case $I_4 = \{z^{(0)}, z^{(1)}, z^{(2)}, z^{(4)}\}$ and $s = z^{(3)} = (1, \frac{1}{2}, 0, 0)$, the degree-$3$ polynomial
     $$
     \Psi_{z^{(3)}}(z) = 2 z_0 (2z_0 - 1) z_1 \tag{C18c}
     $$
     already satisfies $\Psi_{z^{(3)}}|_{I_4} = 0$ and $\Psi_{z^{(3)}}(z^{(3)}) = 1$ (and also vanishes on all $9$ points of $Z_I$), so substituting $\Psi_{z^{(3)}}(z)$ in place of $L_{I_4,z^{(3)}}(z)$ in (C18b) gives a degree-$3$/$6$ complete model pair $(m_*, m_{\mathrm{nl}})$ separating $z^{(3)}$ from $I_4 \cup Z_I$.
2. **Complete model pair $(m_*, m_{\mathrm{cross}}) \in \mathcal{A}_{\mathrm{nl}}$ on the classical 9-to-24 protocol ($Z_I \to Z_V$):**
   Every identification point $z \in Z_I = \{0, \pm e_0, \pm e_1, \pm e_2, \pm e_3\}$ has at most one nonzero coordinate, so $z_i z_j = 0$ on all $9$ points of $Z_I$ for every $0 \le i < j < 4$. Define the complete degree-$2$ polynomial model $m_{\mathrm{cross}} \in \mathcal{A}_{\mathrm{nl}}$ by specifying all observable and ledger components:
   $$
   \begin{aligned}
   b_{0,m_{\mathrm{cross}}}(z) &= R_0 z + z_0 z_1 e_0, \qquad
   b_{1,m_{\mathrm{cross}}}(z) = R_1 z, \\
   E_{0,m_{\mathrm{cross}}}(z) &= E_{0,m_*}(z) = \tfrac{1}{2}z^T G_{\mathrm{source}} z, \qquad
   w_{m_{\mathrm{cross}}}(z) = E_{0,m_{\mathrm{cross}}}(z), \\
   E_{1,m_{\mathrm{cross}}}(z) &= E_{0,m_*}(z) - 2\bigl\|R_0 z + z_0 z_1 e_0\bigr\|^2, \\
   E_{2,m_{\mathrm{cross}}}(z) &= E_{1,m_{\mathrm{cross}}}(z) - 2\|R_1 z\|^2.
   \end{aligned} \tag{C18d}
   $$
   Then $b_{0,m_{\mathrm{cross}}}, b_{1,m_{\mathrm{cross}}}, E_{0,m_{\mathrm{cross}}}$ are total polynomial maps on $\mathbb{Q}^4$ and $w, E_1, E_2$ satisfy `CONTRACT.md` lines 106–111, so $m_{\mathrm{cross}} \in \mathcal{A}_{\mathrm{nl}}$ is a complete admitted model. On every $z \in Z_I$ (and on $\{z^{(0)}, z^{(1)}, z^{(4)}\} \subset Z_5$), $z_0 z_1 = 0$, so $b_{0,m_{\mathrm{cross}}}(z) = R_0 z$, $b_{1,m_{\mathrm{cross}}}(z) = R_1 z$, $E_{0,m_{\mathrm{cross}}}(z) = E_{0,m_*}(z)$, and consequently $E_{1,m_{\mathrm{cross}}}(z) = E_{1,m_*}(z)$, $E_{2,m_{\mathrm{cross}}}(z) = E_{2,m_*}(z)$, and $w_{m_{\mathrm{cross}}}(z) = w_{m_*}(z)$; thus $I_{Z_I}(m_{\mathrm{cross}}) = I_{Z_I}(m_*)$ on all $9$ identification sources. On the superposition points $z^{(2)} = (\frac{1}{2}, \frac{1}{2}, 0, 0)$ and $z^{(3)} = (1, \frac{1}{2}, 0, 0)$ in $Z_5$, $b_{0,m_{\mathrm{cross}}}(z) - b_{0,m_*}(z)$ equals $\frac{1}{4}e_0 \ne 0$ and $\frac{1}{2}e_0 \ne 0$ respectively, and on all $4$ in-plane validation sources $s = \sigma e_0 + \rho e_1 \in Z_V \cap \Pi_2$ ($\sigma, \rho \in \{\pm 1\}$) it equals $\sigma\rho e_0 = \pm e_0 \ne 0$ (and replacing $z_0 z_1 e_0$ in (C18d) by $\bigl(\sum_{0 \le i < j < 4} z_i z_j\bigr)e_0$ preserves $I_{Z_I}(m) = I_{Z_I}(m_*)$ while diverging by $\sigma\rho e_0 = \pm e_0 \ne 0$ on all $24$ validation sources of $Z_V$).

**Proof.**
In Part (1), for any $a \in I$ and $s \notin I$, $s - a \ne 0 \implies \|s - a\|^2 = \sum_{i=0}^3 (s_i - a_i)^2 > 0$ over $\mathbb{Q}$, so $L_{I,s}(z)$ in (C18a) has nonzero rational denominator $\prod_{a \in I}\|s-a\|^2 > 0$, vanishes when $z = a_0 \in I$ because the $a_0$-factor has numerator $\|a_0 - a_0\|^2 = 0$, and equals $1$ at $z = s$ because each factor is $\|s-a\|^2/\|s-a\|^2 = 1$ (or the empty product $1$ when $I = \emptyset$). Substituting $L_{I,s}(a) = 0$ and $L_{I,s}(s) = 1$ into (C18b) verifies identical calibration on $I$ and nonzero divergence at $s$. Direct substitution of $z^{(0)}=(0,0,0,0)$ ($z_0=0$), $z^{(1)}=(\frac{1}{2},0,0,0)$ ($z_1=0$), $z^{(2)}=(\frac{1}{2},\frac{1}{2},0,0)$ ($2z_0-1=0$), $z^{(4)}=(0,1,0,0)$ ($z_0=0$), and $z^{(3)}=(1,\frac{1}{2},0,0)$ ($2 \cdot 1 \cdot 1 \cdot \frac{1}{2} = 1$) verifies (C18c). In Part (2), every $z \in Z_I$ has support of size $\le 1$, so $z_i z_j = 0$ for all $0 \le i < j < 4$, whereas every $s = \sigma e_i + \rho e_j \in Z_V$ has $s_i s_j = \sigma\rho = \pm 1 \ne 0$ and $s_k = 0$ for $k \notin \{i,j\}$, verifying (C18d). $\square$

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
| $\mathcal{A}_{\mathrm{nl}}$ | Any proper subset $I \subsetneq Z_5$ (or $Z_I$) | Any held-out $s \in Z_5 \setminus I$ (or $Z_V$) | Full $\mathcal{O}_m$ ($(b_0,b_1,E_0,E_1,E_2)$) | **UNDERDETERMINED** | Theorem C4, general $(m_*, m_{\mathrm{nl}}^{(I,s)})$ via $L_{I,s}$ in (C18a)–(C18b), cubic $\Psi_{z^{(3)}}$ in (C18c), and $(m_*, m_{\mathrm{cross}})$ in (C18d) |
| $\mathcal{A}_{\mathrm{lin}}$ | $Z_5 \cup U_{\mathrm{ext}}$ with $\operatorname{span}\pi_{23}(U_{\mathrm{ext}})=\mathbb{Q}^2$ ($\min |U_{\mathrm{ext}}|=2$) | All of $\mathbb{Q}^4$ (incl. all $24$ of $Z_V$) | Signed $(b_0, b_1)$ | **DETERMINED** | Theorem C5(1), (C19) |
| $\mathcal{A}_{\mathrm{lin}}$ | $Z_5 \cup Z_I$ (includes $U_{\mathrm{lin},2} = \{e_2,e_3\}$) | $16$ mixed points $\sigma e_i + \rho e_k \in Z_V$ | Full $\mathcal{O}_m$ (arbitrary $G_0 \in \mathbb{Q}^{4\times 4}_{\mathrm{sym}}$) | **UNDERDETERMINED** | Theorem C5(2), witness $(m_*, m_{\mathrm{energy\text{-}flip}})$ in (C21) |
| $\mathcal{A}_{\mathrm{lin}}$ | $Z_5 \cup U_{\mathrm{quad},7}$ ($\min |U_{\mathrm{ext}}|=7$) | All of $\mathbb{Q}^4$ (incl. all $24$ of $Z_V$) | Full $\mathcal{O}_m$ ($(b_0,b_1,E_0,E_1,E_2)$) | **DETERMINED** | Theorem C5(2), (C22)–(C24) |
| $\mathcal{M}_{\mathrm{dyn}}$ | Any $I_{\mathrm{set}} \subseteq \mathbb{Q}^4$ (incl. all $\mathbb{Q}^4$) | Mechanism $D_{\mathrm{NC}}$ vs matched classical clone $D_{\mathrm{cl}}$ | Classical port/energy $\Pi_{\mathrm{port}}$ | **INDISTINGUISHABLE** | Theorem B1, (B1)–(B2) |

---

## 4. Prospective finite test specification and exact qualification debts (Obligation D)

### 4.1 Protocol D1: Prospective $Z_5$-scoped calibration and held-out redundancy test

Without assuming unconstructed out-of-plane sources, the existing native-contact family $Z_5$ supports an exact, non-circular within-plane S/I/V test on $\Pi_2$ under $\mathcal{A}_{\mathrm{lin}}$:

1. **Stage S (Independent pre-calibration qualification, all currently unissued $\implies$ `NOT_READY`):**
   Before opening any Stage $I_5$ or Stage $V_5$ record, the instance packet must supply independent certificates for the twelve qualification fields of `classical/OBSERVABILITY_CALIBRATION.md` Section 6 (`INSTANCE`, `SOURCE`, `READY`, `SENSORS`, `UNITS`, `CLOCK_BINS`, `CONTACT`, `STATE_ENERGY`, `BOUNDARY`, `RENEWAL`, `UNCERTAINTY`, `CUSTODY`) with positive bounded conversion scales $(A_{0,\mathrm{length}}, \tau_{\mathrm{step}}, E_*)$ and derived $V_0 = A_{0,\mathrm{length}}/\tau_{\mathrm{step}}$, $F_0 = E_*/A_{0,\mathrm{length}}$, $Z_0 = E_*\tau_{\mathrm{step}}/A_{0,\mathrm{length}}^2$, $Z_j = 2Z_0$, on the exact ordered port tuple $R = ((0,0,0), (1,1,0), (1,0,1), (0,1,1)) \in D_3^4$.
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

### 4.2 Protocol D2: Conditional full-span and restricted-comparator separation extensions

1. **Full 9/24 $Z_I/Z_V$ span extension:** Requires an independently qualified source adapter or extended contact supplying at least $2$ quotient-independent vectors $u^{(2)}, u^{(3)}$ satisfying (A6) (for signed responses) and $7$ vectors spanning $\mathcal{K}_{\mathrm{quad}}(\Pi_2)^*$ such as $U_{\mathrm{quad},7}$ in (C22) (for unconstrained symmetric quadratic energy). Negative-axis vectors $-e_0 = (-1,0,0,0)$ and $-e_1 = (0,-1,0,0)$ are **not** operationally prepared by $Z_5$ at $n=1$ or by the $n=2$ contact shift (B4): the $n=2$ receiver table $C_2(h)$ prepares only the four distinct vectors $\{e_1,\, (-\frac{1}{2}, \frac{1}{2}, 0, 0),\, (-1, \frac{1}{2}, 0, 0),\, (\frac{1}{2}, 0, 0, 0)\}$, none of which is $-e_0$ or $-e_1$. Because a linear span or linear combination is an algebraic relation on predictions rather than an admitted source-preparation operation, preparing $-e_0$ or $-e_1$ requires an independent sign-inverting or external source-preparation certificate (`UNSUPPLIED`).
2. **Conditional comparator-separation extensions (Witnesses M1–M3 of Theorem B2):** Even after passing `PASS_Z5_SCOPE` or the full 9/24 $Z_I/Z_V$ test on $\Pi_{\mathrm{port}}$, mechanism attribution against a matched classical clone $D_{\mathrm{cl}}$ remains `INDISTINGUISHABLE_ON_PORT` by Theorem B1. Each prospective intervention below tests $D_{\mathrm{NC}}$ only against its explicitly restricted comparator class:
   - **Test M1 (vs. $h$-only comparator):** Read out the retained native checkpoint $x_3(p)$ on distinct inputs $p \ne p'$ within the same fibre $\mathcal{F}_h$ (e.g. $p^{(0,a)}=(0,0,0,0)$ vs $p^{(0,b)}=(1,4,0,0)$ in (B3)) and verify the guarded prepared-image inverse (does not exclude a classical comparator retaining full $p$).
   - **Test M2 (vs. static lookup comparator at single-contact timing $n=2$):** Shift the single contact trigger from $n=1$ to $n=2$ (reading current $C_2(p)$) and test the predicted merger $z_{n=2}^{(0)} = z_{n=2}^{(1)} = e_1$ (B5) and energies (B6) (still factors through $h(p)$ at fixed $n=2$, does not exclude a time-indexed classical table, and is strictly distinct from Agent 2's `#1499` second contact at $n=3$ reading retained $d = C_{1,B}$ captured at $n=1$).
   - **Test M3 (vs. differently funded comparator under historical $H_B$):** Operate a single cold trial from $X_{\mathrm{blank}}, w=0, b=B=\frac{1}{5}, \sigma=+1$ under the full $H_B$ law (B7)–(B9) (`#1495`/`#1496`) and record both $\Pi_{\mathrm{port}}$ and the post-contact store/direction state $(b, \sigma)$ so that accepted $h=0$ ($(b,\sigma)=(\frac{1}{5},-1)$), accepted $h \in \{1,2\}$ ($(b,\sigma)=(\frac{1}{5}-E_0(z^{(h)}),-1)$, $(b_0,b_1) \ne 0$), and refused $h \in \{3,4\}$ ($(b,\sigma)=(\frac{1}{5},+1)$, $(b_0,b_1)=0$) are distinguished without inferring acceptance from a zero port/energy record alone (still factors through $h(p)$ at fixed $(b,B,\sigma)$, does not exclude a classical comparator with the same $(b,B,\sigma)$ guard, and leaves multi-trial wave-reset renewal `UNSUPPLIED`).
