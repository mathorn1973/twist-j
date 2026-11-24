# Paper opposition of completeness and growing weight

**NON-CANONICAL. No authority. Internal shared-context paper review of candidate-D deductions.**

Reviewed the complete `FOUR_UNIT_COMPLETENESS.md` and `GROWING_WEIGHT.md`,
including the latter's explicit empty-sum case, against the predecessor's
`THREE_UNIT_OBSTRUCTION.md`, `SPLIT_COORDINATES.md`,
`DENOMINATOR_RIGIDITY.md` and the integral phase projection in
`PARALLEL_REVIEW.md`. The predecessor is pinned at
`0b81796c01d4bee47eceb6e451670ea0d233610b`. No scientific program, finite
enumeration or primality test was executed for this review.

## Verdict

No mathematical error was found in either stated domain. The completeness
proof establishes the stronger content-gcd identity simultaneously for
every divisor of the specified product M, including repeated prime factors.
The growing-weight proof applies the owned full-divisor theorem to bound
the entire proper gcd, not merely one of its prime factors. Its conclusions
about a growing necessary weight retain their explicit size hypotheses.

## Four-unit completeness

1. **Split zero divisors.** Distinct signed labels by themselves do not imply
   that their difference is a unit. The proof correctly adds equality of the
   two quadratic norms. If one split component agrees, the fixed common norm
   forces the other component to agree. The predecessor's injective label
   kernel then excludes agreement at every prime divisor of M. This proves
   invertibility modulo all of M, rather than merely nonvanishing in the
   whole split algebra. The same argument applies to the relevant pair sums.

2. **Four equal norms.** Vanishing of the sum and the inverse sum makes the
   first and third elementary symmetric functions zero. The resulting even
   polynomial pairs its nonzero roots as x and -x, with multiplicities.
   Equal norms promote the first-coordinate pairings to whole-algebra
   pairings; the common signed labels promote them to identities modulo M.
   Thus a zero at one prime already gives the full gcd M.

3. **Two norms of each sign.** With a noncancelling same-norm pair, its sum
   is a unit. Conjugating a whole-ideal relation forces U=-V. Equality of
   these signed unit labels is a global modulo-M condition. Exponent sums
   can be made exactly equal by changing one exponent by 2h times an
   integer; the two centered exponents retain opposite parity. Both sign
   possibilities are handled: a Lucas pair directly, or an anti-trace pair
   converted by the exact modulo-M identity L_(n+h)=phi^h times
   (phi^n-(-1)^n phi^(-n)). Odd h is essential to this conversion.

4. **Three norms of one sign.** For E=x+y+z-1 and all three norms -1,
   direct expansion gives T_x=-E-yz conjugate(E),
   T_y=-E-xz conjugate(E), and
   T_x-T_y=z(x-y) conjugate(E). The explicitly selected distinct same-norm
   labels make the last coefficient invertible modulo M. Hence both
   transformed relations vanish modulo D if and only if E does, for
   every divisor D of M. If all labels agree, norm(3x)=norm(1) would force
   a prime divisor of 10, which the domain excludes.

5. **Prime-power multiplicity.** The proof does not lift a field zero
   without justification. Field arguments either force a universal label
   identity, already valid modulo M, or exclude every prime divisor.
   All remaining reductions are equalities modulo M or multiplication by
   units modulo M. This is sufficient for every divisor D, and therefore
   for the full content valuations used in the gcd statement.

6. **Fifth-root phases.** The integral direct-sum basis B plus jB makes
   whole rational-ideal divisibility equivalent to two real-coordinate
   conditions. Each coordinate keeps weight at most four. Their two
   gcd representations require at most four Lucas menu entries together.
   A separator at p and not q therefore supplies an individual menu entry
   with the same separation direction.

The result concerns m=5^k, k>=1, h=5m and rational whole-ideal divisibility.
It does not classify arbitrary even orders or a selected prime ideal.
It does not prove that four units separate every prime pair. It proves
that the prescribed complete Lucas menu detects every separation available
at weight at most four, with arbitrary integral exponents and fifth-root
phases. Intersections of menu outputs need not themselves arise from one
four-unit expression; the draft explicitly preserves this distinction.

## Unrestricted exponents and growing weight

1. **Simultaneous reduction.** A nonempty test can be normalized by its
   first integral unit. For v<=w actual terms, Q^(w-1)+1 residue vectors
   in at most Q^(w-1) boxes give a positive index difference
   D<=Q^(w-1)<=m. The five-part of D therefore divides m=5^k, including
   D=m. Half-open intervals give the strict bound |b_i|<m/Q, so the
   exact integer replacement is ceil(m/Q)-1, including divisible m/Q
   and its endpoint case. Adding b_1=0 does not enlarge the stated span.

2. **Whole divisor.** The inherited theorem bounds the entire proper gcd
   by one nonzero lifted norm. It applies to the unchanged original
   expression in its new rational-affine exponent representation.
   The inequalities C_H<=w phi^(H/2) and H<=2B_Q/D yield
   g<=w^(4Q^(w-1)) phi^(4B_Q)<=V_w(m,Q). A proper g satisfies this
   for every admitted Q, so taking their finite minimum is justified.
   No assertion about individual prime valuations is substituted for the
   full-divisor theorem. Empty and one-term tests are treated separately.

3. **Adaptive menus.** The bound is pointwise for every admitted unit
   sum, so choosing later exponents from previous results does not evade
   it. This does not bound a product or least common multiple of many
   separately extracted small gcds. The draft's assertion about primes
   above U applies to their bases; it explicitly avoids conflating a
   large power of a small prime with a large prime.

4. **Asymptotics.** Q=floor(m^(1/w)) is admitted for fixed w and gives
   log U=O_w(m^(1-1/w)). The displayed odd-index Binet identity gives
   log A=2m log(phi)+o(1), so every fixed positive rational power of A
   eventually exceeds the proper-output bound. The integer certificate
   U^b<A^a states the finite-input comparison without rounding.

5. **Growing necessary weight.** If r(w-1)>k, the claimed lower bound
   is immediate. Otherwise Q=5^r is admitted. For 5^r>2/delta the
   coefficient 2delta-4/5^r is positive, yielding
   5^(r(w-1)) log w>=c m. Since this case has w<=k/r+1, taking
   logarithms produces the claimed O(log log(k+2)) error. Proper
   outputs at weights at most three have already been excluded by the
   predecessor. The conclusion applies to a separator of two primes
   each at least A^delta, but existence of infinitely many such sides
   is expressly not supplied.

6. **Covering versus separation.** Counting multisets gives at most
   binomial(t+s,s) values from sums of at most s alphabet elements.
   With t=20m and a prime of exponential size in m, full quadratic
   coverage requires weight bounded below by a positive multiple of m.
   The proof correctly presents this as a coverage restriction, not as
   an additional lower bound for one pair separator.

## Evidence and attribution boundary

The related parallel arity result was reported through personal context;
its full current proof and computational package were not read in this
review. No novelty, priority or independent-discovery claim is made.
The growing-weight derivation uses the explicitly read, owned denominator
theorem and its own written pigeonhole argument, not the unseen parallel
proof. A detailed equivalence or difference claim between those packages
would require reading the latter in full.

The completeness theorem retrospectively proves completeness of the
previously frozen m=25 menu. It changes no finite input, program or output
and supplies no independent computational confirmation. The existing finite
run retains its original one-architecture candidate-C status. This review
is internal paper opposition, not blind or external peer review.
