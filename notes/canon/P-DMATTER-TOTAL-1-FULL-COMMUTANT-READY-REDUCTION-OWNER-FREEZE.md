# P-DMATTER-TOTAL-1 Full-Commutant Ready-Reduction Owner Freeze (NON-CANONICAL)

```text
STATUS:                 OWNER-ADOPTED DEFINITION RULING / BRANCH FREEZE
AUTHORITY:              NOT CANON
SCOPE:                  PROPOSAL-LOCAL / DEFINITION-ONLY
OWNER DECISION:         FULL-COMMUTANT READY REDUCTION
OWNER DECISION DATE:    2026-07-26
PHYSICAL APPARATUS:     UNRESOLVED
PUBLIC BASE:            Public Canon v23
PUBLIC CANON TAG:       canon-v23
ACTIVATION COMMIT:      4ac41b4fac3a3794a6e9d5be1e2027d324edb806
CONTENT COMMIT:         7830d852229ffc06c9d287d026c8ece290bf339b
CANON SHA-256:          f842b613d6f65fe07ddab92ddbe1fb9fec89217d52b781571b7380281c3fb2b1
CANON BYTES:            116017
PUBLIC MAIN BASE:       da3d9e53d1347f373e8edd3ddd78c44b94a43031
ROUTE A OWNER DECISION: 8ce44e09a3967f3c160ba5db632f8e36a9ee71fbb6d62c5d7aad16e1380b2cde
OD1-OD4 OWNER RULING:   0cb5d0e46d2a76d5170ac399b15626b558256984cf2d01c4029441ca0d248ca5
PROPOSAL-ID PACKAGE:    d9e10e605e937971ea56974fb1afaecf36bfc1ebad3e1ff7ed304914f208b266
INSTRUMENT PREDEFINITION:
                        1cfde364a3ad7f64730433ed142fd7cb04df6064779087f7144ffa6991918ee6
KERNEL-APPARATUS PREDEFINITION:
                        ec412acd3b4d03d17a1296d651c7c2145535b07950575bfa1cc89f410464f23c
CLAIM ISSUE:            107
A11 STATUS:             PARTIAL / O-STOP, unchanged
QDD STATUS:             O / STOP, unchanged
FORMAL RUN:             NONE
CANON CHANGE:           NONE
REGISTRY CHANGE:        NONE
DEPENDENCY CHANGE:      NONE
GATE CHANGE:            NONE
```

This ruling records one owner choice exposed by the merged kernel-apparatus
predefinition. The complete system-side admissibility condition on every
future ready-state reduction is the full commutant of the fixed low and high
effects. Reduced centrality is not adopted.

The choice is made after the proposal-local calculation of the commutant
quotient was available. It is therefore an explicit model-definition choice,
not blind evidence, a prediction, or a derived physical selection. The owner
accepts the nonuniqueness pressure of the full commutant and does not narrow
the branch to its center merely to recover the Luders candidate.

This ruling does not adopt a physical apparatus carrier, ready state, joint
composition, coupling class, pointer, physical outcome, kernel source,
kernel-to-amplitude bridge, layer, gate, history rule, sampling rule,
writeback rule, or completeness proof. It does not open a classification.

## 0. Falsification and freeze breach first

Before a physical classification opens, a submitted continuation returns
`FREEZE-BREACH / STOP` if it does any of the following without a new owner
ruling made and merged before the candidate universe is opened:

1. replaces the full-commutant ready-reduction condition by reduced
   centrality, full-joint central control, a preferred frame, or another
   system-side predicate;
2. silently adds a no-intrasector-backaction condition;
3. excludes a reduced operator only because it is not in the Luders class;
4. changes operational `Eq_instrument` to effect equality, matrix equality,
   high-sector conjugacy, apparatus-realization equality, or another
   relation;
5. identifies the fixed `low` and `high` labels or permits their swap;
6. declares an orthogonal transformation inside the high sector to be gauge
   without a separately frozen physical equivalence;
7. removes the exact reduced witness pairs
   `(E_low,P_12 E_high)` or `(E_low,R_t E_high)` from the system-side class
   in order to recover uniqueness;
8. treats the algebraic cardinality result as physical
   `NONUNIQUE(aleph_0)` before the physical apparatus image and its
   completeness are frozen;
9. fills an unresolved apparatus, source, pointer, public-ID, layer, gate,
   sampling, history, writeback, or completeness field by inference from
   this owner choice;
10. moves A11 or `QUADRATIC-DECODER-DATA` from `O / STOP`.

A future independently frozen apparatus and coupling predicate may fail to
realize some system-side class. That is not a freeze breach when the
exclusion follows from the pre-opened apparatus predicate and a complete
proof. Adding the exclusion after observing the classification is a breach.

