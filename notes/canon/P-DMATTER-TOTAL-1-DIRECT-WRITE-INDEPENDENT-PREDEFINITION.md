# P-DMATTER-TOTAL-1 independent DIRECT-WRITE predefinition (NON-CANONICAL)

```text
STATUS:                    PREDEFINITION / NOT CANON
AUTHORITY:                 NO NORMATIVE AUTHORITY
PUBLIC BASE:               a2c96226fc0ec994865d323dfc2b5c72fdd9dc41
PUBLIC CANON:              Public Canon v36 / canon-v36
PUBLIC CONTENT COMMIT:     df64035f6f0cadbeb17f539eaeec5d8d0f444515
PUBLIC CANON SHA-256:      c8f50d0ce4686d7eedc11599a95debee15c71a2cf13c52c93c3f0605890fa2d5
PUBLIC CANON BYTES:        175814
CLAIM ISSUE / COMMENT:     107 / 5179372348
OWNER DECISION:            NONE, READY/STOP LEFT OPEN
FORMAL RUN:                NONE
PROBE / PREREGISTRATION:   NONE
CANON / TABLE CHANGE:      NONE
QDD STATUS:                O / STOP, unchanged
```

This note prepares the next ordered requirement of the prospective
`QUADRATIC-DECODER-DATA` completion package: a genuinely independent
`DIRECT-WRITE`. It fixes candidate maps, a permitted vocabulary, a forbidden
object list, and an exact independence decision procedure. It asserts no
equality, no independence, no completion, and no scientific result.

## 1. What this note prepares and what it does not

The `EFFECT_SHADOW_MINIMAL` owner freeze closed the effect-shadow side of the
package and left one ordered requirement open. Its section 8 firewall states
the negative condition a later direct branch must satisfy but does not state
the positive construction, the permitted vocabulary, or the procedure that
discharges the firewall. This note supplies exactly those three things.

It prepares:

```text
the permitted primitive vocabulary of the direct branch;
the forbidden branch objects, restated from the firewall;
an exact, mechanically checkable independence criterion;
one candidate direct construction inside that vocabulary;
the five-field output manifest the direct branch must write;
the ZERO branch of the direct route;
the field-by-field equality target, as an open question.
```

It does not:

```text
freeze an owner decision;
assert D_QDD_direct = F_QDD o Q_QDD o beta_QDD;
assert that the candidate satisfies the independence criterion;
open a probe, preregistration, verifier, run, or evidence row;
create a public identifier or fill a completion-contract slot;
move QUADRATIC-DECODER-DATA from O / STOP.
```

## 2. Inherited base and stale inputs

The public base is Public Canon v36 as declared in the header. No `DEF-QDD-*`
identifier exists in `canon/NORMATIVE.tsv` at that base; the v27 and 2026-07-30
binding packages remain proposals, and every identifier used below is
proposal-local.

The local v35 package, its exact checks, and the adversarial reaudit remain

```text
STALE_BASE / NON-CANONICAL AUDIT INPUT
```

until rebuilt and reaudited on v36. This note does not rehabilitate them and
does not treat their numbers as evidence.

## 3. Permitted primitive vocabulary

The direct branch may use only the following. Each is a definition-level
primitive of the leg, not an object of the factor or Born branch.

```text
K_QDD                complete forward orbits of the autonomous update
beta_QDD             the total pre-update balanced head map into V_eff
ell                  the balanced section ell(0..4) = 0,1,2,-2,-1
zeta = zeta_5        the fifth root of unity named by AXIOM-J
B0 = (1,zeta,zeta^2,zeta^3)   the public power basis
iota_0               the power-basis embedding of Q^4 into Q(zeta_5)
Amp_QDD = iota_0 o beta_QDD   the amplitude
multiplication and addition in Q(zeta_5)
sigma_4              the Galois map zeta -> zeta^4
Tr                   the field trace Tr_(Q(zeta_5)/Q)
<x,y> = (1/5) Tr( x sigma_4(y) )     the pairing
lambda_B = 1 + zeta + zeta^2 + zeta^3 = -zeta^4
```

Sharing a primitive is not a dependency. `AXIOM-J`, the field, the basis, the
Galois map, the trace, and the pairing are common vocabulary of the whole leg;
if sharing them counted as dependency, no two branches of one algebra could
ever be independent and the firewall would be vacuous.

The exact value `<lambda_B, lambda_B> = 4/5` follows from the pairing and is
recorded here as an arithmetic fact of the vocabulary, not as a result.

## 4. Forbidden branch objects

Restated from section 8 of the `EFFECT_SHADOW_MINIMAL` freeze, unchanged:

```text
EffectPair_QDD
AdmissibleEffectPair_QDD
BornPair_QDD
ForgetSource_QDD
the source-forgetting quotient
the factor map F_QDD
any helper shared with the factor or Born branch
```

