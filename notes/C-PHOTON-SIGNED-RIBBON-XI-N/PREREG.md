# PREREG: C-PHOTON-SIGNED-RIBBON-XI-N

**PUBLIC, NON-CANONICAL. No Canon authority.**
Author: A. M. Thorn <thorn@twistj.com>
Date: 26 September 2026
License: Apache-2.0
Owner issue: #1184
Branch: `notes/photon-signed-ribbon-20260926`

## 1. Basis

Public Canon v92 is the sole authority.

Mathematical inputs only:

1. public-main `FULL-MEASURE.md`, the exact simple-cycle source inequality;
2. #1176 / draft PR #1177 only at its declared NON-CANONICAL candidate scope,
   for `ell(gamma)<=m^2/16`.

No draft is promoted by this item.

## 2. Contact-simple ribbon class

Work in the four-dimensional cubical lattice. A **contact-simple unit ribbon**
is specified by:

- an oriented coordinate displacement `e_b`;
- a simple nonbacktracking lattice path
  `P=(v_0,...,v_D)`, with `D>=2`;
- no step of `P` parallel to axis `b`;
- `P` and `P+e_b` are vertex-disjoint;
- the endpoint connector edges from `v_D` to `v_D+e_b` and from
  `v_0+e_b` to `v_0` complete one simple cycle;
- the only opposite-edge plaquette contacts of that cycle are the `D`
  corresponding pairs consisting of one edge of `P` and its translated
  edge in `P+e_b`.

The final condition in particular excludes an extra opposite contact between
the two connector edges.

Orient the cycle by following `P` forward, the far connector, the translated
path backward, and the near connector.

Let `c_P` be the number of right-angle turns of `P`. Then the intended
deterministic identities are

`
m=2D+2,
c=2c_P+4,
O_+=D,
O_-=0.                                                   (R1)
`

The verifier audits finite examples; the written proof is by direct geometry.

## 3. Exact source weight

At the existing exact source `h=log3` put

`
a=15625/177147,
r=41/25.
`

The public source estimate gives for the two current signs of one fixed ribbon

`
P(E_gamma union E_-gamma)
 <= 2 a^(2D+2) r^(D+2c_P+4).                           (R2)
`

No additional contact factor occurs by the contact-simple definition.

## 4. Weighted path count

Fix `b`, a starting vertex and the first path direction.

Since `P` uses only the three coordinate axes different from `b`, every
nonbacktracking continuation has:

- one straight continuation, adding no turn;
- at most four right-angle turns, each adding one turn to `P`.

Because the ribbon cycle contains both `P` and its translated reverse, one
turn of `P` contributes `r^2` in (R2).

Dropping self-avoidance, translated-path disjointness and the prohibition of
extra contacts only enlarges the path description sum. Hence the weighted
continuation factor is exactly bounded by

`
1+4r^2.
`

Define

`
q_rib=a^2 r(1+4r^2).                                    (R3)
`

The intended candidate-T inequality is

`
q_rib<1.
`

For fixed start, oriented `b` and first direction, the total source-event
weight at base-path length `D` is at most

`
2 a^4 r^5 q_rib^(D-1).                                 (R4)
`

## 5. Global description count and Xi contribution

For each periodic volume `V=L^4`, overcount ribbon descriptions by:

- `V` starting vertices;
- `8` oriented choices of `b`;
- `6` first directions not parallel to `b`.

Equation (R4) already includes both current signs. Thus there are no further
orientation factors.

Let `Xi_rib(L)` be the part of the one-copy paired signed moment contributed
by components whose current is one contact-simple unit ribbon cycle.

The component event is a subset of the full current source event
`E_gamma union E_-gamma`, as in #1176. Union-bounding over ribbon
descriptions and using

`
ell(gamma)^2 <= m^4/256 = (2D+2)^4/256
`

gives

`
Xi_rib(L)
 <= 48 * sum_(D>=2)
      [(2D+2)^4/256]
      * [2 a^4 r^5 q_rib^(D-1)]
 = 6 a^4 r^5
   * sum_(D>=2) (D+1)^4 q_rib^(D-1).                    (R5)
`

The `V` description factor cancels the `1/V` in `Xi_L`.

For `0<q<1`, freeze the generating identity

`
sum_(D>=2)(D+1)^4 q^(D-1)
 =
(16+q+11q^2-5q^3+q^4)/(1-q)^5 - 16.                   (G)
`

The candidate-T uniform bound is therefore

`
Xi_rib(L) <= C_rib
`

with

`
C_rib =
6 a^4 r^5
[
 (16+q_rib+11q_rib^2-5q_rib^3+q_rib^4)/(1-q_rib)^5
 -16
].
`

The verifier prints the exact reduced rational.

## 6. Relation to the signed-contact complement

For these ribbons

`
O_+/m = D/(2D+2) -> 1/2,
O_-=0.
`

Thus for sufficiently large `D`,

`
r^D > tau^(2D+2)
`

with `tau=73/70`; these ribbons lie outside the sign-sensitive class from
#1179. The verifier must find the first `D>=2` where the exact inequality
holds.

This establishes that the ribbon result controls a genuine part of the
remaining simple-cycle complement rather than merely rephrasing #1179.

## 7. Prospective exact audit

Before first execution, commit and publicly read back this file and
`verify.py`.

The verifier uses only integers and `Fraction` and must:

1. reconstruct `a,r,q_rib` and prove `q_rib<1`;
2. verify generating identity (G) algebraically;
3. compute exact `C_rib`;
4. construct explicit straight ribbons for `D=2,...,8`;
5. construct explicit one-turn ribbons for `D=3,...,8`;
6. from the actual current edges and plaquette incidence, verify simplicity,
   `m=2D+2`, `O_+=D`, `O_-=0`, and the claimed turn formula;
7. calculate `ell` on each example and verify the deterministic
   `ell<=m^2/16` bound;
8. find the first exact `D` where the ribbon lies outside the #1179
   signed-contact class;
9. print scope boundaries.

Finite examples audit the geometry. They do not prove the all-D counting
argument.

Any assertion failure, exception, timeout, nonzero exit or nonempty stderr
fails the audit and is preserved.

## 8. Boundary

A successful result controls only contact-simple unit ribbons. It does not
cover:

- ribbons with extra self-contacts;
- general high-contact simple cycles;
- non-simple or branched current networks;
- multi-cycle paired components;
- full `Xi_L`, `Xi_L^(2)`, `chi_L`;
- P1, massless phase or physical photon.

No Canon, Registry, Frontier, probe, tool, workflow or release file changes.
