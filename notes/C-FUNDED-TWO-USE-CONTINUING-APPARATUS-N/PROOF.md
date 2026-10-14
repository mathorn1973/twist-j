# Proof: `C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N`

**NON-CANONICAL / L1 symbolic mathematical proof / 2026-10-15.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1504](https://github.com/mathorn1973/twist-j/issues/1504), following [#1497#issuecomment-6179898943](https://github.com/mathorn1973/twist-j/issues/1497#issuecomment-6179898943).
Preregistration pin commit: `d4b67e44d14a2f224a0ed77eb8dd08b217711cfb`.

All notation, state carriers, conditional L1 primitives ($L_{\mathrm{buf}}, H_{B,A}, H_{B,B}$), and the 8-phase autonomous schedule $\mathcal{G}_B$ are fixed by `CONTRACT.md` (`dcaa61031604eafff9826e1eefb4809efbe492c0`) and `PREREG.md` (`deff2b951da2c6799fe757d07fbf09229cd68f2a`). All matrix and stencil entries are inherited without modification from the pinned sources in `SOURCES.json` (`23ca316806b8159a08277b83c43c2aa078eb6eb1`).

---

## Section 1. Global invertibility of the funded two-use apparatus (`Obligations 1–2`)

### 1.1 Composite state carrier $\mathcal{Z}_B$ and static-source apparatus subcarrier $\mathcal{A}_B$

For any fixed rational capacity $B \in \mathbb{Q}_{\ge 0}$, the full composite state carrier is
$$
\mathcal{Z}_B = \mathbb{N}_0 \times \mathbb{F}_5^6 \times \mathbb{F}_5^6 \times \mathcal{X} \times \mathbb{Q} \times ([0, B] \cap \mathbb{Q}) \times \{\pm 1\}^2 \times \mathbb{F}_5^2 \times (\mathbb{Z}/8\mathbb{Z}),
$$
with state tuple $Z = (n, x_A, x_B, X, W, b, (\sigma_A, \sigma_B), d, c)$ and classical wave/tape state $X = ((u, v), (A_0, A_1), (B_0, B_1), k) \in \mathcal{X}$. Holding supplied receiver labels $(r_A, r_B) \in (\mathbb{F}_5^2)^2$ fixed in place of $(\operatorname{rec}(x_A), \operatorname{rec}(x_B))$ defines the static-source apparatus subcarrier
$$
\mathcal{A}_B = \mathcal{X} \times \mathbb{Q} \times ([0, B] \cap \mathbb{Q}) \times \{\pm 1\}^2 \times \mathbb{F}_5^2.
$$

### Theorem 1 (Global bijectivity and involutivity of $L_{\mathrm{buf}}$, $H_{B,A}$, $H_{B,B}$, and $F$)

1. **Delayed-label buffer capture $L_{\mathrm{buf}}$:** On $\mathbb{F}_5^6 \times \mathbb{F}_5^2$ (and extended by identity on all other coordinates of $\mathcal{Z}_B$ or $\mathcal{A}_B$), the map $L_{\mathrm{buf}}(x_B, d) = (x_B, (d + \operatorname{rec}(x_B)) \bmod 5)$ is a global bijection with exact two-sided inverse
   $$
   L_{\mathrm{buf}}^{-1}(x_B, d') = \bigl(x_B,\, (d' - \operatorname{rec}(x_B)) \bmod 5\bigr).
   $$
2. **Reversible two-tape wave update $F$:** On $\mathcal{X}$, the map $F((u,v),(A_0,A_1),(B_0,B_1),k) = ((v, w_{\mathrm{next}}), (A_1, B_1), (b_{\mathrm{out}}, B_0), k+1 \bmod 2)$ with $w_{\mathrm{next}} = K(H v - J_0 u + 4 P A_0)$ and $b_{\mathrm{out}} = A_0 - \frac{1}{2}P^T(w_{\mathrm{next}} - u)$ is a global bijection with exact two-sided inverse
   $$
   F^{-1}\bigl((v, w_{\mathrm{next}}),\, (A_1, B_1),\, (b_{\mathrm{out}}, B_0),\, k'\bigr) = \bigl((u, v),\, (A_0, A_1),\, (B_0, B_1),\, k' - 1 \bmod 2\bigr),
   $$
   where
   $$
   u = H v - w_{\mathrm{next}} + 2 P b_{\mathrm{out}}, \qquad A_0 = b_{\mathrm{out}} + \frac{1}{2}P^T(w_{\mathrm{next}} - u).
   $$
3. **Bounded-store contact involutions $H_{B,A}$ and $H_{B,B}$:** For every $B \in \mathbb{Q}_{\ge 0}$, both $H_{B,A}$ and $H_{B,B}$ map $\mathcal{Z}_B$ into $\mathcal{Z}_B$ (and $\mathcal{A}_B$ into $\mathcal{A}_B$) and satisfy
   $$
   H_{B,A}^2 = \mathrm{id}_{\mathcal{Z}_B}, \qquad H_{B,B}^2 = \mathrm{id}_{\mathcal{Z}_B}
   $$
   globally across all accepted, refused, and occupied wave states $(u, v) \in \mathbb{Q}^D \times \mathbb{Q}^D$. Furthermore, $L_{\mathrm{buf}}$ and $H_{B,A}$ commute at phase $c = 1$: $H_{B,A} \circ L_{\mathrm{buf}} = L_{\mathrm{buf}} \circ H_{B,A}$.

#### Proof of Theorem 1

- **Part 1 ($L_{\mathrm{buf}}$):** Since $L_{\mathrm{buf}}$ fixes $x_B$, $\operatorname{rec}(x_B) \in \mathbb{F}_5^2$ is identical in the forward and backward steps. Addition and subtraction of $\operatorname{rec}(x_B)$ in the abelian group $(\mathbb{F}_5^2, +)$ are mutual two-sided inverses.
- **Part 2 ($F$):** Inherited from `#1485` (`notes/C-CLASSICAL-SIGNED-PORT-CONTRACT-N/CONTRACT.md` Theorem 1): since $K^{-1} = I + P P^T$ and $J_0 = I - P P^T$, expanding $(I + P P^T)w_{\mathrm{next}} = H v - (I - P P^T)u + 4 P A_0$ and substituting $2 P b_{\mathrm{out}} = 2 P A_0 - P P^T(w_{\mathrm{next}} - u)$ yields $H v - w_{\mathrm{next}} + 2 P b_{\mathrm{out}} = u$, and then $b_{\mathrm{out}} + \frac{1}{2}P^T(w_{\mathrm{next}} - u) = A_0$. Conversely, starting from any target tuple $((v, w_{\mathrm{next}}), (A_1, B_1), (b_{\mathrm{out}}, B_0), k') \in \mathcal{X}$ and defining $(u, A_0)$ by the inverse formulas gives $K(H v - J_0 u + 4 P A_0) = K((I + P P^T)w_{\mathrm{next}}) = w_{\mathrm{next}}$ and $A_0 - \frac{1}{2}P^T(w_{\mathrm{next}} - u) = b_{\mathrm{out}}$, proving $F \circ F^{-1} = F^{-1} \circ F = \mathrm{id}_{\mathcal{X}}$.
- **Part 3 ($H_{B,A}$ and $H_{B,B}$):** Let $i \in \{A, B\}$, where $H_{B,A}$ reads $r_A = \operatorname{rec}(x_A)$ with direction bit $\sigma_A$ and $H_{B,B}$ reads $d \in \mathbb{F}_5^2$ with direction bit $\sigma_B$. Set $a_i = S\eta(r_A)$ for $i=A$ and $a_i = S\eta(d)$ for $i=B$. Note that $H_{B,i}$ leaves $x_A, x_B, d$, and $u$ untouched, so $a_i$ is invariant under $H_{B,i}$. For any state $Z \in \mathcal{Z}_B$, $b \in [0, B] \cap \mathbb{Q}$ and
  $$
  \Delta_i(u, v, \sigma_i) = E_D(u, v + \sigma_i a_i) - E_D(u, v) = \frac{1}{2}\|a_i\|^2 + \sigma_i a_i^T\left(v - \frac{1}{2}H u\right).
  $$
  - **Case 1 (Accepted branch: $0 \le b - \Delta_i(u, v, \sigma_i) \le B$):** The image state $Z' = H_{B,i}(Z)$ has $u' = u$, $v' = v + \sigma_i a_i$, $W' = W + \Delta_i(u, v, \sigma_i)$, $b' = b - \Delta_i(u, v, \sigma_i) \in [0, B] \cap \mathbb{Q}$, and $\sigma_i' = -\sigma_i$. Therefore $Z' \in \mathcal{Z}_B$. At the image state $Z'$, the energy increment is
    $$
    \Delta_i(u', v', \sigma_i') = E_D(u, v + \sigma_i a_i - \sigma_i a_i) - E_D(u, v + \sigma_i a_i) = E_D(u, v) - E_D(u, v + \sigma_i a_i) = -\Delta_i(u, v, \sigma_i).
    $$
    Hence the post-step store candidate at $Z'$ is
    $$
    b' - \Delta_i(u', v', \sigma_i') = \bigl(b - \Delta_i(u, v, \sigma_i)\bigr) - \bigl(-\Delta_i(u, v, \sigma_i)\bigr) = b.
    $$
    Because $Z \in \mathcal{Z}_B$ guarantees $0 \le b \le B$, the two-sided guard $0 \le b' - \Delta_i(u', v', \sigma_i') \le B$ holds automatically at $Z'$. Applying $H_{B,i}$ to $Z'$ therefore takes the accepted branch and yields
    $$
    \begin{aligned}
    v'' &= v' + \sigma_i' a_i = (v + \sigma_i a_i) - \sigma_i a_i = v, \\
    W'' &= W' + \Delta_i(u', v', \sigma_i') = (W + \Delta_i) - \Delta_i = W, \\
    b'' &= b' - \Delta_i(u', v', \sigma_i') = (b - \Delta_i) + \Delta_i = b, \\
    \sigma_i'' &= -\sigma_i' = \sigma_i,
    \end{aligned}
    $$
    while all other coordinates remain unchanged. Thus $H_{B,i}(H_{B,i}(Z)) = Z$.
  - **Case 2 (Refused branch: $b - \Delta_i(u, v, \sigma_i) < 0$ or $b - \Delta_i(u, v, \sigma_i) > B$):** Here $H_{B,i}(Z) = Z \in \mathcal{Z}_B$, so applying $H_{B,i}$ a second time evaluates the identical guard condition at $Z$ and again acts as the identity: $H_{B,i}(H_{B,i}(Z)) = Z$.
  - **Commutativity at $c=1$:** $L_{\mathrm{buf}}$ reads $x_B$ and writes only $d$, whereas $H_{B,A}$ reads $(x_A, u, v, b, \sigma_A)$ and writes only $(v, W, b, \sigma_A)$. Because their read/write supports are disjoint, $H_{B,A} \circ L_{\mathrm{buf}} = L_{\mathrm{buf}} \circ H_{B,A}$. $\blacksquare$

