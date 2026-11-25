# A power saving for the growing numerators of the finite determinant sum

**NON-CANONICAL. No authority. Candidate-D, paper deduction.** Work at the dyadic integer scales and with the unaltered spectrum of round 4, FINITE-TAPER §§1–3. The estimate below is unconditional. It uses no prime-distribution or zero-free hypothesis. All implicit constants indexed by epsilon are uniform in the conductor and numerator intervals and in the height cutoff.

Write χ for the real primitive character modulo 5, X for the block size, t=X^(-1/2), D=4X and k=ceil(3 log₂ X). In each original shell R<r≤min(2R,D), R≥X^(2/3), let θ=a/(5r) run over the original primitive signed numerators up to min(ceil(R³/X²),10r/√X). Put

    h(θ)=X|a|/r,  z_θ=A_r τχ(a)m_t(θ)/[5r(1−e(−θ))],
    A_r=s(r) Σ_{m≤D/r, (m,r)=1}s(m)/m.

Here s(r)=(−2)^ω(r) on squarefree split conductors and is zero elsewhere, e(u)=exp(2πiu) and m_t is the normalized convolution of two triangle functions of width t. The finite rational time taper w is between zero and one, equals one on [X,2X), and is supported in [7X/8,17X/8]. Set J_w(y)=Σ_n w(n)e(ny). Let P_rem(Y) be the part of the genuine ordered, unequal-conductor P_X^rem with max(h(θ),h(ψ))≥Y. Both the thin determinant strip and the small-gcd requirement in FINITE-TAPER are imposed.

**Theorem.** For 640k≤Y≤10√X,

    |P_rem(Y)| ≪_ε X^ε [X³/Y²+X²].                                 (1)

In particular every fixed 0<δ<1/2 gives O_ε(X^(3−2δ+ε)) for the whole part with maximum height ≥X^δ. The contributors to (1) include pairs with only one height above Y. At Y=√X/L(X), with L≥1 and L(X)=X^o(1), this entire part costs O_ε(X^(2+ε)). Removing it preserves the all-epsilon signed criterion. For fixed δ<1/2, the exponent in (1) still exceeds two.

## 1. A numerator sum before the conductor absolute value

Fix a shell and one sign, A≤|a|<2A for a dyadic A≥1. One may further restrict the height to any single interval and the conductor to any subinterval of the shell. At each n in the support of w, the sum B of the corresponding z_θ e(nθ) satisfies

    |B| ≪_ε X^ε R/A.                                                   (2)

If the shell box is nonempty then A≤20R/√X. For each r the allowed positive magnitudes form a single interval, which may depend on r. For a positive numerator retain the sign in χ(a) and in e(na/(5r)). The remaining weight

    W_r(a)=τ m_t(a/(5r))/[5r(1−e(−a/(5r)))]

has supremum plus total variation O(1/A) on that interval. Indeed a≤10r/√X, so the inverse geometric factor including 1/(5r) is O(1/a), with a derivative O(1/a²). The multiplier is a fixed bounded Lipschitz profile at a/(5rt) on [0,2], by rescaling the compact triangles in their circle convolution for sufficiently large X. Its variation is O(1). The same estimates hold with negative numerators parametrized by their positive magnitudes.

Expand the condition (a,r)=1 as Σ_{d|(a,r)} μ(d), and put r=dq, |a|=dj. The constraint (a,5)=1 is encoded by χ(a), and χ(dj)=χ(d)χ(j). The finite additive Fourier expansion of χ(j) is a sum of five constants times e(vj/5). Partial summation in j against W_r(±dj) bounds each of these geometric sums, including its endpoints, by

    ≪ A^(-1) min(C A/d, 1/[2|| (±n+vq)/(5q) ||]),

where a zero denominator denotes infinity and d<2A. The number of terms, also for truncated intervals, is O(A/d) because d<2A. All the original cofactor weights are still present. Only now take |A_{dq}|≪_ε X^ε, from the divisor bound and Σ_{m≤D/r}|s(m)|/m≤1+log D.

For fixed d let Q=R/d, so q∈(Q,2Q]. The distance of ±n+vq to 5q times an integer is at least the distance j₀=dist(n,q Z) to any multiple of q. Each geometric bound before the factor A^(-1) is therefore O(min(A/d,Q/j₀)) if j₀>0 and O(A/d) otherwise. The sum of these bounds over q is

    ≪_ε X^ε [Q log(2X)+A/d].                                         (3)

