# Unrestricted exponents still bound the whole proper divisor

**NON-CANONICAL. NO AUTHORITY. Candidate-D, L1 arithmetic.**

Paper continuation of claim #2090 / PR #2092. The input is the
full-divisor theorem in `DENOMINATOR_RIGIDITY.md` at
`0b81796c01d4bee47eceb6e451670ea0d233610b`. No new finite search or
scientific execution is used below. The simultaneous approximation argument
is elementary. A parallel conversation reportedly obtained a related
conditional prime-size bound for short relations; no novelty or independent
priority claim is made here. Its unseen proof and finite evidence are not
premises of this note.

Let $m=5^k$, $k\ge1$, and let
\[
 A=A_\sigma(m)=5F_m^2+5\sigma F_m+1,\qquad \sigma\in\{-1,1\}.
\]
Work in $\mathcal O=\mathbb Z[j]$, $j=\zeta_5$, with
$\phi=-j^2-j^3$. A test is a sum of at most $w$ signed units
$\pm j^a\phi^e$, with arbitrary integer exponents and repetitions.
Its output is $g=\gcd(A,\operatorname{cont}S)$; content zero is zero.

## 1. The integer bound

For integers $w\ge2$ and $Q\ge1$ satisfying $Q^{w-1}\le m$, define
\[
 B_Q=\left\lceil\frac mQ\right\rceil-1,
 \qquad
 V_w(m,Q)=w^{4Q^{w-1}}L_{4B_Q}.
\]
Here $L_0=2,L_1=1$ and $L_{n+2}=L_{n+1}+L_n$. Put
\[
 U_w(m)=\min_{1\le Q\le\lfloor m^{1/(w-1)}\rfloor}V_w(m,Q).       \tag{1}
\]
All quantities in (1) are nonnegative integers, the minimization is finite,
and no factor of $A$ is used. The power/root notation in the range means the
integer test $Q^{w-1}\le m$; no floating point is required.

**Theorem.** For every test of weight at most $w$,
\[
                 g=A\quad\hbox{or}\quad g\le U_w(m).                   \tag{2}
\]
The bound includes every prime-power multiplicity in the whole proper gcd.
The exponents, signs and phases may be chosen adaptively from any earlier
outputs. The number of tested expressions is unrestricted.

Weight one always has $g=1$. At weights two and three, the earlier
`THREE_UNIT_OBSTRUCTION.md` gives the stronger exact result $g\in\{1,A\}$.
Equation (2) is intended for $w\ge4$; its derivation remains valid for
$w=2,3$.

### Simultaneous reduction of the exponents

The empty sum has $g=A$ and already satisfies the conclusion. Take a
nonempty actual test with $1\le v\le w$ summands. Multiplication by the inverse
of the first summand preserves content, since multiplication by an integral
unit and its inverse are integral unimodular maps. We may therefore take
the first exponent to be zero. If $v=1$ the theorem is immediate. Otherwise
write the remaining exponents as $e_2,\ldots,e_v$.

Consider the $Q^{w-1}+1$ vectors
\[
 (te_2\bmod m,\ldots,te_v\bmod m),
 \qquad 0\le t\le Q^{w-1},
\]
with all residues in $[0,m)$. Partition each coordinate interval into $Q$
half-open intervals of equal length $m/Q$. There are $Q^{v-1}$ boxes, at
most $Q^{w-1}$. Two vectors share a box. Taking their positive index
difference gives an integer
\[
             1\le D\le Q^{w-1}\le m.
\]
For suitable integers $a_i$ their coordinate differences are
\[
 b_i=De_i-a_im,\qquad |b_i|<m/Q.
\]
Set $a_1=b_1=e_1=0$. Since the $b_i$ are integers,
\[
             |b_i|\le B_Q,
 \qquad
 H=\frac{\max b_i-\min b_i}{D}\le\frac{2B_Q}{D}.                    \tag{3}
\]
Thus the original exponents, without changing the test, have the form
$e_i=(a_im+b_i)/D$ required by the prior denominator theorem. Because
$D\le m=5^k$, the five-part $5^{v_5(D)}$ divides $m$ automatically.

