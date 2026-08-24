# P-QDD-RECORD-MONOID-DESCENT-2 preregistration

Date: 2026-08-21

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count zero. Public claim
lock: issue 490.

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v59
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v59
CONTENT_COMMIT: 5da6b883defebd8edc470db1e2e7ebde095ef20a
CANON_SHA256:   7fdea700589a21303109dbb6c33fecd2d8243d0d09184ab9d471f0a59687f641
CANON_BYTES:    314310
BASE_COMMIT:    7820173bdf035fa8b59e40113fdad3ac3c66f12a
```

Target: O2 of `QDD-INSTRUMENT-APPARATUS [O]`, L4 apparatus/support only.
The protocol count below has the same free-monoid shape as the public counter,
but is not identified with `D_clock`. No layer lift. O1 untouched.

## Mandatory predecessor STOP

Issue 489 and `P-QDD-RECORD-MONOID-DESCENT-1` are permanently closed with

```text
STOP / PREREG PUBLIC-BLOB MISMATCH / NO SCIENTIFIC CONCLUSION
formal executions: 0
```

Its issue, identifier, branch, path, pin and files are not repaired, rerun,
renamed or used as evidence. This successor has fresh names and source
constants. The scientific question and thresholds are unchanged.

## Result exposure

Non-canonical dry work exposed the expected theorem and witnesses. Those bytes,
runs and outputs are discovery context only. The accepted verifier is a fresh
five-label sum-zero implementation and is not executed before this file and
`verify.py` are committed together, pushed and read back byte for byte. Static
parsing is allowed. Written proofs carry universal statements.

## Field 1: equation

### A. Readback is not reinteraction

Freeze two types:

```text
same-record readback:
  re-read one immutable record; no fresh coupling and no composition by T;

fresh apparatus repetition:
  prepare a new pointer/record cell and apply the HIGH branch map T again.
