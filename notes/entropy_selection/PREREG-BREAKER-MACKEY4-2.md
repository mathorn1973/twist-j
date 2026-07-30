# PREREG-BREAKER-MACKEY4-2

The successor breaker gate of candidate `C-ENTROPY-MACKEY-OBSTRUCTION-4-N`,
scoped to the common-cocycle premise.

```text
STATUS:        NON-CANONICAL PREREGISTRATION, BREAKER LANE
AUTHORITY:     NONE
CLAIMED GATE:  the common-cocycle premise E9 of
               PREREG-BREAKER-MACKEY4-1, and gates S7 and F6 of
               PREREG-C-ENTROPY-MACKEY-OBSTRUCTION-4-N
PREDECESSOR:   PREREG-BREAKER-MACKEY4-1
               sha256 d02badef96706f4c1e3f88edf1430e4641e2276245873b875e56f399fafc8a51
WRITTEN BY:    owner-side adjudicating session, 2026-07-30. This session has
               read mackey4_verify.py and mackey4_break.py and is therefore
               DISQUALIFIED from authoring the instrument under this prereg.
IMPLEMENTED BY: a clean session, to be named in its own result record, which
               must satisfy the independence fence below.
OPENED:        2026-07-30
PUBLIC BASIS:  Public Canon v28
MAIN:          3161cbc764f547c95a80c3bd5028acf71c2ef524
TAG:           canon-v28
CONTENT:       86a046007f89a64a696d013112a44f02e624dd2e
CANON SHA:     4b720846ccd42c7ec808ab2acb21793962390b074bb3799d28c0f16c00165d2c
LANE BASE:     b1f997d6191d75a61261119e2a2277955151b3ed
               on notes/entropy-selection-recon-breaker-m2
INTENDED CODE: mackey4_cocycle.py (authored after this freeze)
CEILING:       candidate-C at best. The gate decides AGREE or DISAGREE on the
               common-cocycle premise, not status.
COMPUTATION UNDER THIS PREREG BEFORE FREEZE: NONE
```

## Why this preregistration exists

`PREREG-BREAKER-MACKEY4-1` froze `E9` as the common-cocycle expectation and
justified its non-triviality by asserting that, although the four edge maps
are left translations by construction, the residual content is "the uniformity
of the marked presentation across all 312 generic components".

That justification is wrong, and the defect was found only after the first
execution. Under a per-component marking derived from each component's own
dynamics, uniformity is automatic as well. Gate `B13` of `mackey4_break.py`
was run verbatim on a synthetic target carrying four deliberately different
per-block cocycles and reported one uniform cocycle on all of them. The gate
cannot fail once the mirror law and the regular-dihedral gate pass, so it
carries no evidence about the premise it names. The full adjudication is in
`MACKEY4-BREAKER-RESULT.md`, section 5.

Two consequences are recorded here and neither is decided by this file:

```text
1  E9 is currently supported by the primary route only. E1-E8 and E10-E13 are
   supported by two independent exact routes.
2  PREREG-BREAKER-MACKEY4-1 states that a defect in it discovered after first
   execution retires that breaker id, with this file as the successor. Whether
   that retirement is total, which would also withdraw breaker-1's support for
   E1-E8 and E10-E13, or confined to E9, is an OWNER RULING. It is not settled
   by this preregistration.
```

Because that ruling is open, the instrument under this prereg is required to
emit the Mackey menu as a secondary output. It must build the target anyway,
so a total-retirement ruling then costs no third instrument.

## Independence declaration, falsifier first

This breaker is falsified as an independent gate if any of the following is
shown: the implementing session read or imported any file on the forbidden
list; the expected values or thresholds below were altered after this freeze;
or the negative controls of Field 5 were weakened, reordered, or run after the
target gate rather than before it.

```text
FORBIDDEN, at authoring time and at run time:
  mackey4_verify.py
  mackey4_primary.stdout.txt
  MACKEY4-PRIMARY-RUN.md
  MACKEY4-PRIMARY-RESULT.md
  mackey4_break.py
  mackey4_break.stdout.txt
  RESULT-BREAKER-MACKEY4-1.md
  MACKEY4-BREAKER-RESULT.md
  PREREG-BREAKER-MACKEY4-1.md
  every other file in notes/entropy_selection/

PERMITTED:
  this file
  PREREG-C-ENTROPY-MACKEY-OBSTRUCTION-4-N.md   (the frozen claim spec)
  RECON-V28-STATUS.md                          (lane status and scope)
  canon/CANON.md sections 2 and 3, canon/REGISTRY.tsv
```

