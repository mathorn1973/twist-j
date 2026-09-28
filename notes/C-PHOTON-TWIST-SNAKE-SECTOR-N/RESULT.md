# Result: one control qualified and passed; class sums recorded, one size unresolved

**PUBLIC / NON-CANONICAL. Engineering disposition: INCONCLUSIVE_EQUILIBRATION.**

The complete frozen run executed once. The implementation audit and all
136 declared jobs completed with exit code zero and empty stderr, the
custody checks of the frozen analyzer found no error, and the analyzer
exited zero. Under the frozen rules of PREREG.md the per-size labels are
UNRESOLVED at L=4 and INCONCLUSIVE_EQUILIBRATION at L=6, L=8 and L=10,
hence INCONCLUSIVE_EQUILIBRATION overall. No exact identity failed in the
one qualified control group and no consistency gate fired anywhere: G6
fired for no ladder, G11 held where it was read (L=4 and L=6, k=1) and
G10 held at L=4, the only size where it was read. The pairing gate G2,
which is not a consistency gate, fired for no ladder. Every estimate below is quoted as recorded;
intervals are released only for GATES_PASSED modes, and the 4 SE
half-widths of the other modes are listed so that the withheld intervals
can be read off; those values carry the label NONINFERENTIAL_ESTIMATE.
The numerical output has ZERO scientific evidential weight.

## Exact control groups

The leave-one-out sector qualification (all-slice w=-1 count, all-slice
w=+1 count and mean Y of each chain against the other three at both
endpoint dwells, 4 SE with within-chain pooled variance) precedes the
identities. The identity values of an unqualified group were computed by
the analyzer and are preserved in `ENGINEERING/analysis.json`, but they
were not read as gates; they are quoted here in full for that reason.
Batch standard errors in parentheses.

| L | k | Qualification outcome | C1: sum of log r_n | C2 middle sums | mean Y at 2k, at 3k | Status |
|---|---|---|---|---|---|---|
| 4 | 1 | failed for chain 2 at source 2k on all three observables: mean Y -1.137 against +1.501 to +1.509; w=-1 fraction 0.674 against 0.036 to 0.037; w=+1 fraction 0.0024 against 0.0067 to 0.0071 | +0.212 (0.188), not read | m=1: +0.132 (0.148), not read | +0.844 (0.249), -0.207 (0.305), not read | CONTROL_SECTOR_FROZEN |
| 4 | 2 | passed: w=-1 fractions 0.010 to 0.011 (2k) and 0.023 to 0.024 (3k), w=+1 fractions 0.023 to 0.024 and 0.010, mean Y -0.755 to -0.759 and +0.757 to +0.758 | -0.025 (0.034), read | m=1: -0.044 (0.027), read | -0.7579 (0.0014), +0.7574 (0.0014), read | CONTROL_PASS |
| 6 | 1 | failed for chain 2 at both endpoints on all three observables: mean Y -2.256 and -1.512 against +1.498 to +1.512 and +2.255 to +2.262; w=-1 fraction 0.915 against 0.052 to 0.057 (2k); w=+1 fraction 0.0014 against 0.025 to 0.027 (2k) and 0.051 against 0.914 to 0.915 (3k) | -1.161 (0.128), not read | m=1: -0.770 (0.106), m=2: -0.391 (0.073), not read | +0.565 (0.293), +1.316 (0.293), not read | CONTROL_SECTOR_FROZEN |
| 6 | 2 | failed for chain 3 at source 3k on the two slice counts: w=-1 fraction 0.047 against 0.043 to 0.044, w=+1 fraction 0.033 against 0.030 to 0.031; mean Y +0.759 against +0.753 to +0.757 passed | -0.047 (0.057), not read | m=1: -0.030 (0.048), m=2: -0.031 (0.034), not read | -0.7544 (0.0013), +0.7555 (0.0015), not read | CONTROL_SECTOR_FROZEN |

For the L=6, k=1 group the analyzer recorded the named failures
`control:total_log_ratio_nonzero`, `control:row_symmetry_m1`,
`control:row_symmetry_m2` and `control:mean_Y_reversal_antisymmetry`;
under the sector rule they were not read and the group's status is
CONTROL_SECTOR_FROZEN. At L=4, k=1 the four chains recorded mean Y at
source 3k of -0.427, -1.495, +0.705 and +0.388 and w=+1 fractions there
of 0.297, 0.038, 0.569 and 0.493; no qualification gate fired at that
endpoint because the within-chain variances are large. Per-chain sums of
log r_n (chains 0-3): L=4, k=1: +0.249, +1.800, -1.730, +0.529; L=4,
k=2: +0.008, +0.000, -0.175, +0.065; L=6, k=1: -2.343, -2.315, +2.341,
-2.328; L=6, k=2: -0.241, +0.076, -0.089, +0.065. One control group was
qualified and it passed C1, C2 and C3, so no main group was tainted and
none was capped for want of a qualified control.

