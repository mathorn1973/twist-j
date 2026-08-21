# PREREG C-PHOTON-POINT-GROUP-1

```text
CANDIDATE   C-PHOTON-POINT-GROUP-1
SESSION     photon-point-group-2026-08-04
STATUS      CANDIDATE PREREGISTRATION. No authority. Incubation lane.
FROZEN      2026-08-04, before any verifier execution. SHA-256 of this file
            is recorded in the session record and in the RESULT document.
            Hand derivations preceding this freeze are predictions; the
            verifier decides them. No data are opened before this freeze
            (there are no external data; every object below is generated
            by the frozen definitions).
CURRENCY    Public Canon v36 ACTIVE (pins in C-PHOTON-POINT-GROUP-1.md,
            verified by fresh clone this session). Private line
            unreachable; v184 pin unverified.
```

## Frozen field 1: equations (the claims G1 to G7)

Objects, fixed exactly:

```text
L        = { x in Z^4 : x1 + x2 + x3 + x4 = 0 }, the integer model of the
           canonical spatial carrier (GATE-LIFT-KERNEL-Z, cited from the
           frozen PREREG-C-PHOTON-SPATIAL-SYMBOL-1; a declaration, not a
           derivation; every claim below is a theorem about L).
q        = the standard dot product of Z^4 restricted to L. In the frozen
           basis b1 = e1 - e2, b2 = e2 - e3, b3 = e3 - e4 its Gram is the
           A_3 Cartan matrix [[2,-1,0],[-1,2,-1],[0,-1,2]] (gate C1 of the
           cited prereg).
R        = the 12 vectors of L with q(v, v) = 2 (the roots). STEP SET :=
           R. Under the frozen isometry T (columns f1 = (1,-1,0),
           f2 = (0,1,-1), f3 = (-1,-1,0); gate C2 of the cited prereg)
           the step set is the 12 minimal vectors of D_3 =
           { y in Z^3 : y1 + y2 + y3 even }, the FCC lattice.
Aut      = { g in GL(L) : q(g x, g y) = q(x, y) for all x, y }, the
           integral point group.
red_5    = entrywise reduction of basis matrices mod 5, landing in
           O(F_5^3, A mod 5), A the Cartan matrix.
a(S)     = sum_{v in S} v_x^4  -  3 sum_{v in S} v_x^2 v_y^2, the frozen
           fourth-order anisotropy functional of a finite set S in Z^3,
           evaluated in the D_3 picture. For signed-permutation-invariant
           S this is coordinate-choice independent; the verifier checks
           that independence on every shell it uses.
Shell(N) = { y in D_3 : y . y = N }.
```

The claims. Each is falsified by its exact negation; every gate names its
failing input in field 5 (the gate design rule of the working agreement).

```text
G1  |Aut| = 48, and Aut = { restriction to L of eps P_sigma :
    eps in {+1,-1}, sigma in S_4 } exactly, where P_sigma permutes the
    coordinates of Z^4. Enumeration is exhaustive over all triples of
    root images with Cartan Gram.
G2  The element-order multiset of Aut is exactly
    { 1:1, 2:19, 3:8, 4:12, 6:8 }. In particular no element of order 5,
    and the attained order set is {1, 2, 3, 4, 6}.
G3  D_3 transport. (i) Shell(4) = { +-2 e_i } exactly (6 vectors).
    (ii) The transported group T Aut T^-1 equals, as a set of matrices,
    the 48 signed 3 x 3 permutation matrices. (iii) Consequence, proved
    by the breaker as the axes-forced argument: every dot-product
    isometry of D_3 is a signed permutation matrix, so Aut is the FULL
    point group, with nothing above it.
G4  Mod 5. (i) |O(F_5^3, A mod 5)| = 240. (ii) Exactly 24 elements of
    order 5. (iii) red_5 restricted to Aut is injective; the image has
    order 48, index 5. (iv) No element of order 5 lies in the image.
    Consequence: no icosahedral subgroup of the finite orthogonal group
    (every such subgroup contains order-5 elements) lifts integrally.
    This recomputes, by an independent construction, the counts first
    reported in C-PHOTON-SPATIAL-SYMBOL-1 AMENDMENT 1.
G5  The space of degree-4 polynomial invariants of the transported group
    on Q[x, y, z] has dimension exactly 2, and contains r^4 = (x^2 + y^2
    + z^2)^2 and m4 = x^4 + y^4 + z^4 (which are linearly independent).
    Octahedral anisotropy at fourth order is therefore one-dimensional.
G6  Shell data of D_3, norms 2, 4, 6, 8: sizes (12, 6, 24, 12);
    anisotropies a = (-4, +32, -72, -64); every one of the four shells
    alone fails fourth-order isotropy (a != 0).
G7  The fourth-order isotropy cone on the first three shells is
    -4 w1 + 32 w2 - 72 w3 = 0, equivalently w1 = 8 w2 - 18 w3.
    Frozen witnesses: positive integer solutions (8, 1, 0) and (0, 9, 4)
    exist (two shells suffice on this carrier, in two distinct ways);
    (6, 3, 1) is a positive all-three-shell solution; shells {2, 6}
    alone (w2 = 0) admit NO positive solution.
```

Branch decision carried by G1 to G4, stated with its condition: the point
group of the canonical spatial carrier and of its minimal-vector step set
is FULL OCTAHEDRAL (S_4 x C_2, order 48), CONDITIONAL on
GATE-LIFT-KERNEL-Z; the icosahedral branch is excluded integrally; the
"neither" branch is excluded. No unconditional claim about the decoder's
internal step set is made (field 4).

