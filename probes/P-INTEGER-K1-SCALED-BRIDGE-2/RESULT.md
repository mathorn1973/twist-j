# Result: P-INTEGER-K1-SCALED-BRIDGE-2

Status: ABANDONED

Public lock: `#1635`.
Immutable pin: `fd4e5a2734fd99d94480b6bef30d2c657f6debc3`.

## Why the gate did not complete

The frozen preregistration (`PREREG.md`), proofs (`PROOF.md`), source manifest
(`SOURCE.md`), primary verifier (`verify.py`), independent breaker
(`breaker.py`), and hash manifest (`FROZEN.sha256`) were committed, pushed, and
publicly read back from GitHub at `fd4e5a2734fd99d94480b6bef30d2c657f6debc3`
before execution.

On the first formal invocation, `check_pre_pin_integrity()`,
`check_k1_exhaust()` (`2,184` states), and `check_k1_words_and_precision()`
(`1,250` transverse metric checks and `240` step valuation/precision checks)
all completed without error, after which `verify.py` exited nonzero
(`exit_code: 1`) on line 552 inside `check_k1_bounce_cycles()` before any
stdout line was emitted, due to an initial-slice helper formula defect in
`k1_init_U0_U1(word)` (`u0 = (b0 + 2*b1 + 4*b2 + 3*b3) % 5` and
`u1 = (b0 + b1 + b2 + b3) % 5` instead of the `DEF-K1-LINEAR-METRIC` formula
`u_t = (bits[t + 2] - bits[t]) % 5` for `t in {0, 1}` on the ten canonical
words `0010, 0011, 0100, 0101, 0110, 1001, 1010, 1011, 1100, 1101`).

Under `POLICY.md` Section 3 (Abandoned pins), a run that exits nonzero on a
fixture defect yields no exact stdout to pin and no completed gate, so no
`EXPECTED.txt` and no `RUN.md` exist to commit. All six frozen files
(`PREREG.md`, `PROOF.md`, `SOURCE.md`, `verify.py`, `breaker.py`, and
`FROZEN.sha256`) remain unchanged.

## The identifier is consumed

The identifier `P-INTEGER-K1-SCALED-BRIDGE-2` is consumed and must not be
reused, renamed, repaired, rerun, or resumed. The retargeted probe is carried
out under the fresh successor identifier `P-INTEGER-K1-SCALED-BRIDGE-3`, which
names the abandoned predecessors and this initial-slice helper defect in its
own preregistration before its own immutable pin.
