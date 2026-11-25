# Adversarial review of local time taper and determinant pairs

This is internal same-session review, not independent external confirmation.

C-RH-ARITHMETIC-KERNEL-N, #2087 / #2089. NON-CANONICAL. Candidate-D paper review of FINITE-TAPER.md §§1–5. Source files were read without modification. No numerical audit.

**Verdict.** The finite taper, same-block transfer, high-gcd pruning, genuine positive panel and its signed inverse-logarithmic cancellation follow at their stated scope. The arithmetic power saving for the remaining signed sum is open.

## Exact cutoff and time support

For integer dyadic \(X\ge2^{16}\), \(k=\lceil3\log_2 X\rceil\) and \(h=\lfloor X/(16k)\rfloor\) give \(X/(32k)\le h\le X/(16k)\). The \(k\)-fold box convolution is a probability kernel supported on \([-kh,kh]\). Convolving with \(\mathbf1_{[X-kh,2X-1+kh]}\) equals one at every integer in \([X,2X-1]\), since every translated input is in the interval. Its entire support is contained in \([7X/8,17X/8-1]\). The inclusive endpoints are consistent with the geometric sum and do not add an extra value.

The normalized box Fourier coefficient at \(y\) is at most \(1/[2(2h+1)\|y\|]\) off zero by \(|\sin(\pi y)|\ge2\|y\|\). At \(\|y\|\ge64k/X\), the denominator is at least eight. The initial interval has at most \(2X\) elements, so the Fourier tail is at most \(2X8^{-k}\le2X^{-8}\). From \(\sum|s|\ll X\), the cofactor harmonic sum, and \(|b(r,a)|\ll1/|a|\), one gets \(\sum|z_\theta|\ll X(1+\log X)^2\). Thus dropping the far pairs costs \(O(X^{-6}(1+\log X)^4)\) in absolute value. The retained strip includes its equality boundary, and the upper estimate for omitted pairs is valid there as well.

The Jackson shifts \(|j|\le X/2\) from the support of the new taper land within \([3X/8,21X/8]\subset[0,D]\). The exact increment bound for \(F_D=T\) applies there. The shift tails use the bound \(|F_D|\le D\) on all integers, with cost \(O(X^{-1/2})\). The other frequency omissions carry over to finitely many translated length-\(X\) intervals by the same large-sieve coefficient sums. These checks give the claimed \(O(X^2(1+\log X)^5)\) approximation energy on the full taper support. For fixed \(r\), one can also use elementary period covering instead of the large sieve: the nonnegative squared conductor sum has period \(5r\), so its support-interval energy is bounded by \((2X+5r)\) times its complete mean square. This gives the same \(O(X^2\log X)\) bound after summing over \(r\).

The finite weighted energy controls the original block, and RH controls \(T\) on the entire compact support, so the equivalence does not require extra behavior on a remote interval. In the converse direction, a block square bound \(O_\epsilon(X^{2+\epsilon})\) gives an absolute block sum \(O_\epsilon(X^{3/2+\epsilon/2})\) by Cauchy–Schwarz. Dyadic summation makes the Mellin integral of the integer step function \(T\) holomorphic for \(\Re s>1/2\), by choosing \(\epsilon\) small on each compact set. The identity for \(1/(\zeta U)\) then has the stated zero consequence. The Mellin proof here is self-contained. The reference to SIGNED-SPECTRUM §4.1 should be matched to the final published section number.

## High-gcd pruning

Fix the two shells, two nonzero signed numerators and a common divisor \(g\). Put \(l=\gcd(|a|,|b|)\), \(a_0=a/l\), \(b_0=b/l\), \(u=r/g\), \(v=s/g\). Then \(as-br=gl(a_0v-b_0u)\). The admissible integer \(m=a_0v-b_0u\) is nonzero because the unequal-conductor fractions are reduced. Its count under the determinant cutoff is at most \(2560kRS/(Xgl)\), with no constant term needed even when the bound is below one. For each \(m\) any integral solution set is a translate of the progression with signed step \((a_0,b_0)\). Its intersection with the shell rectangle contains at most \(1+lL/g\) points, by using the narrower of the two coordinate interval lengths after dividing by the corresponding absolute step. These bounds allow all numerator signs and omit arithmetic filters only to enlarge the count.

The coefficient bound \(O_\epsilon(X^\epsilon/|ab|)\) is uniform after shrinking the epsilon in the two divisor estimates and absorbing their logarithms. Multiplying the count by this bound and by \(|J_w|\le2X\) gives a sum over \(g\) proportional to
\[
 \frac{kX^\epsilon RS}{|ab|}
 \sum_{g\ge G_0}\left(\frac{1}{gl}+\frac{L}{g^2}\right).
\]
The harmonic sum stops at \(4X\), and the other sum costs \(O(L/G_0)\). Both \(RS\ll X^2\) and \(RS L/G_0\le X^2\) hold. Summing the reciprocal numerators and the shell pairs costs only logarithms. Thus the all-epsilon \(O_\epsilon(X^{2+\epsilon})\) pruning estimate is sound. It does not identify a fixed-logarithm bound.

## Actual top panel and its signed cancellation

For \(a=b=1\) and \(3X<r,s\le4X\), \(A_r=s(r)\) since \(D/r<11\). The multiplier tends uniformly to one, and \(b(r,1)\overline{b(s,1)}\) tends to \(|\tau/(2\pi i)|^2>0\). The phase on the entire taper support stays in the stated arc since \(|1/(5r)-1/(5s)|\le1/(60X)\). Therefore each same-sign contribution has real part bounded below by a positive constant times \(X|s(r)s(s)|\), using \(\sum_n w(n)\ge X\). All these numerators are retained. All the pairs are inside the strip, and for distinct \(r,s\) one even has \(g\le|r-s|<X\), whereas their shell parameters imply \(G_0>27X/8\). Thus the positive panel survives pruning.

The absolute coefficient mass follows from \(|s|=v*(1*\chi_5)\) with the three stated local factors of \(v\). Absolute summability at \(3/4\) controls both the omitted mean and the square-root error in the inner ideal count at size \(O(X^{3/4})\). The Euler product at one is positive. The squared masses of the two sign classes sum to at least half the squared total mass, and removal of the diagonal costs only \(O(X\log X)\) before multiplying by \(X\). This proves a lower bound \(\gg X^3\) for the actual positive entries of the fixed panel. It concerns those entries rather than the signed panel.

For the full signed panel, the unconditional Davenport estimate is stated in [He and Huang, equation (1.2)](https://www.impan.pl/shop/en/publication/transaction/download/product/91740?download.pdf=), before their later conditional results. It supplies \(M\) and \(M_{\chi_5}\) by a finite additive expansion. Hyperbola summation for \(\mu*(\mu\chi_5)\) with both strips cut at \(\sqrt x\), followed by convolution with the coefficients of \(U^{-1}\), gives \(\sum_{r\le x}s(r)\ll_A x/(\log x)^A\) for every fixed \(A\). The large-unit-divisor term is \(O(x^{7/8}(1+\log x))\) by the absolute series at \(3/4\). On \(3X<r\le4X\) the multiplier of \(s(r)\) has uniformly bounded total variation and supremum for all retained times. Summation by parts therefore proves the amplitude estimate. Squaring, summing over \(O(X)\) times, and subtracting the same-conductor diagonal yields the asserted \(O_B(X^3/(\log X)^B)\) for every fixed \(B\). This is genuine cancellation of the specified large positive and negative pieces, leaving the claimed power gap.
