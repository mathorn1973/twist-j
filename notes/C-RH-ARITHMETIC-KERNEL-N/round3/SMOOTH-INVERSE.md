# Smooth inverse, exact cancellation, and its terminal slice

C-RH-ARITHMETIC-KERNEL-N, #2087 / #2089. NON-CANONICAL, no authority. Candidate-D. Result-exposed paper investigation. No numerical audit. The fixed-power Dickman asymptotic is not used.

Let \(\mathcal P=\{p:\ p\equiv1,4\bmod5\}\), \(\chi=\chi_5\), and \(K_d(X)=\sum_{j\le X/d}\chi(j)\) for \(X\ge1\). The squarefree split weight is \(s(d)=(-2)^{\omega(d)}\), zero on other integers. Let \(T(X)=\sum_{d\le X}s(d)K_d(X)\). All summatory functions include their upper endpoints. Write \(D=X^{2/3}\); the large-support tail is \(R=T-\sum_{d\le D}s(d)K_d\).

## 1. The exact same-\(X\) identity

For a threshold \(z\), set \(s_{>z}(d)=s(d)\mathbf1_{P^-(d)>z}\) with \(P^-(1)=+\infty\), and let \(s_{\le z}\) be \(s\) restricted to integers whose prime factors are all at most \(z\), including 1. Their supports use disjoint prime sets and \(s=s_{\le z}*s_{>z}\) under Dirichlet convolution. Define the inverse \(g_z\) of \(s_{\le z}\) coefficientwise. At \(p\in\mathcal P\), \(p\le z\), the factor \(1-2t\) inverts to \((1-2t)^{-1}\); other factors equal one. Hence
\[
 g_z(e)=
 \begin{cases}
 2^{\Omega(e)}, &\text{all prime factors of } e \text{ belong to }\mathcal P \text{ and are }\le z,\\
 0, &\text{otherwise},
 \end{cases}
 \qquad g_z(1)=1 .
\]
Here \(\Omega\) counts prime factors with multiplicity. The identities apply separately at each \(X\) with the same frozen parameter \(z\) everywhere on the right. The parameter may vary with \(X\) between identities.

Write \(B_z^*(X)=\sum_{d\le X}s_{>z}(d)K_d(X)\) for the full rough sum and \(H_z^*(X)=T(X)-B_z^*(X)\). The exact equality \(s_{>z}=g_z*s\) and finite rearrangement give
\[
 \begin{split}
 B_z^*(X)&=T(X)+\sum_{1<e\le X}g_z(e)T(X/e),\\
 H_z^*(X)&=-\sum_{1<e\le X}g_z(e)T(X/e).
 \end{split}                                                    \tag{1}
\]
For the corresponding large-support pieces \(B_z(X)\) and \(H_z(X)\), subtract from the respective lines their short parts \(d\le D\). Thus every displayed common smaller-argument term cancels with its negative at the same \(X\). The original \(T(X)\) remains in (1). A bound for the two pieces separately needs a bound for the indicated signed smaller-argument sum, or it must keep those terms paired in the full statistic.

## 2. A uniform growing-threshold bound

Put \(L=\log X\), \(Z=\log z\), and \(u=L/Z\) for \(11\le z\le X\). There are fixed constants \(c,C>0\) such that
\[
 |B_z(X)|\le
 C X\log z\left(e^{-c\sqrt L}+e^{-c\min\{L,u\log u\}}\right)+X^{2/3}.
                                                               \tag{2}
\]
The same upper bound for the full \(B_z^*\) has no final \(X^{2/3}\) term.

First, the already established Dirichlet unit carries the classical unconditional Mertens estimate to \(|T(y)|\ll y e^{-c_0\sqrt{\log y}}\) for \(y\ge2\). Indeed, writing \(T(y)=\sum_{d\le y}v(d)M(y/d)\) for the inverse-unit coefficients, split at \(d=\sqrt y\). Absolute convergence at 1 bounds the first part using \(M(y/d)\ll (y/d)e^{-c_1\sqrt{\log y}}\), and convergence at \(3/4\) bounds the second by \(O(y^{7/8})\). Also \(|T(y)|\le y\), since the local coefficients of \(s*\chi\) have absolute value at most one. At split primes the coefficients at all positive powers are \(-1\), at inert primes they are \((-1)^k\) at power \(k\), and at 5 they vanish.

