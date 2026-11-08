# A common planar metric and relational-matter action

Status: prospective analytical draft; NON-CANONICAL, NEW_DECLARED L1.
Candidate: P-RELATIONAL-MASS-JOINT-ACTION-1.
Public ownership: https://github.com/mathorn1973/twist-j/issues/1686.
This draft concerns the new common-action carrier following public #1685.
All statements below are derived analytically. No scientific program,
import, or numerical fixture evaluation was used. The finite witness in
Section 11 is verified by the displayed exact identities.

## 1. The precise new carrier

Let I be a finite, possibly empty set of occupied groups. Each group has a fixed
positive integer multiplicity n_k. Zero-count groups are omitted. The
metric variable is a real symmetric positive-definite 2-by-2 matrix G,
interpreted within this declaration as an inverse spatial metric. Its
canonical momentum Pi is real symmetric. Group k has position x_k in
R^2 and a nonzero momentum covector p_k in R^2.

The momentum variables are continuously varied in the action. The
pentagonal covectors of #1685 are permitted initial data; they are not
a discrete restriction on admissible momentum variations. Their
subsequent constancy will be an equation of motion. Restricting p to
a finite set before varying would not give the position equation below.

The phase one-form and Hamiltonian are declared once, as follows:

    theta = tr(Pi dG) + sum_k n_k p_k^T dx_k,
    epsilon_k(G,p_k) = sqrt(p_k^T G p_k),
    E(G,p) = sum_k n_k epsilon_k,
    K(G,Pi) = (1/2) tr(G Pi G Pi),
    H = K+E.                                                   (1)

The kinetic coefficient is explicitly one. No unmentioned energy unit
or fitted parameter is supplied by that normalization. The weighted
matter form is equivalent to ordinary canonical pairs (x_k,rho_k)
with rho_k=n_k p_k. It prevents a spurious factor n_k in a group's
individual position velocity.

The fixed-time common Hamilton principle is

    S = integral_[t0,t1] [tr(Pi Gdot)
              + sum_k n_k p_k^T xdot_k - H] dt.                (2)

G and x are fixed at the two endpoints; Pi and p are freely varied.
All metric derivatives use the Frobenius pairing on symmetric matrices.
Consequently a derivative with respect to one shared off-diagonal
coordinate includes twice the corresponding matrix entry.

This is a new finite-dimensional homogeneous planar action. It replaces
the old scalar kinetic carrier in this question; it is not obtained by
identifying the old scalar amplitudes with entries of G. Any retained
Canon joint action, including a separately scoped FRW joint action,
retains its own carrier and authority. Neither its existence nor the
old scalar lapse completion supplies an identification with (2).

## 2. Variation and the reciprocal source

Define the moment matrix and total matter momentum

    T_G = sum_k (n_k/epsilon_k) p_k p_k^T,
    P = sum_k n_k p_k.                                          (3)

Direct differentiation gives

    partial_G E = T_G/2,
    partial_(p_k) E = n_k G p_k/epsilon_k,
    partial_Pi K = G Pi G,
    partial_G K = Pi G Pi.                                     (4)

Varying (2), including integration by parts in G and x, therefore gives

    Gdot = G Pi G,
    Pidot = -Pi G Pi - T_G/2,
    pdot_k = 0,
    xdot_k = G p_k/epsilon_k.                                  (5)

Thus initially pentagonal momenta remain pentagonal. The source driving
the metric is the derivative of E, namely T_G/2. It is not the different
mass-square derivative R_G=E T_G-P P^T. Positions respond to the same
metric that receives the matter variation. There is a common variation,
not an externally prescribed force appended to a pre-existing flow.

Eliminating Pi in the metric part yields

    Pi = G^(-1) Gdot G^(-1),
    L_metric = (1/2) tr(G^(-1) Gdot G^(-1) Gdot),
    Gddot - Gdot G^(-1) Gdot = -(1/2) G T_G G.                  (6)

