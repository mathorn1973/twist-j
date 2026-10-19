# Exact local parent, all-order symmetry, and dynamical classification

Status: PROSPECTIVE
Scope: NON-CANONICAL, NEW_DECLARED L1
Probe: P-INTEGER-LOCAL-PARENT-CLOSURE-1
Owner: A. M. Thorn (`integer-local-parent-2026-10-19`)
Ownership: https://github.com/mathorn1973/twist-j/issues/1659

This proof concerns the explicitly declared rational finite-horizon model.
All algebraic identities hold for every integer horizon T >= 5 and every
admitted rational state, except statements explicitly restricted to regular
coordinate charts. The local parent carrier, gauge interpretation, invariant
reader, and selected higher-order completion are NEW_DECLARED. They are not
derived from the native micro-law U and do not assert a continuum limit or
nonlinear Einstein dynamics. Finite audit counts belong to PREREG.md; the
proofs below do not infer all-horizon statements from those counts.

## 1. Complete inherited finite-horizon definitions

Put m=324, g=1/m, a in {-1,0,1}, A=a/4, and

    e=(1,1,1,1,1),
    ell=(1,-1,0,0,0),
    sigma=(1/2,1/2,0,0,0),
    Pi0 v=v-(sum_r v_r)e/5.

The vertex set is Z/5. Its ten oriented edges are k=r from r to r+1 with
weight w_k=29/324, and k=5+r from r to r+2 with weight w_k=65/324. Vertex
indices are taken modulo five. B is the head-minus-tail incidence matrix,
W=diag(w_k), and

    L=B^T W B=L_int/m,
    L_int=188 I-29(S+S^(-1))-65(S^2+S^(-2)),
    L_adj=188 I-65(S+S^(-1))-29(S^2+S^(-2)).                    (1.1)

All edge weights are positive and the graph is connected. Therefore

    ker L=span(e),
    <v,Lv>>0 for nonzero v in e-perp.

Direct multiplication gives diagonal entries 42884 and off-diagonal entries
-10721 for L_int L_adj. Hence

    L_int L_adj=53605 Pi0,
    (L restricted to e-perp)^(-1)=m L_adj/53605.              (1.2)

A physical trajectory z=(h_n,chi_n) has n=0,...,T, h_n in Q^5, and chi_n in
Q. Both physical endpoints are fixed in every variation. Interior h is
unrestricted: a fixed spatial mean is not imposed on this off-shell carrier.
Write

    Delta h_b=h_b-h_(b-1),       Delta chi_b=chi_b-chi_(b-1),
    q_h,n=h_(n+1)-h_(n-1),     q_chi,n=chi_(n+1)-chi_(n-1).

The autonomous action is

    A_auto[z]
      = (1/2) sum_(b=1)^T (||Delta h_b||^2+(Delta chi_b)^2)
        + sum_(n=1)^(T-1)
          (-(1/2)<h_n,Lh_n>-(1/2)chi_n^2+A chi_n
           +g chi_n<ell,h_n>).                               (1.3)

Its interior derivatives are -R_h,n and -R_chi,n, where

    R_h,n=h_(n+1)-2h_n+h_(n-1)+Lh_n-g chi_n ell,
    R_chi,n=chi_(n+1)-chi_n+chi_(n-1)-A-g<ell,h_n>.           (1.4)

For interior tangent trajectories u,v with zero endpoints, its constant
Hessian is

    H_A[u,v]
      = sum_b (<Delta u_h,b,Delta v_h,b>
               +Delta u_chi,b Delta v_chi,b)
        -sum_n (<u_h,n,Lv_h,n>+u_chi,n v_chi,n)
        +g sum_n (u_chi,n<ell,v_h,n>+v_chi,n<ell,u_h,n>).
                                                                  (1.5)

The local bond density is the following polynomial, with the edge sum taken
over all edges incident to r, regardless of orientation:

    e_b[z](r)
      = (1/2)(Delta h_b(r))^2
        +(1/4) sum_(k incident to r) w_k (Bh_b)_k(Bh_(b-1))_k
        +sigma_r[(1/2)(Delta chi_b)^2+(1/2)chi_b chi_(b-1)
                  -(A/2)(chi_b+chi_(b-1))]
        -(g/2)ell_r[chi_(b-1)h_b(r)+chi_b h_(b-1)(r)].       (1.6)

