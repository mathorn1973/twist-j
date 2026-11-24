# Analytic reductions and bounds for the signed moment

**NON-CANONICAL research note.** A. M. Thorn. 6 September 2026.

This appendix proves the analytic statements used in the
[overview](README.md). All estimates below are unconditional. The
Riemann hypothesis, a hypothesis about zeros of a character L-function,
and the final target moment are not assumptions. Assertions explicitly
marked as targets or sufficient inputs remain open.

Sections 1--7 give definitions and a finite approximation with errors
strictly below the target. Sections 8--9 give the established global
bound and a reduced sufficient input. The companion
[arithmetic appendix](ARITHMETIC.md) studies the coefficients, and
[prime-cancellation appendix](PRIME-CANCELLATION.md) constructs actual
signed subfamilies. Equation labels here begin with A.

## 1. Definitions and the analytic target

Let $\chi=\chi_5$ be the real primitive character modulo 5:
$\chi(1)=\chi(4)=1$, $\chi(2)=\chi(3)=-1$, and
$\chi(0)=0$, with arguments interpreted modulo 5.
Call a prime split if it is $1$ or $4\pmod5$, and let
$\mathcal R$ consist of the squarefree products of split primes,
including 1. Write
$$
f(r)=(-2)^{\omega(r)}\quad(r\in\mathcal R),\qquad f(r)=0
\quad(r\notin\mathcal R).
\tag{A1}
$$
All integer summation variables are positive. Throughout, unless a
narrower range is stated,
$$
\frac14<\sigma<\frac12,\quad s=\sigma+it,\quad
\rho=\frac12-\sigma,\quad \delta=2\sigma-\frac12,\quad T\ge2.
\tag{A2}
$$
Constants can depend on fixed $\sigma$ and on an arbitrarily small
positive $\epsilon$. No uniformity at the strip endpoints is asserted.
Define the normalized time norm by
$$
\|Q\|_{p,T}=\left(\frac1T\int_T^{2T}|Q(t)|^p\,dt\right)^{1/p}.
$$
The supremum norm on this interval has the usual meaning.

For real $Y\ge1$, put
$$
\begin{split}
\zeta_5(z)&=(1-5^{-z})\zeta(z),\\
T_Y(s)&=\sum_{r\le Y}f(r)r^{-s}
                     \prod_{p\mid r}(1+p^{-2s})^{-1},\\
H(s)&=\frac{(1-5^{-s})L(2s,\chi)}{\zeta_5(4s)},\\
G_Y(s)&=L(s,\chi)T_Y(s),\qquad C(s)=H(s)L(s,\chi).
\end{split}
\tag{A3}
$$
The finite support factor is analytic for $\Re s>0$. All reciprocal
zeta factors used on (A2) are represented by absolutely convergent
Euler products, since $4\sigma>1$.

Here is an explicit definition of the complete prefix. For $\Re s>1$
the unrestricted support product, multiplied by $L(s,\chi)$, is
$$
E(s)=
\prod_{p\ {\rm split}}\frac{1-p^{-s}}{1+p^{-2s}}
\prod_{\substack{p\ne5\\\chi(p)=-1}}\frac1{1+p^{-s}}
=\sum_{n\ge1}e(n)n^{-s}.
\tag{A4}
$$
At a split prime, writing $z=p^{-s}$, the support factor is
$1-2z/(1+z^2)=(1-z)^2/(1+z^2)$; multiplication by
the L-factor $1/(1-z)$ gives the factor in (A4).
At every other prime the support factor is 1.
Equivalently,
$$
E(s)=\prod_{p\ne5}\frac{1-p^{-s}}{1+\chi(p)p^{-2s}}.
\tag{A5}
$$
For a split prime the local coefficient sequence is
$1,-1,-1,1,1,-1,-1,1,\ldots$; for an inert prime it is
$(-1)^j$ at exponent j. Positive powers of 5 have zero coefficient.
Multiplicativity therefore gives $|e(n)|\le1$.

More directly, the geometric expansion of $G_Y$ has coefficients
$$
g_Y(n)=\sum_{\substack{r v^2 m=n,\ r\le Y\\
r\in\mathcal R,\ \operatorname{rad}(v)\mid r}}
f(r)(-1)^{\Omega(v)}\chi(m).
\tag{A6}
$$
It is an absolutely convergent expansion when $\Re s>1$.
For $n\le Y$, the restriction $r\le Y$ is automatic; hence
$g_Y(n)=e(n)$. Set
$$
P_Y(s)=\sum_{n\le Y}e(n)n^{-s},\qquad
r_Y(T)=\|H(s)(G_Y(s)-P_Y(s))\|_{2,T}.
\tag{A7}
$$
No coefficient series is truncated after analytic continuation to
(A2); (A7) is a difference of explicitly defined analytic functions.

At the critical relation $Y=T^2$, define
$$
\mathcal N=Y^{1-\sigma}T^{-1/2},\qquad
\mathcal B=Y^{1-\sigma}T^{-\sigma},\qquad
T^\rho\mathcal N=\mathcal B.
\tag{A8}
$$
The open analytic target is $r_Y(\sqrt Y)\ll_\epsilon Y^{1-3\sigma/2+\epsilon}$. The quantifier is: for every
$\epsilon>0$, a constant exists on the fixed line.

## 2. Positive support estimates

