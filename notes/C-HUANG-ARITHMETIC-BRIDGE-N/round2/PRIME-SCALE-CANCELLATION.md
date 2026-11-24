# Prime-direction filters and the cost of returning to the signed sum

**NON-CANONICAL. Authority none. Action layer NOT_APPLICABLE.**
The exact identities, norm estimates and stated obstruction are candidate-D.
The original complete-window energy estimate remains O.
The scope is recorded in [SCOPE.md](SCOPE.md).

All prefix sums below are extended to real arguments by the defining
inequalities and vanish below one. For \(p\) prime write
\(T_p F(x)=F(x/p)\). For a finite prime set \(S\), put
\(P=\prod_{p\in S}p\) and
\(A_S(x)=\sum_{d\le x,\,(d,P)=1}\mu(d)\).
The positive and negative boundary directions are combined before
taking any positive part.

## Two prime directions and an actual cancellation

**Candidate-D.** Partition each squarefree integer by its selected
prime factors. This gives
\[
 M(x)=\sum_{s\mid P}\mu(s)A_S(x/s)
     =\prod_{p\in S}(I-T_p)A_S(x). \tag{1}
\]
For \(S=\{2,3\}\), the kernel attached to the coefficient \(\mu(d)\),
where \((d,6)=1\), is
\[
 K_d(x)=\mathbf1_{[d,2d)}(x)-\mathbf1_{[3d,6d)}(x).
\]
The two intervals each have length \(\log 2\) in logarithmic
coordinates. Thus \(\int K_d(x)\,dx/x=0\) on the full support.
The two pulses have unequal integrals against the critical amplitude
weight \(dx/x^{3/2}\). In fact
\[
 \int_0^\infty K_d(x)\frac{dx}{x^{3/2}}
   =\frac2{\sqrt d}(1-2^{-1/2})(1-3^{-1/2})>0.
\]
A window may also cut either pulse at an interior point.

