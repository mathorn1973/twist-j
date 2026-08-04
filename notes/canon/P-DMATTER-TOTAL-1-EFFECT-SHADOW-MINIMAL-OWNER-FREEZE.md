# P-DMATTER-TOTAL-1 EFFECT_SHADOW_MINIMAL owner freeze (NON-CANONICAL)

```text
STATUS:                    OWNER-ADOPTED DEFINITION / NOT CANON
AUTHORITY:                 NO NORMATIVE AUTHORITY
PUBLIC BASE:               a2c96226fc0ec994865d323dfc2b5c72fdd9dc41
PUBLIC CANON:              Public Canon v36 / canon-v36
PUBLIC CONTENT COMMIT:     df64035f6f0cadbeb17f539eaeec5d8d0f444515
PUBLIC CANON SHA-256:      c8f50d0ce4686d7eedc11599a95debee15c71a2cf13c52c93c3f0605890fa2d5
PUBLIC CANON BYTES:        175814
CLAIM ISSUE / COMMENT:     107 / 5178456032
OWNER DECISION:            ACCEPT EFFECT_SHADOW_MINIMAL AS FROZEN BELOW
FORMAL RUN:                NONE
PROBE / PREREGISTRATION:   NONE
CANON / TABLE CHANGE:      NONE
QDD STATUS:                O / STOP, unchanged
```

This note records one owner dictionary decision for the prospective
`QUADRATIC-DECODER-DATA` completion package. It freezes the minimal effect
shadow only. It does not define an instrument, perform a classification, open
a formal probe, or move a public status.

The decision was made after the local v35 binding package and adversarial
reaudit were visible. Those four local artifacts are `STALE_BASE /
NON-CANONICAL AUDIT INPUT` until rebuilt and reaudited on Public Canon v36.
The decision does not make their calculations blind, canonical, or evidence.

## 1. Exact owner decision

```text
ACCEPT:
    ordered outcomes LOW/HIGH
    exact fixed effects E_low/E_high
    singleton admissibility
    exact effect completeness
    exact Born trace pairing
    explicit ZERO/NONZERO boundary
    source-forgetting as a typed quotient only

REJECT:
    outcome swap as gauge
    generic class of all projector decompositions
    Kraus or post-state content
    realized outcomes or sampling
    uniqueness-from-J wording
    source forgetting of the evaluated Q-state
    any dependency from DIRECT-WRITE through the quotient or Born branch
```

The tuple is accepted as one whole owner choice. No accepted item may be
silently widened by one of the rejected readings.

## 2. Ordered outcome carrier

Freeze the two tagged outcomes

```text
Outcome_QDD = {LOW, HIGH}
OutcomeOrder_QDD = (LOW, HIGH)
Eq_Outcome_QDD = literal tagged equality.
```

Thus

```text
LOW != HIGH.
```

The order is part of the dictionary. Swapping `LOW` and `HIGH` is not gauge,
not an equality, and not an admissible presentation change.

This carrier describes possible readout labels only. It does not contain a
realized outcome, a sample, a frequency, or an occurrence law.

## 3. Fixed effect pair and singleton admissibility

Use the rational four-dimensional carrier and the already proposed Gram
notation

```text
V_eff subset Q^4,
G = I_4 - (1/5) 1 1^T,
A^sharp = G^(-1) A^T G.
```

Freeze exactly the ordered pair

```text
E_low  = (1/4) 1 1^T,
E_high = I_4 - E_low,
EffectPair_QDD = (E_low, E_high).
```

Matrix equality is entrywise rational equality. Pair equality is ordered
componentwise equality.

The complete admissibility predicate is singleton:

```text
AdmissibleEffectPair_QDD(P)
iff
P = EffectPair_QDD.
```

No generic class of all orthogonal projector decompositions is adopted. No
classification over alternative effect families is opened by this note.

## 4. Exact effect completeness

The frozen pair must satisfy the complete exact effect record

```text
E_low^2  = E_low,
E_high^2 = E_high,

E_low^sharp  = E_low,
E_high^sharp = E_high,

E_low E_high  = 0,
E_high E_low  = 0,

E_low + E_high = I_4.
```

These identities audit the one frozen pair. They do not generate an
admissible family and do not prove that the pair is forced by `J`.

Any failure of one displayed identity routes the candidate package to

```text
EFFECT-SHADOW-COMPLETENESS-INCONSISTENT / STOP.
```

## 5. Exact Born trace pairing

Let the ordered quadratic carrier retain its typed slots. For

