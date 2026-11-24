# What the global close-pair majorant would additionally force

**NON-CANONICAL, no authority. Candidate-D as a logical implication.** Let C_X be the signed unequal-conductor sum of SIGNED-SPECTRUM §5. If (C_X)_+≪X(1+log X)^B for some fixed B at all sufficiently large dyadic X, the preceding deductions imply RH. The same hypothesis would also exclude zeros of L(s,χ₅) with Re s>2/3. The discussion below does not establish the close-pair hypothesis, a contradiction to it, its equivalence to any GRH, or an implication from RH alone to this majorant.

The exact finite-block equivalent target is in [SIGNED-SPECTRUM §4.1](SIGNED-SPECTRUM.md). This note concerns only its optional all-time majorant in §5.

Write S(y)=Σ_{d≤y}s(d), D=4X and w=w_X. By (8) and its diagonal estimates,

    Σ_{n∈Z} w(n)|G_X(n)|² ≪ X²(1+log X)^{max(B,1)}.

Here G_X is the trigonometric sum extended with the *same* block data X,D to all integers. Inspect the additional interval D≤n≤2D. Since ⌊n/d⌋=1 for D<d≤n, one has F_D(n)=T(n)−(S(n)−S(D)) there. The omission estimates of SIGNED-SPECTRUM §4 apply on each translated block of length X, because the large sieve is translation invariant. For the time-smoothing comparison on [D,2D], the exact arithmetic difference of the truncated sum has the global bound

    |ΔF_D(m)| ≤ Σ_{d|m}|s(d)| ≤ 3^{ω(m)} ≪_ε m^ε       (m≥1).

For the last bound, each prime p above 3^(1/epsilon) pays its factor 3
from p^epsilon, and the finitely many smaller primes cost a fixed
constant. The same argument bounds |s(m)| by O_epsilon(m^epsilon).

In the sum over Jackson shifts |j|≤X all the required arguments m are between 3X and 9X. Thus that part costs O_ε(X^{1/2+ε}) pointwise, and the tail |j|>X still costs O(X(tX)^(−3)). By RH, already implied by this majorant, T(n)≪_ε X^{1/2+ε} throughout the supplementary interval. Combining these estimates, using 0≤w≤1 and allowing epsilon to shrink first, gives

    Σ_{D≤n≤2D} w(n)|S(n)−S(D)|² ≪_ε X^{2+ε}.                         (1)

The two zeros of w on this interval are 11X/2 and 15X/2. On [D,2D], w(n) is bounded below by a positive constant times the squared distance to the nearest of these zeros divided by X². Constants are absolute, by the explicit sinc formula on a fixed compact scaled interval. Delete neighborhoods of radius h=ceil(X^(2/3)) around the zeros. Outside them Σ1/w≪X²/h, from the square-summable inverse distances. Cauchy–Schwarz in (1) bounds the absolute sum of |S(n)−S(D)| there by O_ε(X^{5/3+ε}). The deleted O(h) integers contribute O(Xh), since Σ_{d≤2D}|s(d)|≤2D. Therefore the same bound applies on the whole interval.

To bound the anchors, w stays bounded below in a left neighborhood of 2D of length cX for a fixed c>0. Use just the last floor(X^(2/3)) integers in (1). Their unweighted average of |S(n)−S(D)| is O_ε(X^{2/3+ε}) by Cauchy–Schwarz. Traversing these integers to 2D costs O_ε(X^{2/3+ε}) because |ΔS(m)|=|s(m)|≪_ε X^ε. Hence |S(2D)−S(D)|≪_ε X^{2/3+ε}. Summing these increments on dyadic D shows |S(D)|≪_ε D^{2/3+ε} at dyadic endpoints. Adding this anchor in each block yields

    Σ_{D≤n<2D}|S(n)| ≪_ε D^{5/3+ε}.

The integral s∫₁^∞ S(x)x^(−s−1)dx is then absolutely and locally uniformly convergent in Re s>2/3 by dyadic summation. In Re s>1 it equals the Dirichlet series with coefficients s(d). The Euler-unit identity from FOUNDATION gives its meromorphic continuation there as 1/[ζ(s)L(s,χ₅)U(s)], with U holomorphic and nowhere zero for Re s>1/2. Holomorphy just obtained forbids a zero of L(s,χ₅) in Re s>2/3 away from the pole of ζ at 1; the latter point already satisfies L(1,χ₅)>0.

This identifies a genuine further zero-free consequence for this fixed Dirichlet character. For a same-block alternative that introduces no long time tails, the exact two-sided sum Σ_{X≤n<2X}|G_X(n)|² expands with the finite Dirichlet kernel Σ_{X≤n<2X}e(n(θ−ψ)); this kernel usually retains pairs at all frequency separations. The original one-sided equivalent target Q_G remains the finite positive-part sum in §4. The localized close-pair upper bound of §5 is a sufficient target with the additional consequence proved here; its necessity for RH is not established.
