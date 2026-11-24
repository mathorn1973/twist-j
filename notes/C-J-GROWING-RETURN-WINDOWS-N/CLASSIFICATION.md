# Exact growing-window widths and return partners

**NON-CANONICAL. No authority. Candidate-D, L1.**

Owner is A. M. Thorn, ChatGPT-Astra-Sol-20261124-Growing-Windows. The public
basis is `6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`, Public Canon v117.
The scope is recorded in [claim #2084](https://github.com/mathorn1973/twist-j/issues/2084).

An admitted index is an odd integer \(n>1\) with \(5\nmid n\). Write
\(x=\chi_5(n)\), \(r=(n-x)/2\), and \(\alpha=\phi^2\), with
\(\phi=j/J\), \(J=1+j^2\), and \(j=\zeta_5\). Content is the nonnegative
gcd of the integer coordinates in the basis \(1,j,j^2,j^3\) of
\(\mathcal O=\mathbb Z[j]\). For \(R(n)=\operatorname{cont}(J^n-1-(J-1)^n)\),
the signed-return identity gives
\[
B(k,e)=\operatorname{cont}(1-e\alpha^k),\qquad R(n)=B(r,x)
=\begin{cases}F_r,&n\equiv1\pmod4,\\ L_r,&n\equiv3\pmod4.\end{cases}
\]
Here \(F_0=0,F_1=1\) and \(L_0=2,L_1=1\). For an integer \(H\ge0\), let
\[
A_H(n)=\operatorname{lcm}_{\substack{0<d\le H\\n+d\text{ admitted}}}
\gcd(R(n),R(n+d)),\qquad
H_*(n)=\min\{H\ge0:A_H(n)=R(n)\},
\]
using \(1\) for the empty lcm. See [the companion proof](PROOF.md) for the
signed-return identity and the general window result.

For positive \(k\), Binet's identities also give \(B(k,e)=F_k\) when
\(e=(-1)^k\) and \(B(k,e)=L_k\) otherwise. In fact,
\(1-e\alpha^k=-e\phi^k(\phi^k-e(-1)^k\psi^k)\) with \(\psi=-\phi^{-1}\).
The factor outside the parentheses is a unit, and in the Fibonacci case
the parentheses give \(\sqrt5 F_k\). Multiplication by a unit preserves
content, and \(\sqrt5=2\phi-1\) is primitive in the given basis.

## 1. Exact width

**Theorem 1 [candidate-D].** For every admitted \(n\ge53\), the width is
given by the following table. Appendix A extends the table to every admitted
\(n>1\).

The condition \(r=3\cdot2^v\) means that such a nonnegative integer
\(v\) exists; its negation excludes all such powers.

| Condition | \(H_*(n)\) |
| --- | ---: |
| \(n\equiv1\pmod5\) | \(n-1\) |
| \(n\equiv2\pmod5\) | \(2(n+1)\) |
| \(n\equiv3\pmod5\) | \(n+3\) |
| \(n\equiv4\pmod5,\ n\equiv3\pmod4\) | \(4(n-1)\) |
| \(n\equiv4\pmod5,\ n\equiv1\pmod4,\ r=3\cdot2^v\) | \(4(n-1)\) |
| \(n\equiv4\pmod5,\ n\equiv1\pmod4,\ r\ne3\cdot2^v\) | \(5r-2\) |

The uniform bound is \(4(n-1)\), attained on every admitted
\(n\equiv19\pmod{20}\). In the final row and for \(n\ge53\), the first
single gap whose gcd equals \(R(n)\) is \(8r=4(n-1)\).

### Order witnesses

Set \(h(p)=\operatorname{ord}(\alpha\bmod p\mathcal O)\). If \(p\) is an odd
prime other than \(5\), the Fibonacci rank \(z(p)\), the least positive
\(k\) for which \(p\mid F_k\), is \(\operatorname{ord}(-\alpha\bmod p\mathcal O)\).
Indeed \(\psi=-\phi^{-1}\) and \(\phi/\psi=-\alpha\), so Binet's formula
gives the rank statement since \(\psi\) and \(\sqrt5\) are units modulo
\(p\mathcal O\). The quadratic algebra \(\mathbb F_p[\phi]\) is defined by
\(\phi^2-\phi-1=0\) and has cyclic norm-one group of order
\(p-\chi_5(p)\). In the split case
it consists of pairs \((a,a^{-1})\), and in the field case it is the
kernel of the field norm. Its unique involution is \(-1\). Multiplying
\(-\alpha\) by this involution gives
\[
h(p)=\begin{cases}
2z(p),&z(p)\text{ odd},\\
z(p)/2,&z(p)\equiv2\pmod4,\\
z(p),&4\mid z(p).
\end{cases}
\tag{1}
\]
For even \(z=z(p)\), write \(\alpha=(-\alpha)^{1+z/2}\). The gcd of
\(1+z/2\) and \(z\) is two when \(z/2\) is odd and one when it is even.
For odd \(z\), \(-1\) has order two and lies outside
\(\langle-\alpha\rangle\). For the classical rank and Lucas divisibility
relations see [Morgan Ward, *The prime divisors of Fibonacci numbers*](https://msp.org/pjm/1961/11-1/pjm-v11-n1-p31-s.pdf).

Carmichael's theorem gives a primitive prime divisor of \(F_k\) for
each positive \(k\) other than \(1,2,6,12\). Here primitive means
\(p\mid F_k\) and \(p\nmid F_i\) for \(0<i<k\), so \(z(p)=k\) by
definition. For \(k>12\) the prime exceeds five, since the ranks of
\(2,3,5\) are \(3,4,5\). This is the Fibonacci specialization proved in
[Yabuta, Theorem 3](https://www.fq.math.ca/Scanned/39-5/yabuta.pdf), with
the original result in [Carmichael, Theorem XXIII, pp. 61–62](https://doi.org/10.2307/1967798).

For \(x=-1\) the Fibonacci branch has odd \(r\), so choose \(k=r\) in
Carmichael's theorem. The Lucas branch has even \(r\), so choose \(k=2r\).
A prime of rank \(2r\) divides \(L_r\) by \(F_{2r}=F_rL_r\) and the
definition of rank. Both choices give a prime dividing \(R(n)\) with
\(h(p)=2r\). For \(x=+1\) the Lucas branch has odd \(r\). Choosing \(k=2r\)
gives \(h(p)=r\), which is odd. For \(x=+1\) the Fibonacci branch has even
\(r\). Choose \(k=r\) when \(4\mid r\) and \(k=r/2\) when
\(r\equiv2\pmod4\). In the latter case \(F_{r/2}\mid F_r\). Both give
\(h(p)=r\). All these indices satisfy \(k>12\) for \(n\ge53\).

### The first four rows

Write a later admitted index as \(m=2s+y\) with \(y=\chi_5(m)\). A
divisor \(q\) of \(R(n)\) also divides \(R(m)\) exactly when
\(\alpha^s=y\pmod{q\mathcal O}\). In particular, when \(p\) is an odd prime
with the order just established, a necessary gap for the same sign is a
positive multiple of \(2h(p)\). A gap for the opposite sign requires
\(\alpha^{s-r}=-1\), hence even \(h(p)\) and
\(d=m-n\equiv h(p)-2x\pmod{2h(p)}\).

For \(x=-1\), the order \(2r\) gives candidates \(s\equiv r\pmod{2r}\)
for \(y=-1\) and \(s\equiv0\pmod{2r}\) for \(y=+1\). At each candidate
with the stated character, the full congruence
\(\alpha^r=-1\pmod{R(n)\mathcal O}\) gives \(R(n)\mid R(m)\). If
\(n\equiv3\pmod5\), then \(r\equiv2\pmod5\), and the first candidate is
\(m=4r+1\equiv4\pmod5\), with gap \(2r+2=n+3\). If
\(n\equiv2\pmod5\), then \(r\equiv4\pmod5\), and \(4r+1\equiv2\pmod5\)
has character \(-1\). The next candidate is \(6r-1\equiv3\pmod5\), with
the required character \(-1\) and gap \(4r=2(n+1)\). The prime of order
\(2r\) is absent from the entire window before these respective gaps.

For \(x=+1\), the full congruence \(\alpha^r=1\pmod{R(n)\mathcal O}\) gives
a single full return at any later same-sign index \(m=2(1+k)r+1\) with
\(k>0\). If \(n\equiv1\pmod5\), then \(r\equiv0\pmod5\), and \(k=1\)
works. The prime of order \(r\) forces \(d\ge2r\), since any opposite-sign
candidate \(m=(2k+3)r-1\), \(k\ge0\), has character \(+1\). If
\(n\equiv4\pmod5\), then \(r\equiv4\pmod5\), and \(k=1,2,3,4\) yield
residues \(2,0,3,1\) for \(m\) modulo five. Thus the first compatible
same-sign gap is \(8r\). On the Lucas branch \(r\) is odd, so the prime of
order \(r\) can recur only at a same-sign gap. This proves equality at
\(8r\) in the fourth row.

### The final two rows

Assume \(n\equiv9\pmod{20}\). Then \(x=+1\), \(r\equiv4\pmod5\), \(r\) is
even and \(R(n)=F_r\). Put \(u=r/2\). The prime with \(h(p)=r\) has
opposite-sign candidates \(m=(2k+3)r-1\), \(k\ge0\). The first three
residues modulo five are \(1,4,2\), so the first compatible opposite-sign
gap is \(5r-2\). Its first compatible same-sign gap is \(8r\). The odd part
of \(R(n)\) therefore requires a width of at least \(5r-2\).

The gaps \(3r\) and \(5r-2\) have destination indices \(5r+1\) and
\(7r-1\), with characters \(+1\) and \(-1\). Their exact gcds are
\[
\gcd(R(n),R(n+3r))=B(u,+1),\qquad
\gcd(R(n),R(n+5r-2))=B(u,-1).
\tag{2}
\]
To verify this for every integer modulus \(q\), put
\(\gamma=\alpha^u\pmod{q\mathcal O}\). In both gcds the start condition
is \(\gamma^2=1\). The partner conditions are \(\gamma^5=1\) and
\(\gamma^7=-1\), respectively, and under the start condition these reduce
to \(\gamma=1\) and \(\gamma=-1\). Thus the common divisors are exactly
the divisors of the respective contents in (2). The two contents are
\(F_u,L_u\) in a parity-dependent order, so their product is \(F_r\).
Their gcd divides two by subtracting \(1-\alpha^u\) and \(1+\alpha^u\).
It follows that the lcm in (2) recovers the full odd part of \(F_r\).

For the factor at two, \(\alpha\) has order three modulo \(2\mathcal O\) and
\(\alpha^3=8\phi+5=1+4(2\phi+1)\). If \(3\nmid k\), both contents
\(B(k,\pm1)\) are odd. If \(3\mid k\), then \(\alpha^k\equiv1\pmod{4\mathcal O}\),
so \(v_2(B(k,-1))=1\). For positive \(k\) divisible by three,
\[
v_2(B(k,+1))=2+v_2(k).
\tag{3}
\]
Indeed an odd power of \(1+2^b c\) with \(b\ge2\) and
\(c\notin2\mathcal O\) preserves the valuation of its difference from
one. Squaring raises it by one, since
\((1+2^b c)^2-1=2^{b+1}c(1+2^{b-1}c)\) and the final factor is one
modulo two. Apply this to \(\alpha^3\), whose difference from one has
valuation two.

When \(3\mid r\), set \(a=v_2(F_r)=2+v_2(r)\) and write \(r=2^v b\) with
\(b\) odd. Equation (3) gives order \(h_a=3\cdot2^v\) for \(\alpha\) modulo
\(2^a\mathcal O\). Every partner returning \(2^a\) has character \(+1\)
and gap a positive multiple of \(2h_a\). If \(b=3\), then \(h_a=r\) and
the first such gap is \(8r\). Otherwise \(b\ge9\) and \(h_a\le r/3\).
If \(5\mid h_a\), the gap \(2h_a\) preserves the start residue. If
\(5\nmid h_a\), the next four residues at gaps \(2kh_a\), \(1\le k\le4\),
contain the other positive-character residue. Hence \(2^a\) recurs by
\(8h_a\le8r/3\le5r-2\). If \(3\nmid r\), \(F_r\) is odd. This proves
both remaining rows.

For \(n\ge53\), \(B(u,+1)>2\). Any opposite-sign partner containing the
order-\(r\) prime must satisfy \(s\equiv u\pmod r\), at which
\(\alpha^s=1\pmod{B(u,+1)\mathcal O}\). It therefore fails to return the
full content. The first same-sign partner of this prime occurs at \(8r\)
and returns all of \(F_r\), proving the single-gap statement.

## 2. Minimum number of partners

**Theorem 2 [candidate-D].** Suppose \(n\ge53\), \(n\equiv9\pmod{20}\)
and \(r\ne3\cdot2^v\). For \(5r-2\le H<8r\), the smallest subset of
admitted partners \(n+d\), \(0<d\le H\), whose gcds with \(R(n)\) have
lcm \(R(n)\), has size two when \(3\nmid r\) and three when \(3\mid r\).
At \(H=8r\) the minimum is one.

If \(3\nmid r\), (2) gives two partners. The single-gap statement of
Theorem 1 gives the lower bound. If \(3\mid r\), (2) gives the odd part
and the proof of Theorem 1 supplies an additional partner returning
\(2^a\) by \(5r-2\). To prove that three are necessary, take the prime
\(p\) of order \(r\) and a prime \(p'\) of order \(u=r/2\) dividing
\(B(u,+1)\). For \(p'\) use Carmichael at \(2u\) if \(u\) is odd, at
\(u/2\) if \(u\equiv2\pmod4\), and at \(u\) if \(4\mid u\). These
choices have the prescribed order by (1). The indices \(2u\) and \(u\)
exceed twelve. If \(u\equiv2\pmod4\), then \(u/2\) is odd and divisible
by three. Since \(u\ge13\), \(u/2\ge9\), so this index is outside the
Fibonacci exceptions and its primitive prime exceeds five.

Any partner returning \(p\) with \(d<8r\) has character \(-1\) and
\(s\equiv u\pmod r\). Thus it cannot return \(2^a\), and it cannot
return \(p'\), which has \(\alpha^s=1\pmod{p'\mathcal O}\). A partner
returning \(2^a\) and \(p'\) together must have character \(+1\), with
gap a multiple of \(2\operatorname{lcm}(h_a,u)=2r\). Here the lcm
identity follows from \(h_a=3\cdot2^v\), \(u=2^{v-1}b\), and \(3\mid b\).
The first compatible such gap is \(8r\). Hence before \(8r\) the three
requirements need three distinct partners. At \(8r\), the single
same-sign partner returns \(R(n)\).

For the paper example \(n=69\), \(r=34\) and \(u=17\). Equation (2)
gives \(L_{17}\) at gap \(102\) and \(F_{17}\) at gap \(168\). Their gcd
is one since \(3\nmid r\), and their lcm is \(F_{34}\). The first
single full return is at gap \(272\).

## Appendix A. Small witness indices

**Corollary [candidate-D].** The table in Theorem 1 holds for all admitted
\(n>1\). Its proof uses an order witness for each start. The residue
conditions \(r\equiv0,4\pmod5\) for \(x=+1\) and
\(r\equiv2,4\pmod5\) for \(x=-1\), together with the branch parity, imply
that only \(n=3,9,21\) use a chosen rank in
\(\{1,2,3,4,5,6,12\}\). For these starts and five nearby starts the
following are explicit paper witnesses.

| \(n\) | \(p\) | \(h(p)\) | Witness in the Fibonacci sequence |
| ---: | ---: | ---: | --- |
| 3 | 3 | 4 | \(z(3)=4\), from \(F_4=3\) |
| 7 | 7 | 8 | \(z(7)=8\), from \(F_8=21\) |
| 9 | 3 | 4 | \(z(3)=4\), from \(F_4=3\) |
| 11 | 11 | 5 | \(z(11)=10\), from \(F_{10}=55\) |
| 13 | 13 | 14 | \(z(13)=7\), from \(F_7=13\) |
| 17 | 17 | 18 | \(z(17)=9\), from \(F_9=34\) |
| 21 | 5 | 10 | \(5\mid F_{10}=55\) |
| 29 | 13 | 14 | \(z(13)=7\), and \(F_7\mid F_{14}\) |

The displayed rank equalities follow by excluding proper divisors of the
listed indices, using \(F_1=F_2=1\), \(F_3=2\), \(F_4=3\) and \(F_5=5\).
Equation (1) applies to the witnesses other than five. For five,
\(\alpha^5=55\phi+34\equiv-1\pmod{5\mathcal O}\), while
\(\alpha^2=3\phi+2\not\equiv1\pmod{5\mathcal O}\). Thus its order is ten.
At every other start the chosen Fibonacci index has a primitive prime
divisor by Carmichael and its rank excludes \(2,3,5\). Substituting these
orders into the same gap arguments proves the width table. The minimum
partner theorem retains its stated bound \(n\ge53\).
