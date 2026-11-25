# Moving residue zeros in the original capped conductor packet

**NON-CANONICAL. No authority. Candidate-D paper proof.** Issue #2087, draft #2089, same owner and candidate C-RH-ARITHMETIC-KERNEL-N. Action layer NOT_APPLICABLE. The complete all-epsilon bound for Q7 remains **O**. Work follows the frozen lane preregistration. This proof removes explicit parts of the actual Q7 amplitude, including below-time conductors with any fixed number of distinct prime factors in specified smooth frequency packets.

## 1. Fixed coefficients and the moving family

Use the original round-seven `G_7`, `C_z`, `Q_7` and rational taper `w`. Write `||F||_w^2 = sum_n w(n)|F(n)|^2`, `D=4X`, `z=D^(1/3)`, and `e(x)=exp(2 pi i x)`. The support of `w` is in `[7X/8,17X/8]`, and `w=1` at integers in `[X,2X)`. The actual residue kernel is `K_d(n)=H(floor(n/d))`, where the period-five values of `H` are `(0,1,0,-1,0)`. Extend `K_d` periodically to all integer times. For squarefree split `r`, round three gives

\[
 K_r=\sum_{d\mid r}\frac d r\Phi_d,
 \qquad
 \Phi_r=K_r+\sum_{\substack{d\mid r\\d<r}}\mu(r/d)\frac d r K_d.       \tag{1}
\]

The second equality is ordinary Möbius inversion. The Fourier coefficient of `Phi_r` at a primitive signed frequency `theta=a/(5r)` is

\[
 b(r,a)=\frac{\tau\chi_5(a)}{5r(1-e(-a/(5r)))}.
\]

Both its signed partners are used. All retained coefficients have the original signed factor

\[
 A_r=s(r)\sum_{\substack{m\le D/r\\(m,r)=1}}\frac{s(m)}m,
 \qquad |A_r|\ll_\epsilon X^\epsilon.                                \tag{2}
\]

For the upper bound use `|s(r)|<=tau(r)` at supported `r` and the inherited harmonic bound on `|s(m)|`. Denote the original Jackson multiplier by `m_X(theta)` and its probability weights by `p_X(j)`. The original coefficient is `A_r b(r,a)m_X(theta)`. The weights satisfy

\[
 \sum_{|j|>J}p_X(j)\ll (\sqrt X/J)^3\quad(J\ge\sqrt X),
 \qquad \|p_X\|_1=1.                                                 \tag{3}
\]

Fix one original shell `R<r<=min(2R,D)` and an arbitrary fixed subset `F` of its actual surviving squarefree split conductors. Suppose every proper divisor of every `r` in `F` is at most `E`, where `1<=E<=R`. Set `L=ceil(X^(2/3))`. At each time `n` on the taper define `F_n` to be the conductors in `F` for which there is an integer `j>=0` with

\[
 H(j)=0,\qquad jr\le n-L,\qquad n+L<(j+1)r.                         \tag{4}
\]

In particular `K_r(n-u)=0` for every integer `|u|<=L`. The endpoint conventions in (4) come from the floor. For `j>0` the admissible `r` for that `j` belong to the interval `((n+L)/(j+1),(n-L)/j]`. For `j=0` the condition is `r>n+L`, since `n-L>0` at sufficiently late scales. Every occupied `j` is at most `(n-L)/R<3X/R`. Thus `F_n` is the intersection of `F` with the union of at most `1+3X/R` disjoint intervals of integers in the shell. The mask is frozen at time `n` before any convolution in the proof below.

## 2. Uniform control of the moving proper-divisor sum

The following argument works for any circle multiplier `M(theta)` bounded by one, provided it is fixed across the shell and independent of `n`. It is applied first to `m_X` and then to the additional smooth frequency cutoff times `m_X`. For an integer interval `I` in the shell put

\[
 U_I = M\left(\sum_{r\in F\cap I} A_r\sum_{\substack{d\mid r\\d<r}}
                                  \mu(r/d)\frac d r K_d\right),       \tag{5}
\]

where `M` in front of a finite Fourier series means multiplication of its Fourier coefficients. Re-expand in the `Phi_e` basis using (1). At any level of a binary partition of the shell into consecutive intervals `I`, let `c_{I,e}` be the coefficient of `Phi_e` before applying `M`. It vanishes for `e>E`. The intervals at that level are disjoint. Consequently

