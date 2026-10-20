# A covariant two-stream binding sector and an exact stable relative orbit

Status: prospective analytical draft, NON-CANONICAL, NEW_DECLARED L1.
Continuation of P-RELATIONAL-MASS-JOINT-ACTION-1, merged in public #1687.
Public continuation: #1688, ID P-RELATIONAL-MASS-STABLE-BINDING-1.
Source base: 8a2e6a3b1f35bfc2e2616c340086a7182ffbc050.
All derivations below are analytical. No scientific program, import or
finite-fixture execution was used to obtain them.

## 1. The new choice and the precise reduced carrier

Retain the SPD inverse planar metric G, symmetric momentum Pi and metric
kinetic energy K=tr(G Pi G Pi)/2 from #1687. A nonconstant potential of G
alone cannot preserve its full constant GL(2,R) congruence symmetry: that
group acts transitively on the SPD cone, so an invariant function U(G)
must equal U(I) everywhere. A source-dependent or relational variable is
needed for a nontrivial invariant potential.

Introduce exactly two occupied groups, each with multiplicity one. Their
positions and covectors are continuously variable. In the unreduced pair,
declare the additional positive harmonic potential

    V=(kappa/4)(x1-x2)^T G^(-1)(x1-x2),  kappa>0.             (1)

This is an explicit new interaction and coefficient. It is not derived
from the native update U, the old scalar completion or a physical coupling
constant. It is invariant under simultaneous translations and GL changes
of positions, covectors and metric. The total pair Hamiltonian is

    H=K+sqrt(p1^T G p1)+sqrt(p2^T G p2)+V.

Put X=(x1+x2)/2, r=(x1-x2)/2, P=p1+p2 and rho=p1-p2. Then

    p1^T dx1+p2^T dx2=P^T dX+rho^T dr.

Translation symmetry preserves P. The zero-total-momentum sector P=0 is
invariant. There p1=rho/2 and p2=-rho/2, their velocities are opposite,
and X is constant. After removing the constant center coordinate, the
ten-dimensional phase space and action are

    G in Sym_2^+, Pi in Sym_2, r in R^2, rho in R^2\{0},
    theta=tr(Pi dG)+rho^T dr,
    E=sqrt(rho^T G rho), V=kappa r^T G^(-1)r,
    H=K+E+V,
    S=integral [tr(Pi Gdot)+rho^T rdot-H]dt.                 (2)

The two individual stream energies are E/2. The predecessor's stream
mass-square diagnostic is D_stream=E^2 because P=0. It is not silently
identified with the total interacting rest energy H, which includes
the newly declared binding and metric energies.

Opposite covectors need not belong to the old marked five-direction
preparation. They belong to the ambient continuously varied covector
carrier already declared in #1687. No native five-direction closure is
claimed. The reduction and the stability statement below are explicitly
within P=0, not a claim covering every perturbation of the unreduced pair.

## 2. Common variation and all three energy transfers

At fixed kappa>0, variation of (2) gives

    Gdot=G Pi G,
    Pidot=-Pi G Pi-rho rho^T/(2E)
                          +kappa G^(-1)r r^T G^(-1),
    rdot=G rho/E,
    rhodot=-2 kappa G^(-1)r.                                (3)

All symmetric-matrix derivatives use Frobenius pairing. The potential
therefore changes both the matter and metric equations; keeping only
the matter force would not be the declared common action.

Before reduction, xidot=G pi/sqrt(pi^T G pi), while
p1dot=-kappa G^(-1)r and p2dot=+kappa G^(-1)r. Thus Pdot=0 directly.
The unreduced metric force is
-Pi G Pi-(p1p1^T/epsilon1+p2p2^T/epsilon2)/2
+kappa G^(-1)r r^T G^(-1), which becomes (3) on P=0.

Define three signed exchange rates

    A=rho^T G Pi G rho/(2E),
    W=2 kappa r^T rho/E,
    Z=kappa r^T Pi r.

Direct differentiation gives

    Edot=A-W, Vdot=W-Z, Kdot=-A+Z, Hdot=0.                  (4)

