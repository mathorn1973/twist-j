# P-DMATTER-TOTAL-1 Public-K Representation Predefinition (NON-CANONICAL)

```text
STATUS:                 EXACT DEFINITION-ONLY RESULT / OWNER DECISION NOT TAKEN
AUTHORITY:              NOT CANON
SCOPE:                  PROPOSAL-LOCAL / L1 / FORWARD-ORBIT REPRESENTATION
PUBLIC CANON:           Public Canon v24
PUBLIC CANON TAG:       canon-v24
PUBLIC MAIN BASE:       f6f797739be21acfa70851be544c994ea17b7f5a
STACKED PREDECESSOR:    486c4d28f21824772ca43c67050ab502be9bef85
PREDECESSOR PR:         188, itself stacked on 183
IMMEDIATE PREDECESSOR:  P-DMATTER-TOTAL-1-CONDITIONAL-ADJACENT-DICTIONARY-OWNER-FREEZE.md
PREDECESSOR BLOB:       6c9504f0f169cc4a12368c3d73d0e1644f585cb5
PREDECESSOR SHA-256:    720c4747fdb6013eddf420a20f30c54a9c8e4d067536112840668a45b86ba0c3
PREDECESSOR BYTES:      25976
CLAIM ISSUE:            107
CLAIM COMMENT:          5091978424
OWNER DECISION:         NONE IN THIS NOTE
FORMAL RUN:             NONE
CANON/TABLE/GATE CHANGE: NONE
QDD STATUS:             O / STOP, unchanged
READY-FOR-CLASSIFICATION: NO
```

Canon v24 publishes the symbol `K` and the phrase "the set of forward
U-orbits", but no completion-grade carrier, equality, head, position, or
representation IDs. This note compares candidate formalizations; it does not
claim that the public sentence intended any one of them.

## 0. Firewall

```text
PUBLIC-K-OR-INTENT-ADOPTION
    a candidate is called public K or the intended meaning of public K;
PUBLIC-DMATTER-DOMAIN-ADOPTION
    a candidate or subset is identified with dom(D_matter);
STARTING-FAMILY-TRANSFER
    a full-Omega head or tail result is applied to another named start family
    without recomputing its quotient fibers;
RANGE-TAIL-COLLAPSE
    a literal orbit range is identified with a tail-equivalence class;
TAIL-SECTION-AS-DESCENT
    a chosen representative is called a descended head;
DOWNSTREAM-OVERCLAIM
    failure of the complete PairInput map is extended to every projection;
STATUS-PROMOTION
    a public ID, dependency, layer, gate, completion field, or QDD status moves.
```

The rejected `C-ARCH-UNIVERSALITY-1` package is not an input, precedent,
evidence source, or comparison class. No `ARCH-*` row, formal architecture
probe, architecture-level conclusion, or v25 fold is imported. The tail
quotient below is only a representation quotient of forward `U`-orbits.

## 1. Full-Omega headed representations

Let

```text
c(n,x)=n,
c(U^m(omega))=c(omega)+m.                         (1)
```

For `omega in Omega`, define

```text
s_omega(m)=U^m(omega),
K_seq={s_omega : omega in Omega},

R_omega={U^m(omega) : m>=0},
K_rng={R_omega : omega in Omega}.
```

`K_seq` is the predecessor's `Khead_beta`. Its equality and head are

```text
s_omega Eq_seq s_omega' iff omega=omega',
Head_seq(s_omega)=omega.
```

`Eq_rng` is extensional subset equality. By (1), the counters in `R_omega`
are

```text
{c(omega),c(omega)+1,c(omega)+2,...},
```

with exactly one element at each counter. Hence

```text
Head_rng(R)=the unique minimum-counter element of R,
RangeOf(omega)=R_omega
```

are total, equality-compatible, and inverse:

```text
Head_rng o RangeOf=id_Omega,
RangeOf o Head_rng=id_K_rng.                         (2)
```

Define

```text
Phi(s)=Image(s) : K_seq -> K_rng,
Psi(R)=s_(Head_rng(R)) : K_rng -> K_seq.
```

Then

```text
Psi o Phi=id_K_seq,
Phi o Psi=id_K_rng,
Head_rng o Phi=Head_seq,

R_omega Eq_rng R_omega'
iff omega=omega'
iff s_omega Eq_seq s_omega'.                         (3)
```

Set `Trace_seq(s,m)=s(m)` and `Trace_rng(R,m)=U^m(Head_rng(R))`.
Then `Trace_rng(Phi(s),m)=Trace_seq(s,m)` for every `m`. Pointed sequences
and literal ranges are therefore isomorphic representations preserving both
head and trace. This uses strict counter advance, not checkpoint injectivity.

