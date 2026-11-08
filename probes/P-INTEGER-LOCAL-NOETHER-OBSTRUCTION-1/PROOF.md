# Conditional obstruction to bounded temporal multiplier range

Status: PROSPECTIVE analytical proof.  
Scope: NON-CANONICAL, NEW_DECLARED L1, conditional candidate-T.  
This document asserts no completed execution or earned public status.

All notation and the exact class of proposed completions are fixed in
`PREREG.md`. The proof concerns the inherited first-order transformation and
an endpoint-zero second-order variation of the physical fields alone. It is
not an obstruction to every local gauge theory or to a local parent on a
different carrier.

The required identity is quantified over every rational pair of endpoint
values. Each such pair is held fixed during variations. Coefficient
functions may depend on that pair. The second-order field variation must
be defined and finite at every admitted state, including autonomous
on-shell states; division by a vanishing residual is not an admitted way
to avoid the identity there.

## 1. Action gradient and rational autonomous histories

Write `x_n=(h_n,chi_n)` and let `A` be the quadratic action in the
preregistration, with force context `a=0`. For every interior variation
`z=(z_h,z_chi)` with `z_0=z_T=0`, discrete summation by parts gives

    D A(x)[z] = -sum_(n=1)^(T-1)
        [<R_h,n,z_h,n> + R_chi,n z_chi,n].                    (1)

Indeed, the coefficient of `z_h,n` from the kinetic sum is
`2h_n-h_(n-1)-h_(n+1)`. Since `L=B^T W B` is symmetric, the spatial
quadratic term contributes `-Lh_n`. The reciprocal coupling contributes
`g chi_n ell`. Their sum is `-R_h,n`. In the scalar sector the kinetic
coefficient is `2chi_n-chi_(n-1)-chi_(n+1)`, the potential contributes
`-chi_n`, and the coupling contributes `g <ell,h_n>`. Their sum is
`-R_chi,n`. Fixed endpoints remove the endpoint variations.

Fix `T>=5` and `2<=k<=T-2`. Let `u=(1,0,-1,0,0)` and specify two
adjacent slices by

    h_(k-1)=u, h_k=0, chi_(k-1)=chi_k=0.                    (2)

The autonomous equations `R=0` are equivalent to the recurrences

    h_(n+1)=(2I-L)h_n-h_(n-1)+g chi_n ell,
    chi_(n+1)=chi_n-chi_(n-1)+g <ell,h_n>.                 (3)

They also solve for the preceding slice with coefficient one:

    h_(n-1)=(2I-L)h_n-h_(n+1)+g chi_n ell,
    chi_(n-1)=chi_n-chi_(n+1)+g <ell,h_n>.                 (4)

Thus (2) extends uniquely over the required finite interval in both
directions. Every value is rational because all coefficients are rational.
The endpoint values produced by this construction are then held fixed in
the action. A purported identity on the whole inherited domain must apply
to this admitted choice of endpoint data as well.

Since `e^T L=0`, `e^T ell=0`, and both initial spatial means vanish,
equations (3)-(4) imply that every `h_n` has zero spatial mean. The
obstruction therefore does not require a varying spatial mean. At the
distinguished slice they imply, without evaluating any distant history,

    h_(k+1)=-u, chi_(k+1)=0,
    q_h,k=-2u, q_chi,k=0.                                (5)

In what follows take `tau=p=0`. The full state need not solve the
auxiliary Euler-Lagrange equations. It solves the autonomous physical-field
equations, which is exactly what is needed: `B_aux` is independent of `x`.
Consequently every admitted physical-field-only second-order variation
satisfies

    delta2 S0 = D A(x)[delta2 x] = 0.                    (6)

No locality, polynomial dependence, or continuity of the map assigning
`delta2 x` is used. It need only assign a defined, finite endpoint-zero
tangent at this state. Allowing changes of the auxiliary fields invalidates
this step, as Section 6 demonstrates explicitly.

## 2. A localized nonzero current variation

Let the only nonzero multiplier coordinate be `N_(k,0)=1`. Take an arbitrary
uniform spatial parameter

    psi_n=t_n e, t_0=t_T=0.                              (7)

The first-order transformation acts only on the physical fields, so

    delta1 I = D j_k(0)[G_psi x].                         (8)

At slice `k`, (5) gives `(G_psi h)_k=-t_k u`. For any oriented edge
`a=(tail,head)`, differentiation of

    j_h,k(a)=(w_a/4)(Bh_k)_a
                        [q_h,k(tail)+q_h,k(head)]

has two product-rule terms. The term differentiating `q_h,k` vanishes
because `h_k=0`. The other term is

    D j_h,k(a)[G_psi x]
      = (w_a/4)(-t_k(Bu)_a)[-2(u_tail+u_head)]
      = (w_a t_k/2)(u_head^2-u_tail^2).                  (9)

This calculation uses only `t_k`, not its neighboring values. The
interaction-current derivative is zero: in

    j_int,k(0)=-(g/4)q_chi,k[h_k(0)+h_k(1)]

both displayed factors vanish by (5) and `h_k=0`, so each product-rule
term vanishes, regardless of the variation of either factor.

