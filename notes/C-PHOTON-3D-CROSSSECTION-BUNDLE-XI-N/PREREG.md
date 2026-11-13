# PREREG: C-PHOTON-3D-CROSSSECTION-BUNDLE-XI-N

**PUBLIC, NON-CANONICAL. No Canon authority.**
Author: A. M. Thorn <thorn@twistj.com>
Date: 26 September 2026
License: Apache-2.0
Owner issue: #1190
Branch: `notes/photon-3d-crosssection-bundle-20260926`

## 1. Basis

Public Canon v92 is the sole authority.

Mathematical inputs only:

1. public-main `notes/C-PHOTON-BCHI-DIRECT-BOUND-N/FULL-MEASURE.md`,
   the exact simple-cycle source inequality;
2. #1176 / draft PR #1177 only at its declared NON-CANONICAL candidate scope,
   for the deterministic bound `ell(gamma)<=m^2/16`.

#1188 / draft PR #1189 is motivation only. Nothing from that draft is used as
authority.

## 2. Straight prism bundle with a 3D cross-section

Choose one oriented coordinate axis `a` as the base direction. The remaining
three coordinate axes form the cross-section lattice `Z^3`.

Choose any simple lattice polygon

`
Q=(u_0,...,u_(k-1)),  k>=4,
`

in that cross-section, with `u_k=u_0`. The cubic lattice is bipartite, so
`k` is even.

Choose the straight base segment of length `D>=1` along `a`.

For every cross-section vertex `u_j`, take one translated length-`D`
strand. Traverse strand `j` forward for even `j` and backward for odd
`j`. Connect consecutive strands by the polygon edge
`u_j -> u_(j+1)`, at the far endpoint after an even strand and at the near
endpoint after an odd strand.

Require the assembled current cycle to be simple.

No induced-polygon condition is imposed. Nonconsecutive cross-section vertices
may be nearest neighbors and create extra strand contacts.

## 3. Deterministic contact and turn bounds

Let `E_Q` be the number of unordered nearest-neighbor pairs among all
cross-section vertices, including polygon edges and unit-distance chords.

The induced cubic-lattice graph has maximum degree six, hence

`
E_Q<=3k.                                                (D1)
`

Checkerboard parity of a cross-section vertex agrees with its index parity
along `Q`. Every nearest-neighbor pair therefore has opposite index parity,
and the corresponding two parallel strands are traversed in opposite
directions. Each pair gives one reinforcing opposite-edge plaquette contact
for every one of the `D` base edges:

`
O_+^(strand)=D E_Q<=3kD.                               (D2)
`

At a fixed endpoint there are `k/2` connector edges. In the cubic
cross-section a unit edge has at most four opposite parallel unit-edge
neighbors. Therefore the connector-contact graph has maximum degree four and
at most `k` contact pairs at one endpoint. Across both endpoints,

`
O^(connector)<=2k.                                     (D3)
`

Each strand has one connector transition at each end. There are no
connector-to-connector consecutive steps in the cycle, so

`
m=k(D+1),
c=2k.                                                  (D4)
`

Charging every connector contact by the reinforcing factor gives

`
c+O_++O_-<=3kD+4k.                                    (D5)
`

## 4. Exact source choice and entropy

Use the existing source inequality at

`
h=log2.
`

Then

`
a=15625/131072,
r=34/25,
s=16/25.
`

For one fixed bundle description, including both current signs,

`
P(E_gamma union E_-gamma)
 <=2 a^[k(D+1)] r^[3kD+4k].                           (S)
`

