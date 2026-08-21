# P-CARRY-QUADRATIC-SYMMETRY-1 formal run record

Date: 2026-08-21

Status: local formal record. The public two-architecture gate is completed only by the repository pull-request workflow, which reruns the pinned verifier on x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

```text
pin_commit: 6229acdeb8bce1afca61c8f4202821c1ebb2e5d0
verifier_sha256: b03ae613dec89f9a46b9668969ab80c1620c82bf0f96e5ee16d8e8191426f101
command: python3 probes/P-CARRY-QUADRATIC-SYMMETRY-1/verify.py
platform: Debian 13
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: 001d554f7d9e365949de3a452df56f8b3fd5fa9ce15f3f1362d9db2fbf90453a
stdout_bytes: 535
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
base_commit: 4d8558356f2f945b34e9f7fece323771d266585a
pre_pin_prereg_only: 2346374fc5387f1bfc7e86877fef6206e7687766
pin_tree: 2d855b0994b14c5c12a6db9b4e9b8ba4cb176967
probe_tree: 5a739c8badca623828f65236970d8ae33a85e1b3
prereg_blob: cbabf37a450edcd5c1849bbf64b61900975194b1
verify_blob: ed426425311ce06466701ab64d8f0bce8580f9af
```

The accepted verifier bytes were read from the public pin and independently re-materialized before execution. Their Git blob id matched `ed426425311ce06466701ab64d8f0bce8580f9af` and their SHA-256 matched the flat record above.

One earlier invocation through the ChatGPT Python wrapper is explicitly rejected as a formal leg: before verifier code ran, that wrapper wrote an unrelated spreadsheet-runtime warmup failure to stderr. The verifier itself returned the same 8/8 stdout, but the process failed the frozen empty-stderr requirement. No pinned byte changed and no mathematical falsifier fired. The accepted local leg used the system CPython binary without that wrapper and wrote zero stderr bytes.

## Accepted local result

```text
checks: 8/8 ALL PASS
unique_pure_quadratic: e_2
least_weight_period: 4
first_nonatomic_singular_arity: 4
P_4_cardinality: 5
Aut_q4_order: 120
full_symmetric_action: yes
scope: L1 finite/binary arithmetic only
```
