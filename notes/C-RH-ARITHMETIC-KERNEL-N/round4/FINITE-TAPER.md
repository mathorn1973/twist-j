# Local time taper and signed determinant pairs

**NON-CANONICAL. No authority. Candidate-D, paper only.** We use the same geometric sequence of scales and the same trigonometric sum as round 3 of issue 2087. The new deductions remove off-diagonal terms at frequency distances greater than O(log X/X), and then an explicitly costed family of pairs with a large common divisor. The signed sum over the remaining pairs is O as a research question.

## 1. The fixed data and the local time weights

Write X for a dyadic integer, D=4X, t=X^(−1/2), e(y)=exp(2πiy). In the published round 3 SIGNED-SPECTRUM, the signed squarefree split weight is s(d)=(−2)^ω(d). Coefficients with other supports vanish. The genuine finite trigonometric sum uses the signed frequencies θ=a/(5r), gcd(a,5r)=1, on shells R<r≤min(2R,D), R=2^j X^(2/3), j≥0. The cutoff is

    0<|a|≤min(ceil(R³/X²),10r/√X).

Its coefficients and trigonometric extension to every integer are

    A_r=s(r)Σ_{m≤D/r,(m,r)=1}s(m)/m,
    z_θ=A_r b(r,a)m_t(θ),    b(r,a)=τχ₅(a)/[5r(1−e(−θ))],
    G_X(n)=Σ_θ z_θ e(nθ).

Here |τ|=√5, |b(r,a)|≪1/|a| and the circle multiplier m_t is the triangle convolution from round 3, taking real values in [0,1] and zero for ||θ||>2t. The preceding candidate proved Σ|z_θ|²≪X log(2X). It also gave Σ_{d≤D}|s(d)|≤D and |A_r|≤|s(r)|(1+log D). Therefore Σ|z_θ|≪X(1+log X)², by summing 1/|a| over the retained numerators.

Assume X≥2^16; this restriction excludes finitely many blocks. Put

    k=ceil(3 log₂ X),  h=floor(X/(16k)),   p(j)=1_{|j|≤h}/(2h+1),
    I=[X−kh,2X−1+kh]∩Z,   w=1_I * p^{*k},

using additive convolution on the integers. Then X≥32k, X/(32k)≤h≤X/(16k), 0≤w≤1, and w(n)=1 on [X,2X). The support lies in [7X/8,17X/8]. The coefficients are nonnegative rational numbers. Define J_w(y)=Σ_n w(n)e(ny). The geometric sum gives

    J_w(y)=(Σ_{n∈I} e(ny)) (Σ_{|j|≤h}e(jy)/(2h+1))^k,
    |Σ_{|j|≤h}e(jy)/(2h+1)| ≤ min(1,1/[2(2h+1)||y||]).

For ||y||≥64k/X the last absolute value is at most 1/8. Hence |J_w(y)|≤2X·8^(−k)≤2X^(−8). The sum of the absolute values of *all* terms z_θ conjugate(z_ψ)J_w(θ−ψ) at these frequency separations is O(X^(−6)(1+log X)^4), by the bound on Σ|z_θ|. There is no unsigned counting assumption inside the complementary thin strip.

## 2. Why this taper stays within the zeta-only argument

Let F_D(n)=Σ_{d≤D}s(d)K_d(n) be the same frozen sum as round 3. It equals T(n) throughout 0≤n≤D, and has |ΔF_D|≤1 on [1,D], with global bound |F_D|≤D. For n in the support of w, time shifts |j|≤X/2 stay between 3X/8 and 21X/8. The Jackson probability weights p'_j from round 3 satisfy Σ|j|p'_j≪√X and Σ_{|j|>X/2}p'_j≪X^(−3/2). Replacing F_D by its m_t-smoothed Fourier sum therefore costs O(√X) pointwise throughout this support.

For completeness the subsequent frequency cuts remain controlled there. Cover the support by at most three intervals of length X and apply on each the translated large-sieve inequality from KERNEL §7, with coefficient-square sum as in round 3. For all r≤R₀=X^(2/3) this gives O((X+R₀²)R₀(1+log D)^3). In a retained shell R≥R₀, with H_R=ceil(R³/X²), the discarded |a|>H_R have coefficient-square sum O(R(1+log D)^3/H_R) by |b(r,a)|≪1/|a|. Their pair spacing is ≫R^(−2). Each shell thus costs O((X+R²)R(1+log D)^3/H_R)=O(X²(1+log X)^3). There are O(1+log X) shells, costing at most two logarithms upon summing their norms and squaring. Combining these inequalities with the pointwise smoothing gives

    Σ_{n∈supp w}|T(n)−G_X(n)|² ≪ X²(1+log X)^5.                  (1)

In particular (1) only uses F_D in a range where its value agrees with T. The globally pointwise bound D takes care of the negligible Jackson shift tail; no global bound on a finite-conductor extension's energy is required.

Denote by P_X the signed sum over all ordered unequal-conductor pairs with

    0<|as−br|≤320k rs/X,     θ=a/(5r),   ψ=b/(5s),

