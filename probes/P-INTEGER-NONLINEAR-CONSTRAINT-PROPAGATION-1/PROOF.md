# Proofs for P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1

Scope: NON-CANONICAL, L1.  
Ownership: https://github.com/mathorn1973/twist-j/issues/1651.

This document proves the mathematical construction frozen in `PREREG.md`:
1. the exact incidence factorization `L = B_5^T W_e B_5` on the five-site
   planar ring and the closed-form circulant Green identity
   `L_int L_adj = L_adj L_int = 53605 Pi_0`;
2. the vertex/edge resolution `(e_tot,n, j_tot,n)` of the autonomous coupled
   TT-and-source system, its global sum `sum_r e_tot,n(r) = Htot_n`, and its
   exact off-shell pointwise continuity identity at every vertex `r in Z/5`;
3. the cubic constraint-coupled action `A_constr`, its seven field-sector
   variations, the closed-form 48-coordinate gradient of `A_cubic,loc`
   (including off-gauge cubic backreaction terms), and the exactness of
   central unit differences for all 48 coordinates;
4. the Discrete Hamiltonian Constraint `2 L tau_n = Pi_0 e_tot,n`, the
   Discrete Momentum Constraint `2(W_e B_5(tau_(n+1) - tau_n) + p_n) + j_tot,n = 0`,
   and the exact off-shell Discrete Bianchi / Constraint-Propagation Identity
   `B_5^T p_n = -(1/4) Pi_0 (q_h,n * R_h,n + q_chi,n R_chi,n sigma)`, proving
   on-shell co-closure `p_n in K_E = ker B_5^T` at every step;
5. the exact integer lift `(E_int, Theta, J_int, Pi_int)` of the constraint
   records on the entire unrestricted 21-coordinate integer carrier; and
6. the inherited all-counter Lorentz domain, symplectic invariance, 3-adic
   joint denominator growth `v_3(d_n) = 4(n-1)`, and symbolic derivations of
   all fixed witnesses and negative controls.

## 1. Planar incidence carrier and circulant Green operator

Let `X = Z/5 = {0, 1, 2, 3, 4}`, `e = (1, 1, 1, 1, 1)`, `ell = (1, -1, 0, 0, 0)`,
`sigma = (1/2, 1/2, 0, 0, 0)`, `m = 324`, and `g = 1/m`. Orient the ten edges
`E_5 = (e_0, ..., e_9)` by setting `e_r = (r, 1)` (tail `r`, head `(r+1) mod 5`,
weight `w_1 = 29/324`) and `e_(5+r) = (r, 2)` (tail `r`, head `(r+2) mod 5`,
weight `w_2 = 65/324`) for `r = 0, 1, 2, 3, 4`.

For `f in Q^5` and `j in Q^10`,

    (B_5 f)_e = f(head e) - f(tail e),
    (B_5^T j)(r) = sum_(head e = r) j(e) - sum_(tail e = r) j(e).

For any `f, g in Q^5`, summing over the ten edges gives

    <f, B_5^T W_e B_5 g>_V
      = sum_(e in E_5) w_e (B_5 f)_e (B_5 g)_e
      = sum_(r=0)^4 sum_(k in {1,2}) w_k (f(r+k) - f(r))(g(r+k) - g(r))
      = sum_(r=0)^4 f(r) [ 2(w_1 + w_2) g(r)
                           - w_1(g(r-1) + g(r+1))
                           - w_2(g(r-2) + g(r+2)) ].

Since `2(29 + 65) = 188`, this proves the exact matrix factorization

    L = B_5^T W_e B_5 = L_int / 324,
    (L_int g)_r = 188 g_r - 29(g_(r-1) + g_(r+1)) - 65(g_(r-2) + g_(r+2)).   (1.1)

Because the `k = 1` cycle is connected and `w_1, w_2 > 0`, `ker B_5 = ker L = span(e)`
has dimension 1, `im B_5^T = im L = e^perp` has dimension 4, and the co-closed
edge space `K_E = ker B_5^T` has dimension `10 - 4 = 6`.

