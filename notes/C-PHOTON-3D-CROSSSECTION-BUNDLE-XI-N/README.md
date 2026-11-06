# Uniform signed Xi bound for arbitrary 3D cross-section prism bundles

**PUBLIC, NON-CANONICAL.**
**Status:** candidate-T written derivation plus candidate-C one-architecture audit.
Owner: #1190.
Author: A. M. Thorn.
Date: 26 September 2026.
License: Apache-2.0.
Basis: Public Canon v92.

This note removes the planarity restriction from the product-bundle program.

The cross-section may now be any simple even lattice polygon in the full
three-dimensional lattice orthogonal to one straight base axis. Extra
nearest-neighbor chord contacts are allowed.

## 1. Geometry

Let the cross-section have even length `k>=4` and the straight prism length
be `D>=1`.

The assembled alternating cycle has

`
m=k(D+1),
c=2k.
`

Let `E_Q` be the number of all nearest-neighbor pairs among cross-section
vertices. The cubic-lattice induced graph has degree at most six, so

`
E_Q<=3k.
`

Every such pair creates one reinforcing parallel-strand contact on every base
edge:

`
O_+^(strand)=D E_Q<=3kD.
`

At either endpoint, the selected connector-edge contact graph has degree at
most four, hence at most `k` contact pairs. Therefore

`
O^(connector)<=2k.
`

Pessimistically charging every connector contact as reinforcing gives

`
c+O_++O_-<=3kD+4k.                                    (1)
`

## 2. Exact source and entropy

Use `h=log2`:

`
a=15625/131072,
r=34/25,
s=16/25.
`

For one fixed bundle description, including both current signs,

`
P(E_gamma union E_-gamma)
 <=2a^[k(D+1)]r^[3kD+4k].                             (2)
`

A rooted nonbacktracking cross-section description in `Z^3` has at most six
first choices and five later choices.

Set

`
a r^3=4913/16384<1,
q4=(a r^3)^4
  =582622237229761/72057594037927936<1,
`

and

`
b3=5a^2r^7
  =410338673/671088640<1.                              (3)
`

Thus length and three-dimensional cross-section entropy are both summable.

## 3. Signed moment

Using the candidate signed-cycle lemma

`
ell^2<=m^4/256,
`

the rooted description sum gives

`
Xi_3D_bundle(L)
 <=(3/40)
   [sum_(even k>=4)k^4b3^k]
   [sum_(D>=1)(D+1)^4q4^(D-1)].                       (4)
`

The two exact generating functions are the same elementary fourth-moment
series used in the planar case. Hence

`
boxed:
Xi_3D_bundle(L)<=C_3D
`

uniformly in every admitted finite volume, with

`
C_3D=
416111769351155706070895686830876801103138788170283618286216649193431878890383774432994992129503634668171136834991156398402287791533817104721964500733667707895377665906779672
/
810346186280159622950128642014436246076173224046581600732070223656100332631630378613650246835347252680870452600695509050882158368173859139023151286705714420762315673828125.
`

Again, finiteness and volume independence are the relevant statements, not
numerical sharpness.

## 4. Exact geometry audit

The frozen verifier constructed 18 explicit four-dimensional prism cycles,
using base lengths one through six and three cross-sections:

- a planar square;
- a genuinely nonplanar six-edge polygon spanning all three cross-section
  dimensions;
- a genuinely nonplanar eight-edge polygon with additional nearest-neighbor
  chords beyond the polygon edges.

For every example it derived the actual current edges, turns, reinforcing and
canceling contacts, cross-section nearest-neighbor count, connector contacts
and axial primitive `ell`.

All declared inequalities passed exactly.

## 5. Meaning and boundary

The controlled high-contact regime is now broader than planar product bundles.
A whole arbitrary 3D cross-section may fluctuate while one straight base
direction generates the strands.

This still does not cover arbitrary simple cycles. The remaining simple-cycle
debt is geometry that cannot be represented as a straight prism over one
cross-section, together with bent or changing cross-sections.

Non-simple networks, multi-cycle components, full `Xi_L`, `Xi_L^(2)`, P1
and the massless phase remain open.

Public Canon v92 is unchanged.
