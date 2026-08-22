# notes/C-RECORD-CRT-IDEMPOTENT-1

NON-CANONICAL. Incubation candidate, revision 2, no authority, no Canon
change, no `canon/` file touched. Developed 2026-08-22 against Public Canon
v60 (tag `canon-v60`, content commit
`18b21bdaf2c2236c9444b120900277ccfb63e050`, `canon/CANON.md` SHA-256
`9387b75f2036ac6aff5737255956b93fb9b906511b8184ae4c1c999e8ed46db0`).

For `R = Z[zeta_5]` and a nonzero proper ideal `I = prod P^{e_P}` the note
states the record quotient calculus: `Idem(R/I)` is canonically the power set
of `Supp(I)`; the exponents are invisible to that layer and carry the Loewy
profile `|n^k/n^(k+1)| = prod{N(P) : e_P > k}` with `L(R/I) = max_P e_P`;
every `R`-algebra map between finite record rings is the canonical projection
and exists exactly when one ideal contains the other, so the category is thin
and strict quotients have no section; and, negatively, a fixed support admits
arbitrary Loewy length, so the Boolean skeleton cannot determine the
filtration depth.

## Contents

```text
C-RECORD-CRT-IDEMPOTENT-1.md          candidate claim, guards, preregistration,
                                      dead-run record, result
SYNTHESIS-F2-J-M_2026-08-22.md        companion synthesis note and its
                                      correction record; NOT part of the
                                      candidate scope
verify_record_quotient.py             exact verifier, stdlib only, 31 gates
record_quotient.stdout.txt            pinned stdout, exit 0, empty stderr
mutation_test.py                      mutation harness: the guarantee that the
                                      gates can fail
ARCHIVE_verify_record_crt_idempotent_rev1_DEFECTIVE.py
ARCHIVE_verify_record_crt_idempotent_rev1_DEFECTIVE_stdout.txt
                                      the rev1 run, archived unchanged; see
                                      section 6 of the candidate
SHA256SUMS                            pins for every file above
README.md                             this manifest
```

## Reproduce

```sh
cd notes/C-RECORD-CRT-IDEMPOTENT-1
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
    python3 verify_record_quotient.py
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
    python3 mutation_test.py
sha256sum -c SHA256SUMS
```

Expected: the verifier prints `GATE COUNT: 31` and `RESULT: ALL 31 GATES OK`,
exit 0, empty stderr, about 1.1 s. The harness prints
`31 mutations, all killed their targets; 31 of 31 gates covered; self-test
passed`, exit 0, about 72 s. One platform only (x86_64, Python 3); the POLICY
section 4 two-architecture gate is not claimed.

## Why there is a mutation harness

Three revisions of this note's verifier shipped gates that could not fail: a
hardcoded `True`, a comparison of a quantity with itself, and a cardinality
standing in for a structure claim. A source scan for literal constants cannot
see any of those, because they are construction-true rather than literal. The
harness breaks the thing each gate claims to test and requires the gate to
notice; a gate no mutation can kill does not ship. It also self-tests, by
injecting a deliberately tautological gate into a scratch copy and confirming
that the gate is reported as uncovered.

## What this is not

Layer L1 only. No decoder, measure, sampling, event semantics,
coarse-graining, RG flow, continuum limit, or physical reading follows.
Positions are not named write / read / scale here; the three-position reading,
the neighbouring-ring census, and cyclotomic unit-rank minimality are excluded
from the candidate and stay in the companion synthesis note as unverified
material. Whether a physically completed event must land in an idempotent
class is `QDD-TERMINAL-EVENT-SEMANTICS [O]` and is untouched; guard G2 of the
candidate states that fence. See section 3 for all five guards.

## Public predecessors

`CARRY-PENTAD [T]` (`canon/REGISTRY.tsv` row 232), `J-BINARY-NORM-DESCENT [T]`
(row 16), `CARRY-QUADRATIC-SYMMETRY [T]` (row 15). To be re-confirmed from the
public head at claim time.
