# AUDIT G9 SETTLEMENT, C-METRO-FORBIDDEN-WITNESSES-3

Status of this document: audit of my own tooling. NO AUTHORITY. Incubation
lane. It settles a disagreement between two of my own artifacts and records a
diagnosis of mine that turned out to be wrong.

```text
date        2026-08-20
candidate   C-METRO-FORBIDDEN-WITNESSES-3
prereg      c45e9c2c26104031d232e26fbc88c7a86c8bd6f42ea86e2dc473381d190fa6ca
basis       Public Canon v54, tag canon-v54, CONTENT_COMMIT 0bfd67b4
            re-fetched 2026-08-20, head 483591d, SHA256SUMS 5 of 5 OK,
            canon/CANON.md 281522 B sha256 c48254a3c73133244547231bb2cb63ca2f232de64a6f1c26d29a67d8684d88c2
            tag and content commit both ancestors of main. Basis unchanged.
```

## What happened

`verify_metro_forbidden_3.py` reported gate G9 PASS on all five witnesses.
`breaker_metro_forbidden_3.py` reported W5 as CONVENTION-DEPENDENT under the
same flip. Two of my own tools contradicted each other on the same object.

I then wrote a hand diagnosis concluding that BOTH tools were defective in
opposite directions, and that the verifier's G9 was too weak because its
`flip(P) = (ns,(d[1],d[0]),w)` swaps the digit families in the storage slots
and so also renames which position slot feeds which family. On that reading G9
exceeded its own text, which by Field 5 of PREREG-1 is an integrity STOP and
kills the candidate under its id.

That diagnosis was half right. The half that was wrong is the half that would
have killed the candidate.

## The settlement

Two questions, both settled by computation rather than by reading code.

### Question 1. Does G9 as implemented decide G9 as declared?

Declared text: "coordinate 2 acts first and the five frozen readings are
re-evaluated unchanged". Input labels are not permuted. Implemented: the
family swap above.

The implemented map differs from the declared one by a relabelling of the
position set and of the key set. A relabelling is a bijection, and the
existence of a functional obstruction is a property of the fibres of a map, so
it is invariant under bijections on either side. That is an argument. My last
argument was wrong, so the argument is not the evidence.

`settle_g9.py` evaluates both readings side by side on the five named
witnesses. `settle_g9_exhaustive.py` does it on every tuple of both frozen
boxes, for all five forbidden readings.

```text
EXHAUSTIVE G9 SETTLEMENT   BOX-2 2304 tuples, BOX-3 19683 tuples

reading                  declared  disagreements
T1 FLATTEN                  16140              0
T2 ERASE-NAMES              18666              0
T3a WEIGHTS-STRICT          12702              0
T4 OUTPUT-REGROUP            9072              0
T5 BOX-REORDER              13116              0

total disagreements 0 over 21987 tuples x 5 readings
```

The declared counts under the flip are equal, entry by entry, to the
convention-A census of PREREG-2: T1 16140, T3a 12702, T4 9072, T5 13116. The
census is symmetric under the flip. That is a second, independent reason to
expect 0 disagreements, and it was not designed in.

VERDICT: G9 as implemented is exactly G9 as declared on both frozen boxes. It
does not exceed its text. No integrity STOP. The candidate stands.

### Question 2. Which tool was wrong, then?

The breaker, and only the breaker.

`breaker_metro_forbidden_3.py` defines

```python
def v_rev(P, m, s, a, b):
    ns, d, w = P
    return w[d[0][a][d[1][b][s]]]
```

which ignores `m` and always returns the coordinate-2-first composite. Attack 2
hands it `build_flipped(P)`, so the source `s5` also returns the
coordinate-2-first composite. The attack therefore asked whether a value is a
function of itself. It always is. W5 was reported dead by a tautology.

That is a false kill: an artefact of the breaker, not a property of the
witness. Direct computation on W5 with input labels held fixed:

```text
convention A, coordinate 1 first: is the reverse a function of the stream?
  OBSTRUCTION at (s,a,b) = (0,0,1) and (0,1,1),  values 0 vs 1
convention B, coordinate 2 first: is the reverse a function of the stream?
  OBSTRUCTION at (s,a,b) = (0,0,0) and (0,0,1),  values 0 vs 1
```

W5 obstructs T5 under both conventions. It is a genuine two-sided witness, as
PREREG-3 declared.

## Correction

`breaker_metro_forbidden_3_rev2.py` builds the forward table and the
opposite-order table together, so "reverse" always means the reverse of the
order in play. Revision 1 is kept in the record, defect and all. The corrected
breaker adds Attack 5, which re-runs the declared-versus-implemented G9
comparison over both boxes by table construction rather than by composing on
the state, so the coding is independent of both the verifier and
`settle_g9_exhaustive.py`. It finds 0 disagreements over 21987 tuples.

Corrected breaker result: no kill. Every attack failed to destroy the claim.

## What this cost, and what it is worth

Two artifacts disagreed, I reasoned about the code, and the reasoning was
wrong in the direction that would have thrown away a correct result. The rule
that saved it is the boring one: when two tools disagree, do not adjudicate by
reading them, compute the disputed quantity a third way.

Carried forward as a working rule for this lane: a gate that reformulates its
declared object rather than implementing it literally must ship with an
exhaustive equivalence check against the literal reading, on the same frozen
box. G9 now has one.

## Pins

```text
settle_g9.py             bc65f55261b21daafb4f3fbdb36801db49857f43a2f8424a035e313f045d30da
settle_g9_exhaustive.py  16221880c7819ce79bc368a4c2193635e1f63e829486b049f2d7209208cef5f9
breaker rev 1            26bc6eab2dd9f516b596bbbe9956fd74af25d941bee0217f3b272c77a0177dcd
breaker rev 2            e7469235fcc23e4853fa2d8b18769e1be1f1badec93f7dce82f81a4430b0b035
verify_metro_forbidden_3.py
                         cf9f180888bc364a746f658d944adb96b4ecd26d62a6b20345b67df8cdc2748e
```
