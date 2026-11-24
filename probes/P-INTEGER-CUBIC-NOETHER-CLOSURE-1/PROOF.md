# Exact Noether order, global variations, and closure obstruction

Status: PROSPECTIVE. Scope: NON-CANONICAL, L1.  
Probe: P-INTEGER-CUBIC-NOETHER-CLOSURE-1.  
Ownership: https://github.com/mathorn1973/twist-j/issues/1653.

This proof concerns the explicitly declared finite action and transformation
family in `PREREG.md`. The parameter `epsilon` grades a deformation of that
action. It does not grade homogeneous degree in the fields, establish an
Einstein-Hilbert expansion, or identify an ADM gauge algebra. In particular,
an exact first-order cancellation below is distinguished from an exact
symmetry of the finite deformed action.

All calculations are algebraic over the rationals. The finite verifier
audits the identities and fixed counterexamples; the statements for arbitrary
finite horizon and arbitrary admitted rational data follow from the proofs.

## 1. Domain, operators, and the two parts of the action

Fix an integer horizon `T >= 5`. Vertex fields `h_n in Q^5` and scalar fields
`chi_n in Q` exist for `0 <= n <= T`. Their endpoint values are fixed under
variation. All interior field variations are independent. This is the
unrestricted off-shell field domain; it is not restricted to the prepared
unit-sum histories of the predecessor probes.

Use the five-vertex graph and ten oriented edges of the preregistration.
For `r in Z/5`, edge `e_r` runs from `r` to `r+1`, with weight `29/324`, and
edge `e_(5+r)` runs from `r` to `r+2`, with weight `65/324`. Put

    m = 324,  g = 1/m,  e = (1,1,1,1,1),
    ell = (1,-1,0,0,0),  sigma = (1/2,1/2,0,0,0),
    (B h)_edge = h(head edge) - h(tail edge),
    L = B^T W B,  L_int = m L,
    (L_int h)_r = 188 h_r - 29(h_(r-1)+h_(r+1))
                          - 65(h_(r-2)+h_(r+2)).

Vertex and edge inner products are their ordinary finite sums. The adjoint
`B^T` adds an edge value at its head and subtracts it at its tail. The graph
is connected, so `ker L = span(e)`, and `L` is invertible on `e^perp`. Write

    mean(v) = (sum_r v_r)/5,
    Pi_0 v = v - mean(v) e,
    K_E = ker B^T.

The bond variables for `1 <= b <= T` are `tau_b, lambda_b in e^perp` and
`alpha_b in Q`. The interior edge variables for `1 <= n < T` are
`p_n in K_E` and `N_n in Q^10`. The variables `tau` and `p` are independent
auxiliary coordinates in this action domain. In formulas involving adjacent
shifts, set `N_0 = N_T = 0`; these are boundary conventions, not additional
varied variables.

For a fixed source context `a`, put `A = a/4`. The undeformed field action is

    A_auto = (1/2) sum_(b=1)^T [ ||h_b-h_(b-1)||^2
                                + (chi_b-chi_(b-1))^2 ]
             - (1/2) sum_(n=1)^(T-1) [ <h_n,L h_n> + chi_n^2 ]
             + sum_(n=1)^(T-1) [ A chi_n + g chi_n <ell,h_n> ].       (1.1)

Its interior Euler derivatives are minus the residuals

    R_h,n = h_(n+1)-2 h_n+h_(n-1)+L h_n-g chi_n ell,
    R_chi,n = chi_(n+1)-chi_n+chi_(n-1)-A-g <ell,h_n>.             (1.2)

Let `e_loc,b`, `Htot_b`, and `j_n` be the local bond density, total bond
energy, and edge current defined in Section 2. The homogeneous reference
`E_hom` is fixed during all variations. Define

    S_0 = A_auto
          + 2 sum_(b=1)^T <lambda_b,L tau_b>
          + 2 sum_(n=1)^(T-1) <N_n,W B(tau_(n+1)-tau_n)+p_n>,

    S_int = -sum_(b=1)^T alpha_b (Htot_b-E_hom)
            -sum_(b=1)^T <lambda_b,e_loc,b>
            +sum_(n=1)^(T-1) <N_n,j_n>,

    S_epsilon = S_0 + epsilon S_int.                            (1.3)