### 1.1 Exact circulant Green operator on `e^perp`

Define the integer circulant operator

    (L_adj v)_r = 188 v_r - 65(v_(r-1) + v_(r+1)) - 29(v_(r-2) + v_(r+2)).   (1.2)

Clearly `L_adj e = (188 - 130 - 58) e = 0` and `L_int e = 0`. On `e^perp`,
`(S + S^-1) + (S^2 + S^-2) = -I_5`, where `S` is the cyclic shift. Substituting
`S^2 + S^-2 = -I_5 - (S + S^-1)` on `e^perp` gives

    L_int |_(e^perp) = 253 I + 36(S + S^-1),
    L_adj |_(e^perp) = 217 I - 36(S + S^-1).

Moreover, on `e^perp`, `(S + S^-1)^2 = S^2 + S^-2 + 2 I = I - (S + S^-1)`.
Multiplying the two commuting factors on `e^perp` yields

    L_int L_adj |_(e^perp)
      = (253 * 217) I + (253 * (-36) + 36 * 217)(S + S^-1) - 36^2 (I - (S + S^-1))
      = (54901 - 1296) I + 36(-36 + 36)(S + S^-1)
      = 53605 I.

Since both operators annihilate `e`, while `Pi_0 = I_5 - (1/5) e e^T` acts as
the identity on `e^perp` and zero on `e`, we obtain the exact $5 \times 5$
matrix identity on all of `Q^5`:

    L_int L_adj = L_adj L_int = 53605 Pi_0 = 10721 (5 I_5 - e e^T).          (1.3)

In particular, `(L|_(e^perp))^-1 Pi_0 = (324 / 53605) L_adj`. Applying (1.2)
to `ell = (1, -1, 0, 0, 0)` gives `L_adj ell = (253, -253, 36, 0, -36)`,
recovering `L^-1 ell = (324 / 53605)(253, -253, 36, 0, -36)` from #1650.

## 2. Local stress-energy-momentum tensor and off-shell continuity

Fix `a in {-1, 0, 1}` and `A_src = a/4`. For any sequence `(h_n, chi_n)` define

    R_h,n = (Delta_c^2 + L) h_n - g chi_n ell,
    R_chi,n = (Delta_c^2 + 1) chi_n - A_src - g <ell, h_n>.                  (2.1)

With the coupled equilibrium `(h_*, chi_*)` of `PREREG.md` Section 2 and
`z_n = (h_n - h_*, chi_n - chi_*)`, expanding the centered bond energy of #1650
using `K x_* = (0, 0, 0, 0, 0, A_src)` gives

    Htot_n = ||z_n - z_(n-1)||^2 / 2 + <z_(n-1), K z_n> / 2
           = ||h_n - h_(n-1)||^2 / 2 + <h_(n-1), L h_n> / 2
             + (chi_n - chi_(n-1))^2 / 2 + chi_(n-1) chi_n / 2
             - A_src (chi_(n-1) + chi_n) / 2
             - (g/2) [ chi_(n-1) <ell, h_n> + chi_n <ell, h_(n-1)> ]
             + E_*,                                                          (2.2)

where `E_* = (1/2) A_src chi_* = (4342005 / 8683757) A_src^2`.

Now resolve (2.2) onto the five vertices `r in Z/5` as in `PREREG.md` Section 3:

    e_loc,n(r) = e_h,n(r) + e_chi,loc,n(r) + e_int,n(r),
    e_tot,n(r) = e_loc,n(r) + E_* / 5.

Because each oriented edge `e in E_5` has one tail and one head,

    sum_(r=0)^4 e_h,n(r) = ||h_n - h_(n-1)||^2 / 2 + <h_(n-1), L h_n> / 2.

Since `sum_r sigma_r = 1` and `sum_r ell_r f(r) = <ell, f>`, summing `e_tot,n(r)`
over `r = 0, ..., 4` yields `sum_(r=0)^4 e_tot,n(r) = Htot_n` identically for
every `(h_(n-1), chi_(n-1), h_n, chi_n)`.

