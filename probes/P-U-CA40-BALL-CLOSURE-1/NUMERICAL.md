# Incomplete first numerical campaign

PUBLIC NON-CANONICAL. Status C, conditional L1 computational evidence.
Original record Apache-2.0, A. M. Thorn, 2026-10-11.

The first attempt was manually stopped for resource reasons under the
explicit allowance in PREREG.md. No configuration completed. The outcome
is **NOT_CERTIFIED** for both angles; there are no final coherence intervals
or total pair radii. Partial accumulated node bounds are not final error
bounds. The four-hour limit did not expire, and no source, input, pulse,
cutoff or threshold was changed after the pin.

## Source and actual execution

Source pin: `ab33a3f42af66b9bfa52915871b10ce3d914c124`.
All twelve source files passed public byte readback at
2026-10-11T12:26:48.338457+00:00, before first execution.
SOURCE_SHA256SUMS binds all eleven scientific files. The input retains
10093 bytes and SHA256
`ca6b286c9e6d45795677b05e09fbe1b38043c8ff8369b57b652c83195a156d53`.

Platform: Debian GNU/Linux 13 (trixie), x86_64, Python 3.13.5, NumPy 2.5.0,
GNU C++ 14.2.0, MPFR 4.2.2-1 and GMP 2:6.3.0+dfsg-3. Compile flags were
`-O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math -fno-tree-vectorize`;
the kernel uses explicit AVX-512F/DQ/VL target attributes. The compiler
used privately extracted development headers and system MPFR/GMP libraries.
Both compilation streams were empty, exit zero, wall 13.386380571871996 s.
Executable: 330368 bytes, SHA256
`8a98f9f530712d00751ff592d20d0c6dd86bc798fe7aa6219c29b1ad2c593c32`.

The first exact supporting gate passed in 0.36547125689685345 s with its
actual 1884-byte stdout, preserved in EXPECTED.txt and RUN.md. It does not
certify a trajectory. The numerical runner then started at
2026-10-11T12:27:40.055468+00:00 with the frozen 14400-second total budget.
It launched L8/G10/N512, with dimensions 6435/19448, all 120 thermal
columns and the prescribed six branches. Later configurations were not
launched.

OMP_NUM_THREADS=80, OMP_DYNAMIC=FALSE, OMP_PROC_BIND=TRUE and eighty
explicit singleton OMP_PLACES were supplied. A read-only process sample
at 12:37:13.994284 UTC found all 80 workers individually bound to CPUs
0 through 79. Over its five-second observation, CPU use was
79.95007528433067 CPU-seconds per wall second. This observation is not a
final worker-map record or a new 40/80-thread or AVX2/AVX512 comparison.

## Reached phases and resource decision

The lifecycle record reached model_preparation_completed at
44.431419199332595 s and fixtures_completed at 44.457236886024475 s.
This confirms that the frozen runtime checks returned without throwing,
including directed arithmetic, gradual underflow, displacement and small
ball-versus-interval fixtures. Their final numerical values, the full
worker map and the legacy-eta mismatch diagnostic were never emitted.
There is no claim of an independently replayed trajectory certificate.

Before any debugger attachment, repeated progress records yielded these
empirical within-task rates:

| Case class | Cells per task | Observed tasks | Median seconds per cell |
|---|---:|---:|---:|
| Cases 0, 3: one active ion | 16384 | 30 | 3.771273 |
| Cases 1, 2, 4, 5: two active ions | 8192 | 50 | 6.545197 |

Each observed task had at least two measured intervals. Rates are medians
of successive records from the same task, so late start time is not
mistaken for per-cell work. The 90 tasks are scheduled on 80 workers;
ten tasks had not yet started. At the observed rates, a scan-only list
scheduling extrapolation gave about 106298 s remaining, with about
13675 s remaining in the budget. This is an empirical resource estimate,
not a guaranteed duration, statistical interval, or numerical error bound.
It assumes no acceleration of the final smaller worker group and excludes
final restoration and output validation. Even the observed one-active-ion
trajectory rate alone projects to about seventeen hours from its start.

A subsequent single read-only debugger stack sample briefly paused and
detached the target within a 1.4444374199956656-second command. It wrote
no target variables and invoked no target functions. Its 80 top frames
included 28 ball mode actions, 10 candidate mode actions, nine Horner
evaluations and 22 unresolved libc frames. Some libc callers were vector
copies or mode-action buffer initialization. This snapshot is a diagnostic
lead, not a statistical profile or proof of DRAM saturation. The timing
extrapolation above was retained before this perturbation.

At 2026-10-11T12:41:00.328389+00:00 the coordinator explicitly requested
SIGTERM of its numerical runner. The runner terminated its owned child
process group and preserved an INTERRUPTED_OR_FAILED receipt with child
exit -15 and post-child source/input/binary custody PASS. Runner result:

```text
status: NOT_CERTIFIED
failure: Interrupted by signal 15
completed: 0
wall_seconds: 800.5929317045957
ended_utc: 2026-10-11T12:41:00.648379+00:00
```

The outer runner receipt has exit 2, empty stderr and wall
800.7282891403884 s. Its coordinator's `execution-complete` record means
the orchestration finished and explicitly records numerical_exit_code=2;
it is not numerical success. All owned processes were subsequently absent.
This is a manual resource stop, not budget expiry or a precision decision.

## Preserved evidence and missing account

The final progress file contains 330 complete lines from 80 tasks and no
completed-task marker. Cases 0 and 3 reached 192 reported cells in each
of fifteen batches. Cases 1, 2 and 4 reached 96 in each of fifteen batches;
case 5 reached 96 in five batches. The remaining ten batches were not
observed. No final endpoint file, per-column final account, restored
coherence interval or pair radius was produced.

Private compact evidence archive: 51439 bytes, SHA256
`823709f3ee40c705de2cfe73357d07cd59e3895e2b44a0bdd53ef9b861729c2f`.
It contains 37 retained records plus a manifest, including original stdout,
stderr, launch/exit/custody receipts, the explicit resource-stop record,
timing observations, stack sample and partial numerical files. Every
included file was independently checked against the manifest after local
transfer. There are zero binary endpoint artifacts.

| Partial artifact | Bytes | SHA256 |
|---|---:|---|
| basis.json | 103019 | `2d3f5895bf0df360da3a5c42ebcf91beba63ae8e67f8015e3f5cb59c9fa498c9` |
| lifecycle.jsonl | 203 | `f7e2a6f0e431eb18b31d966917ebcae5d3c94d863f9e12746d6ebdcc4e7b8598` |
| progress.jsonl | 42897 | `d7b5ba43d4b6da4f94a1d85b37d7bd7a99b8a7759b450ea40549d1c7942649cc` |

The saved-aggregation audit correctly reports zero completed records; it
cannot audit missing final radii. Full intermediate polynomials were not
retained. Public sources and this neutral summary do not substitute for
missing numerical outputs or independent node-by-node replication.

| Requested account | Positive angle | Negative angle |
|---|---|---|
| Completed full-space numerical bound | Missing | Missing |
| Final thermal/numerical/arithmetic pair radius | Missing | Missing |
| All three pair total radii at most 1/1000 | Not decided | Not decided |
| Certified nonlinear discrepancy witness | Not decided | Not decided |

The exact initial thermal omission remains 680046581/794280046581, with
pair contribution half that mass. That known component alone does not
close the missing numerical account. The exact-darkness premise and the
complete informative-contact source obstruction remain unchanged.