Replacing `e_loc,b` by `e_tot,b` in its pairing with mean-zero `lambda_b`
has no effect. This exact finite action at `epsilon=1` has the chosen
constraint-coupling structure of the predecessor. The auxiliary terms of
`S_0` are bilinear; the force and equilibrium offsets can produce lower
field degrees in `S_int`. Accordingly, the order statements in this proof
are statements about `epsilon`, not an assertion that every added monomial
has homogeneous degree three in field amplitudes.

## 2. Exact local energy identity for arbitrary off-shell data

For a bond `b` between slices `b-1` and `b`, set

    e_h,b(r) = (h_b(r)-h_(b-1)(r))^2/2
               + (1/4) sum_(edge incident to r)
                    w_edge (B h_b)_edge (B h_(b-1))_edge,

    e_chi,b(r) = sigma_r [ (chi_b-chi_(b-1))^2/2
                           + chi_(b-1) chi_b/2
                           - A(chi_(b-1)+chi_b)/2 ],

    e_int,b(r) = -(g/2) ell_r [chi_(b-1) h_b(r)+chi_b h_(b-1)(r)],
    e_loc,b = e_h,b + e_chi,b + e_int,b,
    e_tot,b = e_loc,b + E_*/5,
    Htot_b = sum_r e_loc,b(r) + E_*.                            (2.1)

Here `E_*` is the fixed equilibrium offset declared in `PREREG.md`; it is
constant in space and time. Its value does not enter any identity below
except through the displayed constant offsets. The identities are valid
for every fixed value of `E_*`.

At each interior slice define

    q_h,n = h_(n+1)-h_(n-1),
    q_chi,n = chi_(n+1)-chi_(n-1),

    j_h,n(edge) = (w_edge/4)(B h_n)_edge
                    [q_h,n(tail edge)+q_h,n(head edge)],
    j_int,n(edge) = -(g/4) q_chi,n [h_n(0)+h_n(1)] delta_(edge,e_0),
    j_n = j_h,n + j_int,n.                                    (2.2)

### 2.1 Endpoint calculation

The kinetic difference at vertex `r` is

    [(h_(n+1)(r)-h_n(r))^2-(h_n(r)-h_(n-1)(r))^2]/2
      = q_h,n(r) [h_(n+1)(r)-2h_n(r)+h_(n-1)(r)]/2.

On one oriented edge `u -> v`, put `d=(B h_n)_edge`. The change in the
spatial energy share at either endpoint is
`(w_edge/4)d[q_h,n(v)-q_h,n(u)]`. Subtracting the edge current at the tail
and adding it at the head gives respectively

    -(w_edge/2) q_h,n(u) d,
    +(w_edge/2) q_h,n(v) d.

After summing incident edges, the field contribution is therefore

    Delta e_h,n + B^T j_h,n
      = (1/2) q_h,n * R_h,n + (g/2) chi_n ell * q_h,n.          (2.3)

The symbol `*` means pointwise multiplication of vertex vectors. Expanding
the scalar quadratic gives

    Delta e_chi,n
      = (1/2) sigma q_chi,n R_chi,n
         + (g/2) sigma q_chi,n <ell,h_n>.                     (2.4)

The interaction density difference is

    Delta e_int,n
      = -(g/2) ell [chi_n q_h,n + q_chi,n h_n].                (2.5)

The first transfer terms in (2.3) and (2.5) cancel. The remaining mismatch
is `(g/2)q_chi,n [sigma <ell,h_n>-ell*h_n]`. Its values at vertices zero
and one are minus and plus `(g/4)q_chi,n[h_n(0)+h_n(1)]`, respectively;
it vanishes at the other vertices. The current `j_int,n` in (2.2) has
precisely the opposite incidence divergence. Thus, without using equations
of motion or constraint equations,

    C_n := e_loc,n+1-e_loc,n+B^T j_n
         = e_tot,n+1-e_tot,n+B^T j_n
         = (1/2)[q_h,n * R_h,n + sigma q_chi,n R_chi,n].        (2.6)

This is an exact identity on arbitrary rational three-slice data. Summing
over vertices eliminates `B^T j_n`, giving the corresponding total energy
work identity. No pointwise positivity of `e_loc` or `e_tot` is required.

## 3. Full finite-horizon variations, including adjacent currents

The following are the derivatives of the global action (1.3), not only
the derivatives of a two-bond polynomial containing one shift current.

