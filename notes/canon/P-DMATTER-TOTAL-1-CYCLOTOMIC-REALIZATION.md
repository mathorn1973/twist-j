# P-DMATTER-TOTAL-1 cyclotomic realization (NON-CANONICAL)

Status: `DRAFT / STOP-DEFINITION / ALGEBRAIC-LEMMA-ONLY`

This companion note audits the proposal at commit
`aa28f6d` and retains only its exact algebraic content. It does not adopt
that proposal's claim of an independently published `D_direct`, does not
create a physical dictionary, and does not authorize a probe, verifier,
run, or status change.

## Authority and baseline

```text
Canon:              Public Canon v14
state:              ACTIVE
tag:                canon-v14
activation commit:  f278855cada75691142c02ebad1a75ecc2730db3
content commit:     ab4ea07d15ab1cfa0c403d3c2a74164011ffa0e7
Canon SHA-256:      f9f06af42a9b0b63f806603ddc671ebe6a9e5014b50d230da04a28722ed1a6a2
Canon bytes:        87061
owner row:          QUADRATIC-DECODER-DATA [O]
controlling ruling: notes/canon/P-DMATTER-TOTAL-1-PREDEFINITION.md
draft baseline:     PR #113, commit
                    9d49a1fa5691474180ff341cb59fe9b5ee2596bc
scheduler:          DECODER_CORE / ROOT / STOP / FORMAL
```

The merged predefinition ruling, not draft PR #113, is the controlling
decision. The construction below is a basis-fixed cyclotomic realization of the
Gram factor already proposed in #113. A second implementation can audit the
algebra, but implementation independence is not definition independence.

## 1. Frozen algebraic carrier

Let

```text
K = Q(zeta),             zeta = zeta_5,
bar(x) = sigma_4(x),     Tr = Tr_(K/Q),
B0 = (1,zeta,zeta^2,zeta^3).
```

`B0` is the standard power basis used by the public `CODEC-TR4`
reproducer. This note imports no linear `CODEC-TR4` output into the
quadratic leg; it uses only the explicit algebraic basis convention.

For `v=(v_0,v_1,v_2,v_3)^T in Veff`, where
`Veff=ell(F_5)^4` is the finite balanced carrier of the #113 draft, define
the proposal-local coordinate isomorphism

```text
iota_B0(v) = v_0 + v_1 zeta + v_2 zeta^2 + v_3 zeta^3.
```

This is an algebraic coordinate map. It is not yet an
orbit-to-physical-amplitude dictionary, a layer gate, or a `D_matter` write
rule.

Define the rational trace pairing

```text
<x,y>_tr = (1/5) Tr(x bar(y)).
```

Complex conjugation is fixed here as the standard involution of the
cyclotomic CM field. This note does not select it after comparing numerical
outcomes with other Galois automorphisms.

## 2. Exact trace-Gram identity

For `a,b in {0,1,2,3}`,

```text
(1/5) Tr(zeta^(a-b)) = delta_(a,b) - 1/5.
```

Consequently the matrix of `<.,.>_tr` in `B0` is exactly

```text
G = I_4 - (1/5) 1 1^T,
```

the normalized Gram used by the #113 factor candidate. Thus, for
`w=iota_B0(v)` and `s=sum_i v_i`,

```text
m_tr(w) = <w,w>_tr
        = v^T G v
        = sum_i v_i^2 - s^2/5.
```

This is the useful content of the new proposal: the coordinate Gram is the
cyclotomic trace Gram in the already frozen power basis. No shifted frame is
needed.

## 3. The low line and high subspace without a frame selector

Put

```text
lambda_B = 1 + zeta + zeta^2 + zeta^3 = -zeta^4,
L_B      = Q lambda_B.
```

Let `pi_low` be the `<.,.>_tr`-orthogonal projector onto `L_B` and
`pi_high=I-pi_low`. Since

```text
<lambda_B,lambda_B>_tr = 4/5,
<w,lambda_B>_tr        = s/5,
```

one has

```text
pi_low(w) = (s/4) lambda_B,
w_low     = <pi_low(w),pi_low(w)>_tr = s^2/20,
w_high    = <pi_high(w),pi_high(w)>_tr
          = sum_i v_i^2 - s^2/4,
w_low + w_high = m_tr(w).
```

In coordinates, `pi_low` and `pi_high` are precisely the #113 projectors

```text
E_low  = (1/4) 1 1^T,
E_high = I_4 - E_low.
```

The previously proposed shifted window
`(zeta,zeta^2,zeta^3,zeta^4)` is therefore unnecessary. It is a cyclic
translate of `B0`, not the public power basis itself. Exact trace alignment
in that shifted window would be a new selector decision, not an inherited
public fact.

## 4. Typed rank-one operator

For `w in iota_B0(Veff)`, define

```text
T_w : K -> K,
T_w(x) = w <x,w>_tr.
```

If `A=vv^T`, then the exact matrix representation in the fixed basis is

```text
[T_w]_B0 = v v^T G = A G.
```

This equality supplies the missing representation map between
`End_Q(K)` and `M_4(Q)`; equality of density payloads below is componentwise
rational matrix equality in `B0`. No quotient by frame permutations is
introduced.

Define the total algebraic record

