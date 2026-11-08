# Fixed-total-lapse boundary classification

NON-CANONICAL, NEW_DECLARED L1, scalar normal form, force a=0.

This probe separates fixed total lapse from independently varied lapses.
Fixing the sum before variation allows positive-energy stationary motion;
it does not impose a numerical energy. The complete stationary phase
classification and its endpoint/energy ambiguity are proved in PROOF.md.
The word duration in the identifier is a declared parameter sum, not an
admitted physical clock.

With a fixed number of bonds, the declared finite phase equivalence has
complete invariant (initial phase, total lapse). Fixed configuration
endpoints reduce the remaining freedom to a linear momentum equation.
An additionally chosen real energy shell cuts its kernel into an empty
set, a point, or a sphere. A frozen negative-lapse example has exactly two
phase orbits. The finer relation requiring a continuous regular-chart
path retains additional ordered interval labels.

Run from the repository root:

```text
python3 probes/P-INTEGER-FIXED-DURATION-BOUNDARY-1/verify.py
```

The primary launches its separately authored breaker and requires identical
raw certificate bytes. Both use Python standard-library exact rational
arithmetic. EXPECTED.txt is the first formal stdout; RUN.md binds its
provenance. PREREG.md, PROOF.md, SOURCE.md, both programs and FROZEN.sha256
were published and read back before execution. RESULT.md states the earned
scope; REVIEW.md records source and proof review. Required architecture
checks are recorded on the pull request at its exact result head.

This changes a declared variational boundary condition. It preserves the
predecessor's independent-lapse H=0 result and supplies no new gravitational
interaction, physical clock, metric selection or cross-layer lift.
