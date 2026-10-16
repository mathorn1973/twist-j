# Proof and Universal Rational-Carrier Certificates: `C-FUNDED-TWO-USE-EXECUTABLE-2-N`

**NON-CANONICAL / L1 analytical proof and coefficient-complete identity certificates on reconciled 705-site domain / 2026-10-15.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1515](https://github.com/mathorn1973/twist-j/issues/1515), under parent program [#1506](https://github.com/mathorn1973/twist-j/issues/1506), predecessor [#1507](https://github.com/mathorn1973/twist-j/issues/1507) / [#1512](https://github.com/mathorn1973/twist-j/pull/1512), and G1 geometry reconciliation [#1513](https://github.com/mathorn1973/twist-j/issues/1513) / [#1514](https://github.com/mathorn1973/twist-j/pull/1514).

---

## 1. Paired carrier factorization and $625^2 = 390{,}625$ native-input preservation (`Theorem I2-1`)

### Statement

Let $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ be the common-ready family at any fixed $(c_0, c_1) \in (\mathbb{Q}^4)^2$ and $0 \le b_{\mathrm{init}} \le B$. For every input pair $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$ ($625^2 = 390{,}625$ pairs), prepare $Z(0)$ with $x_{0,A} = (p_A, 0, 1)$, $x_{0,B} = (p_B, 0, 1)$, and residue sums $h_A = \sum_{m=0}^3 p_{A,m} \bmod 5$, $h_B = \sum_{m=0}^3 p_{B,m} \bmod 5$.

1. **Independent head evolution and residue-sum factorization into the apparatus:**
   Under $V(n, x_A, x_B) = (n+1, g_{j(n, x_A)}(x_A), g_{j(n, x_B)}(x_B))$, the two heads evolve without cross-coupling: at every boundary $c \in \{0,\dots,7\}$ (with native counter $n(c) \in \{0,1,1,2,3,3,4,5\}$),
   $$
   x_A(c) = U^{n(c)}(p_A, 0, 1), \qquad x_B(c) = U^{n(c)}(p_B, 0, 1),
   $$
   where $U(n, x) = (n+1, g_{j(n,x)}(x))$ is the single-head native tick. For every $p \in \mathbb{F}_5^4$ with $h = \sum_{m=0}^3 p_m \bmod 5$, the first three selectors $(j_0(h), j_1(h), j_2(h))$ and receivers $(C_1(h), C_2(h), C_3(h))$ depend only on $h$, $\operatorname{sum}(x_3) \equiv 1 \pmod 5$, and ticks $4$ and $5$ apply $g_1$ twice so $x_4 = g_1 x_3$ and $x_5 = g_1 g_1 x_3 = x_3$ with $\operatorname{rec}(x_5) = C_3(h)$.
   At phase $c = 1$ ($n = 1$), $H_{B,A}$ reads only $\operatorname{rec}(x_{1,A}) = C_1(h_A)$ and $L_{\mathrm{buf}}$ adds $\operatorname{rec}(x_{1,B}) = C_1(h_B)$ into $d = (0,0) \mapsto C_1(h_B)$. At phase $c = 4$ ($n = 3$), $H_{B,B}$ reads only the retained buffer $d = C_1(h_B)$. Therefore, at every boundary $c \in \{0,\dots,7\}$, the apparatus substate $A(c) = (X(c), W(c), b(c), (\sigma_A(c), \sigma_B(c)), d(c)) \in \mathcal{A}_B$ factors completely through the residue-sum pair $(h_A, h_B) \in (\mathbb{Z}/5\mathbb{Z})^2$:
   $$
   A(c)\bigl(p_A, p_B\bigr) = M_{c,B}^{(C_1(h(p_A)),\, C_1(h(p_B)))}\bigl(A(0)\bigr), \qquad M_{c,B}^{(r_A, r_B)} := T_{c-1,B}^{(r_A, r_B)} \circ \cdots \circ T_{0,B}^{(r_A, r_B)}.
   $$
   Consequently, the $390{,}625$ input pairs partition into $25$ constant-apparatus fibres $\mathcal{F}_{h_A} \times \mathcal{F}_{h_B}$ of cardinality $125^2 = 15{,}625$ each.
2. **Exact paired recovery and four-part ready-image recognizer across all four branches:**
   Because the five $C_3(h)$ receivers $\{(1,0), (2,0), (2,1), (3,1), (1,2)\}$ are pairwise distinct and each $g_k$ is an involution on $\mathbb{F}_5^6$, the single-head inverse word $\hat{x}_{0,i} = g_{j_0(h_i)} g_{j_1(h_i)} g_{j_2(h_i)} x_{5,i}$ recovers $(p_i, 0, 1)$ for all $625$ single-head inputs $p_i \in \mathbb{F}_5^4$, independently of the acceptance/refusal branch $(\alpha_A, \alpha_B) \in \{0, 1\}^2$. Combining this single-head bijection on the $625$ prepared states with the two-sided supplied-label apparatus substate inverse $(M_{7,B}^{(r_A, r_B)})^{-1}$ on the $25$ fibres proves that `recognize_ready_image` and `recover_prepared_inputs` are exact on all $625^2 = 390{,}625$ input pairs across all four branches.

---

## 2. Universal rational-carrier identity certificates (`Theorem I2-2`)

No finite trajectory set certifies universal statements over $\mathbb{Q}^D$ or $\mathbb{Q}^4$ without an algebraic proof or coefficient-complete polynomial identity check. Every universal rational-carrier claim in this package is certified both analytically below and by exhaustive operator/polynomial coefficient verification in `verify.py`:

1. **Global two-sided invertibility and $1426 \times 1426$ polarized bilinear energy conservation of $F$ on $\mathcal{X}$:**
   - *Linear operator certificate on $\mathbb{Q}^{2|D|+16} = \mathbb{Q}^{1426}$:* With $|D| = |Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}| = 705$, for each $k \in \mathbb{Z}/2\mathbb{Z}$, $F$ and $F^{-1}$ are linear operators on the finite-dimensional rational vector space $\mathcal{V}_{\mathcal{X}} = \mathbb{Q}^D \oplus \mathbb{Q}^D \oplus (\mathbb{Q}^4)^4 \cong \mathbb{Q}^{2|D|+16} = \mathbb{Q}^{1426}$. Since $P^T P = I_4$, $K = I - \frac{1}{2}PP^T = (I + PP^T)^{-1}$, $J_0 = I - PP^T$, and $4 P A_0 = 4 P b_{\mathrm{out}} + 2 PP^T(w_{\mathrm{next}} - u)$, the forward equation $(I + PP^T)w_{\mathrm{next}} = H v - (I - PP^T)u + 4 P A_0$ is algebraically equivalent to $(I + PP^T)u = H v - (I - PP^T)w_{\mathrm{next}} + 4 P b_{\mathrm{out}}$, i.e. $u = K(H v - J_0 w_{\mathrm{next}} + 4 P b_{\mathrm{out}})$. In `verify.py` (`T05`), every matrix entry of $K(I + PP^T) - I_D$, $F \circ F^{-1} - I_{1426}$, and $F^{-1} \circ F - I_{1426}$ is verified to be $0$ across all $1426$ basis vectors.
   - *Complete $1426 \times 1426 = 2{,}033{,}476$ polarized bilinear energy certificate:* Let $Q(X) = 2(E_{\mathrm{full}}(F(X)) - E_{\mathrm{full}}(X))$. For $X_r = (u_r, v_r, A_{0,r}, A_{1,r}, B_{0,r}, B_{1,r})$ and $F(X_r) = (v_r, w_r, A_{1,r}, B_{1,r}, b_{\mathrm{out},r}, B_{0,r})$ ($r \in \{1, 2\}$), the norms $\|v\|_D^2, 4\|A_1\|^2, 4\|B_0\|^2, 4\|B_1\|^2$ cancel identically in $Q(X)$, and the polarized symmetric bilinear form is
     $$
     \mathcal{B}_Q(X_1, X_2) = w_1^T w_2 - \frac{1}{2}v_1^T H w_2 - \frac{1}{2}w_1^T H v_2 + 4 b_{\mathrm{out},1}^T b_{\mathrm{out},2} - u_1^T u_2 + \frac{1}{2}u_1^T H v_2 + \frac{1}{2}v_1^T H u_2 - 4 A_{0,1}^T A_{0,2}.
     $$
     Substituting $b_{\mathrm{out},1} = A_{0,1} - \frac{1}{2}P^T(w_1 - u_1)$ and $w_1 = K(H v_1 - J_0 u_1 + 4 P A_{0,1})$ (with $K^T = K$, $H^T = H$, $J_0^T = J_0$) gives, for any $X_2 \in \mathcal{V}_{\mathcal{X}}$:
     $$
     q_2 := K\Bigl(w_2 - \frac{1}{2}H v_2 - 2 P b_{\mathrm{out},2}\Bigr) = \frac{1}{2}(w_2 - u_2),
     $$
     $$
     \mathcal{B}_Q(X_1, X_2) = u_1^T \underbrace{\Bigl(-J_0 q_2 + 2 P b_{\mathrm{out},2} - u_2 + \frac{1}{2}H v_2\Bigr)}_{\mathrm{col}_u(X_2)} + v_1^T \underbrace{H\Bigl(q_2 - \frac{1}{2}w_2 + \frac{1}{2}u_2\Bigr)}_{\mathrm{col}_v(X_2)} + A_{0,1}^T \underbrace{\bigl(4 P^T q_2 + 4 b_{\mathrm{out},2} - 4 A_{0,2}\bigr)}_{\mathrm{col}_a(X_2)}.
     $$
     In `verify.py` (`T05`), $\mathrm{col}_u(E_m) = 0 \in \mathbb{Q}^D$, $\mathrm{col}_v(E_m) = 0 \in \mathbb{Q}^D$, and $\mathrm{col}_a(E_m) = 0 \in \mathbb{Q}^4$ are verified across all $1426$ standard basis vectors $E_m$ of $\mathcal{V}_{\mathcal{X}}$, proving that every column—and therefore all $1426 \times 1426 = 2{,}033{,}476$ entries—of $\mathcal{B}_Q$ is identically zero in $O(|D|)$ sparse operations.