Root `Q) at one vertex. A nonbacktracking walk in the cubic cross-section
has six first directions and at most five subsequent choices. Dropping closure
and self-avoidance,

`
# rooted Q descriptions <=6*5^(k-1).                   (E1)
`

There are eight oriented choices of the base axis and `V` starting vertices.
The two current signs are already included in the factor two in (S).

Define

`
q_k=(a r^3)^k,
q4=(a r^3)^4,
b3=5 a^2 r^7.                                          (E2)
`

Freeze the intended inequalities

`
0<a r^3<1,
q_k<=q4<1 for all k>=4,
0<b3<1.                                                (E3)
`

## 5. Uniform signed-moment sum

Let `Xi_3D_bundle(L)` be the contribution to the one-copy paired signed
moment from components whose current is exactly one unit simple cycle in the
declared prism-bundle class.

By the candidate deterministic lemma from #1176,

`
ell^2<=m^4/256=k^4(D+1)^4/256.
`

The description count, source price and `1/V` normalization give

`
Xi_3D_bundle(L)
 <=(3/40)
   [sum_(even k>=4) k^4 b3^k]
   [sum_(D>=1)(D+1)^4 q4^(D-1)].                       (X)
`

Freeze the same exact generating functions:

`
x=b3^2,

sum_(even k>=4) k^4 b3^k
=
16[
 x(1+11x+11x^2+x^3)/(1-x)^5 -x
],                                                     (G1)

sum_(D>=1)(D+1)^4q^(D-1)
=
(16+q+11q^2-5q^3+q^4)/(1-q)^5.                        (G2)
`

Define the exact rational candidate

`
C_3D=(3/40) G1(b3) G2(q4).
`

## 6. Frozen examples

The verifier must construct the following cross-sections directly in the
three cross-section coordinates.

### Q4 planar square

`
(0,0,0),
(1,0,0),
(1,1,0),
(0,1,0).
`

### Q6 nonplanar hexagon

`
(0,0,0),
(1,0,0),
(1,1,0),
(1,1,1),
(0,1,1),
(0,0,1).
`

### Q8 nonplanar chorded polygon

`
(0,0,0),
(1,0,0),
(2,0,0),
(2,0,1),
(2,1,1),
(2,1,0),
(1,1,0),
(0,1,0).
`

The Q8 example has at least one nearest-neighbor pair that is not a polygon
edge. The verifier must derive this rather than hard-code the contact count.

For every cross-section use straight base lengths `D=1,...,6`.

## 7. Prospective exact audit

Before the first scientific execution, commit and publicly read back this file
and `verify.py`.

The standard-library verifier uses integers and `Fraction` only and must:

1. reconstruct `a,r,s,a r^3,b3,q4`;
2. verify exactly `s<r`, `a r^3<1`, `b3<1`, `q4<1`;
3. verify `q_k<=q4` on an exact finite audit range, while the written proof
   uses monotonicity of a number in `(0,1)`;
4. verify (G1) and (G2) by exact coefficient identities;
5. construct Q4, Q6 and Q8 and prove simplicity, closure and even length;
6. prove Q6 and Q8 are nonplanar by exhibiting variation in all three
   cross-section coordinates;
7. prove Q8 has a nearest-neighbor chord beyond polygon adjacency;
8. construct the corresponding four-dimensional prism cycles for
   `D=1,...,6`;
9. derive actual current edges, `m,c,O_+,O_-`, `E_Q`,
   connector-contact count and signed-slice `ell`;
10. verify (D1)-(D5) and `ell<=m^2/16` for every example;
11. compute and print exact reduced `C_3D`;
12. print the scientific boundary.

Finite examples audit geometry. They do not prove the all-`k,D` theorem.

Any assertion failure, exception, timeout, nonzero exit or nonempty stderr
fails the audit and is preserved.

## 8. Status and boundary

A successful audit is at most candidate-C. The deterministic contact bounds,
description sum and uniform inequality (X) are candidate-T pending separate
review.

This does not prove that every simple cycle is a straight prism bundle.

Still outside scope:

- arbitrary non-product simple cycles;
- bent-base bundles;
- non-simple or branched current networks;
- paired components containing multiple current cycles;
- full `Xi_L`, `Xi_L^(2)`, `chi_L`;
- P1, massless phase and physical photon.

No Canon, Registry, Frontier, probe, tool, workflow or release file changes.
