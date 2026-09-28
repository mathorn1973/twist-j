# First frozen engineering execution

**PUBLIC / NON-CANONICAL. No scientific evidential weight.**

The complete prospective source pin is
`1c82ae6ff83d8f7e7ed6c4b1ad7a3256f29e9422`. It was committed, pushed,
read back through Git and GitHub, and recorded in issue #1259 before the
first compilation for execution. The checkout was clean at that pin. The
eight frozen files remain byte-identical after execution; their SHA-256
values are those recorded in the issue:

| File | SHA-256 |
|---|---|
| PREREG.md | bd94005ea235103b758f7dd1c2381d2abd190e57ac4265f7ed008e65b71bacee |
| PROOF.md | 11a0dc8bc3feda88e4d991a95dcfced83dba96fe66b3157bda65daab7e5a7cd4 |
| REVIEW.md | b51b8ec46347c6bcd9741ba1d3b55b69265472ef3549ad7128a1e1863ed53de0 |
| sample.cpp | eb1c8f12efedf08906cba3f8047a76b7032b1b3e14bb0b2e52e551c0b6638523 |
| analyze.py | 051de89c121b1f4eb8fbdd3e52f8e138a4e3deae9fbdfc103cf798bf5bfc128c |
| run_snake.py | 2adaea53b74ecaea250ca6a818a7d001d268f7d44c2205b91d41c3d418f22ebe |
| run_analysis.py | a6bc0380bb8fa068a01aca8487dcbf7cbd12315cf20fe55f411f3f79a143935e |
| test_analyze.py | fe17489afc9cf8594eed218cdf8e8748a9bf487dd259e498b49c06d1230acbbe |

## Environment and commands

- Start: 2026-09-28T05:38:52Z. Controller end: 2026-09-28T06:16:45Z. Analysis end: 2026-09-28T06:16:49Z.
- Platform: Linux; architecture: x86_64; four processors.
- Compiler: GCC 13.3.0, Ubuntu 24.04 package. Python: 3.11.15.
- Four concurrent jobs; 600-second audit and 2400-second per-job deadlines.
- No fast-math, external numerical library or adaptive tuning.

The pinned `sample.cpp`, `run_snake.py`, `run_analysis.py` and
`analyze.py` were extracted from the pin commit into a fresh external
workspace. The commands were:

```sh
g++ -std=c++17 -O3 -ffp-contract=off -Wall -Wextra -pedantic sample.cpp -o BINARY
python3 run_snake.py BINARY NEW_RUN_DIRECTORY
python3 run_analysis.py NEW_RUN_DIRECTORY
```

`BINARY` and `NEW_RUN_DIRECTORY` denote fresh external workspace paths;
no executable or private machine path is published. The compiled binary
SHA-256 was
`72ec9f6cdd3107fda4cac98d95171c1d166f030b2777c7b23d6752a7002e8794`,
identical to the pre-pin build recorded in PREREG.md. The three commands
were issued once, in sequence, by one shell script that also recorded the
UTC times and process exit codes; no launch was repeated.

## Preserved execution outcomes

The controller exited zero with empty stderr. Its first
engineering audit exited zero with empty stderr and a 238-byte stdout
whose SHA-256
`1e2f30627085f6d5b46ae16e1e1249c1041e74ca01447dd8dd73bf0e6c90a41d`
is byte-identical to the pre-pin transcript recorded in PREREG.md and to
the copy embedded in `analyze.py`. This tests the frozen implementation;
it is not a computed theorem gate.

All 56 declared sampling jobs completed with exit code zero and empty
stderr, each with its full frozen schedule and block records. The longest
job (L=10, k=2, chain 3) took 665.809 s; the ten L=10 jobs took between
649.953 s and 665.809 s, the L=8 jobs about 176 s to 181 s, the L=6 jobs
about 34 s to 36 s and the L=4 jobs about 4 s. No timeout, retry,
extension or post-observation change occurred. Exact per-job byte counts,
hashes, durations and process outcomes are in `ENGINEERING/execution.json`
(17345 bytes, SHA-256
`61dbffcd469c7a60a6660e31a8cb9c1ad0a92e2f9974383a2d7e6515d4a320f0`).

The analysis wrapper ran `analyze.py` as a subprocess and recorded its
exit code zero, stdout of 639195 bytes with SHA-256
`144456b0897bf0d40a0982d89620b412d7e863a16cc18f904956f5f64ae61c43` and empty stderr in `ENGINEERING/analysis_execution.json`.
The analyzer reports `FAIL_CONSISTENCY`. The analyzer was not rerun.

## Custody and scope

`ENGINEERING/` contains the complete block records, empty stderr
records, the execution and environment manifests, the controller
`SHA256SUMS`, the analyzer output `analysis.json` and its stderr, the
analyzer execution record and `SHA256SUMS_FINAL` over every file. No
private controller log, executable or machine identifier is included.

The result is the disposition described in RESULT.md. The mathematical
identities do not depend on it. Normal repository architecture checks
concern repository consistency, not an independent reproduction or
scientific validation of this floating-point run.
