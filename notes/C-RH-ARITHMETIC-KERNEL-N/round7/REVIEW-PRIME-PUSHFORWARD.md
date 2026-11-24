# Paper opposition of the cube-root prime pushforward

**NON-CANONICAL. No authority. Candidate-D, same-session paper review.**
Owner 2087, draft 2089. I read the integer-dilation version of
PRIME-PUSHFORWARD.md, the prospective scope, the round-six core and
its uniform numerator estimate, and round-three LARGE-PRIME-TAIL for
the unconditional Mellin-moment input. No scientific executable,
numerical experiment or independent confirmation.

**Disposition.** The exact mixed expression, cube-root drift, fixed
logarithmic expansions and stated integer-probe lower bounds survive
the checks below. At an exceptional derivative zero, the same power
obstruction holds for a possibly larger logarithmic exponent, as
specified in the last paragraph. The positive-part estimate for the
actual full core remains open.

## Pushforward and uniform prime averages

For a positive integer product d, floor(n/d)=m is equivalent to
n/(m+1)<d<=n/m. The pushforward therefore gives all the stated
weights, including four on an unordered repeated prime. The reality
of the conjugate-paired core identifies the linear term as
-2 T^t W^t diag(w) G_core. The quadratic term is the nonnegative
Gram form T^t W^t diag(w) W T. Its sign says nothing separately
about the mixed term.

For the first sum, write F(v)=sum_(m<=v) Delta F(m), replace the two
cumulative prime counts at y=n/m and z by their fixed-modulus main
terms, then integrate t from z to y. The errors are O_A(y/L^A)
for y>=z. For ordered pairs at y>=z^2, first sum over z<p<=y/z.
Approximating the inner cumulative counts costs at most
O_A(L^(-A) sum_p (y/p+z))=O_A(y L^(1-A)). For the outer prime
measure write f(t)=Li(y/t)-Li(z). Its upper endpoint value vanishes,
its lower endpoint error is O_A(y/L^(A+1)), and the integrated
Stieltjes error is at most a constant times
y L^(-A-1) integral_(z)^(y/z) dt/t=O_A(y/L^A).
These are absolute endpoint estimates even when y is close to z^2.
Summing against |Delta F(m)| gives exactly the advertised shape.
No equidistribution of primes in individual floor bins is assumed.

