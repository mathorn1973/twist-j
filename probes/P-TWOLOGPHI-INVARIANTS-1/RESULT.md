# P-TWOLOGPHI-INVARIANTS-1 result

Status: `DECIDED AND AUDITED / CANON UNCHANGED / PIN NOT PUSHED`

## Disposition

```text
Mahler:     M(J) = phi^2 exactly, so log M(J) = 2 log phi. The minimal
            polynomial x^4 - 3x^3 + 4x^2 - 2x + 1 = Phi_5(x - 1) is
            irreducible over Q, J . Jbar = 2 - phi = phi^-2 is totally
            real with characteristic polynomial (x^2 - 3x + 1)^2, and
            exactly two conjugates lie outside the unit circle, both of
            modulus phi. phi^2 carries trace 3 = Tr(J) and norm
            1 = N(J).
regulator:  Reg(Q(zeta_5)) = 2 log phi. Unit rank 1 from r_1 = 0,
            r_2 = 2; phi a unit of Z[zeta_5]; phi the fundamental unit
            of Z[phi] by exhaustive enumeration over derived bounds;
            local degree 2 at the complex place. One labeled import,
            the prime-cyclotomic unit index Q = 1 with h^+ = 1. The
            analytic class number formula is not used, so the class
            number result below is independent rather than an input.
class no.:  h(Q(zeta_5)) = 1 by the Minkowski bound (15 sqrt5)/(2 pi^2)
            < 2, established as the exact rational statement
            1125 < 16 pi^4 with a checked alternating-series enclosure
            of pi; h(Q(sqrt5)) = 1 by sqrt5/2 < 2, equivalent to
            5 < 16, with no transcendental input at all.
periodic:   the Lucas closed forms L_n^2 and (L_n - 2)^2 on the two
            residue classes of n divisible by 5; exactly one perfect
            square among the 32 off-residue values on 1..40, at n = 1;
            and the two-sided bracket, proved for every n >= 1 and
            audited on 1..40. Status C: the census is finite-range.
integrity:  no STOP. One formal execution, exit zero, empty stderr,
            29/29 gates PASS, stdout equal to EXPECTED.txt. Byte
            identical on CPython 3.10, 3.11, 3.12 and 3.13.
```

## Independent attempt to break it

A breaker written after the pin, sharing no routine with `verify.py`
(five-coordinate ring model, Sylvester resultants, factorization modulo
primes, a second arctan decomposition), ran seven attacks. Final state:
`BREAKER 0 kills in 7 attacks`.

```text
K1 Kronecker      no k <= 500 with J^k = 1, and the minimal polynomial
                  divides no x^m - 1 for m <= 120, so not every conjugate
                  can lie on the unit circle and M(J) cannot be 1
K2 factorization  irreducible modulo 2, 3, 7 and 13, which implies
                  irreducibility over Q by a route the verifier does not
                  use. It is reducible modulo 11, exactly as the splitting
                  of 11 = 1 mod 5 requires, so the test is discriminating
                  and not a tautology
K3 units          no unit of Z[phi] in the open interval (1, phi) over the
                  box |a|, |b| <= 400, one hundred times the derived bound
K4 resultant      all forty values reproduced by Sylvester determinants of
                  size up to 44, including 1860496 at n = 15
K5 range          closed forms, bracket and census pushed to n = 200, four
                  times the declared range: closed forms hold, the bracket
                  holds with a strictly positive lower bound at every n,
                  and the only off-residue square is still n = 1. This is
                  outside the preregistered scope and promotes nothing
K6 Minkowski      a second, unrelated decomposition
                  pi = 4 (arctan(1/2) + arctan(1/3)) gives an overlapping
                  enclosure and the same verdict 16 pi^4 > 1125
K7 scope          the four proposed row texts carry no forbidden public
                  token and assert no rate, entropy or physical claim
```

## Integrity record: one false firing, kept

`K7` in its first revision reported `KILL`. The kill was false and the
firing is recorded rather than deleted.

```text
what it did     scanned the whole scope field of each proposed row for the
                words naming an overreach, including "physical"
what happened   it matched the row's own disclaimer, "no dynamical,
                entropic or physical reading is created", and reported the
                denial of a claim as the claim
diagnosis       the same defect class the incubation lane already froze a
                lesson about: a flat text scan matches the text that denies
                the thing. There the gate matched its own probe list; here
                it matched the row's own fence
fix             the gate now works clause by clause and an overreach word
                inside a negated clause is not an assertion. The rewritten
                gate passes and the comment recording the firing is in the
                breaker source
```

Nothing in the pinned verifier changed. `verify.py` was not touched after
the pin and the breaker is not evidence for any claim.

## Proposed registry consequence (a later sealed fold, not this probe)

Four rows, exact texts frozen in `FOLD-ROWS.tsv` beside this file:

```text
J-MAHLER-MEASURE             T  canon section 1
REGULATOR-TWO-LOG-PHI        T  canon section 4
CYCLOTOMIC-CLASS-NUMBER-ONE  T  canon section 4
J-TORAL-PERIODIC-POINTS      C  canon section 2
```

Ledger delta: claims +4, T +3, C +1. Frontier unchanged; all four are
closed statuses. No live row moves and no gate is created.

The fold must read `STATUS.md` and choose the branch for the fourth row.
Public Canon v56 is prepared and carries `J-TORAL-ENTROPY [T]`, which
already registers the fixed-point identity and the n = 15 witness; under
that head the fourth row carries only the closed forms, the census and the
bracket and requires that row. Branch B, for a head without v56, is in
`FOLD-ROWS-BRANCH-B.tsv`. The mathematics is identical either way.

## Evidence boundary

```text
This probe proves arithmetic. It proves no dynamical, entropic, measure or
physical statement, and the fact that four independent invariants carry the
constant 2 log phi is a fact about the number phi, not a bridge between
layers. ENTROPY-LAYER-BRIDGE [O] is untouched and stays open at its exact
scope; the three BOUNDED_BY edges proposed in PREREG.md make that fence a
ledger fact rather than prose.

Three imports are named and not reproved: the prime-cyclotomic unit index
Q = 1 with h^+ = 1, the Minkowski bound, and the maximality of Z[zeta_5].
No result here strengthens any of them.

RH, the Li ladder and every carrier row are untouched. The row
SPLIT-PRIME-RAPIDITY-CLASS [T] already consumes class number one for
Q(sqrt5); this probe supplies an exact proof of that fact but changes no
existing row, adds no edge to one, and leaves that observation to a later
fold.
```
