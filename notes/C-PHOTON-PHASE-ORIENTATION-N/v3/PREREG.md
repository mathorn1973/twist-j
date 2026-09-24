# PREREG C-PHOTON-PHASE-ORIENTATION-N, version 3 (parts A3 and B3)

Status: NON-CANONICAL incubation candidate, engineering orientation, no
authority, no Canon or Registry movement. Not #742 or #757. Session: Claude
(Cowork), 2026-09-22. Basis: Public Canon v91 (re-checked this session:
main 11b66d4, STATUS ACTIVE).

## Relation to version 2

Version 2 fired its calibration falsifier
(RESULT-C-PHOTON-PHASE-ORIENTATION-N-V2-PART-A_2026-09-22.md). Diagnosis: the
integer flux statistic used for the sector test is biased for even N, because
the principal lift maps f = N/2 always to +N/2. The confined Z_12 controls were
classed nontrivial in every measurement. Version 2 stays archived as failed.

Version 3 is version 2 with exactly one scientific change: the four Z_12
controls become Z_13 controls, whose principal lift is symmetric. Everything
else is unchanged and is incorporated here by reference, byte for byte:

    PREREG-C-PHOTON-PHASE-ORIENTATION-N-V2-PART-A.md  (sha256 950aaac2...)
      sections 1 to 6: equation, estimation, gates G1 to G4, rule (a) to (d),
      calibration condition, layer
    PREREG-C-PHOTON-PHASE-ORIENTATION-N-V2-PART-B.md  (sha256 9e92fb8e...)
      TWIST equation, by-products, data plan, reproduction clause, reading
      fixed in advance

with these literal substitutions: controls C1, C2, C4, C5 use N = 13 at the
same beta (3/2, 7/10, 11/10, 9/10); C3 stays Z_5 at beta 5; set names A3 and
B3; file names jobs_v3.py and analyze_v3.py; the calibration line reads
ENGINE_CALIBRATION_V3. The engine zlgt2.c is byte-identical to version 2.
The TWIST job list (model TW, sizes, chains, sweeps, seeds, tables) is
identical to version 2.

Known-result disclosure: version 2 control data, including the flatness of
Delta in two Z_12 Coulomb controls and the Higgs-control hot-start
contamination, were seen before this freeze. No data at the TWIST weight have
been seen by this session.

## Calibration condition (unchanged)

PASS iff C1 = COULOMB_ORIENTATION, C2 = MASSIVE_ORIENTATION, C3 is not
COULOMB_ORIENTATION, C4 is not MASSIVE_ORIENTATION, C5 is not
COULOMB_ORIENTATION. FAIL is recorded as a result; B3 is then not run.

## Execution of B3

Authorized by the owner's "Pust" of 2026-09-22 (see the version 2 part B
text), conditional on ENGINE_CALIBRATION_V3 PASS. Primary host x86_64 Linux;
reproduction on an aarch64 Linux host with the identical job list and
compiler flags; END state hashes compared chain by chain.

## Falsifier

ENGINE_CALIBRATION_V3 FAIL, or for B3 the frozen terminals of version 2.
