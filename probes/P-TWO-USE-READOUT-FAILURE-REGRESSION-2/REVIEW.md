# Coordinator source review and exact acceptance scope

PUBLIC / NON-CANONICAL / L1. Review date: 2026-10-15.
Reviewer session: ChatGPT-20261015-day-close. A. M. Thorn.
Primary author session: Antigravity-20261015-readout-failure-regression.
This is source-exposed review and repository-runner reproduction, not another
independently authored verifier or a new scientific status.

## Verdict

Accepted at the frozen finite regression scope: S1-S5 semantic rejection,
P1-P5 positive controls, H1-H6 isolated reporting cases, and the precise
syntactic/custody tests R01/R04. No blocking defect was found in these targets.
Two overbroad prose readings are explicitly excluded below. No frozen file,
threshold, expected output or old apparatus source is changed by this review.

The five inputs at 0803c167d5e903a216b3cd96d9f7c6fcf4e62345 are byte-identical
at 07b1977422d587f1d1d4b240d840a1633f8920cf. The initial post-pin additions
were exactly EXPECTED.txt, RUN.md and RESULT.md. The actual first stdout is
3631 bytes, 22 lines, SHA-256
5bc83612d7364bd85c5b967a3187a96d0228f604f7bc994605a39670574e8f08.
Both actual architecture logs in run 38783559193 carry the exact VERIFY PASS
line with verifier SHA-256
65ec7e05b0b6c6089be5424cff33efd163967e1dced6b4c50bed6119209173fa.
Jobs 116589668927 (x86_64), 116589668503 (aarch64), aggregate 116590032904
all completed successfully. Their agreement is same-code reproduction.

## Checked behavior

Construction is separated from semantic consistency: all five contradictory
records construct, then fail at the appropriate exact ValueError branch.
Accepted zero, refusal and omitted context remain distinct. A nonzero decoded
product with unknown acceptance is a deliberate partial interface, not a
proof that every mathematical decoder would be unable to infer acceptance.
An explicit integer-valued rational record is legal; the bare tuple is not
accepted by the typed entry point. No provenance authentication is implied.

In the six supplied harness scenarios an audit or witness failure leaves
comparison NOT_RUN. A count/digest mismatch after comparison starts produces
COMPARISON_FAILED/FAIL and no adapter completion marker. The first stage and
original AssertionError text are retained. strict_exit_code is returned
report data, not a replacement for the verifier process exit code. The
verifier's own unhandled assertion produces a nonzero process exit.

The old typed verifier is still byte-identical and retains its historical
failure-message limitation. This is a tested new reporting adapter, not an
in-place fix or proof that every caller now uses it. The full 19-stage device
study and 1200-record stream were not rerun to obtain these regression results.

## Two necessary prose qualifications

1. Actual source custody is the 19 enumerated SOURCES.tsv rows: 12 files
   from the typed-readout directory and seven authority/license files.
   PREREG.md section 2's phrase "all 12 scientific and 4 result files ...
   and 7 normative repository files" overstates that inventory. The exact
   manifest, the verifier's fixed count 19, RUN.md and output agree. This
   review accepts those listed bytes only, not custody of all 16 files in
   the upstream directory. The pinned prose is preserved, not silently edited.

2. R04 is a syntactic test on the specified adapter/readout nodes. Absence
   of listed names, imports and attribute stores is not a general Python
   sandbox or a theorem about arbitrary supplied callbacks. The adapter
   invokes stage_fn, witness_fn and compare_fn; different callbacks can
   themselves have side effects or return arbitrary text. PROOF.md section
   3's "cannot alter" conclusion is accepted only for the inspected fixed
   harness and the absence of additional transition logic in this adapter,
   not as an unrestricted capability guarantee. Likewise failure handling
   here covers the specified AssertionError cases, not every possible
   Python exception or adversarial callback. No new test or broader class
   was added after the pin to hide this limit.

Neither qualification changes the five specimens, five controls, six
scenarios, frozen outputs or conditional apparatus law. Any broader claim
needs its own declared class and evidence, not a stronger summary of R04.

## Preservation

The abandoned predecessor is kept under its original ID with unchanged pin
and an explicit abandonment PR. I2 remains PARTIAL/STOP at T11; later typed
closure and this regression do not retroactively make that first run PASS.
Native actuation, physical acquisition, renewal and Canon promotion remain
outside this software regression. No other probe directory is modified.
