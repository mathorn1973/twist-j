# Complete factor rows below the long-product boundary

**NON-CANONICAL. Authority none.** The deletion and rectangle identities
are **candidate-D**. The full positive whole-window bound is **O**.
Action layer `NOT_APPLICABLE`. Unconditional paper derivation for
C-RH-THREE-INTERFACE-SYNTHESIS-N, owner #2091, draft #2093.

Use the original slab, average and notation \(A,B_X,L_X,P_X,E_X,b^u\)
from [BILINEAR-LOW.md](BILINEAR-LOW.md), with \(B_X-1\) the last averaged
integer and \(B_X=2X+o(X)\). Write \(\|f\|_X^2=\sum_{X\le N<2X}|f(N)|^2/[N(N+1)]\).
For a sequence \(z\) of the original raw support type, define
\[
 \mathcal C_X(z)=P_X(z)-L_X\sum_d z_d/d+\tfrac12\sum_d z_d.
\]
The exact compensation identity is
\[
 \mathcal C_X(z)=-U_H^J\sum_d z_d\lfloor N/d\rfloor-E_X(z).       \tag{1}
\]
The projection error has norm \(O((1+\log X)^{3/2})\) if
\(|z_d|\le\tau(d)\), by the cited note.

## 1. Deleting rows through the boundary

Fix \(0\le U\le X^{3/10}\). Let \(\rho_a\) be real, \(|\rho_a|\le1\),
supported on \(B_X/A-U<a\le A\), and put
\[
 z_d=\sum_{ab=d,\ a,b\le A}\rho_a\mu(a)\mu(b).
\]
Then, also with \(z\) replaced by \(z\mathbf 1_{d<B_X}\),
\[
 \|\mathcal C_X(z)\|_X\ll (1+\log X)^{3/2}
                       +A^{1/2}(U+1)^{5/2}/X .                  \tag{2}
\]
The same result applies to the symmetric weight \((\rho_a+\rho_b)/2\)
by interchange of the factors. Both affine terms in (1) use the very
same raw packet.

For every averaged integer \(n\) and every selected row, the integer
\(x=\lfloor n/a\rfloor\) lies in \([1,2A)\) on late slabs. The identity
\(\mu*1=\delta_1\) gives
\[
 \sum_{b\le A}\mu(b)\lfloor n/(ab)\rfloor
   =1-\sum_{A<b\le x}\mu(b).                                    \tag{3}
\]
The second sum is empty for \(a\ge B_X/A\), leaving at most \(U+1\)
rows where it may appear. As \(a\asymp A\), its length is bounded by
\(\max(0,n/a-A)\ll U+1\). The full packet contribution to the floor
sum is the constant \(\sum_a\rho_a\mu(a)\) plus an error bounded by
\(O((U+1)^2)\). The error vanishes for \(n\le B_X-AU\). Since every
shift used by the average is at most \(J(H-1)=B_X-2X\), the averaged
error is supported on the final \(O(A(U+1))\) starts of the original
slab. Its weighted squared norm is \(O(A(U+1)^5/X^2)\). The constant
costs \(O(A/\sqrt X)=O(1)\). Use (1) and the projection estimate to
obtain (2). Raw truncation at \(B_X\) leaves all these floors unchanged
and preserves the divisor majorant.

Taking \(U=X^{3/10}\) and weight one on the deleted rows, one may
replace \(b^u\) by the asymmetric rectangle
\[
 C=\left\lfloor B_X/A-X^{3/10}\right\rfloor,\qquad
 b^{\mathrm{rect}}_d=\sum_{ab=d,\ a\le C,\ b\le A}\mu(a)\mu(b)
\]
in the entire compensated expression. The maximal possible raw
denominator is now \(AC\le B_X-A X^{3/10}\). This lowers the upper
raw support bound by order \(X^{4/5}\) below \(B_X\). It changes the
actual divisor-multiple coefficients, including at primitive heights
\(X|a|/q\asymp1\), with both affine terms recomputed. In comparison,
direct deletion of an arbitrary raw subfamily in
\([B_X-\Delta,B_X)\), for \(0\le\Delta\le X/2\), costs
\(O_\epsilon((1+\log X)^{3/2}+X^{-1+\epsilon}(\Delta+1)^{3/2})\).
Its floors are zero or one, its averaged profile lives on the final
\(O(\Delta+1)\) starts, and the divisor bound gives
\(O_\epsilon(X^\epsilon)\) per coefficient. That direct argument gives
a subpower allowance at \(\Delta=X^{2/3}\). Identity (3) cancels
across the entire second factor and permits the wider cut.

