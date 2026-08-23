# REVIEW: C-JACOBI-PHASE-CROSS-1, bundle audit and canonical-h reanalysis

NON-CANONICAL. Notes lane. This document registers no claim, edits no
Canon file, and earns no public status. It is the originating session's
answer to continuation 3 of `notes/C-JACOBI-PHASE-CROSS-1/`, written by
the author of the NADHLED note of 2026-08-22 that the bundle names as its
origin.

```text
DATE          2026-08-23
REVIEWED      notes/C-JACOBI-PHASE-CROSS-1/ at commit f60850d
              (preregistration pin 2841517)
AUDIT         arithmetic SOUND, discipline SOUND; the bundle's own
              comparison falsifier FIRED (its H is not the canonical h)
              and is resolved here: the reanalysis under the canonical
              conjugation-invariant h confirms all three nulls
PLATFORM      Linux x86_64, single platform, non-formal
```

## 1. Bundle audit

Integrity: `SHA256SUMS` verifies 7 of 7 against the branch content. The
pin commit 2841517 contains the preregistration, both verifiers and the
selftest stdout before the single census execution. `RUN.md` discloses
one pre-pin correction (a composite anchor 29971 whose gates correctly
fired; the anchor list was fixed, no threshold moved) and an interpreter
witness (Python 3.9.6 against 3.13.13, byte-identical stdout, same
architecture, correctly labeled a non-gate).

The micro-selftest is stronger than the origin note asked: the ring
identity `J_p conj(J_p) = p` in `Z[zeta_5]` together with the abelian
Galois group gives `|sigma_a(J_p)|^2 = p` in all four embeddings at once,
never leaving integer arithmetic; gate S4 records the exact character
dependence `J(chi^a, chi^a) = sigma_a(J(chi, chi))`; gate S7 audits the
exact Re/Im machinery through `3 - phi = |1 - zeta|^2`.

Two findings, both already disclosed inside the bundle itself:

```text
F1  stale basis: the session gated against Public Canon v26 (the branch
    base is the v26 fold merge), while the live head is v61. The carrier
    [T] rows for the rapidity classes did not exist at v26, which is why
    the bundle had to reconstruct the modulus-side definitions.
F2  consequence of F1: the bundle's H is not the canonical half-class.
    H is the seam bit of the oriented eta in [0, L) under the
    r_p = min-root tie-break, and it flips under conjugation. The
    canonical h of the public carrier rows is conjugation invariant:
    h = [t > L/4] with t = min(eta, L - eta), realized exactly by the
    octant machinery of the reduced generator (h = 1 iff the octant of
    theta lies in {2, 3, 4, 5}, with the conjugate law o + o' = 7). The
    bundle discovered the mismatch's fingerprint on its own: the entire
    skew of its rapidity marginals lives in the tie-break, and the
    conjugation folding {0,3} against {1,2} = 395 against 413 removes it.
```

The bundle's frozen comparison falsifier reads: if the originating
session used a different h, every table must be recomputed. The
originating session did use a different h, so that falsifier has fired.
The recomputation follows.

## 2. Reanalysis under the canonical h, independent code path

```text
verifier   verify_jacobi_cross_canonical_h.py
           sha256 9639e83c41d604048fe8b5a59d1d0c38f6e3555b07240323ad00f11d5482aa2d
stdout     REANALYSIS-STDOUT.txt
           sha256 8b18f9ad0600e456c94a103394cd60601cba6eaf32953d983df3fa4effa87d13
           exit 0, stderr empty, 2 s
surface    the bundle's frozen phase convention (least primitive root,
           QUAD, SGN) and its frozen lines 11345/1000, 9210/1000,
           21666/1000 with the 1/1000 band; the modulus side canonical:
           deterministic Tonelli root, Lagrange-Gauss shortest
           generator, exact octants by g^16 against p^8 phi^(2j),
           conjugate law asserted per prime, h = [o in {2,3,4,5}],
           arc = min(o, 7 - o), both class functions with no tie-break
independence a different Jacobi implementation (exponent counts reduced
           mod Phi_5), a different modulus engine (the bundle: min-root
           ideal with the A2 phi-ladder; here: Tonelli ideal with
           octants), a different author
```

Cross-check gates against the bundle's pinned stdout, all MATCH:

```text
X1  QUAD marginal (224, 205, 192, 187)   MATCH
X2  SGN marginal  (193, 407, 208)        MATCH
X3  h marginal    (395, 413)             MATCH (equals the bundle's
                                          invariant refold)
X4  T1' table == the {0,3}/{1,2} collapse of the bundle's T3,
    cell by cell                          MATCH
```

Two fully independent code paths agree on the data; each implementation
confirms the other. The value of T1' was predicted from the bundle's
published T3 table before this run (4.76) and is reproduced.

Results in the canonical frame at the bundle's frozen lines:

```text
test   table         X^2 exact                      witness   decision
T1'    QUAD x h      625146097522/131329384725      4.760     NOT-REJECTED
T2'    SGN  x h      122189168952/166587426005      0.733     NOT-REJECTED
T3'    QUAD x arc    1887412483923/174845014960     10.795    NOT-REJECTED
```

The arc marginal (193, 202, 202, 211) is flat: the canonical frame is
clean, confirming the bundle's own diagnosis that the marginal skew was
a pure tie-break artifact.

## 3. What this answers

The cross of the two integer avatars is constructible and exactly
computable; the selftest anchors the phase engine by a theorem (the
rapidity vector of `J_p` is zero); and the first crossing, now in the
convention-free frame, finds no measurable coupling between the angular
datum of the phase avatar and the rapidity datum of the modulus avatar
at 3 x 10^4: three nulls, two authors, two code paths. A REJECT would
have been a frame-shaking discovery; the null is the calibration the
frame predicts. No RH, L-function, Weil-positivity or physical statement
is made or implied in either direction.

## 4. Recommendations

```text
1  the bundle's continuation 1 (the min-root tie-break bias) stays with
   its author; it is the one genuinely new question the run surfaced
2  the bundle's continuation 2 (carrier to 10^6) is the real next test;
   recommended only after adopting the canonical h, so that a public
   probe stands on the v61 carrier rows rather than on a reconstruction
3  the bundle's continuation 3 is resolved by this note
```
