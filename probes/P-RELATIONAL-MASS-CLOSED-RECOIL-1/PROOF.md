# Closed recoil, clock-calibrated mass ratios and the native reading boundary

Status: prospective analytical draft, NON-CANONICAL, NEW_DECLARED L1.
All derivations are analytical. No scientific program or finite-fixture
execution was used to obtain them. Previously completed binding and boost
audits are inputs, not repeated here.

## 1. Scope and assumptions

Retain each internal carrier z_i=(G_i,Pi_i,r_i,rho_i), with canonical form
theta_i=tr(Pi_i dG_i)+rho_i^T dr_i and

    h_i=tr(G_i Pi_i G_i Pi_i)/2
          +sqrt(rho_i^T G_i rho_i)+kappa r_i^T G_i^(-1)r_i,
    j_i=2G_i Pi_i+r_i rho_i^T.

Its admitted elliptic sector has complete flow and bounded positive proper
separation. The known minimum at kappa=3 has h=10. A second explicit
minimum h=45 is proved below. Internal phases remain arbitrary.

The inherited, explicitly declared free collective law is

    epsilon_i=sqrt(h_i^2+c^2P_i^T gamma P_i),              (1)

with a common fixed SPD inverse metric gamma, common c>0, canonical
center pairs (X_i,P_i), and rest-energy normalization epsilon_i(P_i=0)=h_i.
This is conditional mathematics of the new model, not a derivation from U.

Use a smooth center-only interaction W(X_A-X_B), independent of internal
states and time. It closes the momentum/energy exchange autonomously.
It does not by itself supply Lorentz-local interaction, physical detectors
or a native preparation. A finite, noninteracting stable spectator C can
provide a common clock and origin; it does not derive gamma.

## 2. A positive free-center result, including spin

In orthonormal coordinates x=gamma^(-1/2)X, p=gamma^(1/2)P, transform
internal variables canonically into the same basis and suppress tildes.
Put R=[[0,-1],[1,0]], S=tr(jR)=j12-j21 and H=sqrt(h^2+c^2p^2).
The inherited free generators are

    K=(H/c^2)x-S Rp/(H+h), L=x1p2-x2p1+S,
    {K_i,p_j}=delta_ij H/c^2, {K_i,H}=p_i,
    {K1,K2}=-L/c^2, {h,K_i}={S,K_i}=0.

The canonical x alone fails the free worldline condition when S!=0.
Define instead the explicitly specified center reading

    Y=x+g S Rp, g=c^2/[h(H+h)].                          (2)

It is smooth for h>0 and satisfies

    {Y_i,p_j}=delta_ij,
    {Y_i,H}=v_i=c^2p_i/H,
    {L,Y_i}=epsilon_ij Y_j, epsilon_12=+1,
    {Y_i,K_j}=Y_j v_i/c^2,
    {Y1,Y2}=c^2S/(hH).                                  (3)

The penultimate identity is the infinitesimal free worldline condition
with the displayed boost-sign convention. Thus a suitable free center
exists inside the model; it is noncanonical rather than an unproved
physical identification of the canonical x.

For completeness, put q=p^2 and b_i=(Rp)_i. Direct differentiation gives

    {Y_i,K_j}=p_i x_j/H
      +S R_ij/(H+h)+S c^2 b_j p_i/[H(H+h)^2]
      -(H/c^2)S[g R_ij+2g_q p_j b_i].

Use p_j b_i=p_i b_j+q R_ij, H^2-h^2=c^2q and
g_q=-c^4/[2hH(H+h)^2]. The R_ij coefficient cancels and the remaining
term is Sg b_j p_i/H, proving (3). Likewise
{Y1,Y2}=2S(g+qg_q)=c^2S/(hH). The other brackets follow directly.

During free motion h,S,P are constant, so Y-x is constant. Their measured
free velocities are exactly equal. Returning to the marked coordinates
means applying gamma^(1/2) to Y; this leaves all proportional velocity
ratios below unchanged.

The collision potential below is explicitly W(X_A-X_B), using canonical
centers. It is not silently replaced by W(Y_A-Y_B). During interaction
the spin shifts can vary with momentum. We claim free-channel readings
and closed canonical interaction, not Lorentz-local collisions of Y.

