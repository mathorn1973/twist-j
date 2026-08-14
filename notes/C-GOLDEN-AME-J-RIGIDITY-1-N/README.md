# C-GOLDEN-AME-J-RIGIDITY-1-N

Status: **NON-CANONICAL INCUBATION**
Public lock: [issue #369](https://github.com/mathorn1973/twist-j/issues/369)
Branch: `notes/c-golden-ame-j-rigidity-1-n`

This package preregisters an exact arithmetic-rigidity test for the pinned
golden AME(4,6) tensor inside one deliberately narrow printed-gauge family.
The complete support, common `a/b/c` labels, and literal phase-exponent table
are frozen; only three positive real amplitudes and one unit phase vary.

The primary unsolved system is fixed before target computation:

```text
three ordered row-Gram systems FF* - I
then xy - 1
3,889 serialized records
383 nonzero coordinate records
SHA-256 09aac23466680ba762e363ad75845aa1535f4e8e32cee75ad41119f43cb16762
```

Column Grams are mandatory redundant audits, not extra generators.  The sole
saturation is by `alpha*beta*gamma*x*y`.  The strongest possible result is
`EXACT_J_RIGID_UP_TO_CONJUGATION`; resource exhaustion is `NO_VERDICT`.

Key documents:

- `PREREG.md` — normative family, equations, gates, controls, targets, and
  verdict grammar;
- `SOURCE_PINS.json` — machine-readable source, authority, serializer, and
  prior-review pins;
- `SOURCE.md` — human-readable source and provenance record;
- `FIREWALL.md` — audit checklist against hidden target insertion;
- `CAS_PLAN.md` and `CAS_ENVIRONMENT.md` — exact post-lock algebra plan and
  current tool availability; and
- construction/checking programs and their pinned pre-lock transcripts,
  including `PREREG_VERIFY_EXPECTED.txt`.

Before the public lock, no target Gröbner basis, saturation, radical,
elimination, branch classification, or expected-relation test was computed.
No outcome under this lock authorizes a Canon or Registry change, pull
request, release, or `PROMO.md`.

## Post-lock exact result

All frozen gates G0--G7 now pass. The scoped verdict is
`EXACT_J_RIGID_UP_TO_CONJUGATION`: inside the tied
three-amplitude/one-phase printed-gauge family, three-way unitarity leaves
exactly two positive solutions, exchanged by complex conjugation. This is
not a uniqueness statement for all AME(4,6) tensors or local-unitary orbits.

The primary replay is standard-library-only and relocatable. It combines:

1. the blind tracked Gröbner certificate and both ideal containments;
2. a second parser and a six-coordinate straight-line certificate;
3. exact real-root/sign classification and all six frozen targets;
4. NC0--NC5, construction B, known-point replay, and the column-Gram audit;
5. canonical result JSON and artifact cross-checks.

Start with `RESULT.md`, `RUN.md`, and `RESULT.json`. Run
`run_standardlib.sh` with the two pinned upstream files; its stdout must
match `EXPECTED_STANDARDLIB.txt` byte for byte. `independent_sympy.py` is an
optional exact discovery replay and is not required by the primary checker.
`SHA256SUMS.txt` pins the complete preregistration and result package.

Public Canon v46, the Registry, and all promotion surfaces remain unchanged.
