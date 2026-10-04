# Independent static review of the connected-response note

**NON-CANONICAL; analytical review only.** Date: 2026-10-05.
Three separately delegated agents reviewed the mathematical and physical
arguments. They read the actual README.md and CALIBRATION.md; they did not
execute a scientific program, simulate a pulse sequence, inspect laboratory
data or reproduce the user's unavailable calculation package. This review
does not promote a public claim or constitute a public preregistered run.

## Findings

The mathematical review and the separately assigned independent check
confirmed by hand:

- The source branches give the displayed checkpoint tuples.
- Expansion of the raw-loop generator and the four-setting subtraction
  give 2*kappa*lambda^2*g_k*a_m*a_x with the stated phase convention.
- The inherited intensity and B normalization give pi*sign(g_k)*Z_k/50;
  |Z_k|<=1 is sufficient for the principal-phase bound.
- Under a1*a2*(a1-a2)!=0, every affine four-vector reading vanishes on the
  checkpoint family. The argument remains valid for arbitrary real,
  profile-dependent but fixed coefficients. It does not force every
  coefficient or the global observable to vanish.
- The further resonance/degeneracy restrictions are necessary conditions,
  and the explicitly target-fitted exceptional profile gives the stated
  nonzero finite sequences. It prevents an all-profile overclaim.

The physical review and the independent check confirmed that the displayed
Ramsey preparation and analysis pulses give
p0(alpha)=[1+cos(Delta-alpha)]/2. The ideal response, a conditional detector
effect, and a Hodge decoder are kept distinct. Direct level readout uses
joint-shot products; no unprovided nondemolition property or free measurement
ancilla is assumed.

The physical reviewer requested two wording corrections, incorporated in
CALIBRATION.md: the phase reference is an equal-duration LS-off traversal
with the laboratory/free phase retained or compensated; the required joint
level measurement concerns the seven specified ions in the seventeen-ion
apparatus, not an unnecessary measurement of all seventeen ions.

## Remaining boundary

No calibrated d_j, geometry, detector instrument, error bars, native
continuation pulse word or target-independent four-dimensional decoder is
supplied. The phase bound is not an error budget. Exact nondegeneracy must
not be inferred from noisy nominal estimates, and uncertain degeneracy
must not be treated as a verified exceptional solution.

The response derivation is target-independent in its formula and physical
calibration rule; the comparison table and Hodge target were already exposed.
The result is an analytical obstruction for the stated affine class, not
a successful physical realization or a held-out prediction.

No substantive mathematical correction remained after the static review.
