# PREREG C-PHOTON-PHASE-ORIENTATION-N, version 2, part B: the fixed point t = 1

Status: NON-CANONICAL incubation preregistration, engineering orientation,
no authority, no phase evidence in the Canon sense, no Canon or Registry
movement. Not #742 or #757. Frozen 2026-09-22 together with part A of version
2, before any data at the TWIST weight exist in this session.

Authorization: the owner answered "Pust" on 2026-09-22 to the proposal "build
engine v2 (flux handling, absolute test) and adopt its part B as the
preregistration of #1116". Execution is conditional on
ENGINE_CALIBRATION_V2 PASS in part A. If part A fails, this part is void and
is not run. This text is offered unchanged as the #1116 preregistration; if it
is adopted publicly, the public pin governs and nothing here is re-tuned.

## 1. Equation

K_L = (Z/LZ)^4, A in C^1(K_L; Z5), f = dA mod 5,
mu_L proportional to prod_p W(f_p), W = (4, phi^2, phi^-2, phi^-2, phi^2),
phi = (1 + sqrt5)/2 (PHOTON-WINDOW-COORDINATES weight at t = 1).
Score X(f) = sin(2 pi f/5)/(1 + cos(2 pi f/5)) = tan(pi f/5), so X = kappa G,
kappa = tan(pi/5) (notes/canon/PHOTON-DEFECT-SCREENING-CRITERION.md).
A_L(m), B_L(m), Delta_L(m), s, TRIVIAL exactly as in part A of version 2.
Delta_L(1) is the exact/coexact contrast of #1108 at q_min on the primal
side; by the contact identity it equals S_n,02,02 - S_n,01,01.

By-products (no decision weight), with d_L = (1 + E X^2)/2:

    25 chi_L = d_L - A_L(1),    b_L = d_L - B_L(1),    Delta_L(1) = b_L - 25 chi_L.

## 2. Code

zlgt2.c, jobs_v2.py (model TW), analyze_v2.py, byte-identical to the files
hashed with part A. Runner invoked with --owner-authorized.

## 3. Data

L in {8, 12, 16, 24}; per L cold replicas 1, 2 and hot replicas 1, 2;
thermalization 2000 L^2/64 sweeps; 4000 measurements every 2 sweeps;
correlator ingredients every 40th measurement at L = 16.
Seeds as in part A with index 5 (TW).
Primary execution: the same x86_64 Linux host as part A.
Reproduction: the identical job list on an aarch64 Linux host, same compiler
flags (-O2 -ffp-contract=off); the END state hashes are compared chain by
chain.

## 4. Systematics

As in part A. The q_min path is not the ordered S7 limit (#1125 closure
audit); this is finite-size orientation only. Local heat-bath only.

## 5. Decision (identical to part A)

Gates G1 to G4 and rule (a) to (d) of part A. Terminal: one of
COULOMB_ORIENTATION, MASSIVE_ORIENTATION, UNRESOLVED_ORIENTATION,
STOP_MIXING_ORIENTATION.

Reproduction: if every END hash agrees between the two architectures,
REPRODUCTION_BITWISE. Otherwise the aarch64 logs are analysed with the same
rule; the same terminal gives REPRODUCTION_STATISTICAL, a different terminal
gives STOP_REPRODUCTION, which overrides the primary terminal.

## 6. Layer

L6 finite-volume expectations of the selected L4 measure. No lift, no gate.

## Reading fixed in advance

COULOMB_ORIENTATION: at t = 1 the exact/coexact contrast stays positive down
to L = 24 and no photon mass above about 0.13 lattice units is resolved. It
supports the P1 target b - 25 chi > 0 at engineering grade and says nothing
about S1, P2 or S7.
MASSIVE_ORIENTATION: a resolved mass or a vanishing contrast at L = 16 and 24.
It contradicts P1 at engineering grade: the analytic route would be aiming at
a false target at t = 1 unless larger volumes change the picture.
UNRESOLVED_ORIENTATION or STOP: no reading.
Neither label changes PHOTON-MASSLESS-PHASE, which stays O.
