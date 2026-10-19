# Result: P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1

Status: PASS  
Scope: NON-CANONICAL, L1  
Prospective pin: `5e072359a029233d1c2b266c0c4bed2269752535`  
Ownership: https://github.com/mathorn1973/twist-j/issues/1651

## 1. Observed finite certificate

Both `verify.py` (integer recurrence, cyclotomic polynomial ring `Z[j]`,
closed-form circulant Green operator `L_adj`) and `breaker.py` (rational
evolution, direct 8-coordinate Hermitian transforms, 4x4 Gaussian
elimination on `e^perp` for the Hamiltonian constraint) completed with exit
code `0`, empty stderr, and byte-identical 30-line, 1120-byte certificates
(SHA-256 `00772b4ff20e029ed5700161ad3279717589a99a4e8400f8188ea8f30bc752e3`).
The full 32-line, 1160-byte primary output (`EXPECTED.txt`, SHA-256
`b195d97ff97f33cb9c42255a5db95c667c085888d9168b3d5859a4e3348c4630`) is:

```text
CERTIFICATE=P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1
AUTHORITY_FILES=5
TRANSPORT_CHECKS=133
HOLONOMY_CHECKS=95
CORE_FIXTURES=172
FUNDED_CASES=4128
IMAGE_DEFECTS=2223
HISTORY_RECORDS=390
HISTORY_SHA256=8e5c908f2b219bf76660f07b888a428529ae18eeee89123814115bdebbefa834
CONSTRAINT_BONDS=360
BIANCHI_SLICES=330
CONSTRAINT_SHA256=1987b93fc01d457a20a7b59bd9b0cb04b8efeb46afe7b289351fa52e948572b8
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
BREAKER_RAW_BYTES=IDENTICAL
RESULT=PASS
```

## 2. Main earned mathematical conclusions