For bond `b`, put `mu_b=alpha_b e+lambda_b`. Up to terms independent of
the varied fields, its matter coupling is `-<mu_b,e_loc,b>`. For an
interior field slice `n`, its two adjacent bonds are `b=n,n+1`. Let
`(h_nb,chi_nb)` denote the other field endpoint on the bond in question.
Define

    U_b(edge) = (w_edge/4)[mu_b(tail edge)+mu_b(head edge)]
                           (B h_nb)_edge,

    F_h,b,n(r) = mu_b(r)[h_n(r)-h_nb(r)] + (B^T U_b)(r)
                 -(g/2) mu_b(r) ell_r chi_nb,

    F_chi,b,n = <sigma,mu_b>[chi_n-chi_nb/2-A/2]
                 -(g/2) sum_r mu_b(r) ell_r h_nb(r).          (3.1)

These are exactly the field derivatives of `<mu_b,e_loc,b>`.

The current at slice `n` gives the central contribution

    V_n(edge) = (w_edge/4) N_n(edge)
                    [q_h,n(tail edge)+q_h,n(head edge)],

    K_h,n^central(r) = (B^T V_n)(r)
                        -(g/2) q_chi,n N_n(e_0) sigma_r.     (3.2)

It has no derivative with respect to the central `chi_n`. But the
neighboring currents `j_(n-1)` and `j_(n+1)` also consume slice `n`, through
their time differences. Their contributions are

    K_h,n^adjacent(r)
      = (1/4) sum_(edge incident to r) w_edge
          [N_(n-1)(edge)(B h_(n-1))_edge
           -N_(n+1)(edge)(B h_(n+1))_edge],

    K_chi,n^adjacent
      = -(g/4) N_(n-1)(e_0)[h_(n-1)(0)+h_(n-1)(1)]
         +(g/4) N_(n+1)(e_0)[h_(n+1)(0)+h_(n+1)(1)].         (3.3)

The boundary convention `N_0=N_T=0` makes these formulas valid at the
first and last interior slices without adding currents outside the
declared horizon. Direct differentiation now gives

    grad_(h_n) S_epsilon
      = -R_h,n + epsilon[-F_h,n,n-F_h,n+1,n
                          +K_h,n^central+K_h,n^adjacent],

    d S_epsilon/d chi_n
      = -R_chi,n + epsilon[-F_chi,n,n-F_chi,n+1,n
                            +K_chi,n^adjacent].              (3.4)

For example, the plus occurrence of `h_n` in `q_h,n-1` accounts for the
first term in the unsigned endpoint sum (3.3), and its minus occurrence
in `q_h,n+1` accounts for the second. This explicitly prevents the omission
of neighboring shifts when the global action is varied.

The auxiliary and multiplier variations, in their declared spaces, are

    grad_(tau_b) S_epsilon
      = 2 L lambda_b + 2 B^T W(N_(b-1)-N_b)       in e^perp,

    d_p S_epsilon[delta p_n] = 2<N_n,delta p_n>   for delta p_n in K_E,

    grad_(lambda_b) S_epsilon
      = 2 L tau_b-epsilon Pi_0 e_loc,b           in e^perp,

    grad_(N_n) S_epsilon
      = 2 W B(tau_(n+1)-tau_n)+2p_n+epsilon j_n  in Q^10,

    d S_epsilon/d alpha_b = -epsilon(Htot_b-E_hom).           (3.5)

The restricted `p` equation is `proj_(K_E) N_n=0`, equivalently
`N_n in im B`. It is not the ambient equation `N_n=0`. Writing
`N_n=B xi_n`, with the unique mean-zero `xi_n`, the `tau` equation becomes

    lambda_b = xi_b-xi_(b-1),  xi_0=xi_T=0.                 (3.6)

No equation in (3.5) says that the homogeneous lapse must be zero.
The zero-multiplier configurations used by the predecessor are selected
stationary configurations when their field and constraint equations hold;
this does not prove that all stationary configurations have zero
multipliers or that they are related by an all-order gauge symmetry.

### 3.1 Exact adjacent-current witness

Take `T=5,a=0,E_hom=0` and set `h_1=(6,11,11,6,6)/40`, with all other
physical fields zero. This nonzero slice is the frozen initial slice of
the predecessor's `0011,a=0` example; no equation of motion is imposed on
the new off-shell array. Set `N_1=delta_(e_0)` and all other auxiliary
coordinates to zero. Relative to the same field array with `N=0`, the
global action gradient at slice two contains the change from `N_1 j_1`:

    d(N_1 j_1)/d h_2 = (29/10368,29/10368,0,0,0),
    d(N_1 j_1)/d chi_2 = -17/51840.                          (3.7)

