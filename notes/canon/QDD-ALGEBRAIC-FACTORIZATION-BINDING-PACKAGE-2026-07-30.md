# QDD-ALGEBRAIC-FACTORIZATION-BINDING-PACKAGE-2026-07-30

```text
STATUS:                  NON-CANONICAL DEFINITION AND BINDING PROPOSAL
AUTHORITY:               NOT CANON
SCOPE:                   QDD ALGEBRAIC FACTORIZATION ONLY
WRITTEN:                 from scratch, 2026-07-30; not a repair of
                         P-DMATTER-TOTAL-1-PUBLIC-BINDING-PACKAGE-V27.md
RULINGS APPLIED:         notes/canon/QDD-OWNER-RULINGS-2026-07-30.md
AUDIT APPLIED:           notes/canon/AUDIT-QDD-BINDING-PACKAGE-V27.md
CLAIM ISSUE:             107
PUBLIC BASE:             Public Canon v27, tag canon-v27
PUBLIC CONTENT COMMIT:   116b62edf505914d96fcd65318d97f3675c53f85
PUBLIC CANON SHA-256:    c7c4c7e6d5a3116e356b060eaf696963285b0f2f465d5f2e1dcda5c094a309f6
PUBLIC CANON BYTES:      150959
FORMAL RUN:              NONE
PROBE / PREREGISTRATION: NONE
CANON / TABLE CHANGE:    NONE, and see part 7 on why this header line is
                         honest here and was not honest in the predecessor
QDD STATUS:              O / STOP, unchanged
V28:                     HOLD
```

## 0. Scope, and what is excluded

This package asks exactly one question:

```text
does the independently defined direct write of the five-field record
MatterData_QDD factor through Q_QDD ?
```

Excluded, and not mentioned again except to say so:

```text
physical apparatus selection      physical effect identifiers
realized outcomes                 post-state instruments
sampling                          decoder completion
the v28 manifest                  SCOPE_EXCLUDED
```

The exclusions are load bearing. Re-admitting physical effects, apparatus, or a
general `SCOPE_EXCLUDED` constructor would immediately reinstate audit defects
B6 and B8.

Per ruling 2 the word **`PROJECTOR`** is used throughout and the word `EFFECT`
appears nowhere as an identifier. `quadratic_manifest.effect_ids` stays
`UNRESOLVED` and is not touched by this package.

Every witness below is reproduced by
`notes/canon/QDD-ALGEBRAIC-FACTORIZATION-CHECKER-2026-07-30.py`, transcript
pinned in part 8.

## 1. Domain and equalities

Let `X = F_5^6` in the public checkpoint coordinate order, `x = (p1, p4, p1p,
p4p, q, r)`, and

```text
K_QDD = { kappa_x = (U^n(0,x))_(n>=0) : x in X }.
```

`Eq_K_QDD` is literal equality of complete pointed forward sequences; the
distinguished head is the term at `n = 0`. The prospective decoder domain of
this leg is `dom(D_matter,QDD) = K_QDD`, a selected subset of the public
carrier `K`, not a replacement for it.

The balanced section is

```text
ell(0)=0, ell(1)=1, ell(2)=2, ell(3)=-2, ell(4)=-1,
```

and the total pre-update head map is

```text
beta_QDD(kappa_x) = ( ell(p1), ell(p4), ell(p1p), ell(p4p) )^T
                    in V_eff = ell(F_5)^4 subset Q^4.
```

`q`, `r`, every later checkpoint, environment, files, clock, randomness,
network input and dynamic evaluation are **forbidden inputs**. The checker
verifies this by exhaustion: the record is constant across all 25 values of
`(q, r)` for each of the 625 piston tuples.

Equality on `V_eff` is equality in `Q^4`.

## 2. The cyclotomic direct write, with formulas

Let `zeta = zeta_5`, `B0 = (1, zeta, zeta^2, zeta^3)` the public power basis,
and

```text
iota_0(v) = v_0 + v_1 zeta + v_2 zeta^2 + v_3 zeta^3,
Amp_QDD   = iota_0 o beta_QDD : K_QDD -> Q(zeta_5).
```

Freeze the Galois map and the pairing:

```text
sigma_4 : Q(zeta_5) -> Q(zeta_5),   sigma_4(zeta) = zeta^4,
<x, y>  = (1/5) Tr_(Q(zeta_5)/Q)( x sigma_4(y) ).
```

The constant `1/5` is part of the definition, not a convention left to the
reader. In the basis `B0` the Gram of `<.,.>` is exactly `G` of part 4; the
checker verifies this, so the `1/5` is the entire normalisation and nothing
further is hidden.

