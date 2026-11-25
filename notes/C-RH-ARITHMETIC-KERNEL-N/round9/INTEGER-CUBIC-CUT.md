# An integer cubic-moment cut and the retained joint squares

**NON-CANONICAL. No authority. Candidate-D paper deductions.**
C-RH-ARITHMETIC-KERNEL-N, round nine, owner issue 2087 and draft 2089.
Action layer NOT_APPLICABLE. The complete all-epsilon bound remains **O**.
This is within the frozen root question on the actual inverse, coefficient
units and joint short-factor compensation. No scientific execution is used.

## 1. An integer short factor with a zero cubic moment

All convolutions in this note are Dirichlet convolutions. Use the actual
integer coefficients t, their prefix T, and their positive inverse f from
the incoming round-eight draft. Put

    e = delta_1 - 2 delta_8,
    nu(n) = sum_(j>=0, 8^j|n) 2^j t(n/8^j).

Every sum at a fixed integer is finite, and e*nu=t exactly. No convergence
of an inverse series on a critical line is asserted or needed. Define the
nonnegative integer majorant

    gamma(n) = sum_(j>=0, 8^j|n) 2^j.

Since |t(n)|<=1, |nu(n)|<=gamma(n), and for every real L>=1,

    sum_(n<=L) gamma(n)
       = sum_(8^j<=L) 2^j floor(L/8^j)
       <= L sum_(j>=0)(1/4)^j = 4L/3.                           (1)

Freeze A=floor(X^(2/15)) on the dyadic block. Set

    q(n)=nu(n) 1_(n<=A),       a=e*q,       b=t-a.

Then a and b have integer coefficients. At n<=A, both terms in e*q
have their untruncated values, so a(n)=t(n). Hence b(n)=0 through A.
The support of a is at most 8A. Above A its only possible nonzero
coefficients are a(8m)=-2 nu(m), with A<8m<=8A and m<=A.
The short coefficients need not be bounded pointwise. Their weighted
absolute sums, rather than a pointwise bound, will pay the rectangle.

The cubic moment vanishes exactly:

    sum_n a(n)n^(-1/3)
      = (1-2*8^(-1/3)) sum_(m<=A) nu(m)m^(-1/3) = 0.             (2)

The harmonic moment and the total short mass are respectively

    h(a) = (3/4) sum_(m<=A) nu(m)/m,
    sum_n a(n) = -sum_(m<=A) nu(m).                             (3)

Thus h(a) is rational. The only cube root used to cancel the moment
is the exact equality 8^(1/3)=2. In particular this construction does
not require irrational coefficient weights. Partial summation in (1)
gives, for each fixed 0<=theta<1,

    sum_n |a(n)|n^(-theta)
       <= (1+2*8^(-theta)) sum_(m<=A)|nu(m)|m^(-theta)
       <<_theta A^(1-theta).                                  (4)

In particular sum|a|=O(A), uniformly in the block. This is the precise
replacement for the bounded-short-coefficient hypothesis in the other
longer-cut proof.

## 2. The complete integer profile at square-root error

The independently authored inverse mean in
[LONGER-FACTOR-CUT](sol_squares/LONGER-FACTOR-CUT.md) is

    F(y)=sum_(k<=y) f(k)
       = U(1)y+C_U zeta(1/3)y^(1/3)+O(y^(7/22)),                (5)

where f(k)>=0, U(1)>0 and C_U>0. Its paper derivation and primary
analytic inputs are retained in that file. The algebraic identity

    t=2a-f*a*a+f*b*b                                           (6)

holds for the integer a just defined, since f*t=delta_1. For all
sufficiently large X, (8A)^2<=7X/8. Every argument of F in the short
rectangle is therefore at least one on the entire original taper.
Its linear term is n U(1) h(a)^2. Its cubic term is zero by (2).
Using (4) with theta=7/22, the total error in that rectangle is

    << X^(7/22) (sum_m |a(m)|m^(-7/22))^2
    << X^(7/22) A^(15/11) = O(sqrt X).                         (7)

The other short term 2 sum a is O(A) by (1) and (3). No individual
large value of nu is discarded in these estimates.

Extend prefixes by their floor and by zero below one. Put

    B_b(v)=sum_(m<=v)b(m),        r_k=floor(sqrt(n/k)),
    L_b(n)=2 sum_(k<=n/(A+1)^2) f(k)
                 sum_(A<m<=r_k) b(m) B_b(n/(km)),
    S_b(n)=sum_(k<=n/(A+1)^2) f(k) B_b(r_k)^2 >=0.

At fixed k, every pair m,m'>A with kmm'<=n has at least one
coordinate at most r_k. The intersection of the two orientations
is exactly the entire square A<m,m'<=r_k. This finite partition
proves that the long rectangle in (6) is L_b-S_b, including all
floor boundaries. Consequently the original time window satisfies

    T(n)=Z_X(n)+O(sqrt X),
    Z_X(n)=L_b(n)-n U(1)h(a)^2-S_b(n).                         (8)

