# Result: `P-TWO-USE-READOUT-FAILURE-REGRESSION-2`

**Status: NON-CANONICAL**
**Action Layer:** `L1` (finite mathematical and software interface regression/diagnostic audit; not Canon, not `T`, not `C`).
**Issue:** [#1526](https://github.com/mathorn1973/twist-j/issues/1526), under parent program [#1506](https://github.com/mathorn1973/twist-j/issues/1506).
**Author:** A. M. Thorn (`thorn@twistj.com`), Apache-2.0.
**Predecessor disclosure:** Retargeted successor to `P-TWO-USE-READOUT-FAILURE-REGRESSION-1` (pinned at `e7017fbf54ad1c3cb86f8ed456bc32fd44027b02` on `probe/P-TWO-USE-READOUT-FAILURE-REGRESSION-1` and closed with `Status: ABANDONED` at `d94670e18c6882e20a2cd6db04292dc49058ae95` per `POLICY.md` §3 after its first post-pin run exited `1` at `R01.historical_stage_assignments` due to `ast.walk` breadth-first AST traversal order).

---

## 1. Custody and Execution Summary

- **Base commit (`main`):** `b79143fb00839b870686f6cea34e174959060df1`
- **Preregistration pin commit:** `0803c167d5e903a216b3cd96d9f7c6fcf4e62345`
- **Public pin/readback receipt:** [#1526 comment `6198956479`](https://github.com/mathorn1973/twist-j/issues/1526#issuecomment-6198956479)
- **Pinned files (0 post-pin modifications):**
  - `PREREG.md`: `8927e738676236c1ef380df1e47eaab598fc2b101ac33be4d9f2f21f619b58f4` (`11288` bytes)
  - `PROOF.md`: `ea5691cace12408fcd552ed464de1aea14d9dc8d9995429c6203013eae701523` (`9830` bytes)
  - `SOURCES.tsv`: `482b3f65af78211fa07f9a3307fe60e95d35a48f02a357c6c17201120c01b06c` (`2859` bytes)
  - `verify.py`: `65ec7e05b0b6c6089be5424cff33efd163967e1dced6b4c50bed6119209173fa` (`34283` bytes)
  - `CODE_SHA256SUMS`: `31016599bd35380c655e3ef61eb7c35f68f96babd7b8ce184b9dd5f0bbad7a9e` (`305` bytes)
- **First exact pinned run (`aarch64`, `Darwin`, Python `3.13.13`):**
  - `exit_code = 0`, `stderr_bytes = 0` (`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`)
  - `EXPECTED.txt`: `5bc83612d7364bd85c5b967a3187a96d0228f604f7bc994605a39670574e8f08` (`3631` bytes, `22` lines)
- **Upstream custody (`R01`):** All 4 local pinned files and all 19 upstream `SOURCES.tsv` records (`probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/` and normative repository files at `b79143fb00839b870686f6cea34e174959060df1`) passed pre-import and post-harness byte-count and SHA-256 verification (`upstream_files_modified=0`).

---

## 2. Section A: Five Semantic Rejections (`S1`–`S5`) and Five Positive Controls (`P1`–`P5`)

Using $z = (0,0,0,0)$ and $e = (1,0,0,0)$ against the unmodified `DirectPortReadout`, `decode_port_vectors`, and `direct_source_reader` imported read-only from `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/apparatus.py`:

### 2.1 Five semantic rejection specimens (`S1`–`S5`)

Every specimen constructed a valid `DirectPortReadout` and raised `ValueError` at `direct_source_reader(record)` with the exact frozen message:

| Specimen ID | `DirectPortReadout` input | Raised exception | Exact `ValueError` message | Status |
|---|---|---|---|---|
| `S1_REFUSED_A_NONZERO_B0` | `DirectPortReadout(e, z, sigma_A=1)` | `ValueError` | `"Inconsistent refused sigma_A=+1 with non-zero b0"` | PASS |
| `S2_ZERO_B_SOURCE_NONZERO_RESIDUAL` | `DirectPortReadout(z, e, d=(0, 4))` | `ValueError` | `"Inconsistent d=(0,4) with non-zero b2 - D2(alpha_A z_A)"` | PASS |
| `S3_RESIDUAL_INCOMPATIBLE_WITH_D` | `DirectPortReadout(z, e, d=(1, 4))` | `ValueError` | `"Residual b2 - D2(alpha_A z_A) does not match d on ready family"` | PASS |
| `S4_SIGMA_B_CONTRADICTS_ZERO_COST_D` | `DirectPortReadout(z, z, sigma_B=1, d=(0, 4))` | `ValueError` | `"Mismatch between sigma_B and (d, b0, b2) acceptance readout"` | PASS |
| `S5_REFUSED_B_NONZERO_RESIDUAL` | `DirectPortReadout(z, e, sigma_B=1)` | `ValueError` | `"Inconsistent refused Contact B with non-zero residual b2"` | PASS |

### 2.2 Five positive controls (`P1`–`P5`)

| Control ID | Input record | Verified output & scope boundary | Status |
|---|---|---|---|
| `P1_ACCEPTED_ZERO` | `DirectPortReadout(z, z, sigma_A=-1, sigma_B=-1, d=(0, 4))` | `alpha_A=1, alpha_B=1, alpha_B_from_d_b0_b2=1, z_A=(0,0,0,0), z_B=(0,0,0,0)` | PASS |
| `P2_REFUSED_INPUT` | `DirectPortReadout(z, z, sigma_A=1, sigma_B=1, d=(1, 4))` | `alpha_A=0, alpha_B=0, alpha_B_from_d_b0_b2=0, z_A=None, z_B=None` (refusal never returned as accepted zero source) | PASS |
| `P3_UNKNOWN_ACCEPTANCE_ZERO` | `DirectPortReadout(z, z)` | `alpha_A=None, alpha_B=None, alpha_B_from_d_b0_b2=None, z_A=None, z_B=None` (missing context defaults to `None`, never `-1`) | PASS |
| `P4_PARTIAL_CONTRACT_NONZERO_B2_NO_CONTEXT` | `DirectPortReadout(z, R_0 z^{(1)})` with $R_0 z^{(1)} = (-1421/12960, 59/2160, 59/2160, 29/1080)$ | `alpha_B=None, z_B=None` while `alpha_B_z_B=(1/2,0,0,0) != 0`; deliberately partial contract is not a proof of mathematical indistinguishability | PASS |
| `P5_VALID_EXPLICIT_INTEGER_Q4_RECORD` | `DirectPortReadout(e, z)` | `alpha_A=1, z_A=(-154224/21535,-1296/365,-1296/365,-75168/21535)` matching `decode_port_vectors(e, z)`; raw `direct_source_reader(e)` raises `TypeError`; type tag prevents accidental argument confusion and does not authenticate physical provenance | PASS |

---

## 3. Section B: Historical Verifier AST Check (`R01`), Honest Failure-Phase Adapter (`R03`), and Static Non-Interference (`R04`)

1. **Historical verifier preserved untouched (`R01`):**
   Static AST inspection of `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/verify.py` verified that `CURRENT_STAGE` is assigned only at line `1845` (`CURRENT_STAGE = fn.__name__`) and line `1853` (`CURRENT_STAGE = "full_state_comparison"`), that `build_witness_trajectories()` is called at line `1850` while `CURRENT_STAGE` still holds `"run_t19_typed_record_factorization"`, and that `main()` prints `"TYPED_CLOSURE_FAIL remaining_dependent_checks=NOT_RUN comparison=NOT_RUN"` on any `AssertionError`.
2. **Six harness scenarios (`H1`–`H6`) on `run_reporting_adapter` (`R03`):**

   | Scenario ID | `phase_state` | `first_failed_stage` | `audit` | `witnesses` | `comparison` | `remaining` | `completion_marker` | `strict_exit` | Status |
   |---|---|---|---|---|---|---|---|---:|---|
   | `H1_AUDIT_MID_STAGE_T11_FAIL` | `AUDIT` | `run_t11_direct_chronological_and_source_readers` | `FAIL` | `NOT_RUN` | `NOT_RUN` | `NOT_RUN` | `False` | `1` | PASS |
   | `H2_AUDIT_FINAL_STAGE_T19_FAIL` | `AUDIT` | `run_t19_typed_record_factorization` | `FAIL` | `NOT_RUN` | `NOT_RUN` | `NOT_RUN` | `False` | `1` | PASS |
   | `H3_WITNESS_BUILDING_FAIL` | `WITNESS_BUILDING` | `witness_boundary_trajectories` | `PASS` | `FAIL` | `NOT_RUN` | `NOT_RUN` | `False` | `1` | PASS |
   | `H4_COMPARISON_COUNT_MISMATCH` | `COMPARISON_FAILED` | `full_state_comparison` | `PASS` | `PASS` | `FAIL` | `NONE` | `False` | `1` | PASS |
   | `H5_COMPARISON_DIGEST_MISMATCH` | `COMPARISON_FAILED` | `full_state_comparison` | `PASS` | `PASS` | `FAIL` | `NONE` | `False` | `1` | PASS |
   | `H6_COMPLETED_POSITIVE_CONTROL` | `COMPLETED` | `None` | `PASS` | `PASS` | `PASS` | `NONE` | `True` | `0` | PASS |

3. **Static non-interference (`R04`):**
   Static AST inspection verified `adapter_imports=0`, `adapter_attr_stores=0`, `adapter_dynamical_or_head_refs=0` on `AdapterReport` and `run_reporting_adapter`, and `upstream_readout_native_or_transition_refs=0` on `DirectPortReadout`, `decode_port_vectors`, and `direct_source_reader` in `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/apparatus.py`.

---

## 4. Scope Boundaries and Non-Interference

- **Status:** `NON-CANONICAL`, `L1`. Not Canon, not `T`, not `C`.
- **Source-exposure and harness-injection disclosure:** This probe imports `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/apparatus.py` read-only after SHA-256 verification (`SOURCES.tsv`) and tests failure reporting via isolated callbacks in `verify.py`. It is not a blind independent reproduction of the two-use apparatus and does not rerun the 19-stage audit or 1200-state trajectory sweep.
- **No promotion or physical claim:** `DirectPortReadout` is a software record type that prevents accidental argument confusion; it does not prove physical acquisition, authenticate provenance against deliberate caller forgery, or establish native contact realization (`C-NATIVE-CONTACT-REALIZATION`, `C-READER-NO-RAW-SOURCE`).
- **Zero interference:** `0` files modified outside `probes/P-TWO-USE-READOUT-FAILURE-REGRESSION-2/`.
