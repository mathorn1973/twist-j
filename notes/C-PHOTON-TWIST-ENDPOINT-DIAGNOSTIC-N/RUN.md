# First frozen engineering execution

**PUBLIC / NON-CANONICAL. No scientific evidential weight.**

The complete prospective source pin is
`12942b6fc5a7540b7ff73cc65e9725ef4b4625e8`. It was committed, pushed,
read back through Git and GitHub, and recorded in issue #1249 before the
first audit or sampling invocation. The checkout was clean at that pin.
The six frozen files remain byte-identical after execution.

## Environment and commands

- Start: 2026-09-27T21:08:49Z.
- Platform: Linux; architecture: aarch64.
- Compiler: GCC 13.3.0, Ubuntu 24.04 package.
- Python: 3.12.3.
- Eight concurrent jobs; 900-second per-chain deadline.
- No fast-math, external numerical library or adaptive tuning.

With the frozen note directory as the source directory, the commands were:

```sh
g++ -std=c++17 -O3 -Wall -Wextra -pedantic sample.cpp -o BINARY
python3 run_pilot.py BINARY NEW_RUN_DIRECTORY
python3 analyze.py NEW_RUN_DIRECTORY > analysis.json
```

`BINARY` and `NEW_RUN_DIRECTORY` denote fresh external workspace paths;
no executable or private machine path is published. The compiled binary
SHA-256 was
`4498cd9d48bb344de6dac398aa452c606c1dd51ed98ddc88107d3713d3710cf9`.

The remote launch channel reached its ten-second response deadline while
the original detached controller continued. Inspection confirmed the
original running invocation and its output; no launch was repeated.

## Preserved execution outcomes

The controller exited zero with empty stderr. Its first engineering audit
exited zero with empty stderr and 110 stdout bytes:

```text
NON-CANONICAL floating-point engineering audit
geometries	3
fixture_states	12
mutations_caught	24
result	PASS
```

The displayed separations are tabs. The exact bytes are in
`ENGINEERING/audit.tsv`, SHA-256
`50b413540f8b8193242f10a5539582f15ea4af518223ac1175b18e6ddcc15ae7`.
This tests the frozen implementation; it is not a computed theorem gate.

All 24 declared sampling jobs completed with exit code zero and empty
stderr. Each retained exactly 4096 production observations in 32 blocks.
The longest job took 41.320 seconds. No timeout, retry, extension or
post-observation change occurred. Exact per-job byte counts, hashes,
durations and process outcomes are in `ENGINEERING/execution.json`.

The first frozen analyzer output is preserved as
`ENGINEERING/analysis.json`, 87167 bytes, SHA-256
`d5b48289d55d028b29c7635355fa487def2ced7ea9f0b4436c58686e1ee23b38`.
Its stderr was empty. The surrounding shell command did not capture the
analyzer's separate process return code; that field is **not separately
recorded**, and no return code is inferred or presented as observed.
The preserved output reports no execution-custody error and gives
`INCONCLUSIVE_MOBILITY`. The analyzer was not rerun.

## Custody and scope

`ENGINEERING/` contains the complete block records, empty stderr records,
execution and environment manifests, the original controller-generated
`SHA256SUMS`, and the first analyzer output. That original checksum file
covers the controller outputs before the analyzer output was added.
The analysis hash above binds the additional file. No private controller
log, executable or machine identifier is included.

The result is the failed mobility qualification described in RESULT.md.
The mathematical identities do not depend on it. Normal repository
architecture checks concern repository consistency, not an independent
reproduction or scientific validation of this floating-point pilot.
