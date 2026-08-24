# Incubation import, 2026-08-21

NON-CANONICAL. This directory carries incubation material: candidate documents,
preregistrations, verifiers, breakers, run records, audits and session records
that were held outside the repository. It changes no status, promotes nothing,
and edits no normative file. Nothing here is canon. Every document keeps the
status label it was written with, and a candidate label is not a canon label.

## Why this exists

The incubation surface these documents lived on was a convenience surface with
no pin and no history. Material that had already landed publicly was removed
there; what remained is the material with no public counterpart, and it was
carried in one place with no version control. This directory puts it under git
so it has a history, a hash and a reviewable diff. That is the whole purpose.
Promotion still runs through the public probe protocol, one probe at a time.

## Provenance and basis

```text
BASIS      Public Canon v59, tag canon-v59
           CONTENT_COMMIT 5da6b883defebd8edc470db1e2e7ebde095ef20a
           CANON_SHA256 7fdea700589a21303109dbb6c33fecd2d8243d0d09184ab9d471f0a59687f641
           CANON_BYTES 314310, canon/SHA256SUMS 5 of 5 OK
           tag and content commit both verified ancestors of main
INTERNAL   not consulted for this import. Nothing here rests on the v184 pin.
SELECTION  every lane was matched against the pinned public head by claim id
           AND by content. Anything already carried by a registry row, a probe
           directory or an existing notes directory was excluded and is not
           reproduced here.
```

## Sanitization

Thirteen documents mentioned machine nicknames or a private host. Those names
were replaced with neutral platform descriptions (Linux aarch64 leg, Linux
x86_64 leg, macOS arm64 leg) before staging, and one filename was renamed for
the same reason. No secrets, keys, environment files, private logs or binary
models are present. The staged tree was scanned twice, before and after.

## Collisions declared

```text
C-SPLIT-UNIT        an unmerged branch notes/c-split-unit-1 already exists.
                    The copy here is the incubation draft, not a second claim.
                    Resolve by content before either is folded.
C-TM-HANKEL-K4      adjacent to the landed TM-HANKEL K2 and K3 rows. K4 is
                    not landed and nothing here claims it is.
```

## What a reader should not conclude

No row here is stronger than its label. Several lanes carry a fired falsifier
or a stop record, which is first-class progress and is kept, not hidden. A
document living in this directory confers no status of any kind.

## Index

```text
   10  AUDIT-BELL
    8  AUDIT-LAMBDA-GRID
    9  AUDIT-PURE-RECORD
    8  AUDIT-QDD-TERMINALITY
   13  AUDIT-WIDDER-DEPTH
    2  BREAKER-MACKEY4
    2  C-CASIMIR-COEFFICIENT
    4  C-CENSUS-ERGODIC
    2  C-COLOR-MEASURE-DIM
    2  C-DMATTER-CENSUS
    2  C-FIB-MTC-J-LOCK
    1  C-FRONTIER-WELLPOSEDNESS
    2  C-IMPEDANCE-TOLL
    5  C-LI2-PENTAGON-BALANCE
    4  C-METRO-DIM-CRITERION
    9  C-PHOTON-POINT-GROUP
    2  C-PRIME-BOOLE
   13  C-PRIME-ORDER-READING
   12  C-QDD-ERASURE-LATTICE
   13  C-QDD-IDEMPOTENCE-DOMINATES-FORK
    4  C-QS-COUPLING
    4  C-RAY-PICK-KERNEL-374
    5  C-RG-FIXEDPOINT
   12  C-RH-HANKEL-HARD-EDGE
    4  C-RH-OFFCRITICAL-WITNESS
   15  C-RH-WEYL-CANONICAL
    9  C-SCALE-MINIMAL-FIELD
    4  C-SPLIT-UNIT
   36  C-TM-HANKEL-K4
    4  C-TM-WALSH-INERTIA
    4  C-WEIL-GRAM-TOWER
   10  CURVATURE-AND-GEOM
    4  MISC
    2  PAULI-CARRIER
    2  PROMO-J-LI
    4  RH-LANE-NOTES
   35  SESSION-RECORDS
-----
  281  files in 37 lanes
```