The positive kinetic geometry in (6) is an explicit new choice. No
stabilizing potential has been added.

## 3. Exact energy exchange and translational momentum

The quantity K is nonnegative because

    K=(1/2) tr((G^(1/2) Pi G^(1/2))^2)>=0.

Every occupied epsilon_k is positive, hence E>0 for nonempty I; the
empty preparation has E=0. Differentiating (1)
along (5) gives the separate balances

    Edot = (1/2) tr(T_G G Pi G),
    Kdot = -(1/2) tr(T_G G Pi G),
    Hdot = 0.                                                  (7)

There is no fixed sign for the exchange term. Its two contributions
cancel exactly. Replacing T_G/2 by R_G would change (5) and would not
give this cancellation for the declared H.

Since each x_k is absent from H, every rho_k=n_k p_k is conserved.
In particular P is conserved. There is no scattering or momentum
exchange between groups in this homogeneous model. Their changing
energies arise from the evolving inverse metric.

For comparison with #1685 define

    D_G = E^2-P^T G P.

The triangle inequality for the norm sqrt(p^T G p) gives

    0<=D_G<=E^2.                                               (8)

Because p is constant, its evolution is

    Ddot_G = tr((E T_G-P P^T) Gdot).                            (9)

D_G need not be conserved even though the total Hamiltonian H is.

## 4. Full linear-coordinate Noether balance

For any constant invertible real A, consider

    G -> A G A^T,       Pi -> A^(-T) Pi A^(-1),
    x_k -> A x_k,       p_k -> A^(-T) p_k.                     (10)

Both theta and H are invariant: the matter norm is unchanged and
the metric kinetic term is invariant by cyclicity of trace. This is
an invariance of the ambient continuously varied carrier. A particular
marked pentagonal initial preparation need not be invariant under A.

For an infinitesimal matrix B, contraction of theta with the generator
of (10) is

    tr(J B),   J=2G Pi+sum_k n_k x_k p_k^T.                    (11)

The conserved matrix can also be verified without invoking a theorem:

    Jdot = 2(Gdot Pi+G Pidot)
                  +sum_k n_k xdot_k p_k^T
         = -G T_G+sum_k (n_k/epsilon_k) G p_k p_k^T
         = 0.                                                 (12)

The matrix J need not be symmetric. The indicated trace pairing fixes
the convention and avoids an implicit transpose. Its trace is a useful
dilation balance: matter and metric contributions exchange equally.

## 5. Global finite-time positivity and complete phase flow

Let H0 be the conserved initial energy and put c=sqrt(2H0). On every
local solution set A_G=G^(1/2) Pi G^(1/2). Then

    ||A_G||_op <= ||A_G||_F = sqrt(2K) <= c.

Since Gdot=G^(1/2) A_G G^(1/2), this gives

    -cG <= Gdot <= cG                                         (13)

in the positive-semidefinite order. For any fixed nonzero v, division
by the positive number v^T G v gives

    |d log(v^T G v)/dt| <= c.

Integration, for all t,s in the maximal interval of existence, proves

    exp(-c|t-s|) G(s) <= G(t) <= exp(c|t-s|) G(s).              (14)

This is a matrix bound because it holds on every test vector v.
On any finite time interval, G is therefore bounded above and bounded
away from the SPD boundary. Moreover

    ||Pi||_F <= c/lambda_min(G),
    ||xdot_k|| <= sqrt(lambda_max(G)).                         (15)

The second inequality follows from G^2<=lambda_max(G)G. All p_k stay
equal to their fixed nonzero initial values. Thus, at any proposed
finite endpoint of the maximal interval, all phase variables remain
in a bounded subset on which G stays positive and all epsilon_k stay
away from zero. The smooth vector field (5) is bounded and locally
Lipschitz there, so the solution has a limit and continues through
that endpoint. This contradicts finite maximality.

Consequently (5) has a unique global solution for all real t for every
admitted initial phase point. No nonempty preparation reaches a
singular metric at a finite time. The statement concerns this new
positive kinetic geometry, not every canonical kinetic choice.

