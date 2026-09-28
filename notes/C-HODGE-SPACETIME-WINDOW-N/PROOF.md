# Windowed Hodge spacetime, counter clocks, and principal photon sheets

Status: candidate-T mathematical consequences of explicit candidate-D choices.
PUBLIC NON-CANONICAL. No public Canon promotion or physical closure.
Author: A. M. Thorn <thorn@twistj.com>. Owner: #1229.
Preregistration/audit pin: 61c84ad6fecc35332f69ceaf7a8757d808e39d19.
Action layers: the named candidate L1/L2/L5 bridges in PREREG.md only.

## 1. The spacetime carrier is the direct predictive chart

Retain the marked lattice Lambda=Lambda^2 A4, the rational wedge pairing
beta, the integral unimodular step L, and the selected predictive chart E_+.
Work at the real embedding sqrt5>0 of F=Q(sqrt5).
The inherited exact construction gives, in its ordered E basis,

    g = (sqrt5/10) [[3,1,1],[1,3,1],[1,1,3]]
                         direct-sum [-(2+sqrt5)/8].

The spatial block is positive definite: its matrix is 2I+11^T, with
positive eigenvalues 2,2,5. The fourth entry is negative. Thus the form
has signature (3,1), without assigning a Lorentz metric to the failed
rank-four subspaces of Lambda^2 E from the predecessor.

Let i:E->W_F be inclusion and define

    Pi=i(i^T beta i)^-1 i^T beta,       N=I-Pi.

The inherited orthogonal decomposition is

    W_F = E direct-sum N_F,
    E = T direct-sum P_+,
    N_F=P_-,
    T=ker(L^2-3L+I),
    P_+/-=ker(L^10-I) intersect ker(K-/+sqrt5 I).

Here P_+ and P_- are the two-dimensional PERIODIC Hodge planes, not the
full three-dimensional Hodge eigenspaces. E has dimension four, N_F has
dimension two, and beta|N_F is negative definite in this real embedding.
Pi and N commute with L and Q=Lambda^2 C. Both L and Q preserve beta
and Lambda, bijectively. The full real vector space W_R decomposes as
E_R direct-sum N_R, with the same projectors.

Regard E_R as an affine space with differences paired by g. This declares
a flat geometric model. In affine coordinates g is constant, so its
Levi-Civita connection coefficients and curvature vanish. It does NOT
derive a matter-sourced gravitational spacetime.

## 2. Six integer labels are not erased by the real rank-four projection

Galois conjugation sigma fixes rational vectors and exchanges P_- with
P_+. The two planes intersect only at zero. If a rational w satisfies
Pi w=0, then w belongs to P_-, and conjugating shows that the same w
belongs to P_+. Hence w=0. Therefore

    Pi|W_Q is injective, and Pi Lambda is a free abelian group of rank six.

This is compatible with real rank four because Pi is not rational-valued.
The audit checks the equivalent rank-six rational system obtained by
separating the two coefficients of every F-valued matrix entry.

The raw subgroup Gamma=Pi Lambda is NOT locally finite in E_R. Here is a
pigeonhole proof, requiring no claim that Gamma is dense in all of E_R.
The (2m+1)^6 distinct images of the integer cube [-m,m]^6 lie in a fixed
four-dimensional cube of side O(m). For any fixed delta>0, that image cube
has O((m/delta)^4) subcubes of side delta. For large m two distinct images
share a subcube. Their difference is a nonzero Gamma vector of arbitrarily
small norm as delta decreases. Thus zero is an accumulation point.

A real projection alone does not produce a discrete event lattice. Nor can
its real two-dimensional kernel be interpreted as two erased integer labels.

## 3. A fully specified extra rule produces discrete events

Use the compact internal window

    c0=max_{e in {+/-1/2}^6} -beta(Ne,Ne),
    Window={y in N_R: -beta(y,y)<=c0},
    M={Pi w: w in Lambda, Nw in Window}.

This is the additional window selection frozen before computation, not a
claim that J or the native selector forces it. All equality of events is
literal equality in E_R. By section 2, each admitted event retains exactly
one integer label w.

