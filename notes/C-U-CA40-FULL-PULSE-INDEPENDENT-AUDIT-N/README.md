# Independent review of the fixed full-pulse numerical account

**PUBLIC / NON-CANONICAL. Conditional L1 analysis and offline audit design.**
Original work Apache-2.0, A. M. Thorn, 2026-10-12.
Reservation: [#1473](https://github.com/mathorn1973/twist-j/issues/1473).
Authority base: `5f54015ed8361e3a64cb10894397020ddfadd104`, Public Canon v101.

This lane reviews the existing full-pulse source pin
`bca348445715c03f4cdc3af6079207024dd40332` of
`P-U-CA40-DP5-FULL-CLOSURE-1`. It does not change that pin, inspect the live
campaign, contact a numerical machine, run a solver, extend its deadline or
restart an attempt. The ion experiment is outside the present work.

[PROOF_REVIEW.md](PROOF_REVIEW.md) derives the cumulative unitary-defect and
weighted pair accounts independently from their mathematical definitions,
then compares them with named lines of the pinned implementation. The reviewed
full-word composition and aggregation are consistent at this stated scope.
The inherited norm-ball operator estimates, analytic infinite tail,
between-node remainder and MPFR model preparation remain dependencies; this
note does not assert an independent proof of all those implementations.

[audit_saved.py](audit_saved.py) is a separate standard-library auditor for a
**closed offline copy** of the eventual evidence. It imports no candidate
module and has no network, subprocess or solver interface. It checks saved
bytes and exact rational aggregation. In particular, it recomputes exact
binary64 endpoint squared norms rather than accepting their reported norm
enclosures on trust. It distinguishes a complete saved-account audit from a
valid committed-prefix audit after an incomplete attempt. Neither outcome is
an independently rerun propagation or a physical channel certificate.

The complete CLI requires an immutable offline campaign directory containing
`summary.json`, `artifact-inventory.json`, `final-custody.json`, `full.stdout`,
`full.stderr`, and `full-state/`. Run only after this audit's own sources have
been publicly pinned and read back, and the first campaign has ended:

```sh
python3 -B notes/C-U-CA40-FULL-PULSE-INDEPENDENT-AUDIT-N/audit_saved.py \
  --campaign /absolute/path/to/closed-offline-campaign
```

The default hashes every state artifact and checks the exact norm of each
final endpoint. `--all-snapshot-norms` additionally recomputes exact norms of
all committed snapshots, at a potentially substantial offline CPU cost.
The auditor only writes its JSON report to stdout. It never modifies inputs.
An incomplete campaign may be examined with `--allow-incomplete`; its report
cannot earn a complete-account result. Source/binary receipts are checked as
recorded declarations, not independently authenticated execution provenance.

[CONTRACT.md](CONTRACT.md) freezes accepted inputs, checks, failure semantics,
scope limits and the pre-execution gate. [ERROR_BUDGET.md](ERROR_BUDGET.md)
records the exact error budget and post-run decision tree.
[REPORT_TEMPLATE.md](REPORT_TEMPLATE.md) is an unfilled reporting template.
It contains no predicted numerical result. [verify.py](verify.py) supplies
small synthetic positive and negative fixtures for the auditor; it does not
read campaign data or execute candidate scientific code.

No scientific execution or successful synthetic test is asserted by the
source-design text. Actual validation belongs in a later, separately recorded
result after the immutable audit pin. No Canon, registry, frontier, workflow,
sealed probe or action-layer status is changed.
