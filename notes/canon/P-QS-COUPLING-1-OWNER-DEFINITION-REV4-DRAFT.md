# P-QS-COUPLING-1 owner definition, Rev 4 DRAFT

```text
DRAFT / NOT FROZEN / NO AUTHORITY / NO PROBE / NO EVALUATION
Awaiting an EXPLICIT owner ANO against the sha256 of this exact file.
No inference counts as ratification (D0 discipline). No PREREG may be
pinned, and no verifier built, until that ANO exists.
```

Lineage. Rev 1 (sha cf2b4623, 12,055 B): never ratified, history only.
Rev 2 (sha 12cadfc1, 16,471 B): VOID DRAFT, seven defects
(`QS-VOID-DISPOSITION_2026-07-24`). Rev 3 (sha
`93669488f8ffbac90b1fc3cc6aa3310052c04863c0475819fd50a68688ffb543`,
16,826 B, `notes/incubation-import-2026-08-21/C-QS-COUPLING/`): never
ratified; superseded by this Rev 4, which is Rev 3 re-keyed to Public
Canon v71 against the audit of issue #689 (working map step 9.3). Lane:
the Schwinger clause of `QUANT-SUBSTRATE [O]`.

## 0. Audit resolutions (A1 to A6 of issue #689, each addressed below)

```text
A1 stale authority pin    re-keyed to Public Canon v71 (authority pin below);
                          every load-bearing citation now names a v71 row.
A2 gate topology          section 6 spells both proposed gate rows to the
                          v71 explicit-gate contract; neither exists in the
                          current 11-row canon/GATES.tsv; registration rides
                          the owner's fold, never this draft.
A3 citation re-keying     QUANT-SCHWINGER-TARGET [T], WALL-LI2-RUNG [T],
                          WALL-CIRCLE-LEMMA [T], ELECTRON-G-TREE [D],
                          J-PROJECTIONS [T], J-MAHLER-MEASURE [T],
                          BORN-ORDER-STAIRCASE [T] cited by name; the Rev 3
                          identity "xi phi^2 = 5" is REMOVED (no v71 row
                          carries it; nothing below consumes it); the MUB
                          weight 1/5 is demoted to an explicit cite-or-drop
                          slot (section D5).
A4 circularity exclusion  D5 now excludes script-Q and every 2 pi equivalent
                          from the generation set of constants entering c_a
                          or c_w; new certificate C6 (script-Q
                          non-consumption) added in section 7.
A5 reading data           new field D8 freezes the delta-theta reading per
                          POLICY.md section 4 (domain, codomain, context
                          keys, equality, overlap), resting on
                          ELECTRON-G-TREE [D].
A6 internal references    the sealed v184 material is lineage only (one
                          sentence below); no clause of Rev 4 rests on it.
```

## Authority pin

```text
Public Canon v71 ACTIVE, tag canon-v71, content commit
a77d720433c19976f9ab663d023ec9364eac34eb, CANON_SHA256
0306abb2e7f855ceb4fcbfdf14265a9d2c5c8bd23b35868b74a92aae16b5e279,
369,836 bytes; main at drafting
7f4c102e27e7b2ebdf5ca9215db5c5ab846ebbe2.
Owner row: QUANT-SUBSTRATE [O]: "... deriving it as
[alpha^1]((g_e(alpha)-2)/2) from a substrate coupling remains open".
Target row: QUANT-SCHWINGER-TARGET [T]: J Jbar / script-Q = 1/(2 pi),
derived from J Jbar = phi^-2 and script-Q phi^2 = 2 pi; arithmetic only.
Wall rows: WALL-LI2-RUNG [T] (s = 2 data and the "Galois-orbit real-part
sum" label), WALL-CIRCLE-LEMMA [T] (Li_1(J) = i pi/5 as the N = 5, a = 2
case). Tree reading: ELECTRON-G-TREE [D]. Axiom projections:
J-PROJECTIONS [T]. Field trace: J-MAHLER-MEASURE [T] (Tr_(K/Q)(J) = 3
from the characteristic polynomial). Norm tower: BORN-ORDER-STAIRCASE [T].
Lineage only, no authority: the sealed internal v184 snapshot (byte pin
cd92b8bb) motivated Rev 1 to Rev 3; no Rev 4 clause rests on it.
```

## 1. Rings (PROPOSED-D1, load-bearing, owner ANO required)

```text
carrier ring   A' = Z[zeta_5, i][1/10]
reading ring   Q(sqrt5)[pi, pi^-1], integer pi-grading, rational
               coefficients
```