No exchange rate has a prescribed sign. The complete sum cancels exactly.
The old two-component identity Edot=-Kdot is replaced, not retained after
omitting V. Momentum rho is now dynamical, although total pair P remains
zero.

For C=tr(G Pi) and Q=r^T rho, the exact virial relations are

    Cdot=-E/2+V,
    Qdot=E-2V,
    2C+Q=constant.                                         (5)

Thus the strictly negative Cdot of the unbound predecessor is no longer
present. Balance E=2V is possible without modifying the energy accounting.

## 3. The preserved full linear-coordinate charge

For a constant invertible matrix L, transform

    G -> L G L^T, Pi -> L^(-T) Pi L^(-1),
    r -> L r, rho -> L^(-T)rho.                            (6)

The complete theta and H are invariant, including (1). The corresponding
matrix charge, in the convention tr(J B) for a generator B, is

    J=2G Pi+r rho^T.                                       (7)

Directly from (3),

    2(Gdot Pi+G Pidot)
        =-G rho rho^T/E+2 kappa r r^T G^(-1),
    rdot rho^T+r rhodot^T
        =+G rho rho^T/E-2 kappa r r^T G^(-1).

Their sum vanishes. Hence J is constant, transforms by conjugation under
(6), and has constant trace, determinant and discriminant quantity

    delta=det J-(tr J)^2/4.                                (8)

The new binding sector is delta>0. It means J has a nonreal conjugate
eigenvalue pair, with imaginary magnitude sqrt(delta). This is a condition
on a conserved mathematical charge, not an assumed physical angular-momentum
quantization or a selection rule supplied by the native model.

The metric momentum must participate in this sector. At any state with
Pi=0, J=r rho^T has determinant zero and
delta=-(r^T rho)^2/4<=0. In particular, the elliptic sector cannot be
prepared with zero metric momentum.

## 4. The key inequality for permanent binding

At any admitted phase point use the positive square root of G to define

    B=G^(1/2)Pi G^(1/2), y=G^(-1/2)r, q=G^(1/2)rho,
    Jhat=G^(-1/2)J G^(1/2)=2B+y q^T.

B is symmetric, E=|q|, V=kappa |y|^2 and K=tr(B^2)/2. Write

    Jhat=[[s+u,v+a],[v-a,s-u]].

Then

    delta=a^2-u^2-v^2 <= a^2,
    2a=y1 q2-y2 q1.

The second identity holds because 2B is symmetric. The elementary planar
area inequality now gives

    4 delta <= (y1 q2-y2 q1)^2 <= |y|^2 |q|^2,
    E^2 V >= 4 kappa delta.                                (9)

For the exact audit, the gap also has the coordinate-invariant identity

    E^2 V-4kappa delta
      =kappa[(r^T rho)^2+tr(J^2)
                  +tr(G^(-1)J G J^T)-(tr J)^2].           (9a)

Indeed the bracket equals (y^T q)^2+4(u^2+v^2) in the displayed
whitened matrix. This makes its nonnegativity and the sharp area
inequality explicit without numerically taking a matrix square root.

For delta>0 this forces both E and V to remain strictly positive. With
the constant H0=H and K,E,V nonnegative, it gives the uniform bounds

    2 sqrt(kappa delta/H0) <= E <= H0,
    4 kappa delta/H0^2 <= V <= H0,
    D_stream=E^2 >= 4 kappa delta/H0.                       (10)

The instantaneous proper separation measured by the declared covariant
metric is d=2 sqrt(r^T G^(-1)r). Since V=kappa d^2/4,

    4 sqrt(delta)/H0 <= d <= 2 sqrt(H0/kappa).              (11)

These are all-time bounds once global continuation is proved below. They
exclude both collision in this metric distance and unlimited separation;
they also exclude energy loss to zero. They are not claims that coordinate
components of r or G remain bounded at infinite time.

Optimizing E+V under (9) supplies the coarse energy floor

    H0 >= 3 (kappa delta)^(1/3).                            (12)

No equality or sharpness assertion for (12) is needed here; K generally
contributes an additional positive amount.

## 5. Global regularity in the elliptic sector

