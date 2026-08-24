# P-QDD-IDEMPOTENCE-DOMINATES-FORK-1 preregistration

Date: 2026-08-20

Author of record: A. M. Thorn

Status: preregistered protocol only. No scientific result is earned here. The
accepted verifier has formal execution count zero and may not be imported or
executed before this file and `verify.py` are committed together, pushed, and
read back byte for byte from the public remote.

Public claim lock: issue 479.

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

## Result exposure and lineage

This is result-exposed, proof-first work. Non-canonical incubation previously
found the expected affine ceiling and the group-free class-idempotence lemma.
Those calculations, transcripts, failed bookkeeping gates, programs, and
outputs are discovery context only and are excluded from public evidence.

The completed public probes

```text
P-QDD-J-CENTRALIZER-TERMINALITY-1
P-QDD-RECORD-COMPLETE-STABILIZER-1
P-QDD-RECORD-NATURALITY-FORK-1
```

are boundary lineage. Their verifiers are not imported or executed. This probe
reconstructs the public J simplex and every finite control it uses.

Static parsing and syntax compilation are allowed before the pin. Scientific
execution is forbidden.

The written proofs below carry the universal statements. The verifier audits
their exact finite ingredients and deterministic control families; it does not
replace their quantifiers.

## Field 1: equation

### 1. Public rational J simplex

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

The leading principal minors of `G` are

```text
4/5, 3/5, 2/5, 1/5,
```

so `G` is positive definite. Its inverse is `I_4+one one^T`.

For every permutation `pi in S_5`, the unique rational map

```text
rho(pi) u_x = u_(pi(x))
```

exists because the only relation among the five spanning vertices is their
sum zero. It preserves the complete Gram table and is therefore
`G`-orthogonal. The representation is faithful. Conversely every linear
automorphism preserving the marked vertex set induces a permutation. Thus the
complete marked-simplex carrier symmetry is `S_5`, of order 120.

### 2. Frozen J-affine relabeling group

Define two label maps

```text
s(x)=x+1,
m(x)=2x
```

on `F_5`. The term **J-affine relabeling group** in this probe means exactly

```text
A_Jaff = <s,m> inside S_5.
```

The theorem target is

```text
A_Jaff = AGL_1(F_5)
       = {x -> b+c x : b in F_5, c in F_5^x},
|A_Jaff|=20.
```

Indeed, conjugating and composing translations by the nonzero multipliers
produces every displayed affine map, and the displayed set is closed under
composition and inverse. The verifier performs the complete group generation
and closure audit.

A nonidentity affine map solves

```text
b+c x=x
```

in at most one label, whereas a transposition of five labels fixes exactly
three. Therefore no transposition belongs to `A_Jaff`.

This is a theorem about the declared generated label action. It does not say
that every physical apparatus symmetry must be J-affine, or that the
autonomous update `U` realizes every affine element as one time step.

### 3. Record and affine stabilizers

For every token `k in F_5`, define

```text
S_k = {pi in S_5 : pi(k)=k},
H_k = S_k intersection A_Jaff.
```

Then

```text
S_k ~= S_4, |S_k|=24,
H_k ~= F_5^x ~= C_4, |H_k|=4,
[S_k:H_k]=6.
```

Define, before any target comparison,

```text
P_k = (1/4) sum_(h in H_k) rho(h),
Q_k = I_4-P_k.
```

The same projector is obtained by averaging all 24 elements of `S_k`.
The fixed space is the line `Q u_k`, so

```text
P_k^2=P_k=P_k^sharp, rank(P_k)=1,
Q_k^2=Q_k=Q_k^sharp, rank(Q_k)=3,
P_k Q_k=Q_k P_k=0.
```

Here `A^sharp=G^-1 A^T G`. Write `W_k=Q_k V`.

For the affine boundary, let `g_k` be multiplier two about `k` and put

```text
R_k = (1/4)(I-g_k+g_k^2-g_k^3),
C_k = Q_k-R_k,
J_k = g_k C_k.
```

Then

```text
rank(R_k)=1,
rank(C_k)=2,
Q_k=R_k+C_k,
J_k^2=-C_k,
J_k^sharp=-J_k,
R_k C_k=C_k R_k=0.
```

### 4. Group-free class-idempotence lemma

