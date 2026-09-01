# P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2 immutable pin

Status: PRE-EXECUTION / ZERO EVIDENTIAL WEIGHT

The commit that first adds this final file to branch
`probe/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2` is the immutable pilot pin.
Its full commit SHA, parent SHA and public readback receipts must be recorded
in `RUN.md` after execution.

The pin consumes the identifier reserved by issue #755. It does not resume or
repair the first pilot merged by PR #746. No `L=6` or `L=8` decision output
was opened before this file.

After the pin, every pre-execution file named by `SHA256SUMS` is immutable.
The manifest itself is likewise fixed by the public pin commit and public
byte-for-byte readback. The accepted inventory contains exactly fourteen
entries in the order enforced independently by `run_pilot.py` and `verify.py`.
After readback the only local orchestration command is `python3 run_pilot.py`;
it refuses any pre-existing decision artifact and invokes the canonical
repository-root verifier command exactly once.

Allowed later additions are only:

```text
the eight frozen raw chain logs
PILOT_RUNS.tsv
PILOT_ANALYSIS.txt
EXPECTED.txt
RUN.md
RESULT.md
```

Changing source, fixture, seeds, schedules, metrics, thresholds, terminal
precedence or scope spends this identifier without a reusable result. The
record must then follow the repository's abandoned-pin rule; it may not be
silently repaired or rerun.
