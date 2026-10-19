# Exact scalar-lapse completion and its rigidity

Status: PROSPECTIVE analytical proof.

Scope: NON-CANONICAL, NEW_DECLARED L1, conditional candidate-T, force `a=0`.

This document proves the mathematical statements of `PREREG.md` from its
definitions. It reports no execution, audit outcome, or Canon promotion.
The analytic assertions admit real fields and arbitrary real endpoints on
regular charts. The formal assertions are coefficient identities over the
rationals, with unrestricted rational field coordinates; regular formal
stationary histories may be substituted. Positivity statements concern real
or rational states. They are not assertions about complex states.

## 1. Carrier, positivity, and phase matrices

Let `e=(1,1,1,1,1)`, `ell=(1,-1,0,0,0)`, and `g=1/324`. The ten
oriented edges on five vertices are `r -> r+1` of weight `29/324` and
`r -> r+2` of weight `65/324`, with indices modulo five. They contain
each unordered pair once. For head-minus-tail incidence `B_sp` and the
diagonal weight matrix `W`, define

    L=B_sp^T W B_sp,
    V=[[L,-g ell],[-g ell^T,1]],
    C=I_6-V/2, D=I_6-C^2,
    K=[[0,I_6],[-D,0]], M0=[[C,I_6],[-D,C]],
    J=[[0,I_6],[-I_6,0]], G=diag(D,I_6).

Write `v=(e,0)` and `h=h_perp+mean(h)e`. Since the underlying unweighted
graph is complete, `B_sp^T B_sp=5 Pi0`. Hence

    (145/324)||h_perp||^2 <= h^T Lh
                              <= (325/324)||h_perp||^2.

Also `ell dot e=0`, `||ell||^2=2`, and

    |2g chi ell dot h| <= g chi^2+g(ell dot h_perp)^2
                       <= g chi^2+2g||h_perp||^2.

For `x=(h,chi)` this proves the explicit bounds

    (143/324)||h_perp||^2+(323/324)chi^2 <= x^T Vx
       <= (327/324)||h_perp||^2+(325/324)chi^2.        (1)

Thus `V` is symmetric positive semidefinite, with kernel exactly `span(v)`.
Its eigenvalues on `v^perp` lie in `[143/324,327/324]`, in particular
strictly between zero and four. Since `D=V(I-V/4)`, it follows that

    ker D=span(v), D positive definite on v^perp.      (2)

For example, if `q=q_perp+c v`, (1) gives the uniform lower bound

    q^T Dq >= (143/324)(969/1296)||q_perp||^2,
    H(q,p)=(p^T p+q^T Dq)/2
       >= ||p||^2/2+(143*969)/(2*324*1296)||q_perp||^2.

The matrices `C,D` are symmetric and commute. Their identity `C^2+D=I`
gives, by block multiplication,

    M0^T J M0=J, M0^T G M0=G, [M0,K]=0,
    K^T J+J K=0, K^T G+G K=0.                        (3)

In particular `M0` is invertible, and its phase action preserves `H`.
The traces in the contract can be derived without a spectral calculation:

    tr V=1264/324,
    tr V^2=[5(188^2+2*29^2+2*65^2)+4+324^2]/324^2
          =332360/104976,
    tr D=tr V-tr V^2/4=163223/52488,
    K^2=-diag(D,D), tr K^2=-163223/26244.             (4)

These equalities also show that `K` is not nilpotent.

## 2. Exact generating family

For a formal parameter `s`, set

    R(s)=exp(sK)=sum_(j>=0) s^j K^j/j!,
    M(s)=M0 R(s)=[[U(s),B(s)],[-D B(s),U(s)]].

The same definitions give entire real analytic phase matrices. All their
formal coefficients are rational. Equation (3) proves that `R` and `M`
are symplectic and preserve `G`. The commuting block functions obey

    U'=-D B, B'=U, U(0)=C, B(0)=I,
    U^2+D B^2=I.                                    (5)

The last equation follows either from symplecticity or by differentiating
its left side and using its value at zero. The formal inverse of `B`
exists because `B(0)=I`. On a real chart it exists precisely when
`det B(s)!=0`. Define, distinguishing the coefficient matrix from the
autonomous action,

    E(s)=B(s)^(-1), Acoef(s)=E(s)U(s),
    F_s(q,Q)=(q^T Acoef(s)q+Q^T Acoef(s)Q)/2-q^T E(s)Q.

