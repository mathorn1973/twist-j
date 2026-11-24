# Transfer of a largest-prime conductor cutoff down to the cube root

**NON-CANONICAL. No authority. Candidate-D.** Take D=4X and the same dyadic w and G_X^star as in round 5. Write z≥2 for an arbitrary real threshold. The largest-prime conductor projection and the largest-prime raw support projection have an exact difference supported on smaller divisors, allowing the cutoff to be as low as D^(1/3) at square-root norm precision.

## 1. Exact transfer before truncating Fourier modes

Let L_z(n)=Σ_{r≤D,P⁺(r)≤z} A_r(D) Φ_r(n) denote the complete primitive projection, and let B_z(n)=Σ_{d≤D,P⁺(d)≤z}s(d)K_d(n). Use P⁺(1)=1 and P⁻(1)=∞. The full fixed-time expansion of each original squarefree split d is K_d=Σ_{r|d}(r/d)Φ_r. Write d=e q with P⁺(e)≤z and P⁻(q)>z by unique factorization. Then the condition P⁺(r)≤z on a divisor of d is simply r|e. Its projected part is

    Σ_{r|e}(r/d)Φ_r=(1/q)K_e.

As e and q have disjoint prime factors, the original weight factors as s(d)=s(e)s(q). Consequently

    L_z(n)−B_z(n)
    = Σ_{e≤D/z, P⁺(e)≤z} s(e)K_e(n)
         Σ_{1<q≤D/e, P⁻(q)>z} s(q)/q.                                (1)

The high-conductor projection minus its corresponding raw high-prime packet is the negative of (1). The formula retains all small and large prime cofactors and works for every integer n. In particular the size of the discrepancy has the elementary pointwise bound O(D/z): sum the right side over q first, use Σ_{e≤D/q}|s(e)|≤D/q, and apply partial summation to Σ_{q>z}|s(q)|/q²≪1/z.

Let E=D/z. If E≥1, the coefficients c_e of K_e in (1) are supported on e≤E and satisfy |c_e|≤|s(e)|(1+log D). On re-expanding this shorter polynomial into primitive conductors r≤E, each coefficient in front of Φ_r is bounded by

    Σ_{e≤E,r|e}|c_e| r/e ≪ |s(r)|(1+log D)^2.

This follows from squarefreeness and Σ_{m≤E/r}|s(m)|/m≤1+log D for the coprime factors in e=rm. Hence the sum of squared Fourier coefficients is O(E(1+log D)^5) by Σ_{r≤E}s(r)²≪E(1+log D) and Σ_a|b(r,a)|²≪1. The distinct primitive frequencies with r≤E have circle spacing ≫E^(−2), just as in round 3. Consequently the translated additive large sieve on the finite taper gives

    ||L_z−B_z||_w ≪ (1+log D)^(5/2) [√(XE)+E^(3/2)].                (2)

The empty case E<1 has zero discrepancy. For z≥D^(1/3), E≤D^(2/3) and (2) is O(X(1+log X)^(5/2)). The support reduction in (1) is what yields this bound; the coarser pointwise D/z estimate would demand z of order √X.

## 2. Two large primes and an explicit replacement on the original low-height spectrum

Fix D^(1/3)≤z≤D. Let G_>(n) be G_X^star restricted to P⁺(r)>z and G_≤ its complement. For n on the taper let C_z(n)=Σ_{d≤n,P⁺(d)>z}s(d)K_d(n). Then

    ||G_>−C_z||_w² ≪_ε X^(2+ε)                                        (3)

uniformly in z. To see this, apply the original Jackson smoothing to the complete high projection, which equals the full raw high packet minus (1). The raw packet is globally O(D) and has successive differences bounded by Σ_{d|v}|s(d)|≤3^ω(v)≪_ε X^ε on [3X/8,21X/8]. It therefore changes by O_ε(X^(1/2+ε)) per tapered time under the Jackson shifts as in MARKED-PRIME-CANCELLATION §2. The raw packet equals C_z at these times since n≤D and K_d(n)=0 for d>n. For the discrepancy (1), (2) also holds after Fourier multiplication by m_t, because the absolute multiplier is at most one and the frequencies keep the same spacing. This proves the comparison directly for the smoothed complete high projection. Its subsequent small-conductor and high-numerator cuts cost O_ε(X^(1+ε)) in norm by the same restricted large sieve and numerator estimates as for (3) in MARKED-PRIME-CANCELLATION. The height trimming estimate is uniform in the conductor mask, and the roughness threshold (log X)^2 is automatic for P⁺(r)>z. This proves (3).

