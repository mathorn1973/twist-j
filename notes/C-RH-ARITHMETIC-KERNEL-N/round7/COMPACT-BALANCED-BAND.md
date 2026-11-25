# Compact raw denominators and double cancellation in the balanced carrier

C-RH-ARITHMETIC-KERNEL-N, issue #2087 / draft #2089, round 7. **NON-CANONICAL. No authority. Candidate-D.** Paper proof under [PREREG](PREREG-BALANCED.md). The square-root-scale estimate for the full signed carrier has status **O**.

## 1. Compact raw denominators with their affine terms

Use the actual \(t=\mu*v\), \(T(n)=\sum_{m\le n}t(m)\), the exact unit coefficients \(u\), and the balanced \(c\) of round 6. Thus \(X\) is dyadic, \(A=\lceil\sqrt{3X}\rceil\), \(c(a)=t(a)\) for \(a\le A\), and the next \(|T(A)|\) entries are \(-\operatorname{sgn}(T(A))\). The support lies in \(a\le 2A\), \(|c(a)|\le1\), and \(\sum c=0\). Put \(b_L(q)=\sum_{kab=q,\,k\le L}u(k)c(a)c(b)\). The inherited result gives, at integer times \(2A\le n\le 3X\),
\[
 T(n)=-\sum_q b_L(q)\lfloor n/q\rfloor-\mathcal U_L(n),\qquad
 \mathcal U_L(n)=\mathcal C_L(n)+O_\sigma(nL^{\sigma-1}),                 \tag{1}
\]
where \(\log 2/\log 11<\sigma<1/3\), \(2A\le L\le n\), and
\[
 \mathcal C_L(n)=C_U\sum_{m\le n/L}(\mu*v*v)(m)\big[(n/m)^{1/3}-L^{1/3}\big].
\]
Use \(L=\lceil X^{1/[2(1-\sigma)]}\exp(\sqrt{\log X})\rceil\). This is between \(2A\) and \(7X/8\) on sufficiently late slabs. The error in (1) is then \(O_\sigma(\sqrt X\exp[-(1-\sigma)\sqrt{\log X}])\) uniformly on the taper and on the translates below.

Fix a real smooth function \(\eta\in[0,1]\) that is one on \([0,3]\) and zero on \([4,\infty)\). Replace \(b_L(q)\) in the floor sum by \(z(q)=\eta(q/X)b_L(q)\). This is exact throughout the range of (1), since \(\eta(q/X)\ne1\) implies \(q>3X\). With \(\psi_q(n)=\{(n+1/2)/q\}-1/2\),
\[
 -\sum_q z(q)\lfloor n/q\rfloor
  =\sum_q z(q)\psi_q(n)-(n+1/2)\sum_q z(q)/q+\frac12\sum_q z(q).       \tag{2}
\]
The constant and slope both use the masked coefficients. The identity for the removed weights \((1-\eta(q/X))b_L(q)\) has right side identically zero throughout the valid time range. The slope in (2) is a signed truncated sum.

Take \(H=\lceil\sqrt X\rceil\) and \(J=\lceil\log_2 X\rceil\). Let \(\mathcal A\) denote the \(J\)-fold forward average of width \(H\), the expectation of translation by the sum \(s\) of \(J\) independent uniform integers in \([0,H-1]\). Define
\[
 \ell(n)=n+\tfrac12+J(H-1)/2,\qquad
 \mathcal B(n)=\sum_q z(q)\left[\tfrac12-\ell(n)/q\right].
\]
On the original taper \(w\), all \(n+s\) lie in \([2A,3X]\) on late slabs. Equations (1) and (2) give
\[
 \mathcal A T(n)=\mathcal A\sum_qz(q)\psi_q(n)+\mathcal B(n)
                   -\mathcal A\mathcal C_L(n)
                   +O_\sigma\big(\sqrt X e^{-(1-\sigma)\sqrt{\log X}}\big).
                                                                    \tag{3}
\]
The actual short-sum estimate of round 6 applies to every prefix of length \(J(H-1)\) from these starts. The starts are covered by the dyadic blocks with endpoints \(X/2,X,2X\). The length satisfies fixed polynomial margins in each block. The maximum bounds the error of each average. Consequently for every \(D>0\),
\[
 \|\mathcal A T-T\|_w\ll_D X(\log X)^{-D},\qquad
 \|F\|_w^2=\sum_n w(n)|F(n)|^2 .                                    \tag{4}
\]

