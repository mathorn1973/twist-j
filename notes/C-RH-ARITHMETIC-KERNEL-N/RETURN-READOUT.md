# C-RH-ARITHMETIC-KERNEL-N / what a return stream determines

NON-CANONICAL. No authority. The written deductions are candidate-D. The exact finite checks are candidate-C. This comparison uses PR #2085 at `edfcb59a13ae8bdeaaeb26d6d6e0a8e68fa4f397`. It preserves that proposal's ownership of the content identity, window staircase and equal-order prime witnesses. The signed tail estimate for the actual coefficients remains open.

## 1. Full horizontal streams have a precise quotient

Write `O=Z[j]`, `phi=-j^2-j^3`, `alpha=phi^2`, and `B(r,e)=cont(1-e alpha^r)` for `e=+1,-1`. The content means the gcd of the integer coefficients in the integral basis of `O`. At an admitted index `n>1`, odd and prime to five, put `x=chi_5(n)` and `r=(n-x)/2`. The existing content identity gives `R(n)=B(r,x)`.

Let `d>1` be odd, squarefree and prime to five. For each `p|d` let `h_p=ord_p(alpha)`, where the modulus denotes the whole rational ideal. Write `h=lcm h_p`. Define an unmasked bit `epsilon=1` when all `v_2(h_p)` are equal and positive and `epsilon=0` otherwise. Then the full Boolean stream `b_d(n)=[d|R(n)]` is given by

```
chi_5(n)=+1:  hit iff n = 1 mod 2h;
chi_5(n)=-1:  hit iff epsilon=1 and n = h-1 mod 2h.
```

For the first row, `alpha^r=1` modulo `d` iff `h|r`. For the second row, work at each prime in the norm-one group of `F_p[phi]`. In the nonsplit algebra this is the cyclic norm-one subgroup of `F_(p^2)^*`. In the split algebra it consists of `(a,a^-1)`. Its unique involution is `-1`, so the negative power condition is `r=h_p/2 mod h_p` when `h_p` is even, and has no solution for odd `h_p`. If two positive valuations differ, those congruences force conflicting valuations for `r`. If the valuations agree and are positive, `h/h_p` is odd for every `p`, and `r=h/2 mod h` is exactly the joint solution. This proves the displayed formula.

The bit is observable only when `5` does not divide `h`. If `5|h`, the negative congruence forces `n=-1 mod 5`, which has the positive character. If `5` does not divide `h`, the negative congruence when allowed meets the negative character classes modulo five and yields infinitely many hits. The positive part always determines `h`: on `n=1+10k`, `k>=1`, the least hit position is `h/gcd(h,5)`, and on `n=9+10k` there is a hit iff `5` does not divide `h`. Thus equality of the *whole* streams is equivalent to equality of `h` and equality of the visible bit, with the latter set to zero at `5|h`.

For a prime power, its flag for a pairwise gcd is the intersection of the two start/neighbor flags, and its flag for the lcm of these gcds is the union of the pairwise-gcd flags. For a product of distinct primes, the lcm may see different primes through different neighbors. Thus the individual full-product stream described above does not in general determine its lcm-window flags. For factors with identical individual prime-power flags this qualification disappears. Any common family of neighbors, even one chosen from the previously seen Boolean observations, gives the same visibility for such factors. If a modulus block has only all-or-nothing gcds with every return term, then gcd and lcm of those observed divisors preserve the whole block or its absence. A full integer gcd can reveal the numeric modulus: once `d|R(n)`, the integer `gcd(d,R(n))` equals `d`.

