# Joint covariance under one finite-taper projection

**NON-CANONICAL. No authority. Candidate-D paper deduction.** Round nine, C-RH-ARITHMETIC-KERNEL-N, issue #2087, draft #2089. Action layer NOT_APPLICABLE. The full Q8 estimate remains **O**. Use source draft `6a91ef48f6454743797614503aa5863dde54befb` and the frozen lane question. This proof bounds the actual covariance lost when the original sectors are projected together onto common time levels, at a genuinely additive precision.

## 1. The specified sectors have pointwise increments at divisor scale

Use the original `X,D,z,w,G_*,V_0,G_8,C_z,Q_8` from round-eight REPORT §§1–5, with no change to the time mask, coefficient weights, or numerator restrictions. For a function on integer time write `Delta F(n)=F(n)-F(n-1)`. Use the ambient interval `[7X/8,17X/8]` around the taper. The real functions involved are well defined on this interval and one adjoining point at each end. For sufficiently late dyadic `X`, all these times are positive and below `D`.

For each surviving conductor let `g_r(n)` be its full original retained primitive packet, including `A_r`, `b(r,a)` and the original Jackson multiplier `m_X(a/(5r))`. Thus `G_*` is a fixed sum of `g_r`. The exact difference of a term cancels its denominator factor:

\[
 \Delta g_r(n)=\frac{A_r\tau}{5r}
   \sum_{a\in\mathcal A_r}\chi_5(a)m_X(a/(5r)) e(an/(5r)).            \tag{1}
\]

Here `e(x)=exp(2 pi i x)`, `tau` is the original Gauss sum, and `A_r=O_epsilon(X^epsilon)` by its harmonic cofactor bound. We prove on the ambient interval that

\[
 \left|\sum_{r\in\mathcal F_n}\Delta g_r(n)\right|
                                      \ll_\epsilon X^\epsilon        \tag{2}
\]

for an arbitrary subset `F_n` of its fixed actual conductors, with the subset chosen separately at each evaluation time `n`. The derivative here is of each fixed `g_r`, before that selection.

Fix one original shell `R<r<=min(2R,D)` and one signed dyadic numerator box `A<=|a|<2A`. For each `r`, all original magnitude and height cuts restrict this box to an interval before imposing coprimality. Use `chi_5(a)=0` if five divides `a`, and impose `(a,r)=1` by `sum_(d|(a,r))mu(d)`. Write `r=dq`, `|a|=dj`, `Q=R/d`. The factor `chi_5(j)` is a linear combination of five additive phases. In each of them, summation by parts over the allowed consecutive `j` interval uses the supremum plus variation `O(1/R)` of `m_X(a/(5r))/(5r)`. The original rescaled Jackson profile has bounded variation; neither the numerical cap nor the upper support boundary increases that estimate beyond an absolute constant. The geometric progression has phase `(+/- n+hq)/(5q)` for an integer `h`, whose circular distance from an integer is at least `j_0/(5q)`, where `j_0=dist(n,q Z)`. Hence the geometric bound before the `O(1/R)` factor is

\[
 O\left(\min\{A/d,Q/j_0\}\right)\quad(j_0>0),
 \qquad O(A/d)\quad(j_0=0).                                         \tag{3}
\]

The number of terms in the permitted interval is `O(A/d)` because `d<2A` on every nonempty summand. For fixed `d` and positive `j_0` whose nearest multiple of `q` is positive, each eligible `q` divides `n-j_0` or `n+j_0`, with nonpositive arguments omitted. The arguments are positive integers of size `O(X)`. Their divisor counts are `O_epsilon(X^epsilon)`. The contribution in (3) summed over attained `1<=j_0<=Q` is then `O_epsilon(X^epsilon Q log(2X))`. At `j_0=0` the `q` divide `n`, costing `O_epsilon(X^epsilon A/d)`. If zero is a nearest multiple, `j_0=n` and `Q/n=O(1)` throughout the ambient interval, so all such `q` cost `O(Q+1)`. Every occupied box satisfies `A<=20R/sqrt(X)`, by the Jackson support, so `Q>=sqrt(X)/40` for `d<2A`. The last endpoint cost is absorbed.

Restore the factor `O(1/R)`, the actual `A_r` bound and the sum over `d<2A`. The geometric bounds just established have total at most

\[
 O_\epsilon\left(\frac{X^\epsilon}{R}\sum_{d<2A}
                     ((R/d)\log(2X)+A/d)\right)
       =O_\epsilon(X^\epsilon)
\]

after shrinking intermediate exponents, since `A<<R`. No cancellation between different `A_r` is used to take this bound, so it is valid for every `F_n`. Summing over the two signs and logarithmically many shell and magnitude boxes proves (2). This is the numerator argument of round-five NUMERATOR-ESTIMATE used with the exact difference weight in (1), rather than with the original reciprocal numerator weight.

For `G_8` one must also account for the moving mask. Its exact difference is

\[
 \Delta G_8(n)=\sum_{r\in\mathcal G_*}(1-W_r^0(n))\Delta g_r(n)
              -\sum_{r\in\mathcal G_*}\Delta W_r^0(n)g_r(n-1).       \tag{4}
\]

Here `G_*` has support `G_*` in conductor coordinates, denoted `mathcal G_*` in (4), and the mask `W_r^0` selects `5kr-D_0<=n<5kr+D_0`, with `D_0=floor(X^(2/3))`. A jump occurs only at `n=5kr-D_0` or `n=5kr+D_0`. Thus each jumping `r` divides `n+D_0` or `n-D_0`, which are positive and `O(X)` throughout the ambient interval on late blocks. There are `O_epsilon(X^epsilon)` such conductors at any single time. From `|b(r,a)|<<1/|a|`, each `g_r(n-1)` has size `O_epsilon(X^epsilon)` uniformly in time. The first sum in (4) uses (2). This proves `Delta G_8(n)=O_epsilon(X^epsilon)` on the full ambient interval. The same argument with the mask instead of its complement gives the bound for `Delta V_0`, and (2) gives it for `Delta G_*` and `Delta G_7`.

