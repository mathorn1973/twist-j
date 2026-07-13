# P-SPIN-LIFT-FORCED-1: Owner Ruling (NON-CANONICAL)

```text
Program:          SPIN-LIFT-FORCED
Probe:            P-SPIN-LIFT-FORCED-1
Track:            B
Owner:            unchanged, single owner
Date:             2026-07-13
Basis:            Public Canon 1, tag canon-v1, activation commit
                  f4fb064c2a08cd21b9a2bc2bcfd4daf46da47bcb
Status:           RULING CANDIDATE, NON-CANONICAL UNTIL MERGED AND PINNED
Scientific claim: remains O
Action layer:     L3
Public record:    mathorn1973/twist-j issue 12 (decisions and probe claim)
Supersedes:       ruling draft SHA-256
                  fe635c65a9da24f37e3a0170ea049b586974c05270c8358765a968fd11955042
                  (7420 bytes, 259 lines) and candidate SHA-256
                  9856ff9f7c3283ed007cfe3c6af5ddb5fdec7db28dcb28504440a018b1e58127
                  (13506 bytes, 395 lines)
Incorporates:     track B review SHA-256
                  15aa55b989bc3c7b3119fa692c42bd18860ba80c5db0cd08785a45cedbb0b5a9
                  and the owner byte review of candidate 9856ff9f
                  (2026-07-13, blocker B2 and freeze fixes)
```

## 0. Decision

The readiness audit is accepted. The probe was correctly stopped before
preregistration. The earlier public wording conflates two different typed
objects:

1. the two-element readout ensemble `P2 = {e, s}`, called the axiom pair in
   the color witness, and
2. the marked generator pair of the return group `D5`, required to state a
   dicyclic group lift.

The uniqueness probe concerns item 2. Item 1 is renamed the `P2 axiom-measure
ensemble` and is not the base object of this probe.

Amended per the owner decisions recorded in issue 12: blocker B1 is resolved
by the procedural witness of section W; route decision R1 is resolved as
route a (section 3); the track B review recommendations are incorporated
below. Further amended per the owner byte review of candidate 9856ff9f:
the conjugation relation carries no sign choice (blocker B2, see D3 and D5),
and the naming, witness map, and provenance wording are frozen accordingly.

No track exchange is authorized. Track B remains the sole owner of
`P-SPIN-LIFT-FORCED-1`.

## 1. Falsifier first

Let `N` be the number of admissible lift classes under the equivalence relation
in D4, after all integrity gates pass.

```text
PASS:  N = 1
FAIL:  N >= 2
STOP:  the pinned public witness of section W is absent from the admissible
       set, or any declared group, map, relation, or exact count fails its
       integrity gate
```

`STOP` is an invalid probe execution, not a scientific result.

## 2. D1 to D6 rulings

### D1. Base pair

For `SPIN-LIFT-FORCED`, the phrase `axiom pair` means the marked ordered
loop-generator pair

```text
(r, s) in D5,
r^5 = e,
s^2 = e,
s r s^-1 = r^-1.
```

The element labels are those of the exact `COLOR-RETURN-D5` presentation:
`r = ('rot', 1)` and `s = ('ref', 0)`.

Census anchor: the marked pair is a census word, not a labeling convention.
In the pinned witness source (section W), `s_ = Dtab` and
`r = compose(Dtab, beb)` with `beb = compose(Btab, compose(Etab, Btab))`;
the file's composition convention applies the right factor first (source
line 100), so

```text
s = d,
r = d o (b o e o b).
```

The source assigns `('rot', a) = r^a` and `('ref', a) = r^a s` (lines 119 to
122) and publicly checks `r^5 = e`, `s^2 = e`, `s r s = r^-1`,
`b e b = ('ref', 4)`, and `b b = e` (lines 124 to 128, gate at line 139).

