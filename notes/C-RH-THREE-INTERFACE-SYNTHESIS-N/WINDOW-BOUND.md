# Bounds for the complete residual on whole windows

**NON-CANONICAL. Authority none.** The deductions below are **candidate-D**.
The native subpower estimate for the complete signed pairing remains **O**.
The action layer is NOT_APPLICABLE.

Take the residual \(R(N)=R_{1/36}(N)\) of
[DIRICHLET-READOUT.md](DIRICHLET-READOUT.md), Sections 4 and 5. Put
\(z_N=(\log N)^2/36\) and \(I(Y)=[Y,Y^{3/2})\cap\mathbf Z\). For a
real sequence \(F\) set
\[
 \|F\|_I^2=\sum_{N\in I}\frac{|F(N)|^2}{N(N+1)},\qquad
 Q_F(Y)=\|F_+\|_{I(Y)}^2.
\]
The sector \(\gamma_d(N)\), support set \(\mathcal D\), and weight
\(w(d)=|a(d)|\) are those in [MOBIUS.md](MOBIUS.md). The complete
pairing is \(R(N)=\sum_{N^{1/4}<d\le N,\ P^+(d)>z_N}\gamma_d(N)\),
with each support in \(\mathcal D\).

## 1. Neutral mean square on the line \(1/4\)

**Candidate-D.** Extend \(C_0(x)=\sum_{n\le x}c_0(n)\) by zero for
\(0<x<1\). Its factorization in [MOBIUS.md](MOBIUS.md) gives
\[
 G(s)=\frac{\mathcal C_0(s)}s
 =\frac{L(s,\chi_5)L(2s,\chi_5)}{s\,\zeta(4s)}
       \frac{1-5^{-s}}{1-5^{-4s}}.
\]
Then
\[
 B^2:=\int_1^\infty |C_0(x)|^2\,\frac{dx}{x^{3/2}}
     =\frac1{2\pi}\int_{\mathbf R}|G(1/4+it)|^2\,dt<\infty.       \tag{1}
\]

