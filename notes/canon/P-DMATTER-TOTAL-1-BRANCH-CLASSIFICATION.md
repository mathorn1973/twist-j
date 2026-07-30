# P-DMATTER-TOTAL-1 branch classification amendment (NON-CANONICAL)

Status: `DRAFT / STOP-DEFINITION / CLASSIFICATION-FREEZE`

This amendment replaces an open-ended search over one cyclotomic family by
one finite, typed candidate class. It neither adopts a physical branch
dictionary nor claims to classify every possible `D_direct`. It creates no
Canon row, dependency, gate, probe, verifier, evidence, run, or status
change.

## Authority and baseline

```text
Canon:              Public Canon v15
state:              ACTIVE
tag:                canon-v15
activation commit:  8f4e176c5d76f519d3493e56e438aba7856e1f01
content commit:     a850753348583e611bf7ccd5aa074030dc7e12f5
Canon SHA-256:      53237ec25b3782e833367c998c049d19459189a21c2a36638dd9e1600335976b
Canon bytes:        89288
owner row:          QUADRATIC-DECODER-DATA [O]
controlling ruling: notes/canon/P-DMATTER-TOTAL-1-PREDEFINITION.md
draft baseline:     PR #113, commit
                    50f91898ad62d9d3f264cdbeac4ab9cd275942d1
scheduler:          DECODER_CORE / ROOT / STOP / FORMAL
```

The classification is proposal-local until this definition-only package is
reviewed, merged, and read back from public `main`. It remains
`NON-CANONICAL` after that readback unless a later authority action says
otherwise. Readback freezes this proposal; it does not adopt a dictionary,
complete the QDD contract, or change the public status.

## 1. Exact scope

Let the ambient root-injection universe be

```text
I_root = {e=(e_0,e_1,e_2,e_3) in (Z/5Z)^4 :
          e_0,e_1,e_2,e_3 are pairwise distinct}.
```

Thus `|I_root|=5*4*3*2=120`. For `e in I_root`, define the ordered
root-power basis

```text
B_e = (zeta^(e_0),zeta^(e_1),zeta^(e_2),zeta^(e_3)).
```

Write `m_J` for the public multiplication-by-`J` operator and `M_J` for
the public coordinate matrix used by `CODEC-TR4`. Define

```text
Verb(e)  iff  [m_J]_(B_e) = M_J entrywise over Q,
B5 = {B_e : e in I_root and Verb(e)}.
```

The exact surviving basis class is

```text
B5 = {B_k : k in Z/5Z},
B_k = (zeta^k,zeta^(k+1),zeta^(k+2),zeta^(k+3)).
```

This completeness statement has a short coordinate proof. The first,
second, and fourth columns of `[m_J]_(B_e)=M_J` force, modulo five,

```text
e_2=e_0+2,
e_3=e_1+2,
e_0=e_3+2.
```

Pairwise distinctness then gives

```text
e=(k,k+1,k+2,k+3).
```

The remaining column follows from
`1+zeta+zeta^2+zeta^3+zeta^4=0`. Conversely every displayed consecutive
window has the required matrix because multiplication by `zeta^k` commutes
with `m_J`. Hence these five and only these five members of `I_root`
survive.

`B5` is complete only inside the separately frozen universe of the 120
ordered injections of four slots into the five fifth roots. No completeness
beyond that injection universe is claimed. In particular, this note does
not classify arbitrary rational bases, arbitrary rank-one splittings,
nonlinear readouts, histories, ensembles, state reconstruction, post-state
instruments, or all maps with the public shape
`K0 -> MatterData_quadratic`.

Membership in `B5` therefore cannot prove that a genuinely prior public
`D_direct` exists or that none exists. It only makes the current
root-injection ambiguity finite and decidable.

## 2. Candidate data

Let

```text
K = Q(zeta),                    zeta = zeta_5,
bar(x) = sigma_4(x),            Tr = Tr_(K/Q),
<x,y>_tr = (1/5) Tr(x bar(y)),
B0 = (1,zeta,zeta^2,zeta^3).
```

For `k in Z/5Z`, define

```text
U_k : K -> K,                  U_k(x)=zeta^k x,
iota_k(v) = sum_(i=0)^3 v_i zeta^(k+i) = U_k iota_0(v),
lambda_k = sum B_k = -zeta^(k+4),
L_k = Q lambda_k,
H_k = L_k^perp,
Pi_k = the <.,.>_tr-orthogonal projector onto L_k.
```

The candidate is the labeled tuple

```text
c_k = (k,B_k,iota_k,L_k,H_k,Pi_k).
```

The exact candidate class used below is

`C5 = {c_k : k in Z/5Z}`.

Candidate identity is literal:

```text
c_k = c_l  iff  k=l.
```

The label `k` and basis identifier `B_k` are candidate metadata. They are
not fields of the proposed `MatterData` record below. No implicit gauge
quotient discards them; record equivalence is separately and extensionally
defined in Section 4.

## 3. Base admissibility without the target answer

Define `Adm_base(c_k)` by the following pre-result conditions:

1. `B_k` belongs to the exact class `B5` above;
2. `B_k` is a rational basis of `K`;
3. multiplication by `J` has the frozen matrix `M_J` in `B_k`;
4. `<.,.>_tr` is positive definite and has matrix
   `G=I_4-(1/5)11^T` in `B_k`;
5. `Pi_k` is the exact trace-orthogonal projector onto
   `L_k=Q sum(B_k)`;
6. the ZERO/NONZERO record below is total on `Veff=ell(F_5)^4`.

`Adm_base` contains no reference to `Qcan`, `F_Gram`, `A G`, a desired
factorization result, a measured value, or a preferred window. Thus it
cannot select a candidate merely because that candidate matches the #113
factor map.

Membership also does not certify provenance independence. Every `c_k`
remains disallowed as an independently published `D_direct` until a public
owner supplies the missing record ownership and dictionary.

## 4. One common record carrier and equality

For `v in Veff`, put

```text
w_k(v) = iota_k(v),
T_(k,v)(x) = w_k(v) <x,w_k(v)>_tr,
tau(v) = <w_k(v),w_k(v)>_tr,
s(v) = sum_i v_i.
```

The branch weights are defined from the frozen projector, not merely by
their later coordinate formulas:

```text
w_low^(k)(v)  = <Pi_k w_k(v),Pi_k w_k(v)>_tr,
w_high^(k)(v) = <(I-Pi_k)w_k(v),(I-Pi_k)w_k(v)>_tr.
```

Exact evaluation gives the `k`-independent identities

```text
tau(v)        = sum_i v_i^2 - s(v)^2/5,
w_low^(k)(v)  = s(v)^2/20,
w_high^(k)(v) = sum_i v_i^2 - s(v)^2/4,
w_low^(k)(v) + w_high^(k)(v) = tau(v).
```

For `v != 0`, define the normalized density operator before choosing any
matrix representation:

```text
rho_(k,v) = T_(k,v) / tau(v).
```

All density endomorphisms in the proposed record are represented in the one
fixed basis `B0`. With `M_k=[U_k]_B0`,

```text
[T_(k,v)]_B0 = M_k (v v^T G) M_k^(-1).
```

Define `R_k(v)` with the same total tags as the #113 candidate:

```text
R_k(v) =
  ZERO {
    support_state            = ZERO,
    total_weight             = 0,
    branch_weights           = (0,0),
    density_state            = ZERO_DENOMINATOR,
    normalized_weight_state  = ZERO_DENOMINATOR
  }                                              if v = 0

| NONZERO {
    support_state            = NONZERO,
    total_weight             = tau(v),
    branch_weights           =
        (w_low^(k)(v),w_high^(k)(v)),
    density_state            =
        DENSITY([rho_(k,v)]_B0),
    normalized_weight_state  =
        NORMALIZED((w_low^(k)(v),w_high^(k)(v)) / tau(v))
  }                                              if v != 0.
```

Record equality is literal equality of the tag, rational scalar fields,
ordered branch weights, and entrywise `M_4(Q)` density in `B0`.

The induced record equivalence is exact functional equality:

```text
c_k ~_R c_l  iff  R_k(v)=R_l(v) for every v in Veff.
```

No conjugacy, moving-basis equality, unlabeled branch permutation, or
physical gauge is part of `~_R`. Candidate metadata are not record fields,
so this extensional equality does not redefine candidate identity.

## 5. Exact base classification

Multiplication by `zeta^k` is trace-unitary. Consequently all five
candidates have identical scalar subrecords on every input:

```text
support_state,
total_weight,
branch_weights,
normalized_weight_state.
```

Their density fields instead obey

```text
T_(k,v) = U_k T_(0,v) U_k^(-1).
```

Thus `[T_(k,v)]_(B_k)=v v^T G` has the same numbers in each moving basis,
but the common fixed-`B0` records are generally different. Already
`v=(1,0,0,0)` separates the five range lines `Q zeta^k`. In particular,

```text
rho_(0,(1,0,0,0))(1)=1,
rho_(1,(1,0,0,0))(1)=-zeta/4,
```

while both have

```text
(tau,w_low,w_high)=(4/5,1/20,3/4),
normalized weights=(1/16,15/16).
```

Therefore the proposal-local base result is

```text
scalar subrecord classes: 1,
full typed record classes: 5,
base classification:       NONUNIQUE.
```

Calling the five moving-basis matrices identical would silently change the
record equality. Quotienting by `U_k` conjugacy would be a new gauge
dictionary and is not authorized here.

## 6. Conditional Galois classification

To distinguish the window index from the missing-root index, define for
`m in Z/5Z`

```text
L^(m) = Q zeta^m,
P^(m)(x) = (1/4) Tr(x zeta^(-m)) zeta^m.
```

Then

```text
Pi_k = P^(k+4).
```

For `sigma_a(zeta)=zeta^a`, `a in F_5^*`, exact conjugation gives

```text
sigma_a P^(m) sigma_a^(-1) = P^(a m),
sigma_a Pi_k sigma_a^(-1) = Pi_(a(k+4)-4),
```