The function -beta(Nx,Nx) is a positive-semidefinite quadratic form on W_R
and is nonzero. Its maximum on the six-dimensional rounding cube
[-1/2,1/2]^6 occurs at a vertex: successively maximize each convex
one-variable quadratic over its interval. Consequently c0>0. On N_R the
form is positive definite, so Window is a compact ball with nonempty
interior. The complete 64-vertex exact evaluation gives

    c0=(4+2sqrt5)/5.

No sign or extremum is determined with floating point.

### 3.1 Uniform separation

Consider two admitted labels w,w' and z=w-w'. Then

    Nz in Window-Window.

For a fixed auxiliary unit ball B in E_R, any difference with Pi z in B
has z in B+(Window-Window), a compact subset of W_R. This compact set
contains finitely many lattice vectors. Every nonzero such z has Pi z!=0
by section 2. The minimum of their nonzero projected norms, capped at one,
is therefore a positive separation constant delta. If the finite set is
empty, use delta=1. This proves uniform separation of all pairs of M,
not merely of a finite test sample. Local finiteness follows.

### 3.2 Constructive covering bound

Let t be the frozen fourth E basis vector, c_t=-g(t,t)>0, and write

    tau(x)=g(t,x)/g(t,t),
    v(x)=x-tau(x)t,
    |v(x)|_t^2=g(v(x),v(x))/c_t,
    ||x||_*=max(|tau(x)|,|v(x)|_t).

This is a positive norm for topology and error bounds; the spacetime
interval remains g. In particular

    g(x,x)=c_t(|v(x)|_t^2-tau(x)^2),       ||t||_*=1.

Define R_t,R_s2,R as in PREREG.md. For every rounding error e in the
six-cube, linearity gives |tau(Pi e)|<=R_t, and convexity gives
|v(Pi e)|_t^2<=R_s2. Since sqrt(a)<=a+1 for a>=0,

    ||Pi e||_* <= R=R_t+R_s2+1.

The exact finite evaluation returns R=10-9sqrt5/5>0. It is a sufficient
covering bound, not an asserted optimal one.

For arbitrary x in E_R, round its six ambient coordinates to an integer
w, with ties toward +infinity. Put e=w-x. Then e is in the closed rounding
cube, Nw=Ne is in Window, and Pi w=x+Pi e. Thus M has covering radius at
most R in ||.||_*. Every point of E_R is within R of an event.

For any positive integer h, apply the same argument to h*x. It gives

    w_h=round(h*x),
    x_h=Pi w_h/h in M_h=M/h,
    ||x_h-x||_*<=R/h.

This is an explicit integer-label approximation, not scalar extension
alone. Each M_h is still uniformly separated and locally finite, with
separation at least delta/h.

### 3.3 Exact retained symmetries

Because L,N commute and L preserves beta,

    -beta(N Lw,N Lw)=-beta(Nw,Nw).

Unimodularity of L gives both inclusions, hence A M=M, where A=L|E.
The same argument proves (Q|E)M=M. These are genuine discrete-set
symmetries. No invariance of M under every Lorentz transformation, arbitrary
translation, or every A5 element on one fixed chart is asserted.

## 4. Causal order and the geometric limit

Declare the sign of t to choose the future cone

    C_+={x: tau(x)>=0, g(x,x)<=0}
       ={x: tau(x)>=|v(x)|_t}.

It is a closed convex pointed cone. The triangle inequality proves
C_++C_+ subset C_+; pointedness means C_+ intersect (-C_+)={0}.
Therefore

    x preceq y iff y-x in C_+

is reflexive, transitive and antisymmetric on E_R and on every M_h.
The opposite time orientation is an alternative mathematical convention;
J does not select the sign in this construction.

For x preceq y, a point z in their causal interval has tau(z-x) between
zero and tau(y-x) and |v(z-x)|_t<=tau(y-x). The interval is closed and
bounded, hence compact. Its intersection with each M_h is finite.

A preserves the form and satisfies

    g(t,A t)/g(t,t)=3/2>0.

It consequently maps the chosen timelike cone component to itself and is
an order automorphism. The order-five symmetry Q cannot exchange the two
time components: the induced permutation has order dividing both five and
two, hence is identity. It too preserves the order.

### 4.1 Specified order convergence, including null boundaries

For fixed future timelike x,y, the positive cone margin

    m=tau(y-x)-|v(y-x)|_t

