# The signed cubic unit term and a balanced readout of \(T\)

C-RH-ARITHMETIC-KERNEL-N, round 6, issue #2087 / draft #2089. NON-CANONICAL, no authority. Candidate-D, paper proof under [PREREG-BALANCED](PREREG-BALANCED.md). No scientific computation. We use the actual coefficient \(t=(s*\chi_5)=\mu*v\) and its Dirichlet unit from the pinned FOUNDATION and CRITICAL-UNIT. Neighbor #2093, PRIME-CANCELLATION.md §2, owns the balanced identity for \(M\) that motivates §2 below. Its orientation coefficients are distinct from those used here.

## 1. The signed unit has a cubic main term

Write \(U(s)=\sum u(d)d^{-s}\) and \(U(s)^{-1}=\sum v(d)d^{-s}\). The split, inert and ramified factors of \(U\), with \(z=p^{-s}\), are
\[
 (1-z)^2/(1-2z),\qquad 1-z^2,\qquad 1-z.
\]
Set \(\kappa=\log 2/\log 11\). Fix any real \(\kappa<\sigma<1/3\). In particular \(\sigma>1/4\) since \(11<2^4\). The exact formal factorization is
\[
 U(s)=L(2s,\chi_5)\zeta(3s)L(3s,\chi_5)W_4(s),
\]
with local factors of \(W_4\)
\[
 \frac{(1-z)^2(1-z^2)(1-z^3)^2}{1-2z}\quad(p\text{ split}),\qquad
 (1-z^4)(1-z^6)\quad(p\text{ inert}),\qquad
 (1-z)(1-z^3)\quad(p=5).
\]
The unramified deviations start at degree four. At the split primes the denominator also requires \(2p^{-\sigma}<1\), valid uniformly because the first split prime is 11 and \(\sigma>\kappa\). Thus the coefficient sequence \(w_4\) of \(W_4\) has \(\sum |w_4(d)|d^{-\sigma}<\infty\). The real value \(W_4(1/3)\) is positive by the positive individual factors and the convergent deviations.

Write \(f_5=\mathbf1*\chi_5\). The fixed-character hyperbola identity from the earlier candidate gives \(\sum_{m\le y}f_5(m)=L(1,\chi_5)y+O(\sqrt y)\), with \(f_5\ge0\). Consider the summatory product before convolution with \(w_4\):
\[
 B(x)=\sum_{q^2m^3\le x}\chi_5(q)f_5(m).
\]
For \(Q=x^{1/8}\), the terms \(q\le Q\), after summing in \(m\), equal
\[
 L(1,\chi_5)x^{1/3}\sum_{q\le Q}\frac{\chi_5(q)}{q^{2/3}}
  +O\!\left(x^{1/6}\sum_{q\le Q}q^{-1/3}\right).
\]
The error is \(O(x^{1/4})\). Completing the character series at \(2/3\) costs \(O(x^{1/3}Q^{-2/3})=O(x^{1/4})\), using bounded character partial sums. For \(q>Q\), group by \(m\le (x/Q^2)^{1/3}\); the inner character sum on any such interval is bounded, so this part is \(O((x/Q^2)^{1/3})=O(x^{1/4})\). Consequently,
\[
 B(x)=L(1,\chi_5)L(2/3,\chi_5)x^{1/3}+O(x^{1/4}).
\]
Convolving with \(w_4\), the omitted main-series tail is \(O_\sigma(x^\sigma)\) by its absolute norm at \(\sigma\), and the summed \(x^{1/4}\) errors are also \(O_\sigma(x^\sigma)\) because \(\sigma>1/4\). We obtain the signed estimate
\[
 U_\Sigma(x):=\sum_{k\le x}u(k)=C_U x^{1/3}+O_\sigma(x^\sigma),
 \qquad C_U=L(1,\chi_5)L(2/3,\chi_5)W_4(1/3)>0.                \tag{1}
\]
For completeness \(L(s,\chi_5)>0\) on the real line \(s>0\): in every full five-term block the difference between the first two nonzero terms is positive and larger than the absolute opposite difference between the last two. This follows since \(x^{-s}-(x+1)^{-s}\) is strictly decreasing in \(x>0\). The series converges by bounded partial sums. The positive coefficient in (1) concerns signed summation of \(u\). The round-4 absolute coefficient count has a different, square-root exponent.

## 2. A finite balance for the actual \(T\) and its tail correction

Fix a large dyadic integer \(X\), and use the same coefficients throughout \(X\le N\le3X\). Set \(A=\lceil\sqrt{3X}\rceil\), take \(c(a)=t(a)\) for \(a\le A\), and append \(|T(A)|\) copies of \(-\operatorname{sgn}T(A)\) at the next consecutive indices. Set the remaining coefficients to zero. Thus \(\sum c(a)=0\), \(|c(a)|\le1\), and the support lies in \(a\le2A\), since \(|t(a)|\le1\). Put \(b=c*c\) and \(h_X=\sum c(a)/a\).

