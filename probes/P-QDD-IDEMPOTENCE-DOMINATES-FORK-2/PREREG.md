# P-QDD-IDEMPOTENCE-DOMINATES-FORK-2 preregistration

Date: 2026-08-20

Author of record: A. M. Thorn

Status: preregistered protocol only. No scientific result is earned here. The
accepted verifier has formal execution count zero and may not be imported or
executed before this file, `verify.py`, `audit_structure.py`, `audit_controls_a.py`,
`audit_controls_b.py`, `exact_matrix.py`, and `qdd_class.py` are committed together, pushed, and read back byte for byte from the public
remote.

Public claim lock: issue 480.

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v57
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v57
CONTENT_COMMIT: 8e8b04abe4d3359942449533854ef1d142be70df
CANON_SHA256:   c96a2ef52c78d68ef8f04b582e4a17328e6a863b49664f29b1bd324171d802a8
CANON_BYTES:    295013
BASE_COMMIT:    d44645a239df764c630984765a9fdd458b090a31
```

Target: blocker O2 of `QDD-INSTRUMENT-APPARATUS [O]` only, at L4.

## Mandatory predecessor STOP disclosure

Issue 479 and `P-QDD-IDEMPOTENCE-DOMINATES-FORK-1` are permanently closed:

```text
STOP / PUBLIC PIN TRANSPORT MISMATCH / NO SCIENTIFIC CONCLUSION
formal verifier executions: 0
```

Its public `PREREG.md` blob differed from the independently prepared bytes at
mandatory readback. The old issue, identifier, branch, path and pin are not
amended, repaired, rerun, renamed, force-pushed, or used as evidence. This
successor has a fresh issue, identifier, branch, path, pin and verifier
constants. Its scientific question is unchanged.

## Result exposure and lineage

This is result-exposed, proof-first work. Non-canonical incubation found the
expected affine ceiling and group-free class-idempotence lemma. Its programs,
outputs, transcripts, two fired bookkeeping gates and promotion package are
discovery context only and are excluded from public evidence.

The completed probes

```text
P-QDD-J-CENTRALIZER-TERMINALITY-1
P-QDD-RECORD-COMPLETE-STABILIZER-1
P-QDD-RECORD-NATURALITY-FORK-1
```

are boundary lineage only. Their verifiers are not imported or executed. This
probe reconstructs the public J simplex and every finite control it uses.
Static parsing and syntax compilation are allowed before the pin. Scientific
execution is forbidden.

The written proofs below carry universal statements. The verifier audits exact
finite ingredients and deterministic controls; it does not replace their
quantifiers.

## Field 1: equation

### 1. Public J simplex and positivity

Work over

```text
V=Q^4,
one=(1,1,1,1)^T,
G=I_4-(1/5) one one^T,
D=M_J-I_4,
M_J=[[1,0,-1,1],[0,1,-1,0],[1,0,0,0],[0,1,-1,1]],
u_x=D^x e_0, x in F_5.
```

Then

```text
D^5=I,
D^T G D=G,
sum_x u_x=0,
<u_x,u_y>_G=4/5 if x=y and -1/5 otherwise,
u_2=-one.
```

The leading principal minors of `G` are `4/5,3/5,2/5,1/5`, so `G` is positive
definite, and `G^-1=I_4+one one^T`.

Every permutation `pi in S_5` induces one rational map

```text
rho(pi)u_x=u_(pi(x)).
```

The unique vertex relation is their sum zero, so the map exists. It preserves
the Gram table, hence is G-orthogonal; the representation is faithful. Every
linear automorphism preserving the marked vertex set induces such a
permutation. The complete marked-simplex carrier symmetry is therefore `S_5`,
of order 120.

### 2. Frozen J-affine relabeling group

Define

```text
s(x)=x+1,
m(x)=2x
```

on `F_5`. In this probe, **J-affine relabeling group** means exactly

```text
A_Jaff=<s,m> inside S_5.
```

The theorem target is

```text
A_Jaff=AGL_1(F_5)={x -> b+c x : b in F_5, c in F_5^x},
|A_Jaff|=20.
```

The displayed affine set is closed under composition and inverse, and the two
generators produce it. A nonidentity affine map fixes at most one label,
whereas a transposition fixes exactly three, so no transposition is J-affine.

This is a theorem about the declared generated label action. It does not claim
that every physical apparatus symmetry is J-affine or that autonomous `U`
realizes each affine element in one time step.

### 3. Stabilizers and projectors

For token `k in F_5`, define

```text
S_k={pi in S_5:pi(k)=k},
H_k=S_k intersection A_Jaff.
```

Then

```text
S_k ~= S_4, |S_k|=24,
H_k ~= F_5^x ~= C_4, |H_k|=4,
[S_k:H_k]=6.
```

Before target comparison define

```text
P_k=(1/4) sum_(h in H_k) rho(h),
Q_k=I_4-P_k.
```

Averaging all 24 elements of `S_k` gives the same `P_k`. Its image is the fixed
line `Q u_k`. Thus

```text
P_k^2=P_k=P_k^sharp, rank(P_k)=1,
Q_k^2=Q_k=Q_k^sharp, rank(Q_k)=3,
P_k Q_k=Q_k P_k=0.
```

Write `W_k=Q_kV`. For the affine boundary, let `g_k` be multiplier two about
`k` and put

```text
R_k=(1/4)(I-g_k+g_k^2-g_k^3),
C_k=Q_k-R_k,
J_k=g_k C_k.
```

Then `rank(R_k)=1`, `rank(C_k)=2`, `Q_k=R_k+C_k`, `J_k^2=-C_k`,
`J_k^sharp=-J_k`, and `R_k C_k=C_k R_k=0`.

### 4. Group-free class-idempotence lemma

Let a rational branch map `T` satisfy only

```text
T^sharp T=Q_k,
Q_k T=T.
```

No symmetry or normalizer premise is assumed.

For `v in im(P_k)`,

```text
<Tv,Tv>_G=<v,T^sharp T v>_G=<v,Q_k v>_G=0.
```

Positive definiteness gives `Tv=0`, hence `TP_k=0` and, since `I=P_k+Q_k`,
`T=TQ_k`. Therefore `T` restricts to

```text
O=T|_(W_k):W_k -> W_k.
```

The effect equation gives `O^sharp O=I_(W_k)`, so `O` is an invertible
G-orthogonal automorphism. On `V`, `T=OQ_k` and `T^2=O^2Q_k`.

For `delta in {+1,-1}`, if `T^2=delta T`, restriction gives
`O^2=delta O`. Multiplying by `O^-1` gives `O=delta I_(W_k)`, hence
`T=delta Q_k`. Conversely `+Q_k` obeys `T^2=T` and `-Q_k` obeys `T^2=-T`.
Thus

```text
T^sharp T=Q_k, Q_kT=T, T^2=+-T
iff
T=+Q_k or T=-Q_k.
```

Under registered post-state equality `T ~ -T`, the two algebraic maps are one
physical class. Equivalently `[T]^2=[T]` selects `[Q_k]`. No symmetry group
appears in this implication. This probe tests the condition; it does not derive
class-level idempotence from record writing, `U`, or the counter.

### 5. Frozen controls

Before target comparison the verifier audits:

1. the complete 48-member normalizer
   `N_k={+rho(h)Q_k,-rho(h)Q_k:h in S_k}`;
2. the affine centralizer circle points generated by
   `t in {0,1,-1,1/2,-2,3,1/3,-1/5,7/2}` plus `(-1,0)`, with
   `r=(1-t^2)/(1+t^2)`, `s=2t/(1+t^2)`, and
   `X_k(e,r,s)=eR_k+rC_k+sJ_k`, `e=+-1`;
3. every distinct `rho(h)X_k(e,r,s)` for `h in S_k` and frozen points;
4. a deterministic Cayley sample from a three-element basis of rational
   G-skew, Q-supported maps, coefficients `{-2,-1,0,1,2}^3`,
   `O=(I-A)(I+A)^-1`, `T=Q_k O Q_k`, requiring at least 100 distinct members
   per token.

Every control member must satisfy

```text
T^sharp T=Q_k,
Q_kT=T,
TQ_k=T.
```

Across their union, class-level idempotence may hold only at `+-Q_k`.
Completeness is claimed only for explicitly complete finite families. The
universal theorem rests on the written lemma, not the sample.

Retain exact breakers

```text
T_tau=rho(tau)Q_k,
T_*=R_k-C_k.
```

Here `tau` is a transposition of two HIGH labels. Both have the correct effect
and support, both square to `Q_k`, neither is `+-Q_k`, and both fail
class-level idempotence. The transposition is not J-affine.

### 6. Target comparison, deliberately last

Only after all preceding theorems and controls, compare token `k=2` with

```text
E_low=(1/4) one one^T,
E_high=I_4-E_low.
```

The identity `u_2=-one` gives `P_2=E_low`, `Q_2=E_high`. The class selected
conditionally by class-level idempotence is therefore the Lueder class.

## Field 2: code

Accepted exact files:

```text
probes/P-QDD-IDEMPOTENCE-DOMINATES-FORK-2/verify.py
probes/P-QDD-IDEMPOTENCE-DOMINATES-FORK-2/audit_structure.py
probes/P-QDD-IDEMPOTENCE-DOMINATES-FORK-2/audit_controls_a.py
probes/P-QDD-IDEMPOTENCE-DOMINATES-FORK-2/audit_controls_b.py
probes/P-QDD-IDEMPOTENCE-DOMINATES-FORK-2/exact_matrix.py
probes/P-QDD-IDEMPOTENCE-DOMINATES-FORK-2/qdd_class.py
```

Python standard library, integers and `Fraction` only. No float, `Decimal`,
complex approximation, randomness, network, subprocess, external data,
predecessor import, scratch import, or filesystem write. Zero arguments,
deterministic stdout, empty stderr. All five helper modules are pinned source, not generated data. Target comparison is the final scientific gate.

## Field 3: carrier

```text
system:           (Q^4,G)
labels:           F_5
carrier symmetry: S_5
J-affine group:   AGL_1(F_5)
record group:     S_4 at each token
affine group:     C_4 at each token
moving support:   W_k=Q_kV, dimension 3
post equality:    T ~ -T
```

No external data.

## Field 4: completeness and systematics

No tolerance. Obligations C1-C17 are: authority and target firewall; J simplex;
G positivity; complete S5 representation; complete generated AGL1 group;
fixed-label certificate; 24/4 stabilizers and index; projectors and full-average
agreement; R,C,J table; complete normalizer; circle control; enlarged control;
three-dimensional skew basis; Cayley sample with at least 100 members per
token; all control effects/support and exactly `+-Q_k` idempotents; both exact
breakers; and target comparison last.

Hidden target input, omitted finite member, float, pre-pin execution, changed
threshold, unregistered dependency, unnamed layer lift, or post-pin mutation is
STOP. Runtime limit: 120 seconds for the accepted verifier process. Timeout is
STOP.

## Field 5: decision

```text
IDEMPOTENCE-DOMINATES
  C1-C17 pass; the affine ceiling and group-free lemma survive; all controls
  select exactly [Q_k]; final comparison gives the Lueder class.

RELABELING-F
SELECTION-F
CONTROL-F
TARGET-F
STOP
```

Scientific false routes exit zero with exact findings. STOP exits nonzero and
carries no scientific conclusion. Maximum later rows are

```text
QDD-RELABELING-CEILING [T]
QDD-CLASS-IDEMPOTENCE-SELECTION [T]
```

at restricted L4 scope only. The second may state that the naturality-versus-
gauge fork is unnecessary for the conditional selection proof. It may not say
that class-level idempotence was physically derived.

## Field 6: layer

L4 apparatus/support only. No L5/L6 lift. Apparatus records are not public
`D_clock` records. O1 untouched.

```text
SAMPLING NOT PROVIDED.
```

Global O2 remains open.

## Formal order

1. Commit and push this file and all six accepted Python files together.
2. Read all seven back publicly; record hashes, bytes, line endings and blobs.
3. Execute the pinned verifier exactly once from repository root.
4. Add `EXPECTED.txt`, `RUN.md`, and `RESULT.md` without changing pinned bytes.
5. Open one probe-only PR; require byte identity on x86_64 and aarch64 and
   aggregate `check`.
6. Merge any valid scientific or falsified route without squash or rebase.
7. Canon treatment is a separate sealed fold.
