# Result: P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3

**PUBLIC / NON-CANONICAL / L1 — Independent Audit of Two-Contact Wave-Summary Memory Ranks and Refresh Laws on the 705-Site $D_3$ Carrier**

- **Issue:** [#1528](https://github.com/mathorn1973/twist-j/issues/1528) (`5836` UTF-8 bytes, SHA-256 `1c93022e9c24d4e35c290bccb65afe8e14bedfdaaa472ddfbb0cb02f3da80f80`)
- **Primary Lane Audited:** [#1525](https://github.com/mathorn1973/twist-j/issues/1525) / Draft PR [#1527](https://github.com/mathorn1973/twist-j/pull/1527) (`notes/C-HB-REFRESH-MEMORY-BOUNDARY-N`, primary owner `ChatGPT-20261015-hb-refresh-memory-boundary` / `ChatGPT-20261015-contact-memory`, input pin `8ab77c73426a6a65a13ddb8798390df534e64814`, result head `4663229d9c1ba7a70ac03194294b03a0944bb522`)
- **Program:** [#1506](https://github.com/mathorn1973/twist-j/issues/1506) / [#1548](https://github.com/mathorn1973/twist-j/issues/1548) (`13858` UTF-8 bytes, SHA-256 `c209686fede612501394f969d5052518d35c95be0523c9e22619cbd19984fd87`)
- **Audit Owner:** `Antigravity-20261017-v103-hb-refresh-memory-audit`
- **Public Claim Receipt:** [#1528 comment 6225725304](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6225725304)
- **Preserved Predecessors:**
  - `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` (`origin/probe/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1`, pin `bda14aabb495be1db5790c86b6a68d6721cb1fab`, negative report `475a033091db921b28fb409707353ef49870050e`, `PARTIAL / STOP`, `NOT ABANDONED`; receipts [#1528 comment 6225908014](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6225908014) and [#1528 comment 6226034498](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6226034498))
  - `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2` (`origin/probe/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2`, pin `453e4404bf987f7b5747b5bb59351ee459dade7f`, negative report `c8d4fd675490feeeeab06a15a8b1ff5fa06bdd29`, `PARTIAL / STOP`, `NOT ABANDONED`; receipts [#1528 comment 6226130073](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6226130073) and [#1528 comment 6226180715](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6226180715))
- **Successor Pin Commit:** `299b1c4b6fa127ded3f5aea3bede9ca56b50634d` ([#1528 comment 6226242486](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6226242486))
- **Pre-Comparison First-Run Record Commit:** `cff1a32e30a12a5d1ecf96db1a49b8a9026303f3` ([#1528 comment 6226267706](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6226267706))
- **First Formal Run Output (`EXPECTED.txt`):** `819` bytes, `9` lines, SHA-256 `8a2c91f83760bfce9752b4624421e770cbfd0fb69ae65cde475a83087e9574aa`
- **Verdict:** `VERDICT PASS` — **ACCEPT** primary `notes/C-HB-REFRESH-MEMORY-BOUNDARY-N` ([#1525](https://github.com/mathorn1973/twist-j/issues/1525) / PR [#1527](https://github.com/mathorn1973/twist-j/pull/1527)) at `PUBLIC / NON-CANONICAL / L1` (`candidate-T` proofs and `candidate-C` finite evidence).

---

## 1. Recorded First Formal Run Output

```text
PROBE P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3
SCOPE PUBLIC NON-CANONICAL L1 independent-code-audit
STAGE custody PASS files=7 sources=20
STAGE geometry_and_operators PASS sites=705 amp_dim=1426 stencil=60 directed_edges=28954 h=1/324,1/54,1/54,0 kappa=-145483/10497600,-173653/10497600
STAGE refresh_identities_target1 PASS basis_inputs=1426 refresh_coefficients=7130 inverse_compositions=2852
STAGE rank_minors_and_criteria_target2 PASS rank_02=3 det3=-1/1749600 rank_012=4 det4=1/5668704000 guard_separations=18
STAGE far_counterexample_target3 PASS far_rho2_plus=-1/1049760 far_work_plus=419903/1049760 far_work_minus=83981/209952 near_rho1_plus=-1/3240
STAGE finite_contact_predictor_target4 PASS single_cases=2000 two_cases=480 single_ZeroPosNegLowUp=80,970,100,750,100 two_AA_AR_RA_RR=139,157,24,160
VERDICT PASS
```

---

## 2. Summary of Independent Audit Findings (Pre-Exposure Record)

1. **Carrier and Operator Custody (`geometry_and_operators`):**
   - Constructed the 60-point five-shell stencil $B$ (weight sum $288/324 = 8/9$), $B_0 = \{0\} \cup B$ ($61$ points), and $D = Y + B_0 + B_0$ ($705$ sites, $28954$ directed interior edges), matching `DOMAIN.tsv` (`5029` bytes, SHA-256 `2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0`) byte-for-byte.
   - Verified $H + L_D = 2I$, symmetry of $H$ and $L_D$, $A^T J_0 = -\frac{1}{5}\mathbf{1}_2 e_4^T$, $K - \frac{1}{2}I = \frac{1}{2}J_0$, $K J_0 = J_0$, $K P = \frac{1}{2}P$, $G = \frac{1}{5}\begin{pmatrix} 4 & -1 \\ -1 & 4 \end{pmatrix}$, $M = A^T P$, $h^T = e_4^T H P = \frac{1}{324}(1, 6, 6, 0) = (\frac{1}{324}, \frac{1}{54}, \frac{1}{54}, 0)$, and $\kappa^T = \frac{1}{5}e_4^T(A - \frac{1}{2}H K H A) = -\frac{(145483, 173653)}{10497600}$.
2. **Target 1 — Exact Refresh Identities (`refresh_identities_target1`):**
   - Across all $1426$ standard basis inputs of $\mathbb{Q}^{1426}$ ($705$ $u$-sites, $705$ $v$-sites, $16$ tape entries), verified two-sided invertibility $F^{-1}(F(X)) = X = F(F^{-1}(X))$ ($2852$ compositions), the linear port-coupling identity $w + u - H v = 2 P(a_0 + b_{\mathrm{out}})$, and all $5 \times 1426 = 7130$ exact rational coefficients of
     $$\rho(FX) = \gamma(X)\mathbf{1}_2 + 2 M a_0, \qquad \gamma(FX) = \delta(X) - \frac{1}{5} h^T a_0, \qquad \rho(F^2 X) = \left(\delta(X) - \frac{1}{5} h^T a_0\right)\mathbf{1}_2 + 2 M a_1.$$
3. **Target 2 — Fixed Linear Wave-Summary Kernel Criteria and Rank Certificates (`rank_minors_and_criteria_target2`):**
   - Proved in `PROOF.md` (Theorem 2, for both exact pre-guard work and Boolean guard decisions across admissible $(b, B)$) that prediction at horizon $\{0, 2\}$ holds iff $\ker L \subseteq \ker(\rho, \delta)$ (sharp minimum rank $3$) and at horizon $\{0, 1, 2\}$ holds iff $\ker L \subseteq \ker(\rho, \gamma, \delta)$ (sharp minimum rank $4$).
   - Verified the $3 \times 3$ minor on $((0, s_0), (0, s_1), (0, \delta_{(10,0,0)}))$ with $\det = \frac{3}{5}\left(-\frac{1}{10 \cdot 324^2}\right) = -\frac{3}{5248800} = -\frac{1}{1749600}$ and the $4 \times 4$ minor inserting $(0, \delta_{(6,0,0)})$ as third column with $\det = \frac{3}{5}\left(-\frac{1}{10 \cdot 324}\right)\left(-\frac{1}{10 \cdot 324^2}\right) = \frac{3}{17006112000} = \frac{1}{5668704000}$, plus $18$ explicit Boolean guard separations across $n \in \{0, 1, 2\}$.
4. **Target 3 — Equal-Energy, Equal-Tape Opposite-Velocity Counterexample (`far_counterexample_target3`):**
   - Verified that $X_\pm = (u = 0, v = \pm \delta_{(10,0,0)}, 0, 0, 0, 0)$ have $\rho(X_\pm) = (0, 0)^T$, $\gamma(X_\pm) = 0$, $E_{\mathrm{full}}(F^n X_\pm) = 1/2$, and zero four-slot tapes at $n = 0, 1, 2$, while $\delta(X_\pm) = \mp \frac{1}{1049760}$ and $\rho(F^2 X_\pm) = \mp \frac{1}{1049760}\mathbf{1}_2$, producing distinct accepted second-contact works $\frac{419903}{1049760} \ne \frac{419905}{1049760}$ (`83981/209952` in lowest terms) under $A(1, 0)^T$ ($\sigma = +1, B = 1, b = 1/2$).
5. **Target 4 — Finite Two-Contact Predictor $\xi = (\rho, \delta)$ (`finite_contact_predictor_target4`):**
   - Verified all $50$ signed-source constants, all $50 \times 1410 = 70500$ wave-work linear coefficients, and all $50$ reduced $(\rho, \delta)$ contact shifts.
   - Verified exact agreement between the reduced predictor and full $1426$-coordinate evolution across all $2000$ single-contact guarded cases (`zero_cost_accept=80`, `pos_work_accept=970`, `neg_work_accept=100`, `lower_refusal=750`, `upper_refusal=100`) and all $480$ two-contact guarded cases (`AA=139`, `AR=157`, `RA=24`, `RR=160`).

---

## 3. Post-Run Comparison Against Primary `notes/C-HB-REFRESH-MEMORY-BOUNDARY-N` ([#1525](https://github.com/mathorn1973/twist-j/issues/1525) / PR [#1527](https://github.com/mathorn1973/twist-j/pull/1527))

### 3.1 Exposure Chronology and Custody Audit of Primary `#1525`

1. **Strict Pre-Exposure Barrier:** Primary `verify.py`, `PROOF.md`, `EXPECTED.txt`, `RUN.md`, `RESULT.md`, `PROMO.md`, and `#1525` comments were opened **only after** `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3` was pinned (`299b1c4b6fa127ded3f5aea3bede9ca56b50634d`), publicly read back ([#1528 comment 6226242486](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6226242486)), executed (`stdout_sha256: 8a2c91f83760bfce9752b4624421e770cbfd0fb69ae65cde475a83087e9574aa`), committed (`cff1a32e30a12a5d1ecf96db1a49b8a9026303f3`), pushed, and recorded ([#1528 comment 6226267706](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6226267706)).
2. **Primary Pin Integrity:** All five pinned files of `notes/C-HB-REFRESH-MEMORY-BOUNDARY-N` at input pin `8ab77c73426a6a65a13ddb8798390df534e64814` remain byte-identical at result head `4663229d9c1ba7a70ac03194294b03a0944bb522`:
   - `CODE_SHA256SUMS`: `305` bytes, SHA-256 `dcf0c04289447dd2f4eac62b5102553ac62691e562cb5eb0f17ccc92e90a4702`
   - `PREREG.md`: `8911` bytes, SHA-256 `7fea37b85b371702f4a9a18ee75ea237d3ccd2eb7d7b96549d115f9caadfa7d4`
   - `PROOF.md`: `9343` bytes, SHA-256 `95d2e4d838473c87f01b013f9de87f4b8f59bf5f1de021c1bb076f8450fa7c36`
   - `SOURCES.tsv`: `2106` bytes, SHA-256 `21e6e0af66bcad6e953ac1aee0c35c881baf45385fd2b75623e628df747f27d7`
   - `verify.py`: `10594` bytes, SHA-256 `14efe377349b233d545b39f3160604fe28ee195a496335f6fb85be8cbb93b5e2`
3. **Primary Result Files at `4663229d9c1ba7a70ac03194294b03a0944bb522`:**
   - `EXPECTED.txt`: `533` bytes, SHA-256 `4c01c1dbe5e5dd4282d9c37543fe492c13c8835845a10d05e32ef9f77581a030`
   - `RUN.md`: `1553` bytes, SHA-256 `b9797d129e1b7d90057e436aad65899e7786c457d5b4b01d7abec508fce0cf09`
   - `RESULT.md`: `4374` bytes, SHA-256 `03528efc06b6623a31c5a9f914c4108ddfe4e7f77ccb9c55c3b31096ac8c0aad`
   - `PROMO.md`: `2810` bytes, SHA-256 `bd5b189cbd4fb3e390d5dae9f43b9d62be2da2a9a56b21981445d7d08e726131`
   - `README.md`: `1608` bytes, SHA-256 `96ed2950aefd349d541b5fc5cd43a74e1abc954ded3ea31f2200f707d71fb390`

### 3.2 Item-by-Item Scientific Comparison

| Audit Item | Primary `#1525` (`notes/C-HB-REFRESH-MEMORY-BOUNDARY-N`) | Independent Audit (`P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3`) | Comparison Status |
| :--- | :--- | :--- | :--- |
| **Domain $D$ & Dimension** | $705$ sites (`2e9b77cf...d8a7c0`), `dim = 1426`, $60$-point stencil $B$ | $705$ sites (`2e9b77cf...d8a7c0`), `amp_dim = 1426`, $60$-point stencil $B$, $28954$ directed edges | **Exact Match** |
| **Operators $G, M, h^T, \kappa^T$** | $G = \frac{1}{5}\begin{pmatrix} 4 & -1 \\ -1 & 4 \end{pmatrix}$, $h^T = (\frac{1}{324}, \frac{1}{54}, \frac{1}{54}, 0)$, $\kappa^T = -\frac{(145483, 173653)}{10497600}$ | Identical exact rational matrices/rows; $\kappa^T$ also cross-checked against $\Omega_{i,j}$ and $70500$ linear work coefficients | **Exact Match** |
| **Target 1 ($7130$ Refresh Coefficients)** | Assembles $1426$ linear rows of $F$ (`Frows`) and pulls $\rho, \gamma$ through `Frows` and `Frows^2` ($5 \times 1426 = 7130$ equalities) | Evaluates dynamical step $F$ and $F^2$ on all $1426$ basis states, checking all $7130$ coefficients + $2852$ $F/F^{-1}$ inverse compositions + port-coupling identity | **Exact Match** (independent algorithm) |
| **Target 2 (Minors & Kernel Criteria)** | $\det_3 = -\frac{1}{1749600}$, $\det_4 = \frac{1}{5668704000}$; proves $\ker L \subseteq \ker(\rho,\delta)$ (rank $3$) and $\ker L \subseteq \ker(\rho,\gamma,\delta)$ (rank $4$) for exact $\rho$ / pre-guard work | $\det_3 = -\frac{3}{5248800} = -\frac{1}{1749600}$, $\det_4 = \frac{3}{17006112000} = \frac{1}{5668704000}$; proves criteria for both pre-guard work and Boolean guard decisions (`guard_separations=18`) | **Exact Match** (plus Boolean guard separation) |
| **Target 3 (Far Counterexample)** | $X_\pm = (0, \pm\delta_{(10,0,0)}, 0)$: $\rho=\gamma=0, E=1/2$, zero tapes through $F^2$, $\rho(F^2 X_\pm) = \mp\frac{1}{1049760}\mathbf{1}_2$, works $\frac{419903}{1049760}, \frac{83981}{209952}$ | Identical exact trajectories, energies, zero tapes, $\delta(X_\pm) = \mp\frac{1}{1049760}$, $\rho(F^2 X_\pm)$, and works $\frac{419903}{1049760}, \frac{83981}{209952}$, plus near witness $(6,0,0)$ | **Exact Match** |
| **Target 4 ($2000$ 1-Contact & $480$ 2-Contact Cases)** | $2000$ 1-contact & $480$ 2-contact cases (`00:95, 01:17, 10:129, 11:239`); wave energy via $(u\cdot u + v\cdot v - u\cdot H v)/2$ | Independently chosen occupied waves, nonzero tapes, stocks, and 4 source pairs: $2000$ 1-contact (`80,970,100,750,100`) & $480$ 2-contact (`AA:139, AR:157, RA:24, RR:160`); wave energy directly from $L_D$ via $(\|v-u\|^2 + u^T L_D v)/2$ | **Exact Match** on all laws across two distinct witness families |

### 3.3 Final Audit Disposition

- **Verdict on Primary Candidate `C-HB-REFRESH-MEMORY-BOUNDARY-N` ([#1525](https://github.com/mathorn1973/twist-j/issues/1525) / Draft PR [#1527](https://github.com/mathorn1973/twist-j/pull/1527)):** **ACCEPT** within its declared `PUBLIC / NON-CANONICAL / L1` boundary (`candidate-T` proofs and `candidate-C` finite evidence, now backed by independent code and two-architecture CI replay in `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3`). No mathematical, custody, or scope defect was found in `notes/C-HB-REFRESH-MEMORY-BOUNDARY-N`.
- **Interpretation and Authority Boundary:** Ranks $3$ and $4$ count fixed rational linear wave-summary dimensions for horizons $\{0, 2\}$ and $\{0, 1, 2\}$ with separately known initial tapes $(a_0, a_1)$ and spectator variables; they do not assert $\delta(F^2 X)$ closure, autonomous all-time wave compression, finite-bit or native $\mathbb{F}_5$ sensor counts, physical admission, or Canon promotion. `Public Canon v102` (`canon-v102`) remains unchanged.
