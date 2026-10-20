# Composite momentum: unique flow, missing inertial branch

NON-CANONICAL, L1. Prospective analytical proof for
P-RELATIONAL-MASS-INERTIAL-RESPONSE-1, ownership issue #1690.
The complete action of #1687/#1689 is retained. Its interaction and kappa
remain declared premises, not consequences of native U. No prior audit is
repeated. All derivations preceded the first scientific execution.

## 1. What the existing action already determines

Set X=(x1+x2)/2, r=(x1-x2)/2, P=p1+p2, rho=p1-p2. The unchanged action is

    theta=tr(Pi dG)+P^T dX+rho^T dr,
    K=tr(G Pi G Pi)/2, V=kappa r^T G^(-1)r,
    E_P=(sqrt((rho+P)^T G(rho+P))
           +sqrt((rho-P)^T G(rho-P)))/2,
    H=K+E_P+V, S=integral [theta(zdot)-H]dt.                 (1)

G is real symmetric positive definite, Pi symmetric, kappa>0, and both
rho+P and rho-P are nonzero. Time is the fixed Hamiltonian time of #1687.
This is precisely the full two-unit-group Hamiltonian stated before the
P=0 reduction in #1689. There is no freedom to add a P-dependent term while
claiming to keep this same action.

Write p1=(P+rho)/2, p2=(P-rho)/2 and epsilon_i=sqrt(pi^T G pi).
The full equations, using the symmetric Frobenius pairing, are

    Gdot=G Pi G,
    Pidot=-Pi G Pi-(p1 p1^T/epsilon1+p2 p2^T/epsilon2)/2
                    +kappa G^(-1)r r^T G^(-1),
    Xdot=(G p1/epsilon1+G p2/epsilon2)/2,
    rdot=(G p1/epsilon1-G p2/epsilon2)/2,
    Pdot=0, rhodot=-2kappa G^(-1)r.                       (2)

These are smooth on the stated open domain. Every complete initial point
there has a unique local solution. Smooth dependence extends the known
rest orbit, after a specified small perturbation of initial data, over any
fixed compact time interval for sufficiently small perturbations. It does
not prove permanent binding or all-time avoidance of rho=+/-P.

Time, translation and constant GL(2,R) symmetry yield conserved H, P, and

    J=2G Pi+r rho^T+X P^T                                (3)

along the Hamiltonian flow.

Under L, G->LGL^T, Pi->L^(-T)PiL^(-1), X,r->L(X,r),
P,rho->L^(-T)(P,rho), and J->LJL^(-1). Translations X->X+b
send J->J+bP^T. In all moment-pair statements the origin is fixed unless
a translation is explicitly applied.

## 2. The old elliptic internal charge cannot remain fixed

Let j=2G Pi+r rho^T be the old internal charge. Equation (3) gives

    jdot=-Xdot P^T.                                      (4)

For P!=0, constancy of j on an interval requires Xdot=0 there. Set
u=G^(1/2)P, v=G^(1/2)rho. Then

    Xdot=G^(1/2)[(u+v)/|u+v|+(u-v)/|u-v|]/2.

It vanishes exactly when u and v are collinear and |u|<|v|. Thus rho=cP,
|c|>1 throughout the interval. Since P is constant, rhodot=-2kappa G^(-1)r
then forces G^(-1)r parallel to P, hence r parallel to G rho. Consequently

    G^(-1/2)jG^(1/2)=2G^(1/2)PiG^(1/2)
                       +(G^(-1/2)r)(G^(1/2)rho)^T

is symmetric. Its eigenvalues are real, so
delta(j)=det j-(tr j)^2/4<=0.

**Theorem 1.** No smooth nonzero-P trajectory of (1), with kappa>0, can
retain a constant elliptic internal charge delta(j)>0 on any interval.

The full J is conserved instead, but its discriminant is not intrinsic
to the pair under translations at nonzero P. For

    J*=[[0,4],[-2,0]], P=epsilon e1,

translation by b e2 changes delta(J) from 8 to 8-4b epsilon, with no change
in energy or relative state. Thus replacing j by J in the old binding
inequality would change the mathematical premise.

## 3. Exact instantaneous energy and velocity response

Keep G,Pi,r,rho and X fixed, and put E=sqrt(rho^T G rho)>0. Taylor expansion
of the two square roots, with odd terms cancelling, gives

    H(P)=H(0)+(1/2)P^T A P+O(|P|^4),
    A=G/E-G rho rho^T G/E^3,
    Xdot=A P+O(|P|^3).                                  (5)

With q=G^(1/2)rho,

    A=G^(1/2)[I-qq^T/E^2]G^(1/2)/E.

A is positive semidefinite of rank one, with kernel span{rho}. It is the
instantaneous fixed-internal-preparation susceptibility, not a positive
definite mass tensor. If P=s rho, |s|<1, E_P=E exactly.