Edge `0` has tail `0`, head `1`, and weight `29/324`. Since
`u_0=1` and `u_1=0`, (8)-(9) yield the exact identity

    delta1 I = -a0 t_k, a0=29/648.                       (10)

The symbol `a0` in this proof is the positive rational `29/648`; it is
not the inherited force parameter, which remains `a=0`. No variation of
a fixed endpoint has been introduced.

## 3. The necessary mixed-coefficient equation

Choose any fixed independent basis of the multiplier carrier, retaining
the unconstrained coordinates `alpha_b` and `N_(n,a)` among its
coordinates. Homogeneous quadratic dependence means that at fixed
physical and auxiliary coordinates a candidate `S2` is a quadratic form

    S2(M)=(1/2) sum_(i,j) H_ij M_i M_j, H_ij=H_ji.       (11)

Its coefficients may depend on the full field history, auxiliary history,
and horizon. This permission includes coefficients that are temporally
nonlocal. Only their multiplier-pair range is restricted by the proposed
bound. In particular, this proof does not assume a field stencil bound.

Evaluate those coefficients on the history of Section 1 and define

    C_b = H_(alpha_b,N_(k,0)).                           (12)

At the multiplier state of Section 2, differentiation of (11) gives
`partial_(alpha_b) S2=C_b`. There is no additional factor of two: the
two symmetric cross terms in (11) combine to `C_b alpha_b N_(k,0)`.

For (7), `B psi_n=0` and `Pi0(psi_b-psi_(b-1))=0`. Therefore `delta0`
changes only the scalar multiplier coordinates,

    delta0 alpha_b=t_b-t_(b-1),
    delta0 lambda_b=0, delta0 N_n=0.                    (13)

It leaves every coefficient in (11) unchanged because it leaves all
nonmultiplier coordinates unchanged. Combining (6), (10), and (13),
the desired second-order identity requires

    sum_(b=1)^T C_b(t_b-t_(b-1)) = a0 t_k               (14)

for every rational interior array `t`. Discrete summation by parts and
`t_0=t_T=0` turn its left side into
`sum_(n=1)^(T-1)(C_n-C_(n+1))t_n`. Taking each interior unit array
separately proves the necessary equations

    C_b-C_(b+1)=a0 delta_(b,k), b=1,...,T-1.             (15)

Conversely, (15) implies (14) for every such parameter. Thus no parameter
choice has been selected after inspecting a response: (15) classifies
the requirement for the entire declared uniform spatial parameter family.

## 4. Complete tail classification and universal range obstruction

Equation (15) makes `C_b` constant on `1,...,k` and separately constant
on `k+1,...,T`. The jump is `a0`, so its complete solution set is

    C_b=c+a0 for b<=k,
    C_b=c    for b>k,                                  (16)

where `c` is an arbitrary scalar in the coefficient field: it lies in `Q`
for a rational-valued completion, while arbitrary real-valued coefficients
allow `c` in `R`. The obstruction is identical in either case: only
`a0 != 0` is needed. The common constant is not fixed by endpoint-zero
parameters and must not be discarded.

The preregistered range bound requires `C_b=0` whenever `|b-k|>R`.
The two possible single-tail choices have ranges

    c=0:   left tail 1,...,k,       maximum distance k-1;
    c=-a0: right tail k+1,...,T,    maximum distance T-k. (17)

Every other `c` makes both tails nonzero and requires range at least
`max(k-1,T-k)`. Hence the system consisting of (15) and its prescribed
range zeros is solvable exactly when

    R >= min(k-1,T-k).                                 (18)

This sharpness statement concerns the necessary mixed-coefficient system
alone. It does not claim that either single tail, or any chosen collection
of such coefficients, completes the entire second-order identity on the
full state space.

For a horizon-independent proposed nonnegative range `R`, choose

    T=2R+5, k=R+2.                                    (19)

These indices satisfy even the stricter interior condition
`2<=k<=T-2`, and `min(k-1,T-k)=R+1`. Equation (18) is then impossible.
Therefore no family of `S2` and field-only `delta2` in the frozen class
can satisfy the second-order identity for all horizons with one fixed
finite multiplier range. Coefficients depending arbitrarily on the
horizon or on distant physical fields do not evade the argument.

There is also a direct plateau version. Set every interior `t_n=1`.
Only `delta0 alpha_1=1` and `delta0 alpha_T=-1` remain. When both
`k-1` and `T-k` exceed the proposed range, locality forces
`C_1=C_T=0`. Thus `delta0 S2=C_1-C_T=0`, whereas (10) gives
`delta1 I=-a0` and (6) gives `delta2 S0=0`. Their sum is nonzero.
The tail classification strengthens this single contradiction by showing
exactly how any unrestricted-range correction must reach a boundary.

## 5. The inherited prefix correction realizes the left tail

