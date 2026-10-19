# Exact local parent, cubic completion and dynamical classification

Status: PROSPECTIVE  
Scope: NON-CANONICAL, NEW_DECLARED L1  
Probe: P-INTEGER-LOCAL-PARENT-CLOSURE-1  
Owner: A. M. Thorn, session integer-local-parent-2026-10-19  
Ownership: https://github.com/mathorn1973/twist-j/issues/1659

## 1. Question and frozen outcome contract

This probe continues the exact second-order result of draft PR #1658,
P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-3, pin
56437c4ef2c2e3a5aee679bb87b693395213f644, result
96b100322f5301293cefb382ac47b4ed5c484ad3. The question is whether its specific
completion can be written with a local independent state and an exact finite
symmetry, and what dynamics that selected completion actually contains.

The target is an exact polynomial pullback, a dimension-preserving local
parent, its complete gauge quotient and stationary-equation classification,
with explicit singularity, nonlocal-inverse and nonuniqueness boundaries.
PASS means precisely that these declared algebraic statements and fixed
controls pass. It does not mean that nonlinear Einstein dynamics or native-U
realization has been obtained. The claims are at L1; no cross-layer promotion
or change to Public Canon v103 is proposed.

All six prospective files are frozen before the first execution/import of
either implementation. Static syntax, source, fixture and proof inspection
are allowed. No scientific dry run or target-derived adjustment is allowed.
SOURCE.md fixes actual authority hashes, companion pins, and new choices.

## 2. Graph, fields and inherited action

Work over Q on any finite horizon T>=5. Vertices are r=0,...,4 modulo 5.
Edges k=r have tail r, head r+1, weight 29/324; edges k=5+r have tail r,
head r+2, weight 65/324. B has -1 at the tail and +1 at the head; W is the
diagonal weight matrix. Put

    m=324, g=1/m, e=(1,1,1,1,1), ell=(1,-1,0,0,0),
    sigma=(1/2,1/2,0,0,0), a in {-1,0,1}, A=a/4,
    L=B^T W B,
    (324 L v)_r=188v_r-29(v_(r-1)+v_(r+1))-65(v_(r-2)+v_(r+2)),
    E_star=(4342005/8683757) A^2.

A physical trajectory v_n=(h_n(0),...,h_n(4),chi_n) has n=0,...,T and fixed
endpoints. No mean or Lorentz restriction is imposed on the off-shell domain.
Physical tangent arrays have zero endpoints. E_hom is a fixed rational
parameter, not a varied state coordinate. The action is

    A_auto(v)=sum_(b=1)^T (||h_b-h_(b-1)||^2+(chi_b-chi_(b-1))^2)/2
      +sum_(n=1)^(T-1) [-<h_n,Lh_n>/2-chi_n^2/2+A chi_n+g chi_n<ell,h_n>].

Its interior gradient is -R, with

    R_h,n=h_(n+1)-2h_n+h_(n-1)+Lh_n-g chi_n ell,
    R_chi,n=chi_(n+1)-chi_n+chi_(n-1)-A-g<ell,h_n>.

On bond b define the vertex density

    e_b(r)= (h_b(r)-h_(b-1)(r))^2/2
      + (1/4)sum_(edges k incident on r) w_k (Bh_b)_k(Bh_(b-1))_k
      +sigma_r[(chi_b-chi_(b-1))^2/2+chi_b chi_(b-1)/2
                  -A(chi_b+chi_(b-1))/2]
      -(g/2)ell_r[chi_(b-1)h_b(r)+chi_b h_(b-1)(r)].

H_b=sum_r e_b(r)+E_star. With q_h,n=h_(n+1)-h_(n-1) and
q_chi,n=chi_(n+1)-chi_(n-1), define the edge current

    j_n(k)=(w_k/4)(Bh_n)_k(q_h,n(tail k)+q_h,n(head k))
      -(g/4)q_chi,n(h_n(0)+h_n(1)) [k=0].

The inherited exact off-shell identity is

    e_(n+1)-e_n+B^T j_n=(q_h,n*R_h,n+sigma q_chi,n R_chi,n)/2.

