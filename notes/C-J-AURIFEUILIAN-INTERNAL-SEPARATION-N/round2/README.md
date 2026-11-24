# Four units are complete to test, and insufficient at index 125

**NON-CANONICAL. NO AUTHORITY. L1 arithmetic.** Paper deductions are
candidate-D. The exact finite menu and the resulting index-125 obstruction
are candidate-C, supported by the paper completeness theorem. No Canon,
physical or RH status changes.

Continuation of claim #2090 and draft PR #2092 by A. M. Thorn,
ChatGPT-Astra-20261124-Internal-Separation-R2. The predecessor is pinned at
`0b81796c01d4bee47eceb6e451670ea0d233610b`. PUBLIC basis remains main
`6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`, verified Public Canon v117.

## 1. A finite menu covers every four-unit separator [candidate-D]

For m=5^k, k>=1, put h=5m and M=A_minus(m) A_plus(m). The complete menu

    L_a + epsilon L_b,
    a even, b odd, 0 <= a,b < 2h, epsilon in {-1,+1},

has exactly 2h^2 labelled entries. Every gcd obtainable from a sum of at
most four signed real units is the gcd of at most two entries of this menu.
For signed quartic units, with arbitrary fifth-root phases, at most four
menu entries suffice. This equality holds against every divisor of M and
preserves all prime-power multiplicities. No factorization chooses the
entries. Consequently the finite menu detects every prime-pair separation
available to four units, even with unrestricted exponents.

The key case has three units of one quadratic norm and one of the opposite
norm. It reduces to two relations with two units of each norm through
exact conjugation identities. A same-norm label-difference is a unit
modulo M, which is essential in the split algebra. The full proof also
handles the shifted Fibonacci branch and fifth-root phase projection.

An optional reflection reduces the menu to (h^2-1)/2 labelled entries,
with exactly the same information. The finite audit below retained its
original full menu; no post-exposure domain reduction was made.

[Complete proof](FOUR_UNIT_COMPLETENESS.md).

## 2. Both next-index sides resist every four-unit test [candidate-C]

The new prospective audit used m=125, h=625, both signs, and the full
781250-entry menu on each side. The recurrence and matrix programs were
separately authored and frozen before source comparison. All sources were
publicly committed and read back before execution.

| Side | gcd 1 | Proper gcd | gcd equal to the input | Total |
| --- | ---: | ---: | ---: | ---: |
| A_minus(125) | 781246 | 0 | 4 | 781250 |
| A_plus(125) | 781246 | 0 | 4 | 781250 |

Both programs produced byte-identical 1032-byte JSON output. Their exact
finite agreement is one aarch64 execution lane, not a two-architecture
scientific gate. Repository CI does not execute these notes-only programs.

By the completeness theorem, every sum S of at most four signed quartic
units satisfies, for either side at this index,

    gcd(A_sigma(125), content(S)) in {1, A_sigma(125)}.

This excludes every internal four-unit split, with arbitrary integer
exponents and arbitrary fifth-root phases. It is stronger than failure
of one formula or one selected subfamily.

[Frozen specification](PREREG.md), [source pin](https://github.com/mathorn1973/twist-j/commit/7b50c67e16e712d5653d9f594d506eacff2d0ba7),
[verifier](verify.py), [separate matrix program](break.py),
[exact output](EXPECTED.txt), [second output](BREAK_EXPECTED.txt),
[execution record](RUN.md).

## 3. The obstruction has actual distinct prime divisors

The following exposed numerical factors were retrieved from the primary
*Fibonacci and Lucas Factorizations* table after the complete menu had
finished. A separate publicly pinned certificate checks both products and
both coprimalities exactly. They were not inputs to the menu or its choice.

    A_minus(125)
      = 17656721319717734662791328548550157116069628154452501
      = 2775001 * 6362780164662187387605023763432934660589177501.

    A_plus(125)
      = 17656721319717734662791329142801304691196060283203751
      = 13181501253515178490001 * 1339507616024322442312867213751.

In each row the two factors exceed one and are coprime. The exact Bezout
coefficients are in [NONVACUITY_EXPECTED.txt](NONVACUITY_EXPECTED.txt).
These product and Bezout identities are finite integer certificates;
no primality assertion from the source table is needed. Each side
therefore contains at least two distinct prime divisors.

Together with Section 2, this supplies concrete same-side prime pairs
whose least separating unit weight is at least five. It does not show
that five is attained. The earlier index-25 pair still has exact minimum
four; there is no conflict between these different indices.

Source: [expanded table, L(625)](https://mersennus.net/fibonacci/l1000.txt),
[compact L625A/B](https://mersennus.net/fibonacci/lucas.txt),
[format](https://mersennus.net/fibonacci/format.html), consulted 2026-11-24.
The tables cite Brillhart, Montgomery and Silverman (1988) and credit
Blair Kelly and other contributors. Only the numerical facts are used.
[Separate exposed certificate specification](NONVACUITY_PREREG.md) and
[certificate checker](check_nonvacuity.py).

## 4. Unrestricted exponents still bound the whole proper gcd [candidate-D]

For w>=2 define the factor-independent integer threshold

    U_w(m) = min over Q>=1 with Q^(w-1)<=m of
             w^(4 Q^(w-1)) L_(4(ceil(m/Q)-1)).

Every sum of at most w signed units, including arbitrary phases and
arbitrarily large exponents, has

    g = gcd(A_sigma(m), content(S)) = A_sigma(m), or g <= U_w(m).

The bound includes the full proper divisor with all valuations. It holds
for any number of tests, including adaptive choices. It follows by
simultaneously compressing the exponent residues with the pigeonhole
principle and applying the predecessor's full-divisor denominator theorem.

For fixed w, log U_w(m)=O_w(m^(1-1/w)), whereas
log A_sigma(m)=2m log(phi)+o(1). Thus every fixed positive rational power
of A eventually exceeds every proper output at that fixed weight.
For a concrete delta=a/b the exact check is U_w(m)^b < A^a.

All prime bases above U_w(m) have identical flags under every such menu.
If an extraction is required to have size at least A^delta, its weight
must grow at least k/r-O(log log(k+2)) whenever 5^r>2/delta and m=5^k.
These are resource implications; no infinite family of balanced composite
sides is proved. A related parallel arity result retains its own scope and
ownership; no priority claim is made.

[Full proof and exact integer bound](GROWING_WEIGHT.md).

## Review and remaining question

Construction, root review and a separate same-session opponent read the
actual paper files. [Opposition](OPPOSITION.md) records the split-ring,
parity, prime-power and quantitative checks. This is internal paper review,
not external peer review. Code authorship was separate until both sources
were frozen; that is distinct from the paper-review claim.

The next specific open question is whether five units separate prime
divisors inside either index-125 side, under a new prescribed family.
The broader question of one universal constant weight remains open.
Four is now excluded by actual members of this same tower; neither an
unbounded minimum weight nor an efficient general factoring method follows.

The original index-25 frozen source and output files are unchanged. All
new scientific material is in this round-two directory. The existing
candidate and draft PR remain the single owner lane.
