# The complete prime cutoff, its critical contraction, and a logarithmic smooth part

**NON-CANONICAL. No authority. Candidate-D paper deductions.** Owner issue 2087, draft 2089, same candidate C-RH-ARITHMETIC-KERNEL-N. Action layer NOT_APPLICABLE. The all-ε bound for the full signed sum is **O**. The positive correction operator is studied with its actual coefficients. The operator lower test below is a comparison input and is identified as such.

## 1. An Euler completion equal to the whole incoming arithmetic profile

Let X be a sufficiently late dyadic integer, D=4X and z=D^(1/3). Let T(n)=Σ_{a≤n}t(a), t=χ₅*s, with the round-eight multiplicative coefficients. At a split prime p≡1,4 modulo 5, t(p^j)=−1 for every j≥1. At an inert prime p≡2,3, t(p^j)=(−1)^j, and t(5^j)=0 for j≥1. In particular |T(u)|≤u. Extend prefixes by their floor on real arguments and by zero below one. For y≥5 let T_y(n) sum t through n restricted to integers having every prime factor at most y. Include the integer one. This is the true smooth prefix and is different from the raw residue-kernel restriction.

For each cutoff frozen on a block define the signed completion

    L_y(n) = Σ_{d≤n, P⁻(d)>y} λ(d) T_y(⌊n/d⌋),     λ(d)=(−1)^Ω(d).     (1)

Here Ω counts prime factors with multiplicity and P⁻(1)=∞. All large primes occur, both split and inert. For p>y the new coefficient series at p is 1/(1+x); at smaller primes it remains that of t. Thus

    L_y(n) = T(n) + H_y[T](n),
    H_y[F](n) = Σ_{1<d≤n} h_y(d) F(⌊n/d⌋).                            (2)

The multiplicative h_y has h_y(1)=1, is trivial at every prime other than split p>y, and there has local series

    (1−x)/[(1+x)(1−2x)] = 1 + 2x²/[(1+x)(1−2x)].                     (3)

Indeed the true split series is (1−2x)/(1−x). At inert p>y the new and original series coincide. The factor 1/[(1+x)(1−2x)] has successive coefficients (2^(j+1)+(−1)^j)/3 for j≥0. All h_y(d)≥0 and every prime in a nonconstant term occurs at least twice. The first local coefficients at exponents 2,3,4 are 2,2,6. These identities can be checked by finite coefficient multiplication without using convergence of an Euler product.

For y=z and n≤D, only d=p² can occur in (2), with coefficient two. Therefore (1) is exactly the full round-eight arithmetic J_z on that range, by COUPLED-CUTS (4). In particular the original signed one-prime and unequal-prime terms and the split repeated correction have not been assumed small separately.

For y=D^(1/5), d>1 in (2) is p²,p³,p⁴ or p²q² with p<q. Every prime displayed here is split and strictly above y. A fifth prime factor counted with multiplicity would make d>D. For n≤D define

    K_y(n) = L_y(n) − 2 Σ_{y<p≤z} T(⌊n/p²⌋)
                     − 2 Σ_{p>y} T(⌊n/p³⌋)
                     − 4 Σ_{y<p<q} T(⌊n/(pq)²⌋).                       (4)

Equation (1) in this expression still includes both prime classes with every rough multiplicity through four. Equation (2) at its two cutoffs gives

    K_y(n)−J_z(n) = 6 Σ_{p>y}T(⌊n/p⁴⌋) = O(X/y³) = O(X^(2/5)).       (5)

The last inequality follows from |T(u)|≤u and Σ_{k>y}k^(−4)≪y^(−3). The difference thus has squared norm O(X^(9/5)) on the entire original taper. This is a strict power estimate for a difference of complete arithmetic profiles. It does not bound the full amplitude of either profile.

## 2. At σ>1/2 the entire true smooth prefix can be taken out

For a dyadic block Y and σ≥1/2 use the round-eight norm

    E_{σ,Y}(F)=Y^(1/2−σ) (∫_Y^(2Y)|F(u)|² du/u²)^(1/2).

