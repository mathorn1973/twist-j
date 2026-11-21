# PREREG: C-PHOTON-CONTACT-ENTROPY-BUNDLE-XI-N

**PUBLIC, NON-CANONICAL. No Canon authority.**
Author: A. M. Thorn <thorn@twistj.com>
Date: 26 September 2026
License: Apache-2.0
Owner issue: #1188
Branch: `notes/photon-contact-entropy-bundle-20260926`

## 1. Basis

Public Canon v92 is the sole authority.

Mathematical inputs only:

1. public-main `notes/C-PHOTON-BCHI-DIRECT-BOUND-N/FULL-MEASURE.md`,
   the exact simple-cycle source inequality;
2. #1176 / draft PR #1177 only at its declared NON-CANONICAL candidate scope,
   for the deterministic bound `ell(gamma)<=m^2/16`.

The fixed ribbon and square-tube notes #1184/#1186 are motivation only.
Nothing in them is an authority dependency.

## 2. Product-bundle class

Choose an unordered pair of coordinate axes `{b,c}` for the cross-section
plane. The complementary two coordinate axes form the base-path plane.

Choose any simple lattice polygon

`
Q=(u_0,...,u_(k-1)),   k>=4,
`

in the cross-section square lattice, with `u_k=u_0`. Since the square
lattice is bipartite, `k` is even.

Choose a simple nonbacktracking base path

`
P=(v_0,...,v_D),   D>=1,
`

in the complementary coordinate plane.

For every cross-section vertex `u_j`, take the translated strand `P+u_j`.
Traverse strand `j` forward when `j` is even and backward when `j` is
odd. Connect consecutive strands by the polygon edge
`u_j -> u_(j+1)`, at the far endpoint after an even strand and at the near
endpoint after an odd strand.

Require the resulting current cycle to be simple.

No induced-polygon condition is imposed. Nonconsecutive vertices of `Q`
may be nearest neighbors and then generate additional strand contacts.

This item sums only bundle descriptions satisfying this product form. It is
not a decomposition theorem for arbitrary simple cycles.

## 3. Deterministic contact and turn bounds

Let `E_Q` be the number of unordered nearest-neighbor pairs among all
`k` cross-section vertices, including polygon edges and unit-distance
chords.

The induced square-lattice graph on `k` vertices has maximum degree four, so

`
E_Q <= 2k.                                               (D1)
`

Index parity along `Q` equals square-lattice checkerboard parity. Every
nearest-neighbor pair therefore has opposite index parity. Since strand
traversal orientation alternates with index parity, every such pair consists
of oppositely directed parallel strands. For every one of the `D` base-path
edges this gives one reinforcing opposite-edge plaquette contact. Thus

`
O_+^(strand)=D E_Q <=2kD.                               (D2)
`

The `k` connector edges split into `k/2` at each endpoint. In a square
lattice a unit edge has at most two opposite parallel unit-edge neighbors.
Therefore each endpoint connector contact graph has degree at most two and at
most `k/2` contact pairs. Across both endpoints,

`
O^(connector) <= k.                                     (D3)
`

Every connector contact, regardless of its true sign, is pessimistically
charged by the reinforcing source factor `r`.

Let `c_P` be the base-path turn count. Every base-path turn occurs on every
strand, and every one of the `k` connectors gives a turn at each endpoint.
Hence exactly

`
m=k(D+1),
c=k c_P+2k.                                             (D4)
`

Combining (D2)-(D4),

`
c + O_+ + O_-
 <= k c_P + 2kD + 3k,                                  (D5)
`

when every connector contact is upper-bounded by the reinforcing factor.

## 4. Exact source choice

Use the existing general source inequality at

`
h=log2.
`

Then exactly

`
a=15625/131072,
r=34/25,
s=16/25.
`

Ignoring the beneficial `s<r` distinction for connector contacts, one fixed
bundle description, including both current signs, satisfies

`
P(E_gamma union E_-gamma)
 <=2 a^[k(D+1)] r^[2kD + k c_P + 3k].                  (S)
`

No new source inequality is asserted.

## 5. Exact geometric entropy

### Cross-section

Root `Q` at `u_0=0`. A nonbacktracking square-lattice walk has four first
directions and at most three subsequent directions. Dropping closure and
self-avoidance,

`
# rooted Q descriptions of length k <=4*3^(k-1).         (E1)
`

