# P-QDD-RECORD-COMPLETE-STABILIZER-1 preregistration

Date: 2026-08-20

Author of record: A. M. Thorn

Status: preregistered protocol only. No scientific result is earned here. The
accepted verifier has formal execution count zero and may not be imported or
executed before this file and `verify.py` are committed together, pushed, and
read back byte for byte from the public remote.

Public claim lock: issue 474.

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v57
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v57
CONTENT_COMMIT: 8e8b04abe4d3359942449533854ef1d142be70df
CANON_SHA256:   c96a2ef52c78d68ef8f04b582e4a17328e6a863b49664f29b1bd324171d802a8
CANON_BYTES:    295013
BASE_COMMIT:    1ca497af6e3b9f9ec389e9fd1cc241003aca1688
```

Target: blocker O2 of `QDD-INSTRUMENT-APPARATUS [O]` only, at L4.

## Result exposure and lineage

This is result-exposed, proof-first work. Before issue 474, non-canonical
reasoning identified the expected full-partition-stabilizer route. Those
calculations are discovery context only.

The sealed probes `P-QDD-J-CENTRALIZER-TERMINALITY-1` and
`P-QDD-FRESH-RECORD-NOFEEDBACK-2` are boundary lineage. No predecessor helper,
verifier, transcript, or result is imported or executed. This probe reconstructs
the J simplex and both stabilizers independently.

Static parsing and syntax compilation are allowed before the pin. Scientific
execution is forbidden.

## Field 1: equation

### 1. The public J simplex

Work over

```text
V = Q^4,
one = (1,1,1,1)^T,
G = I_4 - (1/5) one one^T,
D = M_J - I_4,
M_J = [[1,0,-1,1],
       [0,1,-1,0],
       [1,0,0,0],
       [0,1,-1,1]].
```

Put

```text
u_x = D^x e_0, x in F_5.
```

Then

```text
D^5 = I,
D^T G D = G,
sum_x u_x = 0,
<u_x,u_y>_G = 4/5 if x=y and -1/5 otherwise,
u_2 = -one.
```

The first four vertices form a rational basis of V and the fifth is their
negative sum.

### 2. Complete regular-simplex symmetry

For every permutation `pi in S_5`, there is one unique rational map

```text
rho(pi) u_x = u_(pi(x)).
```

It exists because the only linear relation among the five vertices is their
sum zero, and every permutation preserves that relation. It is G-orthogonal
because it preserves the complete Gram table. The representation is faithful
because the vertices are distinct and span V.

Conversely, every linear automorphism preserving the five-vertex set induces a
permutation of that set. Therefore the complete linear automorphism group of
the marked regular simplex is exactly `S_5`.

### 3. The binary record partition and its stabilizer

Fix a terminal record token `k in F_5`. The binary record retains only

```text
LOW  = {k},
HIGH = F_5 minus {k}.
```

The complete subgroup preserving this record partition pointwise on the LOW
cell is

```text
S_k = {pi in S_5 : pi(k)=k} ~= S_4.
```

Define, before any target comparison,

```text
P_k = (1/24) sum_(pi in S_k) rho(pi),
Q_k = I - P_k.
```

The group average is the G-orthogonal projector onto the fixed space. Since
`S_k` fixes `u_k` and is transitive on the other four vertices, its fixed space
inside V is exactly `Q u_k`. Hence

```text
P_k^2=P_k=P_k^sharp, rank(P_k)=1, im(P_k)=Q u_k,
Q_k^2=Q_k=Q_k^sharp, rank(Q_k)=3.
```

The moving space `Q_k V` is the standard three-dimensional rational
representation of `S_4`.

### 4. Record-partition completeness

Freeze one added physical premise:

```text
record-partition completeness:
  after the terminal record stores only {k}|other, the apparatus moving-branch
  law may use the record partition and regular-simplex geometry, but no
  residual ordering or affine phase label among the four unrecorded vertices.
```

Algebraically, an admitted moving branch T obeys

```text
T P_k = P_k T = 0,
T rho(pi) = rho(pi) T for every pi in S_k,
T^sharp T = Q_k.
```

This premise is not record persistence, no-feedback, reversibility, or ordinary
repeatability. It is not claimed to follow from the current public architecture.

### 5. Complete S4 centralizer theorem

Identify the four HIGH vertices with the permutation module `Q^4`. Its
decomposition is

```text
Q^4 = Q(1,1,1,1) direct-sum W,
W = {(x_1,x_2,x_3,x_4): sum x_i=0}.
```

The moving space `Q_k V` is isomorphic to W.

Let A commute with every permutation matrix of `S_4`. Commutation with all
transpositions forces every diagonal entry of A to be one common value `a` and
every off-diagonal entry to be one common value `b`. Thus

```text
A = (a-b) I + b 11^T.
```

On W the second term vanishes, so A is scalar. Therefore

```text
End_(S_4)(Q_k V) = Q Q_k.
```

Every admitted moving branch is

```text
T = lambda Q_k.
```

The effect equation gives

```text
T^sharp T = lambda^2 Q_k = Q_k,
lambda^2=1,
lambda in {+1,-1}.
```

Under the registered post-state equivalence `T ~ -T`, the two algebraic
members are one physical class. Strict representative idempotence `T^2=T`
selects `T=+Q_k`.

### 6. Reversible pointer realization

With a fresh binary pointer, ready state `p_0`, and flip X, define

```text
U_T = P_k tensor I_2 + T tensor X.
```

For `T=+Q_k` or `T=-Q_k`,

```text
U_T^sharp U_T = I,
K_LOW=P_k,
K_HIGH=T,
K_LOW^sharp K_LOW=P_k,
K_HIGH^sharp K_HIGH=Q_k,
K_LOW^sharp K_HIGH=0.
```

The two signs are the same physical post-state class.

### 7. Exact affine residual-label boundary

The smaller public-label stabilizer is

```text
H_k = {x -> k + a(x-k): a in F_5^x} ~= C_4.
```

Let `g_k` be multiplier two and define

```text
R_k = (1/4)(I-g_k+g_k^2-g_k^3),
C_k = Q_k-R_k,
J_k = g_k C_k.
```

Then

```text
End_(H_k)(Q_k V) = Q R_k direct-sum Q C_k direct-sum Q J_k,
dim = 3,
J_k^2=-C_k.
```

The exact witness

```text
T_* = R_k-C_k
```

satisfies

```text
T_*^sharp T_*=Q_k,
T_*^2=Q_k,
T_* != +Q_k,
T_* != -Q_k.
```

It commutes with all of `H_k` but fails to commute with at least one element of
the complete record-partition stabilizer `S_k`.

Thus the selection distinction is exact:

```text
residual affine phase labels retained -> three-dimensional centralizer and
                                         nonselection;