\[
 \sum_I |c_{I,e}|
 \le \sum_{\substack{d\le E\\e\mid d}}\frac e d
             \sum_{\substack{r\le 2R\\d\mid r,\ d<r}}
                           |A_r|\frac d r
 \ll_\epsilon X^\epsilon.                                          \tag{6}
\]

Here the actual support of `A_r` can be relaxed in the inner sum. After bounding `|A_r|` by (2) with a smaller exponent, both sums are harmonic. In particular `sum_I |c_(I,e)|^2` is bounded by the square of the right side in (6). The disjoint primitive frequency orbits in `Phi_e` all have spacing at least a constant times `E^(-2)`, taken together, and `sum_a |b(e,a)|^2 << 1`. The inherited translated additive large sieve on intervals of length `O(X)` gives, on each binary level,

\[
 \sum_I\|U_I\|_w^2\ll_\epsilon X^\epsilon (X+E^2)E.                 \tag{7}
\]

This also follows from the elementary logarithmic-loss version of the large sieve in KERNEL §7. The logarithm is absorbed by shrinking the input exponent.

Pad the shell's consecutive integer list to a power of two with empty entries. At every `n` the union defining `F_n` is a disjoint union of at most `O((1+X/R)log(2X))` aligned binary intervals across all levels. To see the binary count, the maximal complete binary intervals inside any one contiguous integer interval contain at most two per level. Replacing `F cap I` by `F cap` each selected aligned interval therefore gives the moving sum in (5) exactly at `n`. Pointwise Cauchy–Schwarz, followed by summation over all levels of (7), proves

\[
 \left\|n\mapsto
 M\left[\sum_{r\in F_n} A_r\sum_{\substack{d\mid r\\d<r}}
                   \mu(r/d)\frac d r K_d\right](n)\right\|_w^2
 \ll_\epsilon X^\epsilon(1+X/R)(X+E^2)E .                          \tag{8}
\]

The operator in this formula is applied to a separate polynomial with the mask `F_n` held fixed for each evaluation at `n`. No Fourier separation estimate is being applied directly to a time-varying trigonometric series.

There is a sharper bound on shells with `R<=X/32`. Every occupied `j` in (4) then satisfies `j>=X/(4R)` for sufficiently late `X`, since `n-L>=3X/4`, `r<=2R`, and `j=floor((n-L)/r)` for the allowed plateau. The real length of that interval of `r` is at most

\[
 \frac n j-\frac n{j+1}\le 34R^2/X.
\]

Thus only aligned integer intervals of length at most `Delta=1+40R^2/X` need be used in the binary argument. The first formula in (1) also gives the proper-divisor part of the second directly as `-sum_(e|r,e<r) (e/r) Phi_e`. Hence, before multiplying, its coefficient in (5) is exactly

\[
 c_{I,e}=-\sum_{\substack{r\in F\cap I\\e\mid r,\ e<r}} A_r\frac e r.
\]

Each applicable `I` contains at most `1+Delta/e` multiples of `e`. Cauchy–Schwarz inside each interval, then disjointness at a fixed binary level, show

\[
 \begin{aligned}
 \sum_{I:\,|I|\le\Delta}|c_{I,e}|^2
 &\ll_\epsilon X^\epsilon(1+\Delta/e)
                  \sum_{R<r\le2R,\ e\mid r}(e/r)^2\\
 &\ll_\epsilon X^\epsilon(e+\Delta)/R .
 \end{aligned}
\]

Indeed there are at most `1+R/e` such multiples in the shell, and `e<=E<=R`. The improved summed coefficient mass at each level is `O_eps(X^eps E(E+Delta)/R)`. Applying the same large sieve and binary argument therefore sharpens the right hand side of (8) to

\[
 \ll_\epsilon X^\epsilon(1+X/R)(X+E^2)\frac{E(E+\Delta)}{R}.
                                                                        \tag{8a}
\]

## 3. A powered removal with the original smooth Jackson multiplier