Let c=sqrt(2H0). As in #1687, ||B||_op<=sqrt(2K)<=c implies

    -cG <= Gdot <= cG,
    exp(-c|t-s|)G(s) <= G(t) <= exp(c|t-s|)G(s).            (13)

On every finite interval, G is bounded above and bounded away from the
SPD boundary. The energy bounds give

    ||Pi||_F <= c/lambda_min(G),
    ||rho|| <= H0/sqrt(lambda_min(G)),
    ||r|| <= sqrt(H0/kappa)*sqrt(lambda_max(G)).             (14)

The lower bound in (10), together with the finite upper bound for G,
also keeps rho uniformly away from zero on every finite interval:

    ||rho|| >= 2sqrt(kappa delta/H0)/sqrt(lambda_max(G)).     (15)

Thus no proposed finite endpoint of a maximal solution can meet either
singular boundary G not SPD or rho=0. All variables stay in a bounded
closed subset of the smooth domain of (3). The vector field is bounded
and locally Lipschitz there, so the solution has a limit and continues.
This excludes both finite maximal endpoints.

Every initial point with G SPD, kappa>0 and delta>0 therefore has one
unique solution for all real time. Bounds (10)-(11) hold throughout it.
In particular, each original individual covector p1=rho/2 and p2=-rho/2
remains nonzero. This addresses the nonsmooth zero-momentum boundary of
the square-root matter energy; it is not silently crossed.

## 6. Robust binding and the limits of that statement

The condition delta>0 is open in the reduced P=0 phase space. Around any
such initial point, choose a sufficiently small neighborhood on which
delta>=delta0>0 and H<=Hmax<infinity. Equations (10)-(11) then give common,
time-independent positive lower bounds for stream energy and separation,
and a common finite upper bound for separation, for every trajectory
from that neighborhood. This is a robust permanently bound sector.

This conclusion alone is not Lyapunov stability of one prescribed orbit,
nor convergence toward an attracting particle. The system is conservative.
The stronger fixed-charge orbit statement in Sections 7-9 is separate.

The criterion delta>0 is sufficient, not asserted necessary. For delta<=0,
the lower bounds in (9) cease to protect the nonzero-momentum domain; no
general global regularity or absence of binding is inferred. For example,
the collinear invariant sector permits small positive rho to reach zero:
with diagonal G,Pi and positive r=(r1,0),rho=(rho1,0), the positive-rho1
branch has r1dot=sqrt(G11)>0 and rho1dot=-2kappa r1/G11<0. Its one-sided
smooth auxiliary extension through rho1=0 shows that sufficiently small positive
rho1 reaches that boundary in a short finite time. This is why the domain
protection must be proved rather than assumed for arbitrary states.
The auxiliary extension establishes finite hitting only; it does not
continue the original nonsmooth Hamiltonian flow beyond rho=0.
The positive potential still gives d<=2sqrt(H/kappa) at every smooth
phase point, regardless of delta. Thus delta<=0 is not a proper-escape
criterion for this positive harmonic potential.

Likewise kappa>0 is essential to the present result. At kappa=0 the
predecessor's two-stream P=0 sector is recovered and its theorem gives
E->0 at both time infinities. For the same initial elliptic charge,
the area part of (9), which does not require kappa, gives
d>=4sqrt(delta)/E. Hence d tends to infinity in both time directions.
This is a globally smooth proper-escape control, since rho is then
constant and nonzero. A conserved charge alone does not supply the
positive interaction energy needed in (9).

## 7. A sharp lower bound on a fixed traceless elliptic charge

Now impose the additional exact charge conditions tr J=0 and delta>0.
For the whitened variables of Section 4 put

    z=y^T q, w=|y||q|,
    a=|y1q2-y2q1|/2, b=sqrt(a^2-delta).

Thus a>=sqrt(delta), b>=0 and w^2=z^2+4a^2. The traceless symmetric
part of Jhat has Frobenius norm sqrt(2)b. The traceless symmetric part
of yq^T has norm w/sqrt(2). Since Jhat=2B+yq^T and tr Jhat=0,
orthogonality of scalar and traceless matrices and the reverse triangle
inequality give

    K >= z^2/16+(w/2-b)^2/4.                               (16)

