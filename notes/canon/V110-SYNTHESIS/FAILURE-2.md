# Preserved second v110 integration attempt

NON-CANONICAL. This disposition records a release-tooling regression-test
failure. It does not report a mathematical counterexample.

The corrected content candidate
`5a8242ee2d3cb624c92648d1dab756cd961931b8` and its three-file release form
`0d974a00bbae5f1c4ba9042c63c0fff4f12e6b84` remain unchanged on branch
`codex/canon-v110-2`, with public PR1964 as the review record. All 21 content
files were publicly read back before direct scientific execution.

On Linux x86_64, Python 3.12.3, the direct status-separation run began at
`2026-11-08T17:31:34.247537+00:00`: exit 0, empty stderr, 35902 stdout
bytes, SHA-256
`50478798472d2c147af4c820e121f6c1046a1880c3e4fb50e67432dbe8d84630`,
exactly EXPECTED.txt and 224/224 PASS. The S3 wrapper began at
`2026-11-08T17:31:37.541618+00:00`: exit 0, empty stderr, 256 stdout
bytes, SHA-256
`f0441b7af0985fa211f9ef65f8e3b7c590fa6892fe57994963bd7e4467ea4563`,
exactly EXPECTED.txt. Neither timed out. The checkout remained unchanged.

[CI run 42505526735](https://github.com/mathorn1973/twist-j/actions/runs/42505526735)
failed on both architectures during the tooling unit suite: 219 tests,
two failures in tools/test_architecture_map_report.py. Jobs 128807195956
(aarch64) and 128807196214 (x86_64) have the same failure reasons:

- test_current_counts_match_the_public_summary still expected 609 claims;
  the admitted v110 registry contains 612. Its status and inline-evidence
  expectations also require the corresponding exact changes 465->468 T
  and 188->191 evidence-none rows.
- test_v108_contact_scope_and_finite_apparatus_closure still expected the
  pre-S3 set of RELATIVE-CONTACT claims. The actual set additionally contains
  the three declared new theorems, whose exact premise and boundary edges
  must be included in the regression test.

The local release-form sequence independently encountered the same two
unit failures after policy passed and stopped there. Its full activation
step did not execute. CI skipped the scientific replay steps, so this run
is not a two-architecture reproduction of the new fold. Captures are
preserved outside the repository; the public CI run remains a failure.

The successor on codex/canon-v110-3 preserves the same main base and complete
Canon, scientific programs, 224 structural criteria and expected bytes.
It updates the engineering test's exact expected registry and dependency
metadata, retaining its existing assertions and adding explicit boundary
checks. No gate, scientific tolerance, execution budget or verifier behavior
is relaxed. The structural audit binds that test and this disposition.
Metadata-tooling unit tests may run during preparation; the new scientific
candidate is still frozen and publicly read back before its first audit
execution. Earlier content and release-form commits are not rewritten.
