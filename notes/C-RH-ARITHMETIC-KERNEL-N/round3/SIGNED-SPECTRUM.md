# The true signed spectrum and the frequencies left by square-root smoothing

**NON-CANONICAL. No authority. Working status candidate-D for the paper deductions, O for a sufficient arithmetic estimate on the remaining signed sum.** This continuation uses the signed split coefficient s(d), the character χ modulo five, its partial sum H and K_d from the preceding KERNEL. No numerical computation or claim of priority. Write e(t)=exp(2πit).

## 1. Exact rational decomposition

For an integer D≥1 freeze F_D(n)=Σ_{d≤D}s(d)K_d(n) for every integer n, extending H periodically. Write

    Φ_r(n)=Σ_{h|r} μ(h)χ(h)K_{r/h}(n)/h,
    A_r(D)=s(r) Σ_{m≤D/r, (m,r)=1} s(m)/m.

Only squarefree split r contribute. Dirichlet inversion on divisors gives

    F_D(n)=Σ_{r≤D} A_r(D) Φ_r(n).                                  (1)

Indeed K_d=Σ_{r|d}χ(d/r)(r/d)Φ_r. For rm squarefree split, χ(m)=1 and s(rm)=s(r)s(m); all incompatible pairs contribute zero.

The Fourier expansion of Φ_r has support precisely at the primitive frequencies a/(5r), (a,5r)=1. With a the signed representative in (−5r/2,5r/2], its coefficient there is

    b(r,a)=τχ(a)/[5r(1−e(−a/(5r)))],    τ=Σ_{j mod 5}χ(j)e(−j/5),  (2)

where |τ|=√5 by the elementary quadratic Gauss sum. To check (2) directly, ΔK_d(n)=K_d(n)−K_d(n−1)=1_{d|n}χ(n/d). Its Fourier coefficient at h/(5d) is τχ(h)/(5d). Multiplying a Fourier coefficient by 1−e(−h/(5d)) gives the coefficient of Δ. The zero frequency of K_d vanishes and nonzero h divisible by five give zero as well. If a/(5r) is in lowest terms, its contribution to K_d exists only for r|d and equals χ(d/r)(r/d)b(r,a). This proves the assertion and formula (1) simultaneously. In particular |b(r,a)|≪1/|a| with an absolute constant.

Distinct Φ_r with 5∤r are orthogonal over a complete period by disjoint Fourier support. For these conductors their squared norms under the normalized period mean are (2/5)J₂(r)/r², where J₂(r)=r²∏_{p|r}(1−p^(−2)). This includes every supported r. In fact for 5∤d the mean of K_d² is 2/5, and its orthogonal divisor decomposition gives Σ_{r|d}r²||Φ_r||²=(2/5)d²; ordinary Möbius inversion gives the formula. In contrast to individual Fourier components, both A_r and Φ_r in (1) are rational.

## 2. Complete variance really has order D log D for the unmasked signs

Put f=1*χ, c=L(1,χ)>0 and w(n)=s(n)². The Dirichlet coefficients h determined by w=h*f*f have Euler factors

    (1+4t)(1−t)⁴ (split),   (1−t²)² (inert),   (1−t)² (p=5),    t=p^(−s).

The series of |h(n)|/n^σ converges for σ>1/2. The product h̃(1)=Σ h(n)/n is strictly positive: every local factor is positive at t=1/p and the deviations are absolutely summable. Dirichlet's hyperbola argument using |H|≤1 gives Σ_{n≤x}f(n)=cx+O(√x): split at √x, replace the floor in Σ_{b≤√x}χ(b)⌊x/b⌋, and bound the other strip and its intersection by O(√x). The tail of Σχ(b)/b is O(1/√x). Since f≥0, partial summation then gives Σ_{n≤x}(f*f)(n)=c²x log x+O(x), by summing f(m)[cx/m+O(√(x/m))]. Convolving with h yields

    Σ_{n≤x} s(n)² = Cx log x+O(x),    C=c²h̃(1)>0.                (3)

Absolute convergence at 3/4 controls the discarded tail of h(n)/n even after multiplication by log x, and Σ|h(n)|log(n)/n is finite.

Since 11 is the first split prime, A_r(D)=s(r) for D/11<r≤D. As J₂(r)/r²≥1/ζ(2), (1) and (3) give ||F_D||²_mean≫D log D. The matching upper bound is §7 of the preceding KERNEL, since that bound already holds for the absolute gcd double sum. Thus

    ||F_D||²_mean ≍ D log D  (D→∞).                              (4)