Indeed, `(B h_1)_(e_0)=1/8`, so each endpoint contribution is
`(29/324)(1/8)/4=29/10368`; the scalar contribution is
`-(1/324)(17/40)/4=-17/51840`. A local action that retains only `N_2 j_2`
misses these terms when `N_2=0`.

### 3.2 Independent coordinates and exact coordinate differences

The four vectors `V_i=e_i-e_4`, `i=0,1,2,3`, form a basis of `e^perp`.
The six edge vectors `K_0,...,K_5` frozen in `PREREG.md` are closed cycles:
`K_0` is the five-edge nearest-neighbor cycle, while each remaining vector
closes one of the five longer edges by a nearest-neighbor path. Therefore
`B^T K_i=0`. The last five edge coordinates of `K_1,...,K_5` are the five
unit vectors, and those of `K_0` are zero. This proves independence.
Since `rank B=4` and there are ten edges, `dim K_E=6`; hence they are a
complete basis, not just selected test directions.

The independent global coordinate count is consequently

    6(T-1)+4T+6(T-1)+T+4T+10(T-1)=31T-22.                  (3.8)

For `T=5` it is 133. A derivative in a `tau` or `lambda` coordinate is the
pairing of its ambient gradient in (3.5) with the corresponding `V_i`;
a derivative in a `p` coordinate is `2<N_n,K_i>`. These are admissible
variations in the declared subspaces.

Every individual such coordinate has polynomial action degree at most two.
Thus its centered unit difference equals its derivative exactly. This
proves the coordinate-difference method used for the 798 comparisons
over the six frozen configurations. It does not apply to joint field and
multiplier directions of degree three; those are treated in Section 7.1.

## 4. Constraint propagation as a residual identity

Define the declared inhomogeneous constraint residuals

    H_b^epsilon = 2 L tau_b-epsilon Pi_0 e_loc,b,
    M_n^epsilon = 2 W B(tau_(n+1)-tau_n)+2p_n+epsilon j_n.

Using only `B^T W B=L` and `Pi_0 B^T=B^T`, one obtains the exact identity

    H_n+1^epsilon-H_n^epsilon
      = B^T M_n^epsilon-2 B^T p_n-epsilon Pi_0 C_n.           (4.1)

For the declared domain `p_n in K_E`, the middle term vanishes. If the
inherited residuals `R_h,n,R_chi,n` vanish and the momentum constraint
`M_n^epsilon=0` is satisfied, (2.6) and (4.1) propagate `H^epsilon=0`
from one bond to the next. This is a genuine compatibility and propagation
statement for these declared constraints.

It must not be confused with substituting the full deformed field Euler
derivatives for `-R_h,-R_chi` in (2.6). Equation (3.4) displays their
additional multiplier-dependent terms. Nor does (4.1) identify the
constraints with ADM constraints or prove a first-class Poisson algebra.

## 5. The exact first-order off-shell Noether identity

Let the vertex parameter `psi_n in Q^5` be arbitrary for `1 <= n < T`,
with `psi_0=psi_T=0`. No spatial mean condition is imposed on `psi`.
For bonds set `Delta psi_b=psi_b-psi_(b-1)`. Define the field-independent
auxiliary variation

    delta_0 N_n = B psi_n,
    delta_0 lambda_b = Pi_0 Delta psi_b,
    delta_0 alpha_b = mean(Delta psi_b),
    delta_0 tau_b = delta_0 p_n = delta_0 h_n = delta_0 chi_n = 0.          (5.1)

The first field variation is

    delta_1 h_n = (1/2) psi_n * q_h,n,
    delta_1 chi_n = (1/2)<sigma,psi_n> q_chi,n,                (5.2)

with zero endpoint field variations and with all auxiliary and multiplier
variations under `delta_1` equal to zero. In particular, both variations
preserve the stated `tau`, `lambda`, and `p` linear spaces.

### 5.1 Zeroth-order identity

Only the auxiliary terms of `S_0` change under `delta_0`. The two `tau`
contributions are

    2 sum_b <Delta psi_b,L tau_b>
      + 2 sum_n <psi_n,L(tau_(n+1)-tau_n)> = 0,