Write `w = Amp_QDD(kappa)`. The five fields are then, **without any reference
to `Q_QDD`, `F_QDD`, `G`, or a projector matrix**:

```text
m(w)        = <w, w>

support(w)  = ZERO      if m(w) = 0
            = NONZERO   otherwise

pi_low(w)   = ( <w, lambda_B> / <lambda_B, lambda_B> ) lambda_B
pi_high(w)  = w - pi_low(w)
w_low(w)    = < pi_low(w),  pi_low(w)  >
w_high(w)   = < pi_high(w), pi_high(w) >

T_w         : Q(zeta_5) -> Q(zeta_5),   T_w(x) = w <x, w>
density(w)  = the matrix of T_w / m(w) in the basis B0,
              column j being T_w(b_j)/m(w)

normalized(w) = ( w_low(w), w_high(w) ) / m(w)
```

with the zero branch tagged rather than divided:

```text
ZERO    { support=ZERO, total_weight=0, branch_weights=(0,0),
          density_state=ZERO_DENOMINATOR,
          normalized_weight_state=ZERO_DENOMINATOR }
```

Call the resulting total map `D_QDD_direct : K_QDD -> MatterData_QDD`. It is
built from three operations only: multiplication in `Q(zeta_5)`, `sigma_4`,
and `Tr_(Q(zeta_5)/Q)`.

Closed forms, for the reader and for the checker, with `s = sum_i v_i`:

```text
m       = sum_i v_i^2 - s^2/5
w_low   = s^2/20
w_high  = sum_i v_i^2 - s^2/4
```

## 3. The LOW LINE

```text
lambda_B = 1 + zeta + zeta^2 + zeta^3 = -zeta^4,
L_B      = Q lambda_B,          <lambda_B, lambda_B> = 4/5.
```

`L_B` is **the low line**. It is neither the rational line `Q.1` nor the trace
kernel: `Tr(lambda_B) = 1`, which is neither zero nor consistent with a
rational generator, and the checker verifies both facts.

The words *rational line* and *trace kernel* are not used anywhere in this
package for this object. Naming that line `Q.1` costs 480 of the 625 carriers,
that is 12000 of the 15625 checkpoints, with smallest witness `v = (1,0,0,0)`
where the correct branch pair is `(1/20, 3/4)` and the mis-named one is
`(4/5, 0)`. That is the exact defect recorded as B2 of the audit, and it is
the reason this part exists as its own numbered section.

`notes/canon/P-DMATTER-TOTAL-1-CYCLOTOMIC-REALIZATION.md` section 3 already
named this object the low line and explicitly rejected the shifted window
`(zeta, ..., zeta^4)` as "a new selector decision, not an inherited public
fact". This package follows that note and not the predecessor package.

## 4. The quadratic side

Coefficient ring `Q`. On `V_eff subset Q^4`:

```text
G          = I_4 - (1/5) 1 1^T,
v^dagger   = v^T,
transpose(A) = A^T,
A^sharp    = G^(-1) A^T G.
```

`G` is exactly the Gram of the pairing of part 2, so it is not an independent
choice.

The adjoint and the transpose are **two separate definitions**, because the
public contract carries `dagger_id`, `transpose_id` and `q_map_id` as three
distinct slots:

```text
DEF-QDD-DAGGER-RATIONAL      dagger_Q(v)    = v^T   on V_eff
DEF-QDD-TRANSPOSE-RATIONAL   transpose_Q(v) = v^T   on V_eff
TYPED-DIAGONAL-IDENTITY      dagger_Q|V_eff = transpose_Q|V_eff
```

`TYPED-DIAGONAL-IDENTITY` is their exact coincidence on the chosen carrier. It
is a recorded identity of this leg, not a licence to merge the slots: **one
identifier must not fill two manifest slots merely because the two values
agree.** The ordered quadratic map is then

```text
Q_QDD(v)       = ( v dagger_Q(v), v transpose_Q(v) ),
QCarrier_QDD   = im( Q_QDD | V_eff )  subset M_4(Q) x M_4(Q),
```

with ordered componentwise rational matrix equality.

**Owner ruling, recorded.** The diagonal ordered pair is admissible for the
current registered scope. The public row asks for
`Q(psi) = (psi psi^dagger, psi psi^T)` and does not ask that the two components
be different, independent, or each carry separate information. On the selected
effective carrier `V_eff subset Q^4` it is therefore permitted that
`v^dagger = v^T` and `Q_QDD(v) = (v v^T, v v^T)`. That is a degenerate
specialization of the registered form, not a violation of it.

