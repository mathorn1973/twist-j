# PREREG C-PHOTON-PHASE-ORIENTATION-N, part B: the fixed point t = 1

Status: NON-CANONICAL incubation preregistration, engineering orientation,
no authority, no phase evidence in the Canon sense. Frozen 2026-09-22 before
any data at the TWIST weight exist in this session. Not #742, not #757.
EXECUTION IS NOT AUTHORIZED by this file. It runs only after an explicit
owner decision, because it measures the observable reserved by public issue
#1116. If the owner adopts this text as the #1116 preregistration, the public
pin supersedes this one and nothing here is re-tuned.

Engine: zlgt.c of part A, unchanged bytes (sha256 in PIN.sha256), and a
driver run_twist.py written before execution; the driver may only set the
parameters below.

## 1. Equation

K_L = (Z/LZ)^4, A in C^1(K_L; Z5), f = dA mod 5,
mu_L proportional to prod_p W(f_p), W = (4, phi^2, phi^-2, phi^-2, phi^2).
Score X(f) = sin(2 pi f/5)/(1 + cos(2 pi f/5)) = tan(pi f/5), so X = kappa G
with kappa = tan(pi/5) (PHOTON-DEFECT-SCREENING-CRITERION section 1).
A_L(m), B_L(m), Delta_L(m) = A_L(m) - B_L(m) as in part A, m = 1, 2.
d_L = (1 + E X^2)/2. By the contact identity, reported as by-products:

    25 chi_L = d_L - A_L(1),    b_L = d_L - B_L(1),    Delta_L(1) = b_L - 25 chi_L.

## 2. Code

zlgt.c (part A pin) and run_twist.py. Floating point categorical draw.

## 3. Data

L in {8, 12, 16, 24}; two chains per L, cold and hot;
2000 thermalization sweeps; 2000 measurements every 2 sweeps;
correlator ingredients every 25th measurement at L = 16 only.
Seeds 0xB0000000 + 1000 L + chain (chain 0 cold, 1 hot).

## 4. Systematics

Local heat-bath only. Plaquette-local observables are insensitive to flat
holonomy sectors; Polyakov data are reported without decision weight.
Near a first-order transition hot and cold chains may settle in different
phases; that is caught by the mixing gate, not averaged. The q_min path is not
the ordered S7 limit (#1125 closure audit); this is finite-size orientation.
Errors: blocked jackknife, block 50 measurements.

## 5. Decision (fixed now)

Mixing gate: for every L, |Delta_L(1)_cold - Delta_L(1)_hot| <= 4 combined SE,
otherwise terminal STOP_MIXING_ORIENTATION and no phase word is used.

rho_a = Delta_24(1)/Delta_12(1), rho_b = Delta_16(1)/Delta_8(1), each with a
jackknife-propagated SE, pooled over chains.

    COULOMB_ORIENTATION  iff rho_a - 2 SE >= 3/4 and rho_b - 2 SE >= 3/4
    MASSIVE_ORIENTATION  iff rho_a + 2 SE <= 1/2 and rho_b + 2 SE <= 1/2
    UNRESOLVED_ORIENTATION otherwise

A massive outcome does not distinguish confined from Z5-broken; monopole
density and Polyakov data are reported for that reading without a vote.

## 6. Layer

L6 finite-volume expectations of the selected L4 measure. No lift, no gate.

## Falsifier of the orientation itself

COULOMB_ORIENTATION would be contradicted by any later exact theorem placing
t = 1 in a massive phase, or by a public production with valid classifiers
returning CONFINED; MASSIVE_ORIENTATION symmetrically.
