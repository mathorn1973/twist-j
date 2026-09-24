# RESULT C-PHOTON-CONTRAST-DRIFT-N (2026-09-22)

Status: NON-CANONICAL incubation, engineering orientation, candidate label
candidate-C. No Canon, Registry or Frontier movement. PHOTON-MASSLESS-PHASE
stays O.

    TERMINAL        NO_DRIFT   (aarch64 leg, complete)
    REPRODUCTION    PENDING    (x86_64 leg on the substitute host still running; see ADDENDUM 2)

The terminal is final under the frozen rule for the leg that completed. The
reproduction clause (END hashes chain by chain against the x86_64 leg) is not
yet evaluated. If the x86_64 leg gives a different terminal, STOP_REPRODUCTION
overrides, as preregistered.

## Pins (stored in the project before execution)

    PREREG-C-PHOTON-CONTRAST-DRIFT-N.md   3a86ca2f0e771ffbeacd77004443953697cf03369f5e853630766c29489ffa62
    ADDENDUM-1 (before any measurement)    a7bc7dabc49454bce9d44252c54c83c6446cdde539e7ebdd1dade20d2d6aa228
    ADDENDUM-2 (host substitution, before any analysis)
                                           b461499eb87f1705eb55739737499358886908bc0f94185d8a22ef4f4f7ac007
    zlgt2.c           62be81dc972596f10ff29636888b8b923c56c1c5c393627a24fba8cc1ab6d27c
    jobs_v3.py        3a9b280b3b1f0fb4e46a0baeaac7d5b096645791a0ff328b88b94c8b6f485f04
    analyze_v3.py     8460818640313e30e3b3fde985222dc7f6ecc9f1abe0a870df39fc35e9dae377
    jobs_drift.py     7708c43e36d00e4daad2171b192d34adb5a8782c33fd27cb10495535f5e144b4
    analyze_drift.py  e5a022a5bef7624936216d86a9460471df70dd23d7eb2a84bd84ff7a321acfae

## Execution

aarch64 Linux, gcc 13.3 -O2 -ffp-contract=off, Python 3.12.3. The five
source files were re-hashed on the host after the run and matched. Launched
2026-09-22 22:16 CEST, 20 of 20 chains complete at 23:36 with END lines and
"done" from the runner.

    logs_DR_aarch64.sha256 (manifest of the 20 logs)  8fd4807378a65043266459fc56af8a6f4faba5f9ef52602a84ceeed71721bb96
    END state-hash list                               780bb01732e670a21b452f3e69dfc6d71be7c869636221a41a8fcf68abb87e62
    analysis_DR_aarch64.txt                           0ede6cdce7a37703ac0952759e9055376de4fe633d2cb6b05bfaae984f69e936

x86_64: the first leg was lost in a host reboot (ADDENDUM 2). The restart on
the substitute host began at 23:18 CEST. Its build reproduced the B3 chain
TW_L8_cold1 byte for byte before the drift data. At the measured speed the
L = 32 chains finish at about 02:30 CEST.

## Frozen analysis output

    L   new chains  Delta_L(1)          Delta_L(2)          d_L = P_ref - Delta_L(1)   sigma_L   z
    24  12          0.5962 +- 0.0040    0.6042 +- 0.0020    0.0059                     0.0049    1.21
    32   8          0.6001 +- 0.0071    0.6030 +- 0.0040    0.0021                     0.0076    0.27

    P_ref = 0.602177, SE_P = 0.002859 (frozen)
    Gates: G1 20 of 20 complete; G2 no stationarity failure; G3 every chain
    qualifies, trivial fraction 1.000 in all 20.
    TERMINAL NO_DRIFT   (|z_24| <= 3 and |z_32| <= 3)

By-products, no decision weight:

    L   d_L                  b_L                  25 chi_L
    24  0.697112 +- 3.6e-06  0.600532 +- 0.00012  0.004288 +- 0.004
    32  0.697111 +- 2.3e-06  0.600474 +- 0.00014  0.000377 +- 0.0071

    monopole density 0.011236 at both sizes; Polyakov radius 0.0106 (L = 24),
    0.0051 (L = 32); fraction of planes carrying integer flux 0.59, 0.71.

    INFO refit, B3 points plus new points (analyze_v3.fit):
    Z = 0.6031 +- 0.0012, M = 0.00058 +- 0.00035, chi2 = 9.34, dof = 10.

    Delta_32(1) - Delta_24(1) = +0.004 +- 0.008 (ADDENDUM 1 by-product; the B3
    massive fit predicted about -0.017).

Decimals are computed witnesses, not conclusions.

## Reading fixed in advance, applied

NO_DRIFT: the B3 dip is neither reproduced at L = 24 by independent chains nor
seen at L = 32. A mass of the size fitted in B3 is disfavoured, and the B3
reading extends to L = 32 at this resolution. Engineering grade only.

## Read after the verdict, no decision weight

- The B3 value Delta_24(1) = 0.580 +- 0.011 (two cold chains) and the new
  0.596 +- 0.004 (twelve cold chains) differ by 1.4 combined SE. The B3 dip
  reads as a low fluctuation of two chains. The two B3 hot chains at L = 24,
  excluded as trapped, sat near the plateau (about 0.60, inferred from the
  unconditioned variant V5 of the B3 second reading).
- Against the B3 massive fit taken literally (Z = 0.604, M = 0.0027), the new
  contrasts lie 3.7 SE (L = 24) and 5.0 SE (L = 32) above its prediction.
  These numbers are post hoc and have no decision weight.
- 25 chi_L no longer rises: 0.004 +- 0.004 at L = 24 and 0.000 +- 0.007 at
  L = 32. b_L stays at 0.600 at every size from 8 to 32.
- Resolution: the probe was built to detect M of about 0.002 and larger. The
  refit M = 0.0006 +- 0.0004 is compatible with zero at 1.7 SE. A mass below
  about 0.04 lattice units is not excluded by any finite-size orientation of
  this kind.

## Scope

Engineering orientation of a finite-size estimator, L <= 32, local heat-bath,
cold starts, sector-conditioned. The q_min path is not the ordered S7 limit
(#1125 closure audit). Nothing here is phase evidence in the Canon sense.
