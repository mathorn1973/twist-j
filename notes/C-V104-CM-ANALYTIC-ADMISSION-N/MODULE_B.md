# Module B. The size of the reachable primitive polarization family

**Status: NON-CANONICAL.** This is an unconditional classical counting
theorem on the fixed complex abelian surface of [Module A](MODULE_A.md).
Its proof imports one explicitly specified mean-value theorem and a
fixed-modulus prime number theorem. It assumes neither RH nor GRH.

The geometric input is the polarization/ideal bijection in the
[public fixed-model geometric dictionary](https://github.com/mathorn1973/twist-j/blob/655e022d0ef95ee94681464d3325d2aa589df1d6/notes/C-RH-CM5-HECKE-DICTIONARY-N/CM5_POLARIZATIONS.md).
The analytic convention reference is
[public full-character normalization](https://github.com/mathorn1973/twist-j/blob/655e022d0ef95ee94681464d3325d2aa589df1d6/notes/C-RH-CM5-HECKE-DICTIONARY-N/HECKE_MAASS_BRIDGE.md).
Only its principal-mode convention, L_F(s,Xi_0) = zeta_F(s), is relevant
here; no nonzero mode or sector theorem is used.

## B.1. What is counted

Keep
$$
K=\mathbb Q(\zeta_5),\qquad F=\mathbb Q(\sqrt5),\qquad
\phi=\frac{1+\sqrt5}{2},\qquad L=\log\phi.
$$
For a totally positive $\eta=x+y\phi\in\mathcal O_F$, put
$$
q(D_\eta)=\frac{D_\eta^2}{2}
 =N_{F/\mathbb Q}(\eta)=x^2+xy-y^2.
$$
The norm variable is $q$; the polarization isogeny has degree $q^2$.
The equivalence relation is pullback by $\operatorname{Aut}(B,0)$.

For an integer $n\ge1$, define
$$
\boxed{
r(n)=\#\{[D_\eta]: q(D_\eta)=n,\ \gcd(x,y)=1,\
 [D_\eta]\text{ is reachable from }[D_1]\}.
}
\tag{B1}
$$
Reachability uses exactly the integral pullbacks specified in Module A,
including the identity. Thus $r$ counts primitive polarization classes,
not integers represented by a norm and not the endomorphisms realizing
a class. In particular $r(1)=1$.

Under the ideal bijection $[D_\eta]\mapsto(\eta)$, primitivity means
that the ideal is not contained in $(c)$ for any integer $c>1$.
Indeed, $(\eta)\subseteq(c)$ is equivalent to $\eta/c\in\mathcal O_F$.
Multiplication by a positive unit is an invertible integral map of
$\mathcal O_F$, so content and primitivity are invariant on orbits.
For the fixed benchmark this is equivalently polarization type $(1,n)$.

For the rest of the proof, let $\rho(n)$ count **all** primitive
polarization classes of norm $n$, with no reachability restriction.
The symbols $r$ and $\rho$ have different meanings.

## B.2. Complete local classification

Let $p$ be a rational prime. The ordinary splitting in $F/\mathbb Q$
and the relative splitting in $K/F$ must both be retained.

### Split primes of F

For $p\equiv1,4\pmod5$, write
$$
(p)=\mathfrak p\mathfrak p',\qquad
N\mathfrak p=N\mathfrak p'=p.
$$
The local part of an integral F-ideal is
$\mathfrak p^a(\mathfrak p')^b$, with $a,b\ge0$.
It is primitive at $p$ precisely when $\min(a,b)=0$. At norm
$p^\nu$, $\nu\ge1$, the two possibilities are therefore
$\mathfrak p^\nu$ and $(\mathfrak p')^\nu$.

If $p\equiv1\pmod5$, both F-primes split in $K/F$, so Module A
imposes no parity condition. Both classes are reachable for every
$\nu\ge1$.

If $p\equiv4\pmod5$, both F-primes are inert in $K/F$. A primitive
class is reachable precisely when its nonzero valuation $\nu$ is
even. The two classes survive for even $\nu$, and none survives for
odd $\nu$. Counting a norm alone would lose this factor of two.

### Inert rational primes

For $p\equiv2,3\pmod5$, the sole F-prime is $(p)$ and has norm
$p^2$. Any positive power of it already has rational content.
Consequently it contributes no nontrivial primitive class, whatever
the relative norm criterion says about its valuation. Its primitive
local factor is $1$. The missing rational primes in $R(s)$ are
therefore explained by primitivity, not by discarding an Euler factor.

### The prime over 5

Write $\mathfrak q_5=(\sqrt5)$; then
$$
(5)=\mathfrak q_5^2,\qquad N\mathfrak q_5=5.
$$
Primitivity permits exactly exponents $0$ and $1$. The relative
extension ramifies at this prime and has residue degree one, so Module A
permits both exponents. The class of exponent one is explicitly
realized by $\phi(1-\zeta_5)$.

### Local coefficients and Euler factors

Put $T=p^{-s}$. The preceding classification gives every exponent:

| Rational prime | $r(p^\nu)$, $\nu\ge1$ | $R_p(s)=\sum_{\nu\ge0}r(p^\nu)T^\nu$ |
| --- | --- | --- |
| $p\equiv1\pmod5$ | $2$ | $(1+T)/(1-T)$ |
| $p\equiv4\pmod5$ | $2$ for even $\nu$, $0$ for odd $\nu$ | $(1+T^2)/(1-T^2)$ |
| $p\equiv2,3\pmod5$ | $0$ | $1$ |
| $p=5$ | $1$ for $\nu=1$, $0$ for $\nu\ge2$ | $1+T$ |

These are geometric series, so the table is not restricted to a finite
coefficient check. Unique ideal factorization makes local choices at
distinct rational primes independent. All resulting F-ideals have
totally positive generators and give exactly one orbit each, by Module A.
Thus $r$ is nonnegative and multiplicative, and
$$
r(n)=
\begin{cases}
2^{\omega_{1,4}(n)},&
v_5(n)\le1,\quad
p\mid n,\ p\ne5\Rightarrow p\equiv1,4\pmod5,\quad
v_p(n)\text{ even for }p\equiv4\pmod5,\\
0,&\text{otherwise}.
\end{cases}
\tag{B2}
$$
Here $\omega_{1,4}(n)$ counts distinct rational prime divisors in the
two indicated classes; it is zero for $n=1$.

Since $0\le r(n)\le\rho(n)\le a_F(n)$, where $a_F(n)$ counts
all integral F-ideals of norm $n$, the series converges absolutely
for $\Re s>1$. The complete Euler product is
$$
\boxed{
R(s)=\sum_{n\ge1}\frac{r(n)}{n^s}
=(1+5^{-s})
\prod_{p\equiv1\ (5)}\frac{1+p^{-s}}{1-p^{-s}}
\prod_{p\equiv4\ (5)}\frac{1+p^{-2s}}{1-p^{-2s}},
\qquad\Re s>1.
}
\tag{B3}
$$

## B.3. The precise mean-value theorem

We use R. de la Bretèche and G. Tenenbaum,
*Remarks on the Selberg--Delange method*,
**arXiv:2010.12929v8, revision 24 June 2025, Theorem 2.1,
printed page 4, equation (2.1)**:
[version record](https://arxiv.org/abs/2010.12929v8),
[PDF](https://arxiv.org/pdf/2010.12929v8).
The retrieved PDF has 423456 bytes and SHA-256
cc20403e28ec1513664bc10c528473f8b20744135e3582580a769a588fee688f.
This is the corrected arXiv version of the article published in
*Acta Arithmetica* 200.4 (2021), 349--369.

Here is the theorem in notation that separates its parameter
$\alpha$ from our function $r(n)$. Suppose $f$ is nonnegative
and multiplicative, $A>0$, $0<\sigma_0<1$, $\alpha>0$, and
$$
\sum_{p\le x}f(p)\log p
=\alpha x+O\!\left(\frac{x}{(\log x)^A}\right)
\quad(x>2),
\tag{B4}
$$
$$
\sum_p\left\{\frac{f(p)^2}{p^{2\sigma_0}}
 +\sum_{\nu\ge2}\frac{f(p^\nu)}{p^{\nu\sigma_0}}\right\}<\infty.
\tag{B5}
$$
The theorem yields
$$
\sum_{n\le x}f(n)
=\lambda_0(f)x(\log x)^{\alpha-1}
\left\{1+
O\!\left(
\frac{(\log\log x)^{\mathbf1_{\{A=1\}}}}
 {(\log x)^{\min(1,A)}}\right)\right\},
\tag{B6}
$$
with
$$
\lambda_0(f)=\frac1{\Gamma(\alpha)}
\prod_p\left[(1-p^{-1})^\alpha
\sum_{\nu\ge0}\frac{f(p^\nu)}{p^\nu}\right].
\tag{B7}
$$
The product in (B7) is taken in increasing-prime order. Its convergence
and its identification with an absolutely convergent expression in the
present case are proved below.

### Verification of all hypotheses

Set
$$
f=r,\qquad A=2,\qquad \sigma_0=\frac34,\qquad\alpha=\frac12.
\tag{B8}
$$
The required positivity and multiplicativity follow from B.2.
All three parameter restrictions are satisfied.

For the prime mean, let
$$
\vartheta(x;5,1)=\sum_{\substack{p\le x\\p\equiv1\ (5)}}\log p.
$$
The local table gives the exact identity
$$
\sum_{p\le x}r(p)\log p
=2\vartheta(x;5,1)+\mathbf1_{\{x\ge5\}}\log5.
\tag{B9}
$$
The unconditional fixed-modulus prime number theorem supplies
$$
\vartheta(x;5,1)=\frac{x}{4}
 +O\!\left(\frac{x}{(\log x)^2}\right).
\tag{B10}
$$
For a precise primary reference, Terence Tao's
[*254A, Notes 2: Complex-analytic multiplicative number theory*,
9 December 2014, Exercise 64](https://terrytao.wordpress.com/2014/12/09/254a-notes-2-complex-analytic-multiplicative-number-theory/)
states the corresponding estimate for
$\sum_{n\le x,\ n\equiv1\ (5)}\Lambda(n)$.
Removing higher prime powers costs at most
$O(\sqrt x(\log x)^2)$: every such prime is at most $\sqrt x$,
and there are at most $\log_2 x$ possible exponents, each weighted
by at most $\log x$. This error is absorbed into
$O(x/(\log x)^2)$. The modulus is fixed at $5$; no growing-modulus
or short-interval assertion is required. The bounded correction
$\mathbf1_{\{x\ge5\}}\log5$ in (B9) is absorbed as well.
Equations (B9)--(B10) therefore prove (B4) with $\alpha=1/2$.

For (B5), the complete prime-power table gives
$0\le r(p^\nu)\le2$ for every prime and every $\nu\ge1$.
In particular
$$
\begin{aligned}
&\sum_p\left\{\frac{r(p)^2}{p^{3/2}}
 +\sum_{\nu\ge2}\frac{r(p^\nu)}{p^{3\nu/4}}\right\}\\
&\quad\le
\sum_p\left(4p^{-3/2}
 +\frac{2p^{-3/2}}{1-p^{-3/4}}\right)\\
&\quad\le
\left(4+\frac2{1-2^{-3/4}}\right)\sum_p p^{-3/2}
<\infty.
\end{aligned}
\tag{B11}
$$
This includes the squares and every higher power, not only the
first-order terms of the Euler product.

These are every hypothesis of Theorem 2.1. In particular, this
application uses no additional short-interval condition from Theorem
1.1 and no unverified condition from Theorem 1.2.

### Reachable-class asymptotic

Equations (B6)--(B11), with $\Gamma(1/2)=\sqrt\pi$, give
$$
\boxed{
\sum_{n\le X}r(n)
=C_{\rm rel}\frac{X}{\sqrt{\log X}}
\left(1+O\!\left(\frac1{\log X}\right)\right).
}
\tag{B12}
$$
The exceptional $\log\log X$ factor in the cited theorem occurs at
$A=1$; our choice $A=2$ avoids it. A positive exact expression
for $C_{\rm rel}$ follows next. No numerical onset of the asymptotic
or explicit numerical bound for its implied constant is asserted.

## B.4. An absolutely convergent expression for the constant

### Removing the half-pole

Define the primitive quartic Dirichlet character $\chi$ modulo $5$
by $\chi(2)=i$, with $\chi(n)=0$ when $5\mid n$.
The residue values are
$$
\begin{array}{c|rrrr}
a\bmod5&1&2&3&4\\ \hline
\chi(a)&1&i&-i&-1\\
\chi_5(a)=\chi(a)^2&1&-1&-1&1
\end{array}.
\tag{B13}
$$
For $K=\mathbb Q(\zeta_5)$, the rational-prime Euler factors are
$$
\zeta_{K,p}(s)=
\begin{cases}
(1-T)^{-4},&p\equiv1\pmod5,\\
(1-T^2)^{-2},&p\equiv4\pmod5,\\
(1-T^4)^{-1},&p\equiv2,3\pmod5,\\
(1-T)^{-1},&p=5.
\end{cases}
\tag{B14}
$$
The splitting table of Module A proves (B14). Multiplying the
Dirichlet factors from (B13), including the prime $5$, gives
$$
\zeta_K(s)=\zeta(s)L(s,\chi_5)L(s,\chi)L(s,\overline\chi).
\tag{B15}
$$
Thus no separate unproved identification of an L-function is needed.

Comparison of (B3) and (B14) gives
$$
R(s)=\zeta_K(s)^{1/2}H(s),\qquad\Re s>1,
\tag{B16}
$$
where
$$
\begin{aligned}
H(s)={}&(1+5^{-s})(1-5^{-s})^{1/2}\\
&{}\times\prod_{p\equiv1\ (5)}(1-p^{-2s})
\prod_{p\equiv4\ (5)}(1+p^{-2s})
\prod_{p\equiv2,3\ (5)}(1-p^{-4s})^{1/2}.
\end{aligned}
\tag{B17}
$$
The square roots on $\Re s>1$ are those defined by the Euler
logarithms and positive values for real $s>1$. The roots in $H$
are equivalently obtained from the power-series logarithm of
$1-p^{-ks}$, normalized to approach $1$ as $\Re s\to+\infty$.

Every infinite-product factor in (B17) differs from $1$ by
$O(p^{-2\Re s})$, or by $O(p^{-4\Re s})$. The logarithms
therefore converge absolutely and locally uniformly for $\Re s>1/2$.
In particular $H(1)>0$. This continuation statement concerns $H$.
It does not assert that a square root of $\zeta_K$ has a
single-valued zero-free continuation throughout that half-plane.

### Identification with the theorem's constant

Theorem 2.1 initially gives
$$
C_{\rm rel}=\frac1{\sqrt\pi}
\prod_p(1-p^{-1})^{1/2}R_p(1).
\tag{B18}
$$
To relate it rigorously to (B17), put $b_p=r(p)-1/2$.
The same fixed-modulus prime number theorem used in (B10) gives
$\vartheta(y;5,a)=y/4+O(y/(\log y)^2)$ for each of the four
reduced residue classes $a=1,2,3,4$. Summing these estimates and
adding the possible contribution of the prime $5$ proves
$\vartheta(y)=y+O(y/(\log y)^2)$. Together with the prime mean
above, this quantitative estimate implies
$$
S(y):=\sum_{p\le y}b_p\log p
=O\!\left(\frac{y}{(\log y)^2}\right).
$$
Partial summation against $1/(t\log t)$ shows that
$\sum_p b_p/p$ converges, with a tail
$O((\log y)^{-2})$. More explicitly, the boundary term is
$O((\log y)^{-3})$, and the tail integral is bounded by a constant
times $\int_y^\infty dt/(t(\log t)^3)$.

Uniformly for real $1\le s\le2$, the same argument against
$t^{-s}/\log t$ bounds the corresponding tails uniformly. Also,
using the local table,
$$
\log\big((1-p^{-s})^{1/2}R_p(s)\big)
=b_pp^{-s}+O(p^{-2s})
$$
uniformly for $p$ and $1\le s\le2$. The absolutely summable
remainder and the uniform tail justify passing from the ordered
product at $1$ to the limit $s\downarrow1$. All factors are
positive at real $s=1$. The product is finite and strictly positive.
It is not absolutely convergent: the linear coefficients satisfy
$|b_p|\ge1/2$, and $\sum_p p^{-1}$ diverges.

On the other hand, (B15)--(B17) and continuity of the nonprincipal
Dirichlet L-series at $1$ give
$$
\boxed{
C_{\rm rel}
=\frac{H(1)}{\sqrt\pi}
\sqrt{L(1,\chi_5)\,|L(1,\chi)|^2}.
}
\tag{B19}
$$
The root is the positive real root. The evaluations below prove
directly that both L-values contributing to its square are nonzero.
Formula (B19) is an exact L-value expression with an absolutely
convergent residual Euler product.

### Evaluation of the L-values

First,
$$
L(1,\chi_5)=\frac{2L}{\sqrt5}.
\tag{B20}
$$
Here is a short derivation so this normalization can be checked
without an unpinned class-number formula. With
$\zeta=e^{2\pi i/5}$, the explicit quadratic Gauss sum is
$$
\sum_{a=1}^4\chi_5(a)\zeta^a
=(\zeta+\zeta^4)-(\zeta^2+\zeta^3)
=(\phi-1)+\phi=\sqrt5.
$$
Replacing $a$ by $na$ proves
$\sum_a\chi_5(a)\zeta^{an}=\sqrt5\,\chi_5(n)$, including
the zero case $5\mid n$. For $0<t<1$, insert this identity into
the absolutely convergent power series
$-\log(1-t\zeta^a)=\sum_{n\ge1}t^n\zeta^{an}/n$.
The bounded partial sums of $\chi_5$ justify the Abel limit
$t\uparrow1$. Pairing $a$ with $5-a$ gives real logarithms,
hence
$$
L(1,\chi_5)
=\frac2{\sqrt5}\log
\frac{\sin(2\pi/5)}{\sin(\pi/5)}
=\frac2{\sqrt5}\log\phi.
$$
The last identity follows from
$2\cos(\pi/5)=\phi$.

For the quartic character, pair the odd character's residue values
within each consecutive block:
$$
\begin{aligned}
L(1,\chi)
={}&\sum_{k\ge0}
\left(\frac1{5k+1}-\frac1{5k+4}\right)\\
&{}+i\sum_{k\ge0}
\left(\frac1{5k+2}-\frac1{5k+3}\right)\\
={}&\frac\pi5
\left(\cot\frac\pi5+i\cot\frac{2\pi}5\right).
\end{aligned}
\tag{B21}
$$
The paired sums converge absolutely. Their evaluation uses the
cotangent partial-fraction formula, for example
[NIST DLMF 4.22.3](https://dlmf.nist.gov/4.22.E3);
pairing the terms indexed by positive and negative integers yields
exactly the two differences above.

For completeness the algebra behind the absolute square is
$$
\cot^2\frac\pi5=\frac{\phi+1}{3-\phi},\qquad
\cot^2\frac{2\pi}5=\frac{2-\phi}{2+\phi}.
$$
Their common denominator is
$(3-\phi)(2+\phi)=5$, while the summed numerator is
$$
(\phi+1)(\phi+2)+(2-\phi)(3-\phi)
=(4\phi+3)+(7-4\phi)=10.
$$
Therefore
$$
\boxed{|L(1,\chi)|^2=\frac{2\pi^2}{25}.}
\tag{B22}
$$

### Final positive Euler product

Define
$$
\boxed{
\mathcal P=
\prod_{p\equiv1\ (5)}(1-p^{-2})
\prod_{p\equiv4\ (5)}(1+p^{-2})
\prod_{p\equiv2,3\ (5)}(1-p^{-4})^{1/2}.
}
\tag{B23}
$$
Every root here is positive. The product is absolutely convergent and
strictly positive by the argument for $H(1)$.
The finite factor at $5$ is
$$
H(1)=(1+1/5)(1-1/5)^{1/2}\mathcal P
=\frac{12}{5\sqrt5}\mathcal P.
$$
Substituting (B20) and (B22) into (B19) proves the explicit form
$$
\boxed{
C_{\rm rel}
=\frac{24\sqrt{\pi L}}{5^{11/4}}\,\mathcal P>0.
}
\tag{B24}
$$
The values (B19) and (B24) are equivalent. No fitted decimal constant
or numerical Euler-product truncation is needed.

## B.5. The denominator, proved separately without a census

This section proves the total primitive-class estimate required for
the ratio. It constructs no lattice census or angular sector and uses only the inherited
ideal bijection and elementary Dirichlet convolution.

Let
$$
a_F(n)=\#\{\mathfrak a\subset\mathcal O_F:N\mathfrak a=n\},
\qquad A_{\rm all}(X)=\sum_{n\le X}a_F(n).
$$
The quadratic Euler factors, or
$\zeta_F(s)=\zeta(s)L(s,\chi_5)$, give
$$
a_F(n)=\sum_{d\mid n}\chi_5(d).
\tag{B25}
$$
This identity counts all polarization classes. It is separate from
the restricted function $r(n)$.

Set $S_\chi(t)=\sum_{n\le t}\chi_5(n)$.
One period of $\chi_5$ is $(1,-1,-1,1,0)$, with partial sums
$(1,0,-1,0,0)$; hence $|S_\chi(t)|\le1$ for every real $t$.
For real $X\ge1$, put $u=\lfloor\sqrt X\rfloor$.
The exact hyperbola identity is
$$
\begin{aligned}
A_{\rm all}(X)
={}&\sum_{d\le u}\chi_5(d)\left\lfloor\frac Xd\right\rfloor\\
&{}+\sum_{a\le u}S_\chi(X/a)-uS_\chi(u).
\end{aligned}
\tag{B26}
$$
Indeed, $a,d>u$ implies $ad\ge(u+1)^2>X$, while the entire
overlap rectangle $a,d\le u$ lies below $X$. Thus (B26) also
handles perfect squares and nonintegral $X$.

The second term and the overlap are $O(u)$. The first term is
$$
X\sum_{d\le u}\frac{\chi_5(d)}d+O(u)
=XL(1,\chi_5)+O(X/u+u).
$$
The tail of the L-series is $O(1/u)$ by partial summation and the
bound on $S_\chi$. Since $X/u\le2\sqrt X$, this proves
$$
A_{\rm all}(X)=\frac{2L}{\sqrt5}X+O(\sqrt X).
\tag{B27}
$$

Every totally positive element has a unique decomposition
$\eta=c\eta_0$, where $c=\gcd(x,y)>0$ and $\eta_0$ is
primitive and totally positive. Its orbit decomposition is also
unique because content is invariant under positive units. Norms
scale by $c^2$. Consequently
$$
a_F(n)=\sum_{c^2\mid n}\rho(n/c^2),\qquad
A_{\rm prim}(X):=\sum_{n\le X}\rho(n)
=\sum_{c\le\sqrt X}\mu(c)A_{\rm all}(X/c^2).
\tag{B28}
$$
These identities classify **all** classes. They do not assert that
division by $c$ is an allowed pullback operation or that it preserves
reachability.

Apply (B27) inside the finite sum:
$$
\begin{aligned}
A_{\rm prim}(X)
={}&\frac{2L}{\sqrt5}X
\sum_{c\le\sqrt X}\frac{\mu(c)}{c^2}
 +O\!\left(\sqrt X\sum_{c\le\sqrt X}\frac1c\right).
\end{aligned}
$$
The absolutely convergent main series is $1/\zeta(2)$; its omitted
tail is $O(X^{-1/2})$. The harmonic sum is $O(\log(2X))$.
We have therefore independently proved the required denominator,
with an error estimate:
$$
\boxed{
A_{\rm prim}(X)
=\frac{2L}{\sqrt5\,\zeta(2)}X
 +O(\sqrt X\log(2X)).
}
\tag{B29}
$$

## B.6. The proportion and its exact scope

Divide (B12) by (B29). The denominator's relative error is
$O(\log X/\sqrt X)=o(1/\log X)$. Therefore
$$
\boxed{
\frac{\sum_{n\le X}r(n)}{A_{\rm prim}(X)}
=\frac{\kappa_{\rm rel}}{\sqrt{\log X}}
\left(1+O\!\left(\frac1{\log X}\right)\right)
\longrightarrow0,
}
\tag{B30}
$$
where
$$
\boxed{
\kappa_{\rm rel}
=\frac{\sqrt5\,\zeta(2)}{2L}C_{\rm rel}
=\frac{2\pi^{5/2}}{5^{9/4}\sqrt L}\,\mathcal P>0.
}
\tag{B31}
$$
The second form uses $\zeta(2)=\pi^2/6$.

This is a zero proportion **among primitive polarization classes,
ordered by $q(D)\le X$**. It is not a density of the integers $n$,
a density of endomorphisms, or a statement about a distribution chosen
on generators. No density assertion for all imprimitive polarizations
is appended: a corresponding reachable numerator would require its
own count.

The operation, initial principal class and equivalence relation are
fixed throughout. Module A's parity obstruction and the present
asymptotic supply no assertion about an unspecified broader
dynamical system and do not derive an operator $U$.

## B.7. Proof dependencies and validation boundary

The dependency chain is explicit:

1. The pinned geometric dictionary and Module A identify reachable
   primitive orbits with the stated integral F-ideals.
2. Unique prime-ideal factorization gives every local coefficient,
   multiplicativity and the full Euler product.
3. The fixed-modulus prime number theorem and (B11) verify every
   hypothesis of arXiv:2010.12929v8, Theorem 2.1.
4. Local factor comparison, ordered-product convergence and the
   explicit L-values identify its leading constant.
5. The independent hyperbola/content argument proves the denominator
   and justifies the error in the final ratio.

Historical auxiliary code and execution records are outside this admission.
The proof relies on the explicit integral construction and cited analytic
theorems, not an experimental evaluation of the asymptotic.
