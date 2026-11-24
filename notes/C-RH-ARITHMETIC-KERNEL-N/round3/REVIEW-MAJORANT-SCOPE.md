# Review of the global majorant and the exact finite cross term

C-RH-ARITHMETIC-KERNEL-N. NON-CANONICAL. Candidate-D paper review of [MAJORANT-SCOPE](MAJORANT-SCOPE.md) and the same-block alternative. Sources within this packet are [SIGNED-SPECTRUM](SIGNED-SPECTRUM.md) §4–5 and the pinned candidate's [FOUNDATION](../FOUNDATION.md). No numerical audit or alteration of either source.

**Verdict.** Both deductions survive. The global sinc majorant has an additional zero-free consequence for \(L(s,\chi_5)\) in \(\Re s>2/3\). The finite cross-term condition is equivalent to RH on the stated inputs. The additional consequence of the global condition does not establish its logical strictness relative to RH, since the argument does not decide whether RH alone implies that consequence.

## 1. The global majorant controls a supplementary interval

Fix a large dyadic \(X\), \(D=4X\), center \(c=3X/2\), and \(w_X(n)=\operatorname{sinc}^2(\pi(n-c)/(2X))\). The global assumption and the established same-conductor and diagonal bounds in (8) give
\[
 \sum_{n\in\mathbb Z}w_X(n)|G_X(n)|^2
       \ll X^2(1+\log X)^{\max(B,1)}.
\]
The polynomial is frozen with the same \(X,D\) in the following argument. A bound only on the original dyadic block would not yield this global positive sum.

On \(D\le n\le2D\) the coefficients removed by truncation at \(D\) have \(1\le n/d<2\), since \(d>D\). Hence exactly \(T(n)-F_D(n)=S(n)-S(D)\) for the unit jump \(H(1)=1\). The omission bounds in SIGNED-SPECTRUM §4 are valid on translated blocks of length \(X\) with unchanged frequencies, coefficients and cutoff because the finite large sieve is translation invariant. A fixed number of such blocks covers the supplementary interval.

