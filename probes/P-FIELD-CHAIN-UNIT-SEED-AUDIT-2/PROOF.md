# Independent Proof: P-FIELD-CHAIN-UNIT-SEED-AUDIT-2

**Status:** `NON-CANONICAL` independent review proof at L1.
**Basis:** Public Canon v102 (`a632c6a162dc87e60104d7a478e7650a6d5c4a1b`, content `b04e22dd3ed8e4240cff347364f24670d4183a4d`), program #1548 lane RB, public lock #1565 (successor of abandoned #1561 / PR #1564).

## 1. Canonical premises and exact matrix identities

From `FIELD-CONSERVATIVE-CHAIN-LAW` (shared proof section 2 of `canon/CANON.md`), for $y = (a,b,c,d)^T \in \mathbb{Z}^4$:

$$
A_f = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ -2 & 1 & -1 & 1 \\ 1 & -3 & 1 & -2 \end{pmatrix}, \quad
B_f = \begin{pmatrix} 4 & -2 & 2 & -1 \\ -2 & 6 & -1 & 3 \\ 2 & -1 & 2 & 0 \\ -1 & 3 & 0 & 2 \end{pmatrix}, \quad
L = \begin{pmatrix} 1 & -3 & -1 & -2 \\ -3 & 4 & -2 & 1 \\ 0 & 5 & 1 & 2 \\ 5 & -5 & 2 & -1 \end{pmatrix},
$$

$$
V_{\mathrm{inv}} = \begin{pmatrix} 1 & 2 & 1 & 2 \\ 2 & -1 & 2 & -1 \\ 0 & -5 & 1 & -3 \\ -5 & 5 & -3 & 4 \end{pmatrix}, \quad
H(y) = \frac{1}{2} y^T B_f y = 2a^2 - 2ab + 3b^2 + c^2 + d^2 + 2ac - ad - bc + 3bd.
$$

Direct integer matrix multiplication establishes:
1. $A_f^5 = I_4$, $\sum_{k=0}^4 A_f^k = 0$, and $A_f^T B_f A_f = B_f$, so $H(A_f y) = H(y)$ for all $y \in \mathbb{Z}^4$, and the only vector $y \in \mathbb{Z}^4$ with $A_f y = y$ is $y = 0$ (since $5y = \sum_{k=0}^4 A_f^k y = 0$).
2. $L = (I_4 - A_f)(I_4 - A_f^2)$, $A_f L = L A_f$, $L^2 = 5 A_f^3$, $V_{\mathrm{inv}} = A_f^2 L$, $V_{\mathrm{inv}} L = L V_{\mathrm{inv}} = 5 I_4$, $\det(L) = 25$, and $L^T B_f L = 5 B_f$, so $H(Lx) = 5 H(x)$ for all $x \in \mathbb{Z}^4$.

---

## 2. Theorem 1 (Native block Schur-complement identity, sharp adjugate bounds, and complete $H(u)=1$ classification)

### 2.1 Exact block Schur-complement and adjugate identities

Partition $B_f$ into $2 \times 2$ blocks corresponding to $(a,b)$ and $(c,d)$:

$$
B_f = \begin{pmatrix} M_{ab} & U \\ U^T & 2 I_2 \end{pmatrix}, \qquad
M_{ab} = \begin{pmatrix} 4 & -2 \\ -2 & 6 \end{pmatrix}, \quad
U = \begin{pmatrix} 2 & -1 \\ -1 & 3 \end{pmatrix}.
$$

Because the lower-right block is $2 I_2$, completing the squares in $c$ and $d$ in $4 H(a,b,c,d) = 2 y^T B_f y$ gives the exact polynomial identity over $\mathbb{Z}[a,b,c,d]$:

$$
4 H(a,b,c,d) = (3a^2 + 2ab + 2b^2) + (2c + 2a - b)^2 + (2d - a + 3b)^2. \tag{1}
$$

Indeed, expanding the right-hand side gives
$$
(3a^2 + 2ab + 2b^2) + (4c^2 + 4a^2 + b^2 + 8ac - 4bc - 4ab) + (4d^2 + a^2 + 9b^2 - 4ad + 12bd - 6ab)
= 8a^2 - 8ab + 12b^2 + 4c^2 + 4d^2 + 8ac - 4ad - 4bc + 12bd = 4 H(a,b,c,d).
$$

