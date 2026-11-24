# Square-power corrections and the signed bilinear sum

**NON-CANONICAL. Authority none.** The estimates and exact identities below are
**candidate-D**. The full positive whole-window bound is **O**. The action
layer is `NOT_APPLICABLE`. This is an unconditional paper calculation.
Throughout, \(R=R_{1/36}\) is the fixed residual of
[DIRICHLET-READOUT.md](DIRICHLET-READOUT.md), with its actual coefficients.

## 1. A square-root bound for large split-prime square corrections

Write \(D_0=N^{1/4}\), \(z=(\log N)^2/36\), and
\(a(d)=(-2)^{\omega(d)}\) for squarefree products of split primes. The
exact sector formula of [MOBIUS.md](MOBIUS.md) is

\[
 \gamma_d(N)=a(d)\sum_{\substack{dm^2\le N\\\operatorname{rad}(m)\mid d}}
 (-1)^{\Omega(m)}C_0(N/(dm^2)).
\]

In this formula restrict \(m\) to have every prime factor at most
\(D_0\), leaving the conditions \(d>D_0\) and \(P^+(d)>z\) fixed.
Denote the resulting sum by \(R_*(N)\). For any subset of the original
supports, the sum of absolute errors of this restriction is
\(O(\sqrt N/\log N)\).

