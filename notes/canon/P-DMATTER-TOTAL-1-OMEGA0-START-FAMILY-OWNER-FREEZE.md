# P-DMATTER-TOTAL-1 Omega0 Start-Family Owner Freeze (NON-CANONICAL)

```text
STATUS:                 OWNER-ADOPTED START-FAMILY FREEZE
ACTION:                 DEFINITION-ONLY; DERIVED RESULTS ARE PROPOSAL-LOCAL EXACT CONSEQUENCES
AUTHORITY:              NOT CANON
SCOPE:                  PROPOSAL-LOCAL / L1 / PUBLIC-K CANDIDATE ONLY
PUBLIC CANON:           Public Canon v24
PUBLIC CANON TAG:       canon-v24
PUBLIC MAIN BASE:       f6f797739be21acfa70851be544c994ea17b7f5a
STACKED PREDECESSOR:    35c98d69abbca5476cdf952e695dd1434236a2db
PREDECESSOR PR:         189, itself stacked on 188 and 183
PREDECESSOR ARTIFACT:   P-DMATTER-TOTAL-1-PUBLIC-K-REPRESENTATION-PREDEFINITION.md
PREDECESSOR BLOB:       a44c43cba85b494d4ab42d7261cf88b6987adfad
PREDECESSOR SHA-256:    ab098149745cac84c04d70314286f5bb9f7e7527be001756cfce6db417bd5de2
PREDECESSOR BYTES:      11591
CLAIM ISSUE:            107
CLAIM COMMENT:          5092466942
OWNER START FAMILY:     Omega_0, proposal-local
OWNER REPRESENTATION:  NONE
FORMAL RUN:             NONE
CANON/TABLE/GATE CHANGE: NONE
QDD STATUS:             O / STOP, unchanged
READY-FOR-CLASSIFICATION: NO
```

The owner instruction was:

```text
zmrazit jinou rodinu muzeme zkusit
```

PR #189 named one concrete restricted alternative to full `Omega`. This
ruling interprets the instruction as the proposal-local choice

```text
S_beta=Omega_0={0} x X subset Omega.                 (1)
```

This choice was made with full post-hoc disclosure. `Omega_0`, `K0`, the
full-`Omega` representation results, and existing decoder consequences were
known beforehand. No favorable consequence below is a blind prediction. If a
later classification uses this start family, changing it after opening fires
`FIRE-POSTHOC`.

## 0. Firewall

```text
PUBLIC-K-ADOPTION
    Omega_0, K0, or a quotient is called public K or its intended meaning;
DOMAIN-OR-OCCURRENCE-ADOPTION
    any displayed carrier is bound to dom(D_matter), occurrence, or measure;
OMEGA0-K0-TYPE-COLLAPSE
    the subset Omega_0 of Omega is identified with its sequence image K0;
INVARIANT-FAMILY-OVERCLAIM
    Omega_0 is called U-invariant or a transversal of all full-Omega tails;
FULL-OMEGA-TRANSFER
    a theorem from PR #189 is reused without recomputing Omega_0 fibers;
TAIL-AS-OMEGA0-HEADED
    the tail quotient is called a HeadedOrbitRep(U;Omega_0);
SYNC-READ-AS-GENESIS-DESCENT
    a new time-3 read is called the descent of the time-0 read;
OPEN-ROW-PROMOTION
    KERNEL-Z6-SYNCHRONIZATION [O] is imported as a public theorem;
STATUS-PROMOTION
    a public ID, dependency, layer, gate, completion field, or status moves.
```

The rejected `C-ARCH-UNIVERSALITY-1` package is not an input, precedent,
evidence source, or comparison class.

## 1. The adopted start family

Retain the public definitions

```text
X=F_5^6,
Omega=N_0 x X,
U(n,x)=(n+1,F_(theta_n)(x)).
```

Adopt (1) with literal equality

```text
(0,x) Eq_Omega0 (0,y) iff x=y
```

and the literal inclusion `Inc_0:Omega_0->Omega`. This is a head family, not
an invariant subsystem:

```text
U(0,x)=(1,F_0(x)) notin Omega_0.
```

The exact proposal-local premise frozen here is:

