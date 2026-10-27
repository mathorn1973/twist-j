# Result

Status: ABANDONED
Scope: NON-CANONICAL, NEW_DECLARED L1
Probe: P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-2
Ownership: https://github.com/mathorn1973/twist-j/issues/1669
Pin: 2fe6646b83f4a4a5f6bd8a7af767f3859134f637

## Why the formal gate never completed

On its first execution after remote pin readback (`2fe6646b83f4a4a5f6bd8a7af767f3859134f637`), `verify.py` completed every scientific check in `audit()` (`PAYLOAD_SHA256 = 61a0a26870a30489eae5687650acfae4b58e9af62c556385ea7f87fd7342db97`), but exited nonzero (`exit_code = 1`) at `F_BREAKER` because `breaker.py` exited nonzero (`exit_code = 1`) at line 237 (`F_POLY_SERIES`). Specifically, `breaker.py` lines 203–215 wrote the unnormalized Taylor numerators instead of the ordinary power-series coefficients $E_3 = -\frac{1}{6}(5C + C^3)$, $E_4 = \frac{1}{24}(5I_6 + 18C^2 + C^4)$, $A_2 = C$, $A_3 = -\frac{1}{3}(I_6 + 2C^2)$, and $A_4 = \frac{1}{3}(2C + C^3)$ in $B(s)E(s) = I_6 + O(s^5)$ and $E(s)U(s) = A(s) + O(s^5)$. Because `main()` returned `1` (`exit_code = 1`), the formal gate (`exit_code == 0`) never completed, and per `POLICY.md` Section 3 ("Abandoned pins") no `EXPECTED.txt` and no `RUN.md` exist to commit. All six frozen files (`PREREG.md`, `PROOF.md`, `SOURCE.md`, `verify.py`, `breaker.py`, and `FROZEN.sha256`) remain byte-identical to the pin `2fe6646b83f4a4a5f6bd8a7af767f3859134f637`.

## Disposition

The identifier `P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-2` is consumed and must not be reused, renamed, or resumed. The probe is retargeted under the new identifier `P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-3` on branch `probe/P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-3` under ownership issue `#1669`.
