# Joint cancellation: integer cuts, contraction, and necessary squares

**NON-CANONICAL. No authority. Candidate-D paper deductions.**
Action layer NOT_APPLICABLE. C-RH-ARITHMETIC-KERNEL-N, continued under
[issue 2087](https://github.com/mathorn1973/twist-j/issues/2087) and
[draft 2089](https://github.com/mathorn1973/twist-j/pull/2089).
The complete all-epsilon power estimate is still **O**.

This round works on whole signed expressions. It obtains a stronger
prime-correction contraction, an integer factor cut with smaller upper
arguments, and additive estimates for joint covariances. It also rules
out the previous sufficient shortcut that discards the overlap square.
No deduction below is an arithmetic proof of the remaining full bound.
The earlier files are retained unchanged.

## 1. The actual state and the unchanged target

Use the incoming round-eight dyadic X, D=4X, z=D^(1/3), and the original
rational time taper w. It equals one on the integers in [X,2X) and is
supported in [7X/8,17X/8]. Write ||F||_w^2=sum_n w(n)|F(n)|^2.
The actual multiplicative coefficient t=chi_5*s has local values

| Prime | t(p^j), j>=1 |
|---|---|
| p congruent to 1 or 4 modulo 5, called split | -1 |
| p congruent to 2 or 3 modulo 5, called inert | (-1)^j |
| p=5 | 0 |

Thus |t(n)|<=1 and T(x)=sum_(n<=x)t(n) is an integer prefix, with
floor convention and zero value below one. Its Dirichlet inverse f
has nonnegative integer coefficients. The prefix of f is denoted F.
The inherited coefficient unit U satisfies t=mu*U^(-1) as a formal
coefficient identity, and has an absolutely convergent inverse above
the critical line.

Round eight defined G_*=G_7-V_out, its common-window removal V_0,
and G_8=G_*-V_0. C_z is the complete original prime profile, including
the repeated split-prime term with its original coefficient -4.
The actual comparisons are

    ||T-(G_8+C_z)||_w^2 <<_epsilon X^(2+epsilon),
    Q_8=||G_8+C_z||_w^2+O_epsilon(X^(2+epsilon)).                (1)

Q_8 retains both mixed orders with V_0 and with C_z, as stated in
[the incoming report](../round8/REPORT.md). The target is

    (Q_8(X))_+ <<_epsilon X^(2+epsilon)
    for every epsilon>0 on all sufficiently late dyadic X.     (2)

The one-sided complete-window criterion for T uses [Y,Y^2) and weights
1/[n(n+1)]. Its equivalence with RH is inherited from FOUNDATION and
is not a premise of any new estimate. In particular neither that
equivalence nor a renamed residual proves (2).

## 2. A previous sufficient shortcut is false for the actual coefficients

At the unchanged strict cut A=floor(X^(1/14)), the incoming identity is

    T(n)=L_A(n)-n U(1)h_A^2-S_A(n)+O(sqrt X),
    h_A=sum_(m<=A)t(m)/m,
    S_A(n)=sum_(k<=n/(A+1)^2) f(k)
                   [T(floor(sqrt(n/k)))-T(A)]^2 >=0.           (3)

Round eight correctly noted that an all-epsilon bound for (L_A)_+
would be sufficient. This round shows that such a bound is false.
Even retaining the affine penalty while dropping only S_A gives

    ||(L_A-n U(1)h_A^2)_+||_w^2 >> X^(18/7)                   (4)

on infinitely many dyadic blocks. The same lower bound holds for
||(L_A)_+||_w^2. This is about the actual t and f, without freely
chosen signs or substitute input states.

The mechanism is elementary after the incoming inverse mean is used.
Among A+1<=m<=2A, a positive proportion of adjacent prefix values
have a unit step because 5 does not divide m. At least a constant
multiple of A prefix values therefore have nonzero integer square.
The exact k-bin with floor(sqrt(n/k))=m has f-mass

    F(n/m^2)-F(n/(m+1)^2) >> X/A^3.

Summing the disjoint bins yields S_A(n)>>X/A^2 uniformly on the
taper. There are arbitrarily late positive times T(n_0)>0, proved
using the existing signed-window lemma and the holomorphic extension
of U past Re(s)=1/2. Hardy's unconditional critical-line zeros
supply the nonreal pole needed for that application. Unit steps of
T then give an interval of length comparable to X/A^2 where the
omitted square dominates the negative part of T and the O(sqrt X)
reconstruction error. Squaring on that interval gives (X/A^2)^3,
which is X^(18/7).

This also defeats the simplified expression on every sufficiently
late complete original window. Take a positive time in
[Y^(5/4),Y^(3/2)] using the signed-window lemma, and use its central
dyadic block inside [Y,Y^2). Dividing (4) by the comparable X^2
from the original weights gives at least c Y^(5/7). Thus the
failure is not merely a sparse set of bad complete windows.
The full expression in (3), retaining both penalties, is not
lower-bounded by this argument.

[SQUARE-RETENTION](sol_squares/SQUARE-RETENTION.md) proves the
dyadic result and the separately scoped affine-penalty obstruction
at a nearby cutoff. The complete-window implication is recorded in
[INTEGER-CUBIC-CUT](INTEGER-CUBIC-CUT.md) and the
[joint review](sol_squares/REVIEW-JOINT-SYNTHESIS.md).

## 3. A longer cut with integer coefficients and both squares

The inverse mean is now sharpened to

    F(y)=U(1)y+C_U zeta(1/3)y^(1/3)+O(y^(7/22)),              (5)

where C_U>0 and zeta(1/3)<0. Because 7/22<1/3, this time the cubic
term is resolved below its own scale. The previous O(y^(5/12))
remainder did not resolve it.

The proof factors the actual inverse series as
zeta(s)L(2s,chi_5)zeta(3s)L(3s,chi_5)W_4(s). Bounded character
intervals, the finite discrepancy inequality and the second
derivative estimate give a y^(1/4) error for the mean of the
zeta(s)L(2s,chi_5) factor. A hyperbola split at y^(3/11) balances the two remaining
errors at y^(7/22). The absolute coefficient convergence of W_4
holds at that exponent, so it preserves the error. The full proof
and endpoint checks are in
[LONGER-FACTOR-CUT](sol_squares/LONGER-FACTOR-CUT.md).

Subtracting the short rectangle gives a positive cubic square.
The new root construction cancels that moment exactly while
keeping integer short coefficients. In Dirichlet convolution set

    e=delta_1-2 delta_8,
    nu(n)=sum_(j>=0,8^j|n)2^j t(n/8^j),
    a=e*(nu 1_(n<=A)),       b=t-a,
    A=floor(X^(2/15)).

Then a=t through A, its support is at most 8A, and b=0 through A.
The cancellation and harmonic moment are exactly

    sum_n a(n)n^(-1/3)=0,
    h(a)=(3/4)sum_(m<=A)nu(m)/m.                              (6)

All a, b, nu are integers and h(a) is rational. Although nu is not
bounded pointwise, its absolute summatory function is at most
4L/3 through L. Consequently sum|a(n)|n^(-theta)<<A^(1-theta)
for fixed theta<1, which is exactly what the short rectangle needs.
At theta=7/22 its remainder is
X^(7/22) A^(15/11)=X^(1/2). The short intercept is O(A) and is
paid, rather than set to zero.

With B_b(v)=sum_(m<=v)b(m) and r_k=floor(sqrt(n/k)), the full result is

    T(n)=Z_X(n)+O(sqrt X),
    Z_X=L_b-n U(1)h(a)^2-S_b,
    L_b=2 sum_(k<=n/(A+1)^2) f(k)
                sum_(A<m<=r_k)b(m)B_b(n/(km)),
    S_b=sum_(k<=n/(A+1)^2) f(k)B_b(r_k)^2 >=0.                 (7)

Every remaining linear prefix argument is O(X^(13/15)); the old
strict cut allowed X^(13/14). The affine square uses a; the overlap
and linear terms use the same b=t-a, all at time n. No arbitrary-input independence is inserted.
The full taper error in squared norm is O(X^2).

The overlap still cannot be dropped: the integer construction gives
the actual lower bounds X^(11/5) on infinitely many dyadic blocks
and Y^(1/4) on every sufficiently late complete weighted window.
[INTEGER-CUBIC-CUT](INTEGER-CUBIC-CUT.md) proves all these claims.
The author longer-cut file also retains its distinct constant-pad
construction and a strict power approximation of the combined
large-inverse-factor range; neither is silently substituted for (7).

## 4. The whole prime completion reaches the fifth root

Let T_y be the true t-prefix restricted to integers with all prime
factors at most y, including one. For y>=5, frozen on the block, define

    L_y(n)=sum_(d<=n,P^-(d)>y)(-1)^Omega(d) T_y(n/d),            (8)

including d=1. Both prime classes and all multiplicities are present.
This differs from a raw residue-kernel restriction. Finite Euler
coefficient multiplication gives the exact identity

    L_y=T+H_y[T],
    H_y[F](n)=sum_(1<d<=n)h_y(d)F(n/d),                        (9)

where h_y(1)=1 and all h_y(d)>=0. Nonconstant coefficients are
supported only on split primes p>y, each with exponent at least two.
Their local factor is

    (1-x)/[(1+x)(1-2x)] = 1+2x^2/[(1+x)(1-2x)].               (10)

At y=z, (8) equals the incoming complete J_z on n<=D. At
y=D^(1/5) the only correction types are p^2, p^3, p^4 and
p^2 q^2 with p<q. Thus, using split primes in the following corrections,

    K_y=L_y-2 sum_(y<p<=z)T(n/p^2)
               -2 sum_(p>y)T(n/p^3)
               -4 sum_(y<p<q)T(n/(pq)^2)

satisfies K_y-J_z=6 sum_(p>y)T(n/p^4)=O(X^(2/5)) pointwise.
The entire difference costs O(X^(9/5)) in squared taper norm.
This is a power estimate for complete profiles, not for separately
chosen signed families.

The repeated-prime operator also has a sharper critical contraction
than the earlier two-block triangle bound. Put

    E_(sigma,Y)(F)=Y^(1/2-sigma)
                       (integral_Y^(2Y)|F(u)|^2 du/u^2)^(1/2).

For y=D^gamma, 1/6<=gamma<1/2, its asymptotic operator norm from
the maximum of smaller dyadic critical norms to E_(1/2,X) is

    S(gamma)=log(1/(2 gamma))
       +(1/2) integral_(s,t>=1, s+t<=1/(2 gamma)) ds dt/(s t).  (11)

The proof sums the actual density of prime dilations over the
smaller dyadic blocks before losing their overlap. Its lower test
is explicitly an arbitrary comparison input, not the actual T.
There is a unique gamma_* between 1/6 and 1/5 with S(gamma_*)=1.
Strict contraction holds at the explicit fifth-root cutoff.
At the old cube root the sharp factor is log(3/2); the old
sqrt(2)log(3/2) was a valid upper bound, not the exact norm.

This identifies the limitation of a universal critical-norm
induction for the correction operator. It does not prove that
the actual remaining joint arithmetic sum has bounded norm.
Nor does the strict arithmetic endpoint remove the epsilon error
from the Fourier transfer (1).
[ROUGH-COMPLETION](astra_joint/ROUGH-COMPLETION-AND-CRITICAL-THRESHOLD.md)
contains the exact statement, proof and lower test.

## 5. A logarithmic cut removes the whole new smooth prefix

For every fixed sigma>1/2 the same positive correction obeys

    E_(sigma,X)(H_y[F])
       <<_sigma y^(1-2sigma)
           max_(Y dyadic,Y<=2X/y^2) E_(sigma,Y)(F),             (12)

whenever y=y_X tends to infinity. This is proved from the actual
squareful Euler tail, and its coefficient tends to zero. At
y=log X, elementary Rankin counting gives

    sup_(u<=4X)|T_y(u)| <<_eta X^eta
    for every eta>0.                                          (13)

Thus the entire new smooth term can be paid. The remaining sum is

    A_X(n)=sum_(1<d<=n,P^-(d)>log X)(-1)^Omega(d)
                                      T_(log X)(n/d).          (14)

For each fixed sigma>1/2, bounded E_(sigma,X)(A_X) on all late
blocks is equivalent to (Q_8)_+=O_sigma(X^(1+2sigma)). The
direction from a bound on A_X to a bound on T, and hence Q_8,
uses lower-block induction in (12), on the actual T. The other
direction needs no induction. No Mertens bound is assumed.

This removes the large smooth-prefix drift that was present at
the old cube-root cut. The price is that (14) now contains all
rough multiplicities. Actual fixed-prime-product subfamilies
already have coherent magnitude >>X/(log X)^k on a central
interval, so taking their absolute values cannot establish the
target. No small bound is claimed for a whole multiplicity layer.

The integer profile (7) can be composed with (14) without changing
the inverse. Stitch Z over its actual smaller dyadic arguments.
For each fixed sigma>1/2,

    A_X(n)=sum_(d<=n)h_y(d)Z(n/d)-T_y(n)+O_sigma(X^sigma).      (15)

The h_y weights are positive, uniformly summable against d^(-sigma),
and include h_y(1)=1. Both negative squares survive in every
dilation. All mixed pairs of these complete lower profiles remain
to be estimated. Equation (15) is a comparison, not that estimate.

An obvious alternative weighting fails on the whole actual profile:
attaching log p/log n to each marked prime while keeping T_z
unchanged gives -[log 2/U(1)] n/(log n)^2+O(X/log^3 X).
Its squared norm has order X^3/log^4 X. The weighted singleton
does cancel to every fixed inverse-log order, but the weighted
distinct pair introduces the uncompensated main term. This
excludes that concrete prescription only, as proved in
[LOG-SHARE-OBSTRUCTION](astra_joint/LOG-SHARE-OBSTRUCTION.md).

## 6. Two joint covariance estimates with all sectors present

First group by the gcd of arithmetic coefficient indices, rather
than the different primitive-conductor gcd. Let

    H_G=sum_n w(n)sum_(m,k<=n)t(m)t(k)1_((m,k)>G),
    L_G=||T||_w^2-H_G,
    lambda_G(r)=sum_(d|r,d>G)mu(r/d).

The exact identity is H_G=sum_(r>G)lambda_G(r)||T_r||_w^2,
where T_r(n)=sum_(a<=n/r)t(ra). It contains the complete raw
core and prime complement and both of their mixed orders.
For 5 not dividing r, its local filter is

    T_r(n)=t(r)sum_l v_r(l)T(n/(rl)),
    sum_l v_r(l)l^(-sigma)
       =product_(p|r,p split)(1-2p^(-sigma))^(-1)
       <<_(sigma,eta) r^eta.

For 5 dividing r it is zero. Define the maximum M_sigma(U) of
the actual normalized central dyadic square energies through U.
For fixed sigma>1/2 and 0<eta<2sigma-1 the proved joint bound is

    |H_G| <<_(sigma,eta) X^(1+2sigma)
                        G^(1-2sigma+eta) M_sigma(3X/G).       (16)

With G=floor(X^delta), 0<delta<1 fixed, this is a power contraction
into earlier blocks. The all-late-block bound for (L_G)_+ is
therefore equivalent to the full target at that sigma. The
complementary low-gcd signed covariance has not been bounded.
No critical-endpoint contraction follows from (16).
[ARITHMETIC-GCD-COVARIANCE](sol_covariance/ARITHMETIC-GCD-COVARIANCE.md)
proves the local identity, the complete regrouping, and the induction.

Second, the actual G_*, V_0, G_8 and C_z have pointwise integer-time
increments O_epsilon(X^epsilon) throughout the taper. The primitive
numerator proof works after differencing cancels its denominator
factor. The additional moving-mask jumps require r to divide
n+floor(X^(2/3)) or n-floor(X^(2/3)), so their count is also at
divisor scale. This directly checks the moving window.

Partition the exact taper into consecutive intervals I of length H,
with only the last possibly shorter. Let W_I=sum_(n in I)w(n) and
m_I(F)=sum_(n in I)w(n)F(n)/W_I. Apply this same weighted orthogonal
projection P_H to every sector. Then for any two listed sectors,

    |<F,G>_w-sum_I W_I m_I(F)conj(m_I(G))|
                    <<_epsilon X^(1+epsilon)H^2.              (17)

The cross terms with one mean and one fluctuation vanish exactly.
There is no loss from multiplying a reconstruction error by an
uncontrolled large sector mean. For H=floor(X^(1/2-delta)),
0<delta<1/2 fixed, (17) has strict power X^(2-2delta+epsilon).

Put E_*=widehat P-||G_*||_w^2, the inherited scalar error.
The complete exact reconstruction is

    Q_8=E_*+sum_I W_I|m_I(G_*)-m_I(V_0)+m_I(C_z)|^2
                  +||(1-P_H)(G_8+C_z)||_w^2.                 (18)

The last nonnegative term is bounded by (17), and E_* retains
its known O_epsilon(X^(2+epsilon)) bound. The common level square
is still open. The original prime-pair repeats, both mixed orders,
the moving mask and every time endpoint remain in it.
[COMMON-TAPER-COVARIANCE](sol_covariance/COMMON-TAPER-COVARIANCE.md)
gives the direct increment proof and all exact level weights.

## 7. Scope of the remaining work and of this evidence

The remaining requirement can now be stated as a bound on (14),
on the full two-square profile (7), on the positive low-gcd
covariance after (16), or on the complete level square in (18),
with their stated all-block quantifiers and allowed error scales.
These are compatible reductions of the same actual state. None
has been estimated at the required full scale in this round.
In particular the invalid shortcut in section 2 is not reused.

The report is supported by seven author proof files, four frozen
question records, same-session opposition notes and a root review.
An Astra and two Sols worked alongside the root Astra. Authors
and reviewers could read each other's proofs; this is neither
blind independent confirmation nor external mathematical review.
No new scientific numerical, symbolic or formal execution ran.
Administrative repository checks and hash custody do not promote
the candidate-D status.

The incoming basis is public draft
6a91ef48f6454743797614503aa5863dde54befb. Authority and collision
checks are recorded in the package RUN file. Adjacent public work
was read at ceb77e3632ec4617c54d8e1fd504d3b1c99dd106 and
fd6232aa10da26a374e421d6d46538b36b41aafb. The latter's growing
prime filters retain their own Möbius carriers; this report does
not import their squares or boundary signs into t without proof.
The source and interpretation differences are stated in the
author files. No Canon, registry, formal probe, checker, gate,
workflow or main-branch change is part of this continuation.