## 2. Spectral restriction at inverse-logarithmic norm cost

At a reduced signed frequency \(\theta=a/q\) with \(0<|\theta|\le1/2\), the coefficient in the sawtooth sum before averaging is
\[
 -\frac{\sum_{q\mid d} z(d)/d}{1-e(-a/q)},\qquad e(y)=\exp(2\pi i y).
\]
For a raw denominator \(d\), this follows by summing the residues against the geometric progression at each nonzero ordinary harmonic \(j/d\). The zero harmonic vanishes. Averaging multiplies the coefficient by \(m_H(\theta)^J\), where \(m_H(\theta)=H^{-1}\sum_{j=0}^{H-1}e(j\theta)\).

Use \(\rho=|u|*\tau\) from round 6. The mask gives \(|z(d)|\le \rho(d)\). Submultiplicativity and the harmonic estimate give
\[
 \left|q\sum_{q\mid d}z(d)/d\right|\ll \rho(q)(1+\log X)^2,\qquad
 \sum_{q\le R}\rho(q)^2\ll R(1+\log R)^3.                             \tag{5}
\]
For a raw denominator \(d\), the sum of the magnitudes of its nonzero sawtooth coefficients is \(O(1+\log d)\). Also \(\sum_{d\le4X}\rho(d)\ll X(1+\log X)\) by the elementary divisor sum and \(\sum_k|u(k)|/k<\infty\). Thus the total absolute coefficient mass before averaging is \(O(X(1+\log X)^2)\). If \(|\theta|\ge1/H\), then \(|m_H(\theta)|\le1/(2H|\theta|)\le1/2\), so these averaged modes cost \(O((1+\log X)^2)\) pointwise.

Among the remaining modes take the boxes \(R<q\le2R,\ B\le|a|<2B\), for powers of two \(R,B\ge1\). By (5) the squared coefficient mass in a box is \(O(R(1+\log X)^7/B)\). Distinct reduced frequencies in this shell have circular spacing at least \((2R)^{-2}\). The translated additive large sieve therefore gives squared norm
\[
 \ll (X+R^2)R(1+\log X)^7/B                                             \tag{6}
\]
on the taper. Delete boxes with \(B\ge\max(1,R^3\exp(\sqrt{\log X})/X^2)\). For \(R\ge\sqrt X\) the factor \((X+R^2)R/B\) is \(O(X^2e^{-\sqrt{\log X}})\), and for \(R<\sqrt X\) it is \(O(X^{3/2})\). The triangle inequality gives a total norm cost \(O_D(X(\log X)^{-D})\) for every fixed \(D\) after summing over the \(O((1+\log X)^2)\) boxes.

Let \(G_{\mathrm b}\) retain exactly the modes with \(|\theta|<1/H\) outside those deleted boxes, and define
\[
 F_X(n)=G_{\mathrm b}(n)+\mathcal B(n)-\mathcal A\mathcal C_L(n).
\]
All frequencies of \(G_{\mathrm b}\) have reduced denominator \(q\le4X\). Equations (3), (4) and (6) give
\[
                 \|T-F_X\|_w\ll_D X(\log X)^{-D}\qquad(D>0).           \tag{7}
\]
The mass bound comes from the second moment in (5), which also covers high powers of individual split primes.

## 3. Double cancellation with a signed large-unit estimate

Let \(\Phi(x)=(\log x)^{3/5}(\log\log x)^{-1/5}\) for sufficiently large \(x\). Round 5 transferred the unconditional bound with a fixed \(\gamma>0\),
\[
             |T(x)|\ll x\log x\,\exp[-\gamma\Phi(x)],                   \tag{8}
\]
from the cited estimate of Lee and Leong while preserving its exponential constant. Round 6 gives \(\sum_{k\le x}u(k)=C_U x^{1/3}+O_\sigma(x^\sigma)\).

Fix a smooth even real function \(\chi\in[0,1]\), equal to one on \([-1,1]\) and supported in \([-2,2]\). Take \(1\le K\le X^{1/10}\). All nonzero frequencies of the compact raw sawtooth sum with \(\chi(X\theta/K)\ne0\) satisfy \(q\ge X/(2K)\), \(|a|\le 8K\), and \(|\theta|<1/H\). They survive the box deletion since \(R\ge X/(4K)\) makes \(R^3/X^2\ge X/(64K^3)>8K\) for late \(X\). Their smooth contribution in \(G_{\mathrm b}\) can therefore be computed using the complete compact raw sawtooth sum.

