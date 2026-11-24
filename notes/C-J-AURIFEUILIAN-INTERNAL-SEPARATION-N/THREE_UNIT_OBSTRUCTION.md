# Three signed units give the same flag throughout a fixed return order

**NON-CANONICAL. No authority. All deductions are candidate-D, L1.**
This paper argument specializes the unit-relation classification discussed in
[claim #2084](https://github.com/mathorn1973/twist-j/issues/2084) to the
power-of-five orders of [claim #2090](https://github.com/mathorn1973/twist-j/issues/2090).
The role of this specialization is to give the lower bound at every such
order, independently of the finite audit at index 25.

Fix $m=5^k$ with $k\ge1$ and put $h=5m$. For either sign define
$A_\sigma(m)=5F_m^2+5\sigma F_m+1$. Take any two distinct rational
primes dividing $A_-(m)A_+(m)$. Every sum of at most three signed units
$\pm j^a\phi^b$ vanishes in both whole prime quotients or vanishes in
neither. This applies to primes on the same side and to primes on
opposite sides at this fixed index.

## Six normalized real-unit pairs

Write $B_p=\mathbf F_p[\phi]$ for the quadratic algebra at one such
prime. Here $\phi^2=\phi+1$ and the conjugate of $\phi$ is $-\phi^{-1}$.
The coordinate proof gives $p>5$, $B_p\cong\mathbf F_p\times\mathbf F_p$,
and $\operatorname{ord}(\phi)=2h$. The quadratic norm is the product
of the two components. [Split coordinates](SPLIT_COORDINATES.md).

The real unit labels are $\epsilon\phi^b$, $\epsilon\in\{-1,1\}$,
with $b$ taken modulo $2h$. All $4h$ labels are distinct. The unique
involution of $\langle\phi\rangle$ is $\phi^h$ and has quadratic norm
$(-1)^h=-1$. The scalar $-1$ has norm $+1$, so the independent sign
produces a disjoint coset. Thus two labels represent the same unit
exactly when their signs and exponents modulo $2h$ agree, at every
prime under consideration.

Divide a three-unit equation by the negative of its last summand and
write it as $x+y=1$. For real units set $s=N(x)$ and $t=N(y)$, each
in $\{-1,1\}$. Conjugation gives $s/x+t/y=1$. Multiplying by $xy$ and
substituting $y=1-x$ yields
\[
                    x^2+(t-s-1)x+s=0.
\]
The six ordered solutions are as follows.

| $s$ | $t$ | Ordered unit images $(x,y)$ |
| ---: | ---: | --- |
| $+1$ | $-1$ | $(\phi^2,-\phi)$, $(\phi^{-2},\phi^{-1})$ |
| $-1$ | $+1$ | $(-\phi,\phi^2)$, $(\phi^{-1},\phi^{-2})$ |
| $-1$ | $-1$ | $(\phi,-\phi^{-1})$, $(-\phi^{-1},\phi)$ |
| $+1$ | $+1$ | None |

The first three rows give respectively $X^2-3X+1$, $X^2+X-1$ and
$X^2-X-1$. In each row the listed pairs already sum to one over
$\mathbf Z[\phi]$ and have the displayed norms. Their first components
for $x$ are the two different roots of the quadratic in $\mathbf F_p$,
since the discriminant is five. If the first component is $v$, the
norm requirement fixes the second as $s/v$. Hence the split algebra
contributes no further choice. In the last row $x^2-x+1=0$ would give
$x^3=-1$. Order two would then force $x=-1$, contradicting
$(-1)^2-(-1)+1=3\ne0$. Thus $x$ would have order six. Every signed
real unit has order dividing $2h$, which is coprime to three.

The table counts images for a normalized **real** equation, with order
of the summands retained. The common label description makes equality
to each listed pair independent of the prime. A two-unit equation
reduces to equality of labels, and a single unit is invertible.

## Whole-ideal test with fifth-root phases

Let $B=\mathbf Z[\phi]$, $u=\phi^{-1}$ and $\mathcal O=\mathbf Z[j]$,
$j=\zeta_5$. We have $\mathcal O=B\oplus jB$ since $j^2=uj-1$ and $j$
has degree two over $\mathbf Q(\phi)$. In the ordered basis $1,j$ the
five powers have the following coefficient pairs.

| Phase | Coefficients in $B\oplus jB$ |
| --- | --- |
| $1$ | $(1,0)$ |
| $j$ | $(0,1)$ |
| $j^2$ | $(-1,u)$ |
| $j^3$ | $(-u,-u)$ |
| $j^4$ | $(u,-1)$ |

Each coefficient of $\pm j^a\phi^b$ is therefore zero or one signed
real unit. For any sum of at most three such terms each coordinate
has at most three real summands. Whole-ideal divisibility by $p$
is equivalent to simultaneous divisibility of both coordinates in
$B$. Each coordinate has the same flag at both primes by the preceding
classification, including an empty coordinate sum. The original
phased sum consequently has the same flag as well.

This gives a lower bound of four units for separating any pair at the
fixed order $h$. Attainment needs a separate witness for that pair.
At different indices $m_1<m_2$ the two-term sum
$\phi^{10m_1}-1$ already separates the two orders.

## The whole product, including repeated prime factors

Put $M=A_-(m)A_+(m)$ and $w=\phi^{2m}$. The identity
$M=w^{-2}\Phi_5(w)$ yields $\phi^{2h}=w^5=1$ modulo $M\mathcal O$,
including all prime powers dividing $M$. Suppose a real relation with
at most three units holds at some $p\mid M$. Write a two-unit equation
as an equality of two signed labels. Their signs and exponents modulo $2h$
agree. In the three-unit case the
two normalized labels agree, in that same sense, with one of the six
ordered pairs in the table. Each indicated equality of labels therefore also
holds modulo $M$, and the displayed pairs sum to one integrally. Undoing
the normalization gives divisibility by $M$. Apply the same argument
to both real coordinates of any phased sum $S$ of at most three units.
It follows that
\[
            \gcd(M,\operatorname{cont}S)\in\{1,M\}.
\]
Here the content is the gcd of the four integral coordinates, with
content zero for the zero sum. This conclusion preserves the full
multiplicities even if one of the two sides has a repeated prime factor.