Let a rational branch map `T` satisfy

```text
T^sharp T = Q_k,
Q_k T = T.
```

No commutation or normalizer premise is assumed.

#### Support completion

For `v in im(P_k)`,

```text
<Tv,Tv>_G
 = <v,T^sharp T v>_G
 = <v,Q_k v>_G
 = 0.
```

Positive definiteness of `G` gives `Tv=0`. Hence

```text
T P_k=0.
```

Since `I=P_k+Q_k`, this also gives

```text
T=TQ_k.
```

Thus `T` restricts to a map

```text
O=T|_(W_k):W_k -> W_k.
```

On `W_k`, the effect equation is

```text
O^sharp O=I_(W_k).
```

Therefore `O` is injective and, in finite dimension, invertible. It is a
`G`-orthogonal automorphism. On all of `V`,

```text
T=O Q_k,
T^2=O^2 Q_k.
```

#### Class-level idempotence

For `delta in {+1,-1}`, suppose

```text
T^2=delta T.
```

Restricting to `W_k` gives

```text
O^2=delta O.
```

Multiplication by `O^-1` yields

```text
O=delta I_(W_k).
```

Therefore

```text
T=delta Q_k.
```

Conversely `+Q_k` satisfies `T^2=T`, and `-Q_k` satisfies `T^2=-T`.

Hence

```text
T^sharp T=Q_k and Q_k T=T and T^2=+-T
iff
T=+Q_k or T=-Q_k.
```

Under the registered post-state equality

```text
T ~_post L iff T=+L or T=-L
```

inside one nonzero effect fibre, the two algebraic members are exactly one
physical class. Equivalently, class-level idempotence

```text
[T]^2=[T]
```

selects `[Q_k]`.

No symmetry group appears in this implication. This probe tests the condition;
it does not derive class-level idempotence from the public record-writing
protocol, `U`, or the counter.

### 5. Frozen finite and sampled controls

The verifier must audit the following target-independent families before the
target comparison.

#### 5a. Complete record normalizer

For every token,

```text
N_k = {+rho(h)Q_k,-rho(h)Q_k : h in S_k}.
```

This is the complete 48-member family exposed by the naturality fork, with 24
classes under sign equality. The verifier exhausts all members.

#### 5b. Affine centralizer circle sample

Freeze

```text
t in {0,1,-1,1/2,-2,3,1/3,-1/5,7/2}
r_t=(1-t^2)/(1+t^2),
s_t=2t/(1+t^2),
```

together with the additional circle point `(-1,0)`. For both
`e in {+1,-1}`, audit

```text
X_k(e,r,s)=e R_k+r C_k+s J_k.
```

Every point has `r^2+s^2=1`.

#### 5c. Enlarged stabilizer-times-circle family

Audit every distinct operator

```text
rho(h) X_k(e,r,s),
h in S_k,
```

for the frozen circle points.

#### 5d. Rational Cayley sample

Construct a deterministic three-element basis of the rational
`G`-skew, `Q_k`-supported endomorphisms. For every coefficient triple in

```text
{-2,-1,0,1,2}^3
```

put

```text
A=c_1 A_1+c_2 A_2+c_3 A_3,
O=(I-A)(I+A)^-1,
T=Q_k O Q_k,
```

whenever the displayed inverse exists. The verifier requires at least 100
distinct sampled operators at every token.

Every member of all four controls must satisfy

```text
T^sharp T=Q_k,
Q_k T=T,
TQ_k=T.
```

Across their union, class-level idempotence may hold only at `+Q_k` and
`-Q_k`. Completeness is claimed only for the explicitly complete finite
normalizer. The universal selection theorem rests on the written lemma, not
on the sample.

Two exact boundary witnesses must be retained:

```text
T_tau=rho(tau)Q_k
```

for a transposition `tau` of two HIGH labels, and

```text
T_*=R_k-C_k.
```

Both have the correct effect and support, both square to `Q_k`, neither is
`+-Q_k`, and therefore both fail class-level idempotence. The transposition is
not J-affine.

### 6. Target comparison, deliberately last

Only after all preceding theorems and controls, compare token `k=2` with

```text
E_low  = (1/4) one one^T,
E_high = I_4-E_low.
```

The simplex identity `u_2=-one` gives