## 2. Window transfer and accumulated loss of deeper cuts

Restrict each squared slab error to its intersection with the original
full window. Summing over \(O(1+\log Y)\) slabs and using the inherited
comparison for \(\mathcal C_X(b^u)\) gives
\[
 \left|\sqrt{Q_{\mathcal C(b^{\mathrm{rect}})}(Y)}
       -\sqrt{Q_R(Y)}\right|\ll(1+\log Y)^2 .                    \tag{4}
\]
The positive part is 1-Lipschitz. The rectangle is chosen separately
for each dyadic slab. Equation (4) preserves the original quantifiers
in both directions by using exponent \(2r\) on the source side and
absorbing the logarithmic norm error. The masks of
[LOW-FREQUENCY-PAIRS.md](LOW-FREQUENCY-PAIRS.md) can also be applied to
this new amplitude: the bound \(|b^{\mathrm{rect}}_d|\le\tau(d)\)
preserves both the divisor-multiple bound and numerator independence.
That removal adds \(O_\epsilon(Y^\epsilon)\) to the norm comparison.
The signed slope and constant in (4) are those of the rectangle.

For any integer first cap \(1\le C\le A\) and \(n\ge A\), finite
convolution gives the exact identity
\[
 -\sum_{a\le C,\ b\le A}\mu(a)\mu(b)\lfloor n/(ab)\rfloor
 =M(n)-M(C)-M(A)
  -\sum_{a>C,\ b>A,\ ab\le n}\mu(a)\mu(b)\lfloor n/(ab)\rfloor. \tag{5}
\]
Sum \(\mu*\mu*1=\mu\) to \(n\) and use inclusion-exclusion. With
only one cap the two sums are \(M(C)\) and \(M(A)\) by (3) with the
other factor unrestricted.

The proof of (2) extends to \(U\le cA\) for a sufficiently small
fixed \(c>0\), since then \(n/a<2A\) still holds. It supplies the
cumulative allowance \(O(A^{1/2}(U+1)^{5/2}/X)\) for a single cut
of depth \(U\). Dividing that cut into disjoint bands of width \(V\ge1\)
gives the same order by the same argument. The band at depths
\(jV\) through \((j+1)V\) has at most \(V+1\) rows, missing intervals
of length \(O((j+1)V)\) per row, and end support of length
\(O(A(j+1)V)\). Its norm allowance for the missing intervals is
\(O(A^{1/2} V((j+1)V)^{3/2}/X)\). Summing through \(\lceil U/V\rceil\)
bands gives \(O(A^{1/2}(U+V)^{5/2}/X)\), before any sum of projection
errors. The supports are nested, so disjointness of rows does not
give disjointness of the end contributions in time. At fixed positive
fractional depth \(U\asymp A\) this allowance is of order \(X^{1/2}\)
in weighted norm. Also, after the first cut the unrestricted-row
threshold for deleting second factors is \(B_X/C>A\). A deeper
alternating application therefore again incurs a corner defect.
Equation (5) retains coefficient one on \(M(n)\) and exposes the
signed sum that would require a further estimate.

[FULL-COUPLED-ENERGY.md](FULL-COUPLED-ENERGY.md) treats the separate
symmetric square and signed corner. The
[adjacent cube-root transfer](https://github.com/mathorn1973/twist-j/blob/4e098f9742a72a128bfb61a10c429bced78fe17e/notes/C-RH-ARITHMETIC-KERNEL-N/round6/CUBE-ROOT-TRANSFER.md)
uses a conductor-to-raw identity and marked primes for its own
split-prime carrier. The asymmetric row cut here reduces the raw
support past the full floor-cancellation threshold. The remaining
coupled positive energy is **O**.
