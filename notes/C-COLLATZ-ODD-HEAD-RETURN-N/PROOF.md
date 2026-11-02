# Odd-head dynamics between exact Collatz blocks

**Status: NON-CANONICAL, L1 exact-arithmetic candidate-T.** The statements
below are analytical identities, elementary consequences, and explicit
counterexamples. No priority claim, universal convergence theorem, or
positive infinite escaping orbit is asserted. No numerical search or
verifier execution is used in these proofs.

## 1. One block definition and its exact head transition

Let

$$
T(n)=\frac{3n+1}{2^{v_2(3n+1)}}
$$

on positive odd integers. Every such integer has a unique representation

$$
n+1=2^k u,\qquad k\ge1,\quad u\text{ positive odd}.
$$

The pair $(u,k)$ is an exact encoding of $n$; $u$ alone is its odd head.
Define throughout this note

$$
B(n)=T^{k(n)}(n),\qquad k(n)=v_2(n+1).
$$

This block consists of the maximal initial run of valuation-one steps,
followed by the first step whose valuation is at least two. It does not
include every subsequent contracting step.

Indeed, for $0\le j\le k-1$,

$$
T^j(n)=3^j u2^{k-j}-1,
$$

because

$$
3(A2^r-1)+1=2(3A2^{r-1}-1)
$$

has valuation one for odd $A$ and $r\ge2$. The final state of this prefix
is $2\cdot3^{k-1}u-1$, and its next numerator is $2(3^k u-1)$. Thus, with

$$
t=v_2(3^k u-1)\ge1,\qquad K=k+t,
$$

the final step has valuation $t+1$, the total division exponent of the
block is $K$, and

$$
\boxed{
m=B(n)=\frac{3^k u-1}{2^t}
=\frac{3^k n+3^k-2^k}{2^{k+t}}.
}                                                               \tag{1}
$$

The case $k=1$ has no initial valuation-one step. In particular,
$B(1)=1$, with $u=k=t=1$.

Write the output in its own head coordinates,

$$
m+1=2^{k'}u',\qquad k'\ge1,\quad u'\text{ positive odd}.
$$

Then the exact transition is

$$
\boxed{2^{t+k'}u'=3^k u+2^t-1,}                                \tag{2}
$$

or explicitly

$$
\begin{aligned}
t&=v_2(3^k u-1),\\
k'&=v_2(3^k u+2^t-1)-t,\\
u'&=\frac{3^k u+2^t-1}{2^{t+k'}}.
\end{aligned}                                                  \tag{3}
$$

Because $3^k$ is a two-adic unit, $t=v_2(u-3^{-k})$: the pole read
by the head depends on $k$. For measure-theoretic interpretation, see
[MEASURE.md](MEASURE.md).

