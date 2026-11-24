# P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-2 — Analytic Proofs

Status: PROSPECTIVE  
Scope: NON-CANONICAL, NEW_DECLARED L1  
Owner: A. M. Thorn (`antigravity-windows-de9b3dcc-e611-4360-a2c9-df8dfe124fd3`)  
Ownership: https://github.com/mathorn1973/twist-j/issues/1655

This document proves the exact algebraic statements frozen in `PREREG.md`.
All identities hold over `Q` and `Z` for any finite horizon `T >= 5` and any
admitted off-shell rational field, auxiliary, and multiplier configuration.
The formal deformation parameter `epsilon` grades the coupling and generator
series; it does not assert an all-order closed gauge algebra at `epsilon = 1`.

## 1. Inherited finite-horizon carrier, operators, and first-order system

Let `T >= 5` be an integer time horizon. On the five-vertex graph `Z/5` with
ten oriented edges `e_r = (r, r+1)` (weight `29/324`) and `e_(5+r) = (r, r+2)`
(weight `65/324`), put `m = 324`, `g = 1/m`, `e = (1,1,1,1,1)`,
`ell = (1,-1,0,0,0)`, `sigma = (1/2,1/2,0,0,0)`, `a in {-1,0,1}`, and `A = a/4`.
With incidence matrix `B` and diagonal edge weight matrix `W`,

    L = B^T W B = L_int / 324,
    (L_int h)_r = 188 h_r - 29(h_(r-1) + h_(r+1)) - 65(h_(r-2) + h_(r+2)),
    Pi0 v = v - mean(v) e,
    L_int L_adj = 53605 Pi0,
    K_E = ker B^T.                                                      (1.1)

The physical trajectory is `x = (h_n, chi_n)_(n=0)^T in (Q^5 x Q)^(T+1)` with
fixed endpoints `x_0, x_T`. The auxiliary variables are `tau_b in e^perp`
(`b = 1,...,T`) and `p_n in K_E` (`n = 1,...,T-1`). The multipliers
`M = (alpha, lambda, N)` consist of `alpha_b in Q`, `lambda_b in e^perp`
(`b = 1,...,T`), and `N_n in Q^10` (`n = 1,...,T-1`), with combined bond lapse
vector `mu_b = alpha_b e + lambda_b in Q^5`.

The autonomous action `A_auto[x]` has interior Euler-Lagrange derivatives
`D_(h_n) A_auto = -R_h,n[x]` and `D_(chi_n) A_auto = -R_chi,n[x]`, where

    R_h,n[x]   = h_(n+1) - 2 h_n + h_(n-1) + L h_n - g chi_n ell,
    R_chi,n[x] = chi_(n+1) - chi_n + chi_(n-1) - A - g <ell, h_n>.      (1.2)

For any interior tangent field `u = (u_h, u_chi)` with `u_0 = u_T = 0`, the
constant quadratic Hessian form of `A_auto` is

    Hess_(A_auto)[u, v]
      = sum_(b=1)^T [ <u_h,b - u_h,b-1, v_h,b - v_h,b-1>
                      + (u_chi,b - u_chi,b-1)(v_chi,b - v_chi,b-1) ]
        - sum_(n=1)^(T-1) [ <u_h,n, L v_h,n> + u_chi,n v_chi,n
                            - g (u_chi,n <ell, v_h,n> + v_chi,n <ell, u_h,n>) ]
      = -sum_(n=1)^(T-1) [ <R_h,n^hom[u], v_h,n>
                           + R_chi,n^hom[u] v_chi,n ],                  (1.3)

where `R^hom` denotes `R` with the constant force `A` set to zero.

With local bond energy density `e_loc,b[x]`, equilibrium constant
`E_star = (4342005/8683757) A^2`, bond total energy
`H_b[x] = sum_r e_loc,b[x](r) + E_star`, and edge current `j_n[x]`, the local
energy continuity identity holds identically off-shell for `n = 1,...,T-1`:

    C_n[x] = e_loc,n+1[x] - e_loc,n[x] + B^T j_n[x]
           = (1/2) [ q_h,n * R_h,n[x] + sigma q_chi,n R_chi,n[x] ],     (1.4)