Nothing may be claimed from it. This package asserts **no** independence of the
two quadratic components, **no** essential use of both, **no** uniqueness of
the adjoint choice, and **no** completeness of a general quadratic
architecture. A choice taking `sigma_4` as a non-trivial adjoint would be a
different candidate with a different carrier and a different equality; it is
not mixed into this package.

The two **projectors**, per ruling 2:

```text
P_low  = (1/4) 1 1^T,      P_high = I_4 - P_low,
P_a^2 = P_a,   P_a^sharp = P_a,   P_low P_high = 0,   P_low + P_high = I_4.
```

They are `ALGEBRAIC_READOUT`. They are **not** a physical apparatus selection,
**not** a realized outcome, **not** a post-state instrument, and they do not
fill `quadratic_manifest.effect_ids`. `P_low` is the `G`-orthogonal projector
onto `L_B` of part 3; `P_high` projects onto its `G`-orthogonal complement,
which is `{v : sum_i v_i = 0}` and is **not** the trace kernel.

The branch weight pairing, for `A` the common slot of a carrier element:

```text
m(A)   = Tr(A G),
w_a(A) = Tr(P_a A G),          w_low(A) + w_high(A) = m(A).
```

`F_QDD : QCarrier_QDD -> MatterData_QDD` is defined by these formulas together
with `density = A G / m(A)` on the nonzero branch and the tagged zero
constructor otherwise.

## 5. The target

```text
D_QDD_direct  =  F_QDD o Q_QDD o beta_QDD        on every element of K_QDD,
with equality of the complete tagged record.
```

The direct side of part 2 is defined without naming `Q_QDD`, `F_QDD`, `G`, or a
projector, so this is a statement relating two independently built maps and not
a re-notation.

**Two honest qualifications, stated here and not buried.**

First, `D_QDD_direct` is of even degree in `w` and `sigma_4(w)`. It therefore
satisfies `D_QDD_direct(w) = D_QDD_direct(-w)` automatically, and since
`Q_QDD` identifies exactly `+-v`, *factoring through some map that identifies
`+-v`* is not by itself content. The checker verifies the evenness explicitly
so that no reader mistakes it for a result.

Second, what is therefore substantive is **field-by-field equality of the two
records**, including the normalising constant `1/5`, the branch order, the
choice of line in part 3, and the `End_Q(Q(zeta_5)) -> M_4(Q)` convention that
makes `T_w` a matrix. Each of those can be got wrong, and the predecessor
package got the third one wrong on 12000 of 15625 checkpoints. The target is
falsifiable in exactly those places.

Result of evaluating both sides on the whole domain: **equal in all five
fields on all 15625 checkpoints**, with no exception. The record separates the
carrier, 313 distinct records for 313 distinct `Q` values.

## 6. The decision condition, and why no gate row is proposed

The decision must admit three outcomes and must not prescribe its own answer:

```text
POSITIVE  the complete tagged record of the independently defined direct write
          equals the record of F_QDD o Q_QDD o beta_QDD on every element of
          K_QDD, field by field, under the frozen types and equalities.

NEGATIVE  at least one exactly determined field of the direct write takes
          different values on two elements with equal Q_QDD, or the two
          records differ on at least one element of K_QDD.

STOP      any type, equality, totality domain, completeness statement,
          dependency graph, or enforceable layer endpoint is missing or
          inconsistent.
```

No output value appears in this condition. It does not say what `m`, the branch
pair, the density or the normalized pair must be. Whether they agree with any
previously computed number is read off the comparison, never imposed on it.

**No `GATES.tsv` row is proposed, and this is deliberate.** The reason is
factual, and it is the one place where this package departs from the letter of
the instruction it was written under.

`tools/check_ledger.py` rejects a gate whose `from_layer` equals its
`to_layer`: it fails with *does not cross a layer*. A gate is therefore
available only to an object that performs a lift. Under ruling 2 this package
claims no `L6` measure and no physical read, and the record is not an `L5`
stream. The whole of part 2 and part 4 is exact algebraic data on the `L1`
state side. **It performs no lift.** Proposing a gate for it would mean
inventing a target layer in order to satisfy a form, which is precisely the
adaptation of the science to the tool that the ruling forbids in its other
direction.

Two further facts, established by reading the checker rather than by argument,
support leaving the gate out and are reported in full in part 9:

```text
the cross-layer rule fires only on a dependency edge whose two endpoints both
carry a concrete layer in L1..L6 and whose layers differ;

exactly 1 of the 11 registered gates is reachable by that rule
(GATE-L1-L5-LOG-PROJECTION, owned by DEF-LOG-STREAM at L5, required by its
REQUIRES edge to DEF-AUTONOMOUS-STATE at L1). The other 10 are decorative.
```

So the three-outcome decision lives in the decision condition of the eventual
obligation row, which is where the registry actually enforces decisions, and
not in a gate row that no rule would reach.

## 7. Proposed future normative delta

**Proposal only, inside a non-canonical package.** Nothing here is installed by
this note, and per ruling 1 nothing here may be installed by a standalone table
patch. These rows enter, if at all, as part of the content commit of a new
Canon, at which point the Canon version, SHA-256 and byte count move.

That is why this package's header can honestly say `CANON / TABLE CHANGE:
NONE`: it proposes no table change now, and it states the version consequence
of the change it proposes later. The predecessor's header could not say it,
because it simultaneously declared new normative identifiers and denied any
Canon change.

### 7.1 `NORMATIVE.tsv`

Columns `item_id, item_type, claim_id, status, layer, gate_ids,
statement_source`. `DEFINITION` items carry empty `claim_id` and empty
`status`, following every existing `DEF-*` row.

The anchor is **definitive, not a placeholder**. `tools/check_ledger.py`
verifies that the anchor string literally occurs in the named file, so a
placeholder would make the delta untestable and would leave the scratch run
checking an improvisation rather than the proposal. The exact proposed text of
the section, which part 7.5 gives in full, is inserted into
`canon/CANON.md` as a `###` sub-section of `## 2. Time, space, and the
decoder`, the section that already sources `DEF-LOG-STREAM` and
`DEF-DECODER-MATTER`. All sixteen rows therefore read:

```text
statement_source = canon/CANON.md::QDD algebraic factorization definitions
```

The sixteen items, all `DEFINITION`, all layer `L1`, all `gate_ids` empty:

```text
DEF-QDD-DOMAIN                 DEF-QDD-GRAM
DEF-QDD-BALANCED-SECTION       DEF-QDD-DAGGER-RATIONAL
DEF-QDD-AMPLITUDE              DEF-QDD-TRANSPOSE-RATIONAL
DEF-QDD-SIGMA4                 DEF-QDD-QPAIR
DEF-QDD-PAIRING                DEF-QDD-MATTER-RECORD
DEF-QDD-LOW-LINE               DEF-QDD-DIRECT-WRITE
DEF-QDD-PROJECTOR-LOW          DEF-QDD-FACTOR-MAP
DEF-QDD-PROJECTOR-HIGH
DEF-QDD-BRANCH-WEIGHT-PAIRING
```

Every `statement_source` is `canon/CANON.md`, per ruling 1. `gate_ids` is empty
on every row, per part 6. Every layer is `L1`, which is the honest layer of
exact algebraic data on the state side, and which is what makes the absence of
a gate correct rather than convenient: all dependency endpoints below share
that layer, so no cross-layer edge exists to require one.

### 7.2 `DEPENDENCIES.tsv`

Columns `item_id, depends_on, relation, basis`. Both `relation` and `basis` are
supplied on every row; `basis` is required non-empty.

```text
DEF-QDD-DOMAIN  DEF-AUTONOMOUS-STATE  REQUIRES
  the domain is the set of complete forward orbits of the autonomous update,
  so it inherits that definition and no other
DEF-QDD-BALANCED-SECTION  DEF-QDD-DOMAIN  REQUIRES
  the section is applied to the four piston coordinates of the domain head
DEF-QDD-AMPLITUDE  DEF-QDD-BALANCED-SECTION  REQUIRES
  the amplitude is the power-basis image of the balanced head vector
DEF-QDD-PAIRING  DEF-QDD-SIGMA4  REQUIRES
  the pairing is defined by the Galois map and the field trace
DEF-QDD-LOW-LINE  DEF-QDD-PAIRING  REQUIRES
  the line is fixed by its pairing norm and is projected onto by the pairing
DEF-QDD-PROJECTOR-LOW  DEF-QDD-LOW-LINE  REQUIRES
  the projector is the pairing-orthogonal projector onto that line
DEF-QDD-PROJECTOR-HIGH  DEF-QDD-PROJECTOR-LOW  REQUIRES
  the high projector is the complement of the low projector
