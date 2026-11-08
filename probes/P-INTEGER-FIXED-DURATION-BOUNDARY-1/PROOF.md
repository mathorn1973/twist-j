# Stationary scalar histories, boundary data, and lapse constraints

Status: PROSPECTIVE analytical proof.
Scope: NON-CANONICAL NEW_DECLARED L1, scalar normal form, force a=0.
Ownership: https://github.com/mathorn1973/twist-j/issues/1668
No scientific program or fixture was executed to prepare this proof.

The purpose is to classify the information that survives scalar lapse
redistribution in the completed scalar model. A mathematical invariant is
not thereby a physically prepared or measured observable. No metric,
gravitational force, or new bulk interaction is introduced.

## 1. Defined carrier and previously established identities

Let `x=(h,chi)` be a real six-vector, with five components in `h`. Rational
vectors form the exact finite-audit subcarrier. Let

    e=(1,1,1,1,1), v=(e,0), ell=(1,-1,0,0,0), g=1/324,
    (324 L h)_r=188 h_r-29(h_(r-1)+h_(r+1))
                           -65(h_(r-2)+h_(r+2)),
    V=[[L,-g ell],[-g ell^T,1]],
    C=I_6-V/2, D=I_6-C^2,
    K=[[0,I_6],[-D,0]], M0=[[C,I_6],[-D,C]],
    G=diag(D,I_6), H(q,p)=(p^T p+q^T Dq)/2.

Indices of the five-site spatial operator are modulo five. The matrices
are fixed data, not a metric selected in this module. Their previously
proved identities include

    C=C^T, D=D^T, [C,D]=0, C^2+D=I,
    ker D=span(v), D positive definite on v^perp,
    [M0,K]=0, M0^T G M0=G, K^T G+G K=0.             (1)

In `M0^T G M0`, the superscript denotes transpose. Below, an integer
power of a matrix will be explicitly called a power to avoid confusion.

The bounds that will be used for chart regularity are

    0 <= V <= (327/324)I,
    321/648 <= eigenvalue(C) <= 1,
    ker(I-C)=span(v).                               (2)

For example, these follow from the complete-graph bound on the weighted
Laplacian and the estimate

    (143/324)||h_perp||^2+(323/324)chi^2 <= x^T Vx
       <= (327/324)||h_perp||^2+(325/324)chi^2.

Define the entire phase maps

    R(s)=exp(sK), M(s)=M0 R(s)
        =[[U(s),B(s)],[-D B(s),U(s)]].

Their blocks commute and are symmetric, with

    U(0)=C, B(0)=I, B'=U, U'=-D B,
    U^2+D B^2=I.                                   (3)

On a regular configuration chart, `det B(s)!=0`, put

    E(s)=B(s)^(-1), A(s)=E(s)U(s),
    F_s(q,Q)=(q^T A(s)q+Q^T A(s)Q)/2-q^T E(s)Q.

The generating equations and parameter derivative are

    p=-partial_q F_s=E Q-Aq,
    P= partial_Q F_s=AQ-Eq,
    (Q,P)=M(s)(q,p),
    partial_s F_s=-H(q,p)=-H(Q,P).                  (4)

These are exact real analytic identities on regular charts and exact
formal identities near zero. No finite nonzero exponential is required
to be numerically evaluated by the proposed finite audit.

For `T>=3`, the scalar action is

    S(x,s)=sum_(b=1)^T F_(s_b)(x_(b-1),x_b)+Ebdry,
    Ebdry=(x_0^T Vx_0+x_T^T Vx_T)/4.

The endpoints are fixed in the variational problem. The different action
`S_E=S+Efixed sum_b s_b` uses an independently declared real constant
`Efixed`. The endpoint term does not affect any interior or lapse equation.

## 2. Fixed total lapse is not an energy constraint

At an interior vertex let `pL_n` be the outgoing momentum of the left
bond and `pR_n` the incoming momentum of the right bond, defined by (4).
The field gradient is exactly

    partial_(x_n) S=pL_n-pR_n.                      (5)

