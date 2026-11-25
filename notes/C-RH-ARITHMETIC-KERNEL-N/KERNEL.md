# A quadratic bound through the support boundary d³ ≤ n²

**NON-CANONICAL, no authority. C-RH-ARITHMETIC-KERNEL-N.** Working status **candidate-D** for the deductions below and **O** for the unrestricted arithmetic estimate. The method uses an elementary form of the additive large sieve. No assertion of historical novelty is made.

Let χ be the quadratic character modulo five, H(k)=Σ_{j≤k}χ(j) for integers k≥0, and K_d(n)=H(⌊n/d⌋). The period-five values of H are (0,1,0,−1,0), in residue order 0 through 4. Put s(d)=(−2)^ω(d) on squarefree products of primes congruent to ±1 modulo 5, including s(1)=1, and zero otherwise. Define the contribution L(n)=Σ_{d³≤n²}s(d)K_d(n).

**Theorem (candidate-D).** For every integer Y≥2,

    Σ_{Y≤n<Y²} |L(n)|² / [n(n+1)]  ≪  (1+log Y)^7.

The implicit constant is absolute. One may replace s(d) by any fixed coefficients c_d supported on the same integers and satisfying |c_d|≤|s(d)|. This includes the true, unmodified coefficients. The cutoff is a function of n throughout the proof.

## 1. Exact complete mean (candidate-D)

For positive d,e coprime to 5, let g=(d,e), a=d/g, b=e/g. With the average over the common period 5 lcm(d,e),

    mean K_d K_e = (2/5) χ(a)χ(b)/(ab).

Writing n=gm+t for 0≤t<g reduces the mean to that of K_a(m)K_b(m) for 0≤m<5ab. The pairs of residues modulo 5a and 5b run exactly once through all pairs with equal residues modulo 5, since gcd(a,b)=1. For any residue r modulo 5 put

    H_a(r)=Σ_{0≤m<5a, m≡r mod5} K_a(m).

The positive interval is [a,2a) and the negative interval is [3a,4a). Removing complete strings of five residues leaves, for a≡1,2,3,4 respectively, the five vectors H,−H,−H,H. Thus H_a(r)=χ(a)H(r). Summing H_a(r)H_b(r) over the five residues proves the formula because ΣH(r)²=2. For the nonzero split coefficients χ(a)=χ(b)=1, so every cross-kernel is positive. Full-period orthogonality already fails for distinct split supports.

For any finite supported linear combination write its complete mean square as E(c), using the common multiple of its periods. The exact result above identifies

    E(c) = (2/5) Σ_{d,e} c_d conjugate(c_e) gcd(d,e)²/(de)
         = (2/5) Σ_h J₂(h) |Σ_{h|d} c_d/d|²,

where J₂(h)=h² ∏_{p|h}(1−p^(−2)); the second equality follows from Σ_{h|g}J₂(h)=g². Each inner sum ranges over the finite support. For the full divisor cube of a finite set P of split primes with c_d=s(d), the answer factors exactly as (2/5)∏_{p∈P}(5−4/p). This calculation contains the off-diagonal terms with their arithmetic signs.

## 2. An absolute complete-mean bound (candidate-D)

For D≥1 and |c_d|≤|s(d)|, support d≤D, the sum of absolute values of all terms of the double sum, including its 2/5 factor, is ≪D(1+log D)^3. Call this nonnegative absolute sum E_abs. Indeed |s(d)|≤τ(d), where τ counts divisors. Group d=ga, e=gb by their exact gcd g, drop (a,b)=1 for an upper bound and use τ(ga)≤τ(g)τ(a). Since Σ_{a≤M}τ(a)/a≤(1+log M)² by summing 1/(uv), it suffices to bound

    Σ_{g≤D} τ(g)² (1+log(D/g))⁴.

The prime-power inequality (k+1)²≤binom(k+3,3) gives τ(g)²≤τ₄(g), the number of ordered quadruple factorizations. Summing over the first three variables gives Σ_{g≤u}τ₄(g)≤u(1+log u)³. On D/2^(j+1)<g≤D/2^j the fourth-power weight is at most (1+(j+1)log2)⁴. Summing the factor 2^(−j)(1+j)⁴ proves the bound. The estimate on E_abs controls the sum of complete energies of multiple *disjoint* d-blocks without multiplying by their number.

## 3. From complete mean to finite intervals (candidate-D)