Furthermore, the binary quadratic form $Q_{ab}(a,b) = 3a^2 + 2ab + 2b^2$ (twice the Schur complement $M_{ab} - \frac{1}{2} U U^T = \frac{1}{2}\begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$) satisfies the two exact integer identities

$$
2(3a^2 + 2ab + 2b^2) = 5a^2 + (a + 2b)^2, \qquad
3(3a^2 + 2ab + 2b^2) = 5b^2 + (3a + b)^2. \tag{2}
$$

Consequently:
- $H(y) \ge 0$ for all $y \in \mathbb{R}^4$, and $H(y) = 0 \iff a = b = 2c+2a-b = 2d-a+3b = 0 \iff y = 0$.
- $\det(B_f) = \det(2 I_2) \det\left(M_{ab} - \frac{1}{2} U U^T\right) = 4 \cdot \frac{3 \cdot 2 - 1}{4} = 5$.
- The integer adjugate matrix $\operatorname{adj}(B_f) = 5 B_f^{-1}$ is explicitly
  $$
  5 B_f^{-1} = \begin{pmatrix}
  4 & -2 & -5 & 5 \\
  -2 & 6 & 5 & -10 \\
  -5 & 5 & 10 & -10 \\
  5 & -10 & -10 & 20
  \end{pmatrix}, \qquad
  B_f (5 B_f^{-1}) = (5 B_f^{-1}) B_f = 5 I_4,
  $$
  whose diagonal entries are $(4, 6, 10, 20)$. By Cauchy–Schwarz for the positive-definite inner product $\langle u, v \rangle = u^T B_f v$ applied to $e_i^T y = \langle B_f^{-1} e_i, y \rangle$,
  $$
  y_i^2 \le (e_i^T B_f^{-1} e_i)(y^T B_f y) = \frac{2 (5 B_f^{-1})_{ii}}{5} H(y),
  $$
  yielding the sharp native coordinate bounds for every $y = (a,b,c,d) \in \mathbb{Z}^4$ with $H(y) \le k$:
  $$
  5a^2 \le 8k, \qquad 5b^2 \le 12k, \qquad c^2 \le 4k, \qquad d^2 \le 8k. \tag{3}
  $$

### 2.2 Complete hand classification of the unit shell $H(u) = 1$

For $k = 1$, (3) forces $a^2 \le \lfloor 8/5 \rfloor = 1$, $b^2 \le \lfloor 12/5 \rfloor = 2 \implies |b| \le 1$, $c^2 \le 4 \implies |c| \le 2$, and $d^2 \le 8 \implies |d| \le 2$. Thus every integer solution of $H(u) = 1$ lies in the 225-point box $[-1,1]^2 \times [-2,2]^2 \subset [-2,2]^4$.

Even without scanning those 225 points, (1) writes $H(a,b,c,d) = 1$ as
$$
(2c + 2a - b)^2 + (2d - a + 3b)^2 = 4 - (3a^2 + 2ab + 2b^2),
$$
where $s_1 = 2c + 2a - b \equiv b \pmod 2$ and $s_2 = 2d - a + 3b \equiv a + b \pmod 2$:
1. $(a,b) = (0,0)$: $Q_{ab} = 0$, $(2c)^2 + (2d)^2 = 4 \iff c^2 + d^2 = 1$, giving **4 units**:
   $(0,0,\pm 1,0)$ and $(0,0,0,\pm 1)$.
2. $(a,b) = (0, \pm 1)$: $Q_{ab} = 2$, $s_1^2 + s_2^2 = 2$ with $s_1, s_2$ odd $\iff s_1, s_2 \in \{\pm 1\}$.
   - For $(a,b) = (0,1)$: $2c - 1 \in \{\pm 1\} \iff c \in \{0,1\}$ and $2d + 3 \in \{\pm 1\} \iff d \in \{-2,-1\}$ (4 units).
   - For $(a,b) = (0,-1)$: $2c + 1 \in \{\pm 1\} \iff c \in \{-1,0\}$ and $2d - 3 \in \{\pm 1\} \iff d \in \{1,2\}$ (4 units, including $u^* = (0,-1,-1,2)$).
   Total from $(0,\pm 1)$: **8 units**.
3. $(a,b) = (\pm 1, 0)$: $Q_{ab} = 3$, $s_1^2 + s_2^2 = 1$ with $s_1$ even and $s_2$ odd $\iff s_1 = 0, s_2 \in \{\pm 1\}$.
   - For $(a,b) = (1,0)$: $2c + 2 = 0 \iff c = -1$ and $2d - 1 \in \{\pm 1\} \iff d \in \{0,1\}$ (2 units).
   - For $(a,b) = (-1,0)$: $c = 1$ and $d \in \{-1,0\}$ (2 units).
   Total from $(\pm 1, 0)$: **4 units**.