with summand z_θ conjugate(z_ψ)J_w(θ−ψ). The determinant is nonzero by primitivity and distinct denominators. The signed representatives obey |θ−ψ|≤4/√X<1/2. The cutoff therefore includes exactly the strip ||θ−ψ||≤64k/X. It is invariant under exchanging the pair, so P_X is real. Same-conductor contributions summed *without* this cutoff have total between 0 and O(X²log(2X)): each is Σ_n w(n)|Σ_{θ of r}z_θe(nθ)|²; dominate w by its interval of support, apply the large sieve at spacing 1/(5r), and sum (X+5r)Σ_{θ of r}|z_θ|². The far-pair estimate in §1 now proves

    Σ_n w(n)|G_X(n)|² = P_X + O(X² log(2X)).                       (2)

**Candidate-D.** For all sufficiently late dyadic X, the estimate (P_X)_+≪_ε X^(2+ε) for every ε>0 is equivalent to RH. Indeed the left side of (2) controls the original block because w=1 there. Conversely RH bounds T(n)≪_ε n^(1/2+ε) through the coefficient unit in FOUNDATION, so (1) bounds this weighted energy by O_ε(X^(2+ε)) after shrinking epsilon first. In the reverse direction the low energy and (1) give the same upper bound for the unweighted block square sum of T. The finite-block Mellin argument in SIGNED-SPECTRUM §4.1 then excludes zeros of ζ in Re s>1/2: Cauchy–Schwarz gives block L¹ norm O_ε(X^(3/2+ε)), sufficient for absolute convergence of the Mellin integral of T, whose Dirichlet series is 1/[ζ(s)U(s)] with a nonvanishing holomorphic unit U. No condition on the zeros of L(s,χ₅) is assumed. This differs from imposing an energy bound for a sinc majorant on all integer times. The original sharp Dirichlet-kernel sum itself has not been asserted to have negligible far terms; it is the compact time taper that makes their removal valid here.

## 3. A common divisor which can be paid without any sign assumption

For r∈(R,2R], s∈(S,2S] let

    g=gcd(r,s),   l=gcd(|a|,|b|),   L=min(R/|a|,S/|b|),
    G₀=max(1, RS L/X²).

**Candidate-D.** The sum of the absolute values of the unequal-conductor terms of P_X with g≥G₀ is O_ε(X^(2+ε)) for every ε>0. Thus one can delete them in the all-epsilon criterion of §2. This is an all-epsilon error and need not preserve a proposed fixed-log error. Define P_X^rem to be exactly P_X restricted to g<G₀, with the shell-dependent G₀ displayed above. Both sums are real by pair exchange. Since the positive-part map is one-Lipschitz, the criterion remains equivalent with (P_X^rem)_+ in place of (P_X)_+, shrinking epsilon in each discarded error if needed.

To prove it fix R,S,a,b,g. Put a₀=a/l, b₀=b/l, u=r/g and v=s/g. Then a₀,b₀ are coprime signed nonzero integers, and u,v are positive coprime integers. The remaining determinant variable is the nonzero integer m=a₀v−b₀u. The strip gives |m|≤1280k RS/(Xgl), so the number of possible m is at most 2560k RS/(Xgl), with no extra constant because m=0 is excluded. Each equation a₀v−b₀u=m, if soluble, gives one integral progression (u,v)=(u₀,v₀)+j(a₀,b₀). It has at most 1+lL/g points in the given two shells. Dropping primitivity and arithmetic support restrictions in this count only enlarges it.

By the divisor bound, |A_r A_s|≪_ε X^ε, using a smaller epsilon for each coefficient; |b(r,a)b(s,b)|≪1/|ab| and |J_w|≤2X. Summing first over g≥G₀ bounds the total for these fixed shells and numerators by

    ≪_ε (k X^ε RS/|ab|) [ (1+log X)/l + L/G₀ ].

Here Σ_{g≥G₀}g^(−2)≪1/G₀ and the harmonic sum stops at 4X. Since RS≤16X² and RS L/G₀≤X², summing 1/|ab| and the O((1+log X)²) shell pairs adds only logarithms. Absorb them by the initial epsilon choice.

For example when R,S both have order X^(4/5) and a=b=1, the bound removes g at least a constant times X^(2/5). Divisibility of the determinant alone only rules out g above order X^(3/5)log X. The remaining terms run over g<G₀ and have the exact primitive progression just described. On genuinely supported pairs, s(r)s(s)=4^ω(g)s(u)s(v) because r,s are squarefree split with (g,uv)=1. In this identity each A coefficient retains in addition its signed coprime cofactor sum from §1. Removing that weight or taking absolute values of the remaining progressions has no justification here.

## 4. A genuine X³ positive contribution inside the remaining strip

Consider the fixed part of P_X with a=b=1 and 3X<r,s≤4X. The multiplier m_t(1/(5r)) tends uniformly to 1 since its argument divided by t tends to zero in its fixed rescaled triangle-convolution profile. Further, b(r,1)=τ/(2πi)+O(1/r) and A_r=s(r), as D/r<11 and 11 is the least split prime. In the entire support of w one has

    |n(1/(5r)−1/(5s))| ≤ (17X/8)/(60X) < 1/20.