### 2.1 Proof of the exact off-shell pointwise continuity identity

Let `(h_(n-1), chi_(n-1))`, `(h_n, chi_n)`, `(h_(n+1), chi_(n+1))` be arbitrary
three-slice data, and put `q_h,n = h_(n+1) - h_(n-1)` and `q_chi,n = chi_(n+1) - chi_(n-1)`.

1. **TT sector (`e_h` and `j_h`).**
   At vertex `r`, the kinetic difference is

       (1/2)(h_(n+1)(r) - h_n(r))^2 - (1/2)(h_n(r) - h_(n-1)(r))^2
         = (1/2) q_h,n(r) (Delta_c^2 h_n)(r).

   On each oriented edge `e` with tail `u` and head `v`, let
   `D_n = (B_5 h_n)_e = h_n(v) - h_n(u)`. The change in the endpoint share of
   the spatial edge energy at `u` and `v` is

       Delta_share(e) = (w_e / 4) D_n [ (h_(n+1)(v) - h_(n-1)(v))
                                        - (h_(n+1)(u) - h_(n-1)(u)) ]
                      = (w_e / 4) D_n (q_h,n(v) - q_h,n(u)),

   while the edge current is `j_h,n(e) = (w_e / 4) D_n (q_h,n(u) + q_h,n(v))`.
   At the tail `u`, `B_5^T` subtracts `j_h,n(e)`, giving

       Delta_share(e) - j_h,n(e) = -(w_e / 2) q_h,n(u) D_n
                                 = (w_e / 2) q_h,n(u) (h_n(u) - h_n(v)).

   At the head `v`, `B_5^T` adds `j_h,n(e)`, giving

       Delta_share(e) + j_h,n(e) = +(w_e / 2) q_h,n(v) D_n
                                 = (w_e / 2) q_h,n(v) (h_n(v) - h_n(u)).

   Summing over the four edges incident to `r` produces `(1/2) q_h,n(r) (L h_n)(r)`.
   Hence for all off-shell field data,

       (e_h,n+1(r) - e_h,n(r)) + (B_5^T j_h,n)(r)
         = (1/2) q_h,n(r) [ (Delta_c^2 + L) h_n ](r)
         = (1/2) q_h,n(r) R_h,n(r) + (g / 2) chi_n ell_r q_h,n(r).          (2.3)

2. **Scalar source sector (`e_chi,loc`).**
   Direct expansion gives

       [ (chi_(n+1) - chi_n)^2 - (chi_n - chi_(n-1))^2 ] / 2
       + chi_n (chi_(n+1) - chi_(n-1)) / 2 - A_src (chi_(n+1) - chi_(n-1)) / 2
         = (1/2) q_chi,n [ (Delta_c^2 + 1) chi_n - A_src ]
         = (1/2) q_chi,n R_chi,n + (g / 2) q_chi,n <ell, h_n>.

   Multiplying by `sigma_r` yields

       e_chi,loc,n+1(r) - e_chi,loc,n(r)
         = (1/2) sigma_r q_chi,n R_chi,n + (g / 2) sigma_r q_chi,n <ell, h_n>. (2.4)

3. **Interaction sector (`e_int` and `j_int`).**
   Subtracting `e_int,n(r)` from `e_int,n+1(r)` cancels the `chi_n h_n(r)` cross
   terms and leaves

       e_int,n+1(r) - e_int,n(r)
         = -(g / 2) ell_r [ chi_n (h_(n+1)(r) - h_(n-1)(r))
                            + (chi_(n+1) - chi_(n-1)) h_n(r) ]
         = -(g / 2) chi_n ell_r q_h,n(r) - (g / 2) q_chi,n ell_r h_n(r).     (2.5)