```text
OMEGA0-START-PREMISE
    the counter is zero and every checkpoint x in X is admitted as a head.
```

This premise is an owner choice. It is not derived from `J`, `U`, the tail
quotient, or a decoder output, and it does not define the complete public
admissibility class.

Retain the already owner-adopted pointed carrier and equality

```text
kappa_x(m)=U^m(0,x),
K0={kappa_x:x in X},
kappa_x Eq_K0 kappa_y iff x=y.
```

Define the restrictions

```text
OrbitOf_0(0,x)=kappa_x,
Head_0(kappa_x)=(0,x),
Trace_0(kappa_x,m)=U^m(0,x),
A_0(kappa_x)=OrbitAdjacentInput_beta(kappa_x).
```

Then `OrbitOf_0` and `Head_0` are equality-compatible inverses, `Trace_0`
realizes `U^m`, and `K0` is a `HeadedOrbitRep(U;Omega_0)`. The subset
`Omega_0` and the sequence carrier `K0` remain different types.

The literal-range representation is

```text
R_x={U^m(0,x):m>=0},
Krange_0={R_x:x in X},
R_x Eq_Krange0 R_y iff R_x=R_y iff x=y.
```

Each `R_x` has the unique minimum-counter element `(0,x)`. Therefore the
restrictions of the PR #189 range maps give an equality-, head-, and
trace-preserving isomorphism

```text
Phi_0(kappa_x)=R_x,
Psi_0(R_x)=kappa_x,
Trace_range0(R_x,m)=U^m(0,x),
A_range0=A_0 o Psi_0,
A_range0 o Phi_0=A_0.                                (2)
```

This proves an encoding equivalence inside the adopted family. It does not
select public `K`.

## 2. Self-contained synchronization lemma

For `z in F_5`, put `X_z={x:z_6(x)=z}` and

```text
F_t(x)=g_((z_6(x)+2t) mod 5)(x),
E_n(x)=pr_checkpoint(U^n(0,x)).
```

Direct summation of the six public generator coordinates gives

```text
z_6(a(x))=z,
z_6(b(x))=-z,
z_6(c(x))=2-z,
z_6(d(x))=2-z,
z_6(e(x))=3-z                              mod 5,
```

and direct substitution in those formulas gives `g_i^2=id`. Combining these
facts with the selector gives the sheet table

```text
             input sheet z
             0  1  2  3  4
t=0          0  4  0  4  4
t=1          2  1  1  3  1.
```

On each fixed input sheet the selector is fixed, so the displayed arrow is
the restriction of one involutive generator. It is a bijection between
3125-element sheets. Since

```text
(theta_0,theta_1,theta_2)=(0,1,1),
image sheets at n=0,1,2,3 are
{0,1,2,3,4}, {0,4}, {1,2}, {1},
```

every restriction

```text
E_3|X_z:X_z->X_1
```

is a bijection. For `n>=3`, put

```text
q_n=4+2 theta_(n-1) mod 5.
```

Here `q_n` is a proof-local sheet-label abbreviation, not the checkpoint
coordinate `q`.

Then `q_3=1`, and the table gives the bijection

```text
F_(theta_n)|X_(q_n):X_(q_n)->X_(q_(n+1)).
```

Hence, for every `n>=3`, there is a bijection
`H_(3,n):X_1->X_(q_n)`, with `H_(3,3)=id`, such that

```text
E_n=H_(3,n) o E_3.                                   (3)
```

The symbols `q_n` and `H_(3,n)` are proof-local abbreviations. They define no
independent interface ID or future dependency.

Equation (3) is proved here from the generators and sheet table. The open
`KERNEL-Z6-SYNCHRONIZATION [O]` row is a consistency control, not a theorem
premise, and its public status does not move.

## 3. The Omega0 common-tail quotient

Define

```text
kappa_x ~tail0 kappa_y
iff exists p,q>=0: Shift^p(kappa_x)=Shift^q(kappa_y),

Ktail_0=K0/~tail0,
pi_0(kappa)=[kappa],
[kappa_x] Eq_Ktail0 [kappa_y] iff kappa_x ~tail0 kappa_y.
```

