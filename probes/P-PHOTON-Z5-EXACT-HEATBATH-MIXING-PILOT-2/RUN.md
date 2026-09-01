# P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2 formal run record

Status: one authorized local pilot execution complete; public architecture
replay pending.

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
```

The public branch ref, commit, parent, tree, all fifteen pre-run Git blobs and
the raw `SHA256SUMS` bytes were read back before execution. The public raw
manifest was 1,155 bytes and matched the local file byte for byte. No decision
artifact existed before that readback.

## Local execution record

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
verifier_sha256: 3857ca1e08ea027c86c6696dd78e80adff6bef8fe75bf939d071410c324896d1
stdout_bytes: 29872
stdout_lines: 182
stdout_sha256: 1ee2040148459d161264108598848c12c7dd8bfb744066a37d96f46bd137926a
result: PILOT_READY_FOR_PRODUCTION_PREREG
evidential_status: ZERO_PILOT_ONLY
architecture_gate: local x86_64 complete; required GitHub x86_64 and aarch64 replays pending
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

Public pull-request replays on Linux x86_64 and native aarch64 remain pending
at the time of this first run record.
