# Prescribed additive separators for equal-order return blocks

**NON-CANONICAL. No authority. L1. All new mathematical deductions are candidate-D.**

Owner: A. M. Thorn, session ChatGPT-Astra-Sol-20261124-Additive-Separators.
Public ownership claim: [#2086](https://github.com/mathorn1973/twist-j/issues/2086).
Basis: public main `6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`, verified Public Canon v117.
The claim exposed the paper results before any file edit. No scientific computation,
enumeration, verifier, or numerical search was performed in this lane.

## Question and reader

Can a prescribed short additive family split a composite block whose prime divisors
have the same return order, without choosing tests from a known factorization?

Write $\mathcal O=\mathbb Z[j]$, $j=\zeta_5$, $J=1+j^2$,
$\phi=-j^2-j^3=j/J$, and $\alpha=\phi^2$. For a rational prime $p>5$,
$h(p)$ is the order of $\alpha$ in the **whole** quotient
$\mathcal O/p\mathcal O$. A test is an integral sum of signed units
$\pm j^a\phi^b$. Its flag says whether the whole sum belongs to $p\mathcal O$.
For a known integer block $N$, the accessible readout is
$\gcd(N,\operatorname{cont}_{\mathcal O}(S))$.

Five different resources must be distinguished:

1. the number of summands, counted with multiplicity;
2. the number of tests in the menu;
3. the span of the unit exponents;
4. the amount of arithmetic needed to find a separating test;
5. whether the menu is one fixed list of elements or a fixed rule indexed by $N,h$.

The results answer different versions of this question.

| Scope | Paper conclusion | Main qualification |
| --- | --- | --- |
| One finite list of concrete sums, all exponents fixed once | Impossible for all common-order blocks | Infinitely many collision orders are proved here |
| One six-unit rule whose exponents use the common order | Splits every displayed block of order $5^{k+1}$ | Does not separate two primes inside the same resulting factor |
| A bounded-weight family determined from $h$ | 65 or 769 units suffice under explicit conditions on $N,h$ | The menu can contain a very high power of $h$ tests |
| Arbitrary known return block | A factor-independent menu exists, with weight linear in its return index | Its scalar implementation is order-filtered trial division |
| One absolute bound on weight for every equal-order pair | Remains open here | A growing list is not a fixed concrete list |

## The six-unit split

For $r=5^k$, $k\ge1$, put $f=F_r$ and

$$
B_r=\frac{L_{5r}}{L_r},\qquad A_\pm=5f^2\pm5f+1.
$$

The classical Aurifeuilian identity gives $B_r=A_-A_+$. Both factors exceed
one and are coprime. Every prime power dividing $B_r$ has exact $\alpha$-order
$h=5r$. The fixed expression

$$
S_+(r)=\phi^{3r}+\phi^{-3r}-\phi^r-\phi^{-r}+\phi+\phi^{-1}
$$

satisfies

$$
\gcd(B_r,\operatorname{cont}S_+(r))=A_-.
$$

It uses six signed units, with no factor-dependent exponent. In integers it is
enough to calculate $\gcd(B_r,F_{3r}-F_r+1)$. Changing the final plus sign to
a minus sign selects $A_+$. The same read works directly on the original
return $R(10r+1)=L_{5r}$, without first removing $L_r$.

At $r=5$, the two factors are $101$ and $151$. The statement is an exact
factor extraction, including prime powers. Six is an upper bound for this
rule, not a claimed minimum for each individual pair. The classical identity,
the exact-order proof, the whole-ideal gcd, and a quadratic Gauss-sum form
are given in [SIX_UNIT_SPLIT.md](SIX_UNIT_SPLIT.md).

## General trace families

Define $T_i=\alpha^i+\alpha^{-i}=L_{2i}$ and

$$
\mathcal S_K(h)=\left\{-1+\sum_{\nu=1}^{k}\epsilon_\nu T_{i_\nu}:
0\le k\le K,\ \epsilon_\nu\in\{-1,1\},\ 0\le i_\nu<h\right\}.
$$

This list is specified before knowing any factor. Set
$b=1+\operatorname{lcm}(2,h)/2$. For distinct prime divisors of a block $N$
sharing order $h$, the following **sufficient** conditions give pairwise separation:

$$
b^4>N\quad\Longrightarrow\quad\mathcal S_{32}(h)\text{ suffices};
\qquad
b^6>4N\quad\Longrightarrow\quad\mathcal S_{384}(h)\text{ suffices}.
$$

These are respectively 65-unit and 769-unit tests. The proof uses two classical
finite-field set estimates and an integral telescoping argument. If $R_x$ is
a short trace representative of each residue modulo $p$, all expressions
$R_{x+1}-R_x-1$ vanish modulo $p$, while their sum is exactly $-p$.
They therefore cannot all vanish modulo a different prime $q$.

The possible failure of the weaker prime-level condition $b_p^3>2p$ occurs
at only $O(X^{2/3})$ primes up to $X$. This does **not** assert density one
among equal-order pairs or among composite return blocks. The sparse-order
exception remains a genuine domain restriction. Full proofs, exact family
sizes, and original sources are in [TRACE_SEPARATORS.md](TRACE_SEPARATORS.md).

## Unconditional baseline and a resource obstruction

If $N\mid F_r$ or $N\mid L_r$ and $s=\lceil r/2\rceil\ge2$, a prescribed
nearest signed Lucas expansion gives a menu with individual unit weight
at most $\lfloor(2s+4)/3\rfloor$. It separates every pair of distinct primes
of a given common order in $N$. The menu is the integers up to $\sqrt N$
in the two permitted order classes, rewritten in units. Its arithmetic cost
is therefore the cost of order-filtered trial division, not a new speed bound.

Conversely, for a nonzero $k$-unit sum of exponent span $H$, divisibility
by $p$ in the whole quotient implies

$$
2p\le k\bigl(\phi^{H/2}+\phi^{-H/2}\bigr).
$$

This restricts all menus with a prescribed weight and span, regardless of
how many tests they contain. An integer-only Lucas form and both complete
proofs appear in [BASELINE_AND_HEIGHT.md](BASELINE_AND_HEIGHT.md).

## Parallel work and status

The user's parallel `C-J-UNIT-ARITY-BOUND-1` note was retrieved in full.
Its integral phase-projection argument was checked on paper: in this
equality-only reader, allowing $j$ phases cannot lower the least separating
unit weight. Its finite minima six and eight remain the source's reported
candidate-C results; the exhaustive programs were not executed here.
See [PARALLEL_REVIEW.md](PARALLEL_REVIEW.md) for exact boundaries and the
relation between the two developments.

Two Astra agents handled construction and opposition, and a Sol agent handled
the finite-field argument and primary literature. Each mathematical file was
read by the root and another team member. This was shared-context internal
review, not a blind independent confirmation. Repository checks are reported
in the PR delivery record; they do not promote these paper deductions.

No new primality test, general efficient factoring method, physical decoder,
RH/A4 theorem, or cross-layer lift is established. No Canon entry is changed.
The complete scoped handoff is
[PROMO-C-J-SHORT-ADDITIVE-SEPARATORS-N.md](PROMO-C-J-SHORT-ADDITIVE-SEPARATORS-N.md).
