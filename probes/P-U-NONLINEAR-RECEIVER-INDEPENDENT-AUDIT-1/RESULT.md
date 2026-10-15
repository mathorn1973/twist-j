# Result: P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-1

Status: ABANDONED

Public lock: `#1534`.
Immutable pin: `8edb5ea97bf38337d9c65f08964a0ae9e2ed7743`.

## Why the gate did not complete

The frozen preregistration (`PREREG.md`), independent proof (`PROOF.md`),
audit script (`break.py`), wrapper (`verify.py`), source manifest
(`SOURCES.tsv`), README (`README.md`), and input hash manifest
(`INPUTS.sha256`) were committed, pushed, and publicly read back from GitHub at
`8edb5ea97bf38337d9c65f08964a0ae9e2ed7743` before execution.

On the first invocation under the default system `python3` (`/usr/bin/python3`,
Python `3.9.6`), the process exited nonzero (`exit_code: 1`) on `n.bit_count()`
in `theta_bit`, and line 487 of `break.py` contained an internal fixture defect
asserting `len(expected_tail_zqr) == 10` on the $2 \times 2 \times 5 = 20$-element
comprehension `{(z, q, (z - A - q) % 5) for z in (1, 4) for A in (1, 4) for q in F5}`
after Stages 0–5 (custody, all 78,125 generator/involution/affine/quotient
checks, all 31,250 chart roundtrips and 25x625 fibres, the 25-pair $n=0$ prefix,
all 5,000 states and 10,000 edges of $\mathcal{S}_{5000}$, and the 500-state
tail carrier with 25,625 trajectory checkpoints) had passed.

Under `POLICY.md` (Abandoned pins), a pin that exits nonzero on an execution or
fixture defect yields no completed formal gate, so no `EXPECTED.txt` and no
`RUN.md` exist to commit. The frozen `PREREG.md`, `PROOF.md`, `README.md`,
`SOURCES.tsv`, `INPUTS.sha256`, `break.py`, and `verify.py` remain unchanged.

## The identifier is consumed

The identifier `P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-1` is consumed and must
not be reused, renamed, repaired, rerun, or resumed. The retargeted independent
audit is carried out under the fresh successor identifier
`P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-2`, which names this abandoned
predecessor and the fixture defect in its own preregistration before its own
immutable pin.
