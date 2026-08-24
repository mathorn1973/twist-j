# P-QDD-RECORD-NATURALITY-FORK-1 preregistration

Date: 2026-08-20

Author of record: A. M. Thorn

Status: preregistered protocol only. No scientific result is earned here. The
accepted verifier has formal execution count zero and may not be imported or
executed before this file and `verify.py` are committed together, pushed, and
read back byte for byte from the public remote.

Public claim lock: issue 476.

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v57
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v57
CONTENT_COMMIT: 8e8b04abe4d3359942449533854ef1d142be70df
CANON_SHA256:   c96a2ef52c78d68ef8f04b582e4a17328e6a863b49664f29b1bd324171d802a8
CANON_BYTES:    295013
BASE_COMMIT:    e6845b96fc19a47c473761ad49d4f8a7812c2f58
```

Target: blocker O2 of `QDD-INSTRUMENT-APPARATUS [O]` only, at L4.

## Result exposure and lineage

This is result-exposed, proof-first work. Before issue 476, non-canonical
reasoning identified the expected fork:

```text
strict law naturality  -> scalar centralizer -> one Lueder sign class;
weak quotient covariance -> +-S_4 normalizer -> 24 registered sign classes.
```

Those calculations are discovery context only. Every earlier scratch matrix,
count, transcript, and witness is excluded from formal evidence.

The sealed probes `P-QDD-RECORD-COMPLETE-STABILIZER-1` and
`P-QDD-FRESH-RECORD-NOFEEDBACK-2` are lineage and boundary controls. No
predecessor helper, verifier, transcript, output, or expected file is imported
or executed. This probe reconstructs the J simplex, the record stabilizers, the
centralizer, the automorphism group, and the normalizer independently.

Static parsing and syntax compilation are allowed before the pin. Scientific
execution is forbidden.

The written proofs below carry the universal statements. The verifier audits
their exact finite ingredients and does not replace their quantifiers.

## Field 1: equation

### 1. Public J simplex

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
D^5=I,
D^T G D=G,
sum_x u_x=0,
<u_x,u_y>_G=4/5 if x=y and -1/5 otherwise,
u_2=-one.
```

The first four vertices are a rational basis and the fifth is their negative
sum.

For every permutation `pi in S_5`, there is a unique rational map

```text
rho(pi) u_x = u_(pi(x)).
```

It exists because the unique relation `sum_x u_x=0` is permutation invariant.
It is G-orthogonal because it preserves the complete Gram table. It is faithful
because the five distinct vertices span V. Conversely every linear
automorphism preserving the marked vertex set induces one permutation.
Therefore the complete marked-simplex automorphism group is exactly `S_5`.

### 2. Binary terminal record

Fix a terminal token `k in F_5`. The binary record stores only

```text
LOW  = {k},
HIGH = F_5 minus {k}.
```

The complete stabilizer of this partition, fixing the LOW cell, is

```text
Gamma_k = {pi in S_5 : pi(k)=k} ~= S_4.
```

Define before any target comparison

```text
P_k = (1/24) sum_(pi in Gamma_k) rho(pi),
Q_k = I_4 - P_k.
```

The group average is the G-orthogonal projector onto the fixed space. Since
`Gamma_k` fixes `u_k` and is transitive on the other four vertices, its fixed
space inside V is exactly `Q u_k`. Hence

```text
P_k^2=P_k=P_k^sharp, rank(P_k)=1, im(P_k)=Q u_k,
Q_k^2=Q_k=Q_k^sharp, rank(Q_k)=3,
P_k Q_k=Q_k P_k=0.
```

The moving space `W_k=Q_k V` is the standard three-dimensional rational
representation of `S_4`.

A moving branch is required throughout to satisfy

```text
T P_k=P_k T=0,
T^sharp T=Q_k.
```

Thus its restriction to `W_k` is an invertible G-isometry. The registered
post-state equality inherited from `QDD-INSTRUMENT-NONSELECTION` remains

```text
T ~_post L iff T=+L or T=-L
```

