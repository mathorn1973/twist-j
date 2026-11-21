# P-INTEGER-POSITIVE-KINETIC-JOINT-1

Positive-kinetic joint variational integer dynamics for the discrete
linear TT metric sector and scalar source, with a positive-definite
uncoupled quadratic bond energy satisfying an exact discrete work balance
and a canonical symplectic invariant associated with the positive kinetic
metric $I_6$ on the homogeneous sector $a = 0$ (and on tangent variations
for fixed $a$).

- **Status:** `PASS` (`NON-CANONICAL`, `L1`)
- **Ownership issue:** https://github.com/mathorn1973/twist-j/issues/1647
- **Prospective pin commit:** `bd7e1dada3a4869ecfae76c0aea03c0a88c9983f`
- **Public pin receipt:** https://github.com/mathorn1973/twist-j/issues/1647#issuecomment-6269491226

## Reproduction

```bash
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-INTEGER-POSITIVE-KINETIC-JOINT-1/verify.py
```

The command runs `verify.py`, launches `breaker.py` in an isolated
subprocess (`python3 -I`), compares their 23-line (680-byte) certificates
byte-for-byte, and prints the 25-line (720-byte) `EXPECTED.txt` (SHA-256
`5b050c5aab38db6bb8865fe00ca5b023a1a73f36b25c9ba3d37c863f3ac8ff0a`).

## Contents

- `PREREG.md` — Frozen prospective specification and falsifier taxonomy.
- `PROOF.md` — Frozen mathematical proofs (joint variational derivation,
  sum-of-squares positivity of the uncoupled bond energy
  $\mathcal{H}_{\mathrm{phys},n}$, discrete work balance, homogeneous
  $a=0$ canonical symplectic Wronskian conservation $\Omega_n^+ = \Omega_1^+$,
  exact integer carrier and congruence inversion, reversible funded
  bijection, uniform bounds and Lorentzian signature; see `RESULT.md` and
  `REVIEW.md` for post-review scope notes and wording errata).
- `SOURCE.md` — Provenance and canonical authority references.
- `verify.py` — Primary integer-recurrence and polynomial-ring gate.
- `breaker.py` — Independent rational/direct-coordinate gate.
- `FROZEN.sha256` — SHA-256 manifest of the 5 prospective files.
- `EXPECTED.txt` — Exact 720-byte stdout from the first formal run.
- `RUN.md` — First local formal run metadata and custody record.
- `RESULT.md` — Summary of verified results, witnesses, scope limits, and
  explicit frozen-text wording errata.
- `REVIEW.md` — Self-review and post-review consistency audit.
