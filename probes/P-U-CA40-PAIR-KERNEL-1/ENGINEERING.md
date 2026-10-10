# SIMD engineering measurements

PUBLIC NON-CANONICAL measured engineering appendix. Original text Apache-2.0.

The complete frozen campaign passed. Every invocation evaluated 512 synthetic coefficient contexts over all 78,125 basis labels, repeated four times: 160,000,000 context/label evaluations. There were four warmups and 20 measured invocations in five rotating rounds. TIMINGS.csv lists all 24 observations in execution order.

## Kernel measurements

Times below are seconds measured internally around the parallel kernel; setup, coefficient generation, numerical validation, buffer allocation and process startup are excluded. Work includes the fixed kernel checksum and repeat barriers.

| ISA | Threads | Median s | Min s | Max s | Sample SD s | Million branches/s | Speedup over AVX2/40 |
|---|---:|---:|---:|---:|---:|---:|---:|
| AVX2 | 40 | 1.421743825 | 1.418853931 | 1.447076101 | 0.013525035 | 112.538 | 1.0000 |
| AVX512 | 40 | 0.837884776 | 0.836641602 | 0.841680983 | 0.001958603 | 190.957 | 1.6968 |
| AVX2 | 80 | 1.182415690 | 1.166287882 | 1.195403242 | 0.010461226 | 135.316 | 1.2024 |
| AVX512 | 80 | 0.735334244 | 0.730509775 | 0.738922073 | 0.003151588 | 217.588 | 1.9335 |

The pilot therefore selects AVX-512/80 as the starting configuration for this kernel. Relative to AVX-512/40, 80 threads increase throughput by 13.95%. Relative to AVX2/80, AVX-512/80 increases throughput by 60.80%. These are ratios of medians from this campaign, not confidence bounds.

## Process observations

| ISA | Threads | Wall median s | Wall min s | Wall max s | Sample SD s |
|---|---:|---:|---:|---:|---:|
| AVX2 | 40 | 1.617128922 | 1.616980264 | 1.617392648 | 0.000177350 |
| AVX512 | 40 | 0.966251617 | 0.966142042 | 0.966634028 | 0.000192732 |
| AVX2 | 80 | 1.370741207 | 1.368861169 | 1.372646488 | 0.001492087 |
| AVX512 | 80 | 0.921979524 | 0.873576986 | 0.972708490 | 0.040997027 |

The outer wall interval includes capture-file opening, process launch, validation, allocation and waiting for child completion; it excludes JSON parsing and source-pin checks. The timeout-based Python child wait can add polling latency, so it is an observed wrapper duration, not a precise process-exit timestamp. Kernel timing is the primary comparison. Neither interval includes source transfer or compilation.

## Correctness and placement

All 24 children returned zero, produced empty stderr, passed every frozen validation, and reported exactly 160,000,000 processed branches. The reported maximum scalar/SIMD or long-double point-check discrepancy was zero for these dyadic fixtures. This does not make future non-dyadic physical coefficients exact. The small Gaussian/Weyl assertions passed their separately declared 1e-14 threshold; their individual residuals are not reported as zero.

All invocations agreed numerically exactly on the three frozen diagnostics:

```text
checksum = 85.413066316396
phase_max = 0.01568603515625
r_max = 5.433801561594009e-06
```

Every actual thread/CPU/place map matched the requested unique CPU places. Forty threads used one sibling on each of 40 physical cores, balanced 20 per NUMA node; 80 threads used both siblings, balanced 40 per node. Workers first-touched their private output buffers. The immutable label tables and shared coefficient allocation were not explicitly NUMA-interleaved, so this is not a claim of optimized placement of all shared data. OpenMP binding was fixed, dynamic teams disabled, and secondary math-library thread pools limited to one. No child timeout, placement failure or diagnostic mismatch occurred.

## Environment and custody

The execution system was Debian GNU/Linux 13 (trixie), x86_64, kernel 6.12.90+deb13-amd64, Python 3.13.5. Hardware readback identified two Intel Xeon Gold 6138 processors, 20 physical cores each, SMT2, two NUMA nodes and 80 allowed logical CPUs. RAM readback was 1,583,896,332 KiB. AVX2 and AVX-512F/DQ/VL support was checked. The pre-run load averages were 0.03271484375, 0.01171875, 0.00048828125. No CPU frequency lock, thermal telemetry or hardware performance counters were imposed, so this is a short engineering pilot under the observed system state.

Compiler: `g++ (Debian 14.2.0-19) 14.2.0`. Frozen build command, with an external output path:

```text
g++ -O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math -fno-tree-vectorize contact_bench.cpp -o <external-output>/contact_bench
```

Compilation completed with exit zero and empty stdout/stderr. Dispatch uses the compiled per-function ISA paths, with no global native-architecture flag.

Immutable source pin: `179199a8972187edb70f576ae4af8aa9078805d2`. SOURCE_SHA256SUMS binds the five science/document inputs and is itself bound by that Git commit. The runtime runner checked source and binary hashes before and after every child.

Binary SHA-256: `65de8e273e990801ab56227cc852dc39d1dbc966b979b8899b0bc3adc6e82ebd`.

The campaign began at 2026-10-10T18:11:05.751146+00:00 and completed at 2026-10-10T18:11:35.189433+00:00. Complete raw child outputs, thread maps, metadata and the source/binary custody records remain in the external execution record. Their sanitized timing projection is TIMINGS.csv; no private paths or raw machine logs are published here.

## Scope

These coefficients are synthetic and do not share a demonstrated physical waveform origin. The code screens a conditional Gaussian branch model, not the full ion apparatus, complete contact or experimental measurement panel. The reported synthetic comparison bound is model-only and is not a measured gate error. Current work is theoretical and numerical only. A new waveform-derived study must validate its own non-dyadic arithmetic and source, reference, bus and energy/work contracts.
