# Result: one exact control failed, ladders and sectors recorded

**PUBLIC / NON-CANONICAL. Engineering disposition: FAIL_CONSISTENCY.**

The complete frozen run executed once. The implementation audit and all
56 declared jobs completed with exit code zero and empty stderr, the
custody checks of the frozen analyzer found no error, and the analyzer
exited zero. Under the frozen rules of PREREG.md the disposition is
FAIL_CONSISTENCY: the exact control group at L=6, k=2 fired gate C1, and
a control failure labels every main group FAIL_CONSISTENCY. Every
estimate below is a NONINFERENTIAL_ESTIMATE; every interval is withheld
and the values are quoted only as recorded. This is not a negative result
for the sector-polarization lower bound or P1, and the numerical output
has ZERO scientific evidential weight.

## Exact control groups

| L | k | C1: sum of log r_n (batch SE) | C2 middle-block sums (batch SE) | mean Y at 2k and at 3k (batch SE) | Status |
|---|---|---|---|---|---|
| 4 | 1 | -0.188 (0.173) | m=1: -0.048 (0.136) | +1.5097 (0.0018), -0.715 (0.262) | CONTROL_PASS |
| 4 | 2 | -0.048 (0.034) | m=1: -0.020 (0.026) | -0.7540 (0.0015), +0.7563 (0.0015) | CONTROL_PASS |
| 6 | 1 | +0.006 (0.146) | m=1: +0.009 (0.120); m=2: -0.006 (0.084) | -0.373 (0.339), +0.376 (0.338) | CONTROL_PASS |
| 6 | 2 | **+0.353 (0.086)** | m=1: +0.168 (0.063); m=2: +0.042 (0.030) | -0.7562 (0.0015), -0.184 (0.293) | FAIL_CONSISTENCY |

At L=6, k=2 the sum that PROOF.md (12) requires to vanish is 4.1 batch
standard errors from zero; C2 and C3 did not fire. The mean of Y at the
3k endpoint of that group, -0.184 with batch SE 0.293, differs from the
value -(-0.7562) that PROOF.md's reversal identity assigns to it, and C3
did not fire only because that standard error is large. The other three
control groups fired no gate.

## Main groups

Values are the pooled estimates of the frozen analyzer with the reported
standard error (the larger of the batch SE and the between-chain SE);
4 SE half-widths are listed so that the withheld intervals can be read
off. Labels are those of the frozen precedence before the control taint.

| L | k | log R_k (4 SE) | mean Y_k at n=L^2 (4 SE) | gates fired before the control taint | label before taint |
|---|---|---|---|---|---|
| 4 | 1 | -0.480 (0.052) | +0.7589 (0.0047) | none | GATES_PASSED |
| 4 | 2 | -1.793 (0.220) | +0.652 (2.545) | G3 chain 4 (mean Y), G7 (mean Y), G9 chain 4 | INCONCLUSIVE_EQUILIBRATION |
| 6 | 1 | -0.489 (0.078) | +0.7554 (0.0114) | G3 chain 3 (mean Y), G9 chain 3 (pure w=0) | INCONCLUSIVE_EQUILIBRATION |
| 6 | 2 | -1.600 (1.339) | +0.754 (3.015) | G3 all chains (mean Y) and chain 4 (log R), G7 both, G9 all chains | INCONCLUSIVE_EQUILIBRATION |
| 8 | 1 | -0.487 (0.104) | +0.7541 (0.0051) | none | GATES_PASSED |
| 8 | 2 | -0.086 (7.482) | +0.754 (3.013) | G3 all chains (log R and mean Y), G7 both | INCONCLUSIVE_EQUILIBRATION |
| 10 | 1 | -0.443 (0.135) | +0.7544 (0.0057) | none | GATES_PASSED |
| 10 | 2 | +0.234 (7.602) | +0.754 (3.015) | G3 all chains (log R and mean Y), G7 (mean Y) | INCONCLUSIVE_EQUILIBRATION |

For k=1 the forward-reverse gate G2, the direction gate G4, the
naive-conditional gate G6 and the calibration gate G8a fired at no size,
and the alternative-sector chain 4 recorded the same log R and mean Y as
the other chains at every size. The equal-weight and Bennett secondary
estimates of log R_1 lie within one batch SE of the primary estimate at
every size. The cross-mode positivity check G10 was applicable at L=8
and L=10 and held; at L=4 and L=6 it was not applicable because G9 had
fired.

