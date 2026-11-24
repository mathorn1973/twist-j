# Signed numerator bounds for the centered long spectrum

**NON-CANONICAL. No authority. Candidate-D, unconditional paper deductions.**
Candidate C-RH-THREE-INTERFACE-SYNTHESIS-N, owner [#2091](https://github.com/mathorn1973/twist-j/issues/2091), draft [#2093](https://github.com/mathorn1973/twist-j/pull/2093). Action layer NOT_APPLICABLE. The outstanding one-sided estimate has status O. No scientific executable or numerical experiment was run.

Use the dyadic \(X\), \(A=\lceil\sqrt{3X}\rceil\), balanced coefficients
\(c\), \(b=c*c\), \(h_X=\sum c_a/a\), \(D,D_1,H,J\) and primitive
frequencies from [PRIME-CANCELLATION.md](PRIME-CANCELLATION.md), §§2–4.
Write \(e(t)=\exp(2\pi i t)\), \(m_H(\theta)=H^{-1}\sum_{0\le j<H}e(j\theta)\).
Use signed representatives \(0<|a|/q<1/H\), and define the height
\(\lambda(a/q)=X|a|/q\). Put
\[
 C_q=-q\sum_{D<d\le 4A^2,\ q\mid d} b_d/d,\qquad
 z_{a/q}=\frac{C_q m_H(a/q)^J}{q(1-e(-a/q))},\qquad
 L_X(n)=(n+1/2+J(H-1)/2)h_X^2 .
\]
Thus \(T_{\rm low}(n)=G_X(n)-L_X(n)\) on the slab, where
\(G_X(n)=\sum_\theta z_\theta e(n\theta)\). All sums keep the actual \(C_q\).
In particular no coprimality within the cofactor sum is imposed.
The bound \(|b_d|\le\tau(d)\) gives \(|C_q|\ll_\epsilon X^\epsilon\)
uniformly, by the divisor bound and a harmonic sum. For all these modes
\(|z_{a/q}|\ll_\epsilon X^\epsilon/|a|\). Constants indexed by \(\epsilon\)
below are uniform in height intervals.

## 1. Summation in the signed numerators

For a single dyadic box \(R<q\le 2R,\ B\le |a|<2B\), with one sign
of \(a\), allow an additional interval restriction in \(q\) and any
single interval in height. The contribution of the box satisfies
\[
 \left|\sum_{\theta \text{ in box}} z_\theta e(n\theta)\right|
 \ll_\epsilon X^\epsilon R/B,\qquad 7X/8\le n\le17X/8.             \tag{1}
\]
This adapts the geometric resonance argument of
[#2087, round 5](https://github.com/mathorn1973/twist-j/blob/f55cbcd1bf0eff6de99449c37ac8c03916b8acfe/notes/C-RH-ARITHMETIC-KERNEL-N/round5/NUMERATOR-ESTIMATE.md).
The present proof uses the signed sawtooth factor and an exact convex
average in place of their character and triangle multiplier.

First omit the multiplier, allowing any integer time \(t\) between
\(X/2\) and \(3X\). For fixed \(q\) the permitted positive magnitudes
lie in a single interval. The factor \(1/[q(1-e(\mp a/q))]\) has
supremum plus total variation \(O(1/B)\) on that interval, by the
bounds \(O(1/a)\) and \(O(1/a^2)\) for its magnitude and derivative.
For primitivity expand \(1_{(a,q)=1}=\sum_{d\mid(a,q)}\mu(d)\),
and put \(q=dv,\ |a|=dj\). Partial summation in \(j\) bounds the
geometric sum, including both endpoints, by
\[
 \ll \frac1B\min\!\left(C B/d,\frac1{2\|t/v\|}\right),
 \qquad d<2B,\quad V<v\le 2V,\quad V=R/d ,
\]
where the second entry is infinite at resonance. This is applied before
taking absolute values in \(q\). Indeed \(C_q\) is independent of \(j\).

Let \(\ell=\operatorname{dist}(t,v\mathbb Z)\). If \(\ell=0\), at most
\(\tau(t)\) values of \(v\) occur, at cost \(O(B/d)\) each before
the \(1/B\) factor. If a chosen nearest multiple of \(v\) is zero,
\(\ell=t\) and each term costs \(O(V/t)=O(1)\). All such terms cost
\(O(V+1)\). In the remaining cases \(v\) divides one of the positive
integers \(t\pm\ell\ll X\) and \(1\le\ell\le V\). Thus for each
\(\ell\) there are \(O_\epsilon(X^\epsilon)\) values of \(v\),
and the geometric bound before \(1/B\) is \(O(V/\ell)\) for each.
In every nonempty box \(B<2R/H\), so \(V=R/d>H/4\).
The total before \(1/B\), for fixed \(d\), is
\(O_\epsilon(X^\epsilon(V\log(2X)+B/d))\).
Summing over \(d<2B\), then absorbing the harmonic and divisor losses,
proves \(O_\epsilon(X^\epsilon R/B)\) without the multiplier.

Restoring \(m_H^J\) takes a convex combination of these exact box sums at
\(t=n+j_1+\cdots+j_J\). Every such time is between \(X/2\) and \(3X\)
for large \(X\). The height and all other masks stay frozen. This proves
(1). Adding both signs and all boxes yields, for any height interval
\(E\subset[U,\infty)\),
\[
 \sup_{7X/8\le n\le17X/8}
 \left|\sum_{\lambda(\theta)\in E} z_\theta e(n\theta)\right|
 \ll_\epsilon X^{1+\epsilon}/U .                               \tag{2}
\]
Here \(R/B\le 2X/U\) in every occupied box. The estimate uses genuine
numerator cancellation even if there is no cancellation between
different \(C_q\).

## 2. Signed crossing pairs in finite time

Use the rational time taper from
[#2087, round 4](https://github.com/mathorn1973/twist-j/blob/f55cbcd1bf0eff6de99449c37ac8c03916b8acfe/notes/C-RH-ARITHMETIC-KERNEL-N/round4/FINITE-TAPER.md).
Explicitly, let \(k=\lceil3\log_2 X\rceil\), \(s=\lfloor X/(16k)\rfloor\),
\(p(j)=1_{|j|\le s}/(2s+1)\), and
\[
 w=1_{[X-ks,\,2X-1+ks]\cap\mathbb Z}*p^{*k},\qquad
 \mathcal J(y)=\sum_n w(n)e(ny).
\]
Here convolution is additive. The taper lies in \([0,1]\), equals one
on the original slab and is supported in \([7X/8,17X/8]\).
Its support and every translate used by the forward averages lie inside
the centered identity's validity range \([2A,3X]\). This taper is used
for the signed quadratic estimates below. The one-sided comparison in
§3 uses the original window weights directly.

For \(\|y\|\ge64k/X\), each normalized geometric factor from \(p\) has
modulus at most \(1/8\) for large \(X\), since
\(s\ge X/(32k)\). Hence \(|\mathcal J(y)|\le2X\cdot8^{-k}\le2X^{-8}\).
The total absolute coefficient mass is \(O_\epsilon(X^{1+\epsilon})\),
by the bound \(O_\epsilon(X^\epsilon/|a|)\). In all pair restrictions
below the distant part therefore has negligible absolute sum.
The remaining unequal-denominator pairs are exactly those in
\[
 0<|a q'-a' q|\le 64 k q q'/X.                                 \tag{3}
\]
In fact the signed representatives have distance \(<2/H<1/2\), and
zero determinant for primitive frequencies implies equal denominators
and equal signed numerators.

For \(U\ge128k\) the actual ordered unequal-denominator sum inside (3)
with \(\max(\lambda(\theta),\lambda(\theta'))\ge U\) satisfies
\[
 \left|\sum z_\theta\overline{z_{\theta'}}\mathcal J(\theta-\theta')\right|
 \ll_\epsilon X^\epsilon(X^3/U^2+X^2).                          \tag{4}
\]
Inside (3) the two absolute heights differ by at most \(64k\), so both
are at least \(U/2\). Write \(E_1=[U,\infty)\) and \(E_0=[U/2,U)\).
The pairs in question belong to the three disjoint rectangles
\(E_1\times E_1,\ E_1\times E_0,\ E_0\times E_1\).
On each rectangle the absolute value of the unrestricted signed tapered
product is \(O_\epsilon(X^{3+\epsilon}/U^2)\) by (2).
Remove distant pairs and the same-denominator terms. For the latter,
apply Cauchy–Schwarz over \((q,n)\) with weight \(w\). At a fixed
\(q\) the frequencies have spacing \(1/q\), so the separated-frequency
bound of [PRIME-CANCELLATION.md](PRIME-CANCELLATION.md), §3, costs
\(O(X+q)\sum_{\theta \text{ of } q}|z_\theta|^2\). Summing over \(q\)
costs \(O_\epsilon(X^{2+\epsilon})\) because \(q=O(X)\) and
\(\sum_\theta|z_\theta|^2\ll_\epsilon X^{1+\epsilon}\).
The distant and same-denominator removals can be taken disjointly,
since the distant portion of any subfamily has negligible absolute
sum. This proves (4), including crossing terms.

Here the large-gcd pruning of the neighboring taper argument also
applies without an assumption on the support of \(C_q\). In denominator
shells \(R<q\le2R,\ S<q'\le2S\), fix signed \(a,a'\), and let
\(g=(q,q')\), \(\ell=(|a|,|a'|)\), \(L=\min(R/|a|,S/|a'|)\) and
\(G_0=\max(1,RSL/X^2)\). The absolute sum of all ordered pairs of (3)
with \(g\ge G_0\) is \(O_\epsilon(X^{2+\epsilon})\), uniformly under
additional restrictions on the pairs. To see this, write \(q=gu\),
\(q'=gv\), \(a=\ell a_0\), \(a'=\ell a'_0\). There are
\(O(kRS/(Xg\ell))\) possible nonzero integers \(a_0v-a'_0u\).
For each, the integral solutions lie on a progression of step
\((a_0,a'_0)\) in \((u,v)\), with at most \(1+\ell L/g\) terms in the
shells. Multiply the counts by
\(O_\epsilon(X^{1+\epsilon}/|aa'|)\), using \(|\mathcal J|\le2X\).
Summing over \(g\ge G_0\) yields
\[
 \ll_\epsilon \frac{k X^\epsilon RS}{|aa'|}
               \left(\frac{\log(2X)}{\ell}+\frac{L}{G_0}\right).
\]
Since \(RS\ll X^2\) and \(RSL/G_0\le X^2\), harmonic summation over
the possible numerators and denominator shells proves the stated bound.
In particular (4) holds also with the extra restriction \(g<G_0\).

## 3. The surviving one-sided target

Choose \(U_X=\sqrt X/(\log X)^2\). It exceeds \(128k\) eventually.
Equation (4) removes the high and crossing pairs from the tapered
two-sided quadratic form with an error \(O_\epsilon(X^{2+\epsilon})\).
Equation (2) also bounds the discarded high amplitude pointwise by
\(O_\epsilon(X^{1/2+\epsilon})\), after shrinking the input exponent.
For a fixed threshold \(U=X^\delta\) with \(0<\delta<1/2\), (4) instead
costs \(O_\epsilon(X^{3-2\delta+\epsilon}+X^{2+\epsilon})\).
This does not give the \(X^{2+\epsilon}\) error throughout that
polynomial height range.

There is a separate estimate within each dyadic box of §1, applied
to its two signs or to any restriction of its modes. Its squared
coefficient mass is at most \(O_\epsilon(X^\epsilon R/B)\).
Primitive spacing is \(\gg R^{-2}\), so its squared norm on the
taper support is \(O_\epsilon(X^\epsilon(X+R^2)R/B)\).
Delete the boxes with \(B\ge\max(1,R^3/X^2)\). Each costs
\(O_\epsilon(X^{2+\epsilon})\) in squared norm. The \(X\)-term uses
\(R\ll X,\ B\ge1\), and the \(R^2\)-term uses \(R^3/B\le X^2\).
The square-root norm triangle inequality over logarithmically many boxes
estimates their joint error, including if these boxes are restricted to
\(\lambda<U_X\). This argument makes no assertion about the signed
quadratic mixed sum between the deleted boxes and the remaining boxes.

Let \(G_X^*(n)\) retain exactly the original modes in the boxes
\(B<\max(1,R^3/X^2)\) and with \(\lambda<U_X\), and put
\(F(n)=G_X^*(n)-L_X(n)\) on \(X\le n<2X\). Take the shells
\(R<q\le2R\) for powers of two \(R\), and \(B\le |a|<2B\) for powers of
two \(B\ge1\). Both restrictions preserve conjugate symmetry. The
remaining heights satisfy \(X/(2R)\le\lambda<\min(U_X,2R^2/X)\)
on each occupied remaining shell. The lower bound follows from
\(|a|\ge1\) and \(q\le2R\). The upper bound follows from \(q>R\)
and \(|a|<2B<2R^3/X^2\), since an occupied remaining shell has
\(R^3/X^2>1\). The upper bound on height alone does not define the mask.

For \(Q_V(Y)=\sum_{Y\le n<Y^{3/2}}(V(n)_+)^2/[n(n+1)]\), on every
sufficiently late full integer window the positive-part Lipschitz
inequality gives
\[
 \big|\sqrt{Q_F(Y)}-\sqrt{Q_{T_{\rm low}}(Y)}\big|
 \ll_\epsilon Y^\epsilon
 \qquad(\epsilon>0).                                           \tag{5}
\]
Indeed on each intersecting slab the squared unweighted norm of the
discarded amplitude is \(O_\epsilon(X^{2+\epsilon})\), by (2) for the
high cut and the separated-frequency estimate for the other boxes.
Multiply by \(X^{-2}\) and sum over at most \(O(\log Y)\) intersecting
slabs, where \(Y/2\le X<Y^{3/2}\), shrinking the input exponent.
The same bound compares \(F\) to the original \(R_{1/36}\) by the
inherited logarithmic error. The drift remains in both sequences in
(5). In particular the signed mixed terms with the drift need no
separate estimate for this square-root comparison.

**O.** The unproved inequality can now be written
\[
 \forall r\ge1\ \forall Y_0\ \exists Y\in\mathbb Z,\quad
 Y\ge\max(11,Y_0),\qquad
 \left(\sum_{Y\le n<Y^{3/2}}
 \frac{(G_X^*(n)-L_X(n))_+^2}{n(n+1)}\right)^r\le Y,
 \quad X\le n<2X.                                             \tag{6}
\]
Here \(X\) in each summand is the unique dyadic lower endpoint for
that \(n\). This has exactly the original quantifiers. To transfer
either direction of the equivalence, invoke the known side's
quantifiers with \(2r\) and use (5) with \(\epsilon<1/(4r)\).
For all sufficiently large passing \(Y\), the target square-root
energy is at most \(Y^{1/(4r)}+O_\epsilon(Y^\epsilon)
\le Y^{1/(2r)}\). The estimates above leave low-height modes such as
\(|a|=1\) with \(q\) of order \(X\). They give no bound at (6) for
the remaining coupled amplitude and drift. The tapered squared
amplitude is a sufficient upper bound on each full slab after
normalization, since \(L_X\ge0\). The exact late-window condition
uses the one-sided expression in (6).