DEF-QDD-BRANCH-WEIGHT-PAIRING  DEF-QDD-PROJECTOR-HIGH  REQUIRES
  the branch weights are the pairing norms of the two projected components
DEF-QDD-GRAM  DEF-QDD-PAIRING  REQUIRES
  the Gram matrix is the matrix of the pairing in the frozen power basis
DEF-QDD-BRANCH-WEIGHT-PAIRING  DEF-QDD-GRAM  REQUIRES
  the weights are traces against the Gram of the frozen pairing
DEF-QDD-DAGGER-RATIONAL  DEF-QDD-BALANCED-SECTION  REQUIRES
  the rational adjoint is defined on the effective carrier the section produces
DEF-QDD-TRANSPOSE-RATIONAL  DEF-QDD-BALANCED-SECTION  REQUIRES
  the rational transpose is defined on the effective carrier the section
  produces
DEF-QDD-QPAIR  DEF-QDD-DAGGER-RATIONAL  REQUIRES
  the first slot of the ordered pair is formed with the rational adjoint
DEF-QDD-QPAIR  DEF-QDD-TRANSPOSE-RATIONAL  REQUIRES
  the second slot of the ordered pair is formed with the rational transpose;
  the two slots coincide on this carrier and remain typed separately
DEF-QDD-MATTER-RECORD  DEF-QDD-BRANCH-WEIGHT-PAIRING  REQUIRES
  the record's five fields are typed by the weights and the tagged zero branch
DEF-QDD-DIRECT-WRITE  DEF-QDD-AMPLITUDE  REQUIRES
  the direct write is a total map out of the amplitude alone
DEF-QDD-DIRECT-WRITE  DEF-QDD-MATTER-RECORD  REQUIRES
  the direct write writes exactly the frozen record schema
DEF-QDD-FACTOR-MAP  DEF-QDD-QPAIR  REQUIRES
  the factor map is defined on the quadratic carrier
DEF-QDD-FACTOR-MAP  DEF-QDD-MATTER-RECORD  REQUIRES
  the factor map writes exactly the frozen record schema
QUADRATIC-DECODER-DATA  DEF-QDD-DIRECT-WRITE  REQUIRES
  the open row's write map is this direct write
QUADRATIC-DECODER-DATA  DEF-QDD-FACTOR-MAP  REQUIRES
  the open row's factorization target is stated against this factor map
```

`DEF-QDD-SIGMA4` is the one new root of this subgraph: the Galois automorphism
of `Q(zeta_5)` depends on nothing else in the ledger, and inventing a parent
for it in order to keep a count stable would be adapting the science to the
tool. `DEF-AUTONOMOUS-STATE` is the only existing item the subgraph attaches
to, and `QUADRATIC-DECODER-DATA` keeps its five existing outgoing edges
unchanged.

No row points at a gate. Gates bind through the owner's `gate_ids` column, and
0 of the 345 existing dependency edges point at a `GATE-*`; the predecessor's
row doing so was a category error.

### 7.3 `GATES.tsv`

```text
no row proposed; see part 6
```

### 7.4 Owner row

`QUADRATIC-DECODER-DATA` keeps `item_type OBLIGATION`, `status O`, `layer
MULTI`, and empty `gate_ids`. **The layer is not changed to `L6`.** Changing it
so that a checker begins to enforce a gate would be adapting the scientific
type to the tool, and, as part 9 records, would make QDD the second enforced
gate in a ledger where ten of eleven are not enforced.

### 7.5 The exact proposed `canon/CANON.md` section

Inserted as a `###` sub-section of `## 2. Time, space, and the decoder`,
immediately before `## 3. The kernel and the census`. Its heading supplies the
anchor of 7.1. This is the complete text; nothing is left to be improvised at
fold time.