To the same effect and by the same reading, the direct branch may not name,
import, or be specified by:

```text
E_low, E_high, or any matrix defined as a projector of the effect pair;
Q_QDD, A_dagger, A_T, or QCarrier_QDD;
the Gram matrix G in its role as the matrix of BornPair_QDD;
m(A_T), w_low(A_T), w_high(A_T);
any quantity whose definition unfolds to one of the above.
```

The last clause is the operative one. A rename, an inlined formula, or a
locally redefined copy of a forbidden object is the forbidden object.

Note the deliberate asymmetry in the Gram row: `G` as the matrix of the
pairing in `B0` is a primitive of section 3, and `G` as the implementation of
`BornPair_QDD` is a forbidden branch object. The same array of rationals sits
in both roles. Only its role in a definition decides, which is exactly why the
criterion below is stated over definitional closures and not over numbers.

## 5. Independence criterion

Let `Def(x)` be the definitional closure of a proposal-local identifier `x`:
the least set containing `x` and, for every member, every identifier named in
its definition.

The criterion is:

```text
INDEPENDENT(DIRECT-WRITE)
iff
Def(DEF-QDD-DIRECT-WRITE) intersect FORBIDDEN = empty
and
Def(DEF-QDD-DIRECT-WRITE) subset of PERMITTED
and
the dependency subgraph restricted to Def(DEF-QDD-DIRECT-WRITE) is acyclic.
```

`FORBIDDEN` is the list of part 4. `PERMITTED` is the vocabulary of part 3
together with identifiers introduced by the direct branch itself. The three
conjuncts are exact set and graph tests over declared rows, not judgements.

The decision procedure, when a package is submitted:

```text
1. read the proposed DEPENDENCIES.tsv rows for the direct branch;
2. compute the transitive closure from DEF-QDD-DIRECT-WRITE;
3. test disjointness from FORBIDDEN;
4. test containment in PERMITTED;
5. test acyclicity of the restricted subgraph;
6. any failure routes to DIRECT-WRITE-NOT-INDEPENDENT / STOP.
```

Equality of computed values is not tested here and never establishes
dependency. Two independent constructions may agree everywhere; that is the
open question of the obligation, not a violation of the firewall. Conversely,
disagreement of values never repairs a declared forbidden edge.

## 6. Candidate direct construction

Proposal only, inside the vocabulary of part 3. For an orbit `kappa` in
`K_QDD` write

```text
w = Amp_QDD(kappa)   in   Q(zeta_5).
```

Total weight:

```text
m_direct(kappa) = <w, w> = (1/5) Tr( w sigma_4(w) ).
```

Low component, by the pairing-orthogonal projection onto the line `Q lambda_B`:

```text
pi_low(w) = ( <w, lambda_B> / <lambda_B, lambda_B> ) lambda_B,
pi_high(w) = w - pi_low(w).
```

Ordered branch weights:

```text
w_low_direct(kappa)  = < pi_low(w),  pi_low(w)  >,
w_high_direct(kappa) = < pi_high(w), pi_high(w) >.
```

Density, through the rank-one operator built from field multiplication and the
pairing alone:

```text
T_w(x) = w <x, w>,
Dens_direct(kappa) = MATRIX_B0( T_w ) / m_direct(kappa)   when m_direct > 0.
```

`MATRIX_B0` means evaluation of `T_w` on the four basis elements of `B0`,
column by column. It is an evaluation of the direct branch's own operator, not
an import of a quadratic pair.

Every displayed quantity is exact rational arithmetic. No floating point, no
sampling, no realized outcome, no post-state, no Kraus map, and no writeback
appears in the construction.

## 7. Output manifest

Both branches must write the same tagged record with exactly five fields:

```text
MatterData_QDD = (
    support_state,
    total_weight,
    branch_weights,
    density_state,
    normalized_weight_state
)
```

with equality per field:

```text
support_state             literal tag equality
total_weight              exact rational equality
branch_weights            ordered pair, exact rational equality componentwise
density_state             literal tag, or exact entrywise rational equality
normalized_weight_state   literal tag, or exact rational equality componentwise
```

Ordered means ordered. The pair `(w_low, w_high)` is not a set, and exchanging
its components is not an equality, consistent with the frozen outcome order
`(LOW, HIGH)`.

## 8. ZERO branch of the direct route

The direct route must be total on `K_QDD` through explicit tags and must
perform no division on the zero branch:

```text
ZERO:
    m_direct(kappa) = 0,
    support_state           = ZERO_SUPPORT,
    total_weight            = 0,
    branch_weights          = (0, 0),
    density_state           = ZERO_DENOMINATOR,
    normalized_weight_state = ZERO_DENOMINATOR.

NONZERO:
    m_direct(kappa) > 0,
    support_state           = SUPPORTED,
    total_weight            = m_direct(kappa),
    branch_weights          = (w_low_direct, w_high_direct),
    density_state           = MATRIX_B0(T_w) / m_direct(kappa),
    normalized_weight_state = (w_low_direct, w_high_direct) / m_direct(kappa).
```

A candidate must prove exact nonnegativity of `m_direct`, of both branch
weights, and total coverage of `K_QDD` by the two tags. A negative weight, an
uncovered orbit, or a division on the zero branch routes to

```text
DIRECT-WRITE-WEIGHT-INCONSISTENT / STOP.
```

`ZERO_DENOMINATOR` is a tag. It is not a measure and is not obtained by
normalizing zero.

## 9. Open equality target

The obligation's question, restated field by field and asserted nowhere:

```text
for every kappa in K_QDD, does

    D_QDD_direct(kappa) = ( F_QDD o Q_QDD o beta_QDD )(kappa)

hold in support_state, total_weight, branch_weights, density_state, and
normalized_weight_state, under the equalities of part 7?
```

Both outcomes remain reachable and both must remain merge-eligible. A positive
answer closes nothing by itself; a negative answer on any one field is a
result, not a defect to be repaired by redefinition.

The registered negative routes of `QUADRATIC-DECODER-DATA` remain live and
unevaluated. Nothing here evaluates a falsifier.

## 10. Independence risk disclosure

One risk is visible before any run and is recorded rather than left for a
reviewer to discover.

Write `w = iota_0(v)` with `v` in `Q^4` over `B0`, and let `G` be the matrix of
the pairing in `B0`. From `G = I_4 - (1/5) 1 1^T` and `1^T 1 = 4`:

```text
G 1 = 1 - (4/5) 1 = (1/5) 1,
<lambda_B, lambda_B> = 1^T G 1 = 4/5,
<w, lambda_B> = v^T G 1 = (1/5) (1^T v).
```

Hence the coefficient vector of `pi_low(w)` over `B0` is

```text
( (1/5)(1^T v) / (4/5) ) 1 = (1/4) 1 1^T v.
```

The coefficient matrix `(1/4) 1 1^T` is entrywise the frozen `E_low`.

This is a two-line derivation from part 3 primitives, auditable by any reader,
and it is not a run. Its consequence must be decided by the owner and is not
decided here:

```text
READING A: the coincidence is a derived identity. pi_low is specified by
    lambda_B and the pairing alone; no forbidden identifier appears in
    Def(DEF-QDD-DIRECT-WRITE); the criterion of part 5 passes; the
    coincidence is part of the open question rather than an answer to it.

READING B: the coincidence shows the two routes are the same object under
    two names, so the equality target is a tautology, the direct branch adds
    no independent content, and the package routes to
    DIRECT-WRITE-NOT-INDEPENDENT / STOP.
```

The criterion of part 5 as written selects reading A, because it tests
definitional closures and explicitly does not test agreement of values. Whether
that criterion is the one the owner intends is exactly the decision this note
leaves open. If the owner intends the firewall to bite on presentational
coincidence as well, the criterion must be strengthened before, not after, a
candidate package is judged against it.

The disclosure is confined to the low projector. It says nothing about
`density_state`, the ZERO branch, totality on `K_QDD`, or the record as a
whole, and it is not a claim about the obligation.

## 11. Predefinition decision, left open

```text
READY:
    the owner adopts an independence criterion, whether part 5 or a
    strengthened form; the permitted and forbidden lists are frozen; every
    identifier in the direct branch is public and exact; both PASS and
    negative routing remain reachable.

STOP:
    the independence criterion is unresolved; the vocabulary lists are not
    frozen; a direct-branch identifier remains UNRESOLVED; or the candidate
    imports a cross-leg or instrument claim.
```

No owner decision is recorded by this note. The lane remains where it was.

## 12. Scope firewall

This note adopts no uniqueness statement, no physical instrument, no post-state
semantics, no realized outcome, no sampling, no probability of occurrence, no
history, and no writeback. It fills no completion-contract slot by itself.
Exact public identifiers, the dependency ledger rows, the insertion block, fold
rehearsal, a pinned verifier over the full domain, and adversarial reaudit
remain separate work.

```text
CANON CHANGE                    NONE
REGISTRY CHANGE                 NONE
DEPENDENCY CHANGE               NONE
GATE CHANGE                     NONE
PROBE                           NONE
FORMAL RUN                      NONE
QUADRATIC-DECODER-DATA          O / STOP
NEXT ORDERED REQUIREMENT        OWNER DECISION ON THE INDEPENDENCE CRITERION
```
