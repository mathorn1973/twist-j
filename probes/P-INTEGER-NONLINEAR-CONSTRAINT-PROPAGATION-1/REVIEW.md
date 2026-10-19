# Review: P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1

Status: APPROVED FOR CLAIMED SCOPE (`PASS`, `NON-CANONICAL`, `L1`)  
Prospective pin: `5e072359a029233d1c2b266c0c4bed2269752535`  
Ownership: https://github.com/mathorn1973/twist-j/issues/1651

## 1. Predecessor audit and obligation alignment

Before designing this probe, the predecessor series (#1644, #1646, #1648,
#1650) was audited:
- Post-run scope and errata dispositions on `#1644` ([6272358961](https://github.com/mathorn1973/twist-j/pull/1644#issuecomment-6272358961))
  and `#1648` ([6272438292](https://github.com/mathorn1973/twist-j/pull/1648#issuecomment-6272438292))
  were completed and verified on `x86_64` and `aarch64`.
- `P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1` (#1650) was independently replayed
  and reviewed in [6272491077](https://github.com/mathorn1973/twist-j/pull/1650#issuecomment-6272491077),
  identifying the first nonlinear (cubic) constraint-coupled action and
  discrete Hamiltonian/momentum constraint propagation as the decisive next
  gravitational obligation.

## 2. Analytical and implementation checks

1. **Incidence factorization and circulant Green identity.**
   Verified `L = B_5^T W_e B_5 = L_int / 324` on the 10-edge planar graph
   `E_5` (`w_1 = 29/324`, `w_2 = 65/324`) and the exact matrix identity
   `L_int L_adj = L_adj L_int = 53605 Pi_0 = 10721 (5 I_5 - e e^T)`. In
   `verify.py`, `tau_n` is computed via the closed-form circulant operator
   `(162/53605) L_adj e_loc,n`; in `breaker.py`, `2 L tau_n = Pi_0 e_tot,n`
   is solved independently on `e^perp` by 4x4 Gaussian elimination in the
   basis `e_i - e_4` (`i = 0, 1, 2, 3`) and checked against `L_adj`.

2. **Off-shell pointwise continuity and dipole interaction current.**
   Verified that resolving the source bond energy on `sigma = (1/2, 1/2, 0, 0, 0)`
   and the interaction energy on `e_int,n(r)` produces the dipole residual
   `(g/2) q_chi,n (sigma_r <ell, h_n> - ell_r h_n(r))`, which equals
   `-(B_5^T j_int,n)(r)` for the dipole-edge current
   `j_int,n(e) = -(g/4) q_chi,n (h_n(0) + h_n(1)) delta_(e, e_0)`. The
   resulting off-shell continuity identity and off-shell Bianchi identity
   were checked symbolically and across all 6 off-shell 3-slice test
   configurations.

3. **48-coordinate cubic local action and off-gauge backreaction.**
   Verified that `A_cubic,loc` has degree at most 2 in each of its 48
   coordinates when the other 47 are held fixed, so central unit differences
   equal exact analytical partial derivatives with zero truncation error.
   Checked all 5760 on-shell/on-gauge derivatives (all zero) and all 288
   off-shell/off-gauge derivatives (matching the closed-form analytical
   gradient, including the shift-to-field backreaction witness
   `(943/1679616, -157/279936, 0, 0, 0)`).

4. **Prospective custody and frozen integrity.**
   All six frozen files (`PREREG.md`, `PROOF.md`, `SOURCE.md`, `verify.py`,
   `breaker.py`, `FROZEN.sha256`) were committed at
   `5e072359a029233d1c2b266c0c4bed2269752535`, pushed to GitHub, read back via
   `gh api`, and recorded on issue #1651 before the first execution of
   `verify.py`. All six files remain byte-identical after execution.
