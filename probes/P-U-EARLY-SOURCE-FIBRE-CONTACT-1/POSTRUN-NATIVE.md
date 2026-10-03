# Post-run native artifact equivalence review

**PASS: the primary and independently authored retained outputs agree throughout the compared complete domains.** This is an artifact review of the coordinator-authorized first formal run at public pin `9754d85622844d40212288d2204fc240e6cd8e31`. No native algorithm was imported, executed or rerun for this review, and no pinned file was changed.

## Run and source custody

The retained receipt is `runs/native-001/RUN.json`: Windows11 x86_64, Python3.12.10, command `python3 probes/P-U-EARLY-SOURCE-FIBRE-CONTACT-1/verify.py`, start `2026-10-03T23:24:38.773316+00:00`, completion `2026-10-03T23:24:43.214726+00:00`, exit0 and empty stderr. The 2377-byte LF stdout has SHA-256 `613ac47b49187ee1e7b89f7587ca393d8b82c71815d7d55a20605fbf7756925e`. Its primary and independent reports equal their respective retained SUMMARY.json objects.

All14 input entries in BEFORE.json were compared against the actual Git blobs at the public pin, including byte counts and SHA-256 hashes. All11 public source entries in pinned SOURCE.json were also verified against that pin's files. The primary evidence manifest and independent evidence manifest match the retained artifacts. In particular:

| Input | SHA-256 |
| --- | --- |
| `primary.py` | `7e3b422d0ebb5a510cfc469b9962d24cbc9ebd14da53d1949a50ca39e26887e1` |
| `independent_native.py` | `f12bbe502c218ca549c7f72fed69d996c7f562c6db9c71e4efd4c0c4225a2fc1` |
| `verify.py` | `58a9ce2a846572842927f2fb18307a30bd7fe216b16233af3c35f53e319191c4` |
| `INPUTS.sha256` | `ff17153e65f0ef8a61e2f423623d92adc58095320eab87b8266d6e24e81f1ea4` |
| `SOURCE.json` | `23f6e936110afc5b0446eb6035286a1c28801b4ecae44534bc5e5506bd68b59b` |

The independent program is exactly the pre-primary-exposure v2 source recorded in FREEZE.json. This review does not rewrite that chronology or claim blind outcome prediction.

## Complete history comparison

Parsed primary `NATIVE-STEPS.csv` and independent `FULL-HISTORIES.json` in their recorded order and required literal equality of the initial head, every counter, every six-coordinate checkpoint and each selected generator. All15625 distinct canonical initial heads were present, with no row omission or surplus. Agreement covers:

- 62500 complete checkpoints and all375000 coordinate values;
- all62500 counters, at0,1,2,3 for every head;
- all46875 selected generator indices;
- all125 primary fibre-table rows against the corresponding independently retained full histories.

This comparison consumed saved states only. It did not regenerate a trajectory or select a new generator.

## Complete rejection-witness comparison

Compared all225000 independent receiver/time records with the matching primary per-time CSV streams, preserving configuration and lexicographic witness order. For every row, the eight common receiver-configuration parameters, first failing `(x,y)`, actual receiver reading and required reading agree. The primary witness's full initial/final states and counters also agree with the independent retained history for that head and time.

There are exactly75000 matching rejections at each of t1,t2,t3. The primary survivor CSV has no data rows, and both reports have zero survivors in all fifteen time/source-sum cells. The independent per-record mismatch counts reproduce its reported mismatch histograms. No new test family or scientific threshold was introduced.

## Exact compared artifact hashes

Paths below are relative to `runs/native-001/evidence/`.

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `NATIVE-STEPS.csv` | 1051563 | `a821aedf52252349ab1fa3544c68d00bd0eccac9b3a7376655a94a4c99329af1` |
| `independent/FULL-HISTORIES.json` | 2156253 | `9253716927d6c0d88f09e8e76d0330bb559fe6f980acc34fd0de7991a4274831` |
| `FIBRE-TABLE.csv` | 3081 | `1a8971d74424b8e3a6f75ffdd895de8f94832919259e2dd47cad8d9a2a0949bd` |
| `FALSIFIERS-T1.csv` | 4554977 | `c2c94222f4ca6debf0a3b27eeadc798f3777636b10de453f75104a422261750c` |
| `FALSIFIERS-T2.csv` | 4555030 | `6a4bcdbe5de90570881605970fd1f3c80eee94790056e51d452a226c624e52e4` |
| `FALSIFIERS-T3.csv` | 4554075 | `9527107f33172eaa4f8b88e44e8540c96e6a88d019e50b70b8c7c10ec6053405` |
| `independent/RECEIVER-WITNESSES.jsonl` | 7424900 | `a97b1d7754d41478ca6b75df08882e957343cb2c140f538e802edf2e5b0269f4` |
| `RECEIVER-SURVIVORS.csv` | 27 | `4aff7e615606d895172df212f146e85985104da0b0e2b0a74e8d0158363abd71` |

The complete comparison record and hashes of all retained run files are in `POSTRUN-NATIVE-COMPARISON.json`, SHA-256 `4ed7175f8f916058c28d39d9b376a880be697366f2bc1a34d16a8cddbcbdac8f`. Comparison completed at `2026-10-03T23:27:57.867410+00:00`.

This establishes exact agreement of the independently produced artifacts on this one recorded architecture. It does not itself complete the required x86_64/aarch64 gate, change a canonical status, or enlarge the fixed affine preparation/reader class. The mathematical nonexistence proof and its source-retention/physical limits remain as reviewed in REVIEW.md.
