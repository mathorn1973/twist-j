# Maurer-Cartan off-shell lapse gauge closure and forced affine scalar-lapse completion

Status: PASS
Scope: NON-CANONICAL, NEW_DECLARED L1, scalar normal-form sector (6-component reduced carrier q = (h, chi)), forces a in {-1, 0, 1}
Theorem status: conditional candidate-T; no Canon promotion
Fired falsifiers: none
Ownership: https://github.com/mathorn1973/twist-j/issues/1669
Preregistration pin: 04e21ecf4a866cd861d875706050006e0d0fbd59

## Universal Maurer-Cartan gauge curvature factorization

For any skew-symmetric interior operator series A_t(s) = -A_t(s)^T on R^{6(T-1)}
linear in the lapse direction t, the gauge-adjusted lapse generator

    delta_tilde_t = partial_t + (L_t(s) + A_t(s) H(s)) q . nabla_q

preserves the all-order off-shell Ward identity delta_tilde_t S(q, s) = 0,
transforms the Euler-Lagrange vector covariantly as

    delta_tilde_t(nabla_q S(q, s)) = -L_tilde_t(s)^T nabla_q S(q, s),

and has an off-shell bracket that factors identically through nabla_q S(q, s):

    [delta_tilde_t, delta_tilde_r] q = F_{t,r}(s) nabla_q S(q, s),

where the Maurer-Cartan gauge curvature is

    F_{t,r}(s) = Omega_{t,r}(s) + partial_t A_r - partial_r A_t
                 + (L_r A_t + A_t L_r^T) - (L_t A_r + A_r L_t^T)
                 + A_r H A_t - A_t H A_r.

Consequently, the raw generator (A_t = 0) never closes off-shell at any order
because Omega_{t,r}^{(0)} != 0 (`NC02`).

## Degree-3 2-bond and degree-4 3-bond off-shell commutation

At degree 3 in combined (s, q) (order O(s) in F_{t,r}), the residual curvature
of the `#1664`/`#1666` 1-bond extension A_t^{(1)}(s) decomposes into a 1-bond
spatial block proportional to C and a 2-bond scalar block proportional to I_6.
Evaluating this residual on the `#1666` witness trajectory and lapse pairs gives
exact agreement with the `#1666` degree-3 commutator residual

    (-395/5184, 0, 395/5184, -1/144, 1/144, -1/5184) = -(1/8) C u,

and demonstrates that 100% of that witness arises from the 2-step convective
transport coupling [Sigma_{t,r}^{(1)}(s)]_{1,3} (H_0 q)_3. No nearest-neighbor
(|m - n| <= 1) skew-symmetric adjustment can cancel the 2-bond block (`NC03`).
Adding the explicit 2-bond quadratic skew kernel A_t^{(2)}(s) cancels the entire
O(s) curvature and achieves exact off-shell commutation through degree 3 across
all horizons T >= 3 with zero boundary defect (`NC04`).

At degree 4 in combined (s, q) (order O(s^2) in F_{t,r}), the quadratic
self-interaction A_r^{(1)} H_0 A_t^{(1)} - A_t^{(1)} H_0 A_r^{(1)} is required
for the parameter-space Bianchi 2-cocycle condition

    partial_u R_{t,r}^{(2)} + partial_t R_{r,u}^{(2)} + partial_r R_{u,t}^{(2)} = 0.

Omitting A^{(1)} H_0 A^{(1)} violates the Bianchi identity by +(1/32) s_4 I_6
at stencil offset (1, 4) (`NC05`), which would make any exact primitive
A_t^{(3)}(s) impossible. Including the full nonlinear Maurer-Cartan curvature,
the Bianchi 2-cocycle vanishes identically on all 20 upper-triangular interior
slice pairs across T in {3, 4, 5, 6}, and the explicit 3-bond cubic skew kernel
A_t^{(3)}(s) (including the Dirichlet boundary-reflection shift
-s_1^2(s_1 + s_2) t_2 / 128 I_6 at (1, 2) and its time-reversal at (T-2, T-1),
`NC06`) closes the off-shell gauge algebra identically through degree 4:

    [delta_tilde_t^{<= 4}, delta_tilde_r^{<= 4}]_{<= 4} q = 0.