```text
### QDD algebraic factorization definitions

These definitions fix the algebraic factorization leg of `D_matter` and
nothing else. They select no physical apparatus, adopt no effect family,
assert no realized outcome, no post-state instrument, and no `L6` measure.
`quadratic_manifest.effect_ids` remains unresolved.

Let `X = F_5^6` in the public checkpoint coordinate order,
`x = (p1, p4, p1p, p4p, q, r)`, and `K_QDD = { (U^n(0,x))_(n>=0) : x in X }`
with equality of complete pointed forward sequences (DEF-QDD-DOMAIN). The
balanced section is `ell(0)=0, ell(1)=1, ell(2)=2, ell(3)=-2, ell(4)=-1`
(DEF-QDD-BALANCED-SECTION), and the total pre-update head map is
`beta_QDD(kappa_x) = (ell(p1), ell(p4), ell(p1p), ell(p4p))^T` in
`V_eff = ell(F_5)^4` inside `Q^4`. The coordinates `q` and `r`, every later
checkpoint, and every environment input are forbidden inputs.

With `zeta = zeta_5` and the public power basis `B0 = (1, zeta, zeta^2,
zeta^3)`, the amplitude is `Amp_QDD = iota_0 o beta_QDD` where
`iota_0(v) = v_0 + v_1 zeta + v_2 zeta^2 + v_3 zeta^3` (DEF-QDD-AMPLITUDE).
The Galois map is `sigma_4(zeta) = zeta^4` (DEF-QDD-SIGMA4) and the pairing is
`<x, y> = (1/5) Tr_(Q(zeta_5)/Q)( x sigma_4(y) )` (DEF-QDD-PAIRING). The
constant `1/5` is part of the definition; the matrix of the pairing in `B0` is
exactly `G = I_4 - (1/5) 1 1^T` (DEF-QDD-GRAM).

The low line is `L_B = Q lambda_B` with
`lambda_B = 1 + zeta + zeta^2 + zeta^3 = -zeta^4` and
`<lambda_B, lambda_B> = 4/5` (DEF-QDD-LOW-LINE). It is neither the rational
line `Q.1` nor the trace kernel; `Tr(lambda_B) = 1`. The pairing-orthogonal
projector onto `L_B` is `P_low = (1/4) 1 1^T` and its complement is
`P_high = I_4 - P_low` (DEF-QDD-PROJECTOR-LOW, DEF-QDD-PROJECTOR-HIGH). They
are algebraic readout, not a physical apparatus selection. The branch weight
pairing is `w_a(A) = Tr(P_a A G)` with `w_low + w_high = m` where
`m(A) = Tr(A G)` (DEF-QDD-BRANCH-WEIGHT-PAIRING).

On `V_eff` the rational adjoint is `dagger_Q(v) = v^T` (DEF-QDD-DAGGER-RATIONAL)
and the rational transpose is `transpose_Q(v) = v^T`
(DEF-QDD-TRANSPOSE-RATIONAL). They are separate definitions filling separate
contract slots; that they coincide on this carrier is a recorded identity of
this leg and is not a claim that the two slots are the same object. The ordered
quadratic map is `Q_QDD(v) = (v dagger_Q(v), v transpose_Q(v))` with ordered
componentwise rational matrix equality on its image `QCarrier_QDD`
(DEF-QDD-QPAIR). On `V_eff` the two components coincide; that degenerate
specialization asserts no independence of the two quadratic components, no
essential use of both, no uniqueness of the adjoint choice, and no completeness
of a general quadratic architecture.

`MatterData_QDD` is the tagged record with exactly five fields, support state,
total weight, ordered branch weights, density state and normalized weight
state, with the zero branch tagged rather than divided (DEF-QDD-MATTER-RECORD).
The direct write `D_QDD_direct : K_QDD -> MatterData_QDD` is built from
multiplication in `Q(zeta_5)`, `sigma_4` and `Tr` alone, using
`pi_low(w) = ( <w, lambda_B> / <lambda_B, lambda_B> ) lambda_B` and the
rank-one operator `T_w(x) = w <x, w>` whose matrix in `B0`, divided by `m(w)`,
is the density (DEF-QDD-DIRECT-WRITE). The factor map
`F_QDD : QCarrier_QDD -> MatterData_QDD` is defined by the displayed Gram and
projector formulas (DEF-QDD-FACTOR-MAP). Whether
`D_QDD_direct = F_QDD o Q_QDD o beta_QDD` holds field by field is the open
question of QUADRATIC-DECODER-DATA and is not asserted here.
```

## 8. Checker transcript

`notes/canon/QDD-ALGEBRAIC-FACTORIZATION-CHECKER-2026-07-30.py`, run from the
repository root under
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`,
Linux x86_64, Python 3.12.3, exit 0, empty stderr, about 18 s:

```text
QDD-ALGEBRAIC-FACTORIZATION checker
direct side: field multiplication, sigma_4 and Tr only
factor side: F_QDD o Q_QDD o beta_QDD, matrices only
arithmetic: int and Fraction only; no float in this file