where `q_h,n = h_(n+1) - h_(n-1)` and `q_chi,n = chi_(n+1) - chi_(n-1)`. The
zeroth- and first-order action sectors are

    S_0[x, tau, p, M]
      = A_auto[x] + 2 sum_(b=1)^T <lambda_b, L tau_b>
        + 2 sum_(n=1)^(T-1) <N_n, W B(tau_(n+1) - tau_n) + p_n>,

    S_int[x, M]
      = -sum_(b=1)^T alpha_b (H_b[x] - E_hom)
        -sum_(b=1)^T <lambda_b, e_loc,b[x]>
        +sum_(n=1)^(T-1) <N_n, j_n[x]>.                                 (1.5)

For any vertex parameter array `psi = (psi_0,...,psi_T)` with `psi_0 = psi_T = 0`,
define the pure-gauge multiplier map `Gamma(psi)` and linear field operator
`G_psi` (with `(G_psi x)_0 = (G_psi x)_T = 0`) by

    Gamma(psi)_alpha,b  = mean(psi_b - psi_(b-1)),
    Gamma(psi)_lambda,b = Pi0(psi_b - psi_(b-1)),
    Gamma(psi)_N,n      = B psi_n,
    (G_psi h)_n         = (1/2) psi_n * q_h,n,
    (G_psi chi)_n       = (1/2) <sigma, psi_n> q_chi,n.                 (1.6)

With `delta_0^(psi) M = Gamma(psi)` (and `delta_0 x = delta_0 tau = delta_0 p = 0`)
and `delta_1^(psi) x = G_psi x` (zero on auxiliaries and multipliers), summation
by parts over `b = 1,...,T` using `psi_0 = psi_T = 0`, `tau_b in e^perp`,
`p_n in K_E`, and (1.4) yields the exact first-order identities

    delta_0^(psi) S_0 = 0,
    delta_0^(psi) S_int[x, M]
      = S_int[x, Gamma(psi)]
      = sum_(n=1)^(T-1) <psi_n, C_n[x]>
      = -D_x A_auto[x][G_psi x]
      = -delta_1^(psi) S_0.                                             (1.7)

## 2. Multiplier dressing map `Psi[M]` and `delta_0`-invariant residual `M_tilde[M]`

### Lemma 2.1 (Reproducing property and `delta_0`-invariant decomposition)

Define `Psi_0[M] = 0`, `Psi_T[M] = 0`, and for `n = 1,...,T-1`:

    Psi_n[M] := sum_(b=1)^n mu_b = sum_(b=1)^n (alpha_b e + lambda_b).  (2.1)

Then for every parameter array `psi` with `psi_0 = psi_T = 0`:

1. `delta_0^(psi) Psi_n[M] = psi_n` for all `n = 0,...,T`.
2. `Psi_n[Gamma(psi)] = psi_n` for all `n = 0,...,T`.
3. The residual multiplier array `M_tilde[M] := M - Gamma(Psi[M])` satisfies
   `delta_0^(psi) M_tilde[M] = 0` identically, and `M_tilde[Gamma(psi)] = 0`.

**Proof.** Under `delta_0^(psi) M = Gamma(psi)`, the combined bond lapse vector
transforms by

    delta_0^(psi) mu_b
      = mean(psi_b - psi_(b-1)) e + Pi0(psi_b - psi_(b-1))
      = psi_b - psi_(b-1).

Since `Psi_n[M]` is linear in `M`, for every `n = 1,...,T-1`,

    delta_0^(psi) Psi_n[M]
      = sum_(b=1)^n (psi_b - psi_(b-1))
      = psi_n - psi_0
      = psi_n,

while at `n = 0, T`, `delta_0^(psi) Psi_n[M] = 0 = psi_n`. Because `Psi[M]` is
linear in `M`, `Psi_n[Gamma(psi)] = delta_0^(psi) Psi_n[M] = psi_n`. Applying
`delta_0^(psi)` to `M_tilde[M] = M - Gamma(Psi[M])` gives

    delta_0^(psi) M_tilde[M]
      = Gamma(psi) - Gamma(delta_0^(psi) Psi[M])
      = Gamma(psi) - Gamma(psi) = 0,