all unrecorded labels erased by S_4   -> scalar centralizer and one Lueder
                                         physical class.
```

### 8. Target comparison, deliberately last

Only after the class, completeness theorem, selection, pointer realization, and
boundary are established, compare token `k=2` with

```text
E_low  = (1/4) one one^T,
E_high = I-E_low.
```

The identity `u_2=-one` gives

```text
P_2=E_low,
Q_2=E_high.
```

Therefore the unique record-complete physical class is represented by

```text
K_low=E_low,
K_high=E_high,
```

the Lueder pair.

## Field 2: code

Accepted exact file:

```text
probes/P-QDD-RECORD-COMPLETE-STABILIZER-1/verify.py
```

Requirements:

```text
Python standard library only
integers and Fraction only
no float, Decimal, complex approximation, random, network, subprocess,
external data, predecessor import, scratch import, or filesystem write
zero arguments
deterministic stdout
empty stderr
```

The verifier reconstructs the J simplex, all 120 simplex permutations, all five
24-member partition stabilizers, their projectors, the full centralizer
equations, the four-member affine stabilizers, the affine centralizer basis,
the `R-C` breaker, the reversible pointer blocks, and the target comparison
last. Universal group and centralizer statements rest on the written proofs.

## Field 3: carrier

```text
system:          (Q^4,G)
simplex labels:  F_5
full symmetry:   S_5
record group:    S_4 at each token
affine control:  C_4 at each token
pointer:         (Q^2,I_2)
post quotient:   T ~ -T
```

No external data.

## Field 4: completeness and systematics

No tolerance. Exact obligations:

```text
C1  authority, collision, target-independence source guard;
C2  J phase motor and regular-simplex identities;
C3  complete 120-member S_5 representation, faithfulness and group law;
C4  five complete 24-member S_4 partition stabilizers;
C5  P_k,Q_k projector identities and ranks;
C6  S_4 centralizer nullity one at every token, with Q_k a basis;
C7  complete effect reduction to T=+-Q_k and one physical class;
C8  reversible pointer realization and strict-idempotence sign choice;
C9  affine C_4 centralizer nullity three with R,C,J basis;
C10 R-C exact nonterminal breaker and failure of full S_4 covariance;
C11 affine transport across all tokens;
C12 target comparison only after C1-C11;
C13 O1/O2/sampling/decoder/layer firewalls.
```

A hidden target input, omitted permutation, incomplete stabilizer, float,
pre-pin execution, changed threshold, unnamed lift, or post-pin mutation is
STOP.

## Field 5: decision

```text
RECORD-COMPLETE-SELECTION
  C1-C13 pass and the complete S_4 record-partition class has exactly one
  physical post-state class, represented by +-Q, with final Lueder comparison.

PARTITION-STABILIZER-F
CENTRALIZER-F
SELECTION-F
BOUNDARY-F
TARGET-F
STOP
```

No tolerance. A valid scientific or falsified route exits zero. STOP exits
nonzero and carries no scientific conclusion.

Maximum later candidate rows on `RECORD-COMPLETE-SELECTION`:

```text
QDD-RECORD-PARTITION-STABILIZER [T]
QDD-RECORD-COMPLETE-LUEDER-SELECTION [T]
QDD-AFFINE-RESIDUAL-LABEL-BOUNDARY [T]
```

All are restricted L4 statements. They do not close O2 globally because
record-partition completeness remains an added physical premise.

## Field 6: layer

L4 apparatus/support only. No L5/L6 lift. Apparatus records are not identified
with public `D_clock` records. O1 is untouched.

```text
SAMPLING NOT PROVIDED.
```

## Formal order

1. Commit and push this file and `verify.py` together.
2. Read both files back publicly and record hashes, bytes, line endings, blobs.
3. Execute the pinned verifier exactly once from repository root.
4. Add `EXPECTED.txt`, `RUN.md`, and `RESULT.md` without changing pinned bytes.
5. Open one probe-only pull request and require byte identity on x86_64 and
   aarch64 plus aggregate `check`.
6. Merge any valid scientific or falsified route without squash or rebase.
7. Canon treatment is a separate fold.
