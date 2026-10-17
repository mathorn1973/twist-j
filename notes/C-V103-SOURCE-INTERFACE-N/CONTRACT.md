# Frozen Analytical Contract: C-V103-SOURCE-INTERFACE-N

**NON-CANONICAL / L1 / no normative authority.**  
A. M. Thorn, 2026-10-16. Original work Apache-2.0.  
Candidate `C-V103-SOURCE-INTERFACE-N`, program [#1548](https://github.com/mathorn1973/twist-j/issues/1548) (Lane D), child issue [#1551](https://github.com/mathorn1973/twist-j/issues/1551).  
Public session: `Antigravity-20261016-v103-source-interface`.

## 1. Exact inherited canonical objects

All mathematical objects are inherited without modification from Public Canon v102 at `main` = peeled `canon-v102` = `a632c6a162dc87e60104d7a478e7650a6d5c4a1b` (content commit `b04e22dd3ed8e4240cff347364f24670d4183a4d`), as pinned in `SOURCES.tsv` and `INPUTS.sha256`.

### 1.1 Native checkpoint dynamics and affine chart

A native checkpoint is
$$x = (p_1, p_4, p_1', p_4', q, r) = (a, b, c, d, q, r) \in \mathbb{F}_5^6,$$
with trace $z = a+b+c+d+q+r \in \mathbb{F}_5$, Thue-Morse bit $\theta_n = \operatorname{popcount}(n) \bmod 2$ for integer $n \ge 0$, and native step
$$x_{n+1} = T_{\theta_n}(x_n) = g_{z(x_n) + 2\theta_n}(x_n),$$
where the five generators $(g_0, g_1, g_2, g_3, g_4) = (\mathrm{a}, \mathrm{b}, \mathrm{c}, \mathrm{d}, \mathrm{e})$ are the affine involutions on $\mathbb{F}_5^6$:
$$\begin{aligned}
g_0(a,b,c,d,q,r) &= (b, a, d, c, q, r), \\
g_1(a,b,c,d,q,r) &= (-c, -d, -a, -b, -q, -r), \\
g_2(a,b,c,d,q,r) &= (2-c, 1-d+r, 2-a, 1-b-r, 1-q, -r), \\
g_3(a,b,c,d,q,r) &= (2-a, 1-b, 3-c, 4-d, 1-q, 1-r), \\
g_4(a,b,c,d,q,r) &= (2-a, 1-b, 3-c, 4-d, 2-q, 1-r).
\end{aligned}$$
The trace quotient maps $f_\theta(z) = z(T_\theta(x))$ for $z = (0,1,2,3,4)$ are
$$f_0 = (0, 4, 0, 4, 4), \qquad f_1 = (2, 1, 1, 3, 1).$$
The quotient $(z, q, r) \in \mathbb{F}_5^3$ evolves autonomously under the selected restriction of $(z,q,r)$, $(-z,-q,-r)$, $(2-z,1-q,-r)$, $(2-z,1-q,1-r)$, and $(3-z,2-q,1-r)$.

The canonical affine coordinates on $(a,b,c,d)$ are
$$A = a+c, \qquad B = b+d, \qquad C = a-c-2, \qquad D = b-d-1,$$
with inverse on $\mathbb{F}_5^6$:
$$a = 3(A+C+2), \quad c = 3(A-C-2), \quad b = 3(B+D+1), \quad d = 3(B-D-1), \quad r = z-A-B-q.$$
On the absorbing sheet $X_{14} = \{x \in \mathbb{F}_5^6 : z(x) \in \{1,4\}\}$, the selected generators are $g_1$ (when $z+2\theta \equiv 1 \pmod 5$) and $g_3$ or $g_4$ (when $z+2\theta \equiv 3 \text{ or } 4 \pmod 5$), acting on $(z,A,B,C,D)$ by
$$g_1: (z,A,B,C,D) \mapsto (-z,-A,-B,C,D), \qquad \text{selected } g_3, g_4: (z,A,B,C,D) \mapsto (z,-A,-B,-C,-D),$$
preserving the sign fibre of the protected vector $V(x) = (A, B, zC, zD)$.

### 1.2 Three inherited native preparation families at origin counter $n=0$

1. **Original 550-point two-message family (`U-ORIGIN-NONLINEAR-TWO-MESSAGE-READOUT`, `U-FIXED-FAMILY-READOUT-COMPLEXITY`):**
   For $(\lambda, \mu) \in \mathbb{F}_5^2$,
   $$E(\lambda, \mu) = \bigl(3(\lambda+3),\, 3(\mu+1),\, 3(-\lambda-1),\, 3(-\mu-1),\, 0,\, 1\bigr) \in \mathbb{F}_5^6,$$
   with initial affine coordinates $(z, A, B, C, D, q, r) = (2, 1, 0, \lambda, \mu, 0, 1)$.
   - Under `U-ORIGIN-NONLINEAR-TWO-MESSAGE-READOUT`, the global bijective chart $\Phi: \mathbb{F}_5^6 \to \mathbb{F}_5^2 \times \mathbb{F}_5^4$ has observation $R(x) = (z, T(x))$ with $T(x) = e_0(z)C + e_2(z)q + (e_1(z)+e_4(z))(zA^3+1-A^4)D + e_3(z)D$ (reduced degree $9$), common raw initial/reset value $R_0 = R_2 = (2,0)$, exact $x_2 = x_0$, and decoded output $\mathrm{BLANK}$ on $z \in \{2,3\}$ and $\mathrm{PRESENT}(T)$ on $z \in \{0,1,4\}$.
   - Under `U-FIXED-FAMILY-READOUT-COMPLEXITY`, on the same 550-point required support $S$, the least affine observation dimension is $3$, realized by $(f_1, f_2, f_3) = (2b+d, 3a+q, 2a+3b+r)$, and the least maximum polynomial degree for two observation coordinates is $2$, realized by $(P, Q) = (A+2z, (1+2B)D + 3BC)$ with $\delta(P,Q) = \mathrm{BLANK}$ if $P=0$, else $\mathrm{PRESENT}(-P^2 Q)$ (whose raw blank $(0,\mu)$ varies with $\mu$).
   - No separate seventh absence codeword is declared for $E(\lambda,\mu)$: the prescribed six semantic outputs are $\mathrm{BLANK}$ and $\mathrm{PRESENT}(k)$ for $k \in \mathbb{F}_5$, with $\mathrm{PRESENT}(0)$ distinct from $\mathrm{BLANK}$.

2. **Alternative 150-point two-message family (`U-ALTERNATIVE-AFFINE-SEMANTIC-READOUT`):**
   For $(\lambda, \mu) \in \mathbb{F}_5^2$, with $r_0 = 3(1+\mu-\lambda) \in \mathbb{F}_5$,
   $$E_{\mathrm{alt}}(\lambda, \mu) = \bigl(3\mu,\, 3,\, 3\mu,\, 2,\, 2-\mu-r_0,\, r_0\bigr) \in \mathbb{F}_5^6,$$
   with initial affine coordinates $(z, A, B, C, D, q, r) = (2, \mu, 0, 3, 0, 2-\mu-r_0, r_0)$.
   - Its affine rank-two observation is $(X, H) = (A+D, C+z)$ with fixed nonlinear decoder $\delta(X,H) = \mathrm{BLANK}$ if $H=0$, else $\mathrm{PRESENT}(H^2 X)$.
   - It satisfies $x_2 = x_0$, has raw ready/reset value $(X_0, H_0) = (X_2, H_2) = (\mu, 0)$ (depending on $\mu$, with common semantic output $\mathrm{BLANK}$), and has a 150-point required support across the 25 pairs.
   - As in the 550-point family, $\mathrm{PRESENT}(0)$ is an occupied message value ($\lambda=0$ or $\mu=0$), distinct from $\mathrm{BLANK}$, with no separate seventh absence preparation declared.

3. **Registered one-shot source family and explicit absence preparation (`U-NATIVE-SOURCE-RECEIVER-RECORD`):**
   With source $S_{\mathrm{reg}} = (p_1, p_1') = (a,c)$, memory $M_{\mathrm{reg}} = (p_4, p_4') = (b,d)$, reference $C_{\mathrm{reg}} = (q,r)$, and complementary receiver $R_{\mathrm{reg}} = (u, v, q, r) = (b, d, q, r) \in \mathbb{F}_5^4$:
   - For each occupied payload $\lambda \in \mathbb{F}_5$,
     $$x_\lambda(0) = (\lambda, 0, -\lambda, 0, 0, 0) \in \mathbb{F}_5^6.$$
   - For declared absence, the distinct sixth source codeword is
     $$x_{\mathrm{empty}}(0) = (0, 0, 1, 0, 0, 0) \in \mathbb{F}_5^6.$$
   - The total finite receiver reader on $R_{\mathrm{reg}} = (u,v,q,r)$ sets $B = u+v$, $D = u-v-1$, $\hat{z} = 3B+q+r$, $\operatorname{ready}(R_{\mathrm{reg}}) = 1 \iff B \in \{2,3\} \text{ and } \hat{z} \in \{1,4\}$, and
     $$\operatorname{read}(R_{\mathrm{reg}}) = \begin{cases} \mathrm{BLANK}, & \operatorname{ready}(R_{\mathrm{reg}}) = 0, \\ \mathrm{PRESENT}(3 - B\hat{z}D), & \operatorname{ready}(R_{\mathrm{reg}}) = 1. \end{cases}$$

### 1.3 Piston-to-field comparison map, raw field split, and shell gate

In `FIELD-CONSERVATIVE-CHAIN-LAW`, `FIELD-CHAIN-FIRST-WORK`, and `FIELD-LOCAL-WORK-RECORD` (Shared proofs 1–8):
- Each cell stores raw field $z_{\mathrm{raw}} = (E, M) \in \mathbb{Z}^4 \times \mathbb{Z}^2$ with active embedding $P(y_0,y_1,y_2,y_3) = (y_0-y_1, -y_0, y_1, y_1, y_2, y_3)$ and static embedding $S_{\mathrm{st}}(u,v) = (u, u, v, u-v, 0, 0)$. The direct sum $P\mathbb{Z}^4 \oplus S_{\mathrm{st}}\mathbb{Z}^2$ has index $5$ in $\mathbb{Z}^6$, characterized by $2E_0 - 3E_1 + E_2 + E_3 \equiv 0 \pmod 5$.
- On the active field carrier $\mathbb{Z}^4$, the shear step $A_f$, quadratic form $H(y) = \frac{1}{2} y^T B_f y$, and shell operator $L = (I - A_f)(I - A_f^2)$ are
  $$A_f = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ -2 & 1 & -1 & 1 \\ 1 & -3 & 1 & -2 \end{pmatrix}, \quad
  B_f = \begin{pmatrix} 4 & -2 & 2 & -1 \\ -2 & 6 & -1 & 3 \\ 2 & -1 & 2 & 0 \\ -1 & 3 & 0 & 2 \end{pmatrix}, \quad
  L = \begin{pmatrix} 1 & -3 & -1 & -2 \\ -3 & 4 & -2 & 1 \\ 0 & 5 & 1 & 2 \\ 5 & -5 & 2 & -1 \end{pmatrix},$$
  satisfying $A_f^5 = I$, $L^2 = 5 A_f^3$, $V_{\mathrm{inv}} = 5 L^{-1} = A_f^2 L$, $L^T B_f L = 5 B_f$, $H(L w) = 5 H(w)$, $\det L = 25$, and the exact shell-image criterion
  $$y = (y_0, y_1, y_2, y_3) \in L\mathbb{Z}^4 \iff y_0 + 2y_1 \equiv 0 \pmod 5 \text{ and } y_2 + 2y_3 \equiv 0 \pmod 5.$$
- Under the fixed comparison map from `#1548`,
  $$W: \mathbb{F}_5^4 \to \mathbb{F}_5^4, \qquad W(p_1, p_4, p_1', p_4') = (p_4, p_1, p_4', p_1') = (b, a, d, c),$$
  a residue $y \bmod 5 = W(p_1, p_4, p_1', p_4')$ lies in $L\mathbb{Z}^4 \bmod 5$ if and only if the gate residue map
  $$h(x) = (h_1(x), h_2(x)) := (p_4 + 2p_1,\, p_4' + 2p_1') = (b + 2a,\, d + 2c) \in \mathbb{F}_5^2$$
  vanishes: $h(x) = (0,0)$.

### 1.4 Balanced lift and supplied funded rational contact $H_B$

In `SIGNED-PORT-OCCUPIED-REVERSIBILITY` and `FUNDED-CONTACT-INVOLUTION`:
- The balanced representative $\ell: \mathbb{F}_5 \to \{-2, -1, 0, 1, 2\} \subset \mathbb{Z}$ is
  $$\ell(0) = 0, \quad \ell(1) = 1, \quad \ell(2) = 2, \quad \ell(3) = -2, \quad \ell(4) = -1.$$
- On the 705-site finite Dirichlet domain $D = Y + B_\star + B_\star \subset D_3$ with $Y = \{y_0, y_1, y_2, y_3, y_4\}$, $S: \mathbb{Q}^4 \to \mathbb{Q}^D$ sets $(Sz)(y_i) = z_i - s/5$ ($i=0,1,2,3$) and $(Sz)(y_4) = -s/5$ for $s = \sum_{i=0}^3 z_i$, and $0$ outside $Y$.
- Retained reference coordinates $(q, r) \in \mathbb{F}_5^2$ determine the rational contact vector
  $$\eta(q, r) = \left(\frac{\ell(q)}{2},\, \frac{\ell(r)+1}{2},\, 0,\, 0\right) \in \mathbb{Q}^4, \qquad a(q, r) = S\eta(q, r) \in \mathbb{Q}^D.$$
- On occupied wave $(u, v) \in \mathbb{Q}^D \times \mathbb{Q}^D$, four rational tape slots $(A_0, A_1), (B_0, B_1) \in (\mathbb{Q}^4)^2$, pointer $k \in \mathbb{Z}/2\mathbb{Z}$, rational store $e \in [0, B] \cap \mathbb{Q}$ ($B \ge 0$), signed rational ledger $w_{\mathrm{led}} \in \mathbb{Q}$, and direction bit $\sigma \in \{+1, -1\}$, the proposed transition $v \mapsto v + \sigma a(q,r)$ has energy increment
  $$\Delta_\sigma(u, v; q, r) = \sigma \langle v - H_D u / 2,\, a(q,r) \rangle + \frac{1}{2}\|a(q,r)\|^2, \qquad H_D = 2I - L_D,$$
  and $H_B$ accepts if and only if $0 \le e - \Delta_\sigma \le B$, updating $(v, e, w_{\mathrm{led}}, \sigma) \mapsto (v + \sigma a(q,r), e - \Delta_\sigma, w_{\mathrm{led}} + \Delta_\sigma, -\sigma)$ and fixing the full state otherwise.

## 2. Frozen analytical questions

- **Q1 (Complete map/domain/equality table and family readiness/absence classification):**
  Construct the complete map, domain, codomain, and equivalence/equality table across all six interface stages:
  1. raw checkpoint $x = (a,b,c,d,q,r) \in \mathbb{F}_5^6$;
  2. $W$-piston residue $W(a,b,c,d) = (b,a,d,c) \in \mathbb{F}_5^4$ and gate map $h(x) = (b+2a, d+2c) \in \mathbb{F}_5^2$;
  3. balanced integer representative $\ell(W(a,b,c,d)) \in \{-2,-1,0,1,2\}^4 \subset \mathbb{Z}^4$ and general integer coset lifts $y \in \mathbb{Z}^4$;
  4. raw integer field split $z_{\mathrm{raw}} = P y + S_{\mathrm{st}} \sigma \in \mathbb{Z}^6$ and active shell image $L \mathbb{Z}^4 \subset \mathbb{Z}^4$ (with funded reaction $G$ and local pointer $p \in C_5$);
  5. supplied rational contact input $\eta(q,r) \in \mathbb{Q}^4$, $a(q,r) = S\eta(q,r) \in \mathbb{Q}^D$, and $H_B$ on the 705-site carrier;
  6. visible receiver readout under each family's declared contract.
  Explicitly classify common raw reset vs common semantic `BLANK`, and `PRESENT(0)` vs declared absence for $E(\lambda,\mu)$, $E_{\mathrm{alt}}(\lambda,\mu)$, and $x_\lambda(0)$ / $x_{\mathrm{empty}}(0)$.

- **Q2 (Algebraic gate overlap and retained message distinctions):**
  Express $h(x) = (h_1(x), h_2(x))$ exactly in the canonical affine coordinates $(A,B,C,D)$ and derive by parametric calculation and induction the exact values of $h(x_n)$, the zero-gate overlap $h(x_n) = (0,0)$, and the retained message dependence across the prefix $n = 0, 1, 2, 3$ and the synchronized tail $n \ge 3$ for:
  1. $E(\lambda, \mu)$ on all 25 message pairs and its full 550-point support (checking the obstruction $A = p_1+p_1'$, $B = p_4+p_4'$, $h_1 = B+2A$ on the prefix and every tail point);
  2. $E_{\mathrm{alt}}(\lambda, \mu)$ on all 25 message pairs and its full 150-point support;
  3. $x_\lambda(0)$ for all $\lambda \in \mathbb{F}_5$ and $x_{\mathrm{empty}}(0)$ on the prefix and synchronized tail / 100-state ready carrier graph.

- **Q3 (Scoped source-blindness composition and $W$ relabeling vs fixed-marking action):**
  1. Prove or refute the scoped source-blindness composition for $E(\lambda, \mu)$: because $E(\lambda, \mu)$ has initial quotient $(z_0, q_0, r_0) = (2, 0, 1)$ independent of $(\lambda, \mu)$, its common-time $(q_n, r_n)$ trajectory is identical for all 25 pairs $(\lambda, \mu) \in \mathbb{F}_5^2$ at every $n \ge 0$; consequently, the unchanged supplied contact source $a(q_n, r_n) = S\eta(q_n, r_n)$, acting on any initially common complete rational receiver state under any source-independent schedule of wave steps and $H_B$ invocations, produces identical receiver trajectories and work ledgers for all $(\lambda, \mu) \in \mathbb{F}_5^2$. Contrast this exact scope with $E_{\mathrm{alt}}(\lambda, \mu)$ and $x_\lambda(0)$.
  2. Prove the exact distinction between: (a) applying $W$ as a simultaneous coordinate relabeling of $\mathbb{Z}^4$ (which transforms $B_f \mapsto W^T B_f W$, $A_f \mapsto W^{-1} A_f W$, and $L \mapsto W^{-1} L W$), and (b) applying $W$ to a state vector within the fixed canonical quadratic form $H(y) = \frac{1}{2} y^T B_f y$, exhibiting $H(W y) - H(y)$ explicitly and verifying the counterexample $e_0 = (1,0,0,0)^T$, $W e_0 = (0,1,0,0)^T$ with $H(e_0) = 2 \ne 3 = H(W e_0)$.

- **Q4 (Assumption table and smallest unresolved interface obligation):**
  Provide a complete assumption-and-boundary table for the frozen comparison and state a single exact conclusion identifying the smallest unresolved mathematical interface obligation between the native two-message preparations, the $L\mathbb{Z}^4 \bmod 5$ shell gate, and the funded contact port, accompanied by a separately scoped next-experiment description only if justified.

## 3. Pre-exposed hypotheses, falsifiers, and scope boundaries

- The original-family gate obstruction ($A=1, B=0 \implies B+2A \ne 0$ at $n=0,2$), the $(q,r)$ source-blindness statement for $E(\lambda,\mu)$, and the non-isometry witness $H(e_0)=2, H(W e_0)=3$ were exposed in `#1548`. They are treated as exposed hypotheses to be proved or refuted by complete symbolic derivations, not blind discoveries.
- Any algebraic error, false universal claim, conflation of semantic `BLANK` with common raw reset, conflation of `PRESENT(0)` with declared absence, or unproved equivalence between $E$, $E_{\mathrm{alt}}$, and $x_\lambda$ refutes the corresponding clause.
- No new generator, selector, matrix, contact law, physical selection principle, or Canon/registry/frontier edit is authorized. All conclusions remain `NON-CANONICAL` at action layer `L1`.
