# Review: P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1

Status: APPROVED FOR NARROWED CLAIMED SCOPE (`PASS`, `NON-CANONICAL`, `L1`)  
Prospective pin: `5e072359a029233d1c2b266c0c4bed2269752535`  
Ownership: https://github.com/mathorn1973/twist-j/issues/1651

## 1. Predecessor audit and obligation alignment

Before designing this probe, the predecessor series (#1644, #1646, #1648,
#1650) was audited:
- Post-run scope and errata dispositions on `#1644` ([6272358961](https://github.com/mathorn1973/twist-j/pull/1644#issuecomment-6272358961))
  and `#1648` ([6272438292](https://github.com/mathorn1973/twist-j/pull/1648#issuecomment-6272438292),
  closed out in [6274577187](https://github.com/mathorn1973/twist-j/pull/1648#issuecomment-6274577187))
  were completed and verified on `x86_64` and `aarch64`.
- `P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1` (#1650) was independently replayed
  and reviewed in [6272491077](https://github.com/mathorn1973/twist-j/pull/1650#issuecomment-6272491077),
  identifying local continuity and discrete Hamiltonian/momentum constraint
  propagation as the next step.

## 2. Analytical and implementation checks

1. **Incidence factorization and circulant Green identity.**
   Verified `L = B_5^T W_e B_5 = L_int / 324` on the 10-edge planar graph
   `E_5` (`w_1 = 29/324`, `w_2 = 65/324`), `dim ker B_5^T = 6`, and the exact
   matrix identity `L_int L_adj = L_adj L_int = 53605 Pi_0 = 10721 (5 I_5 - e e^T)`.
   In `verify.py`, `tau_n` is computed via the closed-form circulant operator
   `(162/53605) L_adj e_loc,n`; in `breaker.py`, `2 L tau_n = Pi_0 e_tot,n`
   is solved independently on `e^perp` by 4x4 Gaussian elimination in the
   basis `e_i - e_4` (`i = 0, 1, 2, 3`) and checked against `L_adj`.

2. **Off-shell pointwise continuity and auxiliary constraint propagation.**
   Verified that resolving the source bond energy on `sigma = (1/2, 1/2, 0, 0, 0)`
   and the interaction energy on `e_int,n(r)` produces the dipole residual
   `(g/2) q_chi,n (sigma_r <ell, h_n> - ell_r h_n(r))`, which equals
   `-(B_5^T j_int,n)(r)` for the dipole-edge current
   `j_int,n(e) = -(g/4) q_chi,n (h_n(0) + h_n(1)) delta_(e, e_0)`. The
   resulting off-shell continuity identity
   `C_n = e_(n+1) - e_n + B_5^T j_n = (1/2) q_h,n * R_h,n + (1/2) sigma q_chi,n R_chi,n`
   and auxiliary constraint propagation relation
   `H_(n+1) - H_n = B_5^T M_n - 2 B_5^T p_n - Pi_0 C_n` were checked
   symbolically and across all 6 off-shell 3-slice test configurations.

3. **Local 48-coordinate ambient cubic functional vs. full global constrained variations.**
   Verified that the separately defined local 48-coordinate ambient functional
   `A_cubic,loc` has degree at most 2 in each of its 48 coordinates when the
   other 47 are held fixed, so central unit differences equal exact analytical
   partial derivatives of `A_cubic,loc` (`5760` on the selected zero-multiplier
   branch and `288` off-shell/off-gauge, including the local shift-to-field
   gradient `(943/1679616, -157/279936, 0, 0, 0)`).
   Per independent review [`#1652#issuecomment-6274568353`](https://github.com/mathorn1973/twist-j/pull/1652#issuecomment-6274568353):
   - Because `p_n in ker B_5^T` and `tau_n, ell_lapse,n in e^perp`, the
     constrained variational equation with respect to `p_n` is
     `P_(ker B_5^T) N_shift,n = 0` (allowing `N_shift,n = B_5 xi_n`,
     `xi_n in e^perp`) and varying `tau_n` gives
     `L ell_lapse,n + B_5^T W_e (N_shift,n-1 - N_shift,n) = 0`
     (`ell_lapse,n = xi_n - xi_(n-1)`), while no general Euler-Lagrange
     equation forces `ell_hom,n = 0`. Zero multipliers therefore form the
     **selected sufficient branch**, not a unique consequence of constrained
     stationarity.
   - Because `A_cubic,loc` centered at slice `n` retains only
     `N_shift,n . j_tot,n`, it omits the neighboring-slice shift-current
     contributions `N_shift,n-1 . j_tot,n-1` and `N_shift,n+1 . j_tot,n+1`
     present in the global action when varying `(h_n, chi_n)` (witnessed on
     word `0011, a = 0, N_shift,1 = delta_(e_0)` at slice `2` by
     `grad_(h_2)(N_shift,1 . j_tot,1) = (29/10368, 29/10368, 0, 0, 0)` and
     `d/d(chi_2)(N_shift,1 . j_tot,1) = -17/51840`). Full global action
     derivatives and off-shell Noether compensation are audited in
     `P-INTEGER-CUBIC-NOETHER-CLOSURE-1` (`#1653`, `#1654`).

4. **Prospective custody and frozen integrity.**
   All six frozen files (`PREREG.md`, `PROOF.md`, `SOURCE.md`, `verify.py`,
   `breaker.py`, `FROZEN.sha256`) were committed at
   `5e072359a029233d1c2b266c0c4bed2269752535`, pushed to GitHub, read back via
   `gh api`, and recorded on issue #1651 before the first execution of
   `verify.py`. All six files and `EXPECTED.txt` remain byte-identical.
