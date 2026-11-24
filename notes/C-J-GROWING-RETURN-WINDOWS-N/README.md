# Growing return windows: exact recovery and unsplit blocks

NON-CANONICAL. No authority. All new deductions are candidate-D, L1.
Paper work only; no new scientific computation or formal proof checker.

Owner: A. M. Thorn, ChatGPT-Astra-Sol-20261124-Growing-Windows.
Date: 2026-11-24. Claim: [#2084](https://github.com/mathorn1973/twist-j/issues/2084).
Public basis: Canon v117 at `6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`.

The preceding [#2083](https://github.com/mathorn1973/twist-j/pull/2083)
proved that every fixed-gap gcd reading is eventually periodic. This
continuation lets the range grow with the input and determines what that
larger reading recovers. The supplied unit-relation-depth note is reviewed
as a separate reference. It retains ownership of its results.

## The reading and its exact completion width [candidate-D]

For odd \(n>1\), \(5\nmid n\), set

\[
R(n)=\operatorname{cont}(J^n-1-(J-1)^n),\qquad
A_H(n)=\mathop{\rm lcm}_{\substack{0<d\le H\\n+d\text{ admitted}}}
\gcd(R(n),R(n+d)).
\]

The empty lcm is one. An admitted neighbor is odd and not divisible by
five, so all contributing gaps are even. The lcm collects the prime powers
of the starting content that recur somewhere in the window. Always
\(A_H(n)\mid R(n)\). Write
\(H_*(n)=\min\{H:A_H(n)=R(n)\}\) and
\(r=(n-\chi_5(n))/2\).

The following table is exact for every admitted \(n>1\).
In the power-of-two alternative, \(v\) is a nonnegative integer.

| Input class | Exact \(H_*(n)\) |
| --- | ---: |
| \(n\equiv1\pmod{10}\) | \(n-1\) |
| \(n\equiv3\pmod{10}\) | \(n+3\) |
| \(n\equiv7\pmod{10}\) | \(2(n+1)\) |
| \(n\equiv19\pmod{20}\) | \(4(n-1)\) |
| \(n\equiv9\pmod{20},\ r=3\cdot2^v\) | \(4(n-1)\) |
| \(n\equiv9\pmod{20},\ r\ne3\cdot2^v\) | \(5r-2=(5n-9)/2\) |

Thus \(A_{4(n-1)}(n)=R(n)\) for all inputs, and the coefficient four
is sharp. This bound is linear in the value of the index, not in its bit
length. It is a restoration of a return content, not a primality test.

The elementary upper bounds need no primitive-divisor theorem. The full
classification uses the classical existence of a primitive prime divisor
of \(F_k\) outside \(k=1,2,6,12\), with explicit small-case witnesses.
See [CLASSIFICATION.md](CLASSIFICATION.md) for the source and complete proof.

## When two or three neighbors are necessary [candidate-D]

For \(n\ge53\), multiple neighbors improve on the first single full return
precisely in the last table row. One neighbor requires width \(8r\).
At any width \(5r-2\le H<8r\), the exact minimum number is:

| Additional condition | Minimum number of neighbors |
| --- | ---: |
| \(3\nmid r\) | 2 |
| \(3\mid r\) | 3 |

The two signed factors \(B(r/2,+1)\) and \(B(r/2,-1)\) recover the odd
part. In the second row a third neighbor is necessary to restore the full
power of two; no two neighbors before width \(8r\) can do so.

For example, at \(n=69\), the gcds at distances 102 and 168 are
\(L_{17}\) and \(F_{17}\). Together they restore \(F_{34}=R(69)\),
whereas the first single full return is at distance 272. The number of
neighbors in this theorem and the number of units in an additive relation
in the side note are distinct measures of complexity.

## An exactly solved growing family [candidate-D]

Let \(K=4a+2\), \(a\ge0\), \(r=3^K\), \(n=2r+1\), and
\(Q_j=L_{3^{j-1}}^2+3\) for \(2\le j\le K\). Then

\[
R(n)=L_{3^K}=4\prod_{j=2}^K Q_j.
\]

The factors \(Q_j\) are pairwise coprime. Every prime power dividing
\(Q_j\) has the same exact order \(3^j\) for \(\alpha=\phi^2\).
Let \(c_j\) be the integer in \(\{1,2,3,4\}\) with
\(3^j c_j\equiv1\pmod5\), and put \(D_j=2\cdot3^j c_j\). The entire
window reading, without factoring any \(Q_j\), is

\[
A_H(n)=b(H)\prod_{D_j\le H}Q_j,\qquad
b(H)=\begin{cases}1,&H<4,\\2,&4\le H<12,\\4,&H\ge12.\end{cases}
\]

In particular, for \(u=3^{K-1}\),

\[
A_H(n)=L_u\quad(4u\le H<24u),\qquad
A_{24u}(n)=L_u(L_u^2+3).
\]

Before that final step, \(A_H(n)^3<R(n)\). Every prime divisor of the
missing factor \(L_u^2+3\) waits until width \(24u=4(n-1)\).
These are new primes relative to the earlier blocks, not merely new
powers of a previously visible prime.

For any \(H(n)=o(n)\), along this family only,
\(\log A_{H(n)}(n)/\log R(n)\to0\). A growing but sublinear window can
miss asymptotically all of the logarithmic size of the content. The
derivation and all boundary cases are in [PROOF.md](PROOF.md).

## What longer observation cannot split [candidate-D]

For every individual admitted index \(m\), the same block satisfies

\[
\gcd(Q_j,R(m))\in\{1,Q_j\}.
\]

One prime divisor hitting forces the same signed order condition for
every full prime power in the block. Thus these gcd queries, even against
the complete original return sequence, cannot split a composite \(Q_j\).
No assertion that every \(Q_j\) is composite is made.

The [side-note review](SIDE_NOTE_REVIEW.md) finds no error in its written
unit-kernel, normalized-triple, flag-stream or vertical-gcd arguments.
Its four-unit witnesses separate the two stated equal-order prime pairs.
Its computational counts and unprovided scripts remain unverified here.
A prescribed universal short additive separator remains open.

## Evidence and remaining scope

The result-exposed paper scope was claimed before file edits. Development,
source reading and opposition took place in one shared session. This is
not blind independent confirmation. There is no new finite census or
scientific executable in the package. Repository delivery checks do not
promote the paper claims.

These results concern exact arithmetic observation of the signed-content
sequence. They neither construct a native TWIST-J apparatus nor supply
prime-density, A4 Fourier-cancellation or RH conclusions. The growing-window
recovery problem for this particular aggregate has been classified; the
additive separation problem can proceed as its own line.

See the [handoff record](PROMO-C-J-GROWING-RETURN-WINDOWS-N.md).
