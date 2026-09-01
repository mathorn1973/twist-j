# P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2

**Status:** formal zero-evidence engineering pilot
**Public reservation:** issue #755
**Exact-kernel dependency:** PR #760 / merge `5c2d469880828f29023e3cf592e86abbe352cd59`

This package tests whether the fixed `t=1` finite-volume `Z5` chain mixes
well enough to freeze a later production experiment. It cannot report a
photon phase. Its only terminals are:

```text
BREAK_KERNEL
STOP_INTEGRITY
STOP_MIXING
PILOT_READY_FOR_PRODUCTION_PREREG
```

All commands are Linux commands executed from this directory with the locale
and runtime environment below:

Build dependency: a C++20 `g++` and Boost.Multiprecision headers on the
compiler's standard include path. The accepted local pre-pin audit used Ubuntu
22.04 `libboost-dev 1.74.0.3ubuntu7`; Boost is header-only for this program.

```sh
export LC_ALL=C
export LANG=C
export TZ=UTC
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
```

Before the public pin, only compilation and the two small-lattice fixtures are
permitted:

```sh
set -euo pipefail
g++ -std=c++20 -O3 -DNDEBUG -Wall -Wextra -Wpedantic photon_z5.cpp -o /tmp/photon_z5_pilot_2
/tmp/photon_z5_pilot_2 --self-test | cmp - SELFTEST_EXPECTED.txt
cmp <(printf '%s\n' 'KERNEL_STATUS STOP_INTEGRITY' 'INTEGRITY_REASON value=STOP_INTEGRITY_modeled_cap_fixture' 'EVIDENTIAL_STATUS ZERO_PILOT_ONLY') <(/tmp/photon_z5_pilot_2 --stop-integrity-fixture)
/tmp/photon_z5_pilot_2 --fixture | cmp - REFERENCE_EXPECTED.txt
python3 reference_check.py --cpp /tmp/photon_z5_pilot_2 | cmp - REFERENCE_EXPECTED.txt
```

`run_pilot.py`, `analyze_pilot.py` on decision logs and `verify.py` are
forbidden before the final pin commit is pushed and every pinned byte is read
back from the public branch. After that readback, the sole local formal command
is:

```sh
set -euo pipefail
python3 run_pilot.py
```

The driver first requires the exact pre-run directory inventory of the fourteen
files named by `SHA256SUMS` plus `SHA256SUMS` itself. It then validates every
hash, rebuilds the accepted source in a temporary directory, reproduces both
frozen fixtures, and uses a four-worker pool (at most four chains concurrently).
Any decision artifact,
foreign log, cache directory, missing pin file or other extra entry refuses the
start. A clean run writes, in this exact order:

```text
L6_cold_r1.log
L6_cold_r2.log
L6_hot_r1.log
L6_hot_r2.log
L8_cold_r1.log
L8_cold_r2.log
L8_hot_r1.log
L8_hot_r2.log
PILOT_RUNS.tsv
PILOT_ANALYSIS.txt
EXPECTED.txt
```

The manifest header is exactly:

```text
filename<TAB>L<TAB>start<TAB>replica<TAB>seed<TAB>thermal_cycles<TAB>measurements<TAB>between_cycles<TAB>bytes<TAB>sha256<TAB>exit_code<TAB>stderr_bytes
```

As its final step, the driver changes the verifier child process to the
repository root and invokes the accepted no-argument gate with the canonical
command `python3 probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/verify.py`
exactly once. Exit zero, empty stderr and ASCII/LF stdout are mandatory; that
captured stdout is written byte for byte as `EXPECTED.txt`. A complete modeled
verifier custody failure is captured normally as `STOP_INTEGRITY`. A driver or
child-process crash, nonzero exit, nonempty stderr, contaminated pre-run
inventory, or any other failure that prevents one complete modeled verifier
terminal closes the pin without a rerun under the abandoned-pin rule.

Pull-request architecture jobs later run the unchanged command below in clean
Linux checkouts and compare its stdout byte for byte with `EXPECTED.txt`:

```sh
cd ../..
python3 probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/verify.py
```