survives any two rounding errors of norm <=R/h once h>4R/m. For a fixed
spacelike pair the positive margin |v(y-x)|_t-|tau(y-x)| is similarly
stable. A convergent sequence of discrete causal pairs has a causal limit
because C_+ is closed.

For a null causal pair, ordinary rounding need not preserve its order.
Use the preregistered padding instead. Round

    x-3R t/h and y+3R t/h

by section 3.2. The rounded endpoints differ from x,y by at most 4R/h.
Their difference has time coordinate at least tau(y-x)+4R/h and spatial
norm at most |v(y-x)|_t+2R/h. It is future timelike. The same argument
works for any causal pair, including coincident endpoints.

Thus every continuum causal pair is approximated by discrete causal pairs
with endpoint error <=4R/h, while every discrete causal pair is already a
continuum causal pair. Together with the R/h event bound, this supplies the
explicit geometric/order limit claimed here. It does not establish a
quantum-state, field, action, stochastic or measure limit.

### 4.2 Four-dimensional counting growth

Uniform separation puts disjoint balls of radius delta/3 around events.
Comparing their ordinary four-dimensional volumes with an expanded ball
gives an upper count bound C rho^4 for large radius rho. The covering
bound covers the ball of radius rho-R by radius-R balls centered at events
inside radius rho. Volume comparison gives a lower bound c rho^4.

A fixed nonempty timelike diamond has nonempty four-dimensional interior
and is compact. Its homothetic dilates contain and are contained in balls
of radii proportional to rho. The same count bounds apply. Therefore

    count(M intersect B_rho)=Theta(rho^4),
    count(M intersect rho*Diamond)=Theta(rho^4).

These are two-sided growth bounds. They are not an exact asymptotic density,
normalized counting measure, physical four-volume or entropy theorem.
The four-dimensional carrier came from the inherited E chart; the window
ensures its event counts have compatible growth rather than the raw
six-label crowding of section 2.

## 5. The J Lorentz action is not itself event-time advancement

On T, the characteristic relation gives A+A^-1=3I. Metric preservation
implies g(u,A^-1 u)=g(Au,u)=g(u,Au), so

    2g(u,Au)=3g(u,u).

Hence for every u in T,

    g(Au-u,Au-u)=2g(u,u)-2g(u,Au)=-g(u,u).

For timelike u, this displacement is spacelike. The exact primitive
integral future-directed witness selected by the preregistered rational
binary-form algorithm is

    u=(0,-1,1,0,-1,0),
    Pi u=u, Nu=0,
    g(u,u)=-2,
    g(Au-u,Au-u)=2.

Both u and Au are admitted future timelike events. They are not causally
ordered. Thus the claim that every application of the linear J action
advances the same event causally is false in this model. A can act as a
Lorentz transformation on geometric data; treating it as a position update
requires a different law.

## 6. A separate exact cumulative clock exists

Use the explicitly added history rule

    w_0=0, v_0=u,
    w_(n+1)=w_n+v_n,
    v_(n+1)=L v_n,
    X_n=Pi w_n.

All coordinates remain integral because L is integral. The rational
hyperbolic plane T is invariant, so w_n,v_n belong to T and have zero
internal component. Every X_n therefore belongs to M. Since A preserves
future orientation and g,

    X_(n+1)-X_n=v_n is future timelike,
    -g(v_n,v_n)=ell^2=-g(u,u)=2.

The polygonal proper time is the sum of segment proper lengths:

    tau_path(n)=n sqrt2,
    tau_path(n)/sqrt2=n.

This gives a mathematically exact counter clock after the declared seed,
path law and normalization have been selected. It is not a derivation of
native U, the already registered METRO-TICK normalization, a physical
clock, or an SI unit. The retained velocity and cumulative position are
explicit additional mathematical state, not hidden inside F5^6.

For the endpoint interval, let r=phi^2, so r+r^-1=3. Decompose u into
the two null eigenlines of A|T. Their geometric-sum factors multiply to

    ((r^n-1)/(r-1))*((r^-n-1)/(r^-1-1))
       = (r^n+r^-n-2)/(r+r^-1-2)
       = r^n+r^-n-2.

It follows that

    -g(X_n,X_n)=ell^2(a_n-2),
    a_0=2, a_1=3, a_(n+2)=3a_(n+1)-a_n.

