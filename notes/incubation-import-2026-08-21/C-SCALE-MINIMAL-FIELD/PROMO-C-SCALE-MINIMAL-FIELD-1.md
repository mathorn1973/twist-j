# PROMO-C-SCALE-MINIMAL-FIELD-1

A hand-off artifact. A canon fold can consume this document without reading
anything else in the incubation lane. It promotes nothing by existing.

```text
CANDIDATE:   C-SCALE-MINIMAL-FIELD-1
TARGET LINE: mathorn1973/twist-j, main
BASIS:       Public Canon v58 (canon-v58, content 05a0749e,
             CANON_SHA256 647822f5...6acc1, 304010 B, SHA256SUMS 5 of 5 OK)
PROPOSED:    one new [T] row and one new [O] row, plus three lines of prose
             in canon/CORE.md, section "Why five". No existing row moves.
LAYER:       L1 state. Pure arithmetic. No decoder, measure, apparatus,
             physical selection, or lift to L2-L6 is proposed.
DO NOT FOLD  into release 59. Single architecture this session. This needs
             a normal public probe with the two-architecture leg first.
```

## 1. The exact statements

```text
SCALE-MINIMAL-FIELD [T]
    a number field has a unit of infinite order exactly when its unit rank
    r_1 + r_2 - 1 is at least one; among all such fields Q(sqrt5) is the
    unique minimizer of absolute discriminant, with minimum 5 and
    fundamental unit phi = (1 + sqrt5)/2; among cyclotomic fields with a
    unit of infinite order Q(zeta_5) is the unique minimizer, with minimum
    125, the orders n = 5 and n = 10 presenting the same field; the
    optimization class is chosen and is not claimed to be forced by J, by
    the decoder, or by Nature, and requiring extra torsion in place of a
    scale returns 3 rather than 5 in the same optimization

SCALE-ELEMENT-NONSELECTION [T]
    the four elements 1 + zeta_5^a for a = 1,2,3,4 are Galois conjugates
    with the single minimal polynomial x^4 - 3x^3 + 4x^2 - 2x + 1 =
    Phi_5(x - 1), hence equal norm 1, equal trace 3, and equal Tr(u^k) for
    every k; therefore no invariant of Z[zeta_5] over Q distinguishes
    J = 1 + zeta_5^2 from 1 + zeta_5, and the axiom's choice of J is fixed
    only by an archimedean embedding together with the choice of the
    contracting representative, abs(1 + zeta_5^2) = phi^-1 against
    abs(1 + zeta_5) = phi; no physical, temporal, or causal reading of that
    choice is asserted here
```

## 2. Falsifiers, one line each

```text
SCALE-MINIMAL-FIELD          fires on a number field of absolute
                             discriminant below 5 containing a unit of
                             infinite order, on a second field attaining 5
                             with such a unit, or on a cyclotomic field
                             other than Q(zeta_5) of absolute discriminant
                             at most 125 containing one
SCALE-ELEMENT-NONSELECTION   fires on any polynomial invariant over Q,
                             evaluated on Z[zeta_5], that takes different
                             values at 1 + zeta_5 and 1 + zeta_5^2
```

## 3. Registry rows to add

Schema is `claim_id  status  scope  canon_section  evidence  falsifier`,
tab separated, evidence a path or the word inline.

```text
SCALE-MINIMAL-FIELD	T	<statement above>	Why five	probes/P-SCALE-MINIMAL-FIELD-1	<falsifier above>
SCALE-ELEMENT-NONSELECTION	T	<statement above>	Why five	probes/P-SCALE-MINIMAL-FIELD-1	<falsifier above>
```

## 4. canon/CORE.md edit

Section "Why five, twice" becomes "Why five, three times", and this is
inserted after the existing two bullets, before the paragraph beginning
"These are separate frozen classes":

```text
- SCALE-MINIMAL-FIELD [T] says that among number fields admitting a unit of
  infinite order, Q(sqrt5) is the unique absolute-discriminant minimizer at
  5, and Q(zeta_5) is the unique cyclotomic one at 125.
```

and the following sentence is appended to the paragraph after them:

```text
The third answer optimizes over a third class and inherits the same
limitation as the first two: requiring extra torsion rather than a scale
returns three, so the class carries the selection and the minimization does
not. SCALE-ELEMENT-NONSELECTION [T] closes the matching negative: the field
can be reached by minimization, the element J cannot be reached by any
rational invariant.
```

Checked against tools/check_canon.py before proposal: none of the five
authority words the tool rejects, and none of its eight forbidden history
phrases, occurs anywhere in the proposed registry rows or CORE.md text
above.

## 5. Frontier edit

None. No live H or O row moves. `SCALE-ELEMENT-NONSELECTION` closes a
question that was not on the frontier as a row, so nothing is removed.

## 6. Dependency edges

```text
depends on   J-UNIT [T], J-PROJECTIONS [T], J-GOLDEN-BRIDGE [T]
             for the identification of phi and of abs(J) = phi^-1
sits beside  QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS [T]
             ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM [T]
             as a third member of the same non-chain
constrains   any future attempt to derive the axiom's element from the ring
             alone. SCALE-ELEMENT-NONSELECTION forbids it.
does NOT     touch BELL-CAUSAL-ACCOUNTING, QDD-INSTRUMENT-NONSELECTION,
             READING-SPLIT, TWO-PLACE-PHYSICS, or any physical row
```

## 7. Verifier and pins

```text
PREREG-C-SCALE-MINIMAL-FIELD-1.md
    bc1ce96f63dd9086d3b090ffcda1ea881687a4508fcec13467fb64a51a570d77
verify_scale_minimal_field_1.py
    30f72a22d0974efcd4a6dbfc2dbd0878f74c7e35e23ffa5129922c393c755496
  stdout, 20 of 20 PASS, 0 findings, exit 0
    6d16ac8aa31ee056b4fbc9fa499bce19a16b7ea7c5ff8af25e231a564a44ef23
breaker_scale_minimal_field_1b.py
    b943625fbd300e018a07c5f2183cb475b349316d42eed2918848afcec0e27670
  stdout, 5 of 7 attacks survived, 2 intended framing breaks
    2948277523f7c4673ac34441b4eb2dfd995e56f9c18e7f1af793a35c85a93188
ARCHIVE_breaker_scale_minimal_field_1_BR4-DEFECTIVE.py
    3cda84fe287e34795a2ebaf64dec63788a3c45a86ba925b699c37df37247b79d
    kept, not deleted. its leg BR4 used an irreducibility test that never
    tested the root zero and reported a spurious cubic of absolute
    discriminant 3. run 1b reports the correct 23.

Standard library only. Integers and Fractions only. No float in any
assertion. No discriminant table lookup: every discriminant is computed,
and the cyclotomic ones are computed twice by independent routes.
Linux x86_64, CPython 3.11.15,
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
Two runs, byte-identical stdout, empty stderr.
```

## 8. What a public probe still owes before this folds

```text
1  a public issue claiming P-SCALE-MINIMAL-FIELD-1, checked against
   existing issues, branches and probes/ for collision
2  PREREG.md with the six fields, pinned before first execution on the
   probe branch
3  verify.py under 120 seconds from repository root, run on aarch64 and on
   the GitHub x86_64 check, byte-identical stdout, EXPECTED.txt, RUN.md,
   RESULT.md
4  a second author attempting the counterexample by an independent code
   path, not a rerun of this one
```