## 3. Two distinct stable minima at the same kappa=3

Object A is the known minimum

    G_A=I, Pi_A=[[0,-1],[-1,0]], r_A=e1, rho_A=6e2,
    j_A=[[0,4],[-2,0]], delta_A=8,
    (K_A,E_A,V_A,h_A)=(1,6,3,10).

Object B is the new exact state

    G_B=I, Pi_B=[[0,-3],[-3,0]], r_B=2e1, rho_B=24e2,
    j_B=[[0,42],[-6,0]], delta_B=252,
    (K_B,E_B,V_B,h_B)=(9,24,12,45).                      (4)

The inherited sharp lower bound at traceless elliptic charge is

    h>=f(a)=3 kappa^(1/3)a^(2/3)
                      +(a-sqrt(a^2-delta))^2/4,
    a>=sqrt(delta).

It has a unique global stationary minimum. At (4), a=24,b=18,
r^T rho=0 and |r||rho|=48; the reverse-triangle and E=2V equality
conditions are all attained. Directly,

    f'(24)=2(3/24)^(1/3)+(24-18)(1-24/18)/2=0,
    f(24)=45.

Thus h_B>=45 on exact j=j_B. Its equality set is the internal centralizer
orbit of (4): whitening forces perpendicular lengths 2 and 24 with aligned
symmetric parts; a rotation brings it to (4), and undoing whitening at
the same j must commute with j_B. The inherited elliptic condition-number
bound, followed by scalar normalization, makes energy sublevels compact
modulo that centralizer. Conservation of h_B-45 proves nonlinear quotient
stability, by the same minimum-set argument as for A.

The explicit relative-equilibrium generator is

    Omega_B=[[0,-7/2],[1/2,0]], Omega_B^2=-(7/4)I.

It gives Gdot=Pi_B, rdot=e2, rhodot=-12e1 and Pidot=diag(3,-21), exactly
the internal equations. Its labeled period is T_B=4pi/sqrt(7); for A,
T_A=sqrt(2)pi. No differing kappa or physical species assignment is used.

## 4. Closed interaction: finite energy, completeness and preserved binding

Declare

    H_AB=epsilon_A+epsilon_B+W(X_A-X_B),
    theta_AB=theta_A+theta_B+P_A^T dX_A+P_B^T dX_B,       (5)

where W>=0 is smooth, bounded, finite range and has bounded force. Then

    Pdot_A=-grad W, Pdot_B=+grad W,
    Xdot_i=c^2gamma P_i/epsilon_i,
    zdot_i=(h_i/epsilon_i)X_(h_i)(z_i),
    hdot_i=jdot_i=0, P_A+P_B=constant, Hdot_AB=0.         (6)

Each internal object follows its old bound orbit with time parameter
tau_i= tau_i(0)+integral h_i/epsilon_i dt. No internal excitation or
phase-dependent impulse is hidden in this center-only coupling.

Conserved H_AB bounds both center momenta. Center speeds are at most c
in the marked norm and |d tau_i/dt|<=1. Completeness of the internal
flows and bounded center force exclude finite-time breakdown. Thus the
closed interacting flow is complete on the inherited elliptic sectors.
This is an analytic theorem; a finite audit need not integrate trajectories.

Prepare both centers at rest at separation where W=w>0 and the repulsive
force is nonzero. For a strictly decreasing radial bump in the gamma
metric, the initial line is invariant and the objects separate until W=0
in finite time. Initial radial acceleration is positive; accumulated
outward momentum then bounds the remaining outward speed away from zero.
After exit, center motion is free and each internal object stays bound.

Let M=h_A+h_B+w. Opposite outgoing momenta P_A=p,P_B=-p and energy
conservation uniquely determine

    epsilon_A=(M^2+h_A^2-h_B^2)/(2M),
    epsilon_B=(M^2+h_B^2-h_A^2)/(2M),                    (7)
    c^2p^T gamma p=
       [(M^2-(h_A+h_B)^2)(M^2-(h_A-h_B)^2)]/(4M^2).