After a physical classification opens, any change to the commutant clause,
ready-reduction scope, physical apparatus universe, apparatus equality,
ready state, joint composition, coupling, pointer, outcome semantics,
coupling-to-`K` reduction, kernel source, source bridge, physical
admissibility predicate, completeness method, classification equality,
public identifiers, layer, gate, sampling, history, writeback, dependency
closure, or output meaning returns `FIRE-POSTHOC`.

Neither `FREEZE-BREACH / STOP` nor `FIRE-POSTHOC` is a Canon or registry
scientific result.

## 1. Fixed algebraic boundary

The merged physical-instrument predefinition supplies

```text
H_Q = (Q^4, <x,y>_G = x^T G y),

G       = I_4 - (1/5) 1 1^T,
G^(-1)  = I_4 + 1 1^T,
A^sharp = G^(-1) A^T G,

E_low  = (1/4) 1 1^T,
E_high = I_4 - E_low,

Instr_alg(E_low,E_high)
  = { (K_low,K_high) in M_4(Q)^2 :
      K_a^sharp K_a = E_a for a in {low,high} }.
```

It also freezes the three distinct relations `Eq_K_matrix`,
`Eq_instrument`, and `Eq_effect`; the tagged post-event operation; and the
outcome-forgetting operation. The present ruling changes none of them.

Define

```text
C = Comm(E_low,E_high)
  = { T in M_4(Q) :
      T E_a = E_a T for a in {low,high} }.
```

The exact owner-adopted system-side class is

```text
Adm_comm
  = { (K_low,K_high) in Instr_alg(E_low,E_high) :
      K_a in C for each a in {low,high} }.
```

Equivalently, the proposal-local system-side predicate is

```text
SysAdm_comm(K_low,K_high) = TRUE
    iff (K_low,K_high) in Adm_comm.
```

`SysAdm_comm` is the complete system-side restriction at the ready-state
reduction boundary. It is not the complete physical admissibility predicate.
Independent apparatus, coupling, source, pointer, layer, gate, and
completeness conditions remain mandatory.

## 2. Meaning of full-commutant ready reduction

The adopted words have a narrow frozen meaning:

```text
READY REDUCTION
    A future physical joint realization is evaluated only after its exact
    frozen ready state and pointer events are supplied. The deterministic
    coupling-to-pointer reduction returns the labeled pair
    (K_low,K_high).

FULL COMMUTANT
    The reduced pair passes the complete system-side test exactly when each
    K_a commutes with both E_low and E_high.

NO ADDITIONAL SYSTEM-SIDE FILTER
    No center condition, preferred high-sector frame, identity action inside
    an eigensector, or full-joint control law is part of SysAdm_comm.
```

The word `full` qualifies the commutant used by the reduced system-side
predicate. It does not say that every member of `Adm_comm` has already been
realized by a physical kernel-apparatus construction.

The word `ready` limits the adopted condition to the reduced operators
obtained from the future frozen ready state. It does not constrain a joint
coupling on apparatus states outside that ready-state input unless a later
pre-opened coupling law does so independently.

## 3. Frozen classification equality and labels

The only classification relation remains

```text
(K_low,K_high) Eq_instrument (K'_low,K'_high)

iff

K_a rho K_a^sharp = K'_a rho (K'_a)^sharp
for every rho in State_G(Q) and each fixed label a.
```

The consequences are frozen:

1. `low` and `high` are fixed ordered labels. Outcome swap is not gauge.
2. `Eq_effect` audits the shadows `E_a`. It does not classify instruments.
3. `Eq_K_matrix` is finer than operational instrument equality and does not
   replace it.
4. Multiplication of either labeled `K_a` by an independent
   `epsilon_a in {+1,-1}` does not change that event operation.
5. High-sector orthogonal conjugacy or frame change is not an adopted
   physical gauge.
6. Equality of apparatus realizations, when later defined, is distinct from
   `Eq_instrument`.
7. The five Route A global decoder classes are a different classification
   problem. They are not multiplied into, quotiented with, or used as gauge
   for the instrument classes.

Any later physical outcome IDs must map by a frozen total bijection to the
two fixed algebraic labels. The strings `low` and `high` do not become
physical detector identifiers through this ruling.

## 4. The future physical universe

Let `AppPhys` denote a future complete physical apparatus-realization
universe, with all required ready, joint, coupling, pointer, source, layer,
gate, history, and dependency fields frozen. Let

```text
Reduce :
    AppPhys -> Instr_alg(E_low,E_high)
```

be its future deterministic exact coupling-to-pointer reduction. Then the
physical instrument universe governed by this ruling has the form

