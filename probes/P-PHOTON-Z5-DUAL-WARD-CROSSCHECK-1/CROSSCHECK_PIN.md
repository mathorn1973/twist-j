# P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1 immutable pin

Status: PRE-EXECUTION / ZERO EVIDENTIAL WEIGHT

The first commit that adds this final file together with the complete
`SOURCE_SHA256SUMS` and `INPUT_SHA256SUMS` to branch
`probe/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1` is the immutable execution pin.
Its full commit SHA, parent and public readback receipt are recorded only
after the one-shot execution.

This fresh identifier was reserved in issue #756 at public comment
`issuecomment-5494663082`.  It does not reopen or modify the sealed source
probe `P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1`.

No `L=6,8` primal replay statistic or dual decision transition was opened
before this file.  Only `L<=4` development fixtures were permitted.

After public pin/readback, every pre-execution byte is immutable.  The sole
formal command is `python3 run_crosscheck.py` from this directory.  It may be
issued once and refuses pre-existing decision artifacts.

Allowed post-pin additions are exactly the four registered primal replay
logs, eight registered dual logs, `PRIMAL_RUNS.tsv`, `DUAL_RUNS.tsv`,
`OUTPUT_SHA256SUMS`, `ANALYSIS.txt`, `EXPECTED.txt`, `RUN.md` and `RESULT.md`.
No source, dependency, seed, schedule, statistic, threshold or terminal may
change after this pin.
