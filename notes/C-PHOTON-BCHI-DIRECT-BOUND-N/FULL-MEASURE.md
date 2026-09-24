# Extension to the full measure: evaluated bounds and switching obstructions

**PUBLIC, NON-CANONICAL; candidate-T written derivations.**
Working item C-PHOTON-BCHI-DIRECT-BOUND-N, issue #1143.
Author: A. M. Thorn. Date: 24 September 2026. Apache-2.0.
Public basis: Canon v91, main
`af6afcc732ef2daa89e2a0a2a2bb4e02644de8e3`, after #1158.

**No complete P1 proof or positive numerical P1 margin is obtained.**
The new unconditional results concern the actual full measure: prescribed
saturated faces in two copies, their contribution to current covariance,
a summable class of simple current loops, and the removal of sufficiently
dense current sectors from transverse second moments. All unspecified
currents are summed. These are evaluated bounds, not constants awaiting
a future estimate.

The attempted extrapolation of the #1158 cap contraction nevertheless
fails even on a fiber with no saturated cap. A single connected neutral
background leaves a positive Fibonacci limit of the conditional current
correlation. A separate complete current sector has zero transverse
response. Their explicitly controlled or potentially small weights prevent
either example from refuting a positive phase in the full measure.

Throughout, L>=4 is even, V=L^4, and the measure is exactly

    mu_L(n)=Z_L^-1 2^(-|supp n|),
    n in {-1,0,1}^P, partial n=0 mod5, j=partial n/5.

Orientations, midpoints, the two-copy identity and the aligned chains
C_0,...,C_(D+1), s=n_D are those of
[REPLICA-CAPS.md](REPLICA-CAPS.md). No current is prescribed outside the
sets explicitly stated below. The original thermodynamic-first,
infrared-second joint profile contract is unchanged.

## 1. Exact full-sum decomposition

Let n^(1),n^(2) be independent samples from

    mu(n)=Z^-1 2^(-|supp n|) 1_{partial n=0 mod5}.

At every face put m=n^(1)+n^(2), d=n^(1)-n^(2). The two original closure
constraints are equivalent to partial m=partial d=0 modulo five, together
with the following allowed local pairs. Division by two is invertible
modulo five, and the displayed local parities make the reconstructed
integer fields n^(1)=(m+d)/2, n^(2)=(m-d)/2 well defined.

| m | permitted d | product weight |
|---|---|---|
| +2 or -2 | 0 | 1/4 |
| +1 or -1 | +1,-1 | 1/2 each |
| 0 | 0 | 1 |
| 0 | +2,-2 | 1/4 each |

Thus, conditional on the entire sum m, the law of d is exactly the product
of these weights restricted by partial d=0 modulo five. Its normalization
must be retained. Summing its unnormalized partition over every admissible
m gives Z^2. If one also fixes |d|, the remaining signs are uniform over
the compatible orientations, but opening a zero-sum cap changes |d| and
has the real weight ratio 1/4. Discarding this ratio changes the measure.

The conditional Fourier factors for d are

    f_(+/-2)(theta)=1/4,
    f_(+/-1)(theta)=cos(theta),
    f_0(theta)=1+(1/2)cos(2theta).

Their product integrated over Z5 edge angles imposes partial d=0 mod5.
The factors at odd m are not pointwise nonnegative on the actual Z5
carrier. Therefore the positive-integrand comparison available for the
original measure cannot simply be reused for every conditional m law.
This is a precise limitation of that attempted argument, not a claim
that the conditional surface weights themselves are negative.

## 2. Any prescribed occupied-face sign pattern is bounded by emptiness

Let B be any nonempty set of k distinct faces, with no separation or
shape restriction, and let sigma in {+1,-1}^B. Write

    p_sigma=mu(n|_B=sigma),
    p_0=mu(n|_B=0),
    p_occ=sum_sigma p_sigma.