For j₀=0 there are at most τ(n) possible divisors q. For an attained distance j₀>0 choose a nearest multiple mq. If m=0, then j₀=n and Q/n=O(1) since n≥7X/8 and Q≤4X. All q assigned to this exceptional case cost O(Q+1). Otherwise 1≤mq≪X, mq=n±j₀, and j₀≤q/2≤Q. For each positive j₀, the number of possible q is at most the sum of τ(n±j₀) over positive arguments. These divisor counts are O_ε(X^ε), and summing Q/j₀ gives (3). In a nonempty box Q=R/d≥R/(2A)≥√X/40, absorbing the single endpoint cost. Finally sum (3) over d<2A. Since Q=R/d and A≪R, the harmonic costs are absorbed into X^ε after reducing input epsilons. This proves (2). The conductor sum has required no cancellation between different A_r.

## 2. Transfer to the actual remaining pairs

For any interval of heights contained in [Y/2,10√X], all occupied dyadic boxes in (2) have R/A≤4X/Y. The same holds for intervals whose endpoints depend on X. Summing first over the two signs and then the O(log²(2X)) shell and magnitude boxes gives a pointwise bound O_ε(X^(1+ε)/Y) for the amplitude. The support of w has O(X) integers. The full weighted product of any two such interval amplitudes is consequently O_ε(X^(3+ε)/Y²).

The signed strip requires |Xa/r−Xb/s|≤320k. Hence when the larger absolute height is at least Y, the other is at least Y/2. Opposite signs cannot occur in such a pair. For H={h≥Y} and M={Y/2≤h<Y}, the ordered pairs in question consist, inside the strip, of the three disjoint rectangles H×H, H×M, M×H. Expand the full weighted product on each rectangle. First remove all same-conductor terms by Cauchy–Schwarz over (r,n) with weights w and the within-r separated-frequency bound of FINITE-TAPER §2 applied to each restricted spectrum. The resulting bound stays O(X²log(2X)), since restriction decreases the sum of squared single-mode coefficients. Next remove the distant unequal-conductor terms, negligible in absolute value by FINITE-TAPER §1. Finally its unequal-conductor strip terms deleted by the large-gcd cut have absolute total O_ε(X^(2+ε)) by §3 there, including after any restriction. These removals are disjoint. This proves (1). It directly accounts for the interactions crossing the threshold. No prior bound for the total or the complementary amplitude was used.

## 3. The actual size before signed summation

For fixed 0<δ<1/2 and Y=X^δ, the sum of the **absolute values** of the ordered summands of P_rem(Y) is at least

    ≫_{ε,δ} X^(3−ε)/Y                                                   (4)

for every ε>0 on all sufficiently large blocks. It is enough to use 3X<r≤4X and Y≤h(θ)≤2Y with positive numerators. On these conductors A_r=s(r), since D/r<11, the first split prime. Both original numerator cutoffs admit the entire chosen range for sufficiently large X (the power cutoff is ≫X and Y=o(√X)). The multiplier is then uniformly 1+o(1). Thus |z_θ|≫|s(r)|/Y there. The integer a interval has length rY/X, of order Y. By elementary inclusion-exclusion the count with (a,5r)=1 equals its length times φ(5r)/(5r), with error O(τ(5r)). For every η>0, φ(5r)/(5r)≥1/τ(5r)≫_η X^(−η); choose η<δ/3 so the error is absorbed. The actual absolute split mass Σ_{3X<r≤4X}|s(r)|≫X is the same established input as FINITE-TAPER §4. Hence the mode mass on this subset is ≫_{η,δ} X^(1−η).

Partition [Y/(5X),2Y/(5X)] into O(Y) intervals of length at most 1/(100X). For frequencies in one interval all phases e(n(θ−ψ)) on the support of w have real part bounded below by an absolute positive constant. Therefore |J_w(θ−ψ)|≫X. Cauchy–Schwarz on the bin masses gives an absolute total ≫ X^(3−2η)/Y. Within one conductor the primitive spacing ≥1/(5r)≥1/(20X) permits at most one mode in each such bin, so equal conductors cost only the diagonal O(X²log(2X)). All pairs are inside the strip. The entire high-gcd deletion costs O_η(X^(2+η)) in absolute value. Choose η sufficiently small in terms of δ and ε and absorb both errors. This proves (4) for the genuine cofactor and multiplier.

Thus the gain of a factor X^δ up to X^ε between (4) and (1) requires signed summation on these polynomially growing height ranges. The argument uses phases and the character-bearing numerator sums. It gives no comparable power saving for h of order one. Estimating the sum on the complementary low heights to square-root precision remains open.
