# Local repository validation

2026-10-04. These checks supplement the first formal Linux execution in
RUN.md. They do not change its pin or replace its raw output.

- Repository policy, Canon v97, ledger and explicit gate-contract checks: PASS.
- Linux infrastructure unit suite: 172 tests, PASS.
- Linux `tools/check_verifier.py --base 2973a432303e046aacb2cee3cea97254ea3ab8eb`:
  PASS, pinned primary SHA-256
  `6974d58afcd62b1aef64e55c5195622bb7affcc4fa57ddeeb91e6fee743156b9` and stdout
  `166826f72f5e61bc70dee1b447d55fa46b0c4a34a290d43bfb9c3f38cddd2754`.

Two local environment limitations were observed and retained explicitly.
The Windows sandbox denied creation/access of temporary fixture directories
in the infrastructure tests; the unmodified suite passed in Linux. A native
Windows verifier replay emitted CRLF stdout instead of the preregistered
Linux LF stdout. Its received digest
`33d957514a145a4ad6b498a7bdf5ce2b5e9daf47052b77ce57c7588aaa6bc6bb` equals
exactly the hash of EXPECTED.txt with LF replaced by CRLF. Replaying under
the prescribed Linux platform passed byte for byte. No accepted source,
scientific threshold or EXPECTED bytes were changed to accommodate either
environment issue. Native Windows byte-identical stdout is not claimed.

The PR workflow independently checks x86_64 and aarch64 Linux. Their actual
status belongs to the PR check records; this local document does not predict
or predeclare CI success.