by finite summation by parts and `psi_0=psi_T=0`. The remaining term is
`2 sum_n <psi_n,B^T p_n>=0` because `p_n in K_E`. Consequently

    delta_0 S_0 = 0.                                         (5.3)

This requires the restricted `p` domain; replacing it by unrestricted edge
momenta would leave the explicitly displayed `2 sum psi_n B^T p_n` term.

### 5.2 First-order cancellation

Since `Htot_b=sum_r e_loc,b(r)+E_*`, the homogeneous and inhomogeneous lapse
variations combine exactly:

    -mean(Delta psi_b)(Htot_b-E_hom)
      -<Pi_0 Delta psi_b,e_loc,b>
      = -<Delta psi_b,e_loc,b>
         +mean(Delta psi_b)(E_hom-E_*).

The last term sums to zero because both offsets are fixed and
`sum_b Delta psi_b=0`. Adding the shift variation and summing by parts gives

    delta_0 S_int
      = sum_(n=1)^(T-1) <psi_n,e_loc,n+1-e_loc,n+B^T j_n>
      = (1/2) sum_n [<psi_n*q_h,n,R_h,n>
                     +<sigma,psi_n> q_chi,n R_chi,n].          (5.4)

The auxiliary part of `S_0` is independent of `h,chi`, so (1.2) gives

    delta_1 S_0 = delta_1 A_auto
      = -(1/2) sum_n [<psi_n*q_h,n,R_h,n>
                      +<sigma,psi_n> q_chi,n R_chi,n].         (5.5)

Thus on the full admitted off-shell domain,

    delta_0 S_int + delta_1 S_0 = 0.                          (5.6)

For `delta=delta_0+epsilon delta_1` and `S_epsilon=S_0+epsilon S_int`,
expanding the directional derivative yields the exact finite identity

    delta S_epsilon = epsilon^2 U,
    U := delta_1 S_int.                                      (5.7)

There is no omitted remainder in (5.7). The nonzero quantity `U` is exactly
what prevents promoting the first-order cancellation to a general exact
symmetry of this finite action.

## 6. Pure auxiliary gauge values and the field-redefinition identity

Set the multipliers equal to the values generated from zero by (5.1):

    alpha_b=mean(Delta psi_b),
    lambda_b=Pi_0 Delta psi_b,
    N_n=B psi_n.                                             (6.1)

For any admitted `tau,p`, the auxiliary part of `S_0` is then zero by the
same calculation as (5.3). Equation (5.4), now evaluated as the value of
`S_int` rather than a derivative, says

    S_int = sum_n [<R_h,n,delta_1 h_n>
                    +R_chi,n delta_1 chi_n].                 (6.2)

Let `x=(h,chi)` and `y=G_psi x=(delta_1 h,delta_1 chi)`, with fixed zero
endpoint increments. Because `A_auto` is a quadratic-affine polynomial,
its Taylor formula is exact:

    A_auto(x-epsilon y)
      = A_auto(x)+epsilon S_int
         +(epsilon^2/2) Hess_(A_auto)[y,y].                   (6.3)

For clarity, the constant Hessian quadratic form is

    Hess_(A_auto)[(u,v),(u,v)]
      = sum_b [||u_b-u_(b-1)||^2+(v_b-v_(b-1))^2]
        -sum_n [<u_n,L u_n>+v_n^2]
        +2g sum_n v_n<ell,u_n>,                              (6.4)

with zero endpoint increments. The force term contributes no Hessian.
Equation (6.3) proves a first-order field-redefinition interpretation of
the pure-gauge coupling. It does not discard the quadratic remainder,
claim invertibility of `x -> x-epsilon G_psi x` for every finite parameter,
or equate a tangent displacement with an integrated gauge flow.

## 7. Symbolic nonzero remainder and central-difference counterexample

Use `T=5`, `a=0`, `E_hom=0`, and denote the first vertex unit vector by
`u=(1,0,0,0,0)`. Set

    h_3=u; all other h_n=0; all chi_n=0,
    psi_2=psi_3=u; all other psi_n=0,
    alpha_3=1; all other multipliers, tau, and p are zero.       (7.1)