and `M_tilde[Gamma(psi)] = Gamma(psi) - Gamma(Psi[Gamma(psi)]) = 0`. QED.

## 3. Equivalence of (3.7a)-(3.7b) and the exact second-order Noether identity

### Lemma 3.1 (Derivative of the pure-gauge interaction action)

For any fixed vertex parameter array `psi` with `psi_0 = psi_T = 0`, any field
trajectory `x`, and any interior field variation `y` with `y_0 = y_T = 0`,

    D_x S_int[x, Gamma(psi)][y]
      = -Hess_(A_auto)[G_psi x, y] - D_x A_auto[x][G_psi y].            (3.1)

**Proof.** By (1.7), `S_int[x, Gamma(psi)] = -D_x A_auto[x][G_psi x]` holds as an
exact polynomial identity in all coordinates of `x`. Because `A_auto[x]` is
quadratic-affine in `x` with constant second derivative `Hess_(A_auto)` on
interior variations `y` (`y_0 = y_T = 0`) and `x -> G_psi x` is linear with
`(G_psi y)_0 = (G_psi y)_T = 0`, differentiating `-D_x A_auto[x][G_psi x]` at `x`
in the direction `y` by the product rule yields (3.1). QED.

### Theorem 3.2 (Equivalence of forms (3.7a) and (3.7b) and exact second-order Noether cancellation)

Define the second-order action term `S_2[x, M]` by

    S_2[x, M]
      := -D_x S_int[x, M_tilde[M]][G_(Psi[M]) x]
         + (1/2) Hess_(A_auto)[G_(Psi[M]) x, G_(Psi[M]) x],             (3.2a)

and the second-order field generator by

    delta_2^(psi) x := G_(Psi[M]) G_psi x,
    delta_2^(psi) (tau, p, M) := 0.                                     (3.2b)

Then:

1. `S_2[x, M]` is algebraically identical to

       S_2[x, M]
         = -D_x S_int[x, M][G_(Psi[M]) x]
           - (1/2) Hess_(A_auto)[G_(Psi[M]) x, G_(Psi[M]) x]
           - D_x A_auto[x][G_(Psi[M]) G_(Psi[M]) x].                    (3.3)

2. On the unrestricted off-shell domain, for every `a in {-1,0,1}` and every
   `psi` with `psi_0 = psi_T = 0`,

       delta_0^(psi) S_2 + delta_1^(psi) S_int + delta_2^(psi) S_0 = 0. (3.4)

3. For `S_<=2(epsilon) = S_0 + epsilon S_int + epsilon^2 S_2` and
   `hat_delta_psi = delta_0^(psi) + epsilon delta_1^(psi) + epsilon^2 delta_2^(psi)`,

       hat_delta_psi S_<=2(epsilon) = epsilon^3 W_3(psi) + epsilon^4 W_4(psi),
       W_3(psi) = delta_1^(psi) S_2 + delta_2^(psi) S_int,
       W_4(psi) = delta_2^(psi) S_2.                                    (3.5)

**Proof.**

1. Since `S_int[x, M]` is affine-linear in `M` with `x`-independent constant part
   `sum_b alpha_b E_hom`, `M -> D_x S_int[x, M][y]` is strictly linear in `M`.
   Substituting `M_tilde[M] = M - Gamma(Psi[M])` into (3.2a) and applying
   Lemma 3.1 with `psi = Psi[M]` and `y = G_(Psi[M]) x` gives

       -D_x S_int[x, M - Gamma(Psi[M])][G_(Psi[M]) x]
       + (1/2) Hess_(A_auto)[G_(Psi[M]) x, G_(Psi[M]) x]
         = -D_x S_int[x, M][G_(Psi[M]) x]
           - Hess_(A_auto)[G_(Psi[M]) x, G_(Psi[M]) x]
           - D_x A_auto[x][G_(Psi[M]) G_(Psi[M]) x]
           + (1/2) Hess_(A_auto)[G_(Psi[M]) x, G_(Psi[M]) x],

   which simplifies immediately to (3.3).

