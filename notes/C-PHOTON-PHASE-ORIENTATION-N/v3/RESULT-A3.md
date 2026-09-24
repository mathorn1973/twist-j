# RESULT C-PHOTON-PHASE-ORIENTATION-N, version 3, part A3 (2026-09-22)

Status: NON-CANONICAL incubation, engineering orientation, candidate label
candidate-C (computed at finite range, float categorical draws, no
exact-arithmetic claim). No Canon, Registry or Frontier movement.

    ENGINE_CALIBRATION_V3 PASS

Part B3 (the TWIST point t = 1) was therefore executed as preregistered; its
result is recorded separately.

## Pins (hashed and stored in the project before execution)

    PREREG-C-PHOTON-PHASE-ORIENTATION-N-V3.md  b4799904e59fa870fc81aabcaf8a13efdc685ba2962cf3f6ec44b10cbb1bce29
    zlgt2.c        62be81dc972596f10ff29636888b8b923c56c1c5c393627a24fba8cc1ab6d27c  (identical to version 2)
    jobs_v3.py     3a9b280b3b1f0fb4e46a0baeaac7d5b096645791a0ff328b88b94c8b6f485f04
    analyze_v3.py  8460818640313e30e3b3fde985222dc7f6ecc9f1abe0a870df39fc35e9dae377
    Incorporated by reference, unchanged:
    PREREG-...-V2-PART-A.md  950aaac24b475e954b4e13572af8a07647c5104d500c8d2d94613ce61fd50440
    PREREG-...-V2-PART-B.md  9e92fb8e5fb090a78ee253eaa57dfca9ba617b730016493b646d4d2407c86e3b

Execution host: x86_64 Linux, 24 logical cores, gcc 11.4 -O2
-ffp-contract=off, Python 3.10.12. The four files were re-hashed on the host
before the run and matched. 80 of 80 chains completed with an END line; the
analysis stderr was empty.

    analysis_A3.txt  99473994f5116fa543627f8e4c50b56b9ca4a1b2817afca047200fb82f8e5794
    blocks_A3.tsv    5d62c105ab19dcc465ee408c14c3749d20a971c43f97820500e98cb40ece4d84

## Frozen verdict lines

    C1  Z_13 beta 3/2    COULOMB_ORIENTATION      Z = 0.5312 +- 0.0012, M = 0.0010 +- 0.0008
    C2  Z_13 beta 7/10   MASSIVE_ORIENTATION      rule (a): Delta_16(1) = -0.0005 +- 0.0016,
                                                  Delta_24(1) = -0.0006 +- 0.0015
    C3  Z_5  beta 5      STOP_MIXING_ORIENTATION  (allowed: not COULOMB)
    C4  Z_13 beta 11/10  COULOMB_ORIENTATION      Z = 0.5907 +- 0.0020, M = -0.0002 +- 0.0010
    C5  Z_13 beta 9/10   UNRESOLVED_ORIENTATION   (allowed: not COULOMB)
    ENGINE_CALIBRATION_V3 PASS

Threshold for rule (b) and (c): qhat_min^2/4 = sin^2(pi/24) = 0.017037
(engineering readout). Decimals above are computed witnesses.

## What the controls show (read after the verdict, not a re-scoring)

Coulomb controls. Delta_L(1) is flat in L within errors (C1: 0.525, 0.530,
0.519, 0.535 at L = 8, 12, 16, 24; C4: 0.588, 0.592, 0.598, 0.588). The fitted
mass is compatible with zero at the 1e-3 level. The C1 fit has chi2 = 14.85
on 6 degrees of freedom; the rule carries no goodness-of-fit gate and none is
added after the fact.

Confined controls. The clear control C2 has a contrast compatible with zero
at L = 16 and 24 and is labelled by rule (a). The near-edge control C5 still
carries Delta_16(1) = 0.0059 +- 0.0019 (3.1 SE) and falls through to
UNRESOLVED; its contrast decays monotonically with L (0.017, 0.0096, 0.0059,
-0.0006), which is the massive signature at a scale the rule does not resolve
at L = 16.

Hot starts. In the Coulomb controls hot chains freeze into coherent nontrivial
flux sectors and are excluded as TRAPPED: C1 one hot chain at L = 8 and both
at L = 16 and 24; C4 both hot chains at every L. The hot/cold gate G4 is
therefore not evaluable there (HOT_TRAPPED), and those controls rest on cold
chains through G3. In the confined controls between 99.2 % and 99.9 % of the
measurements of every chain, hot or cold, are in the trivial sector, and G4
passes with z at most 1.07.

Higgs control. As in version 2, hot starts leave incoherent vortex sheets
that pass the triviality test, fail stationarity and hot/cold, and the gate
stops the control. This was allowed by the calibration condition.

## Scope

Engineering orientation of a finite-size estimator on external control
carriers (Z_13 and Z_5 Wilson weights). It calibrates the engine and the rule;
it is not evidence about any TWIST quantity.

## Custody note (added 2026-09-22, 23:45 CEST)

The raw A3 logs and blocks_A3.tsv lived only on the x86_64 host. They were
lost when that host rebooted at about 23:12 CEST. analysis_A3.txt and the
hashes above are in the project. The engine is deterministic and has been
shown bitwise reproducible across x86_64 and aarch64 builds, so the logs can
be regenerated exactly from the pinned code and seeds.
