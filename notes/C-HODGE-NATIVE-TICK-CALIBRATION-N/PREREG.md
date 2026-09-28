# C-HODGE-NATIVE-TICK-CALIBRATION-N: prospective contract

Status: PUBLIC NON-CANONICAL.
Owner: A. M. Thorn / hodge-native-tick-calibration-20260928; issue #1257.
Basis: Public Canon v92, main d725b9d55cb7d9a758bc184b4553fa42afe87933.

## Frozen inherited inputs

METRO-TICK [T] fixes the dimensionless tick

    T = 2 pi / 5.

TIME-CUT-READING [D] permits the selected reading of one native counter update
as one proper-time tick, without uniqueness or completeness.

The correctly typed Hodge event frame is

    g_frame=diag(a1,a2,a3,-ct),

    a1=2sqrt5/5,
    a2=6sqrt5/5,
    a3=3sqrt5/2,
    ct=(2+sqrt5)/8.

For every integer h>=3, C-HODGE-EVENT-CAUCHY-N selects the ideal event grid

    y_h(m,z)=h^-1(m t + sum_i z_i s_i)

and actual rounded events e_h(m,z) satisfying

    ||e_h(m,z)-y_h(m,z)||_* <= R0/h^4,
    R0=10-9sqrt5/5.

Pinned bytes:
- notes/C-NATIVE-HODGE-METRIC-SEAM-N3/PROOF.md
  SHA256 2f27776ceb851774e0b026b274b446605c8b480ed90fa4f57ede22ce13be742d
- notes/C-HODGE-EVENT-CAUCHY-N/PROOF.md
  SHA256 6ebac7c63bcadba55791db017d273aa2136cdbf8867a72b3006c1d46bae823af
- notes/C-HODGE-EVENT-CAUCHY-N/model.py
  SHA256 adc99adac6ff1e3d9e76d4952b97af16fcdbe919021c5947bdb6c0feb7b3a772
- reproduce/coupling-metrology/verify.py
  SHA256 8b203f9c4885a9f70b4460ded55d884529989cd244a3f0acbdcae9a8de053566
- reproduce/coupling-metrology/README.md
  SHA256 ad9bb19d32d844847a8820ff9d67650c3e914427780c2001aae54ee4e78a1c5b

## G1: selected ideal tick seam

As candidate-D only, identify one native counter update with one IDEAL event
step m->m+1 at fixed z and require its dimensionless proper time to be T.
Since its inherited squared interval is -ct/h^2, this uniquely fixes

    lambda_h = T^2 h^2 / ct.

No SI unit or physical-clock realization is asserted.

## G2: resolution cancellation

Pull lambda_h g_frame back to integer label increments
(dm,dz1,dz2,dz3). Prove exactly

    g_tick =
      T^2 diag(a1/ct,a2/ct,a3/ct,-1),

independent of h. Equivalently its spatial coefficients are T^2/alpha_i
for the inherited scalar stencil alpha_i=ct/a_i.

Thus this selected tick seam fixes an exact dimensionless label metric but
does NOT select the event resolution h. h and lambda_h trade exactly.

## G3: exact coefficients

Prove

    a1/ct = 16(5-2sqrt5)/5,
    a2/ct = 48(5-2sqrt5)/5,
    a3/ct = 12(5-2sqrt5),

all positive, with Lorentz signature (3,1).

## G4: actual rounded-event interval bound

For a same-z actual edge

    Delta=e_h(m+1,z)-e_h(m,z),

write Delta=t/h+eta. The two endpoint rounding bounds give

    ||eta||_* <= epsilon_h = 2R0/h^4.

Decompose eta=tau t+s with |tau|<=epsilon_h and
g(s,s)<=ct epsilon_h^2. Use t orthogonal to the spatial frame to prove

    |g(Delta,Delta)+ct/h^2|
      <= ct(4R0/h^5+8R0^2/h^8).

After selected calibration,

    |lambda_h g(Delta,Delta)+T^2|
      <= T^2(4R0/h^3+8R0^2/h^6).

This is uniform in m,z. It proves convergence of SQUARED tick intervals,
not exact finite-h equality.

## G5: exact finite-resolution obstruction

At h=3 prove the exact actual intervals

    g(e_3(1,0)-e_3(0,0), same)
      = -398/6561,

and, with z=(1,0,0),

    g(e_3(2,z)-e_3(1,z), same)
      = -1861/32805 + sqrt5/32805.

They differ. Therefore no single positive global conformal factor can make
both actual h=3 edges equal to one prescribed nonzero squared tick.

This is only an h=3 obstruction, not an all-h theorem.

## G6: three clocks

Keep distinct:
- native update counter n;
- selected geometric event index m;
- N2 generative archive counter N.

This candidate selects n=m only in the ideal tick dictionary. It does not
identify N with either and does not strengthen TIME-CUT-READING.

## G7: boundaries

No METRO-EDGE-SCALE closure, SI, occurrence, curvature, photon cone, Galois
physical selection or L6 measure. Actual rounded events converge toward the
ideal tick calibration but are not promoted to exact finite-resolution clocks.

Only this new notes directory may be added. No Canon, Registry, Frontier,
public gate, workflow, tool or predecessor edits.

Commit and publicly read back PREREG.md and verify.py before execution.
Universal conclusions require PROOF.md. Finite exact checks are corroboration.
Runtime/integrity failure is STOP.