Define E_star=(4342005/8683757)A^2 and H_b[z]=sum_r e_b[z](r)+E_star.
E_hom is a fixed rational context value. No pointwise positivity of (1.6)
is assumed. The interior edge current is

    j_n[z](k)
      =(w_k/4)(Bh_n)_k
        (q_h,n(tail(k))+q_h,n(head(k)))
       -(g/4)q_chi,n(h_n(0)+h_n(1)) 1_(k=0).                (1.7)

Auxiliary variables are tau_b in e-perp for b=1,...,T and p_n in ker B^T
for n=1,...,T-1. Original multipliers are alpha_b in Q, lambda_b in e-perp,
and N_n in Q^10. Set mu_b=alpha_b e+lambda_b. Their auxiliary and interaction
actions are

    B_aux(M;tau,p)
      =2 sum_b <lambda_b,Ltau_b>
       +2 sum_n <N_n,WB(tau_(n+1)-tau_n)+p_n>,

    I(z,M)
      =-sum_b alpha_b(H_b[z]-E_hom)
       -sum_b <lambda_b,e_b[z]>
       +sum_n <N_n,j_n[z]>.

    S0(z,M,tau,p)=A_auto[z]+B_aux(M;tau,p).                  (1.8)

I is linear in M and quadratic-affine in z. Its constant part in z includes
the declared context E_hom and E_star.

For a vertex parameter theta with theta_0=theta_T=0, define

    Gamma(theta)_alpha,b=mean(theta_b-theta_(b-1)),
    Gamma(theta)_lambda,b=Pi0(theta_b-theta_(b-1)),
    Gamma(theta)_N,n=Btheta_n,

    (G_theta h)_n=(1/2)theta_n*q_h,n,
    (G_theta chi)_n=(1/2)<sigma,theta_n>q_chi,n,             (1.9)

with zero endpoint rows in G_theta. The star in theta_n*q_h,n denotes
componentwise multiplication. G_theta is linear both in theta and in the
physical trajectory. In particular, it acts on zero-endpoint tangents by
the same formula.

## 2. Off-shell identity and the inherited first two orders

### Lemma 2.1. Local continuity and the pure-gauge action identity

For every admitted trajectory,

    C_n[z]:=e_(n+1)[z]-e_n[z]+B^Tj_n[z]
       =(1/2)(q_h,n*R_h,n+sigma q_chi,n R_chi,n).            (2.1)

Moreover, for every theta with zero endpoints,

    B_aux(Gamma(theta);tau,p)=0,
    I(z,Gamma(theta))=-D A_auto[z][G_theta z].              (2.2)

**Proof.** The difference of the two kinetic squares at a vertex is
(1/2)q_h,n Delta_c^2 h_n. For an edge from t to u, the difference of its
local potential contribution is w_k(Bh_n)_k(Bq_h,n)_k/4 at either endpoint.
Adding B^Tj_h gives -(w_k/2)(Bh_n)_k q_h,n(t) at t and
+(w_k/2)(Bh_n)_k q_h,n(u) at u. Summing incident edges gives
(1/2)q_h,n(r)(Lh_n)(r). The scalar part of the density difference is
(sigma_r/2)q_chi,n(Delta_c^2 chi_n+chi_n-A).

The interaction density difference is

    -(g/2)ell_r(chi_n q_h,n(r)+q_chi,n h_n(r)).

At r=0 and r=1, respectively, B^Tj_int adds plus and minus
g q_chi,n(h_n(0)+h_n(1))/4. Since sigma=(1/2,1/2,0,0,0), these are exactly
the corrections required to obtain the two interaction terms on the right
side of (2.1). This proves (2.1) at every vertex without equations of motion.

For the auxiliary action, sum_b <Delta theta_b,Ltau_b>
=-sum_n <theta_n,L(tau_(n+1)-tau_n)> by zero endpoint theta. This cancels the
WB term in B_aux. The remaining term is 2 sum_n <theta_n,B^Tp_n>=0.

In I, the constant term proportional to E_star-E_hom vanishes at Gamma(theta)
because sum_b mean(Delta theta_b)=0. Summation by parts then gives
I(z,Gamma(theta))=sum_n <theta_n,C_n[z]>. By (1.4), (1.9), and (2.1), this
equals -D A_auto[z][G_theta z]. QED.

For original M, define the inherited dressing prescription

    Psi_0[M]=Psi_T[M]=0,
    Psi_n[M]=sum_(b=1)^n mu_b for 1<=n<T,
    theta=Psi[M],      rho=M-Gamma(theta).                 (2.3)

Under delta M=Gamma(psi), one has delta theta=psi and delta rho=0, because
the prefix telescopes. The terminal value Psi_T=0 is an explicit boundary
condition; it is not asserted to equal the total sum of mu.