Thus field stationarity matches the momenta. A common phase point
`z_n=(x_n,p_n)` then exists at every vertex and satisfies

    z_b=M(s_b)z_(b-1).                              (6)

Every map in (6) preserves `H`, so every link has the same energy,
denoted `Ehistory`.

If all bond lapses are varied independently, (4) gives

    partial_(s_b) S_E=-Ehistory+Efixed.

Consequently the full stationary problem for `S_E` imposes
`Ehistory=Efixed`. In particular the unchanged action `S` imposes zero
energy. This is the independently varying-lapse problem.

Now consider the different problem in which the total lapse

    Lambda=sum_b s_b

is held fixed before variation. Every allowed infinitesimal lapse change
has `sum_b delta s_b=0`. At a field-stationary history,

    delta_s S_E=(-Ehistory+Efixed)sum_b delta s_b=0.  (7)

Thus fixed-total-lapse variation adds no energy equation to field
stationarity. The added term `Efixed Lambda` is constant in this problem
and cannot select the history's energy. Equivalently, constrained lapse
variation only asks that all link energies be equal, which already
follows from (6).

One may first solve the independently varying-lapse problem `S_E` and
then classify its solutions at a specified total lapse. That operation
does retain `H=Efixed`. It must not be confused with fixing the total
lapse in the action before taking its variations.

## 3. Complete quotient in phase space

Fix a horizon `T`. A phase history means real data
`(s_1,...,s_T;z_0,...,z_T)` satisfying (6). An energy-constrained phase
history additionally satisfies `H(z_0)=Efixed`. No individual chart
regularity is required to define the entire phase maps themselves.

For a real vertex parameter `theta` with `theta_0=theta_T=0`, define

    s'_b=s_b+theta_b-theta_(b-1),
    z'_n=R(theta_n)z_n.                              (8)

Commutation of `M0` and all the `R` factors proves that (8) preserves
(6). It preserves energy and both endpoint phase points as well.
The parameters compose by addition.

The quantities `z_0` and `Lambda` are invariant. They form a complete
set of orbit labels: two phase histories at the same horizon are
equivalent under (8) if and only if they have the same initial phase
and total lapse.

To prove completeness, put

    a_n=sum_(b=1)^n s_b, a_0=0.

Iteration of (6) gives

    z_n=(M0 to the power n) R(a_n) z_0.              (9)

For another history with the same `z_0,Lambda`, choose
`theta_n=a'_n-a_n`. Then `theta_0=theta_T=0`, its difference gives
exactly `s'_b-s_b`, and (9) gives exactly `z'_n=R(theta_n)z_n`.
Conversely (8) manifestly leaves `z_0,Lambda` unchanged. The action
is free on the full history data: if the lapse array is unchanged,
then `Delta theta=0`, and the endpoint conditions force `theta=0`.

An explicit family of invariant phase coordinates is

    Z_n=R(-a_n)z_n=(M0 to the power n)z_0.            (10)

These are well-defined mathematical observables of the histories. Every
function constant on phase-gauge orbits factors through `(z_0,Lambda)`
at fixed `T`. There is no additional orbit invariant stored solely in
the distribution of lapse among the bonds.

Equation (10) uses the existing phase map and a temporal prefix of the
lapses. It is an observable construction, not a new claim that a local
action contains a prefix inverse, and not a physical readout mechanism.

## 4. Full phase equivalence versus paths in one configuration chart

Let

    Zbad={s in R : det B(s)=0}.

The determinant is real analytic and equals one at zero. Therefore its
real zeros are isolated and form a countable set. Every phase orbit at
every real total lapse has a representative whose individual bonds are
all regular when `T>=2`: choose `s_1=a`, `s_2=Lambda-a`, all remaining
`s_b=0`, with

    a not in Zbad union (Lambda-Zbad).

Such an `a` exists because the excluded set is countable. Equation (9)
then produces a regular configuration representation of the orbit.

This does not create a global type-1 generating chart. The full phase
equivalence on regular representatives means the restriction of the
orbits (8): endpoints of the equivalence are regular, while a phase
interpolation between them may cross a configuration-chart singularity.

