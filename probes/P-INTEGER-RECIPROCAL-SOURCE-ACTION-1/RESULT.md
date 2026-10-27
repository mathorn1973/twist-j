# Result

Status: FAIL  
Scope: NON-CANONICAL, L1  
Probe: P-INTEGER-RECIPROCAL-SOURCE-ACTION-1  
Ownership: https://github.com/mathorn1973/twist-j/issues/1642  
Pin: a369fbf85feb79a2a10716b8bd7efd9ff8da5814

## Observed completed result

On its first formal execution after remote pin readback, `verify.py`
completed with exit code `0`, empty stderr, and the 35-byte, 2-line stdout
(SHA-256 `31e352459901a944bccf26ddae6b75408a9a986f2c66ce770080c823f634444a`):

    FALSIFIER=INITIAL_DATA
    RESULT=FAIL

`EXPECTED.txt` contains those exact bytes and `RUN.md` records the first
local execution custody. All six frozen files (`PREREG.md`, `PROOF.md`,
`SOURCE.md`, `verify.py`, `breaker.py`, and `FROZEN.sha256`) remain
unchanged from the pin `a369fbf85feb79a2a10716b8bd7efd9ff8da5814`.

## Cause of the fired falsifier and disposition

The falsifier `INITIAL_DATA` fired inside `audit_coupling_selection()` at
`require(parity_dipole(p1, p0) == expected_beta, "INITIAL_DATA")` on
canonical word `0100`. For word `0100` (`u0=0, u1=-1`), the canonical
initial slices are `P_0=(1,1,0,0,0)` and `P_1=(1,0,0,0,1)`, so
`Phi(P_1,P_0) = (1-0) - (1-1) = +1`, and for word `1101` (`u0=-1, u1=0`),
`P_0=(1,0,0,0,1)` and `P_1=(1,1,0,0,0)`, so `Phi(P_1,P_0) = (1-1) - (1-0) = -1`.
The literal table column `beta(w)` in `PREREG.md`, `verify.py`, and
`breaker.py` erroneously transcribed `0` instead of `+1` for `0100` and
`0` instead of `-1` for `1101`.

Per `POLICY.md` Section 3, because the formal gate completed and emitted an
exact scientific stdout (`FALSIFIER=INITIAL_DATA`, `RESULT=FAIL`), this
probe is closed by its `FAIL` result with `EXPECTED.txt` and `RUN.md`
preserved. The identifier `P-INTEGER-RECIPROCAL-SOURCE-ACTION-1` is
consumed and must not be reused, renamed, or resumed. The corrected
specification and verifiers are retargeted under the fresh identifier
`P-INTEGER-RECIPROCAL-SOURCE-ACTION-2` on branch
`probe/P-INTEGER-RECIPROCAL-SOURCE-ACTION-2`.