2. **Global involutivity $H_{B,A}^2 = \mathrm{id}$, $H_{B,B}^2 = \mathrm{id}$, and supplied-label substate invertibility vs. full $\mathcal{G}_B$:**
   For any $r \in \mathbb{F}_5^2$ ($a = S\eta(r) \in \mathbb{Q}^D$), $\sigma \in \{-1, +1\}$, and $(u, v) \in (\mathbb{Q}^D)^2$, the affine-linear polynomial $\Delta(u, v, \sigma) = \frac{1}{2}\|a\|^2 + \sigma a^T(v - \frac{1}{2}H u)$ satisfies
   $$
   \Delta(u, v + \sigma a, -\sigma) = \frac{1}{2}\|a\|^2 - \sigma a^T\left(v + \sigma a - \frac{1}{2}H u\right) = \frac{1}{2}(1 - 2\sigma^2)\|a\|^2 - \sigma a^T\left(v - \frac{1}{2}H u\right) = -\Delta(u, v, \sigma)
   $$
   since $\sigma^2 = 1$. Thus on the accepted branch ($0 \le b - \Delta \le B$), $b' = b - \Delta$ and $\Delta' = -\Delta$ give $b' - \Delta' = b \in [0, B]$, so the second application is also accepted and restores $(v, W, b, \sigma)$; on the refused branch ($b - \Delta \notin [0, B]$), $H_{B,i}$ is the identity so $H_{B,i}^2 = \mathrm{id}$. In `verify.py` (`T06`), all constant and linear coefficients of $\Delta(u, v + \sigma a(r), -\sigma) + \Delta(u, v, \sigma)$ in $(u, v) \in (\mathbb{Q}^D)^2$ ($|D| = 705$) are verified to vanish for all $25$ labels $r \in \mathbb{F}_5^2$ and $\sigma \in \{-1, +1\}$.
   Because $L_{\mathrm{buf}}^{(r_B)}$ is a group translation on $\mathbb{F}_5^2$, $H_{B,A}^{(r_A)}$ and $H_{B,B}$ are involutions on $\mathcal{A}_B$, and $F$ is a bijection on $\mathcal{X}$ with two-sided inverse $F^{-1}$, the **supplied-label apparatus substate transitions** $T_{c,B}^{(r_A, r_B)}$ and $S_B^{(r_A, r_B)}$ on $\mathcal{A}_B \times (\mathbb{Z}/8\mathbb{Z})$ have exact two-sided inverses for all $(r_A, r_B) \in (\mathbb{F}_5^2)^2$ and $c \in \mathbb{Z}/8\mathbb{Z}$. By contrast, the full coupled evolution $\mathcal{G}_B$ on $\mathcal{Z}_B$ is not globally invertible because the native step $V$ is not injective on $\mathbb{N}_0 \times (\mathbb{F}_5^6)^2$ (`T02`).