The witness ensemble `P2 = {e, s}` is henceforth called the `P2 axiom-measure
ensemble`. It is outside the candidate object of this probe. Its full preimage,
section, Plancherel mass, and edge-module readout are not admissibility
conditions for `P-SPIN-LIFT-FORCED-1`.

### D2. Declared cover

Define

```text
G       := SL_2(F_5) = 2I,
Z       := {I, -I},
Gbar    := G / Z = PSL_2(F_5),
pi      : G -> Gbar,       pi(g) = gZ = {g, -g}.
```

The kernel is exactly `Z`.

The downstairs copy of the return group is not fixed by a first-found matrix
pair. A candidate includes a monomorphism

```text
iota : D5 -> Gbar.
```

All such monomorphisms are enumerated. Identification with
`COLOR-RETURN-D5` is by the marked presentation in D1 and by direct relation
checks. An order profile alone is not an identification.

The electron closure pair `(5, 10)` is not a second cover. It supplies the
central fifth-power import in D3 and D5.

### D3. Admissibility predicate

An admissible lift is a triple

```text
(iota, R, S)
```

with `iota : D5 -> Gbar` a monomorphism and `R, S in G`, satisfying all of the
following exact conditions:

```text
A1  pi(R) = iota(r)
A2  pi(S) = iota(s)
A3  R^5 = -I
A4  S^2 = -I
A5  S R S^-1 = R^-1
A6  <R, S> = pi^-1(iota(D5))
A7  |<R, S>| = 20
```

Choice attribution, binding for the prereg rationale:

```text
A3  the single imported membership choice, resting on
    ELECTRON-G-DOUBLE-COVER; both central fifth-power values are realized
    in G by the pinned class data, and the import selects -I.
A4  entailed by A2 with the unique involution of the core
    (COLOR-GOLDEN-TABLE): S is noncentral because pi(S) is not the
    identity, and a noncentral solution of S^2 = I would be a second
    involution. Retained as an integrity gate.
A5  entailed by A1 to A3, an integrity gate: transport through pi allows
    only S R S^-1 in {R^-1, -R^-1}, and A3 empties the minus branch,
    since (S R S^-1)^5 = S R^5 S^-1 = -I while (-R^-1)^5 = I. There is
    no conjugation sign choice (see D5).
A6  entailed by A1 to A3, an integrity gate: pi(<R, S>) = iota(D5), and
    R^5 = -I puts the central element in <R, S>, so <R, S> is the full
    preimage of order 20. Carries the dicyclic content.
A7  entailed by A6: the preimage of a group of order 10 under the central
    two to one quotient has exactly 20 elements. Retained as an integrity
    gate.
```

The named public dependencies are:

```text
COLOR-RETURN-D5          D1 and the downstairs relations
COLOR-CORE-2I            G, Z, and the central quotient
COLOR-GOLDEN-TABLE       Dic_5 closure and order-4 reflection lifts
ELECTRON-G-DOUBLE-COVER  the 5-to-10 central sign import R^5 = -I
```

No character value, Plancherel mass, edge-module readout, or magnetic-face
measure is added to this predicate. Those are downstream readings, not
membership rules for this algebraic lift probe.

### D4. Equivalence modulo conjugation

Two admissible triples `(iota, R, S)` and `(iota_prime, R_prime, S_prime)` are
equivalent if and only if there exists one `g in G` such that

```text
R_prime    = g R g^-1,
S_prime    = g S g^-1,
iota_prime = c_pi(g) o iota,
```

where `c_pi(g)(x) = pi(g) x pi(g)^-1` in `Gbar`.

The pair is conjugated jointly. Conjugation by the dicyclic subgroup alone is
not the relation; the full group `G = 2I` acts. The `iota` transport clause is
entailed on generators by A1 and A2 and is retained as an integrity gate.

### D5. Central sign convention

The central relation `R^5 = -I` is an imported membership condition
(ELECTRON-G-DOUBLE-COVER), not an output. The central relation `S^2 = -I` is
entailed (D3, A4) and stands as an integrity gate.

