# P-QDD-FRESH-RECORD-NOFEEDBACK-1 preregistration

Date: 2026-08-20

Author of record: A. M. Thorn

Status: preregistered protocol only. No scientific result is earned by this
file. The accepted verifier has formal execution count zero. It may not be
imported or executed before this file and `verify.py` are committed together,
pushed, and read back byte for byte from the public remote.

Public claim lock: issue 470.

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v57
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v57
CONTENT_COMMIT: 8e8b04abe4d3359942449533854ef1d142be70df
CANON_SHA256:   c96a2ef52c78d68ef8f04b582e4a17328e6a863b49664f29b1bd324171d802a8
CANON_BYTES:    295013
BASE_COMMIT:    4ef54f0c34f80897af0121a2d93b710e70a8377c
```

Target: blocker O2 of `QDD-INSTRUMENT-APPARATUS [O]` only.

The public decoder clause says that decoder outputs do not feed the autonomous
update `U`. That is not silently lifted into an apparatus theorem here. This
probe defines a separate exact L4 no-feedback protocol and asks whether that
protocol, together with fresh apparatus cells, append-only records,
reversibility, and ordinary outcome repeatability, forces projective
idempotence of the post-state branch.

The answer is not selected in advance by the protocol vocabulary. Both
`NONIMPLICATION` and `IMPLICATION` are first-class exit-zero scientific routes.

## Result-exposure disclosure

Before issue 470, NON-CANONICAL reasoning identified the candidate witness
`T_*=R-C` and anticipated that append-only record persistence constrains the
record carrier but not the internal branch motion. The sealed predecessor
`P-QDD-J-CENTRALIZER-TERMINALITY-1` also exposes the relevant centralizer
geometry. Those calculations and files are discovery context only. This probe
imports and executes no predecessor verifier, helper, stdout, or result file.
It reconstructs the required J data from the displayed public step matrix.

Static source inspection and syntax compilation are allowed before the pin.
Scientific execution is forbidden. The written proofs below carry the
universal statements. The verifier is an exact audit and breaker surface.

## Field 1: equation

### 1. General branch data

Let `(V,G)` be a finite-dimensional rational vector space with nondegenerate
symmetric Gram matrix `G`. For an endomorphism `A`, write

```text
A^sharp = G^-1 A^T G.
```

Let `P,Q` be complementary `G`-orthogonal projectors:

```text
P^2=P=P^sharp,
Q^2=Q=Q^sharp,
P+Q=I,
PQ=QP=0.
```

Let the moving branch `T` obey

```text
TP=PT=0,
QT=TQ=T,
T^sharp T=Q.
```

Thus `T` is an isometry and hence invertible on `QV`. No projective
idempotence is assumed.

The physical post-state equivalence used in this scope is the registered
branchwise sign equivalence

```text
T ~_post L  iff  T=+L or T=-L.
```

Projective idempotence is therefore the equation

```text
[T]^2=[T]
```

in the sign quotient, equivalently

```text
T^2=+T or T^2=-T.
```

### 2. Fresh pointer and reversible record writer

Use a fresh binary pointer space `A=Q^2` with basis `a_0,a_1`, ready state
`a_0`, identity `I_A`, and flip

```text
X a_0=a_1,
X a_1=a_0.
```

Define the system-pointer coupling

```text
U_T = P tensor I_A + T tensor X.
```

The cross terms vanish because `PT=TP=0`. Therefore

```text
U_T^sharp U_T
 = P tensor I_A + T^sharp T tensor I_A
 = (P+Q) tensor I_A
 = I.
```

Since the carrier is finite-dimensional, `U_T` is reversible with inverse
`U_T^sharp`.

Use a fresh record cell `M=Q^3` with ordered orthonormal basis

```text
m_blank, m_LOW, m_HIGH.
```

Let `S_LOW` swap `blank` and `LOW` while fixing `HIGH`, and let `S_HIGH`
swap `blank` and `HIGH` while fixing `LOW`. Both are involutive permutation
matrices. With pointer coordinate projectors `pi_0,pi_1`, define

```text
W = pi_0 tensor S_LOW + pi_1 tensor S_HIGH.
```

Then

```text
W^T W=I,
W^2=I.
```

The one-cell apparatus step on `V tensor A tensor M` is

```text
F_T = (I_V tensor W)(U_T tensor I_M).
```

It is a product of rational orthogonal maps and is therefore rational and
reversible.

On the prepared pointer-record state `a_0 tensor m_blank`, one has exactly

```text
F_T(v tensor a_0 tensor m_blank)
 = Pv tensor a_0 tensor m_LOW
 + Tv tensor a_1 tensor m_HIGH.