The field tangent `y=G_psi x` has exactly one nonzero entry,
`y_h,2=u/2`. All its scalar entries vanish. Since
`<u,L u>=188/324=47/81`, the derivative of the third bond energy is

    delta_1 Htot_3
      = <-u+(1/2)L u,u/2>
      = -1/2+(1/4)(188/324)
      = -115/324.

Only `-alpha_3 Htot_3` contributes to `delta_1 S_int`, giving

    U = 115/324 != 0.                                        (7.2)

Hence the finite action at `epsilon=1` is not invariant under the
declared direction, although its zeroth- and first-order cancellations
hold exactly.

### 7.1 A unit central difference along the joint direction is not a derivative

Freeze the direction `delta_0+delta_1` at (7.1) and evaluate the action
along the straight line with scalar parameter `t`. The action on this
line has degree at most three. Its cubic coefficient comes from the
multiplier tangent paired with the quadratic field tangent in `S_int`.
For the tangent field `y`, its only relevant inherited residual is
`R_h,3(y)=u/2`, while `(G_psi y)_3=-u/4`. Thus (6.2), applied to the
homogeneous quadratic part, gives the cubic coefficient

    c_3 = <u/2,-u/4> = -1/8.                                 (7.3)

For any cubic polynomial `P(t)=c_0+c_1 t+c_2 t^2+c_3 t^3`,

    [P(1)-P(-1)]/2 = P'(0)+c_3.

Therefore the unit central difference in this witness equals `149/648`,
whereas the exact derivative is `115/324`. Their difference is

    unit_central_difference - exact_derivative = -1/8.         (7.4)

This is why exact coordinatewise central differences for a polynomial
of degree at most two in each separate coordinate do not justify using
the same two-point rule along a direction that varies fields and
multipliers simultaneously. An exact cubic directional derivative can
instead be recovered from the four values at `t=-2,-1,1,2`:

    P'(0) = [-P(2)+8P(1)-8P(-1)+P(-2)]/12.                  (7.5)

### 7.2 Exact field-redefinition remainder

Keep the field and parameter data in (7.1), but replace the original
`alpha_3=1` multiplier configuration by the pure-gauge values (6.1).
Then `S_int=<R_h,2,y_h,2>=1/2`, and

    A_auto(x) = 1-(1/2)(188/324) = 115/162,
    (1/2) Hess_(A_auto)[y,y] = 1/4-(1/8)(188/324) = 115/648.

The shifted field `x-y` has `h_2=-u/2`, `h_3=u`, all other entries zero,
so `A_auto(x-y)=899/648`. Equation (6.3) therefore has the explicit
nonzero finite remainder

    S_1(x; pure-gauge multipliers)-A_auto(x-G_psi x)
      = -115/648.                                           (7.6)

### 7.3 Further structural negative controls

The same field and parameter data as (7.1) give
`delta_0 S_int=1/2` and `delta_1 S_0=-1/2`, because their sole field
pairing is `<R_h,2,y_h,2>=<u,u/2>`. Reversing the relative completion
sign therefore gives

    delta_0 S_int-delta_1 S_0=1.                             (7.7)

For the homogeneous lapse omission on these data,
`mean(Delta psi_2)=1/5`, `mean(Delta psi_4)=-1/5`, and the other mean
increments vanish. The second and fourth bond energies are respectively
zero and `1/2`. The homogeneous contribution to `delta_0 S_int` is
therefore `-(1/5)0-(-1/5)(1/2)=1/10`. Deleting that contribution while
keeping the other variations leaves the first-order defect

    defect_without_delta_alpha=-1/10.                       (7.8)

For the interaction-current omission use the separate frozen data
`T=5,a=0,E_hom=0,h_2=u,chi_3=1,psi_2=u`, with all other fields,
parameters and auxiliaries zero. At slice two,
`j_int,2(e_0)=-1/1296` and `(B psi_2)_(e_0)=-1`.
Their pairing contributes `1/1296` to `delta_0 S_int`. Removing this
current but retaining the same physical action leaves

    defect_without_j_int=-1/1296.                           (7.9)

Finally, set only `p_2=delta_(e_0)` and `psi_2=u` nonzero. This momentum
is intentionally outside `K_E`. Its incidence divergence pairs with
`u` to give `-1`, so the uncancelled term identified in Section 5.1 is

    delta_0 S_0=2<psi_2,B^T p_2>=-2.                       (7.10)