Equality of the zeroth autonomous states after shifting forces `p=q`, because
their counter coordinates are `p` and `q`. Thus a common tail is equivalent
to `E_n(x)=E_n(y)` at one common time `n`.

If `n<=3`, determinism gives equality at time 3. If `n>=3`, the bijection in
(3) gives equality at time 3. Conversely, equality at time 3 gives equal
shifted sequences. Therefore

```text
kappa_x ~tail0 kappa_y iff E_3(x)=E_3(y).             (4)
```

Consequently:

```text
|K0|=15625,
|Ktail_0|=3125,
every tail0 class has exactly five genesis heads,
one head lies in each initial sheet X_z.
```

The global one-sheet synchronization depth is minimally 3: the image uses
five, two, two, then one sheet at times 0, 1, 2, 3.

Two exact controls are

```text
x=(0,0,0,0,2,1), y=(0,0,0,0,3,1),
F_0(x)=F_0(y)=(2,1,3,4,4,0),

x'=(0,0,0,0,2,1), y'=(2,1,3,4,2,0),
E_1(x')!=E_1(y'), E_2(x')!=E_2(y'),
E_3(x')=E_3(y')=(0,0,0,0,0,1).
```

A non-formal exhaustive audit of all 15625 checkpoints gave image ranks

```text
15625, 6250, 6250, 3125, 3125, 3125, 3125
```

for `E_0,...,E_6`, with 3125 time-3 fibers, all of size five and one seed per
initial sheet. This is a disclosed exact audit, not evidence or a formal run.

### 3.1 Adversarial genesis-sheet control

The all-checkpoint premise above is not encoded by the quotient. For every
nonempty `Z subset F_5`, define

```text
X_Z=union_(z in Z) X_z,
Omega_(0,Z)={0} x X_Z,
K_(0,Z)={kappa_x:x in X_Z}.
```

Restricting (4) gives a canonical bijection

```text
K_(0,Z)/~tail0 -> X_1,    [kappa_x] |-> E_3(x).       (5)
```

Every quotient in (5) has 3125 classes, but every class contains exactly
`|Z|` genesis heads, one from each selected sheet. If `Z subset W`, inclusion
induces the identity on `X_1` under (5). Thus the tail quotients of all
nonempty genesis-sheet families are canonically equivalent. The quotient
does not determine which genesis sheets were selected, and its quotient
projection has fiber size `|Z|`. Multiplicity changes when `|Z|` changes;
equal-size choices remain indistinguishable by multiplicity alone.

This is a local tail-universality theorem and an adversarial control on the
owner premise. It does not adopt any `Omega_(0,Z)` other than
`Omega_(0,F_5)=Omega_0`, and it shows that tail agreement alone cannot force
the all-five-sheet choice.

## 4. What descends, and what changes semantics

For fixed `n`, define

```text
State_n(kappa_x)=(n,E_n(x)),
A_n(kappa_x)=StateAdjacentInput_beta(n,E_n(x)).
```

These two displayed map families carry the proposal-local IDs
`CAND-QDD-MAP-FAMILY-K0-FIXED-TIME-STATE-BETA` and
`CAND-QDD-MAP-FAMILY-K0-FIXED-TIME-ADJACENT-BETA`.

The first map is constant on the fibers (4) exactly when `n>=3`. For fixed
`theta_n`, `AdjacentInput_beta(theta_n,-)` is injective because its tagged
preparation payload retains `kappa_(E_n(x))`. Therefore `A_n` is constant on
the same fibers exactly when `n>=3`.

It follows that:

```text
Head_0=State_0                           DOES NOT DESCEND
the complete Trace_0                     DOES NOT DESCEND
A_0                                      DOES NOT DESCEND
State_n and A_n, n>=3                    DESCEND
```

In particular, the first control above has equal tails but distinct genesis
heads and distinct `A_0` values.

Put

```text
S_3={3} x X_1,
(3,x) Eq_S3 (3,y) iff x=y,
SyncHead_3([kappa_x])=(3,E_3(x)),
TailOf_3(3,y)=[kappa_x] for any x with E_3(x)=y,
Trace_sync([kappa_x],m)=U^m(3,E_3(x)),
A_sync([kappa_x])=StateAdjacentInput_beta(3,E_3(x)).
```

