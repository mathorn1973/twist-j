# notes/C-HERM2-BORN-CONE-1

NON-CANONICAL. Incubation candidate, no authority, no Canon change, no
canon/ file touched. This directory is the durable git landing of the
Herm2(C) analytic-attack consolidation developed 2026-08-02 in a
container session against Public Canon v30 (tag canon-v30, content
commit 857223fcd5e7bc8c8e68f1df768d6e8222b24ee0). The handover document
and its two verification artifacts are committed byte-identically to the
container originals; the hashes below equal the pins recorded inside the
handover itself.

## Contents

```text
C-HERM2-BORN-CONE-1.md                        candidate claim and scope doc (rev 1)
README.md                                     this manifest
HANDOVER-HERM2-ANALYTIC-ATTACK_2026-08-02.md  verbatim handover (Czech), primary document
herm2_consolidation_verify.py                 pinned verifier, 47 gates
herm2_consolidation_verify_stdout.txt         committed stdout of the verifier
SHA256SUMS                                    hashes of the files above
```

## Reproduction

From this directory:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 herm2_consolidation_verify.py
```

Expected: exit 0; stdout byte-identical to the committed stdout file
(SUMMARY 47/47 PASS). Recorded legs: container leg (Linux, python3
stdlib, per the handover) and an independent re-run this session on
x86_64 (Ubuntu 24.04.3 LTS, WSL2, Python 3.12.3), byte-identical stdout.
Both recorded legs are x86_64; the POLICY section 4 two-architecture
gate is NOT claimed. Incubation pins, not a public probe.

## Frozen pins (as recorded in the handover, verified on landing)

```text
6e0bd75b3ec062e0c295fa571913ee265ef1cc52c99123561b84a145f54d8f0b
  herm2_consolidation_verify.py (15944 bytes)
576f744d1b0a736d5428ef937d7ffaba921005d3e702729e4dbe72fbc6d6b220
  herm2_consolidation_verify_stdout.txt (3706 bytes)
```

## Status

The surviving core is candidate-T: the exact J algebra (arg J = 2 pi/5
with no numerics, J^5 = phi^-5 decided by 125 > 121), the Minkowski
determinant and the Born cone = causal cone equivalence, the Q(sqrt5)
boost data of the J-step, the rigidity theorem forcing Minkowski over
Euclid under the single J-boost, the unique A5 bracket, the Zolotarev
orientation bit, and the Galois-forced two-slot pair
(Psi Psi^dagger, Psi Psi^T). Everything ontological is [D]; mass =
non-collinearity and decoder completeness are [H] with named falsifiers;
the four hard points are recorded in the handover, and the common
carrier point is attacked at candidate level in
notes/C-COMMON-CARRIER-ICOSIAN-1. PROMO deferred.