```text
PhysInstr
  = Image(Reduce | AppPhys) intersect Adm_comm.
```

The overall physical admissibility predicate must therefore contain two
separate factors:

```text
AppAdm(realization)       apparatus, coupling, source, and routing test;
SysAdm_comm(Reduce(...))  adopted system-side test.
```

This ruling freezes the second factor only.

Before classification, a complete candidate must prove:

```text
1. AppPhys is an exact set with a decidable membership test;
2. its equality is frozen;
3. Reduce is total and equality-compatible on AppPhys;
4. every reduction satisfies the instrument and Born certificates;
5. Image(Reduce | AppPhys) is classified completely;
6. the intersection with Adm_comm is exact;
7. the quotient by Eq_instrument is complete.
```

Failure to prove any item returns `STOP`. A hand-selected list of reduced
matrices is not a completeness proof.

## 5. Exact known consequence and its limit

The merged kernel-apparatus predefinition proves

```text
C
  = E_low M_4(Q) E_low direct-sum E_high M_4(Q) E_high
  isomorphic to M_1(Q) direct-sum M_3(Q).
```

Every member of `Adm_comm` has

```text
K_low  = V_low E_low,
K_high = V_high E_high,
```

where `V_low` is orthogonal on the one-dimensional low sector and `V_high`
is rational `G`-orthogonal on the three-dimensional high sector.

The quotient

```text
Adm_comm / Eq_instrument
```

has exactly cardinality `aleph_0`. Countability follows from rational matrix
entries. Infinitude is certified by the exact Householder family

```text
u_t = (1,-1,t,-t)^T,
R_t = I_4 - u_t u_t^T / (1+t^2),
t in Z, t >= 2,

K_low^(t)  = E_low,
K_high^(t) = R_t E_high.
```

The frozen name of this exact consequence is

```text
COMMUTANT-ALEPH0-ALGEBRAIC.
```

Its status remains conditional algebra at the adopted system-side branch.
It is not physical `NONUNIQUE(aleph_0)`, because this ruling does not prove

```text
Image(Reduce | AppPhys) = Adm_comm.
```

If a later pre-opened complete apparatus construction proves that equality,
the physical quotient returns `NONUNIQUE(aleph_0)`. If its exact image is a
proper subset, the physical classification is the quotient of that proper
image intersected with `Adm_comm`. In neither case may the system-side
predicate be narrowed after the result.

## 6. Explicit non-adoptions

This ruling does not adopt any of the following:

```text
apparatus carrier                       Q^2, Q^3, or another carrier
apparatus coefficient object            UNRESOLVED
apparatus equality and pairing           UNRESOLVED
ready semantics                          UNRESOLVED
ready state and value                    UNRESOLVED
joint composition                        tensor product or another rule
joint equality and embeddings            UNRESOLVED
coupling type and class                  UNRESOLVED
coupling map and preservation law        UNRESOLVED
reversibility, unitarity, or involution  NOT ADOPTED
weak or full-joint QND                   NOT ADOPTED
full-joint central control               NOT ADOPTED
ready-reduced centrality                 NOT ADOPTED
pointer carrier and events               UNRESOLVED
physical outcome IDs                     UNRESOLVED
kernel source and source domain          UNRESOLVED
kernel-to-amplitude bridge               UNRESOLVED
coupling-to-K reduction implementation   UNRESOLVED
apparatus-realization universe           UNRESOLVED
apparatus-realization equality           UNRESOLVED
physical completeness proof              UNRESOLVED
physical instrument and effect IDs        UNRESOLVED
physical Born-pairing ID                  UNRESOLVED
MatterData outcome fields and maps        UNRESOLVED
layer assignments                         UNRESOLVED
public gate bindings                      UNRESOLVED
sampling                                  UNRESOLVED
history update                            UNRESOLVED
apparatus writeback                       UNRESOLVED
completion-wide terminality               UNRESOLVED
```

The proposal-local amplitude carrier `Q^2`, ready vector `f_low`,
conditional dilations, and weak-QND counterexample remain exact decision
inputs from the predefinition. The reduced witness pairs
`(E_low,P_12 E_high)` and `(E_low,R_t E_high)` likewise remain exact
system-side inputs. None becomes physical merely because the system-side
branch is adopted.

The existing Route A map `beta` and its anchored pre-update convention remain
proposal-local definition content. This ruling does not declare that map to
be the physical kernel-to-apparatus source bridge or infer its layer
endpoints and public gate.

The existing stage-local statement

```text
feeds_U = FALSE
```

for `D_scoped` remains unchanged. It does not choose the apparatus
`writeback_manifest`, prove completion-wide terminality, or close
`OBSERVER-WRITE-PORT`.

