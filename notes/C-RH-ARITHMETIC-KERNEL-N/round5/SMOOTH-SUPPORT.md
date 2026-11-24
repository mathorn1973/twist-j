# Smooth support and conductor removal in the actual signed tail

C-RH-ARITHMETIC-KERNEL-N, issue #2087. NON-CANONICAL, no authority. Candidate-D paper continuation on classical unconditional inputs. The input files are read at draft #2089 head `d26ca6caab5dda3875333f9d2ba73b74b55ba674`. No scientific computation was performed. The neighboring smooth-direction calculation in #2093 is credited below and concerns its oriented Mertens coefficients.

## 1. The absolute scale of the split weight

Let `s(d)=(-2)^omega(d)` on squarefree products of split primes, including `s(1)=1`, with zero elsewhere. Write `P^+(d)` for the largest prime factor, with `P^+(1)=1`. Define

\[
 W(x,y)=\sum_{d\le x,\ P^+(d)\le y}|s(d)|.
\]

For the next calculation let `L=log x`, `y=cL^2`, `H=log y`, and `k_c=-log(2 sqrt(c))`. The constants are uniform when `c` ranges over any compact subinterval of `(0,infinity)`. The weighted count has the following logarithmic expansion:

\[
 \boxed{\displaystyle
 \log W(x,y)=\frac L2+(1-k_c)\frac L H
       +(2-2k_c)\frac L{H^2}
       +2(k_c-2)^2\frac L{H^3}
       +O\!\left(\frac L{H^4}\right).}                           \tag{1}
\]

The Euler product is `Z(sigma)=prod_(p<=y, split)(1+2p^(-sigma))`. Its factor two and the density one half of split primes combine to give unit density in the following weighted means. Under the probability assigning a subset of those primes, of product `d`, mass `|s(d)|d^(-sigma)/Z(sigma)`, prime inclusions are independent. Write `mu` for the mean of `log d`. With `u=1-sigma=1/2+k/H` and `k` in a bounded interval, fixed-modulus PNT and partial summation give, to any fixed inverse-logarithmic precision `B`,

\[
 \mu=\frac{y^u}{u}+O_B(L/H^B),\qquad
 \log Z(\sigma)=\operatorname{Li}(y^u)+O_B(L/H^B).               \tag{2}
\]

For details, the inclusion probability is `2p^(-sigma)/(1+2p^(-sigma))`. Replacing it by `2p^(-sigma)` in the mean costs `O(sum_(n<=y)n^(-2sigma) log(2n))=O(H^2)`. Expanding the logarithms of the Euler factors costs `O(H)`. Both errors are smaller than every fixed `L/H^B` because `n^(-2sigma)<<1/n` for `n<=y` in this bounded `k` range. For the remaining prime sums, the leading integrals are `int_(2)^y t^(-sigma)dt` and `int_(2)^y t^(-sigma)dt/log t`. These are `y^u/u+O(1)` and `Li(y^u)+O(1)`, respectively. To see the required error uniformly, split at `sqrt(y)`. The lower portion has power saving and the upper portion uses the fixed-modulus prime-count error with a larger fixed inverse-logarithmic exponent. This proves (2) while retaining squarefreeness through the actual local factors.

Put `b=L^(2/3)`. Choose `sigma` so that `mu=L-b`. Such a choice is possible with bounded `k`: the mean is continuous and strictly increasing in `k`, and the normalized mean in (2) tends to `2 sqrt(c) exp(k)` uniformly for bounded `k`. Independence gives

\[
 \operatorname{Var}(\log d)\le H\mu=O(HL).
\]

Chebyshev's inequality thus places probability `1-o(1)` on `L-2b<=log d<=L`. Rankin's upper bound is `W(x,y)<=Z(sigma)e^(sigma L)`. Conversely, that probability interval contributes at least `(1-o(1))Z(sigma)e^(sigma(L-2b))` to `W`. The logarithms of these bounds differ by `O(b+1)=o(L/H^4)`. The lower bound also applies to the counted mass restricted to this interval.

