# P-ENTROPY-BRIDGE-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS

## Scientific decision (aarch64 leg)

```text
RESULT 16/16 ALL PASS, exit 0, stderr empty.
```

All sixteen preregistered gates passed on the first execution of the pinned
verifier (pin commit 9fc7a6c3a3d1d4024f4bd9f8fdb844733a80fbc8, public lock
issue 25, base 57de0af8a50e14e52f0fa81e0158f6a370cab5a5).

Recorded outcomes at the preregistered scope:

```text
G02 LIFT-DEFECT    the fired lift falsifier is formalized: over Z,
                   (bc)^5(x) = x + (10, 5 - 5r, 10, 5 + 5r, 5, 0);
                   identity mod 5, not the identity over Z_5. The
                   relation (bc)^5 = 1 is a property of the shadow,
                   not of the literal 5-adic lift.
G04-G08            census re-derived: 313 attractors = 312 x 20 + 1 x 10;
                   basins {50: 312, 25: 1}; support 6250; sheet z in
                   {1, 4}; closure under both branches.
G10                branch indegree on the support: each branch exactly
                   {0: 3125, 2: 3125}; total F_0 + F_1 exactly 2 per
                   state. Neither branch alone preserves the uniform law;
                   the fair average does.
G11-G13            joint Cesaro transport from the uniform law, frozen
                   window [512, 2048): component masses exactly the basin
                   sizes from n = 512; occupation exactly 3840 units per
                   recurrent state and 0 per transient state (psi-marginal
                   exactly uniform 1/6250 on the recurrent core); maximal
                   within-component L1 distance exactly 1/256 at N = 1024
                   and exactly 0 at N = 2048.
G14-G15            letter masses exactly (b, d, e) = (16000000, 4000000,
                   4000000), ratios exactly (2/3, 1/6, 1/6); driver pair
                   (0,0) count exactly 256 = 1536/6.
G16                cut depth necessity: p_TM(3) = 6 < 10 <= p_TM(4) = 10,
                   so a finite-cylindrical cut at lambda-depth 4 requires
                   TM-depth K >= 4.
```

No scientific falsifier fired. The formalized F of gate G02 is a
preregistered first-class record of an already fired lift falsifier, not a
new fire.

## Scope

Layer L5 with the L6 measure content scoped to the frozen finite window.
No L2 lift is claimed. The cut construction beyond the G16 necessary
condition is successor scope. Nothing here modifies canon/, the registry,
or the frontier.

## Two-architecture computation gate

```text
aarch64 leg:  PASS (RUN.md in this directory; stdout sha256
              87650d1cb40992a9aa12ee402b350581dc29e756b9cf7f3c02ba996320e8e6ef,
              1664 bytes)
x86_64 leg:   PASS. Required check job on pull request 26, head
              9d48a144fa6b30c3d7524eb68560063576a1d6f3: run 29337101998,
              job 87098995766, conclusion success (GitHub x86_64
              ubuntu-latest rerun of the pinned verifier with exact byte
              comparison against EXPECTED.txt).
gate:         PASS. Byte-identical stdout on aarch64 and x86_64.
```

Procedural disclosure: the first workflow run (29336418388) stopped before
the verifier with "P-ENTROPY-BRIDGE-1 lacks RESULT.md"; the preliminary
RESULT record was added in commit 9d48a14 without touching the four pinned
files, and the rerun executed the verifier. No gate semantics were affected.

The earned status at the preregistered scope: the sixteen exact gates stand
as computed public facts (C grade at the frozen finite scope; the G02 lift
defect is an exact integer identity), two-architecture reproduced. Folding
into the registry, frontier, or Canon is a separate sealed step and is not
performed by this probe.
