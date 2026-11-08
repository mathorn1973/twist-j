# Local auxiliary completion through second order

Status: PROSPECTIVE analytical proof.

Scope: NON-CANONICAL, NEW_DECLARED L1, conditional candidate-T, `a=0` only.

No completed execution or public promotion is asserted in this document.

The objects, domains, boundary conventions, and proposed formulas are those
of `PREREG.md`. All identities below are exact identities in their specified
coefficients. The formal parameter `epsilon` records order; it is not a
numerical tolerance. The proof applies for every `T>=3` and every rational
endpoint pair. Endpoints are held fixed during variations. It neither
restricts histories to solutions of the equations of motion nor divides by
an equation-of-motion residual.

## 1. Spatial operators and constrained carriers

For the connected five-vertex graph with strictly positive rational edge
weights, `L=B^T W B` is symmetric, `Le=0`, and

    v^T L v = sum_edge w_edge (Bv)_edge^2.

Its kernel is exactly `span(e)`: zero quadratic form forces equal values
across every edge and hence at every vertex. Thus `L+ee^T/5` is invertible
and the defined rational matrix

    Lplus=(L+ee^T/5)^(-1)-ee^T/5

is symmetric and satisfies

    L Lplus=Lplus L=Pi0, Lplus e=0.                     (1)

These facts follow by splitting the vertex space into `span(e)` and
`e^perp`; the two summands are invariant under both matrices.

For the weighted decomposition

    Z=Lplus B^T W N, Q=N-BZ,
    P=I-WB Lplus B^T,

the identity `B^T W N in e^perp` gives

    B^T W Q=0, B^T P=0, P^2=P, P^T Q=Q.              (2)

For example, `B^T W Q=B^T W N-L Lplus B^T W N=0`.
Likewise `B^T P=B^T-Pi0 B^T=0`; if `B^T v=0`, then `Pv=v`.
Consequently `P` projects onto `ker B^T`. It is not asserted to be the
Euclidean orthogonal projector. The multiplier `Q` belongs to
`ker(B^T W)`, which is a different declared subspace. The last identity
in (2) follows from `P^T Q=Q-B Lplus B^T W Q`.

Every inverse in this section is a fixed five-site spatial inverse.
None depends on the temporal horizon. All subsequent applications preserve
rationality.

## 2. Field gradient, density, and lower-order identities

The matrix `C=I_6-V/2` is symmetric. Discrete summation by parts in `A`,
with endpoint-zero field variations, gives

    D A(x)[v]=sum_(n=1)^(T-1) f_n dot v_n,
    f_n=2C x_n-x_(n-1)-x_(n+1)=-R_n.                  (3)

This expression includes the fixed endpoint values in the neighboring
residuals. The convention `f_0=f_T=0` is used only when a matrix acts on
interior tangents; it imposes no equation on either endpoint.

Summing the vertex density counts each edge potential term twice and uses
`sum_r sigma_r=1`. Substituting the block matrix `V` then yields

    H_b=sum_r e_b(r)
       = (||x_b||^2+||x_(b-1)||^2)/2-x_(b-1)^T C x_b.  (4)

We next derive the off-shell local continuity identity needed below:

    e_(n+1)-e_n+B^T j_n
       = [q_h,n * R_h,n + sigma q_chi,n R_chi,n]/2.     (5)

The kinetic-density difference at vertex `r` is
`q_h,n(r)(h_(n+1)(r)-2h_n(r)+h_(n-1)(r))/2`.
For an edge with difference `d=(Bh_n)_edge`, the edge-potential
contribution to this density difference is
`w_edge d (Bq_h,n)_edge/4` at each endpoint. Adding the divergence of
`j_h` gives `w_edge d q_h,n(head)/2` at the head and
`-w_edge d q_h,n(tail)/2` at the tail. Summing incident edges supplies
`q_h,n(r)(Lh_n)(r)/2`.

The scalar-density difference equals

    (sigma/2) q_chi,n
                (chi_(n+1)-chi_n+chi_(n-1)).

The interaction-density difference at vertex `r` is

    -(g/2)ell_r[chi_n q_h,n(r)+q_chi,n h_n(r)].

Only edge `0`, oriented from vertex `0` to vertex `1`, contributes to
the interaction current. Its divergence adds
`+(g/4)q_chi,n(h_n(0)+h_n(1))` at vertex `0` and its negative at vertex
`1`. Together with the second term in the preceding display, this is
`-(g/2)sigma_r q_chi,n <ell,h_n>` at both affected vertices and zero
elsewhere. These contributions are exactly (5), with the declared
reciprocal-coupling residuals. No on-shell substitution was made.