As `y^u/u=L+O(L/H^5)` at the chosen mean, taking logarithms gives `k=k_c+log(1+2k/H)+O(H^(-5))`. Expanding yields

\[
 k=k_c+\frac{2k_c}{H}+\frac{4k_c-2k_c^2}{H^2}+O(H^{-3}).
\]

The three-term expansion of the logarithmic integral, by integration by parts, gives

\[
 \log Z(\sigma)=\frac{L}{H}\left(1+\frac1{uH}+\frac2{(uH)^2}\right)
            +O(L/H^4)
 =\frac L H+\frac{2L}{H^2}+(8-4k_c)\frac L{H^3}+O(L/H^4).
\]

Together with `sigma L=L/2-kL/H`, this proves (1). At `c_0=1/(4e^2)` one has `k_c=1`. Both the `L/H` and `L/H^2` corrections disappear, and the `L/H^3` correction is the positive term `2L/H^3`.

## 2. The residue kernel witnesses the sharp absolute boundary

For integer `n`, let `K_d(n)=S_chi(n/d)` be the actual residue kernel. It is equal to one on `n/2<d<=n`. In particular this whole interval is inside the inherited tail `d^3>n^2` once `n>8`. For a fixed `c`, the absolute smooth tail is

\[
 J_c(n)=\sum_{n^{2/3}<d\le n,\ P^+(d)\le c(\log n)^2}
              |s(d)K_d(n)|.
\]

It is bounded above by (1) at `x=n`. A matching lower bound to the precision of (1) holds on an unbounded sequence of integer intervals, each of length comparable to its own argument. Indeed use the preceding tilted construction at arbitrarily large `x`, with `y=c(L-3b)^2`. Its ratio to `L^2` differs from `c` by `O_c(b/L)`, so the compact-parameter expansion and concentration above still apply. Partition the concentration interval `[e^(L-2b),e^L]` into multiplicative bins `(v,3v/2]` using a fixed geometric grid. At most `O(1+b)` bins meet the interval. Some bin carries at least that inverse factor of the concentrated weight. For each integer `n` with `ceil(3v/2)<=n<=floor(7v/4)`, the entire bin meets `n/2<d<=n`, and `log n=L+O(b)` with `log n>=L-3b` for large `x`. Thus `y<=c(log n)^2`, and this weight enters `J_c(n)` in full. The loss `O(log(1+b))` in its logarithm and the change of parameters from `x,c(L-3b)^2` to `n,c(log n)^2` are both `o(L/H^4)`. This proves the asserted lower bound uniformly along the chosen intervals.

It follows that the strict power bound `J_c(n)=O_c(sqrt(n))` for all sufficiently large integers holds exactly when `c<c_0`. Below `c_0`, (1) gives even `o(sqrt(n))`. At `c_0`, the ratio to `sqrt(n)` is unbounded by its positive `L/H^3` term on the chosen intervals. The same holds above `c_0` already at the `L/H` term. The proof identifies the constant for the actual residue kernel. It does not give a lower bound for the signed smooth tail. The neighboring orientation paper had already obtained the same strict threshold and an endpoint obstruction by tilted subsets and a terminal band. The sharper expansion (1) evaluates the true saddle for the shared split basis weight and carries it to this residue kernel.

## 3. The power boundary for logarithmic cutoff exponents

If `y_X<=(log X)^(2+o(1))`, then for every fixed `epsilon>0`,

\[
 W(4X,y_X)\ll_\epsilon X^{1/2+\epsilon}.                       \tag{3}
\]

For example, choose a fixed `sigma` strictly between `1/2` and `min(1,1/2+epsilon)`, and then use Rankin's inequality. The logarithm of the product is bounded by `2 sum_(n<=y_X)n^(-sigma)=O_sigma(y_X^(1-sigma))=o(log X)`. For each epsilon this proof is uniform under `y_X<=(log X)^(2+delta)` for a sufficiently small fixed positive `delta` depending on `sigma`. The onset of that range may depend on the chosen threshold sequence. This upper bound does not require PNT. It permits any fixed positive constant before the quadratic logarithm and some slowly growing factors as well. Thus the strict constant in Section 2 and the all-epsilon square-root exponent describe different bounds.