The #1658 second-order action term is

    S2(z,M)
      =-D_z I(z,rho)[G_theta z]
        +(1/2)H_A[G_theta z,G_theta z].                    (2.4)

The first and second physical generator coefficients are
G_psi z and G_theta G_psi z. Equations (2.2)-(2.4) fix exactly the inherited
jet that the completion below must reproduce.

## 3. Exact completion and regular old-coordinate transformations

### Theorem 3.1. Exact finite polynomial completion of the action

Let epsilon be rational, K_theta=Id-epsilon G_theta, and y=K_theta x. Define

    S_star(x,M,tau,p;epsilon)
      =A_auto[y]+B_aux(rho;tau,p)+epsilon I(y,rho),          (3.1)

where theta,rho are (2.3). Then on the full old carrier, including singular
K_theta, this polynomial identity holds:

    S_star=S0+epsilon I(x,M)+epsilon^2 S2(x,M)
                 +epsilon^3 S3(x,M),

    S3(x,M)=(1/2)D_x^2 I(x,rho)[G_theta x,G_theta x].       (3.2)

There are no higher powers of epsilon in this action identity. The term S3
is cubic in deformation degree after multiplication by epsilon^3, and is
generally degree five in the combined physical and multiplier coordinates.

**Proof.** Put u=G_theta x. Since A_auto is quadratic-affine,

    A_auto[x-epsilon u]
      =A_auto[x]-epsilon D A_auto[x][u]
                  +(epsilon^2/2)H_A[u,u].

Since I is quadratic-affine in x,

    epsilon I(x-epsilon u,rho)
      =epsilon I(x,rho)-epsilon^2 D_x I(x,rho)[u]
          +(epsilon^3/2)D_x^2I(x,rho)[u,u].

Also B_aux(rho)=B_aux(M) by (2.2), and
I(x,rho)-D A_auto[x][u]=I(x,rho)+I(x,Gamma(theta))=I(x,M).
The quadratic coefficient is (2.4); the cubic coefficient is (3.2). These
Taylor identities are exact, so no coefficient has been omitted. QED.

The purely quadratic interaction I_2(u,rho) is obtained from (1.8) on u by
setting A=E_star=E_hom=0. Thus S3=I_2(G_theta x,rho). This is a formula for
the quadratic part, not an instruction to change the physical context a in
the other action sectors.

### Theorem 3.2. Exact symmetry and composition on regular charts

When K_theta is invertible on physical trajectories with fixed endpoints,
define

    X_psi theta=psi,       X_psi M=Gamma(psi),
    X_psi x=epsilon K_theta^(-1)G_psi x,
    X_psi tau=X_psi p=0.                                  (3.3)

Then X_psi y=0, X_psi rho=0, and X_psi S_star=0 exactly. The full Lie bracket
[X_psi,X_eta]=D X_eta[X_psi]-D X_psi[X_eta] vanishes.

For regular initial and final theta, the finite transformation is

    theta'=theta+psi,
    M'=M+Gamma(psi),
    x'=K_(theta+psi)^(-1)K_theta x,
    tau'=tau, p'=p.                                       (3.4)

Admissible compositions have parameter psi+eta and inverse parameter -psi.

**Proof.** Differentiate y=K_theta x:

    X_psi y=K_theta X_psi x-epsilon G_psi x=0.

The invariance of rho follows from linearity of Gamma. Hence every argument
of (3.1) is invariant. Differentiating the inverse gives

    X_psi(K_theta^(-1))
       =epsilon K_theta^(-1)G_psi K_theta^(-1).

Therefore the physical part of D X_eta[X_psi] is

    epsilon^2 K_theta^(-1)
      (G_psi K_theta^(-1)G_eta+G_eta K_theta^(-1)G_psi)x,

which is symmetric in psi and eta. All other nonzero components are constant
translations, so the full bracket is zero. Formula (3.4) preserves y and rho
directly, and matrix cancellation proves its composition and inverse laws.
Fixed physical endpoints are preserved because G has zero endpoint rows.
QED.

As a formal power series, no convergence assumption is required for

    X_psi x=epsilon G_psi x
        +epsilon^2 G_theta G_psi x
        +epsilon^3 G_theta^2 G_psi x+... .                  (3.5)

This reproduces the exact first two generator coefficients of #1658. For a
particular rational epsilon, (3.3), not a truncated or assumed-convergent
series, defines the transformation. The regular chart set is not preserved
by arbitrary parameter translations, as Section 7 proves. Thus (3.4) is a
composition law between regular endpoints, not a global action of all psi
on that restricted old carrier.

