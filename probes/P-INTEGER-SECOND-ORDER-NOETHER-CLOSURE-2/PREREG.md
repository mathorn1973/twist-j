# P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-2

Status: PROSPECTIVE  
Scope: NON-CANONICAL, NEW_DECLARED L1  
Owner: A. M. Thorn (`antigravity-windows-de9b3dcc-e611-4360-a2c9-df8dfe124fd3`)  
Ownership: https://github.com/mathorn1973/twist-j/issues/1655

## 1. Question, authority, custody, and earned-scope boundary

This probe addresses the exact second-order Barnich-Henneaux / Noether
consistency and generator-closure problem identified by
`P-INTEGER-CUBIC-NOETHER-CLOSURE-1` (#1653, #1654):

1. Does the explicit multiplier-dressed second-order action extension
   `S_<=2(epsilon) = S_0 + epsilon S_int + epsilon^2 S_2` together with the
   second-order field transformation `delta_2^(psi) x = G_(Psi[M]) G_psi x`
   satisfy the exact off-shell second-order Noether identity

       delta_0^(psi) S_2 + delta_1^(psi) S_int + delta_2^(psi) S_0 = 0

   on the complete finite-horizon off-shell domain, cancelling the `115/324`
   remainder witness of #1654 and eliminating the pure-gauge field-redefinition
   remainder so that `S_<=2(epsilon)|_(M = Gamma(psi)) = A_auto(x - epsilon G_psi x)`
   holds with zero defect?
2. Does the multiplier-dependent extended generator
   `hat_delta_psi = delta_0^(psi) + epsilon delta_1^(psi) + epsilon^2 delta_2^(psi)`
   cancel the order-`epsilon^2` bare field commutator
   `[delta_1^(psi), delta_1^(eta)] x = (G_eta G_psi - G_psi G_eta) x` via the
   multiplier-to-field cross-commutator
   `(delta_0^(psi) delta_2^(eta) - delta_0^(eta) delta_2^(psi)) x = -(G_eta G_psi - G_psi G_eta) x`,
   so that `[hat_delta_psi, hat_delta_eta]_<=2 = 0` identically off-shell while
   leaving an explicit, calculable third- and fourth-order commutator residual
   `epsilon^3 C_3 + epsilon^4 C_4` and action remainder `epsilon^3 W_3 + epsilon^4 W_4`?
3. Do the common-denominator integer lift of the second-order Noether identity
   at scale `16 m D^3 Q_psi` and the second-order displaced state at common
   denominator `D'' = 80 D^2 Q_psi` hold exactly in integer arithmetic?

A PASS certificate means that all positive second-order identities, the
order-`epsilon^2` commutator cancellation, the exact pure-gauge field
redefinition, the integer lifts, and the explicitly predicted order-`epsilon^3`
and order-`epsilon^4` truncation remainders and ten negative controls match
the frozen specification. It does NOT claim an all-order closed gauge algebra
at `epsilon = 1`, an ADM Poisson bracket algebra, or full nonlinear Einstein
dynamics.

Public Canon v103 `main` and peeled `canon-v103` are at
`dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`; content commit is
`01fb76f6b3b14a6a5ec05d0017ea922390ab6f66`. `SOURCE.md` gives the five
normative hashes, byte sizes, mathematical inputs, and companion pins.

Predecessor `P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-1` (pin
`4572a78b05994485248db6b480c329b12b335365`, PR #1656) exited nonzero on its
first execution with `0` stdout bytes due to a dictionary-key defect (`KeyError: 'T'`
in `sint_grad_x` when applied to a tangent dictionary created by `zeros(t)`
without metadata key `'T'`). Per `POLICY.md` Section 3, that pin is closed as
`Status: ABANDONED` on its own branch, and the corrected implementation is
retargeted here under the fresh identifier
`P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-2`.

Before any scientific execution or import of either implementation, commit
and publish `PREREG.md`, `PROOF.md`, `SOURCE.md`, `verify.py`, `breaker.py`,
and `FROZEN.sha256`. Read all six files back from GitHub and post the
prospective pin receipt on issue #1655. AST parsing, textual review, and
SHA-256 hashing are permitted before the pin; scientific execution or import is
not. Preserve the first completed outcome.

## 2. Inherited finite-horizon carrier, operators, and first-order sectors

Fix `m = 324`, `g = 1/m`, `e = (1,1,1,1,1)`, `ell = (1,-1,0,0,0)`,
`sigma = (1/2,1/2,0,0,0)`, and `a in {-1,0,1}` with `A = a/4`.
Vertices are `r = 0,...,4` modulo 5. The ten oriented edges are:

    edge r:     tail r, head (r+1) mod 5, weight 29/324, r = 0,...,4;
    edge 5+r:   tail r, head (r+2) mod 5, weight 65/324, r = 0,...,4.

With incidence matrix `B`, Euclidean adjoint `B^T`, and diagonal edge weight
matrix `W`:

    L = B^T W B = [188 I - 29(S + S^-1) - 65(S^2 + S^-2)] / 324,
    Pi0 f = f - mean(f) e,
    L_adj = 188 I - 65(S + S^-1) - 29(S^2 + S^-2),
    L_int = 324 L,
    L_int L_adj = 53605 Pi0.

For a horizon `T >= 5` (with `T = 5` in the finite executable audit), the
physical fields are `x_n = (h_n, chi_n) in Q^5 x Q` for `n = 0,...,T`, with
fixed endpoints `x_0, x_T`. Define interior residuals and central differences
for `n = 1,...,T-1`:

    R_h,n   = h_(n+1) - 2 h_n + h_(n-1) + L h_n - g chi_n ell,
    R_chi,n = chi_(n+1) - chi_n + chi_(n-1) - A - g <ell, h_n>,
    q_h,n   = h_(n+1) - h_(n-1),
    q_chi,n = chi_(n+1) - chi_(n-1).

The autonomous action `A_auto[x]`, bond energy density
`e_loc,b = e_h,b + e_chi,b + e_int,b`, equilibrium offset
`E_star = (4342005/8683757) A^2`, bond total energy
`H_b = sum_r e_loc,b(r) + E_star`, and edge current `j_n = j_h,n + j_int,n`
are identical to #1654 (`PREREG.md` Section 2), satisfying the off-shell
continuity identity

    C_n = e_loc,n+1 - e_loc,n + B^T j_n
        = (q_h,n * R_h,n + sigma q_chi,n R_chi,n) / 2.                 (2.1)

The auxiliary fields on every bond `b = 1,...,T` are `tau_b, lambda_b in e^perp`
and `alpha_b in Q`. On every interior slice `n = 1,...,T-1`, `p_n in K_E = ker B^T`
(dimension 6) and `N_n in Q^10`. `E_hom` is a fixed rational parameter. The
zeroth- and first-order action sectors are

    S_0   = A_auto + 2 sum_(b=1)^T <lambda_b, L tau_b>
                   + 2 sum_(n=1)^(T-1) <N_n, W B(tau_(n+1) - tau_n) + p_n>,
    S_int = -sum_(b=1)^T alpha_b (H_b - E_hom)
            -sum_(b=1)^T <lambda_b, e_loc,b>
            +sum_(n=1)^(T-1) <N_n, j_n>.                                (2.2)

Using the bases `V_0,...,V_3` of `e^perp` and `K_0,...,K_5` of `K_E` from #1654,
there are `31 T - 22` independent global coordinates (`133` at `T = 5`).

## 3. Multiplier dressing map, `S_2`, and exact second-order Noether identity

Write `M = (alpha, lambda, N)` for the multiplier sectors and define the
combined bond lapse vector `mu_b = alpha_b e + lambda_b in Q^5` (`b = 1,...,T`).
For any vertex parameter array `psi = (psi_0,...,psi_T)` with `psi_0 = psi_T = 0`,
let `Gamma(psi)` denote the pure-gauge multiplier configuration

    Gamma(psi)_alpha,b  = mean(psi_b - psi_(b-1)),
    Gamma(psi)_lambda,b = Pi0(psi_b - psi_(b-1)),
    Gamma(psi)_N,n      = B psi_n,                                      (3.1)

and let `G_psi` denote the linear nearest-time field operator on `x = (h, chi)`
with zero endpoint rows (`n = 0, T`) and interior rows (`n = 1,...,T-1`)

    (G_psi h)_n   = (1/2) psi_n * (h_(n+1) - h_(n-1)),
    (G_psi chi)_n = (1/2) <sigma, psi_n> (chi_(n+1) - chi_(n-1)).       (3.2)

Define the prefix-sum multiplier dressing map `Psi[M] = (Psi_0[M],...,Psi_T[M])`
by

    Psi_0[M] = 0,
    Psi_n[M] = sum_(b=1)^n mu_b    (n = 1,...,T-1),
    Psi_T[M] = 0.                                                       (3.3)

Under `delta_0^(psi) M = Gamma(psi)` (with `delta_0 x = delta_0 tau = delta_0 p = 0`),
`delta_0^(psi) mu_b = psi_b - psi_(b-1)` and `psi_0 = 0` imply the exact
reproducing identity

    delta_0^(psi) Psi_n[M] = psi_n    for all n = 1,...,T-1.            (3.4)

Consequently, the residual multiplier array

    M_tilde[M] := M - Gamma(Psi[M])                                     (3.5)

(which has `alpha_tilde_b = 0` and `lambda_tilde_b = 0` for `b = 1,...,T-1`,
`alpha_tilde_T = sum_(b=1)^T alpha_b`, `lambda_tilde_T = sum_(b=1)^T lambda_b`,
and `N_tilde_n = N_n - B Psi_n[M]`) is strictly invariant under `delta_0^(psi)`:

    delta_0^(psi) M_tilde[M] = 0.                                       (3.6)

Define the second-order action term `S_2[x, M]` by the two algebraically
equivalent expressions

    S_2[x, M]
      := -D_x S_int[x, M_tilde[M]][G_(Psi[M]) x]
         + (1/2) Hess_(A_auto)[G_(Psi[M]) x, G_(Psi[M]) x]              (3.7a)
       = -D_x S_int[x, M][G_(Psi[M]) x]
         - (1/2) Hess_(A_auto)[G_(Psi[M]) x, G_(Psi[M]) x]
         - D_x A_auto[x][G_(Psi[M]) G_(Psi[M]) x],                      (3.7b)

and define the second-order field variation `delta_2^(psi)` by

    delta_2^(psi) x = G_(Psi[M]) G_psi x,
    delta_2^(psi) of every auxiliary and multiplier variable = 0.       (3.8)

For the second-order action `S_<=2(epsilon) = S_0 + epsilon S_int + epsilon^2 S_2`
and second-order variation `hat_delta_psi = delta_0^(psi) + epsilon delta_1^(psi) + epsilon^2 delta_2^(psi)`
(where `delta_1^(psi) x = G_psi x`), the following hold identically on the
unrestricted off-shell domain:

    delta_0^(psi) S_0 = 0,
    delta_0^(psi) S_int + delta_1^(psi) S_0 = 0,
    delta_0^(psi) S_2 + delta_1^(psi) S_int + delta_2^(psi) S_0 = 0,    (3.9)

and the complete directional derivative along `hat_delta_psi` is

    hat_delta_psi S_<=2(epsilon) = epsilon^3 W_3(psi) + epsilon^4 W_4(psi),
    W_3(psi) := delta_1^(psi) S_2 + delta_2^(psi) S_int,
    W_4(psi) := delta_2^(psi) S_2.                                      (3.10)

Along any straight line `z + t hat_delta_psi z`, `P(t) = S_<=2(z + t hat_delta_psi z; epsilon)`
has degree at most four in `t`. Because `P(t) - P(-t)` is odd in `t`, the
four-point central difference formula

    D_(hat_delta_psi) S_<=2 = [-P(2) + 8 P(1) - 8 P(-1) + P(-2)] / 12   (3.11)

equals the exact directional derivative `P'(0)` with zero truncation error.
Furthermore, in each of the 133 independent global coordinates individually
(with the other 132 held fixed), `S_<=2(epsilon)` has degree at most two, so
its unit centered difference equals its exact partial derivative.

## 4. Exact pure-gauge field-redefinition completion

When the multipliers are set to the pure-gauge values `M = Gamma(psi)` (for
arbitrary `tau in e^perp` and `p in K_E`), `M_tilde[Gamma(psi)] = 0` and
`Psi[Gamma(psi)] = psi`, so

    S_2[x, Gamma(psi)] = (1/2) Hess_(A_auto)[G_psi x, G_psi x].         (4.1)

Combining (4.1) with the first-order Taylor identity of #1654 eliminates the
quadratic field-redefinition remainder identically for all `epsilon`:

    S_<=2(epsilon)|_(M = Gamma(psi)) = A_auto(x - epsilon G_psi x).     (4.2)

## 5. Order-`epsilon^2` extended commutator closure and order-`epsilon^3` residual

For fixed parameters `psi, eta` with `psi_0 = psi_T = eta_0 = eta_T = 0`, the
Lie commutator of the state-space vector fields `hat_delta_psi` and
`hat_delta_eta` acting on `z = (x, tau, p, M)` is

    [hat_delta_psi, hat_delta_eta] z
      = D_z(hat_delta_eta z)[hat_delta_psi z]
        - D_z(hat_delta_psi z)[hat_delta_eta z].                        (5.1)

Its auxiliary and multiplier components vanish identically. On the physical
fields `x = (h, chi)`, because `hat_delta_psi Psi[M] = psi`, the order-`epsilon^2`
multiplier-to-field cross-commutator is

    (delta_0^(psi) delta_2^(eta) - delta_0^(eta) delta_2^(psi)) x
      = (G_psi G_eta - G_eta G_psi) x
      = -[delta_1^(psi), delta_1^(eta)] x,                              (5.2)

which cancels the bare order-`epsilon^2` commutator identically:

    [hat_delta_psi, hat_delta_eta]_<=2 x = 0.                           (5.3)

The exact full commutator of the second-order truncated generators is pure
`O(epsilon^3)`:

    [hat_delta_psi, hat_delta_eta] x
      = epsilon^3 C_3(psi, eta; x, M) + epsilon^4 C_4(psi, eta; x, M),
    C_3(psi, eta; x, M)
      = [G_eta G_(Psi[M]) G_psi - G_psi G_(Psi[M]) G_eta
         + G_(Psi[M])(G_eta G_psi - G_psi G_eta)] x,
    C_4(psi, eta; x, M)
      = G_(Psi[M]) [G_eta G_(Psi[M]) G_psi - G_psi G_(Psi[M]) G_eta] x. (5.4)

## 6. Common-denominator integer lift of the second-order system

Let all field, auxiliary, and multiplier arrays on `n = 0,...,T` be stored as
integer numerators `(P_n, Y_n, T_b, K_n, A_b, Lambda_b, Ncal_n)` over one
positive integer denominator `D`, and let `psi_n = V_n / Q_psi` (`Q_psi >= 1`).
Then `mu_b = M_b / D` with `M_b = A_b e + Lambda_b in Z^5`, and the dressing
numerators

    Psi_hat_n = sum_(b=1)^n M_b in Z^5    (n = 1,...,T-1),
    Psi_hat_0 = Psi_hat_T = 0                                           (6.1)

satisfy `Psi_n[M] = Psi_hat_n / D` without enlarging `D`.

Define the first-order integer tangent quantities `Q_h,n = P_(n+1) - P_(n-1)`,
`Q_chi,n = Y_(n+1) - Y_(n-1)`, `Y_tilde_h,n = V_n * Q_h,n in Z^5`, and
`Y_tilde_chi,n = (V_n(0) + V_n(1)) Q_chi,n in Z` (`n = 1,...,T-1`, zero at
`n = 0, T`). Multiplying each term of (3.9) by the common integer scale

    S_scale^(2) = 16 m D^3 Q_psi                                        (6.2)

produces three exact integers

    Delta_hat_0^(2) = (16 m D^3 Q_psi) delta_0^(psi) S_2 in Z,
    Delta_hat_1^(2) = (16 m D^3 Q_psi) delta_1^(psi) S_int in Z,
    Delta_hat_2^(2) = (16 m D^3 Q_psi) delta_2^(psi) S_0 in Z,          (6.3)

satisfying the exact integer cancellation

    Delta_hat_0^(2) + Delta_hat_1^(2) + Delta_hat_2^(2) = 0.            (6.4)

For integer `epsilon`, the second-order displaced state
`z + (delta_0^(psi) + epsilon delta_1^(psi) + epsilon^2 delta_2^(psi)) z` has
the common denominator

    D'' = 80 D^2 Q_psi.                                                 (6.5)

After rescaling the original numerators by `80 D Q_psi`, the integer increments
at interior `n = 1,...,T-1` and bond `b = 1,...,T` are:

    h:       40 D epsilon V_n * Q_h,n
             + 20 epsilon^2 Psi_hat_n * (Y_tilde_h,n+1 - Y_tilde_h,n-1),
    chi:     20 D epsilon (V_n(0) + V_n(1)) Q_chi,n
             + 5 epsilon^2 (Psi_hat_n(0) + Psi_hat_n(1))
               * (Y_tilde_chi,n+1 - Y_tilde_chi,n-1),
    alpha:   16 D^2 sum_r (V_b(r) - V_(b-1)(r)),
    lambda:  16 D^2 [5(V_b - V_(b-1)) - sum_r (V_b(r) - V_(b-1)(r)) e],
    N:       80 D^2 B V_n,
    tau, p:  0.                                                         (6.6)

## 7. Frozen finite fixtures, witnesses, negative controls, and certificate

### 7.1 Six off-shell configurations and parameter families

Use the exact six off-shell configurations (`T = 5, D = 60, a in {-1,0,1},
seed s in {0,1}`) and 21 parameter arrays `psi` (`20` unit vertex arrays plus
`f(n,r,7)/7`) from #1654 (`PREREG.md` Section 7.1):
- Compare all `133` independent global coordinate derivatives of
  `S_<=2(epsilon = 1)` across all 6 configurations (`798` checks).
- Check local continuity, auxiliary constraint propagation, and integer
  continuity at all `4 * 5 = 20` interior vertices per configuration (`120`
  checks each).
- For all `6 * 21 = 126` configuration/parameter pairs, check:
  - First-order Noether identity `delta_0 S_0 = 0` and
    `delta_0 S_int + delta_1 S_0 = 0` (`126` checks),
  - Second-order Noether identity
    `delta_0 S_2 + delta_1 S_int + delta_2 S_0 = 0` (`126` checks),
  - Integer second-order Noether identity (6.3)-(6.4) at scale
    `16 m D^3 Q_psi` (`126` checks).
- For all `126` pairs and `epsilon in {-1, 0, 1, 2}` (`504` checks each):
  - Check the four-point directional derivative (3.11) against the analytical /
    dual directional derivative and against `epsilon^3 W_3 + epsilon^4 W_4`
    (`DEFORMATION_CHECKS = 504`),
  - Check the exact pure-gauge field-redefinition identity (4.2) with zero
    defect (`PURE_GAUGE_REDEFINITION_CHECKS = 504`),
  - Check the common-denominator integer tangent encoding (6.5)-(6.6) and
    subspace preservation (`INTEGER_SECOND_ORDER_TANGENT_CHECKS = 504`).
- For each of the 6 configurations and all `190` unordered pairs of the 20 unit
  parameters (`EXTENDED_COMMUTATOR_CHECKS = 1140`), check that the
  order-`epsilon^2` extended commutator (5.3) vanishes identically across the
  entire time horizon and that the full composed commutator at `epsilon = 1`
  matches the closed formula `C_3 + C_4` in (5.4).

### 7.2 Exact witnesses and ten negative controls

1. `GLOBAL_NEIGHBOR_GRADIENT`: `T = 5, a = 0, E_hom = 0`, all fields zero except
   `h_1 = (6,11,11,6,6)/40` and `N_1 = delta_(e_0)`. Relative to `N = 0`, the
   global gradient of `S_<=2(1)` at slice 2 changes by
   `(29/10368, 29/10368, 0, 0, 0)` in `h_2` and `-17/51840` in `chi_2`, while a
   central-current-only functional at slice 2 gives zero.
2. `SECOND_ORDER_SPLIT` and `OMIT_S2_DEFECT`: On `T = 5, a = 0, E_hom = 0`,
   `h_3 = e_0`, `psi_2 = psi_3 = e_0`:
   - With `alpha_3 = 1` (other multipliers zero), `delta_0 S_2 = 0`,
     `delta_1 S_int = 115/324`, `delta_2 S_0 = -115/324`, summing to `0`.
   - With `alpha_2 = 1` and `alpha_3 = 1`, all three terms are nonzero:
     `delta_0 S_2 = 115/324`, `delta_1 S_int = 115/324`,
     `delta_2 S_0 = -115/162`, summing to `0`. Omitting `S_2` leaves the
     nonzero defect `-115/324`.
3. `OMIT_DELTA2_DEFECT` and `THIRD_FOURTH_REMAINDERS`: On `h_3 = e_0`,
   `alpha_3 = 1`, `psi_2 = psi_3 = e_0`, omitting `delta_2` leaves the
   second-order defect `115/324`. With `delta_2` included, the second-order
   variation vanishes while the third- and fourth-order remainders are
   `W_3 = 1/8` (`delta_1 S_2 = -1/8`, `delta_2 S_int = 1/4`),
   `W_4 = -115/1296`, and `W_3 + W_4 = 47/1296`.
4. `QUARTIC_CENTRAL_DEFECT`: On that same witness along `hat_delta_psi` at
   `epsilon = 1`, the naive unit central difference `[P(1) - P(-1)]/2` minus
   the exact four-point / dual derivative `47/1296` is `1/32`.
5. `PURE_GAUGE_S2_COMPLETION`: On `h_3 = e_0, psi_2 = psi_3 = e_0` with pure-gauge
   multipliers `M = Gamma(psi)` at `epsilon = 1`, `S_2[x, Gamma(psi)] = 115/648`,
   cancelling the `-115/648` remainder of `S_0 + S_int` so that
   `S_<=2(1)|_(M = Gamma(psi)) - A_auto(x - G_psi x) = 0`.
6. `OMIT_HOMOGENEOUS_LAPSE`: On `h_3 = e_0, alpha_3 = 1, psi_2 = psi_3 = e_0`,
   setting `delta_0 alpha = 0` leaves first-order defect `-1/10`.
7. `OMIT_INTERACTION_CURRENT`: On `h_2 = e_0, chi_3 = 1, psi_2 = e_0`, removing
   `j_int` from `S_int` leaves first-order defect `-1/1296`.
8. `DROP_COCLOSURE`: On `p_2 = delta_(e_0)` (outside `K_E`), `psi_2 = e_0`,
   `delta_0 S_0 = -2`.
9. `EXTENDED_COMMUTATOR_CANCELLATION` and `WRONG_DELTA2_ORDER`: On
   `psi_2 = ell, eta_3 = ell`, `h_n = e/5` (`n != 4`), `h_4 = e/5 + ell`, the
   bare commutator at slice 2 is `(-1/4, 1/4, 0, 0, 0)`, the cross-commutator
   is `(1/4, -1/4, 0, 0, 0)`, and their sum is `(0, 0, 0, 0, 0)`. Reversing the
   operator order in `delta_2` to `G_psi G_(Psi[M]) x` doubles the order-`epsilon^2`
   commutator defect to `(-1/2, 1/2, 0, 0, 0)`.
10. `THIRD_ORDER_COMMUTATOR_RESIDUAL` and `FIXED_MEAN_ESCAPE`: On that same
    state with `alpha_1 = 1, alpha_2 = -1` (`Psi_1[M] = e`), the third-order
    commutator residual at slice 1 is `C_3(psi, eta; x, M)_(h,1) = (-1/8, 1/8, 0, 0, 0)`,
    and `sum_r (G_eta h_3)(r) = 1`.

### 7.3 Certificate grammar and independent implementation contract

Each implementation emits this exact 25-line ASCII/LF certificate on success:

    CERTIFICATE=P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-2
    AUTHORITY_FILES=5
    GLOBAL_CONFIGURATIONS=6
    GLOBAL_VARIATIONS=798
    CONTINUITY_VERTICES=120
    CONSTRAINT_PROPAGATION_VERTICES=120
    INTEGER_CONTINUITY_VERTICES=120
    FIRST_ORDER_NOETHER=126
    SECOND_ORDER_NOETHER=126
    INTEGER_SECOND_ORDER_NOETHER=126
    DEFORMATION_CHECKS=504
    PURE_GAUGE_REDEFINITION_CHECKS=504
    INTEGER_SECOND_ORDER_TANGENT_CHECKS=504
    EXTENDED_COMMUTATOR_CHECKS=1140
    GLOBAL_S2_GRADIENT_SHA256=<computed lowercase SHA-256>
    SECOND_ORDER_PAYLOAD_SHA256=<computed lowercase SHA-256>
    GLOBAL_NEIGHBOR_GRADIENT=29/10368,29/10368,0,0,0;-17/51840
    SECOND_ORDER_SPLIT=115/324,115/324,-115/162
    THIRD_FOURTH_REMAINDERS=1/8,-115/1296,47/1296
    QUARTIC_CENTRAL_DEFECT=1/32
    PURE_GAUGE_S2_COMPLETION=115/648;0
    EXTENDED_COMMUTATOR_CANCELLATION=-1/4,1/4,0,0,0;1/4,-1/4,0,0,0;0,0,0,0,0
    THIRD_ORDER_COMMUTATOR_RESIDUAL=-1/8,1/8,0,0,0
    NEGATIVE_CONTROLS=10
    CERTIFICATE_RESULT=PASS

The gradient payload record is `a|s|i|value\n` (`i = 0,...,132`) for the
complete action `S_<=2(1)`. The second-order Noether payload record is
`a|s|p|d0S2|d1Sint|d2S0|W3|W4\n` (`p = 0,...,20`). Rationals are printed as
signed integers when denominator is 1, otherwise `num/den` in lowest terms.
`verify.py` (incidence arrays, form (3.7a), analytic polarized gradients,
four-point directional formula) launches `breaker.py` (nested state arrays,
form (3.7b), nilpotent `Dual` automatic differentiation, sparse 36x36 generator
matrices) in an isolated subprocess with `-I`, verifies exit code 0, empty
stderr, and byte-identical 25-line certificate stdout, and appends:

    BREAKER_RAW_BYTES=IDENTICAL
    RESULT=PASS

Registered falsifiers are `AUTHORITY`, `DOMAIN`, `INCIDENCE`, `GLOBAL_GRADIENT`,
`CONTINUITY`, `CONSTRAINT_PROPAGATION`, `INTEGER_CONTINUITY`, `AUXILIARY_GAUGE`,
`NOETHER`, `SECOND_ORDER_NOETHER`, `INTEGER_SECOND_ORDER_NOETHER`,
`DEFORMATION`, `FIELD_REDEFINITION`, `INTEGER_TANGENT`, `COMMUTATOR`,
`NEIGHBOR_WITNESS`, `REMAINDER_WITNESS`, `CENTRAL_WITNESS`, `CONTROL`,
`NONCLOSURE`, `CERTIFICATE`, `BREAKER_BYTES`.
