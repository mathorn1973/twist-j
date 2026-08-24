# RESULT. C-PHOTON-POINT-GROUP-1

```text
CANDIDATE   C-PHOTON-POINT-GROUP-1
SESSION     photon-point-group-2026-08-04
STATUS      CANDIDATE RESULT. All seven frozen gates hit their exact frozen
            statements; all thirteen expected-fail demonstrations fired;
            the self-break pass found no break. No authority. Incubation
            lane. Nothing here moves any public row.
CURRENCY    Public Canon v36 ACTIVE (fresh clone this session; pins in
            C-PHOTON-POINT-GROUP-1.md). Private line unreachable; v184 pin
            unverified.
ORDER       preregistration frozen BEFORE first verifier execution;
            thresholds unmoved; hand predictions in the prereg were then
            decided by the verifier, 7 of 7 as frozen.
```

## Pins

```text
PREREG   PREREG-C-PHOTON-POINT-GROUP-1_2026-08-04.md
         sha256 019887766014890fc6f1a4b79f0b541740921a0dd772846535b2d5cb2aa9014b
         10374 B, frozen before compute
VERIFIER verify_photon_point_group_1.py
         sha256 f32e70788b6c7a056eac50b6b6a744e59ee3ff6cc777d38267d5ffa72247a18a
         14439 B
V-STDOUT photon_point_group_1.stdout.txt
         sha256 dcad65a5cb750dffcf12c958c4c82b6b8006ed90cc65056efeec43568578087e
         1085 B, exit 0, stderr 0 B on BOTH legs
BREAKER  break_photon_point_group_1.py
         sha256 d54163920cfd740b3f59455e1a8d75d91c5be098e0a9e0f66caedccfd33b51ee
         9154 B
B-STDOUT photon_point_group_1_break.stdout.txt
         sha256 a449e9a8bc99c222cf9fe8d458b4d4b146ab07dc30cfbd98e5d423559290ce42
         804 B, exit 0, stderr 0 B on BOTH legs
LEGS     leg 1: x86_64, Python 3.11.15 (cloud sandbox)
         leg 2: aarch64, Ubuntu 24.04, Python 3.12.3 (fleet relay)
         file transfer hash-checked both times; verifier and breaker stdout
         BYTE-IDENTICAL across the two legs
ENV      LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

Two architectures and two CPython versions with byte-identical stdout is
the strongest evidence grade the candidate lane can record. It is still a
candidate record, not a public probe: no public pin, no public issue, no
fold.

## Results, with candidate labels

```text
G1  candidate-T  the integral point group of the canonical spatial carrier
                 (integer model L = ker(sum) in Z^4 with the divided Galois
                 Gram, equal to the A_3 root lattice) has order exactly 48
                 and equals { +-P_sigma : sigma in S_4 }, i.e. S_4 x C_2.
                 Exhaustive over all 1728 root triples.
G2  candidate-T  element-order multiset { 1:1, 2:19, 3:8, 4:12, 6:8 };
                 attained orders {1,2,3,4,6}; NO element of order 5.
G3  candidate-T  under the frozen isometry the group transports exactly
                 onto the 48 signed permutation matrices of Z^3, the
                 norm-4 shell of D_3 is exactly { +-2 e_i }, and the 12
                 roots map onto the 12 FCC minimal vectors. The breaker's
                 axes-forced argument closes the ceiling: EVERY isometry
                 of D_3 is a signed permutation, so nothing sits above
                 the 48. The "neither" branch is excluded.
G4  candidate-T  |O(F_5^3, Cartan mod 5)| = 240 with exactly 24 elements
                 of order 5; the reduction of the integral group is
                 injective, lands inside, has index 5, and contains no
                 order-5 element. No icosahedral subgroup lifts
                 integrally. This confirms, by an independent
                 construction, the 240 / 48 / 24 counts first reported in
                 C-PHOTON-SPATIAL-SYMBOL-1 AMENDMENT 1: agreement.