For a frozen y=y_X→∞, equation (3), the two-block dilation estimate of round eight, and Minkowski give

    E_{σ,X}(H_y[F]) ≤ c_σ(X) max_{Y dyadic, Y≤2X/y²} E_{σ,Y}(F),
    c_σ(X) ≤ √(1+2^(2σ−1)) [Π_{p>y,split} h_{y,p}(p^(−σ))−1]
             ≪_σ y^(1−2σ)   (fixed σ>1/2, all large X).              (6)

For the product bound each local surplus in (3) is O_σ(p^(−2σ)) once y is large. Sum over all integers beyond y and use exp(v)−1=O(v) as v→0. In applying the two-block estimate each d>1 has d>y²; a dyadic start smaller than one contributes zero if its entire interval is below one. If there are no dilations the assertion is immediate. Because the smaller states on the right are T itself, the cutoff can be reset on each new dyadic block. With F=T, (2) and (6) imply boundedness of E_{σ,X}(T) if and only if E_{σ,X}(L_{y_X}) is bounded on all sufficiently late blocks. For the reverse direction use induction, taking c_σ(X)≤1/2 and including the finite initial norm maximum. No RH-size estimate enters the derivation.

Choose specifically y=log X. For every fixed η>0,

    sup_{0≤u≤4X}|T_y(u)| ≪_η X^η.                                   (7)

For 0<δ<min(η,1), the count of y-smooth integers up to 4X is at most (4X)^δ Π_{p≤y}(1−p^(−δ))^(−1). The logarithm of the product is O_δ(Σ_{2≤m≤log X}m^(−δ))=O_δ((log X)^(1−δ))=o(log X). Since |t|≤1, this proves (7). Deleting only the d=1 term from (1) costs O_η(X^(1+η)) in squared norm on the original taper after shrinking η. The single remaining joint sum is

    A_X(n)=Σ_{1<d≤n, P⁻(d)>log X} λ(d) T_{log X}(⌊n/d⌋).             (8)

Equations (6)–(7) and the round-eight comparison show, for each fixed σ>1/2 on all sufficiently late dyadic X,

    (Q₈)_+=O_σ(X^(1+2σ))  ⇔  E_{σ,X}(A_X)=O_σ(1).                   (9)

Here the comparison between Q₈ and T is the paper norm comparison in round8/REPORT §§1,5, with error exponent strictly below 2σ−1. At the cube root T_z has size of order X/log²X in the inherited opposing drift. With the moving logarithmic cutoff the entire new top smooth prefix satisfies (7). This uses the simultaneous change of every rough-mark term in (1). Only the rough multiplicity sum in (8) remains, and its length in multiplicity now grows with X.

Actual small coefficient values in the core do not make the terms of (8) separately negligible. Fix k≥1, take d to be a product of k distinct primes from [X^(1/k),(5X/4)^(1/k)]. There are ≫_k X/(log X)^k such d by fixed-ratio prime counting, and all their primes exceed log X eventually. For every integer n∈[3X/2,7X/4], T_y(⌊n/d⌋)=T_y(1)=1 exactly. The contribution of this specified actual subfamily is (−1)^k times its cardinality throughout that interval. Its squared sum there is ≫_k X³/(log X)^(2k). Thus an estimate that pays this subfamily by absolute values at the target scale fails. This is not a lower bound on the signed sum of a whole multiplicity layer or on (8).

## 3. Critical norm of the repeated-prime correction

The positive dilation operator H_y has a sharp threshold for strictly contracting the norm of *arbitrary smaller prefix inputs* at σ=1/2. We give its precise norm where the threshold lies, as this is not obtained by the two-block triangle bound of round eight. Write E_Y=E_{1/2,Y}. Put y=D^γ with 1/6≤γ<1/2 and define

    S(γ)=log(1/(2γ))
        + (1/2) ∫_{s,t≥1, s+t≤1/(2γ)} ds dt/(s t).                   (10)

The double integral is zero when its region has zero area. If M_X(F)=max_{Y dyadic, 1≤Y≤2X/y²}E_Y(F), then

    sup_{M_X(F)≤1} E_X(H_y[F]) = S(γ)+o_γ(1).                       (11)

The input class may consist of real step prefixes vanishing below one; the upper bound holds for any measurable such input. The supremum refers to the actual positive h_y in (2). No lower bound for H_y[T] follows from an arbitrary test input.