All these block functions commute with each other and with `C,D`.
They are symmetric. Equation (5) yields

    E'=-Acoef E, Acoef'=-E^2, E^2-Acoef^2=D.          (6)

The type-1 generating equations are

    p=-partial_q F_s=E Q-Acoef q,
    P= partial_Q F_s=Acoef Q-E q.                    (7)

Solving the first equation gives `Q=Uq+Bp`; substitution in the second
and (5) gives `P=-DBq+Up`. Thus (7) generates exactly `M(s)`.
Using (6) in the parameter derivative proves

    partial_s F_s(q,Q)
       =-(q^T E^2q+Q^T E^2Q)/2+q^T Acoef E Q
       =-H(q,p)=-H(Q,P).                            (8)

The equality of the two energies also follows from (3). No field equation
is required for (7) or (8): each regular bond has its own endpoint momenta.

For `x_0,...,x_T`, direct expansion gives

    sum_b F_0(x_(b-1),x_b)+Ebdry
      =1/2 sum_b ||x_b-x_(b-1)||^2
         -1/2 sum_(n=1)^(T-1) x_n^T Vx_n=A(x),
    Ebdry=(x_0^T Vx_0+x_T^T Vx_T)/4.                (9)

The endpoint term is fixed during all variations in this proof.
The additive composition law is `R(s)R(t)=R(s+t)`. The one-link transfer
is `M(s)=M0 R(s)`, with `M(0)=M0`, so it does not obey that same law.

## 3. The first three corrections and uniform temporal locality

Repeated differentiation of (6), at zero, gives

    E(0)=I, E'(0)=-C, E''(0)=I+C^2,
    E'''(0)=-5C-C^3,
    Acoef(0)=C, Acoef'(0)=-I, Acoef''(0)=2C,
    Acoef'''(0)=-2I-4C^2.                            (10)

