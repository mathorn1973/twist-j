# RESULT C-PHOTON-PHASE-ORIENTATION-N, version 3, part B3: the TWIST point t = 1 (2026-09-22)

Status: NON-CANONICAL incubation, engineering orientation, candidate label
candidate-C (finite range, float categorical draws, no exact-arithmetic
claim). No Canon, Registry or Frontier movement. PHOTON-MASSLESS-PHASE stays O.

    TERMINAL        COULOMB_ORIENTATION
    REPRODUCTION    REPRODUCTION_BITWISE   (x86_64 and aarch64, 16 of 16 logs byte-identical)
    CROSSCHECK      CROSSCHECK_PASS        (owner's exact heat-bath pilot, L = 8, logw, z = 0.73)

## Pins

Stored in the project before execution:

    PREREG-C-PHOTON-PHASE-ORIENTATION-N-V3.md     b4799904e59fa870fc81aabcaf8a13efdc685ba2962cf3f6ec44b10cbb1bce29
    PREREG-...-V2-PART-B.md (by reference)        9e92fb8e5fb090a78ee253eaa57dfca9ba617b730016493b646d4d2407c86e3b
    zlgt2.c                                       62be81dc972596f10ff29636888b8b923c56c1c5c393627a24fba8cc1ab6d27c
    jobs_v3.py                                    3a9b280b3b1f0fb4e46a0baeaac7d5b096645791a0ff328b88b94c8b6f485f04
    analyze_v3.py                                 8460818640313e30e3b3fde985222dc7f6ecc9f1abe0a870df39fc35e9dae377

Execution. Primary: x86_64 Linux, 24 logical cores, gcc 11.4 -O2
-ffp-contract=off, Python 3.10.12. Reproduction: aarch64 Linux, gcc 13.3,
same flags, Python 3.12.3. Source files re-hashed on both hosts before the run
and matched. Both runs launched 2026-09-22 21:51 CEST; 16 of 16 chains
completed on each host with an END line and empty stderr.

    logs_B3.sha256 (sha256 manifest of the 16 logs)  ca004f0ce0d663419bf642af0d4bd1ac4f3187b830cd13866500b5684fa2c761  both hosts
    END state-hash list                              c06e3046298044a1fa0acb2ed7fa1ba67288a33ba44bf49810323f0900085cce  both hosts
    analysis_B3.txt                                  5d870f10b66ef8c196be5881a0f76251ccab71ce5e770a08d1c2a9ecaa1dce3a  both hosts
    blocks_B3.tsv  x86_64 / Python 3.10              370a2ac909d5fc2292b13f1cfcf4371d81a2f87954cb1a1a07a0785507fe86e7
    blocks_B3.tsv  aarch64 / Python 3.12             041869b7d1f1a73f63c0d8c564920a289db6ce4020612965c8c8397ec3e0db12

The two block tables differ only in the last digits of the block means:
Python 3.12 changed the built-in sum() over floats to compensated summation.
The decision output is byte-identical. Engineering note for any public
verifier that must be byte-identical across Python versions: do not use the
built-in sum() over floats; use math.fsum or an explicit loop.

## Frozen analysis output (analysis_B3.txt)

    L   qualifying  Delta_L(1)         Delta_L(2)         monopoles  Polyakov  fnz     cos      hot/cold z
    8   4           0.5998 +- 0.0027   0.6026 +- 0.0021   0.01122    0.2282    0.127   0.66529  0.06
    12  2           0.6024 +- 0.0056   0.6042 +- 0.0036   0.01123    0.0994    0.253   0.66522  HOT_TRAPPED
    16  3           0.5898 +- 0.0065   0.6031 +- 0.0026   0.01123    0.0440    0.384   0.66523  0.13
    24  2           0.5801 +- 0.011    0.6003 +- 0.0059   0.01123    0.0106    0.592   0.66522  HOT_TRAPPED

    FIT  Z = 0.604252 +- 0.0016,  M = 0.00269367 +- 0.0011,  chi2 = 2.16, dof = 6
    Rule (a): not met (|Delta_16(1)| and |Delta_24(1)| are far above 3 SE).
    Rule (b): Z - 3 SE(Z) = 0.599 > 0 and M + 2 SE(M) = 0.0049 < thr = 0.017037.
    TERMINAL COULOMB_ORIENTATION

Gates: G1 all 16 logs complete; G2 no stationarity failure; G3 both cold
chains qualify at every L with trivial fraction 1.000; G4 passes where
evaluable (L = 8 z = 0.06, L = 16 z = 0.13) and is not evaluable at L = 12 and
24, where both hot chains froze into nontrivial flux sectors. Trapped and
excluded: L12 hot1, L12 hot2, L16 hot2, L24 hot1 (trivial fraction 0.001),
L24 hot2.

By-products, no decision weight, with d_L = (1 + E X^2)/2:

    L   d_L                   b_L                    25 chi_L
    8   0.696999 +- 5.9e-05   0.600621 +- 0.0003      0.000777 +- 0.0027
    12  0.697111 +- 3.1e-05   0.600510 +- 0.00042    -0.001846 +- 0.0056
    16  0.697105 +- 1.4e-05   0.600013 +- 0.0003      0.010209 +- 0.0066
    24  0.697107 +- 8.3e-06   0.600493 +- 0.0003      0.020361 +- 0.011

The correlator diagnostic at L = 16 (300 samples) deviates from the continuum
ratio target by -2.2 %, +5.5 % and -3.8 % at n = 2, 3, 4; diagnostic only.

Decimals are computed witnesses, not conclusions.

## Break checks

1. Engine against the owner's independent exact heat-bath engine (public
   probe P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2). Script sha256
   536017b3e8cf1e0f1600c01d73e0a64a61de211e390632faa761662aee284664, stored
   in the project before any B3 observable was read; criterion fixed in the
   script (z <= 4 on logw at L = 8, all chains, no conditioning).
   Pilot, from the exact integer flux counts of 4 x 512 samples:
   logw = 1.159847 +- 0.000070. B3: 1.159789 +- 0.000037 (4 x 4000
   measurements, all trivial). z = 0.73: CROSSCHECK_PASS. Secondary: x2
   z = 0.74, cos z = 0.67, cold-only z at most 1.40.
       bc_pilot_summary.txt  c1ebd508a4f88bf491ca6033290ac69200c4e79e33f3a249fd3eefffc0b2699a
       bc_b3_summary.txt     bbd9fd7eda403cd05e2a534a8ca2d34c6ac4a0bc7d12daeb36f7409f2a94100d
       bc_compare.txt        f0a52d7d4b4ca96d505a9c5ee4f0234710e91641e1b23e42eb6dfdf0308c79e3

