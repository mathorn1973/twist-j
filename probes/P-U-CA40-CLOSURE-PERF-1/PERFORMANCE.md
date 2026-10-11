# Completed prefix regression; speed target missed

PUBLIC NON-CANONICAL. Status C, conditional L1 engineering evidence.
Original record Apache-2.0, A. M. Thorn, 2026-10-11.

All six frozen children completed, passed runtime fixtures and retained
identical endpoint, partial-account and basis bytes. The observed median
propagation-window speedup was 1.4377742506583304.
The preregistered target of at least 2 was **not met**. End-to-end median
speedup was only 1.0107036906628437.
The outcome is PREFIX_SPEEDUP_TARGET_MISSED, with no missing repetitions,
timeout, retry, source repair or discarded warmup.

## Source, environment and execution

The immutable source pin is
`a7f88f96b7e1d8c20ad78f4079264055120ff87a`.
All fourteen source files passed public byte readback at
2026-10-11T13:02:58.390843+00:00, before the first execution.
SOURCE_SHA256SUMS binds thirteen source files. The pulse/input remains
10093 bytes with SHA-256
`ca6b286c9e6d45795677b05e09fbe1b38043c8ff8369b57b652c83195a156d53`.

The environment was Debian GNU/Linux 13 (trixie), x86_64, Python 3.13.5,
GNU C++ 14.2.0, MPFR 4.2.2-1 and GMP 2:6.3.0+dfsg-3.
Both builds used the same common harness and
`-O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math -fno-tree-vectorize`,
with explicit AVX-512F/DQ/VL functions and system MPFR/GMP libraries.
Private extracted development headers supplied the build includes.
Both compilers exited zero with empty stdout and stderr.

| Executable | Bytes | SHA-256 |
|---|---:|---|
| baseline | 348496 | `b42a252d8515ca125fdc159f0e79dceb4b5bbd9f1a16ea9fa77b7a1db168efdb` |
| optimized | 357224 | `16e0e1f6e516ec993594f391d3a6ce3044594bfab26ec9d00a0bfa240f8b72e9` |

The exact supporting gate passed in 1.0165355056524277 s;
EXPECTED.txt and RUN.md preserve its actual 521-byte stdout. This gate
alone establishes no floating or performance result.

The short runner began at 2026-10-11T13:04:14.032939+00:00, ended at
2026-10-11T13:12:41.951938+00:00, and took 507.91903357207775 s in total.
Its fixed 1800-second budget and all 300-second child budgets were respected.
Each child used L8/G10/N512, 90 tasks, eight thermal lanes, six signed-label
cases and all 120 thermal columns. Each trajectory evolved only its first
four occupied cells from the original thermal basis column and absolute
model time. No full trajectory was attempted.

Every child reported all 80 distinct threads, CPUs and singleton OpenMP
places, both SMT siblings of 40 physical cores on two packages, and zero
observed start/end migrations. OpenMP dynamic teams and nested parallelism
were disabled. This is not a new 40/80-thread or AVX2/AVX512 comparison.

## All six timings

Seconds, rounded here to nine decimals; original binary64 values and receipts
remain in the retained evidence. B,F,F,B,B,F was fixed before execution.

| Run | Variant | Preparation and fixtures | Propagation window | End-to-end |
|---|---|---:|---:|---:|
| 1 | baseline | 44.792878857 | 30.475612655 | 75.860232605 |
| 2 | optimized | 94.407367101 | 21.764226967 | 116.757609410 |
| 3 | optimized | 44.877199324 | 20.206652753 | 65.671197139 |
| 4 | baseline | 44.919441581 | 30.429146644 | 76.031153159 |
| 5 | baseline | 44.658017999 | 30.830874849 | 76.160500824 |
| 6 | optimized | 53.441960284 | 21.196382284 | 75.225957777 |