For fixed w and E>0, V=kappa w^2/E^2. Minimizing the elementary positive
function E+kappa w^2/E^2 yields

    E+V >= 3(kappa w^2/4)^(1/3),
    equality iff E=2(kappa w^2/4)^(1/3), V=E/2.             (17)

At fixed a, w>=2a and w/2-b>=a-b>0. Both the right side of (17) and
the second term of (16) increase with w, while z^2/16 is nonnegative.
Consequently

    H >= f(a),
    f(a)=3 kappa^(1/3) a^(2/3)
                   +(a-sqrt(a^2-delta))^2/4,
    a>=sqrt(delta).                                       (18)

For a>sqrt(delta), put u=sqrt(1-delta/a^2), so 0<u<1. Differentiating
f shows that its stationary point satisfies exactly

    delta^2(1-u)^4=64 kappa u^3(1+u)^2.                    (19)

The left side decreases strictly from delta^2 to zero, while the right
side increases strictly from zero to 256kappa. Thus there is one solution.
The derivative f' tends to minus infinity at the left endpoint and is
positive for sufficiently large a; f tends to infinity as a tends to
infinity. Therefore this stationary point is the unique global minimum.

Equality in (18) requires z=0, w=2a, the balance (17), and aligned
traceless symmetric parts in the reverse triangle inequality (16).
These conditions are attainable. They will be displayed exactly below.

## 8. An exact periodic relative equilibrium with integer data

Choose the explicitly declared witness coefficient kappa=3 and initial
state

    G*=I, Pi*=[[0,-1],[-1,0]],
    r*=(1,0), rho*=(0,6).                                 (20)

Its exact invariants are

    J*=[[0,4],[-2,0]], tr J*=0, delta=8,
    K=1, E=6, V=3, H=10, D_stream=36,
    C=0, Q=0, proper radius=1, d=2.                        (21)

Here a=3,b=1,u=1/3. Equation (19) is satisfied and f(3)=10.
For a direct rational derivative check put c=(kappa/a)^(1/3). Then
f'=2c+(a-b)(1-a/b)/2 and
f''=-2c/(3a)+[(1-a/b)^2+(a-b)delta/b^3]/2.
At this witness f'=0 and f''=88/9>0; global minimality follows from
the uniqueness argument in Section 7, not from this local curvature alone.
All equality conditions in (16)-(18) hold. Thus H=10 is the global
minimum on the complete phase set with the exact fixed charge J=J*.
The coefficient three is a chosen rational example, not a derived physical
constant or a parameter fitted to an observation.

Define

    Omega=[[0,-2],[1,0]]=-J*/2, Omega^2=-2I,
    A(t)=exp(t Omega)
        =cos(sqrt(2)t) I+sin(sqrt(2)t) Omega/sqrt(2).         (22)

The exact solution through (20) is

    G(t)=A(t)A(t)^T,
    Pi(t)=A(t)^(-T)Pi* A(t)^(-1),
    r(t)=A(t)r*, rho(t)=A(t)^(-T)rho*.                      (23)

At t=0 its generator derivatives are

    Gdot=Omega+Omega^T=Pi*,
    rdot=Omega r*=(0,1),
    rhodot=-Omega^T rho*=(-6,0),
    Pidot=-Omega^T Pi*-Pi* Omega=[[2,0],[0,-4]].             (24)

Direct substitution of (20) in (3) gives exactly (24): the metric terms
are -I, diag(0,-3), and diag(3,0). Covariance (6) transports this
equality to every t. Since Omega commutes with J*, the charge along (23)
is the same J*, not merely a conjugate charge.

The complete labeled phase orbit is periodic with period sqrt(2)pi.
At a half-period G and Pi repeat while r and rho change sign; the
full labeled pair has not yet returned. Along the whole orbit all values
in (21) remain constant. The coordinate metric changes, but the proper
pair separation stays exactly two and both streams keep energy three.

For an entirely rational algebraic point on this same exact orbit, one
may use any rational s and

    A_s=(I-s Omega)^(-1)(I+s Omega)
       =[(1-2s^2)I+2s Omega]/(1+2s^2).                     (25)

