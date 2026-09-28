# RUN - C-NATIVE-HODGE-METRIC-SEAM-N3

PUBLIC NON-CANONICAL candidate-C reproduction.

Prospective pin:

    d4847ca43c6b94e1095053cb2e4ad54505601e93

Public readback hashes:

- PREREG.md:
  eb239c336ac7b2abe3a0a0cee60dd508e6e542a109b728485ece93f8b02b6a61
- verify.py:
  d994243cbda91d99b0c994d5a2646e1a1a543760b2817715b714039d268926d0

arm64: Darwin, Python 3.13.13, exit 0, stderr 0.
x86_64: Linux, Python 3.13.5, exit 0, stderr 0.

Both stdout streams are 497 bytes with SHA256

    182b13e52821a1d913c4cec7cf85ef70c2a08b1ca8ef492299622b2d08c61288

Exact stdout:

    PASS G1: actual N2 site coordinates use orthogonal frame s1,s2,s3
    PASS G2: cover-direction squares = sqrt5*(43,67,76)/90; pairwise distinct
    PASS G3: tagged diagonal square = 31sqrt5/10
    PASS G4: abstract hexagon symmetry is not an isometry of the actual N2 Hodge frame
    PASS G5: rho=45/4 reproduced only in the hypothetical original-coordinate N1 control
    PASS G6: typed flat frame = diag(2sqrt5/5,6sqrt5/5,3sqrt5/2,-(2+sqrt5)/8)
    NON-CANONICAL CORRECTION: N1 is superseded for the actual N2 pipeline

These are same-code reproductions, not independent-agent confirmation. Universal statements are supplied by PROOF.md.
