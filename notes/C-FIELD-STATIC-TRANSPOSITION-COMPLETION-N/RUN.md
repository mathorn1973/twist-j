# First-run execution record

Status: **NON-CANONICAL, candidate-C finite exact audits, L1.** The universal conditional candidate-T claims are proved in PROOF.md. This record is not a public computational gate.

## Pin and execution order

Both first executions began after the joint freeze at `2026-10-08T22:23:09.200354+00:00`. The same unchanged proof and separate assistant review were included in that pin. FREEZE.json has SHA-256 `5b35c48854030895c0669ccf949eec814fc5ebc98fa4fcb5d51ad5dc64c6dc68` (1360 bytes).

The two programs ran as separate processes on the same x86_64 environment. Neither author read the other implementation; the parent inspected both sources before execution. Their domains and stdout schemas differ, and each first output is separately pinned for reproduction. This is independent implementation evidence on one architecture.

| Program | Result | Exit | Stderr bytes | Seconds | Input cases | Contact cases |
|---|---|---:|---:|---:|---:|---:|
| verify.py | PASS | 0 | 0 | 15.065681 | 14513 | 43539 |
| break_check.py | PASS | 0 | 0 | 13.230204 | 74384 | 223152 |

Input cases are state visits in the fixed domains. Repeated states occurring in different domains or histories are retained, so these are not counts of distinct states. Each input case is checked with all three contacts and all five pointer values. Exact assertion totals are 1204172 and 5123996; assertion count is an implementation statistic, not a count of independent mathematical claims.

Environment: Ubuntu 24.04.3 LTS, architecture x86_64, Python 3.12.14. The preset time limit was 300 seconds per program. Both completed on their first execution, with no source correction, timeout, rerun or fired new claim. Frozen input hashes matched before and after both processes.

## Exact first outputs

| Output | Bytes | SHA-256 |
|---|---:|---|
| verify.first.stdout | 13371 | `7b285b713da76c2c73b34d4e4c2f6b3cced91117dbf41c200a4dcc61582b497a` |
| verify.first.stderr | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| break_check.first.stdout | 6539 | `28f359edbdf06352feb692137b029c4711fafdcb46a39e8e2a9d737e4db54d4e` |
| break_check.first.stderr | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

The stdout files contain the complete first results; the stderr files are deliberately empty. The two `.run.json` files retain exact UTC start and completion times, command, environment, return code, sizes and hashes. No failure is hidden in a later replacement.

## Domain and branch coverage

| Domain | Primary cases | Independent cases |
|---|---:|---:|
| Raw integer fields and rotating matter/charge fixtures | 2916 | 3645 |
| Integral R/AM fields and funding boundaries | 11560 | 40907 |
| Dedicated R nonimage cosets and boundaries | included in raw domain | 29808 |
| Frozen witnesses and T7 receiver stages | 37 | 24 |

Both runs reach all seven inherited reaction outcomes: accepted R/AM, stock-rejected R/AM, R image rejection, nonintegral split, and other matter. Both include non-Gauss and non-neutral matter cases. All complete contact checks preserve the whole refusal output.

For the independent program, the admission-mismatch counts are:

| Contact | Accepted to rejected | Rejected to accepted |
|---|---:|---:|
| 01 | 0 | 0 |
| 02 | 525 | 494 |
| 12 | 525 | 300 |

The zero mismatch counts for 01 in these enumerated fixtures are reported as zero, not omitted or treated as a universal absence theorem. The 02/12 tests explicitly exercise both mismatch directions and funding rejections. AUDIT-SUMMARY.json and the first stdout files give every domain and branch count.

The independent finite maximality audit evaluated 160 candidate maps on 19 closed orbit cases (64 orbit-cell visits); 40 candidates commuted with G. The proposed completion was the unique greatest-support choice in every case. The infinite-carrier maximality result is the matter-projection proof in PROOF.md, not this finite enumeration.

## Exact witness outcomes

Both implementations confirmed the +5 static contacts, stock 7 to 2, total cell energy 335, and the preserved complete G square. Both found the prescribed failure of naive own-stock-only admission at r=5 and6 and the failure of incident stock-swap commutation. Both confirmed common-input prices (0,0,-5).

For T7 they checked every specified intermediate full tuple and its energy: source/receiver energies 81/343 and86/338, accepted AM guards exactly zero, final receiver energy424, identical final cells/link/pointer, and last receiver increases81 and86. Each old total is425 with the same pointer energy1. The primary implementation additionally reconstructed each full predecessor using its retained contact context.

## Reproduction

The custody wrapper refuses to overwrite the already preserved first run. To reproduce, use ordinary commands and new local output paths. Run each pair of lines separately from this directory:

```sh
LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 -I verify.py > verify.replay.stdout
cmp verify.first.stdout verify.replay.stdout

LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 -I break_check.py > break_check.replay.stdout
cmp break_check.first.stdout break_check.replay.stdout
```

A replay must also exit zero and have empty stderr. The first outputs are the byte references. Same-architecture agreement does not satisfy the public two-architecture gate; that gate has not been run for this candidate. Public PR #1424 checks and its older 183-test tools report concern their own pinned files, not this continuation.