4. **Dipole current cancellation.**
   Adding (2.3), (2.4), and (2.5) cancels `(g/2) chi_n ell_r q_h,n(r)` at
   every vertex `r`, leaving the dipole mismatch

       (g / 2) q_chi,n [ sigma_r <ell, h_n> - ell_r h_n(r) ].

   Evaluating the bracket at each site `r in {0, 1, 2, 3, 4}`:
   - at `r = 0`: `(1/2)(h_n(0) - h_n(1)) - h_n(0) = -(1/2)(h_n(0) + h_n(1))`;
   - at `r = 1`: `(1/2)(h_n(0) - h_n(1)) + h_n(1) = +(1/2)(h_n(0) + h_n(1))`;
   - at `r = 2, 3, 4`: `0`.

   Since `e_0 = (0, 1)` has tail `0` and head `1`, `(B_5^T delta_(e_0))(r) = -delta_(r,0) + delta_(r,1)`.
   Therefore, for `j_int,n(e) = -(g / 4) q_chi,n (h_n(0) + h_n(1)) delta_(e, e_0)`,

       (B_5^T j_int,n)(r) = -(g / 2) q_chi,n [ sigma_r <ell, h_n> - ell_r h_n(r) ].

   Adding `(B_5^T j_int,n)(r)` completes the proof of the exact off-shell
   pointwise continuity identity for all `r in Z/5`:

       (e_tot,n+1(r) - e_tot,n(r)) + (B_5^T j_tot,n)(r)
         = (e_loc,n+1(r) - e_loc,n(r)) + (B_5^T j_tot,n)(r)
         = (1/2) q_h,n(r) R_h,n(r) + (1/2) sigma_r q_chi,n R_chi,n.          (2.6)

## 3. Cubic constraint-coupled action and all field variations

Consider the cubic action `A_constr` of `PREREG.md` Section 4 and its local
two-bond restriction `A_cubic,loc` on `[n-1, n+1]` with fixed endpoint slices
`(h_(n-1), chi_(n-1))` and `(h_(n+1), chi_(n+1))`.

### 3.1 Closed-form 48-coordinate gradient of `A_cubic,loc`

Let `mu_b = ell_hom,b e + Pi_0 ell_lapse,b in Q^5` for `b in {n, n+1}`.
Because `Htot_b = <e, e_loc,b>_V + E_*` and `<ell_lapse,b, Pi_0 e_loc,b>_V = <Pi_0 ell_lapse,b, e_loc,b>_V`,
the lapse couplings on bond `b` combine into

    -ell_hom,b (Htot_b - E_hom) - <ell_lapse,b, Pi_0 e_loc,b>_V
      = -<mu_b, e_loc,b>_V + ell_hom,b (E_hom - E_*).

Differentiating `A_cubic,loc` with respect to each of its 48 coordinates gives:

1. **Interior TT field `v = h_n in Q^5` (5 coordinates):**
   For each bond `b in {n, n+1}` with neighbor slice `(h_nb, chi_nb)`
   (`(h_(n-1), chi_(n-1))` for `b = n` and `(h_(n+1), chi_(n+1))` for `b = n+1`),
    define the edge vector `U_b(e) = (w_e / 4)(mu_b(tail e) + mu_b(head e))(B_5 h_nb)_e`.
   Then

       d <mu_b, e_loc,b(v, xi)>_V / d v(r)
         = mu_b(r)(v(r) - h_nb(r)) + (B_5^T U_b)(r) - (g / 2) mu_b(r) ell_r chi_nb.

   For the shift-current coupling `<N_shift,n, j_tot,n(v)>_E`, define the edge
   vector `V_shift(e) = (w_e / 4) N_shift,n(e) (q_h,n(tail e) + q_h,n(head e))`.
   Since `j_int,n(v)(e_0) = -(g / 2) q_chi,n <sigma, v>_V`,

       d <N_shift,n, j_tot,n(v)>_E / d v(r)
         = (B_5^T V_shift)(r) - (g / 2) q_chi,n N_shift,n(e_0) sigma_r.

   Combining with `d A_local / d v = 2 v - h_(n-1) - h_(n+1) - L v + g xi ell`
   gives the exact 5-vector gradient `grad_v A_cubic,loc`.