## Forced affine scalar-lapse completion and vacuum cold-start shell

For the forced linear source drive f_* = (0, 0, 0, 0, 0, a/4)^T with
a in {-1, 0, 1}, the spatial potential matrix V = K_mat + G_mat is uniquely
invertible on 1_5^perp (+) Q, yielding the exact equilibrium shift

    x_* = (a / 17367514) (20493, -20493, 2916, 0, -2916, 4342005)^T,

with equilibrium energy and vacuum cold-start potential energy

    E_* = (1/2) x_*^T V x_* = (4342005 / 8683757) (a/4)^2,
    E_cold = (1/2) x_*^T D x_* = E_* - (1/8) ||f_*||^2 = (26052283 / 69470056) (a/4)^2.

The affine scalar-lapse action S^{(a)}(q, s) = S(q - x_*^{(T)}, s) + E_* sum_b s_b
reduces at s = 0 to the exact `#1650` forced action up to the path-independent
endpoint constant C_end(q_0, q_T) (`NC07`), satisfies the exact all-order
off-shell Ward identity delta_tilde_t^{(a)} S^{(a)}(q, s) = 0, and closes
off-shell through degree 4 under the shifted Maurer-Cartan generators.

Crucially, for the canonical vacuum cold-start initial condition q_{-1} = q_0 = 0
of `#1650` (`#1641`), the shifted phase-space initial data are q_tilde_0 = -x_*
and p_tilde_0 = (1/2) f_* = (0_5, a/8)^T. The kinetic momentum term
(1/2)||p_tilde_0||^2 = (1/8)||f_*||^2 adds to E_cold to give the exact total
bond energy

    H_bond(-x_*, (1/2) f_*) = E_cold + (1/8) ||f_*||^2 = E_*.

Therefore, the canonical vacuum cold-start trajectory satisfies the free-lapse
variational equation partial S^{(a)} / partial s_b = -H_bond + E_* = 0 on every
bond (`NC08`), while evolving into a non-static oscillating trajectory with
h_2^{(+)} - h_2^{(-)} = (1/648)(1, -1, 0, 0, 0) != 0 for a = +-1.

## Exact finite audit

The independently implemented primary (`verify.py`) and breaker (`breaker.py`)
agree byte-for-byte on the 15-line raw certificate output (`BREAKER_RAW_BYTES=IDENTICAL`).

| Audit | Completed count per implementation |
|---|---:|
| Normative authority files | 5 |
| Formal series order audited | 4 |
| Universal Maurer-Cartan factorization cases | 12 |
| Degree-2 off-shell bracket cases | 12 |
| Degree-3 off-shell bracket cases | 12 |
| Degree-4 off-shell bracket cases | 12 |
| Bianchi 2-cocycle upper-triangular entries | 20 |
| Forced affine Ward cases across a in {-1, 0, 1} | 18 |
| Vacuum cold-start shell and metric-witness slices | 18 |
| Deliberate negative controls detected | 8 |

Payload SHA-256:
`61a0a26870a30489eae5687650acfae4b58e9af62c556385ea7f87fd7342db97`.
The exact 499-byte, 17-line stdout is `EXPECTED.txt`; `RUN.md` records the
first completed execution.

## Boundaries and scope limits

This probe remains strictly `NON-CANONICAL`, `NEW_DECLARED L1`. It establishes
off-shell Maurer-Cartan gauge closure through degree 4 (with stencil width k-1
at degree k) and the forced affine scalar-lapse completion for the linear 6-DOF
carrier. It does not claim closed-form all-order expressions for A_t^{(k)} for
k >= 4, spatially varying lapse N(n, x), nonlinear self-gravitating metric
backreaction, or a native-U integer lift of the transcendental matrix
exponential exp(s K). Earlier abandoned pins `#1672` (`41632126`) and `#1673`
(`2fe6646b`) remain intact as `Status: ABANDONED`. Canon, registry, policy, and
workflows are unchanged.
