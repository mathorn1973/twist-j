# Result: Executable Funded Two-Use Continuing Apparatus (`C-FUNDED-TWO-USE-EXECUTABLE-N`)

**NON-CANONICAL / L1 / PARTIAL — STOP (`T01_geometry_stencil_and_operators` FAILED: `Expected |D| = 869, got 705`; `T02`–`T18`, `X01`–`X10`, `--witnesses`, and `--compare` `NOT_RUN`).**
**Physical status: `NOT_READY`. Promotion recommendation: `DO NOT PROMOTE`.**
Original work Apache-2.0, A. M. Thorn, 2026-10-15.

```text
candidate_id:             C-FUNDED-TWO-USE-EXECUTABLE-N
lane_issue:               https://github.com/mathorn1973/twist-j/issues/1507
parent_program:           https://github.com/mathorn1973/twist-j/issues/1506
branch:                   incubation/C-FUNDED-TWO-USE-EXECUTABLE-N
base_main_commit:         8b91a935c426036e00ecb300019fd94734addeec
preregistration_commit:   81a70caa8dbcc61b64276e7d3df5ba84e860d4f1
pinned_receipt_url:       https://github.com/mathorn1973/twist-j/issues/1507#issuecomment-6189582448
apparatus_sha256:         a3bba3433c81c2e1b445008596d898915031dc67ca73f18195be6f5196422833
verify_sha256:            15dd15ea81ded0f7bda498b9797ee263d2204efe38f763f5b3e7e924cdf76126
expected_stdout_sha256:   2eb562661a6fabef4092f478342ba99e1e205d99e21c4219d4968b8935a052ff
expected_stdout_bytes:    42
first_run_exit_code:      1
scientific_status:        PARTIAL / STOP (T01_geometry_stencil_and_operators FAILED: |Y+B_zero+B_zero| = 705 != 869)
positive_tests_executed:  1 / 18 (0 PASS, 1 FAIL, 17 NOT_RUN)
adversarial_tests_run:    0 / 10 (10 NOT_RUN)
witness_trajectories:     NOT_RUN (blocked by T01 geometry STOP)
comparison_digest_mode:   NOT_RUN (TWOUSE-COMPARE-v1 blocked by unresolved carrier cardinality 705 vs 869)
pinned_files_diff_lines:  0
physical_status:          NOT_READY
promotion_decision:       DO NOT PROMOTE
```

---

## 1. Executive Summary and Scoped Stop Decision

Following public preregistration pin `81a70caa8dbcc61b64276e7d3df5ba84e860d4f1` and public readback [`#1507#issuecomment-6189582448`](https://github.com/mathorn1973/twist-j/issues/1507#issuecomment-6189582448), the first scientific execution of `python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py` halted in the first test `T01_geometry_stencil_and_operators` (`notes/C-FUNDED-TWO-USE-EXECUTABLE-N/apparatus.py`, line 153, `get_geometry()`) with:

```text
RuntimeError: Expected |D| = 869, got 705
```

Per the completion criterion of [`#1507`](https://github.com/mathorn1973/twist-j/issues/1507) (*"All known target values are result-exposed regression targets. A mismatch creates a scoped failure record and STOP for that claim; do not change frozen test cases, cost, source law or thresholds to obtain PASS"*) and Section 1.5 and Section 3 of `PREREG.md` (`81a70caa8dbcc61b64276e7d3df5ba84e860d4f1`), this mismatch triggers an immediate **`STOP`**:

1. All seven pinned files (`README.md`, `CONTRACT.md`, `PREREG.md`, `SOURCES.json`, `PROOF.md`, `apparatus.py`, `verify.py`) are preserved byte-for-byte unchanged (`0` diff lines against `81a70caa8dbcc61b64276e7d3df5ba84e860d4f1`).
2. Exact `stdout` (`EXPECTED.txt`, 42 bytes, SHA-256 `2eb562661a6fabef4092f478342ba99e1e205d99e21c4219d4968b8935a052ff`) and the neutral execution record (`RUN.md`) are committed without post-pin edits or silent threshold/dimension adjustments.
3. Subsequent test cases (`T02`–`T18` and `X01`–`X10`), the 6 witness boundary trajectories (`--witnesses`), and the 1200-record comparison stream (`TWOUSE-COMPARE-v1`, `--compare`) were not reached and are recorded as **`NOT_RUN`**. Planned test counts and analytical certificates in `PREREG.md` and `PROOF.md` are **not** claimed as executed computational evidence.

---

## 2. Exact Localization of the `T01` Carrier Cardinality Discrepancy

1. **Primary Minkowski-sum definition (`#1485`):**
   In `notes/C-CLASSICAL-SIGNED-PORT-CONTRACT-N/CONTRACT.md` (`4302c31f07823b2a843e3702ca14620c1917b853`, lines 23–30), the even sublattice is $D_3 = \{x \in \mathbb{Z}^3 : x_1 + x_2 + x_3 \equiv 0 \pmod 2\}$, the symmetric stencil is
   $$B_{\mathrm{st}} = \bigl\{d \in D_3 : \|d\|_2^2 \in \{2, 4, 8, 10, 16\}\bigr\}, \qquad B_{\mathrm{zero}} = B_{\mathrm{st}} \cup \{(0,0,0)\},$$
   the five marked sites are
   $$Y = \{(0,0,0),\ (1,1,0),\ (1,0,1),\ (0,1,1),\ (2,0,0)\} \subset D_3,$$
   and the finite two-cut causal domain is defined as the Minkowski sum
   $$D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}} \subset D_3.$$
   Neither `#1485`, `#1489`, `#1492` (`probes/P-NATIVE-CLASSICAL-CONTACT-CENSUS-1/verify.py`, which represented wave fields as sparse dictionaries without asserting `len(D_SET)`), `#1495`, `#1498` (`A1`), nor `#1499` (`A2`) asserted a numerical value for $|D|$.

