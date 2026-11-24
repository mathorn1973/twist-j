# Short sums and a narrower Fourier cutoff on the actual taper

C-RH-ARITHMETIC-KERNEL-N, issue #2087. NON-CANONICAL, no authority. Candidate-D paper continuation on the imported unconditional short-sum estimate. Inputs are at draft #2089 head `f55cbcd1bf0eff6de99449c37ac8c03916b8acfe`. No scientific computation was performed. The desired power estimate for the remaining spectrum is open.

## 1. Exact series and the available arithmetic input

Let `X` be a sufficiently large dyadic integer, `D=4X`, and `F_D(n)=sum_(d<=D) s(d)K_d(n)` on all integer times, using the periodic extension of the residue kernel. On `0<=n<=D` it equals the actual `T(n)`. Its first difference on `1<=n<=D` is `t(n)=s*chi_5(n)`, with `|t(n)|<=1`. On all integer times `|F_D(n)|<=D`. These are the existing exact properties in SIGNED-SPECTRUM. Write `I_X=[X/2,3X]` intersected with the integers. This contains the actual finite taper support.

The inherited maximal short-sum estimate, equation (2) of SHORT-SUM-TRANSFER, is

\[
 \sum_{Y\le n<2Y}{\cal W}_t(n,h)^2
 \ll_{\eta,A}Yh^2(\log Y)^{-A}
 \quad\left(Y^{1/3+\eta}\le h\le Y^{1-\eta}\right),             \tag{1}
\]

for every fixed `eta>0` in its stated range and fixed `A>0`. It permits all progressions and additive phases in an interval. The transfer to the actual `t` used the three established coefficient-unit bounds, including the critical `sum_(d<=y)|v(d)|/sqrt(d)<<log(2y)` for quotient intervals shorter than one. There is no new use of the short-interval theorem on scaled intervals outside its proved range. Only phase zero and consecutive progressions of (1) are needed here.

## 2. Compact Fourier support using the positive smoother

For integer `H>=4`, let `J_H` be the positive smoother from SIGNED-SPECTRUM with parameter `1/H`. Its time weights and multiplier satisfy

\[
 p_H(j)=\frac{3}{2H}\operatorname{sinc}(\pi j/H)^4\ge0,
 \quad\sum_{j\in\mathbb Z}p_H(j)=1,
 \quad p_H(j)\ll H^{-1}(1+|j|/H)^{-4}.
\]

The multiplier is the normalized convolution of two circle tents, denoted `m_(1/H)`. It lies in `[0,1]` and vanishes when `||theta||>2/H`. The time weights are summable, so convolution with `F_D` equals multiplication of its exact finite Fourier expansion by this multiplier.

**Theorem.** For fixed `0<eta<1/12` and each fixed `A>0`, uniformly for integers `X^(1/3+eta)<=H<=X^(1-2eta)`,

\[
 \sum_{n\in I_X}|F_D(n)-J_HF_D(n)|^2
       \ll_{\eta,A} XH^2(\log X)^{-A}.                           \tag{2}
\]

To prove it, take `V=floor(X^(1-eta))`. For each integer `j` with `|j|<=V`, put `W=max(H,|j|)`. For every `n` in `I_X`, all differences between `F_D(n)` and `F_D(n-j)` are in the range `1<=m<=D` for sufficiently large `X`. They form a consecutive interval of coefficients of `t` contained in `(n-W,n+W]`. Therefore

\[
 |F_D(n)-F_D(n-j)|\le {\cal W}_t(n-W,2W).
\]

The starts `n-W` lie in `[3X/8,3X]` once `X` is sufficiently large. They are covered by the three dyadic start blocks with left endpoints `X/4,X/2,X`, and the block with left endpoint `2X`. The length `2W` lies between `Y^(1/3+eta/2)` and `Y^(1-eta/2)` for all four endpoints `Y`, by the fixed margins and their bounded ratios to `X`. Apply (1) and take square roots to obtain

\[
 \|F_D(\,\cdot\,)-F_D(\,\cdot\,-j)\|_{\ell^2(I_X)}
       \ll_{\eta,A}\sqrt X\max(H,|j|)(\log X)^{-A/2}.           \tag{3}
\]

This uses separate estimates for each length, without needing a common exceptional set. Sum (3) against `p_H(j)` by the norm triangle inequality. The total factor `sum_j p_H(j) max(H,|j|)` is `O(H)`: sum up to `H`, then use the fourth-power decay on larger dyadic annuli. To handle `|j|>V`, note the pointwise bound `|F_D(n)-F_D(n-j)|<<|j|` for every `j` and `n` in `I_X`. For `|j|<=X/4` both times are between zero and `D` and the unit first-difference bound applies. For larger `|j|`, the global `2D` bound suffices. Thus the tail costs

\[
 O\!\left(\sqrt X\sum_{|j|>V}|j|p_H(j)\right)
     =O(\sqrt X H^3/V^2).
\]

