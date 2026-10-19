# Cubic constraint-coupled integer metric-and-source model with discrete Bianchi propagation

NON-CANONICAL, L1. Ownership:
https://github.com/mathorn1973/twist-j/issues/1651.

This successor to `P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1` (#1650) addresses the
next open gravitational obligation: it extends the autonomous positive-kinetic
coupled TT-and-scalar-source action by the **first nonlinear (cubic)
gravitational constraint-coupling terms** on the five-site planar incidence
carrier `(X = Z/5, E_5, B_5, W_e)` with `L = B_5^T W_e B_5`, and proves
**exact discrete Hamiltonian and momentum constraints together with their
all-step propagation (discrete Bianchi / co-closure identity)** and an
**autonomous integer lift** of the full dynamical and constraint records.

## Main exact results

1. **Local stress-energy-momentum resolution and exact off-shell continuity.**
   The conserved positive bond energy `Htot_n` of #1650 resolves onto the
   five vertices `r in Z/5` as `e_tot,n(r) = e_loc,n(r) + E_*/5`
   (`sum_r e_tot,n(r) = Htot_n`) and onto the ten oriented edges `e in E_5`
   as `j_tot,n = j_h,n + j_int,n`, with dipole interaction current
   `j_int,n(e) = -(g/4)(chi_(n+1) - chi_(n-1))(h_n(0) + h_n(1)) delta_(e, e_0)`.
   For arbitrary off-shell three-slice data,

       (e_tot,n+1(r) - e_tot,n(r)) + (B_5^T j_tot,n)(r)
         = (1/2) q_h,n(r) R_h,n(r) + (1/2) sigma_r q_chi,n R_chi,n.

2. **Cubic constraint-coupled action and 48-coordinate exact variations.**
   Coupling `A_auto` to `ell_hom,n`, `ell_lapse,n in e^perp`, `tau_n in e^perp`,
   `N_shift,n in Q^10`, and `p_n in K_E = ker B_5^T` yields the dynamical
   equations `R_h,n = 0`, `R_chi,n = 0`, the homogeneous constraint
   `Htot_n = E_hom`, the Discrete Hamiltonian Constraint
   `2 L tau_n = Pi_0 e_tot,n`, and the Discrete Momentum Constraint
   `2(W_e B_5(tau_(n+1) - tau_n) + p_n) + j_tot,n = 0`. All 5760 on-shell
   and 288 off-shell/off-gauge central unit differences of the 48-coordinate
   local cubic action match the exact analytical derivatives.

3. **Closed-form circulant Green operator and discrete Bianchi propagation.**
   With `(L_adj v)_r = 188 v_r - 65(v_(r-1) + v_(r+1)) - 29(v_(r-2) + v_(r+2))`,
   the exact identity `L_int L_adj = L_adj L_int = 53605 Pi_0` gives the
   solver-free Hamiltonian constraint solution `tau_n = (162/53605) L_adj e_loc,n`,
   and the momentum record satisfies the exact off-shell Bianchi identity

       B_5^T p_n = -(1/4) Pi_0 [ q_h,n * R_h,n + q_chi,n R_chi,n sigma ],

   vanishing identically on-shell (`p_n in K_E = ker B_5^T` at every step).

4. **Autonomous integer constraint lift on the unrestricted carrier.**
   On every core `x = (Z, R, D, H)` and its bare image `T(x)`, the scaled
   records `E_int(x) = 4 m D^2 e_loc(x) in Z^5`,
   `Theta(x) = L_adj E_int(x) = 428840 D^2 tau(x) in Z^5`,
   `J_int(x) = 4 m^2 D^2 j_tot(x) in Z^10`, and
   `Pi_int(x) = 8 * 53605 m^3 D^2 p(x) in Z^10` are exact integer vectors
   satisfying `sum_r Theta_r(x) = 0`, `L_int Theta(x) = 53605 Pi_0 E_int(x)`,
   `(E_int(T(x)) - m^2 E_int(x)) + m B_5^T J_int(x) = 0`, and
   `B_5^T Pi_int(x) = 0` in `Z^5`.

## Read and reproduce

| File | Purpose |
| --- | --- |
| `PREREG.md` | Prospective incidence carrier, cubic action, integer lift, and certificate |
| `PROOF.md` | Complete analytical proofs and symbolic witness derivations |
| `SOURCE.md` | Normative authority hashes, companion provenance, and explicit L1 choices |
| `verify.py` | Primary implementation: integer recurrence, `Z[j]` ring, circulant `L_adj` |
| `breaker.py` | Secondary implementation: rational evolution, direct Hermitian, 4x4 Gaussian solver |
| `FROZEN.sha256` | Five-file prospective manifest frozen at `5e072359a029233d1c2b266c0c4bed2269752535` |
| `EXPECTED.txt` | Unmodified first formal stdout (`1160` bytes, `32` lines) |
| `RUN.md` | First run metadata and prospective pin custody |
| `RESULT.md` | Observed finite certificate, witnesses, and scope boundaries |
| `REVIEW.md` | Analytical/static review record |

From the repository root, run with Python 3.12 and the standard library:

```sh
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 probes/P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1/verify.py
```

## Limits

This probe has scope `NON-CANONICAL, L1`. Full non-perturbative 4D Einstein
equations, 125-site 3D spatial source coupling, native-U derivation,
continuum manifold limits, and physical SI calibration remain open.