The primal factors are Q_p(A)=1+cos((dA)_p)>=0. Forcing the selected
nonzero Fourier terms gives exactly

    Z p_sigma = 2^-k E_(A in Z5^E)
                  exp(i sum_{p in B}sigma_p(dA)_p)
                  product_{p outside B} Q_p(A),
    Z p_0 = E_(A in Z5^E) product_{p outside B} Q_p(A).

The first integral is nonnegative because it also counts the stated
surface event. Taking its absolute value and using the nonnegative
remaining factors proves, in the full original measure,

    0 <= p_sigma <= 2^-k p_0.                            (R1)

Every unspecified current and exterior face is summed. This is not an
estimate under arbitrary prescribed nonzero exterior data.

Summing (R1) gives p_occ<=p_0. Also p_0+p_occ<=1, since these events are
disjoint for k>=1. No independence between faces is asserted.

## 3. Evaluated saturation probabilities in the full product measure

Call a face saturated when |m_p|=2, equivalently both replicas have the
same nonzero value there. Independence of the two complete replicas gives

    P(all p in B saturated)=sum_sigma p_sigma^2
       <= 2^-k p_0 p_occ
       <= 2^-k p_0(1-p_0)
       <= 2^(-k-2).                                    (R2)

In particular any specified face is saturated with probability at most
1/8, and M specified faces are all saturated with probability at most
2^(-M-2). These are volume-uniform numbers for the full product measure.
They include all exterior charged sectors. The fact that the replicas
are independent does not make the different saturation indicators
independent, and (R2) does not assert a bound (1/8)^k.

For a single face, put p=mu(n_p!=0). Equation (R1) and reversal give p<=1/2,
mu(n_p=+1)=mu(n_p=-1)=p/2. Consequently

    P(|m_p|=2)=p^2/2<=1/8,
    P(m_p=0)=(1-p)^2+p^2/2>=3/8,
    P(|m_p|=1)=2p(1-p)<=1/2.                            (R3)

Nonsaturation is therefore not synonymous with the zero-sum cap that
admits the 1/4 switching insertion: an odd sum is a different local case.

## 4. Exact averaged price of blocked interfaces

Fix M deterministic distinct caps or other faces, and let N_sat be their
number of saturated faces. For t>=1 expand the product of indicators:

    E[t^N_sat]
      = E product_p [1+(t-1)1_{p saturated}]
      <= 1+(1/4)sum_{k=1}^M binom(M,k)((t-1)/2)^k
      = 3/4+(1/4)((1+t)/2)^M.                           (R4)

The bound used for every nonempty subset is exactly (R2), so no assumption
about correlations or an exterior Gibbs condition enters this calculation.
For any 0<=r<=1, substitute t=1/r and multiply by r^M, with the endpoint
r=0 understood by continuity:

    E[r^(M-N_sat)]
       <= (3/4)r^M+(1/4)((1+r)/2)^M.                   (R5)

In particular the already derived cap-chain factor r=3/5 has the explicit
full-measure averaged ceiling

    E[(3/5)^(M-N_sat)]
       <= (3/4)(3/5)^M+(1/4)(4/5)^M.                   (R6)

For any additional event E on which all these specified caps have even
sum, M-N_sat equals their number N_0 of zero-sum caps. Positivity therefore
also gives the unconditioned, event-weighted estimate

    E[1_E (3/5)^N_0]
       <= (3/4)(3/5)^M+(1/4)(4/5)^M.                   (R7)

There is no division by P(E). Thus (R7) does not claim the same upper bound
after arbitrary conditioning on E. It is a usable summed contribution
bound if a switching argument supplies such an event-weighted factor.

A further exact tail estimate, for every integer threshold ell>=1 and
t>1, is

    P(N_sat>=ell)
       <= [((1+t)/2)^M-1]/[4(t^ell-1)].                 (R8)

It follows by applying (R4) to t^N_sat-1, which vanishes when N_sat=0.

## 5. A bounded contribution to the actual full current covariance

Let Delta j=j^(1)-j^(2). Each original edge current is in {-1,0,1}, so
|Delta j_e Delta j_f|<=4. For the event Bad that all M specified caps
are saturated, define its signed contribution to the replica identity by

    C_Bad(e,f)=(1/2)E[Delta j_e Delta j_f 1_Bad].