The conjugation relation carries no independent central sign. Transport
through pi allows only `S R S^-1` in `{R^-1, -R^-1}`, and A3 empties the
minus branch: `(S R S^-1)^5 = S R^5 S^-1 = -I`, while `(-R^-1)^5 = I`. So
`S R S^-1 = R^-1` holds for every admissible triple, and A5 is an integrity
gate entailed by A1 to A3, not a choice. The apparent third central sign
flagged in earlier review rounds was false and is retired here, before the
freeze. The only central choice anywhere in the predicate is the A3 import.

Independent central retwists are not identified by convention. In particular,
`(iota, R, S)` and `(iota, R, -S)` count as distinct unless D4 proves that
they are jointly conjugate in `G`.

The dependency of `SPIN-LIFT-FORCED` on `ELECTRON-G-DOUBLE-COVER` is recorded
by this ruling; the `DEPENDENCIES.tsv` row is deferred to the future
normative fold (section 3).

### D6. Relabeling rule

There is no additional quotient by base relabeling. The pair `(r, s)` is
marked and ordered.

Automorphisms such as

```text
r -> r^a,
s -> r^b s
```

are not silently identified. They are identified only when their effect is
already realized by the simultaneous conjugation relation D4.

A full `Aut(D5)` quotient would answer the different question of unmarked
subgroup-lift uniqueness. That is not this probe.

### W. The pinned public witness (procedural)

Source pin:

```text
source commit:   f4fb064c2a08cd21b9a2bc2bcfd4daf46da47bcb
source file:     reproduce/color-ladder/verify.py
source SHA-256:  5cd3a40c66a6d2b6ca30ffc600d0ca13ebf1f2c7743a21e2bc56d6f572a1ebd8
```

Derivation, self contained and deterministic:

```text
1  Order the elements of G = SL_2(F_5) lexicographically by the row major
   entry tuple (a, b, c, d), entries 0 to 4, for the matrix ((a, b), (c, d)).
2  z = -I, so Z = {I, z}.
3  R_w is the first matrix of exact multiplicative order 10.
4  S_w is the first matrix, in the same order, satisfying
   S_w R_w S_w^-1 = R_w^-1.
5  pi(g) = gZ = {g, zg}.
6  The marked base pair downstairs is the census pair of D1:
   s = d, r = d o (b o e o b).
7  iota_w(r) = pi(R_w), iota_w(s) = pi(S_w).
8  Totalization: iota_w(r^a) = pi(R_w)^a and
   iota_w(r^a s) = pi(R_w)^a pi(S_w), for a = 0 to 4, on the element
   labels of D1, so iota_w is a fully defined map on all ten elements.
```

The witness triple is `(iota_w, R_w, S_w)`. The derivation uses only the
declared order, never the internal iteration order of the source file; the
source pin fixes the group model and the public relation anchors. The STOP
clause of section 1 is therefore decidable with no run before the
preregistration pin.

Integrity notes: exact order 10 entails `R_w^5 = -I` through the unique
involution, so the witness meets A3 by construction; `S_w` satisfies A5 by
step 4. The verifier must reconstruct the witness by this exact procedure
and assert its admissibility.

## 3. Public pin route (route a) and deferred normative edits

Per the owner decision recorded in issue 12, route a applies.

### 3.1 The only pre-preregistration public artifact

This ruling file, added by one standalone pull request:

```text
branch: notes/P-SPIN-LIFT-FORCED-RULING-1
path:   notes/canon/P-SPIN-LIFT-FORCED-RULING-1.md
```

The pull request adds exactly this NON-CANONICAL file. It must not change the
Canon, the registry, the dependency table, or `SHA256SUMS`. Public Canon 1
remains immutable through the probe.

The public ruling pin, recorded after merge:

```text
ruling merge SHA on main
ruling file SHA-256
ruling bytes
ruling lines
```

