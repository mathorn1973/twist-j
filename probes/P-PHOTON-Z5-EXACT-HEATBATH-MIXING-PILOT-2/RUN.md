# P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2 formal run record

Status: `PILOT_READY_FOR_PRODUCTION_PREREG / ZERO_PILOT_ONLY / PUBLIC
X86_64+AARCH64 REPRODUCTION PASS`.

## Immutable public pin

```text
pin_commit: b43ba8c33d244961783c0de42c89b7038fefe561
parent_commit: 5c2d469880828f29023e3cf592e86abbe352cd59
pin_tree: c5a758699b7e7538c56845a7f172eb527ef10980
public_issue: 755
pin_receipt: https://github.com/mathorn1973/twist-j/issues/755#issuecomment-5492100897
readback_receipt: https://github.com/mathorn1973/twist-j/issues/755#issuecomment-5492118152
pin_manifest_sha256: 07ee9dbd69f34875af1e7e1a1cf41e8284217e58c2807dfd57babcbc5e3bf6d2
pin_manifest_bytes: 1155
pin_entries: 14
verifier_sha256: 3857ca1e08ea027c86c6696dd78e80adff6bef8fe75bf939d071410c324896d1
```

The public branch ref, commit, parent, tree, all fifteen pre-run Git blobs and
the raw `SHA256SUMS` bytes were read back before execution. The public raw
manifest was 1,155 bytes and matched the local file byte for byte. No decision
artifact existed before that readback.

## Local formal leg

```text
command: python3 probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/verify.py
orchestration_command: python3 run_pilot.py
environment: LC_ALL=C LANG=C TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
platform: Ubuntu 22.04.5 LTS / Linux 6.6.87.2-microsoft-standard-WSL2
architecture: x86_64
python: CPython 3.10.12
compiler: g++ 11.4.0
boost_headers: libboost-dev 1.74.0.3ubuntu7
completed_at_utc: 2026-09-01T09:51:23Z
formal_runs: 1
runner_exit_code: 0
exit_code: 0
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stdout_bytes: 29872
stdout_lines: 182
stdout_sha256: 1ee2040148459d161264108598848c12c7dd8bfb744066a37d96f46bd137926a
result: PILOT_READY_FOR_PRODUCTION_PREREG
evidential_status: ZERO_PILOT_ONLY
architecture_gate: local x86_64 plus public GitHub x86_64 and aarch64 replays complete
```

The sole orchestration command first revalidated all pinned hashes, rebuilt the
C++ generator, reproduced the self-test, modeled STOP and independent C++/Python
fixtures, and then ran the eight frozen chains with at most four concurrent
workers. It invoked the canonical repository-root verifier child exactly once.
That child exited zero with empty stderr; its captured ASCII, LF-only stdout is
`EXPECTED.txt` byte for byte. The driver also exited zero. Neither the chains,
analyzer nor verifier were rerun after the terminal was produced.

## Raw and analysis custody

```text
raw_logs: 8
raw_samples: 4096
raw_bytes: 2978050
heatbath_decisions: 439418880
pilot_runs_sha256: 1e80dedab5c503836c7627de497aac908e7b6499c42e95db90ff08ff3e44bd81
pilot_runs_bytes: 1137
pilot_analysis_sha256: 3cf1bb420648757473646ecfbbd7c59dc35a020a1235a3f40c5b0ed52d364330
pilot_analysis_bytes: 28997
pilot_analysis_lines: 171
```

`PILOT_RUNS.tsv` contains its exact header and eight canonical rows. Every raw
log has 516 LF-only lines, exit zero, empty stderr, and the byte count and
SHA-256 recorded in that manifest. The frozen analyzer transcript is
byte-identical to the transcript embedded by the wrapper in `EXPECTED.txt`.

## Required GitHub leg