Fix a smooth even real function `eta`, between zero and one, equal to one on `[-1,1]` and zero outside `[-2,2]`. Suppose the additional multiplier `eta(B theta)`, with centered frequencies and `B=X^(13/20)`, has support inside every original numerical cap for the shell; the concrete cases below verify this. Define `V(n)` to be exactly the sum of the original modes of `G_7` at `r in F_n`, with each coefficient multiplied by `eta(B theta)`. Since the original caps contain the support, `V(n)` equals the evaluation at `n` of

\[
      M\left[\sum_{r\in F_n}A_r\Phi_r\right],
      \qquad M(\theta)=m_X(\theta)\,\eta(B\theta).                  \tag{9}
\]

The symmetry of both the original and added caps makes `V` real. With `q_B(j)` the integer Fourier coefficients of `eta(B theta)`, repeated integration by parts gives

\[
 |q_B(j)|\ll_M B^{-1}(1+|j|/B)^{-M},\qquad \|q_B\|_1\ll 1
\]

for any fixed differentiation order `M>=2`. The convolution weights for (9) are `p_X*q_B`. By splitting a shift `j=u+v` with `|j|>L` into the cases `|u|>L/2` or `|v|>L/2`, (3) gives

\[
 \sum_{|j|>L}|(p_X*q_B)(j)|
 \ll_M (\sqrt X/L)^3+(L/B)^{1-M}\ll X^{-1/2}.                     \tag{10}
\]

For the last estimate one can fix any `M>=32`, since `L/B>=X^(1/60)`. These weights act on the full periodic extensions of the frozen raw polynomials, and the bound controls shifts at every endpoint of the taper. By (4), the raw part `sum_(r in F_n) A_r K_r(n-j)` vanishes for all `|j|<=L`. At larger shifts its absolute value is at most `sum_(r in F_n)|A_r| <<_eps R X^eps`, since `|K_r|<=1` globally. Thus its contribution to the squared norm in (9) is `O_eps(R^2 X^eps)`. Combining with (8) yields the quantitative estimate

\[
 \boxed{\quad
 \|V\|_w^2\ll_\epsilon X^\epsilon
       \left[R^2+(1+X/R)(X+E^2)E\right].\quad}                      \tag{11}
\]

The raw zero uses the residue pattern and the complete signed numerator sum. There is no separate claim of small absolute coefficient mass.

On the shorter shells where (8a) applies, the same reasoning gives

\[
 \boxed{\quad
 \|V\|_w^2\ll_\epsilon X^\epsilon
       \left[R^2+(1+X/R)(X+E^2)\frac{E(E+\Delta)}{R}\right].\quad}     \tag{11a}
\]

## 4. Actual examples with four through seven distinct factors

For each late dyadic `X`, take the original shell with largest left endpoint `R<=X^(17/25)`. Then `R` is comparable to `X^(17/25)`. For a fixed `l` from four through seven, let `F` be the conductors made of `l` distinct split primes in

\[
       [(6R/5)^{1/l},(7R/5)^{1/l}].                                 \tag{12}
\]

Every product is in `(R,2R]`, above `D^(2/3)` eventually, and below the time range `[X,2X)`. The split primes in (12) are greater than `(log X)^2` and at most `z`. Their products satisfy both round-seven small-divisor cutoffs with small-prime part one and growing cutoff thresholds. They are therefore included among the actual surviving conductors. For `A_r` the cofactor denominators in (2) are odd. Every term with `m>1` has even numerator before taking a common odd denominator, whereas the `m=1` contribution has odd numerator. The cofactor sum is consequently nonzero. The numerator one is primitive and permitted by both caps, and `m_X(1/(5r))` tends uniformly to one. The cutoff `eta(B/(5r))` is also one eventually, so this is an actual nonzero coefficient with unit additional weight.

For any retained shell, the cap apart from the support of `m_X` is

\[
 |a|\le\lceil R^3/X^2\rceil,\qquad |a|\le 10r/\sqrt X,
 \qquad X|a|/r<\sqrt X\exp(-\sqrt{\log X}).                         \tag{13}
\]

When `|theta|<=2/B` we have `|a|<=10r/B`, and `r<=2R`. The cap `R^3/X^2` admits this eventually because `B/(X^2/R^2)` grows as a positive power of `X`: `13/20 > 2-2(17/25)`. The two `r`-relative caps admit it because `13/20>1/2`, with strict margin also against the subpower exponential. All the support conditions of (9) are therefore met. The largest proper divisor of (12) is at most a constant times `R^(1-1/l)`. With `E` a fixed sufficiently large multiple of this scale, (11a) proves

