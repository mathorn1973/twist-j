# Local continuity, auxiliary constraint propagation, and integer Hodge lift on the coupled metric-source carrier

NON-CANONICAL, L1. Ownership:
https://github.com/mathorn1973/twist-j/issues/1651.

This successor to `P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1` (#1650) resolves the
interaction-inclusive bond energy onto the five-site planar incidence carrier
`(X = Z/5, E_5, B_5, W_e)` with `L = B_5^T W_e B_5`, establishes an exact
off-shell pointwise continuity identity, proves compatibility and propagation
of a declared auxiliary Hamiltonian and momentum constraint system, and
constructs a four-scale integer lift on the inherited 21-coordinate carrier.

## Main exact results

1. **Local stress-energy-momentum resolution and exact off-shell continuity.**
   The conserved bond energy `Htot_n` of #1650 resolves onto the five vertices
   `r in Z/5` as `e_tot,n(r) = e_loc,n(r) + E_*/5` (`sum_r e_tot,n(r) = Htot_n`)
   and onto the ten oriented edges `e in E_5` as `j_tot,n = j_h,n + j_int,n`,
   with dipole interaction current
   `j_int,n(e) = -(g/4)(chi_(n+1) - chi_(n-1))(h_n(0) + h_n(1)) delta_(e, e_0)`.
   For arbitrary off-shell three-slice data,

       C_n(r) := (e_tot,n+1(r) - e_tot,n(r)) + (B_5^T j_tot,n)(r)
               = (1/2) q_h,n(r) R_h,n(r) + (1/2) sigma_r q_chi,n R_chi,n.

   (Pointwise positivity of the vertex density `e_tot,n(r)` is not claimed.)

2. **Auxiliary constraint compatibility and local 48-coordinate ambient variations.**
   The auxiliary constraints `H_n = 2 L tau_n - Pi_0 e_tot,n` (`tau_n in e^perp`)
   and `M_n = 2 W_e B_5(tau_(n+1) - tau_n) + 2 p_n + j_tot,n`
   (`p_n in K_E = ker B_5^T`) satisfy the exact propagation relation

       H_(n+1) - H_n = B_5^T M_n - 2 B_5^T p_n - Pi_0 C_n,

   so `p_n in ker B_5^T`, `M_n = 0`, and `R_h,n = R_chi,n = 0` propagate
   `H_n = 0`. Zero multipliers `ell_hom,n = 0`, `ell_lapse,n = 0`,
   `N_shift,n = 0` form the **selected sufficient branch** (general constrained
   variations on `p_n in ker B_5^T` and `tau_n, ell_lapse,n in e^perp` allow
   `N_shift,n = B_5 xi_n` and `ell_lapse,n = xi_n - xi_(n-1)`). The `5760`
   on-shell/on-gauge and `288` off-shell/off-gauge derivative checks audit the
   separately defined **local 48-coordinate ambient functional** `A_cubic,loc`
   centered at slice `n` (which includes only `N_shift,n . j_tot,n`; see
   `RESULT.md` Section 4 for the neighboring-slice shift-current witness
   `grad_(h_2)(N_shift,1 . j_tot,1) = (29/10368, 29/10368, 0, 0, 0)` and
   `d/d(chi_2)(N_shift,1 . j_tot,1) = -17/51840`).

3. **Closed-form circulant Green operator and discrete Bianchi co-closure.**
   With `(L_adj v)_r = 188 v_r - 65(v_(r-1) + v_(r+1)) - 29(v_(r-2) + v_(r+2))`,
   the exact identity `L_int L_adj = L_adj L_int = 53605 Pi_0` gives the
   solver-free Hamiltonian constraint solution `tau_n = (162/53605) L_adj e_loc,n`,
   and the momentum record satisfies the exact off-shell co-closure identity

       B_5^T p_n = -(1/4) Pi_0 [ q_h,n * R_h,n + q_chi,n R_chi,n sigma ],

   vanishing identically on-shell (`p_n in K_E = ker B_5^T` at every step).

4. **Autonomous four-scale integer lift on the 21-coordinate carrier.**
   On every core `x = (Z, R, D, H)` (21 coordinates; 23 with bank and direction)
   and its bare image `T(x)`, the four scaled records
   `E_int(x) = 4 m D^2 e_loc(x) in Z^5`,
   `Theta(x) = L_adj E_int(x) = 428840 D^2 tau(x) in Z^5`,
   `J_int(x) = 4 m^2 D^2 j_tot(x) in Z^10`, and
   `Pi_int(x) = 8 * 53605 m^3 D^2 p(x) in Z^10` are exact integer vectors
   satisfying `sum_r Theta_r(x) = 0`, `L_int Theta(x) = 53605 Pi_0 E_int(x)`,
   `(E_int(T(x)) - m^2 E_int(x)) + m B_5^T J_int(x) = 0`, and
   `B_5^T Pi_int(x) = 0` in `Z^5`.

## Read and reproduce

| File | Purpose |
| --- | --- |
| `PREREG.md` | Prospective incidence carrier, cubic functional, integer lift, and certificate |
| `PROOF.md` | Complete analytical proofs and symbolic witness derivations |
| `SOURCE.md` | Normative authority hashes, companion provenance, and explicit L1 choices |
| `verify.py` | Primary implementation: integer recurrence, `Z[j]` ring, circulant `L_adj` |
| `breaker.py` | Secondary implementation: rational evolution, direct Hermitian, 4x4 Gaussian solver |
| `FROZEN.sha256` | Five-file prospective manifest frozen at `5e072359a029233d1c2b266c0c4bed2269752535` |
| `EXPECTED.txt` | Unmodified first formal stdout (`1160` bytes, `32` lines) |
| `RUN.md` | First run metadata and prospective pin custody |
| `RESULT.md` | Observed finite certificate, witnesses, scope boundaries, and post-review errata |
| `REVIEW.md` | Analytical/static review record and post-review scope notes |

From the repository root, run with Python 3.12 and the standard library:

```sh
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 probes/P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1/verify.py
```

## Limits

This probe has scope `NON-CANONICAL, L1`. The physical evolution on the
selected zero-multiplier branch is the autonomous linear TT/source law of
`#1650` (`g_00 = -1`, `-1/4 < h_n(r) < 13/20`). Full global multi-slice
action derivatives and off-shell Noether compensation are addressed in
`P-INTEGER-CUBIC-NOETHER-CLOSURE-1` (`#1653`, `#1654`). Full non-perturbative
4D Einstein equations, 125-site 3D spatial source coupling, native-U
derivation, continuum manifold limits, and physical SI calibration remain open.