Equation (4) makes the formulas independent of the representative.
Surjectivity of every `E_3|X_z` makes `TailOf_3` total and inverse to
`SyncHead_3`. Totality of `Trace_sync` and `A_sync` uses public `U` and the
already adopted total `StateAdjacentInput_beta`. Thus all four maps are
total and equality-compatible, and `Ktail_0` is a
`HeadedOrbitRep(U;S_3)` with synchronized future trace.

This is not a headed representation of `Omega_0`. `SyncHead_3` is a new
time-3 head, and `A_sync` is a new time-3 source-position read. Neither is the
descent of the genesis head or `A_0`.

## 5. Conditional three-candidate decision

Freeze only the comparison class

```text
Rep_3(Omega_0)={K0,Krange_0,Ktail_0}.
```

Require a candidate to retain the adopted `Omega_0` head, complete trace, and
`A_0`, up to exact transport. Then:

```text
K0 and Krange_0       one head/trace/A_0-preserving equivalence class;
Ktail_0               excluded by (4) and the non-descent results.
```

Thus `Rep_3(Omega_0)` has exactly one admissible equivalence class under the
retained conditional dictionary. This is not an exhaustive classification of
all representations and not public uniqueness. Choosing `S_3` would instead
be a new owner start-family and source-position decision.

## 6. Dependencies, identifiers, and public boundary

| result | exact dependencies | proposal layer/gate |
|---|---|---|
| `Omega_0`, inclusion | `OMEGA0-START-PREMISE` / `CAND-QDD-OWNER-START-FAMILY-OMEGA0-BETA`; `DEF-CHECKPOINT`, `DEF-ODOMETER-ORBIT`, `DEF-AUTONOMOUS-STATE` | L1 / none |
| `K0`, head, trace | inherited anchored-`K0` carrier/equality plus `U` | L1 -> L1 / none |
| (2) range transport | PR #189 maps restricted to `Omega_0` | L1 -> L1 / none |
| (3) synchronization | `DEF-CHECKPOINT`, `DEF-ODOMETER-ORBIT`, `DEF-AUTONOMOUS-STATE`, `DEF-KERNEL-GENERATORS`, `DEF-SELECTOR`; direct coordinate sums | L1 / none |
| (4) tail fibers | counter equality, determinism, (3) | L1 / none |
| (5) genesis-sheet tail universality | (4), `E_3|X_z:X_z->X_1` bijective | L1 / none |
| fixed-time descent iff | (3), (4), both displayed controls; PR #188 `CAND-QDD-MAP-ADJACENT-INPUT-BETA` injectivity and `CAND-QDD-MAP-STATE-ADJACENT-INPUT-BETA` | L1 -> L1 / none |
| synchronized `S_3` representation | `E_3` surjectivity, (4), `U`, `StateAdjacentInput_beta` | L1 -> L1 / none |
| three-candidate decision | `OMEGA0-START-PREMISE`, (2), `CAND-QDD-CERT-KTAIL-OMEGA0-GENESIS-NONDESCENT`, retained head/trace/`A_0` requirement | L1 / none |

Inherited `K0` IDs remain

```text
CAND-QDD-KERNEL-SOURCE-K0-ANCHORED-N0
CAND-CARRIER-ANCHORED-ORBITS-K0
CAND-EQ-POINTED-FORWARD-SEQUENCE
```

New proposal-local IDs are