2. **Interior scalar source `xi = chi_n in Q` (1 coordinate):**
   With `mu_sigma,b = <sigma, mu_b>_V = (mu_b(0) + mu_b(1)) / 2`,

       d <mu_b, e_loc,b(v, xi)>_V / d xi
         = mu_sigma,b (xi - chi_nb / 2 - A_src / 2)
           - (g / 2) sum_(s=0)^4 mu_b(s) ell_s h_nb(s).

   Since `j_tot,n(v)` does not depend on `xi`,

       d A_cubic,loc / d xi
         = (xi - chi_(n-1) - chi_(n+1) + A_src + g <ell, v>)
           - d <mu_n, e_loc,n>_V / d xi - d <mu_(n+1), e_loc,n+1>_V / d xi.

3. **Scalar constraint potentials `tau_n, tau_(n+1) in Q^5` (10 coordinates):**

       grad_(tau_n) A_cubic,loc = 2 L ell_lapse,n - 2 B_5^T W_e N_shift,n,
       grad_(tau_(n+1)) A_cubic,loc = 2 L ell_lapse,n+1 + 2 B_5^T W_e N_shift,n.

4. **Shift momentum `p_n in Q^10` (10 coordinates):**

       grad_(p_n) A_cubic,loc = 2 N_shift,n.

5. **Homogeneous lapse multipliers `ell_hom,n, ell_hom,n+1 in Q` (2 coordinates):**

       d A_cubic,loc / d ell_hom,b = -(Htot_b(v, xi) - E_hom),   b in {n, n+1}.

6. **Inhomogeneous lapse multipliers `ell_lapse,n, ell_lapse,n+1 in Q^5` (10 coordinates):**

       grad_(ell_lapse,b) A_cubic,loc = 2 L tau_b - Pi_0 e_loc,b(v, xi),   b in {n, n+1}.

7. **Edge shift multiplier `N_shift,n in Q^10` (10 coordinates):**

       grad_(N_shift,n) A_cubic,loc = 2 W_e B_5 (tau_(n+1) - tau_n) + 2 p_n + j_tot,n(v).

### 3.2 Exactness of central unit differences

When any single coordinate `x_i` among the 48 variables is varied while the
remaining 47 are fixed, `A_cubic,loc` is a polynomial in `x_i` of degree at
most 2 (degree 2 for `v(r)` and `xi`, and degree 1 for the 42 constraint and
multiplier coordinates). For every polynomial `P(t) = alpha t^2 + beta t + gamma`
of degree at most 2 over `Q`,

    (P(t + 1) - P(t - 1)) / 2 = 2 alpha t + beta = P'(t)

identically. Therefore, all 48 central unit differences equal the analytical
partial derivatives above without truncation error.

## 4. Discrete Hamiltonian and momentum constraints and Bianchi propagation

Setting `grad_(ell_lapse,n) A_cubic,loc = 0` with `tau_n in e^perp` gives the
Discrete Hamiltonian Constraint

    2 L tau_n = Pi_0 e_loc,n = Pi_0 e_tot,n.                                (4.1)

Applying `L_adj` to `2 L tau_n = (2 / 324) L_int tau_n = Pi_0 e_loc,n` and
using (1.3) together with `Pi_0 tau_n = tau_n` and `L_adj Pi_0 = L_adj` proves
that (4.1) has the unique solution in `e^perp`:

    tau_n = (162 / 53605) L_adj e_loc,n.                                    (4.2)

Setting `grad_(N_shift,n) A_cubic,loc = 0` gives the Discrete Momentum
Constraint

    p_n = -(1/2) j_tot,n - W_e B_5 (tau_(n+1) - tau_n).                     (4.3)