2. Apply `delta_0^(psi)` to (3.2a). Since `delta_0^(psi) x = 0`,
   `delta_0^(psi) M_tilde[M] = 0` (Lemma 2.1), and
   `delta_0^(psi) (G_(Psi[M]) x) = G_(delta_0^(psi) Psi[M]) x = G_psi x`, the
   product rule and symmetry of `Hess_(A_auto)` give

       delta_0^(psi) S_2[x, M]
         = -D_x S_int[x, M_tilde[M]][G_psi x]
           + Hess_(A_auto)[G_(Psi[M]) x, G_psi x].                      (3.6)

   By definition, `delta_1^(psi) S_int[x, M] = D_x S_int[x, M][G_psi x]` and
   `delta_2^(psi) S_0 = D_x A_auto[x][G_(Psi[M]) G_psi x]`. Adding these three
   quantities and using `M - M_tilde[M] = Gamma(Psi[M])` gives

       delta_0^(psi) S_2 + delta_1^(psi) S_int + delta_2^(psi) S_0
         = D_x S_int[x, Gamma(Psi[M])][G_psi x]
           + Hess_(A_auto)[G_(Psi[M]) x, G_psi x]
           + D_x A_auto[x][G_(Psi[M]) G_psi x],

   which vanishes identically by Lemma 3.1 with `psi = Psi[M]` and `y = G_psi x`.

3. Expanding `(delta_0^(psi) + epsilon delta_1^(psi) + epsilon^2 delta_2^(psi))(S_0 + epsilon S_int + epsilon^2 S_2)`
   by powers of `epsilon` and applying `delta_0 S_0 = 0`,
   `delta_0 S_int + delta_1 S_0 = 0`, and (3.4) leaves only the `epsilon^3` and
   `epsilon^4` terms in (3.5). QED.

### Corollary 3.3 (Degree structure and exactness of four-point and coordinatewise differences)

1. In each of the `31 T - 22` independent global coordinates individually (holding
   the remaining coordinates fixed), `S_<=2(epsilon)` has polynomial degree at
   most `2`, so its unit centered difference `[S_<=2(z + d_i) - S_<=2(z - d_i)]/2`
   equals its exact partial derivative.
2. Along any joint line `z(t) = z + t hat_delta_psi z`, `P(t) = S_<=2(z(t); epsilon)`
   has polynomial degree at most `4` in `t`, so the four-point central difference

       [-P(2) + 8 P(1) - 8 P(-1) + P(-2)] / 12 = P'(0)                  (3.7)

   is exact with zero truncation error.

**Proof.** In `S_2[x, M]`, form (3.2a) is homogeneous quadratic in `M` (since
both `M_tilde[M]` and `Psi[M]` are linear in `M`) and quadratic-affine in `x`
(since `D_x S_int[x, M_tilde][G_Psi x]` has degree at most `2` in `x` and
`Hess_(A_auto)[G_Psi x, G_Psi x]` is homogeneous quadratic in `x`). Every single
coordinate basis vector `d_i` modifies only `x`, only `(tau, p)`, or only `M`,
so `t -> S_<=2(z + t d_i; epsilon)` has degree at most `2`. Along the joint
direction `hat_delta_psi z`, `x(t)` is affine in `t` while `M_tilde[M(t)] = M_tilde[M]`
is constant in `t` and `Psi[M(t)] = Psi[M] + t psi` is affine in `t`. Thus
`G_(Psi[M(t)]) x(t)` has degree at most `2` in `t`, so `P(t)` has degree at most
`4` in `t`. For any quartic `P(t) = sum_(k=0)^4 c_k t^k`, `P(t) - P(-t) = 2 c_1 t + 2 c_3 t^3`,
and `[-2(8 c_3) + 8(2 c_3)] / 12 = 0`, leaving `c_1 = P'(0)`. QED.

