# Result

Status: ABANDONED  
Scope: NON-CANONICAL, NEW_DECLARED L1  
Probe: P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-1  
Ownership: https://github.com/mathorn1973/twist-j/issues/1655  
Pin: 4572a78b05994485248db6b480c329b12b335365

## Why the formal gate never completed

On its first execution after remote pin readback (`4572a78b05994485248db6b480c329b12b335365`),
`verify.py` exited nonzero (`exit_code = 1`) with `0` stdout bytes and an
uncaught Python `KeyError: 'T'` at line 373 inside `sint_grad_x(y, mtilde, homogeneous=True)`.
In `verify.py`, `generator(x, psi_m)` constructs the tangent dictionary `y` via
`zeros(t)` (which initializes only the scalar and vector slice arrays and omits
the metadata key `"T"`), whereas `sint_grad_x` read `t = x["T"]` instead of
`t = len(x["h"]) - 1`.

Because the run exited nonzero on an implementation dictionary-key defect and
produced no scientific stdout, the formal gate never completed, and per
`POLICY.md` Section 3 ("Abandoned pins") no `EXPECTED.txt` and no `RUN.md` exist
to commit. All six frozen files (`PREREG.md`, `PROOF.md`, `SOURCE.md`,
`verify.py`, `breaker.py`, and `FROZEN.sha256`) remain unchanged from the pin
`4572a78b05994485248db6b480c329b12b335365`.

## Disposition

The identifier `P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-1` is consumed and must
not be reused, renamed, or resumed. The probe is retargeted under the new
identifier `P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-2` on branch
`probe/P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-2`.