Equation (R2) proves the genuine full-measure bound

    |C_Bad(e,f)| <= 2^(-M-1).                           (R9)

The exact decomposition is C_j(e,f)=C_Bad(e,f)+C_notBad(e,f). The
second term has not been bounded by (R9). The first term is a signed
contribution, not asserted to be a covariance in a separately normalized
measure or to have a fixed sign.

For the D+1 deterministic interfaces of the aligned geometry, its wholly
saturated contribution is therefore at most 2^(-D-2), regardless of what
other charged components appear outside that geometry. This statement
does not require the rest of a configuration to be an aligned tube.

## 6. Saturated conditional fibers really can have no contraction

There is an all-D exact witness using the same mod-five-closed chain
pieces C_0,...,C_(D+1) as #1158. Choose alternating bits a_i (adjacent bits
always differ) and form the admissible pair

    n^(1)=sum_{i:a_i=0} C_i,
    n^(2)=-sum_{i:a_i=1} C_i.

Its difference is s=sum_i C_i=n_D. Its sum m has coefficient
(1-2a_i)s_p on every noncap face of piece i, and twice a nonzero value
on every interface cap, because the cap incidences of neighboring pieces
have opposite signs while their chosen signs also differ. Thus all caps
are saturated. Both replicas are ternary and closed modulo five since
each piece is so, and at a cap only one neighboring piece enters each
replica.

Fix this sum on the patch and a zero halo. The difference must vanish
on all caps, while its value on each S face is +/-1. The original
degree-two and degree-five constraints of the connected S then force
d=s or d=-s. Both choices are admissible by the displayed pair and its
exchange, and there are no further local states. The conditional product
of difference currents at the two chosen end edges is exactly one for
every D. The conditional sum has therefore completely blocked the
previous cap contraction.

This is not an unconditional counterexample. Its entire event is a
subset of Bad, so it pays the ensemble probability bound (R2) and the
covariance-contribution bound (R9). It shows why an averaged estimate,
rather than a uniform contraction for each sum and exterior, is necessary.

## 7. A connected neutral obstruction with no saturated cap

Saturation is not the only obstruction.
Here is an explicit fiber with no saturated designated cap, but a
nonvanishing limiting conditional endpoint correlation.

Fix odd D>=5, L=2D+4, with the same S, q_r and C_i as above. For
r=2,...,D set

    V_r = c_023(r e_1)+c_023(r e_1+e_3),
    tau_r=(-1)^r.

For r=2,...,D-1 set

    delta_r = r mod 2,
    W_r = c_013(r e_1+delta_r e_2+e_3).

Define a different, connected integer-closed background

    B = partial [sum_{r=2}^D tau_r V_r
                 -sum_{r=2}^{D-1} W_r].                (U6)

Each boundary partial V_r is the ten-face boundary of a 1-by-1-by-2 box
in directions 0,2,3, lying in its fixed x_1=r slice. Its bottom 02 face
is q_r. Its upper 03 face at x_2=delta_r has coefficient

    tau_r (1-2 delta_r)=+1,

and the corresponding face of the next box has coefficient -1. The two
03 end faces of partial W_r have exactly these signs. Subtracting
partial W_r cancels both, leaving its four lateral faces as a connector.
Successive joins use opposite x_2 sides of each interior box, at heights
x_3 in [1,2]. Thus their holes do not intersect.

Every joining face cancels, every other coefficient is +/-1, and the
resulting background is a connected closed surface with degree two at
each occupied edge. Its size is

    |supp B|=10(D-1)+2(D-2)=12D-14.                     (U7)

The background is face-disjoint from S. Its only 01 faces belong to the
upper connectors at x_3=1,2, while the middle of S consists of 01 and 12
faces at x_3=0. The endpoint defects are outside the background's axial
range [2,D]. It meets S only along the boundaries of the interior caps.
Its coefficient at q_r is

    beta_r=-tau_r=(-1)^(r+1),           2<=r<=D.        (U8)

