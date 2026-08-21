# P-QDD-AFFINE-PURE-RECORD-BRIDGE-1 result

Status: `PROVED AND AUDITED IN THE FROZEN CLASS / PUBLIC REPLAY PENDING /
CANON UNCHANGED`

## Decision

```text
PURE-RECORD-BRIDGE-BOUNDARY
```

One formal execution returned zero, wrote empty process stderr, and produced
the exact committed 26-line output with 18/18 gates passing. The accepted
verifier was not run before its public pin and was not rerun after the formal
execution.

## 1. The public global helper already contains a faithful pure record

For `v in Q^4`, let

```text
m(v)=v^T G v,
rho(v)=v v^T G / m(v)                 for v != 0.
```

The cyclotomic trace-pairing calculation proves globally, not only on the
finite balanced carrier,

```text
R_cyc(iota_B0(v)).total_weight = m(v),
R_cyc(iota_B0(v)).density      = rho(v).
```

Indeed `MATRIX_B0(T_w)=v v^T G` for
`T_w(x)=w<x,w>_tr`.

For every nonzero `v`, `rho(v)` is the unique `G`-self-adjoint rank-one
idempotent with image `Q v`, and

```text
v v^T = m(v) rho(v) G^-1.
```

Therefore the exact two-field record

```text
R_pure(v)=(m(v),rho(v))
```

has fibres precisely

```text
v ~ -v.
```

It is exact projective state data together with scale.

## 2. The scalar quadratic channel is not enough

On the frozen HIGH support, the explicit rational reflection

```text
O_*=[[-1,-1,-1],[0,1,0],[0,0,1]]
```

is `H`-orthogonal and commutes with `S=A^sharp A`, but does not commute with
the compressed motor `A`. Its internal commutator has rank two.

Nevertheless, for every support vector `v`,

```text
m(O_* A v)=m(A O_* v).
```

Thus a nonzero internal commutator can be invisible to the complete scalar
quadratic channel.

This result does not consume or claim the active parallel issue 495. If that
separate lane later proves scalar-form uniqueness, the exact consequence will
be that the unique scalar line is still insufficient for commutator
faithfulness.

## 3. The complete pure record reads every internal commutator

For any rational `H`-orthogonal `O`,

```text
R_pure(O A v)=R_pure(A O v) for every v
```

implies that `(AO)^-1(OA)` preserves every rational line. Hence

```text
OA=+AO or OA=-AO.
```

The minus case would make `A` similar to `-A`, impossible because

```text
Tr(A)=-3/4.
```

The rational `H`-orthogonal centralizer of `A` is exactly `{+I_W,-I_W}`.
Consequently

```text
R_pure(O A v)=R_pure(A O v) for every v
iff
Xi_T=0
iff
O=+I_W or O=-I_W.
```

The full pure record is therefore faithful to every nonzero internal
commutator on the common ordered-composition domain.

## 4. The current D_matter domain is too small

The public balanced carrier has 625 vectors and exactly 313 outer-product,
hence pure-record, fibres.

The rational projective support `P(W(Q))` is infinite. The explicit family

```text
v_n=(1,n,0,-1-n)^T, n in Z,
```

contains pairwise distinct sign classes.

No readout factoring through the current 313-element image can be
projectively faithful on all of this support. Therefore the existing finite

```text
D_QDD_direct : K_QDD -> MatterData_QDD
```

is not the complete ordered-composition bridge.

The mathematical map

```text
R_cyc o iota_B0 : Q^4 -> MatterData_QDD
```

does exist globally and is projectively faithful through its total-weight and
density fields. What is absent is public decoder ownership:

```text
a D_matter totality domain containing the L4 source,
a bridge manifest,
exact field ownership on that domain,
and a passed GATE-L4-L1-QDD-PURE-RECORD.
```

Underlying-set compatibility is not a typed bridge.

## 5. Consequence for O2

This probe settles the mathematical field question:

```text
scalar quadratic record: can be blind;
complete pure record: faithful;
global algebraic helper: already exists;
current finite decoder domain: insufficient.
```

It does not yet settle the physical adoption question. Global O2 remains open
until the global pure record receives an independently justified public bridge,
stage ownership, a totality domain, and exact full-record event equality inside
the complete admissible apparatus/decoder class.

Only at the final target comparison,

```text
P=E_low,
Q=E_high.
```

No target effect selected the record or the blind witness.

## Candidate rows

After byte-identical public x86_64 and aarch64 replay, a later separate fold may
register at most:

```text
QDD-AFFINE-SCALAR-COMMUTATOR-BLINDNESS [T]
QDD-PURE-RECORD-CANONICALITY [T]
QDD-PURE-RECORD-COMMUTATOR-FAITHFULNESS [T]
QDD-COMMUTATOR-DMATTER-DOMAIN-BOUNDARY [T]
```

All are restricted to the exact carrier, equality, and L1/L4 scope of this
probe. They do not move `QUADRATIC-DECODER-DATA`, close O2, or assert that
issue 495 has earned a result.

## Evidence boundary

The proposed gate

```text
GATE-L4-L1-QDD-PURE-RECORD
```

is named but not registered or passed. No L5 stream, L6 measure, decoder
completion, SI statement, Bell causal account, Canon or registry change.

O1 is untouched.

```text
SAMPLING NOT PROVIDED
```
