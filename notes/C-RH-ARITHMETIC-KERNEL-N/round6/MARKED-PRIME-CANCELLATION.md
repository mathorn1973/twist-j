# Opposing large-prime conductor contributions at low height

**NON-CANONICAL. No authority. Candidate-D, paper deduction.** The low-height spectrum is the actual G_X^star of round 5, with its fixed rough-conductor restriction P⁺(r)>(log X)², height X|a|/r<√X exp(−√log X), original numerator cuts, coprime cofactor, smoothing multiplier and finite time taper w. Split its conductors according to P⁺(r)>√D or P⁺(r)≤√D, where D=4X. These two families are denoted by + and −, respectively.

The two same-family signed determinant sums each have the positive leading term κ²M_X. The signed mixed sum, counting both orders, has leading term −2κ²M_X. Here κ=1/U(1)>0 and

    M_X=Σ_n w(n)n²/(log n)^4 ≍ X³/(log X)^4.

In all three assertions the error is O(X³/(log X)^5). They hold both on the entire G_X^star and upon the further restriction h=X|a|/r≤(log X)^14 on each frequency. Thus both remaining signed same-family sums separately exceed X^(2+ε) for fixed ε<1 on every sufficiently late block. Opposing interactions of actual rough conductors persist down to polylogarithmic heights. The solution of the full square-root problem remains open. Rounds 3 and 4 already gave the prime-average main term on the time side. The deductions here transfer it to actual primitive conductor pairs, control both cross orders, and bound the height-truncation error.

## 1. Complete primitive packet for a large marked prime

Use K_d(n)=S_χ(⌊n/d⌋), F_E(n)=Σ_{d≤E}s(d)K_d(n), and the frozen primitive decomposition F_D=Σ_{r≤D}A_r(D)Φ_r. For split squarefree q and a split prime p not dividing q, divisor expansion gives

    Φ_pq(n)=Φ_q(⌊n/p⌋)−Φ_q(n)/p.

Indeed Φ_r(n)=Σ_{h|r}μ(h)χ(h)K_{r/h}(n)/h, χ(p)=1, and K_{pb}(n)=K_b(⌊n/p⌋). This holds for every integer n, with floor division. For p>√D, q≤D/p implies q<p, and the cofactor m≤D/(pq) is automatically prime to p. Maintaining its required coprimality with q gives exactly

    A_pq(D)=−2 A_q(D/p).

There is at most one prime exceeding √D in a supported r. Summing over these conductors gives the identity

    F_+(n):=Σ_{P⁺(r)>√D}A_r(D)Φ_r(n)
           =−2Σ_{√D<p≤D, split} [F_{D/p}(⌊n/p⌋)−F_{D/p}(n)/p].       (1)

In (1) E=D/p is a real cutoff, interpreted as its floor in sums. On the support of w, n≤17X/8<D, so F_{D/p}(⌊n/p⌋)=T(⌊n/p⌋). In the second term |F_{D/p}(n)|≤D/p, even for arbitrary n, hence its total error is O(√D) using the ordinary sum of p^(−2) above √D. The first term is exactly the raw d-packet with P⁺(d)>√D, by the unique large prime and d=pe. Identity (1) measures the difference between this support mask and the conductor mask.

Uniformly for 7X/8≤n≤17X/8,

    F_+(n)=κ n/(log n)^2+O(X/(log X)^3).                            (2)

To verify the moving endpoint in this invocation of LARGE-PRIME-TAIL §2, use z=√D and a=log z/log n, which lies in [2/5,3/5] for large X. For the split prime count Π the raw sum is −2Σ_{m≤n/z}t(m)[Π(n/m)−Π(z)], where |t(m)|≤1. Fixed-modulus PNT to any fixed logarithmic order supplies the integral

    −n ∫₁^{n/z} T(u) du/[u²(log n−log u)]

with error O_B(X(log X)^(1−B)), since both prime arguments are ≥z. Throughout this integral log n−log u≥(2/5)log n. Expand the denominator to two terms. The absolute second-logarithm moment is finite by the inherited unconditional |T(u)|≪u exp(−c√log u) for u≥2, which also permits extending the moment integrals to infinity with arbitrary fixed inverse-log precision since n/z≥n^(2/5). The zeroth moment vanishes and ∫T(u)log u du/u²=−1/U(1), from the germ 1/[sζ(s)U(s)]. This proves (2). No information on zeros of L(s,χ₅) is used.

## 2. All inherited frequency cuts survive the conductor mask

Write ||f||_w²=Σ_n w(n)|f(n)|². The trigonometric packet G_+ is obtained by the original smooth multiplier and cuts in G_X^star restricted to the conductors of (1). Then

    ||G_+−F_+||_w ≪_ε X^(1+ε).                                     (3)