After all bottom caps q_r are deleted and their boundary edges are not
used, the remaining background is still connected. In each middle box,
the lower side walls connect through their vertical edges; the two upper
23 walls connect these to the top 02 face, even after its two upper 03
walls were removed for the connectors. The connector's four side faces
join the remaining box patches through their seam edges. None of these
connections uses a bottom-cap boundary.

Let R=S union supp(B) union {q_1,q_(D+1)}, and H its full edge-sharing
halo. Condition the original product measure on

    n^(1)+n^(2)=s+B on R,
    both copies zero on H outside R,
    every exterior outside H summed.                   (U9)

All fixed sums are 0,+1,-1. In particular none of the D+1 designated
caps is saturated, and there is no sum of magnitude two anywhere in R.

## 8. Exact classification of the unsaturated fiber

The S segments have colors x_i as before. Since B off its bottom caps is
connected through neutral degree-two edges not meeting S, its noncap
faces have one common copy color Y in {0,1}.

For an interior cap write n^(1)(q_r)=beta_r z_r with z_r in {0,1}.
The sum condition then fixes n^(2)(q_r)=beta_r(1-z_r).
The neutral direction-two seam equations give exactly

    beta_r(z_r-Y)=x_(r-1)-x_r.                          (U10)

The endpoint caps retain the original differences x_0-x_1 and
x_D-x_(D+1). Conversely the reconstructions

    n^(1)|R = sum_i x_i C_i+Y B,
    n^(2)|R = sum_i(1-x_i)C_i+(1-Y)B                   (U11)

are separately closed modulo five. They are ternary with the required
sum if and only if (U10) has a binary z_r at every interior cap.
Thus (U10)-(U11) classify every local state, not merely some states.

For Y=0, an even r has beta_r=-1 and permits only x_(r-1)<=x_r.
An odd r has beta_r=+1 and permits only x_(r-1)>=x_r. The interior
transition matrices, with left/right bit indices 0,1, are therefore

    U = [[1,1],[0,1]],   L = [[1,0],[1,1]] = transpose(U).

For Y=1 every bit is reversed, giving the same partition and endpoint
product after summation. All faces with nonzero sum contribute one
occupied copy and hence a common weight 2^(-|S|-|supp B|). There is no
additional cap penalty inside: these caps already have sum +/-1. Only
the two endpoint zero-sum caps contribute weights 1 or 1/4.

## 9. Fibonacci correlation and its nonzero limit

Write D=2h+1, h>=2. There are 2h interior interfaces, starting with U
and ending with L. For Y=0 their complete product is

    M^h=(UL)^h,
    M=[[2,1],[1,1]],
    M^h=[[F_(2h+1),F_(2h)],[F_(2h),F_(2h-1)]],

where F_0=0,F_1=1 are Fibonacci numbers. With v=(1,1) and w=(1,-1),

    v^T M^h v = F_(2h+3)=F_(D+2),
    w^T M^h w = F_(2h-3)=F_(D-4).                      (U12)

Summing a free endpoint through its original cap matrix multiplies the
constant channel by 5/4 and the sign channel by 3/4. The two values of
Y contribute equally. If c_D=2^(-|S|-|supp B|)=2^(-(16D+26)), the exact
local partition and difference-current numerator are

    Z_local = c_D * 2(5/4)^2 F_(D+2),
    N_local = c_D * 2(3/4)^2 F_(D-4).

Consequently

    E[d_j(e)d_j(f) | (U9)]
       = (9/25) F_(D-4)/F_(D+2)
       --> (9/25) phi^(-6) > 0.                        (U13)

Copy exchange makes both conditional difference-current means zero.
This is again a genuine conditional covariance. For an elementary
rational lower bound, F_(n+6)=8F_(n+1)+5F_n<=21F_n for n>=1. Hence
the right side of (U13) is at least 3/175 for every odd D>=5.

