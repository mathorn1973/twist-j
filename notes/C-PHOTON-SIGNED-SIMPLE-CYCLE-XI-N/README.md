# Uniform signed-slice bound for controlled single current cycles

**PUBLIC, NON-CANONICAL.**
**Status:** candidate-T written derivation plus candidate-C one-architecture audit.
Owner: #1176.
Author: A. M. Thorn.
Date: 26 September 2026.
License: Apache-2.0.
Basis: Public Canon v92.

This note changes the object being paid for.

Earlier absolute component bounds charged the full neutral surface area. The
signed-slice quotient in `SIGNED-SLICES.md` instead depends only on the
integer primitive of the projected current. For a component whose current is
one simple cycle, that primitive has a direct geometric bound in terms of the
cycle itself.

The result is the first explicit volume-uniform bound on a nontrivial
all-distance subfamily of the signed moment `Xi_L`.

It is not a bound on all of `Xi_L`.

## 1. Setup

For one paired component `K`, write

`
B_K(r)=sum_(x:x1=r) J_K(e0(x)).
`

Choose an integer cyclic primitive

`
H_K(r)-H_K(r-1)=B_K(r).
`

The signed axial cost is

`
ell_K=min_(h in Z) sum_r |H_K(r)-h|.
`

The one-copy paired representation gives

`
Xi_L=(1/V) E_aug sum_(K charged) ell_K^2.
`

Retain only components whose current is exactly one unit simple current cycle
`gamma`. Such a cycle has zero winding because every component current
`J_K=partial eta_K/5` has zero total current in every periodic direction.

Let

`
m=|gamma|,
n0=# direction-0 edges of gamma,
n1=# direction-1 edges of gamma.
`

## 2. Deterministic signed-cycle lemma

### Candidate-T

For every such simple zero-winding cycle,

`
boxed: ell(gamma) <= n0*n1/4 <= m^2/16.                (1)
`

### Proof

Lift the zero-winding cycle from the torus to a closed nearest-neighbor path in
`Z^4`.

Let `d` be the range of its coordinate `x1` in that lift. To reach the
maximum from the minimum requires at least `d` positive direction-1 steps,
and returning requires at least `d` negative direction-1 steps. Hence

`
d<=n1/2.                                                (2)
`

The slice source `B_gamma` is the signed sum of the direction-zero edges at
each `x1` level. Therefore

`
sum_r |B_gamma(r)| <= n0.                               (3)
`

Since `B=Delta H` and `sum B=0`, the total upward variation of `H`
equals its total downward variation. Each equals one half of the total
variation. Thus

`
range(H) <= (1/2) sum_r |B(r)| <= n0/2.                 (4)
`

Choose the primitive constant equal to the value of `H` on the exterior
zero interval of the lifted axial support. Only the `d` slice intervals
between the first and last nonzero source can then contribute. Equations
(2)-(4) give

`
ell(gamma)
 <= d*range(H)
 <= (n1/2)(n0/2)
 = n0*n1/4.                                             (5)
`

Finally,

`
n0*n1 <= ((n0+n1)/2)^2 <= m^2/4,
`

which proves (1).

The inequality is sharp already for an axis-aligned rectangle of side lengths
`a,b`: then

`
n0=2a,
n1=2b,
ell=ab=n0*n1/4.
`

The quantity `ell` is therefore the relevant projected area rather than the
neutral filling area.

## 3. Rooting one current cycle

Let `Xi_simple,12(L)` be the part of `Xi_L` from components whose current
is one unit simple cycle and whose opposite-edge plaquette-contact count obeys

`
O(gamma)<=m/12.
`

For one such component,

`
sum_(positive edges e)
   1{e in supp J_K}/m
 =1.                                                     (6)
`

There are `4V` positive lattice edges. Summing (6), using translation and
hypercubic symmetry, gives