Motivation for 1/10 = 1/(2 * 5): prime 5 writes and its inversion was
already granted on the write side; prime 2 reads, and the rest-frame
spectral projectors (I +- X)/2 need exactly the denominator 2 and nothing
else. No exponential exists in Rev 4, so no factorial denominator ever
arises; 2 and 5 are the only inverted primes. The breaker obligation BR-B
(1/2 unavoidable over Z[i]) rides the post-ANO round. Alternatives set
aside as in Rev 3 (a truncated formal family with a declared rational 1/2;
a larger cyclotomic ring): the owner may override at ANO.

## 2. The frozen coupling class: eight fields

D1 CARRIER (pointer and memory). M = M_D tensor R and nothing else: M_D
the Dirac coin, rank 2 over A', fibered over the momentum circle by the
symbol z; R = A'[Z_5], the argument register with deposit operators E_k
(E_k E_l = E_{k+l}, E_0 = 1), reference e_0. No new carrier, no third
factor, no continuum object, no ancilla outside R.
ADOPTED ROOT R-CARRIER (proposed, load-bearing): the only memory the
coupling may write is the registered argument register itself.

D2 ACTION (group-valued exact vertex; no formal strength). One joint tick
is U = (D_J(2) tensor 1) compose W with the vertex

```text
W(c_plus, c_minus) = P_plus tensor E_{c_plus} + P_minus tensor E_{c_minus},
P_plus  = (I + X)/2,   P_minus = (I - X)/2,
(c_plus, c_minus) in Z_5 x Z_5,
```

where {P_plus, P_minus} is the rest-frame spectral resolution: the
eigenprojectors of the rest step D(1) = I + 2iX, the only registered coin
frame at the electron point (the coin modulus is the rest rung). All
properties exact: W^sharp W = 1 identically (sharp is bar-transpose with
zeta -> zeta^-1, i -> -i); entries in A'; local; register-equivariant.
There is NO lambda and NO exponential: the coupling class is the FINITE
set of deposit pairs

```text
S_raw = { W(c_plus, c_minus) : (c_plus, c_minus) in Z_5^2 },  |S_raw| = 25,
(0, 0) the uncoupled tick (excluded from couplings),
```

modulo the D7 equivalences. Broadening the frame or the class is a Rev 5
event, not an evaluation choice. FLUCTUATION GRADING: the formal
bookkeeping variable t marks each completed register excursion (leaves
e_0, later returns to e_0) in the exact path decomposition of the N-tick
evolution; order t^1 means exactly one emitted and reabsorbed flux unit.
t never enters any matrix; every matrix is exact over A'.

D3 STATES (frozen here, with justification). The momentum fiber is frozen
at the rest point z = 1: the electron point is the rest rung of the
ladder, and rest is the unique fiber where the uncoupled step is the pure
coin move D(1) = I + 2iX. The pre-state coin is frozen as v_plus = (1, 1),
the eigenvector of D(1) with eigenvalue 1 + 2i (mass shell at rest;
|1 + 2i|^2 = 5 = det). The conjugate branch v_minus = (1, -1) is the bar
image of v_plus, so the branch choice is quotiented away by the D7 bar
equivalence: no physical freedom remains. Pre-state u = v_plus tensor e_0.
Born squares are normalized by the exact norm tower 5^N after N ticks
(BORN-ORDER-STAIRCASE [T] supplies the registered norm gate). All read
quantities are stationary per-tick rates, with every N to infinity
closure taken only through D6.

D4 EXTRACTION. Two responses of the same coupled stream, both stationary
per-tick rates at order t^1:

```text
moment rate    c_a := per-tick rate of delta a_e at order t^1, where
               a_e = (g - 2)/2 and the tree reading gives
               delta g = delta-theta / (pi/5), hence EXACTLY
               delta a_e = 5 delta-theta / (2 pi);
               delta-theta = the argument shift, at order t^1, of the
               e_0-component amplitude against the uncoupled reference
               (1 + 2i)^N, read through the frozen D8 reading.
channel rate   c_w := per-tick Born rate, at order t^1, of one completed
               excursion (emission tick i < reabsorption tick j), under
               the same 5^N tower.
```

K := c_a / c_w, defined only if both rates exist as exact per-tick limits
under D6 (certificate C2); K is then N-free by construction. Alpha
dictionary: the channel's own excursion weight defines alpha; one
excursion carries one alpha, so K = [alpha^1] a_e(alpha).
ADOPTED ROOT R-ALPHA (proposed, load-bearing): alpha enters as the
channel's own excursion Born rate, not as an external unit; script-Q is
not consumed by the extraction (enforced by C6), so the comparison
against J Jbar / script-Q is not circular.
Degree ledger (parametric): c_w is pi-free, so K = (2 pi)^-1 requires c_a
at pi-degree -1; the reading contributes one division by pi (the
5/(2 pi) factor), so delta-theta must land at degree 0; with n_p tick
phases (+1 each) against n_w wall rungs (+2 each, denominator), the
ledger is n_p = 2 n_w, the INFINITE family {(2m, m) : m >= 0}. The
realized m is an evaluation output; the checker certifies the family and
claims no truncation.

