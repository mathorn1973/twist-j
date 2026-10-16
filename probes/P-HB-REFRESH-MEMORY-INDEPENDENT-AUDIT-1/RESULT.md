# Frozen independent audit disposition: P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1

Status: PARTIAL / STOP — audit-fixture arithmetic typo in redundant expanded-denominator literal `det4-value`; factored `det4-target` passed; Stages 5–6 `NOT_RUN`.

**PUBLIC / NON-CANONICAL / L1 / STOP.**
Original work Apache-2.0, A. M. Thorn, 2026-10-17.
Owner session: `Antigravity-20261017-v103-hb-refresh-memory-audit`.
Issue: [#1528](https://github.com/mathorn1973/twist-j/issues/1528).

The first execution of public pin `bda14aabb495be1db5790c86b6a68d6721cb1fab` completed with return code `0`, empty stderr (`0` bytes), and exact 628-byte stdout (`EXPECTED.txt`, SHA-256 `b102ec4e67f71aeea94db2b0e716497d505fadf254f8de5874f3e4ba50a80224`):

```text
PROBE P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1
SCOPE PUBLIC NON-CANONICAL L1 independent-code-audit
STAGE custody PASS files=7 sources=14
STAGE geometry_and_operators PASS sites=705 amp_dim=1426 stencil=60 directed_edges=28954 h=1/324,1/54,1/54,0 kappa=-145483/10497600,-173653/10497600
STAGE refresh_identities_target1 PASS basis_inputs=1426 refresh_coefficients=7130 inverse_compositions=2852
STAGE rank_minors_and_criteria_target2 FAIL det4-value: actual=Fraction(1, 5668704000) expected=Fraction(1, 566231040000)
STAGE far_counterexample_target3 NOT_RUN
STAGE finite_contact_predictor_target4 NOT_RUN
VERDICT SCIENTIFIC_FAIL
```

This is a completed, byte-recorded negative gate report under the frozen failure contract. It is **not** `ABANDONED`: `EXPECTED.txt` and `RUN.md` exist and preserve the completed exact report. The identifier `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` and pin `bda14aabb495be1db5790c86b6a68d6721cb1fab` are consumed, and all eight pinned files remain unchanged.

## What this run establishes and why `det4-value` fired

1. **Completed passing stages in this run:**
   - `STAGE custody`: all 7 pinned files and 14 `SOURCES.tsv` records verified.
   - `STAGE geometry_and_operators`: all $705$ sites of $D = Y + B_0 + B_0$, $1426$ full wave/tape coordinates, $60$-point stencil, $28,954$ symmetric directed off-diagonal stencil edges, $H + L_D = 2I$, Lemma 1 projector identities, $G$, $M$, $h^T = (1/324, 1/54, 1/54, 0)$, and $\kappa^T = -(145483, 173653)/10497600$ verified.
   - `STAGE refresh_identities_target1` (**Target 1**): all $1426$ full basis inputs, $2852$ two-way inverse compositions of $F$ and $F^{-1}$, the linear energy-coupling identity, and all $5 \times 1426 = 7130$ exact coefficient equalities for $\rho(FX)$, $\gamma(FX)$, and $\rho(F^2 X)$ passed with zero discrepancy.
2. **Exact cause of `STAGE rank_minors_and_criteria_target2 FAIL det4-value`:**
   - In `break.py` lines 476–482, `det3` passed both `check_eq(det3, MINOR_3X3_TARGET, ...)` and `check_eq(det3, Q(-3, 5248800), ...)` (`-1/1749600`).
   - In `break.py` lines 501–502, `det4` was first compared against the factored formula `MINOR_4X4_TARGET = Q(3, 5) * Q(-1, 10 * 324) * Q(-1, 10 * 324 * 324)` (`check_eq(det4, MINOR_4X4_TARGET, stage, "det4-target")`), which **passed** with exact value
     $$\det(M_4) = \frac{3}{5} \cdot \left(-\frac{1}{3240}\right) \cdot \left(-\frac{1}{1049760}\right) = \frac{3}{17006112000} = \frac{1}{5668704000}.$$
   - The immediately following line 503 (`check_eq(det4, Q(3, 1698693120000), stage, "det4-value")`) contained an audit-fixture hand-multiplication typo in the expanded denominator ($5 \cdot 3240 \cdot 1049760 = 17,006,112,000$, whereas the author's hand expansion in `PROOF.md` and `break.py` line 503 wrote $1,698,693,120,000$).
   - Thus the factored Target 2 determinant formula $(3/5)(-1/(10 \cdot 324))(-1/(10 \cdot 324^2))$ stated in [#1528](https://github.com/mathorn1973/twist-j/issues/1528) and primary `PREREG.md` is **confirmed**, and the failure is solely an internal arithmetic typo in the audit's redundant expanded-denominator literal.
3. **Unreached stages:**
   - Because `break.py` halts on the first failed assertion, the remainder of Stage 4 and Stages 5–6 (`far_counterexample_target3`, `finite_contact_predictor_target4`) were `NOT_RUN` in `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1`.

## Disposition and Successor

No primary `verify.py`, `PROOF.md`, `EXPECTED.txt`, `RUN.md`, `RESULT.md`, or `#1525` result discussion was opened before or during this run. To complete the full six-stage audit without modifying or reusing this consumed pin, this completed negative report is preserved intact on `probe/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1`, and the retargeted audit is carried out on the fresh successor branch and directory `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2`, which cites this preserved predecessor before its own immutable pin.
