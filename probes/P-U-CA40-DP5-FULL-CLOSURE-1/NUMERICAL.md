# Closed first numerical campaign

**PUBLIC / NON-CANONICAL. Conditional fixed-model L1 account.**
Original record Apache-2.0, A. M. Thorn, 2026-10-13.

## Execution and custody

Source pin: bca348445715c03f4cdc3af6079207024dd40332.
The complete sources and manifest were publicly read back before execution.
The source files remain unchanged; this record adds only first-outcome evidence.

```text
command: python3 probes/P-U-CA40-DP5-FULL-CLOSURE-1/full_run.py --binary /absolute/path/full --output /absolute/path/new-directory
working_directory: repository root at source pin (private absolute script path normalized)
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
compiler: GNU C++ 14.2.0
mpfr: 4.2.2
gmp: 6.3.0
workers: 80, fixed singleton CPU/place coverage
numerical_runner_started_utc: 2026-10-12T12:16:22.061647+00:00
numerical_runner_ended_utc: 2026-10-12T22:42:17.387906+00:00
runner_wall_seconds: 37555.32627261244
child_started_utc: 2026-10-12T12:16:22.159748+00:00
child_ended_utc: 2026-10-12T22:41:48.638624+00:00
child_wall_seconds: 37526.47893237881
exit_code: 0
stderr_bytes: 0
attempted_launches: 1
launched_children: 1
retry_or_resume_performed: false
ceiling_seconds: 86400
outcome: COMPLETE_PRECISION_GOAL_MET
```

Compilation used -O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math
-fno-tree-vectorize and the frozen target functions. Build exit 0, with empty
stdout/stderr. The original binary is 376464 bytes, SHA-256
cb758140dc2387221c59bd8e5cc4bd9c8b0e0234c9f6bc36bf425e03b11849db.
The wrapper stdout is 83 bytes, SHA-256
dd6297b83a9d09dda3bec40a7e0f3ff7384992b9b17a1d9ff59edffc2eb4a4e2.
The full scientific stdout/final result is 312313 bytes, SHA-256
49940669a1954abaa52a230d1e40d76bc9bc7cef0b6eb395b1c57f10176f3e31.
All recorded stderr streams are empty.

The final closed summary is 17670 bytes, SHA-256
ac9348f39112dfb00de47988f79f483b492600f4bfbbc4d8871babec4ded1def.
The complete state inventory is 2424474 bytes, SHA-256
b540e5135c5d0b81f7c4e7b5ee8bf0a0ac9f08bf6812b1931b113666a40700c8.
It covers 14588 state artifacts. There are 90 complete tasks, 7290 committed
snapshots, 5280 byte-identical inactive carries and no uncommitted state files.
The original first outputs and receipts remain preserved outside this
repository; raw logs, binaries and payloads are not imported here.

## Fixed domain and six exact pair decisions

Cases 0, 1, 2 carry labels (4,3), (4,4), (1,1) at +4*pi/5.
Cases 3, 4, 5 repeat these labels at -4*pi/5.
The program ends at 500 us after 80 segments. K3 means all 120 initial thermal
columns of total occupation at most 3, without renormalization; it is distinct
from the dynamic L8 and guard G10 cutoffs.

Each row below uses exact rational numbers reconstructed from stored
binary64 values. Thermal radius is an upward enclosure of half the omitted
thermal mass 680046581/794280046581. Total radius includes the arithmetic
halfwidth. The final interval already includes the interval-valued center,
so the arithmetic halfwidth is not added a second time to its endpoints.

| Cases | Numerical radius | Thermal radius | Arithmetic radius | Total radius | Distance interval | Discrepancy |
|---|---|---|---|---|---|---|
| 0,1 | 7584607333403175/18446744073709551616 | 1974216350377137/4611686018427387904 | 13773/72057594037927936 | 3870368184609403/4611686018427387904 | [6180320861745755/144115188075855872, 6422218873283843/144115188075855872] | EXCEEDS_TARGET |
| 0,2 | 948075916675333/2305843009213693952 | 1974216350377137/4611686018427387904 | 13747/72057594037927936 | 3870368184607611/4611686018427387904 | [3115375241708271/72057594037927936, 3236324247477259/72057594037927936] | EXCEEDS_TARGET |
| 1,2 | 1183696747253451/2305843009213693952 | 1974216350377137/4611686018427387904 | 97399/576460752303423488 | 4341609845663231/4611686018427387904 | [0, 7183517048513581/4611686018427387904] | UNRESOLVED |
| 3,4 | 1087604666264357/9223372036854775808 | 1974216350377137/4611686018427387904 | 110357/576460752303423488 | 5036037368784343/9223372036854775808 | [1745543596785147/72057594037927936, 7296926722689611/288230376151711744] | EXCEEDS_TARGET |
| 3,5 | 4350418665056665/36893488147419103232 | 1974216350377137/4611686018427387904 | 110359/576460752303423488 | 5036037368784185/9223372036854775808 | [109830130467365/4503599627370496, 7343880685460373/288230376151711744] | EXCEEDS_TARGET |
| 4,5 | 5187105761169209/36893488147419103232 | 1974216350377137/4611686018427387904 | 6573757/36893488147419103232 | 5245209142690017/9223372036854775808 | [0, 1132347373966847/1152921504606846976] | WITHIN_TARGET |

All six total radii pass the strict frozen precision contract <=1/1000.
Four discrepancy intervals are strictly above 1/1000, one is unresolved and
one is within. One above-threshold witness per sign suffices for the stated
selected nonlinear-discrepancy conclusion; no all-input channel conclusion
is inferred.

For the unresolved pair (1,2), the saved center upper endpoint plus the
thermal radius is exactly 9632247108013357/9223372036854775808, about
0.001044330324. Thus these unchanged K3 retained-center/tail intervals
would still not certify WITHIN_TARGET with a zero numerical radius.
This direct rational consequence concerns the enclosure, not the true
discrepancy; it is not an additional auditor check or solver execution.

## Independent saved-output audit and remaining dependencies

Audit A source pin 9a5c07e140d5781934e026414aa7f7b306b15952 was public
before campaign outputs were consumed. A closed independent copy of the
evidence, frozen source and original binary was preserved on 2026-10-13.
One unchanged auditor invocation passed on Linux/x86_64, CPython 3.13.5,
in 56.25480427965522 s, exit 0 and empty stderr. Its 9897-byte stdout SHA-256 is
5f71cf4a6ee8e75aac46dc7382fb05dc2aa2da02eb8d75e702e8f275c654b333.
The report is in draftPR1480 and does not enlarge the exact verifier's scope.

A rehashed all 14588 state artifacts and verified the basis, all checkpoint
records, cumulative components, progress/lifecycle consistency, source/binary
copy custody, 720 exact terminal norms and the rational final-pair account.
The optional all-snapshot norm mode was not requested. Neither the solver,
per-cell quintics/nodes, MPFR preparation nor relative-frame restoration was
independently rerun. Recorded receipts do not independently attest the
original execution environment. The stated local-enclosure and restoration
premises remain dependencies; no physical ion experiment was performed.

The saved-account result justifies an independently specified successor
question. It does not authorize altering or resuming this closed source pin.
New pulse/control choices, different domains and physical interpretations
require their own explicit contracts and evidence.
