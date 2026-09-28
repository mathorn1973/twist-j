# RUN - C-HODGE-NATIVE-TICK-CALIBRATION-N

PUBLIC NON-CANONICAL candidate-C reproduction.

Prospective pin:

    a98e1e17fc7fd52cbb414bd4a35d6fc0ea7c9aec

Public readback hashes:

- PREREG.md:
  2b027532f0e29370e7f54b13da8462a806f6abc8d9f95b40e6223ab12bac19d0
- verify.py:
  e839f8a2d91e8d85da1bca856bf0dbe174c285a53129a925c964bf67558e8acd

arm64: Darwin, Python 3.13.13, exit 0, stderr 0.
x86_64: Linux, Python 3.13.5, exit 0, stderr 0.

Both stdout streams are 485 bytes with SHA256

    82346022a7ef46fdb008a1a215a41c0cf67cd5f9f61fc1a55d0cc8ed70ac163b

Exact stdout:

    PASS G1: ideal tick calibration factor lambda_h/T^2 = h^2/ct is unique
    PASS G2: calibrated integer-label metric coefficients are independent of h
    PASS G3: spatial ratios a_i/ct exact and positive; signature 3+1
    PASS G4: rounded same-site interval bound exact-sample checks=75
    PASS G5: h=3 has two unequal exact timelike tick intervals
    PASS G6: relative squared-tick error bound is O(h^-3)
    NON-CANONICAL: METRO-TICK calibrates the selected ideal seam, not exact finite-h rounded events

These are same-code reproductions, not independent-agent confirmation. Universal statements are supplied by PROOF.md.