For k=2 the chains separate. Per-chain values of log R_2 and of mean
Y_2 at the twisted dwell (chain order cold0, hot0, coldT, hotT,
coldAltT; pooled within-chain SE of log R in parentheses):

| L | log R_2 per chain (SE) | mean Y_2 per chain |
|---|---|---|
| 4 | -1.80, -1.93, -1.83, -1.80, -1.61 (0.13) | +1.51, +1.50, +1.50, +0.52, -1.78 |
| 6 | -1.97, -1.88, -1.99, -1.90, -0.26 (0.22) | +1.51, +1.51, +1.51, +1.50, -2.26 |
| 8 | -1.84, -2.08, -1.95, -1.94, +7.40 (0.14) | +1.50, +1.51, +1.51, +1.51, -2.26 |
| 10 | -1.40, -1.77, -1.76, -1.74, +7.83 (0.18) | +1.51, +1.51, +1.50, +1.51, -2.26 |

At L=4 chain 3 recorded mean Y_2 of -0.47 in the first half and +1.50 in
the second half of its twisted dwell, and chain 4 spent 37 percent of
its dwell sweeps in the pure w=-1 layout against at most 11 percent for
any other chain. At L=6, 8 and 10 chain 4 recorded mean Y_2 of -2.26
throughout its dwell and every other chain +1.50 to +1.51. At L=8 and
L=10 chain 4's log R_2 of +7.4 and +7.8 lies outside the exact bound
R_k <= 1 of PROOF.md by a wide margin; those two values are recorded as
they are and enter the pooled estimate and the between-chain SE by the
frozen rule. The untwisted dwell that chain 4 reached after its down
pass at L=8 and L=10 recorded a mean of Y of -3.76 and -3.77, with 57 of
64 and 88 of 100 untwisted slices carrying w!=0 per sweep, while chains
0 to 3 recorded means within 0.007 of zero with 8 and 19 such slices per
sweep.

## Sector records

Fractions of twisted-dwell sweeps in a pure layout (pooled over the
five chains) and label changes per chain:

| L | k=1 pure w=0 | k=1 changes per chain | k=2 pure w=0 / pure w=-1 | k=2 changes per chain |
|---|---|---|---|---|
| 4 | 0.590 | about 6500 | 0.400 / 0.097 | about 6500 |
| 6 | 0.067 | 1700 to 2100 | 0.049 / 0.009 | 1400 to 1900 |
| 8 | 0.000 | 2 to 8 | 0.000 / 0.000 | 2 to 8 |
| 10 | 0.000 | 0 | 0.000 / 0.000 | 0 |

At L=8 and L=10 no chain of either mode attained a pure layout at any
sweep of its twisted dwell, so the pure-layout occupancies compared by
G9 were all zero and G9 could not fire there; the chain-4 separation at
those sizes was recorded by G3 instead. The pooled fraction of twisted
slices with w=-1 at the twisted dwell for k=2 was 0.24, 0.22, 0.23 and
0.24 at L=4, 6, 8 and 10, of which chain 4 supplies its whole share at
L=6, 8 and 10. Because no down pass of chain 2 or chain 4 stayed pure,
the sector-conditional descriptive was not formed at any size.

## Disposition under the frozen rules

The frozen precedence yields FAIL_CONSISTENCY at every size and overall.
The frozen rule does not distinguish a control identity violated by an
implementation defect from one violated by chains that did not reach the
stationary law of an endpoint within the schedule; the other three
control groups, the naive-conditional gate G6 at every size, the
calibration gate G8a at every size, the audit's exact local enumeration
and the k=1 records are consistent with the second reading, but the rule
was fixed before observation and is not reinterpreted here. Separating
the two readings needs a successor with its own pin, for example a
control group whose chains must agree in sector before its identity
gates are read, and a sector gate that does not rely on pure layouts at
sizes where none occur.

The written finite identities of PROOF.md are unaffected by the run;
they remain candidate-T. The exact bound R_k <= 1 that chain 4 violates
at L=8 and L=10 is a statement about the stationary measures, and the
recorded value is a finite trajectory's estimate, not a counterexample.
No signed contrast interval, squared range D, thermodynamic lower bound,
phase decision or P1 statement follows from these records. The declared
execution is complete and consumed. Its source, seeds, budget and
thresholds are not extended, tuned or resumed. The positive
thermodynamic sector bound, P1 and PHOTON-MASSLESS-PHASE remain open.
Public Canon v92 is unchanged.