inside one nonzero effect fibre.

### 3. Strict law naturality

Treat the record presentations as the one-object groupoid `B Gamma_k`, and the
moving carrier as its representation `rho|_(W_k)`. A natural endomorphism has
one component T and the naturality square is exactly

```text
T rho(g)=rho(g) T for every g in Gamma_k.
```

This is the centralizer condition.

Identify the four HIGH vertices with the permutation module `Q^4` and its
standard submodule

```text
W = {(x_1,x_2,x_3,x_4): x_1+x_2+x_3+x_4=0}.
```

Every rational matrix A commuting with all permutation matrices has one common
diagonal value `a` and one common off-diagonal value `b`, because transpositions
move every diagonal position to every other diagonal position and every
ordered off-diagonal position to every other one. Thus

```text
A=(a-b)I+b 11^T.
```

On W the second term vanishes. Therefore

```text
End_(Gamma_k)(W_k)=Q Q_k.
```

Every strictly natural branch is

```text
T=lambda Q_k.
```

The effect equation gives

```text
lambda^2 Q_k=T^sharp T=Q_k,
lambda in {+1,-1}.
```

Under the registered sign equality this is one physical class. Strict
representative idempotence selects `+Q_k`.

This is the already expected positive side of the fork. The new question is
whether weaker observational requirements force this strict naturality.

### 4. Weak relabeling covariance

Freeze the weaker uniform covariance condition:

```text
there exists alpha in Aut(Gamma_k) such that
T rho(g) T^sharp = rho(alpha(g)) Q_k
for every g in Gamma_k.
```

Since T is invertible on `W_k`, this says exactly that T normalizes the image of
`Gamma_k`. It is enough for T to map every invisible-label orbit uniformly to
another invisible-label orbit. It does not require the same relabeling g to
appear before and after T.

#### Aut(S_4)=Inn(S_4)

There are exactly four subgroups of `S_4` isomorphic to `S_3`, namely the four
point stabilizers. Every `S_3` subgroup contains three transpositions forming
the edge set of one triangle on three of the four points, so it fixes the
remaining point and is one of these four.

An automorphism of `S_4` permutes the four `S_3` subgroups, giving a homomorphism

```text
Aut(S_4) -> S_4.
```

The action is faithful. If an automorphism fixes every point stabilizer, it
fixes their pairwise intersections. Each pairwise intersection is the
order-two subgroup generated by the transposition of the two remaining
points. Hence it fixes all six transpositions, which generate `S_4`, so it is
the identity.

Thus `Aut(S_4)` embeds in `S_4`. The inner automorphism group already has order
24 because the center of `S_4` is trivial. Therefore

```text
Aut(S_4)=Inn(S_4).
```

The verifier independently audits this with the Coxeter generators
`s_1=(12), s_2=(23), s_3=(34)`: it enumerates every generating triple obeying
the three involution relations, the two braid relations, and the distant
commutation relation. Exactly 24 triples survive and they are exactly the 24
inner conjugates.

#### Complete normalizer

Let T satisfy weak covariance and let `alpha` be its induced automorphism.
Choose `h in Gamma_k` with

```text
alpha(g)=h g h^-1
```

for every g. Then

```text
rho(h)^sharp T
```

commutes with every `rho(g)` on `W_k`. By the centralizer theorem it equals
`lambda Q_k`. Hence

```text
T=lambda rho(h) Q_k.
```

The effect equation gives `lambda=+1` or `lambda=-1`. Conversely every such
member normalizes the group. Therefore the complete rational G-orthogonal weak
normalizer is

```text
N_k = {+rho(h)Q_k,-rho(h)Q_k : h in Gamma_k}.
```

There are 48 algebraic members. Modulo only the registered sign equality there
are exactly 24 classes. Indeed, equality up to sign gives

```text
rho(h^-1 h')|_(W_k)=+I or -I.
```

The plus case gives `h=h'` by faithfulness. The minus case is impossible:
`-I` is central, while a faithful image of a nonidentity central element would
give a nontrivial element of the trivial center of `S_4`.

