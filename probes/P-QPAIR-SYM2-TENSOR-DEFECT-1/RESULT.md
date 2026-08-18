# P-QPAIR-SYM2-TENSOR-DEFECT-1 result

Date: 2026-08-18. Preregistration pinned at commit
`a991b70a590bc42aed9cc04ade1bc5836ee58f63` before every accepted formal run.

## Verdict

```text
QPAIR-PRODUCT-COMPOSITION       proposed [T]   29/29 exact audit gates PASS
QPAIR-CROSS-SECTOR-NONDESCENT  proposed [T]   written proof and zeta_5 witness PASS
QPAIR-SYM2-TENSOR-DEFECT       proposed [T]   written proof and 10=9+1 audit PASS
QUADRATIC-DECODER-DATA         [O] / STOP, unchanged
```

The matched componentwise law is natural, associative, symmetric, unital,
and exact on product vectors. The reciprocal factorization gauge leaves
`HH` and `SS` invariant but gives `HS` and `SH` the nontrivial weights
`c(lambda)/lambda` and `lambda/c(lambda)`; the exact
`lambda=zeta_5` witness proves that the cross sectors do not descend to
functions of the composite pure tensor.

For `char(K) != 2` and `dim V=dim W=2`, the written proof establishes

```text
Sym^2(V tensor W)
  = Sym^2(V) tensor Sym^2(W)  direct-sum  Lambda^2(V) tensor Lambda^2(W),
10 = 9 + 1.
```

Product squares span exactly the nine-dimensional first summand. With the
frozen wedge convention, the missing projection is
`(ad-bc) kappa/2` and carries character `det(g)det(h)`.

## Evidence

```text
PREREG.md    sha256 6d5e1a5509e10f558dbdac2881f2f0925b9169397a6de38b7e73bb3366086d9b  17947 B
verify.py    sha256 ccb252f1b2307811ec81e79e7d245a9bd78694965f2d975b8336411c7cca1234  19260 B
EXPECTED.txt sha256 dd4774ed6ad065c19baa7efcb556a4d071d71d68a42e0203dff2c1722bdb16d1   2329 B
```

The accepted local leg ran twice from a fresh detached public worktree at the
pin on Ubuntu 24.04.3 LTS, x86_64, CPython 3.12.13, with deterministic
environment, exit zero, empty stderr, and byte-identical stdout.

## Scope firewall

The one-dimensional line is a determinant/concurrence direction in the
quadratic symmetric target. It is not a Bell state, not the ordinary
two-qubit singlet, and not a claim that the full Hermitian-plus-symmetric
entanglement defect has dimension one. Bell states are input vectors whose
squares have maximal determinant projection after a complex norm is supplied.

The result asserts product-state composition, not surjectivity onto all
entangled squares. It creates no `BELL-CAUSAL-ACCOUNTING` row, no dependency
to `QUADRATIC-DECODER-DATA [O]`, no bridge to rational `V_eff`, and no
decoder, observable, Born rule, instrument, L5 stream, L6 measure, or status
move.