## 4. Exact pure-gauge field-redefinition completion

### Theorem 4.1 (Zero-defect pure-gauge Taylor identity)

At pure-gauge multipliers `M = Gamma(psi)` (for arbitrary `tau in e^perp` and
`p in K_E`),

    S_2[x, Gamma(psi)] = (1/2) Hess_(A_auto)[G_psi x, G_psi x],         (4.1)

and for all `epsilon`,

    S_<=2(epsilon)|_(M = Gamma(psi)) = A_auto(x - epsilon G_psi x).     (4.2)

**Proof.** By Lemma 2.1, `M_tilde[Gamma(psi)] = 0` and `Psi[Gamma(psi)] = psi`.
Substituting these into (3.2a) gives (4.1) immediately. At `M = Gamma(psi)`,
the auxiliary terms in `S_0` vanish and `S_int[x, Gamma(psi)] = -D_x A_auto[x][G_psi x]`.
Since `A_auto` is a quadratic-affine polynomial in `x`, its second-order Taylor
expansion at `x` in the interior direction `-epsilon G_psi x` is exact:

    A_auto(x - epsilon G_psi x)
      = A_auto(x) - epsilon D_x A_auto[x][G_psi x]
        + (epsilon^2 / 2) Hess_(A_auto)[G_psi x, G_psi x]
      = S_0|_(M=Gamma(psi)) + epsilon S_int|_(M=Gamma(psi))
        + epsilon^2 S_2|_(M=Gamma(psi)). QED.

## 5. Order-`epsilon^2` extended commutator closure and `O(epsilon^3)` residual

### Theorem 5.1 (Extended commutator cancellation at order `epsilon^2`)

For any fixed parameter arrays `psi, eta` with `psi_0 = psi_T = eta_0 = eta_T = 0`,
define the Lie bracket of the state-space vector fields `hat_delta_psi` and
`hat_delta_eta` by

    [hat_delta_psi, hat_delta_eta] z
      = D_z(hat_delta_eta z)[hat_delta_psi z]
        - D_z(hat_delta_psi z)[hat_delta_eta z].                        (5.1)

Then `[hat_delta_psi, hat_delta_eta]` vanishes identically on `(tau, p, M)`, and
on `x = (h, chi)` its expansion in `epsilon` has zero `epsilon^0`, `epsilon^1`,
and `epsilon^2` coefficients:

    [hat_delta_psi, hat_delta_eta]_<=2 x = 0,                           (5.2)

while the complete commutator is

    [hat_delta_psi, hat_delta_eta] x
      = epsilon^3 C_3(psi, eta; x, M) + epsilon^4 C_4(psi, eta; x, M),
    C_3(psi, eta; x, M)
      = [G_eta G_(Psi[M]) G_psi - G_psi G_(Psi[M]) G_eta
         + G_(Psi[M])(G_eta G_psi - G_psi G_eta)] x,
    C_4(psi, eta; x, M)
      = G_(Psi[M]) [G_eta G_(Psi[M]) G_psi - G_psi G_(Psi[M]) G_eta] x. (5.3)

**Proof.** Because `hat_delta_psi (tau, p, M) = (0, 0, Gamma(psi))` is constant
on state space, the `(tau, p, M)` components of (5.1) vanish. On the physical
fields `x`,

    hat_delta_eta x = epsilon G_eta x + epsilon^2 G_(Psi[M]) G_eta x.

Differentiating `hat_delta_eta x` along `hat_delta_psi z` (where
`hat_delta_psi M = Gamma(psi)` implies `hat_delta_psi Psi[M] = psi` by Lemma 2.1,
and `hat_delta_psi x = epsilon G_psi x + epsilon^2 G_(Psi[M]) G_psi x`) gives

    D_z(hat_delta_eta x)[hat_delta_psi z]
      = epsilon G_eta (epsilon G_psi x + epsilon^2 G_(Psi[M]) G_psi x)
        + epsilon^2 G_psi G_eta x
        + epsilon^2 G_(Psi[M]) G_eta (epsilon G_psi x + epsilon^2 G_(Psi[M]) G_psi x)
      = epsilon^2 (G_eta G_psi + G_psi G_eta) x
        + epsilon^3 (G_eta G_(Psi[M]) G_psi + G_(Psi[M]) G_eta G_psi) x
        + epsilon^4 G_(Psi[M]) G_eta G_(Psi[M]) G_psi x.                (5.4)

