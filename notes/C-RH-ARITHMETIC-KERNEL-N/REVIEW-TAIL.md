# Opposition review of the rough tail and the window transfer

**NON-CANONICAL. Working verdict: candidate-D for the stated arithmetic consequences, O for the complete tail estimate.** Independent paper reconstruction of sol_arithmetic/ROUGH-TAIL.md and WINDOW-TAIL.md. I did not inspect either author's implementation. To distinguish the notation of the two sources, write L for the short contribution d³≤X², B for the rough contribution in the long range, H_mix for the complementary mixed contribution, and h(j) for the partial character sum.

## Exact cutoffs and the signed kernels

The two kernels occur at different stages. Grouping by k=⌊X/d⌋ uses h(k). Expanding that same h(k)=Σ_{j≤k}χ(j) and interchanging sums uses χ(j). In the long range d>X^(2/3), the last eligible integer j is strictly below Z=X^(1/3). For integral Z the j=Z term therefore never occurs. Three primes greater than Z have product greater than X, and two such primes have product greater than Z². Consequently the rough split squarefree d consist precisely of a prime above D or a pair p<q above Z. Subtracting π_split(p) includes the exclusion of the diagonal. For the mixed terms p is the unique least factor; e=d/p has no prime ≤p, and the lower endpoint D/p is to be subtracted inclusively. These give exactly (1) and (2) in the rough note.

## The logarithm and the uniform quotient tail

For fixed j, write y=X/j and sum over Z<p≤√y. The subtraction Σπ_split(p) is O(π(√y)²)=O_j(X/log²X). At y/p≥√y the fixed-modulus prime number theorem supplies its asymptotic uniformly for all the p in this fixed-j sum. Its outer prime density is 1/2, and the reciprocal-prime measure in v=log p/log X has limiting density dv/(2v). Thus (log X/X)N₂(y;Z) tends to

    (1/(4j))∫_{1/3}^{1/2} dv/[v(1−v)] = log(2)/(4j).

The already ordered sum has no additional symmetry factor. Multiplicity four from the arithmetic coefficient gives the signed semiprime contribution +log(2)/j. The corresponding prime contribution is −1/j. The moving upper endpoint differs from 1/2 by o(1) in v and the reciprocal-prime mass near that endpoint is uniformly small by the same fixed-modulus PNT.

A relative PNT error uniform in j up to Z was not assumed. Cut the χ-sum at a fixed integer Q first, then recombine by d. The difference of two partial character sums has absolute value at most two; it vanishes unless d≤X/(Q+1). With D≤y≤X, the number of eligible rough primes is O(y/log X). For semiprimes use y/p≥√y≥X^(1/3) and the bounded reciprocal-prime sum over X^(1/3)<p≤X^(1/2). This bounds their count too by O(y/log X), uniformly in y. The weights two and four are harmless. When y<D the tail is empty. This proves the uniform O(X/((Q+1)log X)) remainder and justifies taking X→∞ at fixed Q, then Q→∞. It gives B(X)∼−(1−log 2)L(1,χ)X/log X. The individual five-term blocks of Σχ(j)/j are positive, hence the constant is strictly positive.

## What supplies the complementary positive obstruction

The positive sign of H_mix requires the separate estimate T(X)=o(X/log X). It is obtained from the exact transfer coefficients v of U^(−1) and the unconditional de la Vallée Poussin form of the ordinary Mertens bound, verified in [Lee–Leong, Theorem 1.1](https://arxiv.org/html/2208.06141v4#Thmtheorem1.1). On d≤√X, M(X/d) incurs exp(−c√log X) after adjusting c, and Σ|v(d)|/d is finite. On d>√X use d^(−1)≤X^(−1/8)d^(−3/4) and |M(X/d)|≤X/d to obtain O(X^(7/8)). The elementary bound |L(X)|≤D follows from |w|≤1*χ coefficientwise and Σ_{a≤D}h(⌊D/a⌋)≤D. Therefore H_mix=T−L−B is asymptotic to +(1−log 2)L(1,χ)X/log X. This yields positive square energy ≫Y²/log²Y by summing only over the upper half of the window. B itself is eventually negative. Bounding the positive parts separately destroys the cancellation. The fixed-modulus prime number theorem alone supplies the prime and semiprime main terms; the cited unconditional Mertens rate plus the convolution unit supply the complementary positive asymptotic. Both are classical unconditional inputs.

## Quotient statistic and equal-window comparison

The floor identity in WINDOW-TAIL, including its use of max(D_n,⌊n/(k+1)⌋), is exact. Since D_n+1>n^(2/3) one has K_n<n^(1/3), also at perfect cubes. The reverse triangle inequality and the positivity map's Lipschitz constant one compare the square roots of Q_T and Q_R on precisely the same window. The O((1+log Y)²) difference follows from the fourth-power short-support square bound. Using exponent 2r for the given side absorbs the implicit constant and logarithm on each sufficiently late witness. Clearing denominators via lcm(Y,…,Y²) is valid by adjacent coprimality. The isolated prime component in WINDOW-TAIL uses the absolutely convergent series Σ h(k)/[k(k+1)] and fixed-modulus PNT, with no Mertens estimate required for that component. Summation by parts identifies this series with L(1,χ). The earlier RH/window equivalence is an independent imported dependency of the last equivalence. The present arithmetic step supplies no good window for R on its own.

The reviewed proofs stand. When combining their statements, distinguish the two uses of the letter B and explicitly attribute the Mertens rate in the positive-complement conclusion. No numerical experiment or theorem-prover build forms part of this review.
