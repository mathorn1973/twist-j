# Review of the first frozen execution

**PUBLIC / NON-CANONICAL. Disposition: FAIL_CONSISTENCY.**

This continues the same-session assistant review recorded in REVIEW.md;
it is not independent confirmation by another human author. The reviewed
source pin is `1c82ae6ff83d8f7e7ed6c4b1ad7a3256f29e9422`. The preserved
outputs, RUN.md and RESULT.md reviewed here are published in
`33e21ebe2a1f10e7bc1e4a168c4b03a2851778e8`.

## Custody and execution

The eight frozen files are byte-identical between the two commits and
their SHA-256 values equal the RUN.md table. `SHA256SUMS_FINAL` verifies
over the other 120 files of `ENGINEERING/`. I read the manifests and the
analyzer output with Python and recomputed descriptive sums from the block
records; I did not rerun the sampler, audit, controller or analyzer.

`execution.json` (17345 bytes, the hash RUN.md records) holds 57 records,
the audit and the 56 declared jobs, each with exit 0 and zero stderr
bytes; every stdout byte count and hash equals the preserved `.tsv`, every
`.stderr` file is empty, and all 56 block files carry the frozen row count
for their L, 39 fields per row and the completion line. `audit.tsv` is the
238-byte transcript of PREREG.md and of the copy embedded in `analyze.py`.
`environment.json` records four workers, 600 s and 2400 s timeouts and the
binary hash declared in PREREG.md. `analysis_execution.json` records
analyzer exit 0, empty stderr and a 639195-byte stdout whose hash is that
of `analysis.json` and of RUN.md; that file lists 56 runs, no missing run
and no execution error. RUN.md's durations match the manifest (longest job
L=10, k=2, chain 3 at 665.809 s). The UTC times are in no preserved file;
the 2273 s controller wall time is consistent with 7.1 s of audit plus
9056 s of job time on four workers. The issue record and the public
read-back were not checked here.

## Verification of RESULT.md values

Every value in the control, main, per-chain k=2 and sector tables and in
the prose was traced to `analysis.json` (`controls[]`,
`volumes[].modes[]`, `modes[].chains[]`, `sector_*`) or recomputed from
the block records. All agree to the stated precision except:

- L=6, k=1: the 4 SE half-width of mean Y_1 is 4 x 0.002869 = 0.0115, not
  0.0114. L=8, k=1: the 4 SE half-width of log R_1 is 4 x 0.026147 = 0.105,
  not 0.104. Both truncate the last digit.
- "At L=8 and L=10 no chain of either mode attained a pure layout at any
  sweep of its twisted dwell" holds at L=10, not at L=8, where each chain
  recorded 1 to 4 pure w=0 sweeps out of 16384 (13 pooled for k=1, 15 for
  k=2) and chain 4 of k=2 one pure w=-1 sweep. The tabulated 0.000 is
  correct to three decimals; G9 compared these occupancies and did not fire.
- "of which chain 4 supplies its whole share at L=6, 8 and 10": chain 4's
  twisted slices carry w=-1 in 0.91, 0.87 and 0.81 of its slice-sweeps and
  chains 0 to 3 in about 0.05, 0.075 and 0.10 each, so chain 4 accounts for
  about 81, 74 and 66 percent of the pooled fractions, not all of them.
- L=6, k=2 label changes per chain are 1376 to 1883; "1400 to 1900" rounds.

These four descriptive items were found in the RESULT.md of the outputs
commit named above; they are corrected in the RESULT.md of the commit
that adds this review, with no change to any recorded value, label,
threshold or preserved file.

Checks that hold: C1 at L=6, k=2 is +0.3533 with batch SE 0.0859, 4.11 SE
from zero; C2 and C3 (0.940 against 1.170) did not fire; the other three
control groups fired no gate. The "label before taint" column is not a
recorded field, since `analysis.json` labels every mode FAIL_CONSISTENCY;
it follows from the recorded `diagnostic_failures` and `sector_failures`
lists under the PREREG.md mapping, each entry checks, and no mode failed
G9 alone. The equal-weight and Bennett (`log_R_bar`) values of log R_1
lie within 0.91 batch SE of the primary at every L; the chain-4 values
(log R_2, dwell halves, untwisted-dwell mean Y and w!=0 slice counts at
L=8 and L=10) were recomputed from the block records and agree.

## Disposition under the frozen rules

The analyzer's precedence list and thresholds equal PREREG.md's.
`control:exact_control_group_failed` appears in all eight main modes;
every mode, volume and the overall status read FAIL_CONSISTENCY; every
estimate is labelled NONINFERENTIAL_ESTIMATE and every inferential
interval field is null. RESULT.md applies the rule as written: one control
failure taints all four sizes; no interval is quoted as inferential, the
4 SE half-widths standing under the NONINFERENTIAL label; mixed,
transport, mobility improvement and "guides the proof" are absent and
"equilibrat-" occurs only inside the fixed label INCONCLUSIVE_EQUILIBRATION;
no trend, fit, area-law, collapse or other cross-L comparison is drawn; no
thermodynamic, phase, P1 or Canon statement is made; the run is declared
consumed.

RESULT.md's descriptive reading of the control failure is supported by the
records without relabelling. From `L6_k2_b2_c*.tsv`, mean Y over the 16384
dwell sweeps at n=0 (source 2k) is -0.7569, -0.7560, -0.7555, -0.7564 for
chains 0 to 3; at n=36 (source 3k) it is +0.7614, +0.7563, +0.7534 and
-3.0051. The last is chain 3, started from uniform links at n=36; its
dwell halves read -3.006 and -3.005 and its twisted slices carried w=-1 in
0.906 of slice-sweeps against 0.04 for chains 0 to 2. The pooled values
-0.7562 and -0.1835 are the analyzer's C3 inputs. Three chains sit within
0.005 of the value +0.7562 that PROOF.md's reversal identity assigns to
the 3k endpoint; one does not and did not leave its state within the
schedule. These are descriptive statements about one finite trajectory;
the frozen rule does not separate an implementation defect from a chain
that has not reached the endpoint's stationary law, and this review does
not decide between them or alter the label.

## Scope of the conclusion

The frozen attempt failed its exact-control qualification. No signed
contrast interval, squared range, thermodynamic lower bound, phase or P1
decision is supported by these trajectories; the chain-4 values above the
exact bound R_k <= 1 are finite-trajectory estimates, not counterexamples
to PROOF.md, whose identities keep their candidate-T scope. Thresholds,
budget, seeds and identifier are unchanged since the pin; no job was
retried; PREREG.md and REVIEW.md are unchanged since the pin. The attempt
is consumed and any successor requires its own prospective pin. Public
Canon v92 and the open P1 target remain unchanged; these records have ZERO
scientific evidential weight under the preregistration.