Choose a smooth real cutoff \(\beta\in[0,1]\) equal to zero for \(y\le1/4\) and to one for \(y\ge1/2\). Denote by \(V_{X,K}(n)\) the sum of this smooth frequency contribution and the following part of the actual affine term:
\[
       \sum_q z(q)\beta(Kq/X)\left[\tfrac12-\ell(n)/q\right].
\]
This smooth raw range contains every raw denominator contributing to the slow frequency band. The signed affine complement, the complementary frequencies and \(-\mathcal A\mathcal C_L\) belong to \(F_X-V_{X,K}\).

For \(1\le k_0\le X^{1/10}\) set \(Z=X/(16AKk_0)\). Uniformly on the original taper,
\[
 |V_{X,K}(n)|\ll
 X(1+\log X)^4
  \left[(1+K)^2e^{-2\gamma\Phi(Z)}+(1+K)k_0^{-2/3}\right].             \tag{9}
\]
To prove (9) work before averaging at every translated integer time \(t_0=n+s\). Expand \(z(q)\) over \(q=kab\). The positive ordinary harmonics use
\[
 f_j(q)=-\eta(q/X)\chi(Xj/(Kq))\frac{e(t_0j/q)}{q(1-e(-j/q))},
 \qquad 1\le j\le\lfloor 8K\rfloor .
\]
The negative harmonics are conjugates. The affine part uses
\[
 f_0(q)=\eta(q/X)\beta(Kq/X)\left[\tfrac12-(t_0+1/2)/q\right].
\]
Ordinary harmonics count each raw denominator contribution even if other denominators give the same reduced fraction. Write \(D_q=q\,d/dq\). On the supports \(X/(4K)\le q\le4X\). For \(r=0,1,2\),
\[
 |D_q^r f_j(q)|\ll (1+K)^r/j\quad(j\ge1),\qquad
 |D_q^r f_0(q)|\ll 1+K.                                               \tag{10}
\]
For \(j\ge1\), write the prefactor as \(j^{-1}y/(1-e(-y))\) with \(y=j/q\le2K/X\) on support. This factor extends smoothly at zero, and \(t_0 y=O(K)\) controls differentiation of the exponential. The derivatives of the rescaled cutoffs are bounded on their supports. For \(j=0\), use \(t_0/q=O(K)\). These bounds also hold for the zero extensions off the smooth supports.

For \(k\le k_0\), the kernel \(f_j(kab)\) and its derivatives vanish if either \(a\) or \(b\) is at most \(Z\) and the other is at most \(2A\), since \(kab\le X/(8K)\). On \([Z,2A]\) the balanced prefix \(P(a)=\sum_{m\le a}c(m)\) satisfies
\[
 |P(a)|\ll a(1+\log X)e^{-\gamma\Phi(Z)}.
\]
For \(a\le A\) this follows from (8) and eventual monotonicity of \(\Phi\). For \(a>A\) the magnitude decreases from \(|T(A)|\) to zero. Two partial summations have no lower boundary by kernel support and no upper boundary by \(P(2A)=0\). Their mixed derivative is \(D_q^2 f_j(kab)/(ab)\). The factors \(a,b\) in the two prefix bounds cancel its denominator. The area of the integration region is at most
\[
 \int_Z^{2A} \frac{4X}{ka}\,da \ll (X/k)(1+\log X),
\]
since all derivatives require \(kab\le4X\). Sum over \(k\le k_0\) using \(\sum |u(k)|/k<\infty\). Summation of \(1/j\) up to \(8K\) uses one further logarithm. This gives the first term in (9) for the combined expression.

