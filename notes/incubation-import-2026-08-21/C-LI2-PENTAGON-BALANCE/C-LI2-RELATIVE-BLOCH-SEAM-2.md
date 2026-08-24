# C-LI2-RELATIVE-BLOCH-SEAM-2

```text
STATUS      candidate-H. NON-CANONICAL. No authority. Promotes nothing.
LANE        incubation, this project. Target line on promotion: PUBLIC.
DATE        2026-08-01
BASIS       Public Canon v30, tag canon-v30, CONTENT_COMMIT
            857223fcd5e7bc8c8e68f1df768d6e8222b24ee0, CANON_SHA256
            2a32dcbd61ee7792fc2cb990b7f223e08876d71bf7ddcf5ec432acd055f3986a,
            157167 bytes, canon/SHA256SUMS 5 of 5 OK.
LAYER       none declared. No reading, no lift.
DEPENDS     C-LI2-PENTAGON-BALANCE-1 (candidate-T), WALL-LI2-RUNG [T],
            WALL-CIRCLE-LEMMA [T]
```

This candidate separates what is PROVED from what is HYPOTHESISED. The proved
part is not the hypothesis and must never be quoted as if it were.

## Part A, proved in-session and exact

### A1, the golden classes are Bloch classes, by computation not citation

With delta([x]) = x wedge (1-x) in Lambda^2 of the multiplicative group:

```text
1 - r = r^2      so   delta([r])   = r wedge r^2 = 2 (r wedge r) = 0
1 - r^2 = r      so   delta([r^2]) = r^2 wedge r = 0
```

Hence [r], [r^2] and beta := [r] - [r^2] lie in B(Q(sqrt5)). Q(sqrt5) is real
quadratic, so r_2 = 0 and B(Q(sqrt5)) is finite: beta is torsion by rank, with
no appeal to literature. And by C-LI2-PENTAGON-BALANCE-1 T4,

```text
5 L(beta) = 5 (L(r) - L(r^2)) = zeta(2)
```

so beta is 5-torsion under the standard zeta(2)Z normalisation of L on the
Bloch group of a real field.

### A2, every wall point is a Bloch class

For z = 1 + zeta_N^a we have 1 - z = -zeta_N^a, a root of unity, hence torsion
in K^*, hence

```text
delta([1 + zeta_N^a]) = 0   in Lambda^2 tensor Q,  for every N >= 3 and every a
```

Verified in Z[zeta_5] for the four Galois images of J: each 1 - sigma_a(J) has
exact multiplicative order 10. This is new relative to the incoming note and it
is the structural reason a seam between the two sides is conceivable at all.

### A3, the explicit Abel relation at the fifth roots

At (x, y) = (-zeta_5, 1 + zeta_5), Abel's five terms are, exactly in Z[zeta_5]:

```text
x              = -zeta_5                         = 1 - sigma_3(J)
y              = 1 + zeta_5                      = sigma_3(J)
(1-x)/(1-xy)   = -zeta_5^2                       = 1 - J
1 - xy         = 1 + zeta_5 + zeta_5^2           = zeta_5^2 / J
(1-y)/(1-xy)   = 1 + zeta_5^2 + zeta_5^3         = -(zeta_5 + zeta_5^4) = -|J|
```

All five verified as exact identities. Independent witness: the Bloch-Wigner
sum over the five arguments is 0 to 3e-16. The relation is genuine. The
submitted note printed this correctly and it survived a direct attempt to break
it.

## Part B, the hypothesis

```text
[candidate-H]  pi^2/30 is the canonical relative Rogers regulator of the
               trivialisation of beta = [phi^-1] - [phi^-2] under the extension
               F = Q(sqrt5) inside K = Q(zeta_5):

               R^rel_(K/F)(beta) =? W(J) - zeta(2) = (1/5) zeta(2)
```

## The governing difficulty, and it is upstream of every technical condition

This is the part the incoming note did not state, and it changes how the
candidate must be worked.

```text
D1  Both legs are rationals, not periods. W_N/zeta(2) is rational for every N
    by WALL-CIRCLE-LEMMA, and L(r)/zeta(2), L(r^2)/zeta(2) are rational by the
    collapse. The target equality lives in the one-dimensional Q-vector space
    zeta(2)Q. A relative regulator theorem must therefore EXPLAIN A RATIONAL.
    It cannot be supported, tested, or even weakly evidenced by numerical
    agreement, at any precision. Any session that reports "agreement to N
    digits" as progress has produced nothing.

D2  The wall operator is provably not the Bloch regulator. The canonical
    regulator on B(Q(zeta_5)) at a complex place is Bloch-Wigner D, which is
    imaginary-part data. The Canon's wall operator is Re Li_2, real-part data,
    explicitly not a field trace (WALL-LI2-RUNG scope). Witnesses:
    D(sigma_a(J)) = +0.9238, -0.7848, +0.7848, -0.9238; the orbit sum vanishes
    trivially by conjugation and carries no information. Re Li_2 and D are
    orthogonal components of the same Li_2 values, and the wall sits on the
    component the Bloch regulator does not see.

    Consequence: a relative-regulator route must either (a) construct an
    operator that is not D and prove it canonical, or (b) prove the wall
    operator factors through a Bloch-theoretic object despite not being D.
    Neither is a technicality.
```

## PASS target

An exact symbolic identity, not a numerical match:

```text
R^rel_(K/F)(beta) = (1/5) zeta(2) = W(J) - zeta(2)
```

in a regulator codomain fixed in advance, with no post-hoc branch correction,
no hand-inserted multiple of pi^2, and Galois-equivariant by construction.

## Falsifiers

```text
G1  the relative class is not canonical
G2  the value depends on the choice of flattening
G3  the equality requires a hand-inserted multiple of pi^2
G4  the Galois action changes the result
G5  the principal-real-part wall operator cannot be derived from any relative
    regulator, i.e. D2(a) and D2(b) both fail
G6  only a numerical coincidence is produced, with no symbolic identity
G7  a second, inequivalent relative regulator gives a different rational
```

Any of G1 to G7 kills the hypothesis. None of them touches
C-LI2-PENTAGON-BALANCE-1: the exact balance theorem stands whatever happens
here, because it does not depend on this reading.

## Explicit non-claims

```text
1  Part A does not support Part B. A1, A2, A3 are exact facts about Bloch
   classes; they establish that a common home exists, not that a map does.
2  No physical reading. No layer. No anchor. No decoder consequence.
3  The 5-torsion of beta and the order-5 cyclotomy are not shown to be the same
   5 by anything here. They are both 5 and that is all that is proved.
```

## Prior work in this project

```text
claude/RECON-TWIST6D-LEGACY-DECODER_2026-07-31.md  section 5.2 proposed
  C-LI2-MODULUS-POINTS-1 for the Landen partition. That proposal is strictly
  contained in C-LI2-PENTAGON-BALANCE-1 and should be retired into it rather
  than opened separately.
claude/NADHLED-DEKODER-A-METROLOGIE_2026-07-25.md  H-CHANNEL-SEPARATION and
  H-ANCHOR-FORCED. See the audit note part 7 for what this lane does and does
  not do to them. Short answer: it supplies a named bridge and no anchor.
```