The `epsilon^2` term `epsilon^2 (G_eta G_psi + G_psi G_eta) x` is symmetric under
`psi <-> eta` because the cross-variation `delta_0^(psi) (G_(Psi[M]) G_eta x) = G_psi G_eta x`
supplies the transpose product to `delta_1^(psi) (G_eta x) = G_eta G_psi x`.
Antisymmetrizing (5.4) in `(psi, eta)` therefore cancels the `epsilon^2` term
identically and leaves (5.3). QED.

## 6. Common-denominator integer lifts

Let all state sectors have integer numerators `(P_n, Y_n, T_b, K_n, A_b, Lambda_b, Ncal_n)`
over `D >= 1`, and let `psi_n = V_n / Q_psi` (`Q_psi >= 1`). Put
`M_b = A_b e + Lambda_b in Z^5` and `Psi_hat_n = sum_(b=1)^n M_b in Z^5`
(`n = 1,...,T-1`, `Psi_hat_0 = Psi_hat_T = 0`), so `Psi_n[M] = Psi_hat_n / D`.
Let `Q_h,n = P_(n+1) - P_(n-1)`, `Q_chi,n = Y_(n+1) - Y_(n-1)`,
`Y_tilde_h,n = V_n * Q_h,n in Z^5`, and `Y_tilde_chi,n = (V_n(0) + V_n(1)) Q_chi,n in Z`.
Then:

1. `(G_psi h)_n = Y_tilde_h,n / (2 D Q_psi)` and
   `(G_psi chi)_n = Y_tilde_chi,n / (4 D Q_psi)`.
2. `(delta_2^(psi) h)_n = Psi_hat_n * (Y_tilde_h,n+1 - Y_tilde_h,n-1) / (4 D^2 Q_psi)`
   and `(delta_2^(psi) chi)_n = (Psi_hat_n(0) + Psi_hat_n(1))(Y_tilde_chi,n+1 - Y_tilde_chi,n-1) / (16 D^2 Q_psi)`.
3. Because `(m D) R_h,n[x] in Z^5` and `(m D) R_chi,n[x] in Z` (using `A = a/4`
   and `81 a = 324 A`), multiplying `delta_2^(psi) S_0`, `delta_1^(psi) S_int`,
   and `delta_0^(psi) S_2` by `S_scale^(2) = 16 m D^3 Q_psi` clears all
   denominators (`4 D^2 Q_psi * m D` and `16 D^2 Q_psi * m D`) and produces three
   exact integers `Delta_hat_0^(2), Delta_hat_1^(2), Delta_hat_2^(2) in Z`
   satisfying `Delta_hat_0^(2) + Delta_hat_1^(2) + Delta_hat_2^(2) = 0`.
4. Combining `z` (denominator `D`), `delta_0^(psi) M` (denominator `5 Q_psi`),
   `delta_1^(psi) x` (denominators `2 D Q_psi` and `4 D Q_psi`), and
   `delta_2^(psi) x` (denominators `4 D^2 Q_psi` and `16 D^2 Q_psi`) over
   `D'' = lcm(D, 5 Q_psi, 16 D^2 Q_psi) | 80 D^2 Q_psi` yields the exact integer
   increment formulas (6.6) of `PREREG.md`.

## 7. Symbolic derivation of exact witnesses and ten negative controls

Fix `T = 5, a = 0, E_hom = 0`, `u = (1,0,0,0,0)`, and edge unit `delta_(e_0)`.