Every designated cap has sum 0 or +/-1, so N_sat=0 throughout this fiber.
Equation (U13) therefore disproves a uniform conditional domination by
(3/5)^(D+1-N_sat), or any distance-independent multiple of that expression.
The obstruction is a common neutral background color transmitted through
an entire connected surface, rather than a saturated cap.

The exterior factor is again (Z_emptyH/Z_L)^2. The event can have very
small probability, and the remaining fibers are uncontrolled. No
unconditional no-decay conclusion follows from (U13).

## 10. Nonlinear source estimate for simple current cycles

This specializes and sharpens the existing weighted-turn argument in
[PHOTON-LOW-CONFLICT-CURRENT-PATHS.md, sections 5-8](../canon/PHOTON-LOW-CONFLICT-CURRENT-PATHS.md).
That note already bounds paths with an excess-contact budget of length/24.
The direct closed-cycle count and the rational source choice below are
refinements of that argument, not the first decay estimate for this geometry.

The already proved partial-current source comparison from
[CONNECTED-CURRENT.md, section 5](CONNECTED-CURRENT.md) is

    Q_S(a)/Q_S(0) <= exp(-5<a,f>) product_p cosh((df)_p),

for real f supported on S. Here Q_S(a) fixes only j on S and sums every
other current. It is not the completely fixed-current partition Q_j.
In particular P(j|S=a)<=Q_S(a)/Q_S(0), since Q_S(0)<=Z_L.
The same unnormalized inequality is obtained by continuous integration
on S, discrete Z5 integration elsewhere and inserting the complex source
in the finite character expansion; the modulus identity |1+cos(theta-i u)|=cosh(u)+cos(theta)
and coefficientwise cosh comparison finish it. It does not authorize
conditioning on an arbitrary nonzero exterior current.

Let gamma be a simple oriented edge cycle, including a winding cycle. Here
simple means that no vertex repeats except the final return to the starting
vertex. Set S=supp gamma, ell=|S|, and f=h gamma, with h>0. Let m_p be the
number of selected edges on the boundary of p. Then |(d gamma)_p| <= m_p,
and sum_p m_p=6 ell. Let c(gamma) be its number of right-angle turns
(including the closing vertex). Let O(gamma) be the number of unordered
pairs of opposite boundary edges of a plaquette that both belong to gamma,
summed over plaquettes. No sign is imposed on these opposite pairs.

Because the cycle is simple, every pair of selected adjacent edges of a plaquette is exactly one of its right-angle turns. Hence

    sum_p binom(m_p,2) = c(gamma) + O(gamma).

Put u=tanh h and r=1+u^2. For m=0,1,2,3,4,

    cosh(m h) <= cosh(h)^m r^(m(m-1)/2).

For m=2 this is equality. For m=3 divide by cosh(h)^3 and use 1+3u^2 <= (1+u^2)^3. For m=4 use 1+6u^2+u^4 <= (1+u^2)^6. These are polynomial inequalities with nonnegative coefficient differences. Therefore

    C_gamma := exp(-5h ell) product_p cosh(h (d gamma)_p)
              <= a^ell r^(c(gamma)+O(gamma)),
    a := exp(-5h) cosh(h)^6.

Consequently, with E_gamma={j_e=gamma_e for all e in S},

    P(E_gamma) <= C_gamma <= a^ell r^(c+O).

Global reversal gives P(E_gamma)=P(E_-gamma). The zero-on-S event and the two oriented events are disjoint, and each oriented mass is at most C_gamma times the zero mass. Thus also

    P(E_gamma union E_-gamma) <= 2 C_gamma/(1+2 C_gamma).

This is a full-measure probability statement. It says that all edges of the cycle carry its orientation; it does not require the current component to be isolated or exclude additional currents touching its vertices.

The same existing method has a sign-sensitive refinement. Split
O=O_plus+O_minus according to
whether the two selected edges have equal or opposite signed incidences
in that plaquette's curl. With exactly two opposite selected edges of
the second type, the curl is zero and the ratio to cosh(h)^2 is
cosh(h)^(-2). A plaquette with three or four edges of a simple cycle has
coherently oriented incidences, so all its opposite pairs are of the
first type. Multiplying the corresponding face inequalities gives

    C_gamma <= a^ell r^(c+O_plus) cosh(h)^(-2 O_minus).

