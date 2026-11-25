# Unconditional logarithmic savings in the actual short-correlation error

C-RH-ARITHMETIC-KERNEL-N, round 5, #2087 / #2089. PUBLIC-source, NON-CANONICAL, no authority. Candidate-D on the stated unconditional analytic input. Paper proof following PREREG.md. No scientific computation or historical priority claim.

Write \(t(n)=(s*\chi_5)(n)=T(n)-T(n-1)\) as in the fixed candidate. We use \(t=\mu*v\), where \(v\) is the coefficient sequence of \(U^{-1}\), and the bounds already proved in round 4:
\[
 \sum_{d\le y}|v(d)|\ll \sqrt y,\qquad
 \sum_{d\le y}\frac{|v(d)|}{\sqrt d}\ll 1+\log y,\qquad
 \sum_{d>Z}\frac{|v(d)|}{d}\ll Z^{-1/2}.                    \tag{1}
\]
The first two are in CRITICAL-UNIT.md §2. The third follows from the first by partial summation or dyadic subdivision. No cancellation of the signs of \(v\) is assumed in the transfer.

## 1. Maximal short sums of the actual coefficient

For an integer \(h\ge1\) and any real start \(x\), let
\[
 {\cal W}_f(x,h)=
 \sup_{\alpha\in\mathbb R,\ P\subset(x,x+h]\cap\mathbb Z}
       \left|\sum_{m\in P}f(m){\rm e}(\alpha m)\right|,
 \qquad {\rm e}(u)=\exp(2\pi i u),
\]
where the finite set \(P\) ranges over arithmetic progressions, allowing empty sets and singletons. In the proof the same definition is used for real lengths. The intervals, progression moduli, and phases may all vary with the start.

**Theorem.** For every fixed \(0<\eta<1/3\) and \(A>0\), uniformly for integers \(X\) sufficiently large and integers \(X^{1/3+\eta}\le h\le X^{1-\eta}\),
\[
 \sum_{X\le n<2X}{\cal W}_t(n,h)^2
       \ll_{\eta,A}\frac{Xh^2}{(\log X)^A}.                    \tag{2}
\]