Auxiliaries are tau_b in e^perp (b=1,...,T), and p_n in ker B^T
(n=1,...,T-1). Multipliers are combined bond lapses mu_b in Q^5 and edge
shifts N_n in Q^10. The original split is alpha_b=mean(mu_b),
lambda_b=mu_b-alpha_b e. In combined coordinates set

    B_aux(M)=2sum_b <mu_b,Ltau_b>
       +2sum_n <N_n,WB(tau_(n+1)-tau_n)+p_n>,
    I(v,M)=-sum_b <mu_b,e_b(v)>-sum_b mean(mu_b)(E_star-E_hom)
       +sum_n <N_n,j_n(v)>,
    S0=A_auto+B_aux, Sint=I.

## 3. Local parent and exact completion

Use independent coordinates z=(v,theta,r,nu,tau,p), theta_0=theta_T=0,
theta_n in Q^5, r in Q^5, nu_n in Q^10. Residual multipliers rho have

    mu(rho)_b=0 (b<T), mu(rho)_T=r, N(rho)_n=nu_n.

The local reconstruction M=Gamma(theta)+rho is

    mu_b=theta_b-theta_(b-1) (b<T),
    mu_T=r-theta_(T-1), N_n=nu_n+Btheta_n.

The prefix is represented by a five-component state with local update
theta_n=theta_(n-1)+mu_n for n<T. The terminal residual is retained:
r=sum_(b=1)^T mu_b. This update reads the lapse data; it is not a newly
derived autonomous law for choosing the lapse or a native-U program.

For a parameter psi with zero endpoints define

    (G_psi h)_n=psi_n*(h_(n+1)-h_(n-1))/2,
    (G_psi chi)_n=(psi_n(0)+psi_n(1))(chi_(n+1)-chi_(n-1))/4.

For rational epsilon, let u=G_theta x, K_theta=I-epsilon G_theta,
y=K_theta x. The native parent action, with physical coordinate y, is

    S_parent(y,theta,r,nu,tau,p;epsilon)
      =A_auto(y)+B_aux(rho)+epsilon I(y,rho).

It is independent of theta and has only fixed nearest-layer action stencils.
Its global exact finite symmetry is theta'=theta+psi, every other native
coordinate unchanged. Two parent states belong to the same orbit iff their
entire invariant tuple (y,r,nu,tau,p) agrees; theta=0 is the unique section.
At fixed endpoints the dimension is 31T-22, namely 133 at T=5.

The old-coordinate action is the exact pullback

    S_exact(x,M;epsilon)=S_parent(K_theta x,theta,r,nu,tau,p;epsilon)
      =S0+epsilon I(x,M)+epsilon^2 S2+epsilon^3 S3,
    S2=-D_x I(x,rho)[u]+Hess(A_auto)[u,u]/2,
    S3=Hess_x(I(.,rho))[u,u]/2.

The coefficients through epsilon^2 are exactly #1658. S3 is cubic in epsilon;
it is generally degree five in the combined physical/multiplier coordinates.
There is no coefficient of higher epsilon order in this selected action.

For det K_theta !=0 the exact chart generator and finite map are

    delta theta=psi, delta x=epsilon K_theta^(-1)G_psi x,
    x'=K_(theta+psi)^(-1)K_theta x.

They leave y and rho invariant. The generator commutator is zero to all orders.
The finite maps compose by parameter addition when the required endpoint
charts are regular. They are not a global action on the regular old-chart
subset: arbitrary psi can reach a singular chart. The native parent action
is global on its own rational carrier, including those theta values.

## 4. Stationary classification and limits of selection

The constrained p and tau variations of the parent force nu_n=0 for every n
and r=kappa e for one homogeneous terminal multiplier. Therefore physical
stationarity becomes

    DA_auto(y)-epsilon kappa DH_T(y)=0.

For n=1,...,T-2 these are exactly the autonomous equations R_h=R_chi=0.
Only the last interior slice can receive the terminal energy contribution.
The r variation also imposes H_T=E_hom for epsilon!=0, together with the
mean-zero terminal Poisson condition. The nu variations retain the auxiliary
current constraints. Full residual-sector equivalence is not asserted to be
unconditionally A_auto. The selected rho=0 action is exactly A_auto.

The auxiliary multiplier matrix has nullspace span{(r=e,nu=0)}; its rank is
10T-6, or 44 at T=5. PROOF.md establishes this for every T>=5.

This is a classification of this selected pullback. The second-order data
do not force it uniquely: adding epsilon^3 J(y), with J=sum_(n=1)^(T-1)
sum_(r=0)^4 h_n(r)^4, preserves the exact parent symmetry and the old expansion
through order two while adding a cubic physical force. This alternative is
only a nonuniqueness control, not an adopted gravitational law. It preserves
the second-order data and exact symmetry, not an additional all-order
requirement of exact A_auto agreement throughout the pure-gauge sector.