Write \(G_z(\sigma)=\sum_{m\ge1}g_z(m)/m^\sigma=\prod_{p\in\mathcal P,p\le z}(1-2p^{-\sigma})^{-1}\). The fixed-modulus PNT estimate \(\pi_{\mathcal P}(x)=\tfrac12\operatorname{Li}(x)+O(x/\log^2 x)\) and partial summation give
\[
 \sum_{\substack{p\in\mathcal P\\p\le z}}\frac1p
   =\tfrac12\log\log z+O(1),\qquad
 \sum_{\substack{p\in\mathcal P\\p\le z}}\frac{\log p}{p}
   \ll \log z .
\]
Expanding the logarithm of each factor therefore gives \(G_z(1)\asymp\log z\). The terms \(e\le\sqrt X\) in the full inverse formula of (1) are bounded by \(O(XG_z(1)e^{-c_2\sqrt L})\). For the other terms and \(0\le\eta\le1/4\),
\[
 \sum_{e>\sqrt X}\frac{g_z(e)}e
    \le X^{-\eta/2}G_z(1-\eta).
\]
The smallest split prime is 11, and \(2\cdot11^{-3/4}<1\), so the logarithm of every local factor is Lipschitz in \(p^{-\sigma}\) uniformly for \(\sigma\ge3/4\). The inequality \(p^\eta-1\le\eta\log(p)p^\eta\) then gives, with \(b=\eta Z\),
\[
 \log\frac{G_z(1-\eta)}{G_z(1)}
   \ll\sum_{p\in\mathcal P,p\le z}\frac{p^\eta-1}{p}
   \ll b e^b ,
\]
Choose \(b=\min(Z/4,(\log u)/2)\). Since \(e^b\le\sqrt u\), the combined exponent \(-ub/2+O(be^b)\) is at most \(-ub/4\) once \(u\) exceeds an absolute constant. Also \(ub=\min(L/4,u\log u/2)\). For bounded \(u\) use the bound \(G_z(1)\) and enlarge the absolute constant. This proves the stated bound for the full sum by \(|T(X/e)|\le X/e\). For the actual tail, the discarded short portion is at most \(\sum_{d\le D}|s(d)|\le D\), by the nonnegative majorant \(1*\chi\). This proves (2).

In particular, for \(z=(\log X)^A\), with any fixed \(A>0\), (2) gives \(B_z(X)\ll_A Xe^{-c_A\sqrt{\log X}}\). This is an unconditional growing-\(u\) estimate rather than an extrapolation of a fixed-\(u\) asymptotic. It remains a subexponential saving on \(X\).

## 3. Exact exponent of a positive terminal slice

Fix \(A>0\) and set \(z=(\log X)^A\). Put
\[
 P_z(X)=\sum_{X/2<e\le X}g_z(e)T(X/e)
       =\sum_{X/2<e\le X}g_z(e).
\]
The equality is exact since \(\lfloor X/e\rfloor=1\) and \(T(1)=1\). Let \(\kappa=\log 2/\log 11\), which is smaller than \(1/2\). Then
\[
 P_z(X)=X^{\,\max\{\kappa,\,1-1/A\}+o(1)}.                    \tag{3}
\]

For the upper bound take any fixed \(\sigma\) strictly between \(\max\{\kappa,1-1/A\}\) and 1. The Euler factors satisfy \(2p^{-\sigma}\le 2\cdot11^{-\sigma}<1\), and
\[
 \log G_z(\sigma)\ll_\sigma\sum_{m\le z}m^{-\sigma}
     \ll_\sigma z^{1-\sigma}=o(\log X).
\]
Rankin's bound gives \(P_z(X)\le X^\sigma G_z(\sigma)=X^{\sigma+o(1)}\). Taking \(\sigma\) arbitrarily close to the claimed exponent proves the upper limit in (3).

For the lower bound use a bounded padding operation. Given \(d\le X/11^5\), coprime to \(11\cdot19\), put \(r=\lfloor\log(X/d)/\log11\rfloor\ge5\). Set \(\lambda=19/11\), so \(1<\lambda<2\) and \(\lambda^5>11\), the last inequality following from \(\lambda>5/3\). Choose the largest \(s\in\{0,1,2,3,4\}\) with \(\lambda^s\le X/(d11^r)\). Since \(1\le X/(d11^r)<11<\lambda^5\), the padded integer \(e=d11^{r-s}19^s\) satisfies \(1\le X/e<\lambda\). Thus \(X/2<e\le X\). Discarding its factors 11 and 19 recovers \(d\), so the padding is injective. Eventually \(z\ge19\), and the operation preserves the condition that every prime factor is a split prime at most \(z\).

