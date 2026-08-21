# P-QDD-COMMUTATOR-READOUT-FORK-2 result

Status: `PROVED AND AUDITED IN THE FROZEN CLASS / PUBLIC REPLAY PENDING / CANON UNCHANGED`

## Decision

```text
EQUALITY-FORK
```

One formal execution returned zero, wrote empty stderr, and produced the exact
committed 21-line output with 14/14 gates passing. The successor verifier was
not run before its public pin and was not rerun after the formal execution.
Issue 492 remains a separate integrity STOP with no scientific conclusion.

## The equality fork

Let `A=QD_JQ|W` and `Xi_T=OA-AO` for a supported rational branch `T=OQ`.
The exact carrier calculation gives

```text
det(A)=-1/4,
tr(A)=-3/4,
Cent_(O(W,H)(Q))(A)={+I_W,-I_W}.
```

Therefore `Xi_T=0` exactly for the Lueder sign class `T=+Q` or `T=-Q`.

Two readouts with different frozen equalities answer the decoder question in
opposite ways.

### Event-complete readout

The total LOW/HIGH map is nonconstant and a complete quotient for the declared
branch equality. Every nonzero `OAv` and `AOv` remains in the HIGH support, so

```text
B(OAv)=HIGH=B(AOv)
```

for every admissible `O` and every nonzero `v`. It is blind to every internal
commutator, including nonzero ones.

### Quadratic projective readout

For `q(v)=vv^T` with exact matrix equality,

```text
q(v)=q(w) iff w=+v or w=-v.
```

The line-preserving scalar lemma gives

```text
q(OAv)=q(AOv) for every v
  iff OA=+AO or OA=-AO.
```

The plus case reduces through the orthogonal centralizer to `O=+I_W` or
`O=-I_W`. The minus case would make `A` similar to `-A`, impossible because
`tr(A)=-3/4`. Hence

```text
q(OAv)=q(AOv) for every v
  iff Xi_T=0
  iff O=+I_W or O=-I_W.
```

Thus the full quadratic field reads every nonzero internal commutator on the
frozen common ordered-composition domain. Any larger readout retaining that
field with an equality at least as separating inherits the result.

## Public decoder boundary

Public Canon v59 does not define decoder completeness as projective-state
separation. It freezes output equalities, coarse graining, domains, bridges,
field ownership and totality separately. It also supplies no registered bridge
from `W`, `OAv`, or `AOv` to the forward-`U`-orbit decoder domain.

Therefore the unqualified statement

```text
every complete decoder reads every nonzero internal commutator
```

is false when completeness is relative only to event equality, and is not yet
typed for the public full decoder. The exact positive conditional statement is:

```text
a decoder completion containing the total quadratic projective field on the
common ordered-composition domain reads every nonzero Xi_T.
```

Global O2 remains open until that field, or another proved
commutator-separating field, receives an independently typed physical bridge and
ownership in the admissible decoder class. This probe does not derive
`Xi_T=0`, complete the decoder, or move `QUADRATIC-DECODER-DATA`.

## Candidate rows

After byte-identical public x86_64 and aarch64 replay, a later separate fold may
register at most:

```text
QDD-COMMUTATOR-READOUT-EQUALITY-FORK [T]
QDD-QUADRATIC-COMMUTATOR-FAITHFULNESS [T]
```

Both are restricted L4 theorems. O1 is untouched. No L5 stream, L6 measure,
SI statement, Bell causal claim, Canon or registry change.

```text
SAMPLING NOT PROVIDED
```