The external input is the unconditional Möbius statement of Theorem 1.1(i) of Matomäki, Radziwiłł, Shao, Tao and Teräväinen, *Higher uniformity of arithmetic functions in short intervals II*. Take a fixed filtered circle and its unit additive character, so polynomial sequences of degree one include all phases \({\rm e}(\alpha m)\). Their starred sum is the supremum over arithmetic progressions within the interval. The complexity and Lipschitz parameters for this choice are absolute. For any fixed \(B>0\) and \(\eta'>0\), if \(Y^{1/3+\eta'}\le l\le Y^{1-\eta'}\), the theorem gives
\[
 {\cal W}_\mu(x,l)\le l(\log Y)^{-B}
 \quad\text{outside a set of measure }O_{B,\eta'}(Y(\log Y)^{-B})
 \quad (Y\le x\le 2Y).
\]
The bound \({\cal W}_\mu(x,l)\le l+1\) also holds everywhere. In the stated range \(l\ge1\), so integrating squares gives, for every fixed \(A>0\),
\[
 \int_Y^{2Y}{\cal W}_\mu(x,l)^2\,dx
       \ll_{\eta',A} Yl^2(\log Y)^{-A}.                       \tag{3}
\]
Take \(B=A\), or any larger fixed value, in the source theorem. The integrated supremum in (3) already accounts for the exceptional starts and needs no separate exceptional set for phases or progression moduli.

For the coefficient comparison, fix an integer start \(n\) and a progression \(P\) in the definition of \({\cal W}_t(n,h)\). The intersection \(P\cap d\mathbb Z\), divided by \(d\), is empty or an integer arithmetic progression inside \((n/d,(n+h)/d]\). A phase \({\rm e}(\alpha m)\) becomes \({\rm e}(d\alpha q)\) on the quotient variable \(q\). Expanding \(t=\mu*v\) is finite since \(n+h<3X\). Taking suprema thus gives
\[
 {\cal W}_t(n,h)\le
    \sum_{d\le3X}|v(d)|\, {\cal W}_\mu(n/d,h/d).               \tag{4}
\]
Take the unnormalized \(\ell^2\) norm over \(X\le n<2X\) and use the triangle inequality. For a fixed logarithmic cutoff \(Z=\lfloor(\log X)^{A+2}\rfloor\), the range \(d\le Z\) is controlled by (3) with \(Y=X/d\), \(l=h/d\), and \(\eta'=\eta/2\) once \(X\) is sufficiently large. Indeed the logarithmic \(d\)-range leaves a fixed power margin at both ends. Since \(h\) and \(n\) are integers, the integer sets in \((x,x+h/d]\) are constant when \(x\) ranges over \([n/d,(n+1)/d)\). The progression and phase supremum is therefore constant there as well. This gives the exact conversion
\[
 \sum_{X\le n<2X}{\cal W}_\mu(n/d,h/d)^2
       = d\int_{X/d}^{2X/d}{\cal W}_\mu(x,h/d)^2\,dx
       \ll X(h/d)^2(\log X)^{-A}.                            \tag{5}
\]
Summing the norms with \(|v(d)|\) gives \(O_{\eta,A}(\sqrt X h(\log X)^{-A/2})\) by the absolute unit norm at one.

For \(Z<d\le h\) the interval of length \(h/d\) contains at most \(1+h/d\le2h/d\) integers, so its norm costs at most \(2\sqrt X h/d\). The last inequality in (1) makes this middle range \(O(\sqrt X h Z^{-1/2})\).

For \(h<d\le3X\) each quotient interval contains at most one integer. Its squared maximum is bounded by the indicator of a multiple of \(d\) in \((n,n+h]\). Each such multiple belongs to intervals from at most \(h\) integer starts. In the entire start block the possible multiples are \(O(X/d+1)=O(X/d)\), since \(d\le3X\). Thus the norm for this \(d\) is \(O(\sqrt{Xh/d})\). The critical unit estimate in (1) gives the far range the bound \(O(\sqrt{Xh}\log X)\). Compared with \(\sqrt X h\), this is \(O((\log X)/\sqrt h)\), smaller than every fixed inverse log on the stated \(h\)-range. Combining all three bounds and squaring proves (2). In particular the short lengths \(h/d<1\) cost an explicit sparse-multiple estimate, with no application of the Möbius theorem at such lengths.

An additional correlation readout is available without specifying any fixed shift. Let \(J_n=(n,n+h]\cap\mathbb Z\), and for an integer \(\ell\) set \(C_n(\ell)=\sum_{m,m+\ell\in J_n} t(m)t(m+\ell)\). Finite Fourier orthogonality gives
\[
 \sum_\ell |C_n(\ell)|^2
  =\int_0^1\left|\sum_{m\in J_n}t(m){\rm e}(\alpha m)\right|^4d\alpha
  \le {\cal W}_t(n,h)^2\sum_{m\in J_n}|t(m)|^2
  \le h\,{\cal W}_t(n,h)^2 .
\]
Consequently
\[
 \sum_{X\le n<2X}\sum_\ell |C_n(\ell)|^2
       \ll_{\eta,A} Xh^3(\log X)^{-A}.                       \tag{6}
\]
This is an average over both starts and shifts, with the whole short correlation sequence retained.

## 2. The signed error of the original rational triangular average

Use the exact round-4 notation
\[
 D_H(n)=\sum_j u_H(j)t(n+j),\qquad
 {\cal E}(X,H)=\sum_{n=X}^{2X-1}|D_H(n)|^2 .
\]
Here \(u_H\) has support in \([2-H,H-1]\), total variation at most two, and zero extension at the ends. Finite summation by parts therefore bounds each \(|D_H(n)|\) by \(2{\cal W}_t(n-H,2H)\): use the interval prefixes with phase zero in \((n-H,n+H]\) for the partial sums. For \(H\le X/8\) all starts \(n-H\) lie in \([X/2,2X)\). Apply (2) on the two integer dyadic blocks with left endpoints \(X/2\) and \(X\). With a smaller fixed \(\eta\) in (2), the length \(2H\) is in range on both blocks whenever \(X^{1/3+\eta}\le H\le X^{1-\eta}\) and \(X\) is sufficiently large. Thus for all such dyadic \(X\),
\[
 {\cal E}(X,H)\ll_{\eta,A} XH^2(\log X)^{-A}.                 \tag{7}
\]
The interval-sum bound was used on the actual coefficients \(t\), and the time kernel and block were unchanged.

For any fixed \(B\ge0\) and \(K>0\), put \(H=\lfloor\sqrt X(\log X)^B\rfloor\). Taking \(A\ge 2B+K\) in (7) gives \({\cal E}(X,H)\ll_{B,K}X^2(\log X)^{-K}\). In the exact round-4 expression let \({\cal A}(X,H,G)\) be the signed off-diagonal sum with \(\gcd(m,k)<G\). The removed diagonal costs \(O(XH)\), and the discarded large-gcd terms cost \(O(XH^2/G)\) in absolute value. Set \(G=\max(2,\lceil(\log X)^{2B+K}\rceil)\). The same calculation gives the signed bound
\[
 |{\cal A}(X,H,G)|\ll_{B,K}X^2(\log X)^{-K}.                  \tag{8}
\]
The coprime prime pairs from round 4 lie in this retained family and have positive-entry contribution \(\gg X^2(\log X)^{2B-2}\). For example \(B=2\) gives a positive subfamily above \(X^2\), while (8) bounds the entire signed sum to each prescribed inverse-logarithmic order with its displayed choice of \(G\). For a single cutoff independent of \(K\), \(G_\ast=\max(2,\lceil \exp(\sqrt{\log X})\rceil)\) makes the large-gcd remainder smaller than \(X^2(\log X)^{-K}\) for every fixed \(K\), so (8) also holds for this same \(G_\ast\) at every fixed order. The cancellation estimate keeps the original time kernel and the actual signed coefficients.

## 3. Limit of the imported rate

The original real bounded-multiplicative Matomäki–Radziwiłł estimate compares a normalized short interval average with its long average. Its quantitative mean-square error has the terms \((\log\log h/\log h)^2\) and \((\log X)^{-1/50}\). For polynomial-sized \(h\) these only provide a fixed inverse-logarithmic term. A stronger quantitative theorem is needed to pay every preassigned logarithmic widening as in (7)–(8). Here the additional unit transfer uses the all-fixed-logarithmic form (3), with the stated length threshold, rather than extrapolating the 2016 estimate.

For \(H=\lfloor X^{1/2+\delta}\rfloor\) with fixed \(0<\delta<1/2\), (7) gives \(O_{\delta,A}(X^{2+2\delta}(\log X)^{-A})\), which does not give \(O_\epsilon(X^{2+\epsilon})\) for \(\epsilon<2\delta\). Each \(A\) is fixed and its constant may depend on \(A\). This route would need a power improvement in the relevant short correlations, or a stronger use of the centered weights than the total-variation comparison above. The smoothed sum itself also needs its own estimate. There is neither a pointwise bound at every short-interval start nor a bound for every fixed shift in (2), (6) or (7).

## Primary analytic sources

- [Matomäki, Radziwiłł, Shao, Tao and Teräväinen, Higher uniformity of arithmetic functions in short intervals II, Theorem 1.1(i)](https://link.springer.com/article/10.1007/s00222-026-01408-6). Only its unconditional Möbius assertion on almost all starts is used.
- [Matomäki and Radziwiłł, Multiplicative functions in short intervals, Annals of Mathematics 183 (2016)](https://annals.math.princeton.edu/wp-content/uploads/annals-v183-n3-p06-p.pdf), earlier bounded real multiplicative estimate for comparison.
- [Klurman, Mangerel and Teräväinen, Multiplicative functions in short arithmetic progressions](https://doi.org/10.1112/plms.12546), introductory restatement of the earlier quantitative mean-square bound.
