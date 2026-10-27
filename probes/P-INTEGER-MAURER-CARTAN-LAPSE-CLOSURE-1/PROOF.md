# P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-1 — Analytical Proofs

## 1. Exact All-Order Maurer–Cartan Curvature Identity

### Theorem 1 (Covariant Gradient Law and Maurer–Cartan Curvature Factorization)
Let $S(q, s)$ be the all-order scalar-lapse action on a finite horizon $T \ge 3$ with fixed endpoints $q_0, q_T \in \mathbb{Q}^6$ and interior Hessian operator $H(s)$ defined by $(\nabla_q S(q, s))_n = (H(s) q)_n$ for $n = 1, \dots, T-1$ (for $q_0 = q_T = 0$, and by replacing $q$ with $q - q^{\mathrm{stat}}(s; q_0, q_T)$ for general fixed endpoints since the interior operator $L_t(s)$ and $H(s)$ act identically on the homogeneous interior displacement). Let $V_t(s) q = L_t(s) q$ be the raw scalar-lapse generator satisfying the all-order off-shell Ward identity
$$\langle \nabla_q S(q, s), L_t(s) q \rangle + \partial_t S(q, s) = 0, \qquad \partial_t := \sum_{b=1}^T (t_b - t_{b-1}) \frac{\partial}{\partial s_b}. \tag{1}$$
For any skew-symmetric interior operator series $A_t(s) = -A_t(s)^\mathsf{T}$ that is linear in the Dirichlet gauge parameter $t = (0, t_1, \dots, t_{T-1}, 0)$, define the adjusted gauge derivation
$$\tilde\delta_t = \partial_t + \tilde L_t(s) q \cdot \nabla_q, \qquad \tilde L_t(s) := L_t(s) + A_t(s) H(s). \tag{2}$$
Then:
1. **All-Order Off-Shell Ward Invariance:** $\tilde\delta_t S(q, s) = 0$ identically to all orders in $s$.
2. **Covariant Transformation of the Euler–Lagrange Residual:** The interior gradient $g(q, s) := \nabla_q S(q, s) = H(s) q$ transforms covariantly to all orders by
   $$\tilde\delta_t g(q, s) = -\tilde L_t(s)^\mathsf{T} g(q, s). \tag{3}$$
3. **All-Order Maurer–Cartan Curvature Factorization:** For any two Dirichlet gauge parameters $t, r$, the off-shell commutator $[\tilde\delta_t, \tilde\delta_r] q := \tilde\delta_t(\tilde\delta_r q) - \tilde\delta_r(\tilde\delta_t q)$ factors to all orders through $\nabla_q S(q, s)$ as
   $$\boxed{[\tilde\delta_t, \tilde\delta_r] q = \mathcal{F}_{t,r}(s) \nabla_q S(q, s),} \tag{4}$$
   where the skew-symmetric curvature tensor $\mathcal{F}_{t,r}(s) = -\mathcal{F}_{r,t}(s) = -\mathcal{F}_{t,r}(s)^\mathsf{T}$ is
   $$\boxed{\mathcal{F}_{t,r}(s) = \Omega_{t,r}(s) + \partial_t A_r(s) - \partial_r A_t(s) + \bigl(L_r(s) A_t(s) + A_t(s) L_r(s)^\mathsf{T}\bigr) - \bigl(L_t(s) A_r(s) + A_r(s) L_t(s)^\mathsf{T}\bigr) + A_r(s) H(s) A_t(s) - A_t(s) H(s) A_r(s),} \tag{5}$$
   and $[\Omega_{t,r}(s)]_{n,n+1} = -\frac{1}{4}(r_n t_{n+1} - t_n r_{n+1}) E(s_{n+1})$, $[\Omega_{t,r}(s)]_{n,n-1} = -[\Omega_{t,r}(s)]_{n-1,n}^\mathsf{T}$ is the raw curvature.

