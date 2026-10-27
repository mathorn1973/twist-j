# Result: fixed-input relative capture probability

Status: `C` / exact bounded audit reproduced on both architectures; NON-CANONICAL.
Outcome: `RELATIVE-CAPTURE-PROFILE-ENCLOSED`.
Action layer: L1 only.
Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

## Computed observable

The table encloses the complete asymptotic joint probability ratio
`P_win(p)/P_win(0)` for the one frozen capture-and-record law and the
prescribed normalized source family. The momentum window half-width is
`1/1000`; the total-energy window is fixed at `8*pi/5 +/- 1/1000`.
The token starts at zero and the receiver remains at 100. The outgoing
bound/pulse/record event and full `F1,F2` resolvents remain unchanged.

Here `p` is the center of the incoming pair-center-momentum window,
not its exact mean and not conserved total pair/carrier momentum.
The spectrum-selected source is normalized by its declared formula;
this is not an arbitrary rigid translation of a fixed wave packet.

Every printed decimal below is an exact terminating form of the rational
endpoint in `EXPECTED.txt`, rounded outwards by the pinned verifier.
The interval encloses the finite-width packet probability ratio; it is
not a statistical confidence interval or a point-energy approximation.

| Window center `p` | Lower bound | Upper bound |
|---:|---:|---:|
| 0.000 | 1.000000 | 1.000000 |
| 0.100 | 0.998116 | 0.998135 |
| 0.200 | 0.992445 | 0.992505 |
| 0.300 | 0.982903 | 0.983035 |
| 0.400 | 0.969354 | 0.969587 |
| 0.500 | 0.951593 | 0.951962 |
| 0.600 | 0.929341 | 0.929884 |
| 0.700 | 0.902226 | 0.902985 |
| 0.800 | 0.869752 | 0.870779 |
| 0.900 | 0.831259 | 0.832617 |
| 0.999 | 0.786335 | 0.788103 |

The negative-center values agree by the proved evenness. All ten positive
centers have upper bounds below one, strictly separated decreasing
intervals, and widths below the preregistered `1/200` limit. The analytical
proof establishes strict decrease for the entire continuous domain
`0<|p|<=999/1000`, not just for these eleven computed values.

At `p=999/1000`, the complete capture probability is between `78.6335%`
and `78.8103%` of its reference value. This is a decrease of between
`21.1897%` and `21.3665%` relative to the original source, with no change
of the law, energy distribution or output event.

## What supplies the enclosure

`PROOF_CAPTURE_PROFILE.md` derives the actual incoming spectral density
from the inherited Schur/Mobius formula, extends its valid continuum
rectangle, and keeps the full scattering denominator in a fixed positive
weight. It proves evenness and strict momentum decline of the complete
probability. Its finite-width error is below `delta^2=10^-6`, and energy
monotonicity reduces the ratio envelope to the two fixed energy endpoints.

The verifier evaluates that envelope with outward exact rational interval
arithmetic. Its finite consistency checks agree with a separately written
Schur-form density and signed-center symmetry. These checks audit the
formula; they do not replace the analytical source/normalization proof.

## Disposition and provenance

The prospective source pin is
`8ceec7a35f68aa6d78c1f8dee698956a74bf4ef3`. All eight accepted files were
publicly read back before the single first execution. The actual result
was 86 checks, all 11 centers, exit 0 and empty stderr. `EXPECTED.txt`
contains exactly 700 bytes and 15 lines, SHA-256
`9e440107eadca6c01197ba25fdf1837c212187a6f0308e1e508d7ab351132985`.
`RUN.md` records the immutable pin, all accepted hashes, neutral environment
and chronological readback/run timestamps.

No frozen falsifier fired. No input, tolerance, branch, event, verifier or
preregistration was changed after the public pin. Required x86_64/aarch64
PR replay passed at result commit `1dd68997a198e09b778b222cff482080ed12a14f`,
including byte-identical stdout and the aggregate check; see `RUN.md`.
Any later documentation head must also pass its required PR check. Same-session static
reviews are disclosed separately and are not independent external proof
acceptance. The proposed infinite-dimensional results remain conditional
analytical candidates.

## Absolute scale and physical boundary

The complete absolute probability has not been evaluated. The inherited
reference bound and the analytical profile imply `P_win(p)>1/10^28`
throughout the frozen domain. This is a conservative guaranteed lower
bound, not an estimate of the actual rate. The values near `0.79` in the
table are ratios to `P_win(0)`, not absolute capture probabilities.

A separate [post-run analytical addendum](../../notes/C-BOUND-PAIR-CAPTURE-MOMENTUM-N/ABSOLUTE_BOUND.md)
also bounds this same selected joint probability above by
`8/(5*pi*10^6)`. It is explicitly outside the prospective finite audit,
uses unchanged inputs and has no new executable. The absolute interval
remains very wide; its small upper bound concerns the specified source
and narrow outgoing window, not arbitrary capture. No pinned verifier,
proof or preregistration was changed to obtain it.

The process retains the standing token, emitted pulse and record. Its
success projector includes the outgoing bound branch; a bare memory
click is not a binding herald. It is an asymptotic observable with a
supplied spectral source, not a finite physical detector/preparation.
The companion port proof embeds this apparatus exactly in its minus
sector. Changing to computational-port readiness changes the object law
and does not inherit this capture curve automatically.

No identification as a physical photon or electron, charge, spin,
statistics, polarization, SI calibration, native source or cross-layer
occurrence claim is made. No Canon, release, live H/O or inherited source
is modified by this package.