```

Public Canon v59 makes the decoder read-only and gives no registered map from
`ObservableHistory` to an L4 post-state endomorphism. This is a static basis
boundary, not an impossibility theorem for future bridges.

### B. Free count and saturated symbol

Let

```text
M=(N_0,+,0),
B=({0,H},OR,0),
H OR H=H,
sat(0)=0, sat(n)=H for n>=1.
```

Append-only histories are words `H^n` and retain multiplicity:

```text
H^m H^n=H^(m+n),
1+1=2 != 1,
H != HH.
```

`sat` is a surjective monoid homomorphism because
`sat(m+n)=sat(m) OR sat(n)`. It is an extra quotient, not a consequence of
append-only persistence.

### C. Saturation-descent theorem

Let `P,Q` be complementary `G`-orthogonal projectors on a positive-definite
rational carrier and let

```text
T^sharp T=Q,
QT=TQ=T.
```

On `W=QV`, `T` is an invertible `G`-orthogonal map. Modulo the registered sign
equality, define

```text
a_T(n)=[T^n], T^0=Q.
```

Then

```text
a_T factors through sat
iff
[T]^2=[T]
iff
[T]=[Q].
```

Proof. Factorization identifies `sat(1)=sat(2)`, hence `[T]=[T^2]`.
Conversely this equality makes every positive power equal to `[T]`. The image
of `H` is then an idempotent in the supported projective group; the only group
idempotent is the identity, since `g^2=g` and multiplication by `g^-1` gives
`g=1`. Thus `T=+Q` or `T=-Q`.

### D. Same-record conditioning theorem

For any event `E`, exact restriction obeys

```text
C_E(A)=A intersection E,
C_E(C_E(A))=C_E(A).
```

Re-conditioning on one immutable event is idempotent. This does not identify
physical post-state dynamics with conditioning; that identification requires a
new typed bridge.

### E. Target-independent J-simplex witnesses

Use

```text
V_5={x in Q^5:sum x_i=0},
S=I_5-(1/5)11^T,
u_x=e_x-(1/5)1,
P_k=(5/4)u_k u_k^T,
Q_k=S-P_k.
```

For `g_k:x -> k+2(x-k)`, put

```text
R_k=(1/4)(I-g_k+g_k^2-g_k^3),
C_k=Q_k-R_k,
J_k=g_k C_k.
```

Exactly:

```text
rank(P,Q,R,C)=(1,3,1,2),
Q=R+C, RC=CR=0, J^2=-C, J^T=-J.
```

Freeze

```text
T_star=R-C,
T_inf=R+(3/5)C+(4/5)J.
```

Both satisfy `T^T T=Q` and `QT=TQ=T`.

For `T_star`, `T_star^2=Q` but `T_star!=+/-Q`; mixed R/C rays alternate with
period two under one terminal HIGH symbol.

For `T_inf`, the C-plane phase is `lambda=(3+4i)/5`, with norm one and
`lambda+lambda^-1=6/5`. If it were a root of unity, this rational sum would be
an algebraic integer and therefore an integer, contradiction. The R component
precludes projective sign minus. Hence `T_inf` has infinite projective order.
One terminal HIGH symbol is compatible with infinitely many post-state classes
under fresh repetition.

### F. Target comparison last

Only at the end reconstruct the public four-coordinate J basis. At token 2,
`u_2=-one` gives

```text
P_2=E_low=(1/4)11^T,
Q_2=E_high=I-E_low.
```

Saturation descent therefore conditionally selects the Lueder sign class.

## Field 2: code

Accepted file:

```text
probes/P-QDD-RECORD-MONOID-DESCENT-2/verify.py
```

Standard library, integers and Fraction only. No float, approximation,
randomness, network, subprocess, external data, predecessor or scratch import,
or filesystem write. Zero arguments, deterministic stdout, empty stderr. The
verifier audits all subsets of `F_5`, all five tokens, both witnesses, an exact
initial power range, descent controls for `+Q,-Q,T_star,T_inf`, and target last.

## Field 3: carrier

```text
protocol monoid:       (N_0,+)
terminal quotient:     ({0,H},OR)
system carrier:        sum-zero Q^5
moving support:        Q_k V_5, dimension 3
post equality:         T ~ -T
finite breaker:        T_star
infinite breaker:      T_inf
```

No external data.

## Field 4: completeness

No tolerance. Obligations: free monoid and word law; Boolean quotient and
homomorphism; universal descent proof; group-idempotent reduction; conditioning
idempotence; simplex and R,C,J algebra at every token; finite and infinite
breakers; descent controls; readback/reinteraction type boundary; target last;
O1, sampling, decoder and layer firewalls. Runtime limit 120 seconds.

Hidden target input, omitted token, float, pre-pin execution, post-pin mutation,
unnamed lift, or claiming conditioning is already physical dynamics is STOP.

## Field 5: decision

```text
RECORD-MONOID-NONDESCENT
  every obligation passes; conditioning is idempotent; fresh repetition acts
  through the free monoid; descent through the saturated symbol is equivalent
  to projective idempotence and conditionally selects Lueder; both exact
  breakers show that HIGH alone does not force descent; no public bridge does.

SATURATION-DERIVED
  one already registered complete typed bridge independly derives the
  quotient for fresh repetitions without assuming idempotence.

MONOID-F | WITNESS-F | TYPE-BOUNDARY-F | TARGET-F | STOP
```

Scientific routes exit zero. STOP exits nonzero and carries no scientific
conclusion.

Maximum later rows:

```text
QDD-RECORD-SATURATION-DESCENT [T]
QDD-READBACK-REINTERACTION-SEPARATION [T]
QDD-HIGH-REPETITION-ORBIT [T]
```

O2 remains open until a separately typed physical bridge derives saturation or
identifies post-state update with same-record conditioning.

## Field 6: layer

L4 only; no L5/L6 lift; O1 untouched.

```text
SAMPLING NOT PROVIDED.
```

## Formal order

Commit and push `PREREG.md` and `verify.py` together; public byte readback;
one formal run; add `EXPECTED.txt`, `RUN.md`, `RESULT.md` without changing pin;
one probe-only PR; byte identity on x86_64 and aarch64; aggregate `check`; merge
with a merge commit only; Canon treatment separate.