#### Proof
1. Because $A_t(s)^\mathsf{T} = -A_t(s)$, the quadratic form $\langle g, A_t(s) g \rangle = g^\mathsf{T} A_t(s) g = 0$ vanishes identically for every $g = \nabla_q S(q, s)$, so $\tilde\delta_t S = \partial_t S + \langle \nabla_q S, L_t(s) q \rangle + \langle g, A_t(s) g \rangle = 0$.
2. Differentiating the scalar Ward identity $\frac{1}{2} \partial_t(q^\mathsf{T} H(s) q) + q^\mathsf{T} H(s) L_t(s) q = 0$ twice with respect to $q$ yields the exact matrix Ward identity
   $$\partial_t H(s) = -H(s) L_t(s) - L_t(s)^\mathsf{T} H(s). \tag{6}$$
   Since $A_t(s)^\mathsf{T} = -A_t(s)$ and $H(s)^\mathsf{T} = H(s)$, we also have
   $$-H(s) \tilde L_t(s) - \tilde L_t(s)^\mathsf{T} H(s) = -H(s)(L_t + A_t H) - (L_t^\mathsf{T} - H A_t) H(s) = -H(s) L_t(s) - L_t(s)^\mathsf{T} H(s) = \partial_t H(s). \tag{7}$$
   Applying $\tilde\delta_t$ to $g(q, s) = H(s) q$ therefore gives
   $$\tilde\delta_t(H(s) q) = (\partial_t H(s)) q + H(s) \tilde L_t(s) q = \bigl(-H(s) \tilde L_t(s) - \tilde L_t(s)^\mathsf{T} H(s) + H(s) \tilde L_t(s)\bigr) q = -\tilde L_t(s)^\mathsf{T} H(s) q,$$
   proving (3).
3. For the raw generator $\delta_t = \partial_t + L_t(s) q \cdot \nabla_q$, the all-order calculation of `#1666` (`PROOF.md` Eq. (20), noting $\nabla_q S = -f$) gives
   $$\bigl(\partial_t L_r(s) - \partial_r L_t(s) + [L_r(s), L_t(s)]\bigr) q = \Omega_{t,r}(s) H(s) q, \tag{8}$$
   where $[\Omega_{t,r}(s)]_{n,n+1} = -\frac{1}{4}(r_n t_{n+1} - t_n r_{n+1}) E(s_{n+1})$.
   Now expand the commutator $[\tilde\delta_t, \tilde\delta_r] q = \bigl(\partial_t \tilde L_r - \partial_r \tilde L_t + [\tilde L_r, \tilde L_t]\bigr) q$ for $\tilde L_t = L_t + A_t H$. Using (6),
   $$\begin{aligned}
   \partial_t(A_r H) &= (\partial_t A_r) H + A_r (\partial_t H) = (\partial_t A_r) H - A_r H L_t - A_r L_t^\mathsf{T} H, \\
   -\partial_r(A_t H) &= -(\partial_r A_t) H - A_t (\partial_r H) = -(\partial_r A_t) H + A_t H L_r + A_t L_r^\mathsf{T} H, \\
   [\tilde L_r, \tilde L_t] &= [L_r, L_t] + L_r A_t H - A_t H L_r + A_r H L_t - L_t A_r H + (A_r H A_t - A_t H A_r) H.
   \end{aligned}$$
   Summing these three lines, the terms $-A_r H L_t + A_r H L_t$ and $+A_t H L_r - A_t H L_r$ cancel identically, while $[L_r, L_t] + \partial_t L_r - \partial_r L_t = \Omega_{t,r}(s) H(s)$ by (8). Factoring $H(s) q = \nabla_q S(q, s)$ on the right yields (4)–(5). $\square$

---

## 2. Degree-3 Stencil-Width Obstruction and Exact 2-Bond Closure

