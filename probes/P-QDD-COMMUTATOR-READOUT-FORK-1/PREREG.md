# P-QDD-COMMUTATOR-READOUT-FORK-1 preregistration

Date: 2026-08-21. Author: A. M. Thorn. Public lock: issue 492.
Status: protocol only; formal execution count zero.

## Authority

```text
STATE ACTIVE | CANON Public Canon v59 | AUTHORITY mathorn1973/twist-j main
TAG canon-v59
CONTENT_COMMIT 5da6b883defebd8edc470db1e2e7ebde095ef20a
CANON_SHA256 7fdea700589a21303109dbb6c33fecd2d8243d0d09184ab9d471f0a59687f641
CANON_BYTES 314310
BASE_COMMIT 9d06e5386d2481890eedcb13b0fe02ba1386da0b
```

Target: O2 of `QDD-INSTRUMENT-APPARATUS [O]`, L4 only. O1 untouched.
Owner-forwarded commutant work is result exposure, not evidence. The verifier
is fresh and imports no predecessor or scratch implementation. Static compile
is allowed before the pin; scientific execution is forbidden.

## Equation and proofs

Let

```text
V=Q^4, one=(1,1,1,1)^T, G=I-(1/5)one one^T,
M_J=[[1,0,-1,1],[0,1,-1,0],[1,0,0,0],[0,1,-1,1]], D_J=M_J-I.
```

Put `u_x=D_J^x e_0`. Then `D_J^5=I`, `D_J^T G D_J=G`, and
`u_2=-one`. Define `P` before target comparison as the G-orthogonal projector
onto `Q u_2`, put `Q=I-P`, and `W=QV`.

A supported branch obeys `T^sharp T=Q` and `QT=TQ=T`, hence `T=OQ` with
`O` rational G-orthogonal on `W`. Define

```text
A=QD_JQ|W, Xi_T=Q[T,D_J]Q=OA-AO.
```

In the basis `(1,0,0,-1),(0,1,0,-1),(0,0,1,-1)`:

```text
H=[[2,1,1],[1,2,1],[1,1,2]],
A=[[-1,-1,-3/4],[0,0,1/4],[1,0,1/4]], det A=-1/4, tr A=-3/4.
```

Solving `XA=AX` gives

```text
X(a,b,c)=
[[c-5a/4,-a-b/4,-3a/4+b/4],[-b/4,c-a/4-b/2,a/4-b/4],[a,b,c]].
```

For `E=X^T H X-H`:

```text
E22-E11=(5/4)b^2;
with b=0: E11-E33=a(7a-8c)/4, E12-E13=a(a-4c)/2;
with a=b=0: E11=2(c^2-1).
```

Thus `Cent_(O(W,H))(A)={+I,-I}` and `Xi_T=0` iff `T=+Q` or `T=-Q`.

A readout reads `Xi_T` when its frozen equality distinguishes `OAv` from
`AOv` for some nonzero `v` in one common domain.

Event readout: on `(PV\{0}) disjoint-union (W\{0})`, let `B=LOW` on the first
branch and `B=HIGH` on the second. It is total, nonconstant and complete for
that declared event equality. Since `A,O` are invertible on `W`,
`B(OAv)=HIGH=B(AOv)` for every nonzero `v`. Event completeness is blind.

Quadratic readout: in the fixed W basis let `q(v)=vv^T`, with exact matrix
equality. For nonzero rational vectors, `q(v)=q(w)` iff `w=+v` or `w=-v`.
If `q(OAv)=q(AOv)` for every `v`, the line-preserving scalar lemma gives
`OA=+AO` or `OA=-AO`. The plus case gives `O=+I` or `O=-I`. The minus case
would make `A` similar to `-A`, impossible because `tr A=-3/4`. Hence

```text
q(OAv)=q(AOv) for every v  iff  Xi_T=0  iff  O=+I or O=-I.
```

Therefore a completed readout containing this total quadratic field on the
common ordered-composition domain reads every nonzero internal commutator.
Completeness relative only to the event equality does not.

Public Canon v59 types the decoder on forward U-orbits and separately freezes
history equality, coarse graining, output equalities, domains, field ownership,
bridges, totality domains, dependencies and gates. It supplies no map from W,
OAv or AOv to that orbit domain and no theorem that completion means
projective-state separation. The public universal question is therefore not
yet typed. This is a boundary, not an impossibility theorem for future bridges.

Target comparison is last: `u_2=-one` gives `P=E_low=(1/4)one one^T` and
`Q=E_high`. Thus `Xi_T=0` conditionally selects the Lueder HIGH sign class;
this probe does not derive `Xi_T=0` as a law.

## Code, carrier, gates

Accepted file: `probes/P-QDD-COMMUTATOR-READOUT-FORK-1/verify.py`.
Standard library, integer and Fraction only; no float, approximation, random,
network, subprocess, external data, predecessor import or filesystem write;
zero arguments; deterministic stdout; empty stderr.

Carrier: `(Q^4,G)`, moving support `W`, compressed motor `A`, branch class
`O(W,H)(Q)`, event equality LOW/HIGH, quadratic equality exact `vv^T`,
post-state equality `v~-v`.

No tolerance. Gates: authority; motor and metric; target-independent P,Q;
H,A, determinant and trace; centralizer dimension and formula; three exact
orthogonality eliminations; sign centralizer; event completeness and blindness;
quadratic sign fibre and one noncentral rational reflection; quadratic
detection; target comparison last; static public type boundary. Hidden target,
omitted equality/domain, float, pre-pin execution, post-pin mutation, unnamed
lift, or claiming the public decoder already owns q on this domain is STOP.
Runtime limit 120 seconds.

## Decision and scope

```text
EQUALITY-FORK: event completeness blind; quadratic sign-completeness faithful;
               public common-domain bridge absent.
UNIVERSAL-YES | UNIVERSAL-NO | CENTRALIZER-F | QUADRATIC-F | EVENT-F |
TYPE-F | TARGET-F | STOP
```

Maximum later rows after public two-architecture replay:

```text
QDD-COMMUTATOR-READOUT-EQUALITY-FORK [T]
QDD-QUADRATIC-COMMUTATOR-FAITHFULNESS [T]
```

Neither closes O2 nor moves `QUADRATIC-DECODER-DATA`. No L5, L6, decoder
completion, SI, Bell, Canon, registry, gate, workflow or release change.
`SAMPLING NOT PROVIDED`.

Formal order: pin PREREG and verify together; public byte readback; one formal
run; add EXPECTED, RUN and RESULT; one probe-only PR; x86_64, aarch64 and
aggregate check; merge commit only; Canon treatment separate.
