# Root opposition of the short-sum spectral transfer

**NON-CANONICAL. No authority. Candidate-D, same-session paper review.**
Reviewed [SHORT-SPECTRAL-SCALES](SHORT-SPECTRAL-SCALES.md), the actual
round-five short-sum input and its primary MRSTT statement. No scientific
computation, source rerun or formal verifier was used.

The positive Jackson weights have the stated normalization and fourth
power tail. On I_X=[X/2,3X], shifts at most V=X^(1-eta) stay in the
interval where F_D has the actual first differences t. The starts and
lengths of the containing intervals fit the inherited short-sum theorem
with eta/2 after covering four dyadic start blocks. This uses a separate
norm bound for each shift length, not an unstated common exceptional
set. The norm triangle inequality with sum p_H(j) max(H,|j|)=O(H)
then has the stated logarithmic saving.

For the longer shifts the global bound on F_D gives a pointwise
O(|j|) difference, since the only shifts not already controlled by
|t|<=1 have |j| at least a constant times X. Its weighted tail is
O(sqrt X H^3/V^2); H/V<=X^(-eta) makes it negligible relative to
sqrt X H times each fixed inverse logarithm. Integer rounding changes
no endpoint regime. The theorem therefore applies on the whole I_X,
including all shifts needed in the subsequent taper argument.

For the annulus, Pi_H has support between 1/H and 2/H whereas J_(4H)
has support at most 1/(2H). The finite Fourier identity uses the zero
of the latter multiplier on the former's support and introduces no
inverse. The sum of absolute convolution coefficients is bounded.
For distant shifts, the ratio of the error to sqrt X H is bounded by
a constant times (H/X)^(M-2); M>=3 and the fixed margin in H give the
claimed savings. A telescoping sequence of scale bounds is geometric,
so this argument supplies no further power improvement by repetition.

I required a scope clarification in section 4. For fixed B, the new
compact cap 10X/H is asymptotically wider than the already frozen
round-five height cutoff sqrt X exp(-sqrt(log X)). The corrected text
defines an alternative series from the original round-four shell and
numerator restrictions plus the rough-conductor mask, before that
additional height trimming. Its equivalence uses a norm comparison.
The actual gain is the all-fixed-logarithm bound for the compact
smoothing error, not a claim to reduce the existing star spectrum
further. This clarification changes no scientific threshold or executed
test; there was no scientific execution.

The obstruction model is explicitly a different family for each X.
On the stated local interval its sine phases stay below pi/2 and the
derivative is O(c_X/log X). Flooring preserves a nonnegative integer
increment of size at most one. A progression sum of those increments,
even with arbitrary additive phases, is bounded by their total local
variation O(c_X h/log X+1). The exponential coefficient decay pays
every fixed logarithmic budget for polynomial h, while the low-frequency
energy exceeds X^(2+epsilon) for each fixed epsilon below one. This
does not give a counterexample for the actual t: its arithmetic
identities are expressly absent. It rules out inference from just the
specified short-sum and geometric inputs.

After the comparison clarification, I found no mathematical defect in
the displayed arguments. The full low-height signed estimate remains
open. The paper has no external independent confirmation.