1. **`GLOBAL_NEIGHBOR_GRADIENT`:** With `h_1 = (6,11,11,6,6)/40` and `N_1 = delta_(e_0)`,
   `(B h_1)_(e_0) = 5/40 = 1/8` and `h_1(0) + h_1(1) = 17/40`. Since `j_1` depends
   on `q_2 - q_0` through slice `2`, the derivative of `<N_1, j_1>` with respect
   to `(h_2(0), h_2(1), chi_2)` equals
   `(w_0/4)(1/8) = 29/10368` on `h_2(0), h_2(1)` and
   `-(g/4)(17/40) = -17/51840` on `chi_2`. Because `S_2` vanishes whenever
   `alpha = 0` and `lambda = 0` (`Psi[M] = 0` and `G_(Psi[M]) x = 0`), the full
   `S_<=2(1)` gradient shift is identical to `(29/10368, 29/10368, 0, 0, 0; -17/51840)`.

2. **`SECOND_ORDER_SPLIT` and `OMIT_S2_DEFECT`:** Set `h_3 = u` and
   `psi_2 = psi_3 = u`. Then `y = G_psi x` is nonzero only at `n = 2`, where
   `y_h,2 = u/2`. On bond `3`, `D_x H_3[x][y] = <-u + (1/2) L u, u/2> = -1/2 + 47/324 = -115/324`,
   while on bond `2`, `h_1 = h_2 = 0` implies `D_x H_2[x][y] = 0`.
   - When only `alpha_3 = 1` is nonzero, `Psi_3[M] = Psi_4[M] = e`, so
     `(G_(Psi[M]) h)_4 = -u/2` (zero elsewhere) and `(delta_2^(psi) h)_3 = -u/4`
     (zero elsewhere). Pairing with `-R_h,3[x] = (2 - L) u` gives
     `delta_2^(psi) S_0 = -115/324`, while `delta_1^(psi) S_int = 115/324` and
     `delta_0^(psi) S_2 = 0`.
   - When `alpha_2 = alpha_3 = 1`, `D_x H_2[x][y] = 0` leaves
     `delta_1^(psi) S_int = 115/324`, while `Psi_3[M] = 2 e` doubles
     `(delta_2^(psi) h)_3 = -u/2` and thus `delta_2^(psi) S_0 = -115/162`. By
     (3.6), `delta_0^(psi) S_2 = 115/324`, so the three terms are
     `(115/324, 115/324, -115/162)` with sum `0`. Omitting `S_2` leaves the
     nonzero defect `-115/324`.

3. **`OMIT_DELTA2_DEFECT` and `THIRD_FOURTH_REMAINDERS`:** On `h_3 = u, alpha_3 = 1, psi_2 = psi_3 = u`:
   - Omitting `delta_2` leaves `delta_0 S_2 + delta_1 S_int = 115/324`.
   - With `delta_2` included, `(delta_2 h)_3 = -u/4` and `D_(h_3)(-H_3[x]) = -u`,
     so `delta_2^(psi) S_int = <-u, -u/4> = 1/4`. In `S_2[x, M]` (form (3.2a)),
     `M_tilde[M]` has only `alpha_tilde_5 = 1`, and since `x, y, z = delta_2 x`
     all vanish on slices `4, 5`, the `M_tilde` term and its derivatives along
     `y` and `z` vanish identically. Since `(G_Psi x)_4 = -u/2`,
     `(G_Psi y)_3 = -u/4`, and `(G_Psi z)_4 = u/8 = -(1/4)(G_Psi x)_4`,

         delta_1^(psi) S_2 = Hess_(A_auto)[G_Psi x, G_Psi y] = <-u/2, u/4> = -1/8,
         W_3 = delta_1^(psi) S_2 + delta_2^(psi) S_int = -1/8 + 1/4 = 1/8,
         W_4 = delta_2^(psi) S_2 = Hess_(A_auto)[G_Psi x, G_Psi z]
             = -(1/4) Hess_(A_auto)[G_Psi x, G_Psi x]
             = -(1/4)(115/324) = -115/1296,
         W_3 + W_4 = 1/8 - 115/1296 = 47/1296.

