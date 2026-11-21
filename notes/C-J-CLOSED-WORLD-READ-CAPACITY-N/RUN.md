# First-run custody and execution record

**NON-CANONICAL, L1. Finite exact audit, candidate-C; no two-architecture scientific claim.**

## Immutable inputs

Definition/proof pin: `f48598b4c2e7c32423ca54f288be3ffbb5db3e73`.

Complete accepted scientific-code pin: `9b0406c3bf4ea2c9f8d9afe17596ea5308907713`.
The public commit and local worktree were byte-identical for every file below.
Public readback completed at 2026-10-23T11:10:29.066515+00:00.
No scientific program was executed or imported before that readback.
The historical draft-stage sentence in PROOF.md describes its preparation;
the proof bytes were subsequently frozen unchanged by the two pins.

| File at code pin | SHA-256 |
|---|---|
| PREREG.md | 33da6e2fc870a6006c0e71407c64e52028e01154212d88cdc10876be244a9802 |
| PROOF.md | 8aad28c0104c2059d3f2e5720760b5af47b65d4b354ca9a987a2ef313db7c9f9 |
| verify.py | 0d088a7bbb06f1b0b97680d71dc848f654d91ae7948777b7cb6a7cf062a9f230 |
| break.py | 73be1314555b44cda4b95a802a090fcd920b901bf2e25d3cfe9f22d3a74638c9 |
| BREAK_CONTRACT.md | 406640983a3cb10ff11f9472d4b7dba4aa1876f34b2dd189febb87e5354d337f |
| run_once.py | 643ba9179702a62b079a2c5b5814199feb2fd0d06dccf3f439b35424ef7eae77 |
| README.md | 2ee2ec942daa6ac78e181286064727125763373237969c29f103c50cebcaf81f |
| SOURCES.md | d33eddd2e1ea602f078128af788800d9a7254fccc8e003b145ebc8eff634d8d0 |
| STATIC_REVIEW.md | 1c7577e0ee414c36a14308e8357992590ef46d46888619982ac5dad17863b847 |

## First executions

Both programs ran once from the repository root, in parallel subprocesses
on Linux x86_64, Python 3.12.14 (Clang 22.1.3), using only the standard library.
Administrative capture used the pinned run_once.py, exclusive output creation,
PYTHONHASHSEED=0, LC_ALL=C and a 2400-second timeout per program.
Neither program used network, randomness or floating-point scientific arithmetic.
No rerun, repair, threshold change or imported shared implementation occurred.

| Program | UTC start | UTC end | Elapsed ns | Exit | Timeout |
|---|---|---|---:|---:|---|
| verify.py | 2026-10-23T11:10:38.303023+00:00 | 2026-10-23T11:10:39.822217+00:00 | 1519072143 | 0 | False |
| break.py | 2026-10-23T11:10:38.303895+00:00 | 2026-10-23T11:10:38.870331+00:00 | 566334098 | 0 | False |

Both stderr streams are empty. EXPECTED.txt and BREAK_EXPECTED.txt are the
unaltered first stdout bytes. The administrative timestamps are outside the
deterministic scientific stdout.

| Record | Bytes | SHA-256 |
|---|---:|---|
| EXPECTED.txt | 17241 | 327d81693491db6ea76aa3c7cb3edf60bea475edd4a6531f3297f4afc4e15360 |
| BREAK_EXPECTED.txt | 85710 | 88c9702586852f4f968ce905c1f6f874d647ffb37f9b18b536e49744e0472569 |
| STDERR.txt | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| BREAK_STDERR.txt | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

## Reproduction commands

From a clean checkout of the scientific code pin, run:

```sh
PYTHONHASHSEED=0 LC_ALL=C timeout 2400 python3 -u notes/C-J-CLOSED-WORLD-READ-CAPACITY-N/verify.py
PYTHONHASHSEED=0 LC_ALL=C timeout 2400 python3 -u notes/C-J-CLOSED-WORLD-READ-CAPACITY-N/break.py
```

The final notes commit adds the original outputs without changing either
program, proof or preregistration. From that commit, compare outputs with

```sh
python3 notes/C-J-CLOSED-WORLD-READ-CAPACITY-N/compare_outputs.py
```

compare_outputs.py was authored after observing both outputs. It is an
administrative normalization/comparison, not a frozen third verifier.
COMPARISON.json records its checked overlap. Different positive certificates
are allowed: their chosen common multiplicity c need not be minimal or equal.

## Disposition

All first-run scientific assertions passed, both exit codes are zero, and all
overlapping exact counts and decisions agree. The static source-visible review
and code-independent breaker have separately disclosed boundaries. Analytical
proofs are proposed candidate-T; these finite computations remain candidate-C.
Repository CI on both architectures does not execute arbitrary notes programs,
so green repository checks must not be reported as a two-architecture replay
of this candidate. No Canon, registry, probe or physical status changes.