The exact Dirichlet inverse of \(t\) is \(f=\mathbf1*u\), with \(\mathbf1(m)=1\). Indeed \(t=\mu*v\) and \(u*v=\delta\). Hence \(\delta-f*c\) vanishes through \(A\), and its convolution square vanishes through \(3X\). Expanding \(t*(\delta-f*c)^{*2}\) proves \(t(n)=2c(n)-(f*b)(n)\) throughout that range. For \(2A\le N\le3X\) the first term sums to zero, so
\[
 T(N)=-\sum_{k,d}u(k)b(d)\lfloor N/(kd)\rfloor.                \tag{2}
\]
The floor terms automatically restrict the sum to \(kd\le N\).

For an integer \(L\ge2A\), put \(b_L(q)=\sum_{kd=q,\ k\le L}u(k)b(d)\) and \(\alpha_L=\sum_{k\le L}u(k)/k\). Use
\[
 \psi_q(N)=\{(N+1/2)/q\}-1/2,\qquad
 \mathcal U_L(N)=\sum_{m\le N/L} j(m)\,[U_\Sigma(N/m)-U_\Sigma(L)],
 \qquad j=\mu*v*v .
\]
For \(k>L\) and \(m\le N/k\), we have \(m<A\) since \(L\ge2A\), \(A^2\ge3X\). On these indices \((\mathbf1*b)(m)=(\mathbf1*t*t)(m)=j(m)\) exactly. This proves that \(\mathcal U_L\) is the omitted unit sum in (2), with the strict lower endpoint \(k>L\). Also \(\sum_q b_L(q)=0\) and \(\sum_q b_L(q)/q=\alpha_Lh_X^2\). Since \(\lfloor(N+1/2)/q\rfloor=\lfloor N/q\rfloor\) for integer \(N,q\), (2) becomes
\[
 T(N)=\sum_{q\le 4A^2 L}b_L(q)\psi_q(N)
       -(N+1/2)\alpha_Lh_X^2-\mathcal U_L(N).                  \tag{3}
\]
Absolute convergence at one gives \(\alpha_L\to U(1)>0\). Thus the explicit square drift is nonpositive for all sufficiently large \(L\). Terms with \(q>N\) have zero original floor and are still present through their centered affine values in (3).

The auxiliary \(j\) satisfies
\[
 \sum_{m\le x}|j(m)|\le x\left(\sum_{d\ge1}|v(d)|/d\right)^2\ll x.
\]
This follows by expanding the convolution and using \(|\mu|\le1\), without any signed estimate for \(j\). Define the same-argument cubic correction
\[
 \mathcal C_L(N)
   = C_U\sum_{m\le N/L}j(m)\bigl[(N/m)^{1/3}-L^{1/3}\bigr].
\]
For \(2A\le L\le N\), (1) and the preceding absolute mean give
\[
 \mathcal U_L(N)=\mathcal C_L(N)+O_\sigma(N L^{\sigma-1}),
 \qquad |\mathcal U_L(N)|\ll N L^{-2/3}.                        \tag{4}
\]
Indeed each error in (1) is \(O_\sigma((N/m)^\sigma)\) as \(N/m\ge L\). Partial summation gives \(\sum_{m\le N/L}|j(m)|m^{-\sigma}\ll_\sigma(N/L)^{1-\sigma}\). The same calculation with the exponent \(1/3\) proves the second inequality using \(U_\Sigma(x)=O(x^{1/3})\). Neither formula estimates the sign of \(\mathcal C_L(N)\). It can also be written \((C_U/3)N^{1/3}\int_1^{N/L}(\sum_{m\le t}j(m))\,dt/t^{4/3}\), since the upper endpoint of the weight is zero.

There are two useful quantitative scales. At \(L=\lceil X^{3/4}(\log X)^2\rceil\) one may delete all of \(\mathcal U_L\) with pointwise error \(O(\sqrt X(\log X)^{-4/3})\). At the shorter cutoff
\[
 L=\bigl\lceil X^{\,1/[2(1-\sigma)]}(\log X)^2\bigr\rceil       \tag{5}
\]
the same conclusion holds for \(\mathcal U_L-\mathcal C_L\), while keeping the actual signed correction. For sufficiently large \(X\) both cutoffs lie between \(2A\) and \(X\), and (4) applies uniformly on the slab. The exponent in (5) is strictly less than \(3/4\). In either use the squared error summed over all late integers with weight \(1/[N(N+1)]\) is \(O_\sigma((\log Y)^{-5/3})\) above \(Y\): one dyadic block costs \(O_\sigma((\log X)^{-8/3})\), which is summable in the dyadic index.