---

### Theorem 2 (Global apparatus permutation $G_B$ and necessity of two retained direction bits)

1. **Two-sided apparatus permutation $G_B$:** For any fixed static label pair $(r_A, r_B) \in (\mathbb{F}_5^2)^2$ and any $B \in \mathbb{Q}_{\ge 0}$, each phase row map $T_c : \mathcal{A}_B \to \mathcal{A}_B$ ($c \in \mathbb{Z}/8\mathbb{Z}$) in `CONTRACT.md` Section 2.3 is a bijection with explicit inverse
   $$
   T_0^{-1} = T_7^{-1} = \mathrm{id}_{\mathcal{A}_B}, \qquad
   T_1^{-1} = (L_{\mathrm{buf}}^{(r_B)})^{-1} \circ H_{B,A}^{(r_A)}, \qquad
   T_2^{-1} = T_3^{-1} = T_5^{-1} = T_6^{-1} = F^{-1} \times \mathrm{id}, \qquad
   T_4^{-1} = H_{B,B}.
   $$
   Consequently, the clocked apparatus transition $G_B : \mathcal{A}_B \times (\mathbb{Z}/8\mathbb{Z}) \to \mathcal{A}_B \times (\mathbb{Z}/8\mathbb{Z})$ defined by $G_B(a, c) = (T_c(a), (c+1)\bmod 8)$ is a global two-sided permutation with exact inverse
   $$
   G_B^{-1}(a', c') = \Bigl(T_{(c'-1)\bmod 8}^{-1}(a'),\, (c'-1)\bmod 8\Bigr),
   $$
   and the full 8-phase period map $M_{8,B}^{(r_A, r_B)} = T_7 \circ T_6 \circ T_5 \circ T_4 \circ T_3 \circ T_2 \circ T_1 \circ T_0 : \mathcal{A}_B \to \mathcal{A}_B$ is a global bijection with inverse $(M_{8,B}^{(r_A, r_B)})^{-1} = T_0^{-1} \circ T_1^{-1} \circ T_2^{-1} \circ T_3^{-1} \circ T_4^{-1} \circ T_5^{-1} \circ T_6^{-1} \circ T_7^{-1}$.
2. **Coupled composite bijectivity on $\mathcal{Z}_B$:** Because the shared-counter native step $V(n, x_A, x_B) = (n+1, g_{j(n, x_A)}(x_A), g_{j(n, x_B)}(x_B))$ is a bijection from $\{n\} \times \mathbb{F}_5^6 \times \mathbb{F}_5^6$ onto $\{n+1\} \times \mathbb{F}_5^6 \times \mathbb{F}_5^6$ with exact inverse $V^{-1}(n', x_A', x_B') = (n'-1, g_{j(n'-1, x_A')}(x_A'), g_{j(n'-1, x_B')}(x_B'))$ for every $n' \ge 1$, the full coupled 8-phase transition $\mathcal{G}_B$ is a bijection between the $c=0, n=n_0$ slice and the $c=7, n=n_0+5$ slice of $\mathcal{Z}_B$.
3. **Explicit single-direction $\sigma$ failure witness:** Suppose the two direction bits $(\sigma_A, \sigma_B) \in \{\pm 1\}^2$ were replaced by a single shared direction bit $\sigma \in \{\pm 1\}$ initialized to $\sigma = +1$ at $c = 0$, with no mid-cycle direction reset primitive. Consider the input pair $p_A = (0,0,0,0) \in \mathcal{F}_0$ ($z_A = z^{(0)} = 0$, $a_A = 0$) and $p_B = (1,0,0,0) \in \mathcal{F}_1$ ($z_B = z^{(1)} = (\frac{1}{2},0,0,0)^T$, $a_B = S z^{(1)}$) on $\mathcal{R}_{\mathrm{blank}}(\frac{4}{5}, \frac{4}{5})$:
   - At $c = 1$ (Contact A): $\Delta_A = 0$, so the guard $0 \le \frac{4}{5} - 0 \le \frac{4}{5}$ passes and the accepted contact flips the single shared bit $\sigma: +1 \mapsto -1$ while leaving $(u, v) = (0, 0)$.
   - At $c = 2, 3$: $(u, v)$ remains $(0, 0)$ and $(b_0, b_1) = (0, 0)$.
   - At $c = 4$ (Contact B): the second contact reads $\sigma = -1$ and injects $\sigma a_B = -S z^{(1)}$ instead of $+S z^{(1)}$, producing $v = -S z^{(1)}$ and third cut $b_2 = -R_0 z^{(1)} \ne +R_0 z^{(1)}$.
   Thus a single un-reset direction bit $\sigma$ cannot execute two positive source uses on one continuing apparatus; retaining two separate direction bits $(\sigma_A, \sigma_B) \in \{\pm 1\}^2$ resolves this while keeping every phase globally involutive.

#### Proof of Theorem 2

- **Part 1:** By Theorem 1, each $T_c$ is a composition of commuting bijections on $\mathcal{A}_B$, so $T_c \circ T_c^{-1} = T_c^{-1} \circ T_c = \mathrm{id}_{\mathcal{A}_B}$. Then $G_B(G_B^{-1}(a', c')) = G_B(T_{(c'-1)\bmod 8}^{-1}(a'), (c'-1)\bmod 8) = (T_{(c'-1)\bmod 8}(T_{(c'-1)\bmod 8}^{-1}(a')), c') = (a', c')$ and similarly $G_B^{-1}(G_B(a, c)) = (a, c)$.
- **Part 2:** By `#1492` Proposition 2.1 (`probes/P-NATIVE-CLASSICAL-CONTACT-CENSUS/PROOF.md`), each canonical involution $g_k$ ($k \in \{0,1,2,3,4\}$) preserves the coordinate sum $\sum_{m=0}^5 x_m \bmod 5$. Hence $j(n, g_{j(n,x)}(x)) = j(n, x)$, and $g_{j(n,x)}^2 = \mathrm{id}$ implies $V^{-1} \circ V = \mathrm{id}$ on $\mathbb{N}_0 \times \mathbb{F}_5^6 \times \mathbb{F}_5^6$.
- **Part 3:** Direct substitution of $a_A = 0, \sigma = +1$ into $H_{B}$ at $c=1$ yields $\Delta_A = 0 \in [0, \frac{4}{5}]$, which takes the accepted branch and maps $\sigma \mapsto -1$; then at $c=4$, $(u, v) = (0, 0)$ and $\sigma = -1$ give $v \mapsto -a_B$ and $b_2 = -\frac{1}{2}P^T T(-a_B) = -R_0 z^{(1)} \ne +R_0 z^{(1)}$ since $R_0$ is invertible and $z^{(1)} \ne 0$. $\blacksquare$

---

## Section 2. Exact second-contact work in the occupied wave and input-independent two-use funding (`Obligations 3–4`)

### Theorem 3 (Closed-form occupied-wave energy increment $\Delta_B(z_A, z_B)$ and exact 25-pair rational census)

Let $Z(0) \in \mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ be any common-ready state with input pair $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$, residue sums $h_A = h(p_A)$ and $h_B = h(p_B)$, first-tick receivers $C_{1,A} = \operatorname{rec}(x_A(1)) = C_1(h_A)$ and $C_{1,B} = \operatorname{rec}(x_B(1)) = C_1(h_B)$, source vectors $z_A = \eta(C_{1,A}) = z^{(h_A)} \in Z_5$ and $z_B = \eta(C_{1,B}) = z^{(h_B)} \in Z_5$, and zero-mean five-site fields $f = S z_A$ and $g = S z_B$.

1. **Pre-contact-B wave state and archive independence at $c = 4$:**
   - At $c = 1$, $\Delta_A = E_D(0, f) - E_D(0, 0) = \frac{1}{2}\|f\|^2 = \frac{1}{2}z_A^T G_{\mathrm{source}} z_A = E_0(z_A) =: E_A(z_A)$, which is independent of $(c_0, c_1)$.
   - If Contact A is accepted ($\alpha_A = 1$, i.e. $0 \le b_{\mathrm{init}} - E_A(z_A) \le B$), the wave after $c = 1$ is $(u_1, v_1) = (0, f)$ with tapes $A = (0, 0), B_{\mathrm{out}} = (c_0, c_1)$.
   - At $c = 2$ ($F$ step 1, reading $A_0 = 0$), $w_1 = K(H f - J_0(0) + 0) = T f$ and $A$ becomes $(0, c_1)$, $B_{\mathrm{out}}$ becomes $(b_0, c_0)$.
   - At $c = 3$ ($F$ step 2, reading $A_0 = 0$), since $K J_0 = (I - \frac{1}{2}P P^T)(I - P P^T) = I - P P^T = J_0$,
     $$
     w_2 = K(H w_1 - J_0 f + 0) = (T^2 - J_0)f,
     $$
     and $A$ becomes $(c_1, c_0)$, $B_{\mathrm{out}}$ becomes $(b_1, b_0)$. Because both $c = 2$ and $c = 3$ read $A_0 = 0$, the wave $(w_1, w_2) = (T f, (T^2 - J_0)f)$ arriving at Contact B ($c = 4$) is **strictly independent** of the old archive $(c_0, c_1)$.
2. **Exact rank-one fifth-site factorization of $\Delta_B(z_A, z_B)$:**
   For any $z_A, z_B \in \mathbb{Q}^4$ with $f = S z_A$, $g = S z_B$, $s_B = \mathbf{1}^T z_B = \sum_{i=0}^3 (z_B)_i$, and $(w_1, w_2) = (T f, (T^2 - J_0)f)$ at $\sigma_B = +1$, the second-contact wave energy increment is
   $$
   \Delta_B(z_A, z_B) = E_D(w_1, w_2 + g) - E_D(w_1, w_2) = E_0(z_B) + g^T\left(w_2 - \frac{1}{2}H w_1\right),
   $$
   where the bilinear cross-work term factors through the fifth source site $y_4 = (2,0,0)$ as
   $$
   g^T\left(w_2 - \frac{1}{2}H w_1\right) = -\frac{s_B (\mu^T z_A)}{10497600}, \qquad \mu = \begin{pmatrix} 145483 \\ 173653 \\ 173653 \\ 142153 \end{pmatrix},
   $$
   so that
   $$
   \Delta_B(z_A, z_B) = E_0(z_B) - \frac{s_B (\mu^T z_A)}{10497600}.
   $$
3. **Complete 25-pair rational census on $Z_5 \times Z_5$:**
   On the five native source vectors $Z_5 = \{z^{(0)}, z^{(1)}, z^{(2)}, z^{(3)}, z^{(4)}\}$, the port sums $s(z^{(h)}) = \mathbf{1}^T z^{(h)}$, linear forms $\mu^T z^{(h)}$, and cold energies $E_0(z^{(h)}) = \frac{1}{2}(z^{(h)})^T G_{\mathrm{source}} z^{(h)}$ are:

   | $h$ | $C_1(h)$ | $z^{(h)} = \eta(C_1(h))$ | $s(z^{(h)})$ | $\mu^T z^{(h)}$ | $E_0(z^{(h)})$ |
   | :---: | :---: | :---: | :---: | :---: | :---: |
   | `0` | $(0,4)$ | $(0, 0, 0, 0)^T$ | $0$ | $0$ | $0$ |
   | `1` | $(1,4)$ | $(\frac{1}{2}, 0, 0, 0)^T$ | $\frac{1}{2}$ | $\frac{145483}{2}$ | $\frac{1}{10}$ |
   | `2` | $(1,0)$ | $(\frac{1}{2}, \frac{1}{2}, 0, 0)^T$ | $1$ | $159568$ | $\frac{3}{20}$ |
   | `3` | $(2,0)$ | $(1, \frac{1}{2}, 0, 0)^T$ | $\frac{3}{2}$ | $\frac{464619}{2}$ | $\frac{2}{5}$ |
   | `4` | $(0,1)$ | $(0, 1, 0, 0)^T$ | $1$ | $173653$ | $\frac{2}{5}$ |

   The exact rational values of $E_A(z_A)$, $E_0(z_B)$, $g^T(w_2 - \frac{1}{2}H w_1)$, $\Delta_B(z_A, z_B)$, and $W_{\mathrm{final}}(z_A, z_B) = E_A(z_A) + \Delta_B(z_A, z_B)$ across all $25$ ordered pairs $(h_A, h_B) \in (\mathbb{Z}/5\mathbb{Z})^2$ (each representing $125^2 = 15{,}625$ native input pairs $(p_A, p_B) \in \mathcal{F}_{h_A} \times \mathcal{F}_{h_B}$) are:

   | $(h_A, h_B)$ | $E_A(z_A)$ | $E_0(z_B)$ | $g^T(w_2 - \frac{1}{2}H w_1)$ | $\Delta_B(z_A, z_B)$ | $W_{\mathrm{final}}(z_A, z_B) = E_A + \Delta_B$ | $41990400 \cdot W_{\mathrm{final}}$ |
   | :---: | :---: | :---: | :---: | :---: | :---: | ---: |
   | `(0, 0)` | $0$ | $0$ | $0$ | $0$ | $0$ | `0` |
   | `(0, 1)` | $0$ | $\frac{1}{10}$ | $0$ | $\frac{1}{10}$ | $\frac{1}{10}$ | `4199040` |
   | `(0, 2)` | $0$ | $\frac{3}{20}$ | $0$ | $\frac{3}{20}$ | $\frac{3}{20}$ | `6298560` |
   | `(0, 3)` | $0$ | $\frac{2}{5}$ | $0$ | $\frac{2}{5}$ | $\frac{2}{5}$ | `16796160` |
   | `(0, 4)` | $0$ | $\frac{2}{5}$ | $0$ | $\frac{2}{5}$ | $\frac{2}{5}$ | `16796160` |
   | `(1, 0)` | $\frac{1}{10}$ | $0$ | $0$ | $0$ | $\frac{1}{10}$ | `4199040` |
   | `(1, 1)` | $\frac{1}{10}$ | $\frac{1}{10}$ | $-\frac{145483}{41990400}$ | $\frac{4053557}{41990400}$ | $\frac{8252597}{41990400}$ | `8252597` |
   | `(1, 2)` | $\frac{1}{10}$ | $\frac{3}{20}$ | $-\frac{145483}{20995200}$ | $\frac{3003797}{20995200}$ | $\frac{5103317}{20995200}$ | `10206634` |
   | `(1, 3)` | $\frac{1}{10}$ | $\frac{2}{5}$ | $-\frac{145483}{13996800}$ | $\frac{5453237}{13996800}$ | $\frac{6852917}{13996800}$ | `20558751` |
   | `(1, 4)` | $\frac{1}{10}$ | $\frac{2}{5}$ | $-\frac{145483}{20995200}$ | $\frac{8252597}{20995200}$ | $\frac{10352117}{20995200}$ | `20704234` |
   | `(2, 0)` | $\frac{3}{20}$ | $0$ | $0$ | $0$ | $\frac{3}{20}$ | `6298560` |
   | `(2, 1)` | $\frac{3}{20}$ | $\frac{1}{10}$ | $-\frac{9973}{1312200}$ | $\frac{121247}{1312200}$ | $\frac{318077}{1312200}$ | `10178464` |
   | `(2, 2)` | $\frac{3}{20}$ | $\frac{3}{20}$ | $-\frac{9973}{656100}$ | $\frac{44221}{328050}$ | $\frac{186857}{656100}$ | `11958848` |
   | `(2, 3)` | $\frac{3}{20}$ | $\frac{2}{5}$ | $-\frac{9973}{437400}$ | $\frac{164987}{437400}$ | $\frac{230597}{437400}$ | `22137312` |
   | `(2, 4)` | $\frac{3}{20}$ | $\frac{2}{5}$ | $-\frac{9973}{656100}$ | $\frac{252467}{656100}$ | $\frac{175441}{328050}$ | `22456448` |
   | `(3, 0)` | $\frac{2}{5}$ | $0$ | $0$ | $0$ | $\frac{2}{5}$ | `16796160` |
   | `(3, 1)` | $\frac{2}{5}$ | $\frac{1}{10}$ | $-\frac{154873}{13996800}$ | $\frac{1244807}{13996800}$ | $\frac{6843527}{13996800}$ | `20530581` |
   | `(3, 2)` | $\frac{2}{5}$ | $\frac{3}{20}$ | $-\frac{154873}{6998400}$ | $\frac{894887}{6998400}$ | $\frac{3694247}{6998400}$ | `22165482` |
   | `(3, 3)` | $\frac{2}{5}$ | $\frac{2}{5}$ | $-\frac{154873}{4665600}$ | $\frac{1711367}{4665600}$ | $\frac{3577607}{4665600}$ | `32198463` |
   | `(3, 4)` | $\frac{2}{5}$ | $\frac{2}{5}$ | $-\frac{154873}{6998400}$ | $\frac{2644487}{6998400}$ | $\frac{5443847}{6998400}$ | `32663082` |
   | `(4, 0)` | $\frac{2}{5}$ | $0$ | $0$ | $0$ | $\frac{2}{5}$ | `16796160` |
   | `(4, 1)` | $\frac{2}{5}$ | $\frac{1}{10}$ | $-\frac{173653}{20995200}$ | $\frac{1925867}{20995200}$ | $\frac{10323947}{20995200}$ | `20647894` |
   | `(4, 2)` | $\frac{2}{5}$ | $\frac{3}{20}$ | $-\frac{173653}{10497600}$ | $\frac{1400987}{10497600}$ | $\frac{5600027}{10497600}$ | `22400108` |
   | `(4, 3)` | $\frac{2}{5}$ | $\frac{2}{5}$ | $-\frac{173653}{6998400}$ | $\frac{2625707}{6998400}$ | $\frac{5425067}{6998400}$ | `32550402` |
   | `(4, 4)` | $\frac{2}{5}$ | $\frac{2}{5}$ | $-\frac{173653}{10497600}$ | $\frac{4025387}{10497600}$ | $\frac{8224427}{10497600}$ | `32897708` |

#### Proof of Theorem 3

1. **Wave state before Contact B:** Part 1 follows directly by substituting $u_1 = 0, v_1 = f, A_0 = 0$ into $F$ at $c=2$ and $c=3$ and using $K J_0 = J_0$.
2. **Projection onto the fifth site $y_4$:** Since $w_1 = T f = K H f$ and $w_2 = K H w_1 - J_0 f$, where $K = I - \frac{1}{2}P P^T$ and $J_0 = I - P P^T$, we have $K - \frac{1}{2}I = \frac{1}{2}(I - P P^T) = \frac{1}{2}J_0$, and therefore
   $$
   w_2 - \frac{1}{2}H w_1 = \left(K - \frac{1}{2}I\right)H w_1 - J_0 f = \frac{1}{2}J_0 H K H f - J_0 f = J_0\left(\frac{1}{2}H K H f - f\right).
   $$
   Because $P P^T$ is the orthogonal projection onto $\operatorname{span}(\delta_{y_0}, \delta_{y_1}, \delta_{y_2}, \delta_{y_3})$ and $y_4 \notin \{y_0, y_1, y_2, y_3\}$, the complementary orthogonal projection $J_0 = I - P P^T$ satisfies $J_0 \delta_{y_i} = 0$ for $i \in \{0,1,2,3\}$ and $J_0 \delta_{y_4} = \delta_{y_4}$. Applying $J_0$ to $g = S z_B = \sum_{i=0}^3 ((z_B)_i - \frac{s_B}{5})\delta_{y_i} - \frac{s_B}{5}\delta_{y_4}$ gives
   $$
   J_0 g = -\frac{s_B}{5}\delta_{y_4}.
   $$
   By symmetry of $J_0$,
   $$
   g^T\left(w_2 - \frac{1}{2}H w_1\right) = (J_0 g)^T\left(\frac{1}{2}H K H S z_A - S z_A\right) = -\frac{s_B}{5}\,\delta_{y_4}^T\left(\frac{1}{2}H K H S - S\right) z_A.
   $$
3. **Exact hand evaluation of $\delta_{y_4}^T(\frac{1}{2}H K H S - S)$:**
   Since $K = I - \frac{1}{2}P P^T$, we decompose
   $$
   \delta_{y_4}^T\left(\frac{1}{2}H K H S - S\right) = \frac{1}{2}\delta_{y_4}^T H^2 S - \frac{1}{4}(\delta_{y_4}^T H P)(P^T H S) - \delta_{y_4}^T S.
   $$
   From the frozen `#1485` stencil identities (`notes/C-CLASSICAL-SIGNED-PORT-CONTRACT-N/OBSERVABILITY_CALIBRATION.md` lines 93 and 154–192):
   - **Term 1 ($\delta_{y_4}^T S$):** Since $S e_j = \delta_{y_j} - \frac{1}{5}\sum_{m=0}^4 \delta_{y_m}$,
     $$
     \delta_{y_4}^T S = -\frac{1}{5}(1,\, 1,\, 1,\, 1).
     $$
   - **Term 2 ($(\delta_{y_4}^T H P)(P^T H S)$):** The displacements $y_4 - y_j$ for $j = 0,1,2,3$ are $(2,0,0)$ ($|d|^2=4$, weight $1$), $(1,-1,0)$ ($|d|^2=2$, weight $6$), $(1,0,-1)$ ($|d|^2=2$, weight $6$), and $(2,-1,-1)$ ($|d|^2=6 \notin \{2,4,8,10,16\}$, weight $0$), so
     $$
     \delta_{y_4}^T H P = \frac{1}{324}(1,\, 6,\, 6,\, 0).
     $$
     By `#1485` (`OBSERVABILITY_CALIBRATION.md` line 93), $P^T H S = M = \frac{1}{1620}(1770 I_4 - v\mathbf{1}^T)$ with $v = (349, 354, 354, 348)^T$. Since $(1, 6, 6, 0)v = 349 + 2124 + 2124 + 0 = 4597$ and $1770(1, 6, 6, 0) = (1770, 10620, 10620, 0)$, subtracting $4597(1, 1, 1, 1)$ over $324 \times 1620 = 524880$ gives
     $$
     (\delta_{y_4}^T H P)(P^T H S) = \frac{1}{524880}(-2827,\, 6023,\, 6023,\, -4597).
     $$
   - **Term 3 ($\delta_{y_4}^T H^2 S$):** By `#1485` (`OBSERVABILITY_CALIBRATION.md` lines 167–178), the row of $H^2$ at $y_4$ on $(y_0, y_1, y_2, y_3, y_4)$ is
     $$
     \bigl((H^2)_{y_4, y_0},\, (H^2)_{y_4, y_1},\, (H^2)_{y_4, y_2},\, (H^2)_{y_4, y_3},\, (H^2)_{y_4, y_4}\bigr) = \frac{1}{104976}(1038,\, 4740,\, 4740,\, 528,\, 132768) = \frac{1}{17496}(173,\, 790,\, 790,\, 88,\, 22128),
     $$
     whose five-site sum is $\frac{173 + 790 + 790 + 88 + 22128}{17496} = \frac{23969}{17496}$. Therefore, for $j \in \{0,1,2,3\}$, $(\delta_{y_4}^T H^2 S)_j = (H^2)_{y_4, y_j} - \frac{23969}{87480} = \frac{5(173, 790, 790, 88)_j - 23969}{87480}$, namely
     $$
     \delta_{y_4}^T H^2 S = \frac{1}{87480}(-23104,\, -20019,\, -20019,\, -23529).
     $$
   - **Combination over common denominator $2099520 = 24 \times 87480 = 4 \times 524880$:**
     $$
     \begin{aligned}
     2099520\,\delta_{y_4}^T\left(\frac{1}{2}H K H S - S\right)
     &= 12(-23104,\, -20019,\, -20019,\, -23529) - (-2827,\, 6023,\, 6023,\, -4597) + 419904(1,\, 1,\, 1,\, 1) \\
     &= (-277248 + 2827 + 419904,\; -240228 - 6023 + 419904,\; -240228 - 6023 + 419904,\; -282348 + 4597 + 419904) \\
     &= (145483,\, 173653,\, 173653,\, 142153) = \mu^T.
     \end{aligned}
     $$
     Multiplying by $-\frac{s_B}{5}$ with $5 \times 2099520 = 10497600$ yields $g^T(w_2 - \frac{1}{2}H w_1) = -\frac{s_B (\mu^T z_A)}{10497600}$, and evaluating on each pair $(z^{(h_A)}, z^{(h_B)}) \in Z_5 \times Z_5$ gives the 25-row table in Part 3. $\blacksquare$

---

### Theorem 4 (Input-independent two-use store capacity bounds, branch classification, and explicit refusal & warm witnesses)

1. **Sharp bounds on $Z_5 \times Z_5$:** Across all $25$ ordered source pairs $(z_A, z_B) \in Z_5 \times Z_5$:
   $$
   0 \le E_A(z_A) \le \frac{2}{5}, \qquad
   -\frac{154873}{4665600} = -\frac{464619}{13996800} \le g^T\left(w_2 - \frac{1}{2}H w_1\right) \le 0, \qquad
   0 \le \Delta_B(z_A, z_B) \le \frac{2}{5},
   $$
   with $\Delta_B(z_A, z_B) = 0 \iff z_B = z^{(0)} = 0$, and total two-use work
   $$
   0 \le W_{\mathrm{final}}(z_A, z_B) = E_A(z_A) + \Delta_B(z_A, z_B) \le W_{\mathrm{final}}(z^{(4)}, z^{(4)}) = \frac{8224427}{10497600} < \frac{4}{5} = \frac{8398080}{10497600}.
   $$
2. **Input-independent two-use funding condition:** On $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$, an input-independent rational store initialization $(b_{\mathrm{init}}, B)$ accepts **both** Contact A ($c=1$) and Contact B ($c=4$) (`(ACC, ACC)`, $(\sigma_A, \sigma_B)_{\mathrm{final}} = (-1, -1)$) across all $25$ source pairs in $Z_5 \times Z_5$ and all $625^2 = 390{,}625$ native input pairs $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$ if and only if
   $$
   B_* := \frac{8224427}{10497600} \le b_{\mathrm{init}} \le B.
   $$
   In particular:
   - At the **canonical cold two-use capacity** $b_{\mathrm{init}} = B = \frac{4}{5} = \frac{8398080}{10497600}$, all $25$ source pairs ($390{,}625$ native pairs) take `(ACC, ACC)` with strictly positive minimum final store reserve $b_{\mathrm{final}}(z^{(4)}, z^{(4)}) = \frac{173653}{10497600} > 0$.
   - At the **sharp input-independent threshold** $b_{\mathrm{init}} = B = B_* = \frac{8224427}{10497600}$, all $25$ source pairs take `(ACC, ACC)`, with $b_{\mathrm{final}}(z^{(4)}, z^{(4)}) = 0$.
3. **Complete four-branch classification and explicit refusal witnesses at lower capacities:**
   - **At single-use cold capacity $b_{\mathrm{init}} = B = \frac{2}{5}$:** Contact A is accepted for all $5$ values of $h_A$ ($0 \le E_A(z_A) \le \frac{2}{5}$), while Contact B partitions the $25$ pairs into:
     - **`(ACC, ACC)` ($13$ pairs / $203{,}125$ native pairs):**
       $$
       \bigl\{(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2), (3,0), (4,0)\bigr\}.
       $$
     - **`(ACC, REF)` ($12$ pairs / $187{,}500$ native pairs):**
       $$
       \bigl\{(1,3), (1,4), (2,3), (2,4), (3,1), (3,2), (3,3), (3,4), (4,1), (4,2), (4,3), (4,4)\bigr\}.
       $$
       *Explicit witness:* On $(h_A, h_B) = (3, 3)$ (e.g. $p_A = p_B = (3,0,0,0)$) at $b_{\mathrm{init}} = B = \frac{2}{5}$, Contact A is accepted with $E_A = \frac{2}{5}$, $b_1 = 0$, $\sigma_A = -1$; at Contact B ($c=4$), $\Delta_B(z^{(3)}, z^{(3)}) = \frac{1711367}{4665600} > 0$ violates the lower guard $b_1 - \Delta_B = -\frac{1711367}{4665600} < 0$, so Contact B is refused (`(ACC, REF)`), leaving $(\sigma_A, \sigma_B)_{\mathrm{final}} = (-1, +1)$, $W_{\mathrm{final}} = \frac{2}{5}$, and $b_{\mathrm{final}} = 0$.
   - **At intermediate capacity $b_{\mathrm{init}} = B = \frac{1}{5}$:** All four acceptance/refusal regimes are simultaneously inhabited across the $25$ pairs:
     - **`(ACC, ACC)` ($6$ pairs / $93{,}750$ native pairs):** $\{(0,0), (0,1), (0,2), (1,0), (1,1), (2,0)\}$, where $E_A \le \frac{1}{5}$ and $E_A + \Delta_B \le \frac{1}{5}$ (including $(1,1)$ with $W_{\mathrm{final}} = \frac{8252597}{41990400} < \frac{8398080}{41990400} = \frac{1}{5}$).
     - **`(ACC, REF)` ($9$ pairs / $140{,}625$ native pairs):** $\{(0,3), (0,4), (1,2), (1,3), (1,4), (2,1), (2,2), (2,3), (2,4)\}$, where $E_A \le \frac{1}{5}$ but $E_A + \Delta_B > \frac{1}{5}$.
     - **`(REF, ACC)` ($6$ pairs / $93{,}750$ native pairs):** $\{(3,0), (3,1), (3,2), (4,0), (4,1), (4,2)\}$, where Contact A is refused ($E_A = \frac{2}{5} > \frac{1}{5}$, so $u=v=0, b_1 = \frac{1}{5}, \sigma_A = +1$) and Contact B sees the cold wave $(0,0)$ with $\Delta_B = E_0(z_B) \in \{0, \frac{1}{10}, \frac{3}{20}\} \le \frac{1}{5}$ and is accepted ($\sigma_B = -1$).
     - **`(REF, REF)` ($4$ pairs / $62{,}500$ native pairs):** $\{(3,3), (3,4), (4,3), (4,4)\}$, where Contact A is refused ($E_A = \frac{2}{5} > \frac{1}{5}$) and Contact B is also refused ($\Delta_B = E_0(z_B) = \frac{2}{5} > \frac{1}{5}$), leaving $(\sigma_A, \sigma_B)_{\mathrm{final}} = (+1, +1)$.
4. **Occupied-wave (`WARM`) archive/tape witness outside $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$:**
   While $(c_0, c_1) \in B_{\mathrm{out}}$ at $c=0$ enters the wave only at $c=5, 6$ (after Contact B at $c=4$), if the active input tape $A_0$ is non-zero before Contact B (or if a subsequent un-rezeroed cycle $c \in \{8, \dots, 15\}$ is entered after $c_1 = e_0$ was injected at $c=5$), the ambient wave modifies $\Delta_B$. Specifically, if $A_{\mathrm{init}} = (0, e_0)$ at $c=0$ with $p_A = (0,0,0,0)$ ($z_A = 0$) and $p_B = (1,0,0,0)$ ($z_B = (\frac{1}{2},0,0,0)^T$), then $c=2$ shifts $A_1 = e_0$ into $A_0$, and $c=3$ injects $4 P e_0$ into $w_2 = 4 K P e_0 = 2 P e_0$ with $w_1 = 0$. At $c=4$, Contact B sees $(u, v) = (0, 2 P e_0)$ and experiences
   $$
   \Delta_B^{\mathrm{warm}} = E_0(z^{(1)}) + (S z^{(1)})^T(2 P e_0) = \frac{1}{10} + 2(z^{(1)})^T G_{\mathrm{source}} e_0 = \frac{1}{10} + 2\left(\frac{1}{2}\right)\left(\frac{4}{5}\right) = \frac{9}{10} > \frac{4}{5},
   $$
   which violates the lower guard $b - \Delta_B^{\mathrm{warm}} = \frac{4}{5} - \frac{9}{10} = -\frac{1}{10} < 0$ even at $b_{\mathrm{init}} = B = \frac{4}{5}$. Similarly, if $(u, v) = (0, -2 P e_0)$ with $b = b_{\mathrm{init}} = B$, then $\Delta_B^{\mathrm{warm}} = \frac{1}{10} - \frac{4}{5} = -\frac{7}{10} < 0$, which violates the **upper** guard $b - \Delta_B^{\mathrm{warm}} = B + \frac{7}{10} > B$, demonstrating why both inequalities of the two-sided guard $0 \le b - \Delta_i \le B$ are required for global involutivity on $\mathcal{Z}_B$.

#### Proof of Theorem 4

All inequalities and branch memberships in Parts 1–3 follow directly from the exact rational numerators over $41990400$ in the table of Theorem 3:
- Since $E_A(z_A) \ge 0$ and $\Delta_B(z_A, z_B) \ge 0$ for all $25$ pairs, $b_{\mathrm{init}} - E_A \le b_{\mathrm{init}} \le B$ and $b_{\mathrm{init}} - E_A - \Delta_B \le b_{\mathrm{init}} \le B$ hold whenever $b_{\mathrm{init}} \le B$.
- The lower guards $b_{\mathrm{init}} - E_A(z_A) \ge 0$ and $b_{\mathrm{init}} - W_{\mathrm{final}}(z_A, z_B) \ge 0$ hold for all $25$ pairs if and only if $b_{\mathrm{init}} \ge \max_{Z_5^2} W_{\mathrm{final}}(z_A, z_B) = W_{\mathrm{final}}(z^{(4)}, z^{(4)}) = \frac{8224427}{10497600} = B_*$.
- Comparing $41990400 \cdot E_A \in \{0, 4199040, 6298560, 16796160\}$ and $41990400 \cdot W_{\mathrm{final}}$ against $41990400 \cdot \frac{2}{5} = 16796160$ and $41990400 \cdot \frac{1}{5} = 8398080$ gives the exact 13/12 partition at $B = \frac{2}{5}$ and the exact 6/9/6/4 partition at $B = \frac{1}{5}$.
- Part 4 follows by direct substitution of $(u, v) = (0, \pm 2 P e_0)$ and $P^T S z^{(1)} = G_{\mathrm{source}} z^{(1)} = (\frac{2}{5}, -\frac{1}{10}, -\frac{1}{10}, -\frac{1}{10})^T$ into $\Delta_B$. $\blacksquare$

---

## Section 3. Four-cut record retention, acceptance/refusal discrimination, and native prepared-image inverse (`Obligation 5`)

### Theorem 5 (Unified four-cut formulas, archive-independent source decoding, accepted-zero vs. refusal discrimination, and exact native left inverse)

Let $Z(0) \in \mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ be any common-ready state with input pair $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$, source pair $z_A = z^{(h(p_A))}, z_B = z^{(h(p_B))} \in Z_5$, fields $f = S z_A, g = S z_B$, and acceptance indicators $\alpha_A = \frac{1 - \sigma_{A,\mathrm{final}}}{2} \in \{0, 1\}$, $\alpha_B = \frac{1 - \sigma_{B,\mathrm{final}}}{2} \in \{0, 1\}$.

1. **Phase-by-phase retention table across all 8 phases ($c = 0, \dots, 7$):**
   Writing $u_1 = 0, v_1 = \alpha_A f$, $w_1 = \alpha_A T f$, $w_2 = \alpha_A(T^2 - J_0)f$, $w_2^+ = w_2 + \alpha_B g$, $w_3 = K(H w_2^+ - J_0 w_1 + 4 P c_1)$, and $w_4 = K(H w_3 - J_0 w_2^+ + 4 P c_0)$, the state at the end of each phase $c \in \{0, \dots, 7\}$ is:

   | End of phase $c$ | $n$ | Wave $(u, v)$ | Input tape $A = (A_0, A_1)$ | Output tape $B_{\mathrm{out}} = (B_0, B_1)$ | $k$ | $(W, b)$ | $(\sigma_A, \sigma_B)$ | $d$ |
   | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
   | `0` | $1$ | $(0, 0)$ | $(0, 0)$ | $(c_0, c_1)$ | $0$ | $(0, b_{\mathrm{init}})$ | $(+1, +1)$ | $(0, 0)$ |
   | `1` | $1$ | $(0, \alpha_A f)$ | $(0, 0)$ | $(c_0, c_1)$ | $0$ | $(\alpha_A E_A, b_{\mathrm{init}} - \alpha_A E_A)$ | $(1-2\alpha_A, +1)$ | $C_{1,B}$ |
   | `2` | $2$ | $(\alpha_A f, w_1)$ | $(0, c_1)$ | $(b_0, c_0)$ | $1$ | $(\alpha_A E_A, b_{\mathrm{init}} - \alpha_A E_A)$ | $(1-2\alpha_A, +1)$ | $C_{1,B}$ |
   | `3` | $3$ | $(w_1, w_2)$ | $(c_1, c_0)$ | $(b_1, b_0)$ | $0$ | $(\alpha_A E_A, b_{\mathrm{init}} - \alpha_A E_A)$ | $(1-2\alpha_A, +1)$ | $C_{1,B}$ |
   | `4` | $3$ | $(w_1, w_2^+)$ | $(c_1, c_0)$ | $(b_1, b_0)$ | $0$ | $(W_{\mathrm{final}}, b_{\mathrm{final}})$ | $(1-2\alpha_A, 1-2\alpha_B)$ | $C_{1,B}$ |
   | `5` | $4$ | $(w_2^+, w_3)$ | $(c_0, b_0)$ | $(b_2, b_1)$ | $1$ | $(W_{\mathrm{final}}, b_{\mathrm{final}})$ | $(1-2\alpha_A, 1-2\alpha_B)$ | $C_{1,B}$ |
   | `6` | $5$ | $(w_3, w_4)$ | $(b_0, b_1)$ | $(b_3, b_2)$ | $0$ | $(W_{\mathrm{final}}, b_{\mathrm{final}})$ | $(1-2\alpha_A, 1-2\alpha_B)$ | $C_{1,B}$ |
   | `7` | $5$ | $(w_3, w_4)$ | $(b_0, b_1)$ | $(b_3, b_2)$ | $0$ | $(W_{\mathrm{final}}, b_{\mathrm{final}})$ | $(1-2\alpha_A, 1-2\alpha_B)$ | $C_{1,B}$ |

   At the period boundary $c = 7, n = 5$, all four chronological signed port cuts $(b_0, b_1, b_2, b_3)$ are simultaneously retained in the four tape slots $(A_0, A_1, B_1, B_0) = (b_0, b_1, b_2, b_3)$, and $(b_0, b_1)$ are readable at every boundary from $c = 3$ through $c = 7$.
2. **Unified four-cut branch output equations:** Across all four acceptance/refusal branches $(\alpha_A, \alpha_B) \in \{0, 1\}^2$,
   $$
   b_0 = \alpha_A R_0 z_A, \qquad
   b_1 = \alpha_A R_1 z_A, \qquad
   b_2 = \alpha_A D_2(z_A) + \alpha_B R_0 z_B, \qquad
   b_3 = \alpha_A D_3(z_A) + \alpha_B R_1 z_B - \frac{1}{2}J_p c_1,
   $$
   where
   $$
   \begin{aligned}
   R_0 &= -\frac{1}{2}P^T T S = -\frac{1}{4}M = -\frac{1}{6480}(1770 I_4 - v\mathbf{1}^T), & v &= (349, 354, 354, 348)^T, \\
   R_1 &= \frac{1}{2}G_{\mathrm{source}} - \frac{1}{2}P^T T^2 S, & J_p &= P^T T P - I_4 = \frac{1}{2}P^T H P - I_4, \\
   D_2(z_A) &= \frac{1}{2}P^T(T - T^3 + T J_0)S z_A, & D_3(z_A) &= \frac{1}{2}P^T\bigl((T^2 - J_0) - T^4 + T^2 J_0 + J_0 T^2 - J_0\bigr)S z_A.
   \end{aligned}
   $$
   Specifically, the five single-source port-cut vectors $R_0 z^{(h)}$ and $R_1 z^{(h)}$ on $Z_5$ (from `#1492` Theorem 2.2) are:

   | $h$ | $R_0 z^{(h)} \in \mathbb{Q}^4$ | $R_1 z^{(h)} \in \mathbb{Q}^4$ |
   | :---: | :---: | :---: |
   | `0` | $(0, 0, 0, 0)^T$ | $(0, 0, 0, 0)^T$ |
   | `1` | $\frac{1}{12960}(-1421, 354, 354, 348)^T$ | $\frac{1}{20995200}(62683, -1042902, -1042902, -1039542)^T$ |
   | `2` | $\frac{1}{12960}(-1072, -1062, 708, 696)^T$ | $\frac{1}{20995200}(-980219, -960509, -2087829, -2082444)^T$ |
   | `3` | $\frac{1}{12960}(-2493, -708, 1062, 1044)^T$ | $\frac{1}{20995200}(-917536, -2003411, -3130731, -3121986)^T$ |
   | `4` | $\frac{1}{6480}(349, -1416, 354, 348)^T$ | $\frac{1}{10497600}(-521451, 41195, -522463, -521451)^T$ |

3. **Archive-independent recovery of $(z_A, z_B)$ on `(ACC, ACC)`:**
   Since $\det(M) = \frac{131793881}{170061120} \ne 0$ (`#1485` Theorem 4), $R_0 = -\frac{1}{4}M$ is invertible over $\mathbb{Q}^4$ with exact closed-form inverse
   $$
   R_0^{-1} = -4 M^{-1} = -\frac{36}{59}\left(5 I_4 + \frac{1}{699}v\mathbf{1}^T\right), \qquad v = (349, 354, 354, 348)^T.
   $$
   Whenever $(\sigma_A, \sigma_B)_{\mathrm{final}} = (-1, -1)$ ($\alpha_A = \alpha_B = 1$), both source vectors $(z_A, z_B) \in \mathbb{Q}^4 \times \mathbb{Q}^4$ are uniquely recovered from $(b_0, b_2) = (A_{0,\mathrm{final}}, B_{1,\mathrm{final}})$ independently of the old archive $(c_0, c_1)$ via
   $$
   z_A = R_0^{-1} b_0 = -4 M^{-1} b_0, \qquad
   z_B = R_0^{-1}\bigl(b_2 - D_2(z_A)\bigr) = -4 M^{-1}\bigl(b_2 - D_2(-4 M^{-1} b_0)\bigr).
   $$
   On $Z_5 \times Z_5$, this uniquely determines $(h_A, h_B) \in (\mathbb{Z}/5\mathbb{Z})^2$ and $(C_{1,A}, C_{1,B})$ (agreeing with $d_{\mathrm{final}} = C_{1,B}$).
4. **Accepted-zero vs. refusal discrimination via $(\sigma_A, \sigma_B)_{\mathrm{final}}$:**
   On $\mathcal{R}_{(c_0, 0, \frac{1}{5}, \frac{1}{5})}$, the four source pairs $(h_A, h_B) \in \{(0,0), (0,3), (3,0), (3,3)\}$ (for example $p^{(0)} = (0,0,0,0)$ and $p^{(3)} = (3,0,0,0)$) all produce identical classical wave/tape states $(u_{\mathrm{final}}, v_{\mathrm{final}}) = (w_3, w_4)$ and identical four-cut records $(b_0, b_1, b_2, b_3) = (0, 0, 0, 0)$ together with identical work/store $(W_{\mathrm{final}}, b_{\mathrm{final}}) = (0, \frac{1}{5})$. They are discriminated on the apparatus carrier by, and only by, $(\sigma_A, \sigma_B)_{\mathrm{final}}$ (together with $d_{\mathrm{final}} = C_1(h_B)$ for the second slot):
   - $(0, 0) \in \text{(ACC, ACC)} \implies (\sigma_A, \sigma_B)_{\mathrm{final}} = (-1, -1)$ (both contacts accepted with zero source $z^{(0)} = 0$);
   - $(0, 3) \in \text{(ACC, REF)} \implies (\sigma_A, \sigma_B)_{\mathrm{final}} = (-1, +1)$ (Contact A accepted zero; Contact B refused $z^{(3)}$);
   - $(3, 0) \in \text{(REF, ACC)} \implies (\sigma_A, \sigma_B)_{\mathrm{final}} = (+1, -1)$ (Contact A refused $z^{(3)}$; Contact B accepted zero);
   - $(3, 3) \in \text{(REF, REF)} \implies (\sigma_A, \sigma_B)_{\mathrm{final}} = (+1, +1)$ (both contacts refused $z^{(3)}$).
5. **Exact left inverse $\mathcal{D}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ and image recognizer on $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$:**
   For every $(c_0, c_1) \in (\mathbb{Q}^4)^2$ and every $0 \le b_{\mathrm{init}} \le B$, let $\Phi_{(c_0, c_1, b_{\mathrm{init}}, B)} : \mathbb{F}_5^4 \times \mathbb{F}_5^4 \to \mathcal{Z}_B$ map $(p_A, p_B)$ to the boundary state $Z_{\mathrm{final}} = \mathcal{G}_B^8(Z(0))$ at $c = 7, n = 5$. Define the left inverse $\mathcal{D} : \operatorname{Im}(\Phi_{(c_0, c_1, b_{\mathrm{init}}, B)}) \to \mathbb{F}_5^4 \times \mathbb{F}_5^4$ by applying five inverse native steps $V^{-5}$ to $(5, x_A(5), x_B(5))$:
   $$
   (0, \hat{x}_A(0), \hat{x}_B(0)) := V^{-5}(5, x_A(5), x_B(5)), \qquad
   \mathcal{D}(Z_{\mathrm{final}}) := \bigl((\hat{x}_A(0)_0, \dots, \hat{x}_A(0)_3),\, (\hat{x}_B(0)_0, \dots, \hat{x}_B(0)_3)\bigr).
   $$
   Then $\mathcal{D}(\Phi_{(c_0, c_1, b_{\mathrm{init}}, B)}(p_A, p_B)) = (p_A, p_B)$ for all $625^2 = 390{,}625$ native input pairs $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$ across all four acceptance/refusal branches. Moreover, an arbitrary state $Z = (n, x_A, x_B, X, W, b, (\sigma_A, \sigma_B), d, c) \in \mathcal{Z}_B$ lies in $\operatorname{Im}(\Phi_{(c_0, c_1, b_{\mathrm{init}}, B)})$ if and only if:
   1. $n = 5$ and $c = 7$;
   2. $(0, \hat{x}_A(0), \hat{x}_B(0)) := V^{-5}(5, x_A, x_B)$ has last two coordinates $(\hat{x}_A(0)_4, \hat{x}_A(0)_5) = (0, 1)$ and $(\hat{x}_B(0)_4, \hat{x}_B(0)_5) = (0, 1)$;
   3. Setting $(1, \hat{x}_A(1), \hat{x}_B(1)) := V(0, \hat{x}_A(0), \hat{x}_B(0))$, $z_A := \eta(\operatorname{rec}(\hat{x}_A(1)))$, and $z_B := \eta(\operatorname{rec}(\hat{x}_B(1)))$, the delayed buffer satisfies $d = \operatorname{rec}(\hat{x}_B(1))$;
   4. Defining $\alpha_A^{\mathrm{req}} := \mathbf{1}_{[0, B]}(b_{\mathrm{init}} - E_0(z_A))$ and $\Delta_B^{\mathrm{req}} := E_0(z_B) - \alpha_A^{\mathrm{req}}\frac{s_B(\mu^T z_A)}{10497600}$ and $\alpha_B^{\mathrm{req}} := \mathbf{1}_{[0, B]}(b_{\mathrm{init}} - \alpha_A^{\mathrm{req}} E_0(z_A) - \Delta_B^{\mathrm{req}})$, the retained direction bits satisfy $(\sigma_A, \sigma_B) = (1 - 2\alpha_A^{\mathrm{req}}, 1 - 2\alpha_B^{\mathrm{req}})$;
   5. $W = \alpha_A^{\mathrm{req}} E_0(z_A) + \alpha_B^{\mathrm{req}} \Delta_B^{\mathrm{req}}$ and $b = b_{\mathrm{init}} - W$;
   6. $X$ equals the exact 4-step classical state $((w_3, w_4), (b_0, b_1), (b_3, b_2), 0)$ from Part 1 for $(\alpha_A^{\mathrm{req}}, \alpha_B^{\mathrm{req}}, z_A, z_B, c_0, c_1)$.

#### Proof of Theorem 5

- **Parts 1–2:** Tracking the four steps of $F$ at $c = 2, 3, 5, 6$:
  - At $c=2$: $w_1 = \alpha_A T f$ and $b_0 = 0 - \frac{1}{2}P^T(w_1 - 0) = -\frac{1}{2}\alpha_A P^T T S z_A = \alpha_A R_0 z_A$.
  - At $c=3$: $w_2 = \alpha_A(T^2 - J_0)f$ and $b_1 = 0 - \frac{1}{2}P^T(w_2 - \alpha_A f) = \alpha_A(\frac{1}{2}P^T S - \frac{1}{2}P^T T^2 S)z_A = \alpha_A R_1 z_A$ since $P^T J_0 = 0$.
  - At $c=4$: $H_{B,B}$ maps $w_2 \mapsto w_2^+ = w_2 + \alpha_B g$.
  - At $c=5$ ($A_0 = c_1$): $w_3 = K(H w_2^+ - J_0 w_1 + 4 P c_1) = \alpha_A(T^3 - T J_0 - J_0 T)f + \alpha_B T g + 2 P c_1$ since $K P = \frac{1}{2}P$. Then
    $$
    b_2 = c_1 - \frac{1}{2}P^T(w_3 - w_1) = c_1 - \frac{1}{2}\alpha_A P^T(T^3 - T J_0 - T)f - \frac{1}{2}\alpha_B P^T T g - P^T P c_1 = \alpha_A D_2(z_A) + \alpha_B R_0 z_B,
    $$
    because $P^T J_0 = 0$ and $c_1 - P^T P c_1 = 0$.
  - At $c=6$ ($A_0 = c_0$): $w_4 = K(H w_3 - J_0 w_2^+ + 4 P c_0) = \alpha_A(T^4 - T^2 J_0 - T J_0 T - J_0(T^2 - J_0))f + \alpha_B(T^2 - J_0)g + 2 T P c_1 + 2 P c_0$. Since $P^T J_0 = 0$ and $c_0 - \frac{1}{2}P^T(2 P c_0) = 0$,
    $$
    b_3 = c_0 - \frac{1}{2}P^T(w_4 - w_2^+) = \alpha_A D_3(z_A) + \alpha_B R_1 z_B - \frac{1}{2}(P^T T P - I_4)c_1 = \alpha_A D_3(z_A) + \alpha_B R_1 z_B - \frac{1}{2}J_p c_1.
    $$
- **Part 3:** When $\alpha_A = \alpha_B = 1$, $b_0 = R_0 z_A$ and $b_2 = D_2(z_A) + R_0 z_B$. Multiplying by $R_0^{-1} = -4 M^{-1}$ yields $z_A = R_0^{-1} b_0$ and $z_B = R_0^{-1}(b_2 - D_2(z_A))$.
- **Part 4:** At $b_{\mathrm{init}} = B = \frac{1}{5}$ and $c_1 = 0$, for any $(h_A, h_B) \in \{(0,0), (0,3), (3,0), (3,3)\}$, either $h_i = 0$ ($\alpha_i = 1, z^{(0)} = 0$) or $h_i = 3$ ($\alpha_i = 0, z^{(3)} \ne 0$). In every case $\alpha_A z_A = 0$ and $\alpha_B z_B = 0$, so $(b_0, b_1, b_2, b_3) = (0, 0, 0, 0)$ and $(W_{\mathrm{final}}, b_{\mathrm{final}}) = (0, \frac{1}{5})$, while $(\sigma_A, \sigma_B)_{\mathrm{final}} = (1 - 2\alpha_A, 1 - 2\alpha_B)$ takes the four distinct values $(-1,-1), (-1,+1), (+1,-1), (+1,+1)$.
- **Part 5:** By Theorem 2 Part 2, $V^5$ is a bijection from $\{0\} \times \mathbb{F}_5^6 \times \mathbb{F}_5^6$ to $\{5\} \times \mathbb{F}_5^6 \times \mathbb{F}_5^6$ with inverse $V^{-5}$, and none of the apparatus steps at $c=1, \dots, 7$ modify $(n, x_A, x_B)$. Hence $V^{-5}(5, x_A(5), x_B(5)) = (0, (p_A, 0, 1), (p_B, 0, 1))$ recovers $(p_A, p_B)$ uniquely for all $390{,}625$ pairs, and conditions (1)–(6) are necessary and sufficient for membership in $\operatorname{Im}(\Phi_{(c_0, c_1, b_{\mathrm{init}}, B)})$. $\blacksquare$

---

## Section 4. Joint energy conservation, conditioned two-use prediction, and comparator boundary (`Obligation 6`)

### Theorem 6 (Exact conservation of $E_{\mathrm{full}}(X) - W$, $E_{\mathrm{full}}(X) + b$, and $W + b$ across all 8 phases)

For every state $Z = (n, x_A, x_B, X, W, b, (\sigma_A, \sigma_B), d, c) \in \mathcal{Z}_B$ (with stored tape energy counted once inside $E_{\mathrm{full}}(X) = E_D(u, v) + 2(\|A_0\|^2 + \|A_1\|^2 + \|B_0\|^2 + \|B_1\|^2)$) and every phase $c \in \mathbb{Z}/8\mathbb{Z}$, the step $Z' = \mathcal{G}_B(Z)$ satisfies
$$
E_{\mathrm{full}}(X') - W' = E_{\mathrm{full}}(X) - W, \qquad
E_{\mathrm{full}}(X') + b' = E_{\mathrm{full}}(X) + b, \qquad
W' + b' = W + b.
$$
In particular, on any common-ready trajectory starting from $Z(0) \in \mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$, at every phase boundary $c \in \{0, \dots, 7\}$:
$$
E_{\mathrm{full}}(X) - W = 2\bigl(\|c_0\|^2 + \|c_1\|^2\bigr), \qquad
E_{\mathrm{full}}(X) + b = 2\bigl(\|c_0\|^2 + \|c_1\|^2\bigr) + b_{\mathrm{init}}, \qquad
W + b = b_{\mathrm{init}},
$$
and on the Blank-Ready subfamily $\mathcal{R}_{\mathrm{blank}}(b_{\mathrm{init}}, B)$ ($c_0 = c_1 = 0$),
$$
E_{\mathrm{full}}(X) = W = b_{\mathrm{init}} - b.
$$

#### Proof of Theorem 6

- **Phases $c \in \{0, 7\}$ and $L_{\mathrm{buf}}$ at $c=1$:** $(X, W, b)$ are held fixed, so all three quantities are trivially unchanged.
- **Phases $c \in \{2, 3, 5, 6\}$ ($F$ on $X$, $(W, b)$ held fixed):** By `#1485` (`notes/C-CLASSICAL-SIGNED-PORT-CONTRACT-N/CONTRACT.md` Theorem 2), the wave energy satisfies $E_D(v, w_{\mathrm{next}}) - E_D(u, v) = 2\|A_0\|^2 - 2\|b_{\mathrm{out}}\|^2$, while the four-slot tape energy changes by $2(\|A_1\|^2 + \|B_1\|^2 + \|b_{\mathrm{out}}\|^2 + \|B_0\|^2) - 2(\|A_0\|^2 + \|A_1\|^2 + \|B_0\|^2 + \|B_1\|^2) = 2\|b_{\mathrm{out}}\|^2 - 2\|A_0\|^2$. Summing gives $E_{\mathrm{full}}(F(X)) = E_{\mathrm{full}}(X)$, while $W' = W$ and $b' = b$.
- **Phases $c = 1$ ($H_{B,A}$) and $c = 4$ ($H_{B,B}$):** On the refused branch, $(X, W, b)$ are unchanged. On the accepted branch, $u$ and the four tape slots $(A_0, A_1, B_0, B_1)$ are unchanged while $v' = v + \sigma_i a_i$, $W' = W + \Delta_i$, and $b' = b - \Delta_i$, where $\Delta_i = E_D(u, v + \sigma_i a_i) - E_D(u, v) = E_{\mathrm{full}}(X') - E_{\mathrm{full}}(X)$. Thus $E_{\mathrm{full}}(X') - W' = E_{\mathrm{full}}(X) - W$, $W' + b' = W + b$, and $E_{\mathrm{full}}(X') + b' = E_{\mathrm{full}}(X) + b$. Evaluating at $Z(0) \in \mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ gives $E_{\mathrm{full}}(X(0)) = 2(\|c_0\|^2 + \|c_1\|^2)$, $W(0) = 0$, and $b(0) = b_{\mathrm{init}}$. $\blacksquare$

---

### Theorem 7 (Conditioned two-use calibration-to-prediction theorem on $Z_5 \times Z_5 \subset \Pi_2 \times \Pi_2$ and non-identifiability boundaries)

Let $\mathcal{A}_{\mathrm{lin}}^{(2)}$ be the conditioned two-use Blank-Ready linear/quadratic response model class on `(ACC, ACC)` ($\frac{8224427}{10497600} \le b_{\mathrm{init}} \le B$, $c_0 = c_1 = 0$), parameterized by
$$
\theta = (A_0, A_1, D_2, D_3, G_0, \Omega) \in (\mathbb{Q}^{4 \times 4})^4 \times \mathbb{Q}^{4 \times 4}_{\mathrm{sym}} \times \mathbb{Q}^{4 \times 4} \qquad (\dim_{\mathbb{Q}} \mathcal{A}_{\mathrm{lin}}^{(2)} = 4 \times 16 + 10 + 16 = 90),
$$
with observable map $\mathcal{O}_{\theta}(z_A, z_B) = (b_0, b_1, b_2, b_3, E_A, \Delta_B, W_{\mathrm{final}}, b_{\mathrm{final}})$ given by
$$
\begin{aligned}
b_0(z_A, z_B) &= A_0 z_A, & b_1(z_A, z_B) &= A_1 z_A, \\
b_2(z_A, z_B) &= D_2 z_A + A_0 z_B, & b_3(z_A, z_B) &= D_3 z_A + A_1 z_B, \\
E_A(z_A) &= \frac{1}{2}z_A^T G_0 z_A, & \Delta_B(z_A, z_B) &= \frac{1}{2}z_B^T G_0 z_B + z_B^T \Omega z_A, \\
W_{\mathrm{final}}(z_A, z_B) &= E_A(z_A) + \Delta_B(z_A, z_B), & b_{\mathrm{final}}(z_A, z_B) &= b_{\mathrm{init}} - W_{\mathrm{final}}(z_A, z_B).
\end{aligned}
$$

1. **Exact identifiability on $\Pi_2 \times \Pi_2$ and 7-run calibration basis (or 5-run under rank-one fifth-site factorization):**
   Because $Z_5 \subset \Pi_2 = \mathbb{Q}e_0 \oplus \mathbb{Q}e_1$, $\mathcal{O}_{\theta}|_{Z_5 \times Z_5}$ depends only on the $\Pi_2$-restricted parameter tuple
   $$
   \theta|_{\Pi_2} = \bigl(A_0|_{\Pi_2},\, A_1|_{\Pi_2},\, D_2|_{\Pi_2},\, D_3|_{\Pi_2},\, G_0|_{\Pi_2 \times \Pi_2},\, \Omega|_{\Pi_2 \times \Pi_2}\bigr) \in (\mathbb{Q}^{4 \times 2})^4 \times \mathbb{Q}^{2 \times 2}_{\mathrm{sym}} \times \mathbb{Q}^{2 \times 2} \qquad (\dim_{\mathbb{Q}} = 32 + 3 + 4 = 39).
   $$
   The $39$-dimensional restricted parameter $\theta|_{\Pi_2}$ is uniquely and invertibly calibrated from **at most $7$ runs** in $Z_5 \times Z_5$:
   - **Run 1 ($(z^{(1)}, z^{(0)}) = (\frac{1}{2}e_0, 0)$):**
     $$
     A_0 e_0 = 2 b_0(z^{(1)}, 0), \quad A_1 e_0 = 2 b_1(z^{(1)}, 0), \quad D_2 e_0 = 2 b_2(z^{(1)}, 0), \quad D_3 e_0 = 2 b_3(z^{(1)}, 0), \quad (G_0)_{00} = 8 E_A(z^{(1)}) = \frac{4}{5}.
     $$
   - **Run 2 ($(z^{(4)}, z^{(0)}) = (e_1, 0)$):**
     $$
     A_0 e_1 = b_0(z^{(4)}, 0), \quad A_1 e_1 = b_1(z^{(4)}, 0), \quad D_2 e_1 = b_2(z^{(4)}, 0), \quad D_3 e_1 = b_3(z^{(4)}, 0), \quad (G_0)_{11} = 2 E_A(z^{(4)}) = \frac{4}{5}.
     $$
   - **Run 3 ($(z^{(2)}, z^{(0)}) = (\frac{1}{2}(e_0 + e_1), 0)$):**
     $$
     (G_0)_{01} = (G_0)_{10} = 4 E_A(z^{(2)}) - \frac{1}{2}\bigl((G_0)_{00} + (G_0)_{11}\bigr) = \frac{3}{5} - \frac{4}{5} = -\frac{1}{5}.
     $$
   - **Runs 4–7 ($(z^{(1)}, z^{(1)}), (z^{(1)}, z^{(4)}), (z^{(4)}, z^{(1)}), (z^{(4)}, z^{(4)})$):**
     $$
     \begin{aligned}
     \Omega_{00} &= 4\bigl(\Delta_B(z^{(1)}, z^{(1)}) - E_A(z^{(1)})\bigr) = -\frac{145483}{10497600}, &
     \Omega_{10} &= 2\bigl(\Delta_B(z^{(1)}, z^{(4)}) - E_A(z^{(4)})\bigr) = -\frac{145483}{10497600}, \\
     \Omega_{01} &= 2\bigl(\Delta_B(z^{(4)}, z^{(1)}) - E_A(z^{(1)})\bigr) = -\frac{173653}{10497600}, &
     \Omega_{11} &= \Delta_B(z^{(4)}, z^{(4)}) - E_A(z^{(4)}) = -\frac{173653}{10497600}.
     \end{aligned}
     $$
     *(In the $37$-dimensional subclass where $\Omega = -\mathbf{1}\nu^T$ factors through the port sum $s_B = \mathbf{1}^T z_B$, $\Omega_{00} = \Omega_{10}$ and $\Omega_{01} = \Omega_{11}$, so only **5 calibration runs** — Runs 1, 2, 3, $(z^{(1)}, z^{(4)})$, and $(z^{(4)}, z^{(4)})$ — are needed.)*
   Once calibrated on those $7$ (or $5$) pairs, $\theta|_{\Pi_2}$ uniquely and error-freely predicts $\mathcal{O}_{\theta}(z_A, z_B)$ on all remaining **$18$ out-of-sample source pairs** (or $20$ under rank-one $\Omega$) in $Z_5 \times Z_5$ and all $18 \times 15{,}625 = 281{,}250$ out-of-sample native input pairs $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$.
2. **Explicit non-identifiability countermodels outside $\mathcal{A}_{\mathrm{lin}}^{(2)}|_{\Pi_2}$:**
   - **Out-of-plane kernel $\mathcal{K}_{\perp}^{(2)}$ ($\dim_{\mathbb{Q}} = 90 - 39 = 51$):** Any perturbation $\tilde{\theta} = \theta + \delta\theta$ supported on columns or rows in $\Pi_\perp = \mathbb{Q}e_2 \oplus \mathbb{Q}e_3$ (for example $\tilde{A}_0 = R_0 + e_0 e_2^T$, $\tilde{\Omega} = \Omega + e_2 e_3^T$) satisfies $\mathcal{O}_{\tilde{\theta}}(z_A, z_B) = \mathcal{O}_{\theta}(z_A, z_B)$ for all $25$ pairs in $Z_5 \times Z_5 \subset \Pi_2 \times \Pi_2$, while $\tilde{A}_0 e_2 \ne R_0 e_2$ and $e_2^T \tilde{\Omega} e_3 \ne e_2^T \Omega e_3$ on $\Pi_\perp$.
   - **Affine shift family $\mathcal{A}_{\mathrm{aff}}^{(2)}$:** Adding constant offsets $(c_{b_0}, c_{b_1}, c_{b_2}, c_{b_3}, c_{E_A}, c_{\Delta_B})$ requires the zero run $(z^{(0)}, z^{(0)}) = (0, 0)$ to pin all six offsets to $0$.
   - **Nonlinear polynomial/Lagrange countermodel $\mathcal{A}_{\mathrm{nl}}^{(2)}$:** The cubic polynomial
     $$
     q_3(z_0, z_1) = z_0 z_1(2 z_0 - 1)
     $$
     satisfies $q_3(z^{(0)}) = q_3(z^{(1)}) = q_3(z^{(2)}) = q_3(z^{(4)}) = 0$ and $q_3(z^{(3)}) = 1 \cdot \frac{1}{2} \cdot 1 = \frac{1}{2} \ne 0$. Consequently, for any non-zero rational scalar $\lambda \in \mathbb{Q} \setminus \{0\}$ and vector $u \in \mathbb{Q}^4 \setminus \{0\}$, the nonlinear model replacing $b_2(z_A, z_B)$ by $b_2(z_A, z_B) + q_3(z_A) u$ and $\Delta_B(z_A, z_B)$ by $\Delta_B(z_A, z_B) + \lambda q_3(z_B)$ agrees identically with the true apparatus on all $16$ pairs in $\{z^{(0)}, z^{(1)}, z^{(2)}, z^{(4)}\}^2$ (including all $7$ calibration runs), yet differs by $u \ne 0$ whenever $h_A = 3$ and by $\frac{\lambda}{2} \ne 0$ whenever $h_B = 3$. Similarly, the cubic $p_{\mathrm{van}}(z_0, z_1) = z_0(2 z_0 - 1)(2 z_1 - 1)$ vanishes on all $5$ points of $Z_5$ while taking non-zero values on $\Pi_2 \setminus Z_5$ (e.g. $p_{\mathrm{van}}(1, 1) = 1$).

#### Proof of Theorem 7

- **Part 1:** Because $z^{(1)} = \frac{1}{2}e_0$ and $z^{(4)} = e_1$ form a basis of $\Pi_2$ and $z^{(2)} = \frac{1}{2}(e_0 + e_1)$, the linear equations in Runs 1–2 invertibly determine the two columns in $\Pi_2$ of $A_0, A_1, D_2, D_3$ ($4 \times 8 = 32$ parameters) and the diagonal entries $(G_0)_{00}, (G_0)_{11}$; Run 3 determines $(G_0)_{01} = (G_0)_{10}$ ($3$ metric parameters); and Runs 4–7 evaluate $z_B^T \Omega z_A = \Delta_B(z_A, z_B) - E_A(z_B)$ on the four basis pairs $(\frac{1}{2}e_0, \frac{1}{2}e_0), (\frac{1}{2}e_0, e_1), (e_1, \frac{1}{2}e_0), (e_1, e_1)$ of $\Pi_2 \times \Pi_2$, invertibly determining $\Omega|_{\Pi_2 \times \Pi_2}$ ($4$ bilinear parameters, $32 + 3 + 4 = 39$). Since every $(z_A, z_B) \in Z_5 \times Z_5$ lies in $\Pi_2 \times \Pi_2$, the calibrated restriction $\theta|_{\Pi_2}$ determines $\mathcal{O}_\theta(z_A, z_B)$ on all $25$ pairs.
- **Part 2:** Every $z \in Z_5$ has $z_2 = z_3 = 0$, so $\Pi_\perp = \ker(\mathrm{eval}_{Z_5})$ on $\mathbb{Q}^4$ has dimension $2$, giving $\dim_{\mathbb{Q}} \mathcal{K}_\perp^{(2)} = 90 - 39 = 51$. Direct evaluation of $q_3(z_0, z_1) = z_0 z_1(2z_0 - 1)$ and $p_{\mathrm{van}}(z_0, z_1) = z_0(2z_0 - 1)(2z_1 - 1)$ on $Z_5$ verifies the stated nonlinear countermodels. $\blacksquare$

---

### Theorem 8 (Matched classical comparator indistinguishability and five restricted-comparator separation witnesses)

1. **Byte-for-byte indistinguishability against the full matched classical comparator $\mathcal{M}_{\mathrm{matched}}^{(2)}$:**
   Let $\mathcal{M}_{\mathrm{matched}}^{(2)}$ be the classical 25-state lookup comparator that maps $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$ to $(r_A, r_B) = (C_1(h(p_A)), C_1(h(p_B))) \in (\mathbb{F}_5^2)^2$ and executes the static-source apparatus period map $M_{8,B}^{(r_A, r_B)}$ on $\mathcal{A}_B$. Then for every $(c_0, c_1) \in (\mathbb{Q}^4)^2$, every $0 \le b_{\mathrm{init}} \le B$, and all $625^2 = 390{,}625$ native input pairs $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$, the final apparatus state $(X_{\mathrm{final}}, W_{\mathrm{final}}, b_{\mathrm{final}}, (\sigma_A, \sigma_B)_{\mathrm{final}}, d_{\mathrm{final}}) \in \mathcal{A}_B$ of $\mathcal{G}_B^8$ on $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ is byte-for-byte identical to the output of $\mathcal{M}_{\mathrm{matched}}^{(2)}$.
2. **Five explicit separation witnesses against restricted comparator families:**
   Each of the following restricted comparator classes is separated from the funded continuing two-use apparatus $\mathcal{G}_B$ by an explicit rational witness on $\mathcal{R}_{\mathrm{blank}}(b_{\mathrm{init}}, B)$:

   | Restricted comparator class | Missing apparatus mechanism | Explicit witness input $(p_A, p_B)$ and store $(b_{\mathrm{init}}, B)$ | Continuing apparatus $\mathcal{G}_B$ output | Restricted comparator output |
   | :--- | :--- | :--- | :--- | :--- |
   | **1. Single-use comparator** $\mathcal{M}_{\mathrm{single}}$ | Omits second contact $H_{B,B}$ at $c=4$ ($\alpha_B \equiv 0$) | $p_A = (0,0,0,0), p_B = (1,0,0,0)$ ($(h_A, h_B) = (0, 1)$), $b_{\mathrm{init}} = B = \frac{4}{5}$ | $b_2 = R_0 z^{(1)} \ne 0$, $W_{\mathrm{final}} = \frac{1}{10}$, $\sigma_{B,\mathrm{final}} = -1$ | $b_2 = 0$, $W_{\mathrm{final}} = 0$, $\sigma_{B,\mathrm{final}} = +1$ |
   | **2. Cold-restart two-use comparator** $\mathcal{M}_{\mathrm{cold}}$ | Re-zeroes wave $(u,v) \mapsto (0,0)$ before $c=4$ or uses cold increment $E_0(z_B)$ instead of $\Delta_B(z_A, z_B)$ | $p_A = (4,0,0,0), p_B = (4,0,0,0)$ ($(h_A, h_B) = (4, 4)$), $b_{\mathrm{init}} = B = B_* = \frac{8224427}{10497600}$ (or $\frac{4}{5}$) | At $B_*$: **accepts** Contact B ($\sigma_{B,\mathrm{final}} = -1$, $\Delta_B = \frac{4025387}{10497600}$, $b_{\mathrm{final}} = 0$, $b_2 = D_2(z^{(4)}) + R_0 z^{(4)}$) | At $B_*$: **refuses** Contact B ($b_1 - E_0(z^{(4)}) = -\frac{173653}{10497600} < 0$, $\sigma_{B,\mathrm{final}} = +1$, $b_2^{\mathrm{cold}} \ne b_2$) |
   | **3. Two-slot overwriting tape comparator** $\mathcal{M}_{2\text{-slot}}$ | Carries only 2 tape slots, so $(b_2, b_3)$ overwrite $(b_0, b_1)$ at $c=5, 6$ | $p_A = (1,0,0,0), p_B = (0,0,0,0)$ ($(h_A, h_B) = (1, 0)$), $b_{\mathrm{init}} = B = \frac{4}{5}$ | Retains $A_{\mathrm{final}} = (b_0, b_1) = (R_0 z^{(1)}, R_1 z^{(1)}) \ne (0,0)$ alongside $B_{\mathrm{out,final}} = (b_3, b_2)$ | Loses $(b_0, b_1)$ at $c=7$, retaining only $(b_2, b_3) = (D_2(z^{(1)}), D_3(z^{(1)}))$ |
   | **4. Single-direction-bit comparator** $\mathcal{M}_{1\sigma}$ | Collapses $(\sigma_A, \sigma_B)$ into one bit $\sigma \in \{\pm 1\}$ without reset | $p_A = (0,0,0,0), p_B = (1,0,0,0)$ ($(h_A, h_B) = (0, 1)$), $b_{\mathrm{init}} = B = \frac{4}{5}$ | Injects $+S z^{(1)}$ at $c=4$, giving $b_2 = +R_0 z^{(1)}$ | Flips $\sigma: +1 \mapsto -1$ at $c=1$ ($\Delta_A = 0$) and injects $-S z^{(1)}$ at $c=4$, giving $b_2 = -R_0 z^{(1)} \ne +R_0 z^{(1)}$ |
   | **5. Unretained-direction comparator** $\mathcal{M}_{\text{no-}\sigma}$ | Omits $(\sigma_A, \sigma_B)_{\mathrm{final}}$ from the boundary readout | Four pairs $(p^{(h_A)}, p^{(h_B)})$ with $(h_A, h_B) \in \{(0,0), (0,3), (3,0), (3,3)\}$ at $b_{\mathrm{init}} = B = \frac{1}{5}$ | Distinguishes all 4 branches via $(\sigma_A, \sigma_B)_{\mathrm{final}} \in \{(-1,-1), (-1,+1), (+1,-1), (+1,+1)\}$ | Collapses all 4 branches onto $(b_0, b_1, b_2, b_3) = (0,0,0,0)$ and $(W_{\mathrm{final}}, b_{\mathrm{final}}) = (0, \frac{1}{5})$ |

#### Proof of Theorem 8

- **Part 1:** On any state in $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$, phase $c = 0$ advances $n: 0 \mapsto 1$ and sets $(\operatorname{rec}(x_A(1)), \operatorname{rec}(x_B(1))) = (C_1(h(p_A)), C_1(h(p_B))) = (r_A, r_B)$. At phase $c = 1$, $L_{\mathrm{buf}}$ captures $d = r_B$ and $H_{B,A}$ reads $r_A$; at phase $c = 4$, $H_{B,B}$ reads the retained buffer $d = r_B$ rather than $\operatorname{rec}(x_B(3))$. Thus the apparatus trajectory on $\mathcal{A}_B$ across $c = 0, \dots, 7$ equals $T_7 \circ \cdots \circ T_0 = M_{8,B}^{(r_A, r_B)}$, which is identical to $\mathcal{M}_{\mathrm{matched}}^{(2)}$.
- **Part 2:** Witnesses 1, 2, 3, 4, and 5 follow directly from Theorem 5 Part 2 ($R_0 z^{(1)} \ne 0$), Theorem 3 Part 3 and Theorem 4 Part 2 ($\Delta_B(z^{(4)}, z^{(4)}) = \frac{4025387}{10497600} < \frac{4199040}{10497600} = E_0(z^{(4)})$), Theorem 5 Part 1 ($A_{\mathrm{final}} = (b_0, b_1)$), Theorem 2 Part 3 (single-$\sigma$ sign flip on $(0,1)$), and Theorem 5 Part 4 (four-branch collision at $B = \frac{1}{5}$). $\blacksquare$
