# Result: P-INTEGER-K1-SCALED-BRIDGE-3

Status: ABANDONED

Public lock: `#1635`.
Immutable pin: `989c4ba195d1e6a5ecce9baed437ae2fa1372543`.

## Why the gate did not complete

The frozen preregistration (`PREREG.md`), proofs (`PROOF.md`), source manifest
(`SOURCE.md`), primary verifier (`verify.py`), independent breaker
(`breaker.py`), and hash manifest (`FROZEN.sha256`) were committed, pushed, and
publicly read back from GitHub at `989c4ba195d1e6a5ecce9baed437ae2fa1372543`
before execution.

On the first formal invocation, `verify.py` completed all of its own checks
(`check_pre_pin_integrity()`, `check_k1_exhaust()` on `2,184` states,
`check_k1_words_and_precision()` on `1,250` metric checks and `240` step
checks, `check_k1_bounce_cycles()` on `60` cycles, and `check_coupled_bridge()`
on `4,032` states and `8` trajectories), after which its subprocess call to
`breaker.py` exited nonzero (`exit_code: 1`) on line 421 of `breaker.py` before
`verify.py` emitted any stdout line. Line 421 of `breaker.py` asserted
`g % 3 == 0` as an error for `g = gcd(U_n^(w), 2 * 324^n)`, whereas because
`U_1^(w) = 324 * (2 h_1^(w))` and `denom = 2 * 324^n` carry `v_3(denom) = 4n`
while `v_3(d_n) = 4(n - 1)`, the common factor `g = denom / d_n` has exact
3-adic valuation `v_3(g) = 4n - 4(n - 1) = 4` for all `n >= 1`.

Under `POLICY.md` Section 3 (Abandoned pins), a run that exits nonzero on a
fixture/assertion defect before completing the gate yields no exact stdout to
pin, so no `EXPECTED.txt` and no `RUN.md` exist to commit. All six frozen files
(`PREREG.md`, `PROOF.md`, `SOURCE.md`, `verify.py`, `breaker.py`, and
`FROZEN.sha256`) remain unchanged.

## The identifier is consumed

The identifier `P-INTEGER-K1-SCALED-BRIDGE-3` is consumed and must not be
reused, renamed, repaired, rerun, or resumed. The retargeted probe is carried
out under the fresh successor identifier `P-INTEGER-K1-SCALED-BRIDGE-4`, which
names the abandoned predecessors and this `v_3(g) = 4` helper assertion in its
own preregistration before its own immutable pin.