For an arbitrary endpoint-zero parameter `psi`, summation by parts now
gives

    I(x,Gamma(psi))
      =sum_(n=1)^(T-1) psi_n dot (e_(n+1)-e_n+B^T j_n)
      =sum_n R_n dot (G_psi x)_n
      =-D A(x)[G_psi x].                              (6)

In the first equality the homogeneous and mean-zero bond terms combine
because `mean(Delta psi)e+Pi0(Delta psi)=Delta psi`. The endpoint
condition removes boundary terms.

The same summation by parts shows `Baux(Gamma(psi);tau,p)=0`. The terms
containing `L tau` cancel the corresponding `WB Delta tau` terms,
and `(B psi)^T p=psi^T B^T p=0`. Since `A` is multiplier-independent,

    delta0 S0=0, delta0 I+delta1 S0=0.                 (7)

## 3. A local scalar-lapse identity

Let `t_0=t_T=0` be any scalar parameter and set `U=G_(te)x`.
Since `sigma dot e=1`, this operator acts on all six coordinates as

    U_n=t_n(x_(n+1)-x_(n-1))/2.

At each interior slice introduce the two neighboring link momenta and
the two energy derivatives

    pL=Cx_n-x_(n-1),        pR=x_(n+1)-Cx_n,
    vL=x_n-Cx_(n-1),        vR=x_n-Cx_(n+1).            (8)

These are algebraic definitions, not additional state variables. They
satisfy

    f_n=pL-pR, U_n=t_n(pL+pR)/2,
    D_(x_n) H_n=vL, D_(x_n) H_(n+1)=vR,
    K_n=pL dot vL, K_(n+1)=-pR dot vR.                (9)

Let `Ihom=-sum_b alpha_b H_b` and let `d_t=Xhom` be the proposed
homogeneous second-order field variation. Direct differentiation gives

    D Ihom[U]
       =-sum_n (t_n/2)(alpha_n vL+alpha_(n+1) vR)
                                      dot (pL+pR),
    D A[d_t]
       = sum_n (t_n/2)(pL-pR)
                          dot (alpha_(n+1)vR-alpha_n vL).

Adding and using (9) yields

    D Ihom[U]+D A[d_t]
       =sum_n t_n[-alpha_n K_n+alpha_(n+1) K_(n+1)].   (10)

Under `delta0 alpha_b=t_b-t_(b-1)`, the derivative of
`S2hom=sum_b alpha_b^2 K_b/2` is

    delta0 S2hom
       =sum_b alpha_b(t_b-t_(b-1))K_b
       =sum_n t_n[alpha_n K_n-alpha_(n+1)K_(n+1)].     (11)

Equations (10)-(11) prove the off-shell scalar identity

    delta0 S2hom+D Ihom[G_(te)x]+D A[Xhom]=0.          (12)

It is valid with arbitrary fixed rational endpoints, because all field
variations and the parameter vanish there. The lower-order scalar
identity is the uniform-parameter case of (6). Thus the scalar-lapse
action `A+epsilon Ihom+epsilon^2 S2hom` has vanishing variation
coefficients through order two with the displayed scalar transformations.
This statement invokes no all-order generating function.

## 4. Weighted multiplier decomposition

Define `Z_0=Z_T=0` and `l_b=lambda_b-Z_b+Z_(b-1)` as in the contract.
At interior slices, (1) gives

    delta0 Z_n=Pi0 psi_n,
    delta0 Q_n=0, delta0 l_b=0.                       (13)

These relations also hold at the boundaries under the endpoint-zero
parameter convention. The spatial mean of `Z_n` is zero, so the
multiplier decomposition is exactly

    M=(alpha,l,Q)+Gamma(Z).                           (14)

In `Baux`, the pure-gauge contribution in (14) vanishes by Section 2.
The remaining term `Q_n^T WB(tau_(n+1)-tau_n)` vanishes by (2).
Therefore

    Baux=2sum_b l_b^T L tau_b+2sum_n Q_n^T p_n.        (15)

Equations (6) and (14), together with the multiplier linearity of `I`,
also give

    I(x,M)=Ires(x,M)-D A(x)[G_Zx].                    (16)

The notation `Ires(x,M)` here means exactly the declared evaluation
`I(x;(alpha,l,Q))`, with `l,Q` calculated from `M` and held fixed in
the indicated field derivative.

