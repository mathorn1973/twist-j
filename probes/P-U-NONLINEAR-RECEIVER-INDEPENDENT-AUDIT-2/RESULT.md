# Result: P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-2

Status: PASS (NON-CANONICAL / L1 / Independent Audit)

- **Issue:** [#1534](https://github.com/mathorn1973/twist-j/issues/1534)
- **Primary Lane:** [#1532](https://github.com/mathorn1973/twist-j/issues/1532) / Draft PR [#1533](https://github.com/mathorn1973/twist-j/pull/1533) (`probes/P-U-NONLINEAR-ORIGIN-RECEIVER-1`)
- **Abandoned Predecessor:** `P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-1` (`8edb5ea97bf38337d9c65f08964a0ae9e2ed7743`, closed `Status: ABANDONED` at `d9a20f7bba60ae868aa467b5b076960ac5e88b7d`)
- **Audit Owner:** `Antigravity-20261015-nonlinear-receiver-independent-audit-1`
- **Author:** A. M. Thorn `<thorn@twistj.com>`, Apache-2.0
- **Action Layer:** `L1`
- **Immutable Code Pin:** `731d825d966d9b6df5678c4c059ea1e3d068c67a`
- **Fired Falsifiers:** None (`0` discrepancies across all $8$ stages).

---

## 1. Independent First-Run Verdict (Before Primary Code/Output Inspection)

All seven claims in [#1534](https://github.com/mathorn1973/twist-j/issues/1534) are independently proved in `PROOF.md` and exhaustively verified by `break.py` / `verify.py` (`stdout_sha256: 91d70f13de4d43edd91958cc2712112848b07b182c62ae42c90d8dcb2fa3a8c4`, `1001` bytes, `11` lines):

1. **Claim 1 (Complete Nonlinear Bijection $\Phi$ and Fibres):**
   - Both $\Psi_{\mathrm{aff}}$ and $\Phi$ are two-sided bijections on all $15,625$ states of $\mathbb{F}_5^6$ ($31,250$ two-way compositions each).
   - The sheet-by-sheet definition of $\Phi$ and $\Phi^{-1}$ agrees identically with the global Lagrange-polynomial formulas on all $15,625$ states, and $\Phi(x)_1 = T(x) = e_0(z)C + e_2(z)q + (e_1(z)+e_4(z))\tau(z,A)D + e_3(z)D \bmod 5$.
   - On all $6,250$ states with $z \in \{1, 4\}$ (including all $1,250$ states with $z \in \{1, 4\}, A = 0$ where $\tau(z, 0) = 1$), $\tau(z, A)$ is invertible with polynomial inverse $\sigma(z, A) = \tau(z, A)^3 \equiv z A + 1 - A^4 \pmod 5$.
   - Every receiver value $r_0 \in \mathbb{F}_5^2$ ($25$ values) has a preimage fibre of cardinality $625$.
2. **Claim 2 (Actual $n = 0$ Three-Step Prefix):**
   - For all $25$ ordered message pairs $(\lambda, \mu) \in \mathbb{F}_5^2$, $\Phi(E(\lambda, \mu)) = (2, 0, 1, 0, \lambda, \mu)$, so the initial receiver $R(x_0) = (2, 0)$ is common across all $25$ preparations while $\lambda, \mu$ are independent coordinates of the complement $S(x_0) = (1, 0, \lambda, \mu)$.
   - Under unchanged $U$ from $n = 0$, the selector sequence is $(2, 2, 4)$, the trace sequence is $(2, 0, 2, 1)$, $x_2 = x_0$ in $\mathbb{F}_5^6$ (while $(2, x_2) \ne (0, x_0)$ in $\Omega$), the receiver sequence is $((2, 0), (0, \lambda), (2, 0), (1, \mu))$, and the semantic reader outputs $(\mathrm{BLANK}, \mathrm{PRESENT}(\lambda), \mathrm{BLANK}, \mathrm{PRESENT}(\mu))$ with $\mathrm{PRESENT}(0) \ne \mathrm{BLANK}$.
3. **Claim 3 (Synchronized $5,000$-State Invariants and All-Time Induction):**
   - On all $5,000$ states of $\mathcal{S}_{5000} = \{x \in \mathbb{F}_5^6 : z(x) \in \{1, 4\}, A(x) \ne 0\}$ and both selector bits $\theta \in \{0, 1\}$ ($10,000$ transitions), $\mathcal{S}_{5000}$ is closed and both rational invariants $(z C / A, z D / A) \bmod 5$ are preserved, with $R(x) = (z, z D / A)$ and $G(R(x)) = \mathrm{PRESENT}(z D / A)$.
   - Since $x_3(\lambda, \mu) \in \mathcal{S}_{5000}$ has $(z_3 C_3 / A_3, z_3 D_3 / A_3) = (\lambda, \mu)$, induction establishes $G(R(x_n(\lambda, \mu))) = \mathrm{PRESENT}(\mu)$ for all $n \ge 3$.
4. **Claim 4 (Prepared $500$-State Tail Partition and Trajectory Regression):**
   - The $25$ pair sets $\mathcal{T}_{\lambda, \mu}$ ($A \in \{1, 4\}, z \in \{1, 4\}, q \in \mathbb{F}_5, B = 0, C = \lambda A / z, D = \mu A / z$) each have $20$ states, are pairwise disjoint, have $500$-state union $\mathcal{T}_{500}$ closed under both selector bits ($1,000$ edges), and contain $x_3(\lambda, \mu)$ in the proper class $\mathcal{T}_{\lambda, \mu}$.
   - Explicit trajectory regression from $n = 0$ through $n = 1024$ across all $25$ pairs ($25,625$ checkpoints, $25,600$ transitions) confirms invariant retention at every step.
5. **Claim 5 (Autonomous $(z, q, r)$ Quotient and Access Boundary):**
   - $\pi_{z,q,r}(x) = (z(x), q, r)$ forms an exact autonomous quotient under all five generators ($78,125$ checks) and both selector bits ($31,250$ checks).
   - All $25$ preparations start at $\pi_{z,q,r}(E(\lambda, \mu)) = (2, 0, 1)$, whose reachable quotient set under $\{\bar{T}_0, \bar{T}_1\}$ has $22$ states ($2$ prefix triples plus $20$ tail triples). Across all $n \ge 0$, $(z_n, q_n, r_n)$ and the raw $(q_n, r_n)$ port history are completely message-independent, while the raw source block $(a_n, b_n, c_n, d_n)$ retains $25$ distinct values at every $n$ (no source depletion, no fresh second arrival, no counter reset). $R(x)$ is a mixed nonlinear coordinate coupling source and port coordinates.
6. **Claim 6 (Nonaffinity Witness and Reconciliation with the Affine Obstruction):**
   - $E(0, 0) = (4, 3, 2, 2, 0, 1)$ and $E(0, 1) = (4, 1, 2, 4, 0, 1)$ share $R = (2, 0)$ before $g_4$ and split to $R(g_4(E(0, 0))) = (1, 0) \ne (1, 1) = R(g_4(E(0, 1)))$ after $g_4$.
   - The arbitrary-rank affine common-reset obstruction remains intact: across all $15,625$ states, $z(x_2) \in \{1, 2\}$ ($9,375$ states with $z_2 = 1, x_2 + x_3 = t_3, V(x_3) = -V(x_2)$ and $6,250$ states with $z_2 = 2, x_2 + x_3 = t_4$), so any affine map $R_{\mathrm{aff}}(x) = L x + h$ satisfies $R_{\mathrm{aff}}(g_4(x)) = -R_{\mathrm{aff}}(x) + 2h + L t_4$ and cannot split states that share $R_{\mathrm{aff}}$ before $g_4$. The present $R = (z, T)$ escapes solely because $T(x)$ is nonlinear (degree $5$).
7. **Claim 7 (Minimal Two $\mathbb{F}_5$ Coordinates and Non-Autonomy):**
   - Realizing all $6$ distinct semantic outputs ($\mathrm{BLANK}$ and $\mathrm{PRESENT}(0..4)$) requires at least $k = 2$ coordinates in $\mathbb{F}_5$ ($5^1 = 5 < 6 \le 25 = 5^2$). No claim is made regarding bit count, physical dimension, or minimal polynomial degree.
   - $E(0, 0) = (4, 3, 2, 2, 0, 1)$ and $E(1, 0) = (2, 3, 4, 2, 0, 1)$ share $R = (2, 0)$ at $n = 0$ but map to $R(x_1(0, 0)) = (0, 0) \ne (0, 1) = R(x_1(1, 0))$ at $n = 1$, proving no receiver-only autonomous evolution exists.

---

## 2. Scope and Interpretation Limits

This result establishes **NON-CANONICAL L1 mathematical existence** in the finite-field polynomial-coordinate comparison class on $\mathbb{F}_5^6$. Polynomial expressibility over $\mathbb{F}_5$ is broad and does not constitute an independently selected physical detector law, physical apparatus admission, raw-port readout, or L2–L6 lift. No Canon fold or merge is authorized.