4. $(a,b) = \pm(1,-1)$: $Q_{ab} = 3 - 2 + 2 = 3$, $s_1^2 + s_2^2 = 1$ with $s_1$ odd and $s_2$ even $\iff s_1 \in \{\pm 1\}, s_2 = 0$.
   - For $(a,b) = (1,-1)$: $2c + 3 \in \{\pm 1\} \iff c \in \{-2,-1\}$ and $2d - 4 = 0 \iff d = 2$ (2 units).
   - For $(a,b) = (-1,1)$: $c \in \{1,2\}$ and $d = -2$ (2 units).
   Total from $\pm(1,-1)$: **4 units**.
5. $(a,b) = \pm(1,1)$: $Q_{ab} = 3 + 2 + 2 = 7 > 4$, so **0 units**.

Hence there are exactly $4 + 8 + 4 + 4 = 20$ integer solutions to $H(u) = 1$, and all 20 satisfy $a,b \in [-1,1]$ and $c,d \in [-2,2]$.

---

## 3. Theorem 2 (Exact kernel of $L \bmod 5$, unit-shell injectivity, and missing gate residues)

### 3.1 The gate-residue group $\mathcal{G}_{25}$ and $\ker(x \mapsto Lx \bmod 5) = L\mathbb{Z}^4$

By `canon/CANON.md` lines 8023–8037, $y = (r_0,r_1,r_2,r_3)^T \in L\mathbb{Z}^4$ if and only if $r_0 + 2r_1 \equiv 0 \pmod 5$ and $r_2 + 2r_3 \equiv 0 \pmod 5$. Reducing modulo $5$, the image of $\pi_L : \mathbb{Z}^4 \to \mathbb{F}_5^4$, $\pi_L(x) = Lx \bmod 5$, is the 25-element subgroup

$$
\mathcal{G}_{25} = \{r \in \mathbb{F}_5^4 : r_0 + 2r_1 \equiv r_2 + 2r_3 \equiv 0 \pmod 5\}
= \{(3r_1, r_1, 3r_3, r_3) \bmod 5 : (r_1, r_3) \in \mathbb{F}_5^2\}.
$$

**Lemma (Exact kernel of $\pi_L$).** $\ker(\pi_L) = \{x \in \mathbb{Z}^4 : Lx \in 5\mathbb{Z}^4\} = L\mathbb{Z}^4$.

*Proof.* If $x = Lw$ with $w \in \mathbb{Z}^4$, then $Lx = L^2 w = 5 A_f^3 w \in 5\mathbb{Z}^4$. Conversely, if $Lx = 5z$ for $z \in \mathbb{Z}^4$, multiplying on the left by $V_{\mathrm{inv}} = A_f^2 L$ and using $V_{\mathrm{inv}} L = 5 I_4$ yields $5x = 5 V_{\mathrm{inv}} z = 5 L(A_f^2 z)$, so $x = L(A_f^2 z) \in L\mathbb{Z}^4$. $\square$

### 3.2 Injectivity of $\pi_L$ on the unit shell $\{u \in \mathbb{Z}^4 : H(u) = 1\}$

Suppose $u_1, u_2 \in \mathbb{Z}^4$ satisfy $H(u_1) = H(u_2) = 1$ and $Lu_1 \equiv Lu_2 \pmod 5$. By the Lemma, $u_1 - u_2 = Lw$ for some $w \in \mathbb{Z}^4$, so $H(u_1 - u_2) = H(Lw) = 5 H(w) \in 5\mathbb{Z}_{\ge 0}$. On the other hand, by the triangle inequality (Cauchy–Schwarz) for the positive-definite form $H$,
$$
0 \le H(u_1 - u_2) \le \left(\sqrt{H(u_1)} + \sqrt{H(u_2)}\right)^2 = (1 + 1)^2 = 4 < 5.
$$
The only multiple of $5$ in $\{0,1,2,3,4\}$ is $0$, so $H(u_1 - u_2) = 0$, which by positive-definiteness of $H$ forces $u_1 = u_2$. Thus the 20 unit seeds map to **20 distinct** gate residues in $\mathcal{G}_{25}$ (each with multiplicity 1).