This section checks a consequence of the frozen formula, without assuming
or invoking any execution result from a companion probe. Let `A_b` denote
the multiplier configuration with only `alpha_b=1`, and `N_k` the
configuration with only `N_(k,0)=1`. The maps `theta` and `rho` in
`PREREG.md` are linear in the multipliers. Their values on these two
directions satisfy

    theta[N_k]=0, rho[N_k]=N_k,
    theta_n[A_b]=e 1_(b<=n) for 1<=n<=T-1,
    theta_0[A_b]=theta_T[A_b]=0.                        (20)

The field direction `v=G_theta x` is therefore zero for `N_k` and equals
`v_b=G_(theta[A_b])x` for `A_b` and `A_b+N_k`. The Hessian term
`Hess_A(v,v)/2` in the prefix correction has no mixed `A_b,N_k`
coefficient. The difference of its three evaluations defining the mixed
coefficient is zero.

Linearity of `D_x I(x,rho)` in `rho` then makes the mixed coefficient of
the other term exactly

    -D_x I(x,N_k)[v_b] = -D j_k(0)[v_b].                (21)

In (10), use `t_n=1_(b<=n)` on interior slices, with zero endpoints.
Equation (21) is consequently

    C_b^(prefix)=a0 1_(b<=k).                           (22)

This includes `b=T`, for which `theta[A_T]=0` and the coefficient is zero.
The prefix correction thus selects `c=0` in (16). Its noncompact mixed
tail is required by (15) within the inherited class; it is not merely
an accidental numerical feature of one finite trajectory.

## 6. A positive local auxiliary escape, with its precise limitation

Keep the same history and multiplier state and use the interior plateau
parameter. Now relax the field-only restriction for this one witness and
set

    delta2 tau_k=ell/8,
    all other second-order components zero.            (23)

This is an admitted auxiliary direction because `ell` has zero spatial
mean. The only contributing term in the action variation is the shift
term at slice `k`, where `N_(k,0)=1`. Since `tau_k` appears with a minus
sign in `tau_(k+1)-tau_k`,

    delta2 S0
      = -2 <N_k,W B(ell/8)>
      = -(w_0/4)(B ell)_0
      = -(29/1296)(-2)
      = 29/648 = a0.                                  (24)

All terms involving `lambda` vanish because `lambda=0`. Equation (24)
cancels (10) on the plateau without a prefix sum. Reversing the sign
in (23) instead gives total defect `-2a0=-29/324`.

This example is an escape from a premise of the obstruction, not a
counterexample to its conclusion. It shows why the autonomous field
equations alone do not annihilate a variation of the auxiliary sector.
It supplies neither an all-state transformation law nor the remaining
Noether or algebra-closure identities. Those would require a separate
prospective problem.

## 7. Exact integer representations and controls

Let `D` be a positive common denominator of the rational history, and put
`H_n=D h_n`, `X_n=D chi_n`, and `L_int=324L`. Multiplying each autonomous
residual by `324D` gives precisely

    324(H_(n+1)-2H_n+H_(n-1))+L_int H_n-X_n ell=0,
    324(X_(n+1)-X_n+X_(n-1))-ell^T H_n=0.               (25)

All entries are integers. If `Q` is a positive common denominator of the
parameter array, (10) likewise yields the integer identity

    648Q(delta1 I)+29Q t_k=0.                          (26)

The first term is the integer `-29Q t_k`; the second is its opposite.
These are exact encodings, not numerical estimates of small residuals.

The negative controls have independent analytic reasons to fire:

1. Reversing only the tested edge-current sign reverses (10).
2. Removing `N*j` eliminates (8), leaving zero instead of `-a0`.
3. With `g=0` used to build the history, `chi` remains zero. At slice
   `k-1`, evaluation with the inherited nonzero coupling produces scalar
   residual `-g <ell,u>=-1/324`, since `<ell,u>=1`. Thus the two
   recurrences have not been silently decoupled.
4. A range below (18) contradicts the complete classification (16).
5. Adding `C_1=C_T=0` contradicts
   `C_1-C_T=sum_b(C_b-C_(b+1))=a0`.
6. Negating the left tail negates its jump and violates (15).
7. Omitting `S2` leaves the plateau defect `-a0` when `delta2` is
   field-only, by (6).
8. The reversed auxiliary sign leaves `-2a0`, by (24).

The finite audit checks instances and implementation custody. It does not
establish the universal quantifier over range bounds. That quantifier is
settled analytically by (16)-(19). Conversely, the proof does not report
the outcome of either not-yet-executed audit implementation.

## 8. Earned-scope boundary

The mathematical conclusion is conditional on the exact inherited action,
first-order transformation, homogeneous quadratic multiplier correction,
field-only second-order variation, full state-domain requirement, and a
uniform bound on temporal multiplier range. It permits arbitrary spatial
mixing and arbitrary dependence of the coefficient functions and of the
physical-field variation on distant fields.

The conclusion does not exclude transformations of `tau`, `p`, or `M`;
different first-order transformation laws; a new carrier with auxiliary
variables; or another declared action class. In particular, it does not
contradict a local parent formulated in independent coordinates. It proves no
native-U realization, gravitational selection principle, equivalence
principle, Einstein dynamics, or cross-layer statement. The positive
auxiliary example identifies a concrete next admissible question without
answering it prematurely.