The actual nonzero frequencies also have minimum spacing ≍D^(−2). The lower bound follows from denominators ≤5D. For the upper bound take two distinct split primes r,s in (D/2,D], available by the fixed-modulus PNT. All their primitive modes are present, since A_r=A_s=−2. Choose integers a,b with as−br=1. Adding (kr,ks) to (a,b) leaves this identity unchanged. Modulo five at most two classes of k are forbidden to make both numerators coprime to five. They are already coprime to r,s respectively. Their frequencies on the circle are separated by 1/(5rs). Consequently the standard large-sieve expression (X+δ^(−1))||F_D||²_mean has order (X+D²)D log D even with the genuine arithmetic signs. This is a proved limitation of that expression. It does not imply an incomplete-interval lower bound for F_D.

## 3. The exact first difference of the actual sum

Let T(n)=Σ_{d≤n}s(d)K_d(n). For 1≤n≤D, (1) agrees with T(n), and ΔF_D(n)=(s*χ)(n). The latter coefficient is multiplicative. At a split prime its local series is (1−2t)/(1−t), with every positive-degree coefficient −1. At an inert prime it is (1+t)^(−1); at 5 it is 1. Thus |ΔF_D(n)|≤1 on this range. Moreover |F_D(n)|≤Σ_{d≤D}|s(d)|≤D on *all* integers by the preceding KERNEL, §7.

For a dyadic integer X≥64 set D=4X and t=X^(−1/2). On the frequency circle let w_t(α)=(1−||α||/t)_+ and m_t=(w_t*w_t)/(w_t*w_t)(0) with normalized circle convolution. It is real and even, bounded by one via Cauchy–Schwarz, and vanishes for ||α||>2t. Its Fourier coefficients are

    p_j=(3t/2) sinc(πjt)^4,     sinc(z)=sin(z)/z, sinc(0)=1.

Indeed ŵ_t(j)=t sinc(πjt)^2 and ∫w_t²=2t/3. Thus p_j≥0, Σ_j p_j=m_t(0)=1 and p_j≪t(1+t|j|)^(−4). In particular Σ|j|p_j≪1/t and Σ_{|j|>X}p_j≪(tX)^(−3). The finite Fourier expansion of the periodic F_D shows that smoothing to Σ_j p_j F_D(n−j) multiplies frequency α by m_t(α). For X≤n<2X and |j|≤X all intermediate differences between n and n−j occur in [1,D]. The rest costs at most 2D per shift. Therefore on the entire block the pointwise error from retaining this smoothed frequency sum is

    O(t^(−1)+D(tX)^(−3))=O(√X).                                  (5)

This bound uses the arithmetic signs in the exact first difference. Neither positivity nor a finite support of the time shifts was assumed implicitly; their tail and the global bound on F_D appear in (5).

## 4. An explicit remaining signed sum

Partition the positive conductor sizes above R₀=X^(2/3) into shells (R,2R] for R=2^j R₀, j≥0, stopping at D. In such a shell put H_R=max(1,ceil(R³/X²)). For X≤n<2X define

    G(n)=Σ_{shells R} Σ_{R<r≤min(2R,D)} A_r(D)
          Σ_{(a,5r)=1, 0<|a|≤min(H_R,10r/√X)}
               b(r,a) m_t(a/(5r)) e(na/(5r)).                    (6)

Use signed representatives as in (2). The conjugate pairing makes G real. On the finitely many n<64 put G(n)=T(n). The global definition uses the unique dyadic block containing n, independently of the window Y later tested. This trigonometric sum is an analytical residual, not an integer-valued replacement for T.

**Candidate-D.** Uniformly for integers Y≥2,

    Σ_{Y≤n<Y²}|T(n)−G(n)|²/[n(n+1)] ≪ (1+log Y)^6.              (7)

For the proof, |A_r(D)|≤|s(r)|(1+log(D/r)), since Σ_{m≤V}|s(m)|/m≤1+log V. Equations (3) or the earlier majorant imply Σ_{r≤U}|A_r|²≪U(1+log D)^3 for U≤D. The same bound holds on a shell (R,2R] with U replaced by 2R. By (2), summing squared coefficients over |a|>H≥1 costs ≪|A_r|²/H, and summing over all a costs ≪|A_r|². The multipliers m_t have modulus at most one. Among primitive denominators ≤5U the spacing is ≫U^(−2). The additive large sieve proved in KERNEL §7 thus gives an ordinary square sum on X≤n<2X bounded by

    O((X+R₀²)R₀(1+log D)^3) = O(X²(1+log D)^3)