2. **Introduction of the stated cardinality $|D| = 869$ in unexecuted upstream notes (`#1500`, `#1504`, `#1506`):**
   - In `#1500` (`f341b04f737827d9033e60f452fab77231f7b04a`, `notes/C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N/RESULT.md` line 92 and `INTERFACE.json` line 17, which carried `scientific_code_status: NONE / NOT_RUN`), the carrier description stated `with |D| = 869`.
   - In `#1504` (`c67b9af4f25f9ebb5904e3d654fd9fb3856c8c6f`, `notes/C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N/CONTRACT.md` line 21, `PREREG.md` line 42, `README.md` line 18, `SOURCES.json` line 42, and `INTERFACE.json` line 33, also `scientific_code_status: NONE / NOT_RUN`), the combined contract stated `finite causal domain D = Y + B_zero + B_zero (|D| = 869), ordered lexicographically`.
   - Parent program `#1506` (`d31d6cc3c880acaff494d5b1567d849626e6c4efa408291bedde1efaf4dd79bb`) mandated: *"Use the exact 869-site Dirichlet D, ordered ports, S, eta, native generators, selection, F, L_buf, two H_B contacts and ready family of the source contract."*

3. **Actual cardinality of $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$:**
   In `apparatus.get_geometry()` (`notes/C-FUNDED-TWO-USE-EXECUTABLE-N/apparatus.py`, lines 130–153), constructing $B_{\mathrm{st}}$, $B_{\mathrm{zero}}$, and $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$ directly from the primary definition yields:
   $$|Y| = 5, \quad |B_{\mathrm{st}}| = 60, \quad |B_{\mathrm{zero}}| = 61, \quad |Y + B_{\mathrm{zero}}| = 142, \quad |B_{\mathrm{zero}} + B_{\mathrm{zero}}| = 489, \quad |D| = |Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}| = 705.$$
   Because $705 \ne 869$, the formula $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$ and the numerical assertion $|D| = 869$ cannot simultaneously hold for the frozen 5-site set $Y$ and 60-offset stencil $B_{\mathrm{st}}$. Both `apparatus.get_geometry()` (line 152: `if len(domain_d) != 869`) and `WaveTapeState` (lines 203–204: `require_q_tuple(self.u, 869, "u")`) enforce the frozen $|D| = 869$ assertion, causing `T01_geometry_stencil_and_operators` to fail immediately with `RuntimeError: Expected |D| = 869, got 705`.

---

## 3. Audit Test and Adversarial Inventory Status (`T01`–`T18`, `X01`–`X10`)