```text
P_2=E_low,
Q_2=E_high.
```

Therefore the single class selected conditionally by class-level idempotence
is the Lueder class.

## Field 2: code

Accepted exact files:

```text
probes/P-QDD-IDEMPOTENCE-DOMINATES-FORK-1/verify.py
probes/P-QDD-IDEMPOTENCE-DOMINATES-FORK-1/exact_matrix.py
probes/P-QDD-IDEMPOTENCE-DOMINATES-FORK-1/qdd_class.py
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

The two helper modules are accepted pinned source, not generated data.
`exact_matrix.py` contains only elementary `Fraction` linear algbra.
`qdd_class.py` contains only the target-independent J-simplex and branch-class
construction. The verifier reconstructs the J simplex, all 120 permutations, the complete
20-element generated affine group, all stabilizers and projectors, the affine
`R,C,J` decomposition, every member of the complete normalizer, the frozen
circle and enlarged controls, and the deterministic Cayley sample. It checks
the target only in its final scientific gate.

The written proof carries the universal class-idempotence lemma. Finite code
cannot replace that quantifier.

## Field 3: carrier

```text
system:          (Q^4,G)
labels:          F_5
carrier symmetry S_5
J-affine group:  <x->x+1,x->2x> = AGL_1(F_5)
record group:    S_4 at each token
affine group:    C_4 at each token
moving support:  W_kkQ_k V, dimension 3
post equality:   T ~ -T
```

No external data.

## Field 4: completeness and systematics

No tolerance. Exact obligations:

```text
C1  authority constants and target-independence source guard;
C2  J phase motor and regular-simplex identities;
C3  exact positivity and inverse of G;
C4  complete 120-member marked-simplex representation and group law;
C5  complete generated 20-member J-affine group;
C6  fixed-label certificate excluding transpositions;
C7  complete 24/4 stabilizers, intersection, and index six;
C8  projector identities, ranks, sharpness, and full-average agreement;
C9  affine R,C,J multiplication table;
C10 complete 48-member normalizer control;
C11 frozen rational-circle control;
C12 enlarged stabilizer-times-circle control;
C13 three-dimensional G-skww support basis;
C14 deterministic Cayley sample, at least 100 distinct members per token;
C15 every control member has the frozen effect and support, and the control
    idempotents are exactly +-Q_k;
C16 both exact nonterminal breakers survive effect/support and fail
    class-level idempotence;
C17 target comparison only after C1-C16.
```

A hidden target input, omitted finite member, float, pre-pin execution, changed
threshold, unregistered external dependency, unnamed layer lift, or post-pin
mutation is STOP.

The runtime limit is 120 seconds for the accepted verifier process on each
formal execution. Timeout is STOP.

## Field 5: decision

```text
IDEMPOTENCE-DOMINATES
  every obligation passes; the affine ceiling and group-free selection lemma
  survive; all controls select exactly the sign class [Q_k]; and the final
  target comparison gives the Lueder class.

RELABELING-F
  the generated group, carrier symmetry, fixed-label certificate, or
  stabilizer-intersection theorem fails.

SELECTION-F
  the written group-free lemma fails, or an exact counterexample satisfies the
  frozen effect, support, and class-idempotence equations outside +-Q_k.

CONTROL-F
  a frozen finite or sampled control violates its effect/support contract,
  omits a required finite subset, or contains an out-of-class idempotent.

TARGET-F
  the final target comparison fails.

STOP
  authority, collision, pin, target independence, exactness, completeness,
  evidence, runtime, security, layer, or deterministic-output discipline fails.
```

No tolerance. `IDEMPOTENCE-DOMINATES`, `RELABELING-F`, `SELECTION-F`,
@CONTROL-F`, and `TARGET-F` are scientific exit-zero routes. `STOP` exits
nonzero and carries no scientific conclusion.

Maximum later candidate rows on `IDEMPOTENCE-DOMINATES`:

```text
QDD-RELABELING-CEILING [T]
QDD-CLASS-IDEMPOTENCE-SELECTION [T]
```

Both are restricted L4 theorems. The second may record that its conditional
selection proof is independent of the strict-naturality versus enlarged-gauge
fork. It may not say that class-level idempotence has been physically derived.

## Field 6: layer

M4T4 