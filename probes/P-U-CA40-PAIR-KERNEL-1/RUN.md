# First completed exact run

PUBLIC NON-CANONICAL. Original text Apache-2.0.

```text
pin_commit: 179199a8972187edb70f576ae4af8aa9078805d2
verifier_sha256: a2033a585be759a7e65ae726a6a942cba00ad94ad774f231bd758c94bedcc850
command: python3 probes/P-U-CA40-PAIR-KERNEL-1/verify.py
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: f6361b1543bf3de9841806e51c3ddd35329e11ae69f8cd21b7158de0cd931290
stdout_bytes: 1532
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

All six candidate files were publicly read back byte for byte at 2026-10-10T16:26:19.933740+00:00, before scientific execution. The preregistration SHA-256 is `53d061e08163cf03d95392bc0981ddb8f726cdc399bb4dd8a069a03cb78b924e`. A clean checkout of the immutable pin and every source manifest hash were checked on the execution system.

The first formal exact run started at 2026-10-10T18:11:03.042815+00:00 and completed at 2026-10-10T18:11:05.661816+00:00; the coordinator observed 2.619008 seconds under the frozen 600-second limit. The original stdout is EXPECTED.txt. No outcome-dependent rerun preceded this record.

The floating benchmark has separate measurements and custody in ENGINEERING.md. Required x86_64 and aarch64 replay is determined by the repository workflow on the reviewed PR head; no workflow outcome is inferred from this local run.

A subsequent Windows replay failed the byte-comparison gate because its stdout uses CRLF. Its SHA-256, `9a142c5851f7250361094f5cc1c09ef6ad8d8b9f78b75b3509d4b838cb6e05b6`, exactly equals EXPECTED.txt with its single LF replaced by CRLF (1533 bytes). The Linux original and pinned verifier remain unchanged. Windows byte portability is not claimed; required workflow replay uses Linux on both architectures.