\[
 \begin{array}{c|c|c}
 l & E\text{ of order} & \|V\|_w^2\\ \hline
 4 & X^{51/100} & O_\epsilon(X^{42/25+\epsilon})\\
 5 & X^{68/125} & O_\epsilon(X^{227/125+\epsilon})\\
 6 & X^{17/30} & O_\epsilon(X^{143/75+\epsilon})\\
 7 & X^{102/175} & O_\epsilon(X^{69/35+\epsilon}) .
 \end{array}                                                       \tag{14}
\]

Here `E` exceeds both `sqrt(X)` and `Delta` by fixed powers, so the leakage term is of order `X E^4/R^2`. This has exponent `1+(17/25)(2-4/l)`. The raw term `R^2` is smaller in all four cases.

The fixed-modulus prime number theorem gives at least a constant times `R^(1/l)/log X` split primes in (12) on every sufficiently late dyadic block. Choosing distinct sets of `l` primes and using unique factorization gives `>>_l R/(log X)^l` conductors. For each such `r`, every complete period of length `5r` contains at least `3(r-2L)` integer times satisfying (4), because three of the five floor residues are zero and each has a plateau of length `r`. An incomplete period at each end of `[X,2X)` can lose at most `10r` times. Both `L/r` and `r/X` tend uniformly to zero. Consequently each conductor has at least `X/2` qualifying times in `[X,2X)` eventually. This gives `>>_l XR/(log X)^l` incidences of actual nonzero numerator-one modes, even with time restricted to the weight-one block. It counts deletable modes, not a lower bound on their signed sum.

For `l` balanced factors on these scales the dominant term of (11a) has exponent `1+rho(2-4/l)` when `E>=max(sqrt(X),Delta)`. At `l=8` it exceeds two for every fixed `rho>2/3` in this range. This is the threshold of this particular bound. It gives no estimate from below for an actual signed amplitude.

## 5. Removal of the whole sharp-capped packet at a higher shell

There is also an all-numerator version at the required error precision. Use (9) with `M=m_X`, without `eta`, and keep the same frozen masks. Formula (3) replaces (10) at the same cost since `L>=X^(2/3)`. Thus the uncapped, smoothed moving primitive packet still obeys (11). We now pay the difference between this packet and the actual sharp caps (13), uniformly for the varying masks.

Take `R>=c X^(3/4)` for a fixed `c>0`. On the shell the union of omitted ranges on the support of `m_X` only includes `|a|>=N`, with

\[
 N\gg_c \min\{R^3/X^2,\ (R/\sqrt X)\exp(-\sqrt{\log X})\}.
\]

One can take half the minimum rounded down for large scales, which avoids any integer endpoint conventions. On a fixed signed dyadic box `A<=|a|<2A`, the omitted `a` for each `r` form one interval inside the nonzero multiplier support, with the primitive condition kept. We show its amplitude for **any** conductor subset at each fixed time is `O_eps(X^eps R/A)`. The interval may depend on `r`. This is the argument of round-five NUMERATOR-ESTIMATE §1 applied before the conductor sum, with the following counting details.

Write `1_(a,r)=1` as `sum_(d|(a,r)) mu(d)`, set `r=dq`, `|a|=dj`, and keep `chi_5(a)` through its five additive characters. Apart from this character and the time phase, the coefficient `b(r,a)m_X(a/(5r))` on the signed box has supremum plus variation `O(1/A)`. For the denominator of `b`, use its size `O(1/|a|)` and derivative `O(1/a^2)` there. The rescaled Jackson multiplier is a bounded Lipschitz profile of uniformly bounded variation. Finite summation by parts reduces the inner contribution for each `d,q` to a bound

\[
 \ll A^{-1}\min\{A/d,\ Q/j_0\},\qquad
 Q=R/d,\quad j_0=\operatorname{dist}(n,q\mathbb Z),                 \tag{15}
\]