For comparison, if `A>2` is fixed and `y=(log x)^A`, then

\[
 W(x,y)=x^{1-1/A+o(1)}.                                           \tag{4}
\]

Here the same tilted-subset proof works without a higher-order expansion. By PNT the mean satisfies `mu=(1+o(1))y^u/u` uniformly for `u=1-sigma` in a compact interval about `1/A` contained in `(0,1/2)`. The correction between the inclusion probability and `2p^(-sigma)` is bounded in that interval because `2sigma>1`. Choosing the mean `L-b` forces `u=1/A+o(1)` by comparing the two sides at any fixed distance to either side of `1/A`. The partition product has logarithm `O(L/log y)=o(L)`, and the variance remains `O(L log y)`. The matching upper and lower inequalities from Section 1 give (4), including its lower bound in `L-2b<=log d<=L`. With `y=(L-3b)^A`, the same proof and multiplicative-bin argument in Section 2 give absolute tail mass at least `n^(1-1/A-o(1))` on an unbounded sequence of intervals of length comparable to `n`, with the genuine `K_d(n)=1` and `P^+(d)<=(log n)^A`. At least a fixed proportion of each such interval lies in some dyadic block of comparable scale `X`. The unsigned dyadic square error is then at least `X^(3-2/A-o(1))` on an unbounded sequence of blocks. Since `3-2/A>2`, a fixed superquadratic logarithmic exponent cannot be paid uniformly by absolute values at the required all-epsilon scale.

## 4. The two actual deletions and the remaining determinant sum

Let `y_X` be any threshold in (3), fixed for each dyadic block for the conductor calculation. In the actual time sum `T(n)` and separately in its tail `R(n)`, delete precisely the terms `P^+(d)<=y_X`. For all times in the finite taper's support, `n<=17X/8<4X`, so (3) bounds the resulting error pointwise by `O_epsilon(X^(1/2+epsilon))`. If the moving threshold is specified per integer instead, the same uniform assertion holds whenever it is bounded by such a `y_X` throughout this block. After shrinking epsilon, both errors have squared norm `O_epsilon(X^(2+epsilon))` on this support and on the ordinary dyadic block. For a fixed `c<c_0`, a bound `O(sqrt X)` pointwise follows instead from (1), with the constant scale change from `X` to `4X` absorbed by the strict saving.

Now make a separate deletion in the finite trigonometric sum of ROUND3 and FINITE-TAPER. Retain only its conductors `r` with `P^+(r)>y_X`, without modifying their cofactor weight or numerator cut. For the deleted modes, the original bounds give

\[
 \sum_{\substack{r\le4X,\ P^+(r)\le y_X\\a\text{ retained}}}
 |A_r b(r,a)m_t(a/(5r))|
 \ll (1+\log X)^2 W(4X,y_X)
 \ll_\epsilon X^{1/2+\epsilon}.                                 \tag{5}
\]

Indeed `|A_r|<=|s(r)|(1+log(4X))`, `|b(r,a)|<<1/|a|`, and the numerators have absolute value at most `40 sqrt(X)`. The sum of these reciprocals gives the other logarithm. This establishes the pointwise error uniformly in time for the analytic residual. The rational conductor projection satisfies the same bound using `|Phi_r(n)|<=sum_(h|r)1/h<=1+log(4X)` in place of the numerator estimate. These conductor projections are distinct from deleting original support integers `d`. No identification between the masks in the two coordinates is required.

Write `G_X^rough` for the remaining Fourier sum. Define `P_X^(rem,rough)` from the exact remaining signed determinant sum `P_X^rem` in FINITE-TAPER by retaining only pairs whose two conductors satisfy `P^+>y_X`. The finite-time energy identity, distant-pair estimate, same-conductor large sieve, and absolute large-gcd pruning of FINITE-TAPER all apply to this smaller Fourier family. They give, for every fixed epsilon,

