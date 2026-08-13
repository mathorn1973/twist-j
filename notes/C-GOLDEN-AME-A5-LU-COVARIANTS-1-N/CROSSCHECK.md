# Independent modular audit — `C-GOLDEN-AME-A5-LU-COVARIANTS-1-N`

Status: **NON-CANONICAL independent frozen-family locator**

## Pin and implementation

- preregistration commit: `8f8bd9a2e364a6e071fadb3efe3eed01dcd209ab`
- preregistration SHA-256: `d13fa55157a3616fd40fcc5c53d50638a0c4ff9edb6299092dae6a5af35be8cc`
- matrix source: pinned external `AME46_ORIGINAL.m`
- source bytes: `8515`
- source SHA-256: `55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae`
- parsed support: `112`

`crosscheck_f41.py` was written independently and imports neither the primary
implementation nor its intermediate results.

## Literal contraction convention

For descriptor `(q,n,pi)`, the program labels every closed wire by
`(ell,r)`.  For `A^(r)`, the index on leg `ell` carries `(ell,r)`.  For
`bar(A)^(s)`, it carries `(ell,pi_ell^-1(s))`.  The two exceptions are

```text
A^(0) on q       -> open row,
bar(A)^(0) on q  -> open column.
```

Thus a shared wire enforces, literally,

```text
x_q^(r)   = y_q^(pi_q(r)),     r=1,...,n-1,
x_ell^(r) = y_ell^(pi_ell(r)), ell!=q, r=0,...,n-1.
```

Factors are contracted componentwise by deterministic tensor products and
traces.  No connectedness filter or diagram quotient is used.

The deterministic ordering is

```text
q, pi_q, then pi_ell for the other legs in increasing ell,
```

with Python's lexicographic ordering of permutation tuples.  This
implementation serializes the open-leg placeholder as an explicit zero,
whereas the primary transcript prints only the domain `{1,...,n-1}`.  Under
that documented serialization, the combined frozen descriptor list has
SHA-256

```text
6603df99e77241aa6835c779d5519d91aa23813d6659f5373cd6d0299f69b708.
```

## Finite-field reduction

At the pinned map `z -> 6 in F_41`, the exact source constants reduce to

```text
z=6, w=36, a=4, b=28, c=12.
```

The multiplicative order of 6 was checked to be exactly 40.  Conjugation
uses the same amplitudes and reverses every `w` exponent, equivalently
`z -> 6^-1=7`.

## Complete census

All diagrams were computed:

| degree | diagrams per leg | total diagrams |
|---:|---:|---:|
| `n=2` | 8 | 32 |
| `n=3` | 432 | 1728 |

Every resulting `6 x 6` matrix is scalar modulo 41.  The unital matrix span
therefore has dimension one on each of the four legs, and every pairwise
commutator vanishes modulo 41.

The scalar distributions are identical on all legs:

| degree | scalar residue | multiplicity per leg |
|---:|---:|---:|
| `n=2` | 11 | 1 |
| `n=2` | 36 | 4 |
| `n=2` | 6 | 3 |
| `n=3` | 27 | 2 |
| `n=3` | 25 | 24 |
| `n=3` | 11 | 106 |
| `n=3` | 36 | 192 |
| `n=3` | 6 | 108 |

The multiplicities sum respectively to 8 and 432 on every leg.

## Independent contraction checks

As a second ordering, seven dispersed `n=3`, leg-zero descriptors with local
indices

```text
0, 1, 7, 31, 107, 215, 431
```

were recomputed by a direct sparse sum.  The direct algorithm enumerates all
`112^3` triples of nonzero `A` entries, derives all closed conjugate indices
from the descriptor, scans the six open-column values, and looks up the three
conjugate support entries.  All 36 entries agree with the tensor-contraction
algorithm for every selected descriptor.  Their scalar residues are

```text
27, 25, 11, 11, 36, 25, 11.
```

The same contraction routine was applied to deterministic dense, unrelated
`A` and `B` tensors over `F_41`.  The selected outputs had 28--30 nonzero
off-diagonal entries, showing that scalarity is not imposed by an accidental
trace or open-index error in the contraction engine.

## Locator verdict

The frozen modular locator does **not fire** through every prescribed
`n<=3` diagram:

```text
no nonzero commutator modulo 41,
no third independent matrix modulo 41.
```

This means exactly `INCONCLUSIVE`, as frozen in the preregistration.  A scalar
reduction modulo one good prime is not evidence that the exact matrices are
scalar, do not prove exact commutativity, and do not provide evidence for an
`A5` action.  In particular, no exact Schur witness can be claimed from this
modular audit.

## Determinism and hashes

Two complete runs produced byte-identical JSON output.  The complete JSON is
stored as deterministic `gzip -n -9` output; decompression has SHA-256
`37c81c9337656551ce0973b6012203ce58b74fba2ad57e6b7e81a42896712c9a`.

```text
crosscheck_f41.py    SHA-256 1dd557f3e3bcbd1d8516df96fe16b98c3b730501eeed6f00d413510170b92be4
CROSSCHECK.json.gz   SHA-256 384e6b73e787ca0b0cb12bdaee4def5ab5f322b959defba331d3d30d98546d47
```
