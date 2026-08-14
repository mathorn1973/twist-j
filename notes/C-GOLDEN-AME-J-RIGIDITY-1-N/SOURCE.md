# Frozen sources and prior certificates

Status: **NON-CANONICAL input record**
Incubation: `C-GOLDEN-AME-J-RIGIDITY-1-N`
Public lock: [issue #369](https://github.com/mathorn1973/twist-j/issues/369)

`SOURCE_PINS.json` is the machine-readable authority.  This file is its
human-readable companion.

## Public Canon authority

| Field | Frozen value |
|---|---|
| Repository | `https://github.com/mathorn1973/twist-j.git` |
| Canon | Public Canon v46 |
| Activation commit | `6545c1d0de61ff4696eb3de1a258139e8891f436` |
| Content commit | `62628ca4da2d938e4e3a122d35c0d93a6debc27f` |
| `canon/CANON.md` bytes | `222760` |
| `canon/CANON.md` SHA-256 | `6c57e714c441bd679b9f6c673352cfae44ac993433d7c4624cd9c3c93df291ff` |

No Canon definition supplies the parametric rigidity result.  Canon is
authority and comparison context only.

## Upstream golden tensor

Repository: [`matrix-toolbox/AME_4_6`](https://github.com/matrix-toolbox/AME_4_6)
Commit: `1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8`
License: MIT

| File | Role | Bytes | SHA-256 | Git blob SHA-1 |
|---|---|---:|---|---|
| `AME46_ORIGINAL.m` | sole tensor-value authority | 8515 | `55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae` | `e0d0e171d58b3360c39595d677ffc401a466112d` |
| `block944.m` | auxiliary nine-block permutation provenance for independent construction B | 8234 | `af0aac863f54beb2c8396368fd87102e75192a38ec77efee0605210123540649` | `caab29cb76e60e3165abf70931cf35e387b6e3b1` |

The files are not vendored in this package.  Recover them from the exact
commit and reject them before parsing unless byte count, SHA-256, and Git blob
all match.

The raw constructor reads only the two `36 x 36` literals in
`AME46_ORIGINAL.m`.  It treats `a,b,c,w` as opaque names and must not evaluate
their definitions.  Every exponent is retained as the literal printed
integer; it is not a residue modulo 20.

`block944.m` fixes the provenance and orientation of two permutations used by
the independent nine-block reconstruction.  It does not add a target
equation, local factorization, or alternative tensor representative.

## Frozen structural readback

The permitted pre-lock builders established, without solving the target
system:

- support `112 = 40 a + 40 b + 32 c`;
- active exponent range `0..19` as literal integers;
- nine block counts `12,14,14,8,16,8,14,14,12`;
- exact token equality of the direct and nine-block constructions;
- 3,889 row-Gram-plus-`xy-1` coordinate records;
- 383 nonzero coordinate records including `xy-1` (without quotienting
  duplicate nonzero records);
- serialization length 136262 bytes; and
- serialization SHA-256
  `09aac23466680ba762e363ad75845aa1535f4e8e32cee75ad41119f43cb16762`.

The serialization order is `01` row-major, `02` row-major, `03` row-major,
then `xy-1`.  Column Grams are mandatory redundant audits and are not target
generators.

No target Gröbner basis, saturation, radical, elimination, target factor,
positive branch, or expected relation was computed to obtain these facts.

## Prior independent public replay

Commit
[`c5da90c091995e398f2379c9437234754d4e3d3a`](https://github.com/mathorn1973/twist-j/commit/c5da90c091995e398f2379c9437234754d4e3d3a)
records an independent review and x86_64/aarch64 byte-identical runs for the
earlier golden AME source/field/support work.

Its relevant certificate hashes are:

```text
CERT-G0-G1-INDEPENDENT.txt  5afb8eb1c188536de7de175eec3fe1340ea47fa449471540d67f5f6a3c3c1f7d
CERT-G3-G4-REVIEW.txt       48f469f53ffc3803647b0708a590954f356f8f991dbfff4262343d1e533755f9
```

This independently confirms the known source pin, support, exact three-way
unitarity, and minimal entry field of the published specialization.  It is
not evidence that the new parametric ideal is rigid.

## Publication provenance

- S. A. Rather et al.,
  [*Thirty-six entangled officers of Euler: Quantum solution to a classically
  impossible problem*](https://arxiv.org/abs/2104.05122v2),
  arXiv:2104.05122v2; construction provenance.
- K. Zyczkowski et al.,
  [*9 x 4 = 6 x 6: Understanding the quantum solution to the Euler's problem
  of 36 officers*](https://arxiv.org/abs/2204.06800v2),
  arXiv:2204.06800v2; nine-groups-of-four explanatory provenance.

The papers are human provenance, not machine input to the raw ideal.