### Theorem 2 (Origin of the `#1666` Cubic Witness and Exact Degree-3 Closure)
Expand $\mathcal{F}_{t,r}(s) = \sum_{k \ge 0} \mathcal{F}_{t,r}^{(k)}(s)$ in homogeneous degree $k$ in the bond lapses $s = (s_1, \dots, s_T)$ (where $\mathcal{F}_{t,r}^{(k)}(s)$ controls the degree-$(k+2)$ commutator $[\tilde\delta_t, \tilde\delta_r]^{(k+2)}$).
1. **Degree-2 Closure ($k = 0$):** Since $[\Omega_{t,r}^{(0)}]_{n,n+1} = -\frac{1}{4}(r_n t_{n+1} - t_n r_{n+1}) I_6$ and $\partial_t s_{n+1} = t_{n+1} - t_n$, the degree-1 nearest-neighbor kernel $[A_t^{(1)}(s)]_{n,n+1} = \frac{t_n + t_{n+1}}{8} s_{n+1} I_6$ satisfies
   $$\partial_t [A_r^{(1)}(s)]_{n,n+1} - \partial_r [A_t^{(1)}(s)]_{n,n+1} = \frac{(t_{n+1} - t_n)(r_n + r_{n+1}) - (r_{n+1} - r_n)(t_n + t_{n+1})}{8} I_6 = \frac{1}{4}(r_n t_{n+1} - t_n r_{n+1}) I_6 = -[\Omega_{t,r}^{(0)}]_{n,n+1},$$
   so $\mathcal{F}_{t,r}^{(0)} = 0$.
2. **Degree-3 Stencil Decomposition ($k = 1$) and Step-1 No-Go Theorem:** Before adding $A_t^{(2)}(s)$, the degree-1 curvature $\mathcal{R}_{t,r}^{(1)}(s) := \Omega_{t,r}^{(1)}(s) + \Sigma_{t,r}^{(1)}(s)$ decomposes into two disjoint stencil bands:
   - **Nearest-neighbor band ($|m - n| = 1$):**
     $$[\Omega_{t,r}^{(1)}(s)]_{n,n+1} = \frac{1}{4}(r_n t_{n+1} - t_n r_{n+1}) s_{n+1} C.$$
   - **Next-to-nearest-neighbor convective band ($|m - n| = 2$):** Since $(L_r^{(0)} q)_n = \frac{r_n}{2}(q_{n+1} - q_{n-1})$ has $[L_r^{(0)}]_{n,n\pm 1} = \pm \frac{r_n}{2} I_6$, the convective transport
     $$\Sigma_{t,r}^{(1)}(s) := \bigl(L_r^{(0)} A_t^{(1)}(s) + A_t^{(1)}(s) (L_r^{(0)})^\mathsf{T}\bigr) - \bigl(L_t^{(0)} A_r^{(1)}(s) + A_r^{(1)}(s) (L_t^{(0)})^\mathsf{T}\bigr)$$
     vanishes at $|m - n| \in \{0, 1\}$ and has nonvanishing $(n, n+2)$ block ($1 \le n \le T - 3$):
     $$\boxed{[\Sigma_{t,r}^{(1)}(s)]_{n,n+2} = \frac{1}{16}\Bigl(s_{n+2}\bigl(r_n(t_{n+1} + t_{n+2}) - t_n(r_{n+1} + r_{n+2})\bigr) + s_{n+1}\bigl(t_{n+2}(r_n + r_{n+1}) - r_{n+2}(t_n + t_{n+1})\bigr)\Bigr) I_6.}$$
   On the `#1666` witness ($T = 4$, $q_3 = u = (1, 0, -1, 0, 0, 0)^\mathsf{T}$, $q_{n \ne 3} = 0$, $s = (0, 0, 1, 0)$, $t = (0, 1, 0, 0, 0)$, $r = (0, 0, 1, 0, 0)$), we have $s_2 = 0$ on bond $(1, 2)$ and $s_3 = 1$ on bond $(2, 3)$. Thus $[\Omega_{t,r}^{(1)}(s)]_{1,2} = 0$, while $(\partial_t A_r^{(1)} - \partial_r A_t^{(1)})_{1,2} (H_1(s) q)_2 = -\frac{1}{4}(+C u) = -\frac{1}{4} C u$ cancels `raw3[1] = +\frac{1}{4} C u`. The surviving `#1666` residual at slice $n = 1$ comes entirely from the step-2 convective block $(1, 3)$:
   $$[\Sigma_{t,r}^{(1)}(s)]_{1,3} (H_0 q)_3 = \frac{1}{16}\bigl(1 \cdot (0 - 1 \cdot 1) + 0\bigr)(2 C u) = -\frac{1}{8} C u = \left(-\frac{395}{5184}, 0, \frac{395}{5184}, -\frac{1}{144}, \frac{1}{144}, -\frac{1}{5184}\right)^\mathsf{T}.$$
   Because $\partial_t A_r^{(2)}(s) - \partial_r A_t^{(2)}(s)$ preserves the band support of $A_t^{(2)}(s)$, **no** nearest-neighbor ($|m - n| \le 1$) skew operator $A_t^{(2)}(s)$ can cancel $[\Sigma_{t,r}^{(1)}(s)]_{n,n+2}$.
