# Growing windows of signed return contents

NON-CANONICAL. No authority. All new deductions are candidate-D, L1.
Paper proof. No scientific code was run.

Owner: A. M. Thorn, ChatGPT-Astra-Sol-20261124-Growing-Windows.
Claim: [#2084](https://github.com/mathorn1973/twist-j/issues/2084).
Public basis: `6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`, Public Canon v117.

The preceding signed-gaps work supplies the single-index content and the signed
gcd law and credits the supplied C-J-SIGNED-RETURN-GAPS-1 with the original gap
identity. The separate supplied C-J-UNIT-RELATION-DEPTH-1 retains its own
scope and ownership. The growing-window results below use the signed gcd law and
elementary order arguments.
[Signed-gaps proof at the immutable head of #2083](https://github.com/mathorn1973/twist-j/blob/4875cad870dcf59d44a9d859455fcdec8e1468a3/notes/C-J-SIGNED-RETURN-GAPS-N/PROOF.md)

## 1. Contents, signed gcds and windows

Let \(j=\zeta_5\), \(\mathcal O=\mathbb Z[j]\), \(J=1+j^2\),
\(\phi=-j^2-j^3\), and \(\alpha=\phi^2\). We have \(J\phi=j\),
\(\phi^2=\phi+1\), and the real conjugate of \(\phi\) is
\(\bar\phi=-\phi^{-1}\). The rational content of an element of \(\mathcal O\)
is the nonnegative gcd of its coefficients in \(1,j,j^2,j^3\). Thus a
positive integer \(q\) divides its content exactly when the element is zero
in \(\mathcal O/q\mathcal O\). Multiplying by a unit preserves content.

An admitted index is an odd integer \(n>1\) coprime to five. Write
\(x=\chi_5(n)\), where \(\chi_5\) is the quadratic character modulo five,
and \(r=(n-x)/2\). The return content is
\[
 R(n)=\operatorname{cont}(J^n-1-j^{2n}),\qquad
 B(a,e)=\operatorname{cont}(1-e\alpha^a)\quad(e=\pm1).
\]
On the four admitted residues, \(1+j^{2n}=xj^n\phi^{-x}\).
It follows that \(J^n-1-j^{2n}=J^n(1-x\alpha^r)\), so \(R(n)=B(r,x)\).
For the Fibonacci and Lucas sequences take \(F_0=0,F_1=1,L_0=2,L_1=1\),
both with recurrence \(v_{a+2}=v_{a+1}+v_a\). Binet's identities give
\[
 B(a,e)=
 \begin{cases}F_a,&e=(-1)^a,\\L_a,&e\ne(-1)^a.\end{cases}                 \tag{1}
\]
Indeed, after multiplication by the unit \(-e\phi^{-a}\), the element
\(1-e\phi^{2a}\) becomes \(\phi^a-e\phi^{-a}\), equal to
\(\sqrt5 F_a\) or \(L_a\), respectively. The coordinates of
\(\sqrt5=-1-2j^2-2j^3\) have gcd one. The congruence test therefore
includes all rational prime powers, including powers of two and five.

For a second admitted index \(m=2s+y\) with \(y=\chi_5(m)\), put
\(g=\gcd(r,s),\ a=r/g,\ b=s/g\). If \(x^b=y^a\), there is a unique sign
\(z\) with \(z^a=x,z^b=y\), and
\[
 \gcd(R(n),R(m))=B(g,z).                                                \tag{2}
\]
In fact, integers \(i,k\) with \(ia+kb=1\) give \(z=x^iy^k\). Modulo
each positive integer, \(\alpha^r=x,\alpha^s=y\) together are equivalent
to \(\alpha^g=z\), by the same identity and invertibility of \(\alpha\).
If \(x^b\ne y^a\), any common divisor divides the difference of these
signs, hence divides two. Modulo two both signs coincide and \(\alpha\)
has order three. This follows from \(\phi^2=\phi+1\), \(\phi^3=1\)
and \(\phi\ne1\) modulo two. The incompatible gcd is therefore two
when \(3\mid g\) and one otherwise.

For an integer \(H\ge0\) take
\[
 A_H(n)=\mathop{\rm lcm}_{\substack{0<d\le H,\ d\ {\mathrm{even}}\\
                                  n+d\ {\rm admitted}}}
                \gcd(R(n),R(n+d)),\qquad \operatorname{lcm}(\varnothing)=1.
                                                                         \tag{3}
\]
This increasing sequence in the divisibility order always divides \(R(n)\).
For a prime power \(q\mid R(n)\), say that \(q\) is visible at \(H\) if
\(q\mid A_H(n)\). This holds exactly when at least one admitted neighbor
in the window has \(q\mid R(n+d)\), by the prime-power rule for an lcm.

## 2. Locating a prime power by its order [candidate-D]

For a rational prime power \(q\), write \(h=\operatorname{ord}_q(\alpha)\)
in \((\mathcal O/q\mathcal O)^\times\). The permitted indices \(m=2s+y\)
are given by this residue table, subject to \(m>1\).

| Sign \(y\) | Permitted \(s\bmod5\) |
|---|---|
| \(+1\) | \(0,4\) |
| \(-1\) | \(2,4\) |

For \(q\mid R(n)\), a neighbor has \(q\mid R(m)\) precisely when
\(\alpha^{s-r}=xy\pmod{q\mathcal O}\). Equal signs require
\(s-r\equiv0\pmod h\). For odd \(q\), the cyclic subgroup contains
\(-1\) exactly for even \(h\), when the opposite-sign congruence is
\(s-r\equiv h/2\pmod h\). To see this,
\(t=\alpha^{h/2}\) for even \(h\) is a nonidentity involution. Its real
conjugate is its inverse, hence coincides with \(t\) modulo \(q\).
Consequently \(2t\equiv t+\bar t\) is scalar. Since two is invertible,
\(t\) is scalar and must be \(-1\), the only nonidentity scalar
involution modulo an odd prime power. For odd \(h\), the generated
subgroup has no involution. For \(q=2\), both signs require
\(s-r\equiv0\pmod3\). For \(q=2^e\) with \(e\ge2\), opposite signs
are impossible: an exponent giving \(-1\) would be a multiple of three
by reduction modulo two, whereas \(\alpha^3=8\phi+5\equiv1\pmod4\).
These rules and the two table rows give all later collisions in increasing
order of \(m=2s+y\).

Two bounds that require no choice of sign are
\[
 h\le H/8\quad\Longrightarrow\quad q\mid A_H(n)
 \quad\Longrightarrow\quad h\le H+2
 \qquad(q\mid R(n)).                                                     \tag{4}
\]
For sufficiency use \(y=x\) and \(s=r+kh\). If \(5\mid h\), take
\(k=1\). Otherwise one of \(k=1,2,3,4\) reaches the other permitted
residue in the same sign row. The distance is \(2kh\le8h\).
For necessity any collision satisfies \(h\mid 2(s-r)=d+x-y\).
For \(s>r\), this positive multiple of \(h\) is at most \(H+2\).
The only alternative is \(s=r,d=2,x=-1,y=1\). Then \(q\mid2\) and
\(h=3\le H+2\).

## 3. The first neighbor carrying the whole content [candidate-D]

For each input row the following construction gives one later index
with \(R(n)\mid R(m)\). Set \(s=kr\), \(y=x^k\) and \(m=2kr+y\).
The congruence \(\alpha^r=x\pmod{R(n)\mathcal O}\) gives the divisibility.
The permitted residues in Section 2 give the least \(k>1\) of this form.

| \(n\bmod5\) | \(x\) | \(r\bmod5\) | \(k\) | Distance \(m-n\) |
|---|---|---|---:|---:|
| 1 | \(+1\) | 0 | 2 | \(2r\) |
| 4 | \(+1\) | 4 | 5 | \(8r\) |
| 3 | \(-1\) | 2 | 2 | \(2r+2\) |
| 2 | \(-1\) | 4 | 3 | \(4r\) |

The table gives the **first** whole-content neighbor except at \(n=9\).
Indeed, for \(r\ge5\) and any proper divisor \(g\mid r\),
\[
 B(g,z)\le L_{\lfloor r/2\rfloor}<F_r\le R(n).
\]
Here \(L_a\) increases for \(a\ge1\), and
\(F_{2b}=F_bL_b>L_b\) for \(b\ge3\). This proves the strict inequality
for even \(r\ge6\) and, by increase of \(F_a\), for odd \(r\ge7\).
For \(r=5\) it is \(3<5\). Since also \(R(n)>2\), (2) and its
incompatible case show that full divisibility requires \(g=r\) and
\(y=x^{s/r}\). At \(r=2,4\) with \(x=-1\), the contents
\(L_2=3,L_4=7\) again exceed both two and every possible proper-divisor
content. The remaining case is \(n=9\), where \(r=4,x=1,R(n)=3\).
Here \(\alpha^2=3\phi+2\equiv-1\pmod3\). The next permitted \(s>4\)
with \(y=+,\ s\equiv0\pmod4\) is 20, and the next with
\(y=-,\ s\equiv2\pmod4\) is 14. The earlier of the two neighbors is
therefore \(m=27\), at distance 18.

Each table distance is at most \(4(n-1)\), including \(n=3\). Hence
\[
                         A_{4(n-1)}(n)=R(n)                              \tag{5}
\]
throughout the admitted domain. The next section proves the sharpness of
this bound even when the lcm may combine different neighbors.

## 4. The complete window profile on a power-of-three family [candidate-D]

Take \(K=4a+2\), \(a\ge0\), \(r=3^K\), and \(n=2r+1\). Then
\(r\equiv4\pmod5\), \(n\equiv4\pmod5\), and \(R(n)=L_r\) since
\(r\) is odd and \(x=1\). Define, for \(2\le j\le K\),
\[
 Q_j=L_{3^{j-1}}^2+3,\qquad
 D_j=2\cdot3^j c_j,\qquad
 1\le c_j\le4,\quad 3^j c_j\equiv1\pmod5 .
\]
For every integer \(H\ge0\), the exact answer is
\[
 A_H(n)=b(H)\prod_{\substack{2\le j\le K\\D_j\le H}}Q_j,
 \qquad
 b(H)=\begin{cases}
 1,&0\le H<4,\\
 2,&4\le H<12,\\
 4,&12\le H .
 \end{cases}                                                             \tag{6}
\]

**Factorization and orders.** For odd \(w\), the identity
\(L_{3w}=L_w(L_w^2+3)\) follows by cubing
\(L_w=\phi^w+\bar\phi^w\) and using \(\phi^w\bar\phi^w=-1\).
Starting from \(L_3=4\) gives \(R(n)=4\prod_{j=2}^K Q_j\).
At each step \(w=3^{j-1}\) is odd and divisible by three. Thus
\(L_w=B(w,+1)\) is even, since \(\alpha\) has order three modulo two.
It is prime to three, since \(\alpha^2=-1\pmod3\) gives order four.
In particular \(Q_j\) is odd and \(\gcd(Q_j,L_w)=1\).
For each prime power \(q\mid Q_j\), (1) now gives
\[
                   \alpha^{3w}=1,\qquad \alpha^w\ne1
                      \pmod{q\mathcal O}.
\]
As \(3w=3^j\) is a pure prime power, the order is exactly \(3^j\).
Applying this also to each prime separately proves that different \(Q_j\)
are pairwise coprime. Each \(Q_j>1\), so each supplies a prime absent
from the earlier factors.

**Gcd with any return content.** In fact, for every admitted \(m=2s+y\),
\[
 \gcd(Q_j,R(m))=
 \begin{cases}
 Q_j,& y=+1\ \text{and}\ 3^j\mid s,\\
 1,&\text{otherwise}.
 \end{cases}
\]
If any prime divisor of \(Q_j\) divides \(R(m)\), its odd order forces
\(y=+1\) and \(3^j\mid s\). Those conditions give \(\alpha^s=1\)
modulo every full prime power of \(Q_j\), because they all have that
same order. Thus every gcd with an individual member of the original
sequence returns either the whole block or one. This conclusion applies
whether \(Q_j\) is prime or composite.

**First appearances.** For a prime power of \(Q_j\), its odd order
precludes a negative sign. We need \(s>r\), \(s-r\) divisible by \(3^j\),
and \(s\equiv0,4\pmod5\). From \(r\equiv4\pmod5\), the least positive
increment is \(3^jc_j\): advancing by \(c_j\) steps reaches residue zero,
and returning to residue four would take five steps. The resulting distance
is \(D_j\). Every prime power in the same factor makes its first appearance
at that distance.

For the factor four, reduction modulo two allows both signs. A later
admitted neighbor with even content must have \(s\) a multiple of three.
The other sign at \(s=r\) gives an earlier index. The next such \(s\) is
\(r+3\equiv2\pmod5\), where \(y=-1\) gives distance four.
Modulo four, \(\alpha\) has order three, and \(-1\) is outside its
subgroup, by Section 2. The least later permitted multiple of three
with positive sign is \(s=r+6\equiv0\pmod5\), at distance twelve.
This accounts for the two separate appearances in \(b(H)\) and proves (6).

**Thresholds and size of the final jump.** In the order
\(j\equiv0,1,2,3\pmod4\), the inverses \(c_j\) are \(1,2,4,3\).
Thus the \(D_j\) are nondecreasing. Consecutive thresholds coincide exactly
when \(j\equiv3\pmod4\) and \(j+1\) is also in range, since then
\(c_j=3c_{j+1}\).

Write \(u=3^{K-1}\). The last threshold is \(D_K=8r=24u=4(n-1)\).
The preceding threshold is \(4u\): for \(K>2\) this is \(D_{K-1}\),
and for \(K=2\) it is the first appearance of four. Consequently
\[
 \begin{split}
 A_H(n)&=L_u &&(4u\le H<24u),\\
 A_{24u}(n)&=L_{3u}=L_u(L_u^2+3).
 \end{split}                                                             \tag{7}
\]
For **every** \(0\le H<24u\), (6) gives \(A_H(n)\mid L_u\), so
\(A_H(n)^3\le L_u^3<R(n)\). All primes of the missing factor
\(L_u^2+3\) first appear at the last threshold. This proves (5) sharp
along infinitely many indices even for the prime support. It also attains
the sufficient bound of \(8h\) steps in (4), with \(h=3^K\) unbounded.

**Sublinear windows on this family.** Let \(H(n)\ge0\) be integer valued
and \(H(n)=o(n)\). Along \(n=2\cdot3^{4a+2}+1\), one has
\[
                  \frac{\log A_{H(n)}(n)}{\log R(n)}\longrightarrow0 .
                                                                            \tag{8}
\]
For \(H<12\) the numerator is bounded. For \(H\ge12\) the thresholds
already reached in (6) form an initial segment, so \(A_H(n)=L_{3^v}\),
where \(v\) is the largest visible block index, or one if no \(Q_j\) is
yet visible. In either case \(3^v\le H/2\). By Binet's formula
\(\log L_t=t\log\phi+O(1)\) for \(t\ge1\); the denominator is
\(r\log\phi+O(1)\), with \(r=(n-1)/2\). This proves (8) along the
stated sequence of integer inputs. No primality condition is used.
