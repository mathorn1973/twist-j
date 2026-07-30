# P-TM-SYM2-MEASURE-1 selector and Born-halving predefinition (NON-CANONICAL)

Status: `DRAFT / STOP-PREDEFINITION / NO-PROBE`

This note defines the public decisions required before the residual
`TM-SYM2-MEASURE [H]` claim can receive a formal selector probe. It is not a
selector, physical dictionary, preregistration, verifier, run, Canon change,
or status proposal. It authorizes no enumeration or formal execution. The
public lock is issue #119.

## Authority pin

```text
Canon:                 Public Canon v15
state:                 ACTIVE
tag:                   canon-v15
activation commit:     8f4e176c5d76f519d3493e56e438aba7856e1f01
content commit:        a850753348583e611bf7ccd5aa074030dc7e12f5
Canon SHA-256:         53237ec25b3782e833367c998c049d19459189a21c2a36638dd9e1600335976b
Canon bytes:           89288
public-main readback:  ecf38f30e7e7429c3333d88277633e19c148b66f
owner row:             TM-SYM2-MEASURE [H]
scheduler:             MEASURE / ROOT / STOP / FORMAL
normative layer:       MULTI, with the terminal measure at L6
future probe:          P-TM-SYM2-MEASURE-1
```

The Genesis-era file `notes/prereg/post-genesis/02-tm-sym2.md` is provenance
only. It does not freeze the selector carrier, autonomous-state convention,
canonicality class, limiting measure, typed Born map, or layer lifts required
by the current v15 row.

## 1. Exact inherited boundary

The following registered rows constrain this lane but do not close it.

```text
DEF-AUTONOMOUS-STATE [definition, L1]
    Omega = N_0 x F_5^6 and the update U are the complete autonomous input.

GOLDEN-SIX-LINE-SYM2-FRAME [T, L1]
    The six public projective lines, when supplied with equal cardinal
    weights, give
        M = (1/3) P1 + (2/15) P5
    with coefficient ratio 5:2.

GYRON-DENSITY [T]
    The named Thue-Morse pair 00 has stationary density 1/6.

MEASURE-BORN-VERB [D]
    The measure is read as a Born square of the verb; the row does not by
    itself type or derive the requested 1/2 factor here.

TIME-CUT-READING [D]
    The time cut selects fired generator indices. It supplies no map from an
    orbit to the six frame lines and claims no forcing, uniqueness, or
    completeness.
```

The completed `P-TM-SYM2-FRAME-1` probe is not selector evidence. Its six
lines and equal weights are frozen inputs, and its scope explicitly excludes
selection from `J`, `U`, a checkpoint, or a Thue-Morse orbit, as well as
GYRON density, Born halving, physical measure, and any L5 or L6 lift.

The current dependency floor is exactly:

```text
TM-SYM2-MEASURE -> DEF-ARCHITECTURE
TM-SYM2-MEASURE -> DEF-AUTONOMOUS-STATE
TM-SYM2-MEASURE -> GOLDEN-SIX-LINE-SYM2-FRAME
TM-SYM2-MEASURE -> GYRON-DENSITY
TM-SYM2-MEASURE -> MEASURE-BORN-VERB
```

No current row supplies the missing selector or a complete L1-to-L6 lift.
`GATE-L5-L6-BORN-READING` belongs to the registered Born dictionary input;
it does not silently provide the autonomous-stream selector gate.

## 2. Definition object to be frozen

A valid definition package must publish one finite exact tuple

```text
S_TM = (
    C_sel, Dom_sel, Eq_sel,
    update_convention, starts, seed_semantics,
    gauge_quotient, sign_quotient,
    Lines, line_labels, Sel,
    selector_class, selector_equivalence, canonicality_test,
    Measure, convergence, normalization,
    C_Born, Eq_Born, Born_map, half_map, third_map,
    layer_endpoints, layer_gates, dependencies,
    order, decision_algorithm, completeness_method,
    certificate_schema, certificate_checker
).
```

Every symbol is a placeholder until the corresponding decision below is
resolved publicly before any output.

