# Face-simple neutral cube trees: the sibling-only polymer majorant is supercritical

**PUBLIC, NON-CANONICAL.**
**Status:** candidate-T written no-go plus candidate-C one-architecture exact audit.
Owner: #1168.
Author: A. M. Thorn.
Date: 26 September 2026.
License: Apache-2.0.
Basis: Public Canon v92.

The previous photon work already proved an unconditional exponential sum for
simple cube chains and for one generated comb/corridor family. The next natural
attempt was to extend this to **all face-simple cube trees** by keeping every
local sibling collision while dropping only collisions between more distant
descendants.

That attempt fails for an exact reason.

The failure is useful. It shows precisely where the entropy enters: simple
paths are subcritical at face fugacity one half, but local branching already
overwhelms the `1/16` price per added cube unless nonlocal geometric
collisions are also retained.

No statement below concerns arbitrary neutral surfaces, current covariance,
`Xi_L`, a photon phase or P1.

## 1. Exact activity of a cube tree boundary

Let `C` be a face-simple tree of `k` elementary 3-cubes in the
four-dimensional cubical lattice. Its face-intersection graph is a tree, so
there are exactly `k-1` shared plaquettes. Orient cubes coherently across
those interfaces.

Every shared face cancels. No other face is repeated. Thus the integer-closed
ternary boundary has

`
A(k)=6k-2(k-1)=4k+2
`

occupied plaquettes.

The exact deletion identity already proved in `NEUTRAL-SUM.md` gives for
this deterministic boundary and its global reversal

`
mu_L(+partial C or -partial C)
 <= 2^(1-A(k))
 = (1/2) 16^(-k).                                      (1)
`

So the geometric question is whether the number of rooted cube trees grows
slowly enough to sum against `16^(-k)`.

For a simple nonbranching chain the previous count gives at most

`
18*15^(k-2)
`

descriptions for `k>=2`, and therefore the familiar ratio `15/16<1`.
Branching is the issue.

## 2. Exact local sibling graphs

Fix one elementary root cube. Each of its six plaquette faces belongs to four
elementary 3-cubes in four dimensions. Removing the root leaves three possible
children across each face, hence 18 root candidates.

For a non-root cube the complete parent face is unavailable. Five exit faces
remain, hence 15 possible children.

Two candidate children cannot both occur as siblings in a face-simple tree if
their own cube boundaries share a plaquette. The finite exact audit constructs
that conflict relation directly from integer cubical incidence and enumerates
all independent sibling sets.

It gives

`
P6(u)
 = 1 + 18u + 111u^2 + 308u^3
     + 429u^4 + 294u^5 + 79u^6,                        (2)
`

for the root, and for **each of all six choices of parent face**

`
P5(u)
 = 1 + 15u + 74u^2 + 154u^3 + 143u^4 + 49u^5.          (3)
`

The root candidate conflict graph has 42 edges. Every planted graph has 31.

The equality of all six planted polynomials was checked explicitly rather
than inferred from symmetry.

## 3. The sibling-only recursive majorant

Now deliberately forget every collision between descendants that do not share
a parent. This enlarges the class.

Let `T(z)` be the planted recursive description series. At each non-root
cube an allowed child set is one independent set counted by `P5`, and every
selected child receives an independent planted descendant. Therefore

`
T(z)=z P5(T(z)).                                        (4)
`

The root series is

`
H(z)=z P6(T(z)).                                        (5)
`

Every actual rooted face-simple cube tree has a unique parent relation from
the root and determines one recursive description. Therefore its counting
series is coefficientwise bounded by `H`.

This is an upper-counting construction. The dropped cousin and long-range
collisions are exactly why the implication cannot be reversed.

## 4. Exact no-go at the physical activity

For the probability bound (1), the cube activity is

`
x=1/16.
`

A finite sibling-only majorant at the physical activity would require a finite
nonnegative value `t=T(x)` satisfying

`
t=(1/16)P5(t).                                          (6)
`

But from (3),

`
P5(t)-16t
 = 1 - t + 74t^2 + 154t^3 + 143t^4 + 49t^5.             (7)
`

Already

`
1-t+74t^2 > 0                                           (8)
`

for every real `t`, because its discriminant is

`
(-1)^2-4*74 = -295 < 0
`

and its leading coefficient is positive. The remaining terms in (7) are
nonnegative for `t>=0`. Hence

`
P5(t)>16t                                               (9)
`

for every `t>=0`.

Thus

`
(1/16)P5(t)>t
`

for every finite nonnegative `t`, contradicting (6).

Therefore:

`
boxed:
the sibling-only recursive majorant diverges at x=1/16.
`

Equivalently, no certificate of the form

`
z P5(q)<=q
`

exists even at `z=1/16`, let alone at `z=y/16` with `y>1`.

The preregistered dyadic search returned no certificate. Equation (7) explains
why exactly; the negative result is not a grid artefact.

## 5. What failed and what survived

What failed is **not** the absolute tree sum itself.

The recursive description in (4) ignores all collisions between cousins,
grandchildren on different branches and more distant descendants. Those
collisions can be extensive in four dimensions. The exact no-go says only
that retaining sibling compatibility is insufficient to exploit them.

What survives:

- every individual face-simple tree boundary still pays exactly
  `(1/2)16^(-k)` at the union-bound level;
- simple paths remain summable with ratio `15/16`;
- the previously controlled comb/corridor family remains summable with its
  stronger exact transfer estimate;
- the charge-faithful two-replica representation from draft #1167 is
  unaffected;
- no conclusion about the true embedded tree generating function changes.

The next viable absolute-polymer attack must remember more geometry than one
generation. A finite-memory grammar must at least see collisions between
children of adjacent parents, or otherwise impose a canonical corridor
decomposition whose off-corridor decorations are summed rather than counted
independently.

## 6. Exact audit

The verifier was frozen at

`
ea6d059ed3f7bf64b9cb05e1606583235df69856
`

before execution.

One Linux x86_64 / Python 3.13.5 run passed with exit code zero and empty
stderr. It derived (2) and (3) from cubical coordinates, verified the six
planted orientations, generated the recursive upper series through degree 12,
and executed the frozen certificate search.

The first rooted-description coefficients are

`
1,
18,
381,
9020,
229104,
6104058,
168340282,
4765055808,
137652453735,
4041954733588,
120286041826002,
3619888728570540.
`

They are coefficients of the deliberately enlarged recursive grammar, not
counts of actual embedded trees.

**Audit status:** candidate-C on one architecture.

**Written no-go:** candidate-T pending separate review.

Public Canon v92 is unchanged. `Xi_L`, `Xi_L^(2)` and P1 remain open.