## 4. Local independent coordinates and the complete gauge quotient

### Theorem 4.1. Dimension-preserving local parent

Use independent coordinates

    (y,theta,r,nu,tau,p),
    theta_0=theta_T=0, theta_n in Q^5 (1<=n<T),
    r in Q^5, nu_n in Q^10 (1<=n<T),                       (4.1)

with the same physical endpoints and tau,p restrictions. Define residual
rho by mu(rho)_b=0 for b<T, mu(rho)_T=r, and N(rho)_n=nu_n. Reconstruct M by

    mu_b=theta_b-theta_(b-1)                  for b<T,
    mu_T=r-theta_(T-1),
    N_n=nu_n+Btheta_n,
    alpha_b=mean(mu_b), lambda_b=Pi0 mu_b.                 (4.2)

This is a bijection between the old multiplier array M and (theta,r,nu).
It has the same rational dimension 15T-10. The local parent action is

    S_parent(y,theta,r,nu,tau,p;epsilon)
       =A_auto[y]+B_aux(rho;tau,p)+epsilon I(y,rho).        (4.3)

It has bounded temporal stencil and is independent of theta. Its exact
global finite symmetry is theta'=theta+psi with all other independent
coordinates unchanged. Its reconstruction obeys M'=M+Gamma(psi).

**Proof.** From M, calculate theta by (2.3), r=sum_b mu_b, and
nu_n=N_n-Btheta_n. Telescoping gives exactly (4.2), including the terminal
bond. Conversely (4.2) has prefix theta_n and terminal sum r, so these maps
are inverses. The dimensions are

    5(T-1)+5+10(T-1)=15T-10.

Adding physical, tau, and p coordinates gives

    6(T-1)+(15T-10)+4T+6(T-1)=31T-22,

the inherited full finite-horizon dimension; at T=5 it is 133.

All terms of (4.3) use at most three consecutive physical slices or one
adjacent difference of tau. Formula (4.2) is local in time. The inverse
prefix calculation is equivalently the explicit local state update
theta_n=theta_(n-1)+mu_n for n<T, with theta_0=0. The terminal r stores the
unrestricted total lapse. No claim theta_T=sum_b mu_b is made.

For example, theta=0 and r=e reconstruct mu_T=e and total lapse e. Omitting
the terminal residual would reconstruct total lapse zero and fail the
inverse identity. Thus retaining r is necessary on the declared carrier.

Since rho has no theta dependence, neither does (4.3). Its translations
therefore preserve the action on every rational state, for every rational
epsilon, with exact additive composition. Formula (4.2) gives the stated
shift of the reconstructed multipliers. QED.

On a regular old chart, y=K_theta x makes (4.3) exactly (3.1), so the change
of coordinates transfers stationary points and their gauge symmetry. It is
a regular coordinate equivalence on that domain. The native parent is also
well defined where old-chart inversion is singular, but those extra parent
states are not declared bijectively equivalent to singular old coordinates.

### Corollary 4.2. Complete classification of gauge orbits

Two admitted parent states belong to the same gauge orbit if and only if
their entire tuples (y,r,nu,tau,p) agree. The connecting parameter is uniquely
psi=theta'-theta, and each orbit has exactly one representative theta=0.
Every function constant on these orbits factors through that invariant
tuple. This establishes the quotient for the declared symmetry; it does not
assert uniqueness of all possible physical readers or interpretations.

## 5. Complete stationary equations and bulk classification

### Theorem 5.1. The selected parent retains autonomous bulk equations

The parent action has the explicit form

    S_parent=A_auto[y]+2<r,Ltau_T>
      +2 sum_n <nu_n,WB(tau_(n+1)-tau_n)+p_n>
      -epsilon<r,e_T[y]+(E_star-E_hom)e/5>
      +epsilon sum_n <nu_n,j_n[y]>.                       (5.1)

Its complete stationary system is equivalent to the following equations:

    theta is arbitrary,
    nu_n=0 for every interior n,
    r=kappa e for some rational scalar kappa,

    D A_auto[y]-epsilon kappa D H_T[y]=0
        on all interior physical variations,

    2Ltau_T=epsilon[e_T[y]+(E_star-E_hom)e/5],
    2WB(tau_(n+1)-tau_n)+2p_n+epsilon j_n[y]=0,             (5.2)

with the original tau,p admissibility restrictions.

In particular, R_h,n[y]=R_chi,n[y]=0 for 1<=n<=T-2. At n=T-1 the only
additional physical term is the terminal energy derivative. For epsilon
nonzero, (5.2) also imposes H_T[y]=E_hom. At epsilon=0 this energy condition
is not asserted.

