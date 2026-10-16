# Six-Field Preregistration: `P-TWO-USE-READOUT-FAILURE-REGRESSION-1`

**PUBLIC / NON-CANONICAL / L1 / 2026-10-15.**
Original work and attributed source reuse Apache-2.0, A. M. Thorn.
Issue: [#1526](https://github.com/mathorn1973/twist-j/issues/1526), under parent program [#1506](https://github.com/mathorn1973/twist-j/issues/1506).
Owner session: `Antigravity-20261015-readout-failure-regression`.

---

## 1. Equation

This bounded followup closes the two nonblocking review debts identified in [#1522 comment `6195356376`](https://github.com/mathorn1973/twist-j/issues/1522#issuecomment-6195356376) and [#1522 comment `6197220969`](https://github.com/mathorn1973/twist-j/issues/1522#issuecomment-6197220969) on the integrated typed-readout probe `P-TWO-USE-TYPED-READOUT-CLOSURE-1` (scientific pin `c3a93f4cb53a3e541529a205f114489e71ad039b`, reviewed result `d334fd1e7ac3dad65fe290297a78ba97beb74a0a`, merged into `main` at `b79143fb00839b870686f6cea34e174959060df1`), without modifying any file in `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/` and without rerunning the 19-stage or 1200-state apparatus study:

1. **Five semantic rejection branches on `DirectPortReadout` and `direct_source_reader` (`PROOF.md` §1):**
   On the common-ready family, the two recorded cuts $(b_0, b_2) \in (\mathbb{Q}^4)^2$ satisfy
   $$\widehat{a} = R_0^{-1} b_0 = \alpha_A z_A, \qquad r = b_2 - D_2 \widehat{a} = \alpha_B R_0 z_B, \qquad \widehat{b} = R_0^{-1} r = \alpha_B z_B,$$
   with $R_0^{-1} = -\frac{216}{59}\left(I_4 + \frac{1}{365} v \mathbf{1}^T\right)$, $v = (349, 354, 354, 348)^T$, $\alpha_A = (1 - \sigma_A)/2$, $\alpha_B = (1 - \sigma_B)/2$, and $z_B = \eta(d)$ when $d \in \mathbb{F}_5^2$ is supplied. With $z = (0,0,0,0)$ and $e = (1,0,0,0)$, the five records `S1`–`S5` pass `DirectPortReadout` construction and must raise `ValueError` with exact frozen messages at semantic reading `direct_source_reader(record)`. Five positive controls `P1`–`P5` verify accepted zero, refused input, unknown acceptance, the partial-contract boundary (`alpha_B = None` at nonzero $b_2$ without context is not proof of mathematical indistinguishability), and a valid explicit integer-valued $\mathbb{Q}^4$ record (whose tag is not proof of physical acquisition).
2. **Honest failure-phase reporting adapter (`PROOF.md` §2–§3):**
   The historical `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/verify.py` leaves `build_witness_trajectories()` under `CURRENT_STAGE = "run_t19_typed_record_factorization"` and prints `comparison=NOT_RUN` on every `AssertionError`, including `COMPARISON.count` and `COMPARISON.unchanged_I2_V2_state_stream` mismatches after `compute_comparison_digest()` has executed. That historical verifier is preserved untouched and verified via static AST inspection. A new isolated reporting adapter `run_reporting_adapter` defines the five phase states
   $$\mathcal{S}_{\mathrm{phase}} = \{\texttt{AUDIT},\; \texttt{WITNESS\_BUILDING},\; \texttt{COMPARISON\_STARTED},\; \texttt{COMPARISON\_FAILED},\; \texttt{COMPLETED}\}$$
   and is tested across six frozen harness scenarios `H1`–`H6`.

---

## 2. Code and Source-Exposure / Harness-Injection Disclosure

- **Verifier:** `probes/P-TWO-USE-READOUT-FAILURE-REGRESSION-1/verify.py` (Python standard library only, deterministic environment `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`).
- **Source reuse disclosure (source-exposed, not blind independent science):**
  - `verify.py` verifies `CODE_SHA256SUMS` (binding `PREREG.md`, `PROOF.md`, `SOURCES.tsv`, and `verify.py`) and `SOURCES.tsv` (binding all 12 scientific and 4 result files of `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/` and 7 normative repository files at `b79143fb00839b870686f6cea34e174959060df1`) before importing `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/apparatus.py` read-only.
  - No code from `apparatus.py` is duplicated or modified. `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/verify.py` is inspected purely as static source text (`ast.parse`) and is never imported or executed.
- **Harness-injection disclosure:**
  - In `R03_honest_failure_phase_reporting_adapter`, failure injection occurs exclusively inside isolated pure-Python callback lists passed to `run_reporting_adapter` in `probes/P-TWO-USE-READOUT-FAILURE-REGRESSION-1/verify.py`.
  - No monkeypatching, attribute mutation, or mock replacement is ever applied to `apparatus.py` or `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/verify.py`, and no injected scenario prints the upstream `TYPED_CLOSURE_FAIL` or `P-TWO-USE-TYPED-READOUT-CLOSURE-1 AUDIT PASS` strings.

---

## 3. Carrier and Complete Frozen Finite Inventory

With $z = (0,0,0,0)$ and $e = (1,0,0,0)$:

### 3.1 Five semantic rejection specimens (`S1`–`S5`)

| ID | Constructed `DirectPortReadout` | Expected construction | Expected `direct_source_reader` exception | Exact expected `ValueError` message |
|---|---|---|---|---|
| `S1_REFUSED_A_NONZERO_B0` | `DirectPortReadout(e, z, sigma_A=1)` | Valid `DirectPortReadout` | `ValueError` | `"Inconsistent refused sigma_A=+1 with non-zero b0"` |
| `S2_ZERO_B_SOURCE_NONZERO_RESIDUAL` | `DirectPortReadout(z, e, d=(0, 4))` | Valid `DirectPortReadout` | `ValueError` | `"Inconsistent d=(0,4) with non-zero b2 - D2(alpha_A z_A)"` |
| `S3_RESIDUAL_INCOMPATIBLE_WITH_D` | `DirectPortReadout(z, e, d=(1, 4))` | Valid `DirectPortReadout` | `ValueError` | `"Residual b2 - D2(alpha_A z_A) does not match d on ready family"` |
| `S4_SIGMA_B_CONTRADICTS_ZERO_COST_D` | `DirectPortReadout(z, z, sigma_B=1, d=(0, 4))` | Valid `DirectPortReadout` | `ValueError` | `"Mismatch between sigma_B and (d, b0, b2) acceptance readout"` |
| `S5_REFUSED_B_NONZERO_RESIDUAL` | `DirectPortReadout(z, e, sigma_B=1)` | Valid `DirectPortReadout` | `ValueError` | `"Inconsistent refused Contact B with non-zero residual b2"` |

### 3.2 Five positive controls (`P1`–`P5`)

| ID | Input record | Expected `direct_source_reader` tuple `(alpha_A, alpha_B, alpha_B_from_d_b0_b2, z_A, z_B)` | Additional invariant |
|---|---|---|---|
| `P1_ACCEPTED_ZERO` | `DirectPortReadout(z, z, sigma_A=-1, sigma_B=-1, d=(0, 4))` | `(1, 1, 1, (0,0,0,0), (0,0,0,0))` | Accepted zero distinct from refusal and unknown |
| `P2_REFUSED_INPUT` | `DirectPortReadout(z, z, sigma_A=1, sigma_B=1, d=(1, 4))` | `(0, 0, 0, None, None)` | `alpha_A_z_A == (0,0,0,0)` and `alpha_B_z_B == (0,0,0,0)` not returned as `z_A, z_B` |
| `P3_UNKNOWN_ACCEPTANCE_ZERO` | `DirectPortReadout(z, z)` | `(None, None, None, None, None)` | Omitted context defaults to `None`, never `-1` |
| `P4_PARTIAL_CONTRACT_NONZERO_B2_NO_CONTEXT` | `DirectPortReadout(z, R_0 z^{(1)})` | `(None, None, None, None, None)` | `alpha_B_z_B == (1/2, 0, 0, 0) != 0`; `None` is partial contract, not indistinguishability |
| `P5_VALID_EXPLICIT_INTEGER_Q4_RECORD` | `DirectPortReadout(e, z)` | `(1, None, None, (-154224/21535, -1296/365, -1296/365, -75168/21535), None)` | Equals `decode_port_vectors(e, z)`; raw `direct_source_reader(e)` raises `TypeError`; tag is not physical provenance |

### 3.3 Six honest failure-phase harness scenarios (`H1`–`H6`)

| ID | Injected boundary | `phase_state` | `first_failed_stage` | `audit` | `witnesses` | `comparison` | `remaining_dependent_checks` | `completion_marker` | `strict_exit_code` |
|---|---|---|---|---|---|---|---|---|---:|
| `H1_AUDIT_MID_STAGE_T11_FAIL` | `run_t11_direct_chronological_and_source_readers` (`idx=10`) | `AUDIT` | `run_t11_direct_chronological_and_source_readers` | `FAIL` | `NOT_RUN` | `NOT_RUN` | `NOT_RUN` | `False` | `1` |
| `H2_AUDIT_FINAL_STAGE_T19_FAIL` | `run_t19_typed_record_factorization` (`idx=18`) | `AUDIT` | `run_t19_typed_record_factorization` | `FAIL` | `NOT_RUN` | `NOT_RUN` | `NOT_RUN` | `False` | `1` |
| `H3_WITNESS_BUILDING_FAIL` | `witness_boundary_trajectories` | `WITNESS_BUILDING` | `witness_boundary_trajectories` | `PASS` | `FAIL` | `NOT_RUN` | `NOT_RUN` | `False` | `1` |
| `H4_COMPARISON_COUNT_MISMATCH` | `full_state_comparison` (`count=1199 != 1200`) | `COMPARISON_FAILED` | `full_state_comparison` | `PASS` | `PASS` | `FAIL` | `NONE` | `False` | `1` |
| `H5_COMPARISON_DIGEST_MISMATCH` | `full_state_comparison` (`digest='0'*64`) | `COMPARISON_FAILED` | `full_state_comparison` | `PASS` | `PASS` | `FAIL` | `NONE` | `False` | `1` |
| `H6_COMPLETED_POSITIVE_CONTROL` | None (all stages, witnesses, and comparison pass) | `COMPLETED` | `None` | `PASS` | `PASS` | `PASS` | `NONE` | `True` | `0` |

---

## 4. Systematics

- Exact `int` and `Fraction` arithmetic only; no floating point, random sampling, network access, or external packages.
- Only the 4-port basis operators (`get_derived_operators()`) of `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/apparatus.py` are evaluated during `R02`; the 19-stage audit and 1200-state trajectory sweep are not re-executed.
- Static AST verification (`R04`) checks that `run_reporting_adapter` has zero imports, zero external attribute mutations, and zero references to wave/contact/native state fields or transitions, and that `DirectPortReadout`, `decode_port_vectors`, and `direct_source_reader` in `apparatus.py` have zero references to native heads or transition functions.

---

## 5. Failure Threshold and Execution Semantics

- **Tolerance:** Zero on every hash, byte count, exception type, exact error string, positive-control dictionary, harness phase report, and AST non-interference check.
- **Exit-code semantics:**
  1. Inside `AdapterReport` (`R03`), `strict_exit_code == 0` iff `phase_state == "COMPLETED"` (and `1` on any `AUDIT`, `WITNESS_BUILDING`, or `COMPARISON_FAILED` stop), while `harness_replay_exit_code == 0` records that the harness caught the expected `AssertionError` cleanly.
  2. For `probes/P-TWO-USE-READOUT-FAILURE-REGRESSION-1/verify.py`, the process exits `0` with `0` stderr bytes and deterministic stdout matching `EXPECTED.txt` iff all four regression gates (`R01`, `R02`, `R03`, `R04`) pass; any failed assertion raises an unhandled `AssertionError` (nonzero exit). Repository byte-equality checks (`tools/check_verifier.py` comparing stdout byte-for-byte against `EXPECTED.txt` on `x86_64` and `aarch64`), not exit code `0` alone, establish a passed audit.
- No threshold, specimen, or code changes after the preregistration pin.

---

## 6. Action Layer

- **Action layer:** `L1` (finite mathematical and software interface regression/diagnostic audit).
- No Canon file (`canon/`), registry row, gate, workflow, or prior probe directory (`probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/`, `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/`, `#1525`, `#1519`/`#1521`) is modified. No physical acquisition, native contact realization, or Canon promotion is claimed.
