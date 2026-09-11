# P-TT-NATIVE-QUADRATIC-EMISSION-1 proof

Status: proof-first candidate-T at frozen L1 scope. The public Canon is unchanged.
Owner: ChatGPT-TT-SOURCE-20260910-B. Lock: #931.
Basis: Public Canon v83, main 51dee9705628e0c9f7bfc7082df46af46ed314b3.

This file proves the universal statements frozen in PREREG.md. The exact
verifier is an audit of the finite coefficient systems, the ten native source
packets and the polynomial identities. It is not the source of the universal
quantifiers below.

## 1. Native length-four Thue-Morse source

Let the substitution be

    sigma(0)=01,   sigma(1)=10.

Write f_ab for the stationary mass of a legal two-letter word ab. A two-letter
window beginning at an even child position is 01 or 10 with equal total mass
1/2. A two-letter window beginning at an odd child position is determined by
its parent pair:

    00 -> 10,
    01 -> 11,
    10 -> 00,
    11 -> 01.

Hence the stationary equations are

    f_00 = f_10/2,
    f_01 = 1/4 + f_11/2,
    f_10 = 1/4 + f_00/2,
    f_11 = f_01/2.

Their coefficient matrix has full rank four. The unique solution is

    f_00=f_11=1/6,
    f_01=f_10=1/3.

For a parent pair ab, the even-start child triple is

    a,(1-a),b,

and the odd-start child triple is

    (1-a),b,(1-b).

The union over the four parent pairs is exactly

    {001,010,011,100,101,110}.

Each of the six triples has mass 1/6 after the parity factor 1/2 is applied.
There are no 000 or 111 triples.

For a parent pair ab the even-start length-four child word is

    a,(1-a),b,(1-b).

This gives

    {0101,0110,1001,1010}.

For a legal parent triple abc the odd-start child word is

    (1-a),b,(1-b),c.

This gives

    {0010,0011,0100,1011,1100,1101}.

Their union is therefore exactly

    W={0010,0011,0100,0101,0110,1001,1010,1011,1100,1101},

which is the frozen K1 source alphabet. The same parity decomposition gives

    mu(0110)=mu(1001)=1/6,
    mu(w)=1/12  for every other w in W.

Thus the optional K1 law is exactly the stationary length-four factor law of
the native Thue-Morse driver. This is an L1 source-consistency theorem. It is
not a physical occurrence or L6 probability statement.

For the public orientation source

    omega(a,b,c)=c-a,

the two overlapping triples of w=(w0,w1,w2,w3) give identically

    omega(w0,w1,w2)=w2-w0=u0,
    omega(w1,w2,w3)=w3-w1=u1.

Therefore the K1 ordered pair (u0,u1) is a literal two-window read of the same
native orientation function.

## 2. The source object and its spin-one amplitudes

For each legal source word freeze

    b_t(r)=[delta_(r,u_t)+delta_(r,u_t+1)]/sqrt(2),
    H_t(r)=b_t(r)^2
          =[delta_(r,u_t)+delta_(r,u_t+1)]/2,
    t=0,1.

Each H_t has spatial sum one. The ordered L1 source descriptor is

    Src(w)=(w,(u0,u1),(b0,b1),(H0,H1)).

The notation b_t is source data. It is not a postulated square root of the
outgoing radiation field. No outgoing spin-one field is propagated in this
probe.

## 3. Classification of the local quadratic spin-two emission class

Identify the real spin-one O(2) representation with C. A rotation through
alpha acts by

    x -> exp(i alpha)x,
    y -> exp(i alpha)y.

Identify the real traceless spin-two representation with C, on which the same
rotation acts by exp(2 i alpha). Reflection acts by complex conjugation.

Consider a real homogeneous quadratic local polynomial map Q(x,y) into the
spin-two representation. Rotation weight two excludes every quadratic
monomial involving a complex conjugate: x conjugate(x), x conjugate(y), and
their analogues have weight zero, while conjugate(x)^2 and related monomials
have weight minus two. Therefore every weight-two map has the complex form

    Q(x,y)=A x^2+Bxy+C y^2.

Reflection covariance forces A,B,C to be real. Ordered-slice antisymmetry gives

    Q(y,x)=-Q(x,y),

so comparison of coefficients yields

    C=-A,   B=0.

