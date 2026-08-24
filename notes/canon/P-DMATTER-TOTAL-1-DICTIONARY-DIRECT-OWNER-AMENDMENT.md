# P-DMATTER-TOTAL-1 DICTIONARY-DIRECT owner amendment (NON-CANONICAL)

```text
STATUS:                    OWNER-ADOPTED DEFINITION / NOT CANON
AUTHORITY:                 NO NORMATIVE AUTHORITY
PUBLIC BASE:               faa2ae4101200ae5561cdda53231cd79b9aec893
PUBLIC CANON:              Public Canon v36 / canon-v36
PUBLIC CONTENT COMMIT:     df64035f6f0cadbeb17f539eaeec5d8d0f444515
PUBLIC CANON SHA-256:      c8f50d0ce4686d7eedc11599a95debee15c71a2cf13c52c93c3f0605890fa2d5
PUBLIC CANON BYTES:        175814
CLAIM ISSUE / COMMENT:     107 / 5193561215
OWNER DECISION:            ADOPT ROUTE A, DICTIONARY-DIRECT
FORMAL RUN:                NONE
PROBE / PREREGISTRATION:   NONE
CANON / TABLE CHANGE:      NONE
QDD STATUS:                O / STOP, unchanged
```

This note records one owner amendment for the prospective
`QUADRATIC-DECODER-DATA` completion package. It adopts the already proved
cyclotomic realization as the proposal-local direct write dictionary. It does
not claim an independent prior readout, an independent confirmation, a blind
result, a completed decoder, or a public status change.

## 1. Exact owner decision

The owner selects Route A from the fork stated in
`P-DMATTER-TOTAL-1-CYCLOTOMIC-REALIZATION.md` and in the adversarial review of
PR #273.

```text
ADOPT:
    beta_QDD -> iota_B0 -> R_cyc
    as the proposal-local QDD direct write dictionary.

CLASSIFY:
    the cyclotomic presentation as definitionally separate;
    the equality with the factor/Born route as an already derived theorem;
    any finite sweep as conformance or implementation auditing only.

REPLACE:
    the requirement that DIRECT-WRITE be a genuinely independent prior
    readout or an independent scientific confirmation.
```

The replacement is narrow. It amends only section 8 and the terminal
`NEXT ORDERED REQUIREMENT` of
`P-DMATTER-TOTAL-1-EFFECT-SHADOW-MINIMAL-OWNER-FREEZE.md`.

Every other clause of that freeze remains unchanged. In particular:

```text
RETAIN:
    ordered outcomes LOW/HIGH;
    exact fixed effects E_low/E_high;
    singleton admissibility;
    exact effect completeness;
    exact Born trace pairing;
    explicit ZERO/NONZERO boundary;
    source-forgetting as a typed quotient only.

RETAIN REJECTIONS:
    outcome swap as gauge;
    generic class of all projector decompositions;
    Kraus or post-state content;
    realized outcomes or sampling;
    uniqueness-from-J wording;
    source forgetting of the evaluated Q-state;
    dependency from the direct map definition through source forgetting.
```

The owner amendment does not rewrite the merged effect-shadow note. This note
is the later proposal-governance decision for the direct write requirement.

## 2. Why the prior independence claim is retired

The public notes already contain the exact algebraic realization

```text
matrix_B0(<.,.>_tr) = G,
pi_low = E_low,
pi_high = E_high,
[T_w]_B0 = v v^T G,
R_cyc(iota_B0(v)) = F_Gram(Qcan(v)).
```

These identities were proved before this amendment. The candidate in the
original PR #273 predefinition is therefore not a new independent route. It is
the same cyclotomic realization under the same basis, trace pairing, low line,
and representation map.

The distinction now frozen is:

```text
definitionally separate:
    R_cyc is written directly from field arithmetic, sigma_4, Tr, the trace
    pairing, lambda_B, and the rank-one operator T_w;

scientifically independent:
    false for this candidate, because the exact transport theorem to F_Gram
    is already known and published in the notes.
```