### Base path

For fixed first base-path direction, every subsequent nonbacktracking step
has one straight continuation and at most two turns.

A turn is repeated on all `k` strands, so it costs `r^k` in (S). Therefore
the weighted continuation factor is

`
1+2r^k.                                                  (E2)
`

Define

`
q_k = a^k r^(2k) (1+2r^k)
    = (a r^2)^k + 2(a r^3)^k.                           (E3)
`

Freeze

`
q4=(a r^2)^4+2(a r^3)^4.
`

The written proof must establish

`
0<a r^2<1,
0<a r^3<1,
q_k<=q4<1  for every k>=4.                              (E4)
`

The fixed-`k,D` description sum is then at most

`
192 V * 3^(k-1) * a^(2k) r^(5k) * q_k^(D-1).           (E5)
`

The coefficient 192 is frozen before computation:

- `6`: unordered coordinate cross-section planes;
- `4`: first cross-section step;
- `4`: first base-path step;
- `2`: two current signs already present in the source event;
- `V`: starting vertices.

All subsequent choices are carried by (E1)-(E3).

Define the cross-section size factor

`
b=3 a^2 r^5.                                             (E6)
`

The written proof must establish `0<b<1`.

## 6. Uniform signed-moment sum

Let `Xi_bundle(L)` be the part of the one-copy paired signed moment from
components whose current is exactly one unit simple cycle in the product-bundle
class above.

The candidate deterministic lemma from #1176 gives

`
ell^2 <= m^4/256
      = k^4(D+1)^4/256.
`

Union-bound the augmented component event by the corresponding full-current
source event, exactly as in #1176. With (E5), the factor `V` cancels and

`
Xi_bundle(L)
 <= (1/4)
    [ sum_(even k>=4) k^4 b^k ]
    [ sum_(D>=1) (D+1)^4 q4^(D-1) ].                    (X)
`

This uses `q_k<=q4`.

Freeze the exact generating functions. Put `x=b^2`. Then

`
sum_(even k>=4) k^4 b^k
 =
16 [
 x(1+11x+11x^2+x^3)/(1-x)^5 - x
 ].                                                      (G1)
`

Also

`
sum_(D>=1)(D+1)^4 q^(D-1)
 =
(16+q+11q^2-5q^3+q^4)/(1-q)^5.                         (G2)
`

Define the exact rational candidate bound

`
C_bundle=(1/4) G1(b) G2(q4).
`

The verifier prints its reduced fraction.

## 7. Prospective exact audit

Before first scientific execution, commit and publicly read back this file and
`verify.py`.

The standard-library verifier uses integers and `Fraction` only and must:

1. reconstruct `a,r,s,b,q4`;
2. verify exactly
   `s<r`, `a r^2<1`, `a r^3<1`, `b<1`, `q4<1`;
3. verify (G1) and (G2) by exact coefficient identities;
4. compute exact `C_bundle`;
5. construct product bundles with cross-sections equal to the boundary of
   rectangles `1x1`, `1x2`, and `2x2`;
6. combine each with straight base paths and, where possible, one-turn base
   paths of lengths through six;
7. derive from actual current edges:
   `m`, `c`, true `O_+,O_-`, the cross-section nearest-neighbor count
   `E_Q`, and connector-contact count;
8. verify every example obeys (D1)-(D5) and the signed-cycle
   `ell<=m^2/16` inequality;
9. include the `1x2` cross-section specifically to audit a unit-distance
   chord beyond the polygon edges;
10. print explicit scope boundaries.

Finite examples audit geometry. They do not prove the all-`k,D` theorem.

Any assertion failure, exception, timeout, nonzero exit or nonempty stderr
fails the audit and is preserved.

## 8. Status and boundary

A successful audit is at most candidate-C. The deterministic bounds,
description sum and volume-uniform inequality (X) are candidate-T pending
separate review.

This item does not prove that every simple cycle is a product bundle.

Still outside scope:

- arbitrary simple current cycles not admitting one common base path and one
  planar cross-section;
- bundles with geometry outside the declared product construction;
- non-simple or branched current networks;
- paired components containing multiple current cycles;
- full `Xi_L`, `Xi_L^(2)`, `chi_L`;
- P1, massless phase and physical photon.

No Canon, Registry, Frontier, probe, tool, workflow or release files change.
