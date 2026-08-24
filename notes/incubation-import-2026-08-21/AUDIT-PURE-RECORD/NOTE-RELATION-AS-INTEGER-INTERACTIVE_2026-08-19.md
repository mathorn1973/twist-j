# NOTE-RELATION-AS-INTEGER-INTERACTIVE (2026-08-19)

NON-CANONICAL. Third and shortest page of the entanglement exposition set, after
`claude/NOTE-RELATIONAL-AREA-INTERACTIVE_2026-08-19.md` and
`claude/NOTE-BELL-TICKET-INTERACTIVE_2026-08-19.md`. Standard quantum mechanics
only, not TWIST-specific. No claim, no verifier, no registry effect.

## The owner's brief

Show the relation as an integer object. Continuity is not needed; it appears
only when the integers are read through geometry. Cut the length hard enough
that a child gets the magic. Land the line: the key is in the relation, not in
what each one carries alone. Follow-up brief the same day: show plainly *in what
way it differs* from prepared answers, and how it carries the stronger
correlation.

## How the page answers it

Two arrows on a lattice, both ending exactly on lattice points, so the state is
four whole numbers. The parallelogram area is obtained by **counting dots**, via
Pick: interior plus half the boundary minus one. The same number falls out of
the cross product `ad - bc`. Two roads, one integer.

Everything downstream stays exact:

```text
plocha A = |ad - bc|                          whole number
Q        = a^2 + b^2 + c^2 + d^2              whole number
vztah C  = 2A / Q                             fraction
C^2      = 4A^2 / Q^2                         fraction
1 - C^2  = (Q^2 - 4A^2) / Q^2                 fraction
sum      = 1                                  exactly
S_max^2  = 4 + 16 A^2 / Q^2                   fraction
```

The square root enters exactly once, at the very end, and only because someone
wanted a *length*. For the unit square `A = 1, Q = 2` the last line is the
integer `8`, so the famous `2 sqrt2` is nothing but the square root of eight.
The page states it as: the eight is the thing, the root is a way of reading.

## The Euclid link, which is the part that lands

For the plain rectangle `u = (m,0)`, `v = (0,n)`:

```text
Q = m^2 + n^2,   A = mn,   C = 2mn/(m^2+n^2),   |b| = |m^2-n^2|/(m^2+n^2)
```

so the triple (kept, relation, whole) is exactly `(m^2-n^2, 2mn, m^2+n^2)`, the
Euclid parametrization of Pythagorean triples. `m,n = 3,4` gives `7, 24, 25`.
The right triangle from the earlier page is therefore not an analogy for a
Pythagorean triple; on integer states it **is** one. The page computes and
reduces the triple live, and says plainly when the kept part is not rational
(when `Q^2 - 4A^2` is not a perfect square) while the relation still is. That
asymmetry is itself the lesson: the relation is always a fraction, the private
part is not.

## The comparison section, added on the follow-up brief

The whole difference between a prepared answer sheet and the relation is a
single term, and that term is the area:

```text
any ticket    S^2 = 4                exactly, all sixteen, no exception
the relation  S^2 = 4 (1 + C^2)      = 4 + 16 A^2 / Q^2
difference    S^2 - 4 = 16 A^2 / Q^2
in integers   (S^2 - 4) * Q^2 = 16 A^2
```

So the excess over what any ticket can do is the area, squared, times sixteen.
Zero area, zero excess, and the state is indistinguishable from a ticket.
Nonzero area, strictly more, and by exactly that much.

Two facts worth keeping because they are integers, not limits:

- The entire playing field runs from `4` to `8`. Both ends are whole numbers.
  The classical bound squared is `4`; the maximum nature allows, squared, is `8`.
- At `A = 1, Q = 2` the relation gives exactly twice the ticket value, `8`
  against `4`. In `S` itself that is a factor `sqrt2`; the page says both, in
  those words, so the doubling is not mistaken for a doubling of `S`.

The panel renders this as two bars on a `0..8` axis: a grey bar to `4` labelled
"any ticket", and below it the same grey `4` plus a blue segment labelled
"přídavek", with the identity `(S^2 - 4) * Q^2 = 16 * A^2` printed live beneath.
The parallel preset drives the blue segment to zero on screen.

## Two real defects found and fixed by testing

1. The first build drew the lattice over `+-5` while the parallelogram's far
   corner reaches `u + v`, up to `+-10`. Configurations existed where boundary
   points fell outside the drawn and scanned range, so the dot count was short
   and Pick's arithmetic visibly failed on screen. On a page whose entire claim
   is that the counting works, that is fatal rather than cosmetic. Fixed by
   construction: handles clamp to `+-4`, the lattice is drawn and scanned over
   `+-8`, so the polygon is always fully contained.
2. The in-bar label was given its colour as an SVG presentation attribute while
   a CSS class also set `fill`. The class wins, so the label rendered in the
   muted ink on a saturated bar instead of the surface colour. Fixed by moving
   it to an inline style and verified through `getComputedStyle`, which now
   returns the surface colour. This is the third instance of the same trap in
   this set of pages: presentation attributes lose to class rules.

## Checks run

Exhaustive over the whole reachable domain, executed inside the rendered page:
every ordered pair `(u, v)` with both in `[-4,4]^2`, excluding the degenerate
`det = 0` cases, was counted by brute force over the drawn lattice and compared
against both `2(gcd(u) + gcd(v))` for the boundary and `I + B/2 - 1 = |det|` for
Pick.

```text
neshod: 0
```

Preset readback through the UI, after the comparison section was added:

```text
1 a 1        plocha  1   vztah 1      S^2 = 8          16 * 1   = 16     0, 1, 1
2 a 1        plocha  2   vztah 4/5    S^2 = 164/25     16 * 4   = 64     3, 4, 5
3 a 4        plocha 12   vztah 24/25  S^2 = 4804/625   16 * 144 = 2304   7, 24, 25
šikmé        plocha  8   vztah 4/5    S^2 = 164/25     16 * 64  = 1024   3, 4, 5
rovnoběžné   plocha  0   vztah 0      S^2 = 4          16 * 0   = 0      1, 0, 1
```

Every `S^2` was checked against `(4Q^2 + 16A^2)/Q^2` as an exact rational, and
every excess numerator against `16 A^2`. Rendered light and dark at 900 and
390 px. No page errors.

## Relation to the internal line

Stated here only to prevent a later session mistaking one for the other. The
integer invariants on this page are the same `Q`, `Delta = A^2` and
`C = 2|det X|/Q` that appear in the DQRC block of Public Canon v54 section 11,
and the identity `S_inf^2 = 4 + 16 Delta / Q^2` is the same rational statement
carried by `DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY [T]`. The page nonetheless makes
no TWIST-J claim, cites no row, and must not be read as public evidence for one.
It is an exposition of standard quantum mechanics that happens to use the same
integer coordinates.
