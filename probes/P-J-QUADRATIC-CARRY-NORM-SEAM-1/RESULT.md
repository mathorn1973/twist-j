# P-J-QUADRATIC-CARRY-NORM-SEAM-1 result

Status: **STOP / VERIFIER-INTEGRITY DEFECT / NO SCIENTIFIC CONCLUSION / PUBLIC CANON STATUS UNCHANGED.**

The sole formal execution of the immutable verifier exited zero and produced the exact `EXPECTED.txt` bytes with empty stderr. However, post-run source review found a frozen verifier defect before any pull request or architecture claim was made.

## Integrity defect

The preregistration requires the verifier to audit the exact identity

```text
F(x^2)-F(x)^2 = (5/4)(1-4B^2)
```

for the frozen witness `x=1+j`, after normalization `A=1/2`.

The pinned verifier instead contains the following decision path in G4:

```text
factor_coeffs = (5/4, 0, -5)
check("G4 multiplicativity factor",
      factor_coeffs == (5/4, 0, -5), ...)
```

so that gate compares a literal expected tuple with itself. It does not derive the coefficients from the previously computed exact values of `q0(x)`, `q1(x)`, `q0(x^2)`, and `q1(x^2)`.

This is a verifier-integrity failure relative to the frozen verifier obligation, not a mathematical counterexample to the theorem target. Under the no-repair rule, the pinned `verify.py` may not be edited and this probe identifier may not be resumed, renamed, amended, or rerun.

## What the completed stdout means

The captured run printed `20/20 SEAM-CERTIFIED`, but that terminal label is **not accepted as a scientific result** because one of the twenty gates was tautological. `EXPECTED.txt` and `RUN.md` are retained only to preserve the completed execution and its exact provenance. They are not evidence for a public claim.

No scientific falsifier fired. No theorem row is earned. No dependency, gate, Registry, Frontier, Canon, tag, release, or status changes.

## Written argument

The proof text in `PREREG.md` independently states the intended algebraic calculation, including the witness values and the claimed factorization. This STOP does not declare that argument false. It declares only that this probe's accepted verifier failed its frozen audit contract. Any further public test of the same scientific question requires a fresh successor identifier, fresh preregistration, fresh verifier, and fresh pin, with this defect disclosed prospectively.

## Identifier consumed

```text
probe:              P-J-QUADRATIC-CARRY-NORM-SEAM-1
public issue:       #620
pin:                5efc0beed470118fd2648951d1002b2af195048b
formal executions:  1
scientific result:   none
terminal reason:     verifier-integrity defect in G4 audit
```

The identifier is spent. The branch and frozen pin remain immutable audit history.