3. **Universal four-cut linear expansion and bilinear contact-B work for all $(z_A, z_B, c_0, c_1) \in (\mathbb{Q}^4)^4$:**
   On any fixed branch $(\alpha_A, \alpha_B) \in \{0, 1\}^2$, the 7-step wave/tape evolution from $u_0 = v_0 = 0, A_{\mathrm{init}} = (0,0), B_{\mathrm{out,init}} = (c_0, c_1)$ with contact injections $\alpha_A S z_A$ at $c=1$ and $\alpha_B S z_B$ at $c=4$ is a linear map from $(z_A, z_B, c_0, c_1) \in (\mathbb{Q}^4)^4 \cong \mathbb{Q}^{16}$ to $(b_0, b_1, b_2, b_3, w_1^{(\alpha)}, w_2^{(\alpha)}, w_2^+, w_3, w_4)$. Evaluating the exact machine on the $16$ standard basis vectors of $(\mathbb{Q}^4)^4$ for each $(\alpha_A, \alpha_B) \in \{0, 1\}^2$ (`T07` and `T10` in `verify.py`) extracts all rational matrix coefficients on the 705-site domain $D$ and certifies that for **all** $(z_A, z_B, c_0, c_1) \in (\mathbb{Q}^4)^4$:
   $$
   b_0 = \alpha_A R_0 z_A, \qquad
   b_1 = \alpha_A R_1 z_A, \qquad
   b_2 = \alpha_A D_2 z_A + \alpha_B R_0 z_B, \qquad
   b_3 = \alpha_A D_3 z_A + \alpha_B R_1 z_B - \frac{1}{2}J_p c_1,
   $$
   and, when $\alpha_A = 1$, $w_2 - \frac{1}{2}H w_1 = J_0(\frac{1}{2}H K H S z_A - S z_A)$ and $J_0 S z_B = -\frac{s_B}{5}\delta_{y_4}$ yield the universal bilinear work identity
   $$
   (S z_B)^T\left(w_2 - \frac{1}{2}H w_1\right) = z_B^T S^T\left(T^2 - J_0 - \frac{1}{2}H T\right)S z_A = -\frac{s_B(\mu^T z_A)}{10497600}, \qquad \mu = (145483, 173653, 173653, 142153)^T,
   $$
   with zero coefficient on $(c_0, c_1)$. Note that because $S e_j$ is supported on $Y$ ($|Y| = 5$), $H S e_j$ and $K H S e_j$ are supported on $Y + B_{\mathrm{zero}}$ ($142$ sites), and $H K H S e_j$ is supported on $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$ ($705$ sites), every 2-step stencil path from $Y$ to $Y$ lies strictly inside the reconciled 705-site domain $D$.

