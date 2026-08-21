# NOTE-BORN-READING-PUBLIC-PAGE (2026-08-19)

NON-CANONICAL. Working note. No verifier is claimed for this note itself, it
edits no normative file, and it moves no registry row. It records an exposition
artifact and the checks run behind it.

## What was produced

A single self-contained Czech HTML page, `bornovo-cteni.html`, presenting the
Born reading carried by Public Canon v54 in two separately labelled directions,
written for an intelligent lay reader and typeset in the house style of
twistj.com (Cormorant Garamond, the site's own light and dark variable sets, no
external dependency except the Google Font already used by the hub).

Delivered to the owner. Not committed anywhere. Not published.

## Currency gate (Step 0), public target

```text
STATE          ACTIVE
CANON          Public Canon v54
AUTHORITY      mathorn1973/twist-j main
TAG            canon-v54            ancestor of main   CONFIRMED
CONTENT_COMMIT 0bfd67b47f1f59b1ef232b40a9a7d8e8c7459b0f  ancestor of main   CONFIRMED
CANON_BYTES    281522               measured 281522    MATCH
CANON_SHA256   c48254a3c73133244547231bb2cb63ca2f232de64a6f1c26d29a67d8684d88c2  MATCH
SHA256SUMS     5 of 5 OK
HEAD           18f1180 (merge of release/canon-v54)
```

## The two directions as put on the page

Direction one, derivation from the axiom. Presented at the status the Canon
gives it and no higher.

```text
axiom            J = 1 + j^2, N(J) = 1, Tr(J) = 3
two projections  |J| = 1/phi (modulus), arg J = 2 pi / 5 (argument)
five faces       w(k) = |1 + j^k|^2
exact values     w(0) = 4, 2w(1) = 3 + sqrt5, 2w(2) = 3 - sqrt5, w(3)=w(2), w(4)=w(1)
total mass       10, so sum w(k)/10 = 1 as an integer identity, not a normalization postulate
axiom face       J sits at k = 2, so w(2) = |J|^2 = phi^-2; also w(1)+w(2) = 3 = Tr(J), w(1)w(2) = 1
where the square comes from   C_+ = I + S, C_+ C_+^T = circ(2,1,0,0,1), spectrum = {w(k)}
mutually unbiased             position vs Fourier squared overlap 1/5 on all 25 pairs
Plancherel                    masses 2 and 10, ratio p = 5
half angle and spinor         BORN-HALF-ANGLE, BORN-RESIDUAL-SPLIT, SPIN-BISECTOR,
                              BORN-ORDER-STAIRCASE, staircase 4 -> 8 -> 16 first at
                              F_5 -> F_25 -> F_625
```

The page states, in the body and not in a footnote, that no positivity is
claimed in the finite algebra and that probability language belongs to
`MEASURE-BORN-VERB [D]` and to none of the four theorem rows.

Direction two, the integer deterministic description. The whole DQRC recipe is
printed (X integral, Q, Delta, H, the two integer comparator maxima, the signed
count), then the staircase for X = I with exact rationals and the limit
`S_inf = 2 sqrt(H)/Q = 2 sqrt(1 + C^2) = B_max`.

The page prints the honest boundary as its own top-level section, with five
entries: reencoding not derivation; `beta = 4` not selected by the census
identities; origin not selected, with the explicit `S_1^[0] = 0` against
`S_1^[1] = 4` witness above `2 sqrt2`; `BELL-CAUSAL-ACCOUNTING [O]` unmet with
its ten items listed; and the field boundary `sqrt2 not in Q(zeta_5)`.

The single epistemic sentence the page rests direction two on, and which is the
strongest form that does not overclaim: the number usually offered as proof
that nature must be probabilistic does not itself require probability, so the
continuous probabilistic foam is one available language rather than a necessity
that number forces.

## Verification run for this note

Four canonical verifiers, from a clean clone, repository root,
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.

```text
reproduce/born-faces/verify.py                       8/8   ALL PASS   byte identical to EXPECTED.txt
reproduce/born-quartet/verify.py                     11/11 ALL PASS   byte identical to EXPECTED.txt
reproduce/force-born-dictionary/verify.py            10/10 ALL PASS   byte identical to EXPECTED.txt
probes/P-DQRC-ARITHMETIC-RECONSTRUCTION-1/verify.py  15/15 gates PASS byte identical to EXPECTED.txt
```

The DQRC probe verifier raises `INTEGRITY STOP: CPython 3.12 required` under
3.11 and was therefore run under `python3.12`. Its stdout sha256 reproduced as
`7a776facd047c039b8b8f75ab627d93d75341d6da30eee7b2c76eb7cc6e4a94e`, 1032 bytes,
17 lines, equal to the value recorded in `RUN.md`, stderr empty. Platform
Ubuntu 24.04, CPython 3.12. This is a third independent leg on an already
two-architecture probe, recorded here as a review witness only; it is not a
probe run, is not pinned, and changes no leg class.

## Independent recomputation, second code path

`verify_born_reading_independent.py`, written from the Canon prose and not by
reusing any repository code path. Standard library only, integers and
`Fraction`, no float in any assertion. `Z[j]` modelled as
`Z[x]/(1 + x + x^2 + x^3 + x^4)`; the DQRC comparator maxima recomputed by
binary search on integer comparisons; the census rebuilt by literal counting
over `(k, r, t)` rather than by the closed form, then compared against the
closed form.

```text
A01..A19  axiom, trace, norm, sqrt5, the five weights, total mass, tilt, the
          axiom face identity w(2) = |J|^2, w(1)w(2) = 1, w(1)+w(2) = 3,
          Galois sigma_2, the Gram circulant, spectrum equals the weight set,
          Plancherel, the 1/5 overlap
B01..B11  Lagrange identity, binary increments, closed census and 2K margins,
          S_K and the one-sided deficit 0 <= S_inf - S_K < 4/K, Horodecki
          reencoding as an exact rational identity on squares, inserted parity
          -1 against local +1, the maximal sector S_inf^2 = 8, the (11,1,125)
          witness with S_inf^2 = 500/121, no sqrt5 value, beta nonselection
          over beta = 0..12, origin nonselection
RESULT    30/30 ALL PASS
```

Breaker attempts made and recorded, all of which the statements survived: the
census was rebuilt by counting instead of by the closed form on six witnesses
and six values of `K`; `beta` was swept over `0..12` on every witness to see
whether anything other than `4` reproduces `B_max` (nothing does, and nothing
else fails the census identities either, which is the nonselection result and
not a defect); the shifted origin was evaluated to find a finite value above
the asymptote and one was found at `S_1^[1] = 4`.

## What was deliberately not done

No public branch, no probe directory, no pin, no claim lock, no pull request.
The page is exposition and carries no new claim. If it is ever to live in the
repository it belongs under `notes/`, marked NON-CANONICAL, and if it is ever
to live on the hub it belongs under `twistjdotcom` as a reading surface that
states no version of its own and points at `STATUS.md`.

## Open owner decisions this raises

1. Where the page lands: hub page under `twistjdotcom`, `notes/` in the public
   repo, both, or neither.
2. Whether the Czech exposition lane wants this page as its Born head, and
   whether it should be paired with an English sibling for the physicist
   audience, which is a different and sharper text, not a translation.
3. Whether the independent verifier is worth keeping as a standing review
   witness for the Born block, or is a one-off.