3. **Exact Horizon-Uniform Degree-3 Closure:** The 2-bond quadratic skew operator $A_t^{(2)}(s)$ with blocks
   $$[A_t^{(2)}(s)]_{n,n+1} = -\frac{t_n + t_{n+1}}{16} s_{n+1}^2 C, \qquad [A_t^{(2)}(s)]_{n,n+2} = -\frac{s_{n+1}^2 t_{n+2} + 4 s_{n+1} s_{n+2} t_{n+1} + s_{n+2}^2 t_n}{32} I_6$$
   satisfies $\partial_t A_r^{(2)}(s) - \partial_r A_t^{(2)}(s) = -\Omega_{t,r}^{(1)}(s) - \Sigma_{t,r}^{(1)}(s)$, giving $\mathcal{F}_{t,r}^{(1)}(s) = 0$ and $[\tilde\delta_t^{\le 3}, \tilde\delta_r^{\le 3}]_{\le 3} = 0$ identically off-shell on every horizon $T \ge 3$ with zero boundary defect.

#### Proof
Direct differentiation gives:
- At $(n, n+1)$:
  $$\partial_t [A_r^{(2)}]_{n,n+1} - \partial_r [A_t^{(2)}]_{n,n+1} = -\frac{(t_{n+1}-t_n)(r_n+r_{n+1}) - (r_{n+1}-r_n)(t_n+t_{n+1})}{8} s_{n+1} C = -\frac{1}{4}(r_n t_{n+1} - t_n r_{n+1}) s_{n+1} C = -[\Omega_{t,r}^{(1)}(s)]_{n,n+1}.$$
- At $(n, n+2)$: writing $s_1 = s_{n+1}, s_2 = s_{n+2}$ and $(t_0, t_1, t_2) = (t_n, t_{n+1}, t_{n+2})$,
  $$\begin{aligned}
  \partial_t [A_r^{(2)}]_{n,n+2} - \partial_r [A_t^{(2)}]_{n,n+2} &= -\frac{1}{32}\Bigl((t_1 - t_0)(2 s_1 r_2 + 4 s_2 r_1) + (t_2 - t_1)(4 s_1 r_1 + 2 s_2 r_0) - (t \leftrightarrow r)\Bigr) I_6 \\
  &= -\frac{1}{16}\Bigl(s_1\bigl((t_1 - t_0) r_2 - (r_1 - r_0) t_2 + 2(t_2 r_1 - r_2 t_1)\bigr) + s_2\bigl(2(t_1 r_0 - r_1 t_0) + (t_2 - t_1) r_0 - (r_2 - r_1) t_0\bigr)\Bigr) I_6 \\
  &= -\frac{1}{16}\Bigl(s_1\bigl(t_2(r_0 + r_1) - r_2(t_0 + t_1)\bigr) + s_2\bigl(r_0(t_1 + t_2) - t_0(r_1 + r_2)\bigr)\Bigr) I_6 = -[\Sigma_{t,r}^{(1)}(s)]_{n,n+2}.
  \end{aligned}$$
