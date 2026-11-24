# The short-sum price of narrowing the retained frequencies

**NON-CANONICAL. Authority none.** The estimates are **candidate-D**.
The positive whole-window target is **O**. Action layer
NOT_APPLICABLE. This is an unconditional paper argument for
C-RH-THREE-INTERFACE-SYNTHESIS-N, owner #2091, draft #2093.

Use the exact slab coefficients, \(D,D_1,J,H\), and weight \(w_N=1/[N(N+1)]\)
in [PRIME-CANCELLATION.md](PRIME-CANCELLATION.md). Write \(H_0=H\).
For fixed \(B\ge1\), put \(H_B=\lceil\sqrt X(\log X)^B\rceil\).
Define \(T_h\) by the frozen formula with \(H_0\) replaced by \(h\),
both in the forward average and in the retention \(0<\|\theta\|<1/h\).
Keep \(A,c,b,D,D_1,J,h_X\) fixed on the slab. Its affine term is
\(-(N+1/2+J(h-1)/2)h_X^2\). In particular \(T_{H_0}=T_{\rm low}\).

**Candidate-D.** For each fixed \(B\ge1\) and \(K>0\), on every
sufficiently late complete integer window \(I(Y)=[Y,Y^{3/2})\cap\mathbb Z\),
\[
 \left(\sum_{N\in I(Y)}w_N|T_{H_B}(N)-T_{\rm low}(N)|^2\right)^{1/2}
      \ll_{B,K}(\log Y)^{-K}.                                  \tag{1}
\]
In each summand the width is set by the dyadic slab containing \(N\).
The narrower carrier uses the actual signed coefficients and includes
its averaged drift.

## 1. The actual smoothing error

