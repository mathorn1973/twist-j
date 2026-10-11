# Result

Status: C

PUBLIC NON-CANONICAL. Action layer L1. Original text Apache-2.0.

The completed first-run audit finds that the two fixed nominal waveforms
do not meet the 1e-3 RWA accuracy target in the declared comparison with
the full two-frequency linear harmonic model. Direct coherent-input
trace-distance witnesses are 0.014067137981352463 and
0.009378535994174172 for +4*pi/5 and -4*pi/5. These are numerical lower
witnesses, not merely large conservative bounds. The common-phase optimized
upper estimates are 0.02158629392115937 and 0.01635469980834448.

The original RWA calculation remains internally consistent: it closes its
motion and matches its target phase near floating roundoff. The new result
exposes the limit of that approximation for these fixed pulses. It does not
invalidate the prior conditional algebra or establish a measured ion error.
The witness is trace distance, not average gate infidelity. Nor does this
linear-model comparison by itself prove the actual error of the nonlinear
optical parent, whose propagator is not calculated in this probe.

The optical linearization screen is NOT_CERTIFIED_BY_THIS_BOUND. Uncapped
continuous Duhamel upper estimates are 22.76797764334755 and
14.03528666273738, yielding only the trivial channel bound one. Their large
values do not demonstrate large actual nonlinear error. The corresponding
midpoint norm-integral maxima, 16.314448541033055 and 10.286293954929471,
show that simply eliminating the mesh allowance would not give a small
estimate from this same triangle-bound method.

The whole-pulse sampled RMS(k q) maxima are 0.6002098727461145 and
0.49631897175102413; continuous upper estimates are 0.6446237989972406
and 0.5321570779833832. The initial thermal values already range from
0.11339663994980463 to 0.1359918470944777, exceeding the frozen 0.1
heuristic before the drive. The pulse increases this diagnostic further,
but failing this arbitrary heuristic is not a necessary-and-sufficient
test of Lamb-Dicke channel accuracy. The threshold was not relaxed.

The separate continuous RWA phase/displacement envelope is trivial for
both signs and certifies no uniform intermediate accuracy. Relative adjacent
RMS motion remains below about 0.00264 of equilibrium spacing, a useful
geometry diagnostic that does not prove harmonic Coulomb validity or radial
stability. NUMERICAL.md distinguishes all sampled values, mathematical
envelopes, numerical evaluations, endpoint and compensated-frame scopes.

The protected source/reference marginal remains structurally preserved in
all three declared Hamiltonians because all five protected electronic
responses are exactly zero and the ideal shelving return is adjoint.
This covers arbitrary electronic/reference correlations. It does not prove
real spectator darkness, preserve every intermediate physical encoding,
or remove the separate obstruction to retaining an unknown complete source
while the full informative contact leaves distinguishable receiver records.

The exact standard-library audit completed with PASS: 24 single-segment and
24 chronological two-segment formal-series fixtures, Gaussian moments and
majorants, all ideal carrier columns, 25 active response paths and the
periodic common-unary-phase exception. Every named negative control was
exposed. Its precise scope is algebra, not floating trajectory certification.
EXPECTED.txt and RUN.md preserve the original 1369 stdout bytes.

The separate AVX-512/80-thread campaign completed with all integrity,
independent-integration, scalar/SIMD and repeat checks passing. All four
invocations are retained. The measured kernel median was 0.012028687 s;
the complete numerical campaign took 2.887861272 s. No input, pulse,
threshold, grid or source was changed after the public pin.

The justified next investigation is to control approximation error in this
extended model and obtain a nontrivial nonlinear comparison before adding
finite control pulses or claiming practical contact feasibility. It needs
its own frozen scope, convergence/error budget and source pin; no such
successor is executed here. No physical experiment, full-contact simulation,
total work account, physical admission or Canon promotion is claimed.

Required unchanged x86_64/aarch64 CI replays the exact verifier on the
reviewed PR head. It does not reproduce or certify the floating timing or
the physical assumptions.
