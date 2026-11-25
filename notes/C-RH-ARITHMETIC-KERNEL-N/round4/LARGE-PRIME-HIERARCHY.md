# Two large prime factors and a tuned third-order obstruction

C-RH-ARITHMETIC-KERNEL-N, issue #2087. NON-CANONICAL, no authority. Candidate-D paper continuation using classical unconditional analytic inputs. The inherited objects are read at draft #2089 head `09ae5168191eed9cee484c08c5d65f58b31494d1`. No scientific computation was performed. The proof concerns fixed power cutoffs.

## 1. Exact count partition at the original tail boundary

Let `chi=chi_5`, `S_chi(y)=sum_(n<=y) chi(n)`, and let `w(d)=(-2)^omega(d)` on squarefree products of primes with `chi(p)=1`. Set `w(1)=1` and `w(d)=0` elsewhere. Retain the earlier full sum `T(X)=sum_(d<=X) w(d) S_chi(X/d)` and its tail `R(X)` on `X^(2/3)<d<=X`. The inherited split `R=H+B` places in `B` only those tail terms whose primes all exceed `X^(1/3)`.

Fix `1/3<a<1/2`. Write `z=X^a`, `D=X^(2/3)`, and `L=log X`. Let `W_j(X)` be the part of `R(X)` with exactly `j` prime factors greater than `z`. There are only `j=0,1,2` on this support, since a product of three such primes exceeds `X`. In all prime sums below the primes are split. The two-prime part has the exact formula

\[
 W_2(X)=4\sum_{z<p<q,\ pq\le X}T(X/(pq)).                         \tag{1}
\]

Indeed `pq>z^2>D`. Moreover every cofactor `e<=X/(pq)` satisfies `e<X^(1-2a)<X^(1/3)<z`. Thus the two primes are distinct, cannot reappear in the cofactor, and are precisely the two prime factors above the cutoff. The weight factors as `w(pqe)=4w(e)`. This also shows that the restriction of `W_2` to `B` is exactly the same sum with `S_chi` in place of `T`, corresponding to `e=1`.

For one distinguished large prime, the exact incidence identity is

\[
 W_1(X)+2W_2(X)
   =-2\sum_{z<p\le X}
        \sum_{\substack{D/p<e\le X/p\\p\nmid e}}
        w(e)S_\chi(X/(pe)).                                      \tag{2}
\]

Each divisor of the tail with `j` large prime factors is counted `j` times, always with its original weight. The exclusion `p` not dividing `e` is significant because `a<1/2`. Removing the lower bound and that exclusion costs

\[
 W_1(X)+2W_2(X)=-2\sum_{z<p\le X}T(X/p)
                +O(X^{2/3}+X/z).                                \tag{3}
\]

For the lower bound, squarefree terms `d<=D` are counted at most twice and have total absolute weight at most `D`. For repeated `p`, any contributing `e` has the form `pf` with `p` not dividing `f` and `|w(e)|=2|w(f)|`. Their weight is bounded by a constant times `sum_(p>z) X/p^2 << X/z`. Both estimates use the inherited `sum_(d<=y)|w(d)|<=y` and `|S_chi|<=1`.

## 2. The cumulative count of two primes with a signed cofactor

Take `F=T` or `F=S_chi`, and write `F(u)=sum_(m<=u)c(m)`. The prior averaging note proves `sum_(m<=V)|c(m)|/m << (1+log V)^2` and `|F(u)| << u exp(-c_0 sqrt(log u))` for `u>=2`; also `|F(u)|<=u` for `u>=1`. Denote the split-prime count by `Pi(y)`. The fixed-modulus prime number theorem in the form `Pi(y)=Li(y)/2+O_A(y/(log y)^A)` is valid for every fixed `A>0`.

For `z^2<=y<=X` the ordered count allowing equality is

\[
 P_z(y)=\sum_{z<p\le y/z}\bigl[\Pi(y/p)-\Pi(z)\bigr].
\]

Put `f_y(t)=Li(y/t)-Li(z)` on `z<=t<=y/z`. Replacing the inner counts by their main terms gives an error `O_(A,a)(y L^(1-A))`: both arguments are at least `z`, `z<=y/p`, and `sum_(p<=X)1/p<=1+log X` suffices. For the outer sum, write `E(t)=Pi(t)-Li(t)/2`. Stieltjes partial summation controls the error by `|f_y(z)E(z)| + int |f_y'(t)E(t)| dt`, with no upper endpoint contribution since `f_y(y/z)=0`. Here

\[
 0\le f_y(z)\le \frac{y}{z\log z},\qquad
 |f_y'(t)|=\frac{y}{t^2\log(y/t)},\qquad
 |E(t)|\ll_{A,a} tL^{-A}.
\]

Since `log(y/t)>=aL` and `log((y/z)/z)<=L`, the outer error is `O_(A,a)(y L^(-A))`. In particular the estimate

