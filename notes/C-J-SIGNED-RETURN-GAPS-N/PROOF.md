# Signed return contents: exact gcd and correlation laws

NON-CANONICAL. No authority. All new deductions candidate-D, L1.
Owner: A. M. Thorn, ChatGPT-Astra-Sol-20261124-Signed-Gaps.
Date: 2026-11-24. Claim: [#2082](https://github.com/mathorn1973/twist-j/issues/2082).
Basis: 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed, Public Canon v117.

The supplied note C-J-SIGNED-RETURN-GAPS-1 owns the proposed gap identity.
The individual-defect content formula is recorded in
[the pinned #2081 proof](https://github.com/mathorn1973/twist-j/blob/bddd14b4eb684f613db3ec51df56527eea2dd480/notes/C-J-TWO-PLACE-FROBENIUS-N/PROOF.md).
We give a self-contained paper audit and consequences. The signed gcd
argument uses classical Fibonacci/Lucas divisibility; no claim of
literature novelty is made for that machinery. No scientific code was run.

## 1. Rational content and the two signs

Let \(\mathcal O=\mathbb Z[j]\), \(j=\zeta_5\),
\(J=1+j^2\), \(\phi=-j^2-j^3\), so \(J\phi=j\).
Let \(\chi=\chi_5\) and

\[
\Delta(n)=J^n-1-j^{2n},\qquad R(n)=\operatorname{cont}(\Delta(n)).
\]

Content is the nonnegative gcd of the four integer coordinates in
\(1,j,j^2,j^3\). For every positive integer \(h\),

\[
h\mid\operatorname{cont}(a)\quad\Longleftrightarrow\quad a\in h\mathcal O.
\tag{1.1}
\]

Multiplication by a unit preserves content, since its integral matrix
and inverse are unimodular. Also
\(\sqrt5=-1-2j^2-2j^3\) is primitive. Thus
\(\operatorname{cont}(a\sqrt5)=|a|\) for rational integers \(a\),
including factors of five. No inversion of five is involved.

The domain throughout is odd \(n>1\) with \(5\nmid n\). Put
\(x=\chi(n)\), \(r=(n-x)/2\). The four unit classes modulo five give
\(1+j^{2n}=xj^n\phi^{-x}\), hence

\[
\Delta(n)=J^n A_n,\qquad A_n=1-x\phi^{2r}.
\tag{1.2}
\]

For every integer \(u\ge0\) and sign \(e\in\{1,-1\}\), Binet's
identities with \(\bar\phi=-\phi^{-1}\) give

\[
1-e\phi^{2u}=-e\phi^u
\begin{cases}
\sqrt5 F_u,&e=(-1)^u,\\
L_u,&e\ne(-1)^u.
\end{cases}
\tag{1.3}
\]

All displayed prefactors except the explicit \(\sqrt5\) are units.
Consequently the signed return content is

\[
B(u,e):=\operatorname{cont}(1-e\phi^{2u})=
\begin{cases}F_u,&e=(-1)^u,\\L_u,&e\ne(-1)^u.\end{cases}
\tag{1.4}
\]

For \(n=2r+x\), the first case occurs exactly when \(n\equiv1\pmod4\).
This recovers the single-defect formula \(R(n)=F_r\) or \(L_r\).

## 2. The supplied fixed-gap identity

Let \(m=n+d\) also be in the domain, with even \(d>0\). Put

\[
y=\chi(m),\quad s=(m-y)/2,\quad
t=s-r=(d+x-y)/2\ge0.
\]

The exact subtraction is

\[
A_m-xy\phi^{2t}A_n=1-xy\phi^{2t}.
\tag{2.1}
\]

For every rational positive integer \(h\), membership of both \(A_n,A_m\)
in \(h\mathcal O\) is therefore equivalent to membership of both
\(A_n,1-xy\phi^{2t}\). Equations (1.1)-(1.4) prove

\[
\boxed{\gcd(R(n),R(n+d))=\gcd(R(n),C(d;x,y)),}
\tag{2.2}
\]

where \(C=B(t,xy)\). This argument includes every prime power, including
two and five. It does not replace integer content by an ideal norm.

There is a useful simplification. For signs \(x,y\),
\((-1)^{(x-y)/2}=xy\). Hence

\[
\boxed{C(d;x,y)=
\begin{cases}F_t,&4\mid d,\\L_t,&d\equiv2\pmod4.\end{cases}}
\tag{2.3}
\]

The case \(t=0\) occurs only for \(d=2,x=-1,y=1\), and then
\(C=L_0=2\), not zero. The pair \((3,5)\) is outside the domain.

## 3. Closed signed strong-divisibility formula

This section allows any two domain indices \(n,m\), in either order.
Keep \(x,y,r,s\) as above and put

\[
g=\gcd(r,s),\qquad a=r/g,\quad b=s/g.
\]

**Theorem 3.1 [candidate-D].** If \(x^b=y^a\), there is a unique
sign \(z\) with \(z^a=x,z^b=y\), and

\[
\boxed{\gcd(R(n),R(m))=B(g,z).}
\tag{3.1}
\]

If \(x^b\ne y^a\), then

\[
\boxed{\gcd(R(n),R(m))=
\begin{cases}2,&3\mid g,\\1,&3\nmid g.\end{cases}}
\tag{3.2}
\]

**Proof.** Write \(\alpha=\phi^2\). For every positive integer \(h\),
the common-divisor conditions are
\(\alpha^r=x,\alpha^s=y\) in \((\mathcal O/h\mathcal O)^\times\).
Choose integers \(u,v\) with \(ua+vb=1\).
Under the compatibility condition set \(z=x^u y^v\). Then
\(z^a=x^{ua}y^{va}=x^{ua+vb}=x\), and similarly \(z^b=y\).
Uniqueness follows since \(a,b\) are coprime and at least one is odd.
The two congruences imply
\(\alpha^g=(\alpha^r)^u(\alpha^s)^v=z\); conversely this congruence
implies both of them. Negative powers are allowed because \(\alpha\)
is a unit. Taking rational contents proves (3.1) for all \(h\).

If the signs conflict, raising the congruences to \(b,a\) gives
\(x^b=y^a\pmod{h\mathcal O}\). The integer difference is \(\pm2\),
so \(h\mid2\). Modulo two both signs are one and \(\phi^2\) has
order three: \(\phi^2=\phi+1\) and \(\phi^3=1\), with \(\phi\ne1\).
Thus two divides both contents exactly when three divides both indices,
equivalently \(3\mid g\). QED.

## 4. Finite support and full periodicity at every fixed gap

For \(d=2h>0\), a sufficient uniform multiple of all possible gcds is

\[
M_d=
\begin{cases}
\operatorname{lcm}(F_{h-1},F_h,F_{h+1}),&h\text{ even},\\
\operatorname{lcm}(L_{h-1},L_h,L_{h+1}),&h\text{ odd}.
\end{cases}
\tag{4.1}
\]

Every entry here is positive. Some sign pairs may be inadmissible, so
this is a sufficient bound, not necessarily the smallest one.

For a fixed window diameter \(H\), take the prime divisors \(E_H\) of
the lcm of \(M_d\) over positive even \(d\le H\). Removing **all powers**
of primes in \(E_H\) from each \(R(n)\) leaves pairwise coprime contents
for distinct admitted indices in any window of diameter \(H\). The
exceptional prime set depends on \(H\), not on the window position.

There is more than a bound on support. Let \(P\) be a period of the
Fibonacci pair modulo \(M_d\), which exists because its update matrix
has determinant \(-1\) and is invertible over the finite ring. The same
\(P\) is also a period of Lucas numbers since \(L_u=2F_{u+1}-F_u\);
their least periods need not be equal. Then

\[
T_d=\operatorname{lcm}(20,2P)
\tag{4.2}
\]

is a period of the entire gcd function on its admitted indices. On
the ambient indices \(n\ge2\), it is also a period of the function with
an unavailable symbol for parity or divisibility-by-five exclusions.
If the marker also includes the excluded initial input \(n=1\), this
statement gives an eventual period.
For \(M_d=1\) set \(P=1\). Indeed, shifting \(n\) by \(T_d\) preserves
its character, its branch modulo four, the gap factor \(C\), and shifts
the return index by a multiple of \(P\). Equation (2.2) finishes the proof.

Consequently every value has an exact rational natural density on
the admitted periodic domain. These are densities of arithmetic gcd
predicates, not densities conditioned on both inputs being prime.

Any fixed finite collection of such gap readings is jointly periodic.
It cannot be a sound unbounded primality recognizer. Every nonempty
residue class contains arbitrarily large composite integers: for a
positive representative \(a>1\), use \(a(1+kT)\); for the class one,
use \((1+T)(1+kT)\). Any output selected solely by the periodic profile
therefore also selects composites whenever it selects an infinite class.

## 5. Exact gap-two law and period

The admitted starts are odd \(n>1\) with \(5\nmid n(n+2)\), hence
\(n\bmod5\in\{1,2,4\}\).

- In class one, \((x,y)=(1,-1)\), \(t=2\), \(C=L_2=3\).
  Modulo three, \(\phi^4=3\phi+2=-1\), so \(\phi\) has order eight.
  Therefore \(3\mid R(n)\) exactly when \(n\equiv1\pmod8\).
- In class two, \((x,y)=(-1,1)\), \(t=0\), \(C=2\).
  Modulo two, \(\phi\) has order three, so \(2\mid R(n)\) exactly
  when \(3\mid n+1\).
- In class four, \((x,y)=(1,1)\), \(t=1\), \(C=L_1=1\).

Thus, on the full admitted domain,

\[
\boxed{G_2(n):=\gcd(R(n),R(n+2))=
\begin{cases}
3,&n\equiv1\pmod{40},\\
2,&n\equiv17\pmod{30},\\
1,&\text{otherwise}.
\end{cases}}
\tag{5.1}
\]

With an unavailable marker outside the domain, its least eventual
period is 120. Any period must preserve the singleton residue class
of output three modulo forty and that of output two modulo thirty,
so must be divisible by both; 120 works. Among the 36 admitted classes
modulo 120, the counts for outputs \(1,2,3\) are \(29,4,3\).

For joint units modulo thirty, only starts \(11,17,29\pmod{30}\)
remain. The first class has gcd three exactly at \(n\equiv41\pmod{120}\),
otherwise one. The second has gcd two; the third has gcd one. Counts
within this narrower domain are \(7,4,1\) out of twelve. No assertion
that these same fractions hold among actual prime twins is made.

## 6. Gap 182: reduction to L18 and all five values

For \(d=182\), the admitted residues \(n\bmod5\) are \(1,2,4\).
Their gap factors are respectively \(L_{92},L_{90},L_{91}\).
This section treats **only odd \(n\equiv2\pmod5\)**. Here

\[
x=-1,\quad y=1,\quad r=(n+1)/2\equiv4\pmod5,\quad s=r+90.
\]

**Theorem 6.1 [candidate-D].** On this domain,

\[
\boxed{\gcd(R(n),R(n+182))=\gcd(R(n),L_{18}),\quad
L_{18}=5778=2\cdot3^3\cdot107.}
\tag{6.1}
\]

**Direct proof, including every rational prime power.** If \(h\) divides
both original contents, then in \(\mathcal O/h\mathcal O\)
\(\phi^{2r}=-1\) and \(\phi^{180}=-1\). Put \(b=-\phi^{36}\).
Then \(b^5=1\) and \(b^{2r}=1\). Since \(5\nmid2r=n+1\), Bezout
gives \(b=1\), so \(\phi^{36}=-1\). As
\(1+\phi^{36}=\phi^{18}L_{18}\), equation (1.1) gives \(h\mid L_{18}\).
Conversely, \(h\mid R(n),L_{18}\) implies \(\phi^{2r}=-1\) and
\(\phi^{180}=-1\), hence \(\phi^{2s}=1\), so \(h\mid R(n+182)\).
This proves equality of rational gcds without factoring \(h\).

The value follows from \(L_9=76\) and
\(L_{18}=L_9^2+2=5778\). The factor 107 is prime, as the only primes
at most its square root are 2,3,5,7 and none divides it.

**Complete classification.** In Theorem 3.1,
\(g=\gcd(r,r+90)=\gcd(r,18)\), because \(5\nmid r\).
Compatibility is \((-1)^{(r+90)/g}=1\), which is equivalent to
\(r\equiv2\pmod4\): if \(r\) is odd the quotient is odd; if
\(4\mid r\), it is again odd; if \(r\equiv2\pmod4\), it is even.
In the compatible case \(z=-1\), \(g\) is even, and the answer is
\(L_g\), where \(g\in\{2,6,18\}\). Otherwise (3.2) applies.

| Condition on r=(n+1)/2 | Exact gcd | Relative density among odd n=2 mod5 |
| --- | ---: | ---: |
| r is not 2 mod4, 3 does not divide r | 1 | 1/2 |
| r is not 2 mod4, 3 divides r | 2 | 1/4 |
| r is 2 mod4, 3 does not divide r | 3 | 1/6 |
| r is 2 mod4, 3 divides r, 9 does not divide r | 18 | 1/18 |
| r is 2 mod4, 9 divides r | 5778 | 1/36 |

The density computation is finite residue arithmetic: \(r\equiv4\pmod5\)
runs uniformly through all 36 classes modulo 36. The five row counts
are \(18,9,6,2,1\), and CRT with five preserves their proportions.

The maximum occurs exactly when \(r\equiv18\pmod{36}\). Combining
\(n\equiv35\pmod{72}\) with \(n\equiv2\pmod5\) gives

\[
\boxed{G_{182}(n)=5778\quad\Longleftrightarrow\quad
n\equiv107\pmod{360}.}
\tag{6.2}
\]

It is attained at \((n,n+182)=(107,289)\), where \(289=17^2\).
On the prime-admissible subdomain \(n\equiv17\pmod{30}\), the only
values are \(2,18,5778\), with candidate-index proportions
\(3/4,1/6,1/12\). These are not proportions among prime pairs.

For actual prime pairs \(p,p+182\) in this channel, let \(z(p)\) be
the Fibonacci rank of apparition, not the order of J. The classical
return bounds give \(z(p)\mid p+1\), \(z(p+182)\mid p+181\).
Their gcd divides 180; since \(5\nmid p+1\), it divides 36.
This conditional prime-pair consequence is weaker than the all-index
content classification above.

## 7. What the exact correlations do and do not say

On the domain of Section 6, the full table gives

\[
27\mid G_{182}(n)\quad\Longleftrightarrow\quad
107\mid G_{182}(n)\quad\Longleftrightarrow\quad
n\equiv107\pmod{360}.
\tag{7.1}
\]

These two divisibility predicates are identical, despite referring to
different primes. Finite exceptional support does not imply independence.

The associated periodic mode is explicit. Extend the indicator of the
maximum by zero outside its channel, so
\(b(n)=\mathbf1_{n\equiv107\pmod{360}}\). For every positive integer
\(N\) and integer frequency \(k\), with
\(e_{360}(a)=\exp(2\pi i a/360)\),

\[
\sum_{n=1}^{360N}b(n)e_{360}(-kn)
=N e_{360}(-107k).
\tag{7.2}
\]

At nonzero frequencies modulo 360 the same holds after subtracting
the mean \(1/360\). These exact periodic resonances are not square-root
cancellation estimates. They concern an integer-index observable and
do not contradict the differently normalized prime-field Fourier
theorem discussed in SOURCES_REVIEW.md.

Finally, for every \(k\ge0\), take \(n=119+2310k\). Then
\(n\equiv29\pmod{30}\), so \(G_2(n)=1\), but \(7\mid n\) and
\(11\mid n+2\). Both inputs are composite. This whole progression
shows why coprimality of nearby return contents does not force prime
occurrence on the original input diagonal.