### 3.3 Exact characterization of the 5 missing gate residues

For any $r = (3r_1, r_1, 3r_3, r_3)^T \in \mathcal{G}_{25}$, direct multiplication by $A_f$ modulo $5$ gives
$$
A_f \begin{pmatrix} 3r_1 \\ r_1 \\ 3r_3 \\ r_3 \end{pmatrix}
= \begin{pmatrix} 3(r_1 + r_3) \\ r_1 + r_3 \\ -5r_1 - 2r_3 \\ r_3 \end{pmatrix}
\equiv \begin{pmatrix} 3(r_1 + r_3) \\ r_1 + r_3 \\ 3r_3 \\ r_3 \end{pmatrix} \pmod 5.
$$
Thus $A_f \bmod 5$ acts on the $(r_1, r_3)$ coordinates of $\mathcal{G}_{25}$ by the unipotent shear $(r_1, r_3) \mapsto (r_1 + r_3, r_3) \pmod 5$. Its fixed subgroup on $\mathcal{G}_{25}$ is the 5-element subgroup characterized by $r_3 = 0$ (and hence $r_2 \equiv 3r_3 \equiv 0 \pmod 5$):
$$
\mathcal{G}_{25}^{A_f} = \{r \in \mathcal{G}_{25} : A_f r \equiv r \pmod 5\}
= \{(0,0,0,0),\; (3,1,0,0),\; (1,2,0,0),\; (4,3,0,0),\; (2,4,0,0)\}.
$$

If a unit seed $u \in \mathbb{Z}^4$ with $H(u) = 1$ had $\pi_L(u) \in \mathcal{G}_{25}^{A_f}$, then $\pi_L(A_f u - u) = (A_f - I_4)\pi_L(u) = 0$ in $\mathbb{F}_5^4$, so $A_f u - u \in \ker(\pi_L) = L\mathbb{Z}^4$ by the Lemma. Since $H(A_f u) = H(u) = 1$, Cauchy–Schwarz again gives $0 \le H(A_f u - u) \le 4 < 5$ while $H(A_f u - u) \in 5\mathbb{Z}_{\ge 0}$, forcing $H(A_f u - u) = 0 \implies A_f u = u \implies u = 0$, contradicting $H(u) = 1$.

Therefore:
- Every residue in $\mathcal{G}_{25}^{A_f}$ has unit-seed multiplicity $0$.
- Because $|\mathcal{G}_{25} \setminus \mathcal{G}_{25}^{A_f}| = 25 - 5 = 20$ and $\pi_L$ is injective on the 20-element unit shell, the 20 unit seeds map **bijectively** onto $\mathcal{G}_{25} \setminus \mathcal{G}_{25}^{A_f} = \{(3r_1, r_1, 3r_3, r_3) \bmod 5 : r_1 \in \mathbb{F}_5,\; r_3 \in \mathbb{F}_5^\times\}$.
- For the 4 nonzero missing gate residues in $\mathcal{G}_{25}^{A_f} \setminus \{0\}$, taking $u_0 = (0,0,1,0)$ ($H(u_0)=1$, $\pi_L(u_0) = (4,3,1,2)$) gives $x_1 = A_f u_0 - u_0 = (1,0,-2,1)$ with $H(x_1) = 2$ and $\pi_L(x_1) = (A_f - I_4)\pi_L(u_0) = (1,2,0,0) \neq 0$, and its multiples/orbits in the $H(x)=2$ shell attain all 4 nonzero residues in $\mathcal{G}_{25}^{A_f} \setminus \{0\}$ with minimum coset energy $H(Lx) = 5 \cdot 2 = 10$.

---

## 4. Theorem 3 (Exact coset minimum, attainment, and uniqueness for $\bar{y}_3 = (0,0,3,1)$)

