# Preregistration: P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-2

**PUBLIC / NON-CANONICAL / L1 — Independent Audit of Nonlinear Two-Message Possibility on Unchanged $U$**

- **Issue:** [#1534](https://github.com/mathorn1973/twist-j/issues/1534) (5897 UTF-8 bytes, SHA-256 `cf3668d6e51b7225fb0a7e9b223c612792b58dbd9ccf79cf0d19503a578d4b27`)
- **Primary Lane:** [#1532](https://github.com/mathorn1973/twist-j/issues/1532) / Draft PR [#1533](https://github.com/mathorn1973/twist-j/pull/1533) (`probes/P-U-NONLINEAR-ORIGIN-RECEIVER-1`, primary owner `ChatGPT-20261015-nonlinear-origin-receiver`)
- **Audit Owner:** `Antigravity-20261015-nonlinear-receiver-independent-audit-1`
- **Public Claim Receipt:** [#1534 comment 6200684498](https://github.com/mathorn1973/twist-j/issues/1534#issuecomment-6200684498)
- **Author:** A. M. Thorn `<thorn@twistj.com>`, Apache-2.0
- **Authority & Base:** `mathorn1973/twist-j` `main` at `b79143fb00839b870686f6cea34e174959060df1`, `Public Canon v101` (`canon-v101`), `CONTENT_COMMIT: 421a4ec1daf07c04d19022c1ee219607e83c09a8`, `CANON_SHA256: b83a99feccac173bd3c9c5851c5874ca27cbd135f71d136d793b45f86c8a87f7`, `CANON_BYTES: 992352`.

## Mandatory Abandoned Predecessor and Exposure Statement

This probe is the fresh successor to `P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-1` (pinned at `8edb5ea97bf38337d9c65f08964a0ae9e2ed7743` and closed with `Status: ABANDONED` at `d9a20f7bba60ae868aa467b5b076960ac5e88b7d` on `probe/P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-1`). On the predecessor's invocation under the default system `python3` (`3.9.6`), it exited nonzero (`exit_code: 1`) on `n.bit_count()` in `theta_bit`, and line 487 of `break.py` contained an internal fixture defect asserting `len(expected_tail_zqr) == 10` on the $2 \times 2 \times 5 = 20$-element set `{(z, q, (z - A - q) % 5) for z in (1, 4) for A in (1, 4) for q in F5}` after Stages 0–5 had passed (together with `x14_sign_rep` and the $d_1 = 2$ coordinate in `x1_00`, `x1_10` corrected here). The predecessor identifier `P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-1` is permanently consumed and is not reused, repaired, or resumed.

**Independent-code barrier:** Prior to committing, pushing, publicly reading back, and executing this pin, no primary `verify.py`, `EXPECTED.txt`, `RUN.md`, `RESULT.md`, `PROOF.md`, `INTERFACE.json`, source diff, or output digests from `P-U-NONLINEAR-ORIGIN-RECEIVER-1` (#1532 / #1533) were opened or inspected.

---

## 1. Equation

For $x = (a, b, c, d, q, r) \in \mathbb{F}_5^6$, let $z(x) = a + b + c + d + q + r \bmod 5$, $\theta_n = \operatorname{popcount}(n) \bmod 2$, $j_n = (z(x) + 2\theta_n) \bmod 5$, and $U(n, x) = (n + 1, g_{j_n}(x))$ with:
$$\begin{aligned}
g_0(x) &= (b, a, d, c, q, r), \\
g_1(x) &= (-c, -d, -a, -b, -q, -r), \\
g_2(x) &= (2-c, 1-d+r, 2-a, 1-b-r, 1-q, -r), \\
g_3(x) &= (2-a, 1-b, 3-c, 4-d, 1-q, 1-r), \\
g_4(x) &= (2-a, 1-b, 3-c, 4-d, 2-q, 1-r) \pmod 5.
\end{aligned}$$
Set $A = a + c$, $B = b + d$, $C = a - c - 2$, $D = b - d - 1 \pmod 5$, with inverse $\Psi_{\mathrm{aff}}^{-1}(z, A, B, C, D, q) = (3(A+C+2), 3(B+D+1), 3(A-C-2), 3(B-D-1), q, z-A-B-q) \pmod 5$.
For $(\lambda, \mu) \in \mathbb{F}_5^2$, the $n = 0$ preparation is
$$E(\lambda, \mu) = \bigl(3(\lambda+3),\; 3(\mu+1),\; 3(-\lambda-1),\; 3(-\mu-1),\; 0,\; 1\bigr) \pmod 5.$$
Set $\tau(z, A) = z A^3 + 1 - A^4 \bmod 5$, $\sigma(z, A) = z A + 1 - A^4 \bmod 5$, and $e_j(z) = 1 - (z - j)^4 \bmod 5$. The complete nonlinear chart $\Phi : \mathbb{F}_5^6 \to \mathbb{F}_5^6$ is:
$$\Phi(x) = \begin{cases}
(z, C, A, B, D, q) & z = 0, \\
(z, q, A, B, C, D) & z = 2, \\
(z, \tau(z, A) D, A, B, C, q) & z \in \{1, 4\}, \\
(z, D, A, B, C, q) & z = 3,
\end{cases}$$
with second coordinate $T(x) = e_0(z) C + e_2(z) q + (e_1(z) + e_4(z))\tau(z, A) D + e_3(z) D \pmod 5$, global inverse $\Phi^{-1}$ derived in `PROOF.md` Section 2 (using $D = \sigma(z, A) y_1$ on $z \in \{1, 4\}$, including $\tau(z, 0) = \sigma(z, 0) = 1$ at $A = 0$), receiver $R(x) = (\Phi(x)_0, \Phi(x)_1) = (z, T(x)) \in \mathbb{F}_5^2$, and fixed total semantic reader
$$G(z, t) = \begin{cases}
\mathrm{BLANK} & z \in \{2, 3\}, \\
\mathrm{PRESENT}(t) & z \in \{0, 1, 4\},
\end{cases}$$
where $\mathrm{PRESENT}(0) \ne \mathrm{BLANK}$.

---

## 2. Code and Public Pin

- `probes/P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-2/break.py` (37038 bytes, SHA-256 `02f603d72ab50ed2bcc29975b1ffb28b04bd9b6d95e912d37b11661b011fe11c`): self-contained standard-library Python integer audit script implementing all 7 claim checks and input custody checks from scratch.
- `probes/P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-2/verify.py` (649 bytes, SHA-256 `c1a58e10cbf02792ecd44b46eaa9cfc7d56f2f261562c5b8db0efb835c6fd6ba`): minimal standard-library runner invoking `break.py`.
- `probes/P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-2/PROOF.md` (22092 bytes, SHA-256 `c8393b2a4325267457567c0509af63867df29a5bf884254ff8b24ee298acf6b9`): complete independent algebraic proof of Claims 1–7.
- `probes/P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-2/README.md` (1972 bytes, SHA-256 `227c3800d1f4fb77dd3a9dbd543f2f24aee1753c4bd929843053062053ac6c25`): probe overview and scope boundary.
- `probes/P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-2/SOURCES.tsv` (1692 bytes, SHA-256 `994e3b89366efbd16e391c2650ca90bf647f13b31fa16a33e08690fc79a4ab9e`): exact commit, path, SHA-256, and byte-count manifest of authority, predecessor, and disclosed input files.
- `probes/P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-2/INPUTS.sha256`: SHA-256 manifest binding `PREREG.md`, `PROOF.md`, `README.md`, `SOURCES.tsv`, `break.py`, and `verify.py`.

All six initial files and `INPUTS.sha256` are committed, pushed to `origin/probe/P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-2`, and publicly read back via Git before any scientific import or execution of this pin.

---

## 3. Carrier and Exhaustive Test Inventory

All state coordinates are exact canonical integers in $\{0, 1, 2, 3, 4\}$. The verifier executes eight deterministic stages in fixed order:

1. `custody`: verifies `INPUTS.sha256` against all six pinned files and validates `SOURCES.tsv`.
2. `generators_and_quotient`: across all $15,625$ states $x \in \mathbb{F}_5^6$ and all $5$ generators ($78,125$ state-generator pairs), verifies tuple vs. independently derived affine matrix $M_k x + t_k$, involution $g_k(g_k(x)) = x$, affine coordinate transition formulas $(z', A', B', C', D', q', r')$, trace maps, and autonomous $(z, q, r)$ quotient transitions; across both selector bits $\theta \in \{0, 1\}$ ($31,250$ transitions), verifies $\operatorname{im}(\tau_0) = \{0, 4\}$ ($6,250$ states), $\operatorname{im}(\tau_1) = \{1, 2, 3\}$ ($9,375$ states), and quotient intertwining $\pi_{z,q,r}(T_\theta(x)) = \bar{T}_\theta(\pi_{z,q,r}(x))$.
3. `nonlinear_chart_claim1` (**Claim 1**): across all $15,625$ states, verifies two-sided inverses for $\Psi_{\mathrm{aff}}$ ($31,250$ compositions) and $\Phi$ in both sheet-by-sheet and global Lagrange-polynomial forms ($31,250$ compositions each), polynomial equality $\Phi(x)_1 = T(x)$ ($15,625$ checks), all five $z$-sheets ($3,125$ states per sheet), the $A = 0$ locus ($3,125$ states with $\tau(z, 0) = 1$, including $1,250$ states on $z \in \{1, 4\}, A = 0$), $\tau(z, A)\sigma(z, A) \equiv 1 \pmod 5$ on all $6,250$ states with $z \in \{1, 4\}$, and uniform $625$-state preimage fibres across all $25$ receiver values $r_0 \in \mathbb{F}_5^2$.
4. `prefix_claim2` (**Claim 2**): across all $25$ pairs $(\lambda, \mu) \in \mathbb{F}_5^2$, verifies $\Phi(E(\lambda, \mu)) = (2, 0, 1, 0, \lambda, \mu)$, common initial receiver $R(x_0) = (2, 0)$, independent complement coordinates $S(x_0) = (1, 0, \lambda, \mu)$, selector sequence $(2, 2, 4)$, trace sequence $(2, 0, 2, 1)$, checkpoint reset $x_2 = x_0$ (with $(2, x_2) \ne (0, x_0)$ in $\Omega$), receiver trace $((2, 0), (0, \lambda), (2, 0), (1, \mu))$, and semantic outputs $(\mathrm{BLANK}, \mathrm{PRESENT}(\lambda), \mathrm{BLANK}, \mathrm{PRESENT}(\mu))$ with $\mathrm{PRESENT}(0) \ne \mathrm{BLANK}$.
5. `synchronized_invariants_claim3` (**Claim 3**): across all $5,000$ states of $\mathcal{S}_{5000} = \{x \in \mathbb{F}_5^6 : z(x) \in \{1, 4\}, A(x) \ne 0\}$ and both selector bits $\theta \in \{0, 1\}$ ($10,000$ transitions), verifies closure in $\mathcal{S}_{5000}$, invariance of $(z C / A, z D / A) \bmod 5$, $R(x) = (z, z D / A)$, $G(R(x)) = \mathrm{PRESENT}(z D / A)$, uniform $200$-state invariant fibres across all $25$ pairs, and the $n = 3$ induction base $x_3(\lambda, \mu) \in \mathcal{S}_{5000}$.
6. `prepared_tail_and_regression_claim4` (**Claim 4**): generates each $\mathcal{T}_{\lambda, \mu}$ from $A \in \{1, 4\}, z \in \{1, 4\}, q \in \mathbb{F}_5, B = 0, C = \lambda A / z, D = \mu A / z$, verifying $|\mathcal{T}_{\lambda, \mu}| = 20$, pairwise disjointness of all $25$ sets, $500$-state union $\mathcal{T}_{500}$, closure under both selector choices ($1,000$ transitions), $x_3(\lambda, \mu) \in \mathcal{T}_{\lambda, \mu}$, and finite-horizon trajectory regression across $0 \le n \le 1024$ for all $25$ pairs ($25,625$ checkpoints, $25,600$ updates).
7. `access_boundary_and_quotient_claim5` (**Claim 5**): verifies common initial triple $\pi_{z,q,r}(E(\lambda, \mu)) = (2, 0, 1)$, computes the exact $22$-state reachable $(z, q, r)$ quotient set ($2$ prefix triples plus $20$ tail triples) under $\{\bar{T}_0, \bar{T}_1\}$, verifies across all $0 \le n \le 1024$ that $(z_n, q_n, r_n)$ is identical for all $25$ message pairs while the raw source block $(a_n, b_n, c_n, d_n)$ retains $25$ distinct values at every $n$, and verifies that $R(x)$ is a mixed coordinate depending non-trivially on both $(a, b, c, d)$ and $(q, r)$.
8. `nonaffinity_and_minimality_claims6_7` (**Claims 6 & 7**): validates the nonaffinity witness $E(0, 0), E(0, 1)$ ($R = (2, 0)$ before $g_4$, $R = (1, 0) \ne (1, 1)$ after $g_4$), verifies the origin-zero affine obstruction structure ($z(x_2) \in \{1, 2\}$ split $9,375 + 6,250$, $x_2 + x_3 \in \{t_3, t_4\}$, and $X_{14}$ sign-fibre equality $V(x_3) = -V(x_2)$ on $z(x_2) = 1$) across all $15,625$ states, proves $k = 2$ $\mathbb{F}_5$ coordinates minimal for the $6$ semantic outputs ($5^1 < 6 \le 5^2$), validates the non-autonomy witness $E(0, 0), E(1, 0)$ ($R = (2, 0)$ at $n = 0$, $R = (0, 0) \ne (0, 1)$ at $n = 1$), and verifies $6$ explicit malformed-input rejections.

---

## 4. Systematics

- All calculations use Python standard-library exact integer arithmetic modulo $5$; no floating-point numbers, random sampling, or external packages are used.
- Universal all-time retention from $n \ge 3$ and the reconciliation with the arbitrary-rank affine common-reset obstruction rest on the exact algebraic proofs in `PROOF.md` together with exhaustive finite-carrier closure on $\mathcal{S}_{5000}$ and $\mathcal{T}_{500}$, never on finite trajectory extrapolation alone.
- No lookup table of source labels, external clock argument in $R$ or $G$, history buffer, auxiliary state, or modified transition is admitted.

---

## 5. Failure Threshold and Execution Disposition

- **Zero tolerance:** Any single mismatch in any stage raises `ExactAuditFailure`, prints `STAGE <name> FAIL <witness>`, marks all subsequent stages `NOT_RUN`, and exits `0` with `VERDICT SCIENTIFIC_FAIL` so the negative record is preserved and reproducible. Unexpected runtime exceptions, custody failures, or timeouts exit nonzero and require the `POLICY.md` abandoned-pin disposition.
- **Execution environment:** Clean checkout of the publicly read-back pin commit, Python $\ge 3.9$, `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`, timeout $600$ seconds. Exact stdout is saved as `EXPECTED.txt`, neutral environment metadata is recorded in `RUN.md`, and scientific conclusions (followed after two-architecture replay by the primary-code comparison) are recorded in `RESULT.md`.

---

## 6. Action Layer and Interpretation

- **Action layer:** `L1` only (`PUBLIC / NON-CANONICAL / L1`).
- **Interpretation boundary:** A passing audit establishes only L1 mathematical existence of the stated nonlinear polynomial coordinate chart $\Phi$ and two-coordinate receiver $R = (z, T)$ on the unchanged native $U$ within the finite-field polynomial-coordinate comparison class. It does not establish physical admissibility, a unique physical detector law, raw-port observability, source depletion, or any L2–L6 lift, nor does it withdraw or weaken the arbitrary-rank affine common-reset obstruction theorem.