## Class-sum route (primary)

Per (L,k): the class-sum log R_k with its 4 SE half-width from the
reported SE (the larger of the delta-method batch SE and the value with
between-chain SEs), -log R_k/L^2, the endpoint class weight P_-, the
class-sum mean Y_k with its 4 SE half-width, the gates that fired and the
label. The CONTRAST_NEGLIGIBLE flag is false at every (L,k).

| L | k | log R_k (4 SE) | -log R_k/L^2 | P_- (4 SE) | mean Y_k (4 SE) | gates fired | label |
|---|---|---|---|---|---|---|---|
| 4 | 1 | -0.531 (0.117) | 0.0332 | 0.00076 (0.0008) | +0.7567 (0.0064) | none | GATES_PASSED |
| 4 | 2 | -1.822 (0.438) | 0.1139 | 0.079 (0.051) | +1.211 (0.190) | none | GATES_PASSED |
| 6 | 1 | -0.351 (0.180) | 0.0097 | 0.000017 (0.00003) | +0.7551 (0.0045) | none | GATES_PASSED |
| 6 | 2 | -1.856 (0.844) | 0.0516 | 0.149 (0.535) | +0.948 (2.019) | CM G3 on l_- (chains -2.560, -0.473), CM G7 (l_- ratio 1.535) | INCONCLUSIVE_EQUILIBRATION, NONINFERENTIAL_ESTIMATE |
| 8 | 1 | -0.595 (1.168) | 0.0093 | 1.6e-7 (1.1e-6) | +0.7533 (0.0073) | P calibration (mean Y at twist 0), P chain-agreement gates on the class-minus fraction, mean Y at twists 0 and 1, F_0 and Bw_0 (all four chains flagged), P G7 (three ratios); C0 G3 on the all-slice w=-1 count (chains 1 and 2); CM G3 on l_- (chains -16.478, -13.605), CM G7 (1.738) | INCONCLUSIVE_EQUILIBRATION, NONINFERENTIAL_ESTIMATE |
| 8 | 2 | -1.845 (1.447) | 0.0288 | 0.0075 (0.019) | +1.481 (0.072) | none | GATES_PASSED |
| 10 | 1 | -0.404 (0.314) | 0.0040 | 6e-10 (3e-9) | +0.7544 (0.0049) | CM G3 on l_- (chains -18.041, -20.686), CM G7 (1.657) | INCONCLUSIVE_EQUILIBRATION, NONINFERENTIAL_ESTIMATE |
| 10 | 2 | -1.780 (0.729) | 0.0178 | 0.00022 (0.00034) | +1.5086 (0.0051) | none | GATES_PASSED |

Inputs of the sum rule (log r_0 and pi_1(-) from the P group, l_c from
the restricted ladders with reported SEs, E^{(c)} Y from the three-chain
endpoint dwells):

| L | k | log r_0 | pi_1(-) | l_0 | l_- | E^{(0)} Y | E^{(-)} Y |
|---|---|---|---|---|---|---|---|
| 4 | 1 | -0.2375 | 0.0348 | -0.259 (0.029) | -4.114 (0.265) | +0.7595 | -2.919 |
| 4 | 2 | -0.8021 | 0.2200 | -0.854 (0.118) | -2.042 (0.127) | +1.5074 | -2.235 |
| 6 | 1 | -0.2364 | 0.0556 | -0.057 (0.045) | -8.214 (0.427) | +0.7552 | -3.003 |
| 6 | 2 | -0.7913 | 0.2320 | -0.962 (0.168) | -1.509 (1.043) | +1.5087 | -2.261 |
| 8 | 1 | -0.2164 | 0.2869 | -0.041 (0.056) | -14.772 (1.437) | +0.7533 | -3.013 |
| 8 | 2 | -0.7963 | 0.2499 | -0.768 (0.364) | -4.561 (0.523) | +1.5096 | -2.263 |
| 10 | 1 | -0.2356 | 0.1097 | -0.052 (0.078) | -19.198 (1.322) | +0.7544 | -3.017 |
| 10 | 2 | -0.7930 | 0.2638 | -0.681 (0.182) | -8.077 (0.337) | +1.5094 | -2.264 |