Let \(\pi_{>3}(x)\) count primes \(q>3\) through \(x\). The term in
(1) from those coprime cores is
\[
 M_{\rm prime}(x)=
 -\pi_{>3}(x)+\pi_{>3}(x/2)+\pi_{>3}(x/3)-\pi_{>3}(x/6)
 \sim-\frac{x}{3\log x}. \tag{2}
\]
For \(q\in(x/6,x/3]\) the negative pulse gives \(+\!1\) after
multiplication by \(\mu(q)=-1\). These are the positive-splice
matching witnesses of [PRIME-RULES.md](../PRIME-RULES.md).
The earlier pulse for \(q\in(x/2,x]\) gives \(-1\). The prime number
theorem yields (2) by taking the two interval counts on the same
argument. The proportional densities are \(1/6\) and \(1/2\),
respectively.
[Björner, Theorem 2.3(b), \(k=1\)](https://arxiv.org/pdf/1101.5704).

For the complementary coprime stratum, consisting of the unit and
composite cores, its filtered contribution is \(M-M_{\rm prime}\).
The inherited unconditional bound \(M(x)=o(x/\log x)\) therefore
gives
\[
 M_{\rm unit,comp}(x)\sim+\frac{x}{3\log x}. \tag{3}
\]
Consequently the positive part of this complementary sector alone
has energy \(\gg Y^{3/2}/(\log Y)^2\) on every sufficiently late
complete window, with the original weights \(1/[N(N+1)]\).
Each summand for large \(N\) is \(\gg 1/(\log N)^2\), and the
window contains \(\gg Y^{3/2}\) integers. Equations (2) and (3)
exhibit an actual leading cancellation across the two coprime
strata. Treating the complementary positive sector by itself
loses that cancellation.
[Inherited classical Mertens bound](https://github.com/mathorn1973/twist-j/blob/ceb77e3632ec4617c54d8e1fd504d3b1c99dd106/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N/FULL-COUPLED-ENERGY.md).

## Critical norm, inverse cost and translated windows

**Candidate-D.** Write \(f_F(t)=e^{-t/2}F(e^t)\).
For a step prefix \(F\) and integers \(1\le L<U\),
\[
 \int_{\log L}^{\log U}|f_F(t)|^2\,dt
  =\sum_{N=L}^{U-1}\frac{|F(N)|^2}{N(N+1)}.
\]
The same identity holds for positive parts. The original complete
integer windows take \(L=\lceil Y\rceil\) and \(U=\lceil Y^{3/2}\rceil\).
Conjugation of \(T_p\) gives \(p^{-1/2}\tau_{\log p}\) on the log
line, where \(\tau_a f(t)=f(t-a)\). The multiplier of (1) is
\[
 D_S(\xi)=\prod_{p\in S}(1-p^{-1/2}e^{-i\xi\log p}).
\]
On the entire \(L^2(\mathbb R)\) space its inverse norm is exactly
\[
 K_S=\prod_{p\in S}(1-p^{-1/2})^{-1}. \tag{4}
\]
The triangle inequality gives the lower bound \(|D_S|\ge K_S^{-1}\),
with equality at zero frequency. Continuity gives the same bound
for the essential infimum. The forward norm is at most
\(\prod_{p\in S}(1+p^{-1/2})\le K_S\). These are full-line
operator estimates. The arithmetic identities hold locally for
prefix sums without any full-line integrability assumption.

Let \(\mathcal S(P)\) consist of the positive integers whose prime
factors are all in \(S\), including \(1\). The exact reconstruction is
\[
 A_S(x)=\sum_{\substack{a\in\mathcal S(P)\\a\le x}}M(x/a),
 \qquad
 K_S=\sum_{a\in\mathcal S(P)}a^{-1/2}. \tag{5}
\]
The first equality follows by the finite geometric expansion
at each argument \(x\), with terms below one vanishing. Hence for
any bounded log interval \(J\),
\[
 \|(f_{A_S})_+\|_{L^2(J)}
 \le\sum_{a\in\mathcal S(P)}a^{-1/2}
              \|(f_M)_+\|_{L^2(J-\log a)}. \tag{6}
\]
The terms vanish when the translated interval is entirely below
zero. The corresponding two-sided bound follows by absolute
values. On the arithmetic scale these are intervals divided by
\(a\), with fractional endpoint cells in the weighted integral
when the new endpoints are nonintegers. An estimate solely on
\(J\) does not control this union. Even for one prime, a
nonnegative input supported just to the left of \(J\) can have a
nonzero inverse image on \(J\). The forward filter also does not
yield one-sided domination by the input's positive part. A
nonpositive bump to the left of \(J\) gives a positive delayed
term on \(J\) under \(I-p^{-1/2}\tau_{\log p}\). These examples
concern inference from the filter alone.

For \(S=\{p:p\le y\}\), partial summation of the prime number
theorem gives
\[
 \log K_S=\sum_{p\le y}p^{-1/2}
          +O\!\left(\sum_{p\le y}p^{-1}\right)
          \sim\frac{2\sqrt y}{\log y}.
\]
Indeed the partial-summation endpoint is asymptotic to
\(\sqrt y/\log y\), and its integral term has the same asymptotic
by differentiation of \(2\sqrt y/\log y\). The error is at most
\(O(\log y)\) by the harmonic bound. At \(y=(\log X)^2\) the
inverse norm is \(X^{o(1)}\). At \(y=(\log X)^{2+\delta}\) for
fixed \(\delta>0\), the full-line inverse norm exceeds \(X^B\)
for every fixed \(B\) as \(X\to\infty\). A subpower inverse norm
at the former scale still requires control over the translated
windows in (6), including the earlier scales when \(S\) is reset
with the original block.

## Reconstruction on the complete two-factor region

**Candidate-D.** Freeze \(T=T_X\) on the slab as in the inherited
transfer and keep \(S\) fixed for the reconstruction on that
slab. Set
\[
 \begin{split}
 C^{(P)}_{A,B}(x)&=\sum_{\substack{a>A,\ b>B,\ ab\le x\\(ab,P)=1}}
   \mu(a)\mu(b)\left\lfloor\frac{x}{ab}\right\rfloor,\\
 h_A^{(P)}&=\sum_{\substack{d\le A\\(d,P)=1}}\frac{\mu(d)}d .
 \end{split}
\]
Write each of the original factors uniquely as its squarefree
selected-prime divisor times its coprime core. There is no
restriction against a selected prime appearing in both original
factors. With the original \(C_T,h_T\) this gives
\[
 C_T(n)=\sum_{s,t\mid P}\mu(s)\mu(t)
 C^{(P)}_{T/s,T/t}(n/(st)),\qquad
 h_T=\sum_{s\mid P}\frac{\mu(s)}s h^{(P)}_{T/s}. \tag{7}
\]
The lowered bounds in the core variables are forced by the
strict original bounds on both factors. For example, replacing
\(T/s,T/t\) by \(T,T\) omits the two strips with exactly one
core in its interval \(T/s<a\le T\) or \(T/t<b\le T\)
and the rectangle with both cores in those intervals.
The floor condition \(ab\le n/(st)\) still applies in each
piece, including its endpoints.

In particular the centered expression is exactly
\[
 \begin{split}
 G_X(n)&=C_T(n)-(n+1/2)h_T^2\\
 &=\sum_{s,t\mid P}\mu(s)\mu(t)
 \left[C^{(P)}_{T/s,T/t}(n/(st))
  -\frac{n+1/2}{st}h^{(P)}_{T/s}h^{(P)}_{T/t}\right]. \tag{8}
 \end{split}
\]
The intercept in the bracket is \(1/(2st)\). Centering each
rescaled prefix at \(n/(st)+1/2\) changes the intercept and
requires a correction. Linearity of the original forward
average gives \(U_H^JG_X(N)=U_H^J C_T(N)-L_X(N)h_T^2\), since
\(U_H^J(n+1/2)=L_X(N)\). Both lower strips and the full negative
square thus survive prime-direction grouping. Setting all core
cutoffs to the same value would produce a square of the
single-prime filter with a different input. Formula (8)
records the terms required to use that simplification.

The neighboring arithmetic-kernel contraction has a repeated
term of coefficient \(-2\) only at split-prime squares after
its single-mark regrouping. Here (7) has Möbius squarefree
weights separately on \(s\) and \(t\), and therefore coefficient
\(+1\) at \(s=t=p\) before any regrouping, for every selected
prime \(p\). The strip thresholds and the negative square in
(8) are retained. The neighbor's contraction and its two
squares apply to its own prefix and inverse coefficients.
[Neighboring coupled cuts, Sections 1–2 and 4](https://github.com/mathorn1973/twist-j/blob/6a91ef48f6454743797614503aa5863dde54befb/notes/C-RH-ARITHMETIC-KERNEL-N/round8/COUPLED-CUTS.md).

**O.** With \(T_X=\lfloor X^{1/4}\rfloor\) a sufficient estimate
is the original subpower bound, for every required exponent
and on its arbitrarily late complete windows, for the positive
energy of the *joint averaged sum* in (8). The inherited comparison
to \(R_{1/36}\) transfers this estimate with the original
weights. The inverse filter estimate controls an unsigned norm
cost, and (2)–(3) exhibit cancellation at a coarser scale.
Neither yields that bound for (8).
[Inherited signed transfer](https://github.com/mathorn1973/twist-j/blob/ceb77e3632ec4617c54d8e1fd504d3b1c99dd106/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N/FULL-COUPLED-ENERGY.md).
