# P-DMATTER-TOTAL-1 Public Binding Package v27 (NON-CANONICAL)

```text
STATUS:                    OWNER-SELECTED / PROSPECTIVE NORMATIVE INPUT
AUTHORITY:                 NOT CANON
PUBLIC BASE:               b0a53eb65e3a3511af28f5876b9d1bb882bda160
PUBLIC CANON:              Public Canon v27 / canon-v27
PUBLIC CONTENT COMMIT:     116b62edf505914d96fcd65318d97f3675c53f85
PUBLIC CANON SHA-256:      c7c4c7e6d5a3116e356b060eaf696963285b0f2f465d5f2e1dcda5c094a309f6
PUBLIC CANON BYTES:        150959
CLAIM ISSUE:               107
OWNER DECISION:            BINDING-PACKAGE
OWNER CONFIRMATION:        2026-07-30
SCOPE:                     B1 SOURCE THROUGH B5 CLOSURE
FORMAL RUN:                NONE
PROBE / PREREGISTRATION:   NONE
CANON / TABLE CHANGE:      NONE
QDD STATUS:                O / STOP, unchanged
```

This package records the owner's choice of `BINDING-PACKAGE` from
`P-DMATTER-TOTAL-1-QDD-PUBLIC-REQUIREMENTS-AUDIT.md`. It consolidates the
smallest prospective public definition that covers all fourteen registered
`QUADRATIC-DECODER-DATA` inputs. It does not make any identifier public,
change a registry row, add a gate, authorize a probe, or claim that the
displayed factorization passes.

The package deliberately excludes the linear `CODEC-TR4` and binary
Thue-Morse/census legs, cross-leg reconstruction, post-state instrument
uniqueness, sampling, realized outcomes, feedback, `D_geom`, `D_clock`, and
completion-wide terminality.

## 0. Failure and disclosure firewall

The package remains `STOP` if any displayed type, equality, totality domain,
field owner, dependency, layer endpoint, gate, or scope exclusion is missing
or inconsistent.

A later result routes negative under the registered QDD decision condition
if:

1. the action is ill typed;
2. an included field is not constant on `Q`-fibres;
3. two inputs distinguished by the typed direct write have equal `Q`;
4. one normalization identity fails; or
5. an input outside the frozen allowlist is required.

The following facts were visible before this package and must be disclosed in
any preregistration:

```text
|K0|                                      15625
|QCarrier|                                  313
zero Q-fibre size                            25
nonzero Q-fibre size                         50
known Route A factorization calculations     exposed preparation
known cyclotomic/Gram identity                exposed preparation
known apparatus and preparation counts       exposed preparation
```

A future audit is proof-first and result-exposed. It is not a blind
selection experiment.

## 1. B1 SOURCE

Let `X=F_5^6` in the public checkpoint coordinate order and let

```text
K_QDD
  = {kappa_x=(U^n(0,x))_(n>=0) : x in X}.
```

Equality `Eq_K_QDD` is literal equality of complete pointed forward
sequences. The distinguished head is the term at `n=0`. The prospective
decoder domain is

```text
dom(D_matter,QDD) = K_QDD.
```

This adopts the proposal-local headed representation class
`[K0]=[Krange_0]` through its pointed-sequence representative. It does not
replace the public carrier `K`; it selects the explicit subset `K_QDD` as
the common total domain of this decoder leg.

Use the balanced section

```text
ell(0)=0, ell(1)=1, ell(2)=2, ell(3)=-2, ell(4)=-1.
```

For
`x=(p1,p4,p1p,p4p,q,r)`, freeze the total pre-update head map

```text
beta_QDD(kappa_x)
  = (ell(p1),ell(p4),ell(p1p),ell(p4p))^T
  in V_eff=ell(F_5)^4 subset Q^4.
```

The coordinates `q,r`, every later checkpoint, environment, files, clock,
randomness, network input, and dynamic evaluation are forbidden inputs to
`beta_QDD`.

With `zeta=zeta_5` and the Route A basis

```text
B0=(1,zeta,zeta^2,zeta^3),
iota_0(v)=v_0+v_1 zeta+v_2 zeta^2+v_3 zeta^3,
```

the orbit-to-amplitude bridge is the total map

```text
Amp_QDD = iota_0 o beta_QDD : K_QDD -> Q(zeta_5).
```

Prospective definition identifiers:

```text
DEF-QDD-DOMAIN-K0
DEF-QDD-EQ-POINTED-ORBIT
DEF-QDD-BALANCED-PISTON
DEF-QDD-AMPLITUDE-B0
```

