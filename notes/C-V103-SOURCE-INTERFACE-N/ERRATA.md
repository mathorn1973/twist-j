# Additive Errata and Review Reconciliation (R1–R7): C-V103-SOURCE-INTERFACE-N

**NON-CANONICAL / L1 / additive errata record.**  
A. M. Thorn, 2026-10-16. Original work Apache-2.0.  
Candidate `C-V103-SOURCE-INTERFACE-N`, program [#1548](https://github.com/mathorn1973/twist-j/issues/1548) (Lane D), child issue [#1551](https://github.com/mathorn1973/twist-j/issues/1551), draft PR [#1558](https://github.com/mathorn1973/twist-j/pull/1558).  
Specification pin (unchanged): `9cb2b7d89eb1fc955fb67e886e46a379cb1aba43`.  
Reviewed initial result commit (preserved as git parent): `e3d35709a86b42c21c1bf57e2be2b3a3cf707598`.  
Independent review reference: `C-V103-SOURCE-INTERFACE-REVIEW-N` (Lane RD, reviewer session `Codex-v103-RD-20261016`, issue [#1560](https://github.com/mathorn1973/twist-j/issues/1560), independent proof pin `2c9718dbb9661eebdfaf150affb5a3e25eda20fa`, review comparison commit `2a43c0312af7189b84c099c9482b908ac8e9323b`, draft PR [#1563](https://github.com/mathorn1973/twist-j/pull/1563), review comment [#1558 (comment)](https://github.com/mathorn1973/twist-j/pull/1558#issuecomment-6225244124)).

---

## 1. Purpose and Custody

This file records the additive mathematical corrections to the initial result commit `e3d35709a86b42c21c1bf57e2be2b3a3cf707598` required by findings `R1`–`R7` of independent review `C-V103-SOURCE-INTERFACE-REVIEW-N` (`2a43c0312af7189b84c099c9482b908ac8e9323b`).

1. The five specification files pinned at `9cb2b7d89eb1fc955fb67e886e46a379cb1aba43` (`README.md`, `CONTRACT.md`, `PREREG.md`, `SOURCES.tsv`, `INPUTS.sha256`) remain byte-for-byte unchanged.
2. The initial result commit `e3d35709a86b42c21c1bf57e2be2b3a3cf707598` is preserved in the branch history as the direct parent of this repair commit.
3. No scientific script or numerical search was run (`scientific_code: NONE / NOT_RUN`).

---

## 2. Item-by-Item Errata and Exact Mathematical Repairs (R1–R7)

### R1 — Three-step preimage cardinality is $625$, not $250$ (`PROOF.md` lines 238, 242–244; `RESULT.md` line 33; `INTERFACE.json` line 100)

- **Flawed statement in `e3d35709a86b42c21c1bf57e2be2b3a3cf707598`:**
  Called $\mathcal{P}_{\mathrm{gate}} := (T_1 \circ T_1 \circ T_0)^{-1}(\mathcal{G}_0 \cap X_{14})$ a "250-point three-step preimage", conflating the cardinality of the two-sheet target $\mathcal{G}_0 \cap X_{14}$ ($250$ points) with the cardinality of its inverse image under $T_1 \circ T_1 \circ T_0$.
- **Exact correction and proof:**
  Under the driver prefix $\theta_0\theta_1\theta_2 = 011$, the trace maps $f_0 = (0,4,0,4,4)$ and $f_1 = (2,1,1,3,1)$ give:

  | Initial trace $z_0$ | $z_1 = f_0(z_0)$ | $z_2 = f_1(z_1)$ | $z_3 = f_1(z_2)$ | Selected 3-step word on $X_{z_0}$ |
  | :---: | :---: | :---: | :---: | :---: |
  | $0$ | $0$ | $2$ | $1$ | $g_4 \circ g_2 \circ g_0$ |
  | $1$ | $4$ | $1$ | $1$ | $g_3 \circ g_1 \circ g_1 = g_3$ |
  | $2$ | $0$ | $2$ | $1$ | $g_4 \circ g_2 \circ g_2 = g_4$ |
  | $3$ | $4$ | $1$ | $1$ | $g_3 \circ g_1 \circ g_3$ |
  | $4$ | $4$ | $1$ | $1$ | $g_3 \circ g_1 \circ g_4$ |

  On each fixed initial trace sheet $X_{z_0} = \{x \in \mathbb{F}_5^6 : z(x) = z_0\}$ ($|X_{z_0}| = 3125$), $T_1 \circ T_1 \circ T_0|_{X_{z_0}}$ is a fixed composition of three affine bijections and maps $X_{z_0}$ bijectively onto the single trace sheet $X_1 = \{x \in \mathbb{F}_5^6 : z(x) = 1\}$. Consequently:
  1. $T_1 \circ T_1 \circ T_0: \mathbb{F}_5^6 \to X_1$ is globally **$5$-to-$1$ onto $X_1$**, and no checkpoint with $z_3 = 4$ is reachable at $n = 3$.
  2. Of the $250$ checkpoints in $\mathcal{G}_0 \cap X_{14}$, only the **$125$-point sheet $\mathcal{G}_0 \cap X_1$** ($z_3 = 1, B_3 = 3A_3, D_3 = 3C_3$) is reachable at $n = 3$; the $z_3 = 4$ sheet $\mathcal{G}_0 \cap X_4$ ($125$ points) has empty three-step preimage.
  3. Each of the $125$ points in $\mathcal{G}_0 \cap X_1$ has exactly one preimage on each of the five initial trace sheets $X_0, X_1, X_2, X_3, X_4$, so
     $$|\mathcal{P}_{\mathrm{gate}}| = \bigl|(T_1 \circ T_1 \circ T_0)^{-1}(\mathcal{G}_0 \cap X_{14})\bigr| = \bigl|(T_1 \circ T_1 \circ T_0)^{-1}(\mathcal{G}_0 \cap X_1)\bigr| = 5 \times 125 = 625.$$

---

### R2 — Prefix affine tuples of $E_{\mathrm{alt}}(\lambda,\mu)$ at $n=1$ and $n=3$ (`PROOF.md` lines 119–120)

- **Flawed statement in `e3d35709a86b42c21c1bf57e2be2b3a3cf707598`:**
  Printed $(z,A,B,C,D,q,r) = (0, 4\mu, 4, 3, 2+2\lambda+3\mu, 2+2\lambda+4\mu, 2+3\lambda+2\mu)$ at $n=1$ and $(1, 4\mu, 0, 2, 0, 3+2\lambda, 3+3\lambda+\mu)$ at $n=3$. At $\lambda=\mu=0$, the printed $n=1$ tuple $(0,0,4,3,2,2,2)$ had $A+B+q+r = 3 \ne 0 = z_1$.
- **Exact correction and proof:**
  From $x_0^{\mathrm{alt}}(\lambda,\mu) = (3\mu, 3, 3\mu, 2, 4+3\lambda+\mu, 3+2\lambda+3\mu)$ with $(z_0,A_0,B_0,C_0,D_0,q_0,r_0) = (2, \mu, 0, 3, 0, 4+3\lambda+\mu, 3+2\lambda+3\mu)$:
  - At $n=1$, $z_0 = 2, \theta_0 = 0$ select $g_2(a,b,c,d,q,r) = (2-c, 1-d+r, 2-a, 1-b-r, 1-q, -r)$, yielding the raw checkpoint
    $$x_1^{\mathrm{alt}}(\lambda,\mu) = \bigl(2-3\mu,\, 2+2\lambda+3\mu,\, 2-3\mu,\, 3\lambda+2\mu,\, 2+2\lambda+4\mu,\, 2+3\lambda+2\mu\bigr)$$
    and the exact affine tuple
    $$(z_1, A_1, B_1, C_1, D_1, q_1, r_1) = \bigl(0,\, 4-\mu,\, 2,\, 3,\, 1+4\lambda+\mu,\, 2+2\lambda+4\mu,\, 2+3\lambda+2\mu\bigr),$$
    where $A_1 = (2-3\mu)+(2-3\mu) = 4-6\mu \equiv 4-\mu$, $B_1 = (2+2\lambda+3\mu)+(3\lambda+2\mu) = 2+5\lambda+5\mu \equiv 2$, $C_1 = 0-2 \equiv 3$, $D_1 = (2+2\lambda+3\mu)-(3\lambda+2\mu)-1 = 1-\lambda+\mu \equiv 1+4\lambda+\mu$, and $z_1 = (4-\mu)+2+(2+2\lambda+4\mu)+(2+3\lambda+2\mu) = 10+5\lambda+5\mu \equiv 0 \pmod 5$. Its gate coordinates are $s_h = B_1+2A_1 = 2+2(4-\mu) = 10-2\mu \equiv 3\mu$, $d_h = D_1+2C_1 = (1+4\lambda+\mu)+6 \equiv 2-\lambda+\mu$, and $h(x_1^{\mathrm{alt}}) = (1+2\lambda+2\mu, 4+3\lambda+\mu)$ (unchanged).
  - At $n=3$, $x_2^{\mathrm{alt}} = g_2(x_1^{\mathrm{alt}}) = x_0^{\mathrm{alt}}$ has $z_2 = 2, \theta_2 = 1$, selecting $g_4(a,b,c,d,q,r) = (2-a, 1-b, 3-c, 4-d, 2-q, 1-r)$, yielding the raw checkpoint
    $$x_3^{\mathrm{alt}}(\lambda,\mu) = \bigl(2-3\mu,\, 3,\, 3-3\mu,\, 2,\, 3+2\lambda+4\mu,\, 3+3\lambda+2\mu\bigr)$$
    and the exact affine tuple
    $$(z_3, A_3, B_3, C_3, D_3, q_3, r_3) = \bigl(1,\, 4\mu,\, 0,\, 2,\, 0,\, 3+2\lambda+4\mu,\, 3+3\lambda+2\mu\bigr),$$
    with $s_h = 3\mu$, $d_h = 4$, and $h(x_3^{\mathrm{alt}}) = (2+4\mu, 3+4\mu)$ (unchanged).

---

### R3 — Conjugated field operator $\widetilde{A}_f = W A_f W$ (`PROOF.md` line 190)

- **Flawed statement in `e3d35709a86b42c21c1bf57e2be2b3a3cf707598`:**
  Printed the top-right $2 \times 2$ block of $\widetilde{A}_f = W A_f W$ as $\begin{pmatrix}0&1\\1&0\end{pmatrix}$, which maps $e_2 = (0,0,1,0)^T$ to $(0,1,-2,1)^T$.
- **Exact correction and proof:**
  Because $A_f = \begin{pmatrix} I_2 & I_2 \\ M_{21} & M_{22} \end{pmatrix}$ has top-right block $I_2 = \begin{pmatrix}1&0\\0&1\end{pmatrix}$ and $W = \mathrm{diag}(J_2, J_2)$ with $J_2 = \begin{pmatrix}0&1\\1&0\end{pmatrix}$, the top-right block of $W A_f W$ is $J_2 I_2 J_2 = I_2 = \begin{pmatrix}1&0\\0&1\end{pmatrix}$:
  $$\widetilde{A}_f = W A_f W = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ -3 & 1 & -2 & 1 \\ 1 & -2 & 1 & -1 \end{pmatrix},$$
  mapping $e_2 = (0,0,1,0)^T$ to $W A_f (0,0,0,1)^T = W(0,1,1,-2)^T = (1,0,-2,1)^T$.

---

### R4 — Distinction between piston kernel $K$, shell residues $G_L$, and protected vector $V(x)$ (`PROOF.md` lines 25, 222, 234; `RESULT.md` line 32)

- **Flawed statements in `e3d35709a86b42c21c1bf57e2be2b3a3cf707598`:**
  1. Wrote $\ker(h) = L\mathbb{Z}^4 \bmod 5$, conflating the domain of $h$ on checkpoints/pistons with the active field residue space $L\mathbb{Z}^4 \bmod 5$.
  2. In `PROOF.md` Table D4.1 line 222 (Integer Field Chain column), wrote $y \in L\mathbb{Z}^4 \iff h(y \bmod 5) = (0,0)$, omitting $W$.
  3. In `PROOF.md` line 234 and `RESULT.md` line 32, described the $25$ protected vectors $V(x) = (A, 3A, zC, 3zC)$ as mapped by $W$ onto $\ker(h) = L\mathbb{Z}^4 \bmod 5$, conflating the $(A, zC)$-parametrized protected vector $V(x)$ with the $(A, C)$-parametrized piston residue $W(\pi_P(x))$.
- **Exact correction and proof:**
  Let $\pi_P: \mathbb{F}_5^6 \to \mathbb{F}_5^4$ be the piston projection $\pi_P(a,b,c,d,q,r) = (a,b,c,d)$, and define
  $$h_P(a,b,c,d) = (b+2a,\, d+2c) \in \mathbb{F}_5^2, \qquad h = h_P \circ \pi_P: \mathbb{F}_5^6 \to \mathbb{F}_5^2,$$
  $$K := \ker(h_P) = \bigl\{(a, 3a, c, 3c) : (a,c) \in \mathbb{F}_5^2\bigr\} \subset \mathbb{F}_5^4, \qquad \mathcal{G}_0 := \ker(h) = \pi_P^{-1}(K) \subset \mathbb{F}_5^6,$$
  $$G_L := L\mathbb{Z}^4 \bmod 5 = \bigl\{(y_0,y_1,y_2,y_3) \in \mathbb{F}_5^4 : y_0+2y_1 = 0,\, y_2+2y_3 = 0\bigr\} = \bigl\{(3y_1, y_1, 3y_3, y_3) : (y_1,y_3) \in \mathbb{F}_5^2\bigr\} \subset \mathbb{F}_5^4.$$
  1. In the fixed marking, $K \ne G_L$: $(1,3,0,0) \in K \setminus G_L$ ($1 + 2(3) \equiv 2 \ne 0$), and for $y = (0,0,-2,1)^T = L u_\star \in L\mathbb{Z}^4$, $y \bmod 5 = (0,0,3,1) \in G_L \setminus K$ has $h_P(y \bmod 5) = (0,2) \ne (0,0)$.
  2. The comparison map $W(a,b,c,d) = (b,a,d,c)$ restricts to a bijection $W: K \to G_L$, so:
     - for a checkpoint $x \in \mathbb{F}_5^6$: $h(x) = (0,0) \iff \pi_P(x) \in K \iff W(\pi_P(x)) \in G_L$;
     - for an integer field vector $y \in \mathbb{Z}^4$: $y \in L\mathbb{Z}^4 \iff (y \bmod 5) \in G_L \iff h_P(W(y \bmod 5)) = (0,0)$.
  3. On $\mathcal{G}_0 \cap X_{14}$, the piston residue $W(\pi_P(x)) = \bigl(3(3A+3C+1), 3(A+C+2), 3(3A-3C-1), 3(A-C-2)\bigr) \in G_L$ is a bijection of $(A,C) \in \mathbb{F}_5^2$ onto $G_L$, whereas the protected vector $V(x) = (A, 3A, zC, 3zC)$ is a bijection of $(A, zC) \in \mathbb{F}_5^2$ onto $K$. Across the two trace sheets $z \in \{1,4\}$, $W(\pi_P(x))$ is not a function of $V(x)$ alone when $C \ne 0$: for $x = (4,2,1,3,0,1)$ ($z=1, A=0, C=1$) and $x' = (3,4,2,1,0,4)$ ($z=4, A=0, C=4$), both lie in $\mathcal{G}_0 \cap X_{14}$ with $V(x) = V(x') = (0,0,1,3)$, but $W(\pi_P(x)) = (2,4,3,1) \ne (4,3,1,2) = W(\pi_P(x'))$.

---

### R5 — One-shot $h(x_\lambda(n))$ summary at $n=0$ vs $n \ge 1$ (`PROOF.md` line 222; `RESULT.md` line 23)

- **Flawed statement in `e3d35709a86b42c21c1bf57e2be2b3a3cf707598`:**
  Summarized $h(x_\lambda(n)) = (\pm\lambda, \mp\lambda)$ "for all $n \ge 0$", whereas at $n=0$, $x_\lambda(0) = (\lambda, 0, -\lambda, 0, 0, 0)$ has $h(x_\lambda(0)) = (2\lambda, -2\lambda) = (2\lambda, 3\lambda)$ (at $\lambda=1$, $(2,3) \notin \{(1,4),(4,1)\}$).
- **Exact correction:**
  At $n = 0$, $h(x_\lambda(0)) = (2\lambda, 3\lambda) \pmod 5$; for all $n \ge 1$ (and on the 100-state ready carrier graph $Q$), $h(x_\lambda(n)) = (\pm\lambda, \mp\lambda) \pmod 5$ (specifically $(-2Bz\lambda, 2Bz\lambda)$ on $Q$). Because $2$ and $\pm 1$ are units in $\mathbb{F}_5$, $h(x_\lambda(n)) = (0,0) \iff \lambda = 0$ holds at $n = 0$, for all $n \ge 1$, and on all $100$ states of $Q$.

---

### R6 — Explicit record of refuted literal clause `h_1 = B + 2A` in `CONTRACT.md` line 107 (`RESULT.md` line 37)

- **Flawed statement in `CONTRACT.md` line 107 and `RESULT.md` line 37:**
  `CONTRACT.md` line 107 wrote parenthetically `h_1 = B+2A`, and `RESULT.md` line 37 reported "Fired falsifiers: None."
- **Exact correction:**
  The literal equation $h_1(x) = B + 2A$ is **REFUTED** on $\mathbb{F}_5^6$: at $E(0,0) = (4,3,2,2,0,1)$, $h_1(E(0,0)) = 3 + 2(4) \equiv 1 \pmod 5$, whereas $B + 2A = 0 + 2(1) = 2 \pmod 5$. The true affine formulas (derived in `PROOF.md` lines 36–40) are
  $$h_1(x) = 3\bigl((B+2A) + (D+2C)\bigr), \quad h_2(x) = 3\bigl((B+2A) - (D+2C)\bigr), \quad s_h(x) := h_1(x) + h_2(x) = B + 2A \pmod 5.$$
  Thus $B + 2A$ is the **gate sum** $s_h = h_1 + h_2$, not $h_1$. Because $h(x) = (0,0) \implies s_h(x) = B+2A = 0$, the nonvanishing $s_h(x) = B+2A \in \{2,3\} \ne 0$ on $E(\lambda,\mu)$ still establishes the `#1548` gate-sum obstruction $h(x) \ne (0,0)$.

---

### R7 — Fixed-time and full-context qualifiers in summary Table D4.1 (`PROOF.md` lines 223, 225)

- **Flawed statements in `e3d35709a86b42c21c1bf57e2be2b3a3cf707598`:**
  1. In Table D4.1 line 223 ("Retained message in $h(x)$ on $X_{14}$"), stated "$5$ classes" without specifying that this holds at **fixed common time $n \ge 3$ (or fixed carrier context $(A,z)$, $(C,z)$, $(B,z)$)** rather than as a stationary time-blind function on $X_{14}$.
  2. In Table D4.1 line 225 (Rational Contact $H_B$ column), summarized receiver trajectory equality as holding "when $(q_0,r_0)$ and $Y_0$ are common", omitting the required hypotheses of **common initial trace $z_0$** (or identical $(q_n, r_n)$ histories for all $n \ge 0$) and a **common source-independent schedule $\mathcal{S}$**.
- **Exact corrections and witnesses:**
  1. On $X_{14}$, the $5$-class partition of messages by $h(x)$ holds at fixed common time $n \ge 3$ (or fixed $(A,z)$ / $(C,z)$ / $(B,z)$). Across different carrier states on $X_{14}$, stationary $h(x)$ collides between distinct message classes:
     - on the one-shot ready graph $Q$, $h = (-2Bz\lambda, 2Bz\lambda)$ gives $h = (1,4)$ for both $(B,z,\lambda) = (2,1,1)$ and $(3,1,4)$;
     - on the $E_{\mathrm{alt}}$ tail, $h = (C(2z\mu+1), C(2z\mu-1))$ gives $h = (1,2)$ for both $(C,z,\mu) = (2,1,1)$ and $(2,4,4)$;
     - on the $E$ tail, $h = (A(1+z(\lambda+3\mu)), A(1-z(\lambda+3\mu)))$ gives $h = (2,0)$ for both $(A,z,\lambda+3\mu) = (1,1,1)$ and $(1,4,4)$.
  2. For general preparations, equality of the complete rational receiver trajectory $Y_t$ under Theorem D3.1 requires common $(z_0, q_0, r_0)$ (or identical $(q_n, r_n)$ for all $n \ge 0$), common initial complete receiver state $Y_0 \in \mathcal{R}$, and a common source-independent schedule $\mathcal{S}$. Common $(q_0, r_0)$ and $Y_0$ alone do not suffice when $z_0$ differs: $x_\lambda(0)$ ($z_0=0, q_0=r_0=0$) and $x_{\mathrm{empty}}(0)$ ($z_0=1, q_0=r_0=0$) share $(q_0,r_0)=(0,0)$, but at $n=2$ have $(q_2,r_2) = (1,0)$ vs $(0,0)$, yielding contact vectors $\eta = (1/2, 1/2, 0, 0)$ (energy cost $3/20$) vs $\eta = (0, 1/2, 0, 0)$ (energy cost $1/10$), both of which accept on a common blank receiver ($\sigma=+1, e=B=1$) and write different waves.