For the Jackson smoothing step, on the integers 3X/8≤v≤21X/8 the first term of (1) agrees with the raw d-packet. Its successive differences are bounded by Σ_{d|v}|s(d)|≤3^ω(v)≪_ε X^ε. The second term in (1) is globally O(√X). Both F_+ and the raw packet are globally O(X), since the latter has total coefficient mass ≤D, and its identity with the sum −2Σ F_{D/p}(⌊n/p⌋) holds at all integer n by d=pe. Thus averaging F_+(n−j) with the original Jackson weights costs O_ε(X^(1/2+ε)) pointwise throughout the support: for |j|≤X/2 use the first absolute shift moment O(√X) on the raw packet and the global O(√X) correction twice, and for larger shifts use the weight tail O(X^(−3/2)). For the subsequent small-conductor and high-numerator cuts, the translated large-sieve estimates of FINITE-TAPER §2 apply unchanged: each coefficient-square sum of a subset is at most that of the full set. Their total squared cost on the taper is O(X²(1+log X)^5). P⁺(r)>√D already implies the original roughness cutoff. The extra height cutoff in G_X^star costs O_ε(X^(1+ε)) in norm by the round 5 numerator argument; its conductor absolute values were used only after summing numerators and the same proof works for any conductor mask. This establishes (3). The sign-complement G_−=G_X^star−G_+ is taken in the exact same spectrum.

Put L=log X and f(n)=κn/(log n)² on the taper. Equations (2) and (3) give ||G_+−f||_w≪X^(3/2)/L³. Since ||T−G_X^star||_w≪_ε X^(1+ε) by round 5 and T(n)≪_B X/L^B for every fixed B, we also get ||G_−+f||_w≪X^(3/2)/L³. These are signed function estimates in norm, with functions evaluated at the same time.

## 3. A polylogarithmic mean-square height cutoff

The following uniform version of the round 5 numerator estimate is used only on the taper, with the ordinary unweighted square norm over its support. For any conductor mask depending on r alone, restrict the numerators to one sign, to A≤|a|<2A in one shell R<r≤min(2R,D), and optionally to any single height interval. With all original numerator conditions, let B(n) denote the resulting amplitude. Then

    ||B||₂ ≪ √X (R/A) (1+log X)^8.                                 (4)

Here is a proof with the divisor weights retained. Write τ_j=1^{*j}. The exact amplitude coefficient has |A_{dq}|≤(1+log D)τ₂(d)τ₂(q), since |s(r)|≤τ₂(r) and τ₂ is submultiplicative. Following NUMERATOR-ESTIMATE §1, use Σ_{d|(a,r)}μ(d) for (a,r)=1, write r=dq, |a|=db, and expand χ(b) in its five additive phases. The remaining multiplier τm_t/(5r(1−e(∓db/(5r)))) has supremum plus total variation O(1/A) on the allowed b interval. Partial summation costs that factor times the bound for a geometric progression. Before 1/A this is O(min(A/d,Q/j)) for j=dist(n,qZ)>0 and O(A/d) for j=0, with Q=R/d and d<2A. For a nonempty box A≤20R/√X and Q≫√X, allowing endpoints in the q counts to be absorbed.

Sum in q first, with weight τ₂(q). For j=0 the total geometric bound is O((A/d)τ₃(n)), since Σ_{q|n}τ₂(q)=τ₃(n). If zero is a nearest multiple, j=n and Q/n=O(1), giving O(Q log(2X)) from Σ_{Q<q≤2Q}τ₂(q). For other nearest multiples and j>0, q divides one of the positive arguments n±j. Extending τ₃ by zero to nonpositive integers, the sum of the geometric bounds is therefore at most a constant times

    (A/d)τ₃(n) + Q log(2X) + Q Σ_{1≤j≤Q}[τ₃(n+j)+τ₃(n−j)]/j.

For every j≤Q≤4X each translated τ₃ has square norm O(√X(1+log X)^4) on the taper. Indeed τ₃(m)²≤τ₉(m): at a prime exponent k every pair of weak compositions into three parts occurs as the row and column sums of a nonnegative integer 3 by 3 matrix with total k, and multiplication gives the inequality on all integers. The elementary hyperbola bound Σ_{m≤7X}τ₉(m)≪X(1+log X)^8 follows by bounding the last divisor variable and summing eight harmonic series. Minkowski now bounds the q sum in square norm by O(√X(1+log X)^5(Q+A/d)). Restore the factor (1+log D)τ₂(d)/A for each d and use Σ_{d<2A}τ₂(d)/d≪(1+log X)^2. Since A≪R this yields (4). All restrictions on r may be dropped after the geometric and absolute cofactor bounds.