## 2. B2 QUADRATIC ALGEBRA

The coefficient ring is `Q`. On `V_eff subset Q^4`, freeze

```text
G  = I_4 - (1/5) 1 1^T,
v^dagger = v^T,
transpose(A)=A^T.
```

The Gram adjoint `A^sharp=G^(-1)A^T G` remains a distinct typed operation.
Define the ordered quadratic pair

```text
Q_QDD(v)=(v v^dagger, v v^T),
QCarrier_QDD=im(Q_QDD|V_eff)
             subset M_4(Q) x M_4(Q).
```

The equality on `QCarrier_QDD` is ordered componentwise rational matrix
equality. Equal coordinate values do not collapse the dagger and transpose
slots.

Prospective definition identifiers:

```text
DEF-QDD-COEFFICIENT-Q
DEF-QDD-CARRIER-VEFF
DEF-QDD-GRAM
DEF-QDD-DAGGER
DEF-QDD-TRANSPOSE
DEF-QDD-QPAIR
DEF-QDD-QCARRIER-EQUALITY
```

## 3. B3 PHYSICAL READ

Freeze the two exact effects

```text
E_low  = (1/4) 1 1^T,
E_high = I_4-E_low.
```

They satisfy

```text
E_j^2=E_j,
E_j^sharp=E_j,
E_low+E_high=I_4.
```

For `A=v v^T`, define

```text
m(A)      = Tr(A G),
w_j(A)    = Tr(E_j A G),
w_low(A)+w_high(A)=m(A).
```

This package owner-adopts `{E_low,E_high}` as the complete scoped
two-outcome effect family and the displayed trace rule as its Born pairing.
The adoption is a new dictionary input. It is not derived from the effect
identities alone.

No Kraus family, post-state instrument, realized click, frequency,
distribution, sampling law, or instrument-uniqueness claim is included.
Those objects are not required by the registered QDD scope.

Prospective definition identifiers:

```text
DEF-QDD-EFFECT-LOW
DEF-QDD-EFFECT-HIGH
DEF-QDD-BORN-TRACE-PAIRING
DEF-QDD-EFFECT-COMPLETENESS
```

## 4. B4 OUTPUT

The output is the total tagged record

```text
MatterData_QDD =
  ZERO {
    support_state            = ZERO,
    total_weight             = 0,
    branch_weights           = (0,0),
    density_state            = ZERO_DENOMINATOR,
    normalized_weight_state  = ZERO_DENOMINATOR
  }
| NONZERO {
    support_state            = NONZERO,
    total_weight             = m(A),
    branch_weights           = (w_low(A),w_high(A)),
    density_state            = DENSITY(A G/m(A)),
    normalized_weight_state  =
      NORMALIZED((w_low(A),w_high(A))/m(A))
  }.
```

Exactly these five fields are `READOUT` fields owned by stage `D_matter` and
leg `D_quadratic`. No auxiliary field is added.

The prospective field manifest is:

| field ID | type and equality | normalization | source and emit rule |
|---|---|---|---|
| `DEF-QDD-FIELD-SUPPORT` | `TYPE-QDD-SUPPORT={ZERO,NONZERO}` with literal tag equality | `NORM-QDD-SUPPORT-IDENTITY` | `DEF-QDD-AMPLITUDE-B0`; emit `ZERO` iff the amplitude is zero |
| `DEF-QDD-FIELD-TOTAL-WEIGHT` | `TYPE-QDD-NONNEGATIVE-RATIONAL` with rational equality | `NORM-QDD-TOTAL-WEIGHT-IDENTITY` | `DEF-QDD-BORN-TRACE-PAIRING`; emit `0` on ZERO and `m(A)` on NONZERO |
| `DEF-QDD-FIELD-BRANCH-WEIGHTS` | ordered `Q_(>=0)^2` with componentwise rational equality | `NORM-QDD-BRANCH-SUM`, certifying `w_low+w_high=m` | `DEF-QDD-BORN-TRACE-PAIRING`; emit `(0,0)` or `(w_low,w_high)` |
| `DEF-QDD-FIELD-DENSITY` | tagged `ZERO_DENOMINATOR | DENSITY(M_4(Q))` with constructor and componentwise equality | `NORM-QDD-DENSITY-TRACE`, dividing by `m(A)` only on NONZERO | `DEF-QDD-QPAIR` and `DEF-QDD-GRAM`; emit the zero tag or `DENSITY(A G/m(A))` |
| `DEF-QDD-FIELD-NORMALIZED-WEIGHTS` | `TaggedMeasure_QDD` with constructor and componentwise rational equality | `NORM-QDD-TWO-OUTCOME`, dividing by `m(A)` only on NONZERO | `DEF-QDD-BORN-TRACE-PAIRING`; emit the zero tag or the normalized ordered pair |