A narrower equivalence can instead require a continuous gauge path
whose every bond remains regular at every point. Each connected component
of `R minus Zbad` is an interval. Under that narrower equivalence each
bond's interval label is invariant, because a continuous real path cannot
cross a removed value. Conversely, if two representatives have the same
`z_0,Lambda` and the same interval label for every bond, the straight
interpolation of their lapse arrays remains in those intervals and keeps
the total fixed. Applying (9) supplies a continuous regular gauge path.

Thus the narrower orbit classification is exactly `(z_0,Lambda)` plus
the ordered list of individual chart-interval labels, subject to their
nonempty fixed-sum domain. These extra labels are absent from the full
phase quotient. Whether to identify different such chart sectors is an
explicit equivalence choice, not a conclusion obtained by overlooking
the chart singularities.

## 5. Complete boundary and energy classification

For fixed `T,Lambda`, write the composite map as

    P_(T,Lambda)=(M0 to the power T) R(Lambda)
       =[[U_T,B_T],[-D B_T,U_T]].                    (11)

Its blocks are real symmetric functions of `C,D`, and satisfy the same
identities as (3), with parameter derivative taken in `Lambda`.
For fixed configuration endpoints `q_-=x_0`, `q_+=x_T`, the boundary
condition is exactly

    B_T p_-=d, d=q_+-U_T q_-.                        (12)

The full phase quotient is therefore completely classified by solutions
of (12). To impose the independently declared energy sector, additionally
require

    ||p_-||^2=2Efixed-q_-^T Dq_-.                    (13)

If `d` is not in `range(B_T)`, there are no solutions. Otherwise let
`p_*` be the unique solution of (12) orthogonal to `ker B_T`. Every
solution is uniquely `p_-=p_*+k`, where `k in ker B_T`. Orthogonality
reduces (13) to

    ||k||^2=rho^2,
    rho^2=2Efixed-q_-^T Dq_- - ||p_*||^2.            (14)

These norms use the Euclidean pairing already fixed in the action and
Hamiltonian, not a newly selected physical metric. Equations (12)-(14)
give the complete classification over real states:

- a failed range condition or `rho^2<0` gives no orbit;
- `rho^2=0` gives the single orbit with `p_-=p_*`;
- `rho^2>0` and `ker B_T={0}` gives no orbit;
- `rho^2>0` and `dim ker B_T=r>=1` gives a sphere of distinct orbits
  of dimension `r-1`, with center `p_*` in the initial-momentum space.

For `r=1`, the last case is exactly two orbits. Distinct points on that
sphere cannot be related by endpoint-fixed gauge: their initial momenta
are different, while (8) fixes the entire initial phase.

On a regular composite boundary chart, `B_T` is invertible. There is
exactly one field-stationary phase orbit for each configuration endpoint
pair and fixed total lapse, with

    p_-=B_T^(-1)(q_+-U_T q_-).

Its energy is a definite function of those boundary data. It belongs
to a separately fixed energy sector precisely when that function equals
`Efixed`. Thus endpoint data, total lapse, and energy are not independent
free labels even when every individual bond is regular.

## 6. The gauge-invariant boundary action and response

When `B_T` is invertible, define

    E_T=B_T^(-1), A_T=E_T U_T,
    W_(T,Lambda)(q_-,q_+)
      =(q_-^T A_T q_-+q_+^T A_T q_+)/2-q_-^T E_T q_+.

For any regular distribution of the same total lapse, the stationary
value of the sum of bond actions equals `W_(T,Lambda)`. To see this,
the boundary derivatives of the stationary sum are `-p_-` and `p_+`
by (4), and the composite map (11) has precisely those generating
derivatives. Their difference is independent of the endpoint fields.
Both are homogeneous quadratic and vanish on the zero history, so the
difference is zero. Uniqueness of the interior stationary history here
follows from invertibility of `B_T`: a homogeneous variation with zero
configuration endpoints would have `B_T delta p_-=0` and is therefore
zero everywhere by the invertible phase evolution.