## 7. Remaining owner axes

The following independent owner decisions remain open:

```text
APPARATUS READY SEMANTICS
    READY-IN-ONE-OUTCOME
    NEUTRAL-READY-DISTINCT-FROM-OUTCOMES
    NEITHER / REDEFINE

COUPLING TYPE
    READY-DOMAIN ISOMETRY
    FULL REVERSIBLE JOINT EVOLUTION
    IRREVERSIBLE TYPED COUPLING
    NEITHER / REDEFINE

PHYSICAL SOURCE
    exact kernel source and domain
    exact bridge into the amplitude carrier
    source and target layers
    one public gate row for every cross-layer map

HISTORY AND FEEDBACK
    no sampling
    sampled terminal history only
    typed writeback
    NEITHER / REDEFINE.
```

The system-side axis is no longer open:

```text
SYSTEM-SIDE ADMISSIBILITY
    FULL-COMMUTANT READY REDUCTION    OWNER-ADOPTED
    READY-REDUCED CENTRALITY          NOT ADOPTED
    FULL-JOINT CENTRAL CONTROL        NOT ADOPTED
    KERNEL-DERIVED DIFFERENT PREDICATE NOT ADOPTED
    NEITHER / REDEFINE                NOT ADOPTED.
```

A future owner may replace the branch only through a separate pre-opening
ruling that explicitly supersedes this file. It cannot be replaced inside a
classification result.

## 8. Frozen output semantics

```text
OWNER-BRANCH-FROZEN
    The system-side admissibility predicate is exactly SysAdm_comm.
    This is the output of the present ruling.

FREEZE-BREACH
    A continuation changes or evades the adopted system-side predicate or
    its classification equality before classification. The continuation
    returns STOP.

OWNER-INPUT-REQUIRED
    At least one independent apparatus, ready, coupling, pointer, source,
    public-ID, layer, gate, sampling, history, writeback, dependency, or
    completeness field remains unresolved. This remains the current physical
    output.

READY-FOR-CLASSIFICATION
    Every field in the merged kernel-apparatus schema has a legal frozen
    value and the physical universe, equality, reduction, dependency
    closure, and completeness proof are exact. This ruling does not reach
    that state.

PASS, NONUNIQUE(k), EMPTY
    Retain the meanings frozen in the kernel-apparatus predefinition and
    become available only after READY-FOR-CLASSIFICATION.

STOP
    Any required value, type, equality, public identifier, map, certificate,
    layer, gate, dependency, or completeness proof is missing or inexact.

FIRE-POSTHOC
    Any frozen input or output meaning changes after classification opens.
```

The current combined output is

```text
OWNER-BRANCH-FROZEN
OWNER-INPUT-REQUIRED / STOP.
```

## 9. Exact status consequence

```text
FULL-COMMUTANT READY REDUCTION     OWNER-ADOPTED DEFINITION RULE
system-side admissibility axis     FIXED, proposal-local
ready-reduction-only scope         FIXED
Eq_instrument                      FIXED, unchanged
low/high label order               FIXED, no swap
reduced centrality                 NOT ADOPTED
full-joint central control         NOT ADOPTED
COMMUTANT-ALEPH0-ALGEBRAIC         EXACT CONDITIONAL CONSEQUENCE

physical apparatus universe        UNRESOLVED
physical kernel source and bridge  UNRESOLVED
physical reduction image           UNRESOLVED
physical completeness              UNRESOLVED
READY-FOR-CLASSIFICATION           NO
physical NONUNIQUE(aleph_0)        NOT EARNED

A11                                 PARTIAL / O-STOP
QDD-PHYSICAL-EFFECT-SELECTION      O / STOP
QUADRATIC-DECODER-DATA             O / STOP, unchanged
formal scientific run              NONE.
```

No theorem, derived dictionary, physical uniqueness, physical nonuniqueness,
Canon claim, registry row, dependency, gate, probe, verifier, evidence, or
status move is produced by this owner ruling.

## 10. Next allowed actions

1. Predefine one complete apparatus-ready-coupling-pointer package without
   changing `SysAdm_comm`.
2. Freeze the physical kernel source and bridge independently of the desired
   instrument quotient.
3. Assign every object and map an exact layer and every cross-layer map a
   public gate.
4. Choose and type the sampling, history-update, and writeback variants.
5. Prove apparatus-universe membership, reduction totality, dependency
   closure, and classification completeness before opening a classification.
6. Keep `COMMUTANT-ALEPH0-ALGEBRAIC` visibly separate from any future
   physical result.

No formal probe or Canon fold is authorized by this ruling.
