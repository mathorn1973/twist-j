# Result — `P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-2`

Status: FAIL
Scope: NON-CANONICAL / L1
Fired falsifiers: `BREAKER_BYTES` (triggered by `CERTIFICATE` in `breaker.py` line 936)

## 1. Execution Outcome

Following the public six-file prospective pin [`f0520db827dac1b2ec9242a9c82083fd9151aeb4`](https://github.com/mathorn1973/twist-j/commit/f0520db827dac1b2ec9242a9c82083fd9151aeb4) recorded on [Issue #1655](https://github.com/mathorn1973/twist-j/issues/1655#issuecomment-6276701649), the first formal execution of `python -I probes/P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-2/verify.py` exited with `exit_code = 0`, `stderr_bytes = 0`, and exact stdout (`36` bytes, SHA-256 `d5667d2975442b5bca38fb4076f152a4c97564db19078d930efcbf2046818165`):

```text
FALSIFIER=BREAKER_BYTES
RESULT=FAIL
```

Per `POLICY.md` Section 3, because the formal gate completed and produced an exact stdout and run record with a fired falsifier, `P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-2` is closed by its result (`Status: FAIL`), never relabelled as abandoned, and the identifier `P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-2` is consumed and must not be reused.

## 2. Root Cause of `FALSIFIER=BREAKER_BYTES`

- In `verify.py`, `certificate()` passed all 21 scientific checks (`GLOBAL_S2_GRADIENT_SHA256 = 74a025a6de971360111126fa8e1ea1a24b26d5be0a28a64a52617f7ca24c4fba`, `SECOND_ORDER_PAYLOAD_SHA256 = 869bff9169debc3f8ed0196d52e0c0093ab91f7a9779c8241e6a858250e66bbc`, and all witnesses and 10 negative controls).
- In `breaker.py`, `audit_configurations()` produced the exact same two SHA-256 digests (`74a025a6de971360111126fa8e1ea1a24b26d5be0a28a64a52617f7ca24c4fba` and `869bff9169debc3f8ed0196d52e0c0093ab91f7a9779c8241e6a858250e66bbc`) and `audit_witnesses()` passed all witnesses and all 10 negative controls.
- However, in `breaker.py` `audit_witnesses()`, the set `controls` had 11 strings inserted (the 10 negative controls plus the positive pure-gauge witness label `"pure_gauge_s2_completion"` at line 866), causing `require(len(controls) == 10, "CERTIFICATE")` at line 936 of `breaker.py` to raise `ScientificFailure("CERTIFICATE")`.
- Consequently, `breaker.py` wrote `FALSIFIER=CERTIFICATE\nRESULT=FAIL\n`, and `verify.py` line 1011 (`require(child.returncode == 0 and child.stderr == b"" and child.stdout == raw, "BREAKER_BYTES")`) fired `FALSIFIER=BREAKER_BYTES`.

## 3. Retargeting

In accordance with `POLICY.md` Section 3, the probe is retargeted under the new identifier `P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-3` with its own prospective six-file pin under [Issue #1655](https://github.com/mathorn1973/twist-j/issues/1655).
