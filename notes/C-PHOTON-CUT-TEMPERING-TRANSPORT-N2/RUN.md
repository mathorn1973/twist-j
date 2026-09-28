# First frozen N2 invocation

**PUBLIC / NON-CANONICAL. Engineering disposition: TRANSPORT_QUALIFIED.**

Pin: `87a25a4d3367697ebb1d574fcf39d00098842c84`. The six files were
committed, pushed and publicly read back before invocation; #1263 records
that readback and hashes. The checkout was clean at this exact pin.
The predecessor failure remains merged in PR #1262; it was not resumed.

Platform: Linux aarch64, Python 3.12.3. Compiler of the reused unchanged
sampler: `g++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0`, flags
`-std=c++17 -O3 -Wall -Wextra -pedantic`, no fast-math.
Binary SHA-256, verified before invocation:
`538cd406bb2ed8c5d22d70cad719d0dc6b9684e80b76318967ddafb8ee025c35`.
This is the preregistered reuse of identical compiled source, not a reused
trajectory. The N2 sampler audit was actually invoked anew.

Controller command: `python3 run_pilot.py BINARY OUT`, from the N2 package,
with a new output directory. UTC start 2026-09-28T07:23:04.876205+00:00;
finish 2026-09-28T07:24:55.950428+00:00. The launch interface reached its
10-second return limit while the detached controller continued. Read-only
inspection confirmed the original running invocation; no second controller
or replacement job was launched. The separate shell return record reports
controller exit 0; its stderr was empty.

| Program | Invocations | Exit | stderr bytes | Other record |
|---|---:|---:|---:|---|
| sampler audit | 1 | 0 | 0 | 0.031 s, stdout 59 bytes |
| analyzer fixture suite | 1 | 0 | 0 | 2.740 s, stdout 49 bytes |
| declared production chains | 20 | all 0 | all 0 | longest 39.816 s |
| production analyzer | 1 | 0 | 0 | 0.672 s, stdout 703375 bytes |

Both audit outputs equal their predeclared text. The longest chain is
L4_k1_b0_c4. Each production chain carries 128 blocks of 128 observations,
16384 production observations after 2048 warmup sweeps, and the final
completion marker. The controller used exactly eight workers and the
frozen deadlines; no invocation reached its deadline and none was retried.

| Preserved file | Bytes | SHA-256 |
|---|---:|---|
| audit.tsv | 59 | ca77c2a869d00235f493d8923abd08c64af61ac689c43eff1489023ae88840fc |
| analyzer_tests.tsv | 49 | 758995eca095b765986301e71dbdbbf305aa116c398267ff03fd52199c73c8cf |
| execution.json | 6720 | 8ca6f7c6455e12fb4ca7426192acba2055d4a22f076115659706f06faa6be2fc |
| analysis.json | 703375 | caaf5031c7df41f3570f9ac8808c5166569f5718fd87b594b3049bf23576b3db |
| SHA256SUMS | 4173 | 4e78692df99b2a4a9aa86c7ccfd9dd6568939ea2b5e608eac24325914f94aaa0 |

ENGINEERING contains 51 files. SHA256SUMS binds the other 50; every hash was
verified after transfer. execution.json records audit, fixtures and twenty
chains; analysis_execution.json separately binds the analyzer stdout,
stderr and exit. environment.json and controller_result.json preserve
actual environment, source/binary hashes, times and final controller result.
Empty stderr files are retained. No machine nickname, private infrastructure,
compiled binary or controller development log is published.

Frozen source files, unchanged after execution:

| File | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 6267 | `cfef370633293321491d218964dfc9774e8638539bb04e2b80cb5bee33232732` |
| REVIEW.md | 4634 | `97c55f9b536e5369953b21ffe8f3dd0c28536b406c19a220dbdff18b59af82f3` |
| sample.cpp | 32754 | `f629b60e71079b8e14623a1cadd9b7aaac303fb72e859679bba7a82eb08f43a3` |
| analyze.py | 27439 | `e253a555457a1428833c273b5d1a665536a978841b6d55d0fe85fefb956118e5` |
| test_analyze.py | 12665 | `f482e5acb08350d5b9b239dc455a269f817d6a6828821e189e612bfc2e35c5c5` |
| run_pilot.py | 5205 | `3dbe211fdf85a221f6900d6a7b20f17bcfb4e1ca39633410f242ad86d8e89251` |

The fixed analyzer's disposition is TRANSPORT_QUALIFIED with no custody,
mobility or stationary-control failure. This is the first and complete N2
attempt, now consumed. No source, threshold, budget or seed was changed.
Every signed quantity remains NONINFERENTIAL_ESTIMATE and every numerical
output has ZERO scientific evidential weight.
