# Result: one control qualified and passed; class sums recorded, one size unresolved

**PUBLIC / NON-CANONICAL. Engineering disposition: INCONCLUSIVE_EQUILIBRATION.**

The complete frozen run executed once. The implementation audit and all
136 declared jobs completed with exit code zero and empty stderr, the
custody checks of the frozen analyzer found no error, and the analyzer
exited zero. Under the frozen rules of PREREG.md the per-size labels are
UNRESOLVED at L=4 and INCONCLUSIVE_EQUILIBRATION at L=6, L=8 and L=10,
hence INCONCLUSIVE_EQUILIBRATION overall. No exact identity failed in any
qualified group and no consistency gate fired anywhere: G6 fired for no
ladder, G2 for no ladder, G10 held at every size, and G11 held where it
was read. Every estimate below is quoted as recorded; intervals are
withheld except where the frozen rule releases them. This is not a
negative result for the sector-polarization lower bound or P1, and the
numerical output has ZERO scientific evidential weight.

## Exact control groups

Sector qualification precedes the identities. Values are batch
standard errors in parentheses; the identity values of an unqualified
group were computed and are preserved in `ENGINEERING/analysis.json` but
were not read as gates.

| L | k | Qualification | C1: sum of log r_n | C2 middle sums | mean Y at 2k, at 3k | Status |
|---|---|---|---|---|---|---|
| 4 | 1 | chain 2 at source 2k: mean Y -1.137 against +1.501 to +1.509 and all-slice w=-1 fraction 0.674 against 0.036 to 0.037 | +0.212 (0.188), not read | m=1: +0.132 (0.148), not read | +0.844 (pooled), -0.207 (pooled), not read | CONTROL_SECTOR_FROZEN |
| 4 | 2 | four chains agree at both endpoints (w=-1 fractions 0.010-0.011 and 0.023-0.024, w=+1 0.023-0.024 and 0.010, mean Y -0.755 to -0.759 and +0.757 to +0.758) | -0.025 (0.034) | m=1: -0.044 (0.027) | -0.7579 (0.0015), +0.7574 (0.0015) | CONTROL_PASS |
| 6 | 1 | chain 2 at both endpoints: mean Y -2.256 and -1.512 against +1.498 to +1.512 and +2.255 to +2.262; w=-1 fraction 0.915 against 0.052 to 0.057 at 2k, w=+1 fraction 0.051 against 0.914 to 0.915 at 3k | -1.161 (0.128), not read | not read | +0.565, +1.316 (pooled), not read | CONTROL_SECTOR_FROZEN |
| 6 | 2 | chain 3 at source 3k: all-slice w=-1 fraction 0.047 against 0.043 to 0.044 and w=+1 fraction 0.033 against 0.030 to 0.031 (within-chain pooled variance); mean Y +0.759 against +0.753 to +0.757 agrees | -0.047 (0.057), not read | m=1: -0.030 (0.048), m=2: -0.031 (0.034), not read | -0.7544, +0.7555, not read | CONTROL_SECTOR_FROZEN |

Per-chain sums of log r_n: at L=4, k=1 +0.249, +1.800, -1.730, +0.529; at
L=6, k=1 -2.343, -2.315, +2.341, -2.328 (chains 0-3). One control group
was qualified and it passed C1, C2 and C3, so no main group was tainted
and none was capped for want of a qualified control.

## Class-sum route (primary)

Per (L,k): the class-sum log R_k with its 4 SE half-width from the
reported SE (the larger of the delta-method batch SE and the value with
between-chain SEs), the endpoint class weight P_-, the class-sum mean
Y_k with its 4 SE half-width, and the gates that fired. Intervals are
released only for GATES_PASSED modes.

| L | k | log R_k (4 SE) | P_- (4 SE) | mean Y_k (4 SE) | gates fired | label |
|---|---|---|---|---|---|---|
| 4 | 1 | -0.531 (0.117) | 0.00076 (0.0008) | +0.7567 (0.0064) | none | GATES_PASSED |
| 4 | 2 | -1.822 (0.438) | 0.079 (0.051) | +1.211 (0.190) | none | GATES_PASSED |
| 6 | 1 | -0.351 (0.180) | 0.000017 (0.00003) | +0.7551 (0.0045) | none | GATES_PASSED |
| 6 | 2 | -1.856 (0.844) | 0.149 (0.535) | +0.948 (2.019) | CM G3 (l_-: chains -2.560, -0.473), CM G7 (l_- ratio 1.535) | INCONCLUSIVE_EQUILIBRATION |
| 8 | 1 | -0.595 (1.168) | 1.6e-7 (1.1e-6) | +0.7533 (0.0073) | P calibration and every P agreement gate (chain 3), P G7; C0 G3 (all-slice w=-1 count, chains 1 and 2); CM G3 (l_-: chains -16.478, -13.605), CM G7 (1.738) | INCONCLUSIVE_EQUILIBRATION |
| 8 | 2 | -1.845 (1.447) | 0.0075 (0.019) | +1.481 (0.072) | none | GATES_PASSED |
| 10 | 1 | -0.404 (0.314) | 6e-10 (3e-9) | +0.7544 (0.0049) | CM G3 (l_-: chains -18.041, -20.686), CM G7 (1.657) | INCONCLUSIVE_EQUILIBRATION |
| 10 | 2 | -1.780 (0.729) | 0.00022 (0.00034) | +1.5086 (0.0051) | none | GATES_PASSED |

