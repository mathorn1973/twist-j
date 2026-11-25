# Exact tail and transfer of the rational window condition

NON-CANONICAL. C-RH-ARITHMETIC-KERNEL-N, issue #2087.
Status: candidate-D for the deductions; O for the final tail estimate.

## Definitions

Let chi be the quadratic character modulo 5 and let H(q)=sum_{m<=q}chi(m).
Then H takes the periodic values (0,1,0,-1,0). Let a(d)=(-2)^omega(d) when
d is squarefree and all its prime factors are 1 or 4 modulo 5, with a(1)=1;
otherwise let a(d)=0. Put

    T(n) = sum_{d<=n} a(d) H(floor(n/d)),
    D_n = max{d>=0: d^3<=n^2},
    B(n) = sum_{d<=D_n} a(d) H(floor(n/d)),
    R(n) = T(n)-B(n).

These are integer functions, and the boundary uses only an integer comparison.
Write A(u)=sum_{d<=u}a(d), with A(0)=0. Define the positive rational quadratic
window and the two-sided window by

    Q_F(Y) = sum_{n=Y}^{Y^2-1} max(F(n),0)^2/[n(n+1)],
    E_F(Y) = sum_{n=Y}^{Y^2-1} |F(n)|^2/[n(n+1)].

## Exact quotient formula (candidate-D)

For every n>=1 put K_n=floor(n/(D_n+1)). Then

    R(n)=sum_{k=1}^{K_n} H(k)
          [A(floor(n/k))-A(max(D_n,floor(n/(k+1))))].            (1)

Indeed floor(n/d)=k iff floor(n/(k+1))<d<=floor(n/k). Intersect this integer
interval with d>D_n and sum a(d). For k<=K_n its upper endpoint is at least
D_n+1, so the displayed interval is never reversed. For k>K_n it is empty.
Also D_n+1>n^(2/3), hence K_n<n^(1/3). Only k=1 or 3 modulo 5 contribute.
This is a short *quotient index*, not an estimate for the long sums A.

## Deterministic same-window transfer (candidate-D)

The kernel proof establishes unconditionally

    E_B(Y) <= C(1+log Y)^4                                      (2)

for an absolute constant C and all integers Y>=2. The weaker logarithmic
seventh-power proof was also retained and checked; either exponent suffices
for the transfer below. Since u -> max(u,0) is 1-Lipschitz, the triangle
inequality in the finite weighted Euclidean space gives

    |sqrt(Q_T(Y))-sqrt(Q_R(Y))|
       <= sqrt(E_B(Y)) <= sqrt(C)(1+log Y)^2.                    (3)

For an integer-valued F let W(F) denote

    for every integer r>=1 and every Y0>=1,
    some integer Y>=max(2,Y0) satisfies Q_F(Y)^r<=Y.

Then W(T) iff W(R). To prove W(T) implies W(R), fix r and take arbitrarily
late windows for exponent 2r. On those windows Q_T(Y)<=Y^(1/(2r)). From
(3),

    Q_R(Y) <= 2Y^(1/(2r))+2C(1+log Y)^4 <= Y^(1/r)

once Y is sufficiently large. The reverse implication uses the same
inequality with T and R interchanged. This proof is purely a comparison of
the same finite windows; it does not assume that convolution preserves an
isolated good window. The negative-part version follows in exactly the same
way by applying the 1-Lipschitz map u -> max(-u,0).

The [window foundation](FOUNDATION.md), retained from the preceding
C-RH-2D-SYNTHESIS-N packet, supplies the separately proved equivalence
W(T) iff RH, including the nearest-pole signed window argument.
Combined with that theorem, W(R) iff RH. Here the new unconditional content is
the removal of B by (2); no estimate for W(R) has been established.

## Exact integer certificate for one window

Let L_Y=lcm(Y,Y+1,...,Y^2) and

    A_R(Y)=sum_{n=Y}^{Y^2-1} max(R(n),0)^2 L_Y/[n(n+1)].

Each summand is an integer because consecutive n and n+1 are coprime and
both divide L_Y. Thus Q_R(Y)^r<=Y iff A_R(Y)^r<=Y L_Y^r. This describes
verification of a supplied window, not a method for proving arbitrarily
late successful windows. The all-r and arbitrarily-late quantifiers remain
essential.

## A proved prime contribution, and what it does not prove

Put P(n)=-2 sum_{D_n<p<=n, chi(p)=1} H(floor(n/p)). The fixed-modulus prime
number theorem gives

    P(n) ~ -L(1,chi) n/log n,                                  (4)
    L(1,chi)=sum_{k>=1} H(k)/[k(k+1)] > 0.

For a fixed K, count split primes in (n/(k+1),n/k] using
pi_split(x)~x/(2log x), for 1<=k<=K. Their weighted limit is the first K
terms of the displayed convergent series. The omitted quotient range is
bounded in absolute value by 2 pi_split(n/(K+1)); after division by n/log n,
its limsup is O(1/K). The exclusion p<=D_n costs at most 2D_n, which is
o(n/log n). First let n tend to infinity, then K tend to infinity.

The positivity requires no special-value formula: group the series in
blocks of five to get

    L(1,chi)=sum_{j>=0}
      [1/((5j+1)(5j+2))-1/((5j+3)(5j+4))] > 0.

This component is too large in magnitude to bound separately at a square-root
scale. Its negative sign alone creates no positive-part obstruction. The
rough-support note proves a complementary *positive* obstruction and records
the cancellation required between the two pieces. The rough asymptotic uses the classical prime number theorem. The opposite
positive main term also uses the classical unconditional Mertens rate and
the absolutely convergent coefficient unit. None is an RH assumption.

## Remaining arithmetic obligation (O)

Prove W(R) directly from the signed arithmetic of (1), or prove a stronger
bound sufficient for it. The known local kernels, gcd correlations, prime
counts, recovery of a modulus, and bounded quotient index do not by themselves
supply this estimate. In particular, replacing signed interval sums by
their absolute values discards cancellations already necessary at n/log n.