At the rest witness inherited from #1689,

    kappa=3, G*=I, Pi*=[[0,-1],[-1,0]],
    r*=e1, rho*=6e2, X*=0,
    J=J*, K=1, E=6, V=3, H=10,

one obtains A*=diag(1/6,0). With these internal variables fixed,

    H(s e1)=4+sqrt(36+s^2)=10+s^2/12+O(s^4),
    H(s e2)=10, |s|<6.                                 (6)

Both initial families have the same exact full J*, since X=0. Their
unique local trajectories preserve their own H,P,J. Equation (6) is a
concrete falsifier of a positive isotropic energy curvature for this
specified preparation; it does not assert stability at nonzero P.

## 4. Precise local nonuniqueness at the same full charge

For any fixed real c, choose the smooth initial section

    P=epsilon e1, G=I, r=e1, X=c epsilon e2,
    rho=(6+c epsilon^2)e2,
    Pi=[[0,-1-c epsilon^2/2],[-1-c epsilon^2/2,0]].          (7)

All sections meet the same rest phase point at epsilon=0. For sufficiently
small epsilon they are in the smooth domain. Direct multiplication gives

    2Pi+r rho^T+XP^T=J*                                 (8)

for every epsilon and c. Their exact energy is

    H_c=(1+c epsilon^2/2)^2
            +sqrt(epsilon^2+(6+c epsilon^2)^2)+3
       =10+(2c+1/12)epsilon^2+O(epsilon^4).                (9)

**Theorem 2.** The same action, same rest point, same exact full charge and
same momentum path admit every real quadratic coefficient of the prepared
energy. The freedom is the preparation section, not the vector field.
These are initial-data families, not proved stable bound-state branches;
negative coefficients do not establish negative physical mass.

The previous quotient adds a separate comparison ambiguity. The rest
orbit is generated by Omega=[[0,-2],[1,0]], Omega^2=-2I. A transforms as
A->LAL^T. The rational same-orbit element

    L=(-I+2Omega)/3=[[-1/3,-4/3],[2/3,-1/3]]

commutes with J* and gives

    A_L=[[1,-2],[-2,4]]/54.

The same coordinate P=epsilon e2 now has energy coefficient 1/27, compared
with zero at phase zero. Transforming P along with the state preserves
energy, so this is no covariance failure. It shows that a momentum
comparison on the old phase quotient needs a section or averaging rule.
Similarly L=lambda I leaves rest H,J unchanged while A->lambda^2 A.
A scale or metric for comparing coordinate momenta must be supplied.

## 5. The full-charge ground-state prescription fails

For kappa=3 define F(P) as the infimum of H over the full smooth level
with momentum P and full charge J*. At P=0 the proved predecessor result
gives F(0)=10, attained modulo its stated centralizer.

For any epsilon!=0 and s>0 take

    P=epsilon e1, G=diag(s^2,s^6), Pi=0,
    r=s^2 e1, rho=(4/s^2)e2, X=-(2/epsilon)e2.             (10)

Both individual momenta are nonzero. Exactly,

    r rho^T=[[0,4],[0,0]], XP^T=[[0,0],[-2,0]],
    J=J*, K=0, E_P=s sqrt(epsilon^2+16), V=3s^2,
    H=s sqrt(epsilon^2+16)+3s^2 ->0 as s->0+.              (11)

Since E_P>0 throughout the smooth domain, zero is never attained.
This proves F(epsilon e1)=0. For any nonzero P, the vectors P and J*^T P
are independent. Choose a,b with (aI+bJ*)^T P=e1. Then L=aI+bJ* is invertible
because det L=a^2+8b^2>0, commutes with J*, and its canonical GL action
maps the epsilon=1 family to momentum P without changing H or J*.

**Theorem 3.** F(0)=10 and F(P)=0, unattained, for every P!=0. This
full-charge infimum is discontinuous and has no quadratic expansion at
zero. In particular it cannot define the requested inertial mass.

The sequence (10) is not a local perturbation of the rest point as
epsilon->0. Its trajectories are not claimed complete or permanently
bound. Theorem 3 concerns this precisely specified minimization principle,
not every conceivable family of moving bound trajectories.

## 6. No affine relative equilibria on the proposed moving charge level

For a relative equilibrium generated by a constant affine Lie-algebra
element (B,b), conservation of P and J requires

    B^T P=0, [B,J]+bP^T=0.                               (12)

Suppose P!=0 and delta(J)>0. A GL change sets P=e1. Write
J=[[a,c],[d,e]]. Ellipticity implies (a-e)^2+4cd<0, hence c!=0.
The first equation in (12) gives B=[[0,0],[u,v]]. The second column of
the second equation is (-cv,cu)^T=0, so B=0 and then b=0.

