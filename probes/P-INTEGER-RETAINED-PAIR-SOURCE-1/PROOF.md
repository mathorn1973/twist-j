# Mathematical Proofs: P-INTEGER-RETAINED-PAIR-SOURCE-1

**Status:** `NON-CANONICAL`, `L1` (`candidate-T` analytical proofs, `candidate-C`
two-architecture exact computation audit).
**Issue:** `https://github.com/mathorn1973/twist-j/issues/1698`.

---

## 1. Theorem 1 — Cyclotomic Trace-Form and Index-3/41 Seam Coordinate Bridge

### Statement

Let $K_5 = \mathbb Q(j)$ with $\Phi_5(j) = 1 + j + j^2 + j^3 + j^4 = 0$,
$\mathcal O_5 = \mathbb Z[j]$, and $J = 1 + j^2 \in \mathcal O_5$, and let
$K_8 = \mathbb Q(m)$ with $\Phi_8(m) = m^4 + 1 = 0$, $\mathcal O_8 = \mathbb Z[m]$,
and $M = 1 + m + m^2 \in \mathcal O_8$. Set $A = \mathbb Z[J] \subseteq \mathcal O_5$,
$B = \mathbb Z[M] \subseteq \mathcal O_8$, and $S = A \times B$.

1. The minimal polynomials of $J$ and $M$ over $\mathbb Q$ are
   $$f(x) = x^4 - 3x^3 + 4x^2 - 2x + 1, \qquad g(x) = x^4 - 4x^3 + 8x^2 - 4x + 1,$$
   with resultant $\operatorname{Res}(f, g) = 41$ and common modular root
   $\gcd(f \bmod 41, g \bmod 41) = x - 19 \in \mathbb F_{41}[x]$.
2. In the cyclotomic integral basis $(1, j, j^2, j^3; 1, m, m^2, m^3)$ of
   $\mathcal O_5 \oplus \mathcal O_8 \cong \mathbb Z^8$, the canonical positive-definite
   field-trace form
   $$b\bigl((a, \beta), (a', \beta')\bigr) = \operatorname{Tr}_{K_5/\mathbb Q}(a \overline{a'}) + \operatorname{Tr}_{K_8/\mathbb Q}(\beta \overline{\beta'})$$
   has the exact Gram matrix
   $$G = \operatorname{diag}\bigl(G_5,\, G_8\bigr) = \operatorname{diag}\bigl(5I_4 - \mathbf 1_4 \mathbf 1_4^T,\; 4I_4\bigr),$$
   with $\det G_5 = 125$, $\det G_8 = 256$, and $\det G = 32\,000$.
3. The transition matrices from the power bases $(1, J, J^2, J^3)$ of $A$ and
   $(1, M, M^2, M^3)$ of $B$ to $(1, j, j^2, j^3)$ and $(1, m, m^2, m^3)$ are
   $$T_J =
   \begin{pmatrix}
   1 & 1 & 0 & -2 \\
   0 & 0 & -1 & -2 \\
   0 & 1 & 1 & 0 \\
   0 & 0 & -1 & -3
   \end{pmatrix},
   \qquad
   T_M =
   \begin{pmatrix}
   1 & 1 & 0 & -5 \\
   0 & 1 & 2 & 0 \\
   0 & 1 & 3 & 5 \\
   0 & 0 & 2 & 7
   \end{pmatrix},$$
   with $\det T_J = -1$ and $\det T_M = -3$. In particular $A = \mathcal O_5 = \mathbb Z^4$,
   while $T_M(\mathbb Z^4)$ is the exact index-$3$ sublattice
   $$\Lambda_3 = \bigl\{b = (b_0, b_1, b_2, b_3) \in \mathbb Z^4 : b_1 - b_2 - b_3 \equiv 0 \pmod 3\bigr\},$$
   so $S$ in cyclotomic coordinates is $S_{\mathrm{cyc}} = \mathbb Z^4 \times \Lambda_3$,
   the pullback Gram matrix on the power basis of $S$ is
   $G_S = (T_J \oplus T_M)^T G (T_J \oplus T_M)$ with $\det G_S = 9 \det G = 288\,000$,
   and on the glued ring $R = \mathbb Z[x]/(f g) \subset S$ ($[S:R] = 41$) the
   Gram determinant is $\det G_R = 41^2 \det G_S = 484\,128\,000$.