Now apply `B_5^T` to (4.3). Using `B_5^T W_e B_5 = L` and (4.1) on bonds `n`
and `n + 1`,

    B_5^T p_n = -(1/2) B_5^T j_tot,n - L (tau_(n+1) - tau_n)
              = -(1/2) [ B_5^T j_tot,n + Pi_0 (e_loc,n+1 - e_loc,n) ].

Because `<e, B_5^T j_tot,n>_V = <B_5 e, j_tot,n>_E = 0`, we have
`B_5^T j_tot,n = Pi_0 B_5^T j_tot,n`. Substituting the off-shell pointwise
continuity identity (2.6) yields the exact off-shell Discrete Bianchi Identity

    B_5^T p_n = -(1/2) Pi_0 [ (e_loc,n+1 - e_loc,n) + B_5^T j_tot,n ]
              = -(1/4) Pi_0 [ q_h,n * R_h,n + q_chi,n R_chi,n sigma ].      (4.4)

When the coupled dynamical equations `R_h,n = 0` and `R_chi,n = 0` hold, the
right-hand side of (4.4) vanishes identically at every vertex `r in Z/5`,
proving `B_5^T p_n = 0` (`p_n in K_E`).

## 5. Exact integer lift of the constraint sector on the unrestricted carrier

Let `x = (Z, R, D, H)` be any core in the unrestricted 21-coordinate carrier,
with `Z = (P, Y)`, `R = (Q, V)`, `D >= 1`, and rational decoding
`(h, chi) = (P, Y) / D`, `(h_prev, chi_prev) = (Q, V) / D`. Multiplying
`e_loc(x)(r)` by `4 m D^2 = 1296 D^2` gives

    E_int(x)(r) = 4 m D^2 e_loc(x)(r)
                = 2 m (P_r - Q_r)^2
                  + sum_(e incident to r) (m w_e) (B_5 P)_e (B_5 Q)_e
                  + (2 sigma_r) [ m (Y - V)^2 + m Y V - 81 a D (Y + V) ]
                  - 2 ell_r (V P_r + Y Q_r).                                 (5.1)

Since `m w_1 = 29`, `m w_2 = 65`, and `2 sigma_r in {0, 1}` are integers,
`E_int(x) in Z^5`. Multiplying (4.2) by `8 * 53605 D^2 = 428840 D^2` gives

    Theta(x) = (8 * 53605 D^2) tau(x)
             = (8 * 53605 D^2)(162 / 53605) L_adj (E_int(x) / (1296 D^2))
             = L_adj E_int(x) in Z^5.                                       (5.2)

By (1.3), `sum_r Theta(x)(r) = 0` and
`L_int Theta(x) = 10721 (5 E_int(x) - (sum_s E_int(x)(s)) e)` in `Z^5`.

For the bare forward image `x' = T(x) = (Z', R', D', H')`, `D' = m D`,
`R' = m Z`, and `Z' = B Z - m R + 81 a D e_6`. Thus `(h_prev, chi_prev)`,
`(h, chi)`, `(h_next, chi_next) = Z' / (m D)` form an exact on-shell
three-slice triple (`R_h = 0`, `R_chi = 0`) with
`Q_Delta(x) = Z' - m R = m D (q_h, q_chi) in Z^6`. Multiplying `j_tot(x)` by
`4 m^2 D^2` gives

    J_int(x)(e) = 4 m^2 D^2 j_tot(x)(e)
                = (m w_e) (B_5 P)_e [ Q_Delta,h(x)(tail e) + Q_Delta,h(x)(head e) ]
                  - Q_Delta,chi(x) (P_0 + P_1) delta_(e, e_0) in Z^10.       (5.3)

Since `e_loc(T(x)) = E_int(T(x)) / (4 m^3 D^2)` and `e_loc(x) = m^2 E_int(x) / (4 m^3 D^2)`,
multiplying the on-shell continuity equation `(e_loc(T(x)) - e_loc(x)) + B_5^T j_tot(x) = 0`
by `4 m^3 D^2` gives the exact integer continuity identity

    (E_int(T(x)) - m^2 E_int(x)) + m B_5^T J_int(x) = 0 in Z^5.             (5.4)

