# What the five-cell identity controls

**NON-CANONICAL. No authority.** Internal paper opposition on the existing
C-RH-SEMISTABLE-FRAME-N line. All deductions below have status **candidate-D**
in their stated scope. Statements identified as **T** are imports with their
existing scope. The twisted Möbius estimate and the R17 multiplicity bound
remain **O**. No scientific computation or external independent confirmation.

## One polynomial on three different domains

Set \(P(X)=(1-X)(1-X^2)\), \(j=e^{2\pi i/5}\), \(J=1+j^2\),
\(\phi=-j^2-j^3\), and \(h=J\overline J=\phi^{-2}\). Write \(\chi=\chi_5\)
for the primitive real quadratic character, extended by zero at multiples of five.

The five symbols of the group ring give legitimate register coordinates.
They do not give a basis of the cyclotomic field: the relation
\(1+j+j^2+j^3+j^4=0\) cuts its rational dimension to four. Evaluation at
\(j\) quotients the integral register by the span of the all-ones element.
The rational augmentation space identifies with that quotient. Over the
integers the map from the augmentation lattice has image \((1-j)\mathbb Z[j]\),
so this rational identification cannot erase the integral index five.

1. At the selected complex embedding,
   \(jP(j)=j+j^{-1}-j^2-j^{-2}=2\phi-1=\sqrt5\).
   Since \(J\phi=j\), this also equals \(j/J+J/j\).
   On the embedding \(j\mapsto j^a\), the same polynomial has value
   \(\chi(a)\sqrt5\).