The gauge-invariant metric reader, if used, reads y. Reading the old additive
TT metric directly from x is not invariant; neither a coordinate-covariance
law for that metric nor an Einstein interpretation has been proved.

## 5. Integer representation and locality contract

Native independent coordinates (including the fixed physical endpoints when
they share the denominator) are stored as Z/D, D>0, normalized by the joint
gcd of D and every stored numerator. The independent ordering is specified
below. For psi=Omega/Q, Q>0, translation uses D'=DQ, all invariant numerators
multiplied by Q, and Theta'=QTheta+D Omega, followed by joint normalization.
This is a total bijection on canonical rational integer encodings, with inverse
parameter -psi and exact parameter composition. Unnormalized scaling is not
claimed to be a bijection on the unrestricted raw-encoding carrier.

At one common denominator D the local multiplier numerators are

    Mu_b=Theta_b-Theta_(b-1) (b<T), Mu_T=R-Theta_(T-1),
    Nhat_n=V_n+BTheta_n,
    alpha_b=sum(Mu_b)/(5D),
    lambda_b=[5Mu_b-sum(Mu_b)e]/(5D), N_n=Nhat_n/D.

The local shear (Theta,Mu)->(Theta+Mu,Mu) on Z^5 x Z^5 has inverse
(Theta',Mu)->(Theta'-Mu,Mu). These local reading/state equations have a fixed
stencil. The common-denominator choice, gcd normalization and old-chart inverse
are global finite-state arithmetic operations, not local micro-dynamics.
No new least-denominator, energy-bank, or native-U theorem is claimed here.

## 6. Exact frozen fixtures and coordinates

The finite audit uses T=5, D=60 and six configurations indexed i=0,...,5,
ordered by a=-1,0,1 outermost and seed s=0,1 innermost. Define

    f(n,j,c)=((17n+11j+7s+5a+3c) mod 19)-9.

All divisions below are exact rational divisions. In each fixture:

    v_n(j)=f(n,j,0)/60, n=0,...,5, j=0,...,5;
    theta_n(r)=f(n,r,1)/60, n=1,...,4, r=0,...,4;
    r(r_index)=f(5,r_index,2)/60;
    nu_n(k)=f(n,k,3)/60;
    tau_b=sum_(j=0)^3 [f(b,j,4)/60] V_j, V_j=e_j-e_4;
    p_n=sum_(j=0)^5 [f(n,j,5)/60] K_j;
    E_hom=(s+1)/(7+a^2).

The cycle basis is fixed by oriented edge coordinates:

    K_0=e_edge0+e_edge1+e_edge2+e_edge3+e_edge4,
    K_(r+1)=e_edge(5+r)-e_edger-e_edge((r+1) mod 5), r=0,...,4.

Both programs check B^T K_j=0 and independence of these six vectors.
For completion/gauge tests v is the old physical x; the corresponding parent
physical field is y=K_theta x. For native parent derivative tests v is directly
the independent parent y. This distinction is fixed, not selected after a run.

Twenty parameter arrays, ordered by n=1,...,4 then r=0,...,4, contain the
single value 1/16 at (n,r). Parameter 20 has psi_n(r)=f(n,r,6)/112.
All have zero endpoints. For parameter index j its companion eta is parameter
(j+1) mod 21. Deformation values are epsilon=-1,0,1,2 in that order.
All fixture theta, theta+psi and theta+psi+eta matrices are strictly diagonally
dominant: |theta_n(r)|<=9/60 and additions are bounded by 9/112 and 1/16.
Thus the tested charts are regular by a prospective analytic bound.

Independent variation order (133 coordinates) is:

1. y_n(j), n=1,...,4 then j=0,...,5 (24).
2. theta_n(r), n=1,...,4 then r=0,...,4 (20).
3. r(r_index), r_index=0,...,4 (5).
4. nu_n(k), n=1,...,4 then k=0,...,9 (40).
5. tau_b coefficient of V_j, b=1,...,5 then j=0,...,3 (20).
6. p_n coefficient of K_j, n=1,...,4 then j=0,...,5 (24).

