# Independent artisanal F8 G0/G1 audit

Status: **PASS**.  No construction-formula error or integrity-gate blocker was
found.  This audit deliberately stops before every F8 contraction.

## Lock and sources

- Public lock commit `62c1e877c3817923dca6b922ebd4562f83d2bbea` exists locally with subject
  `notes: preregister golden versus artisanal F8 test`.
- The `PREREG.md` blob at that commit and the audited copy both have SHA-256
  `0ffaca441435003aeb0779160e9fcdbca6c40a25c4ea2acce836ff3eca6e0137`.
- Golden source: 8515 bytes, SHA-256
  `55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae`,
  Git blob SHA-1 `e0d0e171d58b3360c39595d677ffc401a466112d`.
- Gross--Goedicke PDF: 643554 bytes, SHA-256
  `3c423439d89a969235612bc4149069e8bfca349cf1532413ae90f19fdbf0e2be`.
- Gross--Goedicke source archive: 49234 bytes, SHA-256
  `c67eab02dc7960e171eea723aada3554fb2869c8e07ece7ae209132cc33c86d2`.
  It contains exactly `00README.json`, `artisanal.bbl`, and `artisanal.tex`;
  the TeX source is 142990 bytes with SHA-256
  `1408d0bf8d7b404f0d0c0fd6b1ff5fbba8b7f22040d2ae457c81d4e7e71525a2`.

## Golden tensor

An independent strict parser found a 36-by-36 literal with 112 nonzero
entries: 40 labelled `a`, 40 labelled `b`, and 32 labelled `c`.  Phase
exponents range from 0 through 19.

The amplitudes were represented exactly in `Q(zeta_40)` and checked against

```text
c=(zeta^5+zeta^-5)/2
a*(zeta^2+zeta^-2)=c
b=(zeta^4+zeta^-4)*a
```

with conjugation `zeta -> zeta^-1`.  Exact Gram matrices over the cyclotomic
quotient were `I_36` for all three flattenings `ij|kl`, `ik|jl`, and `il|jk`.

## Direct Gross--Goedicke construction

The implementation independently used

```text
delta(i-j,k-l)/6 * sum_p lambda(p,i-j) zeta6^(p(i-k)).
```

The sign and index convention agree with the pinned Bell convention: applying
`Z^p X^q` gives the support `i-j=q`, while a ket/bra projector contributes
the phase `zeta6^(p(i-k))`.  No formula discrepancy was found.

For each of `sym` and `sparse`:

- direct `U_lambda` has 180 nonzero computational-basis entries;
- all three exact Gram matrices are `I_36`;
- all 48 lexicographically enumerated `GL(2,F_3)` transforms deduplicate to
  exactly 24 tables;
- every one of the 24 distinct tables passes both exact autocorrelation
  equations at all 36 shifts;
- the two 24-table orbits are disjoint.

The lift `hat(G)=4G+3I mod 6` was applied through `hat(G)^T`.  It reduces to
`G` modulo 3 and fixes the `(x,y)` coordinates modulo 2, as required.

Representative-table SHA-256 values (36 phase exponents serialized as bytes):

| representative | table SHA-256 | sorted 24-table orbit SHA-256 |
|---|---|---|
| sym | `332027bc9bb6615952760d4f0bb2ca4667bceff2236716f08f7d2da986594a07` | `11588515b3f36c38f701262bc5aeffe60cf84831018e8bf7102886d1f30414a7` |
| sparse | `d0fbc53934108b9e9137d54725fc98deec981fafa34af9ad762fedc351fe3fe4` | `4df3ed9f329290d1676ca69b25c4ccdd061aeb07495af34f1b3d5593c86a63f0` |

## Exact 9+27 audit

The projector onto odd `(p,q)` Bell labels was built independently in the
computational basis over `Q(zeta_6)`, rather than assigned a rank by counting
labels.  Exact Gaussian elimination and matrix products give, for both
representatives:

```text
rank(Pi9)=9
rank(Pi27)=27
Pi9^2=Pi9
Pi27^2=Pi27
Pi9*Pi27=0
[U_lambda,Pi9]=0
```

## Determinism and scope

Two fresh runs produced byte-identical stdout and JSON certificates.

- `gate_audit.py` SHA-256:
  `8752f32687cc370fab46d13517c575a613cd4d8bf11ca479711b66ca3babb18c`
- `certificate.json` SHA-256:
  `67c9493c92129eba274345e5042d6c38738cc53e08172ff95e6d879865384834`
- `stdout.txt` and `stdout_run2.txt` SHA-256:
  `738d55bff802314ff95a581ffc9a1a61a2fbbb34aac2a30fe0b2044c54794be3`

This is only the requested independent G0/G1 audit.  No value of any
degree-(4,4) F8 invariant was computed.