First isolate one prime scale. For 1≤q≤√(2X)/y set P=√(2X)/q, s_q=2Σ_{y<p≤P,split}1/p, and

    V_q F(n)=2Σ_{y<p≤P,split} F(n/(qp)²).

Only in this operator estimate F(v) denotes its extension on the incoming real argument. Integer-step F with integer q,p samples precisely its floor. Uniformly in q in this range,

    E_X(V_q F) ≤ q^(−1)[s_q+O_γ(1/log X)] M_X(F).                    (12)

To see this, at fixed n apply Cauchy–Schwarz with weights 2/p. Integrating on [X,2X) against dn/n² and changing the variable to u=n/(qp)² gives

    E_X(V_qF)² ≤ (s_q/q²)∫_1^(2X/(qy)²) |F(u)|² B_q(u)du/u²,
    B_q(u)=2Σ_{y<p≤P, X≤(qp)²u≤2X, split}1/p.                       (13)

The combination of endpoints in B_q is immaterial on the continuous integration boundaries. Write Z=√(X/u)/q. On this integration range Z≥y/√2. The prime number theorem in the two fixed split classes and partial summation uniformly give

    2Σ_{Z≤p≤√2 Z,split}1/p ≤ log 2/log(Z²)+O_γ((log X)^(−2)).

Endpoint primes contribute O(1/Z). This formula follows by integrating dv/(v log v) through v=√2 Z from Z. The same fixed-modulus estimate gives s_q=log(log P/log y)+O_γ(1/log X), uniformly even when P is very close to y, as these are estimates for cumulative differences with absolute error.

On each occupied dyadic [Y,2Y), bound B_q by the full short prime count above, evaluated at the upper endpoint of the main bound in u. Summing these suprema gives at most s_q+O_γ(1/log X). Indeed with Y=2^j, L_q=log(X/q²) and 0≤j≤floor(log₂(2X/(q²y²))), the sum to bound, up to O_γ(1/log X), is

    Σ_j (log 2)/(L_q−(j+1)log 2).

Every denominator is at least 2log y−O(1). Comparison with the integral of 1/v gives log(L_q/(2log y))+O_γ(1/log X) when L_q≥2log y. If L_q is slightly smaller, there is at most one occupied level and its cost is O_γ(1/log X). Replacing L_q by log(2X/q²)=2log P changes the value by O_γ(1/log X). There are O(log X) short-prime estimate errors, each O_γ((log X)^(−2)). Substituting these upper bounds and M_X(F) into (13), then using sqrt(s(s+e))≤s+e for s,e≥0, proves (12). The gain comes from integrating the actual density of prime dilations across the dyadic boundaries.

At 1/6≤γ<1/2, every d≤2X in (2) contains at most five prime factors counted with multiplicity. The terms with at least one exponent ≥3 have total Σ h_y(d)/√d=o_γ(1). For each fixed exponent pattern, its coefficients are bounded since the degree is at most five. A factor with exponent ≥3 costs O(y^(−1/2)) summed over all integers >y, while each square factor costs only O_γ(1) by the bounded reciprocal prime sum through √(2X). There are finitely many patterns. The ordinary two-block dilation bound pays these terms at o_γ(1)M_X(F).

The remaining terms are single p² with split p and unordered distinct p²q² with split p,q. The single bound is (12) at q=1. For the pairs use positivity to dominate their absolute action by the ordered sum on |F|, including the diagonal and with the factor one half for the two orderings. Its norm is bounded by Σ_{y<q≤√(2X)/y,split} E_X(V_q |F|). Thus the limiting coefficient is at most

    2Σ_{y<p≤√(2X)}1/p + 2Σ_{p,q>y, pq≤√(2X)}1/(pq) + o_γ(1),          (14)

where the primes displayed are split and the last pair sum is ordered. The accumulated errors of (12) cost O_γ(1/log X) since the sum of 1/q is bounded. Formula (14) tends to (10). For fixed u>v≥1, the measure 2Σ_{p>y,split}p^(−1)δ_{log p/log y} assigns [v,u] mass tending to log(u/v). Interval subdivision on a fixed compact rectangle then gives convergence of the two-dimensional ordered product integral. The boundary s+t=1/(2γ) has zero limiting measure and the diagonal p=q costs o(1). This proves the upper bound in (11).

