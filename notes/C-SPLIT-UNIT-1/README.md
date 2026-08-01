# notes/C-SPLIT-UNIT-1

NON-CANONICAL. Incubation candidate, no authority, no Canon change, no
canon/ file touched. This directory is the durable git handoff of a
candidate developed 2026-08-01 in the project incubation lane against
Public Canon v30 (tag canon-v30, content commit
857223fcd5e7bc8c8e68f1df768d6e8222b24ee0).

## Contents

```text
C-SPLIT-UNIT-1.md                      candidate claim and scope (rev 2)
AUDIT-C-SPLIT-UNIT-1_2026-08-01.md     accepted external audit, re-gradings
PREREG-C-SPLIT-UNIT-1_2026-08-01.md    frozen prereg (six fields, F1..F7)
verify_split_unit_1.py                 pinned verifier, 38 gates
break_split_unit_1.py                  pinned break attempt, 8 gates
split_unit_1.stdout.txt                verifier stdout, both architectures
split_unit_1_break.stdout.txt          breaker stdout, both architectures
RESULT-C-SPLIT-UNIT-1_2026-08-01.md    run record (immutable; AUDIT
                                       supersedes its prose labels)
SHA256SUMS                             hashes of the files above
```

## Reproduction

From this directory:

```sh
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 verify_split_unit_1.py
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 break_split_unit_1.py
```

Expected: exit 0 and exit 0; stdout byte-identical to the two committed
stdout files. Recorded legs: x86_64 (Linux, Python 3.11.15) and aarch64
(Ubuntu 24.04, Python 3.12.3), byte-identical.

## Frozen pins (recorded before first execution)

```text
f1278995449b1023c2e47589ad80e11ec003dbd78a0317d46e7bb09723ecdca5
  PREREG-C-SPLIT-UNIT-1_2026-08-01.md
5094d5fb15e1369dea760959c89fc4b6a5b050363427151142d88a56e275b913
  verify_split_unit_1.py
601661172325e5335d88f66f443f9cb0737f33dde89b368d130f2cfecb30b782
  break_split_unit_1.py
0855c66111d26a72968f1a3823f357c2f2a5ed3e86048836b402849756ebd5b3
  split_unit_1.stdout.txt (2326 bytes)
d346745d1793d4e1642fa774aefe681724787dfa0fbd339e7e2316b63363fd9b
  split_unit_1_break.stdout.txt (903 bytes)
```

## Status

The surviving core (after the audit): the logarithmic image of J carries
the single quadratic bit chi5 and the principal argument carries the
single phase pair; within the class 1 + mu_10, J is the unique Galois
orbit of units and realizes the minimal logarithmic quantum ln phi.
candidate-T at L1. Everything ontological is [D]; the completeness claim
is [H] with a named falsifier; no registry, frontier, or Canon edit is
proposed by this directory. PROMO deferred.
