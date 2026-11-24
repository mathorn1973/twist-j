# Short trace tests for equal-order prime divisors

**NON-CANONICAL. No authority. Candidate-D, L1.**

Let $j=\zeta_5$, $\mathcal O=\mathbb Z[j]$, $\phi=-j^2-j^3$ and $\alpha=\phi^2$. For a prime $p>5$, write $h_p$ for the multiplicative order of $\alpha$ modulo the rational ideal $p\mathcal O$. A signed unit summand is one label $\pm j^a\phi^e$. Weight counts summands with multiplicity. A separator for distinct primes $p,q$ vanishes modulo exactly one of $p\mathcal O$ and $q\mathcal O$.

For $h\ge 2$, define the integer traces and the prescribed test family by

$$
T_i=\alpha^i+\alpha^{-i},\qquad
\mathcal S_K(h)=\left\{-1+\sum_{\nu=1}^{k}\epsilon_\nu T_{i_\nu}\ :\
0\le k\le K,\ \epsilon_\nu\in\{-1,1\},\ 0\le i_\nu<h\right\}.
$$

The conjugate of $\phi$ in $\mathbb Z[\phi]$ is $-\phi^{-1}$, so $T_i$ is an algebraic integer fixed by that conjugation and lies in $\mathbb Z$. Each trace contributes two signed units of phase $j^0$. A test in $\mathcal S_K(h)$ has weight at most $2K+1$ and uses $\phi$ exponents of absolute value at most $2(h-1)$. With ordered choices and repetitions the number of tests is at most $\sum_{k=0}^{K}(2h)^k$. For a rational integer $S$, membership in $p\mathcal O$ is equivalent to $p\mid S$ by the integral basis $1,j,j^2,j^3$.

## Separation bounds

Put $b=1+\operatorname{lcm}(2,h)/2$. Let $p,q>5$ be distinct primes with $h_p=h_q=h$. If one of the two primes, say $p$, satisfies $b^2>p$, then $\mathcal S_{32}(h)$ contains a separator of weight at most 65. If $b^3>2p$, then $\mathcal S_{384}(h)$ contains a separator of weight at most 769.

For a positive integer $N$ divisible by such a pair, sufficient conditions on the available inputs $N,h$ are

| Condition | Test family | Maximum weight |
| --- | --- | ---: |
| $b^4>N$ | $\mathcal S_{32}(h)$ | 65 |
| $b^6>4N$ | $\mathcal S_{384}(h)$ | 769 |

Indeed, the smaller prime of each pair is at most $\sqrt N$. A witness gives $1<\gcd(N,S)<N$. These implications apply to each pair in the class of order $h$. For fixed $K$, the test count is polynomial in the value of $h$. Polynomial time in the bit length of $N,h$ remains unproved by this construction.

## Trace values and their products

Let $R_p=\mathbb Z[\phi]/p\mathbb Z[\phi]$. The elements $1,\phi$ remain linearly independent modulo $p\mathcal O$ because $\phi=-j^2-j^3$ in the integral basis above. Thus $R_p$ embeds in $\mathcal O/p\mathcal O$, and $\alpha$ has the same order in both rings. The quadratic polynomial $X^2-X-1$ has discriminant five. Consequently $R_p$ is either $\mathbb F_{p^2}$ with its quadratic conjugation or $\mathbb F_p\times\mathbb F_p$ with the two factors exchanged. In both cases the norm-one group is cyclic, of order $p+1$ in the field and $p-1$ in the product. The subgroup $H_p=\langle-1,\alpha\rangle$ of this group has order $\operatorname{lcm}(2,h)$. The order $h$ exceeds one because $\alpha-1=\phi$ is a unit.

For $u\in H_p$, its trace is $u+u^{-1}\in\mathbb F_p$. The trace has exactly the inversion orbits as its fibers. In the field case this follows from the roots of $X^2-(u+u^{-1})X+1$. In the product case write $u=(v,v^{-1})$. The first coordinate determines $u$, and the same quadratic equation applied to $v$ gives the assertion. There are two singleton orbits, those of $1$ and $-1$. The resulting signed trace set

$$
B=\{\pm T_i\bmod p\ :\ 0\le i<h\}\subseteq\mathbb F_p
$$

therefore satisfies $|B|=b$. It is symmetric under negation. The exact identity

$$
T_iT_j=T_{i+j}+T_{i-j}
$$

holds for all integer indices. Modulo $p$ the indices may be reduced modulo $h$. Each product of two signed traces is a sum of two signed traces. Iteration expresses each product of three as a sum of four signed traces.

