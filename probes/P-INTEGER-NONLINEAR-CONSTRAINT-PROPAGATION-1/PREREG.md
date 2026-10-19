# P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1

Status: PROSPECTIVE  
Scope: NON-CANONICAL, L1  
Owner: A. M. Thorn, session antigravity-windows-de9b3dcc-e611-4360-a2c9-df8dfe124fd3  
Ownership: https://github.com/mathorn1973/twist-j/issues/1651

## 1. Question, authority, action layer and custody

Can the autonomous positive-kinetic coupled metric-and-source system of
`P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1` (#1650) be extended by the first
nonlinear (cubic) gravitational constraint-coupling action terms on the
five-site planar incidence carrier so that:
1. the local vertex energy density and edge momentum current of the coupled
   TT-and-source system satisfy an exact off-shell pointwise continuity
   identity at every vertex, summing globally to the conserved positive bond
   energy `Htot_n`;
2. independent variations of all seven field sectors (`h_n`, `chi_n`,
   `tau_n`, `p_n`, `ell_hom,n`, `ell_lapse,n`, `N_shift,n`) yield the coupled
   dynamical equations together with the discrete Hamiltonian and momentum
   constraints;
3. the Hamiltonian constraint is propagated exactly from bond to bond by the
   coupled equations of motion so that the momentum record `p_n` lies
   identically in the co-closed edge space `K_E = ker B_5^T` (discrete
   Bianchi identity) without projection; and
4. both the dynamical slices and the quadratic constraint records lift to
   exact integer vectors on the unrestricted autonomous integer carrier?

The action layer is NEW_DECLARED L1. Every added localization weight, dipole
interaction current, cubic action coupling, circulant Green operator, and
integer constraint scaling is explicit model data. No claim of full
non-perturbative 4D Einstein equations, 125-site 3D spatial source coupling,
native-U derivation, physical SI clock calibration, or continuum manifold
limit is made.

Public Canon v103 is active at `main` and peeled `canon-v103` commit
`dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`, content commit
`01fb76f6b3b14a6a5ec05d0017ea922390ab6f66`. `SOURCE.md` records the five
normative hashes and byte sizes checked by both programs (`canon/CANON.md`
is 1052518 bytes, SHA-256
`d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b`).

Before any scientific execution or import of `verify.py` or `breaker.py`,
freeze `PREREG.md`, `PROOF.md`, `SOURCE.md`, `verify.py`, `breaker.py`, and
`FROZEN.sha256`; push the immutable pin, read all six files back from
GitHub, and post the prospective pin receipt on issue #1651.

## 2. Planar incidence carrier, circulant Green operator, and autonomous law

Let `X = Z/5 = {0, 1, 2, 3, 4}`, `m = 324`, `g = 1/m`, `ell = (1, -1, 0, 0, 0)`,
`e = (1, 1, 1, 1, 1)`, and `sigma = (1/2, 1/2, 0, 0, 0)`. Fix the ten
oriented edges `E_5 = (e_0, ..., e_9)` in canonical order:
- for `r in {0, 1, 2, 3, 4}`, `e_r = (r, 1)` has `tail(e_r) = r`,
  `head(e_r) = (r + 1) mod 5`, weight `w_(e_r) = w_1 = 29/324`, and integer
  weight `m w_(e_r) = 29`;
- for `r in {0, 1, 2, 3, 4}`, `e_(5+r) = (r, 2)` has `tail(e_(5+r)) = r`,
  `head(e_(5+r)) = (r + 2) mod 5`, weight `w_(e_(5+r)) = w_2 = 65/324`, and
  integer weight `m w_(e_(5+r)) = 65`.

Note that `e_0 = (0, 1)` is the dipole edge from site `0` to site `1`. The
incidence difference operator `B_5 : Q^5 -> Q^10` and its unweighted adjoint
`B_5^T : Q^10 -> Q^5` are

    (B_5 f)_e = f(head e) - f(tail e),
    (B_5^T j)(r) = sum_(head e = r) j(e) - sum_(tail e = r) j(e).

With `W_e = diag(w_(e_0), ..., w_(e_9))` and integer operators

    (C P)_r = 460 P_r + 29(P_(r-1) + P_(r+1)) + 65(P_(r-2) + P_(r+2)),
    L_int = 648 I - C,
    (L_int P)_r = 188 P_r - 29(P_(r-1) + P_(r+1)) - 65(P_(r-2) + P_(r+2)),
    (L_adj P)_r = 188 P_r - 65(P_(r-1) + P_(r+1)) - 29(P_(r-2) + P_(r+2)),

the canonical spatial operator `L = L_int / 324` satisfies the exact matrix
factorization and circulant Green identities

    L = B_5^T W_e B_5,
    L_int L_adj = L_adj L_int = 53605 Pi_0 = 10721 (5 I_5 - e e^T),
    L_int e = L_adj e = 0,

where `Pi_0 v = v - (<e, v>/5) e` is orthogonal projection onto the
four-dimensional mean-zero vertex space `e^perp = {v in Q^5 : sum_r v(r) = 0}`.
Thus `(L|_(e^perp))^-1 Pi_0 = (324/53605) L_adj` exactly. The co-closed edge
space is `K_E = ker B_5^T = {p in Q^10 : B_5^T p = 0}`, which has dimension
`10 - 4 = 6`.

For fixed context `a in {-1, 0, 1}` with `A_src = a/4`, the dynamical
variables `h_n in Q^5` and `chi_n in Q` have residuals

    R_h,n = h_(n+1) - 2 h_n + h_(n-1) + L h_n - g chi_n ell,
    R_chi,n = chi_(n+1) - chi_n + chi_(n-1) - A_src - g <ell, h_n>,

and obey the autonomous joint law `R_h,n = 0`, `R_chi,n = 0` for `n >= 1`.
On the fixed-mean space `sum_r h(r) = 1`, the coupled stiffness matrix
`K = [[L, -g ell], [-g ell^T, 1]]` and coupled equilibrium `x_* = (h_* - e/5, chi_*)`
are unchanged from #1650:

    L^-1 ell = (324/53605)(253, -253, 36, 0, -36),
    c = <ell, L^-1 ell> = 163944/53605,
    delta = g^2 c = 253/8684010,
    q = 8683757,
    chi_* = A_src * 8684010 / q,
    h_* = e/5 + A_src * (40986, -40986, 5832, 0, -5832) / q,
    E_* = (1/2) A_src chi_* = (4342005/8683757) A_src^2.

## 3. Local stress-energy density, edge current, and off-shell continuity

For any bond `n >= 1` connecting slice `(h_(n-1), chi_(n-1))` and slice
`(h_n, chi_n)`, define at each vertex `r in Z/5`:

    e_h,n(r) = (h_n(r) - h_(n-1)(r))^2 / 2
               + (1/4) sum_(e incident to r) w_e (B_5 h_n)_e (B_5 h_(n-1))_e,
    e_chi,loc,n(r) = sigma_r [ (chi_n - chi_(n-1))^2 / 2 + chi_(n-1) chi_n / 2
                               - A_src (chi_(n-1) + chi_n) / 2 ],
    e_int,n(r) = -(g/2) ell_r [ chi_(n-1) h_n(r) + chi_n h_(n-1)(r) ],
    e_loc,n(r) = e_h,n(r) + e_chi,loc,n(r) + e_int,n(r),
    e_tot,n(r) = e_loc,n(r) + E_* / 5.

Here "e incident to r" means the four edges in `E_5` with `tail(e) = r` or
`head(e) = r`, namely `(r, 1)`, `((r-1) mod 5, 1)`, `(r, 2)`, and
`((r-2) mod 5, 2)`. Summing over `r in Z/5` gives the exact identity

    sum_(r=0)^4 e_tot,n(r) = sum_(r=0)^4 e_loc,n(r) + E_* = Htot_n,

where `Htot_n = ||z_n - z_(n-1)||^2 / 2 + <z_(n-1), K z_n> / 2` for
`z_n = (h_n - h_*, chi_n - chi_*)` is the conserved positive-definite bond
energy of #1650. Because `E_* / 5` is spatially constant and independent of
`n`, `Pi_0 e_tot,n = Pi_0 e_loc,n` and `e_tot,n+1 - e_tot,n = e_loc,n+1 - e_loc,n`.

For any three consecutive slices `(h_(n-1), chi_(n-1))`, `(h_n, chi_n)`,
`(h_(n+1), chi_(n+1))` centered at slice `n >= 1`, put
`q_h,n = h_(n+1) - h_(n-1)` and `q_chi,n = chi_(n+1) - chi_(n-1)`, and define
on each oriented edge `e in E_5`:

    j_h,n(e) = (w_e / 4) (B_5 h_n)_e [ q_h,n(tail e) + q_h,n(head e) ],
    j_int,n(e) = -(g / 4) q_chi,n (h_n(0) + h_n(1)) delta_(e, e_0),
    j_tot,n(e) = j_h,n(e) + j_int,n(e).

`PROOF.md` proves that for arbitrary off-shell three-slice data, at every
vertex `r in Z/5`:

    (e_tot,n+1(r) - e_tot,n(r)) + (B_5^T j_tot,n)(r)
      = (e_loc,n+1(r) - e_loc,n(r)) + (B_5^T j_tot,n)(r)
      = (1/2) q_h,n(r) R_h,n(r) + (1/2) sigma_r q_chi,n R_chi,n.

On-shell (`R_h,n = 0` and `R_chi,n = 0`), the local continuity equation

    (e_tot,n+1 - e_tot,n) + B_5^T j_tot,n = 0

holds pointwise at every vertex `r in Z/5` and every step `n >= 1`.

## 4. Cubic constraint-coupled action, Hamiltonian/momentum constraints, and Bianchi identity

On a finite horizon `[0, T_max]` (`T_max >= 2`), introduce on each bond
`n in {1, ..., T_max}` the scalar constraint potential `tau_n in e^perp`,
the homogeneous lapse perturbation `ell_hom,n in Q`, and the inhomogeneous
lapse multiplier `ell_lapse,n in e^perp`, and on each interior slice
`n in {1, ..., T_max - 1}` the co-closed momentum `p_n in K_E = ker B_5^T`
and the edge shift multiplier `N_shift,n in Q^10`. With total edge momentum

    P_mom,n = W_e B_5 (tau_(n+1) - tau_n) + p_n,

the cubic constraint-coupled action is

    A_constr = A_auto
      + sum_(n=1)^(T_max) [ -ell_hom,n (Htot_n - E_hom)
                            + 2 <ell_lapse,n, L tau_n>_V
                            - <ell_lapse,n, e_tot,n>_V ]
      + sum_(n=1)^(T_max-1) [ 2 <N_shift,n, P_mom,n>_E
                              + <N_shift,n, j_tot,n>_E ].

Varying before any on-shell or gauge substitution gives:
1. **Inhomogeneous lapse (`ell_lapse,n in e^perp`) — Discrete Hamiltonian Constraint:**

       2 L tau_n - Pi_0 e_tot,n = 2 L tau_n - Pi_0 e_loc,n = 0,   tau_n in e^perp,

   whose unique solution on `e^perp` is given in closed circulant form by

       tau_n = (162 / 53605) L_adj e_loc,n.

2. **Homogeneous lapse (`ell_hom,n in Q`) — Homogeneous Energy Constraint:**

       Htot_n - E_hom = 0,

   satisfied at every bond `n >= 1` with `E_hom = Htot_1`.
3. **Edge shift (`N_shift,n in Q^10`) — Discrete Momentum Constraint:**

       2 P_mom,n + j_tot,n = 2 W_e B_5 (tau_(n+1) - tau_n) + 2 p_n + j_tot,n = 0,

   which determines

       p_n = -(1/2) j_tot,n - W_e B_5 (tau_(n+1) - tau_n).

4. **Discrete Bianchi / Constraint-Propagation Identity:**
   When `tau_n` and `tau_(n+1)` solve the Hamiltonian constraint on bonds `n`
   and `n+1`, applying `B_5^T` to `p_n` yields the exact off-shell identity

       B_5^T p_n = -(1/2) [ B_5^T j_tot,n + Pi_0 (e_loc,n+1 - e_loc,n) ]
                 = -(1/4) Pi_0 [ q_h,n * R_h,n + q_chi,n R_chi,n sigma ],

   where `*` is pointwise vertex multiplication. On-shell (`R_h,n = 0` and
   `R_chi,n = 0`), `B_5^T p_n = 0` holds identically at every step `n >= 1`,
   so `p_n in K_E = ker B_5^T` without any ad hoc projection.
5. **Auxiliary and dynamical variations (`p_n`, `tau_n`, `h_n`, `chi_n`):**
   Stationarity with respect to `p_n in K_E` and `tau_n in e^perp` holds at
   the gauge representative `ell_hom,n = 0`, `ell_lapse,n = 0`, `N_shift,n = 0`,
   where the cubic backreaction terms in the `h_n` and `chi_n` variations
   vanish and the dynamical equations remain `R_h,n = 0` and `R_chi,n = 0`.

To test all partial derivatives locally without boundary interference, fix
neighboring slices `(h_(n-1), chi_(n-1))` and `(h_(n+1), chi_(n+1))` and
define the 48-coordinate two-bond local cubic action

    A_cubic,loc(v, xi, tau_n, tau_(n+1), p_n,
                ell_hom,n, ell_hom,n+1, ell_lapse,n, ell_lapse,n+1, N_shift,n)
      = A_local(v, xi)
        - ell_hom,n (Htot_n(v, xi) - E_hom)
        - ell_hom,n+1 (Htot_(n+1)(v, xi) - E_hom)
        + 2 <ell_lapse,n, L tau_n>_V - <ell_lapse,n, Pi_0 e_loc,n(v, xi)>_V
        + 2 <ell_lapse,n+1, L tau_(n+1)>_V - <ell_lapse,n+1, Pi_0 e_loc,n+1(v, xi)>_V
        + 2 <N_shift,n, W_e B_5 (tau_(n+1) - tau_n) + p_n>_E
        + <N_shift,n, j_tot,n(v)>_E,

where `A_local(v, xi)` is the reduced quadratic local action of #1650:

    A_local(v, xi) = (||v - h_(n-1)||^2 + ||h_(n+1) - v||^2) / 2 - <v, L v> / 2
                     + ((xi - chi_(n-1))^2 + (chi_(n+1) - xi)^2) / 2
                     - xi^2 / 2 + A_src xi + g xi <ell, v>.

Because `A_cubic,loc` has degree at most 2 in each of its 48 arguments when
the other 47 are held fixed, the central unit difference
`[A_cubic,loc(x_i + 1) - A_cubic,loc(x_i - 1)] / 2` equals the exact partial
derivative `d A_cubic,loc / d x_i` for every `i = 1, ..., 48`, both on-shell
and off-shell/off-gauge.

## 5. Autonomous integer carrier and exact integer constraint lift

The 21-coordinate integer core `x = (Z, R, D, H)` with `Z = (P_0..P_4, Y) in Z^6`,
`R = (Q_0..Q_4, V) in Z^6`, `D in Z_(>=1)`, `H in Z^8`, its bare step `T(x)`

    Z' = B Z - m R + 81 a D e_6,   R' = m Z,   D' = m D,
    H' = M(Y' - Y) H M(Y' - Y)^dagger,

its 13-condition partial inverse, the positive arithmetic account
`E(x) = 1 + D + ||Z||^2 + ||R||^2 + N(H)`, and the 23-coordinate funded
bijection `F(x, b, epsilon)` are identical to #1650.

On any integer core `x = (Z, R, D, H)` in the unrestricted carrier, define
the exact integer bond energy-density vector `E_int(x) in Z^5` and integer
scalar constraint potential `Theta(x) in Z^5` at denominator scales
`4 m D^2 = 1296 D^2` and `8 * 53605 D^2 = 428840 D^2`:

    E_int(x)(r) = 2 m (P_r - Q_r)^2
                  + sum_(e incident to r) (m w_e) (B_5 P)_e (B_5 Q)_e
                  + (2 sigma_r) [ m (Y - V)^2 + m Y V - 81 a D (Y + V) ]
                  - 2 ell_r (V P_r + Y Q_r),
    Theta(x) = L_adj E_int(x).

Then `e_loc(x) = E_int(x) / (4 m D^2)` and `tau(x) = Theta(x) / (8 * 53605 D^2)`,
and on the entire unrestricted carrier

    sum_(r=0)^4 Theta(x)(r) = 0,
    L_int Theta(x) = 10721 (5 E_int(x) - (sum_s E_int(x)(s)) e).

For any core `x = (Z, R, D, H)` and its bare forward image `x' = T(x) = (Z', R', D', H')`,
let `Q_Delta(x) = Z' - m R = (Q_Delta,h(x), Q_Delta,chi(x)) in Z^6`. Define the
integer edge momentum current `J_int(x) in Z^10` at scale `4 m^2 D^2` and the
integer co-closed momentum `Pi_int(x) in Z^10` at scale `8 * 53605 m^3 D^2`:

    J_int(x)(e) = (m w_e) (B_5 P)_e [ Q_Delta,h(x)(tail e) + Q_Delta,h(x)(head e) ]
                  - Q_Delta,chi(x) (P_0 + P_1) delta_(e, e_0),
    Pi_int(x) = -53605 m J_int(x)
                - (m W_e) B_5 (Theta(T(x)) - m^2 Theta(x)).

Then `j_tot(x) = J_int(x) / (4 m^2 D^2)` and `p(x) = Pi_int(x) / (8 * 53605 m^3 D^2)`,
and for every `x` on the unrestricted integer carrier, the exact integer
continuity and discrete Bianchi equations hold in `Z^5`:

    (E_int(T(x)) - m^2 E_int(x)) + m B_5^T J_int(x) = 0,
    B_5^T Pi_int(x) = 0.

## 6. Prepared family, Lorentz domain, and fixed exact witnesses

The thirty prepared histories (`ten canonical words` in fixed table order
`0010, 0011, 0100, 0101, 0110, 1001, 1010, 1011, 1100, 1101` and
`a in {-1, 0, 1}`) use the same attenuated initial data as #1650:

    h_t = e/5 + (h_t^can - e/5)/4,   t = 0, 1,
    chi_0 = 0,   chi_1 = a/4,
    D_1 = 40,   P_1 = 6 e + 5 P_1^can,   Q_1 = 6 e + 5 P_0^can,
    Y_1 = 10 a,   V_1 = 0,   H_1 = H_(10 a).

All-counter energy, amplitude, source, Lorentz signature, and 3-adic
denominator bounds from #1650 remain in force: `0 < Htot_n < 3/50`,
`-1/4 < h_n(r) < 13/20`, `|chi_n| < 3/4`, `det g_n(r) < -231/400 < 0`, and
`v_3(d_n) = 4(n - 1)` for `n >= 1`.

In addition to the direct contrast `h_2(+) - h_2(-) = ell / 648` at word
`0010`, the affine Wronskian drift `1/10368` at `(0010, 0011), a = 1`, the
sharp first bank `70657245` at `word 0011, a = 0`, and the six least cycle
periods `2,4,2,4,2,4`, this probe freezes six new constraint and cubic-action
witnesses at `word 0011, a = 0, n = 1`:

1. **Initial integer and rational local vertex energy density:**

       E_int,1 = (2350, 3975, 3975, 2350, 3250),
       e_tot,1 = (47/41472, 53/27648, 53/27648, 47/41472, 65/41472),
       sum_(r=0)^4 e_tot,1(r) = 53/6912 = Htot_1.

2. **Initial integer and rational Hamiltonian constraint potential:**

       Theta_1 = (-211250, 173775, 173775, -211250, 74950),
       tau_1 = (-845/2744576, 6951/27445760, 6951/27445760, -845/2744576, 1499/13722880).

3. **Nonzero dipole interaction current at the first step:**
   Although `chi_0 = chi_1 = 0`, reciprocal feedback creates `chi_2 = -1/2592`,
   so on bond 2 the local source-plus-interaction energy density has a
   nonzero dipole `(+17/134369280, -17/134369280, 0, 0, 0)` whose spatial sum
   is zero. This local dipole shift is transported across `e_0 = (0, 1)` by

       J_int_curr,1(e_0) = 85,
       j_int,1(e_0) = 17/134369280.

4. **Bianchi defect when the dipole interaction current is omitted:**
   Replacing `j_tot,1` by the free-TT current `j_h,1` in `p_1` while keeping
   `tau_1, tau_2` breaks co-closure at sites `0` and `1`:

       B_5^T p_1^(no-int-current) = (-17/268738560, 17/268738560, 0, 0, 0) != 0.

5. **Bianchi defect under reversed feedback sign:**
   Reversing the feedback sign at `word 0011, a = 0, n = 1` gives
   `chi_2^(rev) = +1/2592` and `R_chi,1^(rev) = +1/1296`, breaking co-closure
   at all five vertices in exact agreement with the off-shell Bianchi formula:

       B_5^T p_1^(rev-feedback)
         = (-1/44789760, -1/44789760, 1/67184640, 1/67184640, 1/67184640) != 0.

6. **Off-gauge cubic shift-to-field backreaction gradient:**
   At `word 0011, a = 0, n = 1`, setting the dipole-edge shift multiplier to
   `N_shift,1 = delta_(e_0)` while keeping `(h, chi, tau, p)` on-shell shifts
   the `h_1` gradient of `A_cubic,loc` from zero to

       grad_(h_1) A_cubic,loc |_(N_shift,1 = delta_(e_0))
         = (943/1679616, -157/279936, 0, 0, 0) != 0.

## 7. Exact finite audit and negative controls

### 7.1 Authority, ring, full carrier, and integer constraint lift on fixtures

Both programs check the five normative files (`AUTHORITY_FILES=5`), the 19
Hermitian fixtures across 7 gates (`TRANSPORT_CHECKS=133`) and 5 holonomy
parameters (`HOLONOMY_CHECKS=95`), the 172 core fixtures (`CORE_FIXTURES=172`),
the 4128 funded transitions (`FUNDED_CASES=4128`), and the 2223 corrupted
images (`IMAGE_DEFECTS=2223`) exactly as in #1650.

In addition, for every one of the 172 core fixtures `(a, x)` and `y = T(x)`:
- require `E_int(x), Theta(x), E_int(y), Theta(y) in Z^5` and
  `J_int(x), Pi_int(x) in Z^10`;
- require `sum_r Theta(x)(r) = 0`, `L_int Theta(x) = 10721 (5 E_int(x) - sum(E_int(x)) e)`,
  `(E_int(y) - m^2 E_int(x)) + m B_5^T J_int(x) = 0`, and `B_5^T Pi_int(x) = 0`;
- in all 4128 funded cases, whenever a step reflects, require the decoded
  `e_tot` and `tau` to be unchanged.

### 7.2 Histories, constraint bonds, Bianchi slices, and digests

Evolve all 30 histories (`10 words x 3 contexts a in {-1, 0, 1}`) through
`n = 12`, checking all 390 dynamical records (`HISTORY_RECORDS=390`) and
their SHA-256 digest (`HISTORY_SHA256`), 360 3-adic joint denominator checks
(`PRECISION_CHECKS=360`), 330 canonical Legendre steps (`CANONICAL_STEPS=330`),
and 1620 centered symplectic checks (`SYMPLECTIC_CHECKS=1620`).

Across all 30 histories:
- At every bond `n = 1, ..., 12` (`30 * 12 = 360` `CONSTRAINT_BONDS`), check
  `E_int,n in Z^5`, `Theta_n = L_adj E_int,n in Z^5`, `sum_r Theta_n(r) = 0`,
  `L_int Theta_n = 53605 Pi_0 E_int,n`, rational decoding
  `e_loc,n = E_int,n / (4 m D_n^2)` and `tau_n = Theta_n / (8 * 53605 D_n^2)`,
  `sum_r e_tot,n(r) = Htot_n = Htot_1`, `0 < Htot_n < 3/50`, and the rational
  Hamiltonian constraint `2 L tau_n = Pi_0 e_tot,n`.
- At every interior slice `n = 1, ..., 11` (`30 * 11 = 330` `BIANCHI_SLICES`),
  check `J_int,n in Z^10`, `Pi_int,n in Z^10`, rational decoding
  `j_tot,n = J_int,n / (4 m^2 D_n^2)` and `p_n = Pi_int,n / (8 * 53605 m^3 D_n^2)`,
  rational local continuity `(e_tot,n+1 - e_tot,n) + B_5^T j_tot,n = 0`,
  integer local continuity `(E_int,n+1 - m^2 E_int,n) + m B_5^T J_int,n = 0`,
  rational momentum constraint `2(W_e B_5(tau_(n+1) - tau_n) + p_n) + j_tot,n = 0`,
  rational co-closure `B_5^T p_n = 0`, and integer co-closure `B_5^T Pi_int,n = 0`.
- Hash the 330 integer constraint slice records in `word, a, n` order (`n = 1..11`),
  one LF per record, signed decimal integers without spaces:

      word|a|n|E0,E1,E2,E3,E4|T0,T1,T2,T3,T4|J0,J1,J2,J3,J4,J5,J6,J7,J8,J9|PI0,PI1,PI2,PI3,PI4,PI5,PI6,PI7,PI8,PI9\n

  where `E` is `E_int,n`, `T` is `Theta_n`, `J` is `J_int,n`, and `PI` is
  `Pi_int,n`. Emit the lowercase hex digest as `CONSTRAINT_SHA256`.

### 7.3 On-shell and off-shell/off-gauge 48-coordinate cubic action checks

Order the 48 local coordinates of `A_cubic,loc` at cell `[n-1, n+1]` as:
`v(0..4)` (5), `xi` (1), `tau_n(0..4)` (5), `tau_(n+1)(0..4)` (5), `p_n(0..9)` (10),
`ell_hom,n` (1), `ell_hom,n+1` (1), `ell_lapse,n(0..4)` (5),
`ell_lapse,n+1(0..4)` (5), `N_shift,n(0..9)` (10).

- **On-shell / on-gauge (`CUBIC_VARIATIONS=5760`):**
  For every history `(word, a)` and `n in {1, 2, 5, 11}`, set `(v, xi) = (h_n, chi_n)`,
  `tau_n, tau_(n+1), p_n` to their on-shell constraint values, `E_hom = Htot_1`,
  and all multipliers `ell_hom, ell_lapse, N_shift` to zero. Evaluate all 48
  central unit differences `[A_cubic,loc(x_i + 1) - A_cubic,loc(x_i - 1)] / 2`
  and require all `30 * 4 * 48 = 5760` derivatives to equal zero.

- **Off-shell / off-gauge (`OFFSHELL_CUBIC_VARIATIONS=288`):**
  Start from the baseline on-shell/on-gauge point of `word 0011, a = 0` at
  `n = 2` and form six test configurations:
  1. `v = h_2 + (1, 0, 0, 0, 0)` and `ell_lapse,2 = (1, -1, 0, 0, 0)`;
  2. `xi = chi_2 + 1` and `ell_hom,2 = 1`;
  3. `chi_next = chi_3 + 1` and `N_shift,2 = (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)`;
  4. `h_next = h_3 + (0, 0, 1, 0, 0)`, `tau_2 = tau_2^(on) + (1, -1, 0, 0, 0)`,
     and `ell_lapse,3 = (0, 1, -1, 0, 0)`;
  5. `chi_prev = chi_1 - 1`, `p_2 = p_2^(on) + (1, 1, 1, 1, 1, 0, 0, 0, 0, 0)`,
     and `N_shift,2 = (0, 1, 0, 0, 0, 0, 0, 0, 0, 0)`;
  6. General rational configuration at `a = 1`, `E_hom = 1/7`:
     `v = (1/3, -2/5, 0, 3/7, -1)`, `xi = -2/3`, `h_prev = (0, 0, 0, 0, 0)`,
     `h_next = (1, 1, 1, 1, 1)`, `chi_prev = 1/2`, `chi_next = -3/4`,
     `tau_2 = (1/2, -1/2, 1/3, -1/3, 0)`, `tau_3 = (0, 1/5, -1/5, 1/4, -1/4)`,
     `p_2 = (1/2, -1/3, 0, 1/5, -1/2, 1/4, 0, -1/4, 1/6, -1/6)`,
     `ell_hom,2 = 1/3`, `ell_hom,3 = -1/2`,
     `ell_lapse,2 = (1, -1/2, 0, -1/2, 0)`,
     `ell_lapse,3 = (0, 1, -1, 1/3, -1/3)`,
     `N_shift,2 = (1, 0, -1/2, 0, 1/3, -1/4, 1/2, 0, 0, -1)`.

  In each of the six cases:
  - require all 48 central unit differences to equal the closed-form
    analytical 48-gradient vector (`6 * 48 = 288` checks);
  - require at least one dynamical gradient (in `v, xi`) and at least one
    constraint/multiplier gradient (in the remaining 42 coordinates) to be
    nonzero;
  - on the three-slice data `(h_prev, chi_prev), (v, xi), (h_next, chi_next)`
    of each case, verify both the off-shell pointwise continuity identity and
    the off-shell Bianchi identity at all five vertices.

### 7.4 Green operator, Gram minors, witnesses, and negative controls

Verify the exact matrix identities `L = B_5^T W_e B_5`,
`L_int L_adj = L_adj L_int = 53605 Pi_0`, and `rank(B_5^T) = 4` (`dim K_E = 6`).
In addition to the 15 leading principal minors of the three 5x5 coupled
stiffness Gram matrices from #1650, form the 4x4 Gram matrix of `L` in the
basis `e_i - e_4` (`i = 0, 1, 2, 3`) of `e^perp` and require all 4 leading
principal minors of size `1, 2, 3, 4` to be strictly positive: `15 + 4 = 19`
`GREEN_MINOR_CHECKS`.

Verify all witnesses of Section 6 and all ten negative controls:
1. Disable field-to-source feedback at `word 0011, a = 0`: `chi` stays zero
   and `h` is the attenuated free field, while the joint source gradient at
   `n = 1` is `-1/2592 != 0`.
2. Retain feedback only at `n = 1`: `chi_3 - chi_3^(first) = -71/839808 != 0`,
   and at `n = 2` (where both `q_chi,2 != 0` and `R_chi,2 != 0`) the Bianchi
   divergence `B_5^T p_2` is nonzero.
3. Disable source-to-field coupling while retaining feedback at `word 0011, a = 0`:
   the metric gradient at `n = 2` is `-ell / 839808 != 0` and `B_5^T p_2 != 0`.
4. Reverse the feedback sign at `word 0011, a = 0`: at `n = 1` the source
   gradient is `-1/1296 != 0` and the Bianchi defect is
   `B_5^T p_1^(rev-feedback) = (-1/44789760, -1/44789760, 1/67184640, 1/67184640, 1/67184640) != 0`.
5. Omit the dipole interaction current `j_int,n` from `j_tot,n`: at
   `word 0011, a = 0, n = 1` the Bianchi defect is
   `B_5^T p_1^(no-int-current) = (-17/268738560, 17/268738560, 0, 0, 0) != 0`.
6. Omit the source and interaction energy densities `e_chi,loc + e_int` from
   the Hamiltonian constraint `2 L tau = Pi_0 e`: at `word 0011, a = 0, n = 1`
   the resulting momentum record has nonzero divergence
   `(17/268738560, -17/268738560, 0, 0, 0) != 0`.
7. Turn on the off-gauge shift multiplier `N_shift,1 = delta_(e_0)` at
   `word 0011, a = 0, n = 1`: the cubic backreaction shifts the `h_1`
   gradient to `(943/1679616, -157/279936, 0, 0, 0) != 0`.
8. Omit Hermitian transport: at `word 0011, a = 0, n = 2` the monitor
   coefficient stays `0` while `Y_2 = -5`.
9. Omit interaction energy `I_n` from `Htot_n`: at `word 0011, a = 0` the
   first bond energy increment is `+1/13436928 != 0`.
10. Evaluate the unrestricted core `D = 1, P = (1, 0, 0, 0, 0), Y = 0, Q = (0, 0, 0, 0, 0), V = 0, H = D_H`:
    its metric at site `0` has determinant `0` (outside the prepared Lorentz
    domain).

## 8. Certificate grammar, falsifiers, and completion

Each implementation emits the same 30-line certificate as unmodified ASCII
bytes, with one LF after each line:

    CERTIFICATE=P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1
    AUTHORITY_FILES=5
    TRANSPORT_CHECKS=133
    HOLONOMY_CHECKS=95
    CORE_FIXTURES=172
    FUNDED_CASES=4128
    IMAGE_DEFECTS=2223
    HISTORY_RECORDS=390
    HISTORY_SHA256=<computed lowercase SHA-256>
    CONSTRAINT_BONDS=360
    BIANCHI_SLICES=330
    CONSTRAINT_SHA256=<computed lowercase SHA-256>
    CUBIC_VARIATIONS=5760
    OFFSHELL_CUBIC_VARIATIONS=288
    GREEN_MINOR_CHECKS=19
    PRECISION_CHECKS=360
    CANONICAL_STEPS=330
    SYMPLECTIC_CHECKS=1620
    DIRECT_CONTRAST=1/648,-1/648,0,0,0
    ZERO_SOURCE_ENERGY_DENSITY=47/41472,53/27648,53/27648,47/41472,65/41472
    ZERO_SOURCE_TAU1=-845/2744576,6951/27445760,6951/27445760,-845/2744576,1499/13722880
    ZERO_SOURCE_INTERACTION_CURRENT=17/134369280
    NO_INTERACTION_CURRENT_BIANCHI_DEFECT=-17/268738560,17/268738560,0,0,0
    REVERSED_FEEDBACK_BIANCHI_DEFECT=-1/44789760,-1/44789760,1/67184640,1/67184640,1/67184640
    SHIFT_CUBIC_BACKREACTION=943/1679616,-157/279936,0,0,0
    AFFINE_WRONSKIAN_DRIFT=1/10368
    ZERO_SOURCE_FIRST_BANK=70657245
    CYCLE_PERIODS=2,4,2,4,2,4
    NEGATIVE_CONTROLS=PASS
    CERTIFICATE_RESULT=PASS

`verify.py` launches `breaker.py` in a child process with the same Python
executable and `-I`, requires exit code zero, empty stderr, and exact raw
certificate byte identity, and appends two lines:

    BREAKER_RAW_BYTES=IDENTICAL
    RESULT=PASS

Successful primary stdout therefore has 32 LF-terminated lines. Registered
falsifier keys are:

    AUTHORITY, RING, TRANSPORT, HOLONOMY, COST, INITIAL_DATA,
    INTEGER, BARE_INVERSE, FUNDED_INVERSE, CONSERVATION, BRANCH,
    IMAGE_GUARD, RECURRENCE, MEAN, SOURCE_READER, LORENTZ,
    SOURCE_BOUND, EQUILIBRIUM, ENERGY, PRECISION, GRAM,
    GREEN, CONTINUITY, HAMILTONIAN_CONSTRAINT, MOMENTUM_CONSTRAINT,
    BIANCHI, INTEGER_CONSTRAINT, ACTION, OFFSHELL_ACTION,
    CANONICAL, SYMPLECTIC, FIXED_COUNTER, CONTROL,
    SHARP_BUDGET, PERIOD, CERTIFICATE, BREAKER_BYTES.
