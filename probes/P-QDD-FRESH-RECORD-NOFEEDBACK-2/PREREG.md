# P-QDD-FRESH-RECORD-NOFEEDBACK-2 preregistration

Date: 2026-08-20

Author of record: A. M. Thorn

Status: preregistered protocol only. No scientific result is earned here. The
accepted verifier has formal execution count zero and may not be imported or
executed before this file and `verify.py` are committed together, pushed, and
read back byte for byte from the public remote.

Public claim lock: issue 472.

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

Target: blocker O2 of `QDD-INSTRUMENT-APPARATUS [O]` only, at L4.

## Mandatory predecessor STOP disclosure

Issue 470 and `P-QDD-FRESH-RECORD-NOFEEDBACK-1` are permanently closed with
`STOP / VERIFIER FIXTURE DEFECT / NO SCIENTIFIC CONCLUSION`. Their sole formal
execution exited nonzero because the old-record control changed the label on
only one entry of a multi-entry sparse state and then required every entry to
carry that label. No mathematical disagreement was established. The old pin is
not repaired, renamed, rerun, or used as evidence.

This successor freezes before its own pin a total map

```text
relabel_record(state, cell, label)
```

which changes the selected record coordinate on every sparse-state entry.
Nothing scientific changes: carrier, premises, target, routes, threshold,
layer, and output conclusion are the same.

## Result exposure

Before issue 470, non-canonical reasoning identified `T_*=R-C` as the likely
nonterminal witness. The sealed centralizer probe also exposed the geometry.
Those materials are discovery context only. This verifier imports and executes
no predecessor code, helper, transcript, or result. Static compilation is
allowed before the pin; scientific execution is forbidden.

## Field 1: equation

Let `(V,G)` be rational with nondegenerate symmetric Gram matrix. Write
`A^sharp=G^-1 A^T G`. Let `P,Q` be complementary G-orthogonal projectors and
let the moving branch T obey

```text
P^2=P=P^sharp, Q^2=Q=Q^sharp, P+Q=I, PQ=QP=0,
TP=PT=0, QT=TQ=T, T^sharp T=Q.
```

Thus T is invertible on QV. Physical post-state equivalence is `T ~ -T`.
Projective idempotence means

```text
[T]^2=[T], equivalently T^2=+T or T^2=-T.
```

### Fresh pointer and reversible record

Use a fresh pointer `A=Q^2`, ready state `a_0`, and flip X. Define

```text
U_T=P tensor I_A + T tensor X.
```

Cross terms vanish and `U_T^sharp U_T=I`. Use a fresh record cell `M=Q^3`
with basis `blank,LOW,HIGH`. Let `S_LOW` swap blank/LOW and `S_HIGH` swap
blank/HIGH. With pointer projectors `pi_0,pi_1`, put

```text
W=pi_0 tensor S_LOW + pi_1 tensor S_HIGH,
F_T=(I_V tensor W)(U_T tensor I_M).
```

Both maps are rational and reversible. On a prepared pair,

```text
F_T(v tensor a_0 tensor blank)
 = Pv tensor a_0 tensor LOW + Tv tensor a_1 tensor HIGH.
```

For every finite N, use N distinct fresh pointer-record pairs. Step j acts on
the system and pair j and as identity on all old and unused pairs.

```text
fresh: pair j enters as a_0 tensor blank and is used once;
append-only: every old pair is thereafter acted on by identity;
no feedback: no old pointer or record controls any later system map.
```

`Irreversible record` means monotone protocol history, not microscopic
noninvertibility. Every finite closed map remains reversible.

LOW repeats because `P(Pv)=Pv,T(Pv)=0`. HIGH repeats because
`P(Tv)=0,Q(Tv)=Tv`. Conditioned on N HIGH outcomes,

```text
system state=T^N v, pointer word=1^N, record word=HIGH^N.
```

Hence ordinary repeatability and persistent records constrain support and
history, not the internal powers of T.

### Target-independent J witness

Work on `V=Q^4` with

```text
one=(1,1,1,1)^T,
G=I-(1/5) one one^T,
D=M_J-I,
M_J=[[1,0,-1,1],[0,1,-1,0],[1,0,0,0],[0,1,-1,1]].
```

Put `u_x=D^x e_0`, x in F_5. Then

```text
D^5=I, D^T G D=G,
sum_x u_x=0,
<u_x,u_y>_G=4/5 for x=y and -1/5 otherwise,
u_2=-one.
```

Define `rho(c,b)u_x=u_(b+cx)`. For token k, average its multiplier
stabilizer to obtain P_k and Q_k=I-P_k. Let g_k be multiplier two and put

```text
R_k=(1/4)(I-g_k+g_k^2-g_k^3),
C_k=Q_k-R_k,
J_k=g_k C_k.
```

The exact identities are

```text
rank R_k=1, rank C_k=2, Q_k=R_k+C_k,
R_k^2=R_k=R_k^sharp, C_k^2=C_k=C_k^sharp,
R_k C_k=C_k R_k=0, J_k^2=-C_k, J_k^sharp=-J_k.
```

Freeze

```text
T_*=R_k-C_k.
```

Then