4. Modulo $41$, $j \equiv 10 \pmod{41}$ is the unique root of $\Phi_5(x) \equiv 0 \pmod{41}$
   satisfying $1 + x^2 \equiv 19 \pmod{41}$, and $m \equiv 27 \pmod{41}$ is the
   unique root of $\Phi_8(x) = x^4 + 1 \equiv 0 \pmod{41}$ satisfying
   $1 + x + x^2 \equiv 19 \pmod{41}$. Consequently, for every
   $z = (a_0, a_1, a_2, a_3, b_0, b_1, b_2, b_3) \in S_{\mathrm{cyc}}$, the
   resultant-$41$ evaluation difference $u(a) - v(b) \pmod{41}$ at $J \equiv 19$,
   $M \equiv 19 \pmod{41}$ equals
   $$u(a) - v(b) \equiv \sum_{r=0}^3 a_r\, 10^r - \sum_{s=0}^3 b_s\, 27^s \equiv \ell \cdot z \pmod{41},$$
   where $\ell = (1, 10, 18, 16, -1, -27, -32, -3)$.

### Proof

**(1) Minimal polynomials and resultant.**
Using $j^4 = -1 - j - j^2 - j^3$ and $j^5 = 1$, direct expansion of $J = 1 + j^2$
yields
$$J^0 = 1, \quad J^1 = 1 + j^2, \quad J^2 = -j + j^2 - j^3, \quad J^3 = -2 - 2j - 3j^3,$$
giving the columns of $T_J$, and $J^4 = -5 - 2j - 2j^2 - 5j^3 = 3J^3 - 4J^2 + 2J - 1$,
so $f(J) = 0$. Similarly, using $m^4 = -1$ and $M = 1 + m + m^2$, direct expansion
yields
$$M^0 = 1, \quad M^1 = 1 + m + m^2, \quad M^2 = 2m + 3m^2 + 2m^3, \quad M^3 = -5 + 5m^2 + 7m^3,$$
giving the columns of $T_M$, and $M^4 = -17 - 12m + 12m^3 = 4M^3 - 8M^2 + 4M - 1$,
so $g(M) = 0$. The Bezout identity
$$(14x^3 - 36x^2 + 43x + 64) f(x) + (-14x^3 + 22x^2 - 7x - 23) g(x) = 41$$
together with $f(19) = 68\,921 = 41 \times 1\,681 \equiv 0 \pmod{41}$ and
$g(19) = 61\,951 = 41 \times 1\,511 \equiv 0 \pmod{41}$ shows $\operatorname{Res}(f, g) = 41$
and $\gcd(f \bmod 41, g \bmod 41) = x - 19$.

**(2) Cyclotomic trace Gram matrix $G$.**
In $K_5 = \mathbb Q(j)$, $\overline{j^s} = j^{-s}$, so for $0 \le r, s \le 3$,
$j^r \overline{j^s} = j^{r-s}$ equals $1$ when $r = s$ (trace $4$) and a primitive
5th root of unity when $r \ne s$ (trace $-1$). Hence $(G_5)_{r,s} = 5\delta_{r,s} - 1$,
i.e. $G_5 = 5I_4 - \mathbf 1_4 \mathbf 1_4^T$, whose eigenvalues are $5$ (with
multiplicity $3$) and $5 - 4 = 1$ (with multiplicity $1$), so $\det G_5 = 5^3 \cdot 1 = 125$.
In $K_8 = \mathbb Q(m)$, $\overline{m^s} = m^{-s}$ and $\operatorname{Tr}_{K_8/\mathbb Q}(m^k) = 0$
for $1 \le k \le 3$, while $\operatorname{Tr}_{K_8/\mathbb Q}(1) = 4$. Thus
$(G_8)_{r,s} = 4\delta_{r,s}$, i.e. $G_8 = 4I_4$ with $\det G_8 = 4^4 = 256$, and
$\det G = 125 \times 256 = 32\,000$.

