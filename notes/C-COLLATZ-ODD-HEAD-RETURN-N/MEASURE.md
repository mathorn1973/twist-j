# Odd-head coordinates, Haar branches, and coefficient drift

**Status: NON-CANONICAL analytical note.** The statements below have
self-contained proofs at their stated local or probabilistic scope. They
make no priority claim and do not prove convergence of positive integer
Collatz orbits. No numerical search is used in these proofs.

## 1. The block map and its exceptional points

Let U be the odd 2-adic integers, with normalized Haar probability nu.
On positive odd integers, let T be the accelerated Collatz map. Write

$$
n+1=2^k u,\qquad k\ge1,\quad u\in U.
$$

The complete initial block from `PROOF.md` is

$$
B(n)=T^k(n)=\frac{3^k u-1}{2^t},\qquad
t=v_2(3^k u-1)\ge1.
$$

Its next coordinates satisfy

$$
B(n)+1=2^{k'}u',\qquad
\boxed{2^{t+k'}u'=3^k u+2^t-1.}                 \tag{1}
$$

These formulas also define a partial map on U. Initially n=-1 is
excluded because k is infinite. For each finite k, the head u=3^(-k)
is excluded because 3^k u-1=0. In n coordinates these latter points are

$$
n=(2/3)^k-1,\qquad k\ge1.
$$

To take the next head, B(n)=-1 must also be excluded. For fixed k this
occurs precisely at

$$
u=\frac{1-2^t}{3^k},\qquad t\ge1.              \tag{2}
$$

For indefinite iteration remove the backward orbit of

$$
E_0=\{-1\}\cup\{(2/3)^k-1:k\ge1\}.
$$

Each point has at most countably many inverse branches, indexed by
(k,t), so this backward orbit is countable and Haar-null. It includes
the points in (2) after conversion to n coordinates. Positive integer
orbits encounter none of these exceptions: their blocks remain positive
odd integers. Excluding a null set is needed for the local probability
statements, not an additional hypothesis about positive integer orbits.

The pair (k,u), rather than u alone, is the state coordinate. For example,
u=1 with k=1 gives B=1 and u'=1, whereas u=1 with k=3 gives B=13 and
u'=7. Discarding k does not define an autonomous map on heads.

## 2. Exact product law for a fixed initial k

Fix k>=1. For any t,l>=1 and z in U define

$$
H_{k,t,l}(z)=\frac{2^{t+l}z-2^t+1}{3^k}.       \tag{3}
$$

This is an odd 2-adic integer. Direct substitution gives

$$
3^kH_{k,t,l}(z)-1=2^t(2^lz-1).
$$

The last factor is odd, so the first depth is exactly t, the block output
is 2^lz-1, and its next coordinates are exactly k'=l and u'=z.
Conversely, (1) gives (3) for every admissible input. Thus these branches
are disjoint and exhaust U apart from the fixed-k poles just listed.

The linear part of (3) has 2-adic absolute value 2^(-t-l). Translation
does not affect Haar measure. For every Borel set A in U,

$$
\boxed{
\nu\{u:t(u)=t,\ k'(u)=l,\ u'(u)\in A\}
   =2^{-t-l}\nu(A).
}                                                               \tag{4}
$$

The formula uses normalized measure on U on both sides: scaling a
subset of U and then multiplying its ordinary Haar measure by two
introduces no extra factor.

Since the one-dimensional series $\sum_{r\ge1}2^{-r}=1$, (4) proves that,
for a Haar-distributed head with fixed k:

- t and k' are independent, with P(t=r)=P(k'=r)=2^(-r);
- u' is again Haar-distributed on U and is independent of both depths;
- the joint law does not depend on the chosen initial k.

This is an exact local law, not an assumption of random integer orbits.

## 3. The invariant law and independent complete blocks

For Haar n in U, the decomposition n+1=2^k u itself has product law

$$
\nu\{n:k(n)=k,\ u(n)\in A\}=2^{-k}\nu(A).    \tag{5}
$$

Consequently the coordinate measure is rho times nu, where
rho(k)=2^(-k). Equations (4) and (5) show that it is preserved by
(k,u) -> (k',u'). At a single step, k,t,k' are three independent
copies of rho, and u' is independent of them.

There is also a direct full-block proof. Given k,t>=1 and output y in U,
the inverse is

$$
I_{k,t}(y)
=\frac{2^k(2^ty+1)}{3^k}-1
=\frac{2^{k+t}}{3^k}y+\frac{2^k-3^k}{3^k}.    \tag{6}
$$

Its input has exactly the prescribed k and t. Its measure scaling is
2^(-k-t), giving

$$
\boxed{
\nu\{n:k(n)=k,\ t(n)=t,\ B(n)\in A\}
   =2^{-k-t}\nu(A).
}                                                               \tag{7}
$$

Composing (6) proves that a finite ordered word
(k_0,t_0),...,(k_(N-1),t_(N-1)) has probability

$$
2^{-\sum_{i=0}^{N-1}(k_i+t_i)},
$$

and the endpoint B^N(n) is Haar and independent of that word. Thus the
complete block symbols (k_i,t_i) are independent and identically
distributed under the invariant Haar law. With fixed k_0 and Haar u_0,
the newly read pairs (t_i,k_(i+1)) are likewise independent copies of
rho times rho.

This does not say that full successive states are independent: the
dynamics is deterministic. Nor are the successive head slopes below
independent, because neighboring slopes share k_(i+1).

## 4. Poles, sensitivity, and an exact code

For fixed k, let alpha=3^(-k). Then

$$
t=v_2(u-\alpha).
$$

Within a fixed t branch define beta=(1-2^t)/3^k. Equation (1) yields

$$
t+k'=v_2(u-\beta),\qquad
u'=\frac{3^k(u-\beta)}{2^{t+k'}}.              \tag{8}
$$

