# Transport obstruction and a declared stable collective-inertia completion

Status: prospective analytical draft, NON-CANONICAL, NEW_DECLARED L1.
The internal binding theorem of #1689 is an input and is not re-audited.
All derivations below are analytical; no scientific program or finite
fixture was executed to obtain them. Distinguish throughout:

    H_old: the complete original two-stream Hamiltonian of #1689;
    h:     its retained P=0 internal Hamiltonian;
    H_new: the explicitly changed collective-center Hamiltonian below.

## 1. Original action: an exact positive-transport identity

The original canonical form and Hamiltonian are

    theta=tr(Pi dG)+P^T dX+rho^T dr,
    H_old=K+E_P+V,
    K=tr(G Pi G Pi)/2,
    E_P=(|P+rho|_G+|P-rho|_G)/2,
    V=kappa r^T G^(-1)r, kappa>0.

Here G is SPD, Pi symmetric and |v|_G=sqrt(v^T G v). Its smooth domain
excludes P+rho=0 and P-rho=0. X is the arithmetic center specified in
#1689; no new center or physical frame is substituted in this section.
The conserved quantities are H_old,P and

    J=j+XP^T, j=2G Pi+r rho^T,
    jdot=-Xdot P^T, Xdot=partial_P E_P.

Put u=G^(1/2)P, q_int=G^(1/2)rho and define

    a=|u+q_int|, b=|u-q_int|,
    n_+=(u+q_int)/a, n_-=(u-q_int)/b,
    w=(n_++n_-)/2.

Both a,b are positive. Since 2u=a n_++b n_- and E_P=(a+b)/2,

    Xdot=G^(1/2)w,
    P^T Xdot=(a+b)(1+n_+^T n_-)/4
             =E_P|w|^2
             =E_P Xdot^T G^(-1)Xdot >=0.                 (1)

Equality holds exactly when Xdot=0; for P!=0 this is equivalently
rho=sP with |s|>1. Taking the trace of the charge balance gives

    d tr(j)/dt=-P^T Xdot.                                (2)

This is not dissipation: total H_old is conserved.

## 2. Global obstruction to positive longitudinal mean drift

Let H_old=H0>0. For B=G^(1/2)Pi G^(1/2), y=G^(-1/2)r,
the triangle inequality gives |q_int|<=E_P. Hence

    |tr j|=|2tr B+y^T q_int|
       <=4sqrt(K)+sqrt(V/kappa) E_P
       <=C, C=4sqrt(H0)+H0 sqrt(H0/kappa).                (3)

This bound is uniform even if G grows or degenerates at infinite time.
The identity P^T X=tr J-tr j places P^T X in an interval of width 2C;
(1) makes it nondecreasing on every smooth trajectory.

**Theorem.** Every forward-complete smooth solution of H_old with
P!=0 and finite H0 satisfies

    integral_0^infinity E_P Xdot^T G^(-1)Xdot dt <=2C,
    lim_(T->infinity) P^T[X(T)-X(0)]/T=0.                 (4)

Proof: P^T X is monotone and bounded, so has a finite limit. Integrating
(1)-(2) proves the integral bound, and division of its bounded displacement
by T proves the limit. A two-sided complete solution has both endpoint
limits, with the same 2C bound on the integral over all real time.

Consequently no such solution has X(t)=vt+o(t) with P^T v>0. If a mean
velocity exists, it satisfies P^T v=0; transverse coordinate drift is
not excluded by this theorem. An exactly constant nonzero velocity is
excluded: (4) would give P^T v=0, contradicting strict positivity in (1).
No complete family can have v(P)=A P+o(|P|) with positive-definite
symmetric part of A. This statement takes the long-time limit at each
fixed P, not an interchange of small-P and long-time limits.

If a C2 dispersion F(P) is claimed to obey v(P)=grad_P F(P) for this
same center's long-time mean velocity, (4) forces P^T grad F=0. On a
punctured neighborhood F is constant along every ray; continuity at zero
makes it constant throughout that neighborhood. Its Hessian at zero is
therefore zero. An instantaneous prepared-state Hessian can still be
nonzero, but is not this all-time dispersion.