It equals A(t_s) with t_s=2 arctan(sqrt(2)s)/sqrt(2). Formula (25)
does not assert rational physical time, a global exact evaluator for
arbitrary phase states, or equality of a general discrete-gradient rule
with the common-action flow. It is an exact rationally parametrized
sample of this special analytically known orbit.

## 9. Nonlinear orbital stability on the fixed-charge level

Fix kappa=3. Let M_J be the reduced phase level with the exact charge J=J*.
Let Z(J*)={L in GL(2,R): LJ*=J*L} be its centralizer, acting by (6).
The equality conditions in Section 7 imply that the minimum set of H
on M_J is exactly Z(J*) acting on (20).

To see this, whiten any minimum to G=I. There z=0, |y|=1, |q|=6 and
the oriented area y1q2-y2q1 is six, with orientation fixed by the
elliptic component of J*. Indeed, its sign is continuous as G varies on
the connected SPD cone and cannot vanish when delta>0. The equality
condition in (16) says that
the symmetric part of Jhat is one third the symmetric part of yq^T.
Consequently an ordinary rotation carries the complete whitened state
to (20). Undoing the whitening gives one L with the transformed state
equal to L acting on (20). Both states have the same J*, so L must
commute with J*. Conversely every such L preserves H and J* and is
a minimum.

Energy sublevels on M_J are compact after quotienting by Z(J*). Here is
a direct control of the only noncompact metric freedom. Write

    J*=nu S R S^(-1), nu=sqrt(8),
    R=[[0,1],[-1,0]], S=diag(sqrt(2),1),
    Gbar=S^(-1)G S^(-T).

For any SPD G,

    ||G^(-1/2)J*G^(1/2)||_F^2
       =nu^2 [lambda1(Gbar)/lambda2(Gbar)
                         +lambda2(Gbar)/lambda1(Gbar)].    (26)

This follows from cyclicity of trace and, in dimension two,
R Gbar R^T=(det Gbar)Gbar^(-1). On an energy sublevel H<=Hmax, the
left side is bounded because Jhat=2B+yq^T and

    ||Jhat||_F <= 2sqrt(2Hmax)+Hmax sqrt(Hmax/kappa).

Thus the condition number of Gbar is bounded. Scalar matrices belong
to Z(J*), so one can normalize det Gbar=1 without changing H or J*.
After that normalization both eigenvalues of G, and their reciprocals,
are uniformly bounded. Equations (14)-(15) bound Pi,r,rho and keep
rho away from zero. Closed sublevels therefore have compact sets of
normalized representatives within the smooth phase domain.

Now H-10 is continuous, nonnegative and conserved on M_J, and its zero
set is exactly the centralizer orbit just classified. Compactness of
sublevels modulo the centralizer implies that every neighborhood of
that orbit in the quotient contains a sufficiently small energy sublevel
H<10+epsilon. Otherwise a sequence with H tending to ten but outside
the neighborhood would have normalized convergent representatives,
whose limit is a minimum, a contradiction. Conservation then proves
Lyapunov stability of the minimum orbit modulo Z(J*) on M_J.

This is a nonlinear stability theorem for the exact fixed-charge level.
It is not asymptotic attraction, coordinate-space stability against free
overall rescaling, or a claim for arbitrary perturbations changing J.
The open-sector binding theorem of Sections 4-6 separately covers nearby
charges with delta>0 and retains uniform separation/energy bounds.

## 10. Scientific scope

The construction supplies a genuinely interacting, globally regular and
robust bound pair in a specified conserved-charge sector. It also supplies
an exact periodic relative equilibrium which minimizes energy and is
nonlinearly stable after the stated fixed-charge symmetry reduction.

The positive harmonic pair interaction and its coefficient are new declared
choices. They are not a derivation of gravitational binding, a native
integer implementation, a local spacetime field theory, a physical photon
interaction, an empirical particle spectrum or equality of inertial and
gravitational mass. No Canon promotion follows. The old five-direction
marking and the old scalar carrier are not silently imposed on this new
continuous two-stream interaction.
