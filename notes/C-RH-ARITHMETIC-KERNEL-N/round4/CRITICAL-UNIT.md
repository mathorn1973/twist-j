# The coefficient unit at the square-root boundary

**NON-CANONICAL. No authority. Candidate-D.** This is a paper continuation of C-RH-ARITHMETIC-KERNEL-N, issue #2087. It sharpens the coefficient-unit statement in [FOUNDATION](../FOUNDATION.md), without assuming RH or a zero-free region. No scientific computation was performed.

## 1. Exact absolute coefficients

Use the inherited character chi modulo five, split primes chi(p)=1, and the unit

    U(s) = product_split (1-t)^2/(1-2t)
           product_inert (1-t^2) times (1-5^(-s)),   t=p^(-s).

Write U(s)=sum u(n)n^(-s), U(s)^(-1)=sum v(n)n^(-s). The exact convolution identities are M=u*T and T=v*M, with the summatory meaning M(x)=sum u(d)T(x/d) and its inverse. Both coefficient series are absolutely convergent for Re s>1/2. Their local absolute coefficient factors are as follows; these are coefficientwise absolute values, not the modulus of an analytic factor.

| Prime type | Sum of absolute u coefficients | Sum of absolute v coefficients |
| --- | --- | --- |
| split | 1+t^2/(1-2t) | 1+t^2/(1-t)^2 |
| inert | 1+t^2 | 1/(1-t^2) |
| p=5 | 1+t | 1/(1-t) |

Let a_+(n)=|u(n)| and a_-(n)=|v(n)|. Removing their common quadratic contribution gives the exact Dirichlet identities

    sum a_+(n)n^(-s) = zeta(2s) H_+(s),
    sum a_-(n)n^(-s) = zeta(2s) H_-(s).                         (1)

The local factors of H_+ are (1-t^2)(1+t^2/(1-2t)) at split primes, 1-t^4 at inert primes, and (1-t^2)(1+t) at five. Those of H_- are 1+2t^3/(1-t) at split primes, 1 at inert primes, and 1+t at five. At every unramified prime the deviation now starts in degree at least three. The split geometric denominator in H_+ is harmless throughout Re s>1/3, since the first split prime is 11 and 2^3<11. Consequently both H_+ and H_- have absolutely convergent coefficient series in that half-plane. This convergence statement does not assert that their factors have no zeros there.

Put C_+=H_+(1/2) and C_-=H_-(1/2). Each is finite and strictly positive. Every real local factor at t=p^(-1/2) is positive; the deviations are summable, so the infinite products do not collapse to zero. In particular

    C_-=(1+1/sqrt(5)) product_split [1+2p^(-3/2)/(1-p^(-1/2))]. (2)

These are exact constants. No decimal evaluation is needed.

## 2. Square-root counting and a logarithmic endpoint norm

For either sign, write H(s)=sum h(d)d^(-s), a=a_+ or a_-. Coefficient comparison in (1) gives

    sum_(n<=x) a(n) = sum_(d<=x) h(d) floor(sqrt(x/d)).

Fix 1/3<sigma<1/2. Replacing the floor costs at most sum_(d<=x)|h(d)|=O_sigma(x^sigma). Completing the main coefficient sum to infinity costs at most

    sqrt(x) sum_(d>x) |h(d)|/sqrt(d)
       <= x^sigma sum_(d>x)|h(d)|/d^sigma = O_sigma(x^sigma).

Hence, with the matching C,

    sum_(n<=x) a(n) = C sqrt(x)+O_sigma(x^sigma).                (3)

Partial summation, including the term at n=1, now gives a constant B such that

    sum_(n<=x) a(n)/sqrt(n)
       = (C/2) log x+B+O_sigma(x^(sigma-1/2)).                  (4)

Indeed write the left side as A(x)/sqrt(x)+(1/2) integral_1^x A(y)y^(-3/2)dy. Inserting A(y)=C sqrt(y)+O(y^sigma) gives (4), since the error integral converges at infinity. Thus the absolute coefficient norm at the critical exponent is not bounded: it grows by exactly one logarithmic order in both directions of the transfer.

For any fixed real b>=0, the same argument yields

    sum_(d<=x) a(d)/sqrt(d) [log(e x/d)]^b
       = C/[2(b+1)] (log x)^(b+1)+O_b((1+log x)^b).             (5)

For b=0 this is (4). For b>0, regard the sum as a Stieltjes integral against (4), put y=log d, and integrate by parts. The linear part of (4) integrates to C[(1+log x)^(b+1)-1]/[2(b+1)]. The bounded remainder contributes O_b((1+log x)^b), including the endpoint mass. Replacing 1+log x by log x in the leading expression changes only that error.

Consequently an all-argument bound |M(x)|<=K sqrt(x)[log(e x)]^b implies

    |T(x)| <<_b K sqrt(x)[log(e x)]^(b+1),

and the reverse statement, with T and M exchanged, holds as well. Fixed finitely many small arguments may be absorbed in K. This assertion assumes the displayed pointwise premise; it does not establish that premise. Formula (5) proves that termwise absolute convolution of that positive envelope has precisely this extra logarithm. It does not say that the true signed functions must lose a logarithm or that their actual sizes have these asymptotics. A convolution of all arguments still does not transport an individual good window.

## 3. A signed square-supported factor

The inverse unit has a sharper signed decomposition

    U(s)^(-1) = L(2s,chi)^(-1) V(s).                            (6)

Its residual local factors are

    V_p(s) = (1-2t)/[(1-t)^2(1-t^2)]       (split),
             1/(1-t^4)                   (inert),
             1/(1-t)                     (p=5).

The split factor has no terms of degrees one or two. These factors define an absolutely convergent coefficient series V(s)=sum b(d)d^(-s) for Re s>1/3, since the deviations at unramified primes start in degree at least three and the denominators have their ordinary convergent geometric expansions. Multiplying the Euler factors verifies (6) first in the absolutely convergent half-plane Re s>1/2. As a formal coefficient identity it says, without any limiting argument,

    v(n)=sum_(q^2 d=n) mu(q)chi(q)b(d),
    T(x)=sum_(q^2 d<=x) mu(q)chi(q)b(d) M(x/(q^2 d)).           (7)

The residual b has finite absolute norm at 1/2. The critical harmonic size is isolated in the square-supported coefficient mu(q)chi(q), whose absolute convolution uses sum_(q<=sqrt(x)) |mu(q)chi(q)|/q. Formula (4), proved independently of cancellation in that coefficient, describes the resulting exact total variation. Applying a signed estimate to (7) would require controlling its correlation with the moving argument of M. No such correlation estimate is supplied here.

The identities derive from the already fixed local factors. They add neither a statement about zeros of L(s,chi) nor an assumption that RH for zeta implies GRH for chi. The standard elementary tools used are Euler-factor comparison, absolute Dirichlet convolution and partial summation; no historical priority is asserted.