For the reverse take the integer step test F(u)=floor(√u) for u≥1 and zero below one. Its E_Y norms are at most √log 2. Restrict the above positive square terms to d≤X^(1−δ) with fixed small δ>0. Throughout X≤n≤2X each evaluation differs from √(n/d) by relative O(X^(−δ/2)). The limiting reciprocal coefficient mass in this truncated region is given by (10) with both cut endpoints 1/(2γ) replaced by (1−δ)/(2γ), using zero for an empty single range. Let δ decrease to zero. Dividing by √log 2 and using the same full output interval gives the matching lower coefficient S(γ). This verifies sharpness in the universal input class without assuming a large value of the actual prefix.

The function S is continuous and strictly decreasing on [1/6,1/2), since already the single-prime logarithm is strictly decreasing and the other term is nonincreasing. At 1/6 it exceeds one since log 3>1. At 1/5 the integral term is at most 1/16: put s=1+a,t=1+b with a,b≥0, a+b≤1/2, and bound 1/(st) by one in a triangle of area 1/8 before the outer half. Also log(5/2)<15/16, since the first four terms of exp(15/16) already exceed 5/2. Hence S(1/5)<1. There is a unique γ*∈(1/6,1/5) with S(γ*)=1. For fixed γ<1/6 the single p² test already has limiting mass log(1/(2γ))>1. For γ≥1/2 the correction vanishes on the central dyadic block. Thus, among fixed γ>0, eventual contraction by a constant strictly below one for this positive operator occurs exactly for γ>γ*. Equality does not give a uniform contraction gap. At the cube root the sharp factor is log(3/2), replacing the earlier upper factor √2 log(3/2).

At the explicit fifth-root cutoff the identity (2) and (11) imply by lower-block induction

    sup_X E_X(T)<∞  ⇔  sup_X E_X(L_{(4X)^(1/5)})<∞,                    (15)

with suprema equivalently restricted to all sufficiently late dyadic X and finite initial norms. For each fixed σ>1/2 use (6). The quarter-root and original cube-root scales are contained in the same contraction result. The critical σ=1/2 implication is for these arithmetic norms; the previously paid Fourier error has an ε exponent and does not give an O(X²) transfer to Q₈ at the strict endpoint.

## 4. What the transfer leaves open

Equation (5) pays for a fifth-root reallocation of the full cube-root profile to better than square-root precision. Equation (8) pays for the entire new smooth term after moving the cutoff much further; the cost is the presence of all rough multiplicities. Equation (11) identifies the exact limitation on absorbing the repeated-prime correction by a uniform critical-norm induction on earlier inputs. None of these bounds supplies cancellation at square-root scale among the remaining actual rough products in (8), or the equivalent joint profile at the fifth root. The prescribed all-ε bound for the complete Q₈, Q₇ and the original J_z is O.

Read round8/COUPLED-CUTS §§1–3, round8/REPORT, FOUNDATION §2 and the round-seven PRIME-PUSHFORWARD at incoming draft 6a91ef48f6454743797614503aa5863dde54befb. The prime-direction work in neighboring C-HUANG-ARITHMETIC-BRIDGE-N at fd6232aa10da26a374e421d6d46538b36b41aafb treats a different Möbius filter and complete windows. The neighboring C-RH-THREE-INTERFACE-SYNTHESIS-N at ceb77e3632ec4617c54d8e1fd504d3b1c99dd106 retains its own coefficients, ownership and claims. The only prime-distribution input beyond the frozen candidate estimates is the same fixed-modulus prime counting already used in round eight; the needed short-prime and cumulative reciprocal estimates follow from [Yamada, Explicit formulae for primes in arithmetic progressions, I, Theorem 1.2(4) and Table 5](https://arxiv.org/html/1306.5322v4#S1) at fixed modulus five. For instance the listed row with α₁=1 and A=3 suffices after removing higher prime powers and partial summation. The finite table is not used for arbitrarily many powers of the logarithm. No numerical, symbolic, or scientific executable, independent verification, or formal gate was used. No RH or equivalent hypothesis was assumed.