For the Jackson comparison on that interval, the truncated arithmetic first difference satisfies
\[
 |\Delta F_D(m)|\le\sum_{d\mid m}|s(d)|
   =3^{\#\{p\mid m:\chi_5(p)=1\}}\ll_\epsilon m^\epsilon
 \quad(m\ge1).
\]
The finite prime-factor product gives the equality. For the bound, every prime sufficiently large in terms of \(\epsilon\) has \(3\le p^\epsilon\), and the remaining distinct primes contribute a fixed multiplier. For shifts \(|j|\le X\), all indices in the differences lie in \([3X,9X]\). The first absolute moment of the shift kernel is \(O(\sqrt X)\), so this part is \(O_\epsilon(X^{1/2+\epsilon})\) pointwise. The omitted shifts cost \(O(D(tX)^{-3})\), with \(t=X^{-1/2}\), by the global bound \(|F_D|\le D\). These estimates also treat the inclusive right endpoint.

The global majorant already implies RH by the dyadic block estimate of SIGNED-SPECTRUM §5 and the proved spectral approximation. Thus \(|T(n)|\ll_\epsilon X^{1/2+\epsilon}\) on the supplementary interval by the known transfer. Combining the same frozen spectrum, the translation-invariant omissions and this \(T\) bound yields (1) in MAJORANT-SCOPE.md after reducing the fixed epsilon in the component bounds.

## 2. Recovering the anchor and the extra holomorphy

The only zeros of the weight on \([4X,8X]\) are \(11X/2\) and \(15X/2\). After rescaling by \(X\), each zero is quadratic with a nonzero coefficient, and away from them the weight is positive on a fixed compact set. Therefore \(w_X(n)\gg \operatorname{dist}(n,\{11X/2,15X/2\})^2/X^2\) on this interval. Delete neighborhoods of radius \(h=\lceil X^{2/3}\rceil\). The sum of \(1/w_X(n)\) over the remaining integers is \(O(X^2/h)\), by summing the reciprocal squares of the distances. Consequently weighted Cauchy–Schwarz in (1) gives an absolute sum \(O_\epsilon(X^2h^{-1/2}X^\epsilon)\). The deleted \(O(h)\) integers cost \(O(Xh)\) using \(\sum_{d\le2D}|s(d)|\le2D\). Both costs are \(O_\epsilon(X^{5/3+\epsilon})\).

Near the right endpoint \(2D\) on a fixed length proportion of \(X\), the weight has a uniform positive lower bound. Averaging (1) over the final \(h\) integers produces a point there with \(|S(n)-S(D)|\ll_\epsilon Xh^{-1/2}X^\epsilon\). Move from that point to \(2D\) by at most \(h\) integer differences, each \(|s(m)|\ll_\epsilon X^\epsilon\). It follows that \(|S(2D)-S(D)|\ll_\epsilon X^{2/3+\epsilon}\). Telescoping at dyadic \(D\) gives \(|S(D)|\ll_\epsilon D^{2/3+\epsilon}\), so the full absolute dyadic sum of \(|S(n)|\) is \(O_\epsilon(D^{5/3+\epsilon})\).

The step extension of \(S\) then makes \(s\int_1^\infty S(x)x^{-s-1}\,dx\) absolutely and locally uniformly convergent for \(\Re s>2/3\). Indeed each dyadic block costs \(O_\epsilon(D^{2/3-\Re s+\epsilon})\), and choose \(\epsilon\) strictly below the distance of a compact set from the boundary. The holomorphic integral equals the Dirichlet series for \(\Re s>1\), so it agrees meromorphically with \(1/[\zeta(s)L(s,\chi_5)U(s)]\) in the larger half-plane. At a zero of \(L(s,\chi_5)\) there, \(U\) is nonzero, and \(\zeta\) can only be singular at \(s=1\). A simultaneous zero of \(\zeta\) would add pole order rather than remove it. Since \(L(1,\chi_5)>0\), the supplementary exclusion follows.

## 3. Finite cross-conductor criterion

For the retained coefficients of SIGNED-SPECTRUM (6), let
\[
 g_r(n)=\sum_a z_{ra}\,{\rm e}(na/(5r)),\qquad G_X=\sum_r g_r.
\]
The exact squared norm on the original block is
\[
 E_X=\sum_{n=X}^{2X-1}|G_X(n)|^2=\sum_r E_r+D_X^{\rm cross},
 \qquad E_r=\sum_{n=X}^{2X-1}|g_r(n)|^2 .
\]
Here \(D_X^{\rm cross}\) is precisely the stated sum over \(r\ne s\) with the finite Dirichlet kernel. Reversing the ordered pair conjugates each summand, making \(D_X^{\rm cross}\) real. The argument keeps all frequency separations.

The nonnegative sequence \(|g_r(n)|^2\) is periodic with period \(5r\). A length-\(X\) interval is bounded by at most \(\lceil X/(5r)\rceil\) whole-period sums using positivity. Orthogonality on one whole period gives
\[
 E_r\le(X+5r)\sum_a|z_{ra}|^2.
\]
This is an elementary form of the proposed same-conductor estimate and avoids the large sieve for this step. Since \(r\le4X\) and retaining coefficients with multipliers of modulus at most one makes their total square sum at most the complete mean square of \(F_D\), we obtain \(\sum_rE_r\ll X^2\log(2X)\). Thus
\[
 (D_X^{\rm cross})_+\le E_X
 \le (D_X^{\rm cross})_+ + O(X^2\log(2X)).
\]
The established dyadic approximation bound is \(\sum_{X\le n<2X}|T(n)-G_X(n)|^2\ll X^2(1+\log X)^5\). The finite cross bound for every \(\epsilon>0\) is consequently equivalent to \(\sum_{X\le n<2X}|T(n)|^2\ll_\epsilon X^{2+\epsilon}\) on the dyadic blocks. RH implies the latter by the classical all-epsilon Mertens bound and the Dirichlet unit. In the other direction, cover \([Y,Y^2)\) by its intersecting dyadic blocks, each with left endpoint between \(Y/2\) and \(Y^2\). Divide each block bound by its squared left endpoint. Geometric summation gives \(Q_T(Y)\ll_\epsilon Y^{2\epsilon}\). For any fixed test exponent \(r\), take \(\epsilon=1/(4r)\) and then sufficiently large \(Y\) to get \(Q_T(Y)^r\le Y\). The proved rational-window criterion now gives RH.

No weighted behavior on a supplementary interval is used in this finite route. The close-pair hypothesis gives a sufficient bound with extra global information. The exact all-separation finite cross estimate supplies an equivalent, still unproved arithmetic condition with the same original zero target.
