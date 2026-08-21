# PREREG-P-QS-COUPLING-1, Rev 3 DRAFT (NOT A PIN)

```text
DRAFT / NOT FROZEN / NOT A PIN / NO AUTHORITY / NO EXECUTION
This preregistration cannot be frozen or pinned until the owner issues
the explicit ANO on the Rev 3 owner definition. It exists so the owner
can read the full pipeline in one pass. On ANO it is re-issued with the
ratified definition hash filled in, and only that re-issue is the pin.
```

Probe: P-QS-COUPLING-1. Lane: QUANT-SUBSTRATE-SCHWINGER-COUPLING; owner
row QUANT-SUBSTRATE [O] (public v20, READY). Basis: the Rev 3 owner
definition DRAFT (hash recorded in the accompanying status ledger; the
ratified hash replaces it at re-issue). Prior artifacts: Rev 1
unratified (cf2b4623); Rev 2 and its prereg VOID (12cadfc1, c2baad56).

Layer declaration: L1 (state algebra) and L5 (the coupled tick stream);
lifts only through the two named gates, GATE-L1-L5-QS-COUPLING-STREAM
and GATE-L5-L6-SCHWINGER-TERM. No other lift.

## Field 1. Equation (the claim under test)

On the finite Rev 3 class {W(c_plus, c_minus)}, (c_plus, c_minus) in
Z_5^2 minus (0,0), modulo the proven D7 core:

```text
K := c_a / c_w = [alpha^1] a_e(alpha)   compared exactly against
J Jbar / script-Q = (2 pi)^-1           in Q(sqrt5)[pi, pi^-1].
```

The run lands on exactly one leaf of the Rev 3 decision tree: STOP,
FREE-PARAMETER, NEGATIVE, NONUNIQUE, or PASS. All five first class.

## Field 2. Code version

verify.py: Python standard library only; exact arithmetic only; no
floats in any assertion; under 120 seconds; environment
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
Built strictly after the pin of the re-issued prereg; its file sha256
recorded in the run record BEFORE first execution; a post-execution
defect means a new probe id, never an amendment. Certificates C1..C5:

```text
C1  the exact centralizer of the uncoupled tick on M, the enumeration
    of the 24 couplings, the quotient by the proven D7 core, the class
    count; plus the classification of the quarantined automorphisms
    u in {2, 3, 4} (equivalence with proof, or covariance with witness)
C2  both per-tick rates exist, are exactly first order in the excursion
    grading t, and are N-free
C3  K per class, exact element of the reading ring
C4  K constant on classes
C5  the deterministic route (the 32-state-certified tree)
```

Two architectures, byte-identical stdout, at validation.

## Field 3. Carrier (the exact construction; no external dataset)

```text
S1 system    D(z) = S(z)(I + 2 i X); frozen fiber z = 1 (rest point,
             per the definition D3, not chosen here); D(1) = I + 2iX;
             pre-state coin v_plus = (1, 1), eigenvalue 1 + 2i; Born
             norm tower 5^N.
S2 register  R = A'[Z_5], deposits E_k, reference e_0; A' =
             Z[zeta_5, i][1/10] (PROPOSED-D1, inherited).
S3 coupling  U = (D(1) tensor 1) W(c_plus, c_minus), the group-valued
             vertex of definition D2; no lambda, no exponential.
S4 grading   the bookkeeping variable t marks completed register
             excursions (leaves e_0, returns to e_0) in the exact path
             decomposition of U^N u; t enters no matrix.
S5 responses delta-theta(N) := the argument shift, at order t^1, of the
             e_0-component amplitude against the uncoupled reference
             (1 + 2i)^N, read through the registered phase dictionary
             (tick phase 2 pi/5; s = 1 anchor i pi/5; s = 2 wall data);
             c_a := per-tick rate of 5 delta-theta / (2 pi)
                    (a_e = (g - 2)/2; the factor two is mandatory);
             c_w := per-tick rate, at order t^1, of the completed
                    excursion Born weight (emission i < reabsorption j),
                    same 5^N tower.
S6 K         K := c_a / c_w; comparison exact in the graded ring.
```

Ledger inherited: delta-theta at pi-degree 0; family {(2m, m) : m >= 0};
lowest branches m = 0 (algebraic) and m = 1 (one wall rung); realized m
is an evaluation output.

## Field 4. Systematics (named risks, frozen routes)

```text
R1  centralizer not exactly computable                    -> STOP (C1)
R2  a per-tick limit fails or is not first order in t;
    in particular a driven-register reading where the
    excursion decomposition relative to e_0 degenerates   -> STOP (C2)
R3  an infinite sum fails registered closure              -> STOP (D6)
R4  any needed constant outside A' or the rational
    reading coefficients                                  -> FREE-PARAMETER
R5  K depends on N after the rate clause                  -> STOP
R6  K differs along a quarantined automorphism u that C1
    proves to be an equivalence                           -> contradiction:
                                                             STOP (C1 defect)
R7  sigma_2 or sigma_3 transport used as identification   -> STOP (BR2 guard)
```

## Field 5. Failure threshold

Exact, byte-level, no tolerance: PASS only if every surviving class
yields K identical to (2 pi)^-1 in Q(sqrt5)[pi, pi^-1]. Any exact
deviation routes per the tree. A fired route is final for this probe
id; the dead branch is archived, never deleted; no threshold moves.

## Falsifier (carried verbatim from the public row)

Fires if the frozen exact substrate coupling of the electron to the
electromagnetic argument channel yields d a_e / d alpha at alpha = 0
different from J Jbar / script-Q = 1/(2 pi), if a new free
dimensionless normalization is required, or if two admissible couplings
survive with different coefficients.

## Non-claims

No public status is touched. Nothing here authorizes execution: the
order is owner ANO on Rev 3, re-issue and pin of this prereg with the
ratified hash, verifier build, file-sha pin, run. Validation is public
(two architectures, byte identity, owner fold), not here.