\[
 P_z(y)=\frac14\int_z^{y/z}\int_z^{y/t}
           \frac{dv\,dt}{\log v\log t}
        +O_{A,a}(y L^{1-A})                                       \tag{4}
\]

is uniform over the full range, including at `y=z^2` where the count vanishes. The factor `1/4` is the product of the two split densities. This cumulative estimate avoids any monotonicity assumption on the signed function `F`.

Write `V=X/z^2`. Summing the ordered count `P_z(X/m)` with `c(m)` for `m<=V` gives the ordered double-prime sum with cofactor `F(X/(pq))`. Its diagonal `p=q` has absolute size at most `sum_(p>z) X/p^2=O(X/z)`. After removing it and multiplying by two to obtain the coefficient four on unordered pairs, equation (4) gives

\[
4\sum_{z<p<q,\ pq\le X}F(X/(pq))
 =\frac12\iint_{t,v>z,\ tv\le X}
          \frac{F(X/(tv))}{\log t\log v}\,dt\,dv
    +O_{A,a}\bigl(XL^{3-A}+X/z\bigr).                              \tag{5}
\]

The harmonic bound for `c` accounts for the extra two powers of `L` in this error. The strict inequalities in the prime count are preserved before the integrals are introduced.

## 3. The first two surviving logarithmic terms

In (5) set `u=X/(tv)` and `b=1-(log u)/L`. The integral, including its factor `1/2`, becomes

\[
 \frac{X}{L}\int_1^V\frac{F(u)}{u^2}g_a\!\left(1-\frac{\log u}{L}\right)du,
 \qquad
 g_a(b)=\frac{1}{b}\log\frac{b-a}{a}.                             \tag{6}
\]

In fact, for fixed `u` the remaining variable `v_1=(log t)/L` ranges from `a` to `b-a`, and

\[
 \int_a^{b-a}\frac{dv_1}{v_1(b-v_1)}
      =\frac{2}{b}\log\frac{b-a}{a}.
\]

This supplies the factor two that cancels the one half in (5). For fixed `a`, the function `g_a` has bounded derivatives of any fixed order on `2a<=b<=1`. Taylor expansion at one gives a uniform remainder throughout that interval. All absolute logarithmic moments of `F(u)/u^2` converge, and extending the moment integrals from `V=X^(1-2a)` to infinity costs less than every fixed inverse power of `L`, using the bound from Section 2. Write `G_F(s)=int_(1)^infinity F(u)u^(-s-1)du` on `Re(s)>1` and evaluate the derivatives at one by the right-hand limit. A factor `(-1)^k` arises both from the Taylor expansion in `-(log u)/L` and from the `k`-th Mellin derivative. For every fixed positive integer `m` this proves

\[
 4\sum_{z<p<q,\ pq\le X}F(X/(pq))
 =X\sum_{k=0}^{m-1}\frac{g_a^{(k)}(1)G_F^{(k)}(1)}{k!L^{k+1}}
   +O_{m,a}(X/L^{m+1}).                                            \tag{7}
\]

Here `A` in (5) is chosen large enough for the requested number of terms. No growth of `m` with `X` is used.

For `F=T`, its Mellin germ is `G_T(s)=1/(s zeta(s) U(s))`. Set `kappa=G_T'(1)=1/U(1)>0` and `nu=G_T''(1)`. Then `G_T(1)=0`. Using (1), (3), (7) and the one-prime averaging formula from the preceding round gives