```text
CAND-QDD-OWNER-START-FAMILY-OMEGA0-BETA
CAND-QDD-START-FAMILY-OMEGA0-BETA
CAND-QDD-EQ-START-FAMILY-OMEGA0-BETA-LITERAL
CAND-QDD-MAP-OMEGA0-INTO-OMEGA-BETA
CAND-QDD-MAP-ORBIT-OF-OMEGA0-BETA
CAND-QDD-MAP-HEAD-K0-OMEGA0-BETA
CAND-QDD-MAP-TRACE-K0-OMEGA0-BETA
CAND-QDD-MAP-ORBIT-ADJACENT-INPUT-OMEGA0-BETA
CAND-QDD-CERT-OMEGA0-K0-HEADED-TRACE-BIJECTION
CAND-QDD-CARRIER-KRANGE-OMEGA0-BETA
CAND-QDD-EQ-KRANGE-OMEGA0-EXTENSIONAL
CAND-QDD-MAP-K0-TO-KRANGE-OMEGA0-BETA
CAND-QDD-MAP-KRANGE-OMEGA0-TO-K0-BETA
CAND-QDD-MAP-TRACE-KRANGE-OMEGA0-BETA
CAND-QDD-MAP-KRANGE-ADJACENT-OMEGA0-BETA
CAND-QDD-CERT-K0-KRANGE-OMEGA0-HEAD-TRACE-ISO
CAND-QDD-CARRIER-KTAIL-OMEGA0-BETA
CAND-QDD-EQ-KTAIL-OMEGA0-COMMON-TAIL
CAND-QDD-MAP-K0-TO-KTAIL-OMEGA0-BETA
CAND-QDD-START-FAMILY-SYNC3-BETA
CAND-QDD-EQ-START-FAMILY-SYNC3-LITERAL
CAND-QDD-MAP-KTAIL-OMEGA0-SYNC-HEAD3-BETA
CAND-QDD-MAP-SYNC3-TO-KTAIL-OMEGA0-BETA
CAND-QDD-MAP-KTAIL-OMEGA0-SYNC-FUTURE-TRACE-BETA
CAND-QDD-MAP-KTAIL-OMEGA0-SYNC-ADJACENT-BETA
CAND-QDD-CERT-KTAIL-OMEGA0-E3-FIBRES
CAND-QDD-CERT-KTAIL-OMEGA0-MIN-SYNC-DEPTH-3
CAND-QDD-CERT-KTAIL-OMEGA0-GENESIS-NONDESCENT
CAND-QDD-CERT-KTAIL-OMEGA0-FIXED-TIME-DESCENT
CAND-QDD-MAP-FAMILY-K0-FIXED-TIME-STATE-BETA
CAND-QDD-MAP-FAMILY-K0-FIXED-TIME-ADJACENT-BETA
CAND-QDD-CERT-OMEGA0-THREE-REP-CONDITIONAL-ONE-CLASS
CAND-QDD-SCHEMA-GENESIS-SHEET-START-FAMILY
CAND-QDD-CARRIER-K0Z-TAIL-BETA
CAND-QDD-EQ-K0Z-COMMON-TAIL-E3
CAND-QDD-MAP-K0Z-TAIL-TO-X1-E3
CAND-QDD-CERT-GENESIS-SHEET-TAIL-UNIVERSALITY
```

Future public fields remain literal requirements, not adopted IDs:

```text
public_K_owner_item_id                 UNRESOLVED
public_K_start_family_id               UNRESOLVED
public_K_carrier_id                    UNRESOLVED
public_K_equality_id                   UNRESOLVED
public_K_orbit_of_map_id               UNRESOLVED
public_K_head_map_id                   UNRESOLVED
public_K_trace_map_id                  UNRESOLVED
public_K_position_data_id              UNRESOLVED
public_K_dependency_item_ids           UNRESOLVED
public_K_layer_id                      UNRESOLVED
public_K_gate_ids                      UNRESOLVED
public decoder consumer                DEF-DECODER-MATTER / MULTI
public_Dmatter_domain_id               UNRESOLVED
public_Dmatter_inclusion_id            UNRESOLVED
public_single_orbit_to_pair_map_id      UNRESOLVED
public binding gate audit              REQUIRED; result UNRESOLVED
```

No displayed output feeds `U`. `GATE-L1-L5-LOG-PROJECTION` is not reused.

## 7. Exact result and remaining fork

