# Logarithmic shares break the actual joint cancellation

**NON-CANONICAL. No authority. Candidate-D paper deduction.** Same round-nine owner and candidate. Action layer NOT_APPLICABLE. This is a falsification of a proposed weighting of the complete arithmetic profile. The original unweighted problem remains **O**.

Let X,D,z,T,T_z and w be the frozen cube-root data, with z=(4X)^(1/3). In the exact J_z=T_z−Σ_{p>z}T(⌊n/p⌋)−Σ_{z<p<q}T(⌊n/(pq)⌋), a possible way to limit the aggregate dilation weight is to attach to each marked prime the share log p/log n. This particular prescription gives the following complete observable on the taper, with both prime classes and all original floors:

    J_z^log(n)=T_z(n) − S₁(n)/log n − S₂(n)/(log n)²,
    S₁(n)=Σ_{p>z} (log p)T(⌊n/p⌋),
    S₂(n)=Σ_{z<p<q} (log p)(log q)T(⌊n/(pq)⌋).

The sums omit zero floors; the primes in the second sum are distinct. Here T_z is unchanged and is the actual restricted t prefix. For every fixed A>0, uniformly on the original taper,

    S₁(n)=O_A(X/(log X)^A),
    S₂(n)=(κ/2)n+O_A(X/(log X)^A),       κ=1/U(1)>0.                  (1)

Indeed write θ(v)=Σ_{p≤v}log p=v+O_B(v/(log v)^B) and L=log X. This is the fixed-modulus prime number theorem already used in round eight, summing the two classes of each type and removing the higher powers. All count arguments in a nonempty difference in this calculation are at least z. Expanding T in its increments t, |t|≤1, and replacing θ(n/m)−θ(z) by n/m−z incurs O_B(X L^(1−B)) summed over m≤n/z. Interchanging the finite sums or the corresponding integrals gives

    S₁(n)=n∫_1^(n/z) T(u)du/u²+O_B(X L^(1−B)).

For ordered prime pairs, first consider the cumulative weighted count through a product v≥z². With p≤v/z the inner difference is θ(v/p)−θ(z). Replacing it by v/p−z costs O_B(vL^(1−B)) after summation over p with weights log p, since Σ_{p≤D}(log p)/p≪log D by partial summation. The outer weight v/s−z vanishes at s=v/z, is at most v/z at s=z and has derivative −v/s². Partial summation of θ(s)−s therefore costs another O_B(vL^(1−B)). The resulting main measure is ordinary ds dt on s,t>z, st≤v. Sum these errors at v=n/m against t(m), at total cost O_B(XL^(2−B)). Removing the equal-prime contribution costs O(X L²/z) by |T(u)|≤u. Division by two gives the unordered distinct sum. The change of variables v=st has measure dv ds/s with z<s<v/z. Finally take u=n/v to obtain

    S₂(n)=(n/2)∫_1^(n/z²) T(u)log(n/(z²u))du/u² + O_B(X L^(2−B)+X L²/z).

The two inherited signed moments are ∫_1^∞T(u)du/u²=0 and ∫_1^∞T(u)log u du/u²=−κ. Since n/z and n/z² are fixed positive powers of X up to constants, the inherited unconditional |T(u)|≪_B u/(log u)^B gives tails smaller than every specified inverse logarithm, even after multiplication by log(n/z²). Equation (1) follows, with the plus sign for its pair coefficient.

Round8/COUPLED-CUTS (4),(8) yields T_z(n)=−κ(log 2−1/2)n/(log n)²+O(X/L³) on this same taper. Adding the two exact weighted contributions proves

    J_z^log(n)=−κ(log 2)n/(log n)²+O(X/L³).                            (2)

In particular its squared taper norm is asymptotic to (κ log 2)² Σ_n w(n)n²/(log n)^4, and so has order X³/L⁴. The unchanged repeated split-prime correction in the true identity has size O(X/z) pointwise; adding it to (2) preserves the same main term and norm asymptotic. This identifies the loss in the *combined* modified profile. The logarithmic singleton has canceled to every fixed order, but its weighting and that of the actual pair change the balance against T_z. A method using logarithmic differentiation with additional compensating contributions is outside this counterexample.

Read the true joint profile in round8/COUPLED-CUTS §§1–3 and the signed moments and cumulative prime-count method in round7/PRIME-PUSHFORWARD §§2–3, all at 6a91ef48f6454743797614503aa5863dde54befb. For the arbitrary fixed B used here see [Thorner and Zaman, Refinements to the prime number theorem for arithmetic progressions, Corollary 1.4 and Remark 1.5](https://arxiv.org/html/2108.10878v2). At fixed modulus five any exceptional exponent β<1 gives only O(v^β), and the displayed exponential error is smaller than v/(log v)^B for every fixed B. Summing the four reduced residue classes and including the single prime 5 gives the stated θ estimate. This is a paper argument with no scientific execution or independent confirmation.