```text
R_cyc(w) =
  ZERO {
    support_state            = ZERO,
    total_weight             = 0,
    branch_weights           = (0,0),
    density_state            = ZERO_DENOMINATOR,
    normalized_weight_state  = ZERO_DENOMINATOR
  }                                      if w = 0

| NONZERO {
    support_state            = NONZERO,
    total_weight             = m_tr(w),
    branch_weights           = (w_low,w_high),
    density_state            = DENSITY([T_w]_B0 / m_tr(w)),
    normalized_weight_state  = NORMALIZED((w_low,w_high) / m_tr(w))
  }                                      if w != 0.
```

These tags and payload equalities now match the proposal-local
`CandidateQuadraticData` type in #113 exactly.

## 5. Algebraic lemma, not a blind target

For every `v in Veff`, with `Qcan(v)=(A,A)`, direct substitution gives

```text
R_cyc(iota_B0(v)) = F_Gram(Qcan(v)).
```

Indeed, the total and branch weights agree by Sections 2 and 3, and the
density numerators agree by Section 4. Also `iota_B0(v)=0` iff `v=0`, so
the zero tags agree.

This is a proved algebraic lemma once the displayed definitions are chosen.
Exhaustive enumeration of 625 piston values or 15,625 anchored checkpoints
can regression-test an implementation, but cannot turn this definitional
realization into an independent scientific test.

The finite consequences remain those of the #113 algebraic candidate:

```text
|image(Qcan)| = 313,
zero anchored fiber size = 25,
each of 312 nonzero sign-fiber sizes = 50.
```

## 6. Public-scope audit

The exact public rows support only the following bounded imports:

```text
CODEC-TR4              the standard power-basis convention only
ALPHA-SEED             the Galois Gram and normalized spectrum
READING-SPLIT          the registered quadratic leg is a Born-square leg
COUPLINGS-DETERMINE    the finite Gram-normalized density identity
```

They do not publish the composite checkpoint-to-field-to-record map above.
In particular:

- `MEASURE-BORN-VERB` covers the named amplitudes `1+zeta^k`; it does not
  authorize an arbitrary piston amplitude `sum v_i zeta^i` or the full
  record `R_cyc`.
- `MEASURE-SPATIAL-ONLY` supplies weights in its declared decomposition; it
  does not own this two-branch piston readout.
- `CARRY-PENTAD` explicitly selects no exponent, gauge, physical reading,
  measure, or L2--L6 lift. It supplies no permutation quotient here.
- A public linear `CODEC-TR4` output remains excluded from the QDD leg.

Accordingly, the claims "zero new atoms", "independently published
readout", and "exponent relabeling is exact gauge" are not adopted.

## 7. Disposition of incubation results

The hashes quoted at commit `aa28f6d` have no public, resolvable artifact
bundle on that branch. They are therefore private exploratory provenance,
not evidence. The reported computation has already exposed the
factorization and frame outcomes; a later fresh pin cannot make the same
question blind retroactively.

If this algebraic lemma is adopted publicly, a future verifier may certify
the proof and implementation on two platforms. It must be described as a
reproducibility or conformance certificate, not as an independent selection
of the definitions above.

## 8. One explicit owner decision

The new note reduces the remaining ambiguity to a binary governance choice:

```text
ROUTE A -- explicit dictionary adoption
    Publish a new, scoped dictionary that owns
    beta -> iota_B0 -> R_cyc as the D_quadratic write rule.
    Then the displayed factorization is a derived lemma/audit target, not a
    blind scientific outcome. The complete record, stage, leg, measure,
    dependency, layer-gate, and closure manifests are still required.

ROUTE B -- retain the independent-readout requirement
    Treat R_cyc only as a realization of F_Gram. It does not fill
    D_direct. A genuinely prior public readout with independently owned
    fields is still required.
```

The companion amendment
`P-DMATTER-TOTAL-1-BRANCH-CLASSIFICATION.md` refines this fork. It freezes
the five verb-compatible windows as a bounded candidate class with one fixed
record equality. Their scalar subrecords agree, but their fixed-basis density
operators form five distinct classes. Within `C5`, invariance of the branch
projector under the full group `Gal(Q(zeta_5)/Q)` selects one split only
after it is added as a new admissibility clause. Neither the bounded
`NONUNIQUE` result nor the conditional algebraic uniqueness
adopts that clause or supplies `D_direct`.

Until an owner explicitly selects Route A, Route B is the conservative
default. Route A can be adopted only by a separate definition-only decision
that is reviewed, merged, and read back from public `main`; a private owner
selection is not adoption. This avoids silently growing the dictionary while
preserving the exact algebraic progress.

## 9. Residual ledger

| Surface | Result of this companion | State |
| --- | --- | --- |
| coordinate Gram versus trace Gram | proposal-local proof using the public reproducer's basis convention | contract state unchanged |
| low/high weights | proposal-local field realization | contract state unchanged |
| density representation/equality | proposal-local `End_Q(K)` to `M_4(Q)` map | contract state unchanged |
| frame/gauge | no shifted frame and no quotient used | no new contract debt |
| independent public `D_direct` | not supplied | `UNRESOLVED` |
| generic physical Born dictionary | not supplied | `UNRESOLVED` |
| complete `MatterData_quadratic` ownership | not supplied | `UNRESOLVED` |
| exact dependencies and acyclicity | not supplied | `UNRESOLVED` |
| bridge endpoints and public gate | not supplied | `UNRESOLVED` |
| completion-contract manifests | not supplied | `UNRESOLVED` |

`QUADRATIC-DECODER-DATA` therefore remains `[O]`, the scheduler remains
`STOP`, and no Canon frontier count changes.
