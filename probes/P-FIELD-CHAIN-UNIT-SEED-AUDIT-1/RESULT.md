# Result: P-FIELD-CHAIN-UNIT-SEED-AUDIT-1

Status: ABANDONED.

The single formal execution attempt at pin `46e0ba7e4dafd9bb391253c9e888cfc54db574c2` exited nonzero (`exit_code: 1`) on a hand-transcribed off-diagonal sign error in the hardcoded constant matrix `ADJ_B_F` (`assert mat_mul(B_F, ADJ_B_F) == mat_scale(5, I4)` at line 156 of `verify.py`) before any unit-shell solver, box enumeration, residue classification, or coset-minimum computation ran. Because the formal gate never completed, it produced no scientific stdout and no scientific conclusion; accordingly, no `EXPECTED.txt` and no `RUN.md` exist.

The frozen `PREREG.md` and `verify.py` are preserved unchanged. The identifier `P-FIELD-CHAIN-UNIT-SEED-AUDIT-1` is consumed and must not be reused. The unchanged review specification, equations, domains, thresholds, and falsifiers are retargeted under the successor identifier `P-FIELD-CHAIN-UNIT-SEED-AUDIT-2` with the corrected adjugate cofactor matrix.
