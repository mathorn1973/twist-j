# Joint transfer to a factor-cutoff Möbius sum

**NON-CANONICAL. Authority none.** The convolution identity, complete-window
transfer and model obstruction are **candidate-D**. The positive energy
bound for the actual Möbius sum is **O**. Action layer `NOT_APPLICABLE`.
This is a paper derivation within the scope of `C-RH-THREE-INTERFACE-SYNTHESIS-N`.

## Exact cancellation of the mixed factor ranges

Keep the slabs, weights, \(U_H^J\) and \(L_X(N)=N+1/2+J(H-1)/2\)
from [BILINEAR-LOW.md](BILINEAR-LOW.md). For any integer \(T\ge1\), let
\(u_T(a)=\mu(a)\mathbf1_{a\le T}\), \(v_T=\mu-u_T\), and define
\[
 h_T=\sum_{a\le T}\frac{\mu(a)}a,\qquad
 C_T(n)=\sum_{\substack{a,b>T\\ab\le n}}\mu(a)\mu(b)
                  \left\lfloor\frac{n}{ab}\right\rfloor.
\]
Dirichlet convolution gives the finite-coefficient identity
\[
 \mu=2u_T-u_T*u_T*\mathbf1+v_T*v_T*\mathbf1.
\]
Indeed, the difference of the last two convolutions is
\((v_T-u_T)*(v_T+u_T)*\mathbf1=\mu-2u_T\), since
\(\mu*\mathbf1=\delta_1\). This eliminates the two mixed factor ranges
as complete floor sums, including mixed products below the current
argument. Summing through \(n\ge T\) and centering the small-factor
floor yields
\[
 M(n)=C_T(n)-(n+1/2)h_T^2+\tfrac12 M(T)^2+2M(T)
           +\sum_{d\le T^2}(u_T*u_T)(d)\psi_d(n).
\]
The two squared boundary terms come from the *complete* small
rectangle. The coefficient of \(n+1/2\) is therefore a negative
square even though the slope of the raw-product truncation in
[BILINEAR-LOW.md](BILINEAR-LOW.md) is signed.

## Transfer on the same complete windows

Choose \(T=T_X\le\lfloor X^{1/3}\rfloor\) on each sufficiently late
slab, independently of the individual integer \(N\) in that slab.
The small rectangle has raw support \(d\le T_X^2\le D\) and
\(|(u_{T_X}*u_{T_X})(d)|\le\tau(d)\). Its projected amplitude is zero.
The short raw-denominator estimate in equation (1) of
[BILINEAR-LOW.md](BILINEAR-LOW.md), before the other error terms there,
gives the average's squared slab norm at most a constant times
\[
 \frac{(X+T_X^4)T_X^2}{X^2}(1+\log X)^3.
\]
Here the squared coefficient mass has bound
\(O(T_X^2(1+\log X)^3)\), and the frequency separation on each
translated slab is at least \(T_X^{-4}\). The forward average
preserves the bound by convexity.

For \(T_X=\lfloor X^{1/4}\rfloor\) this norm is
\(O(X^{-1/4}(1+\log X)^{3/2})\) before squaring. The intercept
\(M(T_X)^2/2+2M(T_X)\) is \(O(X^{1/2})\) pointwise by the count of
integers through \(T_X\), hence \(O(1)\) in slab norm. Define
\[
 Z_X(N)=U_H^J C_{T_X}(N)-L_X(N)h_{T_X}^2.
\]
Then \(Z_X-U_H^JM\) has slab norm \(O(1)\). The same comparison to
the projected carrier follows directly from the padded identity
for \(M\) in [PRIME-CANCELLATION.md](PRIME-CANCELLATION.md) and (1) of
[BILINEAR-LOW.md](BILINEAR-LOW.md): subtracting \(T_{\mathrm{low}}\)
from \(U_H^JM\) leaves \(E_X(c*c)\). The affinity uses exactly the
same \(L_X(N)\) on the two sides. Consequently the piecewise \(Z\)
satisfies
\[
 \left|\sqrt{Q_Z(Y)}-\sqrt{Q_{R_{1/36}}(Y)}\right|
       \ll (1+\log Y)^2
\]
on every sufficiently late complete integer window. The errors are
bounded on each whole slab, then summed in square on the slab
intersections with that same window. The inequality follows from the
weighted Lipschitz bound for the positive part. For a required
exponent \(r\), use the windows for \(2r\) in either direction and
absorb the logarithmic error in the remaining margin.