D5 NORMALIZATIONS (REVISED, A3 and A4). Every carrier constant lies in
A', generated only through the following named public identities:
N(J) = 1 and Tr_(K/Q)(J) = 3 (J-MAHLER-MEASURE [T]); det(I + 2iX) = 5;
the tick phase 2 pi/5 through J phi = zeta_5 (J-PROJECTIONS [T]); the
norm tower 5^N (BORN-ORDER-STAIRCASE [T]). Cite-or-drop slot: the MUB
weight 1/5 may be used only if the ANO names the v71 row that carries
it; absent that citation the constant is inadmissible. Reading
coefficients are rational over Q(sqrt5).
EXCLUDED FROM GENERATION: script-Q, phi^2-multiples of pi, and any
identity equivalent to script-Q phi^2 = 2 pi. These may appear only in
the node-5 comparison target of section 4, never in a constant entering
c_a or c_w; certificate C6 enforces this exclusion. A constant outside
these rings or generated outside these identities routes FREE-PARAMETER.
No new dimensionless normalization, anywhere.

D6 REGULARIZATION. None. Every infinite tick sum must close in finitely
many exact steps through registered summation data only: at s = 1 the
tree anchor Li_1(J) = i pi/5 (WALL-CIRCLE-LEMMA [T], the N = 5, a = 2
case); at s = 2 exactly the public WALL-LI2-RUNG [T] data:
Re Li_2(sigma_a(J)) = pi^2/100 for a in {1, 4} and 9 pi^2/100 for
a in {2, 3}, the Galois-orbit real-part sum pi^2/5 (NOT a field trace,
per the public row), the channel law 1 : 9. A quantity that does not
close routes STOP.
ADOPTED ROOT R-WALL (proposed, load-bearing): the polylogarithmic wall
is the sole admissible closure resource at its rung.

D7 EQUIVALENCE (conservative core plus quarantined automorphisms).
V ~ V' iff conjugate by a symmetry in the PROVEN core:

```text
IN            bar conjugation (zeta -> zeta^-1, i -> -i, coin
              transpose): maps W(c_plus, c_minus) to W(-c_plus,
              -c_minus) and v_plus to v_minus; preserves every Re
              reading and the wall pair {1, 4}.
IN            the exact centralizer of the uncoupled tick on M
              (computed, not assumed: certificate C1).
QUARANTINED   register automorphisms u in (Z/5)^*: E_k -> E_{u k}
              (genuine automorphisms). Their K-invariance is NOT
              assumed; the fresh break round classifies each u as
              equivalence or covariance; until classified, covariance.
OUT           field sigma_2, sigma_3 as identifications; recorded as
              covariance between Galois-twisted gates.
OUT           index shifts E_k -> E_{k+c}: not automorphisms (they fix
              neither the unit nor the product); the Rev 2 error,
              retired.
```

INCOMPATIBLE means inequivalent with different K; equal K across
inequivalent classes is value multiplicity, not incompatibility.

D8 READING (NEW, A5; frozen per POLICY.md section 4). The delta-theta
read of D4 is one typed reading with all five data frozen:

```text
domain:      the e_0-component amplitude of the coupled stream at order
             t^1, per tick, as an element of the carrier ring
codomain:    the exact argument datum in the reading ring, graded in pi
context:     the principal archimedean embedding, the uncoupled
             reference (1 + 2i)^N, the fivefold phase orientation
             zeta_5, and the D3 frozen state
equality:    exact equality in the reading ring
overlap:     the tree layer rests on ELECTRON-G-TREE [D] (g = 2 as the
             quotient of the vertex flux arg over the spinor half
             angle pi/5); this reading extends that dictionary at
             order t^1 and introduces no second inequivalent reading
             in the same context
```

The reading is selected structurally, before and independently of any
target comparison, and explains no measurement; the node-5 target is
computed only at the comparison step.

## 3. Admissibility and the class (finite)

W(c_plus, c_minus) is admissible iff (c_plus, c_minus) != (0, 0) and
both rate clauses of D4 hold. The raw class has 24 couplings; S := the
admissible set modulo the proven D7 core. C1 (the verifier's first
obligation): compute the centralizer, enumerate the class, quotient by
proven equivalences, and certify the count.

## 4. Decision rule (a sequential decision tree; disjoint by construction)

