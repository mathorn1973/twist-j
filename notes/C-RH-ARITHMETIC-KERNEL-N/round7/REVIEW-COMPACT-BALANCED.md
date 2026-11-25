# Paper opposition of the compact balanced carrier

**NON-CANONICAL. No authority. Candidate-D, same-session paper review.**
Issue 2087, draft 2089. I checked COMPACT-BALANCED-BAND against the
pinned round-six unit tail, taper and maximal short-sum estimates, the
round-five unit transfer and the attributed neighboring double partial
summation method. I also checked equation (12) of the cited primary
Mertens paper. No scientific executable, numerical evaluation or
external independent confirmation.

**Disposition.** Equations (7), (9), (12), (13), (14) and the buffered
whole-block observation (15) survive. In (15) the finite time mask and
the convolution apply jointly to the core and its exact prime correction.
The longer carrier can omit its complete unit tail at the stated cost.
Its affine term retains both masked coefficients. The square-root-scale
joint estimate is open.

## Compactification, spectral costs and coefficient scope

Throughout the original taper, all forward shifts by at most J(H-1)
satisfy 2A<=n+s<=3X and exceed either unit cutoff, for sufficiently
large X. This uses JH=o(X), A of order sqrt(X), and the fixed upper
and lower margins of the taper. A raw denominator above 3X has zero
floor at each such time. The masked floor sum therefore agrees exactly
with the original one, before rewriting it as centered sawteeth. The
constant term and slope in its rewrite both involve the mask. For
integer time, the ordinary zero harmonic of the centered sawtooth is
zero; summing j e(-aj/q) over one period gives the asserted negative
nonzero coefficient. The average includes the expected forward shift
J(H-1)/2 in its slope.

For the first shorter L, N L^(sigma-1) is at most a constant times
sqrt(X) exp(-(1-sigma)sqrt(log X)). The round-six maximal bound on
almost all starts is used in square norm. It controls all prefix
lengths from each start by one maximum at length J(H-1). This length
has fixed polynomial margins near X^(1/2) for the dyadic starts
required here; its logarithmic excess can be paid at any fixed
inverse-log order. No pointwise assertion at every starting n is
needed for (4).

The raw majorant is rho=|u|*tau. At a split prime p its prime-power
values are 2^h at p^h, so a pointwise O_epsilon(q^epsilon) estimate
for this majorant for every epsilon would be false. The argument
correctly uses the submultiplicativity, harmonic bound and second
moment of rho established in round six. They give
|q sum_(q|d)z(d)/d| << rho(q)(1+log X)^2 and the box coefficient
mass O(R(1+log X)^7/B). On raw d the harmonic mass is O(log(2d));
its sum against rho(d) is O(X(1+log X)^2). For a box omitted at
R>=sqrt(X), its R^3/B cost is O(X^2 exp(-sqrt(log X))) even when
its threshold is below one, as that case itself bounds R^3. Smaller
R costs at most O(X^(3/2)) before logarithms. The triangle
inequality over boxes retains all cross products through the norm.
The reduction to raw harmonics in the slow band is valid: nonzero
reduced frequencies satisfy q>=X/(2K), |a|<=8K, and their box
cutoff exceeds 8K when K<=X^(1/10). Forward averaging preserves
these same frequencies.

## Double partial summation and the inherited exponential constant

For small k, the slow raw kernels (or their derivatives) vanish at
the lower integration edges a=Z or b=Z, including when the other
variable is 2A. At the upper edges the padded coefficient prefix
vanishes exactly. Two integrations by parts against step prefixes
give D_q^2 f(kab)/(ab). The two prefix bounds provide factors a,b.
The area with kab<=4X is O((X/k)(1+log X)). For k>k_0 the signed
difference U_sum(y)-U_sum(k_0) is O(y^(1/3)) for y>=k_0; differentiating
a kernel in y costs one logarithmic derivative divided by y. The
upper y boundary and integral are both O((1+K)W^(1/3)/j) for
harmonic j>0. Summing over ab<=4X/k_0 supplies the factor
X k_0^(-2/3). No estimate for individual signed unit coefficients
was used in this large-k range.