Finally, multiplying `p(x) = -(1/2) j_tot(x) - W_e B_5 (tau(T(x)) - tau(x))`
by `8 * 53605 m^3 D^2` gives

    Pi_int(x) = -53605 m J_int(x)
                - (m W_e) B_5 (Theta(T(x)) - m^2 Theta(x)) in Z^10,         (5.5)

and applying `B_5^T` using `B_5^T (m W_e) B_5 = L_int` and (5.2), (5.4) gives

    B_5^T Pi_int(x)
      = -53605 Pi_0 [ m B_5^T J_int(x) + E_int(T(x)) - m^2 E_int(x) ]
      = 0 in Z^5.                                                           (5.6)

All four integer constraint equations holds on every state of the
unrestricted 21-coordinate carrier without any mean or preparation condition.

## 6. Inherited dynamical, Lorentz, symplectic, and 3-adic precision theorems

The autonomous dynamical step, coupled stiffness bounds `(59/100) I < K < (201/200) I`
and `R_K = K - K^2 / 4 > I / 2` on `e^perp x R`, positive-definite Gram minors
of `K` (now augmented by the 4 positive leading principal minors of `L` on
`e^perp` in the basis `e_i - e_4`, `i = 0, 1, 2, 3`), conserved bond energy
`0 < Htot_n < 3/50`, energy-ellipsoid Lorentz signature bounds
`-1/4 < h_n(r) < 13/20`, `|chi_n| < 3/4`, `det g_n(r) < -231/400 < 0`,
discrete Legendre kick-drift map, centered symplectic invariance
`Omega_(n+1) = Omega_n`, 13-condition partial inverse, funded bijection
`F^-1 = Rev F Rev`, and joint 3-adic denominator valuation `v_3(d_n) = 4(n-1)`
are identical to `P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1` (#1650).

## 7. Symbolic derivation of the new exact witnesses and negative controls

Consider `word 0011` (`u_0 = u_1 = 1`) at `a = 0` (`A_src = 0`, `E_* = 0`).
At `n = 1`, `D_1 = 40`, `P_1 = Q_1 = (6, 11, 11, 6, 6)`, and `Y_1 = V_1 = 0`.

### 7.1 Initial vertex energy density `E_int,1`, `e_tot,1` and constraint `Theta_1`, `tau_1`

Since `P_1 = Q_1` and `Y_1 = V_1 = 0`, only the spatial edge sum in (5.1) is
nonzero. The ten edge differences `B_5 P_1` are:
- for `k = 1` (weight `m w_1 = 29`): `(+5, 0, -5, 0, 0)`, with weighted squares
  `(725, 0, 725, 0, 0)`;
- for `k = 2` (weight `m w_2 = 65`): `(+5, -5, -5, 0, +5)`, with weighted
  squares `(1625, 1625, 1625, 0, 1625)`.

Summing the four incident edges at each site `r in {0, 1, 2, 3, 4}` gives

    E_int,1 = (725 + 1625, 725 + 3250, 725 + 3250, 725 + 1625, 3250)
            = (2350, 3975, 3975, 2350, 3250).

Its sum is `15900`, and dividing by `4 m D_1^2 = 1296 * 1600 = 2073600` yields

    e_tot,1 = (47/41472, 53/27648, 53/27648, 47/41472, 65/41472),
    sum_(r=0)^4 e_tot,1(r) = 15900 / 2073600 = 53 / 6912 = Htot_1.

Subtracting the mean `15900 / 5 = 3180` gives
`Pi_0 E_int,1 = (-830, 795, 795, -830, 70)`. On `e^perp`,
`(L_adj w)_r = 217 w_r - 36(w_(r-1) + w_(r+1))`, which gives

    Theta_1 = L_adj E_int,1 = (-211250, 173775, 173775, -211250, 74950).

Dividing by `8 * 53605 * D_1^2 = 686144000` yields

    tau_1 = (-845/2744576, 6951/27445760, 6951/27445760, -845/2744576, 1499/13722880).

### 7.2 Dipole interaction current and Bianchi defect witnesses at `n = 1`

At `n = 2`, `D_2 = 12960`, `P_2 = (2414, 2769, 2769, 2414, 2594)`, and `Y_2 = -5`.
Hence `Q_Delta,1 = Z_2 - m R_1 = (470, -795, -795, 470, 650, -5)`. Since
`Q_Delta,chi,1 = -5` and `P_1(0) + P_1(1) = 6 + 11 = 17`, the integer dipole
interaction current on `e_0 = (0, 1)` is

    J_int_curr,1(e_0) = -(-5) * 17 = 85,
    j_int,1(e_0) = 85 / (4 * 324^2 * 40^2) = 85 / 671846400 = 17 / 134369280.

On bond 2, `chi_1 = 0` and `chi_2 = -1/2592`, so at `r = 0` (`h_1(0) = 6/40`)
and `r = 1` (`h_1(1) = 11/40`):

    e_chi,loc,2(0) + e_int,2(0) = 1 / 26873856 + (1 / 648)(6 / 40) / 2592 = +17 / 134369280,
    e_chi,loc,2(1) + e_int,2(1) = 1 / 26873856 - (1 / 648)(11 / 40) / 2592 = -17 / 134369280.

Their global sum vanishes, while their local dipole is balanced by
`B_5^T j_int,1 = (-17/134369280, +17/134369280, 0, 0, 0)`. Consequently:
- omitting `j_int,1` from `p_1` leaves the nonzero Bianchi defect

      B_5^T p_1^(no-int-current) = (1/2) B_5^T j_int,1
                                 = (-17/268738560, 17/268738560, 0, 0, 0);

- omitting `e_chi,loc + e_int` from `tau` leaves the opposite defect
  `(+17/268738560, -17/268738560, 0, 0, 0)`.

If the feedback sign is reversed at `n = 1`, `chi_2^(rev) = +1/2592`,
`q_chi,1^(rev) = +1/2592`, `R_h,1^(rev) = 0`, and `R_chi,1^(rev) = +1/1296`.
By the off-shell Bianchi formula (4.4) with `Pi_0 sigma = (3/10, 3/10, -1/5, -1/5, -1/5)`,

    B_5^T p_1^(rev-feedback)
      = -(1/4)(1/2592)(1/1296) Pi_0 sigma
      = (-1/44789760, -1/44789760, 1/67184640, 1/67184640, 1/67184640).

### 7.3 Off-gauge cubic shift-to-field backreaction witness

At `word 0011, a = 0, n = 1`, with `(h, chi, tau, p)` on-shell and only the
dipole-edge shift multiplier `N_shift,1 = delta_(e_0)` turned on, Section 3.1
gives

    grad_(h_1) A_cubic,loc |_(N_shift,1 = delta_(e_0))
      = d j_tot,1(h_1)(e_0) / d h_1.

Since `q_h,1(0) + q_h,1(1) = (470 - 795) / 12960 = -65 / 2592` and
`q_chi,1 = -1 / 2592`,

    (w_1 / 4)(q_h,1(0) + q_h,1(1)) = (29 / 1296)(-65 / 2592) = -1885 / 3359232,
    -(g / 4) q_chi,1 = -(1 / 1296)(-1 / 2592) = +1 / 3359232.

At site `0` (`tail(e_0)`), `(B_5 v)_(e_0) = v(1) - v(0)` contributes
`+1885 / 3359232` and `j_int,1` contributes `+1 / 3359232`, giving
`1886 / 3359232 = 943 / 1679616`. At site `1` (`head(e_0)`), they contribute
`-1885 / 3359232 + 1 / 3359232 = -1884 / 3359232 = -157 / 279936`. Sites
`2, 3, 4` have coefficient `0`. Thus

    grad_(h_1) A_cubic,loc |_(N_shift,1 = delta_(e_0))
      = (943/1679616, -157/279936, 0, 0, 0).
