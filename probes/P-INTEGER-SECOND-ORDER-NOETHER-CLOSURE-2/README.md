# `P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-2`

- **Status:** `FAIL` (`FALSIFIER=BREAKER_BYTES`)
- **Ownership Issue:** [#1655](https://github.com/mathorn1973/twist-j/issues/1655)
- **Prospective Pin:** [`f0520db827dac1b2ec9242a9c82083fd9151aeb4`](https://github.com/mathorn1973/twist-j/commit/f0520db827dac1b2ec9242a9c82083fd9151aeb4)
- **Successor Probe:** `P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-3`

Closed with `Status: FAIL` per `POLICY.md` Section 3 after `verify.py` passed all primary checks in `certificate()` while `breaker.py` raised `FALSIFIER=CERTIFICATE` at line 936 (`len(controls) == 10`) because 11 labels (the 10 negative controls plus `"pure_gauge_s2_completion"`) were inserted into `controls`.