Hence the complete frozen class is the one-dimensional family

    Q_kappa(x,y)=kappa(y^2-x^2),   kappa in R.

This proves uniqueness only inside the explicit class A of PREREG.md. It does
not classify nonlocal, higher-degree, memory-bearing or differently typed
source maps.

In the selected K1 plus frame, b_t has one real component and the public square
is H_t=b_t^2. Thus

    Q_kappa(b0,b1)=kappa(H1-H0).

## 4. Normalization fixes the coefficient magnitude

Put

    Phi=H1-H0.

The frozen K1 kinetic source channel between its two initial slices is

    epsilon_K1(r)=Phi(r)^2/2.

Starting the independent emitted field from h0=h1=0 and applying
Q_kappa gives h2=kappa Phi. At that first link the spatial cross term in the
public quadratic energy vanishes because h1=0, so the emitted field energy is

    epsilon_rad(r)=kappa^2 Phi(r)^2/2.

For every nonstatic packet Phi is nonzero at at least one site. Exact equality
of the radiative source channel and the deposited field channel therefore
forces

    kappa^2=1.

No numerical target or adjustable coupling has entered. The ordered source
convention is later slice minus earlier slice, so forward orientation selects

    kappa=+1,

while reversing the source slices produces the negative source as required by
antisymmetry. The emitted map is consequently

    Phi(Src)=b1^2-b0^2=H1-H0.

The ten source words split exactly into four static packets u0=u1 and six
active packets. Their absolute |u1-u0| census is

    0:4,  1:4,  2:2.

Static packets have Phi=0. Every active packet has Phi nonzero. Since both H_t
have sum one,

    sum_r Phi(r)=0.

Thus this source does not excite the spatial zero mode.

## 5. Independent zero-start TT propagation

Use exactly the public planar operator

    L=[188 I-29(S+S^-1)-65(S^2+S^-2)]/324.

Freeze the isolated impulse equation

    h0=h1=0,
    R_L h1=Phi,
    R_L hm=0  for m>=2,

where

    R_L hm=h_(m+1)-2h_m+h_(m-1)+Lh_m.

Solving for the next slice gives

    h_(m+1)=(2I-L)h_m-h_(m-1)+f_m,

with f_1=Phi and all later f_m zero. The coefficient of h_(m+1) is the
identity. Induction therefore gives exactly one rational history for every
finite horizon, and restriction of a longer history gives the shorter one.
Hence the emitted history is total and prefix compatible. In particular,

    h2=Phi.

This regular recurrence contains no substitution h=v^2 into a variational
principle. The singular differential of the square at v=0 found in the review
of PR #930 is therefore absent. This probe does not claim a dynamical outgoing
square root.

Because L annihilates constants and Phi has zero mean, every emitted slice has
zero mean by induction.

## 6. Source stress satisfies the registered planar conservation laws

Write the emitted spin-two field as

    h=h_+ + i h_x.

The corresponding traceless transverse metric entries are

    H_11=h_+,
    H_22=-h_+,
    H_12=H_21=h_x,

with all H_i3 zero in the selected planar sector.

The public linear constrained action gives the TT equations from the source
stress terms as

    R_L h_+ = 2 lambda S_11 = -2 lambda S_22,
    R_L h_x = 2 lambda S_12,

when the longitudinal fields, lapse and shift are zero. Therefore the frozen
source

    S_11= Phi_+/(2 lambda),
    S_22=-Phi_+/(2 lambda),
    S_12=S_21=Phi_x/(2 lambda)

produces precisely R_L h=Phi at the impulse. The coefficient lambda=216 pi is
inherited from the public action and is not adjusted here.

Set

    rho=0,
    J_1=J_2=J_3=0,
    S_13=S_23=S_33=0.

The registered planar source laws

    (1-E)rho=D J_3,
    (E^-1-1)J_i=D S_i3

then read 0=0 identically for i=1,2,3. No longitudinal source component is
projected away. The transverse TT stress is precisely the sector not fixed by
those planar conservation equations.

## 7. Exact local work identity

For any scalar TT component h on the frozen weighted graph, define

    e_(n+1/2)(x)=Delta h_n(x)^2/2
      +(1/4) sum_(e incident x) w_e (B h_(n+1))_e (B h_n)_e,