For \(k>k_0\), fix \(a,b\) and let \(W=\min(L,4X/(ab))\). The sum is empty if \(W\le k_0\). On \(k_0\le y\le W\), the inherited signed unit estimate gives
\[
             \left|\sum_{k_0<k\le y}u(k)\right|\ll y^{1/3}.
\]
Partial summation and (10) bound the sum over \(k_0<k\le W\) of \(u(k)f_j(kab)\) by \(O((1+K)W^{1/3}/j)\) for positive harmonics, and \(O((1+K)W^{1/3})\) for the affine part. This includes the upper boundary and uses \(\int_{k_0}^W y^{-2/3}\,dy\ll W^{1/3}\). Take absolute values in \(a,b\), using
\[
 \sum_{ab\le Q}(ab)^{-1/3}\ll Q^{2/3}(1+\log Q),
\]
by summing first over \(b\). With \(Q=4X/k_0\) the cost is \(O(Xk_0^{-2/3}(1+\log X))\) times the harmonic or affine factor. The harmonic sum and the convex average prove the second term in (9). The signed exponent \(1/3\) supplies the decay \(k_0^{-2/3}\). The absolute unit count, of order \(x^{1/2}\), would give \(k_0^{-1/2}\) by the same method.

For a subexponential consequence take
\[
 K=\exp(\lambda\Phi(\sqrt X)),\qquad
 k_0=\exp(\nu\Phi(\sqrt X)),\qquad
 0<\lambda<\gamma(1-2^{-2/5}),\quad \nu>3\gamma .
\]
These parameters satisfy the polynomial margins for late \(X\). Since \(\log(Z/\sqrt X)=O(\Phi(\sqrt X))\), the derivative of \(u^{3/5}(\log u)^{-1/5}\) gives \(\Phi(Z)=(1+o(1))\Phi(\sqrt X)\). Equation (9) gives
\[
 \max_{n\in\operatorname{supp}w}|V_{X,K}(n)|
 \ll X\exp[-(2\gamma-2\lambda-o(1))\Phi(\sqrt X)] .                    \tag{11}
\]
In the scale \(\Phi(X)\) the coefficient of the saving is \((2\gamma-2\lambda)2^{-3/5}>\gamma\). The stronger exponential constant applies to this designated signed component. Its squared taper norm bound is \(O(X^3\exp[-(4\gamma-4\lambda-o(1))\Phi(\sqrt X)])\), above the requested \(X^{2+\epsilon}\) scale for \(0<\epsilon<1\).

## 4. The whole affine term and cubic correction at this precision

The same argument bounds the full \(\mathcal B\) at the scale of (11). Write \(Z_0=X/(16Ak_0)\) and \(h_X=\sum_a c(a)/a\). Uniformly on the taper,
\[
 |\mathcal B(n)|\ll
 X|h_X|^2+X(1+\log X)^4
       \left[e^{-2\gamma\Phi(Z_0)}+k_0^{-2/3}\right].                    \tag{12}
\]
Here the two terms of \(\mathcal B\) use the same mask. For its constant term and \(k\le k_0\), replace \(\eta(kab/X)\) by \(\eta(kab/X)-1\), using \(\sum_{a,b}c(a)c(b)=0\) for every fixed \(k\). The resulting kernel vanishes at the lower integration boundary and its mixed derivative is supported in \(3X\le kab\le4X\). The two prefix bounds and the \(X/k\) area estimate of §3 give the first part in brackets. For \(k>k_0\) use \(\eta(kab/X)\) itself and the signed single-variable sum of §3. Its support still gives \(ab\le4X/k_0\) and both its magnitude and first logarithmic derivative are bounded. This gives the second part in brackets.

For the slope, the unmasked harmonic sum is \(\alpha_L h_X^2\), where \(\alpha_L=\sum_{k\le L}u(k)/k\) is bounded. The change from masking uses the kernel \(f(q)=(1-\eta(q/X))\ell(n)/q\). Its first two logarithmic derivatives and its magnitude are \(O(X/q)\). This kernel vanishes for \(q\le3X\). For \(k\le k_0\), the two prefix sums cancel the factors \(a,b\) in the mixed derivative as in §3. The area integral with weight \(X/(kab)\) is \(O((X/k)(1+\log X)^2)\) on \([Z_0,2A]^2\), producing the first bracket of (12). For \(k>k_0\), partial summation with the signed \(u\)-prefix bound gives, for each \(a,b\), an upper bound
\[
 \ll \frac{X}{ab}\left[L^{-2/3}
               +\int_{k_0}^L y^{-5/3}\,dy\right]
 \ll \frac{X k_0^{-2/3}}{ab}.
\]
The harmonic sums over \(a,b\le2A\) finish (12).