Retain the predecessor's conditional map

```text
A_seq=OrbitAdjacentInput_beta : K_seq -> PairInput_beta
```

and transport it by

```text
A_rng=A_seq o Psi : K_rng -> PairInput_beta,
A_rng o Phi=A_seq.                                   (4)
```

Equation (4) removes one encoding-only ambiguity. It is not physical
occurrence, decoder universality, or architecture universality.

For a named head family `S subset Omega`, the candidate schema is

```text
HeadedOrbitRep(U;S)=(S,K_rep,Eq_rep,OrbitOf_rep,Head_rep,Trace_rep),
Eq_rep is an equivalence relation; all maps are equality-compatible.
OrbitOf_rep:S->K_rep, Head_rep:K_rep->S, Trace_rep:K_rep x N_0->Omega,
Head_rep(OrbitOf_rep(omega))=omega,
OrbitOf_rep(Head_rep(k)) Eq_rep k,
Trace_rep(OrbitOf_rep(omega),m)=U^m(omega),
k Eq_rep k' => Head_rep(k)=Head_rep(k') and Trace_rep(k,m)=Trace_rep(k',m) for every m.
```

The proved comparison (2)-(4) has `S=Omega`. The genesis family is

```text
Omega_0={0} x X,
```

whose pointed-sequence image is `K0`. No result is transferred to
`Omega_0` or another family by this note.

## 2. Full-Omega tail tests

Define

```text
Shift(s)(m)=s(m+1),

s ~tail s'
iff exists p,q>=0: Shift^p(s)=Shift^q(s'),

K_tail=K_seq/~tail,
[s] Eq_tail [s'] iff s ~tail s',
pi_tail(s)=[s].
```

`pi_tail` is total and equality-compatible. The relation is reflexive and
symmetric. If

```text
Shift^p(s)=Shift^q(s'),
Shift^r(s')=Shift^t(s''),
M=max(q,r),
```

then

```text
Shift^(p+M-q)(s)=Shift^M(s')=Shift^(t+M-r)(s''),
```

so it is transitive.

A head does not descend. For every `omega`,

```text
s_omega ~tail s_(U(omega)),
Head_seq(s_omega)=omega != U(omega)=Head_seq(s_(U(omega)))
```

because the counters differ by one. Hence no `Head_tail` satisfies

```text
Head_seq=Head_tail o pi_tail.                         (5)
```

A representative selector would be new position structure, not descent.

The complete adjacent map also fails to descend. Use the disclosed carry
witness

```text
x=psi_4=psi_6=(0,0,0,1,0,3),
omega_4=(4,x),
omega_6=(6,x)=U^2(omega_4),
Shift^2(s_(omega_4))=s_(omega_6),

theta_4^B=1,  F_1(x)=(0,4,0,0,0,2),
theta_6^B=0,  F_0(x)=(2,1,3,3,2,3).
```

Their tail classes and preparation payloads agree, but

```text
A_seq(s_(omega_4))=q(kappa_x,kappa_(F_1(x))),
A_seq(s_(omega_6))=q(kappa_x,kappa_(F_0(x)))
```

are unequal by branch separation, `Eq_K0`, and injectivity of the tagged role
constructors. Therefore no `A_tail` satisfies

```text
A_seq=A_tail o pi_tail.                               (6)
```

Equation (6) concerns the complete conditional `PairInput_beta` value. A
coarser invariant may descend; the equal high effect and Born value at this
witness are the explicit warning.

## 3. Dependencies and public boundary

| object or result | exact dependencies | proposal layer/gate |
|---|---|---|
| `K_seq`, `K_rng`, `RangeOf`, `Shift`, `K_tail` | `DEF-AUTONOMOUS-STATE / U` | L1 / none |
| `HeadedOrbitRep / Trace_rep` | `U`, named `S subset Omega`, `N_0` | L1 / none |
| `Trace_seq` | `K_seq`, sequence evaluation | L1 -> L1 / none |
| `Trace_rng` | `K_rng`, `U`, `Head_rng` | L1 -> L1 / none |
| `Phi` trace preservation | `Trace_seq`, `Trace_rng`, `Phi`, `Head_rng o Phi=Head_seq` | L1 -> L1 / none |
| `Head_rng`, `Phi`, `Psi` | `U` plus counter `c` / `DEF-ODOMETER-ORBIT` | L1 -> L1 / none |
| `A_rng` and (4) | PR #188 adopted maps plus `Phi/Psi` | L1 -> L1 / none |
| head nondescent (5) | full-`Omega` `K_tail`, `pi_tail`, `Head_seq`, counter law | L1 / none |
| adjacent nondescent (6) | PR #183 carry witness, PR #188 dictionary, `F_0/F_1` separation, `Eq_K0`, and injectivity of `EVAL_SOURCE` / `MakePairInput_beta` | L1 / none |

