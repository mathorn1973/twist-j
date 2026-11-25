# Large arithmetic gcds in the entire signed covariance

**NON-CANONICAL. No authority. Candidate-D paper deduction.** Round nine, C-RH-ARITHMETIC-KERNEL-N, issue #2087, draft #2089. Action layer NOT_APPLICABLE. The complete Q8 bound remains **O**. This is an arithmetic-index grouping, distinct from the primitive conductor gcd in the fixed pair sum. The source basis is the PUBLIC draft head `6a91ef48f6454743797614503aa5863dde54befb` and the lane question was frozen in `PREREG.md`.

## 1. Exact signed regrouping with the prime profile present

Use the original dyadic `X`, `D=4X`, `z=D^(1/3)`, rational taper `w`, and actual coefficient `t=chi_5*s` of the round-eight report. Set `T(n)=sum_(m<=n)t(m)` and extend by the floor to nonnegative real arguments, with zero below one. Use the actual raw core coefficients and their joint complement

\[
 b_z(m)=\sum_{\substack{d\mid m\\P^+(d)\le z}}s(d)\chi_5(m/d),
 \qquad c_z(m)=t(m)-b_z(m).
\]

Their prefixes are `B_z` and `C_z`, respectively, at all times on the taper. In particular `C_z` here is the original repeated-prime-inclusive profile. This exact relation follows from the cube-root transfer and is written in round eight, COUPLED-CUTS §1. It is an arithmetic realization of both sectors and leaves both sectors evaluated at the same time.

For integer `G>=1` define the actual high-gcd covariance, at coefficient indices rather than conductor coordinates, by

\[
 H_G(X)=\sum_n w(n)\sum_{m,k\le n} t(m)t(k)\mathbf1_{(m,k)>G},
 \qquad
 L_G(X)=\|T\|_w^2-H_G(X).                                            \tag{1}
\]

All sums over arithmetic indices here are over positive integers. Define

\[
 \lambda_G(r)=\sum_{\substack{d\mid r\\d>G}}\mu(r/d),\qquad
 T_r(n)=\sum_{a\le n/r}t(ra).
\]

The elementary divisor identity `sum_(r|h)lambda_G(r)=1_(h>G)` follows by interchanging the two divisor sums and using `sum_(u|v)mu(u)=1_(v=1)`. Therefore the exact finite covariance identity is

\[
                      H_G(X)=\sum_{G<r\le 17X/8}\lambda_G(r)\,\|T_r\|_w^2 . \tag{2}
\]

The upper bound in the index is inclusive at an integer endpoint. For each `r`, write `B_(z,r)(n)=sum_(a<=n/r)b_z(ra)` and `C_(z,r)` accordingly. The same right side of (2) contains exactly the sum

\[
 \|B_{z,r}\|_w^2+2\operatorname{Re}\langle B_{z,r},C_{z,r}\rangle_w
                      +\|C_{z,r}\|_w^2
\]

inside each signed coefficient `lambda_G(r)`. This is the regrouping of all high-gcd terms of the core, both mixed orders, and the full prime profile together. Neither the sign of its contribution at fixed gcd nor the separate smallness of the sector terms is assumed.

## 2. The local filter at a multiplier r

The exact prime-power values of `t` are `-1` at every positive split prime power, `(-1)^j` at inert powers, and zero at positive powers of five. For `5|r` the function `T_r` is identically zero. For `5` not dividing `r`, `|t(r)|=1`. Let `v_r` be the multiplicative coefficient supported on powers of split primes dividing `r`, with local coefficients `v_r(p^j)=2^j` there and with every other positive prime-power coefficient zero. Then

\[
       t(ra)=t(r)(t*v_r)(a),
       \qquad T_r(n)=t(r)\sum_{\ell\le n/r}v_r(\ell)T(n/(r\ell)).        \tag{3}
\]

Indeed an inert prime dividing `r` still has ratio `(-1)^j` after increasing its valuation by `j`. At a split prime dividing `r` the ratio is one for every `j>=0`; its local series is `(1-x)^(-1)` in place of `(1-2x)/(1-x)` for `t`, giving the factor `(1-2x)^(-1)`. Primes outside `r` have the original behavior, including the zero positive powers at five. This proves (3) by multiplication of the local identities.

For fixed `sigma>=1/2` and every `eta>0` its absolute norm satisfies

\[
        \sum_{\ell\ge1}v_r(\ell)\ell^{-\sigma}
        =\prod_{\substack{p\mid r\\p\ {\rm split}}}(1-2p^{-\sigma})^{-1}
        \ll_{\sigma,\eta} r^\eta.                                   \tag{4}
\]

At split primes `p>=11` one has `2p^(-sigma)<1`. The finitely many primes below a fixed threshold cost a constant, and above a large enough threshold each factor is at most `p^eta`. Their product is at most `r^eta`. This proves the uniform bound with no distributional input about the selected primes.

## 3. Power contraction into smaller actual blocks

For dyadic integers `Y>=1` and real `U>=0` let

