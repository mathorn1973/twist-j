# Result: P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3

**PUBLIC / NON-CANONICAL / L1 — Independent Audit of Two-Contact Wave-Summary Memory Ranks and Refresh Laws on the 705-Site $D_3$ Carrier**

- **Issue:** [#1528](https://github.com/mathorn1973/twist-j/issues/1528) (`5836` UTF-8 bytes, SHA-256 `1c93022e9c24d4e35c290bccb65afe8e14bedfdaaa472ddfbb0cb02f3da80f80`)
- **Primary Lane Audited:** [#1525](https://github.com/mathorn1973/twist-j/issues/1525) (`notes/C-HB-REFRESH-MEMORY-BOUNDARY-N`, primary owner `ChatGPT-20261015-hb-refresh-memory-boundary`, primary `PREREG.md` at `8ab77c73426a6a65a13ddb8798390df534e64814`)
- **Program:** [#1506](https://github.com/mathorn1973/twist-j/issues/1506) / [#1548](https://github.com/mathorn1973/twist-j/issues/1548) (`13858` UTF-8 bytes, SHA-256 `c209686fede612501394f969d5052518d35c95be0523c9e22619cbd19984fd87`)
- **Audit Owner:** `Antigravity-20261017-v103-hb-refresh-memory-audit`
- **Public Claim Receipt:** [#1528 comment 6225725304](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6225725304)
- **Preserved Predecessors:**
  - `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` (`origin/probe/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1`, pin `bda14aabb495be1db5790c86b6a68d6721cb1fab`, negative report `475a033091db921b28fb409707353ef49870050e`, `PARTIAL / STOP`, `NOT ABANDONED`; receipts [#1528 comment 6225908014](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6225908014) and [#1528 comment 6226034498](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6226034498))
  - `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2` (`origin/probe/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2`, pin `453e4404bf987f7b5747b5bb59351ee459dade7f`, negative report `c8d4fd675490feeeeab06a15a8b1ff5fa06bdd29`, `PARTIAL / STOP`, `NOT ABANDONED`; receipts [#1528 comment 6226130073](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6226130073) and [#1528 comment 6226180715](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6226180715))
- **Successor Pin Commit:** `299b1c4b6fa127ded3f5aea3bede9ca56b50634d` ([#1528 comment 6226242486](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6226242486))
- **First Formal Run Output (`EXPECTED.txt`):** `819` bytes, `9` lines, SHA-256 `8a2c91f83760bfce9752b4624421e770cbfd0fb69ae65cde475a83087e9574aa`
- **Verdict:** `VERDICT PASS` (all four audit targets independently proved and verified over $\mathbb{Q}$)

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
