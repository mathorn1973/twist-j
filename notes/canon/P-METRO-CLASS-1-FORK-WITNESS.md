# P-METRO-CLASS-1: factorwise versus joint-anchored control (NON-CANONICAL)

Status: `DRAFT / BOUNDED-CONTROL-LEMMA / DEFINITION-UNRESOLVED`

This note supplies one exact matrix control for the compositional fork in
`P-METRO-CLASS-1-SCOPE-MAP.md`. It does not select the public scientific
criterion, prove translated-box uniformity, or supply an all-parameter
decision theorem. It is not `PREREG.md`, a verifier, run, Canon change, or
status proposal. `METRO-ADMISSIBILITY` stays `[O]`.

## Authority pin

```text
Canon:              Public Canon v14
state:              ACTIVE
tag:                canon-v14
activation commit:  f278855cada75691142c02ebad1a75ecc2730db3
content commit:     ab4ea07d15ab1cfa0c403d3c2a74164011ffa0e7
Canon SHA-256:      f9f06af42a9b0b63f806603ddc671ebe6a9e5014b50d230da04a28722ed1a6a2
Canon bytes:        87061
owner row:          METRO-ADMISSIBILITY [O]
gate:               GATE-L5-L6-METRO-NORMALIZATION
child candidate:    METRO-COMMUTING-DIGIT-AUTOMATIC-CHILD-1
draft parent:       PR #115, commit
                    5e60b7768e38e0e6dbb565b9d2c53138eaf260f9
scheduler:          DECODER_CORE / ROOT / READY / FORMAL
```

`READY` only permits the owner to choose and define one residual class. The
draft parent is non-canonical and is not an authority dependency.

## 1. Exact fixed-length word-average control

Take

```text
q=2,
a=2,
r=2,
S={0,1},
W5(s)=e_s in Q_(>=0)^2.
```

Let `X` be the two-state swap matrix. For fixed binary word lengths, define
the coordinate digit actions

```text
coordinate 1: delta_(1,0)=delta_(1,1)=X,
coordinate 2: delta_(2,0)=I, delta_(2,1)=X.
```

All four digit maps commute. Uniform averaging over all words of a fixed
length gives

```text
T_1 = X,
T_2 = (I+X)/2,
T_1^2=I,
T_2^2=T_2,
T_1 T_2=T_2 T_1=T_2.
```

Consequently the factorwise sequence `T_1^m` does not converge. In the
entrywise maximum norm,

```text
max_entry |T_1^(m+1)-T_1^m| = 1
```

for every `m`. But for every start state, every `m_1>=0`, and every
`m_2>=1`, the joint anchored fixed-length average is exactly

```text
(T_1^m1 T_2^m2 W5)(s) = (1/2,1/2).
```

Thus factorwise power convergence is not necessary for joint anchored box
convergence, even in the smallest nontrivial commuting example.

This is deliberately only a fixed-length word-average control. The first
coordinate is not leading-zero invariant, so the note does not claim a
padding-independent stream on `N^2`. The exact digit order, padding, allowed
starts, and pointwise integer semantics remain unresolved in the parent.

The control also has force only if the named rank-two action and independent
rectangular cofinal parameters are retained as typed structure. Synchronously
pairing the two digits produces a one-dimensional four-letter automaton with
average `T_1 T_2=T_2`. Such flattening or diagonalization is forbidden by the
proposed child type but has not yet been publicly adopted.

No private stdout hash or two-architecture report is needed or offered; the
entire bounded calculation is displayed above.

## 2. What the control decides

The exact proposal-local lemma is

```text
FACTORWISE POWERS != JOINT ANCHORED CONVERGENCE
```

on the displayed fixed-length matrix class. Therefore a future definition
on any class containing this control may not assert their equivalence as an
algebraic identity.

The control does not decide:

```text
uniform convergence on arbitrary translated boxes;
padding-independent integer-stream semantics;
the scientific role of a compositional map;
the complete child class;
reduction invariance;
the L5-to-L6 gate endpoints.
```

In particular, it does not prove that the complete direct and factorwise
decisions disagree on an admitted protocol.

## 3. Owner-amendment recommendation, not adoption

For the proposed child, the cleanest future design is to use the direct
translated-box property as the scientific object and a joint spectral
decomposition as an exact certificate for that same property. On such a
design, certificate disagreement is `STOP` integrity rather than a second
scientific outcome.

That recommendation is not active. The controlling merged ruling #112
currently requires two independently defined maps and routes their
disagreement as `NEGATIVE`. Replacing the independent factorwise map by a
joint certificate requires a separate reviewed owner amendment before any
definition freeze or preregistration. Until then, the compositional fork is
`UNRESOLVED`.

No existing Canon theorem is cited as a multidimensional joint-spectral iff.
The active boundary only says that normalized one-dimensional rational
finite-state protocols are already inside the sealed class; it does not
supply this higher-rank theorem.

## 4. Completeness remains a proof obligation

A useful target shape is two-level, but neither level is closed here:

```text
ANCHORED ALL-PARAMETER TARGET:
    seek an exact terminating criterion on the reachable submodule using
    simultaneous primary/peripheral decomposition of commuting rational
    matrices, including the tagged normalization and terminal-value tests;

TRANSLATED-BOX TARGET:
    prove uniform translated-box convergence with an effective boundary
    decomposition and modulus for the same child criterion.
```

Simultaneous decomposition is a suggested route, not a supplied termination
or completeness proof. Translated-box uniformity stays inside the same
`METRO-ADMISSIBILITY` child and the existing
`GATE-L5-L6-METRO-NORMALIZATION`; this note creates no new obligation owner
or gate.

If the all-parameter proofs are not supplied before freeze, the honest
fallback is a finite surface with public bounds on every parameter and
encoding. A bounded exhaustive probe and an unproved all-parameter theorem
may not be claimed simultaneously.

## 5. Exact disposition for the next day

```text
CLOSED PROPOSAL-LOCALLY:
    factorwise powers are not equivalent to joint anchored convergence.

OWNER DECISION REQUIRED:
    amend ruling #112 to choose joint spectral certification,
    or retain an independently scientific factorwise map.

PROOF/TYPE DEBT STILL OPEN:
    digit order and padding;
    admitted N^a stream semantics;
    translated-box theorem and effective modulus;
    anchored all-parameter completeness or finite bounds;
    minimization and blocking invariance;
    exact L5/L6 endpoints and parent-closure routing.

FORMAL PROBE:
    forbidden.
```

`METRO-ADMISSIBILITY` stays `[O]`, `METRO-EDGE-SCALE` stays `[O]`,
`OBSERVER-WRITE-PORT` stays blocked, and the frontier, gates, dependencies,
and Canon remain unchanged.
