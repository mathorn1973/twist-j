# P-QS-COUPLING-1 owner definition, Rev 3 DRAFT

```text
DRAFT / NOT FROZEN / NO AUTHORITY / NO PROBE / NO EVALUATION
Awaiting an EXPLICIT owner ANO against the sha256 of this exact file.
No inference counts as ratification (D0 discipline). No PREREG may be
pinned, and no verifier built, until that ANO exists.
```

Lineage. Rev 1 (sha cf2b4623, 12055 B): never ratified, history only,
not reopened. Rev 2 (sha 12cadfc1, 16471 B): VOID DRAFT, failed owner
readback 2026-07-24 on seven defects (QS-VOID-DISPOSITION_2026-07-24).
This Rev 3 is a fresh draft built against that defect ledger. One named
session: QS coupling Rev 3 draft, 2026-07-24. Lane: the Schwinger clause
of QUANT-SUBSTRATE [O]; proposed branch QUANT-SUBSTRATE-SCHWINGER-COUPLING.

## 0. Defect resolutions (D0 to D6, each addressed in the named section)

```text
D0 false ratification    the banner above; ratification only by explicit
                         ANO against this file's hash; nothing looser.
D1 exp needs 1/2         RESOLVED BY REMOVAL plus a ring proposal: no
                         exponential and no factorial appears anywhere in
                         Rev 3; the vertex is group-valued and exactly
                         unitary (section 2, D2). The proposed carrier
                         ring is A' = Z[zeta_5, i][1/10] (section 1);
                         PROPOSED-D1, owner ANO required specifically on
                         this ring choice.
D2 factor two            corrected at definition level: a_e = (g - 2)/2
                         gives the moment read 5 delta-theta / (2 pi)
                         (section 2, D4; machine certificate).
D3 register symmetries   corrected: the admissible register symmetries
                         are the automorphisms Aut(Z_5) = (Z/5)^*,
                         E_k -> E_{u k}; index shifts E_k -> E_{k+c} are
                         NOT automorphisms and are retired (machine
                         witness); K-invariance under u is NOT assumed
                         (section 2, D7; fresh break round).
D4 ledger truncation     corrected: the ledger solution set is the
                         infinite family {(2m, m) : m >= 0}; the checker
                         certifies the family, claims no truncation
                         (section 2, D4).
D5 predicates, gate,     corrected: the decision rule is a sequential
   trace label           decision TREE, disjoint by construction, with a
                         64-state machine certificate (section 4); the
                         lift structure names BOTH gates, including
                         GATE-L1-L5-QS-COUPLING-STREAM (section 6); the
                         quantity pi^2/5 is everywhere called the
                         Galois-orbit real-part sum, never a trace, per
                         the public WALL-LI2-RUNG wording.
D6 silent selections     corrected: the rest point z = 1 and the coin
                         branch (1, 1) are FROZEN HERE with their
                         justification (section 2, D3), so nothing
                         downstream selects silently.
```

## Authority pin

```text
Public Canon v20 ACTIVE, tag canon-v20, merge f62f0f8, content commit
662a96f080364b39350387db53528e42c67265b2, CANON_SHA256 337d9d0d...,
96575 bytes, canon/SHA256SUMS 5 of 5 OK (fresh clone, this session).
Owner row: QUANT-SUBSTRATE [O], READY: "deriving it as
[alpha^1]((g_e(alpha)-2)/2) from a substrate coupling remains open".
Internal basis: sealed v184 snapshot (byte pin cd92b8bb), Part III (two
places), Part X (D-KCM-ORBIT-MAP, substrate knit, MUB 1/5), Part XII G4
(D-DIRAC-STEP), Part XLI (T-METRO-TICK-UNIT-SPLIT).
```

## 1. Rings (PROPOSED-D1, load-bearing, owner ANO required)

```text
carrier ring   A' = Z[zeta_5, i][1/10]
reading ring   Q(sqrt5)[pi, pi^-1], integer pi-grading, rational
               coefficients (the registered Born weights already carry
               denominators 10 and 20; readings were never A-integral)
```

