# PREREG-BREAKER-MACKEY4-1

The independent breaker gate of candidate C-ENTROPY-MACKEY-OBSTRUCTION-4-N.

```text
STATUS:        NON-CANONICAL PREREGISTRATION, BREAKER LANE
AUTHORITY:     NONE
CLAIMED GATE:  the independent breaker required by
               notes/entropy_selection/PREREG-C-ENTROPY-MACKEY-OBSTRUCTION-4-N.md
               (recon branch) and by MACKEY4-PRIMARY-RESULT.md
SESSION:       M2 breaker session, Cowork claude-fable-5, 2026-07-30.
               A separate named session from the primary owner session.
OPENED:        2026-07-30
PUBLIC BASIS:  Public Canon v28
MAIN:          3161cbc764f547c95a80c3bd5028acf71c2ef524
TAG:           canon-v28
CONTENT:       86a046007f89a64a696d013112a44f02e624dd2e
CANON SHA:     4b720846ccd42c7ec808ab2acb21793962390b074bb3799d28c0f16c00165d2c
RECON BRANCH:  origin/notes/entropy-selection-recon at 9b69881
INTENDED CODE: mackey4_break.py (authored after this freeze)
CEILING:       candidate-C at best; this session runs ONE platform only.
               The breaker gate itself decides AGREE or DISAGREE, not status.
COMPUTATION UNDER THIS PREREG BEFORE FREEZE: NONE
```

## Independence declaration, falsifier first

This breaker is falsified as an independent gate if any of the following is
shown: the author session read or imported `mackey4_verify.py` or its stdout
or its RUN record; the breaker reuses the primary lambda-digit source
presentation; or the comparison values below were altered after this freeze.

Files from `notes/entropy_selection/` read by this session before this
freeze, listed exhaustively:

```text
READ      PREREG-C-ENTROPY-MACKEY-OBSTRUCTION-4-N.md   (the frozen claim spec)
READ      MACKEY4-PRIMARY-RESULT.md                     (the claims to test)
READ      RECON-V28-STATUS.md                           (lane status and scope)
NOT READ  mackey4_verify.py                             (forbidden, and stays so)
NOT READ  mackey4_primary.stdout.txt
NOT READ  MACKEY4-PRIMARY-RUN.md
NOT READ  every other file in notes/entropy_selection/, including README.md,
          tower.py, and all horizon and solver code
```

Public normative sources used: canon/CANON.md section 2 and section 3 of the
v28 clone (autonomous update, selector law, the five involutive generators
with constants s_c, u_c, c_d, v_e), canon/REGISTRY.tsv rows including
COLOR-TORSOR-HOLONOMY [T], ENTROPY-LIVING-SET [C], ENTROPY-MIRROR-LAW [C],
ENTROPY-COUNT-MATCH [C]. These are the public claim surface, not the primary
implementation.

## Field 1. Equation and decision surface

The breaker recomputes, by an independent route, every load-bearing finite
object of the Mackey obstruction and compares against the frozen expected
values E1 to E13 below. AGREE on all load-bearing values confirms the primary
route; DISAGREE on any one is a first-class result to be preserved, never
reconciled by editing either side.

### Source route (distinct presentation, as the candidate prereg requires)

Z[zeta_5] as Z^4 with basis (1, z, z^2, z^3), z^4 = -(1+z+z^2+z^3).
lambda = 1 - z. The ideal L = lambda^5 Z[zeta_5] as the column lattice of the
4x4 integer matrix A with columns lambda^5 z^i. Smith normal form
U A V = D by an own integer implementation; quotient coordinates x -> Ux mod
diag(D); action of J = 1 + z^2 through the conjugated integer matrix
W = U M_J U^-1 taken mod the invariant factors. No lambda-digit arithmetic
anywhere.

### Target route (from the public generator definitions only)