with indices modulo five. Hence the family of five branch projectors is
Galois-covariant and exactly one member is invariant under the full group
`Gal(K/Q)`:

```text
m=0,
k=1,
B_1=(zeta,zeta^2,zeta^3,zeta^4),
L^(0)=Q,
H^(0)=ker(Tr).
```

Define the optional filter

```text
Adm_GalSplit(c_k) := Adm_base(c_k)
                     and sigma_a Pi_k sigma_a^(-1)=Pi_k
                         for every a in F_5^*.
```

Within `C5`, the proposal-local conditional result is

```text
|{c in C5 : Adm_GalSplit(c)} / ~_R| = 1.
```

This is `UNIQUE-ALGEBRAIC` only under the additional filter. It is not an
earned physical selection under current Public Canon.

The invariant object is only the branch projector. Galois conjugation sends
`J` to `sigma_a(J)`, so no invariance of the complete fixed-`J`
architecture, source checkpoint, decoder map, density record, or
`MatterData` record is claimed. A full equivariance claim would first need
typed Galois actions on every source and target carrier.

## 7. Complete mathematical outcome space

Any future classification decision on a publicly frozen candidate universe
must use all four mathematical outcomes:

```text
UNIQUE-ALGEBRAIC
    exactly one admissible equivalence class survives.

NONUNIQUE
    at least two inequivalent admissible classes survive.

EMPTY
    the complete class contains no admissible candidate.

STOP
    the candidate universe, equality, equivalence, admissibility, action,
    completeness proof, typing, or decision procedure is incomplete.
```

`PASS-EARNED` is not used. Even `UNIQUE-ALGEBRAIC` does not adopt a physical
dictionary and does not change `QUADRATIC-DECODER-DATA`.

Two later governance states must remain distinct from those classification
outcomes:

```text
FILTER-ADOPTED
    a reviewed owner fold adopts Adm_GalSplit as a scoped dictionary clause.
    QUADRATIC-DECODER-DATA remains [O], and D_direct may remain UNRESOLVED.

ADOPTED-D
    a later authority action registers a complete public dictionary and
    write rule with all required ownership, bridge, dependency, manifest,
    and layer-gate identifiers resolved.
```

Neither governance state is produced by this classification. In particular,
`ADOPTED-D` is not an automatic `QUADRATIC-DECODER-DATA [O] -> [D]`
transition.

## 8. Owner routing and debt firewall

After the owner readback in `V15-OWNER-FOLD-107-109.md`, `Adm_GalSplit`
remains `NOT ADOPTED`. No `DECLINE` fold or new completion-contract slot is
required. The five-window root-injection search is closed proposal-locally.
Search outside `C5` is unscheduled and may resume only when a genuinely prior
typed readout candidate is supplied.

Only adoption requires a separate reviewed owner fold. Such a fold would
state that, within `C5`, physical branch admissibility requires invariance
of the branch projector under the full group `Gal(K/Q)`. It would select
`c_1` only inside that bounded class.

Adoption could not silently inherit the present fixed-`B0` realization. It
would have to re-freeze the amplitude bridge, basis identifier, record
equality, factor map, dependencies, and layer scope consistently. The
factorization would remain a derived algebraic audit, not a blind probe.

The proposed clause is new. It is not supplied by `ALPHA-SEED`,
`MEASURE-SPATIAL-ONLY`, `MEASURE-BORN-VERB`, `CODEC-TR4`, or
`CARRY-PENTAD`.

No new frontier owner is needed. `Adm_GalSplit` itself creates no gate. It
neither closes nor duplicates the already-open QDD bridge-gate requirement.
That gate remains `UNRESOLVED` until its source, target, `beta`, and `iota`
maps are publicly typed.

## 9. Routing after this amendment

```text
CURRENT PUBLIC STATE:
    QUADRATIC-DECODER-DATA [O]
    scheduler STOP

PROPOSAL-LOCAL ALGEBRA:
    C5 base classification NONUNIQUE (five full-record classes)
    scalar subrecord one class
    C5 plus Adm_GalSplit UNIQUE-ALGEBRAIC (one branch projector)

DEFAULT OWNER STATE AFTER READBACK:
    Adm_GalSplit NOT ADOPTED
    D_direct UNRESOLVED

OWNER ROUTING AFTER V15-OWNER-FOLD-107-109:
    C5 root-injection search CLOSED PROPOSAL-LOCALLY;
    Adm_GalSplit NOT ADOPTED; optional adoption DEFERRED;
    outside-C5 search UNSCHEDULED until a genuinely prior typed readout is
    supplied;
    D_direct UNRESOLVED and no classification result supplies it.

NEXT PUBLIC ACTION:
    none until a complete optional adoption package or a genuinely prior
    typed readout exists.

FORMAL PROBE:
    forbidden; the displayed results are proof-first finite algebra and the
    controlling completion manifests remain incomplete.
```

The frontier count remains unchanged. This amendment reduces only
proposal-local `C5` search ambiguity; it closes no Canon obligation, public
STOP debt, or completion-contract slot.