The comparison holds with the intercept retained for every choice
\(1\le T_X\le\lfloor X^{1/3}\rfloor\). With the stated fourth-root
choice the intercept can be omitted and the square in \(Z\) kept.
Every remaining Möbius factor in \(C_{T_X}\) exceeds \(T_X\), and
writing the floor as a sum over \(k\) leaves
\(k\le(B_X-1)/(T_X+1)^2\ll X^{1/2}\). The open bound now concerns the
positive part of the excess of this two-large-factor floor sum over
\(L_Xh_{T_X}^2\). An upper bound on the positive corner alone would
suffice because \(L_X>0\).

## A vanishing comparison with the full arithmetic residual

The preceding logarithmic comparison can be strengthened for the same
fourth-root choice, using the already stated classical Mertens and
maximal short-sum inputs. Write
\(\Phi(x)=(\log x)^{3/5}(\log\log x)^{-1/5}\).
For every fixed \(K>0\),
\[
 \|Z-R\|_{I(Y)}\ll_K(\log Y)^{-K}                              \tag{1}
\]
on every sufficiently late complete integer window. This comparison
uses the direct identity with \(M\), not the projection through \(T_{\rm low}\).

Write \(m=M(T)\) and \(S_T(n)=\sum_{d\le T^2}(u_T*u_T)(d)\psi_d(n)\).
The exact difference is
\[
 Z-R=(U_H^JM-M)+(M-R)
             -\left(\tfrac12m^2+2m\right)-U_H^JS_T .
\]
The two first norms have every fixed inverse-logarithmic saving by
[ONE-SIDED-LOW.md](ONE-SIDED-LOW.md), Section 1, at total shift length
\(J(H-1)\), and [WINDOW-BOUND.md](WINDOW-BOUND.md), equation (5).
The frozen coefficients are valid at every translated argument.
For the third term, the classical input
\(|M(T)|\ll T e^{-c\Phi(T)}\) and the exact sum of slab weights
\(1/(2X)\) give
\[
 \left\|\tfrac12m^2+2m\right\|_X
 \ll e^{-2c\Phi(T)}+X^{-1/4}e^{-c\Phi(T)}.
\]
Here \(T=\lfloor X^{1/4}\rfloor\), so \(\Phi(T)\) is comparable to
\(\Phi(X)\). This beats every fixed inverse logarithmic power.
The last term has norm \(O(X^{-1/4}(1+\log X)^{3/2})\) as proved above.
Restrict these squared bounds to each slab-window intersection and
sum over the complete window; the logarithmic number of slabs is
absorbed by choosing a stronger fixed saving. This proves (1).

It follows that the square roots of the positive energies have the
same vanishing comparison. There is no corresponding inference of
an additive bound on \(Q_Z-Q_R\) without controlling their levels.
For each carrier's own block projection, however,
[FULL-LEVELS.md](FULL-LEVELS.md) gives
\[
 0\le Q_Z(Y)-S_Z(Y)\ll_{B,K}(\log Y)^{-K}.
\]
Indeed \(\|(1-P)Z\|\le\|(1-P)M\|+\|Z-M\|\), and the same proof of
(1) omits \(M-R\) to bound the second norm. All three block energies
remain energies of their own actual means.

## Limitation of separate one-variable input

On each sufficiently large slab consider a real model sequence with
entries \(+1\) on an integer interval of length
\[
 \ell=\left\lfloor X^{1/2}\exp(- (\log X)^{3/4})\right\rfloor
\]
starting at \(\lceil(21/20)\sqrt X\rceil\), and entries \(-1\) on
one of the same length starting at \(\lceil(7/5)\sqrt X\rceil\).
Set all other entries to zero. The total sum is zero, every interval
sum has absolute value at most \(\ell\), and all entries below any
\(T_X\le X^{1/3}\) are zero. Thus both the model's small-cutoff
slope and intercept vanish. The interval-sum bound at the support
scale is smaller than \(X^{1/2}/(\log X)^K\) for each fixed \(K\).