L1 lambda_B = 1 + z + z^2 + z^3 equals -z^4 OK  sigma_4 has order 4 on it
L2 lambda_B is NOT rational and NOT in the trace kernel OK  Tr(lambda_B) = 1, so Q.lambda_B is neither Q.1 nor ker Tr
L3 the low line norm OK  <lambda_B, lambda_B> = 4/5
P1 the Gram of <x,y> in B0 is exactly G OK  so the 1/5 in the pairing is the whole normalisation
D1 D_direct equals F_QDD o Q_QDD o beta_QDD on all 15625 checkpoints OK  complete tagged record, all five fields
C1 closed forms m = sum v_i^2 - s^2/5 and w_low = s^2/20 OK
A1 the direct side reads only the four piston coordinates OK  625 piston tuples, one record each, independent of q and r
E1 direct_record is even, so factoring through +-w is automatic OK  disclosed, not claimed as content of the target
S1 the record separates the quadratic carrier OK  313 distinct records for 313 distinct Q values

SUMMARY 9/9 witnesses reproduce
```

## 8bis. The scratch delta, run before the audit

The delta of part 7 was applied to a scratch copy of public `main` at
`0096acb`, the base of this package, and the checks were run. This was done
deliberately **before** the adversarial audit: the audit should attack the
scientific and typed content, not be the first thing to discover a TSV slip or
a missing anchor. The result is known in advance and the audit is open rather
than blind, so a prior run does not compromise its independence. **The auditor
must repeat this run independently.** `D:/twistj` was never modified.

Scratch files changed, as one whole:

```text
canon/CANON.md          the exact section of 7.5, inserted before section 3
canon/NORMATIVE.tsv     16 rows
canon/DEPENDENCIES.tsv  21 rows
canon/SHA256SUMS        recomputed inside the scratch copy only
STATUS.md               CANON_SHA256 and CANON_BYTES, scratch copy only
```

No gate row. `canon/CANON.md` goes 150959 to 154521 bytes, which is exactly the
version consequence ruling 1 requires to be stated rather than denied. The
derived views were regenerated with `tools/generate_canon_views.py --apply`.

Check output:

```text
python3 tools/check_policy.py         POLICY PASS
python3 tools/check_canon.py          CANON PASS v27 claims=214
python3 tools/check_ledger.py         LEDGER PASS claims=214 items=246
                                      dependencies=366 evidence=214
                                      history=704 gates=11 programs=8
python3 tools/check_status_labels.py  STATUS LABELS PASS
python3 -m unittest discover -s tools -p 'test_*.py'
                                      FAILED (failures=1)
```

Registry counts: claims unchanged at 214, since these are `NORMATIVE` items and
not registry claims; items 230 to 246; dependencies 345 to 366; evidence,
history, gates and programs unchanged.

`statement_source` confirmation: all sixteen rows point at
`canon/CANON.md::QDD algebraic factorization definitions`, and that anchor is
the heading actually inserted by step 1 of the same run. `check_ledger.py`
verifies anchor presence by literal substring, so this is checked and not
asserted.

### The one failure, and what it means

```text
FAIL test_architecture_is_a_hub_not_the_only_non_algebraic_root
     tools/test_architecture_map_report.py line 48
     self.assertEqual(len(self.report.dependency_terminals), 10)
     AssertionError: 11 != 10
```

`tools/test_architecture_map_report.py` pins exact structural counts of the
ledger. The delta adds exactly one dependency terminal, and it is
`DEF-QDD-SIGMA4`:

```text
                                   base   scratch