These endpoint quantities depend on w, not on pulse shape, collision
duration or the initial internal phases. The interacting Hamiltonian (5)
is not claimed to have the full Poincare symmetry of its free sectors.

## 5. Finite-recoil mass ratio read with internal clocks

In any outgoing free window, measured Y velocities equal canonical ones:

    v_A=c^2gamma p/epsilon_A,
    v_B=-c^2gamma p/epsilon_B,
    a_i=d tau_i/dt=h_i/epsilon_i.

Consequently the exact finite-recoil identity is

    |v_A| a_B/(|v_B| a_A)=h_B/h_A=m_B/m_A.               (8)

Any common vector norm gives the same ratio because v_A and v_B are
opposite and proportional. Numeric gamma and c cancel, and so do common
time/length unit choices. Their shared kinematical law and the calibration
of the internal clocks have not thereby been derived.

A clock rate a_i means the locally unwrapped internal phase derivative
divided by its calibrated rest angular frequency 2pi/T_i. A finite free
observation window short enough to track a continuous phase branch suffices.
For longer observation one must retain a cycle count or unwrapped history.
An instantaneous periodic internal state alone is not an unbounded clock.
Different rest periods must be calibrated separately against the same
reference clock used for the recoil comparison. Comparing raw frequencies
without the factors 2pi/T_i would give a different quantity; arbitrary
independent rescalings of the two internal clocks do not cancel in (8).

To realize one actual finite common reference inside the declared model,
include a noninteracting spectator C on the known h_C=10 minimum with
P_C=0. Set H_ABC=H_AB+epsilon_C and add its canonical/internal forms.
Then Y_C is constant and tau_C=t up to origin. Define the genuinely
relative outputs

    R_A=Y_A-Y_C, R_B=Y_B-Y_C,
    a_i=d tau_i/d tau_C.

Equation (8) becomes

    m_B/m_A=
       |dR_A/dtau_C| a_B / (|dR_B/dtau_C| a_A).           (9)

No measured mass value of C enters (9). It is a finite positive-energy
spectator, not an unbounded charge reservoir. Its direct-sum inclusion is
an analytical construction, not a claim of a full enlarged-carrier finite
audit. It supplies a shared origin and local clock but neither gamma nor
a physical detector coupling. The model deliberately lacks the old
diagonal active GL symmetry; no corresponding charge is hidden in C.

Only R_AB=Y_A-Y_B by itself would give v_A-v_B and would not separate the
two individual velocities. The shared-frame comparison, or explicit C in
(9), is therefore part of the preparation/readout contract.

Without clock rates, the raw finite velocity ratio is epsilon_B/epsilon_A.
As w decreases to zero, it tends to h_B/h_A. This limit is taken after
forming the outgoing channel for each fixed w>0; no limit interchange is
assumed. It is a useful alternative to finite-recoil clock calibration.

### Exact rational recoil

Take c=1,gamma=I, the two minima in (4), initial center momenta zero and
X_A-X_B=e1/2. For Q=|X_A-X_B|^2 declare

    W=22 exp[1/3-Q/(1-Q)] for Q<1; W=0 for Q>=1.          (10)

It is C-infinity, bounded and repulsive; W(e1/2)=22 exactly. Total AB
energy is 77, or 87 with spectator C. Equations (7) give exactly

    (epsilon_A,epsilon_B)=(26,51), (P_A,P_B)=(24,-24)e1,
    (v_A,v_B)=((12/13)e1,-(8/17)e1),
    (a_A,a_B)=(5/13,15/17).

The shell and energy checks are rational:

    26^2-24^2=10^2, 51^2-24^2=45^2,
    26+51=77, (26-10)+(51-45)=22.

The clock-calibrated ratio is

    [(12/13)(15/17)]/[(8/17)(5/13)]=9/2=45/10.           (11)

The raw speed ratio 51/26 and kinetic-energy ratio 16/6=8/3 are both
wrong as rest-mass readings. The free Y-x shifts are constant, so neither
changes (11). No rational full-trajectory evaluator is asserted.

## 6. What closed recoil does not select