```

This formula contains the complete branch and record semantics. It uses no
target effect and no probability parameter.

### 3. Finite append-only protocol

For every `N>=1`, use `N` distinct fresh pairs `(A_j,M_j)`. At step `j`, apply
`F_T` only to the system and pair `j`, tensored with the identity on every
older and every not-yet-used pair.

This is the frozen meaning of the three protocol words:

```text
fresh:
  pair j enters in a_0 tensor m_blank and is used exactly once;

append-only record:
  after step j, every earlier pointer and record cell is acted on by identity;
  the record word is extended by one symbol and its existing prefix is fixed;

no feedback:
  the system-pointer factor of step j contains no projector, coefficient,
  control, or branch choice read from any earlier pointer or record cell.
```

`Append-only irreversible` is therefore protocol monotonicity, not microscopic
noninvertibility. The complete closed map remains reversible. Erasure and
rewriting of old cells are outside the admitted protocol.

Each finite protocol map is a composition of rational orthogonal maps and is
therefore reversible.

### 4. Outcome repeatability and repeated post-state

If the LOW branch fires, its state is `Pv`. A fresh repetition gives

```text
P(Pv)=Pv,
T(Pv)=0,
```

so LOW repeats with certainty and the system state is unchanged.

If the HIGH branch fires, its state is `Tv`. Since `QT=T` and `PT=0`,

```text
P(Tv)=0,
Q(Tv)=Tv.
```

A fresh repetition therefore returns HIGH with certainty, while the system
state becomes `T^2v`. By induction, conditioned on `N` HIGH outcomes,

```text
system state = T^N v,
pointer word = 1^N,
record word  = HIGH^N.
```

Every earlier record persists and no earlier record affects this induction.
Ordinary repeatability is therefore a support theorem. It places no equation
on the internal powers `T^N` beyond support preservation.

### 5. Target-independent J-native witness

Work on the public rational J carrier

```text
V=Q^4,
one=(1,1,1,1)^T,
G=I_4-(1/5) one one^T,
D=M_J-I_4.
```

The displayed public step matrix is

```text
M_J =
[[1,0,-1,1],
 [0,1,-1,0],
 [1,0, 0,0],
 [0,1,-1,1]].
```

Since `D` is multiplication by `zeta_5^2`,

```text
D^5=I,
D^T G D=G.
```

Put

```text
u_x=D^x e_0,   x in F_5.
```

Then

```text
sum_x u_x=0,
<u_x,u_y>_G=4/5 if x=y and -1/5 otherwise,
u_2=-one.
```

For `c in F_5^x,b in F_5`, define the unique rational affine map

```text
rho(c,b)u_x=u_(b+cx).
```

For a memory token `k`, let

```text
H_k={x -> k+a(x-k): a in F_5^x},
P_k=(1/4) sum_(h in H_k) rho(h),
Q_k=I-P_k.
```

`P_k` is the `G`-orthogonal rank-one projector onto `Q u_k`; `Q_k` has rank
three. Let `g_k` be the multiplier-two generator of `H_k` and define

```text
R_k=(1/4)(I-g_k+g_k^2-g_k^3),
C_k=Q_k-R_k,
J_k=g_k C_k.
```

The exact multiplication data needed here are

```text
rank(R_k)=1,
rank(C_k)=2,
R_k^2=R_k=R_k^sharp,
C_k^2=C_k=C_k^sharp,
R_k C_k=C_k R_k=0,
Q_k=R_k+C_k,
J_k^2=-C_k,
J_k^sharp=-J_k.
```

No target effect enters this construction.

Freeze the branch

```text
T_* = R_k-C_k.
```

Then

```text
T_*^sharp=T_*,
T_*^sharp T_*=Q_k,
T_*^2=Q_k,
T_* != +Q_k,
T_* != -Q_k.
```

Thus `T_*` satisfies every general branch premise and is a self-adjoint
involution on `Q_kV`, but

```text
[T_*]^2=[Q_k] != [T_*].
```

Choose nonzero vectors

```text
w_R in im(R_k),
w_C in im(C_k),
w=w_R+w_C.
```

The summands are independent because their projector images are disjoint. Now

```text
T_*w   = w_R-w_C,
T_*^2w = w_R+w_C.
```

If these two vectors were proportional, comparison of the nonzero `R_k` and
`C_k` components would require the same scalar to be both `+1` and `-1`.
Hence their rational rays differ.

Nevertheless the append-only protocol records

```text
HIGH, HIGH, HIGH, ...
```

and never reads those records back into the system map. This is the frozen
nonimplication witness.

### 6. Record sufficiency boundary

Record persistence says only that a written symbol survives. Define the
strictly stronger premise

```text
record sufficiency:
  for a fixed terminal outcome symbol, the conditioned system ray is a
  function of that symbol alone and does not depend on how many identical
  fresh repetitions produced the same symbol.
