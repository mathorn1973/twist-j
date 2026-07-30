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

```text
Q_QDD(v)       = ( v v^dagger, v v^T ),
QCarrier_QDD   = im( Q_QDD | V_eff )  subset M_4(Q) x M_4(Q),
```

with ordered componentwise rational matrix equality. **Disclosure:** because
`v^dagger = v^T` on `Q^4`, the two slots of `Q_QDD(v)` are equal on every one
of the 313 carrier elements. The pair is the diagonal of
`M_4(Q) x M_4(Q)`. The ordered form is retained because the registered scope of
`QUADRATIC-DECODER-DATA` writes `Q(psi) = (psi psi^dagger, psi psi^T)`; whether
that registered form is satisfied in this degenerate diagonal sense is an owner
question, and it is raised in part 9 rather than assumed here.

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
`status`, following every existing `DEF-*` row. `SECTION` below is the section
of `canon/CANON.md` in which the eventual fold states these definitions; it is
filled at fold time and is not invented here.

```text
DEF-QDD-DOMAIN                 DEFINITION  -  -  L1  -  canon/CANON.md::SECTION
DEF-QDD-BALANCED-SECTION       DEFINITION  -  -  L1  -  canon/CANON.md::SECTION
DEF-QDD-AMPLITUDE              DEFINITION  -  -  L1  -  canon/CANON.md::SECTION
DEF-QDD-SIGMA4                 DEFINITION  -  -  L1  -  canon/CANON.md::SECTION
DEF-QDD-PAIRING                DEFINITION  -  -  L1  -  canon/CANON.md::SECTION
DEF-QDD-LOW-LINE               DEFINITION  -  -  L1  -  canon/CANON.md::SECTION
DEF-QDD-PROJECTOR-LOW          DEFINITION  -  -  L1  -  canon/CANON.md::SECTION
DEF-QDD-PROJECTOR-HIGH         DEFINITION  -  -  L1  -  canon/CANON.md::SECTION
DEF-QDD-BRANCH-WEIGHT-PAIRING  DEFINITION  -  -  L1  -  canon/CANON.md::SECTION
DEF-QDD-GRAM                   DEFINITION  -  -  L1  -  canon/CANON.md::SECTION
DEF-QDD-QPAIR                  DEFINITION  -  -  L1  -  canon/CANON.md::SECTION
DEF-QDD-MATTER-RECORD          DEFINITION  -  -  L1  -  canon/CANON.md::SECTION
DEF-QDD-DIRECT-WRITE           DEFINITION  -  -  L1  -  canon/CANON.md::SECTION
DEF-QDD-FACTOR-MAP             DEFINITION  -  -  L1  -  canon/CANON.md::SECTION
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
DEF-QDD-DOMAIN  DEF-ARCHITECTURE  REQUIRES
  the domain is a subset of the declared checkpoint carrier and inherits its
  definition boundary
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
DEF-QDD-QPAIR  DEF-QDD-GRAM  REQUIRES
  the ordered quadratic pair is formed on the carrier the Gram is defined on
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

`DEF-QDD-SIGMA4` and `DEF-QDD-DOMAIN` are the two roots of this subgraph;
`DEF-ARCHITECTURE` is the only existing item the subgraph attaches to, and
`QUADRATIC-DECODER-DATA` keeps its five existing outgoing edges unchanged.

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

**9.2 The ordered pair is diagonal.** `v^dagger = v^T` makes both slots of
`Q_QDD(v)` equal on all 313 carrier elements. Whether the registered
`Q(psi) = (psi psi^dagger, psi psi^T)` is satisfied in that degenerate sense is
an owner question, not a computation. A non-degenerate alternative would take
the dagger to be `sigma_4`, the conjugation of the amplitude field, which is
not the transpose; that choice would change the carrier and is not made here.

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
1  a further adversarial audit of this package, on the same terms as the one
   that produced AUDIT-QDD-BINDING-PACKAGE-V27.md
2  the proposed delta of part 7 applied to a scratch copy and shown to pass
   tools/check_ledger.py, with the PASS line recorded, and separately checked
   by hand against ruling 1 rather than against the tool alone
3  an owner decision on 9.2, the diagonal pair
4  only then, a decision on whether this belongs in a v28 manifest, and only
   after that, whether a formal probe may be preregistered
```

Nothing in this file authorizes a verifier, a run, a preregistration, a probe,
a fold, a tag, or a release.