Inputs of the sum rule (log r_0 and pi_1(-) from the P group, l_c from
the restricted ladders, E^{(c)} Y from the three-chain endpoint dwells):

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

(reported SEs of l_c in parentheses; the L=8, k=1 values of log r_0 and
pi_1(-) are the pooled P values of an unqualified group, see the sector
records). At L=4 both modes passed every gate; the k=1 mode met both
half-width conditions and its mean-Y interval excludes zero, the k=2 mode
met the log R half-width condition (0.438 <= 1.0) but not the mean-Y
half-width condition (0.190 > 0.05), the term (E^{(-)}Y - E^{(0)}Y)^2
Var(P_-) supplying 0.00225 of the squared reported SE 0.00225 and the
two class-conditional means 1.7e-06; the volume label is therefore
UNRESOLVED. The squared range from the two product
boxes, quoted under the frozen rule because both log R half-widths are
at most 1.0, is D in [0.166, 0.377], NONINFERENTIAL. At L=8 the k=2 mode
passed every gate with a log R half-width of 1.447 and a mean-Y
half-width of 0.072, neither within its condition; at L=10 the k=2 mode
passed every gate, met both conditions (0.729 and 0.0051) and its mean-Y
interval [+1.5035, +1.5137] excludes zero, while the k=1 mode fired the
class-minus gates listed above. The pairing deficit G2 fired for no
restricted ladder; the largest recorded value was +0.890 (0.390) for the
class-minus ladder at L=10, k=2.

## Unconstrained route (cross-check)

| L | k | log R_k (4 SE) | mean Y_k (4 SE) | per-chain log R_k | gates fired | sub-label | G11 |
|---|---|---|---|---|---|---|---|
| 4 | 1 | -0.475 (0.064) | +0.7577 (0.0048) | -0.436, -0.451, -0.466, -0.520, -0.504 | none | GATES_PASSED | held: log R difference +0.056 within 0.129; log r_0 +0.0013 within 0.0097; pi_1(-) -0.0058 within 0.020 |
| 4 | 2 | -1.787 (0.248) | +1.381 (0.518) | -1.738, -1.932, -1.862, -1.834, -1.573 | G7 (mean Y ratio 1.875) | INCONCLUSIVE_EQUILIBRATION | not read |
| 6 | 1 | -0.494 (0.081) | +0.7558 (0.0064) | -0.461, -0.547, -0.479, -0.446, -0.536 | none | GATES_PASSED | held: -0.143 within 0.197; -0.0010 within 0.011; +0.0008 within 0.031 |
| 6 | 2 | -1.581 (1.481) | +0.756 (3.010) | -1.810, -1.818, -1.999, -2.161, -0.125 | G9' all chains, G3 (mean Y all chains; log R chain 4), G7 both | INCONCLUSIVE_EQUILIBRATION | not read |
| 8 | 1 | -0.475 (0.105) | +0.7544 (0.0052) | -0.456, -0.555, -0.445, -0.446, -0.474 | none | GATES_PASSED | not read (class-sum route fired gates) |
| 8 | 2 | +0.064 (7.592) | +0.755 (3.021) | -1.815, -1.870, -1.688, -1.968, +7.653 | G9' all chains, G3 all chains, G7 both | INCONCLUSIVE_EQUILIBRATION | not read |
| 10 | 1 | -0.430 (0.134) | +0.7543 (0.0056) | -0.450, -0.408, -0.470, -0.423, -0.398 | none | GATES_PASSED | not read (class-sum route fired gates) |
| 10 | 2 | +0.016 (7.546) | +0.756 (3.023) | -1.860, -1.822, -1.694, -2.100, +7.558 | G9' all chains, G3 all chains, G7 (mean Y) | INCONCLUSIVE_EQUILIBRATION | not read |

For k=2 at L=6, L=8 and L=10 chain 4 (started in the alternative layout)
recorded a class-minus fraction of 1.0 throughout its twisted dwell, mean
Y_2 of -2.254, -2.266 and -2.267 and a twisted-slice w=-1 fraction of
0.915, 0.868 and 0.809, against 0.0 and +1.503 to +1.524 for the other
chains; G9' fired at those sizes on both observables, as designed. At L=4,
k=2 chain 4 recorded a class-minus fraction of 0.345 in the first half of
its dwell (mean Y +0.223) and 0.0 in the second half (mean Y +1.504); no
G9' or G5 gate fired there and the pooled mean-Y coarsening ratio 1.875
fired G7. For k=1 the unconstrained route passed every gate at every size
and G11 held at L=4 and L=6, the only sizes where the class-sum route
had fired no gate.

