# Result: C-V103-SOURCE-INTERFACE-N

**Status:** NON-CANONICAL / conditional candidate-T (analytical L1)  
**Program:** [#1548](https://github.com/mathorn1973/twist-j/issues/1548) (Lane D)  
**Child issue:** [#1551](https://github.com/mathorn1973/twist-j/issues/1551)  
**Public session:** `Antigravity-20261016-v103-source-interface`  
**Author:** A. M. Thorn  
**License:** Apache-2.0  
**Specification pin:** `9cb2b7d89eb1fc955fb67e886e46a379cb1aba43`  
**Scientific code:** `NONE / NOT_RUN`  
**Independent review:** `PENDING` (`C-V103-SOURCE-INTERFACE-REVIEW-N`, Lane RD)  
**Promotion:** `DO NOT PROMOTE`

## Summary of Conclusions (Questions Q1–Q4)

1. **Q1 — Complete six-stage interface table and family readiness/absence classification (`PROOF.md` Section 1, Theorem D1):**
   - Established the complete typing, domain, codomain, and kernel/image table connecting: (1) raw checkpoints $x=(a,b,c,d,q,r) \in \mathbb{F}_5^6$ and affine coordinates $(z,A,B,C,D,q)$; (2) $W$-piston residues $W(a,b,c,d)=(b,a,d,c)$ and the shell-gate map $h(x) = (b+2a, d+2c) \in \mathbb{F}_5^2$, with exact sum/difference coordinates $s_h = h_1+h_2 = B+2A$ and $d_h = h_1-h_2 = D+2C$; (3) the balanced integer lift $\ell: \mathbb{F}_5 \to \{-2,-1,0,1,2\}$; (4) the index-$5$ raw integer field split $P y + S_{\mathrm{st}}\sigma \subset \mathbb{Z}^6$ and index-$25$ active shell sublattice $L\mathbb{Z}^4 \subset \mathbb{Z}^4$; (5) the injective 25-point rational contact map $(q,r) \mapsto a(q,r) = S\eta(q,r) \in \mathbb{Q}^D$ on the 705-site Dirichlet domain $D$; and (6) the visible receiver readouts of $E(\lambda,\mu)$, $E_{\mathrm{alt}}(\lambda,\mu)$, and $x_\lambda(0)$ / $x_{\mathrm{empty}}(0)$.
   - Distinguished common raw reset ($R_0 = R_2 = (2,0)$ under $\Phi$ on $E(\lambda,\mu)$) from common semantic `BLANK` decoding with message-dependent raw blank values ($(0,\mu)$ for the quadratic reader on $E(\lambda,\mu)$ and $(\mu,0)$ for the affine reader on $E_{\mathrm{alt}}(\lambda,\mu)$), and distinguished occupied zero `PRESENT(0)` ($\lambda=0$ or $\mu=0$) from the explicitly declared sixth absence codeword $x_{\mathrm{empty}}(0) = (0,0,1,0,0,0)$ in `U-NATIVE-SOURCE-RECEIVER-RECORD`.

2. **Q2 — Exact gate overlap and retained message distinctions (`PROOF.md` Section 2, Lemma D2.1 and Theorem D2):**
   - **Original 550-point family $E(\lambda,\mu)$:** Across all $25$ pairs $(\lambda,\mu) \in \mathbb{F}_5^2$, the necessary gate sum is $s_h(x) = B + 2A = 2$ at $n=0,2$, $s_h(x_1) = 3$ at $n=1$, and $s_h(x) = 2A \in \{2,3\}$ on all $500$ synchronized tail points ($n \ge 3$). Hence **zero of the 550 support points** (and zero trajectory points at any $n \ge 0$) lie in the zero gate $\mathcal{G}_0 = \{h = (0,0)\}$. At every fixed $n \ge 0$, $h(x_n(\lambda,\mu))$ retains only the $5$-class linear combination $2\lambda + \mu \pmod 5$.
   - **Alternative 150-point family $E_{\mathrm{alt}}(\lambda,\mu)$:** At $n=0,2$ ($25$ blank points) and on the entire $100$-point synchronized tail ($n \ge 3$), the gate difference is $d_h(x) = D + 2C = 2C \in \{1,4\} \ne 0$, so **$0/25$ blank points and $0/100$ tail points** lie in $\mathcal{G}_0$ (even at $\mu = 0$, where $s_h = B+2A = 2\mu = 0$ vanishes). At $n=1$, $(\lambda,\mu) \mapsto h(x_1^{\mathrm{alt}}(\lambda,\mu)) = (1+2\lambda+2\mu, 4+3\lambda+\mu)$ is a bijection $\mathbb{F}_5^2 \to \mathbb{F}_5^2$, hitting $\mathcal{G}_0$ at **exactly $1/25$ pairs**, $(\lambda,\mu) = (2,0)$ ($x_1^{\mathrm{alt}}(2,0) = (2,1,2,1,1,3)$, $z_1 = 0, r_1 = 3$), which exits $\mathcal{G}_0$ at $n=2$.
   - **Registered one-shot family $x_\lambda(0)$ and absence $x_{\mathrm{empty}}(0)$:** For every $\lambda \in \mathbb{F}_5$, $s_h = B+2A = 0$ holds for all $n \ge 0$ and on all $100$ states of the ready carrier graph $Q$, while $h(x_\lambda(n)) = (\pm\lambda, \mp\lambda)$ (and $h = (-2Bz\lambda, 2Bz\lambda)$ on $Q$). Thus $h(x_\lambda(n)) = (0,0) \iff \lambda = 0$ ($20/100$ ready-carrier states, $1/5$ occupied payloads, with $W(x_0(3)_{0..3}) = (0,0,3,1) = \bar{y}_3$). The absence codeword $x_{\mathrm{empty}}(0) = (0,0,1,0,0,0)$ has $s_h(x_{\mathrm{empty}}(n)) = 2(-1)^n \in \{2,3\} \ne 0$ and $h(x_{\mathrm{empty}}(n)) \in \{(0,2),(0,3),(2,0),(3,0)\} \not\ni (0,0)$ for all $n \ge 0$.

3. **Q3 — Scoped source-blindness composition and $W$ relabeling vs fixed-marking action (`PROOF.md` Section 3, Theorems D3.1 and D3.2):**
   - **Source-blindness composition:** Because $E(\lambda,\mu)$ has $(\lambda,\mu)$-independent initial quotient $(z_0, q_0, r_0) = (2,0,1)$, its reference trajectory $(q_n, r_n)$ and contact source $a(q_n, r_n) = S\eta(q_n, r_n)$ are identical for all $25$ pairs $(\lambda,\mu) \in \mathbb{F}_5^2$ at every $n \ge 0$. Acting on any common initial complete receiver state $Y_0 \in \mathcal{R}$ under any source-independent schedule of $F_{\mathrm{wave}}$, $F_{\mathrm{wave}}^{-1}$, and $H_B^{(q_{n_t}, r_{n_t})}$, the complete receiver trajectory $Y_t(\lambda,\mu) = Y_t(0,0)$ is strictly independent of $(\lambda,\mu)$. The same $(q,r)$-port blindness holds across the five occupied payloads $\lambda \in \mathbb{F}_5$ of $x_\lambda(0)$, whereas $E_{\mathrm{alt}}(\lambda,\mu)$ varies $(q_n, r_n)$ bijectively only because $(\lambda,\mu)$ was preloaded directly into the initial reference registers $(q_0, r_0)$.
   - **$W$ relabeling vs fixed-marking action:** Passive relabeling $\tilde{y} = W y$ transforms $B_f \mapsto W^T B_f W$, $A_f \mapsto W A_f W$, and $L \mapsto W L W$ simultaneously. In the fixed canonical marking $H(y) = \frac{1}{2}y^T B_f y$, $W$ is not an $H$-isometry:
     $$H(W y) - H(y) = y_0^2 - y_1^2 + y_0 y_2 - y_1 y_3,$$
     with $H(e_0) = 2 \ne 3 = H(W e_0)$ and $H(u_\star) = 1 \ne 2 = H(W u_\star)$ for $u_\star = (0,-1,-1,2)^T$.

4. **Q4 — Smallest unresolved interface obligation (`PROOF.md` Section 4, Table D4.1 and Theorem D4.2):**
   - The synchronized zero-gate sheet $\mathcal{G}_0 \cap X_{14}$ is characterized by $B = 3A$ and $D = 3C$ ($250$ checkpoints, $25$ protected vectors $V(x) = (A, 3A, zC, 3zC)$ bijection-mapped via $W$ onto the $25$ residues of $\ker(h) = L\mathbb{Z}^4 \bmod 5$). None of the three v102 families populates more than one message inside $\mathcal{G}_0 \cap X_{14}$ ($0$ for $E$, $0$ for $E_{\mathrm{alt}}$, and only $\lambda=0$ for $x_\lambda$).
   - The smallest unresolved interface obligation is to determine whether the $250$-point three-step preimage $\mathcal{P}_{\mathrm{gate}} = (T_1 \circ T_1 \circ T_0)^{-1}(\mathcal{G}_0 \cap X_{14})$ contains an origin-zero preparation family with a common initial receiver projection $R_{\mathrm{init}}$ that reaches at least two distinct protected sign fibres $\{V(x_3), -V(x_3)\}$ in $\mathcal{G}_0 \cap X_{14}$.

## Fired Falsifiers and Scope Boundaries

- **Fired falsifiers:** None. All exposed hypotheses in `#1548` Lane D hold at their exact proved scopes.
- **Boundaries:** No new generator, selector, matrix, contact law, physical selection principle, or Canon/registry/frontier modification is proposed. The initial specification files (`README.md`, `CONTRACT.md`, `PREREG.md`, `SOURCES.tsv`, `INPUTS.sha256`) are unchanged from `9cb2b7d89eb1fc955fb67e886e46a379cb1aba43`.