The forbidden list is wider than breaker-1's on purpose.
`MACKEY4-BREAKER-RESULT.md` contains the construction of the negative control
and the outcome of the gate; `RESULT-BREAKER-MACKEY4-1.md` and both stdout
files contain edge labels and gauge counts. Reading any of them would let the
implementer write toward a known answer.

No expected edge label, gauge value, or gauge census count appears anywhere in
this file. That is deliberate. Those quantities are gauge-dependent and are not
comparable across independent implementations; comparing them was already
shown to be meaningless for the basepoint census. What this gate decides is
stated in Field 1 in invariant terms only.

## Field 1. Equation and decision surface

The premise under test, stated so that it can fail:

```text
There exists ONE group G isomorphic to D_5, given as ten explicit
permutations of the recurrent core R, the SAME ten permutations for every
component, such that after a per-component gauge drawn from a gauge set
declared before the run, all 312 generic components and the singlet carry
the SAME four one-tick edge labels.
```

The load-bearing word is `SAME`. A marking rebuilt separately from each
component's own dynamics satisfies this vacuously and is forbidden by `C4`
below.

### Required construction

```text
C1  Rebuild the recurrent core R from the public canon v28 generator table by
    an exact method of the implementer's choice. R and its two halves are
    inputs to this gate, not its subject; if the reconstruction disagrees with
    the frozen candidate spec, stop and report a defect rather than continue.
C2  Exhibit G <= Sym(R) with G isomorphic to D_5, as ten explicit permutations
    of R, obtained from the public generator table by a documented search or
    construction. The ten permutations are fixed once and are identical for
    every component. The multiplication table must be verified elementwise
    against an abstract D_5.
C3  Verify that G restricts to a free and transitive action on the ten points
    of every generic half, on both sides, and to a transitive action with
    order-2 point stabilizers on the singlet half. This is a real gate: a
    global group need not restrict regularly to every half, and failure here
    is a first-class result.
C4  FORBIDDEN: deriving the group, the rotation, or either marked reflection
    from a restriction of the branch maps to a single component, or from any
    per-component basepoint. The group must exist before any component is
    examined. An implementation in which the group is a function of the
    component is a defective instrument under B2-F2, not a passing gate.
C5  Declare the gauge set Gamma <= D_5 in the run record BEFORE the target
    gate executes, together with the per-component gauge rule. A gauge rule
    that may select any element of D_5 per component is not a gauge rule; it
    is a relabeling and fails C4 in substance. Gamma must be a proper subset
    and the rule must be a stated function of the component, not a search for
    whatever makes the labels agree.
C6  With G, Gamma, and the gauge rule fixed, compute the four one-tick edge
    labels (previous half, current bit) on every generic component and the
    singlet, and report whether they are the same 4-tuple throughout.
```

### Frozen expected values

Load-bearing. Any mismatch is DISAGREE.

```text
G1  A group G satisfying C2 exists and its multiplication table matches D_5.
G2  G restricts to a free regular action on all 312 generic halves, both
    sides, and to a transitive action with order-2 stabilizers on the singlet.
G3  Under the declared Gamma and gauge rule, the four edge labels are the SAME
    4-tuple on all 312 generic components and are compatible with the singlet
    coset action.
G4  Invariant shape of that 4-tuple: the two cross edges are the identity; the
    two own edges are two DISTINCT reflections whose product has order 5,
    hence generate the whole of D_5.
G5  Secondary output, required because the retirement ruling is open: the
    Mackey menu by direct orbit counting over the target half, all eight
    subgroups enumerated individually including the five reflection C_2
    separately, on both halves, together with the statement of whether 629 is
    an element of the resulting menu, and the mixed control
    312a + b = 629 over a in the generic-orbit menu and b in the singlet-orbit
    menu.
```

`G5` is reported, not assumed. Its expected values are those already frozen in
`PREREG-C-ENTROPY-MACKEY-OBSTRUCTION-4-N.md`, Field 1.2, which the
implementing session is permitted to read.

Explicitly NOT part of the decision surface, because they are gauge-dependent
and not comparable across implementations: the identity of the specific
reflections in the 4-tuple, the specific elements of Gamma, the census of
gauge values over the 312 components, and any basepoint-dependent count. These
may be printed as diagnostics and fire nothing.

## Field 2. Code

`mackey4_cocycle.py`. Python standard library only, exact integer arithmetic,
`Fraction` where a rational is needed, no float in any assertion, no network,
no subprocess, no import of any file on the forbidden list. Deterministic:
fixed encodings, sorted iteration, output byte-stable. Runs from a directory
containing only itself. Target runtime under 300 seconds.