For a height interval with h≥Y, each occupied box has R/A≤2X/Y. There are O((1+log X)^2) shell and numerator boxes. Thus for arbitrary fixed conductor masks and any single height interval with h≥Y,

    ||G_{h in interval}||_w ≪ X^(3/2) (1+log X)^10/Y.              (5)

In particular each of G_+,G_− differs from its restriction to h≤L^14 by O(X^(3/2)/L⁴) in norm. This proves that the signed function estimates at the end of §2 still hold for the restricted packets. For the original height cutoff √X exp(−√log X), (5) also suffices on its own in (3).

## 4. The three signed determinant sums

Use either the two families G_+,G_− or their jointly truncated versions h≤L^14. Denote the corresponding amplitudes by B_+,B_−. Let P_{++},P_{−−} be their same-family sums with exactly the unequal-conductor, strip, and gcd cutoffs of P_X^star. Let P_mix include both mixed orders with the same cutoffs. By the finite-taper expansion these three sums differ respectively from

    ||B_+||_w²,   ||B_−||_w²,   2 Re Σ_n w(n) B_+(n)conj(B_−(n))

by O_ε(X^(2+ε)). Indeed the far and large-gcd controls are absolute on every subset, and same-conductor terms for either same-family expression are bounded by the within-conductor large sieve. Distinct-family pairs never have equal conductors. All amplitudes here are real by conjugate pairing. Since ||f||_w²=κ²M_X and ||B_+−f||_w+||B_−+f||_w≪X^(3/2)/L³, Cauchy–Schwarz gives

    P_{++} =  κ²M_X + O(X³/L⁵),
    P_{−−} =  κ²M_X + O(X³/L⁵),
    P_mix  = −2κ²M_X + O(X³/L⁵).                                  (6)

The subset partition is exhaustive on each stated spectrum. For the original P_X^star no mixed term across low and high height is suppressed. For the version restricted to h≤L^14, (5) and Cauchy–Schwarz show that restoring all pairs with at least one larger height changes each of the three signed quantities by O(X³/L⁶+X^(2+ε)), using fixed small ε. This comparison includes both rectangles crossing the height boundary. It does not assert that this change is small at square-root scale.

**Scope.** The result exhibits a joint cancellation of leading terms between three actual low-height conductor sums. It also proves that a strategy demanding square-root-scale estimates separately on the two conductors' largest-prime classes fails, even on the polylogarithmic height range. The residual after their joint cancellation lacks the desired power bound. The primary classical prime-count input is used in the form recorded in round 3 [LARGE-PRIME-TAIL §§2–3](https://github.com/mathorn1973/twist-j/blob/f55cbcd1bf0eff6de99449c37ac8c03916b8acfe/notes/C-RH-ARITHMETIC-KERNEL-N/round3/LARGE-PRIME-TAIL.md). The frozen finite mask, prime averaging and all-logarithmic unrestricted bound have been credited above. The unweighted divisor estimates here are elementary.

## 5. Replacing the marked family by an exact smaller-argument profile

This corollary uses the full round 5 low-height cutoff of G_X^star. Write Π for the split-prime count and t(m)=T(m)−T(m−1). For every integer n in the taper set

    C_X(n)=−2 Σ_{m≤n/√D} t(m)[Π(n/m)−Π(√D)].

This is an exact arithmetic function. All m are at most 17√X/16. Interchanging its finite sums gives C_X(n)=−2Σ_{√D<p≤n,split}T(⌊n/p⌋). By (1), F_+−C_X is O(√X) there, and consequently by (3)

    ||G_+−C_X||_w² ≪_ε X^(2+ε),
    P_{++}−2 Re⟨G_+,C_X⟩_w+||C_X||_w² = O_ε(X^(2+ε)).

Here ⟨f,g⟩_w=Σ_n w(n) f(n)conj(g(n)); P_{++} differs from ||G_+||_w² by the already stated O_ε(X^(2+ε)). Each of the three terms on the second line has absolute order X³/(log X)^4. The result controls their signed combination at the required scale on every sufficiently late dyadic block.

Put R_X=G_−+C_X. The full approximation from round 5 and the first displayed bound yield ||T−R_X||_w²≪_ε X^(2+ε). The remaining pair expression is

    Qcorr(X)=P_{−−}+2 Re⟨G_−,C_X⟩_w+||C_X||_w².

Its difference from ||R_X||_w² is O_ε(X^(2+ε)). Therefore RH is equivalent to (Qcorr(X))_+≪_ε X^(2+ε) for every ε>0 on all sufficiently late dyadic blocks, by the same norm triangle and same-block equivalence as in round 5. This retains the original mixed interaction through the explicit profile at target norm precision. No unconditional bound of that size on P_X^star−Qcorr(X) follows, since its expansion also pairs the approximation error with the unknown joint amplitude. Replacing C_X by its leading term κn/(log n)^2 would only give a logarithmic relative error. The precision here comes from the exact finite prime counts.
