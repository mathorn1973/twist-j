# Execution Receipt: `C-FUNDED-TWO-USE-EXECUTABLE-2-N`

**NON-CANONICAL / L1 post-pin scientific execution receipt / 2026-10-15.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1515](https://github.com/mathorn1973/twist-j/issues/1515), under parent program [#1506](https://github.com/mathorn1973/twist-j/issues/1506).

```text
candidate_id:               C-FUNDED-TWO-USE-EXECUTABLE-2-N
branch:                     incubation/C-FUNDED-TWO-USE-EXECUTABLE-2-N
pin_commit_sha:             06d63ae94f609cc54989e410e3c778ce147d22c5
pin_receipt_url:            https://github.com/mathorn1973/twist-j/issues/1515#issuecomment-6191145416
authority_base:             8b91a935c426036e00ecb300019fd94734addeec
g1_reconciliation_probe:    P-D3-TWO-CUT-GEOMETRY-RECONCILIATION-1 (probes/P-D3-TWO-CUT-GEOMETRY-RECONCILIATION-1/DOMAIN.tsv)
g1_reconciliation_pin:      a96646c22267d59179a5a96a161c5f6f95ba6255
g1_reconciliation_result:   82ad219401d87c3900011d1e8801ffef4221e05b
predecessor_pin:            81a70caa8dbcc61b64276e7d3df5ba84e860d4f1
predecessor_result:         d6c48e463e1c7d78e8da828711cdda726f57e00b
scoped_successor_probe:     P-TWO-USE-TYPED-READOUT-CLOSURE-1 (#1522 / PR #1523, commit d334fd1e7ac3dad65fe290297a78ba97beb74a0a)
platform:                   Darwin
architecture:               aarch64
python_version:             3.13.13
deterministic_env:          LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
pinned_files_diff_lines:    0
default_audit_exit_code:    1 (PASS on T01-T10, STOP at T11 line 858)
default_stdout_bytes:       1073
default_stdout_sha256:      e3e7063bfdb292d6a8ed6a86c82286c51caf150950eb344d99d6a8565c2eff6a
default_stderr_bytes:       1171
default_stderr_sha256:      d24433dcb3d568464e6703c50d7eac4703b6abb77ec3c30c24d076309cce3f92
witnesses_exit_code:        0
witnesses_stdout_bytes:     20740
witnesses_stdout_sha256:    b7996fa6cfc525890892efb6cef02c9acb9098c167ecc8888deffe132e72b896
compare_exit_code:          0
compare_stdout_bytes:       182
compare_stdout_sha256:      77348e12d9948ebafc15c15ea9904b53ece6a30990ea59a59633a1bef8c21c8d
```

> **Correction Notice (`2026-10-15`, per `#1515` review disposition):** The raw stderr traceback block in commit `dac92207c11abb061c10fa4ab729e3789d9cbf85` contained a local user-directory path and local binary path; per `POLICY.md` and `#1515` review disposition, those local paths are replaced below by neutral public run fields, repository-relative call-stack locations, and exact byte/SHA-256 digests (`1171` bytes, SHA-256 `d24433dcb3d568464e6703c50d7eac4703b6abb77ec3c30c24d076309cce3f92`). All 9 pinned files at `06d63ae94f609cc54989e410e3c778ce147d22c5` and `EXPECTED.txt` remain untouched (`0` diff lines).

---

## 1. Frozen pin readback and immutability verification

Before the first scientific execution, commit `06d63ae94f609cc54989e410e3c778ce147d22c5` was pushed to `origin/incubation/C-FUNDED-TWO-USE-EXECUTABLE-2-N`, fetched back via the GitHub API, byte-compared against all nine pinned files in `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/`, and recorded in [`PINNED_I2`](https://github.com/mathorn1973/twist-j/issues/1515#issuecomment-6191145416):

| Pinned file | Bytes | Git blob SHA | SHA-256 | Post-run diff lines |
|---|---:|---|---|---:|
| `DOMAIN.tsv` | `5029` | `b139d0e7bab0ddd547da9f8624c62808a445ef01` | `2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0` | `0` |
| `README.md` | `9353` | `3c9242d1d0adf249d37c0f509456de79850b81ac` | `8695306ac7357b30c5851059f73bfe5a7412b3fbc46e3fad1966f7ccf0ed31b4` | `0` |
| `CONTRACT.md` | `17073` | `92ebca6cd133bef52b1fa34a05a09b2341e48caf` | `c285b6afaaf770c01c5b133b3db64cfd00816b453b747c3fb314e12e3a881952` | `0` |
| `PREREG.md` | `20437` | `a03a86542472a89ca22a1e16b5738a40ec5a6d86` | `d3afb6786ba4a4884421a61a3fa0b7edf8b95ac13dea3712a3709ecc4bc98381` | `0` |
| `SOURCES.json` | `34845` | `60f9899835092f90548b7d15b650d878188a52ef` | `48d0537f1f8f6e0c96754c6225faa9a95524890248d39742f4aa944502a68202` | `0` |
| `PROOF.md` | `14564` | `6e7a720e3f6f72dd621b97f6f0335014db63c4ae` | `57855afb3d5fe90cab0e93e1de97d7e4ec9f15b0224837d37d9c83ceed1f063d` | `0` |
| `MIGRATION.md` | `106269` | `5ecf27b98a71470dcfca95d2692e6aa587478e01` | `7a7c9760428cfce8b8a80d9135c664f8c1f5d8c3f8a56d447354b813965832c3` | `0` |
| `apparatus.py` | `58364` | `b99d515f5d5ece65647ae920558cdfeb59a49c96` | `85c18b1b130d6e7d8cf954ffc8e6ad5960f27e5b371ac381e967979bb518dc6d` | `0` |
| `verify.py` | `70920` | `484737d20943c5014fe3fa1f2b7aa6978e8e7e64` | `d093df3dba5d2f82b8a4493ff3a1f3828e3bd9b9b512a3c34e7aa240671c45f8` | `0` |

---

## 2. Scientific execution records on unmodified pin `06d63ae94f609cc54989e410e3c778ce147d22c5`

### 2.1 Default audit run (`verify.py`)

Command:
```text
env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py
```
*(Note: An initial invocation using a Python `3.9.6` interpreter passed `T01` (`192` stdout bytes, SHA-256 `05192c3e1bbb48bf6c1b42218a6114db26aea9de26074ec9c0b708665f239af4`) and raised `AttributeError: 'int' object has no attribute 'bit_count'` at `T02` because `int.bit_count()` was introduced in Python 3.10. Running on the same unmodified commit `06d63ae94f609cc54989e410e3c778ce147d22c5` with Python `3.13.13` executed `T01` through `T11` as recorded below.)*

Exact stdout saved to `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/EXPECTED.txt` (`1073` bytes, SHA-256 `e3e7063bfdb292d6a8ed6a86c82286c51caf150950eb344d99d6a8565c2eff6a`):
```text
C-FUNDED-TWO-USE-EXECUTABLE-2-N AUDIT START
T01 PASS: |B_st|=60, |B_zero|=61, |Y+B_zero|=142, |B_zero+B_zero|=489, |D|=705, dim=1426, DOMAIN.tsv sha256 verified, P^T P=I_4, J_p and M verified
T02 PASS: 5 generators involutive on 15625 states; V collision at n=0 verified
T03 PASS: all 625 single-head preparations (125/class) audited and inverted
T04 PASS: 390625 paired inputs factor into 25 fibres of 15625; full recovery verified
T05 PASS: coefficient-complete F/F^-1 and E_full (1426x1426=2033476 bilinear entries) verified on all 1426 basis vectors
T06 PASS: universal H_{B,A}^2=id, H_{B,B}^2=id, L_buf^-1, and supplied-label substate S_B^{(r_A,r_B)}^-1 verified across all 25 labels and 8 phases
T07 PASS: 4x4 bilinear cross-work matrix equals -1*mu^T/10497600 with mu=(145483,173653,173653,142153)
T08 PASS: all 25 source pairs and all 6 capacities match work table and branch counts
T09 PASS: order witness W(1,4)=10352117/20995200, W(4,1)=10323947/20995200, W(1,4)-W(4,1)=313/233280
T10 PASS: universal 4-cut operator certificate and c1=e0 WARM witnesses verified
```

Neutral stderr summary (`1171` bytes, SHA-256 `d24433dcb3d568464e6703c50d7eac4703b6abb77ec3c30c24d076309cce3f92`, exit code `1`):
```text
file:           notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py
call_stack:     <module> (line 1765) -> main (line 1749) -> run_full_audit (line 1734) -> run_t11_direct_chronological_and_source_readers (line 858) -> require_true (line 144)
exception:      AssertionError: T11.reject_forbidden[tuple]: expected=True, actual=False
```

### 2.2 Working CLI command for the 7-step `(1,4)`/`(4,1)` comparison, dirty-archive `c1=e0` case, and lower/upper stock refusal (`verify.py --witnesses`)

Command:
```text
env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py --witnesses
```
- **Exit code:** `0`
- **Stderr bytes:** `0`
- **Stdout bytes:** `20740`
- **Stdout SHA-256:** `b7996fa6cfc525890892efb6cef02c9acb9098c167ecc8888deffe132e72b896`
- **Terminal summary line:**
  ```text
  WITNESS_SUMMARY order_W14=10352117/20995200 order_W41=10323947/20995200 order_diff=313/233280 dirty_c1_e0_B0=(-292699/699840,-20263/466560,-20263/466560,-6871/155520) ready_low_ref_sig=(-1,+1) warm_low_ref_sig=(-1,+1) warm_high_ref_sig=(-1,+1)
  ```

### 2.3 Full-state comparison command (`verify.py --compare`, `TWOUSE-COMPARE-v2`)

Command:
```text
env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py --compare
```
- **Exit code:** `0`
- **Stderr bytes:** `0`
- **Stdout bytes:** `182`
- **Stdout SHA-256:** `77348e12d9948ebafc15c15ea9904b53ece6a30990ea59a59633a1bef8c21c8d`
- **Exact stdout line:**
  ```text
  TWOUSE-COMPARE-v2 domain_sha256=2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0 records=1200 sha256=670f270e88386e2f1f507e24ec0ae71daf1ff6638ea44783b793479291af3dbc
  ```

---

## 3. Administrative repository checks vs. scientific execution

Per `#1515`, administrative repository checks are recorded separately from scientific execution:
- `python3 tools/check_policy.py`: `POLICY PASS`
- `python3 tools/check_canon.py`: `CANON PASS v101 claims=514`
- `python3 tools/check_ledger.py`: `LEDGER PASS claims=514 items=578 dependencies=1063 evidence=514 history=1061 gates=26 programs=7`
- `python3 tools/check_gate_contract.py`: `GATE CONTRACT PASS gates=26`
- `python3 tools/check_reproduce.py`: `REPRODUCE CHECK NOT APPLICABLE: no reproduce/*/verify.py changed`
- `python3 tools/check_verifier.py`: `VERIFIER CHECK NOT APPLICABLE: no probe verifier changed`

None of these administrative checks execute `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py`.