For integers \(5X/4\le N\le 7X/5\), every averaged argument
lies between \(5X/4\) and \(29X/20\) eventually, since \(JH=o(X)\).
All products from the positive interval lie strictly between \(X\)
and \(5X/4\), because \(\ell=o(\sqrt X)\). Every product using the
negative interval is at least \((147/100)X>29X/20\). The only
nonzero floors are therefore one for the positive-positive pairs.
The complete averaged corner on this interval is exactly \(\ell^2\).
Its positive squared slab norm is at least a constant times
\[
 \frac{\ell^4}{X}\gg X\exp(-4(\log X)^{3/4}).
\]
The construction concerns estimates applied to the remaining model
corner with generic bounded coefficients and uniform one-variable
interval-sum bounds at its support scale. The Möbius inversion
identity was used to derive the actual corner and the model is
only a test of estimates at that later step. It gives no lower bound
for \(Q_Z\) with the actual Möbius coefficients.

## Hyperbola recursion and its dependence on negative prefix sums

For each \(k\le n/(T+1)^2\), splitting \(ab\le n/k\) at
\(s_k=\lfloor\sqrt{n/k}\rfloor\) counts each pair once after subtracting
the square of the overlap. In the resulting linear term let \(j=ka\).
The exact identity is
\[
 C_T(n)=
 2\sum_{j\ge1} D_T(n,j)\bigl(M(\lfloor n/j\rfloor)-M(T)\bigr)
       -\sum_{k\le n/(T+1)^2}\bigl(M(s_k)-M(T)\bigr)^2,
 \qquad
 D_T(n,j)=\sum_{\substack{a\mid j\\T<a\le n/j}}\mu(a).
\]
The linear coefficient arises from \(a\le\sqrt{n/k}\), which is
equivalent to \(aj\le n\), and \(a>T\) is the only further condition
on that divisor of \(j\). Each coefficient vanishes when \(j>n/(T+1)\).
Every square uses only prefix abscissae at most \(\sqrt n\).
For \(1<j\le\sqrt n\), the upper cutoff inside \(D_T(n,j)\) is
inactive, so
\[
 D_T(n,j)=-\sum_{\substack{a\mid j\\a\le T}}\mu(a).
\]
In particular \(D_T(n,p)=-1\) for any prime \(T<p\le\sqrt n\).
These coefficients act on larger prefix abscissae and do not occur
in the squares.

This yields a quantified obstruction for bounding this recursion
from positive prefix energy alone. Fix \(T=\lfloor X^{1/4}\rfloor\),
\(P=2T\), and let \(p\) run through the primes in \([P,2P]\).
Define a model prefix state \(g\) on integer arguments by
\[
 c_p=\lfloor X/p\rfloor,\quad
 L=\lfloor X/(100P^2)\rfloor,\qquad
 g(t)=-\sum_{p\in[P,2P]} (L-|t-c_p|)_+ ,
\]
where the sum is over those primes. The pulse supports are disjoint,
since \(|X/p-X/q|\ge X/(4P^2)\) for distinct such primes.
For all sufficiently large \(X\) they are also separated by at least
one zero argument. Thus \(|g(t+1)-g(t)|\le1\) and \(g_+=0\).
The supports lie above \(\sqrt{2X}\), so \(g(T)=g(s_k)=0\) for
every \(n\le2X\).

Take \(X\le n\le X+X/(1000P)\). At \(j=p\),
\(|\lfloor n/p\rfloor-c_p|\le X/(1000P^2)+1\le L/2\) eventually.
For every other positive integer \(j\),
\[
 \left|\frac{n}{j}-\frac Xp\right|
  =\frac{|p(n-X)+X(p-j)|}{pj}
  \ge \frac{(1-2/1000)X\,|p-j|}{pj}
  \ge \frac{(1-2/1000)X}{p(p+1)} .
\]
The last inequality follows because \(|p-j|/j\) is minimized for
\(j=p+1\) among integers \(j\ne p\). After accounting for floors,
this distance exceeds \(L\). Thus only \(j=p\) can enter the pulse
at \(c_p\), with \(D_T(n,p)=-1\).