### Application of the full-divisor theorem

The prior theorem says that either $g=A$, or
\[
 g\le
 \left[\frac v2\left(\phi^{H/2}+\phi^{-H/2}\right)\right]^{4D}.
\]
Using $v\le w$, (3), and $\phi>1$ gives
\[
 g\le w^{4D}\phi^{2DH}
   \le w^{4Q^{w-1}}\phi^{4B_Q}
   \le w^{4Q^{w-1}}L_{4B_Q}=V_w(m,Q).                                 \tag{4}
\]
The last inequality uses
$L_{4B_Q}=\phi^{4B_Q}+\phi^{-4B_Q}$, also at $B_Q=0$.
Equation (4) holds for every admitted $Q$, proving (2).

The unit exponents can be arbitrarily large. Their magnitudes disappear
when their residues modulo $m$ are placed in boxes; the resulting slopes
$a_i$ are allowed to be arbitrarily large by the input theorem. This is a
proof of a bound, not a new algorithm for finding a useful test. Constructing
the auxiliary $D$ by the displayed pigeonhole search is unnecessary when
one merely evaluates the public integer threshold (1).

## 2. All large prime powers remain together

Define, for the statement only,
\[
 A_{>U}=\prod_{\substack{p\mid A\\p>U_w(m)}}p^{v_p(A)}.
\]
No factorization of $A$ is needed to choose or evaluate the tests or (1).

For every test of weight at most $w$,
\[
 \gcd(A_{>U},\operatorname{cont}S)\in\{1,A_{>U}\}.                     \tag{5}
\]
Indeed a proper $g$ is at most $U_w(m)$, so it is divisible by no prime
$p>U_w(m)$. In the other case $g=A$, all prime powers occur completely.
Hence any two distinct prime divisors of $A$ above this threshold have
identical vanishing flags for every such expression. This includes an
arbitrarily long or adaptive menu: the pointwise assertion (2) applies to
every test that the menu eventually chooses.

The threshold in (5) compares **prime bases** with $U_w(m)$. A small prime
$p$ whose power $p^{v_p(A)}$ is large can still occur partially in a proper
gcd. In that case (2) bounds the entire extracted power by $U_w(m)$.

Equation (5) does not forbid reading the large component as the remainder
after a separate extraction of small factors. It says that these unit-sum
flags do not distinguish its distinct prime divisors from one another.

## 3. Fixed weight gives a subexponential proper output

For a fixed $w\ge2$, take $Q=\lfloor m^{1/w}\rfloor$. It is admitted in
(1). As $m$ tends to infinity through the tower,
\[
 \log U_w(m)
 \le \bigl(4\log w+4\log\phi+o(1)\bigr)m^{1-1/w}.                    \tag{6}
\]
This follows from $Q\sim m^{1/w}$, $B_Q\sim m^{1-1/w}$ and
$L_{4B_Q}\le2\phi^{4B_Q}$. In particular,
\[
                 U_w(m)=\exp\bigl(O_w(m^{1-1/w})\bigr).                \tag{7}
\]
For comparison, the exact Binet identity at odd $m$ gives
\[
 A_\sigma(m)=\phi^{2m}+\phi^{-2m}+3
             +\sigma\sqrt5\,\bigl(\phi^m+\phi^{-m}\bigr),
\]
so $\log A_\sigma(m)=2m\log\phi+o(1)$.
Consequently, for every fixed rational $\delta>0$ and fixed $w$, all
sufficiently large indices satisfy
\[
              g\ne A\quad\Longrightarrow\quad g<A^\delta.              \tag{8}
\]
At a concrete input one can use the entirely integer certificate
$U_w(m)^b<A^a$ for $\delta=a/b$, with $a,b$ positive integers.

Thus a fixed unit weight eventually extracts only a subpower-sized proper
divisor of a side, regardless of its exponent choices. This is stronger
than saying that one fixed formula eventually fails, but it does not say
that every side has a large prime divisor or two large prime divisors.