**Proof.** Formula (5.1) follows from the support of residual mu at T and
<Pi0 r,Ltau_T>=<r,Ltau_T>. Variation in p_n in ker B^T gives

    nu_n perpendicular to ker B^T, hence nu_n in im B.      (5.3)

Variation in the mean-zero tau coordinates gives

    -B^T Wnu_1=0,
    B^T W(nu_(b-1)-nu_b)=0                  for 1<b<T,
    Lr+B^T Wnu_(T-1)=0.                                  (5.4)

These vectors are already mean-zero, so projection to e-perp does not
weaken the equations. Write nu_1=Bxi_1. The first equation gives Lxi_1=0,
hence xi_1 is constant and nu_1=0. Repeatedly apply the same argument to
nu_b-nu_(b-1), using (5.3), to obtain all nu_n=0. The last equation then
gives Lr=0, or r=kappa e.

The r variation is the penultimate equation in (5.2); the nu variations are
the final equations. With nu=0 and r=kappa e, physical variation of (5.1)
is exactly D A_auto[y]-epsilon kappa D H_T[y]. There is no theta derivative.
This derives every equation of (5.2). Conversely, (5.2), (5.3), and (5.4)
make every admitted independent variation of (5.1) vanish, proving
sufficiency as well as necessity.

H_T involves only slices T-1 and T, so its derivative is zero at all
interior slices n<=T-2. Equation (1.4) gives the stated autonomous bulk
equations. Taking the sum of the terminal Poisson equation yields
epsilon(H_T-E_hom)=0. QED.

The matrix of the p and tau variations of B_aux, with columns (r,nu), has
10T-5 columns and 10T-6 rows. The argument (5.3)-(5.4) proves that its kernel
is exactly span{(r=e,nu=0)}. Therefore its rank is 10T-6 for every T>=5,
namely 44 at T=5. This rank statement is independent of the physical
trajectory, epsilon, and preparation.

The auxiliary solution is also explicit when epsilon!=0 and the terminal
energy condition holds. On e-perp set

    tau_T=(epsilon/2)L^(-1)Pi0 e_T[y],
    tau_n=tau_(n+1)+(epsilon/2)L^(-1)B^Tj_n[y]
             for n=T-1,...,1,
    p_n=-WB(tau_(n+1)-tau_n)-(epsilon/2)j_n[y].             (5.5)

These are rational, have B^Tp_n=0, and satisfy the auxiliary equations in
(5.2). They are unique for the given trajectory because L is invertible on
e-perp. The same formulas
give tau=p=0 at epsilon=0 without requiring a terminal energy condition.
Equations (5.5) solve local constraints with a terminal boundary value;
they do not turn an old-coordinate inverse into a local operation.

There is a useful converse for the inherited autonomous sector. If y obeys
R_h=R_chi=0 at every interior slice and H_b[y]=E_hom, then it embeds as a
stationary parent trajectory with r=0, nu=0, arbitrary theta, and

    tau_b=(epsilon/2)L^(-1)Pi0 e_b[y],
    p_n=-WB(tau_(n+1)-tau_n)-(epsilon/2)j_n[y].             (5.6)

Indeed (2.1) gives Delta e+B^Tj=0. This implies B^Tp_n=0 and the current
equations; the terminal energy assumption gives the full terminal Poisson
equation. The physical variation is D A_auto[y]=0, so all of (5.2) holds.
Here the energy assumption can equivalently be imposed on one bond: summing
(2.1) gives its constancy on any autonomous trajectory.

Thus the selected completion introduces no new nonlinear bulk physical
equation in its invariant coordinates. It retains a terminal energy
condition, its multiplier, and local current constraints. Calling the full
residual system unconditionally A_auto would omit those conditions. On the
sector rho=0 the action itself reduces exactly to A_auto. For arbitrary
fixed rho its physical dependence is still quadratic-affine.

## 6. Regularity and an all-horizon nonlocality theorem

### Theorem 6.1. Exact regular-domain test by temporal continuants

For each of the five h components, put t_n=epsilon theta_n(r)/2; for chi put
t_n=epsilon(theta_n(0)+theta_n(1))/4. On N=T-1 interior slices the relevant
block of K_theta is tridiagonal with diagonal 1, upper entry -t_n in row n,
and lower entry +t_n in row n. Its determinant d_N satisfies

    d_0=d_1=1,
    d_n=d_(n-1)+t_(n-1)t_n d_(n-2) for n>=2.              (6.1)

The old physical chart is regular if and only if the final determinant of
each of the six blocks is nonzero.

