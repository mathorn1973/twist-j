# Neutral-ring phase-to-account receiver

NON-CANONICAL / L1 / prospective exact proof and finite composition audit.
Reservation: [#1891](https://github.com/mathorn1973/twist-j/issues/1891).
Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

The declared integral contact can convert a phase match into a retained
present-state pointer. A ring signal meets one arm of a prepared reference
clock. On a match, the source/reference accounts change from (5,45) to
(25,25), and the clock's own parity gate then stops it. On mismatch,
the reference keeps rotating with account 45. Its internal evolution
preserves the pointer after the single bridge is disconnected.

This construction uses the same contact for ring propagation, reference
rotation, read and retention. The graph, ready preparation and one-shot
read schedule are supplied. It is not a compilation into original U.

The source files are:

- [PREREG.md](PREREG.md): frozen question, carriers, code, controls and thresholds.
- [PROOF.md](PROOF.md): complete conditional analytical derivation.
- [verify.py](verify.py): exact coefficient arithmetic and whole-ring audit.
- [PROVENANCE.md](PROVENANCE.md): disclosed exposure and scope boundaries.
- [SOURCES.tsv](SOURCES.tsv): exact public authority inputs.

After a genuine pinned run, EXPECTED.txt, RUN.md and RESULT.md record its
actual bytes, environment and conclusion. Required PR checks replay the
same scientific bytes on x86_64 and aarch64.

The principal construction is intentionally contrasted with a phase latch
that transfers no account, a negative-source preparation that fails to latch,
and common amplitude scaling. No universal energetic cost of recording,
physical calorimeter, photon, SI clock, Born occurrence, autonomous sampling,
reset or physical energy calibration is claimed.