and

    j_n(e)=(w_e/4)(B h_n)_e
       [q_n(tail e)+q_n(head e)],
    q_n=h_(n+1)-h_(n-1).

The kinetic part obeys the elementary polarization identity

    [(c-b)^2-(b-a)^2]/2
      =(c-a)(c-2b+a)/2.

For one oriented edge with tail values a,b,c and head values d,e,f at three
successive slices, its endpoint-split spatial energy and current obey exactly

    Delta e_tail - j_e
      =(w_e/2)(c-a)(b-e),

    Delta e_head + j_e
      =(w_e/2)(f-d)(e-b).

Summing all incident edges converts the right side into q_n Lh_n/2 at each
vertex. Therefore, off shell and without a continuum approximation,

    Delta e+B^T j=q_n R_L h_n/2.

The verifier proves the displayed identities as exact sparse-polynomial
identities in independent variables.

At the emission step h0=h1=0 and h2=Phi. Thus q_1=Phi and R_L h1=Phi, so

    e_(3/2)-e_(1/2)+B^T j_1=Phi^2/2.

Here e_(1/2)=0 and j_1=0. Freeze only the specific radiative source channel

    e_src,1/2=Phi^2/2,
    e_src,n+1/2=0 for n>=1,
    j_src=0.

It is exactly the K1 kinetic source channel from section 4. Hence at onset

    Delta(e+e_src)+B^T j=0.

For every later step the force vanishes, so R_L h=0 and the ordinary field
identity gives exact local conservation. This ledger does not identify
Phi^2/2 with the complete physical energy of whatever microscopic object
supplies the K1 packet. It proves only transfer of the preregistered radiative
channel.

## 8. v83 auxiliary co-closure

At every half slice solve

    2L tau=Pi0(e+e_src),

with tau mean zero. The connected five-site weighted graph has kernel exactly
the constants, so this equation has one mean-zero solution.

Define

    p_n=-j_n/2-WB(tau_(n+1/2)-tau_(n-1/2)).

Taking B^T and using L=B^TWB gives

    B^T p_n
      =-[B^T j_n+2L(tau_(n+1/2)-tau_(n-1/2))]/2.

The scalar constraints turn the second term into the mean-zero part of the
total energy difference. The total local conservation law has zero spatial
sum and therefore is already mean zero. Hence

    B^T p_n=0.

The verifier checks this exactly through the finite packet histories with an
independent Fraction Gaussian elimination for the Poisson solve. The proof
above carries the general identity on the isolated histories.

## 9. Spin and propagation type

The emitter amplitudes b_t transform with spin weight one. Their quadratic
emission Phi transforms with spin weight two. The already registered
propagation coefficient

    c(s)=1-s^2

gives

    c(1)=0,
    c(2)=-3.

This is a compatibility statement. It does not rederive the Schwarzschild
Regge-Wheeler endpoint, select a curved-background source, or assert an
outgoing spin-one radiation field.

## 10. Falsifier disposition and scientific ceiling

The written proof establishes, conditional on the frozen public inputs and
source class, the mathematical content targeted by F1 through F9:

- the K1 word alphabet and optional weights are exactly the native length-four
  Thue-Morse factor language and stationary law;
- its two u values are overlapping reads of the public orientation function;
- the frozen local O(2)-equivariant, reflection-covariant, slice-antisymmetric
  quadratic source class is one-dimensional;
- source-work equality fixes the coefficient magnitude to one;
- Phi is zero exactly on the four static packets, nonzero on the six active
  packets, and mean zero;
- the emitted TT recurrence is regular, unique and prefix compatible;
- the transverse source obeys the registered planar source conservation laws;
- the local source-field ledger and the v83 auxiliary co-closure are exact;
- spin weights give the registered coefficients 0 and -3;
- no new dimensionless source coefficient is introduced.

The result is strictly L1. It does not by itself prove a physical occurrence
law, detector, SI normalization, irreversible flux, full nonlinear source,
full inhomogeneous GR, a numerical tensor-to-scalar ratio, or a complete
vector state normalization. TT-VECTOR-STATE-NORMALIZATION remains separate.
A later Canon fold must decide whether this exact typed map satisfies the full
registered positive decision condition of TT-SOURCE. This probe does not move
that owner row by itself.