Finally, for any two interior vertices $n$ and $n + 2$ ($1 \le n \le T - 3$), the intermediate vertex in $[L_r^{(0)}]_{n,k} [A_t^{(1)}]_{k,n+2} + [A_t^{(1)}]_{n,k} [(L_r^{(0)})^\mathsf{T}]_{k,n+2}$ is $k = n + 1 \in \{2, \dots, T - 2\}$, which is strictly interior, so no boundary truncation occurs at degree 3. $\square$

---

## 3. Degree-4 Covariant Bianchi Cocycle, Nonlinear $A H A$ Self-Interaction, and Exact 3-Bond Closure

### Theorem 3 (Necessity of Nonlinear $A H A$ Self-Interaction and Exact Degree-4 Closure)
At degree $k = 2$ in $s$ (controlling the degree-4 commutator $[\tilde\delta_t, \tilde\delta_r]^{(4)}$), the curvature residual before adding $A_t^{(3)}(s)$ is
$$\mathcal{R}_{t,r}^{(2)}(s) := \Omega_{t,r}^{(2)}(s) + \sum_{(i,j) \in \{(0,2),(1,1)\}} \Bigl(\bigl(L_r^{(i)} A_t^{(j)} + A_t^{(j)} (L_r^{(i)})^\mathsf{T}\bigr) - (t \leftrightarrow r)\Bigr) + \Bigl(A_r^{(1)}(s) H_0 A_t^{(1)}(s) - A_t^{(1)}(s) H_0 A_r^{(1)}(s)\Bigr). \tag{9}$$
Then:
1. **Exact Parameter-Space Bianchi 2-Cocycle:** On every horizon $T \ge 3$, $\mathcal{R}_{t,r}^{(2)}(s)$ is supported on stencil width $1 \le |m - n| \le 3$ and satisfies the parameter-space 2-cocycle identity
   $$\boxed{\partial_u \mathcal{R}_{t,r}^{(2)}(s) + \partial_t \mathcal{R}_{r,u}^{(2)}(s) + \partial_r \mathcal{R}_{u,t}^{(2)}(s) = 0} \tag{10}$$
   identically for all Dirichlet gauge parameters $u, t, r$.
2. **Failure of the Cocycle Without Nonlinear $A H A$ Self-Interaction:** If the quadratic self-interaction $\mathcal{Q}_{t,r}^{(2)}(s) := A_r^{(1)}(s) H_0 A_t^{(1)}(s) - A_t^{(1)}(s) H_0 A_r^{(1)}(s)$ is omitted from (9), the remaining linear-in-$A$ part $\mathcal{R}_{t,r}^{(2),\mathrm{lin}}(s) := \mathcal{R}_{t,r}^{(2)}(s) - \mathcal{Q}_{t,r}^{(2)}(s)$ **violates** the Bianchi 2-cocycle condition (10) at $|m - n| = 3$: since $[\mathcal{Q}_{t,r}^{(2)}(s)]_{n,n+3} = -\frac{1}{64} s_{n+1} s_{n+3}\bigl((r_n + r_{n+1})(t_{n+2} + t_{n+3}) - (t_n + t_{n+1})(r_{n+2} + r_{n+3})\bigr) I_6$, its parameter curl is
   $$\bigl(\partial_u \mathcal{R}_{t,r}^{(2),\mathrm{lin}} + \partial_t \mathcal{R}_{r,u}^{(2),\mathrm{lin}} + \partial_r \mathcal{R}_{u,t}^{(2),\mathrm{lin}}\bigr)_{n,n+3}\Big|_{t=e_n,\,r=e_{n+1},\,u=e_{n+2}} = +\frac{1}{32} s_{n+3} I_6 \ne 0,$$
   so no cubic potential $A_t^{(3)}(s)$ can solve $\partial_t A_r^{(3)} - \partial_r A_t^{(3)} = -\mathcal{R}_{t,r}^{(2),\mathrm{lin}}$ without $\mathcal{Q}_{t,r}^{(2)}(s)$.
