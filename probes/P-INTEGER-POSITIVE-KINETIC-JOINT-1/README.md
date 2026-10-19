# P-INTEGER-POSITIVE-KINETIC-JOINT-1

Positive-kinetic joint variational integer dynamics for the discrete
linear TT metric sector and scalar source, with an action-derived
positive-definite physical quadratic Hamiltonian and a positive-signature
canonical symplectic invariant.

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
  sum-of-squares positivity of $\mathcal{H}_{\mathrm{phys},n}$, discrete
  Noether energy-work theorem, positive-signature symplectic Wronskian
  conservation $\Omega_n^+ = \Omega_1^+$, exact integer carrier and
  congruence inversion, uniform bounds and Lorentzian signature).
- `SOURCE.md` — Provenance and canonical authority references.
- `verify.py` — Primary integer-recurrence and polynomial-ring gate.
- `breaker.py` — Independent rational/direct-coordinate gate.
- `FROZEN.sha256` — SHA-256 manifest of the 5 prospective files.
- `EXPECTED.txt` — Exact 720-byte stdout from the first formal run.
- `RUN.md` — First local formal run metadata and custody record.
- `RESULT.md` — Summary of verified results, witnesses, and scope limits.
- `REVIEW.md` — Self-review and consistency audit.
