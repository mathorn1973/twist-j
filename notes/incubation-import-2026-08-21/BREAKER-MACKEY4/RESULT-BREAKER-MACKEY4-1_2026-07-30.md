# RESULT-BREAKER-MACKEY4-1

Independent breaker result for candidate C-ENTROPY-MACKEY-OBSTRUCTION-4-N.

```text
STATUS:      NON-CANONICAL BREAKER RESULT, INCUBATION LANE
DECISION:    22 of 22 PASS. INDEPENDENT ROUTE AGREES WITH THE PRIMARY ON
             EVERY LOAD-BEARING VALUE. NO FALSIFIER FIRED.
GRADE:       candidate grade, ONE platform. No public status is earned.
SESSION:     M2 breaker session, Cowork claude-fable-5, 2026-07-30
PUBLIC BASIS Public Canon v28, tag canon-v28,
             content 86a046007f89a64a696d013112a44f02e624dd2e,
             canon sha 4b720846ccd42c7ec808ab2acb21793962390b074bb3799d28c0f16c00165d2c
PREREG:      PREREG-BREAKER-MACKEY4-1_2026-07-30.md
             sha256 d02badef96706f4c1e3f88edf1430e4641e2276245873b875e56f399fafc8a51
             frozen BEFORE the breaker was written; expected values E1-E13
             and the convention-sensitivity classification frozen there.
BREAKER:     mackey4_break.py
             sha256 2bcb6ce2f009395e81f5904aef45475e8f165983003b6c4ca2d6aead86be6faa
             29504 bytes
STDOUT:      mackey4_break.stdout.txt
             sha256 96475153f0c7745d06bcbdde709ce0a5ee6b5da1e6aa8630d56d67cd6556c323
             3912 bytes
ENVIRONMENT: platform Ubuntu 24.04.4 LTS, architecture x86_64,
             Python 3.11.15, LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
             PYTHONHASHSEED=0 TZ=UTC, stdlib only, int and Fraction only,
             no float anywhere, no network, no subprocess.
RUNS LEDGER: run 1: the formal pinned run, exit 0, empty stderr, 22/22 PASS.
             run 2: same-command determinism reproduction, stdout
             byte-identical (same sha256). No other execution of this file
             occurred. Pre-pin activity was limited to py_compile and an SNF
             smoke test on three toy matrices, as the frozen prereg permits.
INDEPENDENCE mackey4_verify.py, mackey4_primary.stdout.txt and
             MACKEY4-PRIMARY-RUN.md were not read at any point, before or
             after the run. Nothing was imported from the recon branch.
```

## What the independent route reconstructed and confirmed

Source, by the distinct presentation the candidate prereg requires
(integer multiplication matrix plus Smith normal form, no lambda digits):

```text
SNF of the lambda^5 ideal lattice: invariant factors (5, 5, 5, 25),
  |det| = 3125, U and V unimodular, U A V = D verified exactly.
  Additive type Z/25 + (Z/5)^3.                                  agrees
J acts through W = U M_J U^-1, well-defined mod (5,5,5,25);
  cycle type {1: 1, 4: 1, 20: 156}, unique fixed class 0,
  permutation order 20.                                          agrees
Dyadic law components(C_m x Z/2^r) = gcd(m, 2^r) verified by
  direct orbit count for m in {1,4,20}, r = 0..8.                agrees
c_src table: 158 at r=0, 315 at r=1, 629 at every r in 2..8;
  stabilization exactly at r = max v_2 = 2. Every 629 carries
  the r >= 2 scope.                                              agrees
```

Target, rebuilt from the public canon v28 generator table only, with an
exact certified recurrent core (closure certificate, no census warmup
window):

