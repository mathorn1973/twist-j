# C-NATIVE-HODGE-METRIC-SEAM-N2: typed correction

Status: PUBLIC NON-CANONICAL.
Owner: A. M. Thorn / native-hodge-metric-seam-20260928-r2; issue #1253.
Basis: Public Canon v92, main e3b78e69752659d39b243eb4908d579d40794533.

This successor corrects the consumed predecessor C-NATIVE-HODGE-METRIC-SEAM-N.
The predecessor applied the original first-three-coordinate Hodge block to N2
site coefficients. N2 actually interprets site z as coefficients of the
orthogonal frame s1,s2,s3. No predecessor file is edited or reused.

Pinned inherited bytes:
- notes/C-OMEGA-GENERATIVE-GEOMETRY-N2/PROOF.md
  a6be9bd44df63655e2a42ec88c9f4cbb853b9ba15f5f5a869ec89e1ca5775c60
- notes/C-HODGE-EVENT-CAUCHY-N/PROOF.md
  6ebac7c63bcadba55791db017d273aa2136cdbf8867a72b3006c1d46bae823af
- notes/C-HODGE-EVENT-CAUCHY-N/model.py
  adc99adac6ff1e3d9e76d4952b97af16fcdbe919021c5947bdb6c0feb7b3a772
- probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py
  02f33f1de4174ee4d4aeb45202d838897e68c3bd205df23f9b208cc669f489d9
- notes/C-NATIVE-HODGE-METRIC-SEAM-N/RESULT.md
  d346d41fcff7a9ba62434e55242475fc05926ef3ab62746c838bc4324e4b571e

Frozen targets:

G1. Keep the N2 difference map x=z1-z3, y=z2-z3 and zero-sum section
    p10=(2,-1,-1)/3, p01=(-1,2,-1)/3, p11=(1,1,-2)/3
in the ACTUAL N2 coefficient space of s1,s2,s3.

G2. Use the correctly typed Hodge frame Gram
    diag(2sqrt5/5, 6sqrt5/5, 3sqrt5/2).
Prove exact squared lengths
    q10=43sqrt5/90,
    q01=67sqrt5/90,
    q11=38sqrt5/45=76sqrt5/90,
all distinct. Thus the abstract regular-hexagon permutation symmetry of the
selected cover is not an isometry symmetry of the actual N2 Hodge target.

G3. For the tagged diagonal increment d=(1,1,1), prove
    q(d)=31sqrt5/10.
No scalar normalization can make the three cover direction pairs equal.

G4. Reproduce the predecessor's rho=45/4 only as a HYPOTHETICAL control when
the cube coefficients are instead interpreted in the original first-three
E+ coordinates. State explicitly that this is not the N2 pipeline.

G5. Record the correctly typed selected flat form in N2 label coordinates:
    diag(2sqrt5/5, 6sqrt5/5, 3sqrt5/2, -(2+sqrt5)/8).
This is inherited Hodge data, not a new derivation.

G6. Selection boundary: before a native metric derivation can be claimed, a
metric-sensitive map from the native commutator cover into this anisotropic
Hodge frame must be supplied. Abstract cover symmetry cannot be imported as
target isometry symmetry.

No time calibration, photon, Galois, curvature, occurrence, L6 or SI claim.
The predecessor #1252 remains publicly superseded.

Commit and publicly read back PREREG.md and verify.py before execution.
Universal conclusions require PROOF.md. Only this directory may be added.