| Metric | Baseline median, s | Optimized median, s | Baseline / optimized |
|---|---:|---:|---:|
| preparation_seconds | 44.792878857 | 53.441960284 | 0.838159353 |
| kernel_seconds | 30.475612655 | 21.196382284 | 1.437774251 |
| end_to_end_seconds | 76.031153159 | 75.225957777 | 1.010703691 |
| child_wall_seconds | 76.063982558 | 75.268610612 | 1.010567113 |

The propagation window includes worker startup, Work/BWork allocation,
barriers, dynamics, certification and progress logging. It excludes model
preparation, fixtures, final endpoint norms, serialization, hashing and
runner comparisons. End-to-end includes the child's preparation and final
serialization; child wall time additionally includes process overhead.
The whole runner also includes validation and custody work.

Preparation was intentionally unchanged and varied substantially, including
94.40736710093915 s in run 2 and 53.44196028448641 s in run 6.
Both observations remain in the medians and record. No cause for this
variation has been established; it cannot be credited as a kernel effect.
A read-only load/process snapshot during run 2 found the benchmark as the
only substantial CPU consumer at that instant; this is not continuous
resource isolation or a statistical performance model.

The exact rational comparison of the recorded medians gives
T_B < 2*T_F. Three repetitions establish an observed median only.
There is no confidence interval, universal speed claim or extrapolated
full-campaign completion time.

## Strict bit equality and numerical checks

Each of the five subsequent runs was compared directly with run 1,
without a numerical tolerance. Every comparison covered all 74,131,200
endpoint bytes, all 69,120 component bytes and all 103,053 basis bytes.
This includes 720 complex endpoint vectors of dimension 6435 and twelve
binary64 partial-account fields per case/column. Signed zero is included.
The JSON component records also reproduced the raw binary64 bytes.

The common artifacts have these identities:

| Artifact | Bytes per child | SHA-256 common to all six |
|---|---:|---|
| basis.json | 103053 | `5472cc292d770ffe229ce79edc1d242bf498c197fb84d090f40d6bd8248039f3` |
| components.bin | 69120 | `1f884c5e53c2297b6d641fb85c5e845c7232ee803655d9045f158a43b0843ea7` |
| endpoints.bin | 74131200 | `39b46fd4e46c4c08119ffd4f9c8cec079ea3db99b6b7b028609ae83d668268fe` |

All six runtime checks passed: embedded directed arithmetic, gradual
underflow, zero displacement, adjoint enclosure, dense/collective
displacement comparison and small norm-ball versus interval enclosures.
All source, serialized input and executable custody comparisons passed
before and after attempted children and at runner exit. All child exits
were zero and all child stderr files were empty.

No endpoint normalization, branch phase fit, reduction-order tolerance or
weakened error allowance was used. The original conservative guard-space
underflow term was retained. The equality is a regression result on the
specified prefix, not a proof that every future floating execution is equal.

## Evidence and limits

The private compact archive has 619441 bytes, SHA-256
`9fdecc37f290309e8d145e46bed5fd76f80d87e9e250339e0ef1fe35f4d53423`.
Its manifest binds 89 records. It includes all non-binary records;
six endpoint and six component files are retained separately with hashes
in the same manifest. All compact entries were locally checked by byte
count and SHA-256 after transfer. Raw records and machine paths are not
published here.

This engineering test does not close either angle's full numerical error
account. The partial guard/tail/continuum/jump values are not final radii.
No final restored-frame coherence or full-source preservation result was
computed. Protected source-reference identity still depends on the existing
exact-darkness premise; the unknown-source no-imprinting boundary is unchanged.

The narrow optimization is bit-preserving on this test and reduces its
propagation time, but it does not satisfy the substantial-speedup target.
No long campaign was started or authorized by this outcome. A coarser or
adaptive time grid would require separate derivation, source pin and error
checks while keeping the pulses fixed. This probe is sealed after its first
complete outcome and must not be resumed or tuned to improve this result.
