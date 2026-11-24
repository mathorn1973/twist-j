# Time intervals for the signed arithmetic boundary

**NON-CANONICAL. Authority none. Action layer NOT_APPLICABLE.**
The identities and norm transfers are **candidate-D**. The complete
positive energy bound is **O**. This is a paper deduction under
[SCOPE.md](SCOPE.md).

## One coordinate and its two times of change

For a prime \(p\), write \(\nu_p(d)=\mu(d)\mathbf1_{p\nmid d}\).
Pair each \(p\)-free squarefree \(d\) with \(pd\). On integers \(N\ge1\),
\[
 M(N)=\sum_d\nu_p(d)\mathbf1_{[d,pd)}(N),\qquad
 M(N)-M(N-1)=\sum_d\nu_p(d)(\mathbf1_{N=d}-\mathbf1_{N=pd}).
\]
Here \(M(0)=0\). These are the retained sign and both endpoint signs,
respectively. The endpoints are exact since \(pd=N\) makes the two
vertices both retained. On an integer interval \([A,B)\), \(1\le A<B\),
equip the real functions with weights \(w(N)=1/[N(N+1)]\). For two
half-open integer intervals \(I=[d,pd)\), \(I'=[e,pe)\), put
\[
 {\cal G}_{[A,B)}(I,I')
    =\left(\frac1{\max(A,d,e)}-\frac1{\min(B,pd,pe)}\right)
       \mathbf1_{\max(A,d,e)<\min(B,pd,pe)} .
\]
This is their exact inner product by telescoping. For other
half-open intervals use the same formula with their own endpoints,
and allow \(+\infty\) as a right endpoint. Linear terms pairing signs
of the opposite type remain part of the full squared norm. The
restriction to positive energy uses a nonnegative dual test, as below.

## Unsimplified two-factor interval family

Use the prior arithmetic input
[FULL-COUPLED-ENERGY.md](https://github.com/mathorn1973/twist-j/blob/ceb77e3632ec4617c54d8e1fd504d3b1c99dd106/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N/FULL-COUPLED-ENERGY.md).
For fixed \(T\), pair in the first factor of
\(C_T(n)=\sum_{a,b>T}\mu(a)\mu(b)\lfloor n/(ab)\rfloor\).
For each \(p\)-free base \(a\), each \(b>T\) and each \(k\ge1\),
the signed interval contribution, apart from \(\mu(a)\mu(b)\), is
\[
 \begin{cases}
 \mathbf1_{[kab,kpab)}(n),& a>T,\\
 -\mathbf1_{[kpab,\infty)}(n),& T/p<a\le T,\\
 0,&a\le T/p .
 \end{cases}                                                   \tag{1}
\]
This is exactly the difference of the two product indicators
for \(a\) and \(pa\), with the cutoff in the first factor
imposed before taking the difference. The sum is finite on
every finite range of the argument. In particular the lower exit
continues past the time at which the upper exit of a retained
pair would end. Omitting it changes the carrier.

On a slab \(X\le N<2X\), use the given forward average \(U_H^J\).
Write \(\lambda_s\) for the probability that its total shift is \(s\),
\(0\le s\le J(H-1)\), and \(I-s=\{N:N+s\in I\}\).
For integer \(Y\) and each nonempty slab-window intersection, take
\(A_X=\max(X,Y)\), \(B_X=\min(2X,\lceil Y^{3/2}\rceil)\), and
\(\mathcal W=[A_X,B_X)\cap\mathbb Z\). These integer endpoints also
apply when \(Y^{3/2}\) is itself an integer. The Gram kernel of two
averaged interval functions is
\[
 {\cal G}^{\,U}_{\mathcal W}(I,I')
   =\sum_{s,t}\lambda_s\lambda_t{\cal G}_{\mathcal W}(I-s,I'-t).
                                                                \tag{2}
\]
Either shifted interval can start at a nonpositive integer. Formula
(2) only takes reciprocals at positive endpoints on nonempty
intersections, and an empty intersection contributes zero. Write a
slab's interval sum as \(\sum_\alpha c_\alpha\mathbf1_{I_\alpha}\),
with the signs in (1) included in \(c_\alpha\). For
\(Z_X=U_H^JC_T-L_X h_T^2\) its complete, two-sided squared norm
on the intersection is exactly
\[
 \sum_{\alpha,\beta}c_\alpha c_\beta
                 {\cal G}^{\,U}_{\mathcal W}(I_\alpha,I_\beta)
 -2h_T^2\sum_\alpha c_\alpha
      \langle U_H^J\mathbf1_{I_\alpha},L_X\rangle_{\mathcal W}
 +h_T^4\|L_X\|_{\mathcal W}^2 .                                \tag{3}
\]
In particular the upper-upper, lower-lower, and upper-lower terms
all occur, along with both affine terms. The nonnegative kernel
entries do not imply that the mixed Möbius contribution has one sign.

For the requested positive energy the exact formula is instead
\[
 \sqrt{Q_Z(Y)}
   =\sup_{\substack{f(N)\ge0\\\sum_{N\in I(Y)}w(N)f(N)^2\le1}}
    \sum_X\left[
      \sum_\alpha c_\alpha
         \sum_{s}\lambda_s\sum_{N\in\mathcal W_X\cap(I_\alpha-s)}
                                      w(N)f(N)
       -h_T^2\sum_{N\in\mathcal W_X}w(N)f(N)L_X(N)\right],
                                                                \tag{4}
\]
where \(\mathcal W_X=I(Y)\cap[X,2X)\) and \(I(Y)=[Y,Y^{3/2})\cap\mathbb Z\).
Weighted one-sided norm duality proves (4), and the normalized
positive part attains the supremum when it is nonzero. The entire
window uses one test and one norm constraint. The two outer slab
fragments are included.

## Absorbing both lower exits with the same Möbius sequence

Write \(\delta_q\) for the convolution atom at \(q\),
\(e_p=\delta_1-\delta_p\), and
\[
 u'_T=e_p*(\nu_p\mathbf1_{d\le T}),\qquad
 g_T=e_p*(\nu_p\mathbf1_{d>T}).
\]
Since \(\mu=e_p*\nu_p\), these satisfy \(\mu=u'_T+g_T\).
The region \(T/p<a\le T\) whose negative interval appears in (1)
is precisely the extra part \(u'_T-u_T=-\delta_p*
(\nu_p\mathbf1_{T/p<d\le T})\); here \(u_T=\mu\mathbf1_{d\le T}\).
In particular \(\sum_d u'_T(d)=0\) exactly and \(u'_T\) is supported
on \(d\le pT\). Its coefficients have absolute value at most one:
the \(p\)-free and exactly-once divisible terms have disjoint
support. No estimate for \(M(T)\) is used in the zero sum.

Because \(\mu*\mathbf1=\delta_1\), the exact coefficient identity is
\[
 \mu=2u'_T-u'_T*u'_T*\mathbf1+g_T*g_T*\mathbf1.
\]
Indeed, \((g_T-u'_T)*(g_T+u'_T)*\mathbf1=\mu-2u'_T\).
This absorbs the lower exits in both factors at once while keeping
the resulting square from the complete small part. Define
\[
 h_{p,T}=\left(1-\frac1p\right)
                   \sum_{\substack{a\le T\\p\nmid a}}\frac{\mu(a)}a,
 \qquad
 C_{p,T}(n)=\sum_{d\le n}(g_T*g_T*\mathbf1)(d).
\]
For every \(n\ge pT\), the centered floor identity now reads
\[
 M(n)= C_{p,T}(n)-(n+1/2)h_{p,T}^2
     + \sum_{d\le p^2T^2}(u'_T*u'_T)(d)\psi_d(n),               \tag{5}
\]
where \(\psi_d(n)=\{(n+1/2)/d\}-1/2\). There is no constant
intercept because \(\sum u'_T=0\); the quadratic affine term
remains nonpositive at positive \(n\). The identity is a reallocation
with an exact compensating square. It does not assert that the old
lower intervals have small energy separately.

The new interval combination can be written using \(b_0=kab\) as
\[
 C_{p,T}(n)=
 \sum_{\substack{a,b>T\\p\nmid ab}}\sum_{k\ge1}
   \mu(a)\mu(b)\bigl(
       \mathbf1_{[b_0,pb_0)}(n)-\mathbf1_{[pb_0,p^2b_0)}(n)\bigr).     \tag{6}
\]
Expansion gives thresholds at \(b_0,pb_0,p^2b_0\) with coefficients
\(1,-2,1\), because the two factors each contribute \(e_p\).
Equivalently one can replace the parenthesis by
\(\rho_p(k)\mathbf1_{[kab,\infty)}(n)\) under the complete \(k\)-sum,
where
\[
 \rho_p(k)=(e_p*e_p*\mathbf1)(k)=
 \begin{cases}1,&p\nmid k,\\-1,&p\mid k,\ p^2\nmid k,\\0,&p^2\mid k.\end{cases}
\]
Thus the two adjacent intervals of (6) retain opposite signs
and are supported on the actual product scales. One can substitute
them directly for the interval families in (2)–(4), replacing \(h_T\)
by \(h_{p,T}\). Alternatively the Gram for each pair of double
intervals is the sum of its two same-type kernels minus both
cross-type kernels.

Fix any prime \(p\) and \(T=\lfloor X^{1/4}\rfloor\).
For sufficiently late slabs all averaged arguments are at least
\(pT\), and the small rectangle in (5) has \(d\le p^2T^2\)
with coefficient bounded by \(\tau(d)\). The short raw-denominator
estimate used in the cited paper, with \(D_0=p^2T^2\), gives the
squared weighted slab error bound
\[
 \ll \frac{(X+D_0^2)D_0}{X^2}(1+\log X)^3
       \ll_p X^{-1/2}(1+\log X)^3 .
\]
It uses squared coefficient mass \(O(D_0(1+\log X)^3)\),
separation at least \(D_0^{-2}\), and convexity under the given
forward average. Consequently the carrier
\(Z_{p,X}=U_H^JC_{p,T}-L_X h_{p,T}^2\) differs from \(U_H^JM\)
by \(O_p(X^{-1/4}(1+\log X)^{3/2})\) in weighted slab norm.
Summed in square on the intersections with the same complete
window, this error is \(O_p(Y^{-1/4}(1+\log Y)^{3/2})\) in norm.
Using the inherited maximal short-sum comparison of \(U_H^JM\)
with \(M\) and the comparison of \(M\) with \(R_{1/36}\) gives
\[
 \|Z_p-R_{1/36}\|_{I(Y)}\ll_{p,K}(\log Y)^{-K}
\]
for every fixed \(K>0\) on sufficiently late complete windows.
This is stronger than a norm transfer with logarithmic loss and
uses no new bound for \(Z_p\) itself. The Lipschitz bound for the
positive part transfers square-root energy in both directions.
For a required exponent \(r\), use \(2r\) in the source bound
and absorb the norm error on arbitrarily late windows.

**O.** A sufficient signed bilinear estimate is to bound the
supremum in (4), with the interval pairs (6) and updated square,
by \(Y^\epsilon\) on arbitrarily late complete windows for each
fixed \(\epsilon>0\). This is equivalent to the target after adjusting
the exponent. A two-sided estimate using (3) would suffice as
well, with a squared-energy exponent adjusted accordingly.
The algebraic absorption and exact interval kernels use the
same Möbius function in both factors, but provide no growing-scale
cancellation estimate for its remaining interval-pair sums.