Consider the complete integer coset
$$
\mathcal{C}(\bar{y}_3) = \{y \in L\mathbb{Z}^4 : y \equiv \bar{y}_3 = (0,0,3,1) \pmod 5\}.
$$
1. Because $\bar{y}_3 = (3 \cdot 0, 0, 3 \cdot 1, 1) \in \mathcal{G}_{25} \setminus \mathcal{G}_{25}^{A_f}$ has $r_1 = 0$ and $r_3 = 1 \neq 0$, Theorem 2 guarantees that $\bar{y}_3$ has a **unique** preimage in the unit shell $\{u \in \mathbb{Z}^4 : H(u) = 1\}$.
2. Explicitly, $u^* = (0, -1, -1, 2)^T \in \mathbb{Z}^4$ satisfies $H(u^*) = 3(-1)^2 + (-1)^2 + 2^2 - (-1)(2) + 3(-1)(2) = 1$ and
   $$
   y^* = L u^* = \begin{pmatrix} 1 & -3 & -1 & -2 \\ -3 & 4 & -2 & 1 \\ 0 & 5 & 1 & 2 \\ 5 & -5 & 2 & -1 \end{pmatrix} \begin{pmatrix} 0 \\ -1 \\ -1 \\ 2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ -2 \\ 1 \end{pmatrix} \equiv \begin{pmatrix} 0 \\ 0 \\ 3 \\ 1 \end{pmatrix} = \bar{y}_3 \pmod 5,
   $$
   with $H(y^*) = 5 H(u^*) = 5$.
3. For any $y \in \mathcal{C}(\bar{y}_3)$, since $\det(L) = 25 \neq 0$, there is a unique $x \in \mathbb{Z}^4$ with $y = Lx$. Because $y \equiv \bar{y}_3 \not\equiv 0 \pmod 5$, $x \neq 0$, so $H(x) \ge 1$ by positive-definiteness and integrality of $H$, and therefore $H(y) = 5 H(x) \ge 5$.
4. Equality $H(y) = 5$ holds if and only if $H(x) = 1$ and $Lx \equiv \bar{y}_3 \equiv Lu^* \pmod 5$, which by the unit-shell injectivity of Theorem 2.2 forces $x = u^* = (0,-1,-1,2)^T$ and $y = y^* = (0,0,-2,1)^T$.

Thus $\min_{y \in \mathcal{C}(\bar{y}_3)} H(y) = 5$, attained uniquely on all of $L\mathbb{Z}^4$ at $y^* = L u^* = (0,0,-2,1)^T$ with $u^* = (0,-1,-1,2)^T$.

---

## 5. Lineage vs. novelty boundary (#1323 and `canon/CANON.md`)

- **Inherited from `canon/CANON.md` (`FIELD-CONSERVATIVE-CHAIN-LAW`, shared proof section 2):** Definitions of $A_f, B_f, L, V_{\mathrm{inv}}, H$, the identities $L = (I_4 - A_f)(I_4 - A_f^2)$, $L^2 = 5 A_f^3$, $V_{\mathrm{inv}} = A_f^2 L$, $V_{\mathrm{inv}} L = 5 I_4$, $H(Lx) = 5 H(x)$, $\det(L) = 25$, the 25-element image criterion $r_0+2r_1 \equiv r_2+2r_3 \equiv 0 \pmod 5$, and the $4 H_{\mathrm{raw}}$ sum-of-squares formula.
- **Inherited from #1323 (`C-FIELD-J-ENERGY-READOUT-N` / `3f53cff429c67fbdfa95941b3024279d9fd59638`):** The $C_{\mathrm{cyc}}$ $A_4$-Cartan chart, the $5 K^{-1}$ Cauchy–Schwarz bound $|a_0|,|a_3| \le 3, |a_1|,|a_2| \le 2$ in $C_{\mathrm{cyc}}$ coordinates for $H \le 5$, and the total shell counts $(1, 20, 30, 60, 60, 120)$ (291 states for $0 \le H \le 5$, including the count of 20 unit seeds at $H = 1$).
- **Genuinely new scope in Lane B / RB:**
  1. Direct native-coordinate completeness bounds for $H(y) \le k$ and $H(u) = 1$ in the literal $B_f$ coordinates (both the author's $4H(y)$ SOS box and our sharper Schur-complement/adjugate box $[-1,1]^2 \times [-2,2]^2$ and two-square fiber decomposition).
  2. Complete classification of the residue map $\pi_L : u \mapsto Lu \bmod 5$ on the 20 unit seeds over the 25 gate residues $\mathcal{G}_{25}$, proving multiplicity $1$ on the 20 residues with $r_3 \not\equiv 0 \pmod 5$ and multiplicity $0$ on the 5 $A_f$-fixed residues $\mathcal{G}_{25}^{A_f} = \{(3r_1, r_1, 0, 0) \bmod 5\}$.
  3. Exact coset minimum $\min_{y \in \mathcal{C}(\bar{y}_3)} H(y) = 5$ and its unique attainment at $y^* = Lu^* = (0,0,-2,1)^T$, $u^* = (0,-1,-1,2)^T$.