Relative to `sqrt(X)H` this last bound has a factor `O(X^(-2eta))`. Combining it with (3) and squaring proves (2). Integer rounding of `V` changes only constants for large `X`.

The improvement over the preceding rational triangular average is the exact compact frequency cutoff for this positive smoother. For every fixed `B>=0`, take `H=ceil(sqrt(X)(log X)^B)`. In (2), choose the arithmetic logarithmic exponent larger than `2B+A`, giving the error `O_(A,B)(X^2/(log X)^A)` for each fixed `A>0`, uniformly on the full taper support. The positively smoothed series only contains frequencies `|a|<=10r/H`. No signed estimate for its remaining part is used.

## 3. Local annuli without dividing by a frequency multiplier

One can also control a smooth annulus of the exact frozen spectrum. Fix an even smooth real function `phi` on the real line supported in `1<=|u|<=2`. On the frequency circle put `Pi_H(theta)=phi(H theta)`, using centered representatives. Let it act by convolution in time with its Fourier coefficients `q_H(j)`. Integration by parts in the fixed compact support gives, for every fixed integer `M>=2`,

\[
 |q_H(j)|\ll_{M,\phi}H^{-1}(1+|j|/H)^{-M},\qquad
 \sum_j|q_H(j)|\ll_\phi1.                                      \tag{4}
\]

The sign of these coefficients is not needed. On the support of `Pi_H`, the positive smoother `J_(4H)` has zero multiplier. Hence the exact finite Fourier identity is `Pi_H F_D=Pi_H(F_D-J_(4H)F_D)`. There is no reciprocal multiplier or assumption of invertibility. If `X^(1/3+eta)<=H<=X^(1-3eta)` and `X` is sufficiently large, `4H` meets the range of (2). For `|j|<=X/16`, each shifted argument from the taper support is inside `I_X`. Apply the triangle inequality and (2) to these shifts in (4). The tail `|j|>X/16` uses `|F_D-J_(4H)F_D|<=2D` and contributes to the norm at most `O_(M,phi)(X^(3/2)(H/X)^(M-1))`. Taking `M>=3` makes this negligible relative to `sqrt(X)H` times every fixed inverse logarithm. This proves

\[
 \sum_{n\in\operatorname{supp} w_X}|\Pi_H F_D(n)|^2
        \ll_{\eta,A,\phi} XH^2(\log X)^{-A}.                    \tag{5}
\]

This is a local estimate for a specified smooth frequency band of the actual signed spectrum. Taking differences of two cutoffs gives the matching multiscale form `||J_(H_1)F_D-J_(H_2)F_D||_2<<sqrt(X)H_2(log X)^(-A/2)` for `H_1<=H_2` in the range of (2). For a list of dyadic increasing `H`, the sum of the bounds for the successive differences is dominated by its final width. There is no harmonic or power gain from repeating the smoothing alone.

## 4. Consequence for the existing determinant criterion

Define `G_(X,H)` using the original round-4 conductor shells and numerator caps, together with the round-5 rough-conductor condition `P^+(r)>(log X)^2`. Use `m_(1/H)` in place of `m_(X^-1/2)` for fixed `B>=0` and `H=ceil(sqrt(X)(log X)^B)`. Do not impose the separate round-5 trim `h=X|a|/r<Y_star=sqrt(X)exp(-sqrt(log X))` in this definition. Since `H>=sqrt(X)`, no mode beyond the original cap `|a|<=10r/sqrt(X)` can survive the new multiplier. The earlier error estimates for removing small conductors and excess numerators continue to apply to `J_H F_D`: they use only `|m_(1/H)|<=1` and the same complete coefficient bounds and spacing. The smooth-conductor deletion uses the same absolute weight bound and is uniform in the multiplier. Together with (2), the total squared error between `T` and `G_(X,H)` on the finite taper support is `O_epsilon(X^(2+epsilon))` for each fixed epsilon. The part specifically from the new positive smoothing is `O_(A,B)(X^2/(log X)^A)` for every fixed `A`.

The surviving frequencies now satisfy the conductor-relative cap `|a|<=10r/H`, in addition to the inherited numerator cap. There are at most `O(X^2/H)` possible modes, or `O_B(X^(3/2)/(log X)^B)` at these widths. This narrows the possible geometric support compared with the original round-4 smoother. The new height cap `10X/H` is wider than `Y_star` for every fixed `B` at sufficiently large `X`, since `exp(sqrt(log X))/(log X)^B` tends to infinity. The gain is the all-fixed-logarithmic bound on the actual compact-smoothing error and on the smooth bands, with no further geometric reduction of the already trimmed round-5 star spectrum claimed here. The finite taper identity and large-gcd pruning apply with these multiplier weights and the inherited determinant rules. Their absolute bounds used a harmonic sum over numerators and coefficient estimates valid under removal, and the weighted same-conductor estimate also holds for this spectrum. A bound `O_epsilon(X^(2+epsilon))` on the positive part of the new remaining signed sum, at all sufficiently late dyadic `X` for each fixed epsilon, is equivalent to the preceding criterion on the original sum. Both series approximate the same `T` on the same taper at the target norm precision, so norm comparison does not require a bound on the cross terms of the difference between their two pair sums.