The reciprocal zeta factor is holomorphic on \(\Re s\ge1/4\),
with a zero at \(s=1/4\), and is \(O(\log(2+|t|))\) uniformly on
\(1/4\le\Re s\le2\). Use the classical zero-free region and the
reciprocal bound in Theorem 3.1 of
[Lee and Leong](https://arxiv.org/html/2208.06141v4), with bounded
heights handled by continuity. The finite factor at five is
bounded on the same strip.

For the fixed primitive even character \(\chi_5\), the functional
equation of the completed \(L\) function and Stirling's formula
give
\(\left|L(-\epsilon+it,\chi_5)\right|\ll_\epsilon
(2+|t|)^{1/2+\epsilon}\) for \(\epsilon>0\), from absolute convergence
on \(\Re s=1+\epsilon\). The function \(L(s,\chi_5)\) has polynomial
growth on the strip between those two lines. On the right half of
the strip this follows by partial summation using bounded character
sums, and on the left half it follows by the functional equation.
Phragmén–Lindelöf interpolation with the bounded right edge gives
\(\left|L(1/4+it,\chi_5)\right|\ll_\epsilon
(2+|t|)^{3/8+\epsilon}\). Theorem 1 of
[Katsurada and Matsumoto](https://www.math.nagoya-u.ac.jp/~kohjimat/L-functions5.pdf)
gives \(\int_0^T|L(1/2+it,\chi_5)|^2\,dt\ll T\log(2T)\) for \(T\ge2\).
Consequently
\[
 \int_T^{2T}|G(1/4+it)|^2\,dt
  \ll_\epsilon T^{-5/4+2\epsilon}(\log T)^2
                 \int_T^{2T}|L(1/2+2it,\chi_5)|^2\,dt
  \ll_\epsilon T^{-1/4+2\epsilon}(\log T)^3 .
\]
The character is real, so the same bound holds at negative heights.
Taking \(0<\epsilon<1/8\) proves square integrability.

To justify the inverse transform at this line, set \(f(u)=C_0(e^u)\).
For \(\Re s=2\), absolute summation gives
\(G(s)=\int_{\mathbf R}f(u)e^{-su}\,du\). For any smooth compactly
supported test function \(\varphi\), Fourier inversion on that line
gives
\[
 \int_{\mathbf R} f(u)e^{-u/4}\varphi(u)\,du
   = \frac1{2\pi i}\int_{\Re s=2}
        G(s)\left(\int_{\mathbf R}e^{(s-1/4)u}\varphi(u)\,du\right)ds .
\]
Repeated integration by parts gives rapid decay of the inner
integral uniformly in the closed strip. The polynomial growth of
\(G\) on the strip and holomorphy on and to the right of its left
edge allow the contour to be shifted to \(\Re s=1/4\). On that
line the right side is the test-function pairing with the
\(L^2\) inverse Fourier transform of \(G(1/4+it)\). The
distributions agree, so the locally integrable function
\(f(u)e^{-u/4}\) belongs to \(L^2\) and Plancherel gives (1).

## 2. Energy of the moving short-support block

**Candidate-D.** For \(0<a\le1/3\), write
\(S_a(N)=\sum_{d\le N^a,\ d\in\mathcal D}\gamma_d(N)\). More generally
the estimate below allows each summand to be multiplied by any
coefficient of absolute value at most one that depends on \(N,d\).
For each integer \(V\ge11\), put \(J_V=[V,2V)\cap\mathbf Z\). If
\(k\) is a positive integer, the function \(C_0(x/k)\) is constant
almost everywhere on each \([N,N+1)\), and
\[
 \big\|C_0(N/k)\big\|_{J_V}^2
 =\int_V^{2V}|C_0(x/k)|^2\,\frac{dx}{x^2}
 =\frac1k\int_{V/k}^{2V/k}|C_0(u)|^2\,\frac{du}{u^2}
 \le B^2 V^{-1/2} k^{-1/2}.
\]
Here \(\int_N^{N+1} dx/x^2=1/[N(N+1)]\), and
\(u^{-2}\le (V/k)^{-1/2}u^{-3/2}\) when \(u\ge V/k\).

On \(J_V\), expand the exact sector formula of
[MOBIUS.md](MOBIUS.md) with \(k=dm^2\), take the triangle inequality
in the weighted square norm, and use the preceding bound on each
term. The restriction \(d\le N^a\) is a mask of absolute value at
most one on the entire interval. The restriction \(dm^2\le N\)
is automatic because \(C_0(u)=0\) for \(u<1\). Thus the sums may be
bounded after extending over \(d\le(2V)^a\) and allowing all square
powers with \(\operatorname{rad}(m)\mid d\). This gives
\[
 \|S_a\|_{J_V}
   \le B V^{-1/4}
       \sum_{d\le(2V)^a,\ d\in\mathcal D}
          w(d)d^{-1/4}\prod_{p\mid d}(1-p^{-1/2})^{-1}
   \ll_a V^{(3a-1)/4}.                                      \tag{2}
\]
For the last step, let \(v\) be the nonnegative multiplicative
function supported on \(\mathcal D\) with
\(v(p)=2p^{-1/2}/(1-p^{-1/2})\) for split \(p\).
At squarefree \(d\in\mathcal D\), the weight
\(w(d)\prod_{p\mid d}(1-p^{-1/2})^{-1}\) equals \((w*v)(d)\).
The convolution majorizes the weight extended by zero.
The bound \(\sum_{d\le x}w(d)\ll x\) in [MOBIUS.md](MOBIUS.md)
and the convergent product for \(\sum_{m\ge1}v(m)/m\) give a linear
bound for the total modified weight. Partial summation then
gives the \(O(((2V)^a)^{3/4})\) estimate used in (2).

Sum the squares in (2) over the disjoint intervals
\(J_{2^jY}\), restricting the final interval to \(I(Y)\). For
\(a<1/3\) the geometric sum is \(O_a(Y^{(3a-1)/2})\).
At \(a=1/3\) there are \(O(\log Y)\) intervals and each contributes
\(O(1)\). In particular
\[
 \|S_{1/4}\|_{I(Y)}^2\ll Y^{-1/8},\qquad
 \|S_{1/3}\|_{I(Y)}^2\ll\log Y.                              \tag{3}
\]
Both estimates are absolute in the window scale. The moving prime
mask \(P^+(d)>z_N\) is also allowed in (2) and (3).

## 3. Energy of the moving smooth-support block

**Candidate-D.** Set \(L=\log N\), \(z=L^2/36\), \(\ell=\log z\),
\(t_0=\log 3\), and \(\delta_*=t_0-1>0\).
The absolute smooth-support estimate of
[LOCAL-AVERAGES.md](LOCAL-AVERAGES.md) gives
\[
 A(N):=\sum_{\substack{d\le N,\ d\in\mathcal D\\P^+(d)\le z}}
        |\gamma_d(N)|
 \ll N^\sigma
 \prod_{\substack{p\le z\\p\ {\rm split}}}
             \left(1+\frac{2p^{-\sigma}}{1-p^{-2/3}}\right),
 \qquad \sigma=\tfrac12-\frac{t_0}{\ell},
\]
where \(\sigma\ge1/3\) on sufficiently late windows. The logarithm
of the product is at most \(2\sum_{p\le z,\ p\ {\rm split}}p^{-\sigma}
+O(1)\), since \(p^{-\sigma}\le 3p^{-1/2}\) and
\(\sum_p p^{-7/6}<\infty\). By partial summation of the
fixed-modulus prime number theorem, uniformly for this \(\sigma\),
\[
 2\sum_{\substack{p\le z\\p\ {\rm split}}}p^{-\sigma}
 =\int_2^z\frac{u^{-\sigma}}{\log u}\,du
    +O(z^{1-\sigma}/\ell^3).
\]
For this error, use
\(\#\{p\le u:p\ {\rm split}\}=\tfrac12\operatorname{Li}(u)
+O_A(u/(\log u)^A)\), split the partial summation integral at
\(\sqrt z\), and take \(A\ge4\). The estimate follows at fixed
modulus five from Corollary 1.4 of
[Thorner and Zaman](https://arxiv.org/pdf/2108.10878v2).
Writing \(b=1-\sigma=1/2+t_0/\ell\) and integrating by parts twice,
\[
 \int_2^z\frac{u^{-\sigma}}{\log u}\,du
 =\frac{z^b}{b\ell}\left(1+\frac1{b\ell}+O(\ell^{-2})\right)
 =\frac{L}{\ell}\left(1-\frac{2\delta_*}{\ell}
                                      +O(\ell^{-2})\right).
\]
The last equality uses \(z^b=3\sqrt z\) and \(6\sqrt z=L\).
Thus \(A(N)\ll\sqrt N\exp[-\delta_*\log N/\log z_N]\) eventually.
In fact the logarithm of the Rankin upper bound contains the
additional saving \(-(2\delta_*+o(1))L/\ell^2\).

For large \(N\), \((\log N)/\log z_N\) increases. Squaring the
pointwise bound and summing with the specified weights gives
\[
 \|A\|_{I(Y)}^2\ll \log Y
             \exp\left(-2\delta_*\frac{\log Y}{\log z_Y}\right)
 \ll \exp\left(-\delta_*\frac{\log Y}{\log\log Y}\right).         \tag{4}
\]
The second inequality uses
\(2/\log z_Y\ge 1/\log\log Y+\log(36)/(2(\log\log Y)^2)\) for
large \(Y\). The extra exponential absorbs the harmonic sum.
The absolute bound applies to any subfamily of the smooth supports.

Since the deletions are disjoint after restricting the smooth
block to \(d>N^{1/4}\), (3) and (4) give
\[
 \begin{split}
 \|M-R\|_{I(Y)}^2
   &\ll Y^{-1/8}+
      \exp\left(-\delta_*\frac{\log Y}{\log\log Y}\right),\\
 \big|\sqrt{Q_R(Y)}-\sqrt{Q_M(Y)}\big|
   &\le\|M-R\|_{I(Y)} .
 \end{split}                                                   \tag{5}
\]
The last line follows from the pointwise Lipschitz inequality for
the positive part. Both comparisons hold on each same exact
window. They apply after taking the complete signed sum.

For a separate cutoff extension, take \(R^{(1/3)}(N)\) with the
same smooth threshold and \(d>N^{1/3}\). Equations (3) and (4) give
\(\|M-R^{(1/3)}\|_{I(Y)}\ll\sqrt{\log Y}\).
The subpower window criterion is therefore unchanged if one uses
this separate cutoff. For a prescribed \(r\), apply the source
condition at \(2r\) and absorb the \(O(\sqrt{\log Y})\) error
in \(Y^{1/(2r)}\) after taking the square root of the energy.
The fixed \(R\) still has cutoff \(N^{1/4}\).

## 4. Bounds for the complete positive energy

**Candidate-D from classical inputs.** Put
\(\Phi(x)=(\log x)^{3/5}(\log\log x)^{-1/5}\) and \(X=Y^{3/2}\).
An admissible classical Vinogradov–Korobov bound is
\(|M(x)|\le Cx e^{-c\Phi(x)}\) for all sufficiently large \(x\).
For example, Theorem 1.2 of
[Lee and Leong](https://arxiv.org/html/2208.06141v4) supplies
\(C=70179/12500\), \(c=319/100000\) when \(x\ge \exp(100000)\).
For any such pair,
\[
 Q_R(Y)\le (C^2+o(1))X e^{-2c\Phi(X)}.                        \tag{6}
\]
In fact \(Q_M(Y)\le C^2\sum_{N\in I(Y)}e^{-2c\Phi(N)}\).
The logarithmic derivative \(d\Phi(x)/d\log x\) tends to zero.
For each fixed \(v\in(0,1]\) this gives
\(e^{-2c\Phi(vX)}/e^{-2c\Phi(X)}\to1\). For \(Y\le x\le X\)
the same derivative bounds the ratio by \((X/x)^{1/2}\) for
all sufficiently large \(Y\). On \(v\ge\eta>0\) convergence
is uniform, and the normalized sum on \(v<\eta\) is bounded by
\(O(\sqrt\eta)\). Hence the upper sum is
\((1+o(1))X e^{-2c\Phi(X)}\), with \(Y/X\to0\). Its scale tends
to infinity, so the vanishing norm error in (5) gives (6).

**Candidate-D conditional on RH.** If RH is supplied as an external
input, the classical estimate \(|M(x)|\le C_\epsilon x^{1/2+\epsilon}\)
holds for every \(\epsilon>0\). See Theorem 1.3 of
[Fujisawa and Minamide](https://arxiv.org/pdf/1212.4348) for the
rational field. Then (5) and summation of \(N^{-1+2\epsilon}\)
give
\[
 Q_R(Y)\le
   \left(\frac{C_\epsilon^2}{2\epsilon}+o(1)\right)Y^{3\epsilon}.
\]
Taking \(\epsilon=1/(6r)\) gives \(Q_R(Y)^r\le Y\) on every
sufficiently late window for that \(r\). This route uses RH and
gives no independent estimate at that scale.

**O.** The unconditional estimate (6) permits energy of size
\(Y^{3/2-o(1)}\) and supplies no arbitrarily late subpower
windows. The unconditional improvement (5) controls the
discarded energy. A subpower bound still requires signed
control of the complete retained pairing, before taking its
positive part. Issue [#2087](https://github.com/mathorn1973/twist-j/issues/2087)
and [#2089](https://github.com/mathorn1973/twist-j/issues/2089)
retain their periodic statistic, Fourier and determinant work,
with their own kernel and cutoffs.