3. **Exact 3-Bond Cubic Closure and Dirichlet Boundary Reflection:** With $\mathcal{Q}_{t,r}^{(2)}(s)$ included, the explicit 3-bond cubic skew operator $A_t^{(3)}(s)$ defined in `PREREG.md` §3.3 satisfies
   $$\partial_t A_r^{(3)}(s) - \partial_r A_t^{(3)}(s) = -\mathcal{R}_{t,r}^{(2)}(s), \qquad \mathcal{F}_{t,r}^{(2)}(s) = 0,$$
   closing the off-shell commutator through degree 4: $[\tilde\delta_t^{\le 4}, \tilde\delta_r^{\le 4}]_{\le 4} = 0$ identically on all horizons $T \ge 3$. At the boundary-adjacent blocks $(1, 2)$ and $(T-2, T-1)$, because the boundary slices $0$ and $T$ are held fixed ($[A_t^{(2)}]_{0,2} = [A_t^{(2)}]_{T-2,T} = 0$), the missing 2-step boundary paths $1 \to 0 \to 2$ and $T-2 \to T \to T-1$ shift $[\mathcal{R}_{t,r}^{(2)}]_{1,2}$ by $+\frac{1}{64} s_1(s_1 + s_2)(r_1 t_2 - r_2 t_1) I_6$, which is exact with boundary-reflection potential $-\frac{s_1^2(s_1 + s_2) t_2}{128} I_6$.

#### Proof
By the Jacobi identity $[\tilde\delta_u^{\le 3}, [\tilde\delta_t^{\le 3}, \tilde\delta_r^{\le 3}]] + \text{cyc} = 0$ and Theorem 2 ($[\tilde\delta_t^{\le 3}, \tilde\delta_r^{\le 3}] q = (\mathcal{R}_{t,r}^{(2)}(s) + O(s^3)) H(s) q$), the lowest nonvanishing $s$-degree ($O(s^1)$) of the Jacobi sum comes exclusively from the parameter derivatives $\partial_u, \partial_t, \partial_r$ acting on $\mathcal{R}^{(2)}(s)$ times the invertible operator $H_0$, proving (10). Direct polynomial differentiation of the three stencil bands $|m - n| \in \{1, 2, 3\}$ of $A_t^{(3)}(s)$ in `PREREG.md` §3.3 verifies $\partial_t A_r^{(3)}(s) - \partial_r A_t^{(3)}(s) = -\mathcal{R}_{t,r}^{(2)}(s)$ on every interior pair $1 \le n < m \le T - 1$. $\square$

---

## 4. Forced Affine Scalar-Lapse Completion and Free-Lapse De-Freezing

### Theorem 4 (Forced Scalar-Lapse Action and Vacuum Cold-Start Free-Lapse Shell)
For $a \in \{-1, 0, 1\}$ and $f_* = (0, 0, 0, 0, 0, a/4)^\mathsf{T}$, let $x_* \in \mathbf{1}_5^\perp \oplus \mathbb{Q}$ be the unique static solution of $V x_* = f_*$.
1. **Exact Equilibrium and Energies:** On $\mathbf{1}_5^\perp \oplus \mathbb{Q}$, Gaussian elimination on $V$ yields
   $$x_* = \frac{a}{17367514}\bigl(20493, -20493, 2916, 0, -2916, 4342005\bigr)^\mathsf{T}, \qquad E_* := \frac{1}{2} x_*^\mathsf{T} V x_* = \frac{1}{2} f_*^\mathsf{T} x_* = \frac{4342005}{8683757}\left(\frac{a}{4}\right)^2.$$
   Using $D = I_6 - C^2 = V - \frac{1}{4} V^2$ and $V x_* = f_*$, we have $D x_* = f_* - \frac{1}{4} V f_*$ and
   $$E_{\mathrm{cold}} := \frac{1}{2} x_*^\mathsf{T} D x_* = \frac{1}{2} x_*^\mathsf{T} V x_* - \frac{1}{8}\|V x_*\|^2 = E_* - \frac{1}{8}\|f_*\|^2 = \left(\frac{4342005}{8683757} - \frac{1}{8}\right)\left(\frac{a}{4}\right)^2 = \frac{26052283}{69470056}\left(\frac{a}{4}\right)^2.$$
