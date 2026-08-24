# P-QDD-COMMUTATOR-SATURATION-CLOSURE-1 preregistration

Date: 2026-08-21

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count zero. No scientific result is earned by this file. The accepted `verify.py` may be parsed and syntax-compiled before the public pin, but it is not imported or executed before this file and `verify.py` are committed together, pushed, and read back byte for byte from the public remote.

Public claim lock: issue 509.

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v59
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v59
CONTENT_COMMIT: 5da6b883defebd8edc470db1e2e7ebde095ef20a
CANON_SHA256:   7fdea700589a21303109dbb6c33fecd2d8243d0d09184ab9d471f0a59687f641
CANON_BYTES:    314310
BASE_COMMIT:    5e077db1a33924bbaaeb8498046605a21e1b0a0d
```

Target: O2 of `QDD-INSTRUMENT-APPARATUS [O]` only.

Layers: L4 apparatus/support and L1 exact read-only record. The decoder completion contract is audited only as a static MULTI type boundary. No L5 or L6 lift.

## Collision and predecessor boundary

Before the claim issue was opened, issue, branch, probe and registry namespaces were searched. No object under this probe identifier or the three proposed theorem identifiers below existed.

Immediate public lineage:

```text
P-QDD-PURE-RECORD-PORT-CANONICAL-1    merged PR 506
P-QDD-PURE-RECORD-TYPED-BRIDGE-1      merged PR 504
P-QDD-AFFINE-PURE-RECORD-BRIDGE-1     merged PR 498
P-QDD-COMMUTATOR-READOUT-FORK-2       merged PR 494
```

The accepted verifier is fresh and imports none of them. Their results are exposure and collision context only. Written proofs below carry the universal statements.

## Field 1: equations and proofs

### A. Target-independent carrier

Let

```text
V = Q^4,
one = (1,1,1,1)^T,
G = I_4-(1/5)one one^T,
G^-1 = I_4+one one^T,
M_J = [[1,0,-1,1],
       [0,1,-1,0],
       [1,0,0,0],
       [0,1,-1,1]],
D_J = M_J-I_4,
u_x = D_J^x e_0.
```

Define `P` before target comparison as the `G`-orthogonal projector onto `Q u_2`, put `Q=I-P`, `W=QV`, and use

```text
w1=(1,0,0,-1)^T,
w2=(0,1,0,-1)^T,
w3=(0,0,1,-1)^T.
```

In this basis

```text
H=[[2,1,1],[1,2,1],[1,1,2]],
A=Q D_J Q|W
 =[[-1,-1,-3/4],[0,0,1/4],[1,0,1/4]],
det(A)=-1/4,
tr(A)=-3/4.
```

Thus `A` is invertible.

### B. Complete repeatable rational pure branch class

Freeze the named class

```text
A_rep(Q)={T in M_4(Q): T^sharp T=Q, QT=TQ=T}.
```

Claim:

```text
A_rep(Q)={OQ: O in O(W,G|W)(Q)}.
```

Proof. If `p` lies in `PV`, then

```text
<Tp,Tp>_G=<p,T^sharp T p>_G=<p,Qp>_G=0.
```

Positive definiteness gives `Tp=0`, hence `TP=0` and `T=TQ`. The frozen two-sided support also gives `QT=T`, so `T` maps `W` to `W`. On `W`, `T^sharp T=Q` becomes `O^sharp O=I_W`. Therefore the restriction `O=T|W` is an injective isometry. Since `W` is finite dimensional, it is an orthogonal automorphism. Conversely every rational orthogonal `O` on `W`, extended by zero on `PV`, gives `T=OQ` and satisfies all three defining equations. This proves completeness of this named rational pure repeatable branch class. It is not a theorem that every possible apparatus architecture belongs to the class.

### C. Canonical read-only post-state port

For nonzero `v in W`, define

```text
m(v)=v^T G v,
rho(v)=v v^T G/m(v),
b_W([v])=(m(v),rho(v)),
[v]=[-v].
```

The density obeys

```text
rho^2=rho,
rho^sharp=rho,
rank rho=1,
tr rho=1,
im rho=Qv,
vv^T=m(v)rho(v)G^-1.
```

Hence

```text
b_W([v])=b_W([w]) iff w=+v or w=-v.
```

This is projective faithfulness at the frozen sign equality. The theorem is proved here from the displayed formula; no predecessor verifier is imported.

### D. Residual commutator and mathematical saturation

For `T=OQ` put

```text
Xi_T=Q[T,D_J]Q=OA-AO.
```

Define `COMM-SAT(T)` only as the mathematical property

```text
b_W([O A v])=b_W([A O v]) for every nonzero v in W.
```

This definition contains no word `terminal`, no target effect and no physical interpretation.

Because `OA` and `AO` are invertible, projective faithfulness implies that `COMM-SAT(T)` makes

```text
C=(AO)^-1(OA)
```

preserve every rational line. In dimension at least two, a linear map preserving every line is scalar, so

```text
OA=lambda AO.
```

Equality of the pure records gives `lambda^2=1`. The case `lambda=-1` would make `A` similar to `-A`, impossible because `tr(A)=-3/4` is nonzero. Therefore

```text
COMM-SAT(T) iff OA=AO iff Xi_T=0.
```

Now solve the rational centralizer. Every `X` with `XA=AX` has the form

```text
X(a,b,c)=
[[c-5a/4,-a-b/4,-3a/4+b/4],
 [-b/4,c-a/4-b/2,a/4-b/4],
 [a,b,c]].
