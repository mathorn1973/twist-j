# P-KERNEL-Z6-SYNCHRONIZATION-1 predefinition (NON-CANONICAL)

Status: `NON-CANONICAL / RESULT-EXPOSED PREDEFINITION / NO PROBE RUN`

Date: 2026-07-26

Public definition issue:
[issue #156](https://github.com/mathorn1973/twist-j/issues/156).

This note freezes a proposed successor to `CARRY-J-CHECKPOINT [T]`.
It is not Canon, evidence, a preregistration, a verifier, a formal run, or a
status change. It adds no public owner row. It is unregistered and confined
to L1. After this note has been reviewed, merged, and publicly read back, the
only authorized next program action is a separate Canon owner fold.

## 1. Authority and protocol boundary

```text
Canon:              Public Canon v22
state:              ACTIVE
authority:          mathorn1973/twist-j main
tag:                canon-v22
activation commit:  91854391ee8529702a5776f028db86dd7fb0bef2
content commit:     dd455edf7e10050bad6722f9bafc27fe6359e411
Canon SHA-256:      67b1286845434ae6d20edb1d09b7d5c892470be3439c3331b07d8d598a780d21
Canon bytes:        113066
antecedent:         CARRY-J-CHECKPOINT [T]
proposed owner:     KERNEL-Z6-SYNCHRONIZATION [O]
future probe:       P-KERNEL-Z6-SYNCHRONIZATION-1
action layer:       L1 only
inter-layer gate:   none
```

The authorized branch and file for this definition step are

```text
branch: definition/P-KERNEL-Z6-SYNCHRONIZATION-1
file:   notes/canon/P-KERNEL-Z6-SYNCHRONIZATION-1-PREDEFINITION.md
```

This step forbids a `probes/` directory, verifier, evaluator, formal
execution, formal `EXPECTED.txt` or run transcript, result record, Canon edit,
registry edit, frontier edit, gate edit, status edit, or release edit.

## 2. Falsifier first and exposure disclosure

The candidate fails if there is an exact counterexample to any of the
following frozen targets:

1. the per-sheet all-`n` bijections in Targets T1 and T2;
2. either fixed-time fiber count implied by Targets T1 and T2;
3. checkpoint-trace non-eventual-periodicity in Target T3;
4. the finite-autonomous-realization no-go in Target T4.

A defect in a frozen Public Canon v22 generator, trace law, selector,
involution, or update premise stops this successor and routes an upstream
authority audit. An incomplete carrier, index convention, proof,
completeness method, dependency, or scope boundary is `STOP`, not a positive
result.

A local analytical proof and the candidate conclusion existed before issue
#156. The proof is disclosed below. A future public probe is therefore a
pinned confirmation and adversarial audit, not blind discovery. Its
threshold, carrier, scope, and equivalence may not be selected from the
exposed conclusion.

## 3. Frozen architecture and indexing

All arithmetic in this section is in `F_5`. Put

```text
X     = F_5^6,
z_6(psi) = p1 + p4 + p1p + p4p + q + r,
X_z   = {psi in X : z_6(psi)=z},
X_14  = X_1 union X_4.
```

Every sheet has

```text
|X_z| = 5^5 = 3125,
|X_14| = 6250.
```

The symbol `X_14` is deliberately neutral. This note assigns it no census or
additional dynamical property. The registered finite-window statement
`CENSUS-Z5-SHEET [C]` is not a premise of the candidate theorem.

For

```text
psi = (p1,p4,p1p,p4p,q,r),
```

expand the five registered Public Canon v22 generators exactly:

```text
a(psi) =
    (p4,p1,p4p,p1p,q,r),

b(psi) =
    (-p1p,-p4p,-p1,-p4,-q,-r),

c(psi) =
    (-p1p+2,-p4p+1+r,-p1+2,-p4+1-r,1-q,-r),

d(psi) =
    (2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),

e(psi) =
    (2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).
```

They are indexed by

```text
(g_0,g_1,g_2,g_3,g_4) = (a,b,c,d,e).
```

Let

```text
theta_n = s_2(n) mod 2,
i_n     = z_6(psi_n) + 2 theta_n mod 5,
U(n,psi_n) = (n+1,g_(i_n)(psi_n)).
```

For a frozen bit `t in {0,1}`, define the checkpoint branch

```text
F_t(psi) = g_((z_6(psi)+2t) mod 5)(psi).
```

For every genesis checkpoint define

```text
E_n(psi_0) = pr_checkpoint(U^n(0,psi_0)).
```

Thus `E_0` is the identity, and the update from `E_n` to `E_(n+1)` uses
`theta_n`. For `n >= 1`, define

```text
q_n = 4 + 2 theta_(n-1) mod 5.
```

Here `q_n` is a sheet-label abbreviation. It is not the time-`n` value of the
checkpoint coordinate `q`. The index is part of the freeze. The sheet
`X_(q_n)` encodes `theta_(n-1)`, which produced checkpoint `E_n`. The next
update uses `theta_n`. At the first synchronized checkpoint,

```text
q_3 = 4 + 2 theta_2 = 1,
4 + 2 theta_3 = 4.
```

Confusing these two values is a frozen failure.

## 4. Exact sheet automaton

The coordinate formulas give the five trace laws

```text
z_6(a psi) =  z_6(psi),
z_6(b psi) = -z_6(psi),
z_6(c psi) = 2-z_6(psi),
z_6(d psi) = 2-z_6(psi),
z_6(e psi) = 3-z_6(psi).
```

Every `g_i` is an involution and hence a bijection. Combining the selector
`i=z+2t mod 5` with the trace laws gives the complete two-by-five sheet
transition table:

```text
             input sheet z
             0  1  2  3  4

t = 0        0  4  0  4  4
t = 1        2  1  1  3  1
```

Each individual displayed arrow `X_z -> X_z'` is a bijection. Indeed, on a
fixed input sheet the selector is fixed, so the branch is the restriction of
one bijection `g_i`; its image lies in the displayed sheet, and both sheets
have cardinality 3125. Multiple input sheets may nevertheless have the same
output sheet.

## 5. Frozen candidate theorem

### T1. Per-sheet synchronization

For every `n >= 3` and every `z in F_5`, the proposed exact statement is

```text
E_n restricted to X_z : X_z -> X_(q_n) is a bijection.       (T1)
```

Consequently, at each fixed known `n >= 3`,

```text
E_n(X) = X_(q_n),
E_n : X -> X_(q_n) is exactly 5-to-1,
```

and every endpoint has exactly one genesis preimage in each initial sheet
`X_z`.

### T2. Neutral two-sheet restriction

For every fixed known `n >= 1`, the proposed exact statements are

```text
E_n restricted to X_1 : X_1 -> X_(q_n) is a bijection,
E_n restricted to X_4 : X_4 -> X_(q_n) is a bijection.       (T2)
```

Consequently,

```text
E_n restricted to X_14 : X_14 -> X_(q_n) is exactly 2-to-1.
```

The ratios in T1 and T2 are fibers of `E_n` with `n` fixed. They make no
claim about the unindexed checkpoint projection on the full forward carrier.

### T3. Checkpoint non-eventual-periodicity

For every `psi_0 in X`, propose

```text
(z_6(E_n(psi_0)))_(n>=0) is not eventually periodic,
(E_n(psi_0))_(n>=0) is not eventually periodic.              (T3)
```

### T4. No finite autonomous time-homogeneous realization

For every `psi_0 in X`, propose that there are no

```text
finite set S,
map H : S -> S,
map pi : S -> X,
state s_0 in S
```

such that

```text
pi(H^n(s_0)) = E_n(psi_0) for every n >= 0.                  (T4)
```

The special case `S=X` and `pi=id` excludes a checkpoint-only update
`f:X->X`. T4 proves only that an autonomous time-homogeneous realization of
a complete v22 checkpoint trajectory needs an infinite state carrier. It
does not select a unique counter, a unique extension, or a unique
factorization into drive and checkpoint. Externally driven and
time-inhomogeneous realizations are outside T4.

## 6. Result-exposed candidate proof

This section exposes the proof that a later preregistration must freeze and
an independent audit must try to break. It earns no public status here.

### 6.1 Three-step base

The initial Thue-Morse prefix is

```text
(theta_0,theta_1,theta_2) = (0,1,1).
```

Applying the complete sheet table to all five initial sheets gives

```text
n = 0:  {0,1,2,3,4}
n = 1:  {0,4}
n = 2:  {1,2}
n = 3:  {1}.
```

More strongly, on each fixed initial sheet `X_z`, the three selectors are
fixed by that sheet's trace path. Their composite is a bijection

```text
E_3 restricted to X_z : X_z -> X_1.
```

Since

```text
q_3 = 4 + 2 theta_2 = 1 mod 5,
```

T1 holds at `n=3`. The common-sheet equality `z_6(E_3)=1` is already a proof
lemma in `CARRY-J-CHECKPOINT [T]`; the present proof rederives it from the
same public trace table.

### 6.2 Four-case induction

Assume at some `n >= 3` that every restricted map in T1 is a bijection onto
`X_(q_n)`. Put

```text
t = theta_(n-1),
u = theta_n.
```

The four adjacent-bit cases are

```text
t  u    q_n    selector i_n    q_(n+1)
0  0     4          4              4
0  1     4          1              1
1  0     1          1              4
1  1     1          3              1
```

Thus in every case

```text
F_u(X_(q_n)) = X_(q_(n+1)).
```

The relevant restriction of `g_(i_n)` is a bijection between these sheets.
Composing it with each induction-hypothesis bijection proves T1 at `n+1`.
This is the all-`n` step. A finite time sweep is not its substitute.

### 6.3 The two-sheet count

At `n=1`, `theta_0=0`, and the sheet table gives separate bijections

```text
E_1 restricted to X_1 : X_1 -> X_4,
E_1 restricted to X_4 : X_4 -> X_4.
```

The same four-case step preserves a bijection from each of the two initial
sheets to `X_(q_n)` for every `n>=1`. Their disjoint union is therefore
exactly two-to-one, proving T2.

### 6.4 Fixed-time fiber counts

For fixed `n>=3`, T1 partitions the domain into five disjoint sheets, each
mapped bijectively onto the same target sheet. Every target has exactly five
preimages, one per initial sheet. The identical argument with the two
disjoint sheets in `X_14` gives T2.

This counting argument has `n` fixed throughout. Dropping `n` changes the
map and is forbidden.

### 6.5 Self-contained Thue-Morse aperiodicity lemma

Assume for contradiction that `theta_n` is eventually periodic with period
`p>=1` after index `N`. Choose arbitrarily large `k` with

```text
2^k-p >= N.
```

The two indices `2^k-p` and `2^k` differ by `p`, so eventual periodicity
would give

```text
theta_(2^k-p) = theta_(2^k) = 1.
```

For `0<p<2^k`, the low `k` binary digits of `2^k-p` are the complement of
the low `k` digits of `p-1`. Hence

```text
s_2(2^k-p) = k-s_2(p-1),
theta_(2^k-p) = k-s_2(p-1) mod 2.
```

The last value alternates when `k` increases by one, so it cannot equal one
for every sufficiently large `k`. This contradiction proves that
`theta_n` is not eventually periodic.

The map

```text
t -> 4+2t mod 5
```

is injective on `{0,1}`. T1 therefore makes the trace sequence from time
three onward an injective recoding of the lag-one Thue-Morse sequence. The
trace sequence is not eventually periodic. If the checkpoint sequence were
eventually periodic, its image under `z_6` would be eventually periodic.
This proves T3.

### 6.6 Finite autonomous no-go

Every orbit of a self-map of a finite set is eventually periodic. Every
projection of such an orbit is also eventually periodic. If the objects in
T4 existed, then

```text
(pi(H^n(s_0)))_(n>=0)
```

would be eventually periodic, contrary to T3. This proves T4 within the
candidate proof.

## 7. Exact novelty and inherited boundary

The registered theorem `CARRY-J-CHECKPOINT [T]` already proves on the full
forward carrier that

```text
z_6(E_3(psi_0)) = 1,
E_4(psi_0) = E_6(psi_0),
Theta_4 = 2 != 4 = Theta_6
```

for every seed, and therefore no single-valued
`h:F_5^6->F_5^*` factors the inherited phase through the checkpoint on that
carrier.

The proposed successor does not reopen that theorem. Its candidate new scope
is exactly:

1. the all-`n` per-sheet bijection T1;
2. the fixed-time `5:1` and `2:1` fiber counts;
3. checkpoint non-eventual-periodicity T3;
4. the finite-autonomous-realization no-go T4.

The candidate does not use `CENSUS-313 [C]` or `CENSUS-Z5-SHEET [C]` as a
premise. It does not use the phase values `Theta_4,Theta_6` in its proof.

## 8. Proposed owner disposition

Only a later reviewed Public Canon fold may create the owner. The proposed
`REGISTRY.tsv` fields are

```text
claim_id:       KERNEL-Z6-SYNCHRONIZATION
status:         O
canon section:  3. The kernel and the census
evidence:       inline
scope:          whether T1 through T4 hold under the declared L1 update,
                including only the fixed-time fiber statements and the
                exclusions frozen in this note
falsifier:      closes positively only by a self-contained all-n proof of
                T1 through T4 plus a complete exact finite audit and the
                required cross-architecture byte gate; closes negatively
                on one exact counterexample to T1 through T4; STOP on a
                broken premise, incomplete proof or audit, invalid pin,
                authority mismatch, or transcript defect
```

The proposed `NORMATIVE.tsv` row is

```text
KERNEL-Z6-SYNCHRONIZATION  OBLIGATION  KERNEL-Z6-SYNCHRONIZATION  O  L1    canon/CANON.md::3. The kernel and the census
```

The proposed `FRONTIER_PROGRAMS.tsv` row is

```text
KERNEL-Z6-SYNCHRONIZATION  DECODER_CORE  ROOT  READY  FORMAL
```

The sole minimal logical dependency is

```text
KERNEL-Z6-SYNCHRONIZATION -> DEF-AUTONOMOUS-STATE
    E_n is the checkpoint projection of the declared U orbit, including
    its selector, odometer coordinate, and kernel generators.
```

`CARRY-J-CHECKPOINT [T]` remains the registered antecedent and novelty
boundary. It is not a proposed `REQUIRES` edge because the proof above
rederives the synchronization base and does not use that theorem's ramified
phase statement. Importing the theorem as a logical dependency would also
import unused transitive phase scope.

No `canon/GATES.tsv` row is proposed. T1 through T4 stay inside L1. Adding an
inter-layer gate would be a type error.

The owner-fold disposition is

```text
READY-OWNER-FOLD
    every definition, dependency, falsifier, scope boundary, and
    completeness condition in this note is exact;

STOP
    any one of those inputs remains unresolved or contradictory.
```

Neither route is a scientific result.

## 9. Future preregistration and completeness contract

This note contains no verifier. After the owner row is active and a distinct
formal-lock issue exists, one immutable preregistration must freeze the
following six fields before the first execution.

### EQUATION

Freeze T1 through T4, the full coordinate formulas, the two-by-five table,
the three-step base, all four induction cases, the fixed-time qualification,
the aperiodicity lemma, and the finite-`S` proof exactly.

### CODE

Freeze one accepted `verify.py` by SHA-256 and byte count. It must use only
the Python standard library and exact integers modulo five. It must be
deterministic and use no floats, randomness, file input, network access, or
subprocess. It may encode only the frozen mathematical targets. It must
compute the observed objects independently and must not hard-code the final
scientific decision.

### CARRIER

The exhaustive finite audit must cover:

```text
all 15625 states of X,
all five generators on all states,
all ten bit-by-sheet transitions,
all five initial sheets,
all 6250 states of X_14,
direct fixed-time controls for n=0,...,6,
all four abstract adjacent-bit induction cases.
```

There is no external dataset. The sweep through `n=6` is a finite regression
containing the base and several post-base steps. It does not prove the
all-`n` target.

### SYSTEMATICS

The all-`n` range is carried by the symbolic proof. The finite verifier
audits the complete finite generator carrier, the sheet automaton, the
proof cases, and finite controls. The result is conditional on the pinned
public architecture. An implementation defect, authority mismatch,
incomplete proof, or transcript mismatch routes `STOP`.

### THRESHOLD

The scientific candidate is `FALSIFIED` only by one exact counterexample to
T1, T2, T3, or T4 in a valid completed transcript. A proof defect or gap
without an exact counterexample routes `STOP`, as does a broken premise,
invalid pin, changed authority, incomplete definition, exception,
nondeterminism, malformed transcript, nonzero stderr, nonzero exit, or
cross-architecture byte mismatch. After the pin, the equation, code,
carrier, and threshold do not move.

A valid completed scientific route, including `FALSIFIED`, must exit zero,
write empty stderr, and produce

```text
run integrity:        PASS
scientific decision:  PROOF-SURVIVES | FALSIFIED
```

An exception, malformed transcript, pin mismatch, nondeterminism, nonzero
exit, or nonempty stderr instead produces

```text
run integrity:        FAIL
scientific decision:  STOP
```

### LAYER

`L1` only. No decoder, physical-history, metrology, or L2-L6 action is part
of the probe.

The accepted verifier must keep run integrity separate from science:

```text
run integrity:        PASS | FAIL
scientific decision:  PROOF-SURVIVES | FALSIFIED | STOP
```

`PROOF-SURVIVES` does not itself register `[T]`.

At minimum, the verifier must provide two logically distinct exact audit
paths:

1. direct state evolution over all 15625 checkpoints;
2. independent sheet-automaton and cardinality reconstruction.

The formal aarch64 leg and the GitHub x86_64 leg must execute the
byte-identical public pin and emit byte-identical stdout. Independent
adversarial review must try to produce a counterexample rather than merely
repeat the same code path.

## 10. Scope firewall

This predefinition does not:

- make `F_5^6` the full autonomous state;
- import a census classification into `X_14`;
- replace `theta_(n-1)` in `q_n` by `theta_n`;
- make a `5:1` or `2:1` claim when time is unknown;
- claim a finite fiber for the unindexed checkpoint projection;
- make an event log an independent state variable;
- claim every decoded log is aperiodic;
- prove a decoder total, unique, canonical, or complete;
- derive physical irreversibility or an arrow of time;
- select one genesis history;
- select a unique counter, drive, or autonomous extension;
- identify dynamics with gauge or unit convention;
- change a reading quotient or metrology obligation;
- lift any statement to L2-L6;
- change any existing Canon status.

## 11. Required public sequence

```text
1. merge and publicly byte-read back this definition note;
2. review and activate a separate Canon owner fold;
3. open a distinct formal-lock issue;
4. create the reserved probe branch and path from current public main;
5. pin PREREG.md and verify.py together before execution;
6. publish and read back their exact bytes and hashes;
7. run the first formal leg on native Linux/aarch64;
8. require byte-identical Linux/x86_64 reproduction;
9. preserve a fired falsifier first-class;
10. route any status change through a separate reviewed Canon fold.
```

No step may be merged with its successor to erase a review boundary.

## References

- [Public definition issue #156](https://github.com/mathorn1973/twist-j/issues/156)
- [Public Canon v22 autonomous state](https://github.com/mathorn1973/twist-j/blob/91854391ee8529702a5776f028db86dd7fb0bef2/canon/CANON.md#L196-L224)
- [Public Canon v22 kernel definitions](https://github.com/mathorn1973/twist-j/blob/91854391ee8529702a5776f028db86dd7fb0bef2/canon/CANON.md#L530-L570)
- [CARRY-J-CHECKPOINT registry row](https://github.com/mathorn1973/twist-j/blob/91854391ee8529702a5776f028db86dd7fb0bef2/canon/REGISTRY.tsv#L189)
- [CARRY-J-CHECKPOINT proof boundary](https://github.com/mathorn1973/twist-j/blob/91854391ee8529702a5776f028db86dd7fb0bef2/canon/CANON.md#L666-L681)
- [CARRY-J-CHECKPOINT preregistration](https://github.com/mathorn1973/twist-j/blob/91854391ee8529702a5776f028db86dd7fb0bef2/probes/P-CARRY-J-CHECKPOINT-1/PREREG.md)