The audit checks forty prefixes in exact integers. The all-n statement
rests on the geometric-sum identity. At two steps the accumulated squared
proper length is 8, while the endpoint squared interval is 10. The path
is not inertial; accumulated length must not be replaced by chord length.

## 7. The actual principal photon null sheets converge

The independently selected D3 law has nonnegative symbol s and inherited
exact estimate, for r=|k|,

    0<=r^2-s(epsilon*k)/epsilon^2<=(11/27)epsilon^2 r^4.

Its positive principal root is

    Omega_epsilon(k)=(2/epsilon)asin(sqrt(s(epsilon*k))/2).

Assume epsilon*r<=1 and put b=sqrt(s(epsilon*k))/epsilon. Then
0<=b<=r, and, for r>0,

    0<=r-b=(r^2-b^2)/(r+b)<=(11/27)epsilon^2 r^3.

Set z=epsilon*b/2<=1/2. Clearly asin(z)>=z. Also, with a=sqrt(1-z^2),

    d/dz (asin z-z)=1/a-1=z^2/[a(1+a)]<=z^2.

Indeed a>=3/4 on this interval, so a(1+a)>=21/16>1. Integrating from
zero gives asin z-z<=z^3/3. Consequently

    b<=Omega_epsilon<=b+epsilon^2 b^3/12.

Combining these inequalities proves

    -(11/27)epsilon^2 r^3 <= Omega_epsilon(k)-r
                              <= (1/12)epsilon^2 r^3.

At r=0 the assertion is exact. The lower principal sheet is the negative
of the upper. For every fixed Rk and epsilon*Rk<=1, both sheet graphs on
|k|<=Rk are within vertical distance

    (11/27)epsilon^2 Rk^3

of the corresponding graphs Omega=+/-|k|. This proves convergence of the
specified zero sets, including the apex, rather than inferring zeros from
function convergence alone.

The independent audit reconstructs the 60 shell vectors with weights,
second moment 648 I3, and fourth moment 3168 |k|^4. It checks twenty-four
rational root brackets using rigorous rational Taylor intervals for cosine;
no decimal roots, floating-point trigonometry or numerical slope inference
enters the certificate.

### 7.1 Precisely how the Hodge cone is compared

The dual metric g^-1 has signature (3,1). The preregistered coframe class
consists of all real linear isometries F0:E_R^*->R x R^3 with

    -g^-1(xi,xi)=Omega^2-|k|^2,      (Omega,k)=F0 xi.

This class is nonempty by diagonalization of the displayed metric. Fixing
one member pulls back the preceding two graph bounds to the dual Hodge
null cone. The error norm is the pulled-back coframe norm. This comparison
contains an explicit isometry choice; coincidence of Lorentz signatures
does not derive a unique physical identification. At nonzero epsilon the
pulled-back dispersion can depend on the coframe.

The result is local in lifted momenta. It constructs no global map from the
reciprocal torus to an ordinary three-vector, no Lorentz-invariant microscopic
propagator, no dynamics on the windowed M, and no phase or polarization.
In particular the D3 field has NOT been transferred to the event set M.
That missing field/carrier map is a real remaining bridge.

## 8. Choice ledger and disposition

The following ingredients are selected, not forced by the single axiom:

1. the already marked fixed-J chart E_+ and real Hodge sign;
2. its affine interpretation and the future sign of t;
3. the compact internal-ball selection, with the explicit c0 convention;
4. the cumulative-path rule and retained primitive timelike seed;
5. a real coframe for comparison with the separately selected D3 law.

The metric, projection identities, exact window value, integer clock
identities, local finiteness, causal order, counting exponent and stated
geometric/null-sheet error bounds are mathematical consequences after
these choices. They do not make the choices disappear.

This supplies one explicit flat mathematical spacetime construction from
the surviving rank-six Hodge lattice, with finite causal intervals and a
controlled continuum approximation. It does not identify that lattice with
native F5^6, select native events, derive a physical probability, provide
matter/curvature coupling, or close the photon massless/global-carrier
owners. No Canon status changes.

Background only: the compact-window projection method is standard in
aperiodic-order mathematics; see the elementary projection-set discussion
in On Sampling and Interpolation by Model Sets (2020), section 2,
https://doi.org/10.1007/s00041-020-09742-w . The separation and covering
arguments used here are written out above. No external theorem is invoked
to bridge TWIST-J physical layers or to supply an unproved density limit.