---

## 3. Proofs of the two `#1506` dispatch clarifications (`Theorem I2-3`)

1. **Clarification (i) ($q_3(z^{(3)}) = \frac{1}{2}$ shift magnitude):**
   On $\Pi_2 = \mathbb{Q}e_0 \oplus \mathbb{Q}e_1$, the cubic polynomial $q_3(z_0, z_1) = z_0 z_1(2 z_0 - 1)$ evaluates on $Z_5$ to:
   - $z^{(0)} = (0, 0) \implies q_3(0, 0) = 0$;
   - $z^{(1)} = (\frac{1}{2}, 0) \implies q_3(\frac{1}{2}, 0) = 0$;
   - $z^{(2)} = (\frac{1}{2}, \frac{1}{2}) \implies q_3(\frac{1}{2}, \frac{1}{2}) = \frac{1}{4}(1 - 1) = 0$;
   - $z^{(4)} = (0, 1) \implies q_3(0, 1) = 0$;
   - $z^{(3)} = (1, \frac{1}{2}) \implies q_3(1, \frac{1}{2}) = 1 \cdot \frac{1}{2} \cdot (2 - 1) = \frac{1}{2}$.
   Therefore, for any $u \in \mathbb{Q}^4 \setminus \{0\}$ and $\lambda \in \mathbb{Q} \setminus \{0\}$, the nonlinear countermodel perturbation $\tilde{b}_2(z_A, z_B) = b_2(z_A, z_B) + q_3(z_A) u$ changes $b_2$ at $h_A = 3$ ($z_A = z^{(3)}$) by $q_3(z^{(3)}) u = \frac{1}{2}u$ (`u/2`), not $u$, while $\tilde{\Delta}_B(z_A, z_B) = \Delta_B(z_A, z_B) + \lambda q_3(z_B)$ changes $\Delta_B$ at $h_B = 3$ by $\frac{\lambda}{2}$.
