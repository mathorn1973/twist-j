# Two cancellations on the slowest part of the retained spectrum

**NON-CANONICAL. Authority none.** The estimates below are **candidate-D**.
The full positive window bound is **O**. Action layer `NOT_APPLICABLE`.
This is a same-session paper derivation and review.

## The actual balanced coefficients on a smooth frequency interval

Use the coefficients, forward average and dyadic slab in
[PRIME-CANCELLATION.md](PRIME-CANCELLATION.md). Write
\(\Phi(x)=(\log x)^{3/5}(\log\log x)^{-1/5}\).
Fix a real smooth even function \(w\) equal to one on \([-1,1]\),
supported in \([-2,2]\), with values in \([0,1]\).
Multiply each oscillatory coefficient of the retained low-frequency sum
by \(w(X\theta/K)\), with the signed representative
\(-1/2<\theta\le1/2\). Denote this part by \(L_{X,K}\).
For \(1\le K\le X^{1/10}\), on every sufficiently late slab,
\[
 |L_{X,K}(N)|\ll_w X(1+K)^2\log^3(2X)
         \exp[-2c\Phi(X/(8AK))].                              \tag{1}
\]
Here \(c\) is an admissible unconditional constant in
\(|M(x)|\ll x\exp[-c\Phi(x)]\).
[Lee and Leong, version 4, Theorem 1.2](https://arxiv.org/html/2208.06141v4).

Indeed, \(0<|\theta|\le 2K/X\) implies that the reduced denominator
\(q\ge X/(2K)>D,D_1\) and that \(|\theta|<1/H\).
Thus all original denominator cuts are automatic in this band.
Expanding \(b_{uv}\) by summing over all ordered pairs with product
\(uv\), the positive-frequency part, before averaging the translates
\(n=N+s\), is a sum of kernels
\[
 -\sum_{1\le k\le 8KA^2/X}\sum_{u,v\le2A}c_uc_v
 \frac{w(Xk/(Kuv))e(nk/(uv))}{uv(1-e(-k/(uv)))}.
\]
The negative-frequency part is its conjugate. This counts ordinary
harmonics before reduction, including coincident rational frequencies.
All translates used have \(X\le n\le3X\) on sufficiently late slabs.

Set \(B=X/(8AK)\). The kernel vanishes unless \(u,v\ge2B\).
For \(B\le t\le2A\) the balanced prefix
\(P(t)=\sum_{a\le t}c_a\) satisfies
\(|P(t)|\ll A\exp[-c\Phi(B)]\). Up to \(A\) use the cited bound,
and past \(A\) the absolute prefix decreases from \(|M(A)|\) to zero.
Use partial summation in both variables on \([B,2A]^2\).
Upper boundary terms vanish since \(P(2A)=0\), and lower terms vanish
by support. For the kernel \(F_k(u,v)\) displayed inside the sum,
\[
 |uv\,\partial_u\partial_v F_k(u,v)|\ll_w (1+K)^2/k.
\]
To see this put \(z=k/(uv)\). The prefactor is
\(k^{-1}z/(1-e(-z))\), smooth at zero after continuation.
Both logarithmic derivatives act as \(-z\partial_z\). On the support,
\(nz\le6K\) and derivatives of \(w(Xz/K)\) in that operator are bounded.
Extend the kernel by zero outside support to avoid irrelevant poles.
The mixed integral costs at most \(\log^2(2A/B)\) times the derivative
bound. Sum \(1/k\) up to \(O(K)\) and average in \(s\) to obtain (1).

Since the slab weights sum to \(1/(2X)\), squaring (1) gives the
direct two-sided energy estimate for this actual signed band,
\[
 \sum_{X\le N<2X}\frac{|L_{X,K}(N)|^2}{N(N+1)}
 \ll_w X(1+K)^4\log^6(2X)\exp[-4c\Phi(X/(8AK))].
\]
It also bounds the positive energy of the band. Both this estimate
and (1) hold for the corresponding smooth band of the balanced
\(T_{H_B}\) of [ONE-SIDED-LOW.md](ONE-SIDED-LOW.md) for each fixed
\(B\ge1\). Uniformly over \(1\le K\le X^{1/10}\), eventually
\(2K/X<1/H_B\), and every convexly averaged integer translate is at
most \(3X\). These are the only width requirements in the proof.
This deduction retains the original balanced coefficients throughout.

In particular let \(K=\exp(\kappa\Phi(\sqrt X))\) for fixed
\(0<\kappa<c\). Then \(\Phi(B)/\Phi(\sqrt X)\to1\), so (1) gives
\[
 |L_{X,K}(N)|\ll_w X\exp[-(2c-2\kappa-o(1))\Phi(\sqrt X)] .
\]
Both factors of cancellation act on this same signed spectral sum.
The transition strip is smoothly weighted. A sharp cutoff in its place
introduces a moving hyperbolic boundary in the second partial summation.
The complementary multiplier \(1-w\) and the affine drift are still
part of the exact retained object. Even the displayed slowly growing
band bound exceeds the square-root scale by a power of \(X\).

## Balancing and the one-sided norm

For the unpadded truncation let \(U=M(A)\), \(h_0=\sum_{a\le A}\mu(a)/a\)
and \(b^0\) be its convolution square. On the original slab the exact
centered sum is
\[
 M(N)=\sum_d b^0_d\psi_d(N)-(N+1/2)h_0^2+2U+U^2/2 .
\]
The constant is \((U+2)^2/2-2\), hence can have either sign.
It comes from the two linear truncation terms and from centering.
Replacing padded coefficients in a spectral projection does not
remove this cost in the full identity. A norm estimate on selected
components can pass to the positive part via its pointwise Lipschitz
bound only when the error has a two-sided norm bound or an applicable
one-sided domination. A bound on squared coefficients alone does not
justify discarding a mixed term between components on a finite slab.

## Opponent review of the two retained-family estimates

**candidate-D, same-session review.** In [BILINEAR-LOW.md](BILINEAR-LOW.md),
the last possible integer averaged from the slab is exactly
\(2X-1+J(H-1)=B_X-1\). Hence a raw denominator equal to \(B_X\)
belongs in the removable part. Each padded linear factor supplies the floor
sum one before multiplication by its signed coefficient. The padded square
supplies zero. This independently reproduces the term \(+2M(A)\) and
the constant \(+M(A)^2/2\). The subsequent removal of raw denominators
\(d\ge B_X\) works only with their own two allocated affine terms.
The surviving slope \(\sum_{d<B_X}b^u_d/d\) is signed.

For the prime-pair example, every proper divisor of \(p\ell\) is at
most \(A<D_1\) eventually. Thus projection retains only primitive
denominator \(p\ell\) from this raw pair. Conversely, no other product
of two positive integers at most \(A\) can be a multiple of \(p\ell\),
since the primes individually exceed \(A/2\). The example therefore
uses complete coefficients of the **unpadded** projected expression.
Its two lower bounds concern designated subintervals of a full slab
and its own oscillatory sum. The affine compensation precludes using
either as a lower bound for the original positive energy. The signed
factorization in (7) follows by choosing the first gcd, so it neither
omits nor double counts splits sharing a prime of a square denominator.

In [LOW-FREQUENCY-PAIRS.md](LOW-FREQUENCY-PAIRS.md), numerator cancellation
uses the actual balanced cofactor coefficient, which is independent of
the numerator. Freezing the masks before averaging over forward translates
preserves the single-interval condition. At exact resonance the modulus
divides the positive integer time. The nearest-multiple-zero case must
be split off since the divisor bound does not apply to zero. These give
the stated box bound. This argument adapts the separately credited
[neighboring numerator estimate](https://github.com/mathorn1973/twist-j/blob/f55cbcd1bf0eff6de99449c37ac8c03916b8acfe/notes/C-RH-ARITHMETIC-KERNEL-N/round5/NUMERATOR-ESTIMATE.md)
to a different coefficient and smoothing operator.

For the tapered crossing-pair estimate the two absolute heights differ
by at most \(64k\) in the determinant strip. Thus if one reaches
\(U\ge128k\), both are at least \(U/2\). This explains why the three
rectangles, with the distant and same-denominator removals, bound the
actual signed crossing terms. The separated-frequency estimate for
discarding individual numerator boxes gives a different conclusion:
it bounds the norm of their combined amplitude. In the absence of a
bound for the remaining amplitude this does not estimate its signed
cross energy with those boxes. For the one-sided comparison it suffices
to compare the two real amplitudes with the same drift and then use
the Lipschitz inequality for the positive part.

Each partially intersected slab has smaller squared error than the
complete slab in that comparison. Summing squared errors over slabs
with \(Y/2<X<Y^{3/2}\) (allowing equality at the lower endpoint also
gives a valid bound) works for every integer \(Y\), including when the
upper endpoint is an integer and therefore excluded. The subpower
allowance in the resulting norm comparison requires a strict exponent
margin, as supplied by using \(2r\) in the source condition. The
two investigations give separate comparisons with the original object;
applying both reductions to a new joint mask would require checking
the individual coordinate bounds on that mask. The full positive
late-window assertion remains **O**.

## Joint consequence for the unpadded coefficients

**candidate-D.** That coordinate check can be made for the two reductions
above. In the notation (6)–(8) of [BILINEAR-LOW.md](BILINEAR-LOW.md), set
\(C'_q=-qS_X(q)\). The raw mask has \(|b^{<}_d|\le\tau(d)\), hence
\[
 |C'_q|\le\tau(q)\sum_{j\le4A^2/q}\tau(j)/j\ll_\epsilon X^\epsilon .
\]
It is real and independent of the numerator. The box estimate (1) in
[LOW-FREQUENCY-PAIRS.md](LOW-FREQUENCY-PAIRS.md) applies verbatim after
this substitution: summation by parts is still performed before taking
the absolute value of the cofactor. The separated-frequency mass bound
for each box uses only \(|z_{a/q}|\ll_\epsilon X^\epsilon/|a|\), also
preserved. Apply that paper's height and box removals to \(P_X(b^{<})\).
Write \(G_X^{*,<}\) for the resulting amplitude, and retain exactly
the two affine terms from (6) of the bilinear note. Then
\[
 F^{<}(N)=G_X^{*,<}(N)-L_X(N)A_X+C_X/2,\qquad
 |\sqrt{Q_{F^{<}}(Y)}-\sqrt{Q_R(Y)}|\ll_\epsilon Y^\epsilon
\]
on each sufficiently late complete integer window. Here \(L_X\) means
the affine argument of the bilinear note, without a factor of \(h_X^2\).
The comparison follows by the squared norm of the deleted amplitude
on each slab, followed by both preceding same-window comparisons.
No sign of \(A_X\) or \(C_X\) is required. The subpower bound for the
positive energy of this joint surviving sum is **O**.

## Opponent review of logarithmic narrowing

**candidate-D, same-session review.** In [ONE-SIDED-LOW.md](ONE-SIDED-LOW.md)
the deleted raw terms split disjointly into all \(d\le D\) and the
\(q\le D_1\) modes from \(d>D\). Only the remaining \(d>D,q>D_1\)
modes enter the high-frequency error, with equality at \(1/h\) assigned
to that error. Neither the affine term nor any zero Fourier mode is
missing: each centered sawtooth has zero constant coefficient, while
the forward average translates the affine term by its exact mean.
Thus one may subtract the two versions of (4) with all raw and reduced
cuts accounted for.

At \(1\le h\|\theta\|\le5/4\) the ratio of sines is at most
\(\sqrt2/4<2/5\); above that range it is at most \(1/(2h\|\theta\|)\).
This validates (5) on the entire discarded high range, including the
cutoff. For a retained low-denominator harmonic of the removed sum
\(S\), the multiplier difference is at most a constant times
\(\min(1,Lv/q)\), by measuring each average against one. The sum of
its squared coefficient bounds over numerators is consequently
\(\ll_\epsilon X^{2\epsilon}(\log X)^2\min(1,L/q)\).
After summing over \(q\le D\), separation costs \(X+D^2\);
weight normalization leaves a squared bound of order
\(X^{-1/6+2\epsilon}\) times fixed logarithms. The gain uses the
multiplier *difference* on the shared removed frequencies.

The fixed-order short-sum estimate from the cited Theorem 1.1(i) applies
to each entire prefix length range through \(J(h-1)\). Integer
\(L\) ensures constant sets of sampled integers on each real unit cell,
even on the last starting cell. Summing squared slab errors over both
window fragments uses one logarithm, which the arbitrarily prescribed
fixed order absorbs before taking the square root. Thus the inverse-log
comparison concerns the two actual complete signed carriers with their
own shifted affine terms. It requires neither a uniform theorem for all
logarithmic powers simultaneously nor a bound on the size of either
carrier itself.

The cosine at \(1/A^2\) tests the information in nonnegativity on the
allowed frequency range. It assumes no nonzero arithmetic coefficient
there and fixes an artificial phase. It gives no lower bound for the
Möbius carrier or its positive energy. The outstanding positive
whole-window bound is **O**.
