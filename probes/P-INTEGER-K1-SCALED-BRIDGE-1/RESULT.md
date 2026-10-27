# Result: P-INTEGER-K1-SCALED-BRIDGE-1

Status: ABANDONED

Public lock: `#1635`.
Immutable pin: `632f59e97c169abe937e00a6d92642f32378d767`.

## Why the gate did not complete

The frozen preregistration (`PREREG.md`), conditional and unconditional proofs
(`PROOF.md`), source manifest (`SOURCE.md`), primary verifier (`verify.py`),
independent breaker (`breaker.py`), and hash manifest (`FROZEN.sha256`) were
committed, pushed, and publicly read back from GitHub at
`632f59e97c169abe937e00a6d92642f32378d767` before execution.

On the first formal invocation, `verify.py` exited nonzero (`exit_code: 1`) on
line 456 inside `check_k1_exhaust()` before any scientific check or stdout line
was emitted, due to an arithmetic sum defect in the test-box cardinality
assertion (`len(states) != 3528` for the three disjoint sub-boxes of sizes
`6 * 6 * 3 * 7 * 2 = 1512`, `3 * 3 * 3 * 2 * 4 * 2 = 432`, and
`10 * 4 * 3 * 2 = 240`, whose actual sum is `1512 + 432 + 240 = 2184`).

Under `POLICY.md` Section 3 (Abandoned pins), a run that exits nonzero on a
fixture defect yields no exact stdout to pin and no completed gate, so no
`EXPECTED.txt` and no `RUN.md` exist to commit. All six frozen files
(`PREREG.md`, `PROOF.md`, `SOURCE.md`, `verify.py`, `breaker.py`, and
`FROZEN.sha256`) remain unchanged.

## The identifier is consumed

The identifier `P-INTEGER-K1-SCALED-BRIDGE-1` is consumed and must not be
reused, renamed, repaired, rerun, or resumed. The retargeted probe is carried
out under the fresh successor identifier `P-INTEGER-K1-SCALED-BRIDGE-2`, which
names this abandoned predecessor and the state-count sum defect in its own
preregistration before its own immutable pin.