## 6. The sharp long-time limitation without a stabilizing potential

Let

    C=tr(G Pi).

Equations (5) and tr(G T_G)=E give

    Cdot=-E/2,
    |C|<=sqrt(2dH0),    d=2.                                  (16)

The bound follows from |tr A_G|<=sqrt(d)||A_G||_F. Therefore C is
strictly decreasing for nonempty matter, is bounded, and has finite
limits at both time infinities. Integrating (16) gives

    integral_R E(t)dt
       =2[C(-infinity)-C(+infinity)]
       <=4sqrt(2dH0)<infinity.                                (17)

The energy derivative obeys a useful relative bound. Positivity of
T_G and (13), together with tr(GT_G)=E, gives

    |Edot|<=(c/2)E.                                          (18)

An everywhere positive function satisfying (17)-(18) tends to zero
at both ends. Indeed, if E exceeded a fixed delta>0 at infinitely
many times tending to either infinity, (18) would keep it above
delta/2 on intervals of one fixed positive length around those times.
A disjoint subsequence of those intervals would contradict (17).
Thus

    E(t)->0,   K(t)->H0,   D_G(t)->0
                      as t->plus or minus infinity.           (19)

The D_G conclusion follows immediately from (8). Each occupied
p_k^T G(t) p_k tends to zero because n_k epsilon_k<=E. If two occupied
covectors span the plane, these two quadratic-form limits force G->0
as a matrix. To see this, use those covectors as a basis. The diagonal
entries of the transformed positive matrix tend to zero; positivity
bounds the square of its off-diagonal entry by their product.

Any two distinct fifth-root covectors span the plane. Hence all
pentagonal preparations occupying at least two directions have G->0
at both ends. G is the inverse metric: this is an approach to its
boundary at infinite time, with the declared source energy tending
to zero. It is not a statement of physical spatial collapse. In
the full-span case the covariant metric G^(-1) expands instead.

Equivalently y=log det G obeys

    ydot=C,    yddot=-E/2.                                    (20)

Strict decrease of C excludes every nonempty periodic full orbit.
There is also no equilibrium: Gdot=0 would force Pi=0, after which
Pidot=-T_G/2 is nonzero. This model supplies reciprocal evolution and
global finite-time positivity. It supplies no binding mechanism or
stability claim beyond the explicit no-equilibrium and no-periodic-orbit
statements just proved.

## 7. Fixed time and an explicitly added clock

Action (2) has fixed time endpoints; it does not independently vary
a lapse multiplying H. If one instead used only a free multiplier
lambda times H, its multiplier equation would impose H=0, impossible
for nonempty matter because K>=0 and E>0. The previous positive-energy
free-lapse obstruction has not disappeared.

