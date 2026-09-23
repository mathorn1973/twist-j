# RESULT C-PHOTON-PHASE-ORIENTATION-N, version 2, part A (2026-09-22)

Status: NON-CANONICAL incubation, engineering. FALSIFIER FIRED:

    ENGINE_CALIBRATION_V2 FAIL

Part B of version 2 (the TWIST point) was not run. No data at the TWIST
weight exist. The thresholds are not moved; this record stays.

## Pins (hashed and stored in the project before execution)

    PREREG-...-V2-PART-A.md  950aaac24b475e954b4e13572af8a07647c5104d500c8d2d94613ce61fd50440
    PREREG-...-V2-PART-B.md  9e92fb8e5fb090a78ee253eaa57dfca9ba617b730016493b646d4d2407c86e3b
    zlgt2.c                  62be81dc972596f10ff29636888b8b923c56c1c5c393627a24fba8cc1ab6d27c
    jobs_v2.py               58e707108e96a3c4f85eea2aceda0dcfd5d309b0228b6a796dea34de1b230d94
    analyze_v2.py            2734fcea962aea3cf76c39383e89c09e5b40fb5f8d3aff5422621ad9bed4bb96
    Execution host: x86_64 Linux, 24 logical cores, gcc 11.4 -O2 -ffp-contract=off,
    Python 3.10.12; the three files were re-hashed on the host before the run
    and matched. 80 of 80 chains completed with exit 0 and empty stderr.
    analysis_A2.txt          86d96b1c0afb96dca845ea5d10a2fa6fde76821e786a0380de4ed0b79634b562
    blocks_A2.tsv            883c344783c70ff8e6c7a6b6d17069752fb10d335d57052d161de63c3c85d9ae

## Frozen verdict lines

    C1  Z_12 beta 3/2    COULOMB_ORIENTATION   Z = 0.5309 +- 0.0013, M = 0.0011 +- 0.0010
    C2  Z_12 beta 7/10   STOP_MIXING_ORIENTATION   (no chain in the trivial sector)
    C3  Z_5  beta 5      STOP_MIXING_ORIENTATION   (hot chains, stationarity and hot/cold)
    C4  Z_12 beta 11/10  COULOMB_ORIENTATION   Z = 0.5906 +- 0.0015, M = -0.0013 +- 0.0010
    C5  Z_12 beta 9/10   STOP_MIXING_ORIENTATION   (no chain in the trivial sector)
    Gate: C2 must be MASSIVE_ORIENTATION. It is STOP. FAIL.

## Diagnosis (after the verdict, not a re-scoring)

The sector statistic is biased for even N. The principal integer lift maps
f = N/2 always to +N/2, never to -N/2. In a phase where f = N/2 occurs with
probability p, the plane-averaged flux acquires the mean (L^2/N)(N/2) p. The
confined Z_12 control reads Fbar = 1.12 at L = 8 and 10.05 at L = 24, with
fluctuations 0.23. Every measurement was therefore classed nontrivial. The
near-edge confined control reads 0.70 at L = 8. The Coulomb controls read at
most 0.03. For odd N the lift is symmetric and there is no bias; the TWIST
point has N = 5.

Separately, the Higgs control C3 shows what was anticipated in the
preregistration: hot starts leave vortex sheets that are not fully coherent
(Fbar about -0.13 and -0.29 in two orientations at L = 24). They pass the
triviality test and contaminate Delta (hot 0.21 to 0.44 against cold 0).
The gate allowed C3 to STOP, and it did.

What worked: both Coulomb controls, the clear one and the near-edge one, were
labelled COULOMB with a fitted mass compatible with zero to 1e-3. Delta_L(1)
is flat from L = 8 to 24 (0.534, 0.527, 0.525, 0.526 and 0.593, 0.594, 0.595,
0.597). Hot chains in the Coulomb phase were trapped in coherent flux sectors
and correctly excluded.

## Consequence

Version 3 changes only the control group to odd N (Z_13 in place of Z_12),
which removes the lift asymmetry without touching the engine, the rule or the
TWIST job list. It is preregistered separately.