Evaluate the right-hand side of the hyperbola identity by keeping
the genuine coefficients \(D_T(n,j)\) and replacing its prefix
state \(M\) by \(g\). Every negative square is zero, and each prime
contributes at least \(L\) to the resulting expression. For
\(N\in[X,X+X/(2000P)]\), all arguments in \(U_H^J\) lie in
the range just considered for all sufficiently large \(X\), because
\(J(H-1)=o(X/P)\). If \(\pi_P\) counts the indicated primes, the
weighted positive squared norm on this part of the slab is
\[
 \gg \frac{(L\pi_P)^2}{XP}
 \gg \frac{X}{P^3(\log P)^2}
 \asymp \frac{X^{1/4}}{(\log X)^2},
\]
using the prime number theorem cited in [BILINEAR-LOW.md](BILINEAR-LOW.md).
This is a property of the hyperbola operator when the prefix state is
allowed to vary with the coefficients fixed. The model respects unit
prefix increments and has zero positive energy. The nonnegative
squares give no control of these negative pulses because they use a
disjoint range of prefix arguments. The same linear increment occurs
if the pulses are added to any fixed base prefix state, with every
square and all data through \(T\) unchanged. A bound that also uses
the relation between the divisor coefficients and the actual Möbius
prefix state is outside this obstruction. The actual positive energy
bound remains **O**.

The lower bound just proved concerns the substituted corner operator.
It does not include subtraction of the actual drift \(L_Xh_T^2\).
Although adding a pulse to a fixed prefix state leaves this drift and
the overlap squares unchanged, a positive lower bound on the change
does not imply that lower bound for the positive part of the complete
drift-subtracted expression.

The same obstruction applies after the weighted block projection of
[FULL-LEVELS.md](FULL-LEVELS.md). For either block length there, the
length is \(o(X/P)\). The blocks contained in the test interval cover
all but at most two boundary blocks and so have total weight
\(\gg 1/(XP)\). Their weighted means of the output are at least
\(L\pi_P\), while every block mean of \(g\) remains nonpositive.
This gives the same lower bound on the model block-level energy.

The model can also satisfy strong short-increment estimates on the
prefix scale. Set \(\delta_X=\exp(-(\log X)^{3/4})\), and replace
\(g(t)\) by
\[
 g_\delta(t)=-\left\lfloor \delta_X
                 \sum_{p\in[P,2P]}(L-|t-c_p|)_+ \right\rfloor .
\]
On real arguments the sum inside the floor, after multiplication by
\(\delta_X\), is piecewise affine and globally \(\delta_X\)-Lipschitz:
the positive supports are disjoint and each affine segment has slope
in \(\{0,\delta_X,-\delta_X\}\). Thus the integer model has unit-bounded
increments, and for all integers \(s\ge0\) and \(t\ge0\),
\[
 |g_\delta(t+s)-g_\delta(t)|\le \delta_X s+1.
\]
In particular, for a starting scale \(V\asymp X/P\), any fixed
\(\eta>0\) and \(h\ge V^{1/3+\eta}\), one has for every fixed \(A>0\)
\[
 \sum_{V\le t<2V}\max_{0\le s\le h}
       |g_\delta(t+s)-g_\delta(t)|^2
       \ll_{A,\eta} Vh^2(\log V)^{-A},
\]
with the maximum over integers. Both \(\delta_X^2\) and \(h^{-2}\)
are eventually bounded by a constant times any fixed inverse
logarithmic power. The prefix envelope is bounded by
\(\delta_X L\) and vanishes away from arguments \(t\asymp X/P\).
In particular it satisfies
\(|g_\delta(t)|\ll_c t\exp(-c(\log t)^{3/4})\) for any fixed \(c>0\)
on the support, since \(L\ll X/P^2\) and \(P\asymp X^{1/4}\).

At each of the prime abscissae in the test interval the model is at
most \(-\delta_X L/2+1\). Since \(\delta_X L\) tends to infinity, the
output retains a positive lower bound of order \(\delta_X L\pi_P\).
The squares and positive input levels still vanish. With forward
averaging and also after the preceding block projection, the same
argument yields model energy
\[
 \gg \frac{\delta_X^2 X^{1/4}}{(\log X)^2}
      =X^{1/4-o(1)}\quad\text{as a lower bound.}
\]
This construction is made afresh for each slab. It tests the use of
positive input levels together with short-increment bounds for a
model prefix sequence in the fixed-coefficient hyperbola expression.
The proof imposes no twisted short-sum bounds on its integer
increments. The actual Möbius prefix state is tied to the divisor
coefficients by the same Möbius function, a relation that this model
does not impose.