| Block | Required decision | Current ruling |
| --- | --- | --- |
| selector carrier | exact carrier `C_sel`, total domain, and equality reading the declared `Omega` and `U`, or a precisely typed orbit/history quotient | `UNRESOLVED` |
| time convention | pre-update versus post-update state, origin, allowed starts, and shift convention | `UNRESOLVED` |
| seed semantics | one seed, a named seed class, or an ensemble; exact seed-independence obligation | `UNRESOLVED` |
| quotients | all gauge and sign actions, fixed points, representatives, and quotient equality | `UNRESOLVED` |
| line typing | ordered public six-line carrier, exact labels, and the relationship between projective signs and selector labels | `UNRESOLVED` |
| selector | total exact map `Sel : Dom_sel -> Lines`, complete allowed selector class, and result-independent equivalence | `UNRESOLVED` |
| canonicality | exact test deciding whether the architecture determines one selector-equivalence class | `UNRESOLVED` |
| limiting measure | exact cylinder or empirical measure, normalization, convergence notion, quantified domain, and seed/shift dependence | `UNRESOLVED` |
| completeness | exhaustive finite bound or theorem-grade reduction covering the full frozen selector class and limit | `UNRESOLVED` |
| Born carrier | coefficient objects, domain, codomain, equality, normalization, and the registered Born input actually used | `UNRESOLVED` |
| factor meanings | typed maps whose values are called `1/2` and `1/3`; neither may be inserted as a desired scalar | `UNRESOLVED` |
| density bridge | exact relationship, if any, between the line measure and `GYRON-DENSITY`; numerical equality alone is forbidden | `UNRESOLVED` |
| action layers | every source and target layer, exact lift, and named gate from the autonomous L1 stream to the terminal L6 measure | `UNRESOLVED` |
| audit | deterministic order, decision algorithm, certificate schema, exact checker, and complete dependency graph | `UNRESOLVED` |

## 3. Canonicality is a scientific gate

The registered hypothesis says that the declared stream **canonically
selects** the frame. A hand-picked map with six equal frequencies would be a
dictionary candidate, not a positive closure.

Before execution the definition must therefore freeze a complete selector
class and an exact equivalence relation. The canonicality test must return
one of:

```text
CANONICAL       exactly one selector-equivalence class survives;
NONCANONICAL    at least two inequivalent classes survive;
EMPTY           no selector satisfies the frozen pre-output rules;
STOP            classification or completeness is unresolved or inexact.
```

These are future probe routes, not registry statuses. The selector class may
not be narrowed after its frequencies, moment operator, or Born behavior are
read.

## 4. False shortcuts

The following do not satisfy the predefinition:

1. using only the finite checkpoint `psi` while omitting `n` and the
   autonomous update convention;
2. mapping the five fired generator indices directly to six frame lines
   without a separately typed rule;
3. choosing a selector because its observed frequencies are already
   `1/6`;
4. identifying the cardinal average in the frame theorem with
   `GYRON-DENSITY`;
5. writing `1/6=(1/2)(1/3)` numerically without typed maps that produce the
   two factors;
6. importing equal weights from `P-TM-SYM2-FRAME-1`, where they were inputs;
7. treating `MEASURE-BORN-VERB [D]` as a theorem that forces the halving;
8. checking a finite prefix without a frozen completeness or convergence
   theorem;
9. selecting a gauge, sign branch, seed, or start after seeing the output.

## 5. Acceptance test before a formal probe

The lane may move from `STOP` to `READY-DEFINITION` only when:

1. every field of `S_TM` is exact and contains no `UNRESOLVED` slot;
2. the selector reads the declared autonomous dynamics, not the checkpoint
   alone;
3. the candidate class, equality, and canonicality test are frozen before
   line counts or weights are computed;
4. pre/post-update, starts, seeds, gauge, sign, and line labels are explicit;
5. the limiting measure and its complete convergence method are exact;
6. the Born carrier and the meanings of `1/2` and `1/3` are typed;
7. the density bridge does more than identify equal rational numbers;
8. every layer lift and gate is named and the dependency graph is complete;
9. the certificate schema and checker establish completeness without
   containing a result-dependent expected class count or weight vector;
10. positive, negative, and STOP scientific routes remain available under
    the frozen definitions.

Any missing item leaves the lane at `STOP`.

## 6. Future formal routing, still forbidden

Only after a reviewed definition freeze may a later, separate immutable pin
create:

```text
branch: probe/P-TM-SYM2-MEASURE-1
path:   probes/P-TM-SYM2-MEASURE-1/
```

Its future routes are:

```text
POSITIVE
    The selector is canonical on the frozen quotient, gives
    mu_i=1/6 for all six lines, yields
    M_TM=(1/3)P1+(2/15)P5, and the typed Born map derives the halving.

NEGATIVE
    The frozen selector is empty or noncanonical, gives unequal weights,
    leaves the exact commutant, changes the 5:2 ratio, or the Born
    factorization is ill typed or contradicts GYRON-DENSITY.

STOP
    The definition, completeness proof, layer typing, certificate, checker,
    or exact reproduction is incomplete or inexact.
```

Any later registry move belongs to a separate reviewed Canon fold. A fired
negative route is preserved rather than repaired by changing the selector.

## 7. Debt firewall

This note does not select a line, measure, gauge, seed, Born map, or physical
probability. It does not promote the completed frame probe, strengthen
`TIME-CUT-READING`, equate the two registered occurrences of `1/6`, add a
free parameter, alter a dependency or gate, or change the frontier.

The immediate next executable work is definition only: supply a genuinely
prior selector principle or an exact complete selector class. Until then no
verifier or formal run is authorized.