where `q in (Q,2Q]` and the second term is omitted for `j_0=0`. In detail, for each additive character the geometric progression has phase `(+-n+hq)/(5q)` with integer `h`, whose circular distance to an integer is at least `j_0/(5q)`. There are `O(A/d)` terms because `d<2A`. For fixed `d`, at `j_0=0` the possible `q` divide `n` and contribute `O_eps(X^eps A/d)` before `A^(-1)`. At each attained positive `j_0`, if the nearest multiple is positive there are at most `tau(n-j_0)+tau(n+j_0)` possibilities with positive arguments only, because `q` divides one of them. The arguments are `O(X)` since `n` is on the taper and `j_0<=q/2`. Summing `Q/j_0` over `1<=j_0<=Q` then costs `O_eps(X^eps Q log(2X))`. If the nearest multiple is zero, `j_0=n` and `Q/n=O(1)` on the taper, so the total of this case is `O(Q+1)`. The only needed boxes have `A<=20R/sqrt X`, hence `Q>=sqrt X/40` and this endpoint term is absorbed. Finally (2) and the harmonic sum over `d<2A` give the asserted `O_eps(X^eps R/A)` bound. Taking the absolute value of each conductor contribution happens after its character-bearing numerator sum. Therefore the argument is valid for an entirely arbitrary subset of the shell at each fixed `n`, including `F_n`.

Sum these dyadic numerator bounds for `A>=N/2`. This gives a pointwise discrepancy `O_eps(X^eps R/N)=O_eps(X^(1/2+eps))` between the capped and uncapped smoothed packets throughout the taper. At `R` comparable to `X^(3/4)`, choose `F` with four, five or six balanced split prime factors as in (12). Then `E` is of order `R^(1-1/l)`, and the sharper bound (11a) on the uncapped term has exponent at most `1+(3/4)(2-4/6)=2`. The complete original capped moving packet therefore has squared norm `O_eps(X^(2+eps))` including the discrepancy. It has the same incidence count as before. This version removes the whole original sharp-capped sum on its moving mask. The strict power bounds in (14) pertain to their smooth subpackets.

## 6. Exact removal of the proper-divisor frequencies

In (9), let `B` be any scale for which the extra multiplier fits the original caps, and choose any integer margin `L` in (4). The primitive expansion of the proper-divisor part is exactly `-sum_(e|r,e<r) (e/r) Phi_e` by (1). Every primitive frequency of `Phi_e` is nonzero and has circular size at least `1/(5e)`, also for `e=1`. Consequently if `B>10E` the whole proper-divisor part is annihilated by `eta(B theta)` on each conductor before the mask is made. This eliminates all of (8) exactly.

A broad instance uses the original shell with largest left endpoint `R<=X/1000`, so `X/2000<R<=X/1000`. Fix any integer `l>=3` and use (12). Take `B=X^(1-1/(2l))` and `L=floor(R/100)` in (4). The largest proper divisor is at most a constant times `R^(1-1/l)`, and `B/R` tends to zero by a fixed power. Thus `B>10E` eventually. Every original cap in (13) admits `|theta|<=2/B`. For its first cap `R^3/X^2` has order `X` and `10r/B=O(X^(1/(2l)))`. For the two `r`-relative caps, use `1-1/(2l)>1/2`. The split primes in (12) lie below `z`, including at `l=3`, since their cubes at `l=3` are at most `7R/5<4X`. These fixed prime choices give actual surviving conductors by the same divisibility, cofactor and numerator-one checks as in §4. In particular `B/(5r)` tends to zero.

Now the tail estimate before the last inequality of (10) is

\[
 \sum_{|j|>L}|(p_X*q_B)(j)|\ll_l (\sqrt X/L)^3+(L/B)^{1-M}
 \ll_l X^{-3/2}
\]

for a fixed order `M>3l+1`. The two convolutions are applied with `F_n` frozen. All shifted raw values in the central shift range vanish by (4), and the total outer raw mass is `O_eps(R X^eps)`. Therefore the actual smooth moving amplitude satisfies

\[
             \boxed{\ \|V\|_w^2\ll_{l,\epsilon} X^\epsilon.\ }          \tag{15a}
\]

