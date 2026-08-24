# NOTE-BELL-TICKET-INTERACTIVE (2026-08-19)

NON-CANONICAL. Exposition artifact, companion to
`claude/NOTE-RELATIONAL-AREA-INTERACTIVE_2026-08-19.md`. Standard quantum
mechanics only, explicitly not TWIST-specific per the owner. No claim, no
verifier, no registry effect. It touches the same subject matter as
`BELL-CAUSAL-ACCOUNTING [O]` and supplies nothing toward that contract.

## What it is

`listek-v-kapse.html`, a single self-contained Czech interactive page answering
the owner's question: show why pre-prepared answers cannot stand in for the
relation. Built around the fact that the impossibility is provable by finite
enumeration rather than by any limiting argument, which is the form the owner's
program prefers.

## The argument as the page stages it

A local deterministic strategy is exactly a pair of answer cards: Alice writes
`A(1), A(2)` and Bob writes `B(1), B(2)`, each in `{+1,-1}`. Four binary slots,
so sixteen possible tickets, and that is the entire space.

```text
S = A(1)B(1) + A(1)B(2) + A(2)B(1) - A(2)B(2)
  = A(1)(B(1)+B(2)) + A(2)(B(1)-B(2))
```

One of the two brackets is always `0` and the other is always `+-2`, so every
one of the sixteen tickets gives `S = +2` or `S = -2` exactly. Eight each. The
page lets the owner flip the four slots by hand, then sweeps all sixteen and
plots them on a number line: two towers of eight dots and nothing anywhere else.

Shared randomness adds nothing, because any distribution over the sixteen is a
convex combination and an average never leaves the interval between the extremes.
The page draws that interval as the grey band and says so in those words. This is
the part usually underexplained, so it gets its own paragraph rather than a
parenthesis.

Against it, the quantum side with in-plane measurements on
`cos(t)|00> + sin(t)|11>`:

```text
E(a,b) = C sin(a) sin(b) + cos(a) cos(b),   C = sin(2t)
max S  = 2 sqrt(1 + C^2)   at a0=0, a1=90, b0=+atan(C), b1=-atan(C)
```

Four draggable directions on a dial plus a slider for `C`, which is the same `C`
as the parallelogram area on the companion page. At `C = 0` the best achievable
value is exactly `2`, on the band edge and never outside it. That is the point
the interaction is built to deliver: no relation, no exit.

## The no-signalling panel, and a correction made during the build

Alice's own marginal for her question at angle `a`:

```text
P(+1 | a) = (1 + |b| cos a)/2,     |b| = sqrt(1 - C^2)
```

The first version of this panel hard-coded 50/50, which is only correct at
`C = 1`. That was wrong and was replaced by the live formula. The replacement is
also the better exposition: the claim is not that Alice sees a fair coin, it is
that whatever she sees is identical under both of Bob's settings.

Verified operationally through the rendered UI rather than by reading the source:
at `C = 0.6` with the optimal angles, both of Bob's directions were rotated by
large amounts, driving `S` from its optimum down to `+0.290`, and Alice's two
bar groups stayed at `90,0 % / 10,0 %` throughout, unchanged and identical.

## Boundaries stated on the page

- The ticket must be blind to the other side's question. That prohibition is the
  entire content of the word "local", it is what fails, and it is also what keeps
  the marginals fixed. Violated locality and controllable signalling are separate
  tests. A ticket allowed to read the far question reaches `4`.
- Measurement independence is assumed and cannot be proved, only narrowed.
- The enumeration says what cannot hold, not what holds instead. Reading "action
  at a distance" out of it adds a sentence no measurement supports.
- Everything on the page is the pure-state case. For mixed states "entangled"
  and "violates the bound" come apart; Werner at `p = 1/2` is entangled and
  violates nothing. The owner's position, which the page adopts: that blurring is
  a feature of the world, not a defect of the picture.

## Checks run

Through the rendered page under Chromium, light and dark, 980 and 390 px.

```text
all 16 tickets driven by clicking the actual switches -> value set is exactly {+2, -2}
optimal-angle preset vs theory 2 sqrt(1+C^2):
  C=0,000 -> 2,000   C=0,250 -> 2,062   C=0,500 -> 2,236
  C=0,750 -> 2,500   C=1,000 -> 2,828        all exact
marginals vs (1 + |b| cos a)/2 at five (C, a) points   all exact, both groups equal
pointer drag and multi-press keyboard on all four dial markers   OK
no page errors
```

A real defect was found and fixed by the keyboard test: the dial was rebuilt with
`innerHTML=''` on every update, which destroyed the focused element, so arrow-key
adjustment worked for exactly one press. The dial is now built once and only its
attributes are updated.

## Where it could go

Reading surface, not a claim. Belongs beside the companion page or nowhere, and
must not be presented as TWIST-J content.