Every row has:

```text
record_id       DEF-QDD-MATTER-RECORD
domain_id       DEF-QDD-DOMAIN-K0
write_map_id    DEF-QDD-DIRECT-WRITE
presence_state  RESOLVED
stage_id        D_matter
leg_id          D_quadratic
role            READOUT
```

The table's type, equality, normalization, source, and emit-rule identifiers
are definitions introduced by the same prospective normative package. No
row inherits one of those identifiers merely from a shared record owner.

The direct write is defined on the cyclotomic side. For
`w=Amp_QDD(kappa)`, use field multiplication, `sigma_4`, and
`Tr_(Q(zeta_5)/Q)` to form the support tag, total trace weight, rational-line
and trace-kernel branch weights, rank-one trace-pairing density, and tagged
normalization. Call the resulting total map

```text
D_QDD_direct : K_QDD -> MatterData_QDD.
```

It is specified without calling `Q_QDD`, `F_QDD`, or a shared
factorization helper.

Separately define

```text
F_QDD : QCarrier_QDD -> MatterData_QDD
```

by the displayed Gram/effect formulas. The prospective theorem target is

```text
D_QDD_direct = F_QDD o Q_QDD o beta_QDD
```

on every element of `K_QDD`, with equality of the complete tagged record.
This equality is a result target, not a definition.

Prospective definition identifiers:

```text
DEF-QDD-MATTER-RECORD
DEF-QDD-FIELD-SUPPORT
DEF-QDD-FIELD-TOTAL-WEIGHT
DEF-QDD-FIELD-BRANCH-WEIGHTS
DEF-QDD-FIELD-DENSITY
DEF-QDD-FIELD-NORMALIZED-WEIGHTS
DEF-QDD-DIRECT-WRITE
DEF-QDD-FACTOR-MAP
```

## 5. Layer split and gate

`K_QDD`, `V_eff`, the amplitude, `QCarrier_QDD`, effects, support, total
weight, branch weights, and density state are L1 state-side exact algebraic
data. The anchored record is not an L5 stream.

Only the nonzero normalized two-outcome weight is read as an L6 finite
probability measure. To keep the zero branch total, define the tagged
codomain

```text
TaggedMeasure_QDD
  = ZERO_DENOMINATOR
  | MEASURE({low,high}, (p_low,p_high)),
    p_low,p_high in Q_(>=0), p_low+p_high=1.
```

The prospective gate is

```text
GATE-L1-L6-QDD-BORN-READOUT
owner:       QUADRATIC-DECODER-DATA
from_layer:  L1
to_layer:    L6
kind:        OPEN_LIFT
```

It closes positively only when the complete typed direct write factors
through `Q_QDD`, every nonzero output gives the displayed normalized
two-outcome measure, the zero output remains explicitly tagged, and the
complete dependency graph and hidden-input allowlist pass. It closes
negatively under any registered QDD falsifier. Missing typing, completeness,
or implementation closure routes `STOP`.

`GATE-L5-L6-BORN-READING` is not reused because no L5 stream is defined.

## 6. B5 dependency closure

The prospective definition DAG is:

```text
DEF-ARCHITECTURE
  -> DEF-QDD-DOMAIN-K0
  -> DEF-QDD-BALANCED-PISTON
  -> DEF-QDD-AMPLITUDE-B0

DEF-QDD-COEFFICIENT-Q
  -> {DEF-QDD-CARRIER-VEFF,
      DEF-QDD-GRAM,
      DEF-QDD-DAGGER,
      DEF-QDD-TRANSPOSE}
  -> DEF-QDD-QPAIR
  -> DEF-QDD-QCARRIER-EQUALITY

{DEF-QDD-GRAM, DEF-QDD-QPAIR}
  -> {DEF-QDD-EFFECT-LOW,
      DEF-QDD-EFFECT-HIGH,
      DEF-QDD-BORN-TRACE-PAIRING}
  -> DEF-QDD-EFFECT-COMPLETENESS

{DEF-QDD-AMPLITUDE-B0,
 DEF-QDD-QPAIR,
 DEF-QDD-BORN-TRACE-PAIRING}
  -> DEF-QDD-MATTER-RECORD
  -> {DEF-QDD-DIRECT-WRITE,
      DEF-QDD-FACTOR-MAP}
  -> GATE-L1-L6-QDD-BORN-READOUT
  -> QUADRATIC-DECODER-DATA.
```