1. **Local coupled stress-energy density, dipole interaction current, and exact off-shell continuity.**
   On the five-site planar incidence carrier `(X = Z/5, E_5, B_5, W_e)` with
   `L = B_5^T W_e B_5`, the interaction-inclusive bond energy `Htot_n` of
   `P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1` (#1650) resolves into a vertex
   energy density `e_tot,n(r) = e_loc,n(r) + E_*/5` (`sum_r e_tot,n(r) = Htot_n`)
   and a 10-edge momentum current `j_tot,n = j_h,n + j_int,n` whose
   dipole-edge interaction current

       j_int,n(e) = -(g / 4)(chi_(n+1) - chi_(n-1))(h_n(0) + h_n(1)) delta_(e, e_0)

   transports the local source-plus-interaction dipole across `e_0 = (0, 1)`.
   For arbitrary off-shell three-slice data, `(e_tot,n+1 - e_tot,n) + B_5^T j_tot,n`
   equals `(1/2) q_h,n * R_h,n + (1/2) q_chi,n R_chi,n sigma` at every vertex
   `r in Z/5`, and vanishes identically on-shell (`CONSTRAINT_BONDS=360`,
   `BIANCHI_SLICES=330`).

2. **Cubic constraint-coupled action and 48-coordinate exact variations.**
   Coupling `A_auto` to the homogeneous lapse `ell_hom,n`, mean-zero
   inhomogeneous lapse `ell_lapse,n in e^perp`, scalar constraint potential
   `tau_n in e^perp`, edge shift `N_shift,n`, and co-closed momentum
   `p_n in K_E = ker B_5^T` produces a cubic action whose independent
   variations yield the dynamical equations `R_h,n = 0`, `R_chi,n = 0`,
   the homogeneous constraint `Htot_n = E_hom`, the Discrete Hamiltonian
   Constraint `2 L tau_n = Pi_0 e_tot,n`, the Discrete Momentum Constraint
   `2(W_e B_5(tau_(n+1) - tau_n) + p_n) + j_tot,n = 0`, and multiplier
   stationarity `ell_hom,n = 0`, `ell_lapse,n = 0`, `N_shift,n = 0`. All
   `30 * 4 * 48 = 5760` on-shell/on-gauge central unit differences vanish,
   and all `6 * 48 = 288` off-shell/off-gauge central unit differences match
   the closed-form 48-component analytical gradient (including cubic
   multiplier-to-field backreaction terms).

3. **Closed-form circulant Green operator and exact discrete Bianchi propagation.**
   The integer circulant operator `(L_adj v)_r = 188 v_r - 65(v_(r-1) + v_(r+1)) - 29(v_(r-2) + v_(r+2))`
   satisfies `L_int L_adj = L_adj L_int = 53605 Pi_0`, giving the unique
   mean-zero Hamiltonian constraint solution `tau_n = (162/53605) L_adj e_loc,n`
   without numerical linear solving. Substituting `tau_n, tau_(n+1)` into
   `p_n = -(1/2) j_tot,n - W_e B_5(tau_(n+1) - tau_n)` yields the exact
   off-shell Bianchi identity

       B_5^T p_n = -(1/4) Pi_0 [ q_h,n * R_h,n + q_chi,n R_chi,n sigma ],

   so `B_5^T p_n = 0` (`p_n in K_E`) holds identically at every step on-shell.

4. **Autonomous integer constraint lift on the unrestricted carrier.**
   For every state `x = (Z, R, D, H)` on the unrestricted 21-coordinate
   integer carrier and its autonomous forward image `T(x)` (tested across all
   172 core fixtures and all 30 prepared histories through `n = 12`), the
   scaled records `E_int(x) = 4 m D^2 e_loc(x) in Z^5`,
   `Theta(x) = L_adj E_int(x) = 428840 D^2 tau(x) in Z^5`,
   `J_int(x) = 4 m^2 D^2 j_tot(x) in Z^10`, and
   `Pi_int(x) = 8 * 53605 m^3 D^2 p(x) in Z^10` are exact integer vectors
   satisfying `sum_r Theta_r(x) = 0`, `L_int Theta(x) = 53605 Pi_0 E_int(x)`,
   `(E_int(T(x)) - m^2 E_int(x)) + m B_5^T J_int(x) = 0`, and
   `B_5^T Pi_int(x) = 0` in `Z^5`.

5. **Decisive witnesses at `word 0011, a = 0, n = 1`.**
   - `E_int,1 = (2350, 3975, 3975, 2350, 3250)` and
     `e_tot,1 = (47/41472, 53/27648, 53/27648, 47/41472, 65/41472)`,
     summing to `53/6912 = Htot_1`.
   - `Theta_1 = (-211250, 173775, 173775, -211250, 74950)` and
     `tau_1 = (-845/2744576, 6951/27445760, 6951/27445760, -845/2744576, 1499/13722880)`.
   - Although `chi_0 = chi_1 = 0`, reciprocal feedback creates `chi_2 = -1/2592`,
     inducing a local dipole energy shift `(17/134369280, -17/134369280, 0, 0, 0)`
     on bond 2 whose global sum is zero and whose local divergence is balanced
     by `j_int,1(e_0) = 17/134369280` (`J_int_curr,1(e_0) = 85`).
   - Omitting `j_int,1` breaks co-closure with
     `B_5^T p_1^(no-int-current) = (-17/268738560, 17/268738560, 0, 0, 0) != 0`.
   - Reversing the feedback sign breaks co-closure across all five vertices with
     `B_5^T p_1^(rev-feedback) = (-1/44789760, -1/44789760, 1/67184640, 1/67184640, 1/67184640) != 0`.
   - Turning on the off-gauge dipole shift multiplier `N_shift,1 = delta_(e_0)`
     produces the cubic backreaction gradient
     `grad_(h_1) A_cubic,loc = (943/1679616, -157/279936, 0, 0, 0) != 0`.

## 3. Explicit boundaries of the earned scope

This result has scope `NON-CANONICAL, L1`. It establishes the first nonlinear
(cubic) constraint-coupling correction and exact discrete Hamiltonian and
momentum constraint propagation for the autonomous coupled integer
metric-and-source system on the five-site planar carrier. Full
non-perturbative 4D Einstein equations, three-dimensional 125-site active
source coupling, native-U derivation of the source coupling, continuum
manifold limits, and physical SI calibration remain open obligations.