The two readings are nested: v_2(alpha-beta)=t, while the input lies
strictly deeper around beta. For two heads u and v in the same branch
(k,t,k'),

$$
u'-v'=\frac{3^k}{2^{t+k'}}(u-v),\qquad
v_2(u'-v')=v_2(u-v)-(t+k').                    \tag{9}
$$

Thus the forward branch expands 2-adic distances by 2^(t+k'); its
inverse contracts by the reciprocal. The complete branch is one odd
residue class modulo 2^(t+k'+1). Specifying u' modulo 2^l, l>=1,
specifies u modulo 2^(t+k'+l). This is an exact finite information
budget, including the final odd bit.

For a full-block word put

$$
d_i=\frac{2^{k_i+t_i}}{3^{k_i}},\qquad
c_i=\frac{2^{k_i}-3^{k_i}}{3^{k_i}}.
$$

Iterating (6) gives

$$
n_0=\sum_{j=0}^{N-1}c_j\prod_{i<j}d_i
        +\left(\prod_{i<N}d_i\right)n_N.       \tag{10}
$$

Since v_2(d_i)=k_i+t_i>=2 and n_N is odd, the last term tends to zero
2-adically. Therefore every infinite word of positive pairs determines
exactly one nonexceptional odd 2-adic input by the convergent series

$$
\boxed{n_0=\sum_{j=0}^{\infty}c_j\prod_{i<j}d_i.}             \tag{11}
$$

For existence with all the prescribed branches, define every tail

$$
x_r=\sum_{j\ge r}c_j\prod_{r\le i<j}d_i.
$$

Each tail is odd: its first term $c_r$ is odd and all later terms are
divisible by four. Moreover $x_r=I_{k_r,t_r}(x_{r+1})$, so (6) gives
exactly the finite depths k_r,t_r at every stage. Thus no tail equals
a pole or has an infinite next depth. Uniqueness follows from the
vanishing remainder in (10). This proves the one-sided Bernoulli
coding directly.

For a finite word, with $Q=\sum_i(k_i+t_i)$, (10) maps all odd
endpoints onto one odd residue class modulo 2^(Q+1). This is the full
cylinder on which the specified N blocks are defined; a later block
may still encounter an exceptional point. Restricting to the global
nonexceptional domain removes its countable exceptional subset and
does not change its measure. In particular, every finite word is
realized by infinitely many positive integer starts. This finite
realization does not imply that the single 2-adic input of an infinite
prescribed word is a positive integer.

## 5. The same logarithmic drift, different first moments

The exact full-block formula in n coordinates is

$$
B(n)=A n+b,\qquad
A=\frac{3^k}{2^{k+t}},\qquad
b=\frac{3^k-2^k}{2^{k+t}}.
$$

In head coordinates, (1) is

$$
u'=a u+e,\qquad
a=\frac{3^k}{2^{t+k'}},\qquad
e=\frac{2^t-1}{2^{t+k'}}.
$$

Here A,a,b,e are ordinary positive rational coefficients. Their real
absolute values and logarithms are defined even when the state itself
is a general 2-adic integer. We do not assign an Archimedean absolute
value to such a state.

For rho(r)=2^(-r), elementary convergent series give

$$
\mathbb E r=\sum_{r\ge1}\frac r{2^r}=2,
\qquad
\mathbb E2^{-r}=\sum_{r\ge1}4^{-r}=\frac13.
$$

For fixed k, the product laws above therefore give

$$
\begin{array}{c|c|c}
&\mathbb E[\text{coefficient}\mid k]
&\mathbb E[\log(\text{coefficient})\mid k]\\ \hline
A&(3/2)^k/3&k\log3-(k+2)\log2\\
a&3^{k-2}&k\log3-4\log2.
\end{array}                                                     \tag{12}
$$

Under the invariant law, k also has distribution rho. The first
moments are then different:

$$
\mathbb E A
=\left(\sum_{k\ge1}(3/4)^k\right)
 \left(\sum_{t\ge1}4^{-t}\right)
=3\cdot\frac13=1,
$$

$$
\boxed{\mathbb E a
=\frac19\sum_{k\ge1}(3/2)^k=+\infty.}                        \tag{13}
$$

The second equality is a divergent series of nonnegative terms; it is
not an interchange involving cancellation. In contrast, both logarithms
are absolutely integrable because k,t,k' have finite mean, and

$$
\boxed{\mathbb E\log A=\mathbb E\log a
=2\log3-4\log2=2\log(3/4)<0.}                               \tag{14}
$$

Thus an arithmetic mean coefficient of one is not invariant under this
exact change of state coordinates. The same stationary dynamics has
mean one for its n-branch coefficient and infinite mean for its head
coefficient. This is a precise limitation of a coordinate-independent
interpretation of a statistical unit.

## 6. The telescoping correction and the coefficient theorem

Pointwise along every admissible orbit,

$$
a_i=A_i2^{k_i-k_{i+1}},\qquad
\boxed{\prod_{i=0}^{N-1}a_i
=2^{k_0-k_N}\prod_{i=0}^{N-1}A_i.}                           \tag{15}
$$

The difference of the two log sums is exactly the boundary term
(k_0-k_N)log2. The strong law applied to the independent k_i,t_i gives

$$
\frac1N\sum_{i<N}\log A_i\longrightarrow2\log(3/4)
\quad\text{almost surely}.
$$

For each epsilon>0, the probabilities P(k_N>=epsilon N) have a finite
sum, by the geometric tail. Borel-Cantelli therefore gives k_N/N -> 0
almost surely. Applying this to (15) yields the same limit for
N^(-1)sum log a_i. A fixed initial k_0 changes no limit. Since the
number of accelerated odd steps at the Nth block endpoint is
$S_N=\sum_{i<N}k_i$, whose ratio to N tends to two, the coefficient
drift per accelerated odd step at those endpoints is log(3/4).

The same limit holds between endpoints for the original odd-step
coefficients. A partial next block of $r<k_N$ steps contains only
valuation-one steps and adds $r\log(3/2)$ to the log product. Since
$k_N/S_N$ tends to zero almost surely, this remainder and the change
of denominator from $S_N$ to $S_N+r$ have vanishing normalized effect.

This is an almost-sure theorem about products of rational branch
coefficients under Haar measure. It is not an almost-sure statement
about real sizes of 2-adic states, and not a theorem about all positive
integer trajectories.

For actual positive integer states there is also an exact size identity,

$$
\frac{u_N}{u_0}
=2^{k_0-k_N}\frac{n_N+1}{n_0+1}.                             \tag{16}
$$

Equivalently, log(u_N/u_0) equals log(n_N/n_0), plus the telescoping
terms (k_0-k_N)log2 and log(1+1/n_N)-log(1+1/n_0). Control of k_N is
needed before transferring an asymptotic size claim between coordinates.

Actual ratios also contain the additive offsets. At the fixed point
n=u=1 one has k=t=k'=1 and A=a=3/4, but the actual size ratios are
one because b=e=1/4. Negative coefficient drift alone cannot replace
control of the affine dynamics. Positive integers form a countable
Haar-null set, so the almost-sure law does not decide any particular
positive integer orbit.

## 7. The other local condition and the product formula

For positive odd integer heads, the inverse (3) must satisfy the exact
integrality condition

$$
3^k\mid 2^{t+k'}u'-2^t+1,
\quad\text{or}\quad
u'\equiv(2^t-1)2^{-t-k'}\pmod{3^k}.                           \tag{17}
$$

Together with positive odd u' and k,t,k'>=1, this is also sufficient
for a positive odd integer input with the declared branch. See
`PROOF.md` for the arithmetic reconstruction. Division by 3^k is
unrestricted in Z_2 because three is a unit there. Hence the local
Haar product law does not by itself retain this integer congruence.

There is a pointwise scalar identity across the two relevant finite
places and the real place:

$$
|A|_\infty|A|_2|A|_3
=\frac{3^k}{2^{k+t}}\,2^{k+t}\,3^{-k}=1.                     \tag{18}
$$

The head coefficient satisfies the same identity with k+t replaced by
t+k'. These are the ordinary normalized absolute values of rational
numbers. The identity involves different places, not Galois-conjugate
embeddings. It establishes neither global bijectivity nor a global
volume-preservation theorem for the piecewise affine block map.

## 8. Standard context and scope

The Haar/Bernoulli setting is classical. Bernstein and Lagarias,
*The 3x+1 Conjugacy Map* (1996), describe the measure-preserving
conjugacy between the half-step Collatz map on Z_2 and the binary shift:
[author-hosted paper](https://cr.yp.to/papers/3x1conjmap-19960215-retypeset20220326.pdf).
Their map convention differs from the accelerated odd map used here.

Tao, *Almost all orbits of the Collatz map attain almost bounded values*,
Forum of Mathematics, Pi (2022), Remark 1.10, explicitly states Haar
invariance on odd 2-adics and independent geometric Syracuse valuations.
Lemma 2.1 gives the affine valuation-word characterization:
[primary journal text](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F).

The branch, code and expectation formulas above were proved directly
for this block/head coordinate system. They are compatible with that
standard setting and are not presented as a new discovery of Bernoulli
Collatz dynamics. They isolate an exact coordinate dependence of the
first moment while retaining the same integrable logarithmic drift.