| Test ID | Name | Status | Actual Outcome |
|---|---|---|---|
| `T01` | `T01_geometry_stencil_and_operators` | **FAIL / STOP** | `RuntimeError: Expected \|D\| = 869, got 705` at `apparatus.py:153` (`get_geometry()`) |
| `T02` | `T02_generators_and_V_non_invertibility` | `NOT_RUN` | Unreached after `T01` stop |
| `T03` | `T03_single_head_625_census_and_recovery` | `NOT_RUN` | Unreached after `T01` stop |
| `T04` | `T04_paired_factorization_390625` | `NOT_RUN` | Unreached after `T01` stop |
| `T05` | `T05_certificate_F_bijectivity_and_energy` | `NOT_RUN` | Unreached after `T01` stop |
| `T06` | `T06_certificate_HB_involutions_and_Lbuf` | `NOT_RUN` | Unreached after `T01` stop |
| `T07` | `T07_certificate_bilinear_work_and_mu` | `NOT_RUN` | Unreached after `T01` stop |
| `T08` | `T08_25_pair_work_table_and_capacities` | `NOT_RUN` | Unreached after `T01` stop |
| `T09` | `T09_order_witness_14_vs_41` | `NOT_RUN` | Unreached after `T01` stop |
| `T10` | `T10_certificate_four_cut_operators_and_archives` | `NOT_RUN` | Unreached after `T01` stop |
| `T11` | `T11_direct_chronological_and_source_readers` | `NOT_RUN` | Unreached after `T01` stop |
| `T12` | `T12_store_bounds_refusal_and_negative_work` | `NOT_RUN` | Unreached after `T01` stop |
| `T13` | `T13_accepted_zero_and_clarification_ii` | `NOT_RUN` | Unreached after `T01` stop |
| `T14` | `T14_seven_eight_boundary_and_energy_invariants` | `NOT_RUN` | Unreached after `T01` stop |
| `T15` | `T15_ready_image_left_inverse_all_branches` | `NOT_RUN` | Unreached after `T01` stop |
| `T16` | `T16_calibration_prediction_and_clarification_i` | `NOT_RUN` | Unreached after `T01` stop |
| `T17` | `T17_comparator_indistinguishability_and_separations` | `NOT_RUN` | Unreached after `T01` stop |
| `T18` | `T18_invalid_endpoint_and_type_rejection_suite` (`X01`–`X10`) | `NOT_RUN` | Unreached after `T01` stop |
| `--witnesses` | 6 witness boundary trajectories | `NOT_RUN` | Blocked by `T01` geometry stop |
| `--compare` | `TWOUSE-COMPARE-v1` (1200 records) | `NOT_RUN` | Blocked by unresolved carrier dimension (`705` vs `869`) |

---

## 4. Cross-Lane Independence and Comparison Protocol Disposition

1. **Blind implementation independence:**
   Lane I (`#1507`) authored, pinned (`81a70caa8dbcc61b64276e7d3df5ba84e860d4f1`), publicly read back (`#1507#issuecomment-6189582448`), and executed its code without reading or importing any code, stdout, result, or digest from Lane V (`#1508`).
2. **Convergence of independent stops on the geometry gate:**
   Sibling Lane V (`#1508`, `probe/P-FUNDED-TWO-USE-INDEPENDENT-AUDIT-1`, Draft PR [`#1511`](https://github.com/mathorn1973/twist-j/pull/1511), pin `1949d6c5c9712fc2c3aa10f0ac296afb9ea5e928`, first run `2d6f2333aa519897e0fc328ef6b640c28733aba8`, submitted head `846902867881e535666d88fadfffb6d47323dbb3`) independently stopped at the same first geometry consistency check between `sorted(Y + B_zero + B_zero)` and the exposed $869$-site assertion, and recorded `PARTIAL / STOP` with `comparison_digest: NOT_RUN`.
3. **`TWOUSE-COMPARE-v1` status:**
   Because the `TWOUSE-COMPARE-v1` record format serializes explicit zero-padded vectors $u, v \in \mathbb{Q}^D$ over all sites of $D$, the 1200-record comparison stream cannot be produced without first resolving whether the contract carrier is the 705-site Minkowski sum $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$ or a different 869-site domain. Accordingly, `TWOUSE-COMPARE-v1` remains `NOT_RUN`.
4. **Notes-only CI limitation:**
   Ordinary `python3 tools/check_verifier.py` and `python3 tools/check_reproduce.py` on this `notes/`-only PR return `NOT APPLICABLE` (`VERIFIER CHECK SKIPPED: no probe verifier changes` and `REPRODUCE PASS: no reproduction directories changed`) and do **not** execute `notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py`.
5. **Handoff boundary:**
   The candidate identifier `C-FUNDED-TWO-USE-EXECUTABLE-N` and its preregistration pin `81a70caa8dbcc61b64276e7d3df5ba84e860d4f1` are consumed and preserved unaltered for review. Any successor executable run after reconciling $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$ ($|D| = 705$) versus $|D| = 869$ requires an explicit upstream disposition and a new authorized candidate identifier and preregistration pin.
