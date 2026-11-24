# Exact Collatz blocks, carries, inverse fibers, and the cycle offset

**Status: NON-CANONICAL, L1 exact-arithmetic candidate-T.** This note gives
self-contained proofs of standard identities and elementary consequences.
It makes no priority claim, proves no universal convergence statement, and
asserts no canonical promotion. Any finite replay is an audit of the stated
scope, not a substitute for the proofs.

## 1. Definitions and carry accounting

For a positive odd integer $n$, write

$$
v(n)=v_2(3n+1),\qquad
T(n)=\frac{3n+1}{2^{v(n)}}.
$$

Let $s(n)$ be binary popcount, with $s(0)=0$, and define for $n\ge0$

$$
c_{\rm in}(n)=2s(n)-s(3n),\qquad
c_{\rm total}(n)=2s(n)+1-s(3n+1).
$$

These count all outgoing carries in the column additions $n+2n$ and
$n+2n+1$, including propagated carries. At column $i$, with incoming
carry $q_i$, the outgoing carry is

$$
q_{i+1}=\left\lfloor\frac{n_i+n_{i-1}+q_i}{2}\right\rfloor,
\qquad n_{-1}=0.
$$

The initial carry is respectively $q_0=0$ or $1$. Summing the column
equations without binary place weights gives the displayed digit-sum
defects. Equivalently, the classical factorial identity
$v_2(N!)=N-s(N)$, obtained by summing $\lfloor N/2^j\rfloor$ over $j\ge1$, gives
the following instances of Kummer's carry theorem:

$$
c_{\rm in}(n)=v_2\binom{3n}{n},\qquad
c_{\rm total}(n)=v_2\binom{3n+1}{n}.
$$