```

For `E=X^T H X-H`, exact subtraction gives

```text
E22-E11=(5/4)b^2.
```

Hence orthogonality forces `b=0`. Then

```text
E11-E33=a(7a-8c)/4,
E12-E13=a(a-4c)/2.
```

If `a!=0`, these demand simultaneously `c=7a/8` and `c=a/4`, contradiction. Thus `a=0`. Finally

```text
E11=2(c^2-1),
```

so `c=+1` or `c=-1`. Therefore

```text
Cent_(O(W,H)(Q))(A)={+I_W,-I_W}.
```

Consequently

```text
COMM-SAT(T)
iff Xi_T=0
iff O=+I_W or O=-I_W
iff T=+Q or T=-Q.
```

Under the registered sign equality this is one physical branch class.

The same class is exactly the projectively idempotent class. If `T^2=delta T`, `delta in {+1,-1}`, then on `W`

```text
O^2=delta O.
```

Invertibility gives `O=delta I_W`. Conversely `+Q` and `-Q` satisfy the two representative equations. Hence

```text
COMM-SAT(T) iff [T]^2=[T].
```

This is a theorem, not a physical adoption of the saturation premise.

### E. Architecture nonimplication

The public decoder text is frozen and audited as text, not inferred from the theorem above. Public Canon v59 states:

1. `D_clock` is terminal in functional order after `D_matter` and `D_geom`;
2. decoder outputs do not feed `U`;
3. totality, uniqueness and completeness of the decoder are not claimed;
4. `DEF-DECODER-COMPLETION-CONTRACT` is a schema, not an existence or completeness theorem;
5. a terminal record `emit_rule_id` is distinct from a write target and does not establish state terminality;
6. maximality and nontriviality are independent optional states;
7. the contract supplies no completion-wide terminality result.

Therefore no current public implication has the form

```text
terminal decoder stage -> COMM-SAT(T)
read-only decoder      -> COMM-SAT(T)
decoder completion schema -> COMM-SAT(T).
```

Any result route claiming that the existing architecture already derives `COMM-SAT(T)` without an additional physical premise fires `ARCHITECTURE-F`. The machine does not assign theorem grade to this text audit; the public source and written comparison do.

### F. Minimal remaining physical dictionary candidate

Public CORE states:

```text
Time is a counter. Space is read through commutators.
```

It also states that physical interpretations are only as strong as registered dictionary rows. Therefore the strongest noncircular candidate remaining after the theorem is explicitly separated as a dictionary proposal:

```text
TERMINAL-EVENT-COMMUTATOR-SATURATION [D candidate]
  a terminal saturated QDD post-event record is read as complete only when the
  canonical post-state port has no residual internal commutator readout,
  equivalently COMM-SAT(T), equivalently Xi_T=0.