4. **`QUARTIC_CENTRAL_DEFECT`:** On the line `z(t) = z + t hat_delta_psi z` at
   `epsilon = 1` for the witness in item 3, let `v = y + z` (`v_h,2 = u/2, v_h,3 = -u/4`).
   Then `[P(1) - P(-1)]/2 - P'(0) = c_3`, where `c_3` is the `t^3` coefficient of
   `P(t)`. The `t^3` coefficient of `t S_int[x + t v, Gamma(psi)]` is
   `-Hess_(A_auto)[v, G_psi v] = -3/32`, and the `t^3` coefficient of `S_2(z(t))`
   is `Hess_(A_auto)[G_Psi v + G_psi x, G_psi v] = 4/32 = 1/8`, so
   `c_3 = -3/32 + 4/32 = 1/32`.

5. **`PURE_GAUGE_S2_COMPLETION`:** On `h_3 = u, psi_2 = psi_3 = u` with
   `M = Gamma(psi)`, `S_2[x, Gamma(psi)] = (1/2) Hess_(A_auto)[y, y] = 115/648`,
   cancelling `(S_0 + S_int)|_(M=Gamma(psi)) - A_auto(x - y) = -115/648` to `0`.

6. **`OMIT_HOMOGENEOUS_LAPSE`:** Setting `delta_0 alpha = 0` on item 3 removes
   `-(1/5) H_2 - (-1/5) H_4 = 1/10`, leaving first-order defect `-1/10`.

7. **`OMIT_INTERACTION_CURRENT`:** On `h_2 = u, chi_3 = 1, psi_2 = u`, removing
   `j_int` omits `-(B psi_2)_(e_0) j_int,2(e_0) = -1/1296`.

8. **`DROP_COCLOSURE`:** On `p_2 = delta_(e_0)` (outside `K_E`) and `psi_2 = u`,
   `delta_0 S_0 = 2 <B psi_2, p_2> = -2`.

9. **`EXTENDED_COMMUTATOR_CANCELLATION` and `WRONG_DELTA2_ORDER`:** On
   `psi_2 = ell, eta_3 = ell`, `h_n = e/5` (`n != 4`), `h_4 = e/5 + ell`,
   `(G_eta h)_3 = (1/2) ell * ell = (1/2, 1/2, 0, 0, 0)`, so at slice `2`:
   - Bare commutator: `([delta_1^(psi), delta_1^(eta)] h)_2 = (G_eta G_psi h - G_psi G_eta h)_2 = -(1/4) ell * (1,1,0,0,0) = (-1/4, 1/4, 0, 0, 0)`.
   - Cross-commutator: `((delta_0^(psi) delta_2^(eta) - delta_0^(eta) delta_2^(psi)) h)_2 = (G_psi G_eta h - G_eta G_psi h)_2 = (1/4, -1/4, 0, 0, 0)`.
   - Sum at order `epsilon^2`: `(0, 0, 0, 0, 0)`.
   - Reversing the operator order in `delta_2` to `G_psi G_(Psi[M]) x` gives
     cross-commutator `(G_eta G_psi - G_psi G_eta) x`, doubling the `epsilon^2`
     commutator defect at slice `2` to `(-1/2, 1/2, 0, 0, 0)`.

10. **`THIRD_ORDER_COMMUTATOR_RESIDUAL` and `FIXED_MEAN_ESCAPE`:** On the state
    of item 9 with `alpha_1 = 1, alpha_2 = -1` (so `Psi_1[M] = e` and
    `Psi_n[M] = 0` for `n >= 2`), `(G_psi G_eta h)_2 = (1/4, -1/4, 0, 0, 0)` and
    `(G_eta G_psi h)_2 = 0`. In (5.3), at slice `1`, only the term
    `-G_(Psi[M]) G_psi G_eta h` is nonzero:

        C_3(psi, eta; x, M)_(h,1)
          = -(1/2) Psi_1[M] * ( (G_psi G_eta h)_2 - (G_psi G_eta h)_0 )
          = -(1/2) e * (1/4, -1/4, 0, 0, 0)
          = (-1/8, 1/8, 0, 0, 0),

    while `sum_r (G_eta h)_3(r) = 1/2 + 1/2 = 1 != 0`.
