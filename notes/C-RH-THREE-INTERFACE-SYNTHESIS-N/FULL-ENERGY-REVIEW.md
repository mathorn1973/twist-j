# Opposition on the complete positive energy

**NON-CANONICAL. Authority none.** Status **candidate-D** for the paper deductions and **O** for the full positive bound. Action layer NOT_APPLICABLE. Same-session opposition for owner #2091, draft #2093.

## Levels and the nonnegative dual

In [FULL-LEVELS.md](FULL-LEVELS.md) the coefficient of the linear Taylor term is constant on each block. Weighted centering kills it exactly, even when the block contains both signs. The remainder for the squared positive part is between zero and the squared change because the derivative is 2-Lipschitz. This proves an additive energy error, which is stronger than applying only a norm comparison. For the residual the small variance uses the norm of the *difference* from the actual Möbius sequence in [WINDOW-BOUND.md](WINDOW-BOUND.md), (5); it does not follow from an inequality comparing two positive norms alone.

Every retained block lies in a single slab. A backward difference is the difference of two prefixes from the integer start \(N-L\), both of length at most \(L\); the shifted starts lie in the current or preceding slab. This proves the summed estimate without sampling sparse selected starts. The short-partition geometric series starts with a slab of size greater than \(Y/2\), also when \(Y\) is a power of two. The terminal integer is \(\lceil Y^{3/2}\rceil-1\). These observations validate both partial slabs and the estimates at both block lengths.

For the weak tail, \(t^2D_Y(t)\) is bounded by the full squared level mass, and on \(1\le t\le 2Y^{3/4}\) integration of \(dt/t\) costs one logarithm. The total normalized block weight also costs one logarithm. Thus the tail inequality must hold at all heights on the same windows. In the dual, the test is constant up to and including \(Y\); the split-off contribution through \(Y-1\) is correct. The inverse difference at the last integer uses the prescribed zero at the next integer. The model in that paper has derivative of size \(O(e^{-c\Phi(x)})\) before flooring. Each complete final log-period contains a positive arc of length at least \(\pi/3\) and a negative arc of that length. The positive arc lies inside the specified window eventually and survives discarding a terminal integer. This contradicts an inference from the modeled increment and size inequalities, without making any assertion about multiplicative coefficients.

## Coupled corner and a second signed square

The convolution in [FULL-COUPLED-ENERGY.md](FULL-COUPLED-ENERGY.md) uses both mixed rectangles and the unit identity before taking any positive part. The short rectangle's intercept is the square of its entire mass divided by two, plus twice its mass. For the fourth-root cutoff it costs bounded slab norm. At the cube-root cutoff the intercept must still be retained under the estimates used there. The negative slope is unchanged by the shift except for the mean displacement. The geometric separation of the two model intervals is strict uniformly throughout the stated forward average. The model's interval bound is relative to its support scale, not relative to the length of each tested interval.

**Candidate-D.** There is another square of known sign *inside* the full corner. For each integer \(n\) in the forward average expand the floor using \(1\le k\le\lfloor n/(T+1)^2\rfloor\). Set \(x=\lfloor n/k\rfloor\), \(t=\lfloor\sqrt{x}\rfloor\) and \(D_T(m)=M(m)-M(T)\). Then
\[
 C_T(n)=\sum_k\left(
 2\sum_{T<a\le t}\mu(a)D_T(\lfloor x/a\rfloor)-D_T(t)^2
 \right).
\]
Every admissible pair has at least one coordinate at most \(t\); the intersection of the two oriented sets is the entire square \(T<a,b\le t\). This counts each pair once, including square and exact product endpoints. The formula supplies a sufficient estimate using the positive energy of the oriented sums alone, by dropping both nonpositive penalties after averaging. The proved equivalence retains both penalties. Neither a size bound on each prefix nor positivity of the dual implies the requisite upper bound.

Indeed fix \(5X/4\le N\le 13X/10\) and the three integer indices nearest to \((19/20)\sqrt X,(61/50)\sqrt X,(33/20)\sqrt X\), respectively. For all large slabs and all forward shifts, the symmetric floor matrix on these indices is
\[
 \begin{pmatrix}1&1&0\\1&0&0\\0&0&0\end{pmatrix}.
\]
The first diagonal product stays above half the largest shifted argument, both first-row products in the first two columns stay below the smallest argument, and the products involving the last index or the second diagonal exceed every shifted argument. Thus even a nonnegative dual supported throughout this interval and normalized to have unit weighted norm gives this matrix multiplied by a positive scalar. On the zero-total-mass coefficient subspace its quadratic form takes the values \(-1\) at \((1,-1,0)\) and \(+1\) at \((1,0,-1)\) before that scalar. All indices exceed the fourth-root cutoff, so the short-factor slope vanishes for these model inputs. This excludes a sign deduction from dual nonnegativity and coefficient balance. It makes no assertion about the value at the actual Möbius vector. The required all-height bound for those arithmetic coefficients is **O**.