**(3) Index-3 sublattice $\Lambda_3$ and Gram determinants.**
Expanding $\det T_J$ and $\det T_M$ along their first columns gives
$$\det T_J = -\det\begin{pmatrix}-1 & -2\\-1 & -3\end{pmatrix} = -1,
\qquad
\det T_M = \det\begin{pmatrix}1 & 2 & 0\\1 & 3 & 5\\0 & 2 & 7\end{pmatrix} = 11 - 14 = -3.$$
For any $c = (c_0, c_1, c_2, c_3)^T \in \mathbb Z^4$, $b = T_M c$ has coordinates
$$b_0 = c_0 + c_1 - 5c_3,\quad b_1 = c_1 + 2c_2,\quad b_2 = c_1 + 3c_2 + 5c_3,\quad b_3 = 2c_2 + 7c_3,$$
whence
$$b_1 - b_2 - b_3 = -3(c_2 + 4c_3) \equiv 0 \pmod 3,$$
so $T_M(\mathbb Z^4) \subseteq \Lambda_3$. Conversely, for any $b \in \Lambda_3$,
setting $s = (-b_1 + b_2 + b_3)/3 \in \mathbb Z$, the integers
$$c_3 = 2s - b_3,\quad c_2 = 4b_3 - 7s,\quad c_1 = b_1 - 2c_2,\quad c_0 = b_0 - c_1 + 5c_3$$
satisfy $T_M c = b$. Thus $T_M(\mathbb Z^4) = \Lambda_3$ and
$\det G_S = (\det T_J)^2 (\det T_M)^2 \det G = 1 \cdot 9 \cdot 32\,000 = 288\,000$.

**(4) Resultant-41 linear form $\ell$.**
In $\mathbb F_{41}$, $10^2 = 100 \equiv 18 \pmod{41}$, $10^3 \equiv 16 \pmod{41}$,
$10^4 \equiv 37 \pmod{41}$, so $1 + 10 + 18 + 16 + 37 = 82 \equiv 0 \pmod{41}$ and
$1 + 10^2 \equiv 19 \pmod{41}$. Since $j^2 = J - 1 \equiv 18 \pmod{41}$ allows only
$j \equiv \pm 10 \pmod{41}$ and $\Phi_5(-10) = 1 - 10 + 18 - 16 + 37 = 30 \not\equiv 0 \pmod{41}$,
$j \equiv 10 \pmod{41}$ is unique, sending $(1, j, j^2, j^3) \mapsto (1, 10, 18, 16) \pmod{41}$.
Similarly, in $\mathbb F_{41}$, $27^2 = 729 \equiv 32 \pmod{41}$,
$27^3 \equiv 3 \pmod{41}$, $27^4 \equiv 81 \equiv -1 \pmod{41}$, and
$1 + 27 + 32 = 60 \equiv 19 \pmod{41}$. Since $m + m^2 = M - 1 \equiv 18 \pmod{41}$
has roots $m \equiv 27$ and $m \equiv 13 \pmod{41}$, and $13^4 = 28\,561 = 696 \times 41 + 25 \not\equiv -1 \pmod{41}$,
$m \equiv 27 \pmod{41}$ is unique, sending $-(1, m, m^2, m^3) \mapsto (-1, -27, -32, -3) \pmod{41}$.
Thus $u(a) - v(b) \equiv \ell \cdot z \pmod{41}$. $\blacksquare$

---

## 2. Theorem 2 — Universal Division-Free Integer Pair Involution on $\mathcal C = \mathbb Z^{81} \times \mathbb Z_{>0}$

### Statement

