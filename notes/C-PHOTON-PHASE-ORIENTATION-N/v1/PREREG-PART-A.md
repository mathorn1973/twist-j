# PREREG C-PHOTON-PHASE-ORIENTATION-N (part A: engine calibration on controls)

Status: NON-CANONICAL incubation candidate, engineering orientation only, no
authority, no phase evidence, not #742, not #757, not #1116. Session: Claude
(Cowork), 2026-09-22. Basis: Public Canon v91.

Part A runs ONLY control models with a phase known from the literature. No
TWIST weight is sampled in part A. Part B (the fixed TWIST point t = 1) is
written and frozen separately after part A and before any TWIST data, and is
executed only on an explicit owner decision, because a run would expose the
observable reserved by public issue #1116 before its own preregistration.

## 1. Equation

Z_N gauge field on (Z/LZ)^4, measure prod_p W(f_p). Score observable
X(f) = -(d/d theta) log W at theta = 2 pi f/N up to a positive constant:
X = sin(theta) for the Wilson controls. For q_m = (2 pi m/L) e_mu, m = 1, 2,

    A_L(m) = mean over mu and the 3 planes containing mu of |X~_a(q_m)|^2,
    B_L(m) = mean over mu and the 3 planes not containing mu,
    Delta_L(m) = A_L(m) - B_L(m),

which is the exact/coexact contrast of #1108 up to normalization. Coulomb
phase: Delta_L(1) tends to a positive constant; massive phase: Delta_L(1)
decreases like L^-2 once L exceeds the correlation length.
Secondary: monopole density (principal representative, dF/N on 3-cubes),
Polyakov radius, the #757 orientation-sum correlator ingredients.

## 2. Code

zlgt.c (independent heat-bath, floating point categorical draw, xoshiro256**),
run_controls.py (driver and analysis, blocked jackknife). No code shared with
the public photon_z5.cpp engine.

## 3. Data

C1 Coulomb control: Z_30 Wilson, beta = 3/2.
C2 confined control: Z_30 Wilson, beta = 7/10.
Sizes L in {8, 12, 16}. Two chains per (control, L), cold and hot.
Thermalization 1000 sweeps, then 1500 measurements every 2 sweeps;
correlator ingredients every 25th measurement at L = 16 only.
Seeds: 0xA0000000 + 1000*L + 10*control + chain.

## 4. Systematics

Z_30 is close to U(1) at these couplings (U(1) Wilson beta_c = 1.0111).
Critical slowing of the q_1 mode under local heat-bath; errors by blocked
jackknife with block length 50 measurements, hot and cold chains pooled only
if they agree within 4 combined standard errors.

## 5. Failure threshold (fixed before computation)

rho = Delta_16(1) / Delta_8(1).
Engine calibration PASSES iff all hold:
  C1: rho >= 3/4 and monopole density < 1/100 at every L;
  C2: rho <= 1/2 and monopole density > 1/20 at every L;
  hot/cold agreement within 4 combined SE for Delta_L(1) at every (control, L).
Any failure: ENGINE_CALIBRATION_FAIL, part B is not written on this engine.

## 6. Layer

L6 finite-volume expectations on external control carriers. No lift.