The L=8, k=1 values of log r_0 and pi_1(-) are the pooled values of the
P group whose gates fired there (see the step-zero records).

Released intervals and derived quantities of the GATES_PASSED modes:

| L | k | log R_k interval | log10 R_k interval | mean Y_k interval | product box R x Y | half-width conditions |
|---|---|---|---|---|---|---|
| 4 | 1 | [-0.648, -0.414] | [-0.281, -0.180] | [+0.7502, +0.7631] | [0.393, 0.504] | both met; Y interval excludes zero |
| 4 | 2 | [-2.260, -1.384] | [-0.982, -0.601] | [+1.021, +1.401] | [0.107, 0.351] | log R met (0.438 <= 1.0); mean Y not met (0.190 > 0.05) |
| 6 | 1 | [-0.531, -0.171] | [-0.231, -0.074] | [+0.7507, +0.7596] | [0.442, 0.640] | both met; Y interval excludes zero |
| 8 | 2 | [-3.292, -0.398] | [-1.430, -0.173] | [+1.410, +1.553] | [0.052, 1.043] | neither met (1.447 > 1.0; 0.072 > 0.05) |
| 10 | 2 | [-2.509, -1.051] | [-1.090, -0.456] | [+1.5034, +1.5137] | [0.122, 0.529] | both met (0.729; 0.0051); Y interval excludes zero |

At L=4 the k=2 mean-Y half-width is set by the class-weight term: of the
squared reported SE 0.00225, the term (E^{(-)}Y - E^{(0)}Y)^2 Var(P_-)
supplies 0.00225 and the two class-conditional means 1.7e-6; the volume
label is therefore UNRESOLVED. The squared range from the two product
boxes, quoted under the frozen rule because both L=4 log R half-widths
are at most 1.0, is D in [0.166, 0.377] (log10 D in [-0.781, -0.423]),
NONINFERENTIAL; the L=4 residue-law intervals of #1259 PROOF.md (14),
formed from the batch-SE corners, are p_0 in [0.460, 0.547], p_{+-1} in
[0.198, 0.241] and p_{+-2} in [0.0017, 0.0563]. At L=6, L=8 and L=10 one
mode fired a gate, so neither the squared range nor G10 nor the
residue-law intervals were read there. The pairing deficit G2 fired for
no restricted ladder; the largest recorded value was +0.890 (0.390) for
the class-minus ladder at L=10, k=2.

## Unconstrained route (cross-check)

4 SE half-widths from the reported SE; rows whose sub-label is not
GATES_PASSED carry NONINFERENTIAL_ESTIMATE.

| L | k | log R_k (4 SE) | mean Y_k (4 SE) | per-chain log R_k (chains 0-4) | gates fired | sub-label | G11 |
|---|---|---|---|---|---|---|---|
| 4 | 1 | -0.475 (0.064) | +0.7577 (0.0048) | -0.436, -0.451, -0.466, -0.520, -0.504 | none | GATES_PASSED | held: log R difference +0.056 within 0.129; log r_0 +0.0013 within 0.0097; pi_1(-) -0.0058 within 0.020 |
| 4 | 2 | -1.787 (0.248) | +1.381 (0.518) | -1.738, -1.932, -1.862, -1.834, -1.573 | G7 (mean Y ratio 1.875) | INCONCLUSIVE_EQUILIBRATION | not read |
| 6 | 1 | -0.494 (0.081) | +0.7558 (0.0064) | -0.461, -0.547, -0.479, -0.446, -0.536 | none | GATES_PASSED | held: -0.143 within 0.197; -0.0010 within 0.011; +0.0008 within 0.031 |
| 6 | 2 | -1.581 (1.481) | +0.756 (3.010) | -1.810, -1.818, -1.999, -2.161, -0.125 | G9' (class-minus fraction and w=-1 count, all chains), G3 (mean Y, all chains; log R, chain 4), G7 (both) | INCONCLUSIVE_EQUILIBRATION | not read |
| 8 | 1 | -0.475 (0.105) | +0.7544 (0.0053) | -0.456, -0.555, -0.445, -0.446, -0.474 | none | GATES_PASSED | not read: class-sum route fired gates |
| 8 | 2 | +0.064 (7.592) | +0.755 (3.021) | -1.815, -1.870, -1.688, -1.968, +7.653 | G9' (both observables, all chains), G3 (both, all chains), G7 (both) | INCONCLUSIVE_EQUILIBRATION | not read |
| 10 | 1 | -0.430 (0.134) | +0.7543 (0.0056) | -0.450, -0.408, -0.470, -0.423, -0.398 | none | GATES_PASSED | not read: class-sum route fired gates |
| 10 | 2 | +0.016 (7.546) | +0.756 (3.023) | -1.860, -1.822, -1.694, -2.100, +7.558 | G9' (both observables, all chains), G3 (both, all chains), G7 (mean Y) | INCONCLUSIVE_EQUILIBRATION | not read |