Indeed, in an omitted term one can write \(d=pe\) and \(m=p^j m'\)
for some \(p>D_0\), \(j\ge1\), and \(p\nmid em'\). Then
\(\operatorname{rad}(m')\mid e\). Use \(|C_0(u)|\ll u^{1/3}\) and the
nonnegative weight

\[
 g(e)=2^{\omega(e)}\prod_{q\mid e}(1-q^{-2/3})^{-1}
\]

on admissible \(e\), extended by zero. The summatory estimate
\(\sum_{e\le v}g(e)\ll v\) in [MOBIUS.md](MOBIUS.md) gives
\(\sum_{e\le v}g(e)e^{-1/3}\ll v^{2/3}\) for \(v\ge1\).
For fixed \(p,j\), sum over \(m'\) by the geometric product and then over
\(e\le N/p^{2j+1}\). The resulting bound is

\[
 \ll (N/p^{2j+1})^{1/3}\sum_{e\le N/p^{2j+1}}g(e)e^{-1/3}
 \ll N/p^{2j+1}.
\]

If \(p^{2j+1}>N\), the original sum for that \(p,j\) is empty.
Summing over \(j\ge1\) and then \(p>D_0\) bounds the error by
\(O(N/(D_0^2\log D_0))\), since \(\pi(v)\ll v/\log v\) and a dyadic
partition gives \(\sum_{p>D_0}p^{-3}\ll D_0^{-2}/\log D_0\).
This is an absolute estimate after expansion into the correction
factors, so counting a term more than once in the upper bound is
permitted. In particular, for a greatest split prime \(p>D_0\) of
\(d=pe\), the same proof controls the omission of the terms \(j\ge1\)
in \(\gamma_{pe}(N)=-2\sum_{j\ge0}(-1)^j\gamma_e(N/p^{2j+1})\).

For any sequence \(F\), use
\(Q_F(Y)=\sum_{Y\le N<Y^{3/2}}F(N)_+^2/[N(N+1)]\). The error just
proved yields

\[
 \big|\sqrt{Q_R(Y)}-\sqrt{Q_{R_*}(Y)}\big|
 \ll (\log Y)^{-1/2}
\]

on each sufficiently late complete window. The error has finite global
squared weighted norm, and its tail above \(Y\) is bounded by a constant
times \(\sum_{N\ge Y}1/((N+1)(\log N)^2)\). Thus the square corrections of
large oriented primes are controlled even before cancellation between
different supports is estimated.

## 2. A centered identity with nonpositive drift

The following signed identity estimates the original residual through
\(M(N)-R(N)=O(\sqrt N)\). Let \(X\) run over powers of two, and work
on the integer slab \(X\le N<2X\), with \(X\) sufficiently large.
Fix \(A=\lceil\sqrt{3X}\rceil\). The same coefficients will also be used
at nearby arguments up to \(3X\). Define integer coefficients \(c_a\)
by \(c_a=\mu(a)\) for \(a\le A\). For
\(A<a\le A+|M(A)|\), put \(c_a=-\operatorname{sgn}M(A)\). Put \(c_a=0\)
elsewhere. Thus \(|c_a|\le1\), \(c_a=0\) for \(a>2A\), and
\(\sum_a c_a=0\). Let \(b=c*c\), using Dirichlet convolution, and put
\(h_X=\sum_a c_a/a\). In particular \(\sum_d b_d=0\),
\(\sum_d b_d/d=h_X^2\), and \(|b_d|\le\tau(d)\).

Use \(\mathbf 1(n)=1\) and the convolution identity \(\mu*\mathbf 1=\delta\).
Then \(\delta-\mathbf 1*c\) vanishes through \(A\), and its convolution
square vanishes through \(A^2\). The identity

\[
 \mu*(\delta-\mathbf 1*c)^{*2}=\mu-2c+\mathbf 1*c*c
\]

therefore gives \(\mu(n)=2c_n-(\mathbf 1*b)(n)\) for \(n\le 3X\).
For integers \(2A\le N\le 3X\) the first term sums to zero. Since
\(\lfloor(N+1/2)/d\rfloor=\lfloor N/d\rfloor\), set

\[
 \psi_d(N)=\left\{\frac{N+1/2}{d}\right\}-\frac12
           =\frac{(N\bmod d)+1/2}{d}-\frac12.
\]

We obtain the exact same-argument formula

\[
 M(N)=\sum_d b_d\psi_d(N)-(N+1/2)h_X^2.                     \tag{1}
\]

All \(d\) through \(4A^2\) can occur in the centered sum. For \(d>N\)
the floor is zero, and its affine pieces in (1) still participate in
cancellation. The second term in (1) is nonpositive.

The padding terms can be checked directly. Write \(u_a=\mu(a)\) for
\(a\le A\), zero otherwise, and \(v=c-u\). For each \(b>A\) in the
support of \(v\), \(N/b<A\) if \(N< A^2\). On the stated slabs,
including the bounded averages below for sufficiently large \(X\),
\(N\ge b\) also holds. Consequently

\[
 \sum_{a\le A}\mu(a)\lfloor N/(ab)\rfloor=1,
 \qquad
 \sum_{a,b}v_a v_b\lfloor N/(ab)\rfloor=0.
\]

The first equality is \(\sum_{m\le N/b}(\mu*\mathbf 1)(m)=1\). The second
holds because every product of two indices of \(v\) exceeds \(N\).
Thus the whole mixed contribution to the uncentered floor sum is
\(2\sum_b v_b=-2M(A)\). Centering in (1) moves these terms between the
drift and the sawtooth sum. This exact identity supplies no sign for the
remaining sawtooth sum.

## 3. A weighted whole-window bound through denominator \(X^{2/3}\)

The exact gcd covariance and separated-frequency method have antecedents
in [#2087](https://github.com/mathorn1973/twist-j/issues/2087) for its
periodic \(\chi_5\) carrier, with earlier work cited there. Here the
carrier is \(\psi_d\) and the coefficients are the balanced bilinear
coefficients of (1).

Let \(g=\gcd(d,e)\). On a full period modulo \(\operatorname{lcm}(d,e)\),
conditional on \(N\equiv r\pmod g\) with \(0\le r<g\), the remainders
modulo \(d,e\) are independent and uniform in their respective classes.
This follows from the Chinese remainder bijection for compatible pairs
of residues. The respective conditional means of \(\psi_d,\psi_e\) are
\((r-(g-1)/2)/d\) and \((r-(g-1)/2)/e\). Averaging their product gives

\[
 \mathbb E\,\psi_d(N)\psi_e(N)=\frac{g^2-1}{12de}.            \tag{2}
\]

For \(S_D(N)=\sum_{d\le D}b_d\psi_d(N)\), let \(z_\theta\) be its finite
Fourier coefficients, with equal frequencies combined. Each nonzero
frequency has reduced denominator at most \(D\), so distinct frequencies
have circular spacing at least \(D^{-2}\). Parseval on the common
integer period and (2) give

\[
 \sum_\theta|z_\theta|^2
 \ll \sum_{d,e\le D}\tau(d)\tau(e)\frac{\gcd(d,e)^2}{de}
 \ll D(1+\log D)^3.                                         \tag{3}
\]

For the last step write \(d=gu,e=gv\), drop the coprimality condition on
\(u,v\), and use \(\tau(gu)\le\tau(g)\tau(u)\). The resulting sum is at
most \(\sum_{g\le D}\tau(g)^2(1+\log(D/g))^4\), since
\(\sum_{u\le V}\tau(u)/u\le(1+\log V)^2\). Coefficientwise
\(\tau(g)^2\le\tau_4(g)\) by \((j+1)^2\le\binom{j+3}{3}\) on prime powers.
Also \(\sum_{g\le V}\tau_4(g)\le V(1+\log V)^3\) by three harmonic sums.
Partitioning \(g\) into \(D/2^{i+1}<g\le D/2^i\) yields (3).

For completeness, for a sum of frequencies with spacing \(\delta\),
majorize the indicator of the slab by twice the triangular weight
\((1-|N-X|/(2X))_+\). Its Fourier transform has absolute value bounded
by \(\min(2X,(8X\|\theta\|^2)^{-1})\) for \(\theta\ne0\), where
\(\|\theta\|\) is distance to the nearest integer. The bound follows
from the square of the geometric sum of length \(2X\), divided by
\(2X\). On either side of each frequency the \(j\)-th distance is at
least \(j\delta\). Summing the transform bound up to and beyond
\(1/(X\delta)\) bounds the absolute row sums by \(O(X+\delta^{-1})\).
The resulting quadratic form is bounded by this maximum row sum times
\(\sum_\theta |z_\theta|^2\), using
\(2|z_\theta z_\eta|\le |z_\theta|^2+|z_\eta|^2\).
Equations (2) and (3) therefore prove

\[
 \sum_{X\le N<2X}|S_D(N)|^2\ll (X+D^2)D(1+\log D)^3.        \tag{4}
\]

Choose \(D=\lfloor X^{2/3}\rfloor\) on each slab. Let

\[
 T(N)=\sum_{d>D}b_d\psi_d(N)-(N+1/2)h_X^2,
 \qquad X\le N<2X.
\]

By (4), the squared norm of \(S_D\) with weight \(1/[N(N+1)]\) is
\(O((1+\log X)^3)\) on the slab. Intersect the slabs with any complete
\([Y,Y^{3/2})\). There are \(O(\log Y)\) such slabs. Equations (1) and
(4), the pointwise deletion error for \(R\), and the Lipschitz property
of positive part give

\[
 \big|\sqrt{Q_R(Y)}-\sqrt{Q_T(Y)}\big|\ll (\log Y)^2.         \tag{5}
\]

Thus the original window assertion holds for \(T\) exactly when it
holds for \(R\). In either direction use the source condition for \(2r\)
and absorb the logarithmic norm error before demanding exponent \(r\).
Dropping the nonpositive term of \(T\) gives a one-sided upper bound
for use with (5). The two-way comparison (5) uses its actual sign and
keeps that term.

## 4. Further bounds for harmonics of long denominators

On the slab let \(J=\log_2 X\), an integer, and
\(H=\lceil\sqrt{XJ}\rceil\). For any function on the required arguments
write \(U_H F(N)=H^{-1}\sum_{j=0}^{H-1}F(N+j)\). Then
\(|U_H^J M(N)-M(N)|\le J(H-1)\) because \(|\mu(n)|\le1\).
This gives squared weighted error \(O((\log X)^3)\) on the slab.
For sufficiently large \(X\), every averaged argument is at most
\(3X\), so (1) holds with the original slab coefficients for all of them.
The proof of (4) applies on each shifted slab of length \(X\) with the
same bound, by shifting the center of the triangular weight. Jensen's
inequality then gives (4) for \(U_H^J S_D\) on the original slab.
The moving choices of \(H,J\) were suggested in internal Astra review.

The multiplier of \(U_H\) at frequency \(\theta\) has modulus at most
\(\min(1,(2H\|\theta\|)^{-1})\). For \(d\ge 2\) the nonzero coefficients
of \(\psi_d\), at \(\theta=r/d\) for \(1\le r<d\), have absolute value
\(1/(d|1-e^{-2\pi i r/d}|)\), by differentiating a finite geometric
sum. Their sum of absolute values is \(O(1+\log d)\). Consequently the
sum of absolute Fourier coefficients of \(\sum_{d>D} b_d\psi_d\) is
\(O(X(1+\log X)^2)\), by \(|b_d|\le\tau(d)\) and \(4A^2=O(X)\).
On \(\|\theta\|\ge1/H\), each average multiplies this bound by at most
\(1/2\). Thus \(U_H^J\) gives a pointwise \(O((\log X)^2)\) bound for
these long-denominator modes.

There is also control by reduced denominator within the surviving
frequency interval. Put \(D_1=\lfloor X^{2/3}/(\log X)^2\rfloor\).
At a frequency \(\theta=r/q\) in lowest terms, the coefficient of
\(\sum_{d>D}b_d\psi_d\) is

\[
 -\frac{1}{1-e^{-2\pi i r/q}}\sum_{\substack{d>D\\q\mid d}}\frac{b_d}{d}.
\]

The sum inside has absolute value at most
\(\tau(q)(1+\log(4A^2))^2/q\). Summing the squared reciprocal factor over
\(1\le r<q\) costs \(O(q^2)\), using
\(|1-e^{-2\pi i r/q}|\ge4\min(r,q-r)/q\). Thus the squared Fourier
coefficient sum over \(q\le D_1\) is \(O(D_1(1+\log X)^7)\). Restricting
to \(\|\theta\|<1/H\) and applying the averaging multiplier can only
reduce this coefficient bound. The separated-frequency estimate with
spacing \(D_1^{-2}\) now controls these harmonics on the slab by
\(O(X^{-2}(X+D_1^2)D_1(1+\log X)^7)\) in squared weighted norm.
This is \(O((\log X)^3)\) for the specified \(D_1\).

Define \(T_{\mathrm{low}}(N)\) by retaining in
\(U_H^J\sum_{d>D}b_d\psi_d(N)\) only frequencies
\(0<\|\theta\|<1/H\) with reduced denominator \(q>D_1\), and adding
\(-(N+1/2+J(H-1)/2)h_X^2\). The restrictions are symmetric under
conjugation and give a real sequence. The preceding estimates and
the averaged form of (4) prove

\[
 \big|\sqrt{Q_R(Y)}-\sqrt{Q_{T_{\mathrm{low}}}(Y)}\big|
 \ll (\log Y)^2                                             \tag{6}
\]

on every sufficiently late complete window. These estimates control
additional families from the long denominators. The denominator bound
for the remaining frequencies gives spacing only of order \(X^{-2}\)
on a slab of length \(X\).

## 5. Lower-argument recurrence and its loss

Write \(C(t)=\sum_{a\le t}c_a\), \(B(D)=\sum_{d\le D}b_d\), and
\(I(D)=\sum_{d\le D}b_d/d\), all using the fixed slab coefficients.
Put \(K(N)=\lfloor N/D\rfloor\). Expanding the floor with index \(k\)
gives the exact formula

\[
 T(N)=-\sum_{k\le K(N)}\sum_a c_a C(N/(ka))
       +(K(N)+1/2)B(D)-(N+1/2)I(D).                         \tag{7}
\]

Indeed \(\sum_{d>D}b_d\lfloor N/d\rfloor=\sum_{k\le K(N)}
(B(N/k)-B(D))\) with \(B(t)=\sum_{d\le t}b_d=\sum_a c_a C(t/a)\).
Further, \(\sum_{d>D}b_d=-B(D)\) and
\(\sum_{d>D}b_d/d-h_X^2=-I(D)\). Those are the two boundary terms
in (7). In the double sum, \(a\le D/(2A)\) contributes zero because
\(N/k\ge D\) and \(C(t)=0\) for \(t\ge2A\). Thus for contributing
\(a,k\), the arguments \(N/(ka)\) range below \(2X/a\), and the
nonzero \(C(N/(ka))\) use arguments between \(D/(2A)\) and \(2A\).
Through \(A\), \(C(t)=M(\lfloor t\rfloor)\). Its values beyond \(A\)
are the fixed signed padding described above.

An exact change of variables measures the loss of estimating the first
term in (7) from lower-argument energies. Set

\[
 \mathcal E_C(V)=\sum_{V/3\le m\le 3V}\frac{|C(m)|^2}{m(m+1)}.
\]

Fix \(k\le2X/D\) and a dyadic range \(U\le a<2U\). Put \(V=X/(kU)\).
The \(1/[N(N+1)]\)-weighted norm on the slab of
\(\mathbf 1_{k\le K(N)} C(N/(ka))\) is bounded by
\((ka)^{-1/2}\sqrt{\mathcal E_C(V)}\) for sufficiently large \(X\).
To see this, drop the indicator in the nonnegative norm, write the
remaining sum as \(\int_X^{2X}|C(x/(ka))|^2\,dx/x^2\), and substitute
\(x=kat\). The integral is exact because \(ka\) is an integer and
\(C(x/(ka))\) is constant on each \([N,N+1)\). The range of \(t\) is
contained in \([V/2,2V]\), and the integer cells it meets lie in
\([V/3,3V]\) once \(V\ge6\). This holds here since \(V\gg D/A\).
Thus the norm of the sum over \(a\) in that dyadic range is at most
\(O(\sqrt{U/k}\sqrt{\mathcal E_C(V)})\).

For the norm of the entire first term in (7) this triangle inequality
costs at most a constant times

\[
 \left(\sum_{a\le2A}a^{-1/2}\right)
 \left(\sum_{k\le2X/D}k^{-1/2}\right)
 \sup_V\sqrt{\mathcal E_C(V)}
 \ll \frac{X^{3/4}}{\sqrt D}\sup_V\sqrt{\mathcal E_C(V)},      \tag{8}
\]

where the supremum is over the lower arguments just used in the norm
bound. At \(D=\lfloor X^{2/3}\rfloor\) the loss is \(X^{5/12}\).
Even uniform subpower bounds for these two-sided lower-argument
energies would leave a positive power in (8). Equation (7) also retains
the two explicit boundary terms. The estimate (8) supplies no
cancellation between different \(a,k\), or between their sum and those
boundary terms.

**O.** The fixed residual still requires the positive whole-window
bound after the proven errors in (5) or (6). The negative drift and the
remaining signed long terms share the same argument \(N\). A bound for
their positive part or their signed coupling at the required scale has
yet to be established.
