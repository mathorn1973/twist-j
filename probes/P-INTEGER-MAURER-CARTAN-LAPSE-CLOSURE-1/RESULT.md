# Result

Status: ABANDONED
Scope: NON-CANONICAL, NEW_DECLARED L1
Probe: P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-1
Ownership: https://github.com/mathorn1973/twist-j/issues/1669
Pin: 41632126fd35240808f104ba2049f88a3d245d0c

## Why the formal gate never completed

On its first execution after remote pin readback (`41632126fd35240808f104ba2049f88a3d245d0c`), `verify.py` exited nonzero (`exit_code = 1`) at line 490 inside `forced_action(x, alpha, a_val)`. While all carrier, Maurer-Cartan factorization, degree-2/3/4 off-shell commutator closure, Bianchi 2-cocycle, and equilibrium solver checks completed, `forced_action` added `-Q(a_val, 8) * (x[0][5] + x[-1][5]) + e_eq / 2` to `res[0]` after adding `(quad(vmat, x_tilde[0]) + quad(vmat, x_tilde[-1])) / 4`, overlooking that the boundary terms $+\frac{1}{4}(\tilde q_0^\mathsf{T} V \tilde q_0 + \tilde q_T^\mathsf{T} V \tilde q_T)$ already cancel the endpoint quadratic terms $-\frac{1}{4}(\tilde q_0^\mathsf{T} V \tilde q_0 + \tilde q_T^\mathsf{T} V \tilde q_T)$ of the end bonds $b = 1$ and $b = T$, so the exact $s = 0$ constant offset is simply `-e_eq` (with no endpoint linear term). Because `main()` returned `1` (`exit_code = 1`), the formal gate (`exit_code == 0`) never completed, and per `POLICY.md` Section 3 ("Abandoned pins") no `EXPECTED.txt` and no `RUN.md` exist to commit. All six frozen files (`PREREG.md`, `PROOF.md`, `SOURCE.md`, `verify.py`, `breaker.py`, and `FROZEN.sha256`) remain byte-identical to the pin `41632126fd35240808f104ba2049f88a3d245d0c`.

## Disposition

The identifier `P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-1` is consumed and must not be reused, renamed, or resumed. The probe is retargeted under the new identifier `P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-2` on branch `probe/P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-2` under ownership issue `#1669`.
