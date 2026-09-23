# PREREG C-PHOTON-PHASE-ORIENTATION-N, version 2, part A: calibration on controls

Status: NON-CANONICAL incubation candidate, engineering orientation, no
authority, no phase evidence in the Canon sense. Not #742, #757 or #1116.
Session: Claude (Cowork), 2026-09-22. Basis: Public Canon v91 (main 11b66d4,
STATUS ACTIVE, SHA256SUMS 5 of 5 OK, re-checked before this freeze).

Version 1 of this candidate fired its calibration falsifier
(RESULT-C-PHOTON-PHASE-ORIENTATION-N-PART-A_2026-09-22.md): a ratio rule that
is undefined when the contrast is already zero, and hot starts trapped in
topological sectors. Version 1 stays archived as failed. Version 2 is a new
preregistration with a new engine, a new rule and new controls; nothing of
version 1 is re-scored.

Known-result disclosure: version 1 diagnostics (Z_30 Wilson, beta 3/2 and 7/10)
and a smoke test of the version 2 code paths (Z_5 Wilson beta 5, 10
thermalization sweeps, 400 measurements, not a result) were seen before this
freeze. No data at the TWIST weight have been seen by this session.

## 1. Equation

Z_N gauge field on K_L = (Z/LZ)^4, measure prod_p W(f_p), f = dA mod N.
Score X(f) odd in f: X = sin(2 pi f/N) for the Wilson controls. For
q = (2 pi m/L) e_mu, m in {1,2},

    A_L(m) = mean over the 4 axes mu and the 3 planes containing mu of
             |sum_x X_a(x) exp(-i q.x)|^2 / L^4,
    B_L(m) = the same mean over the 3 planes not containing mu,
    Delta_L(m) = A_L(m) - B_L(m),     s = qhat^2 = 4 sin^2(pi m/L).

Coulomb phase: Delta tends to a positive constant as s -> 0. Massive phase:
Delta ~ Z s/(s + M) with M = mass^2 > 0.

Topological sector of a configuration: for each of the 6 plane orientations,
Fbar_a = average over the L^2 parallel coordinate planes of the integer flux
(sum of principal representatives of f over the plane)/N. A measurement is
TRIVIAL iff max_a |Fbar_a| < 3/4.

## 2. Code

zlgt2.c (engine; heat-bath with rolled weight tables; built-in selftest
against a brute-force six-plaquette recomputation), jobs_v2.py (job list,
seeds, runner), analyze_v2.py (gates and rule). Standard C and Python standard
library. Floating point categorical draws; no exact-arithmetic claim.
Compiled with gcc -O2 -ffp-contract=off.

## 3. Data

Controls (Wilson weight W(f) = exp(beta cos(2 pi f/N))):

    C1  Z_12, beta 3/2    Coulomb (clear)
    C2  Z_12, beta 7/10   confined (clear)
    C3  Z_5,  beta 5      Higgs / frozen (clear)
    C4  Z_12, beta 11/10  Coulomb, near the edge
    C5  Z_12, beta 9/10   confined, near the edge

L in {8, 12, 16, 24}. Per (control, L): four chains, cold replicas 1, 2 and
hot replicas 1, 2. Thermalization 2000 L^2/64 sweeps (2000, 4500, 8000,
18000). Then 4000 measurements, one every 2 sweeps. Correlator ingredients
every 40th measurement at L = 16 only. Seeds 0xC2000000 + 0x100000 * index
+ 0x1000 * L + 0x10 * [hot] + replica, index = position in (C1, C2, C3, C4,
C5, TW). Executed on one x86_64 Linux host with a process pool.

## 4. Systematics and estimation

Only TRIVIAL measurements are used. A chain qualifies iff at least 1/4 of its
measurements are TRIVIAL; otherwise it is reported TRAPPED and excluded.
Justification: in phases with frozen sectors (Coulomb, Higgs) nontrivial
sectors carry exponentially small equilibrium weight (about exp(-2 pi^2
beta_R) per unit flux in a Coulomb phase, area-suppressed in a Higgs phase);
in phases with mixing sectors (confined) the plane averages stay far below
3/4. Blocks of 200 TRIVIAL measurements; per (control, L) the pooled mean
and standard error use all blocks of all qualifying chains. Measured version 1
autocorrelation of Delta_L(1) in a Coulomb control is at most 8 measurements
at L = 16.

## 5. Gates, rule and calibration threshold (fixed now)

Gates, any failure gives STOP_MIXING_ORIENTATION for that control:
  G1 every chain log complete (4000 measurements, END line);
  G2 stationarity: in every qualifying chain the two halves of the TRIVIAL
     subsequence agree within 4 combined SE (blocks of 100) for Delta_L(1)
     and for monopole density;
  G3 at every L at least one cold chain qualifies;
  G4 at every L where a hot chain qualifies, pooled cold and pooled hot
     Delta_L(1) agree within 4 combined SE; where no hot chain qualifies,
     HOT_TRAPPED is reported and G4 is not evaluable at that L.

Rule on the 8 points (s, Delta_L(m)), L in {8,12,16,24}, m in {1,2}:
  weighted least squares fit of Delta = Z s/(s + M); thr = qhat_min^2/4 with
  qhat_min^2 = 4 sin^2(pi/24).
  (a) MASSIVE_ORIENTATION if |Delta_L(1)| <= 3 SE at both L = 16 and L = 24;
  otherwise
  (b) COULOMB_ORIENTATION if Z - 3 SE(Z) > 0 and M + 2 SE(M) < thr;
  (c) MASSIVE_ORIENTATION if M - 2 SE(M) > thr;
  (d) UNRESOLVED_ORIENTATION otherwise, or if the fit fails.
Scope of COULOMB_ORIENTATION: no mass above about qhat_min/2 (about 0.13 in
lattice units) is resolved at L <= 24.

Calibration PASS iff all hold:
  C1 = COULOMB_ORIENTATION;
  C2 = MASSIVE_ORIENTATION;
  C3 is not COULOMB_ORIENTATION;
  C4 is not MASSIVE_ORIENTATION;
  C5 is not COULOMB_ORIENTATION.
Otherwise ENGINE_CALIBRATION_V2 FAIL, and part B of version 2 is not run.

## 6. Layer

L6 finite-volume expectations on external control carriers. No lift.

## Falsifier

ENGINE_CALIBRATION_V2 FAIL. It is recorded as a result and the thresholds are
not moved.