For a paper example of recombination, `11` has order 5 from `L_5=11` and `19` has order 9 from `L_9=76` and `L_3=4`. There is an odd prime `q` of order 45. Indeed, `L_15=1364` and `L_45/L_15=1364^2+3=19*97921`. Take any prime factor `q` of `97921`. It differs from 19 and is prime to `L_15`, since `gcd(L_15, L_15^2+3)=1`. It is also prime to `L_9=4*19`. The order divides 45 and cannot divide 15 or 9, so is 45. The full Boolean streams for `11*19` and `q` agree, both with odd order 45. At the admitted start `n=91` with exponent `r=45`, the positive neighbors `101` and `109` of exponents 50 and 54 return 11 and 19 separately. Hence `11*19` divides `A_18(91)`. A prime of order 45 cannot return to any neighbor in that interval, so `q` does not divide `A_18(91)`. This illustrates why a bound on learning from aggregate windows needs the individual profile equivalence used below.

## 2. The exact information lost by the signed row

Take the equal-order split primes `101` and `151` from PR #2085. A paper certificate is `B(25,+1)=L_25=11*101*151` and `B(5,+1)=L_5=11`; each prime has order dividing 25 and not dividing 5, hence order 25. Both are congruent to 1 modulo five. Thus `d=101` and `d'=101*151=15251` have identical entire Boolean streams. Both have residue 101 modulo 150. Their weights are respectively `s_5(d)=-2`, `s_5(d')=+4`.

This gives a collision after including the actual residue kernel. At `N=15251`, both moduli lie in the summation range, and their quotients are `151` and `1`. Both have residue 1 modulo five, so both row kernels `S_chi(floor(N/d))` equal 1. The same equality holds at every `N=(1+5k)*15251` with integer `k>=0`. The actual signed contributions remain `-2` and `+4`. There is no row rule from the full Boolean stream, this modulus-residue information, and the residue kernel to the signed contribution. Since the two prime flags coincide, the collision also survives every common forward lcm-window for these squarefree inputs. More generally, if a class contains `r` distinct split primes of the same order, all `2^r-1` nonempty squarefree products have the same Boolean stream. A class with `r>=2` contains both signs. This conclusion does not assert that such `r` are unbounded.

The same obstruction occurs wholly inside the complementary range `d^3>N^2`. The number `241` is a split prime, as it is 1 modulo five and has no divisor among the primes `2,3,5,7,11,13` up to its square root. Multiply both moduli by 241 to obtain `d=101*241=24341` and `d'=101*151*241=3675491`, and set `N=d'=151d`. Since `24341>151^2=22801`, we have `d^3>(151d)^2=N^2`; the same strict inequality holds for `d'=N>1`. The individual flags for 101 and 151 are identical, and both products now share the same additional factor 241. Hence their full Boolean streams and common lcm-window flags still agree. Both moduli are 41 modulo 150 and their integer quotients at `N` are again `151` and `1`, so both kernels equal 1. The signed tail contributions are `+4` and `-8`. This is a paper witness for loss of an individual tail contribution under the stated observations.

The signed transform itself retains these coefficients. With `T(0)=0` and `a(n)=T(n)-T(n-1)`, the step kernel has a jump `chi(n/d)` precisely at multiples of `d`, so `a=s_5*chi` as Dirichlet convolution. The inverse of `chi` is `mu chi`, since complete multiplicativity gives `chi*(mu chi)` equal to the convolution identity, including at numbers divisible by five. Consequently `s_5=a*(mu chi)`. Thus the exact aggregate, given for all integer arguments, preserves the full signed information. This is a statement about recovering coefficients, without any assertion that a bound for the aggregate requires a coefficientwise decoder. The collision tests the proposed replacement of each signed row by its return-order label, without asserting indistinguishability when the integer label `d` itself is provided.

## 3. Vertical order reveals what the horizontal quotient forgets

Now let `d>1` be odd and prime to five, with arbitrary prime exponents. Write `h=ord_d(alpha)`, `B=B(h,+1)`, and `H_k=ord_(d^k)(alpha)`. Then for every `k>=1`,

```
H_k = h*d^k/gcd(d^k,B).
```