## Sector and step-zero records

- Step-zero group. At L=4, L=6 and L=10 (both modes) and at L=8, k=2 the
  four chains recorded mean Y at twist 0 within 0.006 of zero, between
  0.50 and 18.8 untwisted slices with w != 0 per sweep (equal numbers at
  w=-1 and w=+1), and class-minus fractions at twist 1 of 0.034-0.036
  (L=4, k=1), 0.217-0.225 (L=4, k=2), 0.054-0.058 (L=6, k=1), 0.228-0.236
  (L=6, k=2), 0.247-0.254 (L=8, k=2), 0.109-0.110 (L=10, k=1) and
  0.258-0.273 (L=10, k=2). At L=8, k=1 chain 3 (hot start) recorded mean
  Y at twist 0 of -3.757 in both halves of its 32768-sweep dwell, 57.4 of
  its 64 slices at w != 0 per sweep (54.6 at w=-1, 0.32 at w=+1), and a
  class-minus fraction of 0.899 at twist 1, against -0.001 to +0.001,
  8.1 slices and 0.081 to 0.086 for chains 0-2; the calibration gate on
  the exactly known value E Y_0 = 0 and every P agreement gate fired.
- Restricted class-minus ladders. Reset steps per chain (chains 0, 1):
  k=1: 5, 5 (L=4), 8, 8 (L=6), 16, 14 (L=8), 15, 19 (L=10); k=2: 2, 3
  (L=4), 5, 5 (L=6), 7, 7 (L=8), 5, 2 (L=10); 116 of these 126 resets
  opened a segment at an even twist count. The class-0 ladders recorded
  no reset except two on chain 1 at L=10, k=2, both at odd twist counts. At every size and mode the three
  class-minus endpoint chains, including the chain started in the
  alternative layout at twist L^2, agreed in mean Y, mean W and all-slice
  w=-1 count (the twisted-slice w=-1 fractions were 0.906-0.909, 0.905-
  0.906, 0.861-0.863, 0.806 for k=1 and 0.938-0.941, 0.915-0.916, 0.867-
  0.868, 0.808-0.809 for k=2 at L=4, 6, 8, 10), and the three class-0
  endpoint chains agreed in mean Y, mean W and, except at L=8, k=1 (chains
  1 and 2: 4.48 and 4.34 against 4.36 slices per sweep), in the all-slice
  w=-1 count. The two class-minus ladder chains disagreed in l_- at L=6,
  k=2, L=8, k=1 and L=10, k=1 by 2.09, 2.87 and 2.65 against pooled
  batch SEs of l_- of 0.38 to 0.57, and the pooled l_- coarsening ratio
  exceeded 1.5 at those three (L,k) only.
- Naive against conditional estimators (G6) agreed within 4 SE for F, PF
  and Bw in every restricted ladder and for F and Bw in every
  unconstrained and control ladder.

## Disposition under the frozen rules

The frozen precedence yields UNRESOLVED at L=4 and
INCONCLUSIVE_EQUILIBRATION at L=6, L=8 and L=10, hence
INCONCLUSIVE_EQUILIBRATION overall. The sector qualification separated
the one control group whose four chains agreed at both endpoints, and
that group passed its exact identities, from three groups in which one
chain sat in another sector at an endpoint; under the frozen rule the
identities of those three were not read. The class-sum route produced
per-size values of log R_k and of the endpoint class weight P_- at every
size and mode; at L=6, L=8 and L=10 one or more of its gates fired, in
every case on the class-minus ladder of one mode (chain disagreement in
l_- and the coarsening ratio of l_-) and at L=8, k=1 also on the
step-zero group, where a hot start stayed for its whole twist-0 dwell in
a configuration with mean Y = -3.757. The frozen rule does not
distinguish a class-minus ladder whose two chains differ because the
restricted kernel connects the class slowly from one whose reset steps
place the chains in different parts of the class; the recorded reset
counts and the agreement of the three endpoint chains at every size are
consistent with the first reading, but the rule was fixed before
observation and is not reinterpreted here.

The written finite identities of PROOF.md are unaffected by the run;
they remain candidate-T. The class weights P_- and the class-conditional
means are finite-volume records of this run and carry no thermodynamic
reading. No signed contrast interval, squared range D beyond the L=4
NONINFERENTIAL value, thermodynamic lower bound, phase decision or P1
statement follows from these records. The declared execution is
complete and consumed. Its source, seeds, budget and thresholds are not
extended, tuned or resumed. The positive thermodynamic sector bound, P1
and PHOTON-MASSLESS-PHASE remain open. Public Canon v92 is unchanged.