See [Granville's account of Kummer's theorem](https://dms.umontreal.ca/~andrew/Binomial/intro.html).
Since $s(M+1)=s(M)+1-v_2(M+1)$,

$$
\boxed{c_{\rm total}(n)=c_{\rm in}(n)+v_2(3n+1).}                 \tag{1}
$$

Define the golden set

$$
\mathcal Z=\{n\ge0:n\mathbin{\&}(n\gg1)=0\}.
$$

It consists exactly of binary words without adjacent ones. Such a word
cannot generate the first carry in $n+2n$; an adjacent pair does generate
one. Thus $n\in\mathcal Z\iff c_{\rm in}(n)=0$. Initial overlaps and
total carries are different statistics: $3+6=9$ has one initial overlap
and two outgoing carries.

For odd $n>1$, $T(n)>n$ exactly when $n\equiv3\pmod4$, and
$T(n)<n$ exactly when $n\equiv1\pmod4$. These cases have valuation
one and at least two, respectively. Golden odd inputs therefore contract,
apart from the fixed point $1$; the converse fails at $13\mapsto5$.

## 2. Affine centers and complete initial blocks

For a fixed integer $v\ge1$, the affine branch
$f_v(x)=(3x+1)/2^v$ on the rationals has the unique center

$$
a_v=\frac1{2^v-3},\qquad
f_v(x)-a_v=\frac3{2^v}(x-a_v).
$$

This center is integral exactly when $2^v-3=\pm1$: the two cases are
$a_1=-1$ and $a_2=1$. Only the latter is in the positive odd domain.
In particular,

$$
f_1(x)+1=\frac32(x+1),\qquad
f_2(x)-1=\frac34(x-1).
$$

The valuation determines when these branches apply. The signs in the
following two input representations refer to this same map $T$.

**Minus-one form.** Every positive odd $n$ has a unique representation

$$
n+1=2^k u,\qquad k\ge1,\quad u\text{ positive odd}.
$$

There are exactly $k-1$ initial valuation-one steps, with states

$$
\boxed{T^m(n)=3^m u2^{k-m}-1\quad(0\le m\le k-1).}              \tag{2}
$$

Indeed,

$$
3(A2^r-1)+1=2(3A2^{r-1}-1).
$$

For odd $A$ and $r\ge2$, the parenthesis is odd. At $r=1$ it
is even, proving maximality of the prefix. Consequently, with
$t=v_2(3^k u-1)$,

$$
\boxed{v_{\rm boundary}=1+t,\qquad
T^k(n)=\operatorname{oddpart}(3^k u-1).}                         \tag{3}
$$

Here $\operatorname{oddpart}(x)=x/2^{v_2(x)}$ for positive $x$.
The case $k=1$ has an empty valuation-one prefix.

**Plus-one form.** Every odd $n>1$ has a unique representation

$$
n-1=2^r u,\qquad r\ge1,\quad u\text{ positive odd}.
$$

There are exactly $b=\lfloor(r-1)/2\rfloor$ initial valuation-two steps:

$$
\boxed{T^m(n)=3^m u2^{r-2m}+1\quad(0\le m\le b).}              \tag{4}
$$

For odd $A$ and $h\ge3$,

$$
3(A2^h+1)+1=4(3A2^{h-2}+1)
$$

has valuation exactly two. The two boundary cases are

$$
\begin{array}{c|c|c}
r&v_{\rm boundary}&\text{state after the boundary step}\\ \hline
2q&2+v_2(3^q u+1)\ge3&T^q(n)=\operatorname{oddpart}(3^q u+1)\\
2q+1&1&T^{q+1}(n)=3^{q+1}u+2.
\end{array}                                                     \tag{5}
$$

These follow by evaluating $3(4\cdot3^{q-1}u+1)+1$ and
$3(2\cdot3^q u+1)+1$. Their valuations differ from two, proving that
the prefix length is exact. The excluded $n=1$ is fixed with valuation
two forever; $v_2(n-1)$ is not defined there.

## 3. Carry formulas at both boundaries

For odd $A\ge1$, put $H=(A-1)/2$. The disjoint-block identity

$$
A2^r-1=H2^{r+1}+(2^r-1)
$$

implies, for $r\ge1$,

$$
\begin{aligned}
s(A2^r-1)&=s(A)+r-1,\\
c_{\rm total}(A2^r-1)&=c_{\rm in}(A)+r+1,\\
c_{\rm in}(A2^r-1)&=
\begin{cases}
c_{\rm in}(A)+r,&r\ge2,\\
c_{\rm in}(A)+1-v_2(3A-1)=c_{\rm in}(H),&r=1.
\end{cases}
\end{aligned}                                                    \tag{6}
$$

For the middle identity, $s(3(A2^r-1)+1)=s(3A)+r-2$, also at
$r=1$. Subtracting the valuation using (1) proves the last identity.
Alternatively, at $r=1$, $n=4H+1$ and $3n=4(3H)+3$, which gives
$c_{\rm in}(n)=c_{\rm in}(H)$ directly.

The separating zero is not a carry barrier. For $r\ge2$, at column
$r$, the digits of $n$ and $2n$, together with the incoming carry,
are $0+1+1=2$. The low block contributes $r$ carries, including this
column, and sends an incoming carry into the upper addition $H+2H$.
Its contribution is $c_{\rm total}(H)=c_{\rm in}(A)$. For example,
$11=(1011)_2$, $11+22=33$, has four carries; the carry passes through
the zero at column two. The proposed value $c_{\rm in}(A)+r-1$ is
therefore too small by one whenever $r\ge2$.

For the other input form, disjoint low blocks give

$$
\begin{aligned}
s(A2^h+1)&=s(A)+1\quad(h\ge1),\\
c_{\rm in}(A2^h+1)&=c_{\rm in}(A)\quad(h\ge2),\\
c_{\rm in}(2A+1)&=c_{\rm in}(A)+v_2(3A+1).
\end{aligned}                                                    \tag{7}
$$

The last line follows from $3(2A+1)=2(3A+1)+1$ and the increment
identity used in (1). Equation (1) supplies all corresponding total-carry
counts. Golden membership agrees with that of $A$ for $h\ge2$;
at $h=1$, $2A+1$ ends in $11$ and is not golden.

## 4. Mersenne boundaries and an exact golden counterexample

Set $n_0=2^k-1$, $k\ge2$. Equation (6) gives

$$
c_{\rm in}(n_0)=k,\qquad c_{\rm total}(n_0)=k+1.
$$

The last prefix state is $n_{k-1}=2\cdot3^{k-1}-1$. Put
$t=v_2(3^k-1)$. Then

$$
t=\begin{cases}1,&k\text{ odd},\\2+v_2(k),&k\text{ even},\end{cases}
\qquad
v_{\rm boundary}=1+t,\qquad
n_k=\frac{3^k-1}{2^t}.                                         \tag{8}
$$

For odd $k$, $3^k-1\equiv2\pmod4$. For even $k=2^d w$, $w$
odd, the odd geometric-sum factor does not change the valuation.
Starting with $3^2-1=8$, each further doubling adds a factor of
valuation one, since $3^{\text{even}}+1\equiv2\pmod8$. This proves
(8). In particular, the boundary valuation for $k=6$ is four, not three.

All earlier states end in $11$. At the last state,

$$
h=\frac{3^{k-1}-1}{2},\quad n_{k-1}=4h+1,\qquad
\boxed{n_{k-1}\in\mathcal Z\iff h\in\mathcal Z.}                \tag{9}
$$

Appending $01$ introduces no adjacent ones. The exact witness

$$
k=8:\quad h=1093=(10001000101)_2,\quad
n_7=4373=(1000100010101)_2
$$

therefore refutes any exhaustive transformed list omitting $k=8$.
This is the first golden state in that prefix, and

$$
3\cdot4373+1=2^6\cdot205.
$$

Meanwhile $3^7=2187=(100010001011)_2$ is not golden: deleting its
last digit removes its terminal adjacent pair. A classification of golden
powers of three cannot be transferred through that deletion without proof.

**O, unproved here:** the assertion that $1,9,81$ are all golden powers
of three. A historical conjectural formulation appears in
[this original question revision](https://mathoverflow.net/revisions/262193/1).
No global classification of the transformed numbers in (9) is asserted.

## 5. Which complete first Mersenne blocks decrease?

Let $R_k=T^k(2^k-1)$, including $k=1$. Then

$$
\boxed{
R_k<2^k-1\iff k\in\{2,4,8\};\quad
R_k=2^k-1\iff k=1.
}                                                               \tag{10}
$$

All remaining cases strictly increase. Here is a proof covering every
exponent, rather than an extrapolation of examples. Equation (8) gives
$2^t\le4k$. Define

$$
F(k)=3^k-1-4k(2^k-1).
$$

Now $F(9)=19682-18396=1286>0$, and

$$
F(k+1)-3F(k)=(4k-8)2^k-8k+6>0\quad(k\ge4),
$$

using $4k-8\ge2k$ and $2^k\ge4$. Thus $F(k)>0$ for every
$k\ge9$, and

$$
R_k\ge\frac{3^k-1}{4k}>2^k-1.
$$

The remaining exact values complete the proof:

| $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| $2^k-1$ | 1 | 3 | 7 | 15 | 31 | 63 | 127 | 255 |
| $R_k$ | 1 | 1 | 13 | 5 | 121 | 91 | 1093 | 205 |

The boundary step itself always decreases its input for $k\ge2$,
since its valuation is at least two. Equation (10) instead compares the
end and beginning of the entire block. It says nothing about the later
fate of that orbit.

## 6. Common descendants and complete output fibers

For every positive odd $p$,

$$
3(4p+1)+1=4(3p+1),\qquad \boxed{T(4p+1)=T(p).}                \tag{11}
$$

Combining (11) with the even case of (4) proves

$$
\boxed{T^q(2^{2q}u+1)=T(3^{q-1}u)\quad(q\ge1,\ u\text{ odd}>0).} \tag{12}
$$

Indeed, the preceding state is $4\cdot3^{q-1}u+1$. This is a
meeting at a common child, not necessarily a visit to $3^{q-1}u$
itself. For example, $T^4(257)=T(27)=41$.

More generally, put

$$
P_j(p)=4^jp+\frac{4^j-1}{3}\quad(j\ge0).
$$

Then $3P_j(p)+1=4^j(3p+1)$, so

$$
T(P_j(p))=T(p),\qquad v(P_j(p))=v(p)+2j.                       \tag{13}
$$

These are inputs sharing one child, not successive forward iterates.
The identity $P_j(p)+1/3=4^j(p+1/3)$ also gives their exact
2-adic approach to the pole $-1/3$.

For $m=T(n)$, the pair $(m,v(n))$ recovers the input:

$$
\boxed{n=(2^v m-1)/3.}                                        \tag{14}
$$

The admissible pairs are precisely positive odd $m$ with $3\nmid m$,
$v\ge1$, and $2^v m\equiv1\pmod3$. These conditions make (14)
a positive odd integer with valuation exactly $v$. For a fixed output,
let $v_0=2$ if $m\equiv1\pmod3$, and $v_0=1$ if
$m\equiv2\pmod3$. Its entire fiber is

$$
\left\{\frac{2^{v_0+2j}m-1}{3}:j\ge0\right\}
=\{P_j((2^{v_0}m-1)/3):j\ge0\}.                               \tag{15}
$$

Thus the omitted depth records exactly which preimage was chosen.

## 7. Prime supports and the entrance to one

The exact equation $2^vT(n)-3n=1$ implies

$$
\gcd(n,T(n))=1,\qquad\gcd(6,T(n))=1.
$$

Consecutive prime supports are disjoint. This is not disjointness from
the entire past: $55\to83\to125$ contains the prime five twice.
Orthogonality of prime-exponent vectors follows if their basis is assigned
the usual orthonormal inner product; no physical metric is inferred.

All positive odd one-step predecessors of one are exactly

$$
A_j=\frac{4^j-1}{3},\quad j\ge1.                               \tag{16}
$$

Indeed, $3n+1=2^v$ requires even $v=2j$. For every odd integer
$d\ge1$, some $A_j$ is divisible by $d$: choose
$j=\operatorname{ord}_{3d}(4)$, which exists because
$\gcd(4,3d)=1$. Then $3d\mid4^j-1$. This includes all prime
powers in $d$ simultaneously. It proves existence of a multiple of
$d$ mapping directly to one, not that the orbit starting at $d$
visits such a multiple.

## 8. The exact cycle equation includes an offset

For an actual branch word $v_1,\ldots,v_L\ge1$, set

$$
V_0=0,\quad V_i=\sum_{j=1}^i v_j,\quad K=V_L,\qquad
C=\sum_{i=1}^L3^{L-i}2^{V_{i-1}}.
$$

Induction in the branch equations $2^{v_i}n_i=3n_{i-1}+1$ gives

$$
\boxed{2^K n_L=3^L n_0+C.}                                    \tag{17}
$$

Consequently every positive cycle satisfies

$$
\boxed{D=2^K-3^L>0,\qquad Dn_0=C.}                            \tag{18}
$$

Any proposed cycle must retain integral positive odd states and its
declared valuations. In particular, every prime power dividing $D$
must divide $C$. The linear coefficient alone is insufficient: the
fixed branch $(3x+1)/8$ reduces modulo five to $x+2$, not to the
identity; here $D=5,C=1$, so an integral fixed point is impossible.

Multiplying the ratios around a cycle also gives

$$
0<K\log2-L\log3
=\sum_{i=0}^{L-1}\log\left(1+\frac1{3n_i}\right)
<\frac{L}{3\min_i n_i}.                                       \tag{19}
$$

This controls relative proximity of $2^K$ and $3^L$, not the size
of the largest prime factor of their difference. Standard cycle
conditions, logarithmic estimates, and continued-fraction methods are
discussed by [Simons and de Weger, *Acta Arithmetica* 117 (2005), 51–70](https://www.impan.pl/shop/publication/transaction/download/product/82263?download.pdf=).
Their step-count notation differs from the accelerated convention here.
No universal convergence conclusion or new cycle-length bound follows
from this note.