2. **Clarification (ii) ($\sigma_B$ redundancy for ready-family second-acceptance readout from $(d, b_0, b_2)$ vs. role in $H_{B,B}$ and $\Pi_{\mathrm{class}}$):**
   - *Ready-family readout of $\alpha_B$ from $(d, b_0, b_2)$ without $\sigma_B$:* On any trajectory in $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ ($0 \le b_{\mathrm{init}} \le B$), at completion $c = 7, n = 5$ we have $d = C_1(h_B)$, which determines $z_B = \eta(d) \in Z_5$, and $\alpha_A z_A = R_0^{-1} b_0$, so $r_{\mathrm{res}} := b_2 - D_2(R_0^{-1} b_0) = \alpha_B R_0 z_B$.
     - If $d = C_1(0) = (0, 4)$, then $z_B = z^{(0)} = 0$ and $a_B = S z_B = 0$, so at phase $c = 4$ the energy increment is $\Delta_B = 0$. Since $b(c=4) \in [0, B]$ on $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$, the guard $0 \le b(c=4) - 0 \le B$ is always satisfied, forcing $\alpha_B = 1$.
     - If $d \ne (0, 4)$, then $z_B \in \{z^{(1)}, z^{(2)}, z^{(3)}, z^{(4)}\}$ is non-zero, and because $R_0$ is invertible on $\mathbb{Q}^4$, $R_0 z_B \ne 0$. Hence $r_{\mathrm{res}} = \alpha_B R_0 z_B$ equals $R_0 z_B \ne 0$ when $\alpha_B = 1$ and equals $0$ when $\alpha_B = 0$.
     Thus $\alpha_B \in \{0, 1\}$ is uniquely determined from $(d, b_0, b_2)$ on the entire common-ready family without inspecting $\sigma_B$.
   - *Why $\sigma_A$ is still required on $(d, b_0, b_2)$ and $\Pi_{\mathrm{class}+d}$:* At $B = b_{\mathrm{init}} = \frac{1}{5}$, $(h_A, h_B) = (0, 0) \in (\mathrm{ACC}, \mathrm{ACC})$ and $(3, 0) \in (\mathrm{REF}, \mathrm{ACC})$ produce the identical triple $(d, b_0, b_2) = ((0,4), 0, 0)$ (and the identical $\Pi_{\mathrm{class}+d} = (X, W, b, d)$), because Contact A accepts $z^{(0)} = 0$ on $(0,0)$ ($\alpha_A = 1$) and refuses $z^{(3)}$ on $(3,0)$ ($\alpha_A = 0$), both yielding $\alpha_A z_A = 0$. Only $\sigma_{A,\mathrm{final}} \in \{-1, +1\}$ distinguishes them.
   - *Separate roles of $\sigma_B$:* (a) On the buffer-omitted classical projection $\Pi_{\mathrm{class}} = (X, W, b)$ at $B = b_{\mathrm{init}} = \frac{1}{5}$, $(0, 0) \in (\mathrm{ACC}, \mathrm{ACC})$ and $(0, 3) \in (\mathrm{ACC}, \mathrm{REF})$ collide on $\Pi_{\mathrm{class}}$ and are separated by $\sigma_{B,\mathrm{final}} \in \{-1, +1\}$ (or by $d$); (b) in the reversible transition law on $\mathcal{Z}_B$ and $\mathcal{A}_B$, $\sigma_B$ is required so that $H_{B,B}^2 = \mathrm{id}$ reverses accepted non-zero injections ($v' \mapsto v' - a_B$) and so that an accepted zero-source first contact at $c=1$ (which flips $\sigma_A: +1 \mapsto -1$ with $\Delta_A = 0$) does not flip the sign of Contact B at $c=4$ on $(h_A, h_B) = (0, 1)$. $\blacksquare$
