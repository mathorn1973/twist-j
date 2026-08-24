# G0 INVENTORY: DRAFT-PREREG-C-WEIL-GRAM-TOWER-1 against the REV2 gates

```
Status     NON-CANONICAL inventory. Gates nothing, freezes nothing, edits
           no file of the draft or the handoff repo. Input to the owner's
           ANO-7 decision, per the deferral recorded in
           NOTE-RH-DECODER-CLASSIFICATION_2026-08-12.md (REV2), section 7,
           D-A. Owner directive: "pust G0".
Date       2026-08-12
```

## 0. Pins

The draft was located and read on the owner's machine (macOS arm64 leg node):

```
FILE   DRAFT-PREREG-C-WEIL-GRAM-TOWER-1.md, 8447 bytes
SHA256 1c252eaf88561061e019cb30542d4d4f46548cfe2d048856852a55f2e0107eaf
COPIES /Users/user/rh/night-2026-08-12/ and
       /Users/user/rh/twistj-handoff/weil-tower-2026-08-12/
       byte-identical (same SHA-256)
GIT    twistj-handoff, branch handoff/weil-tower-recon-20260812, in sync
       with origin; last commit touching the draft 7b1ace9 ("rank
       diagnosis tested: mechanism confirmed, counting rule softened, U3
       refuted, sigma closed"). The draft text already contains the
       amended U1/U2/U3 block, so the read copy is current with 7b1ace9.
ALSO   WEIL-TOWER-STATUS.md head read (recorded line: U3 premise refuted,
       sigma closed, T_eff measured per block).
```

Public authority, rerun earlier this session from a fresh clone: Public
Canon v45 ACTIVE, tag canon-v45, content commit cbd24827..., SHA256SUMS 5
of 5. Checked for this inventory: SPLIT-PRIME-RAPIDITY-CLASS [T] is alive
at v45, SPLIT-PRIME-RAPIDITY-INDEPENDENCE [T] and
REDUCED-SPLIT-GENERATOR-HEIGHT [T] are present, probe P-ARITH-RAPIDITY-1
exists. So every row the draft's BASIS cites survives at v45; only the
version pin is stale.

## 1. The five G0 items, one by one

### Item 1: input class E and Mor(E)

STATE: frozen as a finite MENU, not as a class. The five block recipes
(zeta, chi5, xi_0..xi_6, DH-, DH+) are exact and complete: conductor,
gamma factor, polar terms, coefficient recipe per block, ideal census for
the tower, true -f'/f by divisor recursion for the guard. No axiomatized
Euler input type is declared, and no morphisms. One morphism-level fact is
nevertheless present and validated: the channel decomposition
B[xi_0] = B[zeta] + B[chi5] (V3, exact to 2.8e-16).

FINDING: for a readout prereg this is legitimate, but it must say so.
FIX (declaration P1): one scope sentence: this prereg tests instruments on
a frozen finite menu; the classification axis of the decoder frame (the
category E, its morphisms, decoder equivalence) is out of scope and
untested here. That sentence prevents any later reading of the run as a
classification result.

### Item 2: directed family of test spaces and inclusions

