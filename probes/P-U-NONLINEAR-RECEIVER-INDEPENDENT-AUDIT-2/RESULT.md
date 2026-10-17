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

---

## 3. Post-First-Run Comparison with Primary `P-U-NONLINEAR-ORIGIN-RECEIVER-1` and Two-Architecture Replay

After publicly recording the immutable code pin (`731d825d966d9b6df5678c4c059ea1e3d068c67a`, [#1534 comment 6201093692](https://github.com/mathorn1973/twist-j/issues/1534#issuecomment-6201093692)) and the first formal run (`e39dd956644fbcdb4ccc269d2c588c7ae4af1051`, [#1534 comment 6201137505](https://github.com/mathorn1973/twist-j/issues/1534#issuecomment-6201137505)), the primary files in `probes/P-U-NONLINEAR-ORIGIN-RECEIVER-1/` (primary pin `91d7fe88a6b964df07e275ec55da96f738b08583`, first result commit `e767c191996389684cd04f0c6c1e6e63ab9484c6`, Draft PR [#1533](https://github.com/mathorn1973/twist-j/pull/1533)) were inspected and compared item-for-item against this independent audit:

1. **Mathematical Definitions and Equations (`PROOF.md` & `INTERFACE.json`):**
   - **Affine chart (`base_chart` / `base_inverse` vs. $\Psi_{\mathrm{aff}}$ / $\Psi_{\mathrm{aff}}^{-1}$):** Identical $\mathbb{F}_5^6$ bijection $(z, A, B, C, D, q) = (a+b+c+d+q+r, a+c, b+d, a-c-2, b-d-1, q) \bmod 5$ with inverse $(a, b, c, d, q, r) = (3(A+C+2), 3(B+D+1), 3(A-C-2), 3(B-D-1), q, z-A-B-q) \bmod 5$.
   - **Nonlinear scale and global chart (`tau`, `chart`, `chart_inverse`, `receiver`, `polynomial_receiver` vs. $\tau, \Phi, \Phi^{-1}, R, T$):** Identical $\tau(z, A) = z A^3 + 1 - A^4 \bmod 5$, identical sheet-by-sheet definition of $\Phi(x) = (z, T(x), S(x))$ across $z \in \{0, 1, 2, 3, 4\}$ (including the unused $z = 3$ sheet $\Phi(x) = (3, D, A, B, C, q)$), identical global inverse via $\tau(z, A)^3 \equiv z A + 1 - A^4 \pmod 5$ on $z \in \{1, 4\}$ (including $A = 0$ where $\tau(z, 0) = 1$), and identical Lagrange selector polynomial $T(x) = e_0(z) C + e_2(z) q + (e_1(z) + e_4(z))(z A^3 + 1 - A^4) D + e_3(z) D \bmod 5$.
   - **Product preparation and prefix (`prepare`, `read_record` vs. $E(\lambda, \mu), G$):** Identical $E(\lambda, \mu) = (3(\lambda+3), 3(\mu+1), 3(-\lambda-1), 3(-\mu-1), 0, 1) \bmod 5$ with $\Phi(E(\lambda, \mu)) = (2, 0, 1, 0, \lambda, \mu)$, common receiver $R(x_0) = (2, 0)$, independent complement $S(x_0) = (1, 0, \lambda, \mu)$, total reader $G(z, t) = \mathrm{BLANK}$ on $z \in \{2, 3\}$ and $\mathrm{PRESENT}(t)$ on $z \in \{0, 1, 4\}$ ($\mathrm{PRESENT}(0) \ne \mathrm{BLANK}$), selector prefix $(2, 2, 4)$, trace prefix $(2, 0, 2, 1)$, $x_2 = x_0$ in $\mathbb{F}_5^6$ without $\Omega$-counter reset $(2, x_2) \ne (0, x_0)$, receiver sequence $((2, 0), (0, \lambda), (2, 0), (1, \mu))$, and semantic output $(\mathrm{BLANK}, \mathrm{PRESENT}(\lambda), \mathrm{BLANK}, \mathrm{PRESENT}(\mu))$.
   - **Synchronized invariants and prepared tail (`invariant_pair`, `tail` vs. $\mathcal{S}_{5000}, \mathcal{T}_{\lambda, \mu}$):** Identical $5,000$-state domain $\{z \in \{1, 4\}, A \ne 0\}$ ($10,000$ edges) preserving $(z C / A, z D / A) \bmod 5$ under both driver bits $\theta \in \{0, 1\}$, and identical $25 \times 20 = 500$-state disjoint prepared-tail partition $\mathcal{T}_{500}$ ($1,000$ edges) with $B = 0, C = \lambda A z^3, D = \mu A z^3$ and $25,625$-checkpoint / $25,600$-update trajectory verification through $n = 1024$.
   - **Comparison boundaries (`quotient`, nonaffinity, coordinate minimum, non-autonomy):** Identical $78,125$-edge generator / $31,250$-edge selector verification of the $(z, q, r)$ quotient, identical $22$-state reachable quotient set ($2$ prefix + $20$ tail) from $(2, 0, 1)$ proving message-independence of $(z_n, q_n, r_n)$ and raw $(q_n, r_n)$ while $(a_n, b_n, c_n, d_n)$ retains $25$ states, identical nonaffinity witness $E(0, 0), E(0, 1)$ under $g_4$, identical reconciliation with the affine common-reset obstruction ($9,375$ states on $z_2 = 1$ with $V(x_3) = -V(x_2)$ and $6,250$ states on $z_2 = 2$), identical $k = 2$ minimal $\mathbb{F}_5$ coordinate count for $6$ semantic labels, and identical non-autonomy witness $E(0, 0), E(1, 0)$ at $n = 1$.
2. **Every Quantitative Count Matches Between Primary `EXPECTED.txt` (`39053d15006fab354bcbfb1219cb249755bb10dbcf168e1d5ccb12623f25d2a9`) and Independent `EXPECTED.txt` (`91d70f13de4d43edd91958cc2712112848b07b182c62ae42c90d8dcb2fa3a8c4`):**
   - `generators`: `78,125` tuple/matrix/involution/affine/trace/quotient checks, `31,250` selector checks.
   - `chart`: `31,250` two-way compositions each for $\Psi_{\mathrm{aff}}$ and $\Phi$, `15,625` polynomial receiver checks, `25` receiver fibres of `625` states, `1,250` zero-$A$ states on $z \in \{1, 4\}$.
   - `prefix`: `25` pairs, selectors `(2, 2, 4)`, traces `(2, 0, 2, 1)`, $x_2 = x_0$ for all `25` pairs, `1` common initial receiver `(2, 0)`.
   - `invariants`: `5,000` states, `10,000` edges, `25` invariant fibres of `200` states.
   - `tail`: `25` disjoint `20`-state sets, `500` union states, `1,000` closed edges.
   - `trajectory`: `25` pairs, horizon `1024`, `25,625` checkpoints, `25,600` updates.
   - `boundaries`: `6` semantic values, `k = 2` minimal $\mathbb{F}_5$ coordinates, `22` reachable $(z, q, r)$ states (`2` prefix + `20` tail), `1` raw $(q_n, r_n)$ trajectory vs. `25` source `(a,b,c,d)` states per step, `9,375` / `6,250` split at $n = 2$, `6` malformed input rejections.
3. **Two-Architecture Public Replay (Draft PR [#1537](https://github.com/mathorn1973/twist-j/pull/1537), GitHub Run [`38798698458`](https://github.com/mathorn1973/twist-j/actions/runs/38798698458)):**
   - Local `aarch64` leg (`Python 3.13.13`), GitHub `x86_64` leg (job [`116641770543`](https://github.com/mathorn1973/twist-j/actions/runs/38798698458/job/116641770543)), and GitHub `aarch64` leg (job [`116641770067`](https://github.com/mathorn1973/twist-j/actions/runs/38798698458/job/116641770067)) all exited `0` with `0` stderr bytes and byte-identical `EXPECTED.txt` (`91d70f13de4d43edd91958cc2712112848b07b182c62ae42c90d8dcb2fa3a8c4`, `1001` bytes, `11` lines), and `policy/check` (job [`116642203746`](https://github.com/mathorn1973/twist-j/actions/runs/38798698458/job/116642203746)) passed.
   - Primary Draft PR [#1533](https://github.com/mathorn1973/twist-j/pull/1533) also independently passed `architecture-x86_64`, `architecture-aarch64`, and `policy/check`.
4. **Audit Conclusion:**
   - **CONFIRMED (0 mathematical, computational, or scope discrepancies).** Both the independent analytical proof and the independent from-scratch audit program confirm all seven claims of [#1532](https://github.com/mathorn1973/twist-j/issues/1532) / [#1533](https://github.com/mathorn1973/twist-j/pull/1533) / [#1534](https://github.com/mathorn1973/twist-j/issues/1534) within their exact `PUBLIC / NON-CANONICAL / L1` scope.