For the rational choice below the last factor is (9/25)^O_minus.
No sum over all possible opposite contacts is evaluated by this refinement.

## 11. Exact subcritical sum for cycles without opposite-edge contacts

Take

    h = log 3,
    a = 15625/177147 = 5^6/3^11,
    r = 41/25.

Call a simple cycle contact-free in the present precise sense when O(gamma)=0. Such a cycle has no plaquette containing a pair of its opposite edges. In particular, no plaquette has three or four selected edges. The previous bound reduces to a^ell r^c.

Fix a positive oriented edge e. Count simple cycles through e by starting them along e. For an open nonbacktracking walk there is one straight next step and six right-angle next steps. Weight a right-angle step by r. The total continuation weight is therefore

    1+6r = 271/25.

Ignoring self-avoidance, closure, and the contact-free restriction only increases the sum. The closing turn contributes at most one extra factor r. Hence the sum over contact-free cycles of length ell containing e, oriented to start along e, obeys

    sum_gamma a^ell r^c <= r a [a(1+6r)]^(ell-1).

The exact common ratio is

    q = a(1+6r) = 169375/177147 < 1,

because 177147-169375=7772>0. The choice h=log 3 is convenient, rational in the resulting constants, and is not claimed to be the exact optimum for this cycle count.

For every integer R>=4, every permitted volume, and the original full measure,

    P(e lies in a contact-free simple current cycle of length >= R)
       <= [2 r a/(1-q)] q^(R-1)
        = (25625/3886) (169375/177147)^(R-1).

The factor 2 includes both current orientations. The right side may be replaced by its minimum with 1. There is no fitted or unspecified constant. This estimate is uniform in L, and the finite cycle-length sum was safely enlarged to an infinite geometric series.

This is stronger than separately using the worst corner penalty and then a bare entropy 7^ell: the straight and turning choices must be summed with their actual weights. It still excludes opposite-edge contacts. Even complete control of individual current cycles would not on its own bound correlations between distinct cycles joined through neutral surfaces.

### Allowing a larger opposite-contact budget

The rational source choice also covers cycles with O<=ell/12. Put
tau=73/70. The positive binomial terms give the exact inequalities

    tau^12 > 1+12(3/70)+66(3/70)^2+220(3/70)^3
           =14173/8575 > 14063/8575 =41/25=r.

Thus r^O<=tau^ell on this class. The same weighted count, including the
closing turn, has ratio and prefactor

    q_contact=q*tau=2472875/2480058<1,
    2 r a tau/(1-q_contact)=748250/7183.

For the full original measure and every R>=4 it follows that

    P(e lies in a simple current cycle of length ell>=R with O<=ell/12)
      <= min{1,(748250/7183)(2472875/2480058)^(R-1)}.

This extends the admissible excess-contact fraction of the existing
weighted argument from 1/24 to 1/12, with a direct closed-cycle count.
The unrestricted contact sum and the signed covariance between distinct
cycles remain uncontrolled.

## 12. A nonempty current sector with identically zero transverse axial response

Let L>=4 be even, V=L^4, and define

\[
s_0(x)=(-1)^{x_1+x_2+x_3},\qquad
s_1(x)=(-1)^{x_0+x_2+x_3}.
\]

Prescribe the current

\[
j_0^*(x)=s_0(x),\quad j_1^*(x)=s_1(x),\quad
j_2^*(x)=j_3^*(x)=0.                              \tag{T1}
\]

It is divergence-free because each nonzero component is independent of its own coordinate. The entire ternary sector `partial n=5j*` consists exactly of

\[
\begin{aligned}
n_{01}(x)&=(s_0(x)-s_1(x))/2,\\
n_{02}(x)&=n_{03}(x)=s_0(x),\\
n_{12}(x)&=n_{13}(x)=s_1(x),\\
n_{23}(x)&=f(x_0,x_1),\qquad f\in\{-1,0,1\}^{(\mathbb Z/L\mathbb Z)^2}.
\end{aligned}                                                       \tag{T2}
\]

