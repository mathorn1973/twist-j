# Exact run record

**NON-CANONICAL. First executions of the frozen candidate, 2026-10-29.**

Reservation: [#1830](https://github.com/mathorn1973/twist-j/issues/1830).
Pre-execution pin: `e54ce523eb2dbc0dae56b3d3773a375fc09a0191`.
Base: `a193e389fb1ddb0bdc89165b015c95a17eb1e425`.

The six candidate files were committed and pushed before either program was
executed. GitHub returned base64 file bytes at the exact pin for PREREG.md,
verify.py and break_check.py; all three matched the prepared bytes exactly.
Prior work consisted of analytical derivation, text review and syntax parsing.

## Frozen source custody

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 8598 | e1c04e126f7ea68953f93473b9678951092b318e59fcc1d05df3f1d4967baf3e |
| verify.py | 9758 | 58635d7a173ea02f503d2fc4a69fd93f3b57c611f68bdfd17e0b264da42e5c4a |
| break_check.py | 9434 | dd42d59b5ffce22be76303abc150ed60040d30567d6fe7b984ec3494137cc2ec |

Public Git blobs at readback were respectively
`d981dec4ac6e9d3649f820333b0495ee9e1f135e`,
`7dd68b7b750ecb2c72cf3acdc772fd7aa1940488`, and
`baf056bd49fdd82ce808dddb150b9b5edc920e59`.

## First execution environments

| System | Architecture | Python | First execution began, UTC | Materialization |
| --- | --- | --- | --- | --- |
| Linux | x86_64 | 3.12.14 | 2026-10-29 17:27:09 | Byte-matched local copies of the public pinned files; all source hashes rechecked before execution |
| Darwin | arm64 | 3.9.6 | 2026-10-29 17:27:11 | Clean Git worktree at the exact pin; commit, clean state and source hashes checked before execution |

The programs have no runtime source dependencies beyond their own bytes and
the Python standard library. Neither reads Canon or any local path at runtime.
Each environment ran verify.py followed by break_check.py. All four exits were
zero; all four stderr streams were empty. No retry or source correction was
needed after the pin. The per-program stdout bytes were compared directly,
not only by comparing hashes.

The environment settings were PYTHONHASHSEED=0, LC_ALL=C, TZ=UTC and
PYTHONDONTWRITEBYTECODE=1. No Python optimization flag was used.

Portable replay from a checkout of this note:

```sh
PYTHONHASHSEED=0 LC_ALL=C TZ=UTC PYTHONDONTWRITEBYTECODE=1 python3 notes/C-U-NATIVE-CONTROLLED-MEMORY-N/verify.py
PYTHONHASHSEED=0 LC_ALL=C TZ=UTC PYTHONDONTWRITEBYTECODE=1 python3 notes/C-U-NATIVE-CONTROLLED-MEMORY-N/break_check.py
```

## Exact outputs

| Program | Committed stdout | Bytes | SHA-256 | Cross-architecture result |
| --- | --- | ---: | --- | --- |
| verify.py | EXPECTED.txt | 602 | a033108badb9617625c07e234ca75b9d6cadc9e3c601c0fb31cc41b72d039ba7 | Byte-identical |
| break_check.py | BREAK_EXPECTED.txt | 464 | 8b9736290614726b795d72a14a4bc1b6ef332a771b112340cbd103804c08c959 | Byte-identical |

The empty stderr SHA-256 is
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
The programs have different output formats; agreement means that each
reproduces its own committed stdout across architectures, not that the two
programs print the same bytes.

## Review and acceptance limits

The two programs use different implementations: direct coordinate formulas
and explicit homogeneous matrices. They were written and reviewed by separate
agents within the same authoring session, with the proof and scope shared.
These are authoring-session cross-checks, not the project's independent
acceptance. Architecture agreement establishes reproducibility of these exact
audits, not a physical realization or an L1-to-L6 lift.

Repository CI is separate. Because this is under notes/, a green repository
check must not be described as automatically replaying these two scientific
programs. The scientific execution evidence is the exact record above.