The same block-by-block comparison also holds for positive-part energy on each complete power window, with arbitrary subpower error in the norm and with exponent slack as in the preceding window reductions. The new cutoff is chosen from the dyadic scale, independently of the window later tested. It does not reorder high and low numerators inside a conductor or use a change of block in the short-sum estimate.

## 5. Limit of the rate and an explicit obstruction to using it alone

If `H=floor(X^(1/2+delta))` with fixed `0<delta<1/2`, take `eta` small enough that (2) applies. That bound and (5) are then of scale `X^(2+2delta)/(log X)^A` for each fixed `A`. This estimate alone cannot be used as an all-epsilon error for `epsilon<2delta`. In particular it gives no square-root bound near the smallest frequencies of size `1/X`.

There is a paper model showing that the inherited short-sum controls alone, even combined with the positions and individual size ceilings of the low-height modes, cannot force such a bound. For each dyadic `X` take the actually allowed numerator-one frequencies of the split primes `3X<r<=4X`, together with their negatives. By the prime number theorem modulo five their number is `asymp X/log X`. Set

\[
 Q_X(n)=c_X\sum_{\substack{3X<r\le4X\\r\text{ split prime}}}
                     \sin\!\left(\frac{2\pi n}{5r}\right),
 \qquad
 c_X=\exp\!\left(-d\frac{(\log X)^{3/5}}{(\log\log X)^{1/5}}\right),
\]

with any fixed `d>0`. These coefficients are artificial and are not those of `T` or `G_X`. The frequencies and their numerator and conductor bounds are genuine. If desired, `d` can exceed the constant in the previously established unconditional full envelope, so the model also lies below that envelope. On `X<=n<2X`, all phases are between `2pi/20` and `4pi/15`, and hence `Q_X(n)>>c_X X/log X`. Its dyadic square sum is at least `c' c_X^2 X^3/(log X)^2`, which exceeds `X^(2+epsilon)` for every fixed `epsilon<1` at sufficiently large `X`.

On `[X/2,3X]` all terms are increasing because their phases are below `pi/2`. Take the integer model `q_X(n)=floor(Q_X(n))` separately for each dyadic scale. Consecutive differences have magnitude at most one for sufficiently large `X`, by the uniform derivative bound `O(c_X/log X)` and rounding. On the entire start and endpoint range of (1) with `Y=X`, the differences are nonnegative. The sum of their magnitudes on any progression in a length `h` interval is at most the full change of `q_X`, which is `O(c_X h/log X+1)`. The same holds for the absolute value after multiplication by any additive phase. This satisfies every fixed logarithmic short-sum budget in (1), even pointwise, for the permitted polynomial lengths. Rounding changes the original amplitudes by less than one. Thus this family of separate local models passes the short-sum tests with integer increments and a bounded approximation by an admissible low-height frequency array on each block. A single global arithmetic sequence with these properties is outside this construction. Its role is to isolate the quantitative gap in trying to obtain the missing power estimate from the inherited local bounds and spectral geometry alone.

## Inputs

- [Pinned SHORT-SUM-TRANSFER](https://github.com/mathorn1973/twist-j/blob/f55cbcd1bf0eff6de99449c37ac8c03916b8acfe/notes/C-RH-ARITHMETIC-KERNEL-N/round5/SHORT-SUM-TRANSFER.md), particularly equations (1), (2) and their unit-transfer proof.
- [Pinned SIGNED-SPECTRUM](https://github.com/mathorn1973/twist-j/blob/f55cbcd1bf0eff6de99449c37ac8c03916b8acfe/notes/C-RH-ARITHMETIC-KERNEL-N/round3/SIGNED-SPECTRUM.md), exact first differences, positive compact-spectrum smoother and Fourier coefficients.
- [Pinned FINITE-TAPER](https://github.com/mathorn1973/twist-j/blob/f55cbcd1bf0eff6de99449c37ac8c03916b8acfe/notes/C-RH-ARITHMETIC-KERNEL-N/round4/FINITE-TAPER.md), exact time support and determinant criterion.
- [MRSTT, Higher uniformity of arithmetic functions in short intervals II, Theorem 1.1(i)](https://doi.org/10.1007/s00222-026-01408-6), unconditional Möbius input used through the pinned transfer.
- [Yamada, Explicit formulae for primes in arithmetic progressions I, introduction](https://arxiv.org/html/1306.5322v4#S1), fixed-modulus PNT, used only to count the model's allowed split-prime frequencies.