Both penalties retain negative signs. The affine square uses a;
the overlap and linear terms use the same actual b=t-a.
Every nonzero linear argument is at most n/(A+1),
hence O(X^(13/15)); square arguments are at most sqrt n. If
V(v)=sum_(m<=v)nu(m), the prefix is explicitly

    B_b(v)=T(v)-V(min(v,A))+2V(min(v/8,A)),                     (9)
    V(v)=sum_(8^j<=v)2^j T(v/8^j).

The additional V arguments in (9) are at most A. The cutoff and
coefficients remain fixed throughout the current block. This is a
new integer version of the longer cut, not a change to the previously
frozen constant-padding construction.

Equation (8) gives ||T-Z_X||_w^2=O(X^2). Together with the incoming
round-eight norm comparisons it preserves the full all-epsilon
Q8 criterion, with all original mixed terms present through the
complete amplitude. At the strict exponent X^2 the incoming
Fourier comparison still has epsilon slack; no stronger transfer
is claimed.

## 3. The overlap remains necessary on complete windows

The integer construction does not make S_b dispensable. In A<m<=2A,
if 5 does not divide m and 8 does not divide m, then a(m)=0 and
|b(m)|=|t(m)|=1. Such edges have density 7/10, up to O(1) endpoints.
Because B_b(A)=0 and B_b takes integer values, at least a constant
multiple of A indices m in this interval satisfy B_b(m)^2>=1.

For each such m, the mass of f at indices where r_k=m is

    F(n/m^2)-F(n/(m+1)^2) >> X/A^3.                            (10)

This already follows from the weaker incoming mean
F(y)=U(1)y+O(y^(5/12)): the error-to-main ratio is
O(X^(-7/12)A^(13/6))=o(1). Endpoints are strict below and inclusive
above, exactly as written. Positivity of f and the disjoint bins
then give S_b(n)>>X/A^2 uniformly on the full taper.

The proof of arbitrarily late positive times T(n_0)>0 and the
signed power-window result are in
[SQUARE-RETENTION](sol_squares/SQUARE-RETENTION.md). At such a
central time in a dyadic block, |T(n)-T(n_0)|<=|n-n_0| gives
an interval of length comparable to X/A^2, still in [X,2X),
on which T is no more negative than a sufficiently small multiple
of X/A^2. The O(sqrt X) error in (8) is smaller than that scale.
It follows that, on infinitely many dyadic blocks,

    ||(L_b-n U(1)h(a)^2)_+||_w^2 >> (X/A^2)^3 = X^(11/5).      (11)

There is also a complete-window statement. Stitch Z_X and the
corresponding simplified profiles using the unique dyadic X with
X<=n<2X. For every sufficiently large Y, apply the inherited
signed power-window lemma to obtain n_0 in
[Y^(5/4),Y^(3/2)] with T(n_0)>0. The dyadic block containing it
is contained in [Y,Y^2) for large Y. On its selected interval,
the original weights 1/[n(n+1)] are bounded below by a constant
times X^(-2). Thus omitting only S_b yields weighted positive
energy at least

    c X^(1/5) >= c' Y^(1/4)                                  (12)

on every sufficiently late complete window. This rules out the
all-exponent one-sided criterion for that simplified profile.
The lower bound does not apply to the full Z_X in (8).

For comparison, the same argument applied to the unchanged strict
round-eight cutoff A=floor(X^(1/14)) and the overlap lower bound
in SQUARE-RETENTION gives weighted positive energy >>Y^(5/7) on
every sufficiently late complete window. No shifted cutoff is
needed to exclude that earlier overlap-deletion shortcut. The
separate affine-deletion statement has the shifted-cutoff scope
specified in the author proof.

## 4. Scope and composition

This proof establishes an integer, rational-harmonic short-factor
construction, a complete two-negative-square comparison with
smaller upper arguments, and actual lower bounds when its overlap
penalty is removed. It supplies no bound for the complete L_b
minus both penalties. That bound remains O.

One can compose (8) with the rough-prime completion without
replacing the inverse f. Stitch the full Z_X as above, using T
itself on a finite set of initial blocks. The pointwise error is
O(sqrt u) globally. For the positive completion coefficients h_y
of [ROUGH-COMPLETION](astra_joint/ROUGH-COMPLETION-AND-CRITICAL-THRESHOLD.md)
and any fixed sigma>1/2, their absolute sum weighted by d^(-sigma)
is uniformly bounded for y=log X. Hence, with A_X denoting the
entire d>1 signed rough sum in that proof,

    A_X(n)=sum_(d<=n) h_y(d) Z(n/d)-T_y(n)+O_sigma(X^sigma).     (13)

Here h_y(1)=1. All smaller profiles retain both negative squares
under their positive h_y weights. The original cutoff y is
frozen in this outer sum, while the inner Z has its own specified
dyadic cutoff at its actual argument. Formula (13) is an
all-epsilon norm comparison only; it is not a strict critical
estimate or a newly proved bound for its entire signed amplitude.

The arithmetic basis is the incoming public draft
6a91ef48f6454743797614503aa5863dde54befb. The refined mean and
rough operator are the reviewed round-nine author deductions
linked above. The finite geometric identity (1), cancellation
(2), and applications (7)--(13) are paper deductions in this
same session, not independent external confirmation or a Canon
promotion. No new scientific numerical, symbolic or formal
execution was performed.