for all discarded small conductors together. For a shell R≥R₀, the discarded modes with |a|>H_R have square sum

    O((X+R²)R(1+log D)^3/H_R) = O(X²(1+log D)^3).

The other discarded modes have multiplier zero by construction. There are O(1+log X) shells. The triangle inequality for the norms, then squaring, costs O((1+log X)²). Adding (5) yields O(X²(1+log X)^5) for the block square sum. Cover [Y,Y²) by its intersecting dyadic blocks and use n(n+1)≥X² on each. This proves (7). The number of retained frequencies is O(X^(3/2)) by summing O(r/√X) over r≤4X; the full denominator frequency list has upper bound O(X²).

Consequently |√Q_T(Y)−√Q_G(Y)|≪(1+log Y)^3 by the positive-part Lipschitz inequality, using the same weighted sum definition for real G. Arbitrarily late subpower good windows for T and G are equivalent by the exponent slack 2k versus k. The original exact rational window remains available for T. One purely rational reduction also follows directly: keep every Φ_r with r>R₀ in (1), without frequency smoothing or numerator cuts. The discarded small Φ_r have the same O(X²(1+log D)^3) block square bound just proved using multiplier one. This rational version keeps a different and larger set of modes.

**O.** The high-conductor low-numerator block (6) contains actual signed near-collisions between different r. The universal estimate proved here removes the complementary frequencies. Neither (4) nor the frequency count supplies a bound on the surviving incomplete energy. The norm and minimum spacing in §2 are both genuine, so their global estimates cannot substitute for arithmetic information on these remaining pairs. The gcd kernel, the additive large sieve, Möbius inversion, quadratic Gauss sums and the positive fourth-power smoothing are classical tools; the claimed deductions concern their application to this fixed coefficient and cutoff.

### 4.1. The equivalent same-block target

Fix each dyadic X≥64 and use precisely the parameters and weights of (6) on that block. Write z_θ=A_r(D)b(r,a)m_t(θ) at each retained θ=a/(5r), g_{X,r}(n)=Σ_{θ of conductor r}z_θ e(nθ), and J_X(y)=Σ_{n=X}^{2X−1}e(ny). Put

    E_X=Σ_{X≤n<2X}|G(n)|²,      E_{X,r}=Σ_{X≤n<2X}|g_{X,r}(n)|²,
    D_X=Σ_{r≠s} Σ_{θ of r, ψ of s} z_θ conjugate(z_ψ) J_X(θ−ψ).

All ordered pairs of unequal conductors enter, including distant frequencies. Conjugate pairing makes D_X real. The identity E_X=Σ_r E_{X,r}+D_X follows by expansion on exactly the original time block. Each E_{X,r}≥0. Within one conductor the spacing is at least 1/(5r), so the translated additive large sieve bounds E_{X,r} by O((X+5r)Σ_{θ of r}|z_θ|²). Since r≤4X and the complete energy of F_D from (4) bounds Σ_θ|z_θ|², one gets

    0 ≤ Σ_r E_{X,r} ≪ X² log(2X),       (D_X)_+ ≤ E_X ≤ (D_X)_+ + O(X²log(2X)).

**Candidate-D, equivalence.** RH is equivalent to the following estimate on signed cross terms:

    For every ε>0 there is C_ε such that (D_X)_+≤C_ε X^(2+ε)
    for all sufficiently large dyadic X.

For the forward implication, RH and the coefficient-unit transfer give |T(n)|≪_ε n^(1/2+ε) pointwise. Squaring on a block with a smaller epsilon, then using the O(X²(1+log X)^5) block bound for |T−G|² from §4, gives E_X≪_ε X^(2+ε). Conversely the displayed estimate gives the same bound on E_X, and then on the block square sum of T by §4. Cauchy–Schwarz gives Σ_{X≤n<2X}|T(n)|≪_ε X^(3/2+ε) after relabeling epsilon. The Mellin integral s∫₁^∞ T(x)x^(−s−1)dx for the step extension now converges absolutely and locally uniformly in Re s>1/2: on compact sets choose epsilon smaller than the distance to this line and sum the resulting geometric series over dyadic X. It equals 1/[ζ(s)U(s)] in Re s>1 by the coefficient identity in FOUNDATION, with U holomorphic and nonvanishing for Re s>1/2. The continuation excludes zeta zeros there; functional symmetry gives RH. This direction uses no assertion about zeros of L(s,χ₅).