\[
 A^{\circ}_{\sigma}(Y)=Y^{-1-2\sigma}\sum_{Y\le n<2Y}|T(n)|^2,
 \qquad M_{\sigma}(U)=\max_{\substack{Y\le U\\Y\ {\rm dyadic},\,Y\ge1}}
                       A^{\circ}_{\sigma}(Y),
\]

using maximum zero when the family is empty. These quantities are defined by the actual prefix, regardless of whether any boundedness claim holds. For integer `d>=1`, the floor equality

\[
 \left\lfloor\frac{x}{d}\right\rfloor=\left\lfloor\frac n d\right\rfloor
      \quad(n\le x<n+1)
\]

allows the supported interval sum on the taper to be written as an integral. Use `0<=w<=1`, the support of `w`, and substitute `x=d u`. The rescaled interval is contained in `[3X/(4d),9X/(4d))` on late blocks. Cover it by at most three consecutive dyadic intervals, treating arguments below one as zero. All the block scales are at most `3X/d`, including if the right endpoint is an integer. Since the sum of the unweighted squares through any such block is at most `Y^(1+2sigma) M_sigma(3X/d)`, this gives

\[
 \|T({\cdot}/d)\|_w
  \ll_\sigma X^{\sigma+1/2}d^{-\sigma}M_\sigma(3X/d)^{1/2}.           \tag{5}
\]

Using the actual filter (3), Minkowski and (4) in (5) gives

\[
 \|T_r\|_w^2\ll_{\sigma,\eta}
   X^{1+2\sigma} r^{-2\sigma+\eta} M_\sigma(3X/r),                     \tag{6}
\]

where the exponent in (4) has been halved before squaring. The coefficient bound `|lambda_G(r)|<=tau(r)` is uniform in `G`. Applying it only after the exact joint regrouping (2), and shrinking the intermediate exponent in (6), gives for every fixed `sigma>1/2` and `0<eta<2sigma-1`

\[
 \boxed{\quad
 |H_G(X)|\ll_{\sigma,\eta}X^{1+2\sigma}
 G^{1-2\sigma+\eta}M_\sigma(3X/G).\quad}                            \tag{7}
\]

Indeed the remaining sum is bounded by `sum_(r>G) r^(-2sigma+eta)` and integral comparison. This statement is unconditional in terms of the earlier actual block energies. It does not invoke an estimate for `M_sigma`. With `G=floor(X^delta)` for a fixed `0<delta<1`, the coefficient of `M_sigma` after normalization has the fixed power saving `X^(-delta(2sigma-1-eta))`, and every block in its maximum is earlier than `X` at sufficiently large `X`. The estimate comes from joint local filtering of both sectors before the norm is taken.

A precise consequence at this `G` is the all-late-dyadic-block equivalence, for each fixed `sigma>1/2`,

\[
 (Q_8)_+=O_\sigma(X^{1+2\sigma})
 \quad\Longleftrightarrow\quad (L_G(X))_+=O_\sigma(X^{1+2\sigma}).        \tag{8}
\]

For the reverse implication, (1) and (7) bound `X^(-1-2sigma)||T||_w^2` by a constant plus a coefficient tending to zero times `M_sigma(3X/G)`. The central block has `w=1`, so the same bound controls `A_sigma^circ(X)`. After making the coefficient at most `1/2`, induction on the dyadic integers bounds the maximum uniformly, starting from the finite initial maximum and twice the given constant. Substitution in (1) and (7) now bounds the entire taper norm. For the other implication the inherited round-eight norm comparison bounds `T` on every taper and then its earlier central blocks. Apply (7) and (1) to bound `L_G`. The transfer in both directions is exactly through `||T-(G_8+C_z)||_w^2<<_epsilon X^(2+epsilon)` and `Q_8=||G_8+C_z||_w^2+O_epsilon(X^(2+epsilon))`, with the error exponent strictly smaller than `2sigma-1`. These comparisons keep the fixed primitive masks, endpoints, both moving-mask cross terms and the repeated prime correction inside their full amplitudes. They do not identify the arithmetic labels `(m,k)` with any fixed primitive determinant pairs. There is no target-scale additive comparison of the full squared norms without control of the same-block amplitudes.

The contraction coefficient in (7) is a proved power on the entire high-gcd portion, at every fixed exponent above the critical one. The sum used in its proof has no decreasing exponent at `sigma=1/2`. The initial band `G<r<=2G` even has `lambda_G(r)=1` exactly, since every proper divisor is at most `r/2`. Other bands can offset it. No conclusion about strict contraction at that endpoint follows from this estimate.

## Scope

**O.** A complete signed estimate of the complementary actual covariance `L_G(X)` in (8) has not been proved. The original Q8 target therefore remains open. Read the pinned round-eight REPORT and COUPLED-CUTS, round six CUBE-ROOT-TRANSFER, round four DILATION-CORRELATION, and the adjacent Huang round-two signed overlap and the adjacent #2093 full coupled-energy note for scope. The local identity (3), joint divisor regrouping, and quantitative contraction are derived here without prime counts or other new external theorems. No scientific numerical or symbolic execution and no formal verifier run. No repository modification or independent external review.