Allow instead epsilon_i=F_i(h_i,q_i), F_i(h,0)=h, (F_i)_h>0, with
F_i=h_i+b_i(h_i)q_i+O(q_i^2), b_i>0. The same autonomous coupling still
preserves binding, h_i,j_i and total momentum/energy. Weak recoil gives

    v_A=2b_A gamma p+O(|p|^3),
    v_B=-2b_B gamma p+O(|p|^3),
    lim |v_A|/|v_B|=b_A/b_B.                             (12)

Since the internal clock factors tend to one, clock correction does not
remove this weak-response freedom. For F_i=h_i+q_i/(2mu_i), arbitrary
positive mu_i give recoil ratio mu_B/mu_A at the same internal minima.
Choosing mu_A=mu_B gives one rather than 9/2 with closed accounting.
The common inherited boost law selects b_i=c^2/(2h_i); conservation alone
does not. A collision can test that selection, not logically create it.

There is a stronger two-law witness with complete agreement on the
calibration object h=10, including its internal clock at every momentum:

    F_A(h,q)=sqrt(h^2+c^2q),
    F_B(h,q)=sqrt(h^2+c^2 a(h)q),
    a(h)=1+(h-10)^3/12250.                              (13)

For h>0, a(h)>45/49>0 and a'(h)=3(h-10)^2/12250>=0, so both laws
are positive and strictly increasing in h. At h=10, a=1 and a'=0;
therefore F, F_h and F_q all agree for every q>=0. The complete one-object
free Hamiltonian vector fields on that internal-energy level agree, not
merely one observed energy or velocity. The same is true for spectator C.
But a(45)=9/2, so under F_B the rest momentum Hessians of the h=10 and
h=45 objects are both (c^2/10)gamma. Their weak-recoil ratio is one;
under F_A it is 9/2. Internal clock factors tend to one in both weak
limits and cannot disguise the difference. Both interactions retain
complete flow and binding: h is conserved, energy bounds q, and F_h
stays finite on every such compact q interval.

F_B is excluded by the additional common boost premises that selected
F_A. It is not excluded by binding, conservation, complete calibration of
the h=10 object, or unrestricted counter intertwining below. The h=45
recoil is thus a genuine second-object prediction not used to choose a
calibration on h=10.

Even rest trajectories do not select an absolute energy offset. The laws

    epsilon_i=sqrt((h_i+C_i)^2+c^2q_i), h_i+C_i>0,

have the same internal rest vector fields and a corresponding free boost
construction, but inertia ratio (h_B+C_B)/(h_A+C_A). They violate the
explicit normalization in (1), so are not counterexamples to its theorem.
They identify a required energy-calibration premise beyond rest motion.

