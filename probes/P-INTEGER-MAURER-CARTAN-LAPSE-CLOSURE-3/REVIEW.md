# Review record

Scope: NON-CANONICAL, NEW_DECLARED L1, conditional candidate-T, forces `a in {-1, 0, 1}`.
This is a post-pin source and proof review.

## Custody and review independence

The six scientific files of `P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-3` were
publicly frozen at `04e21ecf4a866cd861d875706050006e0d0fbd59`. All six files,
their byte sizes, SHA-256 digests, and Git blob IDs were read back from the
GitHub API before first execution and recorded in the pre-execution receipt:
https://github.com/mathorn1973/twist-j/issues/1669#issuecomment-6286325093.
`FROZEN.sha256` binds the other five frozen files. No frozen file was modified
after the pin commit.

Two earlier pins in this investigation were retired without modifying their
frozen files and recorded as `Status: ABANDONED` (`#1672` at `41632126` due to
an endpoint constant in `forced_action`, and `#1673` at `2fe6646b` due to a
missing factorial normalization in `breaker.py` polynomial series conversion).
This review is a same-session, analytically exposed review of the third pin
`04e21ecf4a866cd861d875706050006e0d0fbd59`.

## Mathematical assessment

1. **Maurer-Cartan curvature factorization (Theorem 1):** Because S(q, s) is
   quadratic in q with Hessian H(s) and satisfies partial_t S + (L_t(s) q) . nabla_q S = 0,
   differentiating with respect to q yields the covariant identity
   partial_t H + L_t^T H + H L_t = 0. Adding A_t(s) H(s) q with A_t^T = -A_t
   leaves delta_tilde_t S = 0 intact and shifts L_t -> L_tilde_t = L_t + A_t H,
   so [delta_tilde_t, delta_tilde_r] q = F_{t,r}(s) H(s) q with F_{t,r}(s)
   given by the covariant Maurer-Cartan curvature formula including the
   quadratic term A_r H A_t - A_t H A_r.

2. **Degree-3 2-bond and degree-4 3-bond closure (Theorems 2 and 3):** At
   O(s), R_{t,r}^{(1)}(s) has bandwidth 2 (couplings |m-n| = 1 in C and
   |m-n| = 2 in I_6). Evaluating [R_{t,r}^{(1)} H_0 q]_1 on the `#1666`
   witness state reproduces (-395/5184, 0, 395/5184, -1/144, 1/144, -1/5184)
   exclusively from the (1, 3) block. The 2-bond skew primitive A_t^{(2)}(s)
   satisfies partial_r A_t^{(2)} - partial_t A_r^{(2)} = R_{t,r}^{(1)}(s) with
   zero boundary defect. At O(s^2), the nonlinear curvature contribution
   A_r^{(1)} H_0 A_t^{(1)} - A_t^{(1)} H_0 A_r^{(1)} is essential to close the
   Bianchi 2-cocycle on (n, n+3); with it included, A_t^{(3)}(s) (including
   its Dirichlet boundary shift at (1, 2) and (T-2, T-1)) cancels F_{t,r}^{(2)}(s)
   identically across all tested horizons.

3. **Forced affine completion and vacuum cold-start shell (Theorem 4):** On
   1_5^perp (+) Q, V = K_mat + G_mat has positive determinant and unique
   equilibrium x_*. Because the baseline step uses the midpoint force
   (1/2) f_* (q_b + q_{b+1}), shifting q_b = x_* + q_tilde_b leaves a telescopy
   residual (1/2) f_*^T (q_tilde_0 - q_tilde_T) at the boundaries, so the
   initial canonical momentum is p_tilde_0 = q_0 - q_{-1} + (1/2) f_*. For the
   vacuum cold start q_{-1} = q_0 = 0, p_tilde_0 = (1/2) f_* contributes
   (1/8)||f_*||^2 to the shifted bond energy, which adds to
   E_cold = E_* - (1/8)||f_*||^2 to equal E_* identically. Thus the `#1650`
   cold-start trajectory is stationary under free independent variations of
   every bond lapse s_b in S^{(a)}(q, s) while executing non-trivial metric
   oscillations.

## Source and security assessment

Both `verify.py` and `breaker.py` use only Python standard-library modules
(`fractions`, `hashlib`, `pathlib`, `subprocess`, `sys`) and exact rational
arithmetic (`Fraction`). Authority file reads are restricted to the 5 normative
files from `#1646`, `#1650`, `#1662`, `#1664`, and `#1666`. `verify.py` invokes
`breaker.py` via `[sys.executable, "-I", str(BREAKER_PATH)]` with a 540-second
timeout and verifies exit code 0, empty stderr, and byte-for-byte identity of
the 15-line certificate before emitting `BREAKER_RAW_BYTES=IDENTICAL` and
`RESULT=PASS`. There are no network calls, file writes, or dynamic code
evaluation paths.