Optionally, if mI<=G(t)<=MI uniformly and P!=0, then
E_P>=sqrt(m)|P| and (4) gives integral |Xdot|^2 dt<infinity. Cauchy-Schwarz
implies |X(T)-X(0)|/T->0 in every direction. This extra assumption is not
needed for (4), and it does not imply convergence of X itself.

Preparation alone cannot remove (4). A moving-object completion must
explicitly change a premise of the charge/energy/center balance or enlarge
the carrier. The remainder supplies one sufficient changed model.

## 3. Retained internal action and newly separated collective center

Retain exactly the P=0 internal system

    z=(G,Pi,r,rho), theta_int=tr(Pi dG)+rho^T dr,
    h=K+E+V, E=sqrt(rho^T G rho),
    j=2G Pi+r rho^T.

The #1689 theorem supplies complete h-flow and positive finite proper
separation bounds for delta(j)>0. At kappa=3, its exact j=j* minimum
orbit has h*=10, period T*=sqrt(2)pi and separation two. It is orbitally
stable modulo the internal centralizer, on that exact fixed-charge level.

Declare a separate canonical (X,P), a fixed SPD inverse metric gamma,
and the class

    theta_new=theta_int+P^T dX,
    q=P^T gamma P,
    H_new=F(h,q), F(h,0)=h, F>0, F_h>0.                  (5)

F is smooth on h>0,q>=0, with smooth one-sided q derivatives at zero.
Gamma and dependence on the complete internal energy h are new choices;
gamma is not the evolving G or an undeclared average of it. At P=0,
F_h=1 recovers the internal action exactly. At P!=0, (5) replaces the
old stream expression E_P; no identity with H_old is claimed. X is now
a collective canonical coordinate, not automatically the physical mean
of two massless particles.

## 4. Exact moving family, with arbitrary inertia before boosts

Every j component and h commute with H_new. Thus

    hdot=0, Pdot=0, jdot=0,
    zdot=F_h(h,q)X_h(z), Xdot=2F_q(h,q)gamma P,
    z(t)=Phi_h^(a t)(z0), a=F_h(h0,q0),
    X(t)=X0+2F_q(h0,q0)gamma P0 t.                       (6)

All factors are constant along free motion. Completeness and internal
binding therefore follow from the inherited h-flow. At fixed j=j*,P,
monotonicity in h gives the global minimum F(10,q), with precisely the
old internal minimum set. Conservation of h-10 proves its orbital
stability modulo the internal centralizer and center translations.
Even at fixed P, nearby h can change the center velocity; ordinary
position stability and removal of every drift by one comoving frame
are not claimed.

The general expansion is

    F(h,q)=h+a(h)q+O(q^2),
    E_bound(P)=10+a(10)P^T gamma P+O(|P|^4).              (7)

Its inverse scalar inertia in the gamma norm is 2a(10), still arbitrary.
For example F=h+q and F=h+2q meet (5) but have different curvatures.
This is classification within the declared scalar-separation class (5),
not over every possible center–internal Hamiltonian.

## 5. New boost premises uniquely select F

Use canonical orthonormal external coordinates

    x=gamma^(-1/2)X, p=gamma^(1/2)P, q=p^T p.

Express internal variables in that same basis by the canonical GL change
G->gamma^(-1/2)G gamma^(-1/2), r->gamma^(-1/2)r, with reciprocal changes
of Pi,rho. In these coordinates j->gamma^(-1/2)j gamma^(1/2), while h
is unchanged. Suppress tildes and put

    R=[[0,-1],[1,0]], S=tr(jR)=j12-j21,
    ell=x1p2-x2p1, L=ell+S.

S is the inherited internal rotation charge; {h,S}=0 and it commutes
with x,p. At gamma=I the witness has S=6. No physical spin assignment
or quantization is inferred.

Declare a fixed c>0 and boost generators satisfying

    {K_i,p_j}=delta_ij H_new/c^2,
    {K_i,H_new}=p_i,
    {K_i,h}=0.                                          (8)

These kinematical premises are new. They are independent of any target
mass and are not consequences of binding, energy conservation or U.
The first bracket and canonical coordinates force

    K_i=(H_new/c^2)x_i+k_i(z,p),

with k_i independent of x. The last bracket gives {k_i,h}=0. Since k_i
also commutes with q, it commutes with H_new=F(h,q). Therefore

    {K_i,H_new}=(2F F_q/c^2)p_i.