A complementary finite-momentum discriminator leaves even the rest
momentum Hessian unchanged. Compare F_R=sqrt(h^2+c^2q) with
F_N=h+c^2q/(2h), on q<2h^2/c^2 where (F_N)_h>0. Along a unit momentum
direction, both have E''(0)=c^2/h, but

    h E''''(0)/(3 E''(0)^2)=-1 for F_R, 0 for F_N.

This dimensionless fourth-order difference survives unit changes. F_N
also violates the inherited boost premise away from zero momentum.
Neither comparison is a counterexample to the conditional boost theorem.

## 7. Native representability and a precise relational obstruction

The full native state includes its unbounded counter; a finite-register
recurrence argument is not a theorem about the complete U. The canonical
counter-reading classification supplies conserved onto labels
ell_n:E_n(F5^6)->F5^5 on the origin-zero reachable domain, satisfying
ell_(n+1)d_n=ell_n. For any stipulated set Z and bijection L:Z->Z, every
reader intertwining the full native update with L has the form

    D(n,x)=L^n I(ell_n(x)), I:F5^5->Z arbitrary.          (14)

Conversely every such I gives an exact intertwining. Taking L=Phi_tau
for the complete closed flow (5), or its spectator extension, therefore
gives an exact mathematical reading of that target flow from native U.

Equation (14) also works for every other stipulated complete target and
initialization. It does not select this Hamiltonian, its interaction,
clock calibration, species assignment or mass ratio. Two admitted target
states/laws with different inertial outputs give two exact readers while
U is unchanged. A physical equivalence relation must either identify
those outputs or an independent admissibility rule must select among them.
Intertwining alone cannot establish native physical inertia.

At one fixed common native origin there are at most 5^5=3125 distinct
target initial states in this invertible-target reading class. Therefore
it cannot cover an open continuous momentum-preparation family exactly.
Counter progression does not enlarge that initial menu. Approximation,
growing carriers or other preparations require their own quantitative
contract; finite real-linear span is not surjectivity onto an open set.

There is also a conditional obstruction to hiding the old dilation
problem merely in a new frame or clock. In a closed body/reference model,
assume total momentum zero, a free canonical relative sector (R,p) with
p conserved, and a conserved global dilation trace

    D_total=p^T R+D_internal, |D_internal|<=C_D            (15)

at finite conserved energy. D_internal must include every material
reference and metric degree of freedom. These assumptions must be proved
for the particular extension; total momentum conservation alone is not
relative momentum conservation during an interaction.

For any invertible reference frame A(t), read

    y=A^(-1)R, k=A^T p, k^T y=p^T R.

Let tau(t) be any increasing unbounded clock. If y(tau)/tau->v and
k(tau)->k_infinity, boundedness from (15) forces

    k_infinity^T v=0.                                   (16)

Thus a nonzero coasting velocity with k_infinity=M v for a finite
positive-definite M is impossible under these premises, even with
unbounded frame deformation or nonuniform clock rates.

More locally, with C=A^(-1)dA/dtau and frame-corrected transport
w=dy/dtau+Cy, one has the exact budget

    k^T w=d(p^T R)/dtau,
    |integral_(tau1)^(tau2) k^T w dtau|<=2C_D.            (17)

This does not forbid all growth of proper distance. For R=p=e1,
A=(1+t)^(-1)I,tau=t, one gets y=(1+t)e1,k=e1/(1+t), but w=0.
That kinematic example has growing read distance and vanishing measured
momentum; it is not a claimed Hamiltonian solution or finite-mass coasting.

The marked model (5) does not preserve the old global diagonal GL charge,
so (15) is not silently asserted for it. The finite spectator does not
evade (16) by storing an unbounded hidden charge. A proposed material
reference extension retaining all premises of (15) must confront (16).

## 8. Minimal physical bridge and decisive falsifiers

The positive result is a closed, finite-energy preparation of two stable
composites and an exact dimensionless inertia ratio read from their free
centers and calibrated internal clocks. It needs no prescribed external
force or measured mass anchor, conditional on the common law (1).

A physical identification still requires a target-independent source
preparation; selection of the common Hamiltonian, interaction and energy
normalization; a specified shared frame or material reference; actual
phase/center records with their resolution and finite observation window;
and a test not used to choose the reading. A native continuous preparation
claim needs an approximation or enlargement theorem beyond (14).

Prospective exact falsifiers include:

1. Failure of any free-center identity (3), especially its spin signs.
2. Failure of the B-state minimum/orbit identities in Section 3.
3. Nonzero Hdot_AB, Pdot_A+Pdot_B, hdot_i or jdot_i in (6).
4. Different endpoint energies from (7) at the same h_A,h_B,w, or any
   dependence on initial internal phases under the declared coupling.
5. Failure of the rational endpoint and clock-corrected ratio (11).
6. Calling 51/26 or 8/3 the rest-mass ratio in that finite witness, or
   claiming that relative AB separation alone supplies both velocities.
7. Claiming a globally unbounded clock from one instantaneous periodic
   state without history or a cycle count.
8. Claiming uniqueness from (14), or an exact open preparation family
   from its fixed finite native initial menu.
9. Claiming positive finite-mass coasting while retaining every premise
   of (15)-(16), or claiming (5) is a Lorentz-local interacting theory.

No native-U derivation, empirical particle identification, detector
realization or equality of gravitational and inertial mass is claimed.
The conditional operational ratio is stronger than naming a conserved
energy, while physical selection and readout remain explicit obligations.
