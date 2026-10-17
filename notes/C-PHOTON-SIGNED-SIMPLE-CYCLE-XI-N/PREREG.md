# PREREG: C-PHOTON-SIGNED-SIMPLE-CYCLE-XI-N

**PUBLIC, NON-CANONICAL. No Canon authority.**
Author: A. M. Thorn <thorn@twistj.com>
Date: 26 September 2026
License: Apache-2.0
Owner issue: #1176
Branch: `notes/photon-signed-simple-cycle-20260926`

## 1. Public basis

Public Canon v92 is the sole authority.

- activation/tag target:
  `8b1132d828d94f83e653dab34d686a7e68394939`
- content commit:
  `d7eb6de16c11f6a105996de02ffd7afa32683a93`
- Canon SHA-256:
  `31783fcd8e5ad2a697efd92a6d9fb92c2a21c101b95b9c282ea50fa7cb245f68`
- Canon bytes: `797365`

Mathematical dependencies are limited to the existing NON-CANONICAL public
notes on main:

- `notes/C-PHOTON-BCHI-DIRECT-BOUND-N/SIGNED-SLICES.md`
- `notes/C-PHOTON-BCHI-DIRECT-BOUND-N/FULL-MEASURE.md`

No draft branch is an authority dependency.

## 2. Scoped signed-slice contribution

Retain the one-copy paired augmentation and

`
Xi_L=(1/V) E_aug sum_(K charged) ell_K^2.
`

Define `Xi_simple,12(L)` by retaining only paired components `K` whose
integer current `J_K` is exactly one unit simple current cycle `gamma`
and whose number `O(gamma)` of opposite-edge plaquette contacts satisfies

`
O(gamma) <= |gamma|/12.
`

"Unit" means every nonzero current edge has magnitude one. "Simple" means the
cycle visits no vertex twice except the closing vertex. Since each `J_K` is
an integer boundary current with zero total winding in every direction, such a
cycle has zero winding.

A separate contact-free subquantity `Xi_simple,0(L)` uses `O=0`.

This item asks only for explicit volume-uniform upper bounds on those two
subquantities.

## 3. Frozen deterministic lemma

For one unit simple zero-winding cycle `gamma`, let

- `m=|gamma|` be total length;
- `n0` be its number of direction-zero edges;
- `n1` be its number of direction-one edges;
- `B_gamma(r)` be the signed sum of direction-zero current edges in axial
  slice `r`;
- `H_gamma` be any integer cyclic primitive of `B_gamma`;
- `ell(gamma)=min_h sum_r |H_gamma(r)-h|`.

Freeze the intended lemma

`
ell(gamma) <= n0*n1/4 <= m^2/16.                       (D1)
`

The written proof must use only:

1. zero winding to lift the cycle to a closed path in `Z^4`;
2. axial span `d<=n1/2`;
3. `TV(H)=sum_r |B(r)|<=n0`;
4. because `sum B=0`, upward and downward variation are both
   `TV(H)/2`, so `range(H)<=TV(H)/2`;
5. choose the constant value of `H` outside the lifted axial support.
   At most `d` slice intervals can then be nonconstant, giving
   `ell<=d*range(H)<=n0*n1/4`;
6. AM-GM:
   `n0*n1<=((n0+n1)/2)^2<=m^2/4`.

No finite enumeration is used as the proof of (D1).

## 4. Frozen edge-rooting step

For a single-cycle component of length `m_K`,

`
sum_(positive lattice edges e) 1{e in supp J_K}/m_K = 1.
`

There are exactly `4V` positive edges. Hypercubic symmetry gives the same
source bound for any fixed positive edge.

Hence

`
Xi_simple,12(L)
 <= 4 sum_(gamma through fixed e, O<=m/12)
      [ell(gamma)^2/m] P_mu(E_gamma union E_-gamma).    (M1)
`

The implication used here is frozen: if the augmented component current is
`+-gamma`, then on every edge of `gamma` the full original current has
that same value, because one one-copy charged edge contains exactly one
five-block and belongs to exactly one charged paired component. Other currents
outside `gamma` remain unrestricted. Therefore the augmented event is a
subset of the already defined full-measure source event
`E_gamma union E_-gamma`.

Using (D1),

`
ell(gamma)^2/m <= m^3/256,
`

so

`
Xi_simple,12(L)
 <= (1/64) sum_(m>=4) m^3 W_m,                         (M2)
`

where `W_m` is the existing full-measure sum of source-event probabilities
over admitted simple cycles of length `m` through the fixed edge.

## 5. Frozen existing cycle constants

No path constant is rediscovered here.

For `O<=m/12`, use exactly the consequence of FULL-MEASURE section 11:

`
W_m <= A q^(m-1),  m>=4,
A = 374125/1240029,
q = 2472875/2480058.                                   (C12)
`

These are exactly

`
A = 2*r*a*tau,
q = a*(1+6*r)*tau
`

for the already published
`a=15625/177147`, `r=41/25`, `tau=73/70`.

For the contact-free class use

`
W_m <= A0 q0^(m-1),
A0 = 51250/177147,
q0 = 169375/177147.                                    (C0)
`

## 6. Frozen evaluated bounds

Define for `0<q<1`

`
S3(q)=sum_(m=4)^infinity m^3 q^(m-1)
     =(1+4q+q^2)/(1-q)^4 - 1 - 8q - 27q^2.             (S)
`

The candidate-T conclusions are

`
Xi_simple,12(L) <= C12 := (A/64) S3(q)                 (B12)
`

and

`
Xi_simple,0(L) <= C0 := (A0/64) S3(q0).                (B0)
`

for every admitted even finite volume.

The exact fractions `C12` and `C0` are to be printed by the verifier.
No decimal is part of the theorem.

## 7. Prospective exact audit

Before the first scientific run, commit and publicly read back this file and
`verify.py`.

The standard-library verifier must use only integers and `Fraction` and
must:

1. reconstruct `A,q,A0,q0` from the published primitive constants and compare
   them to the frozen fractions above;
2. prove the rational identity (S) algebraically by checking the standard
   generating-function numerator after clearing denominators;
3. compute exact `C12,C0`;
4. enumerate all simple zero-winding lattice cycles in a fixed two-dimensional
   box with perimeter at most 12, modulo only cyclic start and reversal for
   duplicate removal, and check (D1) directly on every enumerated cycle;
5. explicitly check rectangles `a x b` for `1<=a,b<=6`, including the
   equality case `ell=ab=n0*n1/4`;
6. print scope boundaries.

The finite cycle enumeration audits (D1); it does not prove it.

Any assertion failure, exception, timeout, nonzero exit or nonempty stderr
fails the audit and is preserved.

## 8. Status and boundary

A successful finite audit is at most candidate-C. The written derivations
(D1), (M1)-(M2), and (B12)-(B0) are candidate-T pending separate review.

This item does **not** bound:

- simple cycles with `O>m/12`;
- non-simple current circuits;
- integer current networks with branching;
- a paired component containing two or more current cycles;
- the full `Xi_L` or `Xi_L^(2)`;
- the full susceptibility `chi_L`;
- P1, a massless phase, a physical photon or any apparatus statement.

No Canon, Registry, Frontier, probe, tool, workflow or release file changes.
