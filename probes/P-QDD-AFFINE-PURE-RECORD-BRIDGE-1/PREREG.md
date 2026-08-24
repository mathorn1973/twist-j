# P-QDD-AFFINE-PURE-RECORD-BRIDGE-1 preregistration

Date: 2026-08-21

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count zero. No
scientific result is earned here. The accepted `verify.py` may be parsed and
syntax-compiled before the public pin, but it is not imported or executed
before this file and `verify.py` are committed together, pushed, and read back
byte for byte from the public remote.

Public claim lock: issue 497.

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v59
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v59
CONTENT_COMMIT: 5da6b883defebd8edc470db1e2e7ebde095ef20a
CANON_SHA256:   7fdea700589a21303109dbb6c33fecd2d8243d0d09184ab9d471f0a59687f641
CANON_BYTES:    314310
BASE_COMMIT:    2a5601a9ec5cd5c8e24e80f3da78ca6838608fb4
```

Target: O2 of `QDD-INSTRUMENT-APPARATUS [O]` only.

Layers: L1 exact pure-record algebra and L4 apparatus/support. The candidate
cross-layer bridge name is

```text
GATE-L4-L1-QDD-PURE-RECORD
```

This probe may prove the exact map and its equality properties. It does not
register or pass that gate, assign a new totality domain to `D_matter`, or move
a decoder obligation.

## Collision and parallel-lane audit

Before the issue was opened, open and closed issues, pull requests, remote
branches, `probes/`, and the registry were searched. No object under this probe
identifier or the proposed claim identifiers existed.

Issue 495 and `P-AFFINE-QUADRATIC-READING-1` are a separately owned L1 lane on
the same public base. That lane asks whether the affine system uniquely fixes
the invariant scalar quadratic form. This probe does not read its verifier,
claim its output, alter its branch, or depend on an unmerged result. It takes
the already public QDD Gram as frozen data and decides what the scalar and the
complete pure record distinguish. A later fold may compare the two earned
results.

## Result exposure

RESULT-EXPOSED, proof-first. Non-canonical analysis identified the expected
scalar-blind reflection, the global pure-record identity, and the finite-domain
boundary. Those bytes, runs, counts, and implementations are discovery context
only and are excluded from public evidence.

The accepted verifier is a fresh implementation. It imports no predecessor,
parallel-lane, or scratch code. The written proofs below carry universal
statements. The verifier audits exact finite ingredients and witnesses.

## Field 1: equations and proofs

### A. Public carrier and global direct helper

Let

```text
V = Q^4,
one = (1,1,1,1)^T,
G = I_4 - (1/5) one one^T,
G^-1 = I_4 + one one^T.
```

Let `K=Q(zeta_5)` in the public basis

```text
B0 = (1,zeta_5,zeta_5^2,zeta_5^3)
```

and let `iota_B0 : V -> K` be the coordinate isomorphism. The public trace
pairing is

```text
<x,y>_tr = (1/5) Tr_(K/Q)(x sigma_4(y)).
```

Its matrix in `B0` is `G`.

The public definition `DEF-QDD-DIRECT-WRITE` gives a global helper

```text
R_cyc : K -> MatterData_QDD.
```

Only its restriction

```text
D_QDD_direct = R_cyc o iota_B0 o beta_QDD
```

is owned by the current finite quadratic `D_matter` leg.

For `v != 0`, define

```text
m(v)   = v^T G v,
rho(v) = v v^T G / m(v),
R_pure(v) = (m(v),rho(v)).
```

At `v=0`, use the public ZERO record.

For `w=iota_B0(v)`, the rank-one operator

```text
T_w(x) = w <x,w>_tr
```

has matrix

```text
MATRIX_B0(T_w) = v v^T G.
```

Therefore, on every rational vector, the public global helper has fields

```text
R_cyc(w).total_weight = m(v),
R_cyc(w).density      = rho(v).
```

This is a global identity of the public formulas, not an extension inferred
from the finite census.

### B. Canonical pure record for a fixed Gram

For every nonzero `v`:

```text
rho(v)^2 = rho(v),
rho(v)^sharp = rho(v),
rank rho(v) = 1,
im rho(v) = Q v,
Tr rho(v) = 1,
v v^T = m(v) rho(v) G^-1.
```

Uniqueness proof. A `G`-self-adjoint idempotent has kernel equal to the
`G`-orthogonal complement of its image. Hence a rank-one such idempotent with
image `Q v` must send `x` to

```text
v (x^T G v)/(v^T G v),
```

which is exactly `rho(v)`.

The reconstruction identity gives, for all rational `v,w`,

```text
R_pure(v)=R_pure(w)
iff
v v^T = w w^T
iff
w=+v or w=-v.
```

The last equivalence follows by selecting one nonzero coordinate and comparing
one diagonal and the corresponding row of the two outer products. Thus the
two-field pure record is exact projective data plus scale.

### C. Target-independent support and compressed motor

Put

```text
M_J = [[1,0,-1,1],
       [0,1,-1,0],
       [1,0,0,0],
       [0,1,-1,1]],