**Proof.** The entries follow directly from (1.9). Expansion of the leading
n-by-n determinant along its final row gives
d_n=1*d_(n-1)-(+t_n)(-t_(n-1))d_(n-2). The complete interior matrix is the
direct sum of these six blocks. Fixed endpoint values only add affine
inhomogeneous terms to the interior map; they do not change this determinant.
QED.

An intermediate leading determinant d_n can vanish even when the final
d_N does not. Therefore regularity does not require every leading pivot to
be nonzero, and a correct solver must not silently impose that stronger
condition. Standard exact elimination with pivoting or an adjugate formula
computes the rational inverse wherever the final determinant is nonzero.

### Theorem 6.2. No horizon-independent temporal stencil for the old generator

For epsilon=1 and theta_n=2e on every interior slice, each block has
t_n=1, determinant d_N>0, and

    (K_theta^(-1))_(1,N)=1/d_N,
    d_0=d_1=1, d_N=d_(N-1)+d_(N-2).                       (6.2)

Hence the exact old-chart generator (3.3) cannot be represented by a
horizon-independent bounded temporal stencil on all regular old states.

**Proof.** Positivity follows inductively from the recurrence. The cofactor
for inverse entry (1,N) is the determinant of the matrix obtained by deleting
row N and column 1, times (-1)^(N+1). That minor is triangular with diagonal
-1, so its signed determinant is 1. This proves (6.2).

Choose x_h,T=e_0, all other physical entries zero, and psi_N=2e_0 with all
other parameters zero. Then G_psi x has exactly e_0 at interior time N.
By (6.2), X_psi h_1=e_0/d_N. The temporal separation N-1 can be arbitrarily
large while the chart remains regular. This contradicts any fixed finite
stencil bound for this exact old-coordinate transformation. QED.

At T=5, d_4=5 and direct substitution in K v=e_4 gives

    (X_psi h_1,X_psi h_2,X_psi h_3,X_psi h_4)
      =(1/5,1/5,2/5,3/5)e_0.                             (6.3)

The native symmetry in Section 4 remains a local translation. The theorem
distinguishes that native symmetry from reconstructing the original x.

## 7. Singular charts and the raw-metric control

### Proposition 7.1. Rational singular states are unavoidable on the old carrier

At epsilon=1, theta_1=2e, theta_2=-2e, and all other interior theta zero,
K_theta has a nonzero physical kernel. These theta values are realized by
integer old combined lapses mu_1=2e, mu_2=-4e, mu_3=2e, with all remaining
mu zero. One may choose M=Gamma(theta), hence rho=0.

**Proof.** For any physical component, take a tangent equal to one at
slices 1 and 2 and zero elsewhere, including endpoints. Row 1 of K gives
1-1=0, row 2 gives -1+1=0, and all later rows vanish. The same calculation
applies to each h component and to chi because <sigma,e>=1. Thus the map
collapses distinct old physical fields. Its temporal first block contains
[[1,-1],[-1,1]]. The displayed mu is Delta theta, so it realizes this state
without irrational or undeclared coordinates. QED.

Starting at theta=0 and translating by this theta reaches a singular old
chart. Thus even an initially regular chart does not admit every finite
parameter translation as an old-coordinate bijection.

### Proposition 7.2. The old additive metric is not a gauge-invariant reader

At epsilon=1 take native y_h,3=e_0/4, all other native physical entries zero,
and theta=0. Translate by psi_2=16e_0, with other parameters zero. Both old
charts are regular. The invariant metric reader

    g_r[y]_n=diag(-1,1+y_h,n(r),1-y_h,n(r),1)              (7.1)

remains Lorentzian throughout this fixture, but the same formula applied to
the reconstructed raw x has x_h,2(0)=2 and a negative transverse entry.

**Proof.** For the final theta, G_theta has only an interior row at time 2,
so G_theta^2=0 and K_theta^(-1)=Id+G_theta. Therefore

    x'_h,2=(16/2)(y_h,3-y_h,1)=2e_0,
    x'_h,3=e_0/4.

Since G_theta^2=0, all eigenvalues of K_theta=Id-G_theta equal one, so the
chart is regular.
The invariant reader uses only amplitudes 0 and 1/4, giving positive
transverse entries. The raw reader at (n,r)=(2,0) has entries (-1,3,-1,1).
QED.

Functions of y are gauge invariant by construction. Using (7.1) is an
explicit invariant reading choice, agreeing with the inherited raw reading
at theta=0. It does not prove spacetime tensor-coordinate covariance, and
no Lorentz-signature assertion is made for unrestricted off-shell y.