This last witness tests the necessity of the domain condition; it is not
an admitted-domain counterexample to (5.3). Together with the neighbor,
remainder, differentiation, field-redefinition, commutator, and mean
witnesses, these are the ten independently specified negative controls.

## 8. Exact commutator and failure of closure in the declared family

Parameters are fixed functions of the time label, not varied fields.
For the Lie-derivative convention

    [delta_psi,delta_eta] x
      = delta_psi(delta_eta x)-delta_eta(delta_psi x)
      = G_eta G_psi x-G_psi G_eta x,

apply (5.2) twice. For any interior slice whose displayed neighbors are
within the horizon, the field component is

    [delta_psi,delta_eta] h_n
      = (1/4)[eta_n*psi_(n+1)-psi_n*eta_(n+1)]*h_(n+2)
        +(1/4)[eta_n*psi_(n-1)-psi_n*eta_(n-1)]*h_(n-2)
        -(1/4)[eta_n*(psi_(n+1)+psi_(n-1))
                -psi_n*(eta_(n+1)+eta_(n-1))]*h_n.            (8.1)

At horizon boundaries, the same calculation uses the fixed zero endpoint
tangent rather than introducing exterior fields. The scalar expression
has the identical three-coefficient form with `h` replaced by `chi` and
the parameter vectors replaced by the scalar values
`s_psi,n=<sigma,psi_n>`, `s_eta,n=<sigma,eta_n>`.

These formulas contain time displacements of two. A decisive counterexample
does not require guessing a possible new parameter. Take `T=5`, set

    psi_2=ell, eta_3=ell; all other parameter values zero,
    h_n=e/5 for all n except h_4=e/5+ell,
    chi_n=0 for all n.                                      (8.2)

Both parameter profiles are spatially mean zero, and all field slices in
this witness have spatial sum one. At slice two, (8.1) yields

    [delta_psi,delta_eta] h_2
      =(1/4)(ell*ell)*(h_2-h_4)=-ell/4 != 0.                 (8.3)

But `h_3-h_1=0`, so every transformation of the originally declared
nearest-time family, with any finite parameter `zeta_2`, gives

    delta_zeta h_2=(1/2)zeta_2*(h_3-h_1)=0.                 (8.4)

Equations (8.3)-(8.4) prove nonclosure within that family, even if one
attempts to select `zeta` using the field data. They do not exclude a
larger family with additional generators, wider stencils, additional
fields, or higher deformation terms.

### 8.1 The fixed-mean subspace is not preserved

In the same witness, `q_h,3=h_4-h_2=ell`. The single `eta` transformation
therefore gives

    delta_eta h_3=(1/2)ell*ell=(1/2,1/2,0,0,0),
    sum_r delta_eta h_3(r)=1.                                (8.5)

Thus the transformation is defined on the unrestricted off-shell carrier,
but does not in general preserve the unit-sum prepared sector. In
particular, this proof does not claim a symmetry acting inside the
predecessor's prepared Lorentz family. The scalar transformation in
(8.2) vanishes because `<sigma,ell>=0`.

## 9. Integer lift of continuity, the Noether pairing, and the tangent displacement

Assume all field slices on the finite horizon have a common positive
integer denominator `D`:

    h_n=P_n/D,  chi_n=Y_n/D,
    P_n in Z^5,  Y_n in Z.

This is a simultaneous finite-history encoding. Unlike the predecessor's
evolving-denominator representation, the same `D` is used at every slice
in the formulas of this section. Define

    Q_h,n=P_(n+1)-P_(n-1),
    Q_chi,n=Y_(n+1)-Y_(n-1),

    A_h,n=m(P_(n+1)-2P_n+P_(n-1))+L_int P_n-Y_n ell,
    A_chi,n=m(Y_(n+1)-Y_n+Y_(n-1))-81 a D-<ell,P_n>.

For the declared integer source contexts, these are integers, and
`R_h,n=A_h,n/(mD)`, `R_chi,n=A_chi,n/(mD)`.

### 9.1 Energy and current integer records

Multiplying the density (2.1) by `4mD^2` gives the integer vector

    E_int,b(r)
      = 2m(P_b(r)-P_(b-1)(r))^2
        +sum_(edge incident to r) (m w_edge)
                      (B P_b)_edge (B P_(b-1))_edge
        +(2 sigma_r)[m(Y_b-Y_(b-1))^2+mY_(b-1)Y_b
                       -81 a D(Y_(b-1)+Y_b)]
        -2 ell_r[Y_(b-1)P_b(r)+Y_b P_(b-1)(r)].               (9.1)

