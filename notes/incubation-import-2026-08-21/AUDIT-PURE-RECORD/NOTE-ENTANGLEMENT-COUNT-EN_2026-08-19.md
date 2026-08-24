# NOTE-ENTANGLEMENT-COUNT-EN (2026-08-19)

NON-CANONICAL. English sibling of
`claude/NOTE-RELATION-AS-INTEGER-INTERACTIVE_2026-08-19.md`. Standard quantum
mechanics only, not TWIST-specific. No claim, no verifier, no registry effect.

## What changed against the Czech page

`entanglement-you-can-count.html` is the same interactive with the same
arithmetic, retargeted at a reader who does not know quantum mechanics. The
Czech page assumed the reader already had the earlier two pages in mind; this
one assumes nothing, so sections were added at the front, in the middle and at
the back.

**"What this is about"** states the experiment in three short paragraphs with no
formalism: two particles made together and carried apart, each asked a question,
each answering yes or no, the columns compared. The agreement is higher than any
advance arrangement permits, that phrase has one specific number attached, and
the page's job is to compute it with whole numbers.

**"What you are looking at"** explains the two arrows before the reader meets
them, which the Czech page never did explicitly: the first is what A looks like
when B is in state 0, the second when B is in state 1; parallel means B tells
you nothing; the measure of the difference is the area, because both turning and
shortening change it. Pick's rule is stated before the figure rather than after.

The footer carries the two honest limits in plain language: mixed states blur
the picture and are outside scope, and the argument bounds what a written answer
sheet cannot do rather than asserting that anything travels between the
particles.

## The proof section, added on the owner's demand

The sentence "the experiment's score comes out as 2 or −2, so 4 when squared"
was an unbacked assertion. The owner required it proved and explained. It now
has its own section, elementary and physics-free, in three steps.

**The score.** Four pairings, three demanding agreement and the fourth
disagreement; each scores `+1` if it comes out as demanded and `−1` otherwise;
the total is the score.

**The demands contradict each other.** The first two force `B1 = B2`. The third
gives `A2 = B1`, hence `A2 = B2`, which the fourth forbids. No sheet meets all
four, so at least one always fails.

**The number that fail is always odd.** With `t = (a1 b1, a1 b2, a2 b1, -a2 b2)`
each of the four answers appears in exactly two terms, so every answer is
squared and the signs would cancel to `+1`; the minus on the fourth term makes
the product `-1`. A product of four signs is negative only when an odd number of
them are negative.

Odd means one or three, so the score is `3 - 1 = 2` or `1 - 3 = -2`. Never zero,
never one, never four. Squared, always `4`.

The section ends with the exhaustive sixteen printed as a grid, each cell showing
its four signs and its score, with the reader's current sheet highlighted and
four toggles to rewrite it. Then the convexity remark: any mixture is an average
of those sixteen numbers, and an average never leaves the range of what it
averages.

The Czech page does not need this section, because the Czech set already devotes
a whole page, `listek-v-kapse.html`, to exactly this argument. The English page
stood alone and therefore could not assert it unsupported.

## A defect introduced and caught in this build

The English version first added in-picture labels reading "A when B = 0" and "A
when B = 1" at the arrow tips. They overlapped the parallelogram and the
coordinate labels and were partly unreadable at the default state. Replaced with
an HTML legend under the figure that shows both coordinate pairs and their
meanings and updates live.

## Checks run

Pick sweep re-run inside this page after the rewrite, over every ordered pair of
arrows in `[-4,4]^2` with `det != 0`, comparing the brute-force dot count against
`2(gcd(u)+gcd(v))` and `I + B/2 - 1 = |det|`.

```text
mismatches: 0
```

Preset readback, `S^2` against `(4Q^2 + 16A^2)/Q^2` as an exact rational and the
excess numerator against `16 A^2`:

```text
1 and 1    area  1   rel 1      S^2 = 8          16 * 1   = 16     0, 1, 1
2 and 1    area  2   rel 4/5    S^2 = 164/25     16 * 4   = 64     3, 4, 5
3 and 4    area 12   rel 24/25  S^2 = 4804/625   16 * 144 = 2304   7, 24, 25
skew       area  8   rel 4/5    S^2 = 164/25     16 * 64  = 1024   3, 4, 5
parallel   area  0   rel 0      S^2 = 4          16 * 0   = 0      1, 0, 1
```

The proof section, verified four ways rather than by reading the source:

```text
16 cells rendered, distinct scores  {+2, -2}
every rendered cell re-derived independently from its own signs   0 mismatches
all 16 states driven by clicking the toggles                      only (+2, 4) and (-2, 4)
exactly one cell highlighted, matching the live toggle state       yes
"an odd number of demands fails" checked over all 16 sheets        holds
```

The in-bar label's computed fill resolves to the surface colour on states with an
excess and is absent on the parallel state. Rendered light and dark at 900 and
390 px. English curly quotes throughout; no em dashes. No page errors.

## Set status

Four exposition pages now exist for this subject, none canonical, none citing a
registry row:

```text
vztah-ma-tvar.html               CZ   the relation as an area nobody owns
listek-v-kapse.html              CZ   why prepared answers cannot substitute
vztah-na-prstech.html            CZ   the relation as a whole number
entanglement-you-can-count.html  EN   the same, self-contained, no physics assumed
```

The English page is now the only one that carries the whole argument end to end
without a sibling. Open owner decision, unchanged: whether any of these land on
the hub, under `notes/` in the public repo, or nowhere. English siblings of the
first two Czech pages have not been written and were not requested.
