# Sign-sensitive contact extension of the uniform simple-cycle Xi bound

**PUBLIC, NON-CANONICAL.**
**Status:** candidate-T written derivation plus candidate-C one-architecture audit.
Owner: #1179.
Author: A. M. Thorn.
Date: 26 September 2026.
License: Apache-2.0.
Basis: Public Canon v92.

The coarse simple-cycle result used only the total number of opposite-edge
plaquette contacts. That throws away the most useful sign.

For a simple current cycle, an opposite-edge contact can either reinforce the
plaquette curl or cancel it. The already existing complex-source estimate
penalizes the cancellation case by `9/25`, rather than charging it by
`41/25`.

Keeping that distinction strictly enlarges the class of simple cycles whose
signed-slice contribution is uniformly bounded.

## 1. Existing sign-sensitive source estimate

At the fixed source choice `h=log 3`, write

`
a=15625/177147,
r=41/25,
s=9/25.
`

For a unit simple cycle `gamma) of length `m`, right-angle count `c`,
and signed opposite-contact counts `O_+,O_-`, the existing full-measure
source estimate is

`
C_gamma <= a^m r^(c+O_+) s^(O_-).                       (1)
`

Here `O_+` are reinforcing opposite contacts and `O_-` are canceling
contacts.

Freeze

`
tau=73/70.
`

Define

`
SC={gamma: r^(O_+) s^(O_-) <= tau^m}.                  (2)
`

## 2. The previous contact class is contained in SC

The public note already proves

`
s<r,
tau^12>r.
`

If

`
O_+ + O_- <= m/12,
`

then

`
r^(O_+)s^(O_-)
 <= r^(O_++O_-)
 <= r^(m/12)
 < tau^m.
`

Thus every previously controlled simple cycle is in `SC).

This uses no probabilistic assumption and no finite census.

## 3. The inclusion is strict

Consider the oriented ten-edge cycle

`
(0,0,0)
(1,0,0)
(1,0,1)
(0,0,1)
(0,1,1)
(0,1,0)
(1,1,0)
(1,1,-1)
(0,1,-1)
(0,0,-1)
(0,0,0).
`

It is simple and has zero winding.

Direct oriented plaquette incidence gives

`
O_+=2,
O_-=1.
`

The three contacts are:

- the two x-edges at z=0 and z=1, reinforcing;
- the two x-edges at y=0 and y=1, canceling;
- the two x-edges at y=1, z=0 and z=-1, reinforcing.

Hence

`
O=3,
m=10,
12O=36>10.
`

The old budget `O<=m/12` fails strongly.

But its signed factor is

`
r^2 s
=(41/25)^2(9/25)
=15129/15625
<1
<tau^10.
`

Therefore this cycle belongs to `SC). The extension is strict.

## 4. The cycle sum is unchanged

The contact-free weighted nonbacktracking factor already proved in the source
note is

`
q0=a(1+6r)=169375/177147.
`

For every `gamma in SC`, (1)-(2) give

`
C_gamma <= a^m r^c tau^m.
`

The same one-straight plus six-turn sum therefore yields

`
W_m^(SC) <= A q^(m-1),                                  (3)
`

with

`
A=2 r a tau=374125/1240029,
q=q0 tau=2472875/2480058<1.
`

No new path-counting constant is used. The same constants control a larger
cycle class because the negative contacts were previously thrown away.

## 5. Signed-slice consequence

Use the candidate-T deterministic lemma from #1176:

`
ell(gamma)^2/m <= m^3/256.
`

Rooting one simple current cycle at a positive current edge gives

`
Xi_simple,SC(L)
 <= (1/64) sum_(m>=4) m^3 W_m^(SC).
`

Together with (3),

`
boxed:
Xi_simple,SC(L)
 <= C_SC
`

for every admitted even finite volume, where

`
C_SC =
19289287085600601415245438839426542724609375
/
48127709445264405068802290089074432.
`

This is numerically the same deliberately coarse rational as in #1176, but it
now controls a strictly larger all-distance class.

## 6. What remains

The unresolved simple-cycle complement is exactly

`
r^(O_+) s^(O_-) > tau^m.                               (4)
`

Because `s=9/25<1`, only contact patterns with insufficient canceling
contacts can lie in (4). The dangerous object is therefore no longer
"many contacts". It is **an excess of reinforcing contacts after subtracting
the strong canceling-contact credit**.

This is a sharper target than the old condition `O>m/12`.

Still outside scope are non-simple or branched current networks, several
current cycles inside one paired surface component, full `Xi_L`,
`Xi_L^(2)`, `chi_L`, P1 and the physical-photon program.

## 7. Audit

The successor verifier was frozen at

`
af41b8321c83e0ce815005cb96f30a4ff18a5001
`

before execution.

The one-architecture exact audit:

- reconstructed every rational source constant;
- checked the coarse-to-signed implication on 18,707 exact integer test cases;
- derived the three witness contacts from oriented plaquette incidence;
- obtained exactly `O_+=2,O_-=1`;
- checked the strict-extension inequalities;
- reproduced the exact `C_SC` fraction.

The exhaustive predecessor #1178 timed out and remains separately preserved.
No result from its incomplete census is used here.

Public Canon v92 is unchanged.
