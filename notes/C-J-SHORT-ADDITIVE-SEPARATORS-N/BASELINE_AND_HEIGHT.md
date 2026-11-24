# A prescribed separating family and an exponent-span obstruction

**NON-CANONICAL. No authority. All results below are candidate-D, L1.**
Paper deductions for [claim #2086](https://github.com/mathorn1973/twist-j/issues/2086).
Public basis `6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`.

Work in $\mathcal O=\mathbb Z[j]$, $j=\zeta_5$, with
$\phi=-j^2-j^3>1$ in the chosen embedding and $\alpha=\phi^2$.
For a rational prime $p>5$, let $h(p)$ be the order of $\alpha$ in
the whole quotient $(\mathcal O/p\mathcal O)^\times$.
A test is a sum of signed units $\pm j^a\phi^b$. Its flag at $p$
is one if the sum belongs to $p\mathcal O$, and zero otherwise.
Arity counts summands with multiplicity. Absolute exponent height is
$\max_i|b_i|$. Exponent span is $\max_i b_i-\min_i b_i$.
The span is invariant under multiplication by one common unit.

## A signed Lucas expansion [candidate-D]

Write $F_0=0,F_1=1,L_0=2,L_1=1$, with the Fibonacci recurrence for
both sequences. For $s\ge2$, every integer $1\le m\le L_s$
has a prescribed expression as a sum of at most
$$
                 \left\lfloor\frac{2s+4}{3}\right\rfloor                 \tag{1}
$$
signed real units of absolute exponent height at most $s$.

**Construction.** For the magnitude of a nonzero remainder, choose the
nearest Lucas value, resolving ties toward the smaller value. Subtract
that value with the sign of the remainder. Repeat until the remainder
is zero. Replace each signed $L_k$ by the corresponding signed trace
$\phi^k+(-1)^k\phi^{-k}$, except that $L_1=1$ uses the single unit
$1$. The two copies of $1$ representing $L_0=2$ count separately.

**Proof.** In order of increasing value, the initial choices are
$L_1=1,L_0=2,L_2=3,L_3=4,L_4=7,L_5=11$. For leading index
$k\ge5$, the next remainder has magnitude at most
$$
 \tfrac12(L_{k+1}-L_k)=\tfrac12 L_{k-1}
                       =\tfrac12(L_{k-3}+L_{k-2}).
$$
Indeed the lower neighboring gap is $L_k-L_{k-1}=L_{k-2}$,
smaller than the upper gap. The last quantity is the midpoint of
two consecutive Lucas values. With the specified tie rule the next
chosen index is at most $k-3$. This also holds for $k=5$, when
the possible nonzero remainder magnitudes are $1,2,3$, all of
index at most two. For leading index $0,1,2$ the remainder is zero.
For leading index three it has magnitude at most one, and for leading
index four it has magnitude at most two. Thus the procedure terminates.

For a leading index bounded by $s=2,3,4,5$, these cases give at most
$2,3,4,4$ unit summands, respectively, which are the four values of
(1). For $s\ge6$, a leading index between five and $s$ uses two
units and leaves a leading index at most $s-3$, if a remainder survives.
The bound follows since adding two to (1) at $s-3$ gives (1) at
$s$. The smaller leading indices meet the bound by the base cases.
For $m\le L_s$ and $s\ge2$, the initial index is at most $s$.
All exponents therefore lie in $[-s,s]$.

## Prescribed tests for a known block [candidate-D]

Let $r$ be a positive integer, $s=\lceil r/2\rceil\ge2$, and
let the known positive integer $N$ divide either $F_r$ or $L_r$.
Fix a positive order $h$. Every pair of distinct primes $p,q>5$
dividing $N$ with $h(p)=h(q)=h$ receives different flag vectors
from this ordered menu. Put $X=\lfloor\sqrt N\rfloor$. In increasing
order, use the expansion above for every integer
$$
       2\le m\le X,\qquad m\equiv 1\ \text{or}\ -1\pmod h.              \tag{2}
$$
Include each integer only once. Each test uses at most (1) summands
with absolute exponent height at most $s$ and span at most $2s$.
For $X\ge1$ the number of tests is at most
$$
      \left\lfloor\frac{X-1}{h}\right\rfloor+
      \left\lfloor\frac{X+1}{h}\right\rfloor .                           \tag{3}
$$

**Proof.** We have $N\le L_r\le L_{2s}$, using $F_r\le L_r$ and
the increase of $L_t$ for $t\ge1$. Also
$L_{2s}=L_s^2-2(-1)^s<(L_s+1)^2$, so $X\le L_s$.
The first result gives the asserted representation sizes. The positive
integers $m-1$ and $m+1$ in their respective congruence classes
are multiples of $h$ bounded by $X-1$ and $X+1$. Counting these
multiples bounds the size of their union by (3).

For $p>5$, the real quadratic algebra modulo $p$ is split when
$\chi_5(p)=1$ and is a quadratic field when $\chi_5(p)=-1$.
Its norm-one group has order $p-\chi_5(p)$. In the split case its
elements are the pairs $(a,a^{-1})$, and in the field case the
norm map from the cyclic multiplicative group has kernel of order
$p+1$. Since $\alpha$ has norm one, $h(p)\mid p-\chi_5(p)$.
Take $p<q$ in the stated pair. Then $p^2<pq\le N$, hence
$m=p$ occurs in (2). Each expression equals its scalar $m$ in
$\mathcal O$. Its flags at $p,q$ are consequently one and zero for
that entry. This works for every pair using the same menu. It requires
no squarefreeness of $N$.

**Cost.** The menu uses only $N,h$ for its list. Without a supplied
order one may use all $2\le m\le X$, with the same arity and height
bounds. For a listed $m$, its rational content is exactly $m$ and
the divisor read is $\gcd(N,m)$. The menu therefore implements trial
division restricted to the two congruence classes. Formula (1) is linear
in $r$ with leading coefficient $1/3$. Formula (3) is of order
$O(1+\sqrt N/h)$, which does not give a polynomial bound in the bit
length of $N$ for the number of tests. To write out the expressions,
one can precompute $O(s)$ Lucas integers of $O(s)$ bits and make
$O(s)$ comparisons and additions or subtractions per expansion by
scanning decreasing indices, with the initial small indices ordered by
value. A reader seeking only the gcd can use $m$ directly.
The separate note `C-J-UNIT-ARITY-BOUND-1` is a prior reference on the
upper-bound question. This proof uses the signed nearest-Lucas rule above.

## An arity and exponent-span obstruction [candidate-D]

Let a nonzero sum of $k\ge1$ signed units have exponent span $H$.
If a rational prime $p$ divides that sum in $\mathcal O$, then
$$
        2p\le k(\phi^{H/2}+\phi^{-H/2}).                               \tag{4}
$$
There is an integer-only, slightly weaker form. For the even integer
$E=2\lceil H/2\rceil$, it is
$$
                         4p^2\le k^2(L_E+2).                            \tag{5}
$$

**Proof.** Write the sum as $S=\sum_i\epsilon_i j^{a_i}\phi^{b_i}$
and let $c=(\min_i b_i+\max_i b_i)/2$. At two complex embeddings
the magnitude of $\phi$ is $\phi$, and at the other two it is
$\phi^{-1}$. All fifth roots of unity have magnitude one.
Put $A=\sum_i\phi^{b_i-c}$, $B=\sum_i\phi^{c-b_i}$. The triangle
inequality at the four embeddings bounds the absolute field norm by
$(AB)^2$, as the two scale factors cancel in the product. If
$S\in p\mathcal O$, the nonzero integer norm is a multiple of
$p^4$. Consequently
$$
   p\le\sqrt{AB}\le\tfrac12(A+B)
      \le\tfrac k2(\phi^{H/2}+\phi^{-H/2}).
$$
The last inequality follows term by term from $|b_i-c|\le H/2$.
Increasing $H$ to $E$ and squaring gives (5), since
$\phi^E+\phi^{-E}=L_E$ for even $E$.

In an order-$h$ class every prime $p>5$ is at least $h-1$.
Thus a menu of arity at most $k$ and span at most $H$ has identical
flags throughout the class if $k^2(L_E+2)<4(h-1)^2$, regardless
of the number of entries. Nonzero expressions in that box vanish at
none of these primes, and expressions zero in $\mathcal O$ vanish at
all of them. This condition is sufficient for indistinguishability.

## Falsifiers

* A positive integer $m\le L_s$ whose specified expansion exceeds (1)
  or uses an exponent outside $[-s,s]$ would refute the expansion bound.
* A pair satisfying the hypotheses of (2) with identical flags on its
  entire menu would refute the separation result. A menu exceeding (3)
  would refute the stated count.
* A nonzero integral unit sum divisible in the whole quotient by a prime
  violating (4) would refute the span bound. Divisibility at a single
  prime ideal above $p$ does not meet this hypothesis.