Every such relative equilibrium would therefore be an actual equilibrium.
There is none: each body's velocity G pi/sqrt(pi^T G pi) is nonzero in
the admitted domain.

**Theorem 4.** There is no affine relative equilibrium at nonzero P and
elliptic full J. In particular the #1689 periodic rest relative equilibrium
has no continuation of this type with J=J*. Even the necessary condition
det B=0 contradicts convergence to its generator det Omega=2.

There is also no constrained local critical point of H on this full
(J,P) level. To justify use of Lagrange multipliers, the affine action is
infinitesimally free when P!=0: a stabilizing B obeys BG+GB^T=0, so its
whitened matrix is skew, while B^T P=0 gives a nonzero kernel. A planar
skew matrix with a nonzero kernel is zero; then the center equation gives
b=0. Nondegeneracy of the canonical symplectic form implies that the six
moment-map differentials are independent. The level is regular. A
constrained critical point would have X_H equal to an affine generator,
which Theorem 4 excludes. Thus neither a local minimum nor an unrestricted
global minimum supplies a moving continuation at this fixed charge.

The theorem excludes this specific symmetry mechanism. It does not exclude
all other bound or recurrent trajectories, and it supplies no existence
or long-time stability theorem for them.

## 7. A positive, finite-time response result

Fix the phase-zero internal witness and X(0)=0, and prepare P=epsilon p
while leaving all internal initial variables fixed. The internal field is
even in P and independent of X. Smooth dependence over the fixed interval
[0,T], T=sqrt(2)pi, gives

    z_internal(t,epsilon)=z_0(t)+O(epsilon^2),
    Xdot(t,epsilon)=epsilon A(t)p+O(epsilon^3).             (13)

These remainders are uniform on this fixed interval for sufficiently small
epsilon. Along the unperturbed orbit,

    A(t)=(1/6)a(t)a(t)^T,
    a(t)=(cos(sqrt(2)t),sin(sqrt(2)t)/sqrt(2)).

Integrating over one unperturbed labeled period yields

    [X(T,epsilon)-X(0,epsilon)]/T
       =epsilon A_bar p+O(epsilon^3),
    A_bar=diag(1/12,1/24).                               (14)

This is the exact derivative of a specified finite-time displacement
map. It is positive definite and does not equal the energy Hessian
A*=diag(1/6,0) of its initial-data family. For p=e2, initial total energy
is exactly ten while the one-period displacement has nonzero linear
response. Internal changes at order epsilon^2 retain the full energy
account. No contradiction with conservation occurs.

For the separately chosen period-averaged inverse metric,

    G_bar=diag(3/2,3/4), A_bar=G_bar/18.                   (15)

The number 18 is a conditional susceptibility normalization for that
chosen observation. It is not established physical mass, a rest-energy
identity or a relativistic dispersion law. Neither (13) nor (14) is a
uniform-in-time approximation or a perturbed-periodicity claim.

## 8. What additional data remove which ambiguity

For a unique mathematical response, the action needs no new interaction.
It needs a preparation section P->z(0,P), a fixed origin and representative
of the rest phase/scale, a clock interval, and a declared center/metric
observable. Those data suffice by the smooth initial-value theorem. To
determine just a quadratic energy coefficient, specifying the second jet
of that preparation section suffices. Equation (9) shows that the stated
conserved charges and rest point alone do not fix that jet.

For a bound-state energy, one instead needs a target-independent selection
of a smooth, unique family of genuinely bound states, its exact intrinsic
constraints and reference momentum norm. Existence and stability must be
proved in that selected class. The fixed-full-J extrema and affine
relative-equilibrium choices have been excluded here; adding a section to
them does not repair them. Other long-time families or changed dynamics
require a separately declared problem. No claim of a smallest unique
physical completion is made.

Only if a selected energy has expansion E_bound(P)=E_bound(0)+P^T A_eff P/2
with positive definite A_eff can its inverse define a mathematical mass
tensor in the chosen coordinates. A scalar mass additionally requires
A_eff=g_ref^(-1)/m for an independently selected metric and isotropy.
Physical inertia further requires the momentum/velocity/force relation
and clock/energy calibration, not merely a name assigned to a conserved
quantity. A relativistic energy-momentum law would be an additional result
or premise, not a consequence of the present GL covariance.

## 9. Three distinct levels of conclusion

The instantaneous stream expression D=E_P^2-P^TGP is a relational scalar
under simultaneous GL transformations. The evolving G,Pi and interaction
do not make D automatically conserved or a physical mass. The stable
bound object proved in #1689 is a separate all-time P=0 dynamical theorem.
A physical inertial mass is a further operational statement. This probe
derives their present separation and the exact finite-time response; it
does not identify these three notions.

All universal conclusions rest on the arguments above. The exact finite
verifier audits the new identities and falsifiers, not the old binding
theorem, completeness of arbitrary moving trajectories, or physical data.
