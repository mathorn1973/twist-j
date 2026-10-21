# P-J-RAMIFIED-AREA-WEYL-1

PUBLIC / NON-CANONICAL / L1, Public Canon v103.
Owner: ChatGPT-j-area-weyl-20261017. Author: A. M. Thorn.
SPDX-License-Identifier: Apache-2.0.
Reservation: https://github.com/mathorn1973/twist-j/issues/1582

## Question

On a strictly marked paired cyclotomic carrier, does reciprocal J/phi
scaling induce a finite symplectic map compatible with the known Weyl
fifth-root phase? Does that covariance itself force an energy quantum?

## Decision and boundaries

- **Positive L1 algebra (authored candidate-T):** T=diag(J,phi)
  multiplies the alternating form by j, T^5 restores it; reduction
  modulo (1-j) gives A=diag(2,3) in SL2(F5), implemented by
  a chosen five-state Weyl conjugation D|k>=|3k>.
- **Negative L1 selection (authored candidate-T):** four additive
  character readings remain A-covariant, and rational diagonal
  D-invariant costs have two independent values. The energy gap is
  not fixed; full Weyl-commuting local costs are scalar.
- **No physical promotion:** this is not a native U contact, physical
  Hilbert representation, Planck action, frequency, SI calibration,
  physical photon, Born law or apparatus construction.

All exact local frozen tests passed; local computation is x86_64 only.
Independent review and a passing two-architecture PR check must be
read separately before a computation-grade public status claim.

## Evidence

- PREREG.md: frozen equations, carrier, code, systematics, falsifiers, L1.
- verify.py: accepted Python-stdlib exact audit, unchanged since pin.
- PROOF.md: author-prepared universal algebraic proof and exclusions.
- EXPECTED.txt: exact 520-byte stdout from pinned verifier.
- RUN.md: pin, source/output hashes, execution and scope.
- RESULT.md: exact decision, fired falsifiers, open obligations.

Pin: 6b459a66d670656bd02a09c26da666bd16c077fb.

Run from a checkout root:

    python3 probes/P-J-RAMIFIED-AREA-WEYL-1/verify.py

The script neither opens data files nor imports the public Canon
at runtime. Public inherited inputs are J-PROJECTIONS,
J-GOLDEN-BRIDGE, FORCE-WEYL-HOLONOMY, and KERNEL-WEDGE-COUPLING.
The reserved predecessor work #1419 and #1576-#1580 is untouched.
No Canon, Registry, Frontier, Gates or workflow file is changed.
