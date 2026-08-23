# C-AFFINE-READING-CHARACTER-CENSUS-1. The character graded reading census of the affine carrier

```text
CANDIDATE ID:   C-AFFINE-READING-CHARACTER-CENSUS-1
DATE:           2026-08-23
STATUS:         candidate-T at L1. NON-CANONICAL. No authority.
TARGET ROW:     AFFINE-READING-CHARACTER-CENSUS   (proposed T, L1)
TARGET LINE:    PUBLIC, mathorn1973/twist-j main
BASIS:          Public Canon v60, tag canon-v60,
                content commit 18b21bdaf2c2236c9444b120900277ccfb63e050,
                head at freeze f9b7438747e612eeebf63cb3ac95283fcb2a7085
DECISION:       READING-CENSUS-CERTIFIED
```

## The question

`AFFINE-READING-DEGREE-CENSUS` establishes `(V*)^G = 0`: the carrier has no
nonzero **invariant** linear reading. That leaves a gap. A reading that is not
invariant but merely covariant with a phase weight, `f(rho(g) x) =
lambda(g) f(x)`, would still be a reading, and the existing row says nothing
about it. `G = AGL_1(F_5)` has four linear characters, and only one of them had
been examined.

The question is therefore whether the linear void is a feature of the trivial
sector or of the carrier. This candidate answers it, and then attacks the
informal conclusion that people draw from it.

## What is claimed

**1. The linear void is complete.** `m_lambda(1) = 0` for every one of the four
linear characters, by two frozen independent methods and by a third independent
route in the break attempt. No nonzero linear reading of the carrier exists,
invariant or phase weighted.

**2. The quadratic degree carries exactly two lines.** The invariant `q_+` and
the epsilon graded `q_-`, and nothing in either order four sector.

**3. Sym^3 V is the regular representation of G.** Multiplicities
`(1, epsilon, lambda_1, lambda_3, V) = (1,1,1,1,4)` and dimension `20 = |G|`.

**4. The invariant ring is not concentrated in even degrees.** The smallest odd
invariant degree is three. The unique cubic invariant `K` is exhibited in
primitive integer form, 20 monomials with coefficient set `{-4, 3}`, and
satisfies the exact polynomial identity

```text
3 K = p_1^3 + 6 p_1 q_+ - 25 p_3,
```

with `p_1` the coordinate sum and `p_3` the sum of cubes. `K` is odd, so it
reads the sign of the state.

**5. Readings recover the state up to the orbit.** No element of `G` acts as
`-I`, `chi_V` takes values in `{-1, 0, 4}`, and on the exhaustive test set
`{-2..2}^4` minus zero the invariant fingerprint of degree at most five
separates `G` orbits with zero collisions.

## What is refuted

The informal reading that only even or contractive quantities are observable is
**false at L1**. Point 4 kills it. The state is not unreadable; it is
unreadable **linearly**. Both halves are part of the result and neither may be
quoted without the other.

## Graded census

```text
d   dim   1   eps   i   ibar   V
0     1   1     0   0      0   0
1     4   0     0   0      0   1
2    10   1     1   0      0   2
3    20   1     1   1      1   4
4    35   3     2   1      1   7
5    56   3     3   3      3  11
```

Molien coefficients through degree 12.

```text
invariant sector    1 0 1 1 3 3 5 6 10 11 16 18 25
epsilon sector      0 0 1 1 2 3 5 6  9 11 16 18 24
each order four     0 0 0 1 1 3 3 6  7 11 13 18 21
```

## Layer

**L1 only.** No measurement, apparatus, instrument, observer, decoder, Born
rule, probability, record, photon, light, matter, energy density, cosmology,
expansion, contraction, hidden fraction, SI value, or L2 to L6 lift is assumed
or concluded. The passage to any apparatus statement is named in the
preregistration as `O-LINEAR-READING-APPARATUS-LIFT` and is not crossed, since
an unnamed layer lift is a stop condition.

## Dependencies

```text
requires   AFFINE-READING-DEGREE-CENSUS      (T)
requires   AFFINE-QUADRATIC-FORM-UNIQUENESS  (T)
relates    P-J-ODD-MOTOR-MEDIATED-BRIDGE-2   (merged probe, no canon row)
```

The proposed row extends these and must not restate them.

## Known defect, recorded and not repaired

The frozen verifier extracts an invariant basis with `rref_pivots(tp(A))` where
it must use `rref_pivots(A)`. At degree three the extracted representative was
the zero polynomial and at degree five only one of three was independent. G1
through G8 never touch the extracted basis, so the decision stands; the
`SEPARATING-AT-5` label stands a fortiori because a weaker family already
separated. No minimality claim about the separating degree may be carried from
the frozen run. The fix is a precondition of public pinning, stated in
`PROMO-C-AFFINE-READING-CHARACTER-CENSUS-1.md`.

## Status

candidate-T at L1, one architecture. Not computation grade. Nothing here is a
public probe pin and nothing here promotes anything. The public probe is a new
preregistration under a public issue on branch
`probe/P-AFFINE-READING-CHARACTER-CENSUS-1`, pinned before first execution.
