# RUN - C-OMEGA-GENERATIVE-GEOMETRY-N2

PUBLIC NON-CANONICAL candidate-C exact corroboration.
Owner #1247. Author: A. M. Thorn <thorn@twistj.com>.
No formal public-probe or Canon gate is claimed.

## Prospective custody

Source pin: a6be00cb11f9b521841250418a3daf4b69e8dbf3

All three files were pushed and publicly read back byte-for-byte before
scientific execution. Their SHA-256 hashes are:

- PREREG.md: 2ba04316a62e5b48950addb01c8f13bed31605b7d5313e1395688778556c9ee5
- generate.py: 8a93ea5bfe5ba8cae0d2e20e1735d2c9b5731ec3d0f6fad6ce58bb2def1c0ada
- verify.py: b37c800544b1a55dbde45942c204eefb4d1fae6bdf0e30bdf9710247a62d80d0

The source pin is unchanged. Both implementations hash-check their exact
inherited public sources; the event model also checks its Hodge anchor.

Command from the repository root:

    python3 notes/C-OMEGA-GENERATIVE-GEOMETRY-N2/verify.py

Environment: LC_ALL=C, TZ=UTC, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1. Standard library only.

## First reproduction

platform: Darwin
architecture: arm64
python: 3.13.13
pin: a6be00cb11f9b521841250418a3daf4b69e8dbf3
exit_code: 0
stdout_bytes: 682
stdout_sha256: dc5a89f02e464d6ea8acced2daeb60aac1b37d18c0b682ec73c826f851d68f9b
stderr_bytes: 0

## Second reproduction

platform: Linux
architecture: x86_64
python: 3.13.5
pin: a6be00cb11f9b521841250418a3daf4b69e8dbf3
checkout: clean detached public pin
exit_code: 0
stdout_bytes: 682
stdout_sha256: dc5a89f02e464d6ea8acced2daeb60aac1b37d18c0b682ec73c826f851d68f9b
stderr_bytes: 0

The second lane fetched the public branch and checked out the exact pin,
verified all three source hashes, then ran the same verifier. This is
same-code reproduction on two architectures, not independent confirmation.
Ordinary notes-only CI does not run this scientific audit and is not counted
as another reproduction lane. Universal claims rest on PROOF.md.

## Exact stdout on both architectures

```text
PASS G1: tagged hexagon/cube bijection; 729 exact pairs; signed shells r=0..8
PASS G2: 1715 native-prefix appends; connected immutable graphs; complete C_3 for five heads
PASS G3: 63 exact projected-metric controls at h=3,5,8; rational 5/9 and 13/9 bounds
PASS G4: 2450 exact field records on K_4 match independent sparse evolution; no boundary substitution
PASS G5: cubic spatial/quartic spacetime record counts and sharp batch completion costs
PASS G6: native selectors change partial order, not completed geometry; inequivalent metric controls 6 versus 2
NON-CANONICAL: generator and stable scalar continuation exist; native metric selection and physical memory are not supplied
```

## Predecessor disposition

The N predecessor was ABANDONED at static review before any scientific run,
with its original files preserved in PR #1246. N2 corrects only unsupported
Q5 exponentiation to multiplication before its own prospective pin. There
was no mathematical threshold, data-class or expected-result adjustment.