The integer current on the same common scale is

    J_int,n(edge)
      = (m w_edge)(B P_n)_edge
                        [Q_h,n(tail edge)+Q_h,n(head edge)]
        -Q_chi,n[P_n(0)+P_n(1)]delta_(edge,e_0).               (9.2)

Here `E_int=4mD^2 e_loc` and `J_int=4mD^2 j`. In particular, no additional
factor of `m` is inserted into the current scale when all time slices use
this common `D`. The differing current scale in the predecessor followed
from its differing denominators at adjacent time slices.

Multiplying (2.6) by `4mD^2` proves on arbitrary integer data

    C_int,n := E_int,n+1-E_int,n+B^T J_int,n
       = 2 Q_h,n * A_h,n + (2 sigma) Q_chi,n A_chi,n.          (9.3)

All vectors in this equality are integral because `m w_edge` is 29 or 65
and `2 sigma=(1,1,0,0,0)`.

### 9.2 Integer form of the first-order cancellation

Write the parameter with a positive common integer denominator
`Q_psi` as `psi_n=V_n/Q_psi`, where `V_0=V_T=0`. Multiplying (5.4) and
(5.5) by the same integer scale `4mD^2Q_psi` gives

    (4mD^2Q_psi) delta_0 S_int = sum_n <V_n,C_int,n>,

    (4mD^2Q_psi) delta_1 S_0
      = -sum_n [2<V_n*Q_h,n,A_h,n>
                 +(V_n(0)+V_n(1))Q_chi,n A_chi,n].           (9.4)

Their sum is exactly zero by (9.3). The constant `E_hom` and equilibrium
offset cancel in the finite sum before (9.4), as proved in Section 5;
no false claim that each separate uncancelled offset has this denominator
is needed.

### 9.3 Exact integer encoding of a tangent displacement

Suppose also that all auxiliary and multiplier coordinates are encoded
over the same `D`. Use integer numerators `T_b,K_n,A_b,Lambda_b,Ncal_n`
for `tau_b,p_n,alpha_b,lambda_b,N_n`, respectively. Their admissibility
conditions are `sum T_b=sum Lambda_b=0` and `B^T K_n=0`.

For any integer `epsilon`, the straight tangent displacement
`delta_0+epsilon delta_1` has the common output denominator

    D' = 20 D Q_psi.                                         (9.5)

Every original numerator is first multiplied by `20Q_psi`; add the
following integer increments:

    P'_n:       10 epsilon V_n * Q_h,n,
    Y'_n:        5 epsilon [V_n(0)+V_n(1)] Q_chi,n,
    A'_b:        4 D sum_r (V_b(r)-V_(b-1)(r)),
    Lambda'_b:   4 D [5(V_b-V_(b-1))
                       -sum_r(V_b(r)-V_(b-1)(r)) e],
    Ncal'_n:    20 D B V_n,
    T'_b:        0,
    K'_n:        0.                                          (9.6)

Endpoint field increments are zero. Dividing (9.6) by (9.5) recovers
exactly (5.1) and `epsilon` times (5.2). The sums of the lapse and potential
numerators remain zero, and the co-closure of the momentum numerators is
preserved. No roundoff, denominator reduction, or root extraction occurs.

This is an exact integer representation of a finite tangent displacement.
It is not asserted to be the finite flow of a gauge group, a bijection,
a norm-preserving map, a banked update, or a minimal-denominator encoding.
The nonclosure and mean-escape witnesses apply equally after this exact
change of representation.

## 10. Scope of the combined result

The action admits the exact zeroth-order auxiliary identity (5.3), the
exact first-order off-shell cancellation (5.6), and the exact residual
(5.7). The global variation includes the adjacent-current terms (3.3).
The auxiliary constraint propagation identity (4.1) and all integer
identities in Section 9 hold on their stated domains.

The same construction supplies explicit limits: the finite action
variation has the nonzero residual (7.2), the pure-gauge field
redefinition has the nonzero remainder (7.6), the nearest-time generator
family fails closure by (8.3)-(8.4), and it fails to preserve the unit-sum
subspace by (8.5). These are scoped results about the frozen action and
generator family. They do not establish or rule out a more complete
nonlinear integer gravitational theory.
