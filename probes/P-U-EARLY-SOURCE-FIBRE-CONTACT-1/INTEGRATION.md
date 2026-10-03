# Public execution custody

Owner: coordinating Codex session 01a102c9-e11e-7612-8457-b582333f3dfe,
with a separate native author and independent reviewer. Public branch:
`probe/P-U-EARLY-SOURCE-FIBRE-CONTACT-1`. Baseline:
`5e872c22a18043c8126945a982efad55472cea82` (Public Canon v97).

The entire pre-run directory is committed and pushed before scientific
execution. INPUTS.sha256 binds every pre-run file except itself, including
verify.py; Git binds the wrapper and manifest. Per-directory Git attributes
preserve exact bytes, including the original reviewer freeze JSON. Staged and
committed blobs must match the manifest before execution.

The wrapper validates all listed input bytes before invoking primary.py and
independent_native.py in separate processes. Each has a 270-second timeout
within the repository's 600-second gate. It requires zero exit, empty stderr,
explicit UTF-8/LF JSON, and independent PASS. It compares the two carrier
counts, full preparation-class counts, input coverage, all three receiver
configuration counts, and all fifteen time/source-gain survivor counts. Its
single deterministic JSON stdout includes both actual reports.

REVIEW-PREREG.md and REVIEW-FREEZE.json preserve the reviewer's original
two-branch pre-exposure custody. Local native_check.py is copied byte-for-byte
as independent_native.py. The original v1 stdout serialization was corrected
and refrozen as v2 before primary-source exposure and before any execution;
v1 remains preserved locally. No independent scientific code changed after
primary exposure. REVIEW-STATIC.md supplies the separate subsequent review,
including a distinct sign-profile proof. Known targets are not blind inputs.

The first formal execution sets TWISTJ_EVIDENCE_DIR to a new local directory
and retains all primary CSVs and independent evidence from that same run.
The primary's full trajectories and bounded per-time falsifier CSVs can be
published directly. The optional independent JSONL witness stream is retained
locally and can be regenerated with the frozen program; it is not a required
Git artifact or an additional gate. Its complete full-history JSON and summary
support a direct comparison of both implementations. Scientific stdout is
identical whether evidence files are saved or the default stdout-only CI
mode is used.

After public readback, actual stdout/stderr, input hashes, timestamps and
neutral environment metadata are captured. Successful stdout becomes
EXPECTED.txt; RUN.md and RESULT.md follow as append-only records. Clean
x86_64 and aarch64 CI must match those exact bytes. Runtime SOURCE.json checks
bind the declared authority files as well as scientific definitions; future
Canon changes require an explicit replay-context decision under repository
policy, not silent removal of those checks. Neither publication nor these
checks constitutes a Canon fold or a physical contact construction.
