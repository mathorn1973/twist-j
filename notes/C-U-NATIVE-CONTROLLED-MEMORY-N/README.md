# Native controlled occupied memory

**NON-CANONICAL / L1 analytical candidate.** A. M. Thorn, 2026-10-29.

This note gives a small one-shot routing construction under the original
six-coordinate native U. With independently prepared new label lambda,
old label mu and a raw q control chi, the actual selector chooses ace or bbd.
After at most three native ticks, fixed current-state readers recover either
the swapped labels or the held labels forever. No external gate is inserted
and neither reader receives the native counter. Both use shared native q,r.

This is not the first native occupied operation or retained-control family.
PROOF.md credits the canonical predecessor and PR #1430. The particular
candidate uses a raw q control to select different actual words and transfers
source dependence across the two fixed piston pairs, as certified by complete
raw-coordinate response identities.

- [PROOF.md](PROOF.md): complete construction, two fixed readers, all 50
  inputs, 1000-state closed tail, resource and predecessor boundaries.
- [BOUNDARY.md](BOUNDARY.md): why synchronized U cannot write a new permanent
  payload into a completely ready fixed affine target.
- [PREREG.md](PREREG.md): equations, complete domains and exact audit gates,
  frozen before either scientific program first runs.
- [verify.py](verify.py) and [break_check.py](break_check.py): separately
  written exact standard-library audits from the same authoring session.

- [RESULT.md](RESULT.md): exact outcome, predecessor credit and continuation
  boundary.
- [RUN.md](RUN.md): public pre-execution pin, source custody and first exact
  x86_64/arm64 runs. Both programs passed with per-program byte-identical stdout.
- [EXPECTED.txt](EXPECTED.txt) and [BREAK_EXPECTED.txt](BREAK_EXPECTED.txt):
  the two first scientific outputs.

Reservation: [#1830](https://github.com/mathorn1973/twist-j/issues/1830).
Pre-execution pin: `e54ce523eb2dbc0dae56b3d3773a375fc09a0191`.
No result in this note is public acceptance or a change of Canon status.
Preparation, physical readout, repeat/reset, Born occurrence, energy,
spacetime, and the interpretation of global n remain open.
