# Bounded receiver record reproduction

NON-CANONICAL / candidate-T by conditional proof / L1. Public authority is v95.
This entry audits the new five-layer receiver phase-cycle construction in
[the proof](../../notes/C-FIELD-RECEIVER-BOUNDED-RECORD-N/PROOF.md).
[PREREG.md](../../notes/C-FIELD-RECEIVER-BOUNDED-RECORD-N/PREREG.md) freezes
scope, known analytical predictions, resources, provenance and failure rules.

Run from a clean public source-pin checkout with assertions enabled:

```text
python3 tools/check_reproduce.py --base 04fa72ca2506398bf47a64fe33aa024625bd4f9b
```

The bridge verifies its source map, then loads the two accepted full-state
adapters. They reuse exact public #1310 local arithmetic without invoking
old main routines. Only Python's standard library is used. The repository
runner requires exit 0, empty stderr and byte identity with EXPECTED.txt,
with its existing 120-second limit. CI uses the same head on x86_64 and
aarch64. No workflow change is made.

EXPECTED.txt is a prospective analytical prediction, prepared without
running this new suite. Its presence alone is not an execution receipt.
Actual post-pin evidence belongs in the candidate's RUN.md and RESULT.md.
Finite audits support the proof; they do not establish the all-N or all-time
cut statements by extrapolation. No permanent or robust memory is claimed.