In [Lee and Leong, v5, Theorem 1.1, equation (12)](https://arxiv.org/html/2208.06141v5)
the Mertens estimate holds unconditionally starting from
exp(exp(1001/100)). The source's stated exponential coefficient may
be weakened to gamma=(5/[3(5399/100)^3])^(1/5). The pinned round-five
convolution with v preserves this fixed gamma for T eventually via
absolute convergence at 3/4. No source computations were repeated.
With K=exp(lambda Phi(sqrt(X))) and k_0=exp(nu Phi(sqrt(X))),
both cutoffs stay inside the polynomial margins and log Z differs
from log(sqrt(X)) by O(Phi(sqrt(X))). The corresponding Phi values
have ratio tending to one, also for Z_0 in (12). The large-k term
has exponential saving 2nu/3-lambda, exceeding 2gamma-2lambda.
Passing to Phi(X) multiplies the latter saving by 2^(-3/5);
the stated lambda range gives the strict improvement over gamma
for this designated component. The bound remains above every
fixed X^(1-delta) in its principal upper envelope.

## The full affine part and longer cutoff

For the constant affine term at each small k, subtracting one from
eta(kab/X) has zero effect because the complete padded sum of c(a)
vanishes. The new kernel is zero on the lower integration edges;
its mixed derivative is supported on 3X<=kab<=4X, regardless of
its constant value at larger arguments. The upper boundary again
vanishes by the balanced prefix. At large k use the compact eta
itself, so W=min(L,4X/(ab)) and the signed unit sum and area cost
of the previous paragraph apply with bounded kernel and derivative.

For the slope, the unmasked sum over kab has the exact factor
alpha_L h_X^2, with |alpha_L| bounded by the absolute norm of u at
one. Its change from masking uses (1-eta(q/X)) ell(n)/q. At small
k both lower boundaries vanish; its second logarithmic derivative
is O(X/q), so after prefix cancellation the integral of X/(kab)
over the two variables costs O((X/k)(1+log X)^2). At large k the
endpoint costs O(X L^(-2/3)/(ab)), and the integrated derivative
costs O((X/(ab)) integral_(k_0)^L y^(-5/3)dy). Their sum is
O(X k_0^(-2/3)/(ab)); both remaining harmonic sums are finite
with squared-log cost. These checks include the removed large
raw denominators, even though the correction for the slope itself
has no compact upper support.

Partial summation of the convergent series sum t(n)/n yields a
tail bounded by |T(A)|/A+integral_A^infinity |T(x)|dx/x^2.
Its total is zero by the Mellin value at one. Bound the integral
using the split exponential factor at a fixed delta>0, with the
remaining integrable factor carrying the logarithm. Padding contributes
at most |T(A)|/A. Thus |h_X| <<_delta exp(-(gamma-delta)Phi(A)).
Taking 0<delta<lambda makes the full square drift fit (13).
The cubic correction satisfies |C_L(N)| << N L^(-2/3) by the
absolute linear summatory bound on |mu*v*v| and a weighted partial
summation. This polynomial scale fits (13) uniformly on the needed
forward shifts. The shorter carrier still includes the signed cubic
correction in (7).

For L_+=ceil(X^(3/4) exp(sqrt(log X))), the same linear-mean
calculation and U_sum(x)=O(x^(1/3)) bound the complete discarded
unit tail by O(sqrt(X) exp(-(2/3)sqrt(log X))) pointwise on the
required slab. Its weighted norm therefore costs O_D(X/log^D X)
for every fixed D. The raw cutoff still vanishes above 4X, the
two moment bounds on rho are uniform in the unit cutoff, and
neither partial summation requires L to take its original shorter
value. Construction of the longer coefficients anew proves (14)
with no explicit cubic term. This does not assert equality of the
two balanced spectra.

## Finite block convolution and the power window

Set P=kh. On each half of I^+, every translate of size at most P
directed towards the opposite end stays inside I^+, since its
half-length is at least P. Symmetry and positivity of the averaging
probability give w>=1/2 on all of I^+, including both boundary
points. Rounding gives P>=X/32 on late scales. Consequently the
ordinary square norm of the difference of the two time profiles
on I^+ is at most sqrt(2) times its w-norm. Cauchy-Schwarz with
||p||_2 << sqrt(K/X) gives the claimed pointwise difference
O_eps(X^(1/2+eps) sqrt(K)) after convolution. No comparison of
the profiles on unrestricted integer time is needed.

For an observed n anywhere in the full [X,2X) block, shifts leaving
I^+ have |j|>=P. The cutoff coefficient decay has tail sum
O_M((1+KP/X)^(1-M))=O_M(K^(1-M)). The absolute harmonic mass bound
controls the global periodic balanced oscillatory term even outside
the time slab, so extending that part alone costs
O_M(X(1+log X)^2 K^(1-M)). The truncated affine part is covered
on I^+ by (12) and the absolute l1 norm of p. The true slow band
of the globally extended oscillatory part is covered on the target
block by the f_0-omitted version of (9). The strict choice
(M-1)lambda>2gamma-2lambda pays the logarithms in the periodic
extension cost. Any fixed eps<1/2 pays the prior comparison term
since K and the reciprocal exponential saving are subpower in X.
This proves (15) for the specified filtered and masked joint
profile up to both block edges.

For either carrier, pointwise positivity truncation is one-Lipschitz.
Norm error on one complete or partial dyadic block inside [Y,Y^2)
is bounded using w=1 there and n(n+1)>=X^2. The O(log Y) blocks
are harmless by increasing the input inverse-log exponent. Passing
from source window exponent 2r to r absorbs this uniform norm error
in either direction on the same late windows. None of (7), (13)
or (15) supplies the missing full signed power bound.