```text
T_*^sharp=T_*, T_*^sharp T_*=Q_k, T_*^2=Q_k,
T_* != +Q_k, T_* != -Q_k.
```

For nonzero `w_R in im R_k`, `w_C in im C_k`, and `w=w_R+w_C`,

```text
T_*w=w_R-w_C, T_*^2w=w_R+w_C.
```

The two rays differ, while the fresh apparatus writes HIGH at every repetition,
old records persist, and no record feeds back. This is the frozen
nonimplication witness.

### Exact positive boundary

Define the stronger premise:

```text
record sufficiency:
  for one terminal outcome symbol, the conditioned system ray depends only on
  that symbol and not on the number of identical fresh repetitions.
```

For HIGH this gives `[T^2v]=[Tv]`. Since T is invertible on QV, T preserves
every rational line. A linear map preserving every line in dimension at least
two is scalar: for independent u,v, compare Tu, Tv and T(u+v). Hence
`T=lambda Q`, and `T^sharp T=Q` gives `lambda=+1` or `-1`. Conversely ±Q is
ray-terminal. Therefore inside the frozen invertible branch class,

```text
record sufficiency
iff fresh-pointer ray terminality
iff [T]^2=[T]
iff T in {+Q,-Q}.
```

This extra premise is not append-only persistence, no-feedback, reversibility,
or ordinary repeatability.

### Target comparison last

Only after all preceding statements, compare token k=2 with

```text
E_low=(1/4) one one^T, E_high=I-E_low.
```

Since `u_2=-one`, `P_2=E_low,Q_2=E_high`. Thus the target-independent
`T_*=R_2-C_2` realizes the HIGH effect and violates projective idempotence.

## Field 2: code

Accepted exact file:

```text
probes/P-QDD-FRESH-RECORD-NOFEEDBACK-2/verify.py
```

Python standard library only; integers and Fraction only; no float, random,
network, subprocess, external data, or predecessor import. Zero arguments,
deterministic stdout, empty stderr. It reconstructs J and the affine
stabilizers, audits P,Q,R,C,J and T_*, the reversible writer and one-step
coupling, three fresh HIGH/LOW repetitions, total old-record relabel controls,
repeatability with moving rays, ±Q projective-idempotence controls, record
persistence versus sufficiency, and target comparison last. The N=3 sweep is
a regression; written proofs carry all-N and universal claims.

## Field 3: carrier

```text
system:       (Q^4,G)
pointer cell: (Q^2,I_2)
record cell:  (Q^3,I_3), blank/LOW/HIGH
N protocol:   Q^4 tensor (Q^2 tensor Q^3)^N
witness:      T_*=R_k-C_k
quotient:     T ~ -T
```

No external data.

## Field 4: completeness

No tolerance. Obligations:

```text
C1 authority, collision, path, layer, target independence;
C2 general branch assumptions;
C3 reversible coupling and writer;
C4 append-only prefix preservation;
C5 no old-record feedback;
C6 all-N repeatability and T^N formula;
C7 fresh J/affine/stabilizer reconstruction;
C8 exact T_*=R-C witness;
C9 persistence does not imply sufficiency;
C10 sufficiency equivalence to projective terminality;
C11 target comparison after C1-C10;
C12 O1/O2/sampling/decoder/layer firewalls.
```

The displayed extension is complete for every T satisfying the branch
relations. No claim covers every conceivable J-native apparatus. Hidden target
input, old-record control, nonfresh cell, overwritten record, nonreversible
writer, float, pre-pin result, unnamed lift, or scope change is STOP.

## Field 5: decision

```text
NONIMPLICATION
  C1-C12 pass and T_*=R-C satisfies every fresh, append-only, no-feedback,
  reversible and ordinary-repeatability premise while [T_*]^2 != [T_*].

IMPLICATION
  C1-C12 pass and the frozen premises force [T]^2=[T].

RECORD-EXTENSION-F
J-WITNESS-F
BOUNDARY-F
STOP
```

No tolerance. A valid scientific route exits zero. STOP exits nonzero and
carries no scientific conclusion.

Maximum later candidate rows on NONIMPLICATION:

```text
QDD-FRESH-RECORD-EXTENSION [T]
QDD-PROJECTIVE-IDEMPOTENCE-NONIMPLICATION [T]
QDD-RECORD-SUFFICIENCY-TERMINALITY [T]
```

All are restricted L4 statements and do not close O2 globally.

## Field 6: layer

L4 apparatus/support only. The protocol record is not a realized L5 stream and
not the public D_clock accumulated record. No L5/L6 lift. O1 untouched.

```text
SAMPLING NOT PROVIDED.
```

Global O2 remains open. A later positive attack must derive record sufficiency,
terminality, or another selector from a separately typed physical premise.

## Formal order

1. Commit and push this file and verify.py together.
2. Publicly read back both files and record hashes, bytes, line endings, blobs.
3. Execute the pinned verifier exactly once from repository root.
4. Add EXPECTED.txt, RUN.md and RESULT.md without changing pinned bytes.
5. Open one probe-only PR; require byte identity on x86_64 and aarch64 and the
   aggregate check.
6. Merge any valid scientific or falsified route without squash or rebase.
   Canon treatment is a separate fold.
