# The positive second term in the large-prime slice

C-RH-ARITHMETIC-KERNEL-N, issue #2087. NON-CANONICAL, no authority. Candidate-D paper continuation on classical analytic inputs. The comparison source is draft #2089 at `59a41b28b9c6cedaf2fa3ef4a0a23e197a87d1cd`. No scientific computation or repo change was performed in this lane.

## 1. The actual split-residue tail and its large-prime slice

Let `chi=chi_5`, `S_chi(v)=sum_(j<=v) chi(j)`, and let `w(d)=(-2)^omega(d)` on squarefree products of split primes, with `w(1)=1` and `w(d)=0` off that support. Put

\[
T(X)=\sum_{d\le X}w(d)S_\chi(X/d),\qquad
R(X)=\sum_{X^{2/3}<d\le X} w(d)S_\chi(X/d).
\]

As in the pinned rough-tail note, `B(X)` is the part of `R(X)` with least prime factor strictly greater than `X^(1/3)`, and `H(X)=R(X)-B(X)`. Fix a real `a` with `2/3<=a<1`, and let `C_a(X)` be the part of `R(X)` for which the greatest prime divisor of `d` is strictly greater than `X^a`. Denote its contributions from `B` and `H` by `C_a^B` and `C_a^H`, respectively. For every `X>1`,

\[
 C_a(X)=-2\sum_{X^a<p\le X,\ \chi(p)=1}T(X/p),\qquad
 C_a^B(X)=-2\sum_{X^a<p\le X,\ \chi(p)=1}S_\chi(X/p),\qquad
 C_a^H=C_a-C_a^B.
 \tag{1}
\]

Indeed, two prime factors greater than `X^a` have product greater than `X`. In the unique factorization `d=pe` with this large prime `p`, the cofactor satisfies `e<=X/p<p` and `d>X^(2/3)`. Thus `w(pe)=-2w(e)`. Every term with `e>1` belongs to `H`: a prime `q|e` satisfies `q<=e<=X/p<X^(1/3)`. The part `B` in this slice therefore consists precisely of the split primes themselves. These identities keep the actual sharp cutoffs and the same argument `X`.

## 2. A prime averaging estimate with the cutoff intact

Fix `0<a<1` for this averaging estimate. For `u>=1` take `F(u)=T(u)`, `F(u)=S_chi(u)` or `F(u)=M(u)`. Write `F(u)=sum_(m<=u) c(m)`, with `c=w*chi`, `c=chi` or `c=mu` respectively, and `*` Dirichlet convolution. All three cases have

\[
 \sum_{m\le Z}\frac{|c(m)|}{m}\ll (1+\log Z)^2,\qquad
 |F(u)|\ll u\exp(-c_0\sqrt{\log u})\quad(u\ge2)
 \tag{2}
\]

for some `c_0>0`. To prove the harmonic bound for `T`, use `|w|<=1*chi`. This majorant is nonnegative by its local prime-power factors and has sum through `Z` bounded by `Z`, since that sum is `sum_(e<=Z) S_chi(Z/e)` and `|S_chi|<=1`. Partial summation bounds its harmonic sum by `1+log Z`. Convolving it with `|chi|<=1` gives the squared logarithm. The harmonic bounds for the other two functions follow from `|chi|,|mu|<=1`. The pointwise bound is immediate for `S_chi` and is the classical unconditional Mertens bound for `M`.

For `T`, the pinned coefficient unit is `zeta(s)^(-1)=U(s)L(s,chi)S_5(s)`, where `S_5(s)=sum w(d)d^(-s)`. The expansion of `1/U(s)` has coefficients `v(d)` satisfying `sum |v(d)|d^(-sigma)<infinity` for every `sigma>1/2`. It gives `T(u)=sum_(d<=u) v(d)M(u/d)` with `M` the Mertens function. For `d<=sqrt(u)`, the classical de la Vallée Poussin form of the Mertens bound gives `O(u exp(-c_1 sqrt(log u)))` after summation with `|v(d)|/d`. For `d>sqrt(u)`, the bound `|M(y)|<=y` and convergence at `sigma=3/4` give `O(u^(7/8))`. This proves (2), and also gives `R(X)=O_A(X/(log X)^A)` for every fixed `A>0`, because the omitted support has absolute weight at most `X^(2/3)` by the same majorant.

Write `D=X^a`, `Z=X/D`, `L=log X` and let `Pi(y)` count split primes at most `y`. Finite summation gives the exact identity

\[
 \sum_{D<p\le X,\,\chi(p)=1} F(X/p)
 =\sum_{m\le Z}c(m)\bigl(\Pi(X/m)-\Pi(D)\bigr).
 \tag{3}
\]

