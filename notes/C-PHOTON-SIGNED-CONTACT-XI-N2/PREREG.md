# PREREG: C-PHOTON-SIGNED-CONTACT-XI-N2

**PUBLIC, NON-CANONICAL. No Canon authority.**
Author: A. M. Thorn <thorn@twistj.com>
Date: 26 September 2026
License: Apache-2.0
Owner issue: #1179
Branch: `notes/photon-signed-contact2-20260926`

## 1. Basis

Public Canon v92 is the sole authority.

- activation/tag target: `8b1132d828d94f83e653dab34d686a7e68394939`
- content commit: `d7eb6de16c11f6a105996de02ffd7afa32683a93`
- Canon SHA-256: `31783fcd8e5ad2a697efd92a6d9fb92c2a21c101b95b9c282ea50fa7cb245f68`
- Canon bytes: `797365`

Scientific inputs:

1. public-main `FULL-MEASURE.md`, sign-sensitive simple-cycle source bound;
2. #1176 / draft PR #1177 only at its declared NON-CANONICAL candidate scope.

Consumed predecessor: #1178 timed out before producing scientific stdout.
Nothing from that finite census is used.

## 2. Signed-contact class

For one unit simple zero-winding current cycle `gamma` of length `m`, use
the exact contact split already defined in `FULL-MEASURE.md`:

- `O_+`: opposite edges in one plaquette have equal signed incidence;
- `O_-`: their signed incidences cancel.

At `h=log 3`, the existing source bound is

`
C_gamma <= a^m r^(c+O_+) s^(O_-),
a=15625/177147,
r=41/25,
s=9/25.                                                 (S1)
`

Freeze

`
tau=73/70
`

and define

`
SC = {gamma: r^(O_+) s^(O_-) <= tau^m}.                (SC)
`

The candidate-T inclusion is

`
O_+ + O_- <= m/12  =>  gamma in SC.                     (I)
`

It follows only from `s<r` and the already published exact inequality
`tau^12>r`.

## 3. Source/path consequence

The contact-free weighted path factor is already fixed:

`
q0=a(1+6r)=169375/177147.
`

For `gamma in SC`,

`
C_gamma <= a^m r^c tau^m.
`

Thus the existing one-straight plus six-turn path count gives, for every
`m>=4`,

`
W_m^(SC) <= A q^(m-1),
A=2 r a tau=374125/1240029,
q=q0 tau=2472875/2480058<1.                             (W)
`

No new path entropy constant is introduced.

## 4. Signed-slice consequence

Use the #1176 candidate-T deterministic lemma

`
ell(gamma)^2/m <= m^3/256.
`

Edge rooting then gives, for `Xi_simple,SC(L)`, the contribution to the
one-copy signed moment from paired components whose current is exactly one
unit simple cycle in `SC`,

`
Xi_simple,SC(L)
 <= (A/64) sum_(m>=4) m^3 q^(m-1)
 = C_SC,                                                (X)
`

where the frozen exact value is

`
C_SC =
19289287085600601415245438839426542724609375
/
48127709445264405068802290089074432.
`

This is the same numerical constant as the coarse `O<=m/12` class but
applies to the larger signed-contact class.

## 5. Frozen strict-extension witness

The verifier must use this exact oriented simple cycle:

`
v0=(0,0,0)
v1=(1,0,0)
v2=(1,0,1)
v3=(0,0,1)
v4=(0,1,1)
v5=(0,1,0)
v6=(1,1,0)
v7=(1,1,-1)
v8=(0,1,-1)
v9=(0,0,-1)
v10=v0.
`

It must derive the ten canonical current edges from these vertices and compute
contact signs from the oriented plaquette boundary, not from hard-coded
contact labels.

Frozen expected witness:

`
m=10,
O_+=2,
O_-=1.
`

Therefore

`
O=3,
12 O =36 >10,
`

so the old coarse budget fails.

But

`
r^2 s
=(41/25)^2(9/25)
=15129/15625
<1
<tau^10,
`

so the cycle lies in `SC`.

## 6. Prospective exact audit

Before execution, commit and publicly read back this file and `verify.py`.

The standard-library verifier must use only integers and `Fraction` and:

1. reconstruct `a,r,s,tau,q0,A,q`;
2. verify `s<r`, `tau^12>r`, `q<1`;
3. verify the algebraic implication (I) by exact symbolic integer inequalities
   rather than finite cycle enumeration;
4. verify the fixed witness is closed, simple and unit-step;
5. derive its canonical edge coefficients;
6. derive all opposite-edge contacts from plaquette incidence and obtain
   exactly `O_+=2,O_-=1`;
7. verify the exact strict-extension inequalities above;
8. reconstruct `C_SC` from the cubic generating series and compare it to the
   frozen fraction;
9. print scope boundaries.

No exhaustive cycle enumeration, floating point, randomness, fitted threshold
or adaptive search is admitted.

## 7. Status and boundary

A successful audit is at most candidate-C. The written inclusion, source/path
sum and uniform signed-moment bound are candidate-T pending review.

The unresolved complement of simple cycles is exactly

`
r^(O_+) s^(O_-) > tau^m.
`

Still outside scope are non-simple/branched current networks, multi-cycle
paired components, full `Xi_L`, `Xi_L^(2)`, `chi_L`, P1, massless phase
and physical photon.

No Canon, Registry, Frontier, probe, tool, workflow or release file changes.
