# Exact recurrence of a causal H3 write

This argument uses the finite causal witnesses in [the predecessor](https://github.com/mathorn1973/twist-j/pull/2024) for the frozen four-wire launches on ranks 0, 22 and 43. It gives a computable bound on a second witness on each launch's native forward trajectory.

## The native tick is a bijection

Use the integral basis (1, j, j², j³), where j is a primitive fifth root. Set ρ = j², J = 1 + ρ, h(z) = z times its complex conjugate, and θ = h(J). The tick applies the contact matching selected by the current bit, applies the site collisions, and flips the bit. To invert it, recover the old bit, undo the collisions, and undo contact on the old matching.

A contact refuses if the rail words differ modulo 2. The unchanged pair then also refuses in the inverse. Otherwise the words have the form m + d and m − d with integral midpoint m and half-gap d. Contact sends d to ρd and preserves m. The resulting words still agree modulo 2, so the inverse rotates the new half-gap by ρ⁻¹. Each lane's matching consists of disjoint bonds. Along each bond, contact preserves each rail sum and the sum of the two Hermitian norms, since h(ρd) = h(d).

A collision is idle if either half-gap is nonintegral. For integral matter and radiation half-gaps d and f, B1 requires d ≠ 0 and h(f) = θh(d), while B2 requires f ≠ 0 and h(d) = θh(f). Both active guards force both gaps to be nonzero. If both guards held, they would give θ² = 1. In fact θ = 2 + ρ + ρ⁻¹ is positive, and θ = 1 would give ρ² + ρ + 1 = 0, contradicting the order of ρ.

The unit identity J⁻¹ = −(ρ + ρ³) makes both updates integral. B1 sends (d, f) to (Jd, J⁻¹f), and B2 applies the reciprocal update. Either active update preserves both midpoints and exchanges the two Hermitian gap norms. The output has integral half-gaps and selects the other active guard, so a second collision restores the input. An idle collision fixes its input. The collision is therefore an involution. Since the sum of the norms of m + d and m − d is 2h(m) + 2h(d), the collision preserves the sum of all four rail norms at its site. The whole native tick is a bijection and preserves the whole-field sum H of Hermitian norms.

## The conserved account bounds the period

For one rail write z = a₀ + a₁j + a₂j² + a₃j³ with integer coefficients. Let Tr be the field trace from the fifth cyclotomic field to the rationals. In the expansion of h(z), the trace of j raised to i − k is 4 when i = k and −1 otherwise. The contribution of this rail to Q = Tr(H)/2 is therefore

> q(z) = Tr(h(z))/2 = [5 Σ aᵢ² − (Σ aᵢ)²]/2.

Let a be the four-component coefficient vector and A = 5I − eeᵀ, where e is the vector of four ones. A has eigenvalue 1 along e and 5 on its orthogonal complement. Its inverse is (I + eeᵀ)/5, with diagonal entries 2/5. Applying Cauchy–Schwarz in the inner product defined by A to the ith coordinate gives

> aᵢ² ≤ (2/5)(aᵀAa) = 4q(z)/5.

Every rail has 0 ≤ q(z) ≤ Q = 774. Since 4 × 774 < 5 × 25², each coefficient lies between −24 and 24. The 8 by 4 grid has 128 rails with four coefficients each. This bounds the number of possible augmented states by 2 × 49⁵¹², where the factor of 2 counts the matching bit.

On the finite set with Q = 774, the native tick is a permutation. Every launch returns to its initial augmented state with an even least period P ≤ 2 × 49⁵¹². To compute P, advance the native trajectory until the entire field and the matching bit first equal their launch values. This needs only the launch and current states plus a step counter.

## A later causal write on the same trajectory

On each of the three ranks the predecessor records source B2 at tick 125, restoration of the ordered word at 157 B, retention through 158 B, and a material worker B2 at 159 B. At 159 C the worker matter pair moves. Conservation of the sum along each contacted matter rail implies that the memory pair also changes, consuming the restored word. The fresh source-undo control and the separate compensated exchange before the read each remove that worker write.

Let k be the smallest positive integer with kP ≥ 36. The same native cuts occur at ticks 125 + kP, 157 + kP, 158 + kP and 159 + kP. The new source event occurs strictly after the first work, and the second restoration and read follow consumption of the first word in the same continuous trajectory. To reproduce the controls, undo the new source event in a fresh comparison and make the compensated exchange in a separate copy of the repeated pre-read state. Exact equality of the relevant fields and matching bits makes both comparisons reproduce the earlier local outcomes. The actual trajectory applies neither intervention. Further multiples of kP supply arbitrarily many time-separated copies of the causal witness.

Since P is even and k is minimal, kP ≤ P + 34. A qualifying later write therefore occurs no later than tick 159 + kP ≤ 193 + 2 × 49⁵¹², separately for each launch. The bound guarantees a later cyclic witness and a finite procedure to locate it. It does not estimate the period at the scale of a bounded empirical scan or imply another qualifying write within the first cycle. A scan that observes neither a later witness nor a full return limits only the window measured.
