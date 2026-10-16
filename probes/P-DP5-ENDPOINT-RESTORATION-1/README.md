# Independent restoration of saved seven-mode endpoints

**NON-CANONICAL / conditional L1 / source candidate, not yet executed.**
Apache-2.0, A. M. Thorn, 2026-10-13.

This probe evaluates the finite normal-ordered displacement overlaps from
the immutable full-campaign endpoint vectors with an independent integer
interval implementation. It does not run the historical propagator or
independently prepare the supplied branch alpha/Phi rectangles.

Read [PREREG.md](PREREG.md), [DERIVATION.md](DERIVATION.md) and
[SECURITY.md](SECURITY.md). The exact source/data bindings must be committed,
pushed and read back before any scientific control or production execution.

After acceptance, the repository verifier is:

    python3 -I -B probes/P-DP5-ENDPOINT-RESTORATION-1/verify.py

It exercises the exact arithmetic, operator and negative controls, then
prints one deterministic JSON record. The public architecture jobs replay
these controls against the same `EXPECTED.txt`; they do not independently
rerun the external-data production restoration.

The separately bounded, one-attempt production command is:

    timeout --signal=TERM --kill-after=5s 610s \
      python3 -I -B probes/P-DP5-ENDPOINT-RESTORATION-1/restore.py \
      --candidate FULL_ACCEPTED_COMMIT \
      --campaign ABSOLUTE_PRESERVED_CAMPAIGN \
      --output ABSOLUTE_NEW_OUTPUT_DIRECTORY

The GNU coreutils `timeout` command creates the process-group supervisor:
TERM after 610 seconds, KILL five seconds later if needed. Do not add
`--foreground`, which would prevent group supervision. The implementation
enforces the 600-second scientific deadline; the extra 15 seconds permit
only termination and neutral receipt writing. The `-I -B` flags isolate
imports and prohibit bytecode writes into the clean accepted checkout.
The output directory must be outside the input campaign and source checkout,
and must not exist. Production writes `attempt.json`, the exact first
`result.json` and a neutral `run.json` receipt. Its stdout equals the result
bytes. No old source or data is modified; no failed attempt is resumed.

Results retain new enclosure completeness, old rectangle containment or
conflict, precision, and discrepancy as separate fields. Validity of the
old branch-parameter intervals and propagated-vector error radii remains
explicit. The selected 192-bit/degree 256/600-second contract is fixed, not
a measured performance claim. Failure to finish all 720overlaps is a
preserved `NOT_CERTIFIED` outcome.
