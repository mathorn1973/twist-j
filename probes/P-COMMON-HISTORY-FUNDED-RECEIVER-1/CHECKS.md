# Custody, repository gates and scientific replay receipts

PUBLIC / NON-CANONICAL / L1. A. M. Thorn; Apache-2.0.

## Pre-run public custody

The pin is `2c618efc2e28606edb12ada2f77a06aa0d798d55`. Before the first
scientific execution, its public branch ref and each of the seven full
file contents were fetched from GitHub and compared with the committed
local file, including Git blob ID. Every comparison was byte-identical.
The receipt is issue #1626 comment 6253105699. The worktree was clean
at that pin when the first command began. RUN.md records that execution.

SOURCES.tsv contains 29 exact-commit source records with Git blob ID,
independently computed SHA-256 and byte count. All nine custody entries
printed in ERRATA.md were compared with that manifest and agree. Hashing
source bytes and parsing the verifier's AST were metadata/static operations,
not pre-pin scientific execution. All seven pinned files remain unchanged.

## Required local gates

The following repository commands completed with exit code 0 after the
first result was recorded. All used Python 3.12.14 on Ubuntu 24.04.3 LTS,
x86_64, with interpreter -B suppressing bytecode caches.

| Command | Observed outcome |
|---|---|
| python3 -B tools/check_policy.py | POLICY PASS |
| python3 -B -m unittest discover -s tools -p 'test_*.py' | 189 tests; OK |
| python3 -B tools/check_canon.py | CANON PASS v103 claims=530 |
| python3 -B tools/check_ledger.py | LEDGER PASS claims=530 items=594 dependencies=1105 evidence=530 history=1077 gates=26 programs=7 |
| python3 -B tools/check_gate_contract.py | GATE CONTRACT PASS gates=26 |
| python3 -B tools/check_verifier.py --base dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d | VERIFY PASS for this exact probe and both hashes below |
| python3 -B tools/check_reproduce.py --base dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d | REPRODUCE NOT APPLICABLE |

The unit suite deliberately exercises failing gate fixtures; its intermediate
PROBES FAIL/REPRODUCTIONS FAIL lines are expected test output. The suite
exit code was zero and all 189 tests passed.

The changed-probe replay actually selected
P-COMMON-HISTORY-FUNDED-RECEIVER-1 and executed its verifier again. It
validated the ancestor pin, unchanged verifier, empty stderr, zero exit and
byte identity to the committed-for-submission 602-byte EXPECTED.txt:

- verifier SHA-256: 493db96149dcba94119f273fb3d12e40a7b6a9105b6e36337cc7524e337f3558
- stdout SHA-256: e21cd4fc5c84a6349b6b44912027a5c4ef41c12d0b287dfe6faec178abe0457a

This is same-architecture reproduction of the first local execution, not
two-architecture evidence. GitHub architecture results will be recorded
only after their actual changed-probe logs have been read.

## Scope and security audit

Changes are confined to this one new probe directory. The original seven
pin files have no diff against their pin. No Canon, registry, workflow,
policy, original N/R1/R2 record or foreign branch is edited. The code is
standard-library exact arithmetic with no network, subprocess, file writes,
external data or environmental stdout. Added text contains public source
identifiers and neutral run descriptors, not credentials or private host
identifiers. Apache-2.0 authorship notices are present. git diff --check
passed. No merge or release is part of this submission.
