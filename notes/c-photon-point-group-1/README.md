# C-PHOTON-POINT-GROUP-1, candidate package

NON-CANONICAL. Incubation-lane candidate material. No authority: it creates
no registry row, edits no canon file, and moves no status. This directory is
the durable handoff of one completed candidate run, packaged so that an
independent seat can audit or attack it without any private context.

```text
CANDIDATE   C-PHOTON-POINT-GROUP-1
SESSION     photon-point-group-2026-08-04 (one session, one candidate)
BASIS       Public Canon v36 ACTIVE, verified by fresh clone on the run day:
            TAG canon-v36,
            CONTENT_COMMIT df64035f6f0cadbeb17f539eaeec5d8d0f444515,
            CANON_SHA256 c8f50d0ce4686d7eedc11599a95debee15c71a2cf13c52c93c3f0605890fa2d5,
            175814 B, canon/SHA256SUMS 5 of 5 OK. This branch is cut from
            main head 470d958.
TARGET      the photon operator/symbol lane. The isotropy-6 obligation I0'
            (read the point group of the canonical step set before any
            symbol is expanded), closed at candidate grade for the carrier.
ORDER       preregistration frozen BEFORE first verifier execution;
            thresholds unmoved; every gate names and constructs a failing
            input (13 expected-fail demonstrations, all fired).
```

## Claim, with candidate labels

The canonical spatial carrier is the integer model of GATE-LIFT-KERNEL-Z
(frozen in the C-PHOTON-SPATIAL-SYMBOL-1 preregistration): the sum-zero
lattice in Z^4 with the divided Galois-trace Gram, equal to the A_3 root
lattice, isometric to FCC D_3; the step set is its 12 minimal vectors.

```text
candidate-T  the integral point group has order exactly 48 and equals
             { +-P_sigma }, i.e. S_4 x C_2 (full octahedral); element
             orders {1:1, 2:19, 3:8, 4:12, 6:8}; no element of order 5.
candidate-T  every isometry of D_3 is a signed permutation (axes-forced
             proof: the norm-4 shell is exactly {+-2 e_i}); nothing sits
             above the 48.
candidate-T  |O(F_5^3, Cartan mod 5)| = 240 with exactly 24 elements of
             order 5; the integral reduction is injective, index 5, and
             contains no order-5 element: no icosahedral subgroup lifts.
             Independently reconfirms the 240 / 48 / 24 counts of
             C-PHOTON-SPATIAL-SYMBOL-1 AMENDMENT 1.
candidate-T  degree-4 invariants have dimension exactly 2 (r^4 and
             x^4+y^4+z^4); octahedral fourth-order anisotropy is
             one-dimensional.
candidate-T  D_3 shells at norms (2,4,6,8): sizes (12,6,24,12),
             anisotropies a = (-4,+32,-72,-64); the fourth-order isotropy
             cone on the first three shells is w1 = 8 w2 - 18 w3, with
             positive witnesses (8,1,0), (0,9,4), (6,3,1) and no positive
             solution on shells {2,6} alone. The minimal-vector step set
             alone is anisotropic (deficit -4).
candidate-D  (conditional on GATE-LIFT-KERNEL-Z) the point group of the
             canonical spatial carrier and of its minimal-vector step set
             is FULL OCTAHEDRAL; the icosahedral branch is excluded
             integrally; the "neither" branch is excluded. The decoder's
             internal step set is not publicly derived; if it is a union
             of shells, the decision transfers verbatim (declared limit,
             preregistration field 4).
```

## Evidence grade

Verifier and self-break pass both ran on two architectures with
byte-identical stdout, exit 0, empty stderr, under
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`:
x86_64 (Python 3.11.15) and aarch64 (Ubuntu 24.04, Python 3.12.3). File
transfers between legs were hash-checked. This is candidate grade, not a
public probe: no public pin preceded execution and no issue lock exists.

## Files and pins (sha256)

```text
019887766014890fc6f1a4b79f0b541740921a0dd772846535b2d5cb2aa9014b  PREREG-C-PHOTON-POINT-GROUP-1_2026-08-04.md (10374 B, frozen first)
f32e70788b6c7a056eac50b6b6a744e59ee3ff6cc777d38267d5ffa72247a18a  verify_photon_point_group_1.py (14439 B)
dcad65a5cb750dffcf12c958c4c82b6b8006ed90cc65056efeec43568578087e  photon_point_group_1.stdout.txt (1085 B, both legs)
d54163920cfd740b3f59455e1a8d75d91c5be098e0a9e0f66caedccfd33b51ee  break_photon_point_group_1.py (9154 B)
a449e9a8bc99c222cf9fe8d458b4d4b146ab07dc30cfbd98e5d423559290ce42  photon_point_group_1_break.stdout.txt (804 B, both legs)
                                                                  RESULT-C-PHOTON-POINT-GROUP-1_2026-08-04.md (result record)
```

Rerun from this directory:
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 verify_photon_point_group_1.py`

## Owed before any public movement

```text
1  An independent adversarial breaker by a seat of the other model family,
   written without reading the verifier (preregistration is sufficient to
   derive what would falsify each gate). The in-package break pass is the
   builder's own and does not substitute.
2  A public lock issue for the lane (this seat cannot open issues).
3  An owner decision whether a PROMO / new registry row is wanted
   (working name PHOTON-CARRIER-POINT-GROUP; statement, falsifier and
   dependency edges are in the RESULT document). Until then this package
   carries no public weight.
```
