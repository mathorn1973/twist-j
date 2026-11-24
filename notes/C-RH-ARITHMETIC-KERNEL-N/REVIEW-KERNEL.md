# Independent paper review of the signed-split kernel bound

NON-CANONICAL. No authority. I reviewed the statement and the written proof in `research_round2/astra_kernel/PROOF.md` through its sharpening in Section 7. I did not inspect or rerun its checker. The following is a mathematical review of the bounds under the stated support and mask hypotheses.

## Complete covariance and the uniform majorant

For `d=ga`, `e=gb` with `g=gcd(d,e)`, writing `n=gm+t` with `0<=t<g` gives `floor(n/d)=floor(m/a)` and the equivalent equality at `e`. The fractional remainder of `m/a` is at most `(a-1)/a`, so adding `t/(ga)` cannot cross an integer. In one period the Chinese remainder theorem enumerates each pair of residues modulo `5a` and `5b` that agrees modulo five exactly once. The signed positive-minus-negative count in the five residue classes for `K_a` is exactly `H,-H,-H,H` when `a=1,2,3,4 mod 5`, by the endpoints of `[a,2a)` and `[3a,4a)`. This yields the factor `(2/5) chi(a)chi(b)/(ab)`. The resulting Jordan-totient formula is an exact regrouping. In the divisor cube of a set of split primes, the four local cases for participation in `d,e` have contributions `1,-2/p,-2/p,4`, giving `5-4/p` as stated.

For the sharpened absolute bound, `f=1*chi` is nonnegative at all prime powers and hence all integers. Its partial sum is the sum of `H(floor(u/a))` over `a<=u`, so it is between zero and `u`. At squarefree split integers, `f=|s|` and `f*f=|s|^2`. At other integers, the two functions remain valid majorants. Thus `sum_(g<=u)|s(g)|^2 <= u(1+log u)`, using the harmonic bound `sum_(k<=u) f(k)/k <= 1+log u`. In the exact-gcd grouping, `|s(ga)|<=|s(g)s(a)|` holds on all arguments, since a repeated common prime makes the left side zero. It gives

```
E_abs <= C sum_(g<=D) |s(g)|^2 (1+log(D/g))^2 <= C' D(1+log D).
```

The final step is the dyadic estimate with summable weights `2^(-j)(1+j)^2`. The argument uses absolute values and applies to any majorized mask.

## Finite interval, prefix loss and final exponent

Distinct reduced frequencies from the periods `5d`, `d<=D`, have circular separation at least `delta=(5D)^(-2)`. Orthogonality over a full common period gives the coefficient-square mean after coincident frequencies are combined. The first finite-interval argument loses one logarithm by bounding row sums of the off-diagonal geometric series. In Section 7 the dual sampling proof correctly drops that loss: on disjoint circular intervals of length `delta`, the inequality `G(t)<=delta^(-1) int G+int |G'|` follows by averaging the fundamental theorem of calculus. With `G=|P|^2`, Parseval gives `||P'||_2<=2 pi (X-1)||P||_2`. Duality therefore gives `X+delta^(-1)` up to an absolute constant. The start of the time interval shifts samples by unit phases only.

An independent proof of this last inequality uses a nonnegative tent on integers. Let `w(n)=max(0,1-|n-c|/M)` with an integer center `c` and `M=2X`; then `w>=1/2` on the time interval of length `X` for a suitable center. Its Fourier sum, up to a phase, is `M^(-1)|sum_(0<=j<M) e(jt)|^2`, bounded by a constant times `min(M,(M||t||^2)^(-1))`. The `j`-th frequency in either direction has distance at least `j delta` on the half circle. Thus each absolute row sum is bounded by

```
M + C sum_(j>=1) min(M, 1/(M j^2 delta^2)) <= C' (M+delta^(-1)).
```

Split the sum at `1/(M delta)` when it is at least one; otherwise use its convergent inverse-square tail. This confirms the same sharp large-sieve scale by a separate argument.

The moving endpoint on the block `X<=n<2X` is kept throughout. Decomposing each prefix into aligned binary intervals uses one interval per length. Pointwise Cauchy–Schwarz costs the first logarithm. At each length the intervals partition the coefficient array, so the sum of their complete means costs one `E_abs`, not one per interval. Summing lengths costs the second logarithm. Taking `D=floor((2X)^(2/3))` gives `(X+D^2)D << X^2`, hence the block square sum is `O(X^2(1+log(2X))^3)`. Dividing by `X^2` and summing the `O(log Y)` disjoint time blocks from `Y` to `Y^2` gives the fourth power claimed in Section 7. The earlier seventh power is valid with its weaker majorants. The exact tail partition and the positive-part norm comparison also follow: the quotient blocks give the stated integer endpoints, and positive part is one-Lipschitz.

## Sharpness and its hypotheses

For each fixed `2/3<a<1`, `X/D` tends to infinity for `D=floor(X^a)`. This makes the proportion of acceptable starts uniform for all primes in the chosen interval, after removing incomplete periods at the ends. At a common start the selected primes all retain value `K_p=-1` for `Omega(D)` consecutive integer shifts, so every contribution there is positive. The weighted square lower bound is proportional to `D(D/log D)^2/X^2`, as asserted. Adjusting the prime interval inward keeps every selected prime below the moving cutoff without changing the scale. This construction concerns masks selected for the given window. It makes no lower-bound assertion for the unmodified full signed sum and supplies no estimate beyond `d^3<=n^2` for those coefficients.

No mathematical gap was found in the reviewed scope. The conclusion is an independently reviewed paper deduction at candidate-D, not an independent execution or an authority change.
