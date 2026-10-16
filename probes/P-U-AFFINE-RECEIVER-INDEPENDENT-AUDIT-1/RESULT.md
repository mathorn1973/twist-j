# Result: P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-1

Status: ABANDONED

Public lock: `#1521`.
Immutable pin: `8d6112604793dfbd6fbf4f229ba74d80d3c07a41`.

## Why the gate did not complete

The frozen preregistration (`PREREG.md`), independent audit script (`break.py`),
and wrapper (`verify.py`) were committed, pushed, and publicly read back from
GitHub at `8d6112604793dfbd6fbf4f229ba74d80d3c07a41` before execution.

On the first formal invocation, all exhaustive scientific checks passed (all
15,625-state generator/matrix/involution/trace checks, 62,500 global chart
inverse checks, the 500-state continuation carrier and 1,000 transitions,
all 25,500 late trajectory state checks, all 0011 launch window checks, and
all 15,625 origin-zero $x_2 + x_3 \in \{t_3, t_4\}$ checks), after which the
process exited nonzero (`exit_code: 1`) on line 543 of `break.py` due to a
fixture defect in the auxiliary sharpness witness tuple `x0_w2 = (0, 0, 0, 0, 1, 1)`
(under $g_2 \circ g_2$, $q_2 = q_0 = 1 \ne 0$, whereas `x0_w2 = (0, 0, 0, 0, 0, 0)`
has $q_2 = 0$).

Under `POLICY.md` (Abandoned pins), a run that exits nonzero on a fixture
defect yields no exact stdout to pin and no completed gate, so no
`EXPECTED.txt` and no `RUN.md` exist to commit. The frozen `PREREG.md`,
`break.py`, and `verify.py` remain unchanged.

## The identifier is consumed

The identifier `P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-1` is consumed and must
not be reused, renamed, repaired, rerun, or resumed. The retargeted audit is
carried out under the fresh successor identifier
`P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-2`, which names this abandoned
predecessor and the fixture defect in its own preregistration before its own
immutable pin.