Consequently the stationary action is exactly

    W_(T,Lambda)+Ebdry,

or `W_(T,Lambda)+Ebdry+Efixed Lambda` for the separately declared
energy-shifted action. It is independent of lapse distribution.
The boundary momenta and mixed response are

    p_-=E_T q_+-A_T q_-,
    p_+=A_T q_+-E_T q_-,
    partial_(q_-) partial_(q_+) W=-E_T.             (15)

This supplies a definite invariant response operator already determined
by the original linear phase dynamics. Symmetry of `E_T` is the exact
reciprocity statement; it is not a derivation of gravitational metric
response or new interaction strength.

The momenta in (15) are the bond phase coordinates. If boundary fields
are differentiated in the full stationary action, its fixed-endpoint
term must also be differentiated: the two gradients are
`-p_-+V q_-/2` and `p_++V q_+/2`. This known endpoint correction does
not alter the mixed response `-E_T` or any fixed-endpoint equation.

Differentiating (11) in the total lapse gives `P'=K P`. The same
calculation as (4), now for the composite generating function, gives

    partial_Lambda W_(T,Lambda)=-H(q_-,p_-).         (16)

Varying the total lapse in the energy-shifted stationary action therefore
recovers `H=Efixed`; holding the total fixed removes exactly that equation.
This is the boundary form of the distinction in Section 2.

## 7. A rational regular boundary chart at T=3, total lapse zero

At `T=3,Lambda=0`, direct block multiplication gives

    U_3=4C^3-3C,
    B_3=4C^2-I=(I-V)(3I-V).                         (17)

These matrices are rational. Their regularity can be proved exactly,
without testing an exponential or fitting a numerical eigenvalue.

The nonzero eigenvalues of the five-site circulant `L` are

    lambda_+=(235+18 sqrt(5))/324,
    lambda_-=(235-18 sqrt(5))/324,

each with multiplicity two, and the remaining eigenvalue is zero.
These follow from the two conjugate Fourier-mode pairs. Both are
strictly less than one, since `sqrt(5)<3` gives
`235+18 sqrt(5)<289<324`. Therefore `A0=I_5-L` is positive definite.
In the block matrix

    I_6-V=[[A0,g ell],[g ell^T,0]],

the scalar Schur complement is

    -g^2 ell^T A0^(-1)ell < 0.                      (18)

It is strictly negative because `ell!=0` and `A0` is positive definite.
Thus `I-V` is invertible. Also `3I-V` is positive definite by (2),
so (17) is invertible. Congruence by Schur elimination gives I-V exactly
five positive directions and one negative direction. Since 3I-V is
positive and commutes with I-V, their product B3 has the same inertia.
This proves regularity of the zero-total
three-bond boundary chart for arbitrary endpoint fields.

An optional exact rational certificate for (18) follows by resolving
`ell` into the two Fourier pairs. Its squared norms in those pairs
are `1-sqrt(5)/5` and `1+sqrt(5)/5`, respectively. Hence

    ell^T A0^(-1)ell
      =324[(1-sqrt(5)/5)/(89-18 sqrt(5))
             +(1+sqrt(5)/5)/(89+18 sqrt(5))]
      =46008/6301,
    -g^2 ell^T A0^(-1)ell=-71/1020762.               (19)

No scientific fixture was evaluated in this derivation. At zero lapse,
the histories `z_n=(M0 to the power n)z_0`, their endpoint inversion
using (17), their energies, and their quadratic boundary actions are
all rational for rational initial phases. Formal gauge transformations
can audit nearby identities coefficientwise without evaluating a
finite nonzero exponential.

## 8. A regular representation of an exact two-orbit caustic

Take `T=3,Lambda=-3`. The full composite upper-right block has kernel
exactly `span(v)`. This claim concerns every mode of the defined carrier,
not merely the explicitly prepared uniform histories.

To prove it, diagonalize the symmetric `C`. On a nonuniform mode its
eigenvalue obeys `0<c<1` by (2). Write

    c=cos(phi), 0<phi<pi/2, omega=sin(phi)>0.