Equation (8) implies convergence of \(\sum_n t(n)/n\). Partial summation represents \(\sum_n t(n)n^{-s}\) for real \(s>1\) by \(s\int_1^\infty T(x)x^{-s-1}dx\), and (8) gives an integrable majorant at \(s=1\). The value of the series tends to zero by \(1/(\zeta(s)U(s))\) and \(U(1)>0\). For each fixed \(0<\delta<\gamma\), its tail and the padding give
\[
 |h_X|\ll_\delta e^{-(\gamma-\delta)\Phi(A)}.
\]
In the integral for the tail, split \(e^{-\gamma\Phi(x)}\) as \(e^{-(\gamma-\delta)\Phi(x)}e^{-\delta\Phi(x)}\) and use \(\int_A^\infty \log x\, e^{-\delta\Phi(x)}dx/x<\infty\) with a bound independent of \(A\). The first factor is decreasing on the tail. The padding costs at most \(|T(A)|/A\).

Finally \(\max_n|\mathcal A\mathcal C_L(n)|\ll XL^{-2/3}\) on the taper from the absolute mean \(\sum_{m\le y}|(\mu*v*v)(m)|\ll y\) in round 6. This is polynomially smaller than the right side of (11). Take the same \(K,k_0\) as in (11) and use any \(0<\delta<\lambda\). Then the slow frequency portion plus the full affine term and the signed cubic correction satisfies
\[
 \max_{n\in\operatorname{supp}w}
 \big|\Pi_{X,K}G_{\mathrm b}(n)+\mathcal B(n)-\mathcal A\mathcal C_L(n)\big|
 \ll X\exp[-(2\gamma-2\lambda-o(1))\Phi(\sqrt X)],                       \tag{13}
\]
where \(\Pi_{X,K}\) multiplies the finite \(G_{\mathrm b}\) coefficients by \(\chi(X\theta/K)\). For the oscillatory contribution alone one applies the proof of (9) with the term \(f_0\) omitted. The exact decomposition of \(F_X\) into (13) and \((1-\Pi_{X,K})G_{\mathrm b}\) keeps the interaction of these two parts in its squared norm.

## 5. A longer unit cutoff with the same compact frequencies

One may instead construct the compact carrier with \(L_+=\lceil X^{3/4}\exp(\sqrt{\log X})\rceil\), still between \(2A\) and \(7X/8\) on late slabs. For this choice the inherited bound on the full tail gives
\[
 \max_{2A\le n\le3X,\ n\ge L_+}
       |\mathcal U_{L_+}(n)|
       \ll XL_+^{-2/3}\ll \sqrt X e^{-(2/3)\sqrt{\log X}} .
\]
Build \(z,G_{\mathrm b},\mathcal B\) anew with \(L_+\) in place of \(L\), and write them as \(z_+,G_{\mathrm b,+},\mathcal B_+\). The exact raw mask still bounds the frequencies by \(q\le4X\), so extending the unit cutoff does not widen the available denominators. Use the norm bound on this full tail in (3) and keep the arguments of §§1–2:
\[
        F_{X,+}=G_{\mathrm b,+}+\mathcal B_+,\qquad
        \|T-F_{X,+}\|_w\ll_D X(\log X)^{-D}\qquad(D>0).                 \tag{14}
\]
The proofs of (9) and (12) use only an upper endpoint in the finite unit sum and hold for \(L_+\). Consequently (13) holds for \(\Pi_{X,K}G_{\mathrm b,+}+\mathcal B_+\), with the full omitted tail already covered by (14).

## 6. Exact scope of the comparison

Use \(F_X\) on each dyadic block \(X\le n<2X\). Since \(w=1\) on the block, (7) bounds its difference from \(T\) in the weighted norm on every complete integer window \([Y,Y^2)\) by \(O_D((\log Y)^{-D})\) for each fixed \(D>0\). The window meets \(O(1+\log Y)\) blocks with \(X\ge Y/2\), and the weight \(1/[n(n+1)]\) on each part is at most \(X^{-2}\). The positive-part Lipschitz inequality gives the same comparison for the square roots of their positive window energies. The inherited late-window quantifiers transfer in either direction by using the source exponent \(2r\) for the requested \(r\).

