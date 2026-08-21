# NOTE-ENTANGLED-EN (2026-08-19)

NON-CANONICAL public-facing exposition. Standard quantum mechanics, with one
fenced interpretive step. No claim, no verifier, no registry effect. File is
`entangled.html`.

## The argument, in order

**The note fails.** Four demands, three asking agreement and one asking
disagreement, contradict each other, and the number that fail is always odd, so
every one of the sixteen possible notes scores `+-2` and `4` squared. Mixing
cannot help, because an average never leaves the range of what it averages.

**The cheat sheet was real.** Bell rules out two notes and says nothing about
one. The owner's framing, with the sharpening that came out of the discussion: a
note is a *record*, a list of answers to questions written out in advance, while
the relation is a *rule* about how two answers move together, holding for every
question that could be asked. A record has to commit and a rule does not. This
replaces the owner's first phrasing, "the relation is dynamics not statics",
which would wrongly imply that an isolated pair's relation changes in time.

**Birth and death.** Born from contact and nothing else, which is a theorem
rather than a case count: local operations plus any classical communication
never make an area. Not ended but shared out, because entanglement is
monogamous, so whatever A builds with the room comes off what it holds with B.
That is decoherence entire, and measurement is the same at volume.

**The third mode.** Added after the owner asked whether monogamy is stronger
than polygamy. Per partner monogamy wins outright, since one partner reaches `1`
while `n` partners cap each other at `1/sqrt(n)`. Summed across partners
polygamy wins, since the total grows as `sqrt(n)`. For doing anything that needs
a whole unit, monogamy wins again, because thin shares do not glue together. And
there is a third state that is neither: every pair at zero while the trio is
maximal.

## The widget

Three whole numbers `a, b, c` for one excitation over three parties, the W-class
state `a|100> + b|010> + c|001>`.

```text
Q        = a^2 + b^2 + c^2
C(A,B)   = 2ab/Q,   C(A,C) = 2ac/Q
identity C(A,B)^2 + C(A,C)^2 + tau = C(A,BC)^2,  with tau = 0 on this family
```

Four presets sit on `Q = 26` with `a = 1`, holding the total at `25/169` while
the split moves through `5/13, 0` to `0, 5/13`. A fifth, `5,3,4`, drives the
capacity to exactly `1` split `3/5` and `4/5`. A sixth switches to GHZ, where
both pairs read `0`, the three-way part reads `1`, and the total stays `1`. The
steppers fade to dots in that mode, since the three numbers no longer describe
what is shown, and any stepper press returns to the W family.

The three-way segment is a hatch in the muted ink rather than a third hue. The
validator gave aqua against blue a tritan separation of `4.0` in dark mode,
below any usable floor, and texture is the documented fallback. It also reads
better: that part belongs to no pair, so it should not wear a party's colour.

Birth needed no widget. The lattice already shows it: press "parallel" for two
arrows with no area, then drag one.

## Defects found and fixed this round

The new preset buttons reuse class `p`, so the lattice handler matched them and
threw eight times on an undefined `data-pre`. Handler scoped to
`button.p[data-pre]`. Caught by watching `pageerror`.

The capacity readout collided with the row title whenever the bar was short.
Moved to the right end of the row.

## Checks

```text
monogamy identity over every (a,b,c) in 1..6 x 0..6 x 0..6        0 violations
capacity never exceeds 1 on the same sweep                        0 violations
five W presets against exact rationals                            all match
GHZ preset reads 0, 0, 1, 1                                       exact
a stepper press leaves the trio mode and restores the numbers      holds
steppers: a floors at 1, b and c cannot both reach 0              holds
Pick sweep, all arrow pairs in [-4,4]^2                           0 mismatches
16 notes, distinct scores                                         {+2, -2}
all 16 note states driven through the toggles                     only (+2, 4) and (-2, 4)
preset S^2 against (4Q^2+16A^2)/Q^2                               exact on all five
page errors                                                       none
```

Prose: 1684 words, 31 paragraphs, 0 em dashes, 0 semicolons, 0 mid-sentence
colons, 63 short sentences of 161 against a floor of 11, 2 monotone runs, no
hedges and no canonical AI vocabulary from the humanize checklist.

## Standing instruction

Do not strengthen the fenced paragraph in `The cheat sheet was real`, and do not
promote the TWIST-J mention past "a door, not a result". The detector pass and
the final human read are the owner's, agreed as the last step rather than
something a session can run.

## Set status

```text
vztah-ma-tvar.html      CZ   the relation as an area nobody owns
listek-v-kapse.html     CZ   why prepared answers cannot substitute
vztah-na-prstech.html   CZ   the relation as a whole number
entangled.html          EN   the whole argument, birth, death, the trio, the door
```

The Czech pages carry none of the later material.
