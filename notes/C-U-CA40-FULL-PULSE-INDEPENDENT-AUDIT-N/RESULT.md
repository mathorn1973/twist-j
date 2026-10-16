# Synthetic validation and pending campaign handoff

**PUBLIC / NON-CANONICAL. Conditional L1 analysis and auditor validation.**
Original work Apache-2.0, A. M. Thorn, 2026-10-12.

The first execution of the publicly pinned fixture suite returned
`SYNTHETIC_AUDIT_FIXTURES_PASS`: **27 positive fixtures** passed and **52
negative fixtures** exposed their named invalid inputs. Exact stdout and
environment are in [EXPECTED.txt](EXPECTED.txt) and [RUN.md](RUN.md).
The source pin is `9a5c07e140d5781934e026414aa7f7b306b15952`.

These fixtures exercise exact binary64 norm decoding, retained subnormal
squares, directed error sums, actual initial-basis bytes, checkpoint linking
and cumulative bounds, partial metadata/log semantics, strict JSON types,
inventory paths, weighted Gram accounting, thermal allocation, interval
expansion and precision/discrepancy decisions. They do not exercise a complete
production evidence tree or independently reproduce propagation, restoration
intervals, the MPFR preparation or inherited analytic bounds.

The analytical derivation and source review remain scoped as declared in
[PROOF_REVIEW.md](PROOF_REVIEW.md), [REVIEW.md](REVIEW.md) and
[CONTRACT.md](CONTRACT.md). Review was assisted within the same coordinated
session; it is not blind external review or independent empirical evidence.

**Actual campaign audit is pending.** No six numerical intervals, campaign
precision verdict or discrepancy conclusion are available from these tests.
The existing `P-U-CA40-DP5-FULL-CLOSURE-1` source
`bca348445715c03f4cdc3af6079207024dd40332` must finish under its original fixed
limit before this auditor consumes a preserved closed offline copy. Preserve
the whole attempt, including orchestration records and any failed or partial
evidence; the auditor's `--campaign` points to its copied `numerical/` directory.
An orchestration-complete receipt alone is not a scientific PASS.

After closure, record saved-account completeness separately from numerical
precision and discrepancy for all six pairs. Incomplete evidence can produce
only the prefix/partial outcomes defined in the contract. Missing evidence is
not filled by a replay or resumed attempt. Only then seal the current result
and select one preregistered bounded numerical successor from the actual
error budget. The ion experiment remains deferred. No Canon, registry,
workflow, sealed probe, release or authority status is changed here.
