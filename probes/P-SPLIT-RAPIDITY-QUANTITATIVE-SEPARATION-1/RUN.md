# RUN P-SPLIT-RAPIDITY-QUANTITATIVE-SEPARATION-1

## Immutable pin

```text
pin_commit: d3c964c2ca560f808a8d8062725d834edcefbf1c
prereg_sha256: 12dcb8993e557185ff2a447cdc7a525dd9cbc0f627a440f52bdde7285df4156e
prereg_bytes: 14761
prereg_blob: 10dbd95e22ae650bf6961b0931e27cdd69a5490c
verifier_sha256: c0d695a5e8d8e3d7f898a1cc8a983f798697385eadcae9590a1c384c17e026f3
verifier_bytes: 13817
verifier_blob: f58d1efd496ed5b26b61c8ebcb617344024bce92
expected_sha256: 8434f091256168113d468bad1009261a84a018458eb7eb65964244b7efad4751
expected_bytes: 1110
expected_blob: 020bf066cc185cb236d130067bf63506435f4caf
```

The public branch readback resolved to the full pin commit before execution.
The pin contains exactly `PREREG.md`, `verify.py`, and `EXPECTED.txt`; all three
Git blob identities above are from that commit.

## Command

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-SPLIT-RAPIDITY-QUANTITATIVE-SEPARATION-1/verify.py
```

Machine-readable command field:

```text
command: python3 probes/P-SPLIT-RAPIDITY-QUANTITATIVE-SEPARATION-1/verify.py
```

## Local formal leg

```text
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: Python 3.10.12
start_utc: 2026-08-12T21:51:19.642766504Z
finish_utc: 2026-08-12T21:51:20.975604663Z
wall_seconds: 1.32
deterministic_executions: 1
pre_status_bytes: 0
post_status_bytes: 0
exit_code: 0
stdout_sha256: 8434f091256168113d468bad1009261a84a018458eb7eb65964244b7efad4751
stdout_bytes: 1110
stdout_lines: 23
stdout_cr: 0
stdout_final_byte: 10
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
checks: 18 of 18 PASS
verdict: SURVIVED
```

The checkout was clean immediately before and after the single execution.
`EXPECTED.txt` is the exact raw stdout, with LF line endings and a final LF;
stderr is empty. The verifier uses exact integer arithmetic only and does not
claim to discharge either written universal quantifier by finite enumeration.

## Required GitHub leg

```text
status: PASS
workflow_run_id: 31644793485
job_id: 94275729943
job_url: https://github.com/mathorn1973/twist-j/actions/runs/31644793485/job/94275729943
check_name: architecture-aarch64
event: pull_request
tested_head_commit: a3ef784457eda0cf580694584782f9d27b7cf27a
checkout_merge_commit: a1188c611bd842c359272a3d5773acfe0f28c93b
base_commit: 84e7a81faaffa70d04398b4e535cf7b456624dc2
platform: Ubuntu 24.04.4 LTS GitHub-hosted runner image 20260719.67.1
architecture: aarch64
python: Python 3.12.13
check_step_log_start_utc: 2026-08-12T21:56:45.7402802Z
verify_pass_log_utc: 2026-08-12T21:56:48.3961725Z
verifier_sha256: c0d695a5e8d8e3d7f898a1cc8a983f798697385eadcae9590a1c384c17e026f3
stdout_sha256: 8434f091256168113d468bad1009261a84a018458eb7eb65964244b7efad4751
stdout_bytes: 1110
stdout_lines: 23
exit_code: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
byte_identity: PASS
replay: PASS
verdict: VERIFY PASS
```

The required clean GitHub aarch64 job reproduced the pinned verifier and
matched `EXPECTED.txt` byte for byte. Together with the accepted local x86_64
leg, this completes the public two-architecture gate before the Canon fold.