Equality of values does not generally prove definitional dependency. Here,
however, the full semantic transport theorem is already known. Calling the
candidate an independent confirmation would be false.

## 3. Frozen direct dictionary

Let

```text
K = Q(zeta),             zeta = zeta_5,
bar(x) = sigma_4(x),     Tr = Tr_(K/Q),
B0 = (1,zeta,zeta^2,zeta^3),
<x,y>_tr = (1/5) Tr(x bar(y)).
```

Let `K_QDD` be the proposal-local complete forward-orbit carrier and let

```text
beta_QDD : K_QDD -> V_eff
```

be the total pre-update balanced head map already used by the QDD proposal.
For `v in V_eff`, define

```text
iota_B0(v) = v_0 + v_1 zeta + v_2 zeta^2 + v_3 zeta^3.
```

The owner adopts

```text
D_QDD_direct(kappa)
    := R_cyc(iota_B0(beta_QDD(kappa))).
```

This equation is the proposal-local direct write rule. `DIRECT` names the
direction from the orbit head through the cyclotomic dictionary into the
record. It no longer means independent evidence.

The direct map definition is not specified through `EffectPair_QDD`,
`BornPair_QDD`, `ForgetSource_QDD`, the source-forgetting quotient, or
`F_QDD`. The later factorization theorem may name both sides. The definition
of the direct map may not use the theorem it is later shown to satisfy.

## 4. Cyclotomic record

For `w = iota_B0(v)`, put

```text
lambda_B = 1 + zeta + zeta^2 + zeta^3 = -zeta^4,

m_tr(w) = <w,w>_tr,

pi_low(w)
    = (<w,lambda_B>_tr / <lambda_B,lambda_B>_tr) lambda_B,

pi_high(w) = w - pi_low(w),

w_low(w)  = <pi_low(w),pi_low(w)>_tr,
w_high(w) = <pi_high(w),pi_high(w)>_tr,

T_w(x) = w <x,w>_tr.
```

The record has exactly five fields:

```text
MatterData_QDD = (
    support_state,
    total_weight,
    branch_weights,
    density_state,
    normalized_weight_state
).
```

The ordered branch pair is `(LOW,HIGH)`. Its components may not be swapped.

### ZERO branch

```text
if w = 0:

    support_state            = ZERO_SUPPORT,
    total_weight             = 0,
    branch_weights           = (0,0),
    density_state            = ZERO_DENOMINATOR,
    normalized_weight_state  = ZERO_DENOMINATOR.
```

No division is performed. `ZERO_DENOMINATOR` is a tag, not a normalized
measure.

### NONZERO branch

```text
if w != 0:

    support_state            = SUPPORTED,
    total_weight             = m_tr(w),
    branch_weights           = (w_low(w),w_high(w)),
    density_state
        = MATRIX_B0(T_w) / m_tr(w),
    normalized_weight_state
        = (w_low(w),w_high(w)) / m_tr(w).
```

All equalities are exact rational equalities in the fixed basis `B0`.

## 5. Derived factorization theorem

The direct dictionary is adopted first. The factorization is then a theorem
about that dictionary, not its definition:

```text
D_QDD_direct
    = F_QDD o Q_QDD o beta_QDD.
```

At the finite carrier level, the theorem reduces to the already proved exact
identities

```text
matrix_B0(<.,.>_tr) = G,
pi_low = E_low,
pi_high = E_high,
MATRIX_B0(T_w) = v v^T G,
R_cyc(iota_B0(v)) = F_Gram(Qcan(v)).
```

The theorem must be checked field by field using the record equality:

```text
support_state             literal tag equality
total_weight              exact rational equality
branch_weights            ordered componentwise rational equality
density_state             literal tag or entrywise rational equality
normalized_weight_state   literal tag or componentwise rational equality
```

A mismatch is a construction or transcription defect relative to the adopted
dictionary. It is not an independence result.

## 6. Dependency and acyclicity rule

The adopted direct map has a proposal-local definition graph rooted at

```text
DEF-QDD-DIRECT-WRITE.
```

Its definitional closure may contain:

```text
K_QDD,
beta_QDD,
V_eff,
zeta,
B0,
iota_B0,
sigma_4,
Tr,
the trace pairing,
lambda_B,
pi_low,
pi_high,
T_w,
MATRIX_B0,
R_cyc,
MatterData_QDD,
the ZERO/NONZERO tags.
```

The direct map definition may not contain:

```text
EffectPair_QDD,
AdmissibleEffectPair_QDD,
BornPair_QDD,
ForgetSource_QDD,
the source-forgetting quotient,
F_QDD,
Q_QDD,
QCarrier_QDD,
a helper whose definition unfolds through those objects.
```

This firewall prevents circular definition. It does not assert scientific
independence. A separate theorem node may depend on both
`DEF-QDD-DIRECT-WRITE` and the factor/Born branch in order to prove their exact
equality.

The complete proposal graph must remain acyclic:

```text
orbit head
    -> direct dictionary
    -> MatterData_QDD

orbit head
    -> Q_QDD
    -> F_QDD
    -> MatterData_QDD

both branches
    -> factorization theorem
```

No edge may run from the factorization theorem back into either branch
definition.

## 7. Status of computation

No finite computation can decide the retired independence question.

A future exact verifier may check:

```text
the field identities;
the ZERO/NONZERO partition;
nonnegativity and normalization;
the five record equalities;
totality on the frozen finite domain;
the declared dependency graph and acyclicity;
implementation agreement with the proved formulas.
```

Such a verifier is a proof audit, regression certificate, or conformance
certificate. It is not:

```text
an independent discovery;
an independent physical confirmation;
a selector of the direct dictionary;
a blind test of the factorization;
evidence that the architecture is forced by J.
```

A 625-value or 15,625-state sweep must be labeled accordingly.

## 8. What this amendment closes and what it does not

This amendment closes, at proposal-governance level only:

```text
the Route A versus Route B owner fork;
the meaning of DIRECT-WRITE;
the status of the known cyclotomic equality;
the admissible use of a future finite verifier.
```

It does not close:

```text
the public coefficient-ring and carrier identifiers;
the final orbit-to-amplitude bridge identifier;
the public MatterData ownership rows;
the exact completion-contract insertion;
the complete public dependency and gate rows;
the L1 to L6 typing of the physical dictionary;
physical measure selection;
sampling or realized outcomes;
post-state instrument semantics;
history, feedback, or writeback;
decoder totality, uniqueness, or completeness;
QUADRATIC-DECODER-DATA.
```

The existing effect-shadow, apparatus, source-rule, and prepared-state owner
notes remain proposal inputs only. None becomes Canon evidence through this
amendment.

## 9. Next ordered requirement

The next work is no longer a search for a genuinely independent direct
readout. It is one complete proposal-local insertion package for the adopted
dictionary:

```text
1. assign final proposal identifiers to the direct map and five output fields;
2. bind the exact carrier, domain, codomain, equality, and ZERO/NONZERO tags;
3. state the factorization theorem as a theorem, not a premise;
4. publish the complete dependency graph and acyclicity decision;
5. fill the applicable decoder-completion contract slots;
6. name every required L1 to L6 endpoint and gate without performing a lift;
7. freeze positive, negative, and STOP routing for a later prospective probe;
8. re-audit the whole package on the then-current Public Canon basis.
```

Only after that package is reviewed may a separate prospective
preregistration decide whether a formal conformance probe is useful.

## 10. Scope firewall

This note adds no Canon claim and no public identifier. It authorizes no
formal execution. It adopts no uniqueness-from-J statement, physical
instrument, post-state semantics, realized outcome, sampling, probability of
occurrence, history, feedback, or writeback.

```text
CANON CHANGE                    NONE
REGISTRY CHANGE                 NONE
DEPENDENCY CHANGE               NONE
GATE CHANGE                     NONE
PROBE                           NONE
FORMAL RUN                      NONE
QUADRATIC-DECODER-DATA          O / STOP
NEXT ORDERED REQUIREMENT        COMPLETE DICTIONARY INSERTION PACKAGE
```
