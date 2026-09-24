# PREREG C-PHOTON-CONTRAST-DRIFT-N

Status: NON-CANONICAL incubation candidate, engineering orientation, no
authority, no Canon or Registry movement. Not #742, #757 or #1116. Session:
Claude (Cowork), 2026-09-22. Basis: Public Canon v91 (main 11b66d4, STATUS
ACTIVE, checked this session).

## Question

Part B3 of C-PHOTON-PHASE-ORIENTATION-N version 3 returned
COULOMB_ORIENTATION at the TWIST weight t = 1 (analysis_B3.txt, sha256
5d870f10b66ef8c196be5881a0f76251ccab71ce5e770a08d1c2a9ecaa1dce3a). Its fit
also returned M = 0.0027 +- 0.0011, positive at about 2.5 SE: the contrast at
the two smallest momenta (0.590 at s = 0.152, 0.580 at s = 0.068) lies below
the plateau of the larger momenta (about 0.602). The frozen rule cannot
resolve a mass of that size. This probe asks one question with new,
independent chains: does the contrast keep falling at small momentum?

Known-result disclosure: all B3 data and the B3 second reading were seen
before this freeze. The reference plateau and the massive prediction below
are computed from the frozen B3 output. No data from the chains listed here
exist.

Launch: by this session under the owner's standing request of 2026-09-22 to
build probes that help close open points, as a continuation of the "Pust"
execution of part B. Not separately confirmed by the owner.

## 1. Equation

As part B of version 2 (incorporated by reference, sha256 9e92fb8e...):
K_L = (Z/LZ)^4, Z5 field, measure prod_p W(f_p), W = (4, phi^2, phi^-2,
phi^-2, phi^2), X = tan(pi f/5), Delta_L(m) = A_L(m) - B_L(m),
s = 4 sin^2(pi m/L), TRIVIAL iff max_a |Fbar_a| < 3/4.

Reference plateau of B3: the inverse-variance weighted mean of the six B3
pooled contrasts with s >= 1/4 (L = 8 m = 1, 2; L = 12 m = 1, 2; L = 16 m = 2;
L = 24 m = 2),

    P_ref = 0.602177,  SE_P = 0.002859,

with SE_P taken as fully correlated (weighted mean of the six standard
errors), since contrasts at m = 1 and m = 2 come from the same configurations.

Drift at size L: d_L = P_ref - Delta_L(1), sigma_L = hypot(SE_L, SE_P),
z_L = d_L / sigma_L, where Delta_L(1) and SE_L use only the new chains below.

For orientation only (no decision weight): the B3 massive fit
(Z = 0.604252, M = 0.00269367) predicts Delta_24(1) = 0.5813 and
Delta_32(1) = 0.5647, i.e. d_24 = 0.021 and d_32 = 0.037; the massless reading
predicts d_L = 0.

## 2. Code

zlgt2.c (sha256 62be81dc..., unchanged), jobs_v3.py and analyze_v3.py
(unchanged, imported), jobs_drift.py (job list and runner), analyze_drift.py
(gates and rule). Hashes in PIN-DRIFT.sha256. gcc -O2 -ffp-contract=off.
Standard C and Python standard library. Float categorical draws; no
exact-arithmetic claim.

## 3. Data

TWIST weight t = 1, cold starts only (in B3, 5 of the 6 hot chains at
L >= 12 froze into nontrivial flux sectors and were excluded):

    L = 24: cold replicas 3 to 14 (12 chains), seeds 0xC2518003 to 0xC251800E
    L = 32: cold replicas 1 to 8 (8 chains),   seeds 0xC2520001 to 0xC2520008

Seeds follow the version 3 formula; none coincides with a seed of A2, A3 or
B3. Thermalization 2000 L^2/64 sweeps (18000 and 32000), then 4000
measurements every 2 sweeps, no correlator. Primary host x86_64 Linux;
reproduction on an aarch64 Linux host with the identical job list and flags;
END state hashes compared chain by chain.

## 4. Systematics and estimation

As in version 2 part A: only TRIVIAL measurements, a chain qualifies iff at
least 1/4 of its measurements are TRIVIAL, blocks of 200, pooled mean and
standard error over all blocks of all qualifying chains at that L. The q_min
path is not the ordered S7 limit (#1125 closure audit). Local heat-bath only.
The plateau SE is conservative; the new SE_L are statistical only.

## 5. Gates, rule and falsifier (fixed now)

Gates, any failure gives STOP_DRIFT:
  G1 every one of the 20 logs complete (4000 measurements, RUN and END lines);
  G2 stationarity: in every qualifying chain the two halves of the TRIVIAL
     subsequence agree within 4 combined SE (blocks of 100) for Delta_L(1) and
     for monopole density;
  G3 at each L at least half of the chains qualify.

Terminal:
  DRIFT_CONFIRMED  iff z_24 > 3 and z_32 > 3;
  NO_DRIFT         iff |z_24| <= 3 and |z_32| <= 3;
  MIXED            otherwise (a z below -3 is printed as ANOMALY_HIGH).

By-products without decision weight: d_L, b_L, 25 chi_L at L = 24 and 32, and
a refit of the B3 points together with the new points.

Reproduction: all END hashes equal between the two architectures gives
REPRODUCTION_BITWISE; otherwise the aarch64 logs are analysed with the same
rule, the same terminal gives REPRODUCTION_STATISTICAL, a different terminal
gives STOP_REPRODUCTION, which overrides.

Falsifier, stated both ways. NO_DRIFT falsifies the massive reading of the B3
dip at the resolution of this probe (expected z_32 about 4.7 for the B3 fitted
mass; a mass with M below about 0.0015 is not resolved). DRIFT_CONFIRMED
falsifies the extension of the B3 COULOMB_ORIENTATION reading to L = 32.

## 6. Layer

L6 finite-volume expectations of the selected L4 measure. No lift, no gate.

## Reading fixed in advance

DRIFT_CONFIRMED: the contrast falls below the B3 plateau at small momentum in
independent chains at L = 24 and at L = 32. B3 COULOMB_ORIENTATION stands
only within its scope (no mass above about 0.13 lattice units at L <= 24);
the leading engineering reading at t = 1 becomes a light mass of order 0.05
lattice units, and P1 at t = 1 is in doubt at engineering grade. Split bounds
for b and chi should wait until larger volumes or a sharper estimator settle
it.

NO_DRIFT: the B3 dip is neither reproduced at L = 24 by independent chains
nor seen at L = 32. A mass of the size fitted in B3 is disfavoured, and the
B3 reading extends to L = 32 at this resolution. Engineering grade only.

MIXED or STOP_DRIFT: no reading.

No label changes PHOTON-MASSLESS-PHASE, which stays O.
