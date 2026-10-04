# Public execution custody

Owner: coordinating Codex session 01a102c9-e11e-7612-8457-b582333f3dfe,
with a separate decoder author and independent reviewer. Public branch:
`probe/P-J-LAMBDA6-DECODER-INTERFACE-1`. Baseline:
`5e872c22a18043c8126945a982efad55472cea82` (Public Canon v97).

The public preregistration pin commits this entire directory before its first
scientific execution. `INPUTS.sha256` binds every pre-run file except itself.
The wrapper is included in that manifest; the manifest and wrapper are both
bound by the immutable Git commit. `verify.py` checks those bytes, then runs
`primary.py` and `independent_decoder.py` in separate Python processes. Each
child has a 270-second timeout within the repository's 600-second gate. Both
must return zero, no stderr, and explicit UTF-8/LF JSON stdout. The wrapper
checks both PASS verdicts and the independently recorded API hash, then emits
one deterministic JSON record containing both actual reports. No expected
scientific counts or output bytes are invented before execution.

`REVIEW-PREREG.md` is an exact copy of the reviewer's work-scope freeze, which
covered both new branches. `REVIEW-FREEZE.json` records its v2 byte freeze and
maps local `decoder_check.py` to public `independent_decoder.py` without byte
changes. Its hashes for the other branch are provenance, not an imported
runtime dependency. The v1-to-v2 change fixed stdout serialization before
any primary-code exposure or scientific execution; the original local v1
files remain preserved. Final v2 control code was frozen before the reviewer
read the new primary implementation. Later static review is recorded
separately. Exposed mathematical targets are not blind predictions.

The earlier interface hash in the review freeze identifies the first shared
contract. The final interface changes only integration filenames and custody
wording; mathematical carrier, API, readers and scientific quantifiers remain
the same. `COLLISIONS.md` records the ownership release and search limitations.

After remote readback, the first local execution captures raw stdout/stderr
and timestamps outside the checkout, with the exact pin and all input hashes.
Its stdout becomes EXPECTED.txt only if the run succeeds. RUN.md and RESULT.md
are subsequent append-only public records. Clean x86_64 and aarch64 CI replays
must match those exact bytes. Code independence, proof review, and architecture
reproduction are distinct checks. Canon promotion requires a separate fold.
