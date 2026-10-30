# Unwrapped position, boost and clock reference

**Status: NON-CANONICAL.** Analytical candidate-T within an explicitly declared
reference model, plus a supplementary one-architecture exact arithmetic audit.
This directory is a public *note for review*, not a public probe, accepted
theorem, native-`U` derivation, Canon fold, or physical apparatus claim.

- Date: 2026-10-30.
- Author: A. M. Thorn.
- Scope owner and collision record: [issue #1834](https://github.com/mathorn1973/twist-j/issues/1834).
- Reference: Public Canon v106 on `mathorn1973/twist-j` `main`,
  activation commit `a193e389fb1ddb0bdc89165b015c95a17eb1e425`.
- Action layer: L1 mathematical comparison only. No L1-to-L5/L6 lift.

## Read first

[PROOF.md](PROOF.md) contains the complete analytical argument. Its seven
substantive parts distinguish:

1. The self-adjoint canonical position `X={E^-1,K}/2` from boost
   `K=i d/deta` and establish the free relativistic commutators.
2. The exact unitary momentum impulse and its inertia derivative `q^3/m`.
3. Mass transport at fixed canonical `(X,P)`, including the correction to
   a submitted, non-unitary mass-map formula.
4. The two-by-two spinor frame and its exact metric isometry on golden rungs.
5. **Two different clock preparations:** common rapidity with a named
   comoving generator and readout (exact clock phase and finite-width bound);
   common momentum (different exact energy difference). The former is not
   replaced by the latter.
6. Cell gluing on the unwrapped rapidity line and the non-finite-range
   cell-Fourier coefficients of `m cosh(eta)`. This is not a general no-go
   theorem for all finite-range discrete models.
7. An explicit unimodular integral change of basis `Q`, yielding
   `Q^-1 M_J^5 Q=diag(-F^5,F^-5)` and
   `Q^-1 M_J^10 Q=diag(F^10,F^-10)` for the **specified** Fibonacci
   matrix `F=((0,1),(1,1))`. It gives no one-step/native-`U` bridge.

Standard Newton-Wigner position theory is attributed in PROOF.md to the
original 1949 literature; no global novelty claim is made.

## Supplementary exact audit and provenance

- `verify.py`: Python standard library, integer and `Fraction` arithmetic;
  finite controls, not an all-parameter proof.
- `PREREG.md`: frozen **local** audit specification from before the local run.
  This is not a public probe preregistration or Git pin.
- `LOCAL_PIN_SHA256SUMS`: unchanged SHA-256 of the three scientific inputs
  from that local run: `PREREG.md`, `PROOF.md`, `verify.py`.
- `LOCAL_AUDIT.txt`: actual local stdout, 452 bytes; repeat with
  `python3 verify.py` from this directory.
- `RESULT.md`: original one-architecture result and limitations,
  recorded as they stood **before public submission**. Its references to
  an unsubmitted GitHub draft are historical, not the current repository state.

The local run: x86_64; Python 3.13.5; exit code 0; empty stderr; stdout
SHA-256 `436df21cdf147192aca674991ee0ccd7c93db977a4089445b611ac86af57c3ae`.
These facts do **not** satisfy the public two-architecture computation gate
or constitute independent review. The analytical arguments remain subject
to review. No previous public falsifier or claim is reopened or promoted.

## Boundaries

This note does not modify `canon/`, `probes/`, `reproduce/`, the
registry, the active version, or the repository's release. It makes no
new proper-time calibration, experimental prediction, unique reading
selection, detector realization, or derivation from the original discrete
automaton. Existing boost/clock and contact work keeps its independent scope
(including issue #1603, PR #1605, and drafts #1829, #1831 and #1833).

All newly authored note text and code is submitted under the repository's
Apache-2.0 license. A later Canon promotion would require its own reviewed
decision and the relevant public gates.