```text
OWNER START FAMILY                   OMEGA_0, PROPOSAL-LOCAL
K0 <-> Krange_0                      HEAD/TRACE/A_0 ISOMORPHISM
Ktail_0                              3125 CLASSES OF SIZE 5
global one-sheet synchronization     MINIMUM n=3
genesis head / trace / A_0 descent   NO
time-n state / A_n descent           YES IFF n>=3
Ktail_0 <-> S_3                      SYNC-HEAD/FUTURE-TRACE ISOMORPHISM
nonempty Omega_(0,Z) tail quotients  CANONICALLY X_1; FIBRES HAVE SIZE |Z|
Rep_3(Omega_0)                       ONE CONDITIONAL ADMISSIBLE CLASS

OWNER REPRESENTATION DECISION        NONE
PUBLIC K                             UNRESOLVED
dom(D_matter)                        UNRESOLVED
physical occurrence/distribution     UNRESOLVED
source/pair distributions            UNRESOLVED
sampling/realized history            UNRESOLVED
implementation closure/decoder write UNRESOLVED
physical completeness                UNRESOLVED
QUADRATIC-DECODER-DATA                O / STOP, unchanged
READY-FOR-CLASSIFICATION              NO
FORMAL RUN                            NONE.
```

The next owner fork is:

```text
A. retain Omega_0 with the headed K0/literal-range equivalence class;
B. change again to S_3 and explicitly adopt loss of five-way genesis identity
   plus the time-3 source-position semantics;
C. choose another represented family;
D. STOP.
```

No branch is selected here beyond the proposal-local `Omega_0` start-family
freeze. No Canon, registry, normative, dependency, gate, evidence, probe,
verifier, run, decoder write, physical completeness, or status change occurs.

This action is stacked on draft #189. It MUST NOT merge until #183, then #188,
then #189 have each merged and been read back from public `main`, in that
order.

## 8. Post-merge scope amendment

```text
AMENDMENT DATE:         2026-07-27
AMENDMENT EFFECT:       SCOPE CLARIFICATION ONLY
PUBLIC MAIN BASE:       412d56fd46f3d6a919d17fdaaa39bb4c9bfc681b
ORIGINAL PR / HEAD:     190 / cd2cb46c5d50a77c3d858ee954f27a62bd798eb6
ORIGINAL MERGE COMMIT:  178d5cf9c108379dddd48ddb53b98077b2c227ce
ORIGINAL FILE BLOB:     1c1ec92d99b70a1fe6b31ca13e4bc7893f36d837
ORIGINAL FILE SHA-256:  ae488099bdf0c1a66bd234be74f8909110d04c7f817789c81de9ef83509412dc
ORIGINAL FILE BYTES:    16884
OWNER SCOPE RECORD:     issue 107, comment 5093205688
AMENDMENT CLAIM:        issue 107, comment 5093431422
FORMAL RUN:             NONE
CANON/TABLE/GATE CHANGE: NONE
QDD STATUS:             O / STOP, unchanged
```

This block is an append-only durability amendment. It does not alter the
owner choice, definitions, identifiers, results, or original provenance
above.

For an arbitrary `S subset X`, where `S` is a local dummy variable unrelated
to the named objects `S_beta` and `S_3`, put

```text
K_(0,S)={kappa_x:x in S},
E_3(S)={E_3(x):x in S} subset X_1.
```

Restricting (4) gives the canonical bijection

```text
K_(0,S)/~tail0 -> E_3(S),    [kappa_x] |-> E_3(x).   (5a)
```

This remains the unique empty bijection when `S` is empty. The quotient is
canonically the whole `X_1` exactly when

```text
E_3(S)=X_1
iff S meets every E_3-fiber
iff S intersect E_3^(-1)(y) is nonempty for every y in X_1.   (5b)
```

For `y in E_3(S)`, the corresponding quotient-projection fiber has size

```text
|S intersect E_3^(-1)(y)|.
```

The complete-sheet unions in Section 3.1 are the special case `S=X_Z`.
Because every `E_3|X_z:X_z->X_1` is bijective, a nonempty `Z` gives
`E_3(X_Z)=X_1` and constant fiber size `|Z|`, recovering (5). Thus the
sentences "nonempty genesis-sheet families are canonically equivalent" and
"local tail-universality theorem" above apply to the explicitly frozen
complete-sheet-union class. For a general subset `S`, the canonical quotient
is only `E_3(S)`.


No new public or proposal-local identifier, start family, decoder field,
dependency, gate, probe, evidence item, or status is introduced.