For `p^a||d`, put `b_p=v_p(B)`. In `O`, the integer divisibility order of `alpha^h-1` at `p` is exactly `b_p>=a`. For odd `p`, the coefficientwise binomial expansion shows that taking the `p`-th power of a unit congruent to one modulo `p^b` with exact `b>=1` raises the valuation of its difference from one by exactly one. The leading term is `p` times the previous difference, and each of the other terms is divisible by `p^(b+2)`. Taking a power coprime to `p` preserves the valuation for the same reason. Neither step requires the residue of the leading coefficient to be invertible in the split ring. Thus

```
v_p(alpha^(h*m)-1) = b_p+v_p(m)
```

for every positive `m`. Since an exponent giving `1 mod d^k` is already a multiple of `h`, its least possible quotient by `h` is `prod_(p^a||d) p^max(0,ak-b_p)`. This proves the formula, including cases where one prime of `d` already divides the order supplied by another prime.

Two different squarefree moduli `d,d'` with the same first order `h` have the same `B`. At each height their quotient `H_k/h` carries precisely the prime factors with `b_p<k`, each to exponent `k-b_p`. They first separate at `k=1+min_(p|d xor p|d') b_p`. For the witness above `b_101=b_151=1`, so their depth-two orders are already `2525` and `381275` respectively. More generally the ratio `H_(k+1)/H_k` is exactly `d` once `ak>=b_p` for every `p^a||d`. Choosing `3^k>B` suffices without knowing the factorization of `d`. The positive progressions of Section 1 recover each `H_k` from full flagged streams for the moduli `d^k`, irrespective of squarefreeness or visibility of the negative branch. This gives an injective oracle with enough vertical order data. It supplies neither a complexity bound for obtaining those flags or factoring the recovered modulus nor an estimate for the weighted signed sum.

## 4. A quotient distinguishes one-term gcd loss from an arithmetic operation

For the PR's block `Q_j=L_(3^(j-1))^2+3`, every prime power in the factorization has the same order `h=3^j`. For positive integers `t` the content `B(5h,+1)` divides `B(5ht,+1)`: the higher cyclotomic difference is a multiple of the lower difference in `O`. Both contents occur at admitted positive-sign indices `10h+1` and `10ht+1`. The coefficientwise binomial formula gives, for every prime `p|Q_j`,

```
v_p(B(5ht,+1)/B(5h,+1)) = v_p(t).
```

It follows that `gcd(Q_j, B(5ht,+1)/B(5h,+1))=gcd(Q_j,t)`. This extends the same type of quotient calculation as the fixed Fibonacci vertical-gcd formula reviewed in PR #2085. A ratio of returns therefore presents a different operation than a gcd against a single return. Its splitting ability here exactly matches the already supplied multiplier `t`. No choice of `t` that finds a prime factor cheaply is furnished by the identity.

## Scope and sources

The Boolean collision and vertical recovery leave different, testable burdens. A horizontal use must supply multiplicity or an operation that separates equal-order primes before those data could replace the signed rows. A vertical use can recover numeric products, but would still have to explain how the recovered information controls the signed tail on whole windows. The sign and magnitude of the row depend on factor multiplicity, not on the order of a cyclic unit alone.

- [PR #2085 proof at its pinned head](https://github.com/mathorn1973/twist-j/blob/edfcb59a13ae8bdeaaeb26d6d6e0a8e68fa4f397/notes/C-J-GROWING-RETURN-WINDOWS-N/PROOF.md)
- [PR #2085 side-note review, equal-order prime witnesses and Fibonacci quotient](https://github.com/mathorn1973/twist-j/blob/edfcb59a13ae8bdeaaeb26d6d6e0a8e68fa4f397/notes/C-J-GROWING-RETURN-WINDOWS-N/SIDE_NOTE_REVIEW.md)
- [Morgan Ward, The prime divisors of Fibonacci numbers](https://msp.org/pjm/1961/11-1/pjm-v11-n1-p31-s.pdf)

Run the finite checks with `python notes/C-RH-ARITHMETIC-KERNEL-N/audit/returns/verify.py`. The hypotheses of the general statements are proved above. The finite checker uses single-architecture exact arithmetic and is not an independent implementation of a closed evidence gate.
