# Independent review of the fixed-power rough tail

**NON-CANONICAL, no authority. Candidate-D on paper.** This reconstruction tests the proposed fixed-u extension without numerical computation. Let u>1 be fixed, z=X^(1/u), and B_u(X) restrict the long signed tail d>X^(2/3) to P⁻(d)>z. Then

    B_u(X) ~ −ρ(u−1)L(1,χ₅) X/log X.

Here ρ is the classical Dickman function, with ρ(v)=1 on [0,1] and vρ′(v)=−ρ(v−1) for v>1. The assertion is for each fixed u. Constants and starting points may depend on u.

## Prime tuple reconstruction

After truncating the outer character expansion at a fixed j, the underlying summatory upper limit is y=X/j. The lower cutoff in d costs O(X^(2/3)) using Σ_{d≤t}|s(d)|≤t. The possible numbers r of split prime factors >z are bounded by u. Express their squarefree count in terms of ordered tuples divided by r!. Including repeated primes in the tuple calculation costs O_u(X/z): each repeated product is divisible by some p² with p>z, Σ_{p>z}X/p²≪X/z, and a given product has at most r! ordered presentations.

For r≥2 first sum over r−1 primes of product m≤y/z. The last prime has π_split(y/m)−π_split(z) choices before the repeated-prime correction. The total subtraction is O_u(y/log²X). To see this, for each nonempty prefix count of r−1 primes use the prime number theorem on its last variable, whose allowed upper endpoint is at least z. Sum the reciprocal weights of the other factors; Σ_{z<p≤X}1/p is bounded in terms of u. This bounds the count of r−1 prime tuples with product ≤y/z by O_u((y/z)/log X) if any exist. For r=1 the subtraction π_split(z)=o(X/log X) directly.

Uniformly for y/m≥z, π_split(y/m)∼(y/m)/(2 log(y/m)) by the fixed-modulus prime number theorem. In each remaining prime coordinate v_i=log p_i/log X, the reciprocal-prime measures converge on [1/u,1] to dv_i/(2v_i). This follows for intervals by partial summation and for continuous functions by approximation. Their products converge as well. The permissible region has Σv_i≤1−1/u+o(1), where the moving boundary has zero limiting product mass and the logarithmic denominator 1−Σv_i stays bounded away from zero. At the integer endpoint r=u the region has zero volume and there are no such strict tuples. For r≥1, multiplication by (−2)^r cancels the prime density factors while retaining the alternating sign. Consequently the r-prime leading coefficient relative to X/(j log X) is

    (−1)^r u k^{*r}(u)/r!,    k(t)=1_{t≥1}/t.

Indeed the remaining prime-exponent integral is the r-fold additive convolution on Σv_i=1 of 1_{v≥1/u}/v. The substitution t_i=u v_i gives the factor u. In particular the r=1 coefficient is −1.

## Independent check of the Dickman sign, shift and positivity

Put I₀(v)=1 for v≥0 and I_r(v)=∫_{t_i≥1,Σt_i≤v}∏ dt_i/t_i for r≥1. On the convolution hyperplane, write u=t₁+⋯+t_r. Each of the r terms cancels one denominator and integrating out the corresponding variable leaves exactly I_{r−1}(u−1). Thus u k^{*r}(u)=r I_{r−1}(u−1), including r=1 at u>1. The sum of all r≥1 signed coefficients is exactly −Σ_{h≥0}(−1)^h I_h(u−1)/h!. For any fixed argument this sum is finite. Its unsigned outer negative multiplies the function D(v)=Σ(−1)^h I_h(v)/h!, which equals one on [0,1]. Differentiating the simplex integrals gives vD′(v)=−D(v−1) for v>1, first off integer boundaries and then by continuity. Uniqueness by intervals identifies D=ρ. The identity vρ(v)=∫_{v−1}^vρ(t)dt, obtained by differentiation and matching at v=1, implies positivity for every finite v by contradiction at a first zero. At u=3 one gets −(1−log 2) as required. A standard reference for Dickman's function is [Friedlander and Granville, Limitations to the equi-distribution of primes I](https://dms.umontreal.ca/~andrew/PDF/Equidist1.pdf).

## Uniformity required by the signed window

For D=X^(2/3)≤y≤X, the count of original rough d≤y weighted by |s(d)| is O_u(y/log X) if restricted to d>D. For each r≥1 apply the prime number theorem upper bound to the last prime at y/m≥z as above, then bound the other r−1 reciprocal sums uniformly in X and y; the finitely many weights 2^r depend only on u. For y<D there are no such d. Truncating the expansion Sχ(X/d)=Σ_{j≤X/d}χ(j) at a fixed integer Q therefore costs O_u(X/((Q+1)log X)): each difference of two partial character sums is at most two, and it vanishes except at d≤X/(Q+1). This bound is for the signed tail after recombination by d. Absolute summation of all omitted j terms separately would give an erroneous extra logarithm. Passing first X→∞ at fixed Q, then Q→∞ gives the convergent factor Σχ(j)/j=L(1,χ).

The negative constant persists for every fixed u>1. The rough part alone is eventually negative and its positive-part window energy eventually vanishes. The opposite positive main term in the rest follows after importing the unconditional T=o(X/log X) proved with the classical Mertens bound and its coefficient unit. Neither argument is uniform in u→∞, including u=u(X). With u varying, the small value of ρ(u−1) and the uncontrolled u-dependence in the errors are indispensable. No conclusion about good windows for the full tail follows from these leading constants alone.