D_J = M_J-I_4,
u_x = D_J^x e_0.
```

Define `P` before target comparison as the `G`-orthogonal projector onto the
line `Q u_2`, and put

```text
Q = I_4-P,
W = QV.
```

A supported branch satisfies

```text
T^sharp T=Q,
QT=TQ=T,
```

so `T=OQ` with `O` a rational `G`-orthogonal automorphism of `W`.

In the basis

```text
w1=(1,0,0,-1)^T,
w2=(0,1,0,-1)^T,
w3=(0,0,1,-1)^T,
```

the restricted Gram and compressed motor are

```text
H = [[2,1,1],[1,2,1],[1,1,2]],

A = Q D_J Q |_W
  = [[-1,-1,-3/4],
     [ 0, 0, 1/4],
     [ 1, 0, 1/4]].
```

Exactly

```text
det(A)=-1/4,
Tr(A)=-3/4.
```

The internal commutator is

```text
Xi_T = Q[T,D_J]Q = OA-AO.
```

### D. Scalar blindness

Let

```text
S = A^sharp A,

O_* = [[-1,-1,-1],
       [ 0, 1, 0],
       [ 0, 0, 1]].
```

Then

```text
O_*^T H O_* = H,
O_* S = S O_*,
O_* A != A O_*,
rank(O_* A-A O_*)=2.
```

For every `v in W`,

```text
m(O_* A v)=m(A v)
```

by orthogonality, while `O_* S=S O_*` gives

```text
m(A O_* v)=m(A v).
```

Hence

```text
m(O_* A v)=m(A O_* v)
```

for every `v`, although `Xi_* != 0`. The scalar quadratic channel is therefore
not commutator-faithful.

This probe does not claim that the scalar line is unique. That is the separate
question owned by issue 495.

### E. Full pure-record faithfulness

Suppose, for one rational `H`-orthogonal `O`,

```text
R_pure(O A v)=R_pure(A O v)
```

for every `v in W`. Pure-record reconstruction gives

```text
(O A v)(O A v)^T = (A O v)(A O v)^T.
```

Since `OA` and `AO` are invertible, the sign-fibre lemma implies that

```text
(AO)^-1(OA)
```

preserves every rational line. A linear map on a space of dimension at least
two that preserves every line is scalar, so

```text
OA = lambda AO,
lambda in {+1,-1}.
```

If `lambda=-1`, then `O A O^-1=-A`, making `A` similar to `-A`. This is
impossible because `Tr(A)=-3/4` is nonzero.

Thus `OA=AO`. Solving `XA=AX` gives

```text
X(a,b,c)=
[[c-5a/4,-a-b/4,-3a/4+b/4],
 [-b/4,c-a/4-b/2,a/4-b/4],
 [a,b,c]].
```

For `E=X^T H X-H`:

```text
E22-E11=(5/4)b^2;

with b=0:
E11-E33=a(7a-8c)/4,
E12-E13=a(a-4c)/2;

