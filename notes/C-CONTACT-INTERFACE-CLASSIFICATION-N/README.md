# C-CONTACT-INTERFACE-CLASSIFICATION-N

NON-CANONICAL. No Canon authority. L1 retrospective algebraic classification.

Owner: A. M. Thorn / contact-interface-classification-20261006.
Reservation: [#1396](https://github.com/mathorn1973/twist-j/issues/1396).
Basis: Public Canon v100, `807dae3fe97dd6a872d5d1305a0133e8e8d856ea`.

The frozen [PREREG.md](PREREG.md) asks which complete contact laws and
pointwise reference-table implementations follow from an explicit extension
of the supplied v100 interface class. The control class does not require
identity at h=0. All reversible controls are admitted; involutions are a
marked subclass. The reader class likewise marks involutive couplings inside
all three-state pointwise permutations.

## Result

The conditional classification and its independent exact audit are complete.
There are 4608 full reversible controls, including 600 involutions, and
exactly four complete contact laws. The supplied W_b realizes one of them.
There are 30 admitted reader tables, including five pointwise involutive
tables, with five complete occupied-reference endpoint maps. All reader
tables lie in one orbit under the explicitly frozen q translations and
internal reference relabelings. These different equalities are kept separate.

The proof has an independent analytical derivation and a separate exact
review. Both independently frozen programs passed on their first runs,
with exit 0, empty stderr and identical 571-byte stdout. Both runs used
Ubuntu 24.04.3 LTS, x86_64, CPython 3.12.14. This is one-architecture
evidence, not the public scientific two-architecture gate.

The class and known v100 witnesses are declared, retrospectively motivated
inputs. No physical or native admission, L5 target search, occurrence law,
new reference minimum or Canon closure is claimed. The source
CONTACT-RECORD theorem and the live native-contact owner remain unchanged.

## Package

| File | Purpose |
|---|---|
| [PREREG.md](PREREG.md) | Immutable membership classes, comparisons, execution rules and ceilings |
| [PROOF.md](PROOF.md) | Complete-carrier proof, counts, all laws, reader fibres and inverses |
| [PROOF-CHECK.md](PROOF-CHECK.md) | Independently derived argument before reading the primary proof |
| [REVIEW.md](REVIEW.md) | Review of the exact original and corrected proof pins |
| [verify.py](verify.py) | Orbit-constructed controls and Cartesian reference-table census |
| [break.py](break.py) | Independently frozen raw-table controls and ready-column reader census |
| [EXPECTED.txt](EXPECTED.txt) | Exact common first-run stdout |
| [RUN.md](RUN.md) | Pins, first-execution custody, environment and timing |
| [RESULT.md](RESULT.md) | Scientific result, evidence types and remaining choices |
| [PROMO-C-CONTACT-INTERFACE-CLASSIFICATION-N.md](PROMO-C-CONTACT-INTERFACE-CLASSIFICATION-N.md) | Proposed disposition and obligations for any later public promotion |
| [CHECKS.md](CHECKS.md) | Local repository checks and delivery status |

## Replay

From a clean checkout of the pinned code or an unchanged descendant, run
each command separately. The real timeout is part of the preregistration.
The two programs import no repository verifiers and require only Python's
standard library. Replay was executed with CPython 3.12.14.

```sh
timeout 180s env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 -I notes/C-CONTACT-INTERFACE-CLASSIFICATION-N/verify.py
timeout 180s env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 -I notes/C-CONTACT-INTERFACE-CLASSIFICATION-N/break.py
```

Each successful stdout must match EXPECTED.txt byte for byte. A later
replay is not an additional architecture unless its actual environment
establishes that fact. Ordinary notes pull-request jobs do not execute
these two scientific programs.