STATE: partial. The carrier V_{N,K} is frozen exactly (phi-lattice times
circle modes, l = log phi, t_kappa = pi kappa / l), R1 reads nested
(N', K) sections, and U1 supplies an admissible-section predicate with
measured T_eff per block and a declared 15 to 20 percent soft edge
(honest headline N = 6 at rank efficiency 0.94). What is not declared:
the inclusion maps and the direction of the family.

FIX (declaration P2): one paragraph: j is the basis inclusion
e_{m,kappa} -> e_{m,kappa}; the directed family runs in N at fixed K, the
K series is reported as separate series; U1 is the definition of an
admissible section, and a section violating it is a declared-inefficiency
diagnostic, never a headline. This is the finite-stage shadow of the G5
coherence data (j_RS exists; A and U do not, and are not claimed).

### Item 3: equality notion

STATE: frozen at the linear-algebra layer, GAP at the entry layer. Frozen
and good: exact prime side (compact support truncates exactly at
phi^(2N)), exact closed-form tail, PROP-2b interval-refinable phases (no
exact finite phase model, correctly consumed), U2 interval LDL^T as the
ONLY sign rule with the triple (certainly negative, undecided, certainly
positive) and the undecided dimension reported, never pushed.

THE GAP, and it is the one substantive blocker: the archimedean entries
come from Gauss-Legendre 80-node quadrature with kink-aware subdivision,
and no certified remainder bound is stated. Interval LDL^T on
uncertified entries certifies nothing: the enclosure chain must start at
the matrix entries. V1..V4 are validations at float tolerances (5e-4,
5.5e-2, 2.8e-16, 4.7e-15), which is fine for recon and is not a
certificate chain.

FIX (blocker B2), either arm: (a) specify enclosure-grade entries,
interval quadrature with a stated remainder bound on each analytic piece,
tail already closed-form; then R4's DH inertia becomes a genuine
certificate. Or (b) keep the pipeline and downgrade every occurrence of
"certified" to "float readout with an interval final step". Arm (a) is
what makes the run's prize real; see section 3.

### Item 4: decoder equivalence relation

STATE: absent, and correctly absent: the draft constructs no A, claims no
constructor, and G6 is named elsewhere as the main prize. G5/G6 are
untouched by design.

FIX: covered by the same scope sentence as item 1 (P1). Nothing else
needed. Demanding the equivalence relation from this draft would be gate
theater.

### Item 5: counterfeit battery

STATE: present and strong. DH- and DH+ at the SAME (N, K) as the tower,
separation read inside one carrier; type-closed guard doctrine (the
guard is DH's OWN Weil form from the true -f'/f by divisor recursion,
the linear 2x2 combination shortcut explicitly excluded); the Euler gate
c_4 < 0, c_6 != 0 reported exact (R4); the prime-power-only DH shell as
the Euler-locality contrast (R5).

FINDING, positive: the draft already contains the G8a named obstruction
in substance. "c_6 != 0 at a non-prime-power" IS the multiplicativity
violation in log-derivative coordinates: for any Euler product the
coefficients of -L'/L are supported on prime powers, so a nonzero c_6 is
an exact, named, Euler-local witness that the object is not Euler, and
c_4 < 0 is the companion positivity violation. The D-D one-pager of the
REV2 note does not need a new computation; it needs one lemma naming
this readout as the G8a witness.

Epstein: not in the battery. Per REV2 this stays [O] (freeze one object
with citation before public use) and is NOT a blocker for this freeze.
G8b (an admitted Euler member with certified positivity failure): no
known inhabitant, the draft honestly does not pretend one; stays [O].

## 2. The basis pin (outside the five items, first in importance)

BLOCKER B1: the BASIS block cites Public Canon v44. Public authority is
v45 since today, verified in-session. All cited rows survive at v45, so
nothing breaks; the fix is a re-pin paragraph (v45 tag, content commit,
canon hash), and the same fix applies to WEIL-TOWER-STATUS.md, which
still says "PUBLIC CANON unchanged (v44)". A candidate frozen against a
stale basis is dead on arrival by Step 0; this is the cheapest and most
mandatory fix on the list.

BONUS of the re-pin, not just hygiene: v45 adds
SPLIT-PRIME-RAPIDITY-INDEPENDENCE [T] (the addresses are genuinely
independent, the carrier is an infinite-rank coordinate system, which is
the structural reason the xi_k tower is a basis and not a degeneracy)
and REDUCED-SPLIT-GENERATOR-HEIGHT [T] (a canonical reduced
representative exists). Together with V5 evenness (the construction
consumes only even functions of theta_p, no section of the unit action
enters), ending E1 gets a sharper reading: the trigger is doubly
defused, structurally by evenness and in reserve by the canonical
representative. Keep the ending; note the defusal.

## 3. REV2 alignment beyond G0, in three sentences

G7: the U2 triple is exactly the finite-stage discipline of the typed
readout, UNDECIDED reported, never pushed; the draft asserts no BRIGHT
anywhere ("PSD blocks are consistent with GRH and say nothing more"),
which is correct. The run's prize, stated in REV2 language: with B2 arm
(a), this run delivers the first CERTIFIED DARK WITNESS w for DH inside
the tower's own carrier family, which is the certificate-grade execution
of G8 the classification frame needs. Optional and cheap while the
engine is open (D-C of the REV2 note): a readout R9 reporting the
factorization-coherence defect across nested sections (LDL factors at
section R do not extend along j to section S; record the defect), exact
at small N; it is the measured demonstration of the headline sentence,
finite PSD is not a result.

## 4. Verdict

```
BLOCKERS BEFORE FREEZE (2)
B1  re-pin BASIS to Public Canon v45 (and the lane STATUS page with it);
    rows alive, one paragraph, mandatory by Step 0.
B2  entry-layer certification: interval quadrature with stated remainder
    per analytic piece (arm a), or downgrade the word certified (arm b).
    Arm a is worth the cost: it converts R4 from readout to certificate.

DECLARATIONS BEFORE FREEZE (3, one paragraph each)
P1  scope sentence: finite frozen menu; classification axis out of scope.
P2  directed family declared: j = basis inclusion, direction N at fixed
    K, U1 as the admissible-section predicate.
P3  name the G8a witness: R4's Euler gate is the named Euler-local
    obstruction (multiplicativity violation in log-derivative
    coordinates); one lemma, no new computation (D-D).

NOT BLOCKERS
Epstein object [O]; G8b inhabitant [O]; optional R9 coherence readout;
the equivalence relation (correctly out of scope).
```

With B1, B2 and P1..P3 the freeze of DRAFT-PREREG-C-WEIL-GRAM-TOWER-1
under the REV2 gates is coherent and ANO-7(a) becomes decidable. Without
B2 the freeze would carry the word certified on uncertified entries, and
endings E4 and readout U2 would be softer than their text claims. The
draft is otherwise closer to the REV2 frame than expected: the four
frozen endings, the type-closed guard, U1's measured section rule and
U2's triple readout are already the right shapes.
