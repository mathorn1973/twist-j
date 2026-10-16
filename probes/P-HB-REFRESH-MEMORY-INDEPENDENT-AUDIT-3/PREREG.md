# Preregistration: P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3

**PUBLIC / NON-CANONICAL / L1 — Independent Audit of Two-Contact Wave-Summary Memory Ranks and Refresh Laws on the 705-Site $D_3$ Carrier (Successor to `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` and `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2`)**

- **Issue:** [#1528](https://github.com/mathorn1973/twist-j/issues/1528) (5836 UTF-8 bytes, SHA-256 `1c93022e9c24d4e35c290bccb65afe8e14bedfdaaa472ddfbb0cb02f3da80f80`)
- **Primary Lane:** [#1525](https://github.com/mathorn1973/twist-j/issues/1525) (`notes/C-HB-REFRESH-MEMORY-BOUNDARY-N`, primary owner `ChatGPT-20261015-hb-refresh-memory-boundary`, primary `PREREG.md` at `8ab77c73426a6a65a13ddb8798390df534e64814`)
- **Program:** [#1506](https://github.com/mathorn1973/twist-j/issues/1506) / [#1548](https://github.com/mathorn1973/twist-j/issues/1548) (13858 UTF-8 bytes, SHA-256 `c209686fede612501394f969d5052518d35c95be0523c9e22619cbd19984fd87`)
- **Audit Owner:** `Antigravity-20261017-v103-hb-refresh-memory-audit`
- **Public Claim Receipt:** [#1528 comment 6225725304](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6225725304)
- **Preserved Predecessors:**
  - `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` (`origin/probe/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1`, pin commit `bda14aabb495be1db5790c86b6a68d6721cb1fab`, negative report head `475a033091db921b28fb409707353ef49870050e`, disposition `PARTIAL / STOP`, `NOT ABANDONED`; public receipts [#1528 comment 6225908014](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6225908014) and [#1528 comment 6226034498](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6226034498))
  - `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2` (`origin/probe/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2`, pin commit `453e4404bf987f7b5747b5bb59351ee459dade7f`, negative report head `c8d4fd675490feeeeab06a15a8b1ff5fa06bdd29`, disposition `PARTIAL / STOP`, `NOT ABANDONED`; public receipts [#1528 comment 6226130073](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6226130073) and [#1528 comment 6226180715](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6226180715))
- **Author:** A. M. Thorn `<thorn@twistj.com>`, Apache-2.0
- **Authority & Base:** `mathorn1973/twist-j` `main` at `a632c6a162dc87e60104d7a478e7650a6d5c4a1b`, `Public Canon v102` (`canon-v102`), `CONTENT_COMMIT: b04e22dd3ed8e4240cff347364f24670d4183a4d`, `CANON_SHA256: c0657380438c965f9556b5b298a34a5e799c48a68ce66e9fe51786ce2413d7d1`, `CANON_BYTES: 1024033`, release gate run `38956254023` (attempt 2).

## Predecessor Disclosure, Exposure Boundary, and Information Barrier

### Predecessor Dispositions (`P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` and `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2`)

1. **`P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` (`bda14aabb495be1db5790c86b6a68d6721cb1fab` / `475a033091db921b28fb409707353ef49870050e`):** Passed Stages 1–3 (`custody`, `geometry_and_operators`, and all $7130$ refresh coefficients of `refresh_identities_target1`). In Stage 4 (`rank_minors_and_criteria_target2`), `det3 = -3/5248800` passed and the factored Target 2 check `check_eq(det4, MINOR_4X4_TARGET, stage, "det4-target")` (`(3/5)*(-1/(10*324))*(-1/(10*324^2)) = 1/5668704000 = 3/17006112000`) passed, after which the redundant hand-multiplied denominator literal check `Q(3, 1698693120000)` fired (`5 * 3240 * 1049760 = 17006112000`). Preserved intact on `origin/probe/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` as `PARTIAL / STOP` (`NOT ABANDONED`).
2. **`P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2` (`453e4404bf987f7b5747b5bb59351ee459dade7f` / `c8d4fd675490feeeeab06a15a8b1ff5fa06bdd29`):** Passed Stages 1–5 (`custody`, `geometry_and_operators`, `refresh_identities_target1`, `rank_minors_and_criteria_target2`, and `far_counterexample_target3`) and in Stage 6 (`finite_contact_predictor_target4`) passed all $50$ signed-source constants, all $70500$ wave-work linear coefficients, all $2000$ single-contact guarded cases, and all $480$ two-contact guarded cases; at line 1266 (post-loop regime coverage check), `missing-two-kind-zero_cost_accept` fired because the first source pair in `source_pairs` had been written as `((0, 3), (2, 4))` instead of the zero-source pair `((0, 4), (2, 4))` ($\ell(4) = -1 \implies \eta_2(0, 4) = (0, 0)$, whereas $\ell(3) = -2 \implies \eta_2(0, 3) = (0, -1/2)$). Preserved intact on `origin/probe/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2` as `PARTIAL / STOP` (`NOT ABANDONED`).

Because `tools/check_verifier.py` enforces a single probe directory per branch diff against `main`, this successor branch `probe/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3` starts cleanly from `main` (`a632c6a162dc87e60104d7a478e7650a6d5c4a1b`) and binds both predecessors' `PREREG.md`, `EXPECTED.txt`, and `RESULT.md` in `SOURCES.tsv` (`20` rows total). The single functional change in `break.py` relative to `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2` (aside from `PROBE_ID = "P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3"`) replaces `((0, 3), (2, 4))` by `((0, 4), (2, 4))` on line 1166.

### Exposure Boundary and Active Information Barrier

Prior to committing, pushing, publicly reading back, and executing this successor pin `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3`, only the permitted pre-pin inputs specified in [#1528](https://github.com/mathorn1973/twist-j/issues/1528) and our own predecessors `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` and `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2` were read:
1. Assignment body [#1528](https://github.com/mathorn1973/twist-j/issues/1528) (`5836` bytes, `1c93022e9c24d4e35c290bccb65afe8e14bedfdaaa472ddfbb0cb02f3da80f80`) and program issue [#1548](https://github.com/mathorn1973/twist-j/issues/1548) (`13858` bytes, `c209686fede612501394f969d5052518d35c95be0523c9e22619cbd19984fd87`).
2. Primary preregistration `notes/C-HB-REFRESH-MEMORY-BOUNDARY-N/PREREG.md` (`8911` bytes, `7fea37b85b371702f4a9a18ee75ea237d3ccd2eb7d7b96549d115f9caadfa7d4`) and `SOURCES.tsv` (`2106` bytes, `21e6e0af66bcad6e953ac1aee0c35c881baf45385fd2b75623e628df747f27d7`) at commit `8ab77c73426a6a65a13ddb8798390df534e64814`.
3. Authority and `main` mathematical sources: `probes/P-D3-TWO-CUT-GEOMETRY-RECONCILIATION-1/PROOF.md` and `DOMAIN.tsv`, `probes/P-FUNDED-TWO-USE-INDEPENDENT-AUDIT-2/PROOF.md`, and `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/CLOSURE.md`.
4. Predecessors `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` and `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2`, authored solely by this audit session.

**Independent-code barrier:** Primary `verify.py`, `PROOF.md`, `EXPECTED.txt`, `RUN.md`, `RESULT.md`, and primary result comments in [#1525](https://github.com/mathorn1973/twist-j/issues/1525) remain unopened before `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3` is pinned, pushed, publicly read back, and its first formal run is executed and publicly recorded.

---

## 1. Equation

On the $705$-site finite Dirichlet domain $D = Y + B_0 + B_0 \subset \{x \in \mathbb{Z}^3 : x_1 + x_2 + x_3 \equiv 0 \pmod 2\}$ with $Y = ((0,0,0), (1,1,0), (1,0,1), (0,1,1), (2,0,0))$, ports $Y_p = (y_0, y_1, y_2, y_3)$, fifth site $y_4 = (2,0,0)$, and five-shell stencil $B$ of squared lengths $(2, 4, 8, 10, 16)$ and weights $(6, 1, 15, 1, 1)/324$:
- $H = 2I - L_D$ has diagonal $10/9$ on $D$ and off-diagonal weights $+w(x - y)$ for $x - y \in B$.
- $P \in \mathbb{Q}^{D \times 4}$ inserts the four ports, $Q_p = P P^T$, $J_0 = I - Q_p$, $K = I - \frac{1}{2} Q_p$, $e_4 = \delta_{y_4}$, $s_i = \delta_{y_i} - \frac{1}{5}\sum_{j=0}^4 \delta_{y_j}$, and $A = [s_0\ s_1] \in \mathbb{Q}^{D \times 2}$.
- $G = A^T A = \frac{1}{5}\begin{pmatrix} 4 & -1 \\ -1 & 4 \end{pmatrix}$, $M = A^T P \in \mathbb{Q}^{2 \times 4}$, and $h^T = e_4^T H P = \frac{1}{324}(1, 6, 6, 0)$.
- Full wave/tape state $X = (u, v, a_0, a_1, b_0, b_1) \in \mathbb{Q}^{1426}$ evolves under $F(u, v, a_0, a_1, b_0, b_1) = (v, w, a_1, b_1, b_{\mathrm{out}}, b_0)$ with $w = K(H v - J_0 u + 4 P a_0)$ and $b_{\mathrm{out}} = a_0 - \frac{1}{2}P^T(w - u)$.
- Wave-only linear coordinates:
  $$\rho(u, v) = A^T\left(v - \frac{1}{2} H u\right) \in \mathbb{Q}^2, \qquad \gamma(u, v) = \frac{1}{5}\left(e_4^T u - \frac{1}{2} e_4^T H v\right) \in \mathbb{Q},$$
  $$\delta(u, v) = \frac{1}{5}\left(e_4^T v - \frac{1}{2} e_4^T H K H v + \frac{1}{2} e_4^T H J_0 u\right) \in \mathbb{Q}.$$
- Exact refresh identities on all $X \in \mathbb{Q}^{1426}$:
  $$\rho(FX) = \gamma(X)\mathbf{1}_2 + 2 M a_0, \qquad \gamma(FX) = \delta(X) - \frac{1}{5} h^T a_0, \qquad \rho(F^2 X) = \left(\delta(X) - \frac{1}{5} h^T a_0\right)\mathbf{1}_2 + 2 M a_1.$$
- Reduced two-contact predictor $\xi = (\rho, \delta)$: with $\eta_2(q, r) = (\ell(q)/2, (\ell(r)+1)/2)^T$, $\ell(0..4) = (0, 1, 2, -2, -1)$, and $\kappa^T = \frac{1}{5}e_4^T(A - \frac{1}{2} H K H A) = -\frac{(145483, 173653)}{10497600}$, a guarded contact with effective sign $\tilde{\sigma} \in \{-\sigma, 0, +\sigma\}$ updates $\rho \mapsto \rho + \tilde{\sigma} G \eta_2$ and $\delta \mapsto \delta + \tilde{\sigma} \kappa^T \eta_2$.

---

## 2. Code and Public Pin

- `probes/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3/break.py` (`46090` bytes, SHA-256 `151c132b413f6c9fc6a33442d8700641deb63ea74b70a4c0d60f9eb7976af60f`): self-contained standard-library Python exact rational/integer audit script implementing all four target audits and custody verification from scratch.
- `probes/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3/verify.py` (`835` bytes, SHA-256 `922f58614dc1ef363e0968d5577b6a7192d5ea47ddf5d1f578d8586acf178d91`): minimal standard-library wrapper invoking `break.py`.
- `probes/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3/PROOF.md` (`23064` bytes, SHA-256 `0de577685abd330dff963fbff2fe5e9fe7f014788740d26465e50d8da388f32c`): complete independent algebraic derivations of Targets 1–4 and predecessor disclosures.
- `probes/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3/README.md` (`4346` bytes, SHA-256 `922fe347ac11b329be2dd0100641d5743b574bcf8d11b2eb1ea9300c131e6ee8`): probe overview, predecessor links, and reproduction command.
- `probes/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3/SOURCES.tsv` (`3016` bytes, SHA-256 `40fe65eea744f026f9eb0054108298ef210430614f820200a78807a3c52b6a6b`): exact commit, path, SHA-256, and byte-count manifest of authority, permitted pre-pin inputs, and both predecessor records (`20` rows).
- `probes/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3/DOMAIN.tsv` (`5029` bytes, SHA-256 `2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0`): canonical ordered $705$-site coordinate list verified against independent construction from $Y + B_0 + B_0$.
- `probes/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3/INPUTS.sha256`: SHA-256 manifest binding `DOMAIN.tsv`, `PREREG.md`, `PROOF.md`, `README.md`, `SOURCES.tsv`, `break.py`, and `verify.py`.

All seven files and `INPUTS.sha256` are committed, pushed to `origin/probe/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3`, and publicly read back via Git before the first scientific execution of `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3`.

---

## 3. Carrier and Complete Finite Inventory

All coordinates and energies are exact `fractions.Fraction` values over $\mathbb{Q}$. The verifier executes six deterministic stages in fixed order:

1. `custody`: verifies `INPUTS.sha256` against all seven pinned files in `probes/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3/` and validates all `20` rows of `SOURCES.tsv`.
2. `geometry_and_operators`: constructs $B$ ($60$ points, weight sum $288/324 = 8/9$), $B_0$ ($61$ points), and $D = Y + B_0 + B_0$ ($705$ sites), verifies byte-for-byte and site-by-site equality with `DOMAIN.tsv`, verifies $D_3$ parity, stencil symmetry, $H + L_D = 2I$, Lemma 1 projector identities ($A^T J_0 = -\frac{1}{5}\mathbf{1}_2 e_4^T$, $K - \frac{1}{2}I = \frac{1}{2}J_0$, $K J_0 = J_0$, $K P = \frac{1}{2}P$) across all $705$ sites and $4$ ports, and verifies $G, M, h^T$, and $\kappa^T = -\frac{(145483, 173653)}{10497600}$.
3. `refresh_identities_target1` (**Target 1**): across all $1426$ standard basis inputs of $\mathbb{Q}^{1426}$ ($705$ $u$-sites, $705$ $v$-sites, $16$ tape coordinates), verifies two-sided invertibility of $F$ and $F^{-1}$ ($2852$ compositions), the linear coupling identity $w + u - H v = 2 P(a_0 + b_{\mathrm{out}})$, and all $5 \times 1426 = 7130$ exact coefficient equalities for $\rho(FX)$, $\gamma(FX)$, and $\rho(F^2 X)$ against direct evaluation through $F$ and $F^2$.
4. `rank_minors_and_criteria_target2` (**Target 2**): computes the $3 \times 3$ minor of $(\rho_0, \rho_1, \delta)$ on $((0, s_0), (0, s_1), (0, \delta_{(10,0,0)}))$ ($\det = -\frac{3}{5248800}$) and the $4 \times 4$ minor of $(\rho_0, \rho_1, \gamma, \delta)$ inserting $(0, \delta_{(6,0,0)})$ as third column ($\det = \frac{3}{5}\cdot\left(-\frac{1}{3240}\right)\cdot\left(-\frac{1}{1049760}\right) = \frac{3}{17006112000} = \frac{1}{5668704000}$), and verifies both exact pre-guard work recovery via native basis labels $(2, 4), (0, 1)$ and Boolean guard separation across $n \in \{0, 1, 2\}$.
5. `far_counterexample_target3` (**Target 3**): evolves $X_\pm = (0, \pm \delta_{(10,0,0)}, 0, 0, 0, 0)$ through $F$ and $F^2$, verifying $\rho = (0, 0)^T$, $\gamma = 0$, $E_{\mathrm{full}} = 1/2$, and zero tapes at $n = 0, 1, 2$, $\delta(X_\pm) = \mp \frac{1}{1049760}$, $\rho(F^2 X_\pm) = \mp \frac{1}{1049760}\mathbf{1}_2$, and distinct accepted second-contact works $\frac{419903}{1049760} \ne \frac{419905}{1049760}$ under $A(1, 0)^T$ ($\sigma = +1, B = 1, b = 1/2$), alongside the near witness at $(6, 0, 0)$.
6. `finite_contact_predictor_target4` (**Target 4**): verifies all $50$ signed-source constants and $50 \times 1410 = 70500$ wave-work linear coefficients plus $(\rho, \delta)$ contact shifts, then audits:
   - **$2000$ single-contact guarded cases:** $5$ waves (`far_plus`, `far_minus`, `zero`, `occ_mix_1`, `occ_mix_2`) $\times 2$ four-slot tape options (`tape_zero`, `tape_nonzero`) $\times 25$ labels $(q, r) \in \mathbb{F}_5^2 \times 2$ signs $\sigma \in \{-1, +1\} \times 4$ battery stocks $(b, B) \in \{(0, 0), (1/2, 1), (4/5, 4/5), (2, 4)\}$.
   - **$480$ two-contact guarded cases:** the same $10$ initial states $\times 4$ source pairs $((0, 4), (2, 4))$, $((2, 4), (0, 1))$, $((1, 4), (0, 0))$, $((2, 1), (3, 2)) \times 4$ sign pairs $(\pm 1, \pm 1) \times 3$ battery stocks $(b, B) \in \{(0, 0), (1/2, 1), (4/5, 4/5)\}$, checking the 3-coordinate predictor $\xi = (\rho, \delta)$ against full $1426$-coordinate evolution across all regimes (zero-cost, positive-work, and negative-work acceptances, lower and upper refusals, both signs, and all four `AA, AR, RA, RR` branches).

---

## 4. Systematics

- All calculations use Python standard-library `fractions.Fraction` and `int` arithmetic; no floating-point operations, tolerances, or external libraries are used.
- Universal identities over $\mathbb{Q}^{1426}$ rest on the algebraic proofs in `PROOF.md` and the complete $7130$-coefficient basis audit in Stage 3 and $70500$-coefficient contact audit in Stage 6, not on the finite $2000$-case and $480$-case witness families alone.
- Direct quadratic energy $E_D(u, v) = \frac{1}{2}(\|v - u\|^2 + u^T L_D v)$ uses $L_D$ directly, independently of the reduced $H$-based functional $\rho(u, v)$.

---

## 5. Failure Threshold and Execution Disposition

- **Zero tolerance:** Any single mismatch in any stage raises `ExactAuditFailure`, prints `STAGE <name> FAIL <witness>`, marks all later stages `NOT_RUN`, and exits `0` with `VERDICT SCIENTIFIC_FAIL` so the negative record is preserved and reproducible. Unexpected runtime exceptions, custody failures, or timeouts exit nonzero and require the `POLICY.md` abandoned-pin disposition.
- **Execution environment:** Clean checkout of the publicly read-back pin commit, Python $\ge 3.10$, `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`, timeout $600$ seconds. Exact stdout is saved as `EXPECTED.txt`, neutral environment metadata is recorded in `RUN.md`, and scientific conclusions (followed by post-run comparison against primary `#1525` and two-architecture CI replay) are recorded in `RESULT.md`.

---

## 6. Action Layer and Interpretation

- **Action layer:** `L1` only (`PUBLIC / NON-CANONICAL / L1`).
- **Interpretation boundary:** Ranks $3$ and $4$ count rational linear wave-summary dimensions for fixed horizons $\{0, 2\}$ and $\{0, 1, 2\}$ with known initial tapes $(a_0, a_1)$ and spectator variables; they do not count bits, native $\mathbb{F}_5$ coordinates, physical sensors, or spatial dimensions, nor do they assert all-time autonomous wave compression, a third contact, native compilation, physical admission, or Canon promotion.