Use the fixed-modulus prime number theorem with an error of arbitrary fixed inverse logarithmic order. Thus `Pi(y)=Li(y)/2+O_A(y/(log y)^A)` for every fixed `A>0`. Every argument in (3) is at least `D`, and `D<=X/m` for all retained `m`. By the harmonic bound in (2), the total error after the prime replacement is `O_{A,a}(X L^(2-A))`. This estimate accounts for every jump and does not assume that `F` is monotone. Interchanging the finite sum with the integral of `1/log t`, followed by `u=X/t`, now gives

\[
 -2\sum_{D<p\le X,\,\chi(p)=1} F(X/p)
 =-X\int_1^Z\frac{F(u)}{u^2(L-\log u)}\,du
 +O_{A,a}(X L^{2-A}).
 \tag{4}
\]

For every fixed positive integer `m`, the geometric expansion of `1/(L-log u)` on `1<=u<=Z` has first `m` terms `sum_(0<=j<m) (log u)^j/L^(j+1)`. Its remainder has absolute value at most `(log u)^m/(a L^(m+1))`. Equation (2) makes every absolute logarithmic moment of `F(u)/u^2` finite. Replacing the upper limit `Z` by infinity in each such moment makes an error smaller than any fixed inverse power of `L`: after `t=log u`, the absolute tail is bounded by a constant times `int_((1-a)L)^infinity t^j exp(-c_0 sqrt(t)) dt`. Taking `A` large enough in (4), we obtain

\[
 -2\sum_{D<p\le X,\,\chi(p)=1} F(X/p)
 =-X\sum_{j=0}^{m-1}\frac{(-1)^j G_F^{(j)}(1)}{L^{j+1}}
 +O_{m,a}(X/L^{m+1}),
 \qquad
 G_F(s)=\int_1^\infty F(u)u^{-s-1}\,du\quad(\Re s>1).
 \tag{5}
\]

For the derivatives at one, the Mellin transforms have analytic germs there, given below. Differentiation under the integral for real `s>1` followed by the limit `s` decreasing to one gives the logarithmic moments by dominated convergence and (2). No convergence of the same integral to the left of one is needed. The argument establishes (5) for each fixed number of terms and each fixed `0<a<1`.

## 3. Matched cancellation and its residual

The two Mellin germs at `s=1` are

\[
 G_T(s)=\frac1{s\zeta(s)U(s)},\qquad
 G_{S_\chi}(s)=\frac{L(s,\chi)}s.
\]

For the first, `zeta` has a simple pole of residue one and `U(1)>0`. Indeed each local factor of `U(1)` is positive and the product converges to a nonzero value. Hence `G_T(1)=0` and `G_T'(1)=1/U(1)>0`. The second germ has `G_{S_chi}(1)=L(1,chi)>0` and `G_{S_chi}'(1)=L'(1,chi)-L(1,chi)`. Taking `m=2` in (5) gives, with `kappa=1/U(1)` and `lambda_1=L'(1,chi)-L(1,chi)`,

\[
\begin{aligned}
C_a(X)&=\kappa\frac{X}{L^2}+O_a(X/L^3),\\
C_a^B(X)&=-L(1,\chi)\frac{X}{L}+\lambda_1\frac{X}{L^2}+O_a(X/L^3),\\
C_a^H(X)&=+L(1,\chi)\frac{X}{L}+(\kappa-\lambda_1)\frac{X}{L^2}+O_a(X/L^3).
\end{aligned}
 \tag{6}
\]

Thus the opposing leading terms on this same prime range and the same argument cancel. Their sum has a strictly positive second term. The remaining tail `R-C_a` has the opposite second term, by the bound for `R` above. In fact it has the opposite expansion through every fixed logarithmic order by (5). The positive-part contribution of `C_a` alone on full windows satisfies

\[
 \sum_{Y\le n<Y^2}\frac{(C_a(n)_+)^2}{n(n+1)}
 \sim\frac{\kappa^2Y^2}{16(\log Y)^4}.
\]

For fixed `0<epsilon<1`, on `epsilon Y^2<=n<Y^2` the summands are uniformly `(1+o(1)) kappa^2/(16(log Y)^4)` by (6), since `log n=2 log Y+O_epsilon(1)`. The remaining at most `epsilon Y^2` summands with `n>=Y` each are `O_a((log Y)^(-4))`. Taking `Y` to infinity first and then `epsilon` to zero proves the asymptotic. Controlling this positive slice separately from its complement cannot yield the required window bound. The cancellation of finite logarithmic terms or even any fixed list of such terms provides no square-root estimate for the full remainder.

## 4. Mertens inner sum and the precise bridge

For a fixed `0<a<1`, the same averaging calculation separately gives