One can optimize (1) over all admitted integers $Q$. Its leading continuous
proxy is
\[
        4(\log w)Q^{w-1}+4(\log\phi)m/Q.
\]
This observation is optional; (1) is already an exact finite prescription.

## 4. Macroscopic proper extraction forces growing weight

Let $0<\delta<1$ be fixed and consider any sequence of proper outputs
$A^\delta\le g<A$. Let $r\ge1$ be any fixed integer with
$5^r>2/\delta$. Then their weights necessarily satisfy
\[
                  w\ge k/r-O_\delta(\log\log(k+2)),\qquad m=5^k.       \tag{9}
\]
The constant in the error may also depend on the fixed choice of $r$.

**Proof.** If $r(w-1)>k$, the claimed lower bound already follows.
Otherwise choose $Q=5^r$ in (4). It is admitted, and for large $k$,
$B_Q=m/5^r-1$. Therefore
\[
 \log g\le4\,5^{r(w-1)}\log w
              +4(m/5^r-1)\log\phi.                                   \tag{10}
\]
Since $\log A=2m\log\phi+o(1)$ and
$2\delta-4/5^r>0$, the assumption $g\ge A^\delta$ implies
\[
             5^{r(w-1)}\log w\ge c_{\delta,r}m
\]
for all sufficiently large $k$ and some fixed positive constant. Taking
logarithms gives
\[
 r(w-1)\log5\ge k\log5-\log\log w+O_{\delta,r}(1).
\]
In the case under consideration $w\le k/r+1$, so
$\log\log w=O(\log\log(k+2))$. This proves (9). Weights at most three
cannot supply a proper output at all, by the preceding package.

For example, if a side has two distinct primes both at least $A^\delta$,
any test separating them is proper and its gcd is at least one of those
primes. It therefore obeys (9). The same condition excludes a universal
constant weight along any unbounded sequence of such balanced sides.

Existence of an unbounded sequence of those sides is **not** proved here.
Even the previous, weaker question whether infinitely many individual
sides have two distinct prime divisors remains open in this work. Thus (9)
is a resource theorem and a conditional route to unbounded minimum weight,
not an unconditional resolution of the constant-weight question.

## 5. Covering and separation are different tasks

For completeness, a separate elementary counting guard applies to any
proposed full residue reconstruction. If a specified alphabet has $t$
available signed values, sums of at most $s$ of them have at most
\[
                            {t+s\choose s}
\]
different results: select a multiset of size at most $s$ from $t$ labels.
Repeated numerical values only lower this count. Covering $\mathbf F_p$
therefore requires ${t+s\choose s}\ge p$; covering the entire quadratic
algebra requires ${t+s\choose s}\ge p^2$.

In this tower the signed real-unit alphabet has $4h=20m$ labels, where
$h=5m$. If a prime is at least $\exp(cm)$ for a fixed $c>0$, this count
forces $s$ to be at least a positive constant times $m$ for full quadratic
covering. Indeed for $t=20m$ and $s=o(m)$,
$\log{t+s\choose s}\le s\log(e(t+s)/s)=o(m)$.

This is a limitation of a full covering argument, not a lower bound for a
single pair separator. The known four-unit witness at $m=25$ does not
construct a small additive basis for its prime quotient, and requires no
such basis.

## Falsifiers and limits

* An admitted unit sum with a proper gcd exceeding (1) would refute (2).
* A proper gcd containing any prime above (1) would refute (5).
* A failure of the simultaneous box construction or of the inherited
  full-divisor theorem would invalidate the corresponding proof step.
* No prime factorization, finite census, infinitude statement, efficient
  factoring claim or public scientific promotion is supplied by this note.

The related parallel arity result should be compared by its actual proof
and scope before publication. The distinction asserted here is the full
proper gcd, with all valuations, obtained by an explicit application of
the already owned denominator theorem. It is not a priority assertion.
