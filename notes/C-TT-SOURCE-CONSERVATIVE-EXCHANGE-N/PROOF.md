# Conservative exchange and the singular TT-square pullback

Status: NON-CANONICAL. Mathematical results: candidate-T, pending review.
Object: C-TT-SOURCE-CONSERVATIVE-EXCHANGE-N. Owner lock: #929.
Basis: Public Canon v83, 51dee9705628e0c9f7bfc7082df46af46ed314b3.
No Canon owner, gate, physical source, or numerical r_T is closed here.

## 1. Exact scope and declared choices

The construction is an L1 mathematical extension of the selected v83 hybrid
functional. Its trial output is x, not the registered physical TT variable.
The new choices are a second field y, a reciprocal quadratic interaction,
g=1/5, equal kinetic weights, and a prepared source with x_0=x_1=0.
The coefficient 1/5 is fixed, not fitted, but is NOT derived from J.
The original ten K1 words and their two local initial squares are unchanged.
This supplies a source-dependent mathematical map, not an occurrence law or
a native-U realization of the extra field. U itself is never modified.

The graph, time cells and homogeneous clock convention are the selected v83
ones. No finite vertex is identified with a point of continuous space.
The construction is not claimed to be a full gravitational action or an
all-order gauge theory. Its conservation law is the explicit identity below.

## 2. Graph and independent variables

Let X=(Z/5)^3. Edges have tail z and head z+k e_a, with a=1,2,3 and k=1,2.
Set Bf=f(head)-f(tail), w_1=29/324, w_2=65/324, W=diag(w_e), L=B^T W B.
Both inner products have the common normalization 1/25; hence V0=<1,1>=5.
The graph is connected, L is symmetric nonnegative, and ker L is constants.
Pi0 subtracts the spatial mean. L is rational and invertible on mean-zero
vertex fields. K_E=ker B^T contains the entire co-closed edge space.

Use rational vertex fields x_n,y_n, n>=0. For finite endpoint T>=2, fields
are defined on 0,...,T. Half-slice tau and ell are mean-zero vertex fields;
p_m belongs to K_E and N_m is an unrestricted edge field, 1<=m<T.
All variables remain independent until variation. Endpoint and finite-support
conventions are those of the v83 action. The infinite-time statement means
compatible finite restrictions and stationarity against finite-support
variations, not convergence of an infinite numerical action sum.

For a word w=(w_0,w_1,w_2,w_3), write u_t=w_(t+2)-w_t, t=0,1, and

    H_t(r)=(delta_(r,u_t)+delta_(r,u_t+1))/2,
    x_0=x_1=0,          y_t(z)=H_t(z_3), t=0,1.

The domain is exactly the ten words of DEF-K1-LINEAR-METRIC. No statistical
mixture or physical preparation is inferred from this finite domain.

## 3. Source and field follow one action

With Delta z_n=z_(n+1)-z_n and g=1/5, freeze

    A0=(1/4) sum_n [||Delta x_n||^2+||Delta y_n||^2
       -<x_n,L x_n>-<y_n,L y_n>-g||x_n-y_n||^2].

Put R_L z_n=z_(n+1)-2z_n+z_(n-1)+L z_n. Time summation by parts and
self-adjointness of L give the independent interior equations

    R_L x_n=g(y_n-x_n),          R_L y_n=g(x_n-y_n).

More precisely, the variational covectors are -F_x/2 and -F_y/2, with
F_x=R_L x+g(x-y) and F_y=R_L y-g(x-y). The second equation is not an
independently imposed energy ledger: it is the other variation of A0.

On the prepared domain, x_2=g y_1. Every y_1 has two entries 1/2 in its
planar profile. Thus x_2 has two entries 1/10 and is nonzero for every word,
although both initial x slices vanish. The source already changes at that
step: y_2=(2I-L-gI)y_1-y_0. Energy transfer is reciprocal and reversible;
no irreversible damping or escape to infinity is asserted on the finite torus.

There is a useful exact retention identity. Set s=x+y and d=x-y. Then

    R_L s=0,                R_(L+2gI) d=0.

The prepared s has exactly the original K1 initial pair, so s is the original
K1 history. This does not identify x alone with that existing history.

## 4. Action-derived energy and local work cancellation

For any real vertex field z define, with q_z,m=z_(m+1)-z_(m-1),

    e[z]_(n+1/2)(v)=(Delta z_n(v))^2/2
       +(1/4) sum_(edges e incident to v) w_e (Bz_(n+1))_e (Bz_n)_e,
    j[z]_m(e)=(w_e/4)(Bz_m)_e [q_z,m(tail e)+q_z,m(head e)].

The kinetic difference is q_z Delta_c^2 z/2. For each edge, the difference
of its endpoint-split spatial term plus its incidence current is exactly
the corresponding endpoint contribution to q_z Lz/2. Therefore, off shell,

    Delta e[z]+B^T j[z]=q_z R_L z/2.

