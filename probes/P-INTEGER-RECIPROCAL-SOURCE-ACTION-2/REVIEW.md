# Analytical, static, and post-pin review receipt

Status: NON-CANONICAL, L1 review context  
Probe: P-INTEGER-RECIPROCAL-SOURCE-ACTION-2  
Pin: 3ae3ea66e1e3c633c048ece10e3baf43f144d8c7

This receipt records both the pre-pin static checks and the post-pin public
review findings (`https://github.com/mathorn1973/twist-j/pull/1644#issuecomment-6267871040`).
The six frozen files in `3ae3ea66e1e3c633c048ece10e3baf43f144d8c7` and
`EXPECTED.txt` remain unmodified.

## Predecessor pin disclosure

An earlier probe directory `P-INTEGER-RECIPROCAL-SOURCE-ACTION-1` was pinned on
issue #1642 at commit `a369fbf85feb79a2a10716b8bd7efd9ff8da5814` and failed its
first formal execution with `FALSIFIER=INITIAL_DATA` because the literal
`beta(w)` table had `0` instead of `+1` for word `0100` and `0` instead of `-1`
for word `1101`. In accordance with `POLICY.md` Section 3,
`P-INTEGER-RECIPROCAL-SOURCE-ACTION-1` was preserved and closed as
`Status: FAIL` on its own branch and Draft PR #1643.
`P-INTEGER-RECIPROCAL-SOURCE-ACTION-2` was then created as a new probe directory
with corrected literal `beta(w)` values and pinned prospectively before any
scientific execution.

## Actual implementation encodings in the frozen pin

- `verify.py` implements the polynomial quotient ring
  `Z[j] = Z[x]/(1+x+x^2+x^3+x^4)` with `2x2` Hermitian matrix multiplication,
  explicit operator matrices `C` and `L`, and rational arithmetic via
  `fractions.Fraction`.
- `breaker.py` independently implements direct 8-coordinate integer formulas on
  `Herm_2(Z[j])`, explicit `C` and `L` matrices, and exact rational arithmetic.
  Neither implementation uses a Gaussian-elimination Green solver.

## Post-pin public review corrections and errata

The initial post-run summary (`d47c813c`) mistakenly described an earlier draft
design (`S^(beta(P))`, mod-3 `beta`, `Ad_{M_0}` decomposition, and an adjoint
multiplier action) rather than the actual frozen construction in
`3ae3ea66e1e3c633c048ece10e3baf43f144d8c7`. In response to the public reviews on
PR #1644 (`https://github.com/mathorn1973/twist-j/pull/1644#issuecomment-6267871040`
and `https://github.com/mathorn1973/twist-j/pull/1644#issuecomment-6270220560`),
`RESULT.md`, `REVIEW.md`, and `README.md` have been corrected so that they
describe only the actual frozen pin and record the following explicit errata in
the frozen `PROOF.md` / `PREREG.md` text:

1. **Actual phase-6 update:** `Phi(P,Q) = (P_0 mod 2 - P_1 mod 2) - (Q_0 mod 2 - Q_1 mod 2)`
   updates `s' = s + Phi(P,Q)` while leaving `H` unchanged. On ready histories,
   `Phi(P,Q) = beta(w) = Phi(P_1, P_0)` at the first field gate (`k=1 -> 2`) and
   vanishes for `k >= 2` because `P_n == P_1 (mod 2)`.
2. **Mixed variational property (not continuous source stationarity):** The
   frozen action `A_rec` has source derivative
   `dA_rec / d(chi_n) = (chi_{n+1} - chi_n + chi_{n-1} - f) + <ell, h_n>/324^n = r_n + tau_n`
   (the off-shell formula printed in `PROOF.md` lines 627-629 / `PREREG.md`
   lines 306-308 has the wrong sign on `r_n`). On the selected trajectories
   `r_n = 0`, leaving a **generally nonzero** residual gradient `tau_n` (e.g.
   `1/209952` at word `0010`, `a=0`, `n=2`). The 720 executable checks verify 600
   vanishing reduced TT metric variations and 120 source variations equal to
   `tau_n` together with single-coordinate integer shift optimality
   `A_rec(chi) - A_rec(chi + k e_n) = k^2/2 - k tau_n > 0` for `k in Z \ {0}`
   with neighbor `chi` values held fixed.
3. **Additional frozen-proof errata recorded in `RESULT.md`:**
   - The true nonzero eigenvalues of `L` are `(235 +/- 18*sqrt(5))/324` (not
     `36*sqrt(5)`), which still satisfy the Green bound `5/2` and the true
     uniform response bound `1645/209304 < 1/125` for `|chi_n| <= 6`.
   - The telescoping display in `PROOF.md` lines 321-326 is replaced by adding
     the autonomous source sequence `chi_n^auto = a*(1,2,2,1,0,0)_n` separately
     to the `beta`-driven impulse response `q_n` satisfying
     `q_{t+1} - q_t + q_{t-1} = beta(w) delta_{t,1}` with `q_0 = q_1 = 0`.
   - In `PROOF.md` section 4.1, `N(D_0) = 4` (not `6`), `N(A^-1 D_0) = 14` (not
     `16`), and the squared norms of `P_2` (free / minus / plus) are `344982`,
     `343694`, `346286`.
   - `PROOF.md` section 3.2 (the claimed secular-resonance no-go for unreduced
     feedback) is withdrawn as a theorem.