```text
Five involutions verified on all 15625 states; (bc)^5 = id; the
  M_J step identity; the z6 laws; selector fires only b, d, e
  on the core.                                                   agrees
R = H_0 + H_1, 3125 + 3125, sheets 4 and 1, mirror law exact.    agrees
313 components: 312 x 20 + 1 x 10.                               agrees
All 312 generic halves on both sides: free regular dihedral
  group of order 10 with ord(s s') = 5, multiplication table
  verified elementwise.                                          agrees
Singlet half: transitive order-10 dihedral action on 5 points,
  five distinct reflection stabilizers, k = 0..4: the five
  reflection axes, D_5/C_2.                                      agrees
Common cocycle: in one frozen transported-basepoint
  reconstruction, every component and the singlet carry the
  same four edge labels (0,0)->s, (0,1)->id, (1,0)->id,
  (1,1)->s r: cross edges identity, own edges two distinct
  reflections generating the full D_5.                           agrees
Mackey menu by direct union-find on the 3125-state target half,
  all eight subgroups individually, both halves:
  D_5 -> 313, C_5 -> 625, each of the five reflection C_2 ->
  1563, trivial -> 3125.                                         agrees
629 not in {313, 625, 1563, 3125}.                               agrees
Mixed negative control: 312a + b = 629 has the unique solution
  (2, 5), requiring C_5 on generic blocks and the trivial group
  on the singlet, unavailable to one common Mackey range. The
  common cocycle is load bearing.                                agrees
Embedding arithmetic (1/2)(1/3125) = 1/6250 exact; translation
  transitivity on the 3125 classes (finite Haar shadow).         agrees
```

## The one disclosed difference, diagnostic and non-falsifying

The independent-basepoint cross-edge census over the 312 generic components:

```text
breaker:  id -> 156, reflection (1,2) -> 156     multiset {156, 156}
primary:  id -> 157, ref2 -> 155                 multiset {157, 155}
```

The structure agrees exactly: exactly two gauge classes, one the identity
and one a single fixed reflection (index 2 in both labelings). The counts
differ by one component moved between classes. The frozen prereg classified
this census as convention-dependent BEFORE the run, because it depends on
the basepoint rule, which this session cannot know without reading the
forbidden primary file. It is recorded here as a soft structural
corroboration and an exact count difference, preserved, not reconciled, and
it fires nothing. If the owner later finds the two basepoint rules were
identical, the count difference becomes a real discrepancy and must be
investigated at that point, not now.

## What this result means for the lane

The candidate preregistration's decision rule requires, for the
candidate-C NEGATIVE SUBCLASS RESULT, that every S gate passes, no F gate
fires, BOTH EXACT ROUTES AGREE, and the common-cocycle reconstruction is
explicit. The breaker gate that held the lane at STOP PENDING INDEPENDENT
BREAKER is now satisfied on this session's side: the two routes agree on
every load-bearing object, and this breaker's cocycle reconstruction is
explicit and verified per component.

Modulo the written finite-extension Mackey theorem of the primary (a proof
document, not recomputed here), the confirmed finite content excludes
measurable conjugacy in the fixed-depth-five, fiberwise-bijective,
r >= 2 Route A subclass: 629 source components against a target menu of
{313, 625, 1563, 3125}.

What this does NOT do, restated so nothing inflates:

```text
It is not A_A = empty. ENTROPY-LAYER-BRIDGE [O] stays open and STOP.
It decides nothing about deeper lambda depth, non-bijective fibers,
  variable depth, non-factorizing maps, or r > 2 collar classes.
It earns no public status: one platform, candidate grade, incubation lane.
Promotion needs the public probe protocol with its own preregistration,
  pin, and two-architecture gate.
```

## Owner hand-off

```text
1  Commit mackey4_break.py and mackey4_break.stdout.txt to
   notes/entropy_selection/ on the recon branch as the required breaker
   artifacts, together with this result and the breaker prereg, commit as
   A. M. Thorn <thorn@twistj.com>. This session has no push credentials.
2  The recorded lane decision STOP PENDING INDEPENDENT BREAKER can then be
   re-evaluated by the owner against the candidate prereg decision rule.
3  The diagnostic census difference (156/156 vs 157/155) should be noted in
   the lane; it is convention-dependent unless the basepoint rules are shown
   identical.
```

## Falsifier for this record

This record is wrong if the pinned files do not match the hashes above, if
any stdout line differs from mackey4_break.stdout.txt, if the runs ledger is
incomplete, or if mackey4_break.py is shown to read or import any forbidden
primary file.