### 5. Exact nonterminal weak-covariance witness

Choose a transposition `tau` of two HIGH labels and put

```text
T_tau=rho(tau) Q_k.
```

Then

```text
T_tau^sharp T_tau=Q_k,
Q_k T_tau=T_tau Q_k=T_tau,
T_tau^2=Q_k,
T_tau != +Q_k,
T_tau != -Q_k.
```

It normalizes the full record stabilizer by inner conjugation. It commutes with
exactly four of its 24 elements, the centralizer of a transposition, and fails
the other 20 strict naturality squares.

Choose distinct HIGH labels `a,b,c,d` with `tau` swapping a,b and fixing c,d.
Put

```text
w_minus=u_a-u_b,
w_plus =u_c-u_d,
w=w_plus+w_minus.
```

Both components lie in `W_k`, with eigenvalues `-1` and `+1`. Therefore

```text
T_tau w=w_plus-w_minus,
T_tau^2 w=w_plus+w_minus,
```

and these two vectors span a two-dimensional space. The first and second
conditioned rays differ. Thus weak covariance, exact effects, support
repeatability, involutivity, and the same HIGH record do not imply projective
idempotence.

### 6. Observable quotient completeness

Let

```text
widehat Gamma_k={+rho(g)Q_k,-rho(g)Q_k : g in Gamma_k}.
```

Define the complete observational equality on moving rays by its orbit
quotient. Every T in `N_k=widehat Gamma_k` acts trivially on that quotient,
because `Tv` belongs to the same `widehat Gamma_k` orbit as v.

This is a valid way to make all 48 microscopic representatives one
observational class. It is not a selection theorem under the registered
post-state equality. It changes equality from global sign alone to the full
extended record-stabilizer gauge orbit.

Therefore:

```text
complete observation of the quotient
does not imply
strict law naturality of the microscopic representative.
```

It can identify the 24 registered sign classes only by adopting a new gauge
equality. It cannot prove that the microscopic branch itself is `+Q_k` or
`-Q_k`.

The distinction is exact:

```text
strict natural endomorphism      centralizer  -> 1 registered sign class;
uniform quotient covariance      normalizer   -> 24 registered sign classes;
extended gauge equality          quotient     -> 1 newly identified class.
```

### 7. Same typed record does not choose between them

Use a fresh binary pointer with ready state `p_0` and flip X. For any admitted
T define

```text
U_T=P_k tensor I_2+T tensor X.
```

Both

```text
T_0=Q_k,
T_1=T_tau
```

give rational reversible pointer couplings, the same ordered effects
`(P_k,Q_k)`, and the same terminal LOW/HIGH symbol. They differ as registered
post-state maps, and only `T_0` is strictly natural.

Hence the displayed typed record interface and complete quotient observation
admit both laws. A future positive derivation must supply either:

```text
strict law naturality as a physical law,
```

or

```text
an independently justified enlarged post-state gauge equality.
```

The current public typed partial decoder, whose outputs do not feed the state
update, is not promoted or completed by this statement.

### 8. Target comparison, deliberately last

Only after the simplex, centralizer, automorphism theorem, complete normalizer,
class counts, witness, pointer comparison, and equality boundary are frozen,
compare token `k=2` with

```text
E_low=(1/4) one one^T,
E_high=I_4-E_low.
```

Since `u_2=-one`,

```text
P_2=E_low,
Q_2=E_high.
```

The strictly natural class is the Lueder class. The weak-covariant
transposition witness realizes the same HIGH effect while remaining
sign-inequivalent and nonterminal.

## Field 2: code

Accepted exact file:

```text
probes/P-QDD-RECORD-NATURALITY-FORK-1/verify.py
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

The verifier reconstructs:

1. the J motor and five-vertex simplex;
2. all 120 simplex permutations and the complete group law;
3. all five 24-member record stabilizers and their projectors;
4. the one-dimensional strict centralizer at every token;
5. the 24 Coxeter-image automorphisms and their equality with the inner list;
6. every one of the 48 normalizer members at every token and every conjugation
   equation;
7. the 24 registered sign classes and one extended-gauge class;
8. the strict subset `+-Q`;
9. the transposition breaker, its 4 versus 20 commutation split, involution,
   effect, support, and mixed-ray failure;
10. two reversible pointer couplings with identical ordered effects and record
    symbols;
11. the target comparison last.

The universal normalizer and nonimplication statements rest on the written
proofs above.

## Field 3: carrier

```text
system:                (Q^4,G)
simplex labels:        F_5
full simplex group:    S_5
record stabilizer:     Gamma_k ~= S_4
moving support:        Q_k V, dimension 3
pointer:               (Q^2,I_2)
registered equality:   T ~ -T
comparison equality:   orbit under +-Gamma_k, not adopted
```

No external data.

## Field 4: completeness and systematics

No tolerance. Exact obligations:

```text
C1  authority, collision, source guard, target independence;
C2  J motor and simplex;
C3  complete S_5 representation and group law;
C4  complete S_4 record stabilizers and projectors;
C5  strict centralizer dimension one at all five tokens;
C6  Aut(S_4)=Inn(S_4), written proof plus exact Coxeter audit;
C7  complete weak normalizer theorem and all 48 members;
C8  registered sign quotient exactly 24 classes;
C9  strict natural subset exactly +-Q, one sign class;
C10 transposition witness and nonterminal mixed ray;
C11 extended gauge quotient exactly one comparison class;
C12 same typed pointer record and effects admit strict and nonstrict laws;
C13 target comparison after C1-C12;
C14 O1, O2, sampling, decoder, equality, and layer firewalls.
```

A hidden target input, omitted permutation, incomplete automorphism class,
incomplete normalizer, changed equality, float, pre-pin execution, changed
threshold, unnamed lift, post-pin mutation, or imported predecessor evidence is
STOP.

## Field 5: decision

No tolerance.

```text
NATURALITY-FORK
  C1-C14 pass; strict law naturality selects one Lueder sign class; weak
  quotient covariance leaves 24 sign classes; only the explicitly new extended
  gauge equality collapses them.

STRICT-NATURALITY-F
  a non-scalar strict natural endomorphism survives.

AUTOMORPHISM-F
  Aut(S_4) differs from Inn(S_4).

NORMALIZER-F
  the complete weak normalizer differs from +-S_4.

NONSELECTION-F
  the sign quotient count, transposition witness, or nonterminality boundary
  fails.

GAUGE-BOUNDARY-F
  the orbit quotient or equality distinction fails.

TARGET-F
  the final target comparison fails.

STOP
  authority, integrity, completeness, security, evidence, layer, or
  deterministic-output discipline fails.
```

Maximum later candidate rows on `NATURALITY-FORK`:

```text
QDD-RECORD-NORMALIZER-CLASS [T]
QDD-OBSERVABLE-QUOTIENT-NONSELECTION [T]
QDD-LAW-NATURALITY-VS-GAUGE-BOUNDARY [T]
```

All are restricted L4 theorems. They do not close O2 globally. O2 still
requires an independently specified physical selector, a derivation of strict
law naturality, or an independently justified physical equality. O1 is
untouched.

## Field 6: layer

L4 apparatus/support only. No L5 stream or L6 measure. Apparatus records are
not identified with public `D_clock` records. No decoder completion or
`QUADRATIC-DECODER-DATA` move.

```text
SAMPLING NOT PROVIDED.
```

## Formal order

1. Commit and push this file and `verify.py` together.
2. Read both files back publicly and record SHA-256, bytes, line endings, and
   Git blobs.
3. Execute the pinned verifier exactly once from repository root.
4. Add `EXPECTED.txt`, `RUN.md`, and `RESULT.md` without changing pinned bytes.
5. Open one probe-only pull request and require byte identity on x86_64 and
   aarch64 plus aggregate `check`.
6. Merge any valid scientific or falsified route without squash or rebase.
7. Canon treatment is a separate fold.