This estimate holds on the full taper including the endpoints. On `[X,2X)` the number of selected times per `r` is at least `(3/5)(1-2L/r)X-10r`, by counting complete periods as in §4. With the present `R,L` this is at least `X/2` on sufficiently late blocks. There are therefore `>>_l X^2/(log X)^l` incidences of actual nonzero numerator-one modes. The constants and the onset may depend on the fixed factor count. These bounds concern these specific smooth packets, whose cutoff retains a growing range of numerator values up to order `r/B`.

## 7. Periodic moving masks without an interval loss

Here recover the full sharp cap for a wider class. Define `W_r(n)` on all integers as the indicator of the robust zero plateaux in (4), allowing the floor quotient to be any integer and extending `H` periodically. On the taper this gives the same `1_(r in F_n)` for `r in F`. The case `L=0` retains every zero residue, with no buffer. The function `W_r` is periodic of period `5r` and has at most six jumps in one period. If `w_r(b)` denotes its discrete Fourier coefficient at `b/(5r)` for signed centered `b`, then

\[
              |w_r(b)|\ll (1+|b|)^{-1}.                             \tag{15b}
\]

At nonzero `b`, divide the Fourier coefficient of its first difference, at most `6/(5r)` in absolute value, by `1-e(-b/(5r))`. Its constant coefficient has magnitude at most one. This is uniform in the margin.

The reflection `n` to `-1-n` sends `floor(n/d)` to `-1-floor(n/d)` for every positive integer `d`. The residue values give `K_d(-1-n)=-K_d(n)`, and so `Phi_e` has the same odd reflection by (1). The mask `W_r` has even reflection, because the three zero residues are mapped to each other and the margins are symmetric. The original even multiplier `m_X` commutes with that reflection. For each `e|r`, therefore, `W_r*(m_X Phi_e)` with pointwise multiplication, as a function of time, is odd under reflection and has mean zero over its period `5r`.

Consider the moving proper-divisor amplitude in the complete Jackson-smoothed packet. Its Fourier expansion is, up to its common minus sign, the sum over `r=q e` in `F`, `e<r`, and numerators `a,b` of the coefficient

\[
 \frac{A_r}{q}b(e,a)m_X(a/(5e))w_r(b)
\]

at frequency `(a+b/q)/(5e)`, with `e<=E`, `q>=R/E`, and `a!=0`. The product here is exactly the pointwise product of the preceding paragraph. Thus all terms with `a q+b=0` cancel together for each fixed `r,e` in its zero mean. No other terms are at zero modulo one, since the signed frequency representatives before addition have magnitudes at most `2/sqrt(X)` and `1/2`.

Fix `q,a,b` with `nu=a+b/q!=0` and set `Z=R/q`. The selected `e` range over distinct integers in `(Z,2Z]`. Their frequencies have ordinary spacing at least `|nu|/(20 Z^2)`. All these frequencies have the same sign, their magnitudes are at most `1/2+2/sqrt(X)`, and the ratio of largest to smallest magnitude is at most two, since the numerator `nu` is fixed. They therefore occupy an interval of length less than `1/2` on the real line at late scales, so the same lower spacing applies on the circle. The translated large sieve, (2), (15b), and `|b(e,a)|<<1/|a|` bound the norm for these fixed `q,a,b` by

\[
 \ll_\epsilon \frac{X^\epsilon\sqrt Z}{q|a|(1+|b|)}
                \left(\sqrt X+\frac{Z}{\sqrt{|\nu|}}\right).          \tag{15c}
\]

The support contains at most `2Z` possible `e`, since all are positive integers. The permitted `a,b` are of magnitude `O(X)`. For `|nu|>=1/2`, both sums over `a,b` in (15c) cost only logarithms. On `0<|nu|<1/2`, write `j=aq+b`, so `1<=|j|<q/2` and `|b|>=q|a|/2`. For the part with `|nu|^(-1/2)` the sum of the two weights is

\[
 \ll \sum_{a\ne0}|a|^{-2}\;q^{-1/2}
                               \sum_{1\le |j|<q/2}|j|^{-1/2}\ll 1.
\]

The part without `|nu|^(-1/2)` is also bounded by the same estimate there. Summing (15c) by the norm triangle inequality over proper `q>=max(2,R/E)` now costs at most

