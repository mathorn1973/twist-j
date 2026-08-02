# notes/C-CM-2I-QCARRIER-1

NON-CANONICAL. Incubation candidate, no authority, no Canon change, no
canon/ file touched. Durable git handoff of a candidate developed
2026-08-02 against Public Canon v30 (tag canon-v30, content commit
857223fcd5e7bc8c8e68f1df768d6e8222b24ee0). First exact slice of the
audit-proposed probe P-CM-2I-QCARRIER-1: the descent of the arithmetic
Galois C4 to the registered integral 2I lift, the invariant Gram and
its uniqueness.

## Contents

```text
C-CM-2I-QCARRIER-1.md                     candidate claim and scope doc (rev 1)
README.md                                 this manifest
PREREG-C-CM-2I-QCARRIER-1_2026-08-02.md   frozen prereg (before the recorded run)
RESULT-C-CM-2I-QCARRIER-1_2026-08-02.md   recorded run and per-claim outcome
verify_cm_2i_qcarrier.py                  pinned verifier, 10 gates
cm_2i_qcarrier.stdout.txt                 committed stdout of the verifier
SHA256SUMS                                hashes of the files above
```

## Reproduction

From this directory:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 verify_cm_2i_qcarrier.py
```

Expected: exit 0; stdout byte-identical to the committed stdout file
(SUMMARY 10/10 PASS). Recorded leg: x86_64 (Ubuntu 24.04.3 LTS, WSL2,
Python 3.12.3). One architecture only; incubation pins, not a public
probe; the POLICY section 4 two-architecture gate is not claimed.

## Frozen pins (recorded before the recorded run)

```text
937b79c2377f4dff4f014e942febac639533f7093b84bcf02c0502d77adc7cee
  PREREG-C-CM-2I-QCARRIER-1_2026-08-02.md
ee632df2af7e6e210770af6505b9bdb10991726f59ba13ca88dede8cdcfe53b2
  verify_cm_2i_qcarrier.py
ee7af3c974356d56b0ff20989507dab3d7ef482cbb661b44bfbd626bbc25bb60
  cm_2i_qcarrier.stdout.txt (3073 bytes)
```

## Status

The surviving core is candidate-T: the Galois branches of the
registered lift meet exactly in the geometric C4 {+-I, +-S}; the CM
involution descends to the single carrier with markings intact while
the quarter-turn descends only through the outer 5a <-> 5b swap -- the
descent subgroup with markings is exactly ker chi5, so the bit is the
marking obstruction of the arithmetic C4; the branch pair 2a + 2b is
fully C4-stable (Q-valued character); and the invariant Hermitian Gram
H0 is totally positive definite and unique up to an F-scalar
(machine-checked one-dimensionality), identifying the audit's
coordinate-free Gram with the canonical icosian form h of
C-COMMON-CARRIER-ICOSIAN-1. The kernel/coset reading as "the bit rides
the branch exchange" is [D]; the remaining probe obligations (explicit
semilinear order-4 operator on the pair, equivalence class list,
orbit-to-amplitude bridge) are [O]. PROMO deferred.