A trigonometric sum f(n)=Σ_t b_t exp(2πint), written with distinct frequencies modulo 1 of reduced denominators ≤5D, has gaps ≥δ=(5D)^(−2) on the circle. Its complete mean square is Σ_t|b_t|², by character orthogonality on a common period. This uses no upper bound on that period. On X consecutive integers,

    Σ_n |f(n)|² ≤ C [X+D²(1+log(2D))] Σ_t |b_t|².               (1)

To see this directly, form the frequency Gram matrix. A diagonal entry equals X. A nondiagonal entry has absolute value at most 1/(2||t−t'||) by the finite geometric sum; ||·|| is distance to the nearest integer. On either side of a frequency the j-th neighbor within circular distance 1/2 is at least jδ away. There are O(D²) frequencies, since this also follows from spacing. The absolute row and column sums are O(X+δ^(−1)(1+log(2D))). Apply 2|b_t b_t'|≤|b_t|²+|b_t'|² to the expanded norm. Each K_d is periodic modulo 5d, so every linear combination with d≤D has just such a finite Fourier expansion after identical frequencies are combined.

## 4. Moving cutoff and the logarithmic loss (candidate-D)

On the integer block X≤n<2X let D=⌊(2X)^(2/3)⌋ and pad the coefficient array by zeros over D<d≤2^J, J=ceil(log₂ D). For any n in the block, the prefix 1≤d≤⌊n^(2/3)⌋ is the disjoint union of at most J+1 aligned binary intervals, at most one of each length. By Cauchy–Schwarz at that n,

    |L(n)|² ≤ (J+1) Σ_{all aligned binary intervals I} |Σ_{d∈I} c_d K_d(n)|².

For each of the J+1 lengths the intervals I partition the padded array. The sum of their complete energies E(c 1_I) is at most E_abs from §2, since all retained d,e terms lie in disjoint within-block squares and their absolute values are bounded by the common majorant. Apply (1) on the n-block to every binary interval and sum *after* this complete-energy observation. Hence

    Σ_{X≤n<2X} |L(n)|²
      ≪ (1+log(2D))² [X+D²(1+log(2D))] D(1+log D)³
      ≪ X²(1+log(2X))⁶.

Indeed D≤(2X)^(2/3), so XD≪X^(5/3) and D³≪X². Divide each block by X² to bound the desired weighted sum. Use integer blocks starting at Y,2Y,4Y,… until Y², enlarging the final incomplete block if needed. There are O(1+log Y) blocks and each starting point is ≤Y². This proves the theorem. The comparison for arbitrary coefficient masks holds because their entire common majorant was fixed before the prefix argument.

## 5. Sharpness of the support threshold for uniform masking (candidate-D)

For any fixed 2/3<a<1, let D=⌊X^a⌋. For every sufficiently large X there exists a subset P of the split primes in [D,2D] such that

    Σ_{X≤n<2X} (Σ_{p∈P} s(p)K_p(n))_+²/[n(n+1)]
       ≫ D³/[X²(log D)²].

By the prime number theorem for the two fixed residue classes modulo 5, there are ≫D/log D eligible primes. Average x₀ over integers [X,3X/2]. For a given such prime p, the desired residue condition is 3p≤x₀ mod 5p<3p+⌊p/2⌋. Because X/D tends to infinity there are many complete periods, so at least an absolute positive fraction of these x₀ satisfy it, uniformly in p. Interchange the counts. Some single x₀ satisfies the condition for ≫D/log D primes; take precisely those. For every integer h with 0≤h≤⌊D/2⌋ the residue x₀+h mod 5p lies in [3p,4p), since p≥D. Thus K_p(x₀+h)=−1 and s(p)=−2, giving a *positive* sum 2|P| for an interval of length ≫D. This interval is inside [X,2X) eventually. Its weighted square proves the assertion. For a uniform theorem whose moving upper limit is n^a, use instead primes in [D/3,2D/3] and h≤D/7; the same orders of magnitude hold and all terms satisfy p≤n^a.

The lower bound grows as a positive power of X when a>2/3. This rules out a subpower estimate uniform over arbitrary masks beyond this threshold; the selected subset depends on X. It gives no lower bound for the complete signed s(d) sum and does not rule out cancellation that uses its arithmetic coefficients across different supports. For the fixed-modulus prime number theorem used only in §5, see [Kedlaya, theorem on primes in progressions](https://kskedlaya.org/ant/chap-primes-in-ap.html).

## 6. Remaining arithmetic task (O)

For the full T(n)=Σ_{d≤n}s(d)K_d(n) its complementary range is d³>n². Put D_n=⌊n^(2/3)⌋, S(x)=Σ_{d≤x}s(d). The complement equals the finite exact expression

    Σ_{k≤⌊n/(D_n+1)⌋} H(k) [ S(⌊n/k⌋) − S(max(D_n,⌊n/(k+1)⌋)) ].

The quotient k is <n^(1/3). The unconditional theorem controls the discarded part of the positive square root of the weighted energy by O((1+log Y)^(7/2)), by the triangle inequality and the Lipschitz property of u↦u_+. An independent proof of sufficiently small energy on arbitrarily late windows for the actual complementary sum remains open.

## 7. Sharpened bound for the signed split support (candidate-D)

The theorem in fact holds with the fourth power of 1+log Y in place of the seventh. The previous proof is kept to separate the weaker divisor-only estimate from the extra information recoverable from the split support.

Let f=1*χ, which is nonnegative by its prime-power factors. Its summatory function obeys 0≤Σ_{n≤u}f(n)=Σ_{a≤u}H(⌊u/a⌋)≤u. Hence Σ_{n≤u} f(n)/n≤1+log u by partial summation. At every squarefree split d one has f(d)=|s(d)| and (f*f)(d)=s(d)². Elsewhere f and f*f are nonnegative, so these identities give global majorants. In particular

    Σ_{g≤u} |s(g)|² ≤ Σ_{d≤u} f(d) Σ_{b≤u/d}f(b)
                    ≤ u(1+log u).

In the gcd grouping one has |s(ga)|≤|s(g)s(a)|, including the case of a repeated prime, where the left side vanishes. Therefore

    E_abs ≪ Σ_{g≤D}|s(g)|²(1+log(D/g))² ≪ D(1+log D).

The last step uses the dyadic sum in §2 with weights 2^(−j)(1+j)². This estimate remains true for arbitrary coefficient masks below |s|.

The log factor in (1) can also be dropped. Here is a directly proved version with an absolute constant. By finite-dimensional Hilbert-space duality it suffices to bound Σ_t|P(t)|² for P(t)=Σ_{j=0}^{X−1}a_j exp(2πijt) by O(X+δ^(−1))Σ_j|a_j|². Shifting the starting time by an integer changes the sample by a phase of modulus one. Use pairwise disjoint circle intervals I_t of length δ centered at the distinct sample frequencies. For nonnegative G=|P|² the fundamental theorem of calculus gives G(t)≤δ^(−1)∫_{I_t}G+∫_{I_t}|G'|. Summing and using Parseval and Cauchy–Schwarz gives

    Σ_t |P(t)|² ≤ δ^(−1)||P||₂²+2||P||₂||P'||₂
                 ≤ (δ^(−1)+4πX)||P||₂².

With δ=(5D)^(−2), the prefix argument of §4 now bounds the n-block square sum by O((1+log(2D))² (X+D²) D(1+log D)). For D≤(2X)^(2/3) this is O(X²(1+log(2X))³). Summation over the n-blocks proves

    Σ_{Y≤n<Y²} |L(n)|²/[n(n+1)] ≪ (1+log Y)⁴.

The difference in the square roots of the unrestricted and complementary positive-part energies in §6 is thus O((1+log Y)²). This is a uniform logarithmic bound for the moving short support; no cancellation of signs in s was assumed in the norm upper bound.

## Prior sources and scope

Project issue [1931](https://github.com/mathorn1973/twist-j/issues/1931) already uses a gcd-square covariance, a Jordan-totient divisor-square representation and an additive large sieve for periodic remainder functions. Issue [1948](https://github.com/mathorn1973/twist-j/issues/1948) already uses a weighted gcd-square bound and the same large-sieve transfer for logarithmically weighted Möbius coefficients. Published antecedents include [Montgomery and Vaughan, The large sieve](https://doi.org/10.1112/S0025579300004708) and [Aistleitner, Berkes and Seip, GCD sums from Poisson integrals and systems of dilated functions](https://ems.press/journals/jems/articles/12412). The present calculation applies this methodology to the exact five-residue kernel, signed split support, integer moving cutoff and the one-sided rational statistic. Its masked lower bound describes an obstruction to a uniform extension of this particular estimate.
