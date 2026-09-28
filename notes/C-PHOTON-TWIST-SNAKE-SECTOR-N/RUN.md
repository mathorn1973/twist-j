# First frozen engineering execution

**PUBLIC / NON-CANONICAL. No scientific evidential weight.**

The complete prospective source pin is
`b79ca3df6d5a4b43358218bcb16076e6edc80930`. It was committed, pushed,
read back through Git and GitHub, and recorded in issue #1265 before the
first compilation for execution. The checkout was clean at that pin. The
eight frozen files remain byte-identical after execution; their SHA-256
values are those recorded in the issue:

| File | SHA-256 |
|---|---|
| PREREG.md | 02ca3b88f0efa9c507b2c3d38e3f92b1318d2e8ec6ab7b02d25182e87f8f9848 |
| PROOF.md | fd80251e3135a61b7687e884e46e072c2708fbaa696a44c860e0c67db5544e3b |
| REVIEW.md | e67cf045011e5cfe346ce653ce59d07ec61eb3d3a5ac4dfc5889a61929ca956e |
| sample.cpp | 363b1a2174c6b2d13cf841de8894b98698dd18d16bf89d9db119887638724adc |
| analyze.py | 93e5982dbc33123ea3939d76d999169654d675b0ed5c9b055914822ae018c0a2 |
| run_snake.py | 71adfe4909492cbf2d83a489c69ae342aced802c0a003d80b9a28082e0445876 |
| run_analysis.py | a6bc0380bb8fa068a01aca8487dcbf7cbd12315cf20fe55f411f3f79a143935e |
| test_analyze.py | 66a22dbb6c43092668052e7baa2524c3449f975b5b079841ad698b3ad37b8d3b |

## Environment and commands

- Start: 2026-09-28T08:43:21Z. Controller end: 2026-09-28T10:22:15Z. Analysis end: 2026-09-28T10:22:25Z.
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
`21c5cb2ebe983c325131cf26f928da226d063297f8136f7c83e8348fa6318805`,
identical to the pre-pin build recorded in PREREG.md. The three commands
were issued once, in sequence, by one shell script that also recorded the
UTC times and process exit codes; no launch was repeated.

## Preserved execution outcomes

The controller exited zero with empty stderr. Its first
engineering audit exited zero with empty stderr and a 384-byte stdout
whose SHA-256
`c1286c6e30e6876c1e1c4bba0a20efdcf9e94eb4d0e2958739cb094300c8533e`
is byte-identical to the pre-pin transcript recorded in PREREG.md and to
the copy embedded in `analyze.py`. This tests the frozen implementation;
it is not a computed theorem gate.

All 136 declared sampling jobs completed with exit code zero and empty
stderr, each with its full frozen schedule and block records; every
printed sweep total matched the schedule formula and every restricted
chain stayed in its class. The longest job (L=10, k=1, class-minus
chain 1) took 896.994 s. At L=10 the ten unconstrained round-trip jobs
took 824 s to 848 s, the eight restricted up-only jobs 893 s to 897 s,
the four restricted top-dwell jobs 165 s to 167 s and the eight step-zero
jobs 119 s to 124 s; at L=8 the corresponding ranges were 217-229 s,
248-260 s, 66-68 s and 48-52 s; the L=6 jobs took 15 s to 68 s and the
L=4 jobs 3 s to 8 s, including the sixteen control jobs at 41-43 s and
4.5-5 s. The declared jobs used 23554 CPU-seconds in 99 minutes of wall
time. No timeout, retry, extension or post-observation change occurred.
Exact per-job byte counts, hashes, durations and process outcomes are in
`ENGINEERING/execution.json` (42470 bytes, SHA-256
`3cfc36699a2421b55581aa5652757afbeab02c8c91732040819b1c52f2316e1c`).

The analysis wrapper ran `analyze.py` as a subprocess and recorded its
exit code zero, stdout of 1779415 bytes with SHA-256
`7ecdfe4ce94fa7579d0bd3873d1a31db0d076e879b7d26d3374ab87f320e688f` and
empty stderr in `ENGINEERING/analysis_execution.json`; its custody checks
found no error. The analyzer reports `INCONCLUSIVE_EQUILIBRATION`. The
analyzer was not rerun.

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