For the actual arithmetic `C_z`, use its admitted identity on `0<=n<=D` as the raw sum of `s(d)K_d(n)` with `P^+(d)>z`, part of the cube-root transfer. It retains the complete repeated-prime profile. Then

\[
 |\Delta C_z(n)|\le\sum_{d\mid n}|s(d)|\le3^{\omega(n)}
                                                   \ll_\epsilon X^\epsilon.
\]

The same bound holds for the raw `B_z`, or follows from `B_z=T-C_z` and `|t(n)|<=1`. All increment bounds hold also on the full support of `w`, including at endpoints. In particular no unknown norm bound for `G_8+C_z` was inserted into these pointwise estimates.

## 2. Simultaneous additive covariance estimate

Fix an integer `H>=1`. Starting at the first positive taper weight, partition the consecutive ambient integers through the last positive taper weight into consecutive intervals `I` of length `H`, with only the final interval shortened when necessary. Both outer endpoints are included. Let `W_I=sum_(n in I)w(n)`. Empty-weight intervals are immaterial. Denote by

\[
             m_I(F)=\frac{\sum_{n\in I}w(n)F(n)}{W_I}
\]

the weighted mean and by `P_H F` the function with this constant value on `I`. The same projection is applied to every sector, using the exact original weights. It is an orthogonal projection for the inner product with weight `w`. Therefore for any two weighted functions `F,G` on this support, exactly

\[
 \langle F,G\rangle_w-\sum_I W_I m_I(F)\overline{m_I(G)}
       =\langle (1-P_H)F,(1-P_H)G\rangle_w.                           \tag{5}
\]

The two terms with one mean and one within-block fluctuation vanish exactly. Apply the pointwise difference bounds in §1 to `F,G` from the set `G_*,V_0,G_8,C_z,B_z,T`, or fixed linear combinations of these. Since two integers in one `I` differ by at most `H-1`, each absolute fluctuation from the mean is `O_epsilon(H X^epsilon)`. Also `sum_n w(n)=O(X)`. Thus

\[
 \boxed{\quad
 \left|\langle F,G\rangle_w-\sum_I W_I m_I(F)\overline{m_I(G)}\right|
                       \ll_\epsilon X^{1+\epsilon}H^2.\quad}        \tag{6}
\]

This bounds the actual loss in each signed covariance, including the mixed core and full prime correction, without pairing a norm error against either large sector mean. For any fixed `0<delta<1/2`, choosing `H=floor(X^(1/2-delta))` gives the strict power `X^(2-2delta+epsilon)` for all of those errors and uses `O(X^(1/2+delta))` weighted levels. At `H` of order `sqrt(X)` it gives the target additive precision on the covariance matrix. Fixed logarithmic enlargements of that width also meet the all-epsilon bound. None of these operations changes the original taper or requires discarding crossing signs or endpoints.

For clarity, in the same scalar convention as round eight put `E_*=widehat P-||G_*||_w^2`. Its known bound is `O_epsilon(X^(2+epsilon))`. The exact complete identity after projection is

\[
 Q_8=E_*+\sum_I W_I
          |m_I(G_*)-m_I(V_0)+m_I(C_z)|^2
           +\|(1-P_H)(G_8+C_z)\|_w^2.                                \tag{7}
\]

The last term is nonnegative and is bounded by (6) with `F=G=G_8+C_z`. The square retains both mixed orders with the moving mask, the mixed order with the prime profile, and their diagonal terms. No new fixed determinant-strip identity for the moving mask is used. In particular the power saving in (6) is a statement about the original exact mixed covariances, while (7) still includes the inherited scalar error `E_*`.

These levels use finite time sums exactly. For example if `W_I^(>=v)=sum_(n in I,n>=v)w(n)`, the prime level is

\[
 W_I m_I(C_z)
   =-2\sum_{p>z,\,p\ {\rm split}}\sum_{j\ge1}t(j)W_I^{(\ge pj)}
    -4\sum_{z<p\le q,\,p,q\ {\rm split}}\sum_{j\ge1}t(j)W_I^{(\ge pqj)}.
\]

Windows with zero weight vanish. Every incoming endpoint is inclusive, and `p=q` stays in the second sum. The `G_*` and `V_0` level weights of a frequency are exactly `sum_(n in I)w(n)e(an/(5r))` and `sum_(n in I)w(n)W_r^0(n)e(an/(5r))` with their original coefficients. Thus their level covariance carries the original moving and fixed masks, with the same time cut at both ends.

## Scope

**O.** The coupled levels inside the square in (7) have not been bounded at the required scale. Equations (5)–(7) prove a quantitatively small additive joint covariance error for replacing the full sector functions by common block levels, including strict power savings at the widths stated, and leave the complete criterion unchanged. The full Q8 target remains open. Read round-eight REPORT §§1–5 and PERIODIC-SHARP-CAP, round-six CUBE-ROOT-TRANSFER, and round-five NUMERATOR-ESTIMATE at the pinned public head. The adjacent #2093 FULL-LEVELS uses weighted block levels for a different Möbius observable; the present proof controls the signed covariance of the actual moving `G_8` and the original `C_z` with a direct original-coefficient difference estimate. The adjacent Huang round-two signed intervals motivated checking exact endpoint weights. No new external analytic input, scientific numerical or symbolic execution, formal verifier, or repository modification was used. This is a paper derivation pending same-session review.
