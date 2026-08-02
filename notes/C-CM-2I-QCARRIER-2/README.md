# notes/C-CM-2I-QCARRIER-2

NON-CANONICAL. Incubation candidate, no authority, no Canon change, no
canon/ file touched. Durable git handoff of a candidate developed
2026-08-02 against Public Canon v30 (tag canon-v30, content commit
857223fcd5e7bc8c8e68f1df768d6e8222b24ee0). Second slice of the
audit-proposed probe P-CM-2I-QCARRIER-1: the explicit semilinear
quarter-turn on the branch pair, its cocycle mu = -phi^2, and the
forced order-eight closure nu^4 = -1. Completes the constructive step
left open by notes/C-CM-2I-QCARRIER-1; a draft preregistration for the
future formal public probe is included.

## Contents

```text
C-CM-2I-QCARRIER-2.md                     candidate claim and scope doc (rev 1)
README.md                                 this manifest
PREREG-C-CM-2I-QCARRIER-2_2026-08-02.md   frozen prereg (before the recorded run)
RESULT-C-CM-2I-QCARRIER-2_2026-08-02.md   recorded run and per-claim outcome
P-CM-2I-QCARRIER-1_PREREG_DRAFT.md        draft prereg for the future formal probe
verify_cm_2i_qcarrier_2.py                pinned verifier, 11 gates
cm_2i_qcarrier_2.stdout.txt               committed stdout of the verifier
SHA256SUMS                                hashes of the files above
```

## Reproduction

From this directory:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 verify_cm_2i_qcarrier_2.py
```

Expected: exit 0; stdout byte-identical to the committed stdout file
(SUMMARY 11/11 PASS). Recorded leg: x86_64 (Ubuntu 24.04.3 LTS, WSL2,
Python 3.12.3). One architecture only; incubation pins, not a public
probe; the POLICY section 4 two-architecture gate is not claimed.

## Frozen pins (recorded before the recorded run)

```text
d724e885c67365ffb50699f00ef5d0e388f326c3e4611c95ecc903c67d8b78b0
  PREREG-C-CM-2I-QCARRIER-2_2026-08-02.md
07bc78c68dbc98662f2bfdd065bddf8b26641028a098b755b88318ee6ab2ab4b
  verify_cm_2i_qcarrier_2.py
84ec41562374ab4cb8f91a90314b3bec6aacd27e346366d01fe1f592c8682cde
  cm_2i_qcarrier_2.stdout.txt (2270 bytes)
```

## Status

The surviving core is candidate-T: every G-equivariant tau-semilinear
map on the branch pair has the antidiagonal Schur form; the sigma-
intertwiner line is unique and its cocycle is mu = -phi^2, totally
negative, so the quarter-turn can NEVER close at order four -- the
obstruction class is [-1] in F^x/N(K^x); with N(d) = phi^2 the explicit
nu closes at order eight (nu^4 = -1), swaps the branches, restricts to
the sigma-descent on nu^2, and transports the unique invariant Gram
with totally positive multipliers. The central sign is the same bit as
the order-8 antiunitary S lift, the tenth-root glue phase, and the
half-tick obstruction: vector level C4, spinor level C8, on both the
geometric and the arithmetic side. The ontological reading is [D]; the
formal probe registration is drafted, not executed. PROMO deferred.
