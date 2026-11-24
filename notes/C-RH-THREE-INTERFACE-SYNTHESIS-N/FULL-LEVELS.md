# Positive energy of the full levels

**NON-CANONICAL. Authority none.** The deductions below are **candidate-D**.
The positive whole-window target is **O**. Action layer NOT_APPLICABLE.
This is a paper argument for C-RH-THREE-INTERFACE-SYNTHESIS-N, owner
[#2091](https://github.com/mathorn1973/twist-j/issues/2091), draft
[#2093](https://github.com/mathorn1973/twist-j/pull/2093).

## Weighted block means recover the energy with additive error

Use the fixed `1/36` residual \(R\), \(I(Y)=[Y,Y^{3/2})\cap\mathbb Z\),
\(w_N=1/[N(N+1)]\), and \(Q_F(Y)=\sum_{N\in I(Y)}w_N F(N)_+^2\)
from [WINDOW-BOUND.md](WINDOW-BOUND.md). Given fixed \(B\ge1\), intersect
\(I(Y)\) with each dyadic slab \([X,2X)\). Starting at the first integer
of each nonempty intersection, partition it into consecutive blocks of
length \(L=\lfloor\sqrt X(\log X)^B\rfloor\), with a possibly shorter
last block. Keep all integers of both end slabs. For a block \(I=[a,b]\)
write
\[
 w(I)=1/a-1/(b+1),\qquad
 m_I(F)=\frac{1}{w(I)}\sum_{N\in I}w_N F(N),\qquad
 S_F(Y)=\sum_Iw(I)m_I(F)_+^2.
\]
Let \(P\) be the weighted orthogonal projection onto functions constant
on these blocks. For \(f(t)=t_+^2\), the derivative \(f'(t)=2t_+\)
is 2-Lipschitz and \(f\) is convex. Thus
\[
 0\le f(u)-f(v)-f'(v)(u-v)\le (u-v)^2.
\]
The linear terms sum to zero on each block at \(v=m_I(F)\). Consequently
\[
 0\le Q_F(Y)-S_F(Y)\le \|(1-P)F\|_{I(Y)}^2.                    \tag{1}
\]
The estimate is additive in the energy and needs no bound on the block
levels.

For \(N,K\) in the same block, define the integer-prefix maximum
\(W(n,L)=\max_{0\le s\le L}|M(n+s)-M(n)|\). If \(K\ge N\),
the difference of the two levels is at most \(W(N,L)\). If \(K<N\),
subtract both levels from \(M(N-L)\) to get the bound \(2W(N-L,L)\).
Averaging in \(K\) with weights \(w_K/w(I)\) proves
\[
 |M(N)-m_I(M)|\le W(N,L)+2W(N-L,L).                              \tag{2}
\]
Use the all-start short-interval theorem in
[ONE-SIDED-LOW.md](ONE-SIDED-LOW.md), Section 1, credited there to
Matomäki, Radziwiłł, Shao, Tao and Teräväinen, Theorem 1.1(i).
[Primary source](https://link.springer.com/article/10.1007/s00222-026-01408-6).
For a fixed \(\eta\), for instance \(1/12\), this \(L\) lies in
the theorem range on both \([X,2X)\) and \([X/2,X)\) for late slabs.
Those two ranges contain all the starts in (2). Their squared sums are
\(\ll_A XL^2(\log X)^{-A}\) for every fixed \(A>0\). With \(w_N\le X^{-2}\)
this gives \(O_{A,B}((\log X)^{2B-A})\) on each slab, including any
window fragment. There are \(O(\log Y)\) slabs and their logarithms
are comparable to \(\log Y\). Hence for every \(K>0\),
\[
 \|(1-P)M\|_{I(Y)}^2\ll_{B,K}(\log Y)^{-K}.                       \tag{3}
\]
This uses the starts at every \(N\) and \(N-L\) to apply the all-start
square bound directly.

A shorter partition gives power precision for \(M\). For fixed
\(1/3<\theta<1/2\), use \(L=\lfloor X^\theta\rfloor\) and fix
\(0<\eta<\min(\theta-1/3,1-\theta)\). The same two ranges give a
squared error \(\ll_{\theta,A} X^{2\theta-1}(\log X)^{-A}\) on each
slab. Summing the geometric decay over slabs gives
\(\|(1-P)M\|_{I(Y)}^2\ll_{\theta,A}Y^{2\theta-1}(\log Y)^{-A}\)
for that partition. This is accuracy of the retained means in
reconstructing the energy in (1).


The bound on \(\|M-R\|_{I(Y)}^2\) in
[WINDOW-BOUND.md](WINDOW-BOUND.md), equation (5), tends to zero faster
than every inverse logarithm. Orthogonal projection and its complement
are contractions. It follows from (1) and (3) that for both \(F=M\) and
\(F=R\),
\[
 0\le Q_F(Y)-S_F(Y)\ll_{B,K}(\log Y)^{-K}
\]
on every sufficiently late complete window. In addition,
\(|\sqrt{S_R(Y)}-\sqrt{S_M(Y)}|\le \|M-R\|_{I(Y)}\).
Thus the target, with every integer \(r\ge1\) and arbitrarily late
integer \(Y\), is equivalent to the same target for \(S_M(Y)\).
For a required integer exponent \(r\), use the source condition with
\(2r\) in place of \(r\), then absorb the norm error and fixed constants.

The exact Möbius expression for each retained level is
\[
 w(I)m_I(M)
   = w(I)M(a-1)+\sum_{n=a}^{b}\mu(n)
                         \left(\frac1n-\frac1{b+1}\right).       \tag{4}
\]
Indeed \(M(N)=M(a-1)+\sum_{a\le n\le N}\mu(n)\) in the block,
and the inner weight telescopes. The large term that short increments
leave undetermined is the retained signed level.

## Upper tails and the positive dual

Use the normalized levels \(d_I=m_I(M)/\sqrt a\), weights \(q_I=a w(I)\),
and distribution \(D_Y(t)=\sum_{I:d_I>t}q_I\).
Then \(S_M(Y)=\sum_I q_I(d_I)_+^2=2\int_0^\infty tD_Y(t)\,dt\).
Also \(\sum_Iq_I\le\sum_{N\in I(Y)}1/(N+1)=O(\log Y)\).
Since \(b<2a\) and \(M(N)\le N\), one has \(d_I\le2Y^{3/4}\).
Define \(V(Y)=\sup_{t\ge1}t^2D_Y(t)\). The exact tail formula gives
\[
 V(Y)\le S_M(Y)\ll (1+V(Y))\log Y.                              \tag{5}
\]
For the upper bound integrate separately on \(0<t<1\) and
\(1\le t\le 2Y^{3/4}\). Thus a sufficient and necessary estimate for
the target is that for each fixed \(\epsilon>0\) and every \(Y_0\)
there is an integer \(Y\ge\max(11,Y_0)\) with
\(D_Y(t)\le Y^\epsilon/t^2\) simultaneously for all \(t\ge1\).
For the implication to the stated target one applies this at a smaller
\(\epsilon\) than \(1/r\) and takes \(Y_0\) sufficiently large. For
necessity choose an integer \(r\) with \(1/r<\epsilon\), with room
for the norm comparison. The estimate quantifies only over arbitrarily
late windows.

For the exact full dual, let \(U=\lceil Y^{3/2}\rceil-1\). The
weighted norm of \(M_+\) on this window equals
\[
 \sup_{\substack{v_N\ge0\\ \sum_{N=Y}^U w_Nv_N^2\le1}}
       \sum_{n=1}^U\mu(n)g(n),
 \qquad
 g(n)=\sum_{N=\max(n,Y)}^U w_N v_N.
\]
This follows by interchanging the two finite sums and taking the
norming function proportional to \(M_+\) when that norm is positive.
The tests \(g\) are exactly the nonincreasing functions constant on
\(1\le n\le Y\), with \(g(U+1)=0\) and
\[
 \sum_{n=Y}^U n(n+1)|g(n)-g(n+1)|^2\le1.
\]
The inverse is \(v_n=n(n+1)(g(n)-g(n+1))\). The plateau contributes
\(M(Y-1)g(Y)\) to the pairing. Every nonzero admissible test has
\(g(Y)>0\). In particular a condition forcing \(g(Y)=0\) removes
the full cone. On the reduced set of block-constant \(v\) the exact
dual is \(\sqrt{S_M(Y)}\) by the same weighted norming argument.
The difference between the two suprema is at most
\(\|(1-P)M\|_{I(Y)}\) by Cauchy–Schwarz. This restriction retains
nonnegative tests and approximates the true supremum, including
its plateau contribution.

## Limits of the short-increment and classical-size inputs

For any \(c>0\), put \(\Phi(x)=(\log x)^{3/5}(\log\log x)^{-1/5}\),
and for sufficiently large integers \(n\) define
\[
 A(n)=\left\lfloor n e^{-c\Phi(n)}\sin(\log n)\right\rfloor .
\]
Write \(F(x)\) for the expression before taking the floor.
Since \(x\Phi'(x)\to0\), differentiation gives
\(|F'(x)|\ll_c e^{-c\Phi(x)}\). In particular the integer increments
are in \(\{-1,0,1\}\) eventually. The finite initial segment can be
filled from \(A(0)=0\) with increments in the same set because
\(|A(n)|\le n\) at the joining integer. The sequence obeys the
classical size envelope \(|A(n)|\ll n e^{-c\Phi(n)}\). For
\(X\le n<2X\) and \(1\le L\le X\), the maximum prefix increment
is at most \(1+C_c L e^{-c\Phi(X)}\), by monotonicity of \(\Phi\)
for large \(X\). In the same power-length range as the Möbius theorem
this implies its all-start squared bound of every fixed inverse-log
order, even with a bound at each start.

Nevertheless \(Q_A(Y)\gg_c Y^{3/2}e^{-2c\Phi(Y^{3/2})}\) for
every sufficiently large \(Y\). Put \(T=Y^{3/2}\).
The interval \([\log T-2\pi,\log T]\) contains a subinterval of
length at least \(\pi/3\) on which \(\sin(t)\ge 1/2\). A full
period contributes total length \(2\pi/3\) in at most two pieces.
Exponentiating gives an interval of length \(\gg T\) inside
\([e^{-2\pi}T,T]\). Discard a possible endpoint at \(T\).
For late \(Y\) every remaining integer of this interval lies in
\(I(Y)\). On it, \(A(n)\ge\tfrac14 n e^{-c\Phi(T)}\) because
\(e^{-2\pi}T e^{-c\Phi(T)}\to\infty\), so the floor loses at most
one. Each such integer contributes at least
\(e^{-2c\Phi(T)}/32\) to the energy. Replacing the sine condition
by \(\sin(t)\le-1/2\) also supplies negative levels in each such
late window.

This example tests the hypotheses on increments and size alone.
Together with recurring sign changes, those hypotheses allow positive
energy \(Y^{3/2-o(1)}\) on
every late window. **O.** The needed bound is on the actual Möbius
tail \(D_Y(t)\) in (5), or equivalently on the retained signed means
in (4). The positive whole-window target remains open.