G5  candidate-T  the degree-4 invariant space of the transported group is
                 exactly 2-dimensional, spanned by r^4 and x^4+y^4+z^4
                 (projector rank and trace; breaker Molien route agrees).
                 Octahedral fourth-order anisotropy is one-dimensional.
G6  candidate-T  D_3 shells at norms (2,4,6,8): sizes (12,6,24,12),
                 anisotropies a = (-4, +32, -72, -64) in the frozen
                 convention; every single shell alone is anisotropic at
                 fourth order (the minimal-vector step set included:
                 a = -4 != 0).
G7  candidate-T  fourth-order isotropy cone on the first three shells:
                 -4 w1 + 32 w2 - 72 w3 = 0, i.e. w1 = 8 w2 - 18 w3.
                 Positive integer witnesses (8,1,0), (0,9,4), (6,3,1);
                 shells {norm 2, norm 6} alone admit no positive solution.
```

The branch decision, exactly as frozen, with its condition:

```text
candidate-D (conditional on GATE-LIFT-KERNEL-Z): the point group of the
canonical spatial carrier and of its minimal-vector step set is FULL
OCTAHEDRAL, S_4 x C_2 of order 48. The icosahedral branch is excluded
integrally (no order-5 element lifts); the "neither" branch is excluded
(the group is the full signed-permutation group, so M_2 = c I_3 is
automatic and the isotropy-6 audit's integrity check stays an integrity
check). Obligation I0' of the isotropy-6 audit is closed at candidate
grade for the carrier. The decoder's INTERNAL step set is not publicly
derived; if it is a union of shells, this decision transfers verbatim
(prereg field 4, declared limit).
```

## The break pass

Five independent code paths (B1 axes-forced proof, B2 literature order
formula against a row-condition enumeration, B3 Molien power sums, B4
harmonic identity, B5 second-basis enumeration), all PASS, no break; five
breaker demonstrations fired. The strongest item is B1: it is a proof
sketch with two machine-checked premises, and it excludes ANY 49th
isometry, including non-integer-matrix candidates that a basis-image
enumeration alone could not rule out. Under the working agreement this
self-break does not substitute for the cross-model breaker; that pass is
owed before any public movement (Claude built, a GPT seat breaks).

## What this feeds, and what it does not

Feeds: the successor symbol work may expand in the octahedral invariant
basis with no silent-basis risk (the isotropy-6 audit's I0' warning);
fourth-order isotropy of any shell-weight system on the canonical carrier
is ONE linear equation with frozen coefficients (-4, +32, -72); the
minimal-vector step set alone is exactly anisotropic with deficit -4, so
any single-shell photon transfer operator on this carrier fails
fourth-order isotropy, and the cheapest repairs are the frozen witnesses
(8,1,0) and (0,9,4). C-PHOTON-TIME-CHARACTERISTIC-1 remains gated on the
owner rulings R1 and R3 of the 2026-07-27 verdict and is NOT opened here.

Does not feed: no operator is derived, no weights are canonical (the cone
constrains, it does not select), no dispersion, no time, no continuum, no
physics. A comparison with the cubic-lattice cone of the isotropy-6 audit
is out of scope by prereg field 4 (different shells, conventions not
carried verbatim in the project).

## Promotion path, deliberately not packaged

A PROMO would propose one new public row (working name
PHOTON-CARRIER-POINT-GROUP), statement G1+G3+G4 with the conditional
clause, falsifier: an exhibited isometry of the carrier outside the 48,
or an integral order-5 element, or an invariant-quartic dimension other
than 2. Packaging is deferred: contract open decision 3 has five candidate
lanes parked and the owner has not ruled on additions. The material above
is complete enough that the PROMO is a copy job when wanted.

## Falsifier of this result

Any of G1 to G7 refuted by an exact recomputation; any pin above failing
to reproduce; a demonstrated dependence of the stdout on architecture or
Python version; or a public derivation of the internal step set that is
not a union of Aut-orbits (which narrows the candidate-D reading, not the
theorems).