## 5. Formal pullback and the raw full Ward identity

Write `w=G_Zx`. Introduce the following formal expressions only for the
purpose of deriving coefficients:

    y=x-epsilon w,
    tauhat_b=tau_b-(epsilon/2)Lplus Pi0 e_b(y),
    phat_n=p_n+(epsilon/2)P j_n(y).                    (17)

They respect the fixed endpoints and the auxiliary carrier constraints.
No inverse of `x -> y` is used. In these expressions consider

    F=A(y)-epsilon sum_b alpha_b H_b(y)
       +epsilon^2 S2hom(y,alpha)
       +2sum_b l_b^T L tauhat_b+2sum_n Q_n^T phat_n.  (18)

By (1)-(2), the auxiliary terms become
`Baux+epsilon[-sum l_b^T e_b(y)+sum Q_n^T j_n(y)]`.
Consequently (18) is exactly

    A(y)+Baux+epsilon Ires(y,M)+epsilon^2 S2hom(y,alpha).

Because `A` is quadratic and `Ires` is quadratic in the physical fields,
its expansion through order two, using (16), is

    F=S0+epsilon I+epsilon^2
           [-D_x Ires[w]+Hess_A(w,w)/2+S2hom]+O(epsilon^3).
                                                               (19)

The coefficient in square brackets is precisely the proposed `S2`.
The notation `O(epsilon^3)` means terms of formal degree at least three,
not a bound for a numerical error.

Let `Dpsi_raw=delta0+epsilon delta1+epsilon^2 delta2_raw`, and set
`psi_perp=psi-t e`, where `t=mean psi`. Apply it to (17). Since
`delta0 Z=psi_perp` and `delta1 Z=delta2 Z=0`, the stated `Xraw` gives

    Dpsi_raw y
       =epsilon G_(te)x
          +epsilon^2[Xhom-G_(te)G_Zx]+O(epsilon^3)
       =epsilon G_(te)y+epsilon^2 Xhom(y,alpha)
          +O(epsilon^3).                             (20)

At the same time `Dpsi_raw alpha=Delta t` and `Dpsi_raw l=Dpsi_raw Q=0`.
For the other two formal variables, the ordinary chain rule and the
leading term of (20) give

    Dpsi_raw tauhat_b
       =epsilon^2[F_b-Lplus Pi0 D e_b[G_(te)x]/2]
          +O(epsilon^3)=O(epsilon^3),
    Dpsi_raw phat_n
       =epsilon^2[J_n+P D j_n[G_(te)x]/2]
          +O(epsilon^3)=O(epsilon^3).                 (21)

The identities are valid for arbitrary `tau,p,M,x`; no auxiliary equation
of motion has been used. In particular, `F` is mean zero and `B^T J=0`
by (1)-(2), so these are genuine tangent directions of the unchanged
carrier.

The scalar identities in Sections 2-3, applied to (18)-(21), show that
`Dpsi_raw F` has no coefficient of degree zero, one, or two. Applying
the same transformation to (19) cannot lower the formal degree of its
remainder: all transformation coefficients have nonnegative powers of
`epsilon`. Equating the second-order coefficient therefore proves

    delta0 S2+delta1 I+delta2_raw S0=0.                (22)

This is a proof of an exact coefficient identity. It does not require
convergence of a power series, invertibility at finite `epsilon`, or a
selected solution of any field equation.

## 6. The skew correction preserves the Ward identity

Let `A_t(alpha)` be the specified skew matrix on the interior time
coordinates, acting by scalar multiples of the identity on each six-vector.
Its transpose is `-A_t`, including at the two ends of the interior interval.
For `f=DA`, symmetry of the scalar inner product gives

    D A[A_t f]=f^T A_t f=0.                            (23)

The correction changes only the physical-field component of `delta2`.
The auxiliary part of `S0` is independent of that component. Adding
`A_t f` to `Xraw` thus leaves (22) unchanged and proves

    delta0 S2+delta1 I+delta2_adj S0=0.                (24)

The endpoint rows of the correction vanish. In the row formula, assigning
zero endpoint values to `f` implements exactly this restriction, not an
additional equation on the fields.

## 7. Raw commutator and reduction to scalar means

We use the contract's vector-field convention: applying the commutator to
the coordinate function `x` gives
`D(Deta x)[Dpsi]-D(Dpsi x)[Deta]`.
Its zeroth- and first-order coefficients vanish: `delta0` is a constant
multiplier translation, and `G_psi x` is multiplier-independent.