`PREREG.md` and `verify.py` may be frozen only after this pin exists, and
they cite it.

### 3.2 Deferred normative edits (future integer Canon fold)

The following are agreed content of a separate future integer-numbered Canon
fold. They are not preconditions of the probe; the probe pull request changes
only its own probe directory.

Registry rescope of `SPIN-LIFT-FORCED`:

```text
scope:
uniqueness of the marked D5 loop-generator-pair lift through
pi : SL_2(F_5) -> PSL_2(F_5), under simultaneous conjugation in SL_2(F_5)

falsifier:
closes positively when the admissible triples defined by the pinned owner
ruling form exactly one simultaneous-conjugacy class; closes negatively when
a second class survives the same frozen constraints
```

The claim status remains `O`.

Dependency rows, retaining the existing `DEF-ARCHITECTURE` edge:

```text
SPIN-LIFT-FORCED  COLOR-RETURN-D5          REQUIRES  marked downstairs D5 presentation
SPIN-LIFT-FORCED  COLOR-CORE-2I            REQUIRES  cover group and center
SPIN-LIFT-FORCED  COLOR-GOLDEN-TABLE       REQUIRES  dicyclic and order-4 lift constraints
SPIN-LIFT-FORCED  ELECTRON-G-DOUBLE-COVER  REQUIRES  central 5-to-10 sign constraint
```

Canon clarification sentence, after the current Rung 5 wording:

```text
For SPIN-LIFT-FORCED, the lifted object is the marked ordered D5
loop-generator pair (r, s); the P2 ensemble {e, s} is a downstream
axiom-measure ensemble and is not the base pair of the uniqueness probe.
```

## 4. Preregistration consequences

After this ruling is merged and pinned, Track B may freeze `PREREG.md` and
`verify.py` with these non-negotiable fields:

```text
Layer:              L3
Carrier:            finite groups D5, SL_2(F_5), and PSL_2(F_5)
Arithmetic:         exact integers modulo 5 only
Candidate object:   triples (iota, R, S)
Observable:         number N of D4 equivalence classes
Integrity gate:     the section W witness belongs to the admissible set,
                    reconstructed by the section W procedure
PASS threshold:     N = 1
FAIL threshold:     N >= 2
Stop rule:          no change to D1 through D6 or W after the remote pin
Total matrix order: lexicographic on the row major entry tuple (a, b, c, d),
                    entries 0 to 4
Canonical class rep: the lexicographic minimum of the class under that order
Output discipline:  every printed sequence sorted; no set or dict iteration
                    order reaches any print path
```

The verifier shall print, in deterministic order:

```text
number of monomorphisms iota
number of raw admissible triples
orbit-size multiset under G conjugation
number N of equivalence classes
representative matrices for every class (canonical representatives)
stabilizer size for every representative
A5 integrity confirmation for every class representative
central-retwist pairing table
all integrity-gate results
```

`iota` is derivable from `(R, S)` through A1 and A2; the verifier may
enumerate pairs and derive `iota`, keeping the triple as the typed statement
and checking that the derived map is a monomorphism as an integrity gate.

No candidate enumeration is authorized before the preregistration and code
are remotely pinned.

## 5. Status after this ruling

```text
Readiness audit:        PASS
Track B review:         INCORPORATED (SHA-256 15aa55b9)
Owner byte review:      CHANGES REQUIRED on 9856ff9f; applied in this revision
B1 witness:             RESOLVED, procedural (section W)
R1 route:               ROUTE A (issue 12)
Current probe state:    RULING CANDIDATE READY FOR PULL REQUEST
Probe claim:            recorded in public issue 12
Scientific obligation:  O
Track ownership:        B, unchanged
Track exchange:         NO
PREREG.md:              not yet authorized (awaits the public ruling pin)
verify.py:              not yet authorized (awaits the public ruling pin)
Computation:            NOT STARTED
Result:                 NONE
```