2. On the full marked register put \(g e_k=e_{k+1}\) cyclically,
   \(N=\mathbf1\mathbf1^T\), \(M_J=I+g^2\), and \(G=gP(g)\).
   Then \(G\mathbf1=0\), \(G^2=5I-N\), and
   \(G=3I-2M_J^TM_J+N\). The last identity follows by multiplication
   and \(N=I+g+g^2+g^3+g^4\). Fourier diagonalization proves the square
   identity and gives eigenvalues \(0,\sqrt5,\sqrt5,-\sqrt5,-\sqrt5\)
   as a multiset. On the augmentation space \(\ker \mathbf1^T\), the term
   \(N\) vanishes. Scalar \(+\sqrt5\) specifies just one of its two sectors.
   The Canon mixer named \(A\) is \(gG=g^2P(g)\). This shift explains the
   different polynomials under the same letter. [Existing polar-orbit claim, T](../../../canon/CANON.md#j-plenum-polar-orbit-separation-t).
3. On the open real interval \(0<z<1\), the periodic coefficient series is
   \[
   K(z)=\sum_{n\ge1}\chi(n)z^n=\frac{zP(z)}{1-z^5}>0.
   \]
   Here the factorization gives positivity at every such real argument.
   It gives an analytic consequence distinct from evaluating \(P\) at the roots of unity.

For \(\Re s>1\), Mellin integration term by term gives
\[
 \Gamma(s)L(s,\chi)=\int_0^\infty t^{s-1}K(e^{-t})\,dt .
\]
At zero the kernel is asymptotic to \(2t/5\) and at infinity to \(e^{-t}\).
Consequently the integral is holomorphic for \(\Re s>-1\) and extends the
identity there, with the removable value at zero understood by continuation.
It is positive on the real interval \((-1,\infty)\). Thus \(L(s,\chi)>0\)
on the positive real axis, including the central value, and \(L(s,\chi)<0\)
for \(-1<s<0\). For nonreal \(s\), the factor \(t^{i\Im s}\) has varying
phase. Integral positivity gives no corresponding complex zero exclusion.

**Candidate-D, alternate derivation of an existing special value.** At one,
put \(z=e^{-t}\). The integral becomes
\[
 L(1,\chi)=\int_0^1 \frac{1-z^2}{1+z+z^2+z^3+z^4}\,dz.
\]
Let \(Q_+(z)=z^2+\phi z+1\), \(Q_-(z)=z^2+(1-\phi)z+1\).
Their product is the denominator. Direct differentiation gives
\((\log(Q_+/Q_-))'=\sqrt5(1-z^2)/(Q_+Q_-)\).
The ratios at zero and one are respectively \(1\) and \(\phi^2\), so
\[
 L(1,\chi)=2\log(\phi)/\sqrt5=-\log(h)/\sqrt5.
\]
Canon already evaluates this value by the finite Fourier and log-sine route.
With \(\Lambda(s)=(5/\pi)^{s/2}\Gamma(s/2)L(s,\chi)=\Lambda(1-s)\),
its values at zero and one give \(2L'(0,\chi)=\sqrt5 L(1,\chi)\).
In particular \(L'(0,\chi)=\log\phi\).
[Prior special-value calculation](../../../canon/CANON.md#cm5-reachable-primitive-density-t) ·
[Primitive functional equation](https://dlmf.nist.gov/25.15.E5).

## Frobenius and the Fourier statement

For every prime \(p\ne5\), cyclotomic arithmetic Frobenius sends \(j\)
to \(j^p\). Its restriction to the real quadratic subfield sends \(h\)
to \(h^{\chi(p)}\). In residue classes \(1,4,2,3\) modulo five the full
orders are respectively \(1,2,4,4\). The primes in class four fix \(h\)
and conjugate \(j\). The prime five is ramified. The projective fixed-line
description of \(\chi\) already has an exact public scope.
[Ideal-count and rational Möbius descent, T](../../../canon/CANON.md#ideal-count-rational-descent-and-exact-mertens-two-sum).

For \(p\ne5\), reduce the roots \(\alpha=\phi\), \(\beta=1-\phi\)
of \(X^2-X-1\) in a splitting field over \(\mathbb F_p\). They are distinct
and nonzero, including in characteristic two. Then
\(p\mid F_n\) exactly when \((\beta/\alpha)^n=1\).
The least positive such index is \(\operatorname{ord}(-h)\). Frobenius either
fixes or interchanges the roots, so this rank divides \(p-\chi(p)\).
The full Fibonacci pair must return both eigenvalues to one, a stronger
condition. For instance modulo three the roots have norm \(-1\), whence
both fourth powers are \(-1\) and the pair cannot already have returned at four.

The Fourier sum \(\sum_a\chi(a)j^{ak}\) is zero for \(5\mid k\) and equals
\(\chi(k)\sqrt5\) otherwise by changing variable. The normalized Fourier
transform therefore fixes \(\chi\). The sign in the exponent is immaterial
here since \(\chi(-1)=1\). Lifting the finite identity to the completed
Dirichlet functional equation uses an analytic theorem, for example Poisson
summation of the character theta series followed by Mellin transformation.
The resulting reflection preserves off-line pairs of zeros as well.

## Oppose the change of weight

The partial sum \(S(y)=\sum_{n\le y}\chi(n)\) takes the values
\(0,1,0,-1,0\) indexed by \(\lfloor y\rfloor\bmod5=0,1,2,3,4\).
For \(B(x)=\sum_{n\le x}\mu^2(n)\chi(n)\), square-divisor inversion gives
\[
 B(x)=\sum_{d\le\sqrt{x},\,5\nmid d}\mu(d)S(x/d^2),
 \qquad |B(x)|\le\lfloor\sqrt{x}\rfloor .
\]
[Development](DEVELOPMENT.md) also gives the refinement \(B(x)=o(\sqrt{x})\)
using the ordinary prime number theorem. If a squarefree \(n\) coprime to
five has \(u\) split and \(v\) inert prime factors, then \(\chi(n)=(-1)^v\)
and \(\mu(n)\chi(n)=(-1)^u\). The bound just proved balances the parity
of the second count. The research target balances the parity of the first.

For \(\Re s>1\) the Euler factors distinguish the two sums exactly:
\[
 \sum_n\frac{\mu^2(n)\chi(n)}{n^s}
 =\frac{L(s,\chi)}{(1-5^{-2s})\zeta(2s)},\qquad
 \sum_n\frac{\mu(n)\chi(n)}{n^s}=\frac1{L(s,\chi)}.
\]
The denominator factor at five in the first quotient is required. At a
prime \(p\ne5\) the respective local polynomials are \(1+\chi(p)p^{-s}\)
and \(1-\chi(p)p^{-s}\). Absolute coefficient bounds apply equally to both
but discard their signs. A common support and the density of split primes
do not provide a bound on the signed parity sum.

**Candidate-D, classical fixed-character equivalence.** The estimate
\(M_\chi(x)=\sum_{n\le x}\mu(n)\chi(n)
=O_\epsilon(x^{1/2+\epsilon})\) for every \(\epsilon>0\) makes
\(H(s)=s\int_1^\infty M_\chi(x)x^{-s-1}\,dx\) holomorphic on
\(\Re s>1/2\). There \(H(s)L(s,\chi)=1\) by continuation from the region
of absolute convergence. Reflection then gives the critical line for every
nontrivial zero of this one primitive real Dirichlet function. Conversely its
own RH gives \(1/L(\sigma+it,\chi)\ll_{\delta,\eta}(1+|t|)^\eta\)
for every \(\delta,\eta>0\), uniformly for \(\sigma\ge1/2+\delta\).
Perron inversion gives the stated summatory estimate. This reverse direction
uses a growth bound as well as zero-freeness. Neither implication needs
simple zeros, an endpoint \(O(\sqrt{x})\) bound, or a moving conductor.
[Fixed-character equivalence, Gao and Zhao, (1.2)](https://arxiv.org/html/2212.09241v2#S1.E2).

## The first derivative has a positive main term

**Candidate-D with the prime number theorem in arithmetic progressions.**
Use the registered [golden-ladder polynomial](../../../canon/CANON.md#rapidity-golden-ladder-t)
from [Development](DEVELOPMENT.md). Thus \(Q_x(z)\) sums
\((-1)^{v+\mathbf1_{5\mid n}} z^u\) over squarefree \(n\le x\), where \(u,v\)
count split and inert prime factors in the real quadratic field. The prime
five is counted separately. Put \(f(m)=Q_m(1)-Q_{m-1}(1)\) for positive
integers \(m\), with \(Q_0=0\), and \(F(y)=\sum_{m\le y}f(m)=Q_y(1)\).
The identity \(F(y)=B(y)-B(y/5)\) gives \(F(y)=O(\sqrt y)\) elementarily.
By partial summation the sum \(\sum_{m\ge1} f(m)/m\) converges. Taking the
real limit of its Euler product from \(\sigma>1\) identifies its value:
\[
 C=\lim_{\sigma\downarrow1}
 \frac{L(\sigma,\chi)}{(1+5^{-\sigma})\zeta(2\sigma)}
 =\frac{5L(1,\chi)}{6\zeta(2)}.
\]

Let \(b(p^k)=(-1)^{k-1}\) for split primes \(p\) and \(k\ge1\), and put
\(b(n)=0\) at all other integers. Differentiating the local split factor
\(1+zp^{-s}\) at \(z=1\) divides out that original factor and inserts
\(p^{-s}/(1+p^{-s})=\sum_{k\ge1}(-1)^{k-1}p^{-ks}\).
Absolute convergence for \(\Re s>1\), or formal comparison of coefficients,
therefore gives
\[
 Q'_x(1)=\sum_{mn\le x} f(m)b(n).
\]
For \(H(y)=\sum_{n\le y}b(n)\), the primes \(1,4\bmod5\) give
\(H(y)\sim y/(2\log y)\) by the prime number theorem in those progressions.
Proper prime powers contribute at most \(O(\sqrt y\log(2y))\) in absolute
value. The same argument gives \(H_*(y)=\sum_{n\le y}|b(n)|\ll y/\log(2y)\)
for \(y\ge1\). [Prime number theorem in progressions, Kedlaya, Theorem 4.12](https://kskedlaya.org/ant/chap-primes-in-ap.html).

Fix an integer \(K\ge1\). The portion \(m\le K\) is
\[
 \sum_{m\le K} f(m)H(x/m)=
 \frac{x}{2\log x}\sum_{m\le K}\frac{f(m)}m+o_K(x/\log x).
\]
On the remaining portion exchange the two sums. With \(Y=x/K\), its absolute
value is at most
\[
 \sum_{n\le Y}|b(n)|\,|F(x/n)-F(K)|
 \ll \sqrt{x}\sum_{n\le Y}|b(n)|/\sqrt{n}+\sqrt K\,H_*(Y)
 \ll \frac{x}{\sqrt K\log(2x/K)}.
\]
The last inequality follows by partial summation from
\(\sum_{n\le Y}|b(n)|/\sqrt n\ll\sqrt Y/\log(2Y)\); its constant is
independent of \(K\). For example, split the resulting integral of
\(u^{-1/2}/\log(2u)\) at \(\sqrt Y\) to get this bound.
First let \(x\to\infty\) with \(K\) fixed, then \(K\to\infty\). This proves
\[
 \boxed{\displaystyle Q'_x(1)\sim\frac C2\,\frac{x}{\log x}
 =\frac{\sqrt5\log\phi}{\pi^2}\,\frac{x}{\log x}.}
\]
In particular the derivative is eventually positive. For any fixed \(r>0\)
Cauchy's estimate bounds \(|Q'_x(1)|\) by
\(r^{-1}\max_{|z-1|=r}|Q_x(z)|\). The displayed main term excludes a
uniform \(O(x^\theta)\) bound on that circle for any fixed \(\theta<1\).
It leaves the value at \(z=-1\) open. This derivative concerns the registered
polynomial, with ordinary Mertens evaluation at \(-1\). The fixed-character
Möbius sum above is a separate arithmetic target.

## Test against the previous period obstruction

For the R17 abstract counterexample take \(I_5\otimes A_u\). A cyclic
shift, the five-cell Gauss operator, Fourier projections, clock multipliers
and every matrix they generate on the first factor preserve the word images.
For any subspace \(W\) of the second factor,
\((I_5\otimes A_u)^{-1}(\mathbb C^5\otimes W)
=\mathbb C^5\otimes A_u^{-1}(W)\). Both relevant dimensions and both
normalizations multiply by five, leaving the old positive excess unchanged.
This tests the proposed implication even after granting a full first-factor
matrix algebra. The source still needs bounds for all subspaces of its actual
multiplicity maps. A character on rational primes does not specify an
intertwiner on those maps. [R17, equations (17.10)-(17.11)](../round17/REPORT.md).