## 8. Exact common-denominator integer carrier and quotient

### Theorem 8.1. Integer local readout and finite gauge bijection

Choose the independent rational coordinates of (4.1), including bases for
tau in e-perp and p in ker B^T. For storage include both physical endpoints
in the same coordinate vector, even though they remain fixed under every
variation. Store that vector as Z/D, where D>=1 and Z is integral, in the
ordering fixed by PREREG.md. A canonical encoding satisfies
gcd(D,Z_1,...,Z_d)=1 with d=31T-10: the varied dimension is 31T-22, and the
12 fixed physical endpoint values are also stored. Thus T=5 has 145 stored
rational coordinates and 133 varied coordinates. Every endpoint numerator
participates in the joint gcd. Parameters a, E_hom, T, and epsilon are fixed
context outside this encoded state vector.

The declared integer bases may be written explicitly as V_j=e_j-e_4 for
j=0,...,3, and the six edge cycles

    C_0=e_edge0+e_edge1+e_edge2+e_edge3+e_edge4,
    C_(r+1)=e_edge(5+r)-e_edger-e_edge((r+1) mod 5).

Each C_j has zero incidence boundary. The last five have distinct unit
coordinates on the five length-two edges, and C_0 is nonzero on the
length-one edges. They are independent, hence form a rational basis of the
six-dimensional ker B^T. Thus the prescribed coefficient encoding is
unambiguous. The V_j basis has the same immediate property on e-perp.

If theta=Theta/D, r=R/D, and nu=V/D, then the reconstructed multipliers have
the integer readout

    muhat_b=Theta_b-Theta_(b-1)              for b<T,
    muhat_T=R-Theta_(T-1),
    Nhat_n=V_n+BTheta_n,

    alpha_b=(sum_r muhat_b(r))/(5D),
    lambda_b=[5muhat_b-(sum_r muhat_b(r))e]/(5D),
    N_n=Nhat_n/D.                                         (8.1)

For psi=Omega/Q with Q>=1 and integral Omega, the finite translation is
computed entirely in integers by

    D'=DQ,
    Theta'=QTheta+DOmega,
    every invariant stored numerator'=Q times its old numerator,
                                                                  (8.2)

followed by division of D' and all stored numerators by their joint
gcd. This is a total bijection on canonical rational-state encodings, with
inverse parameter -psi and exact additive composition.

**Proof.** Formula (8.1) is (4.2) with denominators cleared. In (8.2), division
by DQ gives theta+psi and the unchanged invariant tuple exactly. Every finite
rational coordinate vector has exactly one positive common denominator and
integer numerator vector with joint gcd one: it is its least common
denominator representation. Thus canonical reduction is deterministic, and
the rational translation, inverse, and composition laws transfer to exact
integer encodings. The gauge quotient is the invariant tuple by Corollary
4.2. QED.

At a fixed common denominator, the local prefix-state update itself is the
integer shear

    (Theta,Mu) -> (Theta+Mu,Mu) on Z^5 x Z^5,              (8.3)

with inverse (Theta',Mu)->(Theta'-Mu,Mu). It is a total integer bijection and
uses only the current stored potential and current lapse input. It does not
choose that lapse input by a derived autonomous physical law.

The displayed unreduced scaling alone is not surjective on a redundant
unrestricted integer encoding. The bijection claim explicitly uses canonical
encodings. Choosing one common denominator, taking a joint gcd, and
reconstructing an old chart are global finite-state arithmetic operations,
not local micro-dynamics. This theorem supplies integer state storage, local
multiplier readout, and gauge transformations; it does not construct a new physical
time-evolution step, bank account, finite energy shell, or native-U update.

An explicit raw-encoding control starts with all stored coordinates zero
and D=1. Translate theta_2(0) by +1/2 and then by -1/2 using (8.2) without
normalization. The denominator becomes 2 and then 4, while all numerators
return to zero. The raw record is not the initial record. Canonical
normalization divides by 4 and returns exactly the original D=1 record.

## 9. Exact inherited witnesses for the completion

Fix T=5, epsilon=1, a=E_hom=0, u=e_0, x_h,3=u, alpha_3=1, and
psi_2=psi_3=u. All unspecified original physical and multiplier coordinates,
as well as tau,p, are zero. Then

    theta_3=theta_4=e, theta_1=theta_2=0,
    rho has r=e and nu=0,
    (G_theta x)_h,4=-u/2 and all other components zero.    (9.1)

Since I_2(v,rho)=-H_T[v] with zero source context, (9.1) gives

    S3=-1/8.                                              (9.2)

