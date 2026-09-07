# Public Canon v80 r3 reconciliation

**NON-CANONICAL / REVIEW INPUT / NO AUTHORITY.**

Issue #881. Basis public main `1ea039d5a488042cbc4d722cc7dc7b1d3f8d841e`,
ACTIVE Public Canon v79.

## Verdict

The unpublished candidate #874 remains mathematically usable but is stale as a
release candidate because public main advanced after its content pin. It must
not be rebased, amended or published. A fresh r3 content commit is required.

All three scientific rows proposed by #874 survive unchanged:

```text
U-NATIVE-COMMON-READY-SOURCE-RETENTION          [T]
QDD-INCIDENCE-FIRST-HIT-CLASSIFICATION          [T]
QDD-MIXED-CHANNEL-ATTENUATION-RIGIDITY          [T]
```

The later public work adds two compatible L4 theorems:

```text
A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS          [T]
QDD-SIMPLEX-PAIR-INCIDENCE                      [T]
```

The first prevents an overclaim: positivity and complete-frame additivity do
not prove that every rational A4 reading is quadratic. The second supplies the
positive structural result actually needed by the programme: the chosen
quadratic P/Q read is exactly a second-order integer Cartesian-pair census on
the regular-simplex relation, and its p=5 scale 20 is forced by the primitive
simplex ray and minimal universal integral lift.

There is no contradiction. Public reading-family discipline does not require a
unique global decoder. The revised v80 statement is therefore:

```text
quadratic reading is not forced to be the only mathematical reading;
quadratic reading nevertheless has an exact integer relational meaning as the
chosen second-order pair probe.
```

## Source audit

### Old v80 source

Unpublished PR #874:

```text
old base       a51df34fe1f1f433062faeb18f5e03fd0a8082b2
content        79f09fb50530ec2f39dc4be8e972038a04ef746c
release head   5e09ae379acd833846e3186dae1915e0eec3344b
old CANON sha  a6e9e7d3a30eff37cdc2d29796c5976f4b789ee4e5e56ee1ff977583491e13ee
old CANON bytes 535921
```

The old v80 full workflow passed on x86_64 and aarch64. Those bytes are source
material, not current authority.

### Reading nonuniqueness

Merged probe #876, `P-A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS-1`.
The public proof constructs the global rational A4 family
`w_t=1/4+tH`, proves exact frame normalization and positivity, and exhibits an
equal-projector cover with defect `3t`. It is theorem-grade L4 mathematics and
explicitly does not claim a physical realization of the alternative weights.

### Pair-incidence bridge

Attempt #877 is ABANDONED and earns no result. Its terminal record was merged by
#878. It is provenance only.

Fresh successor #879 / merged probe #880,
`P-QDD-SIMPLEX-PAIR-INCIDENCE-2`, completed the theorem under a new immutable
pin. The accepted local run reported 104768 exact assertions on 2560 contexts,
exit zero and empty stderr; GitHub x86_64 and aarch64 reproduced the same
committed output. Universal content rests on the written proof.

## Open-obligation audit

The two new results do not satisfy any existing positive or negative closure
condition of the three physical QDD owners.

`QDD-INSTRUMENT-APPARATUS [O]` remains open because pair incidence is a
mathematical relation census and the nonquadratic family is a mathematical
weight family. Neither supplies a physical effect id, apparatus carrier, ready
state, selected phase, physical context key, coupling, pointer, reduction,
realized event, occurrence law, sampling law, persistence/reset law or L1-to-L5
gate.

`QDD-INSTRUMENT-CLASS-COMPLETENESS [O]` remains open because neither theorem
classifies the complete target-independent physical apparatus family. Decoder
plurality is not apparatus-family completeness.

`QDD-TERMINAL-EVENT-SEMANTICS [O]` remains open because neither theorem gives an
independently justified law saying when one terminal event has physically
completed or why one branch rather than another is the realized record.

No L6 measure is added. No current H or O status changes.

## Ledger disposition

The r3 fold therefore adds exactly two T rows and no new dependency or gate:

```text
claims             398
T                   266
D                    45
C                    39
H                     2
O                    28
F                    18
live H/O             30
normative items     447
dependencies        744
evidence            398
history             931
gates                15
frontier programs     8
```

The two new claims use self-contained inline Canon proof as normative evidence;
the public two-architecture probes remain provenance and independent replay
surfaces. This keeps the status ceiling theorem-based rather than
computation-based.

No new dependency edge means the old v80 architecture-map expectation remains
exactly:

```text
direct architecture requires        182
transitive architecture dependents  258
dependency terminals                 61
```

## Required fresh fold

1. Start from current public main, not #874's branch head.
2. Transport the exact old-v80 content bytes from content commit `79f09fb...`
   for all unchanged old-v80 paths.
3. Apply `V80-R3-CANON-INSERT.md` at the frozen anchor before section 3.
4. Apply the exact registry/normative/evidence/history/status-count deltas from
   `V80-R3-FOLD-MANIFEST.md`.
5. Retain old v80 dependencies, frontier scheduler data and deterministic
   profile unchanged.
6. Update the v80 changelog paragraph and regenerate the five normative hashes.
7. Replace the old reconciliation with this r3 reconciliation.
8. Run policy, all tool tests, Canon, ledger, gate contract, generated views,
   architecture-map tests, status-separation and the full public
   probe/reproduction inventory.
9. Freeze one fresh content commit.
10. From that exact content commit, make one release-form commit changing only
    `STATUS.md`, `README.md`, `CITATION.cff`, with newly computed content SHA,
    Canon SHA-256 and byte count.
11. Open the reviewed v80 r3 PR. The old #874 may then be closed as superseded.

Tagging and release publication are outside #881 and require a separate owner
action after reviewed merge and public-main readback.