The second bracket forces 2F F_q=c^2 for p!=0, hence also at zero by
smoothness. Integration gives F^2=c^2q+C(h). Positivity and F(h,0)=h
select uniquely, within (5) and (8),

    H_new=sqrt(h^2+c^2q).                                (9)

This derives the dispersion from the declared boost premises; it does
not derive the premises themselves.

## 6. Full canonical Poincare algebra, including the spin correction

Abbreviate H_new by H in this section only. Define the smooth generators

    K=(H/c^2)x-S R p/(H+h), L=x1p2-x2p1+S.               (10)

For epsilon_12=+1 they satisfy

    {p_i,p_j}=0, {H,p_i}=0, {L,H}=0,
    {L,p_i}=epsilon_ij p_j, {L,K_i}=epsilon_ij K_j,
    {K_i,p_j}=delta_ij H/c^2, {K_i,H}=p_i,
    {K_1,K_2}=-L/c^2, {h,K_i}={S,K_i}=0.                (11)

Here is the nontrivial bracket proof. Put f=-1/(H+h), k=S f R p.
Since partial_p H=c^2p/H, the scalar-center term is

    {Hx1/c^2,Hx2/c^2}=-ell/c^2.

The spin–spin brackets vanish: their components depend only on the
mutually commuting h,S,p. The two cross terms sum to

    (2HS/c^2)(f+q f_q).

Using H_q=c^2/(2H) and c^2q=(H-h)(H+h),

    f+q f_q=-1/(H+h)+c^2q/[2H(H+h)^2]=-1/(2H).

The cross terms are -S/c^2, establishing the last boost bracket. The
rotation brackets follow because h,H,S are scalars and x,Rp are planar
vectors. The translation and energy brackets are already established
in (8)-(9). Thus a full canonical realization is supplied, not only a
named dispersion relation.

Within the ansatz k=S f(h,q)Rp, the boost-bracket equation integrates to
f=-1/(H+h)+C(h)/q; smoothness at p=0 forces C=0. Uniqueness across all
canonical center conventions is not claimed. The exact invariants are

    H^2-c^2p^2=h^2,
    H L-c^2(K1p2-K2p1)=hS.                               (12)

The second follows from c^2q/(H+h)=H-h. The free conserved boost charges
are K_i-t p_i. When S!=0, x is a canonical center with the correction
in (10); it is not silently identified with the spatial part of a
Lorentz four-vector or with constituent particle positions.

## 7. Preserved internal charge and explicitly changed symmetry

Every j component commutes with h and {j,S}=[R,j]. Consequently

    {j,K_i}=-(Rp)_i[R,j]/(H_new+h).

Boosts preserve h,tr j,det j and delta(j), but can rotate j by conjugacy.
Their internal action combines the commuting h-flow and S-rotation.
A boosted minimum remains a minimum at the correspondingly rotated
charge. Free time evolution preserves the full internal matrix j exactly.

Internal GL now acts on z independently of the marked external gamma,P.
The old simultaneous active full GL symmetry at fixed gamma has been
relinquished. Transforming gamma as a background gives coordinate
covariance, not the missing Noether symmetry of one fixed context.
In particular

    d(j+XP^T)/dt=(c^2/H_new)gamma P P^T.                  (13)

The old full diagonal charge is not conserved. The new total rotation L
and boost charges are conserved. Equation (13), rather than a hidden
identification, is what removes the original transport obstruction.

## 8. Exact stable translating minimum and model inertial mass

Let z_*(tau) be the #1689 orbit, with kappa=3,h*=10,j=j*. For any P put

    E_*(P)=sqrt(100+c^2P^T gamma P),
    z(t)=z_*((10/E_*)t),
    X(t)=X0+(c^2/E_*)gamma P t.                           (14)

This exact solution is complete, has internal proper separation two,
and has laboratory internal period T_lab=(E_*/10)T*. It is the global
energy-minimum family at fixed internal j,P and has the quotient
stability specified in Section 4. These statements hold for every finite
P, not just a formal small-P expansion.

Its dispersion, expansion and operational model mass are

    E_*^2-c^2P^T gamma P=100,
    E_*=10+(c^2/20)P^T gamma P+O(|P|^4),
    m_*=10/c^2.                                         (15)