### Verification and completeness

The canonical boundary formula at an orientation-zero edge gives

\[
(\partial n)_0
=[n_{01}(x)-n_{01}(x-e_1)]
 +[n_{02}(x)-n_{02}(x-e_2)]
 +[n_{03}(x)-n_{03}(x-e_3)]
=s_0+2s_0+2s_0=5s_0.
\]

For direction one the 01 contribution is
`n_01(x-e_0)-n_01(x)=s_1`; the other two differences each contribute `2s_1`. The other two boundary components vanish when n_23 is constant along x_2 and x_3. Thus every field in (T2) belongs to the required sector.

For completeness, six ternary incidences summing to +5 or -5 contain exactly five terms of that sign and one zero. At an 01 face, the two direction-zero edges require the face sign s_0(x), whereas the two direction-one edges require -s_1(x). If these demands disagree the face must be zero. Along either charged edge, exactly one of its two incident 01 faces has conflicting demands. Hence that edge's unique zero face is already determined; all five other incidences are forced nonzero with their prescribed sign.

This fixes precisely the first five entries of (T2). Substituting them into the two neutral edge equations leaves

\[
n_{23}(x)-n_{23}(x-e_3)=0,\qquad
n_{23}(x)-n_{23}(x-e_2)=0,
\]

which is equivalent to the stated free function f(x_0,x_1). There are no other configurations in this sector.

### Partition and axial observable

The fixed fields in the first five orientations occupy `4V+V/2=9V/2` faces. Each nonzero f value fills one whole L^2-face 23 plane. Therefore the complete sector partition is

\[
\boxed{Q_{j^*}=2^{-9V/2}(1+2^{1-L^2})^{L^2}>0.}       \tag{T3}
\]

For every allowed axis momentum `q=t e_1`, the 02 midpoint has first coordinate x_1 and

\[
F_{02}(n;t e_1)
=\sum_x(-1)^{x_1+x_2+x_3}e^{-itx_1}=0,              \tag{T4}
\]

because L is even and the alternating x_2 sum vanishes. This holds for every f, not merely after averaging. Hence even the **raw conditional second moment** is zero:

\[
\boxed{V^{-1}\mathbb E[|F_{02}(n;t e_1)|^2\mid j=j^*]=0.} \tag{T5}
\]

The result does not depend on a distinction between conditional covariance and conditional mean. It disproves any strictly positive transverse lower bound asserted separately for every complete current sector, including a putative uniform Gaussian or neutral-background comparison after prescribing arbitrary j. It does not disprove a positive lower bound in the original averaged measure.

## 13. This particular sector is quantitatively rare

The zero field gives Z_L>=1. Put m=L^2>=16. Since `m 2^(1-m)<=1/2048`, the elementary binomial/geometric estimate gives

\[
(1+2^{1-m})^m
\le\sum_{r\ge0}(m2^{1-m})^r
\le\frac{2048}{2047}<2.
\]

Consequently

\[
\boxed{\mu_L(j=j^*)\le Q_{j^*}<2^{1-9V/2}.}         \tag{T6}
\]

Thus the sector obstruction cannot itself decide the sign of the averaged infrared response. Discarding this one sector loses exponentially little probability, and in fact loses no 02 axial second moment because of (T4).

## 14. An actual full-measure exponential bound for extensive current support

For a nonempty plaquette-independent set S of s>=1 edges, every plaquette meets at most
one selected edge. The source f=h times a prescribed current sign therefore
has comparison factor [exp(-5h) cosh(h)^6]^s. Choosing h=(log11)/2 and
summing the 2^s sign patterns gives the existing complex-source estimate

\[
\mu_L(j_e\ne0\ \forall e\in S)
\le(2b_{\rm edge})^s< (2/11)^s,\qquad
b_{\rm edge}=6^6/11^{11/2}<1/11.                    \tag{T7}
\]

