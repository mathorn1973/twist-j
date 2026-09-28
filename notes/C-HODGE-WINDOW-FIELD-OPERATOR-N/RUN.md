# Exact run record

PUBLIC NON-CANONICAL candidate-C reproduction. Owner: #1237.
Author: A. M. Thorn <thorn@twistj.com>.

## Public pin

pin_commit: 369bd76b38483662395da567e834a38c2eb9a2fa
prereg_sha256: 9db803fff3f02ba295c2de1f94a4d4c05e42396a514b044c2c2e4592193a15a5
verifier_sha256: 6e835c99c88e2fa057e372a22c06711476e3956d79be3d2ddd7fe18816d0e300
public_PREREG_blob: 734e29a509e35691e0ac467dc2be97dd9d2c4791
public_verify_blob: b7613f89d9ce8b31d132d81a60aa2cdb766fa41a
command: python3 notes/C-HODGE-WINDOW-FIELD-OPERATOR-N/verify.py

Both frozen files were publicly read back through the GitHub connector before
the first candidate execution. Conversation-local pre-lock calculations are
explicitly non-evidentiary and are disclosed in PREREG.md.

## Execution A

platform: macOS
architecture: arm64
python: 3.9.6
exit_code: 0
stdout_bytes: 789
stdout_sha256: 3bc9f36791616a77af91b3d59661cb305c7f2744121640b544a3c945eba1f503
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

## Execution B

platform: Linux
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_bytes: 789
stdout_sha256: 3bc9f36791616a77af91b3d59661cb305c7f2744121640b544a3c945eba1f503
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

## Exact stdout

    PASS G1: diagonal six-direction principal-form class is ZERO; system rank 7/7
    PASS G2: C beta^-1 C^T = g^-1; complementary pairs +05,-14,+23 exactly
    PASS G3: unit forward stencil is NOT total; first witness w=-1,-1,-1,-1,0,-1 offset_index=2 win=Q5(1/5,3/5) next=Q5(-1/5,1)
    PASS G4: rounded event-only stencils exact finite checks=1920
    PASS G5: ideal mixed quadratic controls=48; all-n/C4 and plane-wave bounds are proof-level
    PASS G7 C5: FINITE-ROUNDING-COVARIANCE-FAIL witness n=1 w=-1,-1,-1,-1,0,-1 a=1,0,0,0,0,1
    PASS G7 J: FINITE-ROUNDING-COVARIANCE-FAIL witness n=1 w=-1,-1,-1,-1,0,-1 a=1,0,0,0,0,1
    G6 local D3 mode transfer: proof-level consequence of inherited root bound plus G5
    NON-CANONICAL: no finite-n self-adjointness, Cauchy evolution, physical photon or massless-phase claim

This is actual two-architecture reproduction of the unchanged pinned
noncanonical verifier. It is not blind independent-agent confirmation and is
not a formal public-probe computation gate or Canon promotion. Universal
claims rest on PROOF.md.