The required public-ledger delta is:

```text
QUADRATIC-DECODER-DATA -> DEF-DECODER-COMPLETION-CONTRACT
QUADRATIC-DECODER-DATA -> DEF-ACTION-LAYERS
QUADRATIC-DECODER-DATA -> DEF-QDD-DOMAIN-K0
QUADRATIC-DECODER-DATA -> DEF-QDD-QPAIR
QUADRATIC-DECODER-DATA -> DEF-QDD-BORN-TRACE-PAIRING
QUADRATIC-DECODER-DATA -> DEF-QDD-MATTER-RECORD
QUADRATIC-DECODER-DATA -> DEF-QDD-DIRECT-WRITE
QUADRATIC-DECODER-DATA -> GATE-L1-L6-QDD-BORN-READOUT.
```

Together with the five existing public dependencies, these rows form an
acyclic owner graph. No displayed edge points from `MatterData_QDD`, an
outcome, a later checkpoint, or an L6 measure back into `U`, `beta_QDD`,
the effects, or the direct write.

The five QDD fields are not terminal outputs of the complete decoder:
`D_geom` may read `MatterData`. Therefore

```text
write_target_ids     = the five exact QDD field IDs
feeds_U              = FALSE
terminal_output_ids  = empty
terminality_basis_id = DEF-DECODER-GEOMETRY
```

This is stage-local acyclicity, not closure of `OBSERVER-WRITE-PORT`.

The semantic input allowlist is closed by construction:

```text
allowed:
  the literal n=0 head of kappa in K_QDD;
  its four piston coordinates;
  the fixed balanced section;
  the fixed rational/cyclotomic constants and maps in B1 through B4;
  exact deterministic arithmetic.

forbidden:
  q and r;
  every later checkpoint and counter value;
  D_geom, D_clock, MatterData feedback, and any emitted outcome;
  measured values, fitted parameters, environment, files, wall clock,
  randomness, network input, and dynamic evaluation.
```

A future verifier may implement only this graph. Its imports, source files,
environment access, clock, randomness, network access, and dynamic-evaluation
surface must be frozen and checked before the first formal run.

## 7. Completion-contract scope

The QDD submission fills every slot owned by stage `D_matter`, leg
`D_quadratic`, the five record fields, the quadratic manifest, the scoped
L1-to-L6 bridge, and stage-local closure.

Identifier-valued slots belonging exclusively to `D_geom`, `D_clock`,
`D_linear`, `D_binary`, source-current-propagator-detector physics,
metrology, scheme selection, or completion-wide terminality cannot be filled
with bare null, `UNRESOLVED`, or an untyped `NOT_APPLICABLE`.

A prospective normative fold must therefore add the typed constructor

```text
SCOPE_EXCLUDED(
    expected_kind_id,
    submitted_scope_id,
    owning_requirement_id,
    public_basis_item_id)
```

to `DEF-DECODER-COMPLETION-CONTRACT`. It is admissible only when the public
registry scope explicitly excludes the owning requirement, all four fields
resolve, and the constructor is type-checked at the expected identifier
kind. It is not a blanket waiver and cannot exclude one of the fourteen QDD
requirements.

For this package the submitted scope is
`SCOPE-QDD-DMATTER-DQUADRATIC`. The registry text excluding the linear,
binary, cross-leg, reconstruction, and post-state instrument-uniqueness
surfaces supplies the basis for those exclusions. The package makes no
claim about excluded properties.

## 8. Public disposition

At proposal scope the owner decisions are now:

```text
B1 SOURCE                 FROZEN
B2 QUADRATIC ALGEBRA      FROZEN
B3 PHYSICAL READ          FROZEN
B4 OUTPUT                 FROZEN
B5 CLOSURE                FROZEN
```

At public scope all fourteen bindings remain `MISSING` until a reviewed
Canon patch adopts the definitions, dependency rows, contract constructor,
layer split, and gate together. `QUADRATIC-DECODER-DATA` remains `O / STOP`.

After that prospective normative adoption, but before any formal execution,
the lane must still:

1. publish and review the exact finite manifests;
2. pin one six-field `PREREG.md` and an independently reviewable verifier;
3. record hashes and public readback before the first run;
4. preserve both positive and registered negative routing;
5. disclose every known count and prior preparation result;
6. execute only under the public two-architecture protocol.

No probe or verifier is authorized by this file.
