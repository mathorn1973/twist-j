# RESULT C-PHOTON-PHASE-ORIENTATION-N, part A (engine calibration), 2026-09-22

Status: NON-CANONICAL incubation, engineering. FALSIFIER FIRED:

    ENGINE_CALIBRATION FAIL

No TWIST weight was sampled. Part B (fixed point t = 1) is VOID on this
engine: its preregistration was frozen before part A finished, part A
declared in advance that a failure means part B is not run on this engine,
and it is not run. The failed record is kept, the thresholds are not moved.

## Pins (hashed before the first execution)

    PREREG-C-PHOTON-PHASE-ORIENTATION-N.md   0968b601ba3508f1cbc1ee321c46c3d75dcd2661ea7a60f925b8f7eb99e2f3b1
    zlgt.c                                   c019ca1e866ba6d31432b87cd091483bfd515323cf1a5996fdb5fb5a43c0021e
    run_controls.py                          2c4f034beeaeb16f865e2a32bfd3ce2f40ed48e96533d4084ad70781c0198029
    run: Linux x86_64, gcc 13.3 -O3 -march=native, Python 3.11.15; raw logs
    and calibration_stdout.txt hashed in RUNS.sha256

## Frozen verdict lines

    C1_coulomb  (Z_30 Wilson beta 3/2)  rho = Delta16/Delta8 = 0.7421, monopoles 0.0005,
                hot/cold z = 1.24, 2.59, 6.45                    -> FAIL
    C2_confined (Z_30 Wilson beta 7/10) rho = 1.9278 (ratio of two numbers compatible
                with zero), monopoles 0.28, hot/cold z <= 0.56   -> FAIL

## Diagnosis (after the verdict, not a re-scoring)

1. Rule defect, mine. The ratio rho is undefined when Delta_8 is already
   compatible with zero. C2 has Delta_L(1) = 0.0006 +- 0.0038, 0.0006 +- 0.0033,
   0.0012 +- 0.0040 at L = 8, 12, 16: massive at every size, but the ratio
   test cannot say so. A successor rule must test Delta_L against zero, for
   example a weighted fit Delta_L = Z + c/L^2 with an absolute test on Z.
2. Engine defect. Hot starts in the Coulomb control get trapped in nonzero
   integer flux sectors through the (mu,nu) planes. Time-quarter means of
   Delta_L(1), hot chains: L = 12: 0.14, 0.50, 0.51, 0.53; L = 16: 0.16, 0.11,
   0.28, 0.50. Cold chains stay at about 0.50 to 0.54 throughout. The Polyakov
   radius shows it even at L = 8 (cold 0.470, hot 0.270), where Delta agrees.
   In a Coulomb phase with beta_R near 1 a unit flux costs about
   2 pi^2 beta_R, so these sectors are metastable traps, not equilibrium
   states. Local heat-bath tunnels out only through rare wrapping monopole
   loops. A successor engine needs a flux-tunnelling move or tempering.

## What the data nevertheless show (diagnostic, no decision weight)

- Equilibrated Coulomb control (cold chains): Delta_L(1) is about 0.53, 0.51,
  0.51 at L = 8, 12, 16. It is flat, as a Coulomb phase requires. The confined
  control is zero at every L. The observable separates the phases once the
  flux sectors are equilibrated.
- Polyakov radius, cold chains: Coulomb control 0.470, 0.310, 0.203 at L = 8,
  12, 16, an exponential perimeter decay with the Gaussian reading
  beta_R of about 1.2. Confined control 0.039, 0.021, 0.014, exactly the
  L^(-3/2) noise floor. Both tend to zero. This independently supports
  C-PHOTON-PRODUCTION-REACHABILITY-N on a compact control.
- Correlator ingredients at L = 16 (120 samples, hot chains included, no
  error bars): the Coulomb control ratio deviations from the #757 target are
  +0.51 and +0.48 at n = 3, 4, larger than the Gaussian +0.19 and +0.17.
  They point the same way.

## Risk for #757 worth recording (not a finding)

The #757 thermal gate compares hot and cold chains. In a genuine Coulomb phase,
trapped flux sectors produce exactly such hot/cold differences. Whether the
inherited line heat-bath and flat-holonomy moves tunnel flux at L = 16 to 32
is not known from the L = 6, 8 pilot. If they do not, a true photon phase
ends in STOP_MIXING before any classifier runs.

## Successor (proposal, not preregistered here)

v2 engine: add an exact flux-sector move (or replica exchange whose replicas
are all sampled exactly and only the target replica is measured); decision on
Delta_L by an absolute test on Z in Delta_L = Z + c/L^2; controls kept (C1, C2,
plus a Z5 Higgs control). Part B to be rewritten on v2 and frozen before any
data at t = 1.
