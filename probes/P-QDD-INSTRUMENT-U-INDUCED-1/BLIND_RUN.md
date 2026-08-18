# Blind-breaker record

## Freeze

- Source: `blind_break.py`.
- SHA-256: `bae54c4df9b48bc28cb693ab70514fd91ec074181b7a1cc26e75203ecda000a6`.
- Bytes: 26103.
- Checker executions before freeze: 0.
- Checker imports before freeze: 0.
- Static validation before freeze: syntax-only compilation passed.
- Derivation input: `PREREG.md` only; no accepted verifier, expected output, run/result output, or other checker was inspected.

## Declared scope

The checker independently covers C1-C3, exact REAL-SINGLE/LONG/CENSUS, INFO, seed dependence, and orientation dependence. It intentionally omits induced post-object/family checks, accepted-verifier serialization hashes, and repository authority/pin gates.

## First actual execution

```text
C1 PASS generators relations commutators
C2-STRUCTURE PASS zero=25 classes=313 oriented=625
C3 S1-S2 PASS exhaustive_states=15625 drive_bits=2
S3_SELECTOR (0, (0, 0, 0, 0), (0, 0), (2, 0), 0, 2, (0, 0, 0, 0), (2, 1, 2, 1))
S3_DIRECT_C (0, (0, 0, 0, 0), (0, 2), (1, 1), 2, (2, 3, 2, 4), (2, 2, 2, 0))
CHANNEL-PASS
PHASE-A PASS target-free exact residue summaries
C2-TARGET PASS m-zero=25 occ-values=22
REAL-SINGLE count=0
REAL-SINGLE pairs=EMPTY
REAL-LONG count=0
REAL-LONG pairs=EMPTY
REAL-CENSUS count=0
REAL-CENSUS pairs=EMPTY
INFO count=150
NO-REALIZATION-W
LONG-NO-REALIZATION-W2
CENSUS-NO-REALIZATION-W
RECORD-W info=150
SEED-DEPENDENT-271350
ORIENTATION-DEPENDENT-22500
BREAKER-COMPLETE decisive-tags-and-C1-C3-only
BLIND_TIME wall=28.184 user=28.175 sys=0.008
```

The breaker prints the complete 150-member INFO list between `INFO count=150` and `NO-REALIZATION-W`; it is omitted above only to keep this run record readable. Its list is every nonempty proper subset for its canonical representative of the `q+r` functional, at all five delays, exactly matching the accepted verifier up to the checkers' different public labels for the same canonical functional.

Exit status: 0.

## Comparison

The accepted verifier and blind breaker agree exactly on their overlapping scientific predicates and counts. No discrepancy was found.
