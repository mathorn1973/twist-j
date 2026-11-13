# PREREG: C-PHOTON-SIGNED-SQUARE-TUBE-XI-N

**PUBLIC, NON-CANONICAL. No Canon authority.**
Author: A. M. Thorn <thorn@twistj.com>
Date: 26 September 2026
License: Apache-2.0
Owner issue: #1186
Branch: `notes/photon-signed-square-tube-20260926`

## 1. Basis

Public Canon v92 is the sole authority.

Mathematical inputs only:

1. public-main `FULL-MEASURE.md`, simple-cycle source inequality;
2. #1176 / draft PR #1177 only at NON-CANONICAL candidate scope for
   `ell(gamma)<=m^2/16`.

No draft is promoted here.

## 2. Contact-simple square tube

Choose two distinct coordinate axes `b,c`. Choose oriented unit vectors
`e_b,e_c`, including their signs.

Let

`
P=(v_0,...,v_D), D>=1,
`

be a simple nonbacktracking path using only the two coordinate axes
complementary to `{b,c}`.

Define offsets

`
A=0,
B=e_b,
C=e_b+e_c,
D0=e_c.
`

Require the four translated copies of `P` to be mutually vertex-disjoint.

Form one cycle in this order:

1. `P+A` forward;
2. far connector `A->B`;
3. `P+B` backward;
4. near connector `B->C`;
5. `P+C` forward;
6. far connector `C->D0`;
7. `P+D0` backward;
8. near connector `D0->A`.

Require the cycle to be simple.

The **contact-simple** condition is that the only opposite-edge plaquette
contacts are:

- for each of the `D` base-path edges, the four adjacent pairs
  `A-B,B-C,C-D0,D0-A`;
- one pair between the two `b` connectors at the far endpoint;
- one pair between the two `c` connectors at the near endpoint.

All are reinforcing. Thus, if `c_P` is the base-path turn count,

`
m=4D+4,
c=4c_P+8,
O_+=4D+2,
O_-=0.                                                   (T1)
`

The written proof is direct from the construction.

## 3. Source weight and one-path entropy

At the fixed exact source `h=log3`,

`
a=15625/177147,
r=41/25.
`

The existing full-measure source bound gives for both current signs of one
fixed square tube

`
P(E_gamma union E_-gamma)
 <=2 a^(4D+4) r^(4D+4c_P+10).                          (T2)
`

For fixed frame, start and first path direction, the base path lives in a
two-dimensional coordinate plane. Every further nonbacktracking continuation
has:

- one straight continuation;
- at most two turns.

A turn of the base path is repeated on all four strands and therefore costs
`r^4` in (T2).

Dropping simplicity and all excluded extra contacts only enlarges the
description sum. Define

`
q_tube=a^4 r^4 (1+2r^4).                                (T3)
`

The intended candidate-T inequality is

`
q_tube<1.
`

For one fixed frame/start/first direction, the weighted source sum at base
length `D` is at most

`
2 a^8 r^14 q_tube^(D-1).                               (T4)
`

## 4. Global Xi bound

Overcount descriptions in a periodic volume `V` by:

- `V` start vertices;
- `48` ordered oriented cross-section frames: ordered distinct axes
  `(b,c)` and independent signs;
- `4` first path directions in the complementary coordinate plane.

Equation (T4) already includes both current signs.

Using the signed-cycle bound

`
ell^2<=m^4/256=(D+1)^4
`

because `m=4(D+1)`, the volume factor cancels and gives

`
Xi_tube(L)
 <=384 a^8 r^14
   sum_(D>=1)(D+1)^4 q_tube^(D-1).                     (T5)
`

Freeze

`
sum_(D>=1)(D+1)^4 q^(D-1)
 =
(16+q+11q^2-5q^3+q^4)/(1-q)^5.                        (G)
`

The intended explicit uniform bound is

`
Xi_tube(L)<=C_tube
`

with

`
C_tube=
384 a^8 r^14
(16+q_tube+11q_tube^2-5q_tube^3+q_tube^4)/(1-q_tube)^5.
`

The verifier prints the reduced rational.

## 5. Contact density and previous complement

For the square tube

`
O_+/m=(4D+2)/(4D+4) ->1.
`

With `tau=73/70`, the #1179 signed-contact condition would require

`
r^(4D+2)<=tau^(4D+4).
`

The verifier must find the first exact `D>=1` where this fails.

Hence a successful result controls a family whose reinforcing-contact density
tends to one, not merely one half.

## 6. Prospective exact audit

Before first execution, commit and publicly read back this file and
`verify.py`.

The standard-library verifier uses only integer and `Fraction` arithmetic
and must:

1. reconstruct `a,r,q_tube` and prove `q_tube<1`;
2. verify generating identity (G);
3. compute exact `C_tube`;
4. construct straight square tubes for `D=1,...,6`;
5. construct one-turn square tubes for `D=2,...,6`;
6. derive their current edges and oriented plaquette contacts directly;
7. verify simplicity and exactly
   `m=4D+4,c=4c_P+8,O_+=4D+2,O_-=0`;
8. compute the axial signed-slice `ell` for a fixed orientation convention
   and verify `ell<=m^2/16`;
9. find the first exact `D` outside the #1179 signed-contact class;
10. print scope boundaries.

Finite examples audit geometry, not the all-D proof.

## 7. Boundary

This item controls only contact-simple square tubes. It is not a covering
theorem for all high-contact simple cycles.

Still outside scope:

- tubes with extra self contacts;
- other cross-section bundles;
- arbitrary high-contact simple cycles;
- non-simple current networks;
- multi-cycle paired components;
- full `Xi_L`, `Xi_L^(2)`, `chi_L`;
- P1, massless phase and physical photon.

No Canon, Registry, Frontier, probe, tool, workflow or release file changes.