## 3. One controlled balanced target

Take the shorter cutoff (5) and keep \(\mathcal C_L(N)\) with its sign. There is a square-summable deletion on the short denominators in (3). Set \(D=\lfloor X^{2/3}/(\log X)^2\rfloor\). Since \(|b(d)|\le\tau(d)\), the common majorant \(\rho=|u|*\tau\) gives \(|b_L(q)|\le\rho(q)\) for every \(L\). At the \(k\)-th positive prime powers the factors are
\[
 \rho(p^k)=
 \begin{cases}
  2^k,&p\ \text{split},\\
  2k,&p\ \text{inert},\\
  2k+1,&p=5.
 \end{cases}
\]
These follow by multiplying the absolute local factors of \(u\) by \((1-z)^{-2}\). They are submultiplicative at each prime, so \(\rho(de)\le\rho(d)\rho(e)\). Also \(\sum_{n\le x}\rho(n)/n\ll(1+\log x)^2\) by the absolute norm of \(u\) at one. Finally \(\sum_{n\le x}\rho(n)^2\ll x(1+\log x)^3\). To see the last assertion, define \(h_0\) by the Dirichlet coefficient comparison \(\rho(n)^2=(\tau_4*h_0)(n)\). At each unramified prime the local linear coefficient of \(\rho^2\) is four, so the correction obtained by multiplying by \((1-z)^4\) starts at degree two. The higher coefficients are absolutely summable at \(s=1\), with a total \(O(p^{-2})\) per unramified prime, using the geometric series \(4^k\) at split primes \(p\ge11\) and the quadratic bound at inert primes. The single factor at 5 is harmless. Thus \(\sum |h_0(d)|/d<\infty\), and the elementary divisor bound \(\sum_{n\le x}\tau_4(n)\ll x(1+\log x)^3\) proves the assertion.

The complete-period centered sawtooth covariance \((\gcd(q,r)^2-1)/(12qr)\) is the one in #2093 PRIME-CANCELLATION.md §3. Grouping by \(g=\gcd(q,r)\), applying submultiplicativity and the harmonic \(\rho\) bound, and subdividing \(g\) dyadically therefore give
\[
 \sum_{q,r\le D}\rho(q)\rho(r)\frac{\gcd(q,r)^2}{qr}
 \ll \sum_{g\le D}\rho(g)^2(1+\log(D/g))^4
 \ll D(1+\log D)^3.
\]
All distinct nonzero frequencies for \(q\le D\) have circle spacing at least \(D^{-2}\); the established additive large sieve from KERNEL.md §7 gives, after division by \(X^2\), a squared weighted error \(O(X^{-2}(X+D^2)D(1+\log D)^3)=O((\log X)^{-3})\) on the slab. Summing over late dyadic blocks makes its squared weighted norm \(O((\log Y)^{-2})\).

Define the balanced residual on each original block by
\[
 F_{\rm bal}(N)=\sum_{D<q\le4A^2L} b_L(q)\psi_q(N)
             -(N+1/2)\alpha_Lh_X^2-\mathcal C_L(N),
 \qquad X\le N<2X .
\]
It retains all denominators above \(D\). If desired, the terms \(q>3X\) may be grouped exactly as \(\sum_{q>3X}b_L(q)[(N+1/2)/q-1/2]\); their affine contribution is not discarded or given an unproved sign. Combining (3)–(5) with the short-denominator bound gives
\[
 \sum_{N\ge Y}\frac{|T(N)-F_{\rm bal}(N)|^2}{N(N+1)}
       \ll_\sigma(\log Y)^{-5/3} .
\]
In particular the square roots of their positive-part window energies on the same \([Y,Y^2)\) differ by \(O_\sigma((\log Y)^{-5/6})\). The existing window quantifier transfers in both directions by using the source exponent \(2r\) before the requested exponent \(r\). By the already proved criteria this tests the same RH statement as \(P_X^\star\). It is a new one-sided carrier with its own coefficients, not an identity between its pairs and those of \(P_X^\star\).

**O.** The signed low-height estimate in the original \(P_X^\star\) is still open. In the balanced carrier, the long-denominator sum, its affine terms, the negative square, and the actual cubic correction share the same argument. No new all-epsilon bound for their joint positive part is established.

## Sources

- The pinned #2089 FOUNDATION §2, KERNEL §7 and round-4 CRITICAL-UNIT supply the inverse coefficient unit and the finite interval large sieve.
- Neighbor #2093 at 2147cba363d90d2772c3d5f883d79c326260d9c9, PRIME-CANCELLATION.md §§2–3, supplies the balanced Mertens construction and exact sawtooth covariance.
- The signed cubic estimate (1), cutoffs (4)–(5), and \(t\)-balance (3) are derived above.