Write $a_\chi=1*\chi$. Its local coefficients are nonnegative:
at a split prime $a_\chi(p^j)=j+1$, at an inert prime they are
1 for even j and 0 for odd j, and at 5 they equal 1.
The partial sums of $\chi$ over a period are
$0,1,0,-1,0,0$, so each initial partial sum is at most 1.
Consequently, for $z\ge1$,
$$
\sum_{n\le z}a_\chi(n)
=\sum_{m\le z}\sum_{d\le z/m}\chi(d)\le z.
\tag{A9}
$$
Partial summation yields $\sum_{n\le z}a_\chi(n)/n\le1+\log z$.
Thus
$$
\sum_{n\le z}(a_\chi*a_\chi)(n)\le z(1+\log z).
\tag{A10}
$$
On $\mathcal R$, $|f(r)|=a_\chi(r)$ and
$f(r)^2=(a_\chi*a_\chi)(r)$. In particular, for $0<\sigma<1/2$,
$$
\begin{split}
\sum_{r\le U}|f(r)|r^{-\sigma}&\ll_\sigma U^{1-\sigma},\\
\sum_{r\le U}f(r)^2r^{-2\sigma}
&\ll_\sigma U^{1-2\sigma}(1+\log U).
\end{split}
\tag{A11}
$$
The same bounds hold after imposing any coprime exclusion, because
these are positive sums.

For $k\in\mathcal R$, factoring $r=kw$ gives
$$
\sum_{\substack{r\le Y\\k\mid r}}|f(r)|r^{-\sigma}
\ll_\sigma Y^{1-\sigma}\frac{2^{\omega(k)}}k.
\tag{A12}
$$
Indeed $(w,k)=1$ in the actual factorization, and dropping that
restriction only increases the positive majorant in (A11).

For fixed Y and $\Re s>0$, the geometric expansion
$$
T_Y(s)=
\sum_{\substack{v\ge1\\v\ {\rm split\text{-}smooth}}}
(-1)^{\Omega(v)}v^{-2s}
\sum_{\substack{r\le Y,\ r\in\mathcal R\\
\operatorname{rad}(v)\mid r}}f(r)r^{-s}
\tag{A13}
$$
is absolute: only finitely many primes can occur. Let $S_{Y,K}$
be the restriction to $v\le K$. For every fixed $0<\beta<2\sigma$,
$$
\begin{split}
\sup_t|T_Y(\sigma+it)-S_{Y,K}(\sigma+it)|
&\ll_{\sigma,\beta}Y^{1-\sigma}K^{-\beta},\\
\sup_t\bigl(|T_Y(\sigma+it)|+|S_{Y,K}(\sigma+it)|\bigr)
&\ll_\sigma Y^{1-\sigma}.
\end{split}
\tag{A14}
$$
To prove the first inequality, apply (A12) with
$k=\operatorname{rad}(v)$, and then Rankin's inequality:
$$
\sum_{v>K}v^{-2\sigma}
\frac{2^{\omega(\operatorname{rad}(v))}}{\operatorname{rad}(v)}
\le K^{-\beta}
\prod_{p\ {\rm split}}
\left(1+\frac2{p(p^{2\sigma-\beta}-1)}\right)<\infty.
\tag{A15}
$$
The product converges because $2\sigma-\beta>0$. Taking beta zero
and keeping all v proves the second inequality. Preserving the
radical weight $1/k$ is essential.

## 3. Exact Fourier localization and an elementary mean-value bound

For any finite sum $Q(t)=\sum_\lambda c_\lambda\lambda^{-it}$,
where $\lambda>0$, first combine equal frequencies. For $L>0$
and any real center $t_0$, define
$$
d\mu_{L,t_0}(t)=\frac1{2\pi L}
\operatorname{sinc}^2\left(\frac{t-t_0}{2L}\right)dt,\qquad
\operatorname{sinc}(x)=\frac{\sin x}{x}.
\tag{A16}
$$
Its mass is 1. The elementary Fourier transform of the square of
the sinc function is triangular, giving
$$
\int |Q(t)|^2d\mu_{L,t_0}(t)
=\sum_{\lambda,\mu}c_\lambda\overline{c_\mu}
e^{it_0\log(\mu/\lambda)}
\bigl(1-L|\log(\mu/\lambda)|\bigr)_+.
\tag{A17}
$$
For completeness, $\int_{-h/2}^{h/2}e^{itx}\,dx =h\operatorname{sinc}(ht/2)$. The convolution of two interval
indicators is $(h-|x|)_+$. Fourier inversion and Plancherel,
with convention $\widehat f(t)=\int f(x)e^{-itx}\,dx$ and
inverse factor $1/(2\pi)$, therefore show
$$
\frac h{2\pi}\int_{\mathbb R}
\operatorname{sinc}^2(ht/2)e^{itd}\,dt
=(1-|d|/h)_+.
$$
Use $h=1/L$, translate t, and expand the finite square to obtain
(A17). This also verifies all normalization constants.

The version relevant to the moment uses $L=T$, $t_0=3T/2$:
$\mathscr F_T(Q)=\int|Q|^2d\mu_{T,3T/2}$. For real coefficients
its exact real pair kernel is
$$
\mathcal L_T(u)=(1-T|u|)_+\cos(3Tu/2).
\tag{A18}
$$
It is strictly positive for $|u|<1/T$. On $[T,2T]$ the
sinc argument in (A16) has absolute value at most $1/4$, whence
$$
\|Q\|_{2,T}^2
\le\frac{2\pi}{\operatorname{sinc}^2(1/4)}\mathscr F_T(Q)
<7\mathscr F_T(Q)
\tag{A19}
$$
when Q is nonzero; the non-strict bound with 7 applies in all cases.
This is only a sufficient comparison. A bound for the sharp interval
does not by itself bound the global Fejer integral.

The exact signed short-block identity is also useful. With $h=1/T$,
$$
\mathscr F_T(Q)=\frac1h\int_{\mathbb R}
\left|\sum_{z<\log\lambda\le z+h}
c_\lambda e^{-3iT\log\lambda/2}\right|^2dz.
\tag{A20}
$$
Expanding the square gives the intersection length
$(h-|\log(\mu/\lambda)|)_+$, hence (A17). The midpoint modulation
in (A20) is part of the identity.