Let $G_0 = \operatorname{diag}(1, G) \in \mathbb Z^{9 \times 9}$ and
$L = G_0 \otimes G_0 \in \mathbb Z^{81 \times 81}$. On the universal integer pair
carrier
$$\mathcal C = \mathbb Z^{81} \times \mathbb Z_{>0},$$
define the scale content $m(X, D) = \gcd(X_0, \dots, X_{80}, D) \in \mathbb Z_{>0}$.
For any integer bound $Q \ge 8$ and program $z \in \mathbb Z^8$:
- If $z \notin B_Q = \{z \in S_{\mathrm{cyc}} : 0 < q(z) \le Q\}$, set $\widehat U_z(X, D) = (X, D)$.
- If $z \in B_Q$, set $A_z = 1 + q(z) \ge 5$, $d_z = A_z(A_z - 1) \ge 20$,
  $y_z = (1, z) \in \mathbb Z^9$, $w_z = y_z \otimes y_z \in \mathbb Z^{81}$,
  $e = (1, 0, \dots, 0) \in \mathbb Z^{81}$, $v_z = A_z e - w_z \in \mathbb Z^{81}$,
  $r_z = L v_z \in \mathbb Z^{81}$, $N_z = d_z I_{81} - v_z r_z^T \in \mathbb Z^{81 \times 81}$,
  and for $(X, D) \in \mathcal C$ define $Y = N_z X$, $M = d_z D$,
  $g = \gcd(Y_0, \dots, Y_{80}, M) \in \mathbb Z_{>0}$, and
  $$\widehat U_z(X, D) = \left(m(X, D)\,\frac{Y}{g},\; m(X, D)\,\frac{M}{g}\right) \in \mathcal C.$$