```text
Q_QDD(v) = (A_dagger, A_T),
A_T = v v^T,
```

the effect shadow consumes the named transpose slot `A_T`. It does not erase
the typed distinction between dagger, transpose, and Gram adjoint.

Freeze

```text
m(A_T) = Tr(A_T G),

BornPair_QDD(LOW,  Q_QDD(v)) = Tr(E_low  A_T G),
BornPair_QDD(HIGH, Q_QDD(v)) = Tr(E_high A_T G).
```

Write

```text
w_low(A_T)  = BornPair_QDD(LOW,  Q_QDD(v)),
w_high(A_T) = BornPair_QDD(HIGH, Q_QDD(v)).
```

The exact normalization identity required from the frozen effect
completeness is

```text
w_low(A_T) + w_high(A_T) = m(A_T).
```

The Born pairing is an owner-adopted dictionary input. It is not claimed to be
uniquely derived from `J`, the projector identities, or the public Canon.

The pairing contains no Kraus map, Householder map, apparatus evolution,
post-state, realized outcome, sampling rule, frequency, history update,
feedback, or writeback.

## 6. Explicit ZERO/NONZERO boundary

The output boundary is total only through explicit tags:

```text
ZERO:
    m(A_T) = 0,
    branch weights = (0,0),
    normalized two-outcome value = ZERO_DENOMINATOR,
    no division is performed.

NONZERO:
    m(A_T) > 0,
    branch weights = (w_low(A_T), w_high(A_T)),
    normalized two-outcome value
      = NORMALIZED((w_low(A_T),w_high(A_T))/m(A_T)).
```

A candidate implementation must prove exact nonnegativity and total branch
coverage on its frozen domain. A negative total weight or an uncovered value
routes to

```text
EFFECT-SHADOW-WEIGHT-INCONSISTENT / STOP.
```

`ZERO_DENOMINATOR` is not a probability measure and is not obtained by
normalizing zero.

## 7. Source-forgetting quotient

Source forgetting is permitted only as a typed quotient of a source-labeled
copy of the fixed effect family.

For a separately typed source-label carrier `SourceLabel_QDD`, define

```text
SourceEffect_QDD
  = SourceLabel_QDD x {EffectPair_QDD},

ForgetSource_QDD(s, EffectPair_QDD)
  = EffectPair_QDD,

(s,P) ~_source (s',P')
iff
P = P'.
```

The quotient therefore forgets the source label and nothing else:

```text
SourceEffect_QDD / ~_source  ~=  {EffectPair_QDD}.
```

The evaluated quadratic state is not an element of the quotient carrier. It
remains an explicit input of the later evaluation map. Source forgetting may
not:

```text
forget or identify the evaluated Q-state;
identify LOW with HIGH;
turn outcome swap into gauge;
identify distinct MatterData records;
forget a realized outcome, because no realized outcome is defined here;
supply a physical occurrence or distribution law.
```

## 8. DIRECT-WRITE independence firewall

This owner freeze does not define `DIRECT-WRITE`.

A future genuinely independent direct branch may not depend, directly or
transitively, on any of

```text
EffectPair_QDD,
AdmissibleEffectPair_QDD,
BornPair_QDD,
ForgetSource_QDD,
the source-forgetting quotient,
the factor map,
a helper shared with the factor or Born branch.
```

In particular, source forgetting may not be used to manufacture apparent
independence between two branches that share the same physical Born read.

The later equality

```text
D_QDD_direct
  = F_QDD o Q_QDD o beta_QDD
```

may be a result target only after both sides have been defined with the
frozen independence firewall satisfied.

Any dependency path from `DIRECT-WRITE` through the quotient or Born branch
routes to

```text
DIRECT-WRITE-NOT-INDEPENDENT / STOP.
```

## 9. Scope firewall

This note adopts no statement of uniqueness from `J`. It adds no physical
instrument, no post-state semantics, no realized outcome, no sampling, no
probability of occurrence, no history, and no writeback.

It creates no public identifier and fills no completion-contract field by
itself. Exact public identifiers, full completion typing, frozen field names,
the complete ZERO branch, the dependency ledger, the insertion block, fold
rehearsal, and adversarial reaudit remain separate work.

```text
CANON CHANGE                    NONE
REGISTRY CHANGE                 NONE
DEPENDENCY CHANGE               NONE
GATE CHANGE                     NONE
PROBE                           NONE
FORMAL RUN                      NONE
QUADRATIC-DECODER-DATA          O / STOP
NEXT ORDERED REQUIREMENT        GENUINELY INDEPENDENT DIRECT-WRITE
```
