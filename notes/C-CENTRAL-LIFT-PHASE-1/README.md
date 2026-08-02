# notes/C-CENTRAL-LIFT-PHASE-1

NON-CANONICAL. Incubation candidate, no authority, no Canon change, no
canon/ file touched. Durable git handoff of a candidate developed
2026-08-02 against Public Canon v30 (tag canon-v30, content commit
857223fcd5e7bc8c8e68f1df768d6e8222b24ee0). It promotes the algebraic
core of the accepted external audit of notes/C-HERM2-BORN-CONE-1 to
exact gates (branch pinning of arg J, projective fifth power, the cone
theorem, the square-root-free one tick, the Sym central phase, mu_5
versus mu_10, the tick-ladder integrality, the split-unit projectors,
the rigidity lever) and realizes the audit's proposed
P-CENTRAL-LIFT-PHASE-1 at candidate level.

## Contents

```text
C-CENTRAL-LIFT-PHASE-1.md                     candidate claim and scope doc (rev 1)
README.md                                     this manifest
PREREG-C-CENTRAL-LIFT-PHASE-1_2026-08-02.md   frozen prereg (before the recorded run)
RESULT-C-CENTRAL-LIFT-PHASE-1_2026-08-02.md   recorded run and per-claim outcome
verify_central_lift_phase.py                  pinned verifier, 16 gates
central_lift_phase.stdout.txt                 committed stdout of the verifier
SHA256SUMS                                    hashes of the files above
```

## Reproduction

From this directory:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 verify_central_lift_phase.py
```

Expected: exit 0; stdout byte-identical to the committed stdout file
(SUMMARY 16/16 PASS). Recorded leg: x86_64 (Ubuntu 24.04.3 LTS, WSL2,
Python 3.12.3). One architecture only; incubation pins, not a public
probe; the POLICY section 4 two-architecture gate is not claimed.

## Frozen pins (recorded before the recorded run)

```text
170eeb10718d3186a4ce54017e1df333bd6ba85e353bcbaf8d6c597dae447d40
  PREREG-C-CENTRAL-LIFT-PHASE-1_2026-08-02.md
e31b2ad0aa608c00db4fb863cd664f9731df57e3dbfb1ad1c1b0121eec8d9b58
  verify_central_lift_phase.py
82d5f8df5a0af26a02490664d5186e1f2f03e191cfacc076be7d720d94db9477
  central_lift_phase.stdout.txt (4299 bytes)
```

## Status

The surviving core is candidate-T: the branch of arg J is pinned by the
polarization J phi = zeta5, not by the cosine; the fifth power of the
spinor step is a pure boost only projectively (zeta10^5 = -1 exact);
the Born/causal cone equivalence is theorem-grade; one loxodromic tick
is realized square-root free by diag(J, 1) in the projective Herm
action while the Sym slot sees the central phase; the unit-scalar
central phase group is exactly mu_5 and the tenth-root glue phase 1 - J
escapes it by the central sign; and the tick ladder stands: half-tick
over K(sqrt phi), one tick K-projective only, two ticks integral
twisted, four untwisted, ten pure. The tick-counter reading is [D];
any U(1) identification is [H] and deferred. PROMO deferred.