```text
node 1  definitional integrity: any clause of D1..D8 ambiguous in
        execution, or a required object fails D6 closure, or C1, C2, or
        C6 cannot be certified?         YES -> STOP        NO -> node 2
node 2  any admissible coupling needs a constant outside the D5 rings
        or identities, or K varies along a residual freedom inside one
        class?                          YES -> FREE-PARAMETER
                                        NO  -> node 3
node 3  S empty?                        YES -> NEGATIVE (empty class is
                                               a scientific negative)
                                        NO  -> node 4
node 4  all surviving classes share one K?
                                        NO  -> NONUNIQUE
                                        YES -> node 5
node 5  the shared K equals J Jbar / script-Q = (2 pi)^-1 exactly
        (QUANT-SCHWINGER-TARGET [T])?
                                        YES -> PASS
                                        NO  -> NEGATIVE
```

The tree is total and its leaves are disjoint by construction; the
checker certifies exactly one route for all condition states. All five
routes are first class; a fired route is folded and archived, never
repaired in place; no threshold moves after data.

## 5. Falsifier (carried verbatim from the public row, not new)

Fires if the frozen exact substrate coupling of the electron to the
electromagnetic argument channel yields d a_e / d alpha at alpha = 0
different from J Jbar / script-Q = 1/(2 pi), if a new free dimensionless
normalization is required, or if two admissible couplings survive with
different coefficients.

## 6. Layer surface and gates (A2: spelled to the v71 explicit-gate contract)

Neither proposed gate exists in the current 11-row `canon/GATES.tsv`.
Registration rides the owner's fold, never this draft. The two proposed
rows, in the exact public schema
`gate_id / owner_item_id / from_layer / to_layer / gate_kind /
decision_condition`:

```text
GATE-L1-L5-QS-COUPLING-STREAM   QUANT-SUBSTRATE   L1   L5   OPEN_LIFT
    emits the exact N-tick path decomposition of the coupled stream by
    excursion count only when C1 (class and centralizer) is complete;
    ambiguity or an unclosed object routes STOP

GATE-L5-L6-SCHWINGER-TERM       QUANT-SUBSTRATE   L5   L6   OPEN_LIFT
    emits K only when C2 (rates), C3 (K per class), C4 (constancy on
    classes), and C6 (script-Q non-consumption) are complete; an exact
    miss routes NEGATIVE, non-closure routes STOP
```

Both rows satisfy the v71 owner contract: the owner `QUANT-SUBSTRATE` is
an O-status obligation, both kinds are the closed kind `OPEN_LIFT`, and
both endpoint pairs are concrete and distinct. Construction lives at L1
(state algebra) and L5 (the coupled tick stream); the measure reading is
L6.

## 7. Verifier contract (build FORBIDDEN until the ANO plus a pinned PREREG)

Python standard library only; exact arithmetic only (int, Fraction,
Z[zeta_5] four-tuples, Gaussian pairs, Q(sqrt5) pairs, pi-graded ring);
no floats in any assertion; under 120 seconds; environment
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
Certificates: C1 class and centralizer; C2 per-tick rates exist and are
first order in t; C3 K per class; C4 constancy on classes; C5 the
deterministic route of section 4; C6 no constant entering c_a or c_w is
generated through script-Q or any 2 pi equivalent. Two architectures,
byte-identical stdout, at validation.

## 8. Break-round obligations for this revision (to run at draft stage)

```text
BR-A  classify u in {2, 3, 4}: equivalence or covariance, with witness
BR-B  witness that 1/2 is unavoidable for the rest-frame projectors
      over Z[i] (the D1 ring proposal is load-bearing, not convenient)
BR-C  factor-two regression: the void reading 5/pi against the correct
      5/(2 pi); Rev 4 must be immune
BR-D  tree totality fuzz over all condition states, independent code
BR-E  audit: no exponential, no factorial, no float anywhere in the
      Rev 4 tool sources
BR-F  regression: the node-5 target is computed only at the comparison
      step and appears in no constant generation path (C6 dry run)
```

## 9. What this draft does not do

No canon change, no probe, no evaluation, no computation of K, no
narrowing of QUANT-SCHWINGER-TARGET, no import of any incubation value
into a public claim, no authority by living in the project. The three
proposed roots (R-CARRIER, R-ALPHA, R-WALL), the PROPOSED-D1 ring, the
D2 vertex-class freeze, and the D8 reading freeze are exactly the
load-bearing points the owner's ANO must cover, point by point.

## 10. Ratification

The freeze happens only when the owner issues an explicit ANO against
the sha256 of this exact file, covering: (1) the ring A', (2) the vertex
class of D2, (3) the frozen z = 1 and branch of D3, (4) the extraction
of D4 with the 5/(2 pi) reading, (5) the D5 generation identities and
the script-Q exclusion, (6) the D7 core and quarantine, (7) the decision
tree, (8) the two proposed gates, (9) the D8 reading data. A partial ANO
names its exceptions and produces Rev 5. Until the ANO: no PREREG pin,
no verifier, no evaluation.
