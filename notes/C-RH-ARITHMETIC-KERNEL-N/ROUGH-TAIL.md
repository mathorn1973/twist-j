# A signed rough part of the large-support tail

C-RH-ARITHMETIC-KERNEL-N. NON-CANONICAL, no authority. Candidate-D proof. The prime number theorem modulo five and the classical unconditional Mertens estimate are imported. There is no historical priority claim.

Let \(\mathcal P\) be the split primes, \(\chi=\chi_5\), and \(S_\chi(t)=\sum_{j\le t}\chi(j)\), with values \(+1,-1,0\) on floor residues \(1,3,\{0,2,4\}\), respectively. Write \(w(d)=(-2)^{\omega(d)}\) when \(d\) is squarefree and split-supported, and zero otherwise. Set \(Z=X^{1/3}\), \(D=X^{2/3}=Z^2\) and
\[
 R(X)=\sum_{D<d\le X}w(d)S_\chi(X/d).
\]
The rough part \(B(X)\) restricts this sum to \(P^-(d)>Z\), where \(P^-(d)\) is the least prime divisor. Write \(H(X)=R(X)-B(X)\).

## Exact formulas

For real \(y\ge D\), put
\[
 \pi_{\mathcal P}(y)=\#\{p\in\mathcal P:p\le y\},\qquad
 N_2(y;Z)=\sum_{\substack{Z<p\le\sqrt y\\p\in\mathcal P}}
       \bigl[\pi_{\mathcal P}(y/p)-\pi_{\mathcal P}(p)\bigr].
\]
In the second formula the two prime factors are strictly ordered and distinct. If \(d\le X\) and all its primes exceed \(Z\), three such factors cannot occur. Two such factors have product strictly larger than \(D\). Thus
\[
 B(X)=\sum_{1\le j< Z}\chi(j)\left[
       -2\bigl(\pi_{\mathcal P}(X/j)-\pi_{\mathcal P}(D)\bigr)
       +4N_2(X/j;Z)\right].
 \tag{1}
\]
The outer cutoff gives \(j\le X/d<Z\), including when \(Z\) is integral.

For \(p\in\mathcal P\), define a single auxiliary sum
\[
 A_p(y)=\sum_{e\le y,\ P^-(e)>p}w(e),
 \qquad P^-(1)=+\infty .
\]
In the complementary part factor \(d=pe\) with \(p=P^-(d)\le Z\). This is a unique factorization in the summation because \(d\) is squarefree. It satisfies \(P^-(e)>p\) and \(w(pe)=-2w(e)\). Summing over the same quotients gives the exact least-prime recurrence
\[
 H(X)=-2\sum_{\substack{p\le Z\\p\in\mathcal P}}\ \
     \sum_{1\le j<Z}\chi(j)\bigl[A_p(X/(pj))-A_p(D/p)\bigr].
 \tag{2}
\]
For integers the cutoffs in these identities are comparisons of cubes or squares. No choice of orientation and no real-valued filter is involved.

## Asymptotic of the rough part

We prove
\[
 B(X)\sim -(1-\log 2)L(1,\chi)\frac{X}{\log X}.
 \tag{3}
\]
The prime number theorem in the two classes \(1,4\) modulo five gives
\(\pi_{\mathcal P}(u)\sim u/(2\log u)\), hence also the corresponding big-O bound. Put \(L=\log X\). For each fixed integer \(j\ge1\),
\[
  \frac{L}{X}\bigl(\pi_{\mathcal P}(X/j)-\pi_{\mathcal P}(D)\bigr)\longrightarrow\frac1{2j}.
\]

For the semiprime term put \(y=X/j\). The contribution of \(\pi_{\mathcal P}(p)\) in \(N_2\) is at most \(\pi_{\mathcal P}(\sqrt y)^2=O(X/L^2)\). Uniformly over \(Z<p\le\sqrt y\), \(y/p\ge\sqrt y\) tends to infinity for each fixed \(j\). Thus the other term is
\[
 \sum_{\substack{Z<p\le\sqrt y\\p\in\mathcal P}}
          \pi_{\mathcal P}(y/p)
 =\frac{X}{2jL}(1+o(1))
    \sum_{\substack{Z<p\le\sqrt{X/j}\\p\in\mathcal P}}
       \frac{1}{p(1-\log p/L)}.
\]
Indeed \(\log(y/p)=L(1-\log p/L)-\log j\) and \(1-\log p/L\ge1/2\). For any fixed \(0<a<b\), partial summation and the same prime number theorem give
\[
 \sum_{X^a<p\le X^b,\,p\in\mathcal P}\frac1p
     \longrightarrow \frac12\log(b/a).
\]
This proves convergence of the reciprocal-prime measures on compact subintervals in the exponent variable \(v=\log p/L>0\) to \(dv/(2v)\). This can be seen directly by upper and lower step-function approximations of any continuous test function. The upper endpoint \(\log(\sqrt{X/j})/L\) may be replaced by \(1/2\), since the reciprocal-prime mass between \(1/2-\delta\) and \(1/2\) has limit \(\tfrac12\log[(1/2)/(1/2-\delta)]\to0\). Consequently,
\[
 \frac{L}{X} N_2(X/j;Z)\longrightarrow \frac1{4j}
   \int_{1/3}^{1/2}\frac{dv}{v(1-v)}=\frac{\log 2}{4j}.
 \tag{4}
\]