\[
 U_a(X):=-2\sum_{X^a<p\le X,\,\chi(p)=1} M(X/p)
 =\frac{X}{(\log X)^2}+O_a\left(\frac{X}{(\log X)^3}\right).
 \tag{7}
\]

Indeed for `Re(s)>1`, integration of the sharp Mertens sum gives `G_M(s)=1/(s zeta(s))`. Its analytic germ at one has `G_M(1)=0` and `G_M'(1)=1`. Formula (5), applied with `m=2`, gives (7) including `a=1/2`. When `a>=1`, the prime interval is empty and this asymptotic does not apply. For `a=1/2` the cutoff fits the reported neighboring Mertens formula. The proof here uses the actual prime average (7) alone and does not assume an identity with another orientation statistic.

At matched exponents `2/3<=a<1`, the exact analytic relationship is `G_T(s)=G_M(s)/U(s)`. Consequently `C_a(X)=U(1)^(-1)U_a(X)+O_a(X/(log X)^3)` on the same arguments. This comparison distinguishes the Mertens inner sum and the residue-weighted inner sum, and determines the ratio of their leading positive coefficients. The error remains at logarithmic scale.

## 5. Source comparison

- The leading pure-prime term `C_(2/3)^B` was already proved in the pinned `WINDOW-TAIL.md`. The new comparison here uses the full cofactor transform `T(X/p)` on the same range and evaluates the second term for `C_a`, including its exact coefficient. It also places the positive residual and its opposite inside the signed decomposition of the same `R(X)`.
- A neighboring chat report identifies the local branch `notes/c-rapidity-joint-cancellation-n`, abbreviated commit `757b3b28`, and files `JOINT_PROOF.md`, `SUPPORT_COUNT.md` and `REVIEW.md`. GitHub returned no commit for either the branch or the abbreviated ref. The full files were unavailable in this lane and no public source or authority for that local branch was established. Equation (7) reconstructs the reported Mertens prime average on its stated inputs. Equations (1)–(6) are proved for the separately pinned `T,R,H,B`. In particular, a cardinality bound for a support class, even at a moving `k<=floor(log log X)`, does not identify the two signed cofactor moments in (5). A support-class comparison must match the weights and the residue kernel at the same argument before it can transfer a main term.
- Draft #2088 at `1f2e9028d745b6018cd3d092c9f0103712c62722` supplies the added six-unit observation separating the Boolean tail witness already reported in #2089. It does not produce the Mellin moment or uniform cofactor average used in (5).
- Draft #2071 at `948ddd240340e14d6bbac96baade3039e8b9f263` remains round 19 at this check. Its verified local scope is the paper improvement of a span-to-slope inequality and a separate finite commutator criterion. The actual period gap remains open, and the note introduces no comparison with the residue-weighted cofactor sums in (1).

## References

- [Pinned window-tail proof, equation (4)](https://github.com/mathorn1973/twist-j/blob/59a41b28b9c6cedaf2fa3ef4a0a23e197a87d1cd/notes/C-RH-ARITHMETIC-KERNEL-N/WINDOW-TAIL.md)
- [Pinned foundation, coefficient unit](https://github.com/mathorn1973/twist-j/blob/59a41b28b9c6cedaf2fa3ef4a0a23e197a87d1cd/notes/C-RH-ARITHMETIC-KERNEL-N/FOUNDATION.md)
- [Pinned rough-tail proof](https://github.com/mathorn1973/twist-j/blob/59a41b28b9c6cedaf2fa3ef4a0a23e197a87d1cd/notes/C-RH-ARITHMETIC-KERNEL-N/ROUGH-TAIL.md)
- [Yamada, Explicit formulae for primes in arithmetic progressions, I, arXiv:1306.5322v4, introduction](https://arxiv.org/html/1306.5322v4#S1). The classical prime number theorem with error stated there suffices at fixed modulus for arbitrary fixed inverse-logarithmic orders in (3). Discarding higher powers in the weighted prime-power version and applying ordinary partial summation gives the estimate for `Pi`. No explicit error constant is consumed here.
- [Lee and Leong, New explicit bounds for Mertens function and the reciprocal of the Riemann zeta-function, arXiv:2208.06141v4, Theorem 1.1](https://arxiv.org/html/2208.06141v4#Thmtheorem1.1)
- [Pinned six-unit split, draft #2088](https://github.com/mathorn1973/twist-j/blob/1f2e9028d745b6018cd3d092c9f0103712c62722/notes/C-J-SHORT-ADDITIVE-SEPARATORS-N/SIX_UNIT_SPLIT.md)
- [Pinned round 19 report, draft #2071](https://github.com/mathorn1973/twist-j/blob/948ddd240340e14d6bbac96baade3039e8b9f263/notes/C-RH-SEMISTABLE-FRAME-N/round19/REPORT.md)
