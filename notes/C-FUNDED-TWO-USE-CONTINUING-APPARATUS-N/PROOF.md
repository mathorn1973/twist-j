# Proof: `C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N`

**NON-CANONICAL / L1 symbolic mathematical proof / 2026-10-15.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1504](https://github.com/mathorn1973/twist-j/issues/1504), following [#1497#issuecomment-6179898943](https://github.com/mathorn1973/twist-j/issues/1497#issuecomment-6179898943).
Preregistration pin commit: `d4b67e44d14a2f224a0ed77eb8dd08b217711cfb`.

All notation, state carriers, conditional L1 primitives ($L_{\mathrm{buf}}, H_{B,A}, H_{B,B}$), and the 8-phase autonomous schedule $\mathcal{G}_B$ are fixed by `CONTRACT.md` (`dcaa61031604eafff9826e1eefb4809efbe492c0`) and `PREREG.md` (`deff2b951da2c6799fe757d07fbf09229cd68f2a`). All inherited classical and native definitions are taken directly from the pinned sources in `SOURCES.json` (`23ca316806b8159a08277b83c43c2aa078eb6eb1`), specifically `#1485` (`4302c31f07823b2a843e3702ca14620c1917b853`, `1b69563af4018b08d7dc75781b12e9553a8c19c3`), `#1489` (`ea924e214ec3c29009fd4590f294954d3e5ad43f`), `#1492` (`8b91a935c426036e00ecb300019fd94734addeec`), `#1496` (`b7636a334b09fcc68422bcd6cc6e15334d416c59`), A1 (`7b4d55502be44b2f2aed4005c909d7dcb50dbc55`), A2 (`c34baa826cb846260b96373ae6d8f10c3a189a5a`), and A3 (`f341b04f737827d9033e60f452fab77231f7b04a`).

---

## R1 scientific erratum (descendant correction of `a1517dd03fd8330a2e46a712b5e813d27bdb04df`)

This outcome-exposed R1 revision corrects the five analytical defects identified in the review of the initial deliverable commit `a1517dd03fd8330a2e46a712b5e813d27bdb04df` on Draft PR [#1505](https://github.com/mathorn1973/twist-j/pull/1505). The four frozen preregistration pin files (`README.md`, `CONTRACT.md`, `PREREG.md`, `SOURCES.json` from `d4b67e44d14a2f224a0ed77eb8dd08b217711cfb`) remain byte-for-byte unchanged (`0` diff lines).

- **`R1-A` (Exact inverse of $F$, Section 1 `Theorem 1` Part 2):** The misstated expression $u = H v - w_{\mathrm{next}} + 2 P b_{\mathrm{out}}$ in `a1517dd03fd8330a2e46a712b5e813d27bdb04df` (which fails on $u = v = 0, A_0 = e_0 \implies w_{\mathrm{next}} = 2 P e_0, b_{\mathrm{out}} = 0$, returning $-2 P e_0 \ne 0$) is withdrawn and replaced by the exact inherited inverse from A2 (`c34baa826cb846260b96373ae6d8f10c3a189a5a:notes/C-TWO-USE-CONTROL-ARCHIVE-N/PROOF.md` Section 2, eqs. (2)–(3)):
  $$
  u = K\bigl(H v - J_0 w_{\mathrm{next}} + 4 P b_{\mathrm{out}}\bigr), \qquad A_0 = b_{\mathrm{out}} + \frac{1}{2}P^T(w_{\mathrm{next}} - u).
  $$
- **`R1-B` (Withdrawal of false global bijectivity of $V$ and restoration of A2's prepared-image recovery, Section 1 `Theorem 2` Part 2 & Section 3 `Theorem 5` Part 5):** The false assertions in `a1517dd03fd8330a2e46a712b5e813d27bdb04df` that $g_0, \dots, g_4$ preserve $\operatorname{sum}(x) \bmod 5$ and that $V$ is globally invertible on $\mathbb{N}_0 \times \mathbb{F}_5^6 \times \mathbb{F}_5^6$ are withdrawn. As shown in A2 (`PROOF.md` Section 3), the complete-sum actions of $(g_0, g_1, g_2, g_3, g_4)$ are $(z, -z, 2-z, 2-z, 3-z) \pmod 5$, and at $n=0$ ($\theta_0 = 0$) the distinct states $x = (0,0,0,0,0,1)$ ($\operatorname{sum}=1, j=1$) and $\widetilde{x} = (2,1,3,4,2,2)$ ($\operatorname{sum}\equiv 4, j=4$) collide at $g_1(x) = g_4(\widetilde{x}) = (0,0,0,0,0,4)$. Section 3 `Theorem 5` Part 5 restores A2's exact prepared-image recovery (`PROOF.md` Sections 3 and 7): on any prepared head $x_0 = (p, 0, 1)$, ticks 4 and 5 apply $g_1$ twice so $x_5 = g_1 g_1 x_3 = x_3$, the five distinct $C_3(h)$ receivers at $n=5$ decode $h_A, h_B \in \{0,1,2,3,4\}$ directly from $(x_{5,A}, x_{5,B})$, the inverse words $x_{0,i} = g_{j_0(h_i)} g_{j_1(h_i)} g_{j_2(h_i)} x_{5,i}$ reconstruct the full inputs, and the image recognizer enforces both the $(0,1)$ receiver check and the piston-sum selector-consistency check $\sum_{m=0}^3 (\hat{p}_i)_m \bmod 5 = h_i$.
- **`R1-C` (Restoration of inherited matrices $J_p, D_3$ and the $R_1 z^{(h)}$ table, Section 3 `Theorem 5` Part 2):** The altered definition $J_p = P^T T P - I_4$, the omitted term $\frac{1}{2}P^T T J_0 T S z_A$ in $D_3(z_A)$, and the miscomputed $R_1 z^{(h)}$ table in `a1517dd03fd8330a2e46a712b5e813d27bdb04df` are withdrawn. Section 3 restores A2's exact recurrence and matrices (`PROOF.md` Section 5, eqs. (7)–(10)) and `#1489`/`#1492`'s exact $1399680 \, R_1 z^{(h)}$ table:
  $$
  J_p = P^T H P = \frac{1}{54}\bigl(59 I_4 + \mathbf{1}\mathbf{1}^T\bigr), \qquad
  D_3(z_A) = \frac{1}{2}P^T(w_2 - a_4) = \frac{1}{2}P^T\bigl(T^2 - T^4 + T^2 J_0 + T J_0 T\bigr)S z_A,
  $$
  matching $b_3 = -\frac{1}{2}J_p e_0 = (-\frac{5}{9}, -\frac{1}{108}, -\frac{1}{108}, -\frac{1}{108})^T$ at $z_A = z_B = 0, c_0 = 0, c_1 = e_0$.
- **`R1-D` (Restoration of exact source-decoder inverse $R_0^{-1}$, Section 3 `Theorem 5` Part 3):** The erroneous formula $-\frac{36}{59}(5 I_4 + \frac{1}{699}v\mathbf{1}^T)$ (which gives $\frac{5}{6}t \ne t$ on $t = e_0 - e_1$) is withdrawn and replaced by the exact inherited formula from A2 (`PROOF.md` Section 5):
  $$
  M^{-1} = \frac{54}{59}\left(I_4 + \frac{v\mathbf{1}^T}{365}\right), \qquad
  R_0^{-1} = -4 M^{-1} = -\frac{216}{59}\left(I_4 + \frac{v\mathbf{1}^T}{365}\right), \qquad v = (349, 354, 354, 348)^T.
  $$
- **`R1-E` (Unification of the 7-step completion boundary $c = 7, n = 5$ and exact scope of direction-bit / comparator statements, Section 1 `Theorem 2`, Section 3 `Theorem 5`, Section 4 `Theorem 8`):** From $c = 0, n = 0$, **seven** phase updates $\mathcal{G}_B^7(Z(0))$ reach the completion boundary $c = 7, n = 5$ (executing rows $c = 0, 1, 2, 3, 4, 5, 6$), whereas the eighth update $\mathcal{G}_B^8(Z(0))$ executes row $c = 7$ (holding all data coordinates and rotating $c: 7 \mapsto 0$). All endpoint definitions, boundary tables, and the ready-image recognizer now uniformly use $Z(7) = \mathcal{G}_B^7(Z(0))$ at $c = 7, n = 5$. Furthermore, the single-$\sigma$ witness is scoped strictly to direct un-reset substitution of one shared bit $\sigma$ (not a general minimality proof over arbitrary controllers), and the zero-cut comparison at $b_{\mathrm{init}} = B = \frac{1}{5}$ explicitly distinguishes the classical port/work/store projection $\Pi_{\mathrm{class}} = (X, W, b)$ (where all four pairs $(0,0), (0,3), (3,0), (3,3)$ collide) from the delayed-buffer-inclusive projection $\Pi_{\mathrm{class}+d} = (X, W, b, d)$ (where $d = C_1(h_B)$ separates $h_B = 0$ from $h_B = 3$, while $(0,0)$ collides with $(3,0)$, $(0,3)$ collides with $(3,3)$, and $\sigma_{B,\mathrm{final}}$ is still required to distinguish acceptance from refusal).

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
Recall from `#1485` and A2 (`PROOF.md` Section 1, eq. (1)) the basic operator identities following from $P^T P = I_4$:
$$
K = (I + P P^T)^{-1} = I - \frac{1}{2}P P^T, \qquad
J_0 = I - P P^T, \qquad
P^T K = \frac{1}{2}P^T, \qquad
K P = \frac{1}{2}P, \qquad
K J_0 = J_0, \qquad
P^T J_0 = 0, \qquad
J_0 P = 0.
$$

### Theorem 1 (Global bijectivity and involutivity of $L_{\mathrm{buf}}$, $F$, $H_{B,A}$, and $H_{B,B}$)

1. **Delayed-label buffer capture $L_{\mathrm{buf}}$:** On $\mathbb{F}_5^6 \times \mathbb{F}_5^2$ (and extended by identity on all other coordinates of $\mathcal{Z}_B$ or $\mathcal{A}_B$), the map $L_{\mathrm{buf}}(x_B, d) = (x_B, (d + \operatorname{rec}(x_B)) \bmod 5)$ is a global bijection with exact two-sided inverse
   $$
   L_{\mathrm{buf}}^{-1}(x_B, d') = \bigl(x_B,\, (d' - \operatorname{rec}(x_B)) \bmod 5\bigr).
   $$
2. **Reversible two-tape wave update $F$ (inherited from A2 `PROOF.md` Section 2, eqs. (2)–(3)):** On $\mathcal{X}$, the map
   $$
   w_{\mathrm{next}} = K(H v - J_0 u + 4 P A_0), \qquad b_{\mathrm{out}} = A_0 - \frac{1}{2}P^T(w_{\mathrm{next}} - u),
   $$
   $$
   F\bigl((u,v),(A_0,A_1),(B_0,B_1),k\bigr) = \bigl((v, w_{\mathrm{next}}),\, (A_1, B_1),\, (b_{\mathrm{out}}, B_0),\, (k+1) \bmod 2\bigr)
   $$
   is a global bijection on $\mathcal{X}$ with exact two-sided inverse
   $$
   F^{-1}\bigl((v, w_{\mathrm{next}}),\, (\alpha_0, \alpha_1),\, (\beta_0, \beta_1),\, k'\bigr) = \bigl((u, v),\, (A_0, \alpha_0),\, (\beta_1, \alpha_1),\, (k' - 1) \bmod 2\bigr),
   $$
   where, with $b_{\mathrm{out}} = \beta_0$,
   $$
   \boxed{u = K\bigl(H v - J_0 w_{\mathrm{next}} + 4 P b_{\mathrm{out}}\bigr), \qquad A_0 = b_{\mathrm{out}} + \frac{1}{2}P^T(w_{\mathrm{next}} - u).}
   $$
3. **Bounded-store contact involutions $H_{B,A}$ and $H_{B,B}$:** For every $B \in \mathbb{Q}_{\ge 0}$, both $H_{B,A}$ and $H_{B,B}$ map $\mathcal{Z}_B$ into $\mathcal{Z}_B$ (and $\mathcal{A}_B$ into $\mathcal{A}_B$) and satisfy
   $$
   H_{B,A}^2 = \mathrm{id}_{\mathcal{Z}_B}, \qquad H_{B,B}^2 = \mathrm{id}_{\mathcal{Z}_B}
   $$
   globally across all accepted, refused, and occupied wave states $(u, v) \in \mathbb{Q}^D \times \mathbb{Q}^D$. Furthermore, $L_{\mathrm{buf}}$ and $H_{B,A}$ commute at phase $c = 1$: $H_{B,A} \circ L_{\mathrm{buf}} = L_{\mathrm{buf}} \circ H_{B,A}$.

#### Proof of Theorem 1

- **Part 1 ($L_{\mathrm{buf}}$):** Since $L_{\mathrm{buf}}$ fixes $x_B$, $\operatorname{rec}(x_B) \in \mathbb{F}_5^2$ is identical in the forward and backward steps. Addition and subtraction of $\operatorname{rec}(x_B)$ in $(\mathbb{F}_5^2, +)$ are mutual two-sided inverses.
- **Part 2 ($F$, A2 `PROOF.md` Section 2):** Since $K^{-1} = I + P P^T$ and $J_0 = I - P P^T$, the forward wave update is equivalent to
  $$
  (I + P P^T)w_{\mathrm{next}} = H v - (I - P P^T)u + 4 P A_0.
  $$
  The forward port equation $b_{\mathrm{out}} = A_0 - \frac{1}{2}P^T(w_{\mathrm{next}} - u)$ is equivalent to $A_0 = b_{\mathrm{out}} + \frac{1}{2}P^T(w_{\mathrm{next}} - u)$, which left-multiplied by $4 P$ gives $4 P A_0 = 4 P b_{\mathrm{out}} + 2 P P^T(w_{\mathrm{next}} - u)$. Substituting this into the wave equation yields
  $$
  (I + P P^T)w_{\mathrm{next}} = H v - (I - P P^T)u + 4 P b_{\mathrm{out}} + 2 P P^T w_{\mathrm{next}} - 2 P P^T u,
  $$
  and moving the $u$ terms to the left and the $w_{\mathrm{next}}$ terms to the right gives the symmetric relation
  $$
  (I + P P^T)u = H v - (I - P P^T)w_{\mathrm{next}} + 4 P b_{\mathrm{out}} \Longleftrightarrow u = K\bigl(H v - J_0 w_{\mathrm{next}} + 4 P b_{\mathrm{out}}\bigr).
  $$
  Because every step in this rearrangement is reversible on arbitrary $(u, v, A_0) \in \mathbb{Q}^D \times \mathbb{Q}^D \times \mathbb{Q}^4$ and $(v, w_{\mathrm{next}}, b_{\mathrm{out}}) \in \mathbb{Q}^D \times \mathbb{Q}^D \times \mathbb{Q}^4$, $F \circ F^{-1} = F^{-1} \circ F = \mathrm{id}_{\mathcal{X}}$.
  *Explicit check on $u = v = 0, A_0 = e_0$:* The forward step gives $w_{\mathrm{next}} = 4 K P e_0 = 2 P e_0$ and $b_{\mathrm{out}} = e_0 - \frac{1}{2}P^T(2 P e_0) = 0$. The inverse formula then uses $J_0 w_{\mathrm{next}} = 2 J_0 P e_0 = 0$ to return $u = K(0 - 0 + 0) = 0$ and $A_0 = 0 + \frac{1}{2}P^T(2 P e_0 - 0) = e_0$.
- **Part 3 ($H_{B,A}$ and $H_{B,B}$):** Let $i \in \{A, B\}$, where $H_{B,A}$ reads $r_A = \operatorname{rec}(x_A)$ with direction bit $\sigma_A$ and $H_{B,B}$ reads $d \in \mathbb{F}_5^2$ with direction bit $\sigma_B$. Set $a_i = S\eta(r_A)$ for $i=A$ and $a_i = S\eta(d)$ for $i=B$. Because $H_{B,i}$ leaves $x_A, x_B, d$, and $u$ untouched, $a_i$ is invariant under $H_{B,i}$. For any state $Z \in \mathcal{Z}_B$, $b \in [0, B] \cap \mathbb{Q}$ and
  $$
  \Delta_i(u, v, \sigma_i) = E_D(u, v + \sigma_i a_i) - E_D(u, v) = \frac{1}{2}\|a_i\|^2 + \sigma_i a_i^T\left(v - \frac{1}{2}H u\right).
  $$
  - **Case 1 (Accepted branch: $0 \le b - \Delta_i(u, v, \sigma_i) \le B$):** The image state $Z' = H_{B,i}(Z)$ has $u' = u$, $v' = v + \sigma_i a_i$, $W' = W + \Delta_i(u, v, \sigma_i)$, $b' = b - \Delta_i(u, v, \sigma_i) \in [0, B] \cap \mathbb{Q}$, and $\sigma_i' = -\sigma_i$, so $Z' \in \mathcal{Z}_B$. At $Z'$, the energy increment is
    $$
    \Delta_i(u', v', \sigma_i') = E_D(u, v + \sigma_i a_i - \sigma_i a_i) - E_D(u, v + \sigma_i a_i) = E_D(u, v) - E_D(u, v + \sigma_i a_i) = -\Delta_i(u, v, \sigma_i).
    $$
    Hence the post-step store candidate at $Z'$ is
    $$
    b' - \Delta_i(u', v', \sigma_i') = \bigl(b - \Delta_i(u, v, \sigma_i)\bigr) - \bigl(-\Delta_i(u, v, \sigma_i)\bigr) = b \in [0, B] \cap \mathbb{Q}.
    $$
    Thus the two-sided guard $0 \le b' - \Delta_i(u', v', \sigma_i') \le B$ holds automatically at $Z'$, and applying $H_{B,i}$ to $Z'$ takes the accepted branch to return $(v' + \sigma_i' a_i, W' + \Delta_i', b' - \Delta_i', -\sigma_i') = (v, W, b, \sigma_i)$, i.e. $H_{B,i}(H_{B,i}(Z)) = Z$.
  - **Case 2 (Refused branch: $b - \Delta_i(u, v, \sigma_i) < 0$ or $b - \Delta_i(u, v, \sigma_i) > B$):** Here $H_{B,i}(Z) = Z \in \mathcal{Z}_B$, so applying $H_{B,i}$ again sees the identical guard violation at $Z$ and acts as the identity: $H_{B,i}(H_{B,i}(Z)) = Z$.
  - **Commutativity at $c=1$:** $L_{\mathrm{buf}}$ reads $x_B$ and writes only $d$, whereas $H_{B,A}$ reads $(x_A, u, v, b, \sigma_A)$ and writes only $(v, W, b, \sigma_A)$. Because their read/write supports are disjoint, $H_{B,A} \circ L_{\mathrm{buf}} = L_{\mathrm{buf}} \circ H_{B,A}$. $\blacksquare$

---

### Theorem 2 (Global apparatus permutation $G_B$, non-invertibility of global $V$, and direct single-$\sigma$ substitution obstruction)

1. **Two-sided apparatus permutation $G_B$:** For any fixed static label pair $(r_A, r_B) \in (\mathbb{F}_5^2)^2$ and any $B \in \mathbb{Q}_{\ge 0}$, each phase row map $T_c : \mathcal{A}_B \to \mathcal{A}_B$ ($c \in \mathbb{Z}/8\mathbb{Z}$) in `CONTRACT.md` Section 2.3 is a bijection with explicit inverse
   $$
   T_0^{-1} = T_7^{-1} = \mathrm{id}_{\mathcal{A}_B}, \qquad
   T_1^{-1} = (L_{\mathrm{buf}}^{(r_B)})^{-1} \circ H_{B,A}^{(r_A)}, \qquad
   T_2^{-1} = T_3^{-1} = T_5^{-1} = T_6^{-1} = F^{-1} \times \mathrm{id}, \qquad
   T_4^{-1} = H_{B,B}.
   $$
   Consequently, the clocked apparatus transition $G_B : \mathcal{A}_B \times (\mathbb{Z}/8\mathbb{Z}) \to \mathcal{A}_B \times (\mathbb{Z}/8\mathbb{Z})$ defined by $G_B(a, c) = (T_c(a), (c+1)\bmod 8)$ is a global two-sided permutation with exact inverse
   $$
   G_B^{-1}(a', c') = \Bigl(T_{(c'-1)\bmod 8}^{-1}(a'),\, (c'-1)\bmod 8\Bigr).
   $$
   In particular, the 7-step apparatus map from $c=0$ to the completion boundary $c=7$,
   $$
   M_{7,B}^{(r_A, r_B)} := T_6 \circ T_5 \circ T_4 \circ T_3 \circ T_2 \circ T_1 \circ T_0 : \mathcal{A}_B \to \mathcal{A}_B,
   $$
   is a global bijection on $\mathcal{A}_B$ with exact two-sided inverse $(M_{7,B}^{(r_A, r_B)})^{-1} = T_0^{-1} \circ T_1^{-1} \circ T_2^{-1} \circ T_3^{-1} \circ T_4^{-1} \circ T_5^{-1} \circ T_6^{-1}$ (and since $T_7 = \mathrm{id}_{\mathcal{A}_B}$, the 8-step rollover map $M_{8,B}^{(r_A, r_B)} = T_7 \circ M_{7,B}^{(r_A, r_B)}$ equals $M_{7,B}^{(r_A, r_B)}$ on $\mathcal{A}_B$).
2. **Non-invertibility of the selector-defined native tick $V$ on the full checkpoint carrier:**
   On $x = (a, b, c_0, d_0, q, r) \in \mathbb{F}_5^6$, the five canonical involutions $g_0, g_1, g_2, g_3, g_4$ are
   $$
   \begin{aligned}
   g_0(x) &= (b, a, d_0, c_0, q, r), &
   g_1(x) &= (-c_0, -d_0, -a, -b, -q, -r), \\
   g_2(x) &= (2-c_0, 1+r-d_0, 2-a, 1-r-b, 1-q, -r), &
   g_3(x) &= (2-a, 1-b, 3-c_0, 4-d_0, 1-q, 1-r), \\
   g_4(x) &= (2-a, 1-b, 3-c_0, 4-d_0, 2-q, 1-r),
   \end{aligned}
   $$
   whose actions on the complete coordinate sum $z = \sum_{m=0}^5 x_m \bmod 5$ are $(z, -z, 2-z, 2-z, 3-z) \pmod 5$ (A2 `PROOF.md` Section 3). Although each individual $g_k$ is an involution on $\mathbb{F}_5^6$, the state-selected native tick $V(n, x_A, x_B) = (n+1, g_{j(n, x_A)}(x_A), g_{j(n, x_B)}(x_B))$ is **neither surjective nor globally injective** on $\mathbb{N}_0 \times \mathbb{F}_5^6 \times \mathbb{F}_5^6$:
   - *Non-surjectivity:* No state with $n = 0$ lies in the image of $V$.
   - *Explicit non-injectivity collision at $n = 0$ ($\theta_0 = 0$):* For $x = (0, 0, 0, 0, 0, 1)$ ($\operatorname{sum}(x) = 1 \implies j(0, x) = 1$) and $\widetilde{x} = (2, 1, 3, 4, 2, 2)$ ($\operatorname{sum}(\widetilde{x}) = 14 \equiv 4 \implies j(0, \widetilde{x}) = 4$),
     $$
     g_1(x) = (0, 0, 0, 0, 0, 4) = g_4(\widetilde{x}),
     $$
     so $V(0, x, x) = V(0, \widetilde{x}, \widetilde{x}) = (1, (0,0,0,0,0,4), (0,0,0,0,0,4))$.
   Accordingly, no global inverse of $V$ or $\mathcal{G}_B$ on $\mathcal{Z}_B$ is claimed; native inversion holds specifically as a **left inverse and exact ready-image recognizer on the common-ready family $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$** (proved in Section 3 `Theorem 5` Part 5, following A2 `PROOF.md` Section 7).
3. **Obstruction to direct un-reset substitution of a single shared direction bit $\sigma \in \{\pm 1\}$:**
   If the two contact calls at $c = 1$ and $c = 4$ directly share a single direction bit $\sigma \in \{\pm 1\}$ initialized to $\sigma = +1$ at $c = 0$ without an intermediate reset operation (A2 `PROOF.md` Section 9), then on $p_A = (0,0,0,0) \in \mathcal{F}_0$ ($z_A = 0, a_A = 0$) and $p_B = (1,0,0,0) \in \mathcal{F}_1$ ($z_B = (\frac{1}{2},0,0,0)^T, a_B = S z^{(1)}$) with blank wave/tapes and $b_{\mathrm{init}} = B \ge \frac{1}{10}$ (e.g. $B = \frac{2}{5}$ or $\frac{4}{5}$):
   - At $c = 1$ (Contact A): $\Delta_A = 0 \in [0, B]$ passes the guard, so the accepted zero-source call leaves $(u, v) = (0, 0)$ and $b = b_{\mathrm{init}}$ unchanged but flips $\sigma: +1 \mapsto -1$.
   - At $c = 2, 3$: $(u, v)$ and $(b_0, b_1)$ remain $(0, 0)$.
   - At $c = 4$ (Contact B): the second contact reads $\sigma = -1$ with cost $\Delta_B = \frac{1}{10}$ and injects $-S z^{(1)}$ instead of $+S z^{(1)}$, producing $b_2 = -R_0 z^{(1)} \ne +R_0 z^{(1)}$.
   *(Scope note: This witness refutes direct substitution of one shared un-reset $\sigma$ bit into the two $H_B$ calls; it does not assert general minimality of two bits over controllers that introduce an additional mid-cycle sign-reset primitive or alternative multi-state control encodings.)*

#### Proof of Theorem 2

- **Part 1:** By Theorem 1, each $T_c$ is a bijection on $\mathcal{A}_B$ with inverse $T_c^{-1}$, so $G_B \circ G_B^{-1} = G_B^{-1} \circ G_B = \mathrm{id}_{\mathcal{A}_B \times (\mathbb{Z}/8\mathbb{Z})}$ and $M_{7,B}^{(r_A, r_B)}$ has two-sided inverse $T_0^{-1} \circ \cdots \circ T_6^{-1}$.
- **Part 2:** Direct coordinate evaluation of $g_0, \dots, g_4$ gives their sum actions $(z, -z, 2-z, 2-z, 3-z) \pmod 5$ and verifies $g_1(0,0,0,0,0,1) = (0,0,0,0,0,-1) = (0,0,0,0,0,4)$ and $g_4(2,1,3,4,2,2) = (2-2, 1-1, 3-3, 4-4, 2-2, 1-2) = (0,0,0,0,0,4)$.
- **Part 3:** Direct substitution of $a_A = 0, \sigma = +1$ at $c=1$ gives $\Delta_A = 0$ (accepted, $\sigma \mapsto -1$), and at $c=4$ with $(u, v) = (0, 0)$ and $\sigma = -1$ gives $v \mapsto -S z^{(1)}$ and $b_2 = -\frac{1}{2}P^T T(-S z^{(1)}) = -R_0 z^{(1)} \ne +R_0 z^{(1)}$. $\blacksquare$

---

## Section 2. Exact second-contact work in the occupied wave and input-independent two-use funding (`Obligations 3–4`)

### Theorem 3 (Closed-form occupied-wave energy increment $\Delta_B(z_A, z_B)$ and exact 25-pair rational census)

Let $Z(0) \in \mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ be any common-ready state with input pair $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$, residue sums $h_A = h(p_A)$ and $h_B = h(p_B)$, first-tick receivers $C_{1,A} = \operatorname{rec}(x_{1,A}) = C_1(h_A)$ and $C_{1,B} = \operatorname{rec}(x_{1,B}) = C_1(h_B)$, source vectors $z_A = \eta(C_{1,A}) = z^{(h_A)} \in Z_5$ and $z_B = \eta(C_{1,B}) = z^{(h_B)} \in Z_5$, and zero-mean five-site fields $f = S z_A$ and $g = S z_B$.

1. **Pre-contact-B wave state and archive independence at $c = 4$:**
   - At row $c = 1$, $\Delta_A = E_D(0, f) - E_D(0, 0) = \frac{1}{2}\|f\|^2 = \frac{1}{2}z_A^T G_{\mathrm{source}} z_A = E_0(z_A) =: E_A(z_A)$, which is independent of $(c_0, c_1)$.
   - If Contact A is accepted ($\alpha_A = 1$, i.e. $0 \le b_{\mathrm{init}} - E_A(z_A) \le B$), the wave at boundary $c = 2$ is $(u, v) = (0, f)$ with tapes $A = (0, 0), B_{\mathrm{out}} = (c_0, c_1)$.
   - Row $c = 2$ ($F$ cut 0, reading $A_0 = 0$) produces $w_1 = K(H f - J_0(0) + 0) = T f$ and shifts the tapes to $A = (0, c_1), B_{\mathrm{out}} = (b_0, c_0)$ at boundary $c = 3$.
   - Row $c = 3$ ($F$ cut 1, reading $A_0 = 0$) produces
     $$
     w_2 = K(H w_1 - J_0 f + 0) = T w_1 - J_0 f = (T^2 - J_0)f
     $$
     (since $K J_0 = J_0$) and shifts the tapes to $A = (c_1, c_0), B_{\mathrm{out}} = (b_1, b_0)$ at boundary $c = 4$. Because both rows $c = 2$ and $c = 3$ read $A_0 = 0$, the wave $(w_1, w_2) = (T f, (T^2 - J_0)f)$ arriving at Contact B (row $c = 4$) is **strictly independent** of the old archive $(c_0, c_1)$.
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

1. **Wave state before Contact B:** Part 1 follows directly by substituting $u_1 = 0, v_1 = f, A_0 = 0$ into $F$ at rows $c=2$ and $c=3$ and using $K J_0 = J_0$.
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
2. **Input-independent two-use funding condition:** On $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$, an input-independent rational store initialization $(b_{\mathrm{init}}, B)$ accepts **both** Contact A (row $c=1$) and Contact B (row $c=4$) (`(ACC, ACC)`, $(\sigma_A, \sigma_B)_{\mathrm{final}} = (-1, -1)$) across all $25$ source pairs in $Z_5 \times Z_5$ and all $625^2 = 390{,}625$ native input pairs $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$ if and only if
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
       *Explicit witness:* On $(h_A, h_B) = (3, 3)$ (e.g. $p_A = p_B = (3,0,0,0)$) at $b_{\mathrm{init}} = B = \frac{2}{5}$, Contact A is accepted with $E_A = \frac{2}{5}$, remaining store $b = 0$, and $\sigma_A = -1$; at Contact B (row $c=4$), $\Delta_B(z^{(3)}, z^{(3)}) = \frac{1711367}{4665600} > 0$ violates the lower guard $b - \Delta_B = -\frac{1711367}{4665600} < 0$, so Contact B is refused (`(ACC, REF)`), leaving $(\sigma_A, \sigma_B)_{\mathrm{final}} = (-1, +1)$, $W_{\mathrm{final}} = \frac{2}{5}$, and $b_{\mathrm{final}} = 0$.
   - **At intermediate capacity $b_{\mathrm{init}} = B = \frac{1}{5}$:** All four acceptance/refusal regimes are simultaneously inhabited across the $25$ pairs:
     - **`(ACC, ACC)` ($6$ pairs / $93{,}750$ native pairs):** $\{(0,0), (0,1), (0,2), (1,0), (1,1), (2,0)\}$, where $E_A \le \frac{1}{5}$ and $E_A + \Delta_B \le \frac{1}{5}$ (including $(1,1)$ with $W_{\mathrm{final}} = \frac{8252597}{41990400} < \frac{8398080}{41990400} = \frac{1}{5}$).
     - **`(ACC, REF)` ($9$ pairs / $140{,}625$ native pairs):** $\{(0,3), (0,4), (1,2), (1,3), (1,4), (2,1), (2,2), (2,3), (2,4)\}$, where $E_A \le \frac{1}{5}$ but $E_A + \Delta_B > \frac{1}{5}$.
     - **`(REF, ACC)` ($6$ pairs / $93{,}750$ native pairs):** $\{(3,0), (3,1), (3,2), (4,0), (4,1), (4,2)\}$, where Contact A is refused ($E_A = \frac{2}{5} > \frac{1}{5}$, so $u=v=0, b = \frac{1}{5}, \sigma_A = +1$) and Contact B sees the cold wave $(0,0)$ with $\Delta_B = E_0(z_B) \in \{0, \frac{1}{10}, \frac{3}{20}\} \le \frac{1}{5}$ and is accepted ($\sigma_B = -1$).
     - **`(REF, REF)` ($4$ pairs / $62{,}500$ native pairs):** $\{(3,3), (3,4), (4,3), (4,4)\}$, where Contact A is refused ($E_A = \frac{2}{5} > \frac{1}{5}$) and Contact B is also refused ($\Delta_B = E_0(z_B) = \frac{2}{5} > \frac{1}{5}$), leaving $(\sigma_A, \sigma_B)_{\mathrm{final}} = (+1, +1)$.
4. **Occupied-wave (`WARM`) archive/tape witness outside $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$:**
   While $(c_0, c_1) \in B_{\mathrm{out}}$ at $c=0$ enters the wave only at rows $c=5, 6$ (after Contact B at row $c=4$), if the active input tape $A_0$ is non-zero before Contact B (or if a subsequent un-rezeroed cycle is entered after $c_1 = e_0$ was injected at row $c=5$), the ambient wave modifies $\Delta_B$. Specifically, if $A_{\mathrm{init}} = (0, e_0)$ at $c=0$ with $p_A = (0,0,0,0)$ ($z_A = 0$) and $p_B = (1,0,0,0)$ ($z_B = (\frac{1}{2},0,0,0)^T$), then row $c=2$ shifts $A_1 = e_0$ into $A_0$, and row $c=3$ injects $4 P e_0$ into $w_2 = 4 K P e_0 = 2 P e_0$ with $w_1 = 0$. At row $c=4$, Contact B sees $(u, v) = (0, 2 P e_0)$ and experiences
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

### Theorem 5 (Unified four-cut formulas, archive-independent source decoding, accepted-zero vs. refusal discrimination, and exact native prepared-image left inverse)

Let $Z(0) \in \mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ be any common-ready state with input pair $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$, source pair $z_A = z^{(h(p_A))}, z_B = z^{(h(p_B))} \in Z_5$, fields $f = S z_A, g = S z_B$, and acceptance indicators $\alpha_A = \frac{1 - \sigma_{A,\mathrm{final}}}{2} \in \{0, 1\}$, $\alpha_B = \frac{1 - \sigma_{B,\mathrm{final}}}{2} \in \{0, 1\}$.

1. **Boundary-by-boundary state table from $c = 0$ to the completion boundary $c = 7, n = 5$ (7 updates $\mathcal{G}_B^7$):**
   For each $m \in \{0, 1, \dots, 7\}$, let $Z(m) = \mathcal{G}_B^m(Z(0))$ be the state at clock boundary $c = m$ (after executing rows $0, 1, \dots, m-1$). Following A2 `PROOF.md` Sections 4–5 (eqs. (7)–(9)), define the lingering first-contact wave slices
   $$
   w_1 = T f, \qquad w_2 = T w_1 - J_0 f, \qquad a_3 = T w_2 - J_0 w_1, \qquad a_4 = T a_3 - J_0 w_2,
   $$
   and the branch-actual wave slices
   $$
   \begin{aligned}
   w_1^{(\alpha)} &= \alpha_A w_1, &
   w_2^{(\alpha)} &= \alpha_A w_2, &
   w_2^+ &= \alpha_A w_2 + \alpha_B g, \\
   w_3 &= \alpha_A a_3 + \alpha_B T g + 2 P c_1, &
   w_4 &= \alpha_A a_4 + \alpha_B(T^2 - J_0)g + 2 T P c_1 + 2 P c_0.
   \end{aligned}
   $$
   Then the complete boundary state $Z(c)$ at each clock value $c \in \{0, 1, \dots, 7\}$ is:

   | Boundary clock $c$ | Updates $\mathcal{G}_B^c$ | $n$ | Native pair | Wave $(u, v)$ | Input tape $A$ | Output tape $B_{\mathrm{out}}$ | $k$ | $(W, b)$ | $(\sigma_A, \sigma_B)$ | $d$ | Completed cuts |
   | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
   | `0` | $0$ | $0$ | $(x_{0,A}, x_{0,B})$ | $(0, 0)$ | $(0, 0)$ | $(c_0, c_1)$ | $0$ | $(0, b_{\mathrm{init}})$ | $(+1, +1)$ | $(0, 0)$ | none |
   | `1` | $1$ | $1$ | $(x_{1,A}, x_{1,B})$ | $(0, 0)$ | $(0, 0)$ | $(c_0, c_1)$ | $0$ | $(0, b_{\mathrm{init}})$ | $(+1, +1)$ | $(0, 0)$ | none |
   | `2` | $2$ | $1$ | $(x_{1,A}, x_{1,B})$ | $(0, \alpha_A f)$ | $(0, 0)$ | $(c_0, c_1)$ | $0$ | $(\alpha_A E_A, b_{\mathrm{init}} - \alpha_A E_A)$ | $(1-2\alpha_A, +1)$ | $C_{1,B}$ | none |
   | `3` | $3$ | $2$ | $(x_{2,A}, x_{2,B})$ | $(\alpha_A f, w_1^{(\alpha)})$ | $(0, c_1)$ | $(b_0, c_0)$ | $1$ | $(\alpha_A E_A, b_{\mathrm{init}} - \alpha_A E_A)$ | $(1-2\alpha_A, +1)$ | $C_{1,B}$ | `0` |
   | `4` | $4$ | $3$ | $(x_{3,A}, x_{3,B})$ | $(w_1^{(\alpha)}, w_2^{(\alpha)})$ | $(c_1, c_0)$ | $(b_1, b_0)$ | $0$ | $(\alpha_A E_A, b_{\mathrm{init}} - \alpha_A E_A)$ | $(1-2\alpha_A, +1)$ | $C_{1,B}$ | `0, 1` |
   | `5` | $5$ | $3$ | $(x_{3,A}, x_{3,B})$ | $(w_1^{(\alpha)}, w_2^+)$ | $(c_1, c_0)$ | $(b_1, b_0)$ | $0$ | $(W_{\mathrm{final}}, b_{\mathrm{final}})$ | $(1-2\alpha_A, 1-2\alpha_B)$ | $C_{1,B}$ | `0, 1` |
   | `6` | $6$ | $4$ | $(x_{4,A}, x_{4,B})$ | $(w_2^+, w_3)$ | $(c_0, b_0)$ | $(b_2, b_1)$ | $1$ | $(W_{\mathrm{final}}, b_{\mathrm{final}})$ | $(1-2\alpha_A, 1-2\alpha_B)$ | $C_{1,B}$ | `0, 1, 2` |
   | `7` | $7$ | $5$ | $(x_{5,A}, x_{5,B})$ | $(w_3, w_4)$ | $(b_0, b_1)$ | $(b_3, b_2)$ | $0$ | $(W_{\mathrm{final}}, b_{\mathrm{final}})$ | $(1-2\alpha_A, 1-2\alpha_B)$ | $C_{1,B}$ | `0, 1, 2, 3` |

   *(The 8th update $Z(8) = \mathcal{G}_B^8(Z(0))$ applies row $c = 7$, which holds all data coordinates $(n, x_A, x_B, X, W, b, (\sigma_A, \sigma_B), d)$ unchanged and rotates $c: 7 \mapsto 0$.)*
   At the completion boundary $c = 7, n = 5$ ($Z_{\mathrm{final}} = Z(7) = \mathcal{G}_B^7(Z(0))$), all four chronological signed port cuts $(b_0, b_1, b_2, b_3)$ are simultaneously retained in the four tape slots $(A_0, A_1, B_1, B_0) = (b_0, b_1, b_2, b_3)$, and the first-use pair $(b_0, b_1)$ remains literally readable throughout the second use: as $(B_1, B_0)$ at $c = 4, 5$, as $(A_1, B_1)$ at $c = 6$, and as $(A_0, A_1)$ at $c = 7$.
2. **Unified four-cut branch output equations (A2 `PROOF.md` Section 5, eq. (10)):** Across all four acceptance/refusal branches $(\alpha_A, \alpha_B) \in \{0, 1\}^2$,
   $$
   b_0 = \alpha_A R_0 z_A, \qquad
   b_1 = \alpha_A R_1 z_A, \qquad
   b_2 = \alpha_A D_2(z_A) + \alpha_B R_0 z_B, \qquad
   b_3 = \alpha_A D_3(z_A) + \alpha_B R_1 z_B - \frac{1}{2}J_p c_1,
   $$
   where the cold response operators, cross-use operators, and port stencil matrix are inherited without change from `#1485`, `#1489`, `#1492`, and A2 (`PROOF.md` Section 5):
   $$
   \begin{aligned}
   R_0 z &= -\frac{1}{2}P^T T S z = -\frac{1}{4}M z = -\frac{1}{6480}(1770 I_4 - v\mathbf{1}^T)z, & v &= (349, 354, 354, 348)^T, \\
   R_1 z &= \frac{1}{2}P^T\bigl(S z - (T^2 - J_0)S z\bigr) = \frac{1}{2}\bigl(G_{\mathrm{source}} - P^T T^2 S\bigr)z, \\
   J_p &= P^T H P = \frac{1}{54}\bigl(59 I_4 + \mathbf{1}\mathbf{1}^T\bigr), & P^T T P &= P^T K H P = \frac{1}{2}P^T H P = \frac{1}{2}J_p, \\
   D_2(z_A) &= \frac{1}{2}P^T(w_1 - a_3) = \frac{1}{2}P^T\bigl(T - T^3 + T J_0\bigr)S z_A, \\
   D_3(z_A) &= \frac{1}{2}P^T(w_2 - a_4) = \frac{1}{2}P^T\bigl(T^2 - T^4 + T^2 J_0 + T J_0 T\bigr)S z_A.
   \end{aligned}
   $$
   The five single-source port-cut vectors $R_0 z^{(h)}$ and $R_1 z^{(h)}$ on $Z_5$ (inherited directly from `#1489` `ea924e214ec3c29009fd4590f294954d3e5ad43f:notes/C-NATIVE-CLASSICAL-TWO-CUT-CONTACT-N/PROOF.md` Section 4 and `#1492` `8b91a935c426036e00ecb300019fd94734addeec:probes/P-NATIVE-CLASSICAL-CONTACT-CENSUS-1/RESULT.md`) are:

   | $h$ | $12960 \, R_0 z^{(h)}$ | $1399680 \, R_1 z^{(h)}$ |
   | :---: | :---: | :---: |
   | `0` | $(0, 0, 0, 0)^T$ | $(0, 0, 0, 0)^T$ |
   | `1` | $(-1421, 354, 354, 348)^T$ | $(192202, -47829, -47829, -48879)^T$ |
   | `2` | $(-1072, -1062, 708, 696)^T$ | $(143434, 145312, -95658, -97758)^T$ |
   | `3` | $(-2493, -708, 1062, 1044)^T$ | $(335636, 97483, -143487, -146637)^T$ |
   | `4` | $(698, -2832, 708, 696)^T$ | $(-97536, 386282, -95658, -97758)^T$ |

   *Explicit archive-propagation check (`WARM` witness from A2 `PROOF.md` Section 6):*
   - For $z_A = z_B = 0$, $c_0 = 0$, $c_1 = e_0$, the formula gives $b_0 = b_1 = b_2 = 0$ and
     $$
     b_3 = -\frac{1}{2}J_p e_0 = -\frac{1}{2}P^T H P e_0 = \begin{pmatrix} -5/9 \\ -1/108 \\ -1/108 \\ -1/108 \end{pmatrix}.
     $$
   - For $p_A = (0,0,0,0)$ ($z_A = 0$), $p_B = (1,0,0,0)$ ($z_B = z^{(1)} = \frac{1}{2}e_0$), $c_0 = 0, c_1 = e_0$, and $b_{\mathrm{init}} = B \ge \frac{1}{10}$ (`(ACC, ACC)`), $E_A = 0, \Delta_B = \frac{1}{10}$, $b_0 = b_1 = 0$, $b_2 = R_0(e_0/2) = \frac{1}{12960}(-1421, 354, 354, 348)^T$, and
     $$
     b_3 = R_1\left(\frac{e_0}{2}\right) - \frac{1}{2}J_p e_0 = \frac{1}{1399680}\begin{pmatrix} 192202 - 777600 \\ -47829 - 12960 \\ -47829 - 12960 \\ -48879 - 12960 \end{pmatrix} = \frac{1}{1399680}\begin{pmatrix} -585398 \\ -60789 \\ -60789 \\ -61839 \end{pmatrix},
     $$
     matching A2 equation (13) and $E_{\mathrm{full}}(X(7)) - W(7) = \frac{21}{10} - \frac{1}{10} = 2 = 2\|e_0\|^2$.
3. **Archive-independent recovery of $(z_A, z_B)$ on `(ACC, ACC)` (A2 `PROOF.md` Section 5):**
   Since $M = \frac{1}{1620}(1770 I_4 - v\mathbf{1}^T)$ with $v = (349, 354, 354, 348)^T$ and $\mathbf{1}^T v = 1405$, $1770 - 1405 = 365$, and $\frac{1620}{1770} = \frac{54}{59}$, the Sherman–Morrison formula gives
   $$
   M^{-1} = \frac{54}{59}\left(I_4 + \frac{v\mathbf{1}^T}{365}\right), \qquad
   \boxed{R_0^{-1} = -4 M^{-1} = -\frac{216}{59}\left(I_4 + \frac{v\mathbf{1}^T}{365}\right).}
   $$
   *(Check on $t = e_0 - e_1$: since $\mathbf{1}^T t = 0$, $R_0 t = -\frac{1770}{6480}t = -\frac{59}{216}t$ and $R_0^{-1}(R_0 t) = (-\frac{216}{59})(-\frac{59}{216})t = t$.)*
   Whenever $(\sigma_A, \sigma_B)_{\mathrm{final}} = (-1, -1)$ ($\alpha_A = \alpha_B = 1$), both source vectors $(z_A, z_B) \in \mathbb{Q}^4 \times \mathbb{Q}^4$ are uniquely recovered from $(b_0, b_2) = (A_{0,\mathrm{final}}, B_{1,\mathrm{final}})$ independently of the old archive $(c_0, c_1)$ via
   $$
   z_A = R_0^{-1} b_0 = -4 M^{-1} b_0, \qquad
   z_B = R_0^{-1}\bigl(b_2 - D_2(z_A)\bigr) = -4 M^{-1}\bigl(b_2 - D_2(-4 M^{-1} b_0)\bigr).
   $$
   On $Z_5 \times Z_5$, this uniquely determines $(h_A, h_B) \in (\mathbb{Z}/5\mathbb{Z})^2$ and $(C_{1,A}, C_{1,B})$ (agreeing with $d_{\mathrm{final}} = C_{1,B}$).
4. **Accepted-zero vs. refusal discrimination via $(\sigma_A, \sigma_B)_{\mathrm{final}}$ on explicit readout projections:**
   On $\mathcal{R}_{(c_0, 0, \frac{1}{5}, \frac{1}{5})}$, consider the four source pairs $(h_A, h_B) \in \{(0,0), (0,3), (3,0), (3,3)\}$ (for example $p^{(0)} = (0,0,0,0)$ and $p^{(3)} = (3,0,0,0)$). For every one of these four pairs, $\alpha_A z_A = 0$ and $\alpha_B z_B = 0$, so at $c = 7, n = 5$ they produce the identical classical state $X_{\mathrm{final}} = ((0, 2 P c_0), (0, 0), (0, 0), 0)$ (with $(b_0, b_1, b_2, b_3) = (0, 0, 0, 0)$) and the identical work/store pair $(W_{\mathrm{final}}, b_{\mathrm{final}}) = (0, \frac{1}{5})$:
   - **On the classical wave/tape/work/store projection $\Pi_{\mathrm{class}}(Z(7)) = (X_{\mathrm{final}}, W_{\mathrm{final}}, b_{\mathrm{final}})$ (omitting both $d$ and $(\sigma_A, \sigma_B)$):** all four pairs $(0,0), (0,3), (3,0), (3,3)$ collapse onto the single point $(X_{\mathrm{final}}, 0, \frac{1}{5})$.
   - **On the classical + delayed-buffer projection $\Pi_{\mathrm{class}+d}(Z(7)) = (X_{\mathrm{final}}, W_{\mathrm{final}}, b_{\mathrm{final}}, d_{\mathrm{final}})$ (reading $d_{\mathrm{final}} = C_1(h_B)$ but omitting $(\sigma_A, \sigma_B)$):** since $C_1(0) = (0,4)$ and $C_1(3) = (2,0)$, $d_{\mathrm{final}}$ separates $h_B = 0$ from $h_B = 3$, **but still collapses $(0,0) \in \text{(ACC, ACC)}$ with $(3,0) \in \text{(REF, ACC)}$** (both having $d_{\mathrm{final}} = (0,4)$) **and still collapses $(0,3) \in \text{(ACC, REF)}$ with $(3,3) \in \text{(REF, REF)}$** (both having $d_{\mathrm{final}} = (2,0)$); moreover, $d_{\mathrm{final}} = (2,0)$ records only the captured label $C_{1,B}$ at $c=1$, not whether Contact B at $c=4$ accepted or refused that label.
   - **With the retained direction register $(\sigma_A, \sigma_B)_{\mathrm{final}} \in \{\pm 1\}^2$:** all four branches are uniquely separated:
     $$
     (0,0) \mapsto (-1, -1), \qquad (0,3) \mapsto (-1, +1), \qquad (3,0) \mapsto (+1, -1), \qquad (3,3) \mapsto (+1, +1).
     $$
5. **Exact prepared-image left inverse $\mathcal{D}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ and image recognizer on $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ (following A2 `PROOF.md` Sections 3 & 7):**
   For any prepared input $x_0 = (p, 0, 1)$ with piston sum $h = \sum_{m=0}^3 p_m \bmod 5 \in \{0, 1, 2, 3, 4\}$, the canonical first-three-tick selector words and receivers (A2 `PROOF.md` Section 3) are:

   | $h$ | $(j_0(h), j_1(h), j_2(h))$ | $C_1(h) = \operatorname{rec}(x_1)$ | $C_2(h) = \operatorname{rec}(x_2)$ | $C_3(h) = \operatorname{rec}(x_3)$ |
   | :---: | :---: | :---: | :---: | :---: |
   | `0` | $(1, 1, 3)$ | $(0, 4)$ | $(0, 1)$ | $(1, 0)$ |
   | `1` | $(2, 2, 4)$ | $(1, 4)$ | $(0, 1)$ | $(2, 0)$ |
   | `2` | $(3, 1, 3)$ | $(1, 0)$ | $(4, 0)$ | $(2, 1)$ |
   | `3` | $(4, 1, 3)$ | $(2, 0)$ | $(3, 0)$ | $(3, 1)$ |
   | `4` | $(0, 2, 4)$ | $(0, 1)$ | $(1, 4)$ | $(1, 2)$ |

   Every row has $\operatorname{sum}(x_3) \equiv 1 \pmod 5$. Since $\theta_3 = \operatorname{popcount}(3) \bmod 2 = 0$ and $\theta_4 = \operatorname{popcount}(4) \bmod 2 = 1$, tick 4 uses $j_3 = 1$ ($\operatorname{sum}(x_4) \equiv -1 \equiv 4 \pmod 5$) and tick 5 uses $j_4 = (4 + 2) \bmod 5 = 1$, so for both heads $i \in \{A, B\}$:
   $$
   x_{4,i} = g_1 x_{3,i}, \qquad x_{5,i} = g_1 g_1 x_{3,i} = x_{3,i}.
   $$
   Let $\Phi_{(c_0, c_1, b_{\mathrm{init}}, B)} : \mathbb{F}_5^4 \times \mathbb{F}_5^4 \to \mathcal{Z}_B$ map $(p_A, p_B)$ to the 7-step completion endpoint $Z(7) = \mathcal{G}_B^7(Z(0))$ at $c = 7, n = 5$. Because the five $C_3(h)$ receivers $\{(1,0), (2,0), (2,1), (3,1), (1,2)\}$ are pairwise distinct, $\operatorname{rec}(x_{5,i}) = \operatorname{rec}(x_{3,i}) = C_3(h_i)$ uniquely identifies $h_i \in \{0, 1, 2, 3, 4\}$ for each head $i \in \{A, B\}$ without using the classical record. Reconstructing
   $$
   \hat{x}_{0,i} = g_{j_0(h_i)}\, g_{j_1(h_i)}\, g_{j_2(h_i)}\, x_{5,i}, \qquad
   \hat{x}_{1,i} = g_{j_0(h_i)}\, \hat{x}_{0,i} \qquad (i \in \{A, B\}),
   $$
   where $g_{j_2(h_i)}$ is applied first, defines the left inverse
   $$
   \mathcal{D}\bigl(Z(7)\bigr) := \bigl((\hat{x}_{0,A,0}, \dots, \hat{x}_{0,A,3}),\, (\hat{x}_{0,B,0}, \dots, \hat{x}_{0,B,3})\bigr) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4,
   $$
   which satisfies $\mathcal{D}(\Phi_{(c_0, c_1, b_{\mathrm{init}}, B)}(p_A, p_B)) = (p_A, p_B)$ for all $625^2 = 390{,}625$ native input pairs across all four acceptance/refusal branches.
   Moreover, an arbitrary candidate endpoint $Z = (n, x_A, x_B, X, W, b, (\sigma_A, \sigma_B), d, c) \in \mathcal{Z}_B$ belongs to $\operatorname{Im}(\Phi_{(c_0, c_1, b_{\mathrm{init}}, B)})$ if and only if it passes the following four exact tests:
   1. **Clock and $C_3$ receiver test:** $n = 5, c = 7$, and for each $i \in \{A, B\}$, $\operatorname{rec}(x_i)$ belongs to $\{(1,0), (2,0), (2,1), (3,1), (1,2)\}$, uniquely decoding $h_A, h_B \in \{0,1,2,3,4\}$.
   2. **Inverse-word and selector-consistency test:** Reconstruct $\hat{x}_{0,i} = g_{j_0(h_i)} g_{j_1(h_i)} g_{j_2(h_i)} x_i$ for $i \in \{A, B\}$. Require $\operatorname{rec}(\hat{x}_{0,i}) = (0, 1)$ **AND** piston sum $\sum_{m=0}^3 \hat{x}_{0,i,m} \bmod 5 = h_i$ for both $i \in \{A, B\}$.
   3. **Delayed-buffer test:** Reconstruct $\hat{x}_{1,i} = g_{j_0(h_i)} \hat{x}_{0,i}$ and require $d = \operatorname{rec}(\hat{x}_{1,B}) = C_1(h_B)$.
   4. **Apparatus inverse test:** Apply the two-sided apparatus inverse $(M_{7,B}^{(r_A, r_B)})^{-1} = T_0^{-1} \circ T_1^{-1} \circ T_2^{-1} \circ T_3^{-1} \circ T_4^{-1} \circ T_5^{-1} \circ T_6^{-1}$ with $r_A = \operatorname{rec}(\hat{x}_{1,A})$ and $r_B = \operatorname{rec}(\hat{x}_{1,B})$ to $(X, W, b, (\sigma_A, \sigma_B), d)$ (i.e. apply $F^{-1}$ twice, then $H_{B,B}$ with $d$, then $F^{-1}$ twice, then $H_{B,A}$ with $r_A$ and $L_{\mathrm{buf}}^{-1}$ with $r_B$), and require the recovered initial apparatus tuple to equal
      $$
      X_0 = \bigl((0, 0),\, (0, 0),\, (c_0, c_1),\, 0\bigr), \quad W_0 = 0, \quad b_0^{\mathrm{store}} = b_{\mathrm{init}}, \quad (\sigma_{A,0}, \sigma_{B,0}) = (+1, +1), \quad d_0 = (0, 0).
      $$
      *(Equivalently, across the union over all $(c_0, c_1) \in (\mathbb{Q}^4)^2$, require the recovered wave and $A$-tape slots to be zero, $k_0 = 0, W_0 = 0, b_0^{\mathrm{store}} = b_{\mathrm{init}}, (\sigma_{A,0}, \sigma_{B,0}) = (+1, +1), d_0 = (0, 0)$, and read off the recovered old archive $B_{\mathrm{out},0} = (c_0, c_1)$.)*

#### Proof of Theorem 5

- **Parts 1–2:** By A2 `PROOF.md` Sections 4–5 (eqs. (7)–(10)), applying $F$ at rows $c = 2, 3$ with $\alpha_A f$ gives $w_1^{(\alpha)} = \alpha_A T f$, $b_0 = -\frac{1}{2}P^T w_1^{(\alpha)} = \alpha_A R_0 z_A$, $w_2^{(\alpha)} = \alpha_A(T w_1 - J_0 f)$, and $b_1 = \frac{1}{2}P^T(\alpha_A f - w_2^{(\alpha)}) = \alpha_A R_1 z_A$. At row $c = 4$, $H_{B,B}$ maps $w_2^{(\alpha)} \mapsto w_2^+ = \alpha_A w_2 + \alpha_B g$. At row $c = 5$ ($A_0 = c_1$), $w_3 = T w_2^+ - J_0 w_1^{(\alpha)} + 2 P c_1 = \alpha_A a_3 + \alpha_B T g + 2 P c_1$ and
  $$
  b_2 = c_1 + \frac{1}{2}P^T(w_1^{(\alpha)} - w_3) = \alpha_A D_2(z_A) + \alpha_B R_0 z_B + (I_4 - P^T P)c_1 = \alpha_A D_2(z_A) + \alpha_B R_0 z_B.
  $$
  At row $c = 6$ ($A_0 = c_0$), $w_4 = T w_3 - J_0 w_2^+ + 2 P c_0 = \alpha_A a_4 + \alpha_B(T^2 - J_0)g + 2 T P c_1 + 2 P c_0$ and
  $$
  b_3 = c_0 + \frac{1}{2}P^T(w_2^+ - w_4) = \alpha_A D_3(z_A) + \alpha_B R_1 z_B - P^T T P c_1 + (I_4 - P^T P)c_0 = \alpha_A D_3(z_A) + \alpha_B R_1 z_B - \frac{1}{2}J_p c_1,
  $$
  since $P^T P = I_4$ and $P^T T P = P^T K H P = \frac{1}{2}P^T H P = \frac{1}{2}J_p$. Expanding $a_3 = (T^3 - T J_0 - J_0 T)f$ and $a_4 = (T^4 - T^2 J_0 - T J_0 T - J_0 T^2 + J_0)f$ and using $P^T J_0 = 0$ gives the stated operator expansions of $D_2(z_A)$ and $D_3(z_A)$.
- **Part 3:** $(1770 I_4 - v\mathbf{1}^T)(I_4 + \frac{v\mathbf{1}^T}{365}) = 1770 I_4 + (\frac{1770}{365} - 1 - \frac{1405}{365})v\mathbf{1}^T = 1770 I_4$, so $M^{-1} = \frac{1620}{1770}(I_4 + \frac{v\mathbf{1}^T}{365}) = \frac{54}{59}(I_4 + \frac{v\mathbf{1}^T}{365})$ and $R_0^{-1} = -4 M^{-1} = -\frac{216}{59}(I_4 + \frac{v\mathbf{1}^T}{365})$.
- **Part 4:** Immediate from $\alpha_A z_A = 0, \alpha_B z_B = 0$ on all four pairs at $b_{\mathrm{init}} = B = \frac{1}{5}$, together with $d_{\mathrm{final}} = C_1(h_B) \in \{(0,4), (2,0)\}$ and $(\sigma_A, \sigma_B)_{\mathrm{final}} = (1 - 2\alpha_A, 1 - 2\alpha_B)$.
- **Part 5:** Necessity of tests (1)–(4) follows from the forward tables and Theorem 2 Part 1. Conversely, if $Z$ passes tests (1)–(4), then $\hat{x}_{0,i} = (\hat{p}_i, 0, 1)$ has piston sum $h_i$, which forces the forward native trajectory from $(0, \hat{x}_{0,A}, \hat{x}_{0,B})$ to select $(j_0(h_i), j_1(h_i), j_2(h_i), 1, 1)$ and reach $(5, x_A, x_B)$ with $\operatorname{rec}(\hat{x}_{1,i}) = r_i$, while test (4) and the two-sided bijectivity of $M_{7,B}^{(r_A, r_B)}$ on $\mathcal{A}_B$ force $(X, W, b, (\sigma_A, \sigma_B), d) = M_{7,B}^{(r_A, r_B)}(X_0, 0, b_{\mathrm{init}}, (+1,+1), (0,0))$, so $Z = \Phi_{(c_0, c_1, b_{\mathrm{init}}, B)}(\hat{p}_A, \hat{p}_B)$. $\blacksquare$

---

## Section 4. Joint energy conservation, conditioned two-use prediction, and comparator boundary (`Obligation 6`)

### Theorem 6 (Exact conservation of $E_{\mathrm{full}}(X) - W$, $E_{\mathrm{full}}(X) + b$, and $W + b$ across all 8 phases)

For every state $Z = (n, x_A, x_B, X, W, b, (\sigma_A, \sigma_B), d, c) \in \mathcal{Z}_B$ (with stored tape energy counted once inside $E_{\mathrm{full}}(X) = E_D(u, v) + 2(\|A_0\|^2 + \|A_1\|^2 + \|B_0\|^2 + \|B_1\|^2)$) and every phase $c \in \mathbb{Z}/8\mathbb{Z}$, the step $Z' = \mathcal{G}_B(Z)$ satisfies
$$
E_{\mathrm{full}}(X') - W' = E_{\mathrm{full}}(X) - W, \qquad
E_{\mathrm{full}}(X') + b' = E_{\mathrm{full}}(X) + b, \qquad
W' + b' = W + b.
$$
In particular, on any common-ready trajectory starting from $Z(0) \in \mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$, at every boundary $c \in \{0, \dots, 7\}$:
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

- **Rows $c \in \{0, 7\}$ and $L_{\mathrm{buf}}$ at row $c=1$:** $(X, W, b)$ are held fixed, so all three quantities are unchanged.
- **Rows $c \in \{2, 3, 5, 6\}$ ($F$ on $X$, $(W, b)$ held fixed):** By `#1485` (`CONTRACT.md` Theorem 2) and A2 (`PROOF.md` Section 2), the wave energy satisfies $E_D(v, w_{\mathrm{next}}) - E_D(u, v) = 2\|A_0\|^2 - 2\|b_{\mathrm{out}}\|^2$, while the four-slot tape energy changes by $2(\|A_1\|^2 + \|B_1\|^2 + \|b_{\mathrm{out}}\|^2 + \|B_0\|^2) - 2(\|A_0\|^2 + \|A_1\|^2 + \|B_0\|^2 + \|B_1\|^2) = 2\|b_{\mathrm{out}}\|^2 - 2\|A_0\|^2$. Summing gives $E_{\mathrm{full}}(F(X)) = E_{\mathrm{full}}(X)$, while $W' = W$ and $b' = b$.
- **Rows $c = 1$ ($H_{B,A}$) and $c = 4$ ($H_{B,B}$):** On the refused branch, $(X, W, b)$ are unchanged. On the accepted branch, $u$ and the four tape slots $(A_0, A_1, B_0, B_1)$ are unchanged while $v' = v + \sigma_i a_i$, $W' = W + \Delta_i$, and $b' = b - \Delta_i$, where $\Delta_i = E_D(u, v + \sigma_i a_i) - E_D(u, v) = E_{\mathrm{full}}(X') - E_{\mathrm{full}}(X)$. Thus $E_{\mathrm{full}}(X') - W' = E_{\mathrm{full}}(X) - W$, $W' + b' = W + b$, and $E_{\mathrm{full}}(X') + b' = E_{\mathrm{full}}(X) + b$. Evaluating at $Z(0) \in \mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ gives $E_{\mathrm{full}}(X(0)) = 2(\|c_0\|^2 + \|c_1\|^2)$, $W(0) = 0$, and $b(0) = b_{\mathrm{init}}$. $\blacksquare$

---

### Theorem 7 (Conditioned two-use calibration-to-prediction theorem on $Z_5 \times Z_5 \subset \Pi_2 \times \Pi_2$ and non-identifiability boundaries)

Let $\mathcal{A}_{\mathrm{lin}}^{(2)}$ be the conditioned two-use Blank-Ready linear/quadratic response model class on `(ACC, ACC)` ($\frac{8224427}{10497600} \le b_{\mathrm{init}} \le B$, $c_0 = c_1 = 0$), parameterized by
$$
\theta = (A_0, A_1, D_2, D_3, G_0, \Omega) \in (\mathbb{Q}^{4 \times 4})^4 \times \mathbb{Q}^{4 \times 4}_{\mathrm{sym}} \times \mathbb{Q}^{4 \times 4} \qquad (\dim_{\mathbb{Q}} \mathcal{A}_{\mathrm{lin}}^{(2)} = 4 \times 16 + 10 + 16 = 90),
$$
with observable map $\mathcal{O}_{\theta}(z_A, z_B) = (b_0, b_1, b_2, b_3, E_A, \Delta_B, W_{\mathrm{final}}, b_{\mathrm{final}})$ at $c = 7, n = 5$ given by
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
   Let $\mathcal{M}_{\mathrm{matched}}^{(2)}$ be the classical 25-state lookup comparator that maps $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$ to $(r_A, r_B) = (C_1(h(p_A)), C_1(h(p_B))) \in (\mathbb{F}_5^2)^2$ and executes the 7-step static-source apparatus map $M_{7,B}^{(r_A, r_B)} = T_6 \circ T_5 \circ T_4 \circ T_3 \circ T_2 \circ T_1 \circ T_0$ on $\mathcal{A}_B$. Then for every $(c_0, c_1) \in (\mathbb{Q}^4)^2$, every $0 \le b_{\mathrm{init}} \le B$, and all $625^2 = 390{,}625$ native input pairs $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$, the completion apparatus state $(X_{\mathrm{final}}, W_{\mathrm{final}}, b_{\mathrm{final}}, (\sigma_A, \sigma_B)_{\mathrm{final}}, d_{\mathrm{final}}) \in \mathcal{A}_B$ of $\mathcal{G}_B^7$ at $c = 7, n = 5$ on $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ is byte-for-byte identical to the output of $\mathcal{M}_{\mathrm{matched}}^{(2)}$.
2. **Five explicit separation witnesses against restricted comparator families:**
   Each of the following restricted comparator classes is separated from the funded continuing two-use apparatus $\mathcal{G}_B^7$ at $c = 7, n = 5$ by an explicit rational witness on $\mathcal{R}_{\mathrm{blank}}(b_{\mathrm{init}}, B)$:

   | Restricted comparator class | Missing apparatus mechanism | Explicit witness input $(p_A, p_B)$ and store $(b_{\mathrm{init}}, B)$ | Continuing apparatus $\mathcal{G}_B^7$ output at $c=7, n=5$ | Restricted comparator output |
   | :--- | :--- | :--- | :--- | :--- |
   | **1. Single-use comparator** $\mathcal{M}_{\mathrm{single}}$ | Omits second contact $H_{B,B}$ at $c=4$ ($\alpha_B \equiv 0$) | $p_A = (0,0,0,0), p_B = (1,0,0,0)$ ($(h_A, h_B) = (0, 1)$), $b_{\mathrm{init}} = B = \frac{4}{5}$ | $b_2 = R_0 z^{(1)} \ne 0$, $W_{\mathrm{final}} = \frac{1}{10}$, $\sigma_{B,\mathrm{final}} = -1$ | $b_2 = 0$, $W_{\mathrm{final}} = 0$, $\sigma_{B,\mathrm{final}} = +1$ |
   | **2. Cold-restart two-use comparator** $\mathcal{M}_{\mathrm{cold}}$ | Re-zeroes wave $(u,v) \mapsto (0,0)$ before $c=4$ or uses cold increment $E_0(z_B)$ instead of $\Delta_B(z_A, z_B)$ | $p_A = (4,0,0,0), p_B = (4,0,0,0)$ ($(h_A, h_B) = (4, 4)$), $b_{\mathrm{init}} = B = B_* = \frac{8224427}{10497600}$ (or $\frac{4}{5}$) | At $B_*$: **accepts** Contact B ($\sigma_{B,\mathrm{final}} = -1$, $\Delta_B = \frac{4025387}{10497600}$, $b_{\mathrm{final}} = 0$, $b_2 = D_2(z^{(4)}) + R_0 z^{(4)}$) | At $B_*$: **refuses** Contact B ($b - E_0(z^{(4)}) = -\frac{173653}{10497600} < 0$, $\sigma_{B,\mathrm{final}} = +1$, $b_2^{\mathrm{cold}} \ne b_2$) |
   | **3. Two-slot overwriting tape comparator** $\mathcal{M}_{2\text{-slot}}$ | Carries only 2 tape slots, so $(b_2, b_3)$ overwrite $(b_0, b_1)$ at rows $c=5, 6$ | $p_A = (1,0,0,0), p_B = (0,0,0,0)$ ($(h_A, h_B) = (1, 0)$), $b_{\mathrm{init}} = B = \frac{4}{5}$ | Retains $A_{\mathrm{final}} = (b_0, b_1) = (R_0 z^{(1)}, R_1 z^{(1)}) \ne (0,0)$ alongside $B_{\mathrm{out,final}} = (b_3, b_2)$ | Loses $(b_0, b_1)$ at $c=7$, retaining only $(b_2, b_3) = (D_2(z^{(1)}), D_3(z^{(1)}))$ |
   | **4. Direct single-$\sigma$ comparator** $\mathcal{M}_{1\sigma}$ | Shares one un-reset direction bit $\sigma \in \{\pm 1\}$ between $c=1$ and $c=4$ | $p_A = (0,0,0,0), p_B = (1,0,0,0)$ ($(h_A, h_B) = (0, 1)$), $b_{\mathrm{init}} = B = \frac{4}{5}$ | Injects $+S z^{(1)}$ at $c=4$, giving $b_2 = +R_0 z^{(1)}$ | Flips $\sigma: +1 \mapsto -1$ at $c=1$ ($\Delta_A = 0$) and injects $-S z^{(1)}$ at $c=4$, giving $b_2 = -R_0 z^{(1)} \ne +R_0 z^{(1)}$ |
   | **5. Unretained-direction readout comparators** $\mathcal{M}_{\text{no-}\sigma}^{\mathrm{class}}$ and $\mathcal{M}_{\text{no-}\sigma}^{\mathrm{class}+d}$ | Omits $(\sigma_A, \sigma_B)_{\mathrm{final}}$ from the boundary readout $\Pi_{\mathrm{class}} = (X, W, b)$ or $\Pi_{\mathrm{class}+d} = (X, W, b, d)$ | Four pairs $(p^{(h_A)}, p^{(h_B)})$ with $(h_A, h_B) \in \{(0,0), (0,3), (3,0), (3,3)\}$ at $b_{\mathrm{init}} = B = \frac{1}{5}$ | Separates all 4 branches via $(\sigma_A, \sigma_B)_{\mathrm{final}} \in \{(-1,-1), (-1,+1), (+1,-1), (+1,+1)\}$ | $\Pi_{\mathrm{class}}$ collapses all 4 pairs onto $((0,0),(0,0),(0,0),0,0,\frac{1}{5})$; $\Pi_{\mathrm{class}+d}$ still collapses $(0,0)$ with $(3,0)$ ($d=(0,4)$) and $(0,3)$ with $(3,3)$ ($d=(2,0)$) |

#### Proof of Theorem 8

- **Part 1:** On any state in $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$, row $c = 0$ advances $n: 0 \mapsto 1$ and sets $(\operatorname{rec}(x_{1,A}), \operatorname{rec}(x_{1,B})) = (C_1(h(p_A)), C_1(h(p_B))) = (r_A, r_B)$. At row $c = 1$, $L_{\mathrm{buf}}$ captures $d = r_B$ and $H_{B,A}$ reads $r_A$; at row $c = 4$, $H_{B,B}$ reads the retained buffer $d = r_B$ rather than $\operatorname{rec}(x_{3,B})$. Thus the apparatus trajectory on $\mathcal{A}_B$ across the 7 rows $c = 0, \dots, 6$ equals $T_6 \circ \cdots \circ T_0 = M_{7,B}^{(r_A, r_B)}$, which is identical to $\mathcal{M}_{\mathrm{matched}}^{(2)}$.
- **Part 2:** Witnesses 1, 2, 3, 4, and 5 follow directly from Theorem 5 Part 2 ($R_0 z^{(1)} \ne 0$), Theorem 3 Part 3 and Theorem 4 Part 2 ($\Delta_B(z^{(4)}, z^{(4)}) = \frac{4025387}{10497600} < \frac{4199040}{10497600} = E_0(z^{(4)})$), Theorem 5 Part 1 ($A_{\mathrm{final}} = (b_0, b_1)$), Theorem 2 Part 3 (single-$\sigma$ sign flip on $(0,1)$), and Theorem 5 Part 4 (collisions on $\Pi_{\mathrm{class}}$ and $\Pi_{\mathrm{class}+d}$ at $B = \frac{1}{5}$). $\blacksquare$
