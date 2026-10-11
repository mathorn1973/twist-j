# Four-cell regression and performance comparison of the closure kernel

PUBLIC NON-CANONICAL. Conditional L1 engineering evidence.
Apache-2.0, A. M. Thorn, 2026-10-11.
Reservation: https://github.com/mathorn1973/twist-j/issues/1462.

This probe asks whether a narrow memory-traffic optimization preserves every
tested endpoint and partial-account bit and gives at least a twofold observed
median propagation-window speedup. It compares the sealed BALL kernel with
the optimized version on only four occupied cells of each trajectory. It
does not run the full error-closure campaign.

Both variants use the same original pulse/input bytes, prepared node model,
L8/G10 cutoffs, N512 time grid, six branch/sign cases, 120 unnormalized thermal
columns and 80 explicitly bound AVX-512 workers. The changes remove redundant
zeroing and copies, guard ownership swaps against aliasing, and compute
Horner in its supported space before zero extension. They preserve the old
conservative roundoff allowance. No descriptor cache or scheduler redesign
is part of this comparison.

The preceding P-U-CA40-BALL-CLOSURE-1 attempt was stopped for resource reasons
with zero completed numerical configurations. Its source, first outcome and
receipts remain unchanged. That exposed evidence motivated this engineering
study; no blinded replication or physical experiment is claimed.

PREREG.md freezes the decisions and custody protocol. OPTIMIZATION.md states
the conditional arithmetic-trace argument. EXACT-DESIGN.md defines the
narrower rational supporting fixtures, whose standard-library gate is:

```sh
python3 probes/P-U-CA40-CLOSURE-PERF-1/verify.py
```

That gate does not execute C++, test IEEE equivalence or measure performance.
The separate short campaign runs B,F,F,B,B,F, with a 300-second ceiling for
each child and a 1,800-second total runner ceiling. All six must pass runtime
fixtures, custody and placement checks and strict raw endpoint/component bit
comparison. Only then is the ratio of the three baseline timing median to the
three optimized timing median compared with the frozen target of 2.

Numerical execution requires the frozen Linux/AVX-512 environment and the
same GNU C++14.2, MPFR4.2.2, GMP6.3.0 and OpenMP toolchain for both builds.
Use the same compiler flags and common harness, from this probe directory:

```sh
g++ -O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math \
  -fno-tree-vectorize '-DBENCHMARK_KERNEL="baseline_kernel.cpp"' \
  '-DBENCHMARK_VARIANT="baseline"' benchmark.cpp validated_model.cpp \
  -lmpfr -lgmp -o baseline
g++ -O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math \
  -fno-tree-vectorize '-DBENCHMARK_KERNEL="kernel.cpp"' \
  '-DBENCHMARK_VARIANT="optimized"' benchmark.cpp validated_model.cpp \
  -lmpfr -lgmp -o optimized
python3 benchmark_run.py --baseline /absolute/path/baseline \
  --optimized /absolute/path/optimized --output /absolute/path/new-directory
```

The source pin and public readback precede every scientific execution or
candidate import. Compilation and static checks alone establish no result.
Record the actual compiler/dependency versions, commands and binary hashes.

Report all six timings, including preparation and end-to-end timings. The
`kernel_seconds` propagation window includes OpenMP startup, Work/BWork
allocation, barriers and progress logging. It excludes model preparation,
runtime fixtures and final endpoint/component serialization. Its median
ratio is an observation for this short workload, not a full-run forecast.

Timeouts, mismatches and incomplete output remain first outcomes. Passing
this panel proves no full-trajectory error radius, all-input channel bound,
hardware feasibility, complete-source admission or Canon claim. It does not
authorize a subsequent long run. Raw binaries and private diagnostics remain
in the retained evidence archive; the public outcome uses neutral summaries
and hashes.