direct_architecture_requires        172       172
transitive_architecture_dependents  189       189
dependency_terminals                 10        11   + DEF-QDD-SIGMA4
```

This is not a defect of the delta and it is not avoidable by rewiring.
`DEF-QDD-SIGMA4` is the Galois automorphism of `Q(zeta_5)`; it depends on
nothing else in the ledger and belongs beside `AXIOM-J`, `DEF-CHECKPOINT`,
`DEF-SELECTOR` and the other seven existing terminals. Giving it a parent to
keep a pinned number stable would be adapting the science to the tool.

**Consequence for the eventual fold: it must carry a companion update to
`tools/test_architecture_map_report.py`, changing the pinned terminal count
from 10 to 11.** That is a `tools/` change riding with a content fold, and it
must be visible in the fold's diff rather than discovered by its CI.

One earlier variant of the delta is recorded because it is instructive. With
`DEF-QDD-DOMAIN` attached to `DEF-ARCHITECTURE` instead of
`DEF-AUTONOMOUS-STATE`, the same test failed on a different line,
`direct_architecture_requires` 172 to 173. The parent was changed for a
scientific reason and not to dodge the test: `K_QDD` is literally the set of
complete forward orbits of `U`, so `DEF-AUTONOMOUS-STATE` is the precise
parent, and it mirrors `DEF-LOG-STREAM`, which is built from the same orbits.
The architecture-hub numbers being left alone is a consequence of that choice,
not its motive.

## 9. Open disclosures

Stated here so that no later preregistration has to discover them.

**9.1 The `313` collision with an excluded leg.** `|QCarrier_QDD| = 313`, with
one `Q`-fibre of 25 checkpoints and 312 of 50, covering
`25 + 312 * 50 = 15625`. Its arithmetic origin is the `+-v` identification:
`313 = 1 + (5^4 - 1)/2`, lifted 25-fold because `beta_QDD` ignores `q` and `r`.
The registered `CENSUS-313 [C]` leg, which this row's scope **excludes**, has
the identical profile: 313 attractors, 312 basins of 50 and one of 25, over the
same 15625 states, with registered origin `313 = 13^2 + 12^2`. Comparing the
two partitions of `F_5^6` directly gives **0 blocks in common**, and even the
two size-25 blocks are disjoint. The coincidence is numerical; there is no
cross-leg identity, which is what the scope requires. It is recorded because
this repository fences numerical coincidences explicitly.

**9.2 The ordered pair is diagonal — ruled admissible.** `v^dagger = v^T` makes
both slots of `Q_QDD(v)` equal on all 313 carrier elements. The owner has ruled
this a permitted degenerate specialization of the registered
`Q(psi) = (psi psi^dagger, psi psi^T)`, which asks for the ordered pair but not
for the two components to differ, to be independent, or each to carry separate
information. The ruling and its four prohibitions are recorded in part 4, and
the two slots are kept typed apart by `DEF-QDD-DAGGER-RATIONAL` and
`DEF-QDD-TRANSPOSE-RATIONAL` with `TYPED-DIAGONAL-IDENTITY` recording only
their coincidence on this carrier. This disclosure is therefore closed, and it
is not reopened by the audit that follows.

**9.3 Evenness.** Disclosed in part 5 and verified: factoring through a map
that identifies `+-v` is automatic for the direct write. The content of the
target is the field-by-field agreement, not the existence of some factorization.

**9.4 The registry cannot enforce a decision gate.** Established by reading
`tools/check_ledger.py`: the cross-layer rule fires only on a dependency edge
whose two endpoints both carry a concrete layer in `L1..L6` and whose layers
differ, and a gate whose endpoints coincide is rejected outright. Exactly one
of the eleven registered gates is reachable by that rule. There is therefore no
way to attach an enforced decision gate to an item that performs no lift. This
is an architectural limitation of the registry, not of this package, and it is
raised separately rather than worked around here.

**9.5 Degenerate branch reads.** Of the 624 nonzero carriers, 84 give
`w_low = 0` and 4 give `w_high = 0`, the latter being exactly the four nonzero
constant vectors. The normalized pair is then `(0,1)` or `(1,0)`. The type
admits this, since both components are only required to be nonnegative and to
sum to one, but the two-branch read is degenerate on 88 of 624 carriers and a
later physical reading must not assume otherwise.

**9.6 What is not established.** Nothing in this package bears on the physical
selection of effects, which stays `O / STOP` separately per ruling 2; on
decoder completion; on any `L6` measure; or on the contents of any Canon
version. `QUADRATIC-DECODER-DATA` stays `O / STOP`.

## 10. What must happen before a probe

Not a fold and not a probe yet.

```text
DONE  the proposed delta applied to a scratch copy and run; part 8bis. The
      four ledger checks pass; the one unit-test failure is the pinned
      terminal count and is disclosed with its cause and its fix.
DONE  an owner decision on 9.2, the diagonal pair; recorded in part 4.

1  a further adversarial audit of this package, on the same terms as the one
   that produced AUDIT-QDD-BINDING-PACKAGE-V27.md. It must repeat the scratch
   run independently rather than rely on part 8bis, and it should attack the
   five-field agreement, the 1/5 normalisation, the LOW LINE and the matrix
   convention. It should not re-decide 9.2, which is ruled.
2  the delta checked by hand against ruling 1, that is against the authority
   of the statement source, rather than against the tool alone. A delta can
   pass tools/check_ledger.py and still be wrong under ruling 1.
3  the companion update to tools/test_architecture_map_report.py, written as
   part of the fold and visible in its diff.
4  only then, a decision on whether this belongs in a v28 manifest, and only
   after that, whether a formal probe may be preregistered.
```

Nothing in this file authorizes a verifier, a run, a preregistration, a probe,
a fold, a tag, or a release.