\[
 X^\epsilon\sum_q \left(\frac{\sqrt{XR}}{q^{3/2}}
                         +\frac{R^{3/2}}{q^{5/2}}\right)
     \ll_\epsilon X^\epsilon(\sqrt{XE}+E^{3/2}).                    \tag{15d}
\]

This proves a proper-divisor squared leakage bound `O_eps(X^eps(XE+E^3))`, with no factor for the number of moving intervals. The constant coefficient cancellation is necessary in this argument. The interval proof in §2 remains applicable to other time masks that do not have the reflection used here.

For the raw part at `L=0`, freeze `F_n` at the evaluation time. Its raw polynomial vanishes at `n`; on positive times near the taper its successive difference is bounded by `sum_(r|v,r in F_n)|A_r|<<_eps X^eps`, since `K_r(v)-K_r(v-1)=1_(r|v)chi_5(v/r)`. For `|j|<=X/2` use these increments along the shift, and average against the original Jackson weights, whose first absolute moment is `O(sqrt(X))`. For `|j|>X/2` use their cubic tail (3) and the global raw sup bound `O_eps(R X^eps)`. Thus the raw contribution to the squared norm is `O_eps(X^(2+eps))` on the full taper. The sharp-cap comparison of §5 applies unchanged to this mask. Together with (15d), this proves a complete sharp-cap moving removal at target scale for every such fixed family with `R>=c X^(3/4)` and `E=O(X^(2/3))`.

For example take `R` comparable to `X^(3/4)` and the conductors (12) with a fixed number `3<=l<=9` of distinct factors. Here `E=O(R^(1-1/l))=O(X^(2/3))`. The proof deletes the **whole original capped amplitude** for the moving zero mask, with all its actual signed coefficients. Since the mask has no buffer, at least `X/2` times per conductor qualify on `[X,2X)` at late scales, by the complete-period count. These examples extend the whole-cap assertion of §5.

## 8. Coupling and what remains

For either chosen volume of removal, let `V` be its actual tapered amplitude from the definitions above, including the time-dependent conductor mask. Take the full replacement quantity to be

\[
 Q_{\rm new}=Q_7-2\operatorname{Re}\langle V,G_7+C_z\rangle_w
                    +\|V\|_w^2 .                                  \tag{16}
\]

All mixed products are explicit in (16), including `V` with the original prime correction and the full prime correction with `G_7`. The original round-seven norm comparison gives exactly

\[
 Q_{\rm new}=\|G_7-V+C_z\|_w^2+O_\epsilon(X^{2+\epsilon}).            \tag{17}
\]

This follows by subtraction and expansion of the squared norm. The comparisons with `T` retain the original same-argument `C_z`, its repeated prime term, and every endpoint, because only the amplitude `V` is subtracted. The compact balanced carrier, including its two affine terms and signed unit treatment, is used only through the previously established comparison to the same `T` and is unchanged. The norm triangle inequality and (11) or the sharp-cap bound preserve the original all-epsilon criterion on all sufficiently late dyadic blocks. This argument does not bound the difference of the two energies by the squared removal norm. The dynamic mask changes the time factors, so the original determinant-strip identity is used only for `Q_7`, and is not asserted for the new amplitude.

**O.** The remaining complete signed norm in (17) still needs its power-scale estimate. The removable packets do not constitute an estimate of the untouched frequencies or of the original total. No independent claim is made for the affine or prime profile pieces separately.

## Inputs and verification scope

Read PUBLIC candidate sources at head `6649670532e4d69858bc92994a55a54682f5d619`, including rounds three, four, five, six and seven for the fixed cotangent coefficient, probability kernel, divisor weighting, rough core and retained conductor caps, and the pinned KERNEL large sieve. The fixed-modulus prime number theorem used only to count actual incidences is the one already attributed in round-five SMOOTH-SUPPORT and round-seven SMOOTH-DIVISOR-AND-TRANSFER to [Yamada, Explicit formulae for primes in arithmetic progressions, I](https://arxiv.org/html/1306.5322v4#S1). The latest neighboring #2093 full-level and full-coupled energy notes were read for scope, and supply no estimate used here. Derived on paper: the uniform moving proper-divisor bound, smooth and whole-cap deletions, incidence count, and complete cross-term identity. No scientific computation, sampling, external independent verification or formal verifier execution. The all-epsilon complete Q7 bound was not proved.