To pass from a fixed finite set of \(j\) to (1), return to the original sum over \(d\). Replacing \(S_\chi(X/d)\) by \(\sum_{j\le\min(Q,X/d)}\chi(j)\) alters its value by at most two and only for \(d\le X/(Q+1)\). It suffices to count the rough \(d\) in \((D,y]\) for \(y\le X\), weighted by \(|w(d)|\). For \(y<D\) the count is zero. Otherwise \(\pi_{\mathcal P}(y)\ll y/L\). Also
\[
 N_2(y;Z)\le
   \sum_{\substack{Z<p\le\sqrt y\\p\in\mathcal P}}
      \pi_{\mathcal P}(y/p)
 \ll \frac{y}{L}\sum_{\substack{X^{1/3}<p\le X^{1/2}\\p\in\mathcal P}}\frac1p
 \ll \frac{y}{L},
\]
with constants independent of \(y\) and \(Q\), because \(y/p\ge\sqrt y\ge X^{1/3}\) and the reciprocal sum is bounded. Therefore the discarded signed quotient contribution is \(O(X/(Q\log X))\), uniformly. Equations (1) and (4) now give (3), by letting \(X\) tend to infinity with fixed \(Q\) and then letting \(Q\) tend to infinity. The character series \(\sum_{j\ge1}\chi(j)/j=L(1,\chi)\) converges by bounded partial sums. Its consecutive five-term blocks are positive, since \((5k+1)^{-1}-(5k+2)^{-1}>(5k+3)^{-1}-(5k+4)^{-1}\). Also \(\log 2<1\), so the constant \(c=(1-\log 2)L(1,\chi)\) is positive.

## The necessary same-argument cancellation

Let \(T(X)=\sum_{d\le X}w(d)S_\chi(X/d)\). The exact Dirichlet unit from the previous note gives \(T(X)=\sum_{d\le X}v(d)M(X/d)\) with \(\sum_d |v(d)|d^{-\sigma}<\infty\) for \(\sigma>1/2\). The standard unconditional estimate \(|M(u)|\ll u\exp(-c_1\sqrt{\log u})\) implies \(T(X)=o(X/\log X)\). For completeness, terms \(d\le\sqrt X\) are \(O(X\exp(-c_2\sqrt{\log X}))\), using absolute convergence at 1. Terms \(d>\sqrt X\) are \(O(X^{7/8})\), using \(|M(u)|\le u\) and absolute convergence at \(3/4\).

Due to the nonnegative coefficients of \(1*\chi\),
\[
  \sum_{d\le D}|w(d)|\le\sum_{n\le D}(1*\chi)(n)
   =\sum_{a\le D}S_\chi(D/a)\le D.
\]
The coefficientwise domination uses \((1*\chi)(d)=2^{\omega(d)}\) on squarefree split \(d\). Thus \(R(X)=T(X)+O(X^{2/3})=o(X/\log X)\). Together with (3) this gives
\[
 H(X)\sim c X/\log X,\qquad B(X)\sim -c X/\log X .
 \tag{5}
\]
In particular, if \(Q_H(Y)\) means the same rational positive-part square statistic used for \(T\), then every sufficiently large integer \(Y\) satisfies
\[
 Q_H(Y)=\sum_{n=Y}^{Y^2-1}\frac{H(n)_+^2}{n(n+1)}
      \gg \frac{Y^2}{(\log Y)^2}.
\]
Take only \(Y^2/2\le n<Y^2\). Each term contributes \(\gg1/(\log Y)^2\) by (5). In contrast the positive part of \(B\) vanishes on sufficiently late windows. Estimating the two positive parts separately therefore cannot establish the good-window condition for their sum. The exact signed target after this split is to prove sufficiently small positive energy for \(H(X)-[-B(X)]\) on arbitrarily late windows. The asymptotic centering in (5) is at scale \(X/\log X\), which leaves errors larger than the requested square-root scale.

## Sources

- [Bennett, Martin, O’Bryant and Rechnitzer, Explicit bounds for primes in arithmetic progressions](https://arxiv.org/abs/1802.00085), fixed-modulus prime number theorem and its stronger explicit estimates for the needed classes.
- [Lee and Leong, New explicit bounds for Mertens function and the reciprocal of the Riemann zeta-function, Theorem 1.1](https://arxiv.org/html/2208.06141v4#Thmtheorem1.1), classical-form unconditional Mertens estimate.
- [Window foundation](FOUNDATION.md), section 2 for the absolutely convergent coefficient unit.
