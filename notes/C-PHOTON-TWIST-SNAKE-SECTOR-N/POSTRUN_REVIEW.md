# Post-run review of the preserved execution

**PUBLIC / NON-CANONICAL. Review of RUN.md, RESULT.md and ENGINEERING/ against the pin.**

This is a review pass by an assistant agent in the same working session,
not independent confirmation by another human author. It was made after
the single declared execution of pin
`b79ca3df6d5a4b43358218bcb16076e6edc80930` and reads the preserved
records only; nothing was rerun, no threshold was changed and PREREG.md
and REVIEW.md were not edited.

## Custody

Verified without defect: the eight frozen files are byte-identical to
the pin (hashes as in RUN.md and issue #1265); `ENGINEERING/audit.tsv`
(384 bytes, SHA-256 `c1286c6e…c8533e`) is identical to the pre-pin
transcript in PREREG.md and to the copy embedded in `analyze.py`;
`SHA256SUMS` and `SHA256SUMS_FINAL` verify over every file; every job's
byte count and hash in `execution.json` (42470 bytes) matches its record,
all 136 jobs and the audit exited zero with empty stderr; the analyzer
output `analysis.json` (1779415 bytes, SHA-256 `7ecdfe4c…e688f`) and
`analysis_execution.json` (exit 0, empty stderr) are as RUN.md states;
the binary hash in `environment.json` equals the pre-pin hash of
PREREG.md; the first compilation (08:43:21Z) followed the pin commit
(08:42:04Z) and its readback in the issue; no private path, host name or
model identifier appears in the records.

## Findings and corrections

The review of the first versions of RUN.md and RESULT.md (commit
`a0e6d80`) found no defect in the records themselves and the following
defects in the two descriptive files, all corrected in the commit that
adds this review:

1. RUN.md quoted four job-time ranges that did not match
   `execution.json` (L=10 restricted up-only 893-897 s, top-dwell
   165-167 s; L=8 up-only 248-260 s, top-dwell 66-68 s); corrected to
   868-897 s, 165-168 s, 243-260 s and 66-69 s. The sum of elapsed job
   times was described as CPU-seconds and the platform line named a
   processor count absent from `environment.json`; reworded.
2. RESULT.md's disposition contained a sentence reading a mechanism into
   the fired class-minus gates; removed. Its summary of the gates that
   fired at L=8, k=1 omitted the class-0 G3 firing on the all-slice w=-1
   count, and a sentence claimed endpoint agreement of "the three
   endpoint chains at every size" that this gate contradicts; corrected.
3. "G10 held at every size" was wrong: G10 is read only when both
   class-sum modes pass, which happened at L=4 alone; and G2 was listed
   among the consistency gates although it is an equilibration gate;
   corrected.
4. The untwisted dwell of U chain 4 after its down pass at L=8 and L=10,
   k=2 (mean Y -3.757 and -3.771; 54.75 of 64 and 80.27 of 100 slices at
   w=-1 per sweep; pooled untwisted mean of Y over all chains -0.750 and
   -0.753 against +0.0014 and -0.0003 for chains 0 and 1; no gate, since
   G8a reads chains 0 and 1 only) was not reported; added as descriptive.
5. Quantities that PREREG.md lists as reported were missing: -log R_k/L^2,
   the log10 R_k intervals and product boxes of the passing modes, the
   CONTRAST_NEGLIGIBLE flag, the L=4 residue-law intervals, the
   per-chain control sums of the two k=2 groups, the reset counts by
   parity per (L,k) and the C2 values of the L=6, k=1 group together with
   the four named control failures the analyzer recorded for that
   unqualified group; added.
6. 4 SE half-widths were printed for non-passing modes without the
   NONINFERENTIAL_ESTIMATE label; the label and the sentence explaining
   that the half-widths let the withheld intervals be read off were added.
7. Minor numerical and wording corrections: two control SEs (0.0014),
   one U half-width (0.0053), the lower end of the L=10, k=2 mean-Y
   interval (+1.5034), one l_- difference (2.64), the two halves of the
   L=8, k=1 chain-3 dwell (-3.762, -3.752), the L=4, k=1 qualification
   listing all three fired observables, the description of the
   qualification outcomes by the gate rather than by a sector reading,
   the exact list of P gates that fired at L=8, k=1, the removal of
   "as designed" and of a sentence about P1, the identification of the
   SE quoted with the l_- disagreements, and per-size tables in place of
   sentences that strung values of several sizes together.

Verified correct against the record after the corrections: every value
of the class-sum, inputs, released-interval, unconstrained-route,
step-zero and restricted-ladder tables; the control statuses, the
quoted per-chain values and the per-chain sums; the L=4 variance
decomposition and D; the G11 differences and tolerances; the reset
counts by chain and parity; the endpoint fractions; the L=8, k=1 P
per-chain values recomputed from the block records; the per-size and
overall labels; and the absence of the withheld vocabulary.

## Disposition

The records support the labels the analyzer assigned; RUN.md and
RESULT.md now describe them by the fixed labels and fired gates only.
The frozen rules were applied without change. The item remains
notes-only and NON-CANONICAL; the disposition INCONCLUSIVE_EQUILIBRATION
(UNRESOLVED at L=4) stands; no scientific inference is drawn; Public
Canon v92 is unchanged.