The five involutions a, b, c, d, e on F_5^6 implemented from the canon
section 3 table; branch maps F_t(x) = g_(z_6(x) + 2t mod 5)(x); the recurrent
core NOT by the census warmup protocol but by an exact certified route:
iterate the full-space image along Thue-Morse bits until the image size
stabilizes, then prove stabilization by the closure certificate
F_t(H_s) = H_t bijectively for all four (s,t), which makes R = H_0 union H_1
exact without any window heuristic. Components by union-find on the two
branch edges. Per generic component, the return group on the H_0 half is
generated dynamics-natively:

```text
s  := F_0 restricted to the H_0 half            (own-half mirror)
s' := (F_0|H_1) o (F_1|H_1) o (F_1|H_0)         (pullback of the H_1 mirror)
r  := s o s'
```

Expected: s, s' involutions, ord(r) = 5, G = <s, s'> regular of order 10 on
the 10-point half. Torsor coordinates by the lexicographically minimal
basepoint x_0 and transported basepoint c(x_0) on the H_1 half. In these
coordinates the four one-tick edge maps (previous half, current bit) are, by
construction, left translations; the nontautological content is the
uniformity of the marked presentation across all 312 generic components and
its singlet compatibility, which is exactly the common-cocycle statement in
this reconstruction.

### Frozen expected values

Load-bearing. Any mismatch is DISAGREE.

```text
E1   SNF invariant factors of L exactly (5, 5, 5, 25); |Z^4/L| = 3125;
     additive type Z/25 + (Z/5)^3.
E2   J cycle type on the quotient exactly {1: 1, 4: 1, 20: 156}; the unique
     fixed class is 0; the permutation order is 20.
E3   Dyadic product component counts equal gcd(m, 2^r), verified by direct
     union-find for m in {1, 4, 20}, r = 0..8; hence
     c_src(0) = 158, c_src(1) = 315, c_src(r) = 629 for r = 2..8, and
     stabilization exactly at r >= max v_2(m) = 2. Every 629 statement
     carries r >= 2.
E4   Certified recurrent core: |R| = 6250, halves 3125 + 3125, H_0 on sheet
     z_6 = 4, H_1 on sheet z_6 = 1, closure certificate passes.
E5   Mirror law on the reconstruction: F_0 squared = id on H_0, F_1 squared
     = id on H_1, cross restrictions mutually inverse.
E6   Components: exactly 313; sizes 312 x 20 + 1 x 10.
E7   All 312 generic H_0 halves: G regular dihedral of order 10 with
     ord(s o s') = 5 and a free action; the symmetric H_1-side gate passes.
E8   Singlet half: |G| = 10, transitive on 5 points, five distinct order-2
     stabilizers, each generated by a reflection (the five reflection axes).
E9   Common cocycle in the frozen reconstruction: labels
     (0,0) -> s, (0,1) -> id, (1,0) -> id, (1,1) -> s', with s != s' and
     <s, s'> = D_5, uniform over all 312 components and compatible with the
     singlet coset action. Invariant content: cross edges id, own edges two
     distinct reflections with product of order 5.
E10  Mackey menu by direct union-find on the 3125-state target half, all
     eight subgroups enumerated individually, the five reflection C_2
     separately: D_5 -> 313, C_5 -> 625, each C_2 -> 1563, trivial -> 3125.
     The same counts on the H_1 side.
E11  629 is not an element of {313, 625, 1563, 3125}.
E12  Mixed negative control: 312 a + b = 629 with a in {1, 2, 5, 10},
     b in {1, 3, 5} has the unique solution (2, 5).
E13  Embedding arithmetic, exact Fraction: (1/2) x (1/3125) = 1/6250; the
     translation action of the quotient group on itself is transitive
     (finite shadow of the Haar uniformity lemma); kernel relation gates:
     five involutions on all 15625 states, (bc)^5 = id, and the canon step
     formula (a,b,c,d) -> (a-c+d, b-c, a, b-c+d) equals the M_J columns.
```