Consequently, for a single bond `(q,Q)`,

    F'_0=-H_b,
    H_b=(||q||^2+||Q||^2)/2-q^T C Q,
    F''_0=K_b=(C Q-q) dot (Q-Cq),
    F'''_0=T_b=-q^T(I+2C^2)q-Q^T(I+2C^2)Q
                     +q^T(5C+C^3)Q.                (11)

Here `K_b` is a scalar bond expression, distinct from the phase matrix `K`.
Putting `s_b=epsilon alpha_b` in

    S(epsilon)=sum_b F_(epsilon alpha_b)(x_(b-1),x_b)+Ebdry

therefore yields

    S=A+epsilon I+epsilon^2 S2+epsilon^3 S3+...,
    I=-sum_b alpha_b H_b,
    S2=sum_b alpha_b^2 K_b/2,
    S3=sum_b alpha_b^3 T_b/6.                         (12)

At every order a summand involves just the two fields on one bond and
that bond's single lapse. Every mixed derivative with respect to distinct
`alpha_b` is identically zero. This proves the horizon-independent
nearest-bond and bond-separability statements to all formal orders.
No temporal inverse or prefix sum enters the formula. This is locality
on the declared fixed six-component carrier, not a spatial locality
theorem on a variable-size graph or a result about all original auxiliaries.

## 4. Exact raw and adjusted Ward identities

At an interior vertex define the outgoing momentum of its left bond,
the incoming momentum of its right bond, and their difference and mean:

    l_n=pL_n=A_n x_n-E_n x_(n-1),
    r_n=pR_n=E_(n+1)x_(n+1)-A_(n+1)x_n,
    f_n=l_n-r_n, vmean_n=(l_n+r_n)/2,                (13)

where `A_b=Acoef(s_b)` and `E_b=E(s_b)`. Differentiating the total action
with respect to an interior field gives exactly `f_n`. The convention
`f_0=f_T=0` is only for interior tangent operators; it asserts no endpoint
equation of motion.

Let `t_0=t_T=0`. It is convenient first to use independent unscaled bond
parameters `s_b` and the vector field

    V_t s_b=t_b-t_(b-1), V_t x_n=t_n vmean_n.

By (8), summation by parts gives its parameter work as

    sum_b (t_b-t_(b-1)) partial_(s_b)F_(s_b)
      =sum_n t_n[H(x_n,r_n)-H(x_n,l_n)]
      =-sum_n t_n f_n dot vmean_n.                  (14)

This cancels the field work. Thus `V_t S=0` identically off shell.
In variables `s_b=epsilon alpha_b`, the contract's raw generator is
`delta_t=epsilon V_t` on `(x,s)`, namely

    delta_t alpha_b=t_b-t_(b-1),
    delta_t x_n=epsilon t_n vmean_n.                 (15)

It follows that (15) is an exact formal and regular analytic symmetry.
Its coefficients are finite at every field-stationary history in a regular
chart; no division by a field residual is used.

Let `A_t(alpha)` now denote the skew matrix on interior time coordinates
whose upper neighbor entry is

    [A_t(alpha)]_(n,n+1)=alpha_(n+1)(t_n+t_(n+1))/8

and whose lower entry is its negative, with each entry multiplying `I_6`.
All other blocks are zero. For the full gradient (13),

    f^T A_t(alpha) f=0.                              (16)

Therefore adding `epsilon^2 A_t(alpha) f` to (15) preserves the Ward
identity exactly, not merely at a finite order. Endpoint rows are absent.
Equivalently the adjusted unscaled field is

    V_t^adj x=t vmean+A_t(s)f,
    V_t^adj s=Delta t,
    delta_t^adj=epsilon V_t^adj.                     (17)

Expansion of (10) and (13) gives the raw coefficients

    X1_n=t_n(x_(n+1)-x_(n-1))/2,
    X2_n=t_n/2 * {
      alpha_n[-x_n+C x_(n-1)]
      +alpha_(n+1)[x_n-C x_(n+1)]},
    X3_n=t_n/4 * {
      alpha_n^2[2C x_n-(I+C^2)x_(n-1)]
      +alpha_(n+1)^2[(I+C^2)x_(n+1)-2C x_n]}.
                                                               (18)

The displayed `X2` is precisely the predecessor's scalar `Xhom`.
Writing `f=f0+epsilon f1+...`, with `f0=gradient A` and
`f1=gradient I`, the adjusted second and third coefficients are respectively
`X2+A_t(alpha)f0` and `X3+A_t(alpha)f1`. Thus the predecessor's scalar
jet is preserved. The raw fields reach one neighboring time slice; the
adjustment reaches at most two, because it uses neighboring gradients.
These stencil bounds are independent of the temporal horizon.

## 5. Raw commutator, on-shell closure, and the cubic obstruction

The bracket convention is `[V_t,V_s]=V_t V_s-V_s V_t` on coordinate
functions. Here `s` in a subscript denotes the second fixed vertex
parameter, not the bond-coordinate array `s_b`. From (6), direct
differentiation of (13) under the raw `V_t` gives

    V_t l_n=-t_n D x_n
       -[t_n A_n f_n+t_(n-1)E_n f_(n-1)]/2,
    V_t r_n=-t_n D x_n
       -[t_n A_(n+1)f_n+t_(n+1)E_(n+1)f_(n+1)]/2.  (19)

For example, the parameter part of the first derivative uses
`-E_n^2 x_n+A_n E_n x_(n-1)=-D x_n-A_n l_n`.
The neighboring term uses
`D x_n+A_n l_n=E_n r_(n-1)`. Substitution gives (19), including the
endpoint-zero convention. Since the field bracket is
`s_n V_t vmean_n-t_n V_s vmean_n`, its diagonal terms cancel. Restoring
the factors of `epsilon` yields exactly

    [delta_t,delta_s]x_n=-epsilon^2/4 * {
      (s_n t_(n-1)-t_n s_(n-1)) E_n f_(n-1)
      +(s_n t_(n+1)-t_n s_(n+1)) E_(n+1)f_(n+1)}.   (20)

All lapse components of the bracket vanish. The two neighboring block
coefficients in (20) are negative transposes, since `E_b` is symmetric.
Thus it is a skew multiple of the field gradient. It has zero action
work and vanishes on field-stationary histories, but generally not off shell.

At order two the adjustment changes the bracket only by

    [(Delta t) dot partial_alpha A_s
      -(Delta s) dot partial_alpha A_t] f0.

Its upper neighboring entry is

    [(t_(n+1)-t_n)(s_n+s_(n+1))
      -(s_(n+1)-s_n)(t_n+t_(n+1))]/8
       =(s_n t_(n+1)-t_n s_(n+1))/4.                (21)

This cancels the order-two coefficient of (20), for every state and
endpoint-zero parameter pair. It proves strict off-shell commutation
through order two. It does not prove exact commutation of (17).

The failure at order three has a direct closed-form witness. Take `T=4`,
`u=(1,0,-1,0,0,0)`, `x_3=u`, and every other field zero. Set bond
coordinates `s_3=a`, all other `s_b=0`, and vertex parameters `t_1=1`,
`s_2=1`, all other entries zero. In the rest of this witness calculation
write `A=Acoef(a)` and `E=E(a)`. At this state,

    f1=0, f2=-E u, f3=(A+C)u,
    vmean1=0, vmean2=E u/2, vmean3=(A-C)u/2.

For the adjusted unscaled fields, `V_t^adj x=0`, while

    V_s^adj x1=0,
    V_s^adj x2=[E/2+a(A+C)/8]u,
    V_s^adj x3=a E u/8.

The lapse components are respectively `(1,-1,0,0)` and `(0,1,-1,0)`.
Although the displayed first field component is zero at the witness,
its derivatives must be retained: below `s_2` in nearby field formulas
is the second bond coordinate, not the fixed vertex parameter. Nearby
the first field component contains `s_2 f2/8` for
`V_s^adj`, and `vmean1+s_2 f2/8` for `V_t^adj`. Consequently

    V_t^adj(V_s^adj x1)=E u/8,
    V_s^adj(V_t^adj x1)=E u/8+a(A+C)u/16,
    [V_t^adj,V_s^adj]x1=-a(A+C)u/16.                (22)

The remaining field components of this bracket are zero. To check
them without inferring derivatives from a zero value, the nearby
formulas are `V_t^adj x2=-s_2 f1/8`, `V_t^adj x3=0`, and
`V_s^adj x3=-s_3 f2/8`. At the witness `f1=s_2=0` and
`V_t^adj f2=V_t^adj f3=0`; differentiating the displayed formula
for `V_s^adj x2` also gives zero along `V_t^adj`. These observations
give both remaining bracket components explicitly. Endpoint
components vanish by construction.

The raw version of (20) at this same state is `-E u/4` at slice one
and zero elsewhere. Put `a=epsilon`, corresponding to `alpha_3=1`,
and multiply these unscaled brackets by `epsilon^2`. Since
`E(epsilon)=I-epsilon C+...` and `Acoef(epsilon)=C+...`, the four
entire arrays have respectively

    raw degree2:      slice1=-u/4, other slices zero;
    adjusted degree2: all slices zero;
    raw degree3:      slice1=C u/4, other slices zero;
    adjusted degree3: slice1=-C u/8, other slices zero.            (23)

For the stated circulant and coupling,

    C u=(395/648,0,-395/648,1/18,-1/18,1/648),
    -C u/8=(-395/5184,0,395/5184,-1/144,1/144,-1/5184).

Thus the exact Ward extension (17) is not an all-order commuting
extension. This is a counterexample for that particular choice of
higher coefficients, not an obstruction to every possible further
adjustment. The predecessor's degree-two conclusion is unchanged.

## 6. Rigidity under the fixed-lapse Ward premise

Consider now any common homogeneous quadratic family `Fhat_s(q,Q)` in
the class of Section 1 of the preregistration. Its mixed Hessian is
nonsingular and it is real analytic on a connected regular neighborhood
of zero. The prescribed zero and first jets are (9) and (11). A regular
homogeneous quadratic generating function determines a linear symplectic
map `Mhat(s)` by `p=-partial_q Fhat_s`, `P=partial_Q Fhat_s`.
In particular `Mhat(0)=M0`.

Define its incoming and outgoing parameter Hamiltonians by

    Hin_s(q,p)=-partial_s Fhat_s(q,Q(q,p;s)),
    Hout_s(Q,P)=-partial_s Fhat_s(q(Q,P;s),Q).         (24)

These definitions are regular homogeneous quadratic functions of the
phase coordinates. They need not be equal a priori. At zero, the given
first jet and (7)-(8) imply `Hin_0=Hout_0=H`.

We show that the assumed exact Ward identity forces `Hout_s=H`.
Choose any two independently admitted bond parameters `a,b` and any
phase point `z` at their common vertex. There is a field-stationary
three-bond history through that vertex: take phase points

    z0=Mhat(a)^(-1)z, z1=z,
    z2=Mhat(b)z, z3=Mhat(0)z2,

and use their configuration components as the fields. The generating
equations match momenta at both interior vertices, so both interior
field gradients vanish. The corresponding endpoints are admitted by
the arbitrary-endpoint premise and are fixed for this variation.
Finiteness of the accompanying field variation ensures that its work
on this history is zero. Apply the Ward parameter supported at the
first interior vertex. The remaining parameter work is

    -Hout_a(z)+Hin_b(z)=0.                           (25)

Independence of the adjacent bond parameters permits `b=0`; since
`Hin_0=H`, equation (25) gives `Hout_a(z)=H(z)` for all `a,z`.
This argument requires no specified form, locality, or continuity of
the field compensation. It requires its finiteness on these stationary
histories and the declared all-state Ward premise. In the analytic
version these histories and endpoints are real. Identity on rational
samples alone is not substituted for that premise. In the regular
formal version the same construction is made with formal phase
histories and the permitted algebraic substitutions.

For completeness, the outgoing parameter Hamiltonian generates the
parameter derivative of the symplectic map:

    Mhat'(s) Mhat(s)^(-1)=J Hess(Hout_s).             (26)

This follows by differentiating the generating equations at fixed
incoming `(q,p)`. Equivalently their extended differential is
`d Fhat=-p dot dq+P dot dQ-Hout_s ds`; equality of mixed derivatives
gives `Q'=partial_P Hout_s` and `P'=-partial_Q Hout_s`.
Since `J Hess(H)=JG=K`, equations (25)-(26) force

    Mhat'(s)=K Mhat(s), Mhat(0)=M0.                  (27)

The unique analytic solution, or the unique coefficientwise formal
solution of this initial-value equation, is

    Mhat(s)=exp(sK)M0=M0 exp(sK).                    (28)

On a regular chart a type-1 generating function for a given map is
unique up to a function of the parameter alone. Homogeneity of degree
two excludes that addition. Thus `Fhat_s=F_s` as defined in Section 2.
Analytic equality extends throughout the connected regular neighborhood.
This proves uniqueness in the stated class. Merely matching two Taylor
coefficients, or requiring symplecticity and energy preservation, would
not supply (25) and does not imply this theorem.

## 7. Rational-function obstruction

Suppose a matrix with rational-function entries `Mhat(s)`, regular at
zero, satisfied (27). Complexify its rational entries only for this
algebraic argument. At a finite pole of maximal order `m>=1`, a nonzero
leading Laurent coefficient of `Mhat` would give a pole of order `m+1`
in `Mhat'`. Multiplication by the constant `K` cannot create that order
on the right side of (27). This is impossible. Therefore every entry
has no finite complex pole and is a polynomial.

If the polynomial degree is at most `d`, differentiating (27) gives

    0=Mhat^(d+1)(0)=K^(d+1)M0.

Invertibility of `M0` would make `K` nilpotent, contradicting (4).
There is consequently no rational-function transfer in the rigid class.
If the coefficients of a regular homogeneous quadratic `Fhat_s` were
rational functions, solving `p=-partial_q Fhat_s` by the inverse mixed
Hessian would give a rational-function transfer. That possibility is
excluded as well.

This argument does not exclude rational coefficients at each formal
order; the construction in Section 2 has exactly those. It does not
exclude rational parametrizations with a different Ward law, multiple
clock parameters, additional auxiliaries, nonquadratic actions, discrete
clocks, or integer encodings. It concerns the single fixed additive
lapse law and the regular nearest-bond quadratic class declared here.

## 8. The rational Cayley comparison

Define

    Rc(s)=(I-sK/2)^(-1)(I+sK/2), Mc(s)=M0 Rc(s),
    Qden(s)=I+s^2 D/4, N(s)=I+sC-s^2 D/4.

For real `s`, `Qden` is positive definite by (2). The phase inverse
exists, and `Rc(s)^(-1)=Rc(-s)`. From (3), or from multiplying the
two Cayley factors and their transposes, `Rc` is symplectic, preserves
`G`, and commutes with `M0`. Its blocks give

    Bc=N Qden^(-1),
    Uc=(C-sD-s^2 C D/4) Qden^(-1),
    Ecoef_c=Qden N^(-1),
    Acoef_c=(C-sD-s^2 C D/4)N^(-1).                 (29)

On `det N!=0` these define the stated rational generating action.
Because

    Rc(s)=I+sK+s^2 K^2/2+s^3 K^3/4+...,

its map and generating action agree with the exponential through
degree two. This alone imposes no exact Ward or additive-flow law.

The five frozen rational parameters lie on regular configuration
charts. Indeed the eigenvalues of `C` lie in `[321/648,1]`. On a
joint eigenvector put `c` for its eigenvalue and `d=1-c^2`, so
`0<=d<=1`. The eigenvalue of `N` is `1+sc-s^2d/4`. At parameters
`-1/2,0,1/2,1,2`, it is bounded below respectively by

    7/16, 1, 15/16, 3/4, c^2+2c,

all strictly positive. These elementary bounds justify the declared
rational inversions without an evaluated fixture.

On the uniform phase plane, `D=0`, `C=1`, and `Rc(s)` is the shear
`(q,p) -> (q+sp,p)`. Thus any scalar parameter representing
`Rc(1)Rc(1)` must be `2`. Put `X=K/2`. Clearing the invertible commuting
denominators in `Rc(1)^2-Rc(2)` leaves

    (I+X)^2(I-2X)-(I+2X)(I-X)^2=-4X^3=-K^3/2.

This is nonzero because `D!=0` and `K^3` has upper-right block `-D`.
Therefore there is no scalar Cayley parameter representing this
composition. In particular it is not the additive scalar flow.

Differentiating the Cayley expression gives

    Rc'(s) Rc(s)^(-1)
       =K diag(Qden(s)^(-1),Qden(s)^(-1)).           (30)

The associated parameter Hamiltonian, at either endpoint phase, is

    Hc_s(q,p)=[p^T Qden(s)^(-1)p
                 +q^T D Qden(s)^(-1)q]/2.          (31)

It has equal values at the two endpoints because the transfer preserves
this quadratic form as well; all involved blocks commute. Equations
(30)-(31), or direct differentiation of (29), show that the parameter
derivative of the Cayley generating function is `-Hc_s`, not `-H`.

To see the obstruction to any finite field compensation explicitly,
use three bonds with parameters `(1,0,0)` and take

    z1=(q=0,p=e_chi), z0=Mc(1)^(-1)z1,
    z2=M0 z1, z3=M0 z2.

Their configuration components form a stationary field history because
the generating momenta match at both interior vertices. With the Ward
parameter `t1=1`, all other vertex parameters zero, the derivative of
the action from varying the bond parameters is, by (31), exactly

    -Hc_1(z1)+Hc_0(z1)
       =[1-e_chi^T(I+D/4)^(-1)e_chi]/2 > 0.          (32)

The strict sign follows because `e_chi` lies in `v^perp`, on which
`D` is positive definite. Every eigenvalue of `(I+D/4)^(-1)` there
is strictly less than one. At a field-stationary history the work
of every finite field variation is zero, so no such variation can
cancel (32). This directly disproves the fixed-lapse Ward premise for
the Cayley action despite its exact symplecticity and energy preservation.

## 9. Stationary transfer, energy constraints, and chart boundaries

For the exponential family, stationarity in the interior fields is
exactly `l_n=r_n`. There is then a common phase `z_n=(x_n,p_n)` at
each interior vertex, and the bond relations become

    z_b=M(s_b)z_(b-1).

All factors commute, so

    z_T=M0^T exp((sum_b s_b)K)z_0.                   (33)

Here `M0^T` means the integer power with exponent equal to the number
of bonds, not a matrix transpose. Changing the lapse distribution at
fixed total lapse leaves this endpoint transfer unchanged. On stationary
histories the finite vertex transformations can be written

    s_b -> s_b+theta_b-theta_(b-1),
    z_n -> exp(theta_n K)z_n, theta_0=theta_T=0.

They preserve the phase bond relations by commutation of all the
factors, and represent stationary configuration histories whenever
the transformed bond charts remain regular. Their vertex parameters
compose additively. Infinitesimally the raw
formula gives `delta x_n=theta_n p_n` and
`delta p_n=-theta_n D x_n`, in agreement with (19) at `f=0`.
This on-shell statement is distinct from strict off-shell commutation.

The fixed baseline map `M0` need not be replaced by an assertion
`M0=exp(tau K)` for a single scalar `tau`. In fact on this carrier the
uniform shear would force `tau=1`; on any positive `D` eigenmode
with frequency `omega>0`, the exponential's upper-right entry would
be `sin(omega)/omega<1`, whereas `M0` has that entry equal to one.
Equation (33), which keeps `M0` explicitly, is the relevant exact
transfer statement.

If each lapse is varied independently in the action, its equation is
`partial_(s_b)S=-H_b^phase=0`. Combining this with field stationarity
and (2) forces `p=0` and `q=c v` on every bond. The transfer fixes
such a phase point, so the history is static uniform `h`, with
`chi=0`. In the mean-zero sector it is the zero history. Arbitrary
endpoints were admitted off shell; most endpoint pairs cannot satisfy
this zero-energy stationary condition. This is an added constraint
relative to the unrestricted autonomous model, not a claim that the
unrestricted model has no nonzero solutions.

The distinct, explicitly declared action

    S_E=S+Efixed sum_b s_b

has the same endpoint-zero Ward identity because `sum_b Delta t_b=0`.
Its lapse equation is instead `H=Efixed`. For the prepared variant
`Efixed=1`, choose `z0=(0,u)` with the witness vector of Section 5.
Then `H(z0)=||u||^2/2=1`. Since `M0` preserves `G`, every
`z_n=M0^n z0`, including the nine declared states `n=0,...,8`,
has exactly that energy. Omitting the added term changes the lapse
residual at this same initial state from zero to `-1`. The choice
of energy sector is explicit; it is not supplied by the Ward identity.

There is no global type-1 configuration chart. On the uniform phase
plane `K^2=0`, so both the exponential and the Cayley relative maps
are the same shear. Multiplication by `M0` gives

    B(s)v=(1+s)v, Bc(s)v=(1+s)v.

Both configuration charts therefore become singular at `s=-1`.
Their phase maps remain invertible there. The singularity concerns
the ability to use `(q,Q)` as generating coordinates, not a failure
of the underlying invertible phase transfer.

## 10. Finite audit and limits

The formulas prove universal statements within the declared class.
The two frozen independent programs audit their implementation, the
specified examples, controls, and raw-byte agreement. This document
does not infer a run outcome from the formulas. In particular the
fixed dense samples' detection of omitted `S2` and `S3` remains a
frozen computational obligation.

The declared counts follow without evaluating scientific fixtures:
degrees zero through six give seven coefficients; the pairs `i+j<=6`
number `7+6+5+4+3+2+1=28`. The two seeds at each of `T=3,4,5` give
six states and `2(3+4+5)=24` bonds. The `T-1` interior units and one
dense parameter give `T` cases per state, again 24 total. Six nonzero
degrees give `24*6=144` denominator-cleared Ward cases. The ten distinct
pairs of five bonds and five degrees `2,...,6` give 50 mixed coefficients.
Clearing finitely many rational denominators preserves each exact
coefficient identity; it is not a bound on the denominators of an
arbitrarily long evolving history.

The result is an exact local scalar completion and a uniqueness and
non-rational-function theorem under its specified Ward premise. It
identifies a lapse redistribution of the fixed linear phase dynamics,
together with an energy constraint if the lapses are varied. It does
not establish new nonlinear gravitational bulk dynamics, an all-order
completion in every original auxiliary coordinate, a finite rational
formula for arbitrary lapse values, a global generating chart, or
all-order commutation of the adjusted off-shell generators. It makes
no physical preparation, metric-selection, native-U, or cross-layer
claim. Public Canon authority and all such further questions remain
outside this probe.
