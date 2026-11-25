# Cube-root prime correction and the loss in lower-argument estimates

**NON-CANONICAL. No authority. Candidate-D, paper deduction.** Same-session continuation of C-RH-ARITHMETIC-KERNEL-N, owner issue 2087 and draft PR 2089. The full signed square-root-scale bound remains **O**.

Put \(D=4X\), \(z=D^{1/3}\), \(L=\log X\), and use the frozen dyadic taper \(w\). It is one on \([X,2X)\), supported in \([7X/8,17X/8]\), and takes values in \([0,1]\). All primes in the sums below are split modulo five. For a sequence \(F\) on nonnegative integers with \(F(0)=0\), extend it by \(F(u)=F(\lfloor u\rfloor)\) for \(u\ge0\) and define

\[
 \mathcal C_z[F](n)=-2\sum_{z<p\le n}F(n/p)
                 -4\sum_{z<p\le q,\;pq\le n}F(n/(pq)).
\]

The actual correction is \(C_z=\mathcal C_z[T]\) by the round 6 cube-root transfer.

## 1. Exact pushforward and signed quadratic expression

For integers \(n,m\ge1\), let \(W_{nm}\) be twice the count of primes in \((n/(m+1),n/m]\) above \(z\), plus four times the count of unordered pairs \(z<p\le q\) with product in that same half-open interval. Thus \(W_{nm}\ge0\), the pairs with \(p=q\) enter at weight four, and \(\mathcal C_z[F](n)=-\sum_mW_{nm}F(m)\). Define the real quantities

\[
 b_m=\sum_n w(n)G_{\rm core}(n)W_{nm},\qquad
 K_{mj}=\sum_n w(n)W_{nm}W_{nj}.
\]

All sums are finite. The frozen symmetry in the frequencies makes \(G_{\rm core}\) real. The exact signed criterion from round 6 is

\[
 Q_{\rm core}=P_{\rm core}-2\sum_m b_m T(m)
                  +\sum_{m,j}K_{mj}T(m)T(j).                    \tag{1}
\]

The entries of \(K\) are nonnegative and \(K\) is positive semidefinite. The vector \(b\) retains the time correlation with the actual core. Positivity of \(K\) supplies no sign for that linear functional.

## 2. A uniform integral for the combined prime kernel

For \(n\) in the taper support put \(\ell=\log n\), \(a=\log z/\ell\), \(b(u)=1-\log u/\ell\), and let \(\Delta F(m)=F(m)-F(m-1)\). For any fixed \(A>0\) the prime number theorem in the two split residue classes gives

\[
\begin{aligned}
 \mathcal C_z[F](n)
   ={}&-\frac{n}{\ell}\int_1^{n/z}\frac{F(u)}{u^2b(u)}\,du
       -\frac{n}{\ell}\int_1^{n/z^2}\frac{F(u)}{u^2}
                                  g_a(b(u))\,du
       -2\sum_{z<p,\,p^2\le n}F(n/p^2)\\
     &+O_A\!\left(X L^{1-A}
               \sum_{m\le n/z}\frac{|\Delta F(m)|}{m}\right),\\
 g_a(b)={}&\frac1b\log\frac{b-a}{a}.                            \tag{2}
\end{aligned}
\]