Consequently if s(r),s(s) have the same nonzero sign, the real part of every summand z_θ conjugate(z_ψ)J_w(θ−ψ) is at least cX|s(r)s(s)| for some absolute c>0 and all sufficiently large X: every time phase stays in the indicated arc, the two b-factors have product tending uniformly to a positive real number, and Σ_n w(n)≥X. All these pairs satisfy the strip restriction. For distinct r,s in this range g≤2X, while R,S>3X/2 imply RS min(R,S)/X²>27X/8. Thus they also survive §3.

The mass Σ_{3X<r≤4X}|s(r)| is ≍X. This is already established, with a stronger error, in §1 of the [neighboring MOBIUS note at its content commit](https://github.com/mathorn1973/twist-j/blob/c7bf6ec1014b7d6bdc0e75de95054f2aa58ae84e/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N/MOBIUS.md); we use it as a shared input. To verify the weaker error needed here, let f=1*χ₅ with summatory c₅x+O(√x), c₅=L(1,χ₅)>0, as established by hyperbola in round 3. In |s|=v*f the local series of v are (1+2z)(1−z)² at split primes, 1−z² at inert primes and 1−z at 5. The absolute Dirichlet series for v converges at 3/4 and its value V(1)=Σv(n)/n is positive by the convergent product. Summing the convolution gives Σ_{n≤x}|s(n)|=c₅V(1)x+O(x^(3/4)): both the tail of Σv(n)/n and the summed square-root errors are bounded using absolute convergence at 3/4.

The two sign classes have masses M₊,M₋ with M₊²+M₋²≥(M₊+M₋)²/2. Removing the diagonal costs Σ_{r≤4X}s(r)²≪X log X before multiplying by X. Thus the real positive contributions from this fixed numerator and conductor interval alone total at least c′X³ on every sufficiently large block. This rules out discarding signs on the genuine remaining pairs. No choice of an artificial coefficient mask or favorable time window occurred in the construction.

## 5. Unconditional cancellation of that same fixed panel

Retain precisely a=b=1 and 3X<r,s≤4X, now summing *both* sign classes with the actual coefficients. The sum of all ordered unequal-conductor terms from this panel has absolute value O_B(X³/(log X)^B) for every fixed B>0. This pays every fixed logarithmic factor against the X³ absolute-size obstruction. The remaining power gap to the bound X^(2+ε) is unresolved.

Use only Davenport's classical unconditional theorem sup_α|Σ_{n≤x}μ(n)e(αn)|≪_A x/(log x)^A for each A>0 ([Davenport, 1937 II](https://doi.org/10.1093/qmath/os-8.1.313); explicit statement in [He and Huang, equation (1.2)](https://www.impan.pl/shop/en/publication/transaction/download/product/91740?download.pdf=)). It bounds M(x) by taking α=0 and M_χ(x)=Σ μ(n)χ₅(n) by expanding the fixed period-five character in its five additive Fourier coefficients. No GRH estimate in the later source enters this proof. For c=μ*(μχ₅), summation by the Dirichlet hyperbola with cutoff √x bounds Σ_{n≤x}c(n) by O_A(x/(log x)^A): sum μ(a)M_χ(x/a) on a≤√x and μ(b)χ₅(b)M(x/b) on b≤√x, and subtract M(√x)M_χ(√x). The harmonic factor costs one logarithm, allowed by increasing the input exponent. The unit identity in FOUNDATION gives s=c*v with Σ|v(d)|/d^σ finite for each σ>1/2. Split at d=√x: the first range uses convergence at 1 and the preceding bound; in the second use Σ_{n≤y}|c(n)|≤y(1+log y) and convergence at 3/4. The latter costs O(x^(7/8)(1+log x)). Hence

    |Σ_{r≤x}s(r)| ≪_A x/(log x)^A  (x≥3).

For 3X<r≤4X the multiplier b(r,1)m_t(1/(5r))e(n/(5r)) has bounded supremum and bounded total variation, uniformly for n in the taper support. Indeed b(r,1) is a smooth function of 1/r with bounded derivative in that variable, m_t is a fixed Lipschitz profile evaluated at 1/(5rt), and the total variation of the phase is O(|n|/X)=O(1). Partial summation thus gives an amplitude O_A(X/(log X)^A) uniformly in those n. Taking its square and summing w(n) proves the panel bound including the diagonal. The omitted diagonal costs O(X² log X), smaller than X³/(log X)^B for each fixed B. In particular the opposite-sign subtotal cancels the same-sign subtotal of §4 to within O_B(X³/(log X)^B), on every sufficiently large block. This only treats this specified numerator and conductor interval.

## Scope

Read: the round 3 finite-block spectrum, the earlier finite large sieve and the zeta coefficient unit. Derived: finite-time determinant localization, absolute large-gcd pruning, the primitive affine progression and the X³ lower bound for positive contributions and its true signed cancellation to every fixed logarithmic order on the top panel. Open: a signed power saving sufficient for the small-gcd determinant sum. No verification by numerical computation, no historical priority claim, and no changes to the earlier frozen file.
