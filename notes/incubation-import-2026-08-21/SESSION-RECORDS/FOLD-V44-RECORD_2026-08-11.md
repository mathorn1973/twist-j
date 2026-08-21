# FOLD RECORD, Public Canon v44, 2026-08-11

Status: ACTIVE. Tag canon-v44 published, post-activation readback PASS.
The arithmetic rapidity arc is public canon.

## Authority chain

```text
merge      PR 345, no squash, merge commit
           1417b533944e85106901079cc73ae7a0c3c42dc2
parents    3aff96e (prior main, probe PR 343 merged)
           89a3db3 (activation commit, exactly STATUS.md README.md
           CITATION.cff)
content    9da73b96613eb0d6f8d0ec17a5ada3ee6f511a4a
tag        canon-v44, annotated, on the merge commit, pushed only after
           the full pre-tag readback on main
CANON      sha256 c482aff6d0a01faab7fa8b92d2c485b39a8389f67ed99d79024a2878f35acd69
           211566 bytes, claims 237 (T 131, D 41, C 27, H 2, O 23, F 13)
release    issue 344 (closed at activation); claim lock issue 342 closed;
           stale v42 release claim issue 338 closed as administrative
```

## Rows registered

```text
ARITHMETIC-RAPIDITY-DECOMPOSITION            T   10. Relativity as counting
SPLIT-PRIME-RAPIDITY-CLASS                   T   10. Relativity as counting
SPLIT-PRIME-RAPIDITY-CONSTRUCTION-AGREEMENT  C   10. Relativity as counting
evidence: probes/P-ARITH-RAPIDITY-1
bundle:   e053d4950e368c7815f6df723b4dde316c6bb5a17d4f8d62f8fcee8eeb105fda
```

Owner row decision applied exactly: no ARITHMETIC-FRAME-READING row (an H
row requires a concrete falsifier and none is written) and no
PRIME-RAPIDITY-WEIL-BRIDGE row (a live frontier without an executed
program); both non-registrations are stated in the v44 changelog entry.

## Gates passed, in order

```text
pre-PR     builder applied on release/canon-v44; generate_canon_views
           idempotent; exactly one changelog marker pair; LEDGER PASS;
           POLICY PASS; STATUS LABELS PASS; status-separation witness
           extended to 30 of 30 and EXPECTED refreshed; architecture map
           test at 237/131/27/156/22; 99 tools tests; SHA256SUMS 5 of 5;
           check_activation --full ACTIVATION PASS before any tag
CI on PR   full sweep, all probes, both architectures, 10 m, success
post-merge readback on main repeated green, THEN the tag was created
post-tag   check_activation --full --post-activation --expected-tag
           canon-v44 ACTIVATION PASS; tag-triggered publication job
           success in 23 s
```

The v42 lesson held: every repairable check ran before the irreversible
tag, and the tag fired clean on the first attempt.

## Same-day arc, for the record

Incubation C-ARITH-RAPIDITY-1 to -4 (three integrity STOPs, one accepted
id, five-part breaker survived on two architectures), public probe
P-ARITH-RAPIDITY-1 (issue 342, PR 343, 26 of 26, byte-identical on four
legs), canon fold v44 (issue 344, PR 345, tag canon-v44). One day from
first freeze to active canon, with every gate passed in order and both
overclaims of the day dying by their own frozen rules before anything
touched the public line.

## Open next

The k4 third cut under the owner freeze in
claude/FREEZE-K4-THIRD-CUT_2026-08-11.md, now unblocked by the fold.
PRIME-RAPIDITY-WEIL-BRIDGE stays outside canon as probe-preregistration
interface material until a program exists to execute.