The negative controls of Field 5 are part of the same file and print before
the target gate, so that a defective gate is visible in the same stdout that
carries the result.

## Field 3. Carrier and data

No external data. Carriers: `F_5^6` with 15625 states, the Thue-Morse bit
sequence computed locally, the recurrent core `R`, `D_5` of order 10, and the
synthetic control targets of Field 5, which are built from `D_5` alone and
touch no claim carrier. Constants come from the public canon generator table.

## Field 4. Systematics

```text
S1  One platform is expected; disclose it in every output. This caps any
    downstream use at candidate grade. The two-architecture leg belongs to a
    later public probe, not here.
S2  The group is global and prior to the components. C4 is the systematic that
    breaker-1 failed; it is checked structurally, not by assertion.
S3  Gamma and the gauge rule are declared before the target gate runs and are
    printed in the stdout above the target result.
S4  No quantity is imported from any primary or breaker-1 output. Every number
    is recomputed from the carriers.
S5  All 312 generic components and all five reflection subgroups are
    enumerated individually. No representative-only counting. The singlet
    C_2 orbit count comes from direct orbit counting, not Burnside.
S6  Gauge-dependent quantities are classified as diagnostic BEFORE the run and
    are never compared across implementations.
S7  Every statement that mentions 629 carries the r >= 2 scope.
```

## Field 5. Failure thresholds and mandatory negative controls

The controls run FIRST and their outcome is printed before the target gate.
They are acceptance tests of the instrument, not of the claim.

```text
N1  Build a synthetic target of at least four components, each a pair of
    ten-point halves carrying a free regular D_5 action, with the own-half
    reflections and the cross maps chosen DIFFERENTLY on every component, so
    that no common cocycle exists by construction. The gate of C6 must REJECT
    this target. A gate that accepts it is defective and the run stops.
N2  Build a second synthetic target of at least four components in which every
    component shares one common cocycle except exactly one, which is perturbed
    by a single reflection. The gate of C6 must REJECT this target too. This
    tests sensitivity, not only gross failure. A gate that accepts it is
    defective and the run stops.
N3  Build a third synthetic target in which all components genuinely share one
    common cocycle. The gate of C6 must ACCEPT it. A gate that rejects it is
    defective and the run stops.
```

Decision thresholds on the real target, after N1, N2 and N3 pass:

```text
B2-F1  G1, G2, G3 or G4 fails on the real target: the common-cocycle premise
       is NOT established. Record DISAGREEMENT as a first-class outcome,
       preserve both sides, STOP for the candidate. This falsifies the Mackey
       route rather than proving anything about the bridge. Never adjust
       either side to reconcile.
B2-F2  C4 or C5 is violated by the implementation, or any control N1-N3 gives
       the wrong verdict: defective instrument, disclosed, STOP. This is a
       statement about the instrument, not about the premise.
B2-F3  Runtime nondeterminism, or any float in an assertion: defective
       instrument, STOP.
B2-F4  G1-G4 all hold on the real target: the common-cocycle premise is
       CONFIRMED BY AN INDEPENDENT ROUTE at candidate grade, on the declared
       number of platforms. This promotes nothing, does not close
       ENTROPY-LAYER-BRIDGE [O], is not A_A = empty, and decides nothing about
       deeper depth, non-bijective fibers, variable depth, or r > 2 collars.
B2-F5  G5 differs from the values frozen in the candidate preregistration:
       record it as a first-class disagreement on the counting content,
       independently of the G1-G4 verdict.
```

Execution policy, frozen: every execution of `mackey4_cocycle.py` is recorded
in the result ledger with its stdout hash. Defect-fix reruns are permitted with
full disclosure and new file hashes. Expected values, thresholds, controls, and
scope never move after this freeze. A defect in this preregistration discovered
after first execution retires this breaker id; a successor would be
`PREREG-BREAKER-MACKEY4-3`.

Permitted before the code pin: syntax checks, and unit tests of the group and
gauge machinery on synthetic `D_5` data only. Forbidden before the code pin:
any execution touching `F_5^6`, the recurrent core, or any claim carrier.

## Field 6. Action layer

```text
FROM: L2 measurable dynamical source, finite shadow only
TO:   L5 finite recurrent readout
DEPTH: lambda^5 only
NEW LIFT: none.  L6: excluded.  SI: excluded.
```

## Freeze record

At this freeze: `mackey4_cocycle.py` absent, no computation under this prereg
executed, no implementing session named. The SHA-256 of this file is recorded
in `RECON-V28-STATUS.md` in the same commit that adds it.