The complete internal energy h*=K+E+V=10 enters here, not the stream
energy E=6 or its square 36. A different bound minimum h0 gives h0/c^2.
The exact free velocity and internal time factor satisfy

    v=c^2gamma P/H_new,
    |v|_(gamma^-1)^2=c^4q/H_new^2<c^2,
    d tau/dt=h/H_new=sqrt(1-|v|_(gamma^-1)^2/c^2).         (16)

Thus the center velocity and slowing of the internal clock follow from
the same Hamiltonian; their relation is not imposed a second time.

## 9. Explicit external force test

To test inertia operationally within the model, separately declare

    H_total=H_new+W(X,t), f=-grad_X W,

for a smooth external center potential. This is an added test coupling,
not a derivation of a physical force. It gives Pdot=f, hdot=jdot=0 and
Xdot=c^2gamma P/H_new. Wherever the forced solution is smooth,

    Xddot=[(c^2/H_new)gamma
            -(c^4/H_new^3)(gamma P)(gamma P)^T]f.

At rest, Xddot=(c^2/h)gamma f=gamma f/m, with exactly the same m=h/c^2
as the energy curvature. In orthonormal coordinates the transverse
inverse inertia is c^2/H_new and the longitudinal one c^2h^2/H_new^3.
The internal path remains the inherited h-orbit with
tau(t)=integral h/H_new(t) dt. Global existence for arbitrary unbounded
external W is not claimed; the free completeness theorem is separate.

## 10. An explicit preparation and response protocol within the new model

The moving family can be prepared by a specified operation, without
choosing an internal state after inspecting its energy curvature. Fix
gamma,c and an arbitrary phase z_*(tau0) of the inherited h=10,j=j*
minimum. Set P(t0)=0 and choose the center X(t0)=X0. Prescribe a smooth
force pulse f(t), supported in a finite interval [t0,t1], with desired
impulse

    P_*=integral_(t0)^(t1) f(t) dt.

Use exactly the declared coupling W(X,t)=-f(t)^T X. Its equations have
the explicit solution throughout the pulse

    P(t)=integral_(t0)^t f(s) ds,
    H_new(t)=sqrt(100+c^2P(t)^T gamma P(t)),
    tau(t)=tau0+integral_(t0)^t 10/H_new(s) ds,
    z(t)=z_*(tau(t)),
    X(t)=X0+integral_(t0)^t c^2gamma P(s)/H_new(s) ds.     (17)

Thus h=10 and the full internal j=j* stay exact throughout preparation.
The pulse changes the collective momentum and accumulates a definite
internal phase; it does not excite the internal minimum away from its
orbit. Smooth finite support keeps P finite, d tau/dt<=1 and center speed
bounded by c in the marked norm, so this particular forced solution is
complete. This is stronger than the general local force statement of
Section 9, and does not cover arbitrary external potentials.

After t1 the coupling vanishes. Equation (17) becomes exactly the free
ballistic solution (14), with momentum P_*, the resulting center and
internal phase, and permanently bounded proper separation. The final
energy depends only on the impulse:

    Delta H_new=sqrt(100+c^2P_*^T gamma P_*)-10
               =integral_(t0)^(t1) Xdot^T f dt.           (18)

The center offset and internal phase can depend on pulse shape, but the
energy and subsequent velocity do not. Different initial internal phases
also give the same energy/velocity law.

Two distinct model observations can now be compared: energy change versus
prescribed impulse, and acceleration versus prescribed force. For a
nonzero impulse P_* and a scaled pulse lambda f, the former has leading coefficient
(c^2/20)lambda^2 P_*^T gamma P_*. The latter has leading response
Xddot=(c^2/10)gamma lambda f+O(lambda^3) on the fixed pulse interval.
Both determine m=10/c^2 independently of the internal phase. These are
operational statements in the declared equations, not reports of an
experiment or a physical calibration. Native preparation of the internal
state, the reference gamma and this force coupling remains unproved.

## 11. Falsifiers and scientific boundary

Exact prospective checks can attack the following statements directly:

1. In H_old, identity (1), trace balance (2), or uniform bound (3).
   A complete finite-energy trajectory with P^T v_mean>0 refutes (4).
2. Before boost premises, F=h+q and F=h+2q give different curvatures;
   no unique inertia is asserted from separation and binding alone.