with a=b=0:
E11=2(c^2-1).
```

Therefore the rational `H`-orthogonal centralizer is exactly

```text
{+I_W,-I_W}.
```

We have proved

```text
R_pure(O A v)=R_pure(A O v) for every v
iff
Xi_T=0
iff
O=+I_W or O=-I_W.
```

The complete pure record reads every nonzero internal commutator on this common
ordered-composition domain.

### F. Current finite-domain boundary

The public balanced carrier is

```text
V_eff = {0,1,2,-2,-1}^4,
|V_eff|=625.
```

Its outer-product fibres, and therefore its pure-record fibres, number exactly

```text
313.
```

This is the existing finite quadratic image.

The rational projective support `P(W(Q))` is infinite. For example,

```text
v_n=(1,n,0,-1-n)^T, n in Z,
```

lies in `W`, and no two members are equal up to sign.

Therefore no readout factoring through the current 313-element image can be
projectively faithful on all of `W(Q)`. The current finite map

```text
D_QDD_direct : K_QDD -> MatterData_QDD
```

cannot be the full ordered-composition bridge.

The algebraic map

```text
R_cyc o iota_B0 : Q^4 -> MatterData_QDD
```

is globally defined and projectively faithful through its total-weight and
density fields. Public Canon v59 does not assign this global domain to
`D_matter`, does not own the L4 ordered-composition source, and contains no
bridge manifest or passed gate under
`GATE-L4-L1-QDD-PURE-RECORD`.

Thus the mathematical map exists, while decoder-stage ownership and the
cross-layer bridge remain open.

### G. Target comparison last

Only after all classifications:

```text
u_2=-one,
P=(1/4)one one^T=E_low,
Q=I_4-P=E_high.
```

No target effect is used to define the record, the scalar-blind witness, or the
finite-domain boundary.

## Field 2: code

Accepted file:

```text
probes/P-QDD-AFFINE-PURE-RECORD-BRIDGE-1/verify.py
```

Python standard library only. Integers and `Fraction` only. `Q(zeta_5)` is
implemented by four rational coefficients modulo `Phi_5`. No float, complex
number, approximation, randomness, network, subprocess, external data,
predecessor import, parallel-lane import, or filesystem read or write. Zero
arguments. Deterministic stdout. Empty stderr. Exit nonzero on any failed gate.

The verifier audits:

1. authority constants and the target-independent motor construction;
2. the cyclotomic trace-pairing Gram and global rank-one operator identity;
3. pure-record projector and reconstruction identities on all 625 balanced
   vectors and additional rational controls;
4. the exact 313 fibre count;
5. the scalar-blind reflection and nonzero commutator;
6. the sign-fibre lemma on a frozen finite control grid;
7. the centralizer formula and elimination identities;
8. a full-record separating witness;
9. a frozen set of distinct rational support rays;
10. target comparison last.

The universal uniqueness, line-preserving, and infinity arguments are the
written proofs above. The machine is their audit, not their replacement.

## Field 3: carrier

```text
source carrier:          Q^4 with Gram G
amplitude carrier:       Q(zeta_5) in B0
L4 support:              W=E_high V, defined target-independently first
scalar record:           m(v)
complete pure record:    (m(v),rho(v))
finite public domain:    V_eff, 625 vectors, 313 sign fibres
global algebraic domain: Q^4
post-state equality:     v ~ -v
```

No external data.

## Field 4: systematics

No tolerance and no retry.

```text
parallel issue 495 result imported              forbidden
scalar equality read as full-record equality    forbidden
finite V_eff result widened to Q^4               forbidden
global R_cyc helper read as D_matter ownership  forbidden
underlying-set identity read as layer bridge    forbidden
target effects used before final comparison      forbidden
pre-pin verifier execution                       STOP
post-pin mutation or threshold change            STOP
```

Runtime limit: 120 seconds.

## Field 5: decision

```text
PURE-RECORD-BRIDGE-BOUNDARY
  the global direct-helper identity passes; the scalar channel has an exact
  nonzero blind commutator; the complete pure record is canonical for fixed G
  and commutator-faithful; the finite public D_matter image is insufficient;
  the global algebraic map exists but stage ownership and the named bridge gate
  are not public.

SCALAR-FAITHFUL
PURE-RECORD-F
FINITE-DOMAIN-SUFFICIENT
CENTRALIZER-F
TARGET-F
STOP
```

Scientific negative routes exit zero with exact witnesses. Integrity STOP exits
nonzero and carries no scientific conclusion.

Maximum later rows:

```text
QDD-AFFINE-SCALAR-COMMUTATOR-BLINDNESS [T]
QDD-PURE-RECORD-CANONICALITY [T]
QDD-PURE-RECORD-COMMUTATOR-FAITHFULNESS [T]
QDD-COMMUTATOR-DMATTER-DOMAIN-BOUNDARY [T]
```

All are limited to this exact carrier, record equality, and L1/L4 scope.

## Field 6: layer

L1 exact record algebra and L4 apparatus/support. The proposed bridge gate is
named but not registered or passed. No L5 stream or L6 measure.

Global O2 remains open until a separately justified public bridge, stage
ownership, totality domain, and exact full-record event equality are adopted in
the complete admissible class. O1 is untouched.

```text
SAMPLING NOT PROVIDED.
```

## Formal order

1. Commit and push `PREREG.md` and `verify.py` together.
2. Read both back byte for byte from the public remote.
3. Execute the accepted verifier exactly once under the frozen environment.
4. Add `EXPECTED.txt`, `RUN.md`, and `RESULT.md` without changing pin bytes.
5. Open one probe-only pull request.
6. Require byte-identical x86_64 and aarch64 replay and aggregate `check`.
7. Security-review named files and merge with a merge commit only.
8. Canon and registry treatment is a separate later fold.