The output $m$ is odd and $3\nmid m$. Accordingly, an output pair must
satisfy $2^{k'}u'\not\equiv1\pmod3$. Reducing (2) modulo three also gives
the exact flag

$$
\boxed{3\mid u'\iff t\text{ is even}.}                          \tag{4}
$$

If $t$ is odd, more precisely $u'\equiv(-1)^{k'+1}\pmod3$.

### Local digit and carry accounting

Let $s$ be binary popcount and

$$
c_{\rm in}(x)=2s(x)-s(3x),\qquad
c_{\rm total}(x)=2s(x)+1-s(3x+1).
$$

The latter quantities count all outgoing carries in $x+2x$ and $x+2x+1$.
The increment identity gives
$c_{\rm total}(x)-c_{\rm in}(x)=v_2(3x+1)$.

Put $a=3^k u$. Since $a=2^t m+1$ and $m=2^{k'}u'-1$,

$$
s(a)=s(m)+1,\qquad s(m)=s(u')+k'-1,
$$

and therefore

$$
\boxed{s(u')+k'=s(3^k u).}                                    \tag{5}
$$

For the Thue–Morse bit $\tau(x)=s(x)\bmod2$, this gives the exact
corollary

$$
\boxed{
\tau(u')\equiv\tau(3^k u)+k'
\equiv c_{\rm in}(3^{k-1}u)+k'\pmod2,\qquad k\ge1.
}                                                               \tag{5a}
$$

The second congruence follows directly from
$c_{\rm in}(x)=2s(x)-s(3x)$.

For an exact binary description, set $H=(u'-1)/2$. Then

$$
3^k u
=H2^{t+k'+1}+(2^{k'}-1)2^t+1.
$$

The output normalization removes $k'$ ones from the popcount of the
multiplied head; the multiplication by $3^k$ still carries its own
arithmetic.

There is also a local carry balance. Write $w=v_2(3m+1)$. The
minus-one representation of $m$ gives

$$
c_{\rm in}(m)=c_{\rm in}(u')+k'+1-w.
$$

For completeness, this follows from
$s(3m+1)=s(3u')+k'-2$, hence
$c_{\rm total}(m)=c_{\rm in}(u')+k'+1$.
In the plus-one representation $a=2^t m+1$, the low blocks are
disjoint for $t\ge2$, giving $c_{\rm in}(a)=c_{\rm in}(m)$.
At $t=1$, the identity $3(2m+1)=2(3m+1)+1$ instead gives
$c_{\rm in}(a)=c_{\rm in}(m)+w$. Consequently

$$
\boxed{
c_{\rm in}(3^k u)
=c_{\rm in}(u')+k'+1-\mathbf 1_{\{t\ge2\}}\,v_2(3m+1).
}                                                               \tag{6}
$$

These are exact local balances, not monotonicity assertions.

### Segmentation boundary

For odd $n>1$, states $n\equiv3\pmod4$ expand in one $T$ step and
states $n\equiv1\pmod4$ contract. A maximal consecutive contracting
phase is finite, because its positive integer values strictly decrease.
Grouping maximal expanding and contracting phases would nevertheless
define a different induced map: for example, $B(7)=13$ still lies in
the contracting class, and $13\to5\to1$ follows. All statements below
use the single definition of $B$ above.

## 2. Exact inverse records and complete fixed-output fibers

Suppose the output head $u'$ and positive integers $(k,t,k')$ are given.
Set $m=2^{k'}u'-1$. Equation (2) recovers the input head uniquely:

$$
\boxed{
u=\frac{2^{t+k'}u'-2^t+1}{3^k}
 =\frac{2^t m+1}{3^k},\qquad n=2^k u-1.
}                                                               \tag{7}
$$

For positive odd $u'$ and $k,t,k'\ge1$, the necessary and sufficient
admissibility condition is

$$
\boxed{2^t(2^{k'}u'-1)\equiv-1\pmod{3^k}.}                     \tag{8}
$$

Necessity follows from (7). Conversely, divisibility in (8) makes $u$
a positive odd integer: the numerator and denominator are positive
odd integers. Then $n+1=2^k u$ has valuation exactly $k$, and
$3^k u-1=2^t m$ has valuation exactly $t$, because $m$ is odd.
Finally $m+1=2^{k'}u'$ has valuation exactly $k'$. Thus the recovered
input realizes precisely the recorded block. Exact divisibility by
$3^k$, rather than exact three-adic valuation $k$, is required; $u$
may itself be divisible by three.

**Fixed-output theorem.** Fix a positive odd $m$ and any $k\ge1$.
If $3\mid m$, there is no such block predecessor. If $3\nmid m$, there
is exactly one residue class of allowable $t$ modulo

$$
P_k=2\cdot3^{k-1}.
$$

All positive integers in that class are allowed, and all corresponding
predecessors are exactly

$$
\boxed{
u_t=\frac{2^t m+1}{3^k},\qquad n_t=2^k u_t-1.
}                                                               \tag{9}
$$

In particular, every output coprime to three has infinitely many
predecessors with each prescribed block length $k$.

**Proof of the order assertion.** For every positive integer $j$,

$$
v_3(4^j-1)=1+v_3(j).
$$

To see this, write $j=3^a b$ with $3\nmid b$. The geometric-sum
factor for the final exponent $b$ is congruent to $b$ modulo three.
For $X\equiv1\pmod3$, the factor $X^2+X+1$ has valuation exactly one:
if $X=1+3^h z$, $h\ge1$, $3\nmid z$, it equals
$3(1+3^h z+3^{2h-1}z^2)$. Thus each cubing increases the valuation
by exactly one, starting from $v_3(4-1)=1$.

An exponent giving $2^e\equiv1\pmod{3^k}$ must be even, because
$2\equiv-1\pmod3$. Writing $e=2j$, the preceding formula shows that
the least such exponent is $P_k$. There are exactly $P_k$ invertible
residues modulo $3^k$, so powers of two enumerate all of them once
per period. For $3\nmid m$, equation $2^t m\equiv-1\pmod{3^k}$
therefore determines exactly one residue class of $t$. Its positive
representatives give (9), whose sufficiency was already proved.

If $t_0$ is the least positive allowed exponent and $u_0=u_{t_0}$,
the inverse fiber can also be written

$$
u_{t_0+jP_k}
=2^{jP_k}u_0-\frac{2^{jP_k}-1}{3^k}\qquad(j\ge0).
$$

The quotient is integral. In the two-adic metric this family approaches
$3^{-k}$, with the exact depth

$$
v_2\!\left(u_{t_0+jP_k}-3^{-k}\right)=t_0+jP_k.
$$

The chosen input length $k$ therefore remains part of the inverse data.

## 3. The head alone is not a closed dynamical state

The same head can have different next heads:

$$
(u,k)=(1,2)\longmapsto(1,1),\qquad
(u,k)=(1,3)\longmapsto(7,1).
$$

These are $B(3)=1$ and $B(7)=13$. Thus there is no function of $u$
alone that reproduces every head transition.

The ambiguity is unbounded. For $u=1$ and every odd $k\ge1$,
$3^k\equiv3\pmod8$, so $t=k'=1$ and

$$
\boxed{u'=\frac{3^k+1}{4}.}                                   \tag{10}
$$

These heads are unbounded as odd $k$ increases. Each $k$ describes
a different input $n=2^k-1$.

In fact every fixed odd $u$ has unbounded possible next heads.
Modulo sixteen, the powers of three form
$G=\{1,3,9,11\}$. If $u\bmod16$ belongs to $G$, choose $k$ in
a residue class modulo four such that $3^k u\equiv3\pmod{16}$.
Otherwise $u\bmod16$ belongs to $5G=\{5,7,13,15\}$; choose $k$
such that $3^k u\equiv5\pmod{16}$. In the first case

$$
(t,k')=(1,1),\qquad u'=(3^k u+1)/4;
$$

in the second,

$$
(t,k')=(2,1),\qquad u'=(3^k u+3)/8.
$$

Increasing $k$ by four preserves the stated residue and makes $u'$
unbounded.

**Height obstruction.** A real-valued height $\mathcal H$ on odd heads
is called proper here when $\{u:\mathcal H(u)\le M\}$ is finite for
every real $M$. Such a height cannot be nonincreasing along all
admissible head transitions. Otherwise the
infinitely many distinct heads in (10) would all belong to the finite
sublevel set at the value of the height on $1$.

Strict decrease on every nonfixed block is impossible even without
properness: $B(3)=1$ changes the integer state but keeps its head equal
to one. This does not rule out a height on the full pair $(u,k)$, or a
nonproper weakly monotone function; neither is established here.

## 4. Arbitrarily long actual windows with growing states and heads

The preceding obstruction varies $k$ at a fixed head. A separate exact
construction gives arbitrarily long growth along consecutive blocks
of one positive orbit.

Fix an integer $R\ge1$ and define, for $0\le i\le R$,

$$
E_i=3R+3-3i,\qquad
n_i=9^i2^{E_i}-5,\qquad
u_i=9^i2^{E_i-2}-1.
$$

Then $n_0=2^{3R+3}-5$, and

$$
n_i+1=4u_i.
$$

Since $E_i\ge3$, each $u_i$ is positive and odd, so every state
$n_i$ has $k_i=2$. For $i<R$,

$$
9u_i-1
=2\left(9^{i+1}2^{E_i-3}-5\right)
=2n_{i+1}.
$$

The last factor is odd, proving $t_i=1$ and

$$
\boxed{B(n_i)=n_{i+1}\quad(0\le i<R).}                          \tag{11}
$$

Each of these blocks has precisely the two Collatz valuations $(1,2)$,
with total division exponent three. On this branch,

$$
\boxed{
n_{i+1}=\frac{9n_i+5}{8},\qquad
n_{i+1}+5=\frac98(n_i+5),\qquad
u_{i+1}+1=\frac98(u_i+1).
}                                                               \tag{12}
$$

Both $n_i$ and $u_i$ therefore strictly increase through all $R$
blocks. For every fixed finite window length, some positive starting
state has no decrease of either quantity anywhere in that window.

The arithmetic transfer is also exact:

$$
\begin{array}{c|cc}
&v_2&v_3\\ \hline
n_i+5&3R+3-3i&2i\\
u_i+1&3R+1-3i&2i.
\end{array}                                                     \tag{13}
$$

Each growing block removes three factors of two and adds two factors
of three in these shifted quantities.

Extending the same accelerated formula to negative odd integers
gives $-5\mapsto-7\mapsto-5$, with valuations $(1,2)$.
Its two-step affine branch fixes $-5$ and satisfies the second
identity in (12). The positive construction realizes that finite
valuation word repeatedly; the exact two-adic distance from $-5$
is recorded by $v_2(n_i+5)$ in (13).

For each larger $R$ this construction chooses a different $n_0$.
It gives no positive orbit proved to grow forever.

## 5. The exact next boundary and its Mersenne output

The growth construction has a determined next transition, rather
than an unspecified exit. At its final displayed state,

$$
n_R=8\cdot9^R-5,\qquad u_R=2\cdot9^R-1,\qquad k_R=2.
$$

Put $s=R+1$. Then

$$
9u_R-1=2(9^s-5).
$$

Since $9^s-5\equiv4\pmod8$, the next block has exactly

$$
\boxed{t_R=3,\qquad
n_{R+1}=B(n_R)=\frac{9^s-5}{4}.}                              \tag{14}
$$

Its Collatz valuations are $(1,4)$. Moreover,

$$
n_{R+1}+1=\frac{9^s-1}{4}.
$$

The elementary valuation identity

$$
v_2(9^s-1)=3+v_2(s)
$$

follows by writing $s=2^d w$ with $w$ odd. The odd geometric-sum
factor has valuation zero; starting from $v_2(9-1)=3$, each
successive squaring adds the factor $9^{2^j}+1\equiv2\pmod8$,
of valuation one. Consequently

$$
\boxed{
k_{R+1}=1+v_2(R+1),\qquad
u_{R+1}=\frac{9^{R+1}-1}{2^{3+v_2(R+1)}}.
}                                                               \tag{15}
$$

In particular,

$$
\boxed{
u_{R+1}
=\operatorname{oddpart}\!\left(3^{2(R+1)}-1\right)
=B\!\left(2^{2(R+1)}-1\right).
}                                                               \tag{16}
$$

The new odd head is exactly the integer value of a complete first
Mersenne-block output.

This boundary block decreases both its immediate input and its head.
Writing $a=9^R>1$,

$$
\frac{9a-5}{4}<8a-5,\qquad
u_{R+1}\le\frac{9a-1}{8}<2a-1=u_R.
$$

These comparisons are with the last state of the growing window,
not necessarily with its beginning. For example, at $R=6$ the
initial head is $u_0=2^{19}-1=524287$, whereas the head after the
boundary block is

$$
u_7=\frac{9^7-1}{8}=597871>u_0.
$$

Thus even the explicit end of this finite growth episode does not
give a uniform head descent relative to its starting point.
The formulas describe the specified finite blocks and their next
boundary; subsequent global behavior is not inferred.

## 6. Composition retains a positive affine offset

Let $n_{i+1}=B(n_i)$ follow actual positive integer blocks, with labels
$(k_i,t_i)$. Set

$$
L_j=\sum_{i<j}k_i,\qquad
D_j=\sum_{i<j}(k_i+t_i),\qquad C_0=0,
$$

and define

$$
C_{j+1}=3^{k_j}C_j+(3^{k_j}-2^{k_j})2^{D_j}.
$$

Induction in (1) gives the exact composite map

$$
\boxed{2^{D_N}n_N=3^{L_N}n_0+C_N.}                            \tag{17}
$$

All $C_N$ with $N\ge1$ are positive. The slope alone therefore does
not give the full descent criterion:

$$
\boxed{n_N<n_0\iff(2^{D_N}-3^{L_N})n_0>C_N.}                  \tag{18}
$$

For a declared finite word of positive pairs $(k_i,t_i)$, compute the
same $L_N,D_N,C_N$ algebraically. Its exact input cylinder is one odd
residue class modulo $2^{D_N+1}$:

$$
n_0\equiv(3^{L_N})^{-1}(2^{D_N}-C_N)\pmod{2^{D_N+1}}.         \tag{19}
$$

Necessity follows from (17) and oddness of the endpoint. For
sufficiency, compose the inverse branches

$$
I_{k,t}(y)=\frac{2^k(2^t y+1)}{3^k}-1.
$$

Each maps an odd 2-adic endpoint to exactly its declared $(k,t)$
branch. Their composite maps all odd endpoints onto a single class
modulo $2^{D_N+1}$, which must be (19). For positive integer starts in
that class, the actual forward blocks remain positive integers and
realize the word. Thus every finite word has infinitely many positive
integer realizations; its finite realizability does not establish an
infinite positive realization of an infinite prescribed word.

For the head along the same orbit, $n_i+1=2^{k_i}u_i$ gives the exact
size relation

$$
\boxed{\frac{u_N}{u_0}
=2^{k_0-k_N}\frac{n_N+1}{n_0+1}.}                             \tag{20}
$$

The corresponding product of linear head coefficients is treated in
`MEASURE.md`. Neither product removes the additive offsets in (17).

**Remaining global question.** Proving that every positive odd
$n_0>1$ has some actual block prefix satisfying (18) would prove the
Collatz conjecture by strong induction on $n_0$. Conversely,
convergence to one supplies such a prefix: block times increase by
positive integers, and one is fixed. Thus this universal eventual
descent condition is equivalent to the original convergence problem.
No such universal bound or descent proof is supplied here.
