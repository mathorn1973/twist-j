# PREREG: C-PHOTON-POLYMER-UNCLE-MEMORY-N

**PUBLIC, NON-CANONICAL. No Canon authority.**
Author: A. M. Thorn <thorn@twistj.com>
Date: 26 September 2026
License: Apache-2.0
Owner issue: #1170
Branch: `notes/photon-polymer-uncle-20260926`

## 1. Public basis

Public Canon v92 is the only authority.

- activation/tag target:
  `8b1132d828d94f83e653dab34d686a7e68394939`
- content commit:
  `d7eb6de16c11f6a105996de02ffd7afa32683a93`
- Canon SHA-256:
  `31783fcd8e5ad2a697efd92a6d9fb92c2a21c101b95b9c282ea50fa7cb245f68`
- Canon bytes: `797365`

Non-canonical predecessor only:

- #1168 / draft PR #1169, which proves that the scalar sibling-only majorant
  is supercritical at the physical cube activity `x=1/16`.

No predecessor result is promoted by this note.

## 2. Scoped object

Use the same face-simple elementary 3-cube trees as #1168. A tree with `k`
cubes has an integer-closed ternary boundary of `4k+2` plaquettes and each
deterministic signed boundary pair has full-measure union price at most

`
(1/2) 16^(-k).
`

The new counting grammar retains one additional piece of geometry.

For a non-root cube, define its **uncles** as the other children selected by
its parent. If the parent selected `b` children, every one of those children
has type

`
u=b-1 in {0,1,2,3,4}.
`

A prospective child of the current cube is admitted by this majorant only if

1. it does not attach through the current cube's parent interface face;
2. it shares no plaquette with any uncle;
3. the chosen prospective children are pairwise sibling-compatible, meaning
   their own 3-cube boundaries share no plaquette.

Grandparent, great-grandparent and all longer-range exclusions are dropped.
Therefore the grammar remains an upper count for actual face-simple trees.

## 3. Exact context polynomials

Fix one parent cube and one of its six entry faces. The parent has 15 candidate
children across the other five faces.

Enumerate every independent sibling set `S` of those candidates. For each
`c in S`, set

`
U=S\{c},  u=|U|.
`

At the current cube `c`, enumerate its 15 candidate children across all
faces except the interface back to the parent. Delete every candidate sharing
a plaquette with any cube in `U`. On the survivors, enumerate every
independent sibling set exactly.

For each uncle count `u`, let

`
B_u(b)
`

be the coefficientwise maximum, over all such exact geometric contexts, of
the number of admitted current-child sibling sets of size `b`.

The verifier must repeat the entire construction for all six choices of the
parent's entry face and prove that the resulting five worst-case coefficient
vectors `B_0,...,B_4` are identical.

This coefficientwise maximum deliberately combines different geometric
contexts. It is an upper majorant, not an exact embedded-tree recursion.

## 4. Frozen five-type recursion

If a type-`u` cube chooses `b` children, each child has type `b-1`.
Therefore define the monotone polynomial majorant

`
F_u(T_0,...,T_4;z)
 = z [ B_u(0) + sum_(b=1)^5 B_u(b) T_(b-1)^b ].
`

A componentwise supersolution `q_u` satisfying

`
F_u(q;z) <= q_u  for all u=0,...,4
`

bounds the nonnegative recursive series by monotone iteration from zero.

The root has no uncle type. Its exact sibling polynomial coefficients are
`P6(b)`, and its rooted generating series is bounded by

`
H(z) <= z [ P6(0) + sum_(b=1)^6 P6(b) q_(b-1)^b ],
`

where terms with `b=6` require type 5. Therefore the verifier must first
decide whether `P6(6)` is nonzero. If it is, the root-only six-child term is
bounded separately by the scalar value `q_4^6`, which is a deliberate
overbound because every one of the six root children has five root siblings
but the non-root type system has only `u<=4`. This special root convention
is frozen:

`
root b=6 term -> P6(6) q_4^6.
`

For `1<=b<=5`, use `q_(b-1)^b`.

## 5. Frozen supersolution family

Search only vectors

`
q_u = q r^u,
q=m/4096, 1<=m<=32768.
`

Frozen `r` values, in this exact order:

`
15/16,
7/8,
13/16,
3/4,
11/16,
5/8,
9/16,
1/2,
7/16,
3/8,
5/16,
1/4.
`

Frozen `y` values, largest first:

`
17/16,
33/32,
65/64,
129/128,
257/256,
1.
`

For each pair set

`
z=y/16.
`

Search `m` in increasing order. The first `m` satisfying all five exact
component inequalities is the certificate for that `(y,r)`. The first
certificate in the declared `y`, then `r`, order is the audit result.

No other `q`, `r`, `y`, nonlinear ansatz or adaptive enlargement is
allowed after execution.

## 6. Positive consequence

If a certificate with `y>1` exists, the actual rooted face-simple tree
counting series is bounded at `z=y/16`. Let the exact root upper bound be
`H_bound`. Then for `N_k` actual rooted face-simple cube-tree
descriptions,

`
sum_(k>=R) N_k 16^(-k)
 <= y^(-R) H_bound.
`

Combining with the exact boundary price gives

`
mu_L(exists rooted face-simple cube-tree boundary with k>=R)
 <= (1/2) y^(-R) H_bound.
`

This remains only a tree-class theorem.

## 7. Exact verifier obligations

Before the first scientific execution, the committed standard-library verifier
must be read back from GitHub and may only be statically compiled.

The scientific run must:

1. derive all elementary cubical incidences from integer coordinates;
2. verify the six-face, four-cubes-per-face local geometry;
3. derive the 15-candidate planted graph for all six parent entry faces;
4. enumerate all parent sibling independent sets;
5. generate every current/uncle context and child-vs-uncle exclusion;
6. enumerate every surviving child sibling independent set exactly;
7. compute the coefficientwise worst `B_u`, context counts and unique
   filtered child graphs;
8. verify the `B_u` tables are identical for all six parent entry faces;
9. derive `P6` independently;
10. perform only the frozen supersolution search;
11. verify any displayed certificate by exact integer/rational arithmetic;
12. print explicit scope boundaries.

No floats, randomness, optimization library, external data or fitted threshold
is admitted.

## 8. Decision rules

### Positive

If one frozen `y>1` certificate exists, report

`
UNCLE_MEMORY_CERTIFICATE PASS
`

with exact `y,r,q` and root prefactor.

### Diagnostic only

If no `y>1` certificate exists but `y=1` does, report that the frozen
ansatz proves finite total activity but no exponential margin.

### Negative for this ansatz

If no frozen certificate exists even at `y=1`, report

`
UNCLE_MEMORY_CERTIFICATE NONE
`

and close only the frozen `q r^u` supersolution family negatively.

This is not a divergence theorem for the five-type polynomial system and not a
divergence theorem for actual embedded trees.

Any assertion failure, exception, nonzero exit or nonempty stderr is an audit
failure.

## 9. Scope boundary

A PASS does not cover cube complexes with face-intersection cycles, arbitrary
neutral surfaces, charged endpoint gluing, the full two-replica connection
kernel, uniform `Xi_L` or `Xi_L^(2)`, profile existence, a massless phase,
a physical photon or P1.

No Canon, Registry, Frontier, formal probe, tool or workflow file is changed.
