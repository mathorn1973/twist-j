# Result: P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2 (`PARTIAL / STOP`, `NOT ABANDONED`)

**PUBLIC / NON-CANONICAL / L1 — Preserved Negative Report for `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2` (`VERDICT SCIENTIFIC_FAIL`, Superseded by `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3`)**

- **Issue:** [#1528](https://github.com/mathorn1973/twist-j/issues/1528)
- **Primary Lane:** [#1525](https://github.com/mathorn1973/twist-j/issues/1525) (`notes/C-HB-REFRESH-MEMORY-BOUNDARY-N`)
- **Program:** [#1506](https://github.com/mathorn1973/twist-j/issues/1506) / [#1548](https://github.com/mathorn1973/twist-j/issues/1548)
- **Owner:** `Antigravity-20261017-v103-hb-refresh-memory-audit`
- **Pin Commit:** `453e4404bf987f7b5747b5bb59351ee459dade7f` ([#1528 comment 6226130073](https://github.com/mathorn1973/twist-j/issues/1528#issuecomment-6226130073))
- **Predecessor Probe:** `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` (`bda14aabb495be1db5790c86b6a68d6721cb1fab` / `475a033091db921b28fb409707353ef49870050e`, `PARTIAL / STOP`, `NOT ABANDONED`)
- **First Formal Run Output (`EXPECTED.txt`):** `759` bytes, `9` lines, SHA-256 `4c439ab5d11b078564fee62125abedfe7abbeb02aefaca38cbff99d982be0c7c`
- **Disposition:** `PARTIAL / STOP` (`NOT ABANDONED`), preserved intact as a completed negative report under `POLICY.md` and superseded by `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3`.

## 1. Recorded First Formal Run Output

```text
PROBE P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2
SCOPE PUBLIC NON-CANONICAL L1 independent-code-audit
STAGE custody PASS files=7 sources=17
STAGE geometry_and_operators PASS sites=705 amp_dim=1426 stencil=60 directed_edges=28954 h=1/324,1/54,1/54,0 kappa=-145483/10497600,-173653/10497600
STAGE refresh_identities_target1 PASS basis_inputs=1426 refresh_coefficients=7130 inverse_compositions=2852
STAGE rank_minors_and_criteria_target2 PASS rank_02=3 det3=-1/1749600 rank_012=4 det4=1/5668704000 guard_separations=18
STAGE far_counterexample_target3 PASS far_rho2_plus=-1/1049760 far_work_plus=419903/1049760 far_work_minus=83981/209952 near_rho1_plus=-1/3240
STAGE finite_contact_predictor_target4 FAIL missing-two-kind-zero_cost_accept
VERDICT SCIENTIFIC_FAIL
```

## 2. Exact Diagnosis of the Stage 6 Coverage Check Failure

1. **Stages 1–5 Passed Completely:**
   - `STAGE custody PASS files=7 sources=17`
   - `STAGE geometry_and_operators PASS sites=705 amp_dim=1426 stencil=60 directed_edges=28954 h=1/324,1/54,1/54,0 kappa=-145483/10497600,-173653/10497600`
   - `STAGE refresh_identities_target1 PASS basis_inputs=1426 refresh_coefficients=7130 inverse_compositions=2852`
   - `STAGE rank_minors_and_criteria_target2 PASS rank_02=3 det3=-1/1749600 rank_012=4 det4=1/5668704000 guard_separations=18`
   - `STAGE far_counterexample_target3 PASS far_rho2_plus=-1/1049760 far_work_plus=419903/1049760 far_work_minus=83981/209952 near_rho1_plus=-1/3240`
2. **Stage 6 (`finite_contact_predictor_target4`):**
   - All $50$ signed-source constants, all $50 \times 1410 = 70500$ wave-work linear coefficients, and all $50$ reduced $(\rho, \delta)$ contact shifts passed.
   - All $2000$ single-contact guarded cases (including all five outcome regimes `zero_cost_accept`, `pos_work_accept`, `neg_work_accept`, `lower_refusal`, `upper_refusal` and both signs) passed.
   - All $480$ two-contact guarded cases passed every reduced-predictor check (`pred-delta1`, `pred-kind1`, `pred-rho2`, `pred-delta2`, `pred-kind2`, `pred-rho2-after`, `pred-work`, `pred-battery`, `pred-signs`) and every energy conservation check (`e1-conservation`, `f1-energy`, `f2-energy`, `e2-conservation`, `e2-joint-store`, `w2-plus-b2`).
   - At line 1266 of `break.py` (immediately after the $480$-case loop completed), the self-imposed regime-coverage assertion `check(two_kinds["zero_cost_accept"] > 0, stage, "missing-two-kind-zero_cost_accept")` fired because the first source pair in `source_pairs` (line 1166) had been written as `((0, 3), (2, 4))` instead of `((0, 4), (2, 4))`. Under $\ell(0..4) = (0, 1, 2, -2, -1)$ and $\eta_2(q, r) = (\ell(q)/2, (\ell(r)+1)/2)$, the unique zero-source label in $\mathbb{F}_5^2$ is $(0, 4)$ ($\ell(4) = -1 \implies \eta_2(0, 4) = (0, 0)$), whereas $(0, 3)$ has $\ell(3) = -2 \implies \eta_2(0, 3) = (0, -1/2) \ne (0, 0)$.

## 3. Policy Disposition (`PARTIAL / STOP`, `NOT ABANDONED`) and Successor

Per `POLICY.md`, because `verify.py` exited `0` with empty `stderr` and printed `VERDICT SCIENTIFIC_FAIL`, `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2` is a completed negative gate (`PARTIAL / STOP`, `NOT ABANDONED`) and is preserved intact on `origin/probe/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2` with its immutable pin (`453e4404bf987f7b5747b5bb59351ee459dade7f`), `EXPECTED.txt`, `RUN.md`, and `RESULT.md`.

It is superseded by the fresh successor probe `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3`, which replaces `((0, 3), (2, 4))` with `((0, 4), (2, 4))` in `source_pairs` while keeping the information barrier against primary `notes/C-HB-REFRESH-MEMORY-BOUNDARY-N` intact.