The auxiliary second-order components vanish as well. Their first-order
components are zero; `F` and `J` depend only on `x` and the fixed parameter;
and `delta0 x=0`. The multipliers have no higher-order components and their
zeroth-order components are constant. Hence only the field coefficient
in equation (5) of the contract remains.

Let `t=mean psi`, `s=mean eta`. Differentiating the two terms of `Xraw`
that contain `Z`, using (13), gives

    D_M Xraw_eta[Gamma(psi)]
       =G_(psi-te)G_eta x-G_(se)G_(psi-te)x
          +D_alpha Xhom_s[Delta t].                  (25)

Subtract the expression with the parameters exchanged and add the bare
term `G_eta G_psi x-G_psi G_eta x`. Expanding
`G_(psi-te)=G_psi-G_(te)` and its counterpart for `eta` cancels every
nonuniform contribution. The result is

    (G_(se)G_(te)-G_(te)G_(se))x
       +D_alpha Xhom_s[Delta t]
       -D_alpha Xhom_t[Delta s].                      (26)

This cancellation is algebraic on the full state space; it does not
require `Z=0` or pure uniform parameters.

For each interior `n`, put

    kplus_n=s_n t_(n+1)-t_n s_(n+1),
    kminus_n=s_n t_(n-1)-t_n s_(n-1).

The bare part in (26) is

    [kplus_n(x_(n+2)-x_n)
      +kminus_n(x_(n-2)-x_n)]/4,                     (27)

with boundary contributions omitted when the intermediate tangent is an
endpoint. Differentiating `Xhom` with respect to the bond scalars gives
the other part

    [kplus_n(x_n-Cx_(n+1))
      +kminus_n(x_n-Cx_(n-1))]/2.                    (28)

Combining (27)-(28) proves the raw coefficient formula

    Craw_n=[kplus_n R_(n+1)+kminus_n R_(n-1)]/4.       (29)

At `n=1` the coefficient `kminus_n` vanishes because `t_0=s_0=0`;
at `n=T-1` the coefficient `kplus_n` vanishes for the same reason.
Thus no endpoint residual or out-of-range field value is used in (29).

In terms of `f=-R`, (29) is `Craw=B_(t,s) f`, where the upper neighboring
block of `B_(t,s)` is `-kplus_n I_6/4`. The lower block is its negative
transpose, since `kminus_(n+1)=-kplus_n`. Therefore

    f dot Craw=0,                                    (30)

and the raw coefficient vanishes when the autonomous field equations
hold. Equation (30) is a trivial variational symmetry generated by an
antisymmetric multiple of the Euler gradient. It does not assert that
`Craw` is zero off shell.

## 8. Adjusted commutator and the explicit counterexample

At order two, the skew correction adds only

    [delta0_psi A_s-delta0_eta A_t]f                  (31)

to the field commutator, because `delta0 f=0`. Its upper neighboring entry
is

    [(t_(n+1)-t_n)(s_n+s_(n+1))
       -(s_(n+1)-s_n)(t_n+t_(n+1))]/8
       = kplus_n/4.                                 (32)

The lower entry is its negative. Thus the matrix in (31) is exactly
`-B_(t,s)` and cancels (29). Together with the other component calculations
in Section 7 this proves

    [Dpsi_adj,Deta_adj]_(degrees 0,1,2)=0             (33)

off shell for every admitted state and arbitrary endpoint-zero parameters.
No gauge-parameter composition law is being inferred beyond these
coefficients.

For the fixed witness set `T=4`, let
`u=(1,0,-1,0,0,0)`, set `x_3=u` and all other field slices to zero, and
take `M=tau=p=0`. Choose `t_1=1`, `s_2=1`, all other entries zero.
Then `R_2=u`, `R_1=0`, and the only relevant nonzero parameter products
are `kplus_1=-1` and `kminus_2=1`. Equation (29) gives

    Craw_1=-u/4, Craw_n=0 for every other n.            (34)

The cross variation (31) gives `+u/4` at slice `1` and zero elsewhere.
Although the correction vector itself is zero at `alpha=0`, its
multiplier derivative is not zero; it is that derivative that cancels
(34). Omitting the correction leaves (34). Reversing its sign instead
gives `-u/2`, exactly twice the raw coefficient. These statements concern
the commutator and are distinct from the raw Ward identity (22), which
already holds.

## 9. Uniform temporal locality