## Asymmetric row boundary

In [LOWEST-MODES.md](LOWEST-MODES.md) a selected row has \(1\le \lfloor n/a\rfloor<2A\). Each omitted second factor through that quotient contributes a floor of exactly one, including equality at the quotient. For \(n\le B_X-AU\) none is omitted because each chosen first factor strictly exceeds \(B_X/A-U\). With maximum shift \(B_X-2X\), the averaged error is confined to the final \(O(A(U+1))\) starts. The compensated deletion uses its own signed affine coefficients. Rounding the cap down changes the unrounded raw endpoint by less than \(A\).

A band of width \(V\ge1\) at depths up to \(jV\), \(j\ge1\), has missing-floor amplitude \(O((V+1)jV)\) on \(O(AjV)\) starts. Summing the norms of these nested contributions through \(j=\lceil U/V\rceil\) costs \(O(A^{1/2}(U+V)^{5/2}/X)\). At \(U=X^{3/10}\) the single-cut allowance is bounded. At \(U\asymp A\) the allowance grows as \(X^{1/2}\). These are costs of the upper estimates, not lower bounds on the actual loss. The unrestricted single-cap identities used for inclusion-exclusion require \(n\ge A\), as holds throughout the forward averages.

## Recursion with genuine divisor coefficients

The regrouping \(j=ka\) in the hyperbola formula imposes exactly \(a\mid j\) and \(T<a\le n/j\). Each surviving divisor automatically obeys \(k(T+1)^2\le n\). The overlap squares only use arguments at most \(\sqrt n\). For a prime \(p\in[2T,4T]\) and \(n\asymp X\), \(T=\lfloor X^{1/4}\rfloor\), the only retained divisor of \(p\) is \(p\) and its coefficient is exactly \(-1\).

At integer arguments \(X\le n\le X+X/(1000P)\), \(P=2T\), the distance from \(n/j\) to \(X/p\) exceeds \((1-2/1000)X/[p(p+1)]\) or equals this lower bound for \(j\ne p\). One unit of rounding leaves a distance larger than the pulse radius. At \(j=p\) the distance after rounding is at most half the radius. The supports lie above \(\sqrt{2X}\), are mutually separated, and all forward shifts from the smaller test interval remain in the larger one. This verifies simultaneous isolation of the prime columns. The number of starts is of order \(X/P\), each with weight of order \(X^{-2}\); the fixed-coefficient corner therefore has the claimed lower energy. Taking \(Y=X\) supplies a complete window containing the entire test interval. Discarding its at most two intersected end blocks leaves the same order of weight since either block length is \(o(X/P)\).

The coefficients of this operator are genuine Möbius divisor sums, but the substituted nonpositive prefix state does not have those Möbius increments. In particular the lower bound is for the model corner before subtracting the true short-factor drift. The drift and overlap squares are unchanged by adding these pulses to a fixed base state, but the absolute positive energy after subtracting the drift need not inherit a lower bound on the change. No positive lower bound on the actual residual follows. The full positive arithmetic bound remains **O**.

For the slowed model the nonnegative triangular tents have disjoint interiors, so their sum has global Lipschitz constant one, including across the gaps. Scaling by \(\delta_X\) and flooring changes each difference bound to \(\delta_X s+1\). For \(V\asymp X/P\), polynomially long \(h\) makes \(h^{-2}\) smaller than every inverse power of \(\log V\), as is \(\delta_X^2\). This proves the claimed all-start bound for ordinary prefixes. Since \(\delta_X L\to\infty\), rounding cannot cancel the central pulse levels, and the squared lower estimate acquires the factor \(\delta_X^2=X^{-o(1)}\). The support envelope follows even for arbitrary fixed \(c>0\) because \(L/t\ll1/P\) there. The statement concerns a separate model for each slab. It establishes neither cancellation of twisted sums of the model increments nor a positive-energy lower bound for the actual arithmetic carrier.


## Direct vanishing comparison of the complete corner carrier

Root's stronger comparison in FULL-COUPLED-ENERGY.md follows from its exact difference identity with M. At the fourth-root cutoff the squared intercept norm is bounded by a constant times exp(-4c Phi(T)) plus X^(-1/2) exp(-2c Phi(T)); the slab weights sum exactly to 1/(2X). The centered small rectangle has the stated power-saving norm. The total forward shift J(H-1) is in the short-prefix theorem's admitted range, including all original starts near the right edge, and the frozen arithmetic identity is valid at all translated arguments. Squared bounds on complete slabs dominate their restrictions to both partial window ends; summation costs only fixed logarithms. The error M-R already has faster decay than every fixed inverse logarithmic power. This verifies the norm comparison for the actual complete carrier, without a model or an RH input.

The comparison also gives the claimed positive square-root comparison and, by contraction of 1-P, additive approximation of Q_Z by its own block energy S_Z. It does not imply an additive inverse-log bound on Q_Z-Q_R: that difference additionally contains the potentially large sum of the positive norms. The absolute level target remains O.
