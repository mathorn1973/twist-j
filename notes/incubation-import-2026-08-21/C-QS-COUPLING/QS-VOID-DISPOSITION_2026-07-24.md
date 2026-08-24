# QS-COUPLING VOID disposition and Rev 3 defect ledger, 2026-07-24

Incubation lane record, no authority. This supersedes the ratification
narrative of QS-COUPLING-FREEZE-RECORD_2026-07-24. Owner readback: VOID.

## Disposition (owner-directed)

```text
Rev 2 owner definition   VOID DRAFT, archived, sha 12cadfc1 (16471 B)
PREREG-P-QS-COUPLING-1   VOID DRAFT, archived, sha c2baad56 (6074 B)
Rev 1 owner definition   NOT RATIFIED; NOT reopened; sha cf2b4623 stands
                         as history only
coupling verifier        NOT built, NOT run (never was)
next                     Rev 3 with new hashes and a NEW explicit owner ANO
```

## Correction of the false ratification claim (owner is right)

The freeze record attributed a ratification to the directive
"ok. jdi podle pořadí". That reading was wrong. That directive meant
"proceed by the order", not "I adopt these exact bytes". No ratification
occurred in this thread; the owner has now recorded an explicit NO.
Rev 1 was never ratified. The agent owns this misattribution; it is the
first defect and the reason a ratification event must be an explicit,
byte-scoped ANO and nothing looser.

## Defect ledger (all seven confirmed; fix or owner-decision named)

```text
D0  false ratification            CONFIRMED. Fix: a ratification is only an
    (freeze record)               explicit ANO against a named hash. No
                                  agent inference counts. Recorded above.

D1  exp(lambda G) over A[i][[l]]   CONFIRMED. G^2/2 needs 1/2, and
    is not defined; 1/2 not in     1/2 is not in A = Z[zeta_5][1/5].
    A = Z[zeta_5][1/5]             LOAD-BEARING OWNER DECISION for Rev 3:
                                  either (a) drop exp and freeze the tick
                                  as an explicit exact finite unitary whose
                                  entries close in a named ring, or (b) name
                                  the enlarged coefficient ring for the
                                  formal expansion and prove the factorial
                                  denominators cancel in the ratio K, or
                                  (c) restrict to order lambda^2 and carry
                                  the single 1/2 as a declared rational, not
                                  a ring element. The agent must not pick
                                  this; it changes what the coupling is.

D2  factor-two error (PREREG)      CONFIRMED. a_e = (g-2)/2, so the moment
                                  read is 5 delta-theta / (2 pi), not the
                                  used 5 delta-theta / pi. Fix: define a_e
                                  directly and read [alpha^1] a_e; the extra
                                  1/2 is mandatory. Mechanical, but it lived
                                  in a frozen file, so it voids the freeze.

D3  E_k -> E_{k+c} not an          CONFIRMED. A shift fixes neither the unit
    automorphism                   (E_0 -> E_c) nor the product
                                  (E_{k+c}E_{l+c} = E_{k+l+2c}). Fix: the
                                  admissible register symmetries are the
                                  group automorphisms Aut(Z_5) = (Z/5)*,
                                  E_k -> E_{u k}, u in {1,2,3,4}, which do
                                  preserve unit and product. NOTE: E_k -> E_uk
                                  may correlate with sigma_u on the field
                                  (the BR2 hazard); Rev 3 must re-run the
                                  break round on the corrected group, not
                                  assume it inherits BR2's disposition.

D4  ledger n_p - 2 n_w = 0 is       CONFIRMED. The solution set is the
    infinite; checker truncated    infinite family {(2m, m): m >= 0}, not
    with range(5)                  the three tuples the certificate asserted.
                                  Fix: the Rev 3 checker certifies the
                                  parametric family and names the two lowest
                                  branches (m=0 algebraic, m=1 single wall
                                  rung) as branches, with the realized m an
                                  evaluation output. No len(...)==3 claim.

D5  predicates not disjoint;        CONFIRMED (three sub-defects).
    no L1->L5 gate; "trace          (a) The decision rule must be a genuine
    pi^2/5" contradicts             disjoint decision TREE, not overlapping
    public WALL-LI2-RUNG            predicates that happen to sort on a
                                  hand-picked terminal table. (b) Add
                                  GATE-L1-L5-QS-COUPLING-STREAM; only
                                  GATE-L5-L6 was named. (c) The public v20
                                  row states the orbit real-part SUM is
                                  pi^2/5 and EXPLICITLY that it is NOT a
                                  field trace. Every use of the word "trace"
                                  for that sum is forbidden; Rev 3 says
                                  "Galois-orbit real-part sum pi^2/5 (not a
                                  field trace, per WALL-LI2-RUNG)".

D6  PREREG silently fixes z=1        CONFIRMED. Rev 2 D3 froze neither the
    and branch (1,1)                rest point z=1 nor the coin eigenvector
                                  (1,1); the PREREG used both. Fix: either
                                  freeze z=1 (rest mass shell) and the
                                  eigenvector choice IN the definition, with
                                  justification, so the PREREG inherits, or
                                  do not specify them. No silent selection.
```

## What Rev 3 must carry before any freeze

```text
1  the D1 ring/unitary decision made by the owner (load-bearing);
2  D2 factor-two corrected at the definition level;
3  D3 register group = Aut(Z_5), with a FRESH break round (BR2 re-tested);
4  D4 parametric ledger, checker certifies the family;
5  D5 disjoint decision tree + GATE-L1-L5 named + no "trace" for the sum;
6  D6 z and eigenvector either frozen-with-justification or absent;
7  a NEW explicit owner ANO against the Rev 3 hash. No inferred ratification.
```

## S5 accepted (TM-SYM2), recorded verbatim

The owner froze S5 by the entrywise formula
mu_W(w) = (q_* f)([w]) Born_{[w]}(w), mu_s = s_* mu_W; all 48 selectors
evaluated across the four G-orbits, no averaging, no representative;
epsilon_read stays an unmerged tag; descend to one L6 measure only if
mu_s is a singleton, else route NEGATIVE; PASS gives 1/3 * 1/2 = 1/6,
mu_i = 1/6, M = (1/3) P1 + (2/15) P5. This is folded into the TM-SYM2
draft. The rest of that draft (S1, S3, S4, dependency graph S6) stays
open; the draft remains STOP / NO AUTHORITY.

## Larmor

Not publicly pinned. The arithmetic verifier reproduces exit 0 but only
re-establishes the already-public g = 2; the public v17 audit forbids a
physical probe before an owner/governance definition of the equation,
layer, lift, and parent closure. The handoff package also lacks the
cited PREREG, a formal aarch64 record, and the breaker. No issue,
branch, or PR was created. The handoff stays a lane note, not a
public action.