Canonical integer storage uses the same order, except that physical fields
include both endpoints, n=0,...,5, before theta. There are 145 rational
coordinates plus their common denominator. a, E_hom, T and epsilon are fixed
context, not included as varied coordinates. Tests nevertheless include every
stored physical endpoint numerator in normalization.
The integer gauge audit encodes the corresponding parent with y=K_theta x,
not the untransformed physical fixture v.

## 7. Audits, exact controls and certificate grammar

Each implementation independently performs:

- 798 native parent partial derivatives at epsilon=1 (6*133).
- 24 terminating action-expansion checks (6*4).
- 504 regular-chart inverse, finite gauge invariance/composition/inverse checks,
  504 exact Noether directional checks, 504 exact commutator checks, 504
  canonical integer translation/composition/inverse checks, and 504 local
  multiplier reconstruction checks (6*21*4 per named family).
- The auxiliary rank-44/nullspace check at T=5. Matrix rows are p variations
  (n then cycle index), followed by tau variations (b then mean-zero basis).
  Columns are r then nu, in the order above. Field and theta are zero; it is
  the bilinear B_aux matrix, independent of physical preparation.
- 108 bulk derivative comparisons and 36 final-layer derivative comparisons:
  for fixture i set nu=0, r=((i+1)/7)e and epsilon=1; compare the 24 physical
  derivatives against -R-kappa DH_T, with DH_T=0 before n=T-1.

The implementations must use independent inversion and differentiation
strategies. Primary uses temporal continuants and tridiagonal adjugate entries,
coordinatewise exact central derivatives of the native parent, and polarized
quadratic action coefficients. Breaker uses a full temporal matrix, pivoted
rational Gaussian elimination, Dual derivatives and polynomial coefficient
arithmetic. Neither imports or reads the other's source or EXPECTED.txt.

