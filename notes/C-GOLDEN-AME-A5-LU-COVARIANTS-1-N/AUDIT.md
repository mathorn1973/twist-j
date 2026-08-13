# Audit of the frozen `n <= 3` covariant family

## Result

All 8 `n=2` and all 432 `n=3` diagrams on each of the four legs reduce to
scalar matrices.  Therefore no commutator or three-dimensional algebra
witness exists in the preregistered family.  The mandated verdict is
`INCONCLUSIVE`.

This survival is automatic for every four-party 2-unitary tensor; it is not
special evidence for an `A5` action on the golden AME tensor.

## Exact cancellation argument

Represent a balanced contraction with `n` copies of `A` and `n` copies of
`bar(A)` by its bipartite multigraph.  Its left and right vertices are the
copies of `A` and `bar(A)`.  Every closed wire is an edge, colored by its
tensor leg.  There are

```text
3n + (n-1) = 4n-1
```

closed edges: three legs give perfect matchings of size `n`, while the open
leg gives a matching of size `n-1` and leaves one open half-edge on each side.

For `n=2`, `4n-1=7>2^2`; for `n=3`, `4n-1=11>3^2`.  Hence two vertices of
opposite bipartition share at least two edges.  Choose two such wires.  Exact
2-unitarity of `A` for that two-versus-two bipartition gives

```text
sum_(two shared indices) A[...,r,s,...] bar(A)[...,r,s,...]
    = product of two Kronecker deltas.
```

The two vertices can therefore be removed.  The deltas splice their two
remaining wires; a remaining wire shared by the removed pair instead gives a
closed dimension factor.  The result is a scalar multiple of the same type
of balanced graph with one fewer pair of tensor vertices.  If an open vertex
was removed, the delta simply transports that open half-edge to the adjacent
remaining vertex.  If both open vertices were removed, one delta is
`delta(i,j)` directly.  Relabeling the identical copies is harmless.

Induction reduces every frozen `n=2` or `n=3` diagram to the `n=1` network,
which is a scalar multiple of `I_6`.  The first value not covered by this
pigeonhole argument is `n=4`, where `4n-1=15 <= 16=n^2`.

## Machine audit

`verify_a5lu_covariants.py` enumerates the raw frozen ordering without a
connectedness filter:

```text
n=2:   8 per leg,   32 total
n=3: 432 per leg, 1728 total
```

The diagram-list SHA-256 is
`eb08b19c49afaaeaec0c8720be2d25e71e0c527defa0363a9ab86b88bd7433f1`.
The reduction is the frozen exact map `zeta_40 -> 6 in F_41`; conjugation is
`6 -> 7`.  Dense signed-int64 contraction is exact because every intermediate
entry is bounded by

```text
40^6 6^11 = 1486016741376000000 < 2^63-1.
```

All 1760 matrices are scalar.  Their ordered transcript SHA-256 is
`2fa27b3a510c696179c9a6b391811e70d2220fe5868f0928f220eb1ad6a78628`.
An independent sparse ordering agrees on all 32 `n=2` diagrams.  A generic
prime-field tensor transformed by four deterministic nonmonomial orthogonal
matrices passes the covariance equation on all 1760 orientations; its audit
hash is `4c3c2749e9cc35fb4f6528eea4ec8f78611e3a79e409b80ed46f5fb9c1476433`.

No zero modulo 41 is promoted to an exact nonvanishing or vanishing claim;
the exact scalarity conclusion comes from the 2-unitary cancellation proof.
