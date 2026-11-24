# What the scale reader retains

**NON-CANONICAL | candidate-D | exact arithmetic on integer inputs.**
All statements below concern the stated functions and binary inputs.
This note belongs to [coordination issue #2077](https://github.com/mathorn1973/twist-j/issues/2077).

## Normalization and the three fibres

Let $j=e^{2\pi i/5}$, $J=1+j^2$ and $J_n=1+(J-1)^n=1+j^{2n}$
for $n\in\mathbb Z$. This periodic family satisfies $J_0=2$.
Powers of the unit $J$ form a different family, with $J^0=1$.
Write $A(n)=J_n\overline{J_n}=2+j^{2n}+j^{-2n}$,
$D=A(2)-A(1)$, and $\chi(n)=(A(2n)-A(n))/D$.

| $n\bmod 5$ | $A(n)$ in the principal embedding | $\chi(n)$ |
| --- | --- | --- |
| $0$ | $4$ | $0$ |
| $1,4$ | $(3-\sqrt5)/2$ | $+1$ |
| $2,3$ | $(3+\sqrt5)/2$ | $-1$ |

Indeed, $j+j^{-1}$ and $j^2+j^{-2}$ sum to $-1$ and multiply to
$-1$, by the fifth cyclotomic relation. The first is the larger in the
principal embedding, so $D=\sqrt5$ there. The embeddings $j\mapsto j^a$
for $a=2,3$ exchange the two irrational entries and send $D$ to
$-\sqrt5$. The quotient stays fixed because its numerator and denominator
undergo the same embedding. Dividing by $|D|$ instead would reverse the
two signs in those embeddings. The table identifies the quotient with the
quadratic character of $\mathbb F_5^\times$, extended by zero. In
particular $\chi(0)=0$ and $\chi(kn)=\chi(k)\chi(n)$ for all integers.

The three fibres of $A$ are exactly the three fibres of $\chi$.
Each multiplication probe $A(kn)$ depends only on $\chi(k)\chi(n)$
through the table. The whole family, which includes $k=1$, therefore
contains exactly the information in one reading. It gives identical outputs
for $n$ and $-n$ and loses the integer quotient upon division by five.
A single $J_n$, before taking its squared modulus, determines the full
residue modulo five because $j^2$ is primitive.

## Two additive probes

For known $h\not\equiv0\pmod5$, the two integers $\chi(n),\chi(n+h)$
determine $n\bmod5$. The table gives $\chi(u)\equiv u^2\pmod5$, including
at zero. Subtracting the two squares gives the inverse in $\mathbb F_5$,

$$
n\equiv(2h)^{-1}\bigl(\chi(n+h)-\chi(n)-h^2\bigr)\pmod5.
$$

The same reconstruction works from $A(n),A(n+h)$ by applying the table to
each value in the chosen embedding. If $5\mid h$, the two observations
coincide. All these observations have period five on integer inputs.

## How many states does a binary reader need?

Fix a deterministic finite automaton with output after its last input
digit, reading base two from most to least significant. Leading zeros are
permitted. Put $t(n)=(-1)^{s_2(n)}$ for $n\ge0$, where $s_2$
counts the ones in the binary expansion.

* For $\chi(n)$, keep $a=n\bmod5$, start at zero, and on digit
  $d\in\{0,1\}$ update $a\mapsto2a+d\bmod5$. All five states are
  reachable. If $a\ne b$, choose the three-bit suffix representing
  $u\in\{0,1,2,3,4\}$ with $u\equiv-8a\pmod5$. The first state then
  gives output zero and the second gives a nonzero output because
  $8(b-a)\ne0\bmod5$. Thus five states are necessary.
* For $t(n)$, two states suffice. Start with sign $+1$ and multiply
  it by $(-1)^d$ on digit $d$. Both outputs occur, so two are necessary.
* For the ordered pair $(\chi(n),t(n))$, use the product of the two
  automata. For each $0\le a<5$, the integers $a$ and $8\cdot25+a$
  have the same residue modulo five and opposite digit parities. The
  summands $8\cdot25$ and $a$ have disjoint binary digits and
  $25=(11001)_2$ has odd digit sum.
  Thus all ten states occur. Distinct residues are separated by the same
  suffix as above. For equal residues and opposite parities, the current
  second output already differs. Ten states are necessary.

## The first four signs and the full correlation

The ordered unit residues $1,2,3,4$ give $+,-,-,+$, the Thue-Morse
signs $t(0),t(1),t(2),t(3)$. At the next index the direct comparison
gives $\chi(5)=0$ and $t(4)=-1$. Deleting all multiples of five
gives a repetition of the four-character block. The fifth sign in that
stream is $+1$.
There is also an exact composition $\chi(2^{s_2(n)})=t(n)$.
Its argument is a power of two built from the digit sum. This composition
is already recorded in
[RAMIFIED-TM-SYMPLECTIC-ORIENTATION](../../probes/P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-2/RESULT.md).

For the direct comparison at integer shift $h$, put
$S_h(N)=\sum_{n=0}^{N-1}t(n)\chi(n+h)$. For every integer $m\ge1$,

$$
S_h(16^m)=5^m\chi(h).
$$

This is the character specialization of the existing NON-CANONICAL
block identity in [M03, contact-history consolidation](../C-J-CONTACT-HISTORY-CONSOLIDATION-N/README.md).
With $P e_a=e_{a+1\bmod5}$ and $E$ the $5$-by-$5$ matrix of ones,
M03 gives $\sum_{n<16^m,\,n\ge0}t(n)P^n=5^{m-1}(5I-E)$. Apply both sides
to $e_0$, and multiply the coefficient of $e_a$ by $\chi(a+h)$ before
summing over $a$. The contribution from $E e_0$ vanishes since the five
character values sum to zero. The contribution from $5I e_0$ gives the
displayed formula. Thus the direct sum is zero for $h=0$. For $h=1$,
the shift matching the first four signs, its mean is exactly $(5/16)^m$.

The full sequence of means tends to zero for every $h$. On an aligned
interval $[b16^m,(b+1)16^m)$, write $n=b16^m+v$. The binary digits of
the two summands are disjoint, so $t(n)=t(b)t(v)$. The interval sum is
$t(b)S_{h+b16^m}(16^m)$ and has absolute value at most $5^m$. This
also holds at $m=0$ by the single-term bound. For any integer $N\ge1$,
its base-sixteen expansion partitions $[0,N)$ from largest to smallest
places into at most fifteen aligned intervals of each size $16^m$.
For the unique $L$ with $16^L\le N<16^{L+1}$ we obtain

$$
|S_h(N)|\le 15\sum_{m=0}^{L}5^m
=\frac{15(5^{L+1}-1)}4.
$$

Since $N\ge16^L$, the absolute mean is bounded by $(75/4)(5/16)^L$,
which tends to zero uniformly in the integer shift $h$.
