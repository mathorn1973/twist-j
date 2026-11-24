# Common divisors of signed returns

**NON-CANONICAL draft. All deductions have status candidate-D at L1.**
Public basis: Canon v117, main commit
`6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`. Scoped claim: issue #2082.
This note has no Canon authority. Its evidence is a written derivation.

The author's supplied note `C-J-SIGNED-RETURN-GAPS-1` proposed the
fixed-gap identity below. The single-defect factorization comes from
the separate candidate in PR #2081. This candidate studies two indices
and derives their complete common divisor.

## From one gap to an exact common divisor

Let \(j=\zeta_5\), \(J=1+j^2\), \(\phi=-j^2-j^3\), and \(\Delta(n)=J^n-1-j^{2n}\).
Write \(R(n)\) for the nonnegative gcd of the four integral coordinates
of \(\Delta(n)\) in the basis \(1,j,j^2,j^3\).
For positive odd \(n>1\) with \(5\nmid n\), put
\(x=\chi_5(n)\), the quadratic character modulo five, and \(r=(n-x)/2\).
Then \(R(n)=F_r\) for \(n\equiv1\pmod4\) and \(R(n)=L_r\) for
\(n\equiv3\pmod4\). Here \(F_0=0,F_1=1\) and \(L_0=2,L_1=1\);
both sequences satisfy the Fibonacci recurrence.

For a positive even gap \(d\), take \(m=n+d\) with \(5\nmid m\).
Set \(y=\chi_5(m)\), \(s=(m-y)/2\), and \(t=s-r=(d+x-y)/2\).
The proposed identity is

\[
\gcd(R(n),R(m))=\gcd(R(n),C),\qquad
C=\begin{cases}F_t&xy=(-1)^t,\\ L_t&xy\ne(-1)^t.\end{cases}
\]

It holds also at \(t=0\), where the only possible signs give \(C=L_0=2\).
The divisibility argument works for every rational modulus, including
powers of five. The factor \(\sqrt5=-1-2j^2-2j^3\) has integral content one.

There is a closed formula for the gcd itself. Put \(g=\gcd(r,s)\),
\(p=r/g\), and \(q=s/g\).

| Condition | Exact value of \(\gcd(R(n),R(m))\) |
| --- | --- |
| \(x^q=y^p\) | There is a unique sign \(z\) with \(z^p=x,\ z^q=y\). The value is \(F_g\) if \(z=(-1)^g\), and \(L_g\) otherwise. |
| \(x^q\ne y^p\) | The value is \(2\) if \(3\mid g\), and \(1\) otherwise. |

In the first case Bézout's identity combines two power congruences into
one at exponent \(g\). In the second, any common divisor must divide the
difference of two opposite signs. The order of \(\phi^2\) modulo two is
three, which decides whether two survives.

## Gap two

For every admitted odd start \(n>1\) with \(5\nmid n(n+2)\), the gcd is
three exactly at \(n\equiv1\pmod{40}\), two exactly at
\(n\equiv17\pmod{30}\), and one elsewhere. On the class
\(n\equiv1\pmod5\), the extra condition for three is \(n\equiv1\pmod8\).
On \(n\equiv2\pmod5\), the extra condition for two is \(n\equiv-1\pmod3\).

If both indices must additionally be coprime to thirty, the starts are
\(n\equiv11,17,29\pmod{30}\). Among their twelve classes modulo 120,
seven give one, four give two, and only \(n\equiv41\pmod{120}\) gives
three. The corresponding fractions are \(7/12,1/3,1/12\).
They count residue classes and make no primality assumption.

## Gap 182 on the start class two modulo five

Let \(G=\gcd(R(n),R(n+182))\) for odd \(n>1\) with
\(n\equiv2\pmod5\). Here \(x=-1,\ y=1,\ r=(n+1)/2\), and \(s=r+90\).
Since \(5\nmid r\), the reduced index is \(g=\gcd(r,18)\).
The compatible-sign case occurs precisely at \(r\equiv2\pmod4\);
it gives \(L_g\) with \(g\in\{2,6,18\}\).
Equivalently,

\[
G=\gcd(R(n),L_{18}),\qquad L_{18}=5778=2\cdot3^3\cdot107.
\]

| Condition on \(r\) | \(G\) | Classes of \(r\bmod36\) | Fraction of the stated starts |
| --- | ---: | ---: | ---: |
| \(r\not\equiv2\pmod4,\ 3\nmid r\) | 1 | 18 | \(1/2\) |
| \(r\not\equiv2\pmod4,\ 3\mid r\) | 2 | 9 | \(1/4\) |
| \(r\equiv2\pmod4,\ 3\nmid r\) | 3 | 6 | \(1/6\) |
| \(r\equiv2\pmod4,\ 3\mid r,\ 9\nmid r\) | 18 | 2 | \(1/18\) |
| \(r\equiv2\pmod4,\ 9\mid r\) | 5778 | 1 | \(1/36\) |

The table counts **all odd starts in the class two modulo five**. Along
those starts \(r\) advances by five, so every class modulo 36 occurs
once per 36 starts. The maximum requires \(r\equiv18\pmod{36}\), hence

\[
G=5778\quad\Longleftrightarrow\quad n\equiv107\pmod{360}.
\]

The first such pair is \((107,289)\), with \(289=17^2\). Throughout this
domain the divisibility indicators \(\mathbf1_{27\mid G}\) and
\(\mathbf1_{107\mid G}\) are identical: both select precisely the
maximum row.

## Periodicity and the remaining boundary

For every fixed gap, the complete gcd function is eventually periodic,
not merely supported on a finite set of primes. Its value frequencies
therefore follow from residue classes. A fixed finite collection of these
readings cannot by itself be a sound primality recognizer on unbounded
inputs: every selected residue class also contains composite integers.

The progression \(n=119+2310k\), \(k\ge0\), makes the distinction
explicit. Both \(n\) and \(n+2\) are composite, divisible respectively
by seven and eleven, while \(\gcd(R(n),R(n+2))=1\) throughout.
The exact periodic correlation of the 27 and 107 predicates above also
shows why finite exceptional support does not establish independence.

See [the derivations](PROOF.md), [the source and scope review](SOURCES_REVIEW.md),
and [the handoff record](PROMO-C-J-SIGNED-RETURN-GAPS-N.md).