Take \(d=1\). The single padded integer contributes \(2^r=X^{\kappa+o(1)}\). For \(A>1\), put \(k=\lfloor\log(X/11^5)/\log z\rfloor\). Take all products of \(k\) distinct split primes in \((z/2,z]\). Eventually none equals 11 or 19, their product is at most \(X/11^5\), and the number \(m\) of available primes satisfies \(m\asymp z/\log z\). We have \(m/k\to\infty\) and
\[
 \log\binom{m}{k}\ge k\log(m/k)
     =(1-1/A+o(1))\log X.
\]
For the inequality use \((m-i)/(k-i)\ge m/k\) for \(0\le i<k\). The asymptotic follows from \(k\sim L/(A\log L)\) and \(\log(m/k)=(A-1)\log L+O_A(1)\). Each padded product has positive weight at least one. This proves the second lower exponent when \(A>1\). For \(0<A\le1\) the power padding alone gives the larger exponent. Together they prove (3).

For \(A>2\), the positive terminal slice by itself violates the subpower energy target on every sufficiently large quadratic window:
\[
 \sum_{Y\le n<Y^2}\frac{P_{(\log n)^A}(n)^2}{n(n+1)}
      =Y^{\,2-4/A+o(1)} .
\]
Insert (3) termwise. The lower estimate uses only \(Y^2/2\le n<Y^2\); the upper estimate follows by summing \(n^{-2/A+\varepsilon}\). This rules out discarding that slice in a separable positive-part estimate. It cancels with a negative slice in the second line of (1). A bound of the required strength for the signed rough-plus-mixed tail remains open.

## 4. Conditional transfer at the same threshold

Suppose, as a separate hypothesis, that for some \(1/2\le\theta\le1\) one has the global bound \(|T(y)|\ll_\varepsilon y^{\theta+\varepsilon}\) for every \(\varepsilon>0\). For \(z=(\log X)^A\), equation (1) then gives
\[
 |B_z^*(X)|+|H_z^*(X)|
   \ll_{A,\varepsilon}X^{\max\{\theta,1-1/A\}+\varepsilon}.
                                                               \tag{4}
\]
When \(\theta<1\), choose a fixed \(\sigma\) strictly between \(\max\{\theta,1-1/A\}\) and 1, arbitrarily close to that maximum. Both sums are bounded by a constant times \(X^\sigma G_z(\sigma)\), and the Dirichlet-series estimate in §3 gives \(G_z(\sigma)=X^{o(1)}\). When \(\theta=1\), use \(|T(y)|\le y\) and \(G_z(1)\ll\log z\). This proof uses a global premise for \(T\), since the arguments \(X/e\) have different sizes.

In particular, conditional on RH and the known coefficient-unit transfer to \(T\), equation (4) gives all-epsilon square-root bounds for the full rough and mixed sums when \(A\le2\). The companion moving-mask estimate then gives the separate positive-part window bounds for the corresponding sharp tails at those thresholds. Indeed the short corrections have square energy \(O((1+\log Y)^6)\), while the global two-sided power bounds give energy \(O_\varepsilon(Y^{4\varepsilon})\). For \(A>2\) the actual positive slice in §3 prevents any termwise absolute inverse estimate from giving an all-epsilon square-root bound. That obstruction is to the termwise route. The full signed sums may still have the required cancellation.

## Sources

- [Bennett, Martin, O’Bryant and Rechnitzer, Explicit bounds for primes in arithmetic progressions, Theorem 1.2 and Corollary 1.8](https://personal.math.ubc.ca/~bennett/BeMaObRe-IJM-2018.pdf), for the fixed-modulus prime estimates.
- [Lee and Leong, New explicit bounds for Mertens function and the reciprocal of the Riemann zeta-function, Theorem 1.1](https://arxiv.org/html/2208.06141v4#Thmtheorem1.1), for the unconditional \(M(y)\) bound.
- The candidate's FOUNDATION.md and GENERAL-ROUGH.md supply, respectively, the absolute-convergence Dirichlet unit and the earlier fixed-power calculation. Neither estimate in (2) or (3) uses asymptotic uniformity from GENERAL-ROUGH.md.
