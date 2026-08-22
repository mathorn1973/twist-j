# notes/C-RECORD-CRT-IDEMPOTENT-1

NON-CANONICAL. Incubation candidate, no authority, no Canon change, no
`canon/` file touched. Durable git handoff of a candidate developed
2026-08-22 against Public Canon v60 (tag `canon-v60`, content commit
`18b21bdaf2c2236c9444b120900277ccfb63e050`, `canon/CANON.md` SHA-256
`9387b75f2036ac6aff5737255956b93fb9b906511b8184ae4c1c999e8ed46db0`).

It states the record structure of finite quotients of `R = Z[zeta_5]`:
for `I = prod p_i^{e_i}` the Chinese remainder decomposition gives
`Idem(R/I) ~= F_2^r ~= Idem(R/sqrt I)` with `r = |Supp(I)|`, so the prime
support forces the Boolean algebra of outcomes while the exponents carry
only the local thickness. Around that core it fixes the three arithmetic
positions of `J` (ramified residue `lambda`, binary residue `(2)`,
archimedean), the record minima (`6`, `55`, `80`), the `J`-specificity of
the binary position against `Z[i]` and `Z[zeta_7]`, and a modest form of
cyclotomic unit-rank minimality.

## Contents

```text
C-RECORD-CRT-IDEMPOTENT-1.md         candidate claim, guards, preregistration
SYNTHESIS-F2-J-M_2026-08-22.md       companion synthesis note (rev 3) and its
                                     correction record; the origin document
verify_record_crt_idempotent.py      exact verifier, stdlib only, 40 gates
record_crt_idempotent.stdout.txt     pinned stdout, exit 0, empty stderr
SHA256SUMS                           pins for the two files above
README.md                            this manifest
```

## Reproduce

```sh
cd notes/C-RECORD-CRT-IDEMPOTENT-1
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
    python3 verify_record_crt_idempotent.py
sha256sum -c SHA256SUMS
```

Expected: 40 gates OK, `RESULT: ALL GATES OK`, exit 0, empty stderr,
runtime well under a second. One platform only (x86_64, Python 3) — the
two-architecture byte-identity gate belongs to a public probe at promotion,
not to this incubation run.

## What this is not

No decoder, measure, sampling, event semantics, coarse-graining, RG flow,
continuum limit, or physical reading follows. The three positions are named
arithmetically; reading them as write / read / scale is a dictionary act
outside this note, and `(2) subset Z[zeta_5]` is not asserted to be the
`K_8 = Q(zeta_8)` read place of `TWO-PLACE-PHYSICS [D]`. Whether a
physically completed event must land in the idempotent class is
`QDD-TERMINAL-EVENT-SEMANTICS [O]` and is untouched; guard G2 of the
candidate states the fence explicitly. See section 2 of the candidate for
all six guards.

## Public predecessors

`CARRY-PENTAD [T]` (`canon/REGISTRY.tsv` row 232), `J-BINARY-NORM-DESCENT
[T]` (row 16), `CARRY-QUADRATIC-SYMMETRY [T]` (row 15), and, for the
unit-rank clause, `QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS [T]` and
`ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM [T]`. To be re-confirmed
from the public head at claim time.