\[
 \sum_n w_X(n)|G_X^{\mathrm{rough}}(n)|^2
    =P_X^{\mathrm{rem,rough}}+O_\epsilon(X^{2+\epsilon}),          \tag{6}
\]

where `w_X` is the original finite taper. The condition `(P_X^(rem,rough))_+<<_epsilon X^(2+epsilon)` for every epsilon and all sufficiently late dyadic `X` remains equivalent to the same condition on `P_X^rem`. In fact (5) and the triangle inequality in the tapered square norm yield the equivalence of their finite-block energy bounds, and then (6) gives the determinant criterion. This uses a bound on the norm of the deleted Fourier packet. It does not assert an unconditional bound of order `X^(2+epsilon)` on the difference of the two signed pair sums, since that would also require a cross-term estimate. Through the previously proved finite-block approximation, the rough-conductor determinant criterion also tests the time-domain residual after smooth support deletion.

For the one-sided window, each dyadic weighted square error is `O_epsilon(X^epsilon)` after division by `n(n+1)` on the relevant block. Summation over the intersecting dyadic blocks gives `|sqrt(Q_T(Y))-sqrt(Q_{T^rough}(Y))|<<_eta Y^eta` for every `eta>0`, and the same holds with `R` in place of `T`. The original and deleted sequences satisfy equivalent subpower good-window conditions, with the exponent `2r` in the input window and `eta<1/(4r)` for the error. The argument uses each same `Y` and makes no comparison between independently selected windows.

Finally, the removed conductors have absolute mass `O_epsilon(X^(1/2+epsilon))`, whereas the original signed coefficients have absolute mass of order `X` on `3X<r<=4X`. Thus the actual numerator-one same-sign positive subtotal of FINITE-TAPER remains of order `X^3` after this deletion: the remaining two sign masses still have total of order `X`, and removing their diagonal again costs only `O(X log X)` before multiplication by `X`. The rough conductor criterion therefore still requires cancellation at a power scale. Neither the sharp count in (1) nor the unsigned deletion in (5) supplies that signed estimate.

## Sources and attribution

- [Neighboring #2093, LOCAL-AVERAGES and the original strict smooth-support upper range](https://github.com/mathorn1973/twist-j/blob/853237620bc2be69026168f32bb0ad871f668950/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N/LOCAL-AVERAGES.md)
- [Neighboring #2093, endpoint obstruction in ROUND2-REVIEW](https://github.com/mathorn1973/twist-j/blob/853237620bc2be69026168f32bb0ad871f668950/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N/ROUND2-REVIEW.md)
- [Neighboring #2093, exact Dirichlet readout with the orientation masks](https://github.com/mathorn1973/twist-j/blob/853237620bc2be69026168f32bb0ad871f668950/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N/DIRICHLET-READOUT.md)
- [Neighboring #2093, absolute split basis mass](https://github.com/mathorn1973/twist-j/blob/853237620bc2be69026168f32bb0ad871f668950/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N/MOBIUS.md), Section 1
- [Pinned #2089, actual conductor and numerator data](https://github.com/mathorn1973/twist-j/blob/d26ca6caab5dda3875333f9d2ba73b74b55ba674/notes/C-RH-ARITHMETIC-KERNEL-N/round3/SIGNED-SPECTRUM.md)
- [Pinned #2089, finite taper and remaining determinant criterion](https://github.com/mathorn1973/twist-j/blob/d26ca6caab5dda3875333f9d2ba73b74b55ba674/notes/C-RH-ARITHMETIC-KERNEL-N/round4/FINITE-TAPER.md)
- [Yamada, Explicit formulae for primes in arithmetic progressions, I, arXiv:1306.5322v4, introduction](https://arxiv.org/html/1306.5322v4#S1), the fixed-modulus prime number theorem with more than fixed inverse-logarithmic precision used in (2). No numerical bound is imported.