On that two-dimensional phase plane, the baseline map and relative flow
have the oscillator forms

    M0=[[cos(phi),sin(phi)/omega],
         [-omega sin(phi),cos(phi)]],
    R(s)=[[cos(s omega),sin(s omega)/omega],
           [-omega sin(s omega),cos(s omega)]].

Thus the eigenvalue of the composite block `B_(3,-3)` is

    sin(3(phi-sin(phi)))/sin(phi).                   (20)

It is strictly positive: `phi>sin(phi)` for `phi>0`, while

    0<3(phi-sin(phi))<3(pi/2-1)<pi.

The last inequality uses only `pi<6`. On the uniform phase plane,
`C=1,D=0`, so the baseline is a unit shear and the relative map is
a shear of size `s`. The composite shear has size `T+Lambda=0`.
Therefore `B_(3,-3)v=0`, and (20) proves

    ker B_(3,-3)=span(v).                            (21)

The lapse distribution `(-3,0,0)` is a regular representation of
these histories. The zero-lapse links have `B(0)=I`. On a nonuniform
mode the first link has

    B(-3)=sin(phi-3 sin(phi))/sin(phi).

Its numerator is strictly negative. Indeed concavity of sine on
`[0,pi/2]` gives `sin(phi)>=2phi/pi`, so `phi-3 sin(phi)<0`
because `pi<6`; also `phi-3 sin(phi)>-3>-pi`. Thus this angle lies
strictly between `-pi` and zero. On the uniform mode, `B(-3)=-2`.
Consequently the full `B(-3)` is negative definite and invertible.
There is no individual-link chart singularity in this representation,
even though its composite boundary chart is singular.

Now fix `q_-=q_+=0` and `Efixed=5/2`. Equations (12) and (21)
force `p_-=a v`, and the energy condition is `5a^2/2=5/2`.
There are exactly two phase-gauge orbits, with `a=+1` and `a=-1`.
Both have the following rational representatives:

    s=(-3,0,0),
    q_n=a*(0,-2,-1,0)_n v,
    p_n=a v, n=0,1,2,3.                             (22)

The two histories have the same configuration endpoints, total lapse,
energy, and lapse distribution. They are inequivalent because their
initial momenta differ. The invariant `v dot p_-/5` takes values
`+1` and `-1` and separates them.

Even the stationary action does not separate this pair. On the uniform
subspace, a regular link has action
`||Q-q||^2/[2(1+s)]`. For (22) its sum is
`H sum_b(1+s_b)=H(T+Lambda)=0`; the fixed endpoint term is also zero.
The two energy-shifted actions both equal `Efixed Lambda=-15/2`.
This is a concrete reason not to replace the complete phase invariant
by endpoint configuration, energy, or action value alone.

Negative lapses are admitted by this mathematical example. It lies
outside the connected zero-centered configuration chart for its first
bond. It does not show that a separately imposed positive-lapse or
single-chart physical preparation admits the same history. Both
representatives in (22) nevertheless use the same chart intervals,
so their inequivalence holds for both equivalence notions in Section 4.

## 9. What this module decides and what remains open

The proof classifies the stationary scalar model's
full phase quotient, its regular and caustic boundary fibers, and the
effect of genuinely independent lapse variation. It provides an
explicit invariant boundary response and an exact example where common
configuration endpoints, energy, and total lapse fail to determine one
orbit. These statements have content beyond finding additional Ward
coefficients, while remaining consequences of the same fixed linear
dynamics.

They do not select an energy sector, physically prepare endpoints,
identify a measurable clock, impose a lapse orientation, or choose
whether different chart sectors should be physically identified. A
physical reading of the invariant coordinates and momenta needs its own
declared source, output, and equality. The horizon is fixed in the
quotient theorem; changing its number of baseline `M0` steps is not
declared to be gauge.

No nonlinear gravitational bulk law, metric selection, source coupling,
native-U realization, completion of all original auxiliary coordinates,
or cross-layer lift follows from this classification. Those remain
separate questions. The prospective six-file publication and readback
required by PREREG must precede every scientific execution or import.