Then for every $z \in \mathbb Z^8$ and every $(X, D) \in \mathcal C$:
1. $\widehat U_z\bigl(\widehat U_z(X, D)\bigr) = (X, D)$ (exact involution on all of $\mathcal C$).
2. $m\bigl(\widehat U_z(X, D)\bigr) = m(X, D)$ and, setting $(X', D') = \widehat U_z(X, D)$,
   $$\frac{X'}{D'} = U_z\left(\frac{X}{D}\right), \qquad \frac{(X')^T L X'}{(D')^2} = \frac{X^T L X}{D^2}.$$
3. Whenever $z \in B_Q$, $\widehat U_z(e, 1) = (w_z, A_z)$ and $\widehat U_z(w_z, A_z) = (e, 1)$,
   and the rational rank-one projector of $(w_z, A_z)$ factors identically as
   $$\frac{w_z w_z^T L}{A_z^2} = \rho_z \otimes \rho_z, \qquad \rho_z = \frac{y_z y_z^T G_0}{A_z}.$$

### Proof

If $z \notin B_Q$, $\widehat U_z = \mathrm{id}_{\mathcal C}$ and (1)–(2) are immediate.
Suppose $z \in B_Q$. Since $e^T L e = 1$, $e^T L w_z = (e_0^T G_0 y_z)^2 = 1$, and
$w_z^T L w_z = (y_z^T G_0 y_z)^2 = A_z^2$, we have
$$r_z^T v_z = v_z^T L v_z = A_z^2 - 2A_z + A_z^2 = 2A_z(A_z - 1) = 2d_z, \qquad r_z^T e = A_z - 1.$$
Therefore
$$N_z^2 = (d_z I_{81} - v_z r_z^T)^2 = d_z^2 I_{81} - 2d_z v_z r_z^T + (r_z^T v_z) v_z r_z^T = d_z^2 I_{81},$$
and since $L v_z r_z^T = r_z r_z^T$ is symmetric,
$$N_z^T L N_z = (d_z I_{81} - r_z v_z^T) L (d_z I_{81} - v_z r_z^T) = d_z^2 L - 2d_z r_z r_z^T + (v_z^T L v_z) r_z r_z^T = d_z^2 L.$$
Thus $U_z = N_z / d_z$ satisfies $U_z^2 = I_{81}$ and $U_z^T L U_z = L$.

Now let $(X, D) \in \mathcal C$ and $(X', D') = \widehat U_z(X, D)$. By definition
of $g = \gcd(Y, M)$, the pair $(Y/g, M/g)$ is primitive ($\gcd(Y/g, M/g) = 1$) with
$M/g \ge 1$. Multiplying by $m(X, D) \ge 1$ gives
$$m(X', D') = m(X, D)\gcd(Y/g, M/g) = m(X, D)$$
and
$$\frac{X'}{D'} = \frac{Y}{M} = \frac{N_z X}{d_z D} = U_z\left(\frac{X}{D}\right).$$
Applying $\widehat U_z$ a second time to $(X', D')$ yields $(X'', D'') = \widehat U_z(X', D')$
with $m(X'', D'') = m(X', D') = m(X, D)$ and
$$\frac{X''}{D''} = U_z\left(\frac{X'}{D'}\right) = U_z^2\left(\frac{X}{D}\right) = \frac{X}{D}.$$
Since $(X'', D''), (X, D) \in \mathbb Z^{81} \times \mathbb Z_{>0}$ share the same
rational ratio $X''/D'' = X/D$ and the same positive greatest common divisor
$m(X'', D'') = m(X, D)$, we have $D'' = D$ and $X'' = X$, proving (1) and (2).

Finally, for $(X, D) = (e, 1)$, we have $m(e, 1) = 1$, $M = A_z(A_z - 1)$, and
$$Y = N_z e = A_z(A_z - 1)e - (A_z - 1)(A_z e - w_z) = (A_z - 1) w_z.$$
Because the $0$-th coordinate of $w_z = y_z \otimes y_z$ is $y_{z,0}^2 = 1$,
$\gcd(w_{z,0}, \dots, w_{z,80}, A_z) = 1$, so $g = \gcd((A_z - 1)w_z, A_z(A_z - 1)) = A_z - 1$,
whence $\widehat U_z(e, 1) = (w_z, A_z)$, and by (1), $\widehat U_z(w_z, A_z) = (e, 1)$. $\blacksquare$

---

## 3. Theorem 3 — Positive-Definite Integer Energy & Bank Account $E + b$ and Port-Independent Sharp Bank Threshold

### Statement

For capacity $K \ge 1$ and bound $Q \ge 8$, let the state space be
$$\Omega_K = \mathbb Z^8 \times \mathbb Z^8 \times \mathcal C \times \mathcal C^K \times \mathbb Z \times \{0, 1\} \times \mathbb Z_{\ge 0} \times \{-1, +1\},$$
with states $\mathcal S = (u, b, \varepsilon)$, where
$u = (z, z_{\mathrm{arch}}, P, (B_0, \dots, B_{K-1}), n, p)$, direction-reversal
involution $J_{\mathrm{dir}}(u, b, \varepsilon) = (u, b, -\varepsilon)$, cell cost
$E_{\mathrm{cell}}(X, D) = X^T L X + D^2$, and total state energy
$$E(u) = 1 + q(z) + q(z_{\mathrm{arch}}) + E_{\mathrm{cell}}(P) + \sum_{j=0}^{K-1} E_{\mathrm{cell}}(B_j) + n^2 + p^2.$$
Let $T_\varepsilon$ be the 2-phase core transition defined in `PREREG.md` §2.3 and
$F(u, b, \varepsilon)$ the funded step: for $u' = T_\varepsilon(u)$ and
$b' = b + E(u) - E(u')$, $F(u, b, \varepsilon) = (u', b', \varepsilon)$ if $b' \ge 0$
and $(u, b, -\varepsilon)$ if $b' < 0$.

1. **Finite Level Sets:** Since $G \ge I_8$ and $L \ge I_{81}$,
   $E(u) \ge 1 + \|z\|_2^2 + \|z_{\mathrm{arch}}\|_2^2 + (\|X_P\|_2^2 + D_P^2) + \sum_{j=0}^{K-1}(\|X_{B_j}\|_2^2 + D_{B_j}^2) + n^2 + p^2$.
   Hence for every integer $C \ge 1$, the constant-budget level set
   $\{\mathcal S \in \Omega_K : E(u) + b = C\}$ is strictly finite.
2. **Exact Bijectivity and Budget Conservation:** $T_{-1} \circ T_{+1} = T_{+1} \circ T_{-1} = \mathrm{id}$,
   $F$ is a bijection on $\Omega_K$ satisfying $F^{-1} = J_{\mathrm{dir}} \circ F \circ J_{\mathrm{dir}}$,
   and $E + b$ is invariant under $F$.
3. **Port-Independent Sharp Bank Threshold:** For any admitted program $z \in B_Q$,
   any program archive $z_{\mathrm{arch}} \in \mathbb Z^8$, any occupied initial
   output port $P_0 = (X_{P_0}, D_{P_0}) \in \mathcal C$, and ready stock
   $B_0 = \dots = B_{K-1} = (e, 1)$ starting at $(n_0 = 0, p_0 = 0, \varepsilon_0 = +1)$,
   the cumulative energy differences $E_t - E_0$ along the $2K$-step trajectory
   $u_t = T_{+1}^t(u_0)$ ($0 \le t \le 2K$) are:
   $$E_{2r} - E_0 = 2r\bigl(A_z^2 - 1\bigr) + r^2 \quad (0 \le r \le K),$$
   $$E_{2r+1} - E_0 = 2(r+1)\bigl(A_z^2 - 1\bigr) + r^2 + 1 \quad (0 \le r < K).$$
   In particular, the sequence $E_0, E_1, \dots, E_{2K}$ is monotonically
   non-decreasing ($E_0 < E_1 = E_2 < E_3 < E_4 < \dots < E_{2K}$), and the sharp
   initial bank required to complete all $K$ pair rounds ($2K$ fresh outputs) is
   $$\boxed{b_{\mathrm{sharp}}(z, K) = E_{2K} - E_0 = 2K\bigl(A_z^2 - 1\bigr) + K^2 = 2K\,q(z)\bigl(q(z) + 2\bigr) + K^2,}$$
   which is strictly independent of the initial occupied port state $P_0$ and of $z_{\mathrm{arch}}$.
4. **Underfunded Bounce at $b_0 = b_{\mathrm{sharp}}(z, K) - 1$:** For $K \ge 2$ and
   $b_0 = b_{\mathrm{sharp}}(z, K) - 1$, $F$ executes $2K - 1$ forward steps to
   $(n = K-1, p = 1)$ with remaining bank $b_{2K-1} = 2K - 3$, rejects step $2K$
   (whose cost is $E_{2K} - E_{2K-1} = 2(K-1) > 2K - 3$) by flipping $\varepsilon: +1 \to -1$,
   and in the next $2K - 1$ steps unwinds back to $(u_0, b_0, -1)$.

### Proof

**(1) Positivity and finite level sets.**
The eigenvalues of $G_5 = 5I_4 - \mathbf 1_4\mathbf 1_4^T$ are $\{1, 5, 5, 5\}$ and
those of $G_8 = 4I_4$ are $\{4, 4, 4, 4\}$, so $G \ge I_8$, $G_0 = \operatorname{diag}(1, G) \ge I_9$,
and $L = G_0 \otimes G_0 \ge I_{81}$. Every coordinate of $u$ and $b \ge 0$ is
therefore bounded in magnitude by $\sqrt{C}$ whenever $E(u) + b = C$, so each level
set is finite.

**(2) Core and funded bijectivity.**
If $p = 0$, $T_{+1}$ sets $(n', p') = (n, 1)$ and (when $z \in B_Q$ and $0 \le n < K$)
applies the involution $\widehat U_z$ to $B_n$; $T_{-1}$ at $p' = 1$ sees the same
index $n' = n$, applies $\widehat U_z$ again to $B'_n$, and restores $(n, 0)$.
If $p = 1$, $T_{+1}$ swaps $(P, B_n)$ (when $z \in B_Q$ and $0 \le n < K$) and sets
$(n', p') = (n + 1, 0)$; $T_{-1}$ at $p' = 0$ uses $n_{\mathrm{prev}} = n' - 1 = n$,
swaps $(P', B'_n)$ back, and restores $(n, 1)$. Thus $T_{-1} = T_{+1}^{-1}$.
For $F(u, b, \varepsilon)$, if $b' = b + E(u) - E(T_\varepsilon(u)) \ge 0$, then
$F(u, b, \varepsilon) = (u', b', \varepsilon)$ has $E(u') + b' = E(u) + b$, and
$T_{-\varepsilon}(u') = u$ has proposed bank $b' + E(u') - E(u) = b \ge 0$, so
$(J_{\mathrm{dir}} \circ F \circ J_{\mathrm{dir}})(u', b', \varepsilon) = (u, b, \varepsilon)$.
If $b' < 0$, then $F(u, b, \varepsilon) = (u, b, -\varepsilon)$ and
$(J_{\mathrm{dir}} \circ F \circ J_{\mathrm{dir}})(u, b, -\varepsilon) = (u, b, \varepsilon)$.

**(3) Exact energy trajectory and port-independence.**
On the ready pair $(e, 1)$, $E_{\mathrm{cell}}(e, 1) = 1^2 + 1^2 = 2$. On the
prepared pair $\widehat U_z(e, 1) = (w_z, A_z)$, $w_z^T L w_z = (y_z^T G_0 y_z)^2 = A_z^2$,
so $E_{\mathrm{cell}}(w_z, A_z) = A_z^2 + A_z^2 = 2A_z^2$, an increase of
$2(A_z^2 - 1)$ per prepared stock cell.
During round $r \in \{0, \dots, K-1\}$:
- Step $t = 2r \to 2r+1$ ($p: 0 \to 1$ at $n = r$): replaces $B_r = (e, 1)$ by
  $(w_z, A_z)$ and changes $p^2$ from $0$ to $1$, increasing $E$ by
  $$\Delta E_{r,0} = 2(A_z^2 - 1) + 1 > 0.$$
- Step $t = 2r+1 \to 2r+2$ ($p: 1 \to 0, n: r \to r+1$): swaps $P$ and $B_r$,
  which preserves $E_{\mathrm{cell}}(P) + E_{\mathrm{cell}}(B_r)$ identically for
  every occupied state $P$, and changes $n^2 + p^2$ from $r^2 + 1$ to $(r+1)^2 + 0$,
  increasing $E$ by
  $$\Delta E_{r,1} = (r+1)^2 - (r^2 + 1) = 2r \ge 0.$$
Summing over $r$ yields $E_{2r} - E_0 = 2r(A_z^2 - 1) + r^2$ and
$E_{2r+1} - E_0 = 2(r+1)(A_z^2 - 1) + r^2 + 1$. Since $\Delta E_{r,0} > 0$ and
$\Delta E_{r,1} \ge 0$ for all $r \ge 0$, $\max_{0 \le t \le 2K} (E_t - E_0) = E_{2K} - E_0 = 2K(A_z^2 - 1) + K^2$,
independent of $P_0$ and $z_{\mathrm{arch}}$.

**(4) Underfunded bounce.**
For $K \ge 2$, the final step $2K - 1 \to 2K$ has cost $\Delta E_{K-1,1} = 2(K - 1) \ge 2$.
With $b_0 = E_{2K} - E_0 - 1$, every step $1 \le t \le 2K - 1$ has $E_t - E_0 \le E_{2K-1} - E_0 = b_0 - (2K - 3) \le b_0$,
so the first $2K - 1$ steps succeed and leave $b_{2K-1} = 2K - 3 < 2(K - 1) = E_{2K} - E_{2K-1}$.
Step $2K$ therefore has $b' = -1 < 0$, reflects $\varepsilon: +1 \to -1$, and the
subsequent $2K - 1$ steps follow $T_{-1} = T_{+1}^{-1}$ back to $(u_0, b_0, -1)$. $\blacksquare$