Motivation for 1/10 = 1/(2 * 5): the two-places doctrine (Part III).
Prime 5 writes and its inversion 1/5 was already granted; prime 2 reads,
and the registered read-side objects carry its denominators (the spin
bisector (1 - B)/sqrt2, the Born halving 1/2). The rest-frame spectral
projectors (I +- X)/2 need exactly the denominator 2 and nothing else;
the breaker witnesses that 1/2 is unavoidable over Z[i] (load-bearing).
No exponential exists in Rev 3, so no factorial denominator ever arises;
2 and 5 are the only inverted primes.

Alternatives considered and set aside by this draft (owner may override
at ANO): (a) a lambda^2-truncated formal family with a declared rational
1/2 (rejected: keeps a continuous strength dial that integer physics
does not register; the argument channel deposits in fifths, not in
epsilons); (b) a larger cyclotomic ring Z[zeta_40][1/10] (not needed:
only i and zeta_5 occur).

## 2. The frozen coupling class: seven fields

D1 CARRIER (pointer and memory). M = M_D tensor R and nothing else:
M_D the Dirac coin, rank 2 over A', fibered over the momentum circle by
the symbol z; R = A'[Z_5], the argument register with deposit operators
E_k (E_k E_l = E_{k+l}, E_0 = 1), reference e_0. No new carrier, no
third factor, no continuum object, no ancilla outside R.
ADOPTED ROOT R-CARRIER (proposed, load-bearing): the only memory the
coupling may write is the registered argument register itself.

D2 ACTION (group-valued exact vertex; no formal strength). One joint
tick is U = (D_J(2) tensor 1) compose W with the vertex

```text
W(c_plus, c_minus) = P_plus tensor E_{c_plus} + P_minus tensor E_{c_minus},
P_plus  = (I + X)/2,   P_minus = (I - X)/2,
(c_plus, c_minus) in Z_5 x Z_5,
```

where {P_plus, P_minus} is the rest-frame spectral resolution: the
eigenprojectors of the rest step D(1) = I + 2iX, the only registered
coin frame at the electron point (G4: the coin modulus is the rest
rung). Properties, all exact: W^sharp W = 1 identically (projector
algebra; sharp is bar-transpose with zeta -> zeta^-1, i -> -i);
entries in A'; local (coin tensor register only, no momentum
dependence); register-equivariant. There is NO lambda and NO
exponential: the coupling class is the FINITE set of deposit pairs,

```text
S_raw = { W(c_plus, c_minus) : (c_plus, c_minus) in Z_5^2 },  |S_raw| = 25,
(0, 0) the uncoupled tick (excluded from couplings),
```

modulo the D7 equivalences. Broadening the frame or the class is a
Rev 4 event, not an evaluation choice. FLUCTUATION GRADING: the formal
bookkeeping variable t marks each completed register excursion (leaves
e_0, later returns to e_0) in the exact path decomposition of the
N-tick evolution; order t^1 means exactly one emitted and reabsorbed
flux unit. t never enters any matrix; every matrix is exact over A'.

D3 STATES (D6 fix; frozen here, with justification). The momentum fiber
is frozen at the rest point z = 1: the electron point is the rest rung
of the ladder (G4), and rest is the unique fiber where the uncoupled
step is the pure coin move D(1) = I + 2iX. The pre-state coin is frozen
as v_plus = (1, 1), the eigenvector of D(1) with eigenvalue 1 + 2i
(mass shell at rest; |1 + 2i|^2 = 5 = det). The conjugate branch
v_minus = (1, -1) (eigenvalue 1 - 2i) is the bar image of v_plus, so
the branch choice is a bar-orbit choice and is quotiented away by the
D7 bar equivalence: no physical freedom remains. Pre-state
u = v_plus tensor e_0. Born squares are normalized by the exact norm
tower 5^N after N ticks (the registered norm-gated staircase). All read
quantities are stationary per-tick rates (BR1 clause retained), with
every N to infinity closure taken only through D6.

D4 EXTRACTION (D2 and D4 fixes). Two responses of the same coupled
stream, both stationary per-tick rates at order t^1:

```text
moment rate    c_a := per-tick rate of delta a_e at order t^1, where
               a_e = (g - 2)/2 and the tree reading gives
               delta g = delta-theta / (pi/5), hence EXACTLY
               delta a_e = 5 delta-theta / (2 pi);
               delta-theta = the argument shift, at order t^1, of the
               e_0-component amplitude against the uncoupled reference
               (1 + 2i)^N, read through the registered phase dictionary.
channel rate   c_w := per-tick Born rate, at order t^1, of one completed
               excursion (emission tick i < reabsorption tick j), under
               the same 5^N tower.
```

