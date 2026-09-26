# PREREG: C-PHOTON-POLYMER-TREE-ACTIVITY-N

**PUBLIC, NON-CANONICAL. No Canon authority.**
Author: A. M. Thorn <thorn@twistj.com>
Date: 26 September 2026
License: Apache-2.0
Owner issue: #1168
Branch: `notes/photon-polymer-tree-20260926`

## 1. Public basis and dependencies

Public Canon v92 is the only authority.

- activation commit and tag target:
  `8b1132d828d94f83e653dab34d686a7e68394939`
- content commit:
  `d7eb6de16c11f6a105996de02ffd7afa32683a93`
- Canon SHA-256:
  `31783fcd8e5ad2a697efd92a6d9fb92c2a21c101b95b9c282ea50fa7cb245f68`
- Canon bytes: `797365`

Non-canonical mathematical inputs only:

1. `notes/C-PHOTON-BCHI-DIRECT-BOUND-N/NEUTRAL-SUM.md` on public main,
   specifically the exact deletion identity and the face-simple cube-chain
   boundary count.
2. Draft PR #1167 at head
   `92559ba3056c6dddba4377b695ad5b130f47818d`, only as motivation for
   replacing worst-case conditional thinning by an unconditional activity
   estimate. No #1167 statement is treated as Canon.

No file under `canon/`, `probes/`, `tools/`, `.github/`, or any
existing photon note directory is changed by this item.

## 2. One scoped question

Work on the periodic four-dimensional cubical complex, but the counting object
below is local and is represented in `Z^4`.

A **face-simple cube tree** is a finite set of distinct elementary 3-cubes such
that:

- two cubes are adjacent iff they share one plaquette;
- the face-intersection graph is exactly a tree;
- every shared plaquette is one tree edge;
- no plaquette belongs to more than two selected cubes.

Orient one root cube. Propagate orientations uniquely across tree edges so the
shared plaquette cancels. For `k` cubes the resulting boundary is a ternary
integer-closed two-chain with exactly

`
A(k)=6k-2(k-1)=4k+2
`

occupied plaquettes.

The exact deletion identity already proved in `NEUTRAL-SUM.md` therefore
gives, for each such deterministic boundary and its global reversal,

`
mu_L(boundary or -boundary) <= 2^(1-A(k))
                            = (1/2) 16^(-k).
`

The question is whether the **absolute union activity of all such rooted tree
boundaries** has an exponentially summable tail after all geometric branching
is counted.

This is L6 finite-measure mathematics. It is not a coverage theorem for all
neutral surfaces.

## 3. Frozen local child graphs

Fix the root elementary cube `c_012(0)`.

Each of its six plaquette faces has exactly four incident elementary 3-cubes in
four dimensions, one being the root. Thus there are exactly three possible
child cubes across each face.

### Root graph

All six faces are available. The 18 candidate child cubes form a conflict graph
`G6`: two candidates conflict iff their 3-cube boundaries share a
plaquette. A valid sibling set in a face-simple tree is an independent set of
`G6`.

Let

`
P6(u)=sum_b a6[b] u^b
`

be its independent-set polynomial.

### Planted graph

For a non-root cube, the complete parent interface face is unavailable.
For each of the six possible choices of parent face, exactly 15 child
candidates remain across the other five faces. Define `G5` by the same
plaquette-sharing conflict rule.

The verifier must establish that all six parent-face choices have the same
independent-set polynomial

`
P5(u)=sum_b a5[b] u^b.
`

No hypercubic symmetry is taken on faith in the finite audit.

## 4. Frozen recursive upper count

Drop every collision between descendants that do not share a parent. This can
only enlarge the class.

Let `T(z)` be the planted recursive description series and `H(z)` the
rooted description series:

`
T = z P5(T),
H = z P6(T).
`

Every actual rooted face-simple cube tree has a unique parent relation from the
root and injects into one recursively generated description. Therefore the
actual rooted-tree counting series is coefficientwise at most `H`.

At the physical absolute activity,

`
x=1/16.
`

To obtain an exponential size tail, introduce `z=yx` with `y>1`.
If one exact `q>0` satisfies

`
z P5(q) <= q,
`

then monotone iteration from zero gives `T(z)<=q`, hence

`
H(z) <= z P6(q).
`

For the actual counts `N_k`,

`
sum_(k>=R) N_k 16^(-k)
 <= y^(-R) z P6(q).
`

Multiplying by the closed-pattern factor one half gives

`
mu_L(exists rooted face-simple cube-tree boundary with k>=R)
 <= (1/2) y^(-R) z P6(q).
`

This is the sole positive target.

## 5. Frozen exact certificate search

The first scientific execution must derive `P5` and `P6` from integer
cubical incidence, not from hard-coded coefficients.

Candidate `y` values are frozen, tested in this exact descending order:

`
2,
3/2,
5/4,
9/8,
17/16,
33/32,
65/64,
129/128,
257/256.
`

For each `y`, search only

`
q=m/4096, 1<=m<=32768.
`

The first grid point satisfying `(y/16) P5(q)<=q` is its certificate.
The largest candidate `y` with a certificate is the declared finite-audit
result.

The grid is not enlarged after execution.

## 6. Exact verifier obligations

The standard-library verifier committed with this file must, before any result
is known:

1. construct elementary 3-cell boundary plaquettes from integer coordinates;
2. verify every root plaquette has exactly four incident 3-cubes;
3. verify 18 distinct root child candidates and 15 distinct planted candidates;
4. construct sibling conflict graphs solely from shared plaquettes;
5. enumerate every independent set exactly and derive `P6` and all six
   `P5` polynomials;
6. verify the six planted polynomials are identical;
7. form the truncated nonnegative recursive series through degree 12 and verify
   it dominates the already known simple-path description count
   `18*15^(k-2)` for `2<=k<=12`;
8. perform only the frozen `(y,q)` certificate search;
9. if a certificate exists, verify its displayed inequality by exact integer
   cross-multiplication and print the exact prefactor
   `(1/2)(y/16)P6(q)`;
10. print explicit scope boundaries.

No float, random number, fit, external data or adaptive search is admitted.

## 7. Pass and failure rules

### Positive route PASS

PASS requires:

- every exact combinatorial assertion above;
- at least one frozen `y>1` with an exact frozen-grid `q` certificate;
- exit code zero and empty stderr.

A PASS supports only a candidate-C finite audit plus a candidate-T written
counting proof after review.

### Local criterion negative

If all exact local graph checks pass but no frozen `y>1` certificate exists,
the verifier must exit zero and report

`
LOCAL_TREE_CERTIFICATE NONE
`

rather than fabricate a theorem. This closes only the chosen local
sibling-compatibility majorant route negatively. It is not a divergence theorem
for the true embedded tree sum.

Any assertion failure, exception, nonzero exit or nonempty stderr is an audit
failure and is preserved.

## 8. Scope boundary

Even a positive tree-tail theorem does not cover:

- cube complexes whose face-intersection graph has cycles;
- arbitrary integer-closed neutral plaquette surfaces;
- charged endpoint decorations without an additional exact gluing theorem;
- the complete two-replica connection kernel;
- uniform `Xi_L` or `Xi_L^(2)`;
- infinite-volume profile existence;
- a massless phase, physical photon, apparatus or P1.

A later pointwise coverage, switching allocation or theorem-preserving
decomposition would be required before the result can control the full current
covariance.