We will need a standard polynomial upper bound, which follows here
without an additional mean-value theorem. If
$D(t)=\sum_{n\le U}b_n n^{-it}$, then on every interval I of
length V,
$$
\int_I|D(t)|^2dt\ll(V+U)\sum_{n\le U}|b_n|^2.
\tag{A21}
$$
To see this, put $N=\lfloor U\rfloor\ge1$ and $L=2N$.
Distinct logarithms of integers at most N differ by at least
$1/N>1/L$, since
$\log(n+1)-\log n\ge1/(n+1)$. Thus (A17) is exactly
$\sum|b_n|^2$, for every center. On a centered interval of
length at most L, the density is at least $c/L$, with an absolute
positive c. Cover I by at most $1+V/L$ such intervals. This proves
(A21); $N=1$ is immediate as well.

## 4. Fourth moments uniformly in every finite cutoff

The only external moment input is
[Topacogullari, Theorem 1.1, equation (1.8)](https://link.springer.com/article/10.1007/s00209-020-02610-9).
Applied to the fixed primitive character $\chi_5$, it gives
$$
\int_1^U|L(1/2+it,\chi)|^4dt\ll_\epsilon U^{1+\epsilon},
\qquad U\ge2.
\tag{A22}
$$
This is a time average for one character, not an average over
characters. Negative ordinates are covered by conjugation.

### Gaussian transfer to a fixed strip

For fixed $\eta>0$, uniformly for $1/2+\eta\le a\le3/2$,
$$
|L(a+i\tau,\chi)|^4
\ll_\eta 1+\int_{\mathbb R}e^{-w^2}
|L(1/2+i(\tau+w),\chi)|^4dw.
\tag{A23}
$$
Apply Cauchy's formula to
$$
\frac{L(z,\chi)^2\exp((z-a-i\tau)^2)}{z-a-i\tau}
$$
on the strip with boundaries $\Re z=1/2$ and $\Re z=2$.
The left denominator is separated from zero by eta and the right
one by at least $1/2$. The right-boundary L-function is absolutely
bounded. Horizontal integrals tend to zero by Gaussian decay.
Polynomial growth needed here is elementary: bounded character
partial sums and Abel integration give
$|L(z,\chi)|\ll |z|/\Re z$ for $\Re z>0$.
Squaring the resulting integral estimate and applying Cauchy--Schwarz
against the Gaussian proves (A23).

Integrating (A23), using (A22) and conjugation, gives
$$
\sup_{1/2+\eta\le a\le3/2}
\int_{-cU}^{cU}|L(a+it,\chi)|^4dt
\ll_{\eta,c,\epsilon}U^{1+\epsilon}.
\tag{A24}
$$
Indeed the shifted critical-line integral is bounded by a constant
times $(U+|w|)^{1+\epsilon}$; its Gaussian integral is
$O(U^{1+\epsilon})$. Bounded ordinates are harmless because
this nonprincipal L-function is entire.

### Endpoint-safe Perron truncation

We prove, for fixed $1/2<u<1$ and
$\kappa\in\{1,2\}$,
$$
\boxed{\int_{-U}^{U}
\left|\sum_{n\le M}\chi(n)n^{-u-i\kappa t}\right|^4dt
\ll_{u,\epsilon}U^{1+\epsilon}}
\quad(U\ge2,\ M\ge1),
\tag{A25}
$$
with a constant independent of every real finite M.

First assume $M\le40U$. Choose fixed
$0<\eta<\min(u-1/2,1/4)$, and put
$$
x=\lfloor M\rfloor+\tfrac12,\qquad
c=1-u+\eta>0,\qquad b=\tfrac12+\eta-u<0.
$$
For $y>0$, $y\ne1$, the scalar Perron estimate is
$$
\left|\frac1{2\pi i}\int_{c-iU}^{c+iU}\frac{y^w}{w}\,dw
-\mathbf1_{y>1}\right|
\ll_c y^c\min\left(1,\frac1{U|\log y|}\right).
\tag{A26}
$$
The full vertical integral is the indicator by a residue calculation.
Integration by parts on its two tails proves the second bound.
For $|\log y|\le1/U$, pair positive and negative ordinates
in the finite integral. The real integrand is
$(c\cos(t\log y)+t\sin(t\log y))/(c^2+t^2)$.
The bounds $|\sin(t\log y)|\le t|\log y|$ and
$\int_0^Uc/(c^2+t^2)\,dt\le\pi/2$ prove the first bound.

The series for $L(u+i\kappa t+w,\chi)$ is absolutely
convergent at $\Re w=c$. Applying (A26) term by term gives
$$
L_M(u+i\kappa t,\chi)
=\frac1{2\pi i}\int_{c-iU}^{c+iU}
L(u+i\kappa t+w,\chi)\frac{x^w}{w}\,dw+E(t),
$$
$$
|E(t)|\ll_{u,\eta}
\frac{x^c}{U}+\frac{x^{1-u}\log(2x)}U.
\tag{A27}
$$
Outside $x/2<n<2x$, use $|\log(x/n)|\ge\log2$ and
$\sum n^{-u-c}=\zeta(1+\eta)$. Inside that interval use
$|\log(x/n)|\ge|x-n|/(2x)$, the coefficient bound
$n^{-u}(x/n)^c\ll x^{-u}$, and the half-integer condition
$|x-n|\ge1/2$. Summing reciprocal distances proves (A27).

Shift the finite rectangle to $\Re w=b$. The only pole is at
w=0, of residue $L(u+i\kappa t,\chi)$, because L is entire.
For $|t|\le U$, all shifted ordinates lie in $[-3U,3U]$
and real parts in $[1/2+\eta,1+\eta]$. By (A24) and Minkowski,
the normalized fourth norms of the left vertical edge and the two
horizontal edges are respectively
$$
\ll x^bU^\epsilon\log(2U),\qquad
\ll x^cU^{\epsilon-1}.
\tag{A28}
$$
For the vertical edge integrate $1/|b+iv|$ over $[-U,U]$;
for the horizontal edges integrate $x^a/U$ over $b\le a\le c$.
These estimates are uniform in the real contour coordinate.
Since $x\le41U$, $c-b=1/2$, and $b<0$, all errors in
(A27)--(A28) are bounded by $O(U^\epsilon)$, after relabeling
epsilon. Explicitly, their ratios to $x^b$ are bounded by
$\sqrt x/U$ and $x^{1/2-\eta}\log(2x)/U$, while $x^b\le1$.
Together with (A24), this proves (A25) for $M\le40U$.

For $M>40U$, use
[Martin--Ng, Proposition 3.1, equation (6)](https://www.cs.uleth.ca/~nathanng/RESEARCH/NVDVAP.pdf).
For a nonprincipal character modulo q, fixed $C_0>1$, $\Re z=u>0$,
and $x>C_0|\Im z|/(2\pi)$, it states
$$
L(z,\chi)=\sum_{n\le qx}\chi(n)n^{-z}
+O_{C_0}\left(q^{1/2-u}x^{-u}\log q
\left[1+\min\left\{\frac{u}{x\log q},\frac{|\Im z|}{u}\right\}\right]\right).
\tag{A29}
$$
Take q=5, $C_0=2$, $x=M/5$, $z=u+i\kappa t$.
Then $x>8U$, whereas $|\Im z|\le2U$. The hypothesis holds,
including at zero ordinate; the error is $O_u(M^{-u})$.
The cutoff is literal, including integer endpoints. Equation (A24)
now proves (A25) for all remaining M.

### The full Fejer mean of the two character factors

Define
$$
A_M(t)=\sum_{a\le M}\chi(a)a^{\sigma-1+it},\qquad
B_M(t)=\sum_{b\le M}\chi(b)b^{-2\sigma-2it}.
\tag{A30}
$$
Applying (A25) at $u=1-\sigma,\kappa=1$, and
$u=2\sigma,\kappa=2$, and using Holder, gives
$\int_{-U}^U|A_MB_M|^2dt\ll_{\sigma,\epsilon}U^{1+\epsilon}$.
The Fejer density satisfies
$$
\frac{d\mu_{T,3T/2}}{dt}
\ll\frac{T}{T^2+(t-3T/2)^2}.
\tag{A31}
$$
It is $O(1/T)$ on $|t|\le4T$, and $O(T/U^2)$ on
a dyadic annulus $|t|\asymp U\ge4T$. Summing the latter bounds
gives a convergent series $T^\epsilon\sum_{j\ge0}2^{-j(1-\epsilon)}$.
Choose the intermediate epsilon below 1. We have proved
$$
\boxed{\mathscr F_T(A_MB_M)\ll_{\sigma,\epsilon}T^\epsilon
\quad\text{uniformly in every finite }M\ge1.}
\tag{A32}
$$
In particular $\|A_MB_M\|_{2,T}\ll_\epsilon T^\epsilon$.
Neither (A25) nor (A32) replaces a finite time mean by a torus mean.

## 5. Pointwise bounds on the actual character progressions

Set $\theta=13/84$.
[Bourgain, Theorem 6, printed pages 20--21](https://arxiv.org/pdf/1408.5794)
proves that $(\theta+\epsilon,\theta+1/2+\epsilon)$
is an exponent pair. The theorem includes partial dyadic intervals.
The definition of exponent pairs, the A-process, and convexity are
recorded in
[Lelechenko, Definition 1 and Proposition 1](https://arxiv.org/pdf/1402.1993).
We use
$$
A(k,l)=\left(\frac{k}{2(k+1)},\frac{k+l+1}{2(k+1)}\right).
$$
With arbitrarily small epsilon enlargements understood, two applications
give
$$
\begin{array}{c|c|c}
& (k_i,l_i)&d_i=l_i-k_i\\ \hline
P_0&(13/84,55/84)&1/2\\
P_1&(13/194,152/194)&139/194\\
P_2&(13/414,359/414)&173/207 .
\end{array}
\tag{A33}
$$
Finite applications change the final epsilon by only a fixed factor.
Convexity is also immediate from taking geometric means of two upper
bounds for the same exponential sum.

Here are the details transferring these inputs to $\chi_5$.
For $\tau=|t|\ge2$, (A29) permits the literal cutoff
$D_0=\lceil10\tau\rceil$, with error $O_u(\tau^{-u})$
on any fixed line $u>0$. Indeed $D_0/5\ge2\tau>\tau/\pi$.
For any $D>D_0$, the same formula gives
$$
L(u+it,\chi)-L_D(u+it,\chi)=O_u(D^{-u}).
\tag{A34}
$$
Thus it suffices to bound all partial sums up to $D_0$.

Split integers into $n=5m+a$, $a\in\{1,2,3,4\}$.
On $m\asymp N$, the positive phase is
$\phi_a(x)=\tau\log(5x+a)/(2\pi)$. For each fixed j its
j-th derivative agrees with that of $\tau\log x/(2\pi)$
up to relative $O_j(1/N)$. The negative phase is its conjugate.
The exponent-pair class requires only finitely many derivatives
within a fixed relative tolerance. Consequently all sufficiently
large N meet those derivative conditions; the finitely bounded
smaller N are handled trivially.

There is a separate parameter restriction: the exponent-pair
parameter $(\tau/(2\pi))/N$ must exceed 1. On
$N\le c\tau$, with c a sufficiently small fixed positive constant,
the actual character progression therefore satisfies
$$
\left|\sum_{m\in I}e^{2\pi i\phi_a(m)}\right|
\ll_\epsilon \tau^{k+\epsilon}N^{l-k+\epsilon}
\tag{A35}
$$
for every partial interval I in the dyadic block and every fixed
pair used in (A33).

The remaining blocks have $N\asymp\tau$, since $D_0=O(\tau)$.
There are only a bounded number between $c\tau$ and that cutoff.
Here the second-derivative estimate
$$
\left|\sum_{m\in I}e^{2\pi i\phi(m)}\right|
\ll N\sqrt\lambda+\lambda^{-1/2}
\quad\text{if }\lambda\le|\phi''|\le C\lambda
$$
is applicable with $\lambda\asymp\tau/N^2\asymp1/\tau$.
It is
[Titchmarsh, Theorem 5.9, printed page 104](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf).
It gives $O(\sqrt\tau)$ on each such partial block, with constants
depending only on the fixed comparison range. After partial summation
with weight $(5m+a)^{-u}$, the contribution is
$O_u(\tau^{1/2-u})$, hence bounded for $u\ge1/2$.
This argument verifies the parameter restriction explicitly.

The required long-block estimate also has the following direct proof,
so that its special use here does not depend on importing any further
exponential-sum result. On $N\asymp\tau$, the derivative
$\phi_a'$ is monotone, ranges over a fixed bounded interval, and
$|\phi_a''|\asymp1/\tau$. Put $h=\tau^{-1/2}$.
For large tau, the regions where $\phi_a'$ is within $2h$
of an integer consist of a bounded number of intervals of total
length $O(h\tau)=O(\sqrt\tau)$. Bound their integer terms trivially,
including the bounded number of boundary terms. Each complementary
interval has $\phi_a'$ in $[j+h,j+1-h]$ for one integer j.
For its internal integer steps,
$\vartheta_n=\phi_a(n+1)-\phi_a(n)$ is monotone in the same
interval. Put $z_n=e^{2\pi i\phi_a(n)}$ and
$q_n=(e^{2\pi i\vartheta_n}-1)^{-1}$. Then
$z_n=q_n(z_{n+1}-z_n)$. Summation by parts bounds the sum of
$z_n$ by the endpoint sizes and total variation of $q_n$.
The identity
$$
\frac1{e^{2\pi i v}-1}=-\frac12-\frac i2\cot(\pi v)
$$
shows that this variation and the endpoint sizes are $O(1/h)$:
the cotangent is monotone between consecutive integers, and the
arguments remain h away from them. There are only a bounded number
of complementary intervals. This proves $O(\sqrt\tau)$ for every
partial long block; bounded tau can be absorbed in the constant.

For the base pair $P_0$, the smaller weighted blocks have bound
$$
\min\{N^{1-u},\,\tau^{\theta+\epsilon}N^{1/2-u+\epsilon}\}.
\tag{A36}
$$
For fixed $1/2<u<1$, split at $N=\tau^{2\theta}$.
The first geometric sum increases to that scale, and the second
decreases above it. Both cost at most
$\tau^{2\theta(1-u)+\epsilon}$, after reducing intermediate
epsilons. At $u=1/2$ there are only logarithmically many
blocks of size $O(\tau^{\theta+\epsilon})$.
Bounded t is handled uniformly in the cutoff by Abel summation of
the periodic character. Combining with (A34) proves
$$
\boxed{|L_D(u+it,\chi)|+|L(u+it,\chi)|
\ll_{u,\epsilon}(1+|t|)^{2\theta(1-u)+\epsilon},
\quad \tfrac12\le u<1,\quad D\ge1.}
\tag{A37}
$$

The processed pairs give a stronger bound on the lines needed
for the final numerical exponent. For a fixed
$u\in[1/2,173/207]$, choose the convex combination of adjacent
pairs in (A33) with $l-k=u$. After weighting, the power of N
in (A35) is zero, apart from an absorbable epsilon. Partial summation
and the preceding large-block treatment yield, uniformly in D,
$$
|L_D(u+it,\chi)|+|L(u+it,\chi)|
\ll_{u,\epsilon}(1+|t|)^{b(u)+\epsilon},
\tag{A38}
$$
where
$$
\begin{split}
b_0(u)&=\frac{13}{84}
-\frac{715}{1764}\left(u-\frac12\right),
&&\frac12\le u\le\frac{139}{194},\\
b_1(u)&=\frac{13}{194}
-\frac{1430}{4789}\left(u-\frac{139}{194}\right),
&&\frac{139}{194}\le u\le\frac{173}{207}.
\end{split}
\tag{A39}
$$
The constants may depend on the fixed u and epsilon. Both (A37)
and (A38) were derived for the four actual progressions; neither
is inferred by substituting $\chi_5$ into a zeta-only bound.

In the narrower fixed range $1/4<\sigma<0.26$,
$1-\sigma$ belongs to the second segment and $2\sigma$ to
the first. Define
$$
a_\sigma=\frac{2860\sigma-169}{9578},\qquad
b_\sigma=\frac{1261-2860\sigma}{3528},\qquad
\nu_\sigma=a_\sigma+b_\sigma .
\tag{A40}
$$
For every finite M and every real t,
$$
\boxed{|A_M(t)B_M(t)|
\ll_{\sigma,\epsilon}(1+|t|)^{\nu_\sigma+\epsilon}.}
\tag{A41}
$$
Direct substitution at the endpoints of the fixed sigma interval,
using linearity, proves $0<\nu_\sigma<\sigma$ and
$2\nu_\sigma<1$. No optimization over all known exponent pairs
is claimed.

## 6. A finite approximation with a strict error reserve

The real primitive character $\chi_5$ is even and its Gauss sum
is $\sqrt5$. The functional equation
([DLMF 25.15.5](https://dlmf.nist.gov/25.15.E5)), rewritten with the
Gamma reflection and duplication formulas, is
$$
L(s,\chi)=\mathcal X_\chi(s)L(1-s,\chi),\qquad
\mathcal X_\chi(s)=
\left(\frac5\pi\right)^{1/2-s}
\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\tag{A42}
$$
The Gauss sum value follows directly from the four residues
$2\cos(2\pi/5)-2\cos(4\pi/5)=\sqrt5$.
Write
$$
A(t)=L(1-\sigma-it,\chi),\quad
B(t)=L(2\sigma+2it,\chi),\quad
W(t)=\frac{1-5^{-s}}{\zeta_5(4s)}\mathcal X_\chi(s).
\tag{A43}
$$
Then the exact identity and its two-sided size bound are
$$
C(s)T_Y(s)=W(t)A(t)B(t)T_Y(s),\qquad
|W(t)|\asymp_\sigma T^\rho\quad(T\le t\le2T).
\tag{A44}
$$
Indeed $1-5^{-s}$ is bounded above and away from zero,
and both $\zeta_5(4s)$ and its reciprocal have bounded
absolutely convergent Euler products. Stirling's formula
([DLMF 5.11.3](https://dlmf.nist.gov/5.11.E3)) gives
$|\mathcal X_\chi(\sigma+it)|\asymp_\sigma |t|^{1/2-\sigma}$;
the exponential factors in the two Gamma moduli cancel.
There is no division by an L-function or assumption about its zeros.

Set $M=\lceil40T\rceil$. Apply (A29) with q=5,
$C_0=2$, and $x=M/5\ge8T$. The ordinates of A and B have
absolute value at most $2T$ and $4T$, respectively. Hence
$$
\|A-A_M\|_{\infty,T}\ll_\sigma T^{-(1-\sigma)},\qquad
\|B-B_M\|_{\infty,T}\ll_\sigma T^{-2\sigma}.
\tag{A45}
$$
Their fourth norms, and those of the finite factors, are
$O_\epsilon(T^\epsilon)$ by (A24)--(A25).
For $m_\sigma=\min(1-\sigma,2\sigma)>1/2$, expand
$AB-A_MB_M=(A-A_M)B+A_M(B-B_M)$. It follows that
$$
\|AB-A_MB_M\|_{2,T}\ll_{\sigma,\epsilon}T^{-m_\sigma+\epsilon}.
\tag{A46}
$$

Choose fixed parameters
$$
0<\gamma<\min(\rho,\delta)=m_\sigma-\tfrac12,\qquad
0<\beta<2\sigma,\qquad
K=\left\lceil T^{(1/2+\gamma)/\beta}\right\rceil .
\tag{A47}
$$
Define the finite rational-frequency polynomial
$$
\mathcal P(t)=A_M(t)B_M(t)S_{Y,K}(\sigma+it).
\tag{A48}
$$
Equations (A14), (A32), (A46), and (A47) give
$$
\begin{split}
\|ABT_Y-\mathcal P\|_{2,T}
&\le\|(AB-A_MB_M)T_Y\|_{2,T}
+\|A_MB_M(T_Y-S_{Y,K})\|_{2,T}\\
&\ll_{\sigma,\beta,\gamma,\epsilon}
Y^{1-\sigma}T^{-1/2-\gamma+\epsilon}.
\end{split}
\tag{A49}
$$
This is valid for $Y\ge1,T\ge2$. Multiplying by W gives
$$
\|CT_Y-W\mathcal P\|_{2,T}
\ll_{\sigma,\beta,\gamma,\epsilon}
Y^{1-\sigma}T^{-\sigma-\gamma+\epsilon}.
\tag{A50}
$$
At $Y=T^2$ this is $\mathcal B T^{-\gamma+\epsilon}$,
strictly below the target when epsilon is chosen smaller than gamma.
All cutoffs are literal and finite.

The prefix can be removed with its own strict reserve, throughout
the full strip (A2). By (A21), $|e(n)|\le1$, and $Y=T^2$,
$$
\|P_Y\|_{2,T}^2\ll_\sigma
(1+Y/T)Y^{1-2\sigma}\ll_\sigma\mathcal N^2.
\tag{A51}
$$
The absolutely bounded factors in H and the base off-line bound
(A37) at $u=2\sigma$ give
$$
\|H\|_{\infty,T}\ll_{\sigma,\epsilon}
T^{2\theta(1-2\sigma)+\epsilon}.
$$
Consequently, since $4\theta=13/21$,
$$
\boxed{\|HP_Y\|_{2,T}
\ll_{\sigma,\epsilon}\mathcal B T^{-\eta_\sigma+\epsilon},
\qquad \eta_\sigma=(1-4\theta)\rho=\frac8{21}\rho>0.}
\tag{A52}
$$
This prefix estimate needs no RH input.

Let $\gamma_*=\min(\gamma,\eta_\sigma)>0$. Since
$H(G_Y-P_Y)=CT_Y-HP_Y$, (A50)--(A52) prove
$$
\left|r_Y(T)-\|W\mathcal P\|_{2,T}\right|
\ll_{\sigma,\beta,\gamma,\epsilon}
\mathcal B T^{-\gamma_*+\epsilon},\qquad Y=T^2.
\tag{A53}
$$
The two-sided bound for W in (A44) now proves the equivalence of
the following families of proposed bounds:
$$
\boxed{
\begin{array}{c}
r_Y(\sqrt Y)\ll_\epsilon Y^{1-3\sigma/2+\epsilon}
\quad\text{for every }\epsilon>0\\
\Longleftrightarrow\\
\|\mathcal P\|_{2,T}^2\ll_\epsilon
\mathcal N^2T^\epsilon
\quad\text{for every }\epsilon>0,\quad Y=T^2 .
\end{array}}
\tag{A54}
$$
All fixed parameters may enter the constants; epsilon is relabeled
between squared norms and between T and Y. This proves an equivalence,
not either open bound. A merely one-sided estimate for W would not
justify the reverse implication.

## 7. Exact rational coefficients and the local criterion

For coprime positive j,k, define the finite real rational coefficient
$$
J(j,k)=
\sum_{\substack{a,b\le M,\ v\le K,\ r\le Y\\
r\in\mathcal R,\ \operatorname{rad}(v)\mid r\\
k r(vb)^2=j a}}
\frac{\chi(a)\chi(b)f(r)(-1)^{\Omega(v)}}a.
\tag{A55}
$$
Nonzero coefficients have $j\le\lfloor YK^2M^2\rfloor$ and
$k\le M$. The identity $r(vb)^2/a=j/k$ shows exactly that
$$
\mathcal P(t)=\sum_{(j,k)=1}J(j,k)(j/k)^{-\sigma-it}.
\tag{A56}
$$
In particular the factor $1/a$ in (A55) has not been omitted.
All equal rational frequencies are combined before squaring.

With $c_\lambda=J(j,k)(j/k)^{-\sigma}$, $\lambda=j/k$,
the sharp norm in (A54) is the exact finite quadratic form
$$
\sum_{\lambda,\mu}c_\lambda c_\mu
\mathcal K_T(\log(\mu/\lambda)),\qquad
\mathcal K_T(u)=
\begin{cases}
(e^{2iTu}-e^{iTu})/(iTu),&u\ne0,\\
1,&u=0.
\end{cases}
\tag{A57}
$$
The sum is real because both orientations occur. Equations
(A17)--(A20) give a different, nonnegative global form with the
compactly supported logarithmic kernel (A18).
Thus
$$
\mathscr F_T(\mathcal P)\ll_\epsilon\mathcal N^2T^\epsilon
\tag{A58}
$$
is a sufficient condition for (A54), with no converse asserted.
The coefficient and prime appendices retain the actual signed
terms of this form. Neither unequal rational frequencies nor their
finite support permits close pairs to be discarded.

## 8. The established global Fejer and analytic bounds

First, a bound for the unweighted support polynomial is uniform in
every finite K and every time height $V\ge2$:
$$
\boxed{\|S_{Y,K}\|_{2,V}
\ll_\sigma\sqrt{1+\log Y}
\left(Y^{1/2-\sigma}+\frac{Y^{1-\sigma}}{\sqrt V}\right).}
\tag{A59}
$$
It holds on either positive or negative dyadic intervals. For
$$
F_U^{(k)}(s)=
\sum_{\substack{r\le U,\ r\in\mathcal R\\(r,k)=1}}f(r)r^{-s},
\tag{A60}
$$
(A11) and (A21) imply
$$
\|F_U^{(k)}\|_{2,V}
\ll_\sigma\sqrt{1+\log U}
\left(U^{1/2-\sigma}+\frac{U^{1-\sigma}}{\sqrt V}\right)
$$
uniformly in k. In the v-th term of (A13), put
$k=\operatorname{rad}(v)$ and factor $r=kw$.
The two displayed powers gain weights $2^{\omega(k)}/\sqrt k$
and $2^{\omega(k)}/k$, respectively. Minkowski over v is justified
by convergence of the two positive Euler products
$$
\prod_{p\ {\rm split}}
\left(1+\frac2{\sqrt p(p^{2\sigma}-1)}\right),\qquad
\prod_{p\ {\rm split}}
\left(1+\frac2{p(p^{2\sigma}-1)}\right).
\tag{A61}
$$
The first converges exactly in the strict range needed here,
$\sigma>1/4$; the second also converges there. This proves (A59)
with no loss depending on K.

Now restrict to $1/4<\sigma<0.26$ and use (A40).
Combining the uniform pointwise estimate (A41) with (A59) bounds
the unnormalized integral of $|\mathcal P|^2$ on
$|t|\asymp V\ge2$ by
$$
\ll_{\sigma,\epsilon}(1+\log Y)
\left(Y^{1-2\sigma}V^{1+2\nu_\sigma+\epsilon}
+Y^{2-2\sigma}V^{2\nu_\sigma+\epsilon}\right).
\tag{A62}
$$
The same statement holds for arbitrary finite M,K. On
$|t|\le2$, Abel summation bounds A and B uniformly in M,
while (A14) bounds S by $O(Y^{1-\sigma})$.

Integrate (A62) against the actual Fejer density. For $V\le4T$
use $O(1/T)$; because $\nu_\sigma>0$, the dyadic sums
are dominated by their largest scales. For $V\ge4T$, use
$O(T/V^2)$ from (A31). The resulting series have powers
$V^{2\nu_\sigma-1+\epsilon}$ and
$V^{2\nu_\sigma-2+\epsilon}$, which decrease geometrically
after epsilon is chosen small enough. The bounded-height piece
costs $O(Y^{2-2\sigma}/T)$. We obtain
$$
\mathscr F_T(\mathcal P)\ll_{\sigma,\epsilon}(1+\log Y)
\left(Y^{1-2\sigma}T^{2\nu_\sigma+\epsilon}
+Y^{2-2\sigma}T^{2\nu_\sigma-1+\epsilon}\right).
\tag{A63}
$$
This proof controls all real times, not only $[T,2T]$.
At $Y=T^2$, absorb logarithms in epsilon:
$$
\boxed{\mathscr F_T(\mathcal P)\ll_{\sigma,\epsilon}
\mathcal N^2T^{2\nu_\sigma+\epsilon}
\quad\text{uniformly in every finite }M,K.}
\tag{A64}
$$
For the prescribed cutoffs (A47)--(A48), (A19), (A44), and (A53)
give the analytic consequence
$$
\boxed{r_Y(\sqrt Y)\ll_{\sigma,\epsilon}
Y^{1-3\sigma/2+\nu_\sigma/2+\epsilon},
\qquad \tfrac14<\sigma<0.26.}
\tag{A65}
$$
At $\sigma=51/200$,
$$
\nu_\sigma=\frac{7069361}{33791184},\qquad
1-\frac{3\sigma}{2}+\frac{\nu_\sigma}{2}
=0.722103629\ldots .
\tag{A66}
$$
The decimal is a rounded display of the exact expression. The
analytic target has exponent $0.6175$, so (A65) does not prove it.
The global nature of (A64), together with the actual positive and
negative families in [PRIME-CANCELLATION.md](PRIME-CANCELLATION.md),
does prove the compensation statements there without assuming (A58).

## 9. A reduced sufficient input with no long auxiliary v cutoff

There is another exact grouping of the analytic support factor.
For $\Re s>0$, group (A13) by $k=\operatorname{rad}(v)$.
Since
$$
\sum_{\operatorname{rad}(v)=k}(-1)^{\Omega(v)}v^{-2s}
=\prod_{p\mid k}\frac{-p^{-2s}}{1+p^{-2s}},
$$
and factoring $r=kw$ contributes $f(k)k^{-s}$, the two signs
combine to give
$$
\boxed{T_Y(s)=\sum_{\substack{k\le Y\\k\in\mathcal R}}
D_k(s)F_{Y/k}^{(k)}(s),\qquad
D_k(s)=\frac{2^{\omega(k)}k^{-3s}}
{\prod_{p\mid k}(1+p^{-2s})}.}
\tag{A67}
$$
This is a finite sum in k. The remaining coefficients f in F
retain their signs.

Put $V_\sigma(k)=\prod_{p\mid k}(1-p^{-2\sigma})^{-1}$.
For every fixed $0<\beta<2\sigma$, (A11) and (A67) imply
$$
\sup_t\left|\sum_{\substack{k>R\\k\le Y,\ k\in\mathcal R}}
D_k(s)F_{Y/k}^{(k)}(s)\right|
\ll_{\sigma,\beta}Y^{1-\sigma}R^{-\beta}.
\tag{A68}
$$
Indeed $|D_k|\le2^{\omega(k)}k^{-3\sigma}V_\sigma(k)$;
after bounding $F_{Y/k}^{(k)}$ by $(Y/k)^{1-\sigma}$,
the positive remainder is bounded by
$$
Y^{1-\sigma}R^{-\beta}
\prod_{p\ {\rm split}}
\left(1+\frac2{p^{1+2\sigma-\beta}(1-p^{-2\sigma})}\right).
\tag{A69}
$$
The Euler product converges in the stated strict range.

This reduction is valid on the whole strip (A2).
Choose fixed $1/(4\sigma)<\kappa<1$, put $R=T^\kappa$,
and choose $\beta<2\sigma$ with $\kappa\beta>1/2$.
By (A32), multiplication of (A68) by $A_MB_M$ costs only
$T^\epsilon$ in second norm. At $Y=T^2$, the discarded part
is therefore
$$
O_{\sigma,\beta,\epsilon}
\bigl(Y^{1-\sigma}T^{-\kappa\beta+\epsilon}\bigr)
=O\bigl(\mathcal N T^{-(\kappa\beta-1/2)+\epsilon}\bigr).
\tag{A70}
$$
It is strictly below the target.

It follows that the following single family of joint bounds would
be sufficient:
$$
\boxed{\|A_MB_MF_{Y/k}^{(k)}\|_{2,T}
\ \stackrel{?}{\ll}_{\sigma,\kappa,\epsilon}\
(Y/k)^{1-\sigma}T^{-1/2+\epsilon},
\quad k\in\mathcal R,\quad k\le T^\kappa,\quad Y=T^2.}
\tag{A71}
$$
The implied constant must be independent of k. To verify the
implication, multiply (A71) by $\|D_k\|_\infty$, sum, and
use the convergent product (A69) with beta zero. This yields
$\|A_MB_MT_Y\|_{2,T}\ll\mathcal N T^\epsilon$, with
(A70) handling large radicals. Replacing $A_MB_M$ by AB costs
at most $Y^{1-\sigma}T^{-m_\sigma+\epsilon}$ by (A14),(A46),
which is also below $\mathcal N$. Finally apply (A44),(A52).
This proves the sufficiency for the original analytic target.

Every surviving bare length is $Y/k\ge T^{2-\kappa}>T$.
The exclusion $(r,k)=1$ and the common time weight
$|A_MB_M|^2$ are part of (A71). An unweighted short-sum bound
has not been substituted for this joint estimate.
Equation (A71) is neither proved here nor deduced from the target.

## 10. The precise limit of the available separate-moment interpolation

This section again uses $1/4<\sigma<0.26$, with $a_\sigma$,
$b_\sigma$, and $\nu_\sigma$ as in (A40), and $Y=T^2$.
Equation (A59) and the absolute bound (A14) imply, with logarithms
absorbed,
$$
\|S_{Y,K}\|_2\ll_\epsilon\mathcal N T^\epsilon,\qquad
\|S_{Y,K}\|_\infty\ll_\sigma\mathcal N T^{1/2}.
$$
The fourth moments (A25) and the pointwise bounds (A38) give,
for every fixed $p\ge4$,
$$
\|A_M\|_p\ll_\epsilon T^{a_\sigma(1-4/p)+\epsilon},
\qquad
\|B_M\|_p\ll_\epsilon T^{b_\sigma(1-4/p)+\epsilon}.
\tag{A72}
$$
For $q\ge2$, interpolation similarly gives
$\|S_{Y,K}\|_q\ll_\epsilon\mathcal N T^{1/2-1/q+\epsilon}$. Use Holder with
$p_A,p_B\ge4$ and $1/q=1/2-1/p_A-1/p_B$.
The resulting loss in norm above $\mathcal N$ is exactly
$$
d=\nu_\sigma+
\frac{1-4a_\sigma}{p_A}+\frac{1-4b_\sigma}{p_B}.
\tag{A73}
$$
Both numerators are positive in this fixed strip. The minimum
over this entire interpolation family is $\nu_\sigma$, attained
at $p_A=p_B=\infty$, which is the input already used in (A62).
Thus these separate fourth moments, the support second moment,
and elementary interpolation do not improve that power.

This is a limitation of specified available upper-bound certificates.
It is not a lower bound for the true joint moment, a statement
excluding higher-moment or spectral methods, or evidence against
the target. A new joint estimate such as (A71), or a direct bound
for the complete signed Fejer form, is still required.