K := c_a / c_w, defined only if both rates exist as exact per-tick
limits under D6 (certificate C2); K is then N-free by construction.
Alpha dictionary: the channel's own excursion weight defines alpha; one
excursion carries one alpha, so K = [alpha^1] a_e(alpha).
ADOPTED ROOT R-ALPHA (proposed, load-bearing): alpha enters as the
channel's own excursion Born rate, not as an external unit; script-Q is
not consumed by the extraction, so the comparison against
J Jbar / script-Q is not circular.
Degree ledger (corrected, parametric): c_w is pi-free, so
K = (2 pi)^-1 requires c_a at pi-degree -1; the reading contributes
one division by pi (the 5/(2 pi) factor), so delta-theta must land at
degree 0; with n_p tick phases (+1 each) against n_w wall rungs (+2
each, denominator), the ledger is n_p = 2 n_w, the INFINITE family
{(2m, m) : m >= 0}. The lowest branches are m = 0 (algebraic) and
m = 1 (two tick phases against one s = 2 rung). The realized m is an
evaluation output; the checker certifies the family and claims no
truncation.

D5 NORMALIZATIONS. Every carrier constant lies in A', generated through
the registered identities only: N(J) = 1, Tr(J) = 3 (a genuine field
trace), det(I + 2iX) = 5, tick phase 2 pi/5 (J phi = zeta_5), MUB
weight 1/5, script-Q phi^2 = 2 pi, xi phi^2 = 5. Reading coefficients
are rational over Q(sqrt5). A constant outside these rings anywhere
routes FREE-PARAMETER. No new dimensionless normalization, anywhere.

D6 REGULARIZATION. None. Every infinite tick sum must close in finitely
many exact steps through registered summation data only: at s = 1 the
tree anchor Li_1(J) = i pi/5; at s = 2 exactly the public WALL-LI2-RUNG
data: Re Li_2(sigma_a(J)) = pi^2/100 for a in {1, 4} and 9 pi^2/100 for
a in {2, 3}, the Galois-orbit real-part sum pi^2/5 (NOT a field trace,
per the public row), the channel law 1 : 9. A quantity that does not
close routes STOP.
ADOPTED ROOT R-WALL (proposed, load-bearing): the polylogarithmic wall
is the sole admissible closure resource at its rung.

D7 EQUIVALENCE (D3 fix; conservative core plus quarantined
automorphisms). V ~ V' iff conjugate by a symmetry in the PROVEN core:

```text
IN            bar conjugation (zeta -> zeta^-1, i -> -i, coin
              transpose): maps W(c_plus, c_minus) to W(-c_plus,
              -c_minus) and v_plus to v_minus; preserves every Re
              reading and the wall pair {1, 4}.
IN            the exact centralizer of the uncoupled tick on M
              (computed, not assumed: certificate C1).
QUARANTINED   register automorphisms u in (Z/5)^*: E_k -> E_{u k}
              (genuine automorphisms: unit and product preserved,
              machine witness). Their K-invariance is NOT assumed; the
              fresh break round classifies each u as equivalence (K
              provably invariant) or covariance (witness of change);
              until classified, covariance.
OUT           field sigma_2, sigma_3 as identifications (the BR2 kill
              stands: standard (2 pi)^-1 against twisted
              phi^4 (2 pi)^-1); recorded as covariance between
              Galois-twisted gates.
OUT           index shifts E_k -> E_{k+c}: not automorphisms (they
              fix neither the unit nor the product; machine witness);
              the Rev 2 error, retired.
```

INCOMPATIBLE means inequivalent with different K; equal K across
inequivalent classes is value multiplicity, not incompatibility.

## 3. Admissibility and the class (finite)

W(c_plus, c_minus) is admissible iff (c_plus, c_minus) != (0, 0) and
both rate clauses of D4 hold. The raw class has 24 couplings; S := the
admissible set modulo the proven D7 core. C1 (the verifier's first
obligation): compute the centralizer, enumerate the class, quotient by
proven equivalences, and certify the count. The Rev 2 finite-rank
parameterization machinery is retired: the class is literally finite.

