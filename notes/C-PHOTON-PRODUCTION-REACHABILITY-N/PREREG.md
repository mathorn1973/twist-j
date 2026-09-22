# PREREG C-PHOTON-PRODUCTION-REACHABILITY-N

Status: NON-CANONICAL incubation candidate, no authority. Engineering design
audit of a frozen public preregistration. Promotes nothing, changes no Canon,
Registry, Frontier, GATES or public probe. Not phase evidence for the TWIST
model: the TWIST measure is not sampled here at all.

Session: Claude (Cowork), 2026-09-22. Basis: Public Canon v91, main 11b66d4,
STATUS ACTIVE, canon/SHA256SUMS 5 of 5 OK. Audited object:
notes/canon/PHOTON-PRODUCTION-PREREG-FREEZE-1.md (issue #757, parent #742),
merged at 5a3fc9c, sections 9, 11, 13, 15.

## Question

Can the frozen production classifier of #757 emit PHOTON_EVIDENCE when the
sampled system is an ideal lattice Coulomb phase? If the ideal Coulomb phase
cannot earn POLYAKOV_PHOTON or CORRELATOR_PHOTON at the frozen sizes, the
production cannot decide the phase of the TWIST model either, and F3 work on
#756 would unblock a measurement that cannot return its positive label.

## 1. Equation

Control carrier: the free non-compact lattice Maxwell field on
K_L = (Z/LZ)^4 with action (beta/2) sum_p F_p^2, F = dA, beta > 0. This is the
Gaussian fixed point of every Coulomb phase; compact U(1) or Z_N in a Coulomb
phase flows to it with beta replaced by a renormalized beta_R.

Polyakov loop in direction 0: P(x) = exp(i phi(x)) exp(i L theta_0), with
phi(x) = sum_t A_0(x,t) restricted to nonzero spatial modes and theta_0 the
constant holonomy mode, uniform. Then, exactly,

    <phi(x) phi(y)> = (L/beta) G_L(x-y),
    G_L(r) = L^-3 sum_(k in (2 pi/L)Z^3, k != 0) exp(i k.r) / lambda_3(k),
    lambda_3(k) = sum_(i=1..3) (2 - 2 cos k_i),

    Pbar = L^-3 sum_x P(x),
    E|Pbar|^2 = L^-3 sum_r exp(-(L/beta)(G_L(0) - G_L(r))).          (E2)

R_L := E|Pbar| (first absolute moment, as frozen in #757 section 9).

Correlator: for Gaussian F with covariance K, and W = exp(iF),

    C+ = exp(-s2)(exp(-K) - 1),   C- = exp(-s2)(exp(K) - 1),
    K_ab(n e_rho) = (beta L^4)^-1 sum_(k != 0) cos(n k_rho)
                    (|a_a(k)|^2 + |a_b(k)|^2)/lambda_4(k),
    s2 = K_ab(0) = (1/(2 beta)) (1 - L^-4),
    C(n) = 12 C+(K_long(n)) + 12 C-(K_trans(n)),

with K_long = K_01(n e_0) and K_trans = K_01(n e_2) (all twelve longitudinal
and all twelve transverse terms of #757 section 11 are equal by hypercubic
symmetry). Q_L(n) = C(n)/C(n+1), Q4_L(n) the frozen target of #757 section 11,
D_L(n) = Q_L(n)/Q4_L(n) - 1.

## 2. Code

verify_reachability.py in this directory, Python 3 with numpy (FFT and a
seeded PCG64 generator). numpy is an engineering tool here; the candidate
makes no computation-grade claim. Deterministic outputs are printed rounded.

## 3. Carrier and data

beta in B = {1/4, 1/2, 3/4, 1, 3/2, 2, 3, 5}.
Polyakov sizes: L in {12, 16, 24, 32} (the frozen decision sizes of section 9).
Correlator: L = 16 with n = 2..4, L = 24 with n = 3..6, L = 32 with n = 4..8
(the frozen windows of section 11).
R_L by exact Gaussian sampling of phi: 4096 independent samples per (beta, L),
seed 0x757A0D17 + 1000 L + index(beta). E|Pbar|^2 exactly by (E2) via FFT.
No TWIST data are read. The public pilot numbers of
probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2 may be quoted afterwards as
context only and do not enter any terminal.

## 4. Systematics

a) The Gaussian control is the most favourable Coulomb case: no monopoles, no
   compactness corrections, exact massless propagator. A design that fails on
   it fails on every Coulomb phase with the same beta_R.
b) beta_R of the TWIST point is unknown; hence the scan over B.
c) The frozen fit families are applied with weighted least squares. The
   interval rule of section 9 is ambiguous in its degrees of freedom. Both
   readings are evaluated: known-SE normal interval (z = 2.5758) and Student t
   with 2 degrees of freedom (t = 9.9248), with SE_L = r R_L for relative
   precision r in {0.003, 0.01, 0.03, 0.1}. The infinite-precision limit is
   the sign of the WLS intercept itself.
d) For the correlator only the deterministic bias D_L(n) of the frozen target
   is computed. The statistical precision the production would reach is not
   computed here; a rough estimate may be reported, labelled heuristic.

## 5. Failure threshold and terminals (fixed before computation)

For each beta: POLY_REACHABLE(beta) iff the infinite-precision WLS intercept
of R_L is > 0 in BOTH M1 (a/L) and M2 (a/L^2).

Terminal, evaluated on the plausible band B* = {1/2, 3/4, 1, 3/2, 2}:

    DESIGN_POLYAKOV_UNREACHABLE  iff POLY_REACHABLE is false for every beta in B*
    DESIGN_POLYAKOV_REACHABLE    iff POLY_REACHABLE is true for every beta in B*
    DESIGN_POLYAKOV_BETA_DEPENDENT otherwise, with the threshold reported

Secondary terminal:

    CORRELATOR_TARGET_BIAS_HIGH iff max |D_L(n)| over L in {24,32} and the
      frozen windows exceeds 0.01 at beta = 1
    CORRELATOR_TARGET_BIAS_LOW  otherwise

Falsifier of the concern that motivated this audit: DESIGN_POLYAKOV_REACHABLE.
If it fires, the Polyakov leg of the production is sound on the control and
the concern is withdrawn.

## 6. Action layer

L6 (measure: expectations, finite-size fit rules) on an external control
carrier. No lift to the TWIST L4 action is made. No GATE is touched.

## Break plan (before computation)

Independent code path: E|Pbar|^2 by direct real-space double sum at L = 6, 8
without FFT; G_L(0) against the Watson value 0.252731 (large L); K_long and
K_trans by direct summation at L = 8 against the FFT path; Monte Carlo mean of
|Pbar|^2 against (E2).