3. After (8), the residual 2F F_q-c^2 must vanish identically.
   A positive smooth counterexample not satisfying (9) refutes selection.
4. At x=p=0,h=10,S=6, naive K=Hx/c^2 has boost bracket zero, failing
   the required -6/c^2. Corrected (10) must give -6/c^2 exactly.
5. Substitution of (14) must satisfy (6), preserve h,j,P and reproduce
   the energy Hessian c^2gamma/10 and the same rest force response.
6. Claiming conservation of the old full charge at P!=0 contradicts
   the explicit nonzero derivative (13).
7. The prescribed pulse (17) must keep h,j exact and satisfy (18);
   phase-dependent final energy at the same impulse refutes this protocol.

Under new premises, the completion supplies a stable moving bound family,
a uniquely boost-compatible energy law, full canonical planar Poincare
brackets, and matching energy/force inertia. Harmonic V and kappa,
collective separation, gamma,c and validity of (8) remain declared inputs.
This is a consistent mathematical model of inertia. A native-U bridge,
physical particle/clock/metric identification, and equality of inertial
and gravitational mass are not supplied. No Canon promotion follows.

## 12. Optional closed reference lift and its exact resource cost

One can restore a conserved full diagonal GL charge by enlarging the
carrier. Add gamma in Sym_2^+ and Gamma in Sym_2, hence six new phase
coordinates, and declare the autonomous action

    theta_ref=theta_int+P^T dX+tr(Gamma dgamma),
    q=P^T gamma P, H_ref=sqrt(h^2+c^2q).

The absence of Gamma from the energy is explicit. Hamilton's equations are

    hdot=Pdot=H_ref_dot=0, zdot=(h/H_ref)X_h(z),
    Xdot=c^2gamma P/H_ref, gammadot=0,
    Gammadot=-c^2PP^T/(2H_ref).

Gamma(t)=Gamma(0)-c^2t PP^T/(2H_ref); the internal flow and center are
complete in the inherited elliptic sector. Internal fixed-j stability
persists at fixed P,gamma. No coercive stability of Gamma or of arbitrary
reference perturbations is asserted. The initial gamma and c are new data.

Under the old internal GL action and, for A in GL(2,R),

    X->AX, P->A^(-T)P,
    gamma->A gamma A^T, Gamma->A^(-T)Gamma A^(-1),

both theta_ref and H_ref are invariant. The exact total Noether matrix is

    J_all=j+XP^T+2gamma Gamma.

Its derivative vanishes: the center term gives c^2gamma PP^T/H_ref and
the reference term its negative. GL transformations conjugate j; its
centralizer alone preserves the exact fixed-j level used for stability.

This restoration has a precise cost. Put Q_ref=2tr(gamma Gamma). For P!=0,

    Q_ref_dot=-c^2q/H_ref=-P^T Xdot<0.

The reference stores unbounded dilation charge at fixed energy, thereby
removing the bounded-charge premise of Section 2. For Gamma(0)=0, a
candidate positive reference kinetic energy along this same solution is

    K_ref=tr(gamma Gamma gamma Gamma)/2
         =c^4q^2t^2/(8H_ref^2)=Q_ref(t)^2/8.

Adding K_ref while claiming the same constant-energy ballistic trajectory
therefore fails: the required reference energy grows quadratically in time.

For the distinct costed model H_cost=H_ref+K_ref, P and J_all remain
conserved. On H_cost=H0, h<=H0 and K_ref<=H0. Equation (3), applied to h,
bounds tr(j), while |Q_ref|<=4sqrt(K_ref)<=4sqrt(H0). Thus

    P^T X=tr(J_all)-tr(j)-Q_ref

is uniformly bounded. Its derivative c^2q/H_ref is positive at every
smooth nonzero-P state. Every complete smooth solution again has finite
longitudinal displacement and zero longitudinal mean drift.

More generally any closed GL-invariant completion with this total dilation
balance and an energy bound on all non-center dilation charge has bounded
P^T X and cannot sustain positive longitudinal mean drift. Energy positivity
alone is insufficient; bounded charge on a finite-energy level is the
relevant hypothesis. The optional lift is a consistent closed mathematical
extension with an unlimited zero-energy charge reservoir, not a supplied
finite-resource physical reference. Its identities are analytical claims;
the finite verifier audits only the main fourteen-coordinate model.
