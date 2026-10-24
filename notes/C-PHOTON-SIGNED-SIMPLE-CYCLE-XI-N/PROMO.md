# PROMO-C-PHOTON-SIGNED-SIMPLE-CYCLE-XI-N

**NON-CANONICAL review package. No promotion is performed here.**
Owner: #1176.
Basis: Public Canon v92.

## Candidate statement

For the one-copy paired photon representation, the contribution to the signed
slice moment from components carrying exactly one unit simple current cycle
with opposite-edge contact count `O<=m/12` is bounded uniformly in finite
volume by an explicit rational constant.

The key new deterministic lemma is

`
ell(gamma)<=n0*n1/4<=m^2/16.
`

It converts neutral-area control into projected-current geometry.

Together with the already published full-measure cycle estimate,

`
W_m<=A q^(m-1),
A=374125/1240029,
q=2472875/2480058,
`

this yields the exact volume-uniform bound recorded in `README.md`.

## Evidence

- preregistration: `PREREG.md`
- frozen verifier pin:
  `c74c6e56801bd508153b75522b294b9a22340bc7`
- exact run: `RUN.md`
- written proof: `README.md`
- disposition: `RESULT.md`

## Remaining frontier

Do not spend effort sharpening the enormous rational constant yet. It cannot
close P1 numerically.

The structural next target is the complement:

1. classify or sum simple cycles with `O>m/12`, preferably using their
   signed opposite-contact type `O_+,O_-`;
2. then treat multiple current cycles in one paired component without
   reverting to neutral surface area.

The sign-sensitive source estimate already gives the local factor

`
(41/25)^(O_+) (9/25)^(O_-).
`

That split is the natural next attack because cancellation-type opposite
contacts are strongly suppressed while reinforcing contacts are the remaining
dangerous ribbon geometry.

No Canon, full-Xi, P1 or phase promotion is proposed.
