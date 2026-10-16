# First Exact Execution Record (`C-FUNDED-TWO-USE-EXECUTABLE-N`)

**NON-CANONICAL / L1 / PARTIAL — STOP (`T01_geometry_stencil_and_operators` FAILED; `T02`–`T18`, `X01`–`X10`, `--witnesses`, and `--compare` `NOT_RUN`).**
Original work Apache-2.0, A. M. Thorn, 2026-10-15.

```text
candidate_id:        C-FUNDED-TWO-USE-EXECUTABLE-N
issue:               https://github.com/mathorn1973/twist-j/issues/1507
parent_program:      https://github.com/mathorn1973/twist-j/issues/1506
branch:              incubation/C-FUNDED-TWO-USE-EXECUTABLE-N
base_main_commit:    8b91a935c426036e00ecb300019fd94734addeec
pin_commit:          81a70caa8dbcc61b64276e7d3df5ba84e860d4f1
pinned_receipt_url:  https://github.com/mathorn1973/twist-j/issues/1507#issuecomment-6189582448
apparatus_sha256:    a3bba3433c81c2e1b445008596d898915031dc67ca73f18195be6f5196422833
apparatus_bytes:     51473
verify_sha256:       15dd15ea81ded0f7bda498b9797ee263d2204efe38f763f5b3e7e924cdf76126
verify_bytes:        58399
command:             python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py
environment:         LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform:            Darwin 27.0.0
architecture:        arm64 (aarch64)
python:              3.9.6
start_utc:           2026-10-15T10:19:22.686619Z
end_utc:             2026-10-15T10:19:22.804965Z
exit_code:           1
stdout_file:         notes/C-FUNDED-TWO-USE-EXECUTABLE-N/EXPECTED.txt
stdout_bytes:        42
stdout_lines:        1
stdout_sha256:       2eb562661a6fabef4092f478342ba99e1e205d99e21c4219d4968b8935a052ff
scientific_status:   PARTIAL / STOP (T01_geometry_stencil_and_operators FAILED: Expected |D| = 869, got 705)
remaining_checks:    NOT_RUN (T02-T18, X01-X10, --witnesses)
comparison_mode:     NOT_RUN (TWOUSE-COMPARE-v1 withheld and unexecuted under carrier STOP)
pin_diff_lines:      0
```

---

## 1. Execution Chronology and Pin Integrity

1. All seven preregistration files (`README.md`, `CONTRACT.md`, `PREREG.md`, `SOURCES.json`, `PROOF.md`, `apparatus.py`, `verify.py`) were committed at `81a70caa8dbcc61b64276e7d3df5ba84e860d4f1`, pushed to `origin/incubation/C-FUNDED-TWO-USE-EXECUTABLE-N`, retrieved byte-for-byte via the GitHub API, and recorded in [`#1507#issuecomment-6189582448`](https://github.com/mathorn1973/twist-j/issues/1507#issuecomment-6189582448) (`2026-10-15T10:07:10Z`) before `apparatus.py` or `verify.py` was executed or imported for the first time.
2. Following public readback of `PINNED_I`, `python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py` was executed from the repository root with `LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.
3. All seven pinned files remain byte-for-byte identical to `81a70caa8dbcc61b64276e7d3df5ba84e860d4f1` (`0` diff lines).

---

## 2. Exact Output and Neutral Failure Traceback

### 2.1 Exact `stdout` (`EXPECTED.txt`, 42 bytes, SHA-256 `2eb562661a6fabef4092f478342ba99e1e205d99e21c4219d4968b8935a052ff`)

```text
C-FUNDED-TWO-USE-EXECUTABLE-N AUDIT START
```

### 2.2 Neutral repository-relative `stderr` (`exit_code = 1`)

```text
Traceback (most recent call last):
  File "notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py", line 1461, in <module>
    raise SystemExit(main(sys.argv))
  File "notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py", line 1444, in main
    run_full_audit()
  File "notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py", line 1427, in run_full_audit
    msg = fn()
  File "notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py", line 185, in run_t01_geometry_stencil_and_operators
    geom = app.get_geometry()
  File "notes/C-FUNDED-TWO-USE-EXECUTABLE-N/apparatus.py", line 153, in get_geometry
    raise RuntimeError(f"Expected |D| = 869, got {len(domain_d)}")
RuntimeError: Expected |D| = 869, got 705
```

---

## 3. Repository Checkers and Notes-Only CI Limitation

Per `#1507`, ordinary repository verifier/reproduction scripts do not execute scientific code under `notes/`:

- `python3 tools/check_policy.py` $\to$ `POLICY PASS`
- `python3 tools/check_canon.py` $\to$ `CANON PASS v101 claims=514`
- `python3 tools/check_ledger.py` $\to$ `LEDGER PASS claims=514 items=578 dependencies=1063 evidence=514 history=1061 gates=26 programs=7`
- `python3 tools/check_gate_contract.py` $\to$ `GATE CONTRACT PASS gates=26 kinds=DEFINITION_PROJECTION:2,DICTIONARY_LIFT:13,FIRED_NEGATIVE:3,OPEN_DECISION:1,OPEN_LIFT:5,OPEN_SELECTION:2`
- `python3 tools/check_verifier.py --base 8b91a935c426036e00ecb300019fd94734addeec` $\to$ `VERIFIER CHECK SKIPPED: no probe verifier changes` (`NOT APPLICABLE` to `notes/`-only PR; does not execute `notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py`)
- `python3 tools/check_reproduce.py --base 8b91a935c426036e00ecb300019fd94734addeec` $\to$ `REPRODUCE PASS: no reproduction directories changed` (`NOT APPLICABLE` to `notes/`-only PR; does not execute `notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py`)