For comparison with the one-sided finite-window condition, the same block bounds give Q_T(Y)≪_ε Σ_{dyadic X intersecting [Y,Y²)}X^ε≪_ε Y^(2ε). Taking ε<1/(2k) and then sufficiently large Y yields Q_T(Y)^k≤Y. The local G(n) used by every such window is always the same deterministic dyadic choice. The proof of equivalence above uses the all-epsilon exponent, allows a different constant for each epsilon, and assumes the estimate for all sufficiently late dyadic blocks. Replacing X^ε by one fixed logarithmic power would give a stronger sufficient estimate; it is not asserted equivalent. The known exactly rational test is Q_T. The finite analytic sum D_X preserves this equivalence but does not have a rational-coefficient claim.

## 5. Optional all-time close-pair majorant

The residual (6) can be targeted without estimating every off-diagonal term. For fixed dyadic X≥64 extend the finite sum on that block trigonometrically to every integer; denote its coefficient at θ=a/(5r) by z_θ=A_r b(r,a)m_t(θ). Put c=3X/2 and w_X(n)=sinc²(π(n−c)/(2X)). This weight is bounded below by an absolute positive constant on [X,2X). The Fourier coefficients of the circle function h(α)=(1−2X||α||)_+ are (2X)^(−1)sinc²(πj/(2X)), as in §3. Absolute convergence then gives the exact identity

    Σ_{n∈Z} w_X(n)|G_X(n)|²
      = 2X Σ_{θ,ψ} z_θ conjugate(z_ψ) e(c(θ−ψ)) (1−2X||θ−ψ||)_+.       (8)

The diagonal term inside the last sum is O(X log X), because its squared coefficients are bounded termwise by those of F_D and (4) applies. All close pairs from the *same conductor* together also cost O(X log X) in absolute value. Indeed r≤4X and |a−b|≤5r/(2X)≤10. Each numerator has bounded degree in the neighbor graph, and 2|z_θ z_ψ|≤|z_θ|²+|z_ψ|² suffices. There is no circle wrap to consider: |θ|,|ψ|≤2/√X and X≥64, giving |θ−ψ|≤1/2.

Define C_X to be the remaining sum *inside* (8) from unequal conductors r≠s. It is real by conjugate pairing. Only pairs of signed primitive numerators satisfying

    1 ≤ |as−br| ≤ 5rs/(2X),       gcd(r,s) | (as−br)

enter C_X. In particular a common divisor above 5rs/(2X) precludes a close pair. Constants in the sufficient dyadic estimate are now explicit up to absolute factors:

    X^(−2) Σ_{X≤n<2X}|G(n)|² ≪ log(2X) + (C_X)_+/X.

This is a signed sum of concrete cofactor weights and phases. The conditional bound (C_X)_+≪X(1+log X)^B for a fixed B on all large dyadic X would yield two-sided polylogarithmic window energy for T by (7). The condition is sufficient and remains open for the genuine coefficients. The average over all integers in (8) is a positive majorant used for the dyadic estimate; no equivalence of the majorant to a one-sided statistic on that block has been used. [MAJORANT-SCOPE](MAJORANT-SCOPE.md) proves its additional consequence: L(s,χ₅) would have no zero in Re s>2/3. Neither its necessity for RH nor a contradiction to this sufficient condition is asserted. Section 4.1 retains the equivalent target on the original finite block.

The distinction between the rational conductor projection and the analytic numerator cut is intrinsic. For a rational-valued periodic sequence of period M, its Fourier coefficients lie in the cyclotomic field generated by an M-th root of unity. Every cyclotomic automorphism permutes the coefficients by multiplication of the frequency numerator by a unit modulo M. Each reduced-denominator orbit therefore is either wholly present or wholly absent. A literal cutoff retaining just some primitive numerators of a nonzero conductor cannot in general yield a rational-valued periodic sequence. Formula (1) keeps whole conductor orbits; formula (6) is the spectral analysis of the integer test.