The action `S2` is homogeneous quadratic in the independent multiplier
coordinates. Indeed, `Z,l,Q,alpha` are multiplier-linear, `w=G_Zx` is
multiplier-linear, `D Ires` is multiplier-linear, and the two remaining
terms in (1) of the contract are quadratic in their multiplier inputs.

More strongly, all mixed multiplier Hessian entries with label separation
greater than one vanish identically. To see this without a finite-horizon
enumeration, inspect the terms of that formula:

1. `Z_n` depends only on `N_n`. The bond value `l_b` depends only on
   multiplier labels `b` and `b-1`; `Q_n` depends only on label `n`.
2. A derivative of `H_b` or `e_b` in the direction `w` uses only
   `w_b,w_(b-1)`. These carry only `Z_b,Z_(b-1)`. Multiplying by
   `alpha_b` or `l_b` therefore pairs labels within `{b-1,b}`.
3. A derivative of `j_n` uses only `w_(n-1),w_n,w_(n+1)`. It is
   multiplied by `Q_n`, so the resulting multiplier pairs have labels
   `n` and one of `n-1,n,n+1`.
4. The kinetic part of `Hess_A(w,w)` pairs neighboring `w` values;
   its potential part pairs values on the same slice. Thus its
   multiplier labels are equal or adjacent.
5. Every term of `S2hom` pairs `alpha_b` with itself.

At endpoints `Z=0`, so omitted boundary terms cannot enlarge this list.
This proves the horizon-independent multiplier range bound `1` for the
whole formula. It is not a claim that this bound is the smallest possible
one among all completions.

The coefficient functions and transformations also have bounded temporal
stencils. Each `G` reaches one neighboring slice. Hence `Xraw` uses field
values at most two slices away, while `A_t f` uses neighboring residuals
and therefore has the same two-slice field bound. A bond variation `F_b`
uses field slices from `b-2` through `b+1`, restricted to the admitted
interval. A current variation `J_n` uses slices from `n-2` through `n+2`.
Their parameters enter within these same bounded neighborhoods. The
spatial projections in Section 1 do not alter temporal support.
There is no temporal prefix sum and no inverse of a horizon-sized matrix.

## 10. Finite audit versus the universal identities

The formulas are rational on the entire declared rational carrier, so
clearing the denominators of any fixed Ward identity yields an exact
integer identity. This proves the admissibility of the audit's integer
encoding; it is not a uniform precision bound on evolving histories.

The finite case counts can be checked without executing a scientific
fixture. For each horizon the number of parameters per state is
`5(T-1)+1`; the three seeds therefore give

    3[(11)+(16)+(21)+(31)]=237

parameter cases over the four horizons. The locality fixture has 65
independent multiplier coordinates: 15 at each of labels `1,2,3,4` and
5 at label `5`. The six label pairs separated by more than one are
`(1,3),(1,4),(1,5),(2,4),(2,5),(3,5)`, giving

    225+225+75+225+75+75=900

coordinate pairs. These are combinatorial counts, not evaluated fixture
outputs.

Sections 2-9 prove the declared identities for arbitrary horizons and
admitted states. The finite independent programs audit definitions,
implementation, controls, and exact byte agreement. In particular,
whether the chosen dense fixture family detects every defect in
NC01-NC06 is a frozen computational obligation; this proof does not
announce a run or assume its outcome. The two explicit commutator
controls NC07-NC08 have the analytic values derived in (34).

## 11. Interpretation and limits

The field-only premise of the predecessor obstruction has been deliberately
relaxed: `tau` and `p` now transform at second order inside their original
constrained spaces. No existing result is reversed. The construction
provides a bounded-temporal-range second-order action, a raw off-shell
Ward identity, and a skew adjustment that makes the generators commute
off shell through the same order.

The derivation (17)-(19) also identifies its mathematical content. Through
second order it is a local formal pullback of scalar-lapse autonomous
mechanics plus the algebraic auxiliary pairs `l,tauhat` and `Q,phat`.
It does not infer a new nonlinear gravitational bulk law from the
Noether identities. A formal near-identity substitution is sufficient for
the coefficient argument; no exact finite-`epsilon` inverse or
nonperturbative dynamical equivalence has been established here.

All statements are restricted to the fixed force context `a=0`. Orders
three and higher, exact symmetry at `epsilon=1`, physical metric
selection, native-U implementation, and every cross-layer lift remain
outside this result. The allowed inverse is spatial on five fixed sites,
so a spatial locality claim on larger lattices is likewise not supplied.
