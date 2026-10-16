# Result Report: `P-TWO-USE-READOUT-FAILURE-REGRESSION-1`

Status: ABANDONED

**PUBLIC / NON-CANONICAL / L1 / 2026-10-15.**
Original work Apache-2.0, A. M. Thorn.
Issue: [#1526](https://github.com/mathorn1973/twist-j/issues/1526), parent [#1506](https://github.com/mathorn1973/twist-j/issues/1506).

---

## 1. Abandonment Disposition (`POLICY.md` §3)

1. **Frozen pin (`e7017fbf54ad1c3cb86f8ed456bc32fd44027b02`):**
   - `CODE_SHA256SUMS`: `305` bytes, SHA-256 `da59cc4379f3d618175d6303107b61d79597e3b20cefb448a35b53ee4f7d8e5b`
   - `PREREG.md`: `10667` bytes, SHA-256 `38d9cc907b62247075840f91ac470154cd7c1812557833e591e5e3b14c37de98`
   - `PROOF.md`: `9639` bytes, SHA-256 `b9356ef881c33d1e56df739a376d67383f896d3896936dd43791b5615d4b88d7`
   - `SOURCES.tsv`: `2859` bytes, SHA-256 `482b3f65af78211fa07f9a3307fe60e95d35a48f02a357c6c17201120c01b06c`
   - `verify.py`: `34275` bytes, SHA-256 `2ec41aca08e123689ee5516aada1b0aa0853d0404b2fddab265779f4d84fd853`
2. **Why the formal gate did not complete:**
   - On the first execution of `probes/P-TWO-USE-READOUT-FAILURE-REGRESSION-1/verify.py` at pin `e7017fbf54ad1c3cb86f8ed456bc32fd44027b02`, `run_r01_custody_and_historical_verifier_ast()` used `ast.walk(run_full_audit_fn)` to collect `CURRENT_STAGE` assignments in `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/verify.py` without sorting by line number. Because `ast.walk` traverses AST nodes in breadth-first order, it visited the top-level assignment at line `1853` (`(1853, 'full_state_comparison')`) before the nested `for`-loop body assignment at line `1845` (`(1845, 'attr:__name__')`), raising `AssertionError: R01.historical_stage_assignments: expected=[(1845, 'attr:__name__'), (1853, 'full_state_comparison')], actual=[(1853, 'full_state_comparison'), (1845, 'attr:__name__')]` at line `329` (`exit_code: 1`) before reaching `R02`, `R03`, or `R04`.
3. **Permanent consumption of identifier and retargeted successor:**
   - Per `POLICY.md` §3 ("Abandoned pins"), all five pinned files at `e7017fbf54ad1c3cb86f8ed456bc32fd44027b02` remain unchanged (`0` diff lines), no `EXPECTED.txt` or `RUN.md` is committed, and the identifier `P-TWO-USE-READOUT-FAILURE-REGRESSION-1` is permanently consumed and must not be reused.
   - The audit is retargeted under the new identifier `P-TWO-USE-READOUT-FAILURE-REGRESSION-2` (`probes/P-TWO-USE-READOUT-FAILURE-REGRESSION-2/` on branch `probe/P-TWO-USE-READOUT-FAILURE-REGRESSION-2`) with its own fresh preregistration pin.