```

For HIGH, comparing one and two repetitions gives

```text
[T^2 v]=[T v]
```

for every nonzero branch state. Since `T` is invertible on `QV`, put `w=Tv`.
Then every rational line in `QV` is invariant under `T`.

Lemma. A linear map on a rational vector space of dimension at least two that
preserves every line is scalar. For independent `u,v`, write

```text
Tu=alpha u,
Tv=beta v,
T(u+v)=gamma(u+v).
```

Linearity gives `alpha=beta=gamma`. Repeating over a basis gives

```text
T=lambda Q.
```

The effect equation gives `lambda^2=1`, hence

```text
T=+Q or T=-Q.
```

These are one post-state class. Conversely `T=+Q` or `T=-Q` makes the
conditioned ray independent of repetition count. Thus, inside the frozen
invertible branch class,

```text
record sufficiency
iff fresh-pointer ray terminality
iff [T]^2=[T]
iff T=+Q or T=-Q.
```

This boundary theorem does not derive record sufficiency from persistence,
no-feedback, reversibility, or repeatability. It identifies the exact extra
selection law.

### 7. Target comparison, deliberately last

Only after the general extension theorem, the append-only and no-feedback
protocol, the repeatability theorem, the J witness, and the record-sufficiency
boundary are frozen, compare token `k=2` with

```text
E_low=(1/4) one one^T,
E_high=I-E_low.
```

The identity `u_2=-one` gives

```text
P_2=E_low,
Q_2=E_high.
```

Therefore the target-independent witness `T_*=R_2-C_2` realizes the frozen
HIGH effect exactly while violating projective idempotence.

## Field 2: code

Accepted exact file:

```text
probes/P-QDD-FRESH-RECORD-NOFEEDBACK-1/verify.py
```

Requirements:

```text
Python standard library only
integers and Fraction only
no float, Decimal, complex approximation, randomness, network, external data,
subprocess, imported predecessor code, imported probe helper, or scratch output
zero arguments
deterministic stdout
empty stderr
```

The verifier has its own Fraction matrix kernel and audits:

1. target-independence source guard;
2. the J phase motor and five-vertex simplex;
3. all twenty affine maps and their exact group law;
4. all five stabilizer projectors and `R,C,J` multiplication data;
5. the exact `T_*=R-C` branch properties;
6. the reversible three-symbol record writer;
7. one-step system-pointer-record orthogonality and branch formula for four
   representative admitted moving maps;
8. a mixed-line projective-terminality breaker;
9. three fresh append-only HIGH and LOW repetitions by an independent sparse
   state engine;
10. an old-record mutation control proving that later system/fresh-cell output
    is unchanged while the old record persists;
11. ordinary outcome repeatability with moving conditional rays;
12. projective idempotence controls for `+Q,-Q` against `T_*`;
13. record persistence versus record sufficiency;
14. target comparison only after all preceding gates.

The finite three-cell audit is a regression. The all-`N` extension,
nonimplication, and equivalence statements rest on the written proofs above.

## Field 3: carrier or data

No external data.

```text
system carrier       (Q^4,G)
pointer cell         (Q^2,I_2)
record cell          (Q^3,I_3), labels blank/LOW/HIGH
finite N protocol    Q^4 tensor (Q^2 tensor Q^3)^N
witness branch       T_*=R_k-C_k
post-state quotient  T ~ -T
```

The verifier audits `N=3`; the theorem covers every finite `N>=1`.

## Field 4: systematics and completeness

There is no measurement systematic and no tolerance.

Exact obligations are:

```text
C1  current authority, collision, path, layer, and target independence;
C2  complete displayed general branch assumptions;
C3  reversible pointer coupling and reversible three-symbol writer;
C4  exact append-only, prefix-preserving finite protocol;
C5  exact no-feedback factorization through identity on old cells;
C6  all-N LOW/HIGH repeatability and T^N branch formula;
C7  fresh reconstruction of J, affine action, stabilizer and R,C,J data;
C8  exact T_*=R-C nonterminal witness;
C9  record persistence does not imply record sufficiency;
C10 record sufficiency equivalence to projective terminality in the frozen
    invertible branch class;
