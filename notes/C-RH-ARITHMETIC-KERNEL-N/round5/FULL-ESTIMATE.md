# An unconditional estimate for the complete signed remainder

**NON-CANONICAL. No authority. Candidate-D, paper deduction with a named
classical analytic input.** The remaining all-epsilon bound of order
X^(2+epsilon) is **O**. This note estimates the actual sum of round 4,
not a replacement with absolute arithmetic coefficients.

## 1. The imported estimate and an exact coefficient bound

Write M(x)=sum_{n<=x} mu(n), T(x)=sum_{n<=x} t(n), and let v be the
Dirichlet coefficients of U^{-1} from FOUNDATION, Section 2. Thus

    t=mu*v,    T(x)=sum_{d<=x} v(d) M(x/d).

Both identities are exact. The absolute local coefficient series of v are

    split: 1+z^2/(1-z)^2;   inert: 1/(1-z^2);   at 5: 1/(1-z).

Put B=sum_d |v(d)|/d^(3/4). This is finite, and the following coarse
bound is completely explicit:

    B < 162.                                                        (1)

Indeed z=p^(-3/4)<1/2 at every split prime p>=11, so its local factor
is at most 1+4z^2 <= (1-z^2)^(-4). The inert factors are bounded by
the same fourth power. The exceptional factor at 5 is less than two.
Consequently B < 2 zeta(3/2)^4 < 2*3^4=162, using the integral bound
zeta(3/2)<1+integral_1^infinity u^(-3/2)du=3. The inequalities at the
exceptional primes follow by taking fourth powers of positive numbers;
no decimal evaluation or finite computation is used.

For u>1 put

    F(u)=u^(3/5)/(log u)^(1/5).

The only external analytic input in this note is an unconditional bound

    |M(x)| <= C x log x exp(-eta F(log x))     (x>=x0),              (2)

with fixed C,eta>0. A precise current primary source is Lee and Leong,
arXiv:2208.06141v5 (9 September 2026), Theorem 1.1, equation (12).
For example its displayed statement implies (2) with

    C=517/20,
    eta=(5/[3*(5399/100)^3])^(1/5),
    x0=exp(exp(1001/100)).

Here the source's additional factor
(1-log(5399/100)/log log x)^(-1/5) in the exponent is at least one
on the stated range, so dropping it weakens the published bound. These
constants are attributed to the source; its computations have not been
rerun in this package. No verified finite zero height is extrapolated to
all heights, and no Riemann hypothesis is an input. This uses v5 rather
than silently mixing the quantitative statements of v4 and v5.

## 2. Transfer without losing the exponential constant

**Candidate-D.** Under (2), for all sufficiently large x,

    |T(x)| <= C B x log x exp(-eta F(log x)) + B x^(7/8).            (3)

The threshold can be specified by x>=x0^2, (log x)/2>1, and

    eta sup_{u in [(log x)/2,log x]} |F'(u)| <= 1/4.

The last condition eventually holds because F'(u) tends to zero. This
description does not assert a numerical value of the resulting threshold.
It suffices for a finite, explicit-in-principle estimate.

To prove (3), put L=log x and first take d<=sqrt(x). The mean value
theorem gives

    F(L-log d) >= F(L) - (log d)/(4 eta).

Here x/d>=sqrt(x)>=x0, so (2) applies. Also log(x/d)<=L. Hence this
part of the convolution is at most

    C x L exp(-eta F(L)) sum_{d<=sqrt(x)} |v(d)|/d^(3/4).

For d>sqrt(x) use the elementary bound |M(x/d)|<=x/d and

    sum_{d>sqrt(x)} |v(d)|/d <= B x^(-1/8).

This proves (3). Since F(L)=o(L), the last term is eventually smaller
than the first envelope up to a fixed factor. In particular

    T(x) = O(x log x exp(-eta F(log x))).                            (4)

The same eta as in (2) is retained. Replacing a growing cutoff by a
fixed fraction of x and then weakening F was unnecessary. The argument
also applies to any nonnegative sublinear exponent function with derivative
tending to zero, provided the imported bound and its range are stated.

## 3. Both sides of the actual determinant remainder

Use exactly w, G_X, P_X and P_X^rem of round4/FINITE-TAPER. Denote

    E_T(X)=sum_n w(n)|T(n)|^2,
    E_G(X)=sum_n w(n)|G_X(n)|^2.

The support of w lies in [7X/8,17X/8] and has O(X) integers. For
u in this interval, log u=log X+O(1) and F(log u)=F(log X)+o(1),
uniformly. Applying (4) therefore gives

    E_T(X) << X^3 (log X)^2 exp(-2 eta F(log X)).                    (5)

The already proved approximation and same-conductor estimates are

    sum_{n in supp w}|T(n)-G_X(n)|^2 << X^2(1+log X)^5,
    E_G(X)=P_X+O(X^2 log(2X)).

The first estimate and the norm triangle inequality bound E_G by twice
the right side of (5) plus O(X^2(1+log X)^5). Its nonnegativity bounds
P_X from below by -O(X^2 log(2X)). Finally the exact large-gcd deletion
costs O_epsilon(X^(2+epsilon)) in absolute value. We have proved, for
every fixed epsilon>0 and all sufficiently late dyadic X,

    -C_epsilon X^(2+epsilon)
      <= P_X^rem
      <= C' X^3 (log X)^2 exp(-2 eta F(log X))
           + C_epsilon X^(2+epsilon).                              (6)

The constants may depend on the named fixed input and on epsilon,
not on a later choice of time window or coefficient mask. The same
upper bound applies to the positive part. The lower bound does not
state that P_X^rem is nonnegative; the exact retained off-diagonal
sum can have either sign.

For every fixed A>0, (6) implies

    (P_X^rem)_+ <<_A X^3/(log X)^A.

This is now an estimate of the **complete** actual remainder. Round 4,
Section 5 established such logarithmic savings only for its specified
top panel. The stronger shape in (6) comes from the stated classical
Mertens theorem and the exact unit transfer, not from a new zero-free
result.

## 4. The quantitative gap is not a limit interchange

The exponential factor in (6) can be written as X^(-delta(X)), where

    delta(X)=2 eta/[(log X)^(2/5)(log log X)^(1/5)] -> 0.

Thus the principal upper envelope is
X^(3-delta(X)) (log X)^2. It is smaller than X^3 by more than any
fixed logarithmic factor but remains larger than X^(3-delta0) for
every fixed delta0>0 on sufficiently late scales. This comparison is
between upper envelopes; it is **not** a lower bound for P_X^rem and
does not disprove a stronger estimate of the actual sum.

For each fixed 0<epsilon<1, the ratio of this envelope to the target
X^(2+epsilon) tends to infinity. Neither sending A to infinity in a
fixed-A logarithmic theorem nor choosing epsilon after observing X
establishes the all-epsilon target. The new numerator estimate and
short-interval estimates in this round control specified parts more
strongly; the still coupled low-height remainder needs an additional
argument.

## Source and scope record

- Primary input: https://arxiv.org/html/2208.06141v5#Thmtheorem1.1,
  Theorem 1.1 equation (12); the abstract version and the displayed
  hypothesis were checked. The rational constants above merely rewrite
  the source's finite decimals exactly.
- Internal algebra: FOUNDATION Section 2; round4/FINITE-TAPER Sections
  1--3. Those proofs and their frozen evidence are unchanged.
- Read: the source theorem and exact coefficient/taper definitions.
  Derived: (1), the constant-preserving transfer (3), and (6).
  Run: no scientific computation. Open: the all-epsilon power estimate.
- Same-session paper review is not external independent verification.