Chain 4 (started in the alternative layout) records, k=2, per size:

| L | class-minus fraction at the twisted dwell | mean Y_2 at the twisted dwell (other chains) | twisted-slice w=-1 fraction (other chains) | untwisted dwell after the down pass: mean Y_0, untwisted slices at w=-1 per sweep |
|---|---|---|---|---|
| 4 | 0.345 in the first half, 0.0 in the second | +0.223, +1.504 by half (+1.505 to +1.513) | 0.191 (0.035 to 0.036) | -0.002; 0.25 of 16 |
| 6 | 1.0 | -2.254 (+1.503 to +1.512) | 0.915 (0.052 to 0.053) | -0.000; 1.30 of 36 |
| 8 | 1.0 | -2.266 (+1.508 to +1.512) | 0.868 (0.075 to 0.077) | -3.757; 54.75 of 64 (0.31 at w=+1, 2.37 other) |
| 10 | 1.0 | -2.267 (+1.506 to +1.524) | 0.809 (0.102 to 0.103) | -3.771; 80.27 of 100 (0.82 at w=+1, 6.65 other) |

The untwisted-dwell records at L=8 and L=10 are descriptive: the pooled
mean of Y at twist 0 over all five chains is -0.750 (0.241) and -0.753
(0.242) against +0.0014 (0.0020) and -0.0003 (0.0022) for chains 0 and 1,
and no gate reads them, since G8a is formed from chains 0 and 1 only. For
k=1 the unconstrained route passed every gate at every size.

## Step-zero and sector records

Step-zero group, per chain (chains 0-3; cold, hot, cold, hot starts at
twist 0): mean Y at twist 0, untwisted slices with w != 0 per sweep at
twist 0, class-minus fraction at twist 1.

| L | k | mean Y at twist 0 | slices with w != 0 per sweep | class-minus fraction at twist 1 |
|---|---|---|---|---|
| 4 | 1 | -0.003, +0.001, +0.004, -0.001 | 0.51, 0.50, 0.50, 0.51 | 0.034, 0.034, 0.036, 0.035 |
| 4 | 2 | -0.002, -0.001, +0.001, -0.002 | 0.50, 0.50, 0.50, 0.51 | 0.218, 0.225, 0.220, 0.217 |
| 6 | 1 | -0.002, +0.001, -0.001, -0.003 | 2.63, 2.65, 2.64, 2.67 | 0.055, 0.054, 0.058, 0.054 |
| 6 | 2 | +0.002, +0.001, +0.000, +0.002 | 2.65, 2.63, 2.64, 2.65 | 0.236, 0.233, 0.230, 0.228 |
| 8 | 1 | +0.000, -0.001, +0.001, -3.757 (halves -3.762, -3.752) | 8.09, 8.12, 8.10, 57.37 (54.63 at w=-1, 0.32 at w=+1) | 0.082, 0.081, 0.086, 0.899 |
| 8 | 2 | -0.001, -0.004, -0.002, +0.001 | 8.11, 8.11, 8.13, 8.12 | 0.250, 0.254, 0.248, 0.247 |
| 10 | 1 | -0.001, +0.000, +0.003, -0.002 | 18.78, 18.83, 18.77, 18.75 | 0.110, 0.110, 0.110, 0.109 |
| 10 | 2 | +0.002, +0.000, +0.002, +0.001 | 18.75, 18.78, 18.71, 18.83 | 0.258, 0.273, 0.266, 0.259 |

At every (L,k) except L=8, k=1 the slices with w != 0 at twist 0 were
equally split between w=-1 and w=+1 and the calibration gate on the
exactly known value E Y_0 = 0 held. At L=8, k=1 chain 3 fired the
calibration gate (pooled mean Y at twist 0 -0.939 with batch SE 0.205)
and the chain-agreement gates named above.