C11 target comparison only after C1-C10;
C12 preserve O1, O2, sampling, decoder, layer, and status firewalls.
```

The general extension class is complete for the displayed construction because
`F_T` is defined for every `T` satisfying the frozen branch equations. The
probe does not claim that the construction is the class of every possible
J-native apparatus.

A hidden target input, old-record control, nonfresh cell, overwritten record,
nonreversible writer, omitted branch term, floating tolerance, pre-pin result,
unnamed layer lift, or scope mutation is STOP.

## Field 5: decision and falsifiers

No tolerance exists.

```text
NONIMPLICATION
  C1-C12 pass and T_*=R-C satisfies every fresh-apparatus, append-only,
  no-feedback, reversible and ordinary-repeatability premise while
  [T_*]^2 != [T_*].

IMPLICATION
  C1-C12 pass and the complete frozen premises force [T]^2=[T], with no
  admitted exact nonterminal witness.

RECORD-EXTENSION-F
  an exact counterexample breaks the coupling, writer, append-only,
  no-feedback, repeatability, or all-N branch proof.

J-WITNESS-F
  an exact counterexample breaks the J reconstruction, R,C decomposition,
  T_* equations, mixed-line witness, or final target comparison.

BOUNDARY-F
  an exact counterexample breaks the equivalence between record sufficiency,
  ray terminality, projective idempotence, and the class {+Q,-Q}.

STOP
  authority, collision, pin, integrity, completeness, security, evidence,
  target independence, deterministic output, or layer discipline fails.
```

If `NONIMPLICATION` is earned, the maximum later candidate statements are:

```text
QDD-FRESH-RECORD-EXTENSION [T]
  every admitted branch isometry has the displayed reversible fresh-pointer,
  append-only three-symbol record extension with no old-record feedback and
  exact ordinary outcome repeatability;

QDD-PROJECTIVE-IDEMPOTENCE-NONIMPLICATION [T]
  those premises do not imply projective idempotence, witnessed by the exact
  target-independent J-native branch T_*=R-C;

QDD-RECORD-SUFFICIENCY-TERMINALITY [T]
  inside the frozen invertible branch class, record sufficiency is equivalent
  to fresh-pointer ray terminality and to the single Lueder post-state class
  {+Q,-Q}.
```

These are restricted L4 statements. They do not close O2 globally.

## Field 6: action layer

```text
L4 apparatus/support only.
```

The finite protocol record is an L4 apparatus register, not a realized public
L5 event stream and not the accumulated record object of `D_clock`. No L5 or
L6 lift is made. O1 is untouched. The only permitted sampling statement is

```text
SAMPLING NOT PROVIDED.
```

Global O2 and `QDD-INSTRUMENT-APPARATUS [O]` remain unchanged by this probe
alone. A later positive O2 attack must derive record sufficiency, terminality,
or another selecting law from a separately typed public physical premise.

## Formal sequence after the pin

1. Commit and push this file and the accepted exact `verify.py` together.
2. Read both files back from the public remote and record pin, SHA-256, bytes,
   line endings, final LF, and Git blobs on issue 470.
3. Only then execute
   `python3 probes/P-QDD-FRESH-RECORD-NOFEEDBACK-1/verify.py` exactly once from
   a clean directory rooted as the repository.
4. Commit exact `EXPECTED.txt`, neutral `RUN.md`, and `RESULT.md` without
   changing either pinned file.
5. Open one PR changing only this probe directory; require x86_64 and aarch64
   byte identity and aggregate `check`.
6. Merge any valid positive or negative scientific route without squash or
   rebase. Any later Canon or registry treatment is a separate sealed fold.
