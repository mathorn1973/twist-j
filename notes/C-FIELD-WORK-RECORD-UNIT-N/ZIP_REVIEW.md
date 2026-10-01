# Review of the original prototype supplied after the source pin

NON-CANONICAL / source-custody and static review only. No original replay.
This record adds no scientific input to the frozen new audit. The original
archive arrived after source pin d01ff9a4bd0ba6cef62b7fc932a0e8ce8a0c054a
and its first clean local execution. Statements in the frozen proof/protocol,
README and expected output about an unavailable or unverified original ZIP
describe that earlier stage. They are preserved rather than rewritten.

## Archive identity and actual checks

Supplied name: TWISTJ_mistni_zaznam_v95_balicek.zip.
Size: 61685 bytes. SHA-256:
`e25ba83d7728b784553227dbd768d417f328ab5e9056f94d82dff2fcbf2e95b2`.

Two delegated read-only passes examined the archive directly, without
extracting, importing or executing its scientific modules. They found:

- All 19 entries have valid CRCs and safe, unique relative paths.
- All 18 SHA256SUMS entries match archive bytes; the manifest excludes itself.
- All 9 FREEZE.json source entries match. FREEZE itself hashes to
  `ab9bb52679249848e6019622b2693144a0056024ce0d7e91b16ce774e7f06e2a`.
- Archived stdout equals EXPECTED.txt exactly:120 bytes, SHA-256
  `4cc87bd647d73f3a85386b4aa818040ff3b114defc31ddf231ca5b021b7234b7`.
  Archived stderr is empty.
- RESULTS.json has 24589 bytes, SHA-256
  `7cad0376b428623b7f20c3767121dcdd2e1ef427c560e085bc6d621a2c931c1d`,
  matching RUN.md. Its source hashes agree with FREEZE.
- Both vendored arithmetic sources, BASE_PROOF and LICENSE are identical
  to the declared #1310 Git objects; LENGTH_PROOF is identical to #1312.
  All declared Git blob SHA-1 values match. The later-added LENGTH_PROOF
  is correctly declared outside the original runtime freeze.
- The included Czech report is identical to the previously supplied file:
  18072 bytes, SHA-256
  `204903969bb93db3b6b6d7962287f5fec70d33176904f8550162f37460b0b626`.

The scientific receipt
`2c4744073f2d9b560b976e8731942898e47c82e59e28b0aa63e6d3a5d4256bda`
is consistently reported in the stored records. It was not recomputed by
executing the original verifier in this review.

## Static implementation and coverage review

No functional discrepancy was found in accepted-event recognition, the
recovered-input inverse, the four-layer order, full coordinate retention,
energy/charge accounts or projection to the old law. The reported 145800
local cases, 69 trajectories / 952 boundaries and 1280 generic states agree with
the frozen source loops and with the stored output/RESULTS. This is manual
count and source review, not an independent execution of those cases.
The stored example tables agree on arrival 2, reaction 3, old reset 4 and
HIT at 3..10 for the positive three-cell preparation.

RUN.md accurately qualifies its inverse coverage: every primitive's full
coordinates and invariants are compared; explicit inverse round trips cover
the local target gate and whole macrosteps. It does not additionally claim
separate round trips for each F/A/B primitive.

One implementation-order limitation matters for future replay: the original
verify.py imports its adapters and vendored modules before assert_freeze()
checks their hashes. Its internal check is therefore not a pre-import
execution guard. Verify archive/source bytes externally before running it.
This does not invalidate the inspected archive's mathematics or matching
hashes. The newly public reproduction bridge checks all its named sources
before importing its new modules and does not invoke this original verifier.

## What these checks do not establish

The freeze time 2026-10-01T10:13:27.624516+00:00 is a consistent declared
local timestamp, not independent proof of order. RESULTS has no run-start
or run-end timestamp; ZIP timestamps are normalized. Present hash agreement
does not independently prove that freezing preceded the first execution,
that no earlier failed execution occurred, or that no source was ever
repaired. Those historical assertions remain the author's report.

The original claimed execution is one local x86_64 audit, explicitly without
public preregistration. Its custody is not retroactively upgraded by this
review or by the separately written candidate's public CI. The archive
remains a supplied original artifact; no raw archive or transcript is copied
into the repository. Public audit evidence for the common mathematical law
is the new immutable source and actual runs documented in RUN.md.