## Additive covering

For a subset $C$ of $\mathbb F_p$, write $kC$ for its $k$-fold sumset and $C^n$ for its $n$-fold product set. Write $XY$ for the set of products with one factor from $X$ and one from $Y$.

Glibichuk's symmetric product-set theorem gives $8XY=\mathbb F_p$ if $Y=-Y$ and $|X||Y|>p$. Thus $b^2>p$ gives $8B^2=\mathbb F_p$. The trace product identity lifts each residue to an integer sum of at most 16 signed traces. [Glibichuk 2006, Theorem 2][G06].

Suppose $b^3>2p$. If $b^2>p$ the preceding bound already suffices. Otherwise $b^2\le p-1$ since $p$ is prime. The difference-set estimate for products gives

$$
|6B^2|=|3B^2-3B^2|\ge\frac{b^2(p-1)}{b^2+p-1}\ge\frac{b^2}{2}.
$$

Here the equality uses $B=-B$. Hence $|6B^2|\,|B|>p$. Apply the symmetric product-set theorem with $X=6B^2$ and $Y=B$. It gives $8(6B^2)B=\mathbb F_p$, where the notation means $8$ sums of products from $X$ and $Y$. Distributing the products shows that this set is contained in $48B^3$. Each residue therefore lifts to an integer sum of at most $48\cdot4=192$ signed traces. [Glibichuk and Konyagin 2007, Corollary 3.6][GK07]. [Glibichuk 2006, Theorem 2][G06].

## From covering to a separator

Suppose every residue $x\in\mathbb F_p$ has a representative $R_x$ that is a sum of at most $k$ signed traces from the allowed indices. For cyclic addition by one in $\mathbb F_p$, put

$$
S_x=R_{x+1}-R_x-1.
$$

Every $S_x$ belongs to $\mathcal S_{2k}(h)$ and is divisible by $p$. Since $x\mapsto x+1$ permutes the residues, the sum in $\mathbb Z$ is

$$
\sum_{x\in\mathbb F_p}S_x=-p.
$$

If all $S_x$ were divisible by $q$, then $q$ would divide $p$. Thus one of them separates the pair. Taking $k=16$ or $k=192$ from the covering step gives the two stated bounds. The representatives enter the existence proof. The list of tests is specified by $h$ and $K$ alone.

## Exceptional primes

Define $b_p=1+\operatorname{lcm}(2,h_p)/2$. The primes $p\le X$ that satisfy $b_p^3\le2p$ number $O(X^{2/3})$. Indeed, $b_p\ge h_p/2$ implies $h_p\le 2(2X)^{1/3}$. Write $F_n$ for the Fibonacci numbers with $F_0=0,F_1=1$. If $h_p=r$, then $\phi^{2r}=1$ modulo $p$, and the conjugate $\psi=-\phi^{-1}$ also satisfies $\psi^{2r}=1$. The identity $(\phi-\psi)F_{2r}=\phi^{2r}-\psi^{2r}$ gives $p\mid F_{2r}$ because $(\phi-\psi)^2=5$ is invertible modulo $p$.

For $H=\lfloor2(2X)^{1/3}\rfloor$, all the exceptional primes divide $\prod_{r=1}^{H}F_{2r}$. The logarithm of the product is $O(H^2)$, using $F_{2r}\le2^{2r}$. Each distinct prime contributes at least $\log 2$ to this logarithm. This proves the count and shows that the primes with $b_p^3>2p$ have relative density one among primes. The 769-unit conclusion applies to every equal-order pair with at least one prime in that set. The count concerns individual primes. The frequency among equal-order pairs or blocks and the constant-arity question for pairs made up of two exceptional primes remain open here.

## References

- A. A. Glibichuk, *Combinational properties of sets of residues modulo a prime and the Erdős–Graham problem*, Mathematical Notes **79** (2006), 356–365, Theorem 2. The author also states the prime-field result in [arXiv:0801.2021](https://arxiv.org/abs/0801.2021). [Published paper][G06].
- A. A. Glibichuk and S. V. Konyagin, *Additive properties of product sets in fields of prime order*, CRM Proceedings & Lecture Notes **43** (2007), 279–286, Corollary 3.6. [Author preprint][GK07]. [Published chapter](https://doi.org/10.1090/crmp/043/15).

[G06]: https://doi.org/10.1007/s11006-006-0040-8
[GK07]: https://arxiv.org/abs/math/0702729
