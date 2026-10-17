# PREREG: C-PHOTON-SIGNED-CONTACT-XI-N

**PUBLIC, NON-CANONICAL. No Canon authority.**
Author: A. M. Thorn <thorn@twistj.com>
Date: 26 September 2026
License: Apache-2.0
Owner issue: #1178
Branch: `notes/photon-signed-contact-20260926`

## 1. Basis

Public Canon v92 is the sole authority.

- activation/tag target: `8b1132d828d94f83e653dab34d686a7e68394939`
- content commit: `d7eb6de16c11f6a105996de02ffd7afa32683a93`
- Canon SHA-256: `31783fcd8e5ad2a697efd92a6d9fb92c2a21c101b95b9c282ea50fa7cb245f68`
- Canon bytes: `797365`

Mathematical inputs only:

1. public-main `FULL-MEASURE.md`, sign-sensitive simple-cycle source inequality;
2. #1176 / draft PR #1177, only at its declared NON-CANONICAL
   candidate-T deterministic signed-slice lemma.

No Canon statement is imported from a draft.

## 2. Signed contact class

For a unit simple zero-winding current cycle `gamma` of length `m`, let

- `c(gamma)` be its right-angle turn count;
- `O_+(gamma)` count opposite edge pairs on one plaquette whose two
  current coefficients give equal signed plaquette incidence;
- `O_-(gamma)` count opposite edge pairs whose signed incidences cancel.

The existing source estimate at `h=log 3` is

`
C_gamma
 <= a^m r^(c+O_+) s^(O_-),
a=15625/177147,
r=41/25,
s=9/25.                                                 (S1)
`

The existing contact-free weighted path entropy is

`
q0=a(1+6r)=169375/177147.
`

Freeze

`
tau=73/70
`

and define the signed-contact class `SC` by

`
r^(O_+) s^(O_-) <= tau^m.                               (SC)
`

## 3. Relation to the old contact budget

The written proof must establish

`
O_+ + O_- <= m/12  =>  gamma in SC.                      (I1)
`

Use only the already published exact inequalities

`
s<r,
tau^12>r.
`

Indeed, for `O=O_++O_-`,

`
r^(O_+)s^(O_-) <= r^O
                <= r^(m/12)
                < tau^m.
`

Thus `SC` contains the whole earlier class, possibly strictly.

## 4. Weighted cycle sum

For every cycle in `SC`, (S1) gives

`
C_gamma <= a^m r^c tau^m.
`

The existing nonbacktracking weighted count has one straight continuation and
six turns, so without introducing any new path constant,

`
sum_(gamma through fixed positive edge, |gamma|=m, gamma in SC)
 P(E_gamma union E_-gamma)
 <= A q^(m-1),                                          (W)
`

where

`
A=2 r a tau=374125/1240029,
q=q0 tau=2472875/2480058<1.
`

This is exactly the same `A,q` as the coarse `O<=m/12` estimate, but the
admitted cycle class is larger.

## 5. Signed-slice consequence

Use the #1176 deterministic lemma only at candidate scope:

`
ell(gamma)^2/m <= m^3/256.
`

With the same edge-rooting argument, define `Xi_simple,SC(L)` as the
contribution to `Xi_L` from paired components whose current is exactly one
unit simple cycle in `SC`. Then the intended candidate-T conclusion is

`
Xi_simple,SC(L)
 <= (A/64) sum_(m>=4) m^3 q^(m-1)
 = C12,                                                 (X)
`

with the same exact rational `C12` already audited in #1176:

`
C12 =
19289287085600601415245438839426542724609375
/
48127709445264405068802290089074432.
`

This bound is volume-uniform.

## 6. Prospective exact audit

Before the first scientific execution, commit and publicly read back this file
and `verify.py`.

The verifier must use standard library integer/Fraction arithmetic only and:

1. reconstruct `a,r,s,tau,q0,A,q` and verify all frozen fractions;
2. verify `s<r`, `tau^12>r`, and `q<1` exactly;
3. enumerate all simple zero-winding cycles in `Z^3` of lengths
   `4,6,8,10,12`, rooted at the origin, with duplicates removed only by
   cyclic start, reversal and translation, not by rotations/reflections;
4. compute `O_+,O_-` directly from current edge coefficients and opposite
   plaquette incidence;
5. check (I1) on every enumerated cycle;
6. count how many enumerated cycles satisfy `SC`;
7. search the frozen census for an actual strict-extension witness with
   `12(O_++O_-)>m` but (SC) true; if absent, print a diagnostic but do not
   fail the theorem;
8. verify the exact `C12` arithmetic;
9. print explicit scope boundaries.

The finite census audits the contact classification. It does not prove (W).

## 7. Status and boundary

A successful finite audit is at most candidate-C. The written implication
(I1), weighted sum (W), and uniform bound (X) are candidate-T pending review.

No claim is made that `SC` contains every simple cycle. The unresolved
single-cycle complement is exactly

`
r^(O_+) s^(O_-) > tau^m.
`

Also still outside scope:

- non-simple or branched current networks;
- paired components containing multiple current cycles;
- full `Xi_L` or `Xi_L^(2)`;
- full susceptibility, P1, massless phase or physical photon.

No Canon, Registry, Frontier, probe, tool, workflow or release file changes.