For integer \(L\ge1\) put
\[
 W(n,L)=\max_{0\le s\le L}
             \left|\sum_{n<m\le n+s}\mu(m)\right|,
\]
with integer \(s\). Use Matomäki, Radziwiłł, Shao, Tao and Teräväinen,
*Higher uniformity of arithmetic functions in short intervals II.
Almost all intervals*, Theorem 1.1(i), with a fixed filtered circle and
constant function one. Their starred sum in (1.4) includes all
integer interval prefixes as arithmetic progressions. If \(\eta>0\)
is fixed and \(X^{1/3+\eta}\le L\le X^{1-\eta}\), their theorem bounds
the maximum over prefixes by \(L(\log X)^{-C}\) outside an exceptional
set of real starts of measure \(O_{C,\eta}(X(\log X)^{-C})\), for every
fixed \(C>0\).
[Theorem 1.1(i) and its starred sum](https://link.springer.com/article/10.1007/s00222-026-01408-6).

For \(x\in[n,n+1)\) the integers in \((x,x+L]\) are exactly
\(\{n+1,\ldots,n+L\}\). The maximum over their prefixes is constant
throughout that unit cell. Integrating its square over all cells in
\([X,2X)\), using \(W\le L\) on the exceptional starts, gives
\[
 \sum_{X\le n<2X}W(n,L)^2\ll_{C,\eta} XL^2(\log X)^{-C}.        \tag{2}
\]
This conversion includes every integer start and all prefixes that
extend past \(2X\).

For integer width \(h\) put \(L_h=J(h-1)\). Let \(p_h(s)\) be the mass
of the sum of \(J\) independent discrete uniform variables on
\(\{0,\ldots,h-1\}\). Then
\[
 U_h^J M(N)-M(N)
   =\sum_{s=0}^{L_h}p_h(s)\sum_{N<m\le N+s}\mu(m).
\]
Its absolute value is at most \(W(N,L_h)\), which controls all the
translates simultaneously. For both \(h=H_0\) and \(h=H_B\), using
\(w_N\le X^{-2}\) gives
\[
 \sum_{X\le N<2X}w_N|U_h^JM(N)-M(N)|^2
       \ll_C \frac{L_h^2}{X}(\log X)^{-C}.                     \tag{3}
\]
Here \(L_h=X^{1/2}(\log X)^{O_B(1)}\). A single fixed \(\eta\), for
example \(1/12\), is valid on late slabs. Since \(C\) is arbitrary,
(3) gives inverse powers of \(\log X\) of every fixed order.
For \(h=\lceil X^{1/2+\delta}\rceil\) with fixed \(0<\delta<1/2\),
the same argument with a suitable \(\eta\) gives the explicit
squared smoothing allowance \(O_{\delta,C}(X^{2\delta}(\log X)^{2-C})\).
That allowance retains a positive power for every fixed \(C\).

## 2. Comparing the entire signed carriers

Write \(\Pi_{\le D_1}\) for projection onto the nonzero harmonics with
reduced denominator at most \(D_1\). Put
\[
 S=\sum_{d\le D}b_d\psi_d+
         \Pi_{\le D_1}\sum_{d>D}b_d\psi_d,\qquad
 E_h=\Pi_{\|\theta\|\ge1/h}(1-\Pi_{\le D_1})
             U_h^J\sum_{d>D}b_d\psi_d .
\]
For both widths, \(N+L_h\le3X\) on late slabs. Averaging the centered
identity on those arguments gives the exact equality
\[
 T_h=U_h^J M-U_h^J S-E_h.                                      \tag{4}
\]
The affine term in (4) comes from the same mass \(p_h(s)\).

The multiplier \(m_h(\theta)=h^{-1}\sum_{j=0}^{h-1}e(j\theta)\),
where \(e(t)=\exp(2\pi it)\), obeys
\[
 |m_h(\theta)|\le2/5\quad\text{if }h\|\theta\|\ge1.
\]
Its modulus is \(|\sin(\pi ht)|/(h\sin(\pi t))\) for
\(t=\|\theta\|\in(0,1/2]\). For \(1\le ht\le5/4\) the numerator
is at most \(\sqrt2/2\) and the denominator is at least \(2ht\).
For \(ht\ge5/4\) use numerator at most one and the same denominator
bound. By the \(O(X(\log X)^2)\) total absolute Fourier coefficient
bound in the prime note,
\[
 \|E_h\|_\infty\ll X(\log X)^2(2/5)^J
                 =X^{1-\log_2(5/2)}(\log X)^2.                \tag{5}
\]

Set \(L=\max(L_{H_B},L_{H_0})\). The probability representation
and \(|e(s\theta)-1|\le2\pi s\|\theta\|\) imply
\[
 |m_{H_B}(\theta)^J-m_{H_0}(\theta)^J|
       \ll \min(1,L\|\theta\|).
\]
Every frequency of \(S\) has reduced denominator \(q\le D\).
At \(\theta=r/q\) in lowest terms put \(v=\min(r,q-r)\).
The coefficient of \(S\) there is \(O_\epsilon(X^\epsilon\log X/v)\).
Indeed the common factor \(|1-e(-r/q)|^{-1}\) is \(O(q/v)\) and
the sum of the absolute denominator contributions is bounded by
\[
 \sum_{\substack{d\le4A^2\\q\mid d}}\frac{|b_d|}{d}
     \ll_\epsilon X^\epsilon(\log X)/q .
\]
Here \(|b_d|\le\tau(d)\ll_\epsilon d^\epsilon\) and each raw
denominator occurs at most once at a given frequency of \(S\).
The divisor bound follows by bounding \(k+1\) by \(p^{k\epsilon}\)
for every \(k\ge1\) at sufficiently large primes, and taking the
finite product of the bounds at the remaining primes.

For the squared coefficient sum after multiplying by the difference
of multipliers, enlarge to all \(1\le r<q\). Splitting at \(v=q/L\)
gives
\[
 \sum_{1\le v\le q/2}\frac{\min(1,Lv/q)^2}{v^2}
     \ll \min(1,L/q),\qquad
 \sum_{q\le D}\min(1,L/q)\ll L\log(2D).
\]
The squared coefficient mass is thus
\(O_\epsilon(X^{2\epsilon}L(\log X)^3)\). Distinct reduced frequencies
of denominator at most \(D\) have circular separation at least
\(D^{-2}\). The separated-frequency estimate of the prime note gives
\[
 \sum_{X\le N<2X}w_N |(U_{H_B}^J-U_{H_0}^J)S(N)|^2
 \ll_\epsilon
   \frac{X+D^2}{X^2}\,X^{2\epsilon}L(\log X)^3
 \ll_{B,\epsilon}X^{-1/6+2\epsilon}(\log X)^{B+4}.             \tag{6}
\]
Fix \(0<\epsilon<1/12\). Equations (3) through (6) now give
weighted norm at every fixed inverse-logarithmic order on a
whole slab. A complete integer window meets \(O(\log Y)\) slabs,
each with \(Y/2<X<Y^{3/2}\). Restrict the squared bounds to
the intersections, including both end fragments, and increase
the exponent in (3) by a fixed amount to obtain (1).

## 3. What the one-sided estimate still requires

The positive part is 1-Lipschitz, so (1) gives
\(\left|\sqrt{Q_{T_{H_B}}(Y)}-\sqrt{Q_{T_{\rm low}}(Y)}\right|
\ll_{B,K}(\log Y)^{-K}\). Together with the prime note this preserves
the \(O((\log Y)^2)\) comparison with \(\sqrt{Q_R(Y)}\).
In either direction use source exponent \(2r\) and absorb the norm
error to preserve the target that each \(r\ge1\) admits arbitrarily
late integer \(Y\) with \(Q^r\le Y\).

For a nonnegative real test \(f_N\) on a slab, write
\(m_f=\sum_N w_Nf_N\). The exact subtraction from its oscillatory pairing,
\[
 h_X^2\sum_N w_N f_N(N+1/2+J(h-1)/2),
\]
lies between \(Xh_X^2m_f\) and \(3Xh_X^2m_f\) on late slabs.
The test Fourier coefficient has modulus at most \(m_f\).
In the slowest allowed band there is no uniform gain in this
last bound based on positivity alone. Take \(\theta=1/A^2\),
which has \(q>D,D_1\) and \(0<\|\theta\|<1/H_B\) on late slabs.
With \(N_*=(3X-1)/2\), one has
\[
 \Re\left(e(-N_*\theta)\sum_N w_N f_Ne(N\theta)\right)\ge m_f/2
\]
since \(|2\pi(N-N_*)/A^2|\le\pi/3\) throughout the slab. In
particular a hypothetical term \(P\cos(2\pi(N-N_*)/A^2)\)
has positive residual at least \(P/4\) throughout the slab
if \(P\ge12Xh_X^2\) and \(P>0\). The example concerns the
allowed frequency range and positive tests. It assigns no
amplitude or phase to the actual coefficient at \(1/A^2\).

**O.** A bound on the actual signed oscillatory pairing against
positive tests with the drift subtracted is still required.
Equation (3) bounds changes of \(M\) under averaging. Equation (1)
bounds the change of the entire carrier under logarithmic narrowing.
The classical Mertens bound in [ROUND3-REVIEW.md](ROUND3-REVIEW.md)
and the same-window comparison give the subexponential improvement
to the full positive energy on every late window, with leading
power \(Y^{3/2-o(1)}\). The required arbitrarily small power for
the full retained positive energy remains open.