Restricted ladders, per (L,k): reset steps per ladder chain (chains 0,
1) and by parity of the twist count reached; the two chains' values of
l_-; the coarsening ratio of the pooled l_-; the twisted-slice w=-1
fraction of the three class-minus endpoint chains (chains 0, 1 and the
chain started in the alternative layout at twist L^2) and of the three
class-0 endpoint chains.

| L | k | CM resets (chains 0, 1; even, odd twist) | l_- by chain | l_- ratio | CM endpoint w=-1 fraction | C0 endpoint w=-1 fraction | C0 resets |
|---|---|---|---|---|---|---|---|
| 4 | 1 | 5, 5 (10, 0) | -4.250, -3.954 | 1.177 | 0.908, 0.909, 0.906 | 0.024, 0.024, 0.023 | none |
| 4 | 2 | 2, 3 (5, 0) | -2.053, -2.030 | 1.215 | 0.939, 0.941, 0.938 | 0.036, 0.036, 0.036 | none |
| 6 | 1 | 8, 8 (14, 2) | -8.270, -8.375 | 1.495 | 0.906, 0.906, 0.905 | 0.043, 0.044, 0.044 | none |
| 6 | 2 | 5, 5 (8, 2) | -2.560, -0.473 | 1.535 | 0.916, 0.916, 0.915 | 0.052, 0.052, 0.053 | none |
| 8 | 1 | 16, 14 (28, 2) | -16.478, -13.605 | 1.738 | 0.863, 0.861, 0.862 | 0.068, 0.070, 0.068 | none |
| 8 | 2 | 7, 7 (13, 1) | -5.066, -4.021 | 1.336 | 0.867, 0.868, 0.867 | 0.076, 0.076, 0.075 | none |
| 10 | 1 | 15, 19 (31, 3) | -18.041, -20.686 | 1.657 | 0.806, 0.806, 0.806 | 0.095, 0.095, 0.096 | none |
| 10 | 2 | 5, 2 (7, 0) | -8.073, -8.093 | 1.048 | 0.809, 0.808, 0.809 | 0.102, 0.103, 0.102 | chain 1: 2 (0, 2) |

At every (L,k) the three class-minus endpoint chains agreed in mean Y,
mean W and all-slice w=-1 count, and the three class-0 endpoint chains
agreed in mean Y and mean W; the class-0 all-slice w=-1 count fired G3 at
L=8, k=1 for chains 1 and 2 (4.48 and 4.34 against 4.36 slices per sweep
for chain 0). The two class-minus ladder chains disagreed in l_- at L=6,
k=2, L=8, k=1 and L=10, k=1 by 2.09, 2.87 and 2.64 (the aggregate batch
SEs of the pooled l_- there are 0.38, 0.57 and 0.50; the gate's own
tolerance is the within-chain pooled value, which is not recorded), and
the pooled l_- coarsening ratio exceeded 1.5 at those three (L,k) only.
Naive against conditional estimators (G6) agreed within 4 SE for F, PF
and Bw in every restricted ladder and for F and Bw in every unconstrained
and control ladder.

## Disposition under the frozen rules

The frozen precedence yields UNRESOLVED at L=4 and
INCONCLUSIVE_EQUILIBRATION at L=6, L=8 and L=10, hence
INCONCLUSIVE_EQUILIBRATION overall. The sector qualification passed for
one control group, which then passed its exact identities, and failed
for three groups, whose identity values were recorded but not read. The
class-sum route recorded log R_k, the endpoint class weight P_- and the
class-sum mean Y_k at every size and mode; the gates that fired at L=6,
L=8 and L=10 are, per (L,k), those listed in the class-sum table: the
class-minus ladder gates G3 and G7 of one mode at each of the three
sizes, and at L=8, k=1 also the class-0 ladder gate G3 on the all-slice
w=-1 count and the calibration and chain-agreement gates of the step-zero
group. The rule was fixed before observation and is not reinterpreted
here.

The written finite identities of PROOF.md are unaffected by the run;
they remain candidate-T. The class weights P_- and the class-conditional
means are finite-volume records of this run and carry no thermodynamic
reading. No signed contrast interval, squared range D beyond the L=4
NONINFERENTIAL value, thermodynamic lower bound, phase decision or P1
statement follows from these records. The declared execution is
complete and consumed. Its source, seeds, budget and thresholds are not
extended, tuned or resumed. The positive thermodynamic sector bound, P1
and PHOTON-MASSLESS-PHASE remain open. Public Canon v92 is unchanged.
