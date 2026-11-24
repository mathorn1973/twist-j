# Prospective five-hour execution record

This record fixes the bounded, non-canonical run of the existing
preregistration. Source revision `ded7d21732216ea28659bdd5d4b7b2521e1af702` supplies the
sampler, stream drivers, reader, analysis and exact ordering argument.
The laws, observables, nominal precision threshold, chain starts, seeds
and decisions in PREREG.md are the registered requirements.

Run (L=16) and then (L=24). Use four parallel chains with ten
disjoint physical-core places within each chain and OpenMP binding set
to close. Disable dynamic and nested OpenMP teams. The reader pool
contains 24 processes and the numerical libraries use single-thread
operation. Private custody retains the exact affinity map and commands.

Use Linux x86-64, GNU C++ 14.2.0, Boost 1.83 headers, CPython 3.13.5,
NumPy 2.4.2 and 64 significant bits in long-double arithmetic.
Build with C++20 and `-O2 -Wall -Wextra -Wpedantic -Werror -fopenmp`.
The compiler, executable, diagnostic code and measured streams are held
in custody. The compiled sampler uses the checked generated sources.

| Item | SHA-256 |
|---|---|
| GNU C++ executable | `6b3696e4dcb85e1c949c732a02befa50e3983ecf94ce7e8e58d9d503b954b79d` |
| Ordered streaming sampler executable | `d035240e9d904bae6fa247f9f2c8821a92307ba02a95f606f48e836ab8fe784e` |
| Technical calibration receipt | `4ad6cd339a0724a06709e81820f1fb76a1b12393bfae8602412cc5dec51fb62d` |
| Bound versus serial stream and independent replay fixture | `544b811d2981e0e0188cbf39a0ec7a33013643d552b6168db869ae6e146188fc` |
| Lease supervisor | `fed42c7001fb5c88a54db6367e04c7400ff41fb085169747901a588328d3bbc2` |

Runtime source digests are recorded below.

```text
2618e71beef2ae4fd26002b1940a4239b68bfcbd5e48fd14dea1a53a060aaf43  run_ordered_volume.py
73e8043b13ddb1e694a56575fd6c5e98461373ff2d38696e74b67d954b985577  replay_ordered_volume.py
3023331a7f6582315ba9b42a249bfd81a32071df09e0d5eceb41624659bad895  analyze_ordered.py
fbebd8bd6e031d9187bccf3cfd4916228efd50c3f636b882aa314fcd3b384cba  analyze_descriptive.py
7c9e311d815b1525d6ac7a64611875ecbfc2572dffd1a3076856e6170daf60f7  ordered_reader.py
d9c6cdbd4e77766a066ca48d230d123f58218a83535bb8685e260b997a83ba23  parallel_ordered_reader.py
00f24a7dd0a4e831c9f3c9c133f1dd9cc4488f3091987f79a22cb0911ded2aed  ordered_sentinels.py
d3d2ffba5ade37863f8e34a9b6c8198cf3e222aa8f12a6ba78b621d5c5bef4ce  analyze_pilot.py
```

The technical calibration used separate seeds and actual stream framing,
all applicable primary and secondary intervals, and a fresh digest replay.
All eight chain ledgers from the serial and parallel reader paths matched
byte for byte across the two volumes. The independent reader fixture suite
passed 16 tests. The bound stream fixture matched serial-kernel logs and
reader ledgers on both volumes and independently replayed eight states
per configuration on each volume. The calibration rates give approximate
first-endpoint costs of 3,624 and 13,019 seconds, respectively.

The global lease is 18,000 wall seconds starting at the first technical
calibration. It includes setup after that point, analysis and teardown.
Stage caps use the following seconds, including driver teardown.

| Volume | Generation | Digest replay |
|---|---:|---:|
| 16 | 2,800 | 900 |
| 24 | At least 8,550 at admission | 4,350 |

Start a volume only when its two allocations and 120 seconds for final
analysis fit in the remaining lease, with three seconds for handoff.
For (L=24), the generation cap is the remaining whole seconds at
admission less its replay allocation and the 123-second reserve. Replay
begins after a complete generation receipt, including if measured
sentinels fail. If verified ledgers are available, analysis may use up to
600 seconds within the same lease.

Each volume evaluates the blinded thermal candidates in their frozen
order. Its first passing candidate fixes the measurement prefix, followed
by 4,096 consecutive saved states on each of the four chains. Replay
regenerates these states from the same seed starts and verifies the full
thermal controls and state digests. Retain all budget, mixing, arithmetic
and integrity stops and partial records. Neither seed substitution nor
extension of the five-hour lease is authorized by this record.

Admission requires the registered measurement diagnostics, arithmetic
and precision checks, and complete replay. Two volumes give at most a
descriptive fixed-scale comparison. The registered row and the ordered-limit
interpretation require the rest of their prescribed evidence.