It includes all unspecified current sectors. The strict inequality follows from `6^4<11^3`; no decimal estimate is needed. For the empty set the probability and its zeroth-power bound are both one.

Color each positive edge (x,i) by `(i, sum_{a!=i}x_a mod 2)`. There are eight plaquette-independent classes, each with M=V/2 edges. Let N_c be the number of occupied currents in one class. For any u>=1, expanding the product with nonnegative coefficients and applying (T7) to each subset gives

\[
\mathbb E u^{N_c}
=\mathbb E\prod_{e\in c}[1+(u-1)\mathbf1_{j_e\ne0}]
\le[1+(2/11)(u-1)]^M.                               \tag{T8}
\]

This is a factorial-moment argument, not an assertion of independent edge currents or conditional Bernoulli domination.

At u=3/2, Markov's inequality gives

\[
\mu_L(N_c\ge M/4)
\le(3/2)^{-M/4}(12/11)^M
=\left(\frac{13824}{14641}\right)^{V/8}.             \tag{T9}
\]

If the total number N of occupied current edges is at least V, one color contains at least V/8=M/4 occupied edges. Thus, with `r=13824/14641<1`,

\[
\boxed{\mu_L(N\ge V)\le\min\{1,8r^{V/8}\}.}        \tag{T10}
\]

This controls a whole class of extensive-current sectors in the full original measure. The sector (T1) has N=2V and lies within it.

For any orientation I and momentum q, `|F_I(n;q)|<=V`, hence the discarded contribution to the normalized second moment has the explicit bound

\[
0\le V^{-1}\mathbb E[|F_I|^2\mathbf1_{N\ge V}]
\le8V r^{V/8}.                                     \tag{T11}
\]

It tends to zero independently of q. Equivalently the normalized second moment conditioned on `N<V` differs from the full one by at most `V mu_L(N>=V)`, since both conditional moments lie in [0,V]. Thus removing these high-density sectors does not change any admitted thermodynamic-first transverse profile.

## 15. Disposition of the complete-proof attempt

The exact full-sum representation is now available, and saturation pays
an explicit ensemble price. However, the marked faces in the saturation
bounds must be deterministic. A geometry selected from the random pair
requires a valid exploration or a bound on its selection multiplicity.
Independence of the two original copies is also lost after conditioning.
Most decisively, sections 7-9 disprove the proposed per-fiber domination
by (3/5)^(M-N_sat), even though its unconditional expectation was bounded
correctly in section 4. Thus that expectation is not a bound for the
complete current covariance.

The nonlinear source gives a genuine full-measure tail for cycles
without opposite-edge contacts. It does not cover the unrestricted
geometric sum, and correlations of distinct short cycles may still be
transmitted through a neutral surface. The local circulation constant
c<1/3000 cannot be multiplied after deleting successive plaquette shortcuts:
its proof sums the exterior, whereas that deletion would fix nonzero
exterior currents. No required conditional comparison was proved.

The transverse side also needs an averaged argument. Section 12 rules out
a positive bound uniform in every complete current sector; section 14
removes the displayed dense obstruction, and all sectors above its stated
density threshold, with an explicit uniform error. After that removal,
low current density does not itself force large neutral fluctuations.
The source/contact Hessian is an upper bound, and a total spectral-weight
sum rule does not force weight at small momentum. The existing local
insertion floor remains the shared bounded-component contribution to b
and 25 chi, so it supplies no positive difference after subtraction.

The finite checks in [FULL-PREREG-20260924.md](FULL-PREREG-20260924.md)
audit the actual lattice geometry, complete restricted fibers, sector
constraints and rational loop constants. They do not enumerate the full
measure or infer an all-volume theorem from small volumes. Separate agents
reviewed the derivations with shared sources, not blind external evidence.

**Still missing:** an evaluated uniform bound on the full signed current
second moment and a transverse lower bound strong enough to prove
`b_lower > 25 chi_upper` over all original admitted profiles. No claim is
made that the true difference is nonpositive. P1, P2, S7 and the canonical
phase obligation remain OPEN; no Canon promotion is requested.