For z≥D^(1/3) at most two distinct primes greater than z divide an integer ≤D. With primes in the following sums restricted to split primes, C_z has the exact smaller-argument expression

    C_z(n)=−2 Σ_{z<p≤n} T(⌊n/p⌋)
           −4 Σ_{z<p≤q, pq≤n} T(⌊n/(pq)⌋).                         (4)

Both the diagonal p=q and unordered distinct pairs enter. To check the signs, first mark one prime p in a supported d. Its incidence sum is −2 T^(p)(⌊n/p⌋), where T^(p)(x) omits support d divisible by p. Splitting T(x) at p gives T^(p)(x)=T(x)+2T^(p)(⌊x/p⌋). At x=⌊n/p⌋<p² the second term uses argument below p, so it equals 2T(⌊n/p²⌋). Summing incidences counts a d with two large primes twice. Subtract its raw weight 4s(e)K_e(⌊n/(pq)⌋), where e is free of both primes since n/(pq)<z, to leave one copy. This gives (4), including the repeated-prime subtraction. All T arguments are at most n/z≤17X/(8D^(1/3)). Finite prime counting can equivalently replace the sums over p,q by linear combinations of t(m)=T(m)−T(m−1) at these smaller arguments. When z≥√D, the double sum vanishes and the earlier one-prime expression is recovered.

Combining (3) with the inherited approximation to T gives ||T−(G_≤+C_z)||_w²≪_ε X^(2+ε). In particular all Fourier conductors with largest prime exceeding D^(1/3) can be replaced jointly by (4), provided the interaction of this exact explicit function with the retained G_≤ is kept. Equivalently, if P_≤≤ is the original signed determinant sum restricted to both remaining conductors, then

    P_≤≤ + 2 Re⟨G_≤,C_z⟩_w + ||C_z||_w²

obeys the same all-epsilon positive-part criterion as the full P_X^star. No assertion that (4) itself is small is used; the discrepancy is controlled in norm. This transposition combines the prior two-prime incidence method from LARGE-PRIME-HIERARCHY with the exact projection identity (1). The cube root is a sufficient threshold supplied by (2); its sharpness is unproved.

## 3. Every remaining Fourier conductor has at least three distinct split prime factors

At z=D^(1/3) put E=z²=D^(2/3). Starting from the original G_X^star, let G_core retain exactly the modes with

    z²<r≤D,       (log X)²<P⁺(r)≤z,

with all original height, numerator, smoothing and coprime cofactor data. In §2 the replacement already removes the entire class P⁺(r)>z in favor of the exact profile C_z(n) in (4). The extra modes removed from G_≤ here have r≤E. Their squared coefficient sum is O(E(1+log D)^3): use |A_r(D)|≤|s(r)|(1+log D), Σ_{r≤E}s(r)²≪E(1+log D), Σ_a|b(r,a)|²≪1, and |m_t|≤1. Frequency restriction only reduces that sum. The retained rational frequencies with r≤E are primitive and separated by ≫E^(−2) on the circle. Dominate w by the indicator of its interval of length O(X) and apply the translated additive large sieve. The squared norm of the extra discarded packet is therefore at most

    O((X+E²)E(1+log D)^3) = O(X²(1+log X)^3),

since E³=D²=16X². This covers the extra factor 4^(2/3) between E and the original lower conductor cutoff X^(2/3). It also applies to arbitrary subsets of the actual modes at these denominators.

Nonzero conductors are squarefree products of split primes. A product of at most two primes each at most z is at most z², so every surviving r has at least three distinct split prime factors. Combining the displayed norm bound and (3) with the block approximation to T yields

    ||T−(G_core+C_z)||_w² ≪_ε X^(2+ε).

Write P_core for the original determinant sum restricted to pairs of these core conductors, including the original strip, unequal-conductor requirement and small-gcd cutoff. The inherited far-pair, same-conductor and large-gcd estimates give ||G_core||_w²=P_core+O_ε(X^(2+ε)). Thus

    Q_core=P_core+2 Re⟨G_core,C_z⟩_w+||C_z||_w²

differs from ||G_core+C_z||_w² by O_ε(X^(2+ε)). The weighted norm comparison and the round 5 finite-block criterion show that RH is equivalent to (Q_core)_+≪_ε X^(2+ε) for every ε>0 on all sufficiently late dyadic X. No unconditional estimate for the difference between the original and reduced pair sums at that precision is required. This corollary was suggested in the team's internal review.