Now polarize the action's interaction potential, not an unexplained remainder:

    e_int,n+1/2=(g/2)d_(n+1)d_n,
    e_tot=(e[x]+e[y]+e_int)/2,
    j_tot=(j[x]+j[y])/2,
    E=<1,e_tot>.

The interaction product is pointwise. Its difference is

    Delta e_int=(g/2)d_n(q_x-q_y).

Consequently the complete off-shell identity is

    Delta e_tot+B^T j_tot=(q_x F_x+q_y F_y)/4.

Both Euler equations imply exact pointwise conservation, and summing vertices
implies E is constant. No probability, continuum approximation, projection
of a failed component or unaccounted energy bank occurs. The pointwise
interaction and endpoint-polarized local energies need not be nonnegative.

Deleting e_int is not innocuous. At word 0101 and interior time 1, the
five-site conservation defect becomes

    (481/43200,481/43200,0,0,0).

The full expression has zero defect on the same data. Removing reciprocal
response instead violates the y Euler equation already on the initial pair.
These are negative controls, not new Canon F claims.

## 5. Complete hybrid constraint representative

Retain the v83 continuous variables chi=log a and nu>0, time cells
I_n=[n,n+1], eta_n=integral_(I_n)nu(t)dt, and lambda=216 pi. Define

    P_m=WB(tau_(m+1/2)-tau_(m-1/2))+p_m,

    A=A0+sum_n[-(eta_n-1)E_n+2<ell,L tau>-<ell,e_tot>]
         +sum_m[2<N_m,P_m>+<N_m,j_tot,m>],

    S=S_FRW[rho_m]+A/(2 lambda),
    S_FRW[rho_m]=V0 integral dt nu exp(3chi)
                  [-(3/lambda)(dot chi/nu)^2-rho_m(chi)].

On a solution of the reciprocal equations select

    tau_(n+1/2)=(L|mean-zero)^(-1)Pi0 e_tot,n+1/2 /2,
    p_m=-j_tot,m/2-WB(tau_(m+1/2)-tau_(m-1/2)),
    ell=0,              N=0,              nu=1.

The ell equation is 2L tau=Pi0 e_tot. The N equation is 2P+j_tot=0.
Taking B^T of the displayed p and using the difference of the two scalar
constraints gives

    B^T p=-(B^T j_tot+Pi0 Delta e_tot)/2=0,

because Delta e_tot=-B^T j_tot is mean zero. Thus p genuinely belongs to
its prescribed variation space; no nonconserved component is projected away.
All harmonic/coexact currents are retained in p. Variation of p in K_E gives
Proj_(K_E)N=0, satisfied by N=0. The tau variation is proportional to
L ell+B^T W(N_n-N_(n+1)), including the inherited zero endpoint shifts,
and also vanishes. The x and y equations reduce to those of A0 only AFTER
variation, since eta=1 and ell=N=0 at the representative.

The homogeneous lapse varies through every eta_n. Constant E gives the
ordinary integral source -integral E delta nu, with no cell-boundary impulse.
The two homogeneous equations on the selected proper-time representative are

    3H^2=lambda rho_m+E/(2V0 a^3),
    (6/lambda)dot H+(9/lambda)H^2-3rho_m-partial_chi rho_m=0.

No discrete term depends on chi. For rho_m=0 the explicit all-future solution is

    H0=sqrt(E/30),     F(t)=1+(3/2)H0 t,
    a(t)=F(t)^(2/3),   H(t)=H0/F(t),     nu=1.

Every independent first variation therefore vanishes. This is a mathematical
hybrid solution, not adoption of a new physical geometry. Its effective
homogeneous density scales as a^-3 with zero pressure in this chosen action;
it is not asserted to be a physical radiation equation of state.

## 6. Positivity, all-time existence and exact energies

The spatial block operator on Z=(x,y) is

    M=[[L+gI,-gI],[-gI,L+gI]].

Its orthogonal symmetric/antisymmetric decomposition has operators L and
L+2gI. The one-dimensional nonzero eigenvalues of L are

    lambda_plus=(235+18sqrt(5))/324,
    lambda_minus=(235-18sqrt(5))/324.

The three-dimensional eigenvalues are m lambda_plus+n lambda_minus,
m,n>=0, m+n<=3. They are nonnegative. Since sqrt(5)<9/4,

    max Spec(M)<3187/1080<4.

The only zero mode is the common spatial constant of the two fields. For
this prepared domain its velocity vanishes, because the initial sums of
x+y both equal one. Every other mode has recurrence characteristic
r^2+(mu-2)r+1, with 0<mu<4, and therefore two distinct conjugate unit roots.
This proves boundedness for all times on the prepared domain; no finite
numerical scan is used as an all-time proof.

Set Delta Z=Z_(n+1)-Z_n and bar Z=(Z_(n+1)+Z_n)/2. The conserved energy is

    E=(1/4)[||Delta Z||^2+<Z_(n+1),M Z_n>]
     =(1/4)[<Delta Z,(I-M/4)Delta Z>+<bar Z,M bar Z>].