\[
\begin{aligned}
 W_2(X)&=\kappa g_a'(1)\frac{X}{L^2}
           +\frac{\nu}{2}g_a''(1)\frac{X}{L^3}+O_a(X/L^4),\\
 W_1(X)+2W_2(X)&=\kappa\frac{X}{L^2}-\nu\frac{X}{L^3}+O_a(X/L^4),\\
 W_1(X)+W_2(X)&=\kappa(1-g_a'(1))\frac{X}{L^2}
           -\nu\left(1+\frac{g_a''(1)}2\right)\frac{X}{L^3}
           +O_a(X/L^4).                                           \tag{8}
\end{aligned}
\]

At the same threshold and argument, the `B` slice of `W_2` follows from (7) with `F=S_chi`, whose Mellin germ is `L(s,chi)/s`. Its first term is positive,

\[
 W_2^B(X)=g_a(1)L(1,\chi)X/L+O_a(X/L^2),\qquad
 W_2^H(X)=-g_a(1)L(1,\chi)X/L+O_a(X/L^2).                          \tag{9}
\]

The matched pair therefore cancels at order `X/L` but leaves the positive first term of `W_2` in (8).

## 4. A unique fixed cutoff cancels the second order, with a negative third order

Direct differentiation gives

\[
 g_a'(1)=\frac1{1-a}-\log\frac{1-a}{a},\qquad
 g_a''(1)=2\log\frac{1-a}{a}-\frac2{1-a}-\frac1{(1-a)^2}.            \tag{10}
\]

The first expression is strictly increasing in `a`, since its derivative is `(1-a)^(-2)+(1-a)^(-1)+a^(-1)`. At the lower endpoint it tends to `3/2-log 2`, which lies strictly between `1/2` and `1` by `1/2<log 2<1`. At the upper endpoint it tends to `2`. Hence throughout the interval `W_2` is eventually positive at order `X/L^2` and `W_1` is eventually negative at that order. There is a unique fixed `a_*` in the interval satisfying `g_(a_*)'(1)=1`. At this choice, `g_(a_*)''(1)=-2-(1-a_*)^(-2)`, and (8) gives

\[
 (W_1+W_2)(X)=\frac{\nu}{2(1-a_*)^2}\frac{X}{L^3}+O(X/L^4).        \tag{11}
\]

To determine the sign of `nu`, use the Laurent coefficient `gamma` of `zeta` at one. The germ gives

\[
 \nu=-2\kappa\left(1+\gamma+\frac{U'(1)}{U(1)}\right).
\]

The inert and ramified factors of `U` have nonnegative logarithmic derivative on the real line at one. Each split prime `p>=11` contributes `-2 log p/((p-1)(p-2))`. This series is absolutely convergent. The elementary bound below is sufficient, without estimating the values of the Euler product or of `a_*` numerically:

\[
 \sum_{p\,\text{split}}\frac{2\log p}{(p-1)(p-2)}
 \le\frac{242}{90}\int_{10}^{\infty}\frac{\log t}{t^2}\,dt
 =\frac{242}{900}(1+\log 10)<\frac{847}{900}<1.
\]

Indeed `(n-1)(n-2)>=(90/121)n^2` for `n>=11`, and `log(t)/t^2` decreases on this range. Also `log 10<5/2`, as the first five terms of the exponential series at `5/2` already sum to `4169/384>10`. The harmonic-number characterization gives `gamma>=0`. Thus `nu<0` and the third-order term in (11) is strictly negative.

## 5. The residual that must stay coupled

The inherited unconditional estimate gives `R(X)=O_A(X/L^A)` for every fixed `A>0`. Thus `W_0=R-W_1-W_2` has the opposite leading nonzero term from the union in (8)–(11), at the same `X`. If `a<a_*`, the union is positive at order `X/L^2`. If `a>a_*`, it is negative at that order and `W_0` is positive. At `a=a_*`, the union is negative at order `X/L^3`, and `W_0` is positive at that order. In particular, every fixed cutoff in the stated interval leaves a positive part with energy at least `Y^2/(log Y)^6` up to a positive constant on every sufficiently late window if that part is estimated separately. This follows by retaining `Y^2/2<=n<Y^2`. Also, `W_2` separately always has positive energy of order at least `Y^2/(log Y)^4` up to a positive constant. These lower bounds concern partitions of the actual sharp signed sum, with constants depending on the fixed cutoff.

The proof thus identifies two distinct necessary cancellations. In `W_2`, the rough and non-rough pieces cancel first at order `X/log X`. Combining the one- and two-large-prime families may cancel the next order, but at the unique fixed cutoff where this occurs the remaining no-large-prime family carries an opposing term at order `X/(log X)^3`. The proof does not give a square-root bound for their signed sum, or treat cutoffs depending on `X` or a support count growing with `X`. The moving-support claim mentioned in other work is outside this deduction and is not evidence for any step.

## Inputs

- [Pinned large-prime averaging and Mellin germs](https://github.com/mathorn1973/twist-j/blob/09ae5168191eed9cee484c08c5d65f58b31494d1/notes/C-RH-ARITHMETIC-KERNEL-N/round3/LARGE-PRIME-TAIL.md), Section 2 for the harmonic bound, Mertens input, first-prime expansion and pointwise bound for `R`.
- [Pinned coefficient unit](https://github.com/mathorn1973/twist-j/blob/09ae5168191eed9cee484c08c5d65f58b31494d1/notes/C-RH-ARITHMETIC-KERNEL-N/FOUNDATION.md), the exact local factors of `U`.
- [Pinned rough-tail carrier](https://github.com/mathorn1973/twist-j/blob/09ae5168191eed9cee484c08c5d65f58b31494d1/notes/C-RH-ARITHMETIC-KERNEL-N/ROUGH-TAIL.md), the split `R=H+B` at the cube-root boundary.
- [Yamada, Explicit formulae for primes in arithmetic progressions, I, arXiv:1306.5322v4, introduction](https://arxiv.org/html/1306.5322v4#S1), the classical prime number theorem with error. At fixed modulus five, its error and partial summation give the stated count for split primes. No numerical constant is used.
