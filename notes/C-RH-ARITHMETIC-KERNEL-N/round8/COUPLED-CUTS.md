# The complete large-prime regroup and the two signed factor squares

C-RH-ARITHMETIC-KERNEL-N, existing owner [#2087](https://github.com/mathorn1973/twist-j/issues/2087), draft [#2089](https://github.com/mathorn1973/twist-j/pull/2089), round 8. **NON-CANONICAL. No authority. Candidate-D paper deductions.** Action layer NOT_APPLICABLE. The complete power estimate remains **O**. See [PREREG.md](PREREG.md).

## 1. Exact regrouping on the frozen cube-root block

Let \(X\) be dyadic, \(D=4X\), \(z=D^{1/3}\), and \(w\) the frozen taper, equal to one on \([X,2X)\) and supported on \([7X/8,17X/8]\). Write \(T(n)=\sum_{m\le n}t(m)\), \(t=\chi_5*s\), where \(s\) is supported on squarefree products of split primes with weight \((-2)^{\omega(m)}\). Split means \(\chi_5(p)=1\), inert means \(\chi_5(p)=-1\). At powers of primes the actual \(t\) has the values
\[
 t(p^j)=-1\ (p\text{ split}),\qquad
 t(p^j)=(-1)^j\ (p\text{ inert}),\qquad
 t(5^j)=0\quad(j\ge1).
\]
Let \(T_z(n)\) sum \(t(m)\) through \(n\) restricted to \(P^+(m)\le z\), with \(P^+(1)=1\). Let \(B_z(n)\) be the raw sum \(\sum_{d\le n,\,P^+(d)\le z}s(d)\sum_{m\le n/d}\chi_5(m)\). Round 6 proves \(T=B_z+C_z\) on the taper and round 7 proves
\[
 \|G_7-B_z\|_w^2\ll_\epsilon X^{2+\epsilon},\qquad
 Q_7=\|G_7+C_z\|_w^2+O_\epsilon(X^{2+\epsilon}),
 \qquad \|F\|_w^2=\sum_n w(n)|F(n)|^2.                              \tag{1}
\]
The first estimate is the inherited norm comparison after substituting \(T=B_z+C_z\).

At \(n\le D\) every \(m\le n\) has a unique factorization into a factor with all prime factors at most \(z\) and one with all prime factors greater than \(z\). The latter has at most two prime factors counted with multiplicity, since \(z^3=D\) and the restrictions on primes are strict. In the raw \(B_z\) the prime factors weigh \(t\) up to \(z\), and \(\chi_5\) beyond \(z\). The factorization gives
\[
 B_z(n)=T_z(n)+\sum_{p>z}\chi_5(p)T_z(\lfloor n/p\rfloor)
       +\sum_{z<p\le q}\chi_5(p)\chi_5(q)T(\lfloor n/(pq)\rfloor).
                                                                    \tag{2}
\]
Unrestricted prime sums run over both classes. A floor-zero argument contributes zero, which sets the upper endpoints. The prime \(5\) is below \(z\) on late blocks. In the last sum \(n/(pq)<z\), where \(T_z=T\). At a distinct pair \(p,q>z\) the \(t\)-weight is \(1\), and at \(p^2\) it is \(-\chi_5(p)\). Subtract (2) from the corresponding expansion of \(T\) to get exactly
\[
 C_z(n)=-2\sum_{\substack{p>z\\p\ {\rm split}}} T_z(\lfloor n/p\rfloor)
         +2\sum_{\substack{p,q>z\\p\ {\rm split},\,q\ {\rm inert}}}
                         T(\lfloor n/(pq)\rfloor)
         -2\sum_{\substack{p>z\\p\ {\rm split}}}T(\lfloor n/p^2\rfloor).
                                                                    \tag{3}
\]
The mixed sum counts each split–inert pair once. Formula (3) preserves the frozen \(C_z\), including its repeated split pair with weight four there. Indeed, for \(p>z\) the state \(\lfloor n/p\rfloor<z^2\) has at most one prime above \(z\), so
\[
 T_z(\lfloor n/p\rfloor)
   =T(\lfloor n/p\rfloor)+\sum_{q>z}T(\lfloor n/(pq)\rfloor).
\]
Substitution in (3) cancels the mixed sum, gives weight minus four to distinct split–split pairs, and adds the other weight minus two to split repeated pairs. In the full \(T\) expansion the same substitution yields
\[
 \begin{split}
 T(n)&=\mathcal J_z(n)+\mathcal R_z(n),\\
 \mathcal J_z(n)&=T_z(n)-\sum_{p>z}T(\lfloor n/p\rfloor)
                      -\sum_{z<p<q}T(\lfloor n/(pq)\rfloor),\\
 \mathcal R_z(n)&=-2\sum_{\substack{p>z\\p\ {\rm split}}}
                         T(\lfloor n/p^2\rfloor).
 \end{split}                                                        \tag{4}
\]
At each distinct pair the single-mark expansion supplies two ordered incidences and the original \(t\)-weighted pair gives one back. At a repeated pair the net coefficient is \(-1-\chi_5(p)\): inert squares cancel, split squares retain weight minus two. The identity (4) is exact for the joint arithmetic profile and (1) transfers its entire amplitude to the frozen carrier. The squared norm of \(\mathcal J_z+\mathcal R_z\) includes their mixed term.

## 2. The repeated-pair operator is a strict contraction

Extend prefix sums by zero below one and by the integer floor on real arguments. For real \(\sigma\ge1/2\) and dyadic \(X\) use
\[
 E_{\sigma,X}(F)=X^{1/2-\sigma}
                   \left(\int_X^{2X}|F(u)|^2\frac{du}{u^2}\right)^{1/2}.
\]
The integral is the exact discrete sum with weights \(1/[n(n+1)]\) for integer \(X\). For \(d>0\), let \(V\) be dyadic with \(V\le X/d<2V\). Dilation gives a factor \(d^{-1/2}\) in the unnormalized norm, and \([X/d,2X/d)\subset[V,4V)\). Taking the squared norms in the two blocks and using \(V\le X/d\) gives
\[
 E_{\sigma,X}\big(F({\cdot}/d)\big)\le d^{-\sigma}
        \sqrt{1+2^{2\sigma-1}}\,
        \max\{E_{\sigma,V}(F),E_{\sigma,2V}(F)\}.                    \tag{5}
\]
For \(\mathcal R_z\) take \(d=p^2\). For contributing \(p\) the two dyadic blocks have scales at most \(2X/z^2<X\) on late blocks. Minkowski's inequality gives
\[
 E_{\sigma,X}(\mathcal R_z)\le \rho_\sigma(X)
            \max_{\substack{Y\ {\rm dyadic}\\ Y\le2X/z^2}}E_{\sigma,Y}(T),
 \qquad
 \rho_\sigma(X)=2\sqrt{1+2^{2\sigma-1}}
         \sum_{\substack{z<p\le\sqrt{2X}\\p\ {\rm split}}}p^{-2\sigma}.   \tag{6}
\]
Dyadic \(Y<1\) has zero norm. For every \(\sigma>1/2\), summing over all integers gives \(\rho_\sigma(X)=O_\sigma(z^{1-2\sigma})\). At \(\sigma=1/2\), the fixed-modulus prime number theorem and partial summation give
\[
 \rho_{1/2}(X)=\sqrt 2\log(3/2)+o(1)<1
\]
eventually. The reciprocal split-prime sum is \(\frac12\log(\log\sqrt{2X}/\log z)+o(1)\), and \(\log(3/2)<1/2\). Thus for large \(X\), \(\rho_\sigma(X)\le\rho<1\), for every fixed \(\sigma\ge1/2\). If \(E_{\sigma,X}(\mathcal J_z)\) is bounded by \(M\) on all sufficiently late dyadic blocks, with \(z\) reset for each \(X\), induction in (4) and (6) bounds \(E_{\sigma,X}(T)\) by the larger of \(M/(1-\rho)\) and the finite initial maximum. The converse follows from the same inequalities. This induction uses the actual smaller arguments of the repeated terms.

For each \(\sigma>1/2\), boundedness of \(E_{\sigma,X}(T)\) on the central dyadic blocks is equivalent to \(\|T\|_w=O_\sigma(X^{\sigma+1/2})\) on the frozen tapers. On the central block \(w=1\), and \(1/[n(n+1)]\) is comparable to \(X^{-2}\). In the other direction the taper lies in the union of the central blocks at \(X/2,X,2X\), and \(w\le1\). Taking the error exponent in (1) strictly smaller than \(2\sigma-1\) proves, on all sufficiently late dyadic blocks,
\[
 (Q_7)_+=O_\sigma(X^{1+2\sigma})
 \quad\Longleftrightarrow\quad
 E_{\sigma,X}(\mathcal J_z)=O_\sigma(1)
 \qquad(\sigma>1/2).                                               \tag{7}
\]
The forward implication uses \(\|G_7+C_z\|_w^2\le (Q_7)_++O_\epsilon(X^{2+\epsilon})\), then compares amplitudes with \(T\) in norm. The reverse uses (1) after bounding \(T\). This transfers the requested all-epsilon family without assuming an additive comparison of two squared energies. The boundary \(\sigma=1/2\) in (6) concerns the arithmetic identity (4). Identity (1) supplies no \(O(X^2)\) transfer at that boundary.

## 3. Both prime classes contribute to the remaining drift

Write \(\mathcal H_z=\mathcal J_z-T_z\). Set \(\ell=\log n\), \(a=\log z/\ell\), \(b(u)=1-\log u/\ell\), and \(\kappa=1/U(1)>0\). Uniformly on the taper,
\[
 \begin{split}
 -\sum_{p>z}T(\lfloor n/p\rfloor)&=\kappa n/\ell^2+O(X/\ell^3),\\
 -\sum_{z<p<q}T(\lfloor n/(pq)\rfloor)&=-\kappa(3/2-\log 2)n/\ell^2
                                              +O(X/\ell^3),\\
 \mathcal H_z(n)&=\kappa(\log 2-1/2)n/\ell^2+O(X/\ell^3).
 \end{split}                                                       \tag{8}
\]
To pass from the pinned round-seven split-prime integral to this all-prime integral, use \(\pi(y)=\operatorname{Li}(y)+O_A(y/(\log y)^A)\). Insert \(T(u)=\sum_{m\le u}t(m)\) so that each count at \(y=n/m\) is cumulative, with endpoints at least \(z\) in nonempty ranges. For pairs the ordered inner count is \(\pi(y/p)-\pi(z)\). Summing its errors over \(p\) costs \(O_A(y(\log X)^{1-A})\). For the outer partial summation the main-count integrand is \(\operatorname{Li}(y/p)-\operatorname{Li}(z)\). Its upper endpoint is zero, its lower one is \(O(y/(z\log X))\), and its slope is \(O(y/(p^2\log X))\) in magnitude. This gives the same error allowance after the outer prime replacement. Since \(\sum_{m\le n/z}|t(m)|/m\le1+\log X\), a fixed large \(A\) makes the error \(O(X/\ell^3)\). The product integral has weight minus one half on the ordered region, with a diagonal add-back \(+\frac12\sum_{p>z}T(n/p^2)=O(X/z)\). Transforming by \(u=n/(pq)\) and \(s=\log p/\ell\) gives
\[
 \int_a^{b(u)-a}\frac{ds}{s(b(u)-s)}
       =\frac2{b(u)}\log\!\frac{b(u)-a}{a}.
\]
The first and second main terms are respectively
\[
 -\frac n\ell\int_1^{n/z}\frac{T(u)}{u^2b(u)}du,\qquad
 -\frac n\ell\int_1^{n/z^2}\frac{T(u)}{u^2}
                      \frac1{b(u)}\log\!\frac{b(u)-a}{a}\,du .
\]
The round-seven split densities and coefficients give the same two integral kernels. Both cutoffs are fixed powers of \(X\) up to constants. The inherited pointwise cancellation of \(T\) makes all fixed absolute logarithmic moments finite and their truncation errors smaller than any fixed inverse logarithmic power. Use
\(\int_1^\infty T(u)du/u^2=0\) and \(\int_1^\infty T(u)\log u\,du/u^2=-\kappa\).
The first derivatives of the kernels at \(b=1\) tend to \(-1\) and \(3/2-\log2\), respectively, with errors \(O(1/\ell)\). Their second derivatives are uniformly bounded on the displayed ranges. Taylor expansion through the first derivative proves (8).

The coefficient \(\kappa(\log2-1/2)\) is positive since \(\log2>1/2\). The two prime sums therefore have a combined contribution with squared taper norm asymptotic to
\[
 \kappa^2(\log2-1/2)^2\sum_n w(n)n^2/(\log n)^4
       \asymp X^3/(\log X)^4 .
\]
The same \(T_z\) has the opposite leading term, by (4), the inherited \(T(n)=O_B(X/(\log X)^B)\) for all fixed \(B\), and \(\mathcal R_z(n)=O(X/z)\) from \(|T(u)|\le u\). Equation (8) displays the remaining leading cancellation between the actual restricted prefix and the all-prime sector. The latter has the same first prime coefficient in both classes.

## 4. A transfer to two negative squares with the actual inverse weights

Let \(u\) be the Dirichlet coefficients of \(U\), and use \(f=\mathbf1*u=t^{-1}\), where \(\mathbf1(n)=1\) and the inverse is for Dirichlet convolution. All \(f(k)\) are nonnegative by the exact local factors: at split primes \(f(p^j)=2^{j-1}\) for \(j\ge1\), at inert primes \(f(p)=1\) and \(f(p^j)=0\) for \(j\ge2\), and at the ramified prime the positive powers vanish. Let \(F(y)=\sum_{k\le y}f(k)\). The signed unit estimate in round 6 and the absolute count in round 4 give
\[
 U_\Sigma(y)=\sum_{k\le y}u(k)=C_U y^{1/3}+O(y^{3/10}),\qquad
 \sum_{k\le y}|u(k)|=O(y^{1/2}),
\]
with \(C_U>0\). The first exponent is admitted since \(2^{10}<11^3\). These estimates give
\[
 F(y)=U(1)y+C_U\zeta(1/3)y^{1/3}+O(y^{5/12}).                      \tag{9}
\]
For the proof set \(B=\lfloor y^{5/6}\rfloor\), \(K=\lfloor y/B\rfloor\), and split \(F(y)=\sum_{dk\le y}u(d)\) at \(d=B\). The first part is
\[
 yU(1)-\tfrac12 C_U y B^{-2/3}
       +O\big(B^{1/2}+yB^{-7/10}\big)
\]
by partial summation of \(\sum_{d>B}u(d)/d\) and the absolute count for the floors. The second part is \(\sum_{k\le K}[U_\Sigma(y/k)-U_\Sigma(B)]\), namely
\[
 C_U\left[y^{1/3}\sum_{k\le K}k^{-1/3}-KB^{1/3}\right]
       +O\big(y^{3/10}K^{7/10}+KB^{3/10}\big).
\]
The last error is \(O(yB^{-7/10})\). For \(s=1/3\), \(\sum_{k\le K}k^{-s}=K^{1-s}/(1-s)+\zeta(s)+O(K^{-s})\).
To identify the constant, subtract \(\int_k^{k+1}v^{-s}dv\) in each term. The resulting series converges locally uniformly on \(\Re s>0\) by the first derivative bound, and after adding \(-1/(1-s)\) agrees with \(\zeta(s)\) on \(\Re s>1\). Its tail is \(O(K^{-s})\) for real \(s>0\). Replacing \(K\) by \(y/B\) in the two power terms changes them by \(O(B^{1/3})\), at which point they give \(\tfrac12 yB^{-2/3}\), canceling the first-part term. The remaining \(O(B^{1/3})\) errors are smaller than \(O(y^{5/12})\). This proves (9). Also \(\zeta(1/3)<0\), since summing the integral comparison on \([k-1,k]\) gives \(\sum_{k\le K}k^{-s}-K^{1-s}/(1-s)\le 1-1/(1-s)<0\) at \(0<s<1\).

Fix \(A=\lfloor X^{1/14}\rfloor\) on the taper and write \(a(m)=t(m)\mathbf1_{m\le A}\), \(b=t-a\), \(h_A=\sum_{m\le A}t(m)/m\). The exact finite convolution identity is
\[
 t=2a-f*a*a+f*b*b .
\]
Indeed \(f*b*b-f*a*a=f*(t-2a)*t=t-2a\). The short rectangle in its prefix sum is \(\sum_{a_1,a_2\le A}t(a_1)t(a_2)F(n/(a_1a_2))\). The linear part of (9) gives \(nU(1)h_A^2\). The cubic part is
\(C_U\zeta(1/3)n^{1/3}\big(\sum_{m\le A}t(m)m^{-1/3}\big)^2\).
Its contribution after subtracting the rectangle is nonnegative, with size \(O(X^{1/3}A^{4/3})=O(X^{3/7})\). The remaining rectangle error is
\(O(X^{5/12}A^{7/6})=O(X^{1/2})\), using \(|t(m)|\le1\) in the two sums. The term \(2T(A)\) is \(O(X^{1/14})\).

For the large rectangle, let \(r_k=\lfloor\sqrt{n/k}\rfloor\), \(D_A(m)=T(m)-T(A)\), and define
\[
 \begin{split}
 d_A(n,j)&=\sum_{\substack{a_1\mid j\\ A<a_1\le n/j}}
                        f(j/a_1)t(a_1),\\
 \mathcal L_A(n)&=2\sum_{1\le j\le n/(A+1)}
                          d_A(n,j)D_A(\lfloor n/j\rfloor),\\
 \mathcal S_A(n)&=\sum_{1\le k\le n/(A+1)^2} f(k)D_A(r_k)^2 .
 \end{split}
\]
For each \(k\), one coordinate of a pair \(a_1,a_2>A\), \(ka_1a_2\le n\), is at most \(r_k\). The intersection of the two orientations is the entire square \(A<a_i\le r_k\). Subtract its square of the signed mass, and substitute \(j=ka_1\) in the first orientation. The retained condition \(a_1\le r_k\) is \(a_1j\le n\), including equality. This proves uniformly on the taper
\[
 T(n)=\mathcal L_A(n)-n U(1)h_A^2-\mathcal S_A(n)+O(\sqrt X).       \tag{10}
\]
Both explicit squares have nonpositive signs. Each smaller signed state in the linear term and in the squares comes from the same \(t\). For \(1<j\le\sqrt n\), \(d_A(n,j)=-\sum_{a_1\mid j,\,a_1\le A}f(j/a_1)t(a_1)\) by \(f*t=\delta_1\). In particular it is \(-f(j)\) if all prime factors of \(j\) exceed \(A\), and equals \(-1\) at each prime \(A<p\le\sqrt n\), in both classes. At such a prime the linear evaluation is at \(\lfloor n/p\rfloor\), which can exceed \(\sqrt n\). Every evaluation inside an overlap square uses \(r_k\le\sqrt n\).

Let \(\mathcal Z_A=\mathcal L_A-nU(1)h_A^2-\mathcal S_A\). Equations (1) and (10) yield
\[
 \|G_7+C_z-\mathcal Z_A\|_w^2\ll_\epsilon X^{2+\epsilon}.
\]
This transfers the entire signed amplitude, including the mixed terms of its energy. For one-sided energy, \((\mathcal Z_A)_+\le(\mathcal L_A)_+\), and the inherited one-sided \(T\) criterion makes an all-epsilon bound \(\|(\mathcal L_A)_+\|_w^2\ll_\epsilon X^{2+\epsilon}\) sufficient for the complete \(Q_7\) bound. In detail, with \(w=1\) on the dyadic block this bound and (10) give \(O_\epsilon(X^\epsilon)\) for the block energy of \(T_+\) with weights \(1/[n(n+1)]\). Summing over blocks meeting \([Y,Y^2)\) yields \(O_\epsilon(Y^{2\epsilon}(1+\log Y))\) there. For every fixed required \(r\) choose \(2\epsilon<1/r\) and take \(Y\) sufficiently late in the one-sided criterion. The estimate for \(\mathcal L_A\) remains **O**. The exact signs in (10) identify both penalties and the linear columns, including the ones with evaluation at arguments beyond those used by any overlap square.

## Scope and evidence

**Candidate-D.** The recurrence (6) absorbs the net repeated split pairs in the all-block estimate, with a strict contraction at the arithmetic critical norm. Formula (8) gives the still nonzero combined drift of the all-prime sector. Formula (10) retains the two signed squares with the actual inverse weights and bounds the short-rectangle remainder at square-root scale. **O.** A power bound for the joint \(\mathcal J_z\) of (4), or for the complete signed profile in (10), remains open.

- [Frozen arithmetic-kernel draft 6649670532e4d69858bc92994a55a54682f5d619](https://github.com/mathorn1973/twist-j/tree/6649670532e4d69858bc92994a55a54682f5d619/notes/C-RH-ARITHMETIC-KERNEL-N). Read FOUNDATION §§2–3, round 4 CRITICAL-UNIT §§1–2, round 6 CUBE-ROOT-TRANSFER §§1–3 and BALANCED-UNIT-TAIL §§1–2, and round 7 REPORT §§1–3 and PRIME-PUSHFORWARD §§1–3. The unit counts, frozen taper comparison, two moments and unconditional cancellation of \(T\) are used at their stated scopes.
- [Neighbor draft ceb77e3632ec4617c54d8e1fd504d3b1c99dd106](https://github.com/mathorn1973/twist-j/tree/ceb77e3632ec4617c54d8e1fd504d3b1c99dd106/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N). Read FULL-COUPLED-ENERGY, FULL-LEVELS and FULL-ENERGY-REVIEW. The first contains the Möbius orientation and its overlap square. Formula (10) transfers that structure to the distinct inverse weights of \(t\). The neighbor retains owner [#2091](https://github.com/mathorn1973/twist-j/issues/2091) and draft [#2093](https://github.com/mathorn1973/twist-j/pull/2093).
- [Tomohiro Yamada, Explicit formulae for primes in arithmetic progressions, I, §1](https://arxiv.org/html/1306.5322v4#S1). Read the fixed-modulus prime number theorem and classical error statement in §1, already attributed by round 7. Partial summation at modulus five yields the reciprocal-prime estimate in (6) and cumulative count estimate in (8).

Paper algebra and estimates only. No numerical, symbolic or scientific executable, Git mutation, or formal runner was performed in this lane. The public authority checks and prerequisite readback were completed by the same session owner before this paper lane was delegated. The new deductions are subject to same-session cross-review.