The expression is nonnegative. On the selected initial pairs it is positive:

    E(w)=E_K1(w)/2+(g/4)<H_1,H_0>.

The exact values are

| abs(u_1-u_0) | Joint E |
| --- | --- |
| 0 | 373/4320 |
| 1 | 3889/25920 |
| 2 | 67/324 |

They include interaction energy and are not the energy of y alone. The
positive root H0 therefore gives a smooth expanding homogeneous function for
all t>=0. All discrete source and auxiliary entries are rational. Recurrence
and Poisson inversion are total and horizon-independent, which proves
uniqueness of the selected representative and prefix compatibility. This
is not uniqueness of every solution of the unrestricted variational problem.

No metric signature estimate for x is asserted, and the old K1 bound is not
transferred to it. Boundedness alone does not prove |x|<1.

## 7. Exact restriction and its non-equivalence to deleting the source

On x=y=h, interaction vanishes and A0 becomes exactly the v83 free action
with coefficient 1/2. Also e_tot=e[h] and j_tot=j[h], so every constraint and
homogeneous term restricts literally to the v83 hybrid functional. Each v83
selected solution lifts to this invariant synchronized subspace.

This is NOT the restriction y=0. If y_0=y_1=0 with x_1 nonzero, then

    y_2=g x_1,

so the reservoir-zero subspace is not invariant. Calling synchronization
'source removal' would be false. Setting ALL initial x and y fields to zero
is invariant and produces no output. Removing the entire interaction from
the theory is a different functional, not an admissible adjustment of g.

## 8. NC4: a naive square pullback does not determine emission

This analytic qualification is distinct from the finite exchange audit.
It addresses a specific proposed identification, not every admissible TT
source and not a fixed native coefficient carrier.

Extend A0 to complex x and y by summing its real and imaginary component
quadratic terms. Sum their energies and currents, but retain exactly one
FRW action, one lapse and one set of auxiliary fields. Keep all source
initial data real. Now attempt the direct pullback

    x=v^2,       v=v1+i v2,
    x_plus=v1^2-v2^2,        x_cross=2v1 v2,

leaving y independent. This matches the FORM of the registered square, but
does not provide its native carrier or physical reading.

Let E_plus and E_cross be the real x Euler covectors of the unpulled action.
The exact finite-dimensional chain rule gives at each site and time

    delta S_pull/delta v1=2v1 E_plus+2v2 E_cross,
    delta S_pull/delta v2=-2v2 E_plus+2v1 E_cross.

At v=0 both vanish, regardless of the nonzero x forcing covector. Thus the
square pullback loses the radiation equation on its zero locus. This is not
a floating-point effect and cannot be repaired by energy conservation alone.

There are two distinct mathematical stationary branches with the SAME
prepared v_0=v_1=0 and y_0,y_1:

1. Emitting branch. Solve the original reciprocal equations and choose a
   complex square root v_n of each rational x_n. The original first variation
   is zero, so every pullback variation is zero. No native-field or globally
   continuous square-root selector is claimed by this pointwise existence.

2. Silent branch. Put v_n=0 for every n and solve

       R_L y_n=-g y_n.

   The y equation and every v variation hold. In the off-shell balance of
   section 4, q_x=0 and F_y=0, so local conservation still holds even though
   F_x=-g y is generally nonzero. The same auxiliary recipe and homogeneous
   construction solve every remaining variation.

The initial total energy is identical on both branches, since it depends
only on the common two initial slices. Hence even their selected homogeneous
FRW background is identical. Nevertheless, at time 2,

    x_2=g y_1 != 0         on the emitting branch,
    x_2=0                 on the silent branch.

Therefore this PARTICULAR square-pulled variational law does not give a
single-valued emission history from the stated data. Retaining the original
x equation by hand would select the emitting branch, but is extra information
not obtained by varying the square-pulled action. A further selection rule
or a regular vector-level dynamics would need its own explicit justification.
The silent branch belongs only to this pulled-back class: it does not satisfy
the original x equation or the original x+y K1 continuation. Requiring either
of those as an additional law is not a consequence of the square pullback.
The result is a candidate-T obstruction to this attempted lift, NOT a Canon
F result or a no-go for TT-SOURCE as a whole.

## 9. What is supplied and what is still missing

Supplied at candidate mathematical status: one nontrivial reciprocal
source-output map, a local action-derived work balance, co-closed momentum
completion without deletion of the zero mode, all-time existence and positive
joint energy, an exact synchronized v83 restriction, and the specific
singular-square-pullback obstruction.

Not supplied: native-U realization of the additional source variables;
selection of g from J; a regular, selected full TT vector-doublet dynamics;
the registered spin-dependent propagation/Regge-Wheeler comparison; physical
source, event or apparatus meaning; an irreversible radiation flux; full GR;
scalar spectrum, r_T, SI calibration or a new physical layer lift.

TT-SOURCE and TT-VECTOR-STATE-NORMALIZATION remain O. The construction proves
that a missing work/current term can be supplied by an actual reciprocal
mathematical dynamics. It also proves why that alone is not the requested
physical TT-source closure.