The three computed payloads use ASCII and one LF per record. Every fraction
is serialized as numerator/denominator, including /1. No expected digest is
fed to either implementation.

    Action: A|i|epsilon|S0,I,S2,S3,S_exact\n
    Gradient: D|i|coordinate_index|derivative\n
    Gauge: G|i|j|epsilon|flatten(x'),flatten(delta x)\n

In the gauge line the two flattened trajectories are concatenated as 72
comma-separated fractions, time n=0,...,5 then component j=0,...,5. Record
ordering is fixture, parameter when present, then epsilon; derivative order
is as above. The action and gradient families have 24 and 798 records; gauge
has 504. SHA-256 is computed from these actual independently generated bytes.
Index and epsilon tokens are decimal integers; only rational value fields
use numerator/denominator serialization.

Fixed witness states have T=5, a=0, E_hom=0, unspecified coordinates zero:

1. Inherited #1658 witness: old h_3=e_0, alpha_3=1 (thus mu_3=e), N=0,
   psi_2=psi_3=e_0. Its residual includes r=e AND nu=-Btheta. Here theta_3=
   theta_4=e, so Btheta=0 and nu=0. S3=-1/8 and S_exact(1)=85/324.
   Exact tangent h at n=2,3,4 is (1/2,-1/5,1/10)e_0; the finite map by the
   same psi is (3/8,3/4,1/8)e_0. The old truncated variation remains
   (W3,W4,W3+W4)=(1/8,-115/1296,47/1296).
2. Nonlocal inverse: theta_n=2e for n=1,...,4, old h_5=e_0, psi_4=2e_0.
   Exact tangent h at n=1,...,4 is (1,1,2,3)e_0/5. Each scalar block has
   determinant 5. The all-horizon continuant is proved, not inferred from
   this one fixture.
3. Singular chart: theta_1=2e, theta_2=-2e, other theta=0, epsilon=1.
   A nonzero tangent h_1=h_2=e_0 is killed by K_theta. Both implementations
   reject inversion with a specific mathematical singularity result.
4. Raw metric: theta=0, y_3=e_0/4, psi_2=16e_0, epsilon=1. The transformed
   old x has h_2=2e_0, hence raw metric diag(-1,3,-1,1); invariant y_2 stays
   zero with metric diag(-1,1,1,1). This is an off-shell reading/covariance
   counterexample, not a prepared-trajectory Lorentz failure.
5. Alternative completion: parent y_2=e_0, J=sum h^4. The added derivative
   with respect to y_2(0) is 4 at epsilon=1 and is unchanged by theta shifts.
6. Unnormalized encoding: all native coordinates zero with D=1, translate
   theta_2(0) by +1/2 and -1/2 using product denominators without gcd reduction.
   The raw denominator ends at 4, although the canonical state returns to D=1.
7. Regular chart with an intermediate zero minor: theta_1=2e, theta_2=-2e,
   theta_3=2e, theta_4=0 and epsilon=1. Each scalar block has leading
   continuants (1,1,0,-1,-1), so the final determinant is -1. For old
   h_1=e_0 the forward map followed by the inverse must recover the field.
   This positive inversion audit is not a ninth negative-control label.

The eight named negative controls are exactly: OMIT_S3 (nonzero missing action
coefficient -1/8); TRUNCATED_GENERATOR (nonzero variation of S_exact using only
epsilon G_psi x+epsilon^2 G_theta G_psi x on witness 1, exactly 8/81); DROP_TERMINAL_RESIDUAL
(r=e,theta=0 loses sum mu=e if the terminal term is omitted); NONLOCAL_INVERSE;
SINGULAR_CHART; RAW_METRIC; NONUNIQUE_COMPLETION; UNNORMALIZED_ROUNDTRIP.
Every label must be recorded once; positive witness checks are not additional
negative controls.

The shared certificate is exactly the following ordered key grammar, with
computed digests replacing the three angle-bracket placeholders:

    CERTIFICATE=P-INTEGER-LOCAL-PARENT-CLOSURE-1
    AUTHORITY_FILES=5
    CONFIGURATIONS=6
    PARENT_COORDINATES=133
    PARENT_VARIATIONS=798
    CUBIC_COMPLETION_CHECKS=24
    FINITE_GAUGE_CHECKS=504
    EXACT_NOETHER_CHECKS=504
    EXACT_COMMUTATOR_CHECKS=504
    INTEGER_GAUGE_CHECKS=504
    LOCAL_MULTIPLIER_CHECKS=504
    AUXILIARY_CONSTRAINT_RANK=44
    BULK_EQUATION_CHECKS=108
    BOUNDARY_VARIATION_CHECKS=36
    ACTION_PAYLOAD_SHA256=<computed>
    PARENT_GRADIENT_SHA256=<computed>
    GAUGE_PAYLOAD_SHA256=<computed>
    OLD_TRUNCATION_REMAINDERS=1/8,-115/1296,47/1296
    CUBIC_COMPLETION_WITNESS=-1/8,85/324
    EXACT_TANGENT_WITNESS=1/2,-1/5,1/10
    FINITE_MAP_WITNESS=3/8,3/4,1/8
    NONLOCAL_INVERSE_WITNESS=1/5,1/5,2/5,3/5
    SINGULAR_CHART=0;KERNEL_NONZERO
    RAW_METRIC_COUNTEREXAMPLE=2;-1,3,-1,1
    ALTERNATIVE_BULK_GRADIENT=4
    NEGATIVE_CONTROLS=8
    CERTIFICATE_RESULT=PASS

The primary runs breaker.py in a separate isolated process with the same
Python executable. Exact raw certificate-byte identity, exit zero and empty
stderr are required. It then appends exactly

    BREAKER_RAW_BYTES=IDENTICAL
    RESULT=PASS

The frozen falsifier labels are AUTHORITY, DOMAIN, PARENT_VARIATION,
CUBIC_COMPLETION, LOCAL_RECONSTRUCTION, CHART_INVERSE, FINITE_GAUGE,
NOETHER, COMMUTATOR, INTEGER_GAUGE, AUXILIARY_RANK, STATIONARY_EQUATIONS,
WITNESSES, NEGATIVE_CONTROLS, CERTIFICATE and BREAKER_BYTES. A scientific
falsifier produces exact stdout FALSIFIER=<label> followed by RESULT=FAIL,
with exit zero and empty stderr. An unexpected incomplete runtime failure
consumes this identifier under the abandoned-pin procedure. No frozen
fixture, implementation, threshold or conclusion changes after execution.

## 8. Public run and limits

Use Python 3.12 standard library, exact integers/Fraction arithmetic, LC_ALL=C,
LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC. Record actual
start/end times, neutral platform/architecture, exit and stream hashes.
The unchanged PR workflow must replay the same EXPECTED.txt on x86_64 and
aarch64. Finite checks audit the self-contained all-horizon algebraic proofs;
they do not turn finite sampling into an all-counter theorem.

Native-U derivation, a three-dimensional nonlinear gravitational action,
physical calibration/selection of couplings, a manifold limit and a physical
decoder remain open. This probe establishes exactly one selected local parent
and its mathematical relation to the preceding finite-horizon construction.