On the original taper, round 6 and (7), (14) give
\[
          \max_{F\in\{F_X,F_{X,+}\}}\|F-(G_{\rm core}+C_z)\|_w\ll_\epsilon X^{1+\epsilon}
          \qquad(\epsilon>0).
\]
There is also a slow observation directly on the combined core and lower-argument profile. Use \(I^+=[X-kh,2X-1+kh]\cap\mathbb Z\), where \(k=\lceil3\log_2 X\rceil\), \(h=\lfloor X/(16k)\rfloor\) in the original taper. The taper is the convolution of \(1_{I^+}\) with a symmetric probability supported in \([-kh,kh]\). For \(n\in I^+\) the half of its translates towards the midpoint stay in \(I^+\), so \(w(n)\ge1/2\). Also \(kh\ge X/32\) eventually. Define \(\mathscr P\) on integer time sequences by convolution with the Fourier coefficients \(p(j)\) of the smooth circle multiplier \(\chi(X\theta/K)\). Repeated integration by parts gives
\[
 |p(j)|\ll_M (K/X)(1+K|j|/X)^{-M},\qquad
 \|p\|_1\ll1,\qquad \|p\|_2\ll \sqrt{K/X}.
\]
This operation is applied to the finite time sequence \(1_{I^+}(G_{\rm core}+C_z)\). By \(w\ge1/2\) and (14), replacing it by \(1_{I^+}F_{X,+}\) costs \(O_\epsilon(X^{1/2+\epsilon}\sqrt K)\) pointwise after convolution, by Cauchy–Schwarz. For \(X\le n<2X\), extending the truncated oscillatory part \(1_{I^+}G_{\mathrm b,+}\) to the full periodic sum costs \(O_M(X(1+\log X)^2 K^{1-M})\) since the missing shifts have \(|j|\ge kh\) and the absolute coefficient sum is \(O(X(1+\log X)^2)\). The full convolution of \(G_{\mathrm b,+}\) is its slow portion. The affine part over \(I^+\) is bounded using (12) and \(\|p\|_1\ll1\). With the \(K\) of (11), choose any fixed \(0<\epsilon<1/2\) and then a fixed \(M\) with \((M-1)\lambda>2\gamma-2\lambda\). This yields
\[
 \max_{X\le n<2X}
 \left|\mathscr P\big[1_{I^+}(G_{\rm core}+C_z)\big](n)\right|
 \ll X\exp[-(2\gamma-2\lambda-o(1))\Phi(\sqrt X)].                       \tag{15}
\]
This estimate concerns the combined exact time profile after a specified convolution and time mask. Both the core and \(C_z\) enter the convolution.

The two representations have distinct coefficients and the comparison is through \(T\). A bound for the full balanced carrier at the target precision would transfer in the norm and therefore to the combined core quantity
\[
 P_{\rm core}+2\Re\langle G_{\rm core},C_z\rangle_w+\|C_z\|_w^2
\]
up to the inherited allowance. Each squared norm retains its mixed terms. An estimate for the squared-norm difference at order \(X^{2+\epsilon}\) also needs control of a full amplitude.

**O.** A joint bound at the desired precision is still required for (13) and its complementary oscillatory term. Equations (7), (9) and (13)–(15) give compact carriers and unconditional cancellation on the specified signed components and the filtered core profile under the original window and taper tests.

## Sources

- [Candidate #2089 at 4e098f9742a72a128bfb61a10c429bced78fe17e](https://github.com/mathorn1973/twist-j/tree/4e098f9742a72a128bfb61a10c429bced78fe17e/notes/C-RH-ARITHMETIC-KERNEL-N). Round 6 BALANCED-UNIT-TAIL §§1–3 supplies (1) and (5), SHORT-SPECTRAL-SCALES §1 supplies (4), CUBE-ROOT-TRANSFER §3 supplies the core and profile, round 5 FULL-ESTIMATE §2 supplies (8), and KERNEL §7 supplies the translated additive large sieve.
- [Neighbor #2093](https://github.com/mathorn1973/twist-j/pull/2093), head eac05e3cde56d0fb3e429b91aa7129087e5da4db. BILINEAR-LOW §§1–2 motivates the coupled affine deletion. LOW-FREQUENCY-PAIRS §3 supplies the numerator-box method. LOW-ENERGY-REVIEW §1 motivates two partial summations in the slow band of the balanced Mertens carrier. The support-area factor and signed unit estimate here account for the distinct \(t\) coefficients.
- [Lee and Leong, v5, Theorem 1.1, equation (12)](https://arxiv.org/html/2208.06141v5). Used through the precise transferred estimate in the pinned FULL-ESTIMATE.
