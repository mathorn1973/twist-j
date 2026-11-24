# A moving least-prime cut costs only logarithms on short support

C-RH-ARITHMETIC-KERNEL-N, #2087 / #2089. NON-CANONICAL, no authority. Candidate-D. Result-exposed paper argument using the proved kernel estimates in KERNEL.md §7. No numerical audit.

Let \(K_d(n)=S_{\chi_5}(\lfloor n/d\rfloor)\) and let \(s(d)\) be the squarefree split weight of the candidate. For arbitrary real thresholds \(z(n)\), define
\[
 L_>(n)=\sum_{\substack{d^3\le n^2\\P^-(d)>z(n)}}s(d)K_d(n),
 \qquad P^-(1)=+\infty.
\]
Define \(L_\le(n)\) by the complementary least-prime restriction in the same short range.

**Theorem.** On every quadratic integer window,
\[
 \sum_{Y\le n<Y^2}\frac{|L_>(n)|^2+|L_\le(n)|^2}{n(n+1)}
       \ll (1+\log Y)^6,\qquad Y\ge2.                         \tag{1}
\]
The constant is uniform in the entire function \(z(n)\). The result also holds with any fixed coefficients \(c(d)\) satisfying \(|c(d)|\le |s(d)|\).

On an integer block \(X\le n<2X\), put \(D=\lfloor(2X)^{2/3}\rfloor\). Place each supported \(d\le D\) at integer coordinates \((d,\ell(d))\), with \(\ell(d)=P^-(d)\) for \(d>1\) and \(\ell(1)=D+1\). Write \(D_n=\lfloor n^{2/3}\rfloor\) and clamp the second threshold to \(b_n=\min(D,\max(0,\lfloor z(n)\rfloor))\). For \(d>1\), the condition \(\ell(d)>b_n\) is exactly \(P^-(d)>z(n)\). The convention for \(d=1\) always selects it on the rough side. Thus the desired mask is a rectangle consisting of a prefix in the first coordinate and a suffix in the second.

Pad both coordinate lengths to \(2^J\) with \(J=\lceil\log_2(D+1)\rceil\), and assign zero coefficients outside the ranges. Every prefix or suffix is a disjoint union of at most \(J+1\) aligned binary intervals. Therefore each selected rectangle is a disjoint union of at most \((J+1)^2\) aligned binary cells \(I\times J'\). Let \(f_C(n)\) denote the kernel sum with coefficients restricted to a cell \(C\). Cauchy–Schwarz at each \(n\) gives
\[
 |L_>(n)|^2\le (J+1)^2\sum_{C\text{ aligned}}|f_C(n)|^2 .
\]
This is an upper bound using all binary cells, not just those selected at that \(n\).

Fix a pair of dyadic side lengths. The corresponding cells partition the padded coordinate array. For each cell, use the sharp finite-interval inequality from KERNEL.md §7,
\[
 \sum_{X\le n<2X}|f_C(n)|^2\ll (X+D^2)\,\mathcal E_C,
\]
where \(\mathcal E_C\) is the complete-period mean square. Summing the energies at the fixed side-length pair gives \(\sum_C\mathcal E_C\le \mathcal E_{\rm abs}\ll D(1+\log D)\), again by KERNEL.md §7. Indeed the coefficient pairs retained in the complete-period formula lie in disjoint within-cell Cartesian squares, so the sum of their absolute values is bounded by the common majorant regardless of the number of cells. Summing over the \((J+1)^2\) side-length pairs yields
\[
 \sum_{X\le n<2X}|L_>(n)|^2
   \ll (J+1)^4(X+D^2)D(1+\log D)
   \ll X^2(1+\log X)^5 .
\]
The same proof handles \(L_\le\) by a prefix in the second coordinate. Divide by \(X^2\), then cover \([Y,Y^2)\) by the dyadic blocks starting at \(Y,2Y,\dots\). This proves (1).

For every choice of \(z(n)\), the square roots of the positive-part energies of the full rough sum and the sharp rough tail therefore differ by \(O((1+\log Y)^3)\) on the same windows. The mixed piece satisfies the same statement. This follows from the 1-Lipschitz positive-part map and the triangle inequality, and provides a window-strength form of the sharp-cut corrections in SMOOTH-INVERSE.md. The estimate concerns short support \(d^3\le n^2\).