`K_seq` and `K_rng` are each exactly isomorphic to the L1 head family
`Omega`. This does not reuse `GATE-L1-L5-LOG-PROJECTION`: these proposal-local
orbit-source representations are neither `Log` nor `ObservableHistory`.
`NONE / NO NEW GATE` applies only to the displayed L1 comparison maps.

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
public binding gate audit              REQUIRED; result UNRESOLVED
public_Dmatter_domain_id               UNRESOLVED
public_Dmatter_inclusion_id            UNRESOLVED
public_single_orbit_to_pair_map_id      UNRESOLVED
```

No displayed output feeds `U`.

## 4. Candidate IDs and owner fork

Inherited `K_seq`, `OrbitOf_beta`, `Head_beta`, and `A_seq` retain their PR
#188 IDs. New proposal-local IDs are:

```text
K_rng carrier/equality       CAND-QDD-CARRIER-KRANGE-BETA /
                             CAND-QDD-EQ-KRANGE-BETA-EXTENSIONAL
RangeOf / Head_rng           CAND-QDD-MAP-RANGE-OF-BETA /
                             CAND-QDD-MAP-HEAD-KRANGE-BETA
Phi / Psi                    CAND-QDD-MAP-KSEQ-TO-KRANGE-BETA /
                             CAND-QDD-MAP-KRANGE-TO-KSEQ-BETA
Trace_seq / Trace_rng        CAND-QDD-MAP-TRACE-KSEQ-BETA /
                             CAND-QDD-MAP-TRACE-KRANGE-BETA
representation certificate  CAND-QDD-CERT-KSEQ-KRANGE-HEAD-TRACE-ISO
A_rng                        CAND-QDD-MAP-KRANGE-ADJACENT-INPUT-BETA
K_tail carrier/equality      CAND-QDD-CARRIER-KTAIL-BETA /
                             CAND-QDD-EQ-KTAIL-BETA-COMMON-TAIL
pi_tail                      CAND-QDD-MAP-KSEQ-TO-KTAIL-BETA
tail certificates            CAND-QDD-CERT-KTAIL-NO-HEAD-DESCENT /
                             CAND-QDD-CERT-KTAIL-ADJACENT-NONDESCENT
headed/trace schema          CAND-QDD-SCHEMA-HEADED-ORBIT-REPRESENTATION
```

A later owner action must choose in this order:

```text
A. KEEP FULL-OMEGA FAMILY
   choose HEADED INTERFACE, concrete K_seq, concrete K_rng, full-Omega
   K_tail plus separately typed position data, OTHER, or STOP.
   A concrete encoding retains Phi/Psi as certified representation
   equivalence; no physical distinction follows.
B. CHANGE STARTING FAMILY
   freeze S subset Omega first. No full-Omega tail result or representation
   choice transfers automatically.
C. STOP.
```

No branch is selected here. Only a later normative Canon action can define
public `K`; `dom(D_matter)` and occurrence remain separate actions.

## 5. Exact result and remaining boundary

```text
K_seq <-> K_rng                    HEAD/TRACE-PRESERVING ISOMORPHISM
A_seq <-> A_rng                    EXACT TRANSPORT
full-Omega K_tail head             DOES NOT DESCEND
full conditional A_seq on K_tail   DOES NOT DESCEND
arbitrary downstream projection    NOT DECIDED

OWNER DECISION                     NONE
PUBLIC K / START FAMILY            UNRESOLVED
public carrier/equality/head/trace/position  UNRESOLVED
dom(D_matter)                      UNRESOLVED
physical occurrence/distribution   UNRESOLVED
public dependencies/layer/gates     UNRESOLVED
QUADRATIC-DECODER-DATA              O / STOP, unchanged
READY-FOR-CLASSIFICATION            NO
FORMAL RUN                          NONE.
```

No public `K` choice or intent, decoder write, Q-factor closure, totality,
uniqueness, physical history, sampling, measure, probe, verifier, run, or
scientific status is produced.

This action is stacked on unmerged draft #188, itself stacked on #183. It
MUST NOT merge until #183 and then #188 have each merged and been read back
from public `main`, in that order.

No formal probe or Canon fold is authorized by this note.
