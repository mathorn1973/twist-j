# P-SPIN-LIFT-FORCED-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS

## Scientific decision

```text
DECISION NEGATIVE
N = 4
```

The preregistered hypothesis `N = 1` is false. On the complete finite
carrier, exact enumeration of every pair in `G x G` under the pinned
ruling constraints gives 240 admissible triples `(iota, R, S)`, falling
into exactly four D4 simultaneous-conjugacy classes, each of orbit size
60 with stabilizer size 2:

```text
CLASS 1 R=(0, 1, 4, 3) S=(0, 2, 2, 0)
CLASS 2 R=(0, 1, 4, 3) S=(0, 3, 3, 0)
CLASS 3 R=(0, 2, 2, 3) S=(0, 1, 4, 0)
CLASS 4 R=(0, 2, 2, 3) S=(0, 4, 1, 0)
```

The central-retwist pairing exchanges classes 1 and 2 and exchanges
classes 3 and 4: the retwisted candidate `(iota, R, zS)` is never jointly
conjugate to `(iota, R, S)`. The printed representatives show two
distinct `R` values, each carrying one retwist pair. The pinned
procedural witness is admissible and lies in class 1: the dicyclic lift
exists, and three further inequivalent lifts survive the same frozen
constraints.

The registered falsifier of `SPIN-LIFT-FORCED` fired as preregistered:
the obligation closes negatively at the declared scope. A fired
falsifier is first-class progress; the dead branch is archived, not
deleted, and no threshold moved after the pin.

All 17 audit gates pass: group order, unique involution, D5
presentation and associativity, kernel of the quotient, 120
monomorphisms enumerated with full membership consistency, entailment
gates A5 to A7 with zero failures, conjugation closure, orbit times
stabilizer equal to 120 for every class, retwist membership and
involution, and witness reconstruction.

## Scope

This result concerns exactly the pinned owner ruling: the marked ordered
loop-generator pair of `COLOR-RETURN-D5`, the cover
`pi : SL_2(F_5) -> PSL_2(F_5)`, membership A1 to A7 with the single
imported choice `R^5 = -I`, joint conjugation by the full `SL_2(F_5)`,
no identification of central retwists, and no quotient by base
relabeling. Under a coarser equivalence that identifies central retwists
or base relabelings the count would be a different question and, per the
ruling D6, a different probe ID. No physical uniqueness or continuum
statement is inferred from `N`.

The formal `aarch64` record and public GitHub `x86_64` check reproduce
`EXPECTED.txt` byte for byte and satisfy the two-architecture computation
gate for this exact finite result. The registry status move for
`SPIN-LIFT-FORCED` belongs to the future normative fold named in the pinned
ruling, section 3.2.

## Formal evidence

```text
preregistration pin: 9ab4434a0de598426b07780214803594f729c48f
PREREG.md SHA-256:   4a4448a933e1e8dcbaace09ce9ac2f1b74b887780ba006d1b1fee59ad1eef9ee
verifier SHA-256:    11cd0ca1d5bb5408a9debbd52c098258f6f270bbab45fac14b86a69951e6d196
formal run commit:   542d0c3821f95b13c4cb4dc130150b1931d7d536

aarch64 platform:    Ubuntu 24.04
aarch64 Python:      3.12.3
aarch64 exit code:   0
aarch64 stderr:      0 bytes

x86_64 workflow run: 29287670182
x86_64 workflow job: 86943953826
x86_64 platform:     Ubuntu 24.04.4
x86_64 Python:       3.12.13
x86_64 exit code:    0
x86_64 stderr:       0 bytes

stdout SHA-256:      8005fc1de1890a11f5e1d736c64a6796696aab87ae2ce6f41d6ac08fa1c5fb80
stdout bytes:        1125
stdout lines:        32
```

`EXPECTED.txt` is the exact formal stdout. `RUN.md` contains the neutral
local run record. Audit success and the negative scientific decision are
separate: exit zero certifies exact execution and integrity, while
`DECISION NEGATIVE` records the preregistered scientific branch.

The public repository pull-request workflow independently reran the pinned
verifier on GitHub `x86_64` with Python 3.12.13 and reproduced
`EXPECTED.txt` byte for byte. Policy, unit, Canon, ledger, verifier, and
minimal-reproduction stages all passed; publication-only activation stages
were correctly skipped. The formal `aarch64` record and public `x86_64`
reproduction therefore satisfy the two-architecture computation gate for
this finite negative result.