## Frozen field 2: code

```text
verify_photon_point_group_1.py   Python 3, standard library only.
    Integer and Fraction arithmetic; NO float in any assertion or any
    printed value. Deterministic output: all enumerations sorted, no
    timestamps, no environment echo in stdout (stdout must be
    byte-identical across architectures). Runtime target far under 120 s.
    Environment for every formal run:
    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
    Structure: gates G1 to G7 printed as PASS or FAIL with exact data,
    then a separate EXPECTED-FAIL demonstration block (field 5), then a
    summary line. Exit 0 iff all gates PASS and all demonstrations fire.
break_photon_point_group_1.py    independent code paths, no import of and
    no code shared with the verifier: the axes-forced proof path (B1),
    the literature order formula 2q(q^2 - 1) as cross-check (B2), the
    Molien / power-sum route to the invariant dimension (B3), the
    harmonic identity a(S) = (5 M_xxxx - |S| N^2) / 2 (B4), and a
    second, basis-independent enumeration of the D_3 point group from a
    different frozen basis (B5).
```

## Frozen field 3: carrier / data

No external data. The enumerated objects and their frozen bounds: the 12
roots of L; all triples of roots (12^3 = 1728) for G1; the 48 candidate
matrices eps P_sigma; O(F_5^3, A mod 5) enumerated column by column over
F_5^3 (at most 125^3 candidate triples, pruned by the Gram conditions);
the 15 degree-4 monomials in 3 variables for G5; D_3 vectors in the box
[-3, 3]^3 filtered to norm <= 8 for G6 and G7; integer weight triples in
[0, 40]^3 for the G7 witness and non-existence searches. Bounds are frozen
now and do not move.

## Frozen field 4: systematics (declared limits and risks)

```text
1  GATE-LIFT-KERNEL-Z is a declaration, cited, not re-derived. Every
   claim is about the integer model L. If the lift is ever replaced, the
   branch decision must be re-read; G1 to G7 stand as mathematics.
2  STEP SET reading. This candidate identifies "the canonical step set"
   with the minimal-vector shell of the canonical carrier. That is a
   candidate hypothesis for the I0' reading, not a public fact: the
   decoder's internal step set is not publicly derived. If the internal
   step set is a union of Aut-orbits (shells), the branch conclusion
   transfers verbatim; if it breaks shell symmetry, G1 to G5 still give
   the ambient bound and the I0' reading narrows. This session cannot
   see the internal line and says so.
3  Overlap. G4 confirms or refutes counts first computed in AMENDMENT 1
   of C-PHOTON-SPATIAL-SYMBOL-1 by a different construction. No code or
   code path from that amendment is reused or was read.
4  Independence. Verifier and breaker are same-author (one session);
   under the working agreement this is the incubation self-break only.
   A cross-model breaker is owed before any public movement.
5  Convention. a(S) is THIS candidate's frozen fourth-order convention.
   No coefficient-level comparison with the cubic cone of the isotropy-6
   audit (w1 = 2 w2 + 8 w3, cubic shells, its own convention) is claimed
   in either direction; that comparison is out of scope.
6  Architectures. The local leg is x86_64; a second leg on aarch64
   (Ubuntu 24.04, Python 3.12.3) is attempted through the fleet relay
   with byte-identical stdout required. If only one leg completes, every
   computational grade here stays single-architecture candidate grade.
```

## Frozen field 5: failure thresholds and the gate design rule

Any gate's exact negation fires candidate-F for that claim; a fired gate
is archived, never deleted; no threshold or bound moves after this freeze.
Named failing inputs, each CONSTRUCTED and demonstrated in the verifier's
EXPECTED-FAIL block (a demonstration that does not fire is itself a FAIL):

```text
G1  a root triple with a wrong Gram (images b1 -> e1-e2, b2 -> e2-e3,
    b3 -> e1-e3): the extension is not an isometry; the enumeration
    filter must reject it.
G2  the order-multiset check run on Aut plus one injected matrix of
    order 5 (an explicit order-5 element of O(F_5^3) lifted naively to
    Z with entries in {0,...,4}): the multiset comparison must fail.
G3  the Shell(4)-equals-axes check run on Shell(2): 12 vectors, none of
    the form +-2 e_i; the check must fail.
G4  the no-order-5-in-image check run on the full O(F_5^3, A mod 5):
    it contains order-5 elements; the check must fail there.
G5  the dimension-2 check run for the cyclic subgroup generated by one
    fourfold rotation: its degree-4 invariant space is larger than 2;
    the check must fail.
G6  the anisotropy comparison run against a deliberately wrong table
    (a(Shell(2)) claimed 0): must fail. The coordinate-independence
    check run on the non-invariant set {(1,0,0)}: must fail.
G7  the cone membership check run on weights (1, 1, 1): value -44, not
    0; must fail.
```

## Frozen field 6: action layer

L2 (manifold and symbol infrastructure), with the single cited lift
GATE-LIFT-KERNEL-Z, frozen elsewhere and not re-declared here. No L5
stream, no L6 measure, no time transfer, no dispersion, no continuum
limit, no SI claim, no physical photon claim. The branch decision feeds
the successor operator work (symbol expansion, then the L5
characteristic); it does not perform any of it.