Here S0=115/162, I(x,M)=-1/2, and S2=115/648. Therefore

    S_star(1)=115/162-1/2+115/648-1/8=85/324.              (9.3)

For the exact generator, G_psi x has only h_2=u/2. The affected equations
for v=K_theta^(-1)G_psi x are

    v_2=u/2,
    v_3-v_4/2=-u/4,
    v_4+v_3/2=0.

Consequently

    X_psi h_2=u/2, X_psi h_3=-u/5, X_psi h_4=u/10,       (9.4)

with other components zero. This differs from the second-order truncated
generator, whose h_3 component is -u/4.

Indeed that truncated generator produces delta y_h,4=-u/8 and zero in the
other physical components. At the corresponding invariant y, the parent
gradient at h_4 is -(L+Id)u/2. Its action variation is therefore

    (1+188/324)/16=8/81 != 0.                             (9.5)

Equivalently, the previously inherited S_<=2 variation 47/1296 acquires
the S3 derivative 1/16, whose sum is 8/81. The exact generator (9.4) is
required to cancel this full variation.

For the finite transformation by the same psi, the invariant y has y_3=u,
y_4=u/2. The final theta has component zero equal to 1,2,1 at times 2,3,4.
Solving K_(theta+psi)x'=y gives

    h'_2=3u/8, h'_3=3u/4, h'_4=u/8,                     (9.6)

with other physical components zero. Substitution gives y_2=0, y_3=u, and
y_4=u/2, so (9.6) preserves y exactly. The finite transformation is distinct
from x+X_psi x. These values follow by rational algebra and do not rely on
the finite audit output.

## 10. Nonuniqueness and the precise boundary of the result

### Theorem 10.1. The second-order jet does not uniquely select higher physics

Let J(y,r,nu,tau,p) be any declared local rational polynomial in the invariant
tuple. Then

    S_parent_alt=S_parent+epsilon^3 J                     (10.1)

has the same exact local Abelian theta symmetry. In old regular coordinates,
substituting y=K_theta x leaves S0, I, and S2 unchanged. Thus the second-order
jet alone cannot distinguish these completions.

**Proof.** J is independent of theta, so finite translations leave it
unchanged. Its old-coordinate pullback is multiplied by epsilon^3, so it has
no coefficients of deformation degree 0,1,2. QED.

For the explicit local choice

    J(y)=sum_(n=1)^(T-1) sum_r y_h,n(r)^4,                (10.2)

the additional physical derivative is 4 epsilon^3 y_h,n(r)^3. At epsilon=1
and y_h,2=e_0 with all other physical components zero, the derivative shift
at (n,r)=(2,0) is exactly 4. This alternative has the same exact gauge
translation and same second-order jet but different bulk equations. It is
an additional modeling choice, not a consequence of the inherited closure.

Theorem 5.1 classifies the selected minimal pullback completion (3.1),(4.3).
It is not a universal no-go for all possible nonlinear interactions. The
construction neither chooses the extra invariant J nor supplies a physical
principle selecting general relativity from this family.

## 11. Exact differentiation domains for the finite audit

In independent parent coordinates, the action has degree at most two in
each individual coordinate. In old (x,M) coordinates, S_star has degree at
most three in a single multiplier coordinate, since both rho and theta
depend linearly on M. Thus the two-point centered coordinate derivative
used for S_<=2 in #1658 is not universally valid for S_star. The four-point
formula

    [-P(2)+8P(1)-8P(-1)+P(-2)]/12                         (11.1)

is exact whenever P has degree at most four. A generic joint old-coordinate
line can have degree five and requires an exact degree-five derivative
method or exact polynomial/automatic differentiation.

Along the exact gauge tangent specifically, rho is constant and

    y(t)=K_(theta+t psi)(x+t X_psi x)
        =y-epsilon t^2 G_psi X_psi x.                    (11.2)

This follows from K_theta X_psi x=epsilon G_psi x. The parent is
quadratic-affine in y for fixed rho, so its action along (11.2) is an even
quartic. Its derivative vanishes exactly. This special evenness is not a
license to use an insufficient derivative stencil on generic directions.

All integer denominator choices, positive/negative fixtures, and certificate
counts in PREREG.md audit the exact theorems at their stated scope. A local
parent symmetry, an exact regular-chart pullback, a complete gauge quotient,
and the stationary boundary classification are the earned mathematical
targets. A local all-domain inverse for the old x, a new nonlinear bulk
gravity law, physical coordinate covariance, and a native-U derivation are
not asserted.
