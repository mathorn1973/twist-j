# Four explicit coordinates modulo one Aurifeuilian factor

**NON-CANONICAL. No authority. All deductions are candidate-D, L1.**
Paper proof for [claim #2090](https://github.com/mathorn1973/twist-j/issues/2090).

Let $j=\zeta_5$, $K=\mathbb Q(j)$, $\mathcal O=\mathbb Z[j]$, and
$\phi=-j^2-j^3=1+j+j^{-1}$. Choose the complex embedding with
$\phi=(1+\sqrt5)/2$. Its real quadratic conjugate is $\psi=-\phi^{-1}$.
Use the Fibonacci numbers $F_0=0,F_1=1$ and the Lucas numbers
$L_0=2,L_1=1$, both with the Fibonacci recurrence.

Let $m=5^k$, $k\ge1$, $f=F_m$ and $\sigma\in\{-1,1\}$. Write
\[
 A=A_\sigma=5f^2+5\sigma f+1,\qquad C=\mathbb Z/A\mathbb Z.
\]
In particular $A>1$ is odd and coprime to five. The following construction
uses $m$ and $\sigma$ and requires no prime factor of $A$.

## A scalar square root of five and a distinguished fifth root

In $C$ put
\[
 \rho=3+5\sigma f,\qquad
 \lambda=1+\sigma(2f-F_{m-1}).
\]
Then
\[
 \rho^2-\rho-1=0,\qquad
 (2\rho-1)^2=5,\qquad
 \lambda=-\sigma\rho^m,\qquad
 1+\lambda+\lambda^{-1}=\rho,\qquad \Phi_5(\lambda)=0.
\]

**Proof.** For the displayed integer representative of $\rho$ we have
$\rho^2-\rho-1=5A$. Thus $\rho$ is a unit in $C$, with inverse
$\rho-1$. The Fibonacci recurrence gives
$\rho^m=f\rho+F_{m-1}$, since the identity holds at $m=1,2$ and
both sides obey the same recurrence. Reduction of
$-\sigma(f\rho+F_{m-1})$ gives the displayed $\lambda$.

The integral identity $\phi^m-\psi^m=(2\phi-1)F_m$, at odd $m$,
specializes to $\rho^m+\rho^{-m}=(2\rho-1)f$.
The integer $(\rho-1)+\sigma(2\rho-1)f$ equals $2A$, so
$\lambda+\lambda^{-1}=\rho-1$ in $C$. Put $t=\rho-1$.
Then $t^2+t-1=0$ and
$\lambda^{-2}\Phi_5(\lambda)=t^2+t-1$, proving the last equality.
In particular $\lambda^5=1$.

## The whole rational quotient

The following map is an isomorphism of $C$-algebras:
\[
 \mathcal O/A\mathcal O\longrightarrow C^4,\qquad
 P(j)\longmapsto \big(P(\lambda),P(\lambda^2),
                          P(\lambda^3),P(\lambda^4)\big).                 \tag{1}
\]
Here $P$ is any integer polynomial representing the input. The first
coordinate sends $\phi$ to $\rho$, $\sqrt5$ to $2\rho-1=5+10\sigma f$,
and $\phi^m$ to $-\sigma\lambda$.

**Proof.** At every prime $p\mid A$, the reduction of $\lambda$ has
order five. Its fifth power is one and the alternative $\lambda=1$
in $\mathbb F_p$ would imply $p\mid\Phi_5(1)=5$. Hence all
differences $\lambda^i-\lambda^j$ for distinct indices
$1\le i,j\le4$ are units in $C$. All four powers are roots of $\Phi_5$ in $C$, since
$(\lambda^i-1)\Phi_5(\lambda^i)=0$ and $\lambda^i-1$ is a unit.
Consequently the four ideals $(X-\lambda^i)$ of $C[X]$ are pairwise
comaximal. Their product divides $\Phi_5(X)$, by equality of product
and intersection, and both polynomials are monic of degree four.
The Chinese remainder theorem gives (1), also when $A$ has repeated
prime factors. The coordinate of $\phi$ now follows from
$\phi=1+j+j^{-1}$.

Write $\theta:\mathcal O\to C$ for the first evaluation in (1).
The four maps $\theta\circ\tau$, for $\tau\in\operatorname{Gal}(K/\mathbb Q)$,
are exactly the four coordinates. In particular $S\in A\mathcal O$
if and only if all four values $\theta(\tau S)$ vanish.
For each $g\mid A$ the same decomposition holds after reduction modulo $g$.
Thus $\gcd(A,\operatorname{cont} S)$ equals the gcd of $A$ and any
integer representatives of the four coordinates, with full prime-power
multiplicities. Here $\operatorname{cont} S$ is the nonnegative gcd of
the coefficients of $S$ in $1,j,j^2,j^3$, with content zero at $S=0$.

The distinguished evaluation also identifies the norm in the initial
factorization. Put $z=\phi^m$, $x=z+z^{-1}=\sqrt5 f$. Pairing the
complex conjugate factors in the norm gives
\[
 N_{K/\mathbb Q}(z+\sigma j)
   =(x+\sigma(\phi-1))(x+\sigma\phi)
   =5f^2+5\sigma f+1.
\]
Indeed the first relative norm is $z(x+\sigma(\phi-1))$, and
real quadratic conjugation sends $z$ to $-z^{-1}$ and $x$ to $-x$.
As $\theta(z+\sigma j)=0$ and $\theta$ is surjective by constants,
the ideals $(z+\sigma j)$ and $\ker\theta$ have equal index $A$
in $\mathcal O$. The inclusion is therefore equality.

## A lower bound for the prime divisors

Every $p\mid A$ satisfies $p\equiv1\pmod{10m}$ and $p\ge10m+1$.
To see this directly, reduce (1) modulo $p$. The two real coordinates
of $\phi$ are $\rho$ and $1-\rho=-\rho^{-1}$, both in $\mathbb F_p$.
Now $\rho^{2m}=\lambda^2$ has exact order five. The conjugate
coordinate of $\phi^{2m}$ is its inverse. Therefore the order
of $\phi^2$ in the whole quotient modulo $p$ divides $5m$ but
does not divide $m$. Since $5m$ is a power of five it equals $5m$.
The order of $\phi$ is even, since its quadratic norm is $-1$ at the
odd prime $p$. Its square has order $5m$, so its order is $10m$.
Both coordinates of $\phi$ lie in $\mathbb F_p^\times$, giving
$10m\mid p-1$.

**Falsifiers.** A failure of either formula for $\rho$ or $\lambda$ in
$C$, or a nonzero element of $\mathcal O/A\mathcal O$ with all four
coordinates zero in (1), would refute the asserted coordinate description.
