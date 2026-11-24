# Sources and scope correspondence

**NON-CANONICAL. Authority none.** Bibliographic and scope record for
C-HUANG-ARITHMETIC-BRIDGE-N. The new paper deductions are candidate-D;
the complete signed-energy estimate remains O. No novelty is asserted.

## Primary mathematical sources

| Source | Content used here | Limit of that use |
| --- | --- | --- |
| Hao Huang, *Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture*, Annals of Mathematics 190 (2019), 949--955, [DOI](https://doi.org/10.4007/annals.2019.190.3.6), [paper](https://annals.math.princeton.edu/wp-content/uploads/annals-v190-n3-p06-s.pdf) | Theorem 1.1, strict majority implies maximum degree at least the square root of dimension; signed cube with square a scalar | Does not assert a prime-density premise or arithmetic cancellation |
| Roman Karasev, *Huang's theorem and the exterior algebra*, [arXiv:1907.11175v2](https://arxiv.org/abs/1907.11175v2) | Exterior multiplication plus contraction; scalar square, parity and dimension argument | Supplies the known operator description, not a new Mobius estimate |
| Daniel V. Mathews, *The sensitivity conjecture, induced subgraphs of cubes, and Clifford algebras*, [arXiv:1907.12357v2](https://arxiv.org/abs/1907.12357v2) | Theorem 1.2, nonnegative coordinate weights and Euclidean norm lower bound | The weighted extension predates this package |
| Sophie Laplante, Reza Naserasr and Anupa Sunny, *Sensitivity Lower Bounds from Linear Dependencies*, MFCS 2020, LIPIcs 170, 62:1--62:14, [DOI](https://doi.org/10.4230/LIPIcs.MFCS.2020.62) | Theorem 24 confirms the weighted statement; related refinements count vertices within distance two | A distance-two conclusion must not be read as square-root immediate degree on both parity sides |
| Anders Bjorner, *A cell complex in number theory*, [arXiv:1101.5704v1](https://arxiv.org/abs/1101.5704v1) | Section 1 identifies the squarefree-divisor complex and its reduced Euler characteristic as minus M(n); Theorems 2.1 and 3.1 give the shifted-complex and odd-squarefree interval counts used to identify the single-cut homology | The sign uses reduced characteristic; the paper explicitly says its Betti estimates do not improve the growth estimate for M(n). The two-cut inclusion ranks have an explicit paper derivation in round2/MIXED-BOUNDARIES.md |

König's matching theorem and Hall's marriage theorem are used in their
standard finite bipartite forms. The new notes give the precise graph and
the vertex-cover or neighborhood condition before invoking them. The
matching corollary and its localization are proved here as candidate-D
deductions from those published inputs; no claim of original priority is
made. External papers are referenced and summarized. No third-party PDF,
figure, source code or long quotation is redistributed in this package.

Bjorner's Theorem 2.3(b), at k=1, also records the classical prime
counting asymptotic. The final matching-majorant obstruction uses this
input only after the exact pair construction: primes in (N/6,N/3]
give the disjoint edges 3q to 6q. It converts their count to a lower
bound of order N/log N. That lower bound concerns an unsigned matching
majorant, not the signed Mobius sum or the original residual energy.

## Existing public scope

The basis is public main
`6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`, Public Canon v117.
The registered claims
[GOLDEN-CLIFFORD-COIN-IDENTITY](https://github.com/mathorn1973/twist-j/blob/6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed/canon/CANON.md#L32319)
and
[ALPHA-PREFACTOR-UNIFICATION](https://github.com/mathorn1973/twist-j/blob/6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed/canon/CANON.md#L23759)
retain their registered T status and exact scope. The present quadratic
basis interpretation and doubled coefficient record create no new Canon
claim and no physical reading. The fixed real two-dimensional capacity
statement is not a dimension bound on arbitrary enlarged representations.

## Inherited arithmetic target

The source is the separate non-canonical candidate
C-RH-THREE-INTERFACE-SYNTHESIS-N at
`ceb77e3632ec4617c54d8e1fd504d3b1c99dd106`,
[draft #2093](https://github.com/mathorn1973/twist-j/pull/2093).

| Pinned note | Exact use |
| --- | --- |
| [FULL-COUPLED-ENERGY.md](https://github.com/mathorn1973/twist-j/blob/ceb77e3632ec4617c54d8e1fd504d3b1c99dd106/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N/FULL-COUPLED-ENERGY.md) | Complete two-large-factor floor sum, negative affine square, hyperbola overlap squares, and full weighted norm comparison between Z and R |
| [BILINEAR-LOW.md](https://github.com/mathorn1973/twist-j/blob/ceb77e3632ec4617c54d8e1fd504d3b1c99dd106/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N/BILINEAR-LOW.md) | Frozen raw masks, forward average, primitive projection and coefficient majorants preserved by the doubled record |
| [WINDOW-BOUND.md](https://github.com/mathorn1973/twist-j/blob/ceb77e3632ec4617c54d8e1fd504d3b1c99dd106/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N/WINDOW-BOUND.md) | Direct weighted comparison of M with the original R_(1/36), with original complete windows |

These are candidate-D inputs in their own package. This package neither
promotes them nor substitutes a bound on a character twist, a selected
factor range, a model sequence or a shortened window for the actual target.
The original positive-energy bound remains O.

## Round-two source distinctions

The scope at 51c7bc9024ca601d4d21511a2b88ffcacc9f84fe keeps the
preceding arithmetic input fixed. The small-rectangle estimate and
the maximal short-sum and residual comparisons in its full-energy
note supply the analytic inputs to the growing-product transfer.
The exact reallocation and its coefficient-support bound are proved
in the new notes. The logarithmic diagonal bound uses only a count
of odd integers and telescoping weights.

The classical prime number theorem, also stated in Bjorner's
Theorem 2.3(b) at k=1, is used for the prime-core leading term and
for the size of the product of selected small primes. The
complementary-core leading term additionally uses the inherited
classical bound on M. The full-line inverse-filter norm concerns an
abstract two-sided operator; the actual prefix is not assumed to
belong to that full-line space.

The neighboring non-canonical candidate C-RH-ARITHMETIC-KERNEL-N
was read at 6a91ef48f6454743797614503aa5863dde54befb,
[round8/COUPLED-CUTS.md](https://github.com/mathorn1973/twist-j/blob/6a91ef48f6454743797614503aa5863dde54befb/notes/C-RH-ARITHMETIC-KERNEL-N/round8/COUPLED-CUTS.md).
Its split-prime prefix uses different local coefficients and its
own nonnegative inverse. Its contraction is not asserted for the
Möbius sequence. The scopes and ownership of both candidates remain
separate.