Four times the unordered count equals twice the ordered count plus
twice the diagonal. The ordered integral has density
dt dv/(4 log(t) log(v)). For u=n/(tv), the remaining logarithmic
coordinate has range [a,b-a], and the integral of 1/[s(b-s)]
there is (2/b)log((b-a)/a). The density factor 1/4, ordered
coefficient -2 and integral factor 2 yield -n/ell times g_a.
The separate diagonal has coefficient -2. This reconstructs (2)
including both signs and cutoffs. The split-prime approximation uses
only the classical prime number theorem for the fixed modulus five
with an arbitrary fixed logarithmic error, as previously recorded
and attributed to the introduction of [Yamada's paper](https://arxiv.org/html/1306.5322v4#S1).

## Actual sequence, derivative and heights

For T, |Delta T(m)|<=1 gives O_A(X L^(2-A)) for the prime count
errors. The diagonal costs O(X/z) by summing over all integers
above z. Both integral cutoffs tend to infinity at a polynomial
rate uniformly in n. The unconditional bound for T bounds the tail
of each j-th absolute moment by an integral of
v^j exp(-c sqrt(v)) beginning at a constant times L. Thus the
moment substitutions and every fixed-order Taylor remainder are
uniform. On their separate intervals b>=a and b>=2a the kernel
derivatives are bounded for a in a compact neighborhood of 1/3.
This avoids extending g_a through its singularity.

The j-th logarithmic moment is (-1)^j G_T^(j)(1), obtained by
descending to 1 from Re(s)>1 under the integrable absolute
majorant. This cancels the Taylor sign from b=1-log(u)/ell.
In particular G_T(1)=0 and G_T'(1)=kappa. Direct differentiation
gives h_a'(1)=a/(1-a)-log((1-a)/a). With a=1/3+O(1/L),
the coefficient for C_z is kappa(log 2-1/2)>0. This verifies
both the leading term (3) and the sign in (4) for arbitrary fixed
order. No fixed-log expansion gives a power of X in the saving.

The full norm comparison and the unconditional bound on T give
||G_core+C_z||_w <<_B X^(3/2)/L^B for each fixed B. Thus the core
approximates the negative drift to the same fixed-log accuracy, and
the mixed product has both orders, giving the coefficient -2.
The original determinant comparison contributes O_eps(X^(2+eps))
only where it is applied to its own restricted spectrum. The
height estimate removes h>L^14 at a norm cost O(X^(3/2)/L^4)
uniformly in the conductor mask. Pairing with either full amplitude
of norm O(X^(3/2)/L^2) costs O(X^3/L^6). This proves the leading
claims for the limited heights while C_z stays whole. The assertion
of cancellation through every fixed logarithmic order uses the full
core.

## Integer probes and the power obstruction

At a new stage, a collision in products from distinct choices would
force one of the six ordered ratios of r, r+1, r(r+1) to equal
a ratio from a finite fixed set. All six rational functions are
nonconstant. A coincidence with the same new factor would already
have been a collision at the previous stage. Induction therefore
gives distinct final products. Choosing eta after the finitely many
products yields disjoint closed dilated intervals with gaps of
length >>_k M. This also covers the single product for k=0.

For integer d, floor(floor(u)/d)=floor(u/d). Each dilate is thus an
integer-step function whose jump at each integer has magnitude at
most one, and its nonzero support stays in [dM,d A_M]. The positive
gaps prevent different dilates from jumping at adjacent boundaries.
Its height is at most sqrt(M)<=sqrt(m) on the support. Each ramp
has total variation at most 2q, so after summing 3^k dilates one
has sum_m |Delta F_X(m)|/m <<_k M^(-1/2). Bounded total ratio of
supported arguments gives the stated weighted energy bound.

Changing variables u=dv contributes d^(-1). The portions v<1
are zero. Each independent signed reciprocal sum over the triple
vanishes. Every multinomial of centered degree <k therefore has
a missing triple and vanishes. At degree k only one first power
from each triple can remain, and its factor is the product of
positive first-log moments times k!. In each factor the positive
reciprocal weights add to 1/r and both positive choices have log
strictly greater than log r. The ramp at height q occupies a fixed
proportion of its interval, giving integral B_M(v)dv/v^2 of order
M^(-1/2), also for k=0. This recovers the claimed nonzero centered
moment and the binomial implication for the original moments.

For fixed delta<1/3, all of [M,B_k M] lies below the two-prime
ceiling n/z^2. For delta>=1/3 and delta<2/3 it lies above that
ceiling and below n/z. At equality 1/3, the strict comparison
17/8<4^(2/3) leaves a fixed margin before flooring M.
Every absolute centered moment of the bounded support is
O_k(M^(-1/2)) at each fixed order. This bounds the Taylor
remainder in (7). The cumulative count error has the same cost
by taking A>=k+3, and the exact diagonal costs O(sqrt(X)) by the
bounded reciprocal prime sum above z. The latter is negligible
even relative to X M^(-1/2) L^(-k-2). The first nonvanishing
kernel derivative stabilizes uniformly away from zero in the
ranges stated in the author note. A whole block with w=1 yields
the lower bound, with the matching upper bound on the full
support. For the generic upper bound, the inner prime estimate
sum_(q<=Y/p) q^(-1/2) << sqrt(Y/p)/log(Y/p) is used only if
Y/p>=z. The remaining sum in 1/p is bounded, proving the claimed
power comparison.

For delta<1/3 the logarithmic exponent 2k+2 in (6) is claimed
only where h_(1/3)^(k)(1-delta) is nonzero. This condition can
matter: at k=1 the derivative changes sign between b=2/3 and b=1.
For **every** fixed delta in (0,2/3), the power obstruction with
at least k vanishing moments follows. At any exceptional delta
choose a finite j>k with h_(1/3)^(j)(1-delta) nonzero, which
exists because h is real analytic and nonpolynomial on its
connected domain. Construct the j-triple probe. It retains all k
required zero moments and gives X^(3-delta)/L^(2j+2) in squared
norm. In this formulation j and the support constant may depend
on (k,delta). No uniform claim at drifting delta or about the
arithmetic sequence T follows from these probes.