```

This is not a theorem and is not adopted by this probe. It adds no target projector, symmetry group, fitted number, hidden apparatus parameter or writeback. If the owner later adopts it in a separate Canon fold at grade D, the theorem in section D selects the single Lueder sign class inside `A_rep(Q)`. O2 may move only at the scope and grade actually earned by that later fold.

### G. Target comparison last

Only after every class and equivalence above is settled,

```text
u_2=-one,
P=(1/4)one one^T=E_low,
Q=I-P=E_high.
```

Thus the unique commutator-saturated HIGH sign class is the Lueder HIGH class at the final comparison. No target effect enters the class, port or saturation definition.

## Field 2: code

Accepted file:

```text
probes/P-QDD-COMMUTATOR-SATURATION-CLOSURE-1/verify.py
```

Python standard library only. Integers and `Fraction` only. No float, complex number, approximation, randomness, network, subprocess, external data, predecessor import, or filesystem read or write. Zero arguments. Deterministic stdout. Empty stderr. Exit nonzero on any failed exact gate.

The verifier audits the carrier, Gram, motor, target-independent support, compressed motor, representative branch equations, pure-record projector and reconstruction identities, sign fibres, centralizer formula and elimination identities, one exact noncentral commutator witness, saturation of the two sign representatives, failure of saturation for the witness, projective idempotence controls, and target comparison last. Universal class completeness, line-preserving, centralizer elimination and architecture nonimplication are carried by written proofs.

## Field 3: carrier

```text
system carrier:       Q^4 with Gram G
repeatable support:   W=QV, dimension 3
branch class:         A_rep(Q)
post equality:        T ~ -T, v ~ -v
compressed motor:     A=Q D_J Q|W
read-only port:       b_W
residual readout:     Xi_T=OA-AO
```

No external data.

## Field 4: systematics

No tolerance and no retry.

```text
terminal functional order read as state fixed point    forbidden
read-only read as no-disturbance theorem               forbidden
completion schema read as maximality                   forbidden
CORE commutator wording promoted to physics theorem    forbidden
dictionary candidate called derived                    forbidden
class completeness widened to every apparatus          forbidden
target effect used before final comparison              forbidden
pre-pin accepted-verifier execution                     STOP
post-pin mutation or threshold move                     STOP
```

Runtime limit: 120 seconds.

## Field 5: decision

```text
SATURATION-DICTIONARY-BOUNDARY
  the named rational pure repeatable branch class is complete; COMM-SAT is
  exactly equivalent to Xi_T=0, to the sign Lueder class and to projective
  idempotence; the present public decoder architecture does not derive
  COMM-SAT; one explicit physical dictionary remains necessary.

SATURATION-DERIVED
  an already registered public implication derives COMM-SAT without adding a
  dictionary, terminality law, maximality principle or target-dependent input.

CLASS-F | PORT-F | CENTRALIZER-F | ARCHITECTURE-F | TARGET-F | STOP
```

A semantic strengthening of the words `terminal` or `complete` is not evidence for `SATURATION-DERIVED`.

Maximum later theorem rows:

```text
QDD-REPEATABLE-PURE-BRANCH-CLASS            [T]
QDD-COMMUTATOR-SATURATION-SELECTION          [T]
QDD-SATURATION-ARCHITECTURE-NONIMPLICATION  [T]
```

A separate owner-approved fold may additionally consider only at dictionary grade:

```text
TERMINAL-EVENT-COMMUTATOR-SATURATION        [D]
```

The D row is not earned merely by this probe.

## Field 6: layer and firewall

L4 apparatus/support and L1 read-only record only. Static MULTI architecture audit, no new lift.

Global O2 remains open under this probe. It can move only through a later independently justified physical adoption or another selector. The theorem does not claim that every physical apparatus architecture is exhausted by `A_rep(Q)`.

O1 is untouched.

```text
SAMPLING NOT PROVIDED.
```

## Formal order

Commit and push `PREREG.md` and `verify.py` together; read both back byte for byte from the public remote; execute the accepted verifier exactly once; add `EXPECTED.txt`, `RUN.md` and `RESULT.md` without changing the pin; one probe-only pull request; byte identity on x86_64 and aarch64; aggregate `check`; merge with a merge commit only. Canon, registry, frontier and dictionary adoption are a separate later fold.