`
Xi_simple,12(L)
 =
 4 E_aug[
   sum_(single-cycle K through fixed e)
   ell_K^2/m_K
 ].                                                      (7)
`

At a one-copy charged edge there is exactly one five-block, hence exactly one
charged paired component owns that edge. If the component current is
`+gamma` or `-gamma`, then the full original current has that same value
on every edge of `gamma`. Other current edges are unrestricted.

Therefore the augmented event in (7) is contained in the full-measure source
event already bounded in `FULL-MEASURE.md`:

`
E_gamma union E_-gamma.
`

Using (1),

`
ell(gamma)^2/m <= m^3/256.
`

Hence

`
Xi_simple,12(L)
 <= (1/64) sum_(m>=4) m^3 W_m,                          (8)
`

where `W_m` is the existing sum of the two-orientation source-event
probabilities over the admitted simple cycles of length `m` through the
fixed edge.

No neutral surface geometry appears in (8).

## 4. Existing full-measure cycle estimate

The source calculation already proved in `FULL-MEASURE.md` gives, for
`O<=m/12`,

`
W_m <= A q^(m-1),                                      (9)
`

with

`
A=374125/1240029,
q=2472875/2480058<1.
`

These are exactly the previously published constants

`
A=2 r a tau,
q=a(1+6r)tau,
a=15625/177147,
r=41/25,
tau=73/70.
`

For the contact-free class `O=0`,

`
W_m <= A0 q0^(m-1),
A0=51250/177147,
q0=169375/177147<1.                                    (10)
`

Nothing is refitted here.

## 5. Uniform evaluated bounds

For `0<q<1`,

`
S3(q)
 =sum_(m=4)^infinity m^3 q^(m-1)
 =(1+4q+q^2)/(1-q)^4 -1-8q-27q^2.                      (11)
`

Combining (8)-(11) yields, for every admitted even finite torus,

`
boxed:
Xi_simple,12(L)
 <= C12
 = 19289287085600601415245438839426542724609375
   /48127709445264405068802290089074432.                (12)
`

For the contact-free subclass,

`
boxed:
Xi_simple,0(L)
 <= C0
 = 84154245507509267755507354736328125
   /12019566150064311590964767330304.                   (13)
`

The point of (12)-(13) is **uniformity**, not numerical sharpness. The
constants are very large because the previously proved contact-budget cycle
tail is close to critical and the deterministic conversion costs a cubic
length moment.

No volume, momentum or neutral-area factor occurs.

## 6. What this resolves

The long neutral connector obstruction does not by itself make the signed
moment diverge when the paired component carries only one controlled simple
current cycle.

Long distance is paid through the current cycle geometry:

`
neutral surface size -> discarded,
projected current area ell -> bounded by cycle length,
cycle length -> full-measure source tail.
`

This is exactly the cancellation the signed quotient was designed to retain.

The result also shows what the next obstruction actually is. A complete
uniform `Xi_L` bound now needs control of at least one of:

1. single simple cycles with `O>m/12`;
2. non-simple or branched integer current networks;
3. paired components containing several separate current cycles whose signed
   slice primitives can add coherently.

The surface size itself is no longer the right debt for the class closed here.

## 7. Audit

The verifier was frozen at

`
c74c6e56801bd508153b75522b294b9a22340bc7
`

before execution.

A Linux x86_64 / Python 3.13.5 exact run passed with empty stderr. It:

- reconstructed all cycle constants from the published primitive fractions;
- checked the cubic generating-series identity;
- enumerated 162 simple planar cycles through perimeter 12 and found no
  violation of (1);
- checked 36 rectangles up to `6 x 6`, all saturating the first inequality;
- evaluated (12) and (13) as exact reduced fractions.

The finite enumeration is an audit, not the proof of (1).

**Audit status:** candidate-C on one architecture.

Public Canon v92 is unchanged. Full `Xi_L`, `Xi_L^(2)`, `chi_L`, P1 and
the physical-photon obligations remain open.
