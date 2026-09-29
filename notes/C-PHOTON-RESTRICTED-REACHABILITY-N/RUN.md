# Single pinned execution

PUBLIC / NON-CANONICAL. Item C-PHOTON-RESTRICTED-REACHABILITY-N; issue #1267.

Source pin: `33cd67b43bdcb1a6508f87ab54b26caaaa84a688`. Execution HEAD equals this pin.
Parent main: `e8143f5af0df1c1ff7ebb2d3b8ea2f6584d4bed3`.
Source tree: `b6f64844a0050033103c0786aee56de92f51d17a`.
The author explicitly authorized the connected account's default contributor
identity for this PR. The public source tree is byte-identical to the prepared
source tree; the identity exception changed no scientific file.

The branch and commit were publicly read back and fetched, and the nine
source hashes matched. The hash comment
[5871077290](https://github.com/mathorn1973/twist-j/issues/1267#issuecomment-5871077290)
was published at 2026-09-28T13:41:59Z and read back before execution.
The runner independently required a clean worktree, an absent ENGINEERING
directory, pin ancestry and exact equality of all nine frozen source files.

```text
python3 notes/C-PHOTON-RESTRICTED-REACHABILITY-N/run_once.py --pin 33cd67b43bdcb1a6508f87ab54b26caaaa84a688
```

Start: `2026-09-28T13:42:08Z`. Finish: `2026-09-28T13:42:10Z`.
Platform: Linux. Architecture: x86_64. Python: 3.12.14.
Environment: PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1,
LC_ALL=C.UTF-8, TZ=UTC. Runner exit: 0. Status: COMPLETE.

| Task | Limit (s) | Elapsed (s) | Exit | Stdout bytes | Stderr bytes |
|---|---:|---:|---:|---:|---:|
| audit | 45 | 1.589636 | 0 | 1070 | 0 |
| localization | 120 | 0.450640 | 0 | 71 | 0 |

Both tasks were executed once, sequentially, with no timeout, repair, rerun,
new sample or seed. The runner stdout was exactly:

```text
audit: PASS
localization: PASS
```

Subprocess commands, source hashes, output byte counts and neutral environment
are preserved in ENGINEERING/execution.json. Audit stdout SHA-256:
`86d1b927b6b10f65454f545f2b1712e1cd94d548e53c5c494ff2eb871327e6c8`.
Localization stdout SHA-256:
`6cb5adcb0af2d8bedc24b8cbf5220967bcf5006a19106044b58ae34d7e357b86`.
Both stderr files are empty, SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
SHA256SUMS_RESULTS covers all ten ENGINEERING files, including the inner
localization manifest. Its four derived data files have their own SHA256SUMS.

This is one local architecture. The exact finite audit is at most candidate-C;
repository CI does not replay these notes programs. The written all-L proof
is a separate candidate-T argument. Localization is retrospective engineering
arithmetic with ZERO scientific evidential weight. Canon v92 and the parent
INCONCLUSIVE_EQUILIBRATION disposition retain their scope and status.