Diagnostic only, explicitly NON-falsifying, frozen as such because the value
depends on basepoint conventions this session cannot know without reading the
forbidden file: the independent-basepoint cross-edge census over the 312
components (the primary reports id: 157, ref2: 155 under its own
conventions). The breaker prints its own census and compares the count
multiset {157, 155} as soft corroboration only. Agreement is evidence;
disagreement is a convention artifact, not a fired gate.

## Field 2. Code

`mackey4_break.py`. Python standard library only, exact int and Fraction
arithmetic, no float anywhere, no network, no subprocess, no import of any
recon-branch file. Deterministic: fixed state encoding (base-5 tuples in
lexicographic order), sorted iteration everywhere, output byte-stable. Runs
from a directory containing only itself. Target runtime under 120 seconds.
The breaker does not import or read `mackey4_verify.py` at runtime or
authoring time.

## Field 3. Carrier and data

No external data. Carriers: F_5^6 (15625 states), the Thue-Morse bit
sequence s_2(n) mod 2 computed locally, Z^4 with the Phi_5 multiplication
structure, the quotient Z^4/L, D_5 of order 10 as the measured return group.
Constants from the public canon: s_c = (2,1,2,1), u_c = (0,1,0,-1),
c_d = (2,1,3,4,1,1), v_e = (0,0,0,0,1,0).

## Field 4. Systematics

```text
S1  One platform only. This is disclosed in every output and caps any
    downstream use at candidate grade; the two-architecture leg belongs to a
    later public probe.
S2  Convention sensitivity is classified BEFORE the run: E1-E13 invariant,
    the basepoint census diagnostic.
S3  No quantity is imported from the primary stdout; every number in E1-E13
    is recomputed from the carriers.
S4  The recurrent core is certified by closure, not by a warmup window.
S5  All 312 generic components and all five reflection subgroups are
    enumerated individually; no representative-only counting; the singlet
    C_2 count of 3 must come from direct orbit counting, not Burnside.
S6  The Thue-Morse dyadic point-spectrum premise is cited, not re-proved;
    what the breaker verifies exactly is the finite gcd component law it
    implies and both finite consequences 158 and 315 outside the admitted
    range.
S7  r >= 2 scoping is printed with every 629.
```

## Field 5. Failure thresholds

```text
B-F1  Any load-bearing value E1-E13 differs from the frozen expectation:
      record DISAGREEMENT WITH PRIMARY as a first-class outcome, preserve
      both sides, STOP for the candidate pending resolution. Never adjust
      either side to reconcile.
B-F2  An internal certificate fails (closure certificate, SNF verification
      U A V = D with unimodular U and V, well-definedness of the quotient
      action, regularity of G): STOP, defective instrument, disclosed; not a
      statement about the primary.
B-F3  Runtime nondeterminism or any float in an assertion: defective
      instrument, STOP.
B-F4  If the breaker AGREES on every load-bearing value: the primary route
      is CONFIRMED BY AN INDEPENDENT ROUTE at candidate grade, one
      platform. This does not promote anything, does not close
      ENTROPY-LAYER-BRIDGE [O], is not A_A = empty, and decides nothing
      about deeper depth, non-bijective fibers, variable depth, or r > 2
      collars.
```

Execution policy, frozen: every execution of `mackey4_break.py` is recorded
in the result ledger. Defect-fix reruns are permitted with full disclosure
and new file hashes. Expected values, thresholds, and scope never move after
this freeze. A defect in this preregistration discovered after first
execution retires this breaker id; a successor would be
PREREG-BREAKER-MACKEY4-2.

Permitted before the code pin: syntax checks and unit smoke tests of the SNF
routine on small toy matrices unrelated to the claim. Forbidden before the
code pin: any execution touching the claim carriers.

## Field 6. Action layer

```text
FROM: L2 measurable dynamical source, finite shadow only
TO:   L5 finite recurrent readout
DEPTH: lambda^5 only
NEW LIFT: none.  L6: excluded.  SI: excluded.
```

## Freeze record

At this freeze: mackey4_break.py absent, no computation under this prereg
executed. The SHA-256 of this file is recorded in the result ledger and in
the project immediately after this write.