To derive (2), write \(\Pi(y)=\operatorname{Li}(y)/2+E(y)\), with \(E(y)\ll_A y/(\log y)^A\). Insert \(F(u)=\sum_{m\le u}\Delta F(m)\) in the finite prime sums. Each single-prime count is \(\Pi(n/m)-\Pi(z)\). For the ordered pair count with product at most \(y=n/m\), first approximate the inner count \(\Pi(y/p)-\Pi(z)\), then approximate the outer prime sum by Stieltjes partial summation. Both prime arguments in every nonempty range are at least \(z\). The inner total error is \(O_A(yL^{1-A})\) using \(\sum_{p\le y}1/p\le 1+\log y\). In the outer sum the main inner term is proportional to \(f_y(t)=\operatorname{Li}(y/t)-\operatorname{Li}(z)\). At the upper boundary \(f_y(y/z)=0\), at the lower boundary \(|f_y(z)|\ll y/(zL)\), and \(|f_y'(t)|\ll y/(t^2 L)\) on \([z,y/z]\). The outer error is \(O_A(yL^{-A})\). This controls cumulative endpoint errors even for a short range. Summing them against \(|\Delta F(m)|\) gives the error in (2).

The ordered main measure is \(dt\,dv/(4\log t\log v)\) with \(t,v>z\) and \(tv\le n\). Minus four times the unordered sum equals minus twice the ordered sum minus twice its diagonal. This yields the explicit diagonal in (2). For the ordered integral set \(u=n/(tv)\) and \(s=\log t/\ell\). The inner integral in \(s\) is

\[
 \int_a^{b(u)-a}\frac{ds}{s(b(u)-s)}
       =\frac{2}{b(u)}\log\frac{b(u)-a}{a}.
\]

The factor two combines with the coefficient minus two and the split density squared to give the second term of (2). The single-prime integral follows from \(u=n/t\). No comparison of individual prime-count bins with a relative asymptotic is made.

## 3. Actual opposite drifts at the cube-root cutoff

Write \(G_T(s)=\int_1^\infty T(u)u^{-s-1}\,du=1/(s\zeta(s)U(s))\) for \(\Re s>1\), and \(\kappa=G_T'(1)=1/U(1)>0\). The inherited unconditional estimate \(|T(u)|\ll u\exp(-c\sqrt{\log u})\) makes all absolute logarithmic moments of \(T(u)/u^2\) finite. It implies

\[
 \int_1^\infty T(u)\frac{du}{u^2}=0,\qquad
 \int_1^\infty T(u)\frac{\log u}{u^2}\,du=-\kappa.
\]

Both cutoffs in (2) grow as fixed powers of \(X\) uniformly on the taper. Replacing either truncated moment by the full moment costs less than any fixed inverse logarithmic order. Use \(|\Delta T(m)|\le1\) for the count error and \(|T(n/p^2)|\le n/p^2\) for the explicit diagonal. The diagonal then contributes \(O(X/z)\). The derivatives of \(1/b\) and \(g_a(b)\) are uniformly bounded to any fixed order on their respective intervals \(a\le b\le 1\) and \(2a\le b\le1\). With

\[
 h_a(b)=\frac1b+g_a(b),\qquad
 h_a'(1)=\frac{a}{1-a}-\log\frac{1-a}{a},
\]

the first two Taylor terms in (2) give, uniformly on the taper,

\[
 C_z(n)=-\kappa h_a'(1)\frac{n}{\ell^2}+O(X/L^3)
       =c_*\frac{n}{\ell^2}+O(X/L^3),\qquad
 c_*=\kappa(\log 2-1/2)>0.                                      \tag{3}
\]

Indeed \(a=1/3+O(1/L)\) and \(\log 2=\int_1^2 dt/t>1/2\). Applying the same Taylor argument to any fixed number of terms gives

\[
 C_z(n)=-n\sum_{j=0}^{B-1}
       \frac{h_a^{(j)}(1)G_T^{(j)}(1)}{j!\ell^{j+1}}
       +O_B(X/L^{B+1})                                         \tag{4}
\]

for any fixed positive integer \(B\). The actual value of \(a\) is used in (4).

Put \(M_X=\sum_n w(n)n^2/(\log n)^4\asymp X^3/L^4\). The inherited estimates are

\[
 \|G_{\rm core}+C_z-T\|_w\ll_\varepsilon X^{1+\varepsilon},
 \qquad
 P_{\rm core}=\|G_{\rm core}\|_w^2+O_\varepsilon(X^{2+\varepsilon}).
\]

Since \(T(n)\ll_B X/L^B\) for every fixed \(B\), equations (3) and these estimates yield

\[
\begin{aligned}
 P_{\rm core} &= c_*^2 M_X+O(X^3/L^5),\\
 2\operatorname{Re}\langle G_{\rm core},C_z\rangle_w
              &= -2c_*^2 M_X+O(X^3/L^5),\\
 \|C_z\|_w^2 &= c_*^2 M_X+O(X^3/L^5).                          \tag{5}
\end{aligned}
\]

The three leading coefficients are unchanged if the core is further restricted to heights \(h\le L^{14}\) while leaving \(C_z\) exact. Indeed the uniform conductor-mask estimate of round 6, MARKED-PRIME-CANCELLATION §3, bounds the omitted core norm by \(O(X^{3/2}/L^4)\). Its effect on each affected term in (5) is \(O(X^3/L^6)\) by Cauchy–Schwarz and the same determinant comparison applied to the restricted core. For the full core, the exact difference \(G_{\rm core}+C_z\) has norm \(O_B(X^{3/2}/L^B)\) for every fixed \(B\). Consequently the first two lines of (5) can also be written as \(\|C_z\|_w^2+O_B(X^3/L^B)\) and \(-2\|C_z\|_w^2+O_B(X^3/L^B)\), respectively. This is a signed cancellation through every fixed logarithmic order. The stated estimates do not provide a power saving.

## 4. A power loss even with finitely many exact moment cancellations

Fix a nonnegative integer \(k\). Choose a fixed \(\delta\) in \((0,1/3)\) with \(h_{1/3}^{(k)}(1-\delta)\ne0\), or choose any fixed \(1/3\le\delta<2/3\). The first set of choices meets every open subinterval of \((0,1/3)\). For all sufficiently late dyadic \(X\), an integer sequence \(F_X\) supported in \([M,B_kM]\) for a fixed constant \(B_k\), \(M=\lfloor X^\delta\rfloor\), then satisfies

\[
 |F_X(m)|\le\sqrt m,\qquad
 |\Delta F_X(m)|\le 1,\qquad
 \sum_{m\ge1}\frac{|F_X(m)|^2}{m(m+1)}\ll_k1,
\]

and its exact moments \(\int_1^\infty F_X(u)(\log u)^j\,du/u^2\) vanish for \(0\le j<k\). Yet

\[
 \|\mathcal C_z[F_X]\|_w^2\asymp_{k,\delta}
                          \frac{X^{3-\delta}}{L^{2k+2}}.         \tag{6}
\]

In particular the claimed gain from replacing \(n\) by smaller arguments cannot follow from input square-root bounds and any fixed number of these moment cancellations alone.

For the construction choose \(k\) fixed integers \(r_i\ge2\) such that all products formed by taking one factor from each triple
\[
 \{r_i,\ r_i+1,\ r_i(r_i+1)\}
\]
are distinct. Choose them successively. At every step a collision among the new products would equate a ratio of two distinct new factors with one of finitely many fixed ratios of previous products. Each of the six possible new ratios is a nonconstant rational function of \(r_i\), so only finitely many integers are excluded. For the \(i\)-th triple put \(\epsilon_i(r_i)=-1\) and give its other two factors sign \(+1\). Choose a fixed \(\eta>0\) small enough that the intervals \([d,(1+\eta)d]\) for the distinct product values \(d\) are disjoint with positive gaps. Set \(B_k=(1+\eta)\max d\). For \(k=0\) the empty product is one.

Let \(A_M=M+\lfloor\eta M\rfloor\), \(q=\lfloor\sqrt M\rfloor\), and set
\[
 B_M(m)=\max(0,\min(q,m-M,A_M-m)),\qquad
 (\mathcal D_d F)(u)=F(u/d),\qquad
 F_X=\prod_{i=1}^k
       (\mathcal D_{r_i+1}+\mathcal D_{r_i(r_i+1)}-\mathcal D_{r_i})B_M .
\]
Dilations by integers preserve the integer-step extension. In the operator expansion each term is one signed dilate of the integer ramp \(B_M\), and the support intervals \([dM,(1+\eta)dM]\) have gaps exceeding one for large \(M\). This gives the stated amplitude and step bounds, with \(\Delta F_X(m)\in\{-1,0,1\}\). The total variation is \(O_k(\sqrt M)\). The weighted energy bound follows from the support and \(|F_X(m)|^2\le m\), since the ratio of largest to smallest supported index is bounded in terms of \(k\).

Under \(u=dv\), the measure \(du/u^2\) contributes a factor \(1/d\) and \(\log(u/M)=\log(v/M)+\log d\). Let \(J_j=\int_1^\infty F_X(u)(\log(u/M))^j\,du/u^2\). At each \(i\), the identity
\[
 \sum_{d_i}\frac{\epsilon_i(d_i)}{d_i}
 =-\frac1{r_i}+\frac1{r_i+1}+\frac1{r_i(r_i+1)}=0
\]
shows that a term in the multinomial expansion of the \(j\)-th moment vanishes unless it contains a positive power of \(\log d_i\) for every \(i\). It follows that \(J_j=0\) for \(j<k\) and
\[
 J_k=k!\left(\prod_{i=1}^k
             \sum_{d_i}\frac{\epsilon_i(d_i)\log d_i}{d_i}\right)
           \int_1^\infty B_M(v)\frac{dv}{v^2}
       \asymp_k M^{-1/2}.
\]
Each factor is positive because both positively weighted logarithms exceed \(\log r_i\) and the two positive weights add to \(1/r_i\). The ramp has height \(q\) on the middle half of \([M,A_M]\) for large \(M\), which proves the lower bound on its moment. The vanishing centered moments imply the uncentered form by binomial expansion.

For large \(X\) with \(\delta<1/3\), the entire support lies below \(n/z^2\) throughout the taper. The two integrals in (2) there combine into a single one with \(H_a=h_a\). If \(1/3\le\delta<2/3\), the entire support lies above \(n/z^2\) and below \(n/z\) throughout the taper. At \(\delta=1/3\) we have \(n/z^2\le (17/(8\cdot4^{2/3}))X^{1/3}<M\) for large \(X\) since \(17/8<4^{2/3}\). The upper bound follows from \(B_k X^\delta=o(X^{2/3})\) and \(n/z\gg X^{2/3}\) uniformly. In this range only the first integral occurs, with \(H_a(b)=1/b\). Taylor expand \(H_a\) around \(b_M=1-\log M/\ell\). On the support of \(F_X\), \(|\log(u/M)|\le\log B_k\). All Taylor terms below order \(k\) vanish. Also \(\sum_m|\Delta F_X(m)|/m\ll_k M^{-1/2}\), and the diagonal has absolute value \(O(\sqrt X)\) because

\[
 \sum_{z<p,\,p^2\le n}|F_X(n/p^2)|\le \sqrt n\sum_{z<p\le\sqrt n}p^{-1}
 \ll \sqrt X.
\]

The reciprocal prime sum is bounded by partial summation and \(\Pi(t)\ll t/\log t\) for \(z\le t\le D\). For fixed \(\delta<2/3\), \(\sqrt X\) is smaller than \(XM^{-1/2}L^{-k-2}\) for large \(X\). Taking \(A\) sufficiently large in (2), we obtain uniformly in \(n\)

\[
 \mathcal C_z[F_X](n)
    =-\frac{(-1)^k n}{k!\ell^{k+1}}H_a^{(k)}(b_M)J_k
          +O_k(XM^{-1/2}L^{-k-2}).                              \tag{7}
\]

The analytic function \(h_{1/3}\) on \((1/3,\infty)\) is nonpolynomial because it has a logarithmic singularity as \(b\) decreases to \(1/3\). None of its derivatives is identically zero. Its isolated derivative zeros are therefore the only excluded values of \(1-\delta\) for \(\delta<1/3\). For \(\delta\ge1/3\), the limiting derivative of \(1/b\) at \(1-\delta\) is nonzero. In both ranges \(H_a^{(k)}(b_M)\) converges to the chosen nonzero value uniformly in \(n\). This proves (6) since the taper is one on a block of length \(X\).

For every fixed \(0<\delta<2/3\), the power obstruction still holds when at least \(k\) moments are required to vanish. At a derivative zero below \(1/3\), choose a finite \(j>k\) with \(h_{1/3}^{(j)}(1-\delta)\ne0\). Such a derivative exists because the analytic function is not a polynomial. Use the construction with \(j\) triples. It keeps all the first \(k\) moments zero and gives squared norm of order \(X^{3-\delta}/L^{2j+2}\). Here \(j\) and the support constant may depend on \(k,\delta\). No uniform assertion for a moving \(\delta\) is made.

The loss in (6) has the same power in \(X\) as the elementary upper bound on such inputs. For any sequence with \(|F(m)|\le\sqrt m\) supported at \(m\ge M\), set \(Y=n/M\). Its one-prime sum is bounded in magnitude by \(\sqrt n\sum_{z<p\le Y}p^{-1/2}\ll X/(\sqrt M L)\). If the sum is nonempty, \(Y\ge z\) and partial summation of \(\Pi(t)\ll t/\log t\) gives \(\sum_{p\le Y}p^{-1/2}\ll\sqrt Y/\log Y\). For the pair sum use the ordered count as a majorant, sum first over \(z<q\le Y/p\), and then use \(\sum_{z<p\le D}1/p\ll1\). This gives \(X/(\sqrt M L)\) again, including the diagonal. The resulting squared norm is \(O(X^3/(ML^2))\), which agrees with the power of \(X\) in (6). Under the stated generic norms, a correction depending only on the first \(k\) moments cannot repair the loss uniformly. The zero input and \(F_X\) have the same moments and their outputs differ by (6). The probes satisfy integer and unit-step constraints. Their coefficients do not encode the multiplicative identities of \(T\).

## Scope and inputs

The exact identity (1) keeps the mixed term. Equation (5) determines its actual leading sign and size at the cube-root cutoff. Equation (6) rules out a class of induction estimates for the isolated prime operator. An argument coupling the actual core to the arithmetic of the smaller coefficients remains possible. The missing estimate is \((Q_{\rm core})_+\ll_\varepsilon X^{2+\varepsilon}\) for all \(\varepsilon>0\).

- Round 6, CUBE-ROOT-TRANSFER §§2–3 and MARKED-PRIME-CANCELLATION §3, for the exact correction, the norm comparison to the core and the height bound.
- FOUNDATION §2 and round 3, LARGE-PRIME-TAIL §2, for \(T\), its Mellin germ and the unconditional pointwise estimate. Round 4, LARGE-PRIME-HIERARCHY §§2–3, gives the prime-pair integral and profile for fixed power cutoffs. Section 2 above uses that approach uniformly on a dyadic taper up to the cube-root limit.
- Yamada, [Explicit formulae for primes in arithmetic progressions, I, Section 1](https://arxiv.org/html/1306.5322v4#S1). The classical error cited in the introduction gives (2) at fixed modulus five after partial summation and removal of prime powers.