## 4. Decision rule (a sequential decision tree; disjoint by construction)

```text
node 1  definitional integrity: any clause of D1..D7 ambiguous in
        execution, or a required object fails D6 closure, or C1 or C2
        cannot be certified?            YES -> STOP        NO -> node 2
node 2  any admissible coupling needs a constant outside the D5 rings,
        or K varies along a residual freedom inside one class?
                                        YES -> FREE-PARAMETER
                                        NO  -> node 3
node 3  S empty?                        YES -> NEGATIVE (empty class is
                                               a scientific negative)
                                        NO  -> node 4
node 4  all surviving classes share one K?
                                        NO  -> NONUNIQUE
                                        YES -> node 5
node 5  the shared K equals J Jbar / script-Q = (2 pi)^-1 exactly?
                                        YES -> PASS
                                        NO  -> NEGATIVE
```

The tree is total and its leaves are disjoint by construction; the
checker certifies exactly one route for all 32 combinations of the five
binary conditions. All five routes are first class; a fired route is
folded and archived, never repaired in place; no threshold moves after
data.

## 5. Falsifier (carried verbatim from the public row, not new)

Fires if the frozen exact substrate coupling of the electron to the
electromagnetic argument channel yields d a_e / d alpha at alpha = 0
different from J Jbar / script-Q = 1/(2 pi), if a new free
dimensionless normalization is required, or if two admissible couplings
survive with different coefficients.

## 6. Layer surface and gates (D5b fix: both gates named)

```text
GATE-L1-L5-QS-COUPLING-STREAM   L1 -> L5, OPEN_LIFT: emits the exact
    N-tick path decomposition of the coupled stream by excursion count,
    only when C1 (class and centralizer) is complete; ambiguity or an
    unclosed object routes STOP.
GATE-L5-L6-SCHWINGER-TERM       L5 -> L6, OPEN_LIFT: emits K only when
    C2 (rates), C3 (K per class), and C4 (constancy on classes) are
    complete; an exact miss routes NEGATIVE, non-closure routes STOP.
```

Construction lives at L1 (state algebra) and L5 (the coupled tick
stream); the measure reading is L6. Gate registration rides the owner's
fold, not this draft.

## 7. Verifier contract (build FORBIDDEN until the ANO plus a pinned PREREG)

Python standard library only; exact arithmetic only (int, Fraction,
Z[zeta_5] four-tuples, Gaussian pairs, Q(sqrt5) pairs, pi-graded ring);
no floats in any assertion; under 120 seconds; environment
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
Certificates: C1 class and centralizer; C2 per-tick rates exist and are
first order in t; C3 K per class; C4 constancy on classes; C5 the
deterministic route of section 4. Two architectures, byte-identical
stdout, at validation.

## 8. Break-round obligations for this revision (to run at draft stage)

```text
BR-A  classify u in {2, 3, 4}: equivalence or covariance, with witness
BR-B  witness that 1/2 is unavoidable for the rest-frame projectors
      over Z[i] (the D1 ring proposal is load-bearing, not convenient)
BR-C  factor-two regression: the void reading 5/pi against the correct
      5/(2 pi); Rev 3 must be immune
BR-D  tree totality fuzz over all 64 condition states, independent code
BR-E  audit: no exponential, no factorial, no float anywhere in the
      Rev 3 tool sources
```

## 9. What this draft does not do

No canon change, no probe, no evaluation, no computation of K, no
narrowing of QUANT-SCHWINGER-TARGET, no import of any incubation value
into a public claim, no authority by living in the project. The three
proposed roots (R-CARRIER, R-ALPHA, R-WALL), the PROPOSED-D1 ring, and
the D2 vertex-class freeze (rest-frame controlled deposits) are exactly
the load-bearing points the owner's ANO must cover, point by point.

## 10. Ratification

The freeze happens only when the owner issues an explicit ANO against
the sha256 of this exact file, covering: (1) the ring A', (2) the
vertex class of D2, (3) the frozen z = 1 and branch of D3, (4) the
extraction of D4 with the 5/(2 pi) reading, (5) the D7 core and
quarantine, (6) the decision tree, (7) the two gates. A partial ANO
names its exceptions and produces Rev 4. Until the ANO: no PREREG pin,
no verifier, no evaluation.