2. **Exact Bond Square-Completion at $s = 0$:** With $\tilde q_n = q_n - x_*$ and $F_0(\tilde q, \tilde Q) = \frac{1}{2}\|\tilde Q - \tilde q\|^2 - \frac{1}{4}(\tilde q^\mathsf{T} V \tilde q + \tilde Q^\mathsf{T} V \tilde Q)$, expanding $\tilde q = q - x_*$ and $\tilde Q = Q - x_*$ gives
   $$F_0(q - x_*, Q - x_*) + E_* = F_0(q, Q) + \frac{1}{2} f_*^\mathsf{T}(q + Q) = F_0(q, Q) + \frac{a}{8}(\chi + X).$$
   Hence $S^{(a)}(q, 0)$ in `PREREG.md` §3.4 equals the forced autonomous action of `#1650`, and its interior Euler–Lagrange gradient at any $s$ is $\nabla_{q_n} S^{(a)}(q, s) = (H(s)(q - x_*))_n$.
3. **All-Order Affine Ward Identity and Degree-4 Commutator Closure:** For Dirichlet gauge parameters $t_0 = t_T = 0$, $\partial_t \sum_{b=1}^T (1 + s_b) E_* = (t_T - t_0) E_* = 0$. Since $x_*$ is constant in $n$ and $s$, the affine derivation $\tilde\delta_t^{(a)} q = \tilde L_t(s)(q - x_*)$ acts on $\tilde q = q - x_*$ by the homogeneous derivation $\tilde\delta_t \tilde q = \tilde L_t(s) \tilde q$, so $\tilde\delta_t^{(a)} S^{(a)}(q, s) = 0$ to all orders and $[\tilde\delta_t^{(a),\le 4}, \tilde\delta_r^{(a),\le 4}]_{\le 4} = 0$ identically off-shell.
4. **Free-Lapse De-Freezing and Vacuum Cold-Start Trajectory ($q_{-1} = q_0 = 0$):** On any stationary trajectory $\tilde z(\tau) = M_0 \exp(\tau K) \tilde z_0$ with $\tilde z_0 = (q_0 - x_*, \tilde p_0)^\mathsf{T}$, every bond lapse derivative is
   $$\frac{\partial S^{(a)}}{\partial s_b} = -H_{\mathrm{bond}}(\tilde z_0) + E_* = -\frac{1}{2}\|\tilde p_0\|^2 - \frac{1}{2}(q_0 - x_*)^\mathsf{T} D (q_0 - x_*) + E_*.$$
   The canonical vacuum cold-start trajectory of `#1650` defined by $q_{-1} = q_0 = 0$ has $q_1 = 2 C q_0 - q_{-1} + f_* = f_*$, so its initial shifted state at $n = 0$ is $\tilde q_0 = -x_*$ and $\tilde p_0 = \tilde q_1 - C \tilde q_0 = f_* - (I_6 - C) x_* = f_* - \frac{1}{2} V x_* = \frac{1}{2} f_* = (0, 0, 0, 0, 0, a/8)^\mathsf{T}$. Its shifted bond energy is
   $$H_{\mathrm{bond}}\!\left(-x_*, \frac{1}{2} f_*\right) = \frac{1}{2}\left\|\frac{1}{2} f_*\right\|^2 + \frac{1}{2} x_*^\mathsf{T} D x_* = \frac{1}{8}\|f_*\|^2 + \left(E_* - \frac{1}{8}\|f_*\|^2\right) = E_*,$$
   so $\partial S^{(a)} / \partial s_b = 0$ holds identically on every bond for all $a \in \{-1, 0, 1\}$. For $a = \pm 1$, this free-lapse stationary trajectory is non-static, with $q_1 = a(0, 0, 0, 0, 0, 1/4)^\mathsf{T}$ and $q_2 = a(1/1296, -1/1296, 0, 0, 0, 1/2)^\mathsf{T}$, giving metric difference $h_2^{(+)} - h_2^{(-)} = \frac{1}{648}\ell$. $\square$