```text
status: PASS
workflow_run_id: 33496135026
workflow_url: https://github.com/mathorn1973/twist-j/actions/runs/33496135026
job_id: 99818654540
job_url: https://github.com/mathorn1973/twist-j/actions/runs/33496135026/job/99818654540
check_name: architecture-aarch64
event: pull_request
tested_head_commit: 0f5fbec4ba507b31ceb454e87166d39ed7f9edef
checkout_merge_commit: bec7f7efc0fd4f32ea8819e091d74cb6d5a2ea6f
base_commit: 54d35a41ad898a7877ca46272169194e1b5db023
platform: GitHub-hosted Ubuntu 24.04.4 LTS / ubuntu-24.04-arm 20260823.101.1
architecture: aarch64
python: CPython 3.12.14
verifier_sha256: 3857ca1e08ea027c86c6696dd78e80adff6bef8fe75bf939d071410c324896d1
stdout_sha256: 1ee2040148459d161264108598848c12c7dd8bfb744066a37d96f46bd137926a
stdout_bytes: 29872
stdout_lines: 182
exit_code: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
byte_identity: PASS
replay: PASS
verdict: VERIFY PASS
```

## Complete GitHub matrix receipts

```text
WORKFLOW = 33496135026
WORKFLOW_URL = https://github.com/mathorn1973/twist-j/actions/runs/33496135026
EVIDENCE_HEAD = 0f5fbec4ba507b31ceb454e87166d39ed7f9edef
TESTED_MERGE = bec7f7efc0fd4f32ea8819e091d74cb6d5a2ea6f
BASE_COMMIT = 54d35a41ad898a7877ca46272169194e1b5db023

X86_JOB = 99818654875
X86_JOB_URL = https://github.com/mathorn1973/twist-j/actions/runs/33496135026/job/99818654875
X86_RESULT = success
X86_PLATFORM = GitHub-hosted Ubuntu 24.04.4 LTS / ubuntu-24.04 20260823.283.1
X86_ARCH = x86_64
X86_PYTHON = CPython 3.12.14
X86_VERIFIER_SHA256 = 3857ca1e08ea027c86c6696dd78e80adff6bef8fe75bf939d071410c324896d1
X86_STDOUT_SHA256 = 1ee2040148459d161264108598848c12c7dd8bfb744066a37d96f46bd137926a
X86_STDOUT_BYTES = 29872
X86_STDOUT_LINES = 182
X86_BYTE_IDENTITY = PASS

ARM_JOB = 99818654540
ARM_JOB_URL = https://github.com/mathorn1973/twist-j/actions/runs/33496135026/job/99818654540
ARM_RESULT = success
ARM_PLATFORM = GitHub-hosted Ubuntu 24.04.4 LTS / ubuntu-24.04-arm 20260823.101.1
ARM_ARCH = aarch64
ARM_PYTHON = CPython 3.12.14
ARM_VERIFIER_SHA256 = 3857ca1e08ea027c86c6696dd78e80adff6bef8fe75bf939d071410c324896d1
ARM_STDOUT_SHA256 = 1ee2040148459d161264108598848c12c7dd8bfb744066a37d96f46bd137926a
ARM_STDOUT_BYTES = 29872
ARM_STDOUT_LINES = 182
ARM_BYTE_IDENTITY = PASS

AGGREGATE_JOB = 99818770578
AGGREGATE_JOB_URL = https://github.com/mathorn1973/twist-j/actions/runs/33496135026/job/99818770578
AGGREGATE_RESULT = success
AGGREGATE_TERMINAL = TWO-ARCHITECTURE CHECK PASS
```

Both public jobs checked out the signed synthetic merge commit
`bec7f7efc0fd4f32ea8819e091d74cb6d5a2ea6f`, whose parents are the policy base
`54d35a41ad898a7877ca46272169194e1b5db023` and evidence head
`0f5fbec4ba507b31ceb454e87166d39ed7f9edef`. Policy, all 148 tool tests,
Canon v74, Ledger and the gate contract passed before the unchanged verifier
reproduced `EXPECTED.txt` byte for byte on both architectures.
