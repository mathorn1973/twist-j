# What uniform initial intervals of the first harmonic would require

**NON-CANONICAL. No authority. Candidate-D, conditional implication and scope check.** Use the same dyadic X, finite taper w, multiplier m_t and determinant pruning as FINITE-TAPER. For 2X≤u≤4X, let P(X,u) consist of exactly the terms of P_X^rem with a=b=1 and 2X<r,s≤u. It is real by pair exchange. Write S(v)=Σ_{r≤v}s(r).

For each fixed 1/2≤σ<1 the following two estimates are equivalent, with constants allowed to depend on ε and σ:

    sup_{2X≤u≤4X} P(X,u)_+ ≪_ε X^(1+2σ+ε) for all sufficiently large dyadic X, all ε>0;
    |S(v)| ≪_ε v^(σ+ε) for all v≥2, all ε>0.

In particular the uniform square-root target σ=1/2 also excludes zeros of L(s,χ₅) in Re s>1/2. The original full pair sum has a zeta-only equivalence. This statement uses the additional supremum over conductor endpoints and the separation of the first harmonic.

**Proof.** Every first harmonic in these intervals survives the original individual cutoffs, and A_r=s(r) because D/r<2. Set c_X(r)=τm_t(1/(5r))/[5r(1−e(−1/(5r)))] and

    B_u(n)=Σ_{2X<r≤u} s(r)c_X(r)e(n/(5r)).

Uniformly in u, FINITE-TAPER §§1–3 gives
Σ_n w(n)|B_u(n)|²=P(X,u)+O_ε(X^(2+ε)): the excluded far and high-gcd terms are bounded in total absolute value even with the interval restrictions. The equal-conductor contribution is diagonal and costs O(X²log(2X)).

Assume the first estimate. Use w=1 on [X,2X), average B_u there and apply Cauchy–Schwarz. After shrinking the input ε this gives

    |Σ_{2X<r≤u} s(r) C_X(r)| ≪_ε X^(σ+ε),
    C_X(r)=c_X(r) X^(-1) Σ_{n=X}^{2X−1}e(n/(5r)).

On the real interval [2X,4X] one has inf |C_X|≫1 and total variation of C_X and 1/C_X is O(1), uniformly in X. Indeed the phases n/(5r) are in [1/20,1/5], so their real parts have a common strictly positive lower bound. The time average has derivative O(1/X) in r. The function τ/[5r(1−e(−1/(5r)))] tends uniformly to τ/(2πi) and has derivative O(1/X²), by the removable singularity of x/(1−e(−x)) at zero. The triangle-convolution profile is bounded Lipschitz at 1/(5rt), with value 1 at zero, hence tends uniformly to 1 and has total variation O(1) in this range. These facts give the same bounded-variation conclusion for the reciprocal by the lower bound on the modulus.

Apply partial summation to the weighted prefixes using 1/C_X. The result is |S(u)−S(2X)|≪_ε X^(σ+ε) for every endpoint in the interval. The dyadic intervals (2X,4X] are consecutive and cover every sufficiently large integer, so geometric summation over earlier whole intervals proves the second estimate. Conversely on the support of w, c_X(r)e(n/(5r)) has bounded supremum and total variation O(1) in the same r interval, uniformly since |n|≪X. Partial summation now gives |B_u(n)|≪_ε X^(σ+ε). Its weighted energy and the uniform expansion above prove the first estimate.

Finally the second estimate makes s∫₁^∞ S(x)x^(−s−1)dx holomorphic for Re s>σ. In Re s>1 this equals 1/[ζ(s)L(s,χ₅)U(s)] by FOUNDATION §2. The unit U and its inverse are holomorphic and nonvanishing above Re s=1/2. At s=1 the nonvanishing L(1,χ₅)>0 is known; away from that point a zero of either factor ζ or L in the indicated half-plane would give a pole. No zero-free consequence is deduced here for a single fixed endpoint panel. Whether RH by itself can imply the additional character statement is left open.