2. Second reading by an independent code path (script sha256
   3f90ea01271f6c468ac229bd4fc1aac9c58921c52903d6b96590545d03570079, written
   after the terminal was known, stored before it ran, run once, all output
   kept in second_reading_B3.txt, sha256
   df7717be0a7c6d36b8bc40f78a8b0dc4f5d9878b2ba736991b6e5756e326d81b). Batch
   means of 400, autocorrelation-time errors, profile chi2 fit with Z solved
   linearly:

       V1 all qualifying chains       M = 0.0026  2 sigma [0.0006, 0.0046]  COULOMB
       V2 cold chains only            M = 0.0024  2 sigma [0.0003, 0.0046]  COULOMB
       V3 fit without L = 8           M = 0.0032  2 sigma [0.0009, 0.0056]  COULOMB
       V4 tau_int errors              M = 0.0028  2 sigma [0.0007, 0.0049]  COULOMB
       V5 no sector conditioning      M = 0.0013  2 sigma [-0.0002, 0.0028] COULOMB (diagnostic)

   The label survives every variant. The integrated autocorrelation time of
   Delta_24(1) is 15 and 8 measurements, so blocks of 200 span at least 13 of
   them.

## Reading fixed in advance, applied

COULOMB_ORIENTATION: at t = 1 the exact/coexact contrast stays positive down
to L = 24 and no photon mass above about 0.13 lattice units is resolved. It
supports the P1 target b - 25 chi > 0 at engineering grade and says nothing
about S1, P2 or S7.

## What is not hidden

The fitted M is positive at about 2.4 SE, and its two-sigma profile interval
excludes zero in all four valid variants of the second reading. The cause is
the contrast at the two smallest momenta (0.590 at s = 0.152 and 0.580 at
s = 0.068), which lies below the plateau of the larger momenta (about 0.602).
If this is a mass, it is about 0.05 lattice units (correlation length of order
20), far below the resolution of the frozen rule; B3 cannot tell it from a
statistical or finite-size effect. The by-products show where it sits: b_L is
flat at 0.600, and the small rise is in 25 chi_L. A follow-up probe,
C-PHOTON-CONTRAST-DRIFT-N (PREREG sha256
3a86ca2f0e771ffbeacd77004443953697cf03369f5e853630766c29489ffa62), was frozen
and launched to test it with independent chains at L = 24 and L = 32.

## Read after the verdict, no decision weight

The TWIST point sits close to the near-edge Coulomb control C4 (Z_13, beta
11/10) of part A3 in every diagnostic: monopole density 0.0112 against 0.0127,
the fraction of planes carrying integer flux grows with L in the same way
(0.13 to 0.59 against 0.14 to 0.62), the Polyakov radius decays to the noise
level, and hot starts freeze into flux sectors. It is far from the confined
controls (monopole density 0.19 to 0.28, contrast compatible with zero at
L = 24) and from the frozen control (plaquette cosine 0.998).

For the P1 route: if P1 holds, the margin is wide, not thin. At L <= 24 the
contrast is about 0.58 to 0.60 out of d = 0.697, and 25 chi_L is at most about
0.02. Split bounds for b and chi would have room; the open question is only
whether 25 chi_L keeps growing as the momentum goes to zero.

For #757: hot starts with a local heat-bath froze into nontrivial flux sectors
at L = 12, 16 and 24 (5 of 6 hot chains) at the TWIST weight itself. The risk
flagged earlier for the hot/cold gate of the production is therefore real at
this weight for any update set that cannot change flux sectors at L >= 12. The
owner's engine has line and flat-sheet moves designed for this; whether they
equilibrate the sectors at L = 16 to 32 is not tested here.

## Scope

Engineering orientation of a finite-size estimator, L <= 24, local heat-bath,
sector-conditioned. The q_min path is not the ordered S7 limit (#1125 closure
audit). Nothing here is phase evidence in the Canon sense. This text was
offered as the #1116 preregistration; nothing public exists, and if it is
adopted publicly the public pin governs.

## Follow-up and custody (added 2026-09-22, 23:45 CEST)

C-PHOTON-CONTRAST-DRIFT-N returned NO_DRIFT on its completed aarch64 leg:
Delta_24(1) = 0.596 +- 0.004 from 12 new cold chains and Delta_32(1) =
0.600 +- 0.007 from 8, both within 3 SE of the B3 plateau. The B3 dip at
L = 24 reads as a low fluctuation of two chains. See
RESULT-C-PHOTON-CONTRAST-DRIFT-N_2026-09-22.md; its reproduction leg is still
pending.

The x86_64 copies of the B3 logs were lost in a host reboot at about
23:12 CEST. The aarch64 copies are byte-identical (manifest above) and were
moved to a persistent directory; they still match logs_B3.sha256.
