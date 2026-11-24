# A six-unit split for the return orders $5^m$, $m\ge2$

**NON-CANONICAL. No authority. Written deductions: candidate-D, L1.**
The Lucas factorization below is classical. The deductions concern its
whole-ideal order, its realization by six signed units, and the resulting
obstruction to a fixed finite list of tests.

Write $\mathcal O=\mathbf Z[j]$, $j=\zeta_5$, $\phi=(1+\sqrt5)/2$,
$\psi=-\phi^{-1}$, and $\alpha=\phi^2$. Write
$F_m=(\phi^m-\psi^m)/\sqrt5$ and $L_m=\phi^m+\psi^m$.
For $Y\in\mathcal O$, its content is the nonnegative gcd of its
coordinates in an integral basis. Thus $d\mid\operatorname{cont}(Y)$
means $Y=0$ in the whole quotient $\mathcal O/d\mathcal O$.

## The two factors and their order

For a positive odd integer $r$, write $f=F_r$, $z=\phi^r$, $w=z^2$,
$t=w+w^{-1}$ and $A_\sigma=5f^2+1+\sigma 5f$ for $\sigma\in\{-1,1\}$.
The classical Lucas factorization gives
\[
 B=\frac{L_{5r}}{L_r}=A_-A_+.
\]
Here and below subscripts $-$ and $+$ denote the two signs. Brillhart,
Montgomery and Silverman give this identity as formula (2.9) of
*Tables of Fibonacci and Lucas factorizations*, Math. Comp. 50 (1988),
p. 253. [Original publication](https://doi.org/10.1090/S0025-5718-1988-0917832-6).

Indeed $z+z^{-1}=\sqrt5 f$ and $L_r=z-z^{-1}$, so $t=5f^2-2$. Hence
\[
 B=\frac{z^5-z^{-5}}{z-z^{-1}}
  =w^{-2}\Phi_5(w)=t^2+t-1=(5f^2+1)^2-25f^2 .
\]
The two factors are odd and congruent to one modulo five. Any common
prime divides their difference $10f$ and each factor is one modulo $f$.
Thus they are coprime. Also $3\nmid B$, since $t(t+1)$ is zero or two
modulo three.

**Order deduction (candidate-D, L1).** Take $r=5^k$ with $k\ge1$.
Both $A_-$ and $A_+$ exceed one. For every prime power $p^e\mid B$,
$e\ge1$, we have $p>5$ and $\Phi_5(w)=0$ in $\mathcal O/p^e\mathcal O$.
Consequently $\alpha^{5r}=w^5=1$. Already modulo $p$, $w\ne1$ since
$\Phi_5(1)=5$. Every proper divisor of $5r=5^{k+1}$ divides $r$.
It follows that the order of $\alpha$ is exactly $5r$ modulo $p$ and
modulo every $p^e\mid B$. Taking one prime from each factor gives two
different primes of this order for every $k\ge1$.

## Six units recover the complete factor

**Content deduction (candidate-D, L1).** For the same $r=5^k$ define
\[
 S_\sigma=(\phi^{3r}+\phi^{-3r})-(\phi^r+\phi^{-r})
             +\sigma(\phi+\phi^{-1}).
\]
The sign and all six exponents can be fixed from the index. The odd-index
identity $F_{3r}=5f^3-3f$ follows by expanding
$(z+z^{-1})^3-3(z+z^{-1})$. Since $\phi+\phi^{-1}=\sqrt5$, this gives
the exact identity in $\mathcal O$
\[
 S_\sigma=\sqrt5\,(F_{3r}-f+\sigma)
          =\sqrt5\,(f+\sigma)A_{-\sigma}.
\]
The element $\sqrt5=2\phi-1=-1-2j^2-2j^3$ has primitive integer
coordinates, so $\operatorname{cont}(S_\sigma)=|(f+\sigma)A_{-\sigma}|$.
The factor $\sqrt5$ is invertible modulo $B$ and
$A_\sigma=5f(f+\sigma)+1$ is coprime to $f+\sigma$. Reduction modulo
each $d\mid B$ therefore gives the whole-ideal content equality
\[
 \gcd(B,\operatorname{cont}(S_\sigma))=A_{-\sigma}.
\]
Every prime power of the selected factor survives in this gcd.

**Return deduction (candidate-D, L1).** For the inherited signed defect,
$R(n)=\operatorname{cont}(J^n-1-(J-1)^n)$. At $n=10r+1$, the character
is $+1$. Its factorization is
$J^n(1-\alpha^{5r})=-J^n\phi^{5r}L_{5r}$ because $5r$ is odd.
Multiplication by a unit preserves content, giving $R(10r+1)=L_{5r}$.
Likewise $R(2r+1)=L_r$ because $5\mid r$. Thus $B$ is the quotient of
these two actual returns. [Signed-defect source](https://github.com/mathorn1973/twist-j/pull/2081).

The same probe extracts its factor directly from the larger return.
Indeed $L_r^2=5f^2-4$ is one modulo five. If a prime dividing $L_r$
divided $f-1$ or $f+1$, this identity would give $0=1$ modulo that prime.
Also $A_\sigma\equiv5(1+\sigma f)\pmod{L_r}$. Thus $L_r$ is coprime to
$5(f+\sigma)A_{-\sigma}$, and
\[
 \gcd(R(10r+1),\operatorname{cont}(S_\sigma))=A_{-\sigma}.
\]
For $r=5$ the two factors are $101$ and $151$. In general each factor
can contain several primes. The argument distinguishes the two sides of
the displayed factorization. The minimum number of units for an individual
pair can be smaller than six.

## The quadratic Gauss sum in the same whole quotient

**Equivalent comparison (candidate-D, L1).** In $\mathcal O/B\mathcal O$
one has $\Phi_5(w)=0$, $w^5=1$ and $t^2+t=1$. The quadratic Gauss sum
\[
 T=w+w^{-1}-w^2-w^{-2}=2t+1
\]
therefore satisfies $T^2=5$. Put $\epsilon=z^5$. Then
$\epsilon^2=1$ and $z+z^{-1}=\epsilon(w^2+w^{-2})=-\epsilon(1+t)$.
Since $(1+t)(2t+1)=t+3$ in this quotient,
\[
 A_\sigma=t+3+\sigma\sqrt5(z+z^{-1})
          =(1+t)(T-\sigma\epsilon\sqrt5).
\]
The multiplier $1+t$ has inverse $t$. Comparing the two square roots of
five, $T$ and $\sigma\epsilon\sqrt5$, therefore selects $A_\sigma$ with
its full multiplicity modulo $B$. Written as $T-\sigma\epsilon
(\phi+\phi^{-1})$, the comparison also uses six signed real units.

## No finite list of concrete sums is universal

**Obstruction (candidate-D, L1).** Fix finitely many sums in
$\mathcal O$, including all of their signs, phases and exponents.
A zero sum vanishes in every quotient. Each nonzero sum vanishes modulo
only finitely many ideals $(p)$ generated by rational primes, since $p$ then
divides its nonzero integer norm. The union of these finite exceptional
sets is finite. Choose $k$ so that $5^{k+1}$ differs from the orders
of $\alpha$ at all exceptional primes greater than five. Every prime
from either side of the corresponding block $B$ now has the same vector
of zero tests, yet the block has at least two distinct prime divisors.
Any decision that uses only that vector also agrees at these primes.
The six-term prescription above varies its exponents with $r$. Whether
a bounded number of summands suffices for every pair at arbitrary equal
order remains open here.
