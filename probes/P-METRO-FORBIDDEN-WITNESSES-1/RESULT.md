# P-METRO-FORBIDDEN-WITNESSES-1 result

Status: `DECIDED AND AUDITED / CANON UNCHANGED / PARENT STILL OPEN`

## Disposition

```text
claim:      each of the five forbidden entries named in canon section 15,
            under the five ratified readings, admits an exact functional
            obstruction: a pair of positions with equal pointwise L5 stream
            whose transported values differ. None of the five is an
            admissible arrow.
witnesses:  five, at most four states each, hand-checkable, each reproducing
            its declared pair of positions and values exactly.
census:     over the two frozen boxes of 2304 and 19683 tuples, 21987 in all,
            the obstructing counts are 16140 flattening, 18666 erasing names,
            12702 factor weights, 9072 output regrouping, 13116 box
            reordering. Gate G10 enforces that every count is over the same
            declared domain.
controls:   the four admitted arrows of METRO-REDUCTION-ARROWS [C] exhibit
            zero obstructions across both boxes under their own exact
            preconditions: relabel 0, restrict 0, Nerode 0 with all 21987
            applicable, coordinate permutation 0 on the 4329 commuting tuples.
convention: all five obstructions survive reading the composition in the
            opposite order.
parent:     METRO-REDUCTION-CALCULUS [O] stays O and STOP. B is discharged for
            the five entries the Canon names; D and E are untouched.
integrity:  no STOP. One formal execution, exit zero, empty stderr, 12/12
            gates PASS, stdout equal to EXPECTED.txt. Byte identical on
            CPython 3.10, 3.11, 3.12 and 3.13.
```

## Independent attempt to break it

The verifier is carried in from the incubation lane, as `PREREG.md` declares.
The independent code path is the breaker, written fresh for this probe and
sharing no routine with it: protocols encoded as base-`|S|` integer tables
instead of nested tuples, composites precomputed before the output is read,
both boxes enumerated by integer counters instead of `itertools.product`, and
every census count recomputed from scratch. Final state:
`BREAKER 0 kills in 8 attacks`.

```text
B1 census        the independent implementation reproduces all six counts
                 exactly: 16140, 18666, 12702, 9288, 9072, 13116 over 21987
                 tuples, boxes 2304 and 19683. This is the confirmation that
                 matters: the numbers the proposed row carries are not the
                 output of one program
B2 arrows        no admitted arrow breaks the pointwise stream anywhere in
                 either box under its own precondition
B3 controls      commuting tuples 4329 and the non-commuting remainder 13320,
                 both as declared
B4 witnesses     every declared pair of positions and values reproduces
B5 transport     no distinction-preserving tau makes W1, W3 or W4 well
                 defined, and W5 admits no tau at all
B6 convention    all five obstructions survive coordinate 2 acting first
B7 collision     the ratified reading of output regrouping does not collapse
                 onto the admitted Nerode quotient. On the witness, w
                 identifies two states that Nerode separates, so the level-set
                 quotient is strictly coarser. This is the machine check of
                 the ruling's own decisive argument: were the two the same
                 transformation, one operation would be admitted and forbidden
                 at once and the parent would falsify negatively
B8 degeneracy    recorded below
```

## Finding: how the tau clause must be read

`B5` in its first revision reported `KILL`. The kill was false and the
diagnosis is kept rather than deleted, because it sharpens the claim.

```text
what it did   searched every assignment of output values to transported
              positions for a tau satisfying the displayed admissibility
              equation, and found one
what it found the constant transport. With the transformed object free and tau
              unrestricted, a constant tau satisfies
              Stream_(T(P))(sigma(s),iota(n)) = tau(Stream_P(s,n)) trivially,
              by collapsing the stream to a point. This is true for the three
              entries whose obstruction is of the collapsing-index shape, W1,
              W3 and W4. It is not true for W5, which excludes every tau
              outright
why it is not a defect in the claim
              a reduction arrow is typed with an output transport tau_R that
              carries w to w', and every arrow registered by
              METRO-REDUCTION-ARROWS carries tau_R = identity. A transport
              that destroys every distinction of the stream is not in that
              type. The exclusion the three witnesses carry is of every
              distinction-preserving transport, and B5 now searches exactly
              that class exhaustively and finds none
consequence   the pinned row text says the obstruction "excludes every output
              transport tau at once rather than one family of them". That is
              exact for W5 and needs the reading above for W1, W3 and W4. A
              fold should either adopt the reading explicitly or tighten the
              clause to "excludes every distinction-preserving output
              transport at once". The pinned PREREG.md and FOLD-ROWS.tsv were
              not amended, because a pinned file is not amended
```

## Proposed registry consequence (a later sealed fold, not this probe)

One new row, exact text frozen in `FOLD-ROWS.tsv`, plus the parent clause
replacement and the canon paragraph in `FOLD-EDITS.md`.

```text
METRO-FORBIDDEN-WITNESSES  C  canon section 15
```

Ledger delta: claims +1, C +1. No frontier list item, because a C row is not
live. The parent `METRO-REDUCTION-CALCULUS [O]` keeps its status, its STOP
state and its falsifier; only its obligation B clause changes, identically in
`REGISTRY.tsv` and `FRONTIER.md`, to record that the five frozen readings are
the ratified meaning of the five phrases and that B is discharged for those
five entries while any further entry stays open.

## Evidence boundary

```text
The parent is not closed. Discharging obligation B for five entries is not
closing METRO-REDUCTION-CALCULUS, which stays O and STOP until D and E fall.
No summary may say otherwise.

No completeness claim is made about the forbidden catalogue itself. Whether
the Canon's list of five is complete is not addressed.

Nothing is claimed at |S| > 4, q > 2, a > 2, r > 1 or for multi-digit words,
and no blocking, normalization, decision, terminal-value, L6, cross-layer,
physical or SI statement is made. Common q^k blocking is obligation D and is
untouched.

METRO-REDUCTION-ARROWS [C] is a control and does not move. The recorded report
that a transported coordinate swap breaks the pointwise stream on 13320
non-commuting tuples is deliberately not gated: it is a question about a
closed row, and this probe will not move a closed row by a side effect. If it
needs settling, that is its own probe with its own preregistration.

The status is C, not T. The five obstructions would carry T on their own; the
census over a finite box is computation at a declared finite range, and the
row is proposed at the weaker of the two.
```
