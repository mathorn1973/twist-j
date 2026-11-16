# Finite fixed-reference H3 record

SPDX-License-Identifier: Apache-2.0

NON-CANONICAL candidate until the separately reviewed public fold accepts it.
Public reservation: [twist-j issue #1986](https://github.com/mathorn1973/twist-j/issues/1986).
The license covers this verifier, its expected output and this documentation.

From the repository root, using Python 3.12 and the standard library:

```sh
python3 reproduce/h3-referenced-record/verify.py
```

A successful run exits zero, writes no stderr, and reproduces
`reproduce/h3-referenced-record/EXPECTED.txt` byte for byte. The accepted
repository reproduction runner must enforce its 120-second verifier limit.
A timeout or runner refusal is STOP: do not increase the limit, substitute
partial output or call the refused execution successful.

This is a source-exposed reproduction of an already known finite result,
not a blind prediction. `EXPECTED.txt` is predeclared from the exact
contract and counts, not output captured by executing this new verifier.
Commit and push the complete verifier, expected output, contract text and
scope; record and freshly verify that immutable prospective pin before the
first scientific execution. A change after that pin requires a separately
identified prospective successor and preserves the original outcome.

The verifier applies native parity-gated matching transport C, ordered site
collision B, and the matching-bit flip to every coordinate. It uses integer
arithmetic for the native ring `Z[X]/Phi_5(X)`, with `j` the image of `X`,
and exact rational arithmetic for the field chart and projectors. Its
first-nonzero field chart A with retained scalar is the representation
chosen for this minimal reproduction. It does not recheck the distinct
primitive integral section C implementation; the optional primitive-section
proof is separate. There are 84 complete forward ticks and 168 inverse
substeps in the complete reverse histories. These counts do not claim an
additional independently implemented engine or 168 full-tick inverses.

## Audited carrier

The complete periodic fields have `nx=8`, `ny in {4,6}`, and four rails
`(r0,r2,CLK,CORR)` per site. For each geometry the verifier builds the three
specified preparations `ABSENT_ROW0`, `PLUS`, and `MINUS`. The absent
preparation is the named row-and-rail-matched control. Full cuts run from
0 through 14 and post-C cuts from 1 through 14. Each full cut has the bit
for its next matching. Each post-C cut retains the bit of its C substep.

All 174 cuts retain their geometry, stage, tick, bit and complete field
factor. The factor divides by the first nonzero coordinate and stores the
divisor as the scalar, with a separate representation for the zero
vector. The verifier reconstructs integral fields and compares forward
and backward lifted substeps against native steps and the complete
recorded histories. It also checks the signed native write and unlock
events and the archive and reference incident transport guards.

At all cuts the global matter and radiation sums, ring quadratic sum and
scalar budget agree with the preparation. Row, rail, row-and-rail and role
accounts exhaust the field and sum to the same complete account. Those
views also agree among the three preparations at full cut 0. The
reference `b=8*rho^4`, where `rho=j^2`, is the funded native coordinate
`CORR(4,ny-1)`. Its singleton role contributes linear `b`, quadratic
`64` and scalar `128` once within total scalar budget `27392`.

The archive is `a=CORR(2,ny-1)`. Both stages of cuts 4 through 13 have
`R=0,+1,-1` in preparation order, with
`R=Tr((rho-rho^2)*(a-b))/30`. At cut 14 the signed values are
`1/6,-1/2` and both signed archive scalar accounts are `163`. The
complete initial fields differ even though the initial archive/reference
pair and listed account views agree. At the boundary the coincident
archive-only ray and scalar account fail to determine the signed reader.
The singleton archive linear account is outside that reduced key.

In both ordered embeddings the verifier checks the anchored projectors
and their inverses for the five distinct archive values, plus the
Frobenius distance identity and bounds for all ten unordered pairs.
The conservative chart bound `P22 >= 1/429` follows from
`|sigma(a)|^2 <= Q`. Since the counted reference accounts for `128` of
`Q`, `|sigma(a)|^2 <= Q-128` and `P22 >= 1/427` also hold.
These inequalities use the complete budget and require no optimality
claim.

The native reference and record assertions end at cut 14. The trace
reader is an external exact mathematical function on the pair. The
evidence concerns this finite funded carrier and its declared
preparations.