A distinct declared extension introduces the canonical clock pair
(t,p_t) and an arbitrary parameter sigma:

    S_ext=integral [tr(Pi G')+sum_k n_k p_k^T x_k'
                  +p_t t' - lambda(p_t+H)] d sigma.            (21)

Here G, x and t are fixed at the parameter endpoints; their canonical
momenta and lambda are varied freely in the interior.

Its equations include

    t'=lambda,    p_t'=0,    p_t+H=0,
    z'=lambda X_H(z)                                         (22)

for the original phase variables z. Choosing lambda=1 recovers (5)
with t=sigma plus a constant and p_t=-H0. Nonempty positive energy
is admitted because the newly introduced clock momentum can be
negative. This is a new canonical pair and a new constraint, not a
derivation of a physical clock, native time, or an old lapse Ward law.

## 8. The exact integer-indexed flow and what it means

Let Phi_t be the global phase flow of (5). Then

    z_(m+1)=Phi_1(z_m),    m in Z,                            (23)

is a well-defined integer-indexed evolution. It preserves H, each p_k,
P and J exactly, and it has inverse Phi_(-1). The flow is canonical
symplectic: differentiation of the preserved symplectic form along
the Hamilton vector field gives zero, since the derivative of dH is
the symmetric Hessian. Its trajectories are stationary paths of (2).

This is an exact analytic phase map. It does not assert an explicit
finite formula, integer-valued coordinates, rational evaluation at
time one, a native implementation, or a global type-1 configuration
generating chart. None of those properties follows from sampling.

## 9. A separate local symmetric divided-difference relation

The following rule is an independently declared discrete-gradient
comparison. It is not identified with (23), and no discrete variational
principle or symplecticity is asserted for it.

Use minus and plus subscripts for endpoint states, with G_- and G_+
positive definite. Set p_(k,+)=p_(k,-)=p_k and

    epsilon_(k,+/-)=sqrt(p_k^T G_(+/-) p_k),
    A=[Pi_- (G_++G_-) Pi_- + Pi_+ (G_++G_-) Pi_+]/4,
    B=[G_- (Pi_++Pi_-) G_- + G_+ (Pi_++Pi_-) G_+]/4,
    C_d=sum_k n_k p_k p_k^T/(epsilon_(k,+)+epsilon_(k,-)).     (24)

All three displayed matrices are symmetric. For a step parameter h
the rule is

    G_+-G_-=hB,
    Pi_+-Pi_-=-h(A+C_d),
    x_(k,+)-x_(k,-)
       =h (G_++G_-)p_k/(epsilon_(k,+)+epsilon_(k,-)),
    p_(k,+)-p_(k,-)=0.                                       (25)

The denominators are strictly positive on admitted endpoints. At
coincident endpoints, A=Pi G Pi, B=G Pi G and C_d=T_G/2, so the
relation is consistent with (5). The position update also reduces
to xdot=Gp/epsilon, with the weighted convention of (1).

At h=0 the derivative of the implicit equations with respect to the
new endpoint is the identity. Thus the implicit-function theorem
gives a unique smooth, indeed analytic, branch near the old endpoint
for sufficiently small |h|. The branch remains SPD by openness. All
coefficients are symmetric in the two endpoints; exchanging endpoints
and replacing h by -h gives the same relation. On this local branch
the step is self-adjoint and second order. For example, expanding a
consistent local map as z+hX(z)+h^2Y(z)+... and composing its inverse
at -h forces 2Y=DX X, the exact second Taylor coefficient.

This local conclusion is not an all-h existence or uniqueness theorem.
In particular the construction does not assert that h=1 has a unique
admitted endpoint or that a finite witness belongs to the h=0 branch.

## 10. Exact discrete energy exchange and its different Noether balance

Write DeltaG=G_+-G_- and DeltaPi=Pi_+-Pi_-. Exact polarization of
the trace polynomial gives

    K_+-K_-=tr(A DeltaG)+tr(B DeltaPi).                       (26)

One way to check (26) is to average the two rectangular paths changing
G first or Pi first. For fixed Pi, the exact G difference has gradient
Pi(G_++G_-)Pi/2; for fixed G, the exact Pi difference has gradient
G(Pi_++Pi_-)G/2. Averaging the appropriate endpoints gives (24).
This proof does not assume that any matrices commute.

For matter, difference of squares gives

    E_+-E_-=tr(C_d DeltaG).                                  (27)

Substitution of (25) into (26)-(27) proves

    K_+-K_-=-h tr(B C_d),
    E_+-E_-=+h tr(B C_d),
    H_+=H_-.                                                (28)

All p_k and hence P are also preserved. These are exact identities
for every admitted endpoint pair satisfying the relation.

The full continuous charge J generally is not preserved. Put

    M=(G_++G_-)/2,  N=(Pi_++Pi_-)/2,
    d=DeltaG,       e=DeltaPi.

Then (24) is equivalently

    A=NMN+eMe/4,    B=MNM+dNd/4.

The product rule with midpoints and the position update give

    DeltaJ=2(M DeltaPi+DeltaG N)+2h M C_d
          =2h(BN-MA)
          =(h/2)(dNdN-MeMe).                                (29)

There is no general cancellation of the last expression. The rule
preserves total energy and translational momenta; it does not inherit
every continuous Noether charge. The exact example below verifies
this distinction with the same endpoints that verify energy exchange.

The charge failure also occurs on the unique branch near h=0. If the
initial Pi is zero, consistency gives e=-hT_G/2+O(h^2), d=O(h^2),
M=G+O(h^2) and N=O(h). Substitution in (29) yields

    DeltaJ=-(h^3/8)(G T_G)^2+O(h^4).                          (29a)

For nonempty matter, T_G is nonzero positive semidefinite. The matrix
G T_G is similar to the nonzero positive-semidefinite matrix
G^(1/2)T_G G^(1/2), whose square is nonzero. Hence (29a) is a genuine
nonzero defect for all sufficiently small nonzero h. This conclusion
does not depend on identifying the finite witness's continuation branch.

## 11. A prospective exact isotropic exchange and charge-defect witness

Use the exact fifth-root carrier of #1685. Let gamma=phi-1 with
phi^2=phi+1 at phi>1, and let

    u_0=(1,0), u_1=(0,1), u_2=(-1,gamma),
    u_3=(-gamma,-gamma), u_4=(gamma,-1),
    G0=[[1,gamma/2],[gamma/2,1]].

The elementary fifth-root identities give

    u_k^T G0 u_k=1,
    sum_k u_k=0,
    sum_k u_k u_k^T=(5/2)G0^(-1).                             (30)

Take n_k=1 for all five groups, p_k=u_k, arbitrary initial positions,
and prescribe the following exact endpoints and positive step:

    G_-=(36/25)G0,   Pi_-=0,
    G_+=G0,         Pi_+=-G0^(-1),
    h=1100/1921.                                            (31)

Both metrics are SPD. Their occupied lengths are respectively 6/5
and 1, so E_-=6 and E_+=5. The kinetic energies are K_-=0 and
K_+=(1/2)tr(I)=1. Thus both total energies equal six.

Equations (24) give, entirely by rational arithmetic and (30),

    A=(61/100)G0^(-1),
    B=-(1921/2500)G0,
    C_d=(25/22)G0^(-1),
    A+C_d=(1921/1100)G0^(-1).                                (32)

Hence hB=-(11/25)G0=DeltaG and -h(A+C_d)=-G0^(-1)=DeltaPi,
which verifies both metric endpoint equations exactly. The position
equation is

    Delta x_k=(1220/1921)G0 u_k.                             (33)

Indeed its scalar factor is
(1100/1921)(1+36/25)/(1+6/5)=1220/1921.

The full charge change follows directly from (11), (30) and (33):

    DeltaJ=-2I+(1220/1921)G0 sum_k u_k u_k^T
          =-(792/1921)I !=0.                                (34)

Thus the very same admitted step has exact reciprocal energy transfer
6+0 -> 5+1, fixed P=0, and an explicit nonzero J defect. It cannot be
an exact flow step of the common action (2) for any time duration,
because that flow conserves J. This does not exclude unrelated
variational descriptions with changed carriers or auxiliary variables;
none is being claimed here.

The witness is a prescribed algebraic endpoint pair. Verifying it does
not establish global solver uniqueness, identify its continuation branch,
or turn a divided-difference rule into an exact sampled Hamiltonian flow.

## 12. A direct symplectic obstruction at the same exact witness

The witness also gives an actual symplectic obstruction, not merely
the absence of a proof of symplecticity. Restrict the input metric
variables to G=g G0, Pi=pi G0^(-1), keep all p_k=u_k fixed, and
initially fix the positions. Write x,y for the input scalars g,pi
and X,Y for the output scalars. These scalar names in this section
are not the particle positions x_k. On isotropic endpoints, (25)
becomes the following two implicit equations:

    f1=X-x-h(x^2+X^2)(y+Y)/4=0,
    f2=Y-y+h(y^2+Y^2)(x+X)/4
                      +5h/[2(sqrt(x)+sqrt(X))]=0.             (35)

At (x,y,X,Y)=(36/25,0,1,-1) and h=1100/1921, direct differentiation
gives the output and input Jacobian matrices

    F_out=[[2471/1921, -11/25],
           [-h/121,    579/1921]],

    F_in=[[-1129/1921, -11/25],
          [101h/2904, -1]].                                  (36)

Their determinants are exactly

    det(F_out)=1423025/1921^2>0,
    det(F_in)=6875/(6*1921)>0.

The derivative of the local scalar endpoint map is -F_out^(-1)F_in.
In two dimensions its determinant is therefore

    det d(X,Y)/d(x,y)
       =528275/341526 !=1.                                   (37)

For completeness, this scalar branch is regular inside the full
six-dimensional symmetric metric-momentum relation. By congruence
covariance one may compute its output Jacobian in orthonormal
coordinates with G0=I. The unit pentagon has fourth moment

    sum_k u_k u_k^T (u_k^T H u_k)
             =(5/8)[tr(H) I+2H]                             (38)

for any symmetric H. This follows by expanding the entries and using
the vanishing sums of second and fourth angular harmonics. The output
Jacobian splits into the scalar block F_out and two identical
traceless blocks. Each traceless block is

    [[2471/1921, -11/25],
     [117h/968,  579/1921]],

with determinant 3086175/(2*1921^2)>0. Hence the full metric output
Jacobian is invertible. The equations for p_+ and x_+ add identity
diagonal blocks, so the complete implicit phase relation also defines
a regular local map at this witness. Isotropic nearby input states
have the isotropic output branch (35), by this local uniqueness.

The canonical symplectic form restricted to the two-dimensional input
surface is 2 dg wedge d pi: tr(Pi dG)=2pi dg. On the image surface
it is 2 dX wedge dY. All p_k remain fixed, so the matter contribution
sum n_k dx_k wedge dp_k pulls back to zero on both surfaces, even
though the output positions vary. If the complete phase map were
symplectic, these two restricted forms would agree. Equation (37)
proves that they do not.

Thus this admitted regular branch is not canonical symplectic and
cannot be a regular fixed-time canonical variational integrator with
the symplectic form of (1). The proof does not require the finite
witness to lie on the h=0 branch, and does not claim a theorem excluding
every possible changed or enlarged variational carrier.

## 13. Scope and arithmetic limits

The result supplies one genuine common action, its reciprocal energy
and full linear-coordinate balances, a global finite-time SPD theorem,
and a sharp asymptotic energy-loss conclusion for the matter subsystem.
It also supplies a separate local energy-preserving discrete-gradient
relation with a concrete failure of the continuous GL(2) charge.

At initial G0 and pentagonal p, with F-valued initial Pi and positions
or with those remaining data retained as declared formal parameters,
local formal series in h can be formed over F=Q(phi) or the corresponding
parameter algebra: the implicit h=0 Jacobian is identity and all initial
lengths equal one. Exact formal coefficient audits therefore require
no floating point. This does not imply finite rational/cyclotomic
closure of general nonzero steps or uniqueness at h=1. The finite
witness (31) is separately justified by (30)-(34).

The fixed-time action and clock extension are explicitly different
variational declarations. Neither is the previous quadratic scalar
completion, and neither inherits its transfer matrix or Ward identities.
The metric-response identities at the special G0 are not silently
promoted to arithmetic identities for arbitrary evolving metrics.

This homogeneous finite-dimensional model has no local source density,
spatial propagation, scattering, binding mechanism, stable particles,
physical energy calibration, Lorentz-complete carrier, native clock,
native realization, physical metric selection, or unnamed layer lift.
The equality of inertial and gravitational mass is not proved by naming
the derivative of E. Public Canon authority is unchanged.
