# Same-session review of the smooth-divisor packet and the cube-root majorant

**NON-CANONICAL. No authority.** Paper review within C-RH-ARITHMETIC-KERNEL-N, owner issue 2087 and draft 2089. Author source reviewed read-only. No numerical computation. The deductions under review retain **candidate-D**. The signed square-root bound and the signed transfer below the cube root remain **O**.

## Disposition

No mathematical error found in equations (1)–(6) of SMOOTH-DIVISOR-AND-TRANSFER. Two precision edits would improve the stated proof. In the parity argument, refer to the nonzero nonconstant cofactor terms, since the terms with \(s(m)=0\) place no restriction on \(m\). For the fixed-relative-interval prime counts, the classical estimate in Yamada's introduction suffices. If citing Theorem 1.2 directly, choose one available log exponent above one and use it at fixed modulus five.

## Smooth-divisor packet

Fix \(B\ge1\) and take \(0<\eta<\min(1/B,\varepsilon/2)\). With \(\sigma=1-1/B+\eta\), Rankin's prefactor beyond \(v^{1-1/B}\) is \(y^\sigma v^\eta\). The Euler product has logarithm \(O_{B,\eta}(y^{1-\sigma})=O_{B,\eta}((\log X)^{1-B\eta})=o(\log X)\). The prefactor and the product together cost \(O_{B,\varepsilon}(X^\varepsilon)\) uniformly in \(1\le v\le4X\). The case \(B=1\) gives \(\sigma=\eta>0\). The interval count follows by assigning one divisor in \([v,yv]\) to each conductor and bounding its number of multiples by \(H_0/d+1\le2H_0/v\) when \(H_0\ge v\).

For fixed \(a\), strip membership implies
\[
 |r-s|\le320krs/(X|a|)\le1280kR^2/(X|a|).
\]
There is no circular wrap because the inherited \(a/(5r)\) are within \(2/\sqrt X\) of zero. The global count uses \(v=U\) and interval length \(R\). A strip row uses \(v=\min(U,H)\) on an interval of length \(CkH\), which is at least \(v\). Both counts remain valid for an arbitrary submask and include the diagonal. The near-pair product is bounded by \(XRH/|a|^2=R^3/|a|^2\) times the two smooth-divisor savings and a subpower factor. The far-pair error is absorbed because \(R^3/[U\min(U,H)]^{1/B}\ge R\). Minkowski for the retained numerators applies to the actual complex-coefficient functions in the weighted \(L^2\) norm. The harmonic sum costs only a logarithm, since \(|a|\le40\sqrt X\). The same reasoning sums the shell norms after deletion.

For the root \(u_0\) of the threshold equation, monotonicity applies on \([1,\infty)\) because \(R^3/X^2\ge1\) and \(H\ge1\). If \(u_0>R\) and an eligible divisor \(u_y(r)\) exists, then \(r/u_y(r)<2\), so \(u_y(r)=r\) and \(u_0\le2R\). The relation
\[
 R\min(R,H)\le u_0\min(u_0,H)\le4R\min(R,H)
\]
shows that taking \(U=R\) pays at most the fixed factor \(4^{1/B}\). The threshold simplifications for \(B=1\), as well as for \(1\le B\le2\) with \(R\le X\), follow because the claimed explicit roots lie at or below \(H\).

For the nonemptiness construction, \(S=R^{3/2}/X\asymp X^{1/8}\). The product of split primes up to \(\log X\) exceeds \(S\) for large \(X\) by the fixed-modulus Chebyshev asymptotic. First crossing supplies \(d\in[S,S\log X]\). Both large factors in \(r=dpq\) are \(X^{5/16+o(1)}\) and satisfy the core prime limits. The chosen intervals place \(r\) between \(6R/5\) and \(7R/5\). The number of primes in the fixed relative interval is \(\gg(R/d)^{1/2}/\log X\), so unordered distinct pairs yield \(\gg R/[d(\log X)^2]\) distinct conductors. Their \(a=1\) mode passes the power cap, Jackson cap and star height bound. Clearing an odd common denominator in the finite cofactor, the \(m=1\) term gives an odd integer and every other nonzero term gives an even integer. Hence \(A_r\ne0\), and the nonzero kernel and eventual positive multiplier give an actual nonzero mode. The count concerns distinct conductors.

## Below-cube-root absolute majorant

For fixed \(0<\gamma<1/3\) and \(l>(1-\gamma)/\gamma\), counting split primes in the fixed relative range and then choosing \(l\) distinct primes gives \(N\gg_{\gamma,l}E/(\log X)^l\) distinct conductors in \([3E/5,2E/3]\). Their largest prime is smaller than \(z\) by a fixed power because \((1-\gamma)/l<\gamma\). Since \(r>E/2\), no supported \(e\le E\) contributes to its primitive coefficient except \(e=r\). In the inner factor of the exact discrepancy, \(D/r\in[3z/2,5z/3]\), eventually below \(z^2\). Each admissible rough factor is therefore one split prime. This proves the coefficient \(-2s(r)\sum_{z<p\le D/r}p^{-1}\) with exact sign. For the whole chosen panel the coefficients share a sign and have magnitude comparable to \(1/\log X\). The normalized \(b(r,1)\) converges to the same nonzero \(\tau/(2\pi i)\), and the optional smoothing tends to one.

Since \(r\asymp X^{1-\gamma}\), the \(a=1\) mode passes the original star cuts and has \(r>D^{2/3}\) for large \(X\). Its height is of order \(X^\gamma\). Bins of width \(cE^2/X\) give phase differences at most a constant times \(c\) on the taper, so \(c\) can be fixed to give the stated strictly positive real part uniformly. The number of bins is \(O(X/E)\). After subtracting the diagonal the pair count is at least \(N^2/B_{\rm bins}-N\), where \(B_{\rm bins}=O(X/E)\). The first term dominates because \(E^2/(X(\log X)^l)\to\infty\). Multiplying by \(X/(\log X)^2\) gives the claimed positive subtotal.

The original large-gcd bound is absolute. Its proof uses the shell upper bounds, the coprime progression count inside the strip and a bound \(X^\varepsilon/|a|\) for each coefficient. The exact discrepancy coefficients on this panel meet those hypotheses, including when the Jackson factor is absent. Thus pruning costs \(O_\varepsilon(X^{2+\varepsilon})\). Taking \(\varepsilon<1-3\gamma\) preserves a constant proportion of the lower bound.

For the upper absolute comparison, distinct primitive circle frequencies have gap at least a constant times \(E^{-2}\). The near-strip row degree is \(O(1+kE^2/X)\). The short discrepancy expansion gives squared mass \(O(E(1+\log X)^5)\) and absolute coefficient mass \(O(E(1+\log X)^3)\), by the inherited \(|A_r^\Delta|\ll |s(r)|(1+\log X)^2\) and summation of \(1/|a|\). Combining the row bound, \(|J_w|\le2X\), and \(2|c_i c_j|\le |c_i|^2+|c_j|^2\) gives \(O((XE+E^3)(1+\log X)^6)\). The taper tail contributes at most \(O(X^{-6}(1+\log X)^6)\).

The positive subtotal blocks a bound at the target power on the sum of absolute pair contributions for each fixed \(\gamma<1/3\). The signed discrepancy norm remains open. The removable family retains the exact mixed term with the round-six prime profile, as required by the inherited norm criterion.
