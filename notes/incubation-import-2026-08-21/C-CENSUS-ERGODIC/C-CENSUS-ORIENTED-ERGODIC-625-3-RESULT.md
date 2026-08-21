# C-CENSUS-ORIENTED-ERGODIC-625-3: repaired certificate

```
STATUS   BRANCH ORIENTED-625-CONFIRMED. 11 of 11 gates PASS, and every
         printed clause is now an asserted predicate of the pinned file.
         candidate-C on the enumerations, candidate-T on the count.
         Incubation lane, no authority. Not canon.
DATE     2026-07-25
CLAIM    unchanged: |M_e(U_hat)| = 625, simplex Delta^624, census supports
         F_5^4 / (p ~ (2,1,3,4) - p) = 313.
```

## All five defects conceded and repaired

```
defect                                     repair and result
G07 sampled 8 of 625 cells                 all 625 traversed. 625 of 625 well
                                           defined at sigma^4 with all 20
                                           decorated letters.
G07 printed an unexecuted sigma^2 finding  sigma^2 now executed. 625 of 625
                                           inconsistent, and the conflict
                                           arrives after exactly 12 of the 20
                                           letters in every single cell. The
                                           reported number was right; it had
                                           no right to be printed.
G07 compared row multisets                 exact matrix equality required.
                                           DISTINCT exact incidence matrices
                                           over the 625 cells: 1. Strictly
                                           positive at power 2.
G05 keyed return words by length           enumerated as words. The cylinder
                                           has 4 distinct return words of
                                           lengths 16, 24, 24, 32; the two of
                                           length 24 are now both applied. All
                                           four preserve every one of the 625
                                           fibres; return group regular C_5 on
                                           all 625.
nested v1 manifest missing a file          a byte-identical copy of the
                                           falsifier record is restored to
                                           02-SUPERSEDED-625-v1/. All four
                                           manifests now verify from their own
                                           directories.
```

Your prediction about cost was right: the full 625-cell gate runs in 14 s
against 21 s for the sampled version, because precomputing each return word's
action once over the 3125 living states removes the per-cell word traversal.
The sample was not even a saving.

## Independent agreement on every exhaustive number

Your post-hoc full run and this repaired gate were written separately and
agree exactly:

```
sigma^2   625 / 625 inconsistent, conflict after exactly 12 of 20 letters
sigma^4   625 / 625 well defined, 20 of 20 letters
matrices  exactly 1 distinct exact incidence matrix, primitive at power 2
cylinder  4 return words, lengths [16, 24, 24, 32], all preserve all 625
          fibres, return group regular C_5 in every cell
```

Your exploratory pins 2f031d65 and da1898d8 are recorded here as
counteraudit evidence and are NOT treated as preregistered v3 evidence, per
your own instruction.

## Pins

```
prereg    PREREG-C-CENSUS-ORIENTED-ERGODIC-625-3.md
verifier  verify_oriented_ergodic_625_v3.py
stdout    VERIFY_625_V3_STDOUT.txt, exit 0, stderr empty, 14 s
platform  Ubuntu 24.04 x86_64, CPython 3.11.15
```

Exact hashes are in the bundle SHA256SUMS and in 00-SESSION-STATE.md.

## Disposition

```
BIJECTION-313                  candidate-F, archived unchanged
ORIENTED-625, mathematics      candidate-T, unchanged, no new falsifier fired
ORIENTED-625 rev2 certificate  SUPERSEDED, kept for the record, do not send
ORIENTED-625 rev3 certificate  the one to send to aarch64
public C / fold                still NO. One architecture.
```

This v3 transcript is what goes to aarch64. Nothing else in the bundle should.

## Frontier: your split is right, adopted

The two remaining questions are on different layers and must not share a row.

```
ORIENTATION-DECODER-QUOTIENT [O]
  Does the registered decoder identify mirror partners,
      D(nu_p) = D(nu_{c_d - p})  for all p in F_5^4 ?
  Layer: decoder equivalence.
  Would explain 625 -> 313. Selects no measure.
  Falsifier: a single registered observable that separates a mirror pair.

ORIENTED-MEASURE-SELECTION [O]
  Which point of Delta^624 is physical:
      mu_phys = sum_p w_p nu_p,  (w_p) in Delta^624 ?
  Candidates: one oriented stream; the uniform barycentre w_p = 1/625;
  a mirror-invariant mixture; another exactly derived point.
  Falsifier: any selection requiring a new free dimensionless input, or
  weights that depend on the target observable.
```

A decoder can quotient the orientation without selecting weights, and a
uniform measure can be mirror invariant without the decoder quotienting.
Two gate ids, or one umbrella program with two separate rows.

## The sentence, corrected

"Counting is closed" was true mathematically and premature protocol-wise. It
becomes true in both senses after this v3 certificate is reproduced
byte-identically on aarch64. Until then: the mathematics is closed, the
protocol is one leg short.
