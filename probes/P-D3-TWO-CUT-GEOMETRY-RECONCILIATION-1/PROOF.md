# Completeness of the finite geometry check

NON-CANONICAL / L1 / exact analytical justification of the algorithms.
A. M. Thorn, 2026-10-15. Apache-2.0. Source-exposed, self-reviewed.
This file is frozen before the run; it does not report an executed count.

## Primary definition, not a choice of target dimension

The adopted set is exactly D=Y+B0+B0 in the primary #1485 CONTRACT.
All coordinates, shell lengths and ordering are fixed by PREREG.md.
The later number 869 conflicts with reported enumeration and is the object
of reconciliation. We do not define D as an arbitrary set of either size.

## Method A is exhaustive

For d in B, each coordinate satisfies d_i^2<=16, hence -4<=d_i<=4.
Inspecting all triples in this cube with the given parity and squared-norm
predicate returns exactly B, without omissions or extra vectors.
Adding the unique zero vector gives B0. The three nested finite sums return
exactly the elements y+d+e. Passing to a set removes repetitions of one
point; cardinality is the number of distinct points, not paths to them.

## Method B has a separately characterized stencil

Sort the absolute coordinates of a nonzero admissible offset in decreasing
order. The only possibilities for the five squared-norm shells are

    2: (1,1,0), 4: (2,0,0), 8: (2,2,0),
    10: (3,1,0), 16: (4,0,0).

To see completeness, the largest absolute coordinate is 1, 2, 3 or 4.
Subtract its square from each prescribed shell length and test whether the
remainder is a sum of two squares no larger than that coordinate squared.
This yields exactly the five rows displayed. All their coordinate sums
are even; sign changes preserve evenness. Signed permutations therefore
return exactly B. Their distinct sizes are respectively 3*4, 3*2, 3*4,
6*4 and 3*2. The weighted sum is

    12*6 + 6*1 + 12*15 + 24*1 + 6*1 = 288.

Thus the full Laplacian diagonal stays 288/324=8/9, including on the boundary.

## The membership box is a proof bound, not a fitted window

Every coordinate of d+e lies in [-8,8]. The seed coordinate ranges are
[0,2], [0,1], [0,1]. Consequently every element of D belongs to
[-8,10] x [-8,9] x [-8,9]. Method B visits every integer point of that box,
including the odd-parity candidates, then selects by an exact predicate.
For fixed p,y,d, the condition p-y-d in B0 is exactly even coordinate sum
and squared length in {0,2,4,8,10,16}. Thus the existential membership test
is equivalent in both directions to p in Y+B0+B0. It neither consumes A's
point list nor infers equality from an equal cardinality.

## Full certificate and reading scope

The verifier compares the resulting sets literally. If they agree and all
fixed tests pass, the displayed TSV is the exact complete set, since it
is the sorted image of a finite set under the identity coordinate map.
Parsing the bytes back verifies the serialization and absence of duplicates.
The x-slice table is an additional count certificate, not a substitute for
full point equality. The TSV SHA-256 binds the precise bytes a successor
should consume together with its source definition and order.

The 705 count is an exposed target to be checked at execution. If it fails,
this proof of algorithmic completeness does not permit changing the target
or the set. No source work/cut matrix follows merely from fixing the geometry.

## Adversarial self-review

Squared lengths are not ordinary lengths, D3 parity is not omitted, and all
signs/permutations are included. The five marked sites retain their exact
order, including y4=(2,0,0). D is not a box and the containing box does not
replace D. Zero is allowed in each of the two offsets, so one-step and seed
supports are subsets. There is no periodic wrapping or graph-Laplacian
boundary adjustment. Checking full set equality rather than only size
catches misplaced sites that would preserve the total count.
The two algorithms have one author; independent external review is separate.
