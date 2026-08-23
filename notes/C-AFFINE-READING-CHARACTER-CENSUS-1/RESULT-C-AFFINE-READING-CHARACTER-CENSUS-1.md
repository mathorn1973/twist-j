# C-AFFINE-READING-CHARACTER-CENSUS-1 result

Status: **candidate-T at L1. CANDIDATE. NO AUTHORITY. NOT CANON.**
Decision: `READING-CENSUS-CERTIFIED`.

## Pins

```text
PREREG sha256    473f64da93c9b6c488ffe266bb33c1b9c54705c8debc85166757b80aa192ba40
PREREG bytes     11599
PREREG lines     264
verifier sha256  829f91d1269f4802c2dfb0e0afba1b9bd78e0830bb665547719f5371bc2ff430
verifier bytes   13274
stdout file      EXPECTED.txt
stdout sha256    4a3813fa115f875d6f8da44c6d26c8a3c161cef9a273221b7f66539e6fab35f5
stdout bytes     1101
exit code        0
stderr bytes     0
elapsed          1473 ms, engineering readout
environment      LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform         Ubuntu 24.04, x86_64, Python 3.12.3
```

One architecture only. This is a candidate, not a public probe. The two
architecture byte identity gate has not been run and is required before any
public promotion.

## What passed

All of G1 through G8 pass exactly. G9 is recorded as `SEPARATING-AT-5` with
zero collisions.

**The central negative.** `m_lambda(1) = 0` for every one of the four linear
characters of `G = AGL_1(F_5)`, by both frozen methods and by a third
independent route in the break attempt. There is no nonzero linear reading of
the carrier, invariant or phase weighted. The public row
`AFFINE-READING-DEGREE-CENSUS` established this in the invariant sector alone;
it now holds in every sector, so a covariant reading is closed off as well as
an invariant one.

**The graded census.** Multiplicities in `Sym^d V` of the five complex
irreducibles `(1, epsilon, lambda_1, lambda_3, V)`:

```text
d   dim   1   eps   i   ibar   V
0     1   1     0   0      0   0
1     4   0     0   0      0   1
2    10   1     1   0      0   2
3    20   1     1   1      1   4
4    35   3     2   1      1   7
5    56   3     3   3      3  11
```

Molien coefficients through degree 12, invariant sector:
`1 0 1 1 3 3 5 6 10 11 16 18 25`. Epsilon sector:
`0 0 1 1 2 3 5 6 9 11 16 18 24`. Each order four sector:
`0 0 0 1 1 3 3 6 7 11 13 18 21`.

**The overclaim is dead.** The smallest odd invariant degree is 3, not
infinity. A cubic invariant exists, it is odd, and it therefore reads the sign
of the state. The informal claim that only even or contractive quantities are
readable is false at L1. The break attempt exhibits the cubic explicitly, in
primitive integer form with 20 monomials and coefficient set `{-4, 3}`, and
proves the closed form as an exact polynomial identity, not pointwise:

```text
3 K = p_1^3 + 6 p_1 q_+ - 25 p_3,
p_1 = sum of coordinates, p_3 = sum of cubes, q_+ the frozen invariant form.
```

**The counterweight holds.** G9 records `SEPARATING-AT-5`: on the exhaustive
test set `{-2,...,2}^4` minus zero, 624 vectors, the invariant fingerprint of
degree at most 5 separates `G` orbits with zero collisions. So the carrier
state is recoverable from readings up to the 20 element orbit. What is
unreadable is not the state. What is unreadable is the state **linearly**.

## Break attempt, and what it found

Independent third code path, deliberately different algorithms.

1. The linear semi-invariance system solved directly as a nullspace over `Q(i)`,
   never through a projector rank: dimension 0 for all four characters. G3
   survives.
2. `dim End_G(V) = 1` from the commutant nullspace, no character arithmetic.
3. A third multiplicity route by conjugacy classes and Newton power sums,
   touching neither `1/det(I - t rho)` nor any `Sym^d` matrix: agrees with the
   frozen Molien values at all 52 cells.
4. `Sym^3 V` is exactly the regular representation of `G`: multiplicities
   `(1,1,1,1,4)` and dimension 20 equal to the group order.
5. Minimal separating degree, sharpened below the frozen gate: degree at most 2
   leaves 474 non orbit collisions, degree at most 3 leaves 264, degree at most
   4 leaves 8, degree at most 5 leaves 0. Separation first completes at degree
   five on this test set.

## Fired self-check, recorded and not repaired

The break attempt found a real defect in the frozen verifier. Basis extraction
uses `rref_pivots(tp(A))` where it must use `rref_pivots(A)`. Pivots of the
transpose index independent rows, not a basis of the column space, so the
selected columns can include the zero polynomial.

Exact impact, measured:

```text
degree 2   frozen selection rank 1 of 1     no loss
degree 3   frozen selection rank 0 of 1     the cubic was missing entirely
degree 4   frozen selection rank 3 of 3     no loss
degree 5   frozen selection rank 1 of 3     two invariants missing
```

The frozen G9 fingerprint therefore used 6 genuine invariants where 9 were
intended.

Soundness impact: none. G1 through G8 never touch the extracted basis. Every
column of a projector lies in its image, so every extracted polynomial is a
genuine invariant, and the frozen family is a subset of the intended one. A
weaker family separating with zero collisions implies the full family
separates, so `SEPARATING-AT-5` stands a fortiori and is in fact stronger than
reported: six invariants already suffice. `SIGN PAIR SEPARATED BY INVARIANTS
YES` likewise stands, since every degree five homogeneous form is odd.

Power impact: real. Any statement about **which** degree first separates is not
supported by the frozen run and is supported only by the corrected break path.
The frozen run cannot be read as evidence that degree 5 is minimal.

The frozen verifier is not amended and the recorded decision is not moved. The
fix is carried into the promotion proposal as a precondition of public pinning.

## Scope firewall

L1 only. No measurement, apparatus, instrument, observer, decoder, Born rule,
probability, record, photon, light, matter, energy density, cosmology,
expansion, contraction, hidden fraction, SI value, or L2 to L6 lift is assumed
or concluded. This candidate does not establish that any physical apparatus is
unable to record a linear datum. That passage is named in the preregistration
as `O-LINEAR-READING-APPARATUS-LIFT` and is not crossed.
