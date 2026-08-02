# notes/C-COMMON-CARRIER-ICOSIAN-1

NON-CANONICAL. Incubation candidate, no authority, no Canon change, no
canon/ file touched. This directory is the durable git handoff of a
candidate developed 2026-08-02 in the project incubation lane against
Public Canon v30 (tag canon-v30, content commit
857223fcd5e7bc8c8e68f1df768d6e8222b24ee0). It continues the Herm2
analytic lane consolidated in notes/C-HERM2-BORN-CONE-1 and realizes its
probe proposal P-COMMON-CARRIER-ICOSIAN-1 at candidate level.

## Contents

```text
C-COMMON-CARRIER-ICOSIAN-1.md                    candidate claim and scope doc (rev 1)
README.md                                        this manifest
PREREG-C-COMMON-CARRIER-ICOSIAN-1_2026-08-02.md  frozen prereg (before the recorded run)
RESULT-C-COMMON-CARRIER-ICOSIAN-1_2026-08-02.md  recorded run and per-claim outcome
verify_common_carrier_icosian.py                 pinned verifier, 45 gates
break_common_carrier_icosian.py                  pinned break attempt, 6 gates
common_carrier_icosian.stdout.txt                committed stdout of the verifier
common_carrier_icosian_break.stdout.txt          committed stdout of the breaker
SHA256SUMS                                       hashes of the files above
```

## Reproduction

From this directory:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 verify_common_carrier_icosian.py
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 break_common_carrier_icosian.py
```

Expected: exit 0 and exit 0; stdout byte-identical to the two committed
stdout files. Recorded leg: x86_64 (Ubuntu 24.04.3 LTS, WSL2,
Python 3.12.3). One architecture only; these are incubation pins, not a
public probe, and the POLICY section 4 two-architecture gate is not
claimed.

## Frozen pins (recorded before the recorded run)

```text
b4335e452162a6c8fd7011debfdfdf808fbbb37b4431265b15bb7b2a148661c8
  PREREG-C-COMMON-CARRIER-ICOSIAN-1_2026-08-02.md
fd02057af557cbd61ed26983e486bfee023082cd40c72c20387f32508d63e016
  verify_common_carrier_icosian.py
7db04e4accd6a69ead7d02c73079e235f2da432f8f4d851c357eb8d2728667c5
  break_common_carrier_icosian.py
e83e5c494038b53be5236327b1c10a01a91307754c2813391306b31cdd560d91
  common_carrier_icosian.stdout.txt (7154 bytes)
956054a7e65ee8dcda7fbc74c054c592bb200be4aee0c997535f4ff069929a36
  common_carrier_icosian_break.stdout.txt (1073 bytes)
```

## Status

The surviving core is candidate-T: the icosian ring O carries the right
h-unitary 2I, the left K-action with J an h-similitude of multiplier
2 - phi, and both commute with no choices beyond the pinned q (unique up
to inner 2I and CM conjugation) and the canonical line K e. O is a free
rank-2 Z[zeta5]-module on {1, omega}, yet the h-orthogonal splitting is
glued with index 5 at the ramified prime p5; a diagonal operator along
the splitting preserves O exactly when its two slots agree mod p5. The
integral even tick is therefore the sign-twisted diag(J, -J^-1) with
coherence phase 1 - J, the registered tenth root; the untwisted det-1
tick and every fifth-root repair fail; the half tick has no F-rational
realization at all (total positivity), living over K(sqrt phi). The
golden-twisted trace form exhibits O as the E8 lattice, and the right
action in the free basis is GL2(K)-conjugate to the registered
COLOR-INTEGRAL-LIFT, with the class of q landing in the registered 5a
and the conjugation 3-space in the canon row 3a. Everything ontological
is [D]; the carrier-completeness claim is [H] with the named falsifier
F-ICO-3. PROMO deferred.
